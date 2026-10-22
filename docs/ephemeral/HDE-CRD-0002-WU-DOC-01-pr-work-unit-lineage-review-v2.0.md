---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "2.0"
decision: ACCEPT
predecessor: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v1.0.md (v1.0, REJECT, reject_replan; findings LRD-F1, LRD-F2; blob e2329d66c645; #693). Preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
DOCUMENTATION_UNIT_ID: WU-DOC-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob c49ff720ffd2)
PR_IMPLEMENTATION_PLAN_IDS: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md (blob b019aeea0ff3; companion sha256 a334c348…0ab63); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0.md (blob 5d8cbaef8e0d; companion docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0-prototype.diff, blob 7d59f29a1d6c, sha256 40e19bd145af12563a4385b7e7ed783f0b5c10c7c765b5ff5d25b17f006e39c3)
PR30_RESULT_IDS: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.0.md (blob 4ce4ff1d0588); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v2.0.md (PR_CANDIDATE_PUBLISHED; blob fc5798a65a48)
PR35_RESULT_IDS: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.1.md (blob e7893fbca6e3); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v2.1.md (MERGE_PENDING, historical pre-merge evidence; blob eb5f925143da)
PR_REFS: [amthorn78/glow-hdengine-v2#692 (cycle 1, merged as 4c9bbfc), amthorn78/glow-hdengine-v2#695 (cycle 2, merged as cf8b759)]
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-8)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
entry: Nathan's manual-merge assertion for #695 (the cycle-2 PR-35 conditional handoff; no MERGE_OBSERVED result was returned for this merge)
reviewer: the continuing whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
sessions_reviewed: cycle 1 PR-20/PR-30 https://claude.ai/code/session_011Y6ExL6PGDrodZqKLRWCHK, PR-35 https://claude.ai/code/session_01PNt1SBXNuFKsPQZ9r1zkEm; cycle 2 PR-20/PR-30 https://claude.ai/code/session_01WPAu8VRbMGFAKxrRj6WGur, PR-35 https://claude.ai/code/session_01Jn1zDFZYUR1i32p1v2YULk
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state of 2026-10-12T02:29:38.234Z, read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; unchanged on main at cf8b759)
pf10_addendum_created: none (PR-40 is not an addendum producer)
repository_head_read: origin/main cf8b7598ce502bf42155ea0e186ee6fdbd2605c5 (#695's merge; no later commit)
created_at: 2026-10-22T03:32:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§9)
---

# HDE-CRD-0002 WU-DOC-01 — PR work-unit lineage review v2.0 (PR-40, ACCEPT)

## 1. Decision

**ACCEPT.** WU-DOC-01 is delivered on `main` across its ordered merged lineage, #692 then #695, with sufficient attributable evidence.

- **#692** landed plan v1.0 byte for byte. Review v1.0 §5 verified it, and nothing in it has changed since, apart from the one page #695 corrected.
- **#695** landed plan v2.0's correction byte for byte. It changed only `docs/qa_harness_pattern.md`, lines 14 and 97.
- **Both v1.0 findings are resolved on `main`:**
  - LRD-F1 (line 14) now states admission per `ADMITTED_CRD_QA`, which this review's probe confirms;
  - LRD-F2 (line 97) now states the `AGENTS.md` readiness command exactly.
- **Nothing else was reopened**, and no new finding remains.
- **Next stage: DOC-20** completion verification, run by this IA (§10).

ACCEPT is not merge, QA, Ops, acceptance of the change, release or closure.

## 2. Merge and lineage facts

| Item | #692 (cycle 1) | #695 (cycle 2) |
| :- | :- | :- |
| Merged | yes, by `amthorn78`, 2026-10-22T02:28:43Z | yes, by `amthorn78`, 2026-10-22T03:27:54Z |
| Base | `a85067c` (#691, plan v1.0) | `0e2bd9e` (#694, plan v2.0) |
| PR commits, in order | `1ddc47e`, `4ef4ad6`, `4e07d59` | `7289ce4` (the page), `28e6ba1` (result v2.0), `1ef90a1` (result v2.1); read from `refs/pull/695/head` |
| Merge commit | `4c9bbfc`, a squash with one parent | `cf8b759`, a squash with one parent, `0e2bd9e` |
| Landed tree = PR head tree | yes (review v1.0 §2) | yes (`1ef90a1^{tree}` = `cf8b759^{tree}`) |
| Landed diff outside `docs/ephemeral/` | sha256 `a334c348…0ab63` = plan v1.0's companion | sha256 `40e19bd1…6e39c3` = plan v2.0's companion; `docs/qa_harness_pattern.md` blob `9810fb1` → `9ac7119` |
| Paths | the ten documents plus two records | `M docs/qa_harness_pattern.md` plus two records under `docs/ephemeral/` |

**Order and divergence:**
- **Between the merges:** `4c9bbfc..0e2bd9e` adds only `docs/ephemeral/` records: the review v1.0 (#693) and plan v2.0 (#694).
- **Outside `docs/ephemeral/`:** `git diff --name-only 4c9bbfc cf8b759` lists only `docs/qa_harness_pattern.md`.
- **Unit total** (`a85067c..cf8b759`, outside `docs/ephemeral/`): 10 files, +139/−59. That is #692's +137/−57 plus #695's +2/−2.
- **After the merge:** none; `origin/main` is `cf8b759`.

## 3. Reviews and CI for #695

**Reviews:**
- **Codex code review:** completed on the final head `1ef90a1`, with `has_any_findings: false` and `has_unresolved_findings: false` (summary 6331607092, updated 2026-10-22T03:26:55Z). The PR-35 result recorded the same on `28e6ba1`.
- **Other reviews:** 0 formal reviews, 0 review threads, and no other comments.
- **No P1 was raised** (addendum 2.14). Addendum 2.11 rules 7 and 8 were not triggered. Codex security review is not in the chain (addendum 2.3).

**Hosted CI**, `ci` / `test`, all successful:

| Run | Event, head |
| :- | :- |
| 39714426307 | pull_request, `7289ce4` |
| 39714523838 | pull_request, `28e6ba1` (log read by PR-35: `documentation_only`, lanes skipped, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) |
| 39716830747 | pull_request, `1ef90a1` (the final head) |
| 39716972895 | push to `main`, `cf8b759` |

The PR-35 result v2.1 §7 left the record commit's CI, Codex and mergeability to be confirmed. Run 39716830747 succeeded, the Codex summary shows no findings on `1ef90a1`, and the merge succeeded. No v2.2 was needed.

**Addendum 2.12 measure:** no hosted run failed in either cycle, so nothing is recorded; the measure's applicability is still undecided.

## 4. Phase evidence read (cycle 2)

**Plan v2.0**, read in full:
- the corrections C-1 and C-2, with their proofs;
- a 16-row sweep of the page against `tools/qa/qa_harness.py` and `tools/evidence/update_evidence_index.py`;
- RF-11, routed;
- PD-1 to PD-5;
- the prototype: 1,248 passed;
- no Product Owner question.

**Result v2.0 (PR-30)**, read in full:
- recovery;
- one commit, `7289ce4`, equal to the companion;
- local checks, all passing: 1,248 passed; citations OK; `documentation_only`; `not-member`;
- in-flight decision ID-1 (record committed after PR creation);
- force-with-lease restart of the merged-history branch, pinned to `476515c`.

**Result v2.1 (PR-35)**, read in full:
- no correction;
- the review matrix is clean;
- local re-runs on `28e6ba1`, all passing;
- CI on `28e6ba1`;
- PO-35-1: the record was pushed to the PR branch, as authorized.

**Proceed:** cycle 2 had its own Proceed for exactly plan v2.0, and cycle 1's was spent.

**Branches:** #692 and its branch were not touched (result v2.0 §1).

## 5. Independent checks on merged `main` (`cf8b759`)

These ran in a throwaway clone at `cf8b759` with a CPython 3.12.3 venv holding CI's full install (pytest 8.4.2), under `env -i` closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC APP_ENV=dev`). The clone stayed clean.

| # | Check | Result (2026-10-22 UTC) |
| -: | :- | :- |
| 1 | `python ci/checks/check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK` |
| 2 | The six document-reading test files (instruction §5.5) | **1,248 passed** in 79.64 s, exit 0 |
| 3 | LRD-F1: line 14 against the code | `ADMITTED_CRD_QA` = `[HDE-CRD-0001, HDE-CRD-0002]`. For HDE-CRD-0003, `publish_crd_check_family` refuses with "governed CRD publication admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003" and `publish_crd_close_run_family` with "governed CRD close-run publication admits only …". Line 14 ("The composed writers admit only the CRDs in the updater's source-owned `ADMITTED_CRD_QA` table, today `HDE-CRD-0001` and `HDE-CRD-0002`") matches. **Resolved** |
| 4 | LRD-F2: line 97 against `AGENTS.md` | the install command on line 97 is byte-identical to `AGENTS.md`'s pytest readiness command (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), and line 97 states the `hdctl` consequence. **Resolved** |
| 5 | No other stale readiness paraphrase | no bare `requirements-dev.txt` readiness statement remains in the ten documents |
| 6 | Consumers of the page | `git grep qa_harness_pattern` over `tests`, `ci`, `tools`, `scripts`, `.github`, `engine` and `adapter`: none |
| 7 | RF-11 (plan v2.0 §16) | confirmed as stated: line 120 cites "PF10 — HDE Build Notes §2.8", but PF10 v13.7.4 §2.8 (line 876) is the WU-PR-03 lineage review, and PF10 has no "tested state", "evidence-storage" or "review-time" text. It is pre-existing and outside Q-1's and A-4's subjects, so it is routed and not blocking (§8) |
| 8 | Code between `4c9bbfc` and `cf8b759` | unchanged (only `docs/qa_harness_pattern.md` and records). Review v1.0 §5's probes and statement checks therefore hold on `cf8b759` |

**Business-case measure** (addendum 2.18 rule 5). The measure is "each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20".
- Every statement re-checked in review v1.0 §5 and in rows 3 and 4 above matches merged `main`. No changed statement was found wrong.
- The full statement-by-statement check of plan v1.0 §6 and plan v2.0 §6 is DOC-20's work.
- So the measure is **met for every changed statement checked; DOC-20 completes it.**

## 6. Requirement coverage across the unit

| Obligation | State on `main` |
| :- | :- |
| P-8 bounded scope (README, CHANGELOG, `AGENTS.md` passages, EVIDENCE_INDEX, CLI_commands, reader_v1) | delivered (#692). V-1 needed no change |
| Addendum 2.21 routed items | delivered (#692; review v1.0 §5 row 11) |
| Instruction Q-1 (`docs/qa_harness_pattern.md`) | delivered: lines 79, 83 and 87-93 by #692; line 14 by #695 |
| Instruction A-4 (pytest guidance) | delivered: `AGENTS.md` line 55 by #692; the page's line 97 by #695 |
| Plan v1.1 §7 acceptance: "each statement traces to a merged unit" | met (plan v1.0 §6, plan v2.0 §6, CHANGELOG bullets) |
| Plan v1.1 §7 acceptance: `test_check_agents_md_citations.py` passes | met (57 passed within the 1,248; `AGENTS_MD_CITATIONS_OK` locally and in CI) |
| Exclusions | met: Markdown only; release `1.3.0` and `release_id` `77204764…c51e` unchanged; no `docs/pfcanon/` change |
| Security | met: no secret; RF-6 stays routed to the Product Owner |
| Interfaces G-1, H-4, IF-4, IF-5, IF-7 | delivered (review v1.0 §5; plan v2.0 §12) |
| Recovery and rollback | none needed; a revert of either PR is the rollback |

## 7. Attribution

- **Attributable to #692:** the ten documents' changes (`a334c348…`) and the cycle-1 records.
- **Attributable to #695:** the two sentences of `docs/qa_harness_pattern.md` (`40e19bd1…`) and the cycle-2 records.
- **Records PRs between them:** #693 (review v1.0) and #694 (plan v2.0), `docs/ephemeral/` only.
- **Later divergence, unrelated changes and generated evidence:** none.

## 8. Findings, observations and carried items

| Item | State | Owner |
| :- | :- | :- |
| LRD-F1, LRD-F2 | **resolved** by #695 (§5 rows 3 and 4) | — |
| LRD-O1 (review v1.0 §4) | observation; no effect | — |
| RF-11: line 120's "PF10 — HDE Build Notes §2.8" citation | pre-existing; outside the unit's subjects; not blocking | Product Owner, as a later documentation candidate (plan v2.0 §16) |
| RF-1 to RF-10 (plan v1.0 §16) | unchanged | as plan v1.0 routes them |
| Carried items (plan v1.0 §17): DOC10-O1, the O-19 code, OBS-8, OBS-P3-13, PR35-C1, LR8-F1, the canon doc-deltas, the S21 ADR revision | unchanged | as stated there |
| IA lesson (review v1.0 §9) | recorded | this IA |
| WU-OPS-01's business case, before OPS-10 | due | Product Owner |

**Not produced:** a DOC-20 result, a QA artifact, an Ops record, a PF10 addendum.

**Not executed:** a merge, any repository change outside this record, the full statement-by-statement check (DOC-20's), a live probe.

## 9. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged:
- CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED by Thoth;
- CR-4: APPROVED, and CR-5: APPROVED_AS_CHANGED, both by the Product Owner;
- CR-6: APPROVED (a), by the IA through RS-20;
- CR-7 and CR-8: APPROVED (a) each, by the Product Owner.

**No new conflict.** RF-11 is a stale repository citation of PF10's numbering, not a canon conflict.

## 10. Next stage

**Selected: DOC-20 — Verify Final Repository Documentation Completion — 100926.1**, run by this IA.

- **Basis:** PR-40 "Resolve the next approved Plan stage": "a just-accepted final documentation PR needing completion verification goes to DOC-20".
- **Plan location:** Plan v1.1 §7 WU-DOC-01 ("DOC-20 verifies completion"), the only documentation unit (§8), ordered before WU-OPS-01 and QA-10.
- **Dependency evidence:** this ACCEPT, and both PRs merged (§2).
- **Not next:**
  - WU-OPS-01 waits on its business case before OPS-10 (addendum 2.18);
  - QA-10 needs the documentation completion and WU-OPS-01 first (Plan v1.1 §9 item 1; Glow QA Guide §3.1).
- **DOC-20's input contract**, read in full this session, is met: the final `PR_INSTRUCTION_ID`; the merge references; this accepted `PR_WORK_UNIT_LINEAGE_REVIEW_ID`; the approved Specification, Audit, Plan and original `PLAN_REVIEW_ID`; the implementation results; the documentation baseline; identities; and the conflict and attempt lineage.

## 11. TypeSafe reading for the receiving session (DOC-20, WU-DOC-01)

Action sent (v8.2): "Verify, read-only in the continuing whole-change implementation session, that the final repository-documentation unit of an approved change is complete on merged main: the unit landed across two merged pull requests (a ten-document update of about seventy statements and a two-sentence correction after a rejected lineage review), and an accepted lineage review exists. Map every approved requirement and instruction item to the merged documentation text, and check each changed statement against the code, tool help and records that the plans' statement-to-proof lists name, re-running probes and the document-reading tests where a statement asserts behaviour. Decide complete, incomplete, pending or blocked, with owners for any gap. No code changes and no live run occur; QA readiness follows."

- **TypeSafe v8.2: Opus 5.5 at extra high.**
  - Effort score 2.71 (confidence 0.76). Rung probabilities: low 0.00, medium 0.04, high 0.24, extra high 0.68, max 0.04, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.02, Opus 5.5 0.96, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.95).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.014, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.038, Opus 5.5 at high 0.230, Opus 5.5 at extra high 0.653, Opus 5.5 at max 0.038, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.005, Sonnet 5.5 at extra high 0.014, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - No flag printed.
  - Sent 2026-10-22T03:31:40Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T03:31:40Z; HTTP 200 in 0.61 s; 5485 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:**
  - The Notion row was not written.
  - Nathan's pick for DOC-20 is not stated. Nathan's pick for this PR-40 session is not stated; its reading is result v2.1 §8.

**Surface advice:** run DOC-20 in the continuing whole-change HDE-CRD-0002 Implementation Agent session (this one, or a top-level session Nathan creates for that role) on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment:**
  - CPython 3.12 with CI's full install in a throwaway clone of merged `main`, for the six document-reading test files (about 80 s), the test-client probes and the tools' `--help` and `--check`;
  - closed rails through `env -i`.
- **Access:** no live vendor, production or database access.
- **Order:** this review's pull request should be merged first.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-40 / review 2 (v2.0) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state of 2026-10-12T02:29:38.234Z). Receiver contract: DOC-20 — Verify Final Repository Documentation Completion — 100926.1, https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7 (page state of 2026-10-12T02:29:19.255Z), read in full in this session |
| role/stage | continuing whole-change IA / PR-40 |
| capture time | 2026-10-22T03:32:00Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | review v1.0 §13; result v2.1 §10; result v2.0 §8; plan v2.0 §20 |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `cf8b759`. `docs/pfcanon/` was last changed by `e56788c`; PF10 is v13.7.4.

| Decision topic | Sources and sections | How it governs |
| :- | :- | :- |
| Review role, outcomes, next stage | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Execute" 1 to 10; "Required result"; "Resolve the next approved Plan stage"; "ACCEPT → next approved Plan stage"; "Accepted-final lineage protection" | §1, §10: ACCEPT across the ordered lineage; DOC-20 |
| Next-stage receiver | DOC-20 — Verify Final Repository Documentation Completion — 100926.1, "Required inputs" and "Execute", read in full in this session | §10 |
| Real inputs; finding disposition | PF10 addendum 2.11 rules 4 to 8, read in this session | §3, §5 rows 3 and 4 |
| P1 | PF10 addendum 2.14, read in full earlier in this session | §3 |
| Measure; no ceiling | PF10 addendum 2.18 rule 5, read in full in this session | §5 |
| Hosted CI failure record | PF10 addendum 2.12 (option A's measure; undecided) | §3 |
| Reviewer chain | PF10 addendum 2.3 | §3 |
| Unit scope and routing | PF10 addenda 2.19 (P-8) and 2.21; instruction §6 and §9.3; review v1.0 §6 ("What the re-plan covers") | §5, §6 |
| Documentation before QA | PF19-Canon-Glow-QA-Guide §3.1 "Intent", read earlier in this session | §10 |
| Repository rules | `AGENTS.md` "Code review guidelines", "Operating workflow" (pytest readiness rule; closed rails) | §3, §5 row 4 |

**Search:** `git grep -c -i -E 'lineage review|PR-40|WU-DOC-01' origin/main -- docs/pfcanon/` gives the same file set as review v1.0: PF10, HDE Phased Epics, Reality Audits and HDE CRD Records. Only the PF10 addenda above govern this review.
