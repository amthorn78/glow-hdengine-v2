---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-05-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
plan_cycle: 1 (the first plan for this work unit)
predecessor: none
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob ee5acb997fcc; 87,354 bytes; landed by #654 at 1e97ba9; unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0; blob 54809ffbaf34; 120,513 bytes; landed by #655 as 8170cd8); companion docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff (blob a73ef64f9d1f; 59,184 bytes)
S19_RECORD: docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md (v1.0, RECORDED; blob 016e74e557ee; 52,542 bytes)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; not edited)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; §6 S19 and Appendix B)
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.3, 2.5, 2.6, 2.7 (AD-4, AD-5), 2.8 and 2.9, as instruction v1.0 and plan v1.0 apply them
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md (v13.6; blob f6f80d8779e8; 167,152 bytes; unchanged on origin/main 8170cd8 since 86e002c; the unique controlled PF10). Provenance, not a gate
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md §2.3, §2.5, §2.6, §2.7, §2.8, §2.9; §2.1 for §16
pf10_addendum_created: none (PR-30 is not a qualifying approval prompt)
proceed: Nathan / Product Owner, by pasting in this session on 2026-10-18 the PR-30 invocation that names exactly docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0, state AWAITING_PO_PROCEED) with the instruction v1.0, with the prerequisite that the plan's pull request is merged (it is: #655, 8170cd8 on main, merged 2026-10-18T19:43:48Z). The one Proceed for plan cycle 1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: the dedicated HDE-CRD-0002 WU-PR-05 PR engineering session, PR-30 phase, https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc (the session that ran PR-20; Nathan pasted the PR-30 handoff in it)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary (repository write scope)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
repository_baseline: origin/main 8170cd8eb36b5e35adfab1fae9231bcd317d951c (#655 over #654)
pull_request: amthorn78/glow-hdengine-v2#656 (https://github.com/amthorn78/glow-hdengine-v2/pull/656; open, base main, not draft)
commits: d0f25b6 (hand-edited source, plan §8.1; equal to the companion diff); 176de33 (owner-produced re-cut and convergence, plan §9; the tested code and evidence head); 173bf97 (the S19 record, docs/ephemeral/ only); the record commit that adds this file (docs/ephemeral/ only)
release_id: 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (1.3.0, 45 members; supersedes 2f18a5eb…)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§14)
created_at: 2026-10-18T20:38:00Z
next_phase: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in its own dedicated session (session_disposition NEW_DEDICATED)
---

# HDE-CRD-0002 WU-PR-05 — PR Implementation Result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** Plan v1.0 is implemented, converged by the owners, validated locally (§7), and published as [amthorn78/glow-hdengine-v2#656](https://github.com/amthorn78/glow-hdengine-v2/pull/656):
- **The nine fixes** S19-F01 to S19-F09 (plan §7), as the source commit `d0f25b6`. Its diff from `8170cd8` equals plan v1.0's companion diff byte for byte, so no hunk departs from the plan.
- **267 regression cases** (`test_s19_*`) in the 13 existing modules that own each fixed source (plan §8.1, PD-13). There is no new test module and no classifier or CI change.
- **The refresh:** one same-version re-cut at `1.3.0` (`release_id` `77204764…`), and two convergence passes that are byte-identical. 56 owner-produced paths change (§6).
- **The S19 record** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`, written from plan §5 (instruction ID-2; plan §14).

PR-35 owns review retrieval and correction, hosted current-head CI and merge readiness. Nothing here is merged. Nothing here claims merge readiness, QA, acceptance or closure.

## 2. Recovery and base

| Check | Observation |
| :- | :- |
| Prerequisite | #655 merged on 2026-10-18T19:43:48Z; `8170cd8` on `origin/main`. Its tree equals the plan commit this session pushed (`58917cd`): no difference |
| Open pull requests | none (GitHub listing, state open, before any remote write of this phase) |
| Local root, worktrees, branches | One worktree, `/home/user/glow-hdengine-v2`, on the session's designated branch. The branch held only #655's merged history, so it was restarted at `origin/main` `8170cd8` before any change. The remote branch had been deleted at the merge |
| WU-PR-05 artifacts on `main` | instruction v1.0, plan v1.0 and its companion diff. No result record, S19 record, code commit or pull request for this unit existed |
| Plan §10 step 3 (head confirmation) | The 49 blob IDs at `8170cd8` equal plan §5.6 row for row (programmatic comparison). `git diff 1e97ba9 8170cd8` changes only the plan and its companion diff (`docs/ephemeral/`), so no member, manifest or other path moved and the refresh base stays `2f18a5eb…`. `git apply --check` of the companion diff on `8170cd8`: exit 0 |
| Environment | CPython 3.12.3 (`/usr/bin/python3.12`; the container's default `python3` is 3.13, so the venvs were built on 3.12 to match CI), with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .` of the worktree under test): pytest 8.4.2, Flask 2.3.3, Werkzeug 3.1.9. `ruby` 3.3.6, `bash` and `curl` on `PATH`; 4 CPUs. The container sets `ALLOW_NETWORK`, `APP_ENV`, `DATABASE_URL`, `GEO_API_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDAPI_BASE_URL`, `HD_API_KEY` and `SAFE_MODE` (values not recorded). Every run used the closed-rails profile: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. It unset `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV`, and pointed `XDG_STATE_HOME` at an empty scratch directory |

## 3. Authority, Proceed and lineage

- **Proceed:** the one Proceed in the front matter, for plan v1.0 exactly (PR-30 "Inputs": the invocation is the bounded Proceed authority).
- **Scope and authority:**
  - Plan v1.0 implements Implementation Plan v1.1 §7 WU-PR-05 under instruction v1.0. None is rewritten.
  - The repository writes stayed inside that authority: plan §8.1's hand-edited paths, plan §9's owner-produced paths, and these records under `docs/ephemeral/`.
- **Upstream:**
  - WU-PR-01 to WU-PR-04 are accepted (PF10 addenda 2.4, 2.5, 2.8 and 2.9).
  - The refresh base is `2f18a5eb…` (addendum 2.9).

## 4. Implementation (commit `d0f25b6`)

| Path | Change | Finding |
| :- | :- | :- |
| `adapter/http_reader.py` (member) | parse refusals for nesting past the recursion limit; bounded writer read; exact `_dev_admin_gate`; `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED`, `_production_posture`, `_mount_for_production` with its hook `_refuse_in_production`; `get_reader_bp` records `_mount_for_production` | F01–F04 |
| `engine/http/compat_handler.py` (member) | `RecursionError` around `get_json` | F01 |
| `engine/cli/main.py` (member) | exact `_ensure_dev_admin_env`; four parse sites; catch-all token | F02, F07 |
| `engine/bodygraph/resolver.py` (member) | `_rail_value`, `_safe_mode_closed`, `_network_allowed`; override client without `log_path`; `RETRY_LOG` import removed | F05, F06 |
| `engine/bodygraph/ingest.py` | exact rails; `None` log defaults | F05, F06 |
| `engine/config/registry_loader.py` (member) | `path.isprintable()` in the manifest path rule | F08 |
| `scripts/cut_release_manifest.py` | `name.isprintable()` in `_path_unsafe` | F08 |
| `tools/config/generate_config_artifacts.py` | the admitted root in the report refusal | F09 |
| 13 test modules | 267 `test_s19_*` cases (plan §8.1's table); five import lines widened; no existing test or assertion changed | F01–F09 |

Every member file ends with one LF and carries no CR. `_truthy` has no other importer; `scripts/bodygraph/run_refresh_worker.py` keeps its own, which is X-03, out of scope.

## 5. Production route exposure after the unit (contract F-3)

- **Production factory** (`adapter.factory.create_app`, `APP_ENV=prod`; instruction §5.3 probe on `176de33`):
  - The dev harness keeps its refusal bytes: `GET`/`HEAD /reader?v=1` 403 `ERR_READER_FORBIDDEN`; the sampler and the three conjunction routes 403 `ERR_WRITER_FORBIDDEN`. The refusals hold with request-time `APP_ENV=dev`.
  - `/ops/probe/env`, `/ops/db/unavailable` and `/ops/writer/diagnostic` answer 404 `ERR_NOT_FOUND` for every method, the bytes an unknown path gets.
  - Unchanged: the `POST /reader` stub (405, `Allow: GET, HEAD`), `/ops/rails/refusal` (503), `/internal/version` (200), the production Reader, Aux and the compat 404.
- **Served set:** in all three factories, rules and pairs are unchanged (21 and 49; `adapter.wsgi` 23 and 55; `/static` excluded). Requested under `APP_ENV=prod`, only the nine canon-retired pairs and `/internal/version`'s body (the new `release_id`) change.
- **Dev, test and local runners:** the canonical runner `python -m adapter.http_reader`, `scripts/dev_start_reader.sh`, `VERIFY.sh` and the tests build the factories under a non-production posture and get the full mount unchanged. The canonical runner under `APP_ENV=dev` answers as at `1e97ba9`.
- **Env-gate proof:** `artifacts/proofs/endpoints_env_gate_proof.log` is byte-identical. It observes the dev-runner factory's request-time gate under `APP_ENV=prod`; the production mount is proven by `tests/http/test_endpoint_catalog.py`.

## 6. Release refresh and convergence (commit `176de33`)

Run in the implementation branch's working tree after the source commit, under closed rails (plan §9).

| Item | Result |
| :- | :- |
| Pass 1 (steps 2 to 10) | 37 commands, all exit 0; sanity `summary:PASS` |
| Pass 2 (steps 3 to 10) | 34 commands, all exit 0; sanity `summary:PASS` |
| Byte stability | the two `git diff HEAD` patches are identical (SHA-256 `429c63c942a7d3e3e20f0d68cac5421e250180a36325d01b2ed049f545ea1554`); after each pass 56 paths differ and none is untracked |
| Changed set | the 56 paths of plan §9 exactly: the manifest, the `FROZEN_OPEN_ABBA_SHA256` line, 27 evidence primaries and their 27 path proofs, the Index and the Mirror |
| `release_id` | `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, 45 members, `1.3.0`, `built_at_utc` unchanged. Five manifest rows change: the five members. Equal to the rehearsal value, because the member bytes are the rehearsal's |
| Open-rails proof | `audit/gates/determinism/open_rails_abba.json` SHA-256 `e8a47d53b4d9a145ebfc95163a85252c15a4fbddb12dc9dea380662aaa1cb73c`. `FROZEN_OPEN_ABBA_SHA256` changed from `9949ddf5…` to it by one anchored replacement |
| Labels | Mirror 620 rows; 27 carry `77204764…` and none carries `2f18a5eb`; the two purity-report rows carry no `notes` (LR-O3 (c)) |
| Step 11 sweep | `2f18a5eb\|9949ddf5` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256` and `manifest_post.sha256`, and in `docs/` outside `docs/ephemeral/` and `docs/pfcanon/`: no hit |
| Against the rehearsal convergence | only the `generated_at_utc` values of the four engine-core primaries, the path proofs' capture fields, and the Index and Mirror rows derived from them differ |

## 7. Local validation (plan §10 and §12)

| Check | Where | Result |
| :- | :- | :- |
| Pre-cut tests (plan §10 step 6): the affected directories and the two analyzer test files | implementation tree, source applied | 2,497 passed, 3 skipped, 2 xfailed, 17 failed. These are the same 17 stale-manifest refusals plan §4.3 lists, and the 267 `test_s19_*` cases passed |
| Negative controls NC-01 to NC-18 | scratch copy before the cut; detached worktree of `176de33` | each fails exactly as plan §4.3 records, both times; the files were restored byte for byte |
| Classifier (`8170cd8` → `176de33`, `pull_request`) | detached worktree | `reason=selected_lanes`; 77 paths; lanes product, compat, db, rails, evidence and release; `qa=false`; 39 changed-test targets |
| Changed-tests step, as CI runs it (isolated worktree, `PYTHONPATH`) | detached worktree | 1,874 passed; clean tree |
| Product lane | detached worktree | ordering `--check` exit 0; 77 passed |
| Compat lane | detached worktree | `check_cli_help.sh`, serializer guard and emitter proof exit 0; 119 passed, 3 skipped, 2 xfailed |
| Db lane | detached worktree | `check_direct_db_contract.py` exit 0; 268 passed |
| Rails lane | detached worktree | `RAILS_GATE_EVIDENCE_OK`, `RAILS_JOB_DEFINITIONS_OK`; 138 passed |
| Evidence lane | detached worktree | the seven checks exit 0; 130 passed |
| Release lane | detached worktree | recompute exit 0; 79 passed in the isolated worktree; attestation build with `--require-clean`, then `--verify`: exit 0 and exit 0; `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `source_commit` `176de338d9161efb3268184668bd47029e6a4825`, `source_commit_exact` true |
| Full `tests/` sweep | second detached worktree, own venv | 5,185 passed, 3 skipped, 2 xfailed, 0 failed (1,031.6 s, 20:06:16Z to 20:23:28Z), exit 0; clean tree; `XDG_STATE_HOME` left empty. That is `1e97ba9`'s 4,918 plus the 267 new cases |
| Instruction §5.6 read-only checks | detached worktree | Admission `77204764…`, 45, `1.3.0`. Ten evidence and release checks, seven `--check`s, five frozen-family checks and three config and cutter checks, plus the sanity pipeline: 27 × exit 0, sanity `summary:PASS`, `first_failed_stage:NONE` |
| Pre-existing failures | detached worktree | `generate_hde_epic037_v2_to_compat.py --check`, `generate_hde_epic037_bg_resolve.py --check` and `generate_hde_epic036_bg_resolve_route_policy.py --check` exit 1, with output byte-identical to `1e97ba9` (OBS-W5-4, OBS-P4-3). Not caused by this unit |
| Convergence check (§9 steps 3 to 10 again) | detached worktree | 34 commands, all exit 0; no byte changed |
| Probes (instruction §10, gaps 1 to 3) | detached worktree | as §5; gate matrix (`POST /internal/dev/sampler`) served only for exactly `dev`, `test`, `local`, with `DEV`, ` dev`, `Dev`, `TEST `, `prod` and empty refused |
| Hermeticity | detached worktree | the 13 host modules: 915 passed; with `APP_ENV` unset 915 passed; with `tests/adapter/test_jsonschema.py` first 918 passed and 2 xfailed (that file's) |
| Governed analyzers (P-13) | full sweep and product lane | `tests/evidence/test_architecture_snapshot.py` and `tests/evidence/test_hdapi_v2_contract_inventory.py` pass |
| CI guards (P-15) | full sweep and rails lane | `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py` pass with no registry change |

Not run here: hosted CI (it starts with the pull request; PR-35 verifies the current head), the qa lane (not selected), and any live vendor, production or database call. The EPIC030 generator was never run.

## 8. Requirement → proof (plan §11)

| Item | Proof |
| :- | :- |
| S19 review recorded / acceptance (1) | the S19 record: 49 per-file lines with blob IDs; head confirmation at `8170cd8` (§2) |
| S19 findings dispositioned / acceptance (2) | nine fixes with regression tests and negative controls; seven routed findings with owner, reason and evidence (S19 record §4 and §10) |
| Exclusion 6 / acceptance (3) | no `requirements*.txt`, `pyproject.toml`, workflow or classifier change; no scanner run |
| Lanes and release identity / acceptance (4) | admission at `176de33` (`1.3.0`, 45, `77204764…`), second-pass byte identity and recompute exit 0 hold locally (§6, §7). Hosted CI on the exact head with every selected lane green and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` is PR-35's to verify |
| AD-4 (gaps 1 to 4) | `test_s19_production_mount_*`, `test_s19_every_other_posture_mounts_the_blueprint_unchanged`, `test_s19_dev_admin_gate_*`; NC-04, NC-06, NC-17 and NC-18; the probes (§5). Gap 4 is recorded as O-01 |
| PF27 route-policy statement | S19 record §9; route policy unchanged |

## 9. Routed findings (contract F-4), classifier (F-5) and the S19 record (F-2)

- **Routed findings:** S19-R01 to S19-R07, each with its owner, reason and evidence in S19 record §4. The Product Owner owns all seven; they are not decided here.
- **Classifier (F-5):** no registration added. WU-PR-06 has none to read.
- **S19 record (F-2):** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`. Each fix carries its Live QA class and surface in record §4, and each routed finding its owner.

## 10. Stale documents, observations and carried items (not in this pull request)

- **Stale canon passages:** HDE Architecture §3.3, §3.5 and §3.8.1; HDE Users Guide §1.1; HDE Mechanics Guide §34; and the "never fires" wording of addendum 2.7 AD-4 item 4 (O-01). They are canon doc-delta candidates for the Product Owner (plan §19).
- **No change needed:** `docs/server/reader_v1.md` and `docs/CLI_commands.md`. Repository documents that describe the production route set or the root helpers belong to WU-DOC-01 through the IA.
- **Observations:** O-01 to O-25 (owner: the IA, who routes them, or the owner each row names) and X-01 to X-04 (S19 record §7 and §8).
- **Carried, as plan §19 lists:** OBS-W4-1 and OBS-W4-3 become S19-R01 and S19-R02; LR4-O1 is X-01; OBS-P3-17 is X-02. OBS-17 is a qa-lane risk that the classifier did not select. O-6 (`ruby` on runners) stays with PR-35 if a hosted log shows it.

## 11. In-flight decisions

NONE. The source commit equals the plan's companion diff byte for byte; the refresh, the records and the validation follow plan §9, §10, §12 and §14.

## 12. PR_REMOTE_ACTION_LEDGER

| Time (UTC) | Action | Evidence |
| :- | :- | :- |
| 2026-10-18, before any write | open pull requests listed; #655 read | none open; #655 merged 19:43:48Z (`58917cd` → `8170cd8`) |
| before 20:06 | local commits `d0f25b6` (source) and `176de33` (convergence) | §4, §6 |
| after the lanes | push 1 of `d0f25b6` and `176de33` to the designated branch, without a pull request; durability checkpoint | remote head read back `176de338d9161efb3268184668bd47029e6a4825`. CI's `push` trigger covers `main` only, so no run started |
| 20:34 | local commit `173bf97` (S19 record); push 2 | remote head read back `173bf973f5298c81a87956da16e1e07ff5b54a1b` |
| 20:35:33 | pull request #656 opened (base `main` `8170cd8`, head `173bf97`, not draft) | GitHub read back: open, 3 commits, 78 changed files, `mergeable_state` `unstable` at 20:35:46Z while checks were pending |
| after 20:38 | push 3: the commit that adds this record (`docs/ephemeral/` only) | read back in §17. The run for `173bf97` is superseded under the workflow's `cancel-in-progress` rule for pull requests; whether GitHub cancelled it is for PR-35 to read, not claimed here |
| — | review reads, finding dispositions, CI results | none in PR-30; PR-35 owns them |

Remaining useful local action in PR-30: none. Next evidence action, PR-35's: subscribe to #656, read the Codex code review and threads, and verify CI on the current head.

## 13. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Codex code review of #656, review resolution, hosted CI on the current head, mergeability | PR-35 |
| A correction that changes a member restarts plan §9 at step 2; one that changes an evidence primary restarts at step 3b. Either needs the attestation again (plan §20) | PR-35 |
| A correction must keep the F03 hook's shape (plan §7.3, RK-8) and add no test module or registration (PD-13, P-15) | PR-35 |
| S19-R01 to S19-R07 | Product Owner |
| O-01 to O-25, X-01 to X-04 | IA, or the owner each row names |
| Stale canon passages (§10) | Product Owner |
| Merge | Nathan / Product Owner (manual) |
| GCFPE prompt-use persistence (§17) | Product Owner (pending, non-gating) |

## 14. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged: CR-1 to CR-8, all decided (plan §18). There is no new entry. PR-30 found no reading in conflict with canon; the design meets the canon plan §18 names.

## 15. Nonclaims

- The review is implementation-side assurance, not QA and not acceptance (Plan v1.1).
- No fixed surface was run live, and no live vendor, production or database call was made.
- No QA verdict, acceptance, Ops, deployment, PF09 movement or closure is claimed.
- No conformance is claimed beyond the fixes made.
- No canon was edited and no PF10 addendum was created. The routed findings are not decided.
- No merge readiness is claimed: hosted CI and review have not been read.

## 16. TypeSafe reading and surface advice for the receiving session (PR-35, WU-PR-05)

PF10 addendum 2.1 governs. The script ran once, before this record was saved, with the step label "PR-35 — Resolve PR Reviews and Reach Merge Readiness (HDE-CRD-0002 WU-PR-05)" and session kind `review`.

**Action sent (v8.2):** "Continue, in a new dedicated session, one already published but not yet reviewed pull request that implements nine small security fixes from an approved and prototyped plan (eight hand-edited source files, 267 new test cases added to 13 existing test modules, and 56 owner-regenerated governed evidence paths from a same-version release re-cut), following the review-resolution task list: retrieve the automated code review threads and hosted CI results, fix each valid in-scope finding locally with retests (re-running the fixed twelve-step evidence convergence and its byte-stability pass only if a release member changes), push coherent corrections, verify current-head CI on every selected lane and mergeability, and write a result record. No live vendor, production or database call; the Product Owner merges and an independent lineage review follows."

**The reading, as the skill printed it:**
- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.23 (confidence 0.81); rung probabilities low 0.00, medium 0.03, high 0.72, extra high 0.25, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 1.00, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 1.00). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.030, Opus 5.5 at high 0.720, Opus 5.5 at extra high 0.250, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-18T20:18:14Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T20:18:14Z; HTTP 200 in 0.46 s; 5508 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.

**Records:**
- The Notion row was not written, as PR-30 directs.
- Nathan's pick for PR-35: not stated.
- Nathan's pick for this PR-30 session: not stated. The reading for PR-30 is in plan v1.0 §22.

**Surface advice for PR-35** (execution surface only):
- **Session.** A new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access to the pull request. At entry it subscribes to the pull request's activity.
- **Environment, if a correction needs local re-runs.**
  - Use Python 3.12 explicitly (`/usr/bin/python3.12` here; the container's default `python3` was 3.13) with CI's install, which needs package-index access for `pip install`, and `-e .` of the worktree under test.
  - Put `ruby`, `bash` and `curl` on `PATH`.
  - Unset the vendor, database and GitHub keys the container sets (§2 lists the names).
- **Run times observed in this phase** (4 CPUs, with runs concurrent): full `tests/` sweep about 17 minutes; changed-tests step about 5; evidence lane about 9; one refresh pass about 3 minutes; attestation build about 2.
- **Discipline.**
  - Run any re-convergence in the branch's working tree, and only after member edits are committed.
  - Run every other check that can write tracked files in a detached worktree.
  - Pass the classifier full SHAs; it refuses abbreviated ones.
  - Run the attestation before any push that changes a member or an evidence primary.
- **Access.** No live vendor, production or database access is needed.

## 17. Prompt-use provenance (GCFPE_PROMPT_USES) and read-back

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-05 / PR-30 / result 1 (plan cycle 1), version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-05 (S19) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08Z). Receiver contract read: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-05 PR engineering session / PR-30 |
| capture time | 2026-10-18T20:38:00Z |
| execution identity | https://claude.ai/code/session_01FtgUXCdmFGLWASrRUWaDjc |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan 1 (plan v1.0 §23) |
| pull request and commits | amthorn78/glow-hdengine-v2#656 (open, base main, not draft); `d0f25b6`, `176de33`, `173bf97`, and this record's commit |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

Read-back: this record and the S19 record are read back from the remote branch after push 3 (identity, body, version, state, repository path and next consumer).

## 18. Next phase

PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e).
- **Session:** its own new dedicated session (`session_disposition: NEW_DEDICATED`), entered from this phase's handoff, which Nathan pastes.
- **Continuity:** it continues amthorn78/glow-hdengine-v2#656 under the original Proceed for plan v1.0. It shares this phase's work unit, workspace, branch, pull request, instruction, plan, primary skill and recovery lineage.
- **Inputs:**
  - this record and the S19 record;
  - plan v1.0 and its companion diff, and instruction v1.0;
  - the immutable Specification v1.1, Implementation Plan v1.1 and review v1.1;
  - PF10 as resolved at entry (addenda 2.3, 2.5 to 2.9).
- **Branch and head:** PR-35 verifies both at entry from the pull request.

## Canon relied on

Read on `main` at `8170cd8`; `docs/pfcanon/` is unchanged since `86e002c`.

| Topic | Sources |
| :- | :- |
| Phase authority, Proceed, results and handoff | PR-30 — PR Implementation Proceed — 100926.1 (read in full); PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (receiver contract, read in full); HDE Governance §9.1.1 and §9.1.3 |
| Overlays | PF10-HDE-Build-Notes v13.6: addenda 2.1 (§16), 2.3, 2.5 to 2.9 as instruction v1.0 and plan v1.0 apply them |
| Implementation, refresh and tests | plan v1.0 §7 to §12 and its "Canon relied on" (HDE Architecture §1.3, §3.2, §3.3, §3.5, §3.8.1; HDE-CLI-API-Vendor-Ref §3.3, §5.2, §5.4, §5.5, §5.11, §5.12, §7.1, §8; HDE Governance "Dev/admin APP_ENV gating"; HDE Math Spec §5.4.3; HDE Mechanics Guide §25.6; HDE Users Guide §1.1, §6.4, §7.6); instruction v1.0 §5.6, §5.8, §10, §11 |
| Release identity | `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; Implementation Plan v1.1 §10 |
| Operative rules | `AGENTS.md` (closed rails, redaction, sole Index/Mirror writer, no hand edits, pytest readiness, PR descriptions, EPIC030 hazard); `.github/workflows/ci.yml` (lanes, as run in §7) |
