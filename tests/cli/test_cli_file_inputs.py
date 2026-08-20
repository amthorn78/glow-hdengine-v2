import json
import os
import subprocess
import sys
import hashlib
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


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def test_pair_file_and_ab_file_modes(tmp_path: pathlib.Path):
    a = {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"}
    b = {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"}
    pair = {"left": a, "right": b}
    pa = tmp_path / "A.json"
    pb = tmp_path / "B.json"
    pp = tmp_path / "pair.json"
    _write_json(pa, a)
    _write_json(pb, b)
    _write_json(pp, pair)

    env = _cli_env()
    r_pair = subprocess.run(["hdctl", "showcompat", "--pair-file", str(pp)], capture_output=True, env=env)
    r_ab = subprocess.run(["hdctl", "showcompat", "--a-file", str(pa), "--b-file", str(pb)], capture_output=True, env=env)
    r_ba = subprocess.run(["hdctl", "showcompat", "--a-file", str(pb), "--b-file", str(pa)], capture_output=True, env=env)

    assert r_pair.returncode == 0
    assert r_ab.returncode == 0
    assert r_ba.returncode == 0

    for result in (r_pair, r_ab, r_ba):
        out = result.stdout
        assert out.endswith(b"\n") and b"\n\n" not in out
        obj = json.loads(out)
        compat = obj.get("compat") or {}
        assert isinstance(compat.get("categories"), list)

    assert _sha(r_ab.stdout) == _sha(r_ba.stdout)
