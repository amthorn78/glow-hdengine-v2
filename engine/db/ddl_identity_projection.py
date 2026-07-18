"""Strict shared DDL identity projection for provider parity checks."""
from __future__ import annotations

from collections.abc import Mapping

DDL_IDENTITY_PROJECTION_SCHEMA = "hde.ddl_identity_projection.v1"
DDL_IDENTITY_PROJECTION_FIELDS = (
    "projection[].kind",
    "projection[].name",
    "projection[].columns[].name",
    "projection[].columns[].type",
)
DDL_IDENTITY_UNEXAMINED_FIELDS = (
    "source[].columns[].nullable",
    "source[].columns[].default",
    "source[].constraints",
    "source[kind=view].definition",
)

def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise ValueError(f"invalid {label}")
    return value

def project_ddl_identity(value: object) -> list[dict[str, object]]:
    if not isinstance(value, list) or not value:
        raise ValueError("ddl identity input must be a nonempty list")
    seen: set[tuple[str, str]] = set()
    projected: list[dict[str, object]] = []
    for obj in value:
        if not isinstance(obj, Mapping):
            raise ValueError("ddl identity object must be a mapping")
        kind = _strict_string(obj.get("kind"), "kind")
        name = _strict_string(obj.get("name"), "name")
        if kind not in {"table", "view"}:
            raise ValueError("ddl identity kind must be table or view")
        key = (kind, name)
        if key in seen:
            raise ValueError("duplicate ddl identity object")
        seen.add(key)
        cols = obj.get("columns", [])
        if "columns" in obj and not isinstance(cols, list):
            raise ValueError("ddl identity columns must be a list")
        if kind == "table" and (not isinstance(cols, list) or not cols):
            raise ValueError("table ddl identity requires columns")
        out_cols: list[dict[str, str]] = []
        col_seen: set[str] = set()
        for col in cols:
            if not isinstance(col, Mapping):
                raise ValueError("ddl identity column must be a mapping")
            col_name = _strict_string(col.get("name"), "column name")
            if col_name in col_seen:
                raise ValueError("duplicate ddl identity column")
            col_seen.add(col_name)
            has_type, has_data_type = "type" in col, "data_type" in col
            raw_type = col.get("type") if has_type else col.get("data_type")
            col_type = _strict_string(raw_type, "column type")
            if has_type and has_data_type and col.get("type") != col.get("data_type"):
                raise ValueError("conflicting ddl identity column types")
            out_cols.append({"name": col_name, "type": col_type})
        projected.append({"kind": kind, "name": name, "columns": sorted(out_cols, key=lambda c: (c["name"], c["type"]))})
    return sorted(projected, key=lambda item: (item["kind"], item["name"]))
