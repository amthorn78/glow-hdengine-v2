# GCFPE Direct-Handoff and Runtime Artifact Operating Procedure

Version: 3.1.0

Date: 2026-09-13

Activation: this procedure governs only when the sole release register selects GCFPE-20260913.1 at prompt version 091326.2 after successful validation. Until then, the predecessor procedure remains selected. Publication alone has no activation effect.

Predecessor: `GCFPE-20260912.2`; it remains selected while this candidate is staged and validated.

Predecessor procedure: [GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v2.0.0 — 20260912.md](https://drive.google.com/file/d/1SXrg6m6sP8eX1EGvVtDTgLc795LrOkni/view?usp=drivesdk); preserve it intact.

## Purpose and authority

This procedure governs GCFPE prompt selection, runtime planning artifacts, continuation handoffs, PR-development execution, in-flight PF10 overlays, manual abort/escalation, and promotion validation. It preserves the immutable R1 sources, the protected Flowmaster Primary core, every approved Plan/Guide/Specification as an in-flight base, and every native prompt's unaffected planning, engineering, evidence, review, approval, QA, Ops, recovery, and closure behavior.

The Notion [GCFPE Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204) is the only authority for selected release membership. The [Glow HDE Prompt Flow Index](https://app.notion.com/p/3cc4590a05eb8101b5ded32c12616eb6?pvs=204) identifies the governed workflow context. Never choose or invoke a prompt from search rank, recency, a predecessor catalog, an unselected candidate title, or historical Alpha material.

At candidate inventory, the controlled PF10 Markdown source was `PF10-HDE-Build-Notes-v13.1.8.md`, [direct Drive link](https://drive.google.com/file/d/1Qm-oszL0JfPt0TzVfQsws4hjGb9n83e6/view?usp=drivesdk). This observed binding does not waive the duty to resolve the exact current controlled PF10 Markdown and all applicable active addenda at runtime.

## Direct continuation

Every nonterminal substantive continuation goes directly from the producing selected native prompt to the receiving selected native prompt. Do not add an intermediary stage, hidden relay, extra gate, restart, replan, or alternate route that the native branch does not require. Internal phases within one invocation do not create a new continuation. A true terminal result names its return owner and emits no continuation handoff.

## Paste-ready handoff

Each nonterminal final response ends with exactly one fenced plain-text block headed `NEXT_PROMPT_HANDOFF`. The block is the complete prompt the operator can paste into the receiving session. It is not a metadata list, routing summary, blank form, menu, or collection of alternatives.

The handoff must:

1. Begin by directing the receiver to run the exact selected destination prompt by name, version, and direct Notion URL.
2. Name the actual receiving role or dedicated session when the workflow requires one.
3. State the Epic, CRD, PR, work unit, or other change identifier.
4. Give direct Google Drive links for every required artifact, with filenames and versions or immutable identifiers where needed.
5. State current status, relevant decisions, constraints, and unresolved items.
6. State the next required action and exact expected output.
7. Include enough provenance and retained state for the receiver to proceed without reconstructing a prior conversation.
8. Contain no unresolved placeholder, unselected destination, opaque Library identifier, runtime-selection advice, workload rating, model recommendation, or configuration gate.

For a conditional route, the producer selects and populates only the branch qualified by the completed result. A blocked continuation names the missing fact, owner, retained state, and smallest permitted recovery. A terminal result states completion and the native return owner in prose and contains no `NEXT_PROMPT_HANDOFF` block.

## Canonical PF sources

PFCanon authority is available only through controlled Markdown in `Glow / Core Docs / PFCanon`.

- Never open, fetch, inspect, cite as authority, or use a Google Docs, DOC, or DOCX representation of a PFCanon file.
- There is no non-Markdown fallback. A missing, ambiguous, inaccessible, or incomplete controlled Markdown source is a source blocker.
- Do not follow a native-document PF10 link embedded in an RCA or historical artifact. Resolve the current PF10 Markdown independently through the controlled source record.
- Record exact filename, version or identity, direct Drive URL, observed status, applicability, and a digest when the workflow requires one.
- A historical file, mirror, rejected artifact, title match, or more recently modified native document cannot supersede the controlled Markdown source.

## Runtime artifact storage

All GCFPE runtime planning files and off-repository planning artifacts must be stored as efficient, machine-readable Markdown in [Glow / Ephemeral Planning Files](https://drive.google.com/drive/folders/1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc).

The producing session must:

- use a clear stable filename containing the change/work-unit identity, artifact type, and version;
- preserve structured headings, exact identifiers, decisions, status, dependencies, evidence links, unresolved items, and next action;
- upload the complete artifact and fetch it back before claiming success or citing it;
- return the actual direct Drive link and pass that link in every dependent handoff;
- use local scratch only for active working state; and
- never substitute a ChatGPT Library artifact or identifier or require a later session to recover an important artifact from conversation memory.

Reusable prompt bodies remain in Notion. Repository-controlled deliverables remain in their authorized repositories. This section governs runtime planning artifacts and off-repository evidence, not source-code storage.

## Approved bases and PF10 overlays

An approved Plan, Guide, or Specification remains the immutable in-flight base. A material discovery, approved rescope, approved escalation/remediation, or material whole-plan change is never implemented by silently rewriting or replacing that base.

Every qualifying approval produces exactly one standalone Markdown artifact whose `artifact_type` is `PF10_BUILD_NOTES_ADDENDUM`. The addendum is authoritative for its explicit scope only after Nathan has manually drained it into the current controlled PF10 Markdown. It overlays the approved base and does not replace the base or its original approval lineage. The buck stops at PF10.

Every prompt that creates or revises a Plan, Guide, or Specification must resolve and cross-reference:

- the exact current PF10 Markdown filename, identity/version, and direct Drive URL;
- every applicable active PF10 addendum;
- the approved or proposed base artifact separately from overlays; and
- the applicability and scope of each overlay.

No prompt may re-author an approved base during implementation. Initial preapproval drafting and bounded redline correction remain permitted in their native lanes before approval. Once a base is approved, a material change follows the addendum process in this procedure.

## PF10 build-notes addendum contract

A prompt that itself records a qualifying approval must create the addendum separately from its decision artifact and its handoff. For `GCFPE-20260913.1`, the semantic producer set is:

| Producer | Qualifying outcome |
|---|---|
| CF-C-30 | `DELTA_APPROVE` records a material in-flight change to an already approved CRD Specification |
| CF-E-30 | `DELTA_APPROVE` records a material in-flight change to an already approved Epic Specification |
| IA-30 | `APPROVE` records a material in-flight delta to an already approved whole-change Implementation Plan; initial Plan approval alone does not qualify |
| QA-70 | `APPROVE` records a material in-flight delta to an already approved QA Plan; initial QA Plan approval alone does not qualify |
| RS-20 | `APPROVE` records a bounded work-unit rescope |
| ESC-40 | `APPROVE` records an escalation/remediation or material in-flight delta to an approved Plan, Guide, or Specification |

The addendum must contain:

- `artifact_type: PF10_BUILD_NOTES_ADDENDUM`;
- `status: READY_FOR_MANUAL_DRAIN`;
- `canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN`;
- `drain_owner: Nathan / Product Owner`;
- change and work-unit identifiers;
- producing prompt name, version, and direct Notion URL;
- approval decision and direct evidence link;
- immutable approved base identity and approval lineage;
- exact approved overlay delta;
- affected requirements, dependencies, tests, Ops, documentation, and downstream work;
- Canon conflicts, exclusions, and unresolved items; and
- its own filename, version, and direct Drive link after upload/readback.

The producing prompt does not edit PF10, allocate PF10 numbering, insert the addendum, declare canonical adoption, or resume implementation. Nathan's manual drain and verification against the current PF10 Markdown is the canonicalization boundary. Proposal, redline, revision-required, denial, rejection, pending, unchanged, editorial, and nonqualifying initial-approval outcomes emit no addendum. Never emit an empty addendum.

## Existing-work recovery

Before a prompt creates a new workspace, checkout, worktree, branch, commit, pull request, or duplicate planning artifact, it must inspect the authorized local roots, repository state, pull-request state, and linked Drive artifacts for work matching the change and work-unit identifiers.

When one consistent prior state exists, verify its identity, provenance, and status and resume the most advanced valid state. When several plausible states conflict, stop only the affected action, report the candidates and evidence, and request the smallest necessary decision. Do not recreate completed work, overwrite an existing workspace, discard a branch or open PR, force rework because an earlier conversation ended, or invent a session-inspection endpoint or unsupported platform limitation.

## PR-development execution

GCFPE PR-30 uses `glow-hde-pr-development` as the primary workflow skill. `glow-hde-devops` is support-only for bounded environment or Ops operations and does not control PR recovery, workflow policy, rescope, review/CI ordering, escalation, or merge readiness.

A Product Owner `Proceed` authorizes PR-30 to complete the approved work unit through verified merge readiness. It does not authorize the agent to merge. The execution contract is:

- recover existing work before creating new work;
- run relevant local tests before a meaningful commit or push;
- group coherent, locally tested changes into meaningful checkpoints;
- push purposefully rather than after every small edit or never pushing at all;
- permit an early draft PR only after a locally tested coherent checkpoint;
- use an authenticated GitHub connector for supported operations when available; absence of a local `gh` binary is not a blocker when that connector can perform the operation;
- retrieve and address actionable review findings before waiting on, retriggering, or spending more paid CI;
- do not consume stale CI while material review issues remain; cancel a stale run only when an available authorized interface supports cancellation;
- after review fixes, rerun local tests, create one coherent checkpoint, push the corrected candidate once, and then obtain current-head review and CI evidence;
- continue until required reviews are resolved, required CI passes on the current head, mergeability is verified, and the PR is genuinely ready for the Product Owner's manual merge; and
- never merge without separate, direct, PR-specific Product Owner authority.

The action-economy rule protects remote cost without skipping required commits, pushes, reviews, CI, or merge-readiness verification.

## Bounded PR rescope

When PR-30 proves a bounded blocker outside approved scope, it stops the affected action, preserves the existing PR vehicle and valid completed work, and produces one formal rescope request. It does not approve its own request, rewrite a Plan, invoke abort, create a replacement session/workspace/worktree/branch/PR/Instruction/Proceed, or rerun an accepted PR.

The normal route is:

`PR implementation boundary → formal rescope request → same IA decision through RS-20 → qualifying approval emits one PF10 addendum → Nathan manually drains and verifies the addendum in current PF10 Markdown → RS-40 resumes the same PR vehicle under the original Proceed`

PR-30 itself uploads and reads back the complete formal request, then hands it directly to the selected RS-20 in the same whole-change IA context. RS-20 decides the request against the same work unit, immutable approved base Plan, current controlled PF10 Markdown and applicable active addenda, original Proceed, and preserved PR evidence. RS-10 remains a separate, nonredundant proposal-support surface for other valid native inputs or pre-review proposal preparation when explicitly invoked; it is not a mandatory normal in-flight stage, restart, or extra approval. RS-30 owns reviewer-requested bounded redline of a submitted request.

RS-20 has these outcomes:

- `APPROVE`: create the decision artifact and exactly one addendum, then emit one populated conditional post-drain invocation. An existing-open-PR implementation uses selected RS-40 in the same preserved vehicle/original Proceed. Planning, prepublication, Ops, documentation and merged-but-not-accepted findings return to the actual native correction/delivery/evidence owner with only existing inputs and unchanged authority. Nathan drains and verifies before any affected work relies on the delta; never fabricate a PR or Proceed to force RS-40.
- `REJECT`: create no addendum and rewrite no base. Return to the actual native owner (same PR under original Proceed where applicable) only when the complete native intake and unchanged authority permit it; otherwise return terminally to Nathan with preserved evidence and no continuation.
- `REVISION_REQUIRED`: create no addendum and return the actual request/proposal to its same author through RS-30, retaining artifact type and application evidence. An IA redline returns to that same IA; a genuine Product Owner correction returns to Nathan without an invented IA denial. No approved base is rewritten.
- `SPECIFICATION_CHANGE_REQUIRED`: RS-20 emits no addendum and returns the genuine product decision terminally to Nathan. The applicable Specification author/reviewer uses its bounded delta lane only under the actual Product Owner decision; it never rewrites the approved Specification.
- `IN_SCOPE_REPAIR`: create no addendum; return to the actual existing repair/evidence owner under unchanged authority, preserving a PR vehicle where one exists.

Approved rescope never routes through IA-30 or IA-40, never creates a successor whole-change Plan, and never requires a second Proceed. IA-40 remains limited to initial preapproval Plan creation or redline revision.

## RS-40 post-drain continuation

`RS-40 — Approved Rescope — Resume PR Implementation — 091326.2` is designated as the dedicated post-drain continuation prompt. Its versioned Notion page is [here](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204); the page remains non-operational until the release register selects the complete 091326.2 successor.

Before resumption, RS-40 must read the exact current PF10 Markdown and verify:

- the approved addendum is actually drained, active, applicable to the exact change/work unit, and unchanged from the approval decision;
- the approved base Plan and its approval lineage remain the base;
- the original Product Owner Proceed remains the execution authority;
- the same PR session, workspace/worktree, branch, commits, open PR, artifacts, and accepted dependencies are retained; and
- no later applicable addendum conflicts with or supersedes continuation.

Only after all checks pass does RS-40 resume the same PR implementation itself under the original Proceed and primary `glow-hde-pr-development` skill. It does not add a PR-30 invocation. A failed or ambiguous drain/source/owner/recovery check returns terminally to Nathan with preserved evidence and no continuation; it does not accept, close, abort, recreate or rewrite the work.

## Manual abort and escalation

`PR-50 — Abort PR and Escalate — 091326.2` is designated as a manual Product Owner control. Its versioned Notion page is [here](https://app.notion.com/p/3da4590a05eb813bb505eea620942e30?pvs=204); the page remains non-operational until the release register selects the complete 091326.2 successor.

Only Nathan / Product Owner may invoke PR-50 directly for an exact PR and work unit. No agent, PR, IA, RS, QA, skill, automation, hub, prompt, or handoff may invoke, select, or route to PR-50. An unrecoverable or repeatedly failing PR returns complete evidence and Product Owner control; it does not decide to abort and does not emit a PR-50 handoff.

When Nathan directly invokes PR-50, it preserves the workspace/worktree, branch, commits, open PR, current head, review/CI evidence, rescope lineage, accepted dependencies, completed unaffected work, and linked artifacts. It does not delete, reset, rebase, force-push, close, merge, discard, or drain PF10. It returns the preserved evidence and abort/escalation record terminally to Nathan. It selects or invokes no next prompt. A later substantive escalation requires Nathan’s actual separate native invocation.

## Escalation, remediation, and material discovery

ESC-30 proposes a bounded remediation or escalation. ESC-40 decides it. An ESC-40 qualifying approval follows the same one-addendum and manual-drain boundary. Denial or correction returns to the same Thoth through ESC-30, not to IA-30 or IA-40.

An approved remediation or material whole-plan discovery carries the original approved base and approval identity plus a separate remediation decision and applicable PF10 addendum overlay. A remediation approval never substitutes for the base Plan's original `PLAN_REVIEW_ID`. Product-intent changes use the selected Specification-delta lane. No approved escalation, remediation, or discovery authorizes live whole-plan reauthoring.

## Validation before selection

Read every candidate prompt completely and check immediate producers, receivers, controls, skills, and artifacts. Confirm that:

- the candidate contains exactly 54 unique selected-set members at version `091326.2` if promoted;
- every destination resolves to an exact member of that candidate set;
- each nonterminal result emits exactly one populated paste-ready handoff and each terminal result emits none;
- versions, identifiers, actors, sessions, approvals, constraints, and artifact lineage agree;
- the PR-to-IA-to-addendum-to-manual-drain-to-same-PR continuation route is closed;
- no active RS-20/RS-10 restart, replacement-Plan, or IA-30/IA-40 rescope route remains;
- PR-50 has zero automatic inbound edges and only direct Product Owner invocation;
- every semantic qualifying approval producer implements the addendum contract and no nonqualifying outcome emits one;
- every Plan/Guide/Specification writer cross-references current PF10 Markdown and applicable addenda;
- PFCanon use is Markdown-only and runtime artifacts are Drive Markdown with direct links rather than Library identifiers;
- PR-30 and its primary/support skills contain recovery, local-first testing, coherent checkpoints, review-first CI economy, current-head evidence, and merge-ready controls;
- the PE metaprompt cannot regenerate the corrected defects;
- the GCFPE-specific Flowmaster overlay and validators align without modifying the protected Flowmaster Primary core or immutable R1 oracle;
- all six required scenarios pass; and
- no active model/strength assessment, Analyzer routing, reasoning recommendation, eligibility/suitability/account check, or configuration-based workflow gate exists.

Record every issue with source, exact defect, correction, and readback result. Recheck every changed source before selection. Structural validation does not prove a live execution; record that distinction plainly.

## Promotion, archive, and Alpha resume

Keep `GCFPE-20260912.2` selected and active while `GCFPE-20260913.1` is incomplete. Select the successor only after its exact catalog, register entry, hubs, procedure, PE metaprompt, skills, prompt bodies, handoffs, graph, source policy, fixtures, and validation evidence reconcile.

After selection, read back every activated control and prompt and rerun independent validation against the selected successor. Archive superseded prompt and control versions intact only after that post-promotion audit passes. Never delete, overwrite, reset, or improvise an archive. Historical pages remain provenance and cannot be active routing targets.

HDE-EPIC040 Alpha remains `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION` until the successfully read-back promotion report explicitly declares `READY_FOR_MANUAL_ALPHA_RESUMPTION`. Nathan alone manually invokes the one final RS-20 handoff. This maintenance procedure does not invoke RS-20, drain PF10, resume Alpha, run repository work, or modify PR #404.

## Native receiver compatibility and final-history protection

RS-10/20 retain bounded planning, prepublication, Ops, documentation and merged-but-not-accepted finding intake. A return goes to the stage actually needed for the remaining correction/evidence, not blindly back to the discovery stage. No future detailed Plan, PR result, open PR or Proceed becomes a retrospective prerequisite. An initial pending PR-20 Plan retains the first Product Owner Proceed boundary; proceeded work retains its original Proceed.

ESC-40 REMEDIATION_REVIEW is distinct from RS-20 RESCOPE_REVIEW. Already authorized active-PR remedy delivery uses PR-30 with its original Proceed, immutable base, exact REMEDIATION_REVIEW and verified drained overlay. It does not enter RS-40 without an actual RS-20 rescope decision and must not create duplicate approvals/addenda to bridge inputs.

An accepted-final PR remains final and is never reimplemented or re-reviewed for later governance, drift or discoveries. A merged-but-not-accepted PR may have a bounded pending review/correction route with actual evidence; merged state is not a fabricated open implementation vehicle.

A missing source, owner, manual drain, suitable authority/vehicle or unrecoverable workspace returns terminally to Nathan for that invocation and emits no continuation. This is neither work closure nor an abort decision. Every actionable nonterminal result has exactly one complete selected-prompt invocation, with any drain/merge prerequisite explicit.
