import json
import os
import subprocess
import sys
import sysconfig

import pytest

pytestmark = pytest.mark.epic006

PAIR = '{"left":{"birthdate":"1990-01-10","birthtime":"14:05","location":"Chicago, US"},"right":{"birthdate":"1992-03-04","birthtime":"08:15","location":"Berlin, DE"}}'


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    return env


def test_canonical_and_numeric_free():
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)
    result = subprocess.run(["hdctl", "showcompat"], input=(PAIR + "\n").encode(), capture_output=True, env=_cli_env())
    assert result.returncode == 0
    out = result.stdout
    assert out.endswith(b"\n") and b"\n\n" not in out
    payload = json.loads(out)
    compat = payload.get("compat") or {}
    assert isinstance(compat.get("categories"), list)
