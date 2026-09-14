"""Integer-only category reduction for the injected Gate kernel."""
from __future__ import annotations

import sys as _sys
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CategoryValue:
    category_id: str
    score: int
    band: str


def _reduce_category(category_id, q_values, bounds, weights) -> CategoryValue:
    if type(category_id) is not str or not category_id:
        raise ValueError("invalid category identity")
    if type(q_values) is not tuple or len(q_values) != 2 or any(
        type(q) is not int or not 0 <= q <= 200 for q in q_values
    ):
        raise ValueError("invalid category inputs")
    if type(weights) is not tuple or len(weights) != 2 or any(
        type(w) is not int or not 1 <= w <= 3 for w in weights
    ):
        raise ValueError("invalid category weights")
    if set(bounds) != {"min", "max"} or any(type(v) is not int for v in bounds.values()):
        raise ValueError("invalid category bounds")
    lower, upper = bounds["min"], bounds["max"]
    if not 0 <= lower <= upper <= 100:
        raise ValueError("invalid category bounds")
    capped = tuple(min(2 * upper, max(2 * lower, q)) for q in q_values)
    total = sum(weights)
    weighted = sum(w * q for w, q in zip(weights, capped))
    score = min(100, max(0, (weighted + total) // (2 * total)))
    band = ("Cool" if score <= 24 else "Open" if score <= 49
            else "Warm" if score <= 74 else "Glow")
    return CategoryValue(category_id, score, band)


# Passive import provenance; validation remains outside the pure mechanics.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None
