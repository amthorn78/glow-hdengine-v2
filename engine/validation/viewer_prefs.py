from __future__ import annotations
from typing import Dict
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.categories import CATEGORIES_SET_V1
from engine.compat.errors import error_envelope

def validate_viewer_prefs(prefs: Dict[str, object]) -> Dict[str, object] | None:
    if not isinstance(prefs, dict): return error_envelope("invalid_prefs")
    top = prefs.get("top_category")
    weights = prefs.get("weights")
    if not isinstance(top, str) or top not in CATEGORIES_SET_V1:
        return error_envelope("invalid_prefs")
    if not isinstance(weights, dict) or set(weights.keys()) != CATEGORIES_SET_V1:
        return error_envelope("invalid_prefs")
    for k,v in weights.items():
        if not isinstance(v, int): return error_envelope("invalid_prefs")
        if v < 0 or v > 100: return error_envelope("invalid_prefs")
    return None  # OK


def normalize_viewer_prefs(prefs: Dict[str, object]) -> Dict[str, object]:
    """Return canonical viewer prefs after validation.

    - Keeps existing viewer preference semantics unchanged.
    - Preserves explicit zero weights so downstream sampler/ranker ownership
      of zero-weight exclusion remains the single behavior home.
    """

    weights = prefs["weights"]
    assert isinstance(weights, dict)  # validated by validate_viewer_prefs
    return {
        "top_category": prefs["top_category"],
        "weights": {category: int(weights[category]) for category in CATEGORIES_ORDER_V1},
    }


def weight_for_candidate_top_category(
    normalized_prefs: Dict[str, object],
    candidate_top_category: str,
) -> float:
    """Project normalized viewer preferences into sampler candidate weight.

    This is the normalization-side handoff point for zero-weight intent; the
    sampler remains the behavior owner for exclusion when weight <= 0.
    """

    weights = normalized_prefs.get("weights")
    if not isinstance(weights, dict):
        raise ValueError("INVALID_NORMALIZED_PREFS")
    if candidate_top_category not in CATEGORIES_SET_V1:
        raise ValueError("INVALID_CANDIDATE_TOP_CATEGORY")
    value = weights.get(candidate_top_category)
    if not isinstance(value, int):
        raise ValueError("INVALID_NORMALIZED_PREFS")
    return float(value)
