from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.bodygraph.ingest import VendorInputs, ingest_vendor_bodygraph
from engine.bodygraph.vendor_client import VendorError, VendorRequest, VendorResult


class FakeClient:
    def __init__(self) -> None:
        self.request = VendorRequest(
            url="https://vendor.test/v1/bodygraphs",
            headers={},
            body_bytes=b"{}\n",
            input_fingerprint="abc123",
            route="vendor.hdapi.post:/bodygraphs",
        )

    def build_request(self, *, birthdate: str, birthtime: str, location: str) -> VendorRequest:
        return self.request

    def fetch(self, request: VendorRequest) -> VendorResult:
        return VendorResult(payload={"ok": True}, duration_ms=12.0, attempts=1)


class FakeDB:
    def __init__(self) -> None:
        self.rows: dict[tuple[str, str], str] = {}

    def tx(self, statements):
        stmt = statements[0]
        params = stmt.params
        key = (params[0], params[3])
        if key in self.rows:
            return [[]]
        self.rows[key] = params[4]
        return [[(1,)]]

    def query(self, sql: str, params):
        key = (params[0], params[3])
        if "COUNT" in sql:
            exists = 1 if key in self.rows else 0
            return [(exists,)]
        payload = self.rows.get(key)
        if payload is None:
            return []
        return [(payload,)]


def test_ingest_idempotent(tmp_path: Path) -> None:
    client = FakeClient()
    db = FakeDB()
    env = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1"}
    logs_dir = tmp_path / "logs"
    success_log = logs_dir / "success.log"
    retry_log = logs_dir / "retry.log"
    canon_log = logs_dir / "canon.log"
    inputs = VendorInputs(
        user_id="user-1",
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam",
    )

    outcome1 = ingest_vendor_bodygraph(
        inputs,
        env=env,
        client=client,
        db_access=db,
        success_log=success_log,
        retry_log=retry_log,
        canon_log=canon_log,
    )
    outcome2 = ingest_vendor_bodygraph(
        inputs,
        env=env,
        client=client,
        db_access=db,
        success_log=success_log,
        retry_log=retry_log,
        canon_log=canon_log,
    )

    assert outcome1.rows_written == 1
    assert outcome2.rows_written == 0
    assert outcome1.parity_match is True
    assert outcome2.parity_match is True
    records = [json.loads(line) for line in success_log.read_text(encoding="utf-8").splitlines()]
    assert len(records) == 2
    assert records[0]["rows_affected"] == 1
    assert records[1]["rows_affected"] == 0
    canon_records = [json.loads(line) for line in canon_log.read_text(encoding="utf-8").splitlines()]
    assert canon_records
    assert canon_records[-1]["match"] is True
    assert canon_records[-1]["vendor_sha256"] == canon_records[-1]["db_emitted_sha256"]
    assert outcome1.payload == {"ok": True}


def test_ingest_dry_run_skips_db(monkeypatch: pytest.MonkeyPatch) -> None:
    client = FakeClient()
    env = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1"}
    called = False

    def _boom():
        nonlocal called
        called = True
        raise AssertionError("DB should not be touched during dry-run")

    monkeypatch.setattr("engine.bodygraph.ingest.DBAccess.for_current_env", lambda: _boom())
    outcome = ingest_vendor_bodygraph(
        VendorInputs(
            user_id="user-2",
            birthdate="1991-02-02",
            birthtime="01:02",
            location="Paris",
        ),
        env=env,
        client=client,
        dry_run=True,
    )

    assert called is False
    assert outcome.rows_written == 0
    assert outcome.db_rows_after == 0
    assert outcome.parity_match is True
    assert outcome.payload == {"ok": True}


def test_direct_ingest_rejects_v2_chart_route_before_fetch() -> None:
    class V2ChartClient:
        def __init__(self) -> None:
            self.fetch_called = False

        def build_request(self, *, birthdate: str, birthtime: str, location: str) -> VendorRequest:
            return VendorRequest(
                url="https://vendor.test/v2/charts",
                headers={"Authorization": "Bearer raw", "HD-Geocode-Key": "raw"},
                body_bytes=b"{}\n",
                input_fingerprint="v2-chart-fingerprint",
                route="vendor.hdapi.post:/charts",
            )

        def fetch(self, request: VendorRequest) -> VendorResult:
            self.fetch_called = True
            return VendorResult(payload={"raw": "chart-result"}, duration_ms=1.0, attempts=1)

    client = V2ChartClient()

    with pytest.raises(VendorError) as excinfo:
        ingest_vendor_bodygraph(
            VendorInputs(
                user_id="user-v2",
                birthdate="1990-01-01",
                birthtime="12:00",
                location="Amsterdam",
            ),
            env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1"},
            client=client,
            dry_run=True,
        )

    assert excinfo.value.code == "PROVIDER_ROUTE_UNSUPPORTED"
    assert excinfo.value.details["route"] == "vendor.hdapi.post:/charts"
    assert excinfo.value.details["expected_route"] == "vendor.hdapi.post:/bodygraphs"
    assert excinfo.value.details["persistence"] == "refused"
    assert client.fetch_called is False
