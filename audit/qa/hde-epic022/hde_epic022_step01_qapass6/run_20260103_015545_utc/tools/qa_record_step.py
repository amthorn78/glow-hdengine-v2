#!/usr/bin/env python3
import argparse, json, os
from datetime import datetime

ALLOWED_STATUS = {"PASS","FAIL_BEHAVIOR","FAIL_TOOLING","TOOLING_BLOCKED","N.A."}

def utc_now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def load_json(s: str, label: str, t):
    try:
        v = json.loads(s)
    except Exception as e:
        raise SystemExit(f"[qa_record_step] invalid {label}: {e}")
    if not isinstance(v, t):
        raise SystemExit(f"[qa_record_step] {label} must decode to {t.__name__}")
    return v

def ensure_manifest(path: str, epic_id: str) -> dict:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        return {"epic_id": epic_id, "runs": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if data.get("epic_id") != epic_id:
        raise SystemExit("[qa_record_step] manifest epic_id mismatch")
    if not isinstance(data.get("runs"), list):
        raise SystemExit("[qa_record_step] manifest missing runs[]")
    return data

def get_or_create_run(manifest: dict, run_id: str) -> dict:
    for r in manifest["runs"]:
        if r.get("run_id") == run_id:
            return r
    r = {"run_id": run_id, "steps": [], "created_at_utc": utc_now(), "updated_at_utc": utc_now()}
    manifest["runs"].append(r)
    return r

def upsert_step(run: dict, step: dict) -> None:
    steps = run.get("steps")
    if not isinstance(steps, list):
        run["steps"] = []
        steps = run["steps"]
    # Uniqueness-by-construction: upsert by check_id within run_id
    for i, s in enumerate(steps):
        if s.get("check_id") == step.get("check_id"):
            step["updated_at_utc"] = utc_now()
            steps[i] = step
            run["updated_at_utc"] = utc_now()
            return
    step["created_at_utc"] = utc_now()
    step["updated_at_utc"] = utc_now()
    steps.append(step)
    run["updated_at_utc"] = utc_now()

def read_text(p: str) -> str:
    if not os.path.exists(p):
        return f"<missing: {p}>"
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epic-id", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--check-id", required=True)
    ap.add_argument("--step-name", required=True)
    ap.add_argument("--command-json", required=True)
    ap.add_argument("--captured-env-json", required=True)
    ap.add_argument("--rails", required=True)
    ap.add_argument("--pf-refs-json", required=True)
    ap.add_argument("--intended-tokens-json", required=True)
    ap.add_argument("--claimed-tokens-json", required=True)
    ap.add_argument("--status", required=True)
    ap.add_argument("--exit-code", required=True, type=int)
    ap.add_argument("--started-at-utc", required=True)
    ap.add_argument("--ended-at-utc", required=True)
    ap.add_argument("--stdout-path", required=True)
    ap.add_argument("--stderr-path", required=True)
    ap.add_argument("--log-path", required=True)
    ap.add_argument("--manifest-path", required=True)
    args = ap.parse_args()

    if args.status not in ALLOWED_STATUS:
        raise SystemExit(f"[qa_record_step] invalid status: {args.status}")

    command = load_json(args.command_json, "command_json", str)
    captured_env = load_json(args.captured_env_json, "captured_env_json", dict)
    pf_refs = load_json(args.pf_refs_json, "pf_refs_json", list)
    intended = load_json(args.intended_tokens_json, "intended_tokens_json", list)
    claimed = load_json(args.claimed_tokens_json, "claimed_tokens_json", list)

    # PASS-only claim gating (hard)
    if args.status != "PASS" and len(claimed) != 0:
        raise SystemExit("[qa_record_step] claimed_tokens must be empty unless status=PASS")

    header = {
        "epic_id": args.epic_id,
        "run_id": args.run_id,
        "check_id": args.check_id,
        "step_name": args.step_name,
        "command": command,
        "captured_env": captured_env,
        "rails": args.rails,
        "pf_refs": pf_refs,
        "intended_tokens": intended,
        "claimed_tokens": claimed,
        "status": args.status,
        "exit_code": args.exit_code,
        "started_at_utc": args.started_at_utc,
        "ended_at_utc": args.ended_at_utc,
    }

    os.makedirs(os.path.dirname(args.log_path), exist_ok=True)
    with open(args.log_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(header, ensure_ascii=False) + "\n\n")
        f.write("---- STDOUT ----\n")
        f.write(read_text(args.stdout_path))
        if not f.tell() or not read_text(args.stdout_path).endswith("\n"):
            f.write("\n")
        f.write("\n---- STDERR ----\n")
        f.write(read_text(args.stderr_path))
        if not read_text(args.stderr_path).endswith("\n"):
            f.write("\n")

    manifest = ensure_manifest(args.manifest_path, args.epic_id)
    run = get_or_create_run(manifest, args.run_id)
    step_row = {
        "check_id": args.check_id,
        "step_name": args.step_name,
        "status": args.status,
        "exit_code": args.exit_code,
        "log_path": args.log_path,
        "pf_refs": pf_refs,
        "intended_tokens": intended,
        "claimed_tokens": claimed,
        "started_at_utc": args.started_at_utc,
        "ended_at_utc": args.ended_at_utc,
    }
    upsert_step(run, step_row)

    with open(args.manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

if __name__ == "__main__":
    main()
