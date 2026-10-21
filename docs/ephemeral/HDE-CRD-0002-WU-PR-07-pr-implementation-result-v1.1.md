---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
result: none (PR-35 checkpoint after the first corrective commit; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.0.md (PR-30, PR_CANDIDATE_PUBLISHED; preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0), as overlaid by the rescope addendum
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md (RS-20 APPROVE; D-1, D-2)
pf10_addendum_overlay: docs/ephemeral/HDE-CRD-0002-WU-PR-07-PF10-build-notes-addendum-v1.0.md (proposed 2.13)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (the only PF10 file on main at 390bc99; read as provenance)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15.569Z, read in full)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session; session_disposition NEW_DEDICATED)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5 (the PR's head branch; this session's harness default branch claude/exciting-cerf-l5h4cx is not used, because the handoff continues the same branch and pull request)
base: main 390bc9960a3e9012f67fe7ea39905b624259c87e
entry_head: f42dd521e22d4c85de54883f396df46ec382dfe1
corrective_commit: 21c029d1b8af817ea58d1b54de4a87a56ed865e1
created_at: 2026-10-20T17:20:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.1 (PR-35 checkpoint)

## 1. State

Nonterminal checkpoint. One Codex finding (P1) is fixed locally in `21c029d` and is about to be pushed with this record. After the push: a fresh Codex review of the new head, then hosted CI on the final head. The terminal PR-35 record follows as v1.2.

## 2. Entry verification

| Item | Found |
| :- | :- |
| PR #668 | open, not draft, base `main` `390bc99`, head `f42dd52` (`1080f77` implementation + PR-30 result record) |
| Branch | `claude/gallant-cerf-ysdde5`; local checkout tracks it; clean |
| Subscription | active (tool result confirmed at 16:58:07Z) |
| Reviews at entry | Codex code review running on `1080f77`; no threads |
| CI at entry | `test` in progress on `f42dd52` |

## 3. Review findings

| ID | Reviewer, revision | Location | Finding | Real input? (addendum 2.11 rule 4) | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-1 | Codex code review, `1080f77`, P1 (thread `PRRT_kwDOP103ks6ub6gW`, comment 4327887921) | `tools/qa/generate_epic_close_pack.py:2320` `_token_occurs` | A dot was an identifier boundary: `S1` matched `S1.2`, `S1.2` matched `S1.2.3`, so a candidate could bind a criterion absent from the requirements document | Yes. The v2 schema's `item_id` permits dotted IDs, and real dotted parent/child IDs exist on `main` (`HDE-FERM008` 465 occurrences, `HDE-FERM008.2` 144, `HDE-FERM008.5` 108 in tracked docs and audit files). An Epic close citing a parent ID against a document naming only children would falsely bind | Fixed in `21c029d` (rule 7): a dot between alphanumerics continues the identifier, a trailing dot stays punctuation; the same function serves the ADR-deferral check, which gains the same behavior |

Codex security review: deprecated by addendum 2.3; not a step of this chain.

## 4. Local checks on `21c029d`

Detached clone of the commit, closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), CPython 3.12.3, venv with `setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt`, `-e` of a separate clone, `PYTHONPATH` set to the copy.

| Check | Result |
| :- | :- |
| New test `test_v2_requirement_ids_match_only_complete_dotted_identifiers` (8 cases) against the unfixed function | 4 failed, 4 passed (negative control, as intended) |
| `tests/qa/test_generate_epic_close_pack.py` | 467 passed (459 + 8), exit 0, 17:09:40 to 17:11:09; copy clean |
| `prepush_check.py --base f42dd52 --head HEAD lanes` | `reason=selected_lanes;paths=2;lanes=evidence,qa`; targets the writer test and `tests/qa/test_qa_tool_ownership.py` |
| `prepush_check.py membership` for both paths | neither is a release member |
| `prepush_check.py --base f42dd52 --head HEAD replay` | see §5 |

The v1 model does not call `_token_occurs`; v1 output bytes are unchanged.

## 5. Replay of the delta's lanes

`prepush_check.py --base f42dd52 --head 21c029d replay`, 17:12 to 17:27:52, same environment: **PASS**. `ci.yml` sha256 `d02021f3…` (the pinned one); steps 01, 04 and 05 excluded and substituted; step 08 changed tests 613 passed; step 13 evidence lane 134 passed; step 14 qa lane 488 passed; product, compat, db, rails and release lanes not applicable to this delta and skipped; step 16 SUCCESS; copy clean; repository unchanged. Not CI's result. The full seven-lane run against `main` is hosted CI's on the pushed head.

## 6. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| Push to the PR head branch `claude/gallant-cerf-ysdde5`, not the harness default | The handoff continues the same branch and PR (GCF-17 continuity) | `git ls-remote` read-back after push (v1.2) |

## 7. PR_REMOTE_ACTION_LEDGER

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 1 | 16:58 | Subscribe to #668 | active |
| 2 | 16:59 | Safety-net check-in armed for 17:50 | trigger `trig_01Lq8hX2RAiM4UpUqZb9QS8Y` |
| 3 | 17:08 | Read Codex review 5588736037 on `1080f77` | 1 finding (CX7-1, P1) |
| 4 | 17:09 | Hosted `test` on `f42dd52` (run 39461304098) | success at 17:09:09; stale as a gate, since CX7-1 requires a new head |
| 5 | 17:09 | Local fix and tests (§4) | pass |
| 6 | next | Reply on the CX7-1 thread; push `21c029d` and this record; request `@codex review` on the new head | — |

## 8. Spend against the ceiling (instruction ID-1)

Session 4 of 4 (this PR-35 session), within the 3-day limit. No further session is projected unless the Product Owner directs it.

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| AQ-1 (S21 ADR, `Proposed`) | Product Owner | pending; before #668 merges |
| Fresh Codex review of the new head | PR-35 | requested after push |
| Hosted CI on the final head | PR-35 | after push |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment, canon edit or closure.
