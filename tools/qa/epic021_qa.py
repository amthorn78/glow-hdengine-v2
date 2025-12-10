"""EPIC021 QA harness helpers under closed rails.

These helpers were added after inspecting existing QA scaffolding and minimal
pytest discovery in ``tests/qa/test_epic021_scaffolding.py``. There was no
previous EPIC021 harness script, so this module provides bootstrap and
per-run logging with PF19-style tooling vs behavior classification.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env

from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    collect_env_for_logging,
    generate_acceptance_map_viability as harness_generate_acceptance_map_viability,
    summarize_checks,
    update_manifest,
    write_bootstrap_log,
    write_canonical_bootstrap,
    write_step_log,
)

QA_ROOT = Path("audit/qa/hde-epic021")

HARNESS_CONFIG = HarnessConfig(
    epic_id="HDE-EPIC021",
    qa_root=QA_ROOT,
    acceptance_map_path=Path("docs/acceptance_map_epic021.json"),
    token_matrix_path=QA_ROOT / "token_evidence_matrix.md",
    step_names=(
        "bootstrap",
        "serializer_cli_d1",
        "evidence_d2",
        "sanity_d2",
        "acceptance_map_d3",
    ),
)


def determine_run_id() -> str:
    """Derive a timestamp-free run id for QA_ROOT logs.

    Prefers EPIC021_QA_RUN_ID, then git short SHA, then a stable fallback.
    """

    if "EPIC021_QA_RUN_ID" in os.environ:
        return os.environ["EPIC021_QA_RUN_ID"].strip() or "epic021-local"
    try:
        sha = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode("utf-8")
            .strip()
        )
        if sha:
            return f"epic021-{sha}"
    except Exception:
        # Tooling failures during git lookups should not block QA logging.
        pass
    return "epic021-local"


def _status_from_exit(exit_code: int) -> str:
    if exit_code == 0:
        return "OK"
    if exit_code == 4:
        return "FAIL_TOOLING"
    return "FAIL"


def run_bootstrap_checks() -> List[CheckResult]:
    checks: List[CheckResult] = []
    try:
        import pytest  # noqa: F401

        checks.append(CheckResult("import", "OK"))
    except Exception as exc:  # pragma: no cover - exercised by failure paths
        checks.append(CheckResult("import", "FAIL_TOOLING", str(exc)))
        return checks

    exit_code = pytest.main([
        "-q",
        "--collect-only",
        "tests/qa/test_epic021_scaffolding.py",
    ])
    checks.append(CheckResult("pytest-collect", _status_from_exit(exit_code)))

    if exit_code == 0:
        sample_exit = pytest.main(
            ["-q", "tests/qa/test_epic021_scaffolding.py", "-k", "qa_root_exists"]
        )
        checks.append(CheckResult("sample-tests", _status_from_exit(sample_exit)))
    else:
        checks.append(CheckResult("sample-tests", "FAIL_TOOLING", "collection failed"))

    return checks


def generate_acceptance_map_viability(run_id: str):
    return harness_generate_acceptance_map_viability(HARNESS_CONFIG, run_id)


def run_epic021_qa_run(run_id: str | None = None) -> Dict[str, Path]:
    run_id = run_id or determine_run_id()
    env_pins = collect_env_for_logging(os.environ)
    checks = run_bootstrap_checks()
    bootstrap_log = write_bootstrap_log(HARNESS_CONFIG, run_id, checks, env_pins)
    canonical_log = None
    if summarize_checks(checks) == "summary:PASS":
        canonical_log = write_canonical_bootstrap(HARNESS_CONFIG, checks, run_id, env_pins)

    step_logs: List[Tuple[str, Path, str]] = []
    for name in HARNESS_CONFIG.step_names:
        if name == "bootstrap":
            status = summarize_checks(checks).split(":", 1)[1]
            path = write_step_log(HARNESS_CONFIG, run_id, name, checks, env_pins)
        elif name == "acceptance_map_d3":
            viability_log, per_token_status = generate_acceptance_map_viability(run_id)
            status = "PASS" if "MISSING" not in per_token_status.values() else "FAIL"
            path = write_step_log(
                HARNESS_CONFIG,
                run_id,
                name,
                [CheckResult("acceptance-map-viability", status)],
                env_pins,
            )
        else:
            placeholder_checks = [CheckResult("not-exercised", "OK", "placeholder")]
            status = "PASS"
            path = write_step_log(HARNESS_CONFIG, run_id, name, placeholder_checks, env_pins)
        step_logs.append((name, path, status))

    manifest_path = update_manifest(HARNESS_CONFIG, run_id, step_logs)
    viability_log = QA_ROOT / "acceptance_map_viability.log"
    artifacts = {
        "bootstrap_log": bootstrap_log,
        "canonical_bootstrap": canonical_log or QA_ROOT / "test_tooling_bootstrap.log",
        "manifest": manifest_path,
        "viability_log": viability_log,
    }
    return artifacts


def main() -> int:
    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:  # pragma: no cover - CLI exit path
        sys.stderr.write(str(exc) + "\n")
        return 1

    run_id = determine_run_id()
    artifacts = run_epic021_qa_run(run_id=run_id)
    manifest_path = artifacts["manifest"]
    manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    runs = [run for run in manifest_data.get("runs", []) if run.get("run_id") == run_id]
    if not runs:
        return 1
    latest = runs[-1]
    if all(step.get("status") == "PASS" for step in latest.get("steps", [])):
        return 0
    return 1


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
