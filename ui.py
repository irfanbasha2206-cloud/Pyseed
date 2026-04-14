"""Pyseed UI: theme helpers, CSS, and header layouts."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
LOGO_PATH = ROOT / "assets" / "logo.svg"


def inject_css() -> None:
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link rel="stylesheet" media="print" onload="this.media='all'"
              href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap"/>
        <style>
          html, body, [class*="css"]  {
            font-family: 'DM Sans', 'Source Sans Pro', sans-serif !important;
          }
          .pyseed-wrap {
            max-width: 900px;
            margin: 0 auto;
            padding-bottom: 2rem;
          }
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
          .pyseed-header-bar img {
            width: 40px;
            height: 40px;
          }
          .pyseed-wordmark {
            font-size: 1.35rem;
            font-weight: 700;
            color: #1b4332;
            margin: 0;
          }
          .pyseed-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 1.25rem 1.35rem;
            border: 1px solid #dce8df;
            box-shadow: 0 4px 14px rgba(27, 67, 50, 0.06);
            margin-bottom: 1rem;
          }
          .pyseed-card h3 {
            margin: 0 0 0.35rem 0;
            color: #1b4332;
            font-size: 1.15rem;
          }
          .pyseed-card p {
            margin: 0;
            color: #52796f;
            font-size: 0.95rem;
          }
        </style>
        """,
        unsafe_allow_html=True,
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
