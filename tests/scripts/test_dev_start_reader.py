"""Owner tests for the canonical dev runner start script and VERIFY.sh.

HDE-CRD-0002 S09/S10 (IF-10; EC-2): ``scripts/dev_start_reader.sh`` propagates
``APP_ENV`` exactly as the caller supplies it, including unset and empty, and
never defaults it (HDE Architecture §3.8.1; HDE-Mechanics Guide "Dev Reader
start helpers"); the runner it starts serves the dev ``GET /reader`` only for an
explicit ``APP_ENV=dev``.  ``VERIFY.sh`` drives that runner and must pass.
Loopback only, closed rails.
"""

from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "dev_start_reader.sh"
VERIFY = ROOT / "VERIFY.sh"
_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _env(tmp_path: Path, **extra: str) -> dict[str, str]:
    # ``python`` on PATH runs this interpreter (an exec wrapper keeps a virtual
    # environment), so the runner imports this checkout with the test's packages.
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    wrapper = bin_dir / "python"
    wrapper.write_text(f'#!/bin/sh\nexec "{sys.executable}" "$@"\n', encoding="utf-8")
    wrapper.chmod(0o755)
    env = {key: value for key, value in os.environ.items() if key != "APP_ENV"}
    env.update(_RAILS)
    env["PATH"] = f"{bin_dir}{os.pathsep}{env.get('PATH', '')}"
    env["PYTHONPATH"] = str(ROOT)
    env.update(extra)
    return env


def _reader_url(port: int) -> str:
    query = (
        f"v=1&a={ROOT / 'fixtures/charts/alice.json'}&b={ROOT / 'fixtures/charts/bob.json'}"
        "&a_tz=UTC&b_tz=UTC"
    )
    return f"http://127.0.0.1:{port}/reader?{query}"


def _get(url: str) -> tuple[int, bytes]:
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:  # noqa: S310 - loopback only
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()


def _start_and_get(env: dict[str, str], port: int) -> tuple[str, int, bytes]:
    proc = subprocess.Popen(
        ["bash", str(SCRIPT)],
        cwd=ROOT,
        env={**env, "PORT": str(port)},
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        deadline = time.monotonic() + 60
        while True:
            assert proc.poll() is None, proc.stdout.read().decode("utf-8", "replace")
            try:
                status, body = _get(_reader_url(port))
                break
            except (ConnectionError, urllib.error.URLError, OSError):
                assert time.monotonic() < deadline, "runner did not start"
                time.sleep(0.25)
    finally:
        proc.terminate()
        try:
            out, _ = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, _ = proc.communicate()
    return out.decode("utf-8", "replace"), status, body


def test_runner_with_explicit_dev_serves_reader(tmp_path: Path) -> None:
    banner, status, body = _start_and_get(_env(tmp_path, APP_ENV="dev"), _free_port())
    assert "[dev-start] APP_ENV=dev " in banner
    assert status == 200, body
    assert body.endswith(b"\n")


def test_runner_propagates_an_unset_app_env_and_the_gate_refuses(tmp_path: Path) -> None:
    banner, status, body = _start_and_get(_env(tmp_path), _free_port())
    assert "[dev-start] APP_ENV=<UNSET> " in banner
    assert status == 403
    assert json.loads(body)["code"] == "ERR_READER_FORBIDDEN"


@pytest.mark.parametrize("app_env", ["test", "local", "prod", ""])
def test_runner_keeps_an_explicit_app_env_and_the_gate_refuses_it(tmp_path: Path, app_env: str) -> None:
    banner, status, body = _start_and_get(_env(tmp_path, APP_ENV=app_env), _free_port())
    assert f"[dev-start] APP_ENV={app_env} " in banner
    assert status == 403
    assert json.loads(body)["code"] == "ERR_READER_FORBIDDEN"


def test_verify_script_passes_against_the_canonical_runner(tmp_path: Path) -> None:
    assert shutil.which("curl"), "VERIFY.sh requires curl"
    result = subprocess.run(
        ["bash", str(VERIFY)],
        cwd=ROOT,
        env=_env(tmp_path, APP_ENV="dev", VERIFY_PORT=str(_free_port())),
        capture_output=True,
        text=True,
        timeout=180,
    )
    tokens = [line for line in result.stdout.splitlines() if line.endswith(("_OK", "_FAIL"))]
    assert result.returncode == 0, result.stdout + result.stderr
    assert tokens and all(line.endswith("_OK") for line in tokens), tokens
    assert "READER_200_STATUS_OK" in tokens
    assert "READER_304_STATUS_OK" in tokens


@pytest.mark.parametrize("app_env", [None, "", "test"])
def test_verify_script_refuses_without_an_explicit_dev(tmp_path: Path, app_env: str | None) -> None:
    extra = {} if app_env is None else {"APP_ENV": app_env}
    result = subprocess.run(
        ["bash", str(VERIFY)],
        cwd=ROOT,
        env=_env(tmp_path, VERIFY_PORT=str(_free_port()), **extra),
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 2
    assert "VERIFY_APP_ENV_NOT_DEV" in result.stderr
    assert result.stdout == ""
