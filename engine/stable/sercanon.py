"""Deterministic JSON serializer (no I/O at import)."""

from __future__ import annotations

import json
import sys as _sys
from typing import Any

# Passive, immutable top-level execution provenance for active admission.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None

_COMPACT_SEPS = (",", ":")


def dumps_minified_sorted(obj: dict[str, Any], *, sort_keys: bool = True) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=_COMPACT_SEPS, sort_keys=sort_keys)


def serialize(obj: dict[str, Any], *, sort_keys: bool = True) -> bytes:
    s = dumps_minified_sorted(obj, sort_keys=sort_keys)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")
