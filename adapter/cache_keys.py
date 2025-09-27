from __future__ import annotations
from typing import Tuple

def reader_cache_key(user_a: str, user_b: str, release_id: str, fpA: str, fpB: str) -> Tuple[str,str,str,str,str]:
    """Orientation-safe cache key:
       - min,max by user id so AB == BA
       - include release_id and both fingerprints
    """
    lo, hi = (user_a, user_b) if user_a <= user_b else (user_b, user_a)
    return (lo, hi, release_id, fpA, fpB)
