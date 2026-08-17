#!/usr/bin/env python3
"""Generate governed narrative registry diff and pack identity artifacts."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.narratives.constants import BANDS
from engine.runtime.determinism_env import ensure_determinism_env

CATALOG_ROOT = ROOT / "catalog" / "narratives"
MANIFEST_PATH = CATALOG_ROOT / "manifest.json"
KEYS_PATH = CATALOG_ROOT / "keys.json"
DIFF_PATH = ROOT / "audit" / "gates" / "narratives" / "registry.diff.json"
PACK_IDENTITY_PATH = ROOT / "audit" / "gates" / "narratives" / "pack_identity.txt"

REQUIRED_MANIFEST_FILES = (
    "catalog/narratives/keys.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
)
REQUIRED_KEY_FIELDS = ("band", "category", "category_slug", "key", "perspective", "slot")
IDENTITY_PERSPECTIVES = ("personal", "shared")
IDENTITY_SLOTS = (1, 2, 3)
PERSONAL_DIRECTIONS = ("a_to_b", "b_to_a")
SUPPRESSED_SHARED_CATEGORIES = frozenset(("balance", "drive"))
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_UTC_TIMESTAMP = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
)


class RegistryDiffError(RuntimeError):
    """Raised when registry diff evidence cannot be generated unambiguously."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _display_path(path: Path, *, repo_root: Path | None = None) -> str:
    active_root = repo_root or ROOT
    try:
        return path.relative_to(active_root).as_posix()
    except ValueError:
        return path.as_posix()


def _read_json(path: Path, *, repo_root: Path | None = None) -> Any:
    try:
        raw = path.read_bytes()
    except FileNotFoundError as exc:
        raise RegistryDiffError(f"missing file: {_display_path(path, repo_root=repo_root)}") from exc
    if raw.startswith(b"\xef\xbb\xbf"):
        raise RegistryDiffError(f"BOM not allowed: {_display_path(path, repo_root=repo_root)}")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RegistryDiffError(f"invalid JSON: {_display_path(path, repo_root=repo_root)}") from exc


def _canonical_json_bytes(payload: Any, *, trailing_lf: bool = True) -> bytes:
    suffix = "\n" if trailing_lf else ""
    return (json.dumps(payload, separators=(",", ":"), sort_keys=True) + suffix).encode("utf-8")


def _manifest_canonical_bytes(
    manifest_path: Path | None = None, *, repo_root: Path | None = None
) -> bytes:
    active_manifest_path = manifest_path or MANIFEST_PATH
    return _canonical_json_bytes(
        _read_json(active_manifest_path, repo_root=repo_root), trailing_lf=False
    )


def _require_manifest(
    catalog_root: Path | None = None, *, repo_root: Path | None = None
) -> dict[str, Any]:
    active_catalog_root = catalog_root or CATALOG_ROOT
    active_repo_root = repo_root or ROOT
    manifest_path = active_catalog_root / "manifest.json"
    manifest = _read_json(manifest_path, repo_root=repo_root)
    if not isinstance(manifest, dict):
        raise RegistryDiffError("manifest must be an object")
    if set(manifest) != {"created_utc", "files", "pack_name"}:
        raise RegistryDiffError("manifest fields invalid")
    if manifest["pack_name"] != "narratives_v1":
        raise RegistryDiffError("manifest pack_name must be narratives_v1")
    created_utc = manifest["created_utc"]
    if not isinstance(created_utc, str) or _UTC_TIMESTAMP.fullmatch(created_utc) is None:
        raise RegistryDiffError("manifest created_utc invalid")
    try:
        dt.datetime.strptime(created_utc, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise RegistryDiffError("manifest created_utc invalid") from exc
    files = manifest.get("files")
    if not isinstance(files, list):
        raise RegistryDiffError("manifest.files must be a list")

    by_path: dict[str, Mapping[str, Any]] = {}
    for entry in files:
        if not isinstance(entry, dict):
            raise RegistryDiffError("manifest file entry must be an object")
        if set(entry) != {"path", "sha256", "size_bytes"}:
            raise RegistryDiffError("manifest file entry fields invalid")
        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size_bytes")
        if (
            not isinstance(path, str)
            or not isinstance(sha, str)
            or _HEX64.fullmatch(sha) is None
            or type(size) is not int
            or size < 0
        ):
            raise RegistryDiffError("manifest file entry missing path/sha256/size_bytes")
        if path in by_path:
            raise RegistryDiffError(f"duplicate manifest path: {path}")
        by_path[path] = entry

    expected_paths = set(REQUIRED_MANIFEST_FILES)
    actual_paths = set(by_path)
    missing = sorted(expected_paths - actual_paths)
    if missing:
        raise RegistryDiffError(f"missing required manifest paths: {','.join(missing)}")
    extra = sorted(actual_paths - expected_paths)
    if extra:
        raise RegistryDiffError(f"unexpected manifest paths: {','.join(extra)}")
    if tuple(by_path) != REQUIRED_MANIFEST_FILES:
        raise RegistryDiffError("manifest paths must match required ASCII order")

    for rel in sorted(actual_paths):
        artifact_path = active_repo_root / rel
        canonical = _canonical_json_bytes(
            _read_json(artifact_path, repo_root=repo_root), trailing_lf=False
        )
        entry = by_path[rel]
        if _sha256(canonical) != entry["sha256"]:
            raise RegistryDiffError(f"manifest sha mismatch: {rel}")
        if len(canonical) != entry["size_bytes"]:
            raise RegistryDiffError(f"manifest size mismatch: {rel}")
        sidecar = artifact_path.with_suffix(artifact_path.suffix + ".sha256")
        try:
            sidecar_sha = sidecar.read_text(encoding="utf-8").strip()
        except FileNotFoundError as exc:
            raise RegistryDiffError(
                f"missing sidecar: {_display_path(sidecar, repo_root=repo_root)}"
            ) from exc
        if sidecar_sha != entry["sha256"]:
            raise RegistryDiffError(
                f"sidecar sha mismatch: {_display_path(sidecar, repo_root=repo_root)}"
            )

    manifest_sha = _sha256(
        _manifest_canonical_bytes(manifest_path, repo_root=repo_root)
    )
    manifest_sidecar = manifest_path.with_suffix(manifest_path.suffix + ".sha256")
    try:
        expected_manifest_sha = manifest_sidecar.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RegistryDiffError("missing manifest sidecar") from exc
    if manifest_sha != expected_manifest_sha:
        raise RegistryDiffError("manifest sidecar mismatch")

    return manifest


def validate_registry_snapshot(
    catalog_root: Path | None = None, *, repo_root: Path | None = None
) -> dict[str, Any]:
    """Validate one coherent narrative snapshot without producing evidence."""

    active_catalog_root = catalog_root or CATALOG_ROOT
    manifest = _require_manifest(active_catalog_root, repo_root=repo_root)
    identity_records, _summary = _identity_table(
        _read_json(active_catalog_root / "keys.json", repo_root=repo_root)
    )

    key_values = {record["key"] for record in identity_records}
    templates = _read_json(
        active_catalog_root / "templates.json", repo_root=repo_root
    )
    if not isinstance(templates, dict):
        raise RegistryDiffError("templates.json must be an object")
    if set(templates) != key_values:
        raise RegistryDiffError("templates.json keys must exactly match keys.json")
    if any(not isinstance(value, str) or not value for value in templates.values()):
        raise RegistryDiffError("template values must be nonempty strings")

    palettes = _read_json(
        active_catalog_root / "palettes.json", repo_root=repo_root
    )
    if palettes != {"palettes": {"default": {"style": "plain"}}}:
        raise RegistryDiffError("palettes.json must contain the governed default palette")

    suppression_map = _read_json(
        active_catalog_root / "suppression_map.json", repo_root=repo_root
    )
    if not isinstance(suppression_map, dict):
        raise RegistryDiffError("suppression_map.json must be an object")
    expected_suppressions = {
        record["key"]
        for record in identity_records
        if record["perspective"] == "personal"
        or (
            record["perspective"] == "shared"
            and record["category_slug"] in SUPPRESSED_SHARED_CATEGORIES
        )
    }
    if set(suppression_map) != expected_suppressions:
        raise RegistryDiffError(
            "suppression_map.json keys must match the governed suppression policy"
        )
    for key, policy in suppression_map.items():
        if not isinstance(policy, dict) or set(policy) != {"notes", "policy_reason"}:
            raise RegistryDiffError(f"invalid suppression policy shape: {key}")
        if policy["policy_reason"] != "duplicate":
            raise RegistryDiffError(f"invalid suppression policy reason: {key}")
        notes = policy["notes"]
        if not isinstance(notes, str) or not notes.startswith("Duplicate narrative from "):
            raise RegistryDiffError(f"invalid suppression policy notes: {key}")
    return manifest


def _identity_table(keys_payload: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not isinstance(keys_payload, list):
        raise RegistryDiffError("keys.json must be an array")

    allowed_categories = set(CATEGORIES_ORDER_V1)
    allowed_bands = set(BANDS)
    allowed_perspectives = set(IDENTITY_PERSPECTIVES)
    expected_tuples = {
        (category, band, perspective, slot)
        for category in CATEGORIES_ORDER_V1
        for band in BANDS
        for perspective in IDENTITY_PERSPECTIVES
        for slot in IDENTITY_SLOTS
    }

    tuples: set[tuple[str, str, str, int]] = set()
    key_values: set[str] = set()
    summary_by_tuple: Counter[tuple[str, str, str]] = Counter()
    summary_by_category: Counter[str] = Counter()
    summary_by_perspective: Counter[str] = Counter()
    records: list[dict[str, Any]] = []

    for raw in keys_payload:
        if not isinstance(raw, dict):
            raise RegistryDiffError("key record must be an object")
        missing = [field for field in REQUIRED_KEY_FIELDS if field not in raw]
        if missing:
            raise RegistryDiffError(f"key record missing fields: {','.join(missing)}")
        expected_fields = set(REQUIRED_KEY_FIELDS)
        if raw["perspective"] == "personal":
            expected_fields.add("directions")
        if set(raw) != expected_fields:
            raise RegistryDiffError("key record fields do not match its perspective")
        if raw["perspective"] == "personal" and raw["directions"] != list(
            PERSONAL_DIRECTIONS
        ):
            raise RegistryDiffError(
                "personal key directions must be a_to_b then b_to_a"
            )
        record = {field: raw[field] for field in REQUIRED_KEY_FIELDS}
        if any(not isinstance(record[field], str) for field in ("band", "category", "category_slug", "key", "perspective")):
            raise RegistryDiffError("key record string field has invalid type")
        if type(record["slot"]) is not int:
            raise RegistryDiffError("key record slot has invalid type")
        if record["category_slug"] not in allowed_categories:
            raise RegistryDiffError(f"unknown category_slug: {record['category_slug']}")
        if record["category"] != record["category_slug"]:
            raise RegistryDiffError(f"category/category_slug mismatch: {record['key']}")
        if record["band"] not in allowed_bands:
            raise RegistryDiffError(f"unknown band: {record['band']}")
        if record["perspective"] not in allowed_perspectives:
            raise RegistryDiffError(f"unknown perspective: {record['perspective']}")
        if record["slot"] not in IDENTITY_SLOTS:
            raise RegistryDiffError(f"unknown slot: {record['slot']}")
        expected_key = ".".join(
            (
                record["category_slug"],
                record["band"].lower(),
                record["perspective"],
                str(record["slot"]),
            )
        )
        if record["key"] != expected_key:
            raise RegistryDiffError(
                f"key/source identity mismatch: {record['key']}"
            )
        tuple_key = (record["category_slug"], record["band"], record["perspective"], record["slot"])
        if tuple_key in tuples:
            raise RegistryDiffError("duplicate category/band/perspective/slot tuple")
        tuples.add(tuple_key)
        if record["key"] in key_values:
            raise RegistryDiffError(f"duplicate key: {record['key']}")
        key_values.add(record["key"])
        summary_by_tuple[(record["category_slug"], record["band"], record["perspective"])] += 1
        summary_by_category[record["category_slug"]] += 1
        summary_by_perspective[record["perspective"]] += 1
        records.append(record)

    missing_tuples = sorted(expected_tuples - tuples)
    if missing_tuples:
        missing = [
            "/".join((category, band, perspective, str(slot)))
            for category, band, perspective, slot in missing_tuples
        ]
        raise RegistryDiffError(f"missing required registry identities: {','.join(missing)}")
    extra_tuples = sorted(tuples - expected_tuples)
    if extra_tuples:
        extra = [
            "/".join((category, band, perspective, str(slot)))
            for category, band, perspective, slot in extra_tuples
        ]
        raise RegistryDiffError(f"unexpected registry identities: {','.join(extra)}")

    records.sort(key=lambda row: (row["category_slug"], row["band"], row["perspective"], row["slot"], row["key"]))
    summary = {
        "category_count": len(summary_by_category),
        "key_count": len(records),
        "keys_sha256": _sha256(_canonical_json_bytes(records, trailing_lf=False)),
        "perspectives": dict(sorted(summary_by_perspective.items())),
        "tuple_count": len(summary_by_tuple),
    }
    return records, summary


def build_artifacts() -> tuple[dict[str, Any], str]:
    manifest = validate_registry_snapshot()
    _identity_records, registry_summary = _identity_table(_read_json(KEYS_PATH))
    manifest_bytes_a = _manifest_canonical_bytes()
    manifest_bytes_b = _manifest_canonical_bytes()
    pack_sha_a = _sha256(manifest_bytes_a)
    pack_sha_b = _sha256(manifest_bytes_b)
    if manifest_bytes_a != manifest_bytes_b or pack_sha_a != pack_sha_b:
        raise RegistryDiffError("two-run pack identity mismatch")

    manifest_files = [
        {
            "path": entry["path"],
            "sha256": entry["sha256"],
            "size_bytes": entry["size_bytes"],
        }
        for entry in manifest["files"]
    ]
    manifest_files.sort(key=lambda row: row["path"])

    diff_payload: dict[str, Any] = {
        "diff": {
            "added": [],
            "changed": [],
            "removed": [],
            "status": "no_prior_baseline_current_manifest_verified",
        },
        "epic_id": "HDE-EPIC032",
        "identity": {
            "manifest_canonical_sha256": pack_sha_a,
            "manifest_path": "catalog/narratives/manifest.json",
            "pack_sha": pack_sha_a,
            "two_run_identity": {
                "first": pack_sha_a,
                "match": True,
                "second": pack_sha_b,
            },
        },
        "manifest_files": manifest_files,
        "registry_summary": registry_summary,
        "schema_version": "1.0",
        "scope": "HDE-FERM003.2",
    }

    identity_lines = [
        f"pack_sha={pack_sha_a}",
        f"manifest_canonical_sha256={pack_sha_a}",
        "manifest_path=catalog/narratives/manifest.json",
        f"manifest_canonical_size={len(manifest_bytes_a)}",
        f"two_run_first={pack_sha_a}",
        f"two_run_second={pack_sha_b}",
        "two_run_match=true",
    ]
    for entry in manifest_files:
        identity_lines.append(f"{entry['path']} sha256={entry['sha256']} size={entry['size_bytes']}")
    return diff_payload, "\n".join(identity_lines) + "\n"


def write_artifacts(*, check: bool = False) -> None:
    diff_payload, identity_text = build_artifacts()
    diff_bytes = _canonical_json_bytes(diff_payload, trailing_lf=True)
    targets = ((DIFF_PATH, diff_bytes), (PACK_IDENTITY_PATH, identity_text.encode("utf-8")))
    for path, data in targets:
        if path.exists() and path.read_bytes() == data:
            continue
        if check:
            raise SystemExit(f"STALE:{path.relative_to(ROOT).as_posix()}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate narrative registry diff and pack identity evidence")
    parser.add_argument("--check", action="store_true", help="Fail if artifacts would change")
    args = parser.parse_args(argv)
    ensure_determinism_env()
    write_artifacts(check=args.check)


if __name__ == "__main__":
    main()
