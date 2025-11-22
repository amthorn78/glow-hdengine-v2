from __future__ import annotations

import hashlib
from functools import cmp_to_key
from pathlib import Path
from typing import Callable, Iterable

from engine.config.registry_loader import load_registry_config
from engine.order.comparators import (
    ABBA_CANONICAL_PAIR,
    canonicalize_set,
    compare_categories,
    compare_channels,
    compare_ids,
    compare_sets,
)
from engine.serializer import canon as serializer


def _check_antisymmetry(values: Iterable[str], cmp_func: Callable[[str, str], int]) -> bool:
    for left in values:
        for right in values:
            if cmp_func(left, right) != -(cmp_func(right, left)):
                return False
    return True


def _check_totality(values: Iterable[str], cmp_func: Callable[[str, str], int]) -> bool:
    for left in values:
        for right in values:
            res = cmp_func(left, right)
            if res == 0:
                continue
            if res not in (-1, 1):
                return False
    return True


def _check_transitivity(values: Iterable[str], cmp_func: Callable[[str, str], int]) -> bool:
    ordered = sorted(values, key=cmp_to_key(cmp_func))
    for i, a in enumerate(ordered):
        for b in ordered[i:]:
            for c in ordered[i:]:
                if cmp_func(a, b) <= 0 and cmp_func(b, c) <= 0 and cmp_func(a, c) > 0:
                    return False
    return True


def _total_order_status(values: Iterable[str], cmp_func: Callable[[str, str], int]) -> str:
    antisym = _check_antisymmetry(values, cmp_func)
    total = _check_totality(values, cmp_func)
    trans = _check_transitivity(values, cmp_func)
    if antisym and total and trans:
        return "antisymmetry=ok,totality=ok,transitivity=ok"
    return "antisymmetry=fail,totality=fail,transitivity=fail"


def load_ordering_context(root: Path | None = None) -> dict[str, object]:
    cfg = load_registry_config(root)
    channels = tuple(cfg.channels.keys())
    categories = tuple(cfg.magic10_order)
    return {
        "channels": channels,
        "categories": categories,
        "abba_pair": ABBA_CANONICAL_PAIR,
    }


def channels_sorted(context: dict[str, object]) -> list[str]:
    return sorted(context["channels"], key=cmp_to_key(compare_channels))


def categories_sorted(context: dict[str, object]) -> list[str]:
    return sorted(context["categories"], key=cmp_to_key(compare_categories))


def abba_identity_digest(context: dict[str, object]) -> bytes:
    pair = context["abba_pair"]
    canonical = canonicalize_set(pair, compare_ids)
    payload = {"abba_pair": canonical}
    serialized = serializer.sercanon(payload)
    return hashlib.sha256(serialized).digest()


def props_total_order_lines(context: dict[str, object]) -> list[str]:
    sections = []
    id_values = ["alpha", "bravo", "charlie"]
    sections.append(f"ids:{_total_order_status(id_values, compare_ids)}")
    sections.append(
        f"channels:{_total_order_status(channels_sorted(context), compare_channels)}|count={len(context['channels'])}"
    )
    sections.append(
        f"categories:{_total_order_status(categories_sorted(context), compare_categories)}|count={len(context['categories'])}"
    )
    set_a = {"alpha", "charlie", "bravo"}
    set_b = {"charlie", "bravo"}
    set_cmp = compare_sets(set_a, set_b, cmp_func=compare_ids)
    sections.append(f"sets:cmp(alpha/bravo/charlie_vs_brv/chl)={set_cmp}")
    return sections


def render_json_snapshot(payload: object) -> bytes:
    return serializer.sercanon(payload)


def render_props_log(lines: list[str]) -> bytes:
    body = "\n".join(lines) + "\n"
    return body.encode("utf-8")

