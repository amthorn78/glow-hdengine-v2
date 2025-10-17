from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple
import json

# Frozen center order (full names)
_CENTER_ORDER = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
_SHORT2FULL = {"H":"head","A":"ajna","T":"throat","G":"g","E":"ego","Sp":"spleen","So":"solar_plexus","Sa":"sacral","R":"root"}
_TALK_LADDER = ["01-08","07-31","10-20","11-56","13-33","17-62","20-57","23-43"]  # ascending

def center_order() -> List[str]:
    return list(_CENTER_ORDER)

def _load_json(p: str) -> dict:
    return json.loads(Path(p).read_text(encoding="utf-8"))

def _norm_center(c: str) -> str:
    if c in _CENTER_ORDER: return c
    if c in _SHORT2FULL:   return _SHORT2FULL[c]
    raise ValueError(f"unknown center code: {c}")

def _assert_asc_ids(ids: List[str]) -> None:
    if ids != sorted(ids):
        raise AssertionError("channel IDs not ascending")

def _channels_norm() -> List[dict]:
    data = _load_json("catalog/channels_v1.json")["channels"]
    out = []
    for ch in data:
        u,v = ch["centers"]
        ch = dict(ch)  # copy
        ch["centers"] = [_norm_center(u), _norm_center(v)]
        out.append(ch)
    ids = [c["id"] for c in out]
    _assert_asc_ids(ids)
    if len(out) != 36: raise AssertionError("expected 36 channels")
    return out

def _gates_map() -> Dict[int,str]:
    gates = _load_json("catalog/gates_v1.json")["gates"]
    if len(gates) != 64: raise AssertionError("expected 64 gates")
    m: Dict[int,str] = {}
    for g in gates:
        m[int(g["gate"])] = _norm_center(g["center"])
    return m

def channels_sorted() -> List[str]:
    return [c["id"] for c in _channels_norm()]

def gates_center() -> Dict[int,str]:
    return _gates_map()

def center_adj() -> List[List[int]]:
    idx = {c:i for i,c in enumerate(_CENTER_ORDER)}
    M = [[0]*9 for _ in range(9)]
    for ch in _channels_norm():
        a,b = ch["centers"]
        ia, ib = idx[a], idx[b]
        if ia == ib:
            M[ia][ib] = 1
        else:
            M[ia][ib] = 1
            M[ib][ia] = 1
    return M

def deg_vector() -> List[int]:
    return [sum(row) for row in center_adj()]

def domain_coverage() -> Dict[str,int]:
    cov: Dict[str,int] = {}
    for ch in _channels_norm():
        for d in ch.get("domains",[]):
            cov[d] = cov.get(d,0)+1
    return dict(sorted(cov.items()))

def distinguished_sets() -> Dict[str,List[str]]:
    # flags-driven from channel data + fixed talk ladder list
    chans = _channels_norm()
    fmt = sorted([c["id"] for c in chans if "format" in c.get("flags",[])])
    dmt = sorted([c["id"] for c in chans if "direct_mt" in c.get("flags",[])])
    return {
        "format_trio": fmt,
        "direct_mt": dmt,
        "talk_ladder": list(_TALK_LADDER)
    }

def channels_for_correction() -> List[str]:
    # exclude narrative-only (primary=="narrative" and domains=={"narrative"})
    keep: List[str] = []
    for ch in _channels_norm():
        ds = set(ch.get("domains",[]))
        if ch.get("primary_domain") == "narrative" and ds == {"narrative"}:
            continue
        keep.append(ch["id"])
    return keep
