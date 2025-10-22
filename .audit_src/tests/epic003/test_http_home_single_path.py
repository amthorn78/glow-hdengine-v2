from pathlib import Path
FORBIDDEN = ("from adapters", "import adapters")
SEARCH_ROOTS = ("engine/http", "adapter")
def test_http_home_single_path_no_adapters_imports():
    for root in SEARCH_ROOTS:
        p = Path(root)
        if not p.exists():
            continue
        for f in p.rglob("*.py"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            for bad in FORBIDDEN:
                assert bad not in txt, f"Forbidden import '{bad}' found in {f}"
