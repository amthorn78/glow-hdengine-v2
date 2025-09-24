#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib
from typing import Dict, List
from core.stable.sercanon import stable_dumps

ART = Path("artifacts"); ART.mkdir(exist_ok=True)

CENTERS_ORDER = ["H","A","T","G","E","Sp","So","Sa","R"]

def _load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))

def _adjacency_from_channels(chans: List[dict]) -> List[List[int]]:
    idx = {c:i for i,c in enumerate(CENTERS_ORDER)}
    N = len(CENTERS_ORDER)
    M = [[0]*N for _ in range(N)]
    for ch in chans:
        a, b = ch["centers"]
        ia, ib = idx[a], idx[b]
        if ia==ib: 
            M[ia][ib] = 1
        else:
            M[ia][ib] = 1
            M[ib][ia] = 1
    return M

def _deg_vector(M: List[List[int]]) -> List[int]:
    return [sum(row) for row in M]

def _gate_counts_by_center(gates: List[dict]) -> Dict[str,int]:
    out = {c:0 for c in CENTERS_ORDER}
    for g in gates:
        c = g["center"]
        if c in out: out[c]+=1
    return out

def _domain_coverage(chans: List[dict]) -> Dict[str,int]:
    out: Dict[str,int] = {}
    for ch in chans:
        for d in ch.get("domains",[]):
            out[d] = out.get(d,0)+1
    # stable keys enforced by serialization
    return out

def main():
    cats = _load_json("catalog/channels_v1.json")
    gates = _load_json("catalog/gates_v1.json")
    toggles = _load_json("config/toggles_v1.json")

    chans = list(cats["channels"])
    M = _adjacency_from_channels(chans)
    adj_sha = hashlib.sha256(stable_dumps(M)).hexdigest()
    deg = _deg_vector(M)
    channels_sorted = sorted([c["id"] for c in chans])
    gate_counts = _gate_counts_by_center(gates["gates"])
    dist = cats.get("distinguished", {})
    distinguished = {
        "format_trio_sha": hashlib.sha256(stable_dumps(dist.get("format_trio", []))).hexdigest(),
        "direct_mt_sha": hashlib.sha256(stable_dumps(dist.get("direct_mt", []))).hexdigest(),
        "talk_ladder_sha": hashlib.sha256(stable_dumps(dist.get("talk_ladder", []))).hexdigest(),
    }
    domain_coverage = _domain_coverage(chans)
    toggles_frozen_sha = hashlib.sha256(stable_dumps(toggles)).hexdigest()

    # fixed key order (not alpha) — deterministic emit
    payload = {
        "version": 1,
        "adjacency_sha": adj_sha,
        "deg_vector": deg,
        "channels_sorted": channels_sorted,
        "gate_counts_by_center": gate_counts,
        "distinguished": distinguished,
        "domain_coverage": domain_coverage,
        "toggles_frozen_sha": toggles_frozen_sha
    }
    out = ART/"CANON_CHECKSUMS.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, separators=(",",":")), encoding="utf-8")
    print("CANON OK")

if __name__ == "__main__":
    main()
