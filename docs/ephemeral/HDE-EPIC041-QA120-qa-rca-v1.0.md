---
artifact_type: QA_RCA
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA120-QA-RCA
QA_RCA_ID: docs/ephemeral/HDE-EPIC041-QA120-qa-rca-v1.0.md
QA_REPORT_ID: docs/ephemeral/HDE-EPIC041-QA120-final-qa-report-v1.0.md (verdict: PASS)
predecessor: none
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
run_identity: the single approved run of QA Plan v1.0 (T-01 to T-07 attempt 1; P-IDX-RUN; P-EL-01), execution source 6717b29b, evidence landed as 5c9ca784
producer: Kronos, the continuing QA authority for HDE-EPIC041 (role continuity per D27)
prompt: QA-120 — Create Final QA Report and RCA — 102726.1 (https://app.notion.com/p/4064590a05eb810ea503f98b34fa85aa; page state 2026-10-27T13:20:19.853Z)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.5.md
canon_conflict_register: section 7 (the one register for this QA-120 stage)
authored_at: 2026-11-01 (UTC)
GCFPE_PROMPT_USES: "HDE-EPIC041-QA120-20261101 (full entry in the QA_REPORT front matter)"
---

# HDE-EPIC041 — QA RCA v1.0 (QA-120)

## 1. Scope and stance

This RCA covers the completed QA run that the Final QA Report judges `PASS`. **No failure, anomaly, rerun or escalation occurred, and none is invented here** (QA-120 Execute step 4; Glow QA Guide §3.1.2). What follows records:

* the evidenced friction points of the QA stream;
* why each was contained;
* what preserved evidence quality;
* the proof limits that remain.

Causal statements are labelled observed (from a record) or inferred.

## 2. QA timeline (explicit UTC timestamps; primary-source order where none)

| EV | Time (UTC) | Event | Outcome | Pointer |
| :- | :- | :- | :- | :- |
| EV-001 | 2026-10-29 12:29:48 | QA-50 QA Audit and Plan v1.0 land (#803) | PLAN_PENDING | `bba6337c` |
| EV-002 | 2026-11-01 11:10:18 | QA-70 review v1.0 lands (#804) | APPROVE; notes N-01 to N-14 | `6b9c4c40` |
| EV-003 | 2026-11-01 11:35:29 | QA-90 tasks v1.0 land (#805) | TASK_READY (ALL) | `6717b29b`, the execution source |
| EV-004 | 2026-11-01 (session) | Product Owner decisions: commit instruction; PI-01 fresh clone; PI-02 route C, then route A with the Product Owner as IDX-01 author | Recorded | QA-100 results v1.1 §2 |
| EV-005 | 11:51:07 to 11:52:22 | T-01 to T-07 executed | 7 × `PASS`, exit 0 | the primary headers' `timestamp_utc` |
| EV-006 | after 11:52:22 | IDX-01 written; IDX-RUN (write and six validators) | 14 rows; all exit 0 | QA-100 v1.1 §4.1 |
| EV-007 | 12:04:29 to 12:17:08 | #807 opened; exact-head CI run 41304724255 | `success` | #807 |
| EV-008 | 12:22:06 | QA-100 results v1.0 and v1.1 land (#806) | PARTIAL (landing pending) | `ecf3ccf5` |
| EV-009 | 12:31:11 | QA-110 review v1.0 lands (#808) | INCOMPLETE (8 of 9 ACCEPT) | `b5c36196` |
| EV-010 | 12:31:28 | #807 merged | Evidence on `main` | `5c9ca784` |
| EV-011 | 12:31:30 to 12:43:56 | Push CI run 41306902872 on `5c9ca784` | `success` | Actions |
| EV-012 | 12:48:03 | QA-110 review v1.1 lands (#809) | ACCEPT (9 of 9) | `41766acc` |
| EV-013 | 12:56:49 | PF10 v13.9.5 (addendum 2.6, recording QA-110 v1.1) committed by the Product Owner | Published | `6f16420` |

## 3. Failure or friction patterns evidenced

| FP | Pattern | Classification | Evidence | Effect on the run |
| :- | :- | :- | :- | :- |
| FP-001 | The canonical writer cannot index a static registration list before its files exist (`--check` reports `STALE`). Change Process Guide §0.7's QA-branch list names neither Epic QA-root artifacts nor writer tooling, so the evidence and its registration needed a landing route that canon does not spell out | Process-rail gap (canon) | QA Audit QA50-F02 and -F03; CCR-6; Plan §13.1 "Ordering constraint" | Contained: the Plan pre-designed routes A and C; the Product Owner chose A; #807 landed evidence, registration and indices in one mutation set |
| FP-002 | The Product Owner's route decision changed within the QA-100 session (C, then A), and the IDX-01 author was named late | Planning-input timing (observed) | QA-100 v1.1 §0 and §2; #806 PR description still says route C | Contained: QA-100 issued v1.1 and preserved v1.0; QA-110 v1.0 O-01 recorded the stale PR description; no evidence was affected |
| FP-003 | Between execution and push, QA-100 v1.0 held the 28 uncommitted evidence files only on tmpfs `/tmp` | Evidence posture (observed) | QA-100 v1.1 §6 "Persistence"; preservation tar | Contained: route A pushed the evidence within the session; all 28 digests matched at every later read |
| FP-004 | Plan statements were imprecise about runtime behavior: the publish command fails when Step-0B wrote nothing (N-01); proofs keep their first capture time (N-02); the proof count is 13 or 15, not 16 (N-04) | Plan-guidance precision (observed by QA-70) | QA-70 review §6 | Contained: QA-90 carried the cautions into the tasks; the N-01 branch did not occur; QA-110 read times from headers |
| FP-005 | The orientation proof's `produced_at_utc` predates T-01 | Writer semantics (observed; inferred cause: the writer's logical refresh time, set before the QA run) | QA-110 v1.0 O-02 | None; the writer's `--check` and hash checks pass |

No pattern is a product-behavior defect, and none produced a `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `TOOLING_BLOCKED` status.

## 4. Root cause analysis

* **A) Primary root cause.** None. No failure occurred. Every planned predicate held on the first attempt.
* **B) Contributing factors to a clean run** (observed):
  * **CF-001.** A full preapproval smoke of the exact Plan commands. Kronos ran it at QA-50 and Isis reproduced it independently at QA-70. It removed transcription and environment surprises: the four script digests and the 43-test collection matched at every later stage (Plan §9.4; QA-70 §3).
  * **CF-002.** QA-90 extracted the commands and scripts from the approved Plan mechanically, so no hand transcription was needed, and checked them in a throwaway clone (QA-90 §3.2 S-3, §7.1).
  * **CF-003.** Closed rails were enforced by `env -i` on every command, and `captured_env` in every primary shows them (QA-110 v1.0 §3).
  * **CF-004.** D0's caller-set gate re-tested the open-rails determination at the execution source (Plan §3).
* **C) What made it hard to detect earlier.** Not applicable; nothing was undetected.
* **D) What made it hard to close confidently.**
  * Landing and indexing depended on a Product Owner route choice (FP-001, FP-002). QA PASS could not be reached until #807 merged (QA-70 N-14).
  * The two proof limits IR-01 and IR-02 remain bounded, not eliminated (Report §7).

## 5. Remediation loop assessment

* **RL-001.** None. No rerun, Moon Loop, bounded correction, ESC or QA-80 loop occurred.
* **The one routed tooling change, IDX-01,** was planned work under Plan §13.1, not a remediation loop. QA-110 v1.0 §4 classified it as satisfying the Plan's completion predicate.
* **Residual uncertainty:** none for the run's outcome.

## 6. Evidence hygiene and recurrence prevention

* **Strong posture observed:**
  * one primary per check, written by the tracked harness;
  * capture-time path proofs from the canonical writer API;
  * evidence committed exactly as produced (28 of 28 digests stable from capture to `main`);
  * indices regenerated only by the canonical writer;
  * read-only validators run at the reviewed head and again on `main`;
  * distinct source, landing, merge and review-time facts.
* **Recurring proof-risk pattern:** FP-001 recurs across Epics (HDE-EPIC040 D-3 and CC-3; HDE-EPIC041 CCR-6). Every Epic whose QA root is new to the writer needs a tooling registration in the evidence pull request.
* **What would prevent recurrence:** a canon clarification of Change Process Guide §0.7 and §3.5.2.8 that admits Epic QA-root artifacts and their writer registration in one QA landing PR. This is CCR-6's drainage target; the decision belongs to the Product Owner.
* **Template guard to preserve:** the Plan Templates requirement for execution-critical helper readiness (the preapproval smoke), and the QA-90 practice of extracting commands mechanically from the approved Plan.
* **PF doc deltas from this RCA:** none beyond DELTA-001 to -003 (Report §9 line 6) and CCR-6's possible clarification. No new PF-Canon delta is identified for this Epic's behavior.

## 7. CANON_CONFLICT_REGISTER

Carried unchanged from QA-110 review v1.1 §7, with its full history. History addition for every entry: "carried unchanged by QA-120 RCA v1.0, Kronos, 2026-11-01; PF10 v13.9.5 (addendum 2.6) published no ruling on it". For CCR-5: the Product Owner's ruling is still required before CL-05. For CCR-6: route A landed as `5c9ca784`, and the canon disposition is unreviewed.

| ID | Classification | Sources and clauses | Conflict | Affected | Alternatives and recommended disposition | Interim treatment and risk | Drainage target and owner | Status | Reviewer, reviewed artifact, decision time and rationale; history |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION | Plan Templates Preflight B against HDE Governance §2.0.19 and HDE Schemas and Artifacts "legacy token compatibility shape" | Is an acceptance map required for tokenless work? | Specification §10; TI-07 | No operative conflict; listed with no token roster (Ruling R-A) | Close-pack matter for CL-05 | Product Owner (possible canon change) | APPROVED | Thoth, CF-E-30 review v1.1 of Specification v1.1, 2026-10-28; confirmed by Isis, IA-30 review v1.1; carried unchanged by QA Plan v1.0 and here |
| CCR-2 | CANON_RECONCILIATION | HDE Governance §9.7.7 against Plan Templates §2 | Business Case content lists differ | Specification §2 | Specification v1.1 satisfies both | None | None needed | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-3 | CANON_RECONCILIATION | HDE Build Notes (S19 vendor route selection, production vendor override) against the Specification's "adjacent" reading | Possible reach into the orchestration path | TI-02 | Conditional: governs only if the entry performs resolver-selected vendor acquisition | Not triggered (Plan §3; re-checked in §5 here) | Implementation Audit determined applicability | APPROVED as conditional | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-4 | CANON_RECONCILIATION | PF09.3 Task HDE-SEPA006 notes against the current HDE Build Notes | Cited loader record no longer in PF10 | Specification §5 | No conflict; PF09.3 states the defect in full | None | None | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-5 | CANON_RECONCILIATION | HDE Build Notes (close-pack writer only at close, first bullet) against Change Process Guide §3.5.1 "Close-mutation-set stage", Glow QA Guide §3.1.3 and Plan Templates §3B "Entries and exit (normative)" | The Build Notes rule puts the closure decision before the close-pack write; the three permanent documents put the close mutation set before the closure decision | Specification §10, §6 D5; Plan v1.1 DL-04; CL-05 | (A) the Build Notes rule stands; (B) a correcting addendum restores the CL-05 entries and exit; recommended: an explicit Product Owner ruling before CL-05 | The Build Notes rule governs as written; QA planning and execution unaffected (no QA step writes a close pack) | HDE Build Notes under (B), or the three permanent documents under (A); Product Owner | PROPOSED | Not yet reviewed; proposed by Isis, QA-10 triage v1.0 (full entry and history in its §6); recorded in HDE Build Notes 2.5; carried unchanged by the Guide, QA Plan v1.0 and here. Not a QA Plan decision: it bears on CL-05 only |
| CCR-6 | CANON_RECONCILIATION | Change Process Guide §0.7 "QA branches posture" ("Allowed changes are limited to governed artifacts" of a listed set; no tooling) against Change Process Guide §3.5.2.8 "Live QA evidence landing", Glow QA Guide §3.4.3 and §3.4.8 (non-QA-root remediation is a routed work item), and PF09.3 HDE-SEPA006.3 (indexing through the existing writer) | §0.7's list names neither Epic QA-root artifacts nor the doc-delta pair, and no landing route covers evidence plus the writer registration it needs; the writer cannot index a static list before its files exist | QR-04; G-OBS-01; Specification §8, §6 D4; QA Plan §13 | (A) route A under an explicit Product Owner decision (HDE-EPIC040 D-3 precedent, CC-3); (B) route C, a presence-gated writer registration first, then an evidence-only QA PR. Recommended by Kronos: (A), decided by the Product Owner before EL-01, with a later canon clarification of §0.7 | Route A pending PI-02; risk: evidence unindexed if neither is chosen (RK-QA-01), in which case QA PASS is not reachable (Plan §19 item 2) | Change Process Guide §0.7 and §3.5.2.8; Product Owner | PROPOSED | Proposed by Kronos, QA-50 QA Audit v1.0 finding QA50-F03 and QA Plan v1.0 §21, 2026-10-29. **QA-70 assessment (Isis, this review v1.0 of QA Plan v1.0, 2026-10-29):** the Plan's treatment is sound and executable under either alternative. Both keep the same-mutation-set parity rule; both leave the tooling change to a routed PR work item rather than Moon Loop, as Glow QA Guide §3.4.8 requires; neither invents an author, PR or Proceed. Route B is correctly excluded. The IDX-01 and IDX-RUN rehearsal (§3) shows the registration and the regenerated Index validate under the §8.3 rule. The choice between A and C and any clarification of §0.7 are the Product Owner's and are not decided here. Unreviewed fields: none for the Plan's treatment; the canon disposition itself remains unreviewed |

A proposal here is not approval. Decided entries are preserved; unreviewed fields stay unreviewed.

## Canon relied on

As listed in the QA_REPORT v1.0 "Canon relied on" block, which maps each source to its decision topic. The sources used specifically for this RCA:

* Glow QA Guide §3.1.2: an RCA is required, including for an all-PASS run, and must not invent a failure.
* Plan Templates §9: the RCA blocks (failure or friction patterns, primary root cause, contributing factors, remediation loops, evidence hygiene).
* Change Process Guide §0.4.1.2: classification of anomalies and the PF doc-delta mapping.
* HDE Build Notes v13.9.5: addendum 2.6 and the addendum index, for CCR status.

## Nonclaims

This RCA explains the completed QA run. It is not a QA verdict beyond the Report's, acceptance, closure, a close pack, canon drainage, a CCR ruling, PF09 movement, Ops, deployment or release. It edits no file outside `docs/ephemeral/`. Merging it preserves the record and approves nothing (D21-C).
