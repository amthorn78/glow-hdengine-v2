from __future__ import annotations

import itertools
from functools import cmp_to_key

from engine.order.comparators import (
    ABBA_CANONICAL_PAIR,
    canonicalize_set,
    compare_categories,
    compare_channels,
    compare_ids,
    compare_sets,
    normalize_channel_id,
)


def _assert_total_order(values, cmp_func):
    for a, b in itertools.product(values, repeat=2):
        assert cmp_func(a, b) == -(cmp_func(b, a))
    ordered = sorted(values, key=cmp_to_key(cmp_func))
    for a, b, c in itertools.product(ordered, repeat=3):
        if cmp_func(a, b) <= 0 and cmp_func(b, c) <= 0:
            assert cmp_func(a, c) <= 0


def test_compare_ids_total_order():
    values = ["alpha", "bravo", "charlie"]
    _assert_total_order(values, compare_ids)


def test_compare_channels_normalizes_and_orders():
    values = ["20-34", "34-20", "01-09", "09-01", "05-05"]
    normalized = [normalize_channel_id(v) for v in values]
    assert normalized == ["20-34", "20-34", "01-09", "01-09", "05-05"]
    _assert_total_order(values, compare_channels)


def test_compare_categories_uses_magic10_order():
    values = ["balance", "alignment", "harmony", "drive"]
    ordered = sorted(values, key=cmp_to_key(compare_categories))
    assert ordered == ["harmony", "alignment", "drive", "balance"]
    _assert_total_order(values, compare_categories)


def test_canonicalize_set_and_compare_sets():
    original = ["bravo", "alpha", "alpha", "charlie"]
    assert canonicalize_set(original, compare_ids) == ["alpha", "bravo", "charlie"]
    larger = ["alpha", "bravo", "charlie"]
    smaller = ["bravo", "charlie"]
    cmp_val = compare_sets(larger, smaller, cmp_func=compare_ids)
    assert cmp_val == -compare_sets(smaller, larger, cmp_func=compare_ids)
    assert cmp_val != 0


def test_abba_identity_pair_is_stable():
    forward = compare_sets(ABBA_CANONICAL_PAIR, reversed(ABBA_CANONICAL_PAIR), cmp_func=compare_ids)
    assert forward == 0
