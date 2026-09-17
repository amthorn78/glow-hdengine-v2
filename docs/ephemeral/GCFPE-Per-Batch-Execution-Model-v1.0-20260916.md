# GCFPE Per-Batch Execution Model — Two-Pass Session Structure — v1.0 — 20260916

```yaml
artifact_type: GCFPE_PER_BATCH_EXECUTION_MODEL
artifact_version: "1.0"
created_date: 2026-09-16
status: ACTIVE_FROM_BATCH_2_CONTINUATION
governs: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1
authority_change: NONE
scope_change: NONE
batch_count_change: NONE
```

## 1. Purpose and what this does not change

This document defines **how** each remaining repair batch is executed across sessions. It is an execution-mechanics addendum only.

It does not change the approved plan's authority, scope, batch count, batch membership, per-prompt checklist, completion criteria, or any gate. Six batches remain six batches. The skill-review gate after Batch 6 and the separate independent post-flight remain exactly as approved. Nathan's per-batch execution authorization is still required and is not granted by this document.

## 2. Problem this addresses

Batch 2 execution was interrupted by session token exhaustion, not by a defect in the work. The prior session completed all seven prompt repairs and persisted them, then stopped before control synchronization, post-edit validation, and reporting.

Two facts make this a recurring structural issue rather than a one-time event:

1. Batch 2 is the **smallest** batch at 7 prompts. Batches 3 and 4 carry 10 each, Batch 5 carries 9, Batch 6 carries 8. A budget that did not cover the smallest batch will not reliably cover the larger ones.
2. Section 9 of the approved plan requires supporting-control reconciliation **after every batch**. That cost recurs in all six batches; it is not specific to Batch 2.

## 3. The two-pass model

Each remaining batch executes in two dedicated sessions.

### Pass 1 — Review and repair

Scope: the approved plan's Section 5 per-prompt review-and-repair checklist, applied to every prompt in the batch.

- Pin each complete candidate body, Notion identity, parent, version, lifecycle, and selected predecessor.
- Complete contract review, then copy review, as separate ordered activities.
- Record findings before editing. Distinguish contract defects from copy defects.
- Repair only defects supported by the review.
- Persist each repaired body to Notion and read it back completely.
- Produce the batch Contract Ledger and the batch Copy/Repair Ledger as Drive Markdown in `Glow / Ephemeral Planning Files`, and read both back.

Pass 1 **stops** at that point. It does not synchronize supporting controls, run static/tabletop validation, write the batch report, or issue a verdict.

Exit state:

```text
BATCH_<N>_PROMPT_REPAIRS_PERSISTED
SUPPORTING_CONTROLS_AND_VALIDATION_INCOMPLETE
FINAL_BATCH_<N>_VERDICT_NOT_YET_ISSUED
```

### Pass 2 — Synchronization, validation, and closure

Scope: everything downstream of the persisted repairs.

- Supporting-control synchronization per Section 9 of the approved plan, including the candidate graph contract, direct-handoff fixtures control copy, PE Metaprompt where a concrete Batch-specific contradiction is demonstrated, candidate catalog, Flow Index, and relevant family hubs.
- Static/tabletop validation of the batch cases against the current persisted prompts and synchronized controls.
- Producer/consumer reconciliation and regression review.
- The batch report in `Glow / Ephemeral Planning Files` plus its Notion sibling, both read back.
- Exactly one verdict: `BATCH_<N>_COMPLETE` or `BATCH_<N>_BLOCKED`.
- The next-batch handoff or Product Owner blocker handoff, prepared only.

### Why the split falls here

The seam is placed where the work changes character, not at an arbitrary midpoint.

**Corrected 2026-09-17.** Both passes run in Claude Code; Nathan does not use chat sessions. The seam is a context budget, not a capability boundary.

Pass 1 is many small targeted reads and writes against individual prompt pages in Notion, plus its own two ledgers under `docs/ephemeral/`.

Pass 2 is whole-batch reconciliation across the graph parts and every affected control. Running both in one session is what exhausted Batch 2. The graph is no longer a driver of the split: it is held as parts in `docs/graph/parts/` and rebuilt by script, so no pass loads a 570 KB file. If a later batch shows the budget comfortably covers both, collapsing to a single session per batch is the Product Owner's call and changes nothing else.

## 4. Sub-split thresholds for larger batches

Batch 2's Pass 1 scope was 7 prompts and exhausted a session. Batches at 8 or more prompts should be treated as at risk of the same outcome, and Pass 1 split at the seams below. These seams follow the approved plan's own ordering and contract focus; they introduce no new grouping.

| Batch | Prompts | Pass 1 sub-split seam |
|---|---|---|
| 1 | 11 | Complete. Not applicable. |
| 2 | 7 | Not split. Prompt repairs already persisted. |
| 3 | 10 | `3.01–3.04` PR planning and development lane · `3.05–3.10` rescope, drain continuation, post-merge lineage, manual abort |
| 4 | 10 | `4.01–4.06` QA readiness, Guide, Audit, Plan, review, revision · `4.07–4.10` task creation, execution, evidence review, reporting |
| 5 | 9 | `5.01–5.04` escalation · `5.05–5.09` Ops and final documentation |
| 6 | 8 | `6.01–6.04` closure decisions and PF09 revalidation · `6.05–6.08` maintenance, drainage preparation, ADR, follow-up |

A sub-split divides Pass 1 only. It does not create a new batch, a new ledger pair, or a new gate. Both halves write to the same batch Contract Ledger and Copy/Repair Ledger, and the batch still has exactly one Pass 2 and one verdict.

Repair all prompts in a batch against one frozen upstream state, as Section 6.4 of the approved plan requires, including across a sub-split.

## 5. Handoff artifacts between passes

Pass 1 → Pass 2 carries: the list of persisted prompt pages with their observed `page_last_edited_at` values; the batch branch and pull request; the exit state from Section 3 above; and any finding Pass 1 recorded but could not close. The ledgers are not handed over — Pass 1 commits them under `docs/ephemeral/` on the batch branch and Pass 2 reads them from there.

Pass 2 → Product Owner carries: the batch report and Notion sibling links, the verdict, per-prompt dispositions, controls changed, validation results, and unresolved blockers.

Pass 2 reports to the Product Owner directly in its own session and prepares the next handoff as a complete paste-ready invocation. There is no chat session to hand back to.

## 6. Model selection

Open question, recorded here rather than decided.

The review pass is largely structured matching of prompt content against a fixed checklist, which may tolerate a lighter model. The synchronization and validation pass is where a missed stale binding propagates into every subsequent batch, which argues for retaining the higher-capability model there even if Pass 1 is downgraded.

No cost data supports a specific recommendation at the time of writing. Any decision belongs to the Product Owner and should be recorded here when made.

## 7. Current execution state

- Batch 1: complete. Report `GCFPE-Batch-1-Repair-Report-v1.0-20260915.md`.
- Batch 2: Pass 1 complete and independently reconciled. All seven prompt repairs persisted to Notion on 2026-09-15 between 18:45:47Z and 18:45:58Z. All 22 contract findings verified as repaired against the current persisted bodies. No prompt was re-authored during recovery. Pass 2 not started.
- Batches 3 through 6: not started.
