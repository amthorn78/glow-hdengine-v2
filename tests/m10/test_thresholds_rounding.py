import pytest

from engine.magic10.calculators import _reduce_category

pytestmark = pytest.mark.epic007


@pytest.mark.parametrize("qs,score,band", [
    ((0, 0), 0, "Cool"), ((48, 48), 24, "Cool"), ((48, 50), 25, "Open"),
    ((98, 98), 49, "Open"), ((98, 100), 50, "Warm"),
    ((148, 148), 74, "Warm"), ((148, 150), 75, "Glow"), ((200, 200), 100, "Glow"),
    ((100, 150), 63, "Warm"), ((1, 0), 0, "Cool"), ((1, 1), 1, "Cool"),
])
def test_g006_half_up_boundaries(qs, score, band):
    result = _reduce_category("harmony", qs, {"min": 0, "max": 100}, (1, 1))
    assert (result.score, result.band) == (score, band)


def test_caps_precede_weighted_reduction():
    assert _reduce_category("harmony", (0, 200), {"min": 20, "max": 60}, (1, 3)).score == 50
    assert _reduce_category("harmony", (1, 2), {"min": 0, "max": 100}, (1, 3)).score == 1


@pytest.mark.parametrize("field,bad", [
    ("qs", (True, 0)), ("qs", (0.0, 0)), ("qs", ("0", 0)), ("qs", (-1, 0)),
    ("qs", (201, 0)), ("qs", (0,)), ("qs", (0, 0, 0)), ("qs", [0, 0]),
    ("weights", (True, 1)), ("weights", (1.0, 1)), ("weights", ("1", 1)),
    ("weights", (0, 1)), ("weights", (-1, 1)), ("weights", (4, 1)),
    ("weights", (1,)), ("weights", (1, 1, 1)),
    ("bounds", {"min": True, "max": 100}), ("bounds", {"min": 0, "max": 101}),
    ("bounds", {"min": 60, "max": 50}), ("bounds", {"min": 0}),
    ("bounds", {"min": 0, "max": 100, "extra": 0}),
])
def test_reducer_refuses_coercions_and_invalid_arity(field, bad):
    values = {"qs": (0, 0), "weights": (1, 1), "bounds": {"min": 0, "max": 100}}
    values[field] = bad
    with pytest.raises((ValueError, TypeError)):
        _reduce_category("harmony", values["qs"], values["bounds"], values["weights"])
