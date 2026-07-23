"""Dependency-free validator for the bounded HDE-EPIC038 OPS-03 schemas.

This is intentionally not a general JSON Schema implementation.  It accepts
only the Draft 2020-12 keywords and value shapes used by the seven governed
OPS-03 schemas, and rejects unsupported schema input before validating data.
"""
from __future__ import annotations

import datetime as dt
import math
import re
from collections.abc import Mapping
from typing import Any

_SCHEMA_KEYS = frozenset(
    {
        "$defs",
        "$id",
        "$ref",
        "$schema",
        "additionalProperties",
        "allOf",
        "anyOf",
        "const",
        "else",
        "enum",
        "format",
        "if",
        "items",
        "maxItems",
        "maxLength",
        "maximum",
        "minItems",
        "minLength",
        "minimum",
        "pattern",
        "prefixItems",
        "properties",
        "required",
        "then",
        "type",
    }
)
_TYPES = frozenset({"array", "boolean", "integer", "null", "object", "string"})
_SCHEMA_MAP_KEYS = frozenset({"$defs", "properties"})
_SCHEMA_VALUE_KEYS = frozenset({"else", "if", "then"})
_SCHEMA_LIST_KEYS = frozenset({"allOf", "anyOf", "prefixItems"})
_NONNEGATIVE_INTEGER_KEYS = frozenset(
    {"maxItems", "maxLength", "minItems", "minLength"}
)
_NUMERIC_KEYS = frozenset({"maximum", "minimum"})
_LOCAL_REF = re.compile(r"^#/\$defs/([A-Za-z0-9_.-]+)$")
_RFC3339_DATE_TIME = re.compile(
    r"^(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})[Tt]"
    r"(?P<hour>[0-9]{2}):(?P<minute>[0-9]{2}):(?P<second>[0-9]{2})"
    r"(?:\.[0-9]+)?(?P<zone>[Zz]|[+-][0-9]{2}:[0-9]{2})$"
)


def _is_integer(value: Any) -> bool:
    return (
        (isinstance(value, int) and not isinstance(value, bool))
        or (
            isinstance(value, float)
            and math.isfinite(value)
            and value.is_integer()
        )
    )


def _is_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    )


def _json_equal(left: Any, right: Any) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left == right
    if _is_number(left) or _is_number(right):
        return _is_number(left) and _is_number(right) and left == right
    if left is None or right is None:
        return left is None and right is None
    if isinstance(left, str) or isinstance(right, str):
        return isinstance(left, str) and isinstance(right, str) and left == right
    if isinstance(left, list) or isinstance(right, list):
        return (
            isinstance(left, list)
            and isinstance(right, list)
            and len(left) == len(right)
            and all(_json_equal(a, b) for a, b in zip(left, right))
        )
    if isinstance(left, Mapping) or isinstance(right, Mapping):
        return (
            isinstance(left, Mapping)
            and isinstance(right, Mapping)
            and set(left) == set(right)
            and all(_json_equal(left[key], right[key]) for key in left)
        )
    return False


def _schema_source_supported(schema: Any, root: Mapping[str, Any]) -> bool:
    if isinstance(schema, bool):
        return True
    if not isinstance(schema, Mapping) or any(key not in _SCHEMA_KEYS for key in schema):
        return False
    for key, value in schema.items():
        if key == "$id" and not isinstance(value, str):
            return False
        if key == "$schema" and value != "https://json-schema.org/draft/2020-12/schema":
            return False
        if key == "$ref":
            match = _LOCAL_REF.fullmatch(value) if isinstance(value, str) else None
            if match is None:
                return False
            definitions = root.get("$defs")
            if not isinstance(definitions, Mapping) or match.group(1) not in definitions:
                return False
        elif key == "type" and (
            not isinstance(value, str) or value not in _TYPES
        ):
            return False
        elif key in _SCHEMA_MAP_KEYS:
            if not isinstance(value, Mapping) or not all(
                isinstance(name, str) and _schema_source_supported(child, root)
                for name, child in value.items()
            ):
                return False
        elif key in _SCHEMA_VALUE_KEYS and not _schema_source_supported(value, root):
            return False
        elif key in _SCHEMA_LIST_KEYS:
            if (
                not isinstance(value, list)
                or not value
                or not all(_schema_source_supported(child, root) for child in value)
            ):
                return False
        elif key == "additionalProperties" and value is not False:
            return False
        elif key == "items" and value is not False:
            return False
        elif key == "required" and (
            not isinstance(value, list)
            or any(not isinstance(item, str) for item in value)
            or len(value) != len(set(value))
        ):
            return False
        elif key == "enum" and (not isinstance(value, list) or not value):
            return False
        elif key == "pattern":
            if not isinstance(value, str):
                return False
            try:
                re.compile(value)
            except re.error:
                return False
        elif key == "format" and value != "date-time":
            return False
        elif key in _NONNEGATIVE_INTEGER_KEYS and (
            not _is_integer(value) or value < 0
        ):
            return False
        elif key in _NUMERIC_KEYS and not _is_number(value):
            return False
    return True


def _definition_references(schema: Any) -> set[str]:
    if isinstance(schema, bool):
        return set()
    references: set[str] = set()
    reference = schema.get("$ref")
    if isinstance(reference, str):
        match = _LOCAL_REF.fullmatch(reference)
        if match is not None:
            references.add(match.group(1))
    for key in _SCHEMA_MAP_KEYS:
        children = schema.get(key)
        if isinstance(children, Mapping):
            for child in children.values():
                references.update(_definition_references(child))
    for key in _SCHEMA_VALUE_KEYS:
        if key in schema:
            references.update(_definition_references(schema[key]))
    for key in _SCHEMA_LIST_KEYS:
        children = schema.get(key)
        if isinstance(children, list):
            for child in children:
                references.update(_definition_references(child))
    return references


def _references_acyclic(root: Mapping[str, Any]) -> bool:
    definitions = root.get("$defs", {})
    if not isinstance(definitions, Mapping):
        return False
    graph = {
        name: _definition_references(schema)
        for name, schema in definitions.items()
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> bool:
        if name in visiting:
            return False
        if name in visited:
            return True
        visiting.add(name)
        if any(not visit(child) for child in graph.get(name, set())):
            return False
        visiting.remove(name)
        visited.add(name)
        return True

    return all(visit(name) for name in graph)


def _type_matches(value: Any, expected: str) -> bool:
    return {
        "array": isinstance(value, list),
        "boolean": isinstance(value, bool),
        "integer": _is_integer(value),
        "null": value is None,
        "object": isinstance(value, Mapping),
        "string": isinstance(value, str),
    }[expected]


def _date_time_valid(value: str) -> bool:
    match = _RFC3339_DATE_TIME.fullmatch(value)
    if match is None:
        return False
    try:
        dt.date(
            int(match.group("year")),
            int(match.group("month")),
            int(match.group("day")),
        )
    except ValueError:
        return False
    hour = int(match.group("hour"))
    minute = int(match.group("minute"))
    second = int(match.group("second"))
    if hour > 23 or minute > 59 or second > 60:
        return False
    zone = match.group("zone")
    if zone not in {"Z", "z"}:
        offset_hour, offset_minute = map(int, zone[1:].split(":"))
        if offset_hour > 23 or offset_minute > 59:
            return False
    return True


def _resolve_ref(reference: str, root: Mapping[str, Any]) -> tuple[str, Any] | None:
    match = _LOCAL_REF.fullmatch(reference)
    definitions = root.get("$defs")
    if match is None or not isinstance(definitions, Mapping):
        return None
    name = match.group(1)
    return (name, definitions[name]) if name in definitions else None


def _matches(
    value: Any,
    schema: Any,
    root: Mapping[str, Any],
    active_refs: frozenset[str],
) -> bool:
    if isinstance(schema, bool):
        return schema
    reference = schema.get("$ref")
    if reference is not None:
        resolved = _resolve_ref(reference, root)
        if resolved is None or resolved[0] in active_refs:
            return False
        if not _matches(value, resolved[1], root, active_refs | {resolved[0]}):
            return False
    if "const" in schema and not _json_equal(value, schema["const"]):
        return False
    if "enum" in schema and not any(_json_equal(value, item) for item in schema["enum"]):
        return False
    expected_type = schema.get("type")
    if expected_type is not None and not _type_matches(value, expected_type):
        return False
    if "allOf" in schema and not all(
        _matches(value, child, root, active_refs) for child in schema["allOf"]
    ):
        return False
    if "anyOf" in schema and not any(
        _matches(value, child, root, active_refs) for child in schema["anyOf"]
    ):
        return False
    if "if" in schema:
        condition = _matches(value, schema["if"], root, active_refs)
        branch = schema.get("then") if condition else schema.get("else")
        if branch is not None and not _matches(value, branch, root, active_refs):
            return False
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            return False
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            return False
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            return False
        if schema.get("format") == "date-time" and not _date_time_valid(value):
            return False
    if _is_number(value):
        if "minimum" in schema and value < schema["minimum"]:
            return False
        if "maximum" in schema and value > schema["maximum"]:
            return False
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            return False
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            return False
        prefix = schema.get("prefixItems", ())
        if any(
            not _matches(item, prefix[index], root, active_refs)
            for index, item in enumerate(value[: len(prefix)])
        ):
            return False
        if schema.get("items") is False and len(value) > len(prefix):
            return False
    if isinstance(value, Mapping):
        required = schema.get("required", ())
        if any(name not in value for name in required):
            return False
        properties = schema.get("properties", {})
        if any(
            name in properties
            and not _matches(item, properties[name], root, active_refs)
            for name, item in value.items()
        ):
            return False
        if schema.get("additionalProperties") is False and any(
            name not in properties for name in value
        ):
            return False
    return True


def is_valid(value: Any, schema: Any) -> bool:
    """Return whether *value* satisfies one supported, well-formed schema."""

    if (
        not isinstance(schema, Mapping)
        or not _schema_source_supported(schema, schema)
        or not _references_acyclic(schema)
    ):
        return False
    return _matches(value, schema, schema, frozenset())


__all__ = ["is_valid"]
