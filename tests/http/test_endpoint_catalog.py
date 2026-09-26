import json
from pathlib import Path
from adapter.http_reader import create_app
from tools.evidence.generate_a7_transport_proofs import catalog_obj, validate_catalog

def _catalog():
    return json.loads(Path("docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))

def test_endpoint_catalog_schema_is_strict_and_valid():
    cat = _catalog()
    target = validate_catalog(cat)
    assert target["method"] == "GET"
    assert target["path"] == "/reader"
    assert target["classification"] == "dev_harness"
    assert target["internal"] is True

def test_all_endpoint_methods_are_strings_and_internal_is_boolean():
    for entry in _catalog()["endpoints"]:
        assert isinstance(entry["method"], str)
        assert entry["method"] == entry["method"].upper()
        assert isinstance(entry["internal"], bool)

def test_internal_version_remains_a7_ineligible_get_and_head():
    entries = [e for e in _catalog()["endpoints"] if e["path"] == "/internal/version"]
    assert {e["method"] for e in entries} == {"GET", "HEAD"}
    assert all(e["classification"] == "internal_identity" for e in entries)
    assert all(e["internal"] is True for e in entries)
    assert all(e["a7_eligible"] is False for e in entries)

def test_dev_writer_route_id_is_cataloged():
    entry = next(e for e in _catalog()["endpoints"] if e["path"] == "/dev/writer/conjunction")
    assert entry["route_id"] == "dev.writer.conjunction.v1"

def test_internal_dev_sampler_cataloged_as_internal_non_a7_dev_harness(monkeypatch):
    cat = _catalog()
    entries = [e for e in cat["endpoints"] if e["path"] == "/internal/dev/sampler"]
    assert len(entries) == 1
    entry = entries[0]
    assert entry["method"] == "POST"
    assert entry["classification"] == "dev_harness"
    assert entry["internal"] is True
    assert entry["a7_eligible"] is False
    assert entry["env_gate"] == "APP_ENV in {dev,test,local}"
    assert not any(e["path"] == "/internal/dev/sampler" and e["method"] == "GET" for e in cat["endpoints"])
    assert cat["success_endpoints"] == [{"method": "GET", "path": "/reader"}]
    assert validate_catalog(cat)["path"] == "/reader"
    monkeypatch.setenv("APP_ENV", "dev")
    app = create_app()
    app.config.update(TESTING=True)
    assert app.test_client().get("/internal/dev/sampler").status_code == 405


def _production_rows(cat):
    return [e for e in cat["endpoints"] if e["path"] == "/api/reader"]


def _assert_production_row(cat):
    rows = _production_rows(cat)
    assert len(rows) == 1
    row = rows[0]
    assert row["method"] == "POST"
    assert row["classification"] == "public_reader"
    assert row["internal"] is False
    assert row["a7_eligible"] is False
    assert row["env_gate"] == "not_applicable_public"
    assert row["blueprint_module"] == "adapter.http_reader"
    assert "v=2" in row["description"] and "v=1" in row["description"]
    assert cat["success_endpoints"] == [{"method": "GET", "path": "/reader"}]
    target = validate_catalog(cat)
    assert target["method"] == "GET" and target["path"] == "/reader"


def test_authored_catalog_carries_the_production_reader_row():
    _assert_production_row(catalog_obj())


def test_tracked_catalog_carries_the_production_reader_row():
    cat = _catalog()
    _assert_production_row(cat)
    mirror = json.loads(Path("artifacts/audit/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))
    assert mirror == cat


def test_production_reader_route_refuses_get_with_the_governed_405(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    app = create_app()
    app.config.update(TESTING=True)
    resp = app.test_client().get("/api/reader?v=2")
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "POST"
    assert json.loads(resp.data)["code"] == "ERR_NOT_FOUND"
