---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.17"
result: none (PR-35 checkpoint; v1.16's MERGE_PENDING withdrawn; CX7-17, CX7-18 and the PO-35-15 audit fixed; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.16.md (preserved unchanged; its MERGE_PENDING is withdrawn by this record)
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
remote_head_before_push: 477570dddcb0fb471bff6ab1a5a614efc414654a
commits_in_this_push: 4fac34f (CX7-17, CX7-18 and the audit fixes), 5d4fe1a (the ADR's PO-35-13 to PO-35-19 lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T13:31:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.17 (PR-35 checkpoint)

## 1. State

Nonterminal. **v1.16's `MERGE_PENDING` is withdrawn.** #668 is not merge-ready until this push is reviewed and its CI is green.

- **Hosted CI on `477570d` passed** (run 39600172741, 12:30:43Z to 12:51:45Z).
- **Codex round 16** (review 5599806914 on `477570d`, 12:41:32Z) raised two new P1s on real inputs, CX7-17 and CX7-18 (§3). v1.16's predicate "Review findings resolved on the current head" therefore no longer holds.
- **Design questions.** Both findings needed a design choice, so the session asked the Product Owner, as PO-35-7 directs. Codex had raised one or two new P1s on nearly every push since round 10, each in a different part of the v2 contract. So the session also asked whether to audit the rest of the contract against canon in one pass. The Product Owner said yes (PO-35-15) and decided the audit's design choices (PO-35-16 to PO-35-19) (§2, §4).
- **The fix.** CX7-17, CX7-18 and every audit gap that a real input reaches are fixed in `4fac34f`. The ADR records them in `5d4fe1a`. Both commits are in this push.

## 2. Product Owner decisions

| ID | Question | Decision |
| :- | :- | :- |
| PO-35-13 | CX7-17: the writer refuses `SATISFIED` whenever a QA ledger status is not `PASS`, even under an explicit closure override. An accepted gap is free text and names no check. How should the override exempt a check? | "Gap names its check (Recommended)":<br>• each accepted gap has a required `check_id`;<br>• `SATISFIED` may carry a non-`PASS` check only if that check is `TOOLING_BLOCKED` and exactly one accepted gap names it;<br>• `FAIL_BEHAVIOR`, `FAIL_TOOLING` and `PARKED` still block;<br>• an accepted gap that names a `PASS` or unknown check is refused |
| PO-35-14 | CX7-18: posture `po_closeout` is accepted with nothing binding a Product Owner decision, and no canonical PO-decision record format exists. What should the writer do? | "Drop po_closeout (Recommended)":<br>• `po_closeout` is removed from the v2 posture enum, which is a typed schema refusal;<br>• the writer states only `review_trace_only` or `formal_close_pack_completion`;<br>• PO closeout stays the Product Owner's separate action |
| PO-35-15 | Before the next push, audit the whole remaining v2 contract against canon in one pass, and fix every gap a real input reaches? | "Yes, one pass (Recommended)": one audit table, with the fixes in the same push as CX7-17 and CX7-18 |
| PO-35-16 | Audit A4 and A5: PF-title fields only have to look like titles, so a nonexistent title passes. How should a PF title be validated? | "Derive from canon filenames (Recommended)":<br>• a title must equal a name derived from a tracked `docs/pfcanon/` file: after the PF number and kind, before the version, hyphens as spaces, `&` read as `and`;<br>• the later-drain canon homes use the same rule;<br>• the refusal is `PF_TITLE_UNKNOWN` |
| PO-35-17 | Audit A6: a deferral's `drain_target` is free text. How should the pointer form be checked? | "Register heading pointer (Recommended)":<br>• `drain_target` becomes `{binding, heading}`;<br>• the binding is the change kind's register (PF09 for an Epic, PF30 for a CRD), and that file holds the heading;<br>• the deferral's ID still occurs in the drain-targets ledger |
| PO-35-18 | Audit A7: the report renders no coverage ledger and never reads the QA plan. What should the writer do? | "Pin plan, render ledger (Recommended)":<br>• bind the change's current QA plan and read its ``### CHECK <n> `<id>` `` headings in order;<br>• render the coverage ledger from the QA ledger;<br>• `SATISFIED` needs every planned check `PASS` or an accepted gap, and every ledger check must be planned |
| PO-35-19 | Audit A8: the schema has no PR-to-deliverable allocation and no reuse boundary. What should the writer do? | "Required allocation field (Recommended)":<br>• a required `allocation` list of `{slice, deliverable}`, where a slice is a work-unit ID or a PR reference, and one entry is enough for a single-slice close;<br>• a `reuse_boundary` list of lines (see §7 for its form);<br>• both are rendered as their own sections;<br>• every deliverable must appear in the allocation |

## 3. Review findings (round 16)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-17 | Codex, `477570d`, P1 (comment 4336903519, thread `PRRT_kwDOP103ks6uxE8h`) | `tools/qa/generate_epic_close_pack.py`, the `SATISFIED` all-`PASS` rule | An explicit closure override for a `TOOLING_BLOCKED` check still gives `DECISION_CONTRADICTION`, so the writer cannot express the governed closeout path that Change Process Guide §3.5.4 "Closure override (rare; explicit)" provides | Yes: the operator supplies the source and the tracked ledger through `--source`. Reproduced on `477570d` (§6 row 2) | Fixed under PO-35-13 (addendum 2.14 rule 2). The thread is answered and stays open until the next review |
| CX7-18 | Codex, `477570d`, P1 (comment 4336903506, thread `PRRT_kwDOP103ks6uxE8a`) | `schemas/close_candidate_source.v2.json`, the posture enum | `posture: po_closeout` renders "Decision posture: PO closeout" from evidence inputs alone, with no authorized decision bound | Yes, by the same interface. Reproduced on `477570d`: it writes, exit 0, and the report states "PO closeout" | Fixed under PO-35-14, as a typed refusal (addendum 2.14 rule 2: refusing is correct, because PO closeout is the Product Owner's own action). The thread is answered and stays open until the next review |

The canon read:
- **Change Process Guide:** §3.5.4 "ADR block in the close-pack (all epics)", including "Closure override (rare; explicit)" and "No posture-only PASS"; §0.4.1.2 "Mandatory QA RCA & Doc Delta summary", Location (normative); and the separate closure axes, under which PO closeout is a PO-owned action.
- **HDE Governance:** "Close report minimal content (normative)", including:
  - the reuse-boundary and PR-to-deliverable allocation summaries;
  - the "No over-claim rule";
  - "Coverage vs QA Plan accounting";
  - the deviation and receipt accounting;
  - the "Step evidence rule for closeout".
- **Glow QA Guide:** "Exact PF19 QA vocabulary".

**Rule 8.** Round 15 was clean, so rounds 15 and 16 do not raise the same class twice in a row. The Product Owner's audit (PO-35-15) answers the wider pattern of one new finding per round.

The review history across sixteen rounds:
- seventeen P1s, CX7-1 to CX7-10 and CX7-12 to CX7-18, all fixed;
- one P2, CX7-11, with a stated limit.

Three further rounds failed on the Codex usage limit.

## 4. The PO-35-15 audit

Every v2 contract part that round 16 did not raise was checked against the canon read in §3, with one row per gap or limit.

| # | Contract part | Canon | Finding | Disposition |
| :- | :- | :- | :- | :- |
| A1 | Closure override | Change Process Guide §3.5.4 | CX7-17 | Fixed (PO-35-13) |
| A2 | Decision posture | Change Process Guide, closure axes | CX7-18 | Fixed (PO-35-14) |
| A3 | Bound QA RCA | Change Process Guide §0.4.1.2: a separate summary "MUST use the canonical filename `audit/EPIC-<NNN>_QA_RCA.md`" | Any tracked file could be bound as the RCA. Reproduced on `477570d`: an RCA bound to `evidence/qa_report.md` writes, exit 0 | Fixed: the binding must be `audit/<prefix>_QA_RCA.md`, where the prefix is the close report's own (`QA_RCA_UNBOUND`). Canon gives the rule, so no question was needed |
| A4, A5 | PF titles: ADR bounding canon, ADR Doc Delta targets, accepted-gap drain targets, later-drain canon homes | Change Process Guide §3.5.4 (titles only) | A nonexistent title passed. Reproduced: `No Such Canon Document` writes, exit 0 | Fixed (PO-35-16; `PF_TITLE_UNKNOWN`) |
| A6 | Deferral drain target | HDE Schemas & Artifacts §1.2 ("its drain target pointer (PF09 pointer) when available") | The pointer was free text. Reproduced: `somewhere, eventually` writes, exit 0 | Fixed (PO-35-17; `DEFERRAL_POINTER_UNBOUND`) |
| A7 | Coverage versus the QA plan | HDE Governance "Coverage vs QA Plan accounting" | No coverage ledger, and the QA plan was never read. Reproduced: the report has no such section | Fixed (PO-35-18; `QA_PLAN_NOT_CURRENT`, `QA_PLAN_STEPS_ABSENT`, `QA_COVERAGE_INVALID`) |
| A8 | Allocation and reuse boundary | HDE Governance, close-report minimal content | Neither existed. Reproduced: no such sections | Fixed (PO-35-19; `ALLOCATION_INCOMPLETE`) |
| A9 | Over-claim | HDE Governance "No over-claim rule" | The fixed nonclaims did not cover merge provenance, board state, Isis terminal closure or formal Ops action. Reproduced: no such line | Fixed: one fixed nonclaim line in every v2 report. Canon gives the rule |
| A10 | Superseded artifacts | Change Process Guide §3.5.2.1 (a `SATISFIED` close after a different interim verdict names the superseded artifact and the evidence change) | Each entry is a bound tracked input with a stated evidence change. The writer cannot tell whether an earlier verdict exists or judge that the file was in fact superseded | Stated limit (ADR: narrative fields) |
| A11 | ADR texts must not restate canon | Change Process Guide §3.5.4 | Title fields are now checked (A4). A statement or decision text could still paraphrase canon | Stated limit (ADR: narrative fields) |
| A12 | Narrative fields: delivered scope, limitations, follow-ups, rationales, evidence changes, ADR texts, gap texts, the reuse boundary | HDE Governance, close-report minimal content | Free single lines in named fields. Their truth is the author's and the close review's to judge | Stated limit (ADR, new line) |
| A13 | Source-of-truth posture and the required-elements checklist | HDE Governance "Closeout review inputs posture" and "Required-elements checklist", both "when a closeout recommendation is issued" | These belong to the closeout recommendation record, and their RCA elements belong to the QA RCA, which the report embeds or binds (A3). The writer issues no recommendation | No change |
| A14 | Key outputs | HDE Governance "Close-pack manifest `key_outputs` shape (normative)" | Already bound: every key output other than the report and the manifest is a bound tracked input (ADR decision 5) | No change |
| A15 | Verification statement | Change Process Guide §3.5.2.1 ("an explicit verification statement that the close-pack baseline artifacts exist at the canonical filenames") | Fixed text rendered by the writer at the canonical paths | No change |
| A16 | Step evidence for a `PASS` step | HDE Governance "Step evidence rule for closeout" | Met: each ledger entry's tracked primary is checked against its header and recorded under Source bindings | No change |
| A17 | Deviation notes; original versus accepted receipts | HDE Governance "Accepted execution-deviation accounting" and "Original-versus-accepted receipt accounting" | Narrative records of the QA run, carried by the QA RCA or the step-log manifest. The coverage ledger records only status and impact | Stated limit (ADR, the QA-plan line) |

## 5. Implementation

- **`schemas/close_candidate_source.v2.json`** (`4fac34f`):
  - the posture enum is `review_trace_only` and `formal_close_pack_completion`;
  - each accepted gap has a required `check_id`;
  - each PF-title field references `pf_title`;
  - a deferral's `drain_target` is `{binding, heading}`;
  - new required fields: `qa_plan_binding`, `allocation` (at least one `{slice, deliverable}`) and `reuse_boundary` (may be empty).
- **`tools/qa/generate_epic_close_pack.py`** (`4fac34f`):
  - the QA plan pin and its check reader;
  - the coverage ledger, which also checks the closure override;
  - the `SATISFIED` rule now refuses only a planned check that is neither `PASS` nor an accepted gap;
  - the QA RCA path, PF-title, allocation and register-heading checks;
  - three new report sections ("Coverage versus the QA plan", "PR-to-deliverable allocation", "Reuse boundary"), the accepted gap's check ID in the ADR block, the deferral pointer's register and heading, and the fixed nonclaim line;
  - `po_closeout` removed from the posture text.
- **`tests/qa/test_generate_epic_close_pack.py`** (`4fac34f`):
  - the fixture binds a QA plan, the canonical RCA and a register heading;
  - nine new tests, 39 cases, including the real HDE-EPIC040 QA plan v1.2 against its tracked ledger (12 checks in plan order) and every real `docs/pfcanon/` file name.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`5d4fe1a`): decision 4's report content, decision 9's override and title rule, the posture limit, and seven new stated-limit lines. The amendment line now records PO-35-13 to PO-35-19 and the two canon-given rules.

## 6. Local checks

All runs were in this session's clones, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `4fac34f` | 883 passed (844 before, plus 39 new cases) |
| 2 | Negative controls on the pre-fix writer (`477570d`) | Every gap reproduces behaviourally:<br>• `po_closeout` writes, exit 0, and the report states "PO closeout";<br>• the governed `TOOLING_BLOCKED` path under an override is refused (`DECISION_CONTRADICTION`);<br>• an override that names no check, with every check `PASS`, writes, exit 0;<br>• an unknown PF title writes, exit 0;<br>• a free-text drain target writes, exit 0;<br>• an RCA bound to an arbitrary file writes, exit 0;<br>• the report has no coverage, allocation or reuse-boundary section and no fixed over-claim line |
| 3 | Replay of `5d4fe1a`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 13:10:56Z to 13:29:15Z, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, exit 0:<br>• changed tests 4,499 passed, 2 skipped;<br>• product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 |

## 7. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| `reuse_boundary` is required and may be empty, rather than optional as PO-35-19's option text said | `schemas/close_candidate_source.v2.json` | Plan v1.1's PD-1 makes every v2 property required, and `test_v2_schema_is_closed_and_shares_the_v1_feedback_refusal` holds it. An empty list is the absent case, and the report then states "None recorded." | §6 row 1 | the next Codex round |
| A duplicated accepted gap is refused by the writer (`CLOSURE_OVERRIDE_INVALID`), not by schema `uniqueItems` | `tools/qa/generate_epic_close_pack.py` | Two gaps for one check differ in their texts, so `uniqueItems` would not catch them | §6 row 1 | same |
| The QA RCA path is derived from the close report's own prefix | same | Canon names the Epic form, and a CRD uses its ID as the prefix (ADR decision 3) | §6 row 1 | same |
| The test fixture creates a placeholder for every real `docs/pfcanon/PF*.md` name, and real copies of the two registers | `tests/qa/test_generate_epic_close_pack.py` | The PF-title rule reads tracked file names, and the register check reads real headings | §6 row 1 | same |
| The writer's RCA comment cites Change Process Guide §0.4.1.2, where the canonical filename rule is | `tools/qa/generate_epic_close_pack.py`, test comment | HDE Schemas & Artifacts §1.2 does not state that rule | read on `main` | same |

## 8. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 24 hours 16 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 16 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 19 runs:
  - 14 successes: 6 on ubuntu-24.04, 2 on ubuntu-26.04 with the image read (`c9bff83`, `a2ba526`), and 6 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`, `3eb31c3`, `f6e1ad0`, `477570d`);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-19.

## 9. PR_REMOTE_ACTION_LEDGER (continues v1.16 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 98 | ~12:30 | Push `a2ba526..477570d` (record v1.16) | pushed and read back |
| 99 | 12:30 to 12:51 | Hosted `test` on `477570d` (run 39600172741) | success |
| 100 | 12:31 | Check-in `trig_016fdUS5zmaKBKve6xiWdg5b` armed for 13:22 | armed |
| 101 | 12:41 | Codex review 5599806914 on `477570d` | CX7-17 and CX7-18 (P1) |
| 102 | 12:43 to 12:53 | Design questions to the Product Owner | PO-35-13 to PO-35-19 |
| 103 | 13:11 | Delete the check-in, which was armed for the withdrawn `MERGE_PENDING` | deleted |
| 104 | next | Replies on CX7-17 and CX7-18; push `477570d..` this record; update #668's description | — |

## 10. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-17 and CX7-18 threads | this session; Codex | open until the next review of the pushed head answers them |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (`MERGE_PENDING`), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
