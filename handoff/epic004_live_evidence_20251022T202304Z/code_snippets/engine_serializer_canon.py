from __future__ import annotations
import json
_COMPACT = (",", ":")
def dumps(obj) -> bytes:
    s = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=_COMPACT)
    if not s.endswith("\n"):
        s += "\n"
    return s.encode("utf-8")
