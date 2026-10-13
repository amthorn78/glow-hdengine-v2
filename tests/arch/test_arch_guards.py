import os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ACTIVE_PY = [p for p in ROOT.rglob("*.py")
             if "tests" not in p.parts and ".venv" not in p.parts and
                not any(x in p.parts for x in ("adapters", "core", "server", "_archive"))]

def read(p): return p.read_text(encoding="utf-8", errors="ignore")

def test_no_legacy_imports_in_active_code():
    bad = []
    for p in ACTIVE_PY:
        t = read(p)
        # Statement-anchored: `from engine.core import core` is not a legacy import.
        if re.search(r"^\s*(from|import)\s+adapters\b", t, re.M): bad.append(str(p))
        if re.search(r"^\s*(from|import)\s+core\b", t, re.M):     bad.append(str(p))
        if re.search(r"^\s*(from|import)\s+server\b", t, re.M):   bad.append(str(p))
    assert not bad, f"Legacy imports found:\n" + "\n".join(bad)

def test_handlers_cli_use_single_emitter_path():
    # forbid ad-hoc dumps/jsonify in handlers and CLI
    scope = [p for p in ACTIVE_PY if any(s in p.parts for s in ("engine","cli"))]
    bad = []
    for p in scope:
        t = read(p)
        # Product handler and CLI homes only; tools/cli and scripts/cli are
        # evidence/harness generators that build CLI stdin, not public bytes.
        if p.relative_to(ROOT).as_posix().startswith(("engine/http/", "engine/cli/")):
            if re.search(r"\bjson\.dumps\s*\(", t): bad.append(str(p))
            if re.search(r"\bjsonify\s*\(", t):     bad.append(str(p))
    assert not bad, "Ad-hoc emitters/jsonify detected:\n" + "\n".join(bad)

def test_blueprints_only_in_adapter():
    # route registration must be in adapter/
    hits = []
    for p in ACTIVE_PY:
        t = read(p)
        # A registration call, not the bare name (static analyzers mention it).
        if re.search(r"\.\s*(add_url_rule|register_blueprint)\s*\(", t):
            if "adapter" not in p.parts:
                hits.append(str(p))
    assert not hits, "Route registration found outside adapter/: \n" + "\n".join(hits)
