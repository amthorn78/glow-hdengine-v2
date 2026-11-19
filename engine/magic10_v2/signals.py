"""Magic10 v2 signal producers (HDE-CONJ010.2; HDE-EPIC043 WU-PR-02).

HDE Math Spec §5.2.11, evaluation step 6, "Signals": from the v2 kernel's 36
Channel states and owners and an admitted v2 bundle, compute the twenty
governed signals as integer per-mille values in ``0..1000``.

* The twenty signal IDs, their category pairs, the eighteen ordinary Channel
  maps and the response profiles are v1's; the operations are v2's. The
  eighteen ordinary signals use ``saturating_state_sum_v2``. The two Balance
  signals use ``bilateral_owner_mass_v2`` (``equilibrium_score``) and
  ``mutual_state_share_v2`` (``counterweight_ratio``) over all 36 Channels.
* Channel sets, weights, operation names, profile responses and
  ``saturation_k_bp`` are read from the bundle's configuration; none is a
  literal here. The output follows the configuration's signal order, which the
  v2 loader pins to the flattened ``catalog/magic10_caps.json`` pairs.
* Arithmetic is integer only: ``rhu`` uses floor division ``//``; no binary
  floating point is used.
* Inputs are the kernel result and the bundle only. No mask, file,
  environment, clock or global state is read.
* A missing or malformed component this module reads fails closed with a
  ``SchemaValidationError`` carrying a stable code; nothing is defaulted.

Stated limits: the kernel result is trusted to come from the same bundle (the
calculation passes one bundle to both), and ``rhu`` does not check its
arguments, because every caller in the package has ``N >= 0`` and ``D > 0`` by
construction.

Reached from production since the switch (HDE-EPIC043 WU-PR-09), through the
engine core; its last top-level statement records passive execution provenance
for release admission.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from engine.config.magic10_v2_loader import Magic10V2Bundle
from engine.config.registry_loader import SchemaValidationError, _capture_module_execution
from engine.magic10_v2.kernel import CHANNEL_STATES, KernelResult

# HDE Math Spec §5.2.11, "Integer arithmetic": signals and components are per-mille.
PER_MILLE = 1000

ORDINARY_OPERATION = "saturating_state_sum_v2"
OWNER_MASS_OPERATION = "bilateral_owner_mass_v2"
MUTUAL_SHARE_OPERATION = "mutual_state_share_v2"
_OPERATIONS = (ORDINARY_OPERATION, OWNER_MASS_OPERATION, MUTUAL_SHARE_OPERATION)

_OWNED_STATES = frozenset({"dominance", "compromise"})
_MUTUAL_STATES = frozenset({"companionship", "electromagnetic"})

INPUT_INVALID = "M10V2_SIGNALS_INPUT_INVALID"
BUNDLE_INCOMPLETE = "M10V2_SIGNALS_BUNDLE_INCOMPLETE"
OPERATION_UNKNOWN = "M10V2_SIGNALS_OPERATION_UNKNOWN"
PROFILE_MISSING = "M10V2_SIGNALS_PROFILE_MISSING"
CHANNEL_UNKNOWN = "M10V2_SIGNALS_CHANNEL_UNKNOWN"
WEIGHT_INVALID = "M10V2_SIGNALS_WEIGHT_INVALID"


@dataclass(frozen=True, slots=True)
class SignalValue:
    """One governed signal's integer per-mille value."""

    signal_id: str
    q: int


@dataclass(frozen=True, slots=True)
class _SignalRow:
    signal_id: str
    operation: str
    responses: Mapping[str, int] | None
    channels: tuple[tuple[str, int], ...]


def rhu(numerator: int, denominator: int) -> int:
    """HDE Math Spec §5.2.11: ``rhu(N, D) = floor((2N + D) / (2D))``.

    This is ``ROUND_HALF_UP`` for ``N >= 0`` and ``D > 0``; every caller in the
    package meets that by construction. Integer floor division only.
    """
    return (2 * numerator + denominator) // (2 * denominator)


def compute_signals(kernel: KernelResult, bundle: Magic10V2Bundle) -> tuple[SignalValue, ...]:
    """Compute the twenty v2 signals from a kernel result and an admitted v2 bundle.

    Refusals (``SchemaValidationError``), all checked before any value is
    computed, in this order: ``M10V2_SIGNALS_INPUT_INVALID``,
    ``M10V2_SIGNALS_BUNDLE_INCOMPLETE``, then per signal row
    ``M10V2_SIGNALS_OPERATION_UNKNOWN``, ``M10V2_SIGNALS_PROFILE_MISSING``,
    ``M10V2_SIGNALS_CHANNEL_UNKNOWN``, ``M10V2_SIGNALS_WEIGHT_INVALID``.
    """
    if type(kernel) is not KernelResult:
        raise SchemaValidationError(INPUT_INVALID, "signals require a KernelResult", {"argument": "kernel"})
    if type(bundle) is not Magic10V2Bundle:
        raise SchemaValidationError(
            INPUT_INVALID, "signals require an admitted Magic10V2Bundle", {"argument": "bundle"}
        )
    rows, saturation = _signal_rows(bundle, kernel)
    states = {channel.channel_id: channel for channel in kernel.channels}
    return tuple(SignalValue(row.signal_id, _signal_value(row, states, saturation)) for row in rows)


def _incomplete(component: str) -> SchemaValidationError:
    return SchemaValidationError(
        BUNDLE_INCOMPLETE, f"bundle configuration lacks a valid {component}", {"component": component}
    )


def _is_int(value: object) -> bool:
    return type(value) is int


def _signal_rows(bundle: Magic10V2Bundle, kernel: KernelResult) -> tuple[tuple[_SignalRow, ...], int]:
    """Validate every configuration component this module reads; return the parsed rows."""
    configuration = bundle.configuration
    if not isinstance(configuration, Mapping):
        raise _incomplete("configuration")
    signals = configuration.get("signals")
    if type(signals) is not tuple or not signals:
        raise _incomplete("configuration.signals")
    profiles = configuration.get("profiles")
    if type(profiles) is not tuple:
        raise _incomplete("configuration.profiles")
    saturation = configuration.get("saturation_k_bp")
    if not _is_int(saturation) or saturation <= 0:
        raise _incomplete("configuration.saturation_k_bp")
    responses_by_profile = {}
    for profile in profiles:
        if not isinstance(profile, Mapping) or not isinstance(profile.get("responses"), Mapping):
            raise _incomplete("configuration.profiles")
        responses_by_profile[profile.get("profile_id")] = profile["responses"]
    channel_ids = frozenset(channel.channel_id for channel in kernel.channels)
    return tuple(_signal_row(row, responses_by_profile, channel_ids) for row in signals), saturation


def _signal_row(row: object, responses_by_profile: Mapping, channel_ids: frozenset[str]) -> _SignalRow:
    if not isinstance(row, Mapping) or not all(key in row for key in ("signal_id", "operation", "channels")):
        raise _incomplete("configuration.signals")
    signal_id, operation, channels = row["signal_id"], row["operation"], row["channels"]
    if type(signal_id) is not str or type(channels) is not tuple or not channels:
        raise _incomplete("configuration.signals")
    if operation not in _OPERATIONS:
        raise SchemaValidationError(
            OPERATION_UNKNOWN,
            "signal operation is not a v2 operation",
            {"signal_id": signal_id, "operation": operation},
        )
    responses = None
    if operation == ORDINARY_OPERATION:
        profile_id = row.get("profile_id")
        responses = responses_by_profile.get(profile_id)
        if responses is None:
            raise SchemaValidationError(
                PROFILE_MISSING, "signal profile is absent", {"signal_id": signal_id, "profile_id": profile_id}
            )
        for state in CHANNEL_STATES:
            if not _is_int(responses.get(state)):
                raise SchemaValidationError(
                    PROFILE_MISSING,
                    "signal profile lacks a response for a Channel state",
                    {"signal_id": signal_id, "profile_id": profile_id, "state": state},
                )
    parsed = []
    for channel in channels:
        if not isinstance(channel, Mapping):
            raise _incomplete("configuration.signals")
        channel_id, weight = channel.get("channel_id"), channel.get("weight")
        if channel_id not in channel_ids:
            raise SchemaValidationError(
                CHANNEL_UNKNOWN,
                "signal Channel is not a kernel Channel",
                {"signal_id": signal_id, "channel_id": channel_id},
            )
        if not _is_int(weight) or weight < 1:
            raise SchemaValidationError(
                WEIGHT_INVALID,
                "signal Channel weight must be an integer >= 1",
                {"signal_id": signal_id, "channel_id": channel_id},
            )
        parsed.append((channel_id, weight))
    return _SignalRow(signal_id, operation, responses, tuple(parsed))


def _signal_value(row: _SignalRow, states: Mapping, saturation: int) -> int:
    """HDE Math Spec §5.2.11, "Signals": one operation over the row's weighted Channels."""
    if row.operation == ORDINARY_OPERATION:
        # S = Σ w·r(p_s, state_c), basis points; q = rhu(1000·S, S + K), 0 when S = 0.
        total = sum(weight * row.responses[states[channel_id].state] for channel_id, weight in row.channels)
        return 0 if total == 0 else rhu(PER_MILLE * total, total + saturation)
    if row.operation == OWNER_MASS_OPERATION:
        # m_lo, m_hi: each member's owned dominance or compromise Channels.
        m_lo = m_hi = 0
        for channel_id, weight in row.channels:
            channel = states[channel_id]
            if channel.state in _OWNED_STATES:
                if channel.owner == "member_lo":
                    m_lo += weight
                else:
                    m_hi += weight
        return 0 if m_lo + m_hi == 0 else rhu(PER_MILLE * 2 * min(m_lo, m_hi), m_lo + m_hi)
    # mutual_state_share_v2: F Channels not none; M companionship or electromagnetic.
    filled = mutual = 0
    for channel_id, weight in row.channels:
        state = states[channel_id].state
        if state != "none":
            filled += weight
        if state in _MUTUAL_STATES:
            mutual += weight
    return 0 if filled == 0 else rhu(PER_MILLE * mutual, filled)


# HDE-EPIC043 WU-PR-09: passive provenance for release admission (last top-level statement).
_MODULE_EXECUTION = _capture_module_execution(globals())
