from __future__ import annotations
import hashlib, re
from typing import Dict, Tuple

UID_RE = re.compile(r"^[A-Za-z0-9._-]{1,64}$")

def _uid(p: Dict[str, object]) -> str:
    uid = str(p.get("person_uid") or "")
    if not UID_RE.match(uid):
        raise ValueError("invalid or missing person_uid")
    return uid

def normalize_pair(a: Dict[str, object], b: Dict[str, object]) -> Tuple[Dict[str,object], Dict[str,object]]:
    ua, ub = _uid(a), _uid(b)
    if ua < ub: return a,b
    if ub < ua: return b,a
    # tie-break on payload hash (stable, symmetric)
    ha = hashlib.sha256(repr(sorted(a.items())).encode("utf-8")).hexdigest()
    hb = hashlib.sha256(repr(sorted(b.items())).encode("utf-8")).hexdigest()
    return (a,b) if ha <= hb else (b,a)

def pair_key(a: Dict[str, object], b: Dict[str, object]) -> str:
    a1,b1 = normalize_pair(a,b)
    return f"{_uid(a1)}|{_uid(b1)}"
