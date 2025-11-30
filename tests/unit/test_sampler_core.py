from __future__ import annotations

import copy

from engine.sampler.core import (
    CandidateFeatures,
    RankedCandidates,
    SamplerConfig,
    ViewerProfile,
    build_candidate_pool,
    rank_candidates,
    sample_and_rank,
)


def _viewer(uid: str = "viewer") -> ViewerProfile:
    return ViewerProfile(person_uid=uid)


def _candidate(uid: str, weight: float, compat: int, **kwargs) -> CandidateFeatures:
    data = {"person_uid": uid, "weight": weight, "compat_score": compat}
    data.update(kwargs)
    return CandidateFeatures(**data)


def test_zero_weight_candidates_are_excluded() -> None:
    viewer = _viewer()
    raw = [
        _candidate("alpha", 0, 70),
        _candidate("bravo", 1, 60),
        _candidate("charlie", 2, 80),
    ]

    pool = build_candidate_pool(viewer, raw)
    ranked = rank_candidates(pool)

    ids = [c.person_uid for c in pool.candidates]
    ranked_ids = [c.person_uid for c in ranked.candidates]
    assert set(ids) == {"bravo", "charlie"}
    assert ranked_ids == ["charlie", "bravo"]


def test_eligibility_rules_apply_min_score_and_band() -> None:
    viewer = _viewer()
    cfg = SamplerConfig(min_compat_score=50, excluded_bands=("Cool",))
    raw = [
        _candidate("cool", 1, 10),  # Cool band -> excluded
        _candidate("low", 1, 40),  # Below min score -> excluded
        _candidate("warm", 1, 70),
        _candidate("glow", 1, 90),
    ]

    pool = build_candidate_pool(viewer, raw, config=cfg)

    ids = [c.person_uid for c in pool.candidates]
    assert ids == ["warm", "glow"]


def test_rank_candidates_is_deterministic() -> None:
    viewer = _viewer()
    raw = [
        _candidate("alpha", 2, 60),
        _candidate("bravo", 2, 65),
        _candidate("charlie", 1, 90),
    ]

    ranked_first = sample_and_rank(viewer, raw)
    ranked_second = sample_and_rank(viewer, copy.deepcopy(raw))

    assert ranked_first == ranked_second
    assert [c.person_uid for c in ranked_first.candidates] == ["bravo", "alpha", "charlie"]


def test_ab_ba_parity_respects_total_order() -> None:
    viewer_a = _viewer("viewer_a")
    viewer_b = _viewer("viewer_b")

    raw_ab = [_candidate("viewer_b", 1, 75), _candidate("viewer_a", 1, 65)]
    raw_ba = [_candidate("viewer_a", 1, 75), _candidate("viewer_b", 1, 65)]

    ranked_ab: RankedCandidates = sample_and_rank(viewer_a, raw_ab)
    ranked_ba: RankedCandidates = sample_and_rank(viewer_b, raw_ba)

    assert [c.person_uid for c in ranked_ab.candidates] == ["viewer_b", "viewer_a"]
    assert [c.person_uid for c in ranked_ba.candidates] == ["viewer_a", "viewer_b"]
    assert ranked_ab.candidates[0].score == ranked_ba.candidates[0].score
