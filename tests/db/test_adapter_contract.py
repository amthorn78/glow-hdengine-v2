from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, List
import urllib.error

import pytest

from engine.db.adapter import Statement
from engine.db.errors import BridgeUnavailable
from engine.db.providers.bridge_provider import BridgeProvider, BridgeResponse
from engine.db.providers.psycopg_provider import PsycopgProvider


@dataclass
class FakeCursor:
    fetchone_values: List[Any]
    fetchall_values: List[Any]

    def __post_init__(self) -> None:
        self._fetchone_values = list(self.fetchone_values)
        self._fetchall_values = list(self.fetchall_values)

    def execute(self, sql: str, params=None) -> None:
        # Intentionally no-op; SQL recorded via statements if needed.
        pass

    def fetchall(self):
        if not self._fetchall_values:
            return []
        return self._fetchall_values.pop(0)

    def fetchone(self):
        if not self._fetchone_values:
            return None
        return self._fetchone_values.pop(0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False


class FakeConnection:
    def __init__(self, cursor: FakeCursor):
        self._cursor = cursor
        self.closed = False

    def cursor(self):
        return self._cursor

    def commit(self) -> None:
        pass

    def close(self) -> None:
        self.closed = True


def test_bridge_payload_serialization_is_canonical() -> None:
    recorded: list[str] = []

    def recorder(url: str, method: str, data: bytes | None, headers):
        recorded.append(data.decode("utf-8"))
        body = json.dumps({"status": "ok", "rows": []}).encode("utf-8")
        return BridgeResponse(status=200, body=body, headers={})

    provider = BridgeProvider("https://bridge.example", request=recorder)
    provider.query("SELECT 1", {"b": 2, "a": 1})

    assert recorded == ['{"params":{"a":1,"b":2},"sql":"SELECT 1"}']


def test_bridge_network_errors_are_wrapped() -> None:
    def failing_request(url: str, method: str, data, headers):
        raise urllib.error.URLError("temporary failure")

    provider = BridgeProvider("https://bridge.example", request=failing_request)

    with pytest.raises(BridgeUnavailable) as excinfo:
        provider.health()

    assert excinfo.value.code == "bridge_network_error"
    assert excinfo.value.attempts == ["DATABASE_URL", "DB_BRIDGE_URL"]


def test_psycopg_tx_returns_tuples() -> None:
    provider = PsycopgProvider(
        "postgresql://primary",
        connection_factory=lambda dsn: FakeConnection(
            FakeCursor(fetchone_values=[], fetchall_values=[[["x", "y"]]])
        ),
    )

    statements = [Statement(sql="SELECT 1", fetch=True)]
    results = provider.tx(statements)
    assert results == [[("x", "y")]]


def test_introspect_grants_parity(monkeypatch: pytest.MonkeyPatch) -> None:
    cursor = FakeCursor(
        fetchone_values=[(False, False, False)],
        fetchall_values=[
            [
                ("reader", "hde", "body_graphs", "SELECT"),
                ("reader", "public", "hde_body_graphs_current", "SELECT"),
            ],
            [
                ("hde_migrator", "hde", "r", "reader", "SELECT", False),
            ],
        ],
    )

    provider = PsycopgProvider("postgresql://primary", connection_factory=lambda dsn: FakeConnection(cursor))
    grants_payload = provider.introspect("grants")

    bridge_provider = BridgeProvider(
        "https://bridge.example",
        request=lambda url, method, data, headers: BridgeResponse(
            status=200,
            body=json.dumps({"status": "ok", "payload": grants_payload}).encode("utf-8"),
            headers={},
        ),
    )

    assert bridge_provider.introspect("grants") == grants_payload


def test_introspect_fingerprint_parity(monkeypatch: pytest.MonkeyPatch) -> None:
    cursor = FakeCursor(
        fetchone_values=[("SELECT 1",), ("SELECT 2",)],
        fetchall_values=[
            [
                ("user_id", "uuid", "NO", None),
                ("vendor", "text", "NO", None),
            ],
            [
                ("constraint_name", "UNIQUE (vendor)")
            ],
        ],
    )

    provider = PsycopgProvider("postgresql://primary", connection_factory=lambda dsn: FakeConnection(cursor))
    fingerprint_payload = provider.introspect("fingerprint")

    bridge_provider = BridgeProvider(
        "https://bridge.example",
        request=lambda url, method, data, headers: BridgeResponse(
            status=200,
            body=json.dumps({"status": "ok", "payload": fingerprint_payload}).encode("utf-8"),
            headers={},
        ),
    )

    assert bridge_provider.introspect("fingerprint") == fingerprint_payload
