#!/usr/bin/env python3
"""Closed-rails Live QA harness for /internal/dev/sampler (EPIC019 D3 Card C2).

Runs the dev Reader via the canonical helper under multiple APP_ENV variants and
logs governed JSONL records for each run.
"""
from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Mapping, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = REPO_ROOT / "audit" / "qa" / "hde-epic019" / "dev_sampler_http"
READER_LOG_DIR = AUDIT_DIR / "reader"

PAYLOAD = {
    "viewer_id": "qa-epic019-dev",
    "candidate_ids": ["qa-A", "qa-B"],
    "seed": "dev-liveqa",
}

ENV_KEYS = ["APP_ENV", "SAFE_MODE", "ALLOW_NETWORK", "LC_ALL", "LANG", "TZ"]


class SamplerHarnessError(RuntimeError):
    """Raised for hard failures that should exit the harness."""


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_dev_sampler_url() -> str:
    url = os.environ.get("DEV_SAMPLER_URL")
    if not url:
        raise SamplerHarnessError("DEV_SAMPLER_URL is required")
    return url


def _parse_url(url: str) -> Tuple[str, int]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise SamplerHarnessError(f"Unsupported DEV_SAMPLER_URL scheme: {parsed.scheme!r}")
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    return host, port


def _wait_for_port(host: str, port: int, *, attempts: int = 40, delay: float = 0.25) -> bool:
    for _ in range(attempts):
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            time.sleep(delay)
    return False


def _base_env(app_env_value: str | None, port: int) -> Dict[str, str]:
    env = os.environ.copy()
    if app_env_value is None:
        env.pop("APP_ENV", None)
    else:
        env["APP_ENV"] = app_env_value
    env.setdefault("SAFE_MODE", "1")
    env.setdefault("ALLOW_NETWORK", "0")
    env.setdefault("LC_ALL", "C")
    env.setdefault("LANG", "C")
    env.setdefault("TZ", "UTC")
    env["PORT"] = str(port)
    return env


def _env_snapshot(env: Mapping[str, str]) -> Dict[str, str]:
    snapshot = {key: env.get(key, "unset") for key in ENV_KEYS}
    snapshot["APP_ENV"] = env.get("APP_ENV", "unset")
    return snapshot


def _start_reader(app_env_value: str | None, host: str, port: int) -> subprocess.Popen[bytes]:
    env = _base_env(app_env_value, port)
    READER_LOG_DIR.mkdir(parents=True, exist_ok=True)
    logfile = (READER_LOG_DIR / f"reader_{app_env_value or 'unset'}.log").open(
        "w", encoding="utf-8"
    )
    proc = subprocess.Popen(
        ["bash", str(REPO_ROOT / "scripts" / "dev_start_reader.sh")],
        cwd=REPO_ROOT,
        env=env,
        stdout=logfile,
        stderr=subprocess.STDOUT,
    )
    if not _wait_for_port(host, port):
        proc.terminate()
        proc.wait(timeout=5)
        raise SamplerHarnessError(f"Reader did not open {host}:{port} in time")
    return proc


def _stop_reader(proc: subprocess.Popen[bytes]) -> None:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def _post_sampler(url: str, payload: Mapping[str, object]) -> Tuple[int | None, str, Dict[str, object]]:
    data = json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    status: int | None = None
    content_type = ""
    body: Dict[str, object] | None = None

    try:
        with urlopen(request, timeout=5) as resp:  # nosec - closed rails local HTTP
            status = resp.getcode()
            content_type = resp.headers.get("Content-Type", "")
            body = json.loads(resp.read().decode("utf-8"))
    except HTTPError as err:
        status = err.code
        content_type = err.headers.get("Content-Type", "") if err.headers else ""
        try:
            body = json.loads(err.read().decode("utf-8"))
        except Exception:
            body = {"raw": err.read().decode("utf-8", errors="replace")}
    except URLError as err:
        return None, content_type, {"error": str(err)}
    except Exception as err:  # pragma: no cover - defensive
        return None, content_type, {"error": str(err)}

    return status, content_type, body or {}


def _log_record(path: Path, record: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fp:
        fp.write(json.dumps(record, sort_keys=True) + "\n")


def _summarize_request(url: str, payload: Mapping[str, object]) -> Dict[str, object]:
    return {
        "url": url,
        "method": "POST",
        "payload_keys": sorted(payload.keys()),
    }


def _summarize_response(status: int | None, content_type: str, body: Mapping[str, object]) -> Dict[str, object]:
    body_keys: Iterable[str] = body.keys() if isinstance(body, Mapping) else []
    return {
        "status": status,
        "content_type": content_type,
        "body_keys": sorted(body_keys),
    }


def _run_mode(mode: str, app_env_value: str | None, url: str, host: str, port: int, log_path: Path) -> bool:
    env = _base_env(app_env_value, port)
    record: Dict[str, object] = {
        "timestamp_utc": _iso_now(),
        "mode": mode,
        "env": _env_snapshot(env),
        "request": _summarize_request(url, PAYLOAD),
    }

    try:
        proc = _start_reader(app_env_value, host, port)
    except SamplerHarnessError as err:
        record["response"] = {"status": None, "error": str(err)}
        _log_record(log_path, record)
        return False

    try:
        status, content_type, body = _post_sampler(url, PAYLOAD)
        record["response"] = _summarize_response(status, content_type, body)
        if isinstance(body, Mapping):
            record["response_body_excerpt"] = {k: body[k] for k in list(body.keys())[:3]}
    finally:
        _stop_reader(proc)

    _log_record(log_path, record)
    return status is not None


def main() -> int:
    dev_sampler_url = _ensure_dev_sampler_url()
    host, port = _parse_url(dev_sampler_url)

    # Ensure rails in this shell
    os.environ.setdefault("SAFE_MODE", "1")
    os.environ.setdefault("ALLOW_NETWORK", "0")
    os.environ.setdefault("LC_ALL", "C")
    os.environ.setdefault("LANG", "C")
    os.environ.setdefault("TZ", "UTC")

    logs = {
        "dev": AUDIT_DIR / "allowed_dev.jsonl",
        "prod": AUDIT_DIR / "forbidden_prod.jsonl",
        "empty": AUDIT_DIR / "forbidden_empty.jsonl",
        "unset": AUDIT_DIR / "forbidden_unset.jsonl",
    }

    for path in logs.values():
        if path.exists():
            path.unlink()

    modes = [
        ("dev", "dev"),
        ("prod", "prod"),
        ("empty", ""),
        ("unset", None),
    ]

    successes = []
    for mode, app_env_value in modes:
        ok = _run_mode(mode, app_env_value, dev_sampler_url, host, port, logs[mode])
        successes.append(ok)

    return 0 if all(successes) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SamplerHarnessError as exc:
        print(f"dev_sampler_live_qa: {exc}", file=sys.stderr)
        raise SystemExit(1)
