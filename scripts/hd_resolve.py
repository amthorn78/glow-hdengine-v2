#!/usr/bin/env python3
# repo-root on sys.path
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import argparse, pathlib
from core.config.toggles_resolver import resolve_toggles
from engine.stable.sercanon import serialize

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Write resolver envelope to this path (LF-terminated)")
    ns = ap.parse_args()

    resolved, frozen_sha, applied = resolve_toggles()
    env = {
        "ok": True,
        "schema": "v1",
        "toggles_sha": frozen_sha,
        "overrides_applied": bool(applied),
    }
    p = pathlib.Path(ns.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(serialize(env))

if __name__ == "__main__":
    main()
