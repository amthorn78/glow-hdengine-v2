import os
import subprocess
import sys
import sysconfig
import pathlib

import pytest

pytestmark = pytest.mark.epic006


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    return env


def test_missing_file_returns_64_and_stderr():
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", "no_such.json"], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr


def test_bad_json_returns_64_and_stderr(tmp_path: pathlib.Path):
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)
    bad = tmp_path / "bad.json"
    bad.write_text("{bad}\n", encoding="utf-8")
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", str(bad)], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr
