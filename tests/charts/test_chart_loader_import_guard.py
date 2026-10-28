"""engine/charts/loader.py stays removed (HDE-EPIC041 WU-PR-02, HDE-SEPA006.2).

The mixed chart loader and its legacy load_chart(user_id) signature are
retired. No tracked Python file outside the classifier's historical prefixes
and the two planning and canon trees may import the module or reference its
_call_legacy helper. Callers use adapter.chart_orchestration and
engine.charts.pure.
"""
from __future__ import annotations

import ast
from pathlib import Path, PurePosixPath
import re
import subprocess

from ci.checks import classify_ci_changes as classifier

ROOT = Path(__file__).resolve().parents[2]
SELF = Path(__file__).resolve().relative_to(ROOT).as_posix()
RETIRED_PATH = "engine/charts/loader.py"
MODULE = "engine.charts.loader"
LEGACY = "_call_legacy"
# A string that names the module, or an attribute or entry point in it, is a
# dynamic-import form: importlib.import_module, __import__, mock.patch targets.
MODULE_STRING = re.compile(r"engine\.charts\.loader(?:[.:][A-Za-z_]\w*)*")
# A tracked .py file that is not Python (scripts/scratch.py holds Markdown
# notes) is searched as text instead.
TEXT = re.compile(r"engine\.charts\.loader|_call_legacy")
EXCLUDED_PREFIXES = classifier._HISTORICAL_PREFIXES
LIVE_CALLERS = (
    "scripts/make_compat_determinism_artifacts.py",
    "tests/loader/test_load_chart_fixture_only.py",
    "tests/loader/test_loader_logs_keys_only.py",
)


def _absolute(node: ast.ImportFrom, path: str) -> str:
    if not node.level:
        return node.module or ""
    package = PurePosixPath(path).parent.parts
    base = package[: len(package) - node.level + 1]
    return ".".join((*base, *([node.module] if node.module else [])))


def findings(source: str, path: str) -> list[str]:
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == MODULE or alias.name.startswith(MODULE + "."):
                    found.append(f"import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            module = _absolute(node, path)
            names = {alias.name for alias in node.names}
            if module == MODULE or module.startswith(MODULE + "."):
                found.append(f"from {module} import")
            elif module == "engine.charts" and "loader" in names:
                found.append("from engine.charts import loader")
            if LEGACY in names:
                found.append(f"from {module} import {LEGACY}")
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            if MODULE_STRING.fullmatch(node.value) or node.value == LEGACY:
                found.append(f"string {node.value!r}")
        elif isinstance(node, ast.Name) and node.id == LEGACY:
            found.append(f"name {LEGACY}")
        elif isinstance(node, ast.Attribute) and node.attr == LEGACY:
            found.append(f"attribute {LEGACY}")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == LEGACY:
            found.append(f"definition {LEGACY}")
    return found


def scan(source: str, path: str) -> list[str]:
    try:
        return findings(source, path)
    except SyntaxError:
        return [f"text {m.group(0)!r}" for m in TEXT.finditer(source)]


def _tracked_python() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.py", ":(exclude)docs/ephemeral/", ":(exclude)docs/pfcanon/"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout
    return [p for p in out.split("\0") if p]


def test_no_tracked_python_file_imports_the_retired_loader():
    tracked = _tracked_python()
    scanned = [p for p in tracked if p != SELF and not p.startswith(EXCLUDED_PREFIXES)]
    assert set(LIVE_CALLERS) <= set(scanned)
    hits = {}
    for path in scanned:
        found = scan((ROOT / path).read_text(encoding="utf-8"), path)
        if found:
            hits[path] = found
    assert hits == {}


def test_the_retired_module_path_does_not_exist():
    assert not (ROOT / RETIRED_PATH).exists()
    assert RETIRED_PATH not in _tracked_python()


def test_checker_flags_every_import_form():
    planted = {
        "import engine.charts.loader\n": "engine/x.py",
        "import engine.charts.loader as L\n": "engine/x.py",
        "from engine.charts.loader import load_chart\n": "engine/x.py",
        "from engine.charts.loader import LoaderInputError as E\n": "engine/x.py",
        "from engine.charts import loader\n": "engine/x.py",
        "from engine.charts import pure, loader\n": "engine/x.py",
        "from .loader import load_chart\n": "engine/charts/x.py",
        "from . import loader\n": "engine/charts/x.py",
        "from ..charts.loader import load_chart\n": "engine/charts/x.py",
        "import importlib\nimportlib.import_module('engine.charts.loader')\n": "scripts/x.py",
        "__import__('engine.charts.loader')\n": "scripts/x.py",
        "monkeypatch.setattr('engine.charts.loader._Path', p)\n": "tests/x.py",
        "mock.patch('engine.charts.loader:load_chart')\n": "tests/x.py",
        "_call_legacy('u', None)\n": "tests/x.py",
        "L._call_legacy('u', None)\n": "tests/x.py",
        "def _call_legacy(user_id):\n    pass\n": "engine/x.py",
        "from engine.x import _call_legacy\n": "tests/x.py",
        "getattr(L, '_call_legacy')\n": "tests/x.py",
    }
    for source, path in planted.items():
        assert scan(source, path), source
    assert scan("- notes: run engine.charts.loader\n```bash\n", "scripts/x.py")


def test_checker_ignores_text_that_is_not_an_import():
    # Real forms on main: the purity test's planted source text, the
    # classifier's owner-mapping key for the removed path, and comments.
    for source, path in {
        "SOURCES = ('from engine.charts.loader import load_chart\\n',)\n": "tests/charts/x.py",
        "OWNERS = {'engine/charts/loader.py': ('tests/x.py',)}\n": "ci/checks/x.py",
        "# engine.charts.loader was removed\nx = 1\n": "tests/x.py",
        "from engine.charts.pure import normalize_chart\n": "adapter/x.py",
        "from . import pure\n": "engine/charts/x.py",
        "from .loader import x\n": "engine/narratives/x.py",
    }.items():
        assert scan(source, path) == [], source
    assert scan("- notes: run adapter.chart_orchestration\n```bash\n", "scripts/x.py") == []
