#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from __future__ import annotations

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

try:
    db = _util.db_access()
    fingerprint = db.introspect("fingerprint")
except (
    _util.PrimaryUnavailable,
    _util.IntrospectionError,
):
    fingerprint = offline_fingerprint()

_util.write_json(TARGET, fingerprint)
