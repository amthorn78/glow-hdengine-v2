#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$ROOT_DIR"

python - <<'PY'
from scripts.db import _util

TARGET = "artifacts/db/grants.txt"


def write_lines(lines: list[str]) -> None:
    _util.write_text(TARGET, "\n".join(lines) + "\n")


try:
    db = _util.db_access()
    payload = db.introspect("grants")
except (
    _util.PrimaryUnavailable,
    _util.BridgeUnavailable,
    _util.BridgeUnsupported,
    _util.IntrospectionError,
):
    write_lines([
        "missing_db_config: unable to inspect grants",
    ])
    raise SystemExit(0)

flags = payload.get("flags", {})
if any(bool(flags.get(key)) for key in ("rolsuper", "rolcreatedb", "rolcreaterole")):
    raise SystemExit("app role must not have SUPERUSER, CREATEDB, or CREATEROLE")

grants = payload.get("grants", [])
if grants:
    formatted = [f"{grantee} {obj} {priv}" for grantee, obj, priv in grants]
else:
    formatted = ["(no explicit grants)"]

lines: list[str] = []
lines.extend(formatted)
lines.append("")
lines.append("ALTER DEFAULT PRIVILEGES:")

defaults = payload.get("default_privileges", [])
if defaults:
    lines.extend(defaults)
else:
    lines.append("(none)")

write_lines(lines)
