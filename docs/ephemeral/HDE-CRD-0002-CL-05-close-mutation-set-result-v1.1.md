---
artifact_type: CLOSE_MUTATION_SET_RESULT
artifact_id: HDE-CRD-0002-CL-05-CLOSE-MUTATION-SET-RESULT
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-CRD-0002-CL-05-close-mutation-set-result-v1.0.md (CLOSE_PR_READY as stated; CL-C-10 v1.1 §3 found its required-result predicate unmet, finding B-6)
CLOSE_MUTATION_SET_RESULT: CLOSE_PR_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: HDE-CRD-0002-CL-05
prompt: CL-05 — Prepare and Publish the Close Mutation Set — 102626.2 (candidate), https://app.notion.com/p/4054590a05eb8155b301e2cb6dec31d5 (page state of 2026-10-26T11:45:19.630Z, fetched in full in this session)
entry: (b) — docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md, DO_NOT_CLOSE, closure finding B-6, return work R6-1 to R6-4 (§7)
handoff: docs/ephemeral/HDE-CRD-0002-CL-C-10-handoff-to-cl05-v1.0.md (prerequisite #754 merged: main f1cdc88d60ac2cdcccc8943a59b5aa63d0b10c5e)
role: Close Implementer, standalone top-level session https://claude.ai/code/session_01V9x5bdHaGbtb152jyyRts7; separate from Isis (closure authority) and the QA sessions
execution_posture: MANUAL_PROMPT_EXECUTION (the Product Owner's direct invocation)
tooling_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/755 (close-tooling defect B-6; base main f1cdc88d60ac2cdcccc8943a59b5aa63d0b10c5e, head a90029c3b733080faeac6adcd2f29c28e4e6daee; open, not merged)
close_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/751 (unchanged since v1.0: head 2ae4fd5e66b6994414419f86e47981cded28de1c, merged as 09e443f4b899dd4d32fe18b50d6cd4fbb7a004b2; not reproduced, R6-3)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.3.md (647,314 bytes; SHA-256 bea405accb6cc6830045f12fe970426253f5860a8f199b5ec97f969bf1852d64); addenda 2.13 and 2.31 read in full in this session (D-1)
canon_conflict_register: carried unchanged; no new entry
created_at: 2026-10-26T16:15:00Z
next: CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1 (https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022), Isis, after the Product Owner merges #755 and this record's pull request
---

# HDE-CRD-0002 — CL-05 close mutation set result v1.1

## 1. Result

**CLOSE_MUTATION_SET_RESULT: CLOSE_PR_READY**

The close mutation set has been on `main` since #751 merged. This run supplies the one element CL-C-10 v1.1 found missing, B-6: a hosted run of the closeout workflow that validates HDE-CRD-0002's committed close pack, started by itself with no manual action.

- **The repair.** [#755](https://github.com/amthorn78/glow-hdengine-v2/pull/755): a pull request that changes the close tooling (the closeout workflow, the writer or its source schemas) now re-validates every committed writer close pack (§6).
- **The run.** #755 changes the workflow, so its own `pull_request` event started `epic-closeout-validation` run 40353776342 on the exact head `a90029c3`. No dispatch and no manual action was involved. The run selected `audit/HDE-CRD-0002_close_candidate_source.json`, printed `EPIC_CLOSE_PACK_CHECK_OK`, passed the six read-only checks and the clean-checkout assertions, and concluded `success` (§8).
- **The bytes it validated.** On that head the close pack and all 56 inputs its manifest binds are byte-identical to #751's head `2ae4fd5e` (§7). The writer's `--check` passes only when every bound digest matches.

| Predicate (CL-05 "Required result"; CL-C-10 v1.1 R6-1 to R6-4) | Evidence |
| :- | :- |
| The close pull request is open or merged | [#751](https://github.com/amthorn78/glow-hdengine-v2/pull/751), merged by the Product Owner at 2026-10-26T11:01:24Z as `09e443f4` (v1.0 §1); `09e443f4^{tree}` = `2ae4fd5e^{tree}` = `1fe15c33a3c8e48319527d319b4a549f73e25a64` |
| Its exact head passed the hosted `test` job | `test` run 40271349767 `success` on `2ae4fd5e`, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (v1.0 §8). Unchanged |
| The closeout workflow passed on its exact bytes (R6-1) | **Met.** Run 40353776342, job 121680627274, event `pull_request`, head `a90029c3`, `success`. Log read whole. The close pack and its bound inputs are byte-identical to `2ae4fd5e`'s (§3 of CL-C-10 v1.1: "A hosted run on a later head counts when the close pack and every input the manifest binds are byte-identical") |
| The run started by itself (R6-1) | **Met.** Event `pull_request`, opened by this session's push. No dispatch was attempted, and no one was asked for one |
| The repair is close tooling within CL-05's surface (R6-2) | **Met.** Three files: the workflow, its owner test and one `AGENTS.md` line. It keeps every property B-5 kept and stays a distinct, non-required lane (§6) |
| The close pack is not reproduced (R6-3) | **Met.** The merged bytes pass. No close-pack, ledger, Index, Mirror or close-run byte changed |
| The tooling pull request's hosted `test` job | **Passed.** `ci` run 40353776329, job 121680627088 (`test`), `success` on `a90029c3`, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§8). The Codex code review of `a90029c` found nothing; 0 review threads |
| A successor result record (R6-4) | This record |

This record is not a QA verdict, acceptance, closure, canon drainage, PF09 or PF30 movement, board state, Ops or deployment (§13). This session has not merged, enabled automatic merge or asked for a merge.

## 2. Inputs (resolved by the change ID, highest version, read on `main` `f1cdc88d`)

| Input | Path | Read |
| :- | :- | :- |
| Closure decision (entry (b)) | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md` (`DO_NOT_CLOSE`, B-6) | in full |
| Handoff | `docs/ephemeral/HDE-CRD-0002-CL-C-10-handoff-to-cl05-v1.0.md` | in full |
| Predecessor result | `docs/ephemeral/HDE-CRD-0002-CL-05-close-mutation-set-result-v1.0.md` | §1 to §16 in full; Appendices A and B with every `exit 0` line filtered out (each line read where the exit status was not 0) |
| First closure decision | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md` | not re-read; v1.1 carries what bears on B-6 (D-1) |
| QA-120 Report and RCA | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md`, `docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md` | not re-read; they are bound inputs of the close pack, and the writer's `--check` proves their bytes unchanged (D-1) |
| Specification, Plan, QA Plan | as v1.0 §2 lists them | not re-read; bound inputs, unchanged (D-1) |
| QA evidence of record | `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and its 21 primaries | bound by digest. The writer's `--check` passed on `main` and on #755's head |
| The closeout workflow and its owner test | `.github/workflows/epic-closeout-validation.yml`, `tests/evidence/test_rails_ci_workflow_integration.py` (closeout tests) | in full |

## 3. Intake (CL-05 step 1)

Each condition holds on `main` `f1cdc88d`. CL-C-10 v1.1 §7 checked them on `86df572e`; nothing they rest on changed in #754, which touched only `docs/ephemeral/`.

- The current QA-120 Report is v1.0, `verdict: PASS`.
- The QA step-logs manifest has 21 entries, all `PASS`. Its bytes are bound by the close pack's manifest, and the writer's `--check` passed.
- A close pack exists, and the closure decision names it as defective in one respect: no hosted closeout validation (B-6).
- The QA root is admitted: `ADMITTED_CRD_QA` maps `HDE-CRD-0002` to `audit/qa/hde-crd-0002` (v1.0 §3; the updater is unchanged since).

## 4. Tools read (CL-05 step 2)

- **`.github/workflows/epic-closeout-validation.yml` as merged by #752.**
  - Trigger: `pull_request`, path-filtered to the workflow file and `audit/*_close_candidate_source.json`, `audit/*_close_report.md` and `audit/*_MANIFEST.json`, plus `workflow_dispatch`.
  - Selection: only candidate sources, and the sources of writer manifests, that the pull request changes.
- **Does any actor start it by itself for a merged close pack?** No. That is B-6 (§6).
- **`audit/HDE-CRD-0002_MANIFEST.json` inputs.** The candidate source, the schema `schemas/close_candidate_source.v2.json`, the plan, 32 evidence bindings (the ADR `docs/adr/hde/close_pack_writer_adr.md` among them) and 21 QA primaries. A repair that touched any of these would invalidate the committed close pack, so none was touched.
- **Tracked `audit/*_MANIFEST.json` on `main`.** 17 in all: 16 of earlier generators (no `schema_version`; all valid JSON objects) and HDE-CRD-0002's (`close_candidate_manifest.v2`).
- **The ADR, searched for `dispatch`, `trigger`, `closeout-validation` and `pull request`.** It records no trigger, only line 70's unrelated use of "trigger words".

## 5. Rehearsal (CL-05 step 3)

Rehearsal r1 used a throwaway full-history clone of `main` `f1cdc88d60ac2cdcccc8943a59b5aa63d0b10c5e` (`git rev-parse --is-shallow-repository` printed `false`). It was never pushed and ran under closed rails (Appendix A).

- **3a, the causal inputs.** Not re-authored: R6-3. The merged close pack is the input.
- **3b, the checks on the merged close pack.**
  - The writer's `--check` printed `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json`, under CI's install, a `requirements.txt`-only interpreter and a `jsonschema`-only one.
  - `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py` and `check_final_lf.sh` exited 0.
  - Afterwards the tree had 0 entries, ignored files included.
- **Byte identity.** `git diff 09e443f4 f1cdc88d` over the 56 bound inputs and the two outputs printed 0 lines. Since `09e443f4^{tree}` equals `2ae4fd5e^{tree}`, the bytes on `main` are #751's head bytes.
- **The closeout workflow, as merged.**
  - Its step scripts were extracted with Ruby 3.3.6's YAML loader. They ran as a `pull_request` event for a throwaway commit `b93984fa` on `f1cdc88d` that changes only the workflow file, a change the path filter admits. The checkout was replaced by a worktree, and setup-python plus the install by a `requirements.txt`-only interpreter.
  - Result: "No writer close pack changed; closeout validation does not apply." The install, the writer's `--check` and the six read-only checks were skipped, and the job succeeded.
- **3c, classification: close-tooling defect B-6.** The tool lacks an admission the change needs: correct, committed inputs exist, and no event in the tool's trigger set can validate them hosted without changing them. R6-3 rules out changing them, and the Product Owner has ruled out a dispatch.

## 6. Close-tooling defect B-6 and its repair (CL-05 step 4)

**Command and exact output** (r1, 2026-10-26T15:37:12Z). The merged workflow's step scripts ran as a `pull_request` event: `SELECTED_REF` `b93984fa0ac2ee1935bf5953e37bec67a2c236b0`, `BASE_REF` `f1cdc88d60ac2cdcccc8943a59b5aa63d0b10c5e`. The selection step exited 0 and printed

```text
No writer close pack changed; closeout validation does not apply.
```

The validation steps were skipped.

**Proven cause.** Three facts combine:
1. The workflow selects only close packs that the pull request changes (`git diff --name-only <merge-base> HEAD`).
2. HDE-CRD-0002's close pack merged in #751 before B-5's trigger existed (#752), so its own pull request never had the run.
3. No later event selects bytes that do not change. The only alternatives were a `workflow_dispatch`, which the Product Owner will not run and this integration may not run (v1.0 §6a: HTTP 403), or changing the close pack, which R6-3 rules out.

The same gap holds for any close pack whose validation is lost, and for any committed close pack when the writer or its schemas change. PF19 §2.2.11 requires both: "Hosted CI MUST exercise the actual check entrypoint against committed bytes."

**Triggering inputs.** HDE-CRD-0002's committed close pack on `main` (`audit/HDE-CRD-0002_close_candidate_source.json`, `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json`) and the merged workflow.

**Fix ([#755](https://github.com/amthorn78/glow-hdengine-v2/pull/755); three files; commit `a90029c3`).**
- **`.github/workflows/epic-closeout-validation.yml`.**
  - **Trigger.** The `pull_request` path filter adds the close tooling: `tools/qa/generate_epic_close_pack.py`, `schemas/close_candidate_source.v*.json` and `schemas/epic_close_candidate_source.v*.json`. The workflow file was already in it.
  - **Selection.** When a changed path matches `TOOLING_RE` (the same three patterns plus the workflow file), the script adds every tracked top-level `audit/*_MANIFEST.json` at the head to the manifests it reads. Every manifest it reads, changed or tracked, goes through one function `bound_source`, which holds the unchanged rules: a writer manifest selects its bound source; an earlier generator's manifest returns nothing; `CLOSEOUT_MANIFEST_ABSENT`, `CLOSEOUT_MANIFEST_INVALID` and `CLOSEOUT_CANDIDATE_SOURCE_UNBOUND` fail closed. A changed close report without a manifest still fails closed. In tooling mode only manifests are read, so an earlier generator's report without a manifest is not an error.
  - **Comments.** The header comment and the selection step's comment state the rule.
  - **Unchanged:** the changed-pack selection, `workflow_dispatch` and its bounded checks, `contents: read`, one job, `timeout-minutes: 15`, exact-ref checkout with `persist-credentials: false`, the install, the writer's `--check`, the six read-only checks, both clean-checkout assertions, superseded-run cancellation, and no receipt, writeback or hosted-result feedback.
- **`tests/evidence/test_rails_ci_workflow_integration.py`.**
  - `test_closeout_validation_is_isolated_read_only_and_exact_head` asserts the seven-pattern path filter.
  - New: `test_closeout_validation_revalidates_every_committed_writer_close_pack_on_a_tooling_change`, 11 cases. It runs the workflow's own selection script on git histories. The workflow, writer, v2-schema, v1-schema and new-schema-version changes select both committed writer sources (a v2 pack, and a v1 pack whose source lies elsewhere). A writer-test, other-tool or other-schema change, or no committed writer pack, selects nothing. A committed unbound or invalid writer manifest fails closed. An earlier generator's manifest, a nested `audit/history/…_MANIFEST.json` and a report without a manifest are ignored.
  - New: `test_closeout_validation_path_filter_admits_exactly_the_paths_its_selection_reads`. Over every tracked path, GitHub's path filter (modelled by the file's existing `_github_path_filter_selects`) selects exactly the close-tooling and close-pack paths, and the script carries the same tooling pattern.
- **`AGENTS.md` line 144.** "…or the workflow, and checks each changed candidate source on the exact pull-request head;" became "…or the close tooling (the workflow, the writer or its source schemas), and checks each changed candidate source on the exact pull-request head, or every committed one when the close tooling changed;". CL-05 allowed change 3: the old selection wording is untrue after the change. `README.md` line 30 ("runs by itself on every pull request that changes a writer close pack") stays true and was not changed.

**Narrowing (CL-05 step 4.5).** None beyond #752's. The repair adds a trigger and a selection rule and narrows no other rule. HDE Build Notes 2.13's kept property "no pull-request trigger" was already narrowed by #752 under 2.31 rule 8 (v1.0 §6a; O-5).

**ADR.** No change. `docs/adr/hde/close_pack_writer_adr.md` records no trigger (§4), and the repair changes none of its decisions. The ADR is also a bound input of the close pack.

**Lane (PF19 §2.2.11; Plan Templates closeout-automation lane rule).** The workflow stays a separate, non-gating closeout lane. It is not part of the ordinary `test` job, which is unchanged, and no branch protection changes. It runs only on close-tooling or close-pack changes, so it adds no run to unrelated pull requests. One run takes about 25 seconds (run 40353776342: 15:53:38Z to 15:54:02Z).

**Tests and negative control** (Appendix B).
- **Owner test file on `a90029c3`:** 159 passed. On `main` it has 147; 12 are added.
- **Negative control.** The new test file over `main`'s unchanged workflow, `-k closeout`: exit 1, 9 failed, 13 passed. The failures are the extended filter assertion, the seven tooling cases that expect a selection or a refusal, and the filter test. The four that expect no selection pass on both.
- `AGENTS_MD_CITATIONS_OK`.
- **The workflow's own step scripts** from `a90029c3`, run as in §5 (scenario names as in v1.0 Appendix B):
  - **A, #755's head** against `f1cdc88d`: applies, `Closeout candidate: audit/HDE-CRD-0002_close_candidate_source.json`, `EPIC_CLOSE_PACK_CHECK_OK`, six checks exit 0, checkout clean; job succeeds.
  - **B, #751's tree** (`09e443f4` against `8ff6691a`): the same; job succeeds.
  - **C, an earlier generator's manifest changed:** does not apply; job succeeds.
  - **D, a writer manifest without its source binding:** `CLOSEOUT_CANDIDATE_SOURCE_UNBOUND:audit/HDE-CRD-0002_MANIFEST.json`; job fails.
  - **E, a report without a manifest:** `CLOSEOUT_MANIFEST_ABSENT:audit/HDE-CRD-0099_MANIFEST.json`; job fails.
  - **H, a changed source with stale outputs:** selected, then `EPIC_CLOSE_PACK_ERROR:MANIFEST_BINDING_MISMATCH`; job fails.
  - **J, a writer-only change** (a trailing comment): selects HDE-CRD-0002, `EPIC_CLOSE_PACK_CHECK_OK`; job succeeds.
  - **K, an unrelated change:** does not apply; job succeeds. (The path filter would not start the job at all.)
  - **F, dispatch with the real source:** passes. **G, dispatch with a newline in the source,** and **I, dispatch with a ref that is not the head:** the selection step exits 1.

**Publication.**
- **Branch and pre-push checks.** Branch `close/hde-crd-0002-tooling` (CL-05 step 4.6; free again after #750 merged) from `main` `f1cdc88d`, head `a90029c3b733080faeac6adcd2f29c28e4e6daee`.
  - `prepush_check.py lanes build-notes`: exit 0, PASS. `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`, 166 changed-test targets; HDE Build Notes v13.8.3, 647,314 bytes, `bea405ac…852d64`; "repository unchanged".
  - `membership` with the three paths: exit 0, PASS, 3 `not-member` of release 1.3.0 (45 members, `release_id` `77204764…c51e`).
- **Changed-test step, as `ci.yml` runs it** (worktree at `a90029c3`, `PYTHONPATH` the worktree): 166 targets, exit 1, 4,530 passed and 1 failed in 565.88 s. Afterwards `git diff --exit-code` exited 0 with 0 status lines. The failure is `tests/bodygraph/test_vendor_prod_override.py::test_record_and_streams_carry_no_subject_url_or_secret`, and it comes from this container (D-3).
- **Opened.** #755, opened at about 15:53:30Z. Its description follows `.github/pull_request_template.md` as `AGENTS.md` "PR descriptions" defines it.

## 7. The close mutation set (CL-05 step 5)

Not reproduced (R6-3): the merged bytes pass hosted and locally. No T1 to T6 ran in this session, no close-pack byte was written, and no Index, Mirror, path proof, orientation output or close-run primary changed. The close mutation set of record is v1.0 §7's: #751, C1 `5ee940cb`, C2 `814705f3`, C3 `2ae4fd5e`, merged as `09e443f4`.

Byte identity on `main` `f1cdc88d` and on #755's head `a90029c3`, against `09e443f4`: 0 diff lines over `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and the 56 inputs the manifest binds:
- the candidate source;
- the schema;
- the plan;
- the 32 evidence bindings;
- the 21 QA primaries.

#755 changes none of them: its three paths are the workflow, the owner test and `AGENTS.md`, none of them a bound input.

## 8. Publication and validation (CL-05 step 6, T7)

- **Closeout workflow, R6-1.** `epic-closeout-validation` run 40353776342, job 121680627274, run number 2, event `pull_request`, head `a90029c3b733080faeac6adcd2f29c28e4e6daee`, base `f1cdc88d`. `success`, 15:53:38Z to 15:54:02Z, on ubuntu-26.04 image 20261012.163.1 with CPython 3.12.15. The log was read whole (483 lines; the API's `original_length` 483):
  - the token had `Contents: read` and `Metadata: read` only;
  - checkout at `ref: a90029c3…`, `persist-credentials: false`, `fetch-depth: 0`;
  - `EVENT_NAME: pull_request`, `BASE_REF: f1cdc88d…`, `SELECTED_REF: a90029c3…`, and the selection script as committed on `a90029c3`;
  - `Closeout candidate: audit/HDE-CRD-0002_close_candidate_source.json`;
  - `pip install -r requirements.txt`: Flask 2.3.3, gunicorn 21.2.0, jsonschema 4.23.0, psycopg 3.2.13;
  - `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json`;
  - the six read-only checks and the clean-checkout step succeeded, and every step concluded `success`;
  - one Node.js 20 deprecation warning for `actions/checkout@v4` and `actions/setup-python@v5`. No `##[error]` line.

  This is the workflow's second hosted run, and the first that validated a close pack. Its first was #752's, which found nothing to validate (v1.0 §6a).
- **Hosted `ci` `test`.** `ci` run 40353776329, job 121680627088 (`test`), event `pull_request`, head `a90029c3`, base `f1cdc88d`. `success`, 15:53:38Z to 16:13:42Z, on ubuntu-26.04 image 20261012.163.1 with CPython 3.12.15. The log was downloaded whole and read: 928 lines, 75,532 bytes, SHA-256 `a85b7d7a8eea3a5f2dae3e0363f49e44b22e0a9b97a42f624814a19d8193ee03`.
  - `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`; `AGENTS_MD_CITATIONS_OK`; `[env-pins] OK`.
  - Changed tests: 4,529 passed, 2 skipped. The container failure of D-3 did not occur on the runner.
  - Lanes: product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 120, 113, 155 and 159 (the owner test file); evidence 134; qa 488; release 79, with the release-attestation step `success`.
  - Every outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; 0 `##[error]` lines; one Node.js 20 deprecation warning.
- **Codex code review.** On `a90029c` (trigger "PR opened"), completed at 2026-10-26T15:55:24Z with `has_any_findings: false` and `has_unresolved_findings: false` (summary comment 6420541734); 0 review threads.
- **State.** #755 read after both runs: `mergeable_state: clean` against base `f1cdc88d`, still `main`'s head; 1 commit, 3 files (+181, −18); open, not merged.

## 9. The close report's decision and posture

Unchanged from v1.0 §9: `audit/HDE-CRD-0002_close_report.md` records closure decision `SATISFIED`, posture review-trace-only. Its bytes are unchanged (§7). The closure decision is Isis's at CL-C-10.

## 10. Measures the change's records name, as observed

| Measure | Observed |
| :- | :- |
| WU-PR-07: "closes through the ordinary Close Gate with the new writer on the first attempt", every check mode passing, no exceptional-closure record | As CL-C-10 v1.1 §6 records, with one addition. The check mode that was missing, the hosted closeout run, has now passed on the exact close-pack bytes at its first execution (run 40353776342). Every writer and validator run on the real inputs in this session passed at its first execution. No exceptional-closure record exists or was created. The Product Owner owns the measure |
| FND-001 remedy measure (2) | Met, as CL-C-10 v1.1 §6 records. Unchanged here: #755 does not touch `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py` or `tools/qa/qa_harness.py` |

## 11. Open items for the closure decision

None blocks closure. Each needs a decision only its owner can make.

- **O-1 to O-7** stand as v1.0 §11 and CL-C-10 v1.1 §8 record them, with their owners. This run changed none of them.
  - O-4's three documentation lines still call the workflow manual; this run did not change them.
  - O-5 also covers this repair's trigger addition: HDE Build Notes 2.13's kept-property text is unchanged.
- **O-8.** In tooling mode the workflow reads every tracked top-level `audit/*_MANIFEST.json`. A future tracked manifest there that is invalid JSON would fail a close-tooling pull request's closeout run with `CLOSEOUT_MANIFEST_INVALID`. That is the same fail-closed rule the changed-pack mode applies. All 17 tracked manifests parse today (§4). Owner: whoever adds such a file; no action is needed now.

## 12. Deviations and limitations

- **D-1. Reading completeness.** CL-05 requires PF10 and every input to be read completely, and a list of canon sections to be read in full, before any change. This session read in full:
  - the CL-05 page;
  - CL-C-10 v1.1 and its handoff;
  - CL-05 result v1.0 §1 to §16, plus its appendices filtered to their non-zero exit lines;
  - HDE Build Notes 2.13 and 2.31;
  - PF19 §2.2.11;
  - PF06 §3.5.1 and §3.5.2.1 to §3.5.2.4;
  - the Plan Templates closeout-automation lane rule (its two paragraphs).

  It did not re-read the rest of PF10, PF06 §0.4.1.2, §1.0.6 and §3.5.4, the PF12 and PF19 close-pack sections, PF04 §2.0.19, the close-pack ADR beyond the search in §4, CL-C-10 v1.0, the QA-120 Report and RCA, the Specification, the Plan or the QA Plan.

  These govern the close pack's content, which this run did not author or change (R6-3). Their bytes are bound inputs, and the writer's `--check` proved them unchanged. No claim here rests on a section not read. v1.0 §14 records the reading on which the close pack rests.
- **D-2. The hosted run is on a later head.** R6-1's run is on #755's head, not on `2ae4fd5e`. CL-C-10 v1.1 §3 counts such a run when the bytes are identical, and §7 shows that they are.
- **D-3. Container environment.** As v1.0 D-10: in this container `tests/bodygraph/test_vendor_prod_override.py::test_record_and_streams_carry_no_subject_url_or_secret` fails while `DATABASE_URL`, `GEO_API_KEY`, `HDAPI_BASE_URL` and `HD_API_KEY` are set (names only; no value was read).
  - It fails the same way on `main` `f1cdc88d` (1 failed).
  - The file passes with them unset (99 passed).
  - Hosted CI does not set them.
- **D-4. Simulation limits.** The local workflow runs replace the checkout action with a worktree and setup-python with a local `requirements.txt`-only CPython 3.12.3 venv. The install step's `pip install -r requirements.txt` ran against that venv, whose packages were already present. The final clean-checkout step is recorded as not run after an earlier failure, as GitHub's default `success()` condition would skip it. These runs are not CI's result; §8's hosted run is.
- **D-5. Branches.** The tooling repair uses CL-05's named branch `close/hde-crd-0002-tooling`. This record uses the session's designated branch `claude/optimistic-gauss-ib7v32`, which touches only `docs/ephemeral/` (CL-05 step 7.1).
- **D-6. Interpreters.** CPython 3.12.3 locally; hosted CI uses 3.12.15. The `jsonschema`-only interpreter had `jsonschema` 4.23.0.

## 13. Nonclaims

This record and the work it reports establish none of:
- a QA verdict, acceptance or HDE-CRD-0002's closure;
- Ops, deployment or release activation;
- canon drainage, PF09 or PF30 movement, or board state;
- the merge of #755.

Further:
- The close report's `SATISFIED` is review-trace-only.
- The pre-push tool's results and the local runs are not CI's result.
- No PF-Canon, PF10, approved QA evidence, product code, close-pack byte, PF09, PF30 or board state was changed, and no governed artifact was hand-edited.
- No workflow was dispatched or re-run, and no one was asked to.
- No Notion page or row was written. The GCFPE Modification Backlog was not edited.

## 14. Canon relied on

| Topic | Sources read | How it governs here |
| :- | :- | :- |
| The stage, its authority, close-tooling repair and its limits | CL-05 — Prepare and Publish the Close Mutation Set — 102626.2 (candidate), page in full; HDE Build Notes v13.8.3 addendum 2.31 in full (rules 7, 8, 9 and 10) | Proceed for the repair; the repair surface; restart and non-reproduction rules; the result predicate |
| The return work | CL-C-10 v1.1 §3 and §7 (R6-1 to R6-4) | what the run must show; what counts as the exact bytes |
| Hosted check of committed bytes; distinct lanes; CI budget | PF19-Canon-Glow-QA-Guide v3.0.6 §2.2.11 "Evidence-governed CI sequence (names-only)", in full | B-6's requirement; the lane stays distinct and non-required; the run is short-circuited to close-tooling and close-pack changes |
| Closeout automation lane | PF27-Canon-Plan-Templates v2.0.5, the closeout-automation lane paragraphs ("Separately authorized closeout automation MAY remain isolated and non-gating") | the workflow stays isolated and non-gating |
| Close Gate on exact candidate bytes; no feedback cycle | PF06-Canon-Change-Process-Guide v2.5.4 §3.5.1, including "Feedback-free terminal lifecycle", and §3.5.2.1 to §3.5.2.4, in full | the hosted run validates committed bytes and writes nothing back; no close-pack byte changes |
| The closeout job's history and kept properties | HDE Build Notes 2.13, in full | the properties kept (§6); O-5 |
| Real inputs | `AGENTS.md` "Code review guidelines" (real-input rule) | B-6 rests on the committed close pack and the merged workflow, both real |
| Repository rules | `AGENTS.md` "Canon-first rule", "Governed evidence rules", "Evidence attribution, currentness and distinct decisions", "Pre-push check", "PR descriptions", "Truncation/retrieval-failure guardrail" (its exit-status corollary) | closed rails; captured exit statuses; distinct tested and stored states; the PR description headings |

Silence: no PF canon section names the CL-05 stage or a closeout trigger. HDE Build Notes 2.31 governs the stage, with its canon drainage owned by the Product Owner.

## 15. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-CL-05-20261026-02 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | HDE-CRD-0002-CL-05: closure finding B-6 (close-tooling defect B-6; return work R6-1 to R6-4 of CL-C-10 v1.1) |
| prompt | CL-05 — Prepare and Publish the Close Mutation Set — 102626.2 (candidate), page state of 2026-10-26T11:45:19.630Z |
| release | GCFPE-20261009.1 / 100926.1, plus CL-05 candidate 102626.2 (not a release member) |
| role/stage | Close Implementer, CL-05 (entry (b)) |
| capture time | 2026-10-26T16:15:00Z |
| execution identity | https://claude.ai/code/session_01V9x5bdHaGbtb152jyyRts7 (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-CL-05-20261026-01 (v1.0); GCFPE-USE-HDE-CRD-0002-CL-C-10-20261026-01 and -02 (CL-C-10 v1.0 and v1.1) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |

Defects in the CL-05 candidate found in this run, for GCFPE-MGMT-10 (MB-030). The backlog was not written (O-7).

1. Step 6.3 and the "Required result" have no route for a close pull request that merged before its closeout run. B-6's repair supplies a mechanism: a close-tooling pull request re-validates every committed close pack. The candidate text does not yet name it. CL-C-10 v1.1 §9 records the same.
2. The input list requires the Specification, Plan, QA Plan, QA Report and RCA to be read completely even on an entry (b) whose return work excludes reproducing the close pack (R6-3). A rule scoped to what the return work changes would match this run (D-1).

## 16. TypeSafe reading for the receiving session (CL-C-10, HDE-CRD-0002)

The reading was taken once with the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, session kind `review`, label "HDE-CRD-0002 CL-C-10 closure decision after CL-05 B-6 (100926.1)". No Notion row was written. Nathan picks the cell; no pick is stated.

Action sent (v8.2): "In the continuing closure-authority session, re-decide closure for an already QA-passed change request whose second closure decision (already written twice) returned do-not-close for one missing element, a hosted run of the read-only closeout validation workflow against the already merged close pack: read a new result record and a merged three-file close-tooling pull request (one workflow file, its owner test and one documentation line) whose own hosted runs validated that close pack by themselves, confirm from the hosted run logs that the run selected and passed the close pack with byte-identical bound inputs, and write a revised closure decision record in its own pull request. A written step list exists; no live run against a provider occurs; the decision is the change's terminal closure decision, followed only by post-closure records and no later independent review."

The reading as printed:

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 3.15 (confidence 0.64); rung probabilities low 0.01, medium 0.04, high 0.09, extra high 0.52, max 0.34, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.95, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.93). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.003, Fable 5.1 at extra high 0.016, Fable 5.1 at max 0.010, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.038, Opus 5.5 at high 0.085, Opus 5.5 at extra high 0.494, Opus 5.5 at max 0.323, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.002, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.007, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between max and extra high. Sent 2026-10-26T15:54:10Z. Nathan picks the cell.
- Detail (as printed in the script's row object): v8.2 sent 2026-10-26T15:54:10Z; HTTP 200 in 0.58 s; 5507 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between max and extra high.
- The action text describes #755 as merged, which is the state CL-C-10 runs in. It was sent before #755's `test` job finished.

**Execution surface.**
- **Session.** CL-C-10 runs in the continuing Isis session for HDE-CRD-0002 (Isis-53, https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok), or in a top-level session Nathan creates for that role. It needs `amthorn78/glow-hdengine-v2` and Notion read access for the prompt.
- **What it reads.** This record, CL-C-10 v1.1, #755's diff and its two hosted runs (40353776342 and the `ci` run named in §8), and the merged close pack on `main`.
- **What it writes.** Only its decision record under `docs/ephemeral/`, by pull request.
- **What it does not need.** No production, vendor, Railway or database access.

## Appendix A. Command ledger

Each line is one command as run, its label, its start time (UTC) and its exit status, from the session's run logs. Paths under the scratch directory are written `<scratch>`. Full outputs stay in the session's scratch logs, which are not committed. Every repository command ran with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 GIT_CONFIG_GLOBAL=/dev/null`.

### Environment

- `git fetch --unshallow origin` on the session checkout → exit 0; `git rev-parse --is-shallow-repository` → `false`
- `python3.12 -m venv <scratch>/venvs/full`; `python -m pip install -q 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; `python -m pytest --version` → exit 0, `pytest 8.4.2`
- `python3.12 -m venv <scratch>/venvs/req`; `python -m pip install -q -r requirements.txt` → exit 0
- `python3.12 -m venv <scratch>/venvs/js`; `python -m pip install -q 'jsonschema==4.23.0'` → exit 0

### r1: rehearsal on main f1cdc88d

- `git clone -q --no-hardlinks <checkout> <scratch>/r1`; `git checkout -q --detach f1cdc88d60ac2cdcccc8943a59b5aa63d0b10c5e`; `git rev-parse --is-shallow-repository` → `false`
- `writer-check` (15:36:21Z): `<scratch>/venvs/full/bin/python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check` → exit 0, `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json`
- `index-check` (15:36:31Z): `python tools/evidence/update_evidence_index.py --check` → exit 0
- `orientation-check` (15:36:32Z): `python tools/evidence/orientation_demo.py --check` → exit 0
- `mirror-schema` (15:36:32Z): `ci/checks/check_mirror_schema.sh` → exit 0
- `index-hash` (15:36:32Z): `ci/checks/check_evidence_index_hash.sh` → exit 0
- `evidence-paths` (15:36:32Z): `python tools/evidence/validate_evidence_paths.py` → exit 0
- `final-lf` (15:36:32Z): `ci/checks/check_final_lf.sh` → exit 0
- `writer-check-jsonschema-only` (15:36:32Z): `<scratch>/venvs/js/bin/python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check` → exit 0, `EPIC_CLOSE_PACK_CHECK_OK:…`
- `writer-check-req-only` (15:36:41Z): `<scratch>/venvs/req/bin/python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check` → exit 0, `EPIC_CLOSE_PACK_CHECK_OK:…`
- `git status --short --untracked-files=all --ignored` → 0 lines
- `git diff 09e443f4b899dd4d32fe18b50d6cd4fbb7a004b2 HEAD -- <56 bound inputs> audit/HDE-CRD-0002_close_report.md audit/HDE-CRD-0002_MANIFEST.json` → 0 lines
- `ruby <scratch>/tools/extract_steps.rb .github/workflows/epic-closeout-validation.yml <scratch>/steps_main` → exit 0 (7 steps; triggers `pull_request`, `workflow_dispatch`)
- defect reproduction (15:37:12Z): worktree at `f1cdc88d` plus throwaway commit `b93984fa` (one comment line prepended to the workflow); `python3 <scratch>/tools/sim_workflow.py … r1-main-workflow-workflow-only-pr <scratch>/steps_main <worktree> pull_request b93984fa… f1cdc88d… <scratch>/venvs/req/bin` → applies `false`, selection exit 0, "No writer close pack changed; closeout validation does not apply.", job succeeds

## Appendix B. B-6 command ledger

### Repair

- `git checkout -q -b close/hde-crd-0002-tooling origin/main` (at `f1cdc88d`)
- edits to the workflow, the owner test and `AGENTS.md` line 144 (§6)
- `owner-tests-closeout` (15:39:07Z): `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py -k closeout` → exit 0, 22 passed, 137 deselected
- `owner-test-file` (15:39:30Z): `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py` → exit 0, 159 passed
- `agents-md-citations` (15:40:04Z): `python ci/checks/check_agents_md_citations.py` → exit 0, `AGENTS_MD_CITATIONS_OK`
- `negctl-main-workflow` (15:40:05Z): the new test file copied onto a worktree of `main` `f1cdc88d`, `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py -k closeout` → exit 1, 9 failed, 13 passed, 137 deselected; worktree restored and removed
- `git commit` → `a90029c3b733080faeac6adcd2f29c28e4e6daee`

### The workflow's own steps from a90029c3, run locally

`ruby <scratch>/tools/extract_steps.rb <a90029c3's workflow> <scratch>/steps_new`. Then `sim_workflow.py` ran each scenario in a worktree of the session's rehearsal clone. Scenarios C, D, E, H, J and K are `a90029c3` plus one throwaway commit, never pushed.

| Scenario | Event | Head | Base | Applies | Job | Output |
| :- | :- | :- | :- | :- | :- | :- |
| A, #755's head | pull_request | `a90029c3` | `f1cdc88d` | true | succeeds | `Closeout candidate: audit/HDE-CRD-0002_close_candidate_source.json`; `EPIC_CLOSE_PACK_CHECK_OK` |
| B, #751's tree | pull_request | `09e443f4` | `8ff6691a` | true | succeeds | the same |
| C, `audit/EPIC-027_MANIFEST.json` + newline | pull_request | `e2597abc` | `a90029c3` | false | succeeds | does not apply |
| D, `inputs.candidate_source` removed from HDE-CRD-0002's manifest | pull_request | `5f9d275e` | `a90029c3` | unset | fails | `CLOSEOUT_CANDIDATE_SOURCE_UNBOUND:audit/HDE-CRD-0002_MANIFEST.json` |
| E, `audit/HDE-CRD-0099_close_report.md` added | pull_request | `4764163d` | `a90029c3` | unset | fails | `CLOSEOUT_MANIFEST_ABSENT:audit/HDE-CRD-0099_MANIFEST.json` |
| H, HDE-CRD-0002's source + newline | pull_request | `cc9d1533` | `a90029c3` | true | fails | `EPIC_CLOSE_PACK_ERROR:MANIFEST_BINDING_MISMATCH` |
| J, writer + trailing comment | pull_request | `3f7fe41f` | `a90029c3` | true | succeeds | `Closeout candidate: …HDE-CRD-0002…`; `EPIC_CLOSE_PACK_CHECK_OK` |
| K, `README.md` + one line | pull_request | `107c839d` | `a90029c3` | false | succeeds | does not apply |
| F, dispatch, real source | workflow_dispatch | `a90029c3` | — | true | succeeds | `EPIC_CLOSE_PACK_CHECK_OK` |
| G, dispatch, source with a newline | workflow_dispatch | `a90029c3` | — | unset | fails | selection exit 1 |
| I, dispatch, `git_ref` `f1cdc88d` on head `a90029c3` | workflow_dispatch | `a90029c3` | — | unset | fails | selection exit 1 |

### Pre-push and changed tests

- `prepush-lanes-build-notes` (15:42:07Z): `python tools/ci/prepush_check.py lanes build-notes` → exit 0, `PREPUSH_CHECK_RESULT: PASS lanes=PASS build-notes=PASS`
- `prepush-membership` (15:42:09Z): `python tools/ci/prepush_check.py --path .github/workflows/epic-closeout-validation.yml --path AGENTS.md --path tests/evidence/test_rails_ci_workflow_integration.py membership` → exit 0, PASS, 3 `not-member`
- `python3 ci/checks/classify_ci_changes.py --base f1cdc88d… --head a90029c3… --event-name pull_request --github-output <scratch>/ct/gh.txt --changed-tests-output <scratch>/ct/targets.txt` → exit 0, `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`, 166 targets
- `changed-tests` (15:42:40Z): `git worktree add --detach <scratch>/ct/src a90029c3…`; `PYTHONPATH=<scratch>/ct/src python -m pytest -q -p no:cacheprovider -- <166 targets>` → exit 1, 1 failed, 4530 passed in 565.88 s; `git status --short --untracked-files=all` → 0 lines; `git diff --exit-code` → exit 0
- `vendor-override-file-unset-provider-vars` (15:52:23Z): the same file with `DATABASE_URL`, `GEO_API_KEY`, `HDAPI_BASE_URL` and `HD_API_KEY` unset → exit 0, 99 passed
- `vendor-override-test-on-main` (15:52:28Z): that test alone on a worktree of `main` `f1cdc88d` → exit 1, 1 failed

### Publication and hosted results

- `git push -u origin close/hde-crd-0002-tooling` → exit 0, new branch at `a90029c3`
- GitHub `create_pull_request` → #755; `subscribe_pr_activity` #755 → subscribed
- GitHub `actions_list` `list_workflow_runs` `epic-closeout-validation.yml` → `total_count: 2`; run 40353776342, event `pull_request`, head `a90029c3`
- GitHub `actions_list` `list_workflow_jobs` 40353776342 → job 121680627274, every step `success`
- GitHub `get_job_logs` job 121680627274 → 483 lines, the API's `original_length` 483, read whole
- GitHub `actions_list` `list_workflow_jobs` 40353776329 → job 121680627088, every step `success`
- GitHub `get_job_logs` job 121680627088 → download URL; `curl -sS -o <scratch>/hosted/test_job_121680627088.log <url>` → exit 0, 928 lines, 75,532 bytes, SHA-256 `a85b7d7a…ee03`, read whole
- GitHub `pull_request_read` #755 `get` → `mergeable_state: clean`; `get_review_comments` → 0 threads; Codex summary comment 6420541734 → code review of `a90029c` completed with no findings
- TypeSafe `score_v8.py --request request-v8.2.json --label "HDE-CRD-0002 CL-C-10 closure decision after CL-05 B-6 (100926.1)" --session review --action-file <scratch>/action.txt --markdown` → HTTP 200, reading in §16
