#!/usr/bin/env python3
"""Generate showcompat AB/BA parity artifacts using PF05 birth-arg flow."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import sysconfig
from pathlib import Path

from engine.presenter import emitter

PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
}

ARTIFACT_DIR = Path("artifacts/cli")
AB_PATH = ARTIFACT_DIR / "ab.json"
BA_PATH = ARTIFACT_DIR / "ba.json"
SUMMARY_PATH = ARTIFACT_DIR / "summary.json"


def _env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env.setdefault("PATH", f"{scripts_dir}:{env.get('PATH', '')}")
    env.setdefault("SAFE_MODE", "0")
    env.setdefault("ALLOW_NETWORK", "1")
    env.setdefault("LC_ALL", "C")
    env.setdefault("LANG", "C")
    env.setdefault("TZ", "UTC")
    env.setdefault("ENGINE_TAG", "hdengine-dev")
    env.setdefault("RELEASE_ID", "0" * 64)
    env.setdefault("PRODUCT_INVOCATION_TAG", "INV-EPIC025")
    return env


def _birth_args(pair: dict[str, dict[str, str]]) -> list[str]:
    left = pair["left"]
    right = pair["right"]
    return [
        "--birthdate-a",
        left["birthdate"],
        "--birthtime-a",
        left["birthtime"],
        "--location-a",
        left["location"],
        "--birthdate-b",
        right["birthdate"],
        "--birthtime-b",
        right["birthtime"],
        "--location-b",
        right["location"],
        "--source",
        "vendor",
    ]


def _run_showcompat(pair: dict[str, dict[str, str]], env: dict[str, str]) -> subprocess.CompletedProcess[bytes]:
    args = [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(pair)]
    return subprocess.run(args, capture_output=True, env=env)


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _summary_payload(ab_bytes: bytes, ba_bytes: bytes, two_run_bytes: bytes) -> dict[str, object]:
    return {
        "ab_sha256": hashlib.sha256(ab_bytes).hexdigest(),
        "ba_sha256": hashlib.sha256(ba_bytes).hexdigest(),
        "ab_ba_equal": ab_bytes == ba_bytes,
        "two_run_sha256": hashlib.sha256(two_run_bytes).hexdigest(),
        "two_run_equal": ab_bytes == two_run_bytes,
        "commands": {
            "ab": [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(PAIR)],
            "ba": [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args({"left": PAIR["right"], "right": PAIR["left"]})],
            "two_run": [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(PAIR)],
        },
    }


def main() -> int:
    env = _env()
    ab_result = _run_showcompat(PAIR, env=env)
    ba_result = _run_showcompat({"left": PAIR["right"], "right": PAIR["left"]}, env=env)
    two_run = _run_showcompat(PAIR, env=env)

    for label, result in ("ab", ab_result), ("ba", ba_result), ("two", two_run):
        if result.returncode != 0 or result.stderr:
            raise SystemExit(f"showcompat {label} failed: rc={result.returncode}, stderr={result.stderr!r}")
        if not result.stdout.endswith(b"\n"):
            raise SystemExit(f"showcompat {label} missing trailing LF")

    _write_bytes(AB_PATH, ab_result.stdout)
    _write_bytes(BA_PATH, ba_result.stdout)

    summary_bytes = emitter.emit_public(_summary_payload(ab_result.stdout, ba_result.stdout, two_run.stdout))
    _write_bytes(SUMMARY_PATH, summary_bytes)
    return 0


if __name__ == "__main__":  # pragma: no cover - script entrypoint
    raise SystemExit(main())
