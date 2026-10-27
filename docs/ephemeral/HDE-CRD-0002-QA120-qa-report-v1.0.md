---
artifact_type: QA_REPORT
artifact_id: HDE-CRD-0002-QA120-QA-REPORT
artifact_version: "1.0"
predecessor: none. This is the first final QA Report for HDE-CRD-0002; no QA_INTERIM_STATUS was issued for this run
verdict: PASS
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002
role_session_ref: the continuing Kronos session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV), author of QA Plan v1.0 to v1.3, collections v1.0 and v1.1, the ESC-10 report and QA-110 reviews v1.0 to v1.2
invocation_binding: CRD / HDE-CRD-0002 / QA-120 / complete run of approved QA Plan v1.3 (checks 1 to 21; checks 1 to 12, 14 and 15 executed under approved Plan v1.2, whose text for them v1.3 keeps)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-120 — Create Final QA Report and RCA — 100926.1 (https://app.notion.com/p/3f44590a05eb81a4a3fbc0fae65d153e; page state 2026-10-12T02:29:51.614Z; read in full in this session at QA-110 v1.2 and applied here)
ecosystem_release: GCFPE-20261009.1 (100926.1)
qa_rca: docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md (QA_RCA_ID HDE-CRD-0002-QA120-QA-RCA, v1.0)
specification: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED by Thoth, CF-C-30; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by Thoth, docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md; S01 removed; HDE Build Notes 2.20)
implementation_plan: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (INITIAL_APPROVE by Isis, docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (DELTA_APPROVE, docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md; HDE Build Notes 2.19)
approved_qa_plan: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; APPROVE by Isis, docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md, 2026-10-25T16:38:19Z), successor of approved docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (blob 66f6016cc75b; APPROVE, docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md, 2026-10-24T14:52:19Z)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE)
live_qa_guide: docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md
qa_readiness: docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.1.md (READY_FOR_QA), with docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.1.md and docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.1.md
evidence_of_record: audit/qa/hde-crd-0002/ on main at 48cdc25e5856773375fe703ecffc01a6f753cc34 (unchanged outside docs/ephemeral/ since bb931733, the squash of amthorn78/glow-hdengine-v2#744); manifest audit/qa/hde-crd-0002/qa_step_logs_manifest.json, 3,323 bytes, SHA-256 203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874, 21 checks, all PASS
tested_states: state (a) 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171 (tree af5293473238); state (b) da5735eb2c88d232d61babf27497548e24387050 (tree b5356a4ffec03a3dfb41036b38d2cc9411322137) for check 13's remediation verification, and main 463cbbefd36c8fdfa92470156586d35931245cb6 for check 21's evidence checkout; the deployed service at release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e for checks 16 to 20 (§3)
observed_revision: 48cdc25e5856773375fe703ecffc01a6f753cc34 (origin/main at this invocation; amthorn78/glow-hdengine-v2#745 merged)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; v13.7.8 read completely at ESC-10 and the v13.8 additions, addenda 2.27 and 2.28, in full at QA-80, both in this session; unchanged since)
closure_receiver: CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1, the continuing Isis (Isis-53, execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-120 (QA-120 is not an addendum producer)
created_at: 2026-10-26T00:45:00Z
---

# HDE-CRD-0002 — Final QA Report (QA-120), v1.0

## 1. Verdict

| Field | Value |
| --- | --- |
| `QA_REPORT_ID` | `HDE-CRD-0002-QA120-QA-REPORT`, v1.0 (this file) |
| `QA_RCA_ID` | `HDE-CRD-0002-QA120-QA-RCA`, v1.0: `docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md` |
| Verdict | **`PASS`** |
| Run state | Complete. Every check of approved QA Plan v1.3 was selected by the Product Owner, executed, published through the canonical writer and accepted at QA-110: checks 1 to 12, 14 and 15 at review v1.0; check 13's remediation verification at review v1.1; checks 16 to 21 at review v1.2. No check is unexecuted, blocked or waiting, and no task is open |
| Why `PASS` | Each verdict criterion of Plan v1.3 §11 holds (§1.1). The one behavior failure of the run (QA110-F01, check 13 attempt 1) was escalated, remedied by WU-REM-02 and verified at state (b) (§8) |
| Carried caveats | S06 is proven under the venue's distribution-patched setuptools as wired by a Moon Loop, not under the Plan's literal E-D construction (ruling R-1). Every other accepted deviation changes no proof target (§9) |

This verdict is QA's evidence for the closure owner. It is not acceptance or closure: Isis decides `CLOSE` or `DO_NOT_CLOSE` through CL-C-10 (Glow QA Guide §3.1.2).

### 1.1 Plan v1.3 §11 criteria

| Criterion (§11 "`verdict: PASS` only when") | Evidence | Holds |
| :- | :- | :- |
| All twenty-one checks are `PASS` in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` | Manifest on `main`: 21 entries, all `PASS`; each header status equals its manifest status; `validate_crd_check_family` lists 21 checks, all `PASS` (re-verified at `48cdc25`) | Yes |
| Each requirement S02 to S22 has a `PASS` check whose mapping names it (§10) | §5: every S-ID's mapped checks are `PASS`; the close writer's own parser finds all 22 requirement IDs mapped in Plan v1.3 | Yes |
| S01 reported as removed by Specification delta 01, with check 15's `PASS` as the removal evidence | §5 row S01; check 15 `PASS` (review v1.0) | Yes |
| The Live QA minimum holds: checks 17 to 19 and 20 `PASS` | §6 | Yes |
| Check 21 and §5.6's final receipt show the published family coherent | Check 21 `PASS` (review v1.2, R-4); final receipt in QA-100 results v1.3 §3, reproduced at QA-110 v1.2 §4 and again here (§7) | Yes |
| No `TOOLING_BLOCKED` check leaves its criterion unproven | No current status is `TOOLING_BLOCKED`. The two earlier `TOOLING_BLOCKED` executions (check 3 attempt 1; check 21's first run) were superseded by accepted reruns, and their bytes are preserved (§8) | Yes |

## 2. Change, scope and governing records

- **Change.** CRD HDE-CRD-0002. Twenty-two acceptance intents S01 to S22 in Specification v1.1-approved; delta 01 removed S01 and kept release `1.3.0`. The QA scope is S02 to S22 plus check 15 as S01's removal evidence (Plan §1).
- **Excluded from QA** (Plan §1): live Gate readiness and live Reader success; the Reader's unknown-person 404 (FND-004); any `showcompat --source vendor` step (IR-2; S19-R01); any `--upsert`, database write, deployment or configuration change; historical Epic acceptance-map viability (FND-038); older vendor generators in write mode (IR-10); a re-run of the full CI matrix.
- **Delivered work units** (each with an accepted PR-40 lineage review): WU-PR-01 to WU-PR-08, WU-DOC-01 (documentation completion v1.1), WU-REM-01 (FND-001) and WU-REM-02 (QA110-F01). WU-OPS-01 has an Ops task receipt (`ACCEPT`). §13 lists the paths.
- **QA lineage.**
  - QA-10: Reality Audit v1.1, Change Audit Triage v1.1 and readiness v1.1 (`READY_FOR_QA`).
  - QA-20: Live QA Guide v1.0. QA-50: QA Audit v1.0.
  - The Plan: v1.0 was denied (review v1.0), v1.1 was denied (review v1.1), v1.2 was approved (review v1.2). After the remedy, v1.2 was denied as it stands (review v1.3) and its successor v1.3 was approved (review v1.4). The route followed the Product Owner's direction D-1 to D-3 (CR-12).
  - Task collections v1.0 to v1.3, QA-100 results v1.0 to v1.3, and QA-110 reviews v1.0 to v1.2.
  - Escalation of check 13: ESC-10 report v1.0, ESC-30 proposal, ESC-40 remediation review (`APPROVE_AS_CHANGED`, HDE Build Notes 2.27), WU-REM-02.

## 3. Tested states (Plan v1.3 §2)

| State | Identity | Covers |
| :- | :- | :- |
| (a) | `2e03a2686af87ab0607c6cfb9afb4ad79bcdb171`, tree `af5293473238`; code outside `docs/ephemeral/` and `docs/pfcanon/` equal to `0b15328d`'s (check 1's guard) | Checks 1 to 12, 14 and 15 (accepted), and check 13 attempt 1 (`FAIL_BEHAVIOR`, QA110-F01) |
| (b), local | `da5735eb2c88d232d61babf27497548e24387050`, tree `b5356a4ffec03a3dfb41036b38d2cc9411322137`; no code difference from `22a3bc0` outside the two prefixes (rule A's reads, recorded in the primary) | Check 13 remediation verification `RV-1` |
| (b), evidence family | Evidence checkout from `main` `463cbbefd36c8fdfa92470156586d35931245cb6`, holding the published family. The throwaway test copy was restored to state (b) for one Markdown file (R-4) | Check 21 |
| Deployed | The production service `glow-hdengine-v2`, judged by `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (HDE Build Notes 2.19), read at check 16 (2026-10-25T23:18:11Z) and check 20's P1 | Checks 16 to 19 (E-P) and 20 (V-B, container `60f93a3e5923`) |

Release `1.3.0` and its `release_id` are unchanged across all states: none of WU-REM-02's three files is a release member (QA-70 review v1.3 §2 row 7, §3).

## 4. Run reconciliation (QA-120 Execute step 1)

Every check of Plan v1.3, with its task, result, review decision and evidence. Primary SHA-256 values are given as their first 16 hex digits; full values are in the path proofs and in QA-110 v1.2 §4.

| # | `check_id` | Req. | Task (collection) | Result (QA-100) | Review, decision | Attempts | Env | Rails | Status | Primary SHA-256 | Evidence commit, PR |
| -: | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| 1 | `qa-01-preflight` | Step-0 | T01 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `01df910157d7d96e` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 2 | `qa-02-ci-coverage` | S03, S04, S05 | T02 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `bc52ae603d33932c` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 3 | `qa-03-attestation-debian` | S06 | T03 (v1.0) | v1.0 | v1.0, `ACCEPT` (R-1) | 1 (Moon Loop reruns inside; R-2) | E-D | closed | `PASS` | `7dfc152a9f8e3845` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 4 | `qa-04-showcompat-help` | S07 | T04 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `3e8b5c5d74f654c3` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 5 | `qa-05-aux-preview-band` | S08 | T05 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `e06b99d39affdc48` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 6 | `qa-06-dev-harness-retired` | S09 | T06 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `0fe1f4cb69ff89b8` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 7 | `qa-07-dev-reader-gate` | S10 | T07 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `3da89797b92d6804` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 8 | `qa-08-release-evidence-tooling` | S11, S12, S13 | T08 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `f1421a7e6412cedf` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 9 | `qa-09-override-matrix` | S14 | T09 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `fea39bb3ead43325` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 10 | `qa-10-endpoint-catalog` | S15 | T10 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `34c7478089263446` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 11 | `qa-11-template-and-documents` | S16, S17, S18 | T11 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `21c193380cf4accd` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 12 | `qa-12-security-review` | S19 | T12 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `d7c986943c3f52a4` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 13 | `qa-13-prepush-check` | S20 | T13 (v1.0), then T13-RV1 (v1.1) | v1.0 (`FAIL_BEHAVIOR`), then v1.1 | v1.0 `ESCALATION_REQUIRED`, then v1.1 `ACCEPT` | 1 (two executions; rerun consumed, R-2), then `RV-1` (not attempt 2) | E-L | closed | `PASS` | `1944d2f1a44f057a` | attempt 1 `3d808047` (amthorn78/glow-hdengine-v2#726); `RV-1` `26e23c79` (amthorn78/glow-hdengine-v2#741) |
| 14 | `qa-14-close-pack-writer` | S21 | T14 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `d4d2f223c8b6e62f` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 15 | `qa-15-s01-removal` | S01 (removed) | T15 (v1.0) | v1.0 | v1.0, `ACCEPT` | 1 | E-L | closed | `PASS` | `f4233b2f574828f5` | `e97c3bba`, amthorn78/glow-hdengine-v2#726 |
| 16 | `qa-16-deployed-identity` | Step-0C | T16 (v1.2) | v1.2 | v1.2, `ACCEPT` (R-3) | 1 | E-P | Production | `PASS` | `daad275072310b5a` | `ee7b8d9c`, amthorn78/glow-hdengine-v2#744 |
| 17 | `qa-17-deployed-not-found` | S02 | T17 (v1.2) | v1.2 | v1.2, `ACCEPT` | 1 | E-P | Production | `PASS` | `27258d4a7b1d1969` | `7ede02ba`, amthorn78/glow-hdengine-v2#744 |
| 18 | `qa-18-deployed-dev-surfaces` | S10, S19 | T18 (v1.2) | v1.2 | v1.2, `ACCEPT` | 1 | E-P | Production | `PASS` | `63fe7da715fc16c6` | `7ede02ba`, amthorn78/glow-hdengine-v2#744 |
| 19 | `qa-19-deployed-reader-input` | S19 | T19 (v1.2) | v1.2 | v1.2, `ACCEPT` | 1 | E-P | Production | `PASS` | `7c4cc490ccf49338` | `7ede02ba`, amthorn78/glow-hdengine-v2#744 |
| 20 | `qa-20-live-vendor-override` | S14, S19 | T20 (v1.2) | v1.2 | v1.2, `ACCEPT` | 1 (one allowed invocation) | E-V, V-B | Production | `PASS` | `5e96be9bd0261727` | `c4c868ff`, amthorn78/glow-hdengine-v2#744 |
| 21 | `qa-21-evidence-admission` | S22 | T21 (v1.3) | v1.3 | v1.2, `ACCEPT` (R-4) | 1 (first run `TOOLING_BLOCKED`, Moon Loop rerun inside; rerun consumed) | evidence checkout and test copy | closed | `PASS` | `e5b7ca127fed0d22` | first run `d639772d`, republished `7974e2c7`, amthorn78/glow-hdengine-v2#744 |

Squash commits: amthorn78/glow-hdengine-v2#726 `faa2246`, amthorn78/glow-hdengine-v2#741 `86a7556`, amthorn78/glow-hdengine-v2#744 `bb931733`. "Closed" rails are `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`. "Production" is `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod`; publication of every check ran under closed rails.

**Selection union.** The Product Owner selected checks 1 to 15 (QA-90 v1.0), then check 13's re-verification ("create reverification instruction for check 13"), then checks 16 to 21 (SEL-110-1). SEL-110-1 was executed as 16 to 20 (PO-QA100-1), then 21 (PO-QA100-5). The union equals all 21 checks of Plan v1.3. Nothing is deferred.

## 5. Requirement coverage (Plan v1.3 §10)

| Req. | Checks (PASS needed) | Status | Proof class |
| :- | :- | :- | :- |
| S01 | 15 | Removed by Specification delta 01; check 15 `PASS` is the removal evidence | Removal as approved (Live QA Guide §8 G-1) |
| S02 | 17 | `PASS` | Deployed target |
| S03, S04, S05 | 2 | `PASS` | Local/offline, hosted CI cited |
| S06 | 3 | `PASS`, with R-1's caveat | Local/offline, Debian backend as wired |
| S07 | 4 | `PASS` | Operator CLI, local/offline |
| S08 | 5 | `PASS` | Operator CLI, local/offline |
| S09 | 6 | `PASS` | Local/offline |
| S10 | 7, 18 | `PASS`, `PASS` | Local matrix and deployed refusal |
| S11, S12, S13 | 8 | `PASS` | Local/offline |
| S14 | 9, 20 | `PASS`, `PASS` | Local matrix and the live vendor call |
| S15 | 10 | `PASS` | Local/offline |
| S16, S17, S18 | 11 | `PASS` | Mechanical document alignment |
| S19 | 12, 18, 19, 20 | all `PASS` | The record and its tests; F03 and F01 deployed; F05 and F06 live |
| S20 | 13 | `PASS` (`RV-1`, after QA110-F01 and WU-REM-02) | Local/offline, full-history E-L at state (b) |
| S21 | 14 | `PASS` | Local/offline |
| S22 | 21 | `PASS` | The real publication and validation |

## 6. Live QA minimum and check 20

- **Live QA minimum** (Plan §11): checks 17, 18 and 19 against the deployed service and check 20's live vendor call, all `PASS`.
- **Check 20.**
  - Venue V-B: the production service shell of `glow-hdengine-v2` (project `ample-illumination`, environment `production`), through Railway CLI 5.71.0 `railway ssh`, in container `60f93a3e5923` throughout.
  - Interpreter `/app/.venv/bin/python`. Actor `root` (IR-1).
  - Initiator: the Product Owner, who typed and ran V1 and V2. Attestation, verbatim: "I, Nathan, the Product Owner, typed and ran V1 and V2 myself".
  - One allowed invocation. V1 refused with `PROVIDER_PROD_OVERRIDE_REQUIRED` and no outbound request.
  - V2 made one bounded request: route `recommended_v2_chart` and resource `charts`, adapter `mapped` (`ChartResult`), no raw vendor payload, `rows_written` 0, header posture redacted.
  - The sink holds three keys-only events, and the in-service secret scan returned `NO_HIT`.
  - V-A was not used.

## 7. Evidence of record and integrity

- **Re-verified at this invocation** on `main` `48cdc25` (full-history scratch clone; closed rails; status empty afterwards):
  - `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh` and `check_lf_endings.py` each exit 0;
  - `validate_crd_check_family` returns 21 checks, all `PASS`;
  - the manifest SHA-256 is `203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874`;
  - nothing outside `docs/ephemeral/` changed since `bb931733`.
- **Earlier verifications:**
  - The Index and Mirror (22 of 22 keys), every primary's path proof (size and SHA-256), and each header status against the manifest: QA-110 v1.2 §4, at `bb931733`.
  - The decisive predicates were re-read from captured output in QA-110 v1.0 §5 (checks 1 to 15), v1.1 §3 (check 13 `RV-1`) and v1.2 §3 (checks 16 to 21).
- **Failure history preserved:**
  - check 13 attempt 1 is blob `4c6d826ae0ac` at `faa2246`;
  - check 21's first run is blob `3e1562ea1175` at `d639772d`;
  - check 3 attempt 1 was never committed to the QA root; its bytes are preserved at `docs/ephemeral/HDE-CRD-0002-QA100-t03-attempt1-primary-v1.0.log` (12,380 bytes, SHA-256 `f67c2274cb9288f464616b5db503846b36dacd6f245b03521af9b2e4872961e3`).
- **Indexing gaps:** none.
- **Hosted CI on the evidence pull requests.** This is measure (1) of the FND-001 remedy: the first real HDE-CRD-0002 publications pass the evidence lane. It is not a check predicate.

  | PR or push | Head | Run | Lanes | Conclusion |
  | :- | :- | :- | :- | :- |
  | amthorn78/glow-hdengine-v2#726 | `b0830c15` | 40149195209 | evidence, release | success, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
  | `main` push | `faa2246` | 40149378863 | as classified | success |
  | amthorn78/glow-hdengine-v2#741 | `a905f246` | 40218259658 | evidence, release | success |
  | `main` push | `86a7556` | 40218785186 | as classified | success |
  | amthorn78/glow-hdengine-v2#744 | `faea2922` | 40247385667 (job 121331857542) | evidence, release | success, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
  | `main` push | `bb931733` | 40247678102 (job 121332615249) | evidence, release | success |

  Intermediate amthorn78/glow-hdengine-v2#744 runs were cancelled as superseded (40245549332, 40246659316, 40247266229), and 40245581199 on `2861558b` passed. FND-024 (PR35-C1) and IR-7 did not occur on any of these runs. Measure (2) of the remedy belongs to the close-pack pull request.

## 8. Defects found by QA

| ID | Check | Class | Disposition |
| :- | :- | :- | :- |
| QA110-F01 | 13, attempt 1 | `FAIL_BEHAVIOR` (product: `tools/ci/prepush_check.py` exited 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION`, with every report passing) | Escalated (ESC-10). The cause was established at ESC-30 and ESC-40 (HDE Build Notes 2.27: `--shared` copies re-timed the source pack). Remedied by WU-REM-02 (amthorn78/glow-hdengine-v2#734, squash `22a3bc0`; PR-40 `ACCEPT`). Verified by check 13 `RV-1` `PASS` under git 2.53.0, the venue that failed, which meets HDE Build Notes 2.27 V-6. Closed for QA |
| O-1 | 13, attempt 1 | Independent repository-test portability defect, outside S20: two OPS03 tests fail with `EXDEV` when `TMPDIR` and `/tmp` are on different filesystems | Not a CRD-0002 requirement. Avoided in later runs by NZ-08. Open with Thoth, and the Product Owner if independent (HDE Build Notes 2.28) |

No other behavior defect was found. The RCA gives causes and contributing conditions.

## 9. Attempts, reruns, deviations and normalizations

**QA-110 rulings:**

| Ruling | Subject | Decision |
| :- | :- | :- |
| R-1 (v1.0) | Check 3's Moon Loop: E-D wired from uv CPython 3.13.17 with the system `dist-packages` | PASS-only deviation. Caveat: S06 is proven under Ubuntu 26.04's patched setuptools 78.1.1 as wired |
| R-2 (v1.0) | In-session reruns of checks 3 and 13 at the Product Owner's direction | A process deviation; each check's one ordinary rerun is consumed. Check 21's in-session rerun took the same accounting (v1.2 R-4) |
| v1.1 | Check 13's next execution | The remediation verification `RV-1`: not attempt 2 and not a reset (Plan §9) |
| R-3 (v1.2) | QA-100 gap G-1: check 16's header `timestamp_utc` 23:40:00Z was typed during assembly. The requests ran at 23:18:11Z to 23:18:12Z, and the primary was written at 23:23:10Z | Kept as a recorded assembly deviation; not republished. The true times are those given here |
| R-4 (v1.2) | Check 21's first run was `TOOLING_BLOCKED`: Plan v1.3's guard excludes only two of the eight CI-exempt prefixes, and amthorn78/glow-hdengine-v2#737 changed a third. The Moon Loop restored one Markdown file in the throwaway copy only | PASS-only deviation. An independent run on unmodified `main` gave the same counts (31, 1, 81, 1 passed) |
| R-5 (v1.2) | Incident I-1 (§10) | A session incident, not an evidence defect |

**Normalizations recorded by the executors** (each keeps the objective, target, rails, evidence identity and predicates):
- NZ-01 to NZ-07 (collection v1.0);
- NZ-01, NZ-06 and NZ-08 (v1.1);
- NZ-01, NZ-06 and NZ-20 to NZ-25 (v1.2);
- NZ-30 and NZ-31 (v1.3);
- NZ-32 (an execution-time reading of check 21's "exactly the twenty IDs", accepted at v1.2 R-4).

**Product Owner decisions and directions in the run:**
- PO-1 and PO-3: the Moon Loops of checks 3 and 13.
- PO-2: do not pin tool versions (`PENDING_DRAINAGE`).
- PO-4: the evidence-persistence grant.
- PO-5: drain the evidence-persistence rule to Glow QA Guide §3.4.3 (`PENDING_DRAINAGE`).
- D-1 to D-3: the QA-70, QA-80 and QA-90 route for check 13 (CR-12).
- PO-RV1-1: the evidence-only commit grant for `RV-1`.
- PO-QA100-1 to PO-QA100-6: the selection order, check 20 at V-B with the Product Owner as initiator, the evidence-only grant, executing collection v1.2 before its pull request merged, no rotation after I-1, and check 21's Moon Loop.
- SEL-110-1: the selection of checks 16 to 21.

**Executors:**
- Checks 1 to 15 and `RV-1`: two local Claude Code CLI sessions on the Product Owner's workstation, chosen by the Product Owner (not Kronos).
- Checks 16 to 21: a separate local Kronos session, by the Product Owner's arrangement. That session also authored collections v1.2 and v1.3.
- Every review ran in this Kronos session, separate from the executing sessions.

## 10. Unresolved risks, limitations and observations

| Item | Owner | State |
| :- | :- | :- |
| R-1 caveat: S06 under the literal E-D construction or other distributions is unproven | Product Owner (PO-2 context) | Carried |
| O-1 (OPS03 `EXDEV`) | Thoth; Product Owner if independent | Open |
| I-1: secret values (workstation `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `DATABASE_URL`) printed into the executing session's transcript at about 2026-10-25T23:20Z. No repository file holds a value. Not rotated, by the Product Owner's decision (PO-QA100-4); a workstation guard hook was installed | Product Owner | Risk accepted; transcript handling open |
| D-1/LR6-O1 (whether S20 is removed); FND-028 (whether `replay` is removed); O-A (the owner test's `--shared` fixtures re-time the developer's checkout) | Product Owner | Unchanged |
| S19-R01 to R07 routed items (FND-029; FND-012) | Product Owner | Pending, non-gating |
| Live QA Guide §8 G-1: the close representation of S01, which the writer requires among requirement IDs (IR-11) | Close mutation set and Isis; Product Owner if a route beyond the writer is needed | Open; check 15 supplies the evidence |
| CR-9 (path proofs under the WU-OPS-01 root) | Isis, IA-30 boundary | `PROPOSED`; check 16 applied interim (a) |
| O-2 and O-5/O-12: path proofs carry a constant `produced_at_utc`, and republication keeps an earlier `mtime_utc`; the validators accept both | Kronos (record) | Observation; provenance only (`AGENTS.md` "Path-proof portability") |
| O-9: `build_commit` `9479d28` in the deployed identity is an older commit | Record only | Not judged (judged by `release_id`) |
| O-11: Plan v1.3's guards were too narrow (R-4) | Kronos (Plan author) | Lesson in the RCA; no Plan change needed |
| IR-3 observation: `GET //reader?v=1` answered `403` directly (no `308` seen without `-L`); `OPTIONS` on a dev path answered `200 text/html` | Product Owner (LR5-O1 doc-delta candidate) | Recorded, no predicate |
| Residual state on the workstation and the service host (§12) | Product Owner | Open |
| QA70/QA-80 route gap for an approved-Plan change (MB-021) | GCFPE-MGMT-10 maintenance owner | Recorded on the GCFPE Modification Backlog |

**Limitations.**
- QA judged the deployed candidate by `release_id` alone; it performed no deployment.
- Check 20 covers one bounded override call, not broad HumanDesignAPI v2 conformance.
- The full CI matrix was cited, not replayed by QA, apart from check 13's local `replay`.
- `TypeSafe` readings could not be taken in the executors' local venue (HTTP 403).

## 11. Dispositions required by Plan v1.3 §11

**Implementation risks (Live QA Guide §6):**

| Item | Disposition |
| :- | :- |
| IR-1 | The actor is `root`, an account. The initiator is proven by the Product Owner's attestation (check 20) |
| IR-2 | No `showcompat --source vendor` or conjunction vendor step ran. Check 20 used `bg:resolve` only. S19-R01 stays with the Product Owner |
| IR-3 | Recorded in check 18's observation rows; no predicate (§10) |
| IR-4, IR-5 | No claim made from the env guard or the after-request hook (check 18 nonclaims) |
| IR-6 | All vendor evidence lives in check 20's primary; no sidecar (Plan §5.1) |
| IR-7 | Not observed on any evidence pull request or `main` push (§7) |
| IR-8 | No QA selector included `test_hdapi_v2_contract_inventory.py`. The `RV-1` full-validation `replay` reported step 08 "4525 passed, 2 skipped" with no failure |
| IR-9 | Not an objective. Check 21's strict-viability selector (current acceptance inputs) passed |
| IR-10 | The older generators were never run |
| IR-11 | A close-stage design point; carried with the Live QA Guide §8 G-1 (§10) |

**Triage findings:**

| Item | Disposition |
| :- | :- |
| FND-004 | Check 17 exercised unknown non-compat paths and excluded the Reader's unknown-person 404, as its statement says. `PASS` |
| FND-007 | Check 3 re-ran the Debian-backend attestation build. `PASS` through R-1, with its caveat |
| FND-011 | The live call's initiator was the Product Owner, attested; the actor is recorded as an account (IR-1) |
| FND-024 | The PR35-C1 signature did not appear: check 13 step 3 passed 141, and no hosted run failed |
| FND-030 | Plan v1.3 has `### CHECK` headings and mapping lines that the writer parses (22 requirement IDs mapped). This report has `artifact_type: QA_REPORT`, `change_id: HDE-CRD-0002` and `verdict: PASS` in its front matter and is named as the writer expects |
| FND-031 | Check 16 consumed the six WU-OPS-01 files by reference with verified SHA-256 values (CR-9 interim (a)) |
| FND-032 | Check 16 re-read `/internal/version` live (`release_id` the candidate), and check 20's P1 matched it |
| FND-033 | Every validator ran with CI's full install (E-L and evidence-checkout venvs) |

**CR-11:** `APPROVED_AS_CHANGED`, alternative (a) (Isis, QA-70 review v1.0, 2026-10-24T03:57:24Z). Step-0B is carried in check 1's primary. Check 1 found no doc-delta surface and no BLOCKER (HDE Build Notes 2.28).

## 12. Cleanup and residual state

- **Removed by the executors:** throwaway E-L clones and venvs, scratch `XDG_STATE_HOME`, check 16 to 19 scratch directories, and the container's check 20 scratch.
- **Left in place, owner the Product Owner:**
  - on the workstation: `/tmp/hde-crd-0002-evidence` and `/tmp/hde-crd-0002-qa` (until this report is read), uv CPython 3.13.17, four leftover OPS03 test directories under `/tmp/hde-epic038-ops03/`, Railway CLI 5.71.0, the `glow-workstation` key, the trusted host key and the I-1 guard hook;
  - on the service host: the override sink with three events, until the container is replaced.

## 13. Evidence set for the closure receiver (CL-C-10)

- **Specification:** `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, its review `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`, delta `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` and its review `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`.
- **Implementation Plan:**
  - `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` with review `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md`;
  - delta `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md` with review `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md`;
  - Implementation Audit `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`.
- **Work-unit acceptance** (latest PR-40 lineage review each, all `ACCEPT`): `docs/ephemeral/HDE-CRD-0002-<unit>-pr-work-unit-lineage-review-<version>.md` for:
  - WU-PR-01 v2.0, WU-PR-02 v2.0, WU-PR-03 v1.0, WU-PR-04 v1.0, WU-PR-05 v1.0, WU-PR-06 v1.0, WU-PR-07 v1.0, WU-PR-08 v1.0;
  - WU-DOC-01 v3.0, WU-REM-01 v1.0, WU-REM-02 v1.0.
- **Ops and documentation:** `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md` (`ACCEPT`); `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.1.md` (`COMPLETE`).
- **QA:** readiness v1.1, Live QA Guide v1.0, Reality Audit v1.1, Change Audit Triage v1.1; this Report and the RCA.
- **Remediation and rescope lineage:**
  - FND-001: proposal v1.1, review v1.1 and addendum v1.1;
  - QA110-F01: ESC-10 report v1.0, proposal v1.0, review v1.0 and addendum v1.0; the direction v1.1 (CR-12);
  - rescope reviews of WU-PR-01, WU-PR-03 (two) and WU-PR-07.
- **Product Owner direction records:** `docs/ephemeral/HDE-CRD-0002-po-direction-tool-version-pinning-v1.0.md` (PO-2), `docs/ephemeral/HDE-CRD-0002-po-direction-qa-evidence-persistence-v1.0.md` (PO-4, PO-5) and `docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.1.md` (D-1 to D-3, CR-12).
- **Other decision records in the delivery lineage:**
  - Product Owner dispositions, each `docs/ephemeral/HDE-CRD-0002-<name>.md`: `WU-PR-01-po-disposition-cr-4-cr-5-v1.0` (CR-4, CR-5); `WU-PR-08-po-disposition-scope-v1.0` (the scope decision behind Specification delta 01); `WU-PR-07-po-disposition-business-case-v1.0`, `WU-OPS-01-po-disposition-business-case-v1.0` and `WU-DOC-01-po-disposition-business-case-v1.0`; `WU-DOC-01-po-disposition-doc20-correction-v1.0`;
  - `docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md`;
  - `docs/ephemeral/HDE-CRD-0002-WU-PR-06-postmortem-v1.1.md` (the work unit whose tool QA110-F01 concerned).
- **PF10 addendum artifacts produced for this change** (`artifact_type: PF10_BUILD_NOTES_ADDENDUM`), each `docs/ephemeral/HDE-CRD-0002-<name>.md`:
  - rescope (RS-20): `WU-PR-01-PF10-build-notes-addendum-v1.0`, `WU-PR-03-PF10-build-notes-addendum-v1.0`, `WU-PR-03-corrective-PF10-build-notes-addendum-v1.0`, `WU-PR-07-PF10-build-notes-addendum-v1.0`;
  - WU-PR-07 and policy records: `PF10-build-notes-addendum-adr-defers-v1.0`, `PF10-build-notes-addendum-aq1-adr-v1.0`, `PF10-build-notes-addendum-codex-security-review-deprecation-v1.0`, `PF10-build-notes-addendum-no-cost-ceiling-v1.0`, `PF10-build-notes-addendum-p1-findings-v1.0`;
  - deltas: `specification-delta-01-PF10-build-notes-addendum-v1.0` (CF-C-30), `implementation-plan-delta-01-PF10-build-notes-addendum-v1.0` (IA-30);
  - remediation (ESC-40): `remediation-FND-001-PF10-build-notes-addendum-v1.0`, `remediation-FND-001-PF10-build-notes-addendum-v1.1`, `remediation-QA110-F01-PF10-build-notes-addendum-v1.0`.
- **Product Owner publication:**
  - PF10 v13.8 (`21141b39`) carries addenda 2.27 and 2.28.
  - No later publication is recorded. Under CR-12, no PF10 addendum records the Plan v1.3 change; this report, the QA-70 reviews v1.3 and v1.4 and the redline application report v1.2 record it.
  - Any informational publication of this verdict is the Product Owner's and is pending.

## 14. CANON_CONFLICT_REGISTER (carried)

Held in full in Plan v1.3 §13; carried unchanged. QA-120 adds none.

| ID | Status | Decision owner |
| :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth |
| CR-4 | `APPROVED` | Product Owner |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20 |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner |
| CR-9 | `PROPOSED`, unreviewed | Isis, IA-30 boundary |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40 |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis, QA-70 review v1.0 |
| CR-12 | `APPROVED`, alternative (a) | Product Owner, 2026-10-25 |

## 15. TypeSafe reading for the receiving session (CL-C-10)

Action sent (v8.2): "As the continuing technical lead and terminal closure authority, perform the retrospective and decide closure for one completed change request of 22 requirements delivered by about twelve already-reviewed work units, from its approved specification and plan, every work unit's acceptance record, its Ops receipt and documentation completion, and a final QA report with verdict PASS plus a separate root-cause analysis: reconcile delivered against intended scope, judge whether any acceptance-critical blocker remains, record an explicit close or do-not-close decision with reasons, and list post-closure work separately. It is a Markdown decision record only; no code runs and no live call occurs; a closure memo follows a close decision."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 3.06 (confidence 0.59); rung probabilities low 0.01, medium 0.05, high 0.15, extra high 0.46, max 0.33, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.75, Sonnet 5.5 0.22, Haiku 5.5 0.00 (confidence 0.67). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.014, Fable 5.1 at max 0.010, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.007, Opus 5.5 at medium 0.038, Opus 5.5 at high 0.112, Opus 5.5 at extra high 0.345, Opus 5.5 at max 0.247, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.002, Sonnet 5.5 at medium 0.011, Sonnet 5.5 at high 0.033, Sonnet 5.5 at extra high 0.101, Sonnet 5.5 at max 0.073, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between max and extra high. Sent 2026-10-26T00:27:58Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-26T00:27:58Z; HTTP 200 in 0.47 s; 5472 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between max and extra high.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "CL-C-10 HDE-CRD-0002 retrospective and closure decision", before this report was saved.
- **Records:** the Notion row was not written.
- **Picks:** CL-C-10: Nathan's pick is not stated. This QA-120: Nathan's pick is not stated; its reading is in QA-110 review v1.2 §9 (Opus 5.5 at extra high, score 3.30).

**Surface advice.**
- **Session.** CL-C-10 in the continuing Isis session for HDE-CRD-0002 (Isis-53, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok) on `amthorn78/glow-hdengine-v2`, with Notion read access for the CL-C-10 prompt and the CL-20 receiver it names.
- **Reads.** This Report and the RCA first, then §13's evidence set. HDE Build Notes 2.19 to 2.28 in `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md` record most of the lineage in one place.
- **No access needed:** production, Railway, the vendor or the database; no execution.
- **Writes:** only the closure decision and its handoff under `docs/ephemeral/`, by pull request.

## 16. Nonclaims (Plan v1.3 §12)

This Report, its `PASS` verdict and the run establish none of the following:
- acceptance of HDE-CRD-0002, closure, or a close pack;
- PF09 or PF30 movement;
- deployment or release activation;
- broad HumanDesignAPI v2 conformance, or mapped-cache persistence;
- live Reader success or Gate readiness;
- canon drainage;
- a decision on any routed Product Owner item (FND-012, FND-028, FND-029, X-02, the legacy chart-loader defect).

The pre-push tool's result and hosted CI are not QA verdicts.

## Canon relied on

Read on `main` at `48cdc25`; `docs/pfcanon/` last changed by `21141b39`, byte-identical to what QA-80 and the QA-110 reviews v1.1 and v1.2 read. This branch edits no `docs/pfcanon/` file.

| Decision topic | Sources read | Applied in |
| :- | :- | :- |
| Report and RCA contract; routing | QA-120 — Create Final QA Report and RCA — 100926.1 (page state 2026-10-12T02:29:51.614Z), read in full in this session: "Required inputs", Execute 1 to 5, "Required result and routing" (PASS → CL-C-10 for a CRD); CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1 (page state 2026-10-12T02:29:13.994Z), read in full at this invocation: "Inputs", "Execute", "Required result" | §1, §13, handoff |
| Report, RCA and closure separation | PF19-Canon-Glow-QA-Guide v3.0.6 §3.1.2 "Independent QA, reporting and closure", read in full at this invocation ("Every completed QA run requires a final QA Report and a separate RCA, including an all-PASS run") | §1, RCA |
| Verdict criteria, report contents, coverage | Plan v1.3 §10, §11 and §12 (this author's own, approved); Plan Templates "Exact status predicates" (as read at QA-110) | §1.1, §5, §11, §16 |
| Moon Loops, reruns, attempts | PF19 v3.0.6 §3.4.8 and §10.6; PF27-Canon-Plan-Templates v2.0.5 "Moon Loop allowed (bounded)" and "Bounded step-level rerun posture" (read in full at QA-110 v1.2 and earlier in this session); HDE Build Notes 2.28 (R-1, R-2) | §9 |
| Remedy and its verification | HDE Build Notes v13.8 addendum 2.27 (Cause, R-1 to R-6, C-1, V-6), read in full at QA-80 in this session | §8 |
| Deployed identity | HDE Build Notes 2.19 (deployment by commits landing; judged by `release_id`) | §3 |
| Close-format obligation (FND-030) | `tools/qa/generate_epic_close_pack.py` `QA_REPORT_RE` and `_qa_report_verdict` (read; the format this file meets); HDE Build Notes 2.16 LR7-O4 as the Triage records it | §11 FND-030 |
| Secrets (I-1) | PF19 v3.0.6 §3.5.7 (read in full at QA-110 v1.2); `AGENTS.md` redaction rule | §10 |
| Evidence attribution | `AGENTS.md` "Evidence attribution, currentness and distinct decisions" and "Path-proof portability" | §3, §7, §10 |

In-flight documents relied on: the three QA-110 reviews, the four collections and four QA-100 result sets, Plans v1.2 and v1.3 with their approving reviews, the Live QA Guide v1.0 §6 (IR-1 to IR-11) and the Change Audit Triage v1.1 (FND rows, read for the listed IDs). Specification v1.1-approved S-rows and the work-unit lineage reviews were read for their decision lines and identities only; their substance is the closure owner's to read.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-120-20261026-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | Whole QA run: Plan v1.3 checks 1 to 21; S02 to S22, S01 removed |
| prompt | QA-120 — Create Final QA Report and RCA — 100926.1, page state of 2026-10-12T02:29:51.614Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-120 (`PASS`; next CL-C-10) |
| capture time | 2026-10-26T00:45:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-110-20261025-01, -20261025-02 and -20261026-03; the QA-50, QA-70, QA-80, QA-90, QA-100 and ESC uses each review lists |
| task/result/review mapping | §4 |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
