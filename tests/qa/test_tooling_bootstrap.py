import json
import os
from pathlib import Path

import pytest

from tools.qa.epic021_qa import (
    QA_ROOT,
    CheckResult,
    generate_acceptance_map_viability,
    run_bootstrap_checks,
    run_epic021_qa_run,
    summarize_checks,
)


@pytest.fixture(autouse=True)
def enforce_env_pins(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")


def test_bootstrap_checks_pass_under_closed_rails(tmp_path, monkeypatch):
    monkeypatch.setenv("EPIC021_QA_RUN_ID", "test-run")
    checks = run_bootstrap_checks()
    assert summarize_checks(checks) == "summary:PASS"
    log_path = QA_ROOT / "test-run" / "D0_bootstrap.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("seed", encoding="utf-8")
    run_epic021_qa_run("test-run")
    contents = log_path.read_text(encoding="utf-8")
    assert "env:" in contents
    assert "summary:PASS" in contents


def test_epic021_qa_run_emits_manifest_and_viability(monkeypatch):
    monkeypatch.setenv("EPIC021_QA_RUN_ID", "test-run-d3")
    artifacts = run_epic021_qa_run()

    bootstrap_log = artifacts["bootstrap_log"]
    canonical_log = artifacts["canonical_bootstrap"]
    manifest = artifacts["manifest"]
    viability = artifacts["viability_log"]

    for path in [bootstrap_log, canonical_log, manifest, viability]:
        assert path.exists(), f"expected artifact {path} to exist"
        assert path.read_text(encoding="utf-8").strip(), f"{path} should be non-empty"

    manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
    assert manifest_data.get("epic_id") == "HDE-EPIC021"
    assert manifest_data.get("runs"), "manifest should include at least one run"
    latest_run = manifest_data["runs"][-1]
    assert latest_run["run_id"] == "test-run-d3"
    for step in latest_run["steps"]:
        log_path = Path(step["log_path"])
        assert log_path.exists(), f"manifested log path {log_path} should exist"
        content = log_path.read_text(encoding="utf-8")
        assert "env:" in content
        assert "summary:" in content

    viability_content = viability.read_text(encoding="utf-8")
    assert "summary:" in viability_content
    assert "token" in viability_content


def test_epic021_manifest_dedupes_run_id(monkeypatch):
    monkeypatch.setenv("EPIC021_QA_RUN_ID", "dedupe-run")
    artifacts = run_epic021_qa_run()

    manifest_path = artifacts["manifest"]
    first_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    first_runs = [run for run in first_manifest["runs"] if run["run_id"] == "dedupe-run"]
    assert len(first_runs) == 1

    run_epic021_qa_run()

    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    runs = [run for run in manifest_data["runs"] if run["run_id"] == "dedupe-run"]

    assert len(runs) == 1, "manifest should keep only the latest entry per run id"


@pytest.mark.parametrize(
    "checks,expected",
    [
        ([CheckResult("ok", "OK")], "summary:PASS"),
        ([CheckResult("oops", "FAIL")], "summary:FAIL"),
        ([CheckResult("oops", "FAIL_TOOLING")], "summary:FAIL"),
    ],
)
def test_summarize_checks(checks, expected):
    assert summarize_checks(checks) == expected


def test_acceptance_map_viability_parses_matrix(monkeypatch):
    monkeypatch.setenv("EPIC021_QA_RUN_ID", "viability-check")
    log_path, token_status = generate_acceptance_map_viability("viability-check")
    assert log_path.exists()
    assert token_status, "viability should classify at least one token"
    content = log_path.read_text(encoding="utf-8")
    assert "summary:" in content
    assert "token" in content
