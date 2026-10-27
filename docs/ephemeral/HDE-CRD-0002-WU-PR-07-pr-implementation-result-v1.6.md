---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.6"
result: none (PR-35 checkpoint after the fifth corrective commit; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.5.md (preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.5.md (on this branch; read as provenance)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: 45e4cefb84e5fc8945502f9404f469b76dd4b20e
corrective_commit: 6392102412bf7d3531ed65833d96c2c0a8ce44f6
adr_proposal: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.1.md (supersedes v1.0, which is preserved)
created_at: 2026-10-20T23:10:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.6 (PR-35 checkpoint)

## 1. State

Nonterminal. Codex round 5, on `45e4cef`, completed at 22:59:26Z (review 5592846633).
- It did not re-raise CX7-6. Its thread was resolved at about 23:00Z under addendum 2.14.
- It raised one P1, CX7-7, in the same class. The session asked the Product Owner one design question and got PO-35-4 (§2).

The fix is `6392102`, pushed with this record and ADR proposal v1.1.

## 2. Product Owner decision PO-35-4 (round 5)

The options offered:
- pin the ledger format (recommended);
- pin the format and the primaries;
- rescope.

No stated-limit option was offered, under addendum 2.14 rule 4. **Answer: "Pin the ledger format (Recommended)".** The option's text:
- the bound ledger must be a nonempty flat mapping in the format `{check_id: {check_id, log_path, status}}`;
- each entry needs exact keys, a matching `check_id`, and `log_path` `audit/qa/<change-dir>/checks/<id>/primary.log`; otherwise `QA_LEDGER_INVALID`;
- `SATISFIED` needs every status to be `PASS`; otherwise `DECISION_CONTRADICTION`;
- the writer stays stdlib plus `jsonschema` (instruction ID-10).

## 3. Review findings (round 5)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-7 | Codex, `45e4cef`, P1 (thread on comment 4331227614) | `_require_v2_semantics` | The writer never read the bound QA ledger, so `SATISFIED` passed with `{}` | The literal `{}` comes only from a hand edit, which AGENTS.md forbids for governed artifacts, or a test fixture: the canonical harness refuses an empty CRD manifest ("CRD manifest must be a nonempty flat mapping"). The same gap also let a real ledger that records a `FAIL_BEHAVIOR` check back a `SATISFIED` close, and the harness does record such statuses. That is real | Fixed in `6392102` (PO-35-4) |

## 4. Local checks on `6392102`

Detached clone, closed rails, CPython 3.12.3, CI's install (as v1.1 §4).

**Negative control.** The new test file against the pre-fix writer (`45e4cef`), on the `qa_ledger` selection: 10 failed, 1 passed.
- Six failures are behavioral: the old writer wrote with `{}`, `[]`, non-JSON, a wrong `log_path`, a mismatched `check_id`, and `SATISFIED` over a `FAIL_BEHAVIOR` ledger.
- Four failures are the real-ledger pin cases, which call the new `_qa_ledger_statuses`.
- The pass is the guard that `NOT SATISFIED` over a failed check still writes.

**Writer test file** (`tests/qa/test_generate_epic_close_pack.py`): 493 passed (482 + 11), exit 0, 23:06:30 to 23:07:50. The copy was clean afterwards.

**Real ledgers.** The pinned format reads all four tracked ledgers, each nonempty and all `PASS`:
- `audit/qa/hde-crd-0001/`;
- `audit/qa/hde-epic021/`;
- `audit/qa/hde-epic039/`;
- `audit/qa/hde-epic040/`.

**Replay** of `prepush_check.py --base 45e4cef --head 6392102`: **PASS**, 23:09 to 23:19:58. Lanes `evidence,qa` (3 paths); `ci.yml` the pinned one; step 08 changed tests 639 passed; step 13 evidence 134 passed; step 14 qa 488 passed; step 16 SUCCESS; copy clean; repository unchanged. Not CI's result. The proposal v1.1 and this record, both under `docs/ephemeral/`, add no lane.

## 5. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| PO-35-4 implemented as stated (§2) | Product Owner decision | §4 |
| The default test fixture's ledger becomes a one-check `PASS` ledger in the pinned format | The fixture's `{}` is now refused | 493 passed |
| ADR stated limits gain one line: the pinned ledger format, and that the writer reads the ledger but does not open the primaries | Rule 5 stated limit; true description of the check | `QA_LEDGER_INVALID` cases |
| ADR proposal v1.1 issued instead of editing the published v1.0 | An issued version is never edited | — |

## 6. Spend against the ceiling (instruction ID-1)

- **Sessions:** 4 of 4.
- **Codex rounds:** 5 completed, plus two that failed on the usage limit.
- **Elapsed:** within 3 days, excluding Product Owner waits.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.5 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 31 | 22:56 | Reply on CX7-6; push `0d50b06..45e4cef` | pushed and read back (proposal v1.0 sha256 d11c69d0…, v1.5 sha256 13a4c307…) |
| 32 | 22:59 | Codex review 5592846633 on `45e4cef` | CX7-7 (P1); CX7-6 not re-raised |
| 33 | ~23:00 | Resolve CX7-6 thread | resolved |
| 34 | ~23:02 | Rule 8 question (CX7-7) | PO-35-4 |
| 35 | 23:08 | Local fix and checks (§4) | pass |
| 36 | next | Reply on CX7-7; push the fix, proposal v1.1 and this record; CX7-7 thread open until Codex's next review answers it | — |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| AQ-1 (S21 ADR) | IA review of proposal v1.1, then the Product Owner | proposal v1.1 published with this push |
| Codex review and hosted CI on the new head | PR-35 | after push |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure.
