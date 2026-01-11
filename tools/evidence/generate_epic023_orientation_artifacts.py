#!/usr/bin/env python3
"""Generate EPIC023-specific orientation demo artifacts from canonical orientation demo output."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORIENTATION_TXT = ROOT / "audit/gates/topology/orientation_demo.txt"
OUTPUT_DIR = ROOT / "artifacts/hde-epic023_orientation_demo"


def parse_orientation_txt() -> dict:
    """Parse the orientation_demo.txt and extract key information."""
    if not ORIENTATION_TXT.exists():
        raise SystemExit(f"ERROR: {ORIENTATION_TXT} does not exist. Run tools/evidence/orientation_demo.py first.")
    
    text = ORIENTATION_TXT.read_text(encoding="utf-8")
    lines = text.strip().split("\n")
    
    total_artifacts = None
    status = None
    issues = []
    
    for line in lines:
        if line.startswith("total_artifacts:"):
            total_artifacts = int(line.split(":", 1)[1].strip())
        elif line.startswith("status:"):
            status = line.split(":", 1)[1].strip()
        elif line.startswith("- "):
            issues.append(line[2:])
    
    return {
        "total_artifacts": total_artifacts,
        "status": status,
        "issues": issues,
    }


def generate_report_json(parsed: dict) -> dict:
    """Generate the orientation_demo_report.json structure."""
    return {
        "schema": "orientation_demo_report",
        "version": "1.0",
        "status": parsed["status"],
        "total_artifacts": parsed["total_artifacts"],
        "issues_count": len(parsed["issues"]),
        "issues": parsed["issues"] if parsed["issues"] else [],
        "source": "audit/gates/topology/orientation_demo.txt",
        "note": "Generated from canonical orientation demo output for EPIC023 acceptance validation",
    }


def generate_sample_result() -> dict:
    """Generate a sample result demonstrating orientation demo structure."""
    return {
        "schema": "orientation_demo_sample",
        "version": "1.0",
        "description": "Sample orientation demo result structure",
        "sample_artifact_key": "example.artifact",
        "sample_checks": [
            "sha256_match",
            "size_match",
            "proof_exists",
            "mtime_captured",
        ],
        "note": "This is a sample structure demonstrating the orientation demo validation pattern",
    }


def main() -> None:
    """Generate EPIC023 orientation demo artifacts."""
    # Parse the canonical orientation demo output
    parsed = parse_orientation_txt()
    
    # Generate the report and sample structures
    report = generate_report_json(parsed)
    sample = generate_sample_result()
    
    # Write outputs
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    report_path = OUTPUT_DIR / "orientation_demo_report.json"
    sample_path = OUTPUT_DIR / "sample_result.json"
    
    # Write with canonical JSON formatting (UTF-8, sorted keys, compact, LF-terminated)
    report_bytes = (json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    sample_bytes = (json.dumps(sample, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    
    report_path.write_bytes(report_bytes)
    sample_path.write_bytes(sample_bytes)
    
    print(f"Generated: {report_path.relative_to(ROOT)}")
    print(f"Generated: {sample_path.relative_to(ROOT)}")
    print(f"Status: {report['status']}")
    print(f"Total artifacts: {report['total_artifacts']}")
    print(f"Issues count: {report['issues_count']}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        if e.code:
            print(str(e), file=sys.stderr)
        sys.exit(e.code if e.code else 0)
