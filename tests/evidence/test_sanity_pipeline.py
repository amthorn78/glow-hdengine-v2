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


# --- PF10 §2.15: the explicit NOT_ADMITTED outcome (HDE-EPIC040-PR04 F01 overlay) -------------

from tools.evidence import build_release_attestation as attestation  # noqa: E402

NOT_ADMITTED = run_sanity_pipeline.NOT_ADMITTED_STATUS
DISTINCT = run_sanity_pipeline.RELEASE_NOT_ADMITTED_EXIT_CODE


def _not_admitted_model() -> bytes:
    return run_sanity_pipeline._render_log(
        [
            (name, NOT_ADMITTED if name in run_sanity_pipeline.RELEASE_ADMISSION_GATED_STAGES else "OK")
            for name in run_sanity_pipeline.STAGE_NAMES
        ],
        "NONE",
        NOT_ADMITTED,
    )


def test_distinct_code_and_gated_stages_are_pinned_across_pipeline_gate_and_runner():
    from ci.checks import run_rails_job_definitions as runner

    assert DISTINCT == 3
    assert DISTINCT not in (0, 1, 2)
    assert run_sanity_pipeline_gate.RELEASE_NOT_ADMITTED_EXIT_CODE == DISTINCT
    assert runner.RELEASE_NOT_ADMITTED_EXIT_CODE == DISTINCT
    assert attestation.RELEASE_NOT_ADMITTED_EXIT_CODE == DISTINCT
    assert run_sanity_pipeline.RELEASE_ADMISSION_GATED_STAGES == (
        "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks",
        "05 A7 Catalog transport",
        "06 CI rails",
    )
    assert run_sanity_pipeline_gate.RELEASE_ADMISSION_GATED_STAGES == run_sanity_pipeline.RELEASE_ADMISSION_GATED_STAGES
    assert run_sanity_pipeline_gate._expected_not_admitted_log() == _not_admitted_model()
    assert run_sanity_pipeline_gate._expected_log() == _final_pass_log()


def test_probe_classifies_exactly_the_incomplete_roster_refusal(monkeypatch):
    from engine.compat import compute
    from engine.config.registry_loader import SchemaValidationError

    # Real admission owner: the active release is not admitted.
    with pytest.raises(run_sanity_pipeline.ReleaseNotAdmitted) as excinfo:
        run_sanity_pipeline.probe_release_admission()
    assert excinfo.value.code == "INCOMPLETE_RELEASE_ROSTER"
    assert run_sanity_pipeline.release_not_admitted_observed() is True

    def other_refusal():
        raise SchemaValidationError("SCHEMA_INVALID", "unrelated")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", other_refusal)
    with pytest.raises(SchemaValidationError):
        run_sanity_pipeline.probe_release_admission()
    assert run_sanity_pipeline.release_not_admitted_observed() is False

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", lambda: object())
    assert run_sanity_pipeline.probe_release_admission() is not None
    assert run_sanity_pipeline.release_not_admitted_observed() is False


def test_subprocess_distinct_code_renders_not_admitted_only_with_the_observed_state(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
        run_sanity_pipeline.SanityStep("step-three", ["echo", "three"]),
    ]
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0, DISTINCT, 0]))
    monkeypatch.setattr(run_sanity_pipeline, "release_not_admitted_observed", lambda: True)
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == DISTINCT
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "check step-one:OK" in lines
    assert "check step-two:NOT_ADMITTED" in lines
    assert "check step-three:OK" in lines  # later stages still execute
    assert not any(line.startswith("not_executed") for line in lines)
    assert lines[-2:] == ["first_failed_stage:NONE", "summary:NOT_ADMITTED"]

    # The same distinct code without the non-admitted state is an ordinary failure.
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0, DISTINCT, 0]))
    monkeypatch.setattr(run_sanity_pipeline, "release_not_admitted_observed", lambda: False)
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 1
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "check step-two:FAIL" in lines
    assert lines[-2:] == ["first_failed_stage:step-two", "summary:FAIL"]


def test_validator_release_not_admitted_is_the_third_status(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("reader", ["__validate_reader_cli_determinism__"]),
        run_sanity_pipeline.SanityStep("a7", ["__validate_a7_transport__"]),
        run_sanity_pipeline.SanityStep("tail", ["echo", "tail"]),
    ]

    def not_admitted():
        raise run_sanity_pipeline.ReleaseNotAdmitted()

    monkeypatch.setitem(
        run_sanity_pipeline._VALIDATORS, ("__validate_reader_cli_determinism__",), (not_admitted, "reader_failed")
    )
    monkeypatch.setitem(run_sanity_pipeline._VALIDATORS, ("__validate_a7_transport__",), (not_admitted, "a7_failed"))
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0]))
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == DISTINCT
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert lines[4:7] == ["check reader:NOT_ADMITTED", "check a7:NOT_ADMITTED", "check tail:OK"]
    assert lines[-1] == "summary:NOT_ADMITTED"


def test_not_admitted_mixed_with_a_failure_renders_fail(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [
        run_sanity_pipeline.SanityStep("step-one", ["echo", "one"]),
        run_sanity_pipeline.SanityStep("step-two", ["echo", "two"]),
        run_sanity_pipeline.SanityStep("step-three", ["echo", "three"]),
    ]
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([DISTINCT, 1]))
    monkeypatch.setattr(run_sanity_pipeline, "release_not_admitted_observed", lambda: True)
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 1
    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "check step-one:NOT_ADMITTED" in lines
    assert "check step-two:FAIL" in lines
    assert "not_executed step-three:earlier_mandatory_failure=step-two" in lines
    assert lines[-2:] == ["first_failed_stage:step-two", "summary:FAIL"]


def test_all_ok_renders_pass_byte_identically_to_the_current_model(tmp_path, monkeypatch):
    log_path = tmp_path / "sanity.log"
    steps = [run_sanity_pipeline.SanityStep(name, ["ok"]) for name in run_sanity_pipeline.STAGE_NAMES]
    monkeypatch.setattr(run_sanity_pipeline, "_run_command", _fake_runner([0] * 15))
    assert run_sanity_pipeline.run_pipeline(log_path=log_path, steps=steps) == 0
    assert log_path.read_bytes() == _final_pass_log() == run_sanity_pipeline_gate._expected_log()


def test_sanity_gate_accepts_exactly_the_two_models(tmp_path, monkeypatch, capsys):
    log = tmp_path / "sanity_pipeline.log"
    monkeypatch.setattr(run_sanity_pipeline_gate, "LOG", log)

    def run_with(code: int, stdout: str = "", stderr: str = ""):
        proc = _FakeCompletedProcess(code)
        proc.stdout, proc.stderr = stdout, stderr
        monkeypatch.setattr(run_sanity_pipeline_gate.subprocess, "run", lambda *_a, **_k: proc)
        return run_sanity_pipeline_gate.main()

    log.write_bytes(_not_admitted_model())
    assert run_sanity_pipeline_gate._valid_not_admitted_log() is True
    assert run_sanity_pipeline_gate._valid_log() is False
    assert run_with(DISTINCT) == DISTINCT
    assert capsys.readouterr().out == "SANITY_PIPELINE_GATE:RELEASE_NOT_ADMITTED\n"
    # PASS exit with a NOT_ADMITTED log, or the distinct code with a PASS log, or noise: failure.
    assert run_with(0) == 1
    log.write_bytes(_final_pass_log())
    assert run_with(DISTINCT) == 1
    assert run_with(0) == 0
    log.write_bytes(_not_admitted_model())
    assert run_with(DISTINCT, stdout="noise\n") == 1
    for old, new in (
        ("summary:NOT_ADMITTED", "summary:PASS"),
        ("summary:NOT_ADMITTED", "summary:FAIL"),
        ("check 07 Direct DB selection contract:OK", "check 07 Direct DB selection contract:NOT_ADMITTED"),
        ("check 06 CI rails:NOT_ADMITTED", "check 06 CI rails:OK"),
    ):
        log.write_bytes(_not_admitted_model().replace(old.encode(), new.encode(), 1))
        assert run_sanity_pipeline_gate._valid_not_admitted_log() is False
        assert run_with(DISTINCT) == 1
    log.write_bytes(_not_admitted_model() + b"unexpected:claim\n")
    assert run_with(DISTINCT) == 1


def test_attestation_maps_the_release_sanity_distinct_code_to_release_not_admitted(tmp_path, monkeypatch):
    def fake_run(argv, **kwargs):
        return subprocess.CompletedProcess(args=list(argv), returncode=DISTINCT, stdout="", stderr="")

    monkeypatch.setattr(attestation.subprocess, "run", fake_run)
    log: list[str] = []
    with pytest.raises(attestation.AttestationBuildError) as excinfo:
        attestation._run_stage(tmp_path, "release_sanity", ("python", "tools/evidence/run_sanity_pipeline_gate.py"), log, attestation_bin=tmp_path)
    assert excinfo.value.code == "release_not_admitted"
    assert excinfo.value.stage == "release_sanity" and excinfo.value.returncode == DISTINCT
    with pytest.raises(attestation.AttestationBuildError) as other:
        attestation._run_stage(tmp_path, "build_package_wheel", ("python", "x.py"), log, attestation_bin=tmp_path)
    assert other.value.code == "isolated_stage_failed"

    receipt_dir = tmp_path / "receipt"
    receipt_dir.mkdir()
    attestation._write_failure(receipt_dir, excinfo.value)
    receipt = json.loads((receipt_dir / "failure.json").read_bytes())
    assert receipt == {
        "schema": "hde.release_attestation.failure.v1",
        "code": "release_not_admitted",
        "stage": "release_sanity",
        "returncode": DISTINCT,
        "secret_values_recorded": False,
    }
    assert {path.name for path in receipt_dir.iterdir()} == {"failure.json"}
    assert attestation.SCHEMA == "hde.release_attestation.v1"


def test_isolated_closure_refuses_with_the_distinct_code_before_any_producer(monkeypatch, capsys):
    from tools.evidence import regenerate_identity_closure as closure

    assert closure.RELEASE_NOT_ADMITTED_EXIT_CODE == DISTINCT
    monkeypatch.setattr(closure, "_write_closure", lambda: pytest.fail("producer ran"))
    monkeypatch.setattr(closure, "_check_closure", lambda: pytest.fail("closure check ran"))
    monkeypatch.setattr(closure.subprocess, "run", lambda *a, **k: pytest.fail("subprocess spawned"))
    # The isolation guards still come first.
    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    with pytest.raises(SystemExit, match="SOURCE_TREE_RELEASE_CLOSURE_REFUSED"):
        closure.main(["--in-place-isolated"])
    monkeypatch.setenv("HDE_ISOLATED_RELEASE_BUILD", "1")
    with pytest.raises(SystemExit, match="ISOLATED_RELEASE_BUILD_MODE_REQUIRED"):
        closure.main([])
    # Real admission owner: INCOMPLETE_RELEASE_ROSTER → explicit line, distinct code, no producer.
    assert closure.release_not_admitted_observed() is True
    assert closure.main(["--in-place-isolated"]) == DISTINCT
    assert closure.main(["--in-place-isolated", "--check"]) == DISTINCT
    assert capsys.readouterr().out == "IDENTITY_CLOSURE:RELEASE_NOT_ADMITTED\n" * 2
    # Any other refusal is not classified as non-admitted.
    from engine.config.registry_loader import SchemaValidationError

    def other_refusal():
        raise SchemaValidationError("SCHEMA_INVALID", "unrelated")

    monkeypatch.setattr("engine.config.registry_loader.load_active_mechanics_bundle", other_refusal)
    assert closure.release_not_admitted_observed() is False  # fail-closed: never accepted as non-admitted
    monkeypatch.setattr("engine.config.registry_loader.load_active_mechanics_bundle", lambda: object())
    assert closure.release_not_admitted_observed() is False


def test_attestation_maps_every_admission_gated_isolated_stage(tmp_path, monkeypatch):
    def fake_run(argv, **kwargs):
        return subprocess.CompletedProcess(args=list(argv), returncode=DISTINCT, stdout="", stderr="")

    monkeypatch.setattr(attestation.subprocess, "run", fake_run)
    assert attestation._RELEASE_ADMISSION_GATED_STAGES == {"closure_write_and_check", "closure_fixed_point_check", "release_sanity"}
    for stage in sorted(attestation._RELEASE_ADMISSION_GATED_STAGES):
        with pytest.raises(attestation.AttestationBuildError) as excinfo:
            attestation._run_stage(tmp_path, stage, ("python", "x.py"), [], attestation_bin=tmp_path)
        assert (excinfo.value.code, excinfo.value.stage, excinfo.value.returncode) == ("release_not_admitted", stage, DISTINCT)
    with pytest.raises(attestation.AttestationBuildError) as other:
        attestation._run_stage(tmp_path, "build_package_wheel", ("python", "x.py"), [], attestation_bin=tmp_path)
    assert other.value.code == "isolated_stage_failed"
