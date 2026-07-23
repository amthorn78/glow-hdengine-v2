from __future__ import annotations

import json
import os
import sysconfig
from pathlib import Path

from engine.runtime import identity_meta
from tools.cli import generate_cli_conformance_artifacts as generator

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
    before = {path: path.read_bytes() for path in ARTIFACTS}
    current = generator._capture_outputs()

    assert {path: path.read_bytes() for path in ARTIFACTS} == before

    expected_meta = identity_meta()
    for path in (generator.AB_PATH, generator.BA_PATH):
        payload = json.loads(current[path])
        assert payload["conjunction"]["compat"]["meta"] == expected_meta

    current_summary = json.loads(current[generator.SUMMARY_PATH])
    assert current_summary["identity"] == {
        "source": "engine.runtime.identity",
        "meta": expected_meta,
    }
    recorded_env = current_summary["pf05_command_catalog"]["env"]
    assert RETIRED_IDENTITY_ENV.isdisjoint(recorded_env)
    assert recorded_env == {**CLOSED_RAILS, "APP_ENV": "test"}
    assert current_summary["commands"]["ab"][0] == "python"
    assert current_summary["installability"]["console_entrypoint"]["path"] == "hdctl"

    expected_version = (
        f"hdctl 0.0.0 ({expected_meta['engine_tag']};"
        f"{expected_meta['release_id']})\n"
    )
    current_installability = json.loads(current[generator.INSTALLABILITY_SUMMARY_PATH])
    assert current_installability["module_version"]["stdout"] == expected_version
    assert current_installability["console_version"]["stdout"] == expected_version
    assert current_installability["console_entrypoint_path"] == "hdctl"

    frozen_summary = json.loads(before[Path("artifacts/cli/summary.json")])
    frozen_meta = frozen_summary["identity"]["meta"]
    for path in (Path("artifacts/cli/ab.json"), Path("artifacts/cli/ba.json")):
        frozen_payload = json.loads(before[path])
        assert frozen_payload["conjunction"]["compat"]["meta"] == frozen_meta
    frozen_version = (
        f"hdctl 0.0.0 ({frozen_meta['engine_tag']};"
        f"{frozen_meta['release_id']})\n"
    )
    frozen_installability = json.loads(
        before[Path("artifacts/cli/install/installability_summary.json")]
    )
    assert frozen_installability["module_version"]["stdout"] == frozen_version
    assert frozen_installability["console_version"]["stdout"] == frozen_version


def test_cli_conformance_check_exercises_preinstalled_console():
    scripts_dir = Path(sysconfig.get_paths()["scripts"])
    console = scripts_dir / ("hdctl.exe" if os.name == "nt" else "hdctl")
    assert console.is_file()
    assert os.access(console, os.X_OK)

    before = {path: path.read_bytes() for path in ARTIFACTS}
    current = generator._capture_outputs()
    installability = json.loads(current[generator.INSTALLABILITY_SUMMARY_PATH])
    assert installability["console_entrypoint_available"] is True
    assert installability["console_entrypoint_path"] == "hdctl"
    assert {path: path.read_bytes() for path in ARTIFACTS} == before
