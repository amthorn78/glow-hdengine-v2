---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC041-WU-PR-02-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
phase: PR-30
result: PR_CANDIDATE_PUBLISHED
predecessor: none (first result for WU-PR-02)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-02
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-instruction-v1.0.md (v1.0; blob 52faaba5d08857c2cdc391c95360a716260dc187)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 9883d7ae5c27cf76594d935d38e762c21d5c9458; merged by amthorn78/glow-hdengine-v2#795 as abcc13f3)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0)
REMEDIATION_REVIEW_ID: none
RESCOPE_REVIEW_ID: none
proceed: the Product Owner's invocation of PR-30 — PR Implementation Proceed — 102726.1 for exactly PR_IMPLEMENTATION_PLAN v1.0, pasted into this session on 2026-10-28 after #795 merged
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md (sha256 2a43e518f13219569ee3de74f544af9c176a648c8f40c926673671fae164c213; the file the plan read; unchanged on main at abcc13f3; provenance)
effective_baseline: "approved base + applicable PF10 overlays (HDE Build Notes addendum 2.2 as I-7), as the plan states"
prompt: PR-30 — PR Implementation Proceed — 102726.1 (https://app.notion.com/p/4064590a05eb8157bcb9c79a43cefb08; page state 2026-10-27T13:15:20.197Z, read in full during PR-20)
primary_skill: glow-hde-pr-development 1.5.0
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: https://claude.ai/code/session_01Q789u2FkMeZpy3U2W5XTh9 (the dedicated WU-PR-02 PR engineering session; PR-20, then PR-30)
pull_request: amthorn78/glow-hdengine-v2#796 (https://github.com/amthorn78/glow-hdengine-v2/pull/796)
branch: claude/kind-lovelace-30iyf2 (restarted from origin/main abcc13f3 after #795, its plan PR, merged; it carried only that merged commit)
base: origin/main abcc13f33e5cf56128bd27c6d1229373f1ec6b31
tested_source: cc287d8d16c1a62f05654304109d92968e2c645d (the implementation commit; this record's commit adds only this file under docs/ephemeral/)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged from the plan §18; no new entry
created_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES: see §9
---

# HDE-EPIC041 WU-PR-02 — PR Implementation Result v1.0 (PR-30, PR_CANDIDATE_PUBLISHED)

## 1. Result

**PR_CANDIDATE_PUBLISHED:** [amthorn78/glow-hdengine-v2#796](https://github.com/amthorn78/glow-hdengine-v2/pull/796), implementation commit `cc287d8d`, base `abcc13f3`.

* The plan's §6 scope is implemented exactly. The companion diff applied cleanly, and the seven changed or added files are byte-identical to the prototype head `3c8ab627`.
* §11 items 1 to 9 all passed locally (§4).
* No rescope, no in-flight decision, no deviation from the plan.

Not done here, because they are PR-35's: review retrieval and correction, current-head hosted CI, mergeability and readiness. Nathan merges.

## 2. Recovery and baseline

* **Checked before creating anything:**
  * the session checkout and its single worktree;
  * every local and remote branch;
  * open pull requests (none);
  * `docs/ephemeral/` for WU-PR-02 (the instruction, the plan and its diff, all on `main`).
* **The designated branch.** `claude/kind-lovelace-30iyf2` carried only `62e72b78`, the plan's documents commit. #795 squash-merged it as `abcc13f3`; the trees are identical. As a merged plan PR is landed history, the branch was restarted from `origin/main` `abcc13f3` and pushed with `--force-with-lease` against `62e72b78`.
* **`main` against the plan's base.** `main` moved from d09de6ea to abcc13f3 only under `docs/ephemeral/`: `git diff --stat d09de6ea abcc13f3 -- . ':!docs/ephemeral/'` is empty. The §4 baseline therefore holds, and none of the files §9 step 2 names changed.

## 3. Change (commit `cc287d8d`)

| Path | Change |
| :- | :- |
| `scripts/make_compat_determinism_artifacts.py` | import → `adapter.chart_orchestration.load_chart` (1 line) |
| `engine/charts/loader.py` | deleted |
| `tests/adapter/test_chart_orchestration_characterization.py` | deleted |
| `tests/loader/test_load_chart_fixture_only.py` | migrated in place (PD-1, PD-3) |
| `tests/loader/test_loader_logs_keys_only.py` | migrated in place (PD-1, PD-4) |
| `tests/charts/test_chart_loader_import_guard.py` | new (PD-5 to PD-7) |
| `tests/scripts/test_make_compat_determinism_artifacts.py` | new (PD-9) |
| `ci/checks/classify_ci_changes.py` | owner mappings (PD-8) |
| `tests/retired_tests.md` | one row, dated 2026-10-28, the commit's UTC date (PD-10) |

Totals: 9 files, +196 −274. Each changed file's blob equals the prototype's (`git hash-object` against `3c8ab627:<path>`).

## 4. AC-04 record (plan §11, §13.1)

* **Configuration.** Closed rails through `env -i`: `HOME`, `PATH=<venv>/bin:/usr/local/bin:/usr/bin:/bin`, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=<checkout>`. CPython 3.12.3 with CI's install; the editable install was re-pointed at the session checkout. `ruby` was at `/usr/local/bin`.
* **Tested source:** `cc287d8d16c1a62f05654304109d92968e2c645d`. Items 1 and 2 ran on the identical staged tree just before the commit.
* **Actor:** this PR-30 session.
* **Window:** 2026-10-28T20:03:29Z to 20:36:14Z.

| Item | Command (plan §11) | Result |
| :- | :- | :- |
| 1 | Focused set | 56 passed (20:03:29Z); status showed only the staged change |
| 2 | Generator from a temporary CWD; `git diff --exit-code HEAD -- artifacts/compat/` | exit 2, stderr `compat_public not implemented`, 0 files; compat unchanged |
| 3a | Guard on base `abcc13f3` (only the guard file added; throwaway clone) | 2 failed, 2 passed. Flagged exactly the five files: `engine/charts/loader.py` (`definition _call_legacy`, `name _call_legacy`), C-1 (`from engine.charts.loader import`), the characterization file (`import engine.charts.loader`), C-2 and C-3 (`import` and `from` forms) |
| 3b | Planted importers on `cc287d8d` (throwaway clone) | `importlib.import_module("engine.charts.loader")` in `tests/loader/test_validators_strict.py` → 1 failed, naming `string 'engine.charts.loader'`. `from engine.charts import loader` in `adapter/chart_orchestration.py` → 1 failed. Both reverted; clone clean |
| 3c | Migrated C-3 with the clock fixed at 12:34:00Z | 1 passed |
| 4 | `classify_ci_changes.py --base abcc13f3 --head cc287d8d --event-name pull_request` | exit 0; `reason=selected_lanes;paths=9;lanes=product,compat,db,rails,evidence,qa,release`; 170 targets, the same list as the prototype's |
| 4 | The 170 targets as CI's isolated step (a detached worktree of `cc287d8d` in a throwaway clone; 20:05:08Z to 20:12:55Z) | 3,660 passed; `git diff --exit-code` clean; status empty |
| 5 | `prepush_check.py --base abcc13f3 --head HEAD` with the 9 paths, `lanes membership build-notes` | PASS; not-member ×9; admitted `1.3.0`, roster 45, `release_id` 77204764c225…; HDE Build Notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md` 2a43e518…; "repository unchanged" |
| 5 | `prepush_check.py sweep --no-run` (clone at `cc287d8d`) | PASS; `tracked_test_files=220`, `full_validation_targets=170`, `uncovered=0` |
| 6 | `load_active_mechanics_bundle()`; `release_id_recompute.py --check-manifest-only` | `AdmittedMechanicsBundle` returned; exit 0 |
| 7 | Inventory search at `cc287d8d` (plan §13.3 pattern and scope) | 66 files, identical to the prototype head's list; the plan §13.3 dispositions apply unchanged |
| 8 | `git ls-files engine/charts/`; `test -e engine/charts/loader.py` | `engine/charts/pure.py` only; `test -e` exit 1 |
| 9 | `prepush_check.py --base abcc13f3 --head HEAD --full replay` (clone at `cc287d8d`; 20:12:56Z to 20:36:14Z; nothing else touched the clone) | PASS. Steps 01 to 16 SUCCESS: changed tests 3,660 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 160; evidence 134 (720 s); qa 488; release attestation built and verified; final `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "repository unchanged" |

**Limitations.** Local runs only: not hosted CI, not QA, not governed evidence. Exact-head hosted CI on the PR is PR-35's to verify. Items 3 to 9 ran in throwaway clones of the commit, so the session checkout's canon hook could not touch them.

**Business-case measure** (plan §3), as observed locally:
* the loader is absent (item 8);
* the guard passes and fails on planted importers (items 1 and 3b);
* C-1 exits 2 with its stderr from a temporary CWD and writes nothing (items 1 and 2);
* compat bytes are unchanged (item 2);
* the retained-coverage tests pass (item 1);
* the tree is clean after the covering tests (items 1, 4 and 9).

Hosted CI and PR-40 decide it formally.

## 5. In-flight decisions

NONE.

## 6. PR_REMOTE_ACTION_LEDGER

| # | Time (UTC) | Action | Outcome |
| -: | :- | :- | :- |
| 1 | 20:02:58 | `git fetch origin`; read #795 | merged 20:02:00Z by amthorn78 as `abcc13f3`; no open PRs |
| 2 | 20:03 | Branch reset to `origin/main`; diff applied; local commit `cc287d8d` | local only |
| 3 | 20:03 to 20:36 | §11 items 1 to 9 | §4, all PASS |
| 4 | ~20:37 | `git push --force-with-lease=claude/kind-lovelace-30iyf2:62e72b78… -u origin claude/kind-lovelace-30iyf2` | `62e72b78...cc287d8d (forced update)`; `git ls-remote` reads `cc287d8d` |
| 5 | ~20:38 | Opened the one PR | #796, base `main`, head `cc287d8d`; not draft |
| 6 | next | Commit and push this record (`docs/ephemeral/` only); read back the remote head | §8 |

* **Hosted state.** Not read in PR-30. Hosted `test` CI and the Codex review start on the PR's head; PR-35 reads them. No PR subscription was made from this session: PR-35 subscribes at its entry, and a PR's events go to one session at a time.
* **Stale or cancelled runs:** none known.
* **Remaining useful local action:** none.

## 7. Unresolved items and owners

| Item | Owner |
| :- | :- |
| Codex review findings, hosted CI on the current head, mergeability, `MERGE_PENDING` | PR-35 (its own session) |
| The record commit's own head: it adds only this file; hosted `test` runs on it because the PR as a whole selects all seven lanes | PR-35 verifies CI on whatever head is current |
| OBS-6, OBS-7, OBS-8 (plan §16) | As the plan states |
| TI-07 / CCR-1, TI-02, items 9 and 10, FND-005 to FND-007, N-4, DELTA-001 and DELTA-002 | As the plan §17 states |
| Merge | Nathan / Product Owner |

## 8. TypeSafe reading and surface advice for the receiving session (PR-35)

* **Method.** Installed TypeSafe scoring skill, request v8.2, `score_v8.py` run once before this record was saved; session kind `review`; label "HDE-EPIC041 PR-35 WU-PR-02 review to merge readiness". The Notion row was not written.
* **Action sent (v8.2).** "In a dedicated session, take one already published pull request of about 470 changed lines (one legacy Python module and one characterization test deleted, one script import changed, two small tests migrated, a new repository-wide import guard test and a script behavior test added, and a small CI classifier owner-mapping edit), whose implementation was prototyped and locally validated including a full local CI replay, from initial publication to merge readiness: subscribe to its activity, read the automated code review findings and threads, fix any that show a real defect and answer the rest, re-run the local checks before any corrective push, and verify the exact-head CI run of all seven lanes, the remote head and mergeability, then write one result record; a task list exists in the plan; no live run against a provider occurs; the Product Owner merges and a lineage review follows."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.50 (confidence 0.66); rung probabilities low 0.00, medium 0.04, high 0.43, extra high 0.53, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 1.00, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 1.00). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.040, Opus 5.5 at high 0.430, Opus 5.5 at extra high 0.530, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-28T20:05:24Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.67 s; 5515 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high; model by rule: Opus 5.5.
* **Picks.** Nathan has stated no pick for PR-35, and none for this session's PR-20 or PR-30 (their readings are the instruction's §14 and the plan's §20), so none is recorded.
* **Surface advice (PR-35).**
  * Run in a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` that Nathan creates, with GitHub access to #796: reviews, threads, check runs, and pushes to its branch.
  * Subscribe to #796 at entry.
  * For any corrective push, re-run plan §11 items 1 to 6. This needs:
    * CPython 3.12 with CI's install;
    * `ruby` on the `env -i` `PATH` (`/usr/local/bin` here, plan OBS-8);
    * a non-shallow clone;
    * `env -i` closed rails, because the container exports credentials.
  * Observed times: the 170 targets about 8 minutes; the full replay about 23 minutes.
  * No open rails, vendor, Railway, database or Notion writes.

## 9. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage_id | HDE-EPIC041-PR30-WU-PR-02-20261028 |
| change | HDE-EPIC041 (EPIC) |
| specification | `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` (v1.1) |
| work unit | WU-PR-02 |
| ecosystem release | GCFPE-20261027.1 / 102726.1 |
| prompt | PR-30 — PR Implementation Proceed — 102726.1, https://app.notion.com/p/4064590a05eb8157bcb9c79a43cefb08, page state 2026-10-27T13:15:20.197Z |
| role/stage | dedicated WU-PR-02 PR engineering session / GCF-15 to GCF-17 |
| capture time | 2026-10-28 |
| runtime identity | https://claude.ai/code/session_01Q789u2FkMeZpy3U2W5XTh9 |
| inherited usage | `HDE-EPIC041-PR10-WU-PR-02-20261028`; `HDE-EPIC041-PR20-WU-PR-02-20261028` |
| result references | #796; implementation commit `cc287d8d` |
| repository persistence | PENDING: no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md`. Owner: GCFPE management. Non-gating |

## Canon relied on

As the plan's "Canon relied on" (resolved from `docs/pfcanon/` on `main`; `abcc13f3` changes nothing there since d09de6ea). The topics this record decides:

| Topic | Source | How it governs |
| :- | :- | :- |
| Restart of a merged plan branch | Repository session rule for a merged designated branch; `glow-hde-pr-development` "Recover before creating work" (a PR merged under an earlier cycle is landed history) | §2 |
| Result vocabulary and the PR-30/PR-35 boundary | PR-30 — PR Implementation Proceed — 102726.1, "Required result"; `glow-hde-pr-development` "Execute the two-phase engineering lifecycle" | §1, §6, §7 |
| Local checks before publication | The plan §9 and §11; AGENTS.md "Pre-push check" and "Pytest readiness rule" | §4 |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Nonclaims

This record is PR-30's publication checkpoint only. It is not:
* review resolution, hosted CI, merge readiness or a merge;
* a lineage review, QA, Ops, deployment or acceptance;
* PF09 or board movement, a canon change, a PF10 addendum or closure.
