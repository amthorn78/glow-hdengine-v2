import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.evidence import generate_env_matrix_snapshot as generator

DEFAULT_RAILS = {
    "CI": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
    "dev": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
    "prod": {"ALLOW_NETWORK": "1", "SAFE_MODE": "0"},
    "stage": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
}
DETERMINISM_PINS = {"LANG": "C", "LC_ALL": "C", "TZ": "UTC"}
PRESENCE = {
    "DATABASE_URL": False,
    "DB_BRIDGE_URL": False,
    "db_allow_bridge_in_prod": False,
}
EXPECTED = {
    "schema_version": 3,
    "default_rails": DEFAULT_RAILS,
    "determinism_pins": DETERMINISM_PINS,
    "presence": PRESENCE,
    "notes": [],
}
OPTIONAL_DB_ENV = ("DATABASE_URL", "DB_BRIDGE_URL", "DB_ALLOW_BRIDGE_IN_PROD")


def _set_closed_rails(monkeypatch):
    for key, value in generator.GENERATION_ENV.items():
        monkeypatch.setenv(key, value)


def _canonical_bytes(payload):
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def test_env_matrix_v3_write_is_independent_of_optional_db_env(tmp_path, monkeypatch):
    _set_closed_rails(monkeypatch)
    out = tmp_path / "env_matrix.snapshot.json"
    monkeypatch.setattr(generator, "OUT", out)

    for key in OPTIONAL_DB_ENV:
        monkeypatch.delenv(key, raising=False)
    assert generator.main([]) == 0
    without_optional_env = out.read_bytes()

    for key in OPTIONAL_DB_ENV:
        monkeypatch.setenv(key, "operator-specific-value")
    assert generator.main([]) == 0

    assert out.read_bytes() == without_optional_env
    assert json.loads(without_optional_env) == EXPECTED


def test_env_matrix_v3_check_is_exact_and_nonwriting(monkeypatch):
    _set_closed_rails(monkeypatch)
    for key in OPTIONAL_DB_ENV:
        monkeypatch.setenv(key, "operator-specific-value")

    path = Path("artifacts/runtime/env_matrix.snapshot.json")
    before = path.read_bytes()
    subprocess.run(
        [sys.executable, "tools/evidence/generate_env_matrix_snapshot.py", "--check"],
        check=True,
    )

    assert path.read_bytes() == before
    assert before.endswith(b"\n") and b"\n" not in before[:-1]
    assert json.loads(before) == EXPECTED
    assert b"operator-specific-value" not in before
    assert all(type(value) is bool for value in json.loads(before)["presence"].values())


def test_env_matrix_v3_check_rejects_unknown_keys(tmp_path, monkeypatch):
    _set_closed_rails(monkeypatch)
    out = tmp_path / "env_matrix.snapshot.json"
    monkeypatch.setattr(generator, "OUT", out)

    unexpected_top_level = {**EXPECTED, "unexpected": True}
    unexpected_nested = json.loads(json.dumps(EXPECTED))
    unexpected_nested["default_rails"]["CI"]["unexpected"] = "0"

    for drift in (unexpected_top_level, unexpected_nested):
        out.write_bytes(_canonical_bytes(drift))
        with pytest.raises(SystemExit) as exc:
            generator.main(["--check"])
        assert str(exc.value).startswith("DRIFT:")


def test_rails_closed_phase1_delegates_env_matrix_ownership():
    source = Path("tools/evidence/generate_rails_closed_phase1.py").read_text(
        encoding="utf-8"
    )

    assert "generate_env_matrix_snapshot.main([])" in source
    assert "db_access.resolve_env_matrix()" not in source
    assert '_write_json("artifacts/runtime/env_matrix.snapshot.json"' not in source


def test_env_matrix_v3_consumers_use_canonical_singleton_contract():
    qa_source = Path("scripts/qa/epic009_precommit.sh").read_text(
        encoding="utf-8"
    )
    ingest_source = Path("scripts/ingest/run_vendor_ingest.py").read_text(
        encoding="utf-8"
    )

    assert "generate_env_matrix_snapshot.py --check" in qa_source
    assert 'snap.get("result"' not in qa_source
    assert 'snap.get("checks"' not in qa_source
    assert "env_matrix.snapshot.json" not in ingest_source
    assert "_capture_env_snapshot" not in ingest_source
