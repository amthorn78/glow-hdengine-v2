import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

QA_ROOT = Path("audit/qa/hde-epic021")


@pytest.fixture(autouse=True)
def enforce_env_pins(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")


def _remove_run_artifacts(run_id: str) -> None:
    run_dir = QA_ROOT / run_id
    if run_dir.exists():
        shutil.rmtree(run_dir)

    manifest_path = QA_ROOT / "qa_step_logs_manifest.json"
    if manifest_path.exists():
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_data["runs"] = [run for run in manifest_data.get("runs", []) if run.get("run_id") != run_id]
        manifest_path.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")


def test_entrypoint_produces_expected_artifacts(tmp_path):
    run_id = "selftest-run"
    _remove_run_artifacts(run_id)

    env = os.environ.copy()
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "EPIC021_QA_RUN_ID": run_id,
            "PYTHONPATH": str(Path.cwd()),
        }
    )

    result = subprocess.run(
        [sys.executable, "tools/qa/epic021_qa.py"],
        cwd=Path.cwd(),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    run_dir = QA_ROOT / run_id
    assert run_dir.is_dir(), "entrypoint should create the run directory"

    expected_logs = {
        "D0_bootstrap.log",
        "step_bootstrap.log",
        "step_serializer_cli_d1.log",
        "step_evidence_d2.log",
        "step_sanity_d2.log",
        "step_acceptance_map_d3.log",
    }
    assert expected_logs.issubset({path.name for path in run_dir.iterdir()})

    manifest_path = QA_ROOT / "qa_step_logs_manifest.json"
    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    runs = [run for run in manifest_data.get("runs", []) if run.get("run_id") == run_id]
    assert len(runs) == 1, "manifest should contain exactly one entry for the run id"
    for step in runs[0].get("steps", []):
        assert step["status"] == "PASS"
        assert Path(step["log_path"]).exists()

    viability_log = QA_ROOT / "acceptance_map_viability.log"
    viability_content = viability_log.read_text(encoding="utf-8")
    assert run_id in viability_content


def test_entrypoint_rejects_missing_env_pins(tmp_path):
    run_id = "env-fail-run"
    _remove_run_artifacts(run_id)

    env = os.environ.copy()
    env.pop("SAFE_MODE", None)
    env.update(
        {
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "EPIC021_QA_RUN_ID": run_id,
            "PYTHONPATH": str(Path.cwd()),
        }
    )

    result = subprocess.run(
        [sys.executable, "tools/qa/epic021_qa.py"],
        cwd=Path.cwd(),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "SAFE_MODE" in result.stderr

    run_dir = QA_ROOT / run_id
    assert not run_dir.exists(), "run artifacts should not be created when env pins are missing"

    manifest_path = QA_ROOT / "qa_step_logs_manifest.json"
    if manifest_path.exists():
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert all(run.get("run_id") != run_id for run in manifest_data.get("runs", []))
