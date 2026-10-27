---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-REM-01-PR-IMPLEMENTATION-PLAN
artifact_version: "1.1"
artifact_state: AWAITING_PO_PROCEED
plan_result: AWAITING_PO_PROCEED. A complete plan for the approved remedy as amended (R-1 to R-5), within the instruction's three-file limit, with a prototype diff covering all three files and V-1 to V-4 run on it (V-1 to V-4 all pass, including V-3 (b)). It awaits the Product Owner's PR Implementation Proceed for this exact plan; it authorizes no implementation, merge, publication, Ops or QA
predecessor: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0.md (v1.0, BLOCKED on F-1; blob 9009107b3be8; sha256 962371b9b865666f2734a7048985085209067932ab447e71d2b0fcd892ba07cf; #710, squash f5c7c7f), with docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.0-prototype.diff (blob 2a2895a589fd; sha256 1203de91f5aa3eb3d0ad9957f90ee6945ec54248886927fc609c49b72c56216e). Superseded by this version and kept unchanged as history; its BLOCKED result and F-1 evidence stand
supersession_reason: the remedy was amended (remediation review v1.1, APPROVE; HDE Build Notes addendum 2.24) and the instruction re-issued as v1.1. Plan v1.0 planned only R-1 to R-3 under a one-file limit
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-01
work_unit_title: "Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation; S22, with S21's close-run tests and close-pack rows)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.1.md (HDE-CRD-0002-WU-REM-01-PR-INSTRUCTION v1.1, INSTRUCTION_READY; blob 768772ec5e8a; sha256 cbeee7b8bcede005b9f342bfe05dcf27bff9bae59dc33624e0ff5ac0957bee24; #714, squash e1010b5). It supersedes instruction v1.0 (blob d89d1dc9991b; #709)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved; blob abffa2ccbd44), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1, DELTA_APPROVE; blob 5103fe29d588). WU-REM-01 enters its §7 through the remediation overlay's amended P-2, not through a Plan revision
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S21, S22 and Constraints "QA evidence admission", with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE). Preserved as the original approving review
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md (ESC-40 APPROVE, "ASK OK."; CR-10 APPROVED (a); Isis; blob 126330b8f6b9; #712, squash c8d8bc3). It supersedes review v1.0 (APPROVE_AS_CHANGED; blob e100bf4eba08; #708) for WU-REM-01's scope, limit, exclusions, verification and business case
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md (Thoth; blob 12fcbb30585f; sha256 2aa11d33e3b0cd0332aa0471584e3b0662dc5ab8f796bbf2c9c5fe6d7e07474f; #711, squash d524f00). Its §6 is the approved overlay
remediation_addenda: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.23 and §2.24 (published by #713, 3b21327); records docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.0.md (2.23; blob 248c17e7e513) and docs/ephemeral/HDE-CRD-0002-remediation-FND-001-PF10-build-notes-addendum-v1.1.md (2.24; blob 13baa7812398)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; blob b39ac9f276db)
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (QA-10 FND-001; Reality Audit RA2-22; blob dac6d1a79de8), from docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md (QA-10 NOT_READY; blob f6d7ff018ce7)
return_owner: Isis, the same QA-10 — Audit Implementation and Establish QA Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c), for the reassessment of S22 and its dependants, after this unit's PR-40 ACCEPT
accepted_final_not_reopened: WU-PR-02 (addendum 2.5) and WU-PR-07 (addendum 2.16)
business_case_ref: proposal v1.1 §6.5, approved by review v1.1 §5 and addendum 2.24; instruction v1.1 §10. No cost ceiling (addendum 2.18)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (INITIAL_APPROVE). Neither is edited
effective_baseline: approved base + applicable PF10 overlays — Specification delta 01 (addendum 2.20); Plan delta 01 v1.1 (addendum 2.19); the FND-001 remedy (addendum 2.23, as addendum 2.24 amends it: P-1, amended P-2, R-1 to R-5, V-1 to V-5, CR-10 (a)); addenda 2.18, 2.11 (rules 1, 2 and 4 to 8 as 2.18 narrows them), 2.15, 2.14, 2.5, 2.16, 2.3 and 2.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md (blob 3e8ad454c677; 473,130 bytes; sha256 ee6d55b57b3b922116363dd914264333cf3566c4856819e2a139ed50f7a6604e; the only PF10 file on main at e1010b5; last addendum 2.24)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md §2.1, §2.3, §2.5, §2.11, §2.14, §2.15, §2.16, §2.18, §2.19, §2.20, §2.23, §2.24
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.1-prototype.diff (R-1 to R-5; git diff e1010b5 → prototype head b4748fe; 3 files, +60/−27; 156 lines; 7,098 bytes; sha256 1323f0960a1898ce0515d7ad52dacdabd3350962fe5af2f6af12324697488d8e; `git apply --check` clean on e1010b5)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: CONTINUING_DEDICATED_ASSIGNMENT (role and artifact-lineage continuity, PR-20 "Role and artifact continuity")
role_session_ref: https://claude.ai/code/session_01AZdnRebA6fKRxfAgHmLYtP, titled "HDE-CRD-0002 WU-REM-01 PR", created 2026-10-23T21:02:14Z, into which Nathan pasted the PR-20 handoff. PR-20 now; PR-30 after the Proceed
session_provenance: plan v1.0 was written in https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5 (same title), which the platform record shows ARCHIVED, last updated 2026-10-23T18:20:53Z. Instruction v1.1's receiver field names that session
context_conflict: none blocking. The instruction names the archived session; the Product Owner chose this one. This session holds no conversational context from v1.0's session and worked only from the repository records named here
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, fetched and read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_baseline: origin/main e1010b5 (#714). It adds only instruction v1.1 to 3b21327, the instruction's measured baseline (git diff --stat 3b21327 e1010b5: 1 file, docs/ephemeral/ only)
working_branch: claude/relaxed-hamilton-vorgjj, cut from e1010b5 (this plan and its diff only)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on the Product Owner's Proceed for this exact plan
created_at: 2026-10-23T21:36:00Z
canon_conflict_register: CR-1 to CR-8 carried, decided; CR-9 carried PROPOSED, unaffected; CR-10 carried APPROVED (a) and applied; no new entry (§19)
---

# HDE-CRD-0002 WU-REM-01 — PR Implementation Plan v1.1

## 1. Result

**AWAITING_PO_PROCEED.** This is the one complete successor plan for WU-REM-01 under instruction v1.1. It plans the approved remedy as amended: R-1 to R-3 with C-1 in `tests/evidence/test_evidence_index_missing_state.py`, R-4 in `tests/evidence/test_evidence_skeleton.py` and R-5 in `tools/qa/qa_harness.py`, and no other file.

- **Prototype:** the companion diff (3 files, +60/−27) applied to e1010b5 gives head `b4748fe` in a throwaway clone. Plan v1.0's R-1 to R-3 hunks are carried byte for byte.
- **V-1 (root absent):** the 7 evidence-lane validators exit 0; the six files pass **134** tests (681.4 s, run alone); the qa lane passes **488** with both tree checks; the changed-test target `tests/qa/test_qa_tool_ownership.py` passes **146**; the tree stays clean.
- **V-2 (stand-in QA family, published by the harness and the canonical updater):** evidence lane 134 passed, qa lane 488 passed, release lane 79 passed with the attestation built and verified; tree clean.
- **V-3 (V-2 plus the stand-in close-run family, close pack, candidate source and ledgers):** (a) the same three lanes pass with the same counts; (b) all 16 Epic acceptance-map viability statuses equal V-2's, and no result names `crd_id`.
- **V-4:** the R-1 test fails when an Index row under `audit/qa/hde-crd-0002/` is planted in its copy, and passes unmutated.
- **Controls:** FND-001 still reproduces with `main`'s test file (2 failed, 4 errors). Without R-4 the skeleton test fails on `crd_id`; without R-5 the qa-lane viability test fails and four Epic maps turn FAIL_TOOLING. So each of R-4 and R-5 is necessary, and together with R-1 to R-3 they are sufficient.
- **Pre-push check:** PASS (lanes `evidence,qa`; build notes PF10 v13.7.6; all three paths not release members).
- **V-5** (hosted CI on the implementation head) is PR-35's; it cannot run before the code pull request exists.

**Not offered or done here.** Nothing is implemented, committed to a code path, pushed or merged. The Product Owner's Proceed for this exact plan is the gate before PR-30. No boundary finding arose (§16), so no rescope is routed.

## 2. Lineage, reuse and sources read

### 2.1 What is reused from plan v1.0 (instruction §9.1)

| Plan v1.0 | Use here | Why it stays valid |
| :- | :- | :- |
| §5 PD-1 to PD-7 (R-1 to R-3 design) | Reused unchanged as §5.1 | R-1 to R-3 with C-1 are unchanged (addendum 2.24 "R-1, unchanged" to "R-3 with C-1, unchanged"); the file's bytes on `main` are the bytes v1.0 designed against (§4) |
| §6 real-input set | Reused and extended for R-4 and R-5 (§6) | Same inputs; R-4 and R-5 add the close-pack rows' `crd_id` key |
| §8 implementation sequence | Reused and extended to three files (§8) | Same vehicle, one commit, one pull request |
| §11 stand-ins | Method reused; every stand-in re-produced in this session (§11) | C-1's producers are unchanged |
| §12 prototype record | Method reused; every run repeated on the three-file head at e1010b5 (§12). v1.0's numbers stay history | The head changed (R-4, R-5), and so did the lanes V-1 to V-3 run |
| Prototype diff v1.0 | Its hunks carried byte for byte into the v1.1 diff | Applied to e1010b5, the R-1 to R-3 file becomes blob 8c368caf3b42 in both |

Plan v1.0's §16 (F-1), §1 BLOCKED result and §21 ESC-30 reading are history and are not carried as current.

### 2.2 Sources read in this session

- **Instruction v1.1**, read in full at e1010b5 (blob 768772ec5e8a). Its §5 baseline was re-measured (§4).
- **Remediation review v1.1**, **proposal v1.1** and the **2.24 record**, each read in full; the **2.23 record** read in full; PF10 v13.7.6 §2.23 and §2.24 read in full as published.
- **Plan v1.0**, read in full, with its prototype diff (applied to e1010b5 in a throwaway clone).
- **Approved bases:** Specification v1.1-approved, the S21 and S22 rows, the Distillation row and Constraints "QA evidence admission"; Implementation Plan v1.1 §7's common PR terms and WU-PR-02 (acceptance (5)).
- **PF10 v13.7.6:** front matter "Precedence, versioning, and scope" and the Addendum Index; addenda 2.1, 2.3, 2.11, 2.14, 2.15, 2.18, 2.23 and 2.24, each read in full.
- **Prompts:** PR-20 (page state 2026-10-12T02:29:47.327Z) and PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state 2026-10-12T02:30:08.672Z), each fetched and read in full.
- **GCFPE Membership and Release Register** (Notion), searched for its selection lines, not read in full: the selected contract is GCFPE-20261009.1 / 100926.1, 55 members, selected 2026-10-12 by the Product Owner. PR-20 and PR-30 above are its 100926.1 members.
- **Code read at e1010b5:**
  - `tests/evidence/test_evidence_index_missing_state.py`: the prototype head's version (blob 8c368caf3b42) in full, and e1010b5's lines 28–60, 960–1015 and 1236–1300;
  - `tests/evidence/test_evidence_skeleton.py` lines 505–600 (`test_mirror_schema_and_parity`);
  - `tools/qa/qa_harness.py` lines 49–135 (`Status`, `HarnessConfig`, `CheckResult`), 210–250 (the key sets), 578–603 (`_metadata_type_error`), 660–670 (`_mirror_record_error`), 785–870 (`_load_evidence_graph`), 1362–1413 (check-ID and command validation), 3467–3540 (`evaluate_acceptance_map_viability`), and its `crd_id` references;
  - `tools/evidence/update_evidence_index.py` lines 46–56 (`ADMITTED_CRD_QA`), 3778–3790 (`_normalize_index_entry`), 4040–4075 (`_crd_close_pack_entries`), 5160–5290 (`publish_crd_check_family`, `publish_crd_close_run_family`);
  - `ci/checks/check_mirror_schema.sh` lines 100–110 (`EPIC_CRD_EXCLUSIVE`);
  - `.github/workflows/ci.yml` lines 1–134 and 215–420; `ci/checks/classify_ci_changes.py` lines 764–816 (the QA owner table);
  - `.github/pull_request_template.md`; `catalog/manifest.json` (no hit for the three files, the updater or `ci.yml`).

### 2.3 Session identity

Plan v1.0 was written in the WU-REM-01 PR session https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5. The platform record shows that session ARCHIVED (last updated 2026-10-23T18:20:53Z). Nathan pasted the PR-20 handoff into this session, which carries the same title. PR-20's "Role and artifact continuity" makes continuity a matter of the role's task context and artifact lineage, and leaves the session choice to the Product Owner. This session therefore records CONTINUING_DEDICATED_ASSIGNMENT, works only from the repository records named here, and keeps the earlier session as provenance. PR-30 runs here after the Proceed; PR-35 runs in its own session (§20).

## 3. Business case (instruction §10; proposal v1.1 §6.5; addendum 2.24)

Carried, not re-decided:
- **Beneficiaries:** QA (Kronos) and the Product Owner; every later pull request that selects the qa lane; the users of the harness's Epic acceptance-map viability (`tools/qa/epic021_qa.py` and the Epic close-pack generators).
- **Evidence:** proposal v1.0 §4 (six evidence-lane tests break with the root present); plan v1.0 §12.3 (V-3: the skeleton test breaks with the close stage); proposal v1.1 §5.3 and §5.4 (the qa-lane test and four Epic viabilities break with the close stage). This plan reproduced the cause again at e1010b5 (§12, R0 and the necessity controls).
- **Benefit:** QA-20 and QA-50 can proceed, and the close pack leaves no lane or Epic viability failing.
- **Measure (1):** the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests.
- **Measure (2):** the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes, with no change to these three files.
- **At PR-40:** neither measure is observable. PR-40 records V-2 and V-3 as their proxy and each measure as "not yet measurable" (addendum 2.18 rule 5).
- **No cost ceiling** (addendum 2.18 rule 1). No record of this unit records spend against one.

**How the plan keeps to it.** The change is exactly R-1 to R-5. It adds no test, helper module or check beyond them (PD-10), because addendum 2.11 rule 3 stops a unit whose business case is met and rule 2 excludes work for its own sake. The prototype shows the proxy for both measures: V-2 for measure (1), V-3 for measure (2) (§12).

## 4. Baseline re-check (instruction §9.6)

Measured at e1010b5 in the session checkout and in a throwaway clone of it.

| Fact (instruction §5) | Instruction (3b21327) | Measured (e1010b5) |
| :- | :- | :- |
| Bytes outside `docs/ephemeral/` | — | identical to 3b21327 (`git diff --stat 3b21327 e1010b5` lists only instruction v1.1) |
| `tests/evidence/test_evidence_index_missing_state.py` | 1,383 lines; blob bff9a6b0f34f; sha256 fb710617856b629ac69218230f5d4db02f186c94717a82dcc87cb7451bb95e79 | same |
| `tests/evidence/test_evidence_skeleton.py` | 656 lines; blob 057b4ae973ba; sha256 4221cc13d391675ddcfe2e79a20751124ccfe72ba2af7c0496c3a921f769bcdd | same; `optional_fields` at 526–532; the unknown-key assertion at 539 |
| `tools/qa/qa_harness.py` | 4,011 lines; blob 4484408aa713; sha256 243e2bac0221e8e941e6316663cd9a002576c36c13abbfa84408014759e7ac5c | same; `_MIRROR_OPTIONAL_FIELDS` 230–232, `_HUMAN_INDEX_OPTIONAL_FIELDS` 233–245, `_STRING_METADATA_FIELDS` 247–249, `_metadata_type_error` 578, `_mirror_record_error` 660, `_load_evidence_graph` 791 (unknown fields 855–864), `evaluate_acceptance_map_viability` 3467 (CRD refusal 3479–3480) |
| `tools/evidence/update_evidence_index.py` | blob ad441edbea3c; sha256 fc35ff8c8eef9958a87b255e3b1fc878ed60a6c3d3a8cf43dd3a99123a99ad55 | same; `ADMITTED_CRD_QA` 51–54; both-keys refusal 3782–3784; close-pack rows with `crd_id` 4046–4066; `publish_crd_check_family` 5166; `publish_crd_close_run_family` 5222 |
| `.github/workflows/ci.yml` | blob 3836bad11c39; sha256 d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b | same; changed-test step 107–133, evidence 221–240, qa 242–271, release 273–343, final 345–420 |
| Release membership | none of the five in `catalog/manifest.json` | 0 matches |
| R-1 to R-3 loci and helpers (instruction §5.2) | as listed | same (the v1.0 prototype diff applies cleanly; its hunks land at the same lines) |
| `ci/checks/check_mirror_schema.sh` | `EPIC_CRD_EXCLUSIVE` 106–107 | same |
| Classifier on the three files | lanes `evidence`, `qa`; changed-test target `tests/qa/test_qa_tool_ownership.py` (`classify_ci_changes.py:805`) | same, run as `ci.yml` calls it against the prototype head (§12.2) |
| State of `main` | `audit/qa/` holds only `hde-crd-0001`; no `audit/HDE-CRD-0002_*`; the Ops root unindexed | same |

No decisive fact changed.

## 5. Design decisions (instruction §9.2)

### 5.1 R-1 to R-3: reused from plan v1.0 §5, unchanged

- **PD-1, one strip helper in that file, `_strip_from_copy(repo, *relatives)`,** beside `_snapshot`. For each relative path it removes a directory tree, or a file and its sibling `.path_proof.txt`. It drops every Index row whose `discovered_physical_path` is that path or lies under it, then runs the canonical updater: a write, then `--check`. It generalises the existing `crd_repo` strip and keeps that fixture's comment in its docstring. Only `docs/evidence/INDEX.json` is edited; the updater regenerates the Mirror, sentinels, proofs and orientation. Rejected: three inline strips (the same logic three times); a helper in another module (outside the limit).
- **PD-2, the order: remove files, drop rows, write, `--check`.** Rows leave first, because the updater refuses a close-pack row whose file is absent (`CRD_CLOSE_PACK_INDEXED_BUT_ABSENT`) and a CRD row whose root is gone. The updater runs every time, even when nothing named was present, so every fixture starts from an updater-produced fixed point.
- **PD-3, R-1's copy is its own, stripping only `audit/qa/hde-crd-0002`.** Other admitted families stay, so the loader runs over the real admission table with only HDE-CRD-0002 absent. That is R-1's and P-1's wording ("a copy of the checkout from which that root and its Index rows are removed").
- **PD-4, R-1 calls the copy's loader through `_crd_program`.** `CRD_FIXTURE_PROGRAM` asserts `writer.ROOT == Path.cwd()`, so the loader reads the copy, not the real checkout (instruction §4 R-1, §5.3). The loader assertion runs inside that program and the test requires its exit 0; the Index assertion reads the copy's Index. Both predicates are the original test's, and the test keeps its name, so the WU-PR-02 records still name it.
- **PD-5, R-2 reads `ADMITTED_CRD_QA` from the updater imported in-process,** as line 965's test already does; the copy holds the same module byte for byte. `crd_repo` strips the first element of every value, today `audit/qa/hde-crd-0001` and `audit/qa/hde-crd-0002`. `CRD_ROOT` and `CRD_KEY` stay: ten tests still publish HDE-CRD-0001 through them.
- **PD-6, R-3's strip set, with C-1:** a new constant `CLOSE_SOURCE = "audit/HDE-CRD-0002_close_candidate_source.json"` beside `CLOSE_PACK`. `close_repo` strips `CLOSE_ROOT` (with `close/`), both `CLOSE_PACK` files and `CLOSE_SOURCE`, with their proofs and rows, then regenerates and checks. Its existing `assert not (repo / CLOSE_ROOT).exists()` stays and holds by construction. A docstring states the fixture's purpose.
- **PD-7, nothing else in that file changes:** no other test, constant, helper or assertion. Line 1238's and line 1084's mutual-exclusion tests and line 965's admission-table test are untouched (instruction §8). Line numbers are `main`'s; in the prototype they become 983, 1108 and 1262.

### 5.2 R-4 and R-5: their form (new)

- **PD-8, R-4 is one line.** `"crd_id",` becomes the first member of `test_mirror_schema_and_parity`'s `optional_fields` literal (new line 527), keeping its alphabetical order. Nothing else in `tests/evidence/test_evidence_skeleton.py` changes: not `required_fields`, not the unknown-key assertion (now line 540), not the token, ordering, proof or self-record checks. Rejected: also asserting that no row carries both `epic_id` and `crd_id` (CR-10 (a): a stated limit, not a check; §6).
- **PD-9, R-5 is one key added to each of the harness's two optional sets.**
  - `_MIRROR_OPTIONAL_FIELDS` keeps its single-line form and gains `"crd_id"` as its first member: `{"crd_id", "epic_id", "notes", "record_type", "schema_version", "tokens"}` (line 231, 77 characters).
  - `_HUMAN_INDEX_OPTIONAL_FIELDS` gains `"crd_id",` as its first line (new line 235).
  - Both literals keep their alphabetical order. `_MIRROR_REQUIRED_FIELDS`, `_STRING_METADATA_FIELDS`, `_metadata_type_error`, `_mirror_record_error`, `_load_evidence_graph`, the strict Epic predicates and `evaluate_acceptance_map_viability`'s CRD refusal are unchanged, as R-5 requires.
  - Rejected: adding `crd_id` to `_STRING_METADATA_FIELDS` (it would change "the other metadata checks", which R-5 keeps, and model a non-string `crd_id`, which no real producer writes: instruction §4 stated limit); a new shared constant naming the change-container keys (a new name for one key, used twice).
- **PD-10, no further test.** Instruction §4 allows one only "for a condition these leave unprotected" (addendum 2.11 rule 2). Every real input that reaches R-4 or R-5 is a close-pack row written by the sole writer (§6). It is exercised now by V-3 and, once the close pack is on `main`, on every run by the skeleton test itself (evidence lane) and by `test_current_acceptance_inputs_are_strictly_viable` (qa lane). A regression that removed `crd_id` again would need a future edit to one of the three files; that is a constructed input under addendum 2.11 rule 5 and justifies no test. The negative controls of §12.4 show each of R-4 and R-5 is necessary; they are rehearsals, not committed tests.
- **PD-11, the prototype diff covers all three files.** One `git diff` from e1010b5 to the prototype head b4748fe: R-1 to R-3 as plan v1.0's hunks, byte for byte, plus PD-8 and PD-9. It is the exact change PR-30 applies (§8 step 3).

## 6. Real-input set (addendum 2.11 rules 4 to 6)

- **What the R-1 to R-3 fixtures read:** the real checkout, copied whole. Today it holds no HDE-CRD-0002 evidence. After QA-50 it holds the QA family; after the close stage, the close-run family, the close pack and the candidate source. All are planned deliverables of approved stages (rule 4(a)), and the hosted runner runs the lane (rule 4(b)).
- **What R-4 and R-5 read:** the real Index and Mirror. The only rows that carry `crd_id` are the two CRD close-pack rows, which `_crd_close_pack_entries` writes with `"crd_id": crd_id` for an admitted CRD (`update_evidence_index.py` 4046–4066). QA-family and close-run rows carry none. HDE-CRD-0002's close pack is a planned deliverable (Plan v1.1 WU-PR-07 (a)), so the input is real.
- **Stated limits, not modelled (CR-10 (a); rule 5):**
  - A row with both `epic_id` and `crd_id`: the sole writer refuses it (`update_evidence_index.py` 3782–3784, pinned by line 1238's test) and `check_mirror_schema.sh` rejects it (`EPIC_CRD_EXCLUSIVE`, pinned by `test_mirror_schema_accepts_crd_id_and_refuses_epic_and_crd_together`, line 1084) on every evidence-lane run. R-4 and R-5 add no check for it.
  - A non-string `crd_id`: its only producer is the sole writer, which takes the value from `ADMITTED_CRD_QA`'s keys. R-5 adds no type check.
  - The strip helper removes only the paths R-1 to R-3 name. The close stage's two ledgers are not registered by the updater and no evidence-lane test names them; V-3 includes them as supplementary stand-ins.
  - A symlinked root is unlinked, not followed. No real input has one, and the updater refuses an aliased CRD root.
- **No emulation (rule 6):** every fixture and rehearsal calls the real updater and, through it, the real harness.

## 7. Files and requirement-to-change/test map

| Path | Change (prototype) | Resulting blob | Checks |
| :- | :- | :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | +57/−26 (1,383 → 1,414 lines): PD-1 helper; R-2 `crd_repo`; R-1 test; R-3 `CLOSE_SOURCE` and `close_repo` | 8c368caf3b42 (sha256 fae8ed97df6910a2f241e1b74cae344b113080c89ce1abbd232a7f893e5e03dc) | V-1 to V-5 |
| `tests/evidence/test_evidence_skeleton.py` | +1 (656 → 657): PD-8 | f2e0b855c13a (sha256 64c23bae882edf853ea5b913ea46c751a304aedc89d0d8660166bd6c4eb741b7) | V-1, V-3, V-5 |
| `tools/qa/qa_harness.py` | +2/−1 (4,011 → 4,012): PD-9 | 37fd7116d2da (sha256 dcd2093da5b64ebda73757070af1fec12952b755081695e76a09705ce34525b2) | V-1, V-3 (a) and (b), V-5 |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-*` | this plan and its diff; later the PR-30 and PR-35 result records | — | — |

| Requirement | Change | Proof | Prototype |
| :- | :- | :- | :- |
| R-1 | `test_absent_admitted_crd_root_publishes_nothing` builds the absent state in its own copy (PD-3, PD-4) | V-1 (root absent); V-2 (root present); V-4 (planted row) | met: V-1, V-2, V-3 and V-4 |
| R-2 | `crd_repo` strips every root in `ADMITTED_CRD_QA` (PD-5) | V-1; V-2 (`test_crd_0002_fixture_root_publishes_beside_crd_0001` passes with the root present, assertions unchanged) | met: V-1, V-2, V-3 |
| R-3 with C-1 | `close_repo` strips the root, `close/`, the report, the manifest and the candidate source, with proofs and rows (PD-6) | V-1; V-3 (the four close-run tests pass with all close-stage inputs present) | met: V-3 |
| R-4 | `crd_id` in `optional_fields` (PD-8) | V-3 (a) evidence lane; necessity control (§12.4) | met: V-3; necessity shown |
| R-5 | `crd_id` in both harness optional sets (PD-9) | V-3 (a) qa lane; V-3 (b); necessity control (§12.4) | met: V-3 (a) and (b); necessity shown |
| P-1 (acceptance (5) restated) | R-1 in a copy; no evidence-lane test depends on the real checkout's HDE-CRD-0002 state | V-1 to V-4 | met: V-1 to V-4 |
| Limit (three files) | the diff touches exactly the three files | `git diff --stat`; PR-40 attribution | met: 3 files |
| Stated limit (CR-10 (a)) | no both-keys or type check added | the diff; PR-40 | met |
| Exclusions (instruction §7) | none touched | §12 change-set checks; PR-40 | met |

## 8. Implementation sequence for PR-30

1. **Recover before creating.** Inspect this session's checkout, worktrees, branches, open pull requests and `docs/ephemeral/` for WU-REM-01 records. Resume the most advanced consistent state; create nothing that already exists.
2. **Branch.** After this plan's pull request merges, restart the session's designated branch from current `origin/main`. If `main` has moved past e1010b5 outside `docs/ephemeral/`, re-run §4 for the three files, the updater's cited lines, `check_mirror_schema.sh`, `ci.yml` and the classifier's owner table, and record each difference. A decisive difference goes to the instruction's §14 route before any code change.
3. **Apply** `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.1-prototype.diff`: `git apply --check`, then `git apply`. Confirm the three resulting blobs of §7 and that `git diff --stat` lists exactly the three files (+60/−27).
4. **Commit once,** with a message naming the change, for example: `fix(evidence,qa): evidence-lane tests stop assuming HDE-CRD-0002 evidence is absent; skeleton test and QA harness accept crd_id (HDE-CRD-0002 WU-REM-01, FND-001)`.
5. **Validate** the commit as §10 states, before any push.
6. **Pre-push check** (`AGENTS.md`): `python tools/ci/prepush_check.py lanes build-notes`, and `python tools/ci/prepush_check.py --path <path> membership` once for each of the three paths. Expected as in §12.2.
7. **Publish:** push the branch and open one pull request, with the `.github/pull_request_template.md` headings filled under the `AGENTS.md` "PR descriptions" rules ("What merging does" states what becomes current on `main` and that QA, acceptance and closure are not established).
8. **Result record:** `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.0.md`, committed as the pull request's second commit (`docs/ephemeral/` only, as WU-PR-08 did on #687) and read back. It records `PR_CANDIDATE_PUBLISHED`; every check with commands, counts, times and exit codes; the V-2 and V-3 rehearsal outputs, the stand-ins' provenance and the V-3 (b) comparison (amended P-2 evidence obligations); "In-flight decisions" (`NONE` when none); nonclaims; and the PR-35 handoff.

**Integration seams:** the updater's CLI (write and `--check`), the copy's updater module (through `_crd_program`), `ADMITTED_CRD_QA`, the harness's two key sets as read by `_load_evidence_graph` and `_mirror_record_error`, and the Mirror read by the skeleton test. No code changes at any seam besides PD-8 and PD-9.

## 9. PR split and merge dependencies

- **One pull request,** one coherent change in three files. No split: R-4 and R-5 have no value without the close stage that R-3 prepares for, and one vehicle keeps one lineage (proposal v1.1 §10 (a)).
- **Lanes it selects:** `evidence` and `qa`, plus the changed-test step for `tests/qa/test_qa_tool_ownership.py` (§12.2). Adding the result record (`docs/ephemeral/`) adds no lane.
- **Dependencies (amended P-2):** none on unmerged work. This plan's pull request (documents only) merges first.
- **Before merge:** PR-35's `MERGE_PENDING`. The Product Owner merges.
- **After merge:** PR-40 by the whole-change IA; on ACCEPT, the same Isis QA-10 reassessment.
- **No release member, governed artifact or evidence regeneration** is in the change.

## 10. Validation PR-30 runs

**Environment:** CPython 3.12 with CI's install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), the editable install pointed at the checkout under test; then `python -m pytest --version`. Every run goes through `env -i` with closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), `PATH` set to the venv and the system, and `HOME` an empty scratch directory, so no vendor, database or GitHub value reaches a process. Each throwaway clone has no push remote.

1. **Classifier,** as `ci.yml` calls it, base the full `origin/main` SHA, head the commit: exit 0; `reason=selected_lanes;paths=3;lanes=evidence,qa`; `changed_tests=true`; one target, `tests/qa/test_qa_tool_ownership.py`. Also `ci/checks/check_agents_md_citations.py` exits 0.
2. **V-1 on the commit,** each step as `ci.yml` writes it: `ci/checks/check_env_pins.sh`; the evidence step (lines 221–240): the 7 validators exit 0 and the six pytest files pass with no fewer than 134 tests; the qa step (lines 242–271) in a detached worktree: the seven files pass and both tree checks hold; the changed-test step (lines 107–133) in a detached worktree; then the final step's tree checks (`git diff --check`, `git diff --exit-code`, an empty `git status --short --untracked-files=all`).
3. **V-2** in a throwaway clone of the commit: publish the stand-in QA family (§11), commit it in the clone, classify that commit against the PR head, then run the evidence, qa and release steps (lines 221–343) as written. All pass; the tree stays clean.
4. **V-3** in a throwaway clone of the V-2 commit: add the close-stage stand-ins (§11), commit in the clone, classify, then run the evidence, qa and release steps. (a) All pass. (b) Run the read-only viability probe (§11) in the V-2 and V-3 states: each of the 16 `docs/acceptance_map_epic0NN.json` maps has the same status in both, and no result names `crd_id`.
5. **V-4** on the commit, in a throwaway clone: the planted-row mutation of §12.4 makes the R-1 test fail; the unmutated test passes.
6. **Necessity controls (supplementary)** in detached worktrees of the V-3 commit: with `tests/evidence/test_evidence_skeleton.py` restored to e1010b5, `test_mirror_schema_and_parity` fails on `crd_id`; with `tools/qa/qa_harness.py` restored to e1010b5, `test_current_acceptance_inputs_are_strictly_viable` fails and the probe's statuses change and name `crd_id`. Each is restored after.

PR-35 re-runs items 1 and 2 after any correction, and items 3 to 6 when a correction touches a fixture, the helper, R-4 or R-5. **V-5** is PR-35's: hosted CI on the current head, every selected lane and the changed-test step green, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

## 11. Stand-ins (C-1; instruction §9.3)

Produced only in throwaway clones, only through the harness and the canonical updater, plus authored stand-in files. Every one states that it is not QA evidence. Nothing from a rehearsal clone is committed to the repository or pushed.

| Stand-in | Producer | Form |
| :- | :- | :- |
| QA family (V-2) | `writer.publish_crd_check_family(qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT), results, captured_at_utc=<run time>)`, run with the clone as working directory (the script asserts `writer.ROOT == Path.cwd()`); then `qa.validate_crd_check_family` and the updater's `--check` | checks `qa-01-standin` and `qa-02-standin`, each a `qa.CheckResult` with status `PASS` from an executed `python -c "raise SystemExit(0)"` (exit 0), `command_provenance` "WU-REM-01 PR-20 v1.1 V-2 stand-in in a throwaway clone; not QA evidence" |
| Candidate source (V-3, T1) | authored | `audit/HDE-CRD-0002_close_candidate_source.json`: canonical JSON with `change_id` and the note "WU-REM-01 PR-20 v1.1 V-3 stand-in in a throwaway clone; not a close candidate, close pack or QA evidence" |
| Close pack (V-3, T2 and T3) | authored, then indexed by the canonical updater's write and checked by `--check` | `audit/HDE-CRD-0002_close_report.md` (a heading and the note); `audit/HDE-CRD-0002_MANIFEST.json` (canonical JSON with the note) |
| Close-run family (V-3, T5) | `writer.publish_crd_close_run_family(config, results, captured_at_utc=<run time>)`, after the QA family (addendum 2.15); then `--check` | checks `close-pack-check` and `evidence-index-check`, formed as the QA family, provenance "WU-REM-01 PR-20 v1.1 V-3 stand-in close run in a throwaway clone; not QA evidence" |
| Ledgers (V-3, supplementary) | authored | `audit/docdeltas/hde-crd-0002_doc_deltas.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md`, Plan v1.1 WU-PR-07 (a)'s two tracked causal inputs, one heading and the note each; not registered by the updater, so not indexed |
| Viability probe (V-3 (b)) | read-only script | for each `docs/acceptance_map_epic0NN.json`, `qa.evaluate_acceptance_map_viability(qa.HarnessConfig(<epic>, <tree>))`, recording the status and whether the result or ledger text contains `crd_id`. It writes nothing |

The order follows Plan v1.1 WU-PR-07 (b): T1, T2, T3, T5. The stand-in close pack is not writer-produced; the evidence lane checks only its presence, pairing, proofs and rows, and no evidence-lane, qa-lane or release-lane check parses its content.

## 12. Prototype record

Run on 2026-10-23 between 21:04Z and 21:36Z in throwaway clones under this session's scratchpad, all cut from the session checkout at e1010b5. Every clone's push remote was removed; nothing was pushed, and the session checkout was not changed. Each lane run ended with a clean tree.

### 12.1 Environment and method

- **Interpreter:** CPython 3.12.3; one venv per clone, each with CI's install (`pip` exit 0; pytest 8.4.2) and the editable install pointed at that clone; git 2.43.0; 4 CPUs.
- **Rails:** `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PATH` the venv and the system, `HOME` an empty scratch directory, `RUNNER_TEMP` a fresh scratch directory per run. No vendor, database or GitHub value reached any process. `ci/checks/check_env_pins.sh`: `[env-pins] OK`.
- **Lane commands:** the steps of `ci.yml` as written: "Check AGENTS.md cites no project documents", "Verify pytest readiness", "Verify closed deterministic environment", "Run affected behavioral tests in isolation" (107–133), "Run governed evidence integrity lane" (221–240), "Run approved generic QA subsystem lane in isolation" (242–271), "Build and verify exact-source release attestation" (273–343, on the builder's success path; the `release_not_admitted` branch did not arise), and the final step's tree checks (`git diff --check`, `git diff --exit-code`, empty `git status --short --untracked-files=all`).
- **Clone-local commits:**
  - prototype `b4748fe` (tree 9a78782c), the companion diff applied to e1010b5;
  - V-2 `4b7a8a3` on `b4748fe`: the stand-in QA family, 16 paths (+39/−18): two primaries and the step-logs manifest with their proofs, and the ten skeleton files the updater regenerated. The Index then holds 623 rows, 3 of them HDE-CRD-0002's; the Mirror has no `crd_id` row;
  - V-3 `929e567` on `4b7a8a3`: the close stage, 21 paths (+55/−18): the close-run family (two primaries and proofs), the close report and manifest with their proofs, the candidate source, the two ledgers and the regenerated skeleton. The Index then holds 627 rows, 7 of them HDE-CRD-0002's (QA family 3, close run 2, close pack 2); the 2 close-pack rows carry `crd_id` in the Index and the Mirror, and no row carries both `crd_id` and `epic_id`. The candidate source and ledgers have no row.
- **Stand-in times:** the QA family was captured at 2026-10-23T21:20:45Z, the close run at 21:21:20Z.
- **Scripts** (scratchpad, transient; §10, §11 and this section reproduce them): a `ci.yml` step runner, the stand-in script, the viability probe and the V-4 mutation script.

### 12.2 Classifier and pre-push check

| Run | Result |
| :- | :- |
| Classifier as `ci.yml` calls it, base e1010b5 (full SHA), head `b4748fe`, `pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=evidence,qa`; `changed_tests=true`; one target, `tests/qa/test_qa_tool_ownership.py` |
| `ci/checks/check_agents_md_citations.py` on `b4748fe` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| `prepush_check.py --base e1010b5 --head HEAD lanes build-notes` on `b4748fe` | `PASS`: lanes as above, 1 changed-test target; build notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md`, 473,130 bytes, sha256 ee6d55b57b3b922116363dd914264333cf3566c4856819e2a139ed50f7a6604e; "repository unchanged"; exit 0 |
| `prepush_check.py --path` for each of the three files `membership` | `PASS`: release `1.3.0`, roster 45, `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; all three not-member; exit 0 |
| Classifier, base `b4748fe`, head `4b7a8a3` (what a QA-evidence pull request changes) | exit 0; `paths=16;lanes=evidence,release`; `changed_tests=false` |
| Classifier, base `4b7a8a3`, head `929e567` (what a close-pack pull request changes) | exit 0; `paths=21;lanes=evidence,release`; `changed_tests=false`. The qa lane is not selected, which is why V-3 runs it as the next qa-lane pull request would |

### 12.3 Runs

| ID | Head and state | 7 validators | Six evidence-lane files | qa lane, 7 files | Changed-test step | Release lane | Tree after |
| :- | :- | :- | :- | :- | :- | :- | :- |
| V-1 | `b4748fe`, root absent | all exit 0 | **134 passed** in 681.41 s (step 683.3 s) | **488 passed** in 16.93 s; worktree diff and status clean | `tests/qa/test_qa_tool_ownership.py`: **146 passed** in 0.50 s; worktree clean | not selected | clean |
| V-2 | `4b7a8a3`, stand-in QA family | all exit 0 | **134 passed** in 718.52 s (beside V-3) | **488 passed** in 20.22 s; worktree diff and status clean | — | **pass:** manifest check exit 0; **79 passed**; attestation built (exit 0) and verified (exit 0); tree clean; 114.2 s | clean |
| V-3 | `929e567`, plus the close stage | all exit 0 | **134 passed** in 719.14 s (beside V-2) | **488 passed** in 19.75 s; worktree diff and status clean | — | **pass:** manifest check exit 0; **79 passed**; attestation built (exit 0) and verified (exit 0); tree clean; 115.0 s | clean |

- **Lane time (instruction §9.5):** V-1 ran alone on this container: 681.4 s for the six files. The recorded baselines are 696–1,046 s on other containers (instruction §5.6: proposal v1.1 §5.5, plan v1.0 §12.3), and plan v1.0 measured its R-1 to R-3 head within noise of `main` on one container (1,040.5 s against 1,046.0 s). R-4 and R-5 add no test. So the lane shows no growth; no same-container `main` run was made here, so no exact difference is claimed. V-2 and V-3 ran beside each other, so their times do not compare.
- **R-1 to R-3 in V-2 and V-3:** `test_absent_admitted_crd_root_publishes_nothing` and `test_crd_0002_fixture_root_publishes_beside_crd_0001` pass with the root present (V-2, V-3), and the four `close_repo` tests pass with the whole close stage present (V-3).

### 12.4 Negative controls and the viability comparison

**V-4, the R-1 test against a planted Index row** (on `b4748fe`, applied by the mutation script and restored by `git checkout`). Inserted after `_strip_from_copy(repo, "audit/qa/hde-crd-0002")`:

```python
    planted = json.loads((repo / "docs/evidence/INDEX.json").read_bytes())
    planted.append({"artifact_key": "audit.qa.hde_crd_0002.qa_step_logs_manifest", "discovered_physical_path": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "role": "manifest"})
    (repo / "docs/evidence/INDEX.json").write_text(json.dumps(planted, sort_keys=True, separators=(",", ":")) + "\n")
```

| Control | Result |
| :- | :- |
| The R-1 test, unmutated | 1 passed in 6.40 s |
| V-4: planted Index row | **1 failed** in 4.86 s, at the Index assertion (line 1011 of the mutated file; 1008 unmutated): `AssertionError: assert not [{'artifact_key': 'audit.qa.hde_crd_0002.qa_step_logs_manifest', 'discovered_physical_path': 'audit/qa/hde-crd-0002/qa_step_logs_manifest.json', 'role': 'manifest'}]` |
| Supplementary: a root published in the copy (`_success(_crd_program(repo, SECOND_CRD + "writer.publish_crd_check_family(second, (observed(),), captured_at_utc=timestamp)\n"))`, inserted after the existence assertion) | 1 failed: the copy's loader program exits 1 at its assertion. The rows it printed include HDE-CRD-0001's, which also shows the copy keeps the other admitted family (PD-3) |
| R0: FND-001 reproduced. The V-2 state (`4b7a8a3`) with e1010b5's R-1 to R-3 file, the six tests | **2 failed, 4 errors** in 20.05 s: the two root tests FAILED; the four `close_repo` tests ERROR at setup |
| R-4 is necessary. The V-3 state with e1010b5's skeleton test | `test_mirror_schema_and_parity` **1 failed**: `AssertionError: assert {'crd_id'} == set()` at line 539. With R-4: 1 passed |
| R-5 is necessary. The V-3 state with e1010b5's harness | `test_current_acceptance_inputs_are_strictly_viable` **1 failed**: "Human Evidence Index row 567 has unknown fields: ['crd_id']", `FAIL_TOOLING is not PASS`. With R-5: 1 passed in 10.06 s |

Each control ran in a detached worktree or was restored; every tree was clean afterwards.

**V-3 (b), Epic acceptance-map viability.** A read-only probe calls `qa.evaluate_acceptance_map_viability(qa.HarnessConfig(<epic>, <tree>))` for each of the 16 `docs/acceptance_map_epic0NN.json` maps (17 to 20 s per state). It writes nothing. `*` marks a result whose status, reason or ledger text names `crd_id`.

| Map | `main` (e1010b5) | V-1 head (`b4748fe`) | V-2 | V-3 | V-3 without R-5 |
| :- | :- | :- | :- | :- | :- |
| HDE-EPIC021, 027, 028, 029 | PASS | PASS | PASS | PASS | FAIL_TOOLING* |
| HDE-EPIC022, 023, 024 | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING* |
| HDE-EPIC017, 019, 020, 030, 033, 034, 035, 036, 037 | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING |

- **V-3 (b) holds:** every map has the same status in V-3 as in V-2, and no result in either names `crd_id`.
- **R-5 changes no current result:** the 16 statuses on `main` equal those on the prototype head.
- **The probe would see a regression:** without R-5, the four PASS maps turn FAIL_TOOLING and 7 results name `crd_id` ("Human Evidence Index row 567 has unknown fields"), as proposal v1.1 §5.4 recorded for its state C.
- The 12 FAIL_TOOLING maps fail on `main` for reasons unrelated to `crd_id` (OBS-1); the change neither causes nor repairs them.

## 13. Interface contracts (instruction §8)

- **QA-50 and later QA-evidence pull requests:** publishing under `audit/qa/hde-crd-0002/` through `publish_crd_check_family` leaves the evidence lane green with no change to these files. Shown by V-2 (§12.3); that is measure (1)'s proxy.
- **The close stage (S21):** the close-run family, the close pack and the candidate source land without failing the evidence lane; the first qa-lane run after them passes, and Epic viability is unchanged. Shown by V-3 (a) and (b); that is measure (2)'s proxy.
- **The admission table:** R-2 reads `ADMITTED_CRD_QA`. The table is unchanged, and line 965's test still pins it.
- **The mutual-exclusion rule** stays enforced by the writer (line 1238's test, untouched) and by `check_mirror_schema.sh` (`EPIC_CRD_EXCLUSIVE`, run by every evidence-lane run, including V-1 to V-3, and pinned by line 1084's test, untouched). R-4 and R-5 do not duplicate either (CR-10 (a)).
- **Harness users** (`tools/qa/epic021_qa.py`, the Epic close-pack generators, `evaluate_acceptance_map_viability`): on every state without a close pack, R-5 changes no result, because no row carries `crd_id`; on the close-stage state they keep the V-2 statuses (V-3 (b)).

## 14. Security and migration

- Test code and one internal QA tool, neither a release member nor runtime. No secret, credential, network or production surface. The fixtures' subprocesses run under the test file's closed-rails `ENV`; every local run uses `env -i`, so this container's vendor, database and GitHub keys reach no process. No record holds a key value.
- R-5 widens what the harness accepts by one canon-allowed key on Index and Mirror rows (HDE Schemas and Artifacts §8.3); the required keys and every other check stay. On `main` today no row carries `crd_id`, so R-5 changes no current result (§12.4, the V-2 probe).
- **Review chain:** the Codex code review on the pull request, PR-35 for review resolution, PR-40 lineage review. No Codex security review (addendum 2.3).
- **Migration:** none. **Rollback:** the Product Owner reverts the squash commit; no release member changes, so no manifest refresh.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| A strip removes more than intended and hides a regression | Only the named paths and their rows leave; the updater regenerates and checks the copy (PD-1, PD-2); V-1 keeps all 134 tests; V-4 shows the absent-root property still fails when violated |
| R-5 accepts a row it should refuse | Only `crd_id` is added; a both-keys row and a non-string value cannot reach the harness (§6, CR-10); `check_mirror_schema.sh` keeps rejecting a both-keys row on every evidence-lane run |
| Epic viability changes | V-3 (b): the same 16 statuses as V-2, no `crd_id` in any result; the necessity control shows the probe would see it (§12.4) |
| Lane time grows | Measured (§12.3); R-4 and R-5 add no test |
| `main` moves before implementation | §8 step 2 re-measures; a decisive difference goes to the instruction's §14 route |
| A Codex finding on a constructed input, such as the both-keys row or a non-string `crd_id` | Addendum 2.11 rule 7: the traced path and CR-10's stated limit, thread resolved; rule 8 after two consecutive same-class rounds; a P1 on a real input is fixed (addendum 2.14), and declining a P1 goes to the Product Owner first |
| A hosted failure that is not this unit's, such as FND-024 (the PR35-C1 flake) | PR-35 handles it as base-red or flake under its own rules; FND-024 stays with its recorded owner |
| Interruption | Resume in this session from the last saved record; rehearsals only in throwaway clones, discarded and re-cut on failure |

## 16. Boundary findings and observations

**No boundary finding.** None of instruction §14's expected triggers occurred: no change outside the three files was needed; the harness change is the two key additions only; no stand-in rehearsal failed for a reason R-1 to R-5 cannot fix; and no V-3 (b) status differs from V-2 (16 of 16 statuses equal; none names `crd_id`).

**Observations (no action in this unit):**
- **OBS-1, Epic viability already failing on `main`.** 12 of the 16 Epic maps return FAIL_TOOLING on `main` (§12.4), for reasons unrelated to `crd_id`. Not repaired here (instruction §7); the Product Owner owns it as a later-change candidate.
- **OBS-2, `tests/evidence/test_hdapi_v2_contract_inventory.py`.** Not run in this planning session; it is in no lane this change selects. It stays with the QA-10 reassessment and the Product Owner (review v1.1 §3).
- **OBS-3, session identity.** The instruction's receiver field names plan v1.0's session, which is archived; Nathan chose this one (§2.3). Not a blocker; recorded so PR-40 can attribute the lineage.
- **OBS-4, an identifier collision, carried from plan v1.0.** "FND-001" here is QA-10's finding (triage §3), not the WU-OPS-01 receipt's own finding of addendum 2.22.
- **OBS-5, the close-pack pull request runs no qa lane.** It classifies to `evidence,release` only (§12.2). Measure (2)'s qa half is therefore observed on the first later qa-lane run on `main`, which its owners in §17 must look for; nothing in this unit changes that classification (instruction §7).
- **OBS-6, container speed.** V-1's six files took 681 s here; plan v1.0 recorded about 1,040 s on another container and the proposal 696 s on a third. PR-35 records the hosted time.

## 17. Carried items and owners

| Item | Owner |
| :- | :- |
| The Proceed for this exact plan | Product Owner |
| PR-30 (implementation and initial publication), in this session | This WU-REM-01 PR engineering session, after the Proceed |
| PR-35 (review, current-head CI, merge readiness), in its own session | The WU-REM-01 PR-35 session |
| The merge | Product Owner |
| PR-40 lineage review, with both measures recorded "not yet measurable" | The whole-change IA |
| The QA-10 reassessment of S22 and its dependants, including OBS-2 | Isis, after this unit's PR-40 ACCEPT |
| Measures (1) and (2) | The first QA-evidence pull request, the close-pack pull request and the next qa-lane run on `main`, or the QA-10 reassessment |
| CR-10 drainage into HDE Schemas and Artifacts §8.3 | Product Owner |
| OBS-1, the 12 Epic viabilities already failing on `main` | Product Owner, as a later-change candidate |
| CR-9 (path proofs under the Ops evidence root), unaffected | Isis, at IA-30 |
| FND-024, the PR35-C1 flake risk on QA-evidence pull requests | As recorded in the triage |

## 18. Instruction coverage

| Instruction v1.1 | Where this plan meets it |
| :- | :- |
| §1 result and authority boundary | §1; nothing here approves, proceeds, implements, merges or decides QA |
| §2 identity and lineage | Front matter; §2 |
| §3 dependency state | §9 (none on unmerged work; this plan's pull request first) |
| §4 R-1 to R-5, stated limit, Limit, restated acceptance, no new test required | §5; §6; §7; PD-10 |
| §5 baseline | §4 |
| §6 bounded files; expected unchanged | §7; §12 change-set checks |
| §7 exclusions | §7; §11; §14; §12 |
| §8 interface contracts | §13 |
| §9.1 successor plan, reuse stated | §2.1 |
| §9.2 design choices | §5.2 (PD-8, PD-9, PD-10, PD-11) |
| §9.3 stand-ins (C-1) | §11 |
| §9.4 prototype in throwaway clones, counts, times, exit codes, V-3 (b) per map | §12 |
| §9.5 lane time | §12.3 |
| §9.6 baseline re-check | §4 |
| §10 V-1 to V-5, business case | §10; §12; §3 |
| §11 migration, security, real inputs | §14; §6 |
| §12 PR-20 duties; PR-30, PR-35, PR-40 obligations | §8; §10; §20 |
| §13 recovery | §15; §20 |
| §14 rescope behaviour | §16 (no trigger met) |
| §15 unresolved items | §17 |
| §16 canon-conflict register | §19 |
| §17 semantic readiness | §7's requirement map; §12 |

**Approved bases.** Specification v1.1: S22's acceptance intent ("existing Epic and HDE-CRD-0001 inputs still publish and validate") and Constraint "QA evidence admission" are served by V-2, V-3 (a) and V-3 (b); S21's close-run tests and close-pack rows by R-3, R-4, R-5 and V-3. Implementation Plan v1.1 §7: WU-PR-02 acceptance (5) as P-1 restates it is proven in a copy (R-1, V-4); the common PR terms (executor, environment, evidence, migration, rollback, recovery, nonclaims) are kept in §8 to §15, with the reviewer chain read under addendum 2.3. The Implementation Audit is unchanged; this unit adds no surface it did not record (test code and the harness's key sets).

## 19. Canon-conflict register

Carried unchanged: CR-1, CR-2 and CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (a) (IA through RS-20); CR-7 and CR-8 APPROVED (a) each (Product Owner); CR-9 PROPOSED, not yet reviewed (Isis, IA-30), unaffected; CR-10 APPROVED, alternative (a) (Isis, ESC-40, 2026-10-23T20:15:00Z; review v1.1 §4; addendum 2.24), applied as decided in PD-8, PD-9 and §6, drainage into HDE Schemas and Artifacts §8.3 unperformed (Product Owner). **No new conflict.**

## 20. PR-30 invocation package and PR-35 obligations

**The Product Owner's invocation.** PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), for this exact plan, `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.1.md` (v1.1), with `PR_INSTRUCTION_REF` `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.1.md`. The invocation is the Proceed; no other approval object is needed. Its manual prerequisite is that this plan's pull request is merged. The base review stays IA-30 review v1.1; the remediation overlay is review v1.1 with addenda 2.23 and 2.24, and neither replaces the base or creates a successor Plan.

**PR-30, in this session, owns:**
- recovery before creating anything (§8 step 1), with `glow-hde-pr-development` as its sole primary skill;
- challenging the plan's assumptions on the current head (§8 step 2), and the boundary cases §6 states as limits;
- implementing only the three-file change by applying the companion diff (§8 step 3);
- the local validation of §10 items 1 to 6, before the push;
- one coherent commit, the pre-push check, the pull request and the result record (§8 steps 4 to 8);
- `PR_CANDIDATE_PUBLISHED` and one PR-35 handoff to PR-35's own session, naming the result record, this plan, the instruction and the pull request.
- A material boundary found during implementation goes to one `RESCOPE_REQUEST` for the same whole-change IA through RS-20, with `PR_RETURN_PHASE` `PR-30_PREPUBLICATION` or `PR-30_POSTPUBLICATION`.
- PR-30 does not resolve reviews, wait on hosted CI for readiness, merge or claim merge readiness.

**PR-35, in its own dedicated session, owns:**
- retrieving and dispositioning the Codex code review findings under addendum 2.11 rule 7 and addendum 2.14: a P1 on a real input is fixed; declining a P1 goes to the Product Owner first; a finding on the both-keys row or a non-string `crd_id` gets the traced path and CR-10's stated limit (§6); rule 8 applies to a repeated finding class;
- no Codex security review (addendum 2.3);
- re-running §10 items 1 and 2 after any correction, and items 3 to 6 when a correction touches a fixture, the helper, R-4 or R-5; coherent corrective commits;
- V-5 on the current head, economical use of hosted CI, current-head identity and mergeability; a failure red on the base too is handled as base-red, not by widening the unit;
- `MERGE_PENDING` without merging, and the conditional PR-40 handoff.

**After the merge:** PR-40 by the whole-change IA verifies R-1 to R-5 on the merged head and V-1 to V-5 from the records and the hosted run, records both measures as "not yet measurable" with V-2 and V-3 as proxy, and on ACCEPT returns to the same Isis QA-10 reassessment.

**Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change; no HDE-CRD-0002 QA evidence, close pack or close candidate source produced or committed.

## 21. TypeSafe reading for the receiving session (PR-30, WU-REM-01)

Action sent (v8.2): "Implement, as the dedicated pull-request engineering session after the Product Owner's Proceed, an approved detailed plan for a remediation work unit: apply its ready prototype diff to three files (one evidence test file whose absence test and two fixtures build their starting state in a copy, one key added to a second evidence test's allowed set, and one key added to two allowed-key sets in the QA harness; about 60 added and 27 removed lines), then run the plan's local verification (the evidence, qa and changed-test CI steps on the head, two rehearsals in throwaway clones that publish stand-in evidence through the canonical tools and run three CI lanes and an acceptance-map viability comparison, and one negative control), commit once, open the pull request and write a result record. The plan gives the task list; the work is one coherent change, not many independent units; no live run against a provider occurs; Codex code review, hosted CI, a separate review-resolution session and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.00 (confidence 0.67); rung probabilities low 0.00, medium 0.24, high 0.52, extra high 0.23, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.98, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.235, Opus 5.5 at high 0.510, Opus 5.5 at extra high 0.225, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.005, Sonnet 5.5 at extra high 0.002, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-23T21:25:19Z. Nathan picks the cell.
- **Flags:** none printed.
- **Detail:** v8.2 sent 2026-10-23T21:25:19Z; HTTP 200 in 0.57 s; 5547 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `implementation`, before this record was saved.
- **Records:** the Notion row was not written (PR-20 "Mandatory single-block handoff"; addendum 2.1). Nathan's pick for PR-30 is not stated. Nathan's pick for this PR-20 session is not stated; its reading is instruction v1.1 §19.

**Surface advice:** run PR-30 in this WU-REM-01 PR engineering session (https://claude.ai/code/session_01AZdnRebA6fKRxfAgHmLYtP), a Claude Code cloud session on `amthorn78/glow-hdengine-v2` with GitHub access to open the pull request and Notion read access for the prompt.
- **Local runs:** CI's full install on Python 3.12 and closed rails through `env -i`. Allow for three evidence-lane runs (V-1 alone took about 11 minutes here on 4 CPUs; V-2 and V-3 can run side by side), the qa lane (under 20 s per run), two release-lane runs (about 3 minutes each) and the probe and controls (under a minute each).
- **Writes:** the three files on the session's designated branch, the pull request, and the result record under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this plan's pull request is merged first; the Proceed is Nathan's invocation of PR-30 for this exact plan.
- **PR-35** runs afterwards in its own session, which Nathan creates when PR-30 hands off.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | `GCFPE-USE-HDE-CRD-0002-PR-20-20261023-WU-REM-01-02` |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| requirement / work unit | S22, with S21's close-run tests and close-pack rows; WU-REM-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-REM-01 PR engineering session / PR-20 (successor plan) |
| capture time | 2026-10-23T21:36:00Z |
| execution identity | https://claude.ai/code/session_01AZdnRebA6fKRxfAgHmLYtP |
| result | AWAITING_PO_PROCEED; next PR-30 on the Proceed |
| inherited usage | plan v1.0 (`GCFPE-USE-HDE-CRD-0002-PR-20-20261023-WU-REM-01-01`); instruction v1.1 (`GCFPE-USE-HDE-CRD-0002-PR-10-20261023-WU-REM-01-02`); proposal v1.1 (`GCFPE-USE-HDE-CRD-0002-ESC-30-20261023-FND-001-02`); review v1.1 (`GCFPE-USE-HDE-CRD-0002-ESC-40-20261023-FND-001-02`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at e1010b5 (`docs/pfcanon/` last changed by 3b21327, PF10 v13.7.6).

| Decision topic | Sources and sections |
| :- | :- |
| Plan authority, content, result states and handoff | PR-20 — Create Detailed PR Implementation Plan — 100926.1, read in full ("Role and artifact continuity", "Execute" 1 to 10, "Required result", "Next step and recovery", "Mandatory single-block handoff"); PR-30 — PR Implementation Proceed — 100926.1, read in full (its inputs, "Mandatory PR-development execution contract", "Execute" 1 to 6, "Required result") |
| The approved remedy as amended | Instruction v1.1, read in full; remediation review v1.1, proposal v1.1 and the 2.24 record, read in full; the 2.23 record, read in full |
| PF10 authority and the overlays in force | PF10-HDE-Build-Notes v13.7.6: front matter "Precedence, versioning, and scope" (rules 1 to 9) and the Addendum Index; 2.1 (TypeSafe reading), 2.3 (reviewer chain), 2.11 (business case; real inputs; finding disposition; repeated class), 2.14 (P1), 2.15 (close-run family), 2.18 (no ceiling), 2.23 and 2.24 (the remedy), each read in full; 2.5, 2.16, 2.19 and 2.20 as the inputs cite them |
| The Index and Mirror key set; CR-10 | HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.3 "Machine Evidence Index — JSONL mirror", "Allowed top-level keys and unknown-key rejection", read in full |
| The harness's Epic viability, kept by R-5 | HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.6.3 "Generic Epic/CRD QA harness (local records, governed publication, legacy viability)": "Identity and local recording", "Current-family validation and publication" and "Explicit legacy Epic compatibility" ("Preserve the existing Epic logic and strict predicates"), read |
| The objective | Specification v1.1-approved: S21 and S22 rows, Constraints "QA evidence admission", the Distillation row; Implementation Plan v1.1 §7 common PR terms and WU-PR-02 (acceptance (5)), WU-PR-07 (a) (the close mutation set) |
| Evidence writer, CI and PR rules | `AGENTS.md`: canon-first rule; closed rails; pytest readiness; pre-push check; "Governed evidence rules" (sole writer; no hand-editing); QA output placement; "Code review guidelines" (real-input rule); "PR descriptions"; "Evidence attribution, currentness and distinct decisions" |
| Repository facts | As §2.2 lists them, with the blobs and hashes of §4 and §7 |

Canon searched (`git grep` on `origin/main -- docs/pfcanon/`) for `crd_id` and its escaped form `crd\_id`, `WU-REM-01`, `FND-001` and `viability`:
- `crd_id`: HDE Schemas and Artifacts §8.3 (lines 2310–2339, read above); HDE Mechanics Guide §1.6.3 (`HarnessConfig`, lines 902 and 905, read above); PF10 2.24 and its index line (read in full); and an HDE CRD Records template heading (`<CRD_ID>`, a case-insensitive hit) that does not bear on key sets.
- `WU-REM-01`: only PF10's index lines, 2.23 and 2.24 (read in full).
- `FND-001`: PF10 2.22, which names the WU-OPS-01 receipt's own finding, a different item; 2.23 and 2.24 (read in full); the other hits are template examples (Change Process Guide, Plan Templates), a historical Epic summary (HDE Phased Epics) and a Reality Audits table, none naming this finding.
- `viability`: thirteen files. HDE Mechanics Guide §1.6.3 (read above) governs the harness's viability behaviour. The other hits govern Epic acceptance-map and viability-log artifacts (their homes and testability, and the Glow QA Guide's rule that viability evidence precedes dependent Live QA) or name historical Epic logs. None changes R-5, which keeps the Epic predicates as they are.
