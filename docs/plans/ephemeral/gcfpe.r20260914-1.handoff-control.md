---
artifact_type: GCFPE_DIRECT_HANDOFF_CONTRACT_AND_FIXTURES_CONTROL_COPY
artifact_version: "4.0"
title: "GCFPE Direct-Handoff Contract and Fixtures Control Copy — GCFPE-20260914.1"
candidate_release: GCFPE-20260914.1
prompt_version_family: "091426.1"
candidate_member_count: 55
status: UNSELECTED_CANDIDATE_DRAFT
activation_authority: Nathan / Product Owner after separate explicit approval of the exact validated snapshot
predecessor_release: GCFPE-20260913.1
predecessor_version_family: "091326.2"
mutation_posture: UNSELECTED_CANDIDATE_ONLY
recovery_correction_run: GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1
promotion_authorized: false
validation_status: REVALIDATION_REQUIRED_AFTER_SOURCE_IDENTITY_CORRECTION
---

# GCFPE Direct-Handoff Contract and Fixtures Control Copy

## Binding

```yaml
contract_schema: gcfpe-direct-handoff-contract/4.0
release: GCFPE-20260914.1
prompt_version_family: "091426.1"
member_count: 55
graph_contract: candidate/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json
graph_sha256: 77e9e1e0f393fc8bc630a78bda8f50ee77d72e118e436cb2a244e20c9cb0c344
graph_sha256_convention: SHA-256 of the embedded JSON block exactly as it appears in GCFPE-20260914.1-Candidate-Graph-Contract.md, including its trailing newline and excluding the fences
graph_source_binding_revision: 20260916.1-batch-2-contract-synchronization
superseded_graph_sha256: e622e3ce72b2937c3f97c10d8a2190c843d58f476f4b810de468030005f1fe08  # stale before Batch 2; matched none of the five candidate digests of the pre-synchronization graph (whole file, block +/- trailing newline, canonical sort_keys +/- trailing newline) and predates the 20260915.5-batch-1-targeted-correction revision
graph_direct_url: https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk
corrected_source_manifest_url: https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk
source_snapshot_sha256: a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be
selection_status: UNSELECTED_CANDIDATE
```

## Complete handoff contract

Every concrete nonterminal result contains exactly one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`. The block is the complete prompt for the one actual branch: exact selected receiving prompt name/version/direct Notion URL; receiver role and required continuing or initial session; actual change/Epic identity and current status; completed work, decisions, constraints, unresolved items, preserved authority, next action, and expected output. Carry each direct Drive artifact, work-unit identifier, repository/workspace/branch/commit/PR reference, and session reference only when it already exists and the receiving native contract requires it. A future artifact, blank field, or invented reference is forbidden. A menu, routing summary, blank form, opaque alternate-store identifier, unlinked filename, “above,” or reconstructed conversation is invalid. A terminal-for-invocation result states the stop/completion and returns to Nathan with no continuation block.

A handoff transports evidence and the next exact invocation; it does not itself supply Product Owner Proceed. `PR-20` stops at `AWAITING_PO_PROCEED`. Only Nathan's later direct manual invocation of `PR-30` supplies the one Proceed for the exact `WORK_UNIT_ID`. `PR-30 → PR-35` and eligible `RS-40` continuation preserve that same `WORK_UNIT_ID` and original Proceed and may not request, mint, infer, or require another Proceed.


## QA PASS closure compatibility

A verified `EPIC` PASS continues to CL-E-10; a verified `CRD` PASS continues to CL-C-10. Both handoffs carry separate complete QA Report/RCA and the matching approved Specification, Implementation Plan/review, accepted PR/Ops/documentation, readiness/Guide, audit/triage and remediation lineage to continuing Isis. Only an Epic carries its existing Strategy Card. Missing or conflicting class, session or required evidence returns to Nathan with no closure handoff; reuse valid results after recovery. QA supplies evidence and never makes the closure decision. Validate both classes and reject cross-class destinations even when graph and contract copies agree.

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

## Complete v2.0 machine contract

```yaml
handoff_result_cardinality:
  nonterminal_actual_branch: 1
  terminal_for_invocation: 0
  block_fence: text
  block_first_line: NEXT_PROMPT_HANDOFF
handoff_required_fields:
  - selected receiving prompt full name, version, and direct Notion URL
  - receiving role and required continuing or initial session disposition
  - actual Epic or change identity when established or required by the receiver
  - current status, completed work, decisions, constraints, unresolved items, and preserved authority
  - next required action
  - expected output
handoff_conditional_fields:
  - WORK_UNIT_ID only when it already exists and the receiving contract requires it
  - direct Drive artifact links only for artifacts that already exist and the receiving contract requires
  - repository, workspace/worktree, branch, commit, and PR references only when applicable and already existing
  - exact session reference only when it exists or the receiver permits a truthful unassigned state
handoff_forbidden_forms:
  - metadata list
  - routing summary or menu
  - blank form or placeholder
  - opaque alternate-store or Library identifier
  - unlinked filename
  - above-reference or conversation reconstruction
runtime_artifact_continuity:
  store: Glow / Ephemeral Planning Files
  representation: complete efficient machine-readable Markdown
  producer_actions:
    - save
    - fetch back completely
    - verify content
    - return and carry direct Drive link
  prohibited_continuity:
    - Library identifier
    - conversation reconstruction
    - unlinked filename
    - invented link
proceed_boundary:
  handoff_supplies_proceed: false
  PR-20_result: AWAITING_PO_PROCEED
  sole_proceed_actor: Nathan / Product Owner
  sole_proceed_event: direct manual PR-30 invocation for the exact WORK_UNIT_ID
  PR-30_to_PR-35_additional_proceed: 0
  eligible_RS-40_additional_proceed: 0
pr_continuity:
  r1_row: GCF-17
  shared_exactly_one:
    - WORK_UNIT_ID
    - original Product Owner Proceed
    - dedicated PR-development session
    - workspace/worktree
    - branch
    - pull request
    - PR instruction
    - detailed PR plan
    - primary skill authority
    - continuous recovery/artifact lineage
  added_roles_approvals_gates_sessions_work_units_vehicles_R1_rows_merge_authority: 0
PF10_overlay:
  exact_semantic_producers:
    - CF-C-30
    - CF-E-30
    - IA-30
    - QA-70
    - RS-20
    - ESC-40
  qualifying_output: exactly one standalone PF10_BUILD_NOTES_ADDENDUM
  qualifying_predicate: native decision approves a material delta to an already approved base
  nonqualifying_outcomes:
    - initial approval
    - rejection or denial
    - revision required
    - pending
    - unchanged
    - editorial
    - IN_SCOPE_REPAIR
  addendum_status: READY_FOR_MANUAL_DRAIN
  addendum_canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
  drain_owner: Nathan / Product Owner
  required_fields:
    - artifact_type
    - addendum_id
    - artifact_version
    - status
    - canonicality
    - drain_owner
    - producing_prompt stable ID, selected version, and direct Notion URL
    - approval_decision ID, version, and direct Drive URL
    - immutable_base ID, version, approval lineage, and direct Drive URL
    - ordered applicable_prior_addenda direct Drive URLs or NONE
    - complete approved_delta
    - affected requirements, dependencies, tests, Ops, documentation, and downstream work
    - exclusions, conflicts, and unresolved items with owners
    - exact return_point and PR_RETURN_PHASE when applicable
    - stable drain_verification_anchor with addendum ID, decision ID, base ID, and normalized delta digest
  producer_edits_PF10: false
  producer_allocates_PF10_numbering: false
  producer_claims_canonical_adoption: false
rescope_continuation:
  PR_RETURN_PHASE_values:
    - PR-30_PREPUBLICATION
    - PR-30_POSTPUBLICATION
    - PR-35
  PR-30_PREPUBLICATION: direct same-phase PR-30 continuation after fresh DRAIN_VERIFIED; RS-40 ineligible; no open PR fabricated
  PR-30_POSTPUBLICATION: RS-40 resumes recorded PR-30 phase in the same open-PR vehicle after fresh DRAIN_VERIFIED
  PR-35: RS-40 resumes PR-35 in the same open-PR vehicle after fresh DRAIN_VERIFIED
  IN_SCOPE_REPAIR_or_REJECT: same repair owner and exact phase under unchanged authority; no addendum
  REVISION_REQUIRED: RS-30 to same request or proposal author, then same RS-20 owner
  SPECIFICATION_CHANGE_REQUIRED: terminal Nathan return for native Product Owner decision and Specification-delta route
PR_phase_results:
  PR-30:
    success: PR_CANDIDATE_PUBLISHED
    other:
      - RESCOPE_PENDING
      - RECOVERY_PENDING
      - PRODUCT_OWNER_DECISION_REQUIRED
  PR-35:
    success: MERGE_PENDING
    other:
      - RESCOPE_PENDING
      - RECOVERY_PENDING
      - REMOTE_EVIDENCE_PENDING
      - PRODUCT_OWNER_DECISION_REQUIRED
PFCanon_source:
  allowed_representation: unique controlled Markdown direct child of Glow / Core Docs / PFCanon
  native_document_action: DO_NOT_OPEN_FETCH_INSPECT_COMPARE_CITE_OR_USE
  unresolved_result: SOURCE_RESOLUTION_ERROR
PF10_drain_verification:
  exhaustive_results:
    - SOURCE_RESOLUTION_ERROR
    - MANUAL_DRAIN_REQUIRED
    - MANUAL_DRAIN_MISMATCH
    - DRAIN_VERIFIED
  DRAIN_VERIFIED_requires:
    - matching stable drain_verification_anchor
    - substantively equivalent normalized approved delta
    - no later conflicting overlay
observation_boundary:
  unsupported_platform_diagnosis: PROHIBITED
  invented_session_inspection_endpoint: PROHIBITED
  REMOTE_EVIDENCE_PENDING_requires:
    - actual external review or check evidence unavailable
    - no useful local action remains
    - saved and read-back recovery checkpoint
    - one complete same-session PR-35 re-entry handoff
post_merge_three_event_contract:
  event_1: earlier PR-35 MERGE_PENDING is historical pre-merge evidence
  event_2: Nathan later asserts the manual merge by invoking the conditional PR-40 handoff
  event_3: PR-40 independently verifies actual merged state and landed lineage
  agent_merge_or_auto_merge_authorized: false
abort_boundary:
  exact_entry: Nathan / Product Owner directly and manually invokes Abort PR and Escalate for an identified PR
  prompt_agent_skill_hub_automation_inbound_edges: 0
  other_actors_return_evidence_to_Nathan_only: true
RCA_separation:
  PR03-R02: ACCEPTED_TECHNICAL_HISTORY_ONLY
  not_proof_of:
    - PF10 state
    - prompt hang
    - Alpha resumption readiness
  reopen_or_modify_accepted_PR03: false
Alpha_preparation:
  gates:
    - exact successor selected
    - production bindings read back
    - full post-promotion validation passed
    - superseded prompts and controls archived intact with verified receipts
    - Alpha record re-read with PR03 ACCEPTED_FINAL and PR04 not started
    - PR01, PR02, and PR03 accepted-final evidence re-read
    - current controlled PF10 Markdown and all applicable active addenda re-read
    - newly selected PR-10 exact name, version, and direct Notion URL resolved
    - complete PR04 PR-10 handoff saved and read back in Glow / Ephemeral Planning Files
  execute_PR-10: false
  resume_Alpha: false
```

## Exact §13 deterministic fixture catalog

| Fixture | Scenario | Required result |
| --- | --- | --- |
| `PR-SPLIT-POS-01` | Fresh proceeded PR with no prior work | PR-30 implements/tests/commits/publishes once, then hands to same-session PR-35. |
| `PR-SPLIT-POS-02` | Existing matching worktree and draft PR | PR-30 or PR-35 recovers the most advanced consistent state; no duplicate workspace or PR. |
| `PR-SPLIT-NEG-01` | PR-35 asks for another Proceed or session | Validation failure. |
| `PR-SPLIT-NEG-02` | PR-30 stops with complete tested work but no coherent commit/publication without a blocker | Validation failure. |
| `PR-COST-POS-01` | Known review findings and active CI | Fix and test locally first; stale CI is not awaited; cancel only if supported; one coherent corrected push. |
| `PR-COST-POS-02` | New findings arrive after CI auto-starts | Mark current run stale, correct locally, avoid another push until all known findings are resolved. |
| `PR-COST-NEG-01` | Micro-commits or pushes after every edit | Validation failure. |
| `PR-COST-NEG-02` | `[skip ci]` used without direct authorization | Validation failure. |
| `PR-READY-POS-01` | Clean current head | PR-35 proves resolved reviews, passing current-head CI, remote-head identity, and mergeability before `MERGE_PENDING`. |
| `PR-MERGE-NEG-01` | Agent attempts merge or auto-merge | Validation failure. |
| `PF10-POS-01` | RS-20 approves bounded open-PR rescope | Exactly one undrained addendum and conditional RS-40 package; no base rewrite or new Proceed. |
| `PF10-POS-02` | Nathan drains; current PF10 contains exact overlay | RS-40 returns `DRAIN_VERIFIED` and resumes recorded PR phase. |
| `PF10-NEG-01` | Only pre-drain PF10 is supplied | RS-40 resolves current Markdown independently; supplied predecessor is historical evidence only. |
| `PF10-NEG-02` | Current PF10 cannot be uniquely resolved | `SOURCE_RESOLUTION_ERROR`; never `MANUAL_DRAIN_REQUIRED`. |
| `PF10-NEG-03` | Current PF10 resolves and exact addendum is absent | `MANUAL_DRAIN_REQUIRED` with exact missing identity. |
| `PF10-NEG-04` | Related section exists but approved delta differs | `MANUAL_DRAIN_MISMATCH`; no implementation. |
| `PF10-NEG-05` | Rejection, revision, in-scope repair, pending, or initial approval | No addendum. |
| `RS-DECISION-01` | Ordinary in-scope defect | `IN_SCOPE_REPAIR`; no rescope approval or PF10 addendum. |
| `RS-DECISION-02` | Product-intent change | `SPECIFICATION_CHANGE_REQUIRED`; terminal Nathan return, no IA overreach. |
| `RS-RETURN-01` | Prepublication rescope | Resume same PR-30 phase after drain; do not manufacture RS-40 eligibility. |
| `RS-RETURN-02` | Rescope during PR-35 | RS-40 resumes PR-35 responsibilities in same vehicle. |
| `ABORT-POS-01` | Nathan manually invokes PR-50 for exact PR | Prompt executes its preserved evidence/abort-escalation contract. |
| `ABORT-NEG-01` | Any agent or prompt routes to PR-50 | Validation failure; return evidence to Nathan without an abort handoff. |
| `HANDOFF-POS-01` | PR-30 completes initial publication | One complete, runnable PR-35 prompt with exact selected name/version/URL and full continuity. |
| `HANDOFF-POS-02` | PR-35 reaches merge readiness | Conditional post-manual-merge PR-40 prompt separates historical and current event facts. |
| `HANDOFF-NEG-01` | Metadata list, blank field, Library ID, “above,” or unlinked filename | Validation failure. |
| `SOURCE-POS-01` | Controlled PFCanon Markdown available | Read permitted and provenance recorded. |
| `SOURCE-NEG-01` | Only GDoc/DOC/DOCX candidate is found | Source blocker without opening the candidate. |
| `ALPHA-POS-01` | Successor selected and all gates pass | Produce PR04 PR-10 handoff only; do not execute it. |
| `ALPHA-NEG-01` | Older PR02/RS-20 or void PR04 handoff supplied | Reject as historical/non-operative. |
| `OBS-POS-01` | Remote evidence is genuinely pending | Durable checkpoint plus same-session PR-35 re-entry; no fabricated liveness claim. |
| `OBS-NEG-01` | Session-inspection endpoint or unsupported platform diagnosis is asserted | Validation failure. |
| `RCA-SEPARATION-01` | PR03-R02 code issue appears in source evidence | Preserve as accepted technical history; do not treat it as PF10, prompt-hang, or Alpha-resumption proof. |

The validator must execute behavior fixtures, not only string scans. Every repair reruns all dependent fixtures. Candidate prompt URL tokens are local authoring-only and must be absent after publication.

## Artifact availability at the native stage

Determine required inputs from the actual native stage and branch. For each artifact, identify its producer, completion or approval state, and whether that event has already occurred on this lineage. A recovery invocation may reuse an existing valid result; it must not require a future result to start. General preservation and PF10 rules protect actual existing bases and never add missing downstream artifacts or approvals. Ordinary Specification formation precedes Implementation Audit/Plan and review; approved implementation planning precedes PR/Ops delivery and final documentation acceptance; QA-10 readiness precedes QA-20 Guide creation; QA-50 creates the separate QA Audit and then QA Plan after that Guide; QA-60 only completes the Plan after an existing valid QA Audit; QA-70 alone reviews the QA Plan; selected QA tasks and reviewed execution evidence precede the separate final Report/RCA and Isis closure. Ordinary PR work has no change-specific QA Guide or QA Plan prerequisite. An existing Guide or other QA evidence may be read for a later approved remedy when specifically relevant; carry the exact existing evidence on which that remedy depends, without a blanket QA requirement or new approval. QA-20 GUIDE_READY is author completion with no separate Guide approval gate. An origin-scoped remediation or recovery package carries only artifacts that actually exist, preserving its native owner and return point.

