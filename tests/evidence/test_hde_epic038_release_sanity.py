from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from tools.evidence import run_sanity_pipeline as sanity


def _result(code=0):
    return subprocess.CompletedProcess([], code, "", "")


def test_exact_stage_order_and_canonical_path():
    assert tuple(step.name for step in sanity.default_steps()) == sanity.STAGE_NAMES
    assert len(sanity.STAGE_NAMES) == 17
    assert sanity.SANITY_LOG.relative_to(sanity.ROOT).as_posix() == "audit/gates/sanity_pipeline/sanity_pipeline.log"


def test_first_failure_is_fail_closed_and_later_stages_are_recorded(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("one", ["one"]), sanity.SanityStep("two", ["two"]), sanity.SanityStep("three", ["three"])]
    calls = []
    def run(command):
        calls.append(command)
        return _result(7 if command[0] == "two" else 0)
    monkeypatch.setattr(sanity, "_run_command", run)
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=steps) == 7
    assert calls == [("one",), ("two",)]
    text = log.read_text()
    assert "check three:FAIL" in text
    assert "not_executed three:earlier_mandatory_failure=two" in text
    assert "first_failed_stage:two\nsummary:FAIL\n" in text


def test_pass_requires_every_stage_and_log_has_one_lf(tmp_path, monkeypatch):
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result())
    log = tmp_path / "sanity.log"
    assert sanity.run_pipeline(log_path=log, steps=[sanity.SanityStep("one", ["true"])]) == 0
    data = log.read_bytes()
    assert data.endswith(b"\n") and not data.endswith(b"\n\n")
    assert data.count(b"summary:PASS") == 1


def test_canonical_failure_bytes_are_rebound(tmp_path, monkeypatch):
    steps = [sanity.SanityStep("late", ["false"])]
    log = tmp_path / "sanity.log"
    rebound = []
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "default_steps", lambda: steps)
    monkeypatch.setattr(sanity, "_run_command", lambda command: _result(1))
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: rebound.append(True))
    assert sanity.run_pipeline(log_path=log) == 1
    assert rebound == [True]
    assert log.read_text().endswith("first_failed_stage:late\nsummary:FAIL\n")


def _packet_copy(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    target = root / "audit/ops/hde-epic038"
    target.parent.mkdir(parents=True)
    shutil.copytree(sanity.ROOT / "audit/ops/hde-epic038", target)
    return root


@pytest.mark.parametrize("package,name", [("ops-01", "stdout.log"), ("ops-02", "request_summary.json")])
def test_missing_ops_file_fails(tmp_path, package, name):
    root = _packet_copy(tmp_path)
    (root / f"audit/ops/hde-epic038/{package}/{name}").unlink()
    with pytest.raises(ValueError, match=rf"{package}.*{name}"):
        sanity.validate_ops_packages(root)


def test_zero_byte_ops_file_fails(tmp_path):
    root = _packet_copy(tmp_path)
    (root / "audit/ops/hde-epic038/ops-02/stdout.log").write_bytes(b"")
    with pytest.raises(ValueError, match="stdout.log"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("mutation,match", [
    ("malformed", "malformed row"), ("duplicate", "duplicate row"), ("mismatch", "mismatch for stdout.log")
])
def test_checksum_ledger_fails_closed(tmp_path, mutation, match):
    root = _packet_copy(tmp_path)
    packet = root / "audit/ops/hde-epic038/ops-01"
    ledger = packet / "checksums.sha256"
    if mutation == "malformed":
        ledger.write_text("not a checksum\n")
    elif mutation == "duplicate":
        first = ledger.read_text().splitlines()[0]
        ledger.write_text(ledger.read_text() + first + "\n")
    else:
        (packet / "stdout.log").write_text("changed\n")
    with pytest.raises(ValueError, match=match):
        sanity.validate_ops_packages(root)


def _refresh_ledger(packet: Path, name: str):
    lines = []
    for line in (packet / "checksums.sha256").read_text().splitlines():
        digest, current = line.split("  ")
        if current == name:
            digest = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        lines.append(f"{digest}  {current}")
    (packet / "checksums.sha256").write_text("\n".join(lines) + "\n")


def test_unavailable_provider_row_is_not_pass(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "provider_parity.proof.json"; value = json.loads(path.read_text())
    value["capabilities"][0]["direct"]["status"] = "unavailable"
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unavailable"):
        sanity.validate_ops_packages(root)


def test_malformed_provider_row_is_recorded_as_validation_failure(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-01"
    path = packet / "provider_parity.proof.json"; value = json.loads(path.read_text())
    value["capabilities"] = [None]
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="unavailable"):
        sanity.validate_ops_packages(root)


def test_ops02_predicate_failure_is_not_pass(tmp_path):
    root = _packet_copy(tmp_path); packet = root / "audit/ops/hde-epic038/ops-02"
    path = packet / "result_summary.json"; value = json.loads(path.read_text())
    value["predicates"]["mapped_payload_only"] = False
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match="predicate"):
        sanity.validate_ops_packages(root)


@pytest.mark.parametrize("package,field", [("ops-01", "observations"), ("ops-02", "predicates")])
def test_malformed_summary_nested_object_fails_cleanly(tmp_path, package, field):
    root = _packet_copy(tmp_path); packet = root / f"audit/ops/hde-epic038/{package}"
    path = packet / "result_summary.json"; value = json.loads(path.read_text())
    value[field] = None
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n"); _refresh_ledger(packet, path.name)
    with pytest.raises(ValueError, match=field):
        sanity.validate_ops_packages(root)


def test_ops_validation_never_executes_commands(monkeypatch):
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: pytest.fail("OPS command executed"))
    sanity.validate_ops_packages()


def test_current_commands_and_exact_proof_paths_are_wired():
    commands = [command for step in sanity.default_steps() for command in step.commands]
    assert (sanity.sys.executable, "tools/evidence/generate_open_rails_abba_proof.py", "--check") in commands
    assert (sanity.sys.executable, "tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check") in commands
    updater = (sanity.ROOT / "tools/evidence/update_evidence_index.py").read_text()
    assert "artifacts/vendor/rails_gate_keys_only.logs.sample" in updater
    assert "artifacts/cards/a3/IDENTITY_OK.txt" in updater
    assert (sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt").is_file()
    assert (sanity.ROOT / "artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt").is_file()


def test_wrapper_has_no_legacy_writer_or_epic024_identity():
    text = (sanity.ROOT / "tools/evidence/run_sanity_pipeline_gate.py").read_text()
    assert "D07_sanity_pipeline" not in text
    assert "hde-epic024" not in text
    assert "_write_path_proof" not in text
    from tools.evidence import update_evidence_index
    entries = update_evidence_index._load_human_index()
    sanity_paths = {entry["discovered_physical_path"] for entry in entries if entry["artifact_key"] == "sanity.pipeline.log"}
    assert sanity_paths == {"audit/gates/sanity_pipeline/sanity_pipeline.log"}
