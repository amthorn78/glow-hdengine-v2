---
artifact_type: WORKING_STATE_CHECKPOINT
artifact_id: HDE-EPIC040-QA90-CHECKPOINT
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.1.md (checks 1 to 10; preserved unchanged)
change_class: EPIC
change_id: HDE-EPIC040
stage: QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23)
state: TASK_READY
author: Kronos-23 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
time_utc: 2026-09-29
---

# HDE-EPIC040 — QA-90 working-state checkpoint v1.2

| Field | Value |
| --- | --- |
| Task | Convert the Product Owner's selection "Task to run: 11" of the approved QA Plan v1.2 into a bounded QA task |
| Result | `TASK_READY`; no `QA_PREEXECUTION_FINDING` |
| Collection | `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.2.md`, task T11 `open-rails-showcompat-vendor`, attempt 1 |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.2.md` |
| Approved base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010 |
| Approving review | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`, SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025 |
| PF10 read | v13.4.2 on `main` (SHA-256 c53b8d102d255bf55e58d621a87efee3878515e23a6dbab2652d9cf5142c5919); v13.4.4 in the local working tree, not on `main`, reviewed at the Product Owner's direction (new addenda 2.32 and 2.33). T11 meets addendum 2.33: a live vendor call under open rails with synthetic data only |
| Observed revision | `3c29ef4cbb6dbcc9a1a6b38ffff17ef065cba09c` (origin/main) |
| Executors | Vendor commands 4 to 28: the Product Owner in person. Recording preflight, commands 1 to 3 and the recording: the QA-100 operator session (identity PENDING) |
| Venue and storage | Run B checkout `/home/nathan/hde-epic040-qa`; evidence commit on `qa/hde-epic040-qa100-plan-v1.2-run-20260929` (ruling LR-01 item 6), with the storage authorization asked at the start of QA-100 |
| Request limit | Two CLI invocations, at most 12 HTTP requests to HumanDesignAPI (collection §5) |
| Authoring checks | 43 command blocks extracted from the written file and dry-run in a scratch clone with fake keys and a stub `hdctl` (no vendor call by Kronos); PASS, secret-detection, empty-capture and early-stop `TOOLING_BLOCKED` paths all behaved as the task states; one writer defect found and corrected before issue (collection §2.4) |
| Carried open items | Collection §7, including two formatting defects observed in the PF10 v13.4.4 working-tree copy |
| Next stage | QA-100 — Execute Bounded QA Task — 091426.1 |
| Not done by QA-90 | Execution, a vendor call, evidence acceptance, a PASS declaration, step selection, a rerun, merge, PF-Canon or PF10 edits, addendum production |
| Commit and pull request | Recorded after they exist, in the session's final response; this file does not carry its own commit identity |

## Canon relied on

As recorded in the "Canon relied on" section of `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.2.md`: HDE Build Notes (v13.4.2 on `main`: 2.27 "Evidence storage", 2.28, 2.29; v13.4.4 working-tree copy: 2.32, 2.33); Glow QA Guide §3.3, §3.4.7 to §3.4.10, §3.5.5 to §3.5.7, §4.4.1 to §4.4.7, §9.2.15.5, §10.6, §10.8, §11.1; Plan Templates "Step-log header schema expectations (required; v2)", "Vendor-dependent steps (rails-scoped)", "Proof-class and controlled vendor-smoke boundary"; HDE CLI/API Vendor Ref §3.7, §7.3.9; Glow Infrastructure §2.7; Technical Writing Best Practices "Truth and source fidelity".
