import hashlib
import inspect
import json
import os
import stat
import subprocess
import sys
from pathlib import Path

import jsonschema
import pytest

from engine.bodygraph import ingest
from presenter import json_canon_compare
from scripts.db import capture_epic011_posture
from scripts.ops import admin_vendor_qa
from tools.evidence import generate_hde_epic038_direct_db_selection as direct_generator
from tools.evidence import generate_presenter_history as history_generator

ROOT = Path(__file__).resolve().parents[2]
ENV = {
    **os.environ,
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}
SHARED = ROOT / "artifacts/presenter/json_canon_compare.log"
DEDICATED = ROOT / "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json"
SCHEMA = ROOT / "schemas/presenter_db_bridge_compare.v1.json"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args], cwd=ROOT, env=ENV, check=True, capture_output=True, text=True
    )


def test_presenter_history_is_exact_fixed_point_and_check_is_read_only():
    _run("tools/evidence/generate_presenter_history.py")
    first = SHARED.read_bytes()
    assert len(first) == 1559
    assert hashlib.sha256(first).hexdigest() == "64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c"
    assert len(first.splitlines()) == 4
    _run("tools/evidence/generate_presenter_history.py")
    assert SHARED.read_bytes() == first
    _run("tools/evidence/generate_presenter_history.py", "--check")
    assert SHARED.read_bytes() == first
    assert stat.S_IMODE(SHARED.stat().st_mode) == 0o644


def test_presenter_history_atomic_failure_preserves_destination(tmp_path, monkeypatch):
    destination = tmp_path / "json_canon_compare.log"
    destination.write_bytes(b"original\n")
    destination.chmod(0o644)
    monkeypatch.setattr(history_generator, "DESTINATION", destination)
    monkeypatch.setattr(history_generator.os, "replace", lambda *_: (_ for _ in ()).throw(OSError("injected")))
    with pytest.raises(OSError, match="injected"):
        history_generator._atomic_write(b"replacement\n")
    assert destination.read_bytes() == b"original\n"
    assert stat.S_IMODE(destination.stat().st_mode) == 0o644
    assert list(tmp_path.iterdir()) == [destination]


def test_direct_selection_generator_does_not_touch_shared_presenter_history(tmp_path):
    shared_before = SHARED.read_bytes()
    out = tmp_path / "direct_selection.json"
    assert direct_generator.main(["--out", str(out)]) == 0
    assert SHARED.read_bytes() == shared_before
    payload = json.loads(out.read_bytes())
    assert payload["result"] == "PASS"
    assert payload["predicates"]["direct_only_provider"] is True

def test_no_replay_constants_or_implicit_governed_log_defaults():
    source = (ROOT / "tools/evidence/generate_hde_epic038_direct_db_selection.py").read_text()
    assert "artifacts/presenter/json_canon_compare.log" not in source
    assert inspect.signature(ingest.ingest_vendor_bodygraph).parameters["canon_log"].default is None
    parsed = json_canon_compare._build_parser().parse_args(["left.json", "right.json"])
    assert parsed.log is None

def test_compare_without_log_is_stdout_only(tmp_path, capsys):
    left = tmp_path / "left.json"
    right = tmp_path / "right.json"
    left.write_text('{"value":"same"}\n', encoding="utf-8")
    right.write_text('{"value":"same"}\n', encoding="utf-8")
    shared_before = SHARED.read_bytes()
    assert json_canon_compare.main([str(left), str(right)]) == 0
    assert SHARED.read_bytes() == shared_before
    assert "compare: FILE_EQ_CANON_BYTES_OK" in capsys.readouterr().out


def test_compare_can_fail_closed_on_diff(tmp_path):
    left = tmp_path / "left.json"
    right = tmp_path / "right.json"
    diagnostic = tmp_path / "parity.jsonl"
    left.write_text('{"value":"left"}\n', encoding="utf-8")
    right.write_text('{"value":"right"}\n', encoding="utf-8")
    assert json_canon_compare.main([str(left), str(right), "--log", str(diagnostic), "--fail-on-diff"]) == 1
    row = json.loads(diagnostic.read_text(encoding="utf-8"))
    assert row["compare"] == "DIFF"
    assert row["match"] is False


def test_ops_callers_use_dedicated_mutable_parity_log():
    admin_source = (ROOT / "scripts/ops/admin_vendor_qa.py").read_text(encoding="utf-8")
    runbook = (ROOT / "docs/run/RUN_PROD_QA.md").read_text(encoding="utf-8")
    dedicated = "artifacts/ops/admin_vendor_parity.jsonl"
    assert f'PARITY_LOG_PATH = Path("{dedicated}")' in admin_source
    assert "artifacts/presenter/json_canon_compare.log" not in admin_source
    assert f"--log {dedicated}" in runbook
    assert "--fail-on-diff" in runbook
    assert "Omitting `--log` is stdout-only" in runbook
    assert "must not write to `artifacts/presenter/json_canon_compare.log`" in runbook
    assert runbook.count("artifacts/presenter/json_canon_compare.log") == 1
    assert runbook.count(dedicated) >= 3


def test_admin_parity_command_is_explicit_dedicated_and_fail_closed(monkeypatch):
    captured: list[tuple[str, ...]] = []
    monkeypatch.setattr(admin_vendor_qa, "_run_command", lambda cmd, stdout_path=None: captured.append(tuple(cmd)))
    admin_vendor_qa._run_parity_check()
    assert len(captured) == 1
    command = captured[0]
    assert command[command.index("--log") + 1] == "artifacts/ops/admin_vendor_parity.jsonl"
    assert "--fail-on-diff" in command


def test_epic011_live_capture_is_task_scoped_and_writes_no_companions(tmp_path, monkeypatch):
    capture_root = tmp_path / "artifacts/ops/epic011_posture"
    monkeypatch.setattr(capture_epic011_posture, "CAPTURE_ROOT", capture_root)
    capture_epic011_posture._write_text("artifacts/db/ddl_fingerprint.json", "diagnostic")
    expected = capture_root / "db/ddl_fingerprint.json"
    assert expected.read_text(encoding="utf-8") == "diagnostic\n"
    assert not (tmp_path / "artifacts/db/ddl_fingerprint.json").exists()
    assert not Path(f"{expected}.path_proof.txt").exists()
