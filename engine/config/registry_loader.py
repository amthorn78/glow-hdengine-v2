from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from engine.categories.registry import FROZEN_MAGIC10_ORDER


# Discovery (PR3 / EPIC017): this loader owns the PF12 catalogs under catalog/ (gates_v1,
# channels_v1, magic10*.json, manifest.json). The legacy registry_report lived at
# artifacts/reports/registry_report.json with only category ranks; we normalize it to
# artifacts/registry/registry_report.json with PF14 keys and hardened validation. Legacy
# Magic-10 order/caps checks must be preserved; catalog ID handling is tightened to fail
# closed on unknown IDs and aliases.


class RegistryConfigError(Exception):
    def __init__(self, code: str, message: str, details: Mapping[str, object] | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = dict(details or {})


class UnknownIdError(RegistryConfigError):
    pass


class DuplicateIdError(RegistryConfigError):
    pass


class AliasPolicyError(RegistryConfigError):
    pass


class SchemaValidationError(RegistryConfigError):
    pass


@dataclass(frozen=True)
class Gate:
    gate: int
    center: str


@dataclass(frozen=True)
class Channel:
    id: str
    gates: tuple[int, int]
    centers: tuple[str, str]
    circuit_primary: str
    substream: str | None
    primary_domain: str
    domains: tuple[str, ...]
    flags: tuple[str, ...]


@dataclass(frozen=True)
class Magic10Caps:
    inputs: tuple[str, ...]
    bounds: Mapping[str, int]


@dataclass(frozen=True)
class Magic10Seed:
    template_id: str
    seed_version: str
    updated_at_utc: str
    checksum_sha256: str


@dataclass(frozen=True)
class ManifestEntry:
    path: str
    sha256: str
    size: int


@dataclass(frozen=True)
class RegistryConfig:
    gates: dict[int, Gate]
    channels: dict[str, Channel]
    alias_map: dict[str, str]
    magic10_order: tuple[str, ...]
    magic10_caps: dict[str, Magic10Caps]
    magic10_seeds: dict[str, Magic10Seed]
    manifest_entries: tuple[ManifestEntry, ...]
    centers: tuple[str, ...]
    domains: tuple[str, ...]


def _load_json(path: Path) -> object:
    if not path.exists():
        raise SchemaValidationError("MISSING_FILE", f"missing catalog file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - raised via typed error
        raise SchemaValidationError("INVALID_JSON", f"failed to parse {path}") from exc


def _validate_gate_center(center: object, *, centers: set[str]) -> str:
    if not isinstance(center, str) or not center:
        raise SchemaValidationError("INVALID_CENTER", "gate center must be a non-empty string")
    centers.add(center)
    return center


def _load_gates(root: Path) -> tuple[dict[int, Gate], tuple[str, ...]]:
    raw = _load_json(root / "catalog" / "gates_v1.json")
    if not isinstance(raw, dict) or "gates" not in raw:
        raise SchemaValidationError("INVALID_GATES", "gates_v1.json must contain a gates array")
    gates_raw = raw["gates"]
    if not isinstance(gates_raw, list):
        raise SchemaValidationError("INVALID_GATES", "gates must be a list")
    gates: dict[int, Gate] = {}
    centers: set[str] = set()
    for entry in gates_raw:
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_GATES", "gate entry must be an object")
        gate_id = entry.get("gate")
        center = _validate_gate_center(entry.get("center"), centers=centers)
        if not isinstance(gate_id, int):
            raise SchemaValidationError("INVALID_GATES", "gate id must be an int")
        if gate_id in gates:
            raise DuplicateIdError("DUPLICATE_GATE", f"duplicate gate id {gate_id}")
        gates[gate_id] = Gate(gate=gate_id, center=center)
    return gates, tuple(sorted(centers))


def _normalize_channel_id(channel_id: str, gates: Iterable[int]) -> str:
    if not re.match(r"^\d{2}-\d{2}$", channel_id):
        raise SchemaValidationError("INVALID_CHANNEL_ID", f"invalid channel id format: {channel_id}")
    a, b = map(int, channel_id.split("-"))
    g1, g2 = sorted(int(g) for g in gates)
    if (a, b) != (g1, g2):
        raise SchemaValidationError("CHANNEL_ID_MISMATCH", f"channel id {channel_id} does not match gates {gates}")
    return f"{g1:02d}-{g2:02d}"


def _load_channels(
    root: Path,
    *,
    gate_map: Mapping[int, Gate],
    known_centers: set[str],
    allow_aliases: bool,
    alias_ledger: Mapping[str, str] | None,
) -> tuple[dict[str, Channel], dict[str, str], tuple[str, ...]]:
    raw = _load_json(root / "catalog" / "channels_v1.json")
    if not isinstance(raw, dict) or "channels" not in raw:
        raise SchemaValidationError("INVALID_CHANNELS", "channels_v1.json must contain a channels array")
    channels_raw = raw["channels"]
    if not isinstance(channels_raw, list):
        raise SchemaValidationError("INVALID_CHANNELS", "channels must be a list")

    channels: dict[str, Channel] = {}
    alias_map: dict[str, str] = {}
    pending_aliases: list[dict[str, object]] = []
    domains: set[str] = set()

    for entry in channels_raw:
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_CHANNELS", "channel entry must be an object")
        alias_for = entry.get("alias_for")
        if alias_for is not None:
            if not allow_aliases:
                raise AliasPolicyError("ALIASES_FORBIDDEN", "alias entries are not allowed by default")
            pending_aliases.append(entry)
            continue

        channel_id_raw = entry.get("id")
        gates_raw = entry.get("gates")
        centers_raw = entry.get("centers")
        if not isinstance(channel_id_raw, str):
            raise SchemaValidationError("INVALID_CHANNELS", "channel id must be a string")
        if not isinstance(gates_raw, list) or len(gates_raw) != 2:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {channel_id_raw} must reference two gates")
        if not isinstance(centers_raw, list) or len(centers_raw) != 2:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {channel_id_raw} must declare two centers")

        gates_tuple = (int(gates_raw[0]), int(gates_raw[1]))
        normalized_id = _normalize_channel_id(channel_id_raw, gates_tuple)
        if normalized_id in channels:
            raise DuplicateIdError("DUPLICATE_CHANNEL", f"duplicate channel id {normalized_id}")

        for g in gates_tuple:
            if g not in gate_map:
                raise UnknownIdError("UNKNOWN_GATE", f"channel {normalized_id} references unknown gate {g}")
        centers_tuple = (str(centers_raw[0]), str(centers_raw[1]))
        for c in centers_tuple:
            if c not in known_centers:
                raise UnknownIdError("UNKNOWN_CENTER", f"channel {normalized_id} references unknown center {c}")
        circuit_primary = entry.get("circuit_primary")
        primary_domain = entry.get("primary_domain")
        domain_list = entry.get("domains", [])
        flags_list = entry.get("flags", [])
        if not isinstance(circuit_primary, str) or not circuit_primary:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {normalized_id} missing circuit_primary")
        if not isinstance(primary_domain, str) or not primary_domain:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {normalized_id} missing primary_domain")
        if not isinstance(domain_list, list) or not domain_list:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {normalized_id} missing domains")
        if primary_domain not in domain_list:
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {normalized_id} primary_domain must be in domains")
        if not isinstance(flags_list, list):
            raise SchemaValidationError("INVALID_CHANNELS", f"channel {normalized_id} flags must be a list")

        domains.update(str(d) for d in domain_list)
        channels[normalized_id] = Channel(
            id=normalized_id,
            gates=tuple(sorted(gates_tuple)),
            centers=centers_tuple,
            circuit_primary=str(circuit_primary),
            substream=entry.get("substream"),
            primary_domain=str(primary_domain),
            domains=tuple(dict.fromkeys(str(d) for d in domain_list)),
            flags=tuple(dict.fromkeys(str(f) for f in flags_list)),
        )

    if pending_aliases and not allow_aliases:
        raise AliasPolicyError("ALIASES_FORBIDDEN", "alias entries are not allowed")

    ledger = dict(alias_ledger or {})
    for entry in pending_aliases:
        alias_id_raw = entry.get("id")
        alias_for = entry.get("alias_for")
        gates_raw = entry.get("gates")
        if not isinstance(alias_id_raw, str) or not isinstance(alias_for, str):
            raise SchemaValidationError("INVALID_ALIAS", "alias id and alias_for must be strings")
        if alias_id_raw in channels or alias_id_raw in alias_map:
            raise DuplicateIdError("DUPLICATE_ALIAS", f"duplicate alias id {alias_id_raw}")
        if alias_id_raw not in ledger:
            raise AliasPolicyError("ALIAS_NOT_ALLOWED", f"alias {alias_id_raw} not present in allow-list")
        target = ledger[alias_id_raw]
        if target != alias_for:
            raise AliasPolicyError("ALIAS_LEDGER_MISMATCH", f"alias {alias_id_raw} target mismatch")
        if target not in channels:
            raise UnknownIdError("UNKNOWN_ALIAS_TARGET", f"alias target {target} missing from channels")
        if not isinstance(gates_raw, list) or len(gates_raw) != 2:
            raise SchemaValidationError("INVALID_ALIAS", f"alias {alias_id_raw} must reference two gates")
        _normalize_channel_id(alias_id_raw, (int(gates_raw[0]), int(gates_raw[1])))
        alias_map[alias_id_raw] = target

    return channels, alias_map, tuple(sorted(domains))


def _load_magic10(root: Path) -> tuple[tuple[str, ...], dict[str, Magic10Caps], dict[str, Magic10Seed]]:
    order_raw = _load_json(root / "catalog" / "magic10.json")
    if not isinstance(order_raw, dict) or "order" not in order_raw:
        raise SchemaValidationError("INVALID_MAGIC10", "magic10.json must contain an order array")
    order_list = order_raw.get("order")
    if not isinstance(order_list, list):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10 order must be a list")
    magic_order = tuple(order_list)
    if magic_order != FROZEN_MAGIC10_ORDER:
        raise SchemaValidationError("MAGIC10_ORDER_MISMATCH", "magic10 order must match registry")

    caps_raw = _load_json(root / "catalog" / "magic10_caps.json")
    if not isinstance(caps_raw, dict):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10_caps must be an object")
    if set(caps_raw.keys()) != set(magic_order):
        raise SchemaValidationError("MAGIC10_CAPS_COVERAGE", "magic10_caps must cover full magic10 order")
    caps: dict[str, Magic10Caps] = {}
    for key, entry in caps_raw.items():
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MAGIC10", "magic10_caps entries must be objects")
        inputs = entry.get("inputs")
        bounds = entry.get("bounds")
        if not isinstance(inputs, list) or not inputs:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] inputs must be a non-empty list")
        if not isinstance(bounds, dict) or "min" not in bounds or "max" not in bounds:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] bounds invalid")
        caps[key] = Magic10Caps(inputs=tuple(inputs), bounds={"min": int(bounds["min"]), "max": int(bounds["max"])})

    seeds_raw = _load_json(root / "catalog" / "magic10_seeds.json")
    if not isinstance(seeds_raw, dict):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10_seeds must be an object")
    unknown_seeds = set(seeds_raw.keys()) - set(magic_order)
    if unknown_seeds:
        raise UnknownIdError("UNKNOWN_MAGIC10_SEED", f"unknown magic10 seed ids: {sorted(unknown_seeds)}")
    seeds: dict[str, Magic10Seed] = {}
    for key, entry in seeds_raw.items():
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MAGIC10", "magic10_seeds entries must be objects")
        required = {"template_id", "seed_version", "updated_at_utc", "checksum_sha256"}
        if not required <= entry.keys():
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_seeds[{key}] missing required fields")
        seeds[key] = Magic10Seed(
            template_id=str(entry["template_id"]),
            seed_version=str(entry["seed_version"]),
            updated_at_utc=str(entry["updated_at_utc"]),
            checksum_sha256=str(entry["checksum_sha256"]),
        )

    return magic_order, caps, seeds


def _load_manifest(root: Path) -> tuple[ManifestEntry, ...]:
    raw = _load_json(root / "catalog" / "manifest.json")
    if not isinstance(raw, dict) or "entries" not in raw:
        raise SchemaValidationError("INVALID_MANIFEST", "manifest.json must contain entries array")
    entries_raw = raw["entries"]
    if not isinstance(entries_raw, list):
        raise SchemaValidationError("INVALID_MANIFEST", "manifest entries must be a list")
    manifest_entries: list[ManifestEntry] = []
    seen_paths: set[str] = set()
    for entry in entries_raw:
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MANIFEST", "manifest entry must be an object")
        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size")
        if not isinstance(path, str) or not isinstance(sha, str) or not isinstance(size, int):
            raise SchemaValidationError("INVALID_MANIFEST", "manifest entry requires path, sha256, size")
        if path in seen_paths:
            raise DuplicateIdError("DUPLICATE_MANIFEST_ENTRY", f"duplicate manifest path {path}")
        seen_paths.add(path)
        manifest_entries.append(ManifestEntry(path=path, sha256=sha, size=size))
    manifest_entries.sort(key=lambda e: e.path)
    return tuple(manifest_entries)


def load_registry_config(
    root: Path | str | None = None,
    *,
    allow_aliases: bool = False,
    alias_ledger: Mapping[str, str] | None = None,
) -> RegistryConfig:
    base = Path(root) if root is not None else Path.cwd()
    gates, centers = _load_gates(base)
    channels, alias_map, domains = _load_channels(
        base,
        gate_map=gates,
        known_centers=set(centers),
        allow_aliases=allow_aliases,
        alias_ledger=alias_ledger,
    )
    magic10_order, magic10_caps, magic10_seeds = _load_magic10(base)
    manifest_entries = _load_manifest(base)

    return RegistryConfig(
        gates=gates,
        channels=channels,
        alias_map=alias_map,
        magic10_order=magic10_order,
        magic10_caps=magic10_caps,
        magic10_seeds=magic10_seeds,
        manifest_entries=manifest_entries,
        centers=centers,
        domains=domains,
    )

