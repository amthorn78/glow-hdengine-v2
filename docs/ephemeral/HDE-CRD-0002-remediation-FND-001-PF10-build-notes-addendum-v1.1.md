---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002/REMEDIATION-FND-001/PROPOSAL-V1.1/ESC-40-APPROVE
approved_delta_digest: sha256 2aa11d33e3b0cd0332aa0471584e3b0662dc5ab8f796bbf2c9c5fe6d7e07474f (the reviewed proposal v1.1's file bytes)
producing_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
approval_decision: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.1, APPROVE, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md
immutable_base: HDE-CRD-0002 Implementation Plan v1.1 (IA-30 review v1.1, INITIAL_APPROVE), docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 v1.1 (addendum 2.19)
applicable_prior_addenda: 2.5; 2.11; 2.16; 2.18; 2.19; 2.20; 2.23 (docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md)
approved_delta: P-1, amended P-2, R-1 to R-5 and V-1 to V-5, and CR-10's disposition, below
affected_surfaces: below, "Affected surfaces and consequences"
exclusions: below, "Exclusions and nonclaims"
conflicts: CR-10, APPROVED alternative (a), below
unresolved_items: below, "Unresolved obligations and owners"
return_phase: PR-10 — Create PR Work-Unit Instructions — 100926.1, WORK_UNIT_ID WU-REM-01, instruction v1.1; then the same Isis QA-10 reassessment
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (last addendum in the file 2.22), with addendum 2.23 issued; this addendum takes the next number
---

## 2.24 HDE-CRD-0002: the FND-001 remedy is amended — WU-REM-01 also makes the Mirror skeleton test and the QA harness accept crd_id, so HDE-CRD-0002's close pack leaves the evidence lane, the qa lane and Epic viability as they were

Timestamp: 102326 20:15 (UTC). Details: Records the ESC-40 approval of Thoth's remediation proposal v1.1 for the HDE-CRD-0002 QA-10 finding FND-001 (requirement S22). It amends the remedy addendum 2.23 recorded.

The planner of work unit WU-REM-01 found (F-1) that the approved one-file remedy could not meet its own acceptance. Diagnosis then found a second defect with the same cause (F-2). The two defects:
- **F-1.** Once HDE-CRD-0002's close pack is indexed, `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity` rejects the `crd_id` key the canonical updater writes on its two close-pack rows.
- **F-2.** The QA harness (`tools/qa/qa_harness.py`) rejects `crd_id` on Human Index and Machine Mirror rows. With the close pack indexed, four Epic acceptance-map viabilities (HDE-EPIC021, 027, 028, 029) turn from PASS to FAIL_TOOLING, and the qa-lane test `test_current_acceptance_inputs_are_strictly_viable` fails.

WU-REM-01 widens to three files: R-4 and R-5 add `crd_id` to the allowed optional keys of those two validators. The rest of the 2.23 remedy stands.

### Source and approval

* Producing prompt: ESC-40 — Review and Return Approved Remediation — 100926.1; release GCFPE-20261009.1 / 100926.1.
* Decision: APPROVE by Isis, the continuing HDE-CRD-0002 Lead Developer, recorded in docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md, 2026-10-23.
* Reviewed proposal: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md (Thoth, ESC-30; file SHA-256 2aa11d33e3b0cd0332aa0471584e3b0662dc5ab8f796bbf2c9c5fe6d7e07474f; [\#711](https://github.com/amthorn78/glow-hdengine-v2/pull/711)). Predecessor proposal v1.0 ([\#707](https://github.com/amthorn78/glow-hdengine-v2/pull/707)) and review v1.0 ([\#708](https://github.com/amthorn78/glow-hdengine-v2/pull/708)), recorded by addendum 2.23.
* Delivery-stage evidence: WU-REM-01 PR implementation plan v1.0 §12 and §16, BLOCKED on F-1 ([\#710](https://github.com/amthorn78/glow-hdengine-v2/pull/710)); instruction v1.0 ([\#709](https://github.com/amthorn78/glow-hdengine-v2/pull/709)) §14 routes a change to the remedy through ESC-30 and ESC-40.
* Immutable base: Implementation Plan v1.1 with Plan delta 01 v1.1. Not edited.

### Cause

* HDE Schemas and Artifacts §8.3, "Allowed top-level keys and unknown-key rejection", lists `crd_id` as an optional metadata key and requires that "every serializer or validator enforcing this allowed-key set MUST accept crd_id".
* The canonical updater and `ci/checks/check_mirror_schema.sh` accept it. The Mirror skeleton test and the QA harness do not.
* The updater writes `crd_id` only on CRD close-pack rows. So the defects appear when the close pack is indexed, not when the QA root alone exists.
* The close-pack pull request selects only the evidence and release lanes. F-2 would first fail on a later, unrelated qa-lane run.
* All of this was reproduced in throwaway clones of `main` with stand-in states produced only through the harness and the canonical updater.

### Approved remediation

* **P-1, unchanged from addendum 2.23:** Implementation Plan v1.1 §7 WU-PR-02, "Acceptance and verification" item (5), last clause, reads: "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source".
* **P-2, amended. WU-REM-01 — Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation):**
  * Purpose: let HDE-CRD-0002's QA evidence and close pack land without breaking the evidence lane, and keep the qa lane and existing Epic acceptance-map viability unaffected once the close pack is on `main`.
  * Bounded scope: S22, and S21's close-run tests and close-pack rows. Three files: `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py` and `tools/qa/qa_harness.py`.
  * Dependencies: none on unmerged work; it lands before QA-20.
  * Acceptance: V-1 to V-5.
  * Evidence obligations: the PR result record with the V-2 and V-3 rehearsal outputs, the V-3 viability comparison included; no governed-evidence change.
  * Nonclaims: no HDE-CRD-0002 QA evidence, close pack or close candidate source is produced or committed.
* **Required behaviour:**
  * R-1, unchanged: the absence test builds the absent state in a copy, through the canonical updater, and does not read the real checkout's state.
  * R-2, unchanged: `crd_repo` builds the pre-first-publication state for every root in `ADMITTED_CRD_QA`.
  * R-3 with C-1, unchanged: `close_repo` removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, from the copy, then regenerates and checks through the canonical updater.
  * R-4, new: `test_mirror_schema_and_parity` accepts `crd_id` as an optional top-level Mirror key. Nothing else in that file changes.
  * R-5, new: the harness's evidence-graph validation accepts `crd_id` as an optional key on Human Index and Machine Mirror rows. The required keys, the other metadata checks, the strict Epic predicates and the refusal of CRD viability are unchanged.
  * Limit: no file outside the three changes.
* **Verification:**
  * V-1: on the PR head, the seven evidence-lane validators exit 0; the six evidence-lane pytest files pass with no fewer than 134 tests; the qa lane's seven files pass with its two tree checks; and the classifier's changed-test targets pass in isolation, all as `ci.yml` runs them.
  * V-2: in a throwaway clone with a stand-in HDE-CRD-0002 QA family published by the harness and canonical updater, the evidence, qa and release lanes pass.
  * V-3: the same clone additionally holds a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater. (a) The evidence, qa and release lanes pass. (b) Each `docs/acceptance_map_epic0NN.json` gets the same `evaluate_acceptance_map_viability` status as in the V-2 state, and no result names `crd_id`.
  * V-4, unchanged: the R-1 test fails when an Index row under the root is planted in its copy.
  * V-5: on hosted CI on the PR head, every selected lane and the changed-test step are green, and the run ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
  * Nothing from a rehearsal clone is committed.
* **Business case:**
  * beneficiary: QA and the Product Owner; every later qa-lane pull request; users of the harness's Epic viability;
  * evidence: the reproductions above;
  * benefit: QA-20 and QA-50 can proceed, and the close pack leaves no lane or Epic viability failing;
  * measure (1): the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests;
  * measure (2): the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes, with no change to these three files. Neither measure is observable at WU-REM-01's PR-40; V-2 and V-3 are the proxy.
  * No cost ceiling.

### Conflict decided: CR-10

* **The conflict.** HDE Schemas and Artifacts §8.3 also asks every validator of the key set to "enforce the epic\_id/crd\_id mutual-exclusion rule". A row with both keys cannot reach the skeleton test or the harness: the sole writer refuses it, and `check_mirror_schema.sh` rejects it (`EPIC_CRD_EXCLUSIVE`) on every evidence-lane run.
* **Decision: APPROVED, alternative (a).** Addendum 2.11 rule 5, kept by addendum 2.18 rule 6, governs for this exact scope: such a row is an input outside the real set for these two validators, and it gets a stated limit, not a model.
  * The mutual-exclusion rule stays enforced by the canonical writer and the Machine Mirror schema check.
  * R-4 and R-5 accept `crd_id` only.
* **Drainage:** HDE Schemas and Artifacts §8.3, to state where the mutual-exclusion rule is enforced. Unperformed.

### Affected surfaces and consequences

* Requirements:
  * S22 becomes achievable on the real root.
  * S21's close-run tests stop depending on the real checkout, and its close-pack rows stop failing a validator.
  * S22's "existing Epic … inputs still publish and validate" is preserved once the close pack lands.
* Files: two test files and one QA tool. None is a release member; release identity is unchanged.
* CI: WU-REM-01's pull request runs the evidence and qa lanes and the changed-test step.
* Ops and documentation: none.
* Order: WU-REM-01 is delivered and accepted before the HDE-CRD-0002 QA-10 reassessment, and QA-20 waits on that reassessment.
* This addendum supersedes addendum 2.23's WU-REM-01 scope, limit, exclusions, verification and business case. 2.23's P-1 and R-1 to R-3 with C-1 stand unchanged.

### Exclusions and nonclaims

* No updater or runtime change, and no harness change beyond R-5.
* No regeneration or hand edit of governed evidence, and no new evidence family.
* No Specification change.
* No reopening of WU-PR-02 or WU-PR-07, and no re-run of an accepted-final pull request.
* The 12 Epic acceptance maps that already fail viability on `main`, for reasons unrelated to `crd_id`, are not repaired.
* This approval is not a PR Instruction, Proceed, merge, QA verdict, acceptance or closure, and it moves no PF09 or PF30 row.

### Unresolved obligations and owners

* WU-REM-01 instruction v1.1: the whole-change Implementation Agent. The successor PR plan: WU-REM-01's PR-20.
* The QA-10 reassessment of S22 and its dependants, after WU-REM-01 is accepted: Isis. It includes one observation: 9 local failures of `tests/evidence/test_hdapi_v2_contract_inventory.py` in the remediation author's environment, a file that hosted full-validation run 39699657729 passed.
* CR-10 drainage, and the 12 Epic viabilities already failing: the Product Owner.
* CR-9's disposition: Isis, at its native review boundary.

### Relationship to existing HDE Build Notes guidance

This addendum amends addendum 2.23 for WU-REM-01 within the scope stated above. It applies addendum 2.11 rule 5 to HDE Schemas and Artifacts §8.3's mutual-exclusion duty for two validators (CR-10). It leaves addenda 2.5 and 2.16, which accepted WU-PR-02 and WU-PR-07, standing.
