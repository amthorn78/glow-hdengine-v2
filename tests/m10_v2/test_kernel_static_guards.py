"""HDE-EPIC043 WU-PR-01 acceptance 4 and the kernel's import boundary (HDE-CONJ010.1).

HDE Math Spec §5.2.11: "All quantities are integers. No binary floating point is
used anywhere." Every module of ``engine/magic10_v2/`` is scanned statically
against this rule set:

* R1 no ``float`` or ``complex`` literal;
* R2 no name ``float`` or ``complex``;
* R3 no true division ``/`` (or ``/=``);
* R4 no ``**`` (or ``**=``), since a negative exponent yields a ``float``;
* R5 no import of ``math``, ``cmath``, ``decimal``, ``fractions``,
  ``statistics`` or ``numpy``;
* R6 no attribute access on a name ``math``.

The kernel restates the v1 five-state rule and imports only a closed set: no
``engine.magic10``, ``engine.compat`` or ``engine.core`` module. Importing it
reads no file.
"""
from __future__ import annotations

import ast
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "engine" / "magic10_v2"
KERNEL = PACKAGE / "kernel.py"
FORBIDDEN_MODULES = frozenset({"math", "cmath", "decimal", "fractions", "statistics", "numpy"})
KERNEL_IMPORTS = frozenset({
    "__future__",
    "collections.abc",
    "dataclasses",
    "types",
    "engine.config.magic10_v2_loader",
    "engine.config.registry_loader",
})
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


def _float_violations(path: Path) -> list[tuple[str, int]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found = []
    for node in ast.walk(tree):
        line = getattr(node, "lineno", 0)
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            found.append(("R1", line))
        elif isinstance(node, ast.Name) and node.id in ("float", "complex"):
            found.append(("R2", line))
        elif isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, ast.Div):
            found.append(("R3", line))
        elif isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, ast.Pow):
            found.append(("R4", line))
        elif isinstance(node, ast.Import) and any(
            alias.name.split(".")[0] in FORBIDDEN_MODULES for alias in node.names
        ):
            found.append(("R5", line))
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and (
            (node.module or "").split(".")[0] in FORBIDDEN_MODULES
        ):
            found.append(("R5", line))
        elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "math":
            found.append(("R6", line))
    return found


def test_no_binary_floating_point_in_the_package() -> None:
    modules = sorted(PACKAGE.glob("*.py"))
    assert {"__init__.py", "kernel.py"} <= {path.name for path in modules}
    violations = {path.name: _float_violations(path) for path in modules}
    assert violations == {path.name: [] for path in modules}


def _is_v1(name: str) -> bool:
    return any(name == prefix or name.startswith(prefix + ".") for prefix in V1_PREFIXES)


def test_kernel_imports_only_its_closed_set() -> None:
    tree = ast.parse(KERNEL.read_text(encoding="utf-8"), filename=str(KERNEL))
    plain = [node for node in ast.walk(tree) if isinstance(node, ast.Import)]
    from_modules = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert plain == []
    assert from_modules == KERNEL_IMPORTS
    assert not any(_is_v1(name) for name in from_modules)


def test_package_marker_imports_nothing() -> None:
    tree = ast.parse((PACKAGE / "__init__.py").read_text(encoding="utf-8"))
    assert not any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree))


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
import engine.magic10_v2.kernel
prefixes = ("engine.magic10", "engine.compat", "engine.core")
added = sorted(
    name for name in set(sys.modules) - before
    if any(name == prefix or name.startswith(prefix + ".") for prefix in prefixes)
)
print(len(opened))
print(",".join(added))
"""


def test_kernel_import_reads_no_file_and_loads_no_v1_module(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, "-I", "-c", _CHILD_IMPORT_AUDIT, str(ROOT)],
        capture_output=True, text=True, env=CLOSED_RAILS_ENV, cwd=tmp_path, check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.splitlines() == ["0", ""]
