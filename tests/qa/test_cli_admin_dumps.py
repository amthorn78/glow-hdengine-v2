import json
import os
import stat
import subprocess
import sys
import sysconfig
import pathlib
import hashlib

import pytest

pytestmark = pytest.mark.epic006


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    return env


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_mode_0600(path: pathlib.Path) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    assert mode == 0o600


def test_file_inputs_and_admin_dumps(tmp_path: pathlib.Path):
    env = _cli_env()

    left = {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"}
    right = {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"}
    pair = {"left": left, "right": right}

    a_path = tmp_path / "A.json"
    b_path = tmp_path / "B.json"
    pair_path = tmp_path / "pair.json"
    reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"

    _write_json(a_path, left)
    _write_json(b_path, right)
    _write_json(pair_path, pair)

    result = subprocess.run(
        [
            "hdctl",
            "showcompat",
            "--pair-file",
            str(pair_path),
            "--dump-reader",
            str(reader_path),
            "--dump-admin-dir",
            str(admin_dir),
        ],
        env=env,
        capture_output=True,
    )

    assert result.returncode == 0
    out = result.stdout.decode("utf-8")
    assert out.endswith("\n") and "\n\n" not in out

    reader_raw = reader_path.read_text(encoding="utf-8")
    assert reader_raw.endswith("\n") and "\n\n" not in reader_raw

    expected_names = {
        "pair.left.bodygraph.json",
        "pair.right.bodygraph.json",
        "pair.composite.bodygraph.json",
        "pair.compat.proof.json",
    }

    dumped = {p.name for p in admin_dir.glob("*.json")}
    assert expected_names.issubset(dumped)

    for name in expected_names:
        json_path = admin_dir / name
        sha_path = admin_dir / f"{name}.sha256"
        assert sha_path.exists()
        _assert_mode_0600(json_path)
        _assert_mode_0600(sha_path)
        calc = _sha256(json_path)
        recorded = sha_path.read_text(encoding="utf-8").strip()
        assert calc == recorded

    proof = json.loads((admin_dir / "pair.compat.proof.json").read_text(encoding="utf-8"))
    assert "per_category" in proof
    assert "overall" in proof
    assert "signals" in proof
    assert "constants" in proof
