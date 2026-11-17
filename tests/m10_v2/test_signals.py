"""HDE-EPIC043 WU-PR-02 acceptance item 1: the twenty v2 signals (HDE-CONJ010.2; R-02, AC-02).

HDE Math Spec §5.2.11, "Signals". Every expected value below is transcribed
from canon arithmetic on real mask pairs (Gate sets through the repository's own
normalizer), never read back from the module under test:

* ordinary signals, ``saturating_state_sum_v2``: ``q = rhu(1000·S, S + 10000)``,
  ``0`` when ``S = 0``. With every mapped Channel in the profile's top state the
  value is 800 for a four-Channel map and 833 for a five-Channel map, never 1000;
* ``equilibrium_score``, ``bilateral_owner_mass_v2``:
  ``q = rhu(1000·2·min(m_lo, m_hi), m_lo + m_hi)``, ``0`` if both are ``0``;
* ``counterweight_ratio``, ``mutual_state_share_v2``: ``q = rhu(1000·M, F)``,
  ``0`` if ``F = 0``.

Stated limit: no ordinary signal has an exact-half real input (proved here by
enumerating every response combination of every ordinary map), so their
half-up rounding rests on the shared ``rhu`` helper, shown on its own integer
arguments. Both Balance operations are shown at an exact half on real pairs.
Every computing case is also run for (B, A) and must be equal.
"""
from __future__ import annotations

import itertools

import pytest

from engine.magic10_v2.kernel import compute_kernel
from engine.magic10_v2.signals import (
    MUTUAL_SHARE_OPERATION,
    ORDINARY_OPERATION,
    OWNER_MASS_OPERATION,
    compute_signals,
    rhu,
)

# HDE Math Spec §5.2.4, the v1 register v2 keeps (Channel IDs are the catalog's),
# in the category order of catalog/magic10.json; each category's pair is its two rows.
REGISTER = (
    ("rapport_delta", "coherence_bp_v1", ("19-49", "26-44", "27-50", "37-40")),
    ("resonance_strength", "coherence_bp_v1", ("05-15", "06-59", "12-22", "13-33")),
    ("spark_intensity", "activation_bp_v1", ("06-59", "25-51", "30-41", "39-55")),
    ("momentum_flux", "activation_bp_v1", ("03-60", "20-34", "29-46", "35-36")),
    ("signal_clarity", "expression_bp_v1", ("04-63", "17-62", "23-43", "24-61", "47-64")),
    ("exchange_density", "expression_bp_v1", ("11-56", "12-22", "13-33", "20-57", "26-44")),
    ("vector_cohesion", "coherence_bp_v1", ("02-14", "07-31", "10-20", "10-34")),
    ("axis_agreement", "coherence_bp_v1", ("19-49", "27-50", "28-38", "32-54")),
    ("soothe_index", "coherence_bp_v1", ("06-59", "12-22", "19-49", "37-40")),
    ("buffer_resilience", "coherence_bp_v1", ("05-15", "10-57", "27-50", "34-57")),
    ("pattern_integrity", "coherence_bp_v1", ("05-15", "09-52", "16-48", "17-62", "18-58")),
    ("variance_stability", "coherence_bp_v1", ("03-60", "29-46", "32-54", "42-53")),
    ("growth_tendency", "activation_bp_v1", ("03-60", "18-58", "32-54", "42-53")),
    ("horizon_reach", "activation_bp_v1", ("11-56", "28-38", "29-46", "35-36")),
    ("novelty_factor", "activation_bp_v1", ("01-08", "03-60", "23-43", "25-51")),
    ("expression_flow", "expression_bp_v1", ("10-20", "11-56", "12-22", "16-48", "35-36")),
    ("willpower_current", "activation_bp_v1", ("02-14", "21-45", "25-51", "26-44", "32-54")),
    ("focus_pressure", "activation_bp_v1", ("09-52", "18-58", "20-34", "28-38", "42-53")),
)
BALANCE = (("equilibrium_score", OWNER_MASS_OPERATION), ("counterweight_ratio", MUTUAL_SHARE_OPERATION))
# HDE Math Spec §5.2.3: each profile's top-response state.
TOP_STATE = {
    "coherence_bp_v1": "companionship",
    "activation_bp_v1": "electromagnetic",
    "expression_bp_v1": "electromagnetic",
}
# The midpoint state pattern (top, dominance, none, …) gives S = top + dominance.
MIDPOINT_Q = {"coherence_bp_v1": 600, "activation_bp_v1": 636, "expression_bp_v1": 600}

# Exact halves on real pairs, found by search (seed 20261117) and recorded in the
# WU-PR-02 plan (M-5): owned Channels 13 and 19, and F 16 with M 3.
E_HALF = (
    (1, 2, 4, 5, 6, 7, 8, 10, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 39, 40, 41,
     44, 45, 46, 49, 50, 51, 52, 54, 55, 58, 59, 61, 63, 64),
    (3, 7, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 29, 35, 36, 37, 40, 42, 43, 44, 47, 48, 51, 52, 53, 56,
     57, 58, 60, 61, 64),
)
W_HALF = (
    (2, 6, 9, 12, 13, 17, 18, 19, 22, 23, 27, 31, 34, 37, 42, 43, 47, 50, 52, 58, 59, 63),
    (3, 7, 13, 14, 17, 18, 21, 22, 23, 25, 26, 32, 33, 34, 35, 38, 42, 44, 47, 49, 54, 57, 60, 62, 63, 64),
)


def _gates(channel_id: str) -> tuple[int, int]:
    first, second = channel_id.split("-")
    return int(first), int(second)


def _evaluate(bundle, mask_of, gates_a, gates_b):
    """Kernel and signals for (A, B); asserts the (B, A) result is identical."""
    mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
    kernel = compute_kernel(mask_a, mask_b, bundle)
    signals = compute_signals(kernel, bundle)
    reverse_kernel = compute_kernel(mask_b, mask_a, bundle)
    assert reverse_kernel == kernel
    assert compute_signals(reverse_kernel, bundle) == signals
    for signal in signals:
        assert type(signal.q) is int and 0 <= signal.q <= 1000, signal
    return kernel, {signal.signal_id: signal.q for signal in signals}


def _maximum_pair(profile_id: str, channel_ids: tuple[str, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = [_gates(channel_id) for channel_id in channel_ids]
    if TOP_STATE[profile_id] == "companionship":
        both = tuple(sorted({gate for pair in pairs for gate in pair}))
        return both, both
    return tuple(sorted(pair[0] for pair in pairs)), tuple(sorted(pair[1] for pair in pairs))


def _midpoint_pair(profile_id: str, channel_ids: tuple[str, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    first, second = _gates(channel_ids[0]), _gates(channel_ids[1])
    if TOP_STATE[profile_id] == "companionship":
        return (*first, *second), first
    return (first[0], *second), (first[1],)


def test_register_ids_pairs_maps_and_operations_are_unchanged(v2_bundle, mask_of) -> None:
    rows = v2_bundle.configuration["signals"]
    flattened = [signal for category in v2_bundle.registry.magic10_order
                 for signal in v2_bundle.registry.magic10_caps[category].inputs]
    expected_ids = [signal_id for signal_id, _, _ in REGISTER] + [signal_id for signal_id, _ in BALANCE]
    assert [row["signal_id"] for row in rows] == expected_ids == flattened
    for row, (signal_id, profile_id, channel_ids) in zip(rows, REGISTER):
        assert row["operation"] == ORDINARY_OPERATION, signal_id
        assert row["profile_id"] == profile_id, signal_id
        assert [channel["channel_id"] for channel in row["channels"]] == sorted(channel_ids), signal_id
    all_channels = sorted(v2_bundle.registry.channels)
    for row, (signal_id, operation) in zip(rows[18:], BALANCE):
        assert row["operation"] == operation, signal_id
        assert "profile_id" not in row
        assert [channel["channel_id"] for channel in row["channels"]] == all_channels
    assert {channel["weight"] for row in rows for channel in row["channels"]} == {1}
    _, values = _evaluate(v2_bundle, mask_of, (1, 8), (2,))
    assert list(values) == expected_ids


def test_zero_when_every_channel_state_is_none(v2_bundle, mask_of) -> None:
    kernel, values = _evaluate(v2_bundle, mask_of, (1,), (2,))
    assert {channel.state for channel in kernel.channels} == {"none"}
    assert values == {signal_id: 0 for signal_id in values}


@pytest.mark.parametrize("signal_id, profile_id, channel_ids", REGISTER, ids=[row[0] for row in REGISTER])
def test_ordinary_signal_maximum_is_800_or_833_never_1000(v2_bundle, mask_of, signal_id, profile_id, channel_ids):
    gates_a, gates_b = _maximum_pair(profile_id, channel_ids)
    kernel, values = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    states = {channel.channel_id: channel.state for channel in kernel.channels}
    assert [states[channel_id] for channel_id in channel_ids] == [TOP_STATE[profile_id]] * len(channel_ids)
    assert values[signal_id] == {4: 800, 5: 833}[len(channel_ids)]


@pytest.mark.parametrize("signal_id, profile_id, channel_ids", REGISTER, ids=[row[0] for row in REGISTER])
def test_ordinary_signal_midpoint(v2_bundle, mask_of, signal_id, profile_id, channel_ids) -> None:
    gates_a, gates_b = _midpoint_pair(profile_id, channel_ids)
    kernel, values = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    states = {channel.channel_id: channel.state for channel in kernel.channels}
    expected = [TOP_STATE[profile_id], "dominance"] + ["none"] * (len(channel_ids) - 2)
    assert [states[channel_id] for channel_id in channel_ids] == expected
    assert values[signal_id] == MIDPOINT_Q[profile_id]


@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (1, 2, 1), (3, 2, 2), (5, 2, 3), (1, 4, 0), (3, 4, 1), (0, 7, 0),
        (3000, 16, 188), (26000, 32, 813), (2000, 3, 667), (833, 2, 417), (37500, 1000, 38),
    ],
)
def test_rhu_rounds_half_up_on_its_own_integer_arguments(numerator, denominator, expected) -> None:
    assert rhu(numerator, denominator) == expected


def test_no_ordinary_signal_has_an_exact_half_real_input(v2_bundle) -> None:
    """Stated limit (instruction S-2): every response combination of every ordinary map."""
    configuration = v2_bundle.configuration
    saturation = configuration["saturation_k_bp"]
    responses = {row["profile_id"]: sorted(set(row["responses"].values())) for row in configuration["profiles"]}
    checked = 0
    for row in configuration["signals"][:18]:
        for combination in itertools.product(responses[row["profile_id"]], repeat=len(row["channels"])):
            total = sum(combination)
            checked += 1
            if total:
                doubled, denominator = 2 * 1000 * total, total + saturation
                assert not (doubled % denominator == 0 and (doubled // denominator) % 2 == 1), (row["signal_id"], total)
    assert checked == 12 * 5 ** 4 + 6 * 5 ** 5


def _owned(kernel) -> tuple[int, int]:
    owned = [channel.owner for channel in kernel.channels if channel.state in ("dominance", "compromise")]
    return owned.count("member_lo"), owned.count("member_hi")


def _filled_and_mutual(kernel) -> tuple[int, int]:
    states = [channel.state for channel in kernel.channels]
    return (sum(state != "none" for state in states),
            sum(state in ("companionship", "electromagnetic") for state in states))


@pytest.mark.parametrize(
    "gates_a, gates_b, owned, expected",
    [
        ((1, 8), (2, 14), (1, 1), 1000),  # symmetric
        ((1, 8), (2,), (0, 1), 0),  # one-sided
        ((1,), (2,), (0, 0), 0),  # empty
        ((1, 8, 3, 60), (2, 14), (1, 2), 667),  # mixed
        (*E_HALF, (13, 19), 813),  # exact half: 812.5 rounds up
    ],
    ids=["symmetric", "one-sided", "empty", "mixed", "exact-half"],
)
def test_equilibrium_score(v2_bundle, mask_of, gates_a, gates_b, owned, expected) -> None:
    kernel, values = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    assert _owned(kernel) == owned
    assert values["equilibrium_score"] == expected


@pytest.mark.parametrize(
    "gates_a, gates_b, filled_mutual, expected",
    [
        ((1,), (2,), (0, 0), 0),  # F = 0
        ((1, 8), (2,), (1, 0), 0),  # M = 0
        ((1, 8), (1, 8), (1, 1), 1000),  # M = F
        ((1, 8, 2, 14), (1, 8), (2, 1), 500),  # mixed
        (*W_HALF, (16, 3), 188),  # exact half: 187.5 rounds up
    ],
    ids=["F-zero", "M-zero", "M-equals-F", "mixed", "exact-half"],
)
def test_counterweight_ratio(v2_bundle, mask_of, gates_a, gates_b, filled_mutual, expected) -> None:
    kernel, values = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    assert _filled_and_mutual(kernel) == filled_mutual
    assert values["counterweight_ratio"] == expected
