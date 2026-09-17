# GCFPE Batch 1 Targeted Correction Pre-Edit Closure Ledger v1.0 — 20260915

~~~yaml
artifact_type: GCFPE_BATCH_1_TARGETED_CORRECTION_PRE_EDIT_CLOSURE_LEDGER
artifact_version: "1.0"
date: 2026-09-15
scope: "Defects A, B, and C only"
authority: "Nathan / Product Owner targeted correction and evidence-based self-reassessment handoff"
review_type: "author correction preparation; not independent verification"
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
edit_started: false
~~~

## Source snapshot

- Approved plan: https://app.notion.com/p/3dc4590a05eb81a9adf1d8f800863937?pvs=204
- Batch 1 report: https://drive.google.com/file/d/1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-/view?usp=drivesdk
- Contract ledger: https://drive.google.com/file/d/1Ej9MIKgejK69j-BorauRM14AE7mQffVX/view?usp=drivesdk
- Copy/repair ledger: https://drive.google.com/file/d/1bzRCUEBgmw0j-TAer_72xAATZBTH1q9r/view?usp=drivesdk
- Candidate graph: https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk

All eleven mutable Batch 1 candidate pages and their selected predecessors were refreshed before this record.

## Defect A — Classification entry and receiver compatibility

**Original finding:** B1-PO-C1.

**Current conflicting clauses:**

- MGR-10 091426.1 routes FLOW_PROGRESS with no Product Owner class selection directly to CF-PO-10.
- CF-PO-10 091426.1 requires CHANGE_CLASS and explicit Product Owner selection evidence at entry, while its output is CLASS_SELECTED.
- CF-C-10 and CF-E-10 091426.1 route missing/conflicting selection recovery to CF-PO-10 but their generic handoff language says a missing Product Owner decision is terminal with no handoff.

**Supporting authority:**

- B1-PO-C1 in the existing contract ledger: distinguish entry prerequisites from CLASS_SELECTED output predicates.
- Selected CF-C-10 and CF-E-10 accept a CF-PO-10 selection artifact or a complete equivalent explicit Product Owner decision.
- Nathan remains the sole class decision-maker.

**Required behavior:**

CF-PO-10 must accept an unresolved classification case containing change identity, source, and any available evidence without a fabricated class or selection. It must request the exact CRD-or-Epic decision from Nathan and terminate if unavailable. A separately evidenced choice whose record is missing must be recorded/recovered without asking Nathan to choose again. CLASS_SELECTED and a kickoff handoff are emitted only after explicit decision evidence exists.

**Intended targeted correction:**

Separate CF-PO-10 entry modes; make MGR-10 and CF-C-10/CF-E-10 handoffs state whether the decision is absent or evidenced-but-unrecorded; align their terminal exception with the CF-PO-10 recording/request receiver; update only matching graph branch conditions.

**Pre-correction test:**

Unclassified source plus CHANGE_ID routed MGR-10 to CF-PO-10 fails because CF-PO-10 requires the missing CHANGE_CLASS and selection evidence. A known decision with no record is not separately represented.

## Defect B — Approved-Specification factual-correction path

**Original findings:** B1-C20-C1, B1-E20-C1, B1-C30-C1, B1-E30-C1, B1-C40-C2, B1-E40-C2.

**Current conflicting clauses:**

- CF-C-20 and CF-E-20 091426.1 add APPROVED_BASE_DELTA_AUTHORING despite their selected predecessors naming the kickoff as their sole substantive input.
- CF-C-30 and CF-E-30 091426.1 accept only a pending SPECIFICATION_DELTA plus an actual Product Owner product-intent/change decision for approved-base review.
- CF-C-40 and CF-E-40 091426.1 require an already pending delta and applicable Product Owner decision, so no actor can author the first delta from a concrete factual finding.
- The earlier contract ledger instead names CF-C-30/CF-E-30 assessment and CF-C-40/CF-E-40 delta authoring.

**Supporting authority:**

- Selected CF-C-30 and CF-E-30 state that a correction review may receive an approved Specification plus a concrete factual finding or actual authorized product/scope decision; Thoth assesses it, supplies bounded correction redlines to the same Isis revision prompt, does not relabel historical approval as denial, leaves an unsupported concern unchanged, and returns a genuine product choice to Nathan.
- Selected CF-C-20 and CF-E-20 define the complete kickoff as the sole substantive call input.
- The existing contract ledger states that the delta author is CF-C-40 or CF-E-40 and that a factual-finding intake needs an assessment-to-author branch.

**Required behavior:**

A concrete factual finding may reach Thoth without a pre-authored delta or a new product decision. A justified correction returns exact bounded correction redlines to the same Isis author, who authors the first standalone pending delta while preserving the immutable approved base. A genuine product/scope choice requires Nathan only when such a choice is actually unresolved. The subsequent pending-delta review/revision loop remains separate. No assessment of an unwritten delta approves anything or produces an addendum.

**Intended targeted correction:**

Restore sole kickoff authoring to CF-C-20/CF-E-20; add approved-base correction assessment and correction-redline routing to CF-C-30/CF-E-30; add first-delta authoring mode to CF-C-40/CF-E-40; make Product Owner decision conditional in factual-correction modes; synchronize the graph’s C/E-20 outputs, C/E-30 result states/branches, and C/E-40 first-delta branch.

**Pre-correction test:**

Approved Specification plus a concrete factual finding and no pending delta fails: -20 has an unauthorized/competing delta mode, -30 requires the missing delta and decision, and -40 requires the missing delta/redline.

## Defect C — Fixed Batch 1 state in reusable management

**Current conflicting clauses:**

GCFPE-MGMT-10 091426.1 requires only BATCH_1_COMPLETE or BATCH_1_BLOCKED and states that reusable branches are not invoked in the current Batch 1 case.

**Supporting authority:**

- The approved plan authorizes six distinct batches.
- The candidate graph records reusable management states as ECOSYSTEM_CHANGE_COMPLETE, IMPLEMENTATION_BLOCKED, PROMOTION_CHECKPOINT_REQUIRED, and READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION; it contains no fixed Batch 1 completion state.
- The selected manager is a reusable managing prompt for one requested GCFPE change.

**Required behavior:**

The manager derives active repair-batch identity, scope, and completion result from the exact Product Owner authorization and governing plan. Batch completion is case-scoped and never equates to whole-ecosystem acceptance, selection, promotion, automatic later-batch execution, or Alpha resumption.

**Intended targeted correction:**

Replace fixed Batch 1 required-result and current-case language with authorization-derived repair-batch behavior while retaining generic graph result vocabulary. No graph state change is justified unless a persisted graph clause itself contains fixed Batch 1 behavior.

**Pre-correction test:**

A hypothetical authorized Batch 2 repair invocation would still require a Batch 1 result, while ordinary maintenance would be governed by batch-specific instructions.

## Edit guard

Use only targeted page/control updates recorded above. Do not begin Batch 2, modify a selected predecessor, touch PF10, or change the protected release. After every substantive edit, re-read the persisted source and rerun the affected tabletop cases.

