"""Minimal bcrypt auth using Streamlit secrets (no passwords in repo)."""

from __future__ import annotations

import os
from typing import Any

import bcrypt
import streamlit as st


def _normalize_user_table(raw: Any) -> dict[str, Any]:
    if not raw:
        return {}
    if hasattr(raw, "to_dict"):
        raw = raw.to_dict()
    out: dict[str, Any] = {}
    for key, entry in dict(raw).items():
        if hasattr(entry, "to_dict"):
            entry = entry.to_dict()
        if isinstance(entry, dict):
            out[str(key)] = entry
    return out


def _get_auth_users() -> dict[str, Any]:
    try:
        secrets = st.secrets
        raw = secrets.get("auth_users", {})
    except (FileNotFoundError, RuntimeError):
        secrets = None
        raw = {}

    users = _normalize_user_table(raw)

    # Easier for Streamlit Cloud: plain keys (no [auth_users.demo] section).
    if not users and secrets is not None:
        h = secrets.get("PYSEED_DEMO_PASSWORD_HASH") or secrets.get("DEMO_PASSWORD_HASH")
        if h:
            name = secrets.get("PYSEED_DEMO_NAME") or secrets.get("DEMO_NAME") or "Demo Learner"
            users["demo"] = {"name": str(name), "password_hash": str(h)}

    return users


def _load_dotenv_if_present() -> None:
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass


def verify_user(username: str, password: str) -> tuple[bool, str | None]:
    users = _get_auth_users()
    if username not in users:
        return False, None
    entry = users[username]
    if hasattr(entry, "to_dict"):
        entry = entry.to_dict()
    ph = entry.get("password_hash") or entry.get("password")
    if not ph:
        return False, None
    if isinstance(ph, bytes):
        ph_bytes = ph
    else:
        ph_bytes = str(ph).encode()
    ok = bcrypt.checkpw(password.encode("utf-8"), ph_bytes)
    name = entry.get("name") or username
    return ok, name if ok else None


def ensure_session_keys() -> None:
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "display_name" not in st.session_state:
        st.session_state.display_name = None
    if "username" not in st.session_state:
        st.session_state.username = None
    if "view" not in st.session_state:
        st.session_state.view = "dashboard"


def render_login() -> bool:
    """Show login form. Returns True if user is authenticated."""
    _load_dotenv_if_present()
    ensure_session_keys()

    if st.session_state.authenticated:
        return True

    users = _get_auth_users()
    if not users:
        if os.environ.get("PYSEED_DEV_LOGIN") == "1":
            st.warning(
                "Development mode: no `auth_users` in secrets. "
                "Using demo/demo — not for production."
            )
            u = st.text_input("Username", key="login_u")
            p = st.text_input("Password", type="password", key="login_p")
            if st.button("Sign in", type="primary", use_container_width=True):
                if u == "demo" and p == "demo":
                    st.session_state.authenticated = True
                    st.session_state.display_name = "Demo Learner"
                    st.session_state.username = "demo"
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            return False
        st.error("**Authentication is not configured.** Add login keys to Streamlit **Secrets** (see below).")
        st.markdown(
            """
**Where do I type this?**  
There is no menu item named `auth_users.demo`. On Streamlit Cloud you get **one text box** for secrets.  
You **copy and paste lines** into that box — like editing a small config file.

**Streamlit Community Cloud**

1. **Manage app** (bottom right) → **Settings** → **Secrets**.  
2. Paste **Option A** (simplest) or **Option B** from the boxes below.  
3. **Save**, then **Reboot** the app.

**Sign in after that:** username **`demo`**, password **`pyseed-demo`** (for the sample hash below).

**Local run:** save the same text as `.streamlit/secrets.toml` next to `config.toml`.

**Temporary local demo only:** set `PYSEED_DEV_LOGIN=1` and use **demo** / **demo** (not for public sites).
"""
        )
        st.markdown("**Option A — easiest (no `[brackets]`)**")
        st.code(
            'OPENAI_API_KEY = ""\n\n'
            'PYSEED_DEMO_PASSWORD_HASH = "$2b$12$R52UkcUSenMG5B8Vq9aYFe8m15tbaLFC2Zy0jp5TE2N8uzlOvkRiO"\n'
            'PYSEED_DEMO_NAME = "Demo Learner"\n',
            language="toml",
        )
        with st.expander("Option B — grouped user (same thing, different TOML style)", expanded=False):
            st.caption(
                "`[auth_users.demo]` is only a **section header** in the secrets file, not something you search for in GitHub."
            )
            st.code(
                'OPENAI_API_KEY = ""\n\n'
                "[auth_users.demo]\n"
                'name = "Demo Learner"\n'
                'password_hash = "$2b$12$R52UkcUSenMG5B8Vq9aYFe8m15tbaLFC2Zy0jp5TE2N8uzlOvkRiO"\n',
                language="toml",
            )
        st.caption("That hash matches password **pyseed-demo**. Change it before sharing widely.")
        return False

    u = st.text_input("Username", key="login_u")
    p = st.text_input("Password", type="password", key="login_p")
    if st.button("Sign in", type="primary", use_container_width=True):
        ok, name = verify_user(u.strip(), p)
        if ok and name:
            st.session_state.authenticated = True
            st.session_state.display_name = name
            st.session_state.username = u.strip()
            st.rerun()
        else:
            st.error("Invalid username or password.")
    return False


def logout() -> None:
    st.session_state.authenticated = False
    st.session_state.display_name = None
    st.session_state.username = None
    st.session_state.view = "dashboard"
    for k in ("messages",):
        if k in st.session_state:
            del st.session_state[k]
