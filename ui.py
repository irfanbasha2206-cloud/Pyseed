"""Pyseed UI: theme helpers, CSS, and header layouts."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
LOGO_PATH = ROOT / "assets" / "logo.svg"

NOTEBOOK_ICONS = [
    "🌱", "📝", "🔢", "➕", "🔀", "🔁", "🔄", "⏭️", "🧵",
    "📋", "📦", "🗂️", "🔑", "🧩", "🛠️", "⚡", "🔃", "🏗️",
    "🔐", "📂", "⚠️", "📚",
]


def get_notebook_icon(index: int) -> str:
    if index < len(NOTEBOOK_ICONS):
        return NOTEBOOK_ICONS[index]
    return "📖"


def inject_css() -> None:
    st.html(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet"/>
        <style>
          html, body, [class*="css"] {
            font-family: 'DM Sans', 'Source Sans Pro', sans-serif !important;
          }

          /* ── Layout ── */
          .pyseed-wrap {
            max-width: 900px;
            margin: 0 auto;
            padding-bottom: 2rem;
          }

          /* ── Fix text/code overflow in static view ── */
          .stMarkdown p,
          .stMarkdown li,
          .stMarkdown td {
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
            white-space: normal !important;
            max-width: 100% !important;
          }
          .stMarkdown pre,
          .stMarkdown code {
            white-space: pre-wrap !important;
            word-break: break-all !important;
            overflow-x: auto !important;
            max-width: 100% !important;
          }
          .stMarkdown pre {
            padding: 0.75rem 1rem !important;
            border-radius: 8px !important;
            background: #f0f4f1 !important;
            border: 1px solid #d4e6da !important;
          }
          /* Fix expander content overflow */
          [data-testid="stExpander"] > div > div {
            overflow-wrap: break-word !important;
            word-break: break-word !important;
            overflow: visible !important;
          }
          [data-testid="stExpanderDetails"] {
            overflow: visible !important;
            max-width: 100% !important;
          }

          /* ── Notebook topic card ── */
          .nb-card {
            background: linear-gradient(135deg, #f0faf3 0%, #ffffff 100%);
            border: 1.5px solid #b7dfc5;
            border-radius: 14px;
            padding: 0.85rem 1.1rem;
            margin-bottom: 0.6rem;
            display: flex;
            align-items: center;
            gap: 0.85rem;
            cursor: pointer;
            transition: box-shadow 0.18s, border-color 0.18s, transform 0.15s;
            box-shadow: 0 2px 8px rgba(27, 67, 50, 0.06);
            text-decoration: none !important;
          }
          .nb-card:hover {
            border-color: #2d6a4f;
            box-shadow: 0 6px 20px rgba(27, 67, 50, 0.13);
            transform: translateY(-2px);
          }
          .nb-icon {
            font-size: 1.6rem;
            flex-shrink: 0;
            width: 2.4rem;
            text-align: center;
          }
          .nb-title {
            font-weight: 600;
            color: #1b4332;
            font-size: 0.97rem;
            line-height: 1.3;
          }
          .nb-badge {
            margin-left: auto;
            background: #d8f3e3;
            color: #1b4332;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 0.15rem 0.55rem;
            border-radius: 99px;
            flex-shrink: 0;
            letter-spacing: 0.04em;
          }

          /* ── Landing & header ── */
          .pyseed-landing-title {
            font-size: 2.1rem;
            font-weight: 700;
            color: #1b4332;
            margin: 0;
            letter-spacing: -0.02em;
          }
          .pyseed-sub {
            color: #52796f;
            font-size: 1rem;
            margin-top: 0.35rem;
          }
          .pyseed-header-bar {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.35rem 0 1rem 0;
            border-bottom: 1px solid #e0ebe4;
            margin-bottom: 1.25rem;
          }
          .pyseed-header-bar img { width: 40px; height: 40px; }
          .pyseed-wordmark {
            font-size: 1.35rem;
            font-weight: 700;
            color: #1b4332;
            margin: 0;
          }

          /* ── Mode cards ── */
          .pyseed-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 1.25rem 1.35rem;
            border: 1px solid #dce8df;
            box-shadow: 0 4px 14px rgba(27, 67, 50, 0.06);
            margin-bottom: 1rem;
          }
          .pyseed-card h3 { margin: 0 0 0.35rem 0; color: #1b4332; font-size: 1.15rem; }
          .pyseed-card p  { margin: 0; color: #52796f; font-size: 0.95rem; }

          /* ── AI chat free-mode badge ── */
          .free-mode-badge {
            display: inline-block;
            background: #d8f3e3;
            color: #1b4332;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.2rem 0.65rem;
            border-radius: 99px;
            letter-spacing: 0.04em;
            margin-bottom: 0.5rem;
          }
        </style>
        """
    )


def render_landing_brand() -> None:
    if not LOGO_PATH.is_file():
        st.markdown("## Pyseed")
        return
    c1, c2 = st.columns([1, 5])
    with c1:
        st.image(str(LOGO_PATH), width=64)
    with c2:
        st.markdown(
            '<p class="pyseed-landing-title">Pyseed</p>'
            '<p class="pyseed-sub">Beginner Python — your lessons, your pace.</p>',
            unsafe_allow_html=True,
        )


def render_app_header() -> None:
    if not LOGO_PATH.is_file():
        st.markdown("### Pyseed")
        return
    st.markdown('<div class="pyseed-header-bar">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 12])
    with c1:
        st.image(str(LOGO_PATH), width=40)
    with c2:
        st.markdown('<p class="pyseed-wordmark">Pyseed</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def mode_card_html(title: str, body: str, emoji: str) -> str:
    return (
        f'<div class="pyseed-card"><h3>{emoji} {title}</h3><p>{body}</p></div>'
    )


def notebook_card_html(title: str, icon: str, badge: str = "") -> str:
    badge_html = f'<span class="nb-badge">{badge}</span>' if badge else ""
    return (
        f'<div class="nb-card">'
        f'<span class="nb-icon">{icon}</span>'
        f'<span class="nb-title">{title}</span>'
        f'{badge_html}'
        f'</div>'
    )
