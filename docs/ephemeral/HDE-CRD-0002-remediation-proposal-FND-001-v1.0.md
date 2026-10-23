---
artifact_type: REMEDIATION_PROPOSAL
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: REMEDIATION_PENDING
approval_sentinel: "ASK OK?"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001; Reality Audit RA2-22; blob dac6d1a79de8)
originating_stage: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, NOT_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md §5; blob f6d7ff018ce7); producer Isis, session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok
requirement: S22 (QA evidence admission)
author: Thoth, Head of Development, continuing HDE-CRD-0002 remediation author (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum)
reviewer: Isis, continuing Lead Developer, ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
prompt: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
created_at: 2026-10-23T16:23:00Z
repository_head_read: origin/main 7d5a5aa (#706 merged)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (addenda 2.1 to 2.22; last addendum 2.22)
pf10_addendum: none (ESC-30 produces none)
prior_proposal: none (first proposal for FND-001)
next_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1
---

# HDE-CRD-0002 — Remediation proposal for FND-001 (S22), v1.0

## 1. Result

**REMEDIATION_PENDING.** FND-001 is validated and its cause is proven by reproduction. The failure surface is wider than the finding recorded: **six** evidence-lane tests break once a real HDE-CRD-0002 QA root exists, not one. All six are in `tests/evidence/test_evidence_index_missing_state.py`, and all share one cause: the tests assume the real checkout holds no HDE-CRD-0002 QA root, and later no HDE-CRD-0002 close pack.

The remedy is **test-only**:
- it changes no runtime code, updater code, governed evidence, release member, canon or Specification;
- it restates how one Plan acceptance criterion is proven;
- it is delivered as one new pull-request work unit, `WU-REM-01`, by the whole-change Implementation Agent through PR-10.

WU-PR-02 stays accepted-final and is not reopened.

This proposal approves nothing and creates no addendum, work vehicle or Proceed. It awaits Isis's ESC-40 decision (`ASK OK?`).

## 2. Finding validation

| Field | Validated value |
| :- | :- |
| Approved objective | Specification v1.1 S22, acceptance intent: "Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate". Constraints, "QA evidence admission". QA requirement: "published by the canonical updater once S22 holds". Plan v1.1 §7 WU-PR-02 Purpose. Unchanged by Specification delta 01 and Plan delta 01 |
| Expected | Publishing HDE-CRD-0002 QA evidence under the real root leaves a state that the repository's CI lanes accept |
| Observed (QA-10) | `test_absent_admitted_crd_root_publishes_nothing` asserts the real root is absent (E-328), and the evidence lane runs it (E-005) |
| Observed (this diagnosis, §4) | With a real-shaped root published by the canonical updater, six tests break: 2 FAILED and 4 ERROR at fixture setup. The seven evidence validators, the two QA test files and the whole release lane stay green |
| Attempt history | No remediation attempt. WU-PR-02 delivered the test as Plan acceptance (5) ("the absent real root publishes nothing"), which held at delivery and was accepted (lineage review v2.0; HDE Build Notes addendum 2.5) |
| Real input | Yes: this change's own QA evidence, an approved planned deliverable (HDE Build Notes addendum 2.11 rule 4(a)), and the hosted CI runner that will run the lane (rule 4(b)) |
| Return owner | Isis, QA-10 reassessment of S22 and its dependants (readiness §5, "Return condition") |

## 3. Diagnosis

### 3.1 Proven cause

Three test loci assume the real checkout holds no HDE-CRD-0002 root:

| # | Locus (`tests/evidence/test_evidence_index_missing_state.py` on `main` 7d5a5aa) | What it assumes | Observed with the root present |
| :- | :- | :- | :- |
| L-1 | `test_absent_admitted_crd_root_publishes_nothing` (lines 977–984) | On the **real checkout**: `audit/qa/hde-crd-0002/` absent; `_load_crd_qa_entries([])` yields no HDE-CRD-0002 row; `docs/evidence/INDEX.json` has no row under it | FAILED at line 980: `assert not True` |
| L-2 | Fixture `crd_repo` (lines 318–344), used by `test_crd_0002_fixture_root_publishes_beside_crd_0001` (lines 990–1014) | The fixture copies the real checkout and constructs a pre-first-publication state by removing only `CRD_ROOT` (`audit/qa/hde-crd-0001`, line 28) and its Index rows. The test then requires the HDE-CRD-0002 family to hold exactly `qa_step_logs_manifest.json` and `checks/current/primary.log` | FAILED at line 1001: the exact-set comparison sees the copied real checks beside `current` |
| L-3 | Fixture `close_repo` (lines 1270–1275), used by four close-run tests (lines 1285, 1317, 1350, 1377) | `assert not (repo / CLOSE_ROOT).exists()` with `CLOSE_ROOT = "audit/qa/hde-crd-0002"` (line 1250) on the copy of the real checkout. The tests also assume a first publication, for example "CRD record is missing" before any publish, and `set(manifest) == {"current"}` | ERROR at setup in all four tests, line 1274 |

A fourth assumption sits in the same fixture: `test_crd_close_pack_rows_are_absent_tolerant` (lines 1285–1315) assumes the real close pack (`audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json`) is absent and unindexed (line 1290), and then writes stand-in files at those paths (line 1293). This is **proven by reading, not executed**. The setup error at L-3 masks it, and HDE-CRD-0002's close pack does not exist yet. It would break the evidence lane on the pull request that lands this change's close pack, which is the same defect class one stage later.

### 3.2 Not the cause, proven

- **The updater and harness.** `publish_crd_check_family` published a two-check HDE-CRD-0002 family under the real root and regenerated the whole governed skeleton (Index, Mirror, sentinels, path proofs, orientation). `qa.validate_crd_check_family` accepted it, and all seven evidence-lane validators exited 0 on the resulting state. S22's admission works on the real root.
- **The release lane.** It is green with the root present: manifest check, 79 release tests, attestation build and verify, and a clean tree.
- **The QA test files.** `tests/qa/test_generic_qa_harness.py` and `tests/qa/test_generate_epic_close_pack.py` pass 1,072 of 1,072 with the root present. The close-pack test file builds its own synthetic repository (`_init_v2_repo(tmp_path, …)`).

### 3.3 Hypotheses still open

None that bears on the remedy. The close-pack assumption in §3.1 is a reading, and the remedy's verification V-3 executes it.

## 4. Reproduction evidence

All runs were in a throwaway clone of `main` at `7d5a5aa`, under `/tmp/claude-0/-home-user-glow-hdengine-v2/6f0d7b39-d09c-5539-b3ea-d705c7417465/scratchpad/esc30/clone`. The clone was never pushed.
- **Interpreter and install:** Python 3.12.3 venv with CI's install (`pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; pytest 8.4.2).
- **Rails:** closed (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`; `APP_ENV`, `ENGINE_ENV`, vendor and database variables unset).
- **Commands:** exactly those of `.github/workflows/ci.yml`, "Run governed evidence integrity lane" and "Build and verify exact-source release attestation".

| Run | State | Evidence-lane validators (7) | Evidence-lane pytest (6 files) | QA files (2) | Release lane |
| :- | :- | :- | :- | :- | :- |
| Baseline | `7d5a5aa` unmodified | all rc 0 | **134 passed** (827.7 s) | 1,072 passed (147.7 s) | Not run; hosted CI proved it on code-identical `1a4c8ab` (readiness §2, E-003/E-004) |
| Root present | `7d5a5aa` + one local commit `7d8469a` holding a stand-in HDE-CRD-0002 family (checks `qa-01-standin`, `qa-02-standin`) published through `qa.HarnessConfig(crd_id="HDE-CRD-0002")` and `writer.publish_crd_check_family`, then validated | all rc 0 | **2 failed, 128 passed, 4 errors** (803.2 s) | 1,072 passed (133.8 s) | rc 0 throughout: manifest check; 79 release tests; worktree clean; build; verify; tree clean |

The stand-in family is not QA evidence. Its command is `python -c "raise SystemExit(0)"`, and its provenance reads "ESC-30 stand-in in a throwaway clone; not QA evidence". Nothing from the clone enters the repository.

## 5. Proposed bounded remediation

### 5.1 Overlay on the immutable Implementation Plan v1.1

| # | Plan v1.1 anchor | Base text | Proposed overlay |
| :- | :- | :- | :- |
| P-1 | §7 WU-PR-02, "Acceptance and verification" item (5), last clause | "the absent real root publishes nothing" | "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family or its close pack". WU-PR-02's accepted delivery is unchanged; the new proof is delivered by WU-REM-01 |
| P-2 | §7, new work unit after WU-OPS-01 and before QA-10 readiness | — | **WU-REM-01 — Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation).** Purpose: let HDE-CRD-0002's QA evidence and close pack land without breaking the evidence lane (FND-001). Bounded scope: S22, and S21's close-run tests; `tests/evidence/test_evidence_index_missing_state.py` only (R-1 to R-3 below). Dependencies: none on unmerged work; it lands before QA-20. Acceptance: V-1 to V-5 below. Evidence obligations: PR result record with the V-2 and V-3 rehearsal outputs; no governed evidence change. Nonclaims: no QA evidence for HDE-CRD-0002 is produced or committed |

The Specification is unchanged: S22's acceptance intent already requires publication under the real root, and the remedy makes it achievable.

### 5.2 Required repair (behaviour, not code; PR-20 designs the code)

| # | Locus | Required behaviour |
| :- | :- | :- |
| R-1 | L-1 | Replace the real-checkout absence test with one that builds the absent state in a copy: remove `audit/qa/hde-crd-0002/` and its Index rows from the copy, regenerate and `--check` through the canonical updater, then assert that `_load_crd_qa_entries([])` yields no HDE-CRD-0002 row and that the Index holds none under the root. The test must not read whether the real checkout holds the root |
| R-2 | L-2 | `crd_repo` builds the pre-first-publication state for every root in `ADMITTED_CRD_QA` (today HDE-CRD-0001 and HDE-CRD-0002), not only `CRD_ROOT`. It removes each root and its Index rows from the copy, then regenerates and checks through the canonical updater as it does now. The existing assertions of `test_crd_0002_fixture_root_publishes_beside_crd_0001` stay as written |
| R-3 | L-3 and the close-pack assumption | `close_repo` builds HDE-CRD-0002's absent state in the copy: it removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md` and `audit/HDE-CRD-0002_MANIFEST.json`, their path proofs and their Index rows, then regenerates and checks through the canonical updater. The four close-run tests keep their assertions; the fixture's absence assertion then holds on the copy |

No other file changes. If R-1 to R-3 need a shared helper, it lives in the same test file.

### 5.3 Verification

| # | Check | Pass condition |
| :- | :- | :- |
| V-1 | Local, on the PR head (root absent) | The evidence-lane commands of `ci.yml` pass: 7 validators rc 0, and the six pytest files pass with no fewer tests than the baseline's 134 |
| V-2 | Rehearsal, root present | In a throwaway clone of the PR head, publish a stand-in HDE-CRD-0002 QA family through the harness and canonical updater (method of §4), commit locally, and run the evidence lane and the release lane exactly as `ci.yml` does: both pass. Recorded in the PR result; nothing from the clone is committed |
| V-3 | Rehearsal, close stage | In the same kind of clone, additionally publish a stand-in close-run family (`writer.publish_crd_close_run_family`) and stand-in close-pack files at the two `CLOSE_PACK` paths, indexed by the canonical updater. The evidence lane passes |
| V-4 | Property kept (negative control) | The R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy, so it still detects an absent root that publishes something |
| V-5 | Hosted CI on the PR head | The evidence lane is green and the run ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The change selects only the evidence lane (`classify_paths(['tests/evidence/test_evidence_index_missing_state.py'])` returns `evidence: True` and all other lanes false, run read-only for this proposal) |

These cover the triage's required resolution evidence: (1) by R-1 to R-3 on `main` after merge, (2) by V-5, and (3) by V-2 and V-3.

### 5.4 Business case (HDE Build Notes addendum 2.11 rule 1, as amended by addendum 2.18)

| Field | Content |
| :- | :- |
| Beneficiary | QA (Kronos) and the Product Owner: HDE-CRD-0002's QA evidence and later its close pack can be published through ordinary CI |
| Evidence | §4: with a real-shaped root present, six evidence-lane tests break; QA-10 is NOT_READY on S22 for this reason |
| Benefit | QA-20 and QA-50 can proceed; the first QA evidence pull request and the close-pack pull request are not blocked by the evidence lane |
| Measure | The first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests (checked at that PR's PR-40 or by QA-10 reassessment) |

## 6. Affected surfaces

| Area | Effect |
| :- | :- |
| Requirements | S22: becomes achievable on the real root. S21: its close-run tests stop depending on the real checkout. No other requirement is affected |
| Dependencies | QA-10 reassessment; QA-20 Guide and QA-50 publication (all wait on WU-REM-01); the close-pack pull request at closure |
| Tests | `tests/evidence/test_evidence_index_missing_state.py` only |
| Ops | None |
| Documentation | None. The WU-PR-02 records stay as historical; the P-1 overlay is carried by the ESC-40 addendum |
| CI | Evidence lane only on WU-REM-01's PR |
| Release identity | Unchanged; no release member is touched |

## 7. Preserved bases, overlays and exclusions

- **Preserved unchanged:**
  - Specification v1.1-approved with Specification delta 01 (HDE Build Notes addendum 2.20);
  - Implementation Plan v1.1 and its review v1.1, with Plan delta 01 v1.1 (addendum 2.19);
  - the Implementation Audit v1.0;
  - every accepted work unit, WU-PR-02 included (accepted-final; addendum 2.5).
- **Overlays applied:** P-1 and P-2 only, if approved.
- **Exclusions:**
  - no change to `tools/evidence/update_evidence_index.py`, `tools/qa/qa_harness.py` or any runtime file;
  - no regeneration of governed evidence (Index, Mirror, sentinels, path proofs, orientation);
  - no new evidence family;
  - no QA evidence for HDE-CRD-0002 is produced or committed;
  - no Specification boundary or product intent change;
  - no re-run of an accepted-final pull request.
- **Not in scope:** FND-024 (the PR35-C1 flake risk on QA evidence pull requests) stays with its recorded owner.

## 8. Risks

| Risk | Treatment |
| :- | :- |
| The fixture strips more than intended and hides a real regression | R-2 and R-3 strip only admitted CRD roots, the HDE-CRD-0002 close pack and their rows, then run the canonical updater's generate and `--check` on the copy. V-4 keeps the absent-root property detectable |
| Lane time grows (the lane already takes about 14 minutes) | The fixtures already regenerate through the updater, so R-2 and R-3 add a copy-and-strip per fixture, not new runs. PR-20 records the lane time against the 827.7 s baseline |
| A later admitted CRD repeats the defect | R-2 iterates `ADMITTED_CRD_QA`, so a later admission is covered without editing the fixture |

## 9. Delivery and return map

1. **ESC-40**, Isis: APPROVE, APPROVE_AS_CHANGED or DENY. A qualifying approval writes one HDE Build Notes addendum recording P-1 and P-2.
2. **PR-10** — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), by the whole-change Implementation Agent, for `WORK_UNIT_ID: WU-REM-01`. It carries the immutable Plan v1.1, its original review, the same-Isis `REMEDIATION_REVIEW` and the addendum.
3. **Then the ordinary unit lineage:** PR-20 and Product Owner Proceed → PR-30 → PR-35 → Nathan's merge → PR-40 lineage review.
4. **Return:** the same Isis, QA-10 reassessment of S22 and its dependants, on accepted delivery.

`PR_RETURN_PHASE`: not applicable. No existing PR execution phase is affected, and the remedy is new implementation by a lawful prospective PR owner.

## 10. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The ESC-40 decision on this proposal | Isis |
| WU-REM-01's code design (helper shape and fixture order) | PR-20 in WU-REM-01's PR session |
| CR-9 (PROPOSED; WU-OPS-01 Plan-text conflict) is unaffected and stays at its next native review boundary | Isis (IA-30) |
| FND-024 flake risk on QA evidence PRs | As recorded in the triage |

## 11. Canon conflict register (carried)

- **Carried as the readiness record §6 states:**
  - CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED (Thoth);
  - CR-4: APPROVED (Product Owner);
  - CR-5: APPROVED_AS_CHANGED (Product Owner);
  - CR-6: APPROVED, alternative (a) (Implementation Agent through RS-20);
  - CR-7 and CR-8: APPROVED, alternative (a) each (Product Owner);
  - CR-9: PROPOSED, not yet reviewed (Isis at IA-30).
- **New conflict:** none. FND-001 is an implementation defect against an approved objective. The remedy changes no canon and no Specification text.

## 12. Correction to an earlier Thoth record

`docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` names its addendum "2.18". PF10 v13.7.5 publishes it as **2.20**, because 2.18 and 2.19 were assigned to the no-ceiling rule and Plan delta 01 before publication. The addendum's content is unchanged. This proposal and later records cite 2.20. The issued review is not edited.

## 13. TypeSafe reading for the receiving session (ESC-40)

Action sent (v8.2): "Review, as the independent integrated-remediation reviewer, one new bounded remediation proposal for a QA-readiness finding in an approved 21-requirement change: a test-only repair of one evidence test file in which six tests assume the change's own QA evidence directory is absent, with a reproduction already run in a throwaway clone; decide approve, approve as changed or deny, and on approval write one standalone build-notes addendum and route delivery to a new pull-request work unit. It is a read-only review of Markdown records against canon and the repository: no code is written and no live run occurs, and a pull-request work unit with its own reviews and a readiness reassessment follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.90 (confidence 0.80); rung probabilities low 0.00, medium 0.20, high 0.71, extra high 0.08, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.90, Sonnet 5.5 0.07, Haiku 5.5 0.01 (confidence 0.87). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.004, Fable 5.1 at high 0.014, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.180, Opus 5.5 at high 0.639, Opus 5.5 at extra high 0.072, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.014, Sonnet 5.5 at high 0.050, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.002, Haiku 5.5 at high 0.007, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: none. Sent 2026-10-23T16:22:57Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T16:22:57Z; HTTP 200 in 0.56 s; 5486 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Nathan's pick for ESC-40:** not stated.
- **Nathan's pick for this ESC-30 session:** not stated (reading recorded in the readiness record §8).
- **Notion row:** not written.

**Surface advice:** run ESC-40 in the continuing Isis session for HDE-CRD-0002, or a top-level Claude Code cloud session Nathan creates for that role, on `amthorn78/glow-hdengine-v2` with Notion read access.
- **Reads:** this proposal, the readiness record, the triage and the Reality Audit; the Specification and Plan with their deltas; the WU-PR-02 records; `tests/evidence/test_evidence_index_missing_state.py`; `.github/workflows/ci.yml`; `docs/pfcanon/`, including current PF10.
- **Re-running the reproduction (optional):** a throwaway clone with CI's install, Python 3.12 and closed rails. The evidence lane takes about 14 minutes on 4 CPUs.
- **Writes:** only its review and any addendum, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.

## Canon relied on

Read on `main` at `7d5a5aa`. Each source maps to the decision topics it governs.

**ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1.** Read in full on 2026-10-23. Governs:
- the required inputs;
- `AUTHORING_CONTEXT`;
- Execute steps 1 to 6 (validation; proven cause against hypotheses; DISCOVERY_REQUIRED only when decisive evidence is missing; one complete proposal ending `ASK OK?`; no product-intent change; no Plan, vehicle, Proceed or addendum);
- the required result;
- routing to ESC-40.

**ESC-40 — Review and Return Approved Remediation — 100926.1.** Read in full. Governs:
- what the proposal must give the reviewer (one complete bounded overlay; the delivery and return map; `PR_RETURN_PHASE` only when an existing PR phase is affected);
- the qualifying-approval addendum.

**PR-10 — Create PR Work-Unit Instructions — 100926.1.** Read at its "Inputs". Governs the remediation lineage (ESC-30 proposal, ESC-40 review): for an approved remediation overlay, the immutable Plan and its original review are preserved, and the remediation review and addendum are carried. It also requires exactly one planned `WORK_UNIT_ID`, which is P-2's WU-REM-01.

**QA-10 records, read in full:**
- `docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md` (§5, the failed-objective package);
- `docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md` §3 (FND-001; required resolution evidence (1) to (3));
- `docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.0.md`, at E-005, E-326 to E-328, RA2-22 and N-002.

**PF10-HDE-Build-Notes v13.7.5.** Read:
- the Addendum Index (2.1 to 2.22);
- addendum 2.11 (rules 1 and 4, business case and real inputs);
- addendum 2.18 in full (no cost ceiling, so none is stated in §5.4);
- addendum 2.5, WU-PR-02's acceptance, accepted-final;
- addenda 2.19 and 2.20 (Plan delta 01 and Specification delta 01, the overlays in force);
- addendum 2.1 (the TypeSafe reading).

The whole file was searched for "S22", "FND-001", "test_absent_admitted", "ESC-30", "ESC-40", "prospective PR owner" and "accepted-final". No addendum addresses this test's behaviour after QA creates the root.

**In-flight approved bases:**
- **Specification:** `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (S22; Constraints "QA evidence admission"; QA requirement), with `…-specification-delta-v1.0.md` and its review.
- **Implementation Plan:** `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` §7 WU-PR-02, with its review v1.1, and Plan delta 01 v1.1 with its review v1.1. The delta was searched for "WU-PR-02", "S22" and "acceptance (5)"; it touches none of them.
- **WU-PR-02 records:** `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md` §8.4 (where the test was specified) and `…-WU-PR-02-pr-work-unit-lineage-review-v2.0.md` (accepted-final), as cited by addendum 2.5.

**HDE Governance §9.1.1** (read for earlier reviews; unchanged on `main`). Governs:
- an approved base changed only by overlay;
- an IA that may not expand scope;
- accepted-final work preserved.

**`AGENTS.md`.** Governs:
- the evidence-lane and governed-evidence rules (sole writer; no hand-editing; QA output placement);
- the closed rails;
- the pytest readiness rule;
- the code-review real-input rule.

**Repository facts read on `main` at `7d5a5aa`:**
- `tests/evidence/test_evidence_index_missing_state.py`, lines 15–30, 318–344, 965–1014, 1248–1383;
- `.github/workflows/ci.yml`, lines 85–100, 221–240 and 273–343;
- `tools/evidence/update_evidence_index.py` `publish_crd_check_family` (5166–5191);
- `tools/qa/qa_harness.py` `CheckResult` (109–124);
- the Index, Mirror and manifest searched for the test file (0 matches each).

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / ESC-30 / FND-001 proposal 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` + delta 01 |
| requirement / work unit | S22; proposed WU-REM-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9, page state 2026-10-12 |
| role/stage | continuing Thoth, ESC-30 |
| capture time | 2026-10-23T16:23:00Z |
| execution identity | https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent); recorded here only |
