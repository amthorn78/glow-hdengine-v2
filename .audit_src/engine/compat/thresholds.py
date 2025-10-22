"""
Band thresholds (inclusive) for EPIC003.
Order of checks: <= cool_max, <= open_max, <= warm_max, else Glow.
A score of 100 always maps to Glow.
"""
from __future__ import annotations
from typing import Dict

THRESHOLDS_V1: Dict[str, int] = {
    "cool_max": 24,
    "open_max": 49,
    "warm_max": 74,
}
BANDS = ("Cool","Open","Warm","Glow")
