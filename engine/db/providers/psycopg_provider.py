"""Psycopg-backed DB provider."""
from __future__ import annotations

from contextlib import contextmanager
from hashlib import sha256
from typing import Any, Callable, List, Mapping, Sequence

from ..errors import IntrospectionError, PrimaryUnavailable, SqlExecError, TxError

Params = Sequence[Any] | Mapping[str, Any] | None


_COMMENT_MARKERS = ("--", "/*", "*/")
_OPS03_FIRST_SQL = "SET TRANSACTION READ ONLY"
_OPS03_READONLY_SIGNATURES = (
    # set_transaction_read_only
    ("6c20e5345ee8028f61cc0541aeb60699e5cffa99c8f79ff7f8c62b0a8dad1837", False),
    # set_search_path
    ("af8da0d6f83056f8112485041890d45aaa879a91ecc9f8d6090ef64f2742fb18", False),
    # connection_identity
    ("65ef0b855a313d4658ff116ee5e5af3e82794b4b0ad70562e544b24d9233e0ca", True),
    # search_path
    ("7f61e34d59607c563d6fc7b58be362e7b9fe000e8332a2285c03ddbd5423a4bf", True),
    # runtime_role_grants
    ("ecb83bde8b112f6fadc5bdf5288d42b96e0fc751b80a9406eb2224bdeac0d3c0", True),
    # ddl_columns
    ("86b9c707f5ee72cab35081b9db934ed42728e8b862c7e0daad4d1c1241032eac", True),
    # ddl_constraints
    ("dd5059a30814c3af26ceddbb9398bbcf794c440e547d94f3c7f7ac9a7c4419a4", True),
    # boundary_views
    ("545b8ae329096bb6314830d9f3650ed7882821b761917b66634ec7a3727e3c43", True),
    # partition_inventory
    ("0b341af49cfce830daf0517a2573f3033030269da2e55d01dc3080afb4bbb618", True),
    # partition_verify
    ("e6762f64a95930487ec05bdb15f32f65522f95eb9ee1efee5f31ca03041ab7d8", True),
)


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


def _readonly_statement_signature(statement: Any) -> tuple[str, bool] | None:
    normalized = _single_statement_sql(getattr(statement, "sql", ""))
    if normalized is None or getattr(statement, "params", None) is not None:
        return None
    return sha256(normalized.encode("utf-8")).hexdigest(), bool(
        getattr(statement, "fetch", False)
    )


def validate_readonly_statements(statements: Sequence[Any]) -> None:
    """Fail closed unless *statements* are one bounded read-only SQL batch."""

    signatures = tuple(_readonly_statement_signature(stmt) for stmt in statements)
    first_sql = (
        _single_statement_sql(getattr(statements[0], "sql", ""))
        if statements
        else None
    )
    if first_sql != _OPS03_FIRST_SQL or signatures != _OPS03_READONLY_SIGNATURES:
        raise TxError(
            "readonly_tx_roster_mismatch",
            attempts=["DATABASE_URL"],
            code="readonly_tx_roster_mismatch",
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
        failed = False
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1")
        except Exception:  # pragma: no cover - connection failure mocked in tests
            failed = True
        if failed:
            raise PrimaryUnavailable(
                "primary_connect_failed",
                attempts=["DATABASE_URL"],
                code="primary_connect_failed",
            ) from None

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        failed = False
        rows: Sequence[Sequence[Any]] = ()
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                    rows = cur.fetchall()
                conn.commit()
        except Exception:
            failed = True
        if failed:
            raise SqlExecError(
                "sql_query_failed",
                attempts=["DATABASE_URL"],
                code="sql_query_failed",
            ) from None
        return [tuple(row) if not isinstance(row, tuple) else row for row in rows]

    def exec(self, sql: str, params: Params = None) -> None:
        failed = False
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                conn.commit()
        except Exception:
            failed = True
        if failed:
            raise SqlExecError(
                "sql_exec_failed",
                attempts=["DATABASE_URL"],
                code="sql_exec_failed",
            ) from None

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
        failure: TxError | None = None
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
                                results.append([tuple(row) if not isinstance(row, tuple) else row for row in fetched])
                            else:
                                results.append(None)
                except Exception:
                    failure = TxError(
                        "readonly_tx_failed",
                        attempts=["DATABASE_URL"],
                        code="readonly_tx_failed",
                    )
                try:
                    conn.rollback()
                except Exception:
                    if failure is None:
                        failure = TxError(
                            "readonly_tx_rollback_failed",
                            attempts=["DATABASE_URL"],
                            code="readonly_tx_rollback_failed",
                        )
        except Exception:
            if failure is None:
                failure = TxError(
                    "readonly_tx_failed",
                    attempts=["DATABASE_URL"],
                    code="readonly_tx_failed",
                )
        if failure is not None:
            raise failure from None
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
