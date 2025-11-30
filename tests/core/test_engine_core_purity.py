from __future__ import annotations

import ast
import importlib
from pathlib import Path

from engine.runtime.determinism_env import ensure_determinism_env

CORE_MODULE = "engine.core.core"
CORE_PATH = Path(__file__).resolve().parents[2] / "engine" / "core" / "core.py"
FORBIDDEN_ROOT_IMPORTS = {
    "os",
    "time",
    "datetime",
    "random",
    "socket",
    "subprocess",
}
FORBIDDEN_TEXT_SNIPPETS = (
    "os.environ",
    "time.",
    "datetime.",
    "random.",
    "socket.",
)


def test_engine_core_avoids_forbidden_imports() -> None:
    tree = ast.parse(CORE_PATH.read_text())

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                root = alias.name.split(".")[0]
                assert root not in FORBIDDEN_ROOT_IMPORTS


def test_engine_core_text_is_pure_compute() -> None:
    text = CORE_PATH.read_text()
    for snippet in FORBIDDEN_TEXT_SNIPPETS:
        assert snippet not in text


def test_engine_core_import_has_no_side_effects() -> None:
    ensure_determinism_env(apply=True)
    importlib.invalidate_caches()
    module = importlib.import_module(CORE_MODULE)
    importlib.reload(module)
