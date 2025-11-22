"""Deterministic JSON serializer (no I/O at import)."""

from __future__ import annotations

import json
from typing import Any

_COMPACT_SEPS = (",", ":")


def dumps_minified_sorted(obj: dict[str, Any], *, sort_keys: bool = True) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=_COMPACT_SEPS, sort_keys=sort_keys)


def serialize(obj: dict[str, Any], *, sort_keys: bool = True) -> bytes:
    s = dumps_minified_sorted(obj, sort_keys=sort_keys)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")
