---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.12"
record_kind: PR-35 checkpoint for the twelfth corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.11.md (v1.11, PR-35 checkpoint; blob 0043d6495344; 18,061 bytes; sha256 aa82ea9090063199cff7de47cb1cb2346414b6073b520bde3c7994e4765fac77); v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
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
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6 and efff0bb, pushed; 98556947539d84e3e437af019546522d2c300ba8 (CX6-28; parent efff0bb); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T00:00Z
next_step: push 9855694 and this record; answer the CX6-28 thread naming 9855694 and resolve it; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---

# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.12 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `efff0bb` raised one P2 finding, CX6-28. The install substitute compared the editable project's installed version and entry points, but no other installed metadata, with the candidate's.

Under PO-35-2 it is fixed at its root in `9855694` (IF-35-14) and verified locally (§3, §5). This record rides the same push. The Codex re-review of the new head, its hosted CI, the thread resolution and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-24 | Codex reviews 5571963225 to 5578082885 | `d2ed4fc` to `2c6dd5c` | as results v1.1 to v1.10 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-25 to CX6-27 | Codex review 5578496092; P2 | `14a5858` | second workflow job; structured env value; `project = []` | fixed in `7fc63d6` (result v1.11); replies r4319794967, r4319795699 and r4319796410; threads resolved |
| CX6-28 | Codex review 5578877595 (on `efff0bb`), comment r4319823013, P2 | `efff0bb` | `tools/ci/prepush_check.py` 1539: "when a candidate changes `project.dependencies` (or another installed metadata field such as `description` or `requires-python`) while all named dependencies are already installed", the installed `Requires-Dist` metadata is never compared with the candidate's, so "a replayed lane that reads `importlib.metadata.requires()` therefore sees stale metadata while hosted `pip install -e .` regenerates it"; "compare the generated installed metadata rather than only its version and entry points" | Confirmed in the real environment at `efff0bb`. The tool reported no unmet item for six stale-metadata candidates: a dependency added, `description` changed, `requires-python` changed, a README line added, a new top-level package, and the `LICENSE` text changed. Fixed in `9855694` for every metadata file the install regenerates (§3, IF-35-14) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-3 are as results v1.7 and v1.8 §2a; no new decision was needed.

## 3. Correction CX6-28 (`9855694`)

Both paths are in plan §6.1; no path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `050d0ec22fc4`; 1,900 lines; +79/−17 on `efff0bb`) | New `_metadata_differences`. For the editable project, the build backend's own `prepare_metadata_for_build_editable` hook (`REPLAY_BUILD_SYSTEM`'s `setuptools.build_meta`) runs offline in a child process, against the candidate's tree. The process is `sys.executable -I -B`, with the closed-rails child environment, and writes under the run's temporary directory. Its `.dist-info` must equal the installed one file for file and byte for byte. The installed files pip and the wheel writer add are excluded (`REPLAY_INSTALLER_FILES`: `INSTALLER`, `RECORD`, `REQUESTED`, `WHEEL`, `direct_url.json`). Each difference names the file, and its first differing line or the missing side; a backend that fails, or writes other than one `.dist-info`, is a tooling failure. The existing version, requires-python and entry-point checks stay. The comparison runs only where the backend is importable, which is already reported otherwise. `_install_check` and `_substitute` take the scratch directory, and `report_replay` passes the run's temporary directory. The docstring states the limit: a backend release other than CI's can write metadata its own version decides differently, and the comparison then fails closed |
| `tests/tools/test_prepush_check.py` (blob `f533d6d7ff10`; 974 lines; +58/−5) | The site case's stand-in `setuptools.build_meta` now implements the hook from the candidate's name, version and dependencies, and the installed project carries an `INSTALLER` file, which is ignored. New assertions: a dependency the closure already satisfies but the installed `Requires-Dist` lacks (CX6-28's own case); an installed file the candidate does not generate (`top_level.txt`); a file differing only in line breaks; a missing `entry_points.txt`; a backend without the hook (tooling). The two version cases also report the regenerated `METADATA` line. 60 cases, unchanged in number |

## 4. CI on `efff0bb`

Run 39339904072 (job 118358580899) on `efff0bb` ran from 23:10:40Z to 23:22:55Z and completed on its own with conclusion `success`. It became stale when the re-review completed at 23:13:56Z with CX6-28. It was not waited on and is not a gate. Its result covers `efff0bb` only, whose code `9855694` changes.

## 5. Local validation of `9855694`

The environment is as result v1.1 §5: closed rails with the keys unset; a CPython 3.12.3 venv holding CI's install, pip 24.0 and setuptools 84.0.0, its `-e` pointing at the clone `cand`; `ruby` 3.3.6, `bash` and `curl`. The installed project's `.dist-info` was written by setuptools 84.0.0 (its `WHEEL` file's generator).

The clones `cand` (replay), `cand2` (short checks) and `sweep` were moved to `9855694` by fetch and checkout from the session's checkout, after `git clean -fdX`. Each then had no untracked or ignored files, and only its main worktree. One fresh clone was made per negative control. Every check that imports the repository imports the code under test, in one of four ways:
- `PYTHONPATH` set to the clone: item 1 and the negative controls;
- the replay's own `PYTHONPATH`, set to its copy: item 8;
- the working directory, which `python -m pytest` puts first on `sys.path`: item 2, in the session checkout at `9855694`, and item 9;
- the tool loaded by path: items 6 and 7.

Exit statuses are the producer's own.

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 60 passed in 45.9 s (concurrent with items 8 and 9), exit 0 |
| 2 | Pin and neighbouring files, one at a time | 138, 4, 5 and 6 passed; each exit 0 |
| 3 | Classifier `0442d23..9855694`, `pull_request` | exit 0; `reason=selected_lanes;paths=15;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: …`, exit 0; `--help` exit 0 |
| 5 | Negative controls: for each, one guard disabled in a throwaway clone at `9855694`, committed there (23:30:26Z to 23:52:17Z, two at a time) | All 44 fail as intended, each clone clean afterwards. NC-11 to NC-50 fail exactly the cases they failed at `7fc63d6` (result v1.11 §5 item 5). NC-23 is retargeted to the renamed line (`if not backend_found:`) and still fails the site case's "not importable" assertion. The four new controls: NC-51 (the metadata comparison removed) and NC-54 (the byte comparison removed) fail the site case at its first regenerated-metadata assertion, the `0.2.0+candidate` version case, which comes before CX6-28's own dependency case. NC-52 (installed-only files ignored) fails the `top_level.txt` assertion. NC-53 (pip's files not excluded) fails the first clean-site assertion, on `INSTALLER` |
| 6 | The real `ci.yml`, `pyproject.toml` and install step through the tool at `cand2` | The minimal candidate directories of the integration scripts now also hold `LICENSE` and the five top-level package directories, as a real candidate tree does. integ4 (E to M): byte-identical to result v1.11's. integ2 and integ3: identical except for the new metadata lines, each where the case changes metadata CI's install regenerates. Version `0.0.0+candidate` and `0.0` report `METADATA` line 3; `hdctl` retargeted and `pytest11` added report `entry_points.txt`; `requires-python >=3.13` reports `METADATA` line 5. integ2 case 2 now uses a synthetic site holding the real setuptools 84.0.0: `psycopg-binary` is the only unmet item, as before. `cand2` clean |
| 7 | Premises at `efff0bb` (that head's tool, scratch only), and the fix, against a fresh clone of `9855694` in the real environment | Unchanged clone: `[]` at both. Each of the six stale-metadata candidates of §2 gives `[]` at `efff0bb`. Under the fix each reports the regenerated file and line: `Requires-Dist: pytest>=1`, `Summary: Other`, `Requires-Python: >=3.11`, the README body, `top_level.txt` `engine_extra`, `licenses/LICENSE` line 1. The clone stayed clean, ignored files included, after every case. The hook's output for the unchanged clone equals the installed `.dist-info` byte for byte: `METADATA`, `entry_points.txt`, `top_level.txt` and `licenses/LICENSE` |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 23:28:19Z to 23:58:49Z (concurrent with items 1, 5 and 9); classify `reason=selected_lanes;paths=15`, all seven lanes; every one of the 16 steps SUCCESS. The install substitute (step 05, 0.4 s) passed with the metadata comparison: the hook's `.dist-info` from the replay copy equalled the installed one. Changed tests 166 targets, 3,946 passed (result v1.11's count; the owner test still has 60 cases); product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,824.9 s; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`. `cand` afterwards: `head=9855694…`, `status_lines=0`, `git_metadata_digest=c75dc602c02c84595f3e494c6d4aeb3d251fc8742cb9d53f69c52399bfb94f90`; no temporary directory left. This round took no independent before-snapshot of `cand`; the before-and-after comparison is the tool's own |
| 9 | Full `tests/` sweep (`sweep`), `-p no:cacheprovider` | **5,246 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,535.9 s (23:28:19Z to 23:53:57Z, concurrent with items 1, 5 and 8); pytest exit 0; `git diff --exit-code` exit 0, untracked status empty; an ignored `.pytest_cache/` was present afterwards, as after result v1.11's sweep. Equal to result v1.11's count, since the owner test still has 60 cases; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones. **Deviation:** `XDG_STATE_HOME` was left unset this round, not set to an empty scratch directory as plan §9 item 6 and earlier rounds have it. Its default, `~/.local/state`, did not exist after the run, so no state was read from or written there, the same effect as the empty directory. `PYTHONPATH` was also unset. In-process imports resolved to the `sweep` copy, which `python -m pytest` puts first on `sys.path`, and `hdctl` subprocesses used the editable install, mapped to `cand`, at the same commit `9855694`. So every test ran the commit under test, as the plan item requires (OBS-W5-5) |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-13 | as results v1.1 to v1.11 §6 | unchanged | as recorded there |
| IF-35-14 | CX6-28 is fixed by comparing every metadata file the editable install regenerates, generated by the build backend's own hook, rather than by modelling the fields the finding names (`Requires-Dist`, `Summary`, `Requires-Python`). Consequence: a candidate that changes the README, `LICENSE`, the top-level packages or any metadata-bearing `pyproject.toml` value gets a TOOLING failure from the replay until the caller reinstalls the editable project. That is correct, because CI's install regenerates those files. A caller whose setuptools release differs from the one that wrote the installed metadata can also get a TOOLING failure, on fields the backend's own version decides. Hosted CI is unaffected | The finding's root cause is that the substitute checked a hand-picked subset of what the install regenerates. A field model would have missed `top_level.txt` and the license files (§5 item 7's last two cases), and would have reimplemented setuptools' normalization of each field. The hook is what pip itself calls, and its output equals the installed `.dist-info` byte for byte in the measured environment. The hook writes its `.egg-info` only under the temporary directory, never in the copy or the repository (PF14 §27.4). PO-35-2; plan §5.7, §5.8, PD-8 | §5 items 1, 5 (NC-51 to NC-54), 6, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.11 §7)

| Time (UTC, 2026-10-19) | Action | Evidence |
| :- | :- | :- |
| 23:10:28 | push 11 of PR-35: `14a5858..efff0bb` (`7fc63d6`, the v1.11 record), fast-forward, no force | remote head `efff0bb…`; v1.11 read back from the remote: blob `0043d6495344`, 18,061 bytes, sha256 equal to the local file |
| 23:10:41 to 23:10:50 | replies r4319794967 (CX6-25), r4319795699 (CX6-26) and r4319796410 (CX6-27) | GitHub |
| after 23:10:50, before 23:13:21 | the three threads resolved (the tool results carry no time) | GitHub |
| 23:10:42 to 23:13:56 | Codex code review on `efff0bb` (trigger "New commits"): review 5578877595, finding CX6-28 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| 23:10:40 to 23:22:55 | CI run 39339904072 on `efff0bb`: success, stale | §4 |
| 23:27:24 | local commit `9855694` | §3 |
| 23:52:58 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` moved from 23:55Z to 01:05Z, after the round-13 push | it creates no session |
| 23:28:19 to 23:58:49 | local validation of `9855694`, all passed | §5 |
| after this record | push 12 of PR-35: `9855694` and the commit adding this record, fast-forward onto `efff0bb`, no force | read back in the next record |
| next | answer the CX6-28 thread naming `9855694` and resolve it; move the safety-net check-in after the push; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-2 | pending |
| Children are not network- or file-system-sandboxed (CX6-15) | PO-35-3; trust boundary stated in the code and `--help` (IF-35-10) | recorded |
| Scripts a step calls are not scanned for runner variables (CX6-12) | declined by PO-35-1; stated limit (IF-35-8) | recorded |
| CI's pip release (decides the ambiguous clause forms; the hosted log does not print it) | not owned here; the replay fails closed on those forms | recorded |
| The install step's isolated build environment, and the backend release CI fetches into it | stated limit; the modelled build system and configuration, the fail-closed proxy, and the metadata comparison with the caller's backend (IF-35-7, IF-35-12, IF-35-14) | recorded |
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
| Generated metadata stays out of the tree | HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §27.4 "Tracked evidence boundary and rollback" (read in full on `main`) |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-9, ID-12, §6, §7 ("Network", "Dependencies"); plan v1.0 §5.2, §5.7, §5.8, PD-8, §6.1, §13 RK-3 and RK-5, §17; contract G-3 |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
