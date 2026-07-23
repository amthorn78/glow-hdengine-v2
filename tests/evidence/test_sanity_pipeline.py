from __future__ import annotations

import subprocess

import pytest

from tools.evidence import run_sanity_pipeline


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in run_sanity_pipeline.DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)


class _FakeCompletedProcess(subprocess.CompletedProcess[str]):
    def __init__(self, returncode: int):
        super().__init__(args=[], returncode=returncode)


def _fake_runner(expected_returncodes: list[int]):
    def _runner(_command) -> subprocess.CompletedProcess[str]:
        return _FakeCompletedProcess(expected_returncodes.pop(0))

    return _runner


def test_pipeline_success(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
    ]
    monkeypatch.setattr(
        run_sanity_pipeline, "_run_command", _fake_runner([0, 0])
    )
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 0
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "run:sanity-pipeline"
    assert "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC" in lines
    assert "check step-one:OK" in lines
    assert "check step-two:OK" in lines
    assert lines[-2:] == ["first_failed_stage:NONE", "summary:PASS"]


def test_custom_pipeline_failure_stops_and_records(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
        run_sanity_pipeline.SanityStep("step-three", ["echo", "three"]),
    ]
    runner = _fake_runner([0, 1])
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", runner)
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 1
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "check step-one:OK" in lines
    assert "check step-two:FAIL" in lines
    assert "check step-three:FAIL" in lines
    assert "not_executed step-three:earlier_mandatory_failure=step-two" in lines
    assert lines[-2:] == ["first_failed_stage:step-two", "summary:FAIL"]


def test_default_pipeline_has_exact_19_stage_dependency_order():
    names = [step.name for step in run_sanity_pipeline.default_steps()]
    assert names == list(run_sanity_pipeline.STAGE_NAMES)
    assert len(names) == 19
    assert names.index("07 Direct DB selection contract") < names.index(
        "08 Direct DB posture artifacts"
    )
    assert names.index("12 Historical bridge evidence integrity") < names.index(
        "13 OPS-02 mapped-cache packet validation"
    )
    assert names.index("13 OPS-02 mapped-cache packet validation") < names.index(
        "14 OPS-03 direct DB posture packet validation"
    )
    assert names.index("14 OPS-03 direct DB posture packet validation") < names.index(
        "15 Human Index and Machine Mirror refresh"
    )
    assert names.index("15 Human Index and Machine Mirror refresh") < names.index(
        "18 Topology orientation validation"
    )


def test_stage14_failure_marks_all_finalization_stages_not_executed(
    tmp_path, monkeypatch
):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep(name, ["ok"])
        for name in run_sanity_pipeline.STAGE_NAMES[:13]
    ] + [
        run_sanity_pipeline.SanityStep(
            run_sanity_pipeline.STAGE_NAMES[13], ["missing-ops03"]
        )
    ] + [
        run_sanity_pipeline.SanityStep(name, ["must-not-run"])
        for name in run_sanity_pipeline.STAGE_NAMES[14:]
    ]
    monkeypatch.setattr(
        run_sanity_pipeline,
        "_run_command",
        _fake_runner([0] * 13 + [run_sanity_pipeline.PR_A_NONFINAL_EXIT]),
    )
    assert (
        run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps)
        == run_sanity_pipeline.PR_A_NONFINAL_EXIT
    )
    lines = log_path.read_text(encoding="utf-8").splitlines()
    for name in run_sanity_pipeline.STAGE_NAMES[14:]:
        assert (
            f"not_executed {name}:earlier_mandatory_failure="
            f"{run_sanity_pipeline.STAGE_NAMES[13]}"
        ) in lines
    assert lines[-2:] == [
        f"first_failed_stage:{run_sanity_pipeline.STAGE_NAMES[13]}",
        "summary:FAIL",
    ]
