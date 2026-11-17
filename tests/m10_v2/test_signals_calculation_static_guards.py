"""HDE-EPIC043 WU-PR-02: the import boundary of the signals and calculation modules (HDE-CONJ010.2, .3).

The two modules restate what they share with v1 (the ``pair_key`` structure)
and import only a closed set: no ``engine.magic10``, ``engine.compat`` or
``engine.core`` module, no file, environment, clock or randomness source.
Importing them reads no file.

R-02 "no binary floating point": the landed
``test_kernel_static_guards.py::test_no_binary_floating_point_in_the_package``
scans every ``engine/magic10_v2/*.py``; this module asserts the two new files
are where that scan globs.
"""
from __future__ import annotations

import ast
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "engine" / "magic10_v2"
SIGNALS = PACKAGE / "signals.py"
CALCULATION = PACKAGE / "calculation.py"
SIGNALS_IMPORTS = frozenset({
    "__future__",
    "collections.abc",
    "dataclasses",
    "engine.config.magic10_v2_loader",
    "engine.config.registry_loader",
    "engine.magic10_v2.kernel",
})
CALCULATION_IMPORTS = frozenset({
    "__future__",
    "collections.abc",
    "dataclasses",
    "engine.config.magic10_v2_loader",
    "engine.config.registry_loader",
    "engine.magic10_v2.kernel",
    "engine.magic10_v2.signals",
    "engine.serializer.canon",
})
CALCULATION_PLAIN_IMPORTS = frozenset({"hashlib", "re"})
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


def _imports(path: Path) -> tuple[set[str], set[str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    plain = {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
    from_modules = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert all(node.level == 0 for node in ast.walk(tree) if isinstance(node, ast.ImportFrom))
    return plain, from_modules


def _is_v1(name: str) -> bool:
    return any(name == prefix or name.startswith(prefix + ".") for prefix in V1_PREFIXES)


def test_signals_imports_only_its_closed_set() -> None:
    plain, from_modules = _imports(SIGNALS)
    assert plain == set()
    assert from_modules == SIGNALS_IMPORTS
    assert not any(_is_v1(name) for name in from_modules)


def test_calculation_imports_only_its_closed_set() -> None:
    plain, from_modules = _imports(CALCULATION)
    assert plain == CALCULATION_PLAIN_IMPORTS
    assert from_modules == CALCULATION_IMPORTS
    assert not any(_is_v1(name) for name in plain | from_modules)


_CHILD_IMPORT_AUDIT = r"""
import sys
sys.path.insert(0, sys.argv[1])
import engine.config.registry_loader, engine.config.magic10_v2_loader
before = set(sys.modules)
opened = []
def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = args[0].decode() if isinstance(args[0], bytes) else args[0]
        if path.endswith(".json"):
            opened.append(path)
sys.addaudithook(audit)
import engine.magic10_v2.signals, engine.magic10_v2.calculation
prefixes = ("engine.magic10", "engine.compat", "engine.core")
added = sorted(
    name for name in set(sys.modules) - before
    if any(name == prefix or name.startswith(prefix + ".") for prefix in prefixes)
)
print(len(opened))
print(",".join(added))
"""


def test_import_reads_no_file_and_loads_no_v1_module(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, "-I", "-c", _CHILD_IMPORT_AUDIT, str(ROOT)],
        capture_output=True, text=True, env=CLOSED_RAILS_ENV, cwd=tmp_path, check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.splitlines() == ["0", ""]


def test_the_package_float_scan_covers_both_modules() -> None:
    assert {"signals.py", "calculation.py"} <= {path.name for path in PACKAGE.glob("*.py")}
