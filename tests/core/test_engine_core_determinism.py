from __future__ import annotations

import dataclasses
import inspect
import json
from pathlib import Path
from types import MappingProxyType

import jsonschema
import pytest

from engine.bodygraph.gates import NormalizedGates, normalize_gates
from engine.config.registry_loader import SchemaValidationError, _load_active_mechanics_bundle_from_root
from engine.core import compute_core
from engine.core.core import _plain
from engine.magic10.composite import ChannelClassification, _classify_channel
from engine.magic10.signals import _signal_q
from engine.magic10_v2 import signals as v2_signals
from engine.magic10_v2.calculation import assign_band
from engine.magic10_v2.kernel import compute_kernel
from engine.magic10_v2.signals import compute_signals
from engine.serializer.canon import sercanon
from tests.config.helpers import (
    admit_synthetic_v2_candidate,
    synthetic_v2_candidate_root,
    v2_candidate_roster,
    v2_candidate_roster_admission,
    write_release_manifest,
)

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
    # HDE-EPIC043 WU-PR-09: the switched core computes magic10_result.v2 over the
    # admitted v2 candidate bundle (the v1 synthetic root refuses UNBOUND_SOURCE).
    return admit_synthetic_v2_candidate(tmp_path_factory.mktemp("core"))


def _assert_v2_shape(result, bundle):
    """magic10_result.v2 closure: governed orders, q in 0..1000, bands from the admitted maxima."""
    assert result.schema == "magic10_result.v2"
    assert result.config_id == bundle.mechanics["config_id"] == "m10-relevance-centers-type-v2.0.0"
    assert result.release_id == bundle.release_id
    assert tuple(r.signal_id for r in result.signals) == SIGNALS
    assert all(type(r.q) is int and 0 <= r.q <= 1000 for r in result.signals)
    assert tuple(r.category_id for r in result.categories) == CATEGORIES
    for row in result.categories:
        assert type(row.score) is int and 0 <= row.score <= 100
        assert row.band == assign_band(row.score, bundle.magic10_v2.maxima[row.category_id])


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
    # M10-G001 is fixed by canon (PF01 §9.5): gates [1] vs [2], no Channel, two
    # Reflectors -> every category 0, band Cool (so every q is 0).
    result = compute_core(normalize_gates([1]), normalize_gates([2]), bundle, bundle.release_id)
    _assert_v2_shape(result, bundle)
    assert [c.score for c in result.categories] == [0] * 10
    assert [c.band for c in result.categories] == ["Cool"] * 10
    assert [s.q for s in result.signals] == [0] * 20
    # G002 (all 64 Gates both sides): its v2 values were set at the cut maxima
    # (tests/fixtures/magic10/v2/goldens.json, compared over the cut release by
    # tools/config/artifacts.py); this bundle carries the labelled fixture maxima,
    # so the homogeneous-companionship state and the v2 result closure are asserted.
    full = normalize_gates(list(range(1, 65)))
    kernel = compute_kernel(full.mask, full.mask, bundle.magic10_v2)
    assert len(kernel.channels) == 36
    assert {(c.state, c.owner) for c in kernel.channels} == {("companionship", None)}
    result = compute_core(full, full, bundle, bundle.release_id)
    _assert_v2_shape(result, bundle)
    assert result == compute_core(full, full, bundle, bundle.release_id)


def test_g004_fixed_oracle_complete_result_and_two_runs(bundle):
    a, b = normalize_gates(SPARSE_A), normalize_gates(SPARSE_B)
    first = compute_core(a, b, bundle, bundle.release_id)
    second = compute_core(a, b, bundle, bundle.release_id)
    assert first == second
    assert sercanon(first.as_payload()) == sercanon(second.as_payload())
    # HDE-EPIC043 WU-PR-09: the v1 q and score vectors were v1 scoring values (retired
    # with the v1 scorers). WU-PR-10 set this pair's v2 values (M10-G004) at the cut
    # maxima, compared over the cut release by tools/config/artifacts.py; over this
    # fixture-maxima bundle the v2 closure and the two-run identity are asserted.
    _assert_v2_shape(first, bundle)
    assert tuple(f.name for f in dataclasses.fields(first)) == (
        "schema", "config_id", "release_id", "pair_key", "signals", "categories",
    )
    jsonschema.validate(first.as_payload(), json.loads((ROOT / "schemas/magic10_result_v2.schema.json").read_bytes()))
    kernel = compute_kernel(a.mask, b.mask, bundle.magic10_v2)
    active = {r.channel_id: (r.state, r.owner) for r in kernel.channels if r.state != "none"}
    assert active == {
        "05-15": ("electromagnetic", None), "09-52": ("dominance", "member_hi"),
        "12-22": ("dominance", "member_hi"), "19-49": ("dominance", "member_lo"),
        "20-34": ("dominance", "member_lo"), "23-43": ("electromagnetic", None),
    }


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
    lambda m: m["center_map"][0]["weights"].update(g=True),
    lambda m: m["center_map"].reverse(),
    lambda m: m.update(result_schema="magic10_compat_result.v2"),
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
    payload = result.as_payload()
    payload["signals"][0]["q"] = 200
    assert result.signals[0].q == 0


# HDE-EPIC043 WU-PR-09: re-targeted from the v1 signal module (_compute_signals) to the
# v2 signal producers the switched core executes.  The v1 parametrizations whose guard
# has no compute-time v2 counterpart (extra key, duplicate or reversed Channel rows, a
# profile on a Balance signal, reversed profiles, an extra or out-of-range response)
# were retired: v2 leaves those structural checks to the v2 loader at admission.
@pytest.mark.parametrize('mutate,code', [
    (lambda m: m['signals'][0].update(operation='unknown'), v2_signals.OPERATION_UNKNOWN),
    (lambda m: m['signals'][0].update(profile_id='unknown'), v2_signals.PROFILE_MISSING),
    (lambda m: m['signals'][0]['channels'][0].update(channel_id='00-00'), v2_signals.CHANNEL_UNKNOWN),
    (lambda m: m['signals'][19].update(operation='twice_min_owner_mass_v1'), v2_signals.OPERATION_UNKNOWN),
    (lambda m: m['profiles'][0]['responses'].update(none=True), v2_signals.PROFILE_MISSING),
])
def test_signal_operation_profile_and_membership_guards(bundle, mutate, code):
    from engine.config.registry_loader import _deep_freeze
    mechanics = json.loads(sercanon(_plain(bundle.mechanics)))
    mutate(mechanics)
    kernel = compute_kernel(1, 128, bundle.magic10_v2)
    forged = dataclasses.replace(bundle.magic10_v2, configuration=_deep_freeze(mechanics))
    with pytest.raises(SchemaValidationError) as caught:
        compute_signals(kernel, forged)
    assert caught.value.code == code


def test_invalid_result_band_is_refused_at_core_boundary(bundle, monkeypatch):
    import engine.core.core as module
    original = module.compute_magic10_v2
    def wrong_band(*args):
        result = original(*args)
        first = dataclasses.replace(result.categories[0], band='Glow')
        return dataclasses.replace(result, categories=(first, *result.categories[1:]))
    monkeypatch.setattr(module, 'compute_magic10_v2', wrong_band)
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
    # HDE-EPIC043 WU-PR-09: the v2 candidate root, admitted through the test-only roster
    # route; the changed member is the v2 signal module the switched core executes.
    root = synthetic_v2_candidate_root(tmp_path)
    with v2_candidate_roster_admission():
        first_bundle = _load_active_mechanics_bundle_from_root(root)
    path = root / 'engine/magic10_v2/signals.py'
    path.write_bytes(path.read_bytes() + b'# synthetic later release member bytes\n')
    write_release_manifest(root, v2_candidate_roster())
    with v2_candidate_roster_admission():
        second_bundle = _load_active_mechanics_bundle_from_root(root)
    a, b = normalize_gates([1]), normalize_gates([8])
    first = compute_core(a, b, first_bundle, first_bundle.release_id)
    second = compute_core(a, b, second_bundle, second_bundle.release_id)
    assert first.release_id != second.release_id and first.pair_key != second.pair_key
    assert first.signals == second.signals and first.categories == second.categories
