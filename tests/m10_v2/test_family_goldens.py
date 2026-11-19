"""HDE-EPIC043 WU-PR-04 and WU-PR-10: the v2 proof family, the v2 goldens (HDE-DIST008.1, item F-10).

HDE Math Spec §9.5: the v2 goldens ``M10-G001`` to ``M10-G008`` are computed from
the final formula and the per-category maxima, and checked in both pair orders.
``M10-G001`` (no Channel, two Reflectors) is fixed: every category scores ``0``,
band Cool. The values of ``M10-G002`` to ``M10-G008`` were set at the cut
(WU-PR-10) from the governed configuration and the cut maxima in
``math/thresholds.json``.

The calculation-level cases are checked here independently of the comparator, over
``v2_cut_bundle`` (the governed cut bytes): ``M10-G001``, ``M10-G002`` and
``M10-G004`` through ``compute_magic10_v2`` in both pair orders, ``M10-G003``
through ``compute_signals`` with the owners swapped, and ``M10-G006`` through
``assign_band`` at each category's own maxima. Every case, the application-level
``M10-G005``, ``M10-G007`` and ``M10-G008`` included, is also compared over the
active cut release by the comparator. The refused mutations change the case or
the order dependence, not the code.
"""
from __future__ import annotations

import copy
import dataclasses
import json
from pathlib import Path

import pytest

from engine.magic10_v2 import calculation
from engine.magic10_v2.kernel import ChannelState, compute_kernel
from engine.magic10_v2.signals import compute_signals
from tools.config import artifacts

ROOT = Path(__file__).resolve().parents[2]
GOLDENS_PATH = ROOT / "tests" / "fixtures" / "magic10" / "v2" / "goldens.json"
GOLDENS = json.loads(GOLDENS_PATH.read_bytes())
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
SWAP = {"member_lo": "member_hi", "member_hi": "member_lo"}


def _case(case_id: str) -> dict:
    return next(case for case in GOLDENS["cases"] if case["case_id"] == case_id)


def _check_golden(case: dict, bundle, mask_of) -> None:
    mask_a, mask_b = mask_of(*case["inputs"]["gates_a"]), mask_of(*case["inputs"]["gates_b"])
    kernel = compute_kernel(mask_a, mask_b, bundle)
    assert kernel.member_lo.derived_type == kernel.member_hi.derived_type == "Reflector"
    assert all(item.state == "none" for item in kernel.channels)
    for first, second in ((mask_a, mask_b), (mask_b, mask_a)):
        result = calculation.compute_magic10_v2(first, second, bundle, GOLDENS["constants"]["release_id"])
        got = [{"band": item.band, "category_id": item.category_id, "score": item.score} for item in result.categories]
        assert got == case["expected"]["categories"]


def _check_core_golden(case: dict, bundle, mask_of) -> None:
    """M10-G002 / M10-G004: Channel states, signals, scores and bands in both pair orders."""
    mask_a, mask_b = mask_of(*case["inputs"]["gates_a"]), mask_of(*case["inputs"]["gates_b"])
    expected = case["expected"]
    for first, second in ((mask_a, mask_b), (mask_b, mask_a)):
        states = [{"channel_id": c.channel_id, "owner": c.owner, "state": c.state}
                  for c in compute_kernel(first, second, bundle).channels]
        assert states == expected["channel_states"]
        result = calculation.compute_magic10_v2(first, second, bundle, GOLDENS["constants"]["release_id"]).as_payload()
        assert result["schema"] == expected["identities"]["schema"]
        assert result["signals"] == expected["signals"]
        assert result["categories"] == expected["categories"]
    assert expected["ab_ba_identity"] is expected["two_run_identity"] is True


def _owner_mass_q(bundle, owned: list[dict], state: str, signal_id: str, swap: bool = False) -> int:
    base = compute_kernel(1, 2, bundle)
    owners = {row["channel_id"]: (SWAP[row["owner"]] if swap else row["owner"]) for row in owned}
    rows = tuple(ChannelState(c.channel_id, state, owners[c.channel_id]) if c.channel_id in owners
                 else ChannelState(c.channel_id, "none", None) for c in base.channels)
    values = compute_signals(dataclasses.replace(base, channels=rows), bundle)
    return next(value.q for value in values if value.signal_id == signal_id)


def _check_g006(case: dict, bundle) -> None:
    rows = case["expected"]["categories"]
    assert [row["category_id"] for row in rows] == [row["category_id"] for row in case["inputs"]["categories"]]
    for stated, row in zip(case["inputs"]["categories"], rows):
        c1, c2, c3, top = bundle.maxima[row["category_id"]]
        assert row["maxima"] == [c1, c2, c3, top]
        assert stated["scores"] == [c1, c1 + 1, c2, c2 + 1, c3, c3 + 1, top]
        assert [item["score"] for item in row["results"]] == stated["scores"]
        assert [item["band"] for item in row["results"]] == ["Cool", "Open", "Open", "Warm", "Warm", "Glow", "Glow"]
        assert [calculation.assign_band(item["score"], bundle.maxima[row["category_id"]]) for item in row["results"]] == [
            item["band"] for item in row["results"]]


def _compare_over_the_cut_release(monkeypatch):
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)
    return artifacts.compare_goldens(ROOT, GOLDENS_PATH)


def test_goldens_document_holds_m10_g001_to_m10_g008() -> None:
    assert GOLDENS["schema"] == "magic10_goldens.v2"
    assert GOLDENS["source"]["document"] == "PF01-Canon-HDE-Math-Spec"
    assert [case["case_id"] for case in GOLDENS["cases"]] == [f"M10-G00{number}" for number in range(1, 9)]
    assert [case["case_id"] for case in GOLDENS["cases"]] == list(artifacts.GOLDEN_CASE_IDS)
    assert GOLDENS["constants"]["config_id"] == "m10-relevance-centers-type-v2.0.0"
    expected = _case("M10-G001")["expected"]
    assert list(expected) == ["categories"]
    assert {(item["score"], item["band"]) for item in expected["categories"]} == {(0, "Cool")}
    order = json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"]
    assert [item["category_id"] for item in expected["categories"]] == order
    for case_id in ("M10-G002", "M10-G004"):
        assert [item["category_id"] for item in _case(case_id)["expected"]["categories"]] == order


def test_m10_g001_in_both_pair_orders(v2_cut_bundle, mask_of) -> None:
    _check_golden(_case("M10-G001"), v2_cut_bundle, mask_of)


def test_m10_g002_and_m10_g004_in_both_pair_orders(v2_cut_bundle, mask_of) -> None:
    for case_id in ("M10-G002", "M10-G004"):
        _check_core_golden(_case(case_id), v2_cut_bundle, mask_of)
    # M10-G002: both members hold all 64 Gates, so every Channel is companionship.
    assert {(row["state"], row["owner"]) for row in _case("M10-G002")["expected"]["channel_states"]} == {("companionship", None)}


def test_m10_g003_owner_split_with_the_owners_swapped(v2_cut_bundle) -> None:
    case = _case("M10-G003")
    inputs = case["inputs"]
    row = next(r for r in v2_cut_bundle.configuration["signals"] if r["signal_id"] == inputs["signal_id"])
    assert inputs["operation"] == row["operation"] == "bilateral_owner_mass_v2"
    assert inputs["channels"] == [{"channel_id": c["channel_id"], "weight": c["weight"]} for c in row["channels"]]
    for scenario, expected in zip(inputs["scenarios"], case["expected"]["scenarios"]):
        assert expected["scenario_id"] == scenario["scenario_id"]
        q = _owner_mass_q(v2_cut_bundle, scenario["owned"], inputs["state"], inputs["signal_id"])
        swapped = _owner_mass_q(v2_cut_bundle, scenario["owned"], inputs["state"], inputs["signal_id"], swap=True)
        assert (q, swapped) == (expected["q"], expected["q_owners_swapped"]) and q == swapped
    assert [s["q"] for s in case["expected"]["scenarios"]] == [1000, 0, 0]


def test_m10_g006_band_boundaries_at_each_categorys_cut_maxima(v2_cut_bundle) -> None:
    _check_g006(_case("M10-G006"), v2_cut_bundle)


def test_every_golden_matches_the_cut_release_in_both_pair_orders(monkeypatch) -> None:
    result = _compare_over_the_cut_release(monkeypatch)
    assert result.ok is True and result.mismatches == ()
    assert [(row.case_id, row.outcome) for row in result.cases] == [(case_id, "match") for case_id in artifacts.GOLDEN_CASE_IDS]


def test_m10_g001_mutation_changed_band_is_refused(v2_cut_bundle, mask_of) -> None:
    case = copy.deepcopy(_case("M10-G001"))
    case["expected"]["categories"][0]["band"] = "Open"
    with pytest.raises(AssertionError):
        _check_golden(case, v2_cut_bundle, mask_of)


def test_m10_g001_mutation_channel_completing_pair_is_refused(v2_cut_bundle, mask_of) -> None:
    case = copy.deepcopy(_case("M10-G001"))
    case["inputs"]["gates_b"] = [8]  # completes Channel 1-8 with gates_a [1]
    with pytest.raises(AssertionError):
        _check_golden(case, v2_cut_bundle, mask_of)


def test_m10_g004_mutation_changed_score_is_refused(v2_cut_bundle, mask_of) -> None:
    case = copy.deepcopy(_case("M10-G004"))
    case["expected"]["categories"][0]["score"] += 1
    with pytest.raises(AssertionError):
        _check_core_golden(case, v2_cut_bundle, mask_of)


def test_m10_g006_mutation_fixture_maxima_are_refused(v2_bundle, v2_cut_bundle) -> None:
    """The boundary matrix belongs to the cut maxima: the labelled fixture maxima refuse it."""
    assert dict(v2_bundle.maxima) != dict(v2_cut_bundle.maxima)
    with pytest.raises(AssertionError):
        _check_g006(_case("M10-G006"), v2_bundle)


def test_mutation_order_dependent_core_is_refused_as_pair_order(monkeypatch) -> None:
    """A core whose result depends on member order is each Gate-level case's ``pair_order`` mismatch."""
    from engine.core import core as engine_core

    real = engine_core.compute_core

    def order_dependent(member_a, member_b, bundle, release_id):
        result = real(member_a, member_b, bundle, release_id)
        return dataclasses.replace(result, pair_key="0" * 64) if member_a.mask > member_b.mask else result

    monkeypatch.setattr(engine_core, "compute_core", order_dependent)
    result = _compare_over_the_cut_release(monkeypatch)
    assert result.ok is False
    # M10-G002 has equal masks; the application cases normalize the order before the core.
    assert [(row.case_id, row.path) for row in result.mismatches] == [("M10-G001", "pair_order"), ("M10-G004", "pair_order")]
