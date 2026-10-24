---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-REM-01-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
progression: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, the same Isis reassessment of S22 and its dependants (the approved remediation's originating return; §10)
predecessor: none (the first PR-40 review of WU-REM-01)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-01
work_unit_title: "Evidence-lane independence from the HDE-CRD-0002 QA root (PR; Distillation; S22, with S21's close-run tests and close-pack rows)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.1.md (v1.1, INSTRUCTION_READY; blob 768772ec5e8a; #714, squash e1010b5). It superseded v1.0 (blob d89d1dc9991b; #709)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.1.md (v1.1; blob d28458c15047; #715, squash c27d47d; the Product Owner's PR-30 Proceed for exactly v1.1), with docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-plan-v1.1-prototype.diff (blob e286cf0c40bf; sha256 1323f0960a1898ce0515d7ad52dacdabd3350962fe5af2f6af12324697488d8e). It superseded plan v1.0 (BLOCKED on F-1; #710)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 0478fea1362b)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.2.md (MERGE_PENDING on 696c051, historical pre-merge evidence; blob d6b219368838), with v1.1 (MERGE_PENDING on 5abc532; blob dccdc9e47c9a) in the same lineage
PR_REFS: amthorn78/glow-hdengine-v2#716 (the unit's one PR)
entry_event: the Product Owner's fallback PR-40 handoff, pasted after he merged #716 by hand; no MERGE_OBSERVED result reached this session. The merge was verified independently (§3)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md; addendum 2.20)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (blob b39ac9f276db)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44), with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (addendum 2.19). WU-REM-01 is added to its §7 by the remediation overlay's amended P-2
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md (Thoth; blob 12fcbb30585f; #711)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-FND-001 v1.1, docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md (Isis, ESC-40 APPROVE; CR-10 APPROVED (a); blob 126330b8f6b9; #712)
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md §3 (QA-10 FND-001; blob dac6d1a79de8), from docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md (NOT_READY on S22; blob f6d7ff018ce7)
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
reviewer_independence: this session authored WU-REM-01's instructions v1.0 and v1.1 (PR-10), and no plan, code or result record of the unit
sessions_reviewed: PR-20 (plan v1.0) https://claude.ai/code/session_01UnrRbwMW8bPrYjZkNxPmB5 (archived); PR-20 (plan v1.1) and PR-30 https://claude.ai/code/session_01AZdnRebA6fKRxfAgHmLYtP; PR-35 https://claude.ai/code/session_01CjBMTFr8SepLRi97rM6KcL
return_owner: Isis, the continuing Lead Developer and QA-10 readiness owner (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), for the reassessment of S22 and its dependants
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state of 2026-10-12T02:29:38.234Z, fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_state_reviewed: origin/main 3a5d8461e412d386fb6b835461f76d1954dcbf54 (tree cdca58af838e), the merge commit itself; no later commit on main at review time
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.6.md (473,130 bytes; sha256 ee6d55b57b3b922116363dd914264333cf3566c4856819e2a139ed50f7a6604e; last addendum 2.24; unchanged since 3b21327)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried, decided; CR-9 carried PROPOSED, unaffected; CR-10 carried APPROVED (a), applied as decided; no new entry (§11)
created_at: 2026-10-24T00:42:00Z
---

# HDE-CRD-0002 WU-REM-01 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**ACCEPT.** WU-REM-01 is delivered with sufficient attributable evidence by pull request #716. It merged on 2026-10-24T00:14:37Z as squash commit `3a5d846`, whose tree equals the PR's final head `844db2f`.

- **Exactness.** The landed change to the three code files is the proceeded plan v1.1's companion diff, byte for byte (sha256 `1323f096…`; §4). No other code, test, workflow, governed-evidence, release-member or canon file changed.
- **Behaviour.** R-1 to R-5 are on `main` as the approved overlay requires (§5). CR-10's stated limit holds: `crd_id` only, with no both-keys or type check.
- **Reviews.** The Codex code review completed with no findings on the implementation head `9ad4336` and again on the final head `844db2f`. There were no review threads and no formal reviews, so no P1 was raised or declined (§6). The Codex security review is not in the chain (addendum 2.3).
- **CI.** Hosted CI is green on the final PR head (run 40042683632) and on the merge commit (push run 40043995165). Both runs selected the evidence and qa lanes and the changed-test step, and ended `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§7).
- **This review's own checks** on merged `main` and on stand-in states built from it in throwaway clones all pass: V-1, V-3 (a) and (b), V-4 and the necessity controls (§8).
- **Business-case measures (1) and (2):** not yet measurable, as the plan and addendum 2.24 expect. V-2 and V-3 are the proxy, and both hold (§9).

**Next stage:** the remedy's originating return, the same Isis QA-10 reassessment of S22 and its dependants (§10).

ACCEPT is this review's lineage result only. It is not a QA verdict, acceptance of the change, Ops, deployment or closure.

## 2. Inputs read

| Input | Read |
| :- | :- |
| PR-40 prompt (page state 2026-10-12T02:29:38.234Z) | In full, this invocation |
| Instruction v1.1 | This session's own record; the blob on `main` (768772ec5e8a) equals what was written |
| Plan v1.1 and its prototype diff | In full |
| Results v1.0 (PR-30), v1.1 and v1.2 (PR-35) | In full |
| Remediation review v1.1, proposal v1.1, the 2.24 record; PF10 v13.7.6 §2.23 and §2.24 as published | In full in this session for instruction v1.1; unchanged on `main` since |
| QA-10 prompt (page state 2026-10-12T02:30:12.398Z), "Accepted repair delivery → same Isis QA-10 reassessment" and the remediation-return intake | Read for §10 |
| PR #716: details, commits, comments, reviews, review threads, check runs | Through the GitHub API, this invocation |
| Hosted runs 40042683632 (final PR head) and 40043995165 (push on `main`) | Job steps and logs |

## 3. Merge state and lineage

| Fact | Evidence |
| :- | :- |
| PR | #716, `state: closed`, `merged: true`, `merged_by: amthorn78`, `merged_at` 2026-10-24T00:14:37Z |
| Base at merge | `main` `c27d47d` (#715) |
| PR commits, in order | `9ad4336` (implementation, PR-30); `5abc532` (result v1.0, PR-30); `696c051` (result v1.1, PR-35); `844db2f` (result v1.2, PR-35) |
| Final PR head | `844db2f97419b89f4e54e370fbdc366d8ce2f1d0` |
| Merge commit | `3a5d8461e412d386fb6b835461f76d1954dcbf54`, a squash with the single parent `c27d47d`. Its tree `cdca58af838e` equals `844db2f`'s tree |
| `main` at review | `3a5d846`. No later commit, so there is no later divergence to separate |
| Branch | `claude/relaxed-hamilton-vorgjj`, the PR-30 session's branch. PR-35 pushed its records there under PO-35-1 (result v1.1 §6) |
| Proceed | The Product Owner's invocation of PR-30 for exactly plan v1.1, after #715 merged (result v1.0 front matter). It was not reused or renewed |

## 4. Attribution

`git diff c27d47d 3a5d846` changes 6 files, +563/−27:

| Path | Change | Blob on `main` | sha256 | Attributable to |
| :- | :- | :- | :- | :- |
| `tests/evidence/test_evidence_index_missing_state.py` | +57/−26 (1,414 lines) | `8c368caf3b42` | `fae8ed97df6910a2f241e1b74cae344b113080c89ce1abbd232a7f893e5e03dc` | R-1, R-2, R-3 with C-1 (`9ad4336`) |
| `tests/evidence/test_evidence_skeleton.py` | +1 (657 lines) | `f2e0b855c13a` | `64c23bae882edf853ea5b913ea46c751a304aedc89d0d8660166bd6c4eb741b7` | R-4 (`9ad4336`) |
| `tools/qa/qa_harness.py` | +2/−1 (4,012 lines) | `37fd7116d2da` | `dcd2093da5b64ebda73757070af1fec12952b755081695e76a09705ce34525b2` | R-5 (`9ad4336`) |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.0.md` | new | `0478fea1362b` | — | PR-30 record (`5abc532`) |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.1.md` | new | `dccdc9e47c9a` | — | PR-35 record (`696c051`) |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-implementation-result-v1.2.md` | new | `d6b219368838` | — | PR-35 record (`844db2f`) |

- **Byte equality.** `git diff c27d47d 3a5d846` restricted to the three code files is byte-equal to the companion diff (`cmp` equal; both sha256 `1323f0960a1898ce0515d7ad52dacdabd3350962fe5af2f6af12324697488d8e`). The three blobs are the ones plan v1.1 §7 states.
- **Limit (three files).** Met. Every other changed path is a result record under `docs/ephemeral/`, which plan v1.1 §7 lists among the unit's records.
- **Unchanged:** `tools/evidence/update_evidence_index.py`, `.github/workflows/ci.yml`, `ci/checks/**`, governed evidence (Index, Mirror, sentinels, path proofs, orientation), `audit/**`, every release member and `docs/pfcanon/**`.
- **Unattributable or unrelated changes:** none.

## 5. Requirement coverage on `main` (instruction v1.1 §4; addendum 2.24)

| Requirement | On `main` at `3a5d846` | Verified by |
| :- | :- | :- |
| R-1 | `test_absent_admitted_crd_root_publishes_nothing(tmp_path)` copies the checkout and strips `audit/qa/hde-crd-0002` with its Index rows through `_strip_from_copy`. That helper writes the Index, then runs the canonical updater's write and `--check`. The test then asserts the root is absent, runs the loader inside the copy through `_crd_program` (whose `CRD_FIXTURE_PROGRAM` asserts `writer.ROOT == Path.cwd()`), and asserts no Index row under the root. It no longer reads the real checkout | Reading the diff (§4); V-1, V-3, V-4 (§8) |
| R-2 | `crd_repo` strips every root in `writer.ADMITTED_CRD_QA` (today HDE-CRD-0001 and HDE-CRD-0002) through the same helper. Its ten users keep their assertions | Diff; V-1; V-3 (`test_crd_0002_fixture_root_publishes_beside_crd_0001` passes with the root present) |
| R-3 with C-1 | `close_repo` strips `CLOSE_ROOT` (with `close/`), both `CLOSE_PACK` files and the new `CLOSE_SOURCE` (`audit/HDE-CRD-0002_close_candidate_source.json`), with their proofs and rows, then regenerates and checks. Its four users keep their assertions | Diff; V-1; V-3 (the four close-run tests pass with the whole close stage present) |
| R-4 | `"crd_id"` added to `test_mirror_schema_and_parity`'s `optional_fields`; nothing else in that file changes | Diff (+1); V-3 (a); necessity control (§8.3) |
| R-5 | `"crd_id"` added to `_MIRROR_OPTIONAL_FIELDS` and `_HUMAN_INDEX_OPTIONAL_FIELDS`. `_MIRROR_REQUIRED_FIELDS`, `_STRING_METADATA_FIELDS`, `_metadata_type_error`, the strict Epic predicates and the CRD viability refusal are unchanged | Diff (+2/−1); V-3 (a) and (b); necessity control (§8.3) |
| CR-10 (a) stated limit | No both-keys check and no `crd_id` type check added. The mutual-exclusion rule stays enforced by the writer (pinned by `test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together`, unchanged) and by `check_mirror_schema.sh` (`EPIC_CRD_EXCLUSIVE`, which exited 0 on every state in §8) | Diff; §8 |
| P-1 (acceptance (5) restated) | An absent HDE-CRD-0002 root publishes nothing, proven in a copy. No evidence-lane test depends on whether the real checkout holds the QA root, the close-run family, the close pack or the candidate source | V-1 (root absent) and V-3 (all present) both pass 134 of 134; V-4 |
| Exclusions | No updater, runtime or workflow change; no harness change beyond R-5; no governed-evidence change; no HDE-CRD-0002 QA evidence, close pack or candidate source committed | §4 |
| Interfaces (instruction §8) | The admission table is unchanged and still pinned. Harness users keep their results on every state without a close pack, and on the close-stage state they keep the QA-family statuses | §8 |
| Security and migration | Test code and one internal QA tool; no secret, network or production surface; no migration; rollback is a revert of `3a5d846` with no manifest refresh | §4; plan v1.1 §14 |
| Documentation | None required (proposal v1.1 §7) | — |
| Dependencies | None on unmerged work; #715 merged first. WU-REM-01 lands before QA-20, which has not started | §3 |

## 6. Review results

| Source | Head | Result |
| :- | :- | :- |
| Codex code review (summary comment 6375679259) | `9ad4336` | Completed 2026-10-23T22:06:46Z, `has_any_findings: false` (result v1.1 §3) |
| Codex code review | `696c051` | Stalled at "Running" from 22:24:12Z. The Product Owner ruled it not a merge-readiness gate (PO-35-2, result v1.2 §4) |
| Codex code review | `844db2f` (final head) | Completed 2026-10-24T00:01:28Z, trigger "New commits", `has_any_findings: false`, `has_unresolved_findings: false` (read now from the summary comment's state block). PO-35-2's condition, an uncompleted run, does not apply to the merged head |
| Codex security review | — | `status: null`; not part of the chain (addendum 2.3 rule 2) |
| Formal reviews | — | 0 |
| Review threads | — | 0 (`totalCount: 0`) |
| P1 findings | — | None raised, so none declined (addendum 2.14) |

**Corrected-change coverage.** There was no corrective change. The code tree reviewed clean on `9ad4336` is the merged code tree, and the final head was also reviewed clean.

**Product Owner decisions in the lineage.** PO-35-1 (push the PR-35 records to the PR branch) and PO-35-2 (the stalled run on `696c051` is not a gate). Neither waives a finding, a review of code or a security obligation.

## 7. CI ledger

| Run | Event, head | Conclusion | Lanes and counts |
| :- | :- | :- | :- |
| 40031375753 | pull_request, `9ad4336` | cancelled at 22:07:35Z, superseded by `5abc532` under the workflow's pull-request cancellation | — |
| 40031439957 | pull_request, `5abc532` | success | changed tests 146; evidence 134; qa 488; marker (result v1.1 §4.2) |
| 40033364013 | pull_request, `696c051` | success | changed tests 146; evidence 134; qa 488; marker (result v1.2 §3) |
| 40042683632 (job 120717168115) | pull_request, `844db2f` (final head) | success, 23:59:46Z to 00:10:18Z | changed tests **146** passed in 0.40 s; 7 evidence validators; evidence **134** passed in 585.07 s; qa **488** passed in 20.28 s; product, compat, db, rails and release skipped; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (read from the job log in this invocation) |
| 40043995165 (job 120721363419) | push, `3a5d846` on `main` | success, 00:14:42Z to 00:25:11Z | changed tests **146** in 0.39 s; evidence **134** in 583.56 s; qa **488** in 20.00 s; release skipped; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (read from the job log) |

**V-5** ("every lane the classifier selects … and the changed-test step are green, and the run ends `CI_APPLICABILITY_AND_EXACT_HEAD_OK`"): met on the final PR head and on the merge commit. No scoped CI waiver applies to this unit.

## 8. This review's independent checks

**Environment.** Throwaway clones of `main` at `3a5d846` under this session's scratchpad. Each clone had no remote and its own CPython 3.12.3 venv with CI's install (`pip` exit 0; pytest 8.4.2). Every command ran through `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PATH` set to the venv and the system, and `HOME` an empty scratch directory. Each step is `ci.yml`'s, run as written. Nothing from a clone was committed to the repository or pushed.

### 8.1 Classification and citations

| Run | Result |
| :- | :- |
| `classify_ci_changes.py`, base `c27d47d`, head `3a5d846`, `pull_request` and `push` | exit 0 each; `reason=selected_lanes;paths=6;lanes=evidence,qa`; `changed_tests=true`; one target, `tests/qa/test_qa_tool_ownership.py` |
| `check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| Stand-in QA family commit (`3a5d846` → `d2c83dd`) | `paths=16;lanes=evidence,release` |
| Stand-in close stage commit (`d2c83dd` → `624430b`) | `paths=21;lanes=evidence,release`. The qa lane is not selected, which is why V-3 runs it as a later qa-lane pull request would |

### 8.2 Lanes

| ID | State | Result |
| :- | :- | :- |
| V-1 | `3a5d846`, root absent | readiness and env pins exit 0; changed-test step **146 passed** in 0.50 s, worktree clean; qa lane **488 passed** in 17.52 s with both tree checks; 7 evidence validators exit 0; six evidence files **134 passed** in 684.82 s; final tree checks (`git diff --check`, `git diff --exit-code`, empty status) clean |
| V-3 | `624430b`: `3a5d846` plus a stand-in QA family and a stand-in close stage | qa lane **488 passed** in 18.48 s with both tree checks; release lane: manifest check exit 0, **79 passed**, attestation built (exit 0) and verified (exit 0), tree clean, 115 s; 7 evidence validators exit 0, including `check_mirror_schema.sh`; six evidence files **134 passed** in 714.06 s; final tree checks clean |

**Stand-ins**, produced only through the harness and the canonical updater, plus authored files, each stating "WU-REM-01 PR-40 rehearsal stand-in in a throwaway clone; not QA evidence, a close pack or a close candidate":
- QA family: `publish_crd_check_family` with checks `qa-01-standin` and `qa-02-standin`, each a `PASS` from an executed `python -c "raise SystemExit(0)"`, captured 2026-10-24T00:20:13Z; then `validate_crd_check_family` and the updater's `--check`. 16 paths changed (+39/−18).
- Close stage: the authored candidate source, close report and manifest, indexed by the updater's write and checked; then `publish_crd_close_run_family` with checks `close-pack-check` and `evidence-index-check`, captured 00:20:45Z, and `--check`; plus the two authored ledgers. 21 paths changed (+55/−18).
- The close-stage state's Index and Mirror hold 627 rows each, 7 of them HDE-CRD-0002's. 2 rows carry `crd_id` (the close report and the manifest), and none carries both `crd_id` and `epic_id`.

V-2's state is the QA-family commit `d2c83dd`. PR-30 ran the full V-2 lanes (result v1.0 §3). This review ran the V-3 lanes on the superset state and the V-2 probe below.

### 8.3 Viability, negative controls and necessity

**V-3 (b).** A read-only probe called `evaluate_acceptance_map_viability(HarnessConfig(<epic>, <tree>))` for each of the 16 `docs/acceptance_map_epic0NN.json` maps, in clean worktrees of each state. It published nothing, and each tree was clean afterwards.

| Map | `main` `3a5d846` | V-2 `d2c83dd` | V-3 `624430b` | V-3 with `c27d47d`'s harness |
| :- | :- | :- | :- | :- |
| HDE-EPIC021, 027, 028, 029 | PASS | PASS | PASS | FAIL_TOOLING |
| HDE-EPIC017, 019, 020, 022, 023, 024, 030, 033, 034, 035, 036, 037 | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING | FAIL_TOOLING |
| Results naming `crd_id` | 0 | 0 | 0 | 7 |

All 16 V-3 statuses equal V-2's, and no result names `crd_id`, so V-3 (b) holds. The 12 FAIL_TOOLING maps fail on `main` for reasons unrelated to `crd_id` (OBS-1).

| Control (on the V-3 state unless stated) | Result |
| :- | :- |
| Merged code: `test_mirror_schema_and_parity`, `test_current_acceptance_inputs_are_strictly_viable`, `test_absent_admitted_crd_root_publishes_nothing`, `test_crd_0002_fixture_root_publishes_beside_crd_0001` | **4 passed** in 25.88 s |
| R0: `c27d47d`'s R-1 to R-3 file, its six FND-001 tests | **2 failed, 4 errors** in 21.37 s: FND-001 reproduces without the change |
| R-4 necessity: `c27d47d`'s skeleton test | `test_mirror_schema_and_parity` **1 failed**: `AssertionError: assert {'crd_id'} == set()` |
| R-5 necessity: `c27d47d`'s harness | `test_current_acceptance_inputs_are_strictly_viable` **1 failed**: "Human Evidence Index row 567 has unknown fields: ['crd_id']"; the probe gives 0 PASS maps and 7 results naming `crd_id` |
| V-4, on `3a5d846`: the R-1 test with a planted Index row (`audit/qa/hde-crd-0002/qa_step_logs_manifest.json`) inserted after its strip | unmutated **1 passed** in 7.03 s; planted **1 failed** in 6.04 s at the Index assertion: `AssertionError: assert not [{'artifact_key': 'audit.qa.hde_crd_0002.qa_step_logs_manifest', …}]` |

Every control ran in a detached worktree and was restored; each tree was clean afterwards.

## 9. Business case and measures (addendum 2.11 rule 1, as 2.18 narrows it; 2.18 rule 5)

- **Beneficiaries:** QA and the Product Owner; every later qa-lane pull request; the users of the harness's Epic viability.
- **Benefit delivered at this boundary:** the evidence lane no longer blocks HDE-CRD-0002's QA evidence or close pack. Once the close pack is on `main`, the qa lane and Epic viability are unchanged.
- **Measure (1)** (the first pull request that publishes HDE-CRD-0002 QA evidence passes the evidence lane with no change to these tests): **not yet measurable**, because no such pull request exists. Proxy: V-2 (PR-30) and the V-3 lanes, which include the QA family (§8).
- **Measure (2)** (the close-pack pull request passes the evidence lane, and the first qa-lane run on `main` after it passes, with no change to these three files): **not yet measurable**. Proxy: V-3 (a) and (b) (§8; result v1.0 §3).
- **Who checks them:** the first QA-evidence pull request, the close-pack pull request and the next qa-lane run on `main`, or the QA-10 reassessment.
- **No cost ceiling** (addendum 2.18 rule 1). Nothing here records spend against one.
- **Stop rule** (addendum 2.11 rule 3, kept by 2.18 rule 3): the unit's business case is met at this boundary, so WU-REM-01 stops here. Further work needs a new business case.

## 10. Next stage (PR-40 "Resolve the next approved Plan stage")

- **Plan position.** Amended P-2 places WU-REM-01 after WU-OPS-01 and before QA-10 readiness. Every other unit of Plan v1.1 §7 is accepted (addendum 2.22 and earlier). No planned unit remains ahead of QA-10.
- **Controlling return.** The approved remediation's originating return is controlling: review v1.1 §7, addendum 2.24 `return_phase`, and plan v1.1 `return_owner`. So the next stage is QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, in "Accepted repair delivery → same Isis QA-10 reassessment".
- **That branch's intake is satisfied:**
  - the prior `REALITY_AUDIT`, `CHANGE_AUDIT_TRIAGE` and `QA_READINESS` v1.0;
  - `REMEDIATION_PROPOSAL_ID` and `REMEDIATION_REVIEW_ID` v1.1;
  - `ORIGINATING_FINDING_REF`;
  - the accepted returned PR and merge evidence (this review, with #716);
  - the immutable Specification, Plan and Plan review with their overlays;
  - the exact repair scope (S22, with S21's close-run tests and close-pack rows).
- **Not delivered:** no Ops or documentation delivery was part of this remedy.
- **Receiving role:** the same Isis, the continuing Lead Developer and readiness decision owner who produced QA-10 readiness v1.0 (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok).
- **For the reassessment:** OBS-2 (review v1.1 §3) is routed to it.

## 11. Canon-conflict register

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner | addendum 2.7 |
| CR-9 | PROPOSED, not yet reviewed | Isis (IA-30) | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13 |
| CR-10 | APPROVED, alternative (a), applied as decided (§5) | Isis (ESC-40, 2026-10-23T20:15:00Z) | review v1.1 §4; addendum 2.24. Drainage into HDE Schemas and Artifacts §8.3 unperformed (Product Owner) |

**No new conflict.** This review decides no canon.

## 12. Findings, limitations, unresolved items and owners

**Findings against the landed work: none.**

| Item | Owner | State |
| :- | :- | :- |
| QA-10 reassessment of S22 and its dependants | Isis | Next (§10) |
| Measures (1) and (2) | The first QA-evidence pull request, the close-pack pull request and the next qa-lane run on `main`, or the QA-10 reassessment | Not yet measurable |
| OBS-1: the 12 Epic viabilities already failing on `main` | Product Owner, as a later-change candidate | Unchanged; reproduced in §8.3 |
| OBS-2: the local failures of `tests/evidence/test_hdapi_v2_contract_inventory.py` | Isis at the QA-10 reassessment; Product Owner triage | Not run here; in no lane this unit selects |
| CR-10 drainage into HDE Schemas and Artifacts §8.3 | Product Owner | Unperformed |
| CR-9 | Isis, IA-30 | Unaffected |
| FND-024 (the PR35-C1 flake risk on QA-evidence pull requests) | As recorded in the triage | Not observed on #716 |
| Publication of this review into PF10 | Product Owner (informational, non-gating) | Not performed; PR-40 creates no addendum |

**Limitations.**
- Mergeability on `844db2f` before the merge was not recorded in a saved record (result v1.2 §6 left it to the session's reply). The merge itself succeeded, and the merged tree equals that head's tree.
- The full V-2 lane run is PR-30's (result v1.0 §3). This review ran the V-3 lanes on the superset state and the V-2 viability probe.
- Lane times in §8 come from a 4-CPU session container running two lanes side by side, so they do not compare with the hosted times.

**NOT PRODUCED:** no HDE-CRD-0002 QA evidence, close pack, close candidate source, QA Guide, QA Plan or PF10 addendum. **NOT EXECUTED:** QA, Ops, deployment, release activation, closure.

**Nonclaims.** This review establishes no QA verdict, acceptance of the change, Ops, deployment, PF09 or PF30 movement, drainage or closure. It makes no canon, code, test, workflow, release or governed-evidence change.

## 13. TypeSafe reading for the receiving session (QA-10 reassessment)

Action sent (v8.2): "As the continuing lead developer and readiness decision owner, reassess one change's QA readiness after an approved remediation work unit was delivered and accepted: refresh the read-only implementation audit, the triage and the readiness decision for the one requirement that failed (QA evidence admission) and the requirements that depend on it, using the merged remediation pull request (two evidence test files and one QA-harness key set), its lineage review and its rehearsal records, while preserving the unaffected evidence of the earlier full readiness review, and issue a current three-artifact readiness result (ready for QA, not ready, or assessment incomplete) as Markdown records. No code is changed and no live run against a provider occurs; an independent QA guide and QA plan follow only if the change is ready."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.45 (confidence 0.67). Rung probabilities: low 0.00, medium 0.02, high 0.54, extra high 0.41, max 0.03, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.02, Opus 5.5 0.97, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.96).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.011, Fable 5.1 at extra high 0.008, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.524, Opus 5.5 at extra high 0.398, Opus 5.5 at max 0.029, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.005, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - **Flags: boundary between extra high and high.**
  - Sent 2026-10-24T00:26:40Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-24T00:26:40Z; HTTP 200 in 0.57 s; 5498 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for the QA-10 reassessment is not stated. Nathan's pick for this PR-40 session is not stated; its reading is in result v1.1 §8.

**Surface advice:** run the reassessment in the continuing Isis QA-10 session for HDE-CRD-0002 (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), or a top-level Claude Code cloud session Nathan creates for that role, on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt.
- **Reads:** the prior QA-10 records, remediation review and proposal v1.1, this review, and plan v1.1 with its results, with the three files on `main`.
- **Optional re-runs:** a throwaway clone with CI's install on Python 3.12 under closed rails. The evidence lane takes about 10 minutes hosted and 12 to 17 minutes in a session container. The read-only viability probe and the stand-in builds take under two minutes each (§8).
- **Writes:** only the refreshed QA-10 records under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this review's pull request is merged first.

## 14. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-PR-40-20261024-WU-REM-01-01` |
| Change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| Requirement / work unit | S22, with S21's close-run tests and close-pack rows; WU-REM-01 |
| Prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, page state of 2026-10-12T02:29:38.234Z |
| Release | GCFPE-20261009.1 / 100926.1 |
| Role and stage | whole-change IA, read-only PR-40 |
| Capture time | 2026-10-24T00:42:00Z |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |
| Inherited usage | instruction v1.1 (`…-PR-10-20261023-WU-REM-01-02`); plan v1.1 (`…-PR-20-20261023-WU-REM-01-02`); result v1.0 (`…-PR-30-20261023-WU-REM-01-01`); results v1.1 and v1.2 (`…-PR-35-20261023-WU-REM-01-01`) |
| Repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |

## Canon relied on

Read on `main` at `3a5d846`. `docs/pfcanon/` was last changed by `3b21327` (#713), and PF10 is v13.7.6.

| Decision topic | Sources and sections |
| :- | :- |
| Review operation, decision states, next stage, handoff | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Resolve the next approved Plan stage", "Inputs", "Product Owner merge action", "Read-only review boundary", "Execute" 1 to 10, "Required result", "ACCEPT → next approved Plan stage", "Mandatory single-block handoff" |
| The reassessment destination and its intake | QA-10 — Audit Implementation and Establish QA Readiness — 100926.1: the remediation-return intake ("On an approved-remediation return, also carry …") and "Accepted repair delivery → same Isis QA-10 reassessment", read |
| Change authority; merges; Proceed | HDE Governance (`PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 "Change authority and exact-artifact lineage", read: the per-PR plan's approval is the Product Owner's PR Implementation Proceed, and merges are Product Owner actions |
| The approved remedy and its acceptance | PF10-HDE-Build-Notes v13.7.6 §2.23 and §2.24 (P-1, amended P-2, R-1 to R-5, V-1 to V-5, CR-10 (a), the business case); remediation review v1.1; instruction v1.1 §4 and §10; plan v1.1 §7, §10 and §20 |
| The Index and Mirror key set; CR-10 | HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.3 "Machine Evidence Index — JSONL mirror", "Allowed top-level keys and unknown-key rejection", read in full for instruction v1.1 and unchanged since |
| Harness Epic viability preserved | HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.6.3 "Explicit legacy Epic compatibility", read for instruction v1.1 and unchanged since |
| Business case, measure, stop rule, no ceiling | PF10 v13.7.6 §2.11 (rules 1 to 8, "Scope and supersession"), read in full in this invocation; §2.18 (rules 1 to 6, "Scope and supersession"), read in this invocation. Rule 5: "PR-40 still records whether the unit's measure was met" |
| Review chain; P1; security review | PF10 v13.7.6 §2.3 (rules 1 to 5) and §2.14 (rules 1 to 6), read in full in this invocation; §2.11 rules 7 and 8 |
| Accepted-final units untouched | PF10 v13.7.6 §2.5 (WU-PR-02) and §2.16 (WU-PR-07), as their headings and the remedy cite them |
| Evidence writer and CI rules | `AGENTS.md`: "Governed evidence rules" (sole writer; no hand-editing), closed rails, "Pytest readiness rule", "Pre-push check", "QA output placement", "Code review guidelines" and "Code review scope — CI-exempt paths are out of scope", "Evidence attribution, currentness and distinct decisions" |
| Repository facts | `git diff c27d47d 3a5d846` and the three blobs; `.github/workflows/ci.yml` lines 61–343; `ci/checks/classify_ci_changes.py`, run read-only; PR #716 through the GitHub API; hosted job logs 120717168115 and 120721363419 |

Canon searched (`git grep -i` on `origin/main -- docs/pfcanon/`) for `WU-REM-01`, `PR-40`, `lineage review`, `accepted-final` and `crd_id` (with `crd\_id`):
- PF10 holds 156 matching lines. The governing ones are 2.3, 2.11, 2.14, 2.18, 2.23 and 2.24, all read. The rest are earlier HDE-CRD-0002 unit acceptances (2.4, 2.5, 2.8, 2.9, 2.12, 2.16) that do not bear on this unit.
- HDE Governance has 2 matches, both historical accepted-final Epic delivery notes. Its §9.1.1 was read separately for merge and Proceed authority.
- HDE Schemas and Artifacts has 4 matches, in §8.3, which was read.
- HDE Mechanics Guide has 2 matches, the `HarnessConfig` lines of §1.6.3.
- HDE Phased Epics, Reality Audits and HDE CRD Records have 1, 1 and 3 matches, all historical records or template headings that govern nothing here.
