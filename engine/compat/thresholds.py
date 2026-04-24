"""Band thresholds (inclusive) sourced from the constants-pack threshold edges."""
from __future__ import annotations

from typing import Dict

from engine.magic10.thresholds import BANDS as _PACK_BANDS
from engine.magic10.thresholds import THRESHOLD_EDGES

if len(THRESHOLD_EDGES) != 4:
    raise ValueError("Expected exactly four threshold edges from constants pack")

THRESHOLDS_V1: Dict[str, int] = {
    "cool_max": int(THRESHOLD_EDGES[0]),
    "open_max": int(THRESHOLD_EDGES[1]),
    "warm_max": int(THRESHOLD_EDGES[2]),
}

BANDS = tuple(_PACK_BANDS)
