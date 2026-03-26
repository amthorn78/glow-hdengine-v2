from __future__ import annotations

import json
import os
import subprocess
import sys
import sysconfig


PAIR = {
    "left": {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"},
    "right": {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"},
}


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env.setdefault("PATH", f"{scripts_dir}:{env.get('PATH', '')}")
    env.update(
        {
            "SAFE_MODE": "0",
            "ALLOW_NETWORK": "1",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": "hdengine-dev",
            "RELEASE_ID": "0" * 64,
            "PRODUCT_INVOCATION_TAG": "INV-ABBA",
        }
    )
    return env


def _birth_args(pair: dict[str, dict[str, str]]) -> list[str]:
    left = pair["left"]
    right = pair["right"]
    return [
        "--birthdate-a",
        left["birthdate"],
        "--birthtime-a",
        left["birthtime"],
        "--location-a",
        left["location"],
        "--birthdate-b",
        right["birthdate"],
        "--birthtime-b",
        right["birthtime"],
        "--location-b",
        right["location"],
        "--source",
        "vendor",
    ]


def _run_showcompat(pair: dict[str, dict[str, str]]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [sys.executable, "scripts/hdctl.py", "showcompat", *_birth_args(pair)],
        capture_output=True,
        env=_cli_env(),
    )


def test_internal_compat_ab_ba_parity_is_canonical_bytes_identical() -> None:
    ab = _run_showcompat(PAIR)
    ba = _run_showcompat({"left": PAIR["right"], "right": PAIR["left"]})

    assert ab.returncode == ba.returncode == 0
    assert ab.stderr == ba.stderr == b""
    ab_payload = json.loads(ab.stdout)
    ba_payload = json.loads(ba.stdout)

    assert ab.stdout.endswith(b"\n")
    assert ba.stdout.endswith(b"\n")
    assert b"\r\n" not in ab.stdout
    assert b"\r\n" not in ba.stdout
    assert set(ab_payload) == {"a", "b", "compat", "viewer_prefs"}
    assert ab_payload == ba_payload
    assert ab.stdout == ba.stdout
