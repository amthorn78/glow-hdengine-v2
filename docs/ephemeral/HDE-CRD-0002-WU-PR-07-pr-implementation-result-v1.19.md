---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.19"
result: none (PR-35 checkpoint; CX7-20 and CX7-21 fixed under PO-35-20 and PO-35-21; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.18.md (preserved unchanged)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
companion_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/670 (against main; head 606e1b4, hosted CI green on ubuntu-26.04; carried by #668; the Product Owner merges it)
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: cec83675a85da70942cc46edff241fe6b9345769
commits_in_this_push: d50cddb (CX7-20 and CX7-21), f458e1f (the ADR's lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T14:55:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.19 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Hosted CI on `cec8367` passed** (run 39614126924, 14:07:56Z to 14:28:44Z).
- **Codex round 18** (review 5601135022 on `cec8367`, 14:14:34Z):
  - it did not re-raise CX7-19, so that thread is resolved;
  - it raised two new P1s on real inputs, CX7-20 and CX7-21 (§3).
- **Design questions.** Both findings needed a design choice, so the session asked the Product Owner once, as PO-35-7 directs. The answers are PO-35-20 and PO-35-21 (§2).
- **The fix.** It is in `d50cddb`, and the ADR's lines are in `f458e1f`. Both are in this push.

## 2. Product Owner decisions

| ID | Question | Decision |
| :- | :- | :- |
| PO-35-20 | CX7-20: a source can declare `SATISFIED` with `formal_close_pack_completion`, and nothing binds an authorized decision. How should the writer bind closure authority? | "QA report; review-trace (Recommended)":<br>• bind the change's current QA report (`docs/ephemeral/<change-id>-QA120-qa-report-v<N>.<N>.md`, highest version, `artifact_type: QA_REPORT`, the same `change_id`);<br>• `SATISFIED` needs `verdict: PASS`, and the report names it as the authorized decision;<br>• remove `formal_close_pack_completion`, so every v2 report is review-trace-only and formal completion stays with the close PR's merge and Isis |
| PO-35-21 | CX7-21: a `MET` row can bind any tracked input, even the Specification itself. What should a `MET` row need? | "Plan-mapped PASS check (Recommended)":<br>• each `MET` row binds at least one QA primary that the ledger records as `PASS`, and whose check's mapping line names the criterion;<br>• ranges such as `K040-REQ-003 to K040-REQ-006` are read;<br>• otherwise `ACCEPTANCE_EVIDENCE_UNBOUND`;<br>• `SATISFIED` then needs a QA plan that maps every criterion |

Both questions were sent at about 14:15Z and answered at 14:20:24Z.

## 3. Review findings (round 18)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-19 | Codex, `5bf0db6`, P1 | fixed in `46ab9d2` (v1.18) | — | — | Round 18 did not re-raise it; the thread is resolved |
| CX7-20 | Codex, `cec8367`, P1 (comment 4337923607, thread `PRRT_kwDOP103ks6uzf4P`) | `tools/qa/generate_epic_close_pack.py`, the decision check | `SATISFIED` with `formal_close_pack_completion` renders from the source's own assertion, with no authorized decision bound | Yes: the operator supplies the source through `--source`. Reproduced on `cec8367`: it writes, exit 0, and the report states "formal close-pack completion" and binds no decision | Fixed under PO-35-20 (addendum 2.14 rules 2 and 4). The thread is answered and stays open until the next review |
| CX7-21 | Codex, `cec8367`, P1 (comment 4337923621, thread `PRRT_kwDOP103ks6uzf4Y`) | same file, the acceptance binding check | A `MET` row only has to name bindings that resolve, so it may bind the Specification alone or an unrelated file | Yes, by the same interface. Reproduced on `cec8367`: both cases write, exit 0 | Fixed under PO-35-21. The thread is answered and stays open until the next review |

The canon read on `main`:
- Change Process Guide §3.5.2.1: the acceptance section binds each criterion to "the exact final candidate, relied-upon checks or governed evidence, applicable results and limitations, and authorized decision".
- Change Process Guide, "Final QA Closeout Review + QA RCA": formal close-pack completion is marked "not performed, no claim, or not proven" unless directly proven.
- Change Process Guide §3.5.4, "No posture-only PASS".
- HDE Schemas & Artifacts §1.2: a closure-trace decision states its posture, and review-trace satisfaction is not presented as more.
- Plan Templates, the QA check block's "Surface / D-goal mapping:" line.
- HDE Build Notes addendum 2.14 rules 2 and 4: no stated limit for a P1 on a real input.

**Rule 8.** CX7-20 is in the same class as round 16's CX7-18: a posture that claims more than its bound inputs. Rounds 16 and 18 are not consecutive, but the design question was put to the Product Owner anyway, under PO-35-7.

The review history across eighteen rounds:
- twenty P1s, CX7-1 to CX7-10 and CX7-12 to CX7-21, all fixed;
- one P2, CX7-11, with a stated limit.

Three further rounds failed on the Codex usage limit.

## 4. The new rules checked against tracked inputs

| Rule | Tracked inputs | Result |
| :- | :- | :- |
| The QA report (PO-35-20) | every `docs/ephemeral/` record with a `verdict:` line | One `QA_REPORT` exists, HDE-EPIC040's QA-120 report, with `verdict: PASS`. It meets the pinned front matter, and its file name meets the pinned form (§6 row 1) |
| The plan mapping (PO-35-21) | HDE-EPIC040's QA plan v1.2 and its Specification | 20 of the 22 requirement IDs are mapped, and the plan's range is read. K040-REQ-001 and K040-REQ-002, both documentary, map to no check, so a source shaped like HDE-EPIC040's cannot be `SATISFIED` until its plan maps them. That is PO-35-21's stated consequence, not a defect |
| Primaries as evidence inputs | the 140 primaries named by the tracked QA ledgers | none is refused by the feedback-dependency or report-structure rules, so each can be bound |

## 5. Implementation

- **`schemas/close_candidate_source.v2.json`** (`d50cddb`):
  - the posture enum is `review_trace_only` only;
  - a new required `qa_report_binding`.
- **`tools/qa/generate_epic_close_pack.py`** (`d50cddb`):
  - `QA_REPORT_RE` and `_qa_report_verdict`: the QA report's pin and front matter;
  - `QA_REPORT_NOT_CURRENT` and `QA_REPORT_INVALID`; `SATISFIED` needs `verdict: PASS`;
  - `_qa_plan_mapping`: each planned check's criteria, read from the first "Surface / D-goal mapping:" line of its section, with ranges;
  - `ACCEPTANCE_EVIDENCE_UNBOUND`: each `MET` row binds a mapped `PASS` primary;
  - the acceptance section's "Authorized decision" line;
  - `formal_close_pack_completion` removed from the posture text, and formal close-pack completion added to the no-over-claim line.
- **`tests/qa/test_generate_epic_close_pack.py`** (`d50cddb`):
  - the fixture binds a QA report and its check's primary, and its QA plan maps every criterion;
  - helpers `_bind_proof_check` and `_write_proof_check` add a second, `PASS` check where the first is under test;
  - four new tests, 19 cases, including the real HDE-EPIC040 QA-120 report and QA plan.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`f458e1f`):
  - decision 4's report content;
  - the posture limit;
  - two new stated-limit lines (the QA report pin and the `MET` evidence rule);
  - the amendment line's record of PO-35-20 and PO-35-21.

## 6. Local checks

All runs were in this session's clones, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `d50cddb` | 905 passed (886 before, plus 19 new cases) |
| 2 | Negative controls on the pre-fix writer (`cec8367`), with its own fixtures | All three reproduce, each writing with exit 0:<br>• a `formal close-pack completion` `SATISFIED` report that binds no decision;<br>• a `MET` row bound only to the Specification;<br>• a `MET` row bound only to an unrelated file |
| 3 | Replay of `f458e1f`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 14:36:14Z to 14:55:12Z, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, exit 0:<br>• changed tests 4,521 passed, 2 skipped;<br>• product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 |

## 7. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| A `TOOLING_BLOCKED` check accepted under a closure override supports no `MET` row. The override tests now add a second, `PASS` check that maps the criteria | `tools/qa/generate_epic_close_pack.py`; tests | PO-35-21 names a `PASS` primary, and Change Process Guide §3.5.4 "No posture-only PASS" | §6 row 1 | the next Codex round |
| The QA report's verdict may be any non-empty value, and only `PASS` allows `SATISFIED` | `tools/qa/generate_epic_close_pack.py` | `NOT SATISFIED` must stay writable after a failing QA run | §6 row 1 | same |
| A range counts only when both ends share a prefix and a digit width, and only IDs the Specification defines count | same | It keeps `S03 to S05` and `K040-REQ-003 to K040-REQ-006` exact, with no cost from a wide range | §6 row 1; the real-plan test | same |
| The mapping is read from the first "Surface / D-goal mapping:" line before the section's next heading of level 1 to 3 | same | That is where Plan Templates puts it, and it keeps a later section's text from mapping an earlier check | the real-plan test | same |
| The no-over-claim line also names formal close-pack completion | same | HDE Governance's "No over-claim rule" lists it, and the writer no longer states that posture | §6 row 1 | same |

## 8. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 25 hours 41 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 18 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 21 runs:
  - 16 successes: 6 on ubuntu-24.04, 2 on ubuntu-26.04 with the image read (`c9bff83`, `a2ba526`), and 8 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`, `3eb31c3`, `f6e1ad0`, `477570d`, `5bf0db6`, `cec8367`);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-21.

## 9. PR_REMOTE_ACTION_LEDGER (continues v1.18 §8)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 109 | 14:06 to 14:08 | Reply on CX7-19; push `5bf0db6..cec8367`; update #668's description; check-in `trig_01BT991xnng87kS8zX18ebnM` armed for 14:58 | pushed and read back |
| 110 | 14:07 to 14:28 | Hosted `test` on `cec8367` (run 39614126924) | success |
| 111 | 14:14 | Codex review 5601135022 on `cec8367` | CX7-19 not re-raised; CX7-20 and CX7-21 (P1) |
| 112 | ~14:15 to 14:20 | Design questions to the Product Owner | PO-35-20, PO-35-21 |
| 113 | ~14:38 | Resolve the CX7-19 thread | resolved |
| 114 | 14:56 | Delete check-in `trig_01BT991xnng87kS8zX18ebnM`, armed for the previous head | deleted |
| 115 | next | Replies on CX7-20 and CX7-21; push `cec8367..` this record; update #668's description; re-arm the check-in | — |

## 10. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-20 and CX7-21 threads | this session; Codex | open until the next review of the pushed head answers them |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (`MERGE_PENDING`), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| HDE-CRD-0002's QA plan maps every S-ID to a check, and its QA report follows the QA-120 form, so its own close can be `SATISFIED` | HDE-CRD-0002's QA planning (QA-50) and QA report (QA-120) | a consequence of PO-35-20 and PO-35-21, for the close mutation set after QA |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
