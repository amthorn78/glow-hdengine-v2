#!/usr/bin/env python3
import argparse, json, time
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-json", required=True)
    ap.add_argument("--out-stable", required=True)
    ap.add_argument("--out-run", required=True)
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()

    scan = json.loads(Path(args.scan_json).read_text(encoding="utf-8"))

    lines = []
    lines.append("# D0 Scan — EPIC022 required paths")
    lines.append("")
    lines.append(f"run_id: {args.run_id}")
    lines.append(f"captured_at_utc: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    lines.append("")
    lines.append(f"missing_count: {scan['missing_count']}")
    lines.append("")
    if scan["missing_paths"]:
        lines.append("## Missing (FAIL_BEHAVIOR)")
        lines += [f"- {p}" for p in scan["missing_paths"]]
    else:
        lines.append("## Missing (none)")
    lines.append("")
    lines.append("## Full scan")
    for row in scan["paths"]:
        lines.append(f"- [{'x' if row['exists'] else ' '}] {row['path']}")

    Path(args.out_stable).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_run).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_stable).write_text("\n".join(lines) + "\n", encoding="utf-8")
    Path(args.out_run).write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
