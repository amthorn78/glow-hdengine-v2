"""Keys-only HTTP logging utilities."""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

LOG_PATH = Path("artifacts/logs/keys_only.sample.jsonl")
LOG_PATH_ENV = "HDE_KEYS_ONLY_LOG_PATH"


def active_log_path() -> Path:
    override = os.getenv(LOG_PATH_ENV)
    return Path(override) if override else LOG_PATH
_ALLOWED_KEYS = {"at", "route", "status", "duration_ms", "idempotence_hash", "release_id"}


def _round_duration(value: float) -> float:
    return round(float(value), 3)


def log_http_call(*, route: str, status: Any, duration_ms: float, release_id: str | None = None,
                  idempotence_hash: str | None = None) -> None:
    """Append a keys-only HTTP log record.

    The log schema intentionally limits itself to PF04's allow-list. The helper is
    defensive: any exception while logging is swallowed to avoid interfering with
    the caller's primary control flow.
    """
    try:
        path = active_log_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "at": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
            "route": route,
            "status": status,
            "duration_ms": _round_duration(duration_ms),
        }
        if release_id is not None:
            record["release_id"] = release_id
        if idempotence_hash is not None:
            record["idempotence_hash"] = idempotence_hash
        # Hard filter to the allow-list just in case
        record = {k: record[k] for k in record if k in _ALLOWED_KEYS}
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            handle.write("\n")
    except Exception:
        # Logging should never raise; swallow silently.
        return


__all__ = ["log_http_call", "LOG_PATH", "LOG_PATH_ENV", "active_log_path"]
