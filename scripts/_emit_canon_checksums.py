#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, hashlib
from typing import Dict, List

from core.stable.sercanon import stable_dumps
from core.catalog import loader
from core.config.toggles_resolver import resolve_toggles

ART = Path("artifacts"); ART.mkdir(exist_ok=True)

REQ_COUNTS = {
  "head":3,"ajna":6,"throat":11,"g":8,"ego":4,"spleen":7,"solar_plexus":7,"sacral":9,"root":9
}

def _sha(obj) -> str:
    return hashlib.sha256(stable_dumps(obj)).hexdigest()

def _gate_counts_by_center() -> Dict[str,int]:
    g2c = loader.gates_center()
    out: Dict[str,int] = {k:0 for k in loader.center_order()}
    for c in g2c.values():
        out[c] += 1
    return out

def main():
    # canon from loader
    centers = loader.center_order()
    adj = loader.center_adj()
    deg = loader.deg_vector()
    chans = loader.channels_sorted()
    gate_counts = _gate_counts_by_center()
    dist = loader.distinguished_sets()
    domcov = loader.domain_coverage()
    # toggles sha from resolver (frozen)
    _, frozen_sha, _ = resolve_toggles()

    # deterministic payload in the exact required order
    payload = {
        "version": 2,
                "adjacency_sha": _sha(adj),
        "deg_vector": deg,
        "channels_sorted": chans,
        "gate_counts_by_center": gate_counts,
        "distinguished": {
            "format_trio_sha": _sha(dist.get("format_trio", [])),
            "direct_mt_sha": _sha(dist.get("direct_mt", [])),
            "talk_ladder_sha": _sha(dist.get("talk_ladder", [])),
        },
        "domain_coverage": domcov,
        "toggles_frozen_sha": frozen_sha,
        "center_order": centers
    }

    # write with insertion order preserved (compact JSON)
    out = ART / "CANON_CHECKSUMS.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, separators=(",",":")) + "\n", encoding="utf-8")
    print("CANON OK")

if __name__ == "__main__":
    main()
