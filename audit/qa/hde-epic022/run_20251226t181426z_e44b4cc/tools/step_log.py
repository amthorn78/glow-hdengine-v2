#!/usr/bin/env python3
import argparse, json, os, re, subprocess, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path

STATUS_PASS = "PASS"
STATUS_FAIL_BEHAVIOR = "FAIL_BEHAVIOR"
STATUS_FAIL_TOOLING = "FAIL_TOOLING"
STATUS_TOOLING_BLOCKED = "TOOLING_BLOCKED"
STATUS_PARKED = "PARKED"

def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()

def sanitize_command(cmd: str) -> str:
    cmd = re.sub(r"(Authorization:\s*)([^\s\"']+)", r"\1[REDACTED]", cmd, flags=re.IGNORECASE)
    cmd = re.sub(r"(INTERNAL_VERSION_AUTH_HEADER=)(.+)", r"\1[REDACTED]", cmd, flags=re.IGNORECASE)
    return cmd

def ensure_parent(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)

def map_rc_to_status(rc: int) -> str:
    if rc == 0: return STATUS_PASS
    if rc == 2: return STATUS_TOOLING_BLOCKED
    if rc == 3: return STATUS_PARKED
    if rc == 10: return STATUS_FAIL_BEHAVIOR
    return STATUS_FAIL_TOOLING

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-id", required=True)
    ap.add_argument("--log-path", required=True)
    ap.add_argument("--manifest-path", required=True)
    ap.add_argument("--rails", required=True)
    ap.add_argument("--pf-refs", required=True)
    ap.add_argument("--tokens", default="")
    ap.add_argument("--command", required=True)
    args = ap.parse_args()

    check_id = args.check_id
    log_path = Path(args.log_path)
    manifest_path = Path(args.manifest_path)

    ensure_parent(log_path); ensure_parent(manifest_path)

    cmd = args.command
    cmd_s = sanitize_command(cmd)

    started = utc_now()
    proc = subprocess.run(["bash", "-lc", cmd], capture_output=True, text=False)
    ended = utc_now()

    rc = proc.returncode
    status = map_rc_to_status(rc)

    out_b = proc.stdout or b""
    err_b = proc.stderr or b""

    header_lines = [
        f"check_id: {check_id}",
        f"status: {status}",
        f"started_at_utc: {started}",
        f"ended_at_utc: {ended}",
        f"rails: {args.rails}",
        f"pf_refs: {args.pf_refs}",
        f"tokens: {args.tokens}".rstrip(),
        f"command: {cmd_s}",
        f"stdout_sha256: {sha256_bytes(out_b)}",
        f"stderr_sha256: {sha256_bytes(err_b)}",
        f"exit_code: {rc}",
        "",
    ]
    with log_path.open("wb") as f:
        f.write(("\n".join(header_lines)).encode("utf-8"))
        f.write(b"--- stdout ---\n"); f.write(out_b)
        f.write(b"\n--- stderr ---\n"); f.write(err_b)

    rec = {
        "check_id": check_id,
        "status": status,
        "started_at_utc": started,
        "ended_at_utc": ended,
        "rails": args.rails,
        "pf_refs": args.pf_refs,
        "tokens": [t for t in (args.tokens.split() if args.tokens else [])],
        "log_path": str(log_path),
        "stdout_sha256": sha256_bytes(out_b),
        "stderr_sha256": sha256_bytes(err_b),
        "exit_code": rc,
    }

    existing = []
    if manifest_path.exists():
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
            if not isinstance(existing, list): existing = []
        except Exception:
            existing = []
    existing.append(rec)
    manifest_path.write_text(json.dumps(existing, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    sys.exit(rc)

if __name__ == "__main__":
    main()
