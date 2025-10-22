"""
Canonical compat categories (IDs + order).
Order is normative for emission and tests.
"""
from __future__ import annotations
from typing import Tuple

CATEGORIES_ORDER_V1: Tuple[str, ...] = (
    "heat",
    "harmony",
    "communication",
    "alignment",
    "comfort",
    "consistency",
    "expansion",
    "creativity",
    "drive",
    "balance",
)
CATEGORIES_SET_V1 = set(CATEGORIES_ORDER_V1)
