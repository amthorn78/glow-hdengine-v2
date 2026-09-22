"""Pure projection of mapped BodyGraph payloads into a source-neutral shape."""
from __future__ import annotations

import copy
import math
import re
from collections.abc import Mapping
from typing import Any, Iterable, TypedDict
from uuid import UUID

from .gates import GateNormalizationError, NormalizedGates, normalize_gates


class BodyGraphFields(TypedDict):
    authority: Any
    birthDateUtc: Any
    centers: Any
    channelsLong: Any
    channelsShort: Any
    definition: Any
    gates: Any
    profile: Any
    strategy: Any
    type: Any


class _Person(TypedDict):
    person_uid: str


class CanonicalBodyGraph(TypedDict):
    bodygraph: BodyGraphFields
    person: _Person
    person_uid: str


class BodyGraphProjectionError(ValueError):
    """Stable, value-free rejection for an invalid mapped BodyGraph payload."""

    def __init__(self, code: str, field_path: str = "root") -> None:
        self.code = code
        self.field_path = field_path
        super().__init__(f"{code}:{field_path}")


_TOP_LEVEL_KEYS = frozenset({"bodygraph", "person", "person_uid", "source"})
_TOP_LEVEL_REQUIRED = frozenset({"bodygraph", "person", "person_uid"})
_PERSON_KEYS = frozenset({"person_uid"})
_BODYGRAPH_KEYS = frozenset(BodyGraphFields.__required_keys__)
_UNSAFE_KEYS = frozenset(
    {
        "authorization",
        "credential",
        "credentials",
        "database_url",
        "db_bridge_url",
        "header",
        "headers",
        "parameters",
        "raw",
        "request",
        "response",
        "secret",
        "sql",
        "token",
        "transport",
    }
)


def _validate_json_shape(value: Any, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise BodyGraphProjectionError("INVALID_SHAPE", path)
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_shape(item, f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key in sorted(value, key=lambda item: str(item)):
            if not isinstance(key, str):
                raise BodyGraphProjectionError("INVALID_SHAPE", path)
            _validate_json_shape(value[key], f"{path}.{key}")
        return
    raise BodyGraphProjectionError("INVALID_SHAPE", path)


def _scan_unsafe_keys(value: Any, path: str) -> None:
    if isinstance(value, Mapping):
        for key in sorted(value):
            key_path = f"{path}.{key}"
            if key.casefold() in _UNSAFE_KEYS:
                raise BodyGraphProjectionError("UNSAFE_FIELD", key_path)
            _scan_unsafe_keys(value[key], key_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_unsafe_keys(item, f"{path}[{index}]")


def _require_exact_keys(value: Mapping[str, Any], required: frozenset[str], allowed: frozenset[str], path: str) -> None:
    missing = sorted(required - set(value))
    if missing:
        raise BodyGraphProjectionError("MISSING_FIELD", f"{path}.{missing[0]}")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise BodyGraphProjectionError("UNKNOWN_FIELD", f"{path}.{unknown[0]}")


def project_bodygraph(mapped: Mapping[str, Any]) -> CanonicalBodyGraph:
    """Return a deep-copied canonical BodyGraph projection without performing I/O."""

    if not isinstance(mapped, Mapping):
        raise BodyGraphProjectionError("INVALID_SHAPE", "root")
    _validate_json_shape(mapped, "root")
    _scan_unsafe_keys(mapped, "root")
    _require_exact_keys(mapped, _TOP_LEVEL_REQUIRED, _TOP_LEVEL_KEYS, "root")

    bodygraph = mapped["bodygraph"]
    person = mapped["person"]
    if not isinstance(bodygraph, Mapping):
        raise BodyGraphProjectionError("INVALID_SHAPE", "root.bodygraph")
    if not isinstance(person, Mapping):
        raise BodyGraphProjectionError("INVALID_SHAPE", "root.person")
    _require_exact_keys(bodygraph, _BODYGRAPH_KEYS, _BODYGRAPH_KEYS, "root.bodygraph")
    _require_exact_keys(person, _PERSON_KEYS, _PERSON_KEYS, "root.person")
    # PF01 §4.2 raw Gate ingress: strict validation before any deduplication,
    # sorting, persistence or evaluation.  The projection keeps the source
    # spelling; normalization to the ascending tuple belongs to the evaluator.
    validate_raw_gates(bodygraph["gates"], "root.bodygraph.gates")

    top_uid = mapped["person_uid"]
    person_uid = person["person_uid"]
    if not isinstance(top_uid, str) or not top_uid:
        raise BodyGraphProjectionError("INVALID_SHAPE", "root.person_uid")
    if not isinstance(person_uid, str) or not person_uid:
        raise BodyGraphProjectionError("INVALID_SHAPE", "root.person.person_uid")
    if top_uid != person_uid:
        raise BodyGraphProjectionError("PERSON_UID_MISMATCH", "root.person_uid")

    return {
        "bodygraph": copy.deepcopy(dict(bodygraph)),
        "person": {"person_uid": person_uid},
        "person_uid": top_uid,
    }


_GATES_INGRESS_CODES = frozenset({"GATES_NOT_LIST", "GATES_EMPTY", "GATE_VALUE_INVALID", "GATE_DUPLICATE"})
_CANONICAL_UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.ASCII)
_PERSON_LABEL_PREFIX = "person-"


def validate_raw_gates(value: object, path: str = "root.bodygraph.gates") -> NormalizedGates:
    """Strict raw-Gate ingress (PF01 §4.2) delegating to the PR02 normalizer.

    Accepts only a nonempty list of exact integers ``1..64`` or canonical
    decimal strings ``"1"``..``"64"``; booleans, whitespace, signs, leading
    zeroes, floats, duplicates (including integer/string equivalents) and
    out-of-domain values refuse with the normalizer's own value-free code.
    """

    try:
        return normalize_gates(value)
    except GateNormalizationError as exc:
        raise BodyGraphProjectionError(exc.code, path) from None


def is_gate_ingress_code(code: str) -> bool:
    return code in _GATES_INGRESS_CODES


def canonical_uuid(value: object) -> str | None:
    """Return the lowercase hyphenated RFC 4122 spelling of any UUID input, else None."""

    if isinstance(value, UUID):
        return str(value)
    if not isinstance(value, str):
        return None
    candidate = value.strip()
    if not candidate:
        return None
    try:
        return str(UUID(candidate))
    except (ValueError, AttributeError, TypeError):
        return None


def strict_canonical_uuid(value: object) -> str | None:
    """Return the value only when it is already the exact lowercase hyphenated spelling."""

    if not isinstance(value, str) or _CANONICAL_UUID.fullmatch(value) is None:
        return None
    return value if canonical_uuid(value) == value else None


def accepted_identity_labels(canonical_person_id: str, seeds: Iterable[str] = ()) -> frozenset[str]:
    """Labels a mapped chart may carry for one verified canonical identity.

    ``person-…`` labels are resolver provenance, never identity: they are
    accepted only when they name the verified UUID or the trusted seed that the
    sanctioned resolver mapped to that UUID.
    """

    labels = {canonical_person_id, f"{_PERSON_LABEL_PREFIX}{canonical_person_id}"}
    for seed in seeds:
        if isinstance(seed, str) and seed.strip():
            labels.add(seed.strip())
            labels.add(f"{_PERSON_LABEL_PREFIX}{seed.strip()}")
    return frozenset(labels)


def bind_projection_identity(
    projection: Mapping[str, Any],
    canonical_person_id: str,
    *,
    accepted_labels: Iterable[str] = (),
) -> CanonicalBodyGraph:
    """Return the projection with both label slots replaced by the verified UUID.

    The caller supplies the trusted canonical identity and the labels its
    provenance permits.  A label that is neither an accepted label nor another
    spelling of the same UUID is an independently conflicting identity and
    refuses; no prefix is stripped with assumed ownership.
    """

    if strict_canonical_uuid(canonical_person_id) is None:
        raise BodyGraphProjectionError("IDENTITY_INVALID", "root.person_uid")
    label = projection["person_uid"]
    nested = projection["person"]["person_uid"]
    if label != nested:
        raise BodyGraphProjectionError("PERSON_UID_MISMATCH", "root.person_uid")
    accepted = set(accepted_labels) | {canonical_person_id, f"{_PERSON_LABEL_PREFIX}{canonical_person_id}"}
    if label not in accepted and canonical_uuid(label) != canonical_person_id:
        raise BodyGraphProjectionError("IDENTITY_CONFLICT", "root.person_uid")
    return {
        "bodygraph": copy.deepcopy(dict(projection["bodygraph"])),
        "person": {"person_uid": canonical_person_id},
        "person_uid": canonical_person_id,
    }
