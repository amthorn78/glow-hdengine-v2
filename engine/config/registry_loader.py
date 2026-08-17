from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Mapping

from engine.categories.registry import FROZEN_MAGIC10_ORDER


# PF08 — Human Design System, §Channels defines the complete 36-Channel
# BodyGraph roster.  This is an identity set: catalog ordering is enforced by
# the canonical JSON gate, while this loader independently refuses a
# schema-valid substitution of one Channel identity for another.
FROZEN_CHANNEL_IDS = (
    "01-08",
    "02-14",
    "03-60",
    "04-63",
    "05-15",
    "06-59",
    "07-31",
    "09-52",
    "10-20",
    "10-34",
    "10-57",
    "11-56",
    "12-22",
    "13-33",
    "16-48",
    "17-62",
    "18-58",
    "19-49",
    "20-34",
    "20-57",
    "21-45",
    "23-43",
    "24-61",
    "25-51",
    "26-44",
    "27-50",
    "28-38",
    "29-46",
    "30-41",
    "32-54",
    "34-57",
    "35-36",
    "37-40",
    "39-55",
    "42-53",
    "47-64",
)


# PF12 — HDE Schemas & Artifacts, §2.1 owns the exact Gate counts for the
# nine canonical center IDs.  Individual Gate-to-center assignments remain
# single-homed in catalog/gates_v1.json; this aggregate independently refuses
# a coherent cross-catalog reassignment that changes the governed topology.
FROZEN_GATE_CENTER_COUNTS = {
    "ajna": 6,
    "ego": 4,
    "g": 8,
    "head": 3,
    "root": 9,
    "sacral": 9,
    "solar_plexus": 7,
    "spleen": 7,
    "throat": 11,
}


# PF08 — Human Design System, §Channels lists each Channel's Gate endpoints in
# the same order as its Center heading (for example, 8-1 under Throat-to-G).
# Preserve that exact Gate-to-Center assignment independently of the Gate
# catalog so a coherent reassignment cannot redefine its own expected topology.
FROZEN_CHANNEL_ENDPOINT_CENTERS = {
    "01-08": ((8, "throat"), (1, "g")),
    "02-14": ((2, "g"), (14, "sacral")),
    "03-60": ((3, "sacral"), (60, "root")),
    "04-63": ((63, "head"), (4, "ajna")),
    "05-15": ((15, "g"), (5, "sacral")),
    "06-59": ((59, "sacral"), (6, "solar_plexus")),
    "07-31": ((31, "throat"), (7, "g")),
    "09-52": ((9, "sacral"), (52, "root")),
    "10-20": ((20, "throat"), (10, "g")),
    "10-34": ((10, "g"), (34, "sacral")),
    "10-57": ((10, "g"), (57, "spleen")),
    "11-56": ((11, "ajna"), (56, "throat")),
    "12-22": ((12, "throat"), (22, "solar_plexus")),
    "13-33": ((33, "throat"), (13, "g")),
    "16-48": ((16, "throat"), (48, "spleen")),
    "17-62": ((17, "ajna"), (62, "throat")),
    "18-58": ((18, "spleen"), (58, "root")),
    "19-49": ((49, "solar_plexus"), (19, "root")),
    "20-34": ((20, "throat"), (34, "sacral")),
    "20-57": ((20, "throat"), (57, "spleen")),
    "21-45": ((45, "throat"), (21, "ego")),
    "23-43": ((43, "ajna"), (23, "throat")),
    "24-61": ((61, "head"), (24, "ajna")),
    "25-51": ((25, "g"), (51, "ego")),
    "26-44": ((26, "ego"), (44, "spleen")),
    "27-50": ((50, "spleen"), (27, "sacral")),
    "28-38": ((28, "spleen"), (38, "root")),
    "29-46": ((46, "g"), (29, "sacral")),
    "30-41": ((30, "solar_plexus"), (41, "root")),
    "32-54": ((32, "spleen"), (54, "root")),
    "34-57": ((57, "spleen"), (34, "sacral")),
    "35-36": ((35, "throat"), (36, "solar_plexus")),
    "37-40": ((40, "ego"), (37, "solar_plexus")),
    "39-55": ((55, "solar_plexus"), (39, "root")),
    "42-53": ((42, "sacral"), (53, "root")),
    "47-64": ((64, "head"), (47, "ajna")),
}


# PF12 §2.5 makes each caps `inputs` value an array, and §4.2 preserves array
# order unless an owning contract declares set semantics.  The current Magic-10
# calculators consume these values as tuples in catalog order.  Freeze the exact
# ordered input contract here without sorting or deduplicating it.
FROZEN_MAGIC10_INPUTS = {
    "harmony": ("rapport_delta", "resonance_strength"),
    "heat": ("spark_intensity", "momentum_flux"),
    "communication": ("signal_clarity", "exchange_density"),
    "alignment": ("vector_cohesion", "axis_agreement"),
    "comfort": ("soothe_index", "buffer_resilience"),
    "consistency": ("pattern_integrity", "variance_stability"),
    "expansion": ("growth_tendency", "horizon_reach"),
    "creativity": ("novelty_factor", "expression_flow"),
    "drive": ("willpower_current", "focus_pressure"),
    "balance": ("equilibrium_score", "counterweight_ratio"),
}


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
class Manifest:
    root: str
    version: str
    built_at_utc: str
    files: tuple[ManifestEntry, ...]


@dataclass(frozen=True)
class RegistryConfig:
    gates: dict[int, Gate]
    channels: dict[str, Channel]
    alias_map: dict[str, str]
    magic10_order: tuple[str, ...]
    magic10_caps: dict[str, Magic10Caps]
    magic10_seeds: dict[str, Magic10Seed]
    manifest: Manifest
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
    center_counts = {
        center: sum(gate.center == center for gate in gates.values())
        for center in sorted(centers)
    }
    if center_counts != FROZEN_GATE_CENTER_COUNTS:
        raise SchemaValidationError(
            "GATE_CENTER_COUNTS_MISMATCH",
            "gate center counts must match the frozen topology",
            {
                "actual": center_counts,
                "expected": dict(FROZEN_GATE_CENTER_COUNTS),
            },
        )
    return gates, tuple(sorted(centers))


def _normalize_channel_id(channel_id: str, gates: Iterable[int]) -> str:
    if not re.match(r"^\d{2}-\d{2}$", channel_id):
        raise SchemaValidationError("INVALID_CHANNEL_ID", f"invalid channel id format: {channel_id}")
    a, b = map(int, channel_id.split("-"))
    g1, g2 = sorted(int(g) for g in gates)
    if g1 == g2:
        raise SchemaValidationError(
            "DUPLICATE_CHANNEL_GATE",
            f"channel {channel_id} must reference two distinct gates",
        )
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
        projected_centers = {gate_map[g].center for g in gates_tuple}
        if len(projected_centers) != 2:
            raise SchemaValidationError(
                "DUPLICATE_CHANNEL_CENTER",
                f"channel {normalized_id} gate projection must contain two distinct centers",
            )
        if set(centers_tuple) != projected_centers:
            raise SchemaValidationError(
                "CHANNEL_CENTER_PROJECTION_MISMATCH",
                f"channel {normalized_id} centers do not match its gate projection",
            )
        expected_endpoints_raw = FROZEN_CHANNEL_ENDPOINT_CENTERS.get(normalized_id)
        expected_endpoints = (
            dict(expected_endpoints_raw) if expected_endpoints_raw is not None else None
        )
        actual_endpoints = {gate: gate_map[gate].center for gate in gates_tuple}
        if expected_endpoints is not None and actual_endpoints != expected_endpoints:
            raise SchemaValidationError(
                "CHANNEL_CENTER_IDENTITY_MISMATCH",
                f"channel {normalized_id} endpoints do not match the frozen Channel topology",
                {
                    "actual": [
                        [gate, actual_endpoints[gate]] for gate in sorted(actual_endpoints)
                    ],
                    "expected": [
                        [gate, expected_endpoints[gate]]
                        for gate in sorted(expected_endpoints)
                    ],
                },
            )
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

    actual_channel_ids = set(channels)
    expected_channel_ids = set(FROZEN_CHANNEL_IDS)
    if set(FROZEN_CHANNEL_ENDPOINT_CENTERS) != expected_channel_ids:
        raise SchemaValidationError(
            "FROZEN_CHANNEL_CENTER_ROSTER_MISMATCH",
            "frozen Channel center bindings must cover the exact Channel roster",
        )
    if actual_channel_ids != expected_channel_ids:
        missing = sorted(expected_channel_ids - actual_channel_ids)
        unknown = sorted(actual_channel_ids - expected_channel_ids)
        raise SchemaValidationError(
            "CHANNEL_ID_ROSTER_MISMATCH",
            "channel identities must match the frozen 36-Channel roster",
            {"missing": missing, "unknown": unknown},
        )

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
    if not isinstance(order_raw, dict) or set(order_raw) != {"order"}:
        raise SchemaValidationError("INVALID_MAGIC10", "magic10.json must contain an order array")
    order_list = order_raw.get("order")
    if not isinstance(order_list, list):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10 order must be a list")
    magic_order = tuple(order_list)
    if magic_order != FROZEN_MAGIC10_ORDER:
        raise SchemaValidationError("MAGIC10_ORDER_MISMATCH", "magic10 order must match registry")
    if set(FROZEN_MAGIC10_INPUTS) != set(magic_order):
        raise SchemaValidationError(
            "FROZEN_MAGIC10_INPUT_ROSTER_MISMATCH",
            "frozen Magic-10 input bindings must cover the exact category roster",
        )

    caps_raw = _load_json(root / "catalog" / "magic10_caps.json")
    if not isinstance(caps_raw, dict):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10_caps must be an object")
    if set(caps_raw.keys()) != set(magic_order):
        raise SchemaValidationError("MAGIC10_CAPS_COVERAGE", "magic10_caps must cover full magic10 order")
    caps: dict[str, Magic10Caps] = {}
    for key, entry in caps_raw.items():
        if not isinstance(entry, dict) or set(entry) != {"inputs", "bounds"}:
            raise SchemaValidationError(
                "INVALID_MAGIC10", "magic10_caps entries must contain inputs and bounds only"
            )
        inputs = entry.get("inputs")
        bounds = entry.get("bounds")
        if not isinstance(inputs, list) or not inputs:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] inputs must be a non-empty list")
        if any(not isinstance(value, str) or not value for value in inputs):
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_caps[{key}] inputs must be non-empty strings"
            )
        expected_inputs = FROZEN_MAGIC10_INPUTS[key]
        if tuple(inputs) != expected_inputs:
            raise SchemaValidationError(
                "MAGIC10_INPUTS_MISMATCH",
                f"magic10_caps[{key}] inputs must match the frozen ordered contract",
                {
                    "actual": list(inputs),
                    "expected": list(expected_inputs),
                },
            )
        if not isinstance(bounds, dict) or set(bounds) != {"min", "max"}:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] bounds invalid")
        minimum = bounds["min"]
        maximum = bounds["max"]
        if (
            type(minimum) is not int
            or type(maximum) is not int
            or minimum != 0
            or maximum != 100
        ):
            raise SchemaValidationError(
                "INVALID_MAGIC10",
                f"magic10_caps[{key}] bounds must be integers with min 0 and max 100",
            )
        caps[key] = Magic10Caps(
            inputs=tuple(inputs), bounds={"min": minimum, "max": maximum}
        )

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
        if set(entry) != required:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] fields invalid"
            )
        if any(not isinstance(entry[field], str) or not entry[field] for field in required):
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] values must be non-empty strings"
            )
        checksum = entry["checksum_sha256"]
        if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] checksum invalid"
            )
        timestamp = entry["updated_at_utc"]
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", timestamp) is None:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] timestamp invalid"
            )
        try:
            datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError as exc:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] timestamp invalid"
            ) from exc
        seeds[key] = Magic10Seed(
            template_id=entry["template_id"],
            seed_version=entry["seed_version"],
            updated_at_utc=timestamp,
            checksum_sha256=checksum,
        )

    return magic_order, caps, seeds


def _parse_manifest(raw: object) -> Manifest:
    if not isinstance(raw, dict):
        raise SchemaValidationError("INVALID_MANIFEST", "manifest.json must be an object")
    expected_keys = {"root", "version", "built_at_utc", "files"}
    if set(raw.keys()) != expected_keys:
        raise SchemaValidationError(
            "INVALID_MANIFEST_KEYS",
            "manifest.json must contain exactly root, version, built_at_utc, files",
        )

    root = raw.get("root")
    version = raw.get("version")
    built_at_utc = raw.get("built_at_utc")
    files_raw = raw.get("files")

    if root != "catalog/":
        raise SchemaValidationError("INVALID_MANIFEST_ROOT", "manifest root must be 'catalog/'")
    if not isinstance(version, str) or not version:
        raise SchemaValidationError("INVALID_MANIFEST_VERSION", "manifest version must be a non-empty string")
    if not isinstance(built_at_utc, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", built_at_utc):
        raise SchemaValidationError(
            "INVALID_MANIFEST_TIMESTAMP", "built_at_utc must be an ISO-8601 UTC timestamp ending with Z"
        )
    if not isinstance(files_raw, list):
        raise SchemaValidationError("INVALID_MANIFEST", "manifest files must be a list")

    manifest_entries: list[ManifestEntry] = []
    seen_paths: set[str] = set()
    last_path: str | None = None
    for entry in files_raw:
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file entry must be an object")
        if set(entry.keys()) != {"path", "sha256", "size"}:
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file entry must contain path, sha256, size only")

        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size")
        if not isinstance(path, str) or not path:
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file path must be a non-empty string")
        if path == "catalog/manifest.json":
            raise SchemaValidationError("SELF_LISTING_MANIFEST_FORBIDDEN", "manifest.json must not list itself")
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha):
            raise SchemaValidationError("INVALID_MANIFEST", f"manifest sha256 invalid for {path}")
        if not isinstance(size, int) or size < 0:
            raise SchemaValidationError("INVALID_MANIFEST", f"manifest size invalid for {path}")
        if path in seen_paths:
            raise DuplicateIdError("DUPLICATE_MANIFEST_ENTRY", f"duplicate manifest path {path}")
        if last_path is not None and path <= last_path:
            raise SchemaValidationError("INVALID_MANIFEST_ORDER", "manifest files must be ASCII-sorted and deduped by path")

        seen_paths.add(path)
        last_path = path
        manifest_entries.append(ManifestEntry(path=path, sha256=sha, size=size))

    return Manifest(
        root=str(root),
        version=str(version),
        built_at_utc=str(built_at_utc),
        files=tuple(manifest_entries),
    )


def load_manifest(root: Path | str | None = None) -> Manifest:
    base = Path(root) if root is not None else Path.cwd()
    raw = _load_json(base / "catalog" / "manifest.json")
    return _parse_manifest(raw)


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
    manifest = load_manifest(base)

    return RegistryConfig(
        gates=gates,
        channels=channels,
        alias_map=alias_map,
        magic10_order=magic10_order,
        magic10_caps=magic10_caps,
        magic10_seeds=magic10_seeds,
        manifest=manifest,
        centers=centers,
        domains=domains,
    )
