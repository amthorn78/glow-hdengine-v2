from __future__ import annotations

import shutil
import subprocess
import sys

import pytest

from tools.evidence import generate_epic032_pr01_router_evidence as generator


def _copy_frozen_outputs(tmp_path):
    for name in generator.FROZEN_OUTPUTS:
        source = generator.ROOT / name
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)


def test_frozen_epic032_router_outputs_verify_without_regeneration(tmp_path):
    _copy_frozen_outputs(tmp_path)

    generator._verify_frozen_outputs(tmp_path)


def test_frozen_epic032_router_output_drift_is_refused(tmp_path):
    _copy_frozen_outputs(tmp_path)
    drifted_name = next(iter(generator.FROZEN_OUTPUTS))
    (tmp_path / drifted_name).write_bytes(b"drift\n")

    with pytest.raises(
        SystemExit,
        match=f"^FROZEN_EPIC032_ROUTER_DRIFT:{drifted_name}$",
    ):
        generator._verify_frozen_outputs(tmp_path)


def test_historical_epic032_router_writer_is_refused():
    with pytest.raises(
        SystemExit,
        match="^HISTORICAL_EPIC032_ROUTER_WRITE_REFUSED$",
    ):
        generator.main([])


def test_historical_epic032_router_check_uses_frozen_verifier(monkeypatch):
    calls = []
    monkeypatch.setattr(generator, "ensure_determinism_env", lambda: calls.append("env"))
    monkeypatch.setattr(generator, "_verify_frozen_outputs", lambda: calls.append("verify"))

    assert generator.main(["--check"]) == 0
    assert calls == ["env", "verify"]


def test_release_identity_gate_preserves_frozen_historical_derivatives(monkeypatch):
    frozen = (
        generator.ROOT / "artifacts/math/freeze_pack_manifest.json",
        generator.ROOT / "artifacts/math/release_id.txt",
    )
    before = {path: path.read_bytes() for path in frozen}
    for key, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(key, value)

    result = subprocess.run(
        [sys.executable, "ci/checks/check_release_identity.sh"],
        cwd=generator.ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert {path: path.read_bytes() for path in frozen} == before
