# Implementation Plan HDE-EPIC038

Version: r6

## Source posture

* PF10 governs only where it explicitly speaks. It is silent for this epic.  
* PF-Canon governs where PF10 is silent.  
* PF09.6 is the phased completion backbone.  
* PF14 supplies mechanics and component proof anchors, not token semantics or planning authority.  
* PF04 is the single acceptance-token registry.  
* PF12 is the path and artifact authority.  
* PF07 is the infrastructure fact authority.  
* Live repo reality supersedes prior audit observations for current paths and implementation state.  
* PF20 is not used for planning, acceptance, tokens, evidence paths, or required-now claims.  
* No PF document edit is an implementation or OPS deliverable.

## Observed source split

* Observed audit provenance: the earlier static audit inspected repository root `/workspace/glow-hdengine-v2` on branch `work`.  
* Observed repo reality: the connected repository currently exposes default branch `main`.  
* The earlier audit’s repo observations remain useful only as search provenance. Every PR begins by revalidating the current checkout.

## Output

This document is the HDE-EPIC038 Implementation Plan containing:

* PR-01 through PR-06.  
* OPS-01 and OPS-02.  
* PF09 Completion Scope.  
* Complete D1 through D13 crosswalk.  
* Self-contained Codex prompts.  
* Canon-reconciliation ADRs.  
* PO input inventory.

## Later artifacts outside implementation execution

The following are later QA or closeout surfaces. They are not implementation or OPS deliverables in this plan:

* Planned output for later closeout: `audit/EPIC-038_close_report.md`.  
* Planned output for later closeout: `audit/EPIC-038_MANIFEST.json`.  
* Planned output for later acceptance work: `docs/acceptance_map_epic038.json`.  
* Planned output for later acceptance work: `docs/acceptance_map_epic038.json.path_proof.txt`.  
* Planned output for later QA planning and execution: `audit/qa/hde-epic038/`.  
* Planned output for later QA planning and execution: `audit/qa/hde-epic038/token_evidence_matrix.md`.  
* Planned output for later QA planning and execution: `audit/qa/hde-epic038/acceptance_map_viability.log`.  
* Drain target only: `audit/docdeltas/hde-epic038_doc_deltas.md`.  
* Drain target only: `audit/qa/hde-epic038/00_meta/doc_deltas.md`.

Their absence in the current repo does not block implementation planning because their canonical homes are already defined and they belong to later QA, acceptance, documentation, or closeout axes.

# Brief recap of scope

HDE-EPIC038 is the Distillation reliability pass that consolidates governed evidence discipline, immutable identity and provenance, release identity indexing, environment snapshot v3, deterministic gates, Catalog-driven A7 proofs, CI rails, DB and BodyGraph posture, DB-bridge parity, a keys-only architecture snapshot, controlled configured-v2 mapped-cache persistence, and a single release sanity pipeline.

The epic does not add public Reader behavior, public routes, app-side HumanDesignAPI ownership, a second HTTP home, raw vendor-envelope persistence, broad HumanDesignAPI v2 conformance, performance/load scope, production mapped-cache authorization, PF09 status movement, QA PASS, OPS completion, or closeout. Dry-run mapping, compatibility computation, durable cache write/read-back, and production authorization remain separate truth states.

# PF09 Completion Scope

## HDE-DIST005.1

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST005 PF09 subtask ID: HDE-DIST005.1 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 / PR-06 IG source item(s): Deliverable D1 — Global discipline Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Establish canonical encoding and pinned-environment enforcement, then confirm the completed evidence family through the final release sanity chain.

## HDE-DIST005.2

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST005 PF09 subtask ID: HDE-DIST005.2 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 / PR-06 IG source item(s): Deliverable D1 — Global discipline Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Canonical evidence tooling must update the Human Index, hash sentinel, Machine Mirror, checksum sidecar, and path proofs in one coherent run.

## HDE-DIST006.1

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST006  
PF09 subtask ID: HDE-DIST006.1  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-01  
IG source item(s): Deliverable D2 — Identity and provenance module  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: Resolved plan-local implementation decision: create one fetch-only immutable identity module with the exact six-field set and no request-time environment or evidence-root fallback.

## HDE-DIST006.2

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST006 PF09 subtask ID: HDE-DIST006.2 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 IG source item(s): Deliverable D2 — Identity and provenance module Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Reader, CLI, admin, and internal identity surfaces must consume the shared helpers instead of reading identity environment keys directly.

## HDE-DIST006.3

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST006 PF09 subtask ID: HDE-DIST006.3 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 IG source item(s): Deliverable D2 — Identity and provenance module Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Generate emitter and Invocation SHA-256 artifacts and bind the identity family through PF12 evidence discipline.

## HDE-DIST002.4

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST002  
PF09 subtask ID: HDE-DIST002.4  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-01  
IG source item(s): Deliverable D3 — Release identity indexing  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: Use Existing: `artifacts/math/freeze_pack_manifest.json` (PF12 — HDE-Schemas & Artifacts) as the canonical Freeze-Pack evidence copy and do not create a second manifest home.

## HDE-DIST002.5

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST002 PF09 subtask ID: HDE-DIST002.5 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 IG source item(s): Deliverable D3 — Release identity indexing Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Produce and index the PF12-defined BodyGraph release bindings artifact.

## HDE-DIST003.1

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST003 PF09 subtask ID: HDE-DIST003.1 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 IG source item(s): Deliverable D4 — Environment snapshot indexing Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Replace the current schema-v1 environment snapshot with the PF12-required schema-version-3 singleton.

## HDE-DIST003.4

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST003 PF09 subtask ID: HDE-DIST003.4 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-01 IG source item(s): Deliverable D4 — Environment snapshot indexing Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Bind the environment snapshot and any refreshed logs or metrics in the same evidence refresh.

## HDE-DIST001.1

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST001 PF09 subtask ID: HDE-DIST001.1 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-02 IG source item(s): Deliverable D5 — Determinism gates Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Consolidate preimage recompute, Reader-to-CLI parity, AB-to-BA coherence, two-run identity, and canonical compare under one deterministic producer family.

## HDE-DIST001.2

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST001  
PF09 subtask ID: HDE-DIST001.2  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-02  
IG source item(s): Deliverable D6 — A7 transport gates  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: Prove A7 only through the Catalog-designated JSON success route and use Existing: `artifacts/proofs/success_encoding_invariance.txt` (PF12 — HDE-Schemas & Artifacts) for encoding-invariance evidence.

## HDE-DIST001.3

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST001 PF09 subtask ID: HDE-DIST001.3 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-03 IG source item(s): Deliverable D7 — CI rails gates Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Convert prior EPIC031-scoped job definitions into reusable current rails gates without enabling live vendor calls in CI.

## HDE-DIST001.4

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST001  
PF09 subtask ID: HDE-DIST001.4  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-04 / OPS-01 / PR-06  
IG source item(s): Deliverable D8 — DB posture runtime checks  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A

Notes: PR-04 implements the deterministic harness, OPS-01 contributes live read-only posture evidence, and PR-06 verifies and binds the combined evidence without rerunning OPS. The boundary-view proof family is Existing and regenerated at `artifacts/db/boundary_view.readonly.proof.txt` and `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`; no second boundary-view evidence home is created.

## HDE-DIST001.5

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST001 PF09 subtask ID: HDE-DIST001.5 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-04 / PR-06 IG source item(s): Deliverable D9 — BodyGraph mechanics gates Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: BodyGraph policy labels absent from PF04 remain proof obligations, not acceptance tokens.

## HDE-DIST001.9

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST001 PF09 subtask ID: HDE-DIST001.9 Disposition for this plan: Complete in this epic Implementing task ID(s): PR-04 / OPS-01 / PR-06 IG source item(s): Deliverable D10 — DB-bridge parity and environment connectivity Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Fixture-backed parity is implemented in PR-04; live direct/bridge availability and row-level parity are contributed by OPS-01.

## HDE-DIST001.10

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST001  
PF09 subtask ID: HDE-DIST001.10  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-04 / PR-06  
IG source item(s): Deliverable D11 — Architecture snapshot evidence  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: The architecture snapshot path and schema are resolved plan-local planned outputs under existing governed roots; they are not alternate homes for an existing artifact.

## HDE-DIST001.11

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST001  
PF09 subtask ID: HDE-DIST001.11  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-05 / OPS-02 / PR-06  
IG source item(s): Deliverable D12 — v2 mapped-cache persistence hardening  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: The approved epic explicitly authorizes this Optional PF09.6 row for controlled implementation. The mapped-cache artifact family uses the resolved plan-local paths stated in PR-05. Production or production-like write authorization remains excluded.

## HDE-DIST001.6

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation  
PF09 task ID: HDE-DIST001  
PF09 subtask ID: HDE-DIST001.6  
Disposition for this plan: Complete in this epic  
Implementing task ID(s): PR-06  
IG source item(s): Deliverable D13 — Release sanity pipeline  
Caveat ID(s): None  
Proof pointer: N/A  
ADR ID: N/A  
PF07-gap note: N/A  
Notes: The release sanity pipeline uses Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log` as the PF12 canonical evidence surface and consumes OPS evidence without executing OPS.

## HDE-DIST004.1

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST004 PF09 subtask ID: HDE-DIST004.1 Disposition for this plan: Deferred by IG/CAVEATS Implementing task ID(s): N/A IG source item(s): Performance and Load Harness Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Explicitly outside HDE-EPIC038; remains PF09-accounted.

## HDE-DIST004.2

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST004 PF09 subtask ID: HDE-DIST004.2 Disposition for this plan: Deferred by IG/CAVEATS Implementing task ID(s): N/A IG source item(s): Performance and Load Harness Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Explicitly outside HDE-EPIC038; remains PF09-accounted.

## HDE-DIST004.3

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST004 PF09 subtask ID: HDE-DIST004.3 Disposition for this plan: Deferred by IG/CAVEATS Implementing task ID(s): N/A IG source item(s): Performance and Load Harness Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Explicitly outside HDE-EPIC038; remains PF09-accounted.

## HDE-DIST004.4

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation PF09 task ID: HDE-DIST004 PF09 subtask ID: HDE-DIST004.4 Disposition for this plan: Deferred by IG/CAVEATS Implementing task ID(s): N/A IG source item(s): Performance and Load Harness Caveat ID(s): None Proof pointer: N/A ADR ID: N/A PF07-gap note: N/A Notes: Explicitly outside HDE-EPIC038; remains PF09-accounted.

# Crosswalk: IG items \-\> Plan tasks

| IG work item (exact label from IG) | Caveats applied | PF09 document(s) | PF09 task ID(s) | PF09 subtask ID(s) | Implementation tasks | Evidence pointer | Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Deliverable D1 — Global discipline | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST005 | HDE-DIST005.1, HDE-DIST005.2 | PR-01, PR-06 | N/A | Planned |
| Deliverable D2 — Identity and provenance module | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST006 | HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3 | PR-01 | N/A | Planned |
| Deliverable D3 — Release identity indexing | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST002 | HDE-DIST002.4, HDE-DIST002.5 | PR-01 | N/A | Planned |
| Deliverable D4 — Environment snapshot indexing | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST003 | HDE-DIST003.1, HDE-DIST003.4 | PR-01 | N/A | Planned |
| Deliverable D5 — Determinism gates | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.1 | PR-02 | N/A | Planned |
| Deliverable D6 — A7 transport gates | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.2 | PR-02 | N/A | Planned |
| Deliverable D7 — CI rails gates | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.3 | PR-03 | N/A | Planned |
| Deliverable D8 — DB posture runtime checks | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.4 | PR-04, OPS-01, PR-06 | N/A | Planned |
| Deliverable D9 — BodyGraph mechanics gates | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.5 | PR-04, PR-06 | N/A | Planned |
| Deliverable D10 — DB-bridge parity and environment connectivity | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.9 | PR-04, OPS-01, PR-06 | N/A | Planned |
| Deliverable D11 — Architecture snapshot evidence | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.10 | PR-04, PR-06 | N/A | Planned |
| Deliverable D12 — v2 mapped-cache persistence hardening | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.11 | PR-05, OPS-02, PR-06 | N/A | Planned |
| Deliverable D13 — Release sanity pipeline | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST001 | HDE-DIST001.6 | PR-06 | N/A | Planned |
| TI-001 — PF09 row-listed proof labels require registry-safe acceptance handling | None | N/A — PF04 §2.0.0 controls | N/A | N/A | All PR and OPS acceptance sections | Unregistered labels remain non-token proof obligations | Resolved by controlling canon |
| Performance and Load Harness | None | PF09.6 — HDE-Build-Checklist-Distillation | HDE-DIST004 | HDE-DIST004.1, HDE-DIST004.2, HDE-DIST004.3, HDE-DIST004.4 | Deferred | N/A | Deferred |

# Execution plan

1. **PR-01 — Identity, release, environment, and evidence foundations**  
     
   * Intent: Establish the immutable identity source, complete release bindings, migrate the environment singleton to schema version 3, and harden evidence single-writer discipline.  
   * Depends on: None.  
   * IG item(s) covered: D1, D2, D3, D4.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST005, HDE-DIST006, HDE-DIST002, HDE-DIST003.  
   * PF09 subtask ID(s): HDE-DIST005.1, HDE-DIST005.2, HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3, HDE-DIST002.4, HDE-DIST002.5, HDE-DIST003.1, HDE-DIST003.4.  
   * PF09 completion role: Complete in this epic.

   

2. **PR-02 — Determinism and Catalog-driven A7 gates**  
     
   * Intent: Consolidate deterministic public-body gates and the complete A7 proof family around the Endpoint Catalog.  
   * Depends on: PR-01.  
   * IG item(s) covered: D5, D6.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.1, HDE-DIST001.2.  
   * PF09 completion role: Complete in this epic.

   

3. **PR-03 — Reusable CI rails gates**  
     
   * Intent: Generalize closed-rails refusal, fixture-backed open-rails policy, retry/backoff, and keys-only logging gates.  
   * Depends on: PR-02.  
   * IG item(s) covered: D7.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.3.  
   * PF09 completion role: Complete in this epic.

   

4. **PR-04 — DB, BodyGraph, bridge, and architecture posture harness**  
     
   * Intent: Complete deterministic local mechanics for DB posture, BodyGraph policy, direct-versus-bridge parity, environment connectivity, and the keys-only architecture snapshot.  
   * Depends on: PR-01, PR-03.  
   * IG item(s) covered: D8, D9, D10, D11.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.9, HDE-DIST001.10.  
   * PF09 completion role: Complete in this epic.

   

5. **OPS-01 — Live DB and bridge posture capture**  
     
   * Intent: Contribute bounded, read-only, secret-safe current-environment DB posture and provider-parity evidence.  
   * Depends on: PR-04.  
   * IG item(s) covered: D8, D10.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.4, HDE-DIST001.9.  
   * PF09 completion role: Contributes evidence only.

   

6. **PR-05 — Configured-v2 mapped-cache persistence**  
     
   * Intent: Implement safe mapped HDE payload persistence, read-back, idempotence, closed-rails refusal, and legacy fallback preservation.  
   * Depends on: PR-04.  
   * IG item(s) covered: D12.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.11.  
   * PF09 completion role: Complete in this epic.

   

7. **OPS-02 — Controlled configured-v2 mapped-cache proof**  
     
   * Intent: Contribute one bounded, PO-authorized configured-v2 write/read-back and idempotence proof using synthetic identity data.  
   * Depends on: PR-05.  
   * IG item(s) covered: D12.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST001.11.  
   * PF09 completion role: Contributes evidence only.

   

8. **PR-06 — Release sanity orchestration and evidence binding**  
     
   * Intent: Bind completed PR and OPS proof families into the deterministic release sanity pipeline and perform the final canonical evidence refresh.  
   * Depends on: PR-01 through PR-05, OPS-01, OPS-02.  
   * IG item(s) covered: D1, D8, D9, D10, D11, D12, D13.  
   * PF09 document(s): PF09.6 — HDE-Build-Checklist-Distillation.  
   * PF09 task ID(s): HDE-DIST005, HDE-DIST001.  
   * PF09 subtask ID(s): HDE-DIST005.1, HDE-DIST005.2, HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.6, HDE-DIST001.9, HDE-DIST001.10, HDE-DIST001.11.  
   * PF09 completion role: Complete in this epic.

# PR series

## PR-01 — Identity, release, environment, and evidence foundations

### Intent

Create the immutable Identity & Provenance implementation, remove request-time identity environment reads from governed surfaces, produce the complete identity and release-binding evidence families, migrate the environment singleton to schema version 3, and preserve PF12 single-writer evidence discipline.

### IG source items

* Deliverable D1 — Global discipline.  
* Deliverable D2 — Identity and provenance module.  
* Deliverable D3 — Release identity indexing.  
* Deliverable D4 — Environment snapshot indexing.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST005.

PF09 task proof excerpt:

“Enforce that all Phase VI evidence artifacts use canonical encodings and are captured under pinned locale, and that every artifact addition/move/removal is reflected in both Human Index and Machine Mirror in the same PR.”

PF09 task ID: HDE-DIST006.

PF09 task proof excerpt:

“Wire the Identity & Provenance module as the single source of truth for engine and release identity. Identity values are initialized once per cut and are read-only thereafter; all public and operator surfaces consume via helpers.”

PF09 task ID: HDE-DIST002.

Path classification for the quoted locator: Existing: `catalog/manifest.json` (PF12 — HDE-Schemas & Artifacts).

PF09 task proof excerpt:

“Canonicalize `catalog/manifest.json`, compute and recompute `release_id` as `sha256(canonical_bytes("catalog/manifest.json"))`, enforce manifest structure invariants, and maintain pack/manifest identity artifacts.”

PF09 task ID: HDE-DIST003.

PF09 task proof excerpt:

“Capture a v3 singleton environment snapshot, plus keys-only logs and metrics snapshots, and index them under the Evidence Index discipline.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST005.1.

“Ensure all Phase VI evidence artifacts: Use canonical JSON or headers-only text, LF-terminated.”

PF09 subtask ID: HDE-DIST005.2.

“Maintain fixed field order and `proof_anchor` to co-located path\_proof files.”

PF09 subtask ID: HDE-DIST006.1.

“Ensure the Identity & Provenance module exposes and persists exactly these fields — no extras — as read-only values after freeze.”

PF09 subtask ID: HDE-DIST006.2.

“Prove that public Reader and CLI code paths obtain identity from the Identity & Provenance module helpers.”

PF09 subtask ID: HDE-DIST006.3.

“Capture and persist build-time hashes for the shared emitter and invocation and index them as identity artifacts.”

PF09 subtask ID: HDE-DIST002.4.

“Index manifest and release identity artifacts in Human Index and Machine Mirror in the same PR; each mirror record includes a `proof_anchor` path-proof.”

PF09 subtask ID: HDE-DIST002.5.

“Capture and index the release bindings artifact that ties `release_id` to BodyGraph data source policy and refresh behavior.”

PF09 subtask ID: HDE-DIST003.1.

“Produce `artifacts/runtime/env_matrix.snapshot.json` as a singleton per repo.”

Path classification for the quoted locator: Existing: `artifacts/runtime/env_matrix.snapshot.json` (PF12 — HDE-Schemas & Artifacts).

PF09 subtask ID: HDE-DIST003.4.

Existing paths in the quoted line:

* Existing: `docs/evidence/INDEX.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `docs/evidence/INDEX.sha256` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `artifacts/evidence_index.jsonl` (PF12 — HDE-Schemas & Artifacts).

“Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR to include env snapshot, logs sample, and metrics artifacts, with `proof_anchor` path-proofs.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide §1.3.1 Evidence jobs.

“Only a small set of evidence writers may write governed evidence artifacts. All other code — including tests and ad-hoc scripts — MUST NOT modify governed evidence directly.”

PF14 anchor: HDE-Mechanics Guide §13 Identity & Provenance Module.

“Purpose. Single source of truth for engine and release identity. Values are initialized once per cut and are read-only thereafter; all public and operator surfaces consume via helpers.”

PF14 anchor: HDE-Mechanics Guide §13.2 Accessors.

“identity\_meta() → {"engine\_tag","invocation\_tag"} — inserted into the public envelope before idempotence hashing.”

“identity\_admin() → {"engine\_tag","release\_id","invocation\_tag","invocation\_sha256","build\_commit","emitter\_sha256"} — for internal/admin surfaces.”

### PF07 facts / gaps

* PF07-derived repository: `amthorn78/glow-hdengine-v2`.  
* PF07-derived default branch: `main`.  
* PF07-derived HD Engine provider: Railway.  
* PF07-derived HD Engine project: `ample-illumination`.  
* PF07-derived HD Engine service: `glow-hdengine-v2`.  
* PF07-derived database instance: `ample-illumination/production/postgres`.  
* PF07-derived database schema: `hde`.  
* PF07-derived determinism keys: `LC_ALL`, `LANG`, `TZ`.  
* PF07-derived rails keys: `SAFE_MODE`, `ALLOW_NETWORK`.  
* PF07 gap: None for this PR.

### Observed repo reality

* Observed repo reality: `engine/runtime/__init__.py` exports only public Reader emitter functions.  
    
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `engine/runtime/public.py` requires callers to supply `engine_tag`, `invocation_tag`, and `release_id`.  
    
  * Proof excerpt: `def emit_reader_public_envelope(`.  
  * Proof excerpt: `a_chart: Dict[str, object],`.  
  * Proof excerpt: `b_chart: Dict[str, object],`.  
  * Proof excerpt: `*,`.  
  * Proof excerpt: `engine_tag: str,`.  
  * Proof excerpt: `invocation_tag: str,`.  
  * Proof excerpt: `release_id: str,`.  
  * Proof excerpt: `eligible: bool = True,`.  
  * Proof excerpt: `) -> Tuple[bytes, Dict[str, object]]:`.  
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `adapter/http_reader.py` reads `ENGINE_TAG`, `PRODUCT_INVOCATION_TAG`, and `RELEASE_ID` inside the Reader request path.  
    
  * Proof excerpt: `engine_tag = os.environ.get("ENGINE_TAG", "hdengine-alpha")`.  
  * Proof excerpt: `invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-UNKNOWN")`.  
  * Proof excerpt: `release_id = os.environ.get("RELEASE_ID", "0" * 64)`.  
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `engine/cli/main.py` defines `_engine_identity()` using the same three environment values.  
    
  * Proof excerpt: `engine_tag = os.environ.get("ENGINE_TAG", "hdengine-dev")`.  
  * Proof excerpt: `release_id = os.environ.get("RELEASE_ID", "0" * 64)`.  
  * Proof excerpt: `invocation_tag = os.environ.get("PRODUCT_INVOCATION_TAG", "INV-LOCAL")`.  
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `artifacts/identity/service_identity.json` exists with five top-level fields and lacks `invocation_sha256`.  
    
  * Proof excerpt: the present top-level keys are `build_commit`, `emitter_sha256`, `engine_tag`, `invocation_tag`, and `release_id`; `invocation_sha256` is absent.  
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `artifacts/runtime/env_matrix.snapshot.json` currently declares `"schema": "v1"` and is pretty-printed rather than canonical compact JSON.  
    
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `artifacts/identity/release_id.json` was not found.  
    
  * Read-only command used: GitHub `fetch_file`; current default branch returned 404\.


* Observed repo reality: `artifacts/bodygraph/release_bindings.json` was not found.  
    
  * Read-only command used: GitHub `fetch_file`; current default branch returned 404\.

### Observed audit provenance

* Observed audit provenance: the identity family was partial, with only the service identity snapshot found.  
* Observed audit provenance: release identity recompute tooling and the older release-math evidence family were present.  
* Observed audit provenance: no current generator was identified for the BodyGraph release bindings artifact.  
* These observations must be rechecked before editing.

### Discovery

Codex performs these read-only checks before changing files:

* Read-only discovery command for Existing canon root: `find docs/pfcanon -maxdepth 1 -type f -print | sort`.  
* Read-only discovery command for Observed repo reality: `git status --short --branch`.  
* Read-only discovery command for Observed repo reality path: `sed -n '1,180p' engine/runtime/public.py`.  
* Read-only discovery command for Observed repo reality path: `sed -n '320,390p' adapter/http_reader.py`.  
* Read-only discovery command for Observed repo reality path: `grep -n -F '_engine_identity' engine/cli/main.py`.  
* Read-only discovery command for Observed repo reality path: `grep -R -n -F 'service_identity' engine adapter presenter tools tests`.  
* Read-only discovery command for Existing artifact root: `find artifacts/identity -maxdepth 2 -type f -print | sort`.  
* Read-only discovery command for Existing artifact: `cat artifacts/runtime/env_matrix.snapshot.json`.  
* Read-only discovery command for Existing evidence tooling: `sed -n '1,240p' tools/evidence/update_evidence_index.py`.  
* Stop and report the current fact instead of inventing a second identity home if the current repo has gained a canonical identity module after this plan was authored.

### Implementation requirements

1. Create Planned output: `engine/runtime/identity.py`.  
     
   * Define an immutable validated identity snapshot with exactly:  
       
     * `engine_tag`  
     * `build_commit`  
     * `invocation_tag`  
     * `invocation_sha256`  
     * `emitter_sha256`  
     * `release_id`  
   * Identity values originate at cut time from PF14 sources: `release_id` from canonical bytes of Existing: `catalog/manifest.json`; Invocation tag and canonical bytes from the Invocation registry; and `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` from the build snapshot.  
   * Expose `identity_meta()` and `identity_admin()`.  
   * Reject unknown or missing fields.  
   * Load or initialize identity once and prohibit mutation.  
   * The module is fetch-only and must not read `artifacts/identity/service_identity.json` or any other evidence-root file as a runtime input.  
   * Do not read identity environment variables in Reader, CLI, or request handlers.  
   * No conditional alternate identity seam is authorized.

   

2. Update Observed repo reality path: `engine/runtime/__init__.py`.  
     
   * Export only the public identity helpers required by callers.  
   * Preserve existing Reader emitter exports.

   

3. Update Observed repo reality path: `engine/runtime/public.py`.  
     
   * Obtain public identity fields through `identity_meta()` and the frozen release identity.  
   * Remove the need for public callers to inject identity values independently, unless an internal test seam is explicitly retained and cannot affect production call paths.

   

4. Update Observed repo reality path: `adapter/http_reader.py`.  
     
   * Replace Reader request-time identity environment reads with shared helpers.  
   * Route Existing endpoint: `/internal/version` through `identity_admin()`.  
   * Preserve Existing endpoint: `/reader` public bytes and A7 posture.  
   * Do not canonize or alter `/internal/version` authentication posture.

   

5. Update Observed repo reality path: `engine/cli/main.py`.  
     
   * Replace `_engine_identity()` environment reads with shared identity helpers.  
   * Preserve existing CLI output contracts and stream behavior.

   

6. Inspect Observed repo reality path: `engine/http/compat_handler.py`.  
     
   * Use identity helpers where that surface emits identity.  
   * Do not add identity fields to public contracts that do not already carry them.

   

7. Create Planned output: `tools/evidence/generate_identity_provenance.py`.  
     
   * Generate the full identity evidence family from the cut-time identity source.  
   * Compute the shared emitter hash from the allow-listed emitter source.  
   * Compute the Invocation hash from the PO-supplied canonical Invocation bytes.  
   * Derive `release_id` only from canonical bytes of Existing: `catalog/manifest.json` (PF12 — HDE-Schemas & Artifacts).  
   * Regenerate Existing and regenerated output: `artifacts/identity/service_identity.json` with exactly `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, and `release_id`.  
   * Add a regression assertion in Planned test path: `tests/evidence/test_identity_provenance.py` that fails on any missing or extra top-level field.  
   * Provide deterministic write mode and `--check` mode.  
   * Do not use wall-clock time or random values in governed output.

   

8. Create Planned output: `tools/evidence/generate_release_bindings.py`.  
     
   * Generate the PF12-defined BodyGraph release bindings.  
   * Bind release identity to BodyGraph source-selection and refresh-policy artifact identities without duplicating their payloads.  
   * Provide deterministic write and check modes.

   

9. Create Planned output: `tools/evidence/generate_env_matrix_snapshot.py`.  
     
   * Replace the current schema-v1 artifact with a schema-version-3 singleton.  
   * Include default rails and determinism pins.  
   * Include presence booleans for DB, bridge, and production-bridge guard.  
   * Record presence only, never values, for secret-bearing configuration.  
   * Reject unknown fields.  
   * Emit canonical JSON with one LF.  
   * Provide deterministic write and check modes.

   

10. Extend the canonical evidence updater rather than hand-editing governed artifacts.  
      
    * Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).  
    * Ensure all new identity, release-binding, and environment artifacts receive Human Index rows, Machine Mirror rows, checksum updates, and sibling path proofs in one convergent run.

    

11. Preserve current public and vendor boundaries.  
      
    * No new endpoint.  
    * No Reader payload expansion.  
    * No runtime vendor call.  
    * No DB write.  
    * No PF-Canon edit.

### Concrete anchors

* Planned output: `engine/runtime/identity.py`.  
* Observed repo reality: `engine/runtime/__init__.py`.  
* Observed repo reality: `engine/runtime/public.py`.  
* Observed repo reality: `adapter/http_reader.py`.  
* Observed repo reality: `engine/cli/main.py`.  
* Observed repo reality: `engine/http/compat_handler.py`.  
* Planned output: `tools/evidence/generate_identity_provenance.py`.  
* Planned output: `tools/evidence/generate_release_bindings.py`.  
* Planned output: `tools/evidence/generate_env_matrix_snapshot.py`.  
* Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `catalog/manifest.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `artifacts/math/freeze_pack_manifest.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `artifacts/runtime/env_matrix.snapshot.json` (PF12 — HDE-Schemas & Artifacts).

### Evidence outputs

* Planned output: `artifacts/identity/release_id.json`.  
* Planned output: `artifacts/identity/release_id.json.path_proof.txt`.  
* Planned output: `artifacts/identity/release_id_recompute.log`.  
* Planned output: `artifacts/identity/release_id_recompute.log.path_proof.txt`.  
* Planned output: `artifacts/parity/two_run_identity.log`.  
* Planned output: `artifacts/parity/two_run_identity.log.path_proof.txt`.  
* Existing and regenerated output: `artifacts/identity/service_identity.json`.  
* Planned output: `artifacts/identity/service_identity.json.path_proof.txt`.  
* Planned output: `artifacts/identity/emitter_sha256.json`.  
* Planned output: `artifacts/identity/emitter_sha256.json.path_proof.txt`.  
* Planned output: `artifacts/identity/invocation_sha256.json`.  
* Planned output: `artifacts/identity/invocation_sha256.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/release_bindings.json`.  
* Planned output: `artifacts/bodygraph/release_bindings.json.path_proof.txt`.  
* Existing and regenerated output: `artifacts/runtime/env_matrix.snapshot.json`.  
* Existing and regenerated output: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`.  
* Existing and regenerated output: `docs/evidence/INDEX.json`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256`.  
* Existing and regenerated output: `docs/evidence/INDEX.json.path_proof.txt`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.

### Acceptance tokens

Token names below are PF04-registered and are planned claims only. This PR does not declare them satisfied:

* `RELEASE_ID_RECOMPUTE_OK`  
* `CLI_READER_PARITY_OK`  
* `TWO_RUN_IDENTITY_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `ENV_LC_ALL_C_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
* `EVIDENCE_PATH_PROOFS_OK`  
* `CI_CHECK_MIRROR_SCHEMA_OK`  
* `CI_CHECK_FINAL_LF_OK`

The following are proof obligations, not token claims:

* Environment snapshot singleton.  
* Environment snapshot schema version 3\.  
* Presence-only DB, bridge, and guard posture.

### Rails posture

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`  
* No external service calls.  
* No privileged DB access.  
* No secret values in artifacts or logs.

### Basic QA check \+ pass condition

Basic QA check:

* Run Planned command: `python tools/evidence/generate_identity_provenance.py`.  
* Run Planned command: `python tools/evidence/generate_release_bindings.py`.  
* Run Planned command: `python tools/evidence/generate_env_matrix_snapshot.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py`.  
* Run `python -m pytest` against Planned test path: `tests/runtime/test_identity.py`.  
* Run `python -m pytest` against Planned test path: `tests/evidence/test_identity_provenance.py`.  
* Run `python -m pytest` against Planned test path: `tests/evidence/test_release_bindings.py`.  
* Run `python -m pytest` against Planned test path: `tests/evidence/test_env_matrix_snapshot_v3.py`.  
* Run Planned command: `python tools/evidence/generate_identity_provenance.py --check`.  
* Run Planned command: `python tools/evidence/generate_release_bindings.py --check`.  
* Run Planned command: `python tools/evidence/generate_env_matrix_snapshot.py --check`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python tools/evidence/orientation_demo.py --check`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.  
* Run Existing command: `bash ci/checks/check_evidence_index_hash.sh`.  
* Run Existing command: `ci/checks/check_final_lf.sh`.

Pass condition:

* Identity has exactly six immutable fields.  
* Reader, CLI, and internal identity surfaces use shared helpers.  
* Identity evidence recomputes from canonical sources.  
* Environment snapshot is canonical schema version 3 and the only active singleton.  
* Release bindings exist and reference governed sources.  
* All targeted tests and check modes exit 0\.  
* Index, sentinel, mirror, checksum, and path-proof validation are coherent.  
* No public contract or external state changes.

### PO inputs

* Confirmed engine tag for the cut.  
* Canonical Invocation bytes corresponding to `INV-f2ac55d77ce9aacc`.  
* Confirmation that the existing Invocation tag remains current.  
* Confirmation of any optional build-commit exposure policy for operator surfaces.  
* No secret values.

### Codex Prompt

You are implementing HDE-EPIC038 PR-01 in the current `amthorn78/glow-hdengine-v2` checkout.

This is repository implementation work only. Do not edit PF-Canon, perform OPS, access external services, run migrations, claim QA PASS, claim token satisfaction, move PF09 status, or create closeout artifacts.

Implement these PF09.6 mappings:

* HDE-DIST005.1 — canonical encodings and environment pins.  
* HDE-DIST005.2 — Human Index and Machine Mirror discipline.  
* HDE-DIST006.1 — exact immutable identity field set.  
* HDE-DIST006.2 — shared `identity_meta()` and `identity_admin()` helpers.  
* HDE-DIST006.3 — emitter and Invocation hashes with evidence bindings.  
* HDE-DIST002.4 — release identity indexing.  
* HDE-DIST002.5 — BodyGraph release bindings.  
* HDE-DIST003.1 — environment snapshot singleton schema version 3\.  
* HDE-DIST003.4 — environment and observability indexing.

Use these PF14 anchors:

* HDE-Mechanics Guide §1.3.1 Evidence jobs.  
* HDE-Mechanics Guide §13 Identity & Provenance Module.  
* HDE-Mechanics Guide §13.6 Evidence.

Use these PF07 facts:

* Repository: `amthorn78/glow-hdengine-v2`.  
* HD Engine provider: Railway.  
* HD Engine project: `ample-illumination`.  
* HD Engine service: `glow-hdengine-v2`.  
* DB instance: `ample-illumination/production/postgres`.  
* DB schema: `hde`.  
* Determinism pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* Closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

Inspect first:

* Observed repo reality: `engine/runtime/__init__.py`.  
* Observed repo reality: `engine/runtime/public.py`.  
* Observed repo reality: `adapter/http_reader.py`.  
* Observed repo reality: `engine/cli/main.py`.  
* Observed repo reality: `engine/http/compat_handler.py`.  
* Observed repo reality: `artifacts/identity/service_identity.json`, which currently has five top-level fields and lacks `invocation_sha256`.  
* Existing: `catalog/manifest.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `artifacts/math/freeze_pack_manifest.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `artifacts/runtime/env_matrix.snapshot.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).

Revalidate current repo reality with read-only commands before editing.

Create Planned output: `engine/runtime/identity.py` as the single fetch-only identity module. Identity values originate at cut time from these sources only:

* `release_id` from canonical bytes of Existing: `catalog/manifest.json`.  
* Invocation tag and canonical Invocation bytes from the Invocation registry.  
* `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` from the build snapshot.

The runtime module must expose exactly `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, and `release_id`; reject missing or extra fields; initialize once; expose `identity_meta()` and `identity_admin()`; prohibit mutation; and avoid request-time identity environment reads. Existing and regenerated output: `artifacts/identity/service_identity.json` is evidence output only and must never be a runtime input. No conditional alternate identity seam is authorized.

Update the Reader, CLI, compat, and internal identity callers to use the shared helpers. Preserve Existing endpoint: `/reader`. Preserve Existing endpoint: `/internal/version`. Do not alter `/internal/version` authentication policy.

Create these deterministic producers with write and `--check` modes:

* Planned output: `tools/evidence/generate_identity_provenance.py`.  
* Planned output: `tools/evidence/generate_release_bindings.py`.  
* Planned output: `tools/evidence/generate_env_matrix_snapshot.py`.

Generate these exact primary artifacts and their listed sibling path proofs:

* Planned output: `artifacts/identity/release_id.json`.  
* Planned output: `artifacts/identity/release_id.json.path_proof.txt`.  
* Planned output: `artifacts/identity/release_id_recompute.log`.  
* Planned output: `artifacts/identity/release_id_recompute.log.path_proof.txt`.  
* Planned output: `artifacts/parity/two_run_identity.log`.  
* Planned output: `artifacts/parity/two_run_identity.log.path_proof.txt`.  
* Existing and regenerated output: `artifacts/identity/service_identity.json`.  
* Planned output: `artifacts/identity/service_identity.json.path_proof.txt`.  
* Planned output: `artifacts/identity/emitter_sha256.json`.  
* Planned output: `artifacts/identity/emitter_sha256.json.path_proof.txt`.  
* Planned output: `artifacts/identity/invocation_sha256.json`.  
* Planned output: `artifacts/identity/invocation_sha256.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/release_bindings.json`.  
* Planned output: `artifacts/bodygraph/release_bindings.json.path_proof.txt`.  
* Existing and regenerated output: `artifacts/runtime/env_matrix.snapshot.json`.  
* Existing and regenerated output: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`.

Use these exact PF12 ledger and checksum paths and do not create alternates:

* Existing and regenerated output: `docs/evidence/INDEX.json`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256`.  
* Existing and regenerated output: `docs/evidence/INDEX.json.path_proof.txt`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.  
* Existing evidence copy: `artifacts/math/freeze_pack_manifest.json`.

The environment snapshot must use `schema_version: 3`, be canonical compact JSON with one LF, remain a singleton, record default rails and determinism pins, and expose only presence booleans for DB, bridge, and guard configuration.

Add these focused tests:

* Planned test path: `tests/runtime/test_identity.py`.  
* Planned test path: `tests/evidence/test_identity_provenance.py`.  
* Planned test path: `tests/evidence/test_release_bindings.py`.  
* Planned test path: `tests/evidence/test_env_matrix_snapshot_v3.py`.

The identity-provenance regression test must assert that the service-identity top-level key set is exactly the six PF14 fields, with no missing or extra field.

Generate and validate with these exact commands under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`:

* `python tools/evidence/generate_identity_provenance.py`  
* `python tools/evidence/generate_release_bindings.py`  
* `python tools/evidence/generate_env_matrix_snapshot.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python -m pytest tests/runtime/test_identity.py`  
* `python -m pytest tests/evidence/test_identity_provenance.py`  
* `python -m pytest tests/evidence/test_release_bindings.py`  
* `python -m pytest tests/evidence/test_env_matrix_snapshot_v3.py`  
* `python tools/evidence/generate_identity_provenance.py --check`  
* `python tools/evidence/generate_release_bindings.py --check`  
* `python tools/evidence/generate_env_matrix_snapshot.py --check`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py --check`  
* `python ci/checks/check_mirror_schema.sh`  
* `bash ci/checks/check_evidence_index_hash.sh`  
* `ci/checks/check_final_lf.sh`

Do not hand-edit the Human Index, hash sentinel, Machine Mirror, checksums, or path proofs.

PASS means all listed commands exit 0; identity is immutable, fetch-only, and single-sourced from cut-time inputs; the regenerated service-identity artifact has exactly six fields; the environment snapshot is canonical schema version 3 and singleton; release bindings exist; and all ledger, checksum, and path-proof validations are coherent. FAIL means any required field, source rule, producer, artifact, test, or evidence binding is missing or inconsistent.

## PR-02 — Determinism and Catalog-driven A7 gates

### Intent

Create one deterministic proof producer for public-body invariants and one Catalog-driven A7 producer, preserving the shared emitter and excluding `/internal/version` from A7.

### IG source items

* Deliverable D5 — Determinism gates.  
* Deliverable D6 — A7 transport gates.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics (determinism, A7, rails, DB posture, BodyGraph) and produce the full set of binary evidence artifacts in a deterministic, repeatable way, with Index/Mirror discipline.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.1.

“Reader↔CLI parity: For a fixed corpus of pairs, run Reader and CLI on the same inputs and byte-compare JSON envelopes; outputs must be identical.”

“AB↔BA & two-run identity: For each Integration pair, show AB/BA narrative and banding coherence and two-run byte identity.”

PF09 subtask ID: HDE-DIST001.2.

Existing endpoint classifications for the quoted line:

* Existing endpoint: `/reader` (PF05 — HDE-CLI-API-Vendor-Ref).  
* Existing endpoint: `/internal/version` (PF04 — HDE-Governance).

“On a Catalog JSON success route, prove the full A7 matrix and catalog posture.”

“A7 proofs must be captured on a Catalog JSON success route; `/internal/version` is excluded.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide §9.2 Reader.

“Route. GET /reader?v=1 is the governed Reader success-proof surface in current scope and the cataloged Reader success surface used for Reader success-body, Endpoint Catalog/env-gate, and A7 transport work.”

PF14 anchor: HDE-Mechanics Guide A7 proof boundary.

“Local harnesses may capture headers for evidence, but authoritative A7 proofs run on a Catalog JSON success route; /internal/version remains an ops exception.”

### PF07 facts / gaps

* PF07-derived local-style host convention: `127.0.0.1`.  
* PF07-derived determinism pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* PF07-derived closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.  
* PF07 gap: None. The exact local port remains implementation-proven from the existing start command and is not guessed in this plan.

### Observed repo reality

* Observed repo reality: `docs/ENDPOINTS_CATALOG.json` exists but does not meet the PF12 minimum authoritative-catalog schema.  
    
  * Proof excerpt: Existing endpoint `/reader` has `"a7_eligible":true`.  
  * Proof excerpt: Existing endpoint `/internal/version` has `"a7_eligible":false`.  
  * Proof excerpt: the top-level `success_endpoints` array is empty.  
  * Proof excerpt: `generated_at_utc` is absent.  
  * Proof excerpt: Boolean `internal` is absent from every endpoint record.  
  * Proof excerpt: `/reader` and `/internal/version` use method arrays rather than one string method per endpoint record.  
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: `adapter/http_reader.py` sets strong ETag, private revalidation cache control, and `Vary: Authorization, Accept-Encoding` on Reader success.  
    
  * Read-only command used: GitHub `fetch_file` on current default branch.


* Observed repo reality: current Reader identity inputs remain supplied through the runtime public emitter and are addressed by PR-01.  
    
* Observed repo reality: current Endpoint Catalog success-target derivation is incomplete because the `success_endpoints` collection is empty.

### Observed audit provenance

* Observed audit provenance: existing A7 transcript paths and Endpoint Catalog sidecars were present.  
* Observed audit provenance: the deterministic PF09.6 parity paths were not found.  
* Observed audit provenance: A7 artifacts existed, but target derivation from the empty `success_endpoints` collection remained unclear.

### Discovery

* Read-only discovery command for Existing catalog: `cat docs/ENDPOINTS_CATALOG.json`.  
* Read-only discovery command for Existing Reader implementation: `grep -n -F '_set_reader_200_headers' adapter/http_reader.py`.  
* Read-only discovery command for Existing Reader implementation: `grep -n -F 'If-None-Match' adapter/http_reader.py`.  
* Read-only discovery command for Existing proof producers: `grep -R -n -F 'HDE_WRITE_A7_PROOFS' tests tools adapter engine`.  
* Read-only discovery command for Existing parity producers: `grep -R -n -E 'preimage|reader_cli|abba|two_run|canon_compare' tests tools`.  
* Read-only discovery command for Existing artifacts: `find artifacts/proofs audit/gates -type f -print | sort`.  
* Read-only discovery command for Existing schema: `find schemas -type f -print | grep -F 'reader_success'`.  
* Extend a current canonical producer if one already exists. Create the planned producer only when no current single producer owns the required outputs.

### Implementation requirements

1. Create or consolidate Planned output: `tools/evidence/generate_determinism_gate_proofs.py`.  
     
   * Prove preimage recompute.  
   * Prove Reader-to-CLI byte identity.  
   * Prove AB-to-BA byte identity.  
   * Prove two-run identity.  
   * Prove canonical reserialization equality.  
   * Use a fixed, non-PII corpus.  
   * Provide write and `--check` modes.  
   * Fail if any lower-level predicate fails.

   

2. Create or consolidate Planned output: `tools/evidence/generate_a7_transport_proofs.py`.  
     
   * Repair Existing: `docs/ENDPOINTS_CATALOG.json` (PF12 — HDE-Schemas & Artifacts) to the PF12 minimum authoritative-catalog schema.  
   * Add top-level `generated_at_utc`.  
   * Add Boolean `internal` to every endpoint record.  
   * Represent `method` as one string per endpoint record; split existing multi-method arrays into separate method records while preserving route semantics.  
   * Explicitly designate `GET /reader` inside the Catalog’s existing machine-readable structure by populating the existing `success_endpoints` member with exactly one designation that resolves to method `GET` and path `/reader`.  
   * Define and validate the existing `success_endpoints` member in the Catalog schema when no current validator defines its shape; do not create a second designation key, inventory, flag, or route.  
   * Preserve Existing endpoint: `/internal/version` with `a7_eligible:false` and exclude it from the success-proof designation.  
   * Select the A7 target only from the explicit governed designation and fail on a missing, duplicate, ambiguous, or ineligible designation.  
   * Refresh Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256`.  
   * Refresh Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`.  
   * Refresh Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`.  
   * Refresh the Human Index, Machine Mirror, and related A7 artifacts in the same change.  
   * Capture GET, HEAD, conditional 304, writer/error, encoding-invariance, environment-gate, and composite proof artifacts.  
   * Preserve lower-case header names in structured snapshots.  
   * Write proof artifacts only in explicit proof-write mode.  
   * The A7 producer writes only its permitted primary proof artifacts; Existing: `tools/evidence/update_evidence_index.py` writes all Human Index, hash sentinel, Machine Mirror, checksum, and governed path-proof outputs.  
   * Provide non-writing `--check` mode.

   

3. Preserve transport semantics.  
     
   * Strong quoted ETag on success 200\.  
   * HEAD body empty and `Content-Length` equal to identity GET body length.  
   * 304 body empty and no `Content-Type` or `Content-Length`.  
   * `Vary: Authorization, Accept-Encoding`.  
   * Writers and errors `no-store`, no ETag.  
   * Encoding-invariant validator identity.  
   * No public route addition.

   

4. Use Existing: `artifacts/proofs/success_encoding_invariance.txt` (PF12 — HDE-Schemas & Artifacts) as the single encoding-invariance proof path.  
     
   * Do not create legacy `artifacts/proofs/encoding_invariance.txt` as a second home.  
   * Use the PF12 canonical encoding-invariance filename.

   

5. Add negative-path tests.  
     
   * Mismatched AB and BA bodies must fail.  
   * Failed canonical compare must make the top-level proof fail.  
   * Missing or ambiguous Catalog target must fail.  
   * Attempting to target `/internal/version` must fail.  
   * Malformed 304 headers must fail.

### Concrete anchors

* Existing: `docs/ENDPOINTS_CATALOG.json` (PF12 — HDE-Schemas & Artifacts).  
* Observed repo reality: `adapter/http_reader.py`.  
* Observed repo reality: `engine/runtime/public.py`.  
* Observed repo reality: `engine/cli/main.py`.  
* Planned output: `tools/evidence/generate_determinism_gate_proofs.py`.  
* Planned output: `tools/evidence/generate_a7_transport_proofs.py`.  
* Planned test path: `tests/evidence/test_determinism_gate_proofs.py`.  
* Planned test path: `tests/transport/test_a7_transport_proofs.py`.  
* Existing endpoint: `/reader` (PF05 — HDE-CLI-API-Vendor-Ref).  
* Existing endpoint: `/internal/version` (PF04 — HDE-Governance).

### Evidence outputs

* Planned output: `audit/gates/parity/reader_cli/ab.json`.  
* Planned output: `audit/gates/parity/reader_cli/ab.json.path_proof.txt`.  
* Planned output: `audit/gates/parity/reader_cli/ba.json`.  
* Planned output: `audit/gates/parity/reader_cli/ba.json.path_proof.txt`.  
* Planned output: `audit/gates/parity/reader_cli/summary.json`.  
* Planned output: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`.  
* Planned output: `audit/gates/determinism/abba.bytes`.  
* Planned output: `audit/gates/determinism/abba.bytes.path_proof.txt`.  
* Planned output: `audit/gates/determinism/tworun_identity.sha256`.  
* Planned output: `audit/gates/determinism/tworun_identity.sha256.path_proof.txt`.  
* Existing and regenerated output: `audit/gates/canonical_json/json_canon_compare.log`.  
* Planned output: `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`.  
* Planned output: `artifacts/cards/a3/IDENTITY_OK.txt`.  
* Planned output: `artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt`.  
* Documentation-drain candidate only: normalize the PF09.6 mixed-case `A3` directory spelling to lowercase; drainage is not an execution blocker.  
* Existing and regenerated output: `artifacts/reader/endpoints_snapshot.json`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`.  
* Existing and regenerated output: `artifacts/proofs/endpoints_env_gate_proof.log`.  
* Existing and regenerated output: `artifacts/proofs/success_get.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_head.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_304.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_writers_errors.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_encoding_invariance.txt`.  
* Existing and regenerated output: `artifacts/proofs/reader_success_get_head_304.json`.  
* Existing and regenerated evidence ledgers and path proofs from PR-01.

### Acceptance tokens

* `PREIMAGE_RECOMPUTE_OK`  
* `CLI_READER_PARITY_OK`  
* `COMPOSITE_ABBA_IDENTITY_OK`  
* `TWO_RUN_IDENTITY_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `A7_GET_QUOTED_ETAG_OK`  
* `A7_HEAD_PARITY_OK`  
* `A7_304_OMITS_CT_CL_OK`  
* `A7_VARY_AUTH_AE_OK`  
* `A7_ENCODING_INVARIANCE_OK`  
* `A7_TRANSPORT_PROOF_OK`  
* `ENDPOINTS_CATALOG_OK`  
* `ENDPOINTS_CATALOG_ENV_GATE_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`

These are planned claims subject to later QA and acceptance binding. The PR does not declare satisfaction.

### Rails posture

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`  
* Local Reader harness only.  
* No vendor call.  
* No external service.  
* No `/internal/version` A7 use.

### Basic QA check \+ pass condition

Basic QA check:

* Run `python -m pytest` against Planned test path: `tests/evidence/test_determinism_gate_proofs.py`.  
* Run `python -m pytest` against Planned test path: `tests/transport/test_a7_transport_proofs.py`.  
* Run Existing test path: `tests/cli/test_cli_canonical_bytes.py`.  
* Run Existing test path: `tests/cli/test_showcompat_parity_and_identity.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py`.  
* Run Planned command: `python tools/evidence/generate_determinism_gate_proofs.py --check`.  
* Run Planned command: `python tools/evidence/generate_a7_transport_proofs.py --check`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python tools/evidence/validate_evidence_paths.py`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.

Pass condition:

* Every determinism predicate is true.  
* Catalog target selection is unique and current.  
* `/internal/version` is rejected as A7.  
* GET, HEAD, 304, writer/error, encoding, and environment-gate proofs validate.  
* All primary artifacts are indexed and path-proven.  
* No public route or payload change.

### PO inputs

None.

### Codex Prompt

Implement HDE-EPIC038 PR-02 in the current repository.

This is closed-rails repository work. Do not access external services, edit PF-Canon, perform OPS, add public routes, use `/internal/version` as an A7 surface, claim QA PASS, or claim token satisfaction.

PF09.6 scope:

* HDE-DIST001.1 — preimage recompute, Reader-to-CLI parity, AB-to-BA identity, two-run identity, and canonical JSON compare.  
* HDE-DIST001.2 — complete Catalog-driven A7 transport proof.

PF14 anchors:

* HDE-Mechanics Guide §9.2 Reader.  
* HDE-Mechanics Guide A7 proof boundary.  
* HDE-Mechanics Guide §1.3.1 focused A7 proof-writer exception.

Inspect first:

* Existing: `docs/ENDPOINTS_CATALOG.json` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `docs/ENDPOINTS_CATALOG.json.sha256` (PF12 — HDE-Schemas & Artifacts).  
* Observed repo reality: `adapter/http_reader.py`.  
* Observed repo reality: `engine/runtime/public.py`.  
* Observed repo reality: `engine/cli/main.py`.  
* Existing artifact root: `artifacts/proofs/`.  
* Existing gate root: `audit/gates/`.  
* Existing tests root: `tests/transport/`.  
* Existing tests root: `tests/cli/`.

Revalidate current repo reality before editing. The current Catalog has an empty `success_endpoints` array, no `generated_at_utc`, no Boolean `internal` field, and method arrays on the `/reader` and `/internal/version` rows.

Repair Existing: `docs/ENDPOINTS_CATALOG.json` to the PF12 minimum authoritative-catalog schema:

* add top-level `generated_at_utc`;  
* add Boolean `internal` to every endpoint record;  
* represent `method` as one string per endpoint record, splitting current method arrays into separate records while preserving route semantics;  
* populate the existing `success_endpoints` member with exactly one governed designation that resolves to `GET /reader`;  
* define and validate the existing `success_endpoints` member in the Catalog schema when no current validator defines it;  
* preserve `/internal/version` as `a7_eligible:false` and outside the governed designation;  
* do not create a second designation mechanism, inventory, route, or flag.

Create or consolidate these producers with explicit write and non-writing `--check` modes:

* Planned output: `tools/evidence/generate_determinism_gate_proofs.py`.  
* Planned output: `tools/evidence/generate_a7_transport_proofs.py`.

Create these exact test files:

* Planned test path: `tests/evidence/test_determinism_gate_proofs.py`.  
* Planned test path: `tests/transport/test_a7_transport_proofs.py`.

The tests must cover mismatched AB and BA bodies, failed canonical comparison, missing or ambiguous Catalog designation, attempts to target `/internal/version`, malformed HEAD posture, and malformed 304 posture.

Generate or refresh this complete PR-02 output inventory:

* Planned output: `audit/gates/parity/reader_cli/ab.json`.  
* Planned output: `audit/gates/parity/reader_cli/ab.json.path_proof.txt`.  
* Planned output: `audit/gates/parity/reader_cli/ba.json`.  
* Planned output: `audit/gates/parity/reader_cli/ba.json.path_proof.txt`.  
* Planned output: `audit/gates/parity/reader_cli/summary.json`.  
* Planned output: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`.  
* Planned output: `audit/gates/determinism/abba.bytes`.  
* Planned output: `audit/gates/determinism/abba.bytes.path_proof.txt`.  
* Planned output: `audit/gates/determinism/tworun_identity.sha256`.  
* Planned output: `audit/gates/determinism/tworun_identity.sha256.path_proof.txt`.  
* Existing and regenerated output: `audit/gates/canonical_json/json_canon_compare.log`.  
* Planned output: `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`.  
* Planned output: `artifacts/cards/a3/IDENTITY_OK.txt`.  
* Planned output: `artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`.  
* Existing and regenerated output: `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`.  
* Existing and regenerated output: `artifacts/reader/endpoints_snapshot.json`.  
* Existing and regenerated output: `artifacts/proofs/endpoints_env_gate_proof.log`.  
* Existing and regenerated output: `artifacts/proofs/success_get.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_head.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_304.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_writers_errors.txt`.  
* Existing and regenerated output: `artifacts/proofs/success_encoding_invariance.txt`.  
* Existing and regenerated output: `artifacts/proofs/reader_success_get_head_304.json`.  
* Existing and regenerated output: `docs/evidence/INDEX.json`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256`.

Use Existing: `artifacts/proofs/success_encoding_invariance.txt` as the only encoding-invariance proof path. Do not create `artifacts/proofs/encoding_invariance.txt`.

The A7 producer writes only its permitted primary proof artifacts. Existing: `tools/evidence/update_evidence_index.py` writes all Human Index, hash sentinel, Machine Mirror, checksum, and governed path-proof outputs.

Run under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

Generate and validate with these exact commands:

* `python tools/evidence/generate_determinism_gate_proofs.py`  
* `python tools/evidence/generate_a7_transport_proofs.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python -m pytest tests/evidence/test_determinism_gate_proofs.py`  
* `python -m pytest tests/transport/test_a7_transport_proofs.py`  
* `python -m pytest tests/cli/test_cli_canonical_bytes.py`  
* `python -m pytest tests/cli/test_showcompat_parity_and_identity.py`  
* `python tools/evidence/generate_determinism_gate_proofs.py --check`  
* `python tools/evidence/generate_a7_transport_proofs.py --check`  
* `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python ci/checks/check_mirror_schema.sh`

PASS means every listed command exits 0; the Catalog contains exactly one governed `GET /reader` designation; every endpoint record satisfies the minimum field schema; `/internal/version` remains ineligible; every deterministic comparison is true; every A7 predicate validates; and every primary artifact is indexed and path-proven. FAIL means any schema field, designation, predicate, artifact, test, checksum, or evidence binding is absent, ambiguous, stale, or false.

## PR-03 — Reusable CI rails gates

### Intent

Turn the current EPIC031-scoped fixture jobs into reusable current rails gates while keeping live calls forbidden in CI and preserving deterministic refusal, retry/backoff, typed 429, and keys-only logging.

### IG source items

* Deliverable D7 — CI rails gates.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.3.

“Run CI pipelines with rails CLOSED by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).”

“Under closed rails, vendor and external HTTP calls are not permitted; any attempt to reach a provider must return a typed, numeric-free refusal envelope instead of performing outbound I/O.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide HDAPI v2 rails and Live QA mechanics.

“Closed-rails mechanics MUST prove deterministic refusal and no outbound I/O when rails are closed.”

“Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task, not PR work and not QA substitution.”

### PF07 facts / gaps

* PF07-derived canonical vendor base key: `HD_API_BASE_URL`.  
* PF07-derived deprecated compatibility key: `HDAPI_BASE_URL`.  
* PF07-derived vendor credential key: `HD_API_KEY`.  
* PF07-derived geocoding credential key: `GEO_API_KEY`.  
* PF07-derived closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.  
* PF07-derived open rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`.  
* PF07 gap: None.

### Observed repo reality

* Observed repo reality: `ci/jobs/rails_closed_refusal.yml` exists.  
    
  * Proof excerpt: `scope: hde-epic031-pr-01-local-deterministic`.  
  * Proof excerpt: `live_vendor_calls: forbidden`.


* Observed repo reality: `ci/jobs/rails_open_conformance.yml` exists.  
    
  * Proof excerpt: `scope: hde-epic031-pr-01-fixture-backed-only`.  
  * Proof excerpt: `live_vendor_calls: forbidden`.


* Observed repo reality: `ci/jobs/logs_keys_only_redaction.yml` exists.  
    
  * Proof excerpt: current job runs a PR-specific generator.


* Observed repo reality: current jobs remain tied to HDE-EPIC031 labels and do not yet express a reusable Distillation gate family.

### Observed audit provenance

* Observed audit provenance: the three CI job files and supporting local tests were present.  
* Observed audit provenance: deterministic retry/backoff behavior was not fully established across the complete current provider policy surface.

### Discovery

* Read-only discovery command for Observed repo reality: `cat ci/jobs/rails_closed_refusal.yml`.  
* Read-only discovery command for Observed repo reality: `cat ci/jobs/rails_open_conformance.yml`.  
* Read-only discovery command for Observed repo reality: `cat ci/jobs/logs_keys_only_redaction.yml`.  
* Read-only discovery command for Existing workflow: `grep -n -F 'rails_closed_refusal' .github/workflows/ci.yml`.  
* Read-only discovery command for Existing provider tests: `find tests/bodygraph -type f -print | sort`.  
* Read-only discovery command for Existing log generators: `find tools/evidence -type f -print | grep -E 'rails|log_posture|redaction' | sort`.  
* Read-only discovery command for Existing refusal proof: `find artifacts audit -type f -print | grep -E 'refusal|retry_after|keys_only' | sort`.

### Implementation requirements

1. Generalize Observed repo reality path: `ci/jobs/rails_closed_refusal.yml`.  
     
   * Replace epic-specific scope text with a reusable HDE closed-rails gate identity.  
   * Keep live calls forbidden.  
   * Prove refusal before input resolution and before outbound I/O.  
   * Include deterministic environment pins.

   

2. Generalize Observed repo reality path: `ci/jobs/rails_open_conformance.yml`.  
     
   * Keep it fixture-backed and local.  
   * Do not perform a live vendor call.  
   * Prove closed retry family, integer parameters, and no jitter.  
   * Retry only network errors and 5xx.  
   * Do not retry 429 or other 4xx.  
   * Prove deterministic `Retry-After` parsing.

   

3. Generalize Observed repo reality path: `ci/jobs/logs_keys_only_redaction.yml`.  
     
   * Replace the EPIC031-only generator dependency with the current reusable producer or extend that producer to a generic check mode.  
   * Prove no request body, response body, raw header value, bearer token, API key, birth data, or unbounded label in governed samples.

   

4. Create or consolidate Planned output: `tools/evidence/generate_rails_gate_evidence.py`.  
     
   * Produce the PF12 refusal proof.  
   * Produce deterministic retry/backoff and redaction summaries without live calls.  
   * Provide write and `--check` modes.  
   * Fail if any forbidden output is detected.

   

5. Wire the three job definitions into Existing workflow: `.github/workflows/ci.yml`.  
     
   * Closed rails remain the default.  
   * The fixture-backed open policy job must state that it is not live conformance.  
   * No secret requirement for these CI jobs.

   

6. Preserve all public and runtime contracts.  
     
   * No endpoint change.  
   * No vendor route change.  
   * No new token.  
   * No open-rails external action.

### Concrete anchors

* Observed repo reality: `ci/jobs/rails_closed_refusal.yml`.  
* Observed repo reality: `ci/jobs/rails_open_conformance.yml`.  
* Observed repo reality: `ci/jobs/logs_keys_only_redaction.yml`.  
* Existing: `.github/workflows/ci.yml` (PF06 — Epic-Process-Guide process surface).  
* Planned output: `tools/evidence/generate_rails_gate_evidence.py`.  
* Observed repo reality: `tests/bodygraph/test_resolver_vendor.py`.  
* Observed repo reality: `tests/bodygraph/test_vendor_client.py`.

### Evidence outputs

* Planned output: `artifacts/proofs/ops_refusal_proof.txt`.  
* Planned output: `artifacts/proofs/ops_refusal_proof.txt.path_proof.txt`.  
* Existing and regenerated output: `artifacts/vendor/retry_after_parse.log`.  
* Planned output: `artifacts/vendor/retry_after_parse.log.path_proof.txt`.  
* Existing and regenerated output: `artifacts/bodygraph/keys_only.logs.sample`.  
* Existing and regenerated output: `artifacts/bodygraph/keys_only.logs.sample.path_proof.txt`.  
* Existing and regenerated evidence ledgers and checksums from PR-01.

### Acceptance tokens

* `ENV_RAILS_POLICY_OK`  
* `ENV_LC_ALL_C_OK`  
* `NO_EXTERNAL_IO_ON_REFUSAL_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`

These are planned claims only.

### Rails posture

* CI closed gate: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.  
* Fixture-backed policy gate: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, with `live_vendor_calls: forbidden`.  
* Determinism: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* No secret values.  
* No external call.

### Basic QA check \+ pass condition

Basic QA check:

* Run Existing test path: `tests/bodygraph/test_resolver_vendor.py`.  
* Run Existing test path: `tests/bodygraph/test_vendor_client.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py`.  
* Run Planned command: `python tools/evidence/generate_rails_gate_evidence.py --check`.  
* Run Planned command: `python -m pytest tests/evidence/test_rails_ci_workflow_integration.py -q`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.

Pass condition:

* The dedicated `rails-policy-gates` workflow job invokes all three reusable job definitions through Planned output: `ci/checks/run_rails_job_definitions.py`.  
* The workflow job defaults to `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
* The fixture-backed open-policy definition remains explicitly non-live with `live_vendor_calls: forbidden`.  
* The workflow job and all three definitions require no secrets.  
* Closed rails prove no outbound I/O.  
* Open policy remains fixture-backed.  
* Retry and backoff are bounded and jitter-free.  
* 429 and other 4xx are not retried.  
* Logs and evidence are keys-only and secret-free.  
* All targeted tests, producers, workflow-integration checks, and evidence checks exit 0\.

### PO inputs

None for PR execution. Any later live open-rails confirmation remains PO-only and is not part of this PR.

### Codex Prompt

Implement HDE-EPIC038 PR-03.

Map the work to PF09.6 HDE-DIST001.3 and use HDE-Mechanics Guide HDAPI rails mechanics as the mechanics authority.

Inspect first:

* Observed repo reality: `ci/jobs/rails_closed_refusal.yml`.  
* Observed repo reality: `ci/jobs/rails_open_conformance.yml`.  
* Observed repo reality: `ci/jobs/logs_keys_only_redaction.yml`.  
* Existing workflow: `.github/workflows/ci.yml`.  
* Observed repo reality: `tests/bodygraph/test_resolver_vendor.py`.  
* Observed repo reality: `tests/bodygraph/test_vendor_client.py`.  
* Existing evidence and tool roots: `artifacts/proofs/`, `artifacts/vendor/`, `artifacts/bodygraph/`, and `tools/evidence/`.

Generalize the three current epic-scoped job definitions into reusable current gates. Keep all CI calls local and fixture-backed. Closed rails must prove no outbound I/O. Fixture-backed open policy must prove deterministic retry/backoff and 429 behavior without contacting a vendor.

Create or consolidate Planned output: `tools/evidence/generate_rails_gate_evidence.py`.

Create Planned output: `ci/checks/run_rails_job_definitions.py` as the single CI integration mechanism for this gate family.

The runner must:

* Load exactly the job-definition files supplied on its command line.  
* Validate each definition’s `name`, `rails`, `scope`, `live_vendor_calls`, and `steps` structure before execution.  
* Require the exact gate identities `rails_closed_refusal`, `rails_open_conformance`, and `logs_keys_only_redaction`.  
* Reject any remaining `hde-epic031` scope identity.  
* Require `live_vendor_calls: forbidden` for every definition.  
* Apply each definition’s declared rails and determinism environment only to that definition’s local subprocess commands.  
* Execute every declared step command in source order and stop on the first nonzero result.  
* Reject secret declarations, secret-value inputs, and workflow secret references.  
* Perform no external-service call and emit no secret or payload value.

Update Existing workflow: `.github/workflows/ci.yml` with one dedicated job whose job ID is `rails-policy-gates`.

The workflow job must:

* Default to `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
* Use the repository’s existing checkout, Python setup, dependency installation, and editable-install posture.  
* Require no `secrets:` mapping and contain no `${{ secrets.` reference.  
* Execute all three definitions through exactly this one command:

   `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml`

* Permit the open-policy definition’s declared `SAFE_MODE=0` and `ALLOW_NETWORK=1` only for its local mocked or fixture-backed command while retaining `live_vendor_calls: forbidden`.  
* Propagate any definition-validation or step-command failure as a failed CI job.

Create Planned test path: `tests/evidence/test_rails_ci_workflow_integration.py`.

The fixed integration test must prove:

* Existing workflow: `.github/workflows/ci.yml` contains the `rails-policy-gates` job.  
* That job invokes Planned output: `ci/checks/run_rails_job_definitions.py` with all three exact definition paths, each exactly once.  
* The workflow job’s default rails and determinism environment is closed and pinned.  
* Each definition’s `name` matches its required reusable gate identity.  
* No definition retains an `hde-epic031` scope identity.  
* The open-policy scope remains explicitly fixture-backed and non-live.  
* Every definition retains `live_vendor_calls: forbidden`.  
* Neither the workflow job nor any definition requires a secret or references a workflow secret.  
* The runner rejects an unknown gate identity, a non-forbidden live-call posture, a secret declaration, and a nonzero step result.

Produce:

* Planned output: `artifacts/proofs/ops_refusal_proof.txt`.  
* Existing and regenerated output: `artifacts/vendor/retry_after_parse.log`.  
* Existing and regenerated output: `artifacts/bodygraph/keys_only.logs.sample`.

Generate all sibling path proofs and evidence-ledger changes through the canonical evidence updater.

Do not add live vendor calls, secrets, new routes, public payload changes, or new acceptance tokens.

Run these exact commands under the declared rails:

* `python -m pytest tests/bodygraph/test_resolver_vendor.py tests/bodygraph/test_vendor_client.py -q`  
* `python tools/evidence/generate_rails_gate_evidence.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python -m pytest tests/evidence/test_rails_ci_workflow_integration.py -q`  
* `python tools/evidence/generate_rails_gate_evidence.py --check`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python ci/checks/check_mirror_schema.sh`

PASS means all listed commands exit 0; the `rails-policy-gates` workflow job executes all three reusable definitions through the single runner; closed rails remain the workflow default; the open-policy gate remains fixture-backed and explicitly non-live; no secrets are required; closed rails prove zero outbound I/O; retry and backoff remain bounded and jitter-free; 429 and other 4xx responses are not retried; redaction checks find no prohibited material; and all evidence bindings validate. FAIL means any command is nonzero, any gate definition is not wired, the workflow default is not closed, the open-policy gate permits a live call, any secret is required, retry policy is unbounded or jittered, 429 is retried, prohibited data appears, or evidence validation fails.

## PR-04 — DB, BodyGraph, bridge, and architecture posture harness

### Intent

Complete the deterministic local mechanics and evidence producers for DB runtime posture, BodyGraph source and policy behavior, direct-versus-bridge parity, environment connectivity, and a keys-only architecture snapshot.

### IG source items

* Deliverable D8 — DB posture runtime checks.  
* Deliverable D9 — BodyGraph mechanics gates.  
* Deliverable D10 — DB-bridge parity and environment connectivity.  
* Deliverable D11 — Architecture snapshot evidence.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.4.

“Use the Distillation harness to prove and exercise the DB runtime posture defined in Task HDE-FERM004 — Database Runtime Posture for this phase, without redefining posture semantics.”

PF09 subtask ID: HDE-DIST001.5.

“When verified here, prove BodyGraph behavior: Source selection and invariance across AB/BA.”

PF09 subtask ID: HDE-DIST001.9.

“Prove parity between direct DB reads and bridge-mediated reads for BodyGraph, and capture the associated environment connectivity posture.”

PF09 subtask ID: HDE-DIST001.10.

“Capture and index a keys-only architecture snapshot that reflects the Engine’s public and internal surfaces without exposing secrets or raw payloads.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide BodyGraph I/O seam.

Observed repo reality path in the quoted line: `engine/bodygraph/`.

“BodyGraph vendor and DB I/O is permitted only within the BodyGraph seam currently implemented under engine/bodygraph/ in this repo.”

“Any network or DB I/O in the BodyGraph seam MUST respect SAFE\_MODE and ALLOW\_NETWORK rails and keep logs and artifacts secret-free.”

PF14 anchor: HDE-Mechanics Guide §20.1 DB posture mechanics.

“Objective. Capture the runtime DB schema, roles/grants, and boundary view posture in a deterministic way.”

PF14 anchor: HDE-Mechanics Guide §20.3 Bridge parity mechanics.

“Objective. Prove parity between direct DB reads and bridge-mediated reads and capture env connectivity posture.”

PF14 anchor: HDE-Mechanics Guide architecture boundary-proof mechanics.

“Boundary-proof mechanics for the HDAPI vendor seam MUST use a conservative, fail-closed posture.”

“The evidence renderer may render analyzer output into governed artifacts, path proofs, and index or mirror rows, but MUST NOT independently decide architecture-boundary truth.”

### PF07 facts / gaps

* PF07-derived provider: Railway.  
* PF07-derived project: `ample-illumination`.  
* PF07-derived HD Engine service: `glow-hdengine-v2`.  
* PF07-derived database instance: `ample-illumination/production/postgres`.  
* PF07-derived database schema: `hde`.  
* PF07-derived exact search path: `hde, public`.  
* PF07-derived primary DB key: `DATABASE_URL`.  
* PF07-derived bridge key: `DB_BRIDGE_URL`.  
* PF07-derived production bridge override: `DB_ALLOW_BRIDGE_IN_PROD`.  
* PF07-derived production-like values: `prod`, `production`, `live`.  
* PF07-derived dev fallback order: `DATABASE_URL` then `DB_BRIDGE_URL` then typed error.  
* PF07 gap: None for the known provider, service, DB, schema, and key names.  
* Repo-observed existing governed boundary-view family: Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`; Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
* Resolved plan-local path decision for the remaining new outputs: Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json`; Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`; Planned schema: `schemas/architecture_snapshot.keys_only.v1.json`. These remaining paths are planned outputs under existing governed roots, not alternate homes.

### Observed repo reality

* Observed repo reality: `tools/evidence/generate_db_bridge_parity.py` exists.  
    
  * Proof excerpt: it produces `adapter_selection.snapshot.json`, `provider_parity.proof.json`, and environment connectivity artifacts.  
  * Proof excerpt: the current generator is labeled as HDE-EPIC032 PR-03 evidence.


* Observed repo reality: `artifacts/db/ddl_fingerprint.json` and its path proof exist.  
* Observed repo reality: `artifacts/runtime/env_connectivity.snapshot.json` exists.  
* Observed repo reality: `engine/bodygraph/resolver.py` and `engine/bodygraph/v2_adapter.py` exist.  
* Observed repo reality: `scripts/db/capture_epic011_posture.py` writes the current governed boundary-view primary artifact at `artifacts/db/boundary_view.readonly.proof.txt`.  
* Observed repo reality: `artifacts/db/boundary_view.readonly.proof.txt` and `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt` exist; the primary records both `hde.body_graphs_current` and `public.hde_body_graphs_current` as non-updatable and non-insertable, and `artifacts/evidence_index.jsonl` references the primary path.  
* Observed repo reality: `artifacts/architecture/architecture_snapshot.keys_only.json` was not found.  
* Read-only commands used: GitHub `fetch_file` for current files and current-path checks; GitHub exact-string search for the existing boundary-view proof path.

  ### **Observed audit provenance**

* Observed audit provenance: DB fingerprint, grants, schema, constraints, connectivity, BodyGraph source-selection, source-invariance, refresh, metrics, keys-only logging, and DB-bridge evidence were present.  
* Observed audit provenance: the prior audit reported the boundary-view and architecture snapshot artifacts as absent; current repo revalidation supersedes that boundary-view observation, while the architecture snapshot remains absent.  
* Observed audit provenance: the prior provider-parity generator contained fixture-backed and live-unavailable postures that must not be confused.

### Discovery

* Read-only discovery command for Existing DB paths: `find artifacts/db artifacts/db_bridge artifacts/runtime -type f -print | sort`.  
* Read-only discovery command for Existing BodyGraph evidence: `find artifacts/bodygraph -type f -print | sort`.  
* Read-only discovery command for Existing DB tooling: `find scripts/db tools/evidence -type f -print | sort`.  
* Read-only discovery command for Existing DB façade: `find engine/db -type f -print | sort`.  
* Read-only discovery command for Existing BodyGraph seam: `find engine/bodygraph -type f -print | sort`.  
* Read-only discovery command for Existing bridge generator: `sed -n '1,360p' tools/evidence/generate_db_bridge_parity.py`.  
* Read-only discovery command for Existing architecture analyzers: `find tools/evidence -type f -print | grep -E 'boundary|architecture|arch' | sort`.  
* Read-only discovery command for current route registrations: `grep -R -n -E 'route\\(|@bp\\.|Blueprint' adapter engine`.  
* Use existing producers where they already own an artifact family. Do not create duplicate generators for the same primary path.

### Implementation requirements

1. Complete the DB posture producer family.  
     
   * Reuse Observed repo reality path: `scripts/db/ddl_fingerprint.sh` where it remains canonical.  
   * Inspect Observed repo reality path: `scripts/db/capture_epic011_posture.py` as the current producer of the governed boundary-view primary artifact.  
   * Apply PF14 §1.3.1 Evidence jobs (single-writer tools): if `scripts/db/capture_epic011_posture.py` is reused or extended, remove or disable `_write_path_proof` and every direct governed path-proof write from the HDE-EPIC038 execution path.  
   * Remove or bypass the `_write_bytes` call path that invokes `_write_path_proof` for HDE-EPIC038 production. No HDE-EPIC038 DB-posture producer may construct or write a governed `*.path_proof.txt` transcript directly.  
   * The DB-posture producer must write only the primary boundary-view artifact at Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
   * Only Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide) may create or refresh Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
   * Create or consolidate Planned output: `tools/evidence/generate_db_runtime_posture.py` for the remaining DB-posture work; if boundary-view capture is consolidated there, preserve the existing primary and sibling identities and retain the same single-writer separation.  
   * Produce schema/search-path, grants, constraint, DDL fingerprint, boundary-view read-only, and environment-connectivity checks without minting a second boundary-view evidence path.  
   * Use only deterministic local or mocked providers in PR execution.  
   * Do not access privileged DB state in PR work.

   

2. Generalize Observed repo reality path: `tools/evidence/generate_db_bridge_parity.py`.  
     
   * Remove epic-specific authority language from generic outputs.  
   * Preserve fixture-backed local parity.  
   * Preserve explicit unavailable or skipped states for absent live providers.  
   * Never report parity PASS when an active direct or bridge row is missing, skipped, unavailable, or errored.  
   * Preserve `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` as non-token proof labels.

   

3. Complete BodyGraph proof production.  
     
   * Create or consolidate Planned output: `tools/evidence/generate_bodygraph_policy_proofs.py`.  
   * Prove current source selection and AB-to-BA source invariance.  
   * Validate refresh-policy shape against current worker policy.  
   * Validate rate-limit and circuit-breaker evidence.  
   * Preserve keys-only logs and metrics.  
   * Treat `BG_SOURCE_SELECTION_OK`, `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`, `BG_SOURCE_INVARIANCE_OK`, `BG_TTL_SWR_POLICY_OK`, `BG_RATE_LIMIT_POLICY_OK`, and `BG_CIRCUIT_BREAKER_POLICY_OK` as proof labels unless PF04 later admits them.

   

4. Create Planned output: `tools/evidence/generate_architecture_snapshot.py`.  
     
   * Separate analysis from rendering.  
   * Discover current engine, adapter, presenter, CLI, route, I/O seam, evidence-tool, and governed-artifact loci.  
   * Use a fail-closed taxonomy with `allowed`, `forbidden`, `unknown`, and `out_of_scope`.  
   * Produce keys and bounded classifications only.  
   * Exclude birth data, request bodies, response bodies, credentials, secret headers, environment values, and raw vendor payloads.  
   * Do not use the artifact as a new contract or public surface.

   

5. Reuse the current governed boundary-view family and use resolved plan-local paths for the remaining new outputs.  
     
   * Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
   * Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
   * Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json`.  
   * Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
   * Planned schema: `schemas/architecture_snapshot.keys_only.v1.json`.  
   * Do not create an alternate root or second evidence home.

   

6. Replace placeholder alias filenames with one exact synthetic evidence identity.  
     
   * Planned output: `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json`.  
   * Planned output: `artifacts/bodygraph/db_resolve.epic038_synthetic.json`.  
   * No real user identity, birth data, or vendor payload may appear.

   

7. Add deterministic tests for:  
     
   * DB posture output.  
   * Boundary-view proof classification.  
   * A regression assertion in Planned test path: `tests/evidence/test_db_runtime_posture.py` proving that the DB-posture producer does not create or modify `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt` directly.  
   * A regression assertion proving that Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide) creates or refreshes the final sibling path proof and binds it to `artifacts/db/boundary_view.readonly.proof.txt`.  
   * BodyGraph source and policy proof.  
   * Provider-parity false-PASS rejection.  
   * Architecture snapshot unknown/fail-closed handling.  
   * Keys-only and no-secret enforcement.  
   * 

### Concrete anchors

* Observed repo reality: `engine/db/`.  
* Observed repo reality: `engine/bodygraph/`.  
* Observed repo reality: `tools/evidence/generate_db_bridge_parity.py`.  
* Observed repo reality: `scripts/db/ddl_fingerprint.sh`.  
* Planned output: `tools/evidence/generate_db_runtime_posture.py`.  
* Planned output: `tools/evidence/generate_bodygraph_policy_proofs.py`.  
* Planned output: `tools/evidence/generate_architecture_snapshot.py`.  
* Planned test path: `tests/evidence/test_db_runtime_posture.py`.  
* Planned test path: `tests/evidence/test_bodygraph_policy_proofs.py`.  
* Planned test path: `tests/evidence/test_architecture_snapshot.py`.

### Evidence outputs

* Existing and regenerated output: `artifacts/db/ddl_fingerprint.json`.  
* Existing and regenerated output: `artifacts/db/grants.txt`.  
* Existing and regenerated output: `artifacts/db/check_schema.txt`.  
* Existing and regenerated output: `artifacts/db/check_constraints.txt`.  
* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
* Existing and regenerated output: `artifacts/runtime/env_connectivity.snapshot.json`.  
* Existing and regenerated output: `artifacts/runtime/env_connectivity.nondev_failure.json`.  
* Existing and regenerated output: `artifacts/bodygraph/source_selection.snapshot.json`.  
* Existing and regenerated output: `artifacts/bodygraph/source_invariance/ab.json`.  
* Existing and regenerated output: `artifacts/bodygraph/source_invariance/ba.json`.  
* Existing and regenerated output: `artifacts/bodygraph/source_invariance/summary.json`.  
* Existing and regenerated output: `artifacts/bodygraph/refresh_policy.snapshot.json`.  
* Existing and regenerated output: `artifacts/bodygraph/metrics.snapshot.json`.  
* Existing and regenerated output: `artifacts/bodygraph/keys_only.logs.sample`.  
* Planned output: `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json`.  
* Planned output: `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/db_resolve.epic038_synthetic.json`.  
* Planned output: `artifacts/bodygraph/db_resolve.epic038_synthetic.json.path_proof.txt`.  
* Existing and regenerated output: `artifacts/presenter/json_canon_compare.log`.  
* Existing and regenerated output: `artifacts/db_bridge/adapter_selection.snapshot.json`.  
* Existing and regenerated output: `artifacts/db_bridge/provider_parity.proof.json`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
* Existing and regenerated evidence ledgers and path proofs.

### Acceptance tokens

* `DB_RUNTIME_SEARCH_PATH_OK`  
* `DB_ROLE_OK`  
* `DB_SCHEMA_FINGERPRINT_OK`  
* `DB_CONN_ENV_OK`  
* `DEV_DB_BRIDGE_FALLBACK_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
* `EVIDENCE_PATH_PROOFS_OK`

Planned proof obligations without token claims:

* BodyGraph source selection.  
* BodyGraph vendor-disabled production posture.  
* BodyGraph source invariance.  
* BodyGraph TTL and stale-while-revalidate posture.  
* BodyGraph rate-limit posture.  
* BodyGraph circuit-breaker posture.  
* Direct-provider parity.  
* Bridge capability.  
* Architecture snapshot keys-only posture.

### Rails posture

* PR execution uses `SAFE_MODE=1`, `ALLOW_NETWORK=0`.  
* All DB/provider behavior in PR tests is local, fixture-backed, or mocked.  
* `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* No live DB call.  
* No live bridge call.  
* No vendor call.  
* No raw data or secrets.

### Basic QA check \+ pass condition

Basic QA check:

* Run Planned test path: `tests/evidence/test_db_runtime_posture.py`.  
* Run Planned test path: `tests/evidence/test_bodygraph_policy_proofs.py`.  
* Run Planned test path: `tests/evidence/test_architecture_snapshot.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py`  
* Run Planned command: `python tools/evidence/generate_db_runtime_posture.py --check`.  
* Run Existing command: `python tools/evidence/generate_db_bridge_parity.py --check`.  
* Run Planned command: `python tools/evidence/generate_bodygraph_policy_proofs.py --check`.  
* Run Planned command: `python tools/evidence/generate_architecture_snapshot.py --check`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python tools/evidence/validate_evidence_paths.py`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.

Pass condition:

* DB posture outputs are deterministic, canonical, and secret-free.  
* Boundary view is classified read-only.  
* BodyGraph policy and invariance predicates are true.  
* Provider parity cannot falsely pass unavailable rows.  
* Architecture snapshot is keys-only and fail-closed on unknowns.  
* All evidence bindings validate.

### PO inputs

None for PR execution. OPS-01 supplies live DB and bridge observations later.

### Codex Prompt

Implement HDE-EPIC038 PR-04 under closed rails.

PF09.6 mappings:

* HDE-DIST001.4 — DB posture runtime harness.  
* HDE-DIST001.5 — BodyGraph source and policy proofs.  
* HDE-DIST001.9 — direct DB and bridge parity with environment connectivity.  
* HDE-DIST001.10 — keys-only architecture snapshot.

PF14 anchors:

* BodyGraph I/O seam.  
* §20.1 DB posture mechanics.  
* §20.3 Bridge parity mechanics.  
* HDAPI boundary analyzer and renderer separation.

PF07 facts:

* Provider: Railway.  
* Project: `ample-illumination`.  
* Service: `glow-hdengine-v2`.  
* DB instance: `ample-illumination/production/postgres`.  
* DB schema: `hde`.  
* Search path: `hde, public`.  
* Primary DB key: `DATABASE_URL`.  
* Bridge key: `DB_BRIDGE_URL`.  
* Production bridge override: `DB_ALLOW_BRIDGE_IN_PROD`.  
* Production-like values: `prod`, `production`, `live`.

Inspect first:

* Observed repo reality: `engine/db/`.  
* Observed repo reality: `engine/bodygraph/`.  
* Observed repo reality: `tools/evidence/generate_db_bridge_parity.py`.  
* Observed repo reality: `scripts/db/ddl_fingerprint.sh`.  
* Existing artifact families: `artifacts/db/`, `artifacts/db_bridge/`, `artifacts/runtime/`, `artifacts/bodygraph/`, and `artifacts/presenter/`.  
* Existing tests under `tests/db/`, `tests/bodygraph/`, and `tests/evidence/`.

Reuse existing canonical producers. Implement deterministic local posture evidence without contacting DB, bridge, or vendor services. Generalize the existing DB-bridge generator so unavailable live rows remain unavailable and can never be reported as parity PASS.

Before changing DB-posture tooling, inspect Existing: `scripts/db/capture_epic011_posture.py` as the current producer of the governed boundary-view primary artifact.

Apply PF14 §1.3.1 Evidence jobs (single-writer tools):

* If `scripts/db/capture_epic011_posture.py` is reused or extended, remove or disable `_write_path_proof` and every direct governed path-proof write from the HDE-EPIC038 execution path.  
* Remove or bypass the `_write_bytes` behavior that invokes `_write_path_proof` for HDE-EPIC038 production.  
* No HDE-EPIC038 DB-posture producer may construct, create, refresh, or modify a governed `*.path_proof.txt` transcript directly.  
* The DB-posture producer must write only Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
* Only Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide) may create or refresh Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
* Preserve both existing path identities and do not mint a second boundary-view evidence home.

Create or consolidate these exact producer paths:

* Planned output: `tools/evidence/generate_db_runtime_posture.py`.  
* Planned output: `tools/evidence/generate_bodygraph_policy_proofs.py`.  
* Planned output: `tools/evidence/generate_architecture_snapshot.py`.

Use this exact primary and sibling ownership:

* DB-posture producer output: Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
* Canonical evidence-updater output: Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.

Add regression coverage to Planned test path: `tests/evidence/test_db_runtime_posture.py` proving that:

* running the DB-posture producer without the canonical updater does not create or modify the sibling path proof;  
* running Existing: `tools/evidence/update_evidence_index.py` creates or refreshes the sibling proof and binds it to the final primary artifact; and  
* no alternative boundary-view primary or sibling path is created.

Keep the existing command order: all primary producer write commands run first, then `python tools/evidence/update_evidence_index.py`, then the producer check modes, updater check mode, and path validation.

Create these remaining exact planned outputs under existing governed roots:

* Planned output: `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json`.  
* Planned output: `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/db_resolve.epic038_synthetic.json`.  
* Planned output: `artifacts/bodygraph/db_resolve.epic038_synthetic.json.path_proof.txt`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
* Planned schema: `schemas/architecture_snapshot.keys_only.v1.json`.

Do not create an alternate root or second evidence home. The architecture analyzer must determine truth; the renderer may only serialize analyzer output. The architecture snapshot must use the fail-closed classifications `allowed`, `forbidden`, `unknown`, and `out_of_scope`, and must exclude secrets, birth data, request bodies, response bodies, secret headers, environment values, and raw vendor payloads.

Preserve these labels as non-token proof obligations unless PF04 explicitly registers them: `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, `DB_BRIDGE_FALLBACK_OK`, `BG_SOURCE_SELECTION_OK`, `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`, `BG_SOURCE_INVARIANCE_OK`, `BG_TTL_SWR_POLICY_OK`, `BG_RATE_LIMIT_POLICY_OK`, and `BG_CIRCUIT_BREAKER_POLICY_OK`.

Create these exact tests:

* Planned test path: `tests/evidence/test_db_runtime_posture.py`.  
* Planned test path: `tests/evidence/test_bodygraph_policy_proofs.py`.  
* Planned test path: `tests/evidence/test_architecture_snapshot.py`.

Generate and validate with these exact commands under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`:

* `python tools/evidence/generate_db_runtime_posture.py`  
* `python tools/evidence/generate_db_bridge_parity.py`  
* `python tools/evidence/generate_bodygraph_policy_proofs.py`  
* `python tools/evidence/generate_architecture_snapshot.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python -m pytest tests/evidence/test_db_runtime_posture.py`  
* `python -m pytest tests/evidence/test_bodygraph_policy_proofs.py`  
* `python -m pytest tests/evidence/test_architecture_snapshot.py`  
* `python tools/evidence/generate_db_runtime_posture.py --check`  
* `python tools/evidence/generate_db_bridge_parity.py --check`  
* `python tools/evidence/generate_bodygraph_policy_proofs.py --check`  
* `python tools/evidence/generate_architecture_snapshot.py --check`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python ci/checks/check_mirror_schema.sh`

PASS means every listed command exits 0, DB posture outputs are deterministic and secret-free, the boundary view is classified read-only, BodyGraph policy predicates are true, unavailable provider rows cannot falsely pass, the architecture snapshot is keys-only and fail-closed on unknowns, and every governed artifact is indexed and path-proven. FAIL means any command is nonzero, a provider row is misclassified, a secret or payload is exposed, an unknown is silently passed, an exact planned output is absent, or evidence validation fails.

## PR-05 — Configured-v2 mapped-cache persistence

### Intent

Implement safe durable persistence of adapter-mapped HDE BodyGraph/cache data for configured-v2 chart-backed resolution, while retaining closed-rails refusal, explicit legacy fallback, and a hard production-like write guard.

### IG source items

* Deliverable D12 — v2 mapped-cache persistence hardening.

IG Approved:

"PF09 completion: Complete in this epic"  
"\* Notes: Optional row planned in this epic as controlled mapped-cache persistence hardening. PF09 status remains unchanged until later PO-governed status drainage."

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.11.

“Implement and prove a durable mapped-cache persistence path for configured-v2 chart-backed BodyGraph resolution in non-prod or controlled rails before any production-facing write posture is considered.”

“The path must write adapter-mapped HDE BodyGraph/cache payloads, not raw HumanDesignAPI v2 ChartResult envelopes.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide configured-v2 mapped-cache boundary.

“For configured v2 vendor bases, non-dry-run mapped-cache writes MUST fail closed until a separately scoped mapped-cache persistence implementation and evidence chain exists.”

PF14 anchor: HDE-Mechanics Guide mapped-cache persistence mechanics.

“Future mapped-cache persistence mechanics, if implemented, MUST write adapter-mapped HDE BodyGraph/cache payloads, not raw HumanDesignAPI v2 envelopes.”

“The proof family must include mapped output before write, cached output after DB read, canonical-equivalence evidence for governed fields, idempotence evidence, no-secret and no-raw-vendor-payload evidence.”

### PF07 facts / gaps

* PF07-derived canonical vendor base key: `HD_API_BASE_URL`.  
* PF07-derived current vendor base: `https://api.humandesignapi.nl/v2`.  
* PF07-derived vendor key: `HD_API_KEY`.  
* PF07-derived geocoding key: `GEO_API_KEY`.  
* PF07-derived resource-path posture: version-neutral `charts`, `charts/simple`, and `charts/coordinates`.  
* PF07-derived database instance: `ample-illumination/production/postgres`.  
* PF07-derived database schema: `hde`.  
* PF07-derived DB key: `DATABASE_URL`.  
* PF07-derived production-like values: `prod`, `production`, `live`.  
* PF07 gap: no gap in provider, key, DB, or schema names.  
* Production mapped-cache authorization is intentionally absent and must remain absent.

### Observed repo reality

* Observed repo reality: `engine/bodygraph/v2_adapter.py` contains the deterministic ChartResult adapter.  
    
* Observed repo reality: `engine/bodygraph/resolver.py` routes configured-v2 dry-run through the version-neutral `charts` resource and the adapter.  
    
* Observed repo reality: configured-v2 non-dry-run returns `PROVIDER_WRITE_UNSUPPORTED`.  
    
  * Proof excerpt: `v2 chart-backed bg:resolve supports dry-run mapping only until mapped-cache persistence is implemented`.


* Observed repo reality: `engine/bodygraph/ingest.py` persists the vendor payload text for the legacy ingest path.  
    
  * Proof excerpt: def \_persist\_bodygraph(db: DBAccess, user\_id: str, vendor\_version: int, request: VendorRequest, payload\_text: str) \-\> int:  
  * This legacy raw-payload path must not be reused for configured-v2 mapped persistence.


* Observed repo reality: `artifacts/bodygraph/v2_mapped_cache/manifest.json` was not found.  
    
* Observed repo reality: no mapped-cache generator or mapped-cache tests were found during the prior static audit.  
    
* Read-only commands used: current GitHub `fetch_file` and exact path checks.

### Observed audit provenance

* Observed audit provenance: EPIC037 supplied adapter mapping, configured-v2 dry-run, no-raw-payload, route-policy, and compat foundations.  
* Observed audit provenance: no durable mapped-cache implementation, tests, generator, or evidence family existed.  
* Observed audit provenance: the resolver guard remained `PROVIDER_WRITE_UNSUPPORTED`.

### Discovery

* Read-only discovery command for Observed repo reality: `sed -n '1,340p' engine/bodygraph/v2_adapter.py`.  
* Read-only discovery command for Observed repo reality: `sed -n '1,360p' engine/bodygraph/resolver.py`.  
* Read-only discovery command for Observed repo reality: `sed -n '1,340p' engine/bodygraph/ingest.py`.  
* Read-only discovery command for Existing DB façade: `find engine/db -type f -print | sort`.  
* Read-only discovery command for Existing BodyGraph schema and migrations: `grep -R -n -F 'hde.body_graphs' migrations sql schemas engine tests`.  
* Read-only discovery command for Existing v2 tests: `find tests -type f -print | grep -E 'v2_adapter|bg_resolve|mapped_cache' | sort`.  
* Read-only discovery command for Existing v2 evidence: `find artifacts/vendor/hdapi_v2 tools/evidence -type f -print | sort`.  
* Read-only discovery command for duplicate write loci: `grep -R -n -E 'INSERT INTO hde\\.body_graphs|body_graphs_current' engine scripts tools tests`.  
* Stop rather than creating a second persistence home if current repo reality has introduced a sanctioned mapped-cache writer.

### Implementation requirements

1. Create Planned output: `engine/bodygraph/mapped_cache.py`.  
     
   * Accept only adapter-mapped HDE data.  
   * Validate UUID-compatible `user_id`.  
   * Validate integer `vendor_version`.  
   * Validate lower-case 64-hex `input_fingerprint`.  
   * Validate the mapped payload shape before persistence.  
   * Canonicalize governed payload fields through the shared serializer.  
   * Use the existing `hde.body_graphs` cache home and DBAccess façade.  
   * Do not introduce a second table or persistence root.  
   * Return a typed write/read-back result.

   

2. Update Observed repo reality path: `engine/bodygraph/resolver.py`.  
     
   * Pass explicit `upsert` intent into configured-v2 resolution.  
       
   * Preserve dry-run behavior.  
       
   * Permit mapped persistence only when:  
       
     * the existing `--upsert` intent is true;  
     * rails are open;  
     * APP\_ENV is not `prod`, `production`, or `live`;  
     * DB connectivity resolves through the sanctioned DBAccess path;  
     * adapter mapping succeeded.

     

   * Preserve typed refusal when any gate is absent.  
       
   * Preserve `PROVIDER_WRITE_UNSUPPORTED` or a narrower registered typed error for production-like or unapproved writes.  
       
   * Do not add a public flag or route.

   

3. Do not reuse the legacy raw-vendor persistence call in Observed repo reality path: `engine/bodygraph/ingest.py`.  
     
   * Shared low-level DB helper reuse is allowed only if the helper receives canonical adapter-mapped HDE data.  
   * Raw StandardResponse, ChartResult, request body, response body, headers, or secrets must never enter the stored payload.

   

4. Idempotence.  
     
   * Use the normalized `(user_id, vendor, vendor_version, input_fingerprint)` identity.  
   * Repeated writes must not create duplicates.  
   * Repeated writes must not diverge.  
   * Read-back bytes for governed fields must canonically equal mapped pre-write bytes.

   

5. Legacy fallback.  
     
   * Non-v2 configured bases retain explicit legacy BodyGraph behavior.  
   * Configured-v2 behavior must not silently fall back to legacy `bodygraphs`.  
   * Dual-route behavior remains unsupported unless separately authorized.

   

6. Production guard.  
     
   * `prod`, `production`, and `live` remain write-refused.  
   * PR-05 does not add production authorization.  
   * A future authorization decision remains separate.

   

7. Create Planned output: `tools/evidence/generate_v2_mapped_cache_evidence.py`.  
     
   * Fixture-backed write/read-back proof using an injected deterministic DB façade.  
   * No live vendor or DB call in PR execution.  
   * Write and `--check` modes.  
   * Fail if any lower-level predicate fails.  
   * Produce exactly these primary artifacts and schemas:  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.  
     * Planned schema: `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`.  
     * Planned schema: `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`.  
   * Require the canonical evidence updater to create these exact sibling proofs:  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log.path_proof.txt`.  
     * Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json.path_proof.txt`.

   

8. Create Planned output: `scripts/ops/hde_epic038_mapped_cache_smoke.py`.  
     
   * PO-only operator entrypoint.  
   * Must not run during PR checks.  
   * Require explicit open rails and explicit non-production-like APP\_ENV.  
   * Require presence-only secret checks.  
   * Emit redacted and bounded OPS outputs only.  
   * Never print raw vendor or birth payloads.

   

9. Add tests:  
     
   * adapter-mapped write/read-back.  
   * canonical equivalence.  
   * idempotent second write.  
   * raw envelope rejection.  
   * secret-like key rejection.  
   * closed-rails no-I/O refusal.  
   * missing-upsert refusal.  
   * production-like refusal.  
   * legacy fallback preservation.  
   * no second persistence home.  
   * evidence generator fail-closed behavior.

### Concrete anchors

* Observed repo reality: `engine/bodygraph/v2_adapter.py`.  
* Observed repo reality: `engine/bodygraph/resolver.py`.  
* Observed repo reality: `engine/bodygraph/ingest.py`.  
* Observed repo reality: `engine/db/`.  
* Planned output: `engine/bodygraph/mapped_cache.py`.  
* Planned output: `tools/evidence/generate_v2_mapped_cache_evidence.py`.  
* Planned output: `scripts/ops/hde_epic038_mapped_cache_smoke.py`.  
* Planned test path: `tests/bodygraph/test_v2_mapped_cache.py`.  
* Planned test path: `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`.  
* Planned test path: `tests/evidence/test_v2_mapped_cache_evidence.py`.

### Evidence outputs

* Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json.path_proof.txt`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`.  
* Existing and regenerated evidence ledgers and path proofs.

### Acceptance tokens

* `DB_CONN_ENV_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
* `EVIDENCE_PATH_PROOFS_OK`  
* `NO_EXTERNAL_IO_ON_REFUSAL_OK`

These are planned claims only. No new mapped-cache-specific token is introduced.

### Rails posture

PR execution:

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`  
* Fixture-backed DBAccess only.  
* No live vendor.  
* No live DB.  
* No production authorization.

Runtime implementation:

* Open rails are necessary but not sufficient for mapped writes.  
* Explicit `--upsert` intent is required.  
* Production-like APP\_ENV values remain refused.  
* Secrets and raw payloads are prohibited.

### Basic QA check \+ pass condition

Basic QA check:

* Run Planned test path: `tests/bodygraph/test_v2_mapped_cache.py`.  
* Run Planned test path: `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`.  
* Run Planned test path: `tests/evidence/test_v2_mapped_cache_evidence.py`.  
* Run Existing test path: `tests/bodygraph/test_v2_adapter.py`.  
* Run Existing test path: `tests/bodygraph/test_bg_resolve_route_policy.py`.  
* Run Existing test path: `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py`  
* Run Planned command: `python tools/evidence/generate_v2_mapped_cache_evidence.py --check`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python tools/evidence/validate_evidence_paths.py`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.

Pass condition:

* Only adapter-mapped HDE data reaches persistence.  
* Write/read-back canonical equivalence is true.  
* The second write is idempotent.  
* Closed rails perform no outbound I/O.  
* Production-like writes remain refused.  
* Legacy fallback remains explicit.  
* No raw request, response, envelope, secret, or birth payload is persisted or logged.  
* All evidence paths validate.

### PO inputs

None for PR execution. OPS-02 requires later PO authorization and secret presence.

### Codex Prompt

Implement HDE-EPIC038 PR-05 under PF09.6 HDE-DIST001.11.

This PR adds controlled configured-v2 mapped-cache persistence. It does not authorize production writes, change public Reader behavior, add routes, move vendor ownership, perform OPS, or claim QA PASS.

PF14 requirements:

* Configured-v2 non-dry-run writes currently fail closed.  
* New persistence must store adapter-mapped HDE BodyGraph/cache data, not raw HumanDesignAPI envelopes.  
* Required proofs include write/read-back parity, idempotence, no raw vendor persistence, no request/response persistence, no secrets, closed-rails refusal, and legacy fallback preservation.

Inspect first:

* Observed repo reality: `engine/bodygraph/v2_adapter.py`.  
* Observed repo reality: `engine/bodygraph/resolver.py`.  
* Observed repo reality: `engine/bodygraph/ingest.py`.  
* Observed repo reality: `engine/db/`.  
* Existing test path: `tests/bodygraph/test_v2_adapter.py`.  
* Existing test path: `tests/bodygraph/test_bg_resolve_route_policy.py`.  
* Existing test path: `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`.  
* Existing migrations and schema references for `hde.body_graphs`.

Create these exact implementation and operator paths:

* Planned output: `engine/bodygraph/mapped_cache.py`.  
* Planned output: `tools/evidence/generate_v2_mapped_cache_evidence.py`.  
* Planned output: `scripts/ops/hde_epic038_mapped_cache_smoke.py`.

Use the existing `hde.body_graphs` persistence home and DBAccess façade. Validate UUID-compatible `user_id`, integer `vendor_version`, and lower-case 64-hex `input_fingerprint`. Store only canonical adapter-mapped HDE data. Do not reuse the legacy raw-vendor payload persistence call for configured-v2 mapped data.

Update the resolver so configured-v2 persistence requires the existing explicit upsert intent, open rails, non-production-like APP\_ENV, successful adapter mapping, and available DBAccess. Preserve dry-run mapping. Refuse `prod`, `production`, and `live`. Do not silently fall back to legacy `bodygraphs`.

The operator script is PO-only, must not run in PR checks, must require explicit open rails and non-production-like APP\_ENV, and must emit only bounded redacted OPS output.

Create this exact mapped-cache artifact family:

* Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log.path_proof.txt`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json.path_proof.txt`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`.

Create these exact tests:

* Planned test path: `tests/bodygraph/test_v2_mapped_cache.py`.  
* Planned test path: `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`.  
* Planned test path: `tests/evidence/test_v2_mapped_cache_evidence.py`.

PR tests and evidence generation must remain fixture-backed and closed-rails. The operator script must not run in PR checks. Generate all governed path proofs and ledger changes through the canonical evidence updater.

Generate and validate with these exact commands:

* `python tools/evidence/generate_v2_mapped_cache_evidence.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python -m pytest tests/bodygraph/test_v2_mapped_cache.py`  
* `python -m pytest tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`  
* `python -m pytest tests/evidence/test_v2_mapped_cache_evidence.py`  
* `python -m pytest tests/bodygraph/test_v2_adapter.py`  
* `python -m pytest tests/bodygraph/test_bg_resolve_route_policy.py`  
* `python -m pytest tests/compat/test_hde_epic037_v2_adapter_to_compat.py`  
* `python tools/evidence/generate_v2_mapped_cache_evidence.py --check`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python ci/checks/check_mirror_schema.sh`

PASS means every listed command exits 0, mapped data alone is persisted, read-back is canonically equal, repeated writes are idempotent, closed-rails and production-like refusals hold, legacy fallback remains explicit, no raw request, response, envelope, secret, or birth payload is persisted or logged, and all evidence bindings validate. FAIL means any command is nonzero, raw vendor data can be stored, production-like writes are allowed, idempotence fails, a second persistence home appears, an exact artifact or schema is absent, or evidence validation fails.

## PR-06 — Release sanity orchestration and evidence binding

### Intent

Extend the one-button release sanity pipeline to drive all in-scope Distillation proof producers in deterministic order, validate already-produced OPS evidence without rerunning OPS, and finish the canonical evidence refresh.

### IG source items

* Deliverable D1 — Global discipline.  
* Deliverable D8 — DB posture runtime checks.  
* Deliverable D9 — BodyGraph mechanics gates.  
* Deliverable D10 — DB-bridge parity and environment connectivity.  
* Deliverable D11 — Architecture snapshot evidence.  
* Deliverable D12 — v2 mapped-cache persistence hardening.  
* Deliverable D13 — Release sanity pipeline.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST005.

“Enforce that all Phase VI evidence artifacts use canonical encodings and are captured under pinned locale.”

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask IDs: HDE-DIST005.1, HDE-DIST005.2.

“Use canonical JSON or headers-only text, LF-terminated.”

“For any artifact added/moved/removed in this phase, update the Human Index, hash sentinel, and Machine Mirror in the same PR.”

PF09 subtask IDs: HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.9, HDE-DIST001.10, HDE-DIST001.11.

“This task ties together multiple acceptance dimensions and a large evidence surface.”

PF09 subtask ID: HDE-DIST001.6.

“Implement a one-button runner that executes the release and provenance sanity pipeline end-to-end and fails closed on any drift.”

“Run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; keep all evidence artifacts canonical and secret-free.”

### PF09 completion role

Complete in this epic.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide release sanity pipeline.

Existing entrypoint in the quoted canon: Existing: `tools/evidence/run_sanity_pipeline.py` (PF14 — HDE-Mechanics Guide).

“The release sanity pipeline harness is treated as the scripted implementation of this workflow for sampler and Engine Core evidence under closed rails.”

“It MUST refresh the Evidence Index and Machine Mirror so that the sanity pipeline log reflects the full suite of determinism and evidence checks.”

PF14 anchor: HDE-Mechanics Guide parent binding posture.

“A parent-binding or aggregate-evidence PR may consume PO-produced OPS evidence, but it MUST NOT claim to have executed OPS.”

### PF07 facts / gaps

* PF07-derived repository: `amthorn78/glow-hdengine-v2`.  
* PF07-derived closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`.  
* PF07-derived determinism pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* PF07-derived OPS root for this epic: `audit/ops/hde-epic038/`.  
* PF07-derived QA root for later work: `audit/qa/hde-epic038/`.  
* PF07 gap: None.

### Observed repo reality

* Observed repo reality: `tools/evidence/run_sanity_pipeline.py` exists.  
* Observed repo reality: it currently writes `artifacts/sanity/sanity.log`.  
* Observed repo reality: it runs an ordered step list and stops at the first nonzero result.  
* Observed repo reality: it invokes write-producing evidence generators and refreshes the evidence index.  
* Observed repo reality: the current log records successful prior checks but does not include the HDE-EPIC038 identity, A7, DB, architecture, or mapped-cache producers.  
* Observed repo reality: PF12 now names `audit/gates/sanity_pipeline/sanity_pipeline.log` as the single canonical sanity evidence surface.  
* Observed repo reality: `tools/evidence/run_sanity_pipeline_gate.py` writes an unrelated HDE-EPIC024 QA primary log under `audit/qa/hde-epic024/checks/D07_sanity_pipeline/`, copies the legacy sanity log to the gate path, and implements and calls `_write_path_proof` directly.

### Observed audit provenance

* Observed audit provenance: the existing pipeline and older sanity log were present.  
* Observed audit provenance: the PF09 transcript path and EPIC038-specific pipeline coverage were absent.  
* Observed audit provenance: earlier evidence paths and PF filenames require current revalidation.

### Discovery

* Read-only discovery command for Observed repo reality: `sed -n '1,240p' tools/evidence/run_sanity_pipeline.py`.  
* Read-only discovery command for Existing gate wrapper: `sed -n '1,240p' tools/evidence/run_sanity_pipeline_gate.py`.  
* Read-only discovery command for Existing sanity tests: `find tests -type f -print | grep -F 'sanity' | sort`.  
* Read-only discovery command for Existing pipeline references: `grep -R -n -F 'run_sanity_pipeline' .github ci tools tests`.  
* Read-only discovery command for OPS-01 outputs: `find audit/ops/hde-epic038/ops-01 -type f -print | sort`.  
* Read-only discovery command for OPS-02 outputs: `find audit/ops/hde-epic038/ops-02 -type f -print | sort`.  
* Read-only discovery command for current governed artifacts: `find artifacts audit/gates docs/evidence -type f -print | sort`.  
* If either OPS evidence root is absent, do not fabricate it and do not claim the live-dependent PF09 dimensions complete.

### Implementation requirements

1. Use Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log` as the PF12 canonical sanity evidence surface and correct the wrapper’s write ownership.  
     
   * Update Existing: `tools/evidence/run_sanity_pipeline.py` (PF14 — HDE-Mechanics Guide) to write the canonical sanity gate artifact directly.  
   * Update Existing: `tools/evidence/run_sanity_pipeline_gate.py` (PF12 — HDE-Schemas & Artifacts) so it writes only the canonical sanity gate artifact and its own non-governed process streams when needed.  
   * Remove every write to `audit/qa/hde-epic024/`.  
   * Remove the `D07_sanity_pipeline` directory identity and all HDE-EPIC024 check metadata.  
   * Remove the `_write_path_proof` implementation and every call to it.  
   * Delegate every governed `*.path_proof.txt` creation to Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).  
   * Do not create or bind a second sanity log.  
   * Retain Existing: `artifacts/sanity/sanity.log` only as historical unbound material if deletion is unsafe; do not refresh it as a competing truth surface.

   

2. Define deterministic ordered stages:  
     
   * environment pins;  
   * identity and release provenance;  
   * canonical JSON;  
   * Reader-to-CLI, AB-to-BA, two-run, and preimage checks;  
   * A7 Catalog transport;  
   * CI rails;  
   * DB posture;  
   * BodyGraph policy;  
   * DB-bridge parity;  
   * architecture snapshot;  
   * configured-v2 mapped-cache local evidence;  
   * OPS evidence checksum and summary validation;  
   * Human Index and Machine Mirror refresh;  
   * path validation;  
   * mirror schema and hash validation;  
   * topology orientation validation;  
   * final LF validation.

   

3. Fail closed.  
     
   * Stop on first failed stage.  
   * Do not hide skipped required stages.  
   * Distinguish unavailable required OPS evidence from PASS.  
   * Do not claim a live predicate when only fixture evidence exists.  
   * Final summary PASS requires every in-scope mandatory stage to be OK.

   

4. Consume OPS evidence without rerunning it.  
     
   * Validate OPS-01 and OPS-02 checksum ledgers.  
   * Validate required files are present and non-empty.  
   * Validate no secret or raw payload markers.  
   * Validate reported exit codes.  
   * Bind the OPS primary artifacts through the evidence ledgers.  
   * State explicitly that the PR reruns no OPS.

   

5. Update tests.  
     
   * Ordered-stage test.  
   * First-failure stop test.  
   * Missing OPS evidence test.  
   * Invalid checksum test.  
   * Lower-level failure propagation test.  
   * Canonical log and one-LF test.  
   * No duplicate sanity-surface test.  
   * Regression test that the HDE-EPIC038 wrapper writes only `audit/gates/sanity_pipeline/sanity_pipeline.log` and does not write any path under `audit/qa/hde-epic024/`.  
   * Regression test that `tools/evidence/run_sanity_pipeline_gate.py` contains no `D07_sanity_pipeline` directory identity, no `_write_path_proof` implementation, and no direct governed path-proof write.

   

6. Final canonical evidence refresh.  
     
   * Use the canonical evidence updater.  
   * Refresh orientation after the final evidence skeleton.  
   * Validate mirror schema, mirror checksum, Human Index checksum, and final LF.  
   * Do not hand-edit generated evidence.

   

7. Keep later axes separate.  
     
   * Do not create close report, close manifest, acceptance map, token matrix, Live QA plan, or PF-Canon updates.  
   * Do not claim QA PASS, acceptance, PF09 drainage, board update, merge, deployment, or closeout.

### Concrete anchors

* Observed repo reality: `tools/evidence/run_sanity_pipeline.py`.  
* Existing: `tools/evidence/run_sanity_pipeline_gate.py` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `tools/evidence/orientation_demo.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `tools/evidence/validate_evidence_paths.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `ci/checks/check_mirror_schema.sh` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `ci/checks/check_evidence_index_hash.sh` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `ci/checks/check_final_lf.sh` (PF12 — HDE-Schemas & Artifacts).  
* Planned test path: `tests/evidence/test_hde_epic038_release_sanity.py`.  
* Planned OPS evidence root: `audit/ops/hde-epic038/ops-01/`.  
* Planned OPS evidence root: `audit/ops/hde-epic038/ops-02/`.

### Evidence outputs

* Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log`.  
* Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`.  
* Existing and regenerated output: `docs/evidence/INDEX.json`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256`.  
* Existing and regenerated output: `docs/evidence/INDEX.json.path_proof.txt`.  
* Existing and regenerated output: `docs/evidence/INDEX.sha256.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.path_proof.txt`.  
* Existing and regenerated output: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.  
* Existing and regenerated output: `audit/gates/topology/orientation_demo.txt`.  
* Existing and regenerated output: `audit/gates/topology/orientation_demo.txt.path_proof.txt`.  
* Existing and indexed OPS primary artifacts from OPS-01.  
* Existing and indexed OPS primary artifacts from OPS-02.

### Acceptance tokens

* `SANITY_PIPELINE_OK`  
* `ENV_LC_ALL_C_OK`  
* `JSON_CANONICAL_CHECK_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_INDEX_HASH_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
* `EVIDENCE_PATH_PROOFS_OK`  
* `CI_CHECK_MIRROR_SCHEMA_OK`  
* `CI_CHECK_FINAL_LF_OK`

These remain planned claims. The PR does not declare them accepted.

### Rails posture

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`  
* No live vendor call.  
* No live DB call.  
* No OPS rerun.  
* No secret values.

### Basic QA check \+ pass condition

Basic QA check:

* Run Planned test path: `tests/evidence/test_hde_epic038_release_sanity.py`.  
* Run Existing command: `python tools/evidence/run_sanity_pipeline_gate.py`.  
* Run Existing command: `python tools/evidence/update_evidence_index.py --check`.  
* Run Existing command: `python tools/evidence/orientation_demo.py --check`.  
* Run Existing command: `python tools/evidence/validate_evidence_paths.py`.  
* Run Existing command: `python ci/checks/check_mirror_schema.sh`.  
* Run Existing command: `bash ci/checks/check_evidence_index_hash.sh`.  
* Run Existing command: `ci/checks/check_final_lf.sh`.

Pass condition:

* The pipeline runs all required stages in deterministic order.  
* It stops on the first failure.  
* It rejects absent or invalid required OPS evidence.  
* It does not rerun OPS.  
* The canonical sanity log ends with PASS only when every mandatory stage is OK.  
* The complete governed evidence skeleton is coherent.

### PO inputs

* Committed OPS-01 evidence package.  
* Committed OPS-02 evidence package.  
* Confirmation that no additional live-dependent proof is authorized for this implementation phase.

### Codex Prompt

Implement HDE-EPIC038 PR-06.

This is the aggregate implementation and evidence-orchestration PR. It is not OPS, QA execution, PF09 drainage, closeout, or a PF-Canon edit.

PF09.6 mappings:

* HDE-DIST005.1 and HDE-DIST005.2.  
* HDE-DIST001.4, HDE-DIST001.5, HDE-DIST001.6, HDE-DIST001.9, HDE-DIST001.10, and HDE-DIST001.11.

PF14 anchors:

* HDE-Mechanics Guide §1.3 evidence workflow.  
* Release sanity pipeline harness.  
* Parent binding does not rerun OPS.

Inspect first:

* Observed repo reality: `tools/evidence/run_sanity_pipeline.py`.  
* Observed repo reality: `tools/evidence/run_sanity_pipeline_gate.py`.  
* Existing: `tools/evidence/update_evidence_index.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `tools/evidence/orientation_demo.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `tools/evidence/validate_evidence_paths.py` (PF14 — HDE-Mechanics Guide).  
* Existing: `ci/checks/check_mirror_schema.sh` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `ci/checks/check_evidence_index_hash.sh` (PF12 — HDE-Schemas & Artifacts).  
* Existing: `ci/checks/check_final_lf.sh` (PF12 — HDE-Schemas & Artifacts).

Correct the sanity wrapper before orchestration:

* Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log` is the only canonical sanity evidence surface.  
* Existing: `tools/evidence/run_sanity_pipeline.py` must write that path directly.  
* Existing: `tools/evidence/run_sanity_pipeline_gate.py` must not write any path under `audit/qa/hde-epic024/`.  
* Remove `D07_sanity_pipeline` and all HDE-EPIC024 check metadata from the wrapper.  
* Remove `_write_path_proof` and every direct path-proof write from the wrapper.  
* Existing: `tools/evidence/update_evidence_index.py` is the only writer for governed path proofs.  
* Do not refresh Existing: `artifacts/sanity/sanity.log` as a competing evidence surface.

The pipeline must invoke these exact PR-01 through PR-05 producer commands in deterministic order:

* `python tools/evidence/generate_identity_provenance.py`  
* `python tools/evidence/generate_release_bindings.py`  
* `python tools/evidence/generate_env_matrix_snapshot.py`  
* `python tools/evidence/generate_determinism_gate_proofs.py`  
* `python tools/evidence/generate_a7_transport_proofs.py`  
* `python tools/evidence/generate_rails_gate_evidence.py`  
* `python tools/evidence/generate_db_runtime_posture.py`  
* `python tools/evidence/generate_db_bridge_parity.py`  
* `python tools/evidence/generate_bodygraph_policy_proofs.py`  
* `python tools/evidence/generate_architecture_snapshot.py`  
* `python tools/evidence/generate_v2_mapped_cache_evidence.py`

Require these PR-01 primary artifacts before later stages:

* `artifacts/identity/release_id.json`  
* `artifacts/identity/release_id_recompute.log`  
* `artifacts/parity/two_run_identity.log`  
* `artifacts/identity/service_identity.json`  
* `artifacts/identity/emitter_sha256.json`  
* `artifacts/identity/invocation_sha256.json`  
* `artifacts/bodygraph/release_bindings.json`  
* `artifacts/runtime/env_matrix.snapshot.json`  
* `artifacts/math/freeze_pack_manifest.json`

Require these PR-02 primary artifacts:

* `audit/gates/parity/reader_cli/ab.json`  
* `audit/gates/parity/reader_cli/ba.json`  
* `audit/gates/parity/reader_cli/summary.json`  
* `audit/gates/determinism/abba.bytes`  
* `audit/gates/determinism/tworun_identity.sha256`  
* `audit/gates/canonical_json/json_canon_compare.log`  
* `artifacts/cards/a3/IDENTITY_OK.txt`  
* `docs/ENDPOINTS_CATALOG.json`  
* `docs/ENDPOINTS_CATALOG.json.sha256`  
* `docs/ENDPOINTS_CATALOG.json.path_proof.txt`  
* `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`  
* `artifacts/reader/endpoints_snapshot.json`  
* `artifacts/proofs/endpoints_env_gate_proof.log`  
* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`  
* `artifacts/proofs/success_encoding_invariance.txt`  
* `artifacts/proofs/reader_success_get_head_304.json`

Require these PR-03 primary artifacts:

* `artifacts/proofs/ops_refusal_proof.txt`  
* `artifacts/vendor/retry_after_parse.log`  
* `artifacts/bodygraph/keys_only.logs.sample`

Require these PR-04 primary artifacts and the exact existing boundary-view sibling path proof:

* `artifacts/db/ddl_fingerprint.json`  
* `artifacts/db/grants.txt`  
* `artifacts/db/check_schema.txt`  
* `artifacts/db/check_constraints.txt`  
* `artifacts/db/boundary_view.readonly.proof.txt`  
* `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`  
* `artifacts/runtime/env_connectivity.snapshot.json`  
* `artifacts/runtime/env_connectivity.nondev_failure.json`  
* `artifacts/bodygraph/source_selection.snapshot.json`  
* `artifacts/bodygraph/source_invariance/ab.json`  
* `artifacts/bodygraph/source_invariance/ba.json`  
* `artifacts/bodygraph/source_invariance/summary.json`  
* `artifacts/bodygraph/refresh_policy.snapshot.json`  
* `artifacts/bodygraph/metrics.snapshot.json`  
* `artifacts/bodygraph/keys_only.logs.sample`  
* `artifacts/bodygraph/vendor_upsert.epic038_synthetic.json`  
* `artifacts/bodygraph/db_resolve.epic038_synthetic.json`  
* `artifacts/presenter/json_canon_compare.log`  
* `artifacts/db_bridge/adapter_selection.snapshot.json`  
* `artifacts/db_bridge/provider_parity.proof.json`  
* `artifacts/architecture/architecture_snapshot.keys_only.json`  
* `schemas/architecture_snapshot.keys_only.v1.json`

Require these PR-05 primary artifacts and schemas:

* `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`  
* `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`  
* `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`  
* `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`  
* `artifacts/bodygraph/v2_mapped_cache/idempotence.log`  
* `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`  
* `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`  
* `artifacts/bodygraph/v2_mapped_cache/manifest.json`  
* `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`  
* `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`

Every governed primary artifact listed above must have its exact sibling `.path_proof.txt` where PF12 requires one. The pipeline must validate the exact sibling and must not synthesize a passing result when it is absent.

Validate these exact OPS-01 files without rerunning OPS:

* `audit/ops/hde-epic038/ops-01/commands.txt`  
* `audit/ops/hde-epic038/ops-01/stdout.log`  
* `audit/ops/hde-epic038/ops-01/stderr.log`  
* `audit/ops/hde-epic038/ops-01/exit_code.txt`  
* `audit/ops/hde-epic038/ops-01/env_presence.json`  
* `audit/ops/hde-epic038/ops-01/db_posture_summary.json`  
* `audit/ops/hde-epic038/ops-01/provider_parity.proof.json`  
* `audit/ops/hde-epic038/ops-01/bridge_consistency.result.json`  
* `audit/ops/hde-epic038/ops-01/nonclaims.json`  
* `audit/ops/hde-epic038/ops-01/result_summary.json`  
* `audit/ops/hde-epic038/ops-01/checksums.sha256`

Validate these exact OPS-02 files without rerunning OPS:

* `audit/ops/hde-epic038/ops-02/commands.txt`  
* `audit/ops/hde-epic038/ops-02/stdout.log`  
* `audit/ops/hde-epic038/ops-02/stderr.log`  
* `audit/ops/hde-epic038/ops-02/exit_code.txt`  
* `audit/ops/hde-epic038/ops-02/env_presence.json`  
* `audit/ops/hde-epic038/ops-02/request_summary.json`  
* `audit/ops/hde-epic038/ops-02/mapped_output_summary.json`  
* `audit/ops/hde-epic038/ops-02/read_back_summary.json`  
* `audit/ops/hde-epic038/ops-02/canonical_parity.log`  
* `audit/ops/hde-epic038/ops-02/idempotence.log`  
* `audit/ops/hde-epic038/ops-02/no_raw_vendor_payload_persistence.log`  
* `audit/ops/hde-epic038/ops-02/legacy_fallback_preservation.log`  
* `audit/ops/hde-epic038/ops-02/nonclaims.json`  
* `audit/ops/hde-epic038/ops-02/result_summary.json`  
* `audit/ops/hde-epic038/ops-02/checksums.sha256`

For every required OPS file above, absence or zero bytes must stop the pipeline with a nonzero status and identify the exact missing path. A checksum-ledger mismatch must stop with a nonzero status and identify the exact ledger and mismatched file. An absent, skipped, unavailable, or errored required provider row must not be classified as PASS. Do not fabricate or regenerate any OPS file.

Run stages in this exact order:

1. Environment pins.  
2. Identity and release provenance.  
3. Canonical JSON.  
4. Reader-to-CLI, AB-to-BA, two-run, and preimage checks.  
5. A7 Catalog transport.  
6. CI rails.  
7. DB posture.  
8. BodyGraph policy.  
9. DB-bridge parity.  
10. Architecture snapshot.  
11. Configured-v2 mapped-cache local evidence.  
12. OPS evidence checksum and summary validation.  
13. Human Index and Machine Mirror refresh.  
14. Path validation.  
15. Mirror schema and hash validation.  
16. Topology orientation validation.  
17. Final LF validation.

Stop on the first failed stage. Do not hide a skipped required stage. Do not claim a live predicate from fixture-only evidence. Final PASS requires every mandatory stage to be OK.

Create Planned test path: `tests/evidence/test_hde_epic038_release_sanity.py` with coverage for stage ordering, first-failure stop, missing OPS files, zero-byte OPS files, invalid checksums, lower-level failure propagation, canonical one-LF log output, absence of duplicate sanity surfaces, exact-path validation for `artifacts/cards/a3/IDENTITY_OK.txt`, exact-path validation for `artifacts/db/boundary_view.readonly.proof.txt` and `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`, absence of writes under `audit/qa/hde-epic024/`, absence of `D07_sanity_pipeline`, and absence of direct `_write_path_proof` calls.

The wrapper may write only Planned output: `audit/gates/sanity_pipeline/sanity_pipeline.log`. Existing: `tools/evidence/update_evidence_index.py` must create its sibling path proof and all other governed path proofs.

Do not create close-pack, acceptance-map, token-matrix, QA-plan, or PF-canon artifacts.

Run these exact Basic QA and evidence-validation commands under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`:

* `python -m pytest tests/evidence/test_hde_epic038_release_sanity.py`  
* `python tools/evidence/run_sanity_pipeline_gate.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python ci/checks/check_mirror_schema.sh`  
* `bash ci/checks/check_evidence_index_hash.sh`  
* `ci/checks/check_final_lf.sh`

PASS means every mandatory stage is OK, every required PR and OPS artifact is present and valid, OPS checksum validation succeeds without rerunning OPS, the wrapper writes only the canonical sanity gate artifact, all path proofs come from the canonical evidence updater, and the final Human Index, Machine Mirror, checksums, proofs, and orientation are coherent. FAIL means any required file is missing or empty, any checksum mismatches, any mandatory stage is absent, skipped, false, stale, or unbound, the wrapper touches another epic’s QA root, or direct path-proof writing remains.

# Ops tasks

## OPS-01 — Live DB and bridge posture capture

### Intent

Capture bounded, read-only current-environment DB posture and direct-versus-bridge provider parity without mutating database state or exposing connection details.

### IG source items

* Deliverable D8 — DB posture runtime checks.  
* Deliverable D10 — DB-bridge parity and environment connectivity.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.4.

“Use the Distillation harness to prove and exercise the DB runtime posture defined in Task HDE-FERM004.”

PF09 subtask ID: HDE-DIST001.9.

“Prove parity between direct DB reads and bridge-mediated reads for BodyGraph, and capture the associated environment connectivity posture.”

### PF09 completion role

Contributes evidence only.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide §20.1.

“Objective. Capture the runtime DB schema, roles/grants, and boundary view posture in a deterministic way.”

PF14 anchor: HDE-Mechanics Guide §20.3.

“Objective. Prove parity between direct DB reads and bridge-mediated reads and capture env connectivity posture.”

PF14 anchor: HDE-Mechanics Guide OPS provider-parity closure packet.

“The OPS packet MUST keep provider-parity closure evidence machine-readable, secret-safe, and non-overclaiming.”

### PF07 facts / gaps

* PF07-derived operator console repository: `amthorn78/glow-hdengine-v2`.  
* PF07-derived provider: Railway.  
* PF07-derived project: `ample-illumination`.  
* PF07-derived DB instance: `ample-illumination/production/postgres`.  
* PF07-derived DB schema: `hde`.  
* PF07-derived primary key name: `DATABASE_URL`.  
* PF07-derived bridge key name: `DB_BRIDGE_URL`.  
* PF07-derived bridge service: `pg-bridge`.  
* PF07-derived bridge URL: `https://illustrious-freedom-production.up.railway.app`.  
* PF07-derived search path: `hde, public`.  
* PF07-derived production guard key: `DB_ALLOW_BRIDGE_IN_PROD`.  
* PF07 gap: None.

### Preconditions

* PR-04 implementation is available in the operator checkout.  
* PO authorizes read-only access to the shared DB and bridge.  
* `DATABASE_URL` is present.  
* `DB_BRIDGE_URL` is present.  
* No secret value will be echoed.  
* The active parity corpus is fixed before execution.  
* No SQL write, migration, grant change, schema change, or vendor call is permitted.  
* Any unavailable direct or bridge row remains unavailable and cannot be treated as PASS.

### Operator action

Owner: PO. Facilitator: IA.

Run the PR-04 DB posture and bridge-parity operator surfaces in read-only mode from the canonical QA console. Capture command identity, working directory, environment presence, stdout, stderr, exit code, row-level direct/bridge results, parity status, and bridge-consistency status.

The operator must not hand-edit result artifacts or normalize unavailable rows into passing rows.

### Evidence outputs

* Planned output: `audit/ops/hde-epic038/ops-01/commands.txt`.  
* Planned output: `audit/ops/hde-epic038/ops-01/stdout.log`.  
* Planned output: `audit/ops/hde-epic038/ops-01/stderr.log`.  
* Planned output: `audit/ops/hde-epic038/ops-01/exit_code.txt`.  
* Planned output: `audit/ops/hde-epic038/ops-01/env_presence.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/db_posture_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/provider_parity.proof.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/bridge_consistency.result.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/nonclaims.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/result_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-01/checksums.sha256`.

### Verification

* Exit code is recorded.  
* Search path is exactly `hde, public`.  
* The active parity corpus is explicit.  
* Every claimed parity row has both direct and bridge observations.  
* Every claimed parity row records `parity=match`.  
* Missing, skipped, unavailable, or errored rows are not reported as PASS.  
* Bridge consistency result matches the row-level data.  
* Logs contain no DSN, password, token, raw user data, or raw BodyGraph payload.  
* Evidence does not claim QA PASS, token satisfaction, PF09 movement, or closeout.

### Evidence commit plan

The PO commits the secret-free OPS evidence under Planned output root: `audit/ops/hde-epic038/ops-01/`. PR-06 validates the package, binds its primary artifacts through the evidence ledgers, and states that OPS was not rerun.

### PO inputs

* Authorization for read-only DB and bridge access.  
* Presence of `DATABASE_URL`.  
* Presence of `DB_BRIDGE_URL`.  
* Active parity corpus name.  
* Approved synthetic or existing non-PII BodyGraph selector, when a row-level BodyGraph comparison requires one.

## OPS-02 — Controlled configured-v2 mapped-cache proof

### Intent

Capture one bounded, PO-authorized configured-v2 mapped-cache write/read-back and idempotence proof using synthetic data, while preserving production-like write refusal and nonclaims.

### IG source items

* Deliverable D12 — v2 mapped-cache persistence hardening.

### Caveats applied

None.

### PF09 document(s) \+ task IDs \+ proof excerpts

PF09 document: PF09.6 — HDE-Build-Checklist-Distillation.

PF09 task ID: HDE-DIST001.

“Provide one-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.”

### PF09 subtask IDs \+ proof excerpts

PF09 subtask ID: HDE-DIST001.11.

“Implement and prove a durable mapped-cache persistence path for configured-v2 chart-backed BodyGraph resolution in non-prod or controlled rails before any production-facing write posture is considered.”

“This subtask must not simply turn on writes.”

### PF09 completion role

Contributes evidence only.

### PF14 pointers

PF14 anchor: HDE-Mechanics Guide mapped-cache persistence.

“ChartResult StandardResponse data MUST NOT be written into the durable BodyGraph cache as reusable user data until a bounded mapped-cache persistence slice proves adapter-mapped HDE data, write/read-back parity, idempotence, and no raw v2 vendor envelope persistence.”

PF14 anchor: HDE-Mechanics Guide open-rails mechanics.

“Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an ops task.”

### PF07 facts / gaps

* PF07-derived HumanDesignAPI base key: `HD_API_BASE_URL`.  
* PF07-derived configured base: `https://api.humandesignapi.nl/v2`.  
* PF07-derived vendor credential key: `HD_API_KEY`.  
* PF07-derived geocoding key: `GEO_API_KEY`.  
* PF07-derived DB key: `DATABASE_URL`.  
* PF07-derived DB instance: `ample-illumination/production/postgres`.  
* PF07-derived DB schema: `hde`.  
* PF07-derived open rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`.  
* PF07-derived production-like APP\_ENV values: `prod`, `production`, `live`.  
* PF07 gap: staging and development share the same physical DB instance, so this OPS task requires explicit PO authorization for the exact synthetic row and retention or cleanup decision.

### Preconditions

* PR-05 implementation is available.  
* PO authorizes one bounded vendor request and one synthetic mapped-cache write/read-back.  
* The active APP\_ENV is explicitly non-production-like.  
* `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, and `DATABASE_URL` are present.  
* Secret values are not printed or committed.  
* The synthetic identity and birth tuple are PO-approved and contain no real user PII.  
* Existing script: `scripts/ops/hde_epic038_mapped_cache_smoke.py` is reviewed before execution.  
* No production authorization claim is permitted.  
* No uncontrolled repeated vendor call is permitted.

### Operator action

Owner: PO. Facilitator: IA.

Run Existing script: `scripts/ops/hde_epic038_mapped_cache_smoke.py` once for the approved synthetic identity, followed by the script’s bounded idempotence recheck. The script must use the configured version-neutral `charts` resource, map the response through the deterministic v2 adapter, write only mapped HDE data, read it back, compare canonical governed fields, and record bounded redacted summaries.

The operator must not paste or store raw vendor request bodies, response bodies, secret headers, API keys, birth payloads, or full DB connection strings.

### Evidence outputs

* Planned output: `audit/ops/hde-epic038/ops-02/commands.txt`.  
* Planned output: `audit/ops/hde-epic038/ops-02/stdout.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/stderr.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/exit_code.txt`.  
* Planned output: `audit/ops/hde-epic038/ops-02/env_presence.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/request_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/mapped_output_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/read_back_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/canonical_parity.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/idempotence.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/no_raw_vendor_payload_persistence.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/legacy_fallback_preservation.log`.  
* Planned output: `audit/ops/hde-epic038/ops-02/nonclaims.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/result_summary.json`.  
* Planned output: `audit/ops/hde-epic038/ops-02/checksums.sha256`.

### Verification

* Exit code is 0 for the authorized bounded run.  
* The selected runtime resource is `charts`.  
* Auth posture is recorded only as redacted header family.  
* Adapter result is mapped.  
* Stored payload posture is adapter-mapped HDE data.  
* Pre-write and post-read governed fields are canonically equal.  
* Second write creates no duplicate or divergent row.  
* No raw StandardResponse, ChartResult envelope, request body, response body, secret, or uncontrolled payload appears in persistence or evidence.  
* Production-like APP\_ENV values remain refused by the implementation.  
* Explicit legacy non-v2 fallback remains preserved.  
* Evidence does not claim production authorization, QA PASS, PF09 movement, broad v2 conformance, deployment, or closeout.

### Evidence commit plan

The PO commits the secret-free OPS evidence under Planned output root: `audit/ops/hde-epic038/ops-02/`. PR-06 validates checksums and required predicates, indexes the primary evidence, and does not rerun the external action.

### PO inputs

* Authorization for the bounded open-rails vendor request.  
* Authorization for the synthetic mapped-cache DB write/read-back.  
* Presence of `HD_API_BASE_URL`.  
* Presence of `HD_API_KEY`.  
* Presence of `GEO_API_KEY`.  
* Presence of `DATABASE_URL`.  
* Approved synthetic identity.  
* Approved synthetic birth tuple.  
* Retention or cleanup decision for the synthetic cache row.

# PO Inputs Summary

* Confirmed engine tag for the release cut.  
* Canonical Invocation bytes corresponding to `INV-f2ac55d77ce9aacc`.  
* Confirmation of the current Invocation tag.  
* Optional build-commit exposure policy for operator surfaces.  
* Authorization for OPS-01 read-only DB and bridge access.  
* Presence of `DATABASE_URL`.  
* Presence of `DB_BRIDGE_URL`.  
* OPS-01 active parity corpus name.  
* Approved non-PII selector for OPS-01 when row-level BodyGraph parity requires one.  
* Authorization for OPS-02 bounded open-rails vendor access.  
* Authorization for OPS-02 synthetic mapped-cache write/read-back.  
* Presence of `HD_API_BASE_URL`.  
* Presence of `HD_API_KEY`.  
* Presence of `GEO_API_KEY`.  
* Approved synthetic identity for OPS-02.  
* Approved synthetic birth tuple for OPS-02.  
* Retention or cleanup decision for the OPS-02 synthetic cache row.  
* No raw secret values are inputs to this document.

# ADRs (Canon reconciliation notes)

## **ADR-002**

ADR ID: ADR-002  
 Type/Tag: RESOLVED PLAN-LOCAL PATH DECISION

Decision/Problem:

Decision: HDE-EPIC038 will reuse and regenerate the existing governed boundary-view proof at `artifacts/db/boundary_view.readonly.proof.txt` and its sibling path proof. HDE-EPIC038 will create only the remaining exact planned paths listed in this block under the existing `artifacts` and `schemas` roots. Those remaining paths are planned outputs, not new top-level roots and not alternate homes for existing governed artifacts. Later PF12 drainage is documentation-only and is not an execution dependency.

* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json`.  
* Planned output: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
* Planned schema: `schemas/architecture_snapshot.keys_only.v1.json`.  
* Planned output root: `artifacts/bodygraph/v2_mapped_cache/`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/idempotence.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`.  
* Planned output: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_transcript.v1.json`.  
* Planned schema: `schemas/bodygraph_v2_mapped_cache_manifest.v1.json`.

Canon touchpoints:

* PF27 — Plan Templates, Repository locus validation and file minting posture.  
* PF09.6 — HDE-Build-Checklist-Distillation HDE-DIST001.4, HDE-DIST001.10, HDE-DIST001.11.  
* PF12 — HDE-Schemas & Artifacts Evidence Catalog.  
* PF14 — HDE-Mechanics Guide DB, boundary-analysis, and mapped-cache mechanics.

Repo touchpoints:

* Observed repo reality: `engine/bodygraph/resolver.py`.  
* Observed repo reality: `engine/bodygraph/v2_adapter.py`.  
* Observed repo reality: `engine/bodygraph/ingest.py`.  
* Observed repo reality: `tools/evidence/generate_db_bridge_parity.py`.  
* Observed repo reality: `scripts/db/capture_epic011_posture.py` writes the existing governed boundary-view proof family.  
* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt`.  
* Existing and regenerated output: `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`.  
* Observed repo reality: `artifacts/evidence_index.jsonl` references the existing boundary-view primary path.  
* Missing current path: `artifacts/architecture/architecture_snapshot.keys_only.json`.  
* Missing current path: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.

Drain target:

* PF12 — HDE-Schemas & Artifacts.

Plan impact:

PR-04 reuses the existing governed boundary-view proof family. PR-04 and PR-05 create only the remaining exact planned paths listed here. No alternate root or second evidence home is authorized. This resolved plan-local decision requires no separate PO ADR approval.

## ADR-005

ADR ID: ADR-005  
 Type/Tag: RESOLVED PLAN-LOCAL IMPLEMENTATION DECISION

Decision/Problem:

Decision: Create Planned output: `engine/runtime/identity.py` as the single fetch-only identity module. Identity values originate at cut time from PF14 sources: `release_id` from canonical `catalog/manifest.json` bytes, Invocation tag and bytes from the Invocation registry, and `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` from the build snapshot. Existing and regenerated output: `artifacts/identity/service_identity.json` is generated evidence output and is never a runtime input. The current artifact has five top-level fields and must be regenerated with `invocation_sha256`. This plan does not authorize a conditional alternate identity seam.

Canon touchpoints:

* PF14 — HDE-Mechanics Guide §13.1 Fields.  
* PF14 — HDE-Mechanics Guide §13.3 Flow & constraints.  
* PF02 — HDE Architecture.  
* PF12 — HDE-Schemas & Artifacts identity evidence.  
* PF09.6 — HDE-Build-Checklist-Distillation HDE-DIST006.

Repo touchpoints:

* Observed repo reality: `engine/runtime/__init__.py`.  
* Observed repo reality: `engine/runtime/public.py`.  
* Observed repo reality: `adapter/http_reader.py`.  
* Observed repo reality: `engine/cli/main.py`.  
* Observed repo reality: `artifacts/identity/service_identity.json` has five top-level fields and lacks `invocation_sha256`.

Drain target:

* PF14 — HDE-Mechanics Guide only if a permanent concrete code-locus statement is wanted.  
* PF12 — HDE-Schemas & Artifacts only if runtime snapshot semantics require additional schema text.

Plan impact:

PR-01 creates one fetch-only identity authority, removes request-time identity environment reads, prohibits runtime evidence-root input, and regenerates the exact six-field evidence snapshot without creating a second public or configuration surface.

ASK OK?  
