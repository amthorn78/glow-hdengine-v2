import json
import os
import pathlib
import subprocess
import sys
import sysconfig

import pytest

pytestmark = pytest.mark.epic006


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    return env


def _install_cli() -> None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)


def test_missing_file_returns_64_and_stderr():
    _install_cli()
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", "no_such.json"], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr


def test_bad_json_returns_64_and_stderr(tmp_path: pathlib.Path):
    _install_cli()
    bad = tmp_path / "bad.json"
    bad.write_text("{bad}\n", encoding="utf-8")
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", str(bad)], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr


def test_success_writes_stdout_only(tmp_path: pathlib.Path):
    _install_cli()
    payload = {
        "left": {"birthdate": "2000-01-01", "birthtime": "00:00", "location": "Moon"},
        "right": {"birthdate": "2000-02-02", "birthtime": "01:01", "location": "Sun"},
    }
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps(payload), encoding="utf-8")
    result = subprocess.run(
        ["hdctl", "showcompat", "--pair-file", str(pair)],
        capture_output=True,
        text=True,
        env=_cli_env(),
    )
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout.endswith("\n")
    assert result.stdout.strip()


def test_usage_error_writes_stderr_only():
    _install_cli()
    result = subprocess.run(["hdctl"], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert "usage" in result.stderr.lower()


def test_engine_error_writes_stderr_only(monkeypatch, tmp_path: pathlib.Path):
    from engine.cli import main as cli_main
    from engine.bodygraph.vendor_client import VendorError

    def _boom(*args, **kwargs):
        raise VendorError("VENDOR_DOWN", "vendor unavailable")

    monkeypatch.setattr(cli_main, "ingest_vendor_bodygraph", _boom)
    _install_cli()
    result = subprocess.run(
        [
            "hdctl",
            "showcompat",
            "--source",
            "vendor",
            "--birthdate-a",
            "2000-01-01",
            "--birthtime-a",
            "00:00",
            "--location-a",
            "Moon",
            "--birthdate-b",
            "2000-02-02",
            "--birthtime-b",
            "01:01",
            "--location-b",
            "Sun",
        ],
        capture_output=True,
        text=True,
        env=_cli_env(),
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr
    assert result.stderr.endswith("\n")
