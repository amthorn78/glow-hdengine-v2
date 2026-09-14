from __future__ import annotations

import ast
import inspect
import os
from pathlib import Path
import subprocess
import sys

import pytest

from engine import core
from engine.core import compute_core

ROOT = Path(__file__).resolve().parents[2]
PURE_PATHS = (
    "engine/core/core.py", "engine/magic10/composite.py",
    "engine/magic10/signals.py", "engine/magic10/calculators.py",
)
FORBIDDEN_ROOTS = {
    "os", "time", "datetime", "random", "secrets", "uuid", "socket", "subprocess",
    "pathlib", "io", "json", "decimal", "requests", "urllib", "http", "locale",
    "sqlite3", "psycopg", "redis", "importlib",
}
FORBIDDEN_CALLS = {"open", "eval", "exec", "compile", "__import__", "getenv", "read_text", "read_bytes", "write_text", "write_bytes"}
TYPE_IMPORTS = {
    "ADMITTED_RELEASE_ROSTER", "AdmittedMechanicsBundle", "Channel", "Gate",
    "Magic10Caps", "Magic10Seed", "Manifest", "ManifestEntry", "RegistryConfig",
    "SourceIdentity", "FROZEN_CHANNEL_IDS",
}


@pytest.mark.parametrize("path", PURE_PATHS)
def test_all_pure_modules_have_no_forbidden_dependency_or_call(path):
    tree = ast.parse((ROOT / path).read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert all(a.name.split(".")[0] not in FORBIDDEN_ROOTS for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert (node.module or "").split(".")[0] not in FORBIDDEN_ROOTS
            assert not any(part in (node.module or "").split(".") for part in (
                "compat", "cli", "http", "cache", "narratives", "db", "vendor", "runtime",
            ))
            if node.module == "engine.config.registry_loader":
                assert {a.name for a in node.names} <= TYPE_IMPORTS
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else ""
            )
            assert name not in FORBIDDEN_CALLS


def test_fresh_pure_import_and_compute_have_no_external_side_effects(tmp_path):
    script = r'''
import builtins, importlib, os, pathlib, random, socket, subprocess, sys, time, uuid
from contextlib import ExitStack
from tempfile import TemporaryDirectory
from unittest.mock import patch
from engine.bodygraph.gates import normalize_gates
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_complete_release_root
def forbidden(*args, **kwargs):
    raise AssertionError("external side effect")
def no_external_effects():
    guards = ExitStack()
    for owner, name in (
        (builtins, "open"), (pathlib.Path, "read_text"), (pathlib.Path, "read_bytes"),
        (pathlib.Path, "write_text"), (pathlib.Path, "write_bytes"), (os, "getenv"),
        (os._Environ, "__getitem__"), (os._Environ, "__setitem__"),
        (time, "time"), (time, "monotonic"), (random, "random"), (uuid, "uuid4"),
        (socket, "socket"), (subprocess, "Popen"), (importlib, "reload"),
    ):
        guards.enter_context(patch.object(owner, name, forbidden))
    return guards
pure_names = {
    "engine.core.core", "engine.magic10.composite", "engine.magic10.signals",
    "engine.magic10.calculators",
}
assert pure_names.isdisjoint(sys.modules)
captured = []
original_frame = sys._getframe
def observe_frame(depth=0):
    frame = original_frame(depth + 1)
    if depth == 0 and frame.f_code.co_name == "<module>" and frame.f_globals.get("__name__") in pure_names:
        captured.append(frame.f_globals["__name__"])
    return frame
# Import must be genuinely fresh: admission now resolves the pure modules itself.
with no_external_effects(), patch.object(sys, "_getframe", observe_frame):
    from engine.core import compute_core
assert set(captured) == pure_names and len(captured) == 4
with TemporaryDirectory() as tmp:
    bundle = _load_active_mechanics_bundle_from_root(synthetic_complete_release_root(pathlib.Path(tmp)))
    a, b = normalize_gates([1, 8]), normalize_gates([1, 64])
    with no_external_effects(), ExitStack() as guards:
        for owner, name in (
            (builtins, "compile"), (builtins, "exec"), (builtins, "eval"),
            (builtins, "__import__"), (sys, "_getframe"),
        ):
            guards.enter_context(patch.object(owner, name, forbidden))
        result = compute_core(a, b, bundle, bundle.release_id)
        assert len(result.signals) == 20 and len(result.categories) == 10
        assert sercanon(result.to_payload())
'''
    env = dict(os.environ, PYTHONPATH=str(ROOT), PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run([sys.executable, "-c", script], cwd=ROOT, env=env, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr


def test_retired_surface_and_legacy_signature_refuse():
    for name in ("CoreConfig", "ParticipantState", "PerspectiveBreakdown"):
        assert not hasattr(core, name)
    assert tuple(inspect.signature(compute_core).parameters) == ("member_a", "member_b", "mechanics_bundle", "release_id")
    with pytest.raises(TypeError):
        compute_core({"compat_score": 50}, {"compat_score": 80}, {})
    with pytest.raises(TypeError):
        compute_core({}, {}, {}, "", config={})
