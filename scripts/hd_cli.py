#!/usr/bin/env python3
# repo-root on sys.path for direct script runs
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import argparse, json, os
from pathlib import Path
from core.pipeline.compute import compute_pair
from engine.stable.sercanon import serialize  # canonical: sorted, compact, single LF

FROZEN_TALK_LADDER = [
    "01-08","07-31","13-33","10-20","20-57","11-56","17-62","23-43"
]

def _load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def _adjacency_metrics(a_gates, b_gates):
    """Count ladder hits over union of gates; bonus = min(hits, 3)."""
    have = set(int(x) for x in a_gates) | set(int(x) for x in b_gates)
    def _ok(pair):
        x, y = pair.split("-")
        return int(x) in have and int(y) in have
    hits = sum(1 for pair in FROZEN_TALK_LADDER if _ok(pair))
    return {"adjacency_hits": int(hits), "adjacency_bonus": int(min(hits, 3))}

def _throat_em_bonus(em_timing_honored: bool, hits: int) -> int:
    """+1 per satisfied throat adjacency proxy, cap 2; 0 if not paced."""
    if not em_timing_honored:
        return 0
    return int(min(max(hits, 0), 2))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"), ap.add_argument("b")
    ap.add_argument("--verbose", "--admin-debug", dest="verbose", action="store_true",
                    help="(legacy) emit debug artifacts; does not change stdout")
    ap.add_argument("--admin-out", help="Write admin-only JSON sidecar (stdout unchanged)")
    ns = ap.parse_args()

    a, b = _load(ns.a), _load(ns.b)

    # Public envelope (no numerics); stdout must be canonical and LF-terminated
    out_ab = compute_pair(a, b, debug=False)
    sys.stdout.buffer.write(serialize(out_ab))

    # Optional admin sidecar (never mutates stdout)
    if ns.admin_out:
        a_g = list(map(int, a.get("gates", [])))
        b_g = list(map(int, b.get("gates", [])))
        admin = _adjacency_metrics(a_g, b_g)
        em_ok = os.getenv("HD_EMOTIONAL_TIMING_HONORED", "0") == "1"
        admin["throat_em_bonus"] = _throat_em_bonus(em_ok, admin["adjacency_hits"])
        Path(ns.admin_out).write_bytes(serialize(admin))

    # Legacy verbose artifacts (unchanged behavior)
    if ns.verbose:
        art = Path("artifacts"); art.mkdir(exist_ok=True)
        # AB debug snapshot
        (art / "dyad_AB_debug.json").write_text(
            json.dumps(out_ab, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            encoding="utf-8"
        )
        # Symmetric BA snapshot (debug=True for dev audit)
        out_ba = compute_pair(b, a, debug=True)
        (art / "dyad_BA_debug.json").write_text(
            json.dumps(out_ba, ensure_ascii=False, separators=(",", ":"), sort_keys=True),
            encoding="utf-8"
        )

if __name__ == "__main__":
    main()
