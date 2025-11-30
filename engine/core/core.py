from __future__ import annotations

"""
Deterministic Engine Core (behavior-only for HDE-DISS004).

Discovery summary (Step 1):
- ``engine.sampler.core`` already houses a pure-compute sampler; it uses
  frozen dataclasses and deterministic comparators for ordering.
- ``engine.compat.compute`` provides band resolution and category scoring
  without touching I/O or the environment; the band order constants are
  reused here for parity with compat outputs.
- ``engine.order.comparators`` exposes canonical ID and set ordering used
  across Phase II components; we reuse those comparators for AB/BA-neutral
  pair ordering and trait canonicalization.

This module keeps the Engine Core pure-compute: no I/O, no clocks, no
randomness, and no global mutable state. All behavior depends solely on the
provided participant states and config.
"""

from dataclasses import dataclass
from functools import cmp_to_key
from typing import Iterable, Tuple

from engine.compat.thresholds import BANDS
from engine.order.comparators import ABBA_CANONICAL_PAIR, compare_ids, canonicalize_set


@dataclass(frozen=True)
class ParticipantState:
    """Normalized participant state for Engine Core inputs."""

    person_uid: str
    compat_score: int
    band: str
    traits: Tuple[str, ...] = ()


@dataclass(frozen=True)
class CoreConfig:
    """Pure configuration knobs for Engine Core behavior."""

    band_priority: Tuple[str, ...] = BANDS


@dataclass(frozen=True)
class PerspectiveBreakdown:
    """Directional metrics that retain viewer/candidate perspective."""

    from_viewer: int
    from_candidate: int
    delta: int


@dataclass(frozen=True)
class CoreResult:
    """Deterministic Engine Core output suitable for canonical JSON."""

    viewer_id: str
    candidate_id: str
    neutral_score: int
    ordered_pair: Tuple[str, str]
    ordered_bands: Tuple[str, str]
    shared_traits: Tuple[str, ...]
    band_alignment: bool
    perspective: PerspectiveBreakdown


def _band_rank(band: str, band_priority: Tuple[str, ...]) -> int:
    mapping = {value: idx for idx, value in enumerate(band_priority)}
    return mapping.get(band, len(mapping))


def _ordered_pair(a: str, b: str) -> Tuple[str, str]:
    pair = sorted((a, b), key=cmp_to_key(compare_ids))
    if compare_ids(pair[0], pair[1]) == 0:
        return ABBA_CANONICAL_PAIR
    return tuple(pair)  # type: ignore[return-value]


def _ordered_bands(a: str, b: str, config: CoreConfig) -> Tuple[str, str]:
    priority = config.band_priority
    return tuple(
        sorted(
            (a, b),
            key=lambda value: (_band_rank(value, priority), value),
        )
    )  # type: ignore[return-value]


def _neutral_score(viewer_score: int, candidate_score: int) -> int:
    return (viewer_score + candidate_score) // 2


def _shared_traits(viewer_traits: Iterable[str], candidate_traits: Iterable[str]) -> Tuple[str, ...]:
    candidate_set = set(candidate_traits)
    overlap = {trait for trait in viewer_traits if trait in candidate_set}
    return tuple(canonicalize_set(overlap, compare_ids))


def compute_core(
    viewer_state: ParticipantState,
    candidate_state: ParticipantState,
    config: CoreConfig | None = None,
) -> CoreResult:
    """Compute deterministic Engine Core metrics.

    - AB/BA neutrality is achieved by canonical ordering of IDs and bands.
    - Directional metrics are explicit via ``PerspectiveBreakdown`` while
      neutral metrics remain symmetric.
    - All computations rely solely on the provided arguments and band
      priorities from ``CoreConfig``.
    """

    cfg = config or CoreConfig()

    viewer_score = viewer_state.compat_score
    candidate_score = candidate_state.compat_score

    ordered_pair = _ordered_pair(viewer_state.person_uid, candidate_state.person_uid)
    ordered_bands = _ordered_bands(viewer_state.band, candidate_state.band, cfg)

    return CoreResult(
        viewer_id=viewer_state.person_uid,
        candidate_id=candidate_state.person_uid,
        neutral_score=_neutral_score(viewer_score, candidate_score),
        ordered_pair=ordered_pair,
        ordered_bands=ordered_bands,
        shared_traits=_shared_traits(viewer_state.traits, candidate_state.traits),
        band_alignment=viewer_state.band == candidate_state.band,
        perspective=PerspectiveBreakdown(
            from_viewer=viewer_score,
            from_candidate=candidate_score,
            delta=viewer_score - candidate_score,
        ),
    )
