# STEP-01 Report — HDE-EPIC022 / HDE Separation Pass 2 (qapass6)

- Evidence root: [audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc)
- Run ID: 20260103T015609Z; Epic: HDE-EPIC022; Check: STEP-01 (bootstrap_scaffold)
- Determinism pins captured in log header: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0
- Governed input snapshot: release_id.txt copied into 00_meta
- Artifacts directory is present and empty (no additional governed outputs for this step)

## Evidence files (indexed)
- [00_meta/env.sh](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/00_meta/env.sh)
- [00_meta/run_context.md](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/00_meta/run_context.md)
- [00_meta/release_id.txt](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/00_meta/release_id.txt)
- [qa_step_logs_manifest.json](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/qa_step_logs_manifest.json)
- [results/STEP-01.result.env](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/results/STEP-01.result.env) and [results/step-01.result.env](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/results/step-01.result.env)
- [step_logs/STEP-01.log](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/step_logs/STEP-01.log) and [step_logs/step-01.log](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/step_logs/step-01.log)
- [stdout/STEP-01.stdout.txt](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/stdout/STEP-01.stdout.txt) and [stdout/step-01.stdout.txt](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/stdout/step-01.stdout.txt)
- [stderr/STEP-01.stderr.txt](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/stderr/STEP-01.stderr.txt) and [stderr/step-01.stderr.txt](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/stderr/step-01.stderr.txt) (empty)
- [tools/qa_record_step.py](audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/tools/qa_record_step.py)

## Filedump

### 00_meta/env.sh
```bash
export EPIC_ID="HDE-EPIC022"
export RUN_ID="20260103T015609Z"
export EVIDENCE_ROOT="audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc"
```

### 00_meta/run_context.md
```markdown
# Live QA Run Context — HDE-EPIC022

- Execution venue: <FILL> (e.g., GitHub Codespaces)
- Target environment: <FILL> (prod endpoint via HDE_PROD_BASE_URL; local tests via pytest)
- Date (UTC): 2026-01-03T01:56:09Z
- Operators: <FILL>
- Canon precedence statement: PF10 — HDE-Build Notes governs where it speaks; Doc B caveats are implemented; this run is gitless.

```

### 00_meta/release_id.txt
```text
077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
```

### qa_step_logs_manifest.json
```json
{
  "epic_id": "HDE-EPIC022",
  "runs": [
    {
      "created_at_utc": "2026-01-03T01:56:53Z",
      "run_id": "20260103T015609Z",
      "steps": [
        {
          "check_id": "STEP-01",
          "claimed_tokens": [],
          "created_at_utc": "2026-01-03T01:56:53Z",
          "ended_at_utc": "2026-01-03T01:56:53Z",
          "exit_code": 0,
          "intended_tokens": [],
          "log_path": "audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc/step_logs/STEP-01.log",
          "pf_refs": [
            "PF10 — HDE-Build Notes §2.4",
            "PF10 — HDE-Build Notes §2.5",
            "PF10 — HDE-Build Notes §2.10",
            "PF10 — HDE-Build Notes §2.13"
          ],
          "started_at_utc": "2026-01-03T01:56:53Z",
          "status": "PASS",
          "step_name": "bootstrap_scaffold",
          "updated_at_utc": "2026-01-03T01:56:53Z"
        }
      ],
      "updated_at_utc": "2026-01-03T01:56:53Z"
    }
  ]
}
```

### results/STEP-01.result.env (uppercase)
```dotenv
STEP_ID=STEP-01
STATUS=PASS
RUN_ID=20260103T015609Z
EPIC_ID=HDE-EPIC022
```

### results/step-01.result.env (lowercase review copy)
```dotenv
STEP_ID=STEP-01
STATUS=PASS
RUN_ID=20260103T015609Z
EPIC_ID=HDE-EPIC022
```

### step_logs/STEP-01.log (uppercase)
```log
{"epic_id": "HDE-EPIC022", "run_id": "20260103T015609Z", "check_id": "STEP-01", "step_name": "bootstrap_scaffold", "command": "(bootstrap scaffold; created tools/qa_record_step.py, env.sh, run_context.md, release_id snapshot)", "captured_env": {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "PYTHONHASHSEED": "0"}, "rails": "LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "pf_refs": ["PF10 — HDE-Build Notes §2.4", "PF10 — HDE-Build Notes §2.5", "PF10 — HDE-Build Notes §2.10", "PF10 — HDE-Build Notes §2.13"], "intended_tokens": [], "claimed_tokens": [], "status": "PASS", "exit_code": 0, "started_at_utc": "2026-01-03T01:56:53Z", "ended_at_utc": "2026-01-03T01:56:53Z"}

---- STDOUT ----
[STEP-01] EPIC_ID=HDE-EPIC022
[STEP-01] RUN_ID=20260103T015609Z
[STEP-01] EVIDENCE_ROOT=audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc

---- STDERR ----

```

### step_logs/step-01.log (lowercase review copy)
```log
{"epic_id": "HDE-EPIC022", "run_id": "20260103T015609Z", "check_id": "STEP-01", "step_name": "bootstrap_scaffold", "command": "(bootstrap scaffold; created tools/qa_record_step.py, env.sh, run_context.md, release_id snapshot)", "captured_env": {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "PYTHONHASHSEED": "0"}, "rails": "LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "pf_refs": ["PF10 — HDE-Build Notes §2.4", "PF10 — HDE-Build Notes §2.5", "PF10 — HDE-Build Notes §2.10", "PF10 — HDE-Build Notes §2.13"], "intended_tokens": [], "claimed_tokens": [], "status": "PASS", "exit_code": 0, "started_at_utc": "2026-01-03T01:56:53Z", "ended_at_utc": "2026-01-03T01:56:53Z"}

---- STDOUT ----
[STEP-01] EPIC_ID=HDE-EPIC022
[STEP-01] RUN_ID=20260103T015609Z
[STEP-01] EVIDENCE_ROOT=audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc

---- STDERR ----

```

### stdout/STEP-01.stdout.txt (uppercase)
```text
[STEP-01] EPIC_ID=HDE-EPIC022
[STEP-01] RUN_ID=20260103T015609Z
[STEP-01] EVIDENCE_ROOT=audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc
```

### stdout/step-01.stdout.txt (lowercase review copy)
```text
[STEP-01] EPIC_ID=HDE-EPIC022
[STEP-01] RUN_ID=20260103T015609Z
[STEP-01] EVIDENCE_ROOT=audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc
```

### stderr/STEP-01.stderr.txt (uppercase)
```text
<empty>
```

### stderr/step-01.stderr.txt (lowercase review copy)
```text
<empty>
```

### tools/qa_record_step.py
```python
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
```
