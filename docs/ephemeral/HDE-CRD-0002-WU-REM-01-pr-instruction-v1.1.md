---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-REM-01-PR-INSTRUCTION
artifact_version: "1.1"
artifact_state: INSTRUCTION_READY
predecessor: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob d89d1dc9991b; sha256 1661b2d54388483e8e371a32d9d3ef91b75da293e6b7640243a0db3eea7641b9; #709, squash 16ecf95). Superseded by this version for WU-REM-01 and kept unchanged as history
supersession_reason: the approved remedy was amended (remediation review v1.1, APPROVE; HDE Build Notes addendum 2.24), after PR-20 plan v1.0 returned BLOCKED on F-1. v1.0's §4 Limit, §6 bounded files, §7 exclusions, §10 verification and business case no longer match the remedy
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-01
work_unit_title: "Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation; S22, with S21's close-run tests and close-pack rows)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (INITIAL_APPROVE). Neither is edited
applicable_overlays: (1) Specification delta 01 (addendum 2.20); (2) Implementation Plan delta 01 v1.1 (addendum 2.19); (3) the FND-001 remediation as amended — addendum 2.23 (review v1.0, APPROVE_AS_CHANGED with C-1), amended by addendum 2.24 (review v1.1, APPROVE; CR-10 APPROVED (a)); (4) addendum 2.18 (no cost ceiling); (5) addendum 2.11 rules 1, 2 and 4 to 8 as 2.18 narrows them; (6) addendum 2.14 (P1 findings); (7) addendum 2.3 (Codex security review deprecated)
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S21, S22 and Constraints "QA evidence admission", with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md, approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 (WU-PR-02 acceptance (5) as P-1 restates it; WU-REM-01 as amended P-2 adds it), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1; blob 5103fe29d588)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md (APPROVE, "ASK OK."; CR-10 APPROVED (a); Isis; blob 126330b8f6b9; #712, squash c8d8bc3). Predecessor v1.0, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.0.md (APPROVE_AS_CHANGED; blob e100bf4eba08; #708), superseded for WU-REM-01's scope, limit, exclusions, verification and business case
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md (Thoth; blob 12fcbb30585f; sha256 2aa11d33e3b0cd0332aa0471584e3b0662dc5ab8f796bbf2c9c5fe6d7e07474f; #711, squash d524f00). Its §6 is the approved overlay, approved verbatim
remediation_addenda: PF10 v13.7.6 §2.23 and §2.24, published by #713 (3b21327). Their records: docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23; blob 248c17e7e513) and docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.1.md (2.24; blob 13baa7812398)
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (FND-001; Reality Audit RA2-22; blob dac6d1a79de8)
delivery_stage_evidence: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0.md (PR-20, BLOCKED on F-1; blob 9009107b3be8; #710, squash f5c7c7f) with docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0-prototype.diff (blob 2a2895a589fd; sha256 1203de91f5aa3eb3d0ad9957f90ee6945ec54248886927fc609c49b72c56216e)
originating_stage_and_return: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, NOT_READY (docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md; blob f6d7ff018ce7). Return: the same Isis QA-10 reassessment of S22 and its dependants, after this unit's PR-40 ACCEPT
accepted_final_not_reopened: WU-PR-02 (addendum 2.5; lineage review v2.0, ACCEPT; blob 4512db789c82) and WU-PR-07 (addendum 2.16)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (blob b39ac9f276db)
business_case_ref: proposal v1.1 §6.5, approved by review v1.1 §5 and addendum 2.24
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
CURRENT_PF10_MARKDOWN_LINK: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md (473,130 bytes; sha256 ee6d55b57b3b922116363dd914264333cf3566c4856819e2a139ed50f7a6604e; last addendum 2.24)
ACTIVE_PF10_ADDENDA_LINKS:
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.3 (Codex security review deprecated)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.5 (WU-PR-02 accepted-final) and §2.16 (WU-PR-07 accepted)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.11 (business case; real inputs; finding disposition; repeated finding class), as §2.18 narrows it
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.14 (a P1 finding is addressed until resolved)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.15 (the CRD close-run family)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.18 (no cost ceiling; rule 5, PR-40 records the measure)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.19 and §2.20 (Plan delta 01; Specification delta 01)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.23 and §2.24 (the remedy, as amended)
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state of 2026-10-12T02:29:33.739Z, re-fetched in this invocation and unchanged since this session read it in full for v1.0; "Execute", "Semantic readiness", "Required result" and "Next step and recovery" re-read)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-23T21:00:00Z
repository_baseline: origin/main 3b21327 (#713). Every repository fact in §5 was measured at this head. Outside docs/ephemeral/ and docs/pfcanon/, no file changed between bd7366a (v1.0's baseline) and 3b21327; docs/pfcanon/ changed only by PF10 v13.7.5 → v13.7.6
receiver: the dedicated HDE-CRD-0002 WU-REM-01 PR engineering session (https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5; session_disposition CONTINUING_DEDICATED_ASSIGNMENT, as review v1.1 §7 and plan v1.0's role_session_ref name it)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba), for the successor plan
canon_conflict_register: CR-1 to CR-8 carried, decided; CR-9 carried PROPOSED, unaffected; CR-10 carried APPROVED (a) (§16); no new entry
---

# HDE-CRD-0002 WU-REM-01 — PR Work-Unit Instruction v1.1

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one current PR instruction for WU-REM-01. It supersedes v1.0 because Isis approved Thoth's amended remedy (review v1.1, addendum 2.24).

- **Why the remedy changed.**
  - **F-1:** PR-20's rehearsal of the one-file remedy found that a second evidence-lane test rejects `crd_id` once HDE-CRD-0002's close pack is indexed.
  - **F-2:** Thoth's diagnosis found that the QA harness rejects the same key. That turns four Epic acceptance-map viabilities from PASS to FAIL_TOOLING and fails a qa-lane test.
  - Both defects have one cause: two validators of the Index and Mirror key set do not accept `crd_id`, which HDE Schemas and Artifacts §8.3 allows.
- **The unit now** changes three files (§4, §6):
  - `tests/evidence/test_evidence_index_missing_state.py` (R-1 to R-3 with C-1, unchanged);
  - `tests/evidence/test_evidence_skeleton.py` (R-4, new);
  - `tools/qa/qa_harness.py` (R-5, new).
- **The proof** is V-1 to V-5, now across the evidence, qa and release lanes, plus an Epic viability comparison (§10).
- **What carries over.** PR-20's plan v1.0 and its prototype diff remain valid for R-1 to R-3 and may be reused (§9).

This instruction issues the approved remedy into one planned work unit. It does not approve a plan, give a Proceed, implement, merge or decide QA. WU-PR-02 and WU-PR-07 are not reopened. Instruction v1.0 and plan v1.0 stay unchanged as history; plan v1.0's BLOCKED result and its F-1 evidence are not erased.

## 2. Identity and lineage

| Item | Value |
| :- | :- |
| Unit | WU-REM-01, a PR unit in the Distillation phase. Amended P-2 places it in Plan v1.1 §7 after WU-OPS-01 and before QA-10 readiness |
| Approved bases (immutable) | Specification v1.1 with delta 01; Implementation Plan v1.1 with its review v1.1 and Plan delta 01 v1.1 |
| Remediation overlay | Proposal v1.1 §6, approved verbatim by review v1.1; PF10 §2.24, which amends §2.23 |
| Originating finding | Triage §3 FND-001, with its required resolution evidence (1) to (3) |
| Delivery-stage evidence | Plan v1.0 §12 and §16 (F-1); proposal v1.1 §3 to §5 (F-1 and F-2) |
| Return owner | Isis, QA-10 reassessment of S22 and its dependants |
| PR lineage owner | This IA (PR-10 now, PR-40 after the merge) |
| `PR_RETURN_PHASE` | Not applicable: WU-REM-01 has no Proceed and no pull request |

## 3. Unit selection and dependency state

- **Selected because:** review v1.1 routes the amended remedy to PR-10 for instruction v1.1 (its `next_prompt`; §2.24 `return_phase`).
- **Dependencies (amended P-2):** "none on unmerged work; it lands before QA-20". All of Plan v1.1 §7's other units are accepted (§2.22). #712 and #713 are merged.
- **Order after this unit:** WU-REM-01 accepted (PR-40), then Isis's QA-10 reassessment, then QA-20 if READY_FOR_QA.

## 4. Required behaviour (approved overlay; §2.24 "Required behaviour")

**R-1, the absence test** (`tests/evidence/test_evidence_index_missing_state.py`; unchanged from §2.23). "Replace the real-checkout absence test with one that builds the absent state in a copy. It removes `audit/qa/hde-crd-0002/` and its Index rows, regenerates and runs `--check` through the canonical updater, then asserts no HDE-CRD-0002 row from `_load_crd_qa_entries([])` and none in the Index under the root. It does not read whether the real checkout holds the root."
- The test replaced is `test_absent_admitted_crd_root_publishes_nothing` (lines 977–984).
- The loader must be read from the **copy's own updater**. `tools/evidence/update_evidence_index.py` binds `ROOT = Path(__file__).resolve().parents[2]` (line 28), so an in-process import reads the real checkout (§5.3).

**R-2, the `crd_repo` fixture** (same file; unchanged). It "builds the pre-first-publication state for every root in `ADMITTED_CRD_QA`: it removes each root and its Index rows, then regenerates and checks through the canonical updater". The existing assertions of `test_crd_0002_fixture_root_publishes_beside_crd_0001` stay. Ten tests use the fixture (§5.2); none of their assertions changes.

**R-3 with C-1, the `close_repo` fixture** (same file; unchanged). It "removes `audit/qa/hde-crd-0002/` (including `close/`), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and `audit/HDE-CRD-0002_close_candidate_source.json`, with their path proofs and Index rows, from the copy, then regenerates and checks through the canonical updater". The four close-run tests keep their assertions.
- Index rows leave before the updater runs. The updater refuses a close-pack row whose file is absent (`CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`) and a half-present pair (`CRD_CLOSE_PACK_INCOMPLETE`) (§5.3).

**R-4, the Mirror skeleton test** (`tests/evidence/test_evidence_skeleton.py`; new). "`test_mirror_schema_and_parity` accepts `crd_id` as an optional top-level Mirror key. Nothing else in that file changes."
- Today its `optional_fields` (lines 526–532) is `{"epic_id", "notes", "record_type", "schema_version", "tokens"}`. Line 539 asserts `key_set - (required_fields | optional_fields) == set()` over the real Mirror (§5.4).

**R-5, the QA harness** (`tools/qa/qa_harness.py`; new). "The harness's evidence-graph validation accepts `crd_id` as an optional key on Human Index and Machine Mirror rows. The required keys, the other metadata checks, the strict Epic predicates and the refusal of CRD viability are unchanged."
- The two sets are `_MIRROR_OPTIONAL_FIELDS` (line 230) and `_HUMAN_INDEX_OPTIONAL_FIELDS` (line 233). They are used by `_mirror_record_error` (line 660) and by `_load_evidence_graph`'s unknown-field check (lines 855–864) (§5.5).

**Stated limit (CR-10, APPROVED (a)).** R-4 and R-5 accept `crd_id` only. They add no check for a row carrying both `epic_id` and `crd_id`. No such row can reach them:
- the sole writer refuses it (`update_evidence_index.py:3782–3784`, pinned by `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together`, line 1238 of the R-1 to R-3 file);
- `ci/checks/check_mirror_schema.sh` rejects it (`EPIC_CRD_EXCLUSIVE`, lines 106–107) on every evidence-lane run.

The same reasoning (addendum 2.11 rule 5) means R-5 adds no type check for `crd_id`'s value: its only producer is the sole writer, which takes it from `ADMITTED_CRD_QA`. Adding `crd_id` to `_STRING_METADATA_FIELDS` (line 247) would change "the other metadata checks", which R-5 keeps unchanged.

**Limit.** "No file outside the three changes." A shared helper, if any, stays in the file that uses it.

**Restated acceptance (P-1, unchanged).** "an absent admitted HDE-CRD-0002 root publishes nothing, proven in a copy of the checkout from which that root and its Index rows are removed; the evidence-lane tests do not depend on whether the real checkout holds the HDE-CRD-0002 QA root, its close-run family, its close pack or its close candidate source".

**No new committed test is required for R-4 or R-5** (proposal §6.2). R-4 is itself a test, and V-3 shows its effect. For R-5, V-3 (b) shows the effect. Once the close pack is on `main`, the qa lane's `test_current_acceptance_inputs_are_strictly_viable` exercises it on every qa-lane run. A further test is PR-20's choice, and only for a condition these leave unprotected (addendum 2.11 rule 2).

## 5. Current repository and reference baseline (measured at `3b21327`)

### 5.1 Files and identity

| Path | Lines | Blob | sha256 | Release member |
| :- | :- | :- | :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | 1,383 | `bff9a6b0f34f` | `fb710617856b629ac69218230f5d4db02f186c94717a82dcc87cb7451bb95e79` | no |
| `tests/evidence/test_evidence_skeleton.py` | 656 | `057b4ae973ba` | `4221cc13d391675ddcfe2e79a20751124ccfe72ba2af7c0496c3a921f769bcdd` | no |
| `tools/qa/qa_harness.py` | 4,011 | `4484408aa713` | `243e2bac0221e8e941e6316663cd9a002576c36c13abbfa84408014759e7ac5c` | no |
| `tools/evidence/update_evidence_index.py` (unchanged by this unit) | — | `ad441edbea3c` | `fc35ff8c8eef9958a87b255e3b1fc878ed60a6c3d3a8cf43dd3a99123a99ad55` | no |
| `.github/workflows/ci.yml` (unchanged by this unit) | — | `3836bad11c39` | `d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b` | no |

All five equal the bytes that plan v1.0 (16ecf95) and proposal v1.1 (f5c7c7f) measured. "Release member" was checked as 0 matches of each path in `catalog/manifest.json`.

### 5.2 The R-1 to R-3 file

These facts are unchanged from v1.0 §5 and were re-confirmed by plan v1.0 §4.

- **Constants:**
  - `ROOT` (14); `IGNORES` (15–17); closed-rails `ENV` (18–27);
  - `CRD_ROOT = "audit/qa/hde-crd-0001"` and `CRD_KEY` (28–29);
  - `CRD_FIXTURE_PROGRAM` (30–58), which runs inside the copy and asserts `writer.ROOT == Path.cwd()`;
  - `SKELETON` (59–70);
  - `CLOSE_CRD`, `CLOSE_ROOT = "audit/qa/hde-crd-0002"`, `CLOSE_PACK` (1249–1251);
  - `CLOSE_FIXTURE_PROGRAM` (1252–1261).
- **Helpers:** `_run` (73), `_success` (87), `_checks` (91, six validators), `_snapshot` (103), `_crd_program` (347), `_whole_tree_state` (354), `_close_program` (1263), `_index_rows` (1278).
- **The three loci:**
  - L-1 `test_absent_admitted_crd_root_publishes_nothing` (977–984);
  - L-2 fixture `crd_repo` (317–344), whose users are at lines 370, 417, 440, 461, 492, 513, 554, 990, 1017 and 1028;
  - L-3 fixture `close_repo` (1270–1275), whose users are at lines 1285, 1317, 1350 and 1377.
- **Also in this file:** `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together` (1238) and `test_admitted_crd_table_is_explicit_and_matches_the_harness_roots` (965). Both stay unchanged (§8).

### 5.3 Updater facts the remedy relies on

- **Its root.** `ROOT` is bound to its own file (line 28). `ADMITTED_CRD_QA` (51–54) admits HDE-CRD-0001 and HDE-CRD-0002. `_load_crd_qa_entries` (3947) reads under that `ROOT`.
- **Its key set.** `_ALLOWED_INDEX_FIELDS` includes `crd_id` (3749). `_normalize_index_entry` refuses a row with both `epic_id` and `crd_id` (3782–3784).
- **Close-pack rows.** `_crd_close_pack_entries` (4046) pairs `audit/<CRD>_close_report.md` with `audit/<CRD>_MANIFEST.json`:
  - neither present: no rows; both present: one row each, carrying `"crd_id"` (4063);
  - one present: `CRD_CLOSE_PACK_INCOMPLETE`; a row whose file is absent: `CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`.
- **Only the close-pack rows carry `crd_id`.** QA-family and close-run rows carry none. That is why the QA root alone breaks neither R-4's nor R-5's validator (proposal v1.1 §4.2).
- **The candidate source** `audit/HDE-CRD-0002_close_candidate_source.json` is not indexed and has no path proof. Its path is fixed by `docs/adr/hde/close_pack_writer_adr.md` §3 and named at `tests/qa/test_generate_epic_close_pack.py:4346` (`CRD_SOURCE_REL`).
- **State of `main`:**
  - `audit/qa/` holds only `hde-crd-0001`;
  - no `audit/HDE-CRD-0002_*` file exists;
  - `audit/ops/hde-crd-0002/wu-ops-01/` is unindexed and is not an admitted QA root. The remedy does not touch it.

### 5.4 The R-4 file

`test_mirror_schema_and_parity` (lines 511–594):
- it reads the real `artifacts/evidence_index.jsonl`;
- `optional_fields` is at lines 526–532;
- the unknown-key assertion is at line 539.

Plan v1.0 §4 records its last change as 75b3026 (#529), before any CRD admission. This session's checkout is shallow and does not reach that commit; the blob in §5.1 equals the bytes plan v1.0 measured.

### 5.5 The R-5 file

- `_MIRROR_REQUIRED_FIELDS` and `_MIRROR_OPTIONAL_FIELDS` (lines 219–232). The optional set is `{"epic_id", "notes", "record_type", "schema_version", "tokens"}`.
- `_HUMAN_INDEX_OPTIONAL_FIELDS` (233–245): `epic_id`, `notes`, `produced_at_utc`, `record_type`, `role`, `schema_version`, `sha256`, `size_bytes`, `tokens`.
- `_STRING_METADATA_FIELDS` (247–249) and `_metadata_type_error` (578).
- `_mirror_record_error` (660; unknown keys at 663).
- `_load_evidence_graph` (791; Human Index unknown-field rejection at 855–864). It validates the whole Index and Mirror, not only cited rows.
- `evaluate_acceptance_map_viability` (3467). It refuses CRD mode at 3479–3480, before Epic-only paths (HDE Mechanics Guide §1.6.3, "Explicit legacy Epic compatibility").

### 5.6 CI facts

- **Classification of the three files together**, `classify_paths` run read-only at `3b21327`:
  - lanes `evidence` and `qa`, `reason=selected_lanes`, `path_count=3`;
  - `changed_test_targets` returns `tests/qa/test_qa_tool_ownership.py`, because `tools/qa/qa_harness.py` is mapped to `_QA_TEST_OWNERS + (_QA_TOOL_OWNERSHIP_TEST,)` (`classify_ci_changes.py:805`).
  - Each test file alone: `evidence` only. The two test files alone: no changed-test targets.
- **Steps the PR head runs** (`.github/workflows/ci.yml`):
  - "Run affected behavioral tests in isolation" (from line 107);
  - "Run governed evidence integrity lane" (221–240): 7 validators and 6 pytest files;
  - "Run approved generic QA subsystem lane in isolation" (242–271): seven files in a detached worktree, then `git diff --exit-code` and an empty-status check;
  - the final `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Steps the V-2 and V-3 states run.** A QA-evidence or close-pack change regenerates `docs/evidence/INDEX.json`, which classifies to `evidence` and `release`. The release step is "Build and verify exact-source release attestation" (273–343). So V-2 and V-3 run the release lane, and the qa lane as later pull requests would run it over that state.
- **Baselines** (proposal v1.1 §5.5; plan v1.0 §12.3):
  - evidence lane: 134 passed on code-identical heads;
  - qa lane: 488 passed (167 + 114 + 33 + 3 + 2 + 87 + 82);
  - `tests/qa/test_qa_tool_ownership.py`: 146 passed on the rehearsed change;
  - release lane: 79 release tests passed, and the attestation was built and verified.
  - Times vary by container: the six evidence files took 696–1,046 s, the qa lane 16–19 s.
- **Prototype diff.** `git apply --check` of plan v1.0's prototype diff is clean on `3b21327`.

## 6. Bounded files and components

| Path | Change |
| :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | R-1, R-2, R-3 with C-1 |
| `tests/evidence/test_evidence_skeleton.py` | R-4 only |
| `tools/qa/qa_harness.py` | R-5 only |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-*` | The unit's records: the successor plan and its prototype diff, and the result records |

Expected unchanged:
- every other file, including `tools/evidence/update_evidence_index.py`, `.github/workflows/ci.yml`, `ci/checks/**` and every other test file;
- the governed evidence: Index, Mirror, sentinels, path proofs, orientation;
- `audit/**`, every release member, `docs/pfcanon/**`, `AGENTS.md`, `README.md`.

## 7. Exclusions (§2.24 "Exclusions and nonclaims")

- No updater or runtime change, and no harness change beyond R-5.
- No regeneration or hand edit of governed evidence, and no new evidence family.
- No HDE-CRD-0002 QA evidence, close pack or close candidate source is produced or committed. Stand-ins exist only in throwaway clones.
- No Specification change.
- No reopening of WU-PR-02 or WU-PR-07, and no re-run of an accepted-final pull request.
- The 12 Epic acceptance maps that already fail viability on `main` (OBS-1: HDE-EPIC017, 019, 020, 022, 023, 024, 030, 033, 034, 035, 036 and 037) are not repaired.
- FND-024 (the PR35-C1 flake risk on QA-evidence pull requests) stays with its recorded owner.
- OBS-2 (the 9 local failures of `tests/evidence/test_hdapi_v2_contract_inventory.py`) is not this unit's. It is routed to the QA-10 reassessment and the Product Owner (review v1.1 §3).

## 8. Interface contracts with other units

- **QA-50 and later QA-evidence pull requests:** publishing under `audit/qa/hde-crd-0002/` through `publish_crd_check_family` must leave the evidence lane green with no change to these files. This is measure (1).
- **The close stage (S21):** the close-run family (`publish_crd_close_run_family`), the close pack and the candidate source must land on `main` without failing the evidence lane. The first qa-lane run after them must pass, and Epic viability must be unchanged. This is measure (2).
- **The admission table:** R-2 reads `ADMITTED_CRD_QA`. The table is unchanged, and line 965's test still pins it.
- **The mutual-exclusion rule** stays enforced at the writer (pinned by line 1238's test) and by `check_mirror_schema.sh` (`EPIC_CRD_EXCLUSIVE`). R-1 to R-3 must not weaken line 1238's test. R-4 and R-5 do not duplicate either check (CR-10).
- **Harness users** (`tools/qa/epic021_qa.py`, the Epic close-pack generators, `evaluate_acceptance_map_viability`) keep their results on every state without a close pack. On the close-stage state they keep the V-2 statuses (V-3 (b)).

## 9. Disposition rules PR-20 must apply and record

1. **Successor plan.** Write one complete successor plan under `docs/ephemeral/`, superseding plan v1.0. Plan v1.0's §5 (PD-1 to PD-7), §6, §8, §11 and §12 stay valid for R-1 to R-3 and may be reused where unchanged (proposal v1.1 §11 step 3), with their prototype diff. Say what is reused, and re-measure anything that moved.
2. **Design choices recorded in the plan:**
   - the form of R-4's and R-5's lines (the rehearsed 29-line diff in proposal v1.1 §6.2 substantiates the size and is not a design);
   - whether any further test is needed (§4: only for an unprotected condition);
   - the prototype diff's coverage of all three files.
3. **Stand-ins (C-1).** Produced only through the harness and the canonical updater:
   - `publish_crd_check_family` for the QA family;
   - `publish_crd_close_run_family` for the close-run family, after the QA family (§2.15);
   - the updater's write for the close pack;
   - plus an authored candidate-source file.

   Each stand-in states that it is not QA evidence. Plan v1.0 §11 and proposal v1.1 §5.1 record working forms. Nothing from a rehearsal clone is committed.
4. **Prototype.** Run the change and V-1 to V-4 in throwaway clones with:
   - CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`);
   - Python 3.12;
   - closed rails through `env -i` (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`).

   Record exact counts, times and exit codes. For V-3 (b), record each map's status in the V-2 and V-3 states and whether any result names `crd_id`. A read-only probe calling `evaluate_acceptance_map_viability(HarnessConfig(<epic>, <tree>))` over the 16 `docs/acceptance_map_epic0NN.json` maps, as proposal v1.1 §5.4 used, publishes nothing.
5. **Lane time.** Record the evidence lane's time against the baselines in §5.6. Times taken beside other jobs are not comparable.
6. **Re-check the baseline.** Confirm §5's facts at the plan's head. A change in a decisive fact is recorded. A change in scope goes through §14.

## 10. Acceptance, tests and evidence (§2.24 "Verification")

| ID | Check | Pass condition | Covers |
| :- | :- | :- | :- |
| V-1 | Local, on the PR head (root absent) | The 7 evidence-lane validators exit 0. The six evidence-lane pytest files pass with no fewer than 134 tests. The qa lane's seven files pass with its two tree checks. The classifier's changed-test targets (today `tests/qa/test_qa_tool_ownership.py`) pass in isolation. All exactly as `ci.yml` runs them | (1) |
| V-2 | A throwaway clone of the PR head with a stand-in HDE-CRD-0002 QA family, published by the harness and the canonical updater | The evidence, qa and release lanes pass, exactly as `ci.yml` runs them | (3) |
| V-3 (with C-1) | The V-2 clone, also holding a stand-in close-run family, the two close-pack files and the close candidate source, indexed by the canonical updater | (a) The evidence, qa and release lanes pass, exactly as `ci.yml` runs them. (b) Each `docs/acceptance_map_epic0NN.json` gets the same `evaluate_acceptance_map_viability` status as in the V-2 state, and no result names `crd_id` | (3), close stage; S22's "existing Epic … inputs still publish and validate" |
| V-4 | Negative control | The R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy | Keeps acceptance (5)'s property |
| V-5 | Hosted CI on the PR head | Every lane the classifier selects (today evidence and qa) and the changed-test step are green, and the run ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | (2) |

- **Triage resolution evidence (1)**, the updated tests on `main`, is met when the merged change carries R-1 to R-5. PR-40 checks it.
- **Evidence obligations (amended P-2).** The PR result record names every check actually run, with counts. It includes the V-2 and V-3 rehearsal outputs: commands, exit codes, test counts, the stand-ins' provenance and the V-3 (b) viability comparison. There is no governed-evidence change.
- **Business case** (proposal v1.1 §6.5; §2.24):
  - **Beneficiaries:** QA and the Product Owner; every later qa-lane pull request; the users of the harness's Epic viability.
  - **Benefit:** QA-20 and QA-50 can proceed, and the close pack leaves no lane or Epic viability failing.
  - **Measure (1):** the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests.
  - **Measure (2):** the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes, with no change to these three files.
  - **At PR-40:** neither measure is observable there. PR-40 records V-2 and V-3 as their proxy and each measure as "not yet measurable" (§2.18 rule 5). The measures are checked at those pull requests and that run, or by the QA-10 reassessment.
  - **No cost ceiling** (§2.18 rule 1).

## 11. Migration and security constraints

- **Migration:** none.
- **Security:**
  - test code and one internal QA tool, neither a release member nor runtime;
  - no secret, credential, network or production surface. The fixtures' subprocesses run under the file's closed-rails `ENV`;
  - R-5 widens what the harness accepts by one canon-allowed key only. On `main` today no row carries `crd_id`, so R-5 changes no current result (proposal v1.1 §9).
- **Real inputs** (addendum 2.11 rule 4): this change's own QA evidence and close pack, both planned deliverables, and the hosted CI runner. A both-keys row and a non-string `crd_id` are outside the real set and get the stated limit of §4, not a model (rule 5; CR-10).

## 12. Engineering, review, CI and merge obligations

**PR-20, in the dedicated WU-REM-01 PR session:**
- reads this instruction and its lineage, with the three files and `ci.yml` on `main`;
- applies §9;
- writes one complete successor `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`, with its prototype diff;
- returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.

**PR-30**, after Nathan's Proceed for that exact plan, given against the business case:
- recovers existing work first;
- changes only the three files;
- runs V-1 to V-4 on the real branch;
- runs the pre-push check: `python tools/ci/prepush_check.py lanes build-notes`, and `--path <each changed path> membership`;
- commits coherently and publishes `PR_CANDIDATE_PUBLISHED`;
- hands off to PR-35 in its own session.

**PR-35**, in its own dedicated session:
- **Codex code review:** retrieves and dispositions its findings under addendum 2.11 rule 7 and addendum 2.14:
  - a P1 on a real input is fixed;
  - declining a P1 goes to the Product Owner first;
  - a finding on the both-keys row gets the traced path and CR-10's stated limit;
  - rule 8 applies to a repeated finding class.
- **No security review:** addendum 2.3 deprecates the Codex security review.
- **CI:** verifies V-5 and mergeability on the current head. A failure that is red on the base too is handled as base-red, not by widening the unit.
- **Returns** `MERGE_PENDING` without merging.

**Other obligations:**
- **PR description:** the `.github/pull_request_template.md` headings, filled under the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage:
  - verifies R-1 to R-5 on the merged head, and V-1 to V-5 from the records and the hosted run;
  - records both measures' state (§10);
  - on ACCEPT, returns to the same Isis QA-10 reassessment, not to a Plan unit.
- **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, pull requests and `docs/ephemeral/` before creating anything.
- **Rehearsals and prototypes:** they run only in throwaway clones. Discard and re-clone on failure.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version.
- **Rollback:** the Product Owner reverts the squash commit. No release member is touched, so there is no manifest refresh.
- **Abort:** only by Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material:** a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or scope or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional; RS-30 for revisions). This IA reviews it through RS-20.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Changes to the approved remedy itself** belong to Isis through ESC-30 and ESC-40, not to RS-20. Plan v1.0 used this route.
- **Expected triggers:**
  - a needed change outside the three files, for example in the updater, `ci.yml` or another test;
  - a needed harness change beyond adding `crd_id` to the two sets;
  - a stand-in rehearsal that fails for a reason R-1 to R-5 cannot fix;
  - a V-3 (b) status that differs from V-2 for a reason other than `crd_id`.
- **Not a trigger:** a §9.2 design choice, a helper kept in the file that uses it, or a further test within §4's rule.

## 15. Unresolved items, carried observations and owners

| Item | Owner |
| :- | :- |
| CR-10 drainage into HDE Schemas and Artifacts §8.3 | Product Owner |
| OBS-1, the 12 Epic viabilities already failing on `main` | Product Owner, as a later-change candidate |
| OBS-2, the local failures of `tests/evidence/test_hdapi_v2_contract_inventory.py` | Isis at the QA-10 reassessment; Product Owner triage |
| CR-9 (path proofs under the Ops evidence root), unaffected | Isis, at IA-30 |
| FND-024, the PR35-C1 flake risk on QA-evidence pull requests | As recorded in the triage |
| Measures (1) and (2) (§10) | The first QA-evidence pull request, the close-pack pull request and the next qa-lane run, or the QA-10 reassessment |
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
| CR-10 | APPROVED, alternative (a) | Isis (ESC-40, 2026-10-23T20:15:00Z) | review v1.1 §4; addendum 2.24 "Conflict decided: CR-10". Drainage unperformed |

**No new conflict.** This instruction applies CR-10 as decided (§4 stated limit) and decides no canon.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Owned by | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S22 acceptance intent; Constraints "QA evidence admission" ("preserves existing Epic and HDE-CRD-0001 inputs") | QA evidence publishes and validates before QA; existing Epic inputs still validate | §1, §4, §8 | WU-REM-01 | V-2, V-3, V-5 | PR result; hosted CI |
| S21 close-run tests and close-pack rows | The close stage lands without failing a validator | R-3, R-4, R-5; §8 | WU-REM-01 | V-1, V-3 | PR result |
| P-1 (unchanged) | An absent root publishes nothing, proven in a copy; no evidence-lane test depends on the real checkout's HDE-CRD-0002 state | R-1; §4 "Restated acceptance" | WU-REM-01 (WU-PR-02 untouched) | V-1, V-3, V-4 | PR result |
| Amended P-2: purpose, scope, dependencies | Three files; none on unmerged work; lands before QA-20 | §3, §6, §7 | WU-REM-01 | — | PR-40 attribution |
| Amended P-2: evidence obligations | V-2 and V-3 outputs with the viability comparison; no governed-evidence change | §10 | PR-30, PR-35 | — | PR result |
| Business case: measures (1) and (2) | Observed later; proxy at PR-40 | §10 | Product Owner (Proceed); IA (PR-40 records it) | Measures, later | Later pull requests, or QA-10 |
| R-1 to R-3 with C-1 | As v1.0 issued them | §4, unchanged in meaning; §5.2, §5.3 | PR-20; PR-30 | V-1 to V-4 | PR result |
| R-4 | One key added to one test's optional set; nothing else in that file | §4 R-4; §5.4 | PR-20; PR-30 | V-1, V-3 (a) | PR result |
| R-5 | One key added to the harness's two optional sets; required keys, other metadata checks, Epic predicates and CRD refusal unchanged | §4 R-5; §5.5; no `_STRING_METADATA_FIELDS` change | PR-20; PR-30 | V-1, V-3 (a) and (b) | PR result |
| CR-10 (a) | Accept `crd_id` only; mutual exclusion stays at the writer and the schema check | §4 stated limit; §8; §11 | PR-20; PR-35 (findings) | PR-40 attribution | Merged diff |
| Limit | No file outside the three | §4; §6 | PR-20 | PR-40 attribution | Merged diff |
| V-1 to V-5 | As quoted | §10, quoted | PR-30 (V-1 to V-4), PR-35 (V-5) | — | PR result; hosted run |
| Triage (1) to (3) | Updated tests on `main`; hosted CI; a root-present demonstration | §10 "Covers" column | WU-REM-01 | — | PR-40 |
| Exclusions | No updater or runtime change, no harness change beyond R-5, no evidence or Specification change, no QA evidence | §7 | All phases | PR-40 attribution | Merged diff |
| WU-PR-02 and WU-PR-07 accepted | Not reopened | §1, §7 | — | — | — |

- **Numeric domains:**
  - "no fewer than 134" counts passed tests over the six evidence-lane files;
  - "7 validators" is the count in `ci.yml` lines 227–233;
  - "the qa lane's seven files" are `ci.yml` lines 260–266, baseline 488 passed;
  - the 16 Epic maps are `docs/acceptance_map_epic0NN.json`; V-3 (b) compares statuses map by map, not counts;
  - the stand-ins use the harness's own status value `PASS` and no new value.
- **Decisive comparisons:** none fails. Every fact in §5 was re-measured at `3b21327`, or matched to the identical bytes measured by plan v1.0 and proposal v1.1.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in the dedicated WU-REM-01 PR session. It writes the successor plan and returns `AWAITING_PO_PROCEED`.
- **Returns to this IA:** RS-20 for a rescope; PR-10 for an instruction defect; PR-40 after Nathan's merge.
- **Final return:** after PR-40 ACCEPT, the same Isis QA-10 — Audit Implementation and Establish QA Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c), for the reassessment of S22 and its dependants.

## 19. TypeSafe reading for the receiving session (PR-20, WU-REM-01 successor plan)

Action sent (v8.2): "Plan, as the dedicated pull-request engineering author returning after a remedy decision, one successor detailed implementation plan for a remediation work unit whose approved instruction was re-issued: a test-and-tooling change to three files, in which one evidence test is rewritten and two fixtures build their starting state in a copy, one key is added to a second evidence test's allowed set, and one key is added to two allowed-key sets in the QA harness. The plan reuses an existing plan and prototype diff for the first file, extends the prototype to the other two, and defines five verification checks, including two rehearsals in throwaway clones that publish stand-in evidence through the canonical tools and run three CI lanes and an acceptance-map viability comparison, and a hosted CI run. It is a Markdown plan with a prototype diff; no code is committed; a Product Owner Proceed, implementation, review and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.18 (confidence 0.81). Rung probabilities: low 0.00, medium 0.05, high 0.73, extra high 0.21, max 0.01, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.03, Opus 5.5 0.91, Sonnet 5.5 0.06, Haiku 5.5 0.00 (confidence 0.88).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.022, Fable 5.1 at extra high 0.006, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.046, Opus 5.5 at high 0.664, Opus 5.5 at extra high 0.191, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.003, Sonnet 5.5 at high 0.044, Sonnet 5.5 at extra high 0.013, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: none printed.
  - Sent 2026-10-23T20:51:30Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-23T20:51:30Z; HTTP 200 in 0.62 s; 5526 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is in review v1.1 §9.

**Surface advice:** run PR-20 in the existing dedicated WU-REM-01 PR session (https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5) on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Prototype:** throwaway clones with CI's full install, Python 3.12 and closed rails. Allow room for three evidence-lane runs of about 12 to 17 minutes each (V-1, V-2 and V-3), plus the qa lane (under 20 s per run), the release lane (about 3 minutes per run) and the viability probe.
- **Writes:** only the successor plan and its prototype diff, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this instruction's pull request is merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-PR-10-20261023-WU-REM-01-02` |
| Change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| Requirement / work unit | S22, with S21's close-run tests and close-pack rows; WU-REM-01 |
| Prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, page state of 2026-10-12T02:29:33.739Z |
| Release | GCFPE-20261009.1 / 100926.1 |
| Role and stage | whole-change IA, PR-10 (instruction v1.1) |
| Capture time | 2026-10-23T21:00:00Z |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |
| Inherited usage | instruction v1.0 (`…-PR-10-20261023-WU-REM-01-01`); plan v1.0 (`…-PR-20-20261023-WU-REM-01-01`); proposal v1.1 (`…-ESC-30-20261023-FND-001-02`); review v1.1 (`…-ESC-40-20261023-FND-001-02`) |
| Repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) |

## Canon relied on

Read on `main` at `3b21327`. PF10 is v13.7.6.

| Decision topic | Sources and sections |
| :- | :- |
| Instruction contract, successor on a repeated invocation, readiness, routing | PR-10 — Create PR Work-Unit Instructions — 100926.1: "Execute" 1 to 8 and the repeated-invocation rule, "Semantic readiness before INSTRUCTION_READY", "Required result", "Next step and recovery" (re-read in this invocation; the page was read in full for v1.0 and is unchanged) |
| The approved remedy, as amended | `docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md`, read in full; the 2.24 record, read in full; proposal v1.1, read in full; PF10 v13.7.6 §2.23 and §2.24 as published, with §2.24 read in full and the v13.7.5 → v13.7.6 diff checked (it adds only 2.23 and 2.24 and their index lines) |
| What is superseded and what is reused | Instruction v1.0 (this session's own); PR-20 plan v1.0, read in full, with its prototype diff (`git apply --check` clean on `3b21327`) |
| The Index and Mirror key set; CR-10 | PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.3 "Machine Evidence Index — JSONL mirror", "Allowed top-level keys and unknown-key rejection", read in full |
| CR-10's governing rule | PF10 v13.7.6 §2.11 rule 5; §2.18 rule 6 ("addendum 2.11 rules 4 to 8" stand) |
| Harness Epic viability preserved | PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3, "Explicit legacy Epic compatibility" ("Preserve the existing Epic logic and strict predicates"), read |
| Business case and measures | PF10 v13.7.6 §2.11 rules 1, 2 and 4, as §2.18 narrows them; §2.18 rules 1 and 5 |
| Review chain | PF10 v13.7.6 §2.3, §2.11 rules 7 and 8, §2.14 |
| Accepted-final units | PF10 v13.7.6 §2.5 and §2.16 |
| The close-run family | PF10 v13.7.6 §2.15 (as plan v1.0 read it in full; unchanged in v13.7.6) |
| The objective | Specification v1.1-approved, S21 and S22 rows and Constraints "QA evidence admission", as v1.0 and proposal v1.1 quote them; Implementation Plan v1.1 §7 |
| Evidence writer rules | `AGENTS.md` "Governed evidence rules" (sole writer; no hand-editing), "Pre-push check", "Pytest readiness rule", "QA output placement", "Code review guidelines" (real-input rule) |
| Repository facts | `tests/evidence/test_evidence_skeleton.py` lines 520–542; `tools/qa/qa_harness.py` lines 222–249, 578–603, 660–666 and 852–866, plus its `crd_id` references; `tools/evidence/update_evidence_index.py` `crd_id` references (3749, 3782–3784, 4063); `ci/checks/check_mirror_schema.sh` lines 19 and 106–107; `.github/workflows/ci.yml` lines 107–125 and 221–272; `ci/checks/classify_ci_changes.py` `classify_paths` and `changed_test_targets`, run read-only; `catalog/manifest.json` (no hit for any of the five files in §5.1); blobs and hashes in §5.1 |
