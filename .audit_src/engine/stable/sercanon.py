# Deterministic JSON serializer (no I/O at import)
import json
_COMPACT_SEPS = (",", ":")
def dumps_minified_sorted(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=_COMPACT_SEPS, sort_keys=True)
def serialize(obj: dict) -> bytes:
    s = dumps_minified_sorted(obj)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")
