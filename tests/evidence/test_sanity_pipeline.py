from __future__ import annotations

import json
import subprocess

import pytest

from tools.evidence import run_sanity_pipeline
from tools.evidence import run_sanity_pipeline_gate
from tools.evidence import generate_v2_mapped_cache_evidence


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
    assert lines[1] == "pipeline_identity:hde-release-sanity-v1"
    assert "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC" in lines
    assert not any(line.startswith("ops_evidence:") for line in lines)
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


def test_default_pipeline_has_exact_15_stage_dependency_order():
    names = [step.name for step in run_sanity_pipeline.default_steps()]
    assert names == list(run_sanity_pipeline.STAGE_NAMES)
    assert len(names) == 15
    assert names.index("07 Direct DB selection contract") < names.index(
        "08 Direct DB posture artifacts"
    )
    assert names.index("09 BodyGraph policy") < names.index(
        "10 Configured-v2 mapped-cache behavior"
    )
    assert names.index("10 Configured-v2 mapped-cache behavior") < names.index(
        "11 Human Index and Machine Mirror refresh"
    )
    assert names.index("11 Human Index and Machine Mirror refresh") < names.index(
        "14 Topology orientation validation"
    )
    commands = [command for step in run_sanity_pipeline.default_steps() for command in step.commands]
    assert ("__validate_mapped_cache__",) in commands
    assert not any(
        command and command[0] in {
            "__validate_architecture__",
            "__validate_historical_ops01__",
            "__validate_ops02__",
            "__validate_ops03__",
            "__validate_pr05_proofs__",
        }
        for command in commands
    )


def test_mapped_cache_failure_marks_all_finalization_stages_not_executed(
    tmp_path, monkeypatch
):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep(name, ["ok"])
        for name in run_sanity_pipeline.STAGE_NAMES[:9]
    ] + [
        run_sanity_pipeline.SanityStep(
            run_sanity_pipeline.STAGE_NAMES[9], ["mapped-cache-failure"]
        )
    ] + [
        run_sanity_pipeline.SanityStep(name, ["must-not-run"])
        for name in run_sanity_pipeline.STAGE_NAMES[10:]
    ]
    monkeypatch.setattr(
        run_sanity_pipeline,
        "_run_command",
        _fake_runner([0] * 9 + [1]),
    )
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 1
    lines = log_path.read_text(encoding="utf-8").splitlines()
    for name in run_sanity_pipeline.STAGE_NAMES[10:]:
        assert (
            f"not_executed {name}:earlier_mandatory_failure="
            f"{run_sanity_pipeline.STAGE_NAMES[9]}"
        ) in lines
    assert lines[-2:] == [
        f"first_failed_stage:{run_sanity_pipeline.STAGE_NAMES[9]}",
        "summary:FAIL",
    ]


def test_mapped_cache_validation_is_in_memory_and_requires_all_predicates(monkeypatch):
    manifest_path = generate_v2_mapped_cache_evidence.OUT / "manifest.json"
    predicates = {
        name: True for name in generate_v2_mapped_cache_evidence.PREDICATE_KEYS
    }
    calls = []

    def build():
        calls.append("build")
        return {
            manifest_path: (
                '{"predicates":' + json.dumps(predicates, sort_keys=True)
                + ',"status":"PASS"}'
            ).encode("utf-8")
        }

    monkeypatch.setattr(generate_v2_mapped_cache_evidence, "build", build)
    monkeypatch.setattr(
        generate_v2_mapped_cache_evidence,
        "write_or_check",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("tracked evidence writer called")
        ),
    )
    run_sanity_pipeline.validate_current_mapped_cache()
    assert calls == ["build"]

    predicates[next(iter(predicates))] = False
    with pytest.raises(ValueError, match="current mapped-cache behavior failed"):
        run_sanity_pipeline.validate_current_mapped_cache()


def _final_pass_log() -> bytes:
    return run_sanity_pipeline._render_log(
        [(name, "OK") for name in run_sanity_pipeline.STAGE_NAMES],
        "NONE",
        "PASS",
    )


def test_sanity_gate_accepts_only_exact_generic_final_pass_log(tmp_path, monkeypatch):
    log = tmp_path / "sanity_pipeline.log"
    log.write_bytes(_final_pass_log())
    monkeypatch.setattr(run_sanity_pipeline_gate, "LOG", log)
    assert run_sanity_pipeline_gate.STAGE_NAMES == run_sanity_pipeline.STAGE_NAMES
    assert run_sanity_pipeline_gate._valid_log() is True

    for old, new in (
        ("summary:PASS", "summary:FAIL"),
        ("pipeline_identity:hde-release-sanity-v1", "pipeline_identity:stale"),
        (run_sanity_pipeline.STAGE_NAMES[9], run_sanity_pipeline.STAGE_NAMES[8]),
    ):
        log.write_bytes(_final_pass_log().replace(old.encode(), new.encode(), 1))
        assert run_sanity_pipeline_gate._valid_log() is False

    log.write_bytes(_final_pass_log() + b"unexpected:claim\n")
    assert run_sanity_pipeline_gate._valid_log() is False


def test_sanity_gate_rejects_stale_log_when_fresh_run_fails(tmp_path, monkeypatch):
    log = tmp_path / "sanity_pipeline.log"
    log.write_bytes(_final_pass_log())
    monkeypatch.setattr(run_sanity_pipeline_gate, "LOG", log)
    monkeypatch.setattr(
        run_sanity_pipeline_gate.subprocess,
        "run",
        lambda *_args, **_kwargs: _FakeCompletedProcess(1),
    )
    assert run_sanity_pipeline_gate._valid_log() is True
    assert run_sanity_pipeline_gate.main() == 1
