"""HDE-EPIC043 WU-PR-04: the v2 proof family, the v2 goldens (HDE-DIST008.1, item F-10).

HDE Math Spec §9.5: the v2 goldens ``M10-G001`` to ``M10-G008`` are checked in
both pair orders. ``M10-G001`` (no Channel, two Reflectors) is fixed: every
category scores ``0``, band Cool. The values of ``M10-G002`` to ``M10-G008`` are
not canon until the v2 change computes them at the cut (WU-PR-10), so
``tests/fixtures/magic10/v2/goldens.json`` holds ``M10-G001`` only, and only its
canon-fixed categories: it carries no computed value and no maxima.

Score 0 is Cool under any admitted maxima, since every first maximum is at
least 0, so the case holds over the labelled non-canon fixture bundle and over
the cut maxima alike. The refused mutations change the case, not the code: an
expected band, and an input pair that completes a Channel.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from engine.magic10_v2 import calculation
from engine.magic10_v2.kernel import compute_kernel

ROOT = Path(__file__).resolve().parents[2]
GOLDENS_PATH = ROOT / "tests" / "fixtures" / "magic10" / "v2" / "goldens.json"
GOLDENS = json.loads(GOLDENS_PATH.read_bytes())


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


def test_goldens_document_holds_m10_g001_only() -> None:
    assert GOLDENS["schema"] == "magic10_goldens.v2"
    assert GOLDENS["source"]["document"] == "PF01-Canon-HDE-Math-Spec"
    assert [case["case_id"] for case in GOLDENS["cases"]] == ["M10-G001"]
    assert GOLDENS["constants"]["config_id"] == "m10-relevance-centers-type-v2.0.0"
    expected = _case("M10-G001")["expected"]
    assert list(expected) == ["categories"]
    assert {(item["score"], item["band"]) for item in expected["categories"]} == {(0, "Cool")}
    order = json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"]
    assert [item["category_id"] for item in expected["categories"]] == order


def test_m10_g001_in_both_pair_orders(v2_bundle, mask_of) -> None:
    _check_golden(_case("M10-G001"), v2_bundle, mask_of)


def test_m10_g001_mutation_changed_band_is_refused(v2_bundle, mask_of) -> None:
    case = copy.deepcopy(_case("M10-G001"))
    case["expected"]["categories"][0]["band"] = "Open"
    with pytest.raises(AssertionError):
        _check_golden(case, v2_bundle, mask_of)


def test_m10_g001_mutation_channel_completing_pair_is_refused(v2_bundle, mask_of) -> None:
    case = copy.deepcopy(_case("M10-G001"))
    case["inputs"]["gates_b"] = [8]  # completes Channel 1-8 with gates_a [1]
    with pytest.raises(AssertionError):
        _check_golden(case, v2_bundle, mask_of)
