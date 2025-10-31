import os
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


def test_hdctl_and_module_help():
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)
    env = _cli_env()
    r1 = subprocess.run(["hdctl", "--help"], capture_output=True, text=True, env=env)
    r2 = subprocess.run([sys.executable, "-m", "engine.cli", "--help"], capture_output=True, text=True, env=env)
    assert r1.returncode == 0
    assert r2.returncode == 0
    assert r1.stdout == r2.stdout
