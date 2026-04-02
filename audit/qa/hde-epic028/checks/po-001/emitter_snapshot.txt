from __future__ import annotations
from typing import Tuple, Dict, Any
from engine.serializer import canon


def emit_public(envelope: Dict[str, Any], *, sort_keys: bool = True) -> bytes:
    """
    Canonical emitter for governed public JSON bytes.

    - Delegates to the canonical serializer (LF-terminated UTF-8)
    - Sorts keys by default for deterministic public envelopes
    """
    return canon.sercanon(envelope, sort_keys=sort_keys)


def emit_public_with_envelope(
    envelope: Dict[str, Any], *, sort_keys: bool = True
) -> Tuple[bytes, Dict[str, Any]]:
    """Emit canonical bytes and return the original envelope."""
    return emit_public(envelope, sort_keys=sort_keys), envelope


def emit_compact_json(envelope: Dict[str, Any], *, sort_keys: bool = True) -> Tuple[bytes, Dict[str, Any]]:
    """
    Compatibility alias for the canonical emitter.
    Prefer :func:`emit_public_with_envelope` for new call sites.
    """
    return emit_public_with_envelope(envelope, sort_keys=sort_keys)
