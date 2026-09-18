# GCFPE Batch 2 Contract Ledger v1.0 — 20260915

> ### ⚠️ Read as a dated record, not as current status
>
> Written before the cross-cutting drainage removal merged (2026-09-18, PR #415). Where
> this document reports something as *open, standing, deferred to a later batch, or the
> current contract*, check it against the merged baseline first. Specifically:
>
> - the **interim one-check replacement** (`pf10_reference_visibility_check`,
>   `PF10_REFERENCE_VISIBILITY`) was **struck** — no post-addendum check survives, and
>   neither token exists in `docs/graph/parts/global.json`;
> - the `RS-40.drain_verified` **orphan route is closed** and the builder emits no
>   warning;
> - the current graph proof token is **55 nodes · 227 edges · 55 state_routes**; any
>   235/236/240-edge token here is a dated measurement;
> - **Batch 2's blocker is dead** (decision record D10);
> - work deferred here "to Batches 2–5" for the drainage lifecycle was completed outside
>   the batch sequence by the cross-cutting repair.
>
> Current authority: `docs/prompt_ecosystem_management/gcfpe.decision-record.md`,
> `docs/prompt_ecosystem_management/authoritative-surfaces.md`, and
> `docs/ephemeral/gcfpe.drainage-removal.repair-report.md`.


```yaml
artifact_type: GCFPE_BATCH_2_CONTRACT_LEDGER
artifact_version: "1.0"
execution_date: 2026-09-15
execution_scope: BATCH_2_ONLY
candidate: "GCFPE-20260914.1 / 091426.1 / 55 / UNSELECTED_CANDIDATE"
protected_selected_release: "GCFPE-20260913.1 / 091326.2 / 54"
review_state: PRE_EDIT_FINDINGS_RECORDED
author_validation_only: true
```

## Authority and frozen source set

Execution authority is Nathan's direct `GCFPE Batch 2 Prompt Repair Handoff — 20260915`. The approved plan is `GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist v1.0`, Notion page `3dc4590a05eb81a9adf1d8f800863937`, observed `2026-09-15T16:58:37.669Z`, and controlled Drive Markdown `1CUQsQo6KDX1ZHxNfngHls5qW0HaOzHnG`, modified `2026-09-15T15:26:29.660Z`. The original Batch 1 report, Drive `1Gj_x3I-cIWwlZX9U5l4HLPn38ru2gll-`, is historical wherever superseded. The corrective report, Drive `1M7Ni7TGrZfIgHpCW1xlvPnKS9js0LazE`, modified `2026-09-15T18:09:29.579Z`, is the controlling Batch 1 correction evidence within its stated author-self-review scope.

Candidate controls inspected completely: candidate catalog `3db4590a05eb81738ef1d846e3c0df8c` at `2026-09-15T07:10:51.829Z`; Flow Index `3db4590a05eb81de9736ea69bac61016` at `2026-09-15T09:26:56.083Z`; PE Metaprompt `3db4590a05eb8174be35d9e35acb3f77` at `2026-09-15T16:43:54.400Z`; HDE IA hub `3db4590a05eb8195a2ccf7c0959a8b6e` at `2026-09-15T09:27:04.215Z`; candidate graph Drive `1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp`, source binding revision `20260915.5-batch-1-targeted-correction`, source SHA-256 `6b5211f3ea51aa1e2ecfa178e243e9821ab15cad625de6424bcae603bf563ea6`; Direct-Handoff Fixtures Control Copy Drive `1svSBwxD4HEphs8TCh1gZV9KRTKWq8ZlU`; operating procedure Drive `1TDtZNMNxgqt6h-HzQ2up_syK5zauLqBj`.

All seven complete candidates and seven complete selected predecessors were read before this ledger was written. PR-10, RS-20, OPS-10, DOC-10, and QA-10 candidates were inspected read-only as affected or eventual consumers; no later-batch prompt is authorized for edit.

## Per-prompt identity and contract findings

### B2-IA10 — IA-10

- Candidate: `IA-10 — Create Whole-Change Implementation Audit and Plan — 091426.1`, Notion `3db4590a05eb817aa191f1e822c30480`, observed `2026-09-15T09:24:56.298Z`, `UNSELECTED_CANDIDATE`.
- Selected predecessor: `091326.2`, Notion `3da4590a05eb8130b2fcf3993239096c`, observed `2026-09-13T11:35:18.593Z`, read only.
- Native purpose: in the dedicated whole-change IA session, complete the Implementation Audit first and then create a separate initial pending Implementation Plan; preserve recoverable interruption states; do not review or execute.
- Required initial inputs: exact approved CRD/Epic Specification and exact Thoth decision from CF-C-30/CF-E-30; change/class lineage; carried conflict register; actual source/repository/access facts needed for audit; truthful IA session binding; current controlled PFCanon/PF10 and applicable overlays as resolved by the writer.
- Conditional/recovery inputs: saved Audit/Plan checkpoint, `RECOVERY_ENVELOPE`, `ANSWER_REF`, research finding, existing reviewer binding, or changed repository facts only when those items already exist and the actual recovery branch needs them.
- Absence behavior: first entry must not require an Audit, Plan, approval, research result, work unit, PR, QA artifact, or already-assigned reviewer session. Missing decisive source/authority is terminal; incomplete Audit returns to same IA-10; complete Audit/incomplete Plan returns to IA-20.
- Outputs: separate `IMPLEMENTATION_AUDIT` then `IMPLEMENTATION_PLAN`; states `AUDIT_COMPLETE`, `PLAN_PENDING`, or `BLOCKED`; saved separately as Drive Markdown and read back.
- Finding `B2-IA10-C1`: `Required inputs` makes `actual IA and reviewer/session bindings` unconditionally required. The reviewer/session may not yet exist on first entry; Batch 1 guarantees only a truthful IA-session-binding state, not a future reviewer session.
- Finding `B2-IA10-C2`: `Result routing` contains an impossible “exact Plan correction after initial denial” branch inside a prompt whose native operation is initial Audit/Plan creation; a prior denial belongs to IA-40 intake, not ordinary IA-10 entry.
- Finding `B2-IA10-C3`: required separate Audit-only and Plan-creation proof artifacts are not required by the approved plan, predecessor native contract, graph output set, or downstream receiver. They add mandatory outputs and write-failure states without a supported consumer.
- Expected repair: make reviewer/session conditional; remove the denial-correction branch from IA-10; retain only the Audit/Plan/checkpoint artifacts and one lawful branch per actual result.

### B2-IA50 — IA-50

- Candidate: `IA-50 — IA Answer Seeder — 091426.1`, Notion `3db4590a05eb81d78eeae384e93dd697`, observed `2026-09-15T09:25:31.214Z`.
- Selected predecessor: Notion `3da4590a05eb8107a012f68e6b8fd98c`, observed `2026-09-13T11:35:31.624Z`.
- Native purpose: validate one actual answer/finding against one paused IA question/checkpoint and prepare the exact same-author continuation; no substantive Plan decision or authoring.
- Required inputs: complete `RECOVERY_ENVELOPE`; actual `ANSWER_REF` with full text or permitted complete retrievable artifact, identity, source/authority, limitations; exact paused native prompt and base/checkpoint.
- Optional/conditional: partial-answer map, prior application report, reviewer/session binding, and current source overlays only when the paused native branch uses them.
- Outputs: `IA_RECOVERY_SEED`; `SEED_READY` or `SEED_INCOMPLETE`; return only to IA-10, IA-20, IA-30 assessment, or IA-40 when the paused state and receiver predicates support that route.
- Finding `B2-IA50-C1`: the candidate imports remediation artifacts and an ESC-40 route even though its native purpose is IA planning answer seeding and the plan reserves escalation/remediation to Batch 5. This broadens task and downstream authority.
- Finding `B2-IA50-C2`: the IA-30 route requires a complete evidenced material Plan delta, but it also says IA-30 establishes a correction boundary when one does not exist. This fails to distinguish an approved-base finding/request from an already-authored pending delta and contributes to a circular first-delta path.
- Finding `B2-IA50-C3`: duplicate answers are classified `SEED_INCOMPLETE` even when an existing valid applied successor is resolved; that conflates idempotent reuse with an incomplete seed.
- Expected repair: confine to IA planning; separate `APPROVED_BASE_FINDING_OR_REQUEST` from `PENDING_PLAN_DELTA`; route the former to IA-30 assessment and the latter only when a real delta exists; classify resolved duplicate reuse as `SEED_READY_REUSED` or preserve graph-compatible `SEED_READY` with reuse evidence.

### B2-IA60 — IA-60

- Candidate: `IA-60 — Thoth Planning Research — 091426.1`, Notion `3db4590a05eb8141b5b2c8fbf7b725e2`, observed `2026-09-15T09:25:34.465Z`.
- Selected predecessor: Notion `3da4590a05eb81f78afcca35f2dcb7db`, observed `2026-09-13T11:35:31.624Z`.
- Native purpose: answer one bounded advanced engineering planning inquiry before Plan approval and return the finding to the paused IA through IA-50.
- Required inputs: `PLANNING_INQUIRY`, `RECOVERY_ENVELOPE`, actual source/repository evidence and criteria needed by the question; no approved Plan or review ID.
- Outputs: `PLANNING_RESEARCH_FINDING`; `RESEARCH_COMPLETE`, `PARTIAL`, or `BLOCKED`; complete or usable partial research returns to IA-50, while a missing governing decision/source returns terminally to its owner.
- Finding `B2-IA60-C1`: graph and candidate retain a second `RESEARCH_COMPLETE → ESC-30` route for post-failure remediation although the role says not to take over ESC-30 and the approved Batch 2 scope is preapproval planning research.
- Finding `B2-IA60-C2`: `PARTIAL` is always terminal, which discards a source-supported usable partial answer even though the required cases demand usable partial answers return through seeding with remaining unknowns preserved.
- Expected repair: remove remediation intake/route; send complete or usable partial answer to IA-50; reserve terminal return for unusable partials, missing authority, or source failure.

### B2-IA20 — IA-20

- Candidate: `IA-20 — Create Whole-Change Implementation Plan — 091426.1`, Notion `3db4590a05eb81c4825df2ad0dec4750`, observed `2026-09-15T09:24:59.007Z`.
- Selected predecessor: Notion `3da4590a05eb8198bffdf367600ab5b3`, observed `2026-09-13T11:35:26.190Z`.
- Native purpose: same-author plan-only continuation after a complete valid Audit, normally after interruption; do not repeat the Audit.
- Required inputs: approved Specification/Thoth decision; complete valid Audit; same IA/change/class; current controlled PFCanon/PF10 and applicable overlays; carried conflict register.
- Conditional: Plan checkpoint, answers/research, reviewer binding, materially changed repository facts, and access limits only if they exist/apply.
- Outputs: one initial/preapproval `IMPLEMENTATION_PLAN`; `PLAN_PENDING` or `BLOCKED`; return to IA-30, same IA-20 recovery, IA-50/IA-60 support, or terminal owner.
- Finding `B2-IA20-C1`: reviewer binding is made unconditional although the reviewer session may not yet exist at a valid interrupted first Plan continuation.
- Finding `B2-IA20-C2`: a separate mandatory Plan-creation proof has no source-supported native consumer and adds an unsupported write requirement.
- Finding `B2-IA20-C3`: denial correction is routed from IA-20 to IA-40 even though IA-20 is not the review owner and a valid denial should invoke IA-40 directly from IA-30.
- Expected repair: conditionalize reviewer/checkpoint/research inputs; remove proof artifact and denial branch; preserve plan-only recovery and exact IA-30 intake.

### B2-IA30 — IA-30

- Candidate: `IA-30 — Review Whole-Change Implementation Plan — 091426.1`, Notion `3db4590a05eb81c6bfb5f36f7df8f464`, observed `2026-09-15T09:25:24.817Z`.
- Selected predecessor: Notion `3da4590a05eb81029c49c21113701638`, observed `2026-09-13T11:35:26.190Z`.
- Native purpose: Isis reviews either an initial pending Plan or a bounded pending delta against an immutable approved Plan; it does not author the Plan/delta or implement work.
- Initial required inputs: complete pending Plan, approved Specification, complete Audit, same IA author/change, conflict register and source evidence. Existing reviewer session is the current actor, not a future artifact.
- Approved-base assessment inputs: immutable approved Plan/review plus a source-backed factual finding or actual authorized material-change request; no pending delta required at this assessment entry.
- Delta-review inputs: immutable approved Plan/review plus one complete pending `MATERIAL_PLAN_DELTA`, exact originating author/return phase, current PF10 and applicable addenda.
- Outputs: initial `APPROVE`/`DENY`; correction assessment result; delta `APPROVE`/`DENY`; exactly one addendum only for material delta approval.
- Finding `B2-IA30-C1`: current `MATERIAL_PLAN_DELTA_REVIEW` requires a complete delta but no Batch 2 prompt owns creation of the first delta. IA-40 rejects approved bases and IA-20 refuses approved-base work. This is circular and fails case D.
- Finding `B2-IA30-C2`: current two-value `REVIEW_MODE` cannot represent approved-base finding assessment before a delta exists.
- Finding `B2-IA30-C3`: initial approval routes to PR-10 without making clear that PR-10 receives one actual planned PR unit at a time and that Ops/documentation/QA-readiness consumers remain governed by the approved Plan rather than being blanket prerequisites for PR-10.
- Finding `B2-IA30-C4`: material approval is represented in the graph as a nonterminal handoff to `NATHAN_MANUAL_PF10_DRAIN` with count one. Manual drainage is a terminal boundary for this invocation; the addendum records the post-drain return point, but no agent continuation runs before Nathan drains it.
- Finding `B2-IA30-C5`: addendum creation lacks an explicit stable-ID/digest read-before-create reuse rule, so repeated handling can duplicate a qualifying addendum.
- Expected repair: add `APPROVED_BASE_CHANGE_ASSESSMENT`; issue exact `PLAN_DELTA_REDLINE` to the same IA author via IA-40 for first-delta creation; review the resulting pending delta in `MATERIAL_PLAN_DELTA_REVIEW`; make approval terminal to Nathan for manual drain; add duplicate-safe addendum reuse; clarify initial PR-10 work-unit intake without upstream QA leakage.

### B2-IA40 — IA-40

- Candidate: `IA-40 — Prepare or Revise Whole-Change Implementation Plan — 091426.1`, Notion `3db4590a05eb8197bb1bc8f52f896969`, observed `2026-09-15T09:25:28.133Z`.
- Selected predecessor: Notion `3da4590a05eb819d920ac5f14a042d08`, observed `2026-09-13T11:35:26.190Z`.
- Native purpose: same IA author applies exact Isis redlines. It must keep preapproval Plan revision separate from approved-base standalone delta authoring/revision.
- Preapproval required inputs: complete pending Plan and exact IA-30 denial/redline, or exact interrupted correction checkpoint.
- Approved-base delta required inputs: immutable approved Plan/review, exact IA-30 assessment/redline or delta-denial redlines, existing pending delta when revising, applicable PF10/addenda, same author/reviewer and return point.
- Outputs: complete revised pending Plan or complete standalone pending `MATERIAL_PLAN_DELTA`; application report; return only to same IA-30 review lineage.
- Finding `B2-IA40-C1`: the prompt refuses all approved-base material Plan-delta authoring, leaving IA-30's delta review without a producer and routing a nonexistent delta back to IA-30.
- Finding `B2-IA40-C2`: wrong-route branches to RS-20 and ESC-40 import later-lane routing instead of returning evidence to the actual origin owner when the input is truly rescope/remediation.
- Finding `B2-IA40-C3`: blanket PR/QA/remediation prose obscures the two authoring modes and creates contradictory wording about whether a standalone proposed delta can be authored.
- Expected repair: add a distinct `APPROVED_BASE_PLAN_DELTA_AUTHORING` mode that creates/revises only the standalone delta, never the base; return it to IA-30. True rescope/remediation stays terminal to the supplied origin owner without executing later prompts.

### B2-UTIL10 — UTIL-10

- Candidate: `UTIL-10 — Apply Exact Redline to a Complete Artifact — 091426.1`, Notion `3db4590a05eb81b89fbaf4b31a3ed2a9`, observed `2026-09-15T09:26:51.922Z`.
- Selected predecessor: Notion `3da4590a05eb8114a88cda5c9728e26c`, observed `2026-09-13T11:36:39.293Z`.
- Native purpose: the original author or explicitly authorized editor applies an exact redline to the exact complete reviewed base, preserving unaffected content and returning to the originating review owner; no substantive authorship or approval.
- Required inputs: exact base/version, complete redline and decision owner, exact target anchors/operations/replacement text, editor authority, originating owner/session/prompt and change identity.
- Conditional: PFCanon/PF10/addenda, conflict register, repository references, and prior application report only when the target lineage or redline actually depends on them.
- Outputs: complete revised target plus `REDLINE_APPLICATION_REPORT`; `COMPLETE`, `INCOMPLETE`, or idempotent `ALREADY_APPLIED`; return to actual origin owner or terminal Nathan when unresolved.
- Finding `B2-UTIL10-C1`: `Required inputs` makes current PF10/addenda and conflict register universal even for an artifact/redline unrelated to PF10 or Canon conflict.
- Finding `B2-UTIL10-C2`: accepting “an unambiguous bounded instruction” is broader than exact-redline behavior. Exact target, operation and replacement text are required; a missing/ambiguous target must return without substantive interpretation.
- Finding `B2-UTIL10-C3`: already-applied behavior is buried in recovery and not an explicit idempotent result, weakening repeated-invocation handling.
- Expected repair: make lineage inputs conditional; require exact replacement text and uniquely resolvable targets; add explicit `ALREADY_APPLIED`; prohibit semantic gap filling; return to the exact originating owner.

## Pre-edit static/tabletop cases

| Case | Synthetic input facts | Expected route/result before any PASS can be claimed |
|---|---|---|
| A1 | First approved Specification; no Audit, Plan, reviewer session, research, PR, or QA artifact exists | IA-10 accepts the package, creates Audit first and separate pending Plan; no future artifact is required. |
| B1 | Audit checkpoint incomplete with valid completed rows | Same IA-10 resumes first incomplete Audit point and preserves completed rows. |
| B2 | Audit complete; Plan incomplete | IA-20 resumes only Plan work; Audit is not repeated. |
| B3 | Complete valid Audit and Plan already saved | Reuse result and route once to IA-30; create no duplicate artifacts. |
| C1 | Direct Product Owner answer fully covers paused question | IA-50 validates and returns to exact paused IA owner; IA-60 is not invoked. |
| C2 | Research finding answers only a usable subset | IA-60 returns usable partial to IA-50; unanswered subset/owner remains explicit. |
| C3 | Answer is stale or contradictory | IA-50 returns terminally to answer/base owner; no runnable author handoff. |
| C4 | Same answer already applied and successor resolves | Reuse the exact successor; no duplicate Plan or seed. |
| D1 | Initial Plan denied with exact redlines | IA-30 → same IA author through IA-40 → same IA-30 reviewer; pending base only. |
| D2 | Approved Plan plus source-backed factual finding; no delta exists | IA-30 assesses; if justified, exact delta redline → same IA author IA-40 creates first standalone pending delta → same IA-30 reviews. |
| D3 | Approved Plan plus already-authored pending delta | IA-30 reviews the delta directly; no authoring duplication. |
| D4 | Finding is truly PR rescope or QA remediation | Batch 2 preserves exact origin/owner and does not impersonate RS/ESC lanes. |
| E1 | Initial Plan approval | Zero PF10 addenda; hand one actual planned PR unit to PR-10 with approved Plan/review lineage; no QA Guide/Plan prerequisite. |
| E2 | Qualifying material Plan-delta approval, first handling | Exactly one addendum; terminal return to Nathan for manual drain; base unchanged. |
| E3 | Same approval handled again with matching stable ID/digest | Reuse matching read-back addendum; no duplicate. |
| E4 | PF10 cannot be resolved | `SOURCE_RESOLUTION_ERROR`, not an inference that drainage is missing. |
| E5 | PF10 resolves but anchor absent or mismatched | `MANUAL_DRAIN_REQUIRED` or `MANUAL_DRAIN_MISMATCH`; only matching content yields `DRAIN_VERIFIED`. |
| F1 | UTIL exact unique replacement | Apply once, preserve unaffected content, return complete successor/report to originating reviewer. |
| F2 | UTIL target missing or ambiguous | No edit; `INCOMPLETE` with exact ambiguity and owner. |
| F3 | UTIL change already present with matching base/redline lineage | `ALREADY_APPLIED`; reuse existing successor/report. |
| F4 | UTIL redline would rewrite approved base or PF10 | Refuse; preserve evidence; return to actual origin owner/Nathan without applying. |
| G1 | PR-10 receives first planned PR unit after Plan approval | Receives approved Specification/Audit/Plan/review and exact planned unit; no future PR, Proceed, QA Guide/Plan, Ops receipt, or documentation completion is required. |

## Pre-edit completion effect

The seven-prompt interface is not clean before repair. Findings `B2-IA30-C1` and `B2-IA40-C1` are material and circular; `B2-IA60-C1/C2` and `B2-IA50-C1` broaden or block the research/answer route; the remaining findings create future-input, duplicate-write, or exact-redline defects. No prompt disposition is final until persisted repairs and post-edit cases are read back.
