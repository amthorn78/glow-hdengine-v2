"""Deterministic narrative key router."""

from __future__ import annotations

from typing import Iterable

from .constants import BANDS, MISSING_NARRATIVE_KEY, PERSPECTIVES
from .state import get_pack


def _normalize_category(value: str) -> str:
    return value


def _normalize_band(value: str) -> str:
    return value if value in BANDS else ""


def _normalize_perspective(value: str) -> str:
    return value


def _dedupe_sequence(values: Iterable[str]) -> tuple[str, ...]:
    seen = []
    for item in values:
        if item not in seen:
            seen.append(item)
    return tuple(seen)


def route_keys(
    category: str,
    band: str,
    perspective: str,
    *,
    viewer_top: str | None = None,
    flags: Iterable[str] | None = None,
) -> dict[str, str]:
    """Return personal/shared narrative keys for the request tuple."""

    pack = get_pack()
    category_slug = _normalize_category(category)
    normalized_band = _normalize_band(band)
    normalized_perspective = _normalize_perspective(perspective)
    _ = viewer_top  # reserved for future logic
    _flags = _dedupe_sequence(flags or [])
    _ = _flags  # flags currently advisory only

    if category_slug not in pack.categories:
        return {"personal_key": MISSING_NARRATIVE_KEY, "shared_key": MISSING_NARRATIVE_KEY}
    if normalized_band not in BANDS:
        return {"personal_key": MISSING_NARRATIVE_KEY, "shared_key": MISSING_NARRATIVE_KEY}
    if normalized_perspective not in PERSPECTIVES:
        return {"personal_key": MISSING_NARRATIVE_KEY, "shared_key": MISSING_NARRATIVE_KEY}

    shared_record = pack.primary_by_perspective.get(
        (category_slug, normalized_band, "shared")
    )
    personal_record = None
    if normalized_perspective in {"a_to_b", "b_to_a"}:
        personal_record = pack.primary_by_perspective.get(
            (category_slug, normalized_band, normalized_perspective)
        )

    shared_key = shared_record.key if shared_record else MISSING_NARRATIVE_KEY
    personal_key = personal_record.key if personal_record else MISSING_NARRATIVE_KEY

    return {"personal_key": personal_key, "shared_key": shared_key}
