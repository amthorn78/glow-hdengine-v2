---
artifact_type: PROMPT_ECOSYSTEM_PLAN_RECONCILIATION
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
subject: Every box on the six-batch plan, settled against the evidence already in docs/ephemeral/
supersedes: nothing in place; successor to the 2026-09-21 reconciliation written earlier the same day onto the plan page
---

# The plan checklist, reconciled against evidence

**71 of the plan's 112 boxes are ticked, 34 are superseded and will never be ticked, and 7 remain
genuinely open — three of the seven are two items duplicated between §12 and §13, so the real
remainder is five pieces of work.** Applied to the Notion page
*GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1* on 2026-09-21 and verified
by re-fetch: 71 checked, 41 unchecked, composition exactly as stated below.

Every tick rests on a named artifact in `docs/ephemeral/` or a ruling in
`docs/prompt_ecosystem_management/gcfpe.decision-record.md`. None rests on a session's memory.

## The correction that prompted this

An earlier reconciliation the same day recorded **Batch 2** as `UNDETERMINED — the one real hole`,
and said settling it would need "the Drive report, or the Batch 2 session record". That was wrong.
`docs/ephemeral/gcfpe.batch-2.repair-report.md` — 40,791 bytes — has been in the repository the
whole time and settles it outright. The earlier note is dated and is not edited in place
(`AUTH-001`); this is its successor.

The failure was not a missing artifact. It was reaching for a remote source without first reading
the local one that was already listed on disk.

## Batch 2 — closed

Header: `verdict: BATCH_2_BLOCKER_OBSOLETE_PENDING_CURRENT_STATE_VERIFICATION  # was BATCH_2_BLOCKED; see decision record D10`

| Question | Answer | Evidence |
|---|---|---|
| Were the seven prompts repaired? | Yes | §11 — `IA-10`, `IA-20`, `IA-30`, `IA-40`, `IA-50`, `IA-60`, `UTIL-10` each `REPAIRED_AND_VERIFIED`. No prompt is `BLOCKED_WITH_EVIDENCE`: "the blocker is control-side and tooling-side, not prompt-side" |
| Were the contract findings closed? | Yes | 22 of 22 against the persisted bodies; static/tabletop cases A–J all PASS |
| What actually blocked it? | `BLOCKED_ON_DRIVE_CONTENT_WRITE_CAPABILITY` | The synchronized graph, the rebound control copy and report v1.1 could not be persisted — the Drive connector has no content-write for an existing file ID |
| Is that blocker alive? | **No — structurally dead** | `D10`: the graph is no longer a Drive file. It is parts in `docs/graph/parts/`, the assembled artifact is deliberately never persisted, and storage authority is the repository |
| `D10` asked for a bounded current-state verification. Done? | **Yes, twice** | The release-wide gate ran the registry validator against all 55 live bodies — 721 assertions, 0 failing, 0 rows drift against the graph. Round 23's end-to-end validator ran all 55 bodies at **0 errors** against the installed skills |
| Is the §7 graph redline still owed? | No — no subject | Its targets (`NATHAN_MANUAL_PF10_DRAIN`, the drain vocabularies, the IA-30/IA-40 branches) were removed or rebuilt corpus-wide under `D6`, `D13` and `D15`. The graph reproduces its proof token from committed parts |

"A batch status is not preserved for its own sake" (`D10`). It is clean, so it closes.

## What each group of ticks rests on

| Group | Boxes | Evidence |
|---|---|---|
| §5 per-prompt instrument | 19 of 20 | Applied to all 55: Batch 1's contract and copy/repair ledgers (11 prompts), Batch 2's contract ledger and §11 dispositions (7), the consolidated pass (37, four lanes at full roster — 10/10, 10/10, 9/9, 8/8 — 62 findings, 9 prompts clean). Corpus-level closure by the release-wide gate |
| §7 Batch 1 | 6 of 6 | `gcfpe.batch-1.repair-report.md` §5 records all six criteria **MET**, each with its own measurement: lane symmetry from the rebuilt graph, `never_for: INITIAL_APPROVAL`, `exactly_one_per_qualifying_approval: true`, producer set `[CF-C-30, CF-E-30, ESC-40, IA-30, QA-70, RS-20]` |
| §7 Batch 2 | 6 of 6 | The table above, plus the current-PF10 and approved-base obligations validated at 0 errors across all 55 bodies, and interface closure at 0 rows drift |
| §8 coverage proof | 4 of 4 | 37 + 18 = 55, no duplicates, none unassigned; the approved registry carries exactly 55 prompt rows and no control, skill, report or fixture |
| §10 skill-review questions | 9 of 10 | `gcfpe.workflow-skill-fit-review-round10.md` §B answers all ten by number. Q9 found two obsolete bindings; both repaired — `SF10-04` retired and `SF10-05`'s disclaimer added in round 20, installed since |
| §12 final criteria | 15 of 17 | The release-wide gate for routing, states and interfaces; the storage pass for `D7`; the drainage-removal pass for `D6`; rounds 20–23 for controls and fixtures — end-to-end 55 bodies at 0 errors, 155 contract fixtures and 179 body fixtures passing |
| §13 Execution | Batch 2 | As above |

Two ticks worth naming because they are easy to doubt:

- **"Ordinary PR work does not require QA Guide or QA Plan artifacts."** `PR-20`'s registry row
  declares exactly one input, `PR_INSTRUCTION_ID`, and that row is validated against the live body.
- **"No PF document version is pinned anywhere in the prompt."** The registry carries zero version
  pins and zero occurrences of *CRD Plan*, against eight of *CRD Specification*.

## Superseded — 34 boxes that will never be ticked

- **29** Batch 3–6 acceptance criteria and **4** Batch 3–6 execution lines. `D12` retired the batch
  sequence; those lanes were covered by the consolidated pass and the release-wide gate, both
  already ticked. The headings carry the supersession so no future session executes them.
- **1** §10 question about `glow-hde-devops`. `D16`: no DevOps skill exists, none is required, and
  none is to be created.

An unticked superseded box is not open work. It records a question that stopped existing.

## Genuinely open — five pieces of work

| # | Item | Where | What closes it |
|---|---|---|---|
| 1 | Optional inputs have an exact predicate and do not silently become mandatory | §5 | The only §5 line without corpus-level evidence. Batches 1 and 2 verified it per prompt for their 18; the consolidated pass corrected input tokens for the other 37 but did not restate the predicate test. One pass over the 37 registry rows closes it |
| 2 | Final prompt/control snapshot frozen | §13 | `freeze.py` beside this file is the recorded, reproducible recipe. Run it over the final tree once items 3 and 4 have landed |
| 3 | Dedicated skill review complete with `SKILL_FIT_CONFIRMED` | §12, §13 | Round 23's §10 returned `SKILL_FIT_CONFIRMED` **on the installed bytes**, with `F1` accepted and carried: `validator_revision` 3.2.8 → 3.2.9 at four sites, `FLOWMASTER_VALIDATE_REVISION` 3.2.10 → 3.2.11 alongside. Shipping `F1` changes `flowmaster-validate` bytes, so it needs its own §10. Left unticked deliberately — a confirmation that reopens is not a closed gate |
| 4 | Separate independent post-flight passes with no mandatory open finding | §12, §13 | `amthor-workspace-governance-audit` in `BATCH_POSTFLIGHT` mode with `flowmaster-validate`, run **after** item 3 lands. It is the last gate before promotion, not a step with work behind it |
| 5 | Product Owner promotion decision packet prepared | §13 | Assembled from items 2–4 |

Items 3 and 4 appear twice each, once in §12 and once in §13; they are the same two gates.

## The durable lesson

The plan showed 101 open boxes and 11 closed while the work behind 60 of them was finished and
written down. A checklist that is not reconciled stops being a tracker and becomes a second,
contradictory record — and the cost lands on whoever reads it next, who either redoes finished work
or distrusts the whole page. The reconciliation is cheap; the drift is not.
