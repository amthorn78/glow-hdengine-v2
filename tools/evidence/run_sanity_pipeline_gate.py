#!/usr/bin/env python3
"""Invoke and strictly validate the canonical HDE-EPIC038 sanity pipeline."""
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
    "09 BodyGraph policy", "10 Architecture snapshot",
    "11 Configured-v2 mapped-cache local evidence",
    "12 Historical bridge evidence integrity",
    "13 OPS-02 mapped-cache packet validation",
    "14 OPS-03 direct DB posture packet validation",
    "15 Human Index and Machine Mirror refresh", "16 Evidence-path validation",
    "17 Mirror schema and index/mirror hash validation",
    "18 Topology orientation validation", "19 Final-LF validation",
)


def _expected_log() -> bytes:
    lines = [
        "run:sanity-pipeline",
        "pipeline_identity:HDE-EPIC038-PR06-release-sanity",
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC",
        "env_pins:audit/gates/determinism/env_pins.log",
        (
            "ops_evidence:retained_integrity_provenance_secret_safe_only;"
            "historical_nonclaim=true;not_rerun=true"
        ),
    ]
    for name in STAGE_NAMES:
        lines.append(f"check {name}:OK")
        if name == STAGE_NAMES[11]:
            lines.append("stage_result:12:HISTORICAL_INTEGRITY_OK")
    lines.extend(("first_failed_stage:NONE", "summary:PASS"))
    return ("\n".join(lines) + "\n").encode("utf-8")


def _valid_log() -> bool:
    try:
        data = LOG.read_bytes()
        data.decode("utf-8")
    except (OSError, UnicodeError):
        return False
    return data == _expected_log()


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
    if result.returncode == 0 and result.stdout == "" and result.stderr == "" and _valid_log():
        return 0
    if result.stdout:
        print(result.stdout, end="", file=sys.stdout)
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
