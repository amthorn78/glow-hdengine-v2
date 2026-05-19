from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.db.adapter import DBAccess
from engine.db.errors import BridgeUnavailable, PrimaryUnavailable

SNAPSHOT_PATH = Path("artifacts/db_bridge/adapter_selection.snapshot.json")


class FakeProvider:
    def __init__(self, name: str, *, healthy: bool = True, error: Exception | None = None):
        self.name = name
        self._healthy = healthy
        self._error = error

    def health(self) -> None:
        if self._error is not None:
            raise self._error
        if not self._healthy:
            raise RuntimeError("unhealthy")

    def query(self, sql: str, params=None):  # pragma: no cover - not used in selection tests
        return []

    def exec(self, sql: str, params=None):  # pragma: no cover - not used in selection tests
        return None

    def tx(self, statements):  # pragma: no cover - not used in selection tests
        return [None for _ in statements]

    def introspect(self, kind: str):  # pragma: no cover - not used in selection tests
        return None


@pytest.fixture(autouse=True)
def _clean_snapshot(monkeypatch):
    if SNAPSHOT_PATH.exists():
        SNAPSHOT_PATH.unlink()
    monkeypatch.chdir(Path.cwd())
    yield
    if SNAPSHOT_PATH.exists():
        SNAPSHOT_PATH.unlink()


def _read_snapshot() -> dict[str, object]:
    assert SNAPSHOT_PATH.exists(), "expected adapter snapshot to be written"
    return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))


def test_primary_success_selects_psycopg(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.delenv("DB_BRIDGE_URL", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("ENGINE_ENV", raising=False)

    db = DBAccess.for_current_env(
        psycopg_factory=lambda dsn: FakeProvider("psycopg"),
        bridge_factory=lambda url: FakeProvider("bridge"),
    )

    assert db.provider_name == "psycopg"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "psycopg"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "ok"},
    ]


def test_bridge_fallback_when_primary_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "dev")

    primary_error = PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    db = DBAccess.for_current_env(
        psycopg_factory=lambda dsn: FakeProvider("psycopg", error=primary_error),
        bridge_factory=lambda url: FakeProvider("bridge"),
    )

    assert db.provider_name == "bridge"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "bridge"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
        {"provider": "bridge", "status": "ok"},
    ]


def test_force_bridge_flag(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("DB_FORCE_BRIDGE", "1")

    db = DBAccess.for_current_env(
        psycopg_factory=lambda dsn: FakeProvider("psycopg"),
        bridge_factory=lambda url: FakeProvider("bridge"),
    )

    assert db.provider_name == "bridge"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "bridge"
    assert snapshot["attempts"] == [
        {"provider": "bridge", "status": "ok"},
    ]


def test_prod_guard_blocks_bridge(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "prod")

    primary_error = PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    with pytest.raises(PrimaryUnavailable):
        DBAccess.for_current_env(
            psycopg_factory=lambda dsn: FakeProvider("psycopg", error=primary_error),
            bridge_factory=lambda url: FakeProvider("bridge"),
        )

    snapshot = _read_snapshot()
    assert snapshot["selected"] == "none"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
        {"provider": "bridge", "status": "skip", "reason": "guard_blocked"},
    ]


def test_prod_guard_can_be_overridden(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "prod")
    monkeypatch.setenv("DB_ALLOW_BRIDGE_IN_PROD", "1")

    primary_error = PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    db = DBAccess.for_current_env(
        psycopg_factory=lambda dsn: FakeProvider("psycopg", error=primary_error),
        bridge_factory=lambda url: FakeProvider("bridge"),
    )

    assert db.provider_name == "bridge"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "bridge"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
        {"provider": "bridge", "status": "ok"},
    ]


def test_stage_allows_bridge_when_primary_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "stage")

    primary_error = PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    db = DBAccess.for_current_env(
        psycopg_factory=lambda dsn: FakeProvider("psycopg", error=primary_error),
        bridge_factory=lambda url: FakeProvider("bridge"),
    )

    assert db.provider_name == "bridge"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "bridge"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
        {"provider": "bridge", "status": "ok"},
    ]


def test_live_env_uses_prod_bridge_guard(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "live")

    primary_error = PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    with pytest.raises(PrimaryUnavailable):
        DBAccess.for_current_env(
            psycopg_factory=lambda dsn: FakeProvider("psycopg", error=primary_error),
            bridge_factory=lambda url: FakeProvider("bridge"),
        )

    snapshot = _read_snapshot()
    assert snapshot["selected"] == "none"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
        {"provider": "bridge", "status": "skip", "reason": "guard_blocked"},
    ]


def test_nondev_total_failure_missing_config_is_typed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DB_BRIDGE_URL", raising=False)
    monkeypatch.setenv("APP_ENV", "stage")

    with pytest.raises(BridgeUnavailable) as excinfo:
        DBAccess.for_current_env(
            psycopg_factory=lambda dsn: FakeProvider("psycopg"),
            bridge_factory=lambda url: FakeProvider("bridge"),
        )

    assert excinfo.value.code == "missing_bridge_url"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "none"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "skip", "reason": "missing_database_url"},
        {"provider": "bridge", "status": "skip", "reason": "missing_bridge_url"},
    ]


def test_prod_total_failure_missing_database_url_is_typed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("APP_ENV", "prod")

    with pytest.raises(PrimaryUnavailable) as excinfo:
        DBAccess.for_current_env(
            psycopg_factory=lambda dsn: FakeProvider("psycopg"),
            bridge_factory=lambda url: FakeProvider("bridge"),
        )

    assert excinfo.value.code == "missing_database_url"
    snapshot = _read_snapshot()
    assert snapshot["selected"] == "none"
    assert snapshot["attempts"] == [
        {"provider": "psycopg", "status": "skip", "reason": "missing_database_url"},
        {"provider": "bridge", "status": "skip", "reason": "guard_blocked"},
    ]
