"""Deterministic comparators for Engine mechanics (EPIC006).
All functions are pure and total. Return -1/0/1 like py3 cmp.

Legacy aliases now delegate to the ordering layer in ``engine.order``.
"""

from engine.order import (
    compare_categories as cmp_category_by_rank,
    compare_channels as cmp_channel_minfirst,
    compare_ids as cmp_ids,
    normalize_channel_id as _normalize_channel,
)

_CENTER_ORDER = ("head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root")

def cmp_centers(a: str, b: str) -> int:
    ia, ib = _CENTER_ORDER.index(a), _CENTER_ORDER.index(b)
    return (ia > ib) - (ia < ib)
