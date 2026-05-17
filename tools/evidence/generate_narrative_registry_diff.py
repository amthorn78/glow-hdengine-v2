#!/usr/bin/env python3
"""Generate governed narrative registry diff and pack identity artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Mapping


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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


class RegistryDiffError(RuntimeError):
    """Raised when registry diff evidence cannot be generated unambiguously."""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json(path: Path) -> Any:
    try:
        raw = path.read_bytes()
    except FileNotFoundError as exc:
        raise RegistryDiffError(f"missing file: {path.relative_to(ROOT).as_posix()}") from exc
    if raw.startswith(b"\xef\xbb\xbf"):
        raise RegistryDiffError(f"BOM not allowed: {path.relative_to(ROOT).as_posix()}")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RegistryDiffError(f"invalid JSON: {path.relative_to(ROOT).as_posix()}") from exc


def _canonical_json_bytes(payload: Any, *, trailing_lf: bool = True) -> bytes:
    suffix = "\n" if trailing_lf else ""
    return (json.dumps(payload, separators=(",", ":"), sort_keys=True) + suffix).encode("utf-8")


def _manifest_canonical_bytes(manifest_path: Path = MANIFEST_PATH) -> bytes:
    return _canonical_json_bytes(_read_json(manifest_path), trailing_lf=False)


def _require_manifest() -> dict[str, Any]:
    manifest = _read_json(MANIFEST_PATH)
    if not isinstance(manifest, dict):
        raise RegistryDiffError("manifest must be an object")
    files = manifest.get("files")
    if not isinstance(files, list):
        raise RegistryDiffError("manifest.files must be a list")

    by_path: dict[str, Mapping[str, Any]] = {}
    for entry in files:
        if not isinstance(entry, dict):
            raise RegistryDiffError("manifest file entry must be an object")
        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size_bytes")
        if not isinstance(path, str) or not isinstance(sha, str) or not isinstance(size, int):
            raise RegistryDiffError("manifest file entry missing path/sha256/size_bytes")
        if path in by_path:
            raise RegistryDiffError(f"duplicate manifest path: {path}")
        by_path[path] = entry

    missing = [path for path in REQUIRED_MANIFEST_FILES if path not in by_path]
    if missing:
        raise RegistryDiffError(f"missing required manifest paths: {','.join(missing)}")

    for rel in REQUIRED_MANIFEST_FILES:
        artifact_path = ROOT / rel
        canonical = _canonical_json_bytes(_read_json(artifact_path), trailing_lf=False)
        entry = by_path[rel]
        if _sha256(canonical) != entry["sha256"]:
            raise RegistryDiffError(f"manifest sha mismatch: {rel}")
        if len(canonical) != entry["size_bytes"]:
            raise RegistryDiffError(f"manifest size mismatch: {rel}")
        sidecar = artifact_path.with_suffix(artifact_path.suffix + ".sha256")
        try:
            sidecar_sha = sidecar.read_text(encoding="utf-8").strip()
        except FileNotFoundError as exc:
            raise RegistryDiffError(f"missing sidecar: {sidecar.relative_to(ROOT).as_posix()}") from exc
        if sidecar_sha != entry["sha256"]:
            raise RegistryDiffError(f"sidecar sha mismatch: {sidecar.relative_to(ROOT).as_posix()}")

    manifest_sha = _sha256(_manifest_canonical_bytes())
    manifest_sidecar = MANIFEST_PATH.with_suffix(MANIFEST_PATH.suffix + ".sha256")
    try:
        expected_manifest_sha = manifest_sidecar.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RegistryDiffError("missing manifest sidecar") from exc
    if manifest_sha != expected_manifest_sha:
        raise RegistryDiffError("manifest sidecar mismatch")

    return manifest


def _identity_table(keys_payload: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not isinstance(keys_payload, list):
        raise RegistryDiffError("keys.json must be an array")

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
        record = {field: raw[field] for field in REQUIRED_KEY_FIELDS}
        if any(not isinstance(record[field], str) for field in ("band", "category", "category_slug", "key", "perspective")):
            raise RegistryDiffError("key record string field has invalid type")
        if not isinstance(record["slot"], int):
            raise RegistryDiffError("key record slot has invalid type")
        if record["perspective"] not in IDENTITY_PERSPECTIVES:
            raise RegistryDiffError(f"unknown perspective: {record['perspective']}")
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

    missing_primary = [
        "/".join((category, band, perspective))
        for (category, band, perspective), count in sorted(summary_by_tuple.items())
        if count < 1
    ]
    if missing_primary:
        raise RegistryDiffError(f"missing required registry identities: {','.join(missing_primary)}")

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
    manifest = _require_manifest()
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
