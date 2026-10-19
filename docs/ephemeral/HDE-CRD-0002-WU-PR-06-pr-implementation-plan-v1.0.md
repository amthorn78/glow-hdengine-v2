---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 1 (first plan for this work unit)
predecessor: none
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0-prototype.diff (the prototype's diff from 1993d07 for the three paths of §6.1; §4.4)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; 82,556 bytes; landed by amthorn78/glow-hdengine-v2#658 at 1993d07)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2; no note for this unit)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — §3, §5.2, §5.3, §6 S20, §7.1 EC-9 and §7.5 bind this unit
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10). None is rewritten
applicable_pf10_overlays: PF10 addendum 2.2 (WU-PR-06's sweep environment must provide ruby; the coverage definition contracted to WU-PR-06 is unchanged); 2.3 (reviewer chain without the Codex security review); 2.4 (WU-PR-01 accepted; contracts C-1 to C-6; observations O-1 to O-6); 2.5 (OBS-17 as a qa-lane risk; a record commit still selects lanes because the classifier compares base to head); 2.9 (OBS-P4-1 to WU-PR-06 or a later classifier unit); 2.10 (WU-PR-05 accepted; the list "Carried into the WU-PR-06 instruction"). 2.6 to 2.8 have no item for this unit (no release member changes). 2.1 governs §19
effective_baseline: approved base + applicable PF10 overlays = the base above + addenda 2.2, 2.3, 2.4, 2.5, 2.9 and 2.10, as instruction v1.0 applies them
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; 208,266 bytes; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e). Resolved afresh on main at 1993d07: the unique controlled PF10; unchanged since 5e62a65 (git diff 5e62a65 1993d07 adds only the instruction)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md §2.2, §2.3, §2.4, §2.5, §2.9, §2.10; §2.1 for §19
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the dedicated HDE-CRD-0002 WU-PR-06 PR engineering session, created by Nathan / Product Owner)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_01NZEtMVb5HR3XYEmJ6W5cb6
author: dedicated HDE-CRD-0002 WU-PR-06 PR engineering session (PR-20)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the merge; RS-20 for any rescope; PR-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-19T03:08:15Z
repository_baseline: origin/main 1993d077a659ea8bbbafeb7a9393ebd0345ed8cd (#658). git diff 5e62a65 1993d07 adds only the instruction under docs/ephemeral/, so every byte outside docs/ephemeral/ equals 5e62a65, the instruction's measured baseline, and 822ce15 outside docs/ephemeral/ and docs/pfcanon/
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§15)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-06 — Detailed PR Implementation Plan v1.0

## 1. State and authority

**AWAITING_PO_PROCEED.** This is the one complete detailed plan for work unit WU-PR-06 (requirement S20), executable within the approved scope. It is held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.1.1). Nathan's invocation of PR-30 — PR Implementation Proceed — 100926.1 for this exact plan, v1.0, is the approval and the only authorization to implement.

This plan does not:
- authorize implementation, a commit outside `docs/ephemeral/`, a pull request for the code, a merge, Ops, QA, acceptance or closure;
- decide a canon, product or scope question, or change canon, or create a PF10 addendum;
- make the tool's output evidence. "The tool's green is not CI's green and not QA" (Plan v1.1 §7).

Its only writes are this plan and its companion diff, under `docs/ephemeral/`, on the session's working branch and pull request. The prototype ran in throwaway clones under the session's scratch directory; nothing of it was pushed except the companion diff as a record.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-06, "Read-only pre-push and pre-plan check (PR; Distillation)" (Plan v1.1 §7) |
| Requirement | S20 (source item 7); constraints "Duplication" and "Uncovered tests"; Exclusions "No SessionStart hook (item 7)" and the others instruction §4 quotes |
| Interface and loci | IF-9 (Plan v1.1 §5); EC-9 (Audit §7.1) |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0 (front matter) |
| Overlays | PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10 (front matter) |
| Dependency state | Ready: WU-PR-01 accepted (addendum 2.4), WU-PR-05 accepted (addendum 2.10); no `HDE-CRD-0002-WU-PR-06-*` file existed on `main` other than the instruction (checked at `1993d07`) |
| Merge order | WU-PR-05 → **WU-PR-06** → WU-PR-07 (Plan v1.1 §7). WU-PR-07 may be prepared in parallel but merges after this unit |
| Live QA class | Not production-affecting ("read-only repository tooling"; Specification table; Plan §6) |

## 3. Sources read

All read in full in this session unless a section is named.

- **Prompt:** PR-20 — Create Detailed PR Implementation Plan — 100926.1 (above). Receiver contract: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08.672Z; read in full).
- **Instruction:** `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md`, all 20 sections and "Canon relied on".
- **In-flight documents (sections):** Specification v1.1 row S20, constraints "Duplication" and "Uncovered tests", the Distillation phase row and the Live QA table; Plan v1.1 §5 IF-9, §6, §7 (common paragraph and the WU-PR-06 block); Audit §6 S20 and §7.1 EC-9 (and §3, §5.2, §5.3 as the instruction restates them); WU-PR-01 instruction v1.0 §5.1 (the binding coverage definition and the 135-file list); WU-PR-05 plan v1.0 (structure precedent).
- **PF10** `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md`: addenda 2.1 to 2.5 and 2.10 in full; 2.9's observation table and carried list; the index.
- **Canon** (the governing sections the instruction's C1 to C7 name, re-read on `main` at `1993d07`; see "Canon relied on").
- **Repository:** `.github/workflows/ci.yml` (all 420 lines); `ci/checks/classify_ci_changes.py` (constants, `_lanes_for_path`, `changed_test_targets`, the owner-target functions, `classify_paths`, `classify_git_change`, `main`); `tests/evidence/test_rails_ci_workflow_integration.py` (the workflow, full-validation and coverage-guard tests); `engine/config/registry_loader.py` (the admission constants); `pytest.ini`; `requirements*.txt`; `pyproject.toml`.

## 4. Repository baseline (verified at `1993d07`)

Environment for every measurement: CPython 3.12.3 in a scratch venv with CI's install (`pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, editable install mapped to a scratch clone at `1993d07`); pytest 8.4.2; `ruby` 3.3.6 at `/usr/local/bin/ruby`; `bash`, `curl`; git 2.43.0; closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` with `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HD_GEOCODE_KEY`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `GH_TOKEN`, `GITHUB_TOKEN`, `ENGINE_ENV` unset (the container sets several of them). The container's default `python3` is 3.13; the venv uses `/usr/bin/python3.12`. Work ran in scratch clones; the session's checkout was only read.

### 4.1 Instruction facts re-verified (§9.3)

| Fact (instruction §) | At `1993d07` |
| :- | :- |
| Only docs changed since the measured baseline (§5.1) | `git diff --name-only 5e62a65 1993d07` lists only the instruction |
| `ci.yml` (§5.2) | 420 lines, blob `3836bad11c39`, SHA-256 `d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b`: unchanged. Sixteen steps of job `test`, names, ids and conditions as the §5.2 table; job `env:` the seven pins |
| Token sets (§5.2, §5.4) | 39 `tests/` tokens in `python -m pytest` commands and 39 anywhere (the guard's regex); equal |
| Classifier (§5.3) | 2,057 lines, blob `e43181370783`: unchanged. `tools/ci/prepush_check.py` refused `CI_CHANGE_SURFACE_UNCLASSIFIED`; `VERIFY.sh` → `product` only, no target (OBS-P3-5 holds) |
| Coverage (§5.4) | 214 tracked `tests/**/test_*.py`; 165 full-validation targets; uncovered set 0 by the binding definition and by the guard's set |
| Admission (§5.5) | `ADMITTED_RELEASE_VERSION` `1.3.0`; 45 roster paths; `catalog/manifest.json` SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` |
| Build Notes (§5.5) | exactly one match, `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md`, SHA-256 `ca2d91c5…e3e` |
| Reproduction target (§5.4) | at `a429c7c`: 278 tracked, 39 tokens, 94 targets, **135 uncovered**, file for file equal to WU-PR-01 instruction §5.1 (its nested `tests/provider/tests/provider/test_decisions_perms_and_newline.py` included) |
| Hidden-write hazards (§5.7) | confirmed and handled by design (§5.2 below) |

No difference in step names, token sets or the uncovered set: nothing to handle before planning edits.

### 4.2 Facts this session established (not in the instruction)

- **F-1. `_validated_owner_targets` refuses a registered owner whose file is missing.** In the prototype, with the registration added but the owner test not yet written, `lanes --path tools/ci/prepush_check.py` gave `CI_CHANGE_CLASSIFIER_ERROR:CI_TOOL_OWNER_TEST_INVALID:tools/ci/prepush_check.py:tests/tools/test_prepush_check.py`, and the CLI on base..head gave `CI_FULL_VALIDATION_TEST_INVALID:ci/checks/classify_ci_changes.py:tests/tools/test_prepush_check.py`. The registration and the owner test must land in the same commit (§7 step 4).
- **F-2. `pytest.ini` `testpaths` does not contain `tests/tools`.** So `test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`'s `configured == fixed | supplemental | inactive` is not affected by the new test, and `pytest.ini` stays unchanged.
- **F-3. `git clone --shared` from a shallow source falls back to an ordinary clone** (no `objects/info/alternates`), which carries only ref-reachable history. The source is still only read: the source clone's git metadata digest (every non-object file under `.git`) was identical before and after. In CI (`fetch-depth: 0`) and in any full clone, `--shared` uses alternates and every commit is reachable. In a shallow checkout a commit that is on no ref is unavailable to the copy; the tool then fails that report as tooling with "commit … is not available to the throwaway copy" (§5.2).
- **F-4. pytest stops at the first collection error** unless `--continue-on-collection-errors` is given; without it the sweep could not report each file's outcome (§5.6).
- **F-5. GitHub's runner shells.** A step without `shell:` runs under `bash -e {0}`; `shell: bash` runs under `bash --noprofile --norc -eo pipefail {0}`. Steps 5, 6 and 7 of `ci.yml` have no `shell:`. The replay reproduces both forms (§5.7).
- **F-6. No test or tool reads `CI`, `GITHUB_ACTIONS`, `RUNNER_TEMP` or `GITHUB_OUTPUT`** except the classifier's own argument defaults (`git grep` over `tests`, `tools`, `ci`, `scripts`, `engine`, `adapter`).

### 4.3 Prototype (this session; scratch only)

A scratch clone of `1993d07`, with the three files of §6.1 committed there as eight scratch commits (`1c2c728` tool and registration; `08b8377` owner test; `6037b60`, `0cf9c3b`, `0ff958a`, `2e85548` test refinements; `57b894e` and `003c5f3` the report-exception handler and its test, §4.3.5). The final prototype head is `003c5f3695f8927d62a02edd5072fd5f30ea9b82` (tree `3d2e3b1338bd`).

Which head each long run used:
- the replay of §4.3.6 ran on `0ff958a`; the full sweep of §4.3.7 ran on `2e85548`;
- `git diff 0ff958a 003c5f3` is 3 added lines in the tool (the handler in `main`) and 16 insertions, 5 deletions in the owner test; `git diff 2e85548 003c5f3` is the same 3 tool lines and 9 test lines; the registration is byte-identical throughout;
- so neither long run's verdict depends on the later lines except through the owner test, which was re-run in full at `003c5f3` (§4.3.1). PR-30 repeats both long runs at its own commit (§9).

#### 4.3.1 Owner test

`python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` at the final head `003c5f3`, in a detached worktree with `PYTHONPATH` the worktree: **21 passed in 24.5 s**. At `2e85548` (before the last case): 20 passed in 31.9 s; slowest cases the lanes-equality test 18.8 s (three throwaway clones, nine tool runs), the repository-clone reports test 6.3 s plus 3.4 s clone setup, the synthetic sweep 1.3 s. The replay's step 8 also ran the file inside a linked worktree of the copy (§4.3.6), as CI's changed-test step does. Every run left the clone's status empty.

#### 4.3.2 Pins and neighbours

In a detached worktree of the final head `003c5f3` with `PYTHONPATH` the worktree, one file at a time: `tests/evidence/test_rails_ci_workflow_integration.py` **138 passed** (the baseline's count, instruction §5.8 step 12); `tests/evidence/test_http_reader_ci_ownership.py` **4 passed**; `tests/evidence/test_architecture_snapshot.py` **5 passed** (the new `tools/ci/` module does not touch the architecture snapshot); `tests/tools/test_epic020_bundle_tool.py` **6 passed**. Also there: `python3 ci/checks/check_agents_md_citations.py` `AGENTS_MD_CITATIONS_OK`; `ci/checks/check_env_pins.sh` `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC`; the classifier dry run `--base 1993d077… --head 003c5f36… --event-name pull_request`: exit 0, `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`, `changed_tests=true`, 166 targets including `tests/tools/test_prepush_check.py`. `git diff --exit-code` and the untracked status empty afterwards. (Earlier, at `0ff958a`, the four files together: 153 passed.)

#### 4.3.3 Each report, run once (captured; exit statuses from the producer's own status)

The single-report runs used `1c2c728` (the tool and registration commit; the owner test was then not yet written), the replay `0ff958a`.

| Run | Exit | Duration | Result |
| :- | -: | -: | :- |
| `build-notes` | 0 | 0.0 s | `path=docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md bytes=208266 sha256=ca2d91c5…e3e` |
| `membership --path engine/core/core.py --path tools/ci/prepush_check.py --path VERIFY.sh` | 0 | 0.0 s | `admitted release version=1.3.0 roster=45 release_id=77204764…`; `member engine/core/core.py`; `not-member` for the other two; the refresh note |
| `membership … --path ../x` | 1 | 0.0 s | `FAILURE invalid path '../x': changed path is not repository-relative` (the classifier's `_normalized_path`) |
| `lanes --path docs/ephemeral/x.md` | 0 | 0.0 s | `reason=documentation_only;paths=1;lanes=none`, all eleven output keys, 0 targets, the path-filter note |
| `lanes --path … tools/ci/prepush_check.py …` before the owner test existed | 1 | 0.0 s | `CI_CHANGE_CLASSIFIER_ERROR:CI_TOOL_OWNER_TEST_INVALID:…` (F-1) |
| `sweep` at `1c2c728` | 0 | 2.4 s | `tracked_test_files=214 pytest_command_tokens=39 workflow_tests_tokens=39 full_validation_targets=166 uncovered=0` |
| `sweep --head a429c7c --no-run` | 1 | 3.2 s | `tracked_test_files=278 … full_validation_targets=94 uncovered=135`; the 135 lines equal WU-PR-01 instruction §5.1 file for file |
| `replay --base 1993d07` at `0ff958a` | 0 | 1,240 s wall (1,234.5 s step time) | §4.3.6 |

Every run ended with `PREPUSH_CHECK_RESULT: … repository unchanged (tree, HEAD and git metadata)` and the nonclaim line, and the prototype clone's status stayed empty.

#### 4.3.4 Negative controls (one guard disabled each; each failed as intended)

NC-1 to NC-9 ran in fresh throwaway clones of `0ff958a`, the change committed there; NC-6's re-run ran at `2e85548` and NC-10 at `003c5f3`, each in a working copy restored afterwards (status empty).

| ID | Guard disabled | Result |
| :- | :- | :- |
| NC-1 | read-only rule: `build-notes` also writes an ignored file `tests/__pycache__/nc.pyc` | 2 failed (`test_reports_on_a_clone_of_the_repository_are_read_only`, `test_build_notes_requires_exactly_one_file[names1-True]`): the test's snapshot sees ignored files; the tool's own check (status, HEAD, git metadata) does not, by design |
| NC-2 | read-only rule: `build-notes` rewrites tracked `README.md` | the tool's own post-check: `PREPUSH_CHECK_READ_ONLY_VIOLATION`, **exit 4**; the test case fails |
| NC-3 | inventory pin: a step of `ci.yml` renamed | `test_replay_inventory_pins_every_step_of_the_ci_test_job` fails |
| NC-4 | inventory pin: one entry removed from the tool's `REPLAY_INVENTORY` | the pin test and both synthetic replays fail (3 failed) |
| NC-5 | dirty-tree refusal disabled | all three `test_dirty_tree_is_refused_before_any_report` cases fail |
| NC-6 | `HD_API_KEY` removed from the tool's key list | `test_child_environment_is_closed_rails_without_keys` and both synthetic replays fail (3 failed; the replays fail at the step that asserts every key is absent). A first version of this control passed the replays, because the test then derived its dummy keys from the tool's own list; the test now states the keys independently (prototype `2e85548`) |
| NC-7 | coverage definition replaced by the guard's wider token set | `test_sweep_flags_runs_and_classifies_a_synthetic_uncovered_set` fails |
| NC-8 | the classifier's `_ci_tool_owner_targets` call removed | `test_lanes_equals_the_classifier_for_refs_and_for_given_paths` fails (the tool change selects no owner) |
| NC-9 | `_CI_TOOL_TEST_OWNERS` removed from `_registered_owner_test_paths` | the owner test's coverage case and the existing guard `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target` fail |
| NC-10 | the report-exception handler in `main` removed (at `003c5f3`, working copy restored afterwards) | `test_a_report_without_its_inputs_is_a_tooling_failure` fails (the run ends in a traceback without the read-only check) |

#### 4.3.5 Prototype corrections made during the prototype (all inside the three files)

- The lanes-equality fixture pins its throwaway commits to branches of its own throwaway clone (F-3).
- The read-only snapshot compares `lstat` (mode, inode, size, `mtime_ns`, `ctime_ns`) of every entry plus content hashes of git metadata, instead of hashing every file (53 s → 32 s for the file; §5.10).
- The test's child-key list is independent of the tool's (NC-6).
- A self-review found that an `OSError`, `UnicodeError`, `ValueError`, `KeyError` or `subprocess.SubprocessError` raised inside a report would end the run with a traceback and skip the post-run read-only check. `main` now records it as that report's `TOOLING_FAILURE`, and a test case covers it (NC-10).

#### 4.3.6 Replay (`replay --base 1993d07`, event `pull_request`, head `0ff958a`)

| # | Step | Outcome | Seconds | Last lines |
| -: | :- | :- | -: | :- |
| — | (before the steps) | | | `job env LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`; `resolves hdctl (<venv>/bin/hdctl) -> engine.cli.main: <copy>/engine/cli/main.py` |
| 1 | Check out exact candidate head | SUCCESS, excluded, substituted | 0.0 | copy at `0ff958a…` |
| 2 | Classify affected CI lanes | SUCCESS | 0.1 | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release` |
| 3 | Check AGENTS.md cites no project documents | SUCCESS | 0.1 | `AGENTS_MD_CITATIONS_OK` |
| 4 | Set up Python 3.12 | SUCCESS, excluded, substituted | 0.0 | the caller's interpreter, 3.12 |
| 5 | Install applicable validation dependencies | SUCCESS, excluded, substituted | 0.0 | every named distribution installed |
| 6 | Verify pytest readiness | SUCCESS | 0.3 | `pytest 8.4.2` |
| 7 | Verify closed deterministic environment | SUCCESS | 0.1 | `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` |
| 8 | Run affected behavioral tests in isolation | SUCCESS | 425.3 | 166 targets: `3906 passed` (instruction §5.8: 165 targets, 3,886; the difference is the new file's 20 cases) |
| 9 | Run product mechanics and ordering lane | SUCCESS | 22.6 | `77 passed` |
| 10 | Run CLI and compatibility lane | SUCCESS | 9.5 | `119 passed, 3 skipped, 2 xfailed` |
| 11 | Run database and runtime-contract lane | SUCCESS | 10.2 | `269 passed, 5 warnings` |
| 12 | Run rails policy and secret-safety lane | SUCCESS | 38.2 | last pytest `138 passed` |
| 13 | Run governed evidence integrity lane | SUCCESS | 503.8 | `130 passed` |
| 14 | Run approved generic QA subsystem lane in isolation | SUCCESS | 22.9 | `488 passed` (OBS-17 did not occur) |
| 15 | Build and verify exact-source release attestation | SUCCESS | 201.3 | `79 passed`; the attestation built into and verified from `<tmp>/replay-runner-temp/hde-release-attestation/` |
| 16 | Verify truthful applicability and clean candidate tree | SUCCESS | 0.1 | `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

- Run 02:42:19Z to 03:02:59Z, concurrent with the sweep of §4.3.7 from 02:47:20Z; exit 0; 1,240 s wall, 1,234.5 s step time; `status=PASS`; `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, HEAD and git metadata)`.
- The tool ran with dummy values set for `HD_API_KEY`, `DATABASE_URL` and `GH_TOKEN`; step 7 passed and no value was printed.
- Afterwards: "copy after replay: clean"; the prototype clone's git-metadata digest (every non-object file under `.git`, by content) was equal before and after, and its status was empty.
- Equal to the counts of instruction §5.8 and the hosted reference §5.9 lane by lane (product 77, compat 119/3/2, db 269, rails 138, evidence 130, qa 488, release 79).

#### 4.3.7 Full `tests/` sweep at the final prototype head `2e85548`

- **Command:** `python -m pytest -q -p no:cacheprovider tests/` in a detached worktree of a scratch clone at `2e85548`, `PYTHONPATH` the worktree (so `hdctl` subprocesses ran the code under test; OBS-W5-5), `XDG_STATE_HOME` an empty scratch directory, closed rails, `ruby`, `bash` and `curl` on `PATH`.
- **Result:** **5,206 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, in 986.6 s (02:47:20Z to 03:03:48Z, concurrent with the replay); pytest exit 0 (`PIPESTATUS`, the producer's own status).
- **Afterwards:** `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`.
- **Comparison:** instruction §5.10 at `5e62a65` gave 5,186 passed; the difference is exactly the owner test's 20 cases at `2e85548`. The skips, xfails and the `datetime.utcnow()` warnings are the pre-existing ones.

### 4.4 Prototype diff (companion file)

`docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0-prototype.diff` is `git diff 1993d07 003c5f3` of the scratch clone: exactly the three paths of §6.1 (+1,810 lines, no deletion; 89,883 bytes; SHA-256 `2f26f680275bfef9e6fcc6feee59067d45ae66a3e53edef3bbfb5285f28728cc`). Checked: `git apply --index` of the file onto a fresh clone at `1993d07` gives the three blobs below.

| Path | Blob at `003c5f3` | SHA-256 | Lines |
| :- | :- | :- | -: |
| `tools/ci/prepush_check.py` (new) | `34956510e470` | `d7d5acc37584ecbaeb3824eefdac49dd0a31884d1ea994f640b287250c37608f` | 1,229 |
| `tests/tools/test_prepush_check.py` (new) | `9b87df4c7c2c` | `07baca0b5e88a6e451d21afda6e744ab115fdd224923d131275276749295416b` | 552 |
| `ci/checks/classify_ci_changes.py` (+29) | `10a7155f3df2` | `12c897fa1dcc3115ba34901b3074efdfd6a96babf824135ceac0fe018d0a32f2` | 2,086 |

PR-30 applies it with `git apply --index` on a branch from the then-current `main`, and verifies the three blob identities above. The diff is the design of record. PR-30 may change it only as an in-flight decision (§13 and instruction ID-12).

## 5. Design (instruction §9.1 choices, each with its reason)

### 5.1 Command, arguments, output and exit codes (ID-1)

- **Command.** `python tools/ci/prepush_check.py REPORT [REPORT ...] [options]`, with `REPORT` one or more of `lanes`, `membership`, `build-notes`, `sweep`, `replay`, or `all`. Reports always run in that order, whatever order is given. *Reason:* one invocation gives a session its whole pre-push picture, and a fixed order makes captured runs comparable.
- **Options.** `--base REF` (default `origin/main`) and `--head REF` (default `HEAD`) for `lanes` and `replay` (`--head` also for `sweep`); `--event {pull_request,push}` (default `pull_request`, as CI on a pull request); `--path PATH`, repeatable, for `lanes` (given-paths mode) and `membership`; `--full` (base set to head: the classifier's own full validation, for `lanes` and `replay`); `--no-run` (`sweep` lists the set without running it). A hidden `--repo-root` (default: the checkout that holds the tool) exists for the owner test's throwaway repositories. *Reason:* the smallest set that expresses IF-9's inputs; `--full` and `--no-run` serve ID-8 and ID-7 below.
- **Output.** Plain text on stdout. A header `PREPUSH_CHECK: repo=… head=… python=… reports=…`; each report's lines prefixed `<report>: `, naming its resolved inputs (full SHAs, the refs they came from, the copy path) and ending `status=PASS|FAIL duration=…s`; a failure line starts `FAILURE` or `TOOLING_FAILURE` (C3); a final `PREPUSH_CHECK_RESULT: PASS|FAIL lanes=… …; repository unchanged (tree, HEAD and git metadata)` and `PREPUSH_CHECK_NONCLAIM: this result is not CI's result, not QA and not governed evidence`. No environment value is printed except the rails and determinism pins and `APP_ENV`.
- **Exit codes.** 0 only when every requested report passes (IF-9); 1 when any report fails; 2 a usage error (argparse); 3 refused before any report (not a git working tree, not its top level, a dirty tree, a temporary directory that would fall inside the repository); 4 the repository's tree, HEAD or git metadata changed (`PREPUSH_CHECK_READ_ONLY_VIOLATION`). An unexpected `OSError`, `UnicodeError`, `ValueError`, `KeyError` or subprocess error inside a report is that report's `TOOLING_FAILURE`, so the post-run check always runs. *Reason:* a session can tell "something to fix in my change" (1) from "the tool could not judge" (3) and from "the tool broke its own rule" (4).
- **Not evidence.** The output goes to the terminal only. Nothing is written to `docs/evidence/`, `artifacts/` or `audit/` (C6).

### 5.2 Writing nothing to the repository (ID-2, ID-3)

- **One temporary directory.** `tempfile.mkdtemp(prefix="prepush-check-")` (owner-only, mode 0700), refused if it resolves inside the repository, removed in a `finally` at exit, also when a report fails.
- **The copy mechanism.** `git clone --quiet --shared --no-checkout -- <repo> <tmp>/<report>-copy`, then `git -c advice.detachedHead=false checkout --quiet --detach <sha>` inside the copy, then a check that the copy's `HEAD` equals the SHA. *Why it writes nothing to the repository:* a clone only reads the source's refs and objects; with `--shared` the copy records an alternate to the source's object directory and writes its own objects, index, refs and worktree registry under its own `.git`; no command runs with the source as its working directory except reads. The steps' own `git worktree add` therefore registers in the copy, not in the source (instruction §5.8 observed the same with this mechanism). A registered `git worktree` of the source would write `.git/worktrees/` and is never used. F-3 records the shallow-source fallback.
- **The three hazards of instruction §5.7.**
  - *Bytecode.* The tool's first statement after `import sys` is `sys.dont_write_bytecode = True`; repository modules (the classifier) are loaded by file path under that flag; every Python child gets `-B` or `PYTHONDONTWRITEBYTECODE=1` (the job env). The release roster is read with `ast`, not imported.
  - *`git status` index rewrite.* Every git command against the source runs with `GIT_OPTIONAL_LOCKS=0` (and `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` removed); the tree check is `git status --porcelain=v1 -z --untracked-files=all` under that variable.
  - *Worktree registration.* Never against the source (above).
- **The tool's own assertion.** Before any report: the tree is clean (untracked files included; a dirty tree is refused, exit 3, before any report runs) and the state is recorded: `HEAD`, the porcelain status, and a digest of the git metadata (every file under the git dir and the common dir by content, plus names and sizes under `objects/`). After the reports: the same three must be equal, or exit 4. Ignored files are outside the tool's own check (a session's `.venv/` may be large); the owner test covers them (§5.10).
- **Committed state, local refs.** Reports read committed revisions: `build-notes` lists `HEAD`'s tree; `membership` and given-path `lanes` read the checkout, which the clean-tree check makes equal to `HEAD`; `sweep`, `replay` and `lanes` for a head other than `HEAD` use a copy at that head. Refs resolve with `git rev-parse --verify --quiet --end-of-options <ref>^{commit}`; no `git fetch`. The report prints the ref and the SHA it resolved; a missing `origin/main` is a tooling failure that names `--base`.

### 5.3 `lanes` (ID-4)

- **Base and head.** Runs the classifier's own CLI, `python -B ci/checks/classify_ci_changes.py --base <sha> --head <sha> --event-name <event> --repo-root <root> --github-output <tmp> --changed-tests-output <tmp>`, from the checkout when head is the checkout's `HEAD` and otherwise from a copy at head (the head's own classifier, as CI runs it). It prints the CLI's `CI_CHANGE_CLASSIFICATION:` line, every `--github-output` line as `output key=value`, and every target as `target path`. A non-zero exit prints `FAILURE classifier exit <n>: <stderr verbatim>`. *Reason:* delegation by execution re-implements nothing, and equality with the classifier holds by construction; the test proves it.
- **Given paths.** Loads the checkout's classifier by path and computes `classify_paths(paths, governed_paths=_load_governed_primary_paths(root))`, then `result.test_targets or changed_test_targets(root, paths)`, exactly as `classify_git_change` combines them, and writes them with the classifier's own `write_github_output` and `write_changed_test_targets` into the temporary directory, then prints them. A refusal prints `FAILURE CI_CHANGE_CLASSIFIER_ERROR:<exception text>`, the CLI's format. The report notes that targets are computed against the head's files, so a planned file selects no target of its own.
- **Notes.** For `pull_request`, that the classifier compares the merge base with head; for `reason=documentation_only`, that the workflow's path filter starts no hosted run (pinned by the existing path-filter test; no logic of its own).

### 5.4 `membership` (ID-5)

Validates each path with the classifier's `_normalized_path`; reads `ADMITTED_RELEASE_VERSION` and `ADMITTED_RELEASE_ROSTER` from `engine/config/registry_loader.py` with `ast` (the roster is `tuple(sorted({…}))`; any other shape is a tooling failure); prints the version, the roster size and the `release_id` (SHA-256 of `catalog/manifest.json`'s bytes), then `member` or `not-member` per path, and, when a member is named, the information-only note that a member change needs a same-version manifest refresh with convergence. It runs no admission call and no owner tool. Without `--path` the report fails.

### 5.5 `build-notes` (ID-6)

Lists `git ls-tree -r -z --name-only HEAD -- docs/pfcanon/`, keeps names matching `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` directly in that directory, and requires exactly one. It prints the path, the byte count and the SHA-256 of the file's bytes. Zero or several matches fail, naming what was found; there is no fallback.

### 5.6 `sweep` (ID-7)

- **Set.** In a copy at head, a separate process (`python -B -c …`, loading this tool by path) computes, from the copy's own files: tracked `tests/**/test_*.py` by `git ls-files`; the `tests/` tokens of `python -m pytest` commands in every step's `run:` text of the copy's `ci.yml` (line continuations joined, `shlex` split); `_full_validation_test_targets()` of the copy's classifier; uncovered = tracked files not equal to or under any of them. It also reports the guard's wider token set (every `tests/` token anywhere) for comparison. *Reason:* the separate process keeps another revision's classifier out of the tool's process (ID-7), and the same code path serves the head and the reproduction.
- **Reproduction (the choice ID-7 leaves).** `sweep --head <rev>` accepts any local commit. The 135-file reproduction is `sweep --head a429c7c --no-run`: the set is computed from `a429c7c`'s own `ci.yml` and classifier and is not run, because running old tests under today's environment says nothing about the head. Observed: 135, file for file (§4.1).
- **Run.** When the set is not empty and `--no-run` is absent: `python -m pytest -q -p no:cacheprovider --continue-on-collection-errors -o junit_family=xunit1 --junitxml=<tmp>/sweep-junit.xml -- <files>` in the copy, with the child environment of §5.8 and `PYTHONPATH` the copy. The two added options only make per-file outcomes possible (F-4) and write only into the temporary directory. A missing `bash`, `curl` or `ruby` is reported first as a tooling failure (addendum 2.2). Per file: `PASS`, `BEHAVIOR` (a failure or an error during a test), or `TOOLING` (a collection or import error, or no test collected). Then the copy's `git diff --exit-code` and untracked status, so a file that rewrites tracked files is shown (O-11).
- **Status.** Passes only when the set is empty; a non-empty set fails whatever the run gives.

### 5.7 `replay` (ID-8)

- **Parser.** A standard-library reader of the YAML subset `ci.yml` uses: block mappings and sequences by indentation, plain and quoted scalars, `|`, `|-`, `>` and `>-` block scalars. It reads the `jobs:` section only. Job keys other than `runs-on`, `env`, `steps` and step keys other than `name`, `id`, `if`, `uses`, `shell`, `run`, `env`, `with` are a tooling failure. *Reason:* PyYAML is not in CI's install and the Plan adds no dependency; a strict subset fails closed on any construct it does not understand.
- **Inventory.** `REPLAY_INVENTORY` lists all sixteen step names in file order, each `executed` or `excluded` with a reason. Excluded: "Check out exact candidate head" (replaced by the copy), "Set up Python 3.12" (the caller's interpreter, whose major.minor must equal `python-version`), "Install applicable validation dependencies" (needs the package index). The replay refuses (`REPLAY_INVENTORY_DRIFT`, tooling) when the head's step names differ from the inventory, when a step changes between `uses:` and `run:`, or when an unknown key appears. The owner test pins the same against the real `ci.yml` (contract G-3; C-4).
- **Excluded steps get substituted outcomes**, because the final audit step requires `success` from them when `needs_python` is true: checkout `success` once the copy is verified at head; Python `success` only when major.minor equals the workflow's `python-version`, otherwise `failure` (tooling); install `success` only when every distribution the step's own `run:` text names (`-r` files read from the copy, literal requirements, and the `-e .` project's name from the copy's `pyproject.toml`) is installed in the caller's environment, otherwise `failure` naming the missing ones. Reports label them `excluded, substituted`.
- **Conditions and expressions.** An evaluator for the expression subset the workflow uses: string literals, `==`, `!=` (case-insensitive, as GitHub compares), `||` and `&&` (value-returning), `!`, parentheses, `always()`, `success()`, `failure()`, `cancelled()`, and the contexts `github.event_name`, `github.sha`, `github.workflow`, `github.event.before`, `github.event.pull_request.{base,head}.sha`, `steps.<id>.outputs.<name>`, `steps.<id>.outcome`. Any other context or function is a tooling failure. An `if:` without a status function gets the implicit `success()`, so after a failure only `always()` steps run, as on GitHub. For `pull_request` the event carries base and head and `github.event.before` is empty; for `push`, `github.event.before` is base and `github.sha` head. `github.sha` on a pull request is the merge ref on GitHub; every workflow use reads `head.sha || github.sha`, so the head is what the replay needs.
- **Execution.** Each executed step's `run:` text, interpolated, is written to a script in the temporary directory and run with `bash -e` (no `shell:`) or `bash --noprofile --norc -eo pipefail` (`shell: bash`), F-5, in the copy, with: the child environment (§5.8); the job `env:`; the step's `env:` (interpolated); `RUNNER_TEMP` (a fresh directory under the temporary directory); `GITHUB_OUTPUT` (a fresh file per step, parsed afterwards into `steps.<id>.outputs`); `CI=true`, `GITHUB_ACTIONS=true`, `GITHUB_EVENT_NAME` (runner defaults; F-6 shows nothing reads them); and `PYTHONPATH` the copy.
- **`PYTHONPATH` and the installed package (OBS-W5-5).** CI's editable install maps to its own checkout. The caller's editable install maps wherever the caller installed it, so the replay puts the copy first on `PYTHONPATH`, which takes precedence over the editable finder. Before the steps the report prints, for each `[project.scripts]` entry of the copy's `pyproject.toml`, the executable `which` finds and the file its module resolves to under the replay environment; a module that resolves outside the copy fails the report as tooling. Observed: `hdctl (…/venv/bin/hdctl) -> engine.cli.main: <copy>/engine/cli/main.py`.
- **Full validation (the option ID-8 leaves).** `--full` sets base to head; the classifier then returns `identical_refs_full_validation`, all seven lanes and every full-validation target. *Reason:* it is the classifier's own mode, so the replay reaches every lane step and every full-validation target (OBS-P3-5, OBS-P4-1) without classifier logic of its own.
- **Results.** Per step: number, outcome (`SUCCESS`, `FAILURE`, `SKIPPED`), `executed` or `excluded, substituted`, duration, and the last 3 output lines (30 on failure). A failed step is classed `TOOLING` (exit 126 or 127, "command not found", or a collection or import error in its output) or `BEHAVIOR`, by that fixed rule. The final audit runs with the replay's own outcomes, so `CI_APPLICABILITY_AND_EXACT_HEAD_OK` appears only when CI's rule would print it. Afterwards the copy's status is shown.
- **Interpreter.** The report prints `sys.executable` and its version, and the workflow's `python-version`.

### 5.8 Closed rails, no network, keys-only output (ID-9)

- Child environment: the caller's environment without `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HD_GEOCODE_KEY`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `GH_TOKEN`, `GITHUB_TOKEN` and `ENGINE_ENV`; then `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `PYTHONDONTWRITEBYTECODE=1`; `PATH` with the caller's interpreter directory first; `TMPDIR` and `XDG_STATE_HOME` inside the temporary directory. `ENGINE_ENV` is removed beyond the instruction's list because it is the `APP_ENV` alias (Plan IF-1) and its leak changes test results (OBS-P4-7); CI's runner does not set it.
- No report runs `pip`, `git fetch` or an installer, or imports a network module; the owner test checks the tool's imports and string constants (§5.10).
- A missing `ruby`, `bash`, `curl`, pytest or installed distribution is a tooling failure, never installed and never a behavior failure (C3; addendum 2.2).

### 5.9 Classifier registration (ID-10; the choice §9.1 leaves)

The smallest fail-closed registration, mirroring the existing `tools/bodygraph/` owner pattern (29 lines, all additions):
- `_CI_TOOL_PREFIX = "tools/ci/"`, `_CI_TOOL_LANES = frozenset({"product"})`, `_CI_TOOL_TEST_OWNERS = {"tools/ci/prepush_check.py": ("tests/tools/test_prepush_check.py",)}`, with a one-line comment;
- `_lanes_for_path`: a `tools/ci/` path selects `product`;
- `_ci_tool_owner_targets`: a `.py`, `.sh` or `.sql` path under `tools/ci/` without a registered owner raises `CI_TOOL_OWNER_TEST_MISSING:<path>`, and a missing owner file `CI_TOOL_OWNER_TEST_INVALID` (C-6's fail-closed shape);
- `changed_test_targets` calls it; `_registered_owner_test_paths` includes its owners, so the owner test is a full-validation target and the WU-PR-01 guard still finds 0 uncovered files.

*Why `product`:* a changed `tools/ci/` file must turn on `needs_python` and run its owner; `product` is the cheapest lane (12 s hosted, 77 tests) and is the precedent for the repository-owned check `ci/checks/check_agents_md_citations.py`. The new test file itself selects `product` and `release` by the existing generic `tests/` rule, unchanged. Effect on CI for this pull request: the classifier change selects full validation (all seven lanes; acceptance (4)). No workflow step, lane or job is added. The two pin files keep every pin: none enumerates the bodygraph-style registries (the integration file's registry tests use `_registered_owner_test_paths()` generically), so no pin file changes (§6.1).

### 5.10 The owner test (ID-10; the choice §9.1 leaves)

`tests/tools/test_prepush_check.py`: 14 test functions, 21 cases with parameters, 25 to 32 s locally. It imports the tool as `tools.ci.prepush_check` (a namespace package under the existing `tools` package; no `__init__.py` is added) and restores `sys.dont_write_bytecode` after the import. It never runs the repository's suite, a real lane step or the attestation build.

- **Byte identity, ignored files and `.git` (item 7).** Every tool run goes through one helper that snapshots the repository it reads before and after: for every file, directory and symlink under the root, ignored files and `.git` included, the `lstat` mode, inode, size, `mtime_ns` and `ctime_ns`, plus the content hash of every git-metadata file outside `.git/objects/`. Any write to an entry changes its `ctime_ns`, which user space cannot set back, and creating or removing an entry changes its directory's `mtime_ns`; so an equal snapshot proves no byte was written, including a rewrite with identical bytes (OBS-4) and a file created and removed during the run (OBS-14). The helper also asserts no `.git/worktrees` and that no dummy key value appears in the output. The repository clones carry a planted ignored file (`tests/__pycache__/sentinel.cpython-312.pyc`).
- **Cases.** (1) the inventory pin against the real `ci.yml`, with the three exclusions, the two `uses:` actions, the job env equal to the tool's closed rails and `python-version` `3.12`; (2) drift — a renamed step, an added step and an unsupported key each raise `REPLAY_INVENTORY_DRIFT`; (3) the expression forms of the workflow, both events, the implicit `success()`, and unsupported contexts; (4) the interpreter substitute; (5) coverage on the repository: the binding token set equals the guard's, both uncovered sets are empty, the owner test is a full-validation target; (6) a synthetic repository where the guard's wider token set accepts files the binding definition flags, with one passing, one failing, one import-error and one tracked-file-rewriting file: `PASS`, `BEHAVIOR`, `TOOLING`, the copy shown `CHANGED`, the report failing; `--no-run`; then the success rule once the files move under a lane token; (7) on a clone of the repository: `build-notes` (one match, hash equal), `membership` for all 45 roster paths plus a non-member (equal to `ADMITTED_RELEASE_ROSTER`), `sweep` (0), `lanes --full` (full validation, every target), `membership` without a path; (8) `lanes` equality with the classifier's CLI for a tool change under `pull_request` and `push` and for an unregistered path's refusal (head off the checkout's `HEAD`, so through a copy), and with the classifier's functions for six path lists, refusals included; (9) `build-notes` with zero, one and two files; (10) dirty-tree refusal for a modified, a staged and an untracked file; (11) the child environment; (12) no network import and no `fetch`, `remote`, `hooks`, `core.hooksPath` or `worktree` string in the tool; (13) a synthetic workflow with the real sixteen step names, replayed green and with a failing lane (later steps skipped, the final audit failing, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` absent), whose steps assert closed rails and the absence of every key; (14) a report whose inputs are missing fails as tooling and the run still ends with the read-only check.
- No case is skipped, deselected, marked `xfail` or quarantined.

### 5.11 Carried classifier gaps and O-14 (ID-11)

Unchanged and not closed here: OBS-P4-1 and OBS-P3-5 are classifier gaps outside this unit's registration. `lanes` shows the classifier's actual selection; `replay --full` runs every full-validation target, which includes `tests/scripts/test_dev_start_reader.py`, `tests/bodygraph/test_vendor_prod_override.py`, `tests/cli/test_bg_resolve.py` and `tests/cli/test_aux_preview.py`. They go to the Product Owner as later classifier change candidates (no later unit of Plan v1.1 is a classifier unit). O-14 does not reproduce (instruction §5.3); nothing is owed.

## 6. Change set

### 6.1 Files

| Path | Change | Bound (instruction §6) |
| :- | :- | :- |
| `tools/ci/prepush_check.py` | new, 1,229 lines | the tool (ID-1 to ID-9) |
| `tests/tools/test_prepush_check.py` | new, 552 lines | the owner test (ID-10); fixtures only under `tmp_path` |
| `ci/checks/classify_ci_changes.py` | +29 lines | the registration (ID-10) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md` | new (PR-30) | the result record with the captured runs (§11) |

`tests/evidence/test_rails_ci_workflow_integration.py` is not changed: no pin enumerates the registry the entry joins (§5.9). The instruction allowed it; this plan does not need it.

### 6.2 Expected unchanged (a needed change is a finding, §13 and instruction §14)

`.github/workflows/ci.yml` and every other workflow; `ci/jobs/*.yml`; `ci/checks/*` other than the classifier; `requirements*.txt`, `pyproject.toml`, `pytest.ini`, `.gitignore`; every release member, `catalog/manifest.json`, `engine/config/registry_loader.py`; every governed evidence artifact, the Index and Mirror, path proofs, frozen families, `tools/evidence/**` and every other existing tool; every existing test file, the two pin files included; `README.md`, `AGENTS.md`, `CHANGELOG.md`, `docs/**` outside `docs/ephemeral/`, `docs/pfcanon/**`; `.claude/**`; any git hook. No `tools/ci/__init__.py`.

## 7. Implementation sequence (PR-30)

1. **Recover.** Inspect local roots, worktrees, branches, open pull requests and `docs/ephemeral/` for `HDE-CRD-0002-WU-PR-06-*`. Resume the most advanced consistent state; otherwise continue.
2. **Base.** `git fetch origin main`; create the working branch from the then-current `main`. If `main` moved past `1993d07`, confirm the moved commits do not touch §6 paths or `ci.yml`; if they do, re-run §4.1 and record the difference before applying.
3. **Apply.** `git apply --index docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0-prototype.diff`; verify the three blobs of §4.4.
4. **Validate locally** (§9), in throwaway clones and detached worktrees with closed rails, `ruby`, `bash`, `curl`, CI's install and the editable install pointing at the code under test. The registration and the owner test are applied together (F-1).
5. **Commit** the three paths as one coherent commit ("HDE-CRD-0002 WU-PR-06 (S20): read-only pre-push and pre-plan check"), from a clean tree.
6. **Captured runs** (§11) at that commit, from a clean clone of it, with every exit status taken from the producer's own status and the before/after state check of §11.
7. **Result record** `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.0.md` with the captured runs, the checks with counts, the registration, the carried items, in-flight decisions (or `NONE`) and nonclaims; commit it.
8. **Publish:** push; open the one pull request with the template headings (§10); return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

## 8. Requirement → change → test map

| Requirement or obligation | Change | Proof |
| :- | :- | :- |
| S20 "one read-only command"; IF-9 "writes only under a temporary directory; asserts a clean tree before and after" | `main`, `repository_state`, `make_copy`, the temporary directory (§5.1, §5.2) | the snapshot helper around every tool run; the dirty-tree cases; the missing-inputs case; NC-1, NC-2, NC-5, NC-10; the captured runs' before/after check |
| S20 "CI lanes … for given paths" (and base/head); Plan (2) "`lanes` output equals the classifier's" | `report_lanes` (§5.3) | lanes-equality case (CLI, both events, refusal; functions, six lists); NC-8 |
| S20 "release membership for given paths"; Plan (2) "`membership` matches `ADMITTED_RELEASE_ROSTER`" | `report_membership`, `admitted_release` (§5.4) | the 45-path case; `admitted_release` equals the imported constants |
| S20 "the current Build Notes path and hash"; Plan (2) "resolves exactly one … and prints its SHA-256" | `report_build_notes` (§5.5) | the zero, one and two-file cases; the repository case |
| S20 "the uncovered-test sweep run in a throwaway copy"; Plan (2) "`sweep` reproduces the Audit §3(b) set and runs it in a throwaway export"; G-2 | `compute_coverage`, `report_sweep` (§5.6) | the repository coverage case; the synthetic case; NC-7; the 135/0 runs |
| S20 "a `ci.yml` replay in a throwaway worktree"; Plan (2) "`replay` covers every lane step name in `ci.yml` (pinned by the test)"; G-3 | `REPLAY_INVENTORY`, the parser, `Expressions`, `report_replay` (§5.7) | the inventory pin; drift cases; the synthetic replays; NC-3, NC-4; the captured replays |
| Plan (3) "No hook, no writes, no network" | §5.2, §5.8 | the snapshot (hooks directory included); the import and string case; the child-environment case; NC-6 |
| Plan (4) "Lanes green (full validation, classifier changed)" | the registration (§5.9) | hosted CI on the exact head: all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (PR-35) |
| Addendum 2.2 `ruby` requirement | §5.6, §5.8 | the missing-tool preflight; the full sweep with `ruby` on `PATH` |
| Constraint "Duplication" | G-2 and G-3 pins | the coverage and inventory cases fail on drift |
| Exclusion "No SessionStart hook"; no `.claude/` change | none | §6.2; the import and string case |
| Evidence obligation "PR result record with one captured run" | the result record (§11) | PR-40 |

## 9. Validation plan (PR-30, local; every run that can write tracked files in a detached copy, ending with `git diff --exit-code` and an empty untracked status)

1. The owner test alone: `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` (expect 21 passed); record its runtime.
2. The pin files and neighbours: `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_http_reader_ci_ownership.py`, `tests/evidence/test_architecture_snapshot.py`, `tests/tools/test_epic020_bundle_tool.py` (expect the counts of §4.3.2).
3. The classifier dry run on the pull request's base and head: `python ci/checks/classify_ci_changes.py --base <base> --head <head> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>`: all seven lanes, `changed_tests=true`, 166 targets.
4. The changed-test step's targets as `ci.yml` runs them (a detached worktree, `PYTHONPATH` the worktree), which a full replay performs.
5. The seven lanes as `ci.yml` writes them: `python tools/ci/prepush_check.py replay --base <base>` from a clean clone of the commit (all seven lanes are selected because the classifier changed), and one `--full` replay.
6. The full `tests/` sweep in a detached copy with `ruby`, `bash` and `curl` on `PATH`, closed rails, `XDG_STATE_HOME` an empty scratch directory, the editable install mapped to the copy under test or `PYTHONPATH` set to it, as §4.3.7 did (OBS-W5-5); expect 5,207 passed, 3 skipped, 2 xfailed, 0 failed (§4.3.7's 5,206 plus the 21st case).
7. The negative controls NC-1 to NC-10 of §4.3.4, each in a throwaway clone, each restored; record that each fails as intended.
8. `python3 ci/checks/check_agents_md_citations.py` and `ci/checks/check_env_pins.sh` (exit 0).
9. `git diff --name-only <base>..HEAD` lists exactly the three paths of §6.1 and the result record.

OBS-17 (`tests/qa/test_generate_epic_close_pack.py`) is recorded as OBS-17 if it shows; never "fixed" here.

## 10. Pull request split, merge dependencies and description

- **One pull request** for the unit, carrying the three paths and the PR-30 and PR-35 result records. No split: the registration needs the owner test (F-1), and the tool is the owner test's subject.
- **Merge dependency:** this plan's pull request merged first (it carries the companion diff). WU-PR-05 is merged. WU-PR-07 merges after this unit (Plan v1.1 §7).
- **Description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules: "Why" (S20; Plan v1.1 §7 WU-PR-06; instruction v1.0); "What changed" by path; "Checks run" with counts; "Not in this PR" (WU-DOC-01's usage note; the OBS-P4-1 and OBS-P3-5 classifier gaps); "What merging does": the tool becomes current on `main`; no QA, acceptance, Ops or closure is established, and "the tool's green is not CI's green and not QA". The PR carries records under `docs/ephemeral/`, so it also states "Merging preserves the record and approves nothing (D21-C)" for those records.

## 11. Acceptance and evidence obligations

Plan v1.1 §7 acceptance (1) to (4) with the instruction §10 readings; proofs in §8. Evidence obligation "PR result record with one captured run", read as one captured run of every report at the candidate commit, recorded in the result record:
- `lanes --base <PR base> --head <commit>`; `lanes` for a path list with one refused path (for example `--path tools/ci/prepush_check.py --path ci/checks/unregistered_example.py`);
- `membership` for a member and a non-member;
- `build-notes`;
- `sweep` (0 at the head) and `sweep --head a429c7c --no-run` (135, compared file for file with WU-PR-01 instruction §5.1);
- `replay --base <PR base>` and `replay --full`;
- each run's exit status and duration;
- the byte-identity check of the repository around the captured runs: `git status --porcelain=v1 --untracked-files=all` empty and `HEAD` and the git-metadata digest (every file under `.git` outside `objects/`, by content) equal before and after;
- every check of §9 with counts; the registration; the carried items' dispositions (§16); the nonclaims (§17).

The result record is the evidence; the tool's output is quoted in it as non-governed tooling output (C6).

## 12. Security and migration constraints

- **Migration:** none. **Rollback:** Nathan's revert of the squash commit; no member changes, so no refresh.
- **Security:** read-only by construction (§5.2); closed rails and key removal for every child (§5.8); no secret, token, key value, birth input, location or user identifier in output, tests, records or commits (the test asserts dummy key values never appear). Paths are validated by the classifier's `_normalized_path`, refs by `rev-parse --verify --end-of-options`; every subprocess gets an argument vector, never a shell string built from input. The replay runs only the head's own `ci.yml` `run:` text, in the copy, as CI would. The temporary directory is owner-only and removed at exit.

## 13. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | Drift from `ci.yml` | the inventory pin (G-3) and the token-set pin (G-2) fail in the pull request that drifts |
| RK-2 | A shallow checkout cannot copy a commit on no ref (F-3) | the report fails as tooling with the reason; CI and full clones are unaffected |
| RK-3 | Replay differs from hosted CI in environment (the caller's interpreter and install, `PYTHONPATH`, runner defaults) | the substitutes, the interpreter check, the resolution lines and the nonclaim; the tool's green is not CI's green |
| RK-4 | The owner test's runtime grows with repository size | measured 25 to 32 s; the snapshot uses `lstat` plus metadata hashes; recorded in the result record |
| RK-5 | A Codex finding needs a change outside §6.1 | an in-flight decision under instruction ID-12 (path, reason, validation, review coverage); a rescope only for a §6.2 path or a material change (instruction §14) |
| RK-6 | OBS-17 in the qa lane | recorded as OBS-17 |

Recovery: an interrupted PR-30 or PR-35 resumes in its own session from its last saved artifact after inspecting worktrees, branches, pull requests and `docs/ephemeral/`. A failed captured run leaves the repository untouched by design; remove the temporary directory and run again. An instruction defect returns to the IA through PR-10; a plan defect before Proceed returns to this PR-20 session; abort only by Nathan's PR-50.

## 14. Decisions taken in this plan (instruction §9.1; within approved scope)

| ID | Decision | Reason |
| :- | :- | :- |
| PD-1 | Syntax, output, exit codes 0 to 4 (§5.1) | IF-9's exit rule plus distinguishable refusal and violation states |
| PD-2 | Copy by `git clone --shared --no-checkout` and a detached checkout, in one owner-only temporary directory (§5.2) | reads the source only; worktree registrations land in the copy |
| PD-3 | The tool's own check: clean tree, `HEAD`, porcelain status and a git-metadata digest; ignored files checked by the test (§5.2) | exact and cheap at run time; the full rule where it can be proven |
| PD-4 | `lanes` runs the classifier CLI for refs and its functions and writers for paths (§5.3) | delegation, equality by construction |
| PD-5 | `membership` reads the roster with `ast` (§5.4) | no import, no admission call, no bytecode |
| PD-6 | Coverage computed in a separate process from the copy's own files; reproduction by `sweep --head a429c7c --no-run` (§5.6) | ID-7's process rule; one code path for head and reproduction |
| PD-7 | `--continue-on-collection-errors` and a JUnit file in the temporary directory for the sweep run (§5.6) | per-file outcomes (F-4) |
| PD-8 | Standard-library strict YAML subset, a full sixteen-step inventory, substituted outcomes for the three exclusions (§5.7) | no dependency; fails closed; the final audit runs with honest outcomes |
| PD-9 | `--full` as a named option (§5.7) | the classifier's own full validation; covers OBS-P3-5 and OBS-P4-1 |
| PD-10 | `PYTHONPATH` the copy for every step, with a resolution line per console script (§5.7) | OBS-W5-5: the code under test is the copy's |
| PD-11 | `ENGINE_ENV` removed from children in addition to the instruction's list (§5.8) | the `APP_ENV` alias; OBS-P4-7 |
| PD-12 | Registration: a `tools/ci/` prefix in lane `product`, an exact owner map, a fail-closed owner function (§5.9) | the smallest form with C-6's shape; the bodygraph precedent |
| PD-13 | Owner test: throwaway clones and synthetic repositories; `lstat` plus `ctime_ns` snapshot with metadata hashes; 21 cases (§5.10) | hermetic, 25 to 32 s, proves item 7 including identical-byte rewrites |
| PD-14 | No change to the integration pin file (§6.1) | no pin enumerates the registry the entry joins |

## 15. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged: CR-1, CR-2, CR-3 (CANON_RECONCILIATION) APPROVED_AS_CHANGED (Thoth; Specification v1.1 lineage); CR-4 APPROVED (Product Owner; `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2); CR-5 APPROVED_AS_CHANGED (same record §3); CR-6 APPROVED, alternative (a) (the IA through RS-20; rescope review v1.0 §12; addendum 2.6); CR-7, CR-8 APPROVED, alternative (a) each (Product Owner direction of 2026-10-14; decision record §6; addendum 2.7).

No new conflict. The plan's readings stay inside instruction ID-1 to ID-12 and the canon they rest on: the copy outside the repository satisfies both the Specification's "writing nothing to the repository" and the Plan's "throwaway worktree" (Glow QA Guide §2.2.11, non-writing checks); the tool is repository-owned validation tooling whose mechanism the implementation task selects (Plan Templates "CI lane classification and automated budget-control discipline"); its output is non-governed tooling output (Plan Templates "Repository loci and file minting"). Canon is silent on git hooks and pre-push tools; the Specification's Exclusions govern.

## 16. Stale documents and carried items (not in this PR)

- **Stale documents the tool makes stale but this unit may not change:** `README.md` has no usage note for the tool (owner WU-DOC-01, "pre-push check usage", Plan v1.1 §7). `AGENTS.md` names no pre-push tool; any mention belongs to WU-DOC-01's operative passages or the Product Owner. No operative document refers to a pre-push check: `git grep -i -E 'pre-?push'` outside `docs/ephemeral/` at `1993d07` finds only archived directory listings under `.audit_src/` and `_arch/` (the git hook sample name `pre-push.sample`) and PF10 addendum 2.10's next-stage line.
- **Carried items (instruction §15), with dispositions:**

| Item | Disposition here |
| :- | :- |
| F-5 (WU-PR-05's `scripts/ingest/run_vendor_ingest.py` registration) | carried; `lanes` reports it as the classifier applies it; nothing to change |
| C-3 / LR O-1 | applied (§5.6; the token-set pin) |
| C-4 | applied (the inventory pin) |
| C-6 | applied (§5.9) |
| OBS-P4-1, OBS-P3-5 | surfaced (§5.11); to the Product Owner as later classifier change candidates |
| O-14 | does not reproduce; nothing owed |
| `ruby` (addendum 2.2), O-6, `ruby` after `ubuntu-latest` moves to 26.04 | missing `ruby` is a tooling failure (§5.6, §5.8); PR-35 records the hosted version and image if a job log shows them |
| OBS-W5-5 | handled (§5.7 PD-10; §9 item 6) |
| OBS-W5-3, S19-R04 | the replay runs only `ci.yml` text; no owner tool runs outside it |
| OBS-P4-2, OBS-P4-7 | children get `APP_ENV=dev` and no `ENGINE_ENV` (§5.8); the leak's fix stays with a later owner |
| OBS-4, OBS-14 | the sweep and the replay run tests only in a copy; the owner test's snapshot detects both kinds of write |
| OBS-17 | recorded if it shows |
| `release_id` `77204764…`, 45-member roster | `membership` (observed) |
| Current PF10 file | `build-notes` (observed `v13.6.1`) |
| LR5-O2 (ID-12), LR4-O3 | applied (RK-5; §9 lists only checks run at the baseline or by the prototype) |
| Others of instruction §15 | not this unit; with their owners |

## 17. PR-30 and PR-35 ownership

- **PR-30** (after Nathan's Proceed for this exact plan v1.0): recovery; §7 steps 1 to 8; local validation (§9); the captured runs (§11); one coherent commit for the three paths, then the result record; publication and `PR_CANDIDATE_PUBLISHED`; the PR-35 handoff. It does not resolve reviews, chase CI readiness or merge.
- **PR-35** (its own dedicated session, entered from PR-30's handoff): retrieves and resolves the Codex code review findings (the Codex security review is not part of the chain, addendum 2.3); retests locally and pushes coherent corrections (instruction ID-12 for a correction outside §6.1); verifies current-head CI (all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; no `[skip ci]` without Nathan's direct authorization), the remote head and mergeability; records the hosted `ruby` version and image if the job log shows them; returns `MERGE_PENDING` without merging.
- **Merge:** Nathan only. **PR-40:** after the merge is observed or asserted, the IA reviews the landed lineage.
- **Nonclaims** every record keeps: the tool's green is not CI's green and not QA; its output is not governed evidence; no QA verdict, acceptance, Ops, deployment, PF09 movement or closure; no canon edit.

## 18. Session identity and recovery envelope

| Field | Value |
| :- | :- |
| Planning session (PR-20) | https://claude.ai/code/session_01NZEtMVb5HR3XYEmJ6W5cb6 (`session_disposition` INITIAL_DEDICATED_ASSIGNMENT; `role_session_ref` NOT_YET_ASSIGNED, assigned by Nathan) |
| PR-30 | this same dedicated WU-PR-06 PR session, on Nathan's Proceed (PR-30: "PR-30's session plans with PR-20 and builds"); not yet started |
| PR-35 | its own dedicated session, entered from PR-30's handoff; not yet started |
| Vehicle | none yet for the code (NOT PRODUCED). This plan travels on its own docs pull request |
| Resume point | Nathan's Proceed for this plan v1.0, or a returned correction of this plan before Proceed |

## 19. TypeSafe reading for the receiving session (PR-30, WU-PR-06, plan v1.0)

Action sent (v8.2): "Implement, in a dedicated session after a Product Owner Proceed, one work unit from a new detailed plan that has not yet been reviewed: a new read-only pre-push command-line tool of about 1,200 lines with five reports, a new owner test module of about 550 lines, and a 29-line registration in the existing CI change classifier, all three already prototyped in a throwaway copy and supplied as a companion diff that the session applies and re-verifies. A task list exists; the session runs local validation including a full test sweep of about 20 minutes and a CI workflow replay of about 20 minutes, captures one run of every report, writes a result record and opens the pull request; no live provider call occurs, and an automated code review, a separate review-resolution session and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.57 (confidence 0.57); rung probabilities low 0.00, medium 0.06, high 0.41, extra high 0.42, max 0.10, ultracode 0.01. Model probabilities Fable 5.1 0.04, Opus 5.5 0.93, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.91). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.016, Fable 5.1 at extra high 0.017, Fable 5.1 at max 0.004, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.056, Opus 5.5 at high 0.381, Opus 5.5 at extra high 0.391, Opus 5.5 at max 0.093, Opus 5.5 at ultracode 0.009, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.012, Sonnet 5.5 at extra high 0.013, Sonnet 5.5 at max 0.003, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-19T02:47:05Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-19T02:47:05Z; HTTP 200 in 0.58 s; 5517 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and extra high.

- **Which request.** The installed TypeSafe scoring skill's request v8.2 (`request-v8.2.json`) and `scripts/score_v8.py`, run once with session kind `implementation` before this plan was saved.
- **Records.** No Notion row was written, as PR-20 directs. Nathan's pick for PR-30 is not stated. Nathan's pick for this PR-20 session is not stated; its reading is instruction v1.0 §19.

**Surface advice for PR-30:** a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** Python 3.12 with CI's install (package-index access for `pip install -r requirements-dev.txt`; the container's default `python3` is 3.13, so create the venv from `/usr/bin/python3.12`), `ruby`, `bash`, `curl` and git; closed rails with the vendor, database and GitHub keys unset (the container sets several of them); throwaway clones and detached worktrees outside the session's checkout, with the editable install mapped to the copy under test, or `PYTHONPATH` set to it, before the full sweep.
- **History.** The 135-file reproduction needs `a429c7c`; a shallow clone lacks it (`git fetch --deepen=400 origin main` reached it in this session).
- **Run times observed here.** Owner test about 25 to 32 s; a replay of the pull request's shape (all seven lanes) about 21 minutes (1,240 s here, concurrent with a full sweep); a full `tests/` sweep about 16.5 minutes (988 s here, concurrent with the replay); hosted CI about 21 minutes (instruction §5.9).
- **Access.** No live vendor, production or database access.
- **Order.** This plan's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-06 / PR-20 / plan 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-06 (S20) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z). Receiver contract read: PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08.672Z) |
| role/stage | dedicated WU-PR-06 PR engineering session / PR-20 |
| capture time | 2026-10-19T03:08:15Z |
| execution identity | https://claude.ai/code/session_01NZEtMVb5HR3XYEmJ6W5cb6 |
| inherited usage | instruction v1.0 §20 (PR-10) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `1993d07` (`docs/pfcanon/` unchanged since `5e62a65`).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, content and hold | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (all sections); PR-30 — PR Implementation Proceed — 100926.1 (receiver contract); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (detailed PR plan by the dedicated PR session; `ASK OK? — PR IMPLEMENTATION PLAN`; Proceed is the approval; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents govern within their scope) |
| Overlays | PF10-HDE-Build-Notes v13.6.1: addenda 2.2 ("Affected surfaces"; the `ruby` requirement), 2.3 (Rules 1 to 5), 2.4, 2.5 (OBS-17; record commits select lanes), 2.9 (OBS-P4-1), 2.10 (the carried list; LR5-O2, LR5-O5), 2.1 (§19) |
| Non-mutation, rails, failure classes (C1 to C3) | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 "Tooling vs behavior failures (pytest and harnesses)", §2.2.6 "Rails posture in CI (default CLOSED)", §2.2.11 "Evidence-governed CI sequence (names-only)" ("A non-writing check MUST NOT mutate the repository or external state"); HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.2 "CI default CLOSED & evidence" and the determinism pins |
| Classifier and CI scope (C4, C5) | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.2 (a validly reduced lane set with a passing final applicability audit is sufficient; automated CI budget control); Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "CI lane classification and automated budget-control discipline" (repository-owned validation tooling; the implementation task selects the mechanism) |
| Loci and tool output (C6) | Plan Templates "Repository loci and file minting" (minting within established homes; non-governed tooling output) |
| Coverage definition and lanes | WU-PR-01 instruction v1.0 §5.1 and §8 (C-3, C-4, C-6); addendum 2.4 (O-1 to O-6) |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Ordinary CI is the one `test` job …"; "Release identity"; PR descriptions; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" (exit codes from the producer's own status) |

Silence: canon names no git-hook, pre-push or SessionStart rule; the Specification's Exclusions govern.

## Checks run by this session

All in scratch clones; the session's checkout was only read (its own `git fetch --deepen=400 origin main` aside).

| Check | Where | Result |
| :- | :- | :- |
| Prerequisite: amthorn78/glow-hdengine-v2#658 merged | `origin/main` | `1993d07` is #658's merge; `HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md` present |
| Baseline re-check (§4.1) | scratch clone at `1993d07` | as §4.1; no difference |
| Reports, once each (§4.3.3) | prototype clone | as §4.3.3 |
| `sweep --head a429c7c --no-run` vs WU-PR-01 instruction §5.1 | prototype clone | 135 = 135, file for file |
| Owner test | final head `003c5f3` | 21 passed (24.5 s); 20 passed at `2e85548` (31.9 s) |
| Pin files and neighbours, per file | final head `003c5f3` | 138, 4, 5, 6 passed |
| Citations check; env-pins check | final head `003c5f3` | `AGENTS_MD_CITATIONS_OK`; `[env-pins] OK` |
| Classifier dry run `1993d07..003c5f3`, `pull_request` | final head | all seven lanes; 166 targets |
| Replay `--base 1993d07` | `0ff958a` | all 16 steps SUCCESS; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; exit 0; 1,240 s |
| Full `tests/` sweep | `2e85548` | 5,206 passed, 3 skipped, 2 xfailed, 0 failed; exit 0; 986.6 s; tree clean |
| Negative controls NC-1 to NC-10 | throwaway clones | each failed as intended (§4.3.4) |
| Companion diff applies to `1993d07` | fresh clone | three blobs equal §4.4 |
| TypeSafe reading for PR-30 | the installed skill's script | §19 |

Not run here (NOT EXECUTED): a `replay --full` (PR-30 runs it, §9 item 5; the pull-request-shaped replay already selected all seven lanes and 166 targets because the classifier changes); hosted CI (no code pull request exists); the Codex code review; any live vendor, production or database call.
