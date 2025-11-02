import pytest

from engine.magic10 import CATEGORY_INPUTS, calculator_ids, compute_category

pytestmark = pytest.mark.epic007


_PAIR_VALUES = {
    "harmony": (41, 79),
    "heat": (24, 75),
    "communication": (36, 58),
    "alignment": (88, 12),
    "comfort": (67, 43),
    "consistency": (52, 49),
    "expansion": (90, 18),
    "creativity": (72, 51),
    "drive": (83, 45),
    "balance": (64, 40),
}


def _payload_from_pairs(reverse: bool = False) -> dict:
    payload = {}
    for category in calculator_ids():
        inputs = CATEGORY_INPUTS[category]
        first, second = _PAIR_VALUES[category]
        if reverse:
            first, second = second, first
        for key, value in zip(inputs, (first, second)):
            payload[key] = value
    return payload


def _magic10_summary(payload: dict) -> dict:
    summary = {}
    for category in calculator_ids():
        result = compute_category(category, payload)
        summary[category] = {"score": result.score, "band": result.band}
    return summary


def test_magic10_ab_ba_symmetry():
    forward_payload = _payload_from_pairs(reverse=False)
    reverse_payload = _payload_from_pairs(reverse=True)

    summary_ab = _magic10_summary(forward_payload)
    summary_ba = _magic10_summary(reverse_payload)

    assert summary_ab == summary_ba


def test_magic10_two_run_identity():
    payload = _payload_from_pairs(reverse=False)

    first_run = _magic10_summary(payload)
    second_run = _magic10_summary(dict(payload))

    assert first_run == second_run
