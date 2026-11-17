"""HDE-EPIC043 WU-PR-04: the v2 proof family, kernel items (HDE Build Checklist — Distillation, HDE-DIST008.1).

Items F-01 (member and union mechanics, Type from the Gate set only), F-02 (the
four center outcomes on every center, and motor→Throat), F-11 and F-12 (the
five-state truth table over all 36 Channels) and F-14 (Gate normalization).
Each item has a check function that raises ``AssertionError`` when the rule it
proves is broken; the passing case runs it on the landed kernel, and the
refused mutation patches one rule in-process and shows the same check fails.
The mutations are constructed perturbations of a rule, not inputs.

Expectations are transcribed from HDE Math Spec §5.2.11 and the governed
topology (``catalog/channels_v1.json``), not read back from the module under
test. The bundle is the labelled non-canon fixture bundle of ``conftest.py``;
no maxima value is asserted. Nothing is written under the repository's tree.
"""
from __future__ import annotations

import dataclasses
import itertools

import pytest

from engine.bodygraph.gates import GateNormalizationError, normalize_gates
from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2 import kernel

CENTER_ORDER = ("ajna", "ego", "g", "head", "root", "sacral", "solar_plexus", "spleen", "throat")
OUTCOMES = ("open", "shared", "one_sided", "mutual")
STATES = ("none", "companionship", "dominance", "compromise", "electromagnetic")

# F-01: (Gates of A, derived Type, aura class, motor_to_throat, complete Channels, defined centers).
# B is the single Gate {2}, a Reflector, and no case completes a Channel with it.
MEMBER_CASES = (
    ((1,), "Reflector", "reflector", False, (), ()),
    ((1, 8), "Projector", "projector", False, ("01-08",), ("g", "throat")),
    ((20, 34), "Manifesting Generator", "generator", True, ("20-34",), ("sacral", "throat")),
    ((1, 8, 3, 60), "Generator", "generator", False, ("01-08", "03-60"), ("g", "root", "sacral", "throat")),
    ((21, 45), "Manifestor", "manifestor", True, ("21-45",), ("ego", "throat")),
    ((20, 57, 32, 54), "Manifestor", "manifestor", True, ("20-57", "32-54"), ("root", "spleen", "throat")),
)

# F-02: one witness Channel per center, as measured in the WU-PR-04 plan (M-6). One member
# holding both Gates defines the center (one_sided); both holding both (shared); each holding one
# (mutual, the union completes it). The single Gates 2 and 64 complete nothing with these.
WITNESSES = {
    "ajna": (4, 63), "ego": (21, 45), "g": (1, 8), "head": (4, 63), "root": (3, 60),
    "sacral": (2, 14), "solar_plexus": (6, 59), "spleen": (10, 57), "throat": (1, 8),
}


def _mask(*gates: int) -> int:
    return normalize_gates(list(gates)).mask


def _both(bundle, mask_a: int, mask_b: int):
    result = kernel.compute_kernel(mask_a, mask_b, bundle)
    assert result == kernel.compute_kernel(mask_b, mask_a, bundle)
    return result


def _member_of(result, mask_a: int, mask_b: int):
    return result.member_lo if mask_a <= mask_b else result.member_hi


# --- F-01 -------------------------------------------------------------------------------------

def _check_f01(bundle) -> None:
    other = _mask(2)
    for gates, derived_type, aura_class, motor_to_throat, complete, defined in MEMBER_CASES:
        mask = _mask(*gates)
        member = _member_of(_both(bundle, mask, other), mask, other)
        assert (member.derived_type, member.aura_class) == (derived_type, aura_class), gates
        assert member.motor_to_throat is motor_to_throat, gates
        assert (member.complete_channels, member.defined_centers) == (complete, defined), gates
    union = _both(bundle, _mask(1, 20), _mask(8, 34)).union
    assert (union.defined_centers, union.motor_to_throat) == (("g", "sacral", "throat"), True)


def test_f01_member_and_union_mechanics(v2_bundle) -> None:
    _check_f01(v2_bundle)


def test_f01_mutation_aura_class_is_refused(v2_bundle, monkeypatch) -> None:
    mutated = dict(kernel.AURA_CLASS_BY_TYPE, Generator="projector")
    monkeypatch.setattr(kernel, "AURA_CLASS_BY_TYPE", mutated)
    with pytest.raises(AssertionError):
        _check_f01(v2_bundle)


def test_f01_mutation_motor_to_throat_route_is_refused(v2_bundle, monkeypatch) -> None:
    original = kernel._mask_mechanics

    def without_route(*args, **kwargs):
        return dataclasses.replace(original(*args, **kwargs), motor_to_throat=False)

    monkeypatch.setattr(kernel, "_mask_mechanics", without_route)
    with pytest.raises(AssertionError):
        _check_f01(v2_bundle)


# --- F-02 -------------------------------------------------------------------------------------

def _outcome_of(result, center: str) -> tuple[str, str | None]:
    found = {item.center_id: (item.outcome, item.owner) for item in result.centers}
    assert tuple(found) == CENTER_ORDER
    return found[center]


def _check_f02(bundle, center: str) -> set[tuple[str, str | None]]:
    gate_x, gate_y = WITNESSES[center]
    seen = set()
    assert _outcome_of(_both(bundle, _mask(1), _mask(2)), center) == ("open", None)
    seen.add(("open", None))
    holder = _mask(gate_x, gate_y)
    for single in (2, 64):
        if single in (gate_x, gate_y):
            single = 1 if single == 2 else 63
        other = _mask(single)
        expected_owner = "member_lo" if holder < other else "member_hi"
        assert _outcome_of(_both(bundle, holder, other), center) == ("one_sided", expected_owner)
        seen.add(("one_sided", expected_owner))
    assert _outcome_of(_both(bundle, holder, holder), center) == ("shared", None)
    seen.add(("shared", None))
    assert _outcome_of(_both(bundle, _mask(gate_x), _mask(gate_y)), center) == ("mutual", None)
    seen.add(("mutual", None))
    return seen


@pytest.mark.parametrize("center", CENTER_ORDER)
def test_f02_every_outcome_on_every_center(v2_bundle, center) -> None:
    seen = _check_f02(v2_bundle, center)
    assert {outcome for outcome, _ in seen} == set(OUTCOMES)
    assert {owner for outcome, owner in seen if outcome == "one_sided"} == {"member_lo", "member_hi"}


def test_f02_witnesses_cover_every_center() -> None:
    assert set(WITNESSES) == set(CENTER_ORDER)


def test_f02_mutation_shared_and_mutual_swapped_is_refused(v2_bundle, monkeypatch) -> None:
    original = kernel._outcome
    swap = {"shared": "mutual", "mutual": "shared"}

    def swapped(in_lo, in_hi, in_union):
        outcome, owner = original(in_lo, in_hi, in_union)
        return swap.get(outcome, outcome), owner

    monkeypatch.setattr(kernel, "_outcome", swapped)
    for center in CENTER_ORDER:
        with pytest.raises(AssertionError):
            _check_f02(v2_bundle, center)


# --- F-11 and F-12 ----------------------------------------------------------------------------

def _pad_gate(registry, channel) -> int:
    near = set(channel.gates)
    for other in registry.channels.values():
        if set(other.gates) & set(channel.gates):
            near |= set(other.gates)
    return min(gate for gate in registry.gates if gate not in near)


def _expected_state(a: tuple[int, int], b: tuple[int, int], a_is_lo: bool) -> tuple[str, str | None]:
    """HDE Math Spec §6.1, transcribed: ownership patterns of the two endpoints."""
    held_a, held_b = sum(a), sum(b)
    if held_a == 2 and held_b == 2:
        return "companionship", None
    if held_a == 2 or held_b == 2:
        state = "compromise" if min(held_a, held_b) == 1 else "dominance"
        a_holds = held_a == 2
        return state, ("member_lo" if a_holds == a_is_lo else "member_hi")
    if held_a == 1 and held_b == 1 and a != b:
        return "electromagnetic", None
    return "none", None


def _check_f11(bundle) -> set[str]:
    registry = bundle.registry
    assert len(registry.channels) == 36
    seen = set()
    for channel_id, channel in registry.channels.items():
        gate_x, gate_y = channel.gates
        base = 1 << (_pad_gate(registry, channel) - 1)
        for a_x, a_y, b_x, b_y in itertools.product((0, 1), repeat=4):
            mask_a = base | (a_x << (gate_x - 1)) | (a_y << (gate_y - 1))
            mask_b = base | (b_x << (gate_x - 1)) | (b_y << (gate_y - 1))
            states = {item.channel_id: (item.state, item.owner) for item in _both(bundle, mask_a, mask_b).channels}
            expected = _expected_state((a_x, a_y), (b_x, b_y), mask_a <= mask_b)
            assert states[channel_id] == expected, (channel_id, a_x, a_y, b_x, b_y)
            seen.add(expected[0])
    return seen


def test_f11_f12_five_states_over_all_36_channels(v2_bundle) -> None:
    assert _check_f11(v2_bundle) == set(STATES)


def test_f11_f12_mutation_compromise_reported_as_dominance_is_refused(v2_bundle, monkeypatch) -> None:
    original = kernel._classify_channel

    def mutated(channel, mask_lo, mask_hi):
        state = original(channel, mask_lo, mask_hi)
        return dataclasses.replace(state, state="dominance") if state.state == "compromise" else state

    monkeypatch.setattr(kernel, "_classify_channel", mutated)
    with pytest.raises(AssertionError):
        _check_f11(v2_bundle)


# --- F-14 -------------------------------------------------------------------------------------

GATE_REFUSALS = {
    "missing": (None, "GATES_NOT_LIST"),
    "not-a-list": ("1,2", "GATES_NOT_LIST"),
    "empty": ([], "GATES_EMPTY"),
    "duplicate": ([1, 1], "GATE_DUPLICATE"),
    "malformed-text": (["x"], "GATE_VALUE_INVALID"),
    "malformed-bool": ([True], "GATE_VALUE_INVALID"),
    "malformed-float": ([1.5], "GATE_VALUE_INVALID"),
    "below-range": ([0], "GATE_VALUE_INVALID"),
    "above-range": ([65], "GATE_VALUE_INVALID"),
}


def _check_f14(bundle) -> None:
    for name, (value, code) in GATE_REFUSALS.items():
        try:
            normalize_gates(value)
        except GateNormalizationError as exc:
            assert exc.code == code, name
        else:
            raise AssertionError(f"accepted {name}")
    low, high = normalize_gates([1]).mask, normalize_gates(list(range(1, 65))).mask
    assert (low, high) == (1, (1 << 64) - 1)
    assert normalize_gates(["64", "1"]).gates == (1, 64)
    kernel.compute_kernel(low, high, bundle)
    for mask in (0, 1 << 64, True, -1):
        try:
            kernel.compute_kernel(mask, low, bundle)
        except SchemaValidationError as exc:
            assert exc.code == kernel.MASK_OUT_OF_DOMAIN
        else:
            raise AssertionError(f"accepted mask {mask!r}")


def test_f14_gate_normalization_and_mask_domain(v2_bundle) -> None:
    _check_f14(v2_bundle)


def test_f14_mutation_zero_mask_accepted_is_refused(v2_bundle, monkeypatch) -> None:
    original = kernel._check_mask

    def accepts_zero(mask, argument):
        if mask == 0 and type(mask) is int:
            return None
        return original(mask, argument)

    monkeypatch.setattr(kernel, "_check_mask", accepts_zero)
    with pytest.raises(AssertionError):
        _check_f14(v2_bundle)
