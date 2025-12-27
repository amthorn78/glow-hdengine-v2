import hashlib
import json
import os
from pathlib import Path

from engine.serializer import canon
from scripts.release_id_recompute import recompute


def _set_closed_rails_env(monkeypatch) -> None:
    pins = {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }
    for key, value in pins.items():
        monkeypatch.setenv(key, value)


def _compute_manifest_digest(manifest_path: Path) -> tuple[bytes, str]:
    manifest_obj = json.loads(manifest_path.read_text(encoding="utf-8"))
    canonical_bytes = canon.sercanon(manifest_obj, sort_keys=True)
    return canonical_bytes, hashlib.sha256(canonical_bytes).hexdigest()


def test_recompute_rewrites_and_succeeds_after_fix(tmp_path, monkeypatch):
    _set_closed_rails_env(monkeypatch)
    manifest_path = Path("catalog/manifest.json")

    # Prepare stale artifacts in an isolated temp workspace.
    release_id_path = tmp_path / "release_id.txt"
    freeze_path = tmp_path / "freeze_pack_manifest.json"
    manifest_snapshot_path = tmp_path / "manifest_snapshot.json"
    checksums_path = tmp_path / "checksums_audit.log"
    env_pins_path = tmp_path / "env_pins.txt"
    log_path = tmp_path / "release_id_recompute.log"

    release_id_path.write_text("0" * 64 + "\n", encoding="utf-8")
    freeze_path.write_text("stale-freeze", encoding="utf-8")

    canonical_bytes, expected_release_id = _compute_manifest_digest(manifest_path)

    # --check should fail closed and preserve stale artifacts.
    exit_code_check = recompute(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=manifest_snapshot_path,
        checksums_path=checksums_path,
        env_pins_path=env_pins_path,
        log_path=log_path,
        check=True,
    )
    assert exit_code_check == 1
    assert freeze_path.read_text(encoding="utf-8") == "stale-freeze"
    assert release_id_path.read_text(encoding="utf-8").strip() == "0" * 64
    assert not manifest_snapshot_path.exists()
    assert not checksums_path.exists()

    # Non-check run should rewrite artifacts and exit success in the same invocation.
    exit_code_write = recompute(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=manifest_snapshot_path,
        checksums_path=checksums_path,
        env_pins_path=env_pins_path,
        log_path=log_path,
        check=False,
    )
    assert exit_code_write == 0
    assert freeze_path.read_bytes() == canonical_bytes
    assert release_id_path.read_text(encoding="utf-8").strip() == expected_release_id

    # A follow-up --check run should now be clean.
    exit_code_clean_check = recompute(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=manifest_snapshot_path,
        checksums_path=checksums_path,
        env_pins_path=env_pins_path,
        log_path=log_path,
        check=True,
    )
    assert exit_code_clean_check == 0
