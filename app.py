"""
Pyseed — Streamlit entry: login, dashboard (AI / Static), RAG chat, static topics.
"""

from __future__ import annotations

import sys
from pathlib import Path

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
from ui import (
    LOGO_PATH,
    inject_css,
    mode_card_html,
    notebook_card_html,
    get_notebook_icon,
    render_app_header,
    render_landing_brand,
)


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
            "Ask your Python Questions and Get Answers Quickly",
            "✨",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        mode_card_html(
            "Static mode",
            "Great for reading lessons step by step.",
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
    has_key = bool(get_openai_key())

    st.subheader("💬 Ask Python Questions")

    if has_key:
        st.caption("Powered by OpenAI + your lesson notebooks.")
        with st.expander("OpenAI key — test connection", expanded=False):
            fp = openai_key_fingerprint()
            if fp:
                st.caption(f"Loaded key preview: `{fp}`")
            if st.button("Test OpenAI now", key="ping_openai"):
                with st.spinner("Calling OpenAI…"):
                    ok, msg = ping_openai_api()
                if ok:
                    st.success(msg) if "429" not in msg else st.info(msg)
                else:
                    st.error(msg)
    else:
        st.markdown(
            '<span class="free-mode-badge">🆓 FREE MODE — Notebook Search</span>',
            unsafe_allow_html=True,
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown(
                "👋 Hi! I'm **Pyseed**, your beginner Python tutor.\n\n"
                "Ask me anything about Python — variables, loops, functions, OOP and more. "
                "I'll answer from your lesson notebooks!"
            )

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
        st.session_state.messages.append({"role": "assistant", "content": str(reply)})


def _static_view() -> None:
    st.subheader("📚 Python Lesson Notebooks")
    st.caption("Click any notebook below to open and read its full lesson content.")

    topics = load_topics_manifest()
    if not topics:
        st.info("Add entries to `content/topics.json` and markdown files in `content/`.")
        return

    intro_topics = [t for t in topics if "introduction" in t.get("title", "").lower() or t.get("id", "").startswith("nb-an_")]
    numbered_topics = [t for t in topics if t not in intro_topics]

    icon_index = 0
    for t in intro_topics + numbered_topics:
        title = t.get("title") or t.get("id", "Topic")
        fname = t.get("file", "")
        icon = get_notebook_icon(icon_index)
        icon_index += 1

        is_intro = "introduction" in title.lower()
        badge = "Intro" if is_intro else f"Lesson {icon_index - 1}" if icon_index > 2 else ""

        with st.expander(
            label=f"{icon}  {title}",
            expanded=False,
        ):
            content = read_topic_file(fname)
            st.markdown(content, unsafe_allow_html=False)


def main() -> None:
    st.set_page_config(
        page_title="Pyseed",
        page_icon=_page_icon(),
        layout="wide",
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
