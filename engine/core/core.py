"""Four-argument, data-in/data-out Gate kernel (PF01 §5.2 / PF14 §6.7).

HDE-EPIC043 WU-PR-09: the supported core computes ``magic10_result.v2`` through
the Magic10 v2 calculation over the admitted bundle's ``magic10_v2`` member.
"""
from __future__ import annotations

import sys as _sys
from dataclasses import fields
from hashlib import sha256
from types import MappingProxyType

from engine.bodygraph.gates import NormalizedGates
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.config.magic10_v2_loader import (
    MAGIC10_V2_CONFIGURATION_PATH, MAGIC10_V2_RESULT_SCHEMA, Magic10V2Bundle,
)
from engine.config.registry_loader import (
    AdmittedMechanicsBundle, Channel, Gate,
    Magic10Caps, Magic10Seed, Manifest, ManifestEntry, RegistryConfig, SourceIdentity,
    FROZEN_CHANNEL_IDS,
)
from engine.magic10_v2.calculation import CategoryResult, Magic10V2Result, assign_band, compute_magic10_v2
from engine.magic10_v2.signals import PER_MILLE, SignalValue
from engine.serializer.canon import sercanon


# The supported core result is the Magic10 v2 result (``magic10_result.v2``).
CoreResult = Magic10V2Result


def _hex_digest(value) -> bool:
    return type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def _plain(value, depth=0):
    """Check the admitted graph's immutable value types while projecting scalars.

    This does not admit files, load schemas or freeze caller-owned containers.
    The depth bound also refuses forged cyclic mapping proxies.
    """
    if depth > 12:
        raise ValueError("invalid immutable graph")
    if type(value) in (str, int, bool) or value is None:
        return value
    if type(value) is tuple:
        return [_plain(v, depth + 1) for v in value]
    if type(value) is MappingProxyType:
        if any(type(k) not in (str, int) for k in value):
            raise ValueError("invalid immutable keys")
        return {k: _plain(v, depth + 1) for k, v in value.items()}
    if type(value) in (
        AdmittedMechanicsBundle, RegistryConfig, Gate, Channel, Magic10Caps,
        Magic10Seed, Manifest, ManifestEntry, SourceIdentity, Magic10V2Bundle,
    ):
        return {f.name: _plain(getattr(value, f.name), depth + 1) for f in fields(value)}
    raise ValueError("invalid immutable value")


def _digest(value) -> str:
    return sha256(sercanon(value, sort_keys=True)).hexdigest()


def _validate_member(member):
    if type(member) is not NormalizedGates or type(member.gates) is not tuple or not member.gates:
        raise ValueError("invalid normalized member")
    if any(type(g) is not int or not 1 <= g <= 64 for g in member.gates):
        raise ValueError("invalid normalized Gates")
    if member.gates != tuple(sorted(set(member.gates))):
        raise ValueError("invalid normalized Gate order")
    mask = sum(1 << (g - 1) for g in member.gates)
    if type(member.mask) is not int or not 0 < member.mask < 2**64 or member.mask != mask:
        raise ValueError("invalid normalized mask")
    if type(member.mask_hex) is not str or member.mask_hex != f"{mask:016x}":
        raise ValueError("invalid normalized mask hex")


def _validate_bundle(bundle, release_id):
    if type(bundle) is not AdmittedMechanicsBundle or not _hex_digest(release_id):
        raise ValueError("invalid admitted bundle")
    plain = _plain(bundle)
    if (release_id != bundle.release_id or release_id != bundle.manifest_sha256
            or bundle.registry.manifest != bundle.manifest
            or _digest(plain["manifest"]) != release_id):
        raise ValueError("incoherent release identity")
    manifest = bundle.manifest
    identities = bundle.source_identities
    if (type(manifest) is not Manifest or type(bundle.registry) is not RegistryConfig
            or type(identities) is not tuple or not identities
            or tuple(row.path for row in manifest.files) != tuple(row.path for row in identities)):
        raise ValueError("incomplete admitted source identities")
    for entry, source in zip(manifest.files, identities):
        if (type(entry) is not ManifestEntry or type(source) is not SourceIdentity
                or not _hex_digest(source.sha256) or type(source.size) is not int or source.size <= 0
                or (entry.path, entry.sha256, entry.size) != (source.path, source.sha256, source.size)):
            raise ValueError("incoherent source identity")
    by_path = {row.path: row for row in identities}
    magic10_v2 = bundle.magic10_v2
    mechanics = bundle.mechanics
    if type(magic10_v2) is not Magic10V2Bundle or mechanics != magic10_v2.configuration:
        raise ValueError("incoherent v2 bundle")
    config_bytes = sercanon(plain["mechanics"], sort_keys=True)
    config_source = by_path.get(MAGIC10_V2_CONFIGURATION_PATH)
    if (config_source is None or sha256(config_bytes).hexdigest() != bundle.config_sha256
            or bundle.config_sha256 != config_source.sha256 or len(config_bytes) != config_source.size
            or magic10_v2.config_sha256 != bundle.config_sha256):
        raise ValueError("incoherent configuration bytes")
    if mechanics["result_schema"] != MAGIC10_V2_RESULT_SCHEMA:
        raise ValueError("invalid mechanics invariants")
    for name, source in mechanics["sources"].items():
        if (type(source) is not MappingProxyType or set(source) != {"path", "sha256"}
                or source["path"] not in by_path or source["sha256"] != by_path[source["path"]].sha256):
            raise ValueError("incoherent mechanics source")
    registry = bundle.registry
    if (registry.magic10_order != FROZEN_MAGIC10_ORDER
            or tuple(registry.channels) != FROZEN_CHANNEL_IDS
            or tuple(registry.gates) != tuple(range(1, 65))
            or registry.alias_map or set(registry.magic10_caps) != set(registry.magic10_order)):
        raise ValueError("incomplete registry")
    for key, gate in registry.gates.items():
        if type(gate) is not Gate or type(gate.gate) is not int or gate.gate != key:
            raise ValueError("invalid Gate registry")
    for key, channel in registry.channels.items():
        if (type(channel) is not Channel or channel.id != key or len(channel.gates) != 2
                or any(type(g) is not int or not 1 <= g <= 64 for g in channel.gates)
                or channel.gates[0] >= channel.gates[1]
                or key != "-".join(f"{g:02d}" for g in channel.gates)):
            raise ValueError("invalid Channel registry")
    integration = tuple(row.id for row in registry.channels.values() if row.substream == "integration")
    if (integration != ("10-20", "10-57", "20-34", "34-57")
            or registry.channels["10-34"].substream != "centering"
            or registry.channels["20-57"].substream != "knowing"):
        raise ValueError("invalid Integration taxonomy")
    # Bind the consumed typed projections to the already admitted source hashes.
    projections = {
        "catalog/gates_v1.json": {"gates": list(plain["registry"]["gates"].values())},
        "catalog/channels_v1.json": {"channels": list(plain["registry"]["channels"].values())},
        "catalog/magic10.json": {"order": list(registry.magic10_order)},
        "catalog/magic10_caps.json": plain["registry"]["magic10_caps"],
    }
    if any(path not in by_path or _digest(value) != by_path[path].sha256 for path, value in projections.items()):
        raise ValueError("incoherent typed source projection")
    order = []
    for category in registry.magic10_order:
        caps = registry.magic10_caps[category]
        if (type(caps) is not Magic10Caps or len(caps.inputs) != 2
                or any(type(s) is not str or not s for s in caps.inputs)):
            raise ValueError("invalid caps inputs")
        order.extend(caps.inputs)
    if len(order) != 20 or len(set(order)) != 20:
        raise ValueError("invalid caps closure")
    return tuple(order)


def _chart_fingerprint(member) -> str:
    return _digest({"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": member.mask_hex})


def _validate_result(result, bundle, release_id, signal_order, category_order):
    maxima = bundle.magic10_v2.maxima
    if (type(result) is not Magic10V2Result or result.schema != MAGIC10_V2_RESULT_SCHEMA
            or result.config_id != bundle.mechanics["config_id"]
            or result.release_id != release_id or not _hex_digest(result.pair_key)
            or type(result.signals) is not tuple or type(result.categories) is not tuple
            or len(result.signals) != 20 or len(result.categories) != 10):
        raise ValueError("invalid result closure")
    for row, expected in zip(result.signals, signal_order):
        if (type(row) is not SignalValue or row.signal_id != expected
                or type(row.q) is not int or not 0 <= row.q <= PER_MILLE):
            raise ValueError("invalid result signal")
    for row, expected in zip(result.categories, category_order):
        if (type(row) is not CategoryResult or row.category_id != expected
                or type(row.score) is not int or not 0 <= row.score <= 100):
            raise ValueError("invalid result category")
        if type(row.band) is not str or row.band != assign_band(row.score, maxima[expected]):
            raise ValueError("invalid result band")


def compute_core(member_a, member_b, mechanics_bundle, release_id) -> CoreResult:
    """Compute one complete intrinsic ``magic10_result.v2``; eligibility belongs to the caller.

    Member and bundle defects raise ``ValueError``.  A refusal of the Magic10 v2
    calculation (``SchemaValidationError``) propagates unchanged.
    """
    try:
        _validate_member(member_a)
        _validate_member(member_b)
        signal_order = _validate_bundle(mechanics_bundle, release_id)
    except (KeyError, TypeError, AttributeError, ValueError, RecursionError):
        raise ValueError("invalid pure core contract") from None
    result = compute_magic10_v2(member_a.mask, member_b.mask, mechanics_bundle.magic10_v2, release_id)
    try:
        _validate_result(result, mechanics_bundle, release_id, signal_order, mechanics_bundle.registry.magic10_order)
    except (KeyError, TypeError, AttributeError, ValueError, RecursionError):
        raise ValueError("invalid pure core contract") from None
    return result


# Retain passive top-level execution provenance only after definitions complete.
# Admission owns all source capture, compilation and equivalence validation.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None
