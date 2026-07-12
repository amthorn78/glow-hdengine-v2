from __future__ import annotations

import hashlib
import json
from pathlib import Path

from engine.serializer import canon
from scripts import release_id_recompute


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


def test_release_check_mode_does_not_write(tmp_path, monkeypatch):
    source = tmp_path / "payload.txt"
    source.write_bytes(b"stable\n")
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
    log_path = tmp_path / "release.log"
    log_path.write_bytes(b"preserve-me\n")
    sidecar_path = log_path.with_suffix(log_path.suffix + ".sha256")
    sidecar_path.write_bytes(b"preserve-sidecar\n")

    monkeypatch.setattr(release_id_recompute, "require_closed_rails", lambda: None)
    before = {
        path: path.read_bytes()
        for path in (
            manifest_path,
            freeze_path,
            release_id_path,
            log_path,
            sidecar_path,
        )
    }

    rc = release_id_recompute.recompute(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=tmp_path / "snapshot.json",
        checksums_path=tmp_path / "checksums.log",
        env_pins_path=tmp_path / "env.txt",
        log_path=log_path,
        check=True,
    )

    assert rc == 0
    assert {path: path.read_bytes() for path in before} == before
