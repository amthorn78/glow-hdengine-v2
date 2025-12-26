#!/usr/bin/env python3
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--proof", required=True)
    args = ap.parse_args()

    target = Path(args.target)
    proof = Path(args.proof)

    if not target.exists():
        print(f"FAIL: target missing: {target}")
        return 3
    if not proof.exists():
        print(f"FAIL: proof missing: {proof}")
        return 3

    txt = proof.read_text(encoding="utf-8", errors="replace")
    if str(target) not in txt:
        print("FAIL: proof does not reference target path")
        print(f"  target={target}")
        print(f"  proof={proof}")
        return 1

    t_m = target.stat().st_mtime
    p_m = proof.stat().st_mtime
    if p_m + 1e-6 < t_m:
        print("FAIL: proof appears older than target (freshness)")
        print(f"  target_mtime={t_m}")
        print(f"  proof_mtime={p_m}")
        return 1

    print("PASS")
    print(f"  target={target}")
    print(f"  proof={proof}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
