"""HDE-EPIC043 WU-PR-01 acceptance 1: the exhaustive channel-state table (HDE-CONJ010.1).

For each of the 36 Channels, every combination of each member's two Gate bits
(four per member, sixteen per Channel) is scored. Both members also hold one pad
Gate that shares no Channel with either endpoint, so every mask is a nonempty
Gate set (HDE Math Spec §5.2.1) and the pad changes no other Channel's state.

The table proves the five states, owner provenance, AB↔BA equality of the whole
output, and equality with the v1 five-state classifier
``engine.magic10.composite._classify_channel`` (HDE Math Spec §5.2.11 step 2;
§6.1). The kernel restates that rule and never imports it; only this test does.

With a shared pad, the member holding both Gates of a Channel always has the
larger mask, so this table shows ``member_hi`` owners only; ``member_lo``
ownership is covered by the constructed pairs of ``test_kernel_mechanics.py``.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import pytest

from engine.magic10.composite import _classify_channel as v1_classify_channel
from engine.magic10_v2.kernel import CHANNEL_STATES, MEMBERS, compute_kernel

ROOT = Path(__file__).resolve().parents[2]
CHANNEL_IDS = tuple(row["id"] for row in json.loads((ROOT / "catalog/channels_v1.json").read_bytes())["channels"])
OWNED_STATES = {"dominance", "compromise"}


def _pad_gate(registry, channel) -> int:
    """The lowest Gate sharing no Channel with either endpoint of ``channel``."""
    near = set(channel.gates)
    for other in registry.channels.values():
        if set(other.gates) & set(channel.gates):
            near |= set(other.gates)
    return min(gate for gate in registry.gates if gate not in near)


def _table(channel, pad: int):
    gate_x, gate_y = channel.gates
    base = 1 << (pad - 1)
    for a_x, a_y, b_x, b_y in itertools.product((0, 1), repeat=4):
        mask_a = base | (a_x << (gate_x - 1)) | (a_y << (gate_y - 1))
        mask_b = base | (b_x << (gate_x - 1)) | (b_y << (gate_y - 1))
        yield mask_a, mask_b


def test_channel_roster_matches_the_bundle(v2_bundle) -> None:
    assert tuple(v2_bundle.registry.channels) == CHANNEL_IDS
    assert len(CHANNEL_IDS) == 36


@pytest.mark.parametrize("channel_id", CHANNEL_IDS)
def test_exhaustive_channel_state_table(v2_bundle, channel_id: str) -> None:
    registry = v2_bundle.registry
    channel = registry.channels[channel_id]
    pad = _pad_gate(registry, channel)
    observed_states = set()
    observed_owners = set()
    for mask_a, mask_b in _table(channel, pad):
        result = compute_kernel(mask_a, mask_b, v2_bundle)
        assert result == compute_kernel(mask_b, mask_a, v2_bundle), (mask_a, mask_b)
        mask_lo, mask_hi = sorted((mask_a, mask_b))
        for entry, row in zip(result.channels, registry.channels.values(), strict=True):
            expected = v1_classify_channel(row.id, row.gates, mask_lo, mask_hi)
            assert (entry.channel_id, entry.state, entry.owner) == (expected.channel_id, expected.state, expected.owner)
            assert (entry.owner is not None) == (entry.state in OWNED_STATES)
        own = next(entry for entry in result.channels if entry.channel_id == channel_id)
        observed_states.add(own.state)
        if own.owner is not None:
            observed_owners.add((own.state, own.owner))
    assert observed_states == set(CHANNEL_STATES)
    assert observed_owners == {("dominance", "member_hi"), ("compromise", "member_hi")}


def test_channel_states_shape(v2_bundle, mask_of) -> None:
    result = compute_kernel(mask_of(1, 8, 20), mask_of(8, 34, 57), v2_bundle)
    assert tuple(entry.channel_id for entry in result.channels) == CHANNEL_IDS
    assert all(entry.state in CHANNEL_STATES for entry in result.channels)
    assert all(entry.owner is None or entry.owner in MEMBERS for entry in result.channels)
