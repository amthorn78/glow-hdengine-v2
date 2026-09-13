import json
from pathlib import Path

import pytest

from engine.config.registry_loader import DuplicateIdError, SchemaValidationError, load_manifest
from tests.config.helpers import write_canonical


def _write_manifest(tmp_path: Path, payload: dict) -> Path:
    catalog_dir = tmp_path / "catalog"
    catalog_dir.mkdir(exist_ok=True)
    manifest_path = catalog_dir / "manifest.json"
    write_canonical(manifest_path, payload)
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


@pytest.mark.parametrize("size", [True, False, 1.0, "1", -1])
def test_manifest_size_has_exact_integer_domain(tmp_path: Path, size: object) -> None:
    payload = {"root": "catalog/", "version": "1.0.0", "built_at_utc": "2025-01-01T00:00:00Z",
               "files": [{"path": "a.json", "sha256": "0" * 64, "size": size}]}
    with pytest.raises(SchemaValidationError, match="size"):
        load_manifest(_write_manifest(tmp_path, payload))


@pytest.mark.parametrize("path", ["../a.json", "/a.json", "a/../b.json", "a//b.json", "a\\b.json"])
def test_manifest_structure_refuses_unsafe_lexical_paths(tmp_path: Path, path: str) -> None:
    payload = {"root": "catalog/", "version": "1.0.0", "built_at_utc": "2025-01-01T00:00:00Z",
               "files": [{"path": path, "sha256": "0" * 64, "size": 1}]}
    with pytest.raises(SchemaValidationError) as error:
        load_manifest(_write_manifest(tmp_path, payload))
    assert error.value.code == "INVALID_MANIFEST_PATH"


@pytest.mark.parametrize("version", [None, "", 1, True, []])
def test_generic_manifest_version_is_a_nonempty_string(tmp_path: Path, version: object) -> None:
    payload = {"root": "catalog/", "version": version, "built_at_utc": "2025-01-01T00:00:00Z", "files": []}
    with pytest.raises(SchemaValidationError) as caught:
        load_manifest(_write_manifest(tmp_path, payload))
    assert caught.value.code == "INVALID_MANIFEST_VERSION"


@pytest.mark.parametrize(
    "timestamp",
    ["", "2025-01-01", "2025-01-01T00:00:00+00:00", "2025-02-29T00:00:00Z", 1],
)
def test_manifest_timestamp_is_an_exact_valid_utc_value(tmp_path: Path, timestamp: object) -> None:
    payload = {"root": "catalog/", "version": "1.0.0", "built_at_utc": timestamp, "files": []}
    with pytest.raises(SchemaValidationError) as caught:
        load_manifest(_write_manifest(tmp_path, payload))
    assert caught.value.code == "INVALID_MANIFEST_TIMESTAMP"


@pytest.mark.parametrize("sha", ["0" * 63, "0" * 65, "A" * 64, "g" * 64, 0, None])
def test_manifest_digest_is_exact_lowercase_sha256(tmp_path: Path, sha: object) -> None:
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-01-01T00:00:00Z",
        "files": [{"path": "a.json", "sha256": sha, "size": 1}],
    }
    with pytest.raises(SchemaValidationError) as caught:
        load_manifest(_write_manifest(tmp_path, payload))
    assert caught.value.code == "INVALID_MANIFEST"


def test_manifest_entry_keys_are_closed(tmp_path: Path) -> None:
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-01-01T00:00:00Z",
        "files": [{"path": "a.json", "sha256": "0" * 64, "size": 1, "extra": True}],
    }
    with pytest.raises(SchemaValidationError) as caught:
        load_manifest(_write_manifest(tmp_path, payload))
    assert caught.value.code == "INVALID_MANIFEST"


def test_generic_manifest_shape_does_not_claim_full_release_admission() -> None:
    root = Path(__file__).resolve().parents[2]
    manifest = load_manifest(root)
    assert manifest.version == "1.0.0"
    assert len(manifest.files) == 15
    assert all(row.path != "catalog/manifest.json" for row in manifest.files)
