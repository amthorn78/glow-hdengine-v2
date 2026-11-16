"""HDE-EPIC043 WU-PR-01 acceptance 3: fail-closed refusals with stable codes (HDE-CONJ010.1).

HDE Math Spec §5.2.1 and §5.2.11: complete-or-fail-closed. Each case is one
input outside the real set and receives one refusal: a ``SchemaValidationError``
with its stable code and details, and no result.

* Masks: the §5.2.1 domain is an ``int`` with ``1 <= mask < 2**64``; ``bool`` is
  excluded although Python treats it as ``int``. The non-``int`` case is the
  16-digit hex text the normalizer produces as ``mask_hex``.
* Bundle: an admitted bundle cannot trigger these refusals (the centers schema
  fixes the nine center IDs, the loader fixes the four motors and refuses an
  unknown Channel center). Each bundle case is therefore one component of the
  admitted bundle replaced, the bundle object a caller could construct without
  the loader.
"""
from __future__ import annotations

import dataclasses
from types import MappingProxyType

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2.kernel import (
    AURA_CLASS_UNKNOWN,
    BUNDLE_INCOMPLETE,
    CENTER_UNKNOWN,
    CENTERS_INCOMPLETE,
    MASK_OUT_OF_DOMAIN,
    compute_kernel,
)


def _refusal(mask_a: object, mask_b: object, bundle: object) -> SchemaValidationError:
    result = None
    with pytest.raises(SchemaValidationError) as caught:
        result = compute_kernel(mask_a, mask_b, bundle)  # type: ignore[arg-type]
    assert result is None
    return caught.value


def test_refusal_codes_are_stable() -> None:
    assert (MASK_OUT_OF_DOMAIN, CENTER_UNKNOWN, CENTERS_INCOMPLETE, AURA_CLASS_UNKNOWN, BUNDLE_INCOMPLETE) == (
        "M10V2_KERNEL_MASK_OUT_OF_DOMAIN",
        "M10V2_KERNEL_CENTER_UNKNOWN",
        "M10V2_KERNEL_CENTERS_INCOMPLETE",
        "M10V2_KERNEL_AURA_CLASS_UNKNOWN",
        "M10V2_KERNEL_BUNDLE_INCOMPLETE",
    )


OUT_OF_DOMAIN = (
    ("mask_hex_text", normalize_gates([1, 8]).mask_hex),
    ("bool", True),
    ("zero", 0),
    ("negative", -1),
    ("two_to_the_64", 1 << 64),
)


@pytest.mark.parametrize("argument", ("mask_a", "mask_b"))
@pytest.mark.parametrize("value", [case[1] for case in OUT_OF_DOMAIN], ids=[case[0] for case in OUT_OF_DOMAIN])
def test_mask_outside_the_domain_is_refused(v2_bundle, mask_of, argument: str, value: object) -> None:
    good = mask_of(1, 8)
    masks = (value, good) if argument == "mask_a" else (good, value)
    error = _refusal(*masks, v2_bundle)
    assert error.code == MASK_OUT_OF_DOMAIN
    assert error.details == {"argument": argument}


def test_channel_center_absent_from_the_centers_catalog_is_refused(v2_bundle, mask_of) -> None:
    centers = MappingProxyType({key: value for key, value in v2_bundle.centers.items() if key != "spleen"})
    error = _refusal(mask_of(1, 8), mask_of(20, 34), dataclasses.replace(v2_bundle, centers=centers))
    assert error.code == CENTER_UNKNOWN
    assert error.details == {"channel_id": "10-57", "center_id": "spleen"}


def test_centers_catalog_without_throat_is_refused(v2_bundle, mask_of) -> None:
    centers = MappingProxyType({key: value for key, value in v2_bundle.centers.items() if key != "throat"})
    error = _refusal(mask_of(1, 8), mask_of(20, 34), dataclasses.replace(v2_bundle, centers=centers))
    assert error.code == CENTERS_INCOMPLETE
    assert error.details == {"missing": "throat"}


def test_centers_catalog_without_a_motor_is_refused(v2_bundle, mask_of) -> None:
    centers = MappingProxyType({key: False for key in v2_bundle.centers})
    error = _refusal(mask_of(1, 8), mask_of(20, 34), dataclasses.replace(v2_bundle, centers=centers))
    assert error.code == CENTERS_INCOMPLETE
    assert error.details == {"missing": "motor"}


def test_derived_aura_class_absent_from_the_bundle_is_refused(v2_bundle, mask_of) -> None:
    aura_classes = tuple(name for name in v2_bundle.aura_classes if name != "manifestor")
    error = _refusal(mask_of(21, 45), mask_of(2), dataclasses.replace(v2_bundle, aura_classes=aura_classes))
    assert error.code == AURA_CLASS_UNKNOWN
    assert error.details == {"aura_class": "manifestor"}


def _without(bundle, component: str):
    if component == "bundle":
        return None
    if component == "registry.channels":
        return dataclasses.replace(bundle, registry=dataclasses.replace(bundle.registry, channels=MappingProxyType({})))
    if component == "centers":
        return dataclasses.replace(bundle, centers=MappingProxyType({}))
    return dataclasses.replace(bundle, aura_classes=())


@pytest.mark.parametrize("component", ("bundle", "registry.channels", "centers", "aura_classes"))
def test_missing_bundle_component_is_refused(v2_bundle, mask_of, component: str) -> None:
    error = _refusal(mask_of(1, 8), mask_of(20, 34), _without(v2_bundle, component))
    assert error.code == BUNDLE_INCOMPLETE
    assert error.details == {"component": component}
