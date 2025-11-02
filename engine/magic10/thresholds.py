"""Threshold loading and band utilities for Magic-10 scoring."""
from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Tuple

_ROOT = Path(__file__).resolve().parents[2]
_DATA = json.loads((_ROOT / "math" / "thresholds.json").read_text(encoding="utf-8"))

THRESHOLD_EDGES: Tuple[int, ...] = tuple(int(edge) for edge in _DATA["edges"])
_CLAMP_MIN, _CLAMP_MAX = tuple(int(v) for v in _DATA["clamp"])
_ROUNDING_NAME = _DATA.get("rounding", "ROUND_HALF_UP")
if _ROUNDING_NAME != "ROUND_HALF_UP":
    raise ValueError(f"Unsupported rounding mode: {_ROUNDING_NAME}")

BANDS: Tuple[str, ...] = ("Cool", "Open", "Warm", "Glow")
_ONE = Decimal("1")


def clamp_score(value: int) -> int:
    """Clamp a score into the configured inclusive range."""
    if value < _CLAMP_MIN:
        return _CLAMP_MIN
    if value > _CLAMP_MAX:
        return _CLAMP_MAX
    return value


def round_half_up(value: Decimal) -> int:
    """Quantize a decimal to the nearest integer using ROUND_HALF_UP."""
    quantized = value.quantize(_ONE, rounding=ROUND_HALF_UP)
    return int(quantized)


def band_for_score(score: int) -> str:
    """Return the band label for a score based on inclusive-high edges."""
    clamped = clamp_score(score)
    for edge, band in zip(THRESHOLD_EDGES, BANDS):
        if clamped <= edge:
            return band
    return BANDS[-1]
