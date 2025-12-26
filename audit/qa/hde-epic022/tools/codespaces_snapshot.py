#!/usr/bin/env python3
import argparse, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def sh(cmd: str) -> str:
    p = subprocess.run(["bash","-lc", cmd], capture_output=True, text=True)
    return (p.stdout or "").strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--epic-id", required=True)
    ap.add_argument("--manifest-path", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    secret_names = ["INTERNAL_VERSION_AUTH_HEADER"]
    secrets_present = {k: (k in os.environ and bool(os.environ.get(k))) for k in secret_names}

    snap = {
        "captured_at_utc": utc_now(),
        "epic_id": args.epic_id,
        "run_id": args.run_id,
        "tool_versions": {
            "python": sh("python --version || true"),
            "git": sh("git --version || true"),
            "jq": sh("jq --version || true"),
        },
        "rails_and_pins_names_only": {
            "LC_ALL": os.environ.get("LC_ALL",""),
            "LANG": os.environ.get("LANG",""),
            "TZ": os.environ.get("TZ",""),
            "SAFE_MODE": os.environ.get("SAFE_MODE",""),
            "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK",""),
            "APP_ENV": os.environ.get("APP_ENV",""),
        },
        "prod_target_selector_names_only": {
            "HDE_BASE_URL_is_set": bool(os.environ.get("HDE_BASE_URL")),
            "HDE_BASE_URL_name": "HDE_BASE_URL",
        },
        "secrets_presence_only": secrets_present,
        "qa_manifest_path": args.manifest_path,
    }

    out.write_text(json.dumps(snap, indent=2, sort_keys=True) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
