---
artifact_type: REMEDIATION_REVIEW
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
decision: APPROVE_AS_CHANGED
approval_sentinel: "ASK OK."
reviewed_proposal: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md (HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.0; blob ee59f22c432aafcdce9126c3e436c5d350deedb8; sha256 d120223b8e9d5f51176228153a1debf8274f142cd780520cf7513c0a4d02b70d; landed by #707 as 2a8992f)
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001)
originating_stage: QA-10, NOT_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md)
immutable_bases: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md, INITIAL_APPROVE), with Plan delta 01 v1.1 (docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md, DELTA_APPROVE; HDE Build Notes addendum 2.19); Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md with Specification delta 01 (addendum 2.20). All unchanged
pf10_addendum: docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (numbered 2.23)
author_reviewed: Thoth, continuing remediation author (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
reviewer: Isis, continuing Lead Developer and integrated-remediation reviewer (this session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
prompt: ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b; page state of 2026-10-12T02:29:22Z, read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_head_read: origin/main 2a8992f
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (last addendum 2.22)
PR_RETURN_PHASE: not applicable (no existing PR execution phase is affected; delivery is a new work unit)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), WORK_UNIT_ID WU-REM-01
created_at: 2026-10-23T16:40:00Z
---

# HDE-CRD-0002 — Remediation review for FND-001 (S22), v1.0 (ESC-40)

## 1. Decision

**APPROVE_AS_CHANGED.** Thoth's proposal v1.0 is approved, with one change, C-1 (§3). The approved overlay is P-1 and P-2 as proposed, R-1 to R-3 and V-1 to V-5 as proposed, with C-1 applied to R-3 and V-3.
- **The approved base is unchanged.**
- **Addendum:** this qualifying approval creates one HDE Build Notes addendum, `docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md`.
- **Delivery:** a new work unit, WU-REM-01, through PR-10.

This review authorizes no implementation, Proceed, PR, merge, QA or closure.

## 2. Review

| Check | Result |
| :- | :- |
| Finding validated | Yes. The approved objective, expected behaviour, observed behaviour and real input match the QA-10 records |
| Cause | Proven. I read the three loci on `main` `2a8992f`: `tests/evidence/test_evidence_index_missing_state.py` L-1 (:977-984), L-2 `crd_repo` (:318-344, which strips only `CRD_ROOT = "audit/qa/hde-crd-0001"`) and L-3 `close_repo` (:1270-1275, `assert not (repo / CLOSE_ROOT).exists()` with `CLOSE_ROOT = "audit/qa/hde-crd-0002"`). The close-pack test's assumption (:1285-1315) is also confirmed by reading. Thoth's reproduction (2 failed, 4 errors with the root present; 134 passed without it) is consistent with these loci. I did not re-run it, because no tooling is installed in this session |
| Wider surface | Searched: every test naming `audit/qa/hde-crd-0002`, `hde_crd_0002` or the close-pack paths. Outside the target file, `tests/qa/test_generic_qa_harness.py` (:1435) and `tests/qa/test_generate_epic_close_pack.py` use tmp or synthetic repositories (Thoth ran both, 1,072 passed with the root present). No other affected test was found |
| Lanes | `classify_paths(['tests/evidence/test_evidence_index_missing_state.py'])`: evidence only, not a full-validation path. The QA evidence paths, the close-pack paths and the close-run path also select only the evidence lane (run read-only on `main`), so evidence-lane rehearsals V-2 and V-3 cover the CI those PRs will run |
| Scope and intent | Test-only. No Specification boundary or product intent changes; S22's intent already requires publication under the real root. Within remediation authority |
| Overlay | P-1 rewords how WU-PR-02 acceptance (5) is proven, prospectively. P-2 adds WU-REM-01. WU-PR-02 stays accepted-final |
| Material | Yes (IA-30's definition, as used for Plan deltas): it adds a planned work unit and changes an approved acceptance criterion. So it qualifies for an addendum |
| Business case | Beneficiary, evidence, benefit and measure are stated (addendum 2.11 rule 1, as narrowed by 2.18). It is not CI work for its own sake (rule 2): it unblocks QA evidence publication |
| Verification | V-1 to V-5 map onto the triage's required resolution evidence (1) to (3) |
| Delivery and return | PR-10 for WU-REM-01 (whole-change Implementation Agent), then the ordinary unit lineage; return to the same Isis QA-10 reassessment. `PR_RETURN_PHASE` is correctly not applicable |
| Conflicts | None new. CR-1 to CR-9 carried; CR-9 is unaffected |
| §12 numbering correction | Accepted as a factual note: PF10 v13.7.5 numbers the Specification delta 01 addendum 2.20 |

## 3. Change C-1

**The gap.** The close stage will also commit HDE-CRD-0002's close candidate source. The writer and the close-pack tests name its path as `CRD_SOURCE_REL = "audit/HDE-CRD-0002_close_candidate_source.json"` (`tests/qa/test_generate_epic_close_pack.py:4346`). R-3 and V-3 cover the close-run family and the two close-pack files, but not this file.

**C-1, applied to the overlay:**
- **R-3 additionally:** the copy also removes `audit/HDE-CRD-0002_close_candidate_source.json`, with its path proof and Index row if any.
- **V-3 additionally:** the rehearsal also places a stand-in candidate source at that path.

The rehearsal must pass with all three close-stage inputs present. The form of the stand-in is PR-20's. This review does not design it.

## 4. Approved overlay, complete

**Plan v1.1 overlays:**
- **P-1, Plan v1.1 §7 WU-PR-02, "Acceptance and verification" item (5), last clause.** "the absent real root publishes nothing" reads: "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source". WU-PR-02's accepted delivery is unchanged; the new proof is delivered by WU-REM-01.
- **P-2, Plan v1.1 §7, a new unit after WU-OPS-01 and before QA-10 readiness: WU-REM-01 — Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation).**
  - Purpose: let HDE-CRD-0002's QA evidence and close pack land without breaking the evidence lane (FND-001).
  - Bounded scope: S22, and S21's close-run tests; `tests/evidence/test_evidence_index_missing_state.py` only (R-1 to R-3).
  - Dependencies: none on unmerged work; it lands before QA-20.
  - Acceptance: V-1 to V-5.
  - Evidence obligations: the PR result record with the V-2 and V-3 rehearsal outputs; no governed evidence change.
  - Business case: as the proposal §5.4 states.
  - Nonclaims: no QA evidence for HDE-CRD-0002 is produced or committed.

**Required behaviour**, in `tests/evidence/test_evidence_index_missing_state.py`:
- **R-1.** Replace the real-checkout absence test with one that builds the absent state in a copy. It removes `audit/qa/hde-crd-0002/` and its Index rows, regenerates and runs `--check` through the canonical updater, then asserts no HDE-CRD-0002 row from `_load_crd_qa_entries([])` and none in the Index under the root. It does not read whether the real checkout holds the root.
- **R-2.** `crd_repo` builds the pre-first-publication state for every root in `ADMITTED_CRD_QA`: it removes each root and its Index rows, then regenerates and checks through the canonical updater. The existing assertions of `test_crd_0002_fixture_root_publishes_beside_crd_0001` stay.
- **R-3 (with C-1).** `close_repo` removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, from the copy, then regenerates and checks through the canonical updater. The four close-run tests keep their assertions.
- **Limit.** No other file changes. A shared helper, if any, stays in the same file.

**Verification:**
- **V-1, local on the PR head (root absent):** the 7 evidence-lane validators rc 0, and the six pytest files pass with no fewer than 134 tests.
- **V-2, rehearsal with a stand-in HDE-CRD-0002 QA family published by the harness and the canonical updater, in a throwaway clone:** the evidence lane and the release lane pass, exactly as `ci.yml` runs them.
- **V-3 (with C-1), rehearsal adding a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater:** the evidence lane passes.
- **V-4, negative control:** the R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy.
- **V-5, hosted CI on the PR head:** the evidence lane is green, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

Nothing from a rehearsal clone is committed.

## 5. Effects, exclusions, risks

- **Effects:** as the proposal §6 states.
  - S22 becomes achievable on the real root.
  - S21's close-run tests stop depending on the real checkout.
  - QA-10 reassessment, QA-20 and QA-50 wait on WU-REM-01.
- **Exclusions:** as the proposal §7 states.
  - No runtime, updater, harness or governed-evidence change; no new evidence family.
  - No HDE-CRD-0002 QA evidence produced.
  - No Specification change.
  - No re-run of an accepted-final PR.
- **Risks:** as the proposal §8 states. The added C-1 strip is bounded to one named file of the same change.

## 6. Unresolved items and owners

| Item | Owner |
| :- | :- |
| WU-REM-01's instruction | Whole-change Implementation Agent (PR-10) |
| WU-REM-01's code design | PR-20 in WU-REM-01's PR session |
| Proceed, merge | Product Owner |
| QA-10 reassessment of S22 and its dependants | Isis, after WU-REM-01's PR-40 ACCEPT |
| CR-9 | Isis, at its native boundary (IA-30); unaffected |
| FND-024 (PR35-C1 flake) | As recorded in the triage |
| Publication of the addendum into PF10 | Product Owner |

## 7. Canon-conflict register (carried)

CR-1 to CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (a) (Implementation Agent through RS-20); CR-7 and CR-8 APPROVED (a) (Product Owner); CR-9 PROPOSED, not yet reviewed (Isis, IA-30). No new conflict.

## 8. TypeSafe reading for the receiving session (PR-10, WU-REM-01)

Action sent (v8.2): "Write, as the whole-change Implementation Agent, one new self-contained pull-request work-unit instruction for a remediation work unit added to an approved CRD Implementation Plan by a just-approved remediation overlay: a test-only change to one evidence test file, in which six tests and two fixtures stop assuming the change's own QA evidence directory and close pack are absent, with five named verification checks including two rehearsals in a throwaway clone and a hosted evidence-lane run, carrying the unit's business case, its acceptance criteria and its repository baseline. It is a Markdown record only: no code is written and no live run occurs; a detailed PR plan, a Product Owner Proceed, implementation, CI and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.68 (confidence 0.61); rung probabilities low 0.05, medium 0.36, high 0.47, extra high 0.11, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.49, Sonnet 5.5 0.47, Haiku 5.5 0.02 (confidence 0.32). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.007, Fable 5.1 at high 0.009, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.025, Opus 5.5 at medium 0.176, Opus 5.5 at high 0.230, Opus 5.5 at extra high 0.054, Opus 5.5 at max 0.005, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.024, Sonnet 5.5 at medium 0.169, Sonnet 5.5 at high 0.221, Sonnet 5.5 at extra high 0.052, Sonnet 5.5 at max 0.005, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.007, Haiku 5.5 at high 0.009, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between medium and high; model near tie between Opus 5.5 and Sonnet 5.5. Sent 2026-10-23T16:32:36Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T16:32:36Z; HTTP 200 in 0.76 s; 5488 input and 71 output tokens; jev-1.13.0. Session kind "implementation". Rung by rule: high; model by rule: Opus 5.5.
- **Nathan's pick for PR-10:** not stated. **Nathan's pick for this ESC-40 session:** not stated (its reading is in the proposal §13).
- **Notion row:** not written.

**Surface advice:** run PR-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role (session "HDE-CRD-0002-2").
- **Reads from `main`:**
  - this review and the addendum record;
  - the proposal;
  - the QA-10 records;
  - Plan v1.1 with its review and Plan delta 01;
  - `docs/pfcanon/`, including current PF10;
  - for the baseline, `tests/evidence/test_evidence_index_missing_state.py` and `.github/workflows/ci.yml`.
- **Writes:** only the instruction under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this review's pull request is merged first.

## Canon relied on

Read on `main` at `2a8992f`.

| Decision topic | Governing sections |
| :- | :- |
| Review mode, decision values, addendum, routing | ESC-40 — Review and Return Approved Remediation — 100926.1, read in full: "Required inputs", "Execute" 1 to 5, "Qualifying addendum schema", "Required result", "Result routing" |
| Proposal intake and author lineage | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, read in full in this session |
| The failed objective | Specification v1.1-approved S22 row, Constraints "QA evidence admission", QA requirement; Plan v1.1 §7 WU-PR-02 |
| Materiality | IA-30 — Review Whole-Change Implementation Plan — 100926.1, "Material" (read in full in this session) |
| Business case, real inputs, no ceiling | PF10-HDE-Build-Notes v13.7.5 addendum 2.11 rules 1, 2 and 4, and addendum 2.18 (read in full in this session) |
| Accepted-final work not reopened; a lawful prospective PR owner | QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, "Rescope authorship…" (read in full in this session); PF10 addendum 2.5 (WU-PR-02 accepted) |
| Addendum number and format | PF10 v13.7.5 Addendum Index (last 2.22); PF06-Canon-Change-Process-Guide v2.5.4 §0.1A; PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" (read in full in this session) |
| Evidence writer rules | AGENTS.md "Governed evidence rules" (sole writer; no hand-editing) |
| Repository facts | `tests/evidence/test_evidence_index_missing_state.py` :15-30, :318-344, :977-1014, :1248-1320; `tests/qa/test_generate_epic_close_pack.py` :4346-4349; `tests/qa/test_generic_qa_harness.py` :1430-1440; `ci/checks/classify_ci_changes.py` classification run read-only |

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-ESC-40-20261023-FND-001-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| requirement / work unit | S22; WU-REM-01 |
| prompt | ESC-40 — Review and Return Approved Remediation — 100926.1, page state of 2026-10-12T02:29:22Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | continuing Isis, ESC-40 |
| capture time | 2026-10-23T16:40:00Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) |

ASK OK.
