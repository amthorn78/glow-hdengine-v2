from __future__ import annotations

from typing import Dict, Tuple

from engine.compat import ts_v0
from presenter.reader_v1.emitter import emit_reader_v1
from engine.runtime.identity import identity_meta

_HARMONY_ID = "harmony"


def _build_enriched_envelope(
    band: str,
    *,
    eligible: bool,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
) -> Dict[str, object]:
    return {
        "eligible": bool(eligible),
        "categories": [{"id": _HARMONY_ID, "band": band}],
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }


def _compute_harmony_band(a_chart: Dict[str, object], b_chart: Dict[str, object]) -> str:
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    features = ts_v0.compute_features(a_ts, b_ts)
    return ts_v0.band_v0(features)


def emit_reader_public_envelope(
    a_chart: Dict[str, object],
    b_chart: Dict[str, object],
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool = True,
) -> Tuple[bytes, Dict[str, object]]:
    band = _compute_harmony_band(a_chart, b_chart)
    meta = identity_meta()
    enriched = _build_enriched_envelope(
        band,
        eligible=eligible,
        engine_tag=engine_tag or meta["engine_tag"],
        invocation_tag=invocation_tag or meta["invocation_tag"],
        release_id=release_id or meta["release_id"],
    )
    return emit_reader_v1(enriched)


def emit_reader_public_bytes(
    a_chart: Dict[str, object],
    b_chart: Dict[str, object],
    *,
    engine_tag: str | None = None,
    invocation_tag: str | None = None,
    release_id: str | None = None,
    eligible: bool = True,
) -> bytes:
    return emit_reader_public_envelope(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
        eligible=eligible,
    )[0]
