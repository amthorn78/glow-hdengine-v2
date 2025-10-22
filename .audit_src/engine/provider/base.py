from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class PairProfile:
    """Deterministic DTO returned by providers."""
    source: str               # which provider produced this
    data: dict[str, Any]      # stable, JSON-serializable payload

class Provider(Protocol):
    def get_pair_profile(self, a: dict[str, Any], b: dict[str, Any], preset: dict[str, Any] | None = None) -> PairProfile: ...
