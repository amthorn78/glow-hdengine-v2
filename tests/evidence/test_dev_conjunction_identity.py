from __future__ import annotations

import json
import os
import subprocess
import sys
import types
from pathlib import Path

import pytest

from engine.compat.identity import dev_compat_identity
from tools.evidence import generate_conjunction_writer_evidence as generator

ARTIFACTS = (
    Path("artifacts/writer/conjunction_write_readback.log"),
    Path("artifacts/writer/conjunction_writer_summary.json"),
)
OPEN_DEV_RAILS = {
    "APP_ENV": "dev",
    "SAFE_MODE": "0",
    "ALLOW_NETWORK": "1",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}


def test_dev_conjunction_identity_evidence_is_current_and_nonwriting():
    env = os.environ.copy()
    env.update(OPEN_DEV_RAILS)
    before = {path: path.read_bytes() for path in ARTIFACTS}

    subprocess.run(
        [
            sys.executable,
            "tools/evidence/generate_conjunction_writer_evidence.py",
            "--check",
        ],
        check=True,
        env=env,
    )

    assert {path: path.read_bytes() for path in ARTIFACTS} == before
    summary = json.loads(
        Path("artifacts/writer/conjunction_writer_summary.json").read_bytes()
    )
    assert summary["checks"]["writer_dev_identity"] is True
    assert summary["checks"]["reader_dev_identity"] is True
    assert dev_compat_identity() == {
        "engine_tag": "dev",
        "release_id": "dev",
        "invocation_tag": "INV-DEV",
    }


def test_check_mode_neutralizes_database_url_and_preserves_artifacts(monkeypatch):
    sentinel_dsn = "postgresql://sentinel-user:sentinel-pass@example.invalid:5432/hde"
    connect_calls: list[str] = []

    def fail_if_connect_called(*args, **kwargs):
        connect_calls.append("connect")
        pytest.fail("psycopg.connect must not be called by --check")

    monkeypatch.setenv("DATABASE_URL", sentinel_dsn)
    for key, value in OPEN_DEV_RAILS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setitem(
        sys.modules,
        "psycopg",
        types.SimpleNamespace(connect=fail_if_connect_called),
    )
    before = {path: path.read_bytes() for path in ARTIFACTS}

    assert generator.main(["--check"]) == 0

    assert connect_calls == []
    assert {path: path.read_bytes() for path in ARTIFACTS} == before
    assert os.environ["DATABASE_URL"] == sentinel_dsn


def test_check_mode_restores_database_url_when_capture_fails(monkeypatch):
    sentinel_dsn = "postgresql://sentinel-user:sentinel-pass@example.invalid:5432/hde"
    monkeypatch.setenv("DATABASE_URL", sentinel_dsn)

    def fail_capture():
        raise RuntimeError("expected capture failure")

    monkeypatch.setattr(generator, "_capture_outputs", fail_capture)

    with pytest.raises(RuntimeError, match="expected capture failure"):
        generator.main(["--check"])

    assert os.environ["DATABASE_URL"] == sentinel_dsn
