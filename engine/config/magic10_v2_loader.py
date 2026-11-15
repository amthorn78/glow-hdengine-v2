"""Fail-closed Magic-10 v2 loader and v2 configuration identity (inactive).

HDE-EPIC042 WU-PR-03; HDE Build Checklist — Separation, HDE-SEPA007.3 and
HDE-SEPA007.4. The loader admits the complete Magic-10 v2 bundle from a
repository root and the release's manifest rows, or refuses with a typed
``SchemaValidationError``. It reuses the v1 loader's safe-read helpers and v1
topology registry without changing them, validates the v2 inputs with its own
strict validator (the v1 owning-schema set is a release member), and applies the
v2 loader closure of HDE Schemas and Artifacts §2.9 and HDE Math Spec §5.2.11:
the v1 rules v2 keeps, the four relaxed rules, the added rules, and the pinned
v2.0.0 content (the analogue of the v1 ``_validate_initial_mechanics``).

Nothing on the v1 path imports this module, and Magic-10 v1 stays the one
active configuration until the v2 cutover release (C-03). Before the cut the
governed configuration ``catalog/magic10_mechanics_v2.json`` and the v2
thresholds do not exist; tests admit labelled non-canon fixtures from temporary
roots, and an identity computed over them proves the procedure only. The new
``release_id``, the manifest cut and activation belong to HDE-DIST008.2 and
HDE-COAG003.6. This module reads no file at import.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Mapping, Sequence

import jsonschema
from jsonschema import validators
from jsonschema.exceptions import SchemaError, best_match
from referencing import Registry
from referencing.exceptions import Unresolvable

from engine.config.registry_loader import (
    _PROFILE_RESPONSES,
    _SIGNAL_MEMBERSHIP,
    ManifestEntry,
    RegistryConfig,
    RegistryConfigError,
    SchemaValidationError,
    SourceIdentity,
    _deep_freeze,
    _freeze_manifest,
    _freeze_registry,
    _load_channels,
    _load_gates,
    _load_magic10,
    _LocalCapture,
    _parse_manifest,
    _reject_schema_retrieval,
    _schema_references,
    _validate_release_schema_document,
)
from engine.serializer import canon

# HDE Schemas and Artifacts §2.9 "Identities"; HDE Math Spec §5.2.11 and §5.2.1.
MAGIC10_V2_CONFIG_ID = "m10-relevance-centers-type-v2.0.0"
MAGIC10_V2_CONFIG_SCHEMA = "magic10_mechanics_config.v2"
MAGIC10_V2_RESULT_SCHEMA = "magic10_result.v2"
MAGIC10_V2_COMPAT_RESULT_SCHEMA = "magic10_compat_result.v2"
MAGIC10_V2_INTRINSIC_CACHE_PREFIX = "magic10:v2:"

# Written at the v2 release cut by HDE-DIST008.2; absent before it (INV-4).
MAGIC10_V2_CONFIGURATION_PATH = "catalog/magic10_mechanics_v2.json"

_SOURCE_PATHS = {
    "caps": "catalog/magic10_caps.json",
    "categories": "catalog/magic10.json",
    "centers": "catalog/centers_v1.json",
    "channels": "catalog/channels_v1.json",
    "thresholds": "math/thresholds.json",
    "type_pairing": "catalog/type_pairing_v1.json",
}
# The closed owning-schema set for the v2 data inputs.
_INSTANCE_SCHEMAS = {
    MAGIC10_V2_CONFIGURATION_PATH: "schemas/magic10_mechanics_v2.schema.json",
    "catalog/centers_v1.json": "schemas/centers_v1.schema.json",
    "catalog/type_pairing_v1.json": "schemas/type_pairing_v1.schema.json",
    "math/thresholds.json": "schemas/thresholds_v2.schema.json",
}
_RESULT_SCHEMA_PATHS = (
    "schemas/magic10_result_v2.schema.json",
    "schemas/magic10_compat_result_v2.schema.json",
)
# The Magic-10 mechanics configurations a release manifest can name; a release
# selects exactly one (HDE Schemas and Artifacts §2.9; HDE Math Spec §5.2.6).
_MECHANICS_CONFIGURATION_PATHS = frozenset({
    "catalog/magic10_mechanics_v1.json",
    MAGIC10_V2_CONFIGURATION_PATH,
})

# HDE Schemas and Artifacts §5.1: every new Magic-10 v2 release member, declared
# for manifest membership at the cut, and the existing member whose row binds
# new bytes there.
MAGIC10_V2_DECLARED_MEMBERS = tuple(sorted({
    "catalog/centers_v1.json",
    MAGIC10_V2_CONFIGURATION_PATH,
    "catalog/type_pairing_v1.json",
    "engine/config/magic10_v2_loader.py",
    *_INSTANCE_SCHEMAS.values(),
    *_RESULT_SCHEMA_PATHS,
}))
MAGIC10_V2_REBOUND_MEMBERS = ("math/thresholds.json",)

_DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
_PAIR_KEY = re.compile(r"[0-9a-f]{64}")
_SOURCE_BUNDLE_PREIMAGE_SCHEMA = "magic10_source_bundle_preimage.v2"

# HDE Schemas and Artifacts §2.1: the four motor centers.
_MOTOR_CENTERS = frozenset({"ego", "root", "sacral", "solar_plexus"})

# The three required v1 profile orderings, which v2 keeps (strictly decreasing).
_PROFILE_ORDERINGS = {
    "activation_bp_v1": ("electromagnetic", "dominance", "companionship", "compromise", "none"),
    "coherence_bp_v1": ("companionship", "electromagnetic", "dominance", "compromise", "none"),
    "expression_bp_v1": ("electromagnetic", "companionship", "dominance", "compromise", "none"),
}

# Pinned v2.0.0 content. HDE Math Spec §5.2.11 "Configuration fields" and
# "Components"; the operation names are the v2 configuration schema's constants.
_PINNED_RESULT_FIELDS = {
    "config_id": MAGIC10_V2_CONFIG_ID,
    "schema": MAGIC10_V2_CONFIG_SCHEMA,
    "result_schema": MAGIC10_V2_RESULT_SCHEMA,
    "signal_scale": 10,
    "response_scale": 10000,
    "rounding": {
        "signal": "round_half_up_to_per_mille",
        "component": "round_half_up_to_per_mille",
        "category": "round_half_up_once",
    },
    "saturation_k_bp": 10000,
    "blend": {"channel": 60, "center": 25, "type": 15},
}
_ORDINARY_OPERATION = "saturating_state_sum_v2"
_BALANCE_OPERATIONS = {
    "equilibrium_score": "bilateral_owner_mass_v2",
    "counterweight_ratio": "mutual_state_share_v2",
}
_CENTER_PROFILES = (
    ("completion_bp_v2", {"mutual": 10000, "one_sided": 7500, "shared": 2500, "open": 0}),
    ("foundation_bp_v2", {"mutual": 5000, "one_sided": 7500, "shared": 10000, "open": 0}),
)
_CENTER_MAP = (
    ("harmony", "completion_bp_v2", {"g": 3, "solar_plexus": 2, "spleen": 1}),
    ("heat", "completion_bp_v2", {"sacral": 3, "solar_plexus": 2, "ego": 1, "root": 1, "motor_throat": 1}),
    ("communication", "completion_bp_v2", {"throat": 3, "ajna": 2, "head": 1}),
    ("alignment", "foundation_bp_v2", {"g": 3, "ajna": 1, "ego": 1}),
    ("comfort", "completion_bp_v2", {"spleen": 3, "solar_plexus": 2, "g": 1}),
    ("consistency", "foundation_bp_v2", {"sacral": 2, "root": 2, "spleen": 1}),
    ("expansion", "completion_bp_v2", {"head": 2, "root": 2, "sacral": 1}),
    ("creativity", "completion_bp_v2", {"throat": 2, "head": 2, "g": 1}),
    ("drive", "completion_bp_v2", {"root": 3, "ego": 2, "sacral": 1, "motor_throat": 2}),
    ("balance", "bilateral_completion_v2", {}),
)
# HDE Schemas and Artifacts §2.9 "Type-pairing catalog", in canon's order; the
# offsets are HDE Build Notes' offsets table, every other cell 0.
_AURA_CLASSES = ("generator", "projector", "manifestor", "reflector")
_PAIR_RULES = (
    "same_class",
    "generator_with_nonsacral",
    "generator_manifestor",
    "generator_projector",
    "projector_manifestor",
    "reflector_present",
)
_NONZERO_OFFSETS = {
    ("generator_projector", "communication"): 50,
    ("generator_projector", "alignment"): 50,
    ("projector_manifestor", "alignment"): -50,
}
_PINNED_ITEM_ORDER = (
    "config_id",
    "schema",
    "result_schema",
    "signal_scale",
    "response_scale",
    "rounding",
    "saturation_k_bp",
    "blend",
    "profiles",
    "center_profiles",
    "center_map",
    "signals",
)


@dataclass(frozen=True, slots=True)
class Magic10V2Bundle:
    """One admitted, deeply frozen Magic-10 v2 bundle (no release identity)."""

    registry: RegistryConfig
    centers: Mapping[str, bool]
    aura_classes: tuple[str, ...]
    type_pairing: Mapping[str, Mapping[str, int]]
    configuration: Mapping[str, object]
    maxima: Mapping[str, tuple[int, int, int, int]]
    config_sha256: str
    source_identities: tuple[SourceIdentity, ...]
    source_bundle_sha256: str


def magic10_v2_intrinsic_cache_key(pair_key: str) -> str:
    """Return the Magic-10 v2 intrinsic cache key ``magic10:v2:<pair_key>``.

    ``pair_key`` construction under v2 belongs to HDE-CONJ010.3; a real
    ``pair_key`` is a lowercase SHA-256 hex digest, and anything else is refused.
    """
    if not isinstance(pair_key, str) or _PAIR_KEY.fullmatch(pair_key) is None:
        raise SchemaValidationError(
            "M10V2_INVALID_PAIR_KEY", "pair_key must be a lowercase 64-character SHA-256 hex digest"
        )
    return MAGIC10_V2_INTRINSIC_CACHE_PREFIX + pair_key


def magic10_v2_source_bundle_sha256(source_identities: Sequence[SourceIdentity]) -> str:
    """Return the canonical source-bundle SHA-256 over path-sorted identities."""
    paths = [identity.path for identity in source_identities]
    if paths != sorted(set(paths)):
        raise SchemaValidationError(
            "M10V2_SOURCE_IDENTITY_ORDER", "source identities must be unique and ASCII-sorted by path"
        )
    preimage = {
        "config_id": MAGIC10_V2_CONFIG_ID,
        "schema": _SOURCE_BUNDLE_PREIMAGE_SCHEMA,
        "sources": [
            {"path": identity.path, "sha256": identity.sha256, "size": identity.size}
            for identity in source_identities
        ],
    }
    return hashlib.sha256(canon.sercanon(preimage, sort_keys=True)).hexdigest()


def _validate_v2_instance(capture: _LocalCapture, data_path: str, data: object) -> None:
    """Validate one v2 input against its owning schema: strict integers, no retrieval."""
    schema_path = _INSTANCE_SCHEMAS[data_path]
    schema = capture.read(schema_path).data
    if not isinstance(schema, dict) or schema.get("$schema") != _DRAFT_2020_12:
        raise SchemaValidationError(
            "M10V2_SCHEMA_DRAFT_MISMATCH", f"owning schema is not draft 2020-12: {schema_path}", {"schema": schema_path}
        )
    if schema.get("$id") != schema_path:
        raise SchemaValidationError(
            "M10V2_SCHEMA_IDENTITY_MISMATCH", f"owning schema identity mismatch: {schema_path}", {"schema": schema_path}
        )
    _schema_references(schema)
    base = jsonschema.Draft202012Validator
    strict = validators.extend(
        base, type_checker=base.TYPE_CHECKER.redefine("integer", lambda checker, value: type(value) is int)
    )
    try:
        strict.check_schema(schema)
    except SchemaError as exc:
        raise SchemaValidationError(
            "M10V2_SCHEMA_INVALID", f"owning schema is not a valid schema: {schema_path}", {"schema": schema_path}
        ) from exc
    try:
        error = best_match(strict(schema, registry=Registry(retrieve=_reject_schema_retrieval)).iter_errors(data))
    except RegistryConfigError:
        raise
    except Exception as exc:
        keyword = "$ref" if isinstance(exc, Unresolvable) else type(exc).__name__
        raise SchemaValidationError(
            "M10V2_SCHEMA_VALIDATION_FAILED",
            f"owning schema could not be applied: {schema_path}",
            {"schema": schema_path, "instance_path": "/", "keyword": keyword},
        ) from exc
    if error is not None:
        raise SchemaValidationError(
            "M10V2_SCHEMA_VALIDATION_FAILED",
            f"owning schema refused {data_path}: {schema_path}",
            {
                "schema": schema_path,
                "instance_path": "/" + "/".join(str(part) for part in error.absolute_path),
                "keyword": str(error.validator),
            },
        )


def _check_manifest_rows(manifest_rows: object) -> ManifestEntry:
    """Return the one v2 configuration row the supplied manifest rows select."""
    if not isinstance(manifest_rows, (tuple, list)) or any(type(row) is not ManifestEntry for row in manifest_rows):
        raise SchemaValidationError("M10V2_INVALID_MANIFEST_ROWS", "manifest rows must be a sequence of ManifestEntry")
    paths = [row.path for row in manifest_rows]
    if paths != sorted(set(paths)):
        raise SchemaValidationError("M10V2_INVALID_MANIFEST_ROWS", "manifest row paths must be unique and ASCII-sorted")
    configurations = [row for row in manifest_rows if row.path in _MECHANICS_CONFIGURATION_PATHS]
    selected = [row for row in configurations if row.path == MAGIC10_V2_CONFIGURATION_PATH]
    if not selected:
        raise SchemaValidationError(
            "M10V2_CONFIGURATION_ROW_MISSING", f"manifest rows do not bind {MAGIC10_V2_CONFIGURATION_PATH}"
        )
    if len(configurations) != 1:
        raise SchemaValidationError(
            "M10V2_MULTIPLE_CONFIGURATIONS", "manifest rows select more than one mechanics configuration"
        )
    return selected[0]


def _check_configuration_rules(config: Mapping[str, object], registry: RegistryConfig) -> None:
    """The kept and added rules a schema cannot express: order, sums, relations."""
    expected_signals = [signal for category in registry.magic10_order for signal in registry.magic10_caps[category].inputs]
    if [row["signal_id"] for row in config["signals"]] != expected_signals:
        raise SchemaValidationError("M10V2_SIGNAL_ORDER_MISMATCH", "signal order must flatten the exact ordered caps pairs")
    for row in config["signals"]:
        members = [channel["channel_id"] for channel in row["channels"]]
        if members != sorted(set(members)):
            raise SchemaValidationError(
                "M10V2_SIGNAL_MEMBERSHIP_INVALID",
                "signal Channels must be unique and ASCII-ordered",
                {"signal": row["signal_id"]},
            )
    if [row["profile_id"] for row in config["profiles"]] != sorted(_PROFILE_ORDERINGS):
        raise SchemaValidationError("M10V2_PROFILE_ROSTER_MISMATCH", "profiles must be the three v1 profiles in ASCII order")
    for row in config["profiles"]:
        values = [row["responses"][state] for state in _PROFILE_ORDERINGS[row["profile_id"]]]
        if any(earlier <= later for earlier, later in zip(values, values[1:])):
            raise SchemaValidationError(
                "M10V2_PROFILE_INEQUALITY_MISMATCH", "profile response ordering failed", {"profile": row["profile_id"]}
            )
    if [row["category_id"] for row in config["center_map"]] != list(registry.magic10_order):
        raise SchemaValidationError("M10V2_CENTER_MAP_ORDER_MISMATCH", "center_map rows must follow catalog/magic10.json")
    if sum(config["blend"].values()) != 100:
        raise SchemaValidationError("M10V2_BLEND_SUM_MISMATCH", "blend members must sum to 100")


def _expected_pinned_configuration(registry: RegistryConfig) -> dict[str, object]:
    all_channels = [{"channel_id": channel_id, "weight": 1} for channel_id in sorted(registry.channels)]
    signals = []
    for signal_id, (profile_id, channel_ids) in _SIGNAL_MEMBERSHIP.items():
        if signal_id in _BALANCE_OPERATIONS:
            signals.append({"signal_id": signal_id, "operation": _BALANCE_OPERATIONS[signal_id], "channels": all_channels})
        else:
            signals.append({
                "signal_id": signal_id,
                "operation": _ORDINARY_OPERATION,
                "profile_id": profile_id,
                "channels": [{"channel_id": channel_id, "weight": 1} for channel_id in channel_ids],
            })
    return {
        **_PINNED_RESULT_FIELDS,
        "profiles": [{"profile_id": name, "responses": responses} for name, responses in sorted(_PROFILE_RESPONSES.items())],
        "center_profiles": [{"profile_id": name, "responses": responses} for name, responses in _CENTER_PROFILES],
        "center_map": [
            {"category_id": category, "profile_id": profile, "weights": weights}
            for category, profile, weights in _CENTER_MAP
        ],
        "signals": signals,
    }


def _expected_type_pairing(registry: RegistryConfig) -> dict[str, object]:
    return {
        "aura_classes": list(_AURA_CLASSES),
        "rules": [
            {"rule_id": rule, "offsets": {category: _NONZERO_OFFSETS.get((rule, category), 0) for category in registry.magic10_order}}
            for rule in _PAIR_RULES
        ],
    }


def load_magic10_v2_bundle_from_root(root: Path | str, manifest_rows: Sequence[ManifestEntry]) -> Magic10V2Bundle:
    """Admit the complete Magic-10 v2 bundle under ``root``, or fail closed.

    Inputs are read at their fixed relative paths; the manifest rows are the one
    supplied argument, so no caller selects a configuration, weight, profile or
    band (HDE Schemas and Artifacts §2.9). Every refusal is a
    ``SchemaValidationError`` with a stable code.
    """
    # C0: one capture; every file is read once and verified again at the end.
    capture = _LocalCapture(Path(root))
    # C1: the release selects exactly one mechanics configuration, the v2 one.
    config_row = _check_manifest_rows(manifest_rows)
    # C2: the configuration's bytes match the manifest row.
    config_source = capture.read(MAGIC10_V2_CONFIGURATION_PATH)
    if config_source.sha256 != config_row.sha256:
        raise SchemaValidationError("M10V2_MANIFEST_HASH_MISMATCH", "configuration digest differs from its manifest row")
    if config_source.size_bytes != config_row.size:
        raise SchemaValidationError("M10V2_MANIFEST_SIZE_MISMATCH", "configuration size differs from its manifest row")
    config = config_source.data
    # C3: the configuration's own schema.
    _validate_v2_instance(capture, MAGIC10_V2_CONFIGURATION_PATH, config)
    # C4: every source binds its exact captured bytes.
    for name, path in _SOURCE_PATHS.items():
        source = capture.read(path)
        if config["sources"][name] != {"path": path, "sha256": source.sha256}:
            raise SchemaValidationError("M10V2_SOURCE_MISMATCH", f"source binding mismatch: {name}", {"source": name})
    # C5: the v1 topology registry, built as the v1 loader builds it.
    gates, centers = _load_gates(capture)
    channels, aliases, domains = _load_channels(
        capture, gate_map=gates, known_centers=set(centers), allow_aliases=False, alias_ledger=None
    )
    order, caps, seeds = _load_magic10(capture)
    manifest = _parse_manifest(capture.read("catalog/manifest.json").data)
    registry = RegistryConfig(gates, channels, aliases, order, caps, seeds, manifest, centers, domains)
    # C6: centers catalog.
    centers_catalog = capture.read("catalog/centers_v1.json").data
    _validate_v2_instance(capture, "catalog/centers_v1.json", centers_catalog)
    if {entry["center_id"] for entry in centers_catalog["centers"] if entry["motor"]} != _MOTOR_CENTERS:
        raise SchemaValidationError("M10V2_CENTER_MOTOR_MISMATCH", "motor flags differ from the four motor centers")
    # C7: Type-pairing catalog.
    type_pairing = capture.read("catalog/type_pairing_v1.json").data
    _validate_v2_instance(capture, "catalog/type_pairing_v1.json", type_pairing)
    # C8: per-category maxima, four strictly ascending integers ending at 100.
    thresholds = capture.read("math/thresholds.json").data
    _validate_v2_instance(capture, "math/thresholds.json", thresholds)
    for category in thresholds["categories"]:
        maxima = category["maxima"]
        if any(earlier >= later for earlier, later in zip(maxima, maxima[1:])):
            raise SchemaValidationError(
                "M10V2_MAXIMA_NOT_ASCENDING",
                "category maxima must be strictly ascending",
                {"category": category["category_id"]},
            )
    # C9: rules a schema cannot express.
    _check_configuration_rules(config, registry)
    # C10: pinned v2.0.0 content.
    expected = _expected_pinned_configuration(registry)
    for item in _PINNED_ITEM_ORDER:
        if config[item] != expected[item]:
            raise SchemaValidationError(
                "M10V2_PINNED_CONTENT_MISMATCH", f"pinned v2.0.0 content differs: {item}", {"item": item}
            )
    if type_pairing != _expected_type_pairing(registry):
        raise SchemaValidationError(
            "M10V2_PINNED_CONTENT_MISMATCH", "pinned v2.0.0 content differs: type_pairing", {"item": "type_pairing"}
        )
    # C11: the two result schemas as documents.
    for path in _RESULT_SCHEMA_PATHS:
        _validate_release_schema_document(capture, path, expected_draft=_DRAFT_2020_12, expected_identity=path)
    # C12: nothing changed during capture; freeze and identify.
    capture.verify_unchanged()
    identities = tuple(sorted(
        (
            SourceIdentity(path, capture.sources[path].sha256, capture.sources[path].size_bytes)
            for path in (MAGIC10_V2_CONFIGURATION_PATH, *_SOURCE_PATHS.values())
        ),
        key=lambda identity: identity.path,
    ))
    maxima_by_category = {entry["category_id"]: tuple(entry["maxima"]) for entry in thresholds["categories"]}
    return Magic10V2Bundle(
        registry=_freeze_registry(registry, _freeze_manifest(manifest)),
        centers=MappingProxyType({entry["center_id"]: entry["motor"] for entry in centers_catalog["centers"]}),
        aura_classes=tuple(type_pairing["aura_classes"]),
        type_pairing=_deep_freeze({rule["rule_id"]: rule["offsets"] for rule in type_pairing["rules"]}),
        configuration=_deep_freeze(config),
        maxima=MappingProxyType({category: maxima_by_category[category] for category in registry.magic10_order}),
        config_sha256=config_source.sha256,
        source_identities=identities,
        source_bundle_sha256=magic10_v2_source_bundle_sha256(identities),
    )
