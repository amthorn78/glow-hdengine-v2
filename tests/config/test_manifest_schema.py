import json
from pathlib import Path

import pytest

from engine.config.registry_loader import DuplicateIdError, SchemaValidationError, load_manifest


def _write_manifest(tmp_path: Path, payload: dict) -> Path:
    catalog_dir = tmp_path / "catalog"
    catalog_dir.mkdir(exist_ok=True)
    manifest_path = catalog_dir / "manifest.json"
    manifest_path.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    return tmp_path


def test_manifest_requires_closed_keys_and_root(tmp_path: Path) -> None:
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-01-01T00:00:00Z",
        "files": [],
    }
    root = _write_manifest(tmp_path, payload)
    assert load_manifest(root).root == "catalog/"

    payload_extra = dict(payload, extra="x")
    root_extra = _write_manifest(tmp_path, payload_extra)
    with pytest.raises(SchemaValidationError):
        load_manifest(root_extra)

    payload_bad_root = dict(payload, root="bad/")
    root_bad = _write_manifest(tmp_path, payload_bad_root)
    with pytest.raises(SchemaValidationError):
        load_manifest(root_bad)


def test_manifest_requires_sorted_deduped_files(tmp_path: Path) -> None:
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-01-01T00:00:00Z",
        "files": [
            {"path": "b.json", "sha256": "0" * 64, "size": 1},
            {"path": "a.json", "sha256": "0" * 64, "size": 1},
        ],
    }
    root = _write_manifest(tmp_path, payload)
    with pytest.raises(SchemaValidationError):
        load_manifest(root)

    payload_dup = dict(payload)
    payload_dup["files"] = [{"path": "a.json", "sha256": "0" * 64, "size": 1}, {"path": "a.json", "sha256": "0" * 64, "size": 1}]
    root_dup = _write_manifest(tmp_path, payload_dup)
    with pytest.raises(DuplicateIdError):
        load_manifest(root_dup)


def test_manifest_forbids_self_listing(tmp_path: Path) -> None:
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-01-01T00:00:00Z",
        "files": [{"path": "catalog/manifest.json", "sha256": "0" * 64, "size": 1}],
    }
    root = _write_manifest(tmp_path, payload)
    with pytest.raises(SchemaValidationError):
        load_manifest(root)
