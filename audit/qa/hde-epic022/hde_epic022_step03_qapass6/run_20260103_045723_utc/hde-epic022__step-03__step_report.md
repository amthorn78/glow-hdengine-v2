# STEP-03 Report — HDE-EPIC022 / HDE Separation Pass 2 (qapass6)

## Step Results
- What was run: Approved Plan STEP-03 command block (open rails) to generate internal_version_bundle using artifacts/math/release_id.txt, then pytest -q tests/qa/test_epic022_acceptance_scaffold.py -k internal_version_bundle, then file_list emission, all wrapped in qa_record_step; artifacts copied into bundle_root and predicates executed.
- Key outputs: qa_record_step logged; stderr reported `python: can't open file '/workspaces/glow-hdengine-v2/tools/ops/internal_version_bundle.py': [Errno 2] No such file or directory`; file_list.txt absent; predicates failed at BUNDLE_FILE_COUNT (0).
- Final step outcome: FAIL_TOOLING (tool missing), BUNDLE_FILE_COUNT=0, EXIT_CODE=2.

## Repository Changes
- Summary: Added STEP-03 evidence bundle under run_20260103_045723_utc capturing FAIL_TOOLING; recorded deviation explaining missing internal_version_bundle tool.
- Changed files:
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/meta/evidence_root.txt
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/results/step-03.result.env
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/step_logs/step-03.log
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/stdout/step-03.stdout.txt
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/stderr/step-03.stderr.txt
  - audit/qa/hde-epic022/hde_epic022_step03_qapass6/deviations.md

## Evidence Filedump (complete)

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/meta/evidence_root.txt
Contents:
```
audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc
```

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/results/step-03.result.env
Contents:
```dotenv
STEP_ID=STEP-03
STATUS=FAIL_TOOLING
EXIT_CODE=2
BUNDLE_FILE_COUNT=0
```

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/step_logs/step-03.log
Contents:
```log
{"epic_id": "HDE-EPIC022", "run_id": "20260103T015609Z", "check_id": "STEP-03", "step_name": "internal_version_bundle", "command": "set -euo pipefail\n\nif [ ! -f \"artifacts/math/release_id.txt\" ]; then\n  echo \"[STEP-03] Missing required local file: artifacts/math/release_id.txt\" >&2\n  exit 20\nfi\n\nif [ -z \"${HDE_PROD_BASE_URL:-}\" ]; then\n  echo \"[STEP-03] Missing required input: HDE_PROD_BASE_URL\" >&2\n  exit 20\nfi\n\nOUT_DIR=\"${EVIDENCE_ROOT}/artifacts/internal_version_bundle\"\nmkdir -p \"${OUT_DIR}\"\n\npython tools/ops/internal_version_bundle.py \\\n  --release-id-path \"artifacts/math/release_id.txt\" \\\n  --out-dir \"${OUT_DIR}\"\n\npytest -q tests/qa/test_epic022_acceptance_scaffold.py -k internal_version_bundle\n\nfind \"${OUT_DIR}\" -type f -maxdepth 2 | sort > \"${OUT_DIR}/file_list.txt\"\necho \"[STEP-03] bundle_file_count=$(cat \"${OUT_DIR}/file_list.txt\" | wc -l | tr -d ' ')\"", "captured_env": {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "prod", "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "PYTHONHASHSEED": "0"}, "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "pf_refs": ["PF10 — HDE-Build Notes §2.4", "PF10 — HDE-Build Notes §2.5", "PF10 — HDE-Build Notes §2.13", "PF10 — HDE-Build Notes §2.18"], "intended_tokens": [], "claimed_tokens": [], "status": "FAIL_TOOLING", "exit_code": 2, "started_at_utc": "2026-01-03T04:57:24Z", "ended_at_utc": "2026-01-03T04:57:24Z"}

---- STDOUT ----


---- STDERR ----
python: can't open file '/workspaces/glow-hdengine-v2/tools/ops/internal_version_bundle.py': [Errno 2] No such file or directory
```

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/stdout/step-03.stdout.txt
Contents:
```text
<empty>
```

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/run_20260103_045723_utc/stderr/step-03.stderr.txt
Contents:
```text
python: can't open file '/workspaces/glow-hdengine-v2/tools/ops/internal_version_bundle.py': [Errno 2] No such file or directory
```

### Path: audit/qa/hde-epic022/hde_epic022_step03_qapass6/deviations.md
Contents:
```markdown
DEV-01
- What changed: STEP-03 halted with FAIL_TOOLING (exit_code=2) because the plan command could not open tools/ops/internal_version_bundle.py; bundle artifacts were not generated and BUNDLE_FILE_COUNT remained 0.
- Why: Repository reality lacks the required tool (tools/ops/internal_version_bundle.py), so the Approved Plan command failed immediately when invoked.
- Original plan reference: Approved Plan — Step ID: STEP-03
- Commands actually run: see run_20260103_045723_utc stdout/step-03.stdout.txt (empty) and stderr/step-03.stderr.txt (missing tool message); full command captured in run_20260103_045723_utc/step_logs/step-03.log.
- Evidence files impacted: run_20260103_045723_utc/results/step-03.result.env (STATUS=FAIL_TOOLING, EXIT_CODE=2, BUNDLE_FILE_COUNT=0), run_20260103_045723_utc/step_logs/step-03.log, run_20260103_045723_utc/stdout/step-03.stdout.txt, run_20260103_045723_utc/stderr/step-03.stderr.txt; artifacts/internal_version_bundle/file_list.txt is absent because the tool failed to run.
```
