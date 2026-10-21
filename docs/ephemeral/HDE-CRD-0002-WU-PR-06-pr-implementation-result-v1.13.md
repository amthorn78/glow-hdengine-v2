---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.13"
record_kind: PR-35 checkpoint for the thirteenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.12.md (v1.12, PR-35 checkpoint; blob b8cba496e256; 20,083 bytes; sha256 3386df8edfa35b1a83b583ab16338b12129b0af52f056c144fe9930b6b08dcdf); v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; blob 2848847e8bee)
effective_baseline: unchanged from result v1.0 (approved base + PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; unchanged on origin/main 0442d23). Provenance, not a gate
pf10_addendum_created: none
proceed: the original Proceed of result v1.0. No other Proceed exists or is needed
session: the dedicated HDE-CRD-0002 WU-PR-06 PR-35 session, https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary
pull_request: amthorn78/glow-hdengine-v2#660 (https://github.com/amthorn78/glow-hdengine-v2/pull/660), branch claude/youthful-gauss-d9e0ab into main
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694 and 7a3b7b2, pushed; 55a973bff3440575cbdb484b9526f081cc5801e2 (CX6-29; parent 7a3b7b2); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T00:46Z
next_step: push 55a973b and this record; answer the CX6-29 thread naming 55a973b and resolve it; read the Codex re-review and hosted CI of the new head over the active subscription, including whether the changed-tests failure of §4 recurs; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.13 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `7a3b7b2` raised one P2 finding, CX6-29. The replay skipped a `GITHUB_OUTPUT` line without `=` and marked the step successful, where the GitHub runner rejects the record and fails the step.

Under PO-35-2 it is fixed in `55a973b` (IF-35-15) and verified locally (§3, §5).

Hosted CI on `7a3b7b2` failed, in one test this PR does not touch, which ran before any code this PR changes (§4). That run is stale because of CX6-29. The evidence so far points to an intermittent failure outside this PR, but the mechanism is not established; the next head's CI is the check.

This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-27 | Codex reviews 5571963225 to 5578496092 | `d2ed4fc` to `14a5858` | as results v1.1 to v1.11 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-28 | Codex review 5578877595; P2 | `efff0bb` | installed editable metadata not compared with the candidate | fixed in `9855694` (result v1.12); reply r4320098169; thread resolved |
| CX6-29 | Codex review 5579226115 (on `7a3b7b2`), comment r4320129699, P2 | `7a3b7b2` | `tools/ci/prepush_check.py` 1793: "When an executed step appends a nonempty line without `=`", for example `echo invalid >> "$GITHUB_OUTPUT"`, "this parser silently skips the malformed line and still marks the step successful", while the GitHub Actions runner "throws on that record and marks the step failed"; "validate the entire file and either implement the documented delimiter form or classify unsupported records as tooling failure" | Confirmed at `7a3b7b2`, in four forms. The line without `=` gave `success`, with the outputs after it kept. A heredoc record (`body<<EOF`) gave `success` with the output dropped. An empty name (`=v`) and a carriage return were accepted. The `lanes` report's reader of the classifier's output had the same defect. Fixed in `55a973b` for both readers (§3, IF-35-15) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-29 (`55a973b`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `91a8b5e59d0f`; 1,927 lines; +40/−13 on `7a3b7b2`) | New `parse_github_output`, the one reader of a `GITHUB_OUTPUT` file, used by the replay's `_execute` and by the `lanes` report's `_print_outputs`. It reads the file as the Linux runner does: split at line feeds, empty lines skipped, `NAME=VALUE` at the first `=`. A line with neither `=` nor `<<` is a BEHAVIOR problem: the runner rejects it and fails the step, keeping the outputs set before it. The heredoc form `NAME<<DELIMITER`, an empty name, a carriage return and text that is not UTF-8 are not modelled, and are TOOLING problems. In `_execute`, the step fails on either problem, whatever its exit status, because the runner reads file commands after every step; the problem line follows the exit line in the detail. In `lanes`, a problem fails the report: tooling when unmodelled, otherwise behavior |
| `tests/tools/test_prepush_check.py` (blob `b490a030feef`; 1,032 lines; +58/−0) | New `test_github_output_is_read_as_the_linux_runner_reads_it`, nine parameters: empty file; `NAME=VALUE` forms, including a value with `=`, a `<<` after `=`, an empty value and no final line feed; no separator; heredoc; `<<` before `=`; empty name; carriage return; a carriage return alone; not UTF-8. New `test_a_step_whose_output_the_runner_rejects_fails`, through `_execute`: a valid record succeeds; a rejected record fails as BEHAVIOR, keeping the earlier output; an unmodelled record after a nonzero exit gives both lines. New `test_lanes_refuses_classifier_output_the_runner_would_reject`. 71 cases (60 + 11) |

## 4. CI on `7a3b7b2`

Run 39345008218 (job 118375390428) on `7a3b7b2` ran from 00:00:22Z to 00:07:14Z and completed with conclusion **`failure`**. It became stale when the re-review completed at 00:06:25Z with CX6-29, and it is not a gate. Its failure is recorded here, not set aside:

- **What failed.** In "Run affected behavioral tests in isolation", `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest` failed at its last assertion (line 2872). After the recovery `--write` and commit, `--check` returned 1 with `EPIC_CLOSE_PACK_ERROR:MANIFEST_BINDING_MISMATCH` and `EPIC_CLOSE_PACK_ERROR:CHECK_MODE_MUTATION`. The other 3,945 tests passed. Every later lane was skipped, and the final audit printed `APPLICABLE_CI_LANE_NOT_SUCCESSFUL` for each.
- **Why it is not attributed to this PR.** This PR does not touch the test or `tools/qa/generate_epic_close_pack.py`. In CI's target list, the close-pack test (target 143 of 166) runs before this PR's owner test (target 156) in the same pytest process, so no code this PR changes had run when it failed. The last `main` run, on `822ce15`, succeeded; no run is listed for `0442d23` itself. All 12 earlier runs on this PR succeeded, from `d2ed4fc` to `efff0bb`.
- **Local evidence.** At `7a3b7b2`, the test alone passed 40 times out of 40, in a fresh clone under closed rails. It also passed within the replay's changed-tests step at `55a973b` (§5 item 8) and in the sweep (§5 item 9).
- **Mechanism: not established.** The tool reads its outputs with `O_NOATIME` and fails closed on any atime, mtime or ctime change during `--check`, but the `git status` it runs as a subprocess reads files normally. Both errors fit a file's metadata changing during the check. One candidate mechanism is a write and `git add` landing in the same coarse clock tick, so that atime equals mtime and a later read advances atime under `relatime`. Here it did not reproduce in 30 write/add/commit/status cycles: this filesystem's timestamps are fine-grained, and `git add` read about 3 ms after the write. It remains a hypothesis.
- **Next.** The new head's CI is the next evidence, as a fresh run over a new commit, not a re-run. If the test fails again there, it is treated as real, investigated further, and reported on the PR with a proposed patch; it is not in this PR's scope to change.

## 5. Local validation of `55a973b`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `55a973b` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `55a973b`;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 71 passed in 36.2 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..55a973b`, `pull_request` | exit 0; `reason=selected_lanes;paths=16;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…` on the real classifier output | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, all eleven output records read, `PREPUSH_CHECK_RESULT: PASS lanes=PASS; repository unchanged (…)` |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `55a973b`, committed there (00:13:15Z to 00:37:38Z, two at a time) | All 48 fail as intended, each clone clean afterwards. NC-11 to NC-54 fail exactly the cases they failed at `9855694` (result v1.12 §5 item 5). The four new controls: NC-55 (the rejection of a line without `=` removed) fails the parser's `no-separator` case, the `_execute` case and the `lanes` case. NC-56 (the refusal of unmodelled forms removed) fails the parser's heredoc, `<<`-first, empty-name, carriage-return, lone-carriage-return and `_execute` cases. NC-57 (`_execute` ignores the problem) fails the `_execute` case. NC-58 (`lanes` ignores the problem) fails the `lanes` case |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.12's, all three; `cand2` clean |
| 7 | Premises at `7a3b7b2` (that head's tool, scratch only), and the fix | At `7a3b7b2`, `_execute` gave `success` for all four forms of §2. Under the fix: the line without `=` fails as BEHAVIOR ("the runner rejects GITHUB_OUTPUT record 'invalid'"); the heredoc, the empty name and the carriage return fail as TOOLING ("is a form the replay does not model"). The 40 isolated runs of §4 are also recorded here |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 00:13:01Z to 00:45:14Z (concurrent with items 1, 5 and 9); classify `reason=selected_lanes;paths=16`, all seven lanes; every one of the 16 steps SUCCESS, each executed step's `GITHUB_OUTPUT` read by the new parser. Changed tests 166 targets, 3,957 passed (result v1.12's 3,946 plus the eleven new cases), the close-pack test of §4 among them; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,926.2 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=55a973b…`, `status_lines=0`, `git_metadata_digest=1a357b4f0a2bbbbdab2c539707ee3837ddce89df97d049272136a90d381c7b33`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` (plan §9 item 6, restored after result v1.12's deviation) | **5,257 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,609.4 s (00:13:01Z to 00:39:53Z, concurrent with items 1, 5 and 8); pytest exit 0. The close-pack test of §4 passed. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.12's 5,246 plus the eleven new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-14 | as results v1.1 to v1.12 §6 | unchanged | as recorded there |
| IF-35-15 | Two choices. First, the forms the replay does not model are TOOLING failures: the heredoc form, an empty name, a carriage return and text that is not UTF-8. The heredoc form is not implemented. Consequence: a PR whose workflow step writes one of those forms gets a TOOLING failure from the replay until the parser models it; hosted CI is unaffected. Second, the `lanes` report's reader of the classifier's output, the same defect in a sibling place, uses the same parser | The workflow writes only `NAME=VALUE`: the classifier's `write_github_output` is the one step that writes `GITHUB_OUTPUT`. Implementing the heredoc form, or the runner's handling of an empty name or a carriage return, would model runner behavior no step uses, and is not verifiable offline, so those forms fail closed, as the finding's second option allows. The line without `=` is the one form whose runner outcome is certain, so it fails as BEHAVIOR. PO-35-2; plan §5.7 ("Execution": `GITHUB_OUTPUT` parsed into `steps.<id>.outputs`), PD-8 | §5 items 1, 4 (`lanes`), 5 (NC-55 to NC-58), 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.12 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 00:00:10 | push 12 of PR-35: `efff0bb..7a3b7b2` (`9855694`, the v1.12 record), fast-forward, no force | remote head `7a3b7b2…`; v1.12 read back from the remote: blob `b8cba496e256`, 20,083 bytes, sha256 equal to the local file |
| 00:00:46 | reply r4320098169 (CX6-28); the thread resolved | GitHub |
| 00:00:24 to 00:06:25 | Codex code review on `7a3b7b2` (trigger "New commits"): review 5579226115, finding CX6-29 | summary comment 6267808148 |
| 00:00:22 to 00:07:14 | CI run 39345008218 on `7a3b7b2`: **failure**, stale | §4 |
| 00:12:50 | local commit `55a973b` | §3 |
| 00:27 | PR comment 6280395750 on run 39345008218's failure: the failing check, why it is not attributed to this PR, that no fix exists yet and the mechanism is not established, and that the next head's run is the check; no re-run of the stale head | GitHub |
| 00:13:01 to 00:45:14 | local validation of `55a973b`, all passed | §5 |
| after this record | push 13 of PR-35: `55a973b` and the commit adding this record, fast-forward onto `7a3b7b2`, no force | read back in the next record |
| next | answer the CX6-29 thread naming `55a973b` and resolve it; move the safety-net check-in (now 01:05Z) to after the push if needed; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head, including whether §4's failure recurs.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (§4) | PR-35 watches the new head's CI; the close-pack tool and test are outside this PR's change set | mechanism not established; not attributed to this PR |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE` | stated limit; TOOLING (IF-35-15) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.10 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
| Merge | Nathan / Product Owner (manual) | pending |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

Read on `main` at `0442d23` (`docs/pfcanon/` unchanged since `5e62a65`; this branch changes no canon).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Sweep tools | PF10-HDE-Build-Notes v13.6.1 addendum 2.2 ("WU-PR-06's sweep environment must provide ruby") |
| Tooling vs behavior | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 |
| Closed rails | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)" (read in full on `main`) |
| Generated metadata stays out of the tree (IF-35-14, carried) | HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §27.4 "Tracked evidence boundary and rollback" |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7, §5.8, PD-8, §6.1, §9, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
