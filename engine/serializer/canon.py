from __future__ import annotations

from engine.stable import sercanon as stable_sercanon


def sercanon(obj, *, sort_keys: bool = True) -> bytes:
    """
    Canonical JSON serializer for public envelopes.
    - UTF-8 bytes
    - ensure_ascii=False
    - keys sorted by default
    - compact separators
    - exactly one trailing newline
    """
    return stable_sercanon.serialize(obj, sort_keys=sort_keys)


# EPIC004-only compatibility alias; remove in next epic
dumps = sercanon
