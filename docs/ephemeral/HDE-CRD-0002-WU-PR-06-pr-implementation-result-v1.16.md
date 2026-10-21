---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.16"
record_kind: PR-35 checkpoint for the sixteenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.15.md (v1.15, PR-35 checkpoint; blob 08cf62c76359; 20,915 bytes; sha256 4fc2c52f85adb84429d81ac7000f25f6fcdc38b1aa5a8e7c1c1e222b97beb66a); v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0 and ef06f44, pushed; 7be75efd2ed4f3cdcb2d1103823f1fe8a0a9d4a9 (CX6-35; parent ef06f44); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T02:53Z
next_step: push 7be75ef and this record; answer the CX6-35 thread naming 7be75ef and resolve it; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.16 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `ef06f44` raised one P2 finding, CX6-35. The install substitute returned success for `python -m pip install` with no operands, a command pip refuses.

Under PO-35-2 it is fixed in `7be75ef` and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-31 | Codex reviews 5571963225 to 5579511731 | `d2ed4fc` to `161941f` | as results v1.1 to v1.14 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-32 to CX6-34 | Codex review 5579783963; P2 | `0783969` | repeated top-level keys; folded more-indented lines; malformed extras | fixed in `0575fb0` (result v1.15); replies r4320807031, r4320807293 and r4320807526; threads resolved |
| CX6-35 | Codex review 5580042716 (on `ef06f44`), comment r4320834024, P2 | `ef06f44` | `tools/ci/prepush_check.py` 1663: "When `needs_python` is true and the excluded step is changed to `python -m pip install`, `rest` is empty, the loop adds no roots, and `_install_check` returns success", while "Pip instead exits nonzero because every documented install form requires a requirement, requirements file, project, or archive"; "reject an empty operand list" | Confirmed at `ef06f44`: `python -m pip install` and `pip install` each gave `success` from the substitute. The real pip 24.0 of the environment exits 1 on the same command with `ERROR: You must give at least one requirement to install`. Fixed in `7be75ef` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-35 (`7be75ef`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `9a35939db67f`; 1,991 lines; +3/−0 on `ef06f44`) | `_install_check` refuses an install whose operand list is empty ("the install step names nothing to install, which pip refuses"), and `_substitute` reports it as tooling. pip refuses only when there is no requirement argument, `-e` or `-r` at all. Every option the substitute accepts carries an operand, and `-r` or `-e` without one is already refused as an unsupported option. So the empty operand list is exactly pip's refusal case. An empty requirements file, which pip accepts, stays accepted |
| `tests/tools/test_prepush_check.py` (blob `a712d63991ea`; 1,095 lines; +8/−0) | New `test_an_install_step_with_nothing_to_install_is_refused`, three parameters: `python -m pip install`, `pip install`, and the first with trailing spaces. Each is refused by `_install_check` and reported as tooling by `_substitute`. 94 cases (91 + 3) |

## 4. CI on `ef06f44`

Run 39358003580 (job 118417214014) on `ef06f44` ran from 02:16:20Z to 02:37:19Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 02:21:57Z with CX6-35. It was not waited on and is not a gate; its result covers `ef06f44` only, whose code `7be75ef` changes. The changed-tests failure of result v1.13 §4 did not recur.

## 5. Local validation of `7be75ef`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `7be75ef` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `7be75ef`;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 94 passed in 38.5 s, exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..7be75ef`, `pull_request` | exit 0; `reason=selected_lanes;paths=19;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged; `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `7be75ef`, committed there (02:24:32Z to 02:51:01Z, two at a time) | All 59 fail as intended, each clone clean afterwards. NC-11 to NC-68 fail exactly the cases they failed at `0575fb0` (result v1.15 §5 item 5). The new control NC-69 (the empty-operand refusal removed) fails all three parameters of `test_an_install_step_with_nothing_to_install_is_refused` |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.15's, all three: the real install step, which names operands, still passes; `cand2` clean |
| 7 | Premises at `ef06f44` (that head's tool, scratch only), and the fix (the tool at `7be75ef`) | At `ef06f44`: `python -m pip install` and `pip install` each returned `[]` from `_install_check` and `success` from `_substitute`; `-r` and `-e` without an operand were already refused as unsupported options. pip 24.0 itself, with no operands: exit 1, `ERROR: You must give at least one requirement to install (see "pip help install")`. With `--no-index -r` and an empty requirements file: exit 0, no output. Under the fix both are refused ("names nothing to install"), and `_substitute` reports tooling; the `-r` and `-e` cases are unchanged |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 02:24:32Z to 02:51:23Z (concurrent with items 5 and 9); classify `reason=selected_lanes;paths=19`, all seven lanes; every one of the 16 steps SUCCESS, the install substitute (step 05) passing on the real step, which names its operands. Changed tests 166 targets, 3,980 passed (result v1.15's 3,977 plus the three new cases), the close-pack test among them; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,604.0 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=7be75ef…`, `status_lines=0`, `git_metadata_digest=d890e083cc7693ce5103bf2fb5e5a8fa33184e672dea6b5c00b34a70d7a31393`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,280 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,331.6 s (02:24:32Z to 02:46:56Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.15's 5,277 plus the three new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-17 | as results v1.1 to v1.15 §6 | unchanged | as recorded there |

No new in-flight decision: the fix is the finding's own remedy, with no choice beyond it.

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.15 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 02:16:09 | push 15 of PR-35: `0783969..ef06f44` (`0575fb0`, the v1.15 record), fast-forward, no force | remote head `ef06f44…`; v1.15 read back from the remote: blob `08cf62c76359`, 20,915 bytes, sha256 equal to the local file |
| 02:16:21 to 02:16:28 | replies r4320807031 (CX6-32), r4320807293 (CX6-33) and r4320807526 (CX6-34); the three threads resolved | GitHub |
| 02:16:37 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 03:10Z | it creates no session |
| 02:16:28 to 02:21:57 | Codex code review on `ef06f44` (trigger "New commits"): review 5580042716, finding CX6-35 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 02:16:20 to 02:37:19 | CI run 39358003580 on `ef06f44`: success, stale | §4 |
| 02:24:04 | local commit `7be75ef` | §3 |
| 02:24:32 to 02:51:23 | local validation of `7be75ef`, all passed | §5 |
| after this record | push 16 of PR-35: `7be75ef` and the commit adding this record, fast-forward onto `ef06f44`, no force | read back in the next record |
| next | answer the CX6-35 thread naming `7be75ef` and resolve it; move the safety-net check-in if needed; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969` or `ef06f44` (results v1.14 to v1.16 §4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines and the other unmodelled scalar, block and key forms; an install step other than one simple command | stated limits; TOOLING (IF-35-15 to IF-35-17) | recorded |
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
