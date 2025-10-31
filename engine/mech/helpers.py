"""Helpers for canonical ordering and arrays-as-sets (EPIC006)."""
from typing import Callable

def dedupe_sort(seq: list[str]) -> list[str]:
    # ASCII order + stable set
    return sorted(set(seq))

def canonicalize_array(seq: list[str]) -> list[str]:
    return dedupe_sort(seq)

def sort_pairs(a: tuple[str,str], b: tuple[str,str]) -> int:
    # Pair lexical cmp
    return (a > b) - (a < b)

def ensure_total_order(items: list[str], cmp: Callable[[str,str], int]) -> list[str]:
    return sorted(items, key=lambda x: x)  # deterministic baseline; public paths must use domain cmp upstream
