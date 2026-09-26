"""F07 (PF10 §2.23): dev conjunction writer/readback evidence is a closed-rails
deterministic capture through the real admission owner, with the app-config lookup
seam installed only by the generator and the admitted release identity on the routes."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import types
from pathlib import Path

import pytest

from engine.runtime.identity import identity_meta
from tests.support.pr04_fixtures import CLOSED_RAILS, build_bundle, build_pack, inject_seams
from tools.evidence import generate_conjunction_writer_evidence as generator

ARTIFACTS = (
    Path("artifacts/writer/conjunction_write_readback.log"),
    Path("artifacts/writer/conjunction_writer_summary.json"),
)
VENDOR_AND_DB_KEYS = ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL")
CHECKS = (
    "seam_absent_refuses_closed_rails",
    "writer_status_200",
    "reader_status_200",
    "writer_bytes_two_run_equal",
    "writer_payload_two_run_equal",
    "writer_result_reader_readback_equal",
    "writer_success_typed_envelope",
    "writer_error_typed_envelope",
    "writer_admitted_release_identity",
    "reader_admitted_release_identity",
    "no_dev_identity_stamp",
)


@pytest.fixture(autouse=True)
def _closed_rails_without_vendor_or_db(monkeypatch):
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)
    for name in VENDOR_AND_DB_KEYS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("legacy ingest attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))


def _subprocess_env() -> dict[str, str]:
    env = {name: value for name, value in os.environ.items() if name not in VENDOR_AND_DB_KEYS}
    env.update(CLOSED_RAILS)
    return env


# --- real admission owner: the tracked artifacts are current ----------------------------------

def test_dev_conjunction_identity_evidence_is_current_and_nonwriting():
    before = {path: path.read_bytes() for path in ARTIFACTS}

    subprocess.run(
        [sys.executable, "tools/evidence/generate_conjunction_writer_evidence.py", "--check"],
        check=True,
        env=_subprocess_env(),
    )

    assert {path: path.read_bytes() for path in ARTIFACTS} == before
    summary = json.loads(Path("artifacts/writer/conjunction_writer_summary.json").read_bytes())
    assert summary["schema"] == "conjunction_writer_summary.v2"
    assert summary["rails"] == "closed"
    assert set(summary["checks"]) == set(CHECKS)
    assert all(summary["checks"][name] is True for name in CHECKS)
    assert summary["release_id"] == identity_meta()["release_id"]
    assert summary["checks"]["no_dev_identity_stamp"] is True
    log = Path("artifacts/writer/conjunction_write_readback.log").read_text(encoding="utf-8")
    assert log.startswith("schema=conjunction_write_readback.log.v2\nrails=closed\n")
    assert f"release_id={identity_meta()['release_id']}\n" in log
    assert "dev_identity" not in log


def test_check_mode_neutralizes_database_url_and_preserves_artifacts(monkeypatch):
    sentinel_dsn = "postgresql://sentinel-user:sentinel-pass@example.invalid:5432/hde"
    connect_calls: list[str] = []

    def fail_if_connect_called(*args, **kwargs):
        connect_calls.append("connect")
        pytest.fail("psycopg.connect must not be called by --check")

    monkeypatch.setenv("DATABASE_URL", sentinel_dsn)
    monkeypatch.setitem(sys.modules, "psycopg", types.SimpleNamespace(connect=fail_if_connect_called))
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


def test_check_mode_never_constructs_a_vendor_client_even_with_credentials(monkeypatch):
    """Credentials in the environment change nothing: the capture is in-process and closed."""
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.setenv("HD_API_KEY", "set")
    monkeypatch.setenv("GEO_API_KEY", "set")
    assert generator.main(["--check"]) == 0


# --- refusals and seam facts (independent of the tracked artifacts) ---------------------------

@pytest.mark.parametrize(("safe_mode", "allow_network"), [("0", "1"), ("0", "0"), ("1", "1")])
def test_generator_refuses_open_rails_and_writes_nothing(monkeypatch, safe_mode, allow_network):
    monkeypatch.setenv("SAFE_MODE", safe_mode)
    monkeypatch.setenv("ALLOW_NETWORK", allow_network)
    monkeypatch.setattr(generator, "create_app", lambda *a, **k: pytest.fail("app created under open rails"))
    before = {path: path.read_bytes() for path in ARTIFACTS}
    with pytest.raises(SystemExit) as excinfo:
        generator.main([])
    assert "closed rails" in str(excinfo.value)
    with pytest.raises(SystemExit):
        generator.main(["--check"])
    assert {path: path.read_bytes() for path in ARTIFACTS} == before


def test_write_mode_neutralizes_database_url_too(monkeypatch, tmp_path):
    sentinel_dsn = "postgresql://sentinel-user:sentinel-pass@example.invalid:5432/hde"
    monkeypatch.setenv("DATABASE_URL", sentinel_dsn)
    seen: list[object] = []

    def capture():
        seen.append(os.environ.get("DATABASE_URL"))
        return {tmp_path / "log": b"x\n", tmp_path / "summary.json": b"{}\n"}

    monkeypatch.setattr(generator, "_capture_outputs", capture)
    assert generator.main([]) == 0
    assert seen == [None]
    assert os.environ["DATABASE_URL"] == sentinel_dsn
    assert (tmp_path / "log").read_bytes() == b"x\n"


def test_capture_under_the_injected_release_proves_the_seam_and_the_admitted_identity(monkeypatch, tmp_path):
    """The injected synthetic complete release exercises the whole capture in-process:
    the control request refuses without the seam, the seam serves the three routes, and
    the compat result carries the admitted bundle's release_id (never a dev stamp)."""
    bundle = build_bundle(tmp_path / "bundle")
    inject_seams(monkeypatch, bundle, build_pack(tmp_path / "pack"))
    monkeypatch.setattr(generator, "identity_meta", lambda: {**identity_meta(), "release_id": bundle.release_id})
    outputs = generator._capture_outputs()
    summary = json.loads(outputs[generator.WRITER_SUMMARY])
    assert summary["schema"] == "conjunction_writer_summary.v2" and summary["rails"] == "closed"
    assert summary["release_id"] == bundle.release_id
    assert all(summary["checks"][name] is True for name in CHECKS)
    log = outputs[generator.WRITE_READBACK_LOG].decode("utf-8")
    assert "control_status=503\n" in log and "seam_absent_refuses_closed_rails=true\n" in log
    # Two captures are byte-identical (deterministic in-process evidence).
    assert generator._capture_outputs() == outputs


def test_fixture_rows_are_complete_current_view_rows_for_the_engine_keys():
    from engine.bodygraph.ingest import resolve_db_user_id

    rows = generator._fixture_rows()
    assert set(rows) == {resolve_db_user_id("left"), resolve_db_user_id("right")}
    for canonical_id, row in rows.items():
        assert row.user_id == canonical_id and row.vendor == "hdapi" and row.vendor_version == 2
        assert len(row.input_fingerprint) == 64
        assert row.payload["person_uid"] == canonical_id
