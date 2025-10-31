"""Category registry with frozen Magic-10 order (EPIC006)."""
from typing import Callable, Dict, Tuple

FROZEN_MAGIC10_ORDER = ("harmony","heat","communication","alignment","comfort","consistency","expansion","creativity","drive","balance")
_REG: Dict[str, Callable] = {}

def register(id: str, fn: Callable) -> None:
    if id not in FROZEN_MAGIC10_ORDER:
        raise ValueError(f"Unknown category id: {id}")
    _REG[id] = fn

def get_rank(id: str) -> int:
    return FROZEN_MAGIC10_ORDER.index(id)

def all_ids() -> Tuple[str, ...]:
    return FROZEN_MAGIC10_ORDER
