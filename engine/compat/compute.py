from __future__ import annotations
import hashlib
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Literal, Mapping, Tuple

import jsonschema
from jsonschema import validators

from engine.bodygraph.gates import GateNormalizationError, NormalizedGates, normalize_gates
from engine.bodygraph.projection import strict_canonical_uuid
from engine.bodygraph.resolver import (
    ResolvedCompatChart,
    resolve_compat_chart,
)
from engine.compat.error_tokens import CompatBoundaryError
from engine.config.magic10_v2_loader import (
    MAGIC10_V2_COMPAT_RESULT_SCHEMA,
    MAGIC10_V2_INTRINSIC_CACHE_PREFIX,
    MAGIC10_V2_RESULT_SCHEMA,
)
from engine.config.registry_loader import AdmittedMechanicsBundle, SchemaValidationError, load_active_mechanics_bundle
from engine.core.core import _chart_fingerprint, _digest, _validate_member, compute_core
from engine.magic10_v2 import compat as magic10_v2_compat
from engine.magic10_v2.calculation import CategoryResult, Magic10V2Result, assign_band
from engine.magic10_v2.signals import PER_MILLE, SignalValue
from engine.narratives.router import route_keys
from engine.serializer.canon import sercanon


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR04: eligibility, orientation and complete Gate-based evaluation
# (PF01 §4, §5.2.2; PF05 §4.1.3, §5.1.0).  The only mechanics entry is the PR03
# pure core; consumers obtain the immutable typed bundle solely through the
# provider seam below and never re-admit, reload or bypass it.  Since
# HDE-EPIC043 WU-PR-09 the core is the Magic10 v2 calculation and the value is
# the dormant layer's ``magic10_compat_result.v2``.
# ---------------------------------------------------------------------------

_ROOT = Path(__file__).resolve().parents[2]
_COMPAT_RESULT_SCHEMA_PATH = "schemas/magic10_compat_result_v2.schema.json"
COMPAT_RESULT_SCHEMA = MAGIC10_V2_COMPAT_RESULT_SCHEMA
PURE_RESULT_SCHEMA = MAGIC10_V2_RESULT_SCHEMA
INTRINSIC_CACHE_PREFIX = MAGIC10_V2_INTRINSIC_CACHE_PREFIX
INELIGIBLE_SELF = "ineligible_self"
ELIGIBLE = "eligible"

# Default admitted-bundle provider; tests inject the synthetic complete release
# by monkeypatching this module attribute, never by relaxing admission.
_BUNDLE_PROVIDER: Callable[[], AdmittedMechanicsBundle] = load_active_mechanics_bundle

_SCHEMA_VALIDATORS: dict[str, Any] = {}


def admitted_bundle() -> AdmittedMechanicsBundle:
    """Return the admitted mechanics bundle from the active provider seam.

    The default provider is the admission owner's public entry
    ``engine.config.registry_loader.load_active_mechanics_bundle``; its refusal
    propagates unchanged.  Gate-level admission probes read this seam so a test
    that injects the synthetic complete release observes one admission state for
    evaluation and probing alike.  Nothing here relaxes admission.
    """

    return _BUNDLE_PROVIDER()


@dataclass(frozen=True)
class EvaluationParty:
    """One validated evaluation-party record (PF01 §4.1)."""

    canonical_person_id: str
    projection: Mapping[str, Any]
    gates: NormalizedGates
    chart_fingerprint: str


def ineligible_self_carrier() -> Dict[str, object]:
    """PF01 §4.7 emission for a valid self-pair on internal/admin surfaces."""

    return {"categories": [], "eligible": False}


def is_ineligible_carrier(result: Mapping[str, object]) -> bool:
    return isinstance(result, Mapping) and result.get("eligible") is False and "schema" not in result


def evaluation_party(resolved: ResolvedCompatChart) -> EvaluationParty:
    """Project a resolved complete chart into the exact evaluation-party record."""

    if not isinstance(resolved, ResolvedCompatChart):
        raise CompatBoundaryError("chart_missing", detail="party")
    canonical_person_id = resolved.canonical_person_id
    if strict_canonical_uuid(canonical_person_id) is None:
        raise CompatBoundaryError("identity_invalid", detail="party")
    chart = resolved.mapped_chart
    bodygraph = chart.get("bodygraph") if isinstance(chart, Mapping) else None
    if not isinstance(bodygraph, Mapping) or "gates" not in bodygraph:
        raise CompatBoundaryError("gates_missing", detail="party")
    raw_gates = bodygraph["gates"]
    try:
        gates = normalize_gates(list(raw_gates) if isinstance(raw_gates, (list, tuple)) else raw_gates)
    except GateNormalizationError as exc:
        raise CompatBoundaryError("gates_missing" if exc.code == "GATES_EMPTY" else "gates_invalid", detail=exc.code) from None
    if chart.get("person_uid") != canonical_person_id or chart.get("person", {}).get("person_uid") != canonical_person_id:
        raise CompatBoundaryError("identity_conflict", detail="party")
    projection = {
        "bodygraph": {**deepcopy(dict(bodygraph)), "gates": list(gates.gates)},
        "person": {"person_uid": canonical_person_id},
        "person_uid": canonical_person_id,
    }
    return EvaluationParty(
        canonical_person_id=canonical_person_id,
        projection=projection,
        gates=gates,
        chart_fingerprint=_chart_fingerprint(gates),
    )


def _require_party(party: object) -> EvaluationParty:
    if type(party) is not EvaluationParty:
        raise CompatBoundaryError("chart_missing", detail="party")
    if strict_canonical_uuid(party.canonical_person_id) is None:
        raise CompatBoundaryError("identity_invalid", detail="party")
    if type(party.gates) is not NormalizedGates:
        raise CompatBoundaryError("gates_invalid", detail="party")
    if not isinstance(party.projection, Mapping) or party.projection.get("person_uid") != party.canonical_person_id:
        raise CompatBoundaryError("identity_conflict", detail="party")
    if type(party.chart_fingerprint) is not str or len(party.chart_fingerprint) != 64:
        raise CompatBoundaryError("chart_invalid", detail="fingerprint")
    return party


def validate_pair_eligibility(a: EvaluationParty, b: EvaluationParty) -> Literal["eligible", "ineligible_self"]:
    """PF01 §4.1: same UUID + identical normalized projection is ineligible; same
    UUID with unequal projections fails closed; distinct UUIDs are eligible."""

    _require_party(a)
    _require_party(b)
    if a.canonical_person_id != b.canonical_person_id:
        return ELIGIBLE
    if sercanon(a.projection) == sercanon(b.projection):
        return INELIGIBLE_SELF
    raise CompatBoundaryError("inconsistent_self")


def orient(a: EvaluationParty, b: EvaluationParty) -> Tuple[EvaluationParty, EvaluationParty]:
    """Directional orientation by ``(gate_mask, canonical_person_id)``; UUID ASCII
    order breaks only an equal-mask tie.  Never enters intrinsic mathematics."""

    lo, hi = sorted((a, b), key=lambda party: (party.gates.mask, party.canonical_person_id))
    return lo, hi


def intrinsic_pair_key(lo: EvaluationParty, hi: EvaluationParty, *, config_id: str, release_id: str) -> str:
    members = sorted((lo, hi), key=lambda party: party.gates.mask)
    return _digest({
        "schema": "magic10_pair_preimage.v1",
        "members": [member.chart_fingerprint for member in members],
        "config_id": config_id, "release_id": release_id,
        "result_schema": PURE_RESULT_SCHEMA,
    })


def _pure_result_matches(candidate: object, *, bundle: AdmittedMechanicsBundle, pair_key: str, config_id: str, release_id: str) -> bool:
    """Structural check of a cached pure result against the active release."""

    if not isinstance(candidate, Mapping):
        return False
    if set(candidate) != {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}:
        return False
    if (candidate["schema"] != PURE_RESULT_SCHEMA or candidate["config_id"] != config_id
            or candidate["release_id"] != release_id or candidate["pair_key"] != pair_key):
        return False
    registry = bundle.registry
    signal_order = [signal for category in registry.magic10_order for signal in registry.magic10_caps[category].inputs]
    signals = candidate["signals"]
    categories = candidate["categories"]
    if not isinstance(signals, list) or not isinstance(categories, list):
        return False
    if [row.get("signal_id") if isinstance(row, Mapping) else None for row in signals] != signal_order:
        return False
    for row in signals:
        if set(row) != {"signal_id", "q"} or type(row["q"]) is not int or not 0 <= row["q"] <= PER_MILLE:
            return False
    if [row.get("category_id") if isinstance(row, Mapping) else None for row in categories] != list(registry.magic10_order):
        return False
    maxima = bundle.magic10_v2.maxima
    for row in categories:
        if set(row) != {"category_id", "score", "band"} or type(row["score"]) is not int or not 0 <= row["score"] <= 100:
            return False
        if row["band"] != assign_band(row["score"], maxima[row["category_id"]]):
            return False
    return True


def _cached_pure_result(hit: object, *, bundle, pair_key: str, config_id: str, release_id: str, fingerprints: list[str]) -> Mapping[str, Any] | None:
    """Return a served pure result only when the cached identity fully matches."""

    if not isinstance(hit, Mapping):
        return None
    if (hit.get("pair_key") != pair_key or hit.get("config_id") != config_id
            or hit.get("release_id") != release_id or hit.get("result_schema") != PURE_RESULT_SCHEMA
            or list(hit.get("fingerprints") or []) != fingerprints):
        return None
    result = hit.get("result")
    if not _pure_result_matches(result, bundle=bundle, pair_key=pair_key, config_id=config_id, release_id=release_id):
        return None
    return result


def _result_from_payload(payload: Mapping[str, Any]) -> Magic10V2Result:
    """Rebuild the pure ``magic10_result.v2`` value of a verified cache hit."""

    return Magic10V2Result(
        schema=payload["schema"],
        config_id=payload["config_id"],
        release_id=payload["release_id"],
        pair_key=payload["pair_key"],
        signals=tuple(SignalValue(row["signal_id"], row["q"]) for row in payload["signals"]),
        categories=tuple(CategoryResult(row["category_id"], row["score"], row["band"]) for row in payload["categories"]),
    )


def _compat_value(pure: Magic10V2Result, bundle: AdmittedMechanicsBundle, router: Callable[..., Mapping[str, str]] | None) -> Dict[str, Any]:
    """The dormant layer's ``magic10_compat_result.v2`` value, with its refusals mapped (F-28)."""

    try:
        return magic10_v2_compat.compat_result_v2(pure, bundle.magic10_v2, router=router)
    except SchemaValidationError as exc:
        if exc.code == magic10_v2_compat.NARRATIVE_KEY_INVALID:
            raise CompatBoundaryError("narrative_key", detail=str(exc.details.get("category_id"))) from None
        if exc.code == magic10_v2_compat.RESULT_INVALID:
            raise CompatBoundaryError("result_schema", detail=str(exc.details.get("check"))) from None
        raise CompatBoundaryError("admission_config", detail=exc.code) from None


def _compat_result_validator(bundle: AdmittedMechanicsBundle):
    """Return the strict validator for the schema bytes bound to the admitted release."""

    identity = next((row for row in bundle.source_identities if row.path == _COMPAT_RESULT_SCHEMA_PATH), None)
    if identity is None:
        raise CompatBoundaryError("result_schema", detail="unbound_schema")
    raw = (_ROOT / _COMPAT_RESULT_SCHEMA_PATH).read_bytes()
    if hashlib.sha256(raw).hexdigest() != identity.sha256 or len(raw) != identity.size:
        raise CompatBoundaryError("result_schema", detail="schema_bytes")
    cached = _SCHEMA_VALIDATORS.get(identity.sha256)
    if cached is None:
        import json as _json
        schema = _json.loads(raw.decode("utf-8"))
        strict = validators.extend(
            jsonschema.Draft202012Validator,
            type_checker=jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
                "integer", lambda checker, value: type(value) is int
            ),
        )
        strict.check_schema(schema)
        cached = strict(schema)
        _SCHEMA_VALIDATORS[identity.sha256] = cached
    return cached


def validate_compat_result(result: Mapping[str, Any], bundle: AdmittedMechanicsBundle, *, pair_key: str | None = None) -> None:
    """Structural validation of an augmented result against the governed schema
    and the active release identity; refuses with ``ERR_M10_RESULT_SCHEMA_MISMATCH``."""

    validator = _compat_result_validator(bundle)
    try:
        validator.validate(result)
    except jsonschema.ValidationError as exc:
        raise CompatBoundaryError("result_schema", detail="schema") from None
    registry = bundle.registry
    if result["release_id"] != bundle.release_id or result["config_id"] != bundle.mechanics["config_id"]:
        raise CompatBoundaryError("result_schema", detail="identity")
    if pair_key is not None and result["pair_key"] != pair_key:
        raise CompatBoundaryError("result_schema", detail="pair_key")
    if [row["category_id"] for row in result["categories"]] != list(registry.magic10_order):
        raise CompatBoundaryError("result_schema", detail="category_order")
    signal_order = [signal for category in registry.magic10_order for signal in registry.magic10_caps[category].inputs]
    if [row["signal_id"] for row in result["signals"]] != signal_order:
        raise CompatBoundaryError("result_schema", detail="signal_order")


def evaluate_pair(
    a: EvaluationParty,
    b: EvaluationParty,
    *,
    bundle_provider: Callable[[], AdmittedMechanicsBundle] | None = None,
    cache: Any | None = None,
    router: Callable[..., Mapping[str, str]] | None = None,
) -> Dict[str, Any]:
    """Evaluate one validated pair (PF01 §4, §5.2.2; PF05 §4.1.3).

    1. eligibility; 2. orientation; 3. admitted bundle from the provider seam
    (refusal propagates unchanged); 4. intrinsic cache lookup only through an
    injected seam; 5. pure core (``magic10_result.v2``); 6. the dormant layer's
    ``magic10_compat_result.v2`` value, with router keys in both normalized
    directions; 7. structural validation against the release-bound schema;
    8. the canonical result mapping.
    A valid self-pair returns the PF01 §4.7 carrier and touches no core, cache,
    router or ``pair_key``.
    """

    if validate_pair_eligibility(a, b) == INELIGIBLE_SELF:
        return ineligible_self_carrier()
    lo, hi = orient(a, b)
    provider = _BUNDLE_PROVIDER if bundle_provider is None else bundle_provider
    bundle = provider()
    if type(bundle) is not AdmittedMechanicsBundle:
        raise CompatBoundaryError("admission_config", detail="provider")
    config_id = bundle.mechanics["config_id"]
    release_id = bundle.release_id
    pair_key = intrinsic_pair_key(lo, hi, config_id=config_id, release_id=release_id)
    fingerprints = [member.chart_fingerprint for member in sorted((lo, hi), key=lambda party: party.gates.mask)]
    cache_key = f"{INTRINSIC_CACHE_PREFIX}{pair_key}"
    pure: Magic10V2Result | None = None
    stale_hit = False
    if cache is not None:
        hit = cache.get(cache_key)
        if hit is not None:
            cached = _cached_pure_result(hit, bundle=bundle, pair_key=pair_key, config_id=config_id, release_id=release_id, fingerprints=fingerprints)
            stale_hit = cached is None
            if cached is not None:
                pure = _result_from_payload(cached)
    if pure is None:
        try:
            core = compute_core(lo.gates, hi.gates, bundle, release_id)
        except SchemaValidationError as exc:
            # The members were validated first; a v2 calculation, kernel or
            # signals refusal is a configuration defect (HDE-EPIC043 WU-PR-09, F-28).
            raise CompatBoundaryError("admission_config", detail=exc.code) from None
        except ValueError:
            # ``compute_core`` validates both members before it reads the bundle,
            # registry or mechanics, so member validity is what separates a chart
            # defect from a configuration one.  It is therefore asked first, and
            # ahead of ``stale_hit``: PF05 §5.2.3 reserves the stale-result token
            # for valid Gate inputs being unavailable for recomputation, so a
            # server-side defect must not borrow it just because a mismatched
            # cache entry happened to be present.  Reporting either as
            # ``gates_invalid`` would blame a stored BodyGraph --
            # ERR_M10_BODYGRAPH_INCOMPLETE on the Reader transport -- for a
            # roster, mechanics or identity defect.
            try:
                _validate_member(lo.gates)
                _validate_member(hi.gates)
            except ValueError:
                # The members themselves are unusable. A mismatched cache entry
                # is then the reason the cached result could not stand in.
                raise CompatBoundaryError(
                    "stale_result" if stale_hit else "gates_invalid", detail="core"
                ) from None
            raise CompatBoundaryError("admission_config", detail="core") from None
        pure = core
        if pure.pair_key != pair_key:
            raise CompatBoundaryError("result_schema", detail="pair_key")
        if cache is not None and hasattr(cache, "put"):
            cache.put(cache_key, {
                "pair_key": pair_key, "config_id": config_id, "release_id": release_id,
                "result_schema": PURE_RESULT_SCHEMA, "fingerprints": list(fingerprints),
                "result": deepcopy(pure.as_payload()),
            })
    value = _compat_value(pure, bundle, route_keys if router is None else router)
    validate_compat_result(value, bundle, pair_key=pair_key)
    return value


def harmony_band(result: Mapping[str, Any]) -> str:
    """Return the validated ``harmony`` band of a complete result."""

    for row in result.get("categories", ()):
        if isinstance(row, Mapping) and row.get("category_id") == "harmony":
            return str(row["band"])
    raise CompatBoundaryError("result_schema", detail="harmony")


# ---------------------------------------------------------------------------
# Conjunction carriers: a thin pure entry over two validated parties and the
# resolving orchestrator used by the CLI and the dev conjunction routes.
# ---------------------------------------------------------------------------

def conjunction_public(
    left_party: EvaluationParty,
    right_party: EvaluationParty,
    *,
    viewer_top: str | None = None,
    viewer_weights: Mapping[str, int] | None = None,
    engine_tag: str | None = None,
    release_id: str | None = None,
    invocation_tag: str | None = None,
    bundle_provider: Callable[[], AdmittedMechanicsBundle] | None = None,
    cache: Any | None = None,
    router: Callable[..., Mapping[str, str]] | None = None,
) -> Dict[str, object]:
    """Deterministic conjunction payload for two already-validated parties.

    ``viewer_top``, ``viewer_weights`` and the identity tags are accepted for
    existing callers only; they are not scoring operands and do not enter the
    payload.  ``left``/``right`` carry the normalized lo/hi identities so AB
    and BA bytes are identical.  A valid self-pair returns the PF01 §4.7
    carrier unchanged.
    """

    result = evaluate_pair(left_party, right_party, bundle_provider=bundle_provider, cache=cache, router=router)
    if is_ineligible_carrier(result):
        return result
    lo, hi = orient(left_party, right_party)
    return {
        "conjunction": {
            "left": {"person_uid": lo.canonical_person_id},
            "right": {"person_uid": hi.canonical_person_id},
            "compat": result,
        }
    }


def conjunction_public_resolved(
    left: Mapping[str, Any] | str,
    right: Mapping[str, Any] | str,
    *,
    viewer_top: str | None = None,
    viewer_weights: Mapping[str, int] | None = None,
    engine_tag: str | None = None,
    release_id: str | None = None,
    invocation_tag: str | None = None,
    env: Mapping[str, object] | None = None,
    local_lookup: Callable[[str], object] | None = None,
    acquisition: Callable[..., object] | None = None,
    source_policy: str = "vendor",
    bundle_provider: Callable[[], AdmittedMechanicsBundle] | None = None,
    cache: Any | None = None,
    router: Callable[..., Mapping[str, str]] | None = None,
) -> Dict[str, object]:
    """Resolve both parties to complete charts, then evaluate.

    Call-site gating semantics are unchanged: the local lookup is always tried
    first; closed rails refuse acquisition when local data is missing; open
    rails allow read-only acquisition only after a local miss and only under
    the ``vendor`` source policy.  Both parties resolve before any evaluation.
    """

    rails_env: Mapping[str, object] = env if env is not None else {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
    left_resolved = resolve_compat_chart(left, source_policy=source_policy, env=rails_env, local_lookup=local_lookup, acquisition=acquisition)
    right_resolved = resolve_compat_chart(right, source_policy=source_policy, env=rails_env, local_lookup=local_lookup, acquisition=acquisition)
    return conjunction_public(
        evaluation_party(left_resolved),
        evaluation_party(right_resolved),
        viewer_top=viewer_top,
        viewer_weights=viewer_weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
        bundle_provider=bundle_provider,
        cache=cache,
        router=router,
    )
