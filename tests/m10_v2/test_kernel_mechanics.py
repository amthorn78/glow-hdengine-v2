"""HDE-EPIC043 WU-PR-01 acceptance 1 and 2: member mechanics, outcomes and derived Type.

Constructed Gate sets (real-domain masks from the repository's Gate normalizer)
cover every derived Type and aura class, ``motor_to_throat`` true and false
(including a motor reaching ``throat`` only through another center, and a motor
disconnected from ``throat``), and each center and motor→Throat outcome with
each owner. Every result is checked for (A, B) and (B, A).

Expectations are transcribed from HDE Math Spec §5.2.11 (evaluation order steps
1 to 5, Type derivation, center outcomes) and from the repository's governed
topology (``catalog/gates_v1.json``, ``catalog/channels_v1.json``,
``catalog/centers_v1.json``), not read back from the module under test.
"""
from __future__ import annotations

import dataclasses
import inspect
import json
import sys
from pathlib import Path

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.magic10_v2.kernel import compute_kernel

ROOT = Path(__file__).resolve().parents[2]
CENTER_ORDER = ("ajna", "ego", "g", "head", "root", "sacral", "solar_plexus", "spleen", "throat")

# (case id, Gates of A, role of A's member, derived Type, aura class,
#  motor_to_throat, complete Channels, defined centers, definition components).
# B is always the single-Gate set {2}, a Reflector.
TYPE_CASES = (
    ("reflector", (1,), "member_lo", "Reflector", "reflector", False, (), (), ()),
    ("projector", (1, 8), "member_hi", "Projector", "projector", False,
     ("01-08",), ("g", "throat"), (("g", "throat"),)),
    ("manifesting_generator", (20, 34), "member_hi", "Manifesting Generator", "generator", True,
     ("20-34",), ("sacral", "throat"), (("sacral", "throat"),)),
    ("generator_disconnected_motor", (1, 8, 3, 60), "member_hi", "Generator", "generator", False,
     ("01-08", "03-60"), ("g", "root", "sacral", "throat"), (("g", "throat"), ("root", "sacral"))),
    ("manifestor_direct", (21, 45), "member_hi", "Manifestor", "manifestor", True,
     ("21-45",), ("ego", "throat"), (("ego", "throat"),)),
    ("manifestor_any_route", (20, 57, 32, 54), "member_hi", "Manifestor", "manifestor", True,
     ("20-57", "32-54"), ("root", "spleen", "throat"), (("root", "spleen", "throat"),)),
)

# (case id, Gates of A, Gates of B, non-open center outcomes, motor→Throat outcome).
OUTCOME_CASES = (
    ("all_open", (1,), (2,), {}, ("open", None)),
    ("mutual", (1, 20), (8, 34),
     {"g": ("mutual", None), "sacral": ("mutual", None), "throat": ("mutual", None)}, ("mutual", None)),
    ("shared", (20, 34), (1, 20, 34),
     {"sacral": ("shared", None), "throat": ("shared", None)}, ("shared", None)),
    ("one_sided_both_owners", (1, 8), (20, 34),
     {"g": ("one_sided", "member_lo"), "sacral": ("one_sided", "member_hi"), "throat": ("shared", None)},
     ("one_sided", "member_hi")),
    ("one_sided_motor_throat_member_lo", (20, 34), (47, 64),
     {"ajna": ("one_sided", "member_hi"), "head": ("one_sided", "member_hi"),
      "sacral": ("one_sided", "member_lo"), "throat": ("one_sided", "member_lo")},
     ("one_sided", "member_lo")),
)


def _both_orders(bundle, mask_a: int, mask_b: int):
    result = compute_kernel(mask_a, mask_b, bundle)
    assert result == compute_kernel(mask_b, mask_a, bundle)
    return result


@pytest.mark.parametrize("case", TYPE_CASES, ids=[case[0] for case in TYPE_CASES])
def test_derived_type_and_member_mechanics(v2_bundle, mask_of, case) -> None:
    _, gates, role, derived_type, aura_class, motor_to_throat, complete, defined, components = case
    result = _both_orders(v2_bundle, mask_of(*gates), mask_of(2))
    member = getattr(result, role)
    assert member.derived_type == derived_type
    assert member.aura_class == aura_class
    assert member.motor_to_throat is motor_to_throat
    assert member.complete_channels == complete
    assert member.defined_centers == defined
    assert member.definition_components == components
    other = result.member_hi if role == "member_lo" else result.member_lo
    assert (other.derived_type, other.aura_class, other.motor_to_throat) == ("Reflector", "reflector", False)
    assert (other.complete_channels, other.defined_centers, other.definition_components) == ((), (), ())


def test_type_cases_cover_every_type_aura_class_and_predicate_value() -> None:
    assert {case[3] for case in TYPE_CASES} == {
        "Reflector", "Generator", "Manifesting Generator", "Manifestor", "Projector",
    }
    assert {case[4] for case in TYPE_CASES} == {"generator", "projector", "manifestor", "reflector"}
    assert {case[5] for case in TYPE_CASES} == {True, False}


@pytest.mark.parametrize("case", OUTCOME_CASES, ids=[case[0] for case in OUTCOME_CASES])
def test_center_and_motor_throat_outcomes(v2_bundle, mask_of, case) -> None:
    _, gates_a, gates_b, non_open, motor_throat = case
    result = _both_orders(v2_bundle, mask_of(*gates_a), mask_of(*gates_b))
    assert tuple(outcome.center_id for outcome in result.centers) == CENTER_ORDER
    for outcome in result.centers:
        expected = non_open.get(outcome.center_id, ("open", None))
        assert (outcome.outcome, outcome.owner) == expected, outcome.center_id
    assert (result.motor_throat.outcome, result.motor_throat.owner) == motor_throat


def test_outcome_cases_cover_each_outcome_and_owner() -> None:
    seen = {pair for case in OUTCOME_CASES for pair in case[3].values()} | {("open", None)}
    assert seen == {("open", None), ("shared", None), ("mutual", None),
                    ("one_sided", "member_lo"), ("one_sided", "member_hi")}
    assert {case[4] for case in OUTCOME_CASES} == seen


def test_union_mechanics_when_only_the_union_defines_centers(v2_bundle, mask_of) -> None:
    result = _both_orders(v2_bundle, mask_of(1, 20), mask_of(8, 34))
    assert result.union.defined_centers == ("g", "sacral", "throat")
    assert result.union.motor_to_throat is True
    assert result.member_lo.derived_type == result.member_hi.derived_type == "Reflector"


def test_member_lo_owns_a_dominance_channel_when_its_mask_is_lower(v2_bundle, mask_of) -> None:
    result = _both_orders(v2_bundle, mask_of(20, 34), mask_of(47, 64))
    owned = {(entry.channel_id, entry.state, entry.owner) for entry in result.channels if entry.owner}
    assert owned == {("20-34", "dominance", "member_lo"), ("47-64", "dominance", "member_hi")}


def test_equal_masks_are_two_equal_members(v2_bundle, mask_of) -> None:
    mask = mask_of(1, 8)
    result = compute_kernel(mask, mask, v2_bundle)
    assert {entry.state for entry in result.channels} == {"none", "companionship"}
    assert result.member_lo == result.member_hi
    assert {(outcome.center_id, outcome.outcome) for outcome in result.centers if outcome.outcome != "open"} == {
        ("g", "shared"), ("throat", "shared"),
    }
    assert all(outcome.owner is None for outcome in result.centers)
    assert (result.motor_throat.outcome, result.motor_throat.owner) == ("open", None)


def test_derived_type_ignores_a_contradicting_stored_vendor_type(v2_bundle, mask_of) -> None:
    """Acceptance 2: the governed chart fixture bob.json stores ``Projector``; its Gate set derives otherwise."""
    chart = json.loads((ROOT / "fixtures/charts/bob.json").read_bytes())
    bob_mask = normalize_gates(chart["bodygraph"]["gates"]).mask
    result = _both_orders(v2_bundle, bob_mask, mask_of(2))
    assert chart["bodygraph"]["type"] == "Projector"
    assert result.member_hi.derived_type == "Manifesting Generator"
    assert result.member_hi.defined_centers == ("ajna", "head", "root", "sacral", "solar_plexus", "throat")
    assert result.member_hi.motor_to_throat is True
    assert list(inspect.signature(compute_kernel).parameters) == ["mask_a", "mask_b", "bundle"]


_OPENED: list[str] = []
_RECORDING = [False]
_HOOK_INSTALLED = [False]


def _record_open(event: str, args: tuple) -> None:
    if _RECORDING[0] and event == "open":
        _OPENED.append(str(args[0]))


def _tuples_all_the_way_down(value) -> bool:
    if dataclasses.is_dataclass(value):
        return all(_tuples_all_the_way_down(getattr(value, field.name)) for field in dataclasses.fields(value))
    if isinstance(value, (list, dict, set)):
        return False
    if isinstance(value, tuple):
        return all(_tuples_all_the_way_down(item) for item in value)
    return True


def test_kernel_is_pure_deterministic_and_immutable(v2_bundle, mask_of) -> None:
    if not _HOOK_INSTALLED[0]:
        sys.addaudithook(_record_open)
        _HOOK_INSTALLED[0] = True
    mask_a, mask_b = mask_of(1, 8, 20, 57, 32, 54), mask_of(3, 60, 21, 45, 47, 64)
    _OPENED.clear()
    _RECORDING[0] = True
    try:
        first = compute_kernel(mask_a, mask_b, v2_bundle)
        second = compute_kernel(mask_a, mask_b, v2_bundle)
    finally:
        _RECORDING[0] = False
    assert _OPENED == []
    assert first == second
    assert _tuples_all_the_way_down(first)
    with pytest.raises(dataclasses.FrozenInstanceError):
        first.member_lo = first.member_hi  # type: ignore[misc]


def test_domain_boundary_masks_are_accepted(v2_bundle, mask_of) -> None:
    assert mask_of(1) == 1
    assert mask_of(64) == 1 << 63
    assert mask_of(*range(1, 65)) == (1 << 64) - 1
    compute_kernel(mask_of(1), mask_of(64), v2_bundle)
    compute_kernel(mask_of(*range(1, 65)), mask_of(1), v2_bundle)
