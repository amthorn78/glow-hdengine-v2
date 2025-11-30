from __future__ import annotations

import dataclasses
import json

from engine.core import CoreConfig, ParticipantState, compute_core
from engine.runtime.determinism_env import ensure_determinism_env


def _participant(uid: str, score: int, band: str, traits: tuple[str, ...]) -> ParticipantState:
    return ParticipantState(person_uid=uid, compat_score=score, band=band, traits=traits)


def test_compute_core_is_two_run_identical() -> None:
    ensure_determinism_env(apply=True)

    cfg = CoreConfig()
    viewer = _participant("viewer_alpha", 64, "Open", ("hiking", "coffee"))
    candidate = _participant("viewer_charlie", 64, "Open", ("coffee", "reading"))

    first = compute_core(viewer, candidate, config=cfg)
    second = compute_core(viewer, candidate, config=cfg)

    assert first == second

    serialized_first = json.dumps(dataclasses.asdict(first), sort_keys=True)
    serialized_second = json.dumps(dataclasses.asdict(second), sort_keys=True)
    assert serialized_first == serialized_second


def test_compute_core_handles_band_ordering_deterministically() -> None:
    ensure_determinism_env(apply=True)

    cfg = CoreConfig(band_priority=("Glow", "Warm", "Open", "Cool"))
    viewer = _participant("viewer_delta", 80, "Cool", ("art",))
    candidate = _participant("viewer_echo", 82, "Warm", ("art", "music"))

    result = compute_core(viewer, candidate, config=cfg)
    assert result.ordered_bands == ("Warm", "Cool")
    assert result.ordered_pair == ("viewer_delta", "viewer_echo")
