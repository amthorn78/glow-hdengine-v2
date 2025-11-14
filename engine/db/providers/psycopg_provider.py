"""Psycopg-backed DB provider."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Callable, List, Mapping, Sequence

from ..errors import IntrospectionError, PrimaryUnavailable, SqlExecError, TxError

Params = Sequence[Any] | Mapping[str, Any] | None


class PsycopgProvider:
    """Provider that executes SQL through psycopg."""

    name = "psycopg"

    def __init__(self, dsn: str, *, connection_factory: Callable[[str], Any] | None = None):
        if not dsn:
            raise PrimaryUnavailable(
                "missing_database_url",
                attempts=["DATABASE_URL"],
                code="missing_database_url",
            )
        self._dsn = dsn
        if connection_factory is None:
            import psycopg  # type: ignore

            def connector() -> Any:
                return psycopg.connect(self._dsn, connect_timeout=5)  # type: ignore[attr-defined]

            self._connection_factory = connector
        else:
            self._connection_factory = lambda: connection_factory(self._dsn)

    @contextmanager
    def _connect(self):
        conn = self._connection_factory()
        try:
            yield conn
        finally:
            try:
                conn.close()
            except Exception:
                pass

    def health(self) -> None:
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
        except Exception as exc:  # pragma: no cover - connection failure mocked in tests
            raise PrimaryUnavailable(
                "primary_connect_failed",
                attempts=["DATABASE_URL"],
                code="primary_connect_failed",
            ) from exc

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                    rows = cur.fetchall()
                conn.commit()
        except Exception as exc:
            raise SqlExecError(
                "sql_query_failed",
                attempts=["DATABASE_URL"],
                code="sql_query_failed",
            ) from exc
        return [tuple(row) if not isinstance(row, tuple) else row for row in rows]

    def exec(self, sql: str, params: Params = None) -> None:
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                conn.commit()
        except Exception as exc:
            raise SqlExecError(
                "sql_exec_failed",
                attempts=["DATABASE_URL"],
                code="sql_exec_failed",
            ) from exc

    def tx(self, statements: Sequence[Any]) -> List[Sequence[Any] | None]:
        results: List[Sequence[Any] | None] = []
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    for stmt in statements:
                        sql = getattr(stmt, "sql")
                        params = getattr(stmt, "params", None)
                        fetch = bool(getattr(stmt, "fetch", False))
                        cur.execute(sql, params)
                        if fetch:
                            fetched = cur.fetchall()
                            results.append([tuple(row) if not isinstance(row, tuple) else row for row in fetched])
                        else:
                            results.append(None)
                conn.commit()
        except Exception as exc:
            raise TxError(
                "tx_failed",
                attempts=["DATABASE_URL"],
                code="tx_failed",
            ) from exc
        return results

    def introspect(self, kind: str) -> Any:
        if kind == "search_path":
            rows = self.query("SHOW search_path")
            return (rows[0][0] if rows else "").strip()
        if kind == "grants":
            return self._introspect_grants()
        if kind == "fingerprint":
            return self._introspect_fingerprint()
        raise IntrospectionError(
            f"unknown_introspection_kind:{kind}",
            code="unknown_introspection_kind",
        )

    # helpers -----------------------------------------------------------
    def _introspect_grants(self) -> Mapping[str, Any]:
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT rolsuper, rolcreatedb, rolcreaterole
                        FROM pg_roles
                        WHERE rolname = current_user
                        """
                    )
                    flags = cur.fetchone() or (False, False, False)

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
                    entries = cur.fetchall()

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
        except Exception as exc:
            raise IntrospectionError(
                "grants_unavailable",
                attempts=["DATABASE_URL"],
                code="grants_unavailable",
            ) from exc

        entries_norm = []
        for grantee, schema, name, privilege in entries:
            if not (grantee and schema and name and privilege):
                continue
            entries_norm.append((grantee, f"{schema}.{name}", privilege))
        entries_norm = sorted(dict.fromkeys(entries_norm))

        LABELS = {
            "r": "TABLE",
            "S": "SEQUENCE",
            "f": "FUNCTION",
            "T": "TYPE",
            "n": "SCHEMA",
        }

        defaults: List[str] = []
        for owner, schema_name, objtype, grantee, privilege_type, is_grantable in adp_rows:
            label = LABELS.get(objtype, objtype)
            grantable = " WITH GRANT OPTION" if is_grantable else ""
            defaults.append(
                f"{owner} {schema_name} {label} {grantee} {privilege_type}{grantable}"
            )

        return {
            "flags": {
                "rolsuper": bool(flags[0]),
                "rolcreatedb": bool(flags[1]),
                "rolcreaterole": bool(flags[2]),
            },
            "grants": entries_norm,
            "default_privileges": defaults or ["(none)"],
        }

    def _introspect_fingerprint(self) -> Mapping[str, Any]:
        def normalize_sql(text: str) -> str:
            return " ".join((text or "").split())

        try:
            with self._connect() as conn:
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
                    columns_rows = cur.fetchall()

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
                    constraint_rows = cur.fetchall()

                    views: List[tuple[str, str]] = []
                    for schema, name in (("hde", "body_graphs_current"), ("public", "hde_body_graphs_current")):
                        cur.execute(
                            "SELECT pg_get_viewdef(%s::regclass, true)",
                            (f"{schema}.{name}",),
                        )
                        viewdef = (cur.fetchone() or ("",))[0] or ""
                        views.append((f"{schema}.{name}", normalize_sql(viewdef)))
        except Exception as exc:
            raise IntrospectionError(
                "fingerprint_unavailable",
                attempts=["DATABASE_URL"],
                code="fingerprint_unavailable",
            ) from exc

        columns = []
        for name, data_type, is_nullable, column_default in columns_rows:
            columns.append(
                {
                    "name": name,
                    "data_type": data_type,
                    "nullable": is_nullable == "YES",
                    "default": normalize_sql(column_default or ""),
                }
            )

        constraints = [
            {
                "name": name,
                "definition": normalize_sql(defn),
            }
            for name, defn in constraint_rows
        ]

        fingerprint = {
            "schema": "hde",
            "version": 1,
            "objects": {
                "hde.body_graphs": {
                    "columns": columns,
                    "constraints": constraints,
                }
            },
        }

        for key, definition in views:
            fingerprint["objects"][key] = {"definition": definition}

        return fingerprint
