from __future__ import annotations

from typing import Any, Dict

from engine.runtime import emit_reader_public_bytes

def emit_public_envelope(
    a_chart: Dict[str, Any],
    b_chart: Dict[str, Any],
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
    *,
    eligible: bool = False,
    harmony_band: str | None = None,
) -> bytes:
    """Legacy helper retained for harnesses; routes through presenter emitter.

    ``eligible`` and ``harmony_band`` carry the current emitter contract, in both
    directions this helper is used: ``VERIFY.sh`` calls it with the five positional
    arguments only, while ``dev/reader_harness/app.py`` injects it as the Reader
    blueprint's ``emit_fn``, which the routes call with both keywords.

    The default is the ineligible envelope (``categories: []``) rather than a
    fabricated eligible one: an eligible pair must supply its band, and the band
    this helper once derived came from the scorer PR04 retired, so there is no
    truthful default to compute here.
    """

    return emit_reader_public_bytes(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
        eligible=eligible,
        harmony_band=harmony_band,
    )
