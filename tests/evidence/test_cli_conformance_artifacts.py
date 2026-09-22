"""CLI conformance artifacts: frozen capture-time records under PF10 §2.15.

Generation needs an admitted release (and a stored BodyGraph source for the
birth-only conjunction pairs), so the generator refuses truthfully with
``REQUIRES_ADMITTED_RELEASE`` and ``--check`` validates the frozen bytes by digest.
The frozen captures keep their coherent immutable identity.
"""
from __future__ import annotations

import hashlib
import json
import os
import sysconfig
from pathlib import Path

import pytest

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


def test_cli_conformance_generation_refuses_without_admission_and_frozen_captures_are_current(monkeypatch):
    before = {path: path.read_bytes() for path in ARTIFACTS}
    monkeypatch.setattr(generator.subprocess, "run", lambda *a, **k: pytest.fail("CLI subprocess spawned"))

    with pytest.raises(SystemExit) as excinfo:
        generator._capture_outputs()
    assert str(excinfo.value) == generator.REQUIRES_ADMITTED_RELEASE
    with pytest.raises(SystemExit, match=generator.REQUIRES_ADMITTED_RELEASE):
        generator.main([])

    assert {path: path.read_bytes() for path in ARTIFACTS} == before
    assert generator.main(["--check"]) == 0
    assert generator.validate_frozen_captures() == []
    assert set(generator.FROZEN_SHA256) == {path.as_posix() for path in ARTIFACTS}
    assert {
        rel: hashlib.sha256(Path(rel).read_bytes()).hexdigest() for rel in generator.FROZEN_SHA256
    } == generator.FROZEN_SHA256


def test_frozen_cli_conformance_captures_keep_one_immutable_identity():
    frozen_summary = json.loads(Path("artifacts/cli/summary.json").read_bytes())
    frozen_meta = frozen_summary["identity"]["meta"]
    assert frozen_summary["identity"]["source"] == "engine.runtime.identity"
    assert set(frozen_meta) == {"engine_tag", "invocation_tag", "release_id"}
    for path in (Path("artifacts/cli/ab.json"), Path("artifacts/cli/ba.json")):
        frozen_payload = json.loads(path.read_bytes())
        assert frozen_payload["conjunction"]["compat"]["meta"] == frozen_meta
    recorded_env = frozen_summary["pf05_command_catalog"]["env"]
    assert RETIRED_IDENTITY_ENV.isdisjoint(recorded_env)
    assert recorded_env == {**CLOSED_RAILS, "APP_ENV": "test"}
    assert frozen_summary["commands"]["ab"][0] == "python"
    assert frozen_summary["installability"]["console_entrypoint"]["path"] == "hdctl"
    frozen_version = (
        f"hdctl 0.0.0 ({frozen_meta['engine_tag']};"
        f"{frozen_meta['release_id']})\n"
    )
    frozen_installability = json.loads(Path("artifacts/cli/install/installability_summary.json").read_bytes())
    assert frozen_installability["module_version"]["stdout"] == frozen_version
    assert frozen_installability["console_version"]["stdout"] == frozen_version
    assert frozen_installability["console_entrypoint_path"] == "hdctl"


def test_cli_conformance_check_reports_frozen_drift(monkeypatch):
    monkeypatch.setitem(generator.FROZEN_SHA256, "artifacts/cli/summary.json", "0" * 64)
    with pytest.raises(SystemExit, match="DRIFT:artifacts/cli/summary.json"):
        generator.main(["--check"])


def test_cli_conformance_capture_exercises_preinstalled_console_once_admitted(monkeypatch):
    """With admission simulated, the capture reaches the console entrypoint and the
    conjunction step; pre-admission the birth-only pair cannot resolve, so the capture
    ends at that step instead of producing new bytes."""

    scripts_dir = Path(sysconfig.get_paths()["scripts"])
    console = scripts_dir / ("hdctl.exe" if os.name == "nt" else "hdctl")
    assert console.is_file()
    assert os.access(console, os.X_OK)
    assert Path(generator._console_entrypoint_path(generator._env())) == console

    before = {path: path.read_bytes() for path in ARTIFACTS}
    monkeypatch.setattr(generator, "_require_admitted_release", lambda: None)
    with pytest.raises(SystemExit, match="conjunction ab failed"):
        generator._capture_outputs()
    assert {path: path.read_bytes() for path in ARTIFACTS} == before
