import json
from pathlib import Path

import pytest

from engine.magic10 import CATEGORY_INPUTS, calculator_ids

pytestmark = pytest.mark.epic007


def test_calculators_cover_magic10_order():
    order = tuple(json.loads(Path("catalog/magic10.json").read_text(encoding="utf-8"))["order"])
    assert calculator_ids() == order
    assert set(CATEGORY_INPUTS.keys()) == set(order)


def test_compute_requires_known_inputs():
    from engine.magic10 import compute_category

    with pytest.raises(ValueError):
        compute_category("not-real", {})
    # Known category with missing field should raise
    with pytest.raises(ValueError):
        compute_category("harmony", {})
