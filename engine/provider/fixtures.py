from __future__ import annotations
from typing import Any
from .base import PairProfile, Provider

class FixturesProvider:
    """Deterministic fixture-backed provider."""
    def __init__(self, name: str = "fixtures"):
        self._name = name

    def get_pair_profile(self, a: dict[str, Any], b: dict[str, Any], preset: dict[str, Any] | None = None) -> PairProfile:
        # Minimal, deterministic echo for smoke proofs.
        # Never reads clocks/network; order-insensitive AB↔BA set-equality preserved by sorted keys elsewhere.
        return PairProfile(
            source=self._name,
            data={"a_keys": sorted(list(a.keys())), "b_keys": sorted(list(b.keys())), "preset_present": bool(preset)},
        )

# Export typedef for loader isinstance checks if needed
Provider = Provider
