"""High-level direct-only DB adapter."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Protocol, Sequence
import os

from .providers.psycopg_provider import PsycopgProvider
from .errors import AdapterError, IntrospectionError, PrimaryUnavailable, RetiredBridgeConfiguration

Params = Sequence[Any] | Mapping[str, Any] | None

RETIRED_DB_TRANSPORT_KEYS: tuple[str, ...] = (
    "DB_ALLOW_BRIDGE_IN_PROD",
    "DB_BRIDGE_URL",
    "DB_FORCE_BRIDGE",
)


def retired_db_transport_keys_present(environ: Mapping[str, str]) -> tuple[str, ...]:
    """Return retired transport key names present in *environ*, independent of value."""
    return tuple(sorted(name for name in RETIRED_DB_TRANSPORT_KEYS if name in environ))


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
    def tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]: ...
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
            raise RetiredBridgeConfiguration(retired)
        dsn = (env.get("DATABASE_URL") or "").strip()
        attempts: List[Mapping[str, Any]] = []
        if not dsn:
            attempts.append(_canonical_attempt("psycopg", "skip", reason="missing_database_url"))
            raise PrimaryUnavailable("missing_database_url", attempts=["DATABASE_URL"], code="missing_database_url")
        ctor = psycopg_factory or (lambda value: PsycopgProvider(value))
        try:
            provider = ctor(dsn)
            provider.health()
        except PrimaryUnavailable as exc:
            attempts.append(_canonical_attempt("psycopg", "error", reason=exc.code))
            raise
        except Exception as exc:
            attempts.append(_canonical_attempt("psycopg", "error", reason="primary_connect_failed"))
            raise PrimaryUnavailable("primary_connect_failed", attempts=["DATABASE_URL"], code="primary_connect_failed") from exc
        attempts.append(_canonical_attempt("psycopg", "ok", reason=None))
        selection_case: Mapping[str, object] = {
            "case": "healthy_direct",
            "app_env": (env.get("APP_ENV") or "dev").strip() or "dev",
            "database_url_presence": "present_redacted",
            "retired_keys_present": [],
            "attempts": attempts,
            "selected": "psycopg",
            "error": None,
            "alternate_transport_attempts": 0,
            "result": "PASS",
        }
        return cls(provider, attempts=attempts, selection_case=selection_case)

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
    def tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]:
        return self._provider.tx(statements)
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

