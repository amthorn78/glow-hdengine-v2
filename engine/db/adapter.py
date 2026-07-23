"""High-level direct-only DB adapter."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Protocol, Sequence
import os

from .providers.psycopg_provider import PsycopgProvider
from .errors import AdapterError, IntrospectionError, PrimaryUnavailable, RetiredBridgeConfiguration

Params = Sequence[Any] | Mapping[str, Any] | None
TxResult = Sequence[Any] | None
TxValidator = Callable[[Sequence[TxResult]], None]

RETIRED_DB_TRANSPORT_KEYS: tuple[str, ...] = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)

_SAFE_APP_ENV_NAMES = frozenset(
    {"ci", "dev", "local", "prod", "production", "staging", "test"}
)


def _environment_key_names(environ: Mapping[str, str]) -> frozenset[str]:
    """Return environment key names without reading any mapped value."""
    return frozenset(iter(environ))


def retired_db_transport_keys_present(environ: Mapping[str, str]) -> tuple[str, ...]:
    """Return retired transport key names present in *environ*, independent of value."""
    present = _environment_key_names(environ)
    return tuple(name for name in RETIRED_DB_TRANSPORT_KEYS if name in present)


def _safe_app_env_name(environ: Mapping[str, str]) -> str:
    """Return a bounded environment label without serializing arbitrary input."""

    name = (environ.get("APP_ENV") or "dev").strip().lower()
    return name if name in _SAFE_APP_ENV_NAMES else "unknown"


@dataclass(frozen=True)
class Statement:
    """Represents a SQL statement executed within a transaction."""
    sql: str
    params: Params = None
    fetch: bool = False


class Provider(Protocol):
    name: str
    def health(self) -> None: ...
    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]: ...
    def exec(self, sql: str, params: Params = None) -> None: ...
    def tx(
        self,
        statements: Sequence[Statement],
        *,
        validate: TxValidator | None = None,
    ) -> List[TxResult]: ...
    def readonly_tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]: ...
    def introspect(self, kind: str) -> Any: ...


def _canonical_attempt(provider: str, status: str, *, reason: str | None = None) -> Dict[str, Any]:
    return {"provider": provider, "status": status, "reason": reason}


def _normalize_introspect_payload(kind: str, payload: Any) -> Dict[str, Any]:
    if isinstance(payload, Mapping):
        result = dict(payload)
        result.setdefault("status", "ok")
        return result
    if kind == "search_path":
        return {"status": "ok", "search_path": str(payload)}
    if kind == "version":
        return {"status": "ok", "version": str(payload)}
    raise IntrospectionError(f"unexpected_introspection_payload:{kind}", code="unexpected_introspection_payload")


class DBAccess:
    """High-level façade exposing direct PostgreSQL DB operations."""

    def __init__(
        self,
        provider: Provider,
        *,
        attempts: Sequence[Mapping[str, Any]] | None = None,
        selection_case: Mapping[str, object] | None = None,
    ):
        self._provider = provider
        self._attempts = [dict(row) for row in (attempts or ())]
        self._selection_case = dict(selection_case or {})

    @property
    def provider_name(self) -> str:
        return getattr(self._provider, "name", "unknown")

    @property
    def attempts(self) -> Sequence[Mapping[str, Any]]:
        return tuple(dict(row) for row in self._attempts)

    @classmethod
    def for_current_env(
        cls,
        *,
        environ: Mapping[str, str] | None = None,
        psycopg_factory: Callable[[str], Provider] | None = None,
    ) -> "DBAccess":
        env = os.environ if environ is None else environ
        retired = retired_db_transport_keys_present(env)
        if retired:
            exc = RetiredBridgeConfiguration(retired)
            exc.selection_case = cls._retired_failure_case(env, exc)
            exc.attempt_rows = []
            raise exc
        dsn = (env.get("DATABASE_URL") or "").strip()
        attempts: List[Mapping[str, Any]] = []
        if not dsn:
            attempts.append(_canonical_attempt("psycopg", "skip", reason="missing_database_url"))
            exc = PrimaryUnavailable("missing_database_url", attempts=["DATABASE_URL"], code="missing_database_url")
            exc.attempt_rows = [dict(row) for row in attempts]
            exc.selection_case = cls._failure_case(env, exc, attempts=attempts)
            raise exc
        ctor = psycopg_factory or (lambda value: PsycopgProvider(value))
        provider_failed = False
        try:
            provider = ctor(dsn)
            if getattr(provider, "name", None) != "psycopg":
                raise TypeError("unexpected_direct_provider")
            provider.health()
        except Exception:
            provider_failed = True
        if provider_failed:
            attempts.append(_canonical_attempt("psycopg", "error", reason="primary_connect_failed"))
            wrapped = PrimaryUnavailable("primary_connect_failed", attempts=["DATABASE_URL"], code="primary_connect_failed")
            wrapped.attempt_rows = [dict(row) for row in attempts]
            wrapped.selection_case = cls._failure_case(env, wrapped, attempts=attempts)
            raise wrapped from None
        attempts.append(_canonical_attempt("psycopg", "ok", reason=None))
        selection_case: Mapping[str, object] = {
            "case": "healthy_direct",
            "app_env": _safe_app_env_name(env),
            "database_url_presence": "present_redacted",
            "retired_keys_present": [],
            "attempts": attempts,
            "selected": "psycopg",
            "error": None,
            "alternate_transport_attempts": 0,
            "result": "PASS",
        }
        return cls(provider, attempts=attempts, selection_case=selection_case)


    @staticmethod
    def statement(sql: str, params: Params = None, *, fetch: bool = False) -> Statement:
        return Statement(sql=sql, params=params, fetch=fetch)

    @staticmethod
    def _database_url_presence(env: Mapping[str, str]) -> str:
        """Return endpoint presence without reading or serializing its mapped value."""
        return (
            "present_redacted"
            if any(name == "DATABASE_URL" for name in env)
            else "unset"
        )

    @staticmethod
    def _retired_failure_case(env: Mapping[str, str], exc: RetiredBridgeConfiguration) -> Mapping[str, object]:
        return {
            "case": "retired_keys_present",
            "app_env": _safe_app_env_name(env),
            "database_url_presence": DBAccess._database_url_presence(env),
            "retired_keys_present": list(exc.retired_keys),
            "attempts": [],
            "selected": "none",
            "error": {"class": exc.__class__.__name__, "code": exc.code},
            "alternate_transport_attempts": 0,
            "result": "PASS",
        }

    @staticmethod
    def _failure_case(env: Mapping[str, str], exc: AdapterError, *, attempts: Sequence[Mapping[str, Any]]) -> Mapping[str, object]:
        retired = list(getattr(exc, "retired_keys", ()))
        if retired and isinstance(exc, RetiredBridgeConfiguration):
            return DBAccess._retired_failure_case(env, exc)
        return {
            "case": "retired_keys_present" if retired else ("missing_database_url" if exc.code == "missing_database_url" else "unavailable_database_url"),
            "app_env": _safe_app_env_name(env),
            "database_url_presence": DBAccess._database_url_presence(env) if exc.code == "missing_database_url" else ("present_redacted" if (env.get("DATABASE_URL") or "").strip() else "unset"),
            "retired_keys_present": retired,
            "attempts": [dict(row) for row in attempts],
            "selected": "none",
            "error": {"class": exc.__class__.__name__, "code": exc.code},
            "alternate_transport_attempts": 0,
            "result": "PASS",
        }

    @staticmethod
    def selection_failure_evidence(exc: AdapterError) -> Mapping[str, object]:
        case = getattr(exc, "selection_case", None)
        if isinstance(case, Mapping):
            return dict(case)
        return {
            "case": "retired_keys_present" if isinstance(exc, RetiredBridgeConfiguration) else "unavailable_database_url",
            "app_env": "dev",
            "database_url_presence": "unset",
            "retired_keys_present": list(getattr(exc, "retired_keys", ())),
            "attempts": [dict(row) for row in getattr(exc, "attempt_rows", [])],
            "selected": "none",
            "error": {"class": exc.__class__.__name__, "code": exc.code},
            "alternate_transport_attempts": 0,
            "result": "PASS",
        }

    def selection_evidence(self) -> Mapping[str, object]:
        """Return the pure, names-only direct-selection case record."""
        return {
            **self._selection_case,
            "attempts": [dict(row) for row in self._attempts],
            "retired_keys_present": list(self._selection_case.get("retired_keys_present", [])),
        }

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        return self._provider.query(sql, params)
    def exec(self, sql: str, params: Params = None) -> None:
        self._provider.exec(sql, params)
    def tx(
        self,
        statements: Sequence[Statement],
        *,
        validate: TxValidator | None = None,
    ) -> List[TxResult]:
        if validate is None:
            return self._provider.tx(statements)
        return self._provider.tx(statements, validate=validate)
    def readonly_tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]:
        return self._provider.readonly_tx(statements)
    def introspect(self, kind: str) -> Any:
        return self._provider.introspect(kind)
    def health(self) -> None:
        self._provider.health()
    def introspect_search_path(self) -> Mapping[str, Any]:
        return _normalize_introspect_payload("search_path", self.introspect("search_path"))
    def introspect_fingerprint(self) -> Mapping[str, Any]:
        return _normalize_introspect_payload("fingerprint", self.introspect("fingerprint"))
    def introspect_version(self) -> Mapping[str, Any]:
        return _normalize_introspect_payload("version", self.introspect("version"))
    def introspect_grants(self) -> Mapping[str, Any]:
        return _normalize_introspect_payload("grants", self.introspect("grants"))
