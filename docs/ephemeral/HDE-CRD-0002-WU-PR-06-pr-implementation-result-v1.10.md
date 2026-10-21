---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.10"
record_kind: PR-35 checkpoint for the tenth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.9.md (v1.9, PR-35 checkpoint; blob cbaf9d77715f; 17,259 bytes; sha256 f42f69416607327ffb1ac2653bcbbc137b1784806e2f473252ba1b984207be76); v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de and 2c6dd5c, pushed; 3601f5494a46fd6acd44cd826aa93000075e9d61 (CX6-21 to CX6-24; parent 2c6dd5c); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-19T22:19Z
next_step: push 3601f54 and this record; answer the CX6-21 to CX6-24 threads naming 3601f54 and resolve them; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.10 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `2c6dd5c` raised four P2 findings:

- CX6-21: the runner label is not pinned.
- CX6-22: an executed step without `run:` is accepted.
- CX6-23: other editable-project metadata is unvalidated.
- CX6-24: with `TMPDIR` inside the checkout, a refusal still writes there.

Under PO-35-2 all four are fixed in `3601f54` and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-17 | Codex reviews 5571963225 to 5576889488 | `d2ed4fc` to `0f4bb07` | as results v1.1 to v1.8 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-18 to CX6-20 | Codex review 5577595526; P2 | `89e0828` | checkout condition; empty directories; non-mapping step env | fixed in `2fa03de` (result v1.9); replies r4319086245, r4319086692, r4319087103; threads resolved |
| CX6-21 | Codex review 5578082885 (on `2c6dd5c`), comment r4319131074, P2 | `2c6dd5c` | `tools/ci/prepush_check.py` 1058: any `runs-on` beginning `ubuntu-` is accepted, so `ubuntu-24.04-arm` "will replay it as x86" and nonexistent labels pass; "require the modeled `ubuntu-latest` label or validate the exact runner architecture" | Confirmed: at `2c6dd5c`, `replay_steps` accepted `runs-on: ubuntu-24.04-arm`. Fixed in `3601f54` by both: exactly `ubuntu-latest`, and an x86_64 Linux machine (§3) |
| CX6-22 | same review, comment r4319131066, P2 | `2c6dd5c` | `tools/ci/prepush_check.py` 1073: an executed step whose `run:` is removed is accepted, and `_execute` "runs an empty script and records success"; "require each executed inventory entry to contain a nonempty string `run` value" | Confirmed: at `2c6dd5c`, the citation step without its `run:` was accepted. Fixed in `3601f54` (§3) |
| CX6-23 | same review, comment r4319131056, P2 | `2c6dd5c` | `tools/ci/prepush_check.py` 1452: other PEP 621 metadata, "for example `description = 123`", is not checked, while `pip install -e .` "invokes setuptools metadata validation and fails"; "either validate the complete supported project/build configuration or fail closed on unmodeled metadata" | Confirmed: at `2c6dd5c`, the real install step with `description = 123` in the real `pyproject.toml` reported no unmet requirement. Fixed in `3601f54` (§3, IF-35-12) |
| CX6-24 | same review, comment r4319131044, P2 | `2c6dd5c` | `tools/ci/prepush_check.py` 1708: with `TMPDIR` inside the checkout, `mkdtemp` creates the directory before the containment check, and the removal changes the parent's mtime and ctime, while the tool reports only `PREPUSH_CHECK_REFUSED`; "validate the temp parent before creation or perform the read-only comparison on this refusal path" | Confirmed: at `2c6dd5c`, a run with `TMPDIR` set to an empty directory inside a synthetic repository exited 3 with that refusal and changed the directory's mtime. Fixed in `3601f54` by both (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-21 to CX6-24 (`3601f54`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `1b7dae9ecd75`; 1,823 lines; +87/−8 on `2c6dd5c`) | **CX6-21.** `runs-on` must equal `REPLAY_RUNNER` (`ubuntu-latest`). New `replay_machine()` returns why this machine cannot stand in for that x86_64 Linux runner, or None: `sys.platform` must be `linux` and `platform.machine()` `x86_64` or `amd64` (`REPLAY_MACHINES`). The replay refuses otherwise. **CX6-22.** A step without `uses:` needs a nonempty string `run:`, or it is `REPLAY_INVENTORY_DRIFT`. **CX6-23.** New `_configuration_problems` checks the editable project's whole configuration and fails closed on anything outside the model: top-level tables other than `build-system`, `project` and `tool`; a `setup.py` or `setup.cfg`; `[project]` keys outside `REPLAY_PROJECT_KEYS` (`name`, `version`, `description`, `readme`, `requires-python`, `dependencies`, `scripts`, `gui-scripts`, `entry-points`); a name that is not a PEP 508 project name; non-string version, requires-python, description or readme; a multi-line description; a readme that is not an existing `.md`, `.rst` or `.txt` file; dependencies that are not a list of strings; scripts without a `module:callable` reference; an entry-point group that is `console_scripts`, `gui_scripts` or not a table of object references; and a `[tool.setuptools]` other than `REPLAY_SETUPTOOLS_CONFIG` (the repository's own `packages.find` and `package-data`) or any `[tool.distutils]`. **CX6-24.** The temporary parent is resolved from `TMPDIR`, `TEMP`, `TMP`, then `/tmp`, `/var/tmp`, `/usr/tmp`, without tempfile's own search, which would write a probe file into a `TMPDIR` inside the repository. It is refused before anything is created when it lies inside the repository or none exists. `mkdtemp` then creates under it. The remaining post-creation check now compares the repository state and returns `EXIT_READ_ONLY_VIOLATION` if anything changed |
| `tests/tools/test_prepush_check.py` (blob `958d78bb48f7`; 877 lines; +49/−1) | Two drift cases: `runner-label` (`ubuntu-24.04-arm`) and `executed-without-run`. New `test_replay_needs_an_x86_64_linux_machine`, using monkeypatched `sys.platform` and `platform.machine`. New `test_a_temporary_directory_inside_the_repository_is_refused_before_anything_is_created`: an empty `scratch/` in a synthetic repository as `TMPDIR`; exit 3; the owner test's snapshot, directory mtimes included, unchanged; `scratch/` still empty. The site case's candidate now carries the modelled `description`, `readme` (with a `README.md`) and `[tool.setuptools]`. Refused there: `description = 123`, a multi-line description, a `license` key, a missing readme, a script without a callable, a `console_scripts` entry-point group, changed `package-data`, a `[dependency-groups]` table and a `setup.cfg`. 49 cases (45 + 4) |

## 4. CI on `2c6dd5c`

Run 39328226578 (job 118319471022) on `2c6dd5c` ran from 21:31:59Z to 21:48:23Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 21:37:35Z with CX6-21 to CX6-24. It was not waited on and is not a gate. Its result covers `2c6dd5c` only, whose code `3601f54` changes.

## 5. Local validation of `3601f54`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install and pip 24.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`.

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `3601f54` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. `PYTHONPATH` is the clone under test. Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 49 passed in 47.1 s (concurrent with items 5, 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..3601f54`, `pull_request` | exit 0; `reason=selected_lanes;paths=13;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `3601f54`, committed there | All 34 fail as intended, each clone clean afterwards. NC-11 to NC-40 fail exactly the cases they failed at `2fa03de` (result v1.9 §5 item 5). The one difference is NC-21, retargeted to the exact runner label, which now also fails `runner-label`. NC-41 (the architecture check dropped): `test_replay_needs_an_x86_64_linux_machine` fails. NC-42 (the run-command check removed): `executed-without-run` fails. NC-43 (configuration problems ignored): the site case fails. NC-44 (the temporary parent's containment check dropped): the `TMPDIR`-inside case fails |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` | Result v1.9 §5 item 6's cases give output byte-identical to that round's. The scratch scripts now copy `README.md` into their candidates as the new readme check requires; without it every edited-candidate case was refused, correctly. New cases: (E) `runs-on: ubuntu-24.04-arm`: `REPLAY_INVENTORY_DRIFT: runs-on 'ubuntu-24.04-arm' is not the modelled 'ubuntu-latest'`. (F) the citation step without `run:`: `… has neither uses: nor a run: command`. (G) `replay_machine()` here: None. (H) the real `pyproject.toml`: no unmet requirement. Refused as configuration the replay does not model: (I) `description = 123`, (J) a `license` key, (K) changed `package-data`, (L) a missing readme and (M) a `setup.cfg` |
| 7 | Premises at `2c6dd5c` (that head's tool, scratch only) | CX6-21: `ubuntu-24.04-arm` accepted. CX6-22: the citation step without `run:` accepted. CX6-23: `description = 123` gave no unmet requirement. CX6-24: `TMPDIR` inside a synthetic repository: exit 3, and the directory's mtime changed |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 21:46:11Z to 22:19:03Z (concurrent with item 9); classify `reason=selected_lanes;paths=13`, all seven lanes; every one of the 16 steps SUCCESS, the real `pyproject.toml` passing the configuration check at step 05; changed tests 166 targets, 3,935 passed (result v1.9's 3,931 plus the four new cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488 (OBS-17 did not occur); release 79 and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,965.2 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` before and after: `head=3601f54…`, `status_lines=0`, `git_metadata_digest=84fe67797db8d8eedd2ea30bbb999c1254de4f06ee095c7e2abc8bb2f2f2d291`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory | **5,235 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,614.3 s (21:46:11Z to 22:13:13Z, concurrent with item 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`. Result v1.9's 5,231 plus the four new owner-test cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-11 | as results v1.1 to v1.9 §6 | unchanged | as recorded there |
| IF-35-12 | The editable project's whole configuration is modelled, closed-world (CX6-23's first option made total): the tables, the `[project]` keys and their value shapes, the readme file, `[tool.setuptools]` exactly as the repository has it, and no `setup.py`, `setup.cfg` or `[tool.distutils]`. Consequence: a PR that changes `[tool.setuptools]` or adds a `[project]` key outside the model gets a TOOLING failure from the replay until `REPLAY_SETUPTOOLS_CONFIG` or `REPLAY_PROJECT_KEYS` is updated. This is the same rule as `REPLAY_BUILD_SYSTEM` (IF-35-7) and contract G-3's for steps. Hosted CI is unaffected | setuptools validates all of this configuration during CI's `pip install -e .`, and validating it in full offline would mean reimplementing setuptools' schema. The model covers exactly what the repository uses, and anything else fails closed (PO-35-2; plan PD-8) | §5 items 1, 5 (NC-43), 6 (H to M), 7 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.9 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 21:31:51 | push 9 of PR-35: `89e0828..2c6dd5c` (`2fa03de`, the v1.9 record), fast-forward, no force | remote head `2c6dd5c…`; v1.9 read back from the remote: blob `cbaf9d77715f`, 17,259 bytes, sha256 equal to the local file |
| 21:32:02 to 21:32:08 | replies r4319086245 (CX6-18), r4319086692 (CX6-19) and r4319087103 (CX6-20); the three threads resolved | GitHub |
| 21:32:11 to 21:37:35 | Codex code review on `2c6dd5c` (trigger "New commits"): review 5578082885, findings CX6-21 to CX6-24 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 21:31:59 to 21:48:23 | CI run 39328226578 on `2c6dd5c`: success, stale | §4 |
| 21:32:11 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` re-armed for 22:25Z after push 9 | it creates no session |
| 21:44:30 | local commit `3601f54` | §3 |
| 21:44:58 | the check-in moved from 22:25Z to 23:15Z, after the round-11 push | it creates no session |
| 21:46:11 to 22:19:03 | local validation of `3601f54`, all passed | §5 |
| after this record | push 10 of PR-35: `3601f54` and the commit adding this record, fast-forward onto `2c6dd5c`, no force | read back in the next record |
| next | answer the CX6-21 to CX6-24 threads naming `3601f54` and resolve them; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment | stated limit; the modelled build system and configuration plus the fail-closed proxy (IF-35-7, IF-35-12) | recorded |
| O-6 (hosted `ruby` version unprinted) | as plan §16 | stands |
| WU-DOC-01 usage note: as result v1.8 §8, plus that the replay needs an x86_64 Linux machine and refuses a `TMPDIR` inside the repository. OBS-P4-1, OBS-P3-5; every other carried item | as result v1.0 §8 | unchanged |
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
