#!/usr/bin/env python3
"""Invoke and strictly validate the canonical release-sanity pipeline.

Two exact log models are accepted, byte for byte: the generic final PASS log
(exit 0) and, under PF10 — HDE Build Notes §2.15, the NOT_ADMITTED log in which
exactly the release-admission-gated stages read ``NOT_ADMITTED`` while every
other stage reads ``OK`` (exit ``RELEASE_NOT_ADMITTED_EXIT_CODE``, never 0).
``summary:FAIL``, a malformed log, a noisy run, or a log matching neither model
fails.  The constants below are an independent copy of the pipeline's model;
``tests/evidence/test_sanity_pipeline.py`` pins them equal.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log"
PINS = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
STAGE_NAMES = (
    "01 Environment pins", "02 Identity and release provenance", "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks", "05 A7 Catalog transport",
    "06 CI rails", "07 Direct DB selection contract", "08 Direct DB posture artifacts",
    "09 BodyGraph policy", "10 Configured-v2 mapped-cache behavior",
    "11 Human Index and Machine Mirror refresh", "12 Evidence-path validation",
    "13 Mirror schema and index/mirror hash validation",
    "14 Topology orientation validation", "15 Final-LF validation",
)
# Distinct non-admitted exit code (never 0, never 1, never argparse's 2).
RELEASE_NOT_ADMITTED_EXIT_CODE = 3
NOT_ADMITTED_STATUS = "NOT_ADMITTED"
RELEASE_ADMISSION_GATED_STAGES = (STAGE_NAMES[3], STAGE_NAMES[4], STAGE_NAMES[5])
NOT_ADMITTED_MARKER = "SANITY_PIPELINE_GATE:RELEASE_NOT_ADMITTED"


def _render(statuses: dict[str, str], first_failed: str, summary: str) -> bytes:
    lines = [
        "run:sanity-pipeline",
        "pipeline_identity:hde-release-sanity-v1",
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC",
        "env_pins:audit/gates/determinism/env_pins.log",
    ]
    for name in STAGE_NAMES:
        lines.append(f"check {name}:{statuses.get(name, 'OK')}")
    lines.extend((f"first_failed_stage:{first_failed}", f"summary:{summary}"))
    return ("\n".join(lines) + "\n").encode("utf-8")


def _expected_log() -> bytes:
    return _render({}, "NONE", "PASS")


def _expected_not_admitted_log() -> bytes:
    return _render(
        {name: NOT_ADMITTED_STATUS for name in RELEASE_ADMISSION_GATED_STAGES},
        "NONE",
        NOT_ADMITTED_STATUS,
    )


def _read_log() -> bytes | None:
    try:
        data = LOG.read_bytes()
        data.decode("utf-8")
    except (OSError, UnicodeError):
        return None
    return data


def _valid_log() -> bool:
    return _read_log() == _expected_log()


def _valid_not_admitted_log() -> bool:
    return _read_log() == _expected_not_admitted_log()


def main() -> int:
    env = os.environ.copy()
    env.update(PINS)
    result = subprocess.run(
        [sys.executable, "tools/evidence/run_sanity_pipeline.py"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    silent = result.stdout == "" and result.stderr == ""
    if result.returncode == 0 and silent and _valid_log():
        return 0
    if result.returncode == RELEASE_NOT_ADMITTED_EXIT_CODE and silent and _valid_not_admitted_log():
        print(NOT_ADMITTED_MARKER)
        return RELEASE_NOT_ADMITTED_EXIT_CODE
    if result.stdout:
        print(result.stdout, end="", file=sys.stdout)
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode == RELEASE_NOT_ADMITTED_EXIT_CODE:
        # The distinct code without the exact NOT_ADMITTED model is a failure.
        return 1
    return result.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
