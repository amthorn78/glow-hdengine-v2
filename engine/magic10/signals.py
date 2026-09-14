"""Injected integer signal operations; no catalog or calculator registry."""
from __future__ import annotations

from dataclasses import dataclass

from .composite import ChannelClassification


_STATES = frozenset(("none", "companionship", "compromise", "dominance", "electromagnetic"))


@dataclass(frozen=True, slots=True)
class SignalValue:
    signal_id: str
    q: int


def _signal_q(operation, channels, classifications, responses=None) -> int:
    """Round once after the complete weighted sum, in half-score units."""
    if type(channels) is not tuple or not 1 <= len(channels) <= 6:
        raise ValueError("invalid signal members")
    if operation == "weighted_state_sum_v1":
        if responses is None or set(responses) != _STATES or any(
            type(v) is not int or not 0 <= v <= 10000 for v in responses.values()
        ):
            raise ValueError("invalid response profile")
    elif operation not in ("twice_min_owner_mass_v1", "companionship_em_mass_v1") or responses is not None:
        raise ValueError("invalid signal operation")
    seen = []
    total = numerator = lo_mass = hi_mass = matching_mass = 0
    for member in channels:
        if set(member) != {"channel_id", "weight"}:
            raise ValueError("invalid signal member")
        channel_id, weight = member["channel_id"], member["weight"]
        if type(channel_id) is not str or channel_id not in classifications:
            raise ValueError("unknown signal channel")
        if type(weight) is not int or not 1 <= weight <= 3:
            raise ValueError("invalid signal weight")
        row = classifications[channel_id]
        if type(row) is not ChannelClassification or row.channel_id != channel_id or row.state not in _STATES:
            raise ValueError("invalid channel state")
        if row.state in ("dominance", "compromise"):
            if row.owner not in ("member_lo", "member_hi"):
                raise ValueError("invalid channel owner")
        elif row.owner is not None:
            raise ValueError("unexpected channel owner")
        seen.append(channel_id)
        total += weight
        if operation == "weighted_state_sum_v1":
            numerator += weight * responses[row.state]
        if row.owner == "member_lo":
            lo_mass += weight
        elif row.owner == "member_hi":
            hi_mass += weight
        if row.state in ("companionship", "electromagnetic"):
            matching_mass += weight
    if seen != sorted(set(seen)):
        raise ValueError("invalid signal channel order")
    if operation == "weighted_state_sum_v1":
        q = (numerator + 25 * total) // (50 * total)
    elif operation == "twice_min_owner_mass_v1":
        q = (800 * min(lo_mass, hi_mass) + total) // (2 * total)
    else:
        q = (400 * matching_mass + total) // (2 * total)
    if not 0 <= q <= 200:
        raise ValueError("invalid signal result")
    return q


def _compute_signals(classified, mechanics, expected_order) -> tuple[SignalValue, ...]:
    if len(classified) != 36 or len({row.channel_id for row in classified}) != 36:
        raise ValueError("incomplete channel states")
    states = {row.channel_id: row for row in classified}
    profiles = {}
    profile_orders = (
        ("activation_bp_v1", ("electromagnetic", "dominance", "companionship", "compromise", "none")),
        ("coherence_bp_v1", ("companionship", "electromagnetic", "dominance", "compromise", "none")),
        ("expression_bp_v1", ("electromagnetic", "companionship", "dominance", "compromise", "none")),
    )
    if tuple(row["profile_id"] for row in mechanics["profiles"]) != tuple(name for name, _ in profile_orders):
        raise ValueError("invalid profile roster")
    for row, (_, order) in zip(mechanics["profiles"], profile_orders):
        if set(row) != {"profile_id", "responses"} or set(row["responses"]) != _STATES:
            raise ValueError("invalid profile fields")
        responses = row["responses"]
        if any(type(v) is not int or not 0 <= v <= 10000 for v in responses.values()):
            raise ValueError("invalid response domain")
        if any(responses[a] <= responses[b] for a, b in zip(order, order[1:])):
            raise ValueError("invalid response ordering")
        profiles[row["profile_id"]] = responses
    rows = mechanics["signals"]
    if len(rows) != 20 or tuple(row["signal_id"] for row in rows) != expected_order:
        raise ValueError("invalid signal order")
    values = []
    used = set()
    for index, row in enumerate(rows):
        fields = {"signal_id", "operation", "channels"}
        if index < 18:
            fields.add("profile_id")
            if row["operation"] != "weighted_state_sum_v1" or row["profile_id"] not in profiles:
                raise ValueError("invalid ordinary operation")
            responses = profiles[row["profile_id"]]
        else:
            expected = ("twice_min_owner_mass_v1", "companionship_em_mass_v1")[index - 18]
            if row["operation"] != expected:
                raise ValueError("invalid Balance operation")
            responses = None
        if set(row) != fields:
            raise ValueError("invalid signal fields")
        q = _signal_q(row["operation"], row["channels"], states, responses)
        members = {member["channel_id"] for member in row["channels"]}
        if index % 2 and members & previous:
            raise ValueError("overlapping category signals")
        previous = members
        used.update(members)
        values.append(SignalValue(row["signal_id"], q))
    if used != set(states):
        raise ValueError("incomplete signal topology")
    return tuple(values)
