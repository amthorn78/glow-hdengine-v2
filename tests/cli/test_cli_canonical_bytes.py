import json
import os
import subprocess
import sys
import sysconfig

import pytest

from engine.serializer.canon import sercanon
from engine.presenter import emitter

pytestmark = pytest.mark.epic006

PAIR = '{"left":{"birthdate":"1990-01-10","birthtime":"14:05","location":"Chicago, US"},"right":{"birthdate":"1992-03-04","birthtime":"08:15","location":"Berlin, DE"}}'


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": "hdengine-dev",
            "RELEASE_ID": "0" * 64,
            "PRODUCT_INVOCATION_TAG": "INV-TEST",
        }
    )
    return env


def _assert_canonical_bytes(data: bytes) -> dict:
    assert data.endswith(b"\n") and b"\n\n" not in data
    assert b"\r\n" not in data
    payload = json.loads(data)
    assert sercanon(payload) == data
    return payload


def _run_hdctl(args: list[str], *, stdin: bytes | None = None) -> subprocess.CompletedProcess:
    base = [sys.executable, "scripts/hdctl.py"]
    return subprocess.run(base + args, input=stdin, capture_output=True, env=_cli_env())


def test_showcompat_stdout_is_canonical():
    result = _run_hdctl(["showcompat"], stdin=(PAIR + "\n").encode())
    assert result.returncode == 0
    assert result.stderr == b""
    payload = _assert_canonical_bytes(result.stdout)
    assert result.stdout == emitter.emit_public(payload)
    assert set(payload) == {"a", "b", "compat", "viewer_prefs"}
    compat = payload["compat"]
    assert isinstance(compat.get("categories"), list)
    assert compat.get("meta", {}).get("release_id")


def test_reader_dump_and_admin_sidecars_are_canonical(tmp_path: os.PathLike[str]):
    pair_path = tmp_path / "pair.json"
    pair_path.write_text(PAIR + "\n", encoding="utf-8")

    reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"

    result = _run_hdctl(
        [
            "showcompat",
            "--pair-file",
            str(pair_path),
            "--dump-reader",
            str(reader_path),
            "--dump-admin-dir",
            str(admin_dir),
        ]
    )

    assert result.returncode == 0
    assert result.stderr == b""

    _assert_canonical_bytes(result.stdout)
    _assert_canonical_bytes(reader_path.read_bytes())

    produced = sorted(admin_dir.glob("*"))
    assert produced, "expected admin dumps to be written"
    for path in produced:
        if path.suffix == ".sha256":
            assert path.read_text(encoding="utf-8").endswith("\n")
            continue
        _assert_canonical_bytes(path.read_bytes())


def test_aux_preview_admin_out_is_canonical(tmp_path: os.PathLike[str]):
    admin_out = tmp_path / "aux_admin.json"
    result = _run_hdctl(
        [
            "aux-preview",
            "--category",
            "harmony",
            "--band",
            "Cool",
            "--perspective",
            "shared",
            "--admin-out",
            str(admin_out),
        ]
    )

    assert result.returncode == 0
    assert result.stderr == b""
    _assert_canonical_bytes(admin_out.read_bytes())
