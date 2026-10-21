---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.8"
record_kind: PR-35 checkpoint for the eighth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.7.md (v1.7, PR-35 checkpoint; blob cce2ac485fa2; 19,612 bytes; sha256 bfaf78fe2421c07a11e61a1ff6d753cd3d4e3d7c18ffa8b96bd021339af759a8); v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3 and 0f4bb07, pushed; 78b51720b98aac00115307b03703d985fcd4ec2a (CX6-15, CX6-16 and CX6-17; parent 0f4bb07); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T20:44Z
next_step: push 78b5172 and this record; answer the CX6-15, CX6-16 and CX6-17 threads naming 78b5172 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.8 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `0f4bb07` raised three findings:

- CX6-15, P1 (security): replay and sweep run the candidate's code with the caller's environment and network.
- CX6-16, P2: the read-only check does not see ignored files.
- CX6-17, P2: the sweep skips its tool check when no file is uncovered.

CX6-15 changes the child environment that plan §5.8 approved and is a security finding, not one of the fidelity findings PO-35-2 covers, so it was put to Nathan, the Product Owner. He decided it as PO-35-3 (§2a): an allowlisted child environment plus a stated trust boundary, with no network sandbox. `78b5172` fixes all three and is verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-11 | Codex reviews 5571963225 to 5575476393; P2 | `d2ed4fc` to `b5694ae` | as results v1.1 to v1.6 | fixed or dispositioned; threads resolved |
| CX6-12 to CX6-14 | Codex review 5576227131; P2 | `36d292b` | runner variables in called scripts; `persist-credentials`; editable version | CX6-12 declined by PO-35-1; CX6-13 and CX6-14 fixed in `2d567a3` (result v1.7); replies r4318105182, r4318105502, r4318106348; threads resolved |
| CX6-15 | Codex review 5576889488 (on `0f4bb07`), comment r4318144249, **P1** | `0f4bb07` | `tools/ci/prepush_check.py` 1579: a changed `run:` body is launched "with normal host network access and nearly the entire inherited environment"; `SAFE_MODE=1` and `ALLOW_NETWORK=0` "are only environment variables", so a command could exfiltrate "credentials not covered by `REMOVED_ENV_KEYS`"; "run replay commands in an actual network-disabled sandbox with an allowlisted environment, or fail closed on commands that cannot be isolated" | Confirmed: at `0f4bb07`, `child_environment` passed a caller's `AWS_SECRET_ACCESS_KEY` to children, as plan §5.8 specified ("the caller's environment without" the listed keys). **Decided by PO-35-3 (§2a)**, fixed in `78b5172`: the allowlisted environment, and the trust boundary stated in the code and `--help`. The network sandbox is not built. Before the decision, measured here: `unshare --user --map-current-user --net` works in this container, which runs as root, and nine test files refer to `localhost` or `127.0.0.1`. Known platform behaviour, not measured here: Ubuntu 24.04 restricts unprivileged user namespaces by default, and a new network namespace starts with its loopback down (§3, IF-35-10) |
| CX6-16 | same review, comment r4318144266, P2 | `0f4bb07` | `tools/ci/prepush_check.py` 273: `git status --untracked-files=all` omits ignored files, so modifying or deleting one leaves the before and after states equal and the tool prints `repository unchanged` | Confirmed: at `0f4bb07`, rewriting an ignored file and creating another left `repository_state` equal. Fixed in `78b5172` (§3) |
| CX6-17 | same review, comment r4318144280, P2 | `0f4bb07` | `tools/ci/prepush_check.py` 764: with zero uncovered tests the sweep returns before checking `SWEEP_TOOLS`, so an environment without `ruby` reports PASS | Confirmed: at `0f4bb07`, a covered synthetic repository swept with a `PATH` lacking `ruby` gave `PREPUSH_CHECK_RESULT: PASS sweep=PASS`. Also, with uncovered files, a missing tool only printed a `TOOLING_FAILURE` line without failing the report. Fixed in `78b5172` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

### 2a. Product Owner decisions in this session

PO-35-1 and PO-35-2 are as result v1.7 §2a.

| ID | Question put (verbatim) | Options offered | Decision |
| :- | :- | :- | :- |
| PO-35-3 | "Codex CX6-15 (P1, security) on PR #660: replay and sweep run the candidate's own scripts with the caller's network and nearly the whole caller environment. Only the listed vendor, DB and GitHub keys are removed, so e.g. AWS_SECRET_ACCESS_KEY reaches candidate code, and SAFE_MODE/ALLOW_NETWORK are only flags. That is what plan §5.8 and instruction ID-9 approved ('the caller's environment without [the keys]'); it matters when the code isn't the caller's own. A network sandbox (unshare user+net namespaces) works in this root container. On default Ubuntu 24.04 it would refuse for non-root users, and a new network namespace has no loopback, which 9 test files may need. How should I handle it?" | Allowlist env, state limit (recommended); Allowlist + network sandbox; Decline, state trust boundary; Route to rescope (RS-20) | "Allowlist env, state limit (Recommended)" |

The answer was given through the session's question tool before the local commit of 20:05:09Z. The chosen option's description, verbatim: "Children get only a hosted-runner-like environment (PATH, HOME, USER, LOGNAME, SHELL, TERM, the tool's temp dirs, closed rails, modelled runner variables, job env), so the caller's secrets no longer reach candidate code. No network sandbox: the code and help state that replay and sweep run the candidate's code with the caller's file and network access, so use them only on code you trust. Stricter than plan §5.8; recorded as an in-flight decision."

## 3. Correction CX6-15, CX6-16 and CX6-17 (`78b5172`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `0229d20a1447`; 1,716 lines; +47/−14 on `0f4bb07`) | **CX6-15.** New `CHILD_INHERITED_KEYS = ("HOME", "LOGNAME", "PATH", "SHELL", "TERM", "USER")`. `child_environment` copies only those from the caller's environment, then sets closed rails, puts the interpreter's directory first on `PATH`, and sets `TMPDIR`, `XDG_STATE_HOME` and each report's own values. `REMOVED_ENV_KEYS` stays as the named list of keys that are never passed, none of them allowlisted. The replay's separate removal of inherited runner variables is no longer needed: no runner variable is allowlisted. The module docstring, which is the `--help` text, now states the trust boundary: "Children inherit only HOME, LOGNAME, PATH, SHELL, TERM and USER from the caller's environment, so no other variable of the caller's, secrets included, reaches them. They are not sandboxed: ``sweep`` and ``replay`` execute the candidate's own tests and workflow steps with the caller's file-system and network access, and SAFE_MODE and ALLOW_NETWORK are application flags, not isolation. Run them only on code you trust." **CX6-16.** `RepositoryState` gains `ignored`: every file from `git ls-files -z --others --ignored --exclude-standard`, with its lstat mode, size, `st_mtime_ns` and `st_ctime_ns`. Any write changes `st_ctime_ns`, which user space cannot set back, so no content is read. A file listed but gone records `-1`s. Creating, deleting or rewriting an ignored file now changes the state, and the result and violation lines name "ignored files". **CX6-17.** `report_sweep` checks `bash`, `curl` and `ruby` on the child `PATH` before computing coverage, so whether or not any file is uncovered. A missing tool is a tooling failure of the sweep (PF10 addendum 2.2; instruction ID-9). The old informational line in the run step is removed |
| `tests/tools/test_prepush_check.py` (blob `b8a4bbb62706`; 802 lines; +41/−6) | **Child environment.** The caller's environment includes the dummy keys, `AWS_SECRET_ACCESS_KEY`, `HTTPS_PROXY`, `GITHUB_SHA` and `GIT_DIR`. The child's keys are exactly `HOME`, `PATH`, `USER`, `TMPDIR`, `XDG_STATE_HOME` and the closed rails. **Synthetic replay.** The caller also sets `AWS_SECRET_ACCESS_KEY`, which the called script must not see. **Ignored files.** New `test_repository_state_covers_ignored_files`: two ignored files are listed, the state is stable, and a rewrite, a creation and a deletion each change it while `git status` stays empty. **Sweep.** The case with no uncovered file is rerun with a `PATH` holding only `git`, `bash`, `curl` and `sh`: `TOOLING_FAILURE missing on PATH: ruby`, exit 1, `uncovered=0`. 41 cases (40 + 1); `import shutil` added |

## 4. CI on `0f4bb07`

Run 39313715228 (job 118269633287) on `0f4bb07` ran from 19:46:05Z to 20:05:24Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 19:50:00Z with CX6-15 to CX6-17. It was not waited on and is not a gate. Its result covers `0f4bb07` only, whose code `78b5172` changes.

## 5. Local validation of `78b5172`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, with its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `78b5172` by fetch and checkout from the session's checkout. First, `git clean -fdX` removed their ignored caches. They then had no untracked or ignored files, and each only its main worktree. One fresh clone was made per negative control. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 41 passed in 47.8 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..78b5172`, `pull_request` | exit 0; `reason=selected_lanes;paths=11;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `78b5172`, committed there | All 26 fail as intended, each clone clean afterwards. NC-11 to NC-29 and NC-31 to NC-34 fail exactly the cases they failed at `2d567a3` (result v1.7 §5 item 5). NC-30 is retargeted to the allowlist (children get plan §5.8's caller environment minus the listed keys again): the child-environment case and both synthetic replay cases fail. NC-35 (ignored files dropped from `RepositoryState`): `test_repository_state_covers_ignored_files` fails. NC-36 (the sweep's tool check removed): the sweep case fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2`; `--help` | result v1.7 §5 item 6 (A) to (D) and result v1.6 §5 item 6's fifteen cases: identical output. `--help` prints the trust-boundary paragraph quoted in §3 |
| 7 | Premises at `0f4bb07`, with that head's tool loaded from its blob (scratch only) | CX6-15: `child_environment` passed `AWS_SECRET_ACCESS_KEY`. CX6-16: the state was equal after an ignored file was rewritten and another created. CX6-17: the sweep of a covered synthetic repository with a `PATH` lacking `ruby` exited 0 with `PASS sweep=PASS` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 20:09:02Z to 20:43:50Z (concurrent with item 9), every step with the allowlisted child environment; classify `reason=selected_lanes;paths=11`, all seven lanes; every one of the 16 steps SUCCESS; changed tests 166 targets, 3,927 passed (result v1.7's 3,926 plus the one new case); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 2,079.6 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, HEAD and git metadata)`. `cand` before and after: `head=78b5172…`, `status_lines=0`, `git_metadata_digest=8ddc7bd9012db0c54d2307b2d30499764563e772896c89e1308249279f8ff5dc`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,227 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,736.5 s (20:09:03Z to 20:38:01Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.7's 5,226 plus the one new owner-test case; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-9 | as results v1.1 to v1.7 §6 | unchanged | as recorded there |
| IF-35-10 | The child environment is an allowlist (`CHILD_INHERITED_KEYS`), not plan §5.8's "the caller's environment without" the listed keys. The trust boundary is stated in the code and `--help`. No network sandbox. Decided by the Product Owner (PO-35-3) | CX6-15 (P1) showed the caller's other secrets reaching candidate code. Instruction ID-9's own wording, "Child processes get the `ci.yml` job environment (closed rails)", is met more closely by a hosted-runner-like allowlist than by the caller's whole environment. A network sandbox would refuse on default Ubuntu 24.04 for non-root users and could break loopback tests, so the remaining exposure (the caller's files and network) is stated rather than hidden. Consequence: a step or test relying on any other caller variable sees it absent, as on a hosted runner | §5 items 1, 5 (NC-30), 6, 7, 8, 9 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.7 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 19:45:56 | push 7 of PR-35: `36d292b..0f4bb07` (`2d567a3`, the v1.7 record), fast-forward, no force | remote head `0f4bb07…`; v1.7 read back from the remote: blob `cce2ac485fa2`, 19,612 bytes, sha256 equal to the local file |
| 19:46:10 to 19:46:17 | replies r4318105182 (CX6-12, PO-35-1 and the traced path), r4318105502 (CX6-13) and r4318106348 (CX6-14); the three threads resolved | GitHub |
| 19:46:13 to 19:50:00 | Codex code review on `0f4bb07` (trigger "New commits"): review 5576889488, findings CX6-15 (P1) to CX6-17 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 19:46:05 to 20:05:24 | CI run 39313715228 on `0f4bb07`: success, stale | §4 |
| before 20:05:09 | PO-35-3 | §2a |
| 20:05:09 | local commit `78b5172` | §3 |
| 20:11:40 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved from 20:40Z to 21:45Z, after the round-9 push; it carries PO-35-1 to PO-35-3 | it creates no session |
| 20:09:02 to 20:43:50 | local validation of `78b5172`, all passed | §5 |
| after this record | push 8 of PR-35: `78b5172` and the commit adding this record, fast-forward onto `0f4bb07`, no force | read back in the next record |
| next | answer the CX6-15 to CX6-17 threads naming `78b5172` (CX6-15 with PO-35-3) and resolve them; read the Codex re-review and hosted CI of the new head | next record |

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
| WU-DOC-01 usage note: as result v1.6 §8, plus the trust boundary (use sweep and replay only on code you trust) and the allowlisted child environment. OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
| Closed rails | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)" (read in full on `main`): "Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default"; the allowlisted child environment still sets both |
| In-flight scope | instruction v1.0 ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.7, §5.8, PD-8, §6.1, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
