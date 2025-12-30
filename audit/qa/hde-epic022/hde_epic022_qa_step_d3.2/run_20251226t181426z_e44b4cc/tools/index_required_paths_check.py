#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

REQUIRED_INDEX_PATHS = [
  "audit/gates/determinism/env_pins.log",
  "parity/errors_reader_cli.invalid_json.http.json",
  "parity/errors_reader_cli.invalid_json.cli.txt",
  "parity/errors_reader_cli.invalid_viewer_prefs.http.json",
  "parity/errors_reader_cli.invalid_viewer_prefs.cli.txt",
  "parity/errors_reader_cli.db_unavailable.http.json",
  "parity/errors_reader_cli.db_unavailable.cli.txt",
  "parity/errors_reader_cli.vendor_attempt_closed_rails.http.json",
  "parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt",
  "errors/schema_check/error_envelope_invalid_json.log",
  "errors/schema_check/error_envelope_invalid_viewer_prefs.log",
  "errors/schema_check/error_envelope_db_unavailable.log",
  "errors/schema_check/error_envelope_vendor_attempt_closed_rails.log",
  "errors/token_map/token_map.json",
  "artifacts/cli/showcompat/stdout.json",
  "artifacts/cli/showcompat/stdout.json.sha256",
  "artifacts/cli/showcompat/args.json",
  "artifacts/ops/internal_version/body_get.json",
  "artifacts/ops/internal_version/body_get.sha256",
  "artifacts/ops/internal_version/headers_get.txt",
  "artifacts/ops/internal_version/headers_head.txt",
]

ALT_CONDITIONALS = [
  "artifacts/ops/internal_version/cond_if_none_match_headers.txt",
  "artifacts/ops/internal_version/cond_if_modified_since_headers.txt",
  "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
  "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
]

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index-json", required=True)
    ap.add_argument("--out-json", required=True)
    args = ap.parse_args()

    idx_path = Path(args.index_json)
    raw = json.loads(idx_path.read_text(encoding="utf-8"))

    if not isinstance(raw, list):
        out = {
          "captured_at_utc": utc_now(),
          "index_json": args.index_json,
          "pass": False,
          "error": "INDEX.json is not a JSON array",
        }
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        raise SystemExit(10)

    paths = set()
    for ent in raw:
        if isinstance(ent, dict):
            p = ent.get("discovered_physical_path")
            if p:
                paths.add(p)

    missing = [p for p in REQUIRED_INDEX_PATHS if p not in paths]

    cond_ok = {
      "if_none_match": any(p in paths for p in [ALT_CONDITIONALS[0], ALT_CONDITIONALS[2]]),
      "if_modified_since": any(p in paths for p in [ALT_CONDITIONALS[1], ALT_CONDITIONALS[3]]),
    }
    cond_missing = [k for k,v in cond_ok.items() if not v]

    out = {
      "captured_at_utc": utc_now(),
      "index_json": args.index_json,
      "missing_paths": missing,
      "conditional_index_ok": cond_ok,
      "conditional_index_missing": cond_missing,
      "pass": (len(missing)==0 and len(cond_missing)==0),
    }
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    raise SystemExit(0 if out["pass"] else 10)

if __name__ == "__main__":
    main()
