"""High-level DB adapter with HTTPS bridge fallback."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Mapping, Optional, Protocol, Sequence
import json
import os

from .providers.bridge_provider import BridgeProvider
from .providers.psycopg_provider import PsycopgProvider
from .errors import (
    AdapterError,
    BridgeUnavailable,
    BridgeUnsupported,
    IntrospectionError,
    PrimaryUnavailable,
    SqlExecError,
    TxError,
)


Params = Sequence[Any] | Mapping[str, Any] | None


@dataclass(frozen=True)
class Statement:
    """Represents a SQL statement executed within a transaction."""

    sql: str
    params: Params = None
    fetch: bool = False


class Provider(Protocol):
    """Protocol implemented by concrete DB providers."""

    name: str

    def health(self) -> None:
        ...

    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        ...

    def exec(self, sql: str, params: Params = None) -> None:
        ...

    def tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]:
        ...

    def introspect(self, kind: str) -> Any:
        ...


def _env_tag() -> str:
    value = (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "").strip().lower()
    return value


def _is_dev_env(tag: str) -> bool:
    return tag in {"", "dev", "development", "test", "testing"}


PROD_ENV_ALIASES = {"prod", "production", "live"}


def _is_prod_env(tag: str) -> bool:
    return tag in PROD_ENV_ALIASES


def _snapshot_path(default: str | None) -> Path | None:
    if not default:
        return None
    path = Path(default)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _write_snapshot(path: Path | None, payload: Mapping[str, Any]) -> None:
    if not path:
        return
    text = json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")


def _canonical_attempt(provider: str, status: str, *, reason: str | None = None) -> Dict[str, Any]:
    attempt: Dict[str, Any] = {"provider": provider, "status": status}
    if reason:
        attempt["reason"] = reason
    return attempt


def _normalize_introspect_payload(kind: str, payload: Any) -> Dict[str, Any]:
    if isinstance(payload, Mapping):
        result = dict(payload)
        result.setdefault("status", "ok")
        return result

    if kind == "search_path":
        return {"status": "ok", "search_path": str(payload)}

    if kind == "version":
        return {"status": "ok", "version": str(payload)}

    raise IntrospectionError(
        f"unexpected_introspection_payload:{kind}",
        code="unexpected_introspection_payload",
    )


class DBAccess:
    """High-level façade exposing DB operations across providers."""

    def __init__(self, provider: Provider, *, attempts: Sequence[Mapping[str, Any]] | None = None):
        self._provider = provider
        self._attempts = list(attempts or [])

    @property
    def provider_name(self) -> str:
        return getattr(self._provider, "name", "unknown")

    @property
    def attempts(self) -> Sequence[Mapping[str, Any]]:
        return tuple(self._attempts)

    @classmethod
    def for_current_env(
        cls,
        *,
        snapshot_path: str | None = "artifacts/db_bridge/adapter_selection.snapshot.json",
        psycopg_factory: Callable[[str], Provider] | None = None,
        bridge_factory: Callable[[str], Provider] | None = None,
    ) -> "DBAccess":
        tag = _env_tag()
        dev_env = _is_dev_env(tag)

        dsn = (os.getenv("DATABASE_URL") or "").strip()
        bridge_url = (os.getenv("DB_BRIDGE_URL") or "").strip()

        force_pg = os.getenv("DB_FORCE_PG") == "1"
        force_bridge = os.getenv("DB_FORCE_BRIDGE") == "1"
        allow_bridge_prod = os.getenv("DB_ALLOW_BRIDGE_IN_PROD") == "1"

        attempts: List[Mapping[str, Any]] = []
        selected_provider: Provider | None = None

        snapshot = _snapshot_path(snapshot_path)

        original_force_bridge = force_bridge
        if force_pg:
            force_bridge = False

        order: List[str] = []
        if force_bridge:
            order = ["bridge"]
        elif force_pg:
            order = ["psycopg"]
        else:
            order = ["psycopg", "bridge"]

        last_primary_error: PrimaryUnavailable | None = None
        last_bridge_error: AdapterError | None = None

        bridge_allowed = force_bridge or not _is_prod_env(tag) or allow_bridge_prod

        psycopg_ctor = psycopg_factory or (lambda value: PsycopgProvider(value))
        bridge_ctor = bridge_factory or (lambda value: BridgeProvider(value))

        for provider_name in order:
            if provider_name == "psycopg":
                if not dsn:
                    last_primary_error = PrimaryUnavailable(
                        "missing_database_url",
                        attempts=["DATABASE_URL"],
                        code="missing_database_url",
                    )
                    attempts.append(_canonical_attempt("psycopg", "skip", reason="missing_database_url"))
                    continue
                try:
                    provider = psycopg_ctor(dsn)
                    provider.health()
                except PrimaryUnavailable as exc:
                    last_primary_error = exc
                    attempts.append(_canonical_attempt("psycopg", "error", reason=exc.code))
                    continue
                selected_provider = provider
                attempts.append(_canonical_attempt("psycopg", "ok"))
                break

            if provider_name == "bridge":
                if not bridge_url:
                    last_bridge_error = BridgeUnavailable(
                        "missing_bridge_url",
                        attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                        code="missing_bridge_url",
                    )
                    attempts.append(_canonical_attempt("bridge", "skip", reason="missing_bridge_url"))
                    continue
                if not bridge_allowed:
                    last_bridge_error = BridgeUnavailable(
                        "bridge_guard_blocked",
                        attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                        code="guard_blocked",
                    )
                    attempts.append(_canonical_attempt("bridge", "skip", reason="guard_blocked"))
                    continue
                try:
                    provider = bridge_ctor(bridge_url)
                    provider.health()
                except BridgeUnsupported as exc:
                    last_bridge_error = exc
                    attempts.append(_canonical_attempt("bridge", "error", reason=exc.code))
                    continue
                except BridgeUnavailable as exc:
                    last_bridge_error = exc
                    attempts.append(_canonical_attempt("bridge", "error", reason=exc.code))
                    continue
                selected_provider = provider
                attempts.append(_canonical_attempt("bridge", "ok"))
                break

        selection_order = [
            attempt["provider"]
            for attempt in attempts
            if isinstance(attempt, Mapping) and "provider" in attempt
        ]

        snapshot_payload: Dict[str, Any] = {
            "schema": "v1",
            "selected": getattr(selected_provider, "name", "none"),
            "attempts": attempts,
            "selection_order": selection_order,
            "flags": {
                "env": tag or "unset",
                "force_pg": force_pg,
                "force_bridge": bool(original_force_bridge),
                "allow_bridge_prod": allow_bridge_prod,
            },
        }
        _write_snapshot(snapshot, snapshot_payload)

        if not selected_provider:
            if last_primary_error and not bridge_allowed:
                raise last_primary_error
            if last_bridge_error and (force_bridge or bridge_allowed):
                raise last_bridge_error
            if last_primary_error and not last_bridge_error:
                raise last_primary_error
            if last_bridge_error:
                raise last_bridge_error
            raise PrimaryUnavailable(
                "missing_db_config",
                attempts=["DATABASE_URL", "DB_BRIDGE_URL"],
                code="missing_db_config",
            )

        return cls(selected_provider, attempts=attempts)

    # façade operations -------------------------------------------------
    def query(self, sql: str, params: Params = None) -> List[Sequence[Any]]:
        return self._provider.query(sql, params)

    def exec(self, sql: str, params: Params = None) -> None:
        self._provider.exec(sql, params)

    def tx(self, statements: Sequence[Statement]) -> List[Sequence[Any] | None]:
        return self._provider.tx(statements)

    def introspect(self, kind: str) -> Any:
        return self._provider.introspect(kind)

    def health(self) -> None:
        self._provider.health()

    # structured introspection helpers ----------------------------------
    def introspect_search_path(self) -> Mapping[str, Any]:
        payload = self.introspect("search_path")
        return _normalize_introspect_payload("search_path", payload)

    def introspect_fingerprint(self) -> Mapping[str, Any]:
        payload = self.introspect("fingerprint")
        return _normalize_introspect_payload("fingerprint", payload)

    def introspect_version(self) -> Mapping[str, Any]:
        payload = self.introspect("version")
        return _normalize_introspect_payload("version", payload)
