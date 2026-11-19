"""Magic10 v2 calculation (HDE-CONJ010.3; HDE-EPIC043 WU-PR-02).

HDE Math Spec §5.2.11, evaluation steps 1 to 10, and §5.3.7: from two gate
masks, an admitted v2 bundle and an explicit ``release_id``, produce the
complete ``magic10_result.v2`` value.

* Steps 1 to 5 are the v2 kernel's (``compute_kernel``) and step 6 the signal
  producers' (``compute_signals``). This module computes, for each category in
  the governed order, the Channel component ``C_k``, the center component
  ``Z_k``, the pairwise Type component ``T_k``, the score (``0`` when
  ``C_k = 0`` and ``Z_k = 0``) and the band from that category's own inclusive
  maxima, then ``pair_key`` under ``m10-relevance-centers-type-v2.0.0``.
* Weights, profiles, offsets, the blend, scales and maxima are read from the
  bundle; none is a literal here. ``release_id`` is an explicit argument: the
  bundle carries no release identity.
* Arithmetic is integer only; no binary floating point is used.
* Every order is fixed by the configuration, the registry or the centers
  catalog, and every predicate is symmetric, so the result for (A, B) equals the
  result for (B, A). Nothing is read from a file, the environment or a clock.
* A missing or malformed input this module reads fails closed with a
  ``SchemaValidationError`` carrying a stable code; nothing is defaulted.

Stated limits: what the v2 loader pins (the topology, the order of the
``center_map`` rows, the blend sum) is not re-validated; no eligibility rule is
applied (HDE Math Spec §4 is upstream). The two clamps, ``T_k`` to ``0..1000``
and the score to ``0..100``, cannot act on any admitted configuration (the
pinned offsets keep ``500 + Σ I`` in ``450..550`` and the score in ``0..93``);
they are implemented as canon states them. The cache key, the compat envelope
and every surface belong to later work units.

Reached from production since the switch (HDE-EPIC043 WU-PR-09), through the
engine core; its last top-level statement records passive execution provenance
for release admission.
"""
from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from dataclasses import dataclass

from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIG_ID, MAGIC10_V2_RESULT_SCHEMA, Magic10V2Bundle
from engine.config.registry_loader import SchemaValidationError, _capture_module_execution
from engine.magic10_v2.kernel import CENTER_OUTCOMES, KernelResult, compute_kernel
from engine.magic10_v2.signals import PER_MILLE, SignalValue, compute_signals, rhu
from engine.serializer.canon import sercanon

# HDE Math Spec §5.2.11, "Type component, pairwise only", and step 8.
TYPE_MIDPOINT = 500
SCORE_MAX = 100
# HDE Math Spec §5.3.7, in ascending order.
BANDS = ("Cool", "Open", "Warm", "Glow")
# HDE Math Spec §5.2.11: the closed pair-rule set, in canon's order.
PAIR_RULES = (
    "same_class",
    "generator_with_nonsacral",
    "generator_manifestor",
    "generator_projector",
    "projector_manifestor",
    "reflector_present",
)
# The balance center profile and the one non-center center-map key.
BALANCE_CENTER_PROFILE = "bilateral_completion_v2"
MOTOR_THROAT_KEY = "motor_throat"

_CHART_FINGERPRINT_SCHEMA = "magic10_chart_fingerprint.v1"
_PAIR_PREIMAGE_SCHEMA = "magic10_pair_preimage.v1"
_HEX_DIGEST = re.compile(r"[0-9a-f]{64}")
_BLEND_KEYS = ("channel", "center", "type")

RELEASE_ID_INVALID = "M10V2_CALC_RELEASE_ID_INVALID"
INPUT_INVALID = "M10V2_CALC_INPUT_INVALID"
BUNDLE_INCOMPLETE = "M10V2_CALC_BUNDLE_INCOMPLETE"
CENTER_MAP_INVALID = "M10V2_CALC_CENTER_MAP_INVALID"
CENTER_PROFILE_MISSING = "M10V2_CALC_CENTER_PROFILE_MISSING"
TYPE_PAIRING_INVALID = "M10V2_CALC_TYPE_PAIRING_INVALID"
MAXIMA_INVALID = "M10V2_CALC_MAXIMA_INVALID"


@dataclass(frozen=True, slots=True)
class CategoryComponents:
    """One category's components, score and band (internal; never a result field)."""

    category_id: str
    channel_component: int
    center_component: int
    type_component: int
    score: int
    band: str


@dataclass(frozen=True, slots=True)
class CategoryResult:
    """One ``magic10_result.v2`` category row."""

    category_id: str
    score: int
    band: str


@dataclass(frozen=True, slots=True)
class Magic10V2Result:
    """The complete ``magic10_result.v2`` value for one pair."""

    schema: str
    config_id: str
    release_id: str
    pair_key: str
    signals: tuple[SignalValue, ...]
    categories: tuple[CategoryResult, ...]

    def as_payload(self) -> dict[str, object]:
        """Return a new plain object with exactly the ``magic10_result.v2`` fields."""
        return {
            "schema": self.schema,
            "config_id": self.config_id,
            "release_id": self.release_id,
            "pair_key": self.pair_key,
            "signals": [{"signal_id": signal.signal_id, "q": signal.q} for signal in self.signals],
            "categories": [
                {"category_id": category.category_id, "score": category.score, "band": category.band}
                for category in self.categories
            ],
        }


@dataclass(frozen=True, slots=True)
class _CenterRow:
    profile_id: str
    responses: Mapping[str, int] | None
    weights: tuple[tuple[str, int], ...]


@dataclass(frozen=True, slots=True)
class _Inputs:
    order: tuple[str, ...]
    caps: Mapping[str, tuple[str, str]]
    center_rows: Mapping[str, _CenterRow]
    offsets: Mapping[str, Mapping[str, int]]
    maxima: Mapping[str, tuple[int, int, int, int]]
    blend: Mapping[str, int]
    response_scale: int
    signal_ids: tuple[str, ...]


def pair_rules(class_a: str, class_b: str) -> tuple[str, ...]:
    """HDE Math Spec §5.2.11: the pair rules whose symmetric predicate holds, in canon's order."""
    classes = {class_a, class_b}
    holds = {
        "same_class": class_a == class_b,
        "generator_with_nonsacral": (class_a == "generator") != (class_b == "generator"),
        "generator_manifestor": classes == {"generator", "manifestor"},
        "generator_projector": classes == {"generator", "projector"},
        "projector_manifestor": classes == {"projector", "manifestor"},
        "reflector_present": "reflector" in classes,
    }
    return tuple(rule for rule in PAIR_RULES if holds[rule])


def type_component(offset_sum: int) -> int:
    """HDE Math Spec §5.2.11: ``T_k = min(1000, max(0, 500 + Σ I_k[rule]))``."""
    return min(PER_MILLE, max(0, TYPE_MIDPOINT + offset_sum))


def category_score(
    channel_component: int, center_component: int, type_component: int, blend: Mapping[str, int]
) -> int:
    """HDE Math Spec §5.2.11, step 8, with the zero rule and the ``0..100`` clamp."""
    if channel_component == 0 and center_component == 0:
        return 0
    blended = blend["channel"] * channel_component + blend["center"] * center_component + blend["type"] * type_component
    return min(SCORE_MAX, max(0, rhu(blended, PER_MILLE)))


def assign_band(score: int, maxima: tuple[int, int, int, int]) -> str:
    """HDE Math Spec §5.3.7: the band from one category's inclusive maxima ``[c1, c2, c3, 100]``."""
    first, second, third, _ = maxima
    if score <= first:
        return "Cool"
    if score <= second:
        return "Open"
    if score <= third:
        return "Warm"
    return "Glow"


def compute_category_components(
    kernel: KernelResult, signals: tuple[SignalValue, ...], bundle: Magic10V2Bundle
) -> tuple[CategoryComponents, ...]:
    """HDE Math Spec §5.2.11 steps 7 to 9 for every category, in the governed order.

    ``kernel`` and ``signals`` must come from ``bundle`` (``compute_magic10_v2``
    guarantees it). Refusals: ``M10V2_CALC_INPUT_INVALID`` for the kernel, then
    the bundle checks of ``compute_magic10_v2``, then
    ``M10V2_CALC_INPUT_INVALID`` for the signals.
    """
    if type(kernel) is not KernelResult:
        raise SchemaValidationError(INPUT_INVALID, "components require a KernelResult", {"argument": "kernel"})
    inputs = _check_bundle(bundle)
    if (
        type(signals) is not tuple
        or any(type(signal) is not SignalValue for signal in signals)
        or tuple(signal.signal_id for signal in signals) != inputs.signal_ids
    ):
        raise SchemaValidationError(
            INPUT_INVALID, "components require the configuration's signals in order", {"argument": "signals"}
        )
    q = {signal.signal_id: signal.q for signal in signals}
    outcomes = {center.center_id: center.outcome for center in kernel.centers}
    gives_lo, gives_hi = _gives(kernel)
    rules = pair_rules(kernel.member_lo.aura_class, kernel.member_hi.aura_class)
    components = []
    for category in inputs.order:
        first, second = inputs.caps[category]
        channel = rhu(q[first] + q[second], 2)
        center = _center_component(
            inputs.center_rows[category],
            outcomes,
            kernel.motor_throat.outcome,
            gives_lo,
            gives_hi,
            inputs.response_scale,
        )
        type_value = type_component(sum(inputs.offsets[rule][category] for rule in rules))
        score = category_score(channel, center, type_value, inputs.blend)
        band = assign_band(score, inputs.maxima[category])
        components.append(CategoryComponents(category, channel, center, type_value, score, band))
    return tuple(components)


def compute_magic10_v2(mask_a: int, mask_b: int, bundle: Magic10V2Bundle, release_id: str) -> Magic10V2Result:
    """Compute the complete ``magic10_result.v2`` value for two gate masks.

    Refusals (``SchemaValidationError``), in this order, before any result
    exists: ``M10V2_CALC_RELEASE_ID_INVALID``; the bundle checks
    (``M10V2_CALC_BUNDLE_INCOMPLETE``, ``M10V2_CALC_CENTER_MAP_INVALID``,
    ``M10V2_CALC_CENTER_PROFILE_MISSING``, ``M10V2_CALC_TYPE_PAIRING_INVALID``,
    ``M10V2_CALC_MAXIMA_INVALID``); then the kernel's ``M10V2_KERNEL_*`` and the
    signals' ``M10V2_SIGNALS_*`` refusals, propagated unchanged.
    """
    if type(release_id) is not str or _HEX_DIGEST.fullmatch(release_id) is None:
        raise SchemaValidationError(
            RELEASE_ID_INVALID,
            "release_id must be a lowercase 64-character hexadecimal digest",
            {"argument": "release_id"},
        )
    _check_bundle(bundle)
    kernel = compute_kernel(mask_a, mask_b, bundle)  # steps 1 to 5
    signals = compute_signals(kernel, bundle)  # step 6
    components = compute_category_components(kernel, signals, bundle)  # steps 7 to 9
    configuration = bundle.configuration
    mask_lo, mask_hi = (mask_a, mask_b) if mask_a <= mask_b else (mask_b, mask_a)
    pair_key = _pair_key(mask_lo, mask_hi, configuration["config_id"], release_id, configuration["result_schema"])
    return Magic10V2Result(
        schema=configuration["result_schema"],
        config_id=configuration["config_id"],
        release_id=release_id,
        pair_key=pair_key,
        signals=signals,
        categories=tuple(CategoryResult(item.category_id, item.score, item.band) for item in components),
    )


def _gives(kernel: KernelResult) -> tuple[int, int]:
    """HDE Math Spec §5.2.11, center outcomes: ``gives`` over the nine centers only."""
    gives_lo = gives_hi = 0
    for center in kernel.centers:
        if center.outcome == "mutual":
            gives_lo += 1
            gives_hi += 1
        elif center.outcome == "one_sided":
            if center.owner == "member_lo":
                gives_lo += 1
            else:
                gives_hi += 1
    return gives_lo, gives_hi


def _center_component(
    row: _CenterRow, outcomes: Mapping[str, str], motor_throat: str, gives_lo: int, gives_hi: int, response_scale: int
) -> int:
    """HDE Math Spec §5.2.11, "Center component"."""
    if row.profile_id == BALANCE_CENTER_PROFILE:
        if gives_lo + gives_hi == 0:
            return 0
        return rhu(PER_MILLE * 2 * min(gives_lo, gives_hi), gives_lo + gives_hi)
    total = weight_sum = 0
    for key, weight in row.weights:
        outcome = motor_throat if key == MOTOR_THROAT_KEY else outcomes[key]
        total += weight * row.responses[outcome]
        weight_sum += weight
    return rhu(PER_MILLE * total, response_scale * weight_sum)


def _chart_fingerprint(mask: int) -> str:
    """HDE Math Spec §5.2.2: ``sha256(canonical_bytes({"schema", "gate_mask_hex"}))``."""
    preimage = {"schema": _CHART_FINGERPRINT_SCHEMA, "gate_mask_hex": format(mask, "016x")}
    return hashlib.sha256(sercanon(preimage, sort_keys=True)).hexdigest()


def _pair_key(mask_lo: int, mask_hi: int, config_id: str, release_id: str, result_schema: str) -> str:
    """HDE Math Spec §5.2.2 and its v2 identity statement; equal masks give two equal members."""
    preimage = {
        "schema": _PAIR_PREIMAGE_SCHEMA,
        "members": [_chart_fingerprint(mask_lo), _chart_fingerprint(mask_hi)],
        "config_id": config_id,
        "release_id": release_id,
        "result_schema": result_schema,
    }
    return hashlib.sha256(sercanon(preimage, sort_keys=True)).hexdigest()


def _is_int(value: object) -> bool:
    return type(value) is int


def _incomplete(component: str, **extra: str) -> SchemaValidationError:
    return SchemaValidationError(
        BUNDLE_INCOMPLETE, f"bundle lacks a valid {component}", {"component": component, **extra}
    )


def _check_bundle(bundle: object) -> _Inputs:
    """Validate every bundle component this module reads; return them parsed."""
    if type(bundle) is not Magic10V2Bundle:
        raise _incomplete("bundle")
    configuration = bundle.configuration
    if not isinstance(configuration, Mapping):
        raise _incomplete("configuration")
    if configuration.get("config_id") != MAGIC10_V2_CONFIG_ID:
        raise _incomplete("configuration.config_id")
    if configuration.get("result_schema") != MAGIC10_V2_RESULT_SCHEMA:
        raise _incomplete("configuration.result_schema")
    blend = configuration.get("blend")
    if not isinstance(blend, Mapping) or any(not _is_int(blend.get(key)) or blend[key] < 0 for key in _BLEND_KEYS):
        raise _incomplete("configuration.blend")
    response_scale = configuration.get("response_scale")
    if not _is_int(response_scale) or response_scale <= 0:
        raise _incomplete("configuration.response_scale")
    center_profiles = configuration.get("center_profiles")
    if type(center_profiles) is not tuple or any(
        not isinstance(row, Mapping) or not isinstance(row.get("responses"), Mapping) for row in center_profiles
    ):
        raise _incomplete("configuration.center_profiles")
    center_map = configuration.get("center_map")
    if type(center_map) is not tuple or any(
        not isinstance(row, Mapping) or not isinstance(row.get("weights"), Mapping) for row in center_map
    ):
        raise _incomplete("configuration.center_map")
    signals = configuration.get("signals")
    if type(signals) is not tuple or any(not isinstance(row, Mapping) for row in signals):
        raise _incomplete("configuration.signals")
    signal_ids = tuple(row.get("signal_id") for row in signals)
    if not isinstance(bundle.centers, Mapping):
        raise _incomplete("centers")
    order = tuple(getattr(bundle.registry, "magic10_order", ()) or ())
    if not order:
        raise _incomplete("registry.magic10_order")
    caps_source = getattr(bundle.registry, "magic10_caps", None)
    caps = {}
    for category in order:
        entry = caps_source.get(category) if isinstance(caps_source, Mapping) else None
        inputs = tuple(getattr(entry, "inputs", ()) or ())
        if len(inputs) != 2 or any(signal_id not in signal_ids for signal_id in inputs):
            raise _incomplete("registry.magic10_caps", category_id=category)
        caps[category] = inputs
    profiles = {row.get("profile_id"): row["responses"] for row in center_profiles}
    rows = {}
    for row in center_map:
        rows.setdefault(row.get("category_id"), row)
    center_rows = {category: _center_row(category, rows.get(category), profiles, bundle.centers) for category in order}
    return _Inputs(
        order=order,
        caps=caps,
        center_rows=center_rows,
        offsets=_check_type_pairing(bundle.type_pairing, order),
        maxima=_check_maxima(bundle.maxima, order),
        blend=blend,
        response_scale=response_scale,
        signal_ids=signal_ids,
    )


def _center_row(category: str, row: Mapping | None, profiles: Mapping, centers: Mapping) -> _CenterRow:
    if row is None:
        raise SchemaValidationError(
            CENTER_MAP_INVALID, "a category has no center-map row", {"category_id": category, "key": None}
        )
    profile_id, weights = row.get("profile_id"), row["weights"]
    if profile_id == BALANCE_CENTER_PROFILE:
        if weights:
            raise SchemaValidationError(
                CENTER_MAP_INVALID,
                "the balance center profile takes no weights",
                {"category_id": category, "key": next(iter(weights))},
            )
        return _CenterRow(profile_id, None, ())
    responses = profiles.get(profile_id)
    if responses is None:
        raise SchemaValidationError(
            CENTER_PROFILE_MISSING, "center profile is absent", {"category_id": category, "profile_id": profile_id}
        )
    for outcome in CENTER_OUTCOMES:
        if not _is_int(responses.get(outcome)):
            raise SchemaValidationError(
                CENTER_PROFILE_MISSING,
                "center profile lacks a response for an outcome",
                {"category_id": category, "profile_id": profile_id, "outcome": outcome},
            )
    if not weights:
        raise SchemaValidationError(
            CENTER_MAP_INVALID, "a mapped category has no center weight", {"category_id": category, "key": None}
        )
    parsed = []
    for key, weight in weights.items():
        if (key != MOTOR_THROAT_KEY and key not in centers) or not _is_int(weight) or weight < 1:
            raise SchemaValidationError(
                CENTER_MAP_INVALID,
                "a center-map key or weight is not governed",
                {"category_id": category, "key": key},
            )
        parsed.append((key, weight))
    return _CenterRow(profile_id, responses, tuple(parsed))


def _check_type_pairing(type_pairing: object, order: tuple[str, ...]) -> Mapping[str, Mapping[str, int]]:
    if not isinstance(type_pairing, Mapping):
        raise SchemaValidationError(
            TYPE_PAIRING_INVALID, "bundle has no Type-pairing offsets", {"rule_id": None, "category_id": None}
        )
    unknown = sorted(str(rule) for rule in type_pairing if rule not in PAIR_RULES)
    if unknown:
        raise SchemaValidationError(
            TYPE_PAIRING_INVALID, "an unknown pair rule is present", {"rule_id": unknown[0], "category_id": None}
        )
    for rule in PAIR_RULES:
        offsets = type_pairing.get(rule)
        if not isinstance(offsets, Mapping):
            raise SchemaValidationError(
                TYPE_PAIRING_INVALID, "a pair rule is missing", {"rule_id": rule, "category_id": None}
            )
        for category in order:
            if not _is_int(offsets.get(category)):
                raise SchemaValidationError(
                    TYPE_PAIRING_INVALID,
                    "a pair rule lacks an offset for a category",
                    {"rule_id": rule, "category_id": category},
                )
    return type_pairing


def _check_maxima(maxima: object, order: tuple[str, ...]) -> Mapping[str, tuple[int, int, int, int]]:
    for category in order:
        entry = maxima.get(category) if isinstance(maxima, Mapping) else None
        if (
            type(entry) is not tuple
            or len(entry) != 4
            or not all(_is_int(value) for value in entry)
            or not 0 <= entry[0] < entry[1] < entry[2] < SCORE_MAX
            or entry[3] != SCORE_MAX
        ):
            raise SchemaValidationError(
                MAXIMA_INVALID, "category maxima must be [c1, c2, c3, 100] ascending", {"category_id": category}
            )
    return maxima


# HDE-EPIC043 WU-PR-09: passive provenance for release admission (last top-level statement).
_MODULE_EXECUTION = _capture_module_execution(globals())
