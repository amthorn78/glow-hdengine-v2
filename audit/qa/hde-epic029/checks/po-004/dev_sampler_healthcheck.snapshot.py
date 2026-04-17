#!/usr/bin/env python3
"""Dev sampler HTTP harness healthcheck (EPIC019 Card C1).

- Spins up the dev Reader via the canonical adapter runner.
- Posts a minimal payload to DEV_SAMPLER_URL under APP_ENV=dev.
- Repeats under APP_ENV=prod for gating diagnostics (non-fatal).
- Logs rail pins, status codes, HTTP version, and response body summaries.
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
from typing import Any, Dict, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LOG_DIR = REPO_ROOT / "notes" / "dev-sampler"
LOG_DIR = Path(os.environ.get("DEV_SAMPLER_LOG_DIR", DEFAULT_LOG_DIR))
LOG_PATH = Path(os.environ.get("DEV_SAMPLER_LOG_PATH", LOG_DIR / "dev_sampler_healthcheck.log"))
READER_LOG_DIR = LOG_PATH.parent / "reader"

PAYLOAD = {
    "viewer_id": "dev-healthcheck-viewer",
    "candidate_ids": ["dev-cand-1", "dev-cand-2"],
    "seed": "healthcheck",
}


def _log(message: str) -> None:
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"[{timestamp}] {message}"
    print(line)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fp:
        fp.write(line + "\n")


def _env_snapshot() -> Dict[str, str]:
    return {
        "APP_ENV": os.environ.get("APP_ENV", "unset"),
        "SAFE_MODE": os.environ.get("SAFE_MODE", "unset"),
        "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", "unset"),
        "LC_ALL": os.environ.get("LC_ALL", "unset"),
        "LANG": os.environ.get("LANG", "unset"),
        "TZ": os.environ.get("TZ", "unset"),
    }


def _parse_url(url: str) -> Tuple[str, int]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError(f"Unsupported scheme in DEV_SAMPLER_URL: {parsed.scheme!r}")
    if not parsed.hostname:
        raise ValueError("DEV_SAMPLER_URL must include an explicit hostname")
    if parsed.port is None:
        raise ValueError("DEV_SAMPLER_URL must include an explicit port")
    host = parsed.hostname
    port = parsed.port
    return host, port


def _wait_for_port(host: str, port: int, attempts: int = 30, delay: float = 0.25) -> bool:
    for _ in range(attempts):
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except OSError:
            time.sleep(delay)
    return False


def _post_sampler(url: str, payload: Dict[str, Any]) -> Tuple[int | None, str, Dict[str, Any]]:
    data = json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    status: int | None = None
    version = "unknown"
    body: bytes = b""
    headers: Dict[str, Any] = {}

    try:
        with urlopen(request, timeout=5) as resp:
            status = resp.getcode()
            version = {10: "HTTP/1.0", 11: "HTTP/1.1"}.get(getattr(resp, "version", 0), "HTTP/?.?")
            headers = dict(resp.headers.items())
            body = resp.read()
    except HTTPError as err:
        status = err.code
        headers = dict(err.headers.items()) if err.headers else {}
        fp = getattr(err, "fp", None)
        if fp is not None:
            version = {10: "HTTP/1.0", 11: "HTTP/1.1"}.get(getattr(fp, "version", 0), "HTTP/?.?")
        body = err.read()
    except URLError as err:  # pragma: no cover - network errors logged
        _log(f"network_error err={err}")
        return None, version, {"body": str(err)}

    try:
        body_text = body.decode("utf-8")
        parsed_json = json.loads(body_text)
    except Exception:
        parsed_json = {"raw": body.decode("utf-8", errors="replace")}

    return status, version, {"headers": headers, "body": parsed_json}


def _start_reader(app_env: str, host: str, port: int) -> subprocess.Popen[bytes]:
    env = os.environ.copy()
    env["APP_ENV"] = app_env
    env["PORT"] = str(port)
    env.setdefault("SAFE_MODE", "1")
    env.setdefault("ALLOW_NETWORK", "0")
    env.setdefault("LC_ALL", "C")
    env.setdefault("LANG", "C")
    env.setdefault("TZ", "UTC")
    # Reader runner binds to 0.0.0.0; host is used for readiness checks only.
    READER_LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = (READER_LOG_DIR / f"reader_{app_env}.log").open("w", encoding="utf-8")
    proc = subprocess.Popen(
        [sys.executable, "-m", "adapter.http_reader"],
        cwd=REPO_ROOT,
        env=env,
        stdout=log_file,
        stderr=subprocess.STDOUT,
    )
    if not _wait_for_port(host, port):
        proc.terminate()
        proc.wait(timeout=5)
        raise RuntimeError(f"Reader did not open {host}:{port} in time")
    return proc


def _stop_reader(proc: subprocess.Popen[bytes]) -> None:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:  # pragma: no cover - safety belt
        proc.kill()


def _run_check(mode: str, url: str, payload: Dict[str, Any]) -> Tuple[int | None, Dict[str, Any]]:
    host, port = _parse_url(url)
    child_env = {
        "APP_ENV": mode,
        "PORT": str(port),
        "SAFE_MODE": os.environ.get("SAFE_MODE", "1"),
        "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", "0"),
        "LC_ALL": os.environ.get("LC_ALL", "C"),
        "LANG": os.environ.get("LANG", "C"),
        "TZ": os.environ.get("TZ", "UTC"),
    }
    _log(f"starting_reader mode={mode} host={host} port={port} rails={child_env}")
    proc = _start_reader(app_env=mode, host=host, port=port)
    try:
        status, version, body = _post_sampler(url, payload)
        _log(
            f"sampler_response mode={mode} status={status} http_version={version} body={json.dumps(body, sort_keys=True)}"
        )
    finally:
        _stop_reader(proc)
    return status, body


def main() -> int:
    raw_sampler_url = os.environ.get("DEV_SAMPLER_URL")
    dev_sampler_url = raw_sampler_url.strip() if raw_sampler_url is not None else ""
    if not dev_sampler_url:
        _log("DEV_SAMPLER_URL is required and must be non-empty")
        return 1

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    _log(f"dev_sampler_url={dev_sampler_url}")
    _log(f"rails_snapshot={_env_snapshot()}")

    dev_status, dev_body = _run_check("dev", dev_sampler_url, PAYLOAD)
    ok = dev_status == 200

    prod_status, prod_body = _run_check("prod", dev_sampler_url, PAYLOAD)
    _log(
        f"gating_diagnostic expected=403? actual_status={prod_status} body_keys={sorted(prod_body.get('body', {}).keys())}"
    )
    if prod_status != 403:
        _log("gating_discrepancy observed: APP_ENV=prod did not return 403")

    if not ok:
        _log("dev sampler healthcheck failed (status != 200)")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
