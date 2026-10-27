---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-08-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
result_state: MERGE_PENDING (historical pre-merge evidence; the Product Owner merges manually)
phase: PR-35 (review resolution and merge readiness), dedicated session
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; preserved unchanged)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md (v1.0; landed by #685)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0.md (v1.0; landed by #686 as 977a9c7)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-7)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, with Specification delta 01
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md; delta approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS (as the plan's front matter states; no new overlay)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d; the only PF10 file on main at 977a9c7; read as provenance)
pf10_addendum_paths: as the plan's front matter; none added
proceed: Nathan / Product Owner, PR Implementation Proceed for exactly plan v1.0 (unchanged; no second Proceed)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: NEW_DEDICATED
sessions: PR-30 https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA; PR-35 https://claude.ai/code/session_01VASdh3cjEKqEVYa35EwCEn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15.569Z, read in full)
primary_skill: glow-hde-pr-development 1.4.0
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/687 (open; mergeable_state clean)
branch: claude/awesome-einstein-ig69r1 (the PR's branch; pushed to by this session under PO-35-1, §7)
base: origin/main 977a9c7f13db9302d33670494f77549cdbf6d5dd (#686)
reviewed_and_ci_tested_head: bf32d20aaa17a36be8d45b6f98c4ebac533a2952
implementation_commit: 9b93cf0e36121260ceb694cea91fa3546863ca4d (unchanged; no PR-35 correction)
created_at: 2026-10-21T23:49:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged; no new entry
---

# HDE-CRD-0002 WU-PR-08 — PR implementation result v1.1 (PR-35, MERGE_PENDING)

## 1. Result

**MERGE_PENDING. Ready to merge:** [amthorn78/glow-hdengine-v2#687](https://github.com/amthorn78/glow-hdengine-v2/pull/687).

- **Head:** `bf32d20` is the reviewed and CI-tested head. This record's commit adds only this file under `docs/ephemeral/`. That prefix is CI-exempt, and Markdown is outside Codex review scope.
- **Mergeability:** `clean`, against base `main` `977a9c7`.
- **Merge:** the Product Owner's manual action. No agent merges, enables auto-merge or schedules a merge.
- **Hosted CI on this record's own commit:** it starts automatically, because the PR's whole diff includes the classifier. This session observes it through the PR subscription and reports it to the Product Owner. If it fails, a later record withdraws this `MERGE_PENDING`.

This is historical pre-merge evidence. It does not claim a merge, a QA verdict, acceptance, Ops, deployment or closure.

## 2. Merge-readiness predicates (glow-hde-pr-development; PR-35 "Genuine merge-readiness gate")

| Predicate | Evidence |
| :- | :- |
| Approved implementation scope complete | Plan v1.0, delivered at PR-30 (result v1.0). The PR's diff outside `docs/ephemeral/` (`977a9c7..bf32d20`) has sha256 954a7881fbdcf688826bdf41f4da593fc7ea9430529709c1e37cfa3024745acb. That equals the plan's companion diff, byte for byte (§4 row 5) |
| Every applicable current-head review read; substantive findings resolved | Codex code review of `9b93cf0`, completed 2026-10-21T23:24:04Z, trigger "PR opened": no findings (summary comment [6328780869](https://github.com/amthorn78/glow-hdengine-v2/pull/687#issuecomment-6328780869), `has_any_findings: false`, `has_unresolved_findings: false`). `9b93cf0..bf32d20`, and this record's commit, change only `docs/ephemeral/` Markdown. `git diff 9b93cf0 bf32d20 -- . ':(exclude)docs/ephemeral'` is empty, so the review covers every in-scope byte of the head (§3) |
| No required review thread unresolved | 0 review threads; 0 formal reviews; 1 issue comment (the Codex summary) |
| Required current-head CI passes | Run 39693139601, job 119544161876, `test`: success on `bf32d20`, 23:24:26Z to 23:45:13Z. All seven lanes ran, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§5) |
| Local required tests pass on the current head | Plan §12 items 1 to 5, re-run on `bf32d20`: all pass (§4) |
| Remote head equals the verified candidate | PR head `bf32d20aaa17a36be8d45b6f98c4ebac533a2952`, read at 23:45Z; the local checkout and clone are at the same SHA |
| PR open and mergeable; no blocking conflict | `state: open`, `draft: false`, `mergeable_state: clean`. No commit statuses; `test` is the only check run (no Claude Approvals check) |
| No unresolved material rescope, dependency or repository conflict | None. No finding, so no rescope. Merge order: none (the plan, #686, is on `main`) |
| Ledger and final checkpoint saved and read back | this record (§8) |

## 3. Review findings and dispositions

- **Codex code review:** one completed round, on `9b93cf0`, with no findings. So no P1 exists to fix or decline (PF10 addendum 2.14), no finding needs a disposition under addendum 2.11 rule 7, and rule 8 (a repeated finding class) does not arise.
- **No re-request.** `bf32d20` and this record's commit add only `docs/ephemeral/` Markdown. That is excluded from Codex review by `AGENTS.md` "Code review guidelines" and by its "Code review scope — CI-exempt paths are out of scope" rule. The in-scope bytes are those reviewed on `9b93cf0`, so a second request would only re-review the same three files.
- **Codex security review:** not part of the review chain (PF10 addendum 2.3 rule 2). Its absent row in the summary is no gap, finding or waiver need.
- **This session's own read** of the three-file diff against the code (`adapter/wsgi.py` lines 11–51, `adapter/app.py`, `adapter/http_reader.py` lines 1312–1325, `Procfile`, `engine/providers/vendor_http_hdapi.py` lines 50–67): every corrected statement matches plan §6. No defect found.

## 4. Local checks on `bf32d20` (plan §12 items 1 to 5)

Throwaway clone of `bf32d20` in the session scratchpad. CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`, the clone installed editable); pytest 8.4.2. `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, the probes setting `APP_ENV` per runner). Vendor, database and GitHub keys were not passed to any child. Nothing else ran in the clone while each step ran, and `git status --short` was empty after each step.

| # | Check | Result (2026-10-21, UTC) |
| :- | :- | :- |
| 1 | `ci/checks/classify_ci_changes.py --base 977a9c7… --head bf32d20… --event-name pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=4;lanes=product,compat,db,rails,evidence,qa,release`; 166 changed-test targets (23:27:50Z) |
| 1 | `classify_paths(['.env.example'])` (acceptance 4) | `reason='documentation_only'`, every lane false, no `CI_CHANGE_SURFACE_UNCLASSIFIED` |
| 2 | `tools/ci/prepush_check.py --base 977a9c7… --head HEAD --path .env.example --path docs/ADAPTER_009.md --path ci/checks/classify_ci_changes.py lanes membership build-notes` | `PREPUSH_CHECK_RESULT: PASS lanes=PASS membership=PASS build-notes=PASS`; not-member ×3; PF10 v13.7.1 eab61385…; "repository unchanged"; exit 0 |
| 3 | Admission (acceptance 3): `load_active_mechanics_bundle()`; `_manifest_release_id()`; `scripts/release_id_recompute.py --check-manifest-only` | ok; `1.3.0`, 45 members; `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (= base); recompute exit 0 (to 23:27:58Z) |
| 4 | `pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py` | 138 passed in 25.61 s, exit 0 (to 23:28:24Z) |
| 4 | Plan §13.2 set (nine test files) | 791 passed, 2 xfailed in 170.87 s, exit 0 (to 23:31:15Z) |
| 5 | §6 map on the head | the PR diff outside `docs/ephemeral/` equals the companion diff, sha256 954a7881… (above); the statements were re-read against the code (§3) |
| 5 | Live probes, 23:31:36Z to 23:31:39Z | below |

| Runner | Listener | `/internal/version` | `/internal/readyz` | `/internal/healthz` |
| :- | :- | :- | :- | :- |
| `APP_ENV=dev python -m adapter.http_reader`, `PORT` unset | `127.0.0.1:8000` | 200 | 404 | 404 |
| `APP_ENV=dev PORT=8141 scripts/dev_start_reader.sh` (banner "Binding port 8141 … (host=127.0.0.1)") | `127.0.0.1:8141` | 200 | 404 | 404 |
| `APP_ENV=dev flask --app adapter.app run --port 5011` | `127.0.0.1:5011` | 200 | 200, body `{"ok":true,"schema":"v1"}`, no `X-Toggles-SHA` | 200 |
| `APP_ENV=prod python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:8142 --workers 2 --threads 4 --timeout 30` | `0.0.0.0:8142` | 200 | 404 | 404 |

The listeners were read from `/proc/net/tcp` (`ss` is not installed in this container). Each row matches plan §6 and §13.3.

The full local replay (§12 item 6) was not repeated. Plan §12 assigns PR-35 items 1 to 5 only, and those only after a correction; none was made. Hosted CI ran the real workflow on the head (§5).

## 5. Hosted CI proof on `bf32d20`

Run 39693139601 (job 119544161876), `ci` / `test`: **success**. The whole job log was retrieved (920 lines, `original_length` 920) and scanned in full for step headers, outcomes, test counts, errors and warnings. The classification, the final-step outcomes and the last 40 lines were read directly.

| Item | Value |
| :- | :- |
| Image | `ubuntu-26.04`, version 20261018.168.1; runner 2.338.0 |
| `HEAD_SHA` / `BASE_SHA` | `bf32d20aaa17a36be8d45b6f98c4ebac533a2952` / `977a9c7f13db9302d33670494f77549cdbf6d5dd` |
| Classification | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=4;lanes=product,compat,db,rails,evidence,qa,release` |
| Changed tests | 4,521 passed, 2 skipped |
| Product, compat, db | 77; 119 passed, 3 skipped, 2 xfailed; 269 passed (5 warnings) |
| Rails | four runs: 120, 113, 155 and 138 passed |
| Evidence, qa, release | 134; 488; 79 |
| Final step | every outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| Warnings | one: the Node.js 20 deprecation notice for `actions/checkout@v4` and `actions/setup-python@v5`. Not this PR's, and not a failure |

The `test` run on `9b93cf0`, triggered by PR-30's first push, was superseded by `bf32d20` under the workflow's pull-request cancellation (result v1.0 §6). It is not evaluated here.

## 6. Acceptance state (Plan delta 01, P-7)

| Acceptance | State on `bf32d20` |
| :- | :- |
| (1) `.env.example` has a `GEO_API_KEY` entry and nothing else changed | Met: one added line, `GEO_API_KEY=changeme` (companion diff equality) |
| (2) readiness section as implemented, naming the app; port statements match the runner and `Procfile` | Met: plan §6 R-1 to R-4, P-1 and P-2; code re-read (§3); probes (§4) |
| (3) admission `1.3.0`, 45 members, base `release_id` | Met locally (§4 row 3) |
| (4) `.env.example` alone classifies | Met locally (§4 row 1) |
| (5) all seven lanes green on the exact PR head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | Met on `bf32d20` (§5). This record's own commit gets its own run (§1) |

These are implementation-validation states for PR-40 to check. They are not acceptance, and not a QA verdict.

## 7. In-flight decisions and Product Owner directions

**In-flight decisions:** NONE. No correction was made; the PR's code is PR-30's `9b93cf0`, unchanged.

**Product Owner directions in this phase:**

| ID | Direction | Effect |
| :- | :- | :- |
| PO-35-1 | Asked: "May I push this session's result record (docs/ephemeral/ only, no code) to claude/awesome-einstein-ig69r1?" Answered (Nathan, 2026-10-21, between 23:28:19Z and 23:31:36Z by the session clock): "Push to PR branch (Recommended)" | This session's harness names another branch, `claude/inspiring-pascal-2z7tep`; that branch was not used. The record is committed on the PR's branch, so the work unit keeps one branch and one PR (GCF-17 continuity) |

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.0 §6)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 7 | ~23:25 | `subscribe_pr_activity` for #687 | confirmed by the tool result; `subscription.created` queued 23:25:31Z |
| 8 | ~23:25 | Read #687: details, reviews, review threads, issue comments, check runs, commits | head `bf32d20`; 0 reviews; 0 threads; Codex summary (no findings on `9b93cf0`); `test` in progress; 2 commits |
| 9 | 23:27:50 to 23:31:39 | Local checks §4 on `bf32d20` | all pass; clone clean |
| 10 | 23:28 to 23:31 | PO-35-1 (§7) | push to the PR branch authorized |
| 11 | 23:33:05 | Safety-net check-in `trig_0167bFDgNL8RWusvjok3Pog4`, due 2026-10-22T00:24:00Z | armed |
| 12 | 23:45:13 to 23:45:30 | Run 39693139601 `test` completed; `check_suite.completed` delivered 23:45:22Z; PR re-read | success; `mergeable_state: clean`; no new comment, review or thread; no commit status |
| 13 | ~23:46 | Job log retrieved and scanned in full (§5); TypeSafe v8.2 reading for the PR-40 handoff (§9) | read |
| 14 | next | Commit and push this record (`docs/ephemeral/` only); read back the remote head; add the hosted CI result to #687's "Checks run"; observe CI on the record's commit through the subscription; the conditional PR-40 handoff goes to the Product Owner | — |

Remaining useful local action: none. Next evidence action: hosted CI on this record's commit.

## 9. TypeSafe reading for the PR-40 handoff

Run once, with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review`, label "PR-40 — HDE-CRD-0002 WU-PR-08". The reading, as the skill prints it:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.76 (confidence 0.61); rung probabilities low 0.00, medium 0.41, high 0.42, extra high 0.17, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.97, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.398, Opus 5.5 at high 0.407, Opus 5.5 at extra high 0.165, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.012, Sonnet 5.5 at high 0.013, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between medium and high. Sent 2026-10-21T23:46:25Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T23:46:25Z; HTTP 200 in 0.51 s; 5514 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between medium and high.
- **Action text sent:** "Independent post-merge lineage review of one already-reviewed pull-request work unit, HDE-CRD-0002 WU-PR-08 (requirements S16 and S17): check against the repository that merged pull request #687 (3 commits; three existing files changed by about 20 lines: one placeholder key in an environment template, six corrected readiness and port statements in an operator document mapped line by line in the plan, one entry in a CI change classifier; plus three record files) delivered the work unit's five acceptance items from its existing instruction and plan; one Codex review round with no findings, no Product Owner design decisions in the review phase, hosted CI green on all seven lanes. There is no live run of new code against a provider, and QA and the change's close gate follow as later independent gates."
- **Records.** The Notion row was not written (the PR-35 prompt's handoff rule; PF10 addendum 2.1). Nathan's pick for PR-40 is not stated. His pick for this PR-35 session is not stated either; its reading is result v1.0 §8.

**Surface advice for PR-40:**
- A Claude Code session that Nathan creates, with `amthorn78/glow-hdengine-v2` checked out at `main` after the merge.
- GitHub read access to #687, its run 39693139601 and the run on this record's commit, and its Codex summary.
- Closed rails through `env -i`, because the container sets vendor, database and GitHub keys.
- A CPython 3.12 venv with CI's install, if PR-40 re-runs the classifier, admission or the §13.2 tests.
- No live vendor, production or database access is needed. Apart from its own output artifacts, the review writes nothing to the repository.

## 10. Conditional PR-40 handoff

Use it only after the Product Owner has manually merged #687, and only where no `MERGE_OBSERVED` result was returned for that merge. The handoff is reproduced in this session's final response.

- **This record's `MERGE_PENDING`:** historical pre-merge evidence for head `bf32d20`.
- **The merge:** the Product Owner's own later assertion.
- **PR-40:** verifies the actual merged state and the landed lineage independently. That includes:
  - the §6 statement map on the merged `main`;
  - the PF10 addendum 2.14 check that no P1 on a real input was declined (none was raised).

If this subscribed session observes the merge, it returns `MERGE_OBSERVED` with the same PR-40 handoff. Once either has been pasted, the other is void.

## 11. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Merge of #687 | Product Owner | ready (§1) |
| Hosted CI on this record's commit | this session, through the subscription | pending at writing; reported to the Product Owner; a failure withdraws this `MERGE_PENDING` in a later record |
| F-1, override guard wiring (plan §17) | the whole-change IA, through PR-40 | unchanged; a later-change candidate for the Product Owner |
| F-2, further stale statements in `docs/ADAPTER_009.md` (plan §17, §18) | WU-DOC-01, through PR-40 | unchanged |
| Carried items, plan §18 (OBS-P4-5, OBS-P4-7, O-19, business cases for WU-DOC-01 and WU-OPS-01) | as plan §18 states | unchanged |

**Nonclaims:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release cut; no change to `/internal/readyz`'s behavior. This record is not intended to support a later PF-canon drain and recommends no status change (HDE Governance §2.0.19, the "Pre-drain status distinction" and "Later-drain update statement" bullets).

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-08 / PR-35 / result 2 (v1.1) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-PR-08 (S16, S17) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15.569Z) |
| role/stage | dedicated WU-PR-08 PR-35 session / PR-35 |
| capture time | 2026-10-21T23:49:00Z |
| execution identity | https://claude.ai/code/session_01VASdh3cjEKqEVYa35EwCEn |
| inherited usage | result v1.0 (PR-30, session_01QezXHuju1GXwpubx7zDvTA); plan v1.0 (PR-20, same session); instruction v1.0 (PR-10, session_01U3QLYTkfUepeRbSGZNPj9N) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Canon was read on `main` at `977a9c7`. `docs/pfcanon/` was last changed by `7b763db`, and PF10 is v13.7.1.

| Decision topic | Sources and sections read | How it governs here |
| :- | :- | :- |
| Phase authority, results, readiness gate, ledger, checkpoints, handoff | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, read in full; glow-hde-pr-development 1.4.0, read in full | `MERGE_PENDING` only when every gate predicate holds (§2); one Proceed; no merge; conditional PR-40 block |
| Review chain: code review in, security review out | PF10-HDE-Build-Notes v13.7.1, addendum 2.3, read in full | §3: no security review is obtained or waited on; the Codex code review is read |
| Finding disposition, real inputs, repeated class | addendum 2.11, read in full (rules 4 to 8) | no finding; rules 7 and 8 do not arise |
| P1 findings | addendum 2.14, read in full | no P1 was raised; none declined |
| No cost ceiling | addendum 2.18, read in full | no spend against a ceiling is recorded (rule 5) |
| TypeSafe reading; no model advice | addendum 2.1, read in full | §9: the reading as printed; no recommendation; Nathan picks |
| Review scope of `docs/ephemeral/` Markdown | `AGENTS.md` "Code review guidelines" and "Code review scope — CI-exempt paths are out of scope" | §3: no re-request for Markdown-only commits |
| CI shape and exact-head marker | `AGENTS.md` "HDE-EPIC039 current workflow posture"; `.github/workflows/ci.yml` lines 39–40 (concurrency, pull-request cancellation) and 59–72 (checkout ref; `BASE_SHA`/`HEAD_SHA` from the pull request into the classifier) | §5: one `test` job, seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; a new head re-runs every lane |
| Release identity unchanged | `AGENTS.md` "Release identity" and "HDE-EPIC040 current posture" | §4 row 3 |
| Closed rails, redaction, PR descriptions | `AGENTS.md` "Operating workflow" (closed rails, redaction rule), "PR descriptions" | §4 environment; the "Checks run" update to #687 |
| Status wording and later drain | PF04-Canon-HDE-Governance v2.8.7 §2.0.19, the "Pre-drain status distinction" and "Later-drain update statement" bullets | §11 nonclaims |
| Content canon of the corrected statements | carried from plan v1.0 "Canon relied on" (HDE Architecture §3.4; HDE Mechanics Guide §34; Change Process Guide §0.6.1; Glow Infrastructure §2.4, §10.2; Plan Templates CI lane discipline). Not re-read in this session | No correction was made, so no content decision was taken here |

Search: `git grep -i -E 'MERGE_PENDING|merge.readiness|merge-ready|PR-35' origin/main -- docs/pfcanon/`.
- PF10 had 81 hits; addenda 2.1, 2.3, 2.11, 2.14 and 2.18 govern this phase.
- HDE Governance had one hit, at §2.0.19 (above).
- Glow QA Guide had two hits and HDE Phased Epics one; they concern PF09 drains and accepted units, and do not govern this phase.
- `grep WU-PR-08` across PF10 found passages in addenda 2.6 to 2.12, 2.15, 2.16 and 2.18, and in the index. Of these, 2.18 governs this unit's business case without a ceiling. The plan carries the passages that bind this unit (2.7 to 2.10 at their WU-PR-08 items). The rest concern other units, or prerequisites that 2.18 supersedes.
