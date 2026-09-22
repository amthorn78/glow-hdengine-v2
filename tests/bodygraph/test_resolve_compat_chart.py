"""HDE-EPIC040-PR04: the complete chart-bearing resolution seam (input classes 1–3)."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path

import pytest

from engine.bodygraph import resolver
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.mapped_cache import MappedBodyGraphRow, MappedCacheError, read_current_mapped_bodygraph
from engine.bodygraph.resolver import ResolvedCompatChart, _derived_birth_uid, resolve_compat_chart
from engine.bodygraph.vendor_client import VendorError, VendorRequest, VendorResult
from engine.compat.error_tokens import CompatBoundaryError

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures/bodygraph/source_invariance"
UUID_A = "00000000-0000-4000-8000-000000000038"
UUID_B = "00000000-0000-4000-8000-000000000039"
UUID_MIXED = "3fa85f64-5717-4562-b3fc-2c963f66afaa"
CLOSED = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
OPEN = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v2", "HD_API_KEY": "set", "GEO_API_KEY": "set"}
BIRTH = {"birthdate": "1990-01-01", "birthtime": "08:30", "location": "Amsterdam"}


def _chart(uid: str = UUID_A) -> dict:
    payload = json.loads((FIXTURES / "db_cached_payload.v1.json").read_text(encoding="utf-8"))["payload"]
    payload["person_uid"] = uid
    payload["person"] = {"person_uid": uid}
    return payload


def _vendor_chart_result() -> dict:
    return json.loads((FIXTURES / "vendor_chart_result.v1.json").read_text(encoding="utf-8"))["payload"]


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)


# --- class 1: already-resolved charts -------------------------------------------------

def test_class1_uuid_label_binds_identity_without_lookup_or_vendor(monkeypatch):
    monkeypatch.setattr(resolver, "_acquire_dry_run", lambda *a, **k: pytest.fail("acquisition attempted"))
    resolved = resolve_compat_chart(_chart(), source_policy="local", env=CLOSED, local_lookup=lambda *_: pytest.fail("lookup attempted"))
    assert isinstance(resolved, ResolvedCompatChart)
    assert resolved.canonical_person_id == UUID_A
    assert resolved.mapped_chart["person_uid"] == UUID_A and resolved.mapped_chart["person"] == {"person_uid": UUID_A}
    assert resolved.mapped_chart["bodygraph"]["gates"] == ["10", "20", "34"]
    assert resolved.source == "resolved" and resolved.user_id is None


def test_class1_canonicalizes_uuid_spelling_and_binds_alias_label():
    upper = _chart(UUID_MIXED.upper())
    assert resolve_compat_chart(upper, source_policy="local", env=CLOSED).canonical_person_id == UUID_MIXED
    aliased = _chart("person-operator")
    aliased["user_id"] = "operator"
    resolved = resolve_compat_chart(aliased, source_policy="local", env=CLOSED)
    assert resolved.canonical_person_id == resolve_db_user_id("operator")
    assert resolved.user_id == resolved.canonical_person_id


def test_class1_birth_tuple_beside_chart_supplies_identity_through_the_birth_seed():
    chart = _chart("person-birth-fixture")
    chart.update(BIRTH)
    seed = _derived_birth_uid(BIRTH)
    chart["person_uid"] = f"person-{seed}"
    chart["person"] = {"person_uid": f"person-{seed}"}
    resolved = resolve_compat_chart(chart, source_policy="local", env=CLOSED)
    assert resolved.canonical_person_id == resolve_db_user_id(seed)


@pytest.mark.parametrize(
    ("mutate", "reason"),
    [
        (lambda c: c.update(user_id=UUID_B), "identity_conflict"),
        (lambda c: c.update(user_id=UUID_B, canonical_person_id=UUID_A), "identity_conflict"),
        (lambda c: c.update(person_uid="person-nobody", person={"person_uid": "person-nobody"}), "identity_unresolved"),
        (lambda c: c.update(person={"person_uid": UUID_B}), "identity_conflict"),
        (lambda c: c["bodygraph"].update(gates=[]), "gates_missing"),
        (lambda c: c["bodygraph"].pop("gates"), "gates_missing"),
        (lambda c: c["bodygraph"].update(gates=["10", "10"]), "gates_invalid"),
        (lambda c: c["bodygraph"].update(gates=[10, "10"]), "gates_invalid"),
        (lambda c: c["bodygraph"].update(gates=[True]), "gates_invalid"),
        (lambda c: c["bodygraph"].update(gates=["010"]), "gates_invalid"),
        (lambda c: c["bodygraph"].update(gates=[65]), "gates_invalid"),
        (lambda c: c["bodygraph"].pop("profile"), "chart_incomplete"),
        (lambda c: c["bodygraph"].update(headers={}), "chart_invalid"),
        (lambda c: c.update(canonical_person_id="not-a-uuid"), "identity_invalid"),
    ],
)
def test_class1_refusals_carry_stable_reasons_and_tokens(mutate, reason):
    chart = _chart()
    mutate(chart)
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart(chart, source_policy="local", env=CLOSED)
    assert raised.value.reason == reason
    assert raised.value.token
    assert raised.value.reader_token
    assert raised.value.reader_status in {422, 503}


def test_already_resolved_value_passes_through():
    resolved = resolve_compat_chart(_chart(), source_policy="local", env=CLOSED)
    assert resolve_compat_chart(resolved, source_policy="vendor", env=CLOSED) is resolved


# --- class 2: stored-user lookup ------------------------------------------------------

def test_class2_lookup_uses_canonical_key_and_binds_row_identity():
    seen: list[str] = []

    def lookup(key: str):
        seen.append(key)
        return MappedBodyGraphRow(user_id=key, vendor="hdapi", vendor_version=2, input_fingerprint="a" * 64, payload=_chart(f"person-{key}"))

    resolved = resolve_compat_chart({"user_id": UUID_MIXED.upper()}, source_policy="local", env=CLOSED, local_lookup=lookup)
    assert seen == [UUID_MIXED]
    assert resolved.canonical_person_id == UUID_MIXED and resolved.source == "db"
    assert (resolved.vendor, resolved.vendor_version, resolved.input_fingerprint) == ("hdapi", 2, "a" * 64)
    resolved_alias = resolve_compat_chart("operator", source_policy="local", env=CLOSED, local_lookup=lookup)
    assert resolved_alias.canonical_person_id == resolve_db_user_id("operator")
    bare = resolve_compat_chart({"person_uid": UUID_A}, source_policy="local", env=CLOSED, local_lookup=lookup)
    assert bare.canonical_person_id == UUID_A


def test_class2_miss_is_person_unresolved_under_local_policy_and_never_acquires(monkeypatch):
    monkeypatch.setattr(resolver, "_acquire_dry_run", lambda *a, **k: pytest.fail("acquisition attempted"))
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart({"user_id": "missing"}, source_policy="local", env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.reason == "person_unresolved"
    assert (raised.value.reader_token, raised.value.reader_status) == ("ERR_M10_PERSON_UNRESOLVED", 404)


def test_class2_invalid_hit_refuses_without_vendor_fallback(monkeypatch):
    monkeypatch.setattr(resolver, "_acquire_dry_run", lambda *a, **k: pytest.fail("acquisition attempted"))
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart({"user_id": UUID_A}, source_policy="vendor", env=OPEN, local_lookup=lambda *_: {"person_uid": UUID_A})
    assert raised.value.reason == "chart_incomplete"
    wrong_row = MappedBodyGraphRow(user_id=UUID_B, vendor="hdapi", vendor_version=2, input_fingerprint=None, payload=_chart(UUID_B))
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart({"user_id": UUID_A}, source_policy="vendor", env=OPEN, local_lookup=lambda *_: wrong_row)
    assert raised.value.reason == "provenance_mismatch"
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart({"user_id": UUID_A}, source_policy="local", env=CLOSED, local_lookup=lambda *_: "uid-only")
    assert raised.value.reason == "chart_invalid"


def test_class2_lookup_exceptions_propagate_unchanged():
    class Boom(RuntimeError):
        pass

    def lookup(_key):
        raise Boom("db down")

    with pytest.raises(Boom):
        resolve_compat_chart({"user_id": UUID_A}, source_policy="vendor", env=OPEN, local_lookup=lookup)


def test_class2_miss_under_vendor_policy_refuses_on_closed_rails_before_any_vendor_io(monkeypatch):
    monkeypatch.setattr(resolver, "_classify_env_route_policy", lambda *_: pytest.fail("route classified"))
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    with pytest.raises(VendorError) as raised:
        resolve_compat_chart({"user_id": "missing"}, source_policy="vendor", env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"
    with pytest.raises(VendorError) as raised:
        resolve_compat_chart({"user_id": "missing"}, source_policy="vendor", env={"SAFE_MODE": "0", "ALLOW_NETWORK": "0"}, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_NETWORK_BLOCKED"
    with pytest.raises(VendorError) as raised:
        resolve_compat_chart({"user_id": "missing"}, source_policy="vendor", env=None, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"


# --- class 3: birth-only / no-user -----------------------------------------------------

def test_class3_local_first_hit_succeeds_under_closed_rails_with_no_user_row(monkeypatch):
    monkeypatch.setattr(resolver, "_acquire_dry_run", lambda *a, **k: pytest.fail("acquisition attempted"))
    seed = _derived_birth_uid(BIRTH)
    canonical = resolve_db_user_id(seed)
    store = {canonical: _chart(f"person-{seed}")}
    seen: list[str] = []

    def lookup(key: str):
        seen.append(key)
        return store.get(key)

    resolved = resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=CLOSED, local_lookup=lookup)
    assert seen == [canonical]
    assert resolved.canonical_person_id == canonical and resolved.source == "local"
    assert "person_uid" not in BIRTH and "user_id" not in BIRTH


def test_class3_closed_rails_miss_refuses_without_evaluation(monkeypatch):
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor constructed"))
    with pytest.raises(VendorError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"


def test_class3_birth_only_file_surface_is_legacy_unsupported(monkeypatch):
    monkeypatch.setattr(resolver, "_acquire_dry_run", lambda *a, **k: pytest.fail("acquisition attempted"))
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="local", env=CLOSED)
    assert raised.value.reason == "legacy_input"
    assert raised.value.token == "ERR_M10_LEGACY_INPUT_UNSUPPORTED"
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart({"mechanics": {"type": "Generator"}}, source_policy="local", env=CLOSED)
    assert raised.value.reason == "legacy_input"
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="local", env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.reason == "person_unresolved"


def test_class3_permitted_acquisition_uses_the_real_v2_adapter_path_read_only(monkeypatch):
    calls: dict[str, object] = {"fetch": 0, "persist": 0, "db": 0, "ingest": 0, "env_during_fetch": None}

    class FakeClient:
        def build_contract_route_request(self, **kwargs):
            assert kwargs["path"] == "charts"
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=b"{}\n", input_fingerprint="b" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request):
            calls["fetch"] += 1
            calls["env_during_fetch"] = dict(os.environ)
            return VendorResult(payload={"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": _vendor_chart_result()}, duration_ms=1, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: calls.__setitem__("db", calls["db"] + 1) or pytest.fail("DB constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: calls.__setitem__("persist", calls["persist"] + 1) or pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: calls.__setitem__("ingest", calls["ingest"] + 1) or pytest.fail("legacy ingest attempted"))
    before = dict(os.environ)

    seed = _derived_birth_uid(BIRTH)
    canonical = resolve_db_user_id(seed)
    resolved = resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=OPEN, local_lookup=lambda *_: None)

    assert calls["fetch"] == 1 and calls["persist"] == 0 and calls["db"] == 0 and calls["ingest"] == 0
    assert resolved.canonical_person_id == canonical
    assert resolved.source == "vendor_v2_dry_run"
    assert resolved.user_id == canonical and resolved.vendor == "hdapi" and resolved.vendor_version == 2
    assert resolved.input_fingerprint == "b" * 64
    assert resolved.mapped_chart["person_uid"] == canonical
    assert resolved.mapped_chart["bodygraph"]["gates"] == ["10", "20", "34"]
    # The resolver never opened rails for itself: the process environment is untouched.
    assert dict(os.environ) == before
    assert calls["env_during_fetch"]["SAFE_MODE"] == "1" and calls["env_during_fetch"]["ALLOW_NETWORK"] == "0"


def test_class3_acquisition_seam_injection_is_verified_and_env_restored_on_failure(monkeypatch):
    seed = _derived_birth_uid(BIRTH)
    canonical = resolve_db_user_id(seed)
    captured = {}

    def acquisition(**kwargs):
        captured.update(kwargs)
        return _chart(f"person-{seed}")

    resolved = resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=OPEN, local_lookup=lambda *_: None, acquisition=acquisition)
    assert captured["canonical_person_id"] == canonical and captured["birth"] == (BIRTH["birthdate"], BIRTH["birthtime"], BIRTH["location"])
    assert resolved.canonical_person_id == canonical and resolved.source == "local"

    def wrong(**kwargs):
        return ResolvedCompatChart(UUID_B, _chart(UUID_B), "resolved", None, None, None, None)

    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=OPEN, local_lookup=lambda *_: None, acquisition=wrong)
    assert raised.value.reason == "provenance_mismatch"
    before = dict(os.environ)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: (_ for _ in ()).throw(VendorError("PROVIDER_CONFIG_MISSING", "missing vendor configuration")))
    with pytest.raises(VendorError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=OPEN, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_CONFIG_MISSING"
    assert dict(os.environ) == before


def test_class3_legacy_v1_route_is_read_only_and_refuses_unmapped_payloads(monkeypatch):
    seen = {}

    class Outcome:
        vendor = "hdapi"
        vendor_version = 1
        input_fingerprint = "c" * 64
        payload = {"ok": True}

    def fake_ingest(inputs, **kwargs):
        seen.update(kwargs)
        seen["inputs"] = inputs
        return Outcome()

    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", fake_ingest)
    legacy_env = dict(OPEN, HD_API_BASE_URL="https://vendor.test/v1")
    with pytest.raises(CompatBoundaryError) as raised:
        resolve_compat_chart(dict(BIRTH), source_policy="vendor", env=legacy_env, local_lookup=lambda *_: None)
    assert raised.value.reason == "chart_incomplete"
    assert seen["dry_run"] is True and seen["success_log"] is None and seen["retry_log"] is None
    assert seen["inputs"].user_id == resolve_db_user_id(_derived_birth_uid(BIRTH))


# --- current-row accessor ---------------------------------------------------------------

class _DB:
    def __init__(self, rows, raise_adapter=False):
        self.rows = rows
        self.raise_adapter = raise_adapter
        self.queries: list[tuple[str, tuple]] = []

    def query(self, sql, params=None):
        self.queries.append((sql, tuple(params)))
        if self.raise_adapter:
            from engine.db.errors import PrimaryUnavailable

            raise PrimaryUnavailable(code="primary_connect_failed")
        return list(self.rows)


def test_current_row_accessor_is_parameterized_read_only_and_binds_identity():
    db = _DB([(UUID_A, "hdapi", 2, "a" * 64, json.dumps(_chart(UUID_A)))])
    row = read_current_mapped_bodygraph(db, UUID_A)
    assert row is not None and row.user_id == UUID_A and row.vendor_version == 2
    sql, params = db.queries[0]
    assert "public.hde_body_graphs_current" in sql and "vendor = 'hdapi'" in sql and "%s" in sql
    assert params == (UUID_A,)
    for verb in ("INSERT", "UPDATE", "DELETE", "CALL"):
        assert verb not in sql.upper()
    assert read_current_mapped_bodygraph(_DB([]), UUID_A) is None


@pytest.mark.parametrize(
    ("rows", "code"),
    [
        ([(UUID_A, "hdapi", 2, "a" * 64, "{bad"), ], "DB_PAYLOAD_INVALID"),
        ([(UUID_B, "hdapi", 2, "a" * 64, json.dumps(_chart(UUID_A)))], "DB_ROW_CONTRACT_VIOLATED"),
        ([(UUID_A, "other", 2, "a" * 64, json.dumps(_chart(UUID_A)))], "DB_ROW_CONTRACT_VIOLATED"),
        ([(UUID_A, "hdapi", True, "a" * 64, json.dumps(_chart(UUID_A)))], "DB_ROW_CONTRACT_VIOLATED"),
        ([(UUID_A, "hdapi", 2, "zz", json.dumps(_chart(UUID_A)))], "DB_ROW_CONTRACT_VIOLATED"),
        ([(UUID_A, "hdapi", 2, "a" * 64, json.dumps(_chart(UUID_A)))] * 2, "DB_ROW_CONTRACT_VIOLATED"),
        ([(UUID_A, "hdapi", 2)], "DB_ROW_CONTRACT_VIOLATED"),
    ],
)
def test_current_row_accessor_refuses_contract_violations(rows, code):
    with pytest.raises(MappedCacheError) as raised:
        read_current_mapped_bodygraph(_DB(rows), UUID_A)
    assert raised.value.code == code


def test_current_row_accessor_requires_strict_uuid_and_surfaces_db_failures():
    for spelling in ("3FA85F64-5717-4562-B3FC-2C963F66AFAA", "{3fa85f64-5717-4562-b3fc-2c963f66afaa}", "not-a-uuid", ""):
        with pytest.raises(MappedCacheError) as raised:
            read_current_mapped_bodygraph(_DB([]), spelling)
        assert raised.value.code == "PROVIDER_INPUT_INVALID"
    with pytest.raises(MappedCacheError) as raised:
        read_current_mapped_bodygraph(_DB([], raise_adapter=True), UUID_A)
    assert raised.value.code == "DB_QUERY_FAILED"
    incomplete = copy.deepcopy(_chart(UUID_A))
    incomplete["bodygraph"]["gates"] = []
    from engine.bodygraph.projection import BodyGraphProjectionError

    with pytest.raises(BodyGraphProjectionError) as projection_error:
        read_current_mapped_bodygraph(_DB([(UUID_A, "hdapi", 2, None, json.dumps(incomplete))]), UUID_A)
    assert projection_error.value.code == "GATES_EMPTY"
