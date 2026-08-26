from pathlib import Path
from scripts.rag.validate_frontmatter import parse_keys, REQUIRED

IGNORED = {".github", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"}

def test_handbook_markdown_has_required_frontmatter():
    root=Path(__file__).parents[1]
    for p in root.rglob("*.md"):
        rel=p.relative_to(root)
        if any(part in IGNORED for part in rel.parts):
            continue
        assert REQUIRED <= parse_keys(p.read_text(encoding="utf-8")), p
