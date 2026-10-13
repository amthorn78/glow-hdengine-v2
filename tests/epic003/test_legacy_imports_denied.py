from pathlib import Path
import ast
import re

LEGACY_ROOTS = ("core", "server", "adapters")
# Text that is not Python keeps the unanchored patterns.
FORBIDDEN = (r"\bfrom\s+core\b", r"\bimport\s+core\b",
             r"\bfrom\s+server\b", r"\bimport\s+server\b",
             r"\bfrom\s+adapters\b", r"\bimport\s+adapters\b")
SEARCH_ROOTS = ("adapter","engine","cli","scripts")

def _imports_legacy_tree(txt, rx):
    # Import statements by AST: a qualified current import such as
    # `from engine.core import core` is not an import of the legacy `core` tree,
    # while `try: import core` on one line still is.
    try:
        tree = ast.parse(txt)
    except SyntaxError:
        return any(r.search(txt) for r in rx)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and any(alias.name.split(".", 1)[0] in LEGACY_ROOTS for alias in node.names):
            return True
        if isinstance(node, ast.ImportFrom) and node.level == 0 and (node.module or "").split(".", 1)[0] in LEGACY_ROOTS:
            return True
    return False

def test_legacy_imports_denied():
    rx = [re.compile(p) for p in FORBIDDEN]
    hits = []
    for root in SEARCH_ROOTS:
        p = Path(root)
        if not p.exists():
            continue
        for f in p.rglob("*.py"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            if _imports_legacy_tree(txt, rx):
                hits.append(f"{f}")
    assert not hits, f"Legacy imports found: {hits}"

def test_legacy_import_check_flags_statements_not_mentions():
    rx = [re.compile(p) for p in FORBIDDEN]
    assert all(_imports_legacy_tree(t, rx) for t in ("import core\n", "try: import core\nexcept ImportError: pass\n", "x = 1; from adapters import a\n", "- note: import server\n```\n"))
    assert not any(_imports_legacy_tree(t, rx) for t in ("from engine.core import core\n", "# import core\n", "s = 'import server'\n"))
