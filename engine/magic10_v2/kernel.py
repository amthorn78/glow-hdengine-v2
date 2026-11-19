"""Magic10 v2 kernel (HDE-CONJ010.1; HDE-EPIC043 WU-PR-01).

HDE Math Spec §5.2.11, evaluation order steps 1 to 5: from two gate masks and an
admitted v2 bundle, compute the 36 Channel states with owners, each member's
complete Channels, defined centers, definition components, any-route
``motor_to_throat`` predicate and derived Type, the union's defined centers and
``motor_to_throat`` predicate, and the outcome of each of the nine centers and of
motor→Throat.

* Inputs are the two masks and the bundle only. Nothing else is read from the
  stored chart, including the stored vendor ``type``; no file, environment,
  clock or global state is read.
* Arithmetic is integer and bit operations only; no binary floating point.
* Every order is fixed by the bundle's registry or centers catalog, never by
  argument order, so the result for (A, B) equals the result for (B, A).
* A missing center, class or governed input fails closed with a
  ``SchemaValidationError`` carrying a stable code; nothing is defaulted.

Stated limits: the kernel trusts the topology an admitted bundle carries
(36 Channels, ascending in-range Gate pairs, two distinct centers each) as the
v2 loader validated it, and applies no eligibility rule (HDE Math Spec §4 is
applied upstream). Signals, components, scores, bands, ``pair_key`` and
``gives_lo`` / ``gives_hi`` are not computed here (HDE-CONJ010.2 and .3).

Reached from production since the switch (HDE-EPIC043 WU-PR-09), through the
engine core; its last top-level statement records passive execution provenance
for release admission.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

from engine.config.magic10_v2_loader import Magic10V2Bundle
from engine.config.registry_loader import SchemaValidationError, _capture_module_execution

CHANNEL_STATES = ("none", "companionship", "dominance", "compromise", "electromagnetic")
CENTER_OUTCOMES = ("open", "shared", "one_sided", "mutual")
MEMBERS = ("member_lo", "member_hi")
DERIVED_TYPES = ("Reflector", "Generator", "Manifesting Generator", "Manifestor", "Projector")
# HDE Math Spec §5.2.11, Type derivation: the four aura classes.
AURA_CLASS_BY_TYPE = MappingProxyType({
    "Reflector": "reflector",
    "Generator": "generator",
    "Manifesting Generator": "generator",
    "Manifestor": "manifestor",
    "Projector": "projector",
})

_THROAT = "throat"
_SACRAL = "sacral"
_MASK_LIMIT = 1 << 64

MASK_OUT_OF_DOMAIN = "M10V2_KERNEL_MASK_OUT_OF_DOMAIN"
CENTER_UNKNOWN = "M10V2_KERNEL_CENTER_UNKNOWN"
CENTERS_INCOMPLETE = "M10V2_KERNEL_CENTERS_INCOMPLETE"
AURA_CLASS_UNKNOWN = "M10V2_KERNEL_AURA_CLASS_UNKNOWN"
BUNDLE_INCOMPLETE = "M10V2_KERNEL_BUNDLE_INCOMPLETE"


@dataclass(frozen=True, slots=True)
class ChannelState:
    """One Channel's five-state classification; ``owner`` only for dominance and compromise."""

    channel_id: str
    state: str
    owner: str | None


@dataclass(frozen=True, slots=True)
class MemberMechanics:
    """One member's mechanics, computed from its Gate set only."""

    complete_channels: tuple[str, ...]
    defined_centers: tuple[str, ...]
    definition_components: tuple[tuple[str, ...], ...]
    motor_to_throat: bool
    derived_type: str
    aura_class: str


@dataclass(frozen=True, slots=True)
class UnionMechanics:
    """The union mask's defined centers and ``motor_to_throat`` predicate."""

    defined_centers: tuple[str, ...]
    motor_to_throat: bool


@dataclass(frozen=True, slots=True)
class CenterOutcome:
    """One center's outcome; ``owner`` only when the outcome is ``one_sided``."""

    center_id: str
    outcome: str
    owner: str | None


@dataclass(frozen=True, slots=True)
class MotorThroatOutcome:
    """The motor→Throat outcome; ``owner`` only when the outcome is ``one_sided``."""

    outcome: str
    owner: str | None


@dataclass(frozen=True, slots=True)
class KernelResult:
    """The kernel's complete output for one pair (HDE Math Spec §5.2.11 steps 1 to 5)."""

    channels: tuple[ChannelState, ...]
    member_lo: MemberMechanics
    member_hi: MemberMechanics
    union: UnionMechanics
    centers: tuple[CenterOutcome, ...]
    motor_throat: MotorThroatOutcome


@dataclass(frozen=True, slots=True)
class _MaskMechanics:
    complete_channels: tuple[str, ...]
    defined_centers: tuple[str, ...]
    definition_components: tuple[tuple[str, ...], ...]
    motor_to_throat: bool


def compute_kernel(mask_a: int, mask_b: int, bundle: Magic10V2Bundle) -> KernelResult:
    """Compute the v2 kernel outputs for two gate masks over an admitted v2 bundle.

    Refusals (``SchemaValidationError``), checked in this order before any result
    exists: ``M10V2_KERNEL_BUNDLE_INCOMPLETE``, ``M10V2_KERNEL_CENTERS_INCOMPLETE``,
    ``M10V2_KERNEL_CENTER_UNKNOWN``, ``M10V2_KERNEL_MASK_OUT_OF_DOMAIN``; then
    ``M10V2_KERNEL_AURA_CLASS_UNKNOWN`` when a member's derived aura class is not
    one of the bundle's aura classes.
    """
    channels, centers, aura_classes = _bundle_inputs(bundle)
    center_order = tuple(centers)
    _check_centers(centers)
    _check_channel_centers(channels, centers)
    _check_mask(mask_a, "mask_a")
    _check_mask(mask_b, "mask_b")

    # Step 1: order the masks numerically; equal masks stay two equal members.
    mask_lo, mask_hi = (mask_a, mask_b) if mask_a <= mask_b else (mask_b, mask_a)
    # Step 2: the v1 five-state classifier, restated (HDE Math Spec §6.1).
    states = tuple(_classify_channel(channel, mask_lo, mask_hi) for channel in channels)
    # Steps 3 and 4: per member and for the union mask.
    lo = _mask_mechanics(mask_lo, channels, centers, center_order)
    hi = _mask_mechanics(mask_hi, channels, centers, center_order)
    union = _mask_mechanics(mask_lo | mask_hi, channels, centers, center_order)
    member_lo = _member(lo, aura_classes)
    member_hi = _member(hi, aura_classes)
    # Step 5: center outcomes and the motor→Throat outcome.
    lo_defined = frozenset(lo.defined_centers)
    hi_defined = frozenset(hi.defined_centers)
    union_defined = frozenset(union.defined_centers)
    center_outcomes = tuple(
        CenterOutcome(center, *_outcome(center in lo_defined, center in hi_defined, center in union_defined))
        for center in center_order
    )
    motor_throat = MotorThroatOutcome(*_outcome(lo.motor_to_throat, hi.motor_to_throat, union.motor_to_throat))
    return KernelResult(
        channels=states,
        member_lo=member_lo,
        member_hi=member_hi,
        union=UnionMechanics(union.defined_centers, union.motor_to_throat),
        centers=center_outcomes,
        motor_throat=motor_throat,
    )


def _bundle_inputs(bundle: object) -> tuple[tuple, Mapping, tuple[str, ...]]:
    """Return the three bundle components the kernel reads, or refuse a missing one."""
    if type(bundle) is not Magic10V2Bundle:
        raise SchemaValidationError(
            BUNDLE_INCOMPLETE, "the kernel requires an admitted Magic10V2Bundle", {"component": "bundle"}
        )
    registry_channels = getattr(bundle.registry, "channels", None)
    if not isinstance(registry_channels, Mapping) or not registry_channels:
        raise SchemaValidationError(
            BUNDLE_INCOMPLETE, "bundle registry has no Channels", {"component": "registry.channels"}
        )
    if not isinstance(bundle.centers, Mapping) or not bundle.centers:
        raise SchemaValidationError(BUNDLE_INCOMPLETE, "bundle has no centers catalog", {"component": "centers"})
    if type(bundle.aura_classes) is not tuple or not bundle.aura_classes:
        raise SchemaValidationError(BUNDLE_INCOMPLETE, "bundle has no aura classes", {"component": "aura_classes"})
    return tuple(registry_channels.values()), bundle.centers, bundle.aura_classes


def _check_centers(centers: Mapping) -> None:
    if _THROAT not in centers:
        raise SchemaValidationError(CENTERS_INCOMPLETE, "centers catalog has no throat", {"missing": "throat"})
    if not any(centers[center] is True for center in centers):
        raise SchemaValidationError(CENTERS_INCOMPLETE, "centers catalog has no motor", {"missing": "motor"})


def _check_channel_centers(channels: tuple, centers: Mapping) -> None:
    for channel in channels:
        for center in channel.centers:
            if center not in centers:
                raise SchemaValidationError(
                    CENTER_UNKNOWN,
                    "a Channel endpoint center is absent from the centers catalog",
                    {"channel_id": channel.id, "center_id": center},
                )


def _check_mask(mask: object, argument: str) -> None:
    """HDE Math Spec §5.2.1: an unsigned 64-bit mask of a nonempty Gate set."""
    if type(mask) is not int or mask <= 0 or mask >= _MASK_LIMIT:
        raise SchemaValidationError(
            MASK_OUT_OF_DOMAIN,
            "a gate mask must be an int with 1 <= mask < 2^64",
            {"argument": argument},
        )


def _bit(mask: int, gate: int) -> int:
    return (mask >> (gate - 1)) & 1


def _classify_channel(channel, mask_lo: int, mask_hi: int) -> ChannelState:
    """The v1 five-state rule (HDE Math Spec §6.1) over numerically ordered masks."""
    gate_x, gate_y = channel.gates
    lo_x, lo_y = _bit(mask_lo, gate_x), _bit(mask_lo, gate_y)
    hi_x, hi_y = _bit(mask_hi, gate_x), _bit(mask_hi, gate_y)
    lo = lo_x + lo_y
    hi = hi_x + hi_y
    if lo == 2 and hi == 2:
        return ChannelState(channel.id, "companionship", None)
    if lo == 2 or hi == 2:
        state = "compromise" if min(lo, hi) == 1 else "dominance"
        return ChannelState(channel.id, state, "member_lo" if lo == 2 else "member_hi")
    if lo == 1 and hi == 1 and lo_x != hi_x:
        return ChannelState(channel.id, "electromagnetic", None)
    return ChannelState(channel.id, "none", None)


def _mask_mechanics(mask: int, channels: tuple, centers: Mapping, center_order: tuple[str, ...]) -> _MaskMechanics:
    """Complete Channels, defined centers, definition components and ``motor_to_throat``."""
    complete = tuple(
        channel for channel in channels
        if _bit(mask, channel.gates[0]) and _bit(mask, channel.gates[1])
    )
    defined = frozenset(center for channel in complete for center in channel.centers)
    # Connected components of the graph: nodes are the defined centers, edges the
    # complete Channels (each joins its two centers).
    neighbours = {center: set() for center in defined}
    for channel in complete:
        first, second = channel.centers
        neighbours[first].add(second)
        neighbours[second].add(first)
    component_of: dict[str, int] = {}
    components: list[tuple[str, ...]] = []
    for start in center_order:
        if start not in defined or start in component_of:
            continue
        members = {start}
        frontier = [start]
        while frontier:
            current = frontier.pop()
            for neighbour in neighbours[current]:
                if neighbour not in members:
                    members.add(neighbour)
                    frontier.append(neighbour)
        for member in members:
            component_of[member] = len(components)
        components.append(tuple(center for center in center_order if center in members))
    motor_to_throat = _THROAT in defined and any(
        centers[center] is True and component_of[center] == component_of[_THROAT]
        for center in defined
    )
    return _MaskMechanics(
        complete_channels=tuple(channel.id for channel in complete),
        defined_centers=tuple(center for center in center_order if center in defined),
        definition_components=tuple(components),
        motor_to_throat=motor_to_throat,
    )


def _member(mechanics: _MaskMechanics, aura_classes: tuple[str, ...]) -> MemberMechanics:
    """HDE Math Spec §5.2.11, Type derivation, per member from the Gate set only."""
    defined = mechanics.defined_centers
    if not defined:
        derived_type = "Reflector"
    elif _SACRAL in defined:
        derived_type = "Manifesting Generator" if mechanics.motor_to_throat else "Generator"
    else:
        derived_type = "Manifestor" if mechanics.motor_to_throat else "Projector"
    aura_class = AURA_CLASS_BY_TYPE[derived_type]
    if aura_class not in aura_classes:
        raise SchemaValidationError(
            AURA_CLASS_UNKNOWN, "the derived aura class is absent from the bundle", {"aura_class": aura_class}
        )
    return MemberMechanics(
        complete_channels=mechanics.complete_channels,
        defined_centers=defined,
        definition_components=mechanics.definition_components,
        motor_to_throat=mechanics.motor_to_throat,
        derived_type=derived_type,
        aura_class=aura_class,
    )


def _outcome(in_lo: bool, in_hi: bool, in_union: bool) -> tuple[str, str | None]:
    """HDE Math Spec §5.2.11, center outcomes; the same rule serves motor→Throat."""
    if not in_union:
        return "open", None
    if in_lo and in_hi:
        return "shared", None
    if in_lo:
        return "one_sided", "member_lo"
    if in_hi:
        return "one_sided", "member_hi"
    return "mutual", None


# HDE-EPIC043 WU-PR-09: passive provenance for release admission (last top-level statement).
_MODULE_EXECUTION = _capture_module_execution(globals())
