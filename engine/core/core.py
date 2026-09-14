"""Four-argument, data-in/data-out Gate kernel (PF01 §5.2 / PF14 §6.7)."""
from __future__ import annotations

from dataclasses import dataclass, fields
from hashlib import sha256
from types import MappingProxyType

from engine.bodygraph.gates import NormalizedGates
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.config.registry_loader import (
    ADMITTED_RELEASE_ROSTER, AdmittedMechanicsBundle, Channel, Gate,
    Magic10Caps, Magic10Seed, Manifest, ManifestEntry, RegistryConfig, SourceIdentity,
    FROZEN_CHANNEL_IDS,
)
from engine.magic10.calculators import CategoryValue, _reduce_category
from engine.magic10.composite import _classify_channels
from engine.magic10.signals import SignalValue, _compute_signals
from engine.serializer.canon import sercanon


@dataclass(frozen=True, slots=True)
class CoreResult:
    schema: str
    config_id: str
    release_id: str
    pair_key: str
    signals: tuple[SignalValue, ...]
    categories: tuple[CategoryValue, ...]

    def to_payload(self) -> dict:
        """Project immutable ordered values for the owning serializer/schema."""
        return {
            "schema": self.schema, "config_id": self.config_id,
            "release_id": self.release_id, "pair_key": self.pair_key,
            "signals": [{"signal_id": row.signal_id, "q": row.q} for row in self.signals],
            "categories": [{"category_id": row.category_id, "score": row.score,
                            "band": row.band} for row in self.categories],
        }


def _hex_digest(value) -> bool:
    return type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def _plain(value, depth=0):
    """Check the admitted graph's immutable value types while projecting scalars.

    This does not admit files, load schemas or freeze caller-owned containers.
    The depth bound also refuses forged cyclic mapping proxies.
    """
    if depth > 12:
        raise ValueError("invalid immutable graph")
    if type(value) in (str, int) or value is None:
        return value
    if type(value) is tuple:
        return [_plain(v, depth + 1) for v in value]
    if type(value) is MappingProxyType:
        if any(type(k) not in (str, int) for k in value):
            raise ValueError("invalid immutable keys")
        return {k: _plain(v, depth + 1) for k, v in value.items()}
    if type(value) in (
        AdmittedMechanicsBundle, RegistryConfig, Gate, Channel, Magic10Caps,
        Magic10Seed, Manifest, ManifestEntry, SourceIdentity,
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
            or tuple(row.path for row in manifest.files) != ADMITTED_RELEASE_ROSTER
            or tuple(row.path for row in identities) != ADMITTED_RELEASE_ROSTER):
        raise ValueError("incomplete admitted source identities")
    for entry, source in zip(manifest.files, identities):
        if (type(entry) is not ManifestEntry or type(source) is not SourceIdentity
                or not _hex_digest(source.sha256) or type(source.size) is not int or source.size <= 0
                or (entry.path, entry.sha256, entry.size) != (source.path, source.sha256, source.size)):
            raise ValueError("incoherent source identity")
    by_path = {row.path: row for row in identities}
    mechanics = bundle.mechanics
    if set(mechanics) != {
        "schema", "config_id", "result_schema", "signal_scale", "response_scale",
        "rounding", "sources", "profiles", "signals", "category_weights",
    }:
        raise ValueError("invalid mechanics fields")
    if (mechanics["schema"] != "magic10_mechanics_config.v1"
            or mechanics["result_schema"] != "magic10_result.v1"
            or type(mechanics["config_id"]) is not str or not mechanics["config_id"]
            or type(mechanics["signal_scale"]) is not int or mechanics["signal_scale"] != 2
            or type(mechanics["response_scale"]) is not int or mechanics["response_scale"] != 10000
            or dict(mechanics["rounding"]) != {"category": "round_half_up_once",
                                              "signal": "round_half_up_to_half_score_unit"}):
        raise ValueError("invalid mechanics invariants")
    config_bytes = sercanon(plain["mechanics"], sort_keys=True)
    config_source = by_path["catalog/magic10_mechanics_v1.json"]
    if (sha256(config_bytes).hexdigest() != bundle.config_sha256
            or bundle.config_sha256 != config_source.sha256 or len(config_bytes) != config_source.size):
        raise ValueError("incoherent configuration bytes")
    source_paths = (
        ("caps", "catalog/magic10_caps.json"), ("categories", "catalog/magic10.json"),
        ("channels", "catalog/channels_v1.json"), ("thresholds", "math/thresholds.json"),
    )
    if set(mechanics["sources"]) != {name for name, _ in source_paths}:
        raise ValueError("invalid mechanics source roster")
    for name, path in source_paths:
        source = mechanics["sources"][name]
        if set(source) != {"path", "sha256"} or source["path"] != path or source["sha256"] != by_path[path].sha256:
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
    if any(_digest(value) != by_path[path].sha256 for path, value in projections.items()):
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
    weights = mechanics["category_weights"]
    if len(weights) != 10 or tuple(row["category_id"] for row in weights) != registry.magic10_order:
        raise ValueError("invalid category weight order")
    if any(set(row) != {"category_id", "reducer", "weights"} or
           row["reducer"] != "weighted_mean_half_unit_v1" for row in weights):
        raise ValueError("invalid category reducer")
    return tuple(order)


def _chart_fingerprint(member) -> str:
    return _digest({"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": member.mask_hex})


def _validate_result(result, signal_order, category_order):
    if (type(result) is not CoreResult or result.schema != "magic10_result.v1"
            or type(result.config_id) is not str or not result.config_id
            or not _hex_digest(result.release_id) or not _hex_digest(result.pair_key)
            or type(result.signals) is not tuple or type(result.categories) is not tuple
            or len(result.signals) != 20 or len(result.categories) != 10):
        raise ValueError("invalid result closure")
    for row, expected in zip(result.signals, signal_order):
        if (type(row) is not SignalValue or row.signal_id != expected
                or type(row.q) is not int or not 0 <= row.q <= 200):
            raise ValueError("invalid result signal")
    for row, expected in zip(result.categories, category_order):
        if (type(row) is not CategoryValue or row.category_id != expected
                or type(row.score) is not int or not 0 <= row.score <= 100):
            raise ValueError("invalid result category")
        band = ("Cool" if row.score <= 24 else "Open" if row.score <= 49
                else "Warm" if row.score <= 74 else "Glow")
        if type(row.band) is not str or row.band != band:
            raise ValueError("invalid result band")


def compute_core(member_a, member_b, mechanics_bundle, release_id) -> CoreResult:
    """Compute one complete intrinsic result; eligibility belongs to the caller."""
    try:
        _validate_member(member_a)
        _validate_member(member_b)
        signal_order = _validate_bundle(mechanics_bundle, release_id)
        registry, mechanics = mechanics_bundle.registry, mechanics_bundle.mechanics
        classified = _classify_channels(member_a.mask, member_b.mask, registry.channels)
        signals = _compute_signals(classified, mechanics, signal_order)
        values = {row.signal_id: row.q for row in signals}
        categories = tuple(
            _reduce_category(
                category, tuple(values[s] for s in registry.magic10_caps[category].inputs),
                registry.magic10_caps[category].bounds, row["weights"],
            )
            for category, row in zip(registry.magic10_order, mechanics["category_weights"])
        )
        members = sorted((member_a, member_b), key=lambda member: member.mask)
        pair_key = _digest({
            "schema": "magic10_pair_preimage.v1",
            "members": [_chart_fingerprint(member) for member in members],
            "config_id": mechanics["config_id"], "release_id": release_id,
            "result_schema": "magic10_result.v1",
        })
        result = CoreResult("magic10_result.v1", mechanics["config_id"], release_id,
                            pair_key, signals, categories)
        _validate_result(result, signal_order, registry.magic10_order)
        return result
    except (KeyError, TypeError, AttributeError, ValueError, RecursionError):
        raise ValueError("invalid pure core contract") from None
