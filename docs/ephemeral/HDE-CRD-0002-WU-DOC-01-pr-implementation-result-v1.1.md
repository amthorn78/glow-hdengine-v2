---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
result_state: MERGE_PENDING (historical pre-merge evidence; the Product Owner merges manually)
phase: PR-35 (review resolution and merge readiness), dedicated session
predecessor: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; preserved unchanged)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; #690)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md (v1.0; landed by #691 as a85067c)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1) with Plan delta 01 v1.1 (P-8)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1) with Specification delta 01
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md; delta approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md
REMEDIATION_REVIEW_ID: none
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; the only PF10 file on main at a85067c; read as provenance)
effective_baseline: approved base + the PF10 overlays plan v1.0 names (addenda 2.3, 2.11, 2.12, 2.14, 2.15, 2.17, 2.18, 2.19, 2.20, 2.21); none added
proceed: Nathan / Product Owner, PR Implementation Proceed for exactly plan v1.0 (unchanged; no second Proceed)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: NEW_DEDICATED
sessions: PR-30 https://claude.ai/code/session_011Y6ExL6PGDrodZqKLRWCHK; PR-35 https://claude.ai/code/session_01PNt1SBXNuFKsPQZ9r1zkEm
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15.569Z, read in full)
primary_skill: glow-hde-pr-development 1.4.0
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/692 (open; mergeable_state clean)
branch: claude/sharp-carson-5ttoho (the PR's branch; pushed to by this session under PO-35-1, §7)
base: origin/main a85067c24679da9ca15b467e87135fb0f962f39e (#691)
reviewed_and_ci_tested_head: 4ef4ad65def4f31a9ca2f52186a687b3bfd92a63
implementation_commit: 1ddc47e30fb6fd53c235389b4ed3d425c4654f4c (unchanged; no PR-35 correction)
created_at: 2026-10-22T02:22:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged; no new entry
---

# HDE-CRD-0002 WU-DOC-01 — PR implementation result v1.1 (PR-35, MERGE_PENDING)

## 1. Result

**MERGE_PENDING. Ready to merge:** [amthorn78/glow-hdengine-v2#692](https://github.com/amthorn78/glow-hdengine-v2/pull/692).

- **Head:** `4ef4ad6` is the reviewed and CI-tested head. This record's commit adds only this file under `docs/ephemeral/`. That prefix is CI-exempt, and Markdown is outside Codex review scope.
- **Mergeability:** `clean`, against base `main` `a85067c`.
- **Merge:** the Product Owner's manual action. No agent merges, enables auto-merge or schedules a merge.
- **Hosted CI on this record's own commit:** it starts automatically, because the workflow's pull-request path filter reads the PR's whole diff, which includes the ten documents. It will classify `documentation_only` again. This session observes it through the PR subscription and reports it to the Product Owner. If it fails, a later record withdraws this `MERGE_PENDING`.

This is historical pre-merge evidence. It does not claim a merge, a QA verdict, acceptance, Ops, deployment or closure.

## 2. Merge-readiness predicates (glow-hde-pr-development; PR-35 "Genuine merge-readiness gate")

| Predicate | Evidence |
| :- | :- |
| Approved implementation scope complete | Plan v1.0, delivered at PR-30 (result v1.0). The PR's diff outside `docs/ephemeral/` (`a85067c..4ef4ad6`) has sha256 `a334c348bf37187dab26a9051e9ee2f7a56692723fc1dd5f6838c8600e60ab63`. That equals the plan's companion diff, byte for byte (§4 row 5) |
| Every applicable current-head review read; substantive findings resolved | Codex code review of `4ef4ad6`, completed 2026-10-22T02:08:33Z, trigger "New commits": no findings (summary comment [6330946962](https://github.com/amthorn78/glow-hdengine-v2/pull/692#issuecomment-6330946962), `has_any_findings: false`, `has_unresolved_findings: false`) (§3) |
| No required review thread unresolved | 0 review threads; 0 formal reviews; 1 issue comment (the Codex summary) |
| Required current-head CI passes | Run 39709656840, job 119597686980, `test`: success on `4ef4ad6`, 02:07:52Z to 02:08:01Z. Classification `documentation_only`, every lane skipped as inapplicable, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§5) |
| Local required tests pass on the current head | Plan §11 items 2 and 3, the items PR-35 re-runs, plus items 4 and 5, on `4ef4ad6`: all pass (§4) |
| Remote head equals the verified candidate | PR head `4ef4ad65def4f31a9ca2f52186a687b3bfd92a63`, read at entry; the local checkout and the throwaway clone are at the same SHA |
| PR open and mergeable; no blocking conflict | `state: open`, `draft: false`, `mergeable_state: clean`. `test` is the only check run (no Claude Approvals check) |
| No unresolved material rescope, dependency or repository conflict | None. No finding, so no rescope. Merge order: none (the plan, #691, is on `main`) |
| Ledger and final checkpoint saved and read back | this record (§8) |

## 3. Review findings and dispositions

- **Codex code review:** one completed round, on `4ef4ad6`, with no findings. The PR changes Markdown only, which `AGENTS.md` "Code review guidelines" excludes from Codex review; plan §11 expected no Codex finding. So no P1 exists to fix or decline (PF10 addendum 2.14), no finding needs a disposition under addendum 2.11 rule 7, and rule 8 (a repeated finding class) does not arise.
- **No human or other review comment** was posted.
- **No re-request.** This record's commit adds only `docs/ephemeral/` Markdown, excluded from Codex review by the same guidelines and by "Code review scope — CI-exempt paths are out of scope". A review of it may run automatically on the new commit ("New commits" trigger); this session reads it through the subscription.
- **Codex security review:** not part of the review chain (PF10 addendum 2.3 rule 2). Its absent row in the summary is no gap, finding or waiver need.
- **Statement correctness:** the landed text is the plan's text, byte for byte (§2 row 1). Plan v1.0 §6 maps each changed statement to the code or record that proves it, and the prototype was tested at PR-20 (plan §12). This session did not re-verify the ~70 statements one by one against the code; that is DOC-20's completion verification on merged `main` (plan §19). No defect was found or raised.

## 4. Local checks on `4ef4ad6` (plan §11 items 1 to 5)

Throwaway clone of `4ef4ad6` in the session scratchpad. CPython 3.12.3 venv with CI's install (`pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, exit 0); `python -m pytest --version` → pytest 8.4.2. `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`). No vendor, database or GitHub key was passed to any child. `git status --short` was empty after the runs.

| # | Check | Result (2026-10-22, UTC) |
| -: | :- | :- |
| 2 | `python ci/checks/check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 (02:18:03Z) |
| 2 | `pytest -q -p no:cacheprovider tests/unit/test_check_agents_md_citations.py` | 57 passed, exit 0 |
| 3 | The six document-reading test files (instruction §5.5) | **1,248 passed, 0 failed**, 73.23 s, exit 0 (02:18:03Z to 02:19:17Z) |
| 4 | `tools/ci/prepush_check.py --base a85067c… --head HEAD lanes build-notes` | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=11;lanes=none`; build-notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md`, 433,368 bytes, sha256 `8ac97232…6d37ff`; `PREPUSH_CHECK_RESULT: PASS`; repository unchanged; exit 0 |
| 4 | `prepush_check.py --head HEAD --path <each of the ten documents> membership` | 10 `not-member`; `1.3.0`, roster 45, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; PASS; exit 0 |
| 5 | `git diff --name-status a85067c 4ef4ad6` | the ten planned documents, all `M`, plus `A` result v1.0 under `docs/ephemeral/` |
| 5 | `git diff a85067c 4ef4ad6 -- . ':(exclude)docs/ephemeral' \| sha256sum` | `a334c348…0ab63`, the plan's companion diff |

The six files are `tests/unit/test_check_agents_md_citations.py`, `tests/unit/test_check_direct_db_contract.py`, `tests/bodygraph/test_check_magic10_gate_readiness.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/cli/test_cli_usage_and_errors.py` and `tests/qa/test_generate_epic_close_pack.py`.

`paths=11` here and in hosted CI counts result v1.0 under `docs/ephemeral/`; PR-30's `paths=10` was taken on `1ddc47e`, before that record. The `lanes` report's note "documentation_only means the workflow's path filter starts no hosted run" describes a push of exempt paths alone; #692's diff includes the ten documents, so the filter does start a run (§5).

## 5. Hosted CI proof on `4ef4ad6` (plan §11 item 6)

Run 39709656840 (job 119597686980), `ci` / `test`: **success**. The whole job log was retrieved (277 lines, `original_length` 277) and read in full.

| Item | Value |
| :- | :- |
| Image | `ubuntu-26.04`, version 20261018.168.1; runner 2.338.0 |
| Checkout ref | `4ef4ad65def4f31a9ca2f52186a687b3bfd92a63` |
| `HEAD_SHA` / `BASE_SHA` | `4ef4ad65def4f31a9ca2f52186a687b3bfd92a63` / `a85067c24679da9ca15b467e87135fb0f962f39e` |
| Classification | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=11;lanes=none` |
| Citation check | `AGENTS_MD_CITATIONS_OK` |
| Lanes | `NEEDS_PYTHON: false`; setup, dependencies, pytest readiness, environment pins, changed tests and all seven lanes `skipped`, as inapplicable |
| Final step | `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| Warnings | one: the Node.js 20 deprecation notice for `actions/checkout@v4`. Not this PR's, and not a failure |

The six test files therefore ran only locally (§4), as plan §11 item 6 states. The `test` run on `1ddc47e`, triggered by PR-30's first push, was superseded by `4ef4ad6` under the workflow's pull-request cancellation (result v1.0 §5); it is not evaluated here.

## 6. Acceptance state (business case measure; plan §6)

| Item | State on `4ef4ad6` |
| :- | :- |
| The ten documents changed exactly as plan v1.0 §6 specifies | Met: companion diff equality (§2 row 1) |
| Changed documents keep the document-reading tests and the citation check green | Met locally (§4 rows 2 and 3); the citation check also in hosted CI (§5) |
| No release member, code, test, workflow, governed evidence or canon change | Met: 10 `not-member`, `release_id` unchanged (§4 row 4); only Markdown changed |
| Each changed statement matches merged `main` (the business case's measure) | Not checked here: DOC-20 verifies it on merged `main` |

These are implementation-validation states for PR-40 and DOC-20 to check. They are not acceptance, and not a QA verdict.

## 7. In-flight decisions and Product Owner directions

**In-flight decisions:** NONE. No correction was made; the PR's documents are PR-30's `1ddc47e`, unchanged.

**Product Owner directions in this phase:**

| ID | Direction | Effect |
| :- | :- | :- |
| PO-35-1 | Asked: "May I push this session's PR-35 result record (docs/ephemeral/ only, no code) to the PR's branch claude/sharp-carson-5ttoho, as you authorized for WU-PR-08 (PO-35-1)?" Answered (Nathan, 2026-10-22, between 02:09Z and 02:17:54Z by the session clock): "Push to PR branch (Recommended)" | This session's harness names another branch, `claude/nifty-ramanujan-i7nsh7`; that branch was not used. The record is committed on the PR's branch, so the work unit keeps one branch and one PR (GCF-17 continuity) |

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.0 §5)

| # | Time (UTC) | Action | Outcome |
| -: | :- | :- | :- |
| 6 | ~02:09 | `subscribe_pr_activity` for #692 | confirmed by the tool result |
| 7 | ~02:09 | Read #692: details, reviews, review threads, issue comments, check runs; fetched the branch | head `4ef4ad6`; 0 reviews; 0 threads; Codex summary (no findings on `4ef4ad6`); `test` success; `mergeable_state: clean`; 2 commits |
| 8 | ~02:10 | Job log of 119597686980 retrieved and read in full (§5) | success; exact head; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| 9 | 02:09 to 02:17 | PO-35-1 (§7) | push to the PR branch authorized |
| 10 | 02:17:54 to 02:19:30 | Local checks §4 on `4ef4ad6` | all pass; clone clean |
| 11 | 02:19:48 | TypeSafe v8.2 reading for the PR-40 handoff (§9) | HTTP 200 |
| 12 | next | Commit and push this record (`docs/ephemeral/` only); read back the remote head; observe CI and any Codex review on the record's commit through the subscription; the conditional PR-40 handoff goes to the Product Owner | — |

Remaining useful local action: none. Next evidence action: hosted CI on this record's commit.

## 9. TypeSafe reading for the PR-40 handoff

Run once, with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review`, label "PR-40 — HDE-CRD-0002 WU-DOC-01". The reading, as the skill prints it:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.78 (confidence 0.45); rung probabilities low 0.03, medium 0.47, high 0.20, extra high 0.30, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.78, Sonnet 5.5 0.20, Haiku 5.5 0.02 (confidence 0.71). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.023, Opus 5.5 at medium 0.367, Opus 5.5 at high 0.156, Opus 5.5 at extra high 0.234, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.006, Sonnet 5.5 at medium 0.094, Sonnet 5.5 at high 0.040, Sonnet 5.5 at extra high 0.060, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.009, Haiku 5.5 at high 0.004, Haiku 5.5 at extra high 0.006, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and medium. Sent 2026-10-22T02:19:48Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T02:19:48Z; HTTP 200 in 0.52 s; 5509 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and medium.
- **Action text sent:** "Independent post-merge lineage review of one already-reviewed documentation work unit, HDE-CRD-0002 WU-DOC-01: check against the repository that merged pull request #692 (3 commits; ten existing Markdown documents changed by about 190 lines, about seventy statements each mapped to its proof in an existing plan's statement-to-proof list, applied byte for byte from the plan's companion diff; plus three record files) landed exactly the planned change within the unit's bound; one Codex review round with no findings, no corrections and no Product Owner design decisions in the review phase, hosted CI green on its documentation-only path. There is no code change and no live run against a provider, and a separate completion verification of each statement against merged main, then QA, follow as later independent gates."
- **Records.** The Notion row was not written (the PR-35 prompt's "Mandatory single-block handoff"; PF10 addendum 2.1). Nathan's pick for PR-40 is not stated. His pick for this PR-35 session is not stated either; its reading is result v1.0 §7.

**Surface advice for PR-40:**
- A Claude Code session that Nathan creates, with `amthorn78/glow-hdengine-v2` checked out at `main` after the merge.
- GitHub read access to #692, its run 39709656840, the run on this record's commit, and its Codex summary.
- Closed rails through `env -i`, because the container sets vendor, database and GitHub keys.
- A CPython 3.12 venv with CI's install, only if PR-40 re-runs the citation check or the six document-reading test files (about 75 s).
- No live vendor, production or database access is needed. Apart from its own output artifacts, the review writes nothing to the repository.

## 10. Conditional PR-40 handoff

Use it only after the Product Owner has manually merged #692, and only where no `MERGE_OBSERVED` result was returned for that merge. The handoff is reproduced in this session's final response.

- **This record's `MERGE_PENDING`:** historical pre-merge evidence for head `4ef4ad6`.
- **The merge:** the Product Owner's own later assertion.
- **PR-40:** verifies the actual merged state and the landed lineage independently, including the PF10 addendum 2.14 check that no P1 on a real input was declined (none was raised).

If this subscribed session observes the merge, it returns `MERGE_OBSERVED` with the same PR-40 handoff. Once either has been pasted, the other is void.

## 11. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Merge of #692 | Product Owner | ready (§1) |
| Hosted CI on this record's commit | this session, through the subscription | pending at writing; reported to the Product Owner; a failure withdraws this `MERGE_PENDING` in a later record |
| Statement-by-statement verification on merged `main` | DOC-20 (whole-change IA), after PR-40 | not started |
| Plan §16 findings outside the bound, RF-1 to RF-10 | as plan §16 routes them (mostly the Product Owner) | unchanged |
| Carried items, plan §17; canon-conflict register CR-1 to CR-8 | as plan §17 and §18 state | unchanged |

**Nonclaims:** no QA verdict, acceptance, Ops, deployment, activation, PF09 or PF30 movement, canon drainage or closure; no canon edit; no governed evidence; no code, test, workflow or release-member change. This record is not intended to support a later PF-canon drain and recommends no status change (HDE Governance §2.0.19, the "Pre-drain status distinction" and "Later-drain update statement" bullets).

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-35 / result 2 (v1.1) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15.569Z) |
| role/stage | dedicated WU-DOC-01 PR-35 session / PR-35 |
| capture time | 2026-10-22T02:22:00Z |
| execution identity | https://claude.ai/code/session_01PNt1SBXNuFKsPQZ9r1zkEm |
| inherited usage | result v1.0 (PR-30) and plan v1.0 (PR-20), session_011Y6ExL6PGDrodZqKLRWCHK; instruction v1.0 (DOC-10) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Canon was read on `main` at `a85067c`. `docs/pfcanon/` was last changed by `e56788c`, and PF10 is v13.7.4; the PR branch does not change `docs/pfcanon/`.

| Decision topic | Sources and sections read | How it governs here |
| :- | :- | :- |
| Phase authority, results, readiness gate, ledger, checkpoints, handoff | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, read in full; glow-hde-pr-development 1.4.0, read in full | `MERGE_PENDING` only when every gate predicate holds (§2); one Proceed; no merge; conditional PR-40 block |
| Review chain: code review in, security review out | PF10-HDE-Build-Notes v13.7.4, addendum 2.3, read in full | §3: no security review is obtained or waited on; the Codex code review is read |
| Finding disposition, real inputs, repeated class | addendum 2.11 rule 7 and rule 8, read in full | no finding; rules 7 and 8 do not arise |
| P1 findings | addendum 2.14, read in full | no P1 was raised; none declined |
| TypeSafe reading; no model advice | addendum 2.1, read in full | §9: the reading as printed; no recommendation; Nathan picks |
| PR-35's obligations for this unit | plan v1.0 §11 and §19, read in full | §4: items 2 and 3 re-run (plus 4 and 5); §5: item 6 verified; no `[skip ci]` |
| Review scope of Markdown and `docs/ephemeral/` | `AGENTS.md` "Code review guidelines" and "Code review scope — CI-exempt paths are out of scope" | §3: no Codex finding expected; no re-request |
| CI shape and exact-head marker | `AGENTS.md` "HDE-EPIC039 current workflow posture"; `.github/workflows/ci.yml` lines 3–40 (path filters; concurrency with pull-request cancellation) | §1, §5: one `test` job; documentation-only skips; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| Release identity unchanged | `AGENTS.md` "Release identity" and "HDE-EPIC040 current posture" | §4 row 4 |
| Closed rails, redaction, pytest readiness | `AGENTS.md` "Operating workflow" | §4 environment |
| Status wording and later drain | PF04-Canon-HDE-Governance v2.8.7 §2.0.19, the "Pre-drain status distinction" and "Later-drain update statement" bullets | §11 nonclaims |
| Content canon of the corrected statements | carried from plan v1.0 "Canon relied on" (PF05 §4.1.4; PF03 "Truth and source fidelity"; PF04 "Doc-Delta discipline"; PF19 §3.1; addenda 2.12, 2.15, 2.17 to 2.21). Not re-read in this session | No correction was made, so no content decision was taken here |

Search: `git grep -c -i -E 'MERGE_PENDING|merge.readiness|merge-ready|PR-35' origin/main -- docs/pfcanon/`.
- PF10 had 90 hits; addenda 2.1, 2.3, 2.11 and 2.14 govern this phase.
- HDE Governance had one hit, at §2.0.19 (above).
- Glow QA Guide had three hits and HDE Phased Epics one; they concern PF09 drains and accepted units, and do not govern this phase.
- `git grep WU-DOC-01` across PF10 found passages in the index and in addenda 2.5, 2.8, 2.9, 2.10, 2.11, 2.12, 2.16, 2.17, 2.18, 2.19, 2.20 and 2.21. Plan v1.0 carries those that bind this unit's scope (2.19 P-8, 2.21, 2.17, 2.12 LR6-O5 and LR6-O7). None adds a PR-35 obligation beyond plan §19.
