"""HDE-EPIC043 WU-PR-02: fail-closed refusals of the signals and calculation modules (HDE-CONJ010.2, .3).

HDE Math Spec §5.2.11: "A missing center, class, weight, profile or band line
fails closed." Each case is one input outside the real set and receives one
refusal: a ``SchemaValidationError`` with its stable code and details, and no
result.

* ``release_id``: the product supplies the active release's identity, a
  lowercase SHA-256 hex digest; any other value is refused and never echoed.
* Bundle: an admitted bundle cannot trigger these refusals, because the v2
  loader pins the whole configuration, the Type-pairing catalog and ascending
  maxima. Each bundle case is therefore one component of the admitted bundle
  replaced (``dataclasses.replace``), the bundle object a caller could construct
  without the loader.
* The kernel's own refusals propagate unchanged.
"""
from __future__ import annotations

import dataclasses
from types import MappingProxyType

import pytest

from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2 import calculation, signals
from engine.magic10_v2.calculation import compute_category_components, compute_magic10_v2
from engine.magic10_v2.kernel import MASK_OUT_OF_DOMAIN, compute_kernel
from engine.magic10_v2.signals import compute_signals

RELEASE_ID = "1f" * 32


def _thaw(value):
    if isinstance(value, MappingProxyType) or isinstance(value, dict):
        return {key: _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


def _freeze(value):
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _with_configuration(bundle, mutate):
    configuration = _thaw(bundle.configuration)
    mutate(configuration)
    return dataclasses.replace(bundle, configuration=_freeze(configuration))


def _row(rows: list, key: str, value: str) -> dict:
    return next(row for row in rows if row[key] == value)


def _refusal(call, *args) -> SchemaValidationError:
    result = None
    with pytest.raises(SchemaValidationError) as caught:
        result = call(*args)
    assert result is None
    return caught.value


@pytest.fixture()
def kernel(v2_bundle, mask_of):
    return compute_kernel(mask_of(1, 8), mask_of(2, 14), v2_bundle)


@pytest.fixture()
def masks(mask_of):
    return mask_of(1, 8), mask_of(2, 14)


# --- signals.py ------------------------------------------------------------------

def test_signals_refuse_wrong_input_types(v2_bundle, kernel) -> None:
    error = _refusal(compute_signals, None, v2_bundle)
    assert (error.code, error.details) == (signals.INPUT_INVALID, {"argument": "kernel"})
    error = _refusal(compute_signals, kernel, None)
    assert (error.code, error.details) == (signals.INPUT_INVALID, {"argument": "bundle"})


@pytest.mark.parametrize(
    "mutate, component",
    [
        (lambda c: c.pop("signals"), "configuration.signals"),
        (lambda c: c.pop("profiles"), "configuration.profiles"),
        (lambda c: c.__setitem__("saturation_k_bp", 0), "configuration.saturation_k_bp"),
    ],
    ids=["no-signals", "no-profiles", "saturation-zero"],
)
def test_signals_refuse_an_incomplete_configuration(v2_bundle, kernel, mutate, component) -> None:
    error = _refusal(compute_signals, kernel, _with_configuration(v2_bundle, mutate))
    assert (error.code, error.details) == (signals.BUNDLE_INCOMPLETE, {"component": component})


def test_signals_refuse_an_unknown_operation(v2_bundle, kernel) -> None:
    def mutate(configuration):
        _row(configuration["signals"], "signal_id", "rapport_delta")["operation"] = "saturating_state_sum_v1"
    bundle = _with_configuration(v2_bundle, mutate)
    error = _refusal(compute_signals, kernel, bundle)
    assert (error.code, error.details) == (
        signals.OPERATION_UNKNOWN, {"signal_id": "rapport_delta", "operation": "saturating_state_sum_v1"},
    )


def test_signals_refuse_a_missing_profile_or_response(v2_bundle, kernel) -> None:
    def rename(configuration):
        _row(configuration["signals"], "signal_id", "rapport_delta")["profile_id"] = "coherence_bp_v2"
    bundle = _with_configuration(v2_bundle, rename)
    error = _refusal(compute_signals, kernel, bundle)
    assert (error.code, error.details) == (
        signals.PROFILE_MISSING, {"signal_id": "rapport_delta", "profile_id": "coherence_bp_v2"},
    )
    bundle = _with_configuration(
        v2_bundle, lambda c: _row(c["profiles"], "profile_id", "coherence_bp_v1")["responses"].pop("dominance")
    )
    error = _refusal(compute_signals, kernel, bundle)
    assert (error.code, error.details) == (
        signals.PROFILE_MISSING, {"signal_id": "rapport_delta", "profile_id": "coherence_bp_v1", "state": "dominance"},
    )


def test_signals_refuse_an_unknown_channel(v2_bundle, kernel) -> None:
    def mutate(configuration):
        _row(configuration["signals"], "signal_id", "rapport_delta")["channels"][0]["channel_id"] = "01-02"
    error = _refusal(compute_signals, kernel, _with_configuration(v2_bundle, mutate))
    assert (error.code, error.details) == (
        signals.CHANNEL_UNKNOWN, {"signal_id": "rapport_delta", "channel_id": "01-02"},
    )


@pytest.mark.parametrize("weight", [0, True], ids=["zero", "bool"])
def test_signals_refuse_an_invalid_weight(v2_bundle, kernel, weight) -> None:
    def mutate(configuration):
        _row(configuration["signals"], "signal_id", "rapport_delta")["channels"][0]["weight"] = weight
    error = _refusal(compute_signals, kernel, _with_configuration(v2_bundle, mutate))
    assert (error.code, error.details) == (
        signals.WEIGHT_INVALID, {"signal_id": "rapport_delta", "channel_id": "19-49"},
    )


# --- calculation.py --------------------------------------------------------------

@pytest.mark.parametrize(
    "release_id",
    [RELEASE_ID.upper(), RELEASE_ID[:63], RELEASE_ID.encode("ascii"), None],
    ids=["uppercase", "63-digits", "bytes", "none"],
)
def test_calculation_refuses_an_invalid_release_id(v2_bundle, masks, release_id) -> None:
    error = _refusal(compute_magic10_v2, *masks, v2_bundle, release_id)
    assert (error.code, error.details) == (calculation.RELEASE_ID_INVALID, {"argument": "release_id"})
    assert str(release_id) not in str(error)


@pytest.mark.parametrize(
    "mutate, component",
    [
        (lambda c: c.pop("center_map"), "configuration.center_map"),
        (lambda c: c.pop("center_profiles"), "configuration.center_profiles"),
        (lambda c: c.pop("blend"), "configuration.blend"),
        (lambda c: c.__setitem__("response_scale", 0), "configuration.response_scale"),
        (lambda c: c.__setitem__("config_id", "m10-channel-state-v1.0.0"), "configuration.config_id"),
        (lambda c: c.__setitem__("result_schema", "magic10_result.v1"), "configuration.result_schema"),
    ],
    ids=["no-center-map", "no-center-profiles", "no-blend", "response-scale-zero", "v1-config-id", "v1-result-schema"],
)
def test_calculation_refuses_an_incomplete_bundle(v2_bundle, masks, mutate, component) -> None:
    error = _refusal(compute_magic10_v2, *masks, _with_configuration(v2_bundle, mutate), RELEASE_ID)
    assert (error.code, error.details) == (calculation.BUNDLE_INCOMPLETE, {"component": component})


def test_calculation_refuses_a_bundle_of_the_wrong_type(masks) -> None:
    error = _refusal(compute_magic10_v2, *masks, None, RELEASE_ID)
    assert (error.code, error.details) == (calculation.BUNDLE_INCOMPLETE, {"component": "bundle"})


def test_calculation_refuses_missing_signal_rows_or_centers(v2_bundle, masks) -> None:
    error = _refusal(compute_magic10_v2, *masks, _with_configuration(v2_bundle, lambda c: c.pop("signals")), RELEASE_ID)
    assert (error.code, error.details) == (calculation.BUNDLE_INCOMPLETE, {"component": "configuration.signals"})
    error = _refusal(compute_magic10_v2, *masks, dataclasses.replace(v2_bundle, centers=None), RELEASE_ID)
    assert (error.code, error.details) == (calculation.BUNDLE_INCOMPLETE, {"component": "centers"})


def test_calculation_refuses_caps_inputs_that_are_not_configuration_signals(v2_bundle, masks) -> None:
    def rename(configuration):
        _row(configuration["signals"], "signal_id", "rapport_delta")["signal_id"] = "rapport_delta_v2"
    error = _refusal(compute_magic10_v2, *masks, _with_configuration(v2_bundle, rename), RELEASE_ID)
    assert (error.code, error.details) == (
        calculation.BUNDLE_INCOMPLETE, {"component": "registry.magic10_caps", "category_id": "harmony"},
    )


def _rename_heat_key(configuration):
    weights = _row(configuration["center_map"], "category_id", "heat")["weights"]
    weights["throat_motor"] = weights.pop("motor_throat")


def _drop_drive(configuration):
    configuration["center_map"] = [row for row in configuration["center_map"] if row["category_id"] != "drive"]


@pytest.mark.parametrize(
    "mutate, details",
    [
        (_rename_heat_key, {"category_id": "heat", "key": "throat_motor"}),
        (lambda c: _row(c["center_map"], "category_id", "drive")["weights"].__setitem__("root", 0),
         {"category_id": "drive", "key": "root"}),
        (_drop_drive, {"category_id": "drive", "key": None}),
        (lambda c: _row(c["center_map"], "category_id", "balance")["weights"].__setitem__("g", 1),
         {"category_id": "balance", "key": "g"}),
        (lambda c: _row(c["center_map"], "category_id", "harmony").__setitem__("weights", {}),
         {"category_id": "harmony", "key": None}),
    ],
    ids=["unknown-key", "weight-zero", "no-row", "balance-weight", "no-weight"],
)
def test_calculation_refuses_an_invalid_center_map(v2_bundle, masks, mutate, details) -> None:
    error = _refusal(compute_magic10_v2, *masks, _with_configuration(v2_bundle, mutate), RELEASE_ID)
    assert (error.code, error.details) == (calculation.CENTER_MAP_INVALID, details)


def test_calculation_refuses_a_missing_center_profile_or_response(v2_bundle, masks) -> None:
    def rename(configuration):
        _row(configuration["center_map"], "category_id", "harmony")["profile_id"] = "completion_bp_v3"
    bundle = _with_configuration(v2_bundle, rename)
    error = _refusal(compute_magic10_v2, *masks, bundle, RELEASE_ID)
    assert (error.code, error.details) == (
        calculation.CENTER_PROFILE_MISSING, {"category_id": "harmony", "profile_id": "completion_bp_v3"},
    )
    bundle = _with_configuration(
        v2_bundle, lambda c: _row(c["center_profiles"], "profile_id", "completion_bp_v2")["responses"].pop("mutual")
    )
    error = _refusal(compute_magic10_v2, *masks, bundle, RELEASE_ID)
    assert (error.code, error.details) == (
        calculation.CENTER_PROFILE_MISSING,
        {"category_id": "harmony", "profile_id": "completion_bp_v2", "outcome": "mutual"},
    )


def _type_pairing(bundle, mutate):
    offsets = {rule: dict(row) for rule, row in bundle.type_pairing.items()}
    mutate(offsets)
    return dataclasses.replace(
        bundle, type_pairing=MappingProxyType({rule: MappingProxyType(row) for rule, row in offsets.items()})
    )


@pytest.mark.parametrize(
    "mutate, details",
    [
        (lambda t: t.pop("generator_projector"), {"rule_id": "generator_projector", "category_id": None}),
        (lambda t: t.__setitem__("manifestor_reflector", dict(t["same_class"])),
         {"rule_id": "manifestor_reflector", "category_id": None}),
        (lambda t: t["generator_projector"].pop("alignment"),
         {"rule_id": "generator_projector", "category_id": "alignment"}),
    ],
    ids=["missing-rule", "unknown-rule", "missing-cell"],
)
def test_calculation_refuses_invalid_type_pairing(v2_bundle, masks, mutate, details) -> None:
    error = _refusal(compute_magic10_v2, *masks, _type_pairing(v2_bundle, mutate), RELEASE_ID)
    assert (error.code, error.details) == (calculation.TYPE_PAIRING_INVALID, details)


def _maxima(bundle, mutate):
    maxima = dict(bundle.maxima)
    mutate(maxima)
    return dataclasses.replace(bundle, maxima=MappingProxyType(maxima))


@pytest.mark.parametrize(
    "mutate, category",
    [
        (lambda m: m.pop("balance"), "balance"),
        (lambda m: m.__setitem__("harmony", (24, 49, 74, 99)), "harmony"),
        (lambda m: m.__setitem__("harmony", (49, 24, 74, 100)), "harmony"),
    ],
    ids=["missing", "not-ending-100", "not-ascending"],
)
def test_calculation_refuses_invalid_maxima(v2_bundle, masks, mutate, category) -> None:
    error = _refusal(compute_magic10_v2, *masks, _maxima(v2_bundle, mutate), RELEASE_ID)
    assert (error.code, error.details) == (calculation.MAXIMA_INVALID, {"category_id": category})


def test_components_refuse_wrong_kernel_or_signals(v2_bundle, kernel) -> None:
    values = compute_signals(kernel, v2_bundle)
    error = _refusal(compute_category_components, None, values, v2_bundle)
    assert (error.code, error.details) == (calculation.INPUT_INVALID, {"argument": "kernel"})
    error = _refusal(compute_category_components, kernel, values[1:], v2_bundle)
    assert (error.code, error.details) == (calculation.INPUT_INVALID, {"argument": "signals"})


def test_kernel_refusals_propagate_and_release_id_is_checked_first(v2_bundle, mask_of) -> None:
    error = _refusal(compute_magic10_v2, 0, mask_of(2), v2_bundle, RELEASE_ID)
    assert (error.code, error.details) == (MASK_OUT_OF_DOMAIN, {"argument": "mask_a"})
    error = _refusal(compute_magic10_v2, 0, mask_of(2), v2_bundle, "x")
    assert error.code == calculation.RELEASE_ID_INVALID
