import pytest

from engine.magic10 import CATEGORY_INPUTS, compute_category

pytestmark = pytest.mark.epic007


def _payload(category: str, values) -> dict:
    keys = CATEGORY_INPUTS[category]
    assert len(keys) == len(values)
    return dict(zip(keys, values))


@pytest.mark.parametrize(
    "values,expected_score,expected_band",
    [
        ((-10, 0), 0, "Cool"),
        ((1, 1), 1, "Cool"),
        ((24, 24), 24, "Cool"),
        ((24, 25), 25, "Open"),
        ((49, 49), 49, "Open"),
        ((49, 50), 50, "Warm"),
        ((74, 74), 74, "Warm"),
        ((74, 75), 75, "Glow"),
        ((120, 120), 100, "Glow"),
    ],
)
def test_thresholds_rounding_and_bands(values, expected_score, expected_band):
    result = compute_category("harmony", _payload("harmony", values))
    assert result.score == expected_score
    assert result.band == expected_band


def test_out_of_range_inputs_are_clamped():
    result = compute_category(
        "harmony",
        _payload("harmony", (-50, 250)),
    )
    assert result.score == 50
    assert result.band == "Warm"
