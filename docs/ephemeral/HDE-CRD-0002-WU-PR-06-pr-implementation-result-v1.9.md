---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.9"
record_kind: PR-35 checkpoint for the ninth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.8.md (v1.8, PR-35 checkpoint; blob 19bd19aae0f3; 20,924 bytes; sha256 7c0bce0a4e62ffbc3f561a0eb37423f5642f1efb34bab64f97710f5fbcc78607); v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172 and 89e0828, pushed; 2fa03de96673a6d7563a39c0b09c11ca82cca0aa (CX6-18, CX6-19 and CX6-20; parent 89e0828); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T21:31Z
next_step: push 2fa03de and this record; answer the CX6-18, CX6-19 and CX6-20 threads naming 2fa03de and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.9 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `89e0828` raised three P2 findings:

- CX6-18: a condition on the checkout step is accepted.
- CX6-19: empty directories are outside the read-only check.
- CX6-20: a step `env` that is not a mapping is ignored.

Under PO-35-2 ("Fix every finding") all three are fixed in `2fa03de`, together with one more instance of CX6-20's root cause: a step entry that is not a mapping. The fix is verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-14 | Codex reviews 5571963225 to 5576227131 | `d2ed4fc` to `36d292b` | as results v1.1 to v1.7 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-15 to CX6-17 | Codex review 5576889488; CX6-15 P1, the others P2 | `0f4bb07` | child environment and network; ignored files; sweep tools | fixed in `78b5172` (result v1.8; CX6-15 as PO-35-3); replies r4318687833, r4318688513, r4318689044; threads resolved |
| CX6-18 | Codex review 5577595526 (on `89e0828`), comment r4318726214, P2 | `89e0828` | `tools/ci/prepush_check.py` 1550: an `if:` that skips the checkout step, for example `if: ${{ false }}`, "is accepted by the inventory and can produce a replay PASS, while the hosted runner has no checked-out files"; "Require the modeled checkout step to execute unconditionally, or fail with inventory drift when its condition changes" | Confirmed: at `89e0828`, `replay_steps` accepted the real `ci.yml` with `if: ${{ false }}` on the checkout step. Fixed in `2fa03de` (§3): the checkout step may carry no `if`, and the root cause is closed for every excluded step |
| CX6-19 | same review, comment r4318726232, P2 | `89e0828` | `tools/ci/prepush_check.py` 279: creating or removing an empty ignored directory leaves `RepositoryState` equal, because `git ls-files --others --ignored` lists no directory; "include ignored directory identities in the snapshot as well" | Confirmed: at `89e0828`, creating an empty ignored directory left the state equal, and so did an empty untracked one. Fixed in `2fa03de` (§3): every working-tree directory is in the state |
| CX6-20 | same review, comment r4318726227, P2 | `89e0828` | `tools/ci/prepush_check.py` 1053: a scalar or sequence step `env` "is treated as having no keys and `_execute` silently ignores it", although GitHub Actions requires a mapping; "classify every non-dictionary step environment as inventory drift" | Confirmed: at `89e0828`, `env: invalid` on the citation step was accepted. Fixed in `2fa03de` (§3). The same root cause in the parser, a step entry that is not a mapping and was silently dropped, is fixed with it |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-18, CX6-19 and CX6-20 (`2fa03de`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `f1da9a7acf0c`; 1,744 lines; +37/−9 on `89e0828`) | **CX6-18.** New `REPLAY_EXCLUDED_STEP_KEYS` lists the keys each excluded step may carry, which are exactly the ones its substitute models: the checkout `name`, `id`, `uses`, `with`, with no `if`, since the copy exists before step 1 whatever a condition says; setup-python `name`, `id`, `if`, `uses`, `with`; the install step `name`, `id`, `if`, `run`. Any other key, including an `env` or `shell` on any excluded step, is `REPLAY_INVENTORY_DRIFT`. **CX6-20.** A step `env` that is not a mapping is `REPLAY_INVENTORY_DRIFT`. `parse_jobs` now refuses a job whose steps include an entry that is not a mapping ("unsupported shape"), instead of dropping it. **CX6-19.** `RepositoryState` gains `directories`: every working-tree directory outside `.git`, from `os.walk` without following links, with its lstat mode, `st_mtime_ns` and `st_ctime_ns`. Adding or removing an entry changes its parent's mtime and ctime, so an empty directory, ignored or not, can no longer appear or vanish unseen. The result and violation lines name "directories" |
| `tests/tools/test_prepush_check.py` (blob `285b8aef0538`; 829 lines; +29/−2) | Three drift cases: `checkout-condition` (`if: ${{ false }}`), `install-env` (an `env` on the install step) and `step-env-not-a-mapping` (`env: invalid`). New `test_a_step_that_is_not_a_mapping_is_refused` (a bare `- echo hi` step). The ignored-file case also creates and removes an empty ignored directory and creates an empty untracked one: each changes the state while `git status` stays empty, and `.git` is not among the directories. 45 cases (41 + 4) |

## 4. CI on `89e0828`

Run 39322027467 (job 118298216656) on `89e0828` ran from 20:45:49Z to 20:58:40Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 20:50:22Z with CX6-18 to CX6-20. It was not waited on and is not a gate. Its result covers `89e0828` only, whose code `2fa03de` changes.

## 5. Local validation of `2fa03de`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `2fa03de` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 45 passed in 44.1 s (concurrent with items 5, 8 and 9), exit 0. One `PytestWarning` followed the summary: pytest's own cleanup of an older `/tmp/pytest-of-root/garbage-*` directory failed while the concurrent negative-control sessions used the same root. It is not a test result |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..2fa03de`, `pull_request` | exit 0; `reason=selected_lanes;paths=12;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `2fa03de`, committed there | All 30 fail as intended, each clone clean afterwards. NC-11 to NC-36 fail exactly the cases they failed at `78b5172` (result v1.8 §5 item 5); NC-28 and NC-35 are retargeted to the edited lines. NC-37 (the excluded-step key check removed): `checkout-condition` and `install-env` fail. NC-38 (a non-mapping step `env` read as empty, as at `89e0828`): `step-env-not-a-mapping` fails. NC-39 (non-mapping step entries dropped again): `test_a_step_that_is_not_a_mapping_is_refused` fails. NC-40 (directories dropped from `RepositoryState`): the ignored-file case fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` | result v1.8 §5 item 6's cases: output byte-identical to that round's |
| 7 | Premises at `89e0828` (that head's tool, scratch only) | CX6-18: `replay_steps` accepted the checkout step with `if: ${{ false }}`. CX6-20: it accepted `env: invalid` on the citation step. CX6-19: creating an empty ignored directory, and an empty untracked one, left `repository_state` equal |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 20:57:21Z to 21:30:59Z (concurrent with item 9); classify `reason=selected_lanes;paths=12`, all seven lanes; every one of the 16 steps SUCCESS, the real `ci.yml` passing the excluded-step key check; changed tests 166 targets, 3,931 passed (result v1.8's 3,927 plus the four new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,011.2 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=2fa03de…`, `status_lines=0`, `git_metadata_digest=6a6eb7e30aceeadda0954ca21ce4790c488b72b8f68235c710969196ff75dc56`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,231 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,695.2 s (20:57:22Z to 21:25:39Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.8's 5,227 plus the four new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-10 | as results v1.1 to v1.8 §6 | unchanged | as recorded there |
| IF-35-11 | Three fixes beyond the findings' literal text. First, CX6-18 is applied to every excluded step's keys, not only the checkout's `if`: `env` and `shell` on any of them, and `if` on the checkout. Second, CX6-20's rule is applied to step entries, so a step that is not a mapping is refused rather than dropped. Third, the read-only state covers every directory, untracked ones included, not only ignored ones (CX6-19) | Each is the same root cause as its finding: a workflow shape the replay does not model, or a write outside both listings, would otherwise pass unseen. PO-35-2 asks for every finding to be fixed, and fixing only the named instance would invite the next round on the sibling | §5 items 1, 5 (NC-37 to NC-40), 7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.8 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 20:45:42 | push 8 of PR-35: `0f4bb07..89e0828` (`78b5172`, the v1.8 record), fast-forward, no force | remote head `89e0828…`; v1.8 read back from the remote: blob `19bd19aae0f3`, 20,924 bytes, sha256 equal to the local file |
| 20:46:08 to 20:46:16 | replies r4318687833 (CX6-15, with PO-35-3), r4318688513 (CX6-16) and r4318689044 (CX6-17); the three threads resolved | GitHub |
| 20:46:00 to 20:50:22 | Codex code review on `89e0828` (trigger "New commits"): review 5577595526, findings CX6-18 to CX6-20 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 20:45:49 to 20:58:40 | CI run 39322027467 on `89e0828`: success, stale | §4 |
| 20:55:41 | local commit `2fa03de` | §3 |
| 20:57:21 to 21:30:59 | local validation of `2fa03de`, all passed | §5 |
| after this record | push 9 of PR-35: `2fa03de` and the commit adding this record, fast-forward onto `89e0828`, no force; then the safety-net check-in re-armed after the push | read back in the next record |
| next | answer the CX6-18 to CX6-20 threads naming `2fa03de` and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; one modelled build system plus the fail-closed proxy (IF-35-7) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note (as result v1.8 §8); OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7, §5.8, PD-8, §6.1, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
