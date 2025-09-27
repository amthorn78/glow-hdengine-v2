from __future__ import annotations
from typing import Any
from .base import PairProfile

class InternalEngineProvider:
    """Deterministic echo for S2 tests; no numerics, stable ordering."""
    def __init__(self, name: str = "internal_engine"):
        self._name = name

    def get_pair_profile(
        self,
        a: dict[str, Any],
        b: dict[str, Any],
        preset: dict[str, Any] | None = None,
    ) -> PairProfile:
        return PairProfile(
            source=self._name,
            data={
                "a_keys": sorted(list(a.keys())),
                "b_keys": sorted(list(b.keys())),
                "preset_present": bool(preset),
            },
        )
