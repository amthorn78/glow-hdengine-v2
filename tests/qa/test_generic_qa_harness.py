import json
from pathlib import Path

import pytest

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, DeterminismEnvError
from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    collect_env_for_logging,
    generate_acceptance_map_viability,
    summarize_checks,
    update_manifest,
    validate_env_pins,
    write_bootstrap_log,
)


@pytest.fixture
def harness_config(tmp_path: Path) -> HarnessConfig:
    qa_root = tmp_path / "qa_root"
    qa_root.mkdir(parents=True, exist_ok=True)
    acceptance_map = tmp_path / "acceptance_map.json"
    acceptance_map.write_text(
        json.dumps({"tokens": [{"name": "TOKEN_A"}, {"name": "TOKEN_B"}]}),
        encoding="utf-8",
    )
    token_matrix = qa_root / "token_evidence_matrix.md"
    token_matrix.write_text(
        "\n".join(
            [
                "| TOKEN_A | desc | evidence_a | placeholder | placeholder | implemented |",
                "| TOKEN_B | desc | evidence_b | placeholder | placeholder | planned |",
            ]
        ),
        encoding="utf-8",
    )
    return HarnessConfig(
        epic_id="TEST-EPIC",
        qa_root=qa_root,
        acceptance_map_path=acceptance_map,
        token_matrix_path=token_matrix,
        step_names=("bootstrap", "acceptance_map_d3"),
    )


def test_validate_env_pins_blocks_missing(monkeypatch: pytest.MonkeyPatch, harness_config):
    monkeypatch.delenv("SAFE_MODE", raising=False)
    with pytest.raises(DeterminismEnvError):
        validate_env_pins()

    run_dir = harness_config.qa_root / "blocked-run"
    assert not run_dir.exists()


def test_collect_env_creates_run_directory(harness_config):
    env_pins = collect_env_for_logging(DETERMINISM_ENV_PINS)
    bootstrap_log = write_bootstrap_log(
        harness_config,
        "run-123",
        [CheckResult("bootstrap", "OK")],
        env_pins,
    )

    assert bootstrap_log.exists()
    contents = bootstrap_log.read_text(encoding="utf-8")
    assert "env:" in contents
    assert harness_config.qa_root.joinpath("run-123").is_dir()


def test_manifest_dedupes_run_entries(harness_config):
    env_pins = collect_env_for_logging(DETERMINISM_ENV_PINS)
    step_log = write_bootstrap_log(
        harness_config, "dedupe-run", [CheckResult("bootstrap", "OK")], env_pins
    )
    steps = [("bootstrap", step_log, "PASS")]

    manifest_path = update_manifest(harness_config, "dedupe-run", steps)
    first_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len([run for run in first_manifest["runs"] if run["run_id"] == "dedupe-run"]) == 1

    manifest_path = update_manifest(harness_config, "dedupe-run", steps)
    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len([run for run in manifest_data["runs"] if run["run_id"] == "dedupe-run"]) == 1


def test_viability_log_matches_expected_format(harness_config):
    log_path, token_status = generate_acceptance_map_viability(harness_config, "viability-check")

    assert log_path.exists()
    content = log_path.read_text(encoding="utf-8")
    assert "summary:" in content
    assert "token TOKEN_A" in content
    assert "token TOKEN_B" in content
    assert token_status["TOKEN_A"] == "COVERED"
    assert token_status["TOKEN_B"] == "PLANNED"
    assert content.splitlines()[-1].startswith("summary: COVERED=1 PLANNED=1 MISSING=0")


def test_summarize_checks_respects_failures():
    assert summarize_checks([CheckResult("ok", "OK")]) == "summary:PASS"
    assert summarize_checks([CheckResult("bad", "FAIL")]) == "summary:FAIL"
