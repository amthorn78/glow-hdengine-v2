from pathlib import Path

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.core import compute_core
from engine import magic10
from engine.magic10 import calculators
from tests.config.helpers import synthetic_complete_release_root

pytestmark = pytest.mark.epic007


def test_injected_bundle_closes_category_and_signal_order(tmp_path):
    bundle = _load_active_mechanics_bundle_from_root(synthetic_complete_release_root(tmp_path))
    a = normalize_gates([1])
    result = compute_core(a, a, bundle, bundle.release_id)
    assert tuple(r.category_id for r in result.categories) == bundle.registry.magic10_order
    assert tuple(r.signal_id for r in result.signals) == tuple(
        s for category in bundle.registry.magic10_order for s in bundle.registry.magic10_caps[category].inputs
    )


def test_transitional_registry_and_exports_are_removed():
    for name in ("CATEGORY_INPUTS", "compute_category", "calculator_ids", "Magic10Calculator", "_CALCULATORS"):
        assert not hasattr(calculators, name)
        assert not hasattr(magic10, name)
    source = (Path(__file__).resolve().parents[2] / "engine/magic10/calculators.py").read_text()
    assert "Decimal" not in source and "read_text" not in source
