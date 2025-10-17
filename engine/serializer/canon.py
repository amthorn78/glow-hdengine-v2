"""
Canonical JSON serializer:
- UTF-8 bytes
- sort_keys=True
- compact separators (",",":")
- exactly ONE trailing newline
- no BOM
"""
from __future__ import annotations
import json

_COMPACT = (",", ":")

def dumps(obj: dict | list) -> bytes:
    s = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=_COMPACT)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")
