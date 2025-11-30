from __future__ import annotations

from engine.core import CoreConfig, ParticipantState, compute_core
from engine.runtime.determinism_env import ensure_determinism_env


def _participant(uid: str, score: int, band: str, traits: tuple[str, ...]) -> ParticipantState:
    return ParticipantState(person_uid=uid, compat_score=score, band=band, traits=traits)


def test_ab_ba_parity_is_neutral_where_expected() -> None:
    ensure_determinism_env(apply=True)

    cfg = CoreConfig()
    viewer_a = _participant("viewer_alpha", 72, "Warm", ("music", "hiking"))
    viewer_b = _participant("viewer_bravo", 88, "Glow", ("music", "travel"))

    ab = compute_core(viewer_a, viewer_b, config=cfg)
    ba = compute_core(viewer_b, viewer_a, config=cfg)

    assert ab.neutral_score == ba.neutral_score
    assert ab.ordered_pair == ba.ordered_pair
    assert ab.ordered_bands == ba.ordered_bands
    assert ab.shared_traits == ("music",)
    assert ba.shared_traits == ("music",)
    assert ab.band_alignment is False
    assert ba.band_alignment is False

    assert ab.perspective.from_viewer == ba.perspective.from_candidate
    assert ab.perspective.from_candidate == ba.perspective.from_viewer
    assert ab.perspective.delta == -ba.perspective.delta
