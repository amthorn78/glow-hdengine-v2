from __future__ import annotations
import json

def dumps(obj) -> bytes:
    """
    Canonical JSON serializer for public envelopes:
      - UTF-8 bytes
      - ensure_ascii=False
      - sorted keys
      - compact separators
      - exactly one trailing newline
    """
    s = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if not s.endswith("\n"):
        s += "\n"
    return s.encode("utf-8")
