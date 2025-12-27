#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env


SANITY_LOG = Path("artifacts/sanity/sanity.log")


@dataclass(frozen=True)
class SanityStep:
    name: str
    command: Sequence[str]


def _render_env_line() -> str:
    ordered = [f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)]
    return ",".join(ordered)


def _write_log(log_path: Path, steps: Iterable[tuple[str, str]], summary: str) -> None:
    lines = ["sanity_pipeline", f"env:{_render_env_line()}"]
    for name, status in steps:
        lines.append(f"check {name}:{status}")
    lines.append(f"summary:{summary}")
    log_text = "\n".join(lines) + "\n"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(log_text, encoding="utf-8")


def _run_command(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True)


def default_steps() -> List[SanityStep]:
    return [
        SanityStep("pytest tests/cli/test_cli_canonical_bytes.py", ["python", "-m", "pytest", "tests/cli/test_cli_canonical_bytes.py"]),
        SanityStep("pytest tests/cli/test_showcompat_parity_and_identity.py", ["python", "-m", "pytest", "tests/cli/test_showcompat_parity_and_identity.py"]),
        SanityStep("pytest tests/invariance/test_bytes_identity.py", ["python", "-m", "pytest", "tests/invariance/test_bytes_identity.py"]),
        SanityStep("ci/checks/check_env_pins.sh", ["ci/checks/check_env_pins.sh"]),
        SanityStep("python ci/checks/check_release_identity.sh", ["python", "ci/checks/check_release_identity.sh"]),
        SanityStep("python tools/evidence/generate_sampler_evidence.py", ["python", "tools/evidence/generate_sampler_evidence.py"]),
        SanityStep("python tools/evidence/generate_engine_core_evidence.py", ["python", "tools/evidence/generate_engine_core_evidence.py"]),
        SanityStep("pytest tests/invariance/test_locale_tz.py", ["python", "-m", "pytest", "tests/invariance/test_locale_tz.py"]),
        SanityStep("python tools/cli/serializer_grep_guard.py", ["python", "tools/cli/serializer_grep_guard.py"]),
        SanityStep("python tools/cli/emitter_symbol_proof.py", ["python", "tools/cli/emitter_symbol_proof.py"]),
        SanityStep("pytest tests/cli/test_serializer_guards.py", ["python", "-m", "pytest", "tests/cli/test_serializer_guards.py"]),
        SanityStep("python tools/order/generate_ordering_artifacts.py", ["python", "tools/order/generate_ordering_artifacts.py"]),
        SanityStep("python tools/evidence/update_evidence_index.py", ["python", "tools/evidence/update_evidence_index.py"]),
        SanityStep("python tools/order/generate_ordering_artifacts.py --check", ["python", "tools/order/generate_ordering_artifacts.py", "--check"]),
        SanityStep("python tools/evidence/update_evidence_index.py --check", ["python", "tools/evidence/update_evidence_index.py", "--check"]),
        SanityStep("python tools/evidence/orientation_demo.py", ["python", "tools/evidence/orientation_demo.py"]),
        SanityStep("python tools/evidence/orientation_demo.py --check", ["python", "tools/evidence/orientation_demo.py", "--check"]),
    ]


def _run_post_index_refresh() -> str:
    """Refresh the evidence index after writing the sanity log."""

    try:
        from tools.evidence import update_evidence_index

        update_evidence_index.main([])
    except SystemExit as exc:  # pragma: no cover - defensive
        return "FAIL" if exc.code else "OK"
    except Exception:  # pragma: no cover - defensive
        return "FAIL"
    return "OK"


def run_pipeline(
    *,
    log_path: Path = SANITY_LOG,
    steps: Sequence[SanityStep] | None = None,
    refresh_index: bool = True,
) -> int:
    ensure_determinism_env()

    resolved_steps = list(steps) if steps is not None else default_steps()
    results: list[tuple[str, str]] = []
    exit_code = 0

    for step in resolved_steps:
        proc = _run_command(step.command)
        status = "OK" if proc.returncode == 0 else "FAIL"
        results.append((step.name, status))
        if status != "OK":
            exit_code = proc.returncode or 1
            break

    # Write the initial log before refreshing the index so the refresh uses the
    # artifacts from this run instead of the previous one.
    summary = "PASS" if exit_code == 0 else "FAIL"
    _write_log(log_path, results, summary)

    post_index_status: str | None = None
    if refresh_index and log_path == SANITY_LOG:
        post_index_status = _run_post_index_refresh()
        results.append(("update_evidence_index.post", post_index_status))
        if post_index_status != "OK" and exit_code == 0:
            exit_code = 1
        summary = "PASS" if exit_code == 0 else "FAIL"
        _write_log(log_path, results, summary)
        _run_post_index_refresh()
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the closed-rails sanity pipeline")
    parser.add_argument("--log-path", type=Path, default=SANITY_LOG, help="sanity log destination")
    args = parser.parse_args(argv)

    try:
        return run_pipeline(log_path=args.log_path)
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
