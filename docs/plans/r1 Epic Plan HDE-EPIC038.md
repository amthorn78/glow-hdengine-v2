# Epic Plan Record

## Meta

* Epic ID: `HDE-EPIC038`  
* Epic name: Distillation Pass 3  
* Alchemical phase: Distillation  
* Phase rationale: This epic belongs in Distillation because it refines and systematizes release reliability, identity, evidence discipline, gates, and controlled mapped-cache persistence. The work focuses on repeatability, canonical evidence, and durable harness behavior rather than new public product scope or exploratory feature expansion.  
* Status: Planned  
* Version: r1  
* Date started: 2026-07-10  
* Date completed: \[INTENTIONALLY LEFT BLANK\]

## PF Canon Applicability Snapshot

* PF-Invocation — Checked \- no plan impact.  
* PF01 — HDE-Math-Spec — Applied: canonical JSON, determinism, preimage, release identity, and two-run identity posture.  
* PF02 — HDE Architecture — Applied: engine, adapter, presenter, BodyGraph cache, Endpoint Catalog, no second HTTP home, and mapped-cache boundary posture.  
* PF03 — Technical Writing Best Practices — Applied: paste-safe plan body, titles-only routing, no prohibited omission markers, and documentation-drainage posture.  
* PF04 — HDE Governance — Applied: rails posture, token registry posture, A7 policy, no-secret evidence, and operational policy.  
* PF05 — HDE-CLI-API-Vendor-Ref — Applied: CLI/API/vendor byte ownership, A7 Catalog route posture, vendor base/auth posture, and command-materiality posture.  
* PF06 — Epic Process Guide — Applied: PR-first posture, OPS separation, evidence parity, PF09 accountability, and documentation drainage not being a gate.  
* PF07 — Glow Infrastructure — Applied: repository/service/config-key ownership, governed evidence roots, QA root, and infrastructure fact discipline.  
* PF08 — Human Design System — Not applicable.  
* PF09.1 — HDE-Build-Checklist-Calcination — Checked \- no plan impact.  
* PF09.2 — HDE-Build-Checklist-Dissolution — Checked \- no plan impact.  
* PF09.3 — HDE-Build-Checklist-Separation — Checked \- no plan impact.  
* PF09.4 — HDE-Build-Checklist-Conjunction — Checked \- no plan impact.  
* PF09.5 — HDE-Build-Checklist-Fermentation — Applied only for HDE-FERM004 semantic context referenced by the Distillation DB posture row; no Fermentation scope is imported into this epic.  
* PF09.6 — HDE-Build-Checklist-Distillation — Applied: primary PF09 completion backbone for exact task and subtask mapping.  
* PF09.7 — HDE-Build-Checklist-Coagulation — Checked \- no plan impact.  
* PF10 — HDE Build Notes — Checked \- no active addendum impact for this plan.  
* PF11 — The Rave I Ching — Not applicable.  
* PF12 — HDE-Schemas & Artifacts — Applied: governed artifacts, Human Evidence Index, Machine Mirror, canonical JSON, manifests, path proofs, and evidence-family posture.  
* PF13 — Glow Development Philosophy — Reference-only context.  
* PF14 — HDE Mechanics Guide — Applied: mechanics references for evidence jobs, identity/provenance, gates, mapped-cache persistence, BodyGraph, and release sanity.  
* PF15 — HDE Copy Tonality Guide — Not applicable.  
* PF17 — HDE Narratives Guide — Checked \- no plan impact.  
* PF18 — HDE Narrative Deliverables — Not applicable.  
* PF19 — Glow QA Guide — Applied: QA planning posture, QA/OPS separation, evidence posture, token claim posture, and Live QA boundary.  
* PF20 — HDE-Phased Epics — Historical-only.  
* PF21 — 7 Phases of Alchemical Engineering — Applied: Distillation phase mode and rationale.  
* PF23 — Reality Audits — Applied as planning-time consult only for component and locus framing; not acceptance proof and not current repo proof.  
* PF27 — Plan Templates — Applied: Epic Plan structure, PF23 consult posture, PF09 accountability, token inventory, close-pack baseline, and evidence pointer posture.  
* PF29 — HDE Users Guide — Applied: current operator-surface posture and mapped-cache nonclaim boundaries.  
* PF-Reference-Glow Story — Reference-only context.

## Business Case

### Problem statement

The HD Engine has accumulated multiple partially complete Distillation rows around gates, release identity, environment snapshots, identity provenance, evidence indexing, BodyGraph mechanics, DB posture, and mapped-cache persistence. This creates risk for the people operating and reviewing the Engine: repeated proof families may drift, identity may be scattered, evidence may become hard to trust, and runtime-facing changes may be overclaimed without durable proof.

### Proposed change

This epic will consolidate the core Distillation reliability slice: global evidence discipline, identity and provenance, release identity indexing, environment snapshotting, gate scripts, DB and BodyGraph posture proofs, architecture snapshots, controlled v2 mapped-cache persistence hardening, and a one-button release sanity pipeline. The intended effect is a repeatable, indexed, secret-safe, deterministic evidence and release-harness posture that future Distillation and Coagulation work can depend on.

### Value and impact

User-facing behavior is not expanded in this epic. The value is internal product reliability and risk reduction: operators, reviewers, and future implementation sessions get a stronger, more repeatable Engine proof surface. This reduces the chance that a later runtime, vendor, or production-facing claim is accepted from incomplete evidence.

### Why now

Distillation is the phase where the Engine turns repeated success into durable operating practice. The mapped PF09 Distillation rows are still open or partial across identity, evidence, gates, environment snapshotting, and release sanity. This epic addresses the coherent core reliability slice before the separate performance and load harness work is planned.

### What success looks like

Success means the in-scope PF09.6 subtasks are supportable to completion for this epic’s slice through implemented mechanics, governed evidence, Human Evidence Index and Machine Mirror binding, and truthful nonclaim boundaries. The plan does not require PF document drainage to complete implementation or QA; later status drainage remains separate.

### Scope boundaries

In scope:

* Distillation global discipline.  
* Identity and provenance module proof surface.  
* Pack, manifest, and release identity indexing.  
* Environment snapshot singleton and observability indexing.  
* Determinism, A7, CI rails, DB posture, BodyGraph, DB-bridge, architecture snapshot, v2 mapped-cache, and release sanity gate-harness work.  
* Required PO-only OPS support only where a mapped subtask requires external, credentialed, open-rails, DB, or infrastructure confirmation.

Out of scope:

* Performance and load harness rows for this epic.  
* Coagulation deployment hardening.  
* New public Reader behavior.  
* New public routes.  
* App-side HumanDesignAPI ownership.  
* Broad HumanDesignAPI v2 platform conformance.  
* PF document edits as implementation deliverables.  
* Live QA runbooks or QA execution steps.

### Non-goals

* This epic does not change public user copy.  
* This epic does not expand Reader public bytes.  
* This epic does not authorize production mapped-cache writes unless a separate controlled proof and authorization surface supports that posture.  
* This epic does not claim PF09 status movement by itself.  
* This epic does not close performance and load harness work.

## Contract and Compatibility Posture

### Contract changes and new surfaces

No new public user-facing contract is planned.

The epic may introduce or update internal, admin, evidence, harness, CI, and governed artifact surfaces needed to satisfy the mapped Distillation subtasks. All such surfaces are internal proof, operator, or evidence surfaces and must remain governed by their owning PF homes.

### Justification

The internal and evidence surfaces are necessary because the Business Case depends on repeatable proof, identity, release, environment, and mapped-cache durability. These cannot be proven by prose or PF09 status updates alone.

### Flag strategy

No new public feature flag is planned.

If implementation requires an internal or admin-only switch for controlled mapped-cache persistence, rails behavior, or harness proof selection, the switch must be justified in the Implementation Plan and routed to the owning PF home by title. It must not alter public Reader behavior, bypass the HD Engine vendor seam, expose secrets, or create app-side vendor ownership.

### Backward compatibility posture

Existing public Reader behavior remains unchanged by default. Existing closed-rails refusal posture must remain intact. Existing legacy non-v2 BodyGraph fallback behavior must remain preserved unless a separate owning-canon decision changes it. Existing evidence index and mirror homes remain unchanged.

### Open-rails QA declaration

Because this epic touches runtime persistence, DB connectivity, vendor route policy, BodyGraph mechanics, and operator-facing evidence surfaces, bounded open-rails QA is mandatory for any claim that depends on live external service, DB, vendor, credential, or production-like runtime behavior. Closed-rails proof may support closed-rails control flow and deterministic local behavior, but it must not be used to overclaim live vendor, DB, or production persistence behavior.

No Live QA runbook, command sequence, or step-level execution detail is included in this Epic Plan.

### Vendor-call ownership for Glow app integration

The HD Engine remains the default owner of vendor acquisition, persistence-facing behavior, retrieval-facing behavior, and compute-facing behavior. This epic does not authorize direct app-side HumanDesignAPI calls.

### Vendor payload normalization posture

The v2 mapped-cache persistence slice is planned as a bounded adapter-mapped persistence hardening task. It must write adapter-mapped HDE BodyGraph/cache payloads, not raw HumanDesignAPI v2 envelopes. It must prove write/read-back parity, idempotence, no raw vendor payload persistence, no secret persistence, and closed-rails refusal preservation.

### Adapter/schema gap and nonclaim posture

This epic does not claim that vendor chart data currently feeds the existing BodyGraph cache, person/cache contract, compatibility compute path, or full vendor runtime conformance before the mapped-cache persistence slice proves that exact behavior. Any proof must distinguish dry-run mapping, compatibility computation, durable cache write/read-back, and production authorization.

### bg:resolve route-policy posture

Any mapped-cache work involving `bg:resolve --source vendor` must state whether the selected path is configured-v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim. This epic does not treat `charts/simple` success, auth success, geocode-key success, provider availability, or route-family confirmation as proof of complete BodyGraph detail.

### Configured-v2 mapped-cache state separation

This epic distinguishes these states:

* v2 dry-run mapping works.  
* v2 mapped output can feed compatibility computation.  
* v2 mapped output can be durably written and read back from the BodyGraph cache.  
* v2 mapped-cache writes are authorized for production or production-like operation.

Only the states actually implemented and evidenced may be claimed.

## Existing Work Check

The current PF09.6 Distillation backbone records the in-scope rows as open, partial, not done, or optional. This Epic Plan does not treat any open row as already complete.

Repo access was scoped as read-only for planning. No current repo-content claim is required to determine the scope of this Epic Plan. All repo paths below are labeled as Existing by PF canon, Planned output, Proposed path, or Unknown. The Implementation Agent must verify current repo reality before editing or relying on any existing locus.

PF10 currently has no active live addendum that changes this epic’s scope. Where PF10 is silent, the owning PF-Canon home governs.

PF23 was consulted only for planning-time component and locus framing. PF23 does not create acceptance proof, implementation scope, PF09 status movement, QA PASS, OPS completion, or current repo truth.

## PF23 Anchors

Planning-time component anchors consulted for traceability only:

* Engine core and BodyGraph seams.  
* Adapter and Reader transport surfaces.  
* Presenter and single canonical emitter boundary.  
* BodyGraph cache and DB-facing persistence boundary.  
* Governed evidence roots.  
* Evidence index and machine mirror surfaces.  
* QA and audit roots.

These anchors are not deliverables, checks, acceptance tokens, or proof of current repo state.

## Planned Epic Scope

This epic includes the coherent Distillation reliability slice:

* Global discipline.  
* Identity and provenance.  
* Release identity indexing.  
* Environment snapshot indexing.  
* Determinism gates.  
* A7 transport gates.  
* CI rails gates.  
* DB posture runtime checks.  
* BodyGraph mechanics gates.  
* DB-bridge parity and environment connectivity.  
* Architecture snapshot evidence.  
* v2 mapped-cache persistence hardening.  
* One-button evidence harness and release sanity pipeline.

The performance and load harness rows are outside this epic. They remain mapped to PF09.6 and are recorded under future-scope notes below.

## Deliverables

### Deliverable D1 — Global discipline

Includes: \- HDE-DIST005.1, HDE-DIST005.2

PF14: HDE Mechanics Guide, §1.3.1 Evidence jobs and governed evidence discipline

PF09 completion: Complete in this epic

* Job to be done: Enforce Phase VI canonical encodings, locale pins, LF discipline, Human Evidence Index updates, hash sentinel updates, Machine Mirror updates, and path-proof coherence for all governed artifacts touched by this epic.  
* Evidence required: governed artifact refreshes use canonical JSON or LF-terminated text; the Human Evidence Index, hash sentinel, Machine Mirror, and required path proofs are updated in the same PR when artifact bytes change.  
* Planned outputs: Existing by PF canon: `docs/evidence/INDEX.json`; Existing by PF canon: `docs/evidence/INDEX.sha256`; Existing by PF canon: `artifacts/evidence_index.jsonl`; Existing by PF canon: `artifacts/evidence_index.jsonl.sha256`; Existing by PF canon: `artifacts/evidence_index.jsonl.path_proof.txt`.

### Deliverable D2 — Identity and provenance module

Includes: \- HDE-DIST006.1, HDE-DIST006.2, HDE-DIST006.3

PF14: HDE Mechanics Guide, §13 Identity & Provenance Module

PF09 completion: Complete in this epic

* Job to be done: Make identity fields, identity helpers, parity behavior, and identity hash evidence supportable as the single source of truth for engine and release identity.  
* Evidence required: identity field set, identity helper use, public identity parity, admin identity snapshot, release ID proof, emitter hash proof, invocation hash proof, and mirror discipline.  
* Planned outputs: Planned output: `artifacts/identity/release_id.json`; Planned output: `artifacts/identity/release_id_recompute.log`; Planned output: `artifacts/parity/two_run_identity.log`; Planned output: `artifacts/identity/service_identity.json`; Planned output: `artifacts/identity/emitter_sha256.json`; Planned output: `artifacts/identity/invocation_sha256.json`; Existing by PF canon: `docs/evidence/INDEX.json`; Existing by PF canon: `artifacts/evidence_index.jsonl`.

### Deliverable D3 — Release identity indexing

Includes: \- HDE-DIST002.4, HDE-DIST002.5

PF14: HDE Mechanics Guide, §1.3.1 Evidence jobs and §13.6 Evidence

PF09 completion: Complete in this epic

* Job to be done: Bind pack, manifest, and release identity artifacts into Human Evidence Index and Machine Mirror, and produce release bindings evidence tied to BodyGraph data source policy and refresh behavior.  
* Evidence required: pack/manifest identity artifacts indexed and mirrored with path proofs; release bindings artifact produced as canonical JSON and indexed in the same PR.  
* Planned outputs: Existing by PF canon: `docs/evidence/INDEX.json`; Existing by PF canon: `docs/evidence/INDEX.sha256`; Existing by PF canon: `artifacts/evidence_index.jsonl`; Planned output: `artifacts/bodygraph/release_bindings.json`; Planned output: `artifacts/bodygraph/release_bindings.json.path_proof.txt`.

### Deliverable D4 — Environment snapshot indexing

Includes: \- HDE-DIST003.1, HDE-DIST003.4

PF14: HDE Mechanics Guide, §1.3 Evidence and environment-pins evidence surface

PF09 completion: Complete in this epic

* Job to be done: Produce the singleton environment snapshot in the required v3 posture and bind environment snapshot, logs, and metrics evidence through the Evidence Index and Machine Mirror where this epic changes or refreshes those artifacts.  
* Evidence required: singleton environment snapshot canonical JSON, schema-v3 posture, determinism pins, presence map, indexing, mirror row, and path-proof coherence.  
* Planned outputs: Existing by PF canon: `artifacts/runtime/env_matrix.snapshot.json`; Existing by PF canon: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`; Existing by PF canon: `docs/evidence/INDEX.json`; Existing by PF canon: `artifacts/evidence_index.jsonl`.

### Deliverable D5 — Determinism gates

Includes: \- HDE-DIST001.1

PF14: HDE Mechanics Guide, §1.3.1 Evidence jobs and §13 Identity & Provenance Module

PF09 completion: Complete in this epic

* Job to be done: Implement and bind deterministic gates for preimage recompute, Reader to CLI parity, AB to BA coherence, two-run identity, and canonical JSON comparison.  
* Evidence required: parity artifacts, deterministic identity artifacts, canonical JSON compare logs, and governed index/mirror binding.  
* Planned outputs: Existing by PF09/PF12 path posture: `audit/gates/parity/reader_cli/ab.json`; Existing by PF09/PF12 path posture: `audit/gates/parity/reader_cli/ba.json`; Existing by PF09/PF12 path posture: `audit/gates/parity/reader_cli/summary.json`; Existing by PF09/PF12 path posture: `audit/gates/determinism/abba.bytes`; Existing by PF09/PF12 path posture: `audit/gates/determinism/tworun_identity.sha256`; Existing by PF09/PF12 path posture: `audit/gates/canonical_json/json_canon_compare.log`; Planned or existing by PF09 path posture: `artifacts/cards/A3/IDENTITY_OK.txt`.

### Deliverable D6 — A7 transport gates

Includes: \- HDE-DIST001.2

PF14: HDE Mechanics Guide, A7 transport harness posture and governed A7 proof exception

PF09 completion: Complete in this epic

* Job to be done: Prove A7 transport behavior on a Catalog JSON success route without using `/internal/version` as an A7 proof surface.  
* Evidence required: Endpoint Catalog snapshot, success GET, HEAD, 304, writer/error posture, encoding invariance, environment-gate proof, and governed index/mirror binding.  
* Planned outputs: Existing by PF canon: `docs/ENDPOINTS_CATALOG.json`; Existing by PF canon: `docs/ENDPOINTS_CATALOG.json.sha256`; Planned output: `artifacts/reader/endpoints_snapshot.json`; Planned output: `artifacts/proofs/success_get.txt`; Planned output: `artifacts/proofs/success_head.txt`; Planned output: `artifacts/proofs/success_304.txt`; Planned output: `artifacts/proofs/success_writers_errors.txt`; Planned output: `artifacts/proofs/encoding_invariance.txt`; Planned output: `artifacts/proofs/endpoints_env_gate_proof.log`.

### Deliverable D7 — CI rails gates

Includes: \- HDE-DIST001.3

PF14: HDE Mechanics Guide, §1.3 Evidence jobs and HDAPI rails mechanics posture

PF09 completion: Complete in this epic

* Job to be done: Enforce closed-rails default posture, bounded open-rails exception posture, typed refusal behavior, retry and backoff proof posture, and keys-only evidence for rails-sensitive harnesses.  
* Evidence required: closed-rails refusal proof, open-rails conformance proof where authorized, logs redaction proof, canonical refusal fixtures, and governed index/mirror binding.  
* Planned outputs: Proposed path: `ci/jobs/rails_closed_refusal.yml`; Proposed path: `ci/jobs/rails_open_conformance.yml`; Proposed path: `ci/jobs/logs_keys_only_redaction.yml`; Planned output: closed-rails refusal fixture under a governed evidence root selected by HDE-Schemas & Artifacts; Planned output: rails posture sanity log under a governed evidence root selected by HDE-Schemas & Artifacts.  
* OPS posture: PO-only execution is required for any open-rails external confirmation. This plan does not include OPS procedures or commands.

### Deliverable D8 — DB posture runtime checks

Includes: \- HDE-DIST001.4

PF14: HDE Mechanics Guide, BodyGraph and DB runtime seam posture

PF09 completion: Complete in this epic

* Job to be done: Use the Distillation harness to prove DB runtime posture for the HDE-FERM004 semantic boundary without importing new Fermentation scope.  
* Evidence required: DB schema/search-path posture, grants, DDL fingerprint, constraints, boundary view read-only proof, runtime environment connectivity snapshot, secret-free logs, and governed index/mirror binding.  
* Planned outputs: Existing by PF09/PF12 path posture: `artifacts/db/ddl_fingerprint.json`; Existing by PF09/PF12 path posture: `artifacts/db/grants.txt`; Existing by PF09/PF12 path posture: `artifacts/db/check_schema.txt`; Existing by PF09/PF12 path posture: `artifacts/db/check_constraints.txt`; Proposed path: `artifacts/db/boundary_view.readonly.proof`; Existing by PF canon: `artifacts/runtime/env_connectivity.snapshot.json`.  
* OPS posture: PO-only support may be required if runtime DB facts must be captured from privileged or production-like environments. This plan does not include OPS procedures or commands.

### Deliverable D9 — BodyGraph mechanics gates

Includes: \- HDE-DIST001.5

PF14: HDE Mechanics Guide, BodyGraph seam posture and HDAPI v2 request-shaping and response-mapping mechanics

PF09 completion: Complete in this epic

* Job to be done: Prove BodyGraph source selection, source invariance, vendor-disabled production posture where applicable, TTL and stale-while-revalidate policy, rate-limit policy, circuit-breaker policy, and keys-only evidence posture.  
* Evidence required: BodyGraph source selection snapshot, source invariance pair artifacts, refresh policy snapshot, metrics snapshot, and keys-only logs sample.  
* Planned outputs: Existing by PF09/PF12 path posture: `artifacts/bodygraph/source_selection.snapshot.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/source_invariance/ab.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/source_invariance/ba.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/source_invariance/summary.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/refresh_policy.snapshot.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/metrics.snapshot.json`; Existing by PF09/PF12 path posture: `artifacts/bodygraph/keys_only.logs.sample`.  
* Token posture: BodyGraph policy labels that are not confirmed in the Governance token registry must be handled as proof obligations unless registry validation confirms exact token admission.

### Deliverable D10 — DB-bridge parity and environment connectivity

Includes: \- HDE-DIST001.9

PF14: HDE Mechanics Guide, BodyGraph seam posture and operational unknowns posture

PF09 completion: Complete in this epic

* Job to be done: Prove parity between direct DB reads and bridge-mediated reads for BodyGraph and capture associated environment connectivity posture.  
* Evidence required: vendor upsert transcript, DB resolve transcript, canonical compare log, environment connectivity snapshot, secret-free evidence, Human Evidence Index entry, Machine Mirror record, and path-proof binding.  
* Planned outputs: Proposed path: `artifacts/bodygraph/vendor_upsert.<alias>.json`; Proposed path: `artifacts/bodygraph/db_resolve.<alias>.json`; Existing by PF09/PF12 path posture: `artifacts/presenter/json_canon_compare.log`; Existing by PF canon: `artifacts/runtime/env_connectivity.snapshot.json`.  
* OPS posture: PO-only support may be required where bridge or DB facts require privileged access. This plan does not include OPS procedures or commands.

### Deliverable D11 — Architecture snapshot evidence

Includes: \- HDE-DIST001.10

PF14: HDE Mechanics Guide, audit classification for I/O-bearing engine seams and architecture boundary-proof mechanics

PF09 completion: Complete in this epic

* Job to be done: Produce a keys-only architecture snapshot that reflects the Engine’s public and internal surfaces without secrets, raw birth data, credentials, sensitive headers, or raw vendor payloads.  
* Evidence required: canonical JSON architecture snapshot, keys-only verification, Human Evidence Index entry, Machine Mirror record, and path-proof binding.  
* Planned outputs: Proposed path: `artifacts/architecture/architecture_snapshot.keys_only.json`; Proposed path: `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
* Contract posture: The architecture snapshot is an evidence artifact, not a new public surface.

### Deliverable D12 — v2 mapped-cache persistence hardening

Includes: \- HDE-DIST001.11

PF14: HDE Mechanics Guide, HDAPI v2 request-shaping and response-mapping mechanics, BodyGraph resolver route-policy classification, and mapped-cache persistence mechanics

PF09 completion: Complete in this epic

* Job to be done: Implement and prove safe durable mapped-cache persistence for configured-v2 chart-backed BodyGraph resolution in a controlled, non-prod or explicitly authorized rails posture.  
* Evidence required: mapped output before write, cached output after DB read, canonical-equivalence evidence for governed fields, idempotence evidence, no raw vendor payload persistence proof, no secret persistence proof, closed-rails refusal proof, legacy fallback preservation proof, Human Evidence Index update, Machine Mirror update, hash sentinel update, and path-proof binding.  
* Planned outputs: Proposed path: `artifacts/bodygraph/v2_mapped_cache/write_transcript.json`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/canonical_parity.log`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/idempotence.log`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log`; Proposed path: `artifacts/bodygraph/v2_mapped_cache/manifest.json`.  
* OPS posture: PO-only support is required for any credentialed, open-rails, live vendor, or production-like DB confirmation. Implementation work must not claim OPS completion. This plan does not include OPS procedures or commands.  
* Nonclaims: This deliverable does not claim public Reader changes, new public routes, app-side HumanDesignAPI ownership, raw v2 vendor envelope persistence, QA PASS, PF09 status movement, OPS completion, closeout, production deployment, or broad HumanDesignAPI v2 platform conformance.

### Deliverable D13 — Release sanity pipeline

Includes: \- HDE-DIST001.6

PF14: HDE Mechanics Guide, §1.3.1 Evidence jobs and release sanity pipeline harness posture

PF09 completion: Complete in this epic

* Job to be done: Implement or complete the one-button evidence harness and release sanity pipeline so it drives the in-scope Distillation proof families in deterministic order and fails closed on drift.  
* Evidence required: release sanity transcript, deterministic env pins, ordered step results, index and mirror parity, path-proof validation, and canonical text or JSON outputs.  
* Planned outputs: Existing by PF09/PF12 path posture: `artifacts/proofs/sanity_pipeline.transcript.log`; Planned output: `artifacts/proofs/sanity_pipeline.transcript.log.path_proof.txt`; Existing by PF canon: `docs/evidence/INDEX.json`; Existing by PF canon: `docs/evidence/INDEX.sha256`; Existing by PF canon: `artifacts/evidence_index.jsonl`.

## Work Category Separation

### Implementation work

Deliverables D1 through D13 are implementation and evidence-harness workstreams. They may include code, tests, tooling, governed artifacts, or evidence refreshes, but they must preserve PF ownership and repo truth.

### OPS work

OPS work is PO-only and IA-guided. OPS support may be needed for D7, D8, D10, and D12 if external, credentialed, open-rails, production-like DB, vendor, environment, or infrastructure facts must be observed. OPS work must produce secret-free governed evidence under a lowercase governed root, but the Epic Plan does not prescribe OPS procedures.

### QA planning

QA planning is expected later under Glow QA Guide and Plan Templates. This Epic Plan names QA posture and proof obligations only.

### QA execution

QA execution is not included in this Epic Plan. No Live QA steps, commands, logs, or runbook content are embedded here.

### Documentation drainage

Documentation drainage is not an execution deliverable, acceptance gate, QA gate, closeout blocker, or PR task. Doc-delta candidates may be recorded, but PF document edits remain separate documentation work.

### Canon updates

No PF-canon edits are required as implementation outputs for this epic.

### Acceptance posture

Acceptance token claims must be registry-valid before final acceptance artifacts claim them. Proof obligations that are not registry-confirmed must remain non-token evidence obligations until admitted by Governance or PF10.

### Historical context

PF20 is historical-only and is not used to create planning scope.

### Repo-reality consult context

Repo reality must be revalidated by the Implementation Agent before editing, relying on, or claiming existing code paths, tests, modules, commands, or artifacts.

## PF09 Completion Map

### HDE-DIST005.1

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST005  
* PF09 subtask ID(s): HDE-DIST005.1  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D1  
* Notes: Global discipline canonical encodings and environment pins.

### HDE-DIST005.2

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST005  
* PF09 subtask ID(s): HDE-DIST005.2  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D1  
* Notes: Evidence Index and Machine Mirror discipline for artifact movement in this phase.

### HDE-DIST006.1

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST006  
* PF09 subtask ID(s): HDE-DIST006.1  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D2  
* Notes: Identity fields and source-of-truth posture.

### HDE-DIST006.2

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST006  
* PF09 subtask ID(s): HDE-DIST006.2  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D2  
* Notes: Identity helper and parity posture.

### HDE-DIST006.3

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST006  
* PF09 subtask ID(s): HDE-DIST006.3  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D2  
* Notes: Identity hashes and mirror discipline.

### HDE-DIST002.4

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST002  
* PF09 subtask ID(s): HDE-DIST002.4  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D3  
* Notes: Pack and manifest indexing.

### HDE-DIST002.5

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST002  
* PF09 subtask ID(s): HDE-DIST002.5  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D3  
* Notes: Release bindings evidence and indexing.

### HDE-DIST003.1

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST003  
* PF09 subtask ID(s): HDE-DIST003.1  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D4  
* Notes: Environment snapshot singleton v3.

### HDE-DIST003.4

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST003  
* PF09 subtask ID(s): HDE-DIST003.4  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D4  
* Notes: Environment snapshot and observability indexing.

### HDE-DIST001.1

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.1  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D5  
* Notes: Determinism gates.

### HDE-DIST001.2

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.2  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D6  
* Notes: A7 transport gates on Catalog route.

### HDE-DIST001.3

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.3  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D7  
* Notes: CI rails closed/open policy and rails gates.

### HDE-DIST001.4

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.4  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D8  
* Notes: DB posture and runtime checks for the HDE-FERM004 semantic boundary.

### HDE-DIST001.5

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.5  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D9  
* Notes: BodyGraph mechanics gates.

### HDE-DIST001.9

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.9  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D10  
* Notes: DB-bridge parity and environment connectivity.

### HDE-DIST001.10

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.10  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D11  
* Notes: Architecture snapshot keys-only evidence.

### HDE-DIST001.11

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.11  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D12  
* Notes: Optional row planned in this epic as controlled mapped-cache persistence hardening. PF09 status remains unchanged until later PO-governed status drainage.

### HDE-DIST001.6

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST001  
* PF09 subtask ID(s): HDE-DIST001.6  
* Disposition: Complete in this epic  
* Plan work item, deliverable, or Tracked Issue: Deliverable D13  
* Notes: One-button evidence harness and release sanity pipeline.

## Outside This Epic or Future-Scope Notes

### Performance and Load Harness

* PF09.x document: PF09.6-Canon-HDE-Build-Checklist-Distillation  
* PF09 task ID: HDE-DIST004  
* PF09 subtask ID(s): HDE-DIST004.1, HDE-DIST004.2, HDE-DIST004.3, HDE-DIST004.4  
* Disposition: Deferred with rationale  
* Plan work item, deliverable, or Tracked Issue: Future-scope note  
* Notes: The performance and load harness is a coherent Distillation workstream, but it is distinct from this epic’s core reliability, identity, environment, evidence-harness, and mapped-cache persistence slice. It remains PF09-accounted and is not silently dropped.

## PF Reference Map

### Core

* PF21 — 7 Phases of Alchemical Engineering  
* PF27 — Plan Templates  
* PF09.6 — HDE-Build-Checklist-Distillation  
* PF06 — Epic Process Guide  
* PF19 — Glow QA Guide

### Additional

* PF01 — HDE-Math-Spec  
* PF02 — HDE Architecture  
* PF03 — Technical Writing Best Practices  
* PF04 — HDE Governance  
* PF05 — HDE-CLI-API-Vendor-Ref  
* PF07 — Glow Infrastructure  
* PF09.5 — HDE-Build-Checklist-Fermentation  
* PF12 — HDE-Schemas & Artifacts  
* PF14 — HDE Mechanics Guide  
* PF23 — Reality Audits  
* PF29 — HDE Users Guide

### Historical-only

* PF20 — HDE-Phased Epics

## Tokens and Evidence (Acceptance)

### A. Acceptance tokens

#### A1. Baseline tokens

* `TESTS_PASS_OK`  
* `DOC_DELTA_PRESENT_OK`  
* `EVIDENCE_INDEX_UPDATED_OK`  
* `MACHINE_MIRROR_UPDATED_OK`  
* `EVIDENCE_INDEX_HASH_OK`

#### A2. QA rail tokens

* `QA_PRECOMMIT_CHECKLIST_OK`  
* `QA_POSTCOMMIT_CHECKLIST_OK`  
* `ENV_RAILS_POLICY_OK`

#### A3. Phase-specific tokens

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
* `ENV_LC_ALL_C_OK`  
* `EVIDENCE_INDEX_MIRROR_OK`  
* `EVIDENCE_PATHS_VALIDATED_OK`  
* `DB_RUNTIME_SEARCH_PATH_OK`  
* `DB_ROLE_OK`  
* `DB_SCHEMA_FINGERPRINT_OK`  
* `DB_CONN_ENV_OK`  
* `DEV_DB_BRIDGE_FALLBACK_OK`  
* `EVIDENCE_PATH_PROOFS_OK`  
* `CI_CHECK_MIRROR_SCHEMA_OK`  
* `CI_CHECK_FINAL_LF_OK`  
* `NO_EXTERNAL_IO_ON_REFUSAL_OK`  
* `RELEASE_ID_RECOMPUTE_OK`

### Token Inventory

* `TESTS_PASS_OK` — Required baseline token from Plan Templates; acceptance artifacts must registry-check before final claim.  
* `DOC_DELTA_PRESENT_OK` — Canonical acceptance token source: HDE Governance.  
* `EVIDENCE_INDEX_UPDATED_OK` — Canonical acceptance token source: HDE Governance.  
* `MACHINE_MIRROR_UPDATED_OK` — Canonical acceptance token source: HDE Governance.  
* `EVIDENCE_INDEX_HASH_OK` — Canonical acceptance token source: HDE Governance.  
* `QA_PRECOMMIT_CHECKLIST_OK` — Canonical acceptance token source: HDE Governance.  
* `QA_POSTCOMMIT_CHECKLIST_OK` — Canonical acceptance token source: HDE Governance.  
* `ENV_RAILS_POLICY_OK` — Canonical acceptance token source: HDE Governance.  
* `PREIMAGE_RECOMPUTE_OK` — Canonical acceptance token source: HDE Governance.  
* `CLI_READER_PARITY_OK` — Canonical acceptance token source: HDE Governance.  
* `COMPOSITE_ABBA_IDENTITY_OK` — Canonical acceptance token source: HDE Governance.  
* `TWO_RUN_IDENTITY_OK` — Canonical acceptance token source: HDE Governance.  
* `JSON_CANONICAL_CHECK_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_GET_QUOTED_ETAG_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_HEAD_PARITY_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_304_OMITS_CT_CL_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_VARY_AUTH_AE_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_ENCODING_INVARIANCE_OK` — Canonical acceptance token source: HDE Governance.  
* `A7_TRANSPORT_PROOF_OK` — Canonical acceptance token source: HDE Governance.  
* `ENDPOINTS_CATALOG_OK` — Canonical acceptance token source: HDE Governance.  
* `ENDPOINTS_CATALOG_ENV_GATE_OK` — Canonical acceptance token source: HDE Governance.  
* `ENV_LC_ALL_C_OK` — Canonical acceptance token source: HDE Governance.  
* `EVIDENCE_INDEX_MIRROR_OK` — Canonical acceptance token source: HDE Governance.  
* `EVIDENCE_PATHS_VALIDATED_OK` — Canonical acceptance token source: HDE Governance.  
* `DB_RUNTIME_SEARCH_PATH_OK` — Canonical acceptance token source: HDE Governance.  
* `DB_ROLE_OK` — Canonical acceptance token source: HDE Governance.  
* `DB_SCHEMA_FINGERPRINT_OK` — Canonical acceptance token source: HDE Governance.  
* `DB_CONN_ENV_OK` — Canonical acceptance token source: HDE Governance.  
* `DEV_DB_BRIDGE_FALLBACK_OK` — Canonical acceptance token source: HDE Governance.  
* `EVIDENCE_PATH_PROOFS_OK` — Canonical acceptance token source: HDE Governance.  
* `CI_CHECK_MIRROR_SCHEMA_OK` — Canonical acceptance token source: HDE Governance.  
* `CI_CHECK_FINAL_LF_OK` — Canonical acceptance token source: HDE Governance.  
* `NO_EXTERNAL_IO_ON_REFUSAL_OK` — Canonical acceptance token source: HDE Governance.  
* `RELEASE_ID_RECOMPUTE_OK` — Canonical acceptance token source: HDE Governance.

### Non-token proof obligations pending registry validation

These PF09 row-listed labels must not be claimed as satisfied acceptance tokens unless registry validation confirms exact admission in HDE Governance or live HDE Build Notes:

* `BG_SOURCE_SELECTION_OK`  
* `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`  
* `BG_SOURCE_INVARIANCE_OK`  
* `BG_TTL_SWR_POLICY_OK`  
* `BG_RATE_LIMIT_POLICY_OK`  
* `BG_CIRCUIT_BREAKER_POLICY_OK`  
* `ENV_SNAPSHOT_SINGLETON_OK`  
* `ENV_SNAPSHOT_SCHEMA_V3_OK`  
* `ENV_PINS_PRESENT_OK`

They remain valid evidence obligations for the mapped PF09 work, but acceptance artifacts must not overclaim them as tokens unless admitted.

### B. Evidence pointers

#### Canonical close-pack baseline

* Planned output: `audit/EPIC-038_close_report.md`  
* Planned output: `audit/EPIC-038_MANIFEST.json`  
* Planned output: `docs/acceptance_map_epic038.json`  
* Planned output: `docs/acceptance_map_epic038.json.path_proof.txt`  
* Planned output: `audit/qa/hde-epic038/token_evidence_matrix.md`  
* Planned output: `audit/qa/hde-epic038/acceptance_map_viability.log`

#### Canonical doc-delta baseline

* Planned output: `audit/docdeltas/hde-epic038_doc_deltas.md`  
* Planned output: `audit/qa/hde-epic038/00_meta/doc_deltas.md`

#### Canonical evidence ledger surfaces

* Existing by PF canon: `docs/evidence/INDEX.json`  
* Existing by PF canon: `docs/evidence/INDEX.sha256`  
* Existing by PF canon: `docs/evidence/INDEX.json.path_proof.txt`  
* Existing by PF canon: `docs/evidence/INDEX.sha256.path_proof.txt`  
* Existing by PF canon: `artifacts/evidence_index.jsonl`  
* Existing by PF canon: `artifacts/evidence_index.jsonl.sha256`  
* Existing by PF canon: `artifacts/evidence_index.jsonl.path_proof.txt`  
* Existing by PF canon: `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

#### Epic QA root

* Planned output root: `audit/qa/hde-epic038/`

This is a planning-level root only. The Epic Plan does not define Live QA runbook paths or QA execution steps.

### C. Evidence Index Refresh Flow

The epic must use the canonical evidence refresh posture owned by HDE-Schemas & Artifacts and Epic Process Guide. Any generated or refreshed governed artifact must be bound in the Human Evidence Index and Machine Mirror in the same PR as the artifact change, with hash sentinel and path-proof posture preserved.

### D. Normative completion rule

The epic may be proposed for Done only after implementation, OPS evidence where required, QA evidence where required, governed evidence binding, and truthful review artifacts support the mapped scope. The Epic Plan itself does not perform PF09 status movement, QA PASS, OPS completion, PO closeout, merge, or board update.

## QA Rails \- Open/Close

### Final PR rails posture

Closed rails are the default for CI and deterministic proof runs.

Opened rails are allowed only as a bounded, PO-authorized exception where needed for live vendor, DB, bridge, environment, credential, or production-like runtime proof. Opened-rails evidence must be secret-free, governed, and separately recorded. This plan does not include open-rails commands or procedures.

### Live QA requirement

Live QA is required for eventual epic close under Epic Process Guide and Glow QA Guide. This plan does not embed a Live QA Plan or runbook.

### QA-heavy posture

This epic is not a QA-only epic. QA-related work exists to support implementation and evidence trust for Distillation reliability work.

## Tracked Issues

### TI-001

* Issue ID: TI-001  
* Title: PF09 row-listed proof labels require registry-safe acceptance handling  
* Type: token gap  
* What is unresolved: Several PF09.6 row-listed labels appear necessary as proof obligations but are not treated in this plan as acceptance tokens unless Governance or HDE Build Notes confirms exact registry admission.  
* Why it matters for this epic: Acceptance artifacts must not claim unregistered or local token names as satisfied acceptance tokens.  
* Controlling PF touchpoints by title: HDE Governance; HDE Build Notes; Plan Templates; HDE-Build-Checklist-Distillation.  
* Required decision or proof: Final acceptance artifacts must registry-validate token spelling and treat any unregistered label as a non-token proof obligation or route token admission through Governance.  
* Impact on executable work: Does not block implementing or evidencing the mapped work. Blocks only unsupported token claims.

## ADR Stubs

None.

## Plan Preflight

### Token registry validation

Acceptance token claims in this plan are limited to the Token Inventory above. Non-token proof obligations pending registry validation are explicitly separated and must not be claimed as satisfied acceptance tokens unless admitted.

### Close-pack baseline declared

The close-pack baseline is declared in the Tokens and Evidence section. The baseline includes the close report, close manifest, acceptance map, token-evidence matrix, acceptance-map viability log, and doc-delta surfaces.

### Evidence bundle completeness

Any deliverable that emits bundle-style evidence must provide a text-based bundle, bundle manifest, Human Evidence Index binding, Machine Mirror binding, and sibling path-proof posture under HDE-Schemas & Artifacts. No compressed or binary bundle may be the sole governed evidence for an acceptance claim.

### Canonical evidence-path binding validation

All concrete evidence paths in this plan are labeled Existing by PF canon, Existing by PF09/PF12 path posture, Planned output, Proposed path, or Unknown. The Implementation Agent must verify current repo reality and PF12 catalog binding before editing, generating, or claiming any path.

### Repo-content claim posture

This plan does not rely on current repo existence for its scope decision. Planned and proposed paths do not claim current existence. Existing-by-PF-canon paths rely on owning PF documents, not on unverified repository memory.

### OPS preflight

Any external, credentialed, production-like, DB, bridge, vendor, environment, or open-rails confirmation is PO-only and IA-guided. Automated agents must not perform OPS, claim OPS completion, simulate external state, or expose secrets.

### PF23 consult

PF23 was used only as planning-time context for component and locus framing. PF23 is not an acceptance source, token source, task source, proof source, blocker source by itself, or update target.

### PF09 accountability

Every in-scope task-like item is mapped to exact PF09.6 subtasks. Performance and load harness work is explicitly out of this epic and remains mapped to PF09.6 as future scope. No task-like backlog is left unaccounted.

### QA boundary

This Epic Plan does not include a QA Plan, Live QA runbook, QA command sequence, QA step list, QA evidence log layout, PR review, implementation instructions, remediation guide, final review, closeout review, or OPS procedure.

## Final Plan Notes

This plan selects the largest coherent Distillation Pass 3 scope that can be safely planned as one epic without importing the distinct Performance & Load Harness workstream. The epic advances the core reliability, identity, evidence, environment, gate, BodyGraph, DB, mapped-cache, and release sanity surface while preserving QA/OPS separation, PF09 subtask-level mapping, PF10 silence posture, evidence single-home discipline, and public-surface nonclaims.

ASK OK?  
