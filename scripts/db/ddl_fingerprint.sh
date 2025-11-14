#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

import json
from typing import Any

from scripts.db import _util


def offline_fingerprint() -> dict[str, Any]:
    return {
        "schema": "hde",
        "version": 1,
        "objects": {
            "hde.body_graphs": {
                "columns": [
                    {"name": "user_id", "data_type": "uuid", "nullable": False, "default": ""},
                    {"name": "vendor", "data_type": "text", "nullable": False, "default": ""},
                    {"name": "vendor_version", "data_type": "integer", "nullable": False, "default": ""},
                    {
                        "name": "input_fingerprint",
                        "data_type": "character",
                        "nullable": False,
                        "default": "",
                    },
                    {"name": "payload", "data_type": "jsonb", "nullable": False, "default": ""},
                    {
                        "name": "created_at",
                        "data_type": "timestamp with time zone",
                        "nullable": False,
                        "default": "now()",
                    },
                    {"name": "refreshed_at", "data_type": "timestamp with time zone", "nullable": True, "default": ""},
                    {"name": "ttl_at", "data_type": "timestamp with time zone", "nullable": True, "default": ""},
                ],
                "constraints": [
                    {
                        "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
                        "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
                    }
                ],
            },
            "hde.body_graphs_current": {
                "definition": "SELECT DISTINCT ON (user_id, vendor) user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at FROM hde.body_graphs ORDER BY user_id, vendor, COALESCE(refreshed_at, created_at) DESC",
            },
            "public.hde_body_graphs_current": {
                "definition": "SELECT user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at FROM hde.body_graphs_current",
            },
        },
    }

TARGET = "artifacts/db/ddl_fingerprint.json"


def normalize_sql(text: str) -> str:
    return " ".join(text.split())


def build_fingerprint() -> dict[str, Any]:
    fingerprint: dict[str, Any] = {
        "schema": "hde",
        "version": 1,
        "objects": {},
    }

    with _util.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT column_name,
                       data_type,
                       is_nullable,
                       column_default
                FROM information_schema.columns
                WHERE table_schema = 'hde'
                  AND table_name = 'body_graphs'
                ORDER BY ordinal_position
                """
            )
            columns = []
            for name, data_type, is_nullable, column_default in cur.fetchall():
                columns.append(
                    {
                        "name": name,
                        "data_type": data_type,
                        "nullable": is_nullable == "YES",
                        "default": normalize_sql(column_default or ""),
                    }
                )

            cur.execute(
                """
                SELECT con.conname, pg_get_constraintdef(con.oid, true)
                FROM pg_constraint con
                JOIN pg_class cls ON cls.oid = con.conrelid
                JOIN pg_namespace nsp ON nsp.oid = con.connamespace
                WHERE nsp.nspname = 'hde'
                  AND cls.relname = 'body_graphs'
                  AND con.contype = 'u'
                ORDER BY con.conname
                """
            )
            constraints = [
                {
                    "name": name,
                    "definition": normalize_sql(defn),
                }
                for name, defn in cur.fetchall()
            ]

            fingerprint["objects"]["hde.body_graphs"] = {
                "columns": columns,
                "constraints": constraints,
            }

            for schema, name in (
                ("hde", "body_graphs_current"),
                ("public", "hde_body_graphs_current"),
            ):
                cur.execute(
                    "SELECT pg_get_viewdef(%s::regclass, true)",
                    (f"{schema}.{name}",),
                )
                definition = normalize_sql((cur.fetchone() or ("",))[0] or "")
                fingerprint["objects"][f"{schema}.{name}"] = {
                    "definition": definition,
                }

    return fingerprint


try:
    fingerprint = build_fingerprint()
except _util.MissingDbConfigError:
    fingerprint = offline_fingerprint()


_util.write_text(
    TARGET,
    json.dumps(fingerprint, separators=(",", ":"), sort_keys=True) + "\n",
)
PY
