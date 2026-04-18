"""Auth module: bcrypt users from Secrets, open-access fallback, or dev mode."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import bcrypt
import streamlit as st


USER_DB_PATH = Path(__file__).resolve().parent / "user_db.json"


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

    if not users and secrets is not None:
        h = secrets.get("PYSEED_DEMO_PASSWORD_HASH") or secrets.get("DEMO_PASSWORD_HASH")
        if h:
            name = secrets.get("PYSEED_DEMO_NAME") or secrets.get("DEMO_NAME") or "Demo Learner"
            users["demo"] = {"name": str(name), "password_hash": str(h)}

    return users


def _default_user_db() -> dict[str, Any]:
    return {"users": {}}


def _load_user_db() -> dict[str, Any]:
    if not USER_DB_PATH.is_file():
        return _default_user_db()
    try:
        with USER_DB_PATH.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            return _default_user_db()
        users = data.get("users") if isinstance(data.get("users"), dict) else {}
        return {"users": users}
    except Exception:
        return _default_user_db()


def _save_user_db(db: dict[str, Any]) -> None:
    try:
        USER_DB_PATH.write_text(json.dumps(db, indent=2), encoding="utf-8")
    except Exception:
        pass


def _remember_user(username: str, email: str) -> None:
    db = _load_user_db()
    username_key = username.strip().lower()
    email_value = email.strip()
    if username_key:
        db["users"][username_key] = email_value
        _save_user_db(db)


def _load_remembered_user() -> dict[str, str] | None:
    # Removed auto-login to prevent conflicts between users
    return None


def _clear_remembered_user() -> None:
    # No longer needed without remembered user
    pass


def _load_dotenv_if_present() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass


def _is_open_access() -> bool:
    """
    Return True when the app should accept any non-empty username and password.
    Defaults to True (open access) so the app works on Streamlit Community Cloud
    with no secrets required. Set PYSEED_OPEN_ACCESS=0 in secrets to disable.
    """
    # Explicit disable via env var
    if os.environ.get("PYSEED_OPEN_ACCESS", "").strip() == "0":
        return False
    # Explicit enable via env var
    if os.environ.get("PYSEED_OPEN_ACCESS", "").strip() == "1":
        return True
    try:
        v = st.secrets.get("PYSEED_OPEN_ACCESS")
        if v is not None:
            if str(v).strip() in ("0", "false", "no"):
                return False
            if str(v).strip() in ("1", "true", "yes"):
                return True
    except (FileNotFoundError, RuntimeError, AttributeError, KeyError, TypeError):
        pass
    # Default: open access — no secrets needed
    return True


def verify_user(username: str, password: str) -> tuple[bool, str | None]:
    if _is_open_access():
        return True, username.strip() or "Learner"

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
    """Show login form. Returns True if user is now authenticated."""
    _load_dotenv_if_present()
    ensure_session_keys()

    if st.session_state.authenticated:
        return True

    # Removed auto-login to allow each user to login independently

    if _is_open_access():
        u = st.text_input("Username", key="login_u", placeholder="Enter Your Name")
        p = st.text_input("Email ID", key="login_p", placeholder="Enter your email address")
        if st.button("Sign in", type="primary", use_container_width=True):
            if not u.strip():
                st.error("Please enter your name.")
            elif not p.strip():
                st.error("Please enter your email address.")
            else:
                st.session_state.authenticated = True
                st.session_state.display_name = u.strip()
                st.session_state.username = u.strip().lower()
                _remember_user(u, p)
                st.rerun()
        return False

    users = _get_auth_users()

    if not users:
        if os.environ.get("PYSEED_DEV_LOGIN") == "1":
            st.warning(
                "Development mode: no `auth_users` in secrets. "
                "Using demo/demo — not for production."
            )
            u = st.text_input("Username", key="login_u", placeholder="Enter Your Name")
            p = st.text_input("Email ID", key="login_p", placeholder="Enter your email address")
            if st.button("Sign in", type="primary", use_container_width=True):
                if u == "demo" and p == "demo":
                    st.session_state.authenticated = True
                    st.session_state.display_name = "Demo Learner"
                    st.session_state.username = "demo"
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            return False

        st.error("**Authentication is not configured.** Add login keys to Streamlit **Secrets**.")
        st.markdown(
            """
**Streamlit Community Cloud**

1. **Manage app** → **Settings** → **Secrets**.
2. Paste one of the options below → **Save** → **Reboot**.

**Option A — open access (any username/password works)**
"""
        )
        st.code('PYSEED_OPEN_ACCESS = "1"\nOPENAI_API_KEY = ""', language="toml")
        st.markdown("**Option B — fixed demo account (username: `demo`, password: `pyseed-demo`)**")
        st.code(
            'OPENAI_API_KEY = ""\n\n'
            'PYSEED_DEMO_PASSWORD_HASH = "$2b$12$R52UkcUSenMG5B8Vq9aYFe8m15tbaLFC2Zy0jp5TE2N8uzlOvkRiO"\n'
            'PYSEED_DEMO_NAME = "Demo Learner"\n',
            language="toml",
        )
        return False

    u = st.text_input("Username", key="login_u", placeholder="Enter Your Name")
    p = st.text_input("Email ID", key="login_p", placeholder="Enter your email address")
    if st.button("Sign in", type="primary", use_container_width=True):
        if not u.strip():
            st.error("Please enter your name.")
        elif not p.strip():
            st.error("Please enter your email address.")
        else:
            ok, name = verify_user(u.strip(), p)
            if ok and name:
                st.session_state.authenticated = True
                st.session_state.display_name = name
                st.session_state.username = u.strip()
                _remember_user(u, p)
                st.rerun()
            else:
                st.error("Invalid username or password.")
    return False


def logout() -> None:
    st.session_state.authenticated = False
    st.session_state.display_name = None
    st.session_state.username = None
    st.session_state.view = "dashboard"
    _clear_remembered_user()
    for k in ("messages",):
        if k in st.session_state:
            del st.session_state[k]
