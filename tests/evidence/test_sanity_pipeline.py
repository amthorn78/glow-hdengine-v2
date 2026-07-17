from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from tools.evidence import run_sanity_pipeline


class _FakeCompletedProcess(subprocess.CompletedProcess[str]):
    def __init__(self, returncode: int):
        super().__init__(args=[], returncode=returncode)


def _fake_runner(expected_returncodes: list[int]):
    def _runner(_: list[str]) -> subprocess.CompletedProcess[str]:
        code = expected_returncodes.pop(0)
        return _FakeCompletedProcess(code)

    return _runner


def test_pipeline_success(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
    ]
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0, 0]))
    exit_code = run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps)
    assert exit_code == 0
    log_text = log_path.read_text(encoding="utf-8")
    assert log_text.startswith("pipeline:HDE-EPIC038-PR06-release-sanity\n")
    assert "environment:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC" in log_text
    assert "summary:PASS" in log_text
    assert "stage:step-one;status=OK" in log_text
    assert "stage:step-two;status=OK" in log_text


def test_pipeline_failure_stops_and_records(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
        run_sanity_pipeline.SanityStep("step-three", ["echo", "three"]),
    ]
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0, 1, 0]))
    exit_code = run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps)
    assert exit_code == 1
    log_lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "stage:step-one;status=OK" in log_lines
    assert "stage:step-two;status=FAIL" in log_lines
    assert "stage:step-three;status=NOT_EXECUTED_EARLIER_FAILURE:step-two" in log_lines
    assert log_lines[-1] == "summary:FAIL"


def test_default_pipeline_refreshes_index_before_path_checks():
    names = [step.name for step in run_sanity_pipeline.default_steps()]
    assert names == list(run_sanity_pipeline.STAGE_NAMES)
    assert names.index("13 Human Index and Machine Mirror refresh") < names.index("14 Path validation")
