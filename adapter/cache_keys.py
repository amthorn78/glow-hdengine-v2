from __future__ import annotations
from typing import Tuple

def _orient(u1: str, u2: str, f1: str, f2: str) -> Tuple[str, str, str, str]:
    """Return (min_user, max_user, fp_min, fp_max) keeping fp with its user."""
    if u1 <= u2:
        return u1, u2, f1, f2
    return u2, u1, f2, f1

def build_cache_key(userA_id: str, userB_id: str, release_id: str, fpA: str, fpB: str) -> Tuple[str, str, str, str, str]:
    """
    Orientation-safe cache key:
      (min_user, max_user, release_id, fp_min, fp_max)
    AB and BA produce the same tuple; fingerprints follow the oriented users.
    """
    u_min, u_max, fp_min, fp_max = _orient(userA_id, userB_id, fpA, fpB)
    return (u_min, u_max, release_id, fp_min, fp_max)
