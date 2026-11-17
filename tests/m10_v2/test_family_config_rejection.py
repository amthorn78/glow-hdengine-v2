"""HDE-EPIC043 WU-PR-04: the v2 proof family, configuration and manifest-row rejection (HDE-DIST008.1).

Items F-09 (configuration-mutation rejection under the v2 loader rules: a missing
center, class, weight, profile or line, and an unknown aura-class or pair-rule
name) and F-21 (manifest and release-binding rejection, the manifest-row part the
v2 loader enforces).

Every case admits or refuses through ``load_magic10_v2_bundle_from_root`` in a
temporary root assembled as ``conftest.py`` assembles it: the repository's
``catalog/``, ``math/`` and ``schemas/`` bytes with the labelled non-canon
fixtures. A changed input is re-bound in the configuration's ``sources`` and the
manifest row, so each case reaches the rule it names. Each item has a check
function that raises ``AssertionError`` when a rejection disappears; the refused
mutation disables one loader rule in-process. Nothing is written under the
repository's own tree.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from engine.config import magic10_v2_loader as v2
from engine.config.registry_loader import ManifestEntry, SchemaValidationError
from engine.serializer.canon import sercanon

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "magic10_v2"
CONFIG = "catalog/magic10_mechanics_v2.json"
V1_CONFIG = "catalog/magic10_mechanics_v1.json"
CENTERS = "catalog/centers_v1.json"
TYPE_PAIRING = "catalog/type_pairing_v1.json"
THRESHOLDS = "math/thresholds.json"


def _row(root: Path, path: str = CONFIG) -> ManifestEntry:
    raw = (root / path).read_bytes()
    return ManifestEntry(path, hashlib.sha256(raw).hexdigest(), len(raw))


def _root(base: Path, path: str | None = None, change=None, *, rebind: bool = True) -> Path:
    root = base / "root"
    for directory in ("catalog", "math", "schemas"):
        shutil.copytree(ROOT / directory, root / directory)
    shutil.copyfile(FIXTURES / "thresholds_v2.fixture.json", root / THRESHOLDS)
    shutil.copyfile(FIXTURES / "magic10_mechanics_v2.fixture.json", root / CONFIG)
    if path is not None:
        document = json.loads((root / path).read_bytes())
        change(document)
        (root / path).write_bytes(sercanon(document, sort_keys=True))
        if rebind and path != CONFIG:
            configuration = json.loads((root / CONFIG).read_bytes())
            for source in configuration["sources"].values():
                if source["path"] == path:
                    source["sha256"] = hashlib.sha256((root / path).read_bytes()).hexdigest()
            (root / CONFIG).write_bytes(sercanon(configuration, sort_keys=True))
    return root


def _refusal(root: Path, rows) -> str | None:
    try:
        v2.load_magic10_v2_bundle_from_root(root, rows)
    except SchemaValidationError as exc:
        return exc.code
    except Exception as exc:  # a crash is not the named refusal; the check reports it
        return f"UNEXPECTED:{type(exc).__name__}"
    return None


# --- F-09 -------------------------------------------------------------------------------------

def _drop_weight(document: dict) -> None:
    document["center_map"][0]["weights"].pop("g")


REJECTIONS = {
    "missing-center": (CENTERS, lambda d: d["centers"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "missing-class": (TYPE_PAIRING, lambda d: d["aura_classes"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "missing-weight": (CONFIG, _drop_weight, "M10V2_PINNED_CONTENT_MISMATCH"),
    "missing-profile": (CONFIG, lambda d: d["profiles"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "missing-center-profile": (CONFIG, lambda d: d["center_profiles"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "missing-line": (CONFIG, lambda d: d["signals"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "unknown-aura-class": (TYPE_PAIRING, lambda d: d["aura_classes"].__setitem__(3, "observer"), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "unknown-pair-rule": (TYPE_PAIRING, lambda d: d["rules"][0].__setitem__("rule_id", "same_kind"), "M10V2_SCHEMA_VALIDATION_FAILED"),
}


def _check_f09(tmp_path: Path) -> None:
    admitted = _root(tmp_path / "admitted")
    assert _refusal(admitted, (_row(admitted),)) is None
    for name, (path, change, code) in REJECTIONS.items():
        root = _root(tmp_path / name, path, change)
        assert _refusal(root, (_row(root),)) == code, name


def test_f09_configuration_mutation_rejection(tmp_path) -> None:
    _check_f09(tmp_path)


def test_f09_mutation_owning_schema_not_applied_is_refused(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(v2, "_validate_v2_instance", lambda capture, data_path, data: None)
    with pytest.raises(AssertionError):
        _check_f09(tmp_path)


# --- F-21 -------------------------------------------------------------------------------------

def _check_f21(tmp_path: Path) -> None:
    root = _root(tmp_path / "rows")
    row = _row(root)
    v1_row = ManifestEntry(V1_CONFIG, "0" * 64, 1)
    cases = {
        "not-a-manifest-entry": ([(row.path, row.sha256, row.size)], "M10V2_INVALID_MANIFEST_ROWS"),
        "duplicate-paths": ((row, row), "M10V2_INVALID_MANIFEST_ROWS"),
        "unsorted-paths": ((ManifestEntry("math/thresholds.json", "0" * 64, 1), row), "M10V2_INVALID_MANIFEST_ROWS"),
        "no-configuration-row": ((), "M10V2_CONFIGURATION_ROW_MISSING"),
        "two-configurations": ((v1_row, row), "M10V2_MULTIPLE_CONFIGURATIONS"),
        "digest-does-not-bind": ((ManifestEntry(CONFIG, "0" * 64, row.size),), "M10V2_MANIFEST_HASH_MISMATCH"),
        "size-does-not-bind": ((ManifestEntry(CONFIG, row.sha256, row.size + 1),), "M10V2_MANIFEST_SIZE_MISMATCH"),
    }
    for name, (rows, code) in cases.items():
        assert _refusal(root, rows) == code, name
    unbound = _root(tmp_path / "unbound", THRESHOLDS, lambda d: d["categories"].reverse(), rebind=False)
    assert _refusal(unbound, (_row(unbound),)) == "M10V2_SOURCE_MISMATCH"


def test_f21_manifest_row_rejection(tmp_path) -> None:
    _check_f21(tmp_path)


def test_f21_mutation_unchecked_manifest_rows_is_refused(tmp_path, monkeypatch) -> None:
    def first_row(manifest_rows):
        return list(manifest_rows)[0] if manifest_rows else ManifestEntry(CONFIG, "0" * 64, 1)

    monkeypatch.setattr(v2, "_check_manifest_rows", first_row)
    with pytest.raises(AssertionError):
        _check_f21(tmp_path)
