# Prompt Template — Generate QA Session Master Report (General Use)

Use this prompt with Copilot Chat after running any QA session.

```text
Create one single markdown master report for this QA session.

Inputs:
- EPIC_ID: <epic id>
- STEP_IDS: <comma-separated step ids, for example po-001, po-002, po-003>
- CHECKS_ROOT: <checks root path, for example audit/qa/<epic-folder>/checks>
- OUTPUT_REPORT_PATH: <target report path>
- PLAN_FILE: <approved plan file path>
- APPROVAL_FILE: <approval/caveats file path>
- PREVIOUS_REPORT_FILE: <previous report file path>
- PF_CANON_SET: <canon refs used in session>
- HARNESSED_COMMAND_PATTERN: <if applicable, for example python audit/qa/<epic-folder>/00_meta/live_qa_harness.py <check-id>>

Required output behavior:
1) Produce exactly one consolidated report at OUTPUT_REPORT_PATH.
2) Cover all steps in STEP_IDS in one file.
3) Include ALL actions executed in-session:
- preflight commands
- execution commands
- verification actions
- report-generation actions
4) Include full evidence mapping:
- per-step deliverables (primary.log, primary.log.path_proof.txt, result.json)
- supporting evidence files referenced by pass criteria
5) Include explicit extracted proof facts from result.json and primary.log for each step.
6) Include pass/fail criteria resolution per step and overall verdict.
7) Include execution posture (rails/env/determinism) and confirm no scope violations (for example package installs or disallowed edits).
8) Keep all claims evidence-bound to repository files only; do not invent loci.
9) If any required file is missing, classify that step as TOOLING_BLOCKED and list missing paths.

Formatting requirements:
- Use these sections:
  - Version Metadata
  - Manifest Header
  - Execution Posture
  - Commands Executed
  - Action Timeline
  - Results Table
  - Primary Header Proof
  - Per-Check Outcome Proof
  - Artifact Map
  - Pass/Fail Criteria Resolution
  - Final Session Verdict
- Use concise bullets and exact file paths for every evidence statement.
- Do not edit governed evidence artifacts; only write/update OUTPUT_REPORT_PATH.

Validation before finalizing:
1) For each check in STEP_IDS, confirm existence of:
- CHECKS_ROOT/<check-id>/primary.log
- CHECKS_ROOT/<check-id>/primary.log.path_proof.txt
- CHECKS_ROOT/<check-id>/result.json
2) Confirm step status and key pass/fail facts directly from each result.json.
3) Confirm primary header provenance from each primary.log.
4) Confirm any additional claims using explicit supporting files.

Output constraints:
- If all steps pass, report PASS per step and overall PASS.
- If any step is TOOLING_BLOCKED, FAIL_TOOLING, or FAIL_BEHAVIOR, preserve that classification and explain evidence.
- Do not add acceptance-token claims unless directly present in evidence.
```
