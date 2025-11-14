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
    with _util.connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT rolsuper, rolcreatedb, rolcreaterole FROM pg_roles WHERE rolname = current_user"
            )
            flags = cur.fetchone() or (False, False, False)
            if any(flags):
                raise SystemExit("app role must not have SUPERUSER, CREATEDB, or CREATEROLE")

            cur.execute(
                """
                SELECT grantee, table_schema, table_name, privilege_type
                FROM information_schema.table_privileges
                WHERE table_schema IN ('hde','public')
                  AND table_name IN ('body_graphs','body_graphs_current','hde_body_graphs_current')
                  AND grantee NOT IN ('pg_catalog','information_schema')
                UNION ALL
                SELECT grantee, routine_schema, routine_name, privilege_type
                FROM information_schema.routine_privileges
                WHERE routine_schema IN ('hde','public')
                  AND routine_name IN ('body_graphs_current','hde_body_graphs_current')
                  AND grantee NOT IN ('pg_catalog','information_schema')
                UNION ALL
                SELECT grantee, object_schema, object_name, privilege_type
                FROM information_schema.usage_privileges
                WHERE object_type = 'SEQUENCE'
                  AND object_schema = 'hde'
                  AND grantee NOT IN ('pg_catalog','information_schema')
                """
            )
            rows = cur.fetchall()

            entries = []
            for grantee, schema, name, privilege in rows:
                if not (grantee and schema and name and privilege):
                    continue
                entries.append((grantee, f"{schema}.{name}", privilege))

            entries = sorted(dict.fromkeys(entries))

            cur.execute(
                """
                SELECT
                    pg_get_userbyid(d.defaclrole) AS owner,
                    COALESCE(n.nspname, 'public') AS schema_name,
                    d.defaclobjtype,
                    pg_get_userbyid(priv.grantee) AS grantee,
                    priv.privilege_type,
                    priv.is_grantable
                FROM pg_default_acl d
                LEFT JOIN pg_namespace n ON n.oid = d.defaclnamespace
                CROSS JOIN LATERAL aclexplode(d.defaclacl) AS priv
                WHERE pg_get_userbyid(d.defaclrole) = 'hde_migrator'
                ORDER BY owner, schema_name, d.defaclobjtype, grantee, priv.privilege_type
                """
            )
            adp_rows = cur.fetchall()

    lines: list[str] = []
    if entries:
        for grantee, obj, privilege in entries:
            lines.append(f"{grantee} {obj} {privilege}")
    else:
        lines.append("(no explicit grants)")

    lines.append("")
    lines.append("ALTER DEFAULT PRIVILEGES:")

    LABELS = {
        "r": "TABLE",
        "S": "SEQUENCE",
        "f": "FUNCTION",
        "T": "TYPE",
        "n": "SCHEMA",
    }

    if adp_rows:
        for owner, schema_name, objtype, grantee, privilege_type, is_grantable in adp_rows:
            label = LABELS.get(objtype, objtype)
            grantable = " WITH GRANT OPTION" if is_grantable else ""
            lines.append(
                f"{owner} {schema_name} {label} {grantee} {privilege_type}{grantable}"
            )
    else:
        lines.append("(none)")

    write_lines(lines)
except _util.MissingDbConfigError:
    write_lines([
        "(missing_db_config: unable to inspect grants)",
    ])
PY
