"""Load lesson markdown, chunk, BM25 retrieve, and call OpenAI with grounded context."""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import streamlit as st
from openai import APIConnectionError, APIStatusError, AuthenticationError, OpenAI, RateLimitError
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


@st.cache_data(show_spinner=False)
def load_topics_manifest() -> list[dict[str, Any]]:
    topics: list[dict[str, Any]] = []
    path = CONTENT_DIR / "topics.json"
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        topics.extend(list(data.get("topics", [])))

    if NOTEBOOKS_MD_DIR.is_dir():
        for md in sorted(NOTEBOOKS_MD_DIR.glob("*.md")):
            label = re.sub(r"[_-]+", " ", md.stem).strip()
            topics.append(
                {
                    "id": f"nb-{md.stem.lower()}",
                    "title": f"Notebook: {label}",
                    "file": f"notebooks_md/{md.name}",
                }
            )
    return topics


def _iter_markdown_files() -> list[Path]:
    files = sorted(CONTENT_DIR.glob("*.md"))
    if NOTEBOOKS_MD_DIR.is_dir():
        files.extend(sorted(NOTEBOOKS_MD_DIR.glob("*.md")))
    return files


@st.cache_data(show_spinner=False)
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


def _normalize_openai_key(raw: str) -> str:
    """Fix common copy/paste mistakes from Secrets or .env."""
    s = raw.strip().replace("\n", "").replace("\r", "").lstrip("\ufeff")
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1].strip()
    if s.lower().startswith("bearer "):
        s = s[6:].strip()
    return s


def _optional_secret(*names: str) -> str | None:
    """Read first non-empty setting from Streamlit secrets, then environment."""
    for name in names:
        try:
            v = st.secrets.get(name)
            if v is not None and str(v).strip():
                s = _normalize_openai_key(str(v))
                if s:
                    return s
        except (FileNotFoundError, RuntimeError, AttributeError, KeyError, TypeError):
            pass
    import os

    for name in names:
        e = os.environ.get(name)
        if e and e.strip():
            s = _normalize_openai_key(e)
            if s:
                return s
    return None


def _openai_client() -> OpenAI:
    api_key = get_openai_key()
    if not api_key:
        raise RuntimeError("missing API key")
    kwargs: dict[str, str] = {"api_key": api_key}
    org = _optional_secret("OPENAI_ORGANIZATION", "OPENAI_ORG_ID")
    project = _optional_secret("OPENAI_PROJECT", "OPENAI_PROJECT_ID")
    if org:
        kwargs["organization"] = org
    if project:
        kwargs["project"] = project
    return OpenAI(**kwargs)


def get_openai_key() -> str | None:
    try:
        k = st.secrets.get("OPENAI_API_KEY")
        if k:
            s = _normalize_openai_key(str(k))
            if s and s not in ('""', "''", "sk-your-key-here", "your-key-here"):
                return s
    except (FileNotFoundError, RuntimeError, AttributeError):
        pass
    import os

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
    """Short hint that a key loaded (not the full secret)."""
    k = get_openai_key()
    if not k or len(k) < 12:
        return None
    return f"{k[:7]}…{k[-4:]} ({len(k)} characters)"


def ping_openai_api() -> tuple[bool, str]:
    """One minimal completion to verify the key. Does not expose the key."""
    if not get_openai_key():
        return False, "No API key loaded. Add OPENAI_API_KEY to Streamlit Secrets (or .env locally)."
    try:
        client = _openai_client()
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "ok"}],
            max_tokens=1,
        )
        return True, "OpenAI accepted the key — billing and model access are working."
    except AuthenticationError:
        return False, (
            "401 invalid API key — OpenAI rejected the key. Create a new secret key, "
            "confirm billing is active for that organization, paste into Secrets, Save, Reboot."
        )
    except APIStatusError as e:
        code = getattr(e, "status_code", None)
        if code == 401:
            return False, (
                "401 — Check the key, billing, and (if applicable) OPENAI_ORGANIZATION / OPENAI_PROJECT in Secrets."
            )
        if code == 429:
            return (
                True,
                "Your API key is valid. OpenAI returned 429 (rate limit): wait 2–5 minutes, "
                "then try again. Repeated “Test” clicks or a busy public app can hit limits quickly.",
            )
        return False, f"OpenAI HTTP {code}. Open Manage app → Logs for details."
    except RateLimitError:
        return (
            True,
            "Your API key is valid. Rate limit (429): wait a few minutes before more API calls.",
        )
    except APIConnectionError:
        return False, "Network error — could not reach OpenAI."
    except Exception:
        return False, "Request failed — see Manage app → Logs."


def _chat_completions_with_retry(client: OpenAI, **kwargs: Any):
    """Retry on 429 with backoff; re-raise other errors."""
    delays = (2.0, 5.0, 12.0)
    last_exc: BaseException | None = None
    for attempt in range(len(delays) + 1):
        try:
            return client.chat.completions.create(**kwargs)
        except RateLimitError as e:
            last_exc = e
        except APIStatusError as e:
            if getattr(e, "status_code", None) != 429:
                raise
            last_exc = e
        if attempt < len(delays):
            time.sleep(delays[attempt])
            continue
        raise last_exc  # type: ignore[misc]


def chat_answer(
    user_message: str,
    history: list[dict[str, str]],
) -> str:
    api_key = get_openai_key()
    if not api_key:
        return (
            "**OpenAI is not configured.** The tutor needs a real API key (not empty).\n\n"
            "- **Streamlit Cloud:** *Manage app* → *Settings* → *Secrets* → set "
            "`OPENAI_API_KEY = \"sk-...\"` → *Save* → *Reboot*.\n"
            "- **On your PC:** create `.streamlit/secrets.toml` or a `.env` file in the project "
            "with `OPENAI_API_KEY=sk-...`.\n"
            "- Get a key: [platform.openai.com/api-keys](https://platform.openai.com/api-keys) "
            "(requires an OpenAI account and billing/credits)."
        )

    if not api_key.startswith("sk-"):
        return (
            "**OPENAI_API_KEY does not look like an OpenAI API key.** "
            "It should start with `sk-` or `sk-proj-` from "
            "[API keys](https://platform.openai.com/api-keys) — not your ChatGPT login password."
        )

    context = retrieve_context(user_message)
    system = (
        "You are **Pyseed**, a friendly beginner Python tutor. "
        "Answer using ONLY the lesson excerpts below. "
        "If the excerpts do not contain enough information, say so clearly and suggest "
        "which topic the learner might open in Static mode. "
        "Keep answers concise and use simple examples when helpful.\n\n"
        f"### Lesson excerpts\n{context or '(No excerpts retrieved — corpus may be empty.)'}"
    )

    try:
        client = _openai_client()
    except RuntimeError:
        return (
            "**OpenAI is not configured.** Add `OPENAI_API_KEY` to Secrets and reboot the app."
        )

    messages: list[dict[str, str]] = [{"role": "system", "content": system}]
    for turn in history[-10:]:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": user_message})

    auth_help = (
        "**OpenAI rejected the request** (authentication failed — HTTP 401).\n\n"
        "**Most common fixes**\n\n"
        "1. Use an **API key**, not your ChatGPT password. Create one at "
        "[platform.openai.com/api-keys](https://platform.openai.com/api-keys).\n"
        "2. Turn on **billing** for the same org as the key: "
        "[Billing overview](https://platform.openai.com/settings/organization/billing/overview). "
        "Without credits or a card, API calls return 401.\n"
        "3. In Streamlit **Secrets**, use straight ASCII quotes, one line, e.g. "
        "`OPENAI_API_KEY = \"sk-proj-...\"` → **Save** → **Reboot** the app.\n"
        "4. If your company uses **Organizations / Projects**, add optional lines (same Secrets file):\n"
        "   `OPENAI_ORGANIZATION = \"org-...\"`\n"
        "   `OPENAI_PROJECT = \"proj_...\"`  \n"
        "   (IDs appear in the OpenAI dashboard URL or project settings.)\n\n"
        "5. **Create a brand-new key**, paste it in Secrets, save, reboot. Revoke the old key if unsure.\n\n"
        "**Still stuck?** Open *Manage app* → *Logs* and look for `401` / `invalid_api_key` next to the redacted line."
    )

    try:
        resp = _chat_completions_with_retry(
            client,
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=900,
        )
    except AuthenticationError:
        return auth_help
    except APIStatusError as e:
        if getattr(e, "status_code", None) == 401:
            return auth_help
        if getattr(e, "status_code", None) == 429:
            return (
                "**OpenAI rate limit (429)** — still throttled after automatic retries. "
                "Wait **5–15 minutes**, avoid spamming the Test button, and check "
                "[limits](https://platform.openai.com/settings/organization/limits). "
                "A **public** app can burn through free-tier RPM quickly."
            )
        return (
            f"**OpenAI API error** (HTTP {getattr(e, 'status_code', '?')}). "
            "Open *Manage app* → logs for details, or try again later."
        )
    except RateLimitError:
        return (
            "**OpenAI rate limit (429)** — wait several minutes and retry. "
            "Too many requests from this app or account in a short window."
        )
    except APIConnectionError:
        return "**Could not reach OpenAI.** Check network / VPN, or try again in a few minutes."

    return (resp.choices[0].message.content or "").strip()


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
