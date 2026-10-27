---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002/REMEDIATION-FND-001/PROPOSAL-V1.0/ESC-40-APPROVE_AS_CHANGED
approved_delta_digest: sha256 d120223b8e9d5f51176228153a1debf8274f142cd780520cf7513c0a4d02b70d (the reviewed proposal's file bytes) plus change C-1 of the review
producing_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
approval_decision: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.0, APPROVE_AS_CHANGED, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md
immutable_base: HDE-CRD-0002 Implementation Plan v1.1, approved by IA-30 review v1.1 (INITIAL_APPROVE), docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 v1.1 (addendum 2.19)
applicable_prior_addenda: 2.5 (WU-PR-02 accepted); 2.11 and 2.18 (business case, real inputs, no ceiling); 2.19 (Plan delta 01); 2.20 (Specification delta 01)
approved_delta: P-1, P-2, R-1 to R-3 and V-1 to V-5 with C-1, reproduced below under "Approved remediation"
affected_surfaces: below, "Affected surfaces and consequences"
exclusions: below, "Exclusions and nonclaims"
conflicts: NONE
unresolved_items: below, "Unresolved obligations and owners"
return_phase: PR-10 — Create PR Work-Unit Instructions — 100926.1, WORK_UNIT_ID WU-REM-01; then the same Isis QA-10 reassessment
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (last addendum 2.22; this addendum takes the next number)
---

## 2.23 HDE-CRD-0002: remediation of QA-10 finding FND-001 is approved as changed — the evidence-lane tests stop assuming the change's own QA root and close pack are absent, through new work unit WU-REM-01

Timestamp: 102326 16:40 (UTC). Details: Records the ESC-40 approval, with one change, of Thoth's remediation proposal v1.0 for the HDE-CRD-0002 QA-10 finding FND-001.
- **The finding.** Requirement S22's QA evidence admission is not achievable on the real repository, because six tests in `tests/evidence/test_evidence_index_missing_state.py`, which the evidence lane runs, assume that `audit/qa/hde-crd-0002/` and the change's close pack are absent. Publishing HDE-CRD-0002's QA evidence would fail that lane.
- **The remedy.** It is test-only and delivered by a new work unit, WU-REM-01. One Plan acceptance clause is restated.
- **What is unchanged.** The approved Plan v1.1 and the Specification. WU-PR-02 stays accepted-final.

### Source and approval

* Producing prompt: ESC-40 — Review and Return Approved Remediation — 100926.1, release GCFPE-20261009.1 / 100926.1.
* Decision: APPROVE\_AS\_CHANGED by Isis, the continuing HDE-CRD-0002 Lead Developer, recorded in docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md, 2026-10-23.
* Reviewed proposal: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md (Thoth, ESC-30; file SHA-256 d120223b8e9d5f51176228153a1debf8274f142cd780520cf7513c0a4d02b70d; landed by [\#707](https://github.com/amthorn78/glow-hdengine-v2/pull/707)).
* Originating finding: QA-10 readiness v1.0, NOT\_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md); triage §3 FND-001 (docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md; [\#706](https://github.com/amthorn78/glow-hdengine-v2/pull/706)).
* Immutable base: Implementation Plan v1.1 (IA-30 review v1.1, INITIAL\_APPROVE), with Plan delta 01 v1.1 (addendum 2.19). The base file is not edited.

### Cause

* **The three loci,** all in `tests/evidence/test_evidence_index_missing_state.py`:
  * `test_absent_admitted_crd_root_publishes_nothing` asserts that the real checkout holds no `audit/qa/hde-crd-0002/`, no loader row and no Index row.
  * The `crd_repo` fixture strips only `audit/qa/hde-crd-0001`, so `test_crd_0002_fixture_root_publishes_beside_crd_0001` sees real HDE-CRD-0002 checks.
  * The `close_repo` fixture asserts that the real checkout holds no `audit/qa/hde-crd-0002`. The close-pack test it serves also assumes the real close pack is absent.
* **Why the test exists.** WU-PR-02 delivered it to satisfy Plan v1.1 acceptance (5), "the absent real root publishes nothing", which held at delivery.
* **Reproduction.** In a throwaway clone of `main` `7d5a5aa` with a stand-in HDE-CRD-0002 family published by the canonical updater:
  * the evidence-lane pytest files gave 2 failed and 4 errors, against 134 passed without the root;
  * the seven evidence validators, the QA test files and the release lane stayed green.
* **What is not at fault.** The updater, the harness and the release lane work with the root present.

### Approved remediation

* **P-1, Implementation Plan v1.1 §7 WU-PR-02, "Acceptance and verification" item (5), last clause.** "the absent real root publishes nothing" reads: "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source". WU-PR-02's accepted delivery is unchanged; the new proof is delivered by WU-REM-01.
* **P-2, a new work unit in Plan v1.1 §7, after WU-OPS-01 and before QA-10 readiness: WU-REM-01 — Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation).**
  * Purpose: let HDE-CRD-0002's QA evidence and close pack land without breaking the evidence lane.
  * Bounded scope: S22, and S21's close-run tests; `tests/evidence/test_evidence_index_missing_state.py` only.
  * Dependencies: none on unmerged work; it lands before QA-20.
  * Acceptance: V-1 to V-5.
  * Evidence obligations: the PR result record with the V-2 and V-3 rehearsal outputs; no governed evidence change.
  * Business case:
    * beneficiary: QA and the Product Owner;
    * evidence: the reproduction above;
    * benefit: QA-20 and QA-50 can proceed, and the first QA evidence and close-pack pull requests are not blocked by the evidence lane;
    * measure: the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests.
  * Nonclaims: no HDE-CRD-0002 QA evidence is produced or committed.
* **Required behaviour in that file:**
  * R-1: the absence test builds the absent state in a copy, removing the root and its Index rows and regenerating and checking through the canonical updater. It then asserts no loader row and no Index row under the root. It does not read the real checkout's state.
  * R-2: `crd_repo` builds the pre-first-publication state for every root in `ADMITTED_CRD_QA`, and the existing assertions stay.
  * R-3: `close_repo` removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, then regenerates and checks through the canonical updater. The four close-run tests keep their assertions.
  * No other file changes.
* **Verification:**
  * V-1: on the PR head, the seven evidence-lane validators exit 0, and the six evidence-lane pytest files pass with no fewer than 134 tests.
  * V-2: in a throwaway clone with a stand-in HDE-CRD-0002 QA family published through the harness and canonical updater, the evidence and release lanes pass as `ci.yml` runs them.
  * V-3: the same clone additionally holds a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater; the evidence lane passes.
  * V-4: the R-1 test fails when an Index row under the root is planted in its copy.
  * V-5: hosted CI on the PR head has the evidence lane green and ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
  * Nothing from a rehearsal clone is committed.
* **Change C-1 from the proposal:** the close candidate source (`audit/HDE-CRD-0002_close_candidate_source.json`, the path the close-pack tests name) is added to R-3 and V-3.

### Affected surfaces and consequences

* Requirements: S22 becomes achievable on the real root; S21's close-run tests stop depending on the real checkout. No other requirement is affected.
* Tests: one file. CI: the evidence lane only. Release identity, Ops and documentation: unchanged.
* Order: WU-REM-01 is delivered and accepted before the HDE-CRD-0002 QA-10 reassessment, and QA-20 waits on that reassessment.

### Exclusions and nonclaims

* No runtime, updater, harness or governed-evidence change.
* No new evidence family, no Specification change, and no re-run of an accepted-final pull request.
* This approval is not a PR Instruction, Proceed, merge, QA verdict, acceptance or closure, and it moves no PF09 or PF30 row.

### Conflicts

None. The canon-conflict register is unchanged: CR-1 to CR-8 are decided, and CR-9 is proposed and unaffected.

### Unresolved obligations and owners

* WU-REM-01's instruction: the whole-change Implementation Agent. Its code design: WU-REM-01's PR-20.
* The QA-10 reassessment of S22 and its dependants, after WU-REM-01 is accepted: Isis.
* CR-9's disposition: Isis, at its native review boundary.

### Relationship to existing HDE Build Notes guidance

This addendum restates, for HDE-CRD-0002, how acceptance (5) of WU-PR-02 is proven going forward. It adds one work unit to the Plan that addendum 2.19 amended. It leaves addendum 2.5's acceptance of WU-PR-02 standing and supersedes no addendum.
