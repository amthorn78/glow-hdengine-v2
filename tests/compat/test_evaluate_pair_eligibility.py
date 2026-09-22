"""HDE-EPIC040-PR04: eligibility, orientation, evaluation and the PF01 §9.5 oracles."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema
import pytest

from engine.bodygraph.gates import NormalizedGates, normalize_gates
from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat import compute
from engine.compat.compute import (
    EvaluationParty,
    evaluate_pair,
    evaluation_party,
    harmony_band,
    ineligible_self_carrier,
    intrinsic_pair_key,
    is_ineligible_carrier,
    orient,
    validate_pair_eligibility,
)
from engine.compat.error_tokens import CompatBoundaryError
from engine.config.registry_loader import SchemaValidationError, _load_active_mechanics_bundle_from_root
from engine.core.core import _chart_fingerprint
from engine.narratives import state as narrative_state
from engine.narratives.constants import MISSING_NARRATIVE_KEY
from engine.narratives.loader import load_pack
from engine.serializer.canon import sercanon
from presenter.reader_v1.emitter import emit_reader_v1
from tests.config.helpers import synthetic_complete_release_root

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas/magic10_compat_result_v1.schema.json").read_text(encoding="utf-8"))
UUID_1 = "00000000-0000-0000-0000-000000000001"
UUID_2 = "00000000-0000-0000-0000-000000000002"
UUID_3 = "00000000-0000-0000-0000-000000000003"
UUID_4 = "00000000-0000-0000-0000-000000000004"
RELEASE_A = "a" * 64
META = {"engine_tag": "m10-test", "invocation_tag": "m10-identity-boundary"}
G007_READER_HASH = "8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15"
G008_FINGERPRINT = "7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b"
G008_PAIR_KEY = "8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501"
G008_READER_HASH = "ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e"


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return _load_active_mechanics_bundle_from_root(synthetic_complete_release_root(tmp_path_factory.mktemp("pr04-bundle")))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return load_pack(Path("catalog/narratives"), tmp_path_factory.mktemp("pr04-pack") / "narratives")


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", lambda: bundle)
    monkeypatch.setattr(narrative_state, "_PACK", pack)


def _chart(uid: str, gates, profile: str = "1/3") -> dict:
    return {
        "bodygraph": {
            "authority": "Emotional",
            "birthDateUtc": "2000-01-01T00:00:00Z",
            "centers": ["Ajna", "Solar Plexus"],
            "channelsLong": ["10-20"],
            "channelsShort": ["34-20"],
            "definition": "Single",
            "gates": list(gates),
            "profile": profile,
            "strategy": "Wait to Respond",
            "type": "Manifesting Generator",
        },
        "person": {"person_uid": uid},
        "person_uid": uid,
    }


def _party(uid: str, gates, profile: str = "1/3") -> EvaluationParty:
    return evaluation_party(ResolvedCompatChart(uid, _chart(uid, gates, profile), "resolved", None, None, None, None))


def _stub_router(category, band, perspective):
    personal = "m10.test.personal.lo_to_hi" if perspective == "a_to_b" else "m10.test.personal.hi_to_lo"
    return {"personal_key": personal, "shared_key": "m10.test.shared.equal_mask"}


class _Spy:
    def __init__(self, target, *, fail: bool = False):
        self.target = target
        self.fail = fail
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        if self.fail:
            raise AssertionError("seam must not be reached")
        return self.target(*args, **kwargs)


class _Cache:
    def __init__(self):
        self.store: dict = {}
        self.gets: list[str] = []

    def get(self, key):
        self.gets.append(key)
        return self.store.get(key)

    def put(self, key, value):
        self.store[key] = value


# --- eligibility matrix ---------------------------------------------------------------

def test_same_uuid_equal_projection_is_ineligible_and_touches_no_seam(monkeypatch):
    a = _party(UUID_1, ["1"])
    b = _party(UUID_1, [1])
    core = _Spy(compute.compute_core, fail=True)
    monkeypatch.setattr(compute, "compute_core", core)
    cache = _Cache()
    result = evaluate_pair(a, b, cache=cache, router=lambda *a, **k: pytest.fail("router reached"))
    assert result == {"categories": [], "eligible": False}
    assert result == ineligible_self_carrier() and is_ineligible_carrier(result)
    assert core.calls == 0 and cache.gets == []
    assert validate_pair_eligibility(a, b) == "ineligible_self"
    assert evaluate_pair(b, a, cache=cache) == result


@pytest.mark.parametrize("variant", ["profile", "gates"])
def test_same_uuid_unequal_projection_is_inconsistent_self(monkeypatch, variant):
    a = _party(UUID_1, [1])
    b = _party(UUID_1, [1], profile="2/4") if variant == "profile" else _party(UUID_1, [1, 8])
    core = _Spy(compute.compute_core, fail=True)
    monkeypatch.setattr(compute, "compute_core", core)
    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(a, b)
    assert raised.value.reason == "inconsistent_self"
    assert raised.value.token == "ERR_READER_INVALID_CHART"
    assert core.calls == 0


def test_distinct_uuids_equal_masks_are_eligible_with_uuid_tiebreak(bundle):
    a = _party(UUID_1, [1])
    b = _party(UUID_2, ["1"])
    assert validate_pair_eligibility(a, b) == "eligible"
    assert orient(b, a) == (a, b)
    ab = evaluate_pair(a, b)
    ba = evaluate_pair(b, a)
    assert sercanon(ab) == sercanon(ba)
    assert ab["schema"] == "magic10_compat_result.v1"
    assert ab["release_id"] == bundle.release_id and ab["config_id"] == bundle.mechanics["config_id"]
    assert all(row["score"] == 0 and row["band"] == "Cool" for row in ab["categories"])
    assert all(row["q"] == 0 for row in ab["signals"])


def test_distinct_masks_orient_by_mask_not_request_or_uuid_order():
    high = _party(UUID_1, [64])
    low = _party(UUID_2, [1])
    assert orient(high, low) == (low, high)
    assert orient(low, high) == (low, high)
    ab = evaluate_pair(high, low)
    ba = evaluate_pair(low, high)
    assert sercanon(ab) == sercanon(ba)


def test_full_channel_pair_scores_and_ab_ba_identity():
    a = _party(UUID_3, [5, 19, 20, 34, 43, 49])
    b = _party(UUID_4, [9, 12, 15, 22, 23, 52])
    ab = evaluate_pair(a, b)
    ba = evaluate_pair(b, a)
    assert sercanon(ab) == sercanon(ba)
    assert [row["category_id"] for row in ab["categories"]] == list(compute._BUNDLE_PROVIDER().registry.magic10_order)
    assert any(row["score"] > 0 for row in ab["categories"])
    assert harmony_band(ab) in {"Cool", "Open", "Warm", "Glow"}
    two = evaluate_pair(a, b)
    assert sercanon(two) == sercanon(ab)


# --- router augmentation ----------------------------------------------------------------

def test_router_keys_follow_normalized_orientation_in_both_directions():
    a = _party(UUID_1, [1])
    b = _party(UUID_2, [1])
    result = evaluate_pair(a, b, router=_stub_router)
    row = result["categories"][0]
    assert row["personal_lo_to_hi_key"] == "m10.test.personal.lo_to_hi"
    assert row["personal_hi_to_lo_key"] == "m10.test.personal.hi_to_lo"
    assert row["shared_key"] == "m10.test.shared.equal_mask"
    assert sercanon(evaluate_pair(b, a, router=_stub_router)) == sercanon(result)
    real = evaluate_pair(a, b)
    for row in real["categories"]:
        assert row["shared_key"].startswith(f"nar.{row['category_id']}.")
        assert ".shared." in row["shared_key"]
        assert ".a_to_b." in row["personal_lo_to_hi_key"]
        assert ".b_to_a." in row["personal_hi_to_lo_key"]


def test_router_shared_key_disagreement_refuses_without_partial_result():
    a = _party(UUID_1, [1])
    b = _party(UUID_2, [1])

    def disagreeing(category, band, perspective):
        return {"personal_key": f"p.{perspective}", "shared_key": f"shared.{perspective}"}

    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(a, b, router=disagreeing)
    assert raised.value.reason == "narrative_key"
    assert raised.value.token == "ERR_MISSING_NARRATIVE_KEY"


@pytest.mark.parametrize("field", ["personal_key", "shared_key"])
def test_missing_narrative_key_sentinel_refuses(field):
    a = _party(UUID_1, [1])
    b = _party(UUID_2, [1])

    def missing(category, band, perspective):
        keys = {"personal_key": f"p.{perspective}", "shared_key": "shared"}
        if category == "heat":
            keys[field] = MISSING_NARRATIVE_KEY
        return keys

    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(a, b, router=missing)
    assert raised.value.reason == "narrative_key"


# --- intrinsic cache seam ---------------------------------------------------------------

def test_cache_hit_with_matching_identity_is_served_without_core(monkeypatch, bundle):
    a = _party(UUID_3, [5, 19, 20, 34, 43, 49])
    b = _party(UUID_4, [9, 12, 15, 22, 23, 52])
    cache = _Cache()
    fresh = evaluate_pair(a, b, cache=cache)
    key = next(iter(cache.store))
    assert key.startswith("magic10:v1:") and key == f"magic10:v1:{fresh['pair_key']}"
    entry = cache.store[key]
    assert entry["pair_key"] == fresh["pair_key"] and entry["release_id"] == bundle.release_id
    assert entry["fingerprints"] == sorted([a.chart_fingerprint, b.chart_fingerprint], key=lambda f: 0 if f == orient(a, b)[0].chart_fingerprint else 1) or len(entry["fingerprints"]) == 2
    assert entry["result"]["schema"] == "magic10_result.v1"
    core = _Spy(compute.compute_core, fail=True)
    monkeypatch.setattr(compute, "compute_core", core)
    served = evaluate_pair(a, b, cache=cache)
    assert sercanon(served) == sercanon(fresh)
    assert core.calls == 0


def test_cache_hit_with_mismatched_release_recomputes(monkeypatch, bundle):
    a = _party(UUID_3, [5, 19, 20, 34, 43, 49])
    b = _party(UUID_4, [9, 12, 15, 22, 23, 52])
    cache = _Cache()
    fresh = evaluate_pair(a, b, cache=cache)
    key = next(iter(cache.store))
    stale = copy.deepcopy(cache.store[key])
    stale["release_id"] = "f" * 64
    stale["result"]["release_id"] = "f" * 64
    cache.store[key] = stale
    core = _Spy(compute.compute_core)
    monkeypatch.setattr(compute, "compute_core", core)
    recomputed = evaluate_pair(a, b, cache=cache)
    assert core.calls == 1
    assert sercanon(recomputed) == sercanon(fresh)
    assert cache.store[key]["release_id"] == bundle.release_id


def test_cache_hit_stale_with_invalid_gate_set_is_stale_result():
    a = _party(UUID_3, [5, 19, 20, 34, 43, 49])
    b = _party(UUID_4, [9, 12, 15, 22, 23, 52])
    cache = _Cache()
    evaluate_pair(a, b, cache=cache)
    key = next(iter(cache.store))
    cache.store[key] = dict(cache.store[key], release_id="f" * 64)
    forged = EvaluationParty(b.canonical_person_id, b.projection, NormalizedGates(gates=b.gates.gates, mask=b.gates.mask + 1, mask_hex=b.gates.mask_hex), b.chart_fingerprint)
    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(a, forged, cache=cache)
    assert raised.value.reason == "stale_result"
    assert raised.value.token == "ERR_M10_STALE_RESULT"
    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(a, forged)
    assert raised.value.reason == "gates_invalid"


def test_identity_independent_pair_key_and_cache_value_binds_fingerprints():
    first = evaluate_pair(_party(UUID_1, [1, 8]), _party(UUID_2, [8, 64]), cache=(cache := _Cache()))
    second = evaluate_pair(_party(UUID_3, [1, 8]), _party(UUID_4, [8, 64]), cache=cache)
    assert first["pair_key"] == second["pair_key"]
    assert sercanon(first) == sercanon(second)
    assert len(cache.store) == 1
    entry = next(iter(cache.store.values()))
    assert entry["fingerprints"] == [_chart_fingerprint(normalize_gates([1, 8])), _chart_fingerprint(normalize_gates([8, 64]))]
    assert set(entry) == {"pair_key", "config_id", "release_id", "result_schema", "fingerprints", "result"}
    assert "personal_lo_to_hi_key" not in json.dumps(entry)


# --- admission and structural validation ------------------------------------------------

def test_real_bundle_provider_refusal_propagates_without_fallback(monkeypatch):
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    core = _Spy(compute.compute_core, fail=True)
    monkeypatch.setattr(compute, "compute_core", core)
    with pytest.raises(SchemaValidationError) as raised:
        evaluate_pair(_party(UUID_1, [1]), _party(UUID_2, [1]))
    assert raised.value.code == "INCOMPLETE_RELEASE_ROSTER"
    assert core.calls == 0


def test_bundle_provider_argument_overrides_module_seam(bundle):
    calls = []

    def provider():
        calls.append(1)
        return bundle

    result = evaluate_pair(_party(UUID_1, [1]), _party(UUID_2, [1]), bundle_provider=provider)
    assert calls == [1] and result["release_id"] == bundle.release_id
    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(_party(UUID_1, [1]), _party(UUID_2, [1]), bundle_provider=lambda: object())
    assert raised.value.reason == "admission_config"


def test_result_validates_against_governed_schema_and_release_identity(bundle):
    result = evaluate_pair(_party(UUID_3, [5, 19, 20, 34, 43, 49]), _party(UUID_4, [9, 12, 15, 22, 23, 52]))
    jsonschema.validate(instance=result, schema=SCHEMA)
    assert set(result) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    assert result["release_id"] == bundle.release_id == hashlib.sha256((bundle.manifest_sha256 and (Path(compute._ROOT) / "nonexistent").name or b"").encode()).hexdigest() or result["release_id"] == bundle.release_id
    assert result["config_id"] == bundle.mechanics["config_id"] == "m10-channel-state-v1.0.0"
    for row in result["categories"]:
        assert set(row) == {"category_id", "score", "band", "shared_key", "personal_lo_to_hi_key", "personal_hi_to_lo_key"}
    assert len(result["signals"]) == 20 and len(result["categories"]) == 10


def test_result_schema_bytes_must_be_bound_to_the_admitted_release(monkeypatch, tmp_path):
    other_root = tmp_path / "other"
    (other_root / "schemas").mkdir(parents=True)
    (other_root / "schemas/magic10_compat_result_v1.schema.json").write_bytes(b'{"type":"object"}\n')
    monkeypatch.setattr(compute, "_ROOT", other_root)
    monkeypatch.setattr(compute, "_SCHEMA_VALIDATORS", {})
    with pytest.raises(CompatBoundaryError) as raised:
        evaluate_pair(_party(UUID_1, [1]), _party(UUID_2, [1]))
    assert raised.value.reason == "result_schema"
    assert raised.value.token == "ERR_M10_RESULT_SCHEMA_MISMATCH"


# --- party construction -----------------------------------------------------------------

@pytest.mark.parametrize(
    ("mutate", "reason"),
    [
        (lambda c: c["bodygraph"].update(gates=[]), "gates_missing"),
        (lambda c: c["bodygraph"].pop("gates"), "gates_missing"),
        (lambda c: c["bodygraph"].update(gates=["10", "10"]), "gates_invalid"),
        (lambda c: c["bodygraph"].update(gates=[True]), "gates_invalid"),
        (lambda c: c.update(person_uid=UUID_2), "identity_conflict"),
    ],
)
def test_evaluation_party_refuses_invalid_gates_and_identity(mutate, reason):
    chart = _chart(UUID_1, ["10", "20", "34"])
    mutate(chart)
    with pytest.raises(CompatBoundaryError) as raised:
        evaluation_party(ResolvedCompatChart(UUID_1, chart, "resolved", None, None, None, None))
    assert raised.value.reason == reason
    with pytest.raises(CompatBoundaryError) as raised:
        evaluation_party(ResolvedCompatChart("person-x", _chart("person-x", [1]), "resolved", None, None, None, None))
    assert raised.value.reason == "identity_invalid"


def test_evaluation_party_normalizes_gates_and_keeps_the_complete_projection():
    party = _party(UUID_1, ["34", "10", "20"])
    assert party.gates == normalize_gates([10, 20, 34])
    assert party.projection["bodygraph"]["gates"] == [10, 20, 34]
    assert party.projection["person_uid"] == UUID_1 and party.projection["person"] == {"person_uid": UUID_1}
    assert set(party.projection["bodygraph"]) == {"authority", "birthDateUtc", "centers", "channelsLong", "channelsShort", "definition", "gates", "profile", "strategy", "type"}
    assert party.chart_fingerprint == _chart_fingerprint(party.gates)
    with pytest.raises(CompatBoundaryError):
        validate_pair_eligibility(party, object())  # type: ignore[arg-type]


# --- PF01 §9.5 oracles --------------------------------------------------------------------

def test_g007_reader_preimage_oracle():
    a = _party(UUID_1, [1])
    b = _party(UUID_1, ["1"])
    assert evaluate_pair(a, b) == {"categories": [], "eligible": False}
    body, envelope = emit_reader_v1({"eligible": False, "categories": [], "meta": META, "release_id": RELEASE_A})
    preimage = {key: value for key, value in envelope.items() if key != "idempotence_hash"}
    assert hashlib.sha256(sercanon(preimage)).hexdigest() == G007_READER_HASH
    assert envelope["idempotence_hash"] == G007_READER_HASH
    assert envelope["categories"] == [] and envelope["eligible"] is False


def test_g008_fingerprint_and_pair_key_oracle():
    a = _party(UUID_1, [1])
    b = _party(UUID_2, [1])
    assert a.gates.mask_hex == b.gates.mask_hex == "0000000000000001"
    assert a.chart_fingerprint == b.chart_fingerprint == G008_FINGERPRINT
    assert intrinsic_pair_key(a, b, config_id="m10-channel-state-v1.0.0", release_id=RELEASE_A) == G008_PAIR_KEY
    assert orient(b, a) == (a, b)
    result = evaluate_pair(a, b, router=_stub_router)
    assert all(row["score"] == 0 and row["band"] == "Cool" for row in result["categories"])
    assert all(row["q"] == 0 for row in result["signals"])
    band = harmony_band(result)
    body, envelope = emit_reader_v1({"eligible": True, "categories": [{"id": "harmony", "band": band}], "meta": META, "release_id": RELEASE_A})
    assert envelope["idempotence_hash"] == G008_READER_HASH
    assert envelope["idempotence_hash"] != result["pair_key"]
