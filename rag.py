"""Load lesson markdown, chunk, BM25 retrieve, and optionally call OpenAI."""

from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generator

import streamlit as st
from rank_bm25 import BM25Okapi

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
NOTEBOOKS_MD_DIR = CONTENT_DIR / "notebooks_md"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


@dataclass
class Chunk:
    text: str
    source: str


def _split_markdown_chunks(text: str, source: str, max_chars: int = 1200) -> list[Chunk]:
    parts = re.split(r"(?m)^#{1,3}\s+.+\s*$", text)
    chunks: list[Chunk] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) <= max_chars:
            chunks.append(Chunk(part, source))
            continue
        start = 0
        while start < len(part):
            chunks.append(Chunk(part[start : start + max_chars], source))
            start += max_chars
    return chunks


def _notebook_sort_key(path: Path) -> tuple[int, str]:
    stem = path.stem
    if re.match(r"an?[_\-]intro", stem, re.IGNORECASE) or "introduction" in stem.lower():
        return (0, stem)
    m = re.match(r"^(\d+)", stem)
    if m:
        return (int(m.group(1)), stem)
    return (999, stem)


def _sorted_notebooks(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.md"), key=_notebook_sort_key)


@st.cache_data(show_spinner=False, ttl=3600)
def load_topics_manifest() -> list[dict[str, Any]]:
    topics: list[dict[str, Any]] = []
    path = CONTENT_DIR / "topics.json"
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        topics.extend(list(data.get("topics", [])))

    if NOTEBOOKS_MD_DIR.is_dir():
        for md in _sorted_notebooks(NOTEBOOKS_MD_DIR):
            stem = md.stem
            if re.match(r"^(\d+)", stem):
                num_match = re.match(r"^(\d+)[_\-]?(.*)", stem)
                if num_match:
                    num = num_match.group(1)
                    rest = re.sub(r"[_-]+", " ", num_match.group(2)).strip()
                    label = f"{num}. {rest.title()}"
                else:
                    label = re.sub(r"[_-]+", " ", stem).strip().title()
            elif "introduction" in stem.lower():
                label = "Introduction to Python Programming"
            else:
                label = re.sub(r"[_-]+", " ", stem).strip().title()

            topics.append(
                {
                    "id": f"nb-{md.stem.lower()}",
                    "title": label,
                    "file": f"notebooks_md/{md.name}",
                }
            )
    return topics


def _iter_markdown_files() -> list[Path]:
    files = list(sorted(CONTENT_DIR.glob("*.md")))
    if NOTEBOOKS_MD_DIR.is_dir():
        files.extend(_sorted_notebooks(NOTEBOOKS_MD_DIR))
    return files


@st.cache_resource(show_spinner=False)
def load_all_chunks() -> tuple[list[Chunk], BM25Okapi | None]:
    chunks: list[Chunk] = []
    for md in _iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        chunks.extend(_split_markdown_chunks(text, md.relative_to(CONTENT_DIR).as_posix()))
    if not chunks:
        return [], None
    corpus = [tokenize(c.text) for c in chunks]
    bm25 = BM25Okapi(corpus)
    return chunks, bm25


def retrieve_context(query: str, k: int = 6) -> str:
    chunks, bm25 = load_all_chunks()
    if not chunks or bm25 is None:
        return ""
    q = tokenize(query)
    if not q:
        return ""
    scores = bm25.get_scores(q)
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    excerpts = []
    for i in ranked:
        excerpts.append(f"--- From `{chunks[i].source}` ---\n{chunks[i].text}")
    return "\n\n".join(excerpts)


def _retrieve_top_chunks(query: str, k: int = 4) -> list[tuple[Chunk, float]]:
    chunks, bm25 = load_all_chunks()
    if not chunks or bm25 is None:
        return []
    q = tokenize(query)
    if not q:
        return []
    scores = bm25.get_scores(q)
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    return [(chunks[i], float(scores[i])) for i in ranked]


def _source_label(source: str) -> str:
    stem = Path(source).stem
    if re.match(r"^(\d+)", stem):
        m = re.match(r"^(\d+)[_\-]?(.*)", stem)
        if m:
            num = m.group(1)
            rest = re.sub(r"[_-]+", " ", m.group(2)).strip().title()
            return f"Notebook {num}: {rest}"
    if "introduction" in stem.lower():
        return "Introduction to Python Programming"
    return re.sub(r"[_-]+", " ", stem).strip().title()


def _bm25_only_answer(query: str) -> str:
    """Answer purely from notebook content using BM25. No external API needed."""
    results = _retrieve_top_chunks(query, k=3)
    if not results:
        return (
            "Sorry, I am beginner level AI and I could not find anything in the notebooks. "
            "Please try browsing the **Static mode** to read the lessons directly."
        )

    top_score = results[0][1]

    if top_score < 0.5:
        return (
            "Sorry, I am beginner level AI — I could not find a good answer to that question "
            "in the lesson notebooks. Try rephrasing with Python keywords, or browse the "
            "**Static mode** to read the lessons directly."
        )

    parts: list[str] = []
    seen_sources: set[str] = set()

    for chunk, score in results:
        if score < 0.3:
            break
        label = _source_label(chunk.source)
        text = chunk.text.strip()
        if not text:
            continue
        if label not in seen_sources:
            seen_sources.add(label)
            parts.append(f"**From: {label}**\n\n{text}")
        else:
            parts.append(text)

    if not parts:
        return (
            "Sorry, I am beginner level AI — I could not find a relevant answer in the notebooks. "
            "Try browsing **Static mode** for the full lessons."
        )

    answer = "\n\n---\n\n".join(parts)
    answer += (
        "\n\n---\n*This answer is taken directly from your lesson notebooks. "
        "For a deeper explanation, open the topic in **Static mode**.*"
    )
    return answer


def _normalize_openai_key(raw: str) -> str:
    s = raw.strip().replace("\n", "").replace("\r", "").lstrip("\ufeff")
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1].strip()
    if s.lower().startswith("bearer "):
        s = s[6:].strip()
    return s


def _optional_secret(*names: str) -> str | None:
    for name in names:
        try:
            v = st.secrets.get(name)
            if v is not None and str(v).strip():
                s = _normalize_openai_key(str(v))
                if s:
                    return s
        except (FileNotFoundError, RuntimeError, AttributeError, KeyError, TypeError):
            pass
    for name in names:
        e = os.environ.get(name)
        if e and e.strip():
            s = _normalize_openai_key(e)
            if s:
                return s
    return None


@st.cache_resource(show_spinner=False)
def _get_openai_client_cached(api_key: str, org: str | None, project: str | None):
    from openai import OpenAI
    kwargs: dict[str, str] = {"api_key": api_key}
    if org:
        kwargs["organization"] = org
    if project:
        kwargs["project"] = project
    return OpenAI(**kwargs)


def _openai_client():
    api_key = get_openai_key()
    if not api_key:
        raise RuntimeError("missing API key")
    org = _optional_secret("OPENAI_ORGANIZATION", "OPENAI_ORG_ID")
    project = _optional_secret("OPENAI_PROJECT", "OPENAI_PROJECT_ID")
    return _get_openai_client_cached(api_key, org, project)


def get_openai_key() -> str | None:
    try:
        k = st.secrets.get("OPENAI_API_KEY")
        if k:
            s = _normalize_openai_key(str(k))
            if s and s not in ('""', "''", "sk-your-key-here", "your-key-here"):
                return s
    except (FileNotFoundError, RuntimeError, AttributeError):
        pass

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    v = _normalize_openai_key(os.environ.get("OPENAI_API_KEY", ""))
    if v and v not in ('""', "sk-your-key-here"):
        return v
    return None


def openai_key_fingerprint() -> str | None:
    k = get_openai_key()
    if not k or len(k) < 12:
        return None
    return f"{k[:7]}…{k[-4:]} ({len(k)} characters)"


def ping_openai_api() -> tuple[bool, str]:
    from openai import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError
    if not get_openai_key():
        return False, "No API key loaded."
    try:
        client = _openai_client()
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "ok"}],
            max_tokens=1,
        )
        return True, "OpenAI accepted the key — billing and model access are working."
    except AuthenticationError:
        return False, "401 invalid API key — check billing at platform.openai.com."
    except APIStatusError as e:
        code = getattr(e, "status_code", None)
        if code == 429:
            return True, "Key is valid. OpenAI returned 429 (rate limit) — wait a few minutes."
        return False, f"OpenAI HTTP {code}."
    except RateLimitError:
        return True, "Key valid. Rate limit — wait a few minutes."
    except APIConnectionError:
        return False, "Network error — could not reach OpenAI."
    except Exception:
        return False, "Request failed — see Manage app → Logs."


def chat_answer_stream(
    user_message: str,
    history: list[dict[str, str]],
) -> Generator[str, None, None]:
    from openai import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError

    api_key = get_openai_key()

    if not api_key:
        yield _bm25_only_answer(user_message)
        return

    if not api_key.startswith("sk-"):
        yield (
            "**OPENAI_API_KEY does not look like a valid key.** "
            "It should start with `sk-` or `sk-proj-`."
        )
        return

    context = retrieve_context(user_message)
    system = (
        "You are **Pyseed**, a friendly beginner Python tutor. "
        "Answer using the lesson excerpts below as your primary source. "
        "If the excerpts do not contain enough information to answer the question, "
        "respond with exactly: 'Sorry I am beginner level AI' and suggest the learner "
        "browse the relevant topic in Static mode. "
        "Keep answers concise and use simple examples when helpful.\n\n"
        f"### Lesson excerpts\n{context or '(No excerpts retrieved.)'}"
    )

    try:
        client = _openai_client()
    except RuntimeError:
        yield _bm25_only_answer(user_message)
        return

    messages: list[dict[str, str]] = [{"role": "system", "content": system}]
    for turn in history[-10:]:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": user_message})

    auth_help = (
        "**OpenAI rejected the request (401).**\n\n"
        "Fixes:\n"
        "1. Use an API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).\n"
        "2. Ensure billing is active for that key's organisation.\n"
        "3. In Secrets: `OPENAI_API_KEY = \"sk-proj-...\"` → **Save** → **Reboot**.\n\n"
        "*Tip: Remove the key entirely to use the free notebook-based mode.*"
    )

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=900,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                yield delta
    except AuthenticationError:
        yield auth_help
    except APIStatusError as e:
        code = getattr(e, "status_code", None)
        if code == 401:
            yield auth_help
        elif code == 429:
            yield "**OpenAI rate limit (429)** — wait 5–15 minutes and try again."
        else:
            yield f"**OpenAI API error** (HTTP {code})."
    except RateLimitError:
        yield "**OpenAI rate limit (429)** — wait several minutes and retry."
    except APIConnectionError:
        yield "**Could not reach OpenAI.** Falling back to notebook search...\n\n" + _bm25_only_answer(user_message)
    except Exception as exc:
        yield f"**Unexpected error:** {exc}"


def chat_answer(user_message: str, history: list[dict[str, str]]) -> str:
    return "".join(chat_answer_stream(user_message, history))


def read_topic_file(filename: str) -> str:
    if not filename or ".." in filename:
        return "*Invalid topic file.*"
    rel = Path(filename.replace("\\", "/"))
    path = (CONTENT_DIR / rel).resolve()
    content_root = CONTENT_DIR.resolve()
    if (
        not path.is_file()
        or path == content_root
        or content_root not in path.parents
    ):
        return "*Topic file not found.*"
    return path.read_text(encoding="utf-8")
