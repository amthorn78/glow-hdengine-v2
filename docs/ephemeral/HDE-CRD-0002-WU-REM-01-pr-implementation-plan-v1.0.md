---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-REM-01-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: DRAFT
plan_result: BLOCKED on boundary finding F-1 (§16). Not AWAITING_PO_PROCEED. The approved remedy's acceptance (P-1, V-3) cannot be met within its one-file limit; the change to the approved remedy belongs to Isis through ESC-30 and ESC-40 (instruction §14)
predecessor: none (first plan for WU-REM-01)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-01
work_unit_title: "Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation; S22, with S21's close-run tests)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.0.md (HDE-CRD-0002-WU-REM-01-PR-INSTRUCTION v1.0, INSTRUCTION_READY; blob d89d1dc9991b; sha256 1661b2d54388483e8e371a32d9d3ef91b75da293e6b7640243a0db3eea7641b9; landed by #709 as 16ecf95)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved; blob abffa2ccbd44), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1, DELTA_APPROVE; blob 5103fe29d588). WU-REM-01 is added to its §7 by the remediation overlay P-2, not by a Plan revision
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S22 and Constraints "QA evidence admission", with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md (ESC-40 APPROVE_AS_CHANGED, "ASK OK."; Isis; blob e100bf4eba08; #708, squash bd7366a). Its §4 is the overlay this plan implements
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md (Thoth, ESC-30; blob ee59f22c432a; #707, squash 2a8992f)
remediation_addendum: docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (numbered 2.23; blob 248c17e7e513). Not yet published into PF10 v13.7.5, whose last addendum is 2.22; publication is the Product Owner's
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; blob b39ac9f276db)
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (QA-10 FND-001; blob dac6d1a79de8), from docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md (QA-10 NOT_READY; blob f6d7ff018ce7)
boundary_finding: F-1 (§16), raised by this PR-20 against the approved remedy for QA-10 FND-001
return_owner: Isis, the same QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, for the reassessment of S22 and its dependants, after this unit's PR-40 ACCEPT (unchanged)
accepted_final_not_reopened: WU-PR-02 (lineage review v2.0, ACCEPT; PF10 addendum 2.5)
business_case_ref: docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.0.md §5.4, approved by the review's §4 P-2; no cost ceiling (addendum 2.18)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1. Neither is edited
effective_baseline: approved base + applicable PF10 overlays — Specification delta 01 (addendum 2.20), Plan delta 01 v1.1 (addendum 2.19), the approved FND-001 remediation (record 2.23: P-1, P-2, R-1 to R-3, V-1 to V-5 with C-1), and addenda 2.18, 2.11 (as 2.18 narrows it), 2.15, 2.14, 2.5, 2.3 and 2.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md (blob 8697ad656156; 454,052 bytes; sha256 2759c4da5e779970f144686c60f9683048583cd7ca50337026c1f8c7c548e167; the only PF10 file on main at 16ecf95)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md §2.1, §2.3, §2.5, §2.11, §2.14, §2.15, §2.18, §2.19, §2.20; docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23, record pending publication)
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0-prototype.diff (R-1 to R-3 only; git diff 16ecf95 → prototype head b1a4e17; 1 file, +57/−26; 127 lines; 6,142 bytes; sha256 1203de91f5aa3eb3d0ad9957f90ee6945ec54248886927fc609c49b72c56216e; `git apply --check` clean on 16ecf95). F-1's candidate line is quoted in §16 and is not in the diff
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5 (the dedicated WU-REM-01 PR engineering session that Nathan created; PR-20 now, and PR-20 again when the remedy decision returns)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, fetched and read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_baseline: origin/main 16ecf95 (#709). Outside docs/ephemeral/, every byte equals bd7366a, the instruction's measured baseline (git diff --stat bd7366a 16ecf95 lists only the instruction file)
working_branch: claude/zen-thompson-fe89f0, cut from 16ecf95 (documents only)
next_prompt: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9), continuing Thoth
created_at: 2026-10-23T18:20:00Z
canon_conflict_register: CR-1 to CR-8 carried, all decided; CR-9 carried PROPOSED and unaffected; no new entry (§19)
---

# HDE-CRD-0002 WU-REM-01 — PR Implementation Plan v1.0

## 1. Result

**BLOCKED, not AWAITING_PO_PROCEED.** This is a complete planning draft for WU-REM-01. Within the approved remedy (one test file, R-1 to R-3 with C-1) it makes the design choices the instruction leaves to PR-20 (§5) and records the prototype (§12). The prototype found one boundary:

- **R0:** `main`'s test file fails exactly as FND-001 says on a stand-in HDE-CRD-0002 root: 2 failed, 4 errors.
- **V-1:** with the change and no root, the 7 validators exit 0 and the six files pass 134 tests (1,040.5 s; baseline 1,046.0 s).
- **V-2:** with a stand-in QA family published by the harness and the canonical updater, the evidence lane (134 passed) and the release lane pass. **The QA path is fixed:** the evidence lane would no longer block the first QA-evidence pull request.
- **V-4:** the R-1 test fails when an Index row is planted in its copy; a second mutation shows its loader assertion is live too.
- **V-3: fails.** With the close stage added (close-run family, close pack, candidate source), 1 test fails and 133 pass. The failing test is `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity`, in a second file. It reads the real checkout's Machine Mirror and rejects the `crd_id` key, which HDE Schemas and Artifacts §8.3 allows and which the updater puts on the CRD close-pack rows. This is finding **F-1** (§16).
- **V-3′ (substantiation only):** the same state plus one line, `"crd_id"` added to that test's optional key set, passes: 134 passed.

So the approved remedy cannot meet its own acceptance, P-1 and V-3, within its limit "No other file changes". The instruction routes exactly this case: "Changes to the approved remedy itself belong to Isis through ESC-30 and ESC-40, not to RS-20" (§14), and it lists "a needed change outside the one test file, for example in … another test" and "a stand-in rehearsal that fails for a reason R-1 to R-3 cannot fix" as triggers. The next step is the continuing Thoth's ESC-30 (§21).

**What is preserved.** §5 to §15 are the complete plan for R-1 to R-3, valid as written for those requirements, with their prototype. When the remedy decision returns, this session writes the successor plan from them and adds only what the decision approves. Nothing here is offered for Proceed. No code, PR or Proceed exists for WU-REM-01.

## 2. Lineage and sources read in this session

- **Instruction** v1.0, read in full at 16ecf95 (blob d89d1dc9991b, sha256 1661b2d5…, the bytes #709 landed). Its §5 baseline was re-measured (§4).
- **Remediation review** v1.0, read in full (§1 to §8; §3 C-1; §4 the overlay). **Addendum 2.23 record**, read in full. **Remediation proposal** v1.0, read in full (§3 diagnosis, §4 reproduction, §5 remedy and business case, §8 risks).
- **QA-10 records:** triage §3 (FND-001 and its required resolution evidence (1) to (3)) and readiness §5 (the failed-objective package and return condition), read in full.
- **Approved bases:** Specification v1.1-approved, the S22 row, Constraints "QA evidence admission", the QA requirement and the Distillation row; Implementation Plan v1.1 §3 to §5, §7's common terms for PR units, §7 WU-PR-02 (acceptance (5)) and §7 WU-PR-07 (the terminal state (a) and the transitions (b) T0 to T7, which name the close-stage files R-3 strips).
- **PF10 v13.7.5:** addenda 2.1, 2.3, 2.5, 2.11, 2.14, 2.15 and 2.18 read in full; the front matter "Precedence, versioning, and scope" and the Addendum Index read in full; 2.19 and 2.20 read at their S22 lines (they renumber S01 away and touch neither WU-PR-02 nor S22's intent); the search in "Canon relied on".
- **Prompts:** PR-30 — PR Implementation Proceed — 100926.1 (page state 2026-10-12T02:30:08.672Z) and ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (page state 2026-10-12T02:29:51.552Z), each fetched and read in full, to check the receivers' input predicates.
- **Code read at 16ecf95:**
  - `tests/evidence/test_evidence_index_missing_state.py` in full (1,383 lines);
  - `tests/evidence/test_evidence_skeleton.py` `test_mirror_schema_and_parity` (lines 511 to 594) and the file's other reads of the Index and Mirror;
  - `tools/evidence/update_evidence_index.py` lines 20 to 60, 3940 to 4100 and 5166 to 5260;
  - `tools/qa/qa_harness.py` `CheckResult` (lines 100 to 130);
  - `.github/workflows/ci.yml` in full; `ci/checks/classify_ci_changes.py` `classify_paths` and its evidence-lane owner table (lines 955 to 970); `ci/checks/check_final_lf.sh`; `ci/checks/check_mirror_schema.sh` (its `crd_id` entry and `EPIC_CRD_EXCLUSIVE` rule);
  - `tests/qa/test_generate_epic_close_pack.py` lines 4344 to 4349; `docs/adr/hde/close_pack_writer_adr.md` §3 "Paths of record";
  - the other evidence-lane test files and the release-lane tools (`tools/evidence/run_sanity_pipeline.py`, `tools/evidence/build_release_attestation.py`), searched for CRD, close-pack, candidate-source and ledger paths.

## 3. Business case (instruction §10; proposal §5.4; review §4 P-2)

Carried, not re-decided:
- **Beneficiary:** QA (Kronos) and the Product Owner. HDE-CRD-0002's QA evidence, and later its close pack, can be published through ordinary CI.
- **Evidence:** the proposal's reproduction (with a real-shaped root present, 2 failed and 4 errors in the evidence lane) and QA-10's NOT_READY on S22. This plan reproduced it again at 16ecf95 (§12, R0).
- **Benefit:** QA-20 and QA-50 can proceed; the first QA-evidence pull request and the close-pack pull request are not blocked by the evidence lane.
- **Measure:** "The first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests". Not observable at this unit's PR-40; PR-40 records V-2 and V-3 as its proxy and the measure as "not yet measurable" (addendum 2.18 rule 5).
- **No cost ceiling** (2.18 rule 1). No record of this unit records spend against one (rule 5).

**Effect of F-1 on the business case.** Within the approved limit, the QA half of the benefit is delivered (V-2), and the measure as worded would be met. The close-pack half is not: the close-pack pull request would still fail the evidence lane (V-3). F-1 therefore bears on the approved acceptance, not on the beneficiary or the measure.

## 4. Baseline re-check (instruction §9.5)

Measured at 16ecf95 in the session checkout (history deepened read-only, `git fetch --deepen=150`, to reach 1d2c834) and in throwaway clones.

| Fact (instruction §5) | Instruction (bd7366a) | Measured (16ecf95) |
| :- | :- | :- |
| Bytes outside `docs/ephemeral/` | — | identical to bd7366a |
| The test file | 1,383 lines; blob bff9a6b0f34f; sha256 fb710617…; last changed by 8b73b57 (#668), before that 1d2c834 (#634) | same |
| Release member | not listed in `catalog/manifest.json` | not listed (0 matches) |
| Constants and helpers | lines 14 to 70, 1249 to 1261; `_run` 73, `_success` 87, `_checks` 91, `_snapshot` 103, `_crd_program` 347, `_whole_tree_state` 354, `_close_program` 1263, `_index_rows` 1278 | same |
| L-1, L-2, L-3 | 977–984; 317–344; 1270–1275 | same |
| `crd_repo` users | 370, 417, 440, 461, 492, 513, 554, 990, 1017, 1028 | same |
| `close_repo` users | 1285, 1317, 1350, 1377 | same |
| Updater | `ROOT` 28; `ADMITTED_CRD_QA` 51–54 (HDE-CRD-0001, HDE-CRD-0002); `_load_crd_qa_entries` 3947; `_crd_close_pack_entries` 4046 | same; blob ad441edbea3c; `publish_crd_check_family` 5166, `publish_crd_close_run_family` 5222 |
| Candidate source path | `audit/HDE-CRD-0002_close_candidate_source.json` (ADR §3; `CRD_SOURCE_REL` at `tests/qa/test_generate_epic_close_pack.py:4346`) | same |
| State of `main` | `audit/qa/` holds no CRD root but `hde-crd-0001`; no `audit/HDE-CRD-0002_*`; `audit/ops/hde-crd-0002/wu-ops-01/` exists, unindexed | same (6 tracked files under the Ops root; 0 Index rows) |
| `ci.yml` | blob 3836bad11c39; evidence step 221–240; release step 273–343 | same |
| `classify_paths` | this file alone: `evidence` only; QA-root, close-run, close-pack and candidate-source paths: `evidence` only; `docs/evidence/INDEX.json`: `evidence` and `release` | same; also `audit/docdeltas/hde-crd-0002_doc_deltas.md`: `evidence` only |
| Evidence-lane baseline | 134 passed in the six files at 7d5a5aa (827.7 s) | 134 passed at 16ecf95 in 1,046.0 s on this container (§12, B0); the 827.7 s was measured on another container |
| Not in §5 | — | `tests/evidence/test_evidence_skeleton.py` (blob 057b4ae973ba; last changed by 75b3026, #529, before any CRD admission): `test_mirror_schema_and_parity`'s optional key set lacks `crd_id` (F-1) |

No difference in the instruction's facts changes a planning decision. The last row is new and is F-1.

## 5. Design decisions (instruction §9.1)

- **PD-1, one strip helper in this file: `_strip_from_copy(repo, *relatives)`.** It sits beside `_snapshot`, among the file's shared helpers, and serves R-1, R-2 and R-3. For each relative path it removes a directory tree, or a file and its sibling `.path_proof.txt`, whichever is present. It then drops every Index row whose `discovered_physical_path` is that path or lies under it, and runs the canonical updater: a write, then `--check`.
  - It is the existing `crd_repo` strip, generalised and moved, with that fixture's comment ("The real owner then regenerates the complete coherent skeleton and validates that state") kept in its docstring. The seed-ledger method is unchanged: only `docs/evidence/INDEX.json` is edited; the updater regenerates the Mirror, sentinels, proofs and orientation.
  - Rejected: three inline strips (the same logic three times); a helper in a `conftest.py` or shared module (outside the one-file limit, review §4).
- **PD-2, the order: remove files, drop rows, write, `--check`.** Rows leave before the updater runs, because the updater refuses a close-pack row whose file is absent (`CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`) and a CRD row whose root is gone (the loader validates a root that has rows). The updater runs every time, even when nothing named was present (today's `main`), so every fixture starts from an updater-produced fixed point. That costs one write and one check per use; §12 measures it.
- **PD-3, R-1's copy: its own copy, stripping only `audit/qa/hde-crd-0002`.** This is R-1's wording and P-1's ("a copy of the checkout from which that root and its Index rows are removed"). Other admitted families stay as the checkout holds them, so the loader runs over the real admission table with only HDE-CRD-0002 absent. Reusing `crd_repo` would also strip HDE-CRD-0001 for the same cost; rejected as less exact.
- **PD-4, how R-1 calls the copy's loader: through `_crd_program`.** It runs `CRD_FIXTURE_PROGRAM` plus two lines in a subprocess with `cwd` at the copy and the file's closed-rails `ENV`. `CRD_FIXTURE_PROGRAM` already asserts `writer.ROOT == Path.cwd()`, so the loader provably reads the copy, not the real checkout (instruction §5.3). The loader assertion runs inside that program, and the test requires its exit 0; the Index assertion reads the copy's `docs/evidence/INDEX.json`. Both predicates are the original test's, unchanged. The test keeps its name, `test_absent_admitted_crd_root_publishes_nothing`, so the WU-PR-02 records and the triage's E-328 still name it.
- **PD-5, where R-2 reads `ADMITTED_CRD_QA`: the updater imported in-process,** as `test_admitted_crd_table_is_explicit_and_matches_the_harness_roots` already does. The copy holds the same module byte for byte (`shutil.copytree` with `IGNORES` skips only caches and `.git`). `crd_repo` strips the first element of every value, today `audit/qa/hde-crd-0001` and `audit/qa/hde-crd-0002`. `CRD_ROOT` and `CRD_KEY` stay: ten tests still publish HDE-CRD-0001 through them.
- **PD-6, R-3's strip set, with C-1.** A new constant `CLOSE_SOURCE = "audit/HDE-CRD-0002_close_candidate_source.json"` sits beside `CLOSE_PACK`. `close_repo` strips `CLOSE_ROOT` (with `close/`), both `CLOSE_PACK` files and `CLOSE_SOURCE`, with their proofs and rows, then regenerates and checks. Its line `assert not (repo / CLOSE_ROOT).exists()` stays and now holds by construction. A docstring states the fixture's purpose.
- **PD-7, what does not change.** No other test, constant, helper or assertion in this file. No new committed test: V-4's negative control is a mutation run in a throwaway clone, recorded with its patch (§12). R-1 to R-3 bound the change, and a permanent test of the test would protect no product or delivery condition (2.11 rule 2).

## 6. Real-input set (addendum 2.11 rules 4 to 6)

- **What the fixtures read:** the real checkout, copied whole, whatever `main` holds. Today: no HDE-CRD-0002 evidence. After QA-50: the QA family (`qa_step_logs_manifest.json`, `checks/<check_id>/primary.log`, path proofs, Index and Mirror rows). After the close stage: the close-run family, the close pack and the candidate source (Plan v1.1 WU-PR-07 (a)). All are planned deliverables of approved stages (rule 4(a)); the hosted runner that runs the lane is rule 4(b).
- **The admission table** on the PR head, read where it is defined.
- **Stated limits, not modelled:**
  - The helper removes only the paths R-1 to R-3 name. The close stage's two ledgers (`audit/docdeltas/hde-crd-0002_doc_deltas.md`, `…_drain_targets.md`) are not registered by the updater and no evidence-lane test names them; V-3 includes them as supplementary stand-ins and they broke nothing (§12).
  - A symlinked root is unlinked, not followed. No real input has one, and the updater refuses an aliased CRD root.
- **No emulation (rule 6):** every fixture calls the real updater and, through it, the real harness. Nothing models their behaviour.
- **F-1's input is real:** the two close-pack rows with `crd_id` are what the updater on `main` writes for the close pack, a planned deliverable (rule 4(a)); the stand-in pack only triggers the registration (§16).

## 7. Files and requirement-to-change/test map (approved scope)

| Path | Change (prototype) | Check |
| :- | :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | +57/−26 (1,383 → 1,414 lines): PD-1 helper; R-2 `crd_repo`; R-1 test; R-3 `CLOSE_SOURCE` and `close_repo` | V-1 to V-5 |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-*` | this plan, its diff, later the PR-30 and PR-35 result records | — |

| Requirement (review §4) | Change | Proof | Prototype |
| :- | :- | :- | :- |
| R-1 | `test_absent_admitted_crd_root_publishes_nothing` builds the absent state in its own copy (PD-3, PD-4) | V-1 (root absent); V-2 (root present); V-4 (planted row) | met |
| R-2 | `crd_repo` strips every root in `ADMITTED_CRD_QA` (PD-5) | V-1; V-2 (`test_crd_0002_fixture_root_publishes_beside_crd_0001` passes with the root present, assertions unchanged) | met |
| R-3 with C-1 | `close_repo` strips the root, `close/`, the report, the manifest and the candidate source, with proofs and rows (PD-6) | V-1; V-3 (the four close-run tests pass with all three close-stage inputs present) | met: the four tests pass in V-3 |
| P-1 (acceptance (5) restated) | R-1 in a copy; "the evidence-lane tests do not depend on whether the real checkout holds … its close pack" | V-1 to V-4 | **not met within the limit:** `test_evidence_skeleton.py` depends on the close pack's rows (F-1) |
| V-3 | — | the evidence lane passes with the close stage present | **fails** (F-1); V-3′ passes with the candidate line |
| Limit | one file; the helper in it | `git diff --stat`; PR-40 attribution | met by the diff; it is what blocks P-1 and V-3 |
| Exclusions (instruction §7) | none touched | §12 change-set check; PR-40 | met |

## 8. Implementation sequence for PR-30 (R-1 to R-3; not offered for Proceed)

Recorded so the successor plan can reuse it.

1. **Recover before creating.** Inspect this session's checkout, branches, worktrees, open pull requests and `docs/ephemeral/` for WU-REM-01 work.
2. **Branch** from current `origin/main` on the session's designated branch. If `main` moved past 16ecf95 outside `docs/ephemeral/`, re-run §4 for the test file, the updater's cited lines and `ci.yml` first, and record any difference.
3. **Apply** `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0-prototype.diff` (`git apply --check`, then `git apply`). The file's blob is then 8c368caf3b42 (sha256 fae8ed97df6910a2f241e1b74cae344b113080c89ce1abbd232a7f893e5e03dc, 1,414 lines).
4. **Commit** once: `test(evidence): build absent HDE-CRD-0002 states in copies (HDE-CRD-0002 WU-REM-01, FND-001)`.
5. **Validate** the commit as §10 states.
6. **Publish** the pull request, with the `.github/pull_request_template.md` headings under the `AGENTS.md` content rules.
7. **Result record** `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.0.md`: `PR_CANDIDATE_PUBLISHED`; every check with commands, counts, times and exit codes; the V-2 and V-3 rehearsal outputs and the stand-ins' provenance (P-2 evidence obligations); "In-flight decisions"; nonclaims; then the PR-35 handoff.

**Integration seams:** the updater's CLI (write and `--check`), the copy's updater module (through `_crd_program`) and `ADMITTED_CRD_QA`. No code changes at any seam.

## 9. PR split and merge dependencies

- **One pull request,** one coherent change. No split. If the remedy decision adds the second file, it stays one pull request: both files are evidence-lane tests and the pair classifies to the evidence lane only (§16).
- **Dependencies (P-2):** none on unmerged work. This plan's own pull request (documents only) merges first.
- **Before merge:** PR-35's `MERGE_PENDING`. The Product Owner merges.
- **After merge:** PR-40 by the whole-change IA; on ACCEPT, the same Isis QA-10 reassessment.
- **No release member, governed artifact or evidence regeneration** is in the change.

## 10. Validation PR-30 runs

Environment: CPython 3.12 with CI's install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), the editable install pointed at the checkout under test; `ruby`, `bash` and git; `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), because this container sets vendor, database and GitHub keys. Each throwaway clone has no push remote.

1. **Classifier,** as `ci.yml` calls it, base `origin/main`, head the commit: exit 0, `reason=selected_lanes`, `evidence` only, `changed_tests=false`.
2. **Pre-push check** (`AGENTS.md`): `python tools/ci/prepush_check.py lanes build-notes`, and `python tools/ci/prepush_check.py --path <each changed path> membership`.
3. **V-1** on the commit: `ci/checks/check_env_pins.sh`, then the evidence step of `ci.yml` (lines 221 to 240) verbatim: 7 validators exit 0, and the six pytest files pass with no fewer than 134 tests; the tree is clean afterwards.
4. **V-2** in a throwaway clone of the commit: publish the stand-in QA family (§11), commit it in the clone, classify that commit, then run the evidence step and the release step of `ci.yml` (lines 273 to 343) verbatim. Both pass.
5. **V-3** in a throwaway clone of the V-2 commit: add the close-stage stand-ins (§11), commit in the clone, run the evidence step. It passes.
6. **V-4** in a throwaway clone of the commit: the mutations of §12.4. Each fails as stated; the unmutated test passes.

PR-35 re-runs items 1 to 3 after any correction, and V-2 to V-4 when a correction touches the fixtures or the helper. **V-5** is PR-35's: hosted CI on the current head, evidence lane green, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

## 11. Stand-ins (C-1; instruction §9.2)

Produced only in throwaway clones, only through the harness and the canonical updater, plus authored stand-in files. Every one states it is not QA evidence. Nothing from a rehearsal clone is committed to the repository or pushed.

| Stand-in | Producer | Form |
| :- | :- | :- |
| QA family (V-2) | `writer.publish_crd_check_family(qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT), …)`, run from the clone so `writer.ROOT` is the clone | checks `qa-01-standin` and `qa-02-standin`, each `qa.CheckResult` with status `PASS` from an executed `python -c "raise SystemExit(0)"`, `command_provenance` "WU-REM-01 PR-20 V-2 stand-in in a throwaway clone; not QA evidence", `captured_at_utc` the run time (2026-10-23T17:33:27Z); then `qa.validate_crd_check_family` |
| Candidate source (V-3, T1) | authored | `audit/HDE-CRD-0002_close_candidate_source.json`: `{"change_id":"HDE-CRD-0002","stand_in":"WU-REM-01 PR-20 V-3 stand-in in a throwaway clone; not a close candidate, close pack or QA evidence"}` |
| Close pack (V-3, T2 and T3) | authored, then indexed by the canonical updater's write (`tools/evidence/update_evidence_index.py`), which wrote both path proofs and rows | `audit/HDE-CRD-0002_close_report.md` (a heading and the note); `audit/HDE-CRD-0002_MANIFEST.json` (canonical JSON with the note) |
| Close-run family (V-3, T5) | `writer.publish_crd_close_run_family(config, …)` | checks `close-pack-check` and `evidence-index-check`, as the QA family, provenance "WU-REM-01 PR-20 V-3 stand-in close run in a throwaway clone; not QA evidence" |
| Ledgers (V-3, supplementary) | authored | `audit/docdeltas/hde-crd-0002_doc_deltas.md` and `…_drain_targets.md`, one heading and the note each; unregistered, so not indexed |

The order follows Plan v1.1 WU-PR-07 (b): T1, T2, T3, T5 (2.15: the close-run entrypoint requires the recorded QA family, which V-2 supplies). The stand-in close pack is not writer-produced; the evidence lane checks only its presence, pairing, proofs and rows, no evidence-lane validator parses its content, and the release-lane tools name no close-pack path (searched).

## 12. Prototype record

Run on 2026-10-23 in throwaway clones under the session scratchpad, all cut from the session checkout at 16ecf95. Every clone's push remote was removed; nothing was pushed, and the session checkout was not changed. Each clone ended with an empty `git status --short --untracked-files=all`.

### 12.1 Environment and method

- **Interpreter:** CPython 3.12.3; one venv per clone under test, each with CI's install and the editable install pointed at that clone; pytest 8.4.2; git 2.43.0.
- **Rails:** `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and `PATH` set to the venv and the system; no vendor, database or GitHub key reached any process.
- **Evidence lane:** `python -m pytest --version` and `ci/checks/check_env_pins.sh`, then the evidence step of `ci.yml` (lines 221 to 240) verbatim, then the final step's tree checks (`git diff --check`, `git diff --exit-code`, an empty `git status --short --untracked-files=all`).
- **Release lane:** the release step of `ci.yml` (lines 273 to 343) verbatim, including its admission probe, with `RUNNER_TEMP` a fresh scratch directory.
- **Commits (clone-local):**
  - prototype `b1a4e17` (tree `ebbfeb4f…`), the companion diff applied to 16ecf95;
  - V-2 `e24b50a` on `b1a4e17`: the stand-in QA family, 16 paths (+39/−18): three primaries and their proofs, and the ten skeleton files the updater regenerated; the Index gains three HDE-CRD-0002 rows;
  - V-3 `dd2673f` on `e24b50a`: the close stage, 21 paths (+55/−18): the close-run family (two primaries and proofs), the close report and manifest with their proofs, the candidate source, the two ledgers and the regenerated skeleton; the Index then holds seven HDE-CRD-0002 rows (QA family 3, close-run 2, close pack 2); the candidate source and the ledgers have none;
  - V-3′ `ae3ca6f` on `dd2673f`: F-1's candidate line only (§16), outside approved scope, substantiation only.
- **Scripts** (scratchpad `scripts/`, transient; this section and §11 reproduce them): `evidence_lane.sh`, `release_lane.sh`, `standin_common.py`, `v2_standin.py`, `v3_standin.py`, `r0_reproduce.sh`, `v4_mutate.py`, `v4_negative.sh`.

### 12.2 Classifier and pre-push check

| Run | Result |
| :- | :- |
| Classifier as `ci.yml` calls it, base 16ecf95, head `b1a4e17`, `pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=1;lanes=evidence`; `changed_tests=false`; 0 changed-test targets |
| `prepush_check.py --base 16ecf95 --head HEAD lanes build-notes` on `b1a4e17` | PASS; lanes as above; PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md`, 454,052 bytes, sha256 2759c4da…; "repository unchanged"; exit 0 |
| `prepush_check.py … --path tests/evidence/test_evidence_index_missing_state.py membership` | PASS; release `1.3.0`, roster 45, `release_id` 77204764…; not-member; exit 0 |
| Classifier, base `b1a4e17`, head `e24b50a` (what a QA-evidence PR changes) | exit 0; `paths=16;lanes=evidence,release`; `changed_tests=false` |
| Classifier, base `e24b50a`, head `dd2673f` (what a close PR changes) | exit 0; `paths=21;lanes=evidence,release`; `changed_tests=false` |
| Classifier, base `dd2673f`, head `ae3ca6f` (F-1's candidate line alone) | exit 0; `paths=1;lanes=evidence`; `changed_tests=false` |
| `classify_paths` on both test files together | `evidence` only |

### 12.3 Runs

| ID | Head and state | 7 validators | Six pytest files | Release lane | Tree after |
| :- | :- | :- | :- | :- | :- |
| B0 | 16ecf95, unmodified (root absent) | all exit 0 | 134 passed, 1,046.03 s | not run (not selected) | clean |
| R0 | `e24b50a` (stand-in root) with 16ecf95's test file (blob bff9a6b0f34f) | — | the six FND-001 tests only: **2 failed, 4 errors** (33.82 s): `test_absent_admitted_crd_root_publishes_nothing` and `test_crd_0002_fixture_root_publishes_beside_crd_0001` FAILED; the four `close_repo` tests ERROR at setup | — | clean after restoring the file |
| V-1 | `b1a4e17`, root absent | all exit 0 | **134 passed**, 1,040.53 s | not selected | clean |
| V-2 | `e24b50a`, stand-in QA family | all exit 0 | **134 passed**, 1,027.26 s | **pass:** manifest check exit 0; 79 release tests passed; attestation built (exit 0) and verified (exit 0); clean tree; 168 s | clean |
| V-3 | `dd2673f`, plus the close stage | all exit 0 | **1 failed, 133 passed**, 1,019.77 s: `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity`, `AssertionError: assert {'crd_id'} == set()` at line 539 | pass (supplementary; not V-3's condition): 79 passed; built and verified; 176 s | clean (the lane stopped at the failure; `git status` checked before the V-3′ commit) |
| V-3′ | `ae3ca6f` (V-3 plus F-1's candidate line) | all exit 0 | **134 passed**, 1,032.48 s | not run (the line changes no release input) | clean |
| V-4 | `b1a4e17`, the R-1 test mutated in a clone | — | R-1 test alone: unmutated **1 passed**; planted Index row **1 failed** at the Index assertion; supplementary published root **1 failed** at the loader assertion | — | clean after each restore |

- **Lane time (instruction §9.4):** B0 and V-1 ran alone on the container, so they compare: 1,040.5 s with the change against 1,046.0 s without it. The added write and check per fixture use is within run-to-run noise. V-2, V-3 and V-3′ ran beside other jobs, so their times do not compare.
- **In V-3, the four close-run tests passed:** R-3 with C-1 works. The one failure is outside this file.

### 12.4 V-4 mutations (applied by `v4_mutate.py`, restored by `git checkout`)

- **V-4, planted Index row** (the approved control), inserted after `_strip_from_copy(repo, "audit/qa/hde-crd-0002")`:

  ```python
      planted = json.loads((repo / "docs/evidence/INDEX.json").read_bytes())
      planted.append({"artifact_key": "audit.qa.hde_crd_0002.qa_step_logs_manifest", "discovered_physical_path": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "role": "manifest"})
      (repo / "docs/evidence/INDEX.json").write_text(json.dumps(planted, sort_keys=True, separators=(",", ":")) + "\n")
  ```

  Result: `AssertionError: assert not [{'artifact_key': 'audit.qa.hde_crd_0002.qa_step_logs_manifest', …}]` at the Index assertion (line 1011 of the mutated file); 1 failed in 9.15 s.
- **Supplementary, published root,** inserted after `assert not (repo / "audit/qa/hde-crd-0002").exists()`:

  ```python
      _success(_crd_program(repo, SECOND_CRD + "writer.publish_crd_check_family(second, (observed(),), captured_at_utc=timestamp)\n"))
  ```

  Result: the copy's loader program exits 1 at its assertion; the rows it printed include HDE-CRD-0001's eleven and HDE-CRD-0002's two, which also shows the copy keeps HDE-CRD-0001's family beside the absent root (PD-3); 1 failed in 9.30 s. A first placement, before the existence assertion, was caught by that assertion instead, so the mutation was moved to exercise the loader assertion.

## 13. Interface contracts (instruction §8)

- **QA-50 and later QA-evidence pull requests:** publishing under `audit/qa/hde-crd-0002/` through `publish_crd_check_family` leaves the evidence lane green with no change to this file (V-2). That is the business-case measure.
- **The close stage (S21):** the close-run family, the close pack and the candidate source land without breaking the evidence lane. **Not met within the limit** (V-3; F-1); met with F-1's candidate line (V-3′).
- **The admission table:** R-2 reads `ADMITTED_CRD_QA`; the updater's table is unchanged, and `test_admitted_crd_table_is_explicit_and_matches_the_harness_roots` still pins it.

## 14. Security and migration

- Test code only. No secret, credential, network or production surface. The fixtures' subprocesses run under the file's closed-rails `ENV`; every local run used `env -i`, so the container's vendor, database and GitHub keys reached no child. No record holds a key value.
- The Codex code review is in the chain; the Codex security review is not (addendum 2.3).
- **Migration:** none. **Rollback:** the Product Owner reverts the squash commit; no member changes, so no manifest refresh.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| A strip removes more than intended and hides a regression | Only the named paths and their direct rows leave; the updater regenerates and checks the copy (PD-1, PD-2); V-1 keeps all 134 tests; V-4 shows the absent-root property still fails when violated |
| Lane time grows | Measured (§12.3): no measurable change |
| `main` moves before implementation | §8 step 2 re-measures |
| A Codex finding on a constructed input | 2.11 rule 7 (traced path and stated limit); rule 8 after two same-class rounds; a P1 on a real input fixed under 2.14 |
| A hosted failure that is not this unit's, such as FND-024 (the PR35-C1 flake) | PR-35's base-red handling; FND-024 stays with its recorded owner |
| The remedy decision changes R-1 to R-3 | The successor plan re-runs the affected checks; §5 to §12 are reused only where the decision leaves them valid |
| Interruption | Resume in this session from this record; rehearsals only in throwaway clones, discarded and re-cut on failure |

## 16. Boundary finding F-1 and observations

### F-1 — A second evidence-lane test rejects `crd_id`, so the close-pack pull request fails the evidence lane

| Field | Value |
| :- | :- |
| Where | `tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity` (lines 511 to 594 at 16ecf95; blob 057b4ae973ba). The evidence lane runs this file (`ci.yml` line 236) |
| What it does | Reads the real checkout's `artifacts/evidence_index.jsonl` and, for every row, asserts `key_set - (required_fields \| optional_fields) == set()`, with `optional_fields = {"epic_id", "notes", "record_type", "schema_version", "tokens"}`. `crd_id` is not in the set |
| The real input | `_crd_close_pack_entries` (`tools/evidence/update_evidence_index.py` line 4046) writes each CRD close-pack Index row with `"crd_id": crd_id`, and the Mirror row carries it. HDE-CRD-0002's close pack is a planned deliverable (Plan v1.1 WU-PR-07 (a)), so the input is real (addendum 2.11 rule 4(a)). The stand-in pack only triggers the registration; a writer-produced pack gets the same two rows |
| Observed | V-3: 1 failed, 133 passed; `AssertionError: assert {'crd_id'} == set()` at line 539. In the V-3 Mirror, 2 of 627 rows carry `crd_id` (the close report and manifest), none carries both `crd_id` and `epic_id`. V-2's Mirror has no `crd_id` row: QA-family and close-run rows carry none |
| Canon | HDE Schemas and Artifacts §8.3 "Allowed top-level keys and unknown-key rejection" lists `crd_id` among the optional metadata keys and states: "Before the first affected CRD enters QA, the Machine Mirror schema and every serializer or validator enforcing this allowed-key set MUST accept crd_id, enforce the epic_id/crd_id mutual-exclusion rule, and preserve valid historical and active epic_id records." `ci/checks/check_mirror_schema.sh` already does (`crd_id` allowed; `EPIC_CRD_EXCLUSIVE`); this test does not. Its last change (75b3026, #529) predates the CRD admission (1d2c834) and the close-pack rows (8b73b57) |
| Why R-1 to R-3 cannot fix it | The test is in another file, and the review's limit is "No other file changes". Nothing in the one file changes what this test reads |
| Approved objectives affected | P-1's clause "the evidence-lane tests do not depend on whether the real checkout holds … its close pack" and V-3's pass condition; the business case's close-pack benefit (§3). Through §8.3's "before … enters QA" duty it also bears on S22's dependants at QA entry, which the QA-10 reassessment owns. V-2, V-1 and V-4 are unaffected |
| Smallest delta, substantiated | Add `"crd_id",` to that test's `optional_fields` (one line). V-3′ passes with it: 7 validators exit 0, 134 passed. The pair of files classifies to the evidence lane only, with no changed-test targets. §8.3 also asks that a validator enforcing the key set "enforce the epic_id/crd_id mutual-exclusion rule"; a second line in the same test, asserting that no row holds both keys, would do that and changes no outcome on any row measured (none holds both). Whether to include it is the proposal author's |
| Alternatives | (a) Extend WU-REM-01 by that one line (or two), one pull request, V-3 unchanged — what V-3′ shows. (b) Keep WU-REM-01 to one file, narrow V-3 and P-1, and fix the skeleton test in a separate remedy before the close stage; one more vehicle, and §8.3's "before QA" duty stays unmet until then. (c) Stop the updater writing `crd_id` on close-pack rows: contrary to §8.3, and excluded (no updater change). The PR-20 author's recommendation is (a); the decision is Isis's |
| Route | Instruction §14: changes to the approved remedy belong to Isis through ESC-30 and ESC-40, not to RS-20. ESC-30's input is an "actual QA-10 readiness finding … or equivalent stage-owned evidence"; the originating finding stays QA-10 FND-001 (triage §3), and this section is the delivery-stage evidence. Not a canon conflict (§19); not a Specification change (S21 and S22 intents stand) |
| Return | After the remedy decision and whatever re-issue it routes (for example a new instruction version through PR-10), PR-20 in this WU-REM-01 session writes the successor plan. The final return is unchanged: the same Isis QA-10 reassessment after PR-40 ACCEPT |

### Observations (no action in this unit)

- **OBS-1, the other evidence-lane tests are otherwise independent.** Besides F-1, the tests that copy or read the real checkout without stripping it passed with the QA family present (V-2) and with the close stage present (V-3): 133 of 134, the one being F-1.
- **OBS-2, the ledgers.** The close stage's two ledgers are not registered by the updater; they changed no Index row and broke nothing (V-3).
- **OBS-3, the release lane.** It passed with the QA family (V-2) and with the close stage (V-3, supplementary). Its tools name no close-pack path.
- **OBS-4, an identifier collision.** "FND-001" names QA-10's finding (triage §3) and, separately, the WU-OPS-01 receipt's own finding (addendum 2.22). This plan always means QA-10's. Records that cite one should name its source.
- **OBS-5, container speed.** This container ran the six files in about 1,040 s; the proposal recorded 827.7 s on another. Hosted times differ again; PR-35 records the hosted run.

## 17. Carried items and owners

| Item | Owner |
| :- | :- |
| F-1: the change to the approved remedy, or its rejection | Thoth (ESC-30) proposes; Isis (ESC-40) decides |
| Any re-issued work-unit instruction that the decision routes | The whole-change IA (PR-10), if so routed |
| The successor plan | PR-20, in this WU-REM-01 session |
| Publishing addendum 2.23 (and any later remedy addendum) into PF10 | Product Owner |
| CR-9 (path proofs under the Ops evidence root), unaffected | Isis, at IA-30 |
| FND-024, the PR35-C1 flake risk on QA-evidence pull requests | As recorded in the triage |
| The business-case measure (§3) | The first QA-evidence pull request, or the QA-10 reassessment |
| The QA-10 reassessment of S22 and its dependants | Isis, after this unit's PR-40 ACCEPT |

## 18. Instruction coverage

| Instruction | Where this plan meets it |
| :- | :- |
| §4 R-1, R-2, R-3, Limit | §5; §7; §12 (met by the prototype) |
| §4 restated acceptance (P-1) | **Not met within the limit**: F-1 (§16) |
| §5 baseline | §4 |
| §6 bounded files; expected unchanged | §7; §12 |
| §7 exclusions | §7; §11; §14 |
| §8 interface contracts | §13 |
| §9.1 design choices | §5 |
| §9.2 stand-ins | §11 |
| §9.3 prototype | §12 |
| §9.4 lane time | §12.3 |
| §9.5 baseline re-check | §4 |
| §10 V-1 to V-5 | V-1, V-2, V-4 pass; **V-3 fails** (F-1); V-5 not reached |
| §11 migration, security, real inputs | §14; §6 |
| §12 PR-20 duties | Met, except `AWAITING_PO_PROCEED`, which §12 allows "only for a complete plan within this scope" |
| §13 recovery | §15; §17 |
| §14 rescope | Triggered: "a needed change outside the one test file" and "a stand-in rehearsal that fails for a reason R-1 to R-3 cannot fix". Routed by its rule for "changes to the approved remedy itself" (§16) |
| §15 unresolved items | §17 |
| §16 canon-conflict register | §19 |

## 19. Canon-conflict register

Carried unchanged: CR-1, CR-2 and CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (a) (IA through RS-20); CR-7 and CR-8 APPROVED (a) each (Product Owner); CR-9 PROPOSED, not yet reviewed (Isis, IA-30), unaffected. **No new conflict.** F-1 is a test that has not caught up with canon: HDE Schemas and Artifacts §8.3 states the rule plainly, and the updater and the Mirror schema check already follow it. Nothing in canon conflicts.

## 20. Obligations carried to the successor plan

When the remedy decision returns, the successor plan keeps, for PR-30 and PR-35, what §8 to §10 state, with any approved addition:
- **PR-30** (this session, after a Proceed for that exact successor plan): recover first; change only the approved files; run §10; commit once, publish, write and push the result record; return `PR_CANDIDATE_PUBLISHED` and hand off to PR-35 in its own session.
- **PR-35** (its own session): Codex code-review findings under 2.11 rule 7 and 2.14 (a P1 on a real input is fixed; declining a P1 or a security finding goes to the Product Owner first; rule 8 after two same-class rounds); no security review (2.3); coherent corrections with §10 re-run; V-5 and mergeability, base-red failures handled as such; `MERGE_PENDING` without merging.
- **PR-40** (the whole-change IA, after Nathan's merge): R-1 to R-3 (and any addition) on the merged head; V-1 to V-5 from the records and the hosted run; the measure "not yet measurable", with V-2 and V-3 as its proxy; on ACCEPT, the same Isis QA-10 reassessment.
- **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change; no HDE-CRD-0002 QA evidence, close pack or candidate source produced or committed.

## 21. TypeSafe reading for the receiving session (ESC-30, F-1)

Action sent (v8.2): "Diagnose, as the continuing remediation author, one delivery-stage finding against a remediation you proposed and the reviewer approved: while planning the approved one-file test fix, a rehearsal in a throwaway clone showed that a second evidence test file rejects a metadata key that canon allows once the change's close pack is indexed, so the approved remedy cannot meet its own acceptance check within its one-file limit; validate the finding against the approved remedy, canon and the rehearsal records, and author one bounded successor remediation proposal naming the smallest test change (a one-line candidate already rehearsed), its delivery owner and verification. It is a Markdown record only: no code is written and no live run occurs; an independent remediation review and the work unit's re-planning follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.01 (confidence 0.91); rung probabilities low 0.00, medium 0.06, high 0.87, extra high 0.07, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.07, Opus 5.5 0.74, Sonnet 5.5 0.19, Haiku 5.5 0.00 (confidence 0.65). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.004, Fable 5.1 at high 0.061, Fable 5.1 at extra high 0.005, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.044, Opus 5.5 at high 0.644, Opus 5.5 at extra high 0.052, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.011, Sonnet 5.5 at high 0.165, Sonnet 5.5 at extra high 0.013, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-23T18:14:02Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T18:14:02Z; HTTP 200 in 0.62 s; 5500 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Records.** Run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review` (as the readiness record's ESC-30 reading used), before this record was saved. The Notion row was not written (PR-20 handoff rule; addendum 2.1). Nathan's pick for ESC-30 is not stated; his pick for this PR-20 session is not stated (its reading is the instruction's §19).

**Surface advice:** run ESC-30 in the continuing Thoth session for HDE-CRD-0002 remediation, or a top-level Claude Code cloud session Nathan creates for that role, on `amthorn78/glow-hdengine-v2` with Notion read access.
- **Reads:** this plan (§16 and §12), its prototype diff, the instruction, the remediation review and proposal, the 2.23 record, the QA-10 triage, `tests/evidence/test_evidence_skeleton.py`, `tools/evidence/update_evidence_index.py` at `_crd_close_pack_entries`, `ci/checks/check_mirror_schema.sh`, and `docs/pfcanon/` (HDE Schemas and Artifacts §8.3; current PF10).
- **Re-running V-3 or V-3′ (optional):** a throwaway clone with CI's install, Python 3.12 and closed rails through `env -i`; each evidence-lane run takes about 17 minutes on 4 CPUs.
- **Writes:** only its proposal under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this plan's pull request is merged first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | `GCFPE-USE-HDE-CRD-0002-PR-20-20261023-WU-REM-01-01` |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-REM-01 (S22, with S21's close-run tests) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-REM-01 PR engineering session / PR-20 |
| capture time | 2026-10-23T18:20:00Z |
| execution identity | https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5 |
| result | BLOCKED on F-1; next ESC-30 |
| inherited usage | instruction v1.0 §20 (`GCFPE-USE-HDE-CRD-0002-PR-10-20261023-WU-REM-01-01`); review v1.0 (`GCFPE-USE-HDE-CRD-0002-ESC-40-20261023-FND-001-01`); proposal v1.0 (ESC-30, FND-001 proposal 1) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at 16ecf95 (`docs/pfcanon/` last changed by 39122b7, PF10 v13.7.5).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, content and result states | PR-20 — Create Detailed PR Implementation Plan — 100926.1, read in full ("Execute" 1 to 10, "Required result": a boundary finding returns "a complete planning draft with the exact finding and native rescope route"); PR-30 — PR Implementation Proceed — 100926.1, read in full |
| The route for a change to the approved remedy | The instruction §14 (in-flight canon for this change); ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, read in full ("Required inputs", "Execute", "Result routing") |
| The approved remedy and its overlay | `docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md` §1 to §8 and the 2.23 record, read in full; the proposal, read in full; the instruction, read in full |
| PF10 authority and the overlays in force | PF10-HDE-Build-Notes v13.7.5: front matter "Precedence, versioning, and scope" (rules 1 to 9) and the Addendum Index; 2.1 (TypeSafe reading), 2.3 (reviewer chain), 2.5 (WU-PR-02 accepted-final), 2.11 (business case; real inputs; finding disposition; repeated class), 2.14 (P1), 2.15 (the close-run family) and 2.18 (no ceiling), each read in full |
| Change authority; the Proceed | HDE Governance (`PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 "Change authority and exact-artifact lineage", read in full (the detailed per-PR plan's owner is the dedicated PR session; the Product Owner's `PR Implementation Proceed` is its approval; merges are Product Owner actions) |
| The Mirror key set (F-1) | HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.3 "Machine Evidence Index — JSONL mirror": "Format (canonical JSONL)", "Minimum record schema", "Bundle-aware extension" and "Allowed top-level keys and unknown-key rejection", read in full |
| The CRD QA root | HDE Schemas and Artifacts §8.17 "Live QA evidence layout", its "Change-container identity (normative)" passage, read in full |
| CI lane discipline | Plan Templates (`PF27-Canon-Plan-Templates-v2.0.5.md`) "CI lane classification and automated budget-control discipline", read in full. The change stays in the evidence lane it already runs in and protects a current delivery condition (QA and close-pack evidence publication), not an administrative closeout control |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails; pytest readiness; pre-push check; "Governed evidence rules" (sole writer; no hand-editing); QA output placement; "Code review guidelines" (real-input rule); "PR descriptions"; "Evidence attribution, currentness and distinct decisions" |
| In-flight documents | Specification v1.1-approved (S22, Constraints, QA requirement, Distillation row); Plan v1.1 §3 to §5 and §7 (common terms, WU-PR-02, WU-PR-07); QA-10 triage §3 and readiness §5 |

Canon searched (`git grep` on `origin/main -- docs/pfcanon/`) for "Change-container identity", "CRD QA root", `crd_id` (with its escaped form `crd\_id`) and the §8.x headings: `crd_id` appears in HDE Schemas and Artifacts §8.3 (the passage above) and in HDE Mechanics Guide's `HarnessConfig` lines, which do not bear on Mirror keys. PF10 v13.7.5 searched for `S22`, `FND-001`, `WU-REM-01`, `test_absent_admitted`, `accepted-final`, `hde-crd-0002` and `close_candidate_source`:
- `WU-REM-01` and `test_absent_admitted`: no match.
- Hits in 2.5, 2.6, 2.14, 2.16, 2.19, 2.20, 2.21 and 2.22, read at those lines: none governs these tests' behaviour once QA creates the root.
- 2.15, read in full: it introduces the close-run family (`audit/qa/<change-dir>/close/<check_id>/primary.log` with path proofs, written only by the updater's close-run entrypoint, which requires the recorded QA family to exist). R-3 strips it with the root, and V-3 publishes its stand-in after the QA family.
- 2.22's `FND-001` is the WU-OPS-01 receipt's own finding, a different item from QA-10's FND-001 (OBS-4).

2.23 is the record of the approved remedy, pending publication.
