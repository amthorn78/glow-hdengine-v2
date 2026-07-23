from __future__ import annotations

import json
from pathlib import Path
import uuid

import pytest

from engine.bodygraph.mapped_cache import MappedCacheError, MappedCacheResult
from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import VendorRequest, VendorResult
from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable

ROOT = Path(__file__).resolve().parents[2]
CHART = json.loads((ROOT / "tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json").read_text())["payload"]


def env(**changes):
    value = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v2", "HD_API_KEY": "set", "GEO_API_KEY": "set"}
    value.update(changes)
    return value


class Client:
    calls = 0
    def build_contract_route_request(self, **kwargs):
        return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=b"{}\n", input_fingerprint="a" * 64, route="vendor.hdapi.post:/charts")
    def fetch(self, request):
        self.calls += 1
        return VendorResult(payload={"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": CHART}, duration_ms=1, attempts=1)


class MemoryDB:
    provider_name = "fixture"

    def __init__(self):
        self.rows = {}

    def query(self, sql, params=None):
        key = tuple(params)
        if "COUNT" in sql:
            return [(int(key in self.rows),)]
        return [(self.rows[key],)] if key in self.rows else []

    def tx(self, statements):
        statement = statements[0]
        key = tuple(statement.params[:4])
        inserted = key not in self.rows
        self.rows.setdefault(key, statement.params[4])
        return [[(1,)]] if inserted else [[]]


def install(monkeypatch, *, db=object()):
    client = Client()
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: client)
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: db)
    return client


def test_dry_run_with_or_without_upsert_never_constructs_db(monkeypatch):
    client = Client()
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: client)
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB must not be constructed"))
    for upsert in (False, True):
        result = resolve_bodygraph("operator", source="vendor", upsert=upsert, dry_run=True, env=env(), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
        assert result.status == "ok" and result.payload["ingest"]["rows_written"] == 0


def test_missing_upsert_refuses_before_vendor_and_db(monkeypatch):
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    result = resolve_bodygraph("operator", source="vendor", upsert=False, dry_run=False, env=env(), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"


@pytest.mark.parametrize("app_env", ["prod", "production", "live"])
def test_production_like_refuses_before_vendor_and_db(monkeypatch, app_env):
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(APP_ENV=app_env), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"


def test_process_production_environment_cannot_be_overridden_for_database_write(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(APP_ENV="test"), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"


@pytest.mark.parametrize("retired_key", RETIRED_DB_TRANSPORT_KEYS)
@pytest.mark.parametrize("retired_value", ["", None])
def test_scoped_retired_key_refuses_before_mapped_cache_db_and_vendor_io(
    monkeypatch, retired_key, retired_value
):
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(
        "engine.db.adapter.PsycopgProvider",
        lambda _dsn: pytest.fail("direct provider constructed"),
    )
    monkeypatch.setattr(
        "engine.bodygraph.resolver.HdApiClient.from_env",
        lambda **kwargs: pytest.fail("vendor constructed"),
    )

    result = resolve_bodygraph(
        "operator",
        source="vendor",
        upsert=True,
        dry_run=False,
        env=env(
            DATABASE_URL="postgresql://must-not-read",
            **{retired_key: retired_value},
        ),
        birthdate="2000-01-01",
        birthtime="00:00",
        location="Fixture",
    )

    assert result.payload["error"] == {
        "code": "DB_WRITER_UNAVAILABLE",
        "message": "mapped-cache database target unavailable",
        "details": {"code": "retired_bridge_configuration"},
    }


def test_closed_rails_refuse_before_all_io(monkeypatch):
    monkeypatch.setattr("engine.bodygraph.resolver._classify_env_route_policy", lambda *_: pytest.fail("route classified"))
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(SAFE_MODE="1", ALLOW_NETWORK="0"))
    assert result.payload["error"]["code"] == "PROVIDER_REFUSED"


def test_unavailable_db_does_not_consume_vendor(monkeypatch):
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: (_ for _ in ()).throw(PrimaryUnavailable(code="missing_database_url")))
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.payload["error"]["code"] == "DB_WRITER_UNAVAILABLE"


def test_success_uses_mapped_cache_once_and_snapshot_none(monkeypatch):
    db = object(); client = install(monkeypatch, db=db); captured = {}
    def persist(actual_db, cache):
        captured.update({"db": actual_db, "cache": cache})
        return MappedCacheResult("fixture", "b" * 64, 0, 1, 1, True, False)
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", persist)
    calls = []
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: calls.append(kwargs) or db)
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.status == "ok" and client.calls == 1
    assert len(calls) == 1
    assert calls[0]["environ"]["APP_ENV"] == "test"
    assert captured["db"] is db and captured["cache"]["payload_posture"] == "adapter_mapped_no_raw_vendor_payload"
    assert result.payload["ingest"]["canonical_sha256"] == "b" * 64


@pytest.mark.parametrize(
    ("first_user_id", "second_user_id"),
    [
        ("3FA85F64-5717-4562-B3FC-2C963F66AFAA", "3fa85f64-5717-4562-b3fc-2c963f66afaa"),
        ("3fa85f64-5717-4562-b3fc-2c963f66afaa", "3FA85F64-5717-4562-B3FC-2C963F66AFAA"),
        ("{3fa85f64-5717-4562-b3fc-2c963f66afaa}", "3fa85f64-5717-4562-b3fc-2c963f66afaa"),
        ("3fa85f6457174562b3fc2c963f66afaa", "3fa85f64-5717-4562-b3fc-2c963f66afaa"),
    ],
)
def test_equivalent_uuid_spellings_share_one_canonical_mapped_cache_identity(
    monkeypatch, first_user_id, second_user_id
):
    canonical_user_id = "3fa85f64-5717-4562-b3fc-2c963f66afaa"
    db = MemoryDB()
    install(monkeypatch, db=db)
    kwargs = {
        "source": "vendor",
        "upsert": True,
        "dry_run": False,
        "env": env(),
        "birthdate": "2000-01-01",
        "birthtime": "00:00",
        "location": "Fixture",
    }

    first = resolve_bodygraph(first_user_id, **kwargs)
    second = resolve_bodygraph(second_user_id, **kwargs)

    assert first.status == second.status == "ok"
    assert first.payload["cache"]["user_id"] == second.payload["cache"]["user_id"] == canonical_user_id
    assert first.payload["ingest"]["rows_written"] == 1
    assert second.payload["ingest"]["rows_written"] == 0
    assert first.payload["ingest"]["canonical_sha256"] == second.payload["ingest"]["canonical_sha256"]
    assert len(db.rows) == 1
    stored = json.loads(next(iter(db.rows.values())))
    assert stored["person_uid"] == f"person-{canonical_user_id}"


def test_non_uuid_alias_preserves_person_uid_while_using_database_uuid(monkeypatch):
    install(monkeypatch)
    result = resolve_bodygraph(
        "operator",
        source="vendor",
        upsert=False,
        dry_run=True,
        env=env(),
        birthdate="2000-01-01",
        birthtime="00:00",
        location="Fixture",
    )
    assert result.status == "ok"
    assert result.payload["resolved"]["person_uid"] == "person-operator"
    assert result.payload["cache"]["user_id"] == str(uuid.uuid5(uuid.NAMESPACE_URL, "operator"))


def test_adapter_and_cache_failures_write_nothing_or_return_typed_error(monkeypatch):
    db = object(); install(monkeypatch, db=db)
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *_: (_ for _ in ()).throw(MappedCacheError("DB_QUERY_FAILED", "parity failed")))
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=False, env=env(), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.payload["error"]["code"] == "DB_QUERY_FAILED"


def test_explicit_legacy_fallback_remains_legacy(monkeypatch):
    seen = []
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *args, **kwargs: seen.append(kwargs) or type("O", (), {"vendor":"hdapi","vendor_version":1,"input_fingerprint":"x","idempotency_key":"i","rows_written":0,"db_rows_after":0,"duration_ms":0,"payload_sha256":"s","db_emitted_sha256":"s","parity_match":True})())
    result = resolve_bodygraph("operator", source="vendor", upsert=True, dry_run=True, env=env(HD_API_BASE_URL="https://vendor.test/v1"), birthdate="2000-01-01", birthtime="00:00", location="Fixture")
    assert result.status == "ok" and seen
    assert result.payload["resolver"]["route_policy"]["classification"] == "explicit_legacy_fallback"


@pytest.mark.parametrize("retired_key", RETIRED_DB_TRANSPORT_KEYS)
@pytest.mark.parametrize("retired_value", ["", None])
def test_explicit_legacy_fallback_preserves_scoped_retired_key_refusal(
    monkeypatch, retired_key, retired_value
):
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(
        "engine.db.adapter.PsycopgProvider",
        lambda _dsn: pytest.fail("direct provider constructed"),
    )
    monkeypatch.setattr(
        "engine.bodygraph.ingest.HdApiClient.from_env",
        lambda **kwargs: pytest.fail("vendor constructed"),
    )

    result = resolve_bodygraph(
        "operator",
        source="vendor",
        upsert=True,
        dry_run=False,
        env=env(
            HD_API_BASE_URL="https://vendor.test/v1",
            DATABASE_URL="postgresql://must-not-read",
            **{retired_key: retired_value},
        ),
        birthdate="2000-01-01",
        birthtime="00:00",
        location="Fixture",
    )

    assert result.payload["error"] == {
        "code": "DB_WRITER_UNAVAILABLE",
        "message": "database target unavailable",
        "details": {"code": "retired_bridge_configuration"},
    }
