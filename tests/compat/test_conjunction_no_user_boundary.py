"""R040-IA30-02 proof classes 1–5 at the real conjunction boundary.

Class 1: successful birth-only/no-user resolution through the real boundary.
Class 2: successful permitted acquisition seam (fake transport, real adapter).
Class 3: closed-rails miss refuses without evaluation.
Class 4: missing/invalid chart and identity refuse before evaluator/cache/router.
Class 5: prohibited side effects never occur (no vendor call, no write, no log value).
"""
from __future__ import annotations

import json
import os
import uuid
from pathlib import Path

import pytest

from engine.bodygraph import ingest as ingest_module
from engine.bodygraph import resolver
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.resolver import _derived_birth_uid
from engine.bodygraph.vendor_client import VendorError, VendorRequest, VendorResult
from engine.compat import compute
from engine.compat.compute import EvaluationParty, conjunction_public, conjunction_public_resolved, evaluation_party
from engine.compat.error_tokens import CompatBoundaryError
from engine.presenter import emit_public
from tests.support.pr04_fixtures import (
    BIRTH_LEFT,
    BIRTH_RIGHT,
    GATES_B,
    UUID_A,
    UUID_B,
    RowStore,
    build_bundle,
    build_pack,
    complete_chart,
    current_row,
    inject_seams,
)

ROOT = Path(__file__).resolve().parents[2]
VENDOR_CHART = json.loads((ROOT / "tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json").read_text(encoding="utf-8"))["payload"]
CLOSED = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
OPEN = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v2", "HD_API_KEY": "set", "GEO_API_KEY": "set"}


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-conjunction-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-conjunction-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)


class _Spy:
    def __init__(self, target, *, fail=False):
        self.target, self.fail, self.calls = target, fail, []

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        if self.fail:
            raise AssertionError("seam must not be reached")
        return self.target(*args, **kwargs)


def _forbid_side_effects(monkeypatch):
    calls = {"vendor": 0, "ingest": 0, "persist": 0, "db": 0, "log": 0}
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: calls.__setitem__("vendor", calls["vendor"] + 1) or pytest.fail("vendor client constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: calls.__setitem__("ingest", calls["ingest"] + 1) or pytest.fail("ingest attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: calls.__setitem__("persist", calls["persist"] + 1) or pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: calls.__setitem__("db", calls["db"] + 1) or pytest.fail("DB constructed"))
    monkeypatch.setattr(ingest_module, "_append_jsonl", lambda path, record: calls.__setitem__("log", calls["log"] + 1) or pytest.fail("value log written"))
    return calls


def _birth_key(birth):
    return str(uuid.UUID(resolve_db_user_id(str(_derived_birth_uid(birth)))))


def _store_for(*births):
    rows = {}
    for birth, gates in zip(births, ([*GATES_B], ["10", "20", "34"])):
        seed = _derived_birth_uid(birth)
        key = _birth_key(birth)
        rows[key] = current_row(key, complete_chart(f"person-{seed}", gates))
    return RowStore(rows)


# --- class 1 -------------------------------------------------------------------------

def test_birth_only_no_user_success_through_real_boundary(monkeypatch):
    calls = _forbid_side_effects(monkeypatch)
    store = _store_for(BIRTH_LEFT, BIRTH_RIGHT)
    core = _Spy(compute.compute_core)
    monkeypatch.setattr(compute, "compute_core", core)
    handoff: list[tuple[EvaluationParty, EvaluationParty]] = []
    real_evaluate = compute.evaluate_pair

    def spy_evaluate(a, b, **kwargs):
        handoff.append((a, b))
        return real_evaluate(a, b, **kwargs)

    monkeypatch.setattr(compute, "evaluate_pair", spy_evaluate)

    ab = conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env=CLOSED, local_lookup=store)
    ba = conjunction_public_resolved(dict(BIRTH_RIGHT), dict(BIRTH_LEFT), env=CLOSED, local_lookup=store)

    assert "person_uid" not in BIRTH_LEFT and "user_id" not in BIRTH_LEFT
    expected_keys = {_birth_key(BIRTH_LEFT), _birth_key(BIRTH_RIGHT)}
    assert set(store.lookups) == expected_keys
    for key in store.lookups:
        assert key == str(uuid.UUID(resolve_db_user_id(_derived_birth_uid({**BIRTH_LEFT} if key == _birth_key(BIRTH_LEFT) else {**BIRTH_RIGHT}))))
    for party in handoff[0]:
        assert type(party) is EvaluationParty
        assert uuid.UUID(party.canonical_person_id) and party.canonical_person_id in expected_keys
        assert set(party.projection) == {"bodygraph", "person", "person_uid"}
        assert type(party.gates).__name__ == "NormalizedGates" and party.gates.gates
        assert len(party.chart_fingerprint) == 64
    assert core.calls and len(core.calls) == 2
    assert {ab["conjunction"]["left"]["person_uid"], ab["conjunction"]["right"]["person_uid"]} == expected_keys
    assert ab["conjunction"]["compat"]["schema"] == "magic10_compat_result.v1"
    ab_bytes, ba_bytes = emit_public(ab), emit_public(ba)
    assert ab_bytes == ba_bytes
    assert emit_public(conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env=CLOSED, local_lookup=store)) == ab_bytes
    assert ab_bytes.endswith(b"\n") and not ab_bytes.startswith(b"\xef\xbb\xbf")
    assert calls == {"vendor": 0, "ingest": 0, "persist": 0, "db": 0, "log": 0}


# --- class 2 -------------------------------------------------------------------------

def test_local_miss_permitted_acquisition_returns_complete_chart(monkeypatch):
    order: list[str] = []
    seed_left, seed_right = _derived_birth_uid(BIRTH_LEFT), _derived_birth_uid(BIRTH_RIGHT)

    class FakeTransport:
        def build_contract_route_request(self, **kwargs):
            assert kwargs["path"] == "charts"
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=b"{}\n", input_fingerprint="b" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request):
            order.append(f"fetch:{os.environ.get('SAFE_MODE')}:{os.environ.get('ALLOW_NETWORK')}")
            return VendorResult(payload={"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": dict(VENDOR_CHART)}, duration_ms=1, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeTransport())
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("legacy ingest attempted"))
    monkeypatch.setattr(ingest_module, "_append_jsonl", lambda path, record: pytest.fail("value log written"))
    real_evaluate = compute.evaluate_pair

    def spy_evaluate(a, b, **kwargs):
        order.append("evaluate")
        return real_evaluate(a, b, **kwargs)

    monkeypatch.setattr(compute, "evaluate_pair", spy_evaluate)
    before = dict(os.environ)

    payload = conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env=OPEN, local_lookup=lambda *_: None)

    assert order == ["fetch:1:0", "fetch:1:0", "evaluate"]
    assert dict(os.environ) == before
    ids = {payload["conjunction"]["left"]["person_uid"], payload["conjunction"]["right"]["person_uid"]}
    assert ids == {_birth_key(BIRTH_LEFT), _birth_key(BIRTH_RIGHT)}
    assert payload["conjunction"]["compat"]["schema"] == "magic10_compat_result.v1"
    assert seed_left != seed_right


# --- class 3 -------------------------------------------------------------------------

def test_closed_rails_miss_refuses_without_evaluation(monkeypatch):
    calls = _forbid_side_effects(monkeypatch)
    monkeypatch.setattr(compute, "evaluate_pair", _Spy(compute.evaluate_pair, fail=True))
    monkeypatch.setattr(compute, "compute_core", _Spy(compute.compute_core, fail=True))
    with pytest.raises(VendorError) as raised:
        conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"
    with pytest.raises(VendorError) as raised:
        conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env={"SAFE_MODE": "0", "ALLOW_NETWORK": "0"}, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_NETWORK_BLOCKED"
    with pytest.raises(VendorError) as raised:
        conjunction_public_resolved(dict(BIRTH_LEFT), dict(BIRTH_RIGHT), env=None, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"
    assert calls == {"vendor": 0, "ingest": 0, "persist": 0, "db": 0, "log": 0}
    assert "person_uid" not in str(raised.value.as_payload())


def test_closed_rails_stored_user_miss_refuses_and_local_policy_is_missing_chart(monkeypatch):
    _forbid_side_effects(monkeypatch)
    with pytest.raises(VendorError) as raised:
        conjunction_public_resolved({"user_id": "missing-left"}, {"user_id": "missing-right"}, env=CLOSED, local_lookup=lambda *_: None)
    assert raised.value.code == "PROVIDER_REFUSED"
    with pytest.raises(CompatBoundaryError) as boundary:
        conjunction_public_resolved({"user_id": "missing-left"}, {"user_id": "missing-right"}, env=CLOSED, local_lookup=lambda *_: None, source_policy="local")
    assert boundary.value.reason == "person_unresolved"


# --- class 4 -------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("left", "reason"),
    [
        ({"person_uid": UUID_A}, "person_unresolved"),
        ({"mechanics": {"type": "Generator"}}, "legacy_input"),
        (complete_chart(UUID_A, []), "gates_missing"),
        (complete_chart(UUID_A, ["10", "10"]), "gates_invalid"),
        (complete_chart(UUID_A, [10, "10"]), "gates_invalid"),
        (complete_chart(UUID_A, [True]), "gates_invalid"),
        (complete_chart(UUID_A, ["010"]), "gates_invalid"),
        (complete_chart(UUID_A, [" 10"]), "gates_invalid"),
        (complete_chart(UUID_A, ["+10"]), "gates_invalid"),
        (complete_chart(UUID_A, [10.0]), "gates_invalid"),
        (complete_chart(UUID_A, [0]), "gates_invalid"),
        (complete_chart(UUID_A, [65]), "gates_invalid"),
        ({**complete_chart(UUID_A), "user_id": UUID_B}, "identity_conflict"),
        ({**complete_chart("person-nobody")}, "identity_unresolved"),
    ],
)
def test_missing_or_invalid_chart_and_identity_refuse_before_evaluation(monkeypatch, left, reason):
    _forbid_side_effects(monkeypatch)
    monkeypatch.setattr(compute, "evaluate_pair", _Spy(compute.evaluate_pair, fail=True))
    monkeypatch.setattr(compute, "route_keys", _Spy(compute.route_keys, fail=True))
    right = complete_chart(UUID_B, GATES_B)
    with pytest.raises(CompatBoundaryError) as raised:
        conjunction_public_resolved(left, right, env=CLOSED, local_lookup=lambda *_: None, source_policy="local")
    assert raised.value.reason == reason


def test_malformed_shape_and_inconsistent_self_refuse(monkeypatch):
    _forbid_side_effects(monkeypatch)
    incomplete = complete_chart(UUID_A)
    incomplete["bodygraph"].pop("profile")
    with pytest.raises(CompatBoundaryError) as raised:
        conjunction_public_resolved(incomplete, complete_chart(UUID_B, GATES_B), env=CLOSED, source_policy="local")
    assert raised.value.reason == "chart_incomplete"
    monkeypatch.setattr(compute, "compute_core", _Spy(compute.compute_core, fail=True))
    with pytest.raises(CompatBoundaryError) as raised:
        conjunction_public_resolved(complete_chart(UUID_A), complete_chart(UUID_A, profile="2/4"), env=CLOSED, source_policy="local")
    assert raised.value.reason == "inconsistent_self"
    assert raised.value.token == "ERR_READER_INVALID_CHART"


def test_valid_self_pair_returns_carrier_and_distinct_equal_masks_evaluate(monkeypatch):
    calls = _forbid_side_effects(monkeypatch)
    monkeypatch.setattr(compute, "compute_core", _Spy(compute.compute_core, fail=True))
    carrier = conjunction_public_resolved(complete_chart(UUID_A), complete_chart(UUID_A), env=CLOSED, source_policy="local")
    assert carrier == {"categories": [], "eligible": False}
    monkeypatch.setattr(compute, "compute_core", compute.compute_core.__wrapped__ if hasattr(compute.compute_core, "__wrapped__") else __import__("engine.core.core", fromlist=["compute_core"]).compute_core)
    equal_masks = conjunction_public_resolved(complete_chart(UUID_A), complete_chart(UUID_B), env=CLOSED, source_policy="local")
    assert equal_masks["conjunction"]["left"]["person_uid"] == UUID_A
    assert equal_masks["conjunction"]["right"]["person_uid"] == UUID_B
    assert equal_masks["conjunction"]["compat"]["categories"][0]["personal_lo_to_hi_key"].count(".a_to_b.") == 1
    assert calls["vendor"] == 0


def test_conjunction_public_is_a_thin_pure_entry(monkeypatch):
    _forbid_side_effects(monkeypatch)
    from engine.bodygraph.resolver import ResolvedCompatChart

    a = evaluation_party(ResolvedCompatChart(UUID_A, complete_chart(UUID_A), "resolved", None, None, None, None))
    b = evaluation_party(ResolvedCompatChart(UUID_B, complete_chart(UUID_B, GATES_B), "resolved", None, None, None, None))
    monkeypatch.setattr(resolver, "resolve_compat_chart", lambda *a, **k: pytest.fail("pure entry must not resolve"))
    first = conjunction_public(a, b, viewer_top="heat", viewer_weights={"heat": 10}, engine_tag="x", release_id="y", invocation_tag="z")
    second = conjunction_public(b, a)
    assert emit_public(first) == emit_public(second)
    assert set(first["conjunction"]) == {"left", "right", "compat"}
    assert "meta" not in first["conjunction"]["compat"] and "keys" not in first["conjunction"]["compat"]
    assert "viewer_prefs" not in first
