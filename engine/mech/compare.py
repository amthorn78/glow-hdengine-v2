"""Deterministic comparators for Engine mechanics (EPIC006).
All functions are pure and total. Return -1/0/1 like py3 cmp.
"""

_CENTER_ORDER = ("head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root")
_MAGIC10 = ("harmony","heat","communication","alignment","comfort","consistency","expansion","creativity","drive","balance")

def _cmp(a: str, b: str) -> int:
    return (a > b) - (a < b)

def cmp_ids(a: str, b: str) -> int:
    return _cmp(a, b)

def cmp_centers(a: str, b: str) -> int:
    ia, ib = _CENTER_ORDER.index(a), _CENTER_ORDER.index(b)
    return _cmp(ia, ib)

def cmp_category_by_rank(a: str, b: str) -> int:
    ia, ib = _MAGIC10.index(a), _MAGIC10.index(b)
    return _cmp(ia, ib)

def _normalize_channel(s: str) -> str:
    # Expect NN-NN, ensure zero-pad and min-first
    a, b = s.split("-", 1)
    a = f"{int(a):02d}"; b = f"{int(b):02d}"
    lo, hi = sorted([a, b])
    return f"{lo}-{hi}"

def cmp_channel_minfirst(a: str, b: str) -> int:
    return _cmp(_normalize_channel(a), _normalize_channel(b))
