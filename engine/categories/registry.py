"""Category registry with frozen Magic-10 order (EPIC006)."""
import sys as _sys
from typing import Callable, Dict, Tuple

# Passive, immutable top-level execution provenance for active admission.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None

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
