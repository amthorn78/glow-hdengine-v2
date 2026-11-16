"""HDE-EPIC043 INV-5 for WU-PR-01: Stage A v2 code is unreachable from production.

The static import closure of the three production entry points
(``adapter/factory.py``, ``engine/cli/main.py``, ``engine/http/compat_handler.py``)
contains no module of ``engine.magic10_v2``, and ``_BUNDLE_PROVIDER`` stays
``load_active_mechanics_bundle``.

Stated limit: the closure is static. It follows ``import`` and ``from … import``
at any depth (module level and inside functions) and resolves relative imports;
a name joins the closure when ``<name>.py`` or ``<name>/__init__.py`` exists under
the repository root, so third-party and standard-library modules are not
followed. A dynamic import through a computed string is not followed; the test
also refuses any string constant naming the package in a closure module. Entry
points are parsed, never imported, and module names are derived from file paths.
"""
from __future__ import annotations

import ast
from pathlib import Path

from engine.compat import compute
from engine.config.registry_loader import load_active_mechanics_bundle

ROOT = Path(__file__).resolve().parents[2]
ENTRY_POINTS = ("adapter/factory.py", "engine/cli/main.py", "engine/http/compat_handler.py")
V2_PACKAGE = "engine.magic10_v2"
V2_TEXT = ("engine.magic10_v2", "engine/magic10_v2")


def _module_name(path: Path) -> str:
    parts = list(path.relative_to(ROOT).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _module_file(name: str) -> Path | None:
    base = ROOT.joinpath(*name.split("."))
    if base.with_suffix(".py").is_file():
        return base.with_suffix(".py")
    if (base / "__init__.py").is_file():
        return base / "__init__.py"
    return None


def _imported_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    own = _module_name(path)
    package = own if path.name == "__init__.py" else own.rpartition(".")[0]
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package.split(".") if package else []
                if node.level > 1:
                    base = base[: len(base) - (node.level - 1)]
                module = ".".join(base + ([node.module] if node.module else []))
            else:
                module = node.module or ""
            parts = module.split(".")
            names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
            names.update(f"{module}.{alias.name}" for alias in node.names)
    return names


def _static_closure() -> dict[str, Path]:
    seen: dict[str, Path] = {}
    queue = [ROOT / entry for entry in ENTRY_POINTS]
    while queue:
        path = queue.pop()
        name = _module_name(path)
        if name in seen:
            continue
        seen[name] = path
        for imported in _imported_names(path):
            target = _module_file(imported)
            if target is not None and _module_name(target) not in seen:
                queue.append(target)
    return seen


def test_no_production_entry_point_reaches_the_v2_package() -> None:
    closure = _static_closure()
    assert {"engine.compat.compute", "engine.magic10.composite", "engine.cli.main"} <= set(closure)
    reached = sorted(name for name in closure if name == V2_PACKAGE or name.startswith(V2_PACKAGE + "."))
    assert reached == []
    naming = []
    for name, path in sorted(closure.items()):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and any(
                text in node.value for text in V2_TEXT
            ):
                naming.append((name, node.lineno))
    assert naming == []


def test_active_bundle_provider_is_unchanged() -> None:
    assert compute._BUNDLE_PROVIDER is load_active_mechanics_bundle
