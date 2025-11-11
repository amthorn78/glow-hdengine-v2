"""Load and verify the sealed narrative pack."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Mapping

from .constants import BANDS


@dataclass(frozen=True)
class NarrativeKeyRecord:
    """Canonical record for a single narrative template."""

    key: str
    category: str
    category_slug: str
    band: str
    perspective: str
    slot: int
    directions: tuple[str, ...] = field(default_factory=tuple)

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
    shared_primary: Dict[tuple[str, str], NarrativeKeyRecord]
    personal_primary: Dict[tuple[str, str], NarrativeKeyRecord]
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
    canonical = json.dumps(obj, separators=(",", ":"), sort_keys=True)
    return canonical.encode("utf-8")


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
    files = manifest.get("files")
    if not isinstance(files, list):
        raise NarrativePackError("manifest.files must be a list")
    for entry in files:
        if not isinstance(entry, dict):
            raise NarrativePackError("manifest entry must be an object")
        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size_bytes")
        if not isinstance(path, str) or not isinstance(sha, str) or not isinstance(size, int):
            raise NarrativePackError("manifest entry missing required fields")
        file_path = Path(path)
        if not file_path.exists():
            raise NarrativePackError(f"manifest path missing: {path}")
        canonical_bytes = _canonical_bytes(file_path)
        actual_sha = _sha256_hex(canonical_bytes)
        if actual_sha != sha:
            raise NarrativePackError(f"manifest sha mismatch: {path}")
        actual_size = len(canonical_bytes) if file_path.suffix == ".json" else file_path.stat().st_size
        if actual_size != size:
            raise NarrativePackError(f"manifest size mismatch: {path}")
    return manifest


def _select_primary(
    records: Dict[int, NarrativeKeyRecord],
    suppression_map: Mapping[str, Mapping[str, str]],
) -> NarrativeKeyRecord | None:
    for slot in sorted(records):
        record = records[slot]
        if record.key in suppression_map:
            continue
        return record
    if records:
        return records[min(records)]
    return None


def _normalize_band(band: str) -> str:
    normalized = band.strip()
    for value in BANDS:
        if normalized.lower() == value.lower():
            return value
    raise NarrativePackError(f"unknown band: {band}")


def _copy_files_atomic(mount_root: Path, pack_sha: str, files: Iterable[Path]) -> Path:
    mount_root.mkdir(parents=True, exist_ok=True)
    temp_dir = mount_root / f".{pack_sha}.tmp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    for src in files:
        dest = temp_dir / src.name
        shutil.copy2(src, dest)
    target = mount_root / pack_sha
    if target.exists():
        shutil.rmtree(target)
    temp_dir.replace(target)
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

    keys: Dict[str, NarrativeKeyRecord] = {}
    shared_slots: Dict[tuple[str, str], Dict[int, NarrativeKeyRecord]] = {}
    personal_slots: Dict[tuple[str, str], Dict[int, NarrativeKeyRecord]] = {}

    for entry in keys_data:
        if not isinstance(entry, dict):
            raise NarrativePackError("invalid key record")
        try:
            record = NarrativeKeyRecord(
                key=str(entry["key"]),
                category=str(entry["category"]),
                category_slug=str(entry["category_slug"]),
                band=_normalize_band(str(entry["band"])),
                perspective=str(entry["perspective"]),
                slot=int(entry["slot"]),
                directions=tuple(entry.get("directions", ()) or ()),
            )
        except (KeyError, ValueError, TypeError) as exc:
            raise NarrativePackError("invalid key record fields") from exc
        keys[record.key] = record
        bucket_key = (record.category_slug, record.band)
        slots = shared_slots if record.perspective == "shared" else personal_slots
        slots.setdefault(bucket_key, {})[record.slot] = record

    # Verify template coverage
    for key in keys:
        if key not in templates:
            raise NarrativePackError(f"template missing for key {key}")

    shared_primary: Dict[tuple[str, str], NarrativeKeyRecord] = {}
    personal_primary: Dict[tuple[str, str], NarrativeKeyRecord] = {}
    for bucket, slot_map in shared_slots.items():
        record = _select_primary(slot_map, suppression_map)
        if record:
            shared_primary[bucket] = record
    for bucket, slot_map in personal_slots.items():
        record = _select_primary(slot_map, suppression_map)
        if record:
            personal_primary[bucket] = record

    files_to_copy = list(catalog_root.glob("*.json")) + list(catalog_root.glob("*.sha256"))
    pack_mount = _copy_files_atomic(mount_root, pack_sha, files_to_copy)

    return NarrativePack(
        pack_sha=pack_sha,
        manifest=manifest,
        keys=keys,
        templates=templates,
        suppression_map=suppression_map,
        palettes=palettes,
        shared_primary=shared_primary,
        personal_primary=personal_primary,
        mount_path=pack_mount,
    )
