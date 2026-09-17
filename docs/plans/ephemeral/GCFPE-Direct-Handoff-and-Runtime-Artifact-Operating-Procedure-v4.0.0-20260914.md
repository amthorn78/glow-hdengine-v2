---
artifact_type: GCFPE_DIRECT_HANDOFF_AND_RUNTIME_ARTIFACT_OPERATING_PROCEDURE
artifact_version: "4.0.0"
title: "GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v4.0.0 — 20260914"
candidate_release: GCFPE-20260914.1
prompt_version_family: "091426.1"
candidate_member_count: 55
status: UNSELECTED_CANDIDATE_DRAFT
activation_authority: Nathan / Product Owner after separate explicit approval of the exact validated snapshot
predecessor_release: GCFPE-20260913.1
predecessor_version_family: "091326.2"
mutation_posture: LIVE_UNSELECTED_CANDIDATE
recovery_correction_run: GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1
promotion_authorized: false
validation_status: REVALIDATION_REQUIRED_AFTER_SOURCE_IDENTITY_CORRECTION
---

# GCFPE Direct-Handoff and Runtime Artifact Operating Procedure

## 1. Purpose and authority

This procedure governs manual movement among the 55 selected prompt identities after—and only after—the complete `GCFPE-20260914.1` promotion transaction succeeds. It standardizes source resolution, Drive persistence/readback, immutable-base overlays, complete direct handoffs, recovery, and manual Product Owner boundaries. It does not activate automation, execute Alpha, edit PF10, merge a PR, or expand repository authority.

Before promotion, this file is an unselected successor draft and `https://app.notion.com/p/3da4590a05eb81bcbc5deb2d2cec4f1f?pvs=204` remains selected through the release register.

## Controlled-source and artifact rules

- Resolve selection only from the [GCFPE Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204); do not infer it from dates, suffixes, search ordering, or an unselected candidate.
- A PFCanon source is usable only as the unique controlled Markdown direct child resolved through `Glow / Core Docs / PFCanon`. Never open, fetch, inspect, compare, cite as authority, or use any native-document PFCanon candidate, including as an equivalence check or fallback. If the unique controlled Markdown authority cannot be resolved and completely read, return `SOURCE_RESOLUTION_ERROR`; that source failure does not prove any human action was omitted.
- Runtime ledgers, manifests, matrices, reports, addenda, checkpoints, and handoffs are complete machine-readable Markdown stored in [Glow / Ephemeral Planning Files](https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc), fetched back completely, verified, and carried by direct Drive link.
- Preserve existing approved bases and completed artifacts at their actual native status. This protection creates no input requirement, future artifact, or separate Guide approval. Current PF10 Markdown and every applicable active overlay are resolved afresh; pre-drain PF10 evidence is labeled `PRE_DRAIN_BASELINE_EVIDENCE`.


## Direct native continuation

Every nonterminal substantive continuation goes directly from the producing selected native prompt to the receiving selected native prompt. Do not add an intermediary stage, hidden relay, extra role, authority transfer, Product Owner gate, approval, Proceed, session, work unit, duplicate vehicle, restart, replan, or alternate route that the native branch does not require. Internal phases within one invocation do not create a continuation. The only GCFPE same-session continuation exception is the selected PR-30 to PR-35 phase change inside the existing `GCF-17` work unit; eligible RS-40 resumes the recorded phase inside that same work unit and vehicle. A terminal-for-invocation result names its Product Owner return and emits no continuation handoff.

Do not create model, strength, reasoning-level, eligibility, suitability, account-availability, Analyzer, or configuration-based routing requirements.

## Runtime artifact persistence and source provenance

For every controlled source, record the exact filename/title, stable identity, version or revision, direct URL, direct parent, observed status, applicability, complete-read state, and digest when the workflow requires one. Historical files, mirrors, rejected artifacts, title matches, search results, archive results, exports, repository copies, or more recently modified native documents do not supersede the unique controlled Markdown authority.

Each off-repository runtime artifact uses a stable filename containing the change or work-unit identity, artifact type, and complete version. It preserves structured headings, exact identifiers, decisions, status, dependencies, evidence links, unresolved items and owners, return point, and next action. The producer saves it in [Glow / Ephemeral Planning Files](https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc), fetches it back completely, verifies exact content, returns the observed direct Drive link separately from any decision and handoff, and carries that link through every dependent record and handoff. Local scratch is active working state only. Reusable prompt bodies remain in Notion and repository-controlled deliverables remain in their authorized repositories.

## Approved-base writer and overlay obligations

Every prompt that creates or revises a Plan, QA Plan, Guide, Specification, remediation proposal, or work-unit instruction first resolves and completely reads the unique current controlled PF10 Markdown plus every applicable active addendum by direct Drive link. The artifact records the PF10 identity/version/direct link, ordered applicable addenda, immutable approved or proposed base separately from overlays, and the applicability and scope of each overlay. It declares whether its context is `INITIAL_OR_PREAPPROVAL_AUTHORING` or `APPROVED_BASE_WITH_OVERLAYS`.

Initial/preapproval drafting and bounded native redline correction remain permitted before approval. Once a base is approved, no prompt may re-author, replace, or silently revise it in flight. A material approved change follows the standalone addendum process. The addendum is distinct from the producer's decision artifact and from its handoff, and its direct Drive link is returned separately from both.

## Exact PF10 build-notes addendum schema

Every qualifying approval creates exactly one standalone Markdown artifact with at least this schema:

```yaml
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: <stable unique change/work-unit decision identity>
artifact_version: <complete successor version>
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
producing_prompt: <stable ID, selected version, direct Notion URL>
approval_decision: <decision ID, version, direct Drive URL>
immutable_base: <artifact ID, version, approval lineage, direct Drive URL>
applicable_prior_addenda: <ordered direct Drive URLs or NONE>
approved_delta: <complete bounded overlay>
affected_surfaces: <requirements, dependencies, tests, Ops, documentation, downstream work>
exclusions: <preserved boundaries>
conflicts: <Canon or active-overlay conflicts, or NONE>
unresolved_items: <item and owner, or NONE>
return_point: <exact native owner/stage and PR_RETURN_PHASE when applicable>
drain_verification_anchor:
  addendum_id: <same stable ID>
  decision_id: <same decision ID>
  immutable_base_id: <same base ID>
  approved_delta_digest: <digest over normalized approved-delta payload>
```

The producer does not allocate a PF10 section number, edit PF10, insert the addendum, declare it active, or resume affected work. Nathan manually drains it. Formatting differences do not invalidate a drain when the stable anchor and normalized substantive payload match.

## Existing-work recovery

Before creating a workspace, checkout, worktree, branch, commit, pull request, or duplicate planning artifact, inspect authorized local roots, repository state, pull-request state, and linked Drive artifacts for the exact change and `WORK_UNIT_ID`. When one consistent prior state exists, verify its identity, provenance, and status and resume the most advanced valid state. When multiple plausible states conflict, stop only the affected action, report the candidates and evidence, and request the smallest necessary decision. Never recreate completed work, overwrite an existing workspace, discard a branch or pull request, infer absence from a failed lookup, force rework because a conversation ended, or invent a session-inspection endpoint or unsupported platform limitation.

For supported remote operations use an authenticated GitHub connector when available; absence of a local `gh` binary is not itself a blocker when the connector can perform the operation.

## RS-20 decision package and return semantics

The controlled loop is `PR-30 or PR-35 -> formal RESCOPE_REQUEST -> same whole-change IA through RS-20 -> decision -> exactly one undrained addendum on qualifying approval -> Nathan manual drain -> fresh PF10 verification -> exact recorded PR phase`. It never restarts IA-30 or IA-40, rewrites an approved Plan, requests another Proceed, reruns an accepted-final PR, routes automatically to PR-50, or fabricates an open pull request.

An RS-20 `APPROVE` result carries the complete decision/direct Drive link; exactly one addendum/direct Drive link; the immutable base and applicable pre-drain PF10/addendum lineage; `PF10_REFERENCE_ROLE: PRE_DRAIN_BASELINE_EVIDENCE`; `FRESH_CURRENT_PF10_RESOLUTION_REQUIRED: true`; exact originating stage and `PR_RETURN_PHASE`; same IA and PR session identities; and, when they exist, the workspace/worktree, branch, pull request, commit/current head, original Proceed, completed work, tests, reviews, CI state, decisions, unresolved-work lineage, and every direct Drive artifact link. It emits one conditional complete destination prompt for use only after Nathan drains. It does not ask Nathan to edit a future link into the handoff or reconstruct prior context.

`REJECT` and `IN_SCOPE_REPAIR` create no addendum and return to the exact existing owner and PR phase under unchanged authority. `REVISION_REQUIRED` creates no addendum, routes through RS-30 to the same request or proposal author, and returns to the same RS-20 decision owner with the original artifact type and all new evidence. `SPECIFICATION_CHANGE_REQUIRED` creates no addendum and returns terminally to Nathan for the native Product Owner decision and Specification-delta route.

## RS-40 post-drain verification and continuation

RS-40 is eligible only for a real existing-open-PR rescope. It independently resolves and reads the current controlled PF10 Markdown, verifies the stable anchor and normalized delta, checks no later applicable overlay conflicts, and preserves the approved base/approval lineage, original Proceed, same PR-development session, workspace/worktree, branch, commit/current head, pull request, artifacts, accepted dependencies, completed work, tests, reviews, CI state, decisions, and unresolved-work lineage.

Each drain result has one exhaustive effect: `SOURCE_RESOLUTION_ERROR` is terminal for the invocation with the failed source predicate and no drain inference; `MANUAL_DRAIN_REQUIRED` is terminal after current PF10 was read and the exact anchor was proved absent; `MANUAL_DRAIN_MISMATCH` is terminal with both sources and the exact decision/base/delta mismatch; `DRAIN_VERIFIED` alone resumes the recorded eligible phase. `PR-30_PREPUBLICATION` never enters RS-40 and resumes PR-30 directly after fresh verification. `PR-30_POSTPUBLICATION` resumes PR-30 through RS-40; `PR-35` resumes PR-35 through RS-40. A failed or ambiguous source, drain, owner, or recovery check preserves evidence and returns terminally to Nathan without accepting, closing, aborting, recreating, or rewriting the work.

## Product Owner-only abort and evidence preservation

Only Nathan / Product Owner may directly and manually invoke `PR-50 - Abort PR and Escalate` for an exact pull request and work unit. PR-50 has zero prompt-, agent-, skill-, hub-, or automation-originated inbound edges. Other actors may return complete unrecoverable evidence to Nathan but may not emit an abort handoff or invoke PR-50.

When directly invoked, PR-50 preserves the session, workspace/worktree, branch, commits/current head, pull request, review and CI evidence, rescope lineage, accepted dependencies, completed unaffected work, decisions, unresolved items, and linked artifacts. It does not delete, reset, rebase, force-push, close, merge, discard, drain PF10, or select another prompt. It returns the evidence and abort/escalation record terminally to Nathan with no continuation prompt. A later substantive escalation requires Nathan's separate native invocation.

## Escalation, remediation, and native receiver compatibility

ESC-30 proposes a bounded remediation or escalation; ESC-40 decides it. ESC-40 `REMEDIATION_REVIEW` is distinct from RS-20 `RESCOPE_REVIEW`. A denial or correction returns to the same Thoth through ESC-30, not to IA-30/IA-40. A qualifying approval creates one addendum and retains the immutable base, original approval identity and `PLAN_REVIEW_ID`, separate remediation decision, and applicable drained overlay. It never substitutes a new base approval, duplicates an approval/addendum, or enters RS-40 without an actual RS-20 rescope decision. Product-intent changes use the selected Specification-delta lane.

RS-10/RS-20 retain bounded planning, prepublication, Ops, documentation, and merged-but-not-accepted finding intake. A return goes to the actual native correction, delivery, or evidence owner, not blindly to discovery. No future detailed PR plan, PR result, pull request, or Proceed becomes a retrospective prerequisite. Initial pending PR-20 work retains its first Product Owner Proceed boundary; proceeded work retains its original Proceed. An accepted-final PR remains final and is never reimplemented or re-reviewed for later governance, drift, or discoveries. A merged-but-not-accepted PR may use a bounded evidence/correction lane but is not fabricated as an open implementation vehicle.

A missing source, owner, manual drain, suitable authority/vehicle, or unrecoverable workspace returns terminally to Nathan for that invocation with preserved evidence and no continuation. This is neither work acceptance, closure, nor abort. Every actionable nonterminal result still has exactly one complete selected-prompt invocation with any manual drain or merge prerequisite explicit.

## Validation before selection

QA-120 preserves the existing Product Owner-classified change identity. A verified `EPIC` PASS routes to CL-E-10; a verified `CRD` PASS routes to CL-C-10. Both carry the separate complete QA Report/RCA and the matching receiver's full approved-source, delivery, readiness, audit/triage, PF10/addendum and remediation intake to continuing Isis. Only the Epic branch carries its existing Strategy Card. Missing/conflicting class, session or required evidence returns to Nathan without a closure handoff; preserve and reuse valid results after recovery. QA supplies evidence; Isis retains the native closure decision. Validate these source-derived class and intake relationships even when graph and contract copies agree.

Read every one of the 55 candidate prompt bodies and all control successors completely. Before selection prove exact unique membership and direct URLs; closed branch-level graph destinations; result/terminal/handoff cardinality; the canonical ten-item PR continuity list; recovery before vehicle creation; local-first and review-first Git/CI behavior; current-head merge readiness; exact six-producer addendum cardinality and exact no-empty-output outcomes; four distinct drain states and phase-aware returns; complete writer overlay behavior; Product Owner-only merge and zero-inbound abort; controlled-Markdown-only PFCanon; Drive-only runtime continuity; exact Alpha tuple; protected Primary-core byte identity; immutable 46-row R1 identity; absence of prohibited routing/source language; all plan section 13 behavior fixtures; and every plan section 14 acceptance criterion.

Record every failure, exact source, correction, dependent rerun, and complete readback. A static or structural pass is not proof of live execution. Any failure keeps the predecessor release selected and Alpha stopped.


## Complete handoff contract

Every concrete nonterminal result contains exactly one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`. The block is the complete prompt for the one actual branch: exact selected receiving prompt name/version/direct Notion URL; receiver role and required continuing or initial session; actual change/Epic identity and current status; completed work, decisions, constraints, unresolved items, preserved authority, next action, and expected output. Carry each direct Drive artifact, work-unit identifier, repository/workspace/branch/commit/PR reference, and session reference only when it already exists and the receiving native contract requires it. A future artifact, blank field, or invented reference is forbidden. A menu, routing summary, blank form, opaque alternate-store identifier, unlinked filename, “above,” or reconstructed conversation is invalid. A terminal-for-invocation result states the stop/completion and returns to Nathan with no continuation block.

A handoff transports evidence and the next exact invocation; it does not itself supply Product Owner Proceed. `PR-20` stops at `AWAITING_PO_PROCEED`. Only Nathan's later direct manual invocation of `PR-30` supplies the one Proceed for the exact `WORK_UNIT_ID`. `PR-30 → PR-35` and eligible `RS-40` continuation preserve that same `WORK_UNIT_ID` and original Proceed and may not request, mint, infer, or require another Proceed.


## PF10 overlay and manual-drain contract

The exact semantic addendum producers are `CF-C-30`, `CF-E-30`, `IA-30`, `QA-70`, `RS-20`, and `ESC-40`. A producer emits exactly one standalone `PF10_BUILD_NOTES_ADDENDUM` only when its native decision approves a material delta to an already approved base. Initial approval, rejection, denial, revision required, pending, unchanged, editorial, and `IN_SCOPE_REPAIR` emit none.

Each qualifying addendum is saved/read back in Glow / Ephemeral Planning Files and contains `status: READY_FOR_MANUAL_DRAIN`, `canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN`, `drain_owner: Nathan / Product Owner`, the exact base/decision/delta/affected surfaces/dependencies/tests/Ops/documentation/downstream work/exclusions/conflicts/unresolved items/return point, and a stable `drain_verification_anchor`. The producer never edits PF10, allocates PF10 numbering, or claims canonical adoption.

Post-drain verification has exactly four mutually exclusive values:

| Result | Predicate |
| --- | --- |
| `SOURCE_RESOLUTION_ERROR` | A unique current controlled PF10 Markdown cannot be resolved and read; make no drain inference. |
| `MANUAL_DRAIN_REQUIRED` | Current PF10 was read and the exact approved anchor is absent. |
| `MANUAL_DRAIN_MISMATCH` | Related content exists but decision, base, or normalized delta differs. |
| `DRAIN_VERIFIED` | Anchor and substantive delta match with no later conflicting overlay; only the recorded phase may resume. |


## PR execution, rescope, merge, and abort contract

`PR-30` and `PR-35` are two phases of one `GCF-17` PR work unit. Across PR-30, PR-35, interrupted recovery, and eligible RS-40 continuation they share exactly one of every item in this canonical list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage. The primary skill authority is `glow-hde-pr-development`. `glow-hde-devops` remains support-only for a specifically required bounded environment, Railway, vendor, database, deployment, Ops, or QA capability and receives no PR-workflow authority.

`PR-30` inspects all authorized local roots, repository state, existing worktrees, branches, pull requests, and linked Drive artifacts before creating anything. It resumes the most advanced consistent state, implements, tests locally before a meaningful commit or push, creates purposeful coherent non-micro commits, and deliberately publishes or reuses one draft PR. A draft may be opened after one coherent locally tested checkpoint. PR-30 does not stop with complete, tested, authorized work uncommitted or unpublished absent a real blocker. `PR_CANDIDATE_PUBLISHED` hands to `PR-35` in the same dedicated session.

`PR-35` retrieves and resolves reviews, retests locally, batches coherent corrections, uses review-first CI economy, verifies unchanged current head, resolved current-head reviews, required current-head CI or an explicit valid waiver, verified remote-head identity, and mergeability, and returns `MERGE_PENDING` without merging. Both phases preserve the session, workspace/worktree, branch, pull request, commit/head, original Proceed, completed work, tests, reviews, CI state, decisions, unresolved-work lineage, and every direct Drive artifact link across recovery and rescope.

`PR_RETURN_PHASE` is exactly one of `PR-30_PREPUBLICATION`, `PR-30_POSTPUBLICATION`, or `PR-35`. A formal PR rescope goes to the same whole-change IA through `RS-20`. Qualifying `APPROVE` creates one undrained addendum; Nathan drains it; the receiver independently resolves current PF10. Prepublication returns directly to PR-30 and never uses RS-40. Open-PR returns use RS-40 and the same vehicle: `PR-30_POSTPUBLICATION` resumes PR-30, while `PR-35` resumes PR-35. Neither branch skips to the other phase. `REJECT` and `IN_SCOPE_REPAIR` return to the exact existing owner/phase with no addendum; `REVISION_REQUIRED` uses RS-30; `SPECIFICATION_CHANGE_REQUIRED` returns terminally to Nathan for the native decision.

`MERGE_PENDING` is historical pre-merge evidence. Nathan later asserts the manual merge only by invoking the conditional PR-40 handoff, and PR-40 independently verifies actual merged state and landed lineage. PR-50 has zero prompt-, agent-, skill-, hub-, or automation-originated inbound edges; only Nathan may directly invoke `Abort PR and Escalate` for an identified PR.

Known actionable review findings take priority over paid CI. Do not intentionally trigger or wait on fresh CI while substantive known findings remain; an automatically started run that becomes stale ceases to be a gate and may be cancelled only through a supported authorized interface. Resolve all then-known findings and retest locally before one coherent corrective push. Never use `[skip ci]` or equivalent suppression without Nathan's direct, specific authorization.

## Recovery and truthful stopping

Recover the most advanced consistent state from actual source artifacts, repository/worktree/branch/PR state, and direct Drive evidence before creating a vehicle. Never invent a session-inspection endpoint or infer absence from failed lookup. A real blocker records the last verified action, missing predicate, evidence present/missing, recovery attempts, smallest owner action, and next safe action in a Drive Markdown checkpoint. `REMOTE_EVIDENCE_PENDING` is PR-35-only, requires no useful local action remaining, and returns one same-session PR-35 re-entry prompt.

An unsupported-platform diagnosis is not a recovery result and cannot substitute for source or provider evidence. PR03-R02 remains accepted technical history only: it is not PF10 proof, prompt-hang proof, Alpha-resumption proof, or authority to reopen or modify accepted PR03.

## Candidate, promotion, and archive sequence

Keep all 55 candidate prompts and control successors unselected until complete semantic and deterministic validation passes. Promote only the pinned all-or-nothing snapshot; read every activated binding back; rerun production validation; then archive superseded controls intact. Never delete, overwrite, reset, or reconstruct predecessors. Alpha remains stopped and PR-10 is not executed during this procedure update.

## Alpha boundary

The sole operative Alpha record remains `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` with PR03 `ACCEPTED_FINAL`, PR04 not started, handoff `NOT_YET_APPROVED`, and Nathan as resume authority. Prepare a new PR04 PR-10 invocation only after the exact successor is selected, production readback and full post-promotion validation pass, superseded prompts and controls are archived intact with verified receipts, the current Alpha record and PR01/PR02/PR03 accepted-final evidence are re-read, current controlled PF10 Markdown and every applicable active addendum are freshly resolved/read, and the newly selected PR-10 exact name/version/direct Notion URL is resolved. Save and read the complete handoff back in Glow / Ephemeral Planning Files. Only Nathan may review and manually invoke it.

On the complete repair branch, `GCFPE-MGMT-10` returns nonterminal `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION` with exactly one complete, fully populated invocation for the newly selected PR-10. Its destination is PR-10 only through Nathan's later manual invocation; producing the result does not execute PR-10, begin PR04, resume Alpha, or activate automation.

## Artifact availability at the native stage

Determine required inputs from the actual native stage and branch. For each artifact, identify its producer, completion or approval state, and whether that event has already occurred on this lineage. A recovery invocation may reuse an existing valid result; it must not require a future result to start. General preservation and PF10 rules protect actual existing bases and never add missing downstream artifacts or approvals. Ordinary Specification formation precedes Implementation Audit/Plan and review; approved implementation planning precedes PR/Ops delivery and final documentation acceptance; QA-10 readiness precedes QA-20 Guide creation; QA-50 creates the separate QA Audit and then QA Plan after that Guide; QA-60 only completes the Plan after an existing valid QA Audit; QA-70 alone reviews the QA Plan; selected QA tasks and reviewed execution evidence precede the separate final Report/RCA and Isis closure. Ordinary PR work has no change-specific QA Guide or QA Plan prerequisite. An existing Guide or other QA evidence may be read for a later approved remedy when specifically relevant; carry the exact existing evidence on which that remedy depends, without a blanket QA requirement or new approval. QA-20 GUIDE_READY is author completion with no separate Guide approval gate. An origin-scoped remediation or recovery package carries only artifacts that actually exist, preserving its native owner and return point.

