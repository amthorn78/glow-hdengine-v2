"""Ordering helpers and comparators (EPIC017 — ordering layer).

This package centralizes deterministic comparison helpers for IDs, channels,
categories, and arrays-as-sets. See ``engine/order/comparators.py`` for the
primary implementations.
"""

from .comparators import (
    ABBA_CANONICAL_PAIR,
    canonicalize_set,
    compare_categories,
    compare_channels,
    compare_ids,
    compare_sets,
    normalize_channel_id,
)

__all__ = [
    "ABBA_CANONICAL_PAIR",
    "canonicalize_set",
    "compare_categories",
    "compare_channels",
    "compare_ids",
    "compare_sets",
    "normalize_channel_id",
]
