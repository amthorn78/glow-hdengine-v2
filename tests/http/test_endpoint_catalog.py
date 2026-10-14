import copy
import json
from pathlib import Path

import pytest

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
    assert row["blueprint_module"] == create_app.__module__
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


# --- HDE-CRD-0002 S15 (IF-6; ID-1): the catalog covers every served pair ----------
#
# Every (method, path) a factory serves as endpoint behavior has exactly one
# catalog row.  The pairs below are excluded, each for one reason:
#   (a) governed refusal of a catalogued record (PF05 §5.4 "Production mount";
#       PF12 §8.8: the production route's other methods are part of its record);
#   (b) alias spelling of a canonical record, carried by its ``aliases`` (PF05 §5.6);
#   (c) a method Flask adds automatically (HEAD for a GET view; OPTIONS) whose
#       behavior neither PF05 §5.6 nor the route's own view defines.
_GOVERNED_REFUSAL = "a"
_ALIAS = "b"
_FRAMEWORK_IMPLICIT = "c"
_EXCLUDED_PAIRS = {
    **{("/api/reader", m): _GOVERNED_REFUSAL for m in ("DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "PUT")},
    ("/reader", "POST"): _GOVERNED_REFUSAL,
    ("/api/aux/narrative", "GET"): _ALIAS,
    ("/api/aux/narrative", "HEAD"): _FRAMEWORK_IMPLICIT,
    ("/api/aux/narrative", "OPTIONS"): _FRAMEWORK_IMPLICIT,
    ("/reader", "OPTIONS"): _FRAMEWORK_IMPLICIT,
    ("/internal/version", "OPTIONS"): _FRAMEWORK_IMPLICIT,
    **{
        (path, m): _FRAMEWORK_IMPLICIT
        for path in (
            "/aux/narrative",
            "/dev/reader/conjunction",
            "/dev/sampler/conjunction",
            "/dev/writer/conjunction",
            "/internal/healthz",
            "/internal/readyz",
            "/ops/db/unavailable",
            "/ops/probe/env",
            "/ops/rails/refusal",
        )
        for m in ("HEAD", "OPTIONS")
    },
}


def _served_pairs():
    served = set()
    for factory in _factories().values():
        for rule in factory().url_map.iter_rules():
            if rule.endpoint != "static":
                served.update((rule.rule, method) for method in rule.methods)
    return served


def test_every_served_pair_has_one_catalog_row_or_a_reasoned_exclusion(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    served = _served_pairs()
    catalogued = {(e["path"], e["method"]) for e in _catalog()["endpoints"]}
    excluded = set(_EXCLUDED_PAIRS)
    assert not catalogued & excluded
    assert sorted(served - catalogued - excluded) == []  # an uncatalogued route fails
    assert sorted(excluded - served) == []  # a stale exclusion fails
    assert sorted(catalogued - served) == []  # no row for an unmounted route (PF12 §8.8)
    aux = next(e for e in _catalog()["endpoints"] if e["path"] == "/aux/narrative")
    assert [p for (p, m), why in _EXCLUDED_PAIRS.items() if why == _ALIAS and m == aux["method"]] == aux["aliases"]


def test_aux_record_follows_the_pf05_projection():
    rows = [e for e in _catalog()["endpoints"] if e["path"] == "/aux/narrative"]
    assert rows == [
        {
            "a7_eligible": False,
            "aliases": ["/api/aux/narrative"],
            "blueprint_module": create_app.__module__,
            "classification": "public_aux",
            "description": rows[0]["description"],
            "env_gate": "not_applicable_public",
            "internal": False,
            "method": "GET",
            "path": "/aux/narrative",
            "rails_profile": "public-read-only; vendor-network-disabled",
        }
    ]
    assert [e for e in _catalog()["endpoints"] if "aliases" in e] == rows


def test_validator_rejects_aliases_off_the_aux_record_and_alias_collisions():
    cat = catalog_obj()
    bad = copy.deepcopy(cat)
    next(e for e in bad["endpoints"] if e["path"] == "/internal/version")["aliases"] = ["/x"]
    with pytest.raises(ValueError):
        validate_catalog(bad)
    bad = copy.deepcopy(cat)
    row = next(e for e in bad["endpoints"] if e["path"] == "/ops/rails/refusal" and e["method"] == "GET")
    row["classification"], row["aliases"] = "public_aux", ["/x"]  # a second public_aux record cannot carry aliases
    with pytest.raises(ValueError):
        validate_catalog(bad)
    bad = copy.deepcopy(cat)
    next(e for e in bad["endpoints"] if e["path"] == "/aux/narrative")["aliases"] = ["/reader"]
    with pytest.raises(ValueError):
        validate_catalog(bad)
    bad = copy.deepcopy(cat)
    next(e for e in bad["endpoints"] if e["path"] == "/ops/probe/env")["classification"] = "public_ops"
    with pytest.raises(ValueError):
        validate_catalog(bad)


# --- HDE-CRD-0002 S02 (IF-11): unknown paths answer the governed envelope ----------

_NOT_FOUND_BODY = b'{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}\n'


def _factories():
    # Bind each factory function directly: another test may reload the
    # ``adapter`` package, after which its submodule attributes are unset.
    from adapter.factory import create_app as production_app
    from adapter.wsgi import create_app as wsgi_app

    return {
        "factory": production_app,
        "http_reader": create_app,
        "wsgi": wsgi_app,
    }


def _assert_governed(resp, status, *, head=False):
    assert resp.status_code == status
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert resp.data == (b"" if head else _NOT_FOUND_BODY)


@pytest.mark.parametrize("factory_name", ["factory", "http_reader", "wsgi"])
@pytest.mark.parametrize("path", ["/nope", "/reader/x", "/api/reader/x", "/internal/nope", "/aux/narrative/x"])
@pytest.mark.parametrize("method", ["GET", "HEAD", "POST", "OPTIONS", "PUT", "DELETE"])
@pytest.mark.parametrize("app_env", ["dev", "prod"])
def test_unknown_paths_return_the_governed_not_found_envelope(monkeypatch, factory_name, path, method, app_env):
    monkeypatch.setenv("APP_ENV", app_env)
    resp = _factories()[factory_name]().test_client().open(path, method=method)
    _assert_governed(resp, 404, head=method == "HEAD")


@pytest.mark.parametrize("factory_name", ["factory", "http_reader"])
@pytest.mark.parametrize(
    ("method", "path", "allow"),
    [
        ("PUT", "/reader", "GET, HEAD, OPTIONS, POST"),
        ("DELETE", "/aux/narrative", "GET, HEAD, OPTIONS"),
        ("PUT", "/internal/version", "GET, HEAD, OPTIONS"),
        ("GET", "/ops/writer/diagnostic", "HEAD, OPTIONS, POST"),
    ],
)
def test_unrouted_methods_return_the_governed_405_with_allow(monkeypatch, factory_name, method, path, allow):
    monkeypatch.setenv("APP_ENV", "dev")
    resp = _factories()[factory_name]().test_client().open(path, method=method)
    _assert_governed(resp, 405)
    assert resp.headers.get("Allow") == allow


@pytest.mark.parametrize("factory_name", ["factory", "http_reader"])
def test_compat_and_production_reader_shaping_is_unchanged(monkeypatch, factory_name):
    monkeypatch.setenv("APP_ENV", "dev")
    client = _factories()[factory_name]().test_client()
    descendant = client.get("/api/compat/v1/zzz")
    assert descendant.status_code == 404 and descendant.data == _NOT_FOUND_BODY
    put = client.put("/api/compat/v1")
    assert put.status_code == 405 and put.data == _NOT_FOUND_BODY
    # PF05 §5.5: the production factory keeps Flask's Allow on a converted compat 405.
    if factory_name == "factory":
        assert set(put.headers.get("Allow", "").split(", ")) == {"GET", "HEAD", "OPTIONS", "POST"}
    head = client.head("/api/compat/v1")
    assert head.status_code == 405 and head.headers.get("Allow") == "POST, OPTIONS"
    for method in ("GET", "HEAD", "OPTIONS", "PUT", "PATCH", "DELETE", "TRACE"):
        refused = client.open("/api/reader", method=method)
        assert refused.status_code == 405
        assert refused.headers.get("Allow") == "POST"
    unprefixed = client.post("/reader")
    assert unprefixed.status_code == 405 and unprefixed.headers.get("Allow") == "GET, HEAD"
