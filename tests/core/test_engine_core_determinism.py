from __future__ import annotations

import dataclasses
import inspect
import json
from pathlib import Path
from types import MappingProxyType

import jsonschema
import pytest

from engine.bodygraph.gates import NormalizedGates, normalize_gates
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.core import compute_core
from engine.core.core import _plain
from engine.magic10.composite import ChannelClassification, _classify_channel, _classify_channels
from engine.magic10.signals import _compute_signals, _signal_q
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_complete_release_root

ROOT = Path(__file__).resolve().parents[2]
SIGNALS = (
    "rapport_delta", "resonance_strength", "spark_intensity", "momentum_flux",
    "signal_clarity", "exchange_density", "vector_cohesion", "axis_agreement",
    "soothe_index", "buffer_resilience", "pattern_integrity", "variance_stability",
    "growth_tendency", "horizon_reach", "novelty_factor", "expression_flow",
    "willpower_current", "focus_pressure", "equilibrium_score", "counterweight_ratio",
)
CATEGORIES = ("harmony", "heat", "communication", "alignment", "comfort",
              "consistency", "expansion", "creativity", "drive", "balance")
SPARSE_A = [5, 19, 20, 34, 43, 49]
SPARSE_B = [9, 12, 15, 22, 23, 52]


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    root = synthetic_complete_release_root(tmp_path_factory.mktemp("core"))
    return _load_active_mechanics_bundle_from_root(root)


def test_exact_four_required_arguments():
    parameters = inspect.signature(compute_core).parameters
    assert tuple(parameters) == ("member_a", "member_b", "mechanics_bundle", "release_id")
    assert all(p.default is inspect.Parameter.empty and
               p.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD for p in parameters.values())


# Source-owned 4x4 endpoint cases, with the full owner before mask normalization.
CASES = (
    (0, 0, "none", None), (0, 1, "none", None), (0, 2, "none", None), (0, 3, "dominance", "b"),
    (1, 0, "none", None), (1, 1, "none", None), (1, 2, "electromagnetic", None), (1, 3, "compromise", "b"),
    (2, 0, "none", None), (2, 1, "electromagnetic", None), (2, 2, "none", None), (2, 3, "compromise", "b"),
    (3, 0, "dominance", "a"), (3, 1, "compromise", "a"), (3, 2, "compromise", "a"), (3, 3, "companionship", None),
)


@pytest.mark.parametrize("a,b,state,owner", CASES)
@pytest.mark.parametrize("extra_a", (0, 1 << 63))
def test_all_16_states_and_numeric_owner_normalization(a, b, state, owner, extra_a):
    def mask(value):
        return (1 if value & 1 else 0) | (128 if value & 2 else 0)
    ma, mb = mask(a) | extra_a, mask(b)
    lo, hi = sorted((ma, mb))
    expected = None if owner is None else (
        "member_lo" if (ma if owner == "a" else mb) == lo else "member_hi"
    )
    row = _classify_channel("01-08", (1, 8), lo, hi)
    assert (row.state, row.owner) == (state, expected)
    if owner:
        raw_ab = _classify_channel("01-08", (1, 8), ma, mb)
        raw_ba = _classify_channel("01-08", (1, 8), mb, ma)
        assert raw_ab.state == raw_ba.state
        assert {raw_ab.owner, raw_ba.owner} == {"member_lo", "member_hi"}


def test_case_roster_counts():
    from collections import Counter
    assert Counter(row[2] for row in CASES) == {
        "none": 7, "compromise": 4, "dominance": 2, "electromagnetic": 2, "companionship": 1,
    }


def test_catalog_integration_exceptions(bundle):
    channels = bundle.registry.channels
    assert tuple(c.id for c in channels.values() if c.substream == "integration") == (
        "10-20", "10-57", "20-34", "34-57",
    )
    assert channels["10-34"].substream == "centering"
    assert channels["20-57"].substream == "knowing"


def test_g001_none_and_g002_homogeneous_companionship(bundle):
    for gates, scores, bands in [
        ([1], [0] * 10, ["Cool"] * 10),
        (list(range(1, 65)), [100, 50, 75, 100, 100, 100, 50, 63, 50, 50],
         ["Glow", "Warm", "Glow", "Glow", "Glow", "Glow", "Warm", "Warm", "Warm", "Warm"]),
    ]:
        result = compute_core(normalize_gates(gates), normalize_gates(gates), bundle, bundle.release_id)
        assert [c.score for c in result.categories] == scores
        assert [c.band for c in result.categories] == bands
        if gates == [1]:
            assert [s.q for s in result.signals] == [0] * 20


def test_g004_fixed_oracle_complete_result_and_two_runs(bundle):
    a, b = normalize_gates(SPARSE_A), normalize_gates(SPARSE_B)
    first = compute_core(a, b, bundle, bundle.release_id)
    second = compute_core(a, b, bundle, bundle.release_id)
    assert first == second
    assert sercanon(first.to_payload()) == sercanon(second.to_payload())
    assert tuple(r.signal_id for r in first.signals) == SIGNALS
    assert [r.q for r in first.signals] == [25, 63, 0, 38, 40, 20, 0, 25, 50, 38, 50, 0, 0, 0, 50, 20, 0, 60, 0, 33]
    assert tuple(r.category_id for r in first.categories) == CATEGORIES
    assert [r.score for r in first.categories] == [22, 10, 15, 6, 22, 13, 0, 18, 15, 8]
    assert all(r.band == "Cool" for r in first.categories)
    assert tuple(f.name for f in dataclasses.fields(first)) == (
        "schema", "config_id", "release_id", "pair_key", "signals", "categories",
    )
    jsonschema.validate(first.to_payload(), json.loads((ROOT / "schemas/magic10_result_v1.schema.json").read_bytes()))
    active = {r.channel_id: (r.state, r.owner) for r in _classify_channels(a.mask, b.mask, bundle.registry.channels) if r.state != "none"}
    assert active == {
        "05-15": ("electromagnetic", None), "09-52": ("dominance", "member_hi"),
        "12-22": ("dominance", "member_hi"), "19-49": ("dominance", "member_lo"),
        "20-34": ("dominance", "member_lo"), "23-43": ("electromagnetic", None),
    }


@pytest.mark.parametrize("profile,expected", [
    ("activation_bp_v1", [0, 100, 150, 50, 200]),
    ("coherence_bp_v1", [0, 200, 100, 50, 150]),
    ("expression_bp_v1", [0, 150, 100, 50, 200]),
])
def test_ordinary_profiles_exact_responses(bundle, profile, expected):
    responses = next(r["responses"] for r in bundle.mechanics["profiles"] if r["profile_id"] == profile)
    for state, q in zip(("none", "companionship", "dominance", "compromise", "electromagnetic"), expected):
        row = ChannelClassification("01-08", state, "member_hi" if state in ("dominance", "compromise") else None)
        assert _signal_q("weighted_state_sum_v1", ({"channel_id": "01-08", "weight": 1},),
                         {"01-08": row}, responses) == q


def test_g003_balance_mass_and_weighted_rounding(bundle):
    channels = bundle.mechanics["signals"][18]["channels"]
    ids = [r["channel_id"] for r in channels]
    for split, expected in [(0, 0), (1, 67), (2, 133), (3, 200), (6, 0)]:
        rows = {name: ChannelClassification(name, "dominance", "member_lo" if i < split else "member_hi") for i, name in enumerate(ids)}
        assert _signal_q("twice_min_owner_mass_v1", channels, rows) == expected
        reversed_rows = {name: dataclasses.replace(row, owner="member_hi" if row.owner == "member_lo" else "member_lo") for name, row in rows.items()}
        assert _signal_q("twice_min_owner_mass_v1", channels, reversed_rows) == expected
    for state in ("none", "companionship", "electromagnetic"):
        rows = {name: ChannelClassification(name, state, None) for name in ids}
        assert _signal_q("twice_min_owner_mass_v1", channels, rows) == 0
        assert _signal_q("companionship_em_mass_v1", channels, rows) == (0 if state == "none" else 200)
    pair = ({"channel_id": "01-08", "weight": 1}, {"channel_id": "02-14", "weight": 3})
    rows = {"01-08": ChannelClassification("01-08", "none", None),
            "02-14": ChannelClassification("02-14", "compromise", "member_lo")}
    responses = next(r["responses"] for r in bundle.mechanics["profiles"] if r["profile_id"] == "coherence_bp_v1")
    assert _signal_q("weighted_state_sum_v1", pair, rows, responses) == 38


@pytest.mark.parametrize("bad", [None, {}, [1], NormalizedGates((), 0, "0000000000000000"),
    NormalizedGates((True,), 1, "0000000000000001"), NormalizedGates((1.0,), 1, "0000000000000001"),
    NormalizedGates((1, 1), 1, "0000000000000001"), NormalizedGates((2, 1), 3, "0000000000000003"),
    NormalizedGates((0,), 1, "0000000000000001"), NormalizedGates((65,), 1, "0000000000000001"),
    NormalizedGates((1,), True, "0000000000000001"), NormalizedGates((1,), 2, "0000000000000001"),
    NormalizedGates((1,), 1, "1"), NormalizedGates([1], 1, "0000000000000001")])
def test_invalid_normalized_members_refuse_without_payload(bad, bundle):
    with pytest.raises(ValueError, match="^invalid pure core contract$"):
        compute_core(bad, normalize_gates([8]), bundle, bundle.release_id)


@pytest.mark.parametrize("release", [None, "", "A" * 64, "0" * 64, 1, True, "0" * 65])
def test_invalid_release_refuses(release, bundle):
    with pytest.raises(ValueError, match="^invalid pure core contract$"):
        compute_core(normalize_gates([1]), normalize_gates([8]), bundle, release)


def test_forged_bundle_and_mutable_graph_refuse(bundle):
    from dataclasses import replace
    wrong_caps = dict(bundle.registry.magic10_caps)
    wrong_caps["harmony"] = replace(wrong_caps["harmony"], inputs=("unknown", "resonance_strength"))
    variants = [
        {}, replace(bundle, mechanics=dict(bundle.mechanics)),
        replace(bundle, manifest_sha256="0" * 64), replace(bundle, config_sha256="0" * 64),
        replace(bundle, source_identities=bundle.source_identities[:-1]),
        replace(bundle, registry=replace(bundle.registry, magic10_order=tuple(reversed(CATEGORIES)))),
        replace(bundle, registry=replace(bundle.registry, channels=MappingProxyType(dict(list(bundle.registry.channels.items())[:-1])))),
        replace(bundle, registry=replace(bundle.registry, magic10_caps=MappingProxyType(wrong_caps))),
        replace(bundle, registry=replace(bundle.registry, gates=dict(bundle.registry.gates))),
    ]
    for forged in variants:
        with pytest.raises(ValueError, match="^invalid pure core contract$"):
            compute_core(normalize_gates([1]), normalize_gates([8]), forged, bundle.release_id)


@pytest.mark.parametrize("mutate", [
    lambda m: m.pop("signals"), lambda m: m.update(extra=1),
    lambda m: m["signals"].reverse(), lambda m: m["signals"].pop(),
    lambda m: m["signals"].append(m["signals"][0]),
    lambda m: m["signals"][0].update(operation="unknown"),
    lambda m: m["signals"][0].update(profile_id="unknown"),
    lambda m: m["profiles"][0]["responses"].update(none=True),
    lambda m: m["signals"][0]["channels"][0].update(weight=0),
    lambda m: m["signals"][0]["channels"][0].update(weight=4),
    lambda m: m["signals"][0]["channels"][0].update(channel_id="00-00"),
    lambda m: m["category_weights"][0].update(weights=[1, True]),
    lambda m: m["category_weights"].reverse(),
    lambda m: m.update(result_schema="magic10_compat_result.v1"),
])
def test_changed_frozen_mechanics_cannot_reuse_admitted_identity(bundle, mutate):
    from engine.config.registry_loader import _deep_freeze
    # The captured admitted source identity is deliberately retained.
    mechanics = json.loads(sercanon(_plain(bundle.mechanics)))
    mutate(mechanics)
    forged = dataclasses.replace(bundle, mechanics=_deep_freeze(mechanics))
    with pytest.raises(ValueError, match="^invalid pure core contract$"):
        compute_core(normalize_gates([1]), normalize_gates([8]), forged, bundle.release_id)


@pytest.mark.parametrize("weight", [True, 1.0, "1", 0, -1, 4])
def test_signal_weight_domain_is_exact(weight):
    row = ChannelClassification("01-08", "none", None)
    with pytest.raises(ValueError):
        _signal_q("companionship_em_mass_v1", ({"channel_id": "01-08", "weight": weight},), {"01-08": row})


@pytest.mark.parametrize("state,owner", [("unknown", None), ("dominance", None),
    ("compromise", "person"), ("none", "member_lo"), ("companionship", "member_hi")])
def test_signal_state_owner_refuses(state, owner):
    with pytest.raises(ValueError):
        _signal_q("twice_min_owner_mass_v1", ({"channel_id": "01-08", "weight": 1},),
                  {"01-08": ChannelClassification("01-08", state, owner)})


def test_result_and_source_immutability(bundle):
    a = normalize_gates([1])
    result = compute_core(a, a, bundle, bundle.release_id)
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.pair_key = "0" * 64
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.signals[0].q = 1
    with pytest.raises(TypeError):
        result.categories[0] = result.categories[1]
    with pytest.raises(TypeError):
        bundle.mechanics["config_id"] = "changed"
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.mask = 2
    payload = result.to_payload()
    payload["signals"][0]["q"] = 200
    assert result.signals[0].q == 0


@pytest.mark.parametrize('mutate', [
    lambda m: m['signals'][0].update(operation='unknown'),
    lambda m: m['signals'][0].update(profile_id='unknown'),
    lambda m: m['signals'][0].update(extra='unowned'),
    lambda m: m['signals'][0]['channels'].append(m['signals'][0]['channels'][0]),
    lambda m: m['signals'][0]['channels'].reverse(),
    lambda m: m['signals'][0]['channels'][0].update(channel_id='00-00'),
    lambda m: m['signals'][18].update(profile_id='coherence_bp_v1'),
    lambda m: m['signals'][19].update(operation='twice_min_owner_mass_v1'),
    lambda m: m['profiles'].reverse(),
    lambda m: m['profiles'][0]['responses'].update(extra=0),
    lambda m: m['profiles'][0]['responses'].update(none=True),
    lambda m: m['profiles'][0]['responses'].update(none=10001),
    lambda m: m['profiles'][0]['responses'].update(dominance=10000),
])
def test_signal_operation_profile_and_membership_guards(bundle, mutate):
    from engine.config.registry_loader import _deep_freeze
    mechanics = json.loads(sercanon(_plain(bundle.mechanics)))
    mutate(mechanics)
    classified = _classify_channels(1, 128, bundle.registry.channels)
    with pytest.raises((ValueError, KeyError)):
        _compute_signals(classified, _deep_freeze(mechanics), SIGNALS)


def test_invalid_result_band_is_refused_at_core_boundary(bundle, monkeypatch):
    import engine.core.core as module
    original = module._reduce_category
    def wrong_band(*args):
        return dataclasses.replace(original(*args), band='Glow')
    monkeypatch.setattr(module, '_reduce_category', wrong_band)
    with pytest.raises(ValueError, match='^invalid pure core contract$'):
        compute_core(normalize_gates([1]), normalize_gates([1]), bundle, bundle.release_id)


def test_cyclic_forged_mapping_is_bounded(bundle):
    underlying = {}
    proxy = MappingProxyType(underlying)
    underlying['cycle'] = proxy
    forged = dataclasses.replace(bundle, mechanics=proxy)
    with pytest.raises(ValueError, match='^invalid pure core contract$'):
        compute_core(normalize_gates([1]), normalize_gates([8]), forged, bundle.release_id)


def test_new_coherent_admitted_release_changes_pair_identity(tmp_path):
    from tests.config.helpers import write_synthetic_release_manifest
    root = synthetic_complete_release_root(tmp_path)
    first_bundle = _load_active_mechanics_bundle_from_root(root)
    path = root / 'engine/magic10/signals.py'
    path.write_bytes(path.read_bytes() + b'# synthetic later release member bytes\n')
    write_synthetic_release_manifest(root)
    second_bundle = _load_active_mechanics_bundle_from_root(root)
    a, b = normalize_gates([1]), normalize_gates([8])
    first = compute_core(a, b, first_bundle, first_bundle.release_id)
    second = compute_core(a, b, second_bundle, second_bundle.release_id)
    assert first.release_id != second.release_id and first.pair_key != second.pair_key
    assert first.signals == second.signals and first.categories == second.categories
