import json
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


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _run(pair: dict, outdir: pathlib.Path, env: dict[str, str]) -> dict:
    pair_path = outdir / "pair.json"
    admin_dir = outdir / "admin"
    outdir.mkdir(parents=True, exist_ok=True)
    _write_json(pair_path, pair)
    subprocess.run(
        [
            "hdctl",
            "showcompat",
            "--pair-file",
            str(pair_path),
            "--dump-admin-dir",
            str(admin_dir),
        ],
        check=True,
        capture_output=True,
        env=env,
    )
    proof_path = admin_dir / "pair.compat.proof.json"
    return json.loads(proof_path.read_text(encoding="utf-8"))


def test_admin_parity(tmp_path: pathlib.Path):
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True, capture_output=True)
    env = _cli_env()

    left = {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"}
    right = {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"}

    proof_ab = _run({"left": left, "right": right}, tmp_path / "ab", env)
    proof_ba = _run({"left": right, "right": left}, tmp_path / "ba", env)

    assert proof_ab["overall"]["band"] == proof_ba["overall"]["band"]
    assert proof_ab["per_category"].keys() == proof_ba["per_category"].keys()
    assert proof_ab["per_category"] == proof_ba["per_category"]
