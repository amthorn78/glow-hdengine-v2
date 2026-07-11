from __future__ import annotations

import json
import os
import subprocess
import sys
import venv
from pathlib import Path

from engine.runtime import identity_meta

ARTIFACTS = (
    Path("artifacts/cli/help/hdctl_help.txt"),
    Path("artifacts/cli/help/showcompat_help.txt"),
    Path("artifacts/cli/help/reject_nonjson.txt"),
    Path("artifacts/cli/ab.json"),
    Path("artifacts/cli/ba.json"),
    Path("artifacts/cli/install/entrypoints.txt"),
    Path("artifacts/cli/summary.json"),
    Path("artifacts/cli/install/installability_summary.json"),
)
CLOSED_RAILS = {
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}
RETIRED_IDENTITY_ENV = {
    "ENGINE_TAG",
    "RELEASE_ID",
    "PRODUCT_INVOCATION_TAG",
}


def test_cli_conformance_artifacts_use_immutable_identity_and_are_current():
    env = os.environ.copy()
    env.update(CLOSED_RAILS)
    before = {path: path.read_bytes() for path in ARTIFACTS}

    subprocess.run(
        [
            sys.executable,
            "tools/cli/generate_cli_conformance_artifacts.py",
            "--check",
        ],
        check=True,
        env=env,
    )

    assert {path: path.read_bytes() for path in ARTIFACTS} == before

    expected_meta = identity_meta()
    for path in (Path("artifacts/cli/ab.json"), Path("artifacts/cli/ba.json")):
        payload = json.loads(path.read_bytes())
        assert payload["conjunction"]["compat"]["meta"] == expected_meta

    summary = json.loads(Path("artifacts/cli/summary.json").read_bytes())
    assert summary["identity"] == {
        "source": "engine.runtime.identity",
        "meta": expected_meta,
    }
    recorded_env = summary["pf05_command_catalog"]["env"]
    assert RETIRED_IDENTITY_ENV.isdisjoint(recorded_env)
    assert recorded_env == {**CLOSED_RAILS, "APP_ENV": "test"}
    assert summary["commands"]["ab"][0] == "python"
    assert summary["installability"]["console_entrypoint"]["path"] == "hdctl"

    expected_version = (
        f"hdctl 0.0.0 ({expected_meta['engine_tag']};"
        f"{expected_meta['release_id']})\n"
    )
    installability = json.loads(
        Path("artifacts/cli/install/installability_summary.json").read_bytes()
    )
    assert installability["module_version"]["stdout"] == expected_version
    assert installability["console_version"]["stdout"] == expected_version
    assert installability["console_entrypoint_path"] == "hdctl"

def test_cli_conformance_check_installs_and_exercises_console(tmp_path):
    venv_dir = tmp_path / "venv"
    venv.EnvBuilder(with_pip=True, system_site_packages=True).create(venv_dir)
    scripts_dir = venv_dir / ("Scripts" if os.name == "nt" else "bin")
    python = scripts_dir / ("python.exe" if os.name == "nt" else "python")
    console = scripts_dir / ("hdctl.exe" if os.name == "nt" else "hdctl")
    assert not console.exists()

    env = os.environ.copy()
    env.update(CLOSED_RAILS)
    env["PATH"] = str(scripts_dir)
    before = {path: path.read_bytes() for path in ARTIFACTS}

    subprocess.run(
        [
            str(python),
            "tools/cli/generate_cli_conformance_artifacts.py",
            "--check",
        ],
        check=True,
        env=env,
    )

    assert console.is_file()
    assert {path: path.read_bytes() for path in ARTIFACTS} == before

