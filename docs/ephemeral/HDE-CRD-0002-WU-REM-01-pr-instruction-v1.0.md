---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-REM-01-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-01
work_unit_title: "Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation; S22, with S21's close-run tests)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (INITIAL_APPROVE). Neither is edited
applicable_overlays: (1) Specification delta 01 (DELTA_APPROVE; HDE Build Notes addendum 2.20); (2) Implementation Plan delta 01 v1.1 (DELTA_APPROVE; addendum 2.19); (3) the approved remediation of FND-001, REMEDIATION_REVIEW APPROVE_AS_CHANGED, whose §4 overlay (P-1, P-2, R-1 to R-3, V-1 to V-5, with C-1) creates this unit (addendum 2.23, record only); (4) addendum 2.18 (no cost ceiling); (5) addendum 2.3 (Codex security review deprecated)
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S22 and Constraints "QA evidence admission", with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md, approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 (WU-PR-02 acceptance (5), as P-1 restates it; WU-REM-01 as P-2 adds it), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1; blob 5103fe29d588)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md (APPROVE_AS_CHANGED, "ASK OK."; Isis; blob e100bf4eba08; #708, squash bd7366a)
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md (Thoth; blob ee59f22c432a; sha256 d120223b8e9d5f51176228153a1debf8274f142cd780520cf7513c0a4d02b70d; #707, squash 2a8992f)
remediation_addendum: docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (numbered 2.23; blob 248c17e7e513). Not yet published into PF10 v13.7.5, whose last addendum is 2.22; publication is the Product Owner's
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001; Reality Audit RA2-22; blob dac6d1a79de8)
originating_stage_and_return: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, NOT_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md; blob f6d7ff018ce7). Return: the same Isis QA-10 reassessment of S22 and its dependants, after this unit's PR-40 ACCEPT
accepted_final_not_reopened: WU-PR-02 (docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v2.0.md, ACCEPT; blob 4512db789c82; addendum 2.5)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (blob b39ac9f276db)
business_case_ref: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md §5.4, approved by the review's §4 P-2
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
CURRENT_PF10_MARKDOWN_LINK: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (454,052 bytes; sha256 2759c4da5e779970f144686c60f9683048583cd7ca50337026c1f8c7c548e167)
ACTIVE_PF10_ADDENDA_LINKS:
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.3 (Codex security review deprecated)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.5 (WU-PR-02 accepted-final)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.11 (business case; real inputs; finding disposition; repeated finding class), as §2.18 narrows it
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.14 (a P1 finding is addressed until resolved)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.18 (no cost ceiling)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.19 and §2.20 (Plan delta 01; Specification delta 01)
  - docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23, the approved remediation; record pending publication)
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state of 2026-10-12T02:29:33.739Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-23T16:50:00Z
repository_baseline: origin/main bd7366a (#708). Every repository fact in §5 was measured at this head. No file outside docs/ephemeral/ changed between 7d5a5aa, the proposal's reproduction head, and bd7366a
receiver: a new dedicated HDE-CRD-0002 WU-REM-01 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1 to CR-8 carried, all decided; CR-9 carried PROPOSED and unaffected; no new entry (§16)
---

# HDE-CRD-0002 WU-REM-01 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete PR instruction for work unit WU-REM-01 of HDE-CRD-0002. The unit exists because Isis approved, as changed, Thoth's remedy for QA-10 finding FND-001 (requirement S22).

- **The defect.** The evidence lane runs `tests/evidence/test_evidence_index_missing_state.py`. One test and two fixtures in it assume that the real checkout holds no HDE-CRD-0002 QA root and no HDE-CRD-0002 close pack. So the first pull request that publishes this change's QA evidence would fail CI. Thoth reproduced it: 2 failed and 4 errors, against 134 passed without the root.
- **The unit.** A test-only change to that one file:
  - one test is rewritten (R-1);
  - the `crd_repo` fixture is extended (R-2);
  - the `close_repo` fixture is extended (R-3, with C-1).
- **The proof.** V-1 to V-5 (§10).

This instruction issues the approved remedy into one planned work unit. It does not approve a plan, give a Proceed, implement, merge or decide QA. WU-PR-02 stays accepted-final and is not reopened.

## 2. Identity and lineage

| Item | Value |
| :- | :- |
| Unit | WU-REM-01, a PR unit in the Distillation phase. P-2 adds it to Plan v1.1 §7 after WU-OPS-01 and before QA-10 readiness |
| Approved bases (immutable) | Specification v1.1 with delta 01; Implementation Plan v1.1 with its review v1.1 and Plan delta 01 v1.1 |
| Remediation overlay | Remediation review v1.0 §4 (P-1, P-2, R-1 to R-3, V-1 to V-5, C-1); addendum 2.23 record |
| Originating finding | Triage §3 FND-001, with its required resolution evidence (1) to (3) |
| Return owner | Isis, QA-10 reassessment of S22 and its dependants |
| PR lineage owner | This IA (PR-10 now, PR-40 after the merge) |
| `PR_RETURN_PHASE` | Not applicable: no existing PR phase is affected; this is new implementation by a lawful prospective PR owner |

## 3. Unit selection and dependency state

- **Selected because:** the approved remedy (review §4 P-2) names WU-REM-01 and routes it to PR-10 (review front matter, `next_prompt`; addendum 2.23 `return_phase`).
- **Dependencies (P-2):** "none on unmerged work; it lands before QA-20". All of Plan v1.1 §7's units are accepted (addendum 2.22), and #708 is merged.
- **Order after this unit:** WU-REM-01 is accepted (PR-40), then Isis reassesses QA-10, then QA-20 follows if it is READY_FOR_QA.

## 4. Required behaviour (approved remedy, review §4)

All of it is in `tests/evidence/test_evidence_index_missing_state.py`. Each requirement below is quoted from the approved overlay, followed by what it means for this file.

**R-1, the absence test.** "Replace the real-checkout absence test with one that builds the absent state in a copy. It removes `audit/qa/hde-crd-0002/` and its Index rows, regenerates and runs `--check` through the canonical updater, then asserts no HDE-CRD-0002 row from `_load_crd_qa_entries([])` and none in the Index under the root. It does not read whether the real checkout holds the root."
- The test replaced is `test_absent_admitted_crd_root_publishes_nothing` (lines 977–984).
- Its replacement must be true whether or not the real checkout holds the root.
- The loader must be read from the **copy's own updater**. `tools/evidence/update_evidence_index.py` binds `ROOT = Path(__file__).resolve().parents[2]` (line 28), so an in-process import reads the real checkout (§5.3).
- It keeps what Plan acceptance (5) protected, as P-1 restates it: "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed".

**R-2, the `crd_repo` fixture.** "`crd_repo` builds the pre-first-publication state for every root in `ADMITTED_CRD_QA`: it removes each root and its Index rows, then regenerates and checks through the canonical updater. The existing assertions of `test_crd_0002_fixture_root_publishes_beside_crd_0001` stay."
- Today the fixture (lines 317–344) strips only `CRD_ROOT` (`audit/qa/hde-crd-0001`).
- It must strip every admitted root, read from `ADMITTED_CRD_QA`, today HDE-CRD-0001 and HDE-CRD-0002. A later admitted CRD is then covered without editing the fixture (proposal §8).
- Ten tests use this fixture (§5.2). None of their assertions changes.

**R-3, the `close_repo` fixture, with C-1.** "`close_repo` removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, from the copy, then regenerates and checks through the canonical updater. The four close-run tests keep their assertions."
- Today the fixture (lines 1270–1275) only asserts `not (repo / CLOSE_ROOT).exists()` on its copy.
- After the strip and regeneration, that assertion holds on the copy.
- Index rows must be removed before regenerating. The updater refuses a close-pack row whose file is absent (`CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`) and a half-present pair (`CRD_CLOSE_PACK_INCOMPLETE`) (§5.3).
- The close candidate source has no Index row or path proof today (§5.3). It is removed if present, together with any path proof and row a later change may add.

**Limit (review §4).** "No other file changes. A shared helper, if any, stays in the same file." The helper's shape, the fixture order and any refactor of the three strips into one helper are PR-20's design.

**Restated acceptance (P-1)** is quoted in R-1 above: the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source.

## 5. Current repository and reference baseline (measured at `bd7366a`)

### 5.1 The file

- **`tests/evidence/test_evidence_index_missing_state.py`:**
  - 1,383 lines; blob `bff9a6b0f34f`; sha256 `fb710617856b629ac69218230f5d4db02f186c94717a82dcc87cb7451bb95e79`;
  - last changed by `8b73b57` (#668, WU-PR-07), and before that by `1d2c834` (#634, WU-PR-02).
- **Not a release member:** `catalog/manifest.json` does not list it.
- **Constants:**
  - `ROOT` (line 14); `IGNORES` (15–17); `ENV`, closed rails (18–27);
  - `CRD_ROOT = "audit/qa/hde-crd-0001"` and `CRD_KEY` (28–29);
  - `CRD_FIXTURE_PROGRAM` (30–58), which runs inside the copy and asserts `writer.ROOT == Path.cwd()`;
  - `SKELETON` (59–70);
  - `CLOSE_CRD`, `CLOSE_ROOT = "audit/qa/hde-crd-0002"` and `CLOSE_PACK` (1249–1251);
  - `CLOSE_FIXTURE_PROGRAM` (1252–1261).
- **Helpers:** `_run` (73), `_success` (87), `_checks` (91, six validators), `_snapshot` (103), `_crd_program` (347), `_whole_tree_state` (354), `_close_program` (1263), `_index_rows` (1278).

### 5.2 The loci

| Locus | Lines | Today | Users |
| :- | :- | :- | :- |
| L-1 `test_absent_admitted_crd_root_publishes_nothing` | 977–984 | Asserts, on the real `ROOT`, that `audit/qa/hde-crd-0002` is absent, that `writer._load_crd_qa_entries([])` (imported in-process) yields no HDE-CRD-0002 row, and that `docs/evidence/INDEX.json` has no row under it | itself |
| L-2 fixture `crd_repo` | 317–344 | Copies `ROOT`; removes `CRD_ROOT` and its Index rows; runs the updater, then the updater with `--check` | 10 tests: lines 370, 417, 440, 461, 492, 513, 554, 990, 1017, 1028 (some parametrized) |
| L-3 fixture `close_repo` | 1270–1275 | Copies `ROOT`; `assert not (repo / CLOSE_ROOT).exists()` | 4 tests: lines 1285, 1317, 1350, 1377 |
| The close-pack assumption | 1285–1315 | `test_crd_close_pack_rows_are_absent_tolerant` checks that the copy's skeleton is stable under `--check` and a write, that no `CLOSE_PACK` row exists, then writes stand-in close-pack files | served by L-3 |

### 5.3 Code facts the remedy relies on

- **The updater's root.** `tools/evidence/update_evidence_index.py`:
  - binds `ROOT` to its own file (line 28);
  - `ADMITTED_CRD_QA` (lines 51–54) admits HDE-CRD-0001 and HDE-CRD-0002;
  - `_load_crd_qa_entries` (line 3947) reads under that `ROOT`.
  - So a test that inspects a copy must run the copy's own updater, as `_crd_program` and `_close_program` do (`cwd=repo`).
- **Close-pack rows.** `_crd_close_pack_entries` (line 4046) pairs `audit/<CRD>_close_report.md` with `audit/<CRD>_MANIFEST.json` for every admitted CRD:
  - neither present: no rows;
  - both present: one row each;
  - one present: `CRD_CLOSE_PACK_INCOMPLETE`;
  - a row with its file absent: `CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`.
  - The close candidate source is not indexed and gets no path proof.
- **The candidate source.** Its path, `audit/HDE-CRD-0002_close_candidate_source.json`, is fixed by `docs/adr/hde/close_pack_writer_adr.md` §3 ("Paths of record") and named by `tests/qa/test_generate_epic_close_pack.py:4346` (`CRD_SOURCE_REL`).
- **State of `main`:**
  - `audit/qa/` holds only `hde-crd-0001`;
  - no `audit/HDE-CRD-0002_*` file exists;
  - `audit/ops/hde-crd-0002/wu-ops-01/` exists (WU-OPS-01 evidence). It is not an admitted QA root, is not indexed, and the evidence lane passed with it present (hosted push run 39962751831 on `04645f4`). The remedy does not touch it.

### 5.4 CI facts

- **The evidence lane** (`.github/workflows/ci.yml`, step "Run governed evidence integrity lane", lines 221–240; blob `3836bad11c39`) runs:
  - seven validators: `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `ci/checks/check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_final_lf.sh`;
  - `python -m pytest -q` on six files: this file, `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_machine_mirror_self_proof.py`, `tests/evidence/test_orientation_demo.py`, `tests/ops/test_evidence_index.py`, `tests/qa/test_epic020_qa_docs.py`.
- **The release lane** is the step "Build and verify exact-source release attestation", lines 273–343.
- **Classification** (`classify_paths`, run read-only at `bd7366a`):
  - this test file alone: `evidence` only, no changed-test targets;
  - `audit/qa/hde-crd-0002/…`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`: `evidence` only;
  - `docs/evidence/INDEX.json`: `evidence` and `release`. A real QA-evidence pull request regenerates the Index, so it runs both lanes; that is why V-2 runs both.
- **Baselines:**
  - 134 tests passed in the six files at `7d5a5aa`, in 827.7 s (proposal §4), and at `8e6f238` (this IA's OPS-10 rehearsal replay);
  - no file outside `docs/ephemeral/` changed from `7d5a5aa` to `bd7366a`;
  - with a stand-in root: 2 failed, 128 passed, 4 errors (proposal §4).

## 6. Bounded files and components

| Path | Change |
| :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | The only code file changed: R-1, R-2, R-3 |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-*` | The unit's records: the plan, its prototype diff if any, and the result records |

Expected unchanged:
- every other file, including `tools/evidence/update_evidence_index.py`, `tools/qa/qa_harness.py`, `.github/workflows/ci.yml` and `ci/checks/**`;
- the governed evidence: Index, Mirror, sentinels, path proofs, orientation;
- `audit/**`, every release member, `docs/pfcanon/**`, `AGENTS.md`, `README.md`;
- every other test file.

## 7. Exclusions

From review §5 and proposal §7:
- no runtime, updater, harness or workflow change;
- no regeneration or hand edit of governed evidence;
- no new evidence family;
- no HDE-CRD-0002 QA evidence, close pack or candidate source is produced or committed. Stand-ins exist only in throwaway clones;
- no Specification change and no re-run of an accepted-final PR (WU-PR-02);
- FND-024 (the PR35-C1 flake risk on QA-evidence pull requests) stays with its recorded owner.

## 8. Interface contracts with other units

- **QA-50 and later QA evidence pull requests:** after this unit, publishing under `audit/qa/hde-crd-0002/` through `publish_crd_check_family` must leave the evidence lane green with no change to this file. That is the business-case measure.
- **The close stage (S21):** the close-run family (`publish_crd_close_run_family`), the close pack and the candidate source land on `main` without breaking the evidence lane.
- **The admission table:** R-2 reads `ADMITTED_CRD_QA`. The updater's table is unchanged, and `test_admitted_crd_table_is_explicit_and_matches_the_harness_roots` (line 965) still pins it.

## 9. Disposition rules PR-20 must apply and record

1. **Design choices recorded in the plan:**
   - the form of R-1's copy, since it may reuse `crd_repo` or its own copy;
   - the strip helper's shape and where it lives (this file);
   - the order of strip, regeneration and `--check`;
   - how R-1 calls the copy's loader (§5.3).
2. **Stand-ins (C-1).** The form of every stand-in used by V-2 and V-3 is the plan's. Stand-ins are produced only through the harness and the canonical updater (`publish_crd_check_family`, `publish_crd_close_run_family`, and the updater's write for the close pack), plus a stand-in candidate-source file. Each states that it is not QA evidence. Nothing from a rehearsal clone is committed.
3. **Prototype.** Run the planned change and V-1 to V-4 in a throwaway clone with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), Python 3.12 and closed rails. Record exact counts, times and exit codes. The evidence lane takes about 14 minutes.
4. **Lane time.** Record the six files' run time against the 827.7 s baseline (proposal §8). R-1 now builds a copy, which costs one more regenerate-and-check; this is expected.
5. **Re-check the baseline.** Confirm §5's facts at the plan's head. Any change in a decisive fact is recorded, and any change in scope goes through §14.

## 10. Acceptance, tests and evidence

Each check is quoted from review §4 and mapped to the triage's required resolution evidence.

| ID | Check | Pass condition | Covers |
| :- | :- | :- | :- |
| V-1 | Local, on the PR head, with the root absent | The 7 evidence-lane validators exit 0; the six pytest files pass with no fewer than 134 tests | (1) |
| V-2 | Rehearsal in a throwaway clone of the PR head, with a stand-in HDE-CRD-0002 QA family published by the harness and the canonical updater | "the evidence lane and the release lane pass, exactly as `ci.yml` runs them" | (3) |
| V-3 | The V-2 clone, additionally holding a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater | "the evidence lane passes", with all three close-stage inputs present (C-1) | (3), close stage |
| V-4 | Negative control | "the R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy" | Keeps acceptance (5)'s property |
| V-5 | Hosted CI on the PR head | "the evidence lane is green, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`" | (2) |

- **Triage resolution evidence (1)**, the updated test on `main`, is met when the merged change carries R-1 to R-3, checked at PR-40.
- **Evidence obligations (P-2):** the PR result record names every check actually run, with counts, and includes the V-2 and V-3 rehearsal outputs: commands, exit codes, test counts and the stand-ins' provenance. There is no governed evidence change.
- **Business-case measure** (proposal §5.4): "The first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests".
  - It cannot be observed at this unit's PR-40, because that pull request does not exist yet.
  - PR-40 records V-2 and V-3 as its proxy and the measure as "not yet measurable".
  - The measure is checked at the first QA-evidence pull request, or by the QA-10 reassessment (addendum 2.18 rule 5; proposal §5.4).

## 11. Migration and security constraints

- **Migration:** none.
- **Security:** test code only. It touches no secret, credential, network or production surface. The fixtures' subprocesses run under the file's closed-rails `ENV`.
- **Real inputs:** the remedy rests on this change's own QA evidence and the hosted CI runner (addendum 2.11 rule 4; proposal §2), not on a constructed input.

## 12. Engineering, review, CI and merge obligations

**PR-20, in the dedicated PR session:**
- reads this instruction and its lineage, including review §4, proposal §3 to §5 and triage §3, with the file and `ci.yml` on `main`;
- re-checks §5, prototypes (§9.3) and records §9's choices;
- writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`;
- returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.

**PR-30**, after Nathan's Proceed for that exact plan, given against the business case:
- recovers existing work first;
- changes only the one test file;
- runs V-1 to V-4 on the real branch;
- commits coherently;
- publishes `PR_CANDIDATE_PUBLISHED`;
- hands off to PR-35 in its own session.

**PR-35**, in its own dedicated session:
- **Codex review:** retrieves and dispositions the Codex code review findings under addendum 2.11 rule 7 and addendum 2.14. A P1 on a real input is fixed. A decline of a P1 goes to the Product Owner first. Rule 8 applies to a repeated finding class.
- **No security review:** there is none to obtain, because addendum 2.3 deprecates the Codex security review.
- **CI:** verifies current-head CI (V-5) and mergeability. A failure that is red on the base too is handled as base-red, not by widening the unit.
- **Returns** `MERGE_PENDING` without merging.

**Other obligations:**
- **PR description:** the `.github/pull_request_template.md` headings, filled under the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage.
  - It verifies R-1 to R-3 on the merged head, and V-1 to V-5 from the records and the hosted run.
  - It records the business-case measure's state (§10).
  - On ACCEPT it returns to the same Isis QA-10 reassessment (review §6; addendum 2.23), not to a Plan unit.
- **Nonclaims** every record keeps: no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, pull requests and `docs/ephemeral/` before creating anything.
- **Rehearsals and prototypes:** they run only in throwaway clones. Discard and re-clone on failure. Nothing from them is committed.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version.
- **Rollback:** the Product Owner reverts the squash commit. No member is touched, so there is no manifest refresh.
- **Abort:** only by Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material:** a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or scope or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional; RS-30 for revisions), and this IA reviews it through RS-20.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Changes to the approved remedy itself** belong to Isis through ESC-30 and ESC-40, not to RS-20.
- **Expected triggers:**
  - a needed change outside the one test file, for example in the updater, the harness, `ci.yml` or another test;
  - a stand-in rehearsal that fails for a reason R-1 to R-3 cannot fix;
  - a finding that S22 or S21 requires runtime work.
- **Not a trigger:** a §9.1 design choice, or a helper kept in the same file.

## 15. Unresolved items, carried observations and owners

| Item | Owner |
| :- | :- |
| Publishing addendum 2.23 into PF10 | Product Owner |
| CR-9 (path proofs under the Ops evidence root), unaffected by this unit | Isis, at IA-30 |
| FND-024, the PR35-C1 flake risk on QA-evidence pull requests | As recorded in the triage |
| The business-case measure (§10) | Checked at the first QA-evidence pull request or by the QA-10 reassessment |
| The QA-10 reassessment of S22 and its dependants | Isis, after this unit's PR-40 ACCEPT |

## 16. Canon-conflict register

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | addendum 2.7 |
| CR-9 | PROPOSED, not yet reviewed | Isis (IA-30) | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13 |

**No new conflict.** FND-001 is an implementation defect against an approved objective, and the remedy changes no canon (review §2; proposal §11).

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Owned by | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S22 acceptance intent; Constraints "QA evidence admission" | QA evidence under `audit/qa/hde-crd-0002/` publishes and validates before QA | §1, §4: the evidence lane stops blocking that publication | WU-REM-01 | V-2, V-5 | PR result; hosted CI |
| P-1 (acceptance (5) restated) | An absent root publishes nothing, proven in a copy; no test depends on the real checkout's HDE-CRD-0002 state | R-1; §4 "Restated acceptance" | WU-REM-01 (WU-PR-02 untouched) | V-1, V-4 | PR result |
| P-2 Purpose, Scope, Dependencies | Test-only, one file; none on unmerged work; lands before QA-20 | §3, §6, §7 | WU-REM-01 | — | PR-40 attribution |
| P-2 Evidence obligations | The result names V-2 and V-3 outputs; no governed evidence change | §10 | PR-30, PR-35 | — | PR result |
| P-2 Business case | Beneficiary, evidence, benefit, measure | §10 measure; Proceed against it | Product Owner (Proceed); IA (PR-40 records it) | Measure, later | First QA PR, or QA-10 |
| R-1 | The absent state is built in a copy; the loader and Index are asserted without reading the real checkout | §4 R-1, with the copy-loader fact (§5.3) | PR-20 design; PR-30 | V-1, V-4 | PR result |
| R-2 | Strip every admitted root; existing assertions stay | §4 R-2; 10 users (§5.2) | PR-20; PR-30 | V-1, V-2 | PR result |
| R-3 with C-1 | Strip the root, `close/`, the report, the manifest and the candidate source, with their proofs and rows; then regenerate and check; assertions stay | §4 R-3; row-before-regenerate rule (§5.3) | PR-20; PR-30 | V-1, V-3 | PR result |
| Limit | No other file; a helper stays in the file | §4 Limit; §6 | PR-20 | PR-40 attribution | Merged diff |
| V-1 to V-5 | As quoted | §10, quoted | PR-30 (V-1 to V-4), PR-35 (V-5) | — | PR result; hosted run |
| Triage (1) to (3) | Updated test on `main`; hosted CI; a root-present demonstration | §10 "Covers" column | WU-REM-01 | — | PR-40 |
| Exclusions | No runtime, updater, harness, evidence or Specification change; no QA evidence | §7 | All phases | PR-40 attribution | Merged diff |
| WU-PR-02 accepted-final | Not reopened | §1, §2 | — | — | — |

- **Numeric domains:**
  - "no fewer than 134" is a count of passed tests over the six files, measured at code-identical `7d5a5aa`;
  - "7 validators" is the count in `ci.yml` lines 227–233;
  - the stand-in families use the harness's own status values (`PASS`) and no new value.
- **No decisive comparison fails.**

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated WU-REM-01 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Returns to this IA:** RS-20 for a rescope; PR-10 for an instruction defect; PR-40 after Nathan's merge.
- **Final return:** after PR-40 ACCEPT, the same Isis QA-10 — Audit Implementation and Establish QA Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c), for the reassessment of S22 and its dependants.

## 19. TypeSafe reading for the receiving session (PR-20, WU-REM-01)

Action sent (v8.2): "Plan, as the dedicated pull-request engineering author, one new detailed implementation plan for a remediation work unit with an approved instruction: a test-only change to one evidence test file of about 1,400 lines, in which one test is rewritten and two fixtures are extended so that they build their starting state in a copy and stop assuming the change's own QA directory, close-run family and close pack are absent. The plan states the code design, prototypes it in a throwaway clone, and defines five verification checks, including two rehearsals that publish stand-in evidence through the canonical tools and a hosted CI run. It is a Markdown plan with a prototype diff; no code is committed; a Product Owner Proceed, implementation, review and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.01 (confidence 0.86). Rung probabilities: low 0.00, medium 0.10, high 0.79, extra high 0.11, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.07, Opus 5.5 0.81, Sonnet 5.5 0.12, Haiku 5.5 0.00 (confidence 0.75).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.007, Fable 5.1 at high 0.055, Fable 5.1 at extra high 0.008, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.081, Opus 5.5 at high 0.640, Opus 5.5 at extra high 0.089, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.012, Sonnet 5.5 at high 0.095, Sonnet 5.5 at extra high 0.013, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: none.
  - Sent 2026-10-23T16:43:08Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T16:43:08Z; HTTP 200 in 0.56 s; 5496 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is in the remediation review §8.

**Surface advice:** run PR-20 in a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, dedicated to WU-REM-01, with Notion read access for the prompt.
- **Prototype:** a throwaway clone with CI's full install, Python 3.12 and closed rails, with room for about two evidence-lane runs of about 14 minutes each (the V-2 and V-3 rehearsals).
- **Writes:** only the plan, and its prototype diff if any, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this instruction's pull request is merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-PR-10-20261023-WU-REM-01-01` |
| Change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| Requirement / work unit | S22 (with S21's close-run tests); WU-REM-01 |
| Prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, page state of 2026-10-12T02:29:33.739Z |
| Release | GCFPE-20261009.1 / 100926.1 |
| Role and stage | whole-change IA, PR-10 |
| Capture time | 2026-10-23T16:50:00Z |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |
| Repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) |

## Canon relied on

Read on `main` at `bd7366a`. PF10 is v13.7.5.

| Decision topic | Sources and sections |
| :- | :- |
| Instruction contract, readiness, routing | PR-10 — Create PR Work-Unit Instructions — 100926.1, read in full: "Inputs" (the remediation overlay preserves the immutable Plan and original review and carries the remediation review and addendum), "Execute" 1 to 8, "Semantic readiness before INSTRUCTION_READY", "Required result", "Next step and recovery" |
| The approved remedy | `docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md`, read in full (§2 to §6; §4 is the overlay); `docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md`, read in full; `docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md`, read in full |
| The originating finding and return | `docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md`, read in full; `docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md` §3, read in full |
| The objective | Specification v1.1-approved: the S22 row, Constraints "QA evidence admission" and the Distillation phase row; Implementation Plan v1.1 §7 WU-PR-02, read in full, and §7's common terms for PR units |
| WU-PR-02 accepted-final | PF10-HDE-Build-Notes v13.7.5 §2.5; `docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v2.0.md` |
| Review chain | PF10 v13.7.5 §2.3 (Codex security review deprecated), §2.11 rules 7 and 8, §2.14 (P1 findings) |
| Business case and its measure | PF10 v13.7.5 §2.11 rules 1, 2 and 4, as §2.18 narrows them; §2.18 rule 5 (PR-40 records whether the measure was met) |
| What changed in PF10 since v13.7.4 | v13.7.5 adds only §2.22 (the WU-OPS-01 receipt), read in full; addendum 2.23 is a record pending publication |
| Evidence writer rules | `AGENTS.md` "Governed evidence rules" (sole writer; no hand-editing); HDE Schemas and Artifacts §8.3 (single-writer remediation), as cited in the WU-OPS-01 task record |
| QA entry | PF19-Canon-Glow-QA-Guide v3.0.6 §3.1 and §3.1.1, read for the OPS-30 receipt in this session; unchanged on `main` |
| Repository facts | `tests/evidence/test_evidence_index_missing_state.py` lines 1–113, 300–370, 960–1030 and 1245–1383; `tools/evidence/update_evidence_index.py` lines 28–54, 3947–3960 and 4046–4090; `tests/qa/test_generate_epic_close_pack.py:4346`; `docs/adr/hde/close_pack_writer_adr.md` §3; `.github/workflows/ci.yml` lines 221–343; `ci/checks/classify_ci_changes.py` `classify_paths`, run read-only |
