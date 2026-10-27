---
artifact_type: REMEDIATION_REVIEW
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001
artifact_version: "1.1"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
decision: APPROVE
approval_sentinel: "ASK OK."
reviewed_proposal: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md (HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.1; blob 12fcbb30585f2e560a4897cf7cf6955a92497e3c; sha256 2aa11d33e3b0cd0332aa0471584e3b0662dc5ab8f796bbf2c9c5fe6d7e07474f; landed by #711 as d524f00)
predecessor: docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md (APPROVE_AS_CHANGED with C-1 on proposal v1.0; #708). Kept unchanged as history
superseded_overlay: review v1.0 §4 and its addendum record docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23), for WU-REM-01's scope, limit, exclusions, verification and business case only; P-1 and R-1 to R-3 with C-1 are carried unchanged
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001)
delivery_stage_evidence: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0.md §12 and §16 (F-1; BLOCKED; #710)
immutable_bases: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (IA-30 review v1.1, INITIAL_APPROVE) with Plan delta 01 v1.1 (addendum 2.19); Specification v1.1-approved with Specification delta 01 (addendum 2.20). All unchanged
pf10_addendum: docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.1.md (numbered 2.24)
author_reviewed: Thoth (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
reviewer: Isis, continuing Lead Developer and integrated-remediation reviewer (this session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
prompt: ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b; read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_head_read: origin/main d524f00
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (last addendum in the file 2.22), with the 2.23 record treated as in PF10 (ESC-40, "From the turn after it is created the addendum is part of PF10")
PR_RETURN_PHASE: not applicable (WU-REM-01 has no Proceed and no pull request)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), WORK_UNIT_ID WU-REM-01, instruction v1.1
created_at: 2026-10-23T20:15:00Z
---

# HDE-CRD-0002 — Remediation review for FND-001 (S22), v1.1 (ESC-40)

## 1. Decision

**APPROVE.** Thoth's proposal v1.1 is approved as written, with CR-10 decided APPROVED, alternative (a) (§4).
- **The approved overlay** is proposal v1.1 §6:
  - P-1 unchanged;
  - P-2 amended to three files;
  - R-1 to R-3 with C-1 unchanged, and R-4 and R-5 new;
  - V-1 to V-5 as extended.
- **Supersession.** It supersedes, for WU-REM-01, the scope, limit, exclusion, verification and business-case parts of review v1.0 §4 and of addendum 2.23.
- **Addendum.** This qualifying approval creates one addendum: `docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.1.md` (2.24).
- **Next.** Delivery continues through PR-10, which re-issues the WU-REM-01 instruction as v1.1.

The approved bases are unchanged. This review authorizes no implementation, Proceed, PR, merge, QA or closure.

## 2. Review

| Check | Result |
| :- | :- |
| Route | Correct. Instruction v1.0 §14 sends a change to the approved remedy to ESC-30 and ESC-40, not RS-20. No Proceed or PR exists, so `PR_RETURN_PHASE` is not applicable |
| F-1 (delivery-stage evidence) | Confirmed by reading on `main` `d524f00`. `tests/evidence/test_evidence_skeleton.py:526-532`: `optional_fields` holds `epic_id`, `notes`, `record_type`, `schema_version` and `tokens`, with no `crd_id`; :539 asserts `key_set - (required_fields | optional_fields) == set()` over the real Mirror. The updater's `_crd_close_pack_entries` writes `"crd_id": crd_id` on the close-pack rows (`tools/evidence/update_evidence_index.py`, the block at :4056-4066). So once the close pack is indexed, the test fails. PR-20 reproduced it (plan v1.0 §12.3), and so did Thoth (§5.2) |
| F-2 | Confirmed by reading. `tools/qa/qa_harness.py:230-245`: `_MIRROR_OPTIONAL_FIELDS` and `_HUMAN_INDEX_OPTIONAL_FIELDS` both lack `crd_id`. Thoth's executed evidence: 4 Epic viabilities go from PASS to FAIL_TOOLING; `test_current_acceptance_inputs_are_strictly_viable` fails with the close stage; M3 restores all 16 statuses. I did not re-run it, because no tooling is installed in this session |
| Common cause and canon | HDE Schemas and Artifacts §8.3, "Allowed top-level keys and unknown-key rejection", read in full: `crd_id` is an allowed metadata key, and "every serializer or validator enforcing this allowed-key set MUST accept crd_id". `ci/checks/check_mirror_schema.sh` accepts it (:19) and refuses both keys together (`EPIC_CRD_EXCLUSIVE`, :106-107) |
| Real inputs | Yes: the close-pack rows are a planned deliverable, and the hosted runner runs both validators (addendum 2.11 rule 4(a), (b)) |
| Scope and authority | Within remediation. No Specification boundary or product intent changes: S22's intent already includes "existing Epic … inputs still publish and validate", and its Constraint already requires "preserves existing Epic and HDE-CRD-0001 inputs". Neither `tools/qa/qa_harness.py` nor `tests/evidence/test_evidence_skeleton.py` is a release member (0 hits in `catalog/manifest.json`) |
| Size | R-4: one key added to one test's set. R-5: one key added to two harness sets. Rehearsed diff 29 lines (§6.2) |
| Alternatives | Option (a) is the smallest that closes both defects before QA entry; (b) to (d) are rightly not taken (§10) |
| Verification | V-1 to V-5 cover the triage's required resolution evidence (1) to (3) and add V-3 (b), the Epic viability comparison. Thoth's M1 to M3 rehearsals pass every lane (§5.5) |
| Business case | The beneficiary, evidence, benefit and measures are stated, and there is no ceiling (addendum 2.18). Measure (2) is correctly marked not observable at WU-REM-01's PR-40 |
| Correction to v1.0 (§4.4) | Accepted. The close stage is now executed, not only read |
| Materiality | Material: it changes an approved work unit's scope, limit and acceptance. So it qualifies for an addendum |

## 3. Observation on OBS-2 (not a remedy matter)

Thoth records that `tests/evidence/test_hdapi_v2_contract_inventory.py` failed 9 tests in his clone in both states and says "No CI lane runs the file". The second clause is not exact.
- **It is a full-validation target.** `_full_validation_test_targets()` includes it (read-only check on `d524f00`).
- **Hosted CI ran it green.** Hosted run 39699657729 on `1a4c8ab` was a full-validation run: its changed-test step selected the full-validation targets and passed "4521 passed, 2 skipped" (QA-10 Reality Audit E-003). The code at `d524f00` is identical outside `docs/ephemeral/`.
- **So the 9 failures are local to that environment.** Their cause is not established.

This is a real observation for the QA-10 reassessment and the Product Owner's triage. It does not affect this remedy or S03's coverage finding.

## 4. CR-10 decision

| Field | Value |
| :- | :- |
| ID | CR-10 |
| Status | **APPROVED, alternative (a)** |
| Reviewer and session | Isis, ESC-40, this session |
| Reviewed artifact | Proposal v1.1 §13 |
| Decision time | 2026-10-23T20:15:00Z |
| Rationale | Addendum 2.11 rule 5 ("An input constructed only to exercise code justifies no requirement, design element, test, fix or blocking finding. An input outside the real set gets one refusal or a stated limit, never a model of it"), kept by addendum 2.18 rule 6, governs over HDE Schemas and Artifacts §8.3 for this exact scope, by 2.11's own supersession clause and PF10 precedence. A row with both `epic_id` and `crd_id` cannot reach the skeleton test or the harness: the sole writer refuses it (`test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together`), and `check_mirror_schema.sh` rejects it (`EPIC_CRD_EXCLUSIVE`) on every evidence-lane run. The mutual-exclusion rule is enforced where such a row could arise; R-4 and R-5 accept `crd_id` only, with that stated limit |
| Scope of the decision | These two validators only. The writer and the Mirror schema check keep the mutual-exclusion rule |
| Drainage | HDE Schemas and Artifacts §8.3: the Product Owner, by a later addendum or permanent canon revision. Unperformed |

## 5. Approved overlay

Proposal v1.1 §6 is approved verbatim, so it is not restated here. The addendum record reproduces it in full. In summary:
- **P-1 and P-2:** P-1 unchanged; P-2 amended to three files: `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py` and `tools/qa/qa_harness.py`.
- **R-1 to R-5:** R-1 to R-3 with C-1 unchanged; R-4 and R-5 new.
- **The limit:** no file outside the three changes.
- **V-1 to V-5:** as §6.4 states them, including V-3 (b).
- **The business case:** as §6.5 states it.

## 6. Effects, exclusions, risks

The effects are as proposal §7 states them.
- WU-REM-01's PR selects the evidence and qa lanes and the changed-test step (`tests/qa/test_qa_tool_ownership.py`).
- QA-10 reassessment, QA-20 and QA-50 wait on WU-REM-01.

The exclusions are as proposal §8 states them.
- The harness change is R-5 only.
- No updater, runtime or governed-evidence change.
- No HDE-CRD-0002 QA evidence, close pack or candidate source is produced.
- The 12 Epic maps already failing viability are not repaired (OBS-1).

The risks are as proposal §9 states them.

## 7. Unresolved items and owners

| Item | Owner |
| :- | :- |
| WU-REM-01 instruction v1.1 | Whole-change Implementation Agent (PR-10) |
| Successor PR plan, code design | PR-20 in the WU-REM-01 PR session (https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5) |
| Proceed, merge | Product Owner |
| QA-10 reassessment of S22 and dependants, including OBS-2 (§3) | Isis, after WU-REM-01's PR-40 ACCEPT |
| CR-10 drainage into HDE Schemas and Artifacts §8.3 | Product Owner |
| CR-9 | Isis (IA-30); unaffected |
| OBS-1 (12 Epic maps failing viability on `main`) | Product Owner, as a later-change candidate |
| FND-024 | As recorded in the triage |
| Publication of 2.23 and 2.24 into PF10 | Product Owner |

## 8. Canon-conflict register

| ID | Status |
| :- | :- |
| CR-1 to CR-3 | APPROVED_AS_CHANGED (Thoth) |
| CR-4 | APPROVED (Product Owner) |
| CR-5 | APPROVED_AS_CHANGED (Product Owner) |
| CR-6 | APPROVED (a) (Implementation Agent through RS-20) |
| CR-7, CR-8 | APPROVED (a) (Product Owner) |
| CR-9 | PROPOSED, not yet reviewed (Isis, IA-30) |
| CR-10 | **APPROVED (a)** (Isis, ESC-40, this review §4) |

## 9. TypeSafe reading for the receiving session (PR-10, WU-REM-01 instruction v1.1)

Action sent (v8.2): "Revise, as the whole-change Implementation Agent, an already issued pull-request work-unit instruction for a remediation work unit whose approved remedy has just been amended: re-issue it as a new version that widens the unit from one evidence test file to three files (two test files and the QA harness's index-row key validation), carries the amended required behaviours, the extended verification checks across the evidence, qa and release lanes, the updated business case and one approved canon-conflict disposition, and keeps the unchanged parts. It is a Markdown record only: no code is written and no live run occurs; a successor pull-request plan, a Product Owner Proceed, implementation, CI and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.27 (confidence 0.64); rung probabilities low 0.01, medium 0.12, high 0.48, extra high 0.38, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.71, Sonnet 5.5 0.27, Haiku 5.5 0.01 (confidence 0.61). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.004, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.007, Opus 5.5 at medium 0.085, Opus 5.5 at high 0.341, Opus 5.5 at extra high 0.270, Opus 5.5 at max 0.007, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.003, Sonnet 5.5 at medium 0.032, Sonnet 5.5 at high 0.130, Sonnet 5.5 at extra high 0.103, Sonnet 5.5 at max 0.003, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.001, Haiku 5.5 at high 0.005, Haiku 5.5 at extra high 0.004, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and high. Sent 2026-10-23T20:08:33Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T20:08:33Z; HTTP 200 in 0.56 s; 5482 input and 71 output tokens; jev-1.13.0. Session kind "correction". Rung by rule: high; model by rule: Opus 5.5. Flags: boundary between extra high and high.
- **Nathan's pick for PR-10:** not stated. **Nathan's pick for this ESC-40 session:** not stated (its reading is in the proposal v1.1 §15).
- **Notion row:** not written.

**Surface advice:** run PR-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role (session "HDE-CRD-0002-2").
- **Reads from `main`:**
  - this review, the 2.24 record, proposal v1.1, instruction v1.0 and PR-20 plan v1.0;
  - Plan v1.1 with its review and Plan delta 01;
  - `docs/pfcanon/`, including current PF10 and HDE Schemas and Artifacts §8.3;
  - for the baseline, the three named files and `.github/workflows/ci.yml`.
- **Writes:** only instruction v1.1 under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this review's pull request is merged first.

## Canon relied on

Read on `main` at `d524f00`.

| Decision topic | Governing sections |
| :- | :- |
| Review mode, decisions, addendum, successor handling, routing | ESC-40 — Review and Return Approved Remediation — 100926.1, read in full: "Required inputs", "Execute" 1 to 5, "Qualifying addendum schema", "Required result", "Result routing", "Carried conflict and decision lineage" (Isis decides the integrated remediation review) |
| The Index and Mirror key set; F-1, F-2 and CR-10 | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.3, "Allowed top-level keys and unknown-key rejection", read in full |
| CR-10's governing rule | PF10-HDE-Build-Notes v13.7.5 addendum 2.11 rules 4 and 5 and "Scope and supersession" (read in full in this session); addendum 2.18 rule 6 |
| Harness legacy Epic viability preserved | PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3, as the proposal quotes it ("Preserve the existing Epic logic and strict predicates"); R-5 changes no predicate |
| The objective | Specification v1.1-approved S22 row and Constraints "QA evidence admission" (read in full for QA-10) |
| Route for a remedy change | WU-REM-01 instruction v1.0 §14 (read at that section) |
| Addendum number and format | PF10 v13.7.5 Addendum Index (2.1 to 2.22), with 2.23 issued; PF06-Canon-Change-Process-Guide v2.5.4 §0.1A; PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" |
| Repository facts | `tests/evidence/test_evidence_skeleton.py:520-540`; `tools/qa/qa_harness.py:224-245`; `tools/evidence/update_evidence_index.py:4040-4070`; `ci/checks/check_mirror_schema.sh:19, 106-107`; `catalog/manifest.json` (no hit for either file); `ci/checks/classify_ci_changes.py` `_full_validation_test_targets()` (OBS-2) |

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-ESC-40-20261023-FND-001-02 |
| change | CRD HDE-CRD-0002 |
| requirement / work unit | S22 (with S21's close-run tests and close-pack rows); WU-REM-01 |
| prompt | ESC-40 — Review and Return Approved Remediation — 100926.1 |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | continuing Isis, ESC-40 (second review for FND-001) |
| capture time | 2026-10-23T20:15:00Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok |
| repository persistence | PENDING / NON_GATING |

ASK OK.
