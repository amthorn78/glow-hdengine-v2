import json
from pathlib import Path
from types import SimpleNamespace

import pytest

import tools.qa.run_hde_epic024_harness as harness
from tools.qa.run_hde_epic024_harness import (
    _derive_retained_bootstrap_status,
    _one_path_diff_ok,
    _render_acceptance_map,
    _render_token_matrix,
    _selective_acceptance_bindings,
    _status_from_bootstrap,
)


def test_bootstrap_missing_pytest_maps_to_tooling_failure():
    stderr = "ModuleNotFoundError: No module named 'pytest'\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_TOOLING"


def test_bootstrap_exit_code_one_still_counts_as_behavior_failure():
    stderr = "E   AssertionError: failed test\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_BEHAVIOR"


def test_subprocess_environment_forces_closed_rails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for key in harness.DETERMINISM_ENV_PINS:
        monkeypatch.setenv(key, "poisoned")
    monkeypatch.setenv("APP_ENV", "prod")

    env = harness._env_for_subprocess()

    assert {
        key: env[key] for key in harness.DETERMINISM_ENV_PINS
    } == harness.DETERMINISM_ENV_PINS
    assert env["APP_ENV"] == "dev"


def test_check_specs_have_unique_closed_rails_execution_contract() -> None:
    checks = harness._check_specs()
    check_ids = [check.check_id for check in checks]
    assert check_ids == [
        "D00_bootstrap_pytest",
        "D01_env_pins_gate",
        "D02_canonical_json_gate",
        "D03_showcompat_artifacts",
        "D04_sampler_evidence",
        "D05_arrays_as_sets",
        "D06_tests_pass",
        "D07_sanity_pipeline",
        "D08_update_evidence_index",
        "D09_generate_evidence_index_snapshot",
        "D10_check_evidence_index_hash",
        "D11_check_mirror_schema",
        "D12_check_final_lf",
        "D17_token_matrix",
        "D18_acceptance_map",
        "D15_doc_deltas",
        "D16_close_pack",
        "D19_step_logs_manifest",
        "D13_acceptance_map_viability",
        "D14_harness_selftest",
    ]
    assert len(check_ids) == len(set(check_ids))
    assert {
        check.check_id for check in checks if check.command is None
    } == {
        "D13_acceptance_map_viability",
        "D14_harness_selftest",
        "D15_doc_deltas",
        "D16_close_pack",
        "D17_token_matrix",
        "D18_acceptance_map",
        "D19_step_logs_manifest",
    }
    command_text = " ".join(
        part
        for check in checks
        for part in (check.command or ())
    ).lower()
    for forbidden in (
        "allow_network=1",
        "safe_mode=0",
        "http://",
        "https://",
        "curl",
    ):
        assert forbidden not in command_text


def test_run_command_passes_closed_env_and_classifies_bootstrap_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[tuple[object, ...]] = []
    env = {
        **harness.DETERMINISM_ENV_PINS,
        "APP_ENV": "dev",
        "PATH": "/runtime/bin",
    }

    def fake_run(argv: list[str], **kwargs: object) -> SimpleNamespace:
        calls.append((argv, kwargs))
        return SimpleNamespace(
            returncode=1,
            stdout="pytest bootstrap stdout\n",
            stderr="ModuleNotFoundError: No module named 'pytest'\n",
        )

    captured_log: dict[str, object] = {}

    def fake_write_primary_log(**kwargs: object) -> Path:
        captured_log.update(kwargs)
        return tmp_path / "primary.log"

    monkeypatch.setattr(harness.subprocess, "run", fake_run)
    monkeypatch.setattr(harness, "_write_primary_log", fake_write_primary_log)
    check = harness.CheckSpec(
        check_id="D00_bootstrap_pytest",
        command=["python", "-m", "pytest", "--version"],
        description="bootstrap",
        evidence_outputs=(),
    )

    status, exit_code, log_path = harness._run_command(check, env)

    assert (status, exit_code, log_path) == (
        "FAIL_TOOLING",
        1,
        tmp_path / "primary.log",
    )
    assert calls == [
        (
            ["python", "-m", "pytest", "--version"],
            {
                "capture_output": True,
                "text": True,
                "env": env,
            },
        )
    ]
    assert captured_log == {
        "check_id": "D00_bootstrap_pytest",
        "command": "python -m pytest --version",
        "status": "FAIL_TOOLING",
        "exit_code": 1,
        "evidence_outputs": (),
        "stdout": "pytest bootstrap stdout\n",
        "stderr": "ModuleNotFoundError: No module named 'pytest'\n",
    }


def test_renderers_preserve_bootstrap_status_byte_identity():
    passing_map = json.loads(_render_acceptance_map(bootstrap_status="PASS"))
    passing_matrix = _render_token_matrix(bootstrap_status="PASS").decode("utf-8")
    assert _derive_retained_bootstrap_status(passing_map, passing_matrix) == "PASS"

    blocked_map = json.loads(_render_acceptance_map(bootstrap_status="TOOLING_BLOCKED"))
    blocked_matrix = _render_token_matrix(bootstrap_status="TOOLING_BLOCKED").decode("utf-8")
    assert _derive_retained_bootstrap_status(blocked_map, blocked_matrix) == "TOOLING_BLOCKED"
    assert _render_acceptance_map(bootstrap_status="PASS").endswith(b"\n")
    assert _render_token_matrix(bootstrap_status="PASS").endswith(b"\n")


def test_retained_bootstrap_status_conflict_refuses():
    acceptance = json.loads(_render_acceptance_map(bootstrap_status="PASS"))
    matrix = _render_token_matrix(bootstrap_status="TOOLING_BLOCKED").decode("utf-8")
    with pytest.raises(ValueError, match="conflicting retained bootstrap status"):
        _derive_retained_bootstrap_status(acceptance, matrix)


def test_one_path_diff_allows_exact_sanity_path_only():
    old = b'{"path":"artifacts/sanity/sanity.log"}\n'
    new = b'{"path":"audit/gates/sanity_pipeline/sanity_pipeline.log"}\n'
    assert _one_path_diff_ok(old, new)
    assert not _one_path_diff_ok(old + old, new + new)
    assert not _one_path_diff_ok(old, b'{"path":"other"}\n')


def test_selective_acceptance_bindings_exact_write_set_and_no_check_specs(tmp_path, monkeypatch):
    acceptance_path = tmp_path / "docs/acceptance_map_epic024.json"
    matrix_path = tmp_path / "audit/qa/hde-epic024/token_evidence_matrix.md"
    acceptance_path.parent.mkdir(parents=True)
    matrix_path.parent.mkdir(parents=True)
    current_map = _render_acceptance_map(bootstrap_status="PASS")
    current_matrix = _render_token_matrix(bootstrap_status="PASS")
    old_map = current_map.replace(
        b"audit/gates/sanity_pipeline/sanity_pipeline.log",
        b"artifacts/sanity/sanity.log",
        1,
    )
    old_matrix = current_matrix.replace(
        b"audit/gates/sanity_pipeline/sanity_pipeline.log",
        b"artifacts/sanity/sanity.log",
        1,
    )
    acceptance_path.write_bytes(old_map)
    matrix_path.write_bytes(old_matrix)

    monkeypatch.setattr(harness, "ACCEPTANCE_MAP_PATH", acceptance_path)
    monkeypatch.setattr(harness, "TOKEN_MATRIX_PATH", matrix_path)
    monkeypatch.setattr(harness, "_check_specs", lambda: pytest.fail("_check_specs called"))

    assert _selective_acceptance_bindings(write=False) == 1
    assert acceptance_path.read_bytes() == old_map
    assert matrix_path.read_bytes() == old_matrix

    assert _selective_acceptance_bindings(write=True) == 0
    assert acceptance_path.read_bytes() == current_map
    assert matrix_path.read_bytes() == current_matrix


def test_check_acceptance_bindings_no_write_when_current(tmp_path, monkeypatch):
    acceptance_path = tmp_path / "docs/acceptance_map_epic024.json"
    matrix_path = tmp_path / "audit/qa/hde-epic024/token_evidence_matrix.md"
    acceptance_path.parent.mkdir(parents=True)
    matrix_path.parent.mkdir(parents=True)
    acceptance_bytes = _render_acceptance_map(bootstrap_status="PASS")
    matrix_bytes = _render_token_matrix(bootstrap_status="PASS")
    acceptance_path.write_bytes(acceptance_bytes)
    matrix_path.write_bytes(matrix_bytes)

    monkeypatch.setattr(harness, "ACCEPTANCE_MAP_PATH", acceptance_path)
    monkeypatch.setattr(harness, "TOKEN_MATRIX_PATH", matrix_path)
    assert _selective_acceptance_bindings(write=False) == 0
    assert acceptance_path.read_bytes() == acceptance_bytes
    assert matrix_path.read_bytes() == matrix_bytes
