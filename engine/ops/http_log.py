"""Keys-only HTTP logging utilities."""
from __future__ import annotations

import json
import os
import re
import stat
from datetime import datetime
from pathlib import Path
from typing import Any

LOG_PATH = Path("artifacts/logs/keys_only.sample.jsonl")
LOG_PATH_ENV = "HDE_KEYS_ONLY_LOG_PATH"
CAPTURE_LOG_ROOT = Path("artifacts/ops/rails_open_scope")
_CAPTURE_LOG_NAME = re.compile(
    r"^keys_only\.[1-9][0-9]*\.[0-9]{8}T[0-9]{6}Z\.jsonl$"
)


def active_log_path() -> Path:
    override = os.getenv(LOG_PATH_ENV)
    if not override:
        return LOG_PATH
    candidate = Path(override)
    if (
        candidate.is_absolute()
        or candidate.parent != CAPTURE_LOG_ROOT
        or _CAPTURE_LOG_NAME.fullmatch(candidate.name) is None
    ):
        raise ValueError("invalid_keys_only_capture_path")
    return candidate
_ALLOWED_KEYS = {"at", "route", "status", "duration_ms", "idempotence_hash", "release_id"}


def _round_duration(value: float) -> float:
    return round(float(value), 3)


def _assert_real_parent(path: Path) -> None:
    current = Path()
    for part in path.parent.parts:
        current /= part
        info = current.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
            raise OSError("unsafe_keys_only_log_parent")


def _append_record(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _assert_real_parent(path)
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags, 0o600)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError("unsafe_keys_only_log_target")
        with os.fdopen(fd, "a", encoding="utf-8") as handle:
            fd = -1
            handle.write(payload)
            handle.write("\n")
    finally:
        if fd >= 0:
            os.close(fd)


def log_http_call(*, route: str, status: Any, duration_ms: float, release_id: str | None = None,
                  idempotence_hash: str | None = None) -> None:
    """Append a keys-only HTTP log record.

    The log schema intentionally limits itself to PF04's allow-list. The helper is
    defensive: any exception while logging is swallowed to avoid interfering with
    the caller's primary control flow.
    """
    try:
        path = active_log_path()
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
        _append_record(path, json.dumps(record, sort_keys=True, separators=(",", ":")))
    except Exception:
        # Logging should never raise; swallow silently.
        return


__all__ = [
    "log_http_call",
    "LOG_PATH",
    "LOG_PATH_ENV",
    "CAPTURE_LOG_ROOT",
    "active_log_path",
]
