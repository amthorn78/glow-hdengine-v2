"""Load and verify the sealed narrative pack."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Mapping

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.serializer.canon import sercanon

from .constants import BANDS, PERSPECTIVES
from .lints import run_all as run_narrative_lints


_SOURCE_KEY = re.compile(
    r"^nar\.(?P<category>[a-z0-9_]+)\.(?P<band>[a-z]+)\."
    r"(?P<perspective>shared|a_to_b|b_to_a)\.(?P<slot>[123])\."
    r"[a-z0-9-]+$"
)
_KEY_FIELDS = {"band", "category", "category_slug", "key", "perspective", "slot"}
_MANIFEST_FILES = (
    "catalog/narratives/keys.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
)


@dataclass(frozen=True)
class NarrativeKeyRecord:
    """Canonical record for a single narrative template."""

    key: str
    category: str
    category_slug: str
    band: str
    perspective: str
    slot: int

    def __post_init__(self) -> None:
        if not self.key:
            raise ValueError("key required")

    @property
    def composition_id(self) -> str:
        return self.key


@dataclass
class NarrativePack:
    """Loaded narrative pack, ready for routing and composition."""

    pack_sha: str
    manifest: Mapping[str, object]
    keys: Dict[str, NarrativeKeyRecord]
    templates: Mapping[str, str]
    suppression_map: Mapping[str, Mapping[str, str]]
    palettes: Mapping[str, object]
    primary_by_perspective: Dict[tuple[str, str, str], NarrativeKeyRecord]
    mount_path: Path

    @property
    def categories(self) -> set[str]:
        return {record.category_slug for record in self.keys.values()}


class NarrativePackError(RuntimeError):
    """Raised when verification or loading fails."""


def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json(path: Path) -> object:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise NarrativePackError(f"missing file: {path}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise NarrativePackError(f"invalid JSON: {path}") from exc


def _canonical_bytes(path: Path) -> bytes:
    raw = path.read_bytes()
    if path.suffix != ".json":
        return raw
    try:
        obj = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise NarrativePackError(f"invalid JSON: {path}") from exc
    canonical = sercanon(obj, sort_keys=True)
    if raw != canonical:
        raise NarrativePackError(f"noncanonical JSON bytes: {path}")
    return raw


def _verify_sidecar(path: Path) -> None:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    try:
        expected = sidecar.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise NarrativePackError(f"missing sidecar: {sidecar}") from exc
    actual = _sha256_hex(_canonical_bytes(path))
    if actual != expected:
        raise NarrativePackError(f"sha256 mismatch for {path}")


def _verify_manifest(manifest_path: Path) -> dict:
    manifest = _read_json(manifest_path)
    if not isinstance(manifest, dict):
        raise NarrativePackError("manifest must be an object")
    if set(manifest) != {"created_utc", "files", "pack_name"}:
        raise NarrativePackError("manifest fields invalid")
    if manifest.get("pack_name") != "narratives_v1":
        raise NarrativePackError("manifest pack_name invalid")
    files = manifest.get("files")
    if not isinstance(files, list):
        raise NarrativePackError("manifest.files must be a list")
    repo_root = manifest_path.parents[2]
    seen: set[str] = set()
    for entry in files:
        if not isinstance(entry, dict):
            raise NarrativePackError("manifest entry must be an object")
        if set(entry) != {"path", "sha256", "size_bytes"}:
            raise NarrativePackError("manifest entry fields invalid")
        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size_bytes")
        if (
            not isinstance(path, str)
            or not isinstance(sha, str)
            or type(size) is not int
            or path in seen
        ):
            raise NarrativePackError("manifest entry missing required fields")
        seen.add(path)
        file_path = repo_root / path
        if not file_path.exists():
            raise NarrativePackError(f"manifest path missing: {path}")
        canonical_bytes = _canonical_bytes(file_path)
        actual_sha = _sha256_hex(canonical_bytes)
        if actual_sha != sha:
            raise NarrativePackError(f"manifest sha mismatch: {path}")
        actual_size = len(canonical_bytes)
        if actual_size != size:
            raise NarrativePackError(f"manifest size mismatch: {path}")
    if tuple(entry["path"] for entry in files) != _MANIFEST_FILES:
        raise NarrativePackError("manifest file roster invalid")
    return manifest


def _select_primary(
    records: Dict[int, NarrativeKeyRecord],
    suppression_map: Mapping[str, Mapping[str, str]],
    templates: Mapping[str, str],
) -> NarrativeKeyRecord | None:
    for slot in sorted(records):
        record = records[slot]
        if record.key in suppression_map:
            continue
        text = templates.get(record.key)
        if not isinstance(text, str) or tuple(run_narrative_lints(text)):
            continue
        return record
    return None


def _normalize_band(band: str) -> str:
    if band in BANDS:
        return band
    raise NarrativePackError(f"unknown band: {band}")


def _copy_files_atomic(mount_root: Path, pack_sha: str, files: Iterable[Path]) -> Path:
    source_files = tuple(files)

    def _require_exact_mount(target: Path) -> None:
        expected_names = {source.name for source in source_files}
        actual_names = {path.name for path in target.iterdir() if path.is_file()}
        if actual_names != expected_names:
            raise NarrativePackError("existing narrative mount file roster mismatch")
        for source in source_files:
            mounted = target / source.name
            if not mounted.is_file() or mounted.read_bytes() != source.read_bytes():
                raise NarrativePackError(
                    f"existing narrative mount bytes mismatch: {source.name}"
                )

    mount_root.mkdir(parents=True, exist_ok=True)
    target = mount_root / pack_sha
    if target.exists():
        _require_exact_mount(target)
        return target
    temp_dir = mount_root / f".{pack_sha}.tmp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    for src in source_files:
        dest = temp_dir / src.name
        shutil.copy2(src, dest)
    try:
        temp_dir.replace(target)
    except FileExistsError:
        shutil.rmtree(temp_dir)
        _require_exact_mount(target)
    return target


def load_pack(catalog_root: Path | None = None, mount_root: Path | None = None) -> NarrativePack:
    """Load, verify, and mount the narrative pack from catalog/narratives."""

    catalog_root = catalog_root or Path("catalog/narratives")
    mount_root = mount_root or Path("narratives")

    json_files = sorted(catalog_root.glob("*.json"))
    if not json_files:
        raise NarrativePackError("no narrative pack files found")

    for path in json_files:
        _verify_sidecar(path)

    manifest_path = catalog_root / "manifest.json"
    manifest = _verify_manifest(manifest_path)

    manifest_bytes = _canonical_bytes(manifest_path)
    pack_sha = _sha256_hex(manifest_bytes)
    manifest_sidecar = manifest_path.with_suffix(".json.sha256")
    manifest_expected = manifest_sidecar.read_text(encoding="utf-8").strip()
    if pack_sha != manifest_expected:
        raise NarrativePackError("manifest sidecar mismatch")

    keys_data = _read_json(catalog_root / "keys.json")
    templates = _read_json(catalog_root / "templates.json")
    suppression_map = _read_json(catalog_root / "suppression_map.json")
    palettes = _read_json(catalog_root / "palettes.json")

    if not isinstance(keys_data, list):
        raise NarrativePackError("keys.json must be an array")
    if not isinstance(templates, dict):
        raise NarrativePackError("templates.json must be an object")
    if not isinstance(suppression_map, dict):
        raise NarrativePackError("suppression_map.json must be an object")
    if not isinstance(palettes, dict):
        raise NarrativePackError("palettes.json must be an object")

    if palettes != {"palettes": {"default": {"style": "plain"}}}:
        raise NarrativePackError("palettes.json invalid")
    if any(
        not isinstance(key, str)
        or not isinstance(value, str)
        or not value
        for key, value in templates.items()
    ):
        raise NarrativePackError("templates.json invalid")

    keys: Dict[str, NarrativeKeyRecord] = {}
    slots_by_perspective: Dict[
        tuple[str, str, str], Dict[int, NarrativeKeyRecord]
    ] = {}
    identities: set[tuple[str, str, str, int]] = set()
    source_records: list[NarrativeKeyRecord] = []

    for entry in keys_data:
        if not isinstance(entry, dict) or set(entry) != _KEY_FIELDS:
            raise NarrativePackError("invalid key record")
        try:
            if any(
                not isinstance(entry[field], str)
                for field in ("key", "category", "category_slug", "band", "perspective")
            ) or type(entry["slot"]) is not int:
                raise TypeError
            record = NarrativeKeyRecord(
                key=entry["key"],
                category=entry["category"],
                category_slug=entry["category_slug"],
                band=_normalize_band(entry["band"]),
                perspective=entry["perspective"],
                slot=entry["slot"],
            )
        except (KeyError, ValueError, TypeError) as exc:
            raise NarrativePackError("invalid key record fields") from exc
        if (
            record.category != record.category_slug
            or record.category_slug not in CATEGORIES_ORDER_V1
            or record.band not in BANDS
            or record.perspective not in PERSPECTIVES
            or record.slot not in (1, 2, 3)
        ):
            raise NarrativePackError("invalid key record identity")
        source_match = _SOURCE_KEY.fullmatch(record.key)
        if source_match is None or (
            source_match.group("category") != record.category_slug
            or source_match.group("band") != record.band.lower()
            or source_match.group("perspective") != record.perspective
            or int(source_match.group("slot")) != record.slot
        ):
            raise NarrativePackError("key/source identity mismatch")
        identity = (
            record.category_slug,
            record.band,
            record.perspective,
            record.slot,
        )
        if identity in identities or record.key in keys:
            raise NarrativePackError("duplicate key record identity")
        identities.add(identity)
        keys[record.key] = record
        source_records.append(record)
        bucket_key = (record.category_slug, record.band, record.perspective)
        slots_by_perspective.setdefault(bucket_key, {})[record.slot] = record

    expected_identities = {
        (category, band, perspective, slot)
        for category in CATEGORIES_ORDER_V1
        for band in BANDS
        for perspective in PERSPECTIVES
        for slot in (1, 2, 3)
    }
    if identities != expected_identities:
        raise NarrativePackError("narrative candidate grid incomplete")
    canonical_records = sorted(
        source_records,
        key=lambda record: (
            record.category_slug,
            record.band,
            record.perspective,
            record.slot,
            record.key,
        ),
    )
    if source_records != canonical_records:
        raise NarrativePackError("key records not in canonical identity order")

    if set(templates) != set(keys):
        raise NarrativePackError("templates.json keys must exactly match keys.json")
    if any(key not in keys for key in suppression_map):
        raise NarrativePackError("suppression_map contains unknown key")
    for key, policy in suppression_map.items():
        if (
            not isinstance(policy, dict)
            or set(policy) != {"notes", "policy_reason"}
            or policy.get("policy_reason") != "conflict"
            or not isinstance(policy.get("notes"), str)
            or not policy["notes"]
        ):
            raise NarrativePackError(f"invalid suppression policy: {key}")

    primary_by_perspective: Dict[
        tuple[str, str, str], NarrativeKeyRecord
    ] = {}
    for bucket, slot_map in slots_by_perspective.items():
        record = _select_primary(slot_map, suppression_map, templates)
        if record:
            primary_by_perspective[bucket] = record

    files_to_copy = list(catalog_root.glob("*.json")) + list(catalog_root.glob("*.sha256"))
    pack_mount = _copy_files_atomic(mount_root, pack_sha, files_to_copy)

    return NarrativePack(
        pack_sha=pack_sha,
        manifest=manifest,
        keys=keys,
        templates=templates,
        suppression_map=suppression_map,
        palettes=palettes,
        primary_by_perspective=primary_by_perspective,
        mount_path=pack_mount,
    )
