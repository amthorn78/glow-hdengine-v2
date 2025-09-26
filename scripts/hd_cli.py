#!/usr/bin/env python3
# repo-root on sys.path for direct script runs
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import argparse, json, pathlib
from core.pipeline.compute import compute_pair
from engine.stable.hashcouple import finalize_envelope
from engine.stable.sercanon import serialize

def _load(p): 
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def _public_envelope(raw: dict) -> dict:
    # Drop any admin/debug keys from the public envelope
    pub = dict(raw)
    pub.pop("_admin_debug", None)
    pub.pop("idempotence_hash", None)
    return pub

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"), ap.add_argument("b")
    ap.add_argument("--debug", action="store_true", help="Compute admin debug payload too (stdout unchanged)")
    ap.add_argument("--admin-out", help="Write admin/debug sidecar JSON to this path (LF-terminated). Stdout unchanged.")
    ns = ap.parse_args()

    a, b = _load(ns.a), _load(ns.b)

    # 1) Compute PUBLIC stdout envelope from a single canonical serializer path
    public_raw = compute_pair(a, b, debug=False)
    pre_env = _public_envelope(public_raw)
    final_env, final_bytes, _h = finalize_envelope(pre_env)

    # stdout: exactly one LF, canonical bytes; NEVER include admin here
    sys.stdout.buffer.write(final_bytes)

    # 2) Optional admin sidecar: recompute with debug=True to gather internals
    if ns.admin_out or ns.debug:
        admin_raw = compute_pair(a, b, debug=True)
        # If user asked for a sidecar file, write LF-terminated canonical JSON
        if ns.admin_out:
            outp = pathlib.Path(ns.admin_out)
            outp.parent.mkdir(parents=True, exist_ok=True)
            outp.write_bytes(serialize(admin_raw))

if __name__ == "__main__":
    main()
