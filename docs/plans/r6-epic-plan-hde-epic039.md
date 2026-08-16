# HDE-EPIC039 — Calcination Pass 6

## Meta

Epic ID: HDE-EPIC039
Epic name: Calcination Pass 6
Alchemical phase: Calcination
Status: Planned
Version: r6
Date started: 2026-08-13
Date completed: Not completed; no closeout claim is made
Repository consult: amthorn78/glow-hdengine-v2, main at commit 9c068b0a69971d734747039c0ff0a30d59994b84
Approval sentinel: ASK OK?

Phase rationale: This epic burns away obsolete epic-specific closeout machinery and consolidates the remaining foundational rules for canonical bytes, evidence parity, QA harness integrity, and terminal closeout reachability. It preserves essential shared primitives while avoiding work owned by later alchemical phases.

## PF Canon Applicability Snapshot

PF01-Canon-HDE-Math-Spec — Not applicable
PF02-Canon-HDE-Architecture — Applied — Effect: Preserves component ownership, offline evidence boundaries, and single-home architecture.
PF03-Reference-Technical-Writing-Best-Practices — Applied — Effect: Governs paste-ready structure, title-safe references, and source-grounded wording.
PF04-Canon-HDE-Governance — Applied — Effect: Governs tokens, evidence parity, canonical gates, and nonclaim posture.
PF05-Canon-HDE-CLI-API-Vendor-Ref — Applied — Effect: Governs supported tool invocation and canonical byte-facing surfaces.
PF06-Canon-Epic-Process-Guide — Applied — Effect: Governs PR-first delivery, workflow separation, and feedback-free terminal reachability.
PF07-Canon-Glow-Infrastructure — Not applicable
THE HUMAN DESIGN SYSTEM — Not applicable
PF09.1-Canon-HDE-Build-Checklist-Calcination — Applied — Effect: Supplies the exact subtasks, order, and recorded completion statuses.
PF09.2-Canon-HDE-Build-Checklist-Dissolution — Not applicable
PF09.3-Canon-HDE-Build-Checklist — Not applicable
PF09.4-Canon-HDE-Build-Checklist-Conjunction — Not applicable
PF09.5-Canon-HDE-Build-Checklist-Fermentation — Not applicable
PF09.6-Canon-HDE-Build-Checklist-Distillation — Not applicable
PF09.7-Canon-HDE-Build-Checklist-Coagulation — Not applicable
PF10-HDE-Build-Notes — Applied — Effect: Addendum 2.1 Block reviewer-invented technical design; addendum 2.2 Require materiality for approval blockers; addendum 2.3 Keep CI tied to continuing product and delivery risk, not epic administration.
RAVE I CHING — Not applicable
PF12-Canon-HDE-Schemas-and-Artifacts — Applied — Effect: Governs canonical serialization, evidence families, path proofs, ledgers, and the acyclic attestation lifecycle.
PF13-Reference-Glow Development Philosophy v1 — Reference-only context
PF14-Canon-HDE-Mechanics-Guide — Applied — Effect: Supplies the exact mechanics and component references for every executable work item.
Glow Tonality Guide v1.1: Writing for Human Connection — Not applicable
PF16‑Canon — HD Engine Epics Map — Historical-only
PF17-Canon-HDE-Narratives-Guide — Not applicable
PF18‑Reference‑HDE‑Narrative Deliverables — Not applicable
PF19-Canon-Glow-QA-Guide — Applied — Effect: Governs QA readiness, harness status semantics, tooling-versus-behavior classification, and QA/OPS separation.
PF20-Reference-HDE-Phased Epics — Historical-only
7 Phases of Alchemical Engineering — Applied — Effect: Establishes Calcination as the correct mode for removing obsolete machinery and consolidating essentials.
PF23-Canon-Reality-Audits — Reference-only context
PF27-Canon-Plan-Templates — Applied — Effect: Governs this Epic Plan’s structure and approval preflight.
PF29-Canon-HDE-Users-Guide — Not applicable

Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Business Case

### Objective

Complete the remaining coherent Calcination foundation work in one epic by:

* consolidating canonical JSON and arrays-as-sets behavior;
* making Evidence Index, Machine Mirror, orientation, and path-proof updates operate as one deterministic discipline;
* hardening reusable QA invocation, logging, status, and acceptance-map viability behavior;
* removing the withdrawn HDE-EPIC038-specific closeout subsystem and its CI cost;
* classifying every current CI trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior under PF10 addendum 2.3;

* removing, narrowing, separating, or relocating controls according to their continuing-risk justification and correct lane;
* replacing that subsystem with an epic-agnostic, feedback-free terminal lifecycle.

### Problem

Nine Calcination subtasks remain open with statuses of Consolidation pending, Partial, or Not done. Current repository tooling contains useful foundations, but they remain split between partially generalized mechanisms, legacy artifact-family posture, a QA harness that retains prohibited run identity, and an HDE-EPIC038-specific closeout lifecycle whose receipt feedback made ordinary terminal completion unreachable.

### Who experiences the problem

The direct impact is on engineering, QA, and Product Owner closeout work. Inconsistent canonicalization, evidence parity drift, phantom viability passes, and receipt-driven source mutation make results harder to trust and make delivery more expensive. No new user-facing Human Design capability is required.

### Why this epic now

These tasks share one Calcination purpose: remove what is obsolete, expose false assurances, and retain only deterministic, reusable foundations. Planning them together prevents a new generic closeout lifecycle from being built on unresolved canonicalization, indexing, or harness defects.

### Measurable outcome

The epic succeeds when:

* all nine mapped PF09.1 subtasks have implementation and governed proof sufficient to support completion in this epic as a plan-local intended outcome, without moving PF09 status;
* canonical JSON and schema-declared set arrays fail closed on noncanonical or ambiguous input;
* evidence writers and checkers reach a stable fixed point without hosted-CI repair;
* current reusable QA tooling distinguishes behavior, tooling, and prerequisite failures and cannot report a phantom PASS;
* the HDE-EPIC038-specific DEV-01/DEV-02 closeout generator, validators, focused tests, private-receipt handling, authenticated receipt-consumption path, network-enabled generation lane, and CI bindings created only for the withdrawn r5 lifecycle are removed without deleting shared primitives or historical evidence;
* every current CI trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior is classified under PF10 addendum 2.3; administrative closeout controls are removed or relocated; independently justified product and delivery protection is preserved or narrowed; triggers, job conditions, and the job-dependency graph are corrected; and no tracked-source writeback, hosted-receipt feedback loop, or closeout-only merge gate remains;
* an epic-agnostic closeout candidate can be fully generated from repository-local inputs before hosted validation and validated without source writeback.

## Scope Boundary

### In scope

1. Canonical JSON and arrays-as-sets consolidation.
2. Evidence Index, Machine Mirror, orientation, hash, path-proof, and CI parity discipline.
3. Canonical pytest invocation and generic QA harness viability hardening.
4. Complete current CI workflow classification and remediation under PF10 addendum 2.3, including the HDE-EPIC038 closeout subsystem and every other trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior.
5. Preserve or narrow independently justified product and delivery protection; remove, separate, relocate, or repair controls that fail the continuing-risk or lane-placement tests.
6. Feedback-free generic closeout lifecycle reachability in epic closeout automation.

All nine identified Calcination subtasks are included exactly once. No identified task is deferred or assigned to another epic.

### Out of scope

* Human Design calculations, Gate or Line meanings, chart mechanics, scoring, bands, narratives, and public copy.
* New product features, public routes, endpoints, flags, or payload contracts.
* Vendor, database, deployment, migration, or infrastructure work.
* Domain-specific evidence-family expansion owned by later phases.
* QA execution, Live QA procedures, or a QA PASS determination.
* OPS execution.
* PF-document edits, PF09 status movement, board movement, token satisfaction, acceptance, or epic closeout.
* Reopening or retroactively closing HDE-EPIC038.
* Rewriting or deleting accurate historical evidence.

### Phase fit

Calcination is the correct phase because the work removes obsolete assumptions and machinery, proves where current foundations are incomplete, and leaves a smaller set of deterministic essentials. Later-phase feature refinement, operational expansion, and release admission remain outside this epic.

## Contract and Compatibility Posture

Public compatibility posture: No user-facing contract change is planned.

Internal compatibility posture: Repository tooling and CI contracts will change where current behavior is obsolete, ambiguous, or non-conforming.

Preservation rules:

* Preserve history. Preserve generic evidence writers, path-proof mechanics, and reusable QA primitives only where each retained control independently protects current product or delivery integrity in its correct lane. Evaluate release-attestation and sanity-pipeline behavior against actual release, security, or deployment consumers rather than preserving or deleting it by name.
* Preserve ordered arrays unless their owning schema explicitly declares set semantics.
* Preserve all Human Design meaning and mechanics.
* Preserve HDE-EPIC038 implementation history, QA history, failure evidence, and formal-closeout nonclaims.
* Do not preserve an active compatibility layer for the withdrawn HDE-EPIC038 receipt-feedback lifecycle.

Rails posture: Implementation and CI verification remain closed-rails and deterministic. The obsolete network-enabled closeout generation lane is removed rather than generalized.

Migration posture: No runtime data migration or OPS migration is included.

## Existing Work Check

The following current loci were verified on main at commit 9c068b0a69971d734747039c0ff0a30d59994b84.

Existing: `tools/evidence/run_canonical_json_gate.py` — Support: scoped repo inspection — exact-file fetch and bounded canonical-gate review.
Existing: `tools/evidence/generate_arrays_as_sets_report.py` — Support: scoped repo inspection — exact-file fetch and producer/test linkage review.
Existing: `tools/evidence/update_evidence_index.py` — Support: scoped repo inspection — exact-file fetch and writer/check-mode symbol review.
Existing: `tools/evidence/orientation_demo.py` — Support: scoped repo inspection — exact-file fetch and current CI-binding review.
Existing: `ci/checks/check_mirror_schema.sh` — Support: scoped repo inspection — exact-file fetch confirming the retained Python entrypoint.
Existing: `tools/qa/qa_harness.py` — Support: scoped repo inspection — exact-file fetch confirming generic harness and run-identity behavior.
Existing: `tools/evidence/generate_hde_epic038_closeout.py` — Support: scoped repo inspection — exact-file fetch confirming epic-specific closeout, receipt, and network behavior.
Existing: `tests/evidence/test_hde_epic038_closeout.py` — Support: scoped repo inspection — exact-file fetch confirming focused subsystem coverage.
Existing: `.github/workflows/ci.yml` — Support: scoped repo inspection — exact-file review of closeout generation, receipt, test, and evidence bindings.
Existing: `tools/evidence/build_release_attestation.py` — Support: scoped repo inspection — exact-file fetch confirming the generic external-attestation primitive.
Existing: `tools/evidence/run_sanity_pipeline.py` — Support: scoped repo inspection — exact-file fetch confirming the file identifies itself as the HDE-EPIC038 closed-rails release-sanity chain and sets `PIPELINE_ID` to `HDE-EPIC038-PR06-release-sanity`; it is not preclassified as a generic primitive.
Existing: `tools/evidence/run_sanity_pipeline_gate.py` — Support: scoped repo inspection — exact-file fetch confirming an HDE-EPIC038 sanity-pipeline validator that invokes `tools/evidence/run_sanity_pipeline.py`.
Existing: `tests/evidence/test_hde_epic038_release_sanity.py` — Support: scoped repo inspection — exact-file fetch confirming focused coverage for the HDE-EPIC038-bound sanity pipeline.
Existing: `tools/evidence/check_hde_epic038_qa_current_state.py` — Support: scoped repo inspection — exact-file fetch confirming an HDE-EPIC038 QA current-state validator.
Existing: `tests/evidence/test_hde_epic038_qa_current_state.py` — Support: scoped repo inspection — exact-file fetch confirming focused coverage for that validator.

The current canonical gate produces both the authoritative canonical-gate family and a still-produced supplemental legacy family. Current PF12 and PF04 require coherent refresh of both while both remain produced.

The current generic QA harness contains run-identity behavior that must be removed from current-state correctness.

A bounded exact-name and symbol search across current main for `generate_hde_epic038_closeout`, `test_hde_epic038_closeout`, `EPIC038_CLOSEOUT`, and `hde_epic038_closeout`, followed by review of CI and evidence-updater bindings, found hits limited to the epic-specific generator and test, active CI and updater bindings addressed by this epic, historical HDE-EPIC038 records, and PF09.1. No additional active repository consumer appeared within that bounded scope. The removal work must repeat this proof against its execution ref before deletion.

PF23 was used only as planning-time component context. All material current repository claims above were verified directly.

Existing tokens validated: None are reused without re-proof by this epic.
Existing evidence located: See the exact existing evidence paths under `Tokens and Evidence — Acceptance`.

## Delivery Strategy and Sequence

The epic uses five PR-capable implementation slices:

1. D1 consolidates canonical JSON and arrays-as-sets behavior.
2. D2 establishes atomic evidence-ledger and parity discipline on the consolidated byte posture.
3. D3 hardens active pytest callers and the reusable QA harness against tooling confusion, run identity, empty output, and phantom viability.
4. D4 inspects and remediates the complete current CI workflow at the execution ref under PF10 addendum 2.3, including the HDE-EPIC038-specific subsystem, after recording a current-ref classification for every trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior.
5. D5 implements the generic feedback-free lifecycle after D4 and validates terminal reachability against the foundations delivered by D1 through D3.

D4 must complete before D5. Required PR CI, release or security automation, QA or audit automation, and epic closeout automation remain separated; all hosted validation remains non-writing and each required check requires a continuing-risk justification.

## Deliverables — Jobs To Be Done

### D1 — Canonical serialization and set-array consolidation

Primary disposition: A — Executable work item

Job: Make one current, repository-wide Calcination implementation of canonical governed JSON and schema-declared arrays-as-sets, without changing Human Design meaning or ordered-array semantics.

Includes: - HDE-CALC002.2; HDE-CALC002.3
PF14: §4 Canonical Serialization Package; §5 Deterministic Tie-Break & Total-Order Module
PF09 disposition: in the current epic with exact phased PF09 task or subtask mapping

Required outcomes:

* Governed JSON uses the current PF12 canonical byte contract: UTF-8 without BOM, ASCII-sorted object keys, compact separators, schema-valid values, and exactly one trailing LF.
* Arrays are treated as sets only where the owning schema declares set semantics and supplies an identity rule.
* Duplicate byte-identical set members collapse deterministically; conflicting duplicate identities fail closed.
* Set ordering uses strict ASCII identity order without locale transformation.
* The canonical gate inventories every current governed target in its Calcination scope and fails when a target is omitted or noncanonical.
* The authoritative and still-produced supplemental canonical-gate families remain coherent until the supplemental family is intentionally retired under its owning authority.
* The arrays-as-sets report is deterministic, mechanically produced, checkable, and covered by positive and fail-closed regression behavior.
* No Gate, Channel, Line, Profile, Authority, BodyGraph, score, band, or narrative meaning changes.

Token posture: Use only current PF04-registered canonical-gate tokens.

### D2 — Evidence-ledger parity and touch discipline

Primary disposition: A — Executable work item

Job: Make evidence updates atomic and convergent across the Human Evidence Index, hash sentinel, Machine Mirror, path proofs, and topology orientation.

Includes: - HDE-CALC003.10; HDE-CALC003.11
PF14: §1.3 Evidence & CI coupling; §1.3.1 Evidence jobs (single-writer tools); §1.3.2 Evidence change workflow
PF09 disposition: in the current epic with exact phased PF09 task or subtask mapping

Required outcomes:

* The canonical evidence updater remains the single writer for ledger, mirror, sentinel, and required proof bindings.
* Any authorized write pass is followed by non-writing fixed-point validation against the final bytes.
* Orientation is refreshed only after the final ledger state and then validated without repair.
* Each D2 evidence or parity control is classified under PF10 addendum 2.3. A control remains required PR CI only when it has an independent continuing-risk justification; otherwise it must not be required PR CI and is removed, narrowed, separated, or relocated to the correct lane. All retained hosted validation remains non-writing.
* The retained mirror-schema entrypoint follows the current PF04 and PF05 interpreter posture; obsolete operand assumptions are removed from active callers.
* The Machine Mirror self-record matches the complete final mirror bytes.
* Governed additions and removals update every required ledger and proof companion in the same change.
* Historical evidence remains historical; current parity work does not refresh frozen historical artifacts as current proof.
* Domain-specific work owned by later phases is not imported into Calcination.

Intended implementation tokens:

* EVIDENCE_INDEX_UPDATED_OK
* EVIDENCE_INDEX_MIRROR_OK
* EVIDENCE_INDEX_HASH_OK
* MACHINE_MIRROR_UPDATED_OK
* EVIDENCE_PATHS_VALIDATED_OK
* EVIDENCE_PATH_PROOFS_OK
* CI_CHECK_MIRROR_SCHEMA_OK
* CI_CHECK_FINAL_LF_OK

### D3 — Reusable QA invocation and viability hardening

Primary disposition: A — Executable work item

Job: Make active QA and CI tooling runnable, current-state based, and incapable of translating tooling defects or missing prerequisites into behavior failures or phantom success.

Includes: - HDE-CALC003.13; HDE-CALC003.14; HDE-CALC003.15
PF14: §1.6.1 QA tooling bootstrap harness (PRE-step component); §1.6.2 Live QA harness (commands, classification, and logs); §1.6.3 Generic epic QA harness entrypoint (per-check primary logs, manifest, viability)
PF09 disposition: in the current epic with exact phased PF09 task or subtask mapping

Required outcomes:

* Active executable CI, reusable QA harnesses, and current QA tooling invoke pytest through the active Python interpreter rather than a bare wrapper.
* Historical transcripts and archived QA records are preserved rather than rewritten.
* Generic harness correctness uses stable epic and check identities without `run_id`, operator-selected run roots, timestamped correctness paths, or per-run nesting.
* Current PF27 and PF19 status semantics govern: PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, or PARKED.
* Missing dependencies or required inputs produce tooling or prerequisite classifications, not behavior verdicts.
* Acceptance-map token identity is derived from the governed token-name field and checked against current governance.
* Missing token-set material returns deterministic TOOLING_BLOCKED behavior instead of an uncaught exception.
* Invalid or broken references cannot produce a viability PASS.
* A successful viability result proves that required references resolve and that the generic harness can load and evaluate the map.
* Empty, absent, or partially written required outputs fail closed.
* Generic harness regression coverage proves both successful production and decisive failure behavior.
* This deliverable implements shared tooling; it does not execute Live QA or determine QA PASS.

Intended implementation and QA-readiness tokens:

* QA_HARNESS_DISCIPLINE_OK
* QA_HARNESS_ENTRYPOINT_SELFTEST_OK

### D4 — HDE-EPIC038 closeout subsystem removal

Primary disposition: A — Executable work item

Job: Inspect and remediate the complete current CI workflow under PF10 addendum 2.3, including removal of the withdrawn HDE-EPIC038-specific closeout implementation and active CI cost, while preserving or narrowing independently justified product and delivery protection.

Includes: - HDE-CALC003.21
PF14: §1.3.1 Evidence jobs (single-writer tools); §27.4 Tracked evidence boundary and rollback; §27.5 Sanity pipeline (release & provenance)
PF09 disposition: in the current epic with exact phased PF09 task or subtask mapping

Ordered prerequisite:

* Resolved matter: At `26e41934be7197be98cbfa0891618db439a9a380`, a current consumer exists beyond the HDE-EPIC038-specific closeout layer: `tools/evidence/build_release_attestation.py` invokes `tools/evidence/run_sanity_pipeline_gate.py`, which invokes `tools/evidence/run_sanity_pipeline.py`. PF12-Canon-HDE-Schemas-and-Artifacts and PF14-Canon-HDE-Mechanics-Guide retain the runner and gate. The required execution-ref proof must repeat this classification before deletion.
* Controlling authority: PF09.1-Canon-HDE-Build-Checklist-Calcination, PF06-Canon-Epic-Process-Guide, and PF14-Canon-HDE-Mechanics-Guide.
* Required proof: Before any deletion or retention decision, D4’s assigned executor records a complete execution-ref classification of every current CI trigger, job, step, `needs` edge, artifact transfer, and source-writing behavior. The classification includes the exact-symbol and consumer inspection in this section and answers all ten PF10 addendum 2.3 Required decision test questions for each control.
* Affected work: Complete current CI remediation under PF10 addendum 2.3, including the HDE-EPIC038-specific DEV-01/DEV-02 closeout generator, validators, focused tests, private-receipt handling, authenticated receipt-consumption path, network-enabled generation lane, other epic-specific evidence or closeout controls, triggers, job conditions, dependencies, artifact transfers, and source-writing behavior.
* Continuation rule: Preserve or narrow controls that independently protect current product or delivery integrity; remove, separate, relocate, or repair controls that fail the continuing-risk or lane-placement tests. If classification cannot establish a safe disposition, D4 fails closed and D5 does not start. No Epic Plan edit or reapproval is required.

Required outcomes:

* The HDE-EPIC038-specific DEV-01/DEV-02 closeout layer is absent from active code: the generator, validators, and focused tests created only for the withdrawn r5 lifecycle are removed.
* Private-receipt production, authenticated receipt consumption, network-enabled closeout generation, and their active CI bindings are absent.
* Active evidence-updater bindings owned only by the withdrawn closeout layer are removed.
* Release-attestation and sanity-pipeline behavior are evaluated against actual release, security, or deployment consumers. Any retained permanent CI control preserves or narrows independently justified product or delivery protection and removes historical epic identity and administrative assertions; controls without continuing-risk justification are removed, separated, or relocated.
* HDE-EPIC038 implementation evidence, QA evidence, failure evidence, and formal-closeout nonclaims remain intact.
* No result from this work is represented as retroactive HDE-EPIC038 completion.
* No new acceptance token is created.

Token posture: No token is invented. Removal, preservation, consumer classification, and CI-cost elimination are plain governed obligations.

### D5 — Feedback-free generic closeout lifecycle

Primary disposition: A — Executable work item

Job: Establish one generic closeout candidate lifecycle whose terminal state is reachable without a hosted-CI receipt being written back into tracked source.

Includes: - HDE-CALC003.22
PF14: §27 Release and Provenance Packaging; §27.3 External release attestation; §27.5 Sanity pipeline (release & provenance)
PF09 disposition: in the current epic with exact phased PF09 task or subtask mapping

Ordered prerequisite: D4 is complete. The current PF06, PF12, and PF27 lifecycle contract is already established and governs implementation.

Proposed path: `tools/qa/generate_epic_close_pack.py`

Validation predicate: The proposal is valid only if it remains in the existing QA/tooling component home, consumes repository-local governed inputs, deterministically produces every tracked candidate byte before hosted validation, provides distinct authorized-write and non-writing check behavior, and introduces no second evidence ledger, release-identity source, runtime route, or receipt-feedback path.

Required outcomes:

* Repository-local tracked inputs determine all tracked closeout candidate bytes.
* One authorized writer owns generation for a candidate.
* Hosted validation validates the exact committed candidate without repairing or rewriting it. Epic closeout automation remains outside required PR CI unless a specific part independently qualifies for another lane under PF10 addendum 2.3.
* Current external release attestation remains external to the source it attests and cannot become a tracked identity input.
* Exact-head, clean-tree, deterministic generation, path-proof, and evidence-ledger responsibilities remain distinct and fail closed.
* A bounded end-to-end feasibility proof establishes that a candidate can reach its terminal validated state without source-to-CI-to-source feedback.
* Any dependence on a later hosted receipt, run identifier, mutable attestation, or later source commit causes deterministic failure.
* The lifecycle is epic-agnostic and does not contain HDE-EPIC038 identity or semantics.
* The mechanism does not close HDE-EPIC039, satisfy tokens, establish QA PASS, or perform Product Owner closeout.

Token posture: No closeout token is invented. Feedback-free reachability, exact-candidate validation, and non-writeback are plain obligations unless current Governance explicitly binds an existing token with semantic fit.

## PF Reference Map

### D1 authority map

Primary phase authority: PF09.1-Canon-HDE-Build-Checklist-Calcination
Architecture: PF02-Canon-HDE-Architecture
Governance: PF04-Canon-HDE-Governance
Artifact contract: PF12-Canon-HDE-Schemas-and-Artifacts
Mechanics: PF14-Canon-HDE-Mechanics-Guide
QA posture: PF19-Canon-Glow-QA-Guide

PF12 controls canonical artifact-family identity and current serialization bytes. PF09.1 controls task identity, order, and recorded status. Where older PF09 artifact notes differ from current PF12 or PF04 posture, the current owning canon controls without changing the PF09 mapping.

### D2 authority map

Primary phase authority: PF09.1-Canon-HDE-Build-Checklist-Calcination
Architecture: PF02-Canon-HDE-Architecture
Governance: PF04-Canon-HDE-Governance
Invocation contract: PF05-Canon-HDE-CLI-API-Vendor-Ref
Process: PF06-Canon-Epic-Process-Guide
Artifact contract: PF12-Canon-HDE-Schemas-and-Artifacts
Mechanics: PF14-Canon-HDE-Mechanics-Guide
QA posture: PF19-Canon-Glow-QA-Guide

### D3 authority map

Primary phase authority: PF09.1-Canon-HDE-Build-Checklist-Calcination
Governance: PF04-Canon-HDE-Governance
Process: PF06-Canon-Epic-Process-Guide
Mechanics: PF14-Canon-HDE-Mechanics-Guide
QA semantics: PF19-Canon-Glow-QA-Guide
Template and status owner: PF27-Canon-Plan-Templates
Reality consult: PF23-Canon-Reality-Audits, read-only and non-gating

Current PF27 and PF19 QA status vocabulary controls over older PF09 examples because QA vocabulary is owned in the QA and template lanes.

### D4 authority map

Primary phase authority: PF09.1-Canon-HDE-Build-Checklist-Calcination
Architecture: PF02-Canon-HDE-Architecture
Process: PF06-Canon-Epic-Process-Guide
Artifact preservation: PF12-Canon-HDE-Schemas-and-Artifacts
Mechanics: PF14-Canon-HDE-Mechanics-Guide

### D5 authority map

Primary phase authority: PF09.1-Canon-HDE-Build-Checklist-Calcination
Process and terminal reachability: PF06-Canon-Epic-Process-Guide
Artifact and attestation acyclicity: PF12-Canon-HDE-Schemas-and-Artifacts
Mechanics: PF14-Canon-HDE-Mechanics-Guide
Plan and close-candidate structure: PF27-Canon-Plan-Templates

Current PF10-HDE-Build-Notes addenda 2.1, 2.2, and 2.3 govern their exact topics; addendum 2.3 governs CI lane classification and HDE-EPIC039 remediation.

PF20-Reference-HDE-Phased Epics and PF16‑Canon — HD Engine Epics Map are historical-only and contribute no current planning requirement.

## Plan-local completion summary

### Map entry 1

Source document: PF09.1-Canon-HDE-Build-Checklist-Calcination
Source task ID: HDE-CALC002
Source subtask ID(s): HDE-CALC002.2; HDE-CALC002.3
Plan-local intended outcome: Complete in this epic
Plan work item: D1
Notes: Current recorded statuses are Consolidation pending and Consolidation pending. Neither status equals Done. This plan makes no PF09 status movement claim.

### Map entry 2

Source document: PF09.1-Canon-HDE-Build-Checklist-Calcination
Source task ID: HDE-CALC003
Source subtask ID(s): HDE-CALC003.10; HDE-CALC003.11
Plan-local intended outcome: Complete in this epic
Plan work item: D2
Notes: Both current recorded statuses are Partial. Calcination completion is limited to the reusable indexing and parity discipline and does not import later-phase domain expansion.

### Map entry 3

Source document: PF09.1-Canon-HDE-Build-Checklist-Calcination
Source task ID: HDE-CALC003
Source subtask ID(s): HDE-CALC003.13; HDE-CALC003.14; HDE-CALC003.15
Plan-local intended outcome: Complete in this epic
Plan work item: D3
Notes: All three current recorded statuses are Partial. Completion concerns active and reusable tooling; historical QA records remain unchanged.

### Map entry 4

Source document: PF09.1-Canon-HDE-Build-Checklist-Calcination
Source task ID: HDE-CALC003
Source subtask ID(s): HDE-CALC003.21
Plan-local intended outcome: Complete in this epic
Plan work item: D4
Notes: Current recorded status is Not done. Its consumer proof is an ordered execution-time predicate, and HDE-CALC003.21 precedes HDE-CALC003.22.

### Map entry 5

Source document: PF09.1-Canon-HDE-Build-Checklist-Calcination
Source task ID: HDE-CALC003
Source subtask ID(s): HDE-CALC003.22
Plan-local intended outcome: Complete in this epic
Plan work item: D5
Notes: Current recorded status is Not done. D4 must complete first. The required PF06, PF12, and PF27 lifecycle contract is present in current canon.

## PF09 Completion Map

| Work item ID | PF09 disposition                                                   | Phased PF09 document                         | Task ID     | Subtask ID     | Exact source heading                                                                      | Contribution              | Current recorded status | Status nonclaim                                  |
| :----------- | :----------------------------------------------------------------- | :------------------------------------------- | :---------- | :------------- | :---------------------------------------------------------------------------------------- | :------------------------ | :---------------------- | :----------------------------------------------- |
| D1           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC002 | HDE-CALC002.2  | Subtask HDE-CALC002.2 — Canonical JSON rules                                              | D1 advances this subtask. | Consolidation pending   | This Epic Plan does not itself move PF09 status. |
| D1           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC002 | HDE-CALC002.3  | Subtask HDE-CALC002.3 — Arrays-as-sets semantics                                          | D1 advances this subtask. | Consolidation pending   | This Epic Plan does not itself move PF09 status. |
| D2           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.10 | Subtask HDE-CALC003.10 — Indexing & parity CI gates                                       | D2 advances this subtask. | Partial                 | This Epic Plan does not itself move PF09 status. |
| D2           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.11 | Subtask HDE-CALC003.11 — Evidence index touch discipline                                  | D2 advances this subtask. | Partial                 | This Epic Plan does not itself move PF09 status. |
| D3           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.13 | Subtask HDE-CALC003.13 — Canonical pytest invocation for QA & CI                          | D3 advances this subtask. | Partial                 | This Epic Plan does not itself move PF09 status. |
| D3           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.14 | Subtask HDE-CALC003.14 — QA harness discipline (tooling vs behavior, commands, emptiness) | D3 advances this subtask. | Partial                 | This Epic Plan does not itself move PF09 status. |
| D3           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.15 | Subtask HDE-CALC003.15 — Acceptance map & QA harness viability check                      | D3 advances this subtask. | Partial                 | This Epic Plan does not itself move PF09 status. |
| D4           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.21 | Subtask HDE-CALC003.21 — HDE-EPIC038 closeout subsystem removal and CI-cost cleanup       | D4 advances this subtask. | Not done                | This Epic Plan does not itself move PF09 status. |
| D5           | in the current epic with exact phased PF09 task or subtask mapping | PF09.1-Canon-HDE-Build-Checklist-Calcination | HDE-CALC003 | HDE-CALC003.22 | Subtask HDE-CALC003.22 — Feedback-free closeout lifecycle reachability                    | D5 advances this subtask. | Not done                | This Epic Plan does not itself move PF09 status. |

## Tokens and Evidence — Acceptance

### Intended tokens

Canonical source for every intended token: PF04-Canon-HDE-Governance, §2.0 Acceptance Tokens (single-home roster) [Required-Now].
Preflight result: Every token listed below appears exactly in the current PF04 roster; this plan claims no tokens.

D1:

* CANONICAL_JSON_GATE_UPDATED_OK
* CANONICAL_JSON_GATE_PASSED_OK
* JSON_CANONICAL_CHECK_OK

D2:

* EVIDENCE_INDEX_UPDATED_OK
* EVIDENCE_INDEX_MIRROR_OK
* EVIDENCE_INDEX_HASH_OK
* MACHINE_MIRROR_UPDATED_OK
* EVIDENCE_PATHS_VALIDATED_OK
* EVIDENCE_PATH_PROOFS_OK
* CI_CHECK_MIRROR_SCHEMA_OK
* CI_CHECK_FINAL_LF_OK

D3 and separate QA-readiness or close posture:

* QA_HARNESS_DISCIPLINE_OK
* QA_HARNESS_ENTRYPOINT_SELFTEST_OK
* QA_BOOTSTRAP_OK
* QA_LIVE_QA_RUN_OK

D4 and D5 use plain obligations because PF09.1 identifies their tokens as Unknown and current Governance does not admit a dedicated subsystem-removal or feedback-free-closeout token.

### Claimed tokens

None. An Epic Plan cannot satisfy or claim acceptance tokens.

### Evidence posture

Implementation and later QA evidence must remain separated by lane. Expected proof classes are:

* deterministic canonical-gate and arrays-as-sets behavior;
* positive and fail-closed regression coverage;
* single-writer and fixed-point evidence-ledger behavior;
* Human Evidence Index, hash sentinel, Machine Mirror, and path-proof coherence;
* current-state generic harness behavior and acceptance-map viability;
* active-consumer classification and obsolete-binding removal;
* generic terminal-reachability and exact-candidate validation.

Required planning-level artifact paths are prescribed here without QA commands, step logs, operator procedures, or execution detail.

Administrative closeout artifacts do not independently authorize required PR CI. Their generation and validation remain in QA or audit automation or epic closeout automation unless a specific control independently qualifies for another lane under PF10 addendum 2.3.

Planned-new close-pack, acceptance, and doc-delta pointers for eventual epic close:

* `audit/EPIC-039_close_report.md`
* `audit/EPIC-039_close_report.md.path_proof.txt`
* `audit/EPIC-039_MANIFEST.json`
* `audit/EPIC-039_MANIFEST.json.path_proof.txt`
* `docs/acceptance_map_epic039.json`
* `docs/acceptance_map_epic039.json.path_proof.txt`
* `token_evidence_matrix.md`
* `acceptance_map_viability.log`
* `audit/docdeltas/hde-epic039_doc_deltas.md`
* `audit/docdeltas/hde-epic039_doc_deltas.md.path_proof.txt`
* `doc_deltas.md` (QA-root copy)
* `audit/docdeltas/hde-epic039_drain_targets.md`
* `audit/docdeltas/hde-epic039_drain_targets.md.path_proof.txt`
* `qa_step_logs_manifest.json`

Planned-new validation predicate: Each base artifact and required sibling path proof is generated and validated; the acceptance map and token-evidence matrix are mutually consistent; the acceptance-map viability log is produced mechanically; the two doc-delta surfaces are byte-identical; and the close-pack manifest binds declared outputs by exact repo-relative path.

Every planned-new base artifact named by a path or a titles-only pointer in this list is intended to appear in the Human Evidence Index and Machine Evidence Mirror; required sibling path-proof transcripts remain proof companions.

Existing Evidence Index, Machine Mirror, and proof-companion paths directly used by D2:

* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.json.path_proof.txt`
* `docs/evidence/INDEX.sha256`
* `docs/evidence/INDEX.sha256.path_proof.txt`
* `artifacts/evidence_index.jsonl`
* `artifacts/evidence_index.jsonl.path_proof.txt`
* `artifacts/evidence_index.jsonl.sha256`
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Existing canonical JSON gate paths directly used by D1:

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`
* `audit/gates/json_gate/canonical/json_gate_structured_record.json`
* `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`

Existing arrays-as-sets diagnostic path:

* `artifacts/canonical/arrays_as_sets_report.log`

QA commands, step logs, operator procedures, and execution detail remain in the separate QA planning and execution lane.

Evidence presence does not independently establish token satisfaction, QA PASS, PF09 status movement, acceptance, OPS completion, or closeout.

## QA Rails — Open/Close (Final PR)

QA planning required: Yes, after implementation readiness.

QA execution authorized by this plan: No.

Live QA posture: A separate PF27-conforming QA artifact must define executable checks. This Epic Plan establishes only the high-level requirement that the implemented generic harness, canonicalization, evidence parity, removal, and terminal-reachability outcomes receive appropriate validation.

Live QA is required for close.

Rails posture:

* Closed rails are the default for implementation verification and evidence tooling.
* No open-rails or network-dependent behavior is required for the planned outcome.
* The current HDE-EPIC038 network-enabled closeout lane is removed.
* External attestation remains external and non-mutating.
* Tooling and prerequisite failures remain distinct from behavior failures.

QA-readiness order:

1. D1 through D5 implementation outcomes exist.
2. Implementation-level regression and non-writing CI checks establish readiness.
3. QA planning defines the separate validation scope.
4. QA execution produces its own governed verdicts.
5. Documentation drainage and closeout remain later, separate lanes.

No QA PASS is asserted.

## Workflow-Lane Separation

Implementation: D1 through D5 only.

Required PR CI: Only controls with an independent continuing-risk justification may block merge.

Release or security automation: Controls gate only an actual release, security, deployment, or external-obligation boundary that consumes or requires them.

QA or audit automation: Deeper validation and governed result capture remain in their bounded lanes without becoming ordinary merge gates.

Epic closeout automation: Administrative closeout preparation remains isolated from required PR CI unless a specific part independently qualifies for another lane; it creates no tracked-source writeback, unrelated future-change burden, or source-to-CI-to-source feedback loop.

OPS: No OPS task is included. No deployment, migration, external service mutation, credential use, or PO-only operation is required.

QA planning: Required separately after implementation readiness.

QA execution: Not authorized or specified here.

Documentation drainage: Separate and post-QA. It is not an implementation deliverable, PR substitute, acceptance gate, or proof of completion.

Canon updates: No PF-document update is required as an execution output.

Acceptance: Token claims and acceptance decisions occur outside this plan and require governed evidence.

Historical context: Preserved only; it creates no current requirement or completion claim.

Repository consult: Establishes current repository facts only.

## Tracked Issues

No tracked issues.

## ADR Stubs

No ADR stub is required. The authority hierarchy resolves the current artifact-family, invocation, QA-vocabulary, and lifecycle questions without an open architecture choice.

## Plan Preflight

* Epic identity, Calcination phase, objective, and boundaries are definitive.
* All nine in-scope PF09.1 subtasks have exactly one primary disposition: A — Executable work item.
* Each executable work item has an exact PF09 parent and subtask mapping, exact PF14 reference, and PF09 disposition.
* Every mapped PF09 status was read as recorded; no Partial, Consolidation pending, or Not done status was converted to Done.
* The complete current PF10 source was checked; addenda 2.1, 2.2, and 2.3 govern their exact topics, and this plan applies addendum 2.3 to D1 through D5 work, CI remediation, evidence posture, and the closeout lifecycle.
* The complete PF27 Epic Record Template unit governs this structure.
* Every material current repository locus was directly inspected.
* The bounded negative repository-consumer observation identifies its search terms and scope.
* D4’s current-ref consumer proof and D5’s reachability proof are ordered execution predicates with fixed continuation and failure rules.
* All intended token names are validated against the current PF04 §2.0 roster; no token-resolution Tracked Issue remains.
* No in-scope planning field is left open, provisional, or dependent on later Epic Plan authoring.
* No source-derived task is silently omitted or deferred.
* No public contract, Human Design mechanic, OPS task, deployment, migration, PF update, or later-phase work is introduced.
* Implementation, QA, OPS, documentation, acceptance, history, and repository-reality lanes remain separate.
* No QA command, Live QA procedure, QA PASS, token satisfaction, acceptance, PF09 movement, board movement, or closeout claim appears; required planning-level artifact paths are listed without QA execution detail.
* Approval activates this fixed epic scope and sequence without requiring an Epic Plan addendum, resubmission, or reapproval.

ASK OK?
