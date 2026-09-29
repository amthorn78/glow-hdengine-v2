---
artifact_type: QA_RCA
artifact_id: HDE-EPIC040-QA120-QA-RCA
artifact_version: "1.0"
predecessor: none. This is the first QA RCA for the HDE-EPIC040 QA run
companion_report: docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md (QA_REPORT_ID HDE-EPIC040-QA120-QA-REPORT, v1.0; verdict PASS)
run_verdict: PASS
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
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010)
evidence_of_record: branch qa/hde-epic040-qa100-plan-v1.2-run-20260929 at commit 787bb97b58b638d6b307cad6d76484c883c58aec
tested_source: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d
observed_revision: 917909c75390c871c5710c5b60177bb53fd01919 (origin/main at this invocation)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.8.md (SHA-256 5fb9bad917a1a2c5a8cd86fa38ee0a2a6be824985a9685e97bf88091aff777ce)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-120 (QA-120 is not an addendum producer)
---

# HDE-EPIC040 — QA RCA and Doc Delta summary (QA-120), v1.0

## 1. Summary

- **Outcome.** The QA run passed. All 12 checks of QA Plan v1.2 are `PASS` in both result layers. No product-behavior failure occurred in the evidence of record, so this RCA names no product root cause. It does not invent an incident for a passing run (Glow QA Guide §3.1.2).
- **What this RCA records.** The actual failures around the run, their corrections, the accepted deviations, causal limits and lessons:
  - two QA Plan approvals that the Product Owner overturned before the run;
  - an execution under the rejected Plan v1.0 that is not carried forward;
  - two stored executions of one task collection;
  - six defects in Kronos's own task collections (K-01 to K-06) and one execution-recording lesson (K-07);
  - a vendor-execution authority conflict that HDE Build Notes 2.34 decided.

  None of them changed a predicate outcome of the approved run.
- **Canon updates.** No new PF-Canon delta is identified for product behavior. Documentation deltas DD-01 to DD-13 and the drainage of C040-05 to C040-10 are pending with their owners, and §10 proposes six process and documentation deltas. None is a blocker for a step verdict or for the closeout recommendation (Plan v1.2 §13).
- **Closeout readiness.** The QA outcome supports `CLOSE` (§12). The decision is Isis's.

## Canon relied on

Read from `docs/pfcanon/` on `main` at `917909c`, as recorded in the companion Report's "Canon relied on":
- **HDE Build Notes v13.4.8**: 2.29, 2.33 and 2.36 in full; 2.32, 2.34 and 2.35 as read earlier in this session; whole-document search.
- **Glow QA Guide v3.0.5**: §3.1.2, §3.1.3, §3.3, §4.4.1, §9.2.15.5 to §9.2.15.8, §10.7, §10.8, §11.1.
- **Change Process Guide v2.5.3**: §0.4.1 to §0.4.1.3 in full. This RCA follows its §0.4.1.2 "Mandatory QA RCA & Doc Delta summary".
- **Plan Templates v2.0.4**: §9, for compatible RCA structure only (Glow QA Guide §10.7).
- **HDE Build Checklist — Separation v1.1.5**: HDE-SEPA005.

In-flight documents read at this invocation:
- **in full:**
  - the planning-failure RCA v1.1;
  - the QA-90 handoff RCA v1.0;
  - the Alpha feedback brief "QA Plan approval never tests whole-plan coherence" v1.0;
  - the approval revocation v1.0 and the Alpha state record v1.0;
  - QA-70 review v1.4;
  - the stored doc-delta surface at `787bb97`;
- **in the parts relied on:** the three QA-110 reviews (per-task reviews, deviations, defects, lineage and open items), which this session authored and had read in full earlier;
- **the remaining inputs:** as the companion Report's "Canon relied on" records, which states for each whether it was read in full or in part.

## 2. What ran and what the outcomes mean

| Item | Fact |
| --- | --- |
| What ran | The 12 checks of approved QA Plan v1.2 at tested source `0db3f0ef`. Checks 1 to 10 and 12 ran under the closed posture; check 11 ran under the CLI-local vendor posture. Proof classes: ops and identity (checks 1, 2); local/offline with no vendor (checks 3 to 8, 12); in-process (check 9); loopback HTTP under the closed posture (check 10); vendor-backed (check 11) |
| Outcome meanings | `PASS` means every [E] predicate held at execution and every [K] predicate held at QA-110 (Plan §12). No check recorded `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED` or `PARKED` in the evidence of record |
| Evidence that proves them | One manifest, 12 primary logs, 14 supplementary files and 15 path proofs under `audit/qa/hde-epic040/` and `audit/docdeltas/` on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97`. Digests are in the Report §6. The [K] evaluations are in QA-110 review v1.0 §5, review T11 v1.0 §4 and review T12 v1.0 §4 |
| Steps blocked by unavailable inputs | None. The two requirements that depend on inputs unavailable before the Glow App are not steps: the approved Plan deferred them (Plan §2). Had they been planned as steps, their outcome would have been `TOOLING_BLOCKED` for input availability, never `PASS` (QA Audit QA50-F05). No artifact was expected for them in this run. Rerun condition: a future epic that defines user-bound QA surfaces once the App user model exists (Plan §2; Glow QA Guide §3.3) |
| Canon updates required | Documentation drainage only (§10). "No new PF-Canon deltas identified" for product behavior |

## 3. Source-of-truth posture

- **Primary epic-specific execution source.** The governed QA root at `787bb97`, together with the three QA-110 reviews that evaluated its [K] predicates.
- **Canon homes used for closeout interpretation.**
  - Glow QA Guide §3.1.2, §3.3, §9.2.15.5 to §9.2.15.8, §10.7 and §10.8.
  - Change Process Guide §0.4.1.
- **QA Plan v1.2.** The run's approved contract and the intended QA requirement framing.
- **Live QA Guide v1.0.** Goal and scope framing only. The Plan records its §4.3 (a mandatory live readiness run) and §5 (a rails statement) as superseded by canon (Plan v1.2 §2.1).
- **HDE Build Notes addenda.** 2.32, 2.35 and 2.36 record the QA-110 decisions with direct evidence-pointer lines: commit identifiers, repository paths and SHA-256 values. They are not evidence-light guidance. No addendum is the decisive close authority.
- **Mismatches between the primary source and the QA Plan.** None. The manifest holds exactly the 12 Plan checks in Plan order, and each `log_path` is the path the Plan states (review T12 K1 and K2; re-verified at this invocation).

## 4. Coverage vs QA Plan, in plan order

| # | Plan step | Evidenced | Governed pointer | Mismatch vs Plan | Accepted execution deviation | Closeout impact |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `d0-discovery` | Fully | `audit/qa/hde-epic040/checks/d0-discovery/primary.log` | None | Second execution without a QA-110 decision (LR-01); collected count 2,092 against the reference 2,090, explained (results v1.1 D-03) | Non-blocker |
| 2 | `step-0b-doc-delta-capture` | Fully | `…/step-0b-doc-delta-capture/primary.log`; both doc-delta surfaces | None | LR-01 | Non-blocker |
| 3 | `ac040-08-evidence-validators` | Fully | `…/ac040-08-evidence-validators/primary.log` | None | Attempt label unknown (LR-01 item 7) | Non-blocker |
| 4 | `ac040-02-03-catalog-config` | Fully | `…/ac040-02-03-catalog-config/primary.log` | None | LR-01 | Non-blocker |
| 5 | `ac040-04-05-admission-identity` | Fully | `…/ac040-04-05-admission-identity/primary.log` | None | LR-01 | Non-blocker |
| 6 | `ac040-06-golden-comparison` | Fully | `…/ac040-06-golden-comparison/primary.log` and its four files | None | LR-01 | Non-blocker |
| 7 | `ac040-07-gate-ingress-offline` | Fully | `…/ac040-07-gate-ingress-offline/primary.log` | None | LR-01 | Non-blocker |
| 8 | `ac040-04-09-compat-cli-offline` | Fully | `…/ac040-04-09-compat-cli-offline/primary.log` | None | LR-01. Three recorded skips, which contribute no proof | Non-blocker |
| 9 | `ac040-09-reader-http-in-process` | Fully | `…/ac040-09-reader-http-in-process/primary.log` | None | LR-01 | Non-blocker |
| 10 | `sec-reader-http-live` | Fully | `…/sec-reader-http-live/primary.log`, `http_probes.jsonl`, `gunicorn_server.log` | None | LR-01; E-01 normalization; D-02 operator repeat before the server started | Non-blocker |
| 11 | `open-rails-showcompat-vendor` | Fully | `…/open-rails-showcompat-vendor/primary.log` and its five files | Executor: the Product Owner's directed agent instead of the Product Owner in person | D-01, authorized by HDE Build Notes 2.34; E-01 normalization | Non-blocker |
| 12 | `qa-closeout-deliverables` | Fully | `…/qa-closeout-deliverables/primary.log`; 15 path proofs | None | D-03 runner script (O-01, K-07) | Non-blocker |

`…` stands for `audit/qa/hde-epic040/checks`, on branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97`.

The two deferred requirements are not Plan steps. The Report §4 accounts for them as uncovered by approved deferral.

## 5. Same-run runtime proof

Same-run runtime proof exists at tested source `0db3f0ef` across the changed runtime surfaces that the approved Plan requires. Each surface is proven at its stated proof class:

| Surface | Proof class | Governed artifacts |
| --- | --- | --- |
| Admission of the complete release, the pure core and release identity | Local/offline | Checks 1 and 5 |
| Catalog and mechanics configuration | Local/offline | Check 4 |
| Read-only golden comparison | Local/offline | Check 6 |
| Gate ingress and the readiness command | Local/offline | Check 7 |
| Compat and CLI | Local/offline | Check 8 |
| Compat and CLI | Vendor-backed | Check 11 |
| Reader v1 and v2 routes | In-process | Check 9 |
| Reader v1 and v2 routes | Loopback HTTP under the closed posture | Check 10 |

Absent by approved deferral: live current-row Gate readiness and the live DB Reader success path (Report §7.2).

## 6. Failures, corrections and causes

These are the actual incidents only. The classification column uses the Change Process Guide §0.4.1.2 status classes where the incident is a step outcome. Planning and process incidents that are not step outcomes are labelled as such.

### 6.1 Before the run: QA planning and review

| ID | What happened | Evidenced cause | Classification | Correction |
| --- | --- | --- | --- | --- |
| F-1 | On 2026-09-27 the Product Owner rejected QA-70 review v1.0, which had approved QA Plan v1.0. That Plan mixed `SAFE_MODE=0` with `ALLOW_NETWORK=0`, switched rails per command, and planned live database checks that need users who do not exist before the App | Stated by the reviewer in RCA v1.1: "The failure is mine: Claude's execution of the work."<br>**Root causes:**<br>- C1: the governing QA canon was not read.<br>- C2 and R9: canon conformity was claimed without reading canon.<br>- C3 and R8: the Product Owner was asked questions canon answers.<br>- C4: the Guide originated defective content.<br>- C5: code behavior was reviewed instead of canon posture.<br>- C6: the Implementation Plan and Specification lack the epic rails statement.<br>**Contributing:**<br>- documentation gaps D-1 to D-4;<br>- prompt gaps P-1 and P-2 | Not a step outcome (planning and review) | QA-70 review v1.1 `DENY` with redlines; QA Plan v1.1 |
| F-2 | The QA-70 to QA-90 handoff carried no task selection and no operational rails | QA-90 handoff RCA v1.0:<br>- RC-1: the handoff contract has no field for the Product Owner's selection.<br>- RC-2: the selection was not put to the Product Owner.<br>- RC-3 and RC-4: the Plan had no operational rails table or per-command unset wording.<br>- RC-5: the list was re-sorted | Not a step outcome (handoff) | Later handoffs carried the Product Owner's selection explicitly: "Tasks: 1-10", "Task: 11", "Selection: check 12". The prompt change (RC-1) is a GCFPE-MGMT-10 matter; the Alpha feedback brief lists the QA-90 handoff RCA as Alpha feedback entry AF-021 |
| F-3 | Checks 1 to 10 were executed under Plan v1.0 (commit `06b04a9`). In that execution, check 3's group G failed at the file-mode assertion of `tests/evidence/test_evidence_index_missing_state.py`: the Codespace checkout mode was 666 and the regenerated mode 644 | The venue's umask shaped the checkout mode. The Plan wrongly said the venue could not affect results (RCA v1.1 D7; QA-70 review v1.1 FND-008) | `TOOLING_BLOCKED`-class under the Plan v1.2 venue rule (a required environment fact), never `FAIL_BEHAVIOR`. Historical: the execution is not carried forward | Plan v1.2 venue rule and check 3 venue evidence. Run B recorded `umask` 0022 and mode 644, and group G passed |
| F-4 | On 2026-09-27 the Product Owner revoked QA-70 review v1.2's approval of QA Plan v1.1 as "abject failure". Checks 12 and 14 ran nothing (`PARKED` records), check 13 was an empty numbered heading, and seven checks re-ran test groups and validators that CI had already run, with only a general note on change-aware CI as the reason | Alpha feedback R1 to R6:<br>- the re-review audited redline application rather than judging the whole Plan;<br>- "coherent" had no operational test;<br>- QA-80 preserved removed and parked checks to keep their identity;<br>- the reviewer judged the result of its own redline RL-09;<br>- QA-50 did not require binding CI evidence instead of re-running it.<br>Revocation §2 records the same facts | Not a step outcome (review) | Isis-52 replaced the reviewer for QA-70. Review v1.3 `DENY` (FND-101 to FND-107; RL-01 to RL-08). Plan v1.2 then moved the deferred requirements into the scope section, dropped every non-executing check, bound the exact-head CI evidence (§10.2) and stated what each re-run adds. Review v1.4 `APPROVE` |

The Alpha state `ALPHA_STOPPED_FAILED_AT_QA` (2026-09-27) named QA-70 as the resume point. The resumed flow is the run this RCA covers.

### 6.2 During the run

| ID | What happened | Evidenced cause | Classification | Correction |
| --- | --- | --- | --- | --- |
| F-5 | Two stored executions of collection v1.1 exist. Run A, in a Codespace, executed T01, T02 and T04 to T10 and stored its evidence on `qa/hde-epic040-qa100-plan-v1.2`. Run B, in the Product Owner's Linux shell, then executed T01 to T10 and stored them on a new branch | The collection checked for an existing QA root only in the fresh clone, and checked `origin` for the evidence branch only at storage time (K-03). Review v1.0 records the process miss as D-13, a gap shared with the collection design | None: no step status was affected, and outcomes are equal wherever both runs recorded (review v1.0 §4.1). It is a process deviation: the one ordinary rerun of nine checks was consumed without a decision | Ruling LR-01. Collections v1.3 and v1.4 checked `origin` before the first command |
| F-6 | Run A left no trace of T03, and no primary log or receipt for T10 | T10: probably K-01, since `CheckResult` rejects the empty-string argument of command 11. This is an inference and is not established. T03: unknown | T10: `FAIL_TOOLING`-class at recording, by inference only. T03: unknown. Neither governs; Run B is the evidence of record | Carried as an unknown (LR-01 item 7), owned by the Product Owner, who holds the Run A Codespace |
| F-7 | Run A's T01 command 22 first exited 2 because a stray backtick and full stop had been copied from the collection; it was repeated. Commands 26 and 27 were repeated after a wrong stdout target. Four Run A logs lack an OUTPUT section | Command 22: collection presentation, inline code followed by a full stop (K-02). Commands 26 and 27: operator error. Missing OUTPUT sections: cause not recorded | None: within a non-canonical run, recorded in its body | Later collections put each command in its own fenced block |
| F-8 | Run B's T10 command 11 first ran with a 65,446-byte request file and was repeated with the correct 32,769-byte file before the server started | Operator error while applying normalization E-01 (results v1.1 D-02) | None: no probe used the wrong file, and it is not an attempt | Recorded in `argv.txt` and the body |
| F-9 | The Plan assigned check 11's vendor commands to the Product Owner in person. The Product Owner directed the QA-100 session to execute them | A canon conflict on vendor-call authority (C040-10) that no decision had yet settled | None: authority resolved | The Product Owner decided it the same day in HDE Build Notes 2.34. Three fixed-text lines in the evidence still name the Product Owner as executor (K-06); the header's `command_provenance` is accurate |
| F-10 | T12's executor fed the commands through one runner script, against the collection's "no script file", and did not record it in `command_provenance` | The collection did not state how command blocks are fed or how an intermediate file is recorded (K-07) | None: the executed bytes equal the collection's, and every [E] result was re-derived from the raw captures | Lesson K-07 |

## 7. Accepted deviations

Deviations are surfaced separately here, as Change Process Guide §0.4.1.2 requires, even though every step is fully evidenced and `PASS`.

| Check | Deviation | Disposition and pointer |
| --- | --- | --- |
| 1, 2, 4 to 10 | Second execution without the QA-110 decision that attempt 2 requires (D-12) | Ruled in LR-01; process deviation; rerun allowance consumed (review v1.0 §4.2) |
| 1 | Collected count 2,092 against the reference 2,090 (D-03) | Explained by two added parametrize cases (review v1.0 T01) |
| 3 | Venue rule evidence recorded; rule not triggered | Review v1.0 T03 |
| 10 | E-01, a one-space final argument; D-02, an operator repeat | Syntax-origin normalization (Glow QA Guide §3.4.10); not an attempt (review v1.0 §6.1) |
| 1 to 10 | D-04 tested source differing from the collection's observed revision by one docs-only commit; D-05 other venue; D-06 the recording invocation is not a check command; D-07 inline capture wrapper; D-08 read-only observations; D-09 server posture; D-10 storage branch; D-11 versions; D-14 trailing space | Accepted (review v1.0 §6.1) |
| 11 | D-01 delegated vendor execution; D-02 vendor configuration from the environment; D-03 restore scope; D-04 commit identity; D-05 `/tmp` helpers; E-01 normalization | Accepted (review T11 §5.1) |
| 11 | D-06 (the collection defect K-05); D-09 (a model switch during the session, with no effect on identity, scratch state or evidence) | Confirmed and noted (review T11 §5.1) |
| 11 | D-07: HDE Build Notes 2.34 rule 5 against Plan v1.2 §5.2, which unsets `HDAPI_BASE_URL` | Noted. No effect: `HD_API_BASE_URL` was set, and no vendor task remains under Plan v1.2. For any later vendor task under this Plan whose environment holds only the alias, 2.34 governs |
| 11 | D-08: `.env.example` lacks `GEO_API_KEY` | Documentation drift owned by the implementation lane (a 2.34 deferred obligation). It is not a `DOC_DELTA:` line, so it is not in DD-13 |
| 12 | D-01 automated QA/infra executor; D-02 storage authorization; D-03 runner script (O-01); D-04 committer identity; D-05 wording corrected; D-07 HDE Build Notes version | Accepted (review T12 §5.1) |
| 12 | D-06 (one model used throughout, with no effect) | Noted (review T12 §5.1) |

## 8. Normalizations, Moon Loop and rerun lineage

- **Normalizations.** T10 E-01 (a one-space final argument) and T11 E-01 (command text taken mechanically, a syntax-origin normalization). Each is recorded in its header's `command_provenance` or the result. T12 D-03 is an execution-recording deviation, not a normalization.
- **Moon Loop.** None. No `audit/qa/hde-epic040/00_meta/delta/` record exists.
- **Reruns.** None was routed or executed. No failure signature, remediation note, `attempt1_primary.log` or `rerun_note.md` exists, so none can be cited.
- **Attempt history against the governing outcome.** For checks 1 to 10 the governing outcome is Run B's (LR-01 item 4). Run A's executions are preserved as a non-canonical record on their own branch. No earlier failed attempt of Plan v1.2 exists to supersede. Where Run A recorded a result it equals Run B's. The Plan v1.0 executions (`06b04a9`) belong to a rejected approval and are not attempts under Plan v1.2.

## 9. Root cause analysis

This section follows the compatible structure of Plan Templates §9.

### 9.1 Failure and friction patterns

| ID | Pattern | Class | Evidence |
| --- | --- | --- | --- |
| FP-1 | QA artifacts were authored and approved without reading the governing canon | Planning drift | F-1; RCA v1.1 C1 to C5 |
| FP-2 | Approval narrowed to redline verification; whole-plan coherence was untested | Planning drift | F-4; Alpha feedback R1, R2, R4 |
| FP-3 | The handoff contract had no carrier for the Product Owner's task selection | Process rail gap | F-2; QA-90 handoff RCA RC-1 |
| FP-4 | Collection guards checked local state, not `origin` | QA harness process | F-5; K-03 |
| FP-5 | A collection dry run did not pass real command lines through the recorder | QA harness process | F-6 (inference); K-01, K-04 |
| FP-6 | Evidence fields stated the executor as fixed text | Evidence posture | F-9; K-06 |
| FP-7 | The task did not require intermediate helper files to be disclosed | Evidence posture | F-10; K-07 |
| FP-8 | A test assertion depends on the venue (checkout file mode) | Current-reality context | F-3 |

### 9.2 Primary root cause

The two overturned approvals (F-1, F-4) are the incidents with the largest effect. Their evidenced primary cause is that QA planning artifacts were approved without being tested against the governing canon and against the Plan as a whole.
- For the first approval: canon was not read (RCA v1.1 C1, C2).
- For the second: canon was read, but only the application of the redlines was checked (Alpha feedback §1: "The failure was not a reading gap").

For product behavior there is no root cause, because no product failure occurred.

### 9.3 Contributing factors

- **CF-1.** Canon documentation gaps recorded in RCA v1.1 (D-1 to D-4): Glow QA Guide §2.3 invites a rails question that §3.3 and §3.4.8 already answer; Glow Infrastructure §2.4 lacks a complete QA Codespaces rails pair and holds a stale inventory; "production endpoints" is ambiguous for the database.
- **CF-2.** Prompt gaps:
  - from RCA v1.1: no task-selection field (P-1) and no required per-check rails determination (P-2);
  - from the QA-90 handoff RCA: RC-1, the same selection gap;
  - from the Alpha feedback brief: no operational coherence test for approval or re-review (R1, R2); QA-80 preserving non-executing checks (R3); a reviewer judging its own redlines (R4); no rule on binding CI evidence (R5).
- **CF-3.** Parallel operator sessions in two venues with no shared guard (F-5).
- **CF-4.** A canon tension on vendor-call authority that no decision had yet settled until HDE Build Notes 2.34 (F-9).

### 9.4 What made the failures hard to detect earlier

- The QA-70 reviews verified outputs and redline application, not canon posture or whole-plan coherence (RCA v1.1 R1 to R7; Alpha feedback §1).
- The collection dry run used synthetic argv lines, so K-01 reached execution (K-04).
- Run A stored its evidence on a branch that Run B's setup did not check (K-03).

### 9.5 What made the run hard to close confidently, and how it was resolved

- **Two stored executions.** Resolved by LR-01: Run B is the evidence of record, and the outcomes are equal.
- **Run A's missing T03 trace.** Left open as a non-gating unknown.
- **The executor of check 11.** It differed from the Plan's assignment until HDE Build Notes 2.34 decided the authority.

### 9.6 Causal limits

These are unknown and are not asserted:
- why Run A left no T03 trace;
- whether K-01 caused Run A's missing T10 receipt (an inference);
- why four Run A logs lack an OUTPUT section;
- for the planning failures, whether IA-10 and IA-30 name the Plan Templates rails section (RCA v1.1 §7, not checked).

This RCA establishes no cause beyond those its sources record.

### 9.7 Remediation-loop assessment

| Loop | Outcome | Residual uncertainty |
| --- | --- | --- |
| RL-A: QA-70 review v1.0 rejected, then review v1.1 `DENY`, Plan v1.1, review v1.2 `APPROVE` revoked, review v1.3 `DENY`, Plan v1.2, review v1.4 `APPROVE` | The approved Plan v1.2 executed to `PASS` | None for the run. Prompt hardening rests with GCFPE-MGMT-10 through the Alpha feedback brief and RC-1 |
| RL-B: ruling LR-01 on two executions; no rerun | Evidence of record fixed; outcomes equal | Run A's T03 outcome is unknown |
| RL-C: C040-10 decided by HDE Build Notes 2.34; T11 accepted | Delegated execution authorized | Drainage of the superseded passages is pending |

## 10. Doc deltas

### 10.1 Carried from the run: DD-01 to DD-13

These rows are taken from the stored doc-delta surface at `787bb97`. Every row states "Drives decision: No". Documentation drainage never blocks a step verdict or the recommendation (Plan v1.2 §13).

| ID | Delta | Drain target (title) | Owner |
| --- | --- | --- | --- |
| DD-01 | The QA Codespaces inventory lists the retired `DB_BRIDGE_URL` (QA50-F14) | PF07-Canon-Glow-Infrastructure §2.4 | PF07 maintainer |
| DD-02 | Glow Infrastructure §2.8 forbids git operations and QA-time scripts; Glow QA Guide §3.4.9 and Plan Templates permit read-only observation and embedded harness calls (C040-09) | PF07-Canon-Glow-Infrastructure §2.8 | PF07 maintainer |
| DD-03 | Glow QA Guide §§3.4.3, 3.6 and 10.8 name ChatGPT Library or Google Drive; superseded by HDE Build Notes 2.29, wording drainage pending | PF19-Canon-Glow-QA-Guide §§3.4.3, 3.6, 10.8 | PF19 maintainer |
| DD-04 | PF05 §7.1.11 `--allow-prod-vendor` is not implemented (QA50-B01) | PF05-Canon-HDE-CLI-API-Vendor-Ref §7.1.11 | PF05 and CLI owners |
| DD-05 | AGENTS.md's "PF10 §2.8" citation; resolved by a document update | AGENTS.md | Repository docs owner |
| DD-06 | Guide §8 names `6e4b3a1` as the attestation candidate; the attestation binds `6f53d82` (QA50-F11) | None (ephemeral record) | Isis |
| DD-07 | Drainage of C040-05 to C040-08 pending (RA-18) | Per register | Named maintainers |
| DD-08 | `showcompat` help says Reader v1 (O-P07-01) | Repository CLI help | Whole-change IA |
| DD-09 | `APP_ENV` asymmetry between dev `GET /reader` and the conjunction routes (O-P07-04, RA-06) | O-P07-04 record | Whole-change IA |
| DD-10 | `ci/checks/check_mirror_schema.sh` is Python; AGENTS.md invocation (RA-13) | AGENTS.md | Repository docs owner |
| DD-11 | `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` (FND-017) | `docs/ADAPTER_009.md` | Compat docs owner |
| DD-12 | HDE Build Notes 2.28 line references to 2.19 and 2.20 are off by two | PF10-HDE-Build-Notes §2.28 | PF10 drain owner |
| DD-13 | HDE CLI/API Vendor Ref §3.7 lists `HDAPI_BASE_URL` among the CLI vendor smoke's target facts, while its §1, Glow Infrastructure §2.7 and Glow QA Guide §3.5.7 make `HD_API_BASE_URL` canonical and `HDAPI_BASE_URL` a deprecated alias (from check 11) | PF05-Canon-HDE-CLI-API-Vendor-Ref §3.7 | PF05 maintainer |

The drainage of C040-05 to C040-10 is also pending with the owners named in the register (Report §19).

### 10.2 Proposed by this RCA (PF-Canon only, excluding HDE Build Notes)

**Glow QA Guide deltas:**

| ID | Section | Delta | Tag | Why and evidence |
| --- | --- | --- | --- | --- |
| PF19D-001 | §2.3 | Point the sentence "Every EPIC’s PO specifies what rails posture must be used to accept the epic" to §3.3 and §3.4.8, which already fix the posture for pre-App Engine and CLI Live QA | CLARIFICATION | Read literally, the sentence invited a question that canon answers (F-1; RCA v1.1 D-1) |
| PF19D-002 | §3.4.8 | State whether "production endpoints" includes the production database | CLARIFICATION | RCA v1.1 D-4. §3.3 made it moot for this epic |
| PF19D-003 | §9.2.15.5 | Before a task collection's first execution, check `origin` for an existing evidence branch or QA root for the change and stop if one exists, so that a second operator session cannot duplicate the executions | NEW CANON PROPOSAL | F-5; K-03 |
| PF19D-004 | §4.4.6 | Record each executor and recorder identity in step-log evidence from a captured identity, not as fixed text | CLARIFICATION | F-9; K-06 |

Owner of PF19D-001 to PF19D-004: the Glow QA Guide maintainer.

**Other PF deltas** (Glow QA Guide is not their correct home):

| ID | Document and section | Delta | Tag | Why PF19 is not the home, and evidence |
| --- | --- | --- | --- | --- |
| OPFD-001 | PF07-Canon-Glow-Infrastructure §2.4 | Give QA Codespaces a complete rails pair and an inventory that matches the console | CONSISTENCY | Environment inventories are owned by Glow Infrastructure (RCA v1.1 D-2, D-3; overlaps DD-01) |
| OPFD-002 | PF06-Canon-Change-Process-Guide §0.4.1.2 "Location" | Reconcile the governed placement of the QA RCA summary with HDE Build Notes 2.29's storage of change-process RCAs in `docs/ephemeral/`. State whether a `docs/ephemeral/` RCA suffices at the Close Gate or must be copied by the close-pack writer | CONSISTENCY | The location rule is owned by the Change Process Guide. This RCA exists only in `docs/ephemeral/` (§11) |

Prompt-level causes (R1 to R6, RC-1, P-1, P-2) are not PF-Canon deltas. They are routed to GCFPE-MGMT-10 through the Alpha feedback brief and the QA-90 handoff RCA.

### 10.3 Follow-on carriers

| Delta or item | Carrier |
| --- | --- |
| DD-01 to DD-13, PF19D-001 to PF19D-004, OPFD-001 and OPFD-002 | The named maintainers at their next revision of each document. No follow-on epic is required |
| The deferred live Gate readiness and live Reader success | A future epic with the App user model (Plan §2) |
| QA50-F01 | The evidence owner, through the whole-change IA PR route |
| Repository hygiene items | CRD candidate 5 (QA-10 triage) |
| Prompt hardening | GCFPE-MGMT-10 |

## 11. Lessons

| ID | Lesson | Correction | Applied |
| --- | --- | --- | --- |
| L-1 (RCA v1.1) | Read the governing canon before authoring or reviewing a QA artifact; cite only canon read; never ask what canon answers | Canon-first rule in `AGENTS.md` and HDE Build Notes 2.29 | From Plan v1.1 onward |
| L-2 (Alpha feedback) | An approval, including one after a revision, judges the whole Plan. Verifying redlines is necessary but not sufficient | Review v1.3 re-judged the whole Plan; the prompt change is with GCFPE-MGMT-10 | Reviews v1.3, v1.4 |
| L-3 (Alpha feedback R5) | Bind existing exact-head CI evidence for closed-rails criteria, and state what each local re-run adds | Plan v1.2 §10.2 | Plan v1.2 |
| L-4 (RC-1) | The Product Owner's task selection travels in the handoff | Explicit selection in each QA-90 handoff | Collections v1.1 to v1.4 |
| K-01 | No command may carry an empty argv part, because the recorder rejects it | Use a one-space argument | Collections v1.3, v1.4 |
| K-02 | Put each command in its own fenced block, with nothing after it | Presentation | Collections v1.3, v1.4 |
| K-03 | Check `origin` for an existing evidence branch before the first task | Setup guard | Collections v1.3, v1.4 |
| K-04 | Dry-run the recorder with the real command lines. The recording invocation is not a check command | Authoring verification | Collections v1.3, v1.4 |
| K-05 | A vendor base URL is configuration, not a secret. Use the environment's vendor configuration with a presence preflight | Task content (HDE Build Notes 2.34 rules 4, 5 and 7) | For future vendor tasks; not applicable to T12, which used no vendor configuration |
| K-06 | Record executors from captured identity files, not fixed text | Evidence design | Collection v1.4 (`executor_identity.txt`) |
| K-07 | State how command blocks are fed; if an intermediate file is used, record its path and role and that it evaluates nothing; take the normalization list from a captured file | Execution recording | For future collections |

None of the lessons changes a Plan objective, proof target, rails posture, evidence identity or predicate of this run.

## 12. Closeout-readiness recommendation and completion states

This recommendation is distinct from Isis's `CLOSE` or `DO_NOT_CLOSE` decision and from any close-report SATISFIED decision.

- **Recommendation.** The QA outcome supports `CLOSE`. The run is complete and `PASS`, and no acceptance-critical QA defect is open. The deferred requirements, QA50-F01, landing the evidence on `main`, the close pack, canon drainage and PF09 maintenance are follow-ups with named owners. Report §15 gives the full recommendation and its labelled Unknowns.
- **Repo-supported completion.** The QA run is complete. This summary is limited to repo-supported completion.
- **Canon-drain completion.** No claim.
- **Formal close-pack completion.** No claim. No `audit/EPIC-040_close_report.md`, `audit/EPIC-040_MANIFEST.json` or `audit/EPIC-040_QA_RCA.md` exists.
- **Merge and close.** The QA evidence of record is not merged, and closure is not decided. Neither is implied.

## 13. Location of this summary

The Change Process Guide §0.4.1.2 lets the QA RCA & Doc Delta summary live in the epic close report or at `audit/EPIC-<NNN>_QA_RCA.md`.

This RCA is a change-process RCA. HDE Build Notes 2.29 stores it in `docs/ephemeral/`, and the QA-120 contract requires it there. QA-120 writes nothing outside `docs/ephemeral/`.

Placing this summary in the governed close pack is work for the authorized close-pack writer, done when a close pack is authorized. It is not done here and not claimed. OPFD-002 proposes reconciling the two locations.

## 14. Nonclaims

- This RCA claims no product defect, because none occurred in the evidence of record.
- It makes no closure decision, acceptance, PF09 status movement, PF-Canon drainage, close pack or HDE Build Notes addendum.
- It executed nothing. It made no vendor, database or network call to a product service, and it changed no approved artifact or evidence.
- Merging the pull request that carries this record preserves the record and approves nothing (D21-C).

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-120-20260929-01. This use is shared with the companion Report.
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-01 to AC040-09; HDE-SEPA005 and HDE-SEPA005.1 to HDE-SEPA005.5; QA Plan v1.2 checks 1 to 12
  - prompt: QA-120 — Create Final QA Report and RCA — 091426.1; Notion 3db4590a05eb81589d21e798cf38e8ba; page as of 2026-09-24T15:53:04.131Z; release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-120
  - capture_time: 2026-09-29T16:47:49Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_RCA v1.0, with QA_REPORT v1.0 (`PASS`)
  - task_and_attempt_mapping: as in the Report's Provenance
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `917909c`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses: listed in the Report's Provenance.
