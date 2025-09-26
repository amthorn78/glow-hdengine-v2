# Deterministic JSON serializer (no I/O at import)
import json

_COMPACT_SEPS = (",", ":")

def dumps_minified_sorted(obj: dict) -> str:
    """
    Return a minified, sorted-keys JSON string.
    - ensure_ascii=False (UTF-8 capable)
    - separators without spaces (compact)
    - sort_keys=True (deterministic key order)
    """
    return json.dumps(obj, ensure_ascii=False, separators=_COMPACT_SEPS, sort_keys=True)

def serialize(obj: dict) -> bytes:
    """
    Return canonical JSON bytes with exactly one trailing LF.
    - UTF-8, sorted keys, compact separators
    - normalizes any stray LFs to a single trailing LF
    """
    s = dumps_minified_sorted(obj)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")
