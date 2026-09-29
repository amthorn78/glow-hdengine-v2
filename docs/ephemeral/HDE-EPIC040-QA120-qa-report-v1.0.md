---
artifact_type: QA_REPORT
artifact_id: HDE-EPIC040-QA120-QA-REPORT
artifact_version: "1.0"
predecessor: none. This is the first final QA Report for HDE-EPIC040. No QA_INTERIM_STATUS was issued for this run
verdict: PASS
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-120 / QA Plan v1.2 complete run (checks 1 to 12)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-120 — Create Final QA Report and RCA — 091426.1 (Notion 3db4590a05eb81589d21e798cf38e8ba; page as of 2026-09-24T15:53:04.131Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
qa_rca: docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md (QA_RCA_ID HDE-EPIC040-QA120-QA-RCA, v1.0)
specification: docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md (approved v1.1; CHANGE_CLASS EPIC; Thoth-17 APPROVE 2026-09-08T13:23:24Z; SHA-256 43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (APPROVE by Isis-52, 2026-09-28T00:26:24Z; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
evidence_of_record: branch qa/hde-epic040-qa100-plan-v1.2-run-20260929 at commit 787bb97b58b638d6b307cad6d76484c883c58aec (the Run B stream of ruling LR-01; checks 1 to 10 stored at 345148b, check 11 at 380cf46, check 12 at 787bb97)
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d
observed_revision: 917909c75390c871c5710c5b60177bb53fd01919 (origin/main at this invocation)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.8.md (SHA-256 5fb9bad917a1a2c5a8cd86fa38ee0a2a6be824985a9685e97bf88091aff777ce; 424,735 bytes)
closure_receiver: CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1, in the continuing Isis session (Isis-50 session; execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-120 (QA-120 is not an addendum producer)
---

# HDE-EPIC040 — Final QA Report (QA-120), v1.0

## 1. Verdict

| Field | Value |
| --- | --- |
| `QA_REPORT_ID` | `HDE-EPIC040-QA120-QA-REPORT`, v1.0 (this file) |
| `QA_RCA_ID` | `HDE-EPIC040-QA120-QA-RCA`, v1.0: `docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md` |
| Verdict | **`PASS`** |
| Run state | Complete. The Product Owner selected all 12 checks of QA Plan v1.2. Each was executed, recorded and accepted at QA-110 with per-task result `PASS` in both result layers of Plan §12. No check is unexecuted, blocked or waiting, and no rerun or escalation is open (§3) |
| Why `PASS` | Every criterion that the approved Plan requires this run to satisfy is satisfied. Every [E] and [K] predicate of the 12 checks is `PASS` (§5), and the evidence of record re-verifies at this invocation (§6). Each Specification criterion AC040-01 to AC040-09 is supported for the scope this run decides (§7.1). The approved Plan deferred two requirements and excluded them from the run. Canon treats such requirements as "blocked by environment, not as failed acceptance" (Glow QA Guide §3.3), so this Report records them as not supported for that reason, not as failures (§7.2) |
| Scope of the verdict | The whole-change QA verdict for the approved run of Plan v1.2 at tested source `0db3f0ef`. It establishes the stated predicates and proof classes only |
| Not established | Closure, which Isis decides at CL-E-10. Also acceptance, PF09 status movement, PF-Canon drainage, a close pack, deployment, release activation, full HumanDesignAPI conformance, deployed-service or live-database behavior, a ledger-bound QA manifest, and Index or Mirror publication (§13) |
| Recommendation to Isis | The QA outcome supports a `CLOSE` decision. None of the following is a QA failure, but Isis should weigh them: the two deferred requirements; the missing Index and Mirror registration of the QA evidence (QA50-F01); the QA evidence of record not yet being on `main`; and the canon-drain and close-pack axes, which are not claimed (§15) |
| Closure receiver | CL-E-10 in the continuing Isis session, the Isis-50 session (§16) |

## Canon relied on

Read from `docs/pfcanon/` on `main` at `917909c`.

- **HDE Build Notes v13.4.8** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.8.md`).
  - Its complete difference from v13.4.6, the version QA-110 T12 read, was read at this invocation. The difference is the version line, one index entry and addendum 2.36 "HDE-EPIC040-QA110 — QA Evidence Review of task T12 qa-closeout-deliverables v1.0", which records the T12 review and routes the completed run here. It states no new rule.
  - Read in full at this invocation: 2.29 "PF10-CANON-001" (canon location; change-process documents, including reports and RCAs, are stored in `docs/ephemeral/`; governed evidence homes and writers are unchanged) and 2.33 "PF10-OPENRAILS-001" (a mandatory live vendor call under open rails with synthetic data; "A passing open-rails test proves only what it exercises").
  - Relied on as read earlier in this session: 2.32 and 2.35 (the earlier QA-110 records); 2.34 ("PF10-VENDOR-001"); 2.20 (readiness proven offline only); 2.23 and 2.25 (the C040-07 and C040-08 overlays); 2.28 (the QA-10 triage).
  - Whole-document search at this invocation for `QA-120`, `final QA report`, `QA_REPORT`, `QA_RCA`, `closure receiver`, `retrospective` and `PR04-F02`. The only QA-120 hits are routing and carried-item lines in 2.32, 2.35 and 2.36. PF10 states no rule for the final Report, the RCA or the PF09 later drain of HDE-SEPA005, so the Glow QA Guide, the Change Process Guide and the approved Plan govern them.
  - Addendum index checked for 2.1 to 2.36. The addenda that record this change's decisions are mapped to their source records in §17.1 and §17.2.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`), read at this invocation: §3.1.2 (a final Report and a separate RCA for every completed run; the RCA must not invent a failure); §3.1.3; §3.3 (pre-App no-user mode and deferral); §4.4.1 (proof surfaces); §9.2.15.5 to §9.2.15.8 (coverage accounting, required elements, acceptability language, evidence coherence); §10.7 (later-drain vocabulary); §10.8 (tested state, later divergence, claim separation); §11.1 (roles).
- **Change Process Guide** (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md`) §0.4.1, §0.4.1.1 to §0.4.1.3, read in full at this invocation, and the Close Gate lines that cite them.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`) §9 "Final QA Closeout Review + QA RCA", read in full at this invocation. It is used for compatible structure only, because Glow QA Guide §10.7 says a historical combined template "cannot collapse" the Report and the RCA.
- **HDE Build Checklist — Separation** (`docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`): Task HDE-SEPA005 and subtasks .1 to .5 (lines 1148 to 1213) and the Phase Notes line 171, read at this invocation.
- **Repository instruction (not PF-Canon)**: `AGENTS.md`, "Canon-first rule", "Evidence attribution, currentness and distinct decisions" and "Operating routes and authority".

In-flight documents. The extent of reading differs by input, and is stated here:
- **Read in full at this invocation:**
  - QA Plan v1.2 and QA-70 review v1.4;
  - the Live QA Guide, QA readiness, Reality Audit, Change Audit Triage and PO disposition;
  - the approval revocation, the planning-failure RCA v1.1 and the Alpha state record;
  - the OPS01 result and receipt, and DOC-20;
  - the QA-90 handoff RCA and the Alpha feedback brief.
- **Read in the parts this Report relies on:**
  - the three QA-110 reviews (results, per-task reviews, deviations, lineage, register, open items) and the T12 checkpoint;
  - the QA-100 results (front matter, deviation tables, executor identities);
  - the three collections (front matter and selections);
  - the QA Audit (its findings);
  - Specification v1.1 (§§1 to 4 and §11) and Implementation Plan v2.1 (§2.1, §3 and §8);
  - the decision lines of each delivered unit's lineage review and of each rescope and deferral record (§17);
  - the Isis-52 handoff and the front matter of QA-70 reviews v1.0 to v1.3 (§16).
- **Not re-read at this invocation:** the body of Implementation Plan review v2.1. Its decision is taken from the readiness record and HDE Build Notes 2.5, and its SHA-256 is pinned in §2. The QA-100 results and the QA-110 reviews were read in full earlier in this session, when they were reviewed or authored.

## 2. Inputs

Every input was resolved in `docs/ephemeral/` on `main` at `917909c`, and its SHA-256 was computed at this invocation. "Canon relied on" states how much of each was read.

| Input | SHA-256 | State |
| --- | --- | --- |
| `HDE-EPIC040-QA110-qa-evidence-review-t12-v1.0.md` | `6750ba29026380e7074afca6db230c822a4b853af77b93b679e1b9a9bd0b6210` | T12 `ACCEPT`; run complete |
| `HDE-EPIC040-QA110-checkpoint-t12-v1.0.md` | `7ff1d0e5fd902361ff75e332e1b93ee90e5df79a63f9d8d1c87be68b79b6a9a4` | Working state after T12 |
| `HDE-EPIC040-QA110-qa-evidence-review-t11-v1.0.md` | `c7abc4441a87d942c471ffcaa5388599e876263b3d26b5d740464200ac24ac64` | T11 `ACCEPT`; C040-10; K-05, K-06 |
| `HDE-EPIC040-QA110-qa-evidence-review-v1.0.md` | `2d45e7f0d252a3009ffb9cc0fe3d51b9652a7929eeb798bd618f2c497ab34ac3` | T01 to T10 `ACCEPT`; LR-01; K-01 to K-04 |
| `HDE-EPIC040-QA100-qa-execution-results-t12-v1.0.md` | `f09b3cb423b70217549591987b754577fb310e4581a3ebb73cbd16d84774a02f` | T12 attempt 1, `COMPLETE` |
| `HDE-EPIC040-QA100-qa-execution-results-t11-v1.0.md` | `0c884e8f6e56fdf959c68ec77860faef60ac1d2899494231745a3594e0dfe397` | T11 attempt 1, `COMPLETE` |
| `HDE-EPIC040-QA100-qa-execution-results-v1.1.md` | `afcb8df263c1e2295caa63e0fb213a3f1c48da8a8dca6ea0470eb1199944e041` | T01 to T10, `COMPLETE` (supersedes v1.0) |
| `HDE-EPIC040-QA90-qa-task-collection-v1.4.md` | `06498acbb5576f2e389affbf19d46f3371aebae6783eac17c91e3c8565e8d499` | T12, `TASK_READY` |
| `HDE-EPIC040-QA90-qa-task-collection-v1.3.md` | `c4ae999f9a38b7bcfabb66ac92ae542a1754682debd17fbd87c18fcc936de16b` | T11, `TASK_READY` |
| `HDE-EPIC040-QA90-qa-task-collection-v1.1.md` | `4d498d91382a16df3a73653172fa00d427402a9c12ad85e6d2589d699415f836` | T01 to T10, `TASK_READY` |
| `HDE-EPIC040-QA50-qa-plan-v1.2.md` | `330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010` | Approved base, immutable |
| `HDE-EPIC040-QA70-qa-plan-review-v1.4.md` | `e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025` | `APPROVE` by Isis-52 |
| `HDE-EPIC040-QA50-qa-audit-v1.0.md` | `1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df` | `AUDIT_COMPLETE` |
| `HDE-EPIC040-QA20-live-qa-guide-v1.0.md` | `5a61d77b8301dcee750eedb2916ecae1ec231d540b85028c022fa6d7883a9818` | `GUIDE_READY`; §4.3 and §5 superseded by canon (Plan v1.2 §2.1) |
| `HDE-EPIC040-QA10-qa-readiness-v1.0.md` | `cc513834b5274d6b5778347a5e0486ec82962f828e993231439e51ebcdf58185` | `READY_FOR_QA` |
| `HDE-EPIC040-QA10-reality-audit-v1.0.md` | `a527b074ba2d11df70f0fceaf0dd8c9978c23703bcfb666a68ff18ffe7528dbc` | `COMPLETE` |
| `HDE-EPIC040-QA10-change-audit-triage-v1.0.md` | `b36da0a8aeaff8e758384c06d4b2c478473ff4ae4991d197e0eefcc0ca321194` | `COMPLETE` |
| `HDE-EPIC040-QA10-po-disposition-v1.0.md` | `713e8c1f8c913ec13a59d18a17bb5a697b7cc4fc7ab3ff7635783012da204682` | Q-1 yes, Q-2 yes |
| `HDE-EPIC040-QA70-approval-revocation-v1.0.md` | `9a22372807085375bf507f101100ee52a2159e9598999f6f414fafefc1286d3c` | Review v1.2 `APPROVE` revoked |
| `HDE-EPIC040-QA70-planning-failure-rca-v1.1.md` | `a3f76e8c0ef3d1a50e2e30c68e30193237a1b9cb6f08f88cd89f1b9d03bd0381` | RCA of the rejected review v1.0 |
| `HDE-EPIC040-alpha-state-stopped-failed-at-qa-v1.0.md` | `e8a04409e350c30152a24ee1ec751e44784ab5226e05a984132fad4bca0b8177` | `ALPHA_STOPPED_FAILED_AT_QA`; resume at QA-70 |
| `HDE-EPIC040-specification-v1.1-approved.md` | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` | Approved v1.1 |
| `HDE-EPIC040-implementation-plan-v2.1.md` | `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` | Approved, immutable |
| `HDE-EPIC040-implementation-plan-review-v2.1.md` | `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` | `APPROVE` by Isis-50, 2026-09-09T13:36:43Z |
| `HDE-EPIC040-OPS01-ops-execution-result-v1.4.md` | `d1ed2c553618b097c2a3c8d21eb335e922fe7ec210544c9e3aa617b57b2ca4f8` | `PASS` |
| `HDE-EPIC040-OPS01-ops-task-receipt-v1.2.md` | `011495095591978ca5aca45e8138e4bd947a5f1b1274e13e7013d585c7caeebc` | `ACCEPT`; OPS01 complete |
| `HDE-EPIC040-DOC-20-documentation-completion-v1.0.md` | `a0298e957a997d5d1d03949e24cce17f34d630d6083807ca4e66cb253cb36aa7` | `COMPLETE` |

## 3. Reconciliation of the run

### 3.1 Selections and collections

| Collection | Product Owner selection | Tasks | Outcome |
| --- | --- | --- | --- |
| v1.0 | Plan v1.0 checks 1 to 10, under the QA-70 review v1.0 approval that the Product Owner rejected | T01 to T10 of Plan v1.0 | Not carried forward. Its execution evidence, commit `06b04a9` on branch `qa/hde-epic040-qa100-checks-1-10`, is historical record only (Alpha state record v1.0, "Resumption") |
| v1.1 | "Tasks: 1-10", 2026-09-28 | T01 to T10 = Plan v1.2 checks 1 to 10 | Executed. Evidence of record at `345148b` |
| v1.2 | "Task to run: 11" | T11 = check 11 | Never executed. Superseded for T11 by v1.3 |
| v1.3 | "Task: 11", 2026-09-29 | T11 = check 11 | Executed. Evidence at `380cf46` |
| v1.4 | "Selection: check 12", 2026-09-29 | T12 = check 12 | Executed. Evidence at `787bb97` |

The union of the executed selections is checks 1 to 12, which is every check of Plan v1.2 (Plan §10, §11). No required step is unselected or unexecuted.

### 3.2 Task, result and review of every check

| # | `check_id` | Task (collection) | Result record | QA-110 review | Evidence commit | Decision | Per-task result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | T01 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 2 | `step-0b-doc-delta-capture` | T02 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 3 | `ac040-08-evidence-validators` | T03 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 4 | `ac040-02-03-catalog-config` | T04 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 5 | `ac040-04-05-admission-identity` | T05 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 6 | `ac040-06-golden-comparison` | T06 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 7 | `ac040-07-gate-ingress-offline` | T07 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 8 | `ac040-04-09-compat-cli-offline` | T08 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 9 | `ac040-09-reader-http-in-process` | T09 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 10 | `sec-reader-http-live` | T10 (v1.1) | results v1.1 | review v1.0 | `345148b` | `ACCEPT` | `PASS` |
| 11 | `open-rails-showcompat-vendor` | T11 (v1.3) | result T11 v1.0 | review T11 v1.0 | `380cf46` | `ACCEPT` | `PASS` |
| 12 | `qa-closeout-deliverables` | T12 (v1.4) | result T12 v1.0 | review T12 v1.0 | `787bb97` | `ACCEPT` | `PASS` |

All records are under `docs/ephemeral/` with the prefix `HDE-EPIC040-`. The QA-100 results v1.0 are superseded by v1.1 and are preserved unchanged.

### 3.3 Deferred members, reruns, failures and evidence gaps

- **Deferred requirements.** The approved Plan (§2) deferred two requirements. They are not checks, and no command ran for them. Check 12 command 22 recorded them in its `DEFERRED` line. They are reported in §7.2.
- **Attempt lineage.** Two stored executions exist of collection v1.1 at the same tested source: Run A (`e5b671c`, branch `qa/hde-epic040-qa100-plan-v1.2`) and Run B (`345148b`). Ruling LR-01 (review v1.0 §4.2; HDE Build Notes 2.32) decided their status:
  - Run B is the evidence of record for checks 1 to 10.
  - Run A's executions of T01, T02 and T04 to T10 are attempt 1. For T10, Run A stored the probe captures but left no primary log and no receipt.
  - Run B's executions of T01, T02 and T04 to T10 are second executions made without the QA-110 decision that attempt 2 requires. They are recorded as a process deviation, and the one ordinary rerun of those checks is consumed.
  - T03 has one recorded execution, and its attempt label is unknown (LR-01 items 2, 3 and 7).
  - Checks 11 and 12 each have one execution, attempt 1.
- **Reruns.** None was routed or executed. No `attempt1_primary.log` or `rerun_note.md` exists. No Moon Loop was used, and no `00_meta/delta/` record exists.
- **Failures.** None in the evidence of record. Wherever Run A recorded or captured a result, it equals Run B's (review v1.0 §4.1).
- **Evidence gaps.** Three gaps remain, and none of them is a failed predicate (§11):
  - The HDE-EPIC040 QA evidence has no Index or Mirror registration (QA50-F01).
  - The evidence of record is on the Run B branch and not on `main`. At this invocation no pull request exists for that branch.
  - Run A's T03 outcome remains unknown (LR-01 item 7).
- **Plan v1.0 attempts.** The `06b04a9` executions under Plan v1.0 are not carried forward and are not counted as attempts of Plan v1.2 (Plan v1.2 §7.3; Alpha state record v1.0; QA-70 review v1.4 N-104).

### 3.4 Conclusion of the reconciliation

The approved run is complete. QA-120 therefore issues this final Report and the separate RCA, not a `QA_INTERIM_STATUS`.

## 4. Coverage vs QA Plan

This section applies Glow QA Guide §9.2.15.5, Plan §13 and the Change Process Guide §0.4.1.2. Every Plan step is listed in Plan order.

- **Evidence pointers.** Each pointer is the step's primary log, `audit/qa/hde-epic040/checks/<check_id>/primary.log`, on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97`. Each has a sibling `.path_proof.txt`. §6 gives each log's size and SHA-256.
- **Final accepted proof basis.** For every step it is the original planned receipt: no remediation or rerun receipt exists.

| # | `check_id` (D-goal) | Class and proof class | Coverage | Attempt | Accepted execution deviations | Closeout impact |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` (D0) | 1; ops and identity | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution (LR-01); D-03 count 2,092 against the reference 2,090, explained by two added parametrize cases | Non-blocker |
| 2 | `step-0b-doc-delta-capture` (D1) | 1; ops and identity | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 3 | `ac040-08-evidence-validators` (D2) | 2; local/offline (no vendor) | COVERED, fully evidenced | One recorded execution, label unknown | Venue rule not triggered (`umask` 0022, mode 644) | Non-blocker |
| 4 | `ac040-02-03-catalog-config` (D3) | 2; local/offline (no vendor) | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 5 | `ac040-04-05-admission-identity` (D4) | 2; local/offline (no vendor), with OPS01 corroboration | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 6 | `ac040-06-golden-comparison` (D5) | 2; local/offline (no vendor) | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 7 | `ac040-07-gate-ingress-offline` (D6) | 2; local/offline (no vendor) | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 8 | `ac040-04-09-compat-cli-offline` (D7) | 2; local/offline (no vendor) | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution. The three skips, reason "showcompat vendor calls require open rails", are recorded and contribute no proof | Non-blocker |
| 9 | `ac040-09-reader-http-in-process` (D8) | 2; in-process | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution | Non-blocker |
| 10 | `sec-reader-http-live` (D9) | 2; loopback HTTP under the closed posture | COVERED, fully evidenced | Run B, per LR-01 | Run B second execution; E-01, a one-space final argument (syntax-origin normalization); D-02, an operator-error repeat before the server started | Non-blocker |
| 11 | `open-rails-showcompat-vendor` (D10) | 3; vendor-backed, CLI-local vendor posture | COVERED, fully evidenced | Attempt 1 | D-01, execution of the vendor commands by the Product Owner's directed agent (authorized by HDE Build Notes 2.34); E-01, a syntax-origin normalization | Non-blocker |
| 12 | `qa-closeout-deliverables` (D11) | 2; local/offline (no vendor) | COVERED, fully evidenced | Attempt 1 | D-03, a runner script (observation O-01, lesson K-07); D-01, an automated QA/infra executor, as the collection permits | Non-blocker |

Two further rows cover the requirements the approved Plan deferred. They are not Plan steps. They are listed here so that no requirement is silently omitted.

| Deferred requirement (Plan §2) | Coverage | Unsatisfied claim | Reason and decision reference | Closeout impact |
| --- | --- | --- | --- | --- |
| Live, read-only Gate readiness against current rows | UNCOVERED by approved deferral. No check exists, no command ran and no artifact was expected | AC040-07, live part | Blocked by environment (Glow QA Guide §3.3). Decision references: QA-70 review v1.1 FND-003 and RL-09; QA-70 review v1.3 FND-101, RL-01 and RL-03; approved with Plan v1.2 by QA-70 review v1.4 | Caveat, carried to a future epic. Not a failure |
| Live DB Reader success path: Reader v1 and v2 success bytes over live HTTP on live current rows | UNCOVERED by approved deferral. No check exists, no command ran and no artifact was expected | AC040-09, live success path | As above | Caveat, carried to a future epic. Not a failure |

The Change Process Guide §0.4.1.2 asks for a rerun condition for each blocked step. It is the Plan §2 reactivation condition: a future epic, under its approved Specification and the applicable phased HDE Build Checklist, defines user-bound QA surfaces once the Glow App user model exists, and plans these requirements in its own QA Plan.

## 5. Per-task results, with every [K] predicate

The two result layers of Plan §12 are recorded for each check:
- the execution layer: step-log status, with every [E] predicate re-verified by Kronos against the captured output;
- the [K] layer: evaluated by Kronos at QA-110.

A check supports its criteria only when both layers pass.

| # | Execution layer ([E]) | [K] predicates | Per-task result |
| --- | --- | --- | --- |
| 1 | QA root absent before any write; Python 3.12.3; `harness_ready`; collection test exit 0 with `2092 tests collected`; every help command exit 0 with the required flags; admission printed `AdmittedMechanicsBundle 1.3.0 2026-08-24T18:04:49Z 45 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96 m10-channel-state-v1.0.0`; no `BLOCKER:` line | None | `PASS` |
| 2 | Both doc-delta surfaces absent before the write; written; byte-identical (`cmp` exit 0) | K1 LF-terminated, no BOM or CR, 2,867 bytes each, identical: `PASS`. K2 DD-01 to DD-12 each exactly once: `PASS`. K3 BLOCKERS and CAVEATS sections present: `PASS`. K4 no `BLOCKER:` line and BLOCKERS reads `none`: `PASS` | `PASS` |
| 3 | Venue evidence `0022` and `644 docs/evidence/INDEX.sha256`; the nine read-only validators exit 0; group G `587 passed`; governed-graph digest `29b7d9cbc557bc855d25b55b6cee9a562ef1f01840b788b1dad56ad7a4045150` before and after | None | `PASS` |
| 4 | Catalog digests captured; group A `304 passed` | K1 `catalog/channels_v1.json`: 36 rows with exactly the eight required keys, ascending unique Gate pairs and no null: `PASS`. K2 `catalog/magic10_mechanics_v1.json`: `config_id` `m10-channel-state-v1.0.0`, schema `magic10_mechanics_config.v1`, 20 unique signals, the three profiles, 10 category weights, and the two Balance operations with the other 18 signals on `weighted_state_sum_v1`: `PASS` | `PASS` |
| 5 | `--check-manifest-only` exit 0; manifest SHA-256 `52be4558…4afe96`; OPS01 `SHA256SUMS` 7 of 7 `OK`; group B `371 passed` | Binding: the attestation hashes to its `SHA256SUMS` line: `PASS`. K1 `release_id` and `manifest_sha256` both equal the manifest digest: `PASS`. K2 `validation_result` `PASS` and `release_admission` `PR06R_B_FINAL_PASS`: `PASS`. Recorded: `source_commit` `6f53d828a30101bb7cd6638f3695eb82c2b10979` | `PASS` |
| 6 | Two match runs exit 0 and byte-identical; the mismatch run exits 1 with stderr `GOLDEN_COMPARISON_MISMATCH:2`; tree digest equal before and after; group C `153 passed` | K1 match report: `ok` true, no mismatches, `M10-G001` to `M10-G008` each `match`, the `config_id`, and `candidate_release_id` equal to the manifest SHA-256: `PASS`. K2 mismatch report: `ok` false, both rows on `M10-G001`, one row `transcription.expected`, the other cases `match`: `PASS`. K3 the altered input differs from the fixture only in `M10-G001` `expected.signals[0].q`, 0 to 1: `PASS` | `PASS` |
| 7 | The three readiness commands exit 5 with `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID` and `READINESS_UNAVAILABLE`, each with empty stdout; group D `191 passed` | None | `PASS` |
| 8 | Group E `144 passed, 3 skipped`; each skip line and reason copied into PREDICATES | None | `PASS` |
| 9 | Group F `339 passed`, no skip | None | `PASS` |
| 10 | Server ready (`200`) before any probe; 22 probes captured; server stopped and port 8000 closed; `wc -l` printed `22` | K1 every probe has its expected status and code, all 22; S-26 is the HTML 404 known limitation O-P06a-22, observed and not failed: `PASS`. K2 S-02 to S-21 carry `content-type: application/json; charset=utf-8`, `cache-control: no-store` and no `etag`, and every error body is the canonical four-key envelope ending with one LF, 20 of 20: `PASS`. K3 no `Traceback`, `File "`, `psycopg`, `postgresql`, `gates` key, or number in a Reader error body, 22 of 22: `PASS` | `PASS` |
| 11 | Recording and readiness preflights; preflight matrix; both vendor runs exit 0 with empty stderr and non-empty output; byte identity of both output pairs; secret scan 0 everywhere; four files parse; closed posture restored | K1 both results are canonical `magic10_compat_result.v1` with exactly the six keys, `config_id` `m10-channel-state-v1.0.0`, `release_id` equal to the manifest SHA-256, 20 signals and 10 categories in canonical order: `PASS`. K2 both Reader v1 dumps have exactly six keys, `reader_version` `v1`, `categories` `[{"band":"Cool","id":"harmony"}]`, no JSON number, 330 bytes and one final LF: `PASS`. K3 the exercised-versus-inferred statement matches the captured stderr: `PASS` | `PASS` |
| 12 | E1 to E7: dependency gate (11 entries); readiness line; 25 digests captured; doc-delta surfaces identical after the DD-13 append; 13 path proofs pass check mode; updater `--check` and path validator exit 0 with the QA files present; coverage accounting with 12 `COVERAGE` lines and one `DEFERRED` line | K1 the manifest holds exactly one entry for each of checks 1 to 11: `PASS`. K2 each `log_path` is the concrete path the block states: `PASS`. K3 each primary log is non-empty, LF-terminated and has a v2 header whose status equals the manifest: `PASS`. K4 every supplementary file has its recorded SHA-256: `PASS`. K5 the coverage accounting lists every check: `PASS`. Step 8: both finalization proofs match their files: `PASS` | `PASS` |

Sources: review v1.0 §5 (checks 1 to 10), review T11 v1.0 §4 (check 11), review T12 v1.0 §4 (check 12).

## 6. Proof surfaces of the complete run

These are the Glow QA Guide §4.4.1 and Plan Templates §9 trust surfaces for every check.

**Re-verified at this invocation.** At `787bb97`, from `origin`:
- the SHA-256 and size of all 12 primary logs, the manifest and both doc-delta surfaces equal the values below and those of review T12 §6.2;
- the commit holds 41 paths under `audit/` for this change's QA root and doc deltas;
- neither the Human Evidence Index nor the Machine Mirror names `audit/qa/hde-epic040`.

**Common to every row** (review T12 §6.2).
- The manifest entry is present with the full `log_path` and status `PASS`.
- The header is `pf27.step_log_header.v2`, status `PASS` with an empty reason, and `exit_code` 0.
- `intended_tokens` and `claimed_tokens` are both `[]`.
- `captured_env` holds the six admitted keys, with `LC_ALL=C`, `LANG=C` and `TZ=UTC`.
- The path proof's size and SHA-256 equal the file.

| # | `check_id` | `captured_env` (`SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`) | `evidence_artifacts` | `timestamp_utc` | Primary log bytes and SHA-256 | Path proof `produced_at_utc` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | 1, 0, dev | 2 | 2026-09-29T01:31:42Z | 329,498, `f5b0f82c7974307bc52efac98232947726f534441fe07992ce384321aa7d5c1d` | 2026-09-29T13:48:00Z |
| 2 | `step-0b-doc-delta-capture` | 1, 0, dev | 3 | 2026-09-29T01:33:05Z | 15,951, `a64483b5460b75fbc4ce7028f238ff9e72a3f62c617c8e3361ab3d3c163d2c4b` | 2026-09-29T13:48:00Z |
| 3 | `ac040-08-evidence-validators` | 1, 0, dev | 1 | 2026-09-29T01:46:26Z | 28,542, `170171e1bbdb61b45c5650207425eabb63fea83597a2d0088023096ef1f11aed` | 2026-09-29T13:48:00Z |
| 4 | `ac040-02-03-catalog-config` | 1, 0, dev | 1 | 2026-09-29T01:48:22Z | 12,806, `6e622d117b9cbb9dc96845e61b34572c9d667bf62ed9d900a9cbebfaef65b5f6` | 2026-09-29T13:48:00Z |
| 5 | `ac040-04-05-admission-identity` | 1, 0, dev | 1 | 2026-09-29T01:50:07Z | 14,284, `ffa2a4629db34c415554f32ed88365641471f2995ac440c5b688b8b7262a45cc` | 2026-09-29T13:48:00Z |
| 6 | `ac040-06-golden-comparison` | 1, 0, dev | 5 | 2026-09-29T01:52:28Z | 36,195, `0b8cda3488141932d45205c9285620ac1545b78c93a6a5a322f218890a6c2e73` | 2026-09-29T13:48:00Z |
| 7 | `ac040-07-gate-ingress-offline` | 1, 0, dev | 1 | 2026-09-29T01:53:21Z | 19,946, `fea547063e4b5f2476736e0b0e1f9f35bb6b2a1ad51cab97de4db6c4e3b2758e` | 2026-09-29T13:48:00Z |
| 8 | `ac040-04-09-compat-cli-offline` | 1, 0, dev | 1 | 2026-09-29T01:54:22Z | 14,003, `2c69c50a0520ab0f5b2a5e7d7ed94fa745ff10120bade979f127fec6a682ac87` | 2026-09-29T13:48:00Z |
| 9 | `ac040-09-reader-http-in-process` | 1, 0, dev | 1 | 2026-09-29T01:55:14Z | 12,737, `6e53c15e3e0b496c62457887ccc39b9629c1305dfcd830bc9b6964e315452854` | 2026-09-29T13:48:00Z |
| 10 | `sec-reader-http-live` | 1, 0, dev | 3 | 2026-09-29T02:00:29Z | 73,940, `97e37e38b75d793bef7b57d47bb024070bc7366df718edb1303d0c378022d960` | 2026-09-29T13:48:00Z |
| 11 | `open-rails-showcompat-vendor` | 0, 1, dev | 6 | 2026-09-29T05:53:32Z | 64,998, `1e4341e27e1ce47fe172546581ac4737e2dcb9745f82bac42f0001ac6f5f4674` | 2026-09-29T13:48:00Z |
| 12 | `qa-closeout-deliverables` | 1, 0, dev | 16 | 2026-09-29T13:50:25Z | 64,249, `df03f7b6561d6182cdc59d095c8dc140ba8e3a048f5c31ee9842c7d3eaab35ff` | 2026-09-29T13:50:37Z |

Further bindings:
- The manifest `audit/qa/hde-epic040/qa_step_logs_manifest.json` is 1,997 bytes, SHA-256 `2bb4764f46bd5b362504f53f2894e9ed28b8f40e857d062cf663e1b4af2f1dfc`, path proof produced 2026-09-29T13:50:37Z.
- Each doc-delta surface, `audit/docdeltas/hde-epic040_doc_deltas.md` and `audit/qa/hde-epic040/00_meta/doc_deltas.md`, is 3,585 bytes, SHA-256 `f440538c9bc8e7f3dc6d008bb061175c3d12a20a10cb3f2450b8c6316d099ab5`, path proof produced 2026-09-29T13:48:00Z.
- The 14 supplementary files and their digests are listed in review v1.0 §7 (checks 6 and 10), review T11 §3 (check 11) and review T12 §4.2 K4.

## 7. Acceptance criteria AC040-01 to AC040-09

### 7.1 Conclusions

Proof classes follow Plan §10.1 and Glow QA Guide §3.3. "Local/offline" means under the closed posture with no vendor. It proves no live vendor, deployed-service or live-database behavior. The exact-head CI runs are those of Plan §10.2, each recorded in the named HDE Build Notes addendum:
- PR01 amthorn78/glow-hdengine-v2#403, run 34393325625 (2.6);
- PR02 amthorn78/glow-hdengine-v2#404, run 34784828890, attempt 2 (2.11);
- PR03 amthorn78/glow-hdengine-v2#405, run 34841280306 (2.13);
- PR04 amthorn78/glow-hdengine-v2#467, run 35777936856 (2.19);
- PR05 amthorn78/glow-hdengine-v2#492, run 36098781587 (2.20);
- PR06 amthorn78/glow-hdengine-v2#501, run 36210650937 (2.22);
- PR06a amthorn78/glow-hdengine-v2#508, run 36222478818 (2.24);
- PR06b amthorn78/glow-hdengine-v2#513, run 36257377433 (2.26);
- OPS01, accepted external release verification (2.27).

Each of those runs is change-aware: it supports what its lanes executed at that head, not a full-suite run of the final tree. PR07 (amthorn78/glow-hdengine-v2#518, run 36272965542) changed documentation only and supports no criterion.

| Criterion | Conclusion | QA run evidence and proof class | Exact-head CI and PR evidence | Limits |
| --- | --- | --- | --- | --- |
| AC040-01 Complete scope and ownership | **Supported** | Documentary, as Plan §2 defines it. All 13 requirements are mapped to units in Implementation Plan v2.1 §8. The six selected units and 29 excluded ones are in Plan v2.1 §2. All nine PR units are `ACCEPT` and merged; OPS01 is accepted and DOC-20 is `COMPLETE` (§17.1). Every scope change went through its native route and is recorded in HDE Build Notes (§17.2). Register C040-01 to C040-10 carries an actual decision for every entry and a named drainage owner where drainage is pending (§19). The coverage accounting of check 12 (K5) and §4 account for the whole approved QA assignment | Lineage records; Implementation Plan v2.1 §8 | Canon drainage of C040-05 to C040-10 is pending; the criterion itself says "Physical Canon drainage remains a separate later act". The criterion names "actual Thoth approval or change" for Plan-carried ADR proposals. Thoth decided C040-01 to C040-04, the conflicts known at Specification time. Each later conflict was decided by its native owner, recorded in the register: Isis-49 or Isis-50 for Implementation Plan conflicts (C040-05, C040-06); the Product Owner for C040-07 and C040-10; the PR06b rescope decision recorded in HDE Build Notes 2.25 for C040-08; Isis at QA-70 for C040-09. No conflict was resolved silently |
| AC040-02 Corrected catalog and compatibility | **Supported** | Check 4, local/offline: group A `304 passed` covers the registry catalog contract, the Magic10 contracts, the manifest schema, typed bundles, alias policy, fail-closed unknown identifiers, registry-report determinism and indexing, arrays as sets, category order and threshold rounding. K1 proves the 36-row structure, ascending unique Gate pairs and no nulls. Check 3 re-validates the PR01 governed catalog evidence, including the two Mirror records tagged HDE-EPIC040 (`catalog.catalog_schema_validation`, `catalog.domain_closure_report`) | PR01, PR02 | FE/BE bundle compatibility is proven by the repository's bundle and registry tests and the PR01 evidence. No external consumer was exercised |
| AC040-03 Adopted default and closed schemas | **Supported** | Check 4, local/offline: K2 proves the adopted configuration's structure (20 signals, the three profiles, 10 category weights, both Balance operations), and group A exercises schema and loader contracts. Check 11, vendor-backed: a live result carries `config_id` `m10-channel-state-v1.0.0` with 20 signals and 10 categories | PR01, PR03, PR04 | K2 is structural. Caps closure, source hashes and result-schema validation rest on the group tests and the PR evidence |
| AC040-04 Immutable fail-closed consumption | **Supported** | Check 5, local/offline: group B `371 passed` covers production admission, execution coherence, Engine Core purity, determinism and AB/BA, symmetry identity and runtime identity. Check 8, local/offline: group E `144 passed` covers eligibility, the no-user boundary and CLI source and error parity. Check 1: the admission probe admitted the complete release. Check 9, in-process: group F passed, and its route tests include admission refusal as a 503 `ERR_M10_MANIFEST_MISMATCH` (Plan check 9). Check 11, vendor-backed: birth-only inputs produce a release-bound result through the admitted bundle | PR02, PR03, PR04 | The refusal matrix and deep immutability are proven by tests, not by a live refusal |
| AC040-05 Configuration and source identity | **Supported** | Check 5: `--check-manifest-only` exit 0 over the 45 members; manifest SHA-256 `52be4558…4afe96`; the OPS01 ledger 7 of 7; the attestation binding K1 and K2. Check 1: `release_id` equals the manifest SHA-256. Check 10: probe S-01 `/internal/version` reports the same `release_id`. Check 11: the vendor-backed results carry the same `release_id` | PR02, PR03, PR06; OPS01 (attestation `PR06R_B_FINAL_PASS`; adverse checks A-1 to A-7 refused, receipt v1.2) | The OPS01 attestation is corroboration; QA did not rebuild it (Plan §2). It binds source commit `6f53d828`. `6e4b3a1` is the candidate of the supplemental A-5 to A-7 run, and the release members are unchanged since `6f53d828` (QA50-F11, DD-06). Frozen historical captures are not current identity (AGENTS.md) |
| AC040-06 Exact read-only comparison | **Supported** | Check 6, local/offline: 8 of 8 goldens `match` at the repository root; two runs byte-identical; a deliberate one-leaf change reported as a mismatch naming only `M10-G001`; tree digest unchanged before and after; group C `153 passed`; K1 to K3. AB/BA identity: groups B and E, and the vendor-backed AB/BA byte identity of check 11 | PR03, PR04, PR05, PR06 | Comparison was run at the repository root only; no other candidate root was compared |
| AC040-07 Gate ingress and current-row readiness | **Supported for the offline part. The live part is not supported: blocked by environment and deferred (§7.2)** | Check 7, local/offline: the readiness command's typed refusals through its real entrypoint, each exit 5 with empty stdout, so an unavailable dataset is never reported ready. Group D `191 passed` covers the Gate normalization and rejection corpus, projection ingress, compat chart resolution and the readiness tool, including its open-rails refusal | PR02, PR04, PR05 | The Specification's own evidence rule applies: "Synthetic fixtures prove only fixture behavior; unavailable live facts remain unavailable." No live current-row observation exists, and none is claimed |
| AC040-08 Integrated selected proof and governed artifacts | **Supported** for the owner-generated evidence of the change | Check 3, local/offline: nine read-only validators exit 0 (evidence-index updater `--check`, orientation `--check`, evidence paths, Mirror schema, Index hash, canonical JSON gate `--check-only`, LF endings, environment pins, configuration artifacts `--check`); group G `587 passed`; governed-graph digest unchanged. At the tested source the Human Evidence Index and the Machine Mirror hold 606 records each. Check 12: the governed graph passes its checks with the QA files present, and the QA manifest, primary logs, supplementary files and path proofs are coherent (K1 to K5) | Every PR above; PR06 (convergence); OPS01 | The QA evidence of this run is not registered in the Index or the Mirror (QA50-F01). The QA manifest is not ledger-bound (Glow QA Guide §4.4.3), and no ledger-bound claim is made |
| AC040-09 Boundary and decision integrity | **Supported for the closed-rails part and the vendor-backed Reader v1 dump. The live success path is not supported: blocked by environment and deferred (§7.2)** | Check 8, local/offline: compat and CLI boundary, canonical bytes, AB/BA. Check 9, in-process: group F `339 passed` covers Reader v1 and v2 success with injected rows, eligibility, refusal classes, every non-POST method including CONNECT and QUERY on all three factories, the emitter and schemas, transport, keys-only logging, and the production gating of the dev routes. Check 10, loopback HTTP under the closed posture: 22 probes, K1 to K3, with no secret, stack trace, Gate payload or internal diagnostic in any response. Check 11, vendor-backed: a numeric-free, bands-only Reader v1 dump. Decision integrity: every header carries empty token arrays, and no acceptance map, token matrix or replacement token system exists | PR01 to PR06, PR06a, PR06b; OPS01 | "No new surface" is read with the C040-07 overlay (§7.3): Reader v2 is an approved public surface. Its success bytes are proven in-process only; over loopback only its refusal paths were probed. Nothing was proven about the deployed service |

### 7.2 Parts not supported because they are blocked by environment and deferred

These are the two deferred requirements of Plan §2. Canon treats them as "blocked by environment, not as failed acceptance" (Glow QA Guide §3.3). The approved Plan excluded them from the run. Neither is a failure of this run.

| Requirement | Affected claim | Why no proof exists | Reactivation |
| --- | --- | --- | --- |
| Live, read-only Gate readiness against current rows | AC040-07, live part | Before the Glow App, no app-level user IDs and no persistent user-bound BodyGraphs exist that QA may rely on, and QA must not create them (Glow QA Guide §3.3). The QA Audit finding QA50-F05 records the same dependency on existing current rows | A future epic that defines user-bound QA surfaces once the App user model exists (Plan §2) |
| Live DB Reader success over live HTTP on live current rows | AC040-09, live success path | As above | As above |

Treatment for closure: the Specification scopes AC040-07's evidence with "unavailable live facts remain unavailable". Both deferrals were decided in the approved QA Plan with their references. Whether the change closes with them carried to a future epic is Isis's decision at CL-E-10. §15 records the recommendation.

### 7.3 Specification overlays that bear on the criteria

| Overlay | Effect on the criteria | Source |
| --- | --- | --- |
| C040-07: full Magic-10 exposure through Reader v2 | Supersedes, for this change, the Specification's line 265 exclusion of public ten-category expansion and the `surface_water` promise of no public category expansion. Reader v2 on `POST /api/reader?v=2` is an approved public surface. AC040-09's "no new surface" is read as no surface beyond Reader v2 | Product Owner decision of 2026-09-26, recorded in HDE Build Notes 2.23; delivered by PR06a (2.24) |
| C040-08: Reader v1 error envelope | Reader v1 errors use the four-key `error_v1` envelope. Check 10 asserts it for every JSON error response it probed | HDE Build Notes 2.25; delivered by PR06b (2.26) |

## 8. Product Owner Q-1 and Q-2

| Question and decision | Where it was planned | Outcome |
| --- | --- | --- |
| Q-1: a bounded security QA step on `POST /api/reader` and admission refusals. Decided "yes" (PO disposition v1.0) | Checks 9 and 10 | `PASS`. Check 10, over loopback HTTP against `adapter.factory:create_app()` built from the tested source under the closed posture, sent 22 probes. They covered version refusals (S-04 to S-06), malformed, BOM, extra-key, upper-case and empty bodies (S-07 to S-11), oversize bodies with and without `Content-Length` (S-12, S-13) and the eight non-POST methods (S-14 to S-21). Each returned its governed status and envelope with `no-store` and no `ETag`. No response carried a stack trace, database driver text, Gate payload or number in an error body. The 503 on S-02 and S-03 is the resolver-unavailable refusal with no database, as planned. Check 9 carried admission-refusal propagation, CONNECT and QUERY, and the production gating of the dev routes, in-process |
| Q-2: the PF05 §7.3.9 open-rails step applies, with no exemption. Decided "yes" | Check 11 | `PASS`. A live vendor call under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`) with synthetic birth tuples, the QA Audit L-51 defaults (QA50-S01). Two CLI invocations in all (AB, BA). It also meets HDE Build Notes 2.33 "PF10-OPENRAILS-001": a live vendor call, open rails and synthetic data only |

Q-2, vendor behavior:
- **Exercised.** Both birth tuples were resolved through HumanDesignAPI. The pair was evaluated through the admitted release. Canonical `magic10_compat_result.v1` output and a Reader v1 dump were emitted, byte-identical for AB and BA (review T11 K3).
- **Inferred, not exercised.** Both runs' captured stderr is empty, so the exact vendor resource path, the auth-header family and the adapter status are inferred from code, not observed.
- **Not exercised.** Rate-limit and `Retry-After` handling, typed vendor error mapping, malformed-response handling, the v1 legacy guard, mapped-cache persistence, Reader v2 and any deployed service.

As 2.33 states, "A passing open-rails test proves only what it exercises".

Authority for the delegated execution of check 11's vendor commands: HDE Build Notes 2.34 "PF10-VENDOR-001", register entry C040-10, and review T11 §4.3.

Q-1 is a behavior-level security check of the public surface. It is not a code security review of the implementation deltas of PR04, PR05, PR06 and PR06a, whose review coverage the QA-10 triage recorded as an evidence limit (RA-09). The Product Owner chose the QA step "rather than reopening accepted PRs" (triage §5), and that recorded limit is unchanged.

## 9. Environments, tested source, evidence commits and later divergence

| Item | Fact |
| --- | --- |
| Venue of record (Run B) | A Product Owner-controlled Linux shell, `glow-devops-vps`. Checkout `/home/nathan/hde-epic040-qa`, virtual environment `/tmp/hde-epic040-qa-v1.2/venv`, Python 3.12.3, `umask` 0022. One checkout, one QA root, one manifest (Plan §7.1). The venue is not material to any claim ("Venue-specific claim: NOT CLAIMED", Plan front matter) |
| Run A venue (preserved, non-canonical) | GitHub Codespace, `/workspaces/hde-epic040-qa`, Python 3.12.14 (review v1.0 §4.1) |
| Rails | Closed posture (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, pins `LC_ALL=C LANG=C TZ=UTC`) for checks 1 to 10 and 12, with the secret-bearing and drift names unset on every command. Check 11 alone used the CLI-local vendor posture (`SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`), and the closed posture was restored when it ended. No check used a production posture, a database or a deployed service |
| Executors | Checks 1 to 10 (Run B): Claude Code local VS Code session `fd43ebfd-1614-44e1-8ee5-6d03da21b70a`, delegated by the Product Owner. Check 11: Claude Code local VS Code session `f0edea78-3120-4040-92a1-020776ba5a6f`, the QA/infra executor that recorded the check. The same session executed the vendor commands as the Product Owner's directed agent under HDE Build Notes 2.34 (result T11 D-01). Check 12: the QA/infra executor, Claude Code local VS Code session `0f9a38bb-0ae2-4bf0-be59-17703912e6f7`. Kronos executed no check |
| Tested source | `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`, 2026-09-28T01:10:02Z (amthorn78/glow-hdengine-v2#544). Compared with the readiness-audited state `39b9cdf`, it differs outside `docs/` only in CI and agent-process files: `.claude/` hooks and settings, `.github/workflows/ci.yml`, `AGENTS.md`, two `ci/checks/` scripts and the unit test of one of them. It also changes `tests/evidence/test_rails_ci_workflow_integration.py`, which adds two parametrize cases, one of the 70 surface files that group G ran. No path under `engine/`, `adapter/`, `catalog/`, `schemas/`, `tools/` or `scripts/` differs |
| Evidence commits (storage, not tested state) | `345148b` (checks 1 to 10), `380cf46` (check 11) and `787bb97` (check 12), each on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, each adding only QA evidence under `audit/`. The branch head on `origin` is `787bb97` |
| `main` at this invocation | `917909c`. The tested source is its ancestor. The 14 later commits change only `docs/ephemeral/` (32 files), HDE Build Notes (v13.4.2 to v13.4.8) and two prompt-ecosystem-management files (`modification-template.md` and its validator `modification_validate.py`). No file outside `docs/` changed, so no product, test, `tools/`, schema, catalog, CI or requirements file changed |
| Currentness assessment (Glow QA Guide §10.8) | The later commits change no implementation, input, dependency, configuration or test. They change governing canon only by adding addenda 2.32 to 2.36. 2.33 and 2.34 set rules that the run meets: check 11 is the required live vendor call, and its delegated execution is authorized. 2.32, 2.35 and 2.36 record the QA-110 decisions. No conclusion of this Report is affected, and no focused retest is needed |
| HDE Build Notes progression during the run | v13.4.2 (the Plan's pin) to v13.4.4 (2.32, 2.33), v13.4.5 (2.34), v13.4.6 (2.35) and v13.4.8 (2.36), all on `main` |

## 10. Defects, deviations, cleanup and limitations

### 10.1 Product defects

None was found by the run. Known limitations were observed as planned and are not failures:
- the HTML 404 of the production factory for unknown non-compat paths (probe S-26; O-P06a-22, HDE Build Notes 2.24);
- the three closed-rails skips in group E, which are not vendor coverage.

### 10.2 QA-process defects and deviations

Every deviation was dispositioned and accepted at QA-110. None changed an executed byte, proof target, rails posture, evidence identity or predicate. The RCA gives their causes, corrections and lessons:
- the duplicate executions (LR-01; D-12, D-13);
- the collection defects K-01 to K-07;
- the syntax-origin normalizations (T10 E-01, T11 E-01);
- the delegated vendor execution (T11 D-01, authorized by 2.34);
- the runner script (T12 D-03, O-01).

### 10.3 Cleanup

- Check 10: the local server stopped, and port 8000 was confirmed closed (`000`, exit 7).
- Check 11: the vendor keys were unset in its shell and confirmed `UNSET` (commands 27 and 28). Every later command ran under the closed prefix.
- Temporary files: the venv, the recording files and the comparator report before its copy stayed outside the repository and were not committed.
- Tracked files: the only ones check 12 left changed were the two doc-delta surfaces, modified by its designed append, with the 13 path proofs untracked until storage (command 21).
- Secrets: the secret-value scans of check 11 found zero occurrences. The review v1.0 secret-pattern scan of both runs found no hit.
- No database state was touched, so no database rollback exists.

### 10.4 Limitations

- Kronos executed no check. At this invocation Kronos re-verified the stored evidence digests, the Index and Mirror state and the divergence of `main`. It did not re-run tests.
- Hosted CI on the tested source itself: the tested source is the merge commit of amthorn78/glow-hdengine-v2#544, which changed three files under `docs/ephemeral/` only. The criteria rely on the per-unit exact-head CI of §7.1 and on the local run of this QA, not on a full-suite CI run at `0db3f0ef`.
- Test files outside the 70-file HDE-EPIC040 surface were not run. This includes `tests/reader_v1/test_cli_proof.py` (baseline failure O-P06a-03) and the recorded 57 failures and 13 errors among other out-of-lane files (Plan §2). They are baseline, not results of this change.
- No deployed service, live database or production posture was exercised. No live claim is made beyond check 11's vendor-backed CLI behavior.

## 11. Unresolved risks and items

| Item | Owner | Status and effect |
| --- | --- | --- |
| Deferred live Gate readiness against current rows (AC040-07 live part) | A future epic with the App user model (Plan §2, §14) | Open. Blocked by environment; not a failure |
| Deferred live DB Reader success over live HTTP (AC040-09 live success path) | As above | Open. Blocked by environment; not a failure |
| Index and Mirror registration of the HDE-EPIC040 QA evidence (QA50-F01) | Evidence owner, through the whole-change IA PR route (Plan §14) | Open. It blocks only a ledger-bound manifest claim, which nobody makes. It is mapped to PF09.3 HDE-SEPA005.5 "indexed evidence" (§14) |
| Evidence of record on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97`, not on `main`; no pull request exists | Product Owner (pull request and merge) | Open |
| Run A branch `qa/hde-epic040-qa100-plan-v1.2` at `e5b671c`: preserved and non-canonical. It must not be merged into `main` as the QA root (LR-01 item 6) | Product Owner | Standing |
| Run A's T03 outcome and T10 receipt (LR-01 item 7) | Product Owner (holds the Run A Codespace) | Open, non-gating. A non-`PASS` T03 outcome would reopen T03 for focused review |
| Code security review never covered the implementation deltas of PR04, PR05, PR06 and PR06a (RA-09) | Isis (retrospective); the Product Owner chose the QA step instead (Q-1) | Recorded evidence limit; unchanged by QA |
| Carried implementation items: O-12, O-P06a-22, O-P06a-03, O-P06a-23, O-P06b-17, O-P07-01 to O-P07-09 (OPS01 receipt v1.2 §5; DOC-20 §6 describes O-P07-01 to O-P07-04), O-OPS01-01, O-OPS01-02 | Their recorded owners (QA-10 triage §2; OPS01 receipt v1.2 §5) | Non-gating |
| Epic rails statement missing from Implementation Plan v2.1 (RCA v1.1 C6) | Whole-change IA | Carried, non-gating |
| Drainage of DD-01 to DD-13 and of C040-05 to C040-10 | Their named maintainers (§19; RCA) | Pending. Never a blocker for a step verdict (Plan §13) |
| `.env.example` lacks `GEO_API_KEY` (T11 D-08) | Implementation lane (a 2.34 deferred obligation) | Documentation drift |
| Which execution environments hold the vendor configuration (a 2.34 deferred obligation) | Product Owner | Open, non-gating |
| The governed placement of the QA RCA & Doc Delta summary (Change Process Guide §0.4.1.2: a close-report section or `audit/EPIC-040_QA_RCA.md`) | The authorized close-pack writer, when a close pack is authorized | Not produced. QA-120 writes only under `docs/ephemeral/`. Close-pack completion: no claim (§13) |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING; no such procedure at `917909c` |

## 12. Required-elements checklist

This checklist applies Glow QA Guide §9.2.15.6, the Plan Templates §9 compatible checklist and Change Process Guide §0.4.1.3.

| Element | Present or absent | Evidence pointer |
| --- | --- | --- |
| D0 discovery artifact and baseline rails posture | Present. It records the rails posture, determinism pins, captured environment presence, tool health and admission | `audit/qa/hde-epic040/checks/d0-discovery/primary.log` at `787bb97` (SHA-256 `f5b0f82c…5c1d`) |
| Step-0B doc-delta capture | Present, DD-01 to DD-13 | Both doc-delta surfaces at `787bb97` (SHA-256 `f440538c…9ab5`) |
| Functional runtime proof on changed runtime surfaces | Present, same run and same tested source, each at its proof class. Catalog, configuration, admission, core and identity: checks 1, 4 and 5 (local/offline). Golden comparison: check 6. Gate ingress and readiness tool: check 7. Compat and CLI: check 8 (local/offline) and check 11 (vendor-backed). Reader HTTP: check 9 (in-process) and check 10 (loopback HTTP). The two live surfaces that need user-bound rows are deferred (§7.2) | The primary logs of checks 1 and 4 to 11 |
| Governed current-state QA evidence under the canonical epic QA root | Present at `audit/qa/hde-epic040/`: one manifest, one primary log per check, path proofs. It is on the Run B branch, not on `main` | Manifest at `787bb97` (SHA-256 `2bb4764f…1dfc`) |
| Per-step manifest, header and path-proof trust proof | Present for all 12 checks | §6 |
| Evidence-package content validation | Not applicable. No uploaded package was used; the tracked evidence was read directly from `origin` | §6 |
| Final QA Report and separate RCA | Present | This file; `docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md` |
| QA RCA & Doc Delta summary | Present in the RCA (Change Process Guide §0.4.1.2 contents). Its governed close-pack placement is not produced (§11) | RCA |
| Coverage vs QA Plan accounting | Present | §4; check 12 command 22 |
| All-slice coherence proof | Present: the manifest, header statuses and exit codes of all 12 checks agree | Review T12 §4.2 K1 to K5; §6 |
| Moon Loop pre-remediation context | Not applicable; no Moon Loop occurred | §3.3 |
| Overall QA conclusion and closure recommendation to Isis | Present. Isis's terminal decision is separate | §1, §15 |
| Indexed evidence in the Human Evidence Index and the Machine Mirror | **Absent for the HDE-EPIC040 QA evidence** (QA50-F01). The implementation's governed evidence is indexed and coherent: 606 records each, including the two tagged HDE-EPIC040, validated by check 3 | §11; check 3 primary log |
| Execution-venue posture | `NOT CLAIMED`. The Plan's four venue fields were surfaced and applied in check 3; no claim depends on the venue | Plan v1.2 front matter; check 3 primary log |
| PF10 addendum as close authority | No PF10 addendum is the decisive close authority: closure is Isis's decision. The QA-110 records in HDE Build Notes 2.32, 2.35 and 2.36 carry direct evidence-pointer lines (commit identifiers, repository paths, SHA-256 values). They are not evidence-light | HDE Build Notes v13.4.8 |
| Compliance statement | The run complied with the approved Plan v1.2 under the accepted deviations of §4. No unapproved scope change, rails change or evidence substitution occurred | §4, §10.2 |

## 13. Completion states

These states are kept separate (Glow QA Guide §9.2.15.6, §10.8; Change Process Guide §0.4.1.2). This Report is limited to repo-supported completion.

| State | Status |
| --- | --- |
| Repo-supported completion of the QA run | Complete: 12 of 12 checks recorded `PASS` and accepted. No check is blocked or unrecorded. The two deferred requirements are recorded as deferred, not as passed |
| Implementation delivery | Complete, as recorded before QA: nine PR units `ACCEPT` and merged; OPS01 accepted; DOC-20 `COMPLETE` (readiness v1.0; §17.1) |
| Canon-drain completion | No claim. C040-05 to C040-10 and DD-01 to DD-13 are undrained |
| Formal close-pack completion | No claim. No `audit/EPIC-040_close_report.md`, `audit/EPIC-040_MANIFEST.json` or `audit/EPIC-040_QA_RCA.md` exists on `main` or on the evidence branch |
| Merge provenance of the QA evidence | Not merged. The evidence of record is on the Run B branch at `787bb97`, and no pull request exists |
| PF09 status | No claim. The recorded posture is unchanged: HDE-SEPA005 Partial; .1 and .2 Partial; .3 to .5 Not done. §14 gives the later-drain recommendation |
| Board state, Product Owner closeout action | No claim |
| Formal OPS action | OPS01 was completed and accepted separately (receipt v1.2). QA performed no Ops action |
| Closure | Not decided here. Isis decides at CL-E-10 |

## 14. Later-drain statement and PF09 accountability

This updates Plan §14 from the executed evidence, using the exact vocabulary of Glow QA Guide §10.7. It is a recommendation posture. It moves no status, edits no canon and closes nothing. HDE Build Notes states no PF09 status decision for these rows (2.36: "No PF09 task or subtask closure determination, status recommendation or status action is made"), so the determination rests on the evidence and on Glow QA Guide §9.2.15.7.

| Field | HDE-SEPA005.1 | HDE-SEPA005.2 | HDE-SEPA005.3 | HDE-SEPA005.4 | HDE-SEPA005.5 | HDE-SEPA005 (parent) |
| --- | --- | --- | --- | --- | --- | --- |
| Affected PF canon home | `PF09.3-Canon-HDE-Build-Checklist-Separation` | Same | Same | Same | Same | Same |
| Exact affected locator | Subtask HDE-SEPA005.1 status line; Phase Notes line 171 | HDE-SEPA005.2 status line; line 171 | HDE-SEPA005.3 status line; line 171 | HDE-SEPA005.4 status line; line 171 | HDE-SEPA005.5 status line; line 171 | Task HDE-SEPA005 status line; line 171 |
| Current canon posture | Partial | Partial | Not done | Not done | Not done | Partial |
| Supported later-drain action | `change to Done` | `change to Done` | `change to Done` | `change to Done` | `change to Partial` | `No status change recommended` |
| Drain readiness classification | `Supportable from repo evidence` | `Supportable from repo evidence` | `Supportable from repo evidence` | `Supportable from repo evidence` | `Supportable from repo evidence` | `Supportable from repo evidence` |
| Epic-close expectation | `at epic close` | `at epic close` | `at epic close` | `at epic close` | `at epic close` | `at epic close` |
| Evidence basis | PR01 accepted (2.6); catalog decision C040-06 (2.5); check 4 K1 and group A; check 3 | PR01 accepted (2.6); check 4 K2 and group A; check 11 result shape | PR02 (2.11), PR03 (2.13), PR04 (2.19), PR06 (2.22) accepted; checks 5, 7 and 8; check 9 admission refusal | PR02, PR03, PR05 (2.20) and PR06 accepted; OPS01 (2.27); checks 5 and 6 | Implemented and proven: the schema mutation matrix, Gate-ingress rejection, canonical-byte checks, catalog, caps and threshold closure, and the readiness command (checks 3, 4, 6, 7 and every pytest group). Not complete: the QA evidence Index and Mirror registration (QA50-F01) and the deferred live current-row readiness observation, both mapped to this subtask by Plan §14 | .1 to .4 supportable as Done; .5 Partial. Reader v2, security and vendor proof (checks 9 to 11) map to the parent with the PF09 gap Plan §14 notes |

Notes:

- Every basis cites the evidence of record on the Run B branch at `787bb97`. It is in the repository but not on `main`. Its landing is the Product Owner's.
- **HDE-SEPA005.5 path to Done.** `change to Done` becomes supportable once QA50-F01 lands through the evidence owner's PR route and the deferred live readiness observation is re-homed by the PF09 owner, for example to a future-epic row. Plan §14 maps that observation here and states "No PF09 status claim".
- **Alternative reading of .5.** A PF09 owner might treat QA-evidence indexing and the live observation as outside the subtask's implementation text ("Implement … read-only current-row Gate-readiness command, and indexed evidence"). Under that reading .5 is complete in substance. The determination belongs to the separately authorized PF09 maintenance route (CL-E-20), not to QA-120. It is recorded here as an Unknown.
- The parent stays Partial while .5 is Partial.

Task-like items and their single accountabilities:

| Item | Accountability |
| --- | --- |
| QA50-F01 | PF09.3 HDE-SEPA005.5, as above |
| DD-04, `--allow-prod-vendor` gap (QA50-B01) | PF09 gap; PF05 and CLI owners through change control; outside HDE-EPIC040 |
| The two deferred requirements | Plan §14, unchanged: live readiness under HDE-SEPA005.5; live Reader success as a PF09 gap noted at the parent |

## 15. Readiness and closeout recommendation for CL-E-10

This is a closure-oriented recommendation. It is distinct from Isis's `CLOSE` or `DO_NOT_CLOSE` decision and from any close-report SATISFIED decision (Change Process Guide §0.4.1.2).

**Recommendation.** The QA outcome supports `CLOSE`. The approved run is complete and `PASS`. Every criterion is supported for the scope this run decides. No acceptance-critical QA defect is open. All of the following are follow-ups for their owners, not QA blockers:
- **The two deferred requirements.** Recommended treatment: carry them to a future epic, as the approved Plan and Glow QA Guide §3.3 provide, through the CL-40 scan for missing PF09 rows and CRD candidates.
- **QA50-F01.** Recommended treatment: post-closure evidence-owner work. It gates only a ledger-bound manifest claim and PF09 HDE-SEPA005.5 Done. It gates no criterion.
- **Landing the QA evidence of record on `main`.** Recommended treatment: a Product Owner pull request of the Run B branch. The Run A branch must not be merged as the QA root.
- **The close pack and its QA RCA placement, canon drainage, and PF09 maintenance.** Post-closure administration under their own authorization (Glow QA Guide §3.1.3; `AGENTS.md` "Operating routes and authority": "Permanent documentation and build-checklist drainage are not closure prerequisites").

Unknowns, labelled:
- **Close-pack timing.** Whether Isis treats the Change Process Guide §0.4.1.3 Close Gate placement of the QA RCA summary (a close-report section or `audit/EPIC-040_QA_RCA.md`) as required before or after the closure decision: Unknown, Isis's decision. This RCA exists in `docs/ephemeral/`, where HDE Build Notes 2.29 stores change-process RCAs.
- **Merge timing.** Whether Isis requires the QA evidence on `main` before closure: Unknown, Isis's decision.
- **Run A's T03 outcome** (LR-01 item 7): Unknown and non-gating.

## 16. Closure receiver: the continuing Isis

| Fact | Source |
| --- | --- |
| The change class is `EPIC`. The Product Owner selected it on 2026-09-08 | Specification v1.1 §1 (`CHANGE_CLASS` `EPIC`) and §2 |
| The continuing Lead Developer is the Isis-50 session, execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq. It approved Implementation Plan v2.1, decided C040-06, PR04-F01 and the PR06a rescope, and produced the QA-10 readiness, Reality Audit, triage and Live QA Guide | Readiness v1.0 (`decision_owner`, provenance); HDE Build Notes 2.5, 2.15, 2.23 |
| The same session is labelled Isis-51 in the revocation record and the later QA-70 records. At the Product Owner's direction, Isis-52 (execution identity https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2) replaced it as QA Plan reviewer: "Isis-51 makes no further QA-70 decision on this Plan". Isis-52 is recorded as "QA Plan reviewer for HDE-EPIC040" and approved Plan v1.2 | Revocation v1.0 §3; QA-70 review v1.3 front matter (`replaced_reviewer`); review v1.4 |
| No record transfers the Lead Developer role or the terminal closure authority from the Isis-50 session | The records above; HDE Build Notes v13.4.8 search for the Isis session labels |

Resolution: CL-E-10's receiver, "Isis, continuing Lead Developer and terminal closure authority", is the Isis-50 session. The replacement by Isis-52 was scoped to QA-70 on the QA Plan. If the Product Owner intends Isis-52 to decide closure, that is a Product Owner selection, and the handoff's receiver line would change. This Report's content would not.

## 17. Change lineage for the closure receiver

All paths are under `docs/ephemeral/` unless stated.

### 17.1 Delivery and final acceptance

| Unit | Final acceptance record | Decision | Landed | HDE Build Notes |
| --- | --- | --- | --- | --- |
| PR01 | `HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md` | `ACCEPT` | amthorn78/glow-hdengine-v2#403, `3828d4b` | 2.6 |
| PR02 | `HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT` | amthorn78/glow-hdengine-v2#404, `5b2fb8d` | 2.11 |
| PR03 | `HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#405, `9cda1b4` | 2.13 |
| PR04 | `HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT` | amthorn78/glow-hdengine-v2#467, `cd6f9e6` | 2.19 |
| PR05 | `HDE-EPIC040-PR05-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#492, `4d7ab9d` | 2.20 |
| PR06 | `HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#501, `f7484d0` | 2.22 |
| PR06a | `HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#508, `d79cfc1` | 2.24 |
| PR06b | `HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#513, `8999bd0` (release 1.3.0, 45 members) | 2.26 |
| PR07 | `HDE-EPIC040-PR07-pr-work-unit-lineage-review-v1.0.md` | `ACCEPT`, `ACCEPTED_FINAL` | amthorn78/glow-hdengine-v2#518, `edbd414` | Not in an addendum (Guide §11) |
| OPS01 | `HDE-EPIC040-OPS01-ops-execution-result-v1.4.md`; `HDE-EPIC040-OPS01-ops-task-receipt-v1.2.md` | `PASS`; `ACCEPT` | Evidence under `audit/ops/hde-epic040/ops01/`; the supplemental run landed in amthorn78/glow-hdengine-v2#527 | 2.27 |
| Documentation | `HDE-EPIC040-DOC-20-documentation-completion-v1.0.md` | `COMPLETE` | amthorn78/glow-hdengine-v2#531 | — |

### 17.2 Rescope, remediation and deferral decisions

| Record | Decision | HDE Build Notes |
| --- | --- | --- |
| `HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md` | C040-01 to C040-04 resolved in flight | 2.4 (2.2 holds the original decisions) |
| `HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md` | C040-05 `APPROVED`, alternative A (Isis-49) | 2.3 |
| `HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md` | C040-06 `APPROVED`, alternative A (Isis-50) | 2.5 |
| `HDE-EPIC040-PR02-rescope-review-v2.0.md` (preceded by v1.0, the rejected RS-20 result recorded in `HDE-EPIC040-alpha-rs20-escalation-planning-failure-rca-v1.0.md`); drafts `HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md` and `-v2.0.md` | PR02-F01 rescope `APPROVE` | 2.7 |
| `HDE-EPIC040-PR02-F02-rescope-review-v1.0.md`; `HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md` | `APPROVE` | 2.9 |
| `HDE-EPIC040-PR02-F03-rescope-review-v1.0.md`; `HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md` | `APPROVE` | 2.10 |
| `HDE-EPIC040-PR03-rescope-review-v1.0.md`; `HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` | PR03-R02 `APPROVE` | 2.12 |
| `HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` (v1.0 was `REVISION_REQUIRED`); `HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` | `APPROVE` (Isis-50) | 2.15 |
| `HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md` | Decided directly in the PR04 lineage, without an RS-20 decision (2.19) | 2.19 |
| `HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md`, `-F05-`, `-F07-` | Product Owner `DEFER` decisions, later delivered or bounded by PR06a (Plan v1.2 §2.2) | 2.16, 2.17, 2.18 |
| `HDE-EPIC040-PR06-F01-rescope-review-v1.0.md`; `HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md` | `APPROVE` | 2.21 |
| `HDE-EPIC040-PR06a-rescope-decision-v1.0.md`; `HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` | PR07-F01 `APPROVE`, option 1, add PR06a (Isis-50); C040-07 | 2.23 |
| `HDE-EPIC040-PR06b-rescope-decision-v1.0.md`; `HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` | `APPROVE`; C040-08 | 2.25 |

### 17.3 HDE Build Notes publication

**Actual publication.** Every approved decision in §17.2, each PR acceptance of §17.1 except PR07's, OPS01 (2.27) and the QA-10 triage (2.28, the informational Product Owner publication) is published in HDE Build Notes v13.4.8 on `main`. The three QA-110 reviews are published as 2.32, 2.35 and 2.36. Rules that bear on this change but belong to no single record: 2.29, 2.30, 2.31, 2.33 and 2.34.

**Pending.** Publication of this Report and the RCA, if the Product Owner chooses it, is pending and informational. QA-120 produces no addendum.

### 17.4 QA-stage lineage

| Stage | Records |
| --- | --- |
| QA-10 | Readiness v1.0; Reality Audit v1.0; Change Audit Triage v1.0; PO disposition v1.0 |
| QA-20 | Live QA Guide v1.0 |
| QA-50 | QA Audit v1.0; QA Plan v1.0 |
| QA-70 | Review v1.0 `APPROVE` of Plan v1.0, rejected by the Product Owner; RCA v1.0 and v1.1; review v1.1 `DENY`; review v1.2 `APPROVE` of Plan v1.1, revoked by the Product Owner (revocation v1.0; `GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md`); review v1.3 `DENY` (Isis-52); review v1.4 `APPROVE` of Plan v1.2 (Isis-52) |
| QA-80 | Plan v1.1 and v1.2; redline application reports v1.0 and v1.1 |
| QA-90 | Collections v1.0 (not carried forward), v1.1, v1.2 (never executed), v1.3, v1.4; `HDE-EPIC040-QA90-handoff-rca-v1.0.md` |
| QA-100 | Results v1.0 (superseded), v1.1, T11 v1.0, T12 v1.0 |
| QA-110 | Reviews v1.0, T11 v1.0, T12 v1.0 |
| Alpha | `HDE-EPIC040-alpha-state-stopped-failed-at-qa-v1.0.md` (resume point QA-70; the resumed flow is this run) |

### 17.5 Change-level RCAs and feedback records

- `HDE-EPIC040-alpha-rs20-escalation-planning-failure-rca-v1.0.md`: the PR02 RS-20 governance failure.
- `HDE-EPIC040-PR03-RS40-PF10-Resolution-RCA-v1.0.md`.
- `HDE-EPIC040-PR03-Session-Completion-and-CI-Control-RCA-v1.0.md` and `-v1.1.md`.
- `HDE-EPIC040-PR10-onward-RCA-v1.0.md`.
- `HDE-EPIC040-OPS01-RCA-v1.0.md`.
- `HDE-EPIC040-QA70-planning-failure-rca-v1.1.md`.
- `HDE-EPIC040-QA90-handoff-rca-v1.0.md`.
- `GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md`.
- The QA-stage RCA for this run: `HDE-EPIC040-QA120-qa-rca-v1.0.md`.

### 17.6 Carried unresolved findings

The QA-10 triage §2 to §4 hold the carried implementation and informational items. The OPS01 receipt v1.2 §5, DOC-20 §6 and this Report §11 add to them. None is a failure of an approved objective. The triage records "Objective failures: none evidenced", and this run found none.

## 18. Strategy Card (carried)

The approved Specification's Strategy Card is carried here unchanged from Specification v1.1 §4. It is the single strategy source. Its author-stage statements and named roles are source history. QA-120 creates no competing Card.

### `outcome_fire`

- **Outcome:** After this change, the selected production Magic10 mechanics configuration contract is implemented as one coherent, deterministic, release-bound capability spanning the corrected catalog, strict default configuration, fail-closed loading, identity/comparison and governed verification.
- **Success signal:** Exact-source evidence decides every §11 criterion against the actual candidate and all thirteen kickoff requirements, without using prior token claims or document presence as implementation proof.
- **Scope line:** HDE-SEPA005 and its five selected subtasks only; the other twenty-nine PF09.3 units remain Done/context. PF09.3 v1.1.4 is outside the selected baseline.

### `surface_water`

- **Surface statement:** One governed production mechanics configuration and its already-governed internal FE/BE projections; no second public compatibility surface.
- **Promise check:** Preserve the existing public Reader's bands-only, numeric-free covenant, non-scoring Product metadata and FE/BE bundle compatibility. No public category expansion, payload extension or alternate configuration selector is authorized.
- **Minimal contract phrase:** One trusted release configuration supplies validated mechanics inputs and governed result contracts; consumers and evidence tools use projections, not competing authorities.

### `boundary_air`

- **Contract name:** Production Magic10 mechanics configuration contract.
- **Evolution posture:** Implement the current adopted configuration contract rather than retune it. Preserve current bundle schema identities and consumer promises. Where legitimate dependency regeneration is needed, it must reflect the governed source change without silently changing the consumer contract. A genuinely incompatible migration, structural mechanics change or new public promise requires its actual owner before execution; no coexistence period or migration mechanism is invented here.
- **Data posture:** Only the governed catalog, categories, caps, thresholds, source identities, immutable configuration/release identity, result schemas and bounded comparison evidence are needed. Identity or request metadata, viewer preferences, clocks, prose and mutable configuration handles must not become intrinsic operands. Exact allowed fields and values remain in the owning Canon.

### `stewardship_earth`

- **Ownership:** Master Scrum owns the kickoff. Isis-49 is the continuing Specification author selected by the Product Owner. The continuing Thoth reviewer owns approval or denial; IA, QA, authorized environment operators and the governed PF09 owner retain their later duties.
- **Phase signals:** Entry is the complete KICKOFF_READY handoff and the PO's selected class, identity, source and disposition. This authoring output is complete but SPECIFICATION_PENDING; its immediate destination is independent Thoth review through Analyzer middleware. Approval alone permits mandatory IA-10 audit-then-plan preparation, not implementation.
- **Safety note:** Invalid, ambiguous, stale, hash-mismatched or release-incoherent configuration produces no successful mechanics result. Comparison and current-row readiness remain read-only. Rollback is one complete compatible prior release, never mixed code/configuration/schema identities. No rollback or deployment is executed or authorized by this document.

### Where the QA evidence bears on the Card (for Isis's assessment)

This subsection is evidence for Isis's assessment at CL-E-10, not a Card revision.
- **`outcome_fire`.** Exact-source evidence decided every §11 criterion at the tested source (§7), except the two parts blocked by environment (§7.2).
- **`surface_water`.** The public Reader stays bands-only and numeric-free (checks 9 to 11). "No public category expansion" is superseded for Reader v2 by C040-07 (§7.3).
- **`boundary_air`.** Admission accepts only the complete pinned release (checks 1 and 5). Comparison is read-only (check 6).
- **`stewardship_earth`.** Its safety note matches the typed refusals, the read-only comparison and the read-only readiness command (checks 5 to 7). No deployment or rollback was executed.

## 19. CANON_CONFLICT_REGISTER (carried)

This is the change's one register. It is carried from review T12 §7, which carried collection v1.4 §6 and review T11 §7. The only change is to C040-10's full history, which now also notes that addendum 2.36 carries the entry. No entry is added and no decision is changed. QA-120 found no new conflict. It considered three possible tensions:
- **The QA RCA location.** Change Process Guide §0.4.1.2 places the RCA summary in the close report or at `audit/EPIC-<NNN>_QA_RCA.md`. HDE Build Notes 2.29 stores change-process RCAs in `docs/ephemeral/` and leaves governed evidence homes unchanged. The two apply to different artifacts, so there is no conflict.
- **The Plan Templates §9 verdict vocabulary.** It is resolved by Glow QA Guide §10.7, which uses that template for compatible structure only.
- **Glow QA Guide §10.8's Google Drive passage.** It is already superseded by 2.29 (DD-03).

QA-120 makes no register decision. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 to v13.4.8 keep for 2.2 to 2.28. A proposal here is not approval.

| ID | Classification | Sources and clauses | Decision and status | Reviewer, artifact, time | Interim treatment | Drainage target and owner | Full history |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION | Pinned source/scope predicate | APPROVED exactly as proposed | Thoth-17, Specification v1.0 (represented by approved v1.1), 2026-09-08T13:23:24Z | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 v13.3.9 §2.2, §2.4 |
| C040-02 | CANON_RECONCILIATION | PF12 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-03 | CANON_RECONCILIATION | PF14 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-04 | CANON_RECONCILIATION | PF19 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-05 | CANON_RECONCILIATION | PF14 §6.7 superseded precomputed-score test instructions | APPROVED, alternative A | Isis-49, Plan v1.0 review, 2026-09-09T03:57:16Z | PF10 §2.3 governs | PF14 §6.7; PF14 maintainer; pending, non-gating | Plan v2.1 §11.2; PF10 §2.3 |
| C040-06 | NEW_CANON | 36-row Channel taxonomy and 16-case existing-state conformance | APPROVED, alternative A | Isis-50, Implementation Plan Review v2.0, 2026-09-09T11:48:08Z | PF10 §2.5 governs | PF12 §2.1, PF01 §§6.1–6.2; their maintainers; pending | Plan v2.1 §11.3; `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`; PF10 §2.5 |
| C040-07 | NEW_CANON | Full Magic-10 exposure via Reader v2 versus Specification line 265 and PF01, PF04, PF05, PF12 statements | PO decision 2026-09-26; delivered by PR06a | Product Owner; PF10 §2.23 | PF10 §2.23 governs; QA tests `?v=2` | PF01, PF04, PF05, PF12, with PF14 and PF29 consequences; their maintainers; pending | PF10 §2.23, §2.24 |
| C040-08 | CANON_RECONCILIATION | Reader v1 error envelope versus schema | Alternative A; delivered by PR06b | PF10 §2.25 decision record | PF10 §2.25 governs; QA asserts the four-key envelope | PF01 §2.3, PF04 §8.1.2; their maintainers; pending | PF10 §2.25, §2.26 |
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks"; QA-only harness scaffolding permitted) | `APPROVED_AS_CHANGED`. Proposed: alternative (a), PF19 and PF27 govern the execution rail and plan shape; alternative (b), forbid all git reads and embedded helpers, which loses the tested-source attribution PF19 §10.8 requires, was not adopted. Change: the approval covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; it does not cover newly written decisive evaluators, which Glow QA Guide §3.4.8 governs. Rationale: Glow Infrastructure §2.1 is names-only ("No procedures or policy here") and §2.8 routes the Live QA execution rail to the Glow QA Guide, so Glow QA Guide §3.4.9 (read-only repository observation for attribution, never a PASS predicate) and Plan Templates govern | Isis, continuing QA Plan reviewer (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq); reviewed QA Plan v1.0 and QA Audit v1.0; decision in `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md` §3, "Decisions carried to this review"; 2026-09-27 | Applied in this Plan: read-only git observations for attribution only, never a PASS gate; no script file is created; tracked harness APIs through `python -c`; no decisive evaluator written at run time (§12). Unresolved risk: a reader who applies PF07 §2.8 literally until its wording is drained | PF07 §2.8 wording; PF07 maintainer; documentation drainage only | Original proposal: QA Audit v1.0 §11 (`PROPOSED`, 2026-09-27). QA-70 review v1.0 §4: APPROVED as proposed; that review was rejected by the Product Owner on 2026-09-27 and is history only (RCA v1.1, C2). QA-70 review v1.1 §3: `APPROVED_AS_CHANGED` (current) |
| C040-10 | CANON_CONFLICT (vendor execution authority) | Barring an automated agent from the vendor call or requiring the Product Owner as executor: Glow QA Guide §3.3 and §3.5.7; HDE CLI/API Vendor Ref §3.7 and §7.1.8a; HDE Governance §3.4 ("Controlled vendor-backed no-user validation") and §11.1; HDE Mechanics Guide §1.1 and §17.9.4; Plan Templates "Artifact execution boundary" and "Proof-class and controlled vendor-smoke boundary"; HDE Build Checklist Fermentation, HDE-FERM008 and HDE-FERM008.2. Versus Product Owner-delegated execution: HDE Governance §3.4 ("HDAPI v2 open-rails vendor proof posture") and §9.1; Change Process Guide "Ops tasks"; Plan Templates "Execution authority (normative)", which are written for Ops tasks | Product Owner decision, 2026-09-29, recorded as HDE Build Notes addendum 2.34 PF10-VENDOR-001 (v13.4.5). A directed agent executes live vendor calls, including open-rails HumanDesignAPI calls in QA checks; "PO-only" names the authorizing principal; vendor configuration comes from environment variables. The listed bars are superseded for that scope | Product Owner; HDE Build Notes v13.4.5 addendum 2.34 (Timestamp 092926 06:04 UTC); direction given in the QA-100 session that executed T11 | PF10 2.34 governs; T11's delegated execution is authorized (QA-110 review T11 v1.0 §4.3) | The passages in 2.34's superseded-passage table; their maintainers; pending (2.34: "Drainage into the listed documents is unperformed") | Observed as a canon tension in collection v1.3 §7 on 2026-09-29, and not entered then because no decision of the change depended on it. It became decisive when the Product Owner directed the QA-100 session to execute T11's vendor commands (result D-01), and was decided the same day by addendum 2.34. Entered by the QA-110 review T11 v1.0; also recorded in HDE Build Notes v13.4.6 addendum 2.35, "Canon-conflict register" (Timestamp 092926 12:49 UTC) and carried by 2.36 |

Affected requirements:
- C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013).
- C040-10: the vendor-backed part of AC040-04 and AC040-09 (check 11) and PO Q-2.

## 20. Nonclaims

- `PASS` is the QA verdict for the approved run. It is not closure, acceptance, PF09 status movement, PF-Canon drainage, a close pack, deployment, release activation, token satisfaction, a ledger-bound manifest, or Index or Mirror publication. Kronos's reporting remains distinct from Isis's terminal acceptance and closure decision (Glow QA Guide §3.1.2).
- QA-120 executed no check. It made no vendor, database or network call to a product service, changed no approved artifact or evidence, repaired nothing and produced no PF10 addendum.
- Its read-only verification used `git` reads of `origin`.
- Merging the pull request that carries this record preserves the record and approves nothing (D21-C).

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-120-20260929-01
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-01 to AC040-09; HDE-SEPA005 and HDE-SEPA005.1 to HDE-SEPA005.5; QA Plan v1.2 checks 1 to 12
  - prompt: QA-120 — Create Final QA Report and RCA — 091426.1; Notion 3db4590a05eb81589d21e798cf38e8ba; page as of 2026-09-24T15:53:04.131Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-120
  - capture_time: 2026-09-29T16:47:49Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_REPORT v1.0 (`PASS`) and QA_RCA v1.0; routed to CL-E-10 in the continuing Isis session
  - task_and_attempt_mapping: T01 to T10 (collection v1.1; Run B at `345148b` per LR-01), T11 (collection v1.3, attempt 1, `380cf46`), T12 (collection v1.4, attempt 1, `787bb97`)
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `917909c`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact:
  - GCFPE-USE-HDE-EPIC040-QA-110-20260929-03 (review T12 v1.0)
  - GCFPE-USE-HDE-EPIC040-QA-100-20260929-03 (result T12 v1.0)
  - GCFPE-USE-HDE-EPIC040-QA-90-20260929-03 (collection v1.4)
  - GCFPE-USE-HDE-EPIC040-QA-110-20260929-02 (review T11 v1.0)
  - GCFPE-USE-HDE-EPIC040-QA-100-20260929-02 (result T11 v1.0)
  - GCFPE-USE-HDE-EPIC040-QA-90-20260929-02 (collection v1.3)
  - GCFPE-USE-HDE-EPIC040-QA-90-20260929-01 (collection v1.2)
  - GCFPE-USE-HDE-EPIC040-QA-110-20260929-01 (review v1.0)
  - GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (results v1.1)
  - GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (collection v1.1)
  - GCFPE-USE-HDE-EPIC040-QA-70-20260928-01 (review v1.4)
  - GCFPE-USE-HDE-EPIC040-QA-80-20260928-01 (Plan v1.2)
