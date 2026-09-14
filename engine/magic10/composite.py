"""Single five-state Channel classification over intrinsic Gate masks."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ChannelClassification:
    channel_id: str
    state: str
    owner: str | None


def _classify_channel(channel_id: str, gates: tuple[int, int],
                      mask_lo: int, mask_hi: int) -> ChannelClassification:
    """The caller supplies validated topology and numerically ordered masks."""
    x, y = (1 << (gate - 1) for gate in gates)
    lo = bool(mask_lo & x) + bool(mask_lo & y)
    hi = bool(mask_hi & x) + bool(mask_hi & y)
    owner = None
    if lo == hi == 2:
        state = "companionship"
    elif lo == 2 or hi == 2:
        state = "compromise" if min(lo, hi) == 1 else "dominance"
        owner = "member_lo" if lo == 2 else "member_hi"
    elif lo == hi == 1 and bool(mask_lo & x) != bool(mask_hi & x):
        state = "electromagnetic"
    else:
        state = "none"
    return ChannelClassification(channel_id, state, owner)


def _classify_channels(mask_a: int, mask_b: int, channels) -> tuple[ChannelClassification, ...]:
    mask_lo, mask_hi = sorted((mask_a, mask_b))
    return tuple(_classify_channel(row.id, row.gates, mask_lo, mask_hi)
                 for row in channels.values())
