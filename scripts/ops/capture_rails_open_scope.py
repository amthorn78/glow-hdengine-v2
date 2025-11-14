"""Capture HTTP usage scope for an open-rails run."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.ops.http_log import LOG_PATH

REQUIRED_ENV = {
    "SAFE_MODE": "0",
    "ALLOW_NETWORK": "1",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}

HARNESS_COMMANDS: Sequence[Sequence[str]] = (
    ("python", "scripts/db_bridge/capture_introspection.py"),
    ("python", "scripts/db_adapter/capture_adapter_introspection.py"),
)

SUMMARY_PATH = Path("artifacts/ops/rails_open_scope.txt")


def _check_env() -> None:
    missing = [key for key in ("DB_BRIDGE_URL", "DATABASE_URL") if not (os.getenv(key) or "").strip()]
    if missing:
        raise SystemExit(f"Missing required environment values: {', '.join(missing)}")
    for key, expected in REQUIRED_ENV.items():
        actual = os.getenv(key)
        if actual != expected:
            raise SystemExit(f"Expected {key}={expected!r} but saw {actual!r}")


def _reset_log() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("", encoding="utf-8")


def _run_command(cmd: Sequence[str]) -> None:
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        raise SystemExit(f"Command {' '.join(cmd)} failed with exit code {result.returncode}")


def _load_records() -> Iterable[dict[str, object]]:
    if not LOG_PATH.exists():
        raise SystemExit(f"Log file {LOG_PATH} not found")
    for idx, line in enumerate(LOG_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON on line {idx} of {LOG_PATH}: {exc}") from exc


def _write_summary(records: Iterable[dict[str, object]]) -> int:
    counts: Counter[str] = Counter()
    entries = list(records)
    for entry in entries:
        route = str(entry.get("route", ""))
        if route:
            counts[route] += 1
    vendor_count = sum(count for route, count in counts.items() if route.startswith("vendor."))

    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"captured_at_utc: {datetime.utcnow().isoformat(timespec='seconds')}Z",
        f"safe_mode: {os.getenv('SAFE_MODE', '<unset>')}",
        f"allow_network: {os.getenv('ALLOW_NETWORK', '<unset>')}",
        f"db_bridge_url_present: {bool((os.getenv('DB_BRIDGE_URL') or '').strip())}",
        f"database_url_present: {bool((os.getenv('DATABASE_URL') or '').strip())}",
        "route_counts:",
    ]
    for route in sorted(counts):
        lines.append(f"  {route} {counts[route]}")
    lines.append(f"vendor_call_count: {vendor_count}")

    text = "\n".join(lines) + "\n"
    SUMMARY_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {SUMMARY_PATH} ({len(text)} bytes)")
    if vendor_count > 0:
        raise SystemExit(f"Detected {vendor_count} vendor HTTP calls; rails-open scope violated")
    return vendor_count


def main() -> int:
    _check_env()
    _reset_log()
    for cmd in HARNESS_COMMANDS:
        _run_command(cmd)
    _write_summary(_load_records())
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as exc:
        raise
    except Exception as exc:  # pragma: no cover - unexpected failure
        print(f"ERROR: {exc}")
        sys.exit(1)
