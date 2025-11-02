from __future__ import annotations

from typing import Any, Dict

from engine.runtime import emit_reader_public_bytes

def emit_public_envelope(
    a_chart: Dict[str, Any],
    b_chart: Dict[str, Any],
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
) -> bytes:
    """Legacy helper retained for harnesses; routes through presenter emitter."""
    return emit_reader_public_bytes(
        a_chart,
        b_chart,
        engine_tag=engine_tag,
        invocation_tag=invocation_tag,
        release_id=release_id,
    )
