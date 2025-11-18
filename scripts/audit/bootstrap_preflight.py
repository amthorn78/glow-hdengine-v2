#!/usr/bin/env python3
"""Run bootstrap checks for Codespaces readiness."""
from __future__ import annotations

import datetime as _dt
import json
import subprocess
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _cli_help() -> str:
    cmd = [sys.executable, "-m", "engine.cli", "--help"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"CLI help failed (exit={proc.returncode})")
    stdout_len = len(proc.stdout.encode("utf-8"))
    return f"CLI_HELP_OK exit={proc.returncode} stdout_bytes={stdout_len}"


def _endpoints_probe(prod_file: Path) -> str:
    payload = json.loads(prod_file.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit("Production endpoints JSON must be an object at the top level")
    envs = len(payload)
    services = sum(len(v) for v in payload.values() if isinstance(v, dict))
    return f"PROD_ENDPOINTS_OK envs={envs} services={services}"


def main() -> None:
    repo_root = _repo_root()
    prod_file = repo_root / "docs/run/PROD_ENDPOINTS.json"
    if not prod_file.is_file():
        raise SystemExit(f"Missing production endpoints file: {prod_file}")

    timestamp = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    log_lines = [
        f"timestamp_utc={timestamp}",
        _cli_help(),
        _endpoints_probe(prod_file),
    ]

    output_path = repo_root / "audit/bootstrap/preflight.log"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
