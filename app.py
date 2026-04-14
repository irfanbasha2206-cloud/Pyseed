"""
Pyseed — Streamlit entry: login, dashboard (AI / Static), RAG chat, static topics.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure sibling modules resolve on Streamlit Cloud (Linux) and odd cwd cases.
_APP_DIR = Path(__file__).resolve().parent
_root = str(_APP_DIR)
if _root not in sys.path:
    sys.path.insert(0, _root)

import streamlit as st

from seed_auth import ensure_session_keys, logout, render_login
from rag import (
    chat_answer_stream,
    get_openai_key,
    load_topics_manifest,
    openai_key_fingerprint,
    ping_openai_api,
    read_topic_file,
)
from ui import LOGO_PATH, inject_css, mode_card_html, render_app_header, render_landing_brand


def _page_icon() -> str:
    if LOGO_PATH.is_file() and LOGO_PATH.suffix.lower() in (".png", ".ico"):
        return str(LOGO_PATH)
    return "🌱"


def _dashboard() -> None:
    st.subheader("Welcome")
    st.caption(f"Signed in as **{st.session_state.display_name}** — pick a mode below.")
    st.markdown(
        mode_card_html(
            "AI mode",
            "Ask questions; answers are grounded in the markdown lessons in `content/`.",
            "✨",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        mode_card_html(
            "Static mode",
            "Browse topics as expandable sections — great for reading in order.",
            "📚",
        ),
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Open AI mode", type="primary", use_container_width=True):
            st.session_state.view = "ai"
            st.rerun()
    with c2:
        if st.button("Open static mode", type="primary", use_container_width=True):
            st.session_state.view = "static"
            st.rerun()


def _ai_view() -> None:
    st.subheader("ASK Python related questions")
    st.caption(
        "The tutor uses **your** lesson files under `content/` as context (simple BM25 search + OpenAI). "
        "If something is not in the lessons, it should say so."
    )
    if not get_openai_key():
        st.warning(
            "**AI mode needs a real OpenAI key.** "
            "An empty `OPENAI_API_KEY = \"\"` in Secrets does not work.\n\n"
            "**Streamlit Cloud:** *Manage app* → *Settings* → *Secrets* → add one line like "
            "`OPENAI_API_KEY = \"sk-proj-...\"` (your actual key) → *Save* → *Reboot*.\n\n"
            "**This computer:** put the same in `.streamlit/secrets.toml`, or in a `.env` file as "
            "`OPENAI_API_KEY=sk-...`, then restart Streamlit.\n\n"
            "Keys come from [OpenAI API keys](https://platform.openai.com/api-keys) (account required)."
        )
    else:
        with st.expander("OpenAI key — test connection", expanded=False):
            fp = openai_key_fingerprint()
            if fp:
                st.caption(f"Loaded key preview (not full key): `{fp}`")
            if st.button("Test OpenAI now", key="ping_openai"):
                with st.spinner("Calling OpenAI…"):
                    ok, msg = ping_openai_api()
                if ok:
                    if "429" in msg or "rate limit" in msg.lower():
                        st.info(msg)
                    else:
                        st.success(msg)
                else:
                    st.error(msg)
            st.markdown(
                "- **401** = bad key or billing — fix at [API keys](https://platform.openai.com/api-keys) "
                "and [Billing](https://platform.openai.com/settings/organization/billing/overview), "
                "then update Secrets and **Reboot**.\n"
                "- **429** = your key is fine; OpenAI is **throttling** (too many requests). "
                "Wait a few minutes, click **Test** less often, or review "
                "[Limits](https://platform.openai.com/settings/organization/limits)."
            )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    prompt = st.chat_input("Ask a Python question…")
    if prompt:
        history = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            reply = st.write_stream(chat_answer_stream(prompt, history))
        st.session_state.messages.append({"role": "assistant", "content": reply})


def _static_view() -> None:
    st.subheader("Static topics")
    st.caption(
        "Open a topic to read lessons from `content/` and converted notebooks in `content/notebooks_md/`."
    )
    topics = load_topics_manifest()
    if not topics:
        st.info("Add entries to `content/topics.json` and markdown files in `content/`.")
        return
    for t in topics:
        title = t.get("title") or t.get("id", "Topic")
        fname = t.get("file", "")
        with st.expander(title, expanded=False):
            st.markdown(read_topic_file(fname))


def main() -> None:
    st.set_page_config(
        page_title="Pyseed",
        page_icon=_page_icon(),
        layout="centered",
        initial_sidebar_state="expanded",
    )
    inject_css()
    ensure_session_keys()

    if not st.session_state.authenticated:
        st.markdown('<div class="pyseed-wrap">', unsafe_allow_html=True)
        render_landing_brand()
        st.markdown("---")
        if not render_login():
            st.markdown("</div>", unsafe_allow_html=True)
            st.stop()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="pyseed-wrap">', unsafe_allow_html=True)
    render_app_header()

    with st.sidebar:
        st.caption("Navigation")
        if st.button("Dashboard", use_container_width=True):
            st.session_state.view = "dashboard"
            st.rerun()
        st.divider()
        if st.button("Log out", use_container_width=True):
            logout()
            st.rerun()

    view = st.session_state.view
    if view == "dashboard":
        _dashboard()
    elif view == "ai":
        _ai_view()
    elif view == "static":
        _static_view()
    else:
        st.session_state.view = "dashboard"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
