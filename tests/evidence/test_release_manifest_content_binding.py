from __future__ import annotations

import hashlib
import json
from pathlib import Path

from engine.serializer import canon
from scripts import release_id_recompute
from tools.evidence import regenerate_identity_closure


def _manifest_bytes(path: str, body: bytes) -> bytes:
    return canon.sercanon(
        {
            "built_at_utc": "2025-12-26T00:00:00Z",
            "files": [
                {
                    "path": path,
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "size": len(body),
                }
            ],
            "root": "catalog/",
            "version": "1.0.0",
        },
        sort_keys=True,
    )


def test_release_evaluation_rejects_manifest_entries_that_do_not_match_disk(
    tmp_path,
):
    source = tmp_path / "payload.txt"
    source.write_bytes(b"first\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest_path = catalog / "manifest.json"
    manifest_bytes = _manifest_bytes("payload.txt", source.read_bytes())
    manifest_path.write_bytes(manifest_bytes)

    freeze_path = tmp_path / "freeze.json"
    freeze_path.write_bytes(manifest_bytes)
    release_id_path = tmp_path / "release_id.txt"
    release_id_path.write_text(
        hashlib.sha256(manifest_bytes).hexdigest() + "\n",
        encoding="utf-8",
    )

    initial = release_id_recompute._evaluate_state(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
    )
    assert initial.problems == []

    source.write_bytes(b"drifted\n")
    drifted = release_id_recompute._evaluate_state(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
    )
    assert any(
        problem.startswith("manifest_file_audit:BAD payload.txt")
        for problem in drifted.problems
    )


def test_refresh_manifest_entries_rebinds_hash_and_size(tmp_path):
    source = tmp_path / "payload.txt"
    source.write_bytes(b"current\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest_path = catalog / "manifest.json"
    manifest_path.write_bytes(_manifest_bytes("payload.txt", b"stale\n"))

    release_id_recompute._refresh_manifest_entries(manifest_path)

    payload = json.loads(manifest_path.read_bytes())
    entry = payload["files"][0]
    assert entry["sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert entry["size"] == len(source.read_bytes())


def test_committed_release_manifest_entries_match_repository_bytes():
    payload = json.loads(Path("catalog/manifest.json").read_bytes())
    for entry in payload["files"]:
        source = Path(entry["path"])
        body = source.read_bytes()
        assert entry["sha256"] == hashlib.sha256(body).hexdigest()
        assert entry["size"] == len(body)


def test_release_check_mode_validates_outputs_without_writing(
    tmp_path,
    monkeypatch,
):
    source = tmp_path / "payload.txt"
    source.write_bytes(b"stable\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest_path = catalog / "manifest.json"
    manifest_path.write_bytes(_manifest_bytes("payload.txt", source.read_bytes()))

    freeze_path = tmp_path / "freeze.json"
    release_id_path = tmp_path / "release_id.txt"
    snapshot_path = tmp_path / "snapshot.json"
    checksums_path = tmp_path / "checksums.log"
    env_pins_path = tmp_path / "env.txt"
    log_path = tmp_path / "release.log"

    monkeypatch.setattr(release_id_recompute, "require_closed_rails", lambda: None)
    kwargs = {
        "manifest_path": manifest_path,
        "freeze_path": freeze_path,
        "release_id_path": release_id_path,
        "manifest_snapshot_path": snapshot_path,
        "checksums_path": checksums_path,
        "env_pins_path": env_pins_path,
        "log_path": log_path,
    }
    assert release_id_recompute.recompute(**kwargs) == 0

    governed_paths = (
        manifest_path,
        freeze_path,
        freeze_path.with_suffix(freeze_path.suffix + ".sha256"),
        release_id_path,
        release_id_path.with_suffix(release_id_path.suffix + ".sha256"),
        snapshot_path,
        checksums_path,
        env_pins_path,
        log_path,
        log_path.with_suffix(log_path.suffix + ".sha256"),
    )
    before = {path: path.read_bytes() for path in governed_paths}

    assert release_id_recompute.recompute(**kwargs, check=True) == 0
    assert {path: path.read_bytes() for path in governed_paths} == before

    log_path.write_bytes(b"stale\n")
    stale_before = {path: path.read_bytes() for path in governed_paths}
    assert release_id_recompute.recompute(**kwargs, check=True) == 1
    assert {path: path.read_bytes() for path in governed_paths} == stale_before


def test_closure_write_regenerates_env_matrix(monkeypatch):
    calls: list[tuple[str, ...]] = []
    monkeypatch.setattr(
        regenerate_identity_closure,
        "_run",
        lambda *args, **kwargs: calls.append(args),
    )
    monkeypatch.setattr(
        regenerate_identity_closure,
        "_is_current",
        lambda *args, **kwargs: False,
    )
    monkeypatch.setattr(
        regenerate_identity_closure,
        "_refresh_cut_time_identity",
        lambda: None,
    )

    regenerate_identity_closure._write_closure()

    env_matrix_call = ("tools/evidence/generate_env_matrix_snapshot.py",)
    assert env_matrix_call in calls
    assert calls.index(env_matrix_call) < calls.index(
        ("tools/evidence/update_evidence_index.py",)
    )


def test_closure_roster_covers_release_dependent_local_derivatives():
    writes = {step.write for step in regenerate_identity_closure.CLOSURE_STEPS}
    checks = {step.check for step in regenerate_identity_closure.CLOSURE_STEPS}
    expected_writes = {
        ("tools/config/generate_config_artifacts.py",),
        ("tools/config/generate_bundles.py",),
        ("tools/evidence/generate_determinism_gate_proofs.py",),
        ("tools/evidence/generate_open_rails_abba_proof.py",),
        ("tools/evidence/generate_a7_transport_proofs.py",),
        ("tools/evidence/generate_architecture_snapshot.py",),
        ("tools/evidence/generate_v2_mapped_cache_evidence.py",),
        ("tools/evidence/update_evidence_index.py",),
        ("tools/evidence/orientation_demo.py",),
    }
    assert expected_writes <= writes
    for write in expected_writes:
        step = next(item for item in regenerate_identity_closure.CLOSURE_STEPS if item.write == write)
        assert step.check in checks
        assert step.check[-1] in {"--check", "--check-only"}


def test_closure_write_skips_current_producers(monkeypatch):
    calls: list[tuple[str, ...]] = []
    monkeypatch.setattr(regenerate_identity_closure, "_is_current", lambda *args, **kwargs: True)
    monkeypatch.setattr(regenerate_identity_closure, "_run", lambda *args, **kwargs: calls.append(args))
    monkeypatch.setattr(regenerate_identity_closure, "_refresh_cut_time_identity", lambda: None)

    regenerate_identity_closure._write_closure()

    assert calls == [("scripts/release_id_recompute.py", "--check")]


def test_cut_time_release_refresh_updates_only_release_field():
    old_release = "1" * 64
    new_release = "2" * 64
    source = (
        '_CUT_TIME_IDENTITY = {\n'
        '    "engine_tag": "hdengine@prod",\n'
        f'    "release_id": "{old_release}",\n'
        '}\n'
    )

    updated = regenerate_identity_closure._replace_cut_time_release_id(
        source,
        new_release,
    )

    assert f'"release_id": "{new_release}"' in updated
    assert "hdengine@prod" in updated
    assert old_release not in updated
