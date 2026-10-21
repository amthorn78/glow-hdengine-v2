---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-07-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
progression: TERMINAL_PRODUCT_OWNER_RETURN
predecessor: none (the first PR-40 review of WU-PR-07)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
work_unit_title: "Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation; S21)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 3df86c4c6a43)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1; the Product Owner's PR-30 Proceed for exactly v1.1; blob 6cbe99d70018)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 1fe7f038492b)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.20.md (MERGE_PENDING, historical pre-merge evidence for head 073e5d6; blob 73245fc15335); checkpoints v1.1 to v1.19 in the same lineage (v1.10 and v1.16 MERGE_PENDING, withdrawn by v1.11 and v1.17)
PR_REFS: amthorn78/glow-hdengine-v2#668 (the unit's one PR); companion amthorn78/glow-hdengine-v2#670 (a separate Product Owner-directed test fix against main, carried by #668)
entry_event: the Product Owner's assertion that he manually merged #668 and #670 (the PR-40 invocation of 2026-10-21); no MERGE_OBSERVED result reached this session. The assertion authorized this review only; the merged state below was verified independently
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), continuing the IA lineage of https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j and https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah
reviewer_independence: this session authored no plan, code, result or ADR text of WU-PR-07. The IA lineage authored instruction v1.0, the rescope review v1.0 and the AQ-1 review v1.0; their defects are recorded as the IA's own (LR7-O12)
sessions_reviewed: PR-20/PR-30 https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF; PR-35 https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA
return_owner: the whole-change IA for Plan progress; the Product Owner for the pending decisions of §12
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38.234Z, fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_state_reviewed: origin/main a4189c59dfcab8510b39bd8d9fcffddfcb6d4737 (tree 051b13f48f01). The unit landed as 8b73b57164591adb3ca15ea9cba53071c7f579be; the later commits 4ab35a5 (#669), 102e97e (#670) and a4189c5 (#671) change only docs/ephemeral/ or nothing (§3)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (301,279 bytes; sha256 6604d8906d66c05e647109158894cce601e5c116f6ffbe51cca09a3ace37de86; current on main since 8b73b57). Addenda 2.11, 2.12, 2.13, 2.14 and 2.15 read in full in this invocation
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§13)
created_at: 2026-10-21T17:05:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**ACCEPT.** WU-PR-07 (requirement S21) is delivered with sufficient attributable evidence by pull request #668, merged on 2026-10-21T16:21:50Z as squash commit `8b73b57`, whose tree equals the reviewed head's tree.

- **Behaviour.** The v2 close-pack writer, the v2 schema, the close-run family entrypoint, the absent-tolerant CRD close-pack rows, D-1 and D-2 all landed. This review re-ran the unit's tests on the merged tree: the writer's test file passed 905 of 905, and the 25 updater-consumer files passed 1,177 of 1,177 (§9). It also re-ran the unit's terminal-state rehearsal (acceptance (7)) against the merged code in two fresh runs, and both passed (§9.4).
- **Product Owner decisions.** All 21, PO-35-1 to PO-35-21, are on `main` in their final form (§6).
- **Findings.** All 21 Codex findings are resolved. All 20 P1s were fixed and none was declined, so PF10 addendum 2.14 holds (§7).
- **CI.** Hosted CI is green on the merged head and on `main` after the merge (§8).
- **Ceiling.** The unit did not pass its cost ceiling (§10).

**One documentation defect is open, outside the implementation (LR7-O1).** One clause of the approved ADR's "Stated limits" (line 65) still says `SATISFIED` "needs every recorded status to be `PASS`". That contradicts PO-35-13, which the same ADR records correctly at lines 5, 21 and 50, and which the code and tests implement. It changes no delivered behaviour. The correction route is the Product Owner's, as the ADR's owner (§12). This defect is not an implementation, review, corrected-code or lineage defect, so it is not PR-40's REJECT branch.

**What ACCEPT is not.** It is a delivery verdict against the approved scope. It is not any of the following:
- QA, acceptance of HDE-CRD-0002, Ops, deployment or release activation;
- PF09 or PF30 movement, canon drainage or closure;
- the business-case measure, which is checked at HDE-CRD-0002's close (§10).

The writer and the close-run family are capability only. No close pack of any change exists.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-07 (Implementation Plan v1.1 §7, "WU-PR-07 — Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation)") |
| Requirement | S21 (Specification v1.1); CD-1 (resolved by S21); EC-10; IF-3; IF-4 |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (v1.1, "ASK OK."; blob c4802a5a7fa3) |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md` (blob b39ac9f276db) |
| Implementation Plan and review | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (blob abffa2ccbd44); `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (Isis, IA-30 INITIAL_APPROVE; blob 0cc0276524b2) |
| Business case and ceiling | `docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md` (Product Owner, 2026-10-20; blob 88a65d8a4663) |
| Rescope | `docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md` (RS-20 APPROVE, D-1 and D-2; blob 1390886305fc); PF10 addendum 2.13 |
| AQ-1 | `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md` (blob 5b4301430d4c); PF10 addendum 2.15 (approved with changes, conditions C-1 to C-4 before merge) |
| P1 rule | PF10 addendum 2.14 |
| Instruction, plan, results | the header IDs; PR-30 result v1.0; PR-35 records v1.1 to v1.20 |
| ADR | `docs/adr/hde/close_pack_writer_adr.md` (blob fcaa9da66fb7 on main), "Approved with changes by the Product Owner on 2026-10-20", amended 2026-10-21 (PO-35-7 to PO-35-21) |

## 3. Merge state and landed lineage

| PR | State | Merge evidence | Head | Base | Size |
| :- | :- | :- | :- | :- | :- |
| #668 | merged by amthorn78, 2026-10-21T16:21:50Z | squash commit `8b73b57164591adb3ca15ea9cba53071c7f579be`, one parent `390bc99` (#667); tree `a05a825f00ad`, **equal to the tree of head `4ae2033`** | `4ae2033f5067d1b325091abf5b9d5b9d18c30e10` (branch `claude/gallant-cerf-ysdde5`, deleted after merge; read through `refs/pull/668/head`) | `main` `390bc99` (unchanged between the PR's last base and the merge) | 58 commits, 36 files, +7,633/−38 |
| #670 | merged by amthorn78, 2026-10-21T16:23:02Z | squash commit `102e97e`, parent `4ab35a5`; tree `3697204807d3`, **equal to its parent's tree**: an empty change on `main` | `606e1b4` (an ancestor of `4ae2033` through #668's merge commit `cf39b95`) | `main` `390bc99` | 3 commits, 3 files, +57/−20 |

Order on `main`:
1. `8b73b57` (#668)
2. `4ab35a5` (#669: the IA's records — the AQ-1 review, the page-ready texts of addenda 2.14 and 2.15, and the continuity record; `docs/ephemeral/` only)
3. `102e97e` (#670: empty)
4. `a4189c5` (#671: TypeSafe ladder records under `docs/ephemeral/typesafe-ladder/`; unrelated)

`git diff --name-only 8b73b57 a4189c5` lists only `docs/ephemeral/` paths. #670's three files are byte-identical on `main` to its head, except the writer test file. That file's `606e1b4` → `8b73b57` diff only adds lines (0 removed): #670's version plus #668's own additions.

**The record commit `4ae2033`** adds exactly one file to the reviewed head `073e5d6`: `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.20.md` (`git diff --name-status 073e5d6 4ae2033`). The landed code is therefore the code CI tested and Codex reviewed at `073e5d6`.

## 4. Attribution

| Path | Change | Attributed to |
| :- | :- | :- |
| `schemas/close_candidate_source.v2.json` (new, 697 lines) | IF-3 and the PO-35 narrowings | WU-PR-07: `1080f77` and the PR-35 corrections to `d50cddb` |
| `tools/qa/generate_epic_close_pack.py` (+1,072) | the v2 model beside v1 | WU-PR-07 (same lineage) |
| `tests/qa/test_generate_epic_close_pack.py` (+1,862) | the v2 tests; the five v1 tests made true under a `strictatime` `/tmp` (`b50c79b`, `367afbd`, also #670's) | WU-PR-07; the five-test change is shared with #670 |
| `tools/evidence/update_evidence_index.py` (+170) | `publish_crd_close_run_family`, the reconciler's close rows, the absent-tolerant CRD close-pack rows | WU-PR-07 (`1080f77`; no PO-35 decision touched it) |
| `tools/qa/qa_harness.py` (+22) | the `family` keyword (plan PD-10) | WU-PR-07 (`1080f77`) |
| `tests/evidence/test_evidence_index_missing_state.py` (+138) | 4 updater tests | WU-PR-07 |
| `ci/checks/classify_ci_changes.py` (+3) | the v2 schema's owner entry (ID-11) | WU-PR-07 |
| `.github/workflows/epic-closeout-validation.yml` (+2/−2) | D-1, the install step only | WU-PR-07 under RS-20 APPROVE (addendum 2.13) |
| `tests/evidence/test_rails_ci_workflow_integration.py` (+4) | D-2 | WU-PR-07 under addendum 2.13 |
| `docs/adr/hde/close_pack_writer_adr.md` (new) | the S21 ADR, approved with changes and amended | WU-PR-07; the decisions are the Product Owner's (AQ-1, PO-35-7 to PO-35-21) |
| `pytest.ini` (+4); `tests/evidence/test_v2_mapped_cache_evidence.py` (+18/−4) | the ubuntu-26.04 test fixes | **#670**, directed by the Product Owner (PO-35-6, record v1.9 §2). They entered #668 through the merge `cf39b95` (in-flight decision, record v1.9 §8) and landed in #668's squash because #668 merged first. **Not WU-PR-07 scope** |
| `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md` → `v13.6.6.md` | the Product Owner's uploads v13.6.4 to v13.6.6 (`c1a41b4`, `a48e0b9`, `abdb6df`), committed at his direction | **Not WU-PR-07 scope**: the Product Owner's canon replacement, current on `main` from the merge |
| `docs/ephemeral/` (21 result records, the AQ-1 proposal v1.0 and v1.1) | the unit's records | WU-PR-07's records; merging preserves them and approves nothing (D21-C) |

- **Unchanged, as the instruction requires:**
  - the v1 schema;
  - `.github/workflows/ci.yml` and every other workflow apart from D-1;
  - `tools/evidence/run_sanity_pipeline.py`;
  - `requirements*.txt`, `pyproject.toml`;
  - every release member and `catalog/manifest.json`;
  - the Index trio, its sentinels, every path proof and the orientation output;
  - `audit/**`; `ADMITTED_CRD_QA`'s rows; `README.md`, `AGENTS.md`, `CHANGELOG.md`.

  Checked with `git diff --stat 390bc99 8b73b57` over those paths: empty.
- **Membership.** None of the twelve changed code, test and configuration paths is a member of release `1.3.0` (45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; §9.3). No refresh is owed.

## 5. Requirement coverage across the work unit

All MET unless noted. The evidence is on `main` at `8b73b57`.

| Requirement | Evidence |
| :- | :- |
| **S21 "produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD"**; acceptance (1) | `test_v2_crd_dry_run_writes_complete_close_pack_and_check_is_read_only` (the 18 headings in order, the pointers, the decision and its posture, the 22 real S-IDs, `key_outputs` as an object of strings); `test_v2_epic_dry_run_uses_the_epic_prefix`; this review's rehearsal on the merged code (§9.4) writes the same 18 headings, `- Closure decision: SATISFIED` and `- Decision posture: review-trace-only` |
| Acceptance (2): the feedback-dependency refusal; identity only by tracked-path digests | `test_v2_schema_is_closed_and_shares_the_v1_feedback_refusal`; `test_v2_refuses_feedback_identities_in_every_free_text_field`; `test_v2_refuses_the_head_identity_like_v1`; `test_v2_refuses_updater_outputs_and_the_close_run_family_as_causal_inputs`. Requirement text is bound by reference (ADR decision 6), so S06 and S11 are expressible |
| Acceptance (3): check mode writes nothing and validates exact committed bytes | `test_v2_check_rejects_committed_bytes_that_differ_from_a_fresh_derivation`; the dry-run test's read-only check; the rehearsal's check runs leave the tree clean, and the idempotent re-run on the terminal state changes no byte |
| **S21 "close-workflow run evidence has a home … that does not reopen an approved QA manifest"**; acceptance (4); IF-4; M1 | `test_close_run_family_publishes_without_touching_the_qa_family`, `test_close_run_publication_refuses_scope_and_restores_on_failure`, `test_close_run_family_refuses_an_unexpected_member`, `test_crd_close_pack_rows_are_absent_tolerant` (no rows, one refused, both rows). In the rehearsal, `git diff C2 C3` over `qa_step_logs_manifest.json` and `checks/` is empty. The Index trio is byte-unchanged at merge (§4) |
| **S21 "the accompanying ADR is approved"**; acceptance (5); AQ-1 | ADR status line (line 3) as addendum 2.15 states it. Affected canon with drainage consequences, lines 78 to 88, include Change Process Guide §3.5.2 and §3.5.2.1; HDE Schemas & Artifacts §1.2 "Close-pack artifacts"; and Glow QA Guide "Close-pack truthfulness and same-run execution" and "Close report requirements". AQ-1 conditions C-1 to C-4 landed in `aa94c34` and later commits (ADR block, decision 9; current approved Specification, decision 4; literal TI field; R-1 to R-4). The amendment of 2026-10-21 is at line 5. Open defect: LR7-O1 (line 65) |
| Acceptance (6): lanes green, all seven, on the exact head | Run 39623318908 on `073e5d6` and run 39628344025 on `4ae2033`: all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Push run 39634092300 on `8b73b57`: the same (§8) |
| Acceptance (7): end-to-end rehearsal, check modes exit 0, byte-stable, no hosted byte | PR-30 ran it on `1080f77` (result v1.0 §4). No PR-35 record re-ran it after the corrections changed the contract. **This review ran it on the merged code in two fresh runs: PASS** (§9.4) |
| CD-1; HDE Schemas & Artifacts §1.2 Epic-only inventory | ADR "Epic-only identity inventory"; the CRD and Epic dry runs |
| D-1, D-2 (addendum 2.13) | The workflow diff is exactly the install step (§4). D-2's four lines are in the named test. In this review's rehearsal, the job's seven checks pass on the terminal state under a `requirements.txt`-only interpreter, in the job's environment. The writer's `--check` passes with `jsonschema` only (ID-10's retained constraint) |
| ID-3 to ID-9 and ID-11 to ID-15 (instruction) | ID-7's invariants: v1 cases unchanged (116 → 166 test functions, v1's kept). ID-8: `publish_crd_close_run_family` per plan PD-4. ID-9: absent-tolerant rows. ID-11: the classifier entry. ID-13: no new emulation (the writer's git reader is HDE-EPIC039's). ID-14: OBS-17 did not recur (LR7-O13). ID-15: the updater consumers (§9.2) |
| Security (instruction §11; addendum 2.3) | Closed rails kept (`CLOSED_RAILS_REQUIRED`). Close-run primaries record argv, exit code, output and the rails pins only. Source paths are validated as tracked and regular. The entrypoint writes only under the admitted root's `close/` and the Index trio, inside one transaction (`test_close_run_publication_refuses_scope_and_restores_on_failure`). The Codex code review is in the chain; the Codex security review is not (addendum 2.3) |
| Documentation | WU-PR-07 has no repository-documentation deliverable beyond the ADR. The stale-document list (plan §18) goes to WU-DOC-01 and the drainage owners |
| Migration and rollback | None. v1 is unchanged. Rollback is the Product Owner's revert of `8b73b57` |
| Dependencies | WU-PR-02's CRD admission model is used unchanged. WU-PR-08 relies on H-2, the absent-tolerant rows (the rehearsal and the updater tests) |

## 6. Product Owner decisions PO-35-1 to PO-35-21 against the landed code and the ADR

A read-only worker built the ledger, and this review spot-checked it (PO-35-13, PO-35-20 and PO-35-21 by reading the code; PO-35-21 and PO-35-13 by the rehearsal and a test). Legend: W = writer, S = v2 schema; W and S lines are on `main`.

| ID | Record | Decision (short) | Finding | Landed evidence (refusal code; test) | ADR | Verdict |
| :- | :- | :- | :- | :- | :- | :- |
| 1 | v1.2 §2 | TI ADR status against the drain ledger; S-row pin; full coverage for SATISFIED | CX7-2, CX7-3 | W 2660–2674, 2788, 2843 (`REQUIREMENTS_TABLE_ABSENT`, `REQUIREMENT_ID_UNBOUND`, `REQUIREMENT_COVERAGE_INCOMPLETE`, `TRACKED_ISSUE_UNBOUND`) | 57 | implemented |
| 2 | v1.3 §2 | K-REQ and AC pins (CX7-4); TI pointer `{binding, heading}` (CX7-5) | CX7-4, CX7-5 | `test_v2_epic_close_binds_the_real_epic_specification` | 57 | CX7-4 implemented; CX7-5 part superseded by PO-35-11 |
| 3 | v1.5 §2 | each change kind reads only its own format | CX7-6 | `test_v2_requirement_format_must_match_the_change` | 57 | implemented (fixture note, LR7-O11) |
| 4 | v1.6 §2 | pinned ledger format; SATISFIED needs all PASS | CX7-7 | W 2548–2570 (`QA_LEDGER_INVALID`) | 65 | implemented; amended by PO-35-13 and PO-35-18 |
| 5 | v1.8 §2 | read each entry's tracked primary | CX7-9 | W 2936–2953; `test_v2_qa_ledger_entries_must_agree_with_their_tracked_primaries` | 65 | implemented (widened by CX7-12) |
| 6 | v1.9 §2 (v1.8 §1 uses the ID for "I can rerun CI manually as needed") | "Fix the tests; do not pin the runner and do not waive" | v1.8 §8 | the five atime tests; #670; `ci.yml` keeps `ubuntu-latest` | — | implemented (ID note, LR7-O8) |
| 7 | v1.9 §2 | every deferral, in both forms, in the ledger; R-2 reworded; audit of every v2 path/ID/pointer field | CX7-10 | W 2798–2800 (`DEFERRAL_UNBOUND`), 2711–2722 (`POINTER_UNRESOLVED`) | 5, 21 | implemented |
| 8 | v1.9 §2 | TI pointer names a register heading | audit | removed by `6cd8649` | 5, 58 | superseded by PO-35-11 |
| 9 | v1.9 §2 | `plan_path` is the current implementation plan | audit | W 2747–2748 (`PLAN_SOURCE_NOT_CURRENT`); `test_v2_plan_path_must_be_the_changes_current_implementation_plan` | 5, 59 | implemented |
| 10 | v1.12 §2 | ledger only in the QA harness's own bytes | CX7-13 | W 2548–2570; `test_v2_qa_ledger_read_agrees_with_the_harness_crd_family_check` | 5, 65 | implemented |
| 11 | v1.14 §2 | TI maps only through an ADR status | CX7-15 | S 264–284; `test_v2_schema_admits_only_the_adr_status_form_of_a_tracked_issue` | 5, 21, 58, 84 | implemented |
| 12 | v1.15 §2 | supporting ledgers' minimum content | CX7-16 | W 2818–2832 (`DOC_DELTAS_INVALID`, `DRAIN_TARGETS_INVALID`) | 5, 60–64 | implemented |
| 13 | v1.17 §2 | an accepted gap names its `TOOLING_BLOCKED` check | CX7-17 | W 2504–2537 (`CLOSURE_OVERRIDE_INVALID`), 2836–2842; `test_v2_closure_override_exempts_only_the_tooling_blocked_check_it_names` (TOOLING_BLOCKED with its gap writes SATISFIED) | 5, 21, 26, 50; **65 contradicts** | implemented in code; ADR defect LR7-O1 |
| 14 | v1.17 §2 | no PO-closeout posture | CX7-18 | S 316–319 | 5, 47 | implemented (narrowed further by PO-35-20) |
| 15 | v1.17 §2 and §4 | one-pass audit of the v2 contract against canon | audit A1–A17 | W 2758–2762 (`QA_RCA_UNBOUND`); the no-over-claim line | 5, 55, 56 | implemented |
| 16 | v1.17 §2 | PF titles from tracked canon file names | A4, A5; CX7-19 | W 2763–2779 (`PF_TITLE_UNKNOWN`); `test_v2_pf_titles_derive_from_the_real_canon_filenames` | 5, 26, 52 | implemented |
| 17 | v1.17 §2 | a deferral's drain target is a register heading | A6 | W 2801–2814 (`DEFERRAL_POINTER_UNBOUND`) | 5, 21, 53 | implemented |
| 18 | v1.17 §2 | QA plan pin and coverage ledger | A7 | W 2439–2448, 2751, 2518 (`QA_PLAN_STEPS_ABSENT`, `QA_PLAN_NOT_CURRENT`, `QA_COVERAGE_INVALID`) | 5, 21, 51 | implemented |
| 19 | v1.17 §2 | `allocation` and reuse boundary | A8 | W 2780–2782 (`ALLOCATION_INCOMPLETE`) | 5, 21, 54 | implemented (reuse boundary required, may be empty; v1.17 §7) |
| 20 | v1.19 §2 | the current QA-120 report is the authorized decision; SATISFIED needs `verdict: PASS`; posture review-trace-only only | CX7-20 | W 2482–2500, 2752–2757, 2838 (`QA_REPORT_INVALID`, `QA_REPORT_NOT_CURRENT`); `test_v2_satisfied_needs_the_current_qa_report_verdict`; rehearsal | 5, 21, 47, 48 | implemented |
| 21 | v1.19 §2 | each MET row binds a PASS check whose plan mapping names it | CX7-21 | W 2452, 2847–2868 (`ACCEPTANCE_EVIDENCE_UNBOUND`); `test_v2_met_criteria_bind_a_mapped_passing_check`; rehearsal (ranges `S01 to S11`, `S12 to S22`) | 5, 21, 49 | implemented |

- No PO-35-22 or later exists.
- The numbers run 1 to 21 without a gap.
- No Product Owner decision touched `update_evidence_index.py` or `qa_harness.py`.

## 7. Reviews and the addendum 2.14 check

**The configured mechanism** is the Codex code review (addendum 2.3; the Codex security review is not in the chain). It ran 19 completed rounds:
- 17 rounds with findings, from `1080f77` to `cec8367`;
- 2 rounds recorded without findings, `a2ba526` (record v1.16) and `073e5d6` (record v1.20).

Five attempts did not complete:
- 2026-10-20 at 19:10 and 20:15, and 2026-10-21 at 03:19, each on the usage limit;
- on `4ae2033`: an automatic attempt that hit the usage limit at 15:53:42Z, and a manual retry the summary marks "Failed" at 16:19:05Z.

There was no human review and no APPROVED or CHANGES_REQUESTED review.

**Findings: 21 threads, 21 resolved.** Each thread has exactly two comments: the bot's finding, then the PR-35 session's reply. Each record row's comment ID, reviewed commit and severity match GitHub.

| CX7 | Severity | Reviewed | Finding (short) | Disposition | Fix |
| :- | :- | :- | :- | :- | :- |
| 1 | P1 | `1080f77` | dotted requirement IDs | fixed | `21c029d` |
| 2 | P1 | `a6c6655` | TI closeout mapping | fixed (PO-35-1) | `e274fbf` |
| 3 | P1 | `a6c6655` | every governing criterion before SATISFIED | fixed (PO-35-1) | `e274fbf` |
| 4 | P1 | `5d04297` | Epic requirement IDs | fixed (PO-35-2) | `f91927f` |
| 5 | P1 | `5d04297` | auditable TI pointers | fixed (PO-35-2); the pointer form later removed by PO-35-11, so the input is a schema refusal | `f91927f`, `6cd8649` |
| 6 | P1 | `0d50b06` | requirement IDs from another change kind | fixed (PO-35-3) | `5717008` |
| 7 | P1 | `45e4cef` | empty QA ledgers | fixed (PO-35-4) | `6392102` |
| 8 | P1 | `b0a7305` | CRD bound to its approved Specification | fixed (AQ-1 C-2) | `aa94c34`, `41e8897` |
| 9 | P1 | `abc0254` | statuses against primary logs | fixed (PO-35-5) | `ff0de6e`, `0fc625d` |
| 10 | P1 | `0b57143` | every deferral ID in the drain ledger | fixed (PO-35-7) | `d7f51b9` |
| 11 | **P2** | `c9bff83` | symlinked close-pack members before indexing | **stated limit** (addendum 2.11 rule 7; P2, not security): "the updater registers a CRD close-pack pair by presence. It relies on the writer, the pair's sole producer, for regular-file members, and on the writer's `--check` to refuse an aliased pair" (record v1.10 §3) | — |
| 12 | P1 | `52bb1f2` | the complete QA primary before trusting PASS | fixed | `4ef99c7`, `2b03694` |
| 13 | P1 | `09c0843` | duplicate check IDs in ledgers | fixed (PO-35-10) | `c32d618`, `78f1eff` |
| 14 | P1 | `170051e` | `close_expectation` vocabulary | fixed | `8f2b640`, `8040d72` |
| 15 | P1 | `3eb31c3` | TI pointers against the cited issue | fixed (PO-35-11) | `6cd8649`, `12bc437` |
| 16 | P1 | `f6e1ad0` | malformed doc-deltas ledgers | fixed (PO-35-12) | `9fe2684`, `0e4ef98` |
| 17 | P1 | `477570d` | validated closure overrides | fixed (PO-35-13) | `4fac34f`, `5d4fe1a` |
| 18 | P1 | `477570d` | PO-closeout posture without a decision | fixed (PO-35-14) | `4fac34f`, `5d4fe1a` |
| 19 | P1 | `5bf0db6` | titles from every tracked PF file name | fixed | `46ab9d2`, `e0c4e2a` |
| 20 | P1 | `cec8367` | formal closure bound to an authorized decision | fixed (PO-35-20) | `d50cddb`, `f458e1f` |
| 21 | P1 | `cec8367` | evidence supports each MET criterion | fixed (PO-35-21) | `d50cddb`, `f458e1f` |

**Addendum 2.14 check: met.**
- There is no P0.
- All 20 P1s are fixed, each with a fix commit in the merged tree and a regression test on `main`. The tests were removed where a later decision deleted the form; the input is still covered (LR7-O10).
- No P1 was declined, deferred or recorded as a stated limit.
- CX7-15, CX7-18 and CX7-20 were fixed by narrowing the design under Product Owner decisions: a typed refusal or a removed option. Addendum 2.14 rules 2 and 4 count that as a fix.
- Before addendum 2.14 existed, the PR-35 session offered to decline CX7-2 and CX7-3. The Product Owner refused, and both were fixed.
- CX7-11 is the only stated limit. It is a P2, which addendum 2.14 rule 6 leaves under addendum 2.11 rule 7.

**Rule 8 (repeated finding class)** was applied by the Product Owner's design decisions: PO-35-5, PO-35-10, PO-35-11, PO-35-12 and PO-35-13 to PO-35-21.

**Corrected-change coverage of the final heads.**
- **`073e5d6` (round 19, no findings): a record-only attestation (LR7-O2).**
  - Record v1.20 §2 cites the bot's summary comment 6296260293 as `has_any_findings: false` at 15:30:17Z. The author's comment 6320495013 (16:04:09Z) says "Your review of `073e5d6` found nothing".
  - The summary comment is edited in place. At 16:19:05Z the failed `4ae2033` run overwrote it, and its edit history needs GraphQL, which this session cannot reach (HTTP 403: "GitHub GraphQL is not available from Claude Code sessions").
  - Corroboration by this review:
    - it read the corrected writer and schema diff of `d50cddb` (113 writer lines) and found no wrong result on a real input;
    - the merged tests pass;
    - the rehearsal exercises the corrected paths: the QA-120 verdict, and the mapped PASS checks with `A to B` ranges.
- **`4ae2033`: no completed review (LR7-O3).**
  - It adds only the v1.20 record, Markdown under `docs/ephemeral/`. `AGENTS.md` "Code review guidelines" and "Code review scope" put that file outside code-review scope.
  - CI passed on it (run 39628344025).

## 8. Hosted CI

A read-only worker read all 26 job logs whole: line counts equal the API's `original_length`. The ledger was then reconciled against record v1.20 §6.

| Branch or ref | Runs | Result |
| :- | :- | :- |
| #668 (`claude/gallant-cerf-ysdde5`) | 23 | 18 success, 4 failure, 1 cancelled (`1080f77`, superseded at 35%) |
| #670 (`claude/mapped-cache-test-same-filesystem`) | 2 | 1 failure (`84e1c26`, the quota), 1 success (`606e1b4`) |
| `main` (push) | 1 | success: run 39634092300 on `8b73b57`, ubuntu-26.04 20261018.168.1, `event=push;reason=selected_lanes;paths=37;lanes=product,compat,db,rails,evidence,qa,release`, changed tests 4,521 passed and 2 skipped, every lane passed, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

- **Every success passed all seven lanes:**
  - product 77;
  - compat 119 passed, 3 skipped, 2 xfailed;
  - db 269;
  - rails 120, 113, 155 and 138;
  - evidence 134;
  - qa 488;
  - release 79;
  - and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Runner images.** The six earliest successes ran on ubuntu-24.04 (`f42dd52` on 20261018.339.1, the others on 20261012.334.1). Every run from `45e4cef` onwards ran on ubuntu-26.04, image 20261012.163.1 or 20261018.168.1.
  - Record v1.20 §6 left eight successes as "image not read" (`52bb1f2` to `cec8367`). All eight ran on ubuntu-26.04 (LR7-O7).
- **The four #668 failures** (`45e4cef`, `b0a7305`, `abc0254`, `0b57143`) were the same 7 tests: 2 mapped-cache cross-device tests and 5 atime metadata tests. These are `main`'s own tests under ubuntu-26.04's separate `strictatime` `/tmp`, fixed by #670 and `b50c79b`/`367afbd` (PO-35-6). Run 39523821233 on #670 failed 43 evidence tests and 1 error on `[Errno 122] Disk quota exceeded`, fixed by `pytest.ini`'s `tmp_path_retention_policy = failed`.
- **No waiver** exists or was used. No runner pin. No commit message in `390bc99..4ae2033` carries a CI-skip marker.
- **Other workflows.** `epic-closeout-validation.yml` has never run: its first hosted run is HDE-CRD-0002's T7 (addendum 2.13).
- **Merges without a push run.** `4ab35a5` and `a4189c5` change only CI-exempt `docs/ephemeral/` paths, and `102e97e` changes nothing, so none triggers `ci.yml`.

## 9. Checks run by this review on the merged tree

Each check ran in detached scratch clones of `8b73b57` (`--no-hardlinks`) under the session scratchpad, with:
- CPython 3.12.3 in a venv with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`), pytest 8.4.2, git 2.43.0, ruby, bash and curl;
- closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`;
- `ENGINE_ENV`, `DATABASE_URL`, vendor keys and GitHub tokens unset, an empty `XDG_STATE_HOME`, and `PYTHONPATH` set to the clone under test.

Exit codes are the producer's own. Each clone's `git status --short --untracked-files=all` was empty afterwards. None of this is CI's result, QA or governed evidence.

### 9.1 The writer's test file

`python -m pytest -q -p no:cacheprovider tests/qa/test_generate_epic_close_pack.py`: **905 passed** in 125.69 s (16:35:39Z to 16:37:45Z), exit 0.

### 9.2 Every updater consumer (ID-15; LR-O2)

The 23 test files on `main` that reference `tools/evidence/update_evidence_index.py`, other than the writer's test, plus `tests/qa/test_generic_qa_harness.py` and `tests/evidence/test_http_reader_ci_ownership.py`: 25 files in one run, from 16:35:55Z. The rails workflow test (D-2) is among them. Result: **1,177 passed** in 833.12 s (16:35:55Z to 16:49:48Z), exit 0; the clone's status and diff were empty afterwards.

### 9.3 Read-only checks, lanes and membership on `8b73b57`

| Check | Result |
| :- | :- |
| `update_evidence_index.py --check` | exit 0 |
| `orientation_demo.py --check` | exit 0 |
| `ci/checks/check_mirror_schema.sh` (a Python script, run directly) | exit 0 |
| `ci/checks/check_evidence_index_hash.sh` | exit 0 |
| `validate_evidence_paths.py` | exit 0 |
| `ci/checks/check_final_lf.sh` | exit 0 |
| `ci/checks/check_env_pins.sh` | exit 0, `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` |
| `prepush_check.py --base 390bc99 --head 8b73b57 lanes` | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=37;lanes=product,compat,db,rails,evidence,qa,release`, classified in a throwaway copy |
| `prepush_check.py membership build-notes` with the twelve non-document paths | every path `not-member` (release 1.3.0, 45 members, `release_id` 77204764…); build notes `PF10-HDE-Build-Notes-v13.6.6.md`, 301,279 bytes, sha256 6604d890…de86; "repository unchanged" |

### 9.4 Terminal-state rehearsal on the merged code (acceptance (7); addendum 2.13 validation)

The PR-30 driver (result v1.0 §11) predates PO-35-10 to PO-35-21, and no PR-35 record re-ran a rehearsal. This review adapted it to the landed contract (Appendix A; sha256 `1bec66df67d4ea7c3a61660309317d914eb62e982b90a8d7668721c507621b77`, 209 lines). It ran the driver twice, each time from a fresh clone of `8b73b57`, with the real tools and the real git:

- **T0.** `publish_crd_check_family` for HDE-CRD-0002 with two really executed checks: `env-pins` and `evidence-index-check`.
- **T1.** The candidate source binds:
  - the real Specification v1.1-approved (22 S-IDs) and the real Plan v1.1;
  - a stand-in `HDE-CRD-0002-QA50-qa-plan-v1.0.md` with two `### CHECK` headings mapping `S01 to S11` and `S12 to S22`;
  - a stand-in `HDE-CRD-0002-QA120-qa-report-v1.0.md` with `verdict: PASS`;
  - both ledgers, the QA ledger and both primaries, and the PF30.1 register heading.

  It also carries two deferrals (ADR-status and register-heading forms), one TI, one ADR-block decision and an allocation.
- **T2 and T3.** The writer's `--write` and the updater's write.
- **T4.** The seven checks.
- **T5.** `publish_crd_close_run_family` from the nine captured runs.
- **T6.** The T4 set again.
- **Then:**
  - the hosted job's seven checks under a `requirements.txt`-only interpreter (Flask 2.3.3, jsonschema 4.23.0; no editable install) in the job's environment (closed rails, `GIT_OPTIONAL_LOCKS=0`, `GIT_NO_LAZY_FETCH=1`);
  - the writer's `--check` under a `jsonschema`-only interpreter;
  - an idempotent re-run of T2, T3 and T5 on the terminal state.

| Fact | Run r1 (16:40:03Z to 16:41:01Z) | Run r2 (16:41:24Z to 16:42:21Z) |
| :- | :- | :- |
| Commands | 54, every one exit 0 | 54, every one exit 0 |
| Close report | 18 headings in order; `- Closure decision: SATISFIED`; `- Decision posture: review-trace-only` | same |
| Terminal state | close report, manifest, 9 close-run primaries with 9 path proofs (20 tracked close files) | same |
| QA manifest and `checks/` between C2 and C3 | unchanged | unchanged |
| The job's seven checks, `requirements.txt`-only | all exit 0 (the writer: `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json`); tree clean | same |
| Writer `--check`, `jsonschema`-only | exit 0 | exit 0 |
| Re-run of T2, T3 and T5 on clean C3 | no byte changed | no byte changed |
| Hosted CI | not used; no byte of C3 comes from it | same |

**Byte stability between r1 and r2** (C3 trees `73054441763c` and `13b0cf05273e`):
- **Identical:** the close report (`5bf9840b3b38`), the manifest (`a45011d59807`), `docs/evidence/INDEX.json` (`c34d17ce9ac8`), `INDEX.sha256` (`2e068aa22c2e`), the orientation output (`91acec1866a0`) and every close-run primary.
- **Different:** the 19 differing files are 16 path proofs, the Mirror, its SHA-256 sentinel and the Mirror's own proof. Their only non-hash differences are the `mtime_utc` and `produced_at_utc` lines.

That is capture-time provenance, not a correctness input (`AGENTS.md` "Path-proof portability"), as the PR-30 rehearsal also found.

The stand-in QA plan and report are rehearsal inputs, not QA artifacts. The rehearsal shows the merged code can reach a terminal close state. It does not show that HDE-CRD-0002's real QA artifacts will take the pinned forms (LR7-O4).

## 10. Cost against the ceiling (addendum 2.11 rule 3) and the option A line

**Ceiling** (Product Owner, 2026-10-20): "One PR, with review rounds capped by addendum 2.11 rule 8. At most 4 sessions or 3 days from PR-10 to merge. Past that, the unit returns to the Product Owner."

| Term | Actual | Within? |
| :- | :- | :- |
| One PR | one unit PR, #668. #670 was a separate test fix against `main`, directed by the Product Owner and opened from the PR-35 session; its content is not WU-PR-07 scope (§4) | yes |
| Review rounds under rule 8 | 19 completed Codex rounds (5 further attempts did not complete). Rule 8 led to the Product Owner's design decisions each time a class repeated (§7) | yes, by the Product Owner's decisions |
| Sessions | 4 of 4: PR-10 and the RS-20 review in the IA session (counted as sessions 1 and 3), the PR-20/PR-30 session (2), and the PR-35 session (4), re-entered after a worker restart of about six hours and counted once (records v1.4, v1.5, v1.20) | yes, no slack |
| Elapsed | 2026-10-20T13:14:32Z (PR-10 start) to 2026-10-21T16:21:50Z (merge): **27 h 07 min 18 s, Product Owner waits included** | yes (3 days) |

Actual spend:
- 58 commits; 21 result records (v1.0 to v1.20);
- 21 Product Owner design decisions in PR-35;
- 21 Codex findings (20 P1, 1 P2) over 19 completed rounds;
- 23 hosted runs on #668, 2 on #670 and 1 push run on `main`;
- PR open to merge 23 h 31 min (16:50:45Z to 16:21:50Z).

**The measure** is "HDE-CRD-0002 closes through the ordinary Close Gate with the new writer on the first attempt". It is checked at HDE-CRD-0002's close and is not yet evaluable. Its preconditions now include the QA artifact forms of LR7-O4.

**Option A line** (disposition record §3; instruction ID-17): **no hosted CI failure in this unit's lineage was one a local replay would have caught.**
- All five hosted failures (4 on #668, 1 on #670) were runner-image failures on ubuntu-26.04:
  - the separate `strictatime` `/tmp`;
  - the cross-filesystem move;
  - the size-limited `/tmp`.
- `prepush_check.py replay` runs on the session's own image, where `/tmp` shares the checkout's filesystem. The replays recorded before those pushes passed (`0fc625d`, record v1.8 §6; `84e1c26` on #670, record v1.9).
- The later replays ran in a private mount namespace with a 2 GB `strictatime` tmpfs `/tmp` (records v1.9 and v1.19). That is a change to the environment, not to the tool.

Under the stop rule, the replay report is removed in a later change if no such failure is recorded by QA-10 readiness. That is the Product Owner's decision at QA-10.

## 11. Findings, observations and owners

No defect is open against the delivered behaviour. LR7-O1 is the one open documentation defect.

| ID | Finding or observation | Owner and route |
| :- | :- | :- |
| LR7-O1 | **ADR self-contradiction on PO-35-13.**<br>- `docs/adr/hde/close_pack_writer_adr.md` line 65 ends "…and `SATISFIED` needs every recorded status to be `PASS`." That clause came in with `6392102` (PO-35-4) and survived `5d4fe1a` and `f458e1f`.<br>- Lines 5, 21 and 50 state PO-35-13: a `TOOLING_BLOCKED` check named by a closure-override gap does not block `SATISFIED`.<br>- The code (W 2519–2535, 2836–2842) and `test_v2_closure_override_exempts_only_the_tooling_blocked_check_it_names` (that case writes a SATISFIED pack) follow PO-35-13.<br>- Effect: a drainage owner reading line 65 alone would record the superseded rule. No behaviour is wrong | Product Owner, as the ADR's owner (HDE Governance §9.7.3). The correction is one clause, made only on his instruction. This review does not edit the ADR |
| LR7-O2 | **Round 19 on `073e5d6` rests on records.** The "no findings" result is attested by record v1.20 §2 and comment 6320495013. The bot's summary comment was overwritten at 16:19:05Z, and its edit history is not reachable from this session. This review read `d50cddb`'s writer and schema diff, which is the round-18 correction, and found no wrong result on a real input. The tests and the rehearsal exercise it | Product Owner, optionally: the summary comment's edit history in GitHub's interface shows the 15:30 revision. Not blocking |
| LR7-O3 | **The record commit `4ae2033` has no completed Codex review.** There was an automatic usage-limit stop and a "Failed" manual retry. The summary comment now reads `status: failed`, `has_any_findings: true`, `has_unresolved_findings: true` for `4ae2033`. No unresolved thread exists (21 of 21 resolved). The commit adds only out-of-scope Markdown | none |
| LR7-O4 | **The close sequence H-1 needs updating.** H-1 as restated in result v1.0 §5 predates PO-35-10 to PO-35-21. At T1, HDE-CRD-0002's close now needs:<br>- its QA plan as `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v<N>.<N>.md`, with `### CHECK <n> \`<id>\`` headings in order and `Surface / D-goal mapping:` lines that, together, name all 22 S-IDs;<br>- its QA report as `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v<N>.<N>.md`, with front matter `artifact_type: QA_REPORT`, `change_id` and `verdict: PASS`;<br>- an allocation; an ADR block; ledgers in their pinned minimum content; and each MET row bound to a mapped PASS check's primary.<br>Another format needs a later writer pin, which would defeat the measure's "first attempt". Appendix A is a working restatement against the merged code | HDE-CRD-0002's QA planning (QA-50) and QA report (QA-120), then its close mutation set (PO-35-20, PO-35-21; record v1.19 §10). This IA carries it to QA-10 readiness. WU-DOC-01 owns the H-4 usage note |
| LR7-O5 | **Rehearsal not re-run in PR-35.** Plan v1.1 §3 re-runs the rehearsal "only if a writer or updater correction changes behaviour". Sixteen writer or schema corrections followed PR-30, from `21c029d` to `d50cddb` (`git log 1080f77..4ae2033` over the writer, the v2 schema and the updater), and no PR-35 record re-ran it. This review ran it on the merged code (§9.4) | closed by this review |
| LR7-O6 | **Paths the instruction lists as expected unchanged changed on `main` through #668's squash.** `pytest.ini` and `tests/evidence/test_v2_mapped_cache_evidence.py` are #670's (PO-35-6; in-flight decision v1.9 §8). The workflow change is D-1 (addendum 2.13), and `docs/pfcanon/` holds the Product Owner's uploads. None is a WU-PR-07 scope change, so no rescope was owed | none (attribution recorded, §4) |
| LR7-O7 | **Record v1.20 §6 lists eight successes as "image not read".** All eight ran on ubuntu-26.04: 6 on 20261012.163.1 and 2 on 20261018.168.1 | none; history not rewritten |
| LR7-O8 | **Two PO-35 ID issues.**<br>- PO-35-6 has two contents: in record v1.8 it is the statement "I can rerun CI manually as needed"; in v1.9 it is the decision "Fix the tests; do not pin the runner and do not waive".<br>- The PO-35-N series is reused across units: WU-PR-06's PO-35-1 to PO-35-6 are different decisions, cited in PF10 and in instruction v1.0. ADR line 5 qualifies each citation by record path; lines 21 and 47 to 65 do not | readers resolve a PO-35 ID by its record path; no action owed |
| LR7-O9 | **A TI closed as satisfied cannot be expressed in v2.**<br>- HDE Governance §2.0.19 asks for `PF09 pointers:`, `TI-<id> pointers:` and `ADR status line:` fields when a TI item is closed as satisfied. Change Process Guide §3.5.2.1 allows form (a), PF09 subtask pointers, or form (b), an ADR status line.<br>- PO-35-11 narrowed v2 to form (b) only, because no PF09 or PF30 file cites a TI ID (ADR line 58). That also narrows addendum 2.15 C-3's pointer field.<br>- Form (b) satisfies §3.5.2.1, so this is a stated limit, not a canon conflict | Product Owner, through the ADR's drainage targets (HDE Governance §2.0.19 row) |
| LR7-O10 | **Superseded tests and incomplete real-input cells.**<br>- Tests cited for CX7-2's reply and CX7-5 were removed when PO-35-11 deleted the pointer form (`6cd8649`; record v1.14). CX7-5's input is now a schema refusal, which `test_v2_schema_admits_only_the_adr_status_form_of_a_tracked_issue` covers.<br>- Records v1.2 and v1.3 have no "Real input?" column for CX7-2 to CX7-5, and the cells for CX7-7 and CX7-9 are partial. All were fixed | none |
| LR7-O11 | **Fixture notes.**<br>- PO-35-3's Epic fixture carries K041-REQ rows but no AC041 rows. The AC format is tested on the real HDE-EPIC040 Specification and on inline bytes.<br>- PO-35-19's reuse boundary landed as required and allowed to be empty, not as optional (record v1.17 §7; ADR line 54) | none |
| LR7-O12 | **This IA's own defects in instruction v1.0.**<br>- (a) ID-10's premise that the closeout job's other checks pass was not measured under the job's install, and was false (F-1; addendum 2.13 "Instruction premise"). It cost one rescope cycle and plan v1.1.<br>- (b) §4.1 did not map Change Process Guide §3.5.4 or HDE Governance §2.0.19 (AQ-1 review, "This reviewer's own omission"). They became AQ-1 conditions C-1 and C-3.<br>- (c) The AQ-1 review's redline R-2 (the ledger check for the ADR-status form only) and addendum 2.15's one-line R-2 summary ("the deferral's or tracked issue's own ID") disagreed. That was this IA's drafting error. CX7-10 raised it, and PO-35-7 resolved it: the ADR was reworded to cover every deferral, fixed in `d7f51b9` | this IA. For WU-PR-08's PR-10: measure each premise in the environment that consumes it, and map every canon element the unit's outputs must carry |
| LR7-O13 | **OBS-17** (`test_manifest_reader_rejects_new_report_with_old_manifest`) did not recur in the lineage's 26 hosted runs. The mechanism is not established (plan v1.1 §12.5) | QA tool and test owner, through this IA (as LR6-O8) |
| LR7-O14 | **Ruby on ubuntu-26.04.** Ruby was available on image 20261012.163.1: the ruby-dependent contract-inventory test passed (record v1.8 §5). Addendum 2.2's open item concerns the undeclared dependency | Product Owner (documentation-delta candidate) |
| LR7-O15 | **CX7-11's stated limit stands.** The updater registers a CRD close-pack pair by presence and relies on the writer and its `--check` | carried with the ADR's stated limits |

Carried unchanged: OBS-P4-1, OBS-P3-5, S19-R01 to S19-R07, X-01 to X-04, LR6-O4, LR6-O5 (this unit did not edit `ci.yml`; the pre-push pin is unaffected) and LR6-O7, with their named owners.

## 12. Next stage and decisions returned to the Product Owner

**Next stage: not runnable.** Implementation Plan v1.1 §7 orders the units:

WU-PR-01 … WU-PR-06 → WU-PR-07 → **WU-PR-08** → WU-DOC-01 → WU-OPS-01 → QA-10.

WU-PR-08 (S01, S16, S17, the `1.4.0` cut) is the next ordered unit. It has two unmet prerequisites:
- **Its business case and cost ceiling** (addendum 2.11 rules 1 and 3). None exists: `docs/ephemeral/`, `docs/prompt_ecosystem_management/` and Notion were searched for "WU-PR-08" and its business case.
- **The S01 real-input fact**: the Railway build command and deploy trigger (addendum 2.11 "Epic, task, and status effects"; addendum 2.12, decision 4).

PR-40's rule for an unmet next-unit dependency applies: preserve this ACCEPT and return the pending decision to its owner. This result is therefore terminal for the invocation, with no continuation handoff.

**Decisions returned to the Product Owner:**
1. **WU-PR-08's business case** under addendum 2.11 rule 1 (beneficiary, evidence, benefit, measure, cost ceiling), **and the S01 real-input fact**, before WU-PR-08's PR-10.
2. **LR7-O1:** whether to correct ADR line 65's clause, and by which route. The ADR is his, and the edit is one clause.
3. **LR7-O2 (optional):** confirm round 19's result from the summary comment's edit history.
4. **Merging this review's pull request.** It carries this record only.
5. Whether to publish a PF10 addendum recording this result, as addendum 2.12 did for WU-PR-06. This review creates none.

**Resume point.** When the Product Owner supplies WU-PR-08's business case and the S01 fact, the next stage is WU-PR-08 through PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a). The whole-change IA runs it, with this review, WU-PR-06's review and the business case as inputs.

## 13. Canon-conflict register

The register is carried unchanged:
- CR-1, CR-2, CR-3 (CANON_RECONCILIATION): APPROVED_AS_CHANGED (Thoth; Specification v1.1 lineage).
- CR-4: APPROVED (Product Owner).
- CR-5: APPROVED_AS_CHANGED (Product Owner).
- CR-6: APPROVED, alternative (a) (IA through RS-20; addendum 2.6).
- CR-7, CR-8: APPROVED, alternative (a) each (Product Owner; addendum 2.7).

There is no new conflict:
- **The S21 canon change** is ADR-covered: Change Process Guide §1.0.5, AQ-1 and addendum 2.15.
- **The close-run family's `close/`-only membership exception** is addendum 2.15's.
- **LR7-O9** is a stated limit within §3.5.2.1's two allowed forms.
- **The review-trace-only posture** is one of HDE Schemas & Artifacts §1.2's named postures, by PO-35-20.

## 14. NOT PRODUCED and NOT EXECUTED

**NOT PRODUCED:**
- a close pack, candidate source, close-run family, QA plan or QA report for any change (the rehearsal's stand-ins lived only in scratch clones);
- a PF10 addendum;
- a business case for WU-PR-08;
- any QA, Ops, acceptance or closure artifact;
- a continuation handoff (terminal result).

**NOT EXECUTED:**
- the attribution-lock collector;
- a full `tests/` sweep or `prepush_check.py replay --full` (hosted CI on `073e5d6`, `4ae2033` and `8b73b57` covers all seven lanes);
- the per-finding negative controls;
- the closeout-validation workflow;
- any live vendor, production or database call.

## 15. TypeSafe reading

TypeSafe: not read. The result is a terminal return to the Product Owner with no receiving session to score. A reading belongs to the record that hands off WU-PR-08's PR-10, once that stage is runnable.

The Product Owner has not stated the model and setting chosen for this PR-40 session. PR-35 record v1.20 §8 holds the reading its author took for this handoff, and it is not reproduced as this session's pick.

**Surface notes for re-running this review's checks:**
- a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`;
- Python 3.12 with CI's install, plus a `requirements.txt`-only and a `jsonschema`-only interpreter;
- ruby, bash, curl and git;
- closed rails with the keys unset;
- throwaway clones.

Observed on 4 CPUs: the writer's test file took 126 s, a rehearsal run about 60 s, and the 25-file consumer run 14 minutes.

## 16. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38.234Z) |
| role/stage | continuing whole-change IA (session "HDE-CRD-0002-2") / PR-40, read-only |
| capture time | 2026-10-21T17:05:00Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| workers | three read-only subagents inside this session: the PO-decision ledger, the finding ledger and the CI ledger. Each finding was reconciled here |
| inherited usage | instruction v1.0 (PR-10); rescope review v1.0 (RS-20); plan v1.1 (PR-20); result v1.0 (PR-30); results v1.1 to v1.20 (PR-35) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `a4189c5`. `docs/pfcanon/` was last changed by `8b73b57`, which brought PF10 v13.6.6; no other PF file changed.

| Topic | Sources and sections |
| :- | :- |
| Review authority, verdicts, next stage, terminal return | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full ("Read-only review boundary", "Execute", "Required result", "Resolve the next approved Plan stage", "PRECISE IN-SCOPE DEFECT → re-plan", "Terminal operator return and receiver compatibility", "Mandatory single-block handoff", "Accepted-final lineage protection"). HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (authorities; merges are Product Owner actions) and §9.1.2 (canon precedence; in-flight documents govern within their scope) |
| Overlays | PF10-HDE-Build-Notes v13.6.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md`):<br>- addendum 2.11 in full (rules 1 to 8; WU-PR-07 and WU-PR-08 effects), read with 2.12's numbering;<br>- 2.12 in full (decision 4, the S01 fact);<br>- 2.13 in full (D-1, D-2, overlaid instruction clauses, validation);<br>- 2.14 in full (rules 1 to 6; P1 check);<br>- 2.15 in full (AQ-1 decision, C-1 to C-4, the close-run family) |
| Close-pack content (S21 "canon-conforming") | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`): §1.0.5 "Canon changes"; §1.0.6; §3.5.1 "Requirement" ("Feedback-free terminal lifecycle", "Exceptional closure record"); §3.5.2.1 "Close-pack files" (TI forms (a) and (b), binary decision, superseded artifact); §3.5.4 "ADR block in the close-pack (all epics)" (closure override; "No posture-only PASS"); §0.4.1.2 (heading and opening). HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §1.2: "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", "Change-container compatibility (normative)", close-report requirements, later-drain vocabulary, decision-posture rule. HDE Governance §2.0.19: "Close report minimal content (normative)" (reuse boundary, PR-to-deliverable allocation, no over-claim rule, TI canon-pointer fields, coverage versus QA plan). Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`): "Close-pack truthfulness and same-run execution (normative)", "Close report requirements (validator-bound; mechanical)", §9.2.15.5, and §9.2.15.6 (opening list) |
| In-flight documents | Specification v1.1 (S21 row); Implementation Plan v1.1 §7 order and the WU-PR-07 block, through the instruction's verbatim quotation; instruction v1.0 in full; plan v1.1 in full; the business-case disposition §1 to §3; result v1.0 §4 (check rows), its section headings and §11 (the driver) in full; result v1.8 and v1.20 in full; result v1.9 §8 and its spend section (by search); the spend sections of v1.4, v1.5 and v1.17; the AQ-1 review (its own-omission paragraph); the rescope review's header; the ADR in full; the continuity record |
| Operative documentation | `AGENTS.md`: canon-first rule; "Code review guidelines" (Markdown excluded; real-input rule) and "Code review scope" (CI-exempt prefixes); "Evidence attribution, currentness and distinct decisions"; closed rails and redaction; pytest readiness; "Path-proof portability"; "PR descriptions"; the truncation guardrail; "HDE-EPIC039 current workflow posture" |

Silence: canon defines no lineage-review predicate beyond the PR-40 prompt and HDE Governance §9.1. It states no business case for WU-PR-08, and no rule for correcting an approved ADR other than its owner's decision (HDE Governance §9.7.3, as instruction v1.0 cites it).

## Appendix A. Rehearsal driver (scratch tool; sha256 1bec66df67d4ea7c3a61660309317d914eb62e982b90a8d7668721c507621b77)

Run it as follows:

`python rehearse_v2.py <repo> <commit> <empty-workdir> <label> <venv-python> <jsonschema-only-python> <requirements-only-python>`

It clones `<repo>` into `<workdir>/<label>`, never touches the source repository, and writes a JSON result and the captures beside the clone.

```python
"""PR-40 scratch rehearsal of Plan v1.1 WU-PR-07 T0-T7-precheck against the landed v2 contract.

Adapted from the PR-30 driver (result v1.0 §11) for the contract as merged (PO-35-10 to PO-35-21):
the source now binds the change's QA plan (QA-50 form) and QA report (QA-120 form), maps each MET
criterion to the primary of a PASS check whose plan mapping names it, allocates deliverables, and
carries an ADR block. Runs only in a fresh clone under <workdir>/<label>.

Usage: rehearse_v2.py <repo> <commit> <workdir> <label> <venv-python> <jsonschema-only-python> <requirements-only-python>
"""
import json, os, re, subprocess, sys, time
from pathlib import Path

src, commit_ref, work, label, PY, PYJS, PYREQ = sys.argv[1], sys.argv[2], Path(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
repo = work / label
RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "PYTHONDONTWRITEBYTECODE": "1"}
BASE = {k: v for k, v in os.environ.items() if k in ("HOME", "PATH", "USER", "LOGNAME", "SHELL", "TERM")}
ENV = dict(BASE, **RAILS, PYTHONPATH=str(repo), GIT_CONFIG_GLOBAL="/dev/null")
JOB_ENV = dict(BASE, **RAILS, GIT_OPTIONAL_LOCKS="0", GIT_NO_LAZY_FETCH="1", GIT_CONFIG_GLOBAL="/dev/null")
CAPTURED_AT = "2026-10-21T00:00:00Z"   # fixed rehearsal capture time (not a live close)
CRD = "HDE-CRD-0002"
log = []

def run(argv, *, py=None, capture=False, env=None):
    argv = [py, *argv] if py else list(argv)
    t0 = time.monotonic()
    cp = subprocess.run(argv, cwd=repo, env=env or ENV, capture_output=True, text=True)
    shown = [a.replace(str(repo), "<repo>").replace(PYJS, "python(jsonschema-only)").replace(PYREQ, "python(requirements-only)").replace(PY, "python") for a in argv]
    log.append({"argv": shown[:4], "exit": cp.returncode, "seconds": round(time.monotonic() - t0, 2)})
    if cp.returncode and not capture:
        print(cp.stdout[-3000:], cp.stderr[-3000:]); raise SystemExit(f"FAILED: {shown[:4]}")
    return cp

def git(*args):
    return run(("git", *args)).stdout.strip()

def status():
    return git("status", "--porcelain=v1", "--untracked-files=all")

def commit(msg):
    git("add", "-A"); git("-c", "user.email=r@example.invalid", "-c", "user.name=rehearsal", "commit", "-q", "-m", msg)
    assert status() == "", status()
    return git("rev-parse", "HEAD")

subprocess.run(("git", "clone", "-q", "--no-hardlinks", src, str(repo)), check=True)
git("checkout", "-q", "--detach", commit_ref)
heads = {"P": git("rev-parse", "HEAD")}
assert not (repo / "audit/qa/hde-crd-0002").exists()

# T0 (precondition stand-in): a real HDE-CRD-0002 QA family published by publish_crd_check_family.
t0 = '''
import subprocess, sys
from tools.evidence import update_evidence_index as writer
from tools.qa import qa_harness as qa
config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)
def observed(check_id, argv):
    cp = subprocess.run(argv, capture_output=True, text=True, check=False)
    return qa.CheckResult(check_id, qa.Status.PASS if cp.returncode == 0 else qa.Status.FAIL_BEHAVIOR,
        status_reason="" if cp.returncode == 0 else f"exit {cp.returncode}", command=tuple(argv),
        command_provenance="executed in a throwaway rehearsal clone", exit_code=cp.returncode, output=cp.stdout + cp.stderr)
writer.publish_crd_check_family(config, (observed("env-pins", ("ci/checks/check_env_pins.sh",)),
    observed("evidence-index-check", (sys.executable, "tools/evidence/update_evidence_index.py", "--check"))),
    captured_at_utc="''' + CAPTURED_AT + '''")
'''
run(("-c", t0), py=PY)
heads["C0"] = commit("rehearsal T0: QA family (stand-in for the recorded QA verdict)")

# T1: the causal inputs: the real Specification and Plan; a stand-in QA plan and QA report.
spec = "docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md"
ids = re.findall(r"^\| (S\d\d) \|", (repo / spec).read_text(encoding="utf-8"), re.M)
assert ids == [f"S{n:02d}" for n in range(1, 23)], ids
qa_plan = f"docs/ephemeral/{CRD}-QA50-qa-plan-v1.0.md"
qa_report = f"docs/ephemeral/{CRD}-QA120-qa-report-v1.0.md"
(repo / qa_plan).write_text(
    "# HDE-CRD-0002 QA plan (rehearsal stand-in)\n\n"
    "### CHECK 1 `env-pins`: Environment pins\n\nSurface / D-goal mapping: S01 to S11.\n\n"
    "### CHECK 2 `evidence-index-check`: Evidence index check\n\nSurface / D-goal mapping: S12 to S22.\n", encoding="utf-8")
(repo / qa_report).write_text(
    f"---\nartifact_type: QA_REPORT\nartifact_id: {CRD}-QA120-QA-REPORT\nverdict: PASS\nchange_id: {CRD}\n---\n\n"
    "# Final QA report (rehearsal stand-in)\n", encoding="utf-8")
(repo / "audit/docdeltas/hde-crd-0002_doc_deltas.md").write_text("Doc Deltas: None\n", encoding="utf-8")
(repo / "audit/docdeltas/hde-crd-0002_drain_targets.md").write_text(
    "# HDE-CRD-0002 drain targets (rehearsal stand-in)\n\n- DEF-1: close-pack canon\n- DEF-2: close-pack canon\n- TI-002: close-pack canon\n", encoding="utf-8")
primary = {"env-pins": "qa_env_pins", "evidence-index-check": "qa_evidence_index"}
ev = [
    {"binding": "specification", "path": spec},
    {"binding": "qa_plan", "path": qa_plan},
    {"binding": "qa_verdict", "path": qa_report},
    {"binding": "doc_deltas", "path": "audit/docdeltas/hde-crd-0002_doc_deltas.md"},
    {"binding": "drain_targets", "path": "audit/docdeltas/hde-crd-0002_drain_targets.md"},
    {"binding": "qa_manifest", "path": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json"},
    {"binding": "qa_env_pins", "path": "audit/qa/hde-crd-0002/checks/env-pins/primary.log"},
    {"binding": "qa_evidence_index", "path": "audit/qa/hde-crd-0002/checks/evidence-index-check/primary.log"},
    {"binding": "register", "path": "docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.1.md"},
]
deliverable = "Rehearsal stand-in for the delivered scope of S01 to S22."
source = {
    "schema_version": "close_candidate_source.v2", "change_id": CRD,
    "plan_path": "docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md",
    "evidence_inputs": ev,
    "requirements_binding": "specification", "qa_plan_binding": "qa_plan", "qa_report_binding": "qa_verdict",
    "acceptance": [{"criterion_id": i, "evidence_bindings": ["qa_manifest", primary["env-pins" if int(i[1:]) <= 11 else "evidence-index-check"]],
                    "result": "MET", "limitation": "Rehearsal stand-in; no QA verdict exists."} for i in ids],
    "deliverables": [deliverable],
    "allocation": [{"slice": "WU-PR-07", "deliverable": deliverable}],
    "reuse_boundary": [],
    "deferrals": [
        {"id": "DEF-1", "adr_status": "Deferred", "rationale": "Drains with the close-pack ADR."},
        {"id": "DEF-2", "drain_target": {"binding": "register", "heading": "**4.2 Material update**"}},
    ],
    "later_drain_statements": [{"canon_homes": ["Change Process Guide"], "locators": ["3.5.2.1 Close-pack files"],
        "current_posture": "Names the Epic filename prefix only.", "action": "No status change recommended",
        "readiness": "Supportable from repo evidence", "evidence_bindings": ["specification"],
        "close_expectation": "after a separate canon-only drain step"}],
    "tracked_issues": [{"id": "TI-002", "adr_status": "Deferred with drain targets"}],
    "adr_block": {"decisions": [{
        "label": "Close-pack writer for Epic and CRD identities",
        "statement": "One writer serves both change kinds through a second source schema.",
        "decision_point": "How a CRD close report is written from tracked inputs.",
        "options_considered": ["Extend the generic writer.", "Add a separate writer."],
        "bounding_canon": ["Change Process Guide", "HDE Schemas & Artifacts"],
        "final_decision": "Extend the generic writer.", "scope": "canonical",
        "doc_delta_targets": ["Change Process Guide"]}]},
    "closure_decision": {"decision": "SATISFIED", "posture": "review_trace_only"},
    "follow_ups": [], "superseded": [],
    "pointers": ["audit/docdeltas/hde-crd-0002_doc_deltas.md", "audit/docdeltas/hde-crd-0002_drain_targets.md",
                 "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "audit/qa/hde-crd-0002/close/"],
    "qa_rca": {"summary_lines": ["Rehearsal stand-in: no QA run or RCA exists for this synthetic candidate."]},
    "key_outputs": {"close_report": "audit/HDE-CRD-0002_close_report.md", "close_manifest": "audit/HDE-CRD-0002_MANIFEST.json",
        "doc_deltas": "audit/docdeltas/hde-crd-0002_doc_deltas.md", "drain_targets": "audit/docdeltas/hde-crd-0002_drain_targets.md",
        "qa_step_logs_manifest": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json"},
    "nonclaims": ["no_canon_drainage_or_register_movement", "no_execution_by_writer", "no_hosted_feedback_inputs", "no_unbound_claim"],
}
SRC = "audit/HDE-CRD-0002_close_candidate_source.json"
(repo / SRC).write_text(json.dumps(source, indent=2, sort_keys=True) + "\n", encoding="utf-8")
heads["C1"] = commit("rehearsal T1: candidate source, QA plan, QA report and ledgers")

captures = []
def step(check_id, argv, py=None):
    cp = run(argv, py=py, capture=True)
    captures.append({"check_id": check_id, "command": ["python", *argv] if py else list(argv), "exit": cp.returncode, "output": cp.stdout + cp.stderr})
    if cp.returncode:
        print(cp.stdout[-3000:], cp.stderr[-3000:]); raise SystemExit(f"step failed: {check_id}")
step("close-pack-write", ("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--write"), py=PY)
step("evidence-index-write", ("tools/evidence/update_evidence_index.py",), py=PY)
heads["C2"] = commit("rehearsal T2-T3: close pack and evidence graph")
T4 = [("close-pack-check", ("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check"), PY),
      ("evidence-index-check", ("tools/evidence/update_evidence_index.py", "--check"), PY),
      ("orientation-check", ("tools/evidence/orientation_demo.py", "--check"), PY),
      ("mirror-schema", ("ci/checks/check_mirror_schema.sh",), None),
      ("evidence-index-hash", ("ci/checks/check_evidence_index_hash.sh",), None),
      ("evidence-paths", ("tools/evidence/validate_evidence_paths.py",), PY),
      ("final-lf", ("ci/checks/check_final_lf.sh",), None)]
for check_id, argv, py in T4:
    step(check_id, argv, py)
assert status() == ""
(work / f"{label}_captures.json").write_text(json.dumps(captures, indent=1))
t5 = '''
import json, sys
from tools.evidence import update_evidence_index as writer
from tools.qa import qa_harness as qa
config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)
results = [qa.CheckResult(c["check_id"], qa.Status.PASS if c["exit"] == 0 else qa.Status.FAIL_BEHAVIOR,
    status_reason="" if c["exit"] == 0 else "exit %d" % c["exit"], command=tuple(c["command"]),
    command_provenance="executed in the same local close run (rehearsal)", exit_code=c["exit"], output=c["output"])
    for c in json.load(open(sys.argv[1]))]
print(len(writer.publish_crd_close_run_family(config, results, captured_at_utc="''' + CAPTURED_AT + '''")))
'''
run(("-c", t5, str(work / f"{label}_captures.json")), py=PY)
heads["C3"] = commit("rehearsal T5: close-run family (terminal state)")
qa_untouched = git("diff", "--name-only", heads["C2"], heads["C3"], "--", "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "audit/qa/hde-crd-0002/checks") == ""
assert qa_untouched
# T6: the T4 set again on clean C3.
for check_id, argv, py in T4:
    run(argv, py=py)
assert status() == ""
# The hosted closeout job's seven checks under the job's own install (D-1): requirements.txt only, job env, no PYTHONPATH.
job = {}
for argv, py in (((("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check")), PYREQ),
                 (("tools/evidence/update_evidence_index.py", "--check"), PYREQ),
                 (("tools/evidence/orientation_demo.py", "--check"), PYREQ),
                 (("ci/checks/check_evidence_index_hash.sh",), None),
                 (("tools/evidence/validate_evidence_paths.py",), PYREQ),
                 (("ci/checks/check_mirror_schema.sh",), None),
                 (("ci/checks/check_final_lf.sh",), None)):
    env = dict(JOB_ENV)
    if py is None:  # shell checks call `python`; put the requirements-only interpreter first on PATH
        env["PATH"] = str(Path(PYREQ).parent) + os.pathsep + env["PATH"]
    cp = run(argv, py=py, capture=True, env=env)
    job[argv[0]] = [cp.returncode, (cp.stdout + cp.stderr).strip().splitlines()[-1:]]
# The writer's --check with jsonschema only (ID-10's retained writer constraint).
cp = run(("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check"), py=PYJS, capture=True, env=JOB_ENV)
jsonschema_only = [cp.returncode, (cp.stdout + cp.stderr).strip().splitlines()[-1:]]
clean_after_job = status() == ""
# Idempotence: T2-T5 again on clean C3 with the same captures changes no byte.
run(("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--write"), py=PY)
run(("tools/evidence/update_evidence_index.py",), py=PY)
run(("-c", t5, str(work / f"{label}_captures.json")), py=PY)
idempotent = status() == ""
files = git("ls-files", "audit/HDE-CRD-0002_close_report.md", "audit/HDE-CRD-0002_MANIFEST.json", "audit/qa/hde-crd-0002/close").splitlines()
report = (repo / "audit/HDE-CRD-0002_close_report.md").read_text(encoding="utf-8")
out = {"label": label, "heads": heads, "tree_C3": git("rev-parse", "HEAD^{tree}"), "qa_manifest_and_checks_untouched_C2_C3": qa_untouched,
       "job_seven_checks_requirements_only": job, "writer_check_jsonschema_only": jsonschema_only, "clean_after_job_checks": clean_after_job,
       "idempotent_rerun_on_C3": idempotent, "close_files": files,
       "report_headings": [l[3:] for l in report.splitlines() if l.startswith("## ")],
       "report_decision_lines": [l for l in report.splitlines() if l.startswith("- Closure decision") or l.startswith("- Decision posture")],
       "commands": len(log), "nonzero": [s for s in log if s["exit"]], "steps": log}
(work / f"{label}_result.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("heads", "tree_C3", "qa_manifest_and_checks_untouched_C2_C3", "job_seven_checks_requirements_only", "writer_check_jsonschema_only", "clean_after_job_checks", "idempotent_rerun_on_C3", "report_decision_lines", "commands")}, indent=1))
print(len(files), "close files")
```
