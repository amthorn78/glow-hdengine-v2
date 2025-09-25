#!/usr/bin/env python3
# repo-root on sys.path for direct script runs
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import argparse, json, sys, pathlib
from core.pipeline.compute import compute_pair

def _load(p): return json.load(open(p, "r", encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"), ap.add_argument("b")
    ap.add_argument("--verbose", "--admin-debug", dest="verbose", action="store_true")
    ns = ap.parse_args()

    a, b = _load(ns.a), _load(ns.b)
    out_ab = compute_pair(a, b, debug=ns.verbose)

    # Always print exactly one minified JSON object to stdout (exit 0)
    sys.stdout.write(json.dumps(out_ab, ensure_ascii=False, separators=(",",":"), sort_keys=True) + "\n")

    # When verbose, also emit symmetric debug artifacts for audit
    if ns.verbose:
        art = pathlib.Path("artifacts"); art.mkdir(exist_ok=True)
        (art/"dyad_AB_debug.json").write_text(
            json.dumps(out_ab, ensure_ascii=False, separators=(",",":"), sort_keys=True), encoding="utf-8"
        )
        out_ba = compute_pair(b, a, debug=True)
        (art/"dyad_BA_debug.json").write_text(
            json.dumps(out_ba, ensure_ascii=False, separators=(",",":"), sort_keys=True), encoding="utf-8"
        )

if __name__ == "__main__":
    main()
