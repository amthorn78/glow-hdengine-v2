"""Determinism gate generator (release-sanity stage 04).

Positive matrix: the synthetic complete release is injected through the
evaluation seam and the CLI runs in-process, so no subprocess or gate ever sees
a synthetic release.  Non-admitted matrix (PF10 §2.15): with the real admission
owner the generator raises the typed outcome before any live capture, prints
its explicit line, exits with the distinct code and writes nothing.
"""
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

import pytest

from engine.cli.main import cli
from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams
from tools.evidence import generate_determinism_gate_proofs as g
from tools.evidence import run_sanity_pipeline as release_sanity

CANON_OK = {"command": "test canon", "passed": True, "returncode": 0}


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-determinism-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-determinism-pack"))


def _in_process_cli_bytes(left=g.LEFT, right=g.RIGHT) -> bytes:
    """The CLI file path in-process (a subprocess cannot receive the injected bundle)."""

    with tempfile.TemporaryDirectory() as raw:
        td = Path(raw)
        a_path, b_path, dump = td / "a.json", td / "b.json", td / "reader.json"
        a_path.write_bytes(g.cjson(left))
        b_path.write_bytes(g.cjson(right))
        assert cli(["showcompat", "--a-file", str(a_path), "--b-file", str(b_path), "--dump-reader", str(dump)]) == 0
        return dump.read_bytes()


@pytest.fixture
def admitted(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    monkeypatch.setattr(g, "cli_bytes", _in_process_cli_bytes)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    return bundle


def _redirect_outputs(monkeypatch, tmp_path):
    paths = {
        "AB": tmp_path / "ab.json",
        "BA": tmp_path / "ba.json",
        "SUM": tmp_path / "summary.json",
        "ABB": tmp_path / "abba.bytes",
        "TWO": tmp_path / "tworun_identity.sha256",
        "ID": tmp_path / "IDENTITY_OK.txt",
    }
    for name, path in paths.items():
        monkeypatch.setattr(g, name, path)
    return paths


# --- positive matrix under the injected synthetic complete release ---------------------------

def test_successful_fixed_corpus_generation_predicates(admitted):
    top, outs = g.build(canon_gate=CANON_OK)
    assert top
    summary = json.loads(outs[g.SUM])
    assert summary["predicates"]["reader_cli_byte_identity"]
    assert summary["predicates"]["abba_byte_identity"]
    assert summary["predicates"]["two_run_byte_identity"]
    assert summary["predicates"]["preimage_hash_match"]
    assert summary["predicates"]["canonical_reserialization"]
    assert summary["canonical_gate"]["passed"] is True
    assert summary["fixtures"] == {"left": "fixtures/charts/alice.json", "right": "fixtures/charts/bob.json"}
    envelope = json.loads(outs[g.AB])
    assert envelope["eligible"] is True
    assert envelope["categories"] == [{"band": envelope["categories"][0]["band"], "id": "harmony"}]
    assert envelope["release_id"] == admitted.release_id


def test_canonical_gate_result_pins_the_stable_command(admitted):
    top, outs = g.build()
    summary = json.loads(outs[g.SUM])
    assert summary["canonical_gate"]["command"] == "python tools/evidence/run_canonical_json_gate.py --check-only"
    assert summary["predicates"]["canonical_gate_check"] is summary["canonical_gate"]["passed"]
    assert top is summary["top_level_pass"]


def test_mismatched_abba_fails_top_level(admitted):
    top, _ = g.build(canon_gate=CANON_OK, ba_override=b'{"bad":true}\n')
    assert not top


def test_failed_canonical_comparison_fails_top_level(admitted):
    top, _ = g.build(canon_gate={"command": "test seam", "passed": False, "returncode": 1})
    assert not top


def test_unavailable_canonical_gate_fails_closed(admitted):
    top, _ = g.build(canon_gate={"passed": True})
    assert not top


def test_check_mode_model_matches_committed_after_generation(admitted):
    top, outs = g.build(canon_gate=CANON_OK)
    assert top
    for _path, body in outs.items():
        assert body.endswith(b"\n")


def test_no_partial_evidence_when_predicate_failure(admitted, monkeypatch, tmp_path):
    monkeypatch.setattr(g, "ID", tmp_path / "IDENTITY_OK.txt")
    top, _ = g.build(canon_gate=CANON_OK, ba_override=b"{}\n")
    assert not top
    assert not (tmp_path / "IDENTITY_OK.txt").exists()


def test_main_write_mode_produces_exact_expected_files(admitted, monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: dict(CANON_OK))
    g.main([])
    assert set(p.name for p in tmp_path.iterdir()) == {p.name for p in paths.values()}
    assert paths["ID"].read_text(encoding="utf-8").startswith("IDENTITY_OK\n")


def test_main_check_mode_makes_no_file_changes(admitted, monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: dict(CANON_OK))
    top, outs = g.build(canon_gate=CANON_OK)
    assert top
    for p, b in outs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
    before = {p: p.read_bytes() for p in outs}
    g.main(["--check"])
    assert {p: p.read_bytes() for p in outs} == before
    assert set(paths) == {"AB", "BA", "SUM", "ABB", "TWO", "ID"}


def test_main_failure_writes_no_marker(admitted, monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: {"command": "test canon", "passed": False, "returncode": 1})
    with pytest.raises(SystemExit, match="DETERMINISM_PREDICATES_FAILED"):
        g.main([])
    assert not any(path.exists() for path in paths.values())


# --- non-admitted matrix with the real admission owner (no injection) ------------------------

def _forbid_live_capture(monkeypatch):
    monkeypatch.setattr(g.subprocess, "run", lambda *a, **k: pytest.fail("CLI subprocess spawned"))
    monkeypatch.setattr(g, "runtime_bytes", lambda *a, **k: pytest.fail("live Reader envelope emitted"))
    monkeypatch.setattr(g, "cli_bytes", lambda *a, **k: pytest.fail("CLI capture attempted"))
    monkeypatch.setattr(g, "canonical_gate_result", lambda *a, **k: pytest.fail("canonical gate spawned"))


def _refuse_admission(monkeypatch):
    """The repository root is admitted; the non-admitted branch is reached through the seam."""

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)


def test_build_and_check_succeed_on_the_admitted_root(monkeypatch, tmp_path):
    """On the admitted repository root the live build reproduces the tracked outputs byte for byte."""
    for name, value in {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    tracked = {name: Path(getattr(g, name)) for name in ("AB", "BA", "SUM", "ABB", "TWO", "ID")}
    paths = _redirect_outputs(monkeypatch, tmp_path)
    assert release_sanity.release_not_admitted_observed() is False
    g.main([])
    for name, path in paths.items():
        assert path.read_bytes() == tracked[name].read_bytes(), name
    g.main(["--check"])


def test_build_raises_typed_release_not_admitted_before_any_live_capture(monkeypatch):
    _refuse_admission(monkeypatch)
    _forbid_live_capture(monkeypatch)
    with pytest.raises(release_sanity.ReleaseNotAdmitted) as excinfo:
        g.build()
    assert excinfo.value.code == "INCOMPLETE_RELEASE_ROSTER"


def test_main_check_prints_explicit_line_exits_distinct_code_and_writes_nothing(monkeypatch, tmp_path, capsys):
    _refuse_admission(monkeypatch)
    _forbid_live_capture(monkeypatch)
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    with pytest.raises(SystemExit) as excinfo:
        g.main(["--check"])
    assert excinfo.value.code == release_sanity.RELEASE_NOT_ADMITTED_EXIT_CODE == 3
    assert capsys.readouterr().out == "DETERMINISM_GATE_CHECK:RELEASE_NOT_ADMITTED\n"
    assert not any(path.exists() for path in paths.values())


def test_main_write_mode_writes_none_of_its_outputs_when_not_admitted(monkeypatch, tmp_path, capsys):
    _refuse_admission(monkeypatch)
    _forbid_live_capture(monkeypatch)
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    with pytest.raises(SystemExit) as excinfo:
        g.main([])
    assert excinfo.value.code == release_sanity.RELEASE_NOT_ADMITTED_EXIT_CODE
    assert "RELEASE_NOT_ADMITTED" in capsys.readouterr().out
    assert not any(path.exists() for path in paths.values())
    assert list(tmp_path.iterdir()) == []


def test_other_admission_refusals_are_not_classified_as_non_admitted(monkeypatch):
    _forbid_live_capture(monkeypatch)

    def other_refusal():
        raise SchemaValidationError("SCHEMA_INVALID", "unrelated refusal")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", other_refusal)
    with pytest.raises(SchemaValidationError, match="unrelated refusal"):
        g.build()
