"""Magic-10 calculator registry and deterministic scoring helpers."""
from __future__ import annotations

import json
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Callable, Dict, Mapping, NamedTuple, Tuple

from engine.categories.registry import FROZEN_MAGIC10_ORDER, register

from .thresholds import band_for_score, clamp_score, round_half_up

ROOT = Path(__file__).resolve().parents[2]
_CAPS_DATA = json.loads((ROOT / "catalog" / "magic10_caps.json").read_text(encoding="utf-8"))
_ORDER_DATA = tuple(json.loads((ROOT / "catalog" / "magic10.json").read_text(encoding="utf-8"))["order"])

if _ORDER_DATA != FROZEN_MAGIC10_ORDER:
    raise ValueError("Magic-10 order mismatch between catalog pack and registry")
if set(_CAPS_DATA.keys()) != set(_ORDER_DATA):
    raise ValueError("Magic-10 caps do not cover the full category order")

CATEGORY_INPUTS: Dict[str, Tuple[str, ...]] = {
    category: tuple(_CAPS_DATA[category]["inputs"]) for category in _ORDER_DATA
}


class Magic10Result(NamedTuple):
    score: int
    band: str


Magic10Calculator = Callable[[Mapping[str, object]], Magic10Result]
_CALCULATORS: Dict[str, Magic10Calculator] = {}


def _to_decimal(value: object) -> Decimal:
    if isinstance(value, Decimal):
        return value
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"Unsupported input value: {value!r}") from exc


def _clamp_decimal(value: Decimal, lower: Decimal, upper: Decimal) -> Decimal:
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value


def _score_for(category: str, payload: Mapping[str, object]) -> int:
    if category not in CATEGORY_INPUTS:
        raise ValueError(f"Unknown category id: {category}")
    inputs = CATEGORY_INPUTS[category]
    bounds = _CAPS_DATA[category]["bounds"]
    lower = Decimal(bounds["min"])
    upper = Decimal(bounds["max"])
    values = []
    for key in inputs:
        if key not in payload:
            raise ValueError(f"Missing input '{key}' for category '{category}'")
        values.append(_clamp_decimal(_to_decimal(payload[key]), lower, upper))
    total = sum(values, start=Decimal("0"))
    average = total / Decimal(len(values))
    rounded = round_half_up(average)
    return clamp_score(rounded)


def _make_calculator(category: str) -> Magic10Calculator:
    def _calculator(payload: Mapping[str, object]) -> Magic10Result:
        score = _score_for(category, payload)
        return Magic10Result(score=score, band=band_for_score(score))

    return _calculator


for category in FROZEN_MAGIC10_ORDER:
    calculator = _make_calculator(category)
    _CALCULATORS[category] = calculator
    register(category, calculator)


def compute_category(category: str, payload: Mapping[str, object]) -> Magic10Result:
    try:
        calculator = _CALCULATORS[category]
    except KeyError as exc:
        raise ValueError(f"Unknown category id: {category}") from exc
    return calculator(payload)


def calculator_ids() -> Tuple[str, ...]:
    return tuple(_CALCULATORS.keys())
