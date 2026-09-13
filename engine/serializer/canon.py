from __future__ import annotations

import sys as _sys

from engine.stable import sercanon as stable_sercanon


# Passive, immutable top-level execution provenance for active admission.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None


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
