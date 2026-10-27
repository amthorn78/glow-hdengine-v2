---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: REJECT
reject_route: reject_replan (PR-20, new dedicated session; the earlier Proceed is spent)
predecessor: none (first lineage review of WU-DOC-01)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
DOCUMENTATION_UNIT_ID: WU-DOC-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob c49ff720ffd2; #690)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md (v1.0; blob b019aeea0ff3; #691), with its companion docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0-prototype.diff (blob ced9d9b33e19; sha256 a334c348bf37187dab26a9051e9ee2f7a56692723fc1dd5f6838c8600e60ab63)
PR30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 4ce4ff1d0588)
PR35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.1.md (MERGE_PENDING, historical pre-merge evidence; blob e7893fbca6e3)
PR_REFS: [amthorn78/glow-hdengine-v2#692] (one PR; merged)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md, approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-8)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
entry: Nathan's manual-merge assertion (the PR-35 conditional handoff; no MERGE_OBSERVED result was returned for this merge)
reviewer: the continuing whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N); also the DOC-10 author of the instruction (§7, LRD-F1 origin)
sessions_reviewed: PR-20 and PR-30 https://claude.ai/code/session_011Y6ExL6PGDrodZqKLRWCHK; PR-35 https://claude.ai/code/session_01PNt1SBXNuFKsPQZ9r1zkEm
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state of 2026-10-12T02:29:38.234Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; unchanged on main at 4c9bbfc)
pf10_addendum_created: none (PR-40 is not an addendum producer)
repository_head_read: origin/main 4c9bbfc061e66c5d0ef504814c6d847f905c61c4 (#692's merge; no later commit)
created_at: 2026-10-22T02:37:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§10)
---

# HDE-CRD-0002 WU-DOC-01 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**REJECT, with a bounded re-plan through PR-20.**

- **What landed is sound.** #692 merged exactly the proceeded plan: the landed diff outside `docs/ephemeral/` is the plan's companion diff, byte for byte. Hosted CI was green on every run. The six document-reading test files pass on merged `main` (1,248 passed). Every statement I re-probed matched the code (§5).
- **What remains wrong.** `docs/qa_harness_pattern.md`, one of the unit's documents, still carries two stale statements inside the subjects it was meant to correct (§6):
  - **LRD-F1:** line 14 says "The composed writer currently admits only `HDE-CRD-0001`". The updater admits every CRD in `ADMITTED_CRD_QA`, today HDE-CRD-0001 and HDE-CRD-0002, and line 79 of the same page now says so.
  - **LRD-F2:** line 97 tells the reader to "follow AGENTS.md readiness: install `requirements-dev.txt`". The landed `AGENTS.md` readiness rule now requires CI's full install, `-e .` included.
- **Why this is a real defect, not a cosmetic one.** HDE-CRD-0002's own QA will publish through that composed writer. A QA session reading line 14 would conclude that HDE-CRD-0002 cannot be published. The input is real: the page on `main`, read by the next real consumer (addendum 2.11 rule 4 (a)).
- **Route.** A precise in-scope defect in landed work returns REJECT and goes to PR-20 for a new per-PR plan for the same work unit (PR-40, "PRECISE IN-SCOPE DEFECT → re-plan"). The earlier Proceed is spent. #692 is landed history and is not reopened or pushed to.

This review does not merge, implement, repair, or decide QA, Ops, acceptance or closure.

## 2. Merge and lineage facts

| Item | Evidence |
| :- | :- |
| PR | #692, `claude/sharp-carson-5ttoho` → `main`; `merged: true`, merged by `amthorn78` at 2026-10-22T02:28:43Z |
| Base | `a85067c24679da9ca15b467e87135fb0f962f39e` (#691) |
| PR commits, in order | `1ddc47e` (the ten documents, PR-30), `4ef4ad6` (result v1.0), `4e07d59` (result v1.1, PR-35); read from `refs/pull/692/head` |
| Merge commit | `4c9bbfc061e66c5d0ef504814c6d847f905c61c4`, a squash with one parent, `a85067c` |
| Landed tree | equals the PR head `4e07d59`'s tree (`git rev-parse <commit>^{tree}` identical) |
| Changed paths, `a85067c..4c9bbfc` | the ten planned documents (all `M`) and the two result records (`A`, under `docs/ephemeral/`) |
| Landed diff vs plan | `git diff a85067c 4c9bbfc -- . ':(exclude)docs/ephemeral' \| sha256sum` = `a334c348bf37187dab26a9051e9ee2f7a56692723fc1dd5f6838c8600e60ab63`, the companion diff's sha256 |
| Later divergence on `main` | none: `origin/main` is `4c9bbfc` |
| Code between the measured heads and `main` | no non-Markdown path changed from `6f2478f` (instruction baseline) or `b7458aa` (plan baseline) to `4c9bbfc`. The plan's code proofs, measured at `b7458aa`, apply unchanged to merged `main` |

## 3. Reviews and CI

**Reviews.**
- **Codex code review:** completed on `4e07d59` (the final head) with `has_any_findings: false`, `has_unresolved_findings: false`. The summary comment is 6330946962, updated 2026-10-22T02:22:34Z. PR-35 recorded the same result on `4ef4ad6`.
- **Other reviews:** 0 formal reviews and 0 review threads. The Codex summary is the only issue comment.
- **No P1 was raised, so none was declined** (addendum 2.14). No finding needed a disposition under addendum 2.11 rule 7, and rule 8 did not arise.
- **Codex security review:** not part of the chain (addendum 2.3).

**Hosted CI**, `ci` / `test`. Every run classified the change `documentation_only`, skipped setup, install and the lanes, and printed `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

| Run | Event, head | Conclusion |
| :- | :- | :- |
| 39709537690 | pull_request, `1ddc47e` | success |
| 39709656840 | pull_request, `4ef4ad6` | success |
| 39710971754 (job 119601959573) | pull_request, `4e07d59` | success; log read: `NEEDS_PYTHON: false`, every lane `skipped`, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| 39711590944 (job 119603942524) | push to `main`, `4c9bbfc` | success; the same steps skipped; the citation step and the final step succeeded |

**Addendum 2.12 measure** ("each later unit's PR-40 records any hosted CI failure a local replay would have caught"): none to record, because no hosted run failed. Whether that measure applies is still undecided (addendum 2.12).

## 4. Phase evidence read

**PR-30**, result v1.0, read in full:
- recovery before creation;
- one commit, `1ddc47e`, equal to the companion diff;
- local checks, all passing: the citation check; 1,248 tests passed with CI's full install; pre-push `documentation_only`; 10 `not-member`;
- in-flight decision ID-1 (the push re-created the deleted remote branch; no history overwritten).

**PR-35**, result v1.1, read in full:
- the readiness predicates;
- no correction;
- local re-runs on `4ef4ad6`, all passing;
- CI on `4ef4ad6`;
- PO-35-1: the result record was pushed to the PR branch, as authorized.

`MERGE_PENDING` was true for its head. It stays historical pre-merge evidence and is not rewritten.

- **LRD-O1 (observation, no effect).** Result v1.1 §5 says the `1ddc47e` run "was superseded … under the workflow's pull-request cancellation". Run 39709537690 in fact completed with success; it was not cancelled. No conclusion depends on it.

## 5. Independent checks on merged `main` (`4c9bbfc`)

These ran in a throwaway clone of `4c9bbfc` with a CPython 3.12.3 venv holding CI's full install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; pytest 8.4.2). Every run used `env -i` closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`, `APP_ENV` as stated). The clone stayed clean.

| # | Check | Result (2026-10-22 UTC) |
| -: | :- | :- |
| 1 | `python ci/checks/check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| 2 | The six document-reading test files (instruction §5.5) | **1,248 passed**, 77.98 s, exit 0 (02:30:54Z to 02:32:21Z) |
| 3 | `python ci/checks/check_direct_db_contract.py` | `DIRECT_DB_CONTRACT_OK`, exit 0 |
| 4 | `AGENTS.md` word diff, `a85067c..4c9bbfc`, read in full | only A-1 to A-7 changed. The review-scope rule's paragraph differs only in the factual sentence; the bolded rule and the eight-prefix list are byte-identical (`diff` of the paragraph) |
| 5 | A-3's facts | `ci.yml` re-includes `**.path_proof.txt` and the two `docs/run/` files on both `pull_request` and `push`; `classify_ci_changes.py:1732` gives every `.path_proof.txt` the `evidence` lane |
| 6 | A-6's facts: each EPIC037 generator's `--check` | `field_sufficiency`, `v2_adapter` and `v2_to_compat` exit 1 (`STALE_…`); `bg_resolve` exits 1 (`KeyError: 'adapter'`); `parent_binding` exits 0. These match the landed text |
| 7 | A-1 and R-3: CRD close output paths | `_derived_paths_v2` (`generate_epic_close_pack.py:2335-2339`) gives `audit/HDE-CRD-<NNNN>_close_report.md` and `_MANIFEST.json`, as written |
| 8 | R-1 and A-2: `release_id` | recomputed from `catalog/manifest.json`: `77204764c225…c51e`, in README and `AGENTS.md`; `52be4558…` absent from both |
| 9 | D-1, D-6, D-9 and K-1 (test client, `APP_ENV` `dev`, `test`, `prod`) | `/internal/version` returns 200 with `Authorization: Bearer x` on `adapter.factory` and `adapter.wsgi`. Body keys, in order: `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`. `X-Release-Id`: absent on `adapter.factory`, `rel_dev` on `adapter.wsgi`. `GET /api/reader/missing` returns 404 `application/json; charset=utf-8` on both. All match the landed text |
| 10 | R-5, A-5 and L-1k: dev `GET /reader?v=1` on `adapter.http_reader` | `dev` passes the gate (400 `ERR_READER_MISSING_PARAM` without a pair); `test`, `local` and `prod` return 403 `ERR_READER_FORBIDDEN`. Matches "served only when `APP_ENV` is exactly `dev`" |
| 11 | Routed stale strings in the ten documents | absent: `test_epic022_acceptance_scaffold`, `tests/test_sercanon.py`, "binds `0.0.0.0`" (the `Procfile` line in D-7 is correct), "Known limitation: a path that no route serves". `ENGINE_SERVICE_TOKEN` appears only in "no code reads" statements. `encoding_invariance.txt` appears only as `success_encoding_invariance.txt` |
| 12 | Secret scan of the landed diff's added lines (key, token, credential and DSN patterns) | no hit |
| 13 | Subject sweep of the ten documents (CRD admission, readiness, close-run, release, bind, harness) | two stale statements, both in `docs/qa_harness_pattern.md` (§6) |

**Business-case measure** (addendum 2.18 rule 5: PR-40 records whether it was met). The measure is "each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20".
- Every statement re-checked in rows 4 to 11 matches merged `main`. No changed statement was found wrong.
- This review did not re-verify all of plan §6 one by one; that is DOC-20's work. The measure is therefore **met for every changed statement checked, and not yet fully established**.
- The two findings concern statements the unit left unchanged, so they do not falsify the measure. They fail the instruction's Q-1 and A-4 obligations (§6).

## 6. Findings

### LRD-F1 — `docs/qa_harness_pattern.md:14` contradicts the admission table (blocking)

| Field | Content |
| :- | :- |
| Text on `main` | "… syntax support neither allocates that change nor grants governed-publication admission. The composed writer currently admits only `HDE-CRD-0001`." |
| Fact | `publish_crd_check_family` refuses any `crd_id` not in `ADMITTED_CRD_QA` (`tools/evidence/update_evidence_index.py:5180-5186`), and that table admits `HDE-CRD-0001` and `HDE-CRD-0002` (lines 51-54). Line 79 of the same page, as landed, says "today **`HDE-CRD-0001` and `HDE-CRD-0002`**" |
| Affected obligation | Instruction §6.5 Q-1, "Change: CRD admission per E-1"; S22 (CRD admission for HDE-CRD-0002's QA root); instruction §9.3: "A new stale statement inside the §6 documents and within an item's subject is added and recorded" |
| Real input | the page on `main`, which HDE-CRD-0002's QA sessions will read before publishing through the composed writer (addendum 2.11 rule 4 (a)) |
| Origin | Instruction Q-1 named only line 79 and said "The rest of the page stays". That was this IA's DOC-10 wording. Plan v1.0's §9.3 sweep did not catch line 14 either. Both sides missed it; neither recorded a decision to keep it |
| Bounded correction | Line 14's last sentence states admission per the `ADMITTED_CRD_QA` table, consistent with line 79 and `docs/EVIDENCE_INDEX.md` line 62 |

### LRD-F2 — `docs/qa_harness_pattern.md:97` paraphrases the superseded readiness rule

| Field | Content |
| :- | :- |
| Text on `main` | "When a selected check uses pytest, follow AGENTS.md readiness: install `requirements-dev.txt` with that interpreter and confirm `python -m pytest --version` before execution." |
| Fact | The landed `AGENTS.md` readiness rule (line 55, A-4) is: "install what CI installs, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` … Without `-e .` the `hdctl` console script is missing, and the CLI tests that run it fail." The instruction baseline (§5.5) showed that failure: 5 tests failed without `-e .` |
| Affected obligation | Instruction §6.2 A-4 (pytest guidance) and DOC10-F2. §9.3 covers this as a stale statement in a §6 document within an item's subject |
| Real input | the page on `main`; a QA harness session following it gets an install that fails the CLI tests |
| Bounded correction | Line 97 states the readiness rule as `AGENTS.md` now gives it, or points to it without restating the old command |

### What the re-plan covers

- The two findings.
- A re-read of the whole of `docs/qa_harness_pattern.md` against `tools/qa/qa_harness.py` and `tools/evidence/update_evidence_index.py` at the re-plan's head, for any other statement within Q-1's or A-4's subject.
- Each such statement is fixed or recorded with a reason. Line 12's `HDE-CRD-0001` example and line 44's `HDE-CRD-0001` paths are examples, not admission claims; PR-20 confirms that reading.
- Nothing else in the ten documents is reopened. Everything §5 verified stands as landed.

## 7. Requirement coverage across the unit

| Obligation | State on `main` |
| :- | :- |
| P-8 bounded scope (README, CHANGELOG, `AGENTS.md` passages, EVIDENCE_INDEX, CLI_commands, reader_v1) | delivered as planned. V-1 (`docs/server/reader_v1.md`) needed no change; confirmed |
| Addendum 2.21 routed items (LR8-F2, LR8-O1 and earlier carried items) | delivered as planned (plan §7); the routed stale strings are gone (§5 row 11) |
| Instruction Q-1 (`docs/qa_harness_pattern.md` CRD admission; close-run API) | **partly**: lines 79, 83 and 87-93 delivered; **line 14 not (LRD-F1)** |
| Instruction A-4 (pytest guidance) | delivered in `AGENTS.md`; **the page's paraphrase at line 97 is stale (LRD-F2)** |
| Plan v1.1 §7 acceptance: "each statement traces to a merged unit" | met for the changed statements (plan §6; CHANGELOG bullets cite merged PRs) |
| Plan v1.1 §7 acceptance: `test_check_agents_md_citations.py` passes | met: 57 passed within the 1,248; `AGENTS_MD_CITATIONS_OK` locally and in CI |
| Exclusions (no canon, code, test, workflow, governed artifact or release member) | met: Markdown only; release unchanged; no `docs/pfcanon/` change |
| Security (no secret; no authorization design) | met (§5 row 12). RF-6 (`/internal/version` has no authorization) stays routed to the Product Owner |
| Interfaces G-1, H-4, IF-4, IF-5 and IF-7 | delivered (rows 5 to 7; plan §13) |
| Recovery and rollback | rollback is a revert; none needed |

## 8. Attribution

- **Attributable to #692:** the ten documents' changes, equal to the companion diff, and the two result records.
- **Later divergence:** none.
- **Unrelated changes:** none.
- **Generated evidence:** none.
- **The two findings** are pre-existing text the unit was required to correct (Q-1) or brought out of line (A-4). They are not later divergence.

## 9. Carried items and owners (unchanged unless stated)

| Item | Owner |
| :- | :- |
| LRD-F1, LRD-F2 | the re-plan: PR-20, then PR-30 and PR-35 after a new Proceed, in new dedicated sessions |
| IA lesson: an instruction naming one line of a page should not say "the rest of the page stays" when §9.3 asks for a subject sweep | this IA (DOC-10 author); recorded here |
| Plan v1.0 §16, RF-1 to RF-10 | as plan §16 routes them, mostly the Product Owner |
| DOC10-O1, the O-19 code, OBS-8, OBS-P3-13, PR35-C1, LR8-F1, the canon doc-deltas, the S21 ADR revision | as plan §17 states |
| LRD-O1 (§4) | observation only |
| DOC-20 completion verification | this IA, after the re-planned unit's PR is merged and accepted |
| WU-OPS-01's business case, before OPS-10 | Product Owner |

**Not produced:** a DOC-20 result, a QA artifact, an Ops record, a PF10 addendum.

**Not executed:** a merge, any repository change outside this record, the full statement-by-statement check (DOC-20's), a live probe.

## 10. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged:
- CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED by Thoth;
- CR-4: APPROVED, and CR-5: APPROVED_AS_CHANGED, both by the Product Owner;
- CR-6: APPROVED (a), by the IA through RS-20;
- CR-7 and CR-8: APPROVED (a) each, by the Product Owner.

**No new conflict.** Both findings are repository-documentation drift against code and against `AGENTS.md`, not canon conflicts.

## 11. Next stage

- **REJECT → PR-20** (re-plan entry), for the same `WORK_UNIT_ID`, in a new dedicated top-level session that Nathan creates. It plans from the landed state (`4c9bbfc`) and this review's findings, and ends at a new `AWAITING_PO_PROCEED`.
- **Then:** Product Owner Proceed, PR-30, PR-35, Nathan's merge, PR-40 again, then DOC-20.
- **The earlier Proceed is spent.** #692 is landed history: never resumed, reused or pushed to.
- **Not material** (PR-40 "Material"): no acceptance criterion, boundary, unit scope, dependency or Product Owner risk changes. No RS-10.

## 12. TypeSafe reading for the receiving session (PR-20 re-plan, WU-DOC-01)

Action sent (v8.2): "Write, in a new dedicated session, a re-plan after a lineage review rejected one merged documentation work unit: a detailed PR implementation plan, not yet reviewed, that corrects two stale sentences left on one 112-line Markdown harness guide (one says the writer admits only the first change identity, contradicting a corrected line on the same page and the code's admission table; one paraphrases a pytest install rule that the agent-instructions file has since changed), after re-reading that whole page against the harness and updater code to find any other statement of the same kind. The landed state, the two findings and their code proofs are in the review; the plan drafts the exact text, prototypes it in a throwaway copy and names the local tests that read the page, because CI runs no test lane for a documentation-only change. No code changes and no live run occur; a Product Owner Proceed, implementation, CI, a lineage review and a completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 1.93 (confidence 0.89). Rung probabilities: low 0.00, medium 0.12, high 0.83, extra high 0.05, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.78, Sonnet 5.5 0.21, Haiku 5.5 0.00 (confidence 0.71).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.008, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.094, Opus 5.5 at high 0.647, Opus 5.5 at extra high 0.039, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.025, Sonnet 5.5 at high 0.174, Sonnet 5.5 at extra high 0.011, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - No flag printed.
  - Sent 2026-10-22T02:36:32Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T02:36:32Z; HTTP 200 in 0.55 s; 5542 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:**
  - The Notion row was not written.
  - Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-40 session is not stated; its reading is result v1.1 §9.

**Surface advice:** run the PR-20 re-plan as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment:**
  - Python 3.12 with CI's full install in a throwaway copy, for the six document-reading test files (about 80 s) and the citation check;
  - git, bash, `ruby` and `curl` for the pre-push check;
  - closed rails.
- **Access:** no live vendor, production or database access.
- **Order:** this review's pull request should be merged first.

## 13. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-40 / review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state of 2026-10-12T02:29:38.234Z). Receiver contract read: PR-20 "Inputs" (re-plan entry) and "Execute", in this session; DOC-20 — Verify Final Repository Documentation Completion — 100926.1 (page state of 2026-10-12T02:29:19.255Z), read in full to confirm that DOC-20 needs an accepted lineage review |
| role/stage | continuing whole-change IA / PR-40 |
| capture time | 2026-10-22T02:37:00Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | result v1.1 (PR-35), result v1.0 (PR-30), plan v1.0 (PR-20), instruction v1.0 (DOC-10) |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `4c9bbfc`. `docs/pfcanon/` was last changed by `e56788c`; PF10 is v13.7.4.

| Decision topic | Sources and sections | How it governs |
| :- | :- | :- |
| Review role, outcomes, routing | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Execute" 1 to 10; "Required result"; "Direct native handoff packages" ("PRECISE IN-SCOPE DEFECT → re-plan"; "Material"); "Mandatory single-block handoff"; "Accepted-final lineage protection" | §1, §11: REJECT and the PR-20 re-plan; no RS-10 |
| Real inputs; finding disposition | PF10 addendum 2.11 rules 4 to 8, read in this invocation | §1, §6: each finding's input is the page on `main`; no Codex finding needed a disposition |
| P1 | PF10 addendum 2.14, read in full earlier in this session | §3: none raised or declined |
| Measure; no ceiling | PF10 addendum 2.18, read in full in this invocation (rule 5: "PR-40 still records whether the unit's measure was met") | §5: the measure is recorded as checked in part, not falsified |
| Hosted CI failure record | PF10 addendum 2.12 (option A's measure, its "undecided" status), read at those passages | §3 |
| Reviewer chain | PF10 addendum 2.3 | §3 |
| Unit scope and routing | PF10 addendum 2.19 (P-8) and addendum 2.21 (the stale-document list), read at their WU-DOC-01 passages in this invocation and in full earlier in this session; instruction §6, §9.3; plan v1.0 §6, §7 | §6, §7 |
| Documentation before QA | PF19-Canon-Glow-QA-Guide §3.1 "Intent", read earlier in this session | §11: DOC-20 and QA-10 wait on the corrected unit |
| Source fidelity | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity", read earlier in this session | §6: each finding cites the code that controls it |
| Repository rules | `AGENTS.md` "Code review guidelines", "Operating workflow" (pytest readiness; closed rails; redaction), "HDE-EPIC039 current workflow posture" | §3, §5, LRD-F2 |

**Search:** `git grep -n -i -E 'lineage review|PR-40|WU-DOC-01' origin/main -- docs/pfcanon/`. The hits: PF10 (152), HDE Phased Epics (1), Reality Audits (1) and HDE CRD Records (2). Only PF10 addenda govern this review: 2.11, 2.12, 2.14, 2.18, 2.19 and 2.21. The other hits concern HDE-EPIC040 units and HDE-CRD-0001's historical lineage reviews, and do not govern this unit.
