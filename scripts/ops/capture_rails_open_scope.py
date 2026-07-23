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

from engine.ops.http_log import (
    CAPTURE_LOG_ROOT,
    LOG_PATH_ENV,
    initialize_capture_log,
    read_owned_text,
    replace_owned_text,
)
from engine.db.adapter import retired_db_transport_keys_present

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


def _check_env(environ=None) -> None:
    env = os.environ if environ is None else environ
    retired = retired_db_transport_keys_present(env)
    if retired:
        raise SystemExit(
            "Retired database transport environment names are present: "
            + ",".join(retired)
        )
    if not (env.get("DATABASE_URL") or "").strip():
        raise SystemExit("Missing required environment value: DATABASE_URL")
    for key, expected in REQUIRED_ENV.items():
        actual = env.get(key)
        if actual != expected:
            raise SystemExit(f"Expected {key}={expected!r} but saw {actual!r}")


def _child_log_path() -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return CAPTURE_LOG_ROOT / f"keys_only.{os.getpid()}.{stamp}.jsonl"


def _run_command(command: Sequence[str], *, log_path: Path) -> None:
    print("Running:", " ".join(command))
    env = os.environ.copy()
    env[LOG_PATH_ENV] = str(log_path)
    result = subprocess.run(command, check=False, env=env)
    if result.returncode:
        raise SystemExit(
            f"Command {' '.join(command)} failed with exit code {result.returncode}"
        )


def _load_records(log_path: Path) -> Iterable[dict[str, object]]:
    if not log_path.exists():
        raise SystemExit(f"Log file {log_path} not found")
    for line_number, line in enumerate(
        read_owned_text(log_path).splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"Invalid JSON on line {line_number} of {log_path}: {exc}"
            ) from exc
        if not isinstance(value, dict):
            raise SystemExit(f"Invalid record on line {line_number} of {log_path}")
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
    lines = [
        "captured_at_utc: "
        + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        f"safe_mode: {os.getenv('SAFE_MODE', '<unset>')}",
        f"allow_network: {os.getenv('ALLOW_NETWORK', '<unset>')}",
        f"database_url_present: {'DATABASE_URL' in os.environ}",
        "provider: psycopg",
        "route_counts:",
    ]
    lines.extend(f"  {route} {counts[route]}" for route in sorted(counts))
    lines.append(f"vendor_call_count: {vendor_count}")
    text = "\n".join(lines) + "\n"
    replace_owned_text(SUMMARY_PATH, text)
    print(f"Wrote {SUMMARY_PATH} ({len(text)} bytes)")
    if vendor_count:
        raise SystemExit(
            f"Detected {vendor_count} vendor HTTP calls; rails-open scope violated"
        )
    return vendor_count


def main() -> int:
    _check_env()
    log_path = _child_log_path()
    initialize_capture_log(log_path)
    for command in HARNESS_COMMANDS:
        _run_command(command, log_path=log_path)
    _write_summary(_load_records(log_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
