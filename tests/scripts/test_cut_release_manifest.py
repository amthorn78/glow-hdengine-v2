from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from engine.serializer import canon
from scripts import cut_release_manifest as cutter


def _closed(monkeypatch) -> None:
    for name, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(name, value)


def test_release_cut_updates_only_manifest_and_reaches_read_only_fixed_point(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"new release bytes\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_bytes(
        canon.sercanon(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {
                        "path": "payload.txt",
                        "sha256": "0" * 64,
                        "size": 0,
                    }
                ],
            },
            sort_keys=True,
        )
    )

    assert cutter.cut_manifest(
        manifest,
        version="1.1.0",
        built_at_utc="2026-07-23T00:00:00Z",
    ) == 0
    payload = json.loads(manifest.read_bytes())
    assert set(payload) == {"root", "version", "built_at_utc", "files"}
    assert payload["version"] == "1.1.0"
    assert payload["built_at_utc"] == "2026-07-23T00:00:00Z"
    assert payload["files"] == [
        {
            "path": "payload.txt",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "size": len(source.read_bytes()),
        }
    ]
    before = {path.name for path in tmp_path.rglob("*") if path.is_file()}
    assert cutter.cut_manifest(
        manifest,
        version="1.1.0",
        built_at_utc="2026-07-23T00:00:00Z",
        check=True,
    ) == 0
    assert {path.name for path in tmp_path.rglob("*") if path.is_file()} == before


def test_release_cut_rejects_implicit_or_malformed_identity_inputs(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    manifest = tmp_path / "manifest.json"
    manifest.write_text("{}\n", encoding="utf-8")

    assert cutter.main(
        [
            "--manifest",
            str(manifest),
            "--version",
            "latest",
            "--built-at-utc",
            "now",
        ]
    ) == 1


def test_release_cut_accepts_full_semver_and_rejects_leading_zero(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [{"path": "payload.txt", "sha256": "0" * 64, "size": 0}],
    }
    manifest.write_bytes(canon.sercanon(payload, sort_keys=True))

    assert cutter.cut_manifest(
        manifest,
        version="1.2.3-rc.1+build.5",
        built_at_utc="2026-07-23T00:00:00Z",
    ) == 0
    with pytest.raises(ValueError, match="release_version_invalid"):
        cutter.cut_manifest(
            manifest,
            version="01.2.3",
            built_at_utc="2026-07-23T00:00:00Z",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("root", "release_manifest_root_invalid"),
        ("empty", "release_manifest_files_invalid"),
        ("extra", "release_manifest_entry_invalid"),
        ("duplicate", "release_manifest_entry_path_unsafe"),
        ("self", "release_manifest_entry_path_unsafe"),
        ("traversal", "release_manifest_entry_path_unsafe"),
    ),
)
def test_release_cut_rejects_manifest_roster_mutations(
    tmp_path,
    monkeypatch,
    mutation,
    message,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    entry = {"path": "payload.txt", "sha256": "0" * 64, "size": 0}
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [entry],
    }
    if mutation == "root":
        payload["root"] = "alternate/"
    elif mutation == "empty":
        payload["files"] = []
    elif mutation == "extra":
        entry["unknown"] = True
    elif mutation == "duplicate":
        payload["files"].append(dict(entry))
    elif mutation == "self":
        entry["path"] = "catalog/manifest.json"
    else:
        entry["path"] = "../outside"
    manifest.write_bytes(canon.sercanon(payload, sort_keys=True))

    with pytest.raises(ValueError, match=message):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )


def test_release_cut_rejects_noncanonical_input(tmp_path, monkeypatch):
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {"path": "payload.txt", "sha256": "0" * 64, "size": 0}
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="release_manifest_not_canonical"):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )


def test_release_cut_rejects_symlinked_source(tmp_path, monkeypatch):
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"payload\n")
    linked = tmp_path / "linked.txt"
    linked.symlink_to(source.name)
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_bytes(
        canon.sercanon(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {"path": "linked.txt", "sha256": "0" * 64, "size": 0}
                ],
            },
            sort_keys=True,
        )
    )

    with pytest.raises(ValueError, match="release_manifest_source_symlink"):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )
