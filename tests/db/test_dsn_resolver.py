from __future__ import annotations

from types import SimpleNamespace

import pytest

from scripts.db import _util


class DummyConn:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def close(self):
        pass


def _stub_psycopg(monkeypatch: pytest.MonkeyPatch, *, behavior: dict[str, str]) -> None:
    def connect(dsn: str, *, connect_timeout: int = 5):  # noqa: D401 - test stub
        outcome = behavior.get(dsn, "raise")
        if outcome == "ok":
            return DummyConn()
        if outcome == "raise":
            raise RuntimeError(f"boom:{dsn}")
        raise AssertionError(f"unexpected outcome {outcome!r} for {dsn!r}")

    monkeypatch.setattr(_util, "psycopg", SimpleNamespace(connect=connect))


def test_dsn_resolver_prefers_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "postgresql://bridge")
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("ENGINE_ENV", raising=False)

    _stub_psycopg(monkeypatch, behavior={"postgresql://primary": "ok"})

    assert _util.dsn_for_db_scripts() == "postgresql://primary"


def test_dsn_resolver_falls_back_to_bridge(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "postgresql://bridge")
    monkeypatch.setenv("APP_ENV", "dev")

    _stub_psycopg(
        monkeypatch,
        behavior={
            "postgresql://primary": "raise",
            "postgresql://bridge": "ok",
        },
    )

    assert _util.dsn_for_db_scripts() == "postgresql://bridge"


def test_dsn_resolver_requires_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("DB_BRIDGE_URL", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("ENGINE_ENV", raising=False)

    _stub_psycopg(monkeypatch, behavior={})

    with pytest.raises(_util.MissingDbConfigError) as excinfo:
        _util.dsn_for_db_scripts()

    assert str(excinfo.value) == "missing_db_config"


def test_dsn_resolver_no_fallback_in_prod(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://primary")
    monkeypatch.setenv("DB_BRIDGE_URL", "postgresql://bridge")
    monkeypatch.setenv("APP_ENV", "prod")

    _stub_psycopg(
        monkeypatch,
        behavior={
            "postgresql://primary": "raise",
        },
    )

    with pytest.raises(_util.MissingDbConfigError) as excinfo:
        _util.dsn_for_db_scripts()

    assert excinfo.value.attempts == ["DATABASE_URL", "DB_BRIDGE_URL"]
