from __future__ import annotations

import ast
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PURE_PATH = "engine/charts/pure.py"
FORBIDDEN_ROOTS = {
    "os", "time", "datetime", "random", "secrets", "uuid", "socket", "subprocess",
    "pathlib", "io", "json", "logging", "decimal", "requests", "urllib", "http",
    "locale", "sqlite3", "psycopg", "redis", "importlib", "adapter",
}
FORBIDDEN_MODULE_PARTS = {
    "compat", "cli", "http", "cache", "narratives", "db", "vendor", "runtime",
    "config", "provider", "providers", "loader",
}
# engine.util.input_validators also holds file and randomness readers; only this
# pure helper may be imported from it.
VALIDATOR_MODULE = "engine.util.input_validators"
ALLOWED_VALIDATOR_NAMES = {"parse_time_hh_mm"}
FORBIDDEN_CALLS = {
    "open", "print", "eval", "exec", "compile", "__import__", "getenv", "read_text",
    "read_bytes", "write_text", "write_bytes", "getLogger", "ensure_cid",
    "parse_place_city_cc", "parse_tz_iana", "parse_date_yyyy_mm_dd", "_load_list",
}


def violations(source: str) -> list[str]:
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                if parts[0] in FORBIDDEN_ROOTS or FORBIDDEN_MODULE_PARTS & set(parts) or alias.name == VALIDATOR_MODULE:
                    found.append(f"import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            parts = (node.module or "").split(".")
            if parts[0] in FORBIDDEN_ROOTS or FORBIDDEN_MODULE_PARTS & set(parts):
                found.append(f"from {node.module} import")
            if node.module == VALIDATOR_MODULE and not {a.name for a in node.names} <= ALLOWED_VALIDATOR_NAMES:
                found.append(f"from {node.module} import {sorted(a.name for a in node.names)}")
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else ""
            )
            if name in FORBIDDEN_CALLS:
                found.append(f"call {name}")
    return found


def test_pure_module_has_no_forbidden_dependency_or_call():
    assert violations((ROOT / PURE_PATH).read_text(encoding="utf-8")) == []


def test_checker_flags_planted_violations():
    for planted in (
        "import os\n",
        "from datetime import datetime\n",
        "import engine.util.input_validators\n",
        "from engine.util.input_validators import ensure_cid\n",
        "from engine.util.input_validators import parse_date_yyyy_mm_dd\n",
        "from engine.config.provider_loader import resolve_provider\n",
        "from engine.charts.loader import load_chart\n",
        "import logging\n",
        "open('artifacts/logs/x')\n",
        "print('x')\n",
    ):
        assert violations(planted), planted


# Patches every time, randomness, environment, filesystem, logging, socket and
# subprocess entry point, then imports the module fresh and calls it.
HARNESS = r'''
import builtins, io, logging, os, pathlib, random, secrets, socket, subprocess, sys, time, uuid
from contextlib import ExitStack
from unittest.mock import patch
def forbidden(*args, **kwargs):
    raise AssertionError("external side effect")
def no_external_effects():
    guards = ExitStack()
    for owner, name in (
        (builtins, "open"), (io, "open"), (os, "open"), (pathlib.Path, "open"),
        (pathlib.Path, "read_text"), (pathlib.Path, "read_bytes"), (pathlib.Path, "write_text"),
        (pathlib.Path, "write_bytes"), (pathlib.Path, "mkdir"), (os, "getcwd"), (os, "getenv"),
        (os._Environ, "__getitem__"), (os._Environ, "__setitem__"), (time, "time"),
        (time, "time_ns"), (time, "monotonic"), (time, "perf_counter"), (time, "localtime"),
        (time, "gmtime"), (time, "strftime"), (time, "tzset"), (random, "random"),
        (random, "getrandbits"), (os, "urandom"), (secrets, "token_hex"), (uuid, "uuid4"),
        (socket, "socket"), (socket, "getaddrinfo"), (socket, "create_connection"),
        (subprocess, "Popen"), (logging.Logger, "_log"),
    ):
        guards.enter_context(patch.object(owner, name, forbidden))
    return guards
name = sys.argv[1]
assert name not in sys.modules and "engine.util.input_validators" not in sys.modules
with no_external_effects():
    module = __import__(name, fromlist=["*"])
if name == "engine.charts.pure":
    with no_external_effects():
        iso, iana = frozenset({"NL", "US"}), frozenset({"Europe/Amsterdam"})
        ok = module.validate_birth_inputs("1990-01-01", "12:34", "Amsterdam, NL", "Europe/Amsterdam", iso_codes=iso, iana_zones=iana)
        assert ok == ((1990, 1, 1), (12, 34), "Amsterdam", "NL", "Europe/Amsterdam"), ok
        for bad in (
            ("1990-02-30", "12:34", "Amsterdam, NL", "Europe/Amsterdam"),
            ("1990-01-01", "24:00", "Amsterdam, NL", "Europe/Amsterdam"),
            ("1990-01-01", "12:34", "Nowhere", "Europe/Amsterdam"),
            ("1990-01-01", "12:34", "Amsterdam, NL", None),
            ("1990-01-01", "12:34", "Amsterdam, NL", "Europe/NotARealCity"),
        ):
            try:
                module.validate_birth_inputs(*bad, iso_codes=iso, iana_zones=iana)
            except module.ChartInputError:
                pass
            else:
                raise SystemExit(f"accepted {bad}")
        assert module.normalize_chart({"gates": [1, "2", "x"], "type": ""}) == {"gates": [1, 2], "type": ""}
'''


def _run(name: str, extra_path: Path | None = None) -> subprocess.CompletedProcess:
    path = str(ROOT) if extra_path is None else os.pathsep.join((str(extra_path), str(ROOT)))
    env = dict(os.environ, PYTHONPATH=path, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, "-c", HARNESS, name], cwd=ROOT, env=env, text=True, capture_output=True)


def test_fresh_import_and_calls_have_no_external_side_effects():
    result = _run("engine.charts.pure")
    assert result.returncode == 0, result.stderr


def test_harness_flags_a_planted_side_effect(tmp_path):
    (tmp_path / "planted_effect.py").write_text("import os\nos.getenv('SAFE_MODE')\n", encoding="utf-8")
    result = _run("planted_effect", tmp_path)
    assert result.returncode != 0 and "external side effect" in result.stderr
