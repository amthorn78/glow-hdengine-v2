---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.2"
result: none (PR-35 checkpoint after the second corrective commit; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.1.md (preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0), as overlaid by the rescope addendum
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md (RS-20 APPROVE; D-1, D-2)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.4.md (Product Owner's upload, placed on this branch in c1a41b4 at the Product Owner's direction; sha256 208651022419427cf5758fc64b7ebcaeb94e141a81aa4ca721f1c66fe74fe827; adds addendum 2.13; addendum 2.11 unchanged; read as provenance)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5
base: main 390bc9960a3e9012f67fe7ea39905b624259c87e
remote_head_before_push: c1a41b48ff7c44aca14a055fab8c6f89f9af4c02
corrective_commit: e274fbf (full SHA in §7, read back after push)
created_at: 2026-10-20T18:20:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.2 (PR-35 checkpoint)

## 1. State

Nonterminal. Codex round 2 (on `a6c6655`) raised CX7-2 and CX7-3, both P1, in the same check as round 1's CX7-1 (`_require_v2_semantics`, the binding of declared acceptance and ledger entries). Addendum 2.11 rule 8 tripped, and the session asked the Product Owner one design question. The Product Owner's decision (§2) is implemented in `e274fbf` and pushed with this record. Next: fresh Codex review and hosted CI on the new head, then the terminal record.

## 2. Product Owner decision PO-35-1 (rule 8 design question, round 2)

Asked: narrow fix (fix CX7-2, decline CX7-3 as the ADR's stated limit), stated limits for both, or rescope. **Answer, verbatim:**

> Neither A nor B. Do not decline either P1. Fix both on PR #668:
> - CX7-2: apply the drain-targets ledger check to tracked_issues items with adr_status, as for deferrals (Change Process Guide §3.5.2.1, TI mapping (b)). Add a test.
> - CX7-3: require full requirement coverage for SATISFIED (Change Process Guide §3.5.2.1, "binds each current governing requirement or acceptance criterion"). To stay within addendum 2.11 rules 5 and 6, pin one requirements-table format, for example first-column IDs as in HDE-CRD-0002's Specification (| S01 | … | S22 |), refuse a bound document without it, and refuse SATISFIED unless every ID has an acceptance row. Remove the ADR's "Requirement coverage is the source author's" limit line. Add tests, including the real Specification's 22 rows.
> Run the negative controls, the writer test file and the evidence and qa lanes locally before one push. Reply on both threads, then push. Record this decision in the PR-35 result record.

Before answering, the Product Owner directed the replacement of PF10 v13.6.3 by v13.6.4. It was done in `c1a41b4` and pushed; v13.6.4 adds only addendum 2.13, so the rule 8 question stood.

Effect on the plan: PD-2's "the writer checks that each ID occurs as a token in that document" is replaced for criteria by membership in the pinned table's row IDs, plus SATISFIED coverage. Bind-by-reference itself is unchanged. This is an in-flight decision under the Product Owner's direction (§5), not a rescope: no acceptance criterion, protected boundary or other unit changes.

## 3. Review findings

| ID | Reviewer, revision | Location | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX7-1 | Codex, `1080f77`, P1 (thread `PRRT_kwDOP103ks6ub6gW`) | `_token_occurs` | dot treated as an identifier boundary | fixed in `21c029d` (v1.1); thread resolved |
| CX7-2 | Codex, `a6c6655`, P1 (thread `PRRT_kwDOP103ks6uc1a_`, comment 4328279140) | `_require_v2_semantics`, deferral ledger check | a `tracked_issues` item closed by `adr_status` was not checked against the drain-targets ledger | fixed in `e274fbf` (PO-35-1): same check as deferrals; refusal `TRACKED_ISSUE_UNBOUND` |
| CX7-3 | Codex, `a6c6655`, P1 (thread `PRRT_kwDOP103ks6uc1a5`, comment 4328279129) | `_require_v2_semantics`, acceptance binding | SATISFIED accepted with requirements omitted | fixed in `e274fbf` (PO-35-1): pinned table rows `^\| (S[0-9]{2,}) \|`; `REQUIREMENTS_TABLE_ABSENT`, `REQUIREMENT_ID_UNBOUND` (criterion not a row ID), `REQUIREMENT_COVERAGE_INCOMPLETE` (SATISFIED without every row ID); NOT SATISFIED may cover part |

Rule 8 status: rounds 1 and 2 shared a class; the design question was asked once and answered (PO-35-1). A further same-class finding returns to the Product Owner.

## 4. Local checks on `e274fbf`

Detached clone, closed rails, CPython 3.12.3, CI's install (as v1.1 §4).

| Check | Result |
| :- | :- |
| Negative control: the new test file against the pre-fix writer (`c1a41b4`), the affected selection | 4 failed as intended (`adr_tracked_issue_not_in_drain_targets`, `satisfied_omits_a_requirement`, `requirements_document_without_table`, `test_v2_requirement_table_pin_reads_the_real_specification_rows`); 14 passed, including the two over-refusal guards (NOT SATISFIED partial coverage; TI pointer without ledger entry) |
| `tests/qa/test_generate_epic_close_pack.py` | 473 passed (467 + 6), exit 0, 18:14:47 to 18:16:12; copy clean |
| Real Specification | `_requirement_ids` on `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` returns exactly S01 to S22 (22), equal to the verbatim fixture rows |
| `prepush_check.py --base c1a41b4 --head e274fbf replay` (evidence and qa lanes) | **PASS**, 18:17 to 18:29:32: `reason=selected_lanes;paths=3;lanes=evidence,qa`; `ci.yml` the pinned one; step 08 changed tests 619 passed; step 13 evidence lane 134 passed; step 14 qa lane 488 passed; other lanes not applicable; step 16 SUCCESS; copy clean; repository unchanged. Not CI's result |

## 5. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| Push to the PR head branch `claude/gallant-cerf-ysdde5` (v1.1) | GCF-17 continuity: same branch and PR | `git ls-remote` read-backs |
| PF10 v13.6.4 replaces v13.6.3 on this branch (`c1a41b4`) | Product Owner's explicit direction; precedent #660 carried a PF10 replacement | `cmp` with the upload: identical; one PF10 file in `docs/pfcanon/` |
| PO-35-1: TI ledger check and pinned requirements table with SATISFIED coverage (§2) | Product Owner's rule 8 decision; canon §3.5.2.1 | §4 |
| The ADR stated limit is replaced by the pin's limit (an Epic Specification in another format, such as HDE-EPIC040's `HDE-SEPA005.1` rows, is refused until a later pin) | Rule 5: an input outside the pinned set gets one refusal and a stated limit | `REQUIREMENTS_TABLE_ABSENT` case |
| Default test fixture's drain-targets ledger gains `TI-002` | The fixture's `TI-002` ADR status now needs a ledger entry | 473 passed |

## 6. Spend against the ceiling (instruction ID-1)

Session 4 of 4, within 3 days. No further session is projected unless the Product Owner directs it.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.1 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 6 | 17:28 | Reply on CX7-1; push `f42dd52..a6c6655`; resolve CX7-1; comment `@codex review` | pushed and read back; Codex had already started a review on new commits, so the manual request was redundant (one extra review) |
| 7 | 17:47 | Read Codex review 5589224509 on `a6c6655` | CX7-2, CX7-3 (P1) |
| 8 | 17:50 | Hosted `test` on `a6c6655` (run 39466384991) | success; `mergeable_state` clean; stale as a gate after round 2 |
| 9 | ~18:05 | Rule 8 question to the Product Owner | answered PO-35-1 (§2) |
| 10 | 18:05 | Commit and push PF10 v13.6.4 (`a6c6655..c1a41b4`) | pushed and read back; Codex review on `c1a41b4` started (new commits) |
| 11 | 18:16 | Local fix and checks (§4) | pass |
| 12 | next | Reply on CX7-2 and CX7-3; push `e274fbf` and this record; resolve both threads | — |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| AQ-1 (S21 ADR, `Proposed`) | Product Owner | pending; before #668 merges |
| Codex review and hosted CI on the new head | PR-35 | after push |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure. The PF10 file change is the Product Owner's direction; this session does not number, adopt or claim canonical status for it.
