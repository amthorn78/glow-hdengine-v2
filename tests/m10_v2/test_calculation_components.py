"""HDE-EPIC043 WU-PR-02 acceptance item 2: ``C_k``, ``Z_k``, ``T_k``, the score and the zero rule (HDE-CONJ010.3).

HDE Math Spec §5.2.11, "Components" and evaluation step 8, on real mask pairs.
Expected values are transcribed from canon arithmetic, never read back from the
module under test:

* ``C_k = rhu(q_s1 + q_s2, 2)`` over the category's two caps inputs;
* mapped ``Z_k = rhu(1000·Σ w·r(profile, outcome), 10000·Σ w)``, with
  ``motor_throat`` reading the motor→Throat outcome; ``balance``
  ``Z = rhu(1000·2·min(gives_lo, gives_hi), gives_lo + gives_hi)``, ``gives``
  counted over the nine centers only (the motor→Throat outcome is not a center);
* ``T_k = min(1000, max(0, 500 + Σ I_k[rule]))`` over the rules that hold;
* ``score_k = 0`` when ``C_k = 0`` and ``Z_k = 0``, else
  ``min(100, max(0, rhu(60·C + 25·Z + 15·T, 1000)))``.

Stated limits (instruction S-6): over every admitted class pair and category
``500 + Σ I`` stays in ``450..550`` and the score in ``0..93``, so neither clamp
acts on a real input; both clamps are shown on their own integer arguments.
Every computing case is also run for (B, A) and must be equal.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import pytest

from engine.magic10_v2.calculation import (
    PAIR_RULES,
    category_score,
    compute_category_components,
    pair_rules,
    type_component,
)
from engine.magic10_v2.kernel import compute_kernel
from engine.magic10_v2.signals import compute_signals, rhu

ROOT = Path(__file__).resolve().parents[2]
CAPS = json.loads((ROOT / "catalog" / "magic10_caps.json").read_bytes())

# Representative members (as the kernel tests): derived Type from the Gate set.
CLASS_MASKS = {
    "R": (1,),  # Reflector
    "P": (1, 8),  # Projector
    "G": (1, 8, 3, 60),  # Generator
    "MG": (20, 34),  # Manifesting Generator
    "M": (21, 45),  # Manifestor
}
# HDE Math Spec §5.2.11 rule predicates over the aura classes of each pair.
EXPECTED_RULES = {
    ("R", "R"): ("same_class", "reflector_present"),
    ("R", "P"): ("reflector_present",),
    ("R", "G"): ("generator_with_nonsacral", "reflector_present"),
    ("R", "MG"): ("generator_with_nonsacral", "reflector_present"),
    ("R", "M"): ("reflector_present",),
    ("P", "P"): ("same_class",),
    ("P", "G"): ("generator_with_nonsacral", "generator_projector"),
    ("P", "MG"): ("generator_with_nonsacral", "generator_projector"),
    ("P", "M"): ("projector_manifestor",),
    ("G", "G"): ("same_class",),
    ("G", "MG"): ("same_class",),
    ("G", "M"): ("generator_with_nonsacral", "generator_manifestor"),
    ("MG", "MG"): ("same_class",),
    ("MG", "M"): ("generator_with_nonsacral", "generator_manifestor"),
    ("M", "M"): ("same_class",),
}
PAIRS = (
    ((1,), (2,)),
    ((1, 8), (2,)),
    ((1, 8), (1, 8)),
    ((1,), (8,)),
    ((20, 34), (20, 34)),
    ((21,), (45,)),
    ((1, 8), (20, 34)),
    ((1, 8), (20, 34, 21, 45)),
    ((18, 26, 44, 58), (18, 26, 44, 58)),
    ((1, 8, 3, 60), (2, 14)),
    ((4, 17, 23, 24, 47), (43, 61, 62, 63, 64)),
)


def _evaluate(bundle, mask_of, gates_a, gates_b):
    """Kernel, signals and components for (A, B); asserts (B, A) is identical."""
    mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
    kernel = compute_kernel(mask_a, mask_b, bundle)
    signals = compute_signals(kernel, bundle)
    components = compute_category_components(kernel, signals, bundle)
    reverse = compute_kernel(mask_b, mask_a, bundle)
    assert compute_category_components(reverse, compute_signals(reverse, bundle), bundle) == components
    return kernel, {signal.signal_id: signal.q for signal in signals}, {item.category_id: item for item in components}


def test_channel_component_on_real_pairs(v2_bundle, mask_of) -> None:
    _, values, components = _evaluate(v2_bundle, mask_of, (4, 17, 23, 24, 47), (43, 61, 62, 63, 64))
    assert (values["signal_clarity"], values["exchange_density"]) == (833, 0)
    assert components["communication"].channel_component == 417  # exact half: 416.5 rounds up
    _, _, components = _evaluate(v2_bundle, mask_of, (21,), (45,))
    assert components["balance"].channel_component == 500
    for gates_a, gates_b in PAIRS:
        _, values, components = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
        for category, entry in CAPS.items():
            first, second = entry["inputs"]
            assert components[category].channel_component == rhu(values[first] + values[second], 2)


@pytest.mark.parametrize(
    "gates_a, gates_b, expected",
    [
        ((1, 8), (1, 8), {"harmony": 125, "alignment": 600}),  # g shared
        ((1, 8), (2,), {"harmony": 375, "alignment": 450}),  # g one_sided
        ((1,), (8,), {"harmony": 500, "alignment": 300}),  # g mutual
        ((1,), (2,), {"harmony": 0, "alignment": 0}),  # g open
        ((20, 34), (20, 34), {"heat": 125, "drive": 94}),  # motor_throat shared
        ((21,), (45,), {"heat": 250, "drive": 500}),  # motor_throat mutual
        ((1, 8), (20, 34), {"heat": 375, "drive": 281}),  # motor_throat one_sided
        ((18, 26, 44, 58), (18, 26, 44, 58), {"heat": 63}),  # Σ = 5000: exact half, 62.5 rounds up
    ],
    ids=["g-shared", "g-one-sided", "g-mutual", "g-open", "mt-shared", "mt-mutual", "mt-one-sided", "heat-half"],
)
def test_center_component_mapped(v2_bundle, mask_of, gates_a, gates_b, expected) -> None:
    _, _, components = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    assert {category: components[category].center_component for category in expected} == expected


def _gives(kernel) -> tuple[int, int]:
    lo = sum(c.outcome == "mutual" or (c.outcome == "one_sided" and c.owner == "member_lo") for c in kernel.centers)
    hi = sum(c.outcome == "mutual" or (c.outcome == "one_sided" and c.owner == "member_hi") for c in kernel.centers)
    return lo, hi


@pytest.mark.parametrize(
    "gates_a, gates_b, gives, expected",
    [
        ((21,), (45,), (2, 2), 1000),
        ((1, 8), (20, 34), (1, 1), 1000),  # motor→Throat one_sided is not counted (it would give 667)
        ((1, 8), (20, 34, 21, 45), (1, 2), 667),
        ((1, 8), (2,), (0, 2), 0),
        ((1,), (2,), (0, 0), 0),
    ],
)
def test_center_component_balance_counts_the_nine_centers_only(v2_bundle, mask_of, gates_a, gates_b, gives, expected):
    kernel, _, components = _evaluate(v2_bundle, mask_of, gates_a, gates_b)
    assert _gives(kernel) == gives
    assert components["balance"].center_component == expected
    if (gates_a, gates_b) == ((1, 8), (20, 34)):
        assert kernel.motor_throat.outcome == "one_sided"


@pytest.mark.parametrize("pair", list(EXPECTED_RULES), ids=["-".join(pair) for pair in EXPECTED_RULES])
def test_type_component_and_every_pair_rule(v2_bundle, mask_of, pair) -> None:
    kernel, _, components = _evaluate(v2_bundle, mask_of, CLASS_MASKS[pair[0]], CLASS_MASKS[pair[1]])
    assert pair_rules(kernel.member_lo.aura_class, kernel.member_hi.aura_class) == EXPECTED_RULES[pair]
    expected = {category: 500 for category in v2_bundle.registry.magic10_order}
    if "generator_projector" in EXPECTED_RULES[pair]:
        expected.update(communication=550, alignment=550)
    if "projector_manifestor" in EXPECTED_RULES[pair]:
        expected.update(alignment=450)
    assert {category: item.type_component for category, item in components.items()} == expected


def test_every_rule_is_shown_holding_and_not_holding() -> None:
    holding = {rule for rules in EXPECTED_RULES.values() for rule in rules}
    assert holding == set(PAIR_RULES)
    for rule in PAIR_RULES:
        assert any(rule not in rules for rules in EXPECTED_RULES.values()), rule
    assert len(EXPECTED_RULES[("R", "R")]) == 2  # two rules at once


def test_generator_with_nonsacral_holds_exactly_when_sacral_is_one_sided(v2_bundle, mask_of) -> None:
    pairs = [(CLASS_MASKS[a], CLASS_MASKS[b]) for a, b in EXPECTED_RULES] + list(PAIRS)
    for gates_a, gates_b in pairs:
        kernel = compute_kernel(mask_of(*gates_a), mask_of(*gates_b), v2_bundle)
        sacral = next(center for center in kernel.centers if center.center_id == "sacral")
        holds = "generator_with_nonsacral" in pair_rules(kernel.member_lo.aura_class, kernel.member_hi.aura_class)
        assert holds == (sacral.outcome == "one_sided"), (gates_a, gates_b)


def test_pair_rules_are_symmetric(v2_bundle) -> None:
    for class_a, class_b in itertools.product(v2_bundle.aura_classes, repeat=2):
        assert pair_rules(class_a, class_b) == pair_rules(class_b, class_a)


@pytest.mark.parametrize(
    "offset_sum, expected", [(-501, 0), (-500, 0), (-50, 450), (0, 500), (50, 550), (500, 1000), (501, 1000)]
)
def test_type_component_clamp_on_its_own_arguments(offset_sum, expected) -> None:
    assert type_component(offset_sum) == expected


def test_type_component_clamp_cannot_act_on_an_admitted_bundle(v2_bundle) -> None:
    """Stated limit (S-6): the pinned offsets keep 500 + Σ I inside 450..550."""
    raw = set()
    for class_a, class_b in itertools.product(v2_bundle.aura_classes, repeat=2):
        for category in v2_bundle.registry.magic10_order:
            offsets = sum(v2_bundle.type_pairing[rule][category] for rule in pair_rules(class_a, class_b))
            raw.add(500 + offsets)
    assert min(raw) == 450 and max(raw) == 550


def test_zero_rule_and_score(v2_bundle, mask_of) -> None:
    _, _, components = _evaluate(v2_bundle, mask_of, (1,), (2,))
    for item in components.values():
        assert (item.channel_component, item.center_component, item.type_component, item.score) == (0, 0, 500, 0)
    _, _, components = _evaluate(v2_bundle, mask_of, (1, 8), (2,))
    harmony = components["harmony"]
    assert (harmony.channel_component, harmony.center_component, harmony.score) == (0, 375, 17)
    _, _, components = _evaluate(v2_bundle, mask_of, (1, 8), (1, 8))
    balance = components["balance"]
    assert (balance.channel_component, balance.center_component, balance.score) == (500, 0, 38)  # 37.5 rounds up


@pytest.mark.parametrize(
    "channel, center, type_value, expected",
    [
        (1, 0, -100, 0),  # inner value -1, clamped to 0
        (1, 0, 0, 0),  # inner value 0, not the zero rule
        (1000, 1000, 1000, 100),
        (1010, 1010, 1010, 100),  # inner value 101, clamped to 100
        (0, 0, 500, 0),  # the zero rule
    ],
)
def test_score_clamp_on_its_own_arguments(v2_bundle, channel, center, type_value, expected) -> None:
    assert category_score(channel, center, type_value, v2_bundle.configuration["blend"]) == expected


def test_score_clamp_cannot_act_on_an_admitted_bundle(v2_bundle) -> None:
    """Stated limit (S-6): with the pinned blend and T <= 550 the inner value is at most 93."""
    blend = v2_bundle.configuration["blend"]
    assert dict(blend) == {"channel": 60, "center": 25, "type": 15}
    assert rhu(blend["channel"] * 1000 + blend["center"] * 1000 + blend["type"] * 550, 1000) == 93
