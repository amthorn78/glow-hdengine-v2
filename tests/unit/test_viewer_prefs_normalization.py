from __future__ import annotations

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.sampler.core import CandidateFeatures, ViewerProfile, build_candidate_pool
from engine.validation.viewer_prefs import (
    normalize_viewer_prefs,
    validate_viewer_prefs,
    weight_for_candidate_top_category,
)


def _valid_prefs() -> dict[str, object]:
    return {
        "top_category": CATEGORIES_ORDER_V1[0],
        "weights": {category: 1 for category in CATEGORIES_ORDER_V1},
    }


def test_normalize_viewer_prefs_preserves_zero_weight() -> None:
    prefs = _valid_prefs()
    weights = prefs["weights"]
    assert isinstance(weights, dict)
    weights[CATEGORIES_ORDER_V1[1]] = 0

    err = validate_viewer_prefs(prefs)
    assert err is None

    normalized = normalize_viewer_prefs(prefs)
    normalized_weights = normalized["weights"]
    assert isinstance(normalized_weights, dict)
    assert normalized_weights[CATEGORIES_ORDER_V1[1]] == 0


def test_invalid_viewer_prefs_fail_closed() -> None:
    prefs = {
        "top_category": "not-a-valid-category",
        "weights": {category: 1 for category in CATEGORIES_ORDER_V1},
    }
    assert validate_viewer_prefs(prefs) is not None


def test_zero_weight_handoff_to_sampler_exclusion() -> None:
    prefs = _valid_prefs()
    weights = prefs["weights"]
    assert isinstance(weights, dict)
    excluded_category = CATEGORIES_ORDER_V1[2]
    kept_category = CATEGORIES_ORDER_V1[3]
    weights[excluded_category] = 0
    weights[kept_category] = 2

    err = validate_viewer_prefs(prefs)
    assert err is None
    normalized = normalize_viewer_prefs(prefs)

    viewer = ViewerProfile(person_uid="viewer-001", top_category=str(normalized["top_category"]))
    candidates = [
        CandidateFeatures(
            person_uid="zero-weight-candidate",
            weight=weight_for_candidate_top_category(normalized, excluded_category),
            compat_score=80,
            categories=(excluded_category,),
        ),
        CandidateFeatures(
            person_uid="positive-weight-candidate",
            weight=weight_for_candidate_top_category(normalized, kept_category),
            compat_score=80,
            categories=(kept_category,),
        ),
    ]

    pool = build_candidate_pool(viewer, candidates)
    assert [cand.person_uid for cand in pool.candidates] == ["positive-weight-candidate"]


def test_weight_handoff_rejects_unknown_top_category() -> None:
    prefs = _valid_prefs()
    assert validate_viewer_prefs(prefs) is None
    normalized = normalize_viewer_prefs(prefs)

    try:
        weight_for_candidate_top_category(normalized, "unknown-category")
    except ValueError as exc:
        assert str(exc) == "INVALID_CANDIDATE_TOP_CATEGORY"
    else:  # pragma: no cover
        raise AssertionError("expected INVALID_CANDIDATE_TOP_CATEGORY")
