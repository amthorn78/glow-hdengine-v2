import json
from pathlib import Path
from adapter.http_reader import create_app
from tools.evidence.generate_a7_transport_proofs import validate_catalog

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
