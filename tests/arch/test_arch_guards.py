import ast, os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ACTIVE_PY = [p for p in ROOT.rglob("*.py")
             if "tests" not in p.parts and ".venv" not in p.parts and
                not any(x in p.parts for x in ("adapters", "core", "server", "_archive"))]

def read(p): return p.read_text(encoding="utf-8", errors="ignore")

LEGACY_ROOTS = ("adapters", "core", "server")
REGISTRATION_METHODS = ("add_url_rule", "register_blueprint")

def parse(t):
    try:
        return ast.parse(t)
    except SyntaxError:
        return None

def has_legacy_import(t):
    # Import statements by AST, so `from engine.core import core` is not a legacy
    # import while `try: import core` still is; text that is not Python keeps the
    # unanchored pattern.
    tree = parse(t)
    if tree is None:
        return any(re.search(rf"\b(from|import)\s+{root}\b", t) for root in LEGACY_ROOTS)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and any(alias.name.split(".", 1)[0] in LEGACY_ROOTS for alias in node.names):
            return True
        if isinstance(node, ast.ImportFrom) and node.level == 0 and (node.module or "").split(".", 1)[0] in LEGACY_ROOTS:
            return True
    return False

def has_route_registration(t):
    # Any use of a registration method: a call, an alias such as
    # `register = app.register_blueprint`, a getattr-family lookup by name, or a
    # string-keyed lookup such as `vars(type(app))["register_blueprint"]`.
    # A string that only mentions the name, as the static analyzers' do, is not one;
    # text that is not Python keeps the unanchored pattern.
    tree = parse(t)
    if tree is None:
        return re.search(r"add_url_rule|register_blueprint", t) is not None
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in REGISTRATION_METHODS:
            return True
        if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant) and node.slice.value in REGISTRATION_METHODS:
            return True
        if isinstance(node, ast.Call):
            func = node.func.attr if isinstance(node.func, ast.Attribute) else getattr(node.func, "id", "")
            if func in ("getattr", "attrgetter", "methodcaller") and any(isinstance(arg, ast.Constant) and arg.value in REGISTRATION_METHODS for arg in node.args):
                return True
    return False

def test_no_legacy_imports_in_active_code():
    bad = []
    for p in ACTIVE_PY:
        t = read(p)
        if has_legacy_import(t): bad.append(str(p))
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
        if has_route_registration(t):
            if "adapter" not in p.parts:
                hits.append(str(p))
    assert not hits, "Route registration found outside adapter/: \n" + "\n".join(hits)

def test_guard_patterns_flag_real_violations_not_mentions():
    real_imports = ("import core\n", "from server import app\n", "try: import core\nexcept ImportError: pass\n", "x = 1; import adapters\n", "import os, core\n")
    clean_imports = ("from engine.core import core\n", "# import core\n", "s = 'from core import x'\n", "from .core import x\n")
    real_registrations = (
        "app.register_blueprint(bp)\n",
        "register = app.register_blueprint\nregister(bp)\n",
        "getattr(app, 'add_url_rule')('/x', 'x', f)\n",
        "app.__class__.__dict__['register_blueprint'](app, bp)\n",
    )
    clean_registrations = ("NAMES = {'register_blueprint', 'add_url_rule'}\n", "ok = chain.endswith('.add_url_rule')\n", "# app.register_blueprint(bp)\n", "Rec(kind='add_url_rule')\n")
    assert all(has_legacy_import(t) for t in real_imports)
    assert not any(has_legacy_import(t) for t in clean_imports)
    assert all(has_route_registration(t) for t in real_registrations)
    assert not any(has_route_registration(t) for t in clean_registrations)
    # Text that is not Python keeps the base's unanchored patterns.
    assert has_legacy_import("- note: import core\n```\n") and has_route_registration("- note: app.register_blueprint(\n```\n")
