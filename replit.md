# Pyseed

An interactive, web-based Python learning platform for beginners, powered by Streamlit and OpenAI.

## Features

- **AI Mode**: Chat interface where users ask Python questions; answers are grounded in lesson files using BM25 search + OpenAI (gpt-4o-mini).
- **Static Mode**: Documentation browser that displays lesson contents in an expandable format.
- **Secure Login**: bcrypt-based authentication via Streamlit secrets.
- **Content Conversion**: Script (`convert_notebooks.py`) to convert Jupyter Notebooks to Markdown for the platform.

## Tech Stack

- **Language**: Python 3.12
- **Framework**: Streamlit
- **AI**: OpenAI API (gpt-4o-mini)
- **Search**: rank-bm25 (RAG retrieval)
- **Auth**: bcrypt

## Project Structure

```
app.py                # Main Streamlit entry point
rag.py                # RAG logic (BM25 search + OpenAI)
seed_auth.py          # Authentication (bcrypt, session management)
ui.py                 # UI components and CSS
convert_notebooks.py  # Utility to convert .ipynb to .md
assets/               # Static assets (logo.svg)
content/              # Educational content (Markdown lessons)
  notebooks_md/       # Converted notebook Markdown files
.streamlit/
  config.toml         # Streamlit server config (port 5000, 0.0.0.0)
```

## Running Locally

The app runs on port 5000 via the "Start application" workflow.

### Development Login

Set `PYSEED_DEV_LOGIN=1` to enable a demo login (username: `demo`, password: `demo`). This is used in the workflow command.

### Production Auth

Configure users in `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-proj-..."
PYSEED_DEMO_PASSWORD_HASH = "$2b$12$R52UkcUSenMG5B8Vq9aYFe8m15tbaLFC2Zy0jp5TE2N8uzlOvkRiO"
PYSEED_DEMO_NAME = "Demo Learner"
```

The hash above matches password `pyseed-demo`.

## Dependencies

Listed in `requirements.txt`:
- streamlit>=1.28.0
- openai>=1.0.0
- rank-bm25
- python-dotenv>=1.0.0
- bcrypt>=4.0.0
