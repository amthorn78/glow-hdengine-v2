#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

import json
import re

from scripts.db import _util

TARGET = "artifacts/db/ddl_fingerprint.json"


def normalize_sql(text: str) -> str:
    return " ".join(text.split())


def normalize_body(defn: str) -> str:
    pattern = re.compile(r"AS\s+\$(?P<tag>[^$]*)\$(?P<body>.*)\$(?P=tag)\$", re.DOTALL)
    match = pattern.search(defn)
    if not match:
        return ""
    body = match.group("body")
    lines = [line.rstrip() for line in body.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


fingerprint = {
    "schema": "v1",
    "extensions": [],
    "sequences": [],
    "indexes": [],
    "constraints": [],
    "domains": [],
    "functions": [],
}


with _util.connect() as conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT extname FROM pg_extension WHERE extname NOT IN ('plpgsql') ORDER BY extname"
        )
        fingerprint["extensions"] = [row[0] for row in cur.fetchall()]

        cur.execute(
            """
            SELECT n.nspname, c.relname
            FROM pg_class c
            JOIN pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind = 'S' AND n.nspname NOT IN ('pg_catalog','information_schema')
            ORDER BY n.nspname, c.relname
            """
        )
        fingerprint["sequences"] = [f"{n}.{r}" for n, r in cur.fetchall()]

        cur.execute(
            """
            SELECT schemaname, tablename, indexname, indexdef
            FROM pg_indexes
            WHERE schemaname NOT IN ('pg_catalog','information_schema')
            ORDER BY schemaname, tablename, indexname
            """
        )
        fingerprint["indexes"] = [
            {
                "name": f"{schema}.{index}",
                "table": f"{schema}.{table}",
                "definition": normalize_sql(indexdef),
            }
            for schema, table, index, indexdef in cur.fetchall()
        ]

        cur.execute(
            """
            SELECT n.nspname, cls.relname, con.conname, pg_get_constraintdef(con.oid, true)
            FROM pg_constraint con
            JOIN pg_class cls ON cls.oid = con.conrelid
            JOIN pg_namespace n ON n.oid = cls.relnamespace
            WHERE n.nspname NOT IN ('pg_catalog','information_schema')
            ORDER BY n.nspname, cls.relname, con.conname
            """
        )
        fingerprint["constraints"] = [
            {
                "name": f"{schema}.{table}.{conname}",
                "definition": normalize_sql(defn),
            }
            for schema, table, conname, defn in cur.fetchall()
        ]

        cur.execute(
            """
            SELECT domain_schema, domain_name, data_type, domain_default
            FROM information_schema.domains
            WHERE domain_schema NOT IN ('pg_catalog','information_schema')
            ORDER BY domain_schema, domain_name
            """
        )
        fingerprint["domains"] = [
            {
                "name": f"{schema}.{name}",
                "data_type": data_type,
                "default": domain_default or "",
            }
            for schema, name, data_type, domain_default in cur.fetchall()
        ]

        cur.execute(
            """
            SELECT n.nspname,
                   p.proname,
                   pg_get_function_identity_arguments(p.oid),
                   pg_get_functiondef(p.oid),
                   l.lanname,
                   pg_get_function_result(p.oid)
            FROM pg_proc p
            JOIN pg_namespace n ON n.oid = p.pronamespace
            JOIN pg_language l ON l.oid = p.prolang
            WHERE n.nspname NOT IN ('pg_catalog','information_schema')
            ORDER BY n.nspname, p.proname, pg_get_function_identity_arguments(p.oid)
            """
        )
        functions = []
        for schema, name, identity_args, definition, language, returns in cur.fetchall():
            functions.append(
                {
                    "name": f"{schema}.{name}({identity_args})",
                    "language": language,
                    "returns": normalize_sql(returns),
                    "body": normalize_body(definition),
                }
            )
        fingerprint["functions"] = functions


_util.write_text(TARGET, json.dumps(fingerprint, separators=(",", ":"), sort_keys=True) + "\n")
PY
