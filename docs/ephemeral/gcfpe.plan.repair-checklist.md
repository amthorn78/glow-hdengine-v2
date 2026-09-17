# GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1

Durable Markdown copy of the Notion page [GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1](https://app.notion.com/p/3dc4590a05eb81a9adf1d8f800863937), exported 2026-09-16 from the page as last edited 2026-09-16T16:27:22.369Z. Notion page mentions are rendered as direct links.

```yaml
artifact_type: GCFPE_EXPANDED_PROMPT_REPAIR_PLAN_AND_CHECKLIST
artifact_version: "1.0"
created_date: 2026-09-15
status: APPROVED_BATCH_1_IN_PROGRESS
execution_authority: BATCH_1_ONLY_BY_PRODUCT_OWNER_HANDOFF_20260915
supersedes_for_next_iteration: GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md
selected_release: GCFPE-20260913.1
selected_prompt_version: "091326.2"
selected_member_count: 54
candidate_review_source: GCFPE-20260914.1
candidate_prompt_version: "091426.1"
candidate_member_count: 55
candidate_status: UNSELECTED_CANDIDATE
prompt_repair_batches: 6
in_scope_prompt_count: 55
skill_review_position: AFTER_BATCH_6
postflight_position: AFTER_SKILL_REVIEW_AND_ANY_APPROVED_SKILL_CORRECTION
alpha_stop_position: PR03_ACCEPTED_FINAL_BEFORE_PR04_PLANNING
pf10_drain_owner: Nathan / Product Owner
runtime_artifact_root: Glow / Ephemeral Planning Files
mutation_performed: false
```

## Execution approval record — 2026-09-15

Nathan's direct handoff titled `GCFPE Prompt Repair — Batch 1 Initialization` states: "Nathan has approved the six-batch repair plan. This handoff authorizes execution of Batch 1 only."

This is the approval evidence. The approved scope is unchanged. This session is authorized to repair the eleven Batch 1 candidate prompts and directly affected supporting controls, save/read back the Batch 1 report, and prepare only the applicable next-session or Product Owner blocker handoff. It must stop before Batch 2. Skill review and independent post-flight remain after Batch 6; promotion, selected-release mutation, PF10 drainage, repository/PR/CI work, PR04 planning, and Alpha resumption remain unauthorized. The original plan-creation no-mutation statements below describe publication-time history, not a continuing lack of this approval.

## 1. Plan decision

The repair scope is expanded from targeted correction of the defects listed in the prior plan to a complete contract-and-copy review of all 55 prompts in the current unselected candidate. The work already present in `GCFPE-20260914.1 / 091426.1` is retained as reusable candidate evidence, but no prompt is presumed correct merely because prior author checks passed.

The next repair iteration must:

1. inspect all 55 candidate prompt bodies and their selected predecessors;
2. review each prompt's complete contract before editing its copy;
3. repair required and optional inputs, outputs, states, handoffs, authority, and upstream/downstream dependencies;
4. repair clarity, precision, economy, and paste-readiness without deleting necessary governance;
5. process the prompts in exactly six dependency-aware batches;
6. keep the selected `GCFPE-20260913.1 / 091326.2 / 54` release untouched;
7. perform a dedicated workflow-skill suitability review only after all six prompt batches are complete; and
8. run a separate independent post-flight only after prompt repair and any separately approved skill correction are complete.

This document authorizes nothing. Prompt repair, control repair, skill repair, promotion, archival, PF10 drainage, PR04 planning, and Alpha resumption remain blocked until Nathan explicitly approves the plan and separately authorizes the applicable execution.

## 2. Sources reviewed for this update

- [Prior repair plan v2.0](https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk)
- [Selected 54-member catalog](https://app.notion.com/p/3da4590a05eb81bcbc5deb2d2cec4f1f)
- [Current 55-member candidate catalog](https://app.notion.com/p/3db4590a05eb81738ef1d846e3c0df8c)
- [Current candidate Flow Index](https://app.notion.com/p/3db4590a05eb81de9736ea69bac61016)
- [Recovery-grounded completion checklist](https://app.notion.com/p/3db4590a05eb8104b04cc01ed90ec39f)
- [Stable release register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1)
- [Current Alpha record](https://app.notion.com/p/3d64590a05eb81e1a645e0ca209b45c0)

### Current state established by those sources

- Production selection remains `GCFPE-20260913.1 / 091326.2 / 54`.
- `GCFPE-20260914.1 / 091426.1 / 55` is an unselected candidate and contains `PR-35` as its sole additional member.
- Previous author validation does not replace the prompt-by-prompt review required by this expanded plan.
- Alpha remains stopped after `HDE-EPIC040-PR03` reached `ACCEPTED_FINAL`; PR04 planning has not started.
- No previous post-flight result may be applied to a newly repaired snapshot.

## 3. Expanded scope

### In scope

- All 55 prompt bodies in the current unselected candidate.
- Selected-predecessor comparison for every existing logical ID; `PR-35` is reviewed as a new member without a selected predecessor.
- Contract review and copy review as separate, ordered activities for every prompt.
- Required inputs, optional inputs, conditional-input predicates, source authority, and native-stage availability.
- Outputs, result vocabularies, terminal/nonterminal status, artifact ownership, handoffs, and consumer readiness.
- Upstream/downstream dependencies and lane boundaries.
- Role, session, approval, Proceed, merge, abort, PF10, and manual-action boundaries.
- PF10 addendum production, Nathan's manual drainage, fresh current-PF10 Markdown resolution, and post-drain continuation.
- PR recovery, local-test-first publication, purposeful commits/pushes, review-before-CI action economy, and genuine merge readiness.
- Runtime artifact persistence as efficient machine-readable Markdown in `Glow / Ephemeral Planning Files`.
- Controlled PFCanon Markdown-only resolution.
- Candidate graph, catalog, Flow Index, metaprompt, operating procedure, family hubs, Alpha controls, and validation fixtures as supporting controls synchronized to the repaired prompts.
- A dedicated post-batch skill-fit review and a later independent post-flight.

### Out of scope for the six prompt batches

- Skill edits. Skills are assessed after Batch 6 and changed only through a separately approved skill-repair action.
- Selection or promotion of any candidate release.
- Moving, archiving, deleting, restoring, or overwriting any page or file.
- PF10 editing or drainage.
- Product repository changes, PR activity, CI, merge, deployment, or Ops execution.
- PR04 planning or Alpha resumption.
- Changes to the protected Flowmaster Primary core or immutable 46-row R1 baseline.

## 4. Mandatory contract rules for every batch

Every prompt review must enforce these rules where applicable.

### 4.1 Native-stage artifact availability

- An input is `REQUIRED` only when its producer has already completed the relevant native event on that branch and the receiving prompt cannot lawfully operate without it.
- An input is `OPTIONAL` only when its exact condition is stated and absence does not block ordinary entry.
- A future downstream artifact must never be required to start an upstream prompt.
- Existing valid artifacts are reused; prompts do not recreate them merely to satisfy a template.
- Ordinary PR work has no change-specific QA Guide or QA Plan prerequisite. An existing QA Guide, QA Plan, or QA evidence may be an optional, specifically relevant input for an approved post-QA remedy or escalation lineage. It must never become a blanket PR requirement.

### 4.2 PF10 and approved-base integrity

- Approved Plans, Guides, and Specifications remain immutable bases during implementation.
- A qualifying native approval emits exactly one standalone PF10 build-notes addendum.
- Nathan manually drains every qualifying addendum.
- Continuation must resolve and completely read the fresh current PF10 Markdown and verify the exact drained delta.
- Source-resolution failure, missing drain, and mismatched drain remain distinct states.
- Prompts must not allocate PF10 section numbers, edit PF10, claim an undrained addendum is canonical, or infer that Nathan failed to drain when the source could not be resolved.

### 4.3 PR-lane integrity and action economy

- PR-30 and PR-35 remain two phases of one work unit, one dedicated PR session, one workspace/worktree, one branch, one PR, and one original Proceed.
- Every fresh or uncertain entry searches for and recovers matching existing work before creating a new vehicle.
- Local testing precedes a meaningful commit and push.
- The workflow must avoid both extremes: no abandonment of complete tested work without a justified blocker, and no micro-commit/micro-push behavior.
- All known substantive review findings are resolved and locally tested before another push or another paid CI attempt.
- A CI run on a revision already known to require correction is stale and must not be awaited as a gate.
- No unauthorized `[skip ci]`, equivalent suppression, merge, auto-merge, or abort action is permitted.
- `PR-50 — Abort PR and Escalate` has no prompt-originated inbound edge and can be invoked only by Nathan.

### 4.4 Source, storage, and handoff integrity

- PFCanon sources are read only from controlled Markdown. Google Docs, `.doc`, and `.docx` PFCanon variants must not be opened, inspected, compared, cited, or used as fallback.
- ChatGPT Library and Library IDs are not used.
- Runtime ledgers, plans, reports, checkpoints, addenda, and handoffs are complete machine-readable Markdown stored in `Glow / Ephemeral Planning Files`, read back, and referenced by direct Drive link.
- Every nonterminal handoff is a complete paste-ready invocation that names the selected destination prompt, exact version, and direct Notion URL.
- Metadata lists, placeholders, “use the above,” bare filenames, and unsupported session-inspection claims are invalid handoffs.
- Model selection, model-strength assessment, Analyzer routing, reasoning recommendations, and configuration-driven routing remain excluded.

## 5. Per-prompt review-and-repair checklist

The executor must complete this sequence for every prompt in every batch. Review precedes repair.

- [ ] Pin the complete candidate body, exact Notion identity, parent, version, lifecycle, and selected predecessor where one exists.
- [ ] State the prompt's single native purpose and identify any behavior that belongs to a different lane.
- [ ] Inventory every input with producer, artifact identity, native availability point, authority, and `REQUIRED`/`OPTIONAL`/`CONDITIONAL` classification.
- [ ] Verify that each optional input has an exact predicate and does not silently become mandatory.
- [ ] Inventory every output with schema, owner, status vocabulary, storage location, and intended consumer.
- [ ] Enumerate every result branch and classify it as terminal or nonterminal.
- [ ] Verify each nonterminal branch has exactly one lawful, complete next-prompt handoff.
- [ ] Verify each terminal branch emits no misleading continuation.
- [ ] Map immediate upstream producers and downstream consumers and reconcile both sides of every interface.
- [ ] Verify role, session, approval, Proceed, merge, abort, and manual-action authority.
- [ ] Verify PF10, PFCanon, Drive, Notion, repository, and source-resolution behavior.
- [ ] Review copy for precision, plain meaning, consistent terminology, unnecessary repetition, contradictory instructions, false implications, placeholders, and unpasteable output.
- [ ] Record findings before editing; distinguish contract defects from copy defects.
- [ ] Repair only the defects supported by the review while preserving correct native behavior.
- [ ] Read back the complete repaired prompt and rerun producer/consumer reconciliation.
- [ ] Record `REPAIRED`, `CONFIRMED_NO_CHANGE`, or `BLOCKED_WITH_EVIDENCE`; no prompt may be silently skipped.

## 6. Batch execution protocol

1. Execute batches strictly in order from Batch 1 through Batch 6.
2. Do not edit a prompt before its complete review row is recorded.
3. Keep one batch-level contract ledger and one batch-level copy/repair ledger in Drive Markdown.
4. Repair all prompts in a batch against one frozen upstream state.
5. Update affected candidate controls and graph bindings as supporting synchronization inside that batch; these do not form a seventh prompt batch.
6. Read back every changed Notion page and Drive artifact.
7. Run batch-scoped structural, semantic, source-format, and handoff validation.
8. Do not begin the next batch while the current batch has an unresolved blocker or an unreconciled outgoing interface.
9. A later batch may expose a defect in an earlier batch. Return it to the owning batch ledger, repair it once, and revalidate all affected interfaces; do not start an untracked global rewrite.
10. After Batch 6, freeze one complete prompt/control snapshot for the dedicated skill review.

## 6A. Per-batch execution model — two-pass session structure

Added 2026-09-16. Execution mechanics only. This changes no authority, scope, batch count, batch membership, per-prompt checklist, completion criteria, or gate. Nathan's per-batch execution authorization is still required and is not granted by this section.

Complete specification: [GCFPE-Per-Batch-Execution-Model-v1.0-20260916.md](https://drive.google.com/file/d/1ha8I5QcTqAtcbDCifdtT8lJW0NhkFcmt/view?usp=drivesdk)

**Reason.** Batch 2 execution was interrupted by session token exhaustion, not by a defect in the work. Batch 2 is the smallest batch at 7 prompts; Batches 3 and 4 carry 10 each. Separately, Section 9 requires supporting-control reconciliation after every batch, and the candidate graph contract is 569,990 bytes, so that cost recurs in all six batches.

Each remaining batch executes in two dedicated sessions.

**Pass 1 — Review and repair (chat session).** Apply the Section 5 per-prompt checklist to every prompt in the batch. Persist each repaired body to Notion and read it back. Produce and read back the batch Contract Ledger and Copy/Repair Ledger in `Glow / Ephemeral Planning Files`. Pass 1 stops there: it does not synchronize supporting controls, run static/tabletop validation, write the batch report, or issue a verdict. Exit state is `BATCH_<N>_PROMPT_REPAIRS_PERSISTED` / `SUPPORTING_CONTROLS_AND_VALIDATION_INCOMPLETE` / `FINAL_BATCH_<N>_VERDICT_NOT_YET_ISSUED`.

**Pass 2 — Synchronization, validation, closure (Claude Code session).** Supporting-control synchronization per Section 9, static/tabletop validation against the current persisted prompts and synchronized controls, producer/consumer reconciliation, regression review, the batch report plus Notion sibling both read back, exactly one verdict, and the next handoff prepared only.

**Why the seam falls here.** Pass 1 is Notion-and-Drive work: many small targeted reads and writes against individual prompt pages, needing no filesystem or git access. Pass 2 is dominated by the 570KB graph contract, which must be scanned in targeted sections rather than loaded whole — a Code session can read a file that size from disk selectively; a chat session cannot.

**Sub-split thresholds.** Batches at 8 or more prompts should have Pass 1 split at the seams below, which follow this plan's own ordering and contract focus and introduce no new grouping. A sub-split divides Pass 1 only: it creates no new batch, ledger pair, or gate, both halves write to the same batch ledgers, and the batch still has exactly one Pass 2 and one verdict. Section 6.4's one-frozen-upstream-state rule holds across a sub-split.

| Batch | Prompts | Pass 1 sub-split seam |
|---|---|---|
| 1 | 11 | Complete. Not applicable. |
| 2 | 7 | Not split. Prompt repairs already persisted. |
| 3 | 10 | 3.01–3.04 PR planning and development lane · 3.05–3.10 rescope, drain continuation, post-merge lineage, manual abort |
| 4 | 10 | 4.01–4.06 QA readiness, Guide, Audit, Plan, review, revision · 4.07–4.10 task creation, execution, evidence review, reporting |
| 5 | 9 | 5.01–5.04 escalation · 5.05–5.09 Ops and final documentation |
| 6 | 8 | 6.01–6.04 closure decisions and PF09 revalidation · 6.05–6.08 maintenance, drainage preparation, ADR, follow-up |

**Model selection.** Open question, recorded rather than decided. The review pass is largely structured checklist matching and may tolerate a lighter model; the synchronization and validation pass is where a missed stale binding propagates into every subsequent batch, arguing for the higher-capability model there. No cost data supports a specific recommendation. The decision belongs to the Product Owner and should be recorded in the execution-model document when made.

**Reporting back from Pass 2.** When Pass 2 runs in Claude Code, it emits its return report as a single fenced `text` block for the Product Owner to paste into a chat session. Claude Code cannot message a chat session directly; cross-session messaging reaches other Claude Code sessions only.

## 7. Exactly six repair batches

### Batch 1 — Governance, classification, and Specification formation

**Size:** 11 prompts  
**Execution position:** 1 of 6  
**Reason:** These prompts define the reusable management contract, change classification, CRD/Epic Specification formation, approval, revision, and the earliest PF10-producing decisions. Every later lane depends on their artifact and authority semantics.

| Order | Prompt | Contract focus |
|---|---|---|
| 1.01 | [Notion page](https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54) | Reusable repair-management scope, six-batch control, final handoff boundary, no runtime execution. |
| 1.02 | [Notion page](https://app.notion.com/p/3db4590a05eb8108ad2dd4d0e20bd6c4) | Coordination without absorbing native decisions or creating authority. |
| 1.03 | [Notion page](https://app.notion.com/p/3db4590a05eb8161b4d7cb6d07f5101c) | Nathan's classification record and exact CRD/Epic branch handoff. |
| 1.04 | [Notion page](https://app.notion.com/p/3db4590a05eb8119a5a8e4d083fcf360) | Complete CRD kickoff intake and direct CF-C-20 handoff. |
| 1.05 | [Notion page](https://app.notion.com/p/3db4590a05eb8173a73edc73f302a90a) | Initial versus in-flight Specification context; PF10 overlays; author output. |
| 1.06 | [Notion page](https://app.notion.com/p/3db4590a05eb8149a8d2ed42c9c01ffd) | Decision branches; qualifying addendum production only for material approved-base delta. |
| 1.07 | [Notion page](https://app.notion.com/p/3db4590a05eb81269931cee342ce8a0e) | Bounded revision, immutable-base rule, return to same review lineage. |
| 1.08 | [Notion page](https://app.notion.com/p/3db4590a05eb815b84a5c5a5ace85fe1) | Complete Epic kickoff intake and direct CF-E-20 handoff. |
| 1.09 | [Notion page](https://app.notion.com/p/3db4590a05eb810eb177f7dced41bc8f) | Initial versus in-flight Specification context; PF10 overlays; author output. |
| 1.10 | [Notion page](https://app.notion.com/p/3db4590a05eb81b4be79f405566da9a7) | Decision branches; qualifying addendum production only for material approved-base delta. |
| 1.11 | [Notion page](https://app.notion.com/p/3db4590a05eb8101b655ed223b11a85e) | Bounded revision, immutable-base rule, return to same review lineage. |

**Batch 1 completion criteria**

- [ ] All 11 prompts have complete review rows and final dispositions.
- [ ] CRD and Epic branches are parallel where intended and explicitly different where required.
- [ ] Initial approvals are not misclassified as PF10 addendum events.
- [ ] Material in-flight approved-base changes produce exactly one standalone addendum.
- [ ] Specification outputs provide complete lawful intake to Batch 2.
- [ ] Manager/coordinator prompts do not absorb Product Owner, Isis, Thoth, IA, PR, QA, or closure authority.

### Batch 2 — Whole-change Implementation Audit, Plan, research, and exact revision

**Size:** 7 prompts  
**Execution position:** 2 of 6  
**Reason:** These prompts transform the approved Specification into the authoritative whole-change Audit and Plan. They must be correct before PR, Ops, QA, documentation, rescope, or escalation prompts can be validated against their real approved base.

| Order | Prompt | Contract focus |
|---|---|---|
| 2.01 | [Notion page](https://app.notion.com/p/3db4590a05eb817aa191f1e822c30480) | Whole-change audit intake, artifact separation, research needs, IA continuity. |
| 2.02 | [Notion page](https://app.notion.com/p/3db4590a05eb81d78eeae384e93dd697) | Bounded answers only; no unsupported authority or silent planning decision. |
| 2.03 | [Notion page](https://app.notion.com/p/3db4590a05eb8141b5b2c8fbf7b725e2) | Bounded research question, source evidence, return to the same IA. |
| 2.04 | [Notion page](https://app.notion.com/p/3db4590a05eb81c4825df2ad0dec4750) | Plan authoring from completed audit/research; PF10 cross-reference; complete review handoff. |
| 2.05 | [Notion page](https://app.notion.com/p/3db4590a05eb81c6bfb5f36f7df8f464) | Approval/denial/revision branches; qualifying addendum rule; no live Plan rewrite. |
| 2.06 | [Notion page](https://app.notion.com/p/3db4590a05eb8197bb1bc8f52f896969) | Initial completion versus bounded preapproval revision; no in-flight restart. |
| 2.07 | [Notion page](https://app.notion.com/p/3db4590a05eb81b89fbaf4b31a3ed2a9) | Exact authorized redline application without scope expansion or authorship transfer. |

**Batch 2 completion criteria**

- [ ] All 7 prompts have complete review rows and final dispositions.
- [ ] Audit, Plan, research, seeding, review, and revision artifacts remain distinct.
- [ ] Every Plan creator/reviser resolves current PF10 Markdown and lists applicable overlays.
- [ ] An approved Plan is never re-authored in flight; material changes use PF10 addenda.
- [ ] IA-30 emits an addendum only for a qualifying material delta to an already approved base.
- [ ] Batch 2 produces complete, unambiguous approved-base inputs for PR, Ops, QA, and documentation lanes.

### Batch 3 — PR development, rescope, recovery, merge readiness, and manual abort boundary

**Size:** 10 prompts  
**Execution position:** 3 of 6  
**Reason:** This is the highest-risk Alpha defect cluster. PR planning, implementation, review correction, rescope, post-drain continuation, post-merge lineage review, and Product Owner-only abort must be reconciled as one closed contract before downstream QA and closure are reviewed.

| Order | Prompt | Contract focus |
|---|---|---|
| 3.01 | [Notion page](https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d) | Work-unit boundary, current PF10 overlays, complete PR-20 intake. |
| 3.02 | [Notion page](https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be) | Required versus optional inputs, no blanket QA prerequisites, paste-ready PR-30 invocation. |
| 3.03 | [Notion page](https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294) | Recovery first, same vehicle, bounded implementation, local testing, coherent publication checkpoint. |
| 3.04 | [Notion page](https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c) | Same-session continuation, review-first correction, action-efficient pushes, current-head CI and merge readiness. |
| 3.05 | [Notion page](https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4) | Evidence threshold, smallest bounded delta, exact origin and return phase. |
| 3.06 | [Notion page](https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497) | IA decision matrix, one qualifying addendum, pre-drain package, no Plan restart. |
| 3.07 | [Notion page](https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf) | Bounded revision preserving request identity and return to same IA decision. |
| 3.08 | [Notion page](https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226) | Fresh PF10 verification, four-state result schema, exact same-vehicle PR phase continuation. |
| 3.09 | [Notion page](https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634) | Manual-merge assertion versus verified merged state; read-only landed attribution. |
| 3.10 | [Notion page](https://app.notion.com/p/3db4590a05eb8138ac99c13cf6f2f282) | Nathan-only direct invocation, zero inbound edges, evidence preservation, terminal escalation. |

**Batch 3 completion criteria**

- [ ] All 10 prompts have complete review rows and final dispositions.
- [ ] PR-30 and PR-35 share one work unit, session, vehicle, PR, and original Proceed without a second approval gate.
- [ ] Existing workspace/worktree/branch/PR/artifacts are searched before anything new is created.
- [ ] PR-20 does not require QA Guide/Plan evidence for ordinary PR work; later relevant QA evidence is conditional and optional.
- [ ] Local tests precede coherent commits/pushes; known reviews precede another paid CI attempt.
- [ ] PR-30 always emits a complete named/versioned PR-35 handoff after lawful publication.
- [ ] Rescope returns to the exact originating phase and never rewrites or restarts the whole Plan.
- [ ] `SOURCE_RESOLUTION_ERROR`, `MANUAL_DRAIN_REQUIRED`, `MANUAL_DRAIN_MISMATCH`, and `DRAIN_VERIFIED` are exhaustive and noncontradictory.
- [ ] PR-40 does not treat historical `MERGE_PENDING` as proof of merge.
- [ ] PR-50 has no prompt-, skill-, manager-, or automation-originated inbound route.

### Batch 4 — QA readiness, Guide, Plan, execution, evidence review, and final reporting

**Size:** 10 prompts  
**Execution position:** 4 of 6  
**Reason:** The QA lane depends on accepted implementation evidence from Batch 3 and produces the evidence consumed by escalation and closure. It must be reviewed as its own downstream system so QA artifacts do not leak backward into ordinary PR prerequisites.

| Order | Prompt | Contract focus |
|---|---|---|
| 4.01 | [Notion page](https://app.notion.com/p/3db4590a05eb818bad2fcb4bc2610b29) | Accepted implementation intake and QA-readiness decision. |
| 4.02 | [Notion page](https://app.notion.com/p/3db4590a05eb816daa3adff37283482b) | Guide creation after QA readiness; author completion without invented approval gate. |
| 4.03 | [Notion page](https://app.notion.com/p/3db4590a05eb81a3ac91f602bad8cfa2) | QA Audit and QA Plan separation; existing Guide as native prerequisite here only. |
| 4.04 | [Notion page](https://app.notion.com/p/3db4590a05eb810b8aa3e1692830d4b8) | Complete QA Plan from valid QA Audit, PF10 overlays, and exact execution mapping. |
| 4.05 | [Notion page](https://app.notion.com/p/3db4590a05eb8143bf26d1459fbbcad7) | Native QA Plan decision and qualifying PF10-addendum rule. |
| 4.06 | [Notion page](https://app.notion.com/p/3db4590a05eb813ba9a9dbd9a641d36c) | Bounded preapproval revision and return to the same reviewer. |
| 4.07 | [Notion page](https://app.notion.com/p/3db4590a05eb811e8582cf30238c5b9c) | Atomic task creation, exact evidence contract, escalation branch to ESC-10. |
| 4.08 | [Notion page](https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848) | Bounded execution, truthful receipt, no acceptance or routing overreach. |
| 4.09 | [Notion page](https://app.notion.com/p/3db4590a05eb816984d1d34da0e08f40) | Evidence validity, correction/retry/escalation routing, no false finality. |
| 4.10 | [Notion page](https://app.notion.com/p/3db4590a05eb81589d21e798cf38e8ba) | Separate Report/RCA, EPIC/CRD closure routing, complete class-specific intake. |

**Batch 4 completion criteria**

- [ ] All 10 prompts have complete review rows and final dispositions.
- [ ] QA Guide and QA Plan exist only at their native downstream stages.
- [ ] QA Audit, QA Plan, Guide, execution task, receipt, evidence review, Report, and RCA remain distinct artifacts.
- [ ] QA-70 alone produces a qualifying QA Plan addendum when its native predicate is met.
- [ ] QA-90 escalation routes to ESC-10 with complete evidence.
- [ ] QA-120 routes verified EPIC PASS to CL-E-10 and verified CRD PASS to CL-C-10; ambiguous class returns terminally to Nathan.
- [ ] No QA prompt grants merge, closure, PF10 drainage, Product Owner, or PR-development authority.

### Batch 5 — Escalation, bounded Ops, and final repository documentation

**Size:** 9 prompts  
**Execution position:** 5 of 6  
**Reason:** Escalation consumes QA findings; Ops and documentation consume approved whole-change or remediation boundaries. Reviewing these after PR and QA prevents them from inventing upstream inputs, stealing PR authority, or confusing post-QA evidence with ordinary development prerequisites.

| Order | Prompt | Contract focus |
|---|---|---|
| 5.01 | [Notion page](https://app.notion.com/p/3db4590a05eb81d582b8d490e77f9f40) | Complete QA escalation intake, evidence lineage, and bounded discovery handoff. |
| 5.02 | [Notion page](https://app.notion.com/p/3db4590a05eb81bf9326e46a1017de38) | Read-only/bounded discovery, truthful evidence return, no remediation authority. |
| 5.03 | [Notion page](https://app.notion.com/p/3db4590a05eb813e99b4e416bc7afdae) | Diagnosis versus proposal, smallest remediation, native return owner. |
| 5.04 | [Notion page](https://app.notion.com/p/3db4590a05eb81efb6d4cd8d02ba9756) | Approval branches, one qualifying addendum, actual delivery owner, no RS impersonation. |
| 5.05 | [Notion page](https://app.notion.com/p/3db4590a05eb81db98cce3e30a62bce5) | Exact Ops scope, authority, environment, evidence, and execution handoff. |
| 5.06 | [Notion page](https://app.notion.com/p/3db4590a05eb81858a9dd361d3689ce8) | Bounded environment action and receipt; no PR/PF/approval authority. |
| 5.07 | [Notion page](https://app.notion.com/p/3db4590a05eb816f91c9c394f9c9fa57) | Acceptance/rejection from evidence and return to native IA/remediation owner. |
| 5.08 | [Notion page](https://app.notion.com/p/3db4590a05eb8193a9a8d7ddd751cd2d) | Final documentation scope after implementation; PR instruction without live PR execution. |
| 5.09 | [Notion page](https://app.notion.com/p/3db4590a05eb8164ac09e722dc967f25) | Completion evidence, accepted lineage, and downstream closure readiness. |

**Batch 5 completion criteria**

- [ ] All 9 prompts have complete review rows and final dispositions.
- [ ] Escalation preserves QA evidence and returns approved remediation to its actual native owner.
- [ ] ESC-40 produces one PF10 addendum only for a qualifying approved material delta.
- [ ] Ops access does not grant PR workflow, merge, PF-document, drainage, or Product Owner authority.
- [ ] Documentation prompts consume completed implementation lineage and do not create a premature QA or closure dependency.
- [ ] Every return path resolves to an existing prompt and carries only artifacts that actually exist at that stage.

### Batch 6 — Retrospective, closure, drainage preparation, ADR, and PF09 follow-up

**Size:** 8 prompts  
**Execution position:** 6 of 6  
**Reason:** Closure is the terminal consumer of Specification, implementation, QA, escalation, Ops, and documentation evidence. It must be reviewed last so its acceptance, drainage-preparation, ADR, and PF09 decisions are grounded in the repaired upstream contracts.

| Order | Prompt | Contract focus |
|---|---|---|
| 6.01 | [Notion page](https://app.notion.com/p/3db4590a05eb81ad8989faa77f441a64) | CRD-specific closure decision and complete accepted evidence. |
| 6.02 | [Notion page](https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac) | Epic-specific closure decision and PF09-revalidation branch. |
| 6.03 | [Notion page](https://app.notion.com/p/3db4590a05eb81c2b5d5ff46126f9e45) | Bounded PF09 evidence without reopening accepted work. |
| 6.04 | [Notion page](https://app.notion.com/p/3db4590a05eb81b4a649fdcdb1903345) | Revalidation decision, unresolved-gap return, maintenance handoff. |
| 6.05 | [Notion page](https://app.notion.com/p/3db4590a05eb81e78e82f83a5f2e4b68) | Bounded maintenance proposal/instruction without direct PF edit authority. |
| 6.06 | [Notion page](https://app.notion.com/p/3db4590a05eb81f4812be61e8877c02c) | Drainage preparation versus Nathan's actual manual PF10 drain; closure memo lineage. |
| 6.07 | [Notion page](https://app.notion.com/p/3db4590a05eb8190a444d8818e445c1d) | Conditional ADR need, exact owner, no direct edit without authority. |
| 6.08 | [Notion page](https://app.notion.com/p/3db4590a05eb81db9c88cde6027e07bf) | Gap identification and candidate preparation without auto-starting a new change. |

**Batch 6 completion criteria**

- [ ] All 8 prompts have complete review rows and final dispositions.
- [ ] CRD and Epic closure routes consume the correct class-specific QA Report/RCA and accepted evidence.
- [ ] Closure decisions do not merge, drain PF10, edit PF documents, or reopen accepted-final PRs.
- [ ] CL-20 prepares, but does not perform or misrepresent, Nathan's manual drainage.
- [ ] PF09/ADR follow-up remains conditional, bounded, and routed to its actual owner.
- [ ] No closure output automatically starts a new CRD, Epic, PR, abort, or Alpha action.

## 8. Batch count and coverage proof

| Batch | Prompt count | Cumulative count |
|---|---|---|
| 1 — Governance, classification, Specification | 11 | 11 |
| 2 — Implementation Audit/Plan and support | 7 | 18 |
| 3 — PR and rescope | 10 | 28 |
| 4 — QA | 10 | 38 |
| 5 — Escalation, Ops, documentation | 9 | 47 |
| 6 — Closure and follow-up | 8 | 55 |

Coverage requirement:

- [ ] Exactly 55 unique prompt IDs are assigned.
- [ ] Every candidate prompt appears in exactly one batch.
- [ ] No selected or candidate prompt is omitted.
- [ ] No control document, skill, report, or fixture is miscounted as a prompt batch member.

## 9. Supporting-control synchronization

Supporting controls are updated only to reflect completed prompt repairs. They are not additional prompt batches.

After each batch, reconcile the affected portions of:

- candidate graph contract and direct-handoff fixtures;
- PE Metaprompt;
- GCFPE Direct-Handoff and Runtime Artifact Operating Procedure;
- candidate catalog and release-entry draft;
- candidate Flow Index;
- relevant Change Flow, IA, QA, Escalation, TW, Ops, and closure hubs;
- Alpha establishment/change-management checklist; and
- candidate Alpha run record.

Control synchronization must never select the candidate, change the stable release register, move older pages, drain PF10, or resume Alpha.

## 10. Dedicated workflow-skill review after Batch 6

After all six prompt batches pass and one complete prompt/control snapshot is frozen, create and run one separate dedicated **GCFPE Workflow Skill-Fit Review** prompt. It is not part of any repair batch and must not be performed by the prompt author as a casual appendix.

### Skill-review scope

Review the complete installed sources, references, validators, and actual assigned prompt roles for:

- `change-flow`;
- `glow-hde-pr-development`;
- `glow-hde-devops`;
- `flowmaster-validate`;
- `amthor-workspace-governance-audit`;
- `glow-merged-change-attribution-lock`;
- `flowmaster-primary` and the immutable R1 oracle as protected upstream controls;
- `flowmaster-propagate` only if an approved Primary-core change exists; and
- `skill-creator` as the governed editing mechanism, not a runtime workflow owner.

### Required skill-review questions

- [ ] Does every prompt that needs a primary skill have exactly one appropriate primary skill?
- [ ] Are support skills prevented from assuming workflow authority?
- [ ] Does `glow-hde-pr-development` fully and narrowly own PR-30, PR-35, interrupted PR recovery, and eligible RS-40 continuation?
- [ ] Is `glow-hde-devops` support-only for specific environment, Railway, vendor, database, deployment, or bounded Ops capabilities, with no PR-lane authority?
- [ ] Is `glow-merged-change-attribution-lock` limited to optional read-only landed-attribution support for PR-40?
- [ ] Does `change-flow` orchestrate the selected workflow without performing repository implementation?
- [ ] Do `flowmaster-validate` and `amthor-workspace-governance-audit` validate rather than author, approve, promote, or execute runtime work?
- [ ] Do any prompt contracts require a capability that no installed skill safely supplies?
- [ ] Do any installed skills overlap, contradict, overreach, or carry obsolete prompt/version bindings?
- [ ] Is a new specialized skill actually required, or can the existing specialized PR-development skill be corrected without duplicating authority?

### Skill-review output and gate

The dedicated review must produce a complete prompt-to-skill matrix with `PRIMARY`, `SUPPORT`, `VALIDATOR`, `EDITING_TOOL`, `PROHIBITED`, or `NONE` for every applicable relationship, plus exactly one verdict:

- `SKILL_FIT_CONFIRMED`
- `SKILL_REPAIR_REQUIRED`
- `SKILL_GAP_REQUIRES_PRODUCT_OWNER_DECISION`
- `SKILL_REVIEW_INDETERMINATE`

The review itself performs no skill edits. If it returns anything other than `SKILL_FIT_CONFIRMED`, stop before post-flight. Present the exact findings and proposed bounded skill change to Nathan for separate approval. Any approved skill edit must use `skill-creator`, preserve unrelated behavior, be committed and read back, and then rerun the dedicated skill review against the final installed snapshot.

## 11. Separate independent post-flight

Only after:

1. all six prompt batches are complete;
2. all supporting controls are synchronized and read back;
3. the dedicated skill review returns `SKILL_FIT_CONFIRMED`; and
4. any separately approved skill repairs are complete and re-reviewed,

run a fresh, distinct independent post-flight using `amthor-workspace-governance-audit` in `BATCH_POSTFLIGHT` mode, with `flowmaster-validate` for deterministic suite validation.

The post-flight auditor must not be the author or skill reviewer and must not repair findings. It must validate:

- all 55 complete prompt bodies;
- all six batch ledgers and final dispositions;
- producer/consumer and required/optional input agreement;
- all terminal and nonterminal branches;
- graph closure and exact handoff identities;
- PF10 producer count and manual-drain handshake;
- PR/QA boundary, including the absence of blanket QA prerequisites in ordinary PR work;
- PR recovery, PR-30/PR-35 continuity, review-before-CI rules, and Nathan-only abort/merge controls;
- Markdown-only PFCanon and Drive artifact routing;
- prompt-to-skill agreement against the final skill-review matrix;
- protected Primary/R1 identity;
- selected-release nonmutation; and
- Alpha remaining stopped at PR03 accepted-final before PR04 planning.

Required verdict: `PASS`, `PASS WITH WARNINGS`, `FAIL`, or `INDETERMINATE`.

- `PASS` or `PASS WITH WARNINGS` with no mandatory open finding permits preparation of a separate Product Owner promotion decision packet.
- `FAIL` or `INDETERMINATE` returns findings to the owning batch or skill gate. It does not authorize wholesale re-authoring, promotion, archival, PF10 drainage, or Alpha resumption.

## 12. Final completion criteria for this repair iteration

- [ ] Nathan approved this exact plan before repair began.
- [ ] Six and only six prompt repair batches were executed in order.
- [ ] All 55 prompts were reviewed once as primary batch members with no omission or duplication.
- [ ] Every prompt has a contract review, copy review, repair/no-change disposition, and complete readback.
- [ ] Required and optional inputs are native-stage correct and producer-backed.
- [ ] Every output and result state has an owner and lawful consumer.
- [ ] Every nonterminal handoff is complete, selected-name/version/link specific, and paste ready.
- [ ] Ordinary PR work does not require QA Guide or QA Plan artifacts; specifically relevant later QA evidence is conditional only.
- [ ] PF10 addenda, manual drain, fresh verification, immutable bases, and rescope continuation are consistent across all producers/readers.
- [ ] PR recovery, local-first testing, purposeful commit/push behavior, review-first CI economy, and current-head merge readiness are consistent.
- [ ] PR-50 and merge remain Nathan-only manual actions.
- [ ] All supporting controls and fixtures match the repaired prompts.
- [ ] Dedicated skill review confirms every skill assignment or all separately approved repairs are complete and re-reviewed.
- [ ] Independent post-flight passes with no mandatory open finding.
- [ ] The selected `GCFPE-20260913.1 / 091326.2 / 54` release remained untouched during candidate repair.
- [ ] PF10 remained untouched and undrained by agents.
- [ ] Alpha remained stopped after PR03 accepted-final; PR04 planning was not started.

## 13. Current checklist state

### Planning

- [x] Current selected release identified.
- [x] Current unselected 55-member candidate identified.
- [x] Prior v2.0 plan reviewed.
- [x] Expanded scope defined as all 55 prompt contracts and bodies.
- [x] Exactly six batches assigned with complete 55-prompt coverage.
- [x] Dedicated post-batch skill-review gate defined.
- [x] Separate independent post-flight gate defined.
- [x] Product Owner approval of this exact plan.

### Execution

- [x] Batch 1 complete. See [GCFPE Batch 1 Repair Report v1.0 — 20260915](https://drive.google.com/file/d/1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-/view?usp=drivesdk).
- [ ] Batch 2 complete. **Pass 1 complete and independently reconciled 2026-09-16.** All seven prompt repairs were persisted to Notion on 2026-09-15 between 18:45:47Z and 18:45:58Z. All 22 contract findings in the Batch 2 Contract Ledger verify as repaired against the current persisted bodies; no prompt was re-authored during recovery. Pass 2 — supporting-control synchronization, static/tabletop validation, final report, and verdict — is not started. State: `BATCH_2_PROMPT_REPAIRS_PERSISTED_AND_CONTRACT_RECONCILED` / `SUPPORTING_CONTROLS_AND_VALIDATION_INCOMPLETE` / `FINAL_BATCH_2_VERDICT_NOT_YET_ISSUED`.
- [ ] Batch 3 complete.
- [ ] Batch 4 complete.
- [ ] Batch 5 complete.
- [ ] Batch 6 complete.
- [ ] Final prompt/control snapshot frozen.
- [ ] Dedicated workflow-skill review complete with `SKILL_FIT_CONFIRMED`.
- [ ] Separate independent post-flight complete with acceptable verdict.
- [ ] Product Owner promotion decision packet prepared.

## Batch 1 completion record — 2026-09-15

BATCH_1_COMPLETE. The approved plan scope is unchanged. The final Batch 1 report is [GCFPE-Batch-1-Repair-Report-v1.0-20260915.md](https://drive.google.com/file/d/1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-/view?usp=drivesdk). Batch 2 has not been started by this session. The following Current stop section remains the publication-time record described by the execution approval record.

## 14. Current stop

`AWAITING_PRODUCT_OWNER_APPROVAL`

No prompt repair, control repair, skill edit, selection, promotion, archival, PF10 drainage, repository action, PR/CI action, PR04 planning, or Alpha resumption was performed while creating this plan.

## Child page

- [GCFPE Batch 2 Repair Report v1.0 — 20260916](https://app.notion.com/p/3dd4590a05eb818aa99ec695f664d82f)
