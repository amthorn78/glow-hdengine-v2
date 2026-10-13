---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.3.md
artifact_version: "1.3"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review resolution and merge readiness); this record is the checkpoint for PR-35's third corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.2.md (v1.2, PR-35 checkpoint for the second corrective push; blob f722b4d3f1ddb1263bfe7db9262b53d8fdd675ef). Preserved unchanged; v1.0 and v1.1 likewise
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d92f90b3389d56d498f12964a91a9)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5804a88bcf861f45ea24d8846288f)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain), as planned by PR_IMPLEMENTATION_PLAN_ID v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112da05bbcc9fae7316f64d1657824ff; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this PR-35 session; unchanged on main 0cd7b84 and on the branch)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (reviewer chain) and § 2.1 (TypeSafe reading)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-02 PR-35 session, https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK; session_disposition NEW_DEDICATED; role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/intelligent-cannon-32u7tl; pull request amthorn78/glow-hdengine-v2#634 (open, not draft, base main 0cd7b84)
step_entry_head: e7ec65f86c5d761f7c1201626d709126001a4ebb (v1.2 checkpoint commit; parent 489bc17)
correction_commit: a028b0c48b154676746e9a104ec84a96b7082ee4 ("fix(evidence): HDE-CRD-0002 WU-PR-02 — decide the wheel layout compat in the wheel child's environment (S06)"; parent e7ec65f; tree 823aa4eb43fee7bc3579a7505529dab08d0d2a75, the exact tree every §4 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.4.md (PR-35, written after the remote evidence below arrives)
created_at: 2026-10-13T20:07:00Z
---

# HDE-CRD-0002 WU-PR-02 — PR implementation result v1.3 (PR-35 checkpoint)

## 1. State

PR-35 checkpoint after the third corrective push. The Codex code review of `e7ec65f` raised one finding, CX-4 (P2) in the S06 wheel stage. It is corrected by `a028b0c`, reproduced before and after in the Debian-patched environment, locally validated (§4) and pushed together with this record. Hosted CI and the Codex code review on the pushed head are pending and arrive through this session's pull-request subscription. Nothing here merges, claims merge readiness, QA, acceptance or closure. Finding identifiers follow v1.2 §2 (`CX-<n>`).

## 2. Review matrix (delta from v1.2 §3)

| ID | Reviewer / location / head | Finding | Classification | Disposition | Evidence |
| :- | :- | :- | :- | :- | :- |
| CX-1 | v1.1 / v1.2 | — | — | corrected (`c0ca923`); thread resolved | v1.1 §4 |
| CX-2 | v1.2 | — | — | accepted residual by Product Owner decision; thread answered (comment 4263215340) and resolved ~19:43Z; recorded for the IA at PR-40 | v1.2 §3.1, §8 |
| CX-3 | v1.2 | — | — | corrected (`489bc17`); thread answered (comment 4263215759) and resolved ~19:43Z | v1.2 §5 |
| CX-4 | Codex code review 5509067586, comment 4263251889, `tools/evidence/build_release_attestation.py` L368, `e7ec65f` | P2 "Detect setuptools using the wheel child's environment": the patched-setuptools check probed the builder's own interpreter state, while `pip wheel` runs with `_clean_child_env()` (only `PATH`, `TMPDIR`, rails and `HDE_ISOLATED_RELEASE_BUILD` survive); a caller `PYTHONPATH` or user base that resolves an unpatched setuptools hides the Debian backend the cleaned child then uses, so the compat module is omitted and the `install_layout` failure returns | substantive, in scope (S06, same file and design as PD-1) | corrected by `a028b0c` (§5 ID-35-5); reproduced before/after (§3); thread answered and resolved after the push | §3, §4 |
| — | Codex review summary (issue comment 6152304678) | Code Review completed 2026-10-13T19:46:29Z on `e7ec65f`, trigger "New commits" | — | read | — |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not requested or waited on | — |

## 3. CX-4 reproduction (E-DEB)

E-DEB: `/usr/bin/python3 -m venv --system-site-packages` in the session scratchpad, CPython 3.13.16, `setuptools` 68.1.2 from `/usr/lib/python3/dist-packages` (Ubuntu-patched: `install_layout` appears 3 times in its `command/install_lib.py`), repository requirements installed, no `-e .`, `_distutils_system_mod` and `engine` not importable. The caller-path condition: `PYTHONPATH` pointing at a scratch copy of the unpatched setuptools 84.0.0 package from E-CI (`install_layout` 0 times). Each case from a clean clone at the stated commit, run as `env -i <rails> PATH=<E-DEB bin>:/usr/bin:/bin [PYTHONPATH=…] <E-DEB python> tools/evidence/build_release_attestation.py --output <external empty> --require-clean`, then `--verify --require-clean` when a bundle exists.

Run 2026-10-13T19:50:05Z–19:53:58Z.

| # | Case | Commit | Result |
| :- | :- | :- | :- |
| 1 | CX-4 before: caller `PYTHONPATH` = unpatched setuptools | `e7ec65f` | build exit 1; stderr `RELEASE_ATTESTATION_FAILED:isolated_package_install_failed`; `failure.json` = `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}`; clone clean. The parent saw the unpatched copy, omitted the compat, and the cleaned child built with the Debian backend (Codex's path) |
| 2 | CX-4 after: same caller `PYTHONPATH` | `a028b0c` | build 0, `--verify --require-clean` 0; `build.log` has `build_backend_compat=distribution_install_layout`; `attestation.json` 28,163 bytes, SHA-256 `231c47b9280c8cc290574737119bdc16e3529a5b34d2c52b0999a5a684b084f1`, `source_commit a028b0c…`, `source_commit_exact true`, `pipeline_stop null`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| 3 | S06 after (plan §11 step 10), no caller `PYTHONPATH` | `a028b0c` | identical to row 2, including the attestation SHA-256 `231c47b9…`: the caller path no longer changes the decision or the output; clone clean |

## 4. Local validation of `a028b0c` (E-CI)

Environment E-CI exactly as v1.1 §4; detached worktree or clean clone; clean tree after each.

Run 2026-10-13T19:50:06Z–20:05:21Z, tested commit `a028b0c` (base `0cd7b84`).

| # | Check (plan §11 numbering) | Result |
| :- | :- | :- |
| 1 | `ci/checks/check_env_pins.sh`; `python3 ci/checks/check_agents_md_citations.py` | 0; 0 |
| 3 | Updater write twice in the worktree | 0, 0; `git diff --exit-code` 0, 0 untracked (governed companions byte-unchanged) |
| 4 | the nine read-only validators (as v1.1 §4 row 4) | all 0 |
| 5 | Classifier `--base 0cd7b84… --head a028b0c… --event-name pull_request` | exit 0; `lanes=evidence,release`; `product/compat/db/rails/qa=false`; `changed_tests=true`; `path_count=18`; the same five targets |
| 6 | Changed-test step (detached worktree, `PYTHONPATH` = worktree) | **198 passed**; tree clean |
| 7 | Evidence lane as `ci.yml` runs it | checks 0; **130 passed** (599.0 s) |
| 7b | `tests/config/test_config_artifacts.py`, `tests/evidence/test_engine_core_evidence.py` | **165 passed**; tree clean |
| 8 | Release-lane tests (four files) | **79 passed** (75 + the four probe-binding cases); tree clean |
| 11 | qa lane, seven files (prudence) | **488 passed**; tree clean |
| 9 | Release-lane build: clean clone at `a028b0c`, E-CI, `release_id_recompute.py --check-manifest-only`, build `--require-clean`, `--verify --require-clean` | 0, 0, 0; no `build_backend_compat` line (compat not applied; PR-30 result v1.0 §4 records that this interpreter resolves `_distutils_system_mod`); `attestation.json` 28,163 bytes, SHA-256 `5eedddea3211f314f8bed9fafb148ba7575acb8ea7fcde94251550e9bc7bea07`, `source_commit a028b0c…`, `source_commit_exact true`, `pipeline_stop null`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| — | Narrow run before commit | `tests/evidence/test_release_attestation.py` 44 passed |

## 5. In-flight decisions

| ID | Decision | Why necessary to deliver the approved scope | Tested by (identity → outcome) |
| :- | :- | :- | :- |
| ID-35-5 | CX-4 correction in `tools/evidence/build_release_attestation.py`: the in-process check is replaced by `_LAYOUT_COMPAT_PROBE`, the same logic as source text, run by `_distribution_layout_compat_required(env, cwd)` with `sys.executable` in exactly the wheel child's cleaned environment and working directory; it applies the compat only on exit 0 with stdout `required`. `import importlib.util` leaves the builder. In `tests/evidence/test_release_attestation.py`: the four-case semantics test executes the probe source with `find_spec` monkeypatched; a new test pins the probe's interpreter, environment (an ambient `PYTHONPATH` and `PYTHONUSERBASE` do not reach it) and directory, and its failure cases; the two wheel-stage tests take the new signature; `test_isolated_console_entrypoint_is_installed_from_tracked_package` (plan §8.1 "unchanged") gains one monkeypatch isolating the probe, since its fake `run` counts exactly three child calls | S06's acceptance (1) is that the attestation builds on a Debian interpreter; deciding the compat in a different environment from the one that builds the wheel leaves a reachable failure (§3). Same file, same design (PD-1), no new child-environment input: the probe runs with the existing `_clean_child_env()` | §3 rows 1–2 (fails before, builds and verifies after); `test_wheel_layout_compat_is_required_only_for_a_distribution_patched_backend` ×4, `test_layout_compat_probe_runs_in_the_wheel_child_interpreter_and_environment` ×4, `test_wheel_build_env_adds_only_the_builder_owned_compat_path`, `test_wheel_layout_compat_supplies_neutral_install_options`, `test_wheel_stage_records_and_scopes_the_layout_compat`, `test_isolated_console_entrypoint_is_installed_from_tracked_package` (all pass) |

ID-35-1 to ID-35-4 stand unchanged.

## 6. PR_REMOTE_ACTION_LEDGER (PR-35, continued from v1.2 §7)

| Time (UTC) | Action | Fact |
| :- | :- | :- |
| 19:42:33 | Push 2 | `b6fe37d..e7ec65f` (`489bc17` + v1.2), no force; remote head read back `e7ec65f86c5d761f7c1201626d709126001a4ebb` |
| ~19:43 | CX-2, CX-3 threads | replies 4263215340 and 4263215759; threads `PRRT_kwDOP103ks6sA712` and `PRRT_kwDOP103ks6sA719` resolved |
| ~19:44 | PR description | updated: CX-2/CX-3 under "Why" and "What changed", `489bc17` checks, CX-2 under "Not in this PR"; headings kept |
| 19:45:42 | Safety-net check-in fired | head `e7ec65f`, CI run 38456991751 in progress, Codex running; nothing open; re-armed `trig_015UpKwTaRpbAnyN781w5fvk` for 20:36Z |
| 19:46:29–31 | Codex review on `e7ec65f` | review 5509067586: CX-4 (P2); summary completed |
| ~19:47–19:49 | CX-4 correction and narrow tests | `tests/evidence/test_release_attestation.py` 44 passed |
| 19:49:36 | Commit `a028b0c` (local) | builder +30/−6, test +42/−7 |
| 19:50:05–19:53:58 | E-DEB reproduction | §3: fails before, builds and verifies after |
| 19:50:06–20:05:21 | Local validation (E-CI) | §4, all 0 / passed |
| ~19:56 | Hosted CI read | run 38456991751 (job 115502168686) on `e7ec65f`: success 19:42:40Z–19:53:35Z; stale (CX-4 required a further change); it completed before the correction was pushed, so nothing was cancelled |
| after this record's commit | Push 3 | `a028b0c` and this record, one push; read back in v1.4 |
| after push | CX-4 thread reply and resolution; PR description update | recorded in v1.4 |

**Remaining useful local action:** none. **Next evidence action:** hosted CI and the Codex code review on the pushed head, received through the subscription; then v1.4.

## 7. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Hosted CI and Codex code review on the pushed head | this PR-35 session |
| CX-2 residual (accepted by Product Owner decision) | recorded for the IA at PR-40 (v1.2 §3.1, §8) |
| PD-10 superseded by ID-35-2; PD-11 stands; `test_isolated_console_entrypoint_is_installed_from_tracked_package` adapted by ID-35-5 although plan §8.1 listed it as unchanged | Nathan / IA (PR-40) |
| OBS-W2-1, OBS-W2-2, OBS-W2-3; OBS-17 | plan §17 owners; QA tool and test owner through the IA |
| Prompt-use provenance writer absent | pending, non-gating |

## Canon relied on

Read on `main` at `0cd7b84` (the branch changes no file under `docs/pfcanon/`):
- **Review chain:** PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1; PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 2 and 3; PR instruction v1.0 §11 ("the attestation keeps its exact-source binding, clean child environment, `--no-index` and `--require-clean` refusal; any build backend seeded into the isolated build comes only from the invoking environment, never the network": the probe adds no child-environment input and runs in that clean environment) and §12.
- **CX-4 and ID-35-5:** HDE Schemas & Artifacts §6.2.1 (the attestation interface, `--require-clean`, refusal and output contracts) and §6.4 (build and verify as the current release surfaces); in-flight: Implementation Plan v1.1 §7 WU-PR-02 acceptance (1); plan v1.0 §5.1 (PD-1, the guarantees kept) and §8.1.
- **Operative documentation:** `AGENTS.md` (current release-bound derivatives only through `build_release_attestation.py --output <external-empty-directory> --require-clean`; closed rails; evidence attribution).

## Nonclaims

No merge readiness, QA evidence, QA verdict, acceptance, PF09/PF30 movement, deployment, canon change or closure. Local green is not hosted CI; CI green is not QA.
