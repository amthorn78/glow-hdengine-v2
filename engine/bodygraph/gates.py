"""Pure normalization for public Gate collections.

The accepted boundary is deliberately narrower than Python's general numeric
protocol: callers must provide a non-empty built-in list containing only exact
Gate integers or their canonical ASCII decimal spellings.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


_CANONICAL_GATE_TEXT = re.compile(r"(?:[1-9]|[1-5][0-9]|6[0-4])", re.ASCII)


class GateNormalizationError(ValueError):
    """A value-free, stable refusal from :func:`normalize_gates`."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True, slots=True)
class NormalizedGates:
    gates: tuple[int, ...]
    mask: int
    mask_hex: str


def normalize_gates(value: object) -> NormalizedGates:
    """Return the canonical Gate tuple and its uint64 bit-set representation."""
    if type(value) is not list:
        raise GateNormalizationError("GATES_NOT_LIST")
    if not value:
        raise GateNormalizationError("GATES_EMPTY")

    normalized: list[int] = []
    seen: set[int] = set()
    for item in value:
        if type(item) is int and 1 <= item <= 64:
            gate = item
        elif type(item) is str and _CANONICAL_GATE_TEXT.fullmatch(item) is not None:
            gate = int(item)
        else:
            raise GateNormalizationError("GATE_VALUE_INVALID")
        if gate in seen:
            raise GateNormalizationError("GATE_DUPLICATE")
        seen.add(gate)
        normalized.append(gate)

    gates = tuple(sorted(normalized))
    mask = sum(1 << (gate - 1) for gate in gates)
    return NormalizedGates(gates=gates, mask=mask, mask_hex=f"{mask:016x}")
