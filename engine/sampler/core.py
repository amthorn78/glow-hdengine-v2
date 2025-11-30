from __future__ import annotations

"""
Pure-compute sampler core (DISS003).

Discovery notes:
- Deterministic comparators already live in ``engine.order.comparators``
  (ID, channel, category ordering) and are reused here for tie-breaking.
- Phase II inputs surfaced so far include normalized viewer prefs and
  compat outputs (bands/percent scores) from ``engine.compat.compute``.
  Candidate weights are present on the normalized candidate payloads from
  DISS001.
- No prior sampler prototypes are depended on; PF10 notes were treated as
  historical context only.

The sampler enforces zero-weight rules during pool construction, applies
simple eligibility checks (compat threshold + allowed bands), and ranks
eligible candidates deterministically using existing comparators.
"""

from dataclasses import dataclass
from functools import cmp_to_key
from typing import Iterable, List, Sequence

from engine.compat.compute import band_for
from engine.compat.thresholds import BANDS
from engine.order.comparators import compare_ids


@dataclass(frozen=True)
class ViewerProfile:
    """Minimal viewer state passed into the sampler."""

    person_uid: str
    top_category: str | None = None


@dataclass(frozen=True)
class CandidateFeatures:
    """Normalized candidate state from Phase II inputs."""

    person_uid: str
    weight: float
    compat_score: int
    band: str | None = None
    diversity_key: str | None = None
    is_recent: bool = False
    categories: Sequence[str] | None = None


@dataclass(frozen=True)
class SamplerConfig:
    """Sampler knobs applied uniformly across calls."""

    min_compat_score: int = 0
    excluded_bands: tuple[str, ...] = ()
    allowed_bands: tuple[str, ...] | None = None
    require_diversity_key: bool = False
    band_priority: tuple[str, ...] = tuple(reversed(BANDS))


@dataclass(frozen=True)
class CandidatePoolEntry:
    person_uid: str
    weight: float
    compat_score: int
    band: str
    diversity_key: str | None
    is_recent: bool


@dataclass(frozen=True)
class CandidatePool:
    viewer_id: str
    candidates: List[CandidatePoolEntry]


@dataclass(frozen=True)
class RankedCandidate:
    person_uid: str
    score: int
    weight: float
    band: str
    rank: int
    diversity_key: str | None
    is_recent: bool


@dataclass(frozen=True)
class RankedCandidates:
    viewer_id: str
    candidates: List[RankedCandidate]


def _cmp(a, b) -> int:
    return (a > b) - (a < b)


def _resolve_band(candidate: CandidateFeatures) -> str:
    band = candidate.band
    if isinstance(band, str) and band:
        return band
    return band_for(candidate.compat_score)


def _band_priority_map(priority: tuple[str, ...]) -> dict[str, int]:
    return {band: idx for idx, band in enumerate(priority)}


def _is_zero_weight(candidate: CandidateFeatures) -> bool:
    return candidate.weight <= 0


def _is_eligible(candidate: CandidateFeatures, band: str, config: SamplerConfig) -> bool:
    if candidate.compat_score < config.min_compat_score:
        return False
    if config.allowed_bands is not None and band not in config.allowed_bands:
        return False
    if band in config.excluded_bands:
        return False
    if config.require_diversity_key and not candidate.diversity_key:
        return False
    return True


def build_candidate_pool(
    viewer: ViewerProfile,
    raw_candidates: Iterable[CandidateFeatures],
    config: SamplerConfig | None = None,
) -> CandidatePool:
    """Construct the candidate pool after eligibility and zero-weight filtering."""

    cfg = config or SamplerConfig()
    pool: List[CandidatePoolEntry] = []
    for candidate in raw_candidates:
        if _is_zero_weight(candidate):
            continue
        band = _resolve_band(candidate)
        if not _is_eligible(candidate, band, cfg):
            continue
        pool.append(
            CandidatePoolEntry(
                person_uid=candidate.person_uid,
                weight=candidate.weight,
                compat_score=candidate.compat_score,
                band=band,
                diversity_key=candidate.diversity_key,
                is_recent=bool(candidate.is_recent),
            )
        )
    return CandidatePool(viewer_id=viewer.person_uid, candidates=pool)


def _band_rank(band: str, priority: tuple[str, ...]) -> int:
    mapping = _band_priority_map(priority)
    return mapping.get(band, len(mapping))


def _compare_entries(a: CandidatePoolEntry, b: CandidatePoolEntry, config: SamplerConfig) -> int:
    if a.weight != b.weight:
        return -_cmp(a.weight, b.weight)
    if a.compat_score != b.compat_score:
        return -_cmp(a.compat_score, b.compat_score)
    band_cmp = _cmp(_band_rank(a.band, config.band_priority), _band_rank(b.band, config.band_priority))
    if band_cmp:
        return band_cmp
    return compare_ids(a.person_uid, b.person_uid)


def rank_candidates(pool: CandidatePool, config: SamplerConfig | None = None) -> RankedCandidates:
    """Deterministically rank candidates in the pool.

    - Sorting combines weight, compat score, band priority, and ID tie-breaker
      (using canonical comparators) to produce a total order.
    - No randomness, clocks, or external state are consulted.
    """

    cfg = config or SamplerConfig()
    ordered = sorted(pool.candidates, key=cmp_to_key(lambda a, b: _compare_entries(a, b, cfg)))
    ranked: List[RankedCandidate] = []
    for idx, cand in enumerate(ordered, start=1):
        ranked.append(
            RankedCandidate(
                person_uid=cand.person_uid,
                score=cand.compat_score,
                weight=cand.weight,
                band=cand.band,
                rank=idx,
                diversity_key=cand.diversity_key,
                is_recent=cand.is_recent,
            )
        )
    return RankedCandidates(viewer_id=pool.viewer_id, candidates=ranked)


def sample_and_rank(
    viewer: ViewerProfile,
    raw_candidates: Iterable[CandidateFeatures],
    config: SamplerConfig | None = None,
) -> RankedCandidates:
    """Helper to build a pool and immediately rank it."""

    pool = build_candidate_pool(viewer, raw_candidates, config=config)
    return rank_candidates(pool, config=config)
