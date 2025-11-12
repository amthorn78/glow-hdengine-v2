"""Shared Aux narrative emission helpers for public surfaces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .composer import compose_text
from .state import get_pack


@dataclass(frozen=True)
class AuxPublicEmission:
    """Resolved Aux emission metadata for public presentation."""

    body: bytes
    composition_id: str
    key: str
    pack_sha: str
    suppressed: bool
    text: str | None


def emit_public_aux(
    *,
    category: str,
    band: str,
    perspective: str,
    viewer_top: str | None = None,
    flags: Iterable[str] | None = None,
    families_fired: Sequence[str] | None = None,
    release_id: str,
    pack_sha: str | None = None,
) -> AuxPublicEmission:
    """Return the Aux public emission for the requested tuple."""

    pack = get_pack()
    resolved_families = tuple(families_fired or ())
    resolved_pack_sha = pack_sha or pack.pack_sha

    result = compose_text(
        category=category,
        band=band,
        perspective=perspective,
        viewer_top=viewer_top,
        flags=flags,
        families_fired=resolved_families,
        release_id=release_id,
        pack_sha=resolved_pack_sha,
    )

    has_text = result.ok and result.text is not None
    body = (result.text + "\n").encode("utf-8") if has_text else b""

    return AuxPublicEmission(
        body=body,
        composition_id=result.composition_id,
        key=result.key,
        pack_sha=pack.pack_sha,
        suppressed=not has_text,
        text=result.text,
    )
