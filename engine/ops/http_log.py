"""Keys-only HTTP logging utilities."""
from __future__ import annotations

import json
import os
import re
import secrets
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


_DIR_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
_NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)


def _open_parent_dir(path: Path, *, create: bool) -> int:
    """Open and pin every parent component without following symbolic links."""

    if not path.name or path.name in {".", ".."}:
        raise OSError("unsafe_keys_only_log_target")
    if path.is_absolute():
        parent_fd = os.open("/", _DIR_FLAGS)
        parts = path.parent.parts[1:]
    else:
        parent_fd = os.open(".", _DIR_FLAGS)
        parts = path.parent.parts
    try:
        for part in parts:
            if part in {"", "."}:
                continue
            if part == ".." or "/" in part:
                raise OSError("unsafe_keys_only_log_parent")
            if create:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=parent_fd)
                except FileExistsError:
                    pass
            child_fd = os.open(part, _DIR_FLAGS, dir_fd=parent_fd)
            try:
                if not stat.S_ISDIR(os.fstat(child_fd).st_mode):
                    raise OSError("unsafe_keys_only_log_parent")
            except BaseException:
                os.close(child_fd)
                raise
            os.close(parent_fd)
            parent_fd = child_fd
        return parent_fd
    except BaseException:
        os.close(parent_fd)
        raise


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("keys_only_log_write_failed")
        view = view[written:]


def _append_record(path: Path, payload: str) -> None:
    parent_fd = _open_parent_dir(path, create=True)
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT | _NOFOLLOW
    fd = -1
    try:
        fd = os.open(path.name, flags, 0o600, dir_fd=parent_fd)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError("unsafe_keys_only_log_target")
        _write_all(fd, (payload + "\n").encode("utf-8"))
    finally:
        if fd >= 0:
            os.close(fd)
        os.close(parent_fd)


def initialize_capture_log(path: Path) -> None:
    """Create an owned empty capture log without following pre-planted links."""

    if (
        path.is_absolute()
        or path.parent != CAPTURE_LOG_ROOT
        or _CAPTURE_LOG_NAME.fullmatch(path.name) is None
    ):
        raise ValueError("invalid_keys_only_capture_path")
    parent_fd = _open_parent_dir(path, create=True)
    fd = -1
    try:
        fd = os.open(
            path.name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | _NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError("unsafe_keys_only_log_target")
        os.fsync(fd)
        os.fsync(parent_fd)
    finally:
        if fd >= 0:
            os.close(fd)
        os.close(parent_fd)


def read_owned_text(path: Path) -> str:
    """Read a regular file through a pinned, no-follow directory chain."""

    parent_fd = _open_parent_dir(path, create=False)
    fd = -1
    try:
        fd = os.open(path.name, os.O_RDONLY | _NOFOLLOW, dir_fd=parent_fd)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError("unsafe_keys_only_log_target")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks).decode("utf-8", "strict")
    finally:
        if fd >= 0:
            os.close(fd)
        os.close(parent_fd)


def replace_owned_text(path: Path, text: str) -> None:
    """Atomically replace a text file inside a pinned, no-follow directory."""

    parent_fd = _open_parent_dir(path, create=True)
    temporary = f".{path.name}.{os.getpid()}.{secrets.token_hex(8)}.tmp"
    fd = -1
    try:
        fd = os.open(
            temporary,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | _NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise OSError("unsafe_keys_only_log_target")
        _write_all(fd, text.encode("utf-8"))
        os.fsync(fd)
        os.close(fd)
        fd = -1
        os.replace(
            temporary,
            path.name,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        os.fsync(parent_fd)
    finally:
        if fd >= 0:
            os.close(fd)
        try:
            os.unlink(temporary, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        os.close(parent_fd)


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
    "initialize_capture_log",
    "read_owned_text",
    "replace_owned_text",
]
