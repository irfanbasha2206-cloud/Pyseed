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


# ── Notebook markdown preprocessor ────────────────────────────────────────────

def preprocess_notebook_md(text: str) -> str:
    """
    Jupyter notebooks converted to markdown have Python docstrings ('''...''')
    inside ```python``` code blocks that contain prose, tables, and explanations.
    This function extracts those and renders them as proper markdown so Streamlit
    shows tables as HTML tables, bold text as bold, etc.
    """

    def process_code_block(m: re.Match) -> str:
        block = m.group(1)

        # Check if there is any real Python code (not just comments and docstrings)
        stripped = block
        stripped = re.sub(r"'''.*?'''", "", stripped, flags=re.DOTALL)
        stripped = re.sub(r'""".*?"""', "", stripped, flags=re.DOTALL)
        stripped = re.sub(r"^#[^\n]*\n?", "", stripped, flags=re.MULTILINE)
        has_real_code = bool(stripped.strip())

        if has_real_code:
            return m.group(0)  # keep real code blocks as-is

        # No real code — extract and render as markdown
        result: list[str] = []
        last_pos = 0

        for dm in re.finditer(r"'''(.*?)'''", block, re.DOTALL):
            before = block[last_pos : dm.start()]
            for line in before.splitlines():
                ln = line.strip()
                if ln.startswith("#"):
                    heading = ln.lstrip("#").strip()
                    if heading:
                        result.append(f"\n#### {heading}\n\n")
            content = dm.group(1).strip()
            if content:
                result.append(content + "\n\n")
            last_pos = dm.end()

        after = block[last_pos:]
        for line in after.splitlines():
            ln = line.strip()
            if ln.startswith("#"):
                heading = ln.lstrip("#").strip()
                if heading:
                    result.append(f"\n#### {heading}\n\n")

        return "\n" + "".join(result) + "\n"

    processed = re.sub(r"```python\n?(.*?)```", process_code_block, text, flags=re.DOTALL)
    processed = re.sub(r"^\s*'''\s*$", "", processed, flags=re.MULTILINE)
    processed = re.sub(r"\n{4,}", "\n\n\n", processed)
    return processed


# ── Tokenisation & chunks ──────────────────────────────────────────────────────

def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


@dataclass
class Chunk:
    text: str
    source: str


def _split_markdown_chunks(text: str, source: str, max_chars: int = 1000) -> list[Chunk]:
    parts = re.split(r"(?m)^#{1,4}\s+.+\s*$", text)
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
        raw = md.read_text(encoding="utf-8")
        text = preprocess_notebook_md(raw)
        chunks.extend(_split_markdown_chunks(text, md.relative_to(CONTENT_DIR).as_posix()))
    if not chunks:
        return [], None
    corpus = [tokenize(c.text) for c in chunks]
    bm25 = BM25Okapi(corpus)
    return chunks, bm25


# ── BM25 retrieval with title boost ───────────────────────────────────────────

def _title_boost(query_tokens: set[str], source: str) -> float:
    """
    Give a score multiplier to chunks whose notebook title overlaps with the query.
    Uses *query coverage* (how much of the query is in the title) so a single-word
    query like 'variables' that fully matches the title 'variables_and_datatypes'
    gets the maximum boost, while off-topic notebooks get no boost.
    """
    stem = Path(source).stem
    stem_clean = re.sub(r"^\d+[_\-]?", "", stem)
    title_tokens = set(tokenize(stem_clean))
    if not title_tokens or not query_tokens:
        return 1.0
    overlap = query_tokens & title_tokens
    if not overlap:
        return 1.0
    # fraction of QUERY words found in the notebook title
    query_coverage = len(overlap) / len(query_tokens)
    if query_coverage >= 1.0:
        return 12.0   # every query word is in the title → overwhelming boost
    if query_coverage >= 0.5:
        return 6.0
    return 2.5


def retrieve_context(query: str, k: int = 5) -> str:
    chunks, bm25 = load_all_chunks()
    if not chunks or bm25 is None:
        return ""
    q = tokenize(query)
    if not q:
        return ""
    q_set = set(q)
    scores = bm25.get_scores(q)
    boosted = [scores[i] * _title_boost(q_set, chunks[i].source) for i in range(len(chunks))]
    ranked = sorted(range(len(boosted)), key=lambda i: boosted[i], reverse=True)[:k]
    excerpts = []
    for i in ranked:
        excerpts.append(f"--- From `{chunks[i].source}` ---\n{chunks[i].text}")
    return "\n\n".join(excerpts)


def _retrieve_top_chunks(query: str, k: int = 3) -> list[tuple[Chunk, float]]:
    chunks, bm25 = load_all_chunks()
    if not chunks or bm25 is None:
        return []
    q = tokenize(query)
    if not q:
        return []
    q_set = set(q)
    scores = bm25.get_scores(q)
    boosted = [scores[i] * _title_boost(q_set, chunks[i].source) for i in range(len(chunks))]
    ranked = sorted(range(len(boosted)), key=lambda i: boosted[i], reverse=True)[:k]
    return [(chunks[i], float(boosted[i])) for i in ranked]


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


def _clean_chunk_text(text: str) -> str:
    """Strip raw Python docstring markers and tidy whitespace from a chunk."""
    text = text.strip()
    # Remove ''' delimiters left over from raw notebook markdown
    text = re.sub(r"^\s*'''\s*", "", text)
    text = re.sub(r"\s*'''\s*$", "", text)
    text = re.sub(r"'''", "", text)
    # Remove lone '#' comment lines that have no content
    text = re.sub(r"(?m)^#\s*$", "", text)
    # Collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _bm25_only_answer(query: str) -> str:
    """
    Answer from the single best-matching notebook only.
    No notebook name label, no cross-notebook pollution.
    """
    # Retrieve more candidates so we get several chunks from the top notebook
    results = _retrieve_top_chunks(query, k=10)
    if not results:
        return (
            "Sorry, I am beginner level AI — I could not find anything in the notebooks. "
            "Please try browsing **Static mode** to read the lessons directly."
        )

    top_score = results[0][1]

    # Very low score → likely a misspelling
    if top_score < 0.15:
        return (
            "❗ **Check your word and enter the correct spelling.**\n\n"
            "I could not find any matching lesson content. "
            "Try a Python keyword like `variables`, `loops`, `functions`, or `OOP`."
        )

    if top_score < 0.5:
        return (
            "Sorry, I am beginner level AI — I could not find a good answer to that in the lessons. "
            "Try rephrasing with Python keywords, or browse **Static mode** to read the lessons."
        )

    # Only use chunks from the single top-scoring notebook
    top_source = results[0][0].source
    min_score = max(top_score * 0.25, 0.3)
    top_chunks = [
        chunk for chunk, score in results
        if chunk.source == top_source and score >= min_score
    ]

    if not top_chunks:
        top_chunks = [results[0][0]]

    # Build clean answer — definitions and examples only, no notebook name
    parts: list[str] = []
    for chunk in top_chunks:
        text = _clean_chunk_text(chunk.text)
        if text:
            parts.append(text)

    if not parts:
        return (
            "Sorry, I am beginner level AI — no relevant answer found in the notebooks. "
            "Try browsing **Static mode** for the full lessons."
        )

    return "\n\n".join(parts)


# ── OpenAI helpers ─────────────────────────────────────────────────────────────

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
        "Answer using ONLY the lesson excerpts below as your source. "
        "If the question asks for a definition, answer with a clear definition, and when available include the exact notebook wording. "
        "Do not add any information that is not present in the excerpts. "
        "If the excerpts do not contain enough information, respond with: "
        "'Sorry I am beginner level AI' and suggest browsing Static mode. "
        "Keep answers precise and definition-focused.\n\n"
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
        "1. Use an API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).\n"
        "2. Ensure billing is active.\n"
        "3. In Secrets: `OPENAI_API_KEY = \"sk-proj-...\"` → **Save** → **Reboot**.\n\n"
        "*Tip: Remove the key to use free notebook-search mode instead.*"
    )

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=700,
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
        yield "**Could not reach OpenAI.** Falling back...\n\n" + _bm25_only_answer(user_message)
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
    raw = path.read_text(encoding="utf-8")
    return preprocess_notebook_md(raw)
