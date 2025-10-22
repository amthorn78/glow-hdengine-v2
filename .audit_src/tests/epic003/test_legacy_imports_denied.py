from pathlib import Path
import re

FORBIDDEN = (r"\bfrom\s+core\b", r"\bimport\s+core\b",
             r"\bfrom\s+server\b", r"\bimport\s+server\b",
             r"\bfrom\s+adapters\b", r"\bimport\s+adapters\b")
SEARCH_ROOTS = ("adapter","engine","cli","scripts")

def test_legacy_imports_denied():
    rx = [re.compile(p) for p in FORBIDDEN]
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
