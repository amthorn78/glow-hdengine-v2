"""Psycopg-backed DB provider."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Callable, List, Mapping, Sequence

from ..errors import IntrospectionError, PrimaryUnavailable, SqlExecError, TxError

Params = Sequence[Any] | Mapping[str, Any] | None


_COMMENT_MARKERS = ("--", "/*", "*/")
_MUTATING_TOKENS = frozenset(
    {"ALTER", "CALL", "COPY", "CREATE", "DELETE", "DO", "DROP", "GRANT",
     "INSERT", "INTO", "LOCK", "MERGE", "REVOKE", "SHARE", "TRUNCATE", "UPDATE"}
)
_SIDE_EFFECT_OR_SENSITIVE_TOKENS = frozenset(
    {
        "DBLINK_CONNECT",
        "DBLINK_EXEC",
        "LO_CREATE",
        "LO_UNLINK",
        "NEXTVAL",
        "PG_ADVISORY_LOCK",
        "PG_ADVISORY_LOCK_SHARED",
        "PG_ADVISORY_UNLOCK",
        "PG_ADVISORY_UNLOCK_ALL",
        "PG_ADVISORY_UNLOCK_SHARED",
        "PG_CANCEL_BACKEND",
        "PG_LOGICAL_EMIT_MESSAGE",
        "PG_LS_DIR",
        "PG_NOTIFY",
        "PG_READ_BINARY_FILE",
        "PG_READ_FILE",
        "PG_SLEEP",
        "PG_STAT_FILE",
        "PG_TERMINATE_BACKEND",
        "SET_CONFIG",
        "SETVAL",
    }
)
_SQL_TOKEN_SEPARATORS = str.maketrans({char: " " for char in "()[],.=+-*/%<>!|'\""})
_OPS_SEARCH_PATH = "SET LOCAL SEARCH_PATH TO HDE, PUBLIC"
_MAX_READONLY_STATEMENTS = 10


def _single_statement_sql(sql: str) -> str | None:
    """Return one normalized statement, rejecting batching and comment tricks."""

    if not isinstance(sql, str):
        return None
    stripped = sql.strip()
    if not stripped or any(marker in stripped for marker in _COMMENT_MARKERS):
        return None
    if stripped.endswith(";"):
        stripped = stripped[:-1].rstrip()
    if not stripped or ";" in stripped:
        return None
    return " ".join(stripped.split()).upper()


def _normalized_sql(sql: str) -> str:
    return _single_statement_sql(sql) or ""


def _readonly_sql_allowed(sql: str, *, first: bool = False) -> bool:
    normalized = _single_statement_sql(sql)
    if normalized is None:
        return False
    if first:
        return normalized == "SET TRANSACTION READ ONLY"
    if normalized == _OPS_SEARCH_PATH:
        return True
    if normalized.startswith("SHOW "):
        return normalized == "SHOW SEARCH_PATH"
    if not normalized.startswith("SELECT "):
        return False
    words = set(normalized.translate(_SQL_TOKEN_SEPARATORS).split())
    return words.isdisjoint(_MUTATING_TOKENS | _SIDE_EFFECT_OR_SENSITIVE_TOKENS)


def validate_readonly_statements(statements: Sequence[Any]) -> None:
    """Fail closed unless *statements* are one bounded read-only SQL batch."""

    if not statements:
        raise TxError(
            "readonly_tx_requires_statements",
            attempts=["DATABASE_URL"],
            code="readonly_tx_requires_statements",
        )
    if len(statements) > _MAX_READONLY_STATEMENTS:
        raise TxError(
            "readonly_tx_too_many_statements",
            attempts=["DATABASE_URL"],
            code="readonly_tx_too_many_statements",
        )
    sqls = [getattr(stmt, "sql", "") for stmt in statements]
    if not _readonly_sql_allowed(sqls[0], first=True):
        raise TxError(
            "readonly_tx_requires_read_only_first",
            attempts=["DATABASE_URL"],
            code="readonly_tx_requires_read_only_first",
        )
    if any(not _readonly_sql_allowed(sql) for sql in sqls[1:]):
        raise TxError(
            "readonly_tx_rejected_sql",
            attempts=["DATABASE_URL"],
            code="readonly_tx_rejected_sql",
        )


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

    def tx(
        self,
        statements: Sequence[Any],
        *,
        validate: Callable[[Sequence[Sequence[Any] | None]], None] | None = None,
    ) -> List[Sequence[Any] | None]:
        results: List[Sequence[Any] | None] = []
        try:
            with self._connect() as conn:
                try:
                    with conn.cursor() as cur:
                        for stmt in statements:
                            sql = getattr(stmt, "sql")
                            params = getattr(stmt, "params", None)
                            fetch = bool(getattr(stmt, "fetch", False))
                            cur.execute(sql, params)
                            if fetch:
                                fetched = cur.fetchall()
                                results.append(
                                    [
                                        tuple(row) if not isinstance(row, tuple) else row
                                        for row in fetched
                                    ]
                                )
                            else:
                                results.append(None)
                    if validate is not None:
                        validate(tuple(results))
                    conn.commit()
                except Exception:
                    try:
                        conn.rollback()
                    except Exception as exc:
                        raise TxError(
                            "tx_rollback_failed",
                            attempts=["DATABASE_URL"],
                            code="tx_rollback_failed",
                        ) from exc
                    raise
        except TxError:
            raise
        except Exception as exc:
            raise TxError(
                "tx_failed",
                attempts=["DATABASE_URL"],
                code="tx_failed",
            ) from exc
        return results


    def readonly_tx(self, statements: Sequence[Any]) -> List[Sequence[Any] | None]:
        validate_readonly_statements(statements)
        results: List[Sequence[Any] | None] = []
        try:
            with self._connect() as conn:
                transaction_failed = False
                try:
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
                except TxError:
                    transaction_failed = True
                    raise
                except Exception as exc:
                    transaction_failed = True
                    raise TxError(
                        "readonly_tx_failed",
                        attempts=["DATABASE_URL"],
                        code="readonly_tx_failed",
                    ) from exc
                finally:
                    try:
                        conn.rollback()
                    except Exception as exc:
                        if not transaction_failed:
                            raise TxError(
                                "readonly_tx_rollback_failed",
                                attempts=["DATABASE_URL"],
                                code="readonly_tx_rollback_failed",
                            ) from exc
        except TxError:
            raise
        except Exception as exc:
            raise TxError(
                "readonly_tx_failed",
                attempts=["DATABASE_URL"],
                code="readonly_tx_failed",
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
        if kind == "version":
            return self._introspect_version()
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

    def _introspect_version(self) -> Mapping[str, Any]:
        try:
            rows = self.query("SELECT current_setting('server_version')")
        except SqlExecError as exc:
            raise IntrospectionError(
                "version_unavailable",
                attempts=["DATABASE_URL"],
                code="version_unavailable",
            ) from exc

        version = ""
        if rows and rows[0]:
            first = rows[0]
            version = str(first[0]) if first else ""

        return {"status": "ok", "version": version}
