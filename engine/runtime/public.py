from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from presenter.reader_v1.emitter import emit_reader_v1, emit_reader_v2
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.runtime.identity import identity_meta

_HARMONY_ID = "harmony"
_BANDS = ("Cool", "Open", "Warm", "Glow")
_READER_VERSIONS = ("v1", "v2")


def _build_enriched_envelope(
    *,
    eligible: bool,
    categories: List[Dict[str, str]],
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
) -> Dict[str, object]:
    return {
        "eligible": bool(eligible),
        "categories": categories,
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }


def _v1_categories(eligible: bool, harmony_band: str | None) -> List[Dict[str, str]]:
    # PF01 §4.7: eligible ⇒ exactly one numeric-free harmony item; ineligible ⇒ [].
    if not eligible:
        return []
    if harmony_band not in _BANDS:
        raise ValueError("reader_band_required")
    return [{"id": _HARMONY_ID, "band": harmony_band}]


def _v2_categories(eligible: bool, categories: Iterable[object] | None) -> List[Dict[str, str]]:
    # PF10 §2.23 / C040-07: eligible ⇒ exactly the ten Magic-10 categories in the
    # canonical governed order, each band from the complete canonical matrix;
    # ineligible ⇒ [].  Accepts (id, band) pairs or {id, band} items.
    if not eligible:
        if categories:
            raise ValueError("reader_v2_categories_forbidden")
        return []
    if categories is None:
        raise ValueError("reader_v2_categories_required")
    items: List[Tuple[str, str]] = []
    for entry in categories:
        if isinstance(entry, dict):
            if set(entry) != {"id", "band"}:
                raise ValueError("reader_v2_categories_required")
            cid, band = entry["id"], entry["band"]
        else:
            try:
                cid, band = entry
            except (TypeError, ValueError):
                raise ValueError("reader_v2_categories_required") from None
        if band not in _BANDS:
            raise ValueError("reader_band_required")
        items.append((str(cid), str(band)))
    if [cid for cid, _ in items] != list(FROZEN_MAGIC10_ORDER):
        raise ValueError("reader_v2_categories_required")
    return [{"id": cid, "band": band} for cid, band in items]


def emit_reader_public_envelope(
    a_chart: object = None,
    b_chart: object = None,
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool,
    harmony_band: str | None = None,
    reader_version: str = "v1",
    categories: Iterable[object] | None = None,
) -> Tuple[bytes, Dict[str, object]]:
    """Emit the Reader public success envelope through the single emitter.

    ``reader_version`` selects the versioned public contract: ``"v1"`` projects
    exactly one ``harmony`` item from ``harmony_band``; ``"v2"`` projects the
    complete ten-item result supplied in ``categories`` (canonical governed
    order).  Both are bands-only and numeric-free; the band(s) are validated rows
    of a complete Gate-based result supplied by the caller, and no chart-derived
    or type-derived banding exists here.  ``a_chart``/``b_chart`` are retained
    only for the governed emitter symbol contract and carry no scoring input.
    An eligible pair must supply its band(s); an ineligible pair emits
    ``categories: []``.
    """

    if reader_version not in _READER_VERSIONS:
        raise ValueError("reader_version_unsupported")
    if reader_version == "v2":
        public = _v2_categories(eligible, categories)
        emit = emit_reader_v2
    else:
        public = _v1_categories(eligible, harmony_band)
        emit = emit_reader_v1
    meta = identity_meta()
    enriched = _build_enriched_envelope(
        eligible=eligible,
        categories=public,
        engine_tag=engine_tag or meta["engine_tag"],
        invocation_tag=invocation_tag or meta["invocation_tag"],
        release_id=release_id or meta["release_id"],
    )
    return emit(enriched)


def emit_reader_public_bytes(
    a_chart: object = None,
    b_chart: object = None,
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool,
    harmony_band: str | None = None,
    reader_version: str = "v1",
    categories: Iterable[object] | None = None,
) -> bytes:
    return emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
        eligible=eligible,
        harmony_band=harmony_band,
        reader_version=reader_version,
        categories=categories,
    )[0]
