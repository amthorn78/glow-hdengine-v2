from __future__ import annotations
import json

def sercanon(obj, *, sort_keys: bool = True) -> bytes:
    """
    Canonical JSON serializer for public envelopes.
    - UTF-8 bytes
    - ensure_ascii=False
    - keys sorted
    - compact separators
    - exactly one trailing newline
    """
    s = json.dumps(obj, ensure_ascii=False, sort_keys=sort_keys, separators=(",", ":"))
    # Guarantee exactly one trailing LF
    if not s.endswith("\n"):
        s += "\n"
    return s.encode("utf-8")

# EPIC004-only compatibility alias; remove in next epic
dumps = sercanon
