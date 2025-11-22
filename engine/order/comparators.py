"""Deterministic comparators for the ordering layer (EPIC017).

Discovery notes (Phase 1):
- Legacy helpers live in ``engine.mech.compare`` and ``engine.mech.helpers``
  (ID, category-by-rank, channel min-first, and ASCII set sorting).
- Observable ordering today: registry loader normalizes channels to ``NN-NN``,
  categories follow the frozen Magic-10 order, and artifacts/tests such as
  ``tests/mech/test_order_properties.py`` and registry outputs rely on
  deterministic iteration.
- This module extends that surface with set canonicalization and explicit
  comparators to back the ordering artifacts under ``artifacts/engine/order``
  and the new tests under ``tests/order``.
"""

from __future__ import annotations

from functools import cmp_to_key
from typing import Callable, Iterable

from engine.categories.registry import FROZEN_MAGIC10_ORDER


def _cmp(a, b) -> int:
    return (a > b) - (a < b)


def compare_ids(a: str, b: str) -> int:
    """ASCII lexicographic comparison for IDs."""

    return _cmp(a, b)


def normalize_channel_id(channel_id: str) -> str:
    """Normalize a channel identifier to ``NN-NN`` with the lower gate first."""

    parts = channel_id.split("-", 1)
    if len(parts) != 2:
        raise ValueError(f"invalid channel id: {channel_id}")
    lhs, rhs = parts
    try:
        a = f"{int(lhs):02d}"
        b = f"{int(rhs):02d}"
    except ValueError as exc:  # pragma: no cover - defensive
        raise ValueError(f"invalid channel id: {channel_id}") from exc
    lo, hi = sorted([a, b])
    return f"{lo}-{hi}"


def compare_channels(a: str, b: str) -> int:
    """Compare two channel identifiers after canonical normalization."""

    return _cmp(normalize_channel_id(a), normalize_channel_id(b))


_MAGIC10_INDEX = {cid: idx for idx, cid in enumerate(FROZEN_MAGIC10_ORDER)}


def _category_rank(category_id: str) -> tuple[int, str]:
    return (_MAGIC10_INDEX.get(category_id, len(_MAGIC10_INDEX)), category_id)


def compare_categories(a: str, b: str) -> int:
    """Compare categories by Magic-10 rank, then by ID as tie-breaker."""

    return _cmp(_category_rank(a), _category_rank(b))


def canonicalize_set(values: Iterable[str], cmp_func: Callable[[str, str], int]) -> list[str]:
    """Deduplicate and deterministically order an iterable using ``cmp_func``."""

    deduped = {v for v in values}
    return sorted(deduped, key=cmp_to_key(cmp_func))


def compare_sets(
    a: Iterable[str], b: Iterable[str], cmp_func: Callable[[str, str], int] = compare_ids
) -> int:
    """Compare two array-as-set collections using a comparator for their elements."""

    canon_a = canonicalize_set(a, cmp_func)
    canon_b = canonicalize_set(b, cmp_func)
    for left, right in zip(canon_a, canon_b):
        step = cmp_func(left, right)
        if step:
            return step
    return _cmp(len(canon_a), len(canon_b))


ABBA_CANONICAL_PAIR: tuple[str, str] = ("alpha", "bravo")

