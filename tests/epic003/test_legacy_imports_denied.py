from pathlib import Path
import re

# Anchored to the start of an import statement: a qualified current import such
# as `from engine.core import core` is not an import of the legacy `core` tree.
FORBIDDEN = (r"^\s*from\s+core\b", r"^\s*import\s+core\b",
             r"^\s*from\s+server\b", r"^\s*import\s+server\b",
             r"^\s*from\s+adapters\b", r"^\s*import\s+adapters\b")
SEARCH_ROOTS = ("adapter","engine","cli","scripts")

def test_legacy_imports_denied():
    rx = [re.compile(p, re.MULTILINE) for p in FORBIDDEN]
    hits = []
    for root in SEARCH_ROOTS:
        p = Path(root)
        if not p.exists(): 
            continue
        for f in p.rglob("*.py"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            for r in rx:
                if r.search(txt):
                    hits.append(f"{f}")
    assert not hits, f"Legacy imports found: {hits}"
