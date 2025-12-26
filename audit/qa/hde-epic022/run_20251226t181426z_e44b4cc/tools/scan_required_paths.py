#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--paths", nargs="+", required=True)
    args = ap.parse_args()

    rows = []
    missing = []
    for p in args.paths:
        exists = Path(p).exists()
        rows.append({"path": p, "exists": exists})
        if not exists:
            missing.append(p)

    out = {
        "captured_at_utc": utc_now(),
        "missing_count": len(missing),
        "missing_paths": missing,
        "paths": rows,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    raise SystemExit(0 if not missing else 10)  # 10 => FAIL_BEHAVIOR
if __name__ == "__main__":
    main()
