---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-08-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
predecessor: none (first result for WU-PR-08)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md (v1.0; landed by #685)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0.md (v1.0, AWAITING_PO_PROCEED; blob e704695f0c80; landed by #686 as 977a9c7)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-7)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, with Specification delta 01
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md; delta approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS (as the plan's front matter states; no new overlay)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d; unchanged at 977a9c7)
pf10_addendum_paths: as the plan's front matter; none added
proceed: Nathan / Product Owner, PR Implementation Proceed for exactly plan v1.0, given in this session by pasting the plan's PR-30 handoff after #686 merged (2026-10-21)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA (dedicated WU-PR-08 PR engineering session; PR-20 then PR-30)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08.672Z, read in full)
primary_skill: glow-hde-pr-development 1.4.0
base: origin/main 977a9c7 (#686)
branch: claude/awesome-einstein-ig69r1 (restarted from 977a9c7; the remote branch had been deleted after #686 merged)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/687 (open, ready for review)
implementation_commit: 9b93cf0e36121260ceb694cea91fa3546863ca4d (pushed; remote head read back equal before this record's commit)
created_at: 2026-10-21T23:27:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged; no new entry
---

# HDE-CRD-0002 WU-PR-08 — PR implementation result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** Plan v1.0 is implemented exactly: the companion diff applied byte-for-byte to 977a9c7 (`git diff` equal to the diff file), committed once as 9b93cf0, locally tested (§3), pushed, and published as [#687](https://github.com/amthorn78/glow-hdengine-v2/pull/687). This record is the PR's second commit (`docs/ephemeral/` only). PR-35, in its own session, owns review, current-head CI and merge readiness. Nothing here is a merge, QA verdict, acceptance, Ops act or closure.

## 2. Recovery before creating

- No open PR in the repository; no WU-PR-08 implementation branch, worktree or result file; `docs/ephemeral/` held only the decision record, instruction, plan and companion diff.
- The session branch's tip (fa8d7d2) had the same tree as `main` after #686's squash merge; the branch was restarted from 977a9c7. The remote branch no longer existed, so the push created it anew.
- `main` moved from 3715252 to 977a9c7 only by the plan's two `docs/ephemeral/` files, so the plan's §4 baseline and §6 line numbers stand (plan §10 step 2).

## 3. Checks (plan §12; at 9b93cf0, `env -i` closed rails, CPython 3.12.3, throwaway clones, editable install of the clone under test)

| # | Check | Result |
| :- | :- | :- |
| 1 | `ci/checks/classify_ci_changes.py --base 977a9c7… --head 9b93cf0… --event-name pull_request` | exit 0; `reason=selected_lanes;paths=3;lanes=product,compat,db,rails,evidence,qa,release`; 166 changed-test targets |
| 1 | `classify_paths(['.env.example'])` (acceptance 4) | `documentation_only`, no lanes, no `CI_CHANGE_SURFACE_UNCLASSIFIED` |
| 2 | `prepush_check.py … lanes membership build-notes` (3 paths) | PASS; not-member ×3; PF10 v13.7.1 eab61385…; "repository unchanged"; exit 0 |
| 3 | Admission (acceptance 3) | `load_active_mechanics_bundle()` ok; `1.3.0`, 45 members; `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (= base) |
| 3 | `scripts/release_id_recompute.py --check-manifest-only` | exit 0 |
| 4 | `tests/evidence/test_rails_ci_workflow_integration.py` | 138 passed, exit 0 (22:25:05Z to 22:25:34Z) |
| 4 | The plan §13.2 set (6 classifier-owning test files, `tests/adapter/test_jsonschema.py`, `tests/http/test_endpoint_catalog.py`, `tests/scripts/test_dev_start_reader.py`) | 791 passed, 2 xfailed, exit 0 (22:25:34Z to 22:28:29Z) |
| 5 | §6 map on the head | the committed diff equals the plan's companion diff, so §6's corrected texts are the published texts |
| 5 | Live probes (below) | as §6 states |
| 6 | Full replay, `prepush_check.py --base 977a9c7 --head HEAD --full replay`, fresh clone | exit 0; `PREPUSH_CHECK_RESULT: PASS replay=PASS`; "repository unchanged"; all 16 steps SUCCESS (1, 4, 5 excluded and substituted); `ci.yml` sha256 d02021f3… (modelled); `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; changed tests 4,523 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 with the attestation built and verified (22:54:01Z to 23:22:04Z) |

**Live probes (operator's shell, at 9b93cf0):**

| Runner | Listener | `/internal/version` | `/internal/readyz` | `/internal/healthz` |
| :- | :- | :- | :- | :- |
| `python -m adapter.http_reader`, `PORT` unset | `127.0.0.1:8000` | 200 | 404 | 404 |
| `PORT=8133 scripts/dev_start_reader.sh` | `127.0.0.1:8133` | 200 | 404 | 404 |
| `flask --app adapter.app run --port 5001` | `127.0.0.1:5001` | 200 | 200, `{"ok":true,"schema":"v1"}`, no `X-Toggles-SHA` | 200 |
| `APP_ENV=prod python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8134 …` | `0.0.0.0:8134` | 200 | 404 | 404 |

**First replay attempt, superseded.** A replay started at 22:25:05Z in the clone where items 4 and 5 then ran: every step SUCCESS and `status=PASS`, but exit 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION`. The change was a `.pytest_cache/` created at 22:25:20Z in that clone by a subprocess of the concurrent item-4 rails test, not by the replay (which runs in its own copy). The replay was re-run in a fresh clone with nothing else in it (row 6). Lesson for PR-35: run the replay in a clone nothing else touches.

## 4. Acceptance state at publication

| Acceptance (P-7) | State |
| :- | :- |
| (1) `.env.example` has a `GEO_API_KEY` entry and nothing else changed | Met on 9b93cf0: one added line (`GEO_API_KEY=changeme`) |
| (2) readiness section as implemented, naming the app; port statements match the runner and `Procfile` | Met on 9b93cf0: plan §6 R-1 to R-4, P-1, P-2; probes above |
| (3) admission `1.3.0`, 45, base `release_id` | Met locally (row 3) |
| (4) `.env.example` alone classifies | Met locally (row 1) |
| (5) all seven lanes green on the exact PR head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | **PENDING**: hosted CI on #687's current head; PR-35 verifies. Local replay passed (row 6) |

## 5. In-flight decisions

NONE. The plan was applied unchanged; no decision beyond the plan was taken.

## 6. PR_REMOTE_ACTION_LEDGER

| Action | Detail |
| :- | :- |
| Local commit | 9b93cf0 (implementation; 3 files, +11/−10) |
| Push 1 | branch created at 9b93cf0; remote head read back 9b93cf0. An earlier `--force-with-lease` attempt was rejected ("stale info") because the remote branch had been deleted; nothing was written by it |
| PR | #687 created against `main` (not draft) |
| Push 2 | this record (`docs/ephemeral/` only); supersedes push 1's CI run under the workflow's pull-request concurrency cancellation |
| Reviews read | none yet (PR-35) |
| CI | runs triggered by the pushes; none evaluated by PR-30 |
| Remaining useful local action | none for PR-30 |
| Next evidence action | PR-35: Codex code review on the current head; hosted CI on the current head; mergeability |

## 7. Constraints, unresolved items and owners

- PR-35 duties (plan §20): dispose of Codex code review findings under addendum 2.11 rule 7 and addendum 2.14 (a P1 on a real input is fixed; declining a P1 or a security finding goes to the Product Owner first; rule 8 after two same-class rounds); re-run plan §12 items 1 to 5 after any correction, replay in an untouched clone; verify current-head CI (seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability; base-red failures handled as base-red. The Codex security review is not in the chain (addendum 2.3).
- F-1 (override guard wiring) and F-2 (further stale statements): unchanged; the IA through PR-40 (plan §17).
- Merge: Nathan only.
- Nonclaims: no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release cut; no change to `/internal/readyz`'s behavior.

## 8. TypeSafe reading for the receiving session (PR-35, WU-PR-08)

Action sent (v8.2): "Bring one already published, small pull request to merge readiness in a dedicated session: the pull request changes three existing files by about 20 lines (one placeholder key in a three-line environment template, six corrected readiness and port statements in a 230-line operator document, one entry added to a set in a 2,100-line CI change classifier) and was locally tested and fully replayed before publication; read and disposition the automated code review findings under fixed real-input and P1 rules, correct and retest locally if any finding is real, push coherent corrections, and verify that the hosted CI run of all seven lanes passes on the current head and the pull request is mergeable, without merging; no live provider call occurs; a later independent lineage review follows."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.08 (confidence 0.85); rung probabilities low 0.00, medium 0.08, high 0.77, extra high 0.15, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.97, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.078, Opus 5.5 at high 0.747, Opus 5.5 at extra high 0.145, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.023, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T22:29:12Z. Nathan picks the cell.
- **Detail:** session kind `review`; request v8.2 with the installed skill's `score_v8.py`, run once. No flag was printed in the header line. The script's detail line (HTTP time, token counts) was not kept in this session's copy and is not reconstructed; the text was not re-sent.
- **Records.** The Notion row was not written (handoff rule; addendum 2.1). Nathan's pick for PR-35 is not stated. Nathan's pick for this PR-30 session is not stated (its reading is plan v1.0 §21).

**Surface advice:** PR-35 runs as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` that Nathan creates, with GitHub access to #687 (reviews, checks, push) and PR-activity subscription if available. Environment: CPython 3.12 with CI's install (package-index access), `ruby`, `bash`, `curl`, git; closed rails through `env -i` (the container sets vendor, database and GitHub keys); every replay in a clone nothing else touches. Observed times: §12 items 1 to 4 about 4 minutes; full replay about 28 minutes; hosted seven-lane run about 20 minutes. No live vendor, production or database access is needed.

## 9. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-08 / PR-30 / result 1 (v1.0) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-PR-08 (S16, S17) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08.672Z) |
| role/stage | dedicated WU-PR-08 PR engineering session / PR-30 |
| capture time | 2026-10-21T23:27:00Z |
| execution identity | https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA |
| inherited usage | plan v1.0 (PR-20, this session); instruction v1.0 (PR-10, session_01U3QLYTkfUepeRbSGZNPj9N) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

As plan v1.0 "Canon relied on" (read at 3715252; `docs/pfcanon/` unchanged at 977a9c7), plus PR-30 — PR Implementation Proceed — 100926.1, read in full, and `AGENTS.md` "PR descriptions" for #687's body.
