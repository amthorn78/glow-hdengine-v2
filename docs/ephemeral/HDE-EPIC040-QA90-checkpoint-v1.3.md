---
artifact_type: WORKING_STATE_CHECKPOINT
artifact_id: HDE-EPIC040-QA90-CHECKPOINT
artifact_version: "1.3"
predecessor: docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.2.md (collection v1.2, task T11; preserved unchanged)
change_class: EPIC
change_id: HDE-EPIC040
stage: QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23)
state: TASK_READY
author: Kronos-23 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
time_utc: 2026-09-29
---

# HDE-EPIC040 — QA-90 working-state checkpoint v1.3

| Field | Value |
| --- | --- |
| Task | Repeated QA-90 invocation: the Product Owner's selection "Task: 11" of the approved QA Plan v1.2, which collection v1.2 had already packaged as task T11 |
| Result | `TASK_READY`; no `QA_PREEXECUTION_FINDING` |
| Decision | Collection v1.2 was inspected in full, checked against canon on `main` and dry-run. It is reused except for five repairs, issued as collection v1.3 (§1.1 there). V-01: the stop rule for a vendor command that cannot be run as written skipped the secret scan once command 14 had run. V-02: the scan-to-body gate relied on the PO reading 87 and 91 `path:count` lines by eye, and had no rule for a failed scan. V-03: no status for a vendor command not run as written. V-04: retry wording. V-05: PF10 paths |
| Collection | `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md`, task T11 `open-rails-showcompat-vendor`, attempt 1 |
| Superseded for T11 | Collection v1.2 (SHA-256 6dec3bae15580fe88ee8994368ef2fa6dfb95d0b4dc20478f7c54810b717c9b3), checkpoint v1.2 and handoff v1.2, all preserved unchanged. v1.2's T11 was never executed: no branch on `origin` holds check 11 evidence, and the Run B branch is still at `345148b` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.3.md` |
| Approved base | `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010 |
| Approving review | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`, SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025 |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.4.md` on `main` since `4ad12fe` (SHA-256 8f3edd03dea4badd36933ef23bb726e35d7a40840277413128bf4ccaf91c0e55), byte-identical to the working-tree copy collection v1.2 read. Addenda 2.32 and 2.33 read in full; T11 meets 2.33 |
| Observed revision | `4ad12fe4be4c8149b9159adb1abe7812a8b5da50` (origin/main) |
| Executors | Vendor commands 4 to 28, the displays D1 and D2, the quarantine commands Q1 and Q2 and writer W2: the Product Owner in person. Recording preflight, commands 1 to 3, Part C and the recording: the QA-100 operator session (identity PENDING) |
| Venue and storage | Run B checkout `/home/nathan/hde-epic040-qa`; evidence commit on `qa/hde-epic040-qa100-plan-v1.2-run-20260929` (ruling LR-01 item 6), with the storage authorization asked at the start of QA-100 |
| Request limit | Two CLI invocations, at most 12 HTTP requests to HumanDesignAPI (collection §5) |
| Authoring checks | Commands 14 and 15 run through the real `hdctl` under closed rails: `PROVIDER_REFUSED`, no dump. The 45 command blocks of collection §5 extracted from v1.3 and run in seven scenarios, each shell started with an empty environment, with fake keys and a stub `hdctl`; Kronos made no vendor call. Every recording published a valid 14-key header and an 11-entry manifest; no fake key or base URL appeared outside the quarantine directory; `git status` listed only §4.8 paths (collection §2.4) |
| Observation | This Kronos session's cloud environment has `HD_API_KEY`, `GEO_API_KEY`, `HDAPI_BASE_URL` and `DATABASE_URL` set, observed by name only; no value was read or printed. No Kronos command used them: the closed-rails parse check refused before any vendor configuration was read, and every dry-run shell started with an empty environment and fake values. Owner: Product Owner (environment configuration). Recorded because Glow QA Guide §3.5.7 bars automated agents from handling plaintext secrets |
| Carried open items | Collection §7 |
| Next stage | QA-100 — Execute Bounded QA Task — 091426.1 |
| Not done by QA-90 | Execution, a vendor call, evidence acceptance, a PASS declaration, step selection, a rerun, merge, PF-Canon or PF10 edits, addendum production |
| Commit and pull request | Recorded after they exist, in the session's final response; this file does not carry its own commit identity |

## Canon relied on

As recorded in the "Canon relied on" section of `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md`: HDE Build Notes v13.4.4 (whole-document search at this invocation; 2.27 "Evidence storage", 2.28, 2.29, 2.32, 2.33); HDE Governance §3.4; Glow QA Guide §3.3 and §3.5.5 to §3.5.7, and as read at QA-110 §3.4.7 to §3.4.10, §4.4.1 to §4.4.7, §9.2.15.5, §10.6, §10.8 and §11.1; Plan Templates "Step-log header schema expectations (required; v2)", "Vendor-dependent steps (rails-scoped)" and "Proof-class and controlled vendor-smoke boundary (required when applicable)"; HDE CLI/API Vendor Ref §1, §3.7, §7.3.9; Glow Infrastructure §2.7; Technical Writing Best Practices "Truth and source fidelity".
