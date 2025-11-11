"""Compose Aux narrative text with lint enforcement."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, Sequence

from .constants import (
    MISSING_NARRATIVE_KEY,
    PERSPECTIVES,
)
from .lints import run_all
from .router import route_keys
from .state import get_pack

_HEX_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass
class CompositionResult:
    ok: bool
    key: str
    composition_id: str
    text: str | None
    policy_reason: str | None = None


def _normalize_direction(value: str) -> str:
    return value.strip().lower().replace("\\_", "_")


def _validate_pack_sha(pack_sha: str) -> bool:
    return bool(_HEX_RE.match(pack_sha))


def _validate_release_id(release_id: str) -> bool:
    return bool(_HEX_RE.match(release_id))


def _validate_families(families: Sequence[str]) -> bool:
    if any(not isinstance(item, str) or not item for item in families):
        return False
    if list(families) != sorted(set(families)):
        return False
    if any(not item.isascii() for item in families):
        return False
    return True


def compose_text(
    *,
    category: str,
    band: str,
    perspective: str,
    viewer_top: str | None,
    flags: Iterable[str] | None,
    families_fired: Sequence[str],
    release_id: str,
    pack_sha: str,
) -> CompositionResult:
    """Return the composed narrative or suppression metadata."""

    normalized_perspective = _normalize_direction(perspective)
    if normalized_perspective not in PERSPECTIVES:
        return CompositionResult(False, MISSING_NARRATIVE_KEY, MISSING_NARRATIVE_KEY, None, "invalid_perspective")

    if not _validate_families(families_fired):
        return CompositionResult(False, MISSING_NARRATIVE_KEY, MISSING_NARRATIVE_KEY, None, "invalid_families")

    if not _validate_release_id(release_id):
        return CompositionResult(False, MISSING_NARRATIVE_KEY, MISSING_NARRATIVE_KEY, None, "invalid_release_id")

    pack = get_pack()
    if not _validate_pack_sha(pack_sha) or pack_sha != pack.pack_sha:
        return CompositionResult(False, MISSING_NARRATIVE_KEY, MISSING_NARRATIVE_KEY, None, "pack_mismatch")

    routed = route_keys(
        category,
        band,
        normalized_perspective,
        viewer_top=viewer_top,
        flags=flags,
    )

    target_key = routed["shared_key"] if normalized_perspective == "shared" else routed["personal_key"]

    if target_key == MISSING_NARRATIVE_KEY:
        return CompositionResult(False, target_key, target_key, None, "missing_key")

    record = pack.keys.get(target_key)
    if record is None:
        return CompositionResult(False, target_key, target_key, None, "unknown_key")

    if normalized_perspective in {"a_to_b", "b_to_a"} and normalized_perspective not in record.directions:
        return CompositionResult(False, target_key, target_key, None, "direction_not_allowed")

    if target_key in pack.suppression_map:
        reason = pack.suppression_map[target_key].get("policy_reason", "suppressed")
        return CompositionResult(False, target_key, target_key, None, reason)

    text = pack.templates.get(target_key)
    if text is None:
        return CompositionResult(False, target_key, target_key, None, "missing_template")

    lint_failures = list(run_all(text))
    if lint_failures:
        reason = ",".join(sorted(lint_failures))
        return CompositionResult(False, target_key, target_key, None, reason)

    return CompositionResult(True, target_key, record.composition_id, text, None)
