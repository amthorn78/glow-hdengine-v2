from __future__ import annotations
from typing import Tuple, Dict, Any
from engine.serializer import dumps

def emit_compact_json(envelope: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """
    Single entrypoint for public JSON bytes.
    Returns (bytes, envelope) with bytes LF-terminated and keys sorted.
    """
    b = dumps(envelope)
    return b, envelope
