from __future__ import annotations

import hashlib
import hmac
import http.client
import json
import os
import subprocess
import sys
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

import pytest
from jsonschema import Draft202012Validator, ValidationError

import engine.bodygraph.resolver as resolver_module
import engine.bodygraph.vendor_client as vendor_client_module
import engine.db.adapter as db_adapter_module
import engine.db.providers.psycopg_provider as psycopg_provider_module
import engine.ops.http_log as http_log_module
from engine.bodygraph.resolver import ResolveBodygraphResult
from tools.evidence import generate_v2_mapped_cache_evidence as generator

ROOT = Path(__file__).resolve().parents[2]
RETAINED_RECORD = b'{"at":"2026-07-16T18:26:14.958Z","duration_ms":737.062,"route":"db_bridge.get:/health","status":200}'
GOVERNED_COMPANIONS = (
    ROOT / "artifacts/logs/keys_only.sample.jsonl.path_proof.txt",
    ROOT / "docs/evidence/INDEX.json",
    ROOT / "docs/evidence/INDEX.sha256",
    ROOT / "docs/evidence/INDEX.json.path_proof.txt",
    ROOT / "docs/evidence/INDEX.sha256.path_proof.txt",
    ROOT / "artifacts/evidence_index.jsonl",
    ROOT / "artifacts/evidence_index.jsonl.sha256",
    ROOT / "artifacts/evidence_index.jsonl.path_proof.txt",
    ROOT / "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    ROOT / "audit/gates/topology/orientation_demo.txt",
    ROOT / "audit/gates/topology/orientation_demo.txt.path_proof.txt",
    *(ROOT / f"artifacts/bodygraph/v2_mapped_cache/{name}.path_proof.txt" for name in generator.PRIMARY_NAMES),
    ROOT / "schemas/bodygraph_v2_mapped_cache_transcript.v1.json.path_proof.txt",
    ROOT / "schemas/bodygraph_v2_mapped_cache_manifest.v1.json.path_proof.txt",
)


def _bytes_and_mtimes(paths) -> dict[Path, tuple[bytes, int]]:
    return {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}


def _governed_state() -> dict[Path, bytes]:
    return {path: path.read_bytes() for path in GOVERNED_COMPANIONS}


def _shared_log_state() -> tuple[bool, bytes | None, str | None]:
    exists = generator.SHARED_HTTP_LOG.exists()
    data = generator.SHARED_HTTP_LOG.read_bytes() if exists else None
    return exists, data, hashlib.sha256(data).hexdigest() if data is not None else None


def _repo_inventory() -> set[str]:
    ignored = {".git", ".venv", "__pycache__", ".pytest_cache"}
    return {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and not ignored.intersection(path.relative_to(ROOT).parts)
    }


def _stage_inventory() -> set[str]:
    return {path.name for path in ROOT.parent.glob("hde-epic038-pr05-*")}


def _command_env(**changes: str) -> dict[str, str]:
    env = dict(os.environ)
    env.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "PYTHONDONTWRITEBYTECODE": "1"})
    env.update(changes)
    return env


def _redacted_environment_value(redaction_key: bytes, name: str, value: str) -> str:
    return hmac.new(
        redaction_key,
        f"{name}\0{value}".encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def _redacted_environment_snapshot(redaction_key: bytes) -> dict[str, tuple[bool, str | None]]:
    """Return assertion-safe environment state without retaining raw values."""

    snapshot: dict[str, tuple[bool, str | None]] = {}
    for name in generator.HERMETIC_ENV_KEYS:
        if name not in os.environ:
            snapshot[name] = (False, None)
            continue
        digest = _redacted_environment_value(redaction_key, name, os.environ[name])
        snapshot[name] = (True, digest)
    return snapshot


def _forbidden(name: str, calls: dict[str, int]):
    calls[name] = 0

    def canary(*_args, **_kwargs):
        calls[name] += 1
        raise generator.HermeticityViolation(f"TEST_FORBIDDEN_SEAM:{name}")

    return canary


def _wrap_build_with_canaries(
    monkeypatch,
    targets,
    observations: dict[str, object],
    redaction_key: bytes,
) -> dict[str, int]:
    actual = generator._build_files
    calls: dict[str, int] = {}

    def guarded_build(guard, *, force_failure=False):
        observations["inside_env"] = _redacted_environment_snapshot(redaction_key)
        observations["production_canaries"] = dict(guard.attempts)
        with ExitStack() as stack:
            for name, owner, attribute in targets:
                stack.enter_context(patch.object(owner, attribute, _forbidden(name, calls)))
            return actual(guard, force_failure=force_failure)

    monkeypatch.setattr(generator, "_build_files", guarded_build)
    return calls


def test_exact_primary_inventory_and_canonical_outputs() -> None:
    files = generator.build()
    relative = {path.relative_to(ROOT).as_posix() for path in files}
    expected = {f"artifacts/bodygraph/v2_mapped_cache/{name}" for name in generator.PRIMARY_NAMES} | {
        "schemas/bodygraph_v2_mapped_cache_transcript.v1.json", "schemas/bodygraph_v2_mapped_cache_manifest.v1.json"}
    assert relative == expected
    for path, data in files.items():
        assert data.endswith(b"\n") and not data.endswith(b"\n\n") and b"\r\n" not in data
        assert not path.name.endswith(".path_proof.txt")


def test_schema_validation_unknown_keys_and_manifest_bindings() -> None:
    files = generator.build()
    transcript_schema = json.loads(files[generator.TRANSCRIPT_SCHEMA])
    manifest_schema = json.loads(files[generator.MANIFEST_SCHEMA])
    write = json.loads(files[generator.OUT / "write_transcript.json"])
    manifest = json.loads(files[generator.OUT / "manifest.json"])
    Draft202012Validator(transcript_schema).validate(write)
    Draft202012Validator(manifest_schema).validate(manifest)
    bad = dict(write); bad["unknown"] = True
    with pytest.raises(ValidationError): Draft202012Validator(transcript_schema).validate(bad)
    bad = json.loads(files[generator.OUT / "write_transcript.json"]); bad["identity"]["unknown"] = True
    with pytest.raises(ValidationError): Draft202012Validator(transcript_schema).validate(bad)
    assert manifest["status"] == ("PASS" if all(manifest["predicates"].values()) else "FAIL")
    for binding in manifest["artifacts"] + manifest["schemas"]:
        data = files[ROOT / binding["path"]]
        assert binding["sha256"] == hashlib.sha256(data).hexdigest() and binding["size"] == len(data)


def test_shared_primary_remains_byte_identical_for_build_and_real_check() -> None:
    before = _shared_log_state()
    original_log_path = http_log_module.LOG_PATH
    generator.build()
    assert _shared_log_state() == before
    assert http_log_module.LOG_PATH is original_log_path
    result = subprocess.run(
        [sys.executable, str(generator.__file__), "--check"], cwd=ROOT, env=_command_env(),
        check=True, capture_output=True, text=True,
    )
    assert result.stdout == "V2_MAPPED_CACHE_EVIDENCE_OK\n" and result.stderr == ""
    assert _shared_log_state() == before
    assert http_log_module.LOG_PATH is original_log_path


def test_environment_assertion_snapshot_redacts_ambient_values(monkeypatch) -> None:
    ambient = {
        "DATABASE_URL": "postgresql://user:password@database.invalid/db",
        "HD_API_BASE_URL": "https://vendor-with-private-base.invalid/v2",
        "HD_API_KEY": "private-api-key-marker",
        "GEO_API_KEY": "private-geo-key-marker",
    }
    for name, value in ambient.items():
        monkeypatch.setenv(name, value)

    snapshot = _redacted_environment_snapshot(os.urandom(32))
    rendered = repr(snapshot)

    assert all(snapshot[name][0] and len(snapshot[name][1] or "") == 64 for name in ambient)
    assert all(value not in rendered for value in ambient.values())


def test_traceback_locals_redact_raw_environment_restore_state(tmp_path) -> None:
    sentinels = {
        "DATABASE_URL": "postgresql://trace-user:trace-password@database.invalid/db",
        "HD_API_BASE_URL": "https://trace-private-vendor.invalid/v2",
        "HDAPI_BASE_URL": "https://trace-private-legacy.invalid/v1",
        "HD_API_KEY": "trace-private-api-key",
        "GEO_API_KEY": "trace-private-geo-key",
    }
    child_test = tmp_path / "test_environment_restore_traceback.py"
    child_test.write_text(
        """from tools.evidence import generate_v2_mapped_cache_evidence as generator


def test_unhandled_failure_inside_hermetic_boundary(monkeypatch):
    def injected_restore(self):
        raise RuntimeError(\"INJECTED_RESTORE_TRACEBACK_FAILURE\")

    monkeypatch.setattr(generator._EnvironmentRestoreState, \"restore\", injected_restore)
    generator.build()
""",
        encoding="utf-8",
    )
    env = _command_env(**sentinels)
    env["PYTHONPATH"] = os.pathsep.join(filter(None, (str(ROOT), env.get("PYTHONPATH", ""))))

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--showlocals", "--tb=long", "-q", str(child_test)],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr

    assert result.returncode == 1
    assert "INJECTED_RESTORE_TRACEBACK_FAILURE" in output
    assert "values=<redacted>" in output
    assert all(value not in output for value in sentinels.values())


def test_ambient_db_configuration_cannot_escape_and_environment_restores(monkeypatch) -> None:
    for key, value in {
        "DATABASE_URL": "postgresql://sentinel.invalid/db",
        "DB_ALLOW_BRIDGE_IN_PROD": "1",
        "DB_BRIDGE_URL": "https://bridge.invalid",
        "DB_FORCE_BRIDGE": "1",
        "HDE_KEYS_ONLY_LOG_PATH": "/tmp/must-not-use.jsonl",
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
        "APP_ENV": "production",
    }.items():
        monkeypatch.setenv(key, value)
    monkeypatch.delenv("ENGINE_ENV", raising=False)
    redaction_key = os.urandom(32)
    caller_env = _redacted_environment_snapshot(redaction_key)
    shared = _shared_log_state()
    observations: dict[str, object] = {}
    calls = _wrap_build_with_canaries(monkeypatch, (
        ("dbaccess", resolver_module.DBAccess, "for_current_env"),
        ("psycopg_ctor", db_adapter_module, "PsycopgProvider"),
        ("psycopg_connect", psycopg_provider_module.PsycopgProvider, "_connect"),
    ), observations, redaction_key)
    generator.build()
    inside = observations["inside_env"]
    assert all(
        inside[key] == (True, _redacted_environment_value(redaction_key, key, value))
        for key, value in generator.DETERMINISM_ENV_PINS.items()
    )
    assert all(inside[key] == (False, None) for key in generator._CONNECTION_ENV_KEYS)
    assert calls and set(calls.values()) == {0}
    assert observations["production_canaries"] and set(observations["production_canaries"].values()) == {0}
    assert _redacted_environment_snapshot(redaction_key) == caller_env
    assert _shared_log_state() == shared


def test_ambient_vendor_configuration_cannot_escape_in_build_or_check(monkeypatch) -> None:
    for key, value in {
        "HD_API_BASE_URL": "https://vendor.invalid/v2",
        "HDAPI_BASE_URL": "https://legacy.invalid/v1",
        "HD_API_KEY": "sentinel-api-key",
        "GEO_API_KEY": "sentinel-geo-key",
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
    }.items():
        monkeypatch.setenv(key, value)
    redaction_key = os.urandom(32)
    caller_env = _redacted_environment_snapshot(redaction_key)
    shared = _shared_log_state()
    observations: dict[str, object] = {}
    calls = _wrap_build_with_canaries(monkeypatch, (
        ("vendor_from_env", resolver_module.HdApiClient, "from_env"),
        ("vendor_fetch", vendor_client_module.HdApiClient, "fetch"),
        ("vendor_request", vendor_client_module.HdApiClient, "_default_request"),
        ("vendor_opener", vendor_client_module.urlrequest, "build_opener"),
        ("dns", vendor_client_module.socket, "getaddrinfo"),
        ("socket", vendor_client_module.socket, "create_connection"),
        ("http", http.client.HTTPConnection, "connect"),
        ("https", http.client.HTTPSConnection, "connect"),
    ), observations, redaction_key)
    generator.build()
    assert calls and set(calls.values()) == {0}
    assert _redacted_environment_snapshot(redaction_key) == caller_env
    result = subprocess.run(
        [sys.executable, str(generator.__file__), "--check"], cwd=ROOT,
        env=_command_env(
            HD_API_BASE_URL="https://vendor.invalid/v2", HDAPI_BASE_URL="https://legacy.invalid/v1",
            HD_API_KEY="sentinel-api-key", GEO_API_KEY="sentinel-geo-key", SAFE_MODE="0", ALLOW_NETWORK="1",
        ), check=True, capture_output=True, text=True,
    )
    assert result.stdout == "V2_MAPPED_CACHE_EVIDENCE_OK\n" and result.stderr == ""
    assert _shared_log_state() == shared


def test_mapped_cache_tool_has_no_retired_provider_import():
    source = Path("tools/evidence/generate_v2_mapped_cache_evidence.py").read_text()
    assert "bridge_provider" not in source
    assert "BridgeProvider" not in source
