"""HDE-EPIC043 WU-PR-04: the v2 proof family, signal and calculation items (HDE-DIST008.1).

Items F-03 (the twenty signals in per-mille under the three v2 operations), F-04
(the channel, center and Type components, every pair rule, the clamp of ``T_k``),
F-05 (the score rule), F-06 (band assignment at every edge of every category),
F-07 (integer-only arithmetic and exactly four calculation inputs), F-13 (every
default Channel-to-signal row), F-15 (complete-matrix atomicity), F-16 (AB/BA
identity) and F-17 (two-run identity).

Each item has a check function that raises ``AssertionError`` when its rule is
broken; the passing case runs it on the landed code and the refused mutation
patches one rule in-process. Mutations are constructed perturbations of a rule,
not inputs. Expected values are transcribed from HDE Math Spec §5.2.11 and §5.3.7.
The bundle is the labelled non-canon fixture bundle; the per-category maxima of
F-06 are test values ``(5 + i, 20 + i, 40 + i, 100)``, not canon and not the cut.

Stated limit (F-03): no exact half is reachable for the eighteen ordinary
signals on a real input (PF10 addendum 2.4 R-4), so their half-up reading is
shown on ``rhu``'s own integer arguments.
"""
from __future__ import annotations

import dataclasses
import inspect
import shutil
from pathlib import Path

import pytest

from engine.config.registry_loader import _SIGNAL_MEMBERSHIP, SchemaValidationError
from engine.magic10_v2 import calculation, signals
from engine.magic10_v2.kernel import compute_kernel
from engine.serializer.canon import sercanon
from tests.m10_v2.test_kernel_static_guards import _float_violations

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "engine" / "magic10_v2"
RELEASE_ID = "a" * 64
BALANCE_SIGNALS = ("equilibrium_score", "counterweight_ratio")
PAIRS = (
    ((1,), (2,)),
    ((1, 8), (2,)),
    ((1, 8), (1, 8)),
    ((1,), (8,)),
    ((20, 34), (47, 64)),
    ((1, 8, 3, 60), (2, 14)),
    ((1, 8, 20, 57, 32, 54), (3, 60, 21, 45, 47, 64)),
    ((4, 17, 23, 24, 47), (43, 61, 62, 63, 64)),
)


def _q(bundle, mask_of, gates_a, gates_b) -> dict[str, int]:
    kernel = compute_kernel(mask_of(*gates_a), mask_of(*gates_b), bundle)
    return {value.signal_id: value.q for value in signals.compute_signals(kernel, bundle)}


# --- F-03 -------------------------------------------------------------------------------------

BALANCE_CASES = (
    ("equilibrium_score", (1, 8), (2, 14), 1000),
    ("equilibrium_score", (1, 8), (2,), 0),
    ("equilibrium_score", (1, 8, 3, 60), (2, 14), 667),
    ("counterweight_ratio", (1, 8), (2,), 0),
    ("counterweight_ratio", (1, 8), (1, 8), 1000),
    ("counterweight_ratio", (1, 8, 2, 14), (1, 8), 500),
)


def _check_f03(bundle, mask_of) -> None:
    for numerator, denominator, expected in ((1, 2, 1), (3, 2, 2), (5, 10, 1), (4, 10, 0), (0, 7, 0), (1000, 1, 1000)):
        assert signals.rhu(numerator, denominator) == expected, (numerator, denominator)
    zero = _q(bundle, mask_of, (1,), (2,))
    assert len(zero) == 20 and set(zero.values()) == {0}
    for gates_a, gates_b in PAIRS:
        values = _q(bundle, mask_of, gates_a, gates_b)
        assert all(type(value) is int and 0 <= value <= 1000 for value in values.values())
        assert all(values[name] <= 833 for name in values if name not in BALANCE_SIGNALS)
    for name, gates_a, gates_b, expected in BALANCE_CASES:
        assert _q(bundle, mask_of, gates_a, gates_b)[name] == expected, (name, gates_a, gates_b)


def test_f03_signals_in_per_mille(v2_bundle, mask_of) -> None:
    _check_f03(v2_bundle, mask_of)


def test_f03_mutation_half_down_rounding_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    monkeypatch.setattr(signals, "rhu", lambda numerator, denominator: (2 * numerator + denominator - 1) // (2 * denominator))
    with pytest.raises(AssertionError):
        _check_f03(v2_bundle, mask_of)


def test_f03_mutation_companionship_not_mutual_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    monkeypatch.setattr(signals, "_MUTUAL_STATES", frozenset({"electromagnetic"}))
    with pytest.raises(AssertionError):
        _check_f03(v2_bundle, mask_of)


# --- F-04 -------------------------------------------------------------------------------------

PAIR_RULE_CASES = (
    (("reflector", "reflector"), ("same_class", "reflector_present")),
    (("generator", "projector"), ("generator_with_nonsacral", "generator_projector")),
    (("generator", "manifestor"), ("generator_with_nonsacral", "generator_manifestor")),
    (("projector", "manifestor"), ("projector_manifestor",)),
    (("generator", "reflector"), ("generator_with_nonsacral", "reflector_present")),
    (("generator", "generator"), ("same_class",)),
)


def _check_f04(bundle, mask_of) -> None:
    for offset, expected in ((0, 500), (50, 550), (-50, 450), (600, 1000), (-600, 0)):
        assert calculation.type_component(offset) == expected, offset
    for classes, expected in PAIR_RULE_CASES:
        assert calculation.pair_rules(*classes) == expected, classes
        assert calculation.pair_rules(*reversed(classes)) == expected, classes
    caps = bundle.registry.magic10_caps
    for gates_a, gates_b in PAIRS:
        kernel = compute_kernel(mask_of(*gates_a), mask_of(*gates_b), bundle)
        values = signals.compute_signals(kernel, bundle)
        q = {value.signal_id: value.q for value in values}
        components = calculation.compute_category_components(kernel, values, bundle)
        assert [item.category_id for item in components] == list(bundle.registry.magic10_order)
        for item in components:
            first, second = caps[item.category_id].inputs
            assert item.channel_component == (2 * (q[first] + q[second]) + 2) // 4, item.category_id
            assert 0 <= item.center_component <= 1000 and 0 <= item.type_component <= 1000


def test_f04_components_and_pair_rules(v2_bundle, mask_of) -> None:
    _check_f04(v2_bundle, mask_of)


def test_f04_mutation_unclamped_type_component_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    monkeypatch.setattr(calculation, "type_component", lambda offset_sum: calculation.TYPE_MIDPOINT + offset_sum)
    with pytest.raises(AssertionError):
        _check_f04(v2_bundle, mask_of)


def test_f04_mutation_dropped_pair_rule_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation.pair_rules
    monkeypatch.setattr(
        calculation, "pair_rules", lambda a, b: tuple(rule for rule in original(a, b) if rule != "reflector_present")
    )
    with pytest.raises(AssertionError):
        _check_f04(v2_bundle, mask_of)


# --- F-05 -------------------------------------------------------------------------------------

def _check_f05(bundle) -> None:
    blend = bundle.configuration["blend"]
    assert dict(blend) == {"channel": 60, "center": 25, "type": 15}
    score = calculation.category_score
    assert score(0, 0, 1000, blend) == 0  # Type never scores alone
    assert score(0, 0, 0, blend) == 0
    assert score(1000, 0, 0, blend) == 60
    assert score(0, 20, 0, blend) == 1  # 500 / 1000 = 0.5 rounds half up, once
    assert score(10, 10, 500, blend) == 8  # 8350 / 1000 = 8.35
    assert score(1000, 1000, 1000, blend) == 100
    assert score(1, 0, 0, blend) == 0  # 60 / 1000 rounds down; the zero rule does not apply


def test_f05_score_rule(v2_bundle) -> None:
    _check_f05(v2_bundle)


def test_f05_mutation_type_scoring_alone_is_refused(v2_bundle, monkeypatch) -> None:
    def no_zero_rule(channel, center, type_value, blend):
        blended = blend["channel"] * channel + blend["center"] * center + blend["type"] * type_value
        return min(100, max(0, signals.rhu(blended, 1000)))

    monkeypatch.setattr(calculation, "category_score", no_zero_rule)
    with pytest.raises(AssertionError):
        _check_f05(v2_bundle)


def test_f05_mutation_rounding_down_is_refused(v2_bundle, monkeypatch) -> None:
    def rounds_down(channel, center, type_value, blend):
        if channel == 0 and center == 0:
            return 0
        return min(100, (blend["channel"] * channel + blend["center"] * center + blend["type"] * type_value) // 1000)

    monkeypatch.setattr(calculation, "category_score", rounds_down)
    with pytest.raises(AssertionError):
        _check_f05(v2_bundle)


# --- F-06 -------------------------------------------------------------------------------------

def _check_f06(bundle, mask_of) -> None:
    order = bundle.registry.magic10_order
    for index, category in enumerate(order):
        first, second, third, last = maxima = (5 + index, 20 + index, 40 + index, 100)
        expected = {0: "Cool", first: "Cool", first + 1: "Open", second: "Open", second + 1: "Warm",
                    third: "Warm", third + 1: "Glow", last: "Glow"}
        for score, band in expected.items():
            assert calculation.assign_band(score, maxima) == band, (category, score)
    for gates_a, gates_b in PAIRS:
        kernel = compute_kernel(mask_of(*gates_a), mask_of(*gates_b), bundle)
        for item in calculation.compute_category_components(kernel, signals.compute_signals(kernel, bundle), bundle):
            first, second, third, _ = bundle.maxima[item.category_id]
            band = "Cool" if item.score <= first else "Open" if item.score <= second else "Warm" if item.score <= third else "Glow"
            assert item.band == band, item.category_id


def test_f06_band_at_every_edge_of_every_category(v2_bundle, mask_of) -> None:
    _check_f06(v2_bundle, mask_of)


def test_f06_mutation_exclusive_maxima_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    def exclusive(score, maxima):
        first, second, third, _ = maxima
        return "Cool" if score < first else "Open" if score < second else "Warm" if score < third else "Glow"

    monkeypatch.setattr(calculation, "assign_band", exclusive)
    with pytest.raises(AssertionError):
        _check_f06(v2_bundle, mask_of)


# --- F-07 -------------------------------------------------------------------------------------

def _check_f07_integer_only(directory: Path) -> None:
    modules = sorted(directory.glob("*.py"))
    assert modules
    assert {path.name: _float_violations(path) for path in modules} == {path.name: [] for path in modules}


def _check_f07_inputs(function) -> None:
    assert list(inspect.signature(function).parameters) == ["mask_a", "mask_b", "bundle", "release_id"]


def test_f07_integer_only_and_exactly_four_inputs() -> None:
    _check_f07_integer_only(PACKAGE)
    _check_f07_inputs(calculation.compute_magic10_v2)


def test_f07_mutation_a_float_operation_is_flagged(tmp_path) -> None:
    for path in PACKAGE.glob("*.py"):
        shutil.copyfile(path, tmp_path / path.name)
    with (tmp_path / "calculation.py").open("a", encoding="utf-8") as handle:
        handle.write("\n_RATIO = 60 / 100\n")
    with pytest.raises(AssertionError):
        _check_f07_integer_only(tmp_path)


def test_f07_mutation_a_caller_weight_input_is_refused() -> None:
    def with_weights(mask_a, mask_b, bundle, release_id, weights=None):
        return calculation.compute_magic10_v2(mask_a, mask_b, bundle, release_id)

    with pytest.raises(AssertionError):
        _check_f07_inputs(with_weights)


# --- F-13 -------------------------------------------------------------------------------------

def _pad(registry, channel) -> int:
    near = set(channel.gates)
    for other in registry.channels.values():
        if set(other.gates) & set(channel.gates):
            near |= set(other.gates)
    return min(gate for gate in registry.gates if gate not in near)


def _check_f13(bundle) -> None:
    registry = bundle.registry
    members = {name: set(channels) for name, (_profile, channels) in _SIGNAL_MEMBERSHIP.items()}
    ordinary = [name for name in members if name not in BALANCE_SIGNALS]
    assert len(ordinary) == 18
    for channel_id, channel in registry.channels.items():
        holder = (1 << (channel.gates[0] - 1)) | (1 << (channel.gates[1] - 1))
        kernel = compute_kernel(holder, 1 << (_pad(registry, channel) - 1), bundle)
        q = {value.signal_id: value.q for value in signals.compute_signals(kernel, bundle)}
        assert list(q) == list(_SIGNAL_MEMBERSHIP), channel_id
        assert {name for name in ordinary if q[name] > 0} == {name for name in ordinary if channel_id in members[name]}, channel_id


def test_f13_every_default_channel_to_signal_row(v2_bundle) -> None:
    _check_f13(v2_bundle)


def test_f13_mutation_dropped_row_is_refused(v2_bundle, monkeypatch) -> None:
    original = signals._signal_rows
    monkeypatch.setattr(signals, "_signal_rows", lambda bundle, kernel: (original(bundle, kernel)[0][1:], original(bundle, kernel)[1]))
    with pytest.raises(AssertionError):
        _check_f13(v2_bundle)


def test_f13_mutation_moved_channel_is_refused(v2_bundle, monkeypatch) -> None:
    original = signals._signal_rows

    def moved(bundle, kernel):
        rows, saturation = original(bundle, kernel)
        first, second = rows[0], rows[1]
        rows = (
            dataclasses.replace(first, channels=first.channels[1:]),
            dataclasses.replace(second, channels=second.channels + first.channels[:1]),
            *rows[2:],
        )
        return rows, saturation

    monkeypatch.setattr(signals, "_signal_rows", moved)
    with pytest.raises(AssertionError):
        _check_f13(v2_bundle)


# --- F-15 -------------------------------------------------------------------------------------

def _check_f15(bundle, mask_of) -> None:
    order = list(bundle.registry.magic10_order)
    signal_order = [row["signal_id"] for row in bundle.configuration["signals"]]
    for gates_a, gates_b in PAIRS:
        result = calculation.compute_magic10_v2(mask_of(*gates_a), mask_of(*gates_b), bundle, RELEASE_ID)
        assert [item.category_id for item in result.categories] == order
        assert [item.signal_id for item in result.signals] == signal_order and len(signal_order) == 20


def test_f15_complete_matrix_or_refusal(v2_bundle, mask_of, monkeypatch) -> None:
    _check_f15(v2_bundle, mask_of)
    produced = []

    def refuses_midway(kernel, bundle):
        raise SchemaValidationError(signals.BUNDLE_INCOMPLETE, "refused after the kernel", {"component": "test"})

    monkeypatch.setattr(calculation, "compute_signals", refuses_midway)
    with pytest.raises(SchemaValidationError):
        produced.append(calculation.compute_magic10_v2(mask_of(1, 8), mask_of(2), v2_bundle, RELEASE_ID))
    assert produced == []


def test_f15_mutation_partial_matrix_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation.compute_category_components
    monkeypatch.setattr(calculation, "compute_category_components", lambda *args: original(*args)[:9])
    with pytest.raises(AssertionError):
        _check_f15(v2_bundle, mask_of)


# --- F-16 and F-17 ----------------------------------------------------------------------------

def _payload(bundle, mask_a: int, mask_b: int) -> bytes:
    return sercanon(calculation.compute_magic10_v2(mask_a, mask_b, bundle, RELEASE_ID).as_payload(), sort_keys=True)


def _check_f16(bundle, mask_of) -> None:
    for gates_a, gates_b in PAIRS:
        mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
        assert _payload(bundle, mask_a, mask_b) == _payload(bundle, mask_b, mask_a), (gates_a, gates_b)


def _check_f17(bundle, mask_of) -> None:
    for gates_a, gates_b in PAIRS:
        mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
        assert _payload(bundle, mask_a, mask_b) == _payload(bundle, mask_a, mask_b), (gates_a, gates_b)


def _emptied(result):
    return dataclasses.replace(
        result, channels=tuple(dataclasses.replace(item, state="none", owner=None) for item in result.channels)
    )


def test_f16_ab_ba_identity(v2_bundle, mask_of) -> None:
    _check_f16(v2_bundle, mask_of)


def test_f17_two_run_identity(v2_bundle, mask_of) -> None:
    _check_f17(v2_bundle, mask_of)


def test_f16_mutation_order_dependent_kernel_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation.compute_kernel

    def order_dependent(mask_a, mask_b, bundle):
        result = original(mask_a, mask_b, bundle)
        return _emptied(result) if mask_a > mask_b else result

    monkeypatch.setattr(calculation, "compute_kernel", order_dependent)
    with pytest.raises(AssertionError):
        _check_f16(v2_bundle, mask_of)


def test_f17_mutation_run_dependent_kernel_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation.compute_kernel
    calls = []

    def run_dependent(mask_a, mask_b, bundle):
        calls.append(1)
        result = original(mask_a, mask_b, bundle)
        return _emptied(result) if len(calls) % 2 == 0 else result

    monkeypatch.setattr(calculation, "compute_kernel", run_dependent)
    with pytest.raises(AssertionError):
        _check_f17(v2_bundle, mask_of)
