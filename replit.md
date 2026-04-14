# Pyseed

An interactive, web-based Python learning platform for beginners, powered by Streamlit and OpenAI.

## Features

- **AI Mode**: Chat interface (streaming responses) where users ask Python questions; answers are grounded in lesson files using BM25 search + OpenAI (gpt-4o-mini).
- **Static Mode**: Documentation browser displaying lessons in correct order (Introduction first, then notebooks 1–22).
- **Open Access**: Any username/password accepted when `PYSEED_OPEN_ACCESS=1` is set.
- **Secure Login**: bcrypt-based authentication via Streamlit secrets (alternative to open access).
- **Content Conversion**: Script (`convert_notebooks.py`) to convert Jupyter Notebooks to Markdown.

## Tech Stack

- **Language**: Python 3.12
- **Framework**: Streamlit
- **AI**: OpenAI API (gpt-4o-mini) with streaming
- **Search**: rank-bm25 (RAG retrieval, cached via `@st.cache_resource`)
- **Auth**: bcrypt or open-access mode

## Project Structure

```
app.py                # Main Streamlit entry point
rag.py                # RAG logic (BM25 search + OpenAI streaming)
seed_auth.py          # Authentication (bcrypt, open-access, dev mode)
ui.py                 # UI components and CSS (async font loading)
convert_notebooks.py  # Utility to convert .ipynb to .md
assets/               # Static assets (logo.svg)
content/              # Educational content (Markdown lessons)
  notebooks_md/       # Converted notebook Markdown files (ordered numerically)
.streamlit/
  config.toml         # Streamlit server config (port 5000, 0.0.0.0)
  secrets.toml.example  # Example secrets file
```

## Running Locally

The app runs on port 5000 via the "Start application" workflow.

Workflow command: `PYSEED_DEV_LOGIN=1 PYSEED_OPEN_ACCESS=1 streamlit run app.py`

## Authentication Modes

### Open Access (default for global use)
Set `PYSEED_OPEN_ACCESS = "1"` in secrets — anyone can log in with any username/password.

### Fixed User Account
```toml
PYSEED_DEMO_PASSWORD_HASH = "$2b$12$R52UkcUSenMG5B8Vq9aYFe8m15tbaLFC2Zy0jp5TE2N8uzlOvkRiO"
PYSEED_DEMO_NAME = "Demo Learner"
```
(Hash above matches password `pyseed-demo`)

### Development Mode
Set `PYSEED_DEV_LOGIN=1` — accepts username `demo` / password `demo`.

## OpenAI Setup

Add to secrets:
```toml
OPENAI_API_KEY = "sk-proj-..."
# For project-scoped keys, also add:
# OPENAI_PROJECT = "proj_..."
# OPENAI_ORGANIZATION = "org-..."
```

## Dependencies

Listed in `requirements.txt`:
- streamlit>=1.28.0
- openai>=1.0.0
- rank-bm25
- python-dotenv>=1.0.0
- bcrypt>=4.0.0

## Performance Notes

- BM25 corpus is built once and cached via `@st.cache_resource` (survives reruns)
- Topics manifest is cached for 1 hour via `@st.cache_data(ttl=3600)`
- OpenAI client is cached via `@st.cache_resource`
- Google Fonts loaded asynchronously (non-blocking)
- AI responses stream token-by-token using `st.write_stream`
