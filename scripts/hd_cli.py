#!/usr/bin/env python3
# Ensure repo-root is on sys.path for direct script runs
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import argparse, json, hashlib
from engine.stable.sercanon import serialize
from core.pipeline.compute import compute_pair

def _load(p: str):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def _public_without_admin(d: dict) -> dict:
    # Drop any admin/debug key if present (public is numeric-free)
    return {k: v for k, v in d.items() if k != "_admin_debug"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--admin-out", help="Write admin debug sidecar (stdout unchanged)")
    ns = ap.parse_args()

    a, b = _load(ns.a), _load(ns.b)

    # Compute public result (no admin/debug)
    out_ab = compute_pair(a, b, debug=False)
    public = _public_without_admin(out_ab)

    # Preimage hash coupling: sha256( sercanon(preimage_without_hash) )
    preimage = dict(public)
    preimage.pop("idempotence_hash", None)
    pre_b = serialize(preimage)  # bytes, LF-terminated
    public["idempotence_hash"] = _sha256(pre_b)

    # Optional admin sidecar (does not affect stdout)
    if ns.admin_out:
        dbg = compute_pair(a, b, debug=True)
        admin_payload = dbg.get("_admin_debug", dbg)
        with open(ns.admin_out, "wb") as f:
            f.write(serialize(admin_payload))  # LF-terminated

    # STDOUT: canonical public bytes (LF-terminated)
    sys.stdout.buffer.write(serialize(public))

if __name__ == "__main__":
    main()
