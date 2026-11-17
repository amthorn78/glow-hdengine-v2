"""HDE-EPIC043 WU-PR-03: the import boundary of the dormant integration layer (HDE-CONJ010.4).

``engine/magic10_v2/compat.py`` restates what it shares with v1's compat
module and imports only a closed set: no ``engine.magic10``, ``engine.compat``
or ``engine.core`` module directly, because the switch (WU-PR-09) re-targets
``engine/compat/compute.py`` to call this layer. The guard is on direct
imports, as the landed guards are: importing the narrative router loads
``engine.compat`` and ``engine.compat.categories``, and nothing else under the
v1 prefixes, so the child-process audit pins exactly those two and refuses
``engine.compat.compute``.

``engine.runtime.public`` is imported inside ``reader_projection_v2`` only,
because importing it reads the packaged manifest; importing ``compat.py``
reads no file. R-02 "no binary floating point": the landed package-wide scan
covers the new module.
"""
from __future__ import annotations

import ast
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "engine" / "magic10_v2"
COMPAT = PACKAGE / "compat.py"
COMPAT_PLAIN_IMPORTS = frozenset({"hashlib", "json", "jsonschema"})
COMPAT_IMPORTS = frozenset({
    "__future__",
    "collections.abc",
    "dataclasses",
    "pathlib",
    "jsonschema",
    "engine.config.magic10_v2_loader",
    "engine.config.registry_loader",
    "engine.magic10_v2.calculation",
    "engine.narratives.constants",
    "engine.narratives.router",
    "engine.presenter.emitter",
    "engine.runtime.public",
})
LAZY_IMPORTS = ["engine.runtime.public"]
V1_PREFIXES = ("engine.magic10", "engine.compat", "engine.core")
CLOSED_RAILS_ENV = {
    "PATH": os.environ.get("PATH", ""),
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "test",
}


def _is_v1(name: str) -> bool:
    return any(name == prefix or name.startswith(prefix + ".") for prefix in V1_PREFIXES)


def test_compat_imports_only_its_closed_set() -> None:
    tree = ast.parse(COMPAT.read_text(encoding="utf-8"), filename=str(COMPAT))
    plain = {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
    from_modules = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert all(node.level == 0 for node in ast.walk(tree) if isinstance(node, ast.ImportFrom))
    assert plain == COMPAT_PLAIN_IMPORTS
    assert from_modules == COMPAT_IMPORTS
    assert not any(_is_v1(name) for name in plain | from_modules)
    lazy = [
        node.module
        for function in ast.walk(tree)
        if isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef))
        for node in ast.walk(function)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]
    assert lazy == LAZY_IMPORTS


_CHILD_IMPORT_AUDIT = r"""
import sys
sys.path.insert(0, sys.argv[1])
import engine.config.registry_loader, engine.config.magic10_v2_loader, engine.magic10_v2.calculation
before = set(sys.modules)
opened = []
def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = args[0].decode() if isinstance(args[0], bytes) else args[0]
        if path.endswith(".json"):
            opened.append(path)
sys.addaudithook(audit)
import engine.magic10_v2.compat
prefixes = ("engine.magic10", "engine.compat", "engine.core")
added = sorted(
    name for name in set(sys.modules) - before
    if any(name == prefix or name.startswith(prefix + ".") for prefix in prefixes)
)
print(len(opened))
print(",".join(added))
print("engine.runtime.public" in sys.modules)
"""


def test_import_reads_no_file_and_loads_no_v1_scorer(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, "-I", "-c", _CHILD_IMPORT_AUDIT, str(ROOT)],
        capture_output=True, text=True, env=CLOSED_RAILS_ENV, cwd=tmp_path, check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.splitlines() == ["0", "engine.compat,engine.compat.categories", "False"]


def test_the_package_float_scan_covers_compat() -> None:
    assert "compat.py" in {path.name for path in PACKAGE.glob("*.py")}
