import json

import pytest

from adapter.http_reader import create_app
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.vendor_client import VendorRequest, VendorResult
from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS
from tests.support.pr04_fixtures import GATES_A, GATES_B, build_bundle, build_pack, inject_seams

VENDOR_CHART = json.loads(open("tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json", encoding="utf-8").read())["payload"]
QUERY = {
    "a_user_id": "left",
    "b_user_id": "right",
    "a_birthdate": "1990-01-01",
    "a_birthtime": "08:30",
    "a_location": "Amsterdam",
    "b_birthdate": "1991-02-02",
    "b_birthtime": "09:45",
    "b_location": "Berlin",
}


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-devconj-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-devconj-pack"))


@pytest.fixture(autouse=True)
def _isolate_external_resolution(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("legacy ingest attempted"))


def _client(monkeypatch, app_env: str):
    monkeypatch.setenv("APP_ENV", app_env)
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _install_fake_transport(monkeypatch):
    """Guarded test-only acquisition: a fake transport feeding the real v2 adapter path."""
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.setenv("HD_API_KEY", "set")
    monkeypatch.setenv("GEO_API_KEY", "set")
    fetches: list[str] = []

    class FakeTransport:
        def build_contract_route_request(self, **kwargs):
            body = json.dumps({k: kwargs[k] for k in ("birthdate", "birthtime", "location")}, sort_keys=True).encode()
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=body, input_fingerprint="d" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request):
            fetches.append(request.body_bytes.decode())
            data = dict(VENDOR_CHART)
            data["gates"] = GATES_A if "Amsterdam" in request.body_bytes.decode() else GATES_B
            return VendorResult(payload={"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": data}, duration_ms=1, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeTransport())
    return fetches


def test_dev_conjunction_endpoints_gate_in_prod(monkeypatch):
    client = _client(monkeypatch, "prod")
    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string={"a_user_id": "left", "b_user_id": "right"})
        assert resp.status_code == 403
        assert json.loads(resp.data) == {"schema": "v1", "ok": False, "code": "ERR_WRITER_FORBIDDEN", "error": "insufficient scope"}


def test_dev_conjunction_endpoints_closed_rails_refusal(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed under closed rails"))
    client = _client(monkeypatch, "dev")
    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string={"a_user_id": "left", "b_user_id": "right"})
        assert resp.status_code == 503
        payload = json.loads(resp.data)
        assert payload["code"] == "ERR_WRITER_RAILS_CLOSED"
        assert payload["details"]["rails"] == {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
        assert payload["details"]["provider_code"] == "PROVIDER_REFUSED"
        if route == "/dev/writer/conjunction":
            assert payload["type"] == "dev.writer.conjunction.error.v1"


@pytest.mark.parametrize("app_env", ["dev", "test", "local"])
def test_dev_conjunction_endpoints_open_rails_success(monkeypatch, app_env):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    fetches = _install_fake_transport(monkeypatch)
    client = _client(monkeypatch, app_env)
    expected = {resolve_db_user_id("left"), resolve_db_user_id("right")}
    for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):
        resp = client.get(route, query_string=QUERY)
        assert resp.status_code == 200, resp.data
        payload = json.loads(resp.data)
        conjunction_payload = payload.get("result", payload)
        assert "conjunction" in conjunction_payload
        assert {conjunction_payload["conjunction"]["left"]["person_uid"], conjunction_payload["conjunction"]["right"]["person_uid"]} == expected
        assert conjunction_payload["conjunction"]["compat"]["schema"] == "magic10_compat_result.v1"
        assert "meta" not in conjunction_payload["conjunction"]["compat"]
    assert len(fetches) == 6


def test_dev_conjunction_open_rails_without_birth_data_cannot_acquire(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    _install_fake_transport(monkeypatch)
    client = _client(monkeypatch, "dev")
    resp = client.get("/dev/reader/conjunction", query_string={"a_user_id": "left", "b_user_id": "right"})
    assert resp.status_code == 503
    payload = json.loads(resp.data)
    assert payload["code"] == "ERR_WRITER_RAILS_CLOSED"
    assert payload["details"]["provider_code"] == "PROVIDER_INPUT_MISSING"


def test_dev_writer_conjunction_is_idempotent_bytes(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    _install_fake_transport(monkeypatch)
    client = _client(monkeypatch, "dev")
    resp_one = client.get("/dev/writer/conjunction", query_string=QUERY)
    resp_two = client.get("/dev/writer/conjunction", query_string=QUERY)
    assert resp_one.status_code == 200, resp_one.data
    assert resp_two.status_code == 200
    assert resp_one.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp_one.headers
    assert resp_one.data == resp_two.data
    payload_one = json.loads(resp_one.data)
    payload_two = json.loads(resp_two.data)
    assert payload_one["schema"] == "v1"
    assert payload_one["type"] == "dev.writer.conjunction.success.v1"
    assert payload_one["writer"] == payload_two["writer"]
    assert payload_one["writer"]["writer_route_id"] == "dev.writer.conjunction.v1"
    assert payload_one["writer"]["idempotence_hash"]


def test_dev_writer_conjunction_invalid_input_uses_typed_error(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    client = _client(monkeypatch, "dev")
    resp = client.get("/dev/writer/conjunction", query_string={"a_user_id": "left"})
    assert resp.status_code == 422
    assert resp.headers["Cache-Control"] == "no-store"
    assert "ETag" not in resp.headers
    payload = json.loads(resp.data)
    assert payload["schema"] == "v1" and payload["ok"] is False
    assert payload["code"] == "ERR_WRITER_INVALID_INPUT"
    assert payload["type"] == "dev.writer.conjunction.error.v1"


def test_dev_writer_conjunction_retired_db_config_uses_typed_error(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("DATABASE_URL", "postgresql://must-not-be-used")
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("DB_BRIDGE_URL", "")
    provider_calls = []
    monkeypatch.setattr("engine.db.adapter.PsycopgProvider", lambda _dsn: provider_calls.append("provider") or pytest.fail("provider attempted"))
    client = _client(monkeypatch, "dev")
    response = client.get("/dev/writer/conjunction", query_string={"a_user_id": "left", "b_user_id": "right"})
    assert response.status_code == 503
    assert response.headers["Cache-Control"] == "no-store"
    assert "ETag" not in response.headers
    assert json.loads(response.data) == {
        "schema": "v1",
        "ok": False,
        "code": "ERR_WRITER_RAILS_CLOSED",
        "error": "rails are closed",
        "details": {"adapter_code": "retired_bridge_configuration", "retired_keys": ["DB_BRIDGE_URL"]},
        "type": "dev.writer.conjunction.error.v1",
    }
    assert provider_calls == []
