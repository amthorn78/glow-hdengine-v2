from __future__ import annotations
import json, math, unicodedata as _ud
from hashlib import sha256
from typing import Any, Iterable

# sentinel for masking
class _Mask: pass
_MASK = _Mask()

def _nfc(s: str) -> str:
    return _ud.normalize("NFC", s)

def stable_normalize(obj: Any) -> Any:
    """Return a JSON-serializable structure with deterministic ordering."""
    # primitives
    if obj is None or isinstance(obj, (bool, str, int)):
        return _nfc(obj) if isinstance(obj, str) else obj
    if isinstance(obj, float):
        if not math.isfinite(obj):
            raise ValueError("non-finite float not allowed")
        return obj
    # mappings
    if isinstance(obj, dict):
        for k in obj.keys():
            if not isinstance(k, str):
                raise ValueError("dict keys must be str")
        # normalize values, then reassemble with sorted keys (by codepoint)
        return {k: stable_normalize(obj[k]) for k in sorted(obj.keys())}
    # sequences
    if isinstance(obj, (list, tuple)):
        return [stable_normalize(x) for x in obj]
    # sets → list sorted by stable JSON bytes of each normalized element
    if isinstance(obj, (set, frozenset)):
        norm = [stable_normalize(x) for x in obj]
        def _bytes(v: Any) -> bytes:
            return json.dumps(v, ensure_ascii=False, separators=(",",":"), sort_keys=True).encode("utf-8")
        return sorted(norm, key=_bytes)
    raise ValueError(f"unsupported type: {type(obj).__name__}")

def stable_dumps(obj: Any) -> bytes:
    x = stable_normalize(obj)
    return json.dumps(x, ensure_ascii=False, separators=(",",":"), sort_keys=True).encode("utf-8")

def stable_dumps_str(obj: Any) -> str:
    return stable_dumps(obj).decode("utf-8")

def stable_hash(obj: Any) -> str:
    return sha256(stable_dumps(obj)).hexdigest()

def _deepcopy(x: Any) -> Any:
    if isinstance(x, dict):
        return {k: _deepcopy(v) for k,v in x.items()}
    if isinstance(x, list):
        return [_deepcopy(v) for v in x]
    if isinstance(x, tuple):
        return tuple(_deepcopy(v) for v in x)
    if isinstance(x, (set, frozenset)):
        return type(x)(_deepcopy(v) for v in x)
    return x

def mask_paths(obj: Any, masks: Iterable[str]) -> Any:
    """Return a deep-copied obj with dotted dict paths replaced by _MASK.
    Missing paths are no-ops; only dict navigation is supported for segments.
    """
    out = _deepcopy(obj)
    for path in masks or ():
        segs = [s for s in path.split(".") if s]
        cur = out
        for i, seg in enumerate(segs):
            if not isinstance(cur, dict):
                break
            if i == len(segs) - 1:
                if seg in cur:
                    cur[seg] = _MASK
            else:
                cur = cur.get(seg, None)
                if cur is None:
                    break
    return out

def _prune_masked(x: Any) -> Any:
    if isinstance(x, dict):
        return {k: _prune_masked(v) for k, v in x.items() if v is not _MASK}
    if isinstance(x, list):
        return [_prune_masked(v) for v in x if v is not _MASK]
    if isinstance(x, tuple):
        return tuple(_prune_masked(v) for v in x if v is not _MASK)
    return x

def _drop_empty(x: Any) -> Any:
    if isinstance(x, dict):
        d = {k:_drop_empty(v) for k,v in x.items()}
        d = {k:v for k,v in d.items() if not (_is_empty(v))}
        return d
    if isinstance(x, list):
        lst = [_drop_empty(v) for v in x]
        lst = [v for v in lst if not _is_empty(v)]
        return lst
    if isinstance(x, tuple):
        tpl = tuple(_drop_empty(v) for v in x)
        tpl = tuple(v for v in tpl if not _is_empty(v))
        return tpl
    return x

def _is_empty(v: Any) -> bool:
    return (isinstance(v, dict) and not v) or (isinstance(v, (list, tuple)) and len(v)==0)

DEFAULT_IDEMPOTENCE_MASKS = ('_diagnostics','_why','_admin_debug','meta.trace')

def stable_idempotence_hash(payload: Any, masks: Iterable[str]=DEFAULT_IDEMPOTENCE_MASKS) -> str:
    masked = mask_paths(payload, masks)
    pruned = _prune_masked(masked)
    cleaned = _drop_empty(pruned)
    return stable_hash(cleaned)
