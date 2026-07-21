"""Capture HTTP usage scope for a direct-DB open-rails run."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
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
    (sys.executable, "scripts/db_adapter/capture_adapter_introspection.py"),
)
SUMMARY_PATH = Path("artifacts/ops/rails_open_scope.txt")


def _check_env() -> None:
    if not (os.getenv("DATABASE_URL") or "").strip():
        raise SystemExit("Missing required environment value: DATABASE_URL")
    for key, expected in REQUIRED_ENV.items():
        actual = os.getenv(key)
        if actual != expected:
            raise SystemExit(f"Expected {key}={expected!r} but saw {actual!r}")


def _reset_log() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("", encoding="utf-8")


def _run_command(command: Sequence[str]) -> None:
    print("Running:", " ".join(command))
    result = subprocess.run(command, check=False)
    if result.returncode:
        raise SystemExit(
            f"Command {' '.join(command)} failed with exit code {result.returncode}"
        )


def _load_records() -> Iterable[dict[str, object]]:
    if not LOG_PATH.exists():
        raise SystemExit(f"Log file {LOG_PATH} not found")
    for line_number, line in enumerate(
        LOG_PATH.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"Invalid JSON on line {line_number} of {LOG_PATH}: {exc}"
            ) from exc
        if not isinstance(value, dict):
            raise SystemExit(f"Invalid record on line {line_number} of {LOG_PATH}")
        yield value


def _write_summary(records: Iterable[dict[str, object]]) -> int:
    counts: Counter[str] = Counter()
    for entry in records:
        route = str(entry.get("route", ""))
        if route:
            counts[route] += 1
    vendor_count = sum(
        count for route, count in counts.items() if route.startswith("vendor.")
    )
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "captured_at_utc: "
        + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        f"safe_mode: {os.getenv('SAFE_MODE', '<unset>')}",
        f"allow_network: {os.getenv('ALLOW_NETWORK', '<unset>')}",
        f"database_url_present: {bool((os.getenv('DATABASE_URL') or '').strip())}",
        "provider: psycopg",
        "route_counts:",
    ]
    lines.extend(f"  {route} {counts[route]}" for route in sorted(counts))
    lines.append(f"vendor_call_count: {vendor_count}")
    text = "\n".join(lines) + "\n"
    SUMMARY_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {SUMMARY_PATH} ({len(text)} bytes)")
    if vendor_count:
        raise SystemExit(
            f"Detected {vendor_count} vendor HTTP calls; rails-open scope violated"
        )
    return vendor_count


def main() -> int:
    _check_env()
    _reset_log()
    for command in HARNESS_COMMANDS:
        _run_command(command)
    _write_summary(_load_records())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
