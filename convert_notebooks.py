"""Convert course notebooks (.ipynb) to markdown for Static mode."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "content" / "notebooks_md"


def _slug(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "lesson"


def _cell_text(cell: dict) -> str:
    src = cell.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return str(src)


def notebook_to_markdown(ipynb_path: Path) -> str:
    data = json.loads(ipynb_path.read_text(encoding="utf-8"))
    cells = data.get("cells", [])
    parts: list[str] = [f"# {ipynb_path.stem}", ""]
    for cell in cells:
        ctype = cell.get("cell_type")
        text = _cell_text(cell).strip()
        if not text:
            continue
        if ctype == "markdown":
            parts.append(text)
            parts.append("")
        elif ctype == "code":
            parts.append("```python")
            parts.append(text)
            parts.append("```")
            parts.append("")
    return "\n".join(parts).strip() + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    notebooks = sorted(ROOT.glob("*.ipynb"))
    count = 0
    for nb in notebooks:
        out_name = _slug(nb.stem) + ".md"
        md_text = notebook_to_markdown(nb)
        (OUT_DIR / out_name).write_text(md_text, encoding="utf-8")
        count += 1
    print(f"Converted {count} notebooks to {OUT_DIR}")


if __name__ == "__main__":
    main()
