"""HDE-EPIC043 INV-5 for WU-PR-01: Stage A v2 code was unreachable from production.

Retired at the switch (HDE-EPIC043 WU-PR-09). INV-5 held "until WU-PR-09": the
switch re-targets the production entry points to the v2 layer, so its two
assertions -- no production entry point reaches ``engine.magic10_v2``, and
``_BUNDLE_PROVIDER`` is ``load_active_mechanics_bundle`` unchanged -- end here.
They are replaced by acceptance item 2's static proof in
``tests/m10_v2/test_switch.py`` (no retired module, fallback or selector is
reached, and the v2 package is).

``_static_closure`` and its helpers stay in place under their names:
``tests/scripts/test_m10_cutover_guard.py`` loads ``_static_closure`` from this
file for its closure-equality check.

Stated limit (of the helpers): the closure is static. It follows ``import`` and
``from … import`` at any depth (module level and inside functions) and resolves
relative imports; a name joins the closure when ``<name>.py`` or
``<name>/__init__.py`` exists under the repository root, so third-party and
standard-library modules are not followed. A dynamic import through a computed
string is not followed. Entry points are parsed, never imported, and module
names are derived from file paths.
"""
from __future__ import annotations

import ast
from pathlib import Path

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
