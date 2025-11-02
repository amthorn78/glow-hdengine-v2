"""Magic-10 calculators and band utilities."""
from .calculators import Magic10Result, compute_category, calculator_ids, CATEGORY_INPUTS
from .thresholds import band_for_score, clamp_score, THRESHOLD_EDGES, BANDS

__all__ = [
    "Magic10Result",
    "compute_category",
    "calculator_ids",
    "CATEGORY_INPUTS",
    "band_for_score",
    "clamp_score",
    "THRESHOLD_EDGES",
    "BANDS",
]
