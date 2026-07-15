"""Pure projection of mapped BodyGraph payloads into a source-neutral shape."""
from __future__ import annotations

import copy
import math
from collections.abc import Mapping
from typing import Any, TypedDict


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

