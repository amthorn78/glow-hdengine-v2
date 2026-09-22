from __future__ import annotations

from typing import Dict, Tuple

from presenter.reader_v1.emitter import emit_reader_v1
from engine.runtime.identity import identity_meta

_HARMONY_ID = "harmony"
_BANDS = ("Cool", "Open", "Warm", "Glow")


def _build_enriched_envelope(
    *,
    eligible: bool,
    harmony_band: str | None,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
) -> Dict[str, object]:
    # PF01 §4.7: eligible ⇒ exactly one numeric-free harmony item; ineligible ⇒ [].
    categories = [{"id": _HARMONY_ID, "band": harmony_band}] if eligible else []
    return {
        "eligible": bool(eligible),
        "categories": categories,
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }


def emit_reader_public_envelope(
    a_chart: object = None,
    b_chart: object = None,
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool,
    harmony_band: str | None = None,
) -> Tuple[bytes, Dict[str, object]]:
    """Emit the Reader v1 success envelope through the single emitter.

    The band is the validated ``harmony`` row of a complete Gate-based result
    supplied by the caller; no chart-derived or type-derived banding exists
    here.  ``a_chart``/``b_chart`` are retained only for the governed emitter
    symbol contract and carry no scoring input.  An eligible pair must supply
    its band; an ineligible pair emits ``categories: []``.
    """

    if eligible:
        if harmony_band not in _BANDS:
            raise ValueError("reader_band_required")
    else:
        harmony_band = None
    meta = identity_meta()
    enriched = _build_enriched_envelope(
        eligible=eligible,
        harmony_band=harmony_band,
        engine_tag=engine_tag or meta["engine_tag"],
        invocation_tag=invocation_tag or meta["invocation_tag"],
        release_id=release_id or meta["release_id"],
    )
    return emit_reader_v1(enriched)


def emit_reader_public_bytes(
    a_chart: object = None,
    b_chart: object = None,
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool,
    harmony_band: str | None = None,
) -> bytes:
    return emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
        eligible=eligible,
        harmony_band=harmony_band,
    )[0]
