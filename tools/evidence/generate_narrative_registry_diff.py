#!/usr/bin/env python3
"""Build the PF17 pack and verify frozen EPIC032 registry evidence."""

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
from engine.narratives.lints import run_all as run_narrative_lints
from engine.runtime.determinism_env import ensure_determinism_env

CATALOG_ROOT = ROOT / "catalog" / "narratives"
MANIFEST_PATH = CATALOG_ROOT / "manifest.json"
PF18_SOURCE_PATH = (
    ROOT
    / "docs"
    / "pfcanon"
    / "PF18-Reference-HDE-Narrative Deliverables v0.7.md"
)

REQUIRED_MANIFEST_FILES = (
    "catalog/narratives/keys.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
)
REQUIRED_KEY_FIELDS = ("band", "category", "category_slug", "key", "perspective", "slot")
IDENTITY_PERSPECTIVES = ("a_to_b", "b_to_a", "shared")
IDENTITY_SLOTS = (1, 2, 3)
PF18_SOURCE_SHA256 = "ec501b3b42c9f5321d295bd1b56659435f17c21bf73c847c6af4e207a2a3150b"
PF18_SOURCE_OCCURRENCES = 384
PF18_UNIQUE_CANDIDATES = 360
PF18_DUPLICATE_OCCURRENCES = 24
PACK_CREATED_UTC = "2025-11-11T02:28:46Z"
SUPPRESSED_SOURCE_CANDIDATES: Mapping[str, Mapping[str, str]] = {
    "nar.balance.glow.a_to_b.2.fair-01": {
        "notes": "PF15 forbidden token: blame",
        "policy_reason": "conflict",
    },
    "nar.balance.glow.shared.2.fair-01": {
        "notes": "PF15 forbidden token: blame",
        "policy_reason": "conflict",
    },
}
FROZEN_EPIC032_EVIDENCE: Mapping[str, tuple[str, int]] = {
    "audit/gates/narratives/pack_identity.txt": (
        "e4facb2a0e2d6ace217c2bcdb639b7a508bbc8f19333dca904371b81f4de3b2c",
        883,
    ),
    "audit/gates/narratives/registry.diff.json": (
        "15fc9dd6a1d03b6170fc619fbf53ada0f7fc5a8a63006a39178816ec6dd11911",
        1372,
    ),
}
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_UTC_TIMESTAMP = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
)


class RegistryDiffError(RuntimeError):
    """Raised when registry diff evidence cannot be generated unambiguously."""


def _normalize_source_value(value: str) -> str:
    """Undo only Markdown escaping used by the checked-in PF18 intake transcript."""

    return value.replace(r"\_", "_")


def _pf18_source_records(
    source_path: Path | None = None,
) -> list[dict[str, Any]]:
    """Parse and close the PF18 direction-aware authoring corpus.

    PF18 is a transcript and repeats the 24 Drive/Balance shared rows once.
    Exact repeats are coalesced; conflicting repeats fail closed.
    """

    active_source = source_path or PF18_SOURCE_PATH
    try:
        source_bytes = active_source.read_bytes()
    except FileNotFoundError as exc:
        raise RegistryDiffError("PF18 narrative source missing") from exc
    if _sha256(source_bytes) != PF18_SOURCE_SHA256:
        raise RegistryDiffError("PF18 narrative source digest mismatch")
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RegistryDiffError("PF18 narrative source is not UTF-8") from exc

    field_names = {
        "CATEGORY": "category",
        "BAND": "band",
        "PERSPECTIVE": "perspective",
        "SLOT": "slot",
        "ID": "key",
        "TEXT": "text",
    }
    pending: dict[str, Any] = {}
    occurrences: list[dict[str, Any]] = []
    for raw_line in source_text.splitlines():
        line = raw_line.strip()
        prefix, separator, raw_value = line.partition(":")
        if not separator or prefix not in field_names:
            continue
        field = field_names[prefix]
        value = _normalize_source_value(raw_value.strip())
        if field == "category" and pending:
            # A new candidate may start only after the prior one was complete.
            raise RegistryDiffError("PF18 narrative source candidate incomplete")
        if field in pending:
            raise RegistryDiffError(f"PF18 narrative source duplicate field: {field}")
        if field == "slot":
            try:
                pending[field] = int(value)
            except ValueError as exc:
                raise RegistryDiffError("PF18 narrative source slot invalid") from exc
        else:
            pending[field] = value
        if field == "text":
            if set(pending) != set(field_names.values()):
                raise RegistryDiffError("PF18 narrative source candidate incomplete")
            occurrences.append(pending)
            pending = {}
    if pending:
        raise RegistryDiffError("PF18 narrative source candidate incomplete")
    if len(occurrences) != PF18_SOURCE_OCCURRENCES:
        raise RegistryDiffError("PF18 narrative source occurrence count mismatch")

    by_identity: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    source_ids: set[str] = set()
    duplicate_count = 0
    for record in occurrences:
        identity = (
            record["category"],
            record["band"],
            record["perspective"],
            record["slot"],
        )
        expected_id_prefix = ".".join(
            (
                "nar",
                record["category"],
                record["band"].lower(),
                record["perspective"],
                str(record["slot"]),
            )
        ) + "."
        if not record["key"].startswith(expected_id_prefix):
            raise RegistryDiffError(
                f"PF18 source id does not match candidate identity: {record['key']}"
            )
        previous = by_identity.get(identity)
        if previous is not None:
            if previous != record:
                raise RegistryDiffError("PF18 narrative source has conflicting duplicate")
            duplicate_count += 1
            continue
        if record["key"] in source_ids:
            raise RegistryDiffError(f"PF18 narrative source id duplicated: {record['key']}")
        source_ids.add(record["key"])
        by_identity[identity] = record

    records = sorted(
        by_identity.values(),
        key=lambda row: (
            row["category"],
            row["band"],
            row["perspective"],
            row["slot"],
            row["key"],
        ),
    )
    if len(records) != PF18_UNIQUE_CANDIDATES:
        raise RegistryDiffError("PF18 narrative source candidate count mismatch")
    if duplicate_count != PF18_DUPLICATE_OCCURRENCES:
        raise RegistryDiffError("PF18 narrative source duplicate count mismatch")
    return records


def build_pf17_directional_pack(
    source_path: Path | None = None,
) -> dict[str, Any]:
    """Build the exact direction-native PF17 pack payloads from PF18."""

    source_records = _pf18_source_records(source_path)
    keys = [
        {
            "band": record["band"],
            "category": record["category"],
            "category_slug": record["category"],
            "key": record["key"],
            "perspective": record["perspective"],
            "slot": record["slot"],
        }
        for record in source_records
    ]
    templates = {record["key"]: record["text"] for record in source_records}
    return {
        "keys.json": keys,
        "palettes.json": {"palettes": {"default": {"style": "plain"}}},
        "suppression_map.json": dict(SUPPRESSED_SOURCE_CANDIDATES),
        "templates.json": templates,
    }


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
        _read_json(active_manifest_path, repo_root=repo_root), trailing_lf=True
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
            _read_json(artifact_path, repo_root=repo_root), trailing_lf=True
        )
        if artifact_path.read_bytes() != canonical:
            raise RegistryDiffError(f"artifact is not canonical LF JSON: {rel}")
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

    manifest_bytes = _manifest_canonical_bytes(manifest_path, repo_root=repo_root)
    if manifest_path.read_bytes() != manifest_bytes:
        raise RegistryDiffError("manifest is not canonical LF JSON")
    manifest_sha = _sha256(manifest_bytes)
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
    expected_pack = build_pf17_directional_pack()
    if identity_records != expected_pack["keys.json"]:
        raise RegistryDiffError("keys.json must exactly preserve the PF18 directional corpus")

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
    if templates != expected_pack["templates.json"]:
        raise RegistryDiffError("templates.json must exactly preserve PF18 source copy")

    palettes = _read_json(
        active_catalog_root / "palettes.json", repo_root=repo_root
    )
    if palettes != expected_pack["palettes.json"]:
        raise RegistryDiffError("palettes.json must contain the governed default palette")

    suppression_map = _read_json(
        active_catalog_root / "suppression_map.json", repo_root=repo_root
    )
    if not isinstance(suppression_map, dict):
        raise RegistryDiffError("suppression_map.json must be an object")
    if suppression_map != expected_pack["suppression_map.json"]:
        raise RegistryDiffError("suppression_map.json must match PF17/PF15 candidate policy")
    for key, policy in suppression_map.items():
        if not isinstance(policy, dict) or set(policy) != {"notes", "policy_reason"}:
            raise RegistryDiffError(f"invalid suppression policy shape: {key}")
        if policy["policy_reason"] != "conflict":
            raise RegistryDiffError(f"invalid suppression policy reason: {key}")
        notes = policy["notes"]
        if not isinstance(notes, str) or not notes.startswith("PF15 forbidden token: "):
            raise RegistryDiffError(f"invalid suppression policy notes: {key}")
    for key, text in templates.items():
        failures = tuple(run_narrative_lints(text))
        if key in suppression_map:
            if failures != ("NARR_INCLUSIVE_TONE_OK",):
                raise RegistryDiffError(f"suppressed candidate lint posture changed: {key}")
        elif failures:
            raise RegistryDiffError(
                f"unsuppressed template failed narrative lints: {key}:{','.join(failures)}"
            )
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
        if set(raw) != set(REQUIRED_KEY_FIELDS):
            raise RegistryDiffError("key record fields do not match PF17")
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
        expected_key_prefix = ".".join(
            (
                "nar",
                record["category_slug"],
                record["band"].lower(),
                record["perspective"],
                str(record["slot"]),
            )
        ) + "."
        if not record["key"].startswith(expected_key_prefix):
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

    canonical_records = sorted(
        records,
        key=lambda row: (
            row["category_slug"],
            row["band"],
            row["perspective"],
            row["slot"],
            row["key"],
        ),
    )
    if records != canonical_records:
        raise RegistryDiffError("keys.json rows must match canonical identity order")
    records = canonical_records
    summary = {
        "category_count": len(summary_by_category),
        "key_count": len(records),
        "keys_sha256": _sha256(_canonical_json_bytes(records, trailing_lf=False)),
        "perspectives": dict(sorted(summary_by_perspective.items())),
        "tuple_count": len(summary_by_tuple),
    }
    return records, summary


def _pf17_pack_outputs(
    catalog_root: Path | None = None,
    *,
    source_path: Path | None = None,
) -> dict[Path, bytes]:
    active_catalog_root = catalog_root or CATALOG_ROOT
    payloads = build_pf17_directional_pack(source_path)
    outputs: dict[Path, bytes] = {}
    manifest_files: list[dict[str, Any]] = []
    for name in sorted(payloads):
        path = active_catalog_root / name
        body = _canonical_json_bytes(payloads[name], trailing_lf=True)
        digest = _sha256(body)
        outputs[path] = body
        outputs[path.with_suffix(path.suffix + ".sha256")] = (
            digest + "\n"
        ).encode("ascii")
        manifest_files.append(
            {
                "path": f"catalog/narratives/{name}",
                "sha256": digest,
                "size_bytes": len(body),
            }
        )
    manifest = {
        "created_utc": PACK_CREATED_UTC,
        "files": manifest_files,
        "pack_name": "narratives_v1",
    }
    manifest_path = active_catalog_root / "manifest.json"
    manifest_bytes = _canonical_json_bytes(manifest, trailing_lf=True)
    outputs[manifest_path] = manifest_bytes
    outputs[manifest_path.with_suffix(".json.sha256")] = (
        _sha256(manifest_bytes) + "\n"
    ).encode("ascii")
    return outputs


def write_pf17_directional_pack(
    *,
    check: bool = False,
    catalog_root: Path | None = None,
    source_path: Path | None = None,
) -> None:
    """Write or verify the PF17 direction-native pack without historical evidence."""

    active_catalog_root = catalog_root or CATALOG_ROOT
    stale: list[str] = []
    for path, expected in _pf17_pack_outputs(
        active_catalog_root, source_path=source_path
    ).items():
        if path.exists() and path.read_bytes() == expected:
            continue
        if check:
            stale.append(_display_path(path))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(expected)
    if stale:
        raise SystemExit("STALE:" + ",".join(stale))


def _verify_frozen_epic032_evidence(root: Path = ROOT) -> None:
    drift: list[str] = []
    for name, (expected_sha256, expected_size) in FROZEN_EPIC032_EVIDENCE.items():
        path = root / name
        if not path.is_file() or path.is_symlink():
            drift.append(name)
            continue
        body = path.read_bytes()
        if (
            len(body) != expected_size
            or _sha256(body) != expected_sha256
        ):
            drift.append(name)
    if drift:
        raise SystemExit(
            "FROZEN_EPIC032_REGISTRY_DRIFT:" + ",".join(sorted(drift))
        )


def write_artifacts(*, check: bool = False) -> None:
    """Refuse historical writes; check only the retained capture bytes."""

    if not check:
        raise SystemExit("HISTORICAL_EPIC032_REGISTRY_WRITE_REFUSED")
    _verify_frozen_epic032_evidence()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Build the PF17 pack or verify frozen EPIC032 registry evidence"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the retained EPIC032 capture bytes",
    )
    parser.add_argument(
        "--export-pf17-pack",
        action="store_true",
        help="Export the PF17 direction-native pack from the governed PF18 source",
    )
    parser.add_argument(
        "--check-pf17-pack",
        action="store_true",
        help="Fail if the PF17 direction-native pack differs from its governed source",
    )
    args = parser.parse_args(argv)
    mode_count = sum(
        (args.check, args.export_pf17_pack, args.check_pf17_pack)
    )
    if mode_count == 0:
        raise SystemExit("HISTORICAL_EPIC032_REGISTRY_WRITE_REFUSED")
    if mode_count > 1:
        parser.error("choose exactly one mode")
    ensure_determinism_env()
    if args.export_pf17_pack:
        write_pf17_directional_pack()
        return
    if args.check_pf17_pack:
        write_pf17_directional_pack(check=True)
        return
    write_artifacts(check=args.check)


if __name__ == "__main__":
    main()
