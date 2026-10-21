---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.17"
record_kind: PR-35 checkpoint for the seventeenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.16.md (v1.16, PR-35 checkpoint; blob 0d7b2026f6b4; 16,863 bytes; sha256 c7417408b24bf9c0e5a933636979f3abc1f30002d4f7d09a4ac25efda8b3cfd2); v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef and ba65334, pushed; bb524267e87068791a7260c609fc1b4d52843e1f (CX6-36 and CX6-37; parent ba65334); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T03:33Z
next_step: push bb52426 and this record; answer the CX6-36 and CX6-37 threads naming bb52426 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.17 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `ba65334` raised two P2 findings:

- CX6-36: the conditions of the substituted set-up and install steps are not pinned, so `if: ${{ false }}` skips the install substitute while the caller's environment still holds what the step installs.
- CX6-37: plain scalars that YAML reads as non-strings, such as `run: true`, are read as strings.

Under PO-35-2 both are fixed in `bb52426` (IF-35-18) and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-34 | Codex reviews 5571963225 to 5579783963 | `d2ed4fc` to `0783969` | as results v1.1 to v1.15 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-35 | Codex review 5580042716; P2 | `ef06f44` | an install step with no operands | fixed in `7be75ef` (result v1.16); reply r4320992576; thread resolved |
| CX6-36 | Codex review 5580246369 (on `ba65334`), comment r4321008931, P2 | `ba65334` | `tools/ci/prepush_check.py` 143: "if a candidate changes this install step's `if:` to `${{ false }}`, the inventory accepts it and `report_replay` skips `_install_check`", so later steps "can therefore pass using the caller's dependencies, while hosted `ci.yml` has not installed either the requirements or editable project"; "require the setup/install conditions to match the modeled workflow" | Confirmed at `ba65334`: `if: ${{ false }}` was accepted on the install step and on the set-up step, and so was the install step's condition removed. Fixed in `bb52426` (§3) |
| CX6-37 | same review, comment r4321008941, P2 | `ba65334` | `tools/ci/prepush_check.py` 462: "When an executed step is changed to `run: true`, this plain-scalar path returns the string `"true"`, so replay executes Bash's successful `true` builtin", while "YAML resolves unquoted `true` as a boolean" and the workflow schema "requires `run` to be a string, so hosted validation rejects the workflow"; "decode scalar types or fail closed on implicitly typed non-string values" | Confirmed at `ba65334`: `run:` set to `true`, `null`, `~`, `1.0`, `0x10` or `False` each read as that text. Job `env` values `1.0`, `0x10`, `010`, `+1`, `True` and `~` read as typed, where GitHub writes back another string. A key `true:` was accepted. Fixed in `bb52426` (§3, IF-35-18) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-36 and CX6-37 (`bb52426`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `6878c9116df2`; 2,040 lines; +54/−5 on `ba65334`) | **CX6-36.** New `REPLAY_EXCLUDED_STEP_CONDITIONS`. Each excluded step must carry exactly its modelled condition: none for the checkout, and `${{ steps.classify.outputs.needs_python == 'true' }}` for set-up and install. Any other condition, its absence included, is `REPLAY_INVENTORY_DRIFT`. **CX6-37.** New `_Resolved`, a string subclass marking a plain scalar that YAML 1.2's core schema reads as a null, boolean, integer or float. `_plain` returns one for such a scalar, never for a quoted or block one. A step's `name`, `id`, `if`, `uses`, `shell` or `run` that is resolved is `REPLAY_INVENTORY_DRIFT`, since GitHub requires a string there. An `env` or `with` value is accepted, through the new `_as_string`, only where GitHub writes it back unchanged: a string, `true`, `false`, or a decimal integer written `0` or without a leading zero, optionally after a minus sign. Any other resolved value is refused: as drift in a step, and as an unsupported shape in the job `env`. A key YAML reads as a non-string is refused |
| `tests/tools/test_prepush_check.py` (blob `912079a524b1`; 1,124 lines; +30/−1) | The drift test gains five cases: `install-condition` (`${{ false }}`), `setup-python-condition`, `install-condition-removed`, `run-boolean` (`run: true`), `step-env-float` (`HEAD_SHA: 1.0`). New `test_implicitly_typed_scalars_are_refused_unless_github_writes_them_back_unchanged`. It refuses job `env` values `1.0`, `0x10`, `010`, `+1`, `True`, `~`, `null` and `.inf`, and reads `true`, `false`, `0`, `12` and `-3` unchanged. It refuses a key `true:`, and checks that `TRUE` resolves while `'true'` and `ubuntu-latest` do not. 100 cases (94 + 6) |

## 4. CI on `ba65334`

Run 39361297404 (job 118427858257) on `ba65334` ran from 02:52:54Z to 03:07:33Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 02:56:26Z with CX6-36 and CX6-37. It was not waited on and is not a gate; its result covers `ba65334` only, whose code `bb52426` changes. The changed-tests failure of result v1.13 §4 did not recur.

## 5. Local validation of `bb52426`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `bb52426` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1, the negative controls and item 9;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `bb52426`;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 100 passed in 39.2 s, exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..bb52426`, `pull_request` | exit 0; `reason=selected_lanes;paths=20;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0; `lanes` exit 0, eleven output records, PASS, repository unchanged; `sweep --no-run` at the head `uncovered=0`, exit 0, and at `a429c7c` `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `bb52426`, committed there (03:01:33Z to 03:30:57Z, two at a time) | All 64 fail as intended, each clone clean afterwards. NC-11 to NC-69 fail the cases they failed at `7be75ef` (result v1.16 §5 item 5), with five explained differences. NC-38 (the `env`/`with` shape check removed) also fails `step-env-float`, and NC-50 (the job `env` check removed) and NC-62 (the key check removed) also fail the new typed-scalar test: those guards now carry the new checks. NC-37 (the excluded-step key check removed) no longer fails `checkout-condition`, and NC-46 (the strict-string check removed) no longer fails `step-if-not-a-string`, because the new condition pin also refuses those mutations. Two guards now cover each, and NC-46 still fails `run-boolean`. NC-38, NC-46, NC-50 and NC-62 are retargeted to their rewritten lines. The five new controls: NC-70 (the condition pin removed) fails `install-condition`, `setup-python-condition` and `install-condition-removed`. NC-71 (no scalar typed) fails `run-boolean`, `step-env-float` and the typed-scalar test. NC-72 (every typed value accepted as a string) fails `step-env-float` and the typed-scalar test. NC-73 (typed values accepted in strict-string keys) fails `run-boolean`. NC-74 (typed keys accepted) fails the typed-scalar test |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` (integ2 with the real-setuptools site, integ3, integ4) | output byte-identical to result v1.16's, all three. The real workflow reads all 16 steps: its excluded steps carry exactly the modelled conditions, and its two typed values, `fetch-depth: 0` and `persist-credentials: false`, are the forms GitHub writes back unchanged. `cand2` clean |
| 7 | Premises at `ba65334` (that head's tool, scratch only), and the fix (the tool at `bb52426`) | At `ba65334`: each case of §2 accepted, as listed there; the real workflow 16 steps. Under the fix: the three condition cases refused as drift, naming the condition and the modelled one. The six `run:` values refused as "not a string". The six job `env` values refused as an unsupported shape, while `true`, `0` and `12` still read unchanged. `true:` refused as a key. The real workflow still 16 steps. Rounds 15 to 17's premise cases at `bb52426` give their earlier outputs. Round 16's differs only in the printed order of one `frozenset` (`{'bar', 'foo'}` for `{'foo', 'bar'}`): set order varies with hash randomization between processes, and the contents are equal |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 03:01:33Z to 03:29:05Z (concurrent with items 5 and 9); the real workflow's excluded steps accepted with their modelled conditions; classify `reason=selected_lanes;paths=20`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 166 targets, 3,986 passed (result v1.16's 3,980 plus the six new cases), the close-pack test among them; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,646.0 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=bb52426…`, `status_lines=0`, `git_metadata_digest=bcd4fa8a15209202a09fbd1d5be1903a99dc6c828c0a9ddc52a420fdedaa4773`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,286 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,371.7 s (03:01:33Z to 03:24:38Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. That is result v1.16's 5,280 plus the six new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-17 | as results v1.1 to v1.15 §6 | unchanged | as recorded there |
| IF-35-18 | Three choices. First, CX6-36 pins the condition of every excluded step, not only the install step's. The set-up step is skipped in the same way, and a removed condition counts as drift too. Second, CX6-37 is fixed by typing plain scalars with YAML 1.2's core schema and refusing them where GitHub requires a string, rather than refusing every unquoted scalar. GitHub reads YAML 1.2: its `on:` key would be a boolean under 1.1. Third, in `env` and `with`, where GitHub converts a typed value to a string, only `true`, `false` and decimal integers are accepted, the spellings GitHub writes back unchanged; keys of a typed form are refused. Consequence: a PR that writes another such form gets a TOOLING failure from the replay until the model covers it; hosted CI is unaffected | A substitute stands in for its step only when the step runs exactly when CI runs it, because the caller's environment holds what the substituted steps provide either way. The real workflow uses exactly the modelled conditions, and its only typed values are `fetch-depth: 0` and `persist-credentials: false` (§5 item 6). So the closed model costs nothing there, while a value GitHub writes back as another string would make the replay run different inputs. PO-35-2; plan §5.7 (excluded steps, substituted outcomes; the YAML subset, PD-8) | §5 items 1, 5 (NC-38, NC-46, NC-50 and NC-62 retargeted; NC-70 to NC-74), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.16 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 02:52:47 | push 16 of PR-35: `ef06f44..ba65334` (`7be75ef`, the v1.16 record), fast-forward, no force | remote head `ba65334…`; v1.16 read back from the remote: blob `0d7b2026f6b4`, 16,863 bytes, sha256 equal to the local file |
| 02:53:06 | reply r4320992576 (CX6-35); the thread resolved | GitHub |
| 02:53:06 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved to 03:45Z | it creates no session |
| 02:53:00 to 02:56:26 | Codex code review on `ba65334` (trigger "New commits"): review 5580246369, findings CX6-36 and CX6-37 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 02:52:54 to 03:07:33 | CI run 39361297404 on `ba65334`: success, stale | §4 |
| 03:01:02 | local commit `bb52426` | §3 |
| 03:01:33 to 03:30:57 | local validation of `bb52426`, all passed | §5 |
| after this record | push 17 of PR-35: `bb52426` and the commit adding this record, fast-forward onto `ba65334`, no force | read back in the next record |
| next | answer the CX6-36 and CX6-37 threads naming `bb52426` and resolve them; move the safety-net check-in if needed; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| The changed-tests failure on `7a3b7b2` in `test_manifest_reader_rejects_new_report_with_old_manifest` (result v1.13 §4; PR comment 6280395750) | PR-35 watches each new head's CI; the close-pack tool and test are outside this PR's change set | did not recur on `161941f`, `0783969`, `ef06f44` or `ba65334` (results v1.14 to v1.17 §4); intermittent, mechanism not established |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
| `GITHUB_OUTPUT` forms other than `NAME=VALUE`; YAML escape sequences, folding around more-indented lines, typed scalars other than `true`, `false` and decimal integers in `env` and `with`, and the other unmodelled scalar, block and key forms; an install step other than one simple command; an excluded step with another condition | stated limits; TOOLING (IF-35-15 to IF-35-18) | recorded |
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
