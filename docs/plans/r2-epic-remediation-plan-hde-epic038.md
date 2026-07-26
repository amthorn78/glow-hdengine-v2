# Epic Remediation Plan HDE-EPIC038

Version: r2  
Status: Approved  
Prepared: 2026-07-26  
Epic: HDE-EPIC038 \- Distillation Pass 3  
Repository: `amthorn78/glow-hdengine-v2`  
Validated repository baseline: `main@801c82ebfa46aebb4deea096c552acd2c67358bb`

## Artifact Map

Inputs:

* Current-conversation QA readiness findings, including `RCF-005`, Required Additional Work `PR-01`, and `Decision: NOT QA READY` \- provenance only; not required to execute.  
* `r1 Epic Plan HDE-EPIC038.md`.  
* `r6 Implementation Plan HDE-EPIC038.md`.  
* `PF10-HDE-Build-Notes-v12.4.3.md`, Addendum 2.23.  
* `PF23-Canon-Reality-Audits-v1.1.8.md` \- planning-time provenance only; not execution, acceptance, or proof authority.  
* `PF02-Canon-HDE-Architecture-v2.3.8.md`.  
* Current Repo copy of `PF09.6-Canon-HDE-Build-Checklist-Distillation-v1.1.2.md`.  
* Current Repo copy of `PF27-Canon-Plan-Templates-v1.9.5.md`.  
* `glow_dev_board_bundle.json` \- board provenance only. The supplied bundle is dated 2026-07-10 and contains no `HDE-EPIC038` item, so it supplies no current Epic state for this plan.  
* Read-only Repo inspection at the validated baseline.

Output:

* This Epic Remediation Plan for approval.

No external attachment is required to execute the approved plan. The operative non-PF Repo facts are embedded below.

## Executive Summary

HDE-EPIC038 is not ready to enter QA because the app factory selected by production and local launchers omits the existing compatibility blueprint. `Procfile`, `scripts/start_web.sh`, and `run_flask.py` select `adapter.factory:create_app()`. That factory mounts the Reader blueprint but not the existing internal/admin compatibility surface at `/api/compat/v1`, while the other observed factories mount both.

The remediation is one bounded DEV PR. It will:

* Mount the existing compatibility blueprint in the selected canonical factory without creating a route, handler, payload, public contract, or second HTTP home.  
* Make existing compatibility contract and parity tests exercise the factory selected by production and local launchers.  
* Make the existing keys-only architecture snapshot fail closed if the selected factory loses required Reader or compatibility registration.  
* Regenerate the existing architecture evidence and coherently refresh its Human Index, Machine Mirror, checksum, and path-proof bindings.  
* Run the existing closed-rails test and nineteen-stage release-sanity posture.

No OPS task, vendor call, database action, deployment, QA run, QA verdict, PF edit, PF09 status change, acceptance claim, or Epic closure is authorized.

## Scope

### In scope

* `PR-01 - Canonical adapter factory route-mount parity`.  
* The factory selected by the existing production and local launchers.  
* The existing Reader blueprint and existing `compat_blueprint`.  
* Existing route-inventory, compatibility-contract, parity, architecture-snapshot, evidence-index, and release-sanity proof surfaces.  
* Closed-rails, repo-local verification.

### Out of scope

* New public Reader behavior.  
* A new public or internal route.  
* Changes to `/api/compat/v1` request or response contracts.  
* Broad consolidation or deletion of every `create_app()` implementation.  
* Reclassification of `/api/compat/v1` from `internal_admin`.  
* Changes to `docs/ENDPOINTS_CATALOG.json` unless current Repo discovery contradicts the embedded catalog fact. Such a contradiction stops this plan for PO review.  
* Changes to `Procfile`, `scripts/start_web.sh`, or `run_flask.py`. They are selection anchors, not planned edit targets.  
* Schema changes to `schemas/architecture_snapshot.keys_only.v1.json`.  
* Vendor, DB, credentialed, network, infrastructure, deployment, or production operations.  
* QA planning, QA execution, QA evidence capture, QA PASS/FAIL judgment, or closeout.  
* PF09.6, PF14, PF23, PF10, board, or other PF/document edits as PR outputs.

## Canon Frame: What Correct Means

* Adapter owns route registration and transport wiring. Multiple `create_app()` implementations may exist, but production startup must delegate to one canonical adapter app factory entrypoint to avoid divergent route mounting. Source: PF02 \- HDE Architecture, §1.1, “Single homes.”  
* The dev/QA Reader harness is responsible for mounting the existing compat HTTP surface at `/api/compat/v1`. Source: PF02 \- HDE Architecture, §3.8.1, “Dev/QA Reader availability.”  
* `/api/compat/v1` is the existing adapter compatibility surface and is not a new route created by this remediation. Source: PF02 \- HDE Architecture, §3.1, “Compat v1.”  
* The keys-only architecture snapshot must reflect public and internal Engine surfaces, remain canonical and secret-free, and stay bound through the governed Evidence Index discipline. Source: PF09.6 \- HDE Build Checklist Distillation, `HDE-DIST001.10`.  
* The exact current remediation trigger is PF10 Addendum 2.23 `FND-004 - SD-02`: the selected factory omits the compat blueprint mounted by adjacent factories.  
* This Epic Remediation Plan uses one bounded DEV remediation step with embedded verification, explicit lane separation, and an approval sentinel. PF27 does not yet define this plan type; temporary review posture is governed by PF10 Addendum 2.25 until drained into PF27.

## PF09 Accountability

Classification: `PF09 gap`.

Current `PF09.6-Canon-HDE-Build-Checklist-Distillation-v1.1.2.md` contains no direct subtask for canonical app-factory route-mount parity. A complete-document search for `app factor`, `create_app`, `canonical adapter app factory`, `route mounting`, `route-mount`, and `factory parity` found no matching task language.

Related context is `HDE-DIST001.10 - Architecture snapshot (keys-only) evidence`, but that row does not directly own the selected-factory runtime correction. This plan does not remap the remediation to `HDE-DIST001.10`, reopen its completed HDE-EPIC038 implementation slice, or claim a PF09 status change.

PF10 Addendum 2.23 proposes a later PF09.6 task delta with no assigned task ID or status. This plan does not invent either field. Any PF09.6 or PF14 delta remains non-mandatory, PO-owned documentation drainage after implementation and is not an approval, merge, QA-entry, or completion condition for this PR.

## PF23 Anchors

PF23 was consulted only for planning-time names and loci:

* Components: adapter app factories, Reader blueprint, compatibility blueprint, launch entrypoints, Endpoint Catalog, and architecture snapshot.  
* Loci: `adapter/factory.py`, `adapter/http_reader.py`, `adapter/wsgi.py`, `engine/http/compat_handler.py`, `Procfile`, `scripts/start_web.sh`, `run_flask.py`, and `docs/ENDPOINTS_CATALOG.json`.

PF23 supplies no command, required output, acceptance token, blocker, status, QA result, or current Repo proof. The current Repo inspection below controls current-state claims.

## Observed Evidence Snapshot

### Selected launchers

At `main@801c82ebfa46aebb4deea096c552acd2c67358bb`:

* `Procfile` contains `adapter.factory:create_app()`.  
* `scripts/start_web.sh` constructs its gunicorn command with `adapter.factory:create_app()`.  
* `run_flask.py` imports `create_app` from `adapter.factory`.

These three launch paths select the same factory.

### Current factory divergence

The complete current `adapter/factory.py`:

* Imports `bp` from `adapter.http_reader`.  
* Registers `bp` at the root.  
* Preserves internal-route ETag stripping.  
* Does not import or register `compat_blueprint`.

Negative-search proof: complete-file, case-insensitive search of `adapter/factory.py` for `compat` returns zero hits.

Adjacent factories:

* `adapter/wsgi.py:create_app()` registers `reader_bp` and `compat_blueprint`.  
* `adapter/http_reader.py:create_app()` registers `bp` and `compat_blueprint`.

### Existing surface classification

`docs/ENDPOINTS_CATALOG.json` already records:

* Path: `/api/compat/v1`.  
* Method: `POST`.  
* Classification: `internal_admin`.  
* Internal: `true`.  
* A7 eligible: `false`.  
* Non-empty environment gate.

The remediation mounts this existing surface. It does not mint or widen it.

### Existing test gap

* `tests/http/test_compat_endpoint_contract.py` imports `create_app` from `adapter.http_reader`, not from the factory selected by production and local launchers.  
* `tests/adapter/test_compat_http_parity.py` compares the `adapter.http_reader` and `adapter.wsgi` factories, not `adapter.factory`.  
* `tests/adapter/test_compat_http_dev.py` also exercises `adapter.http_reader:create_app()`.

The existing compatibility tests can therefore pass while the selected factory omits `/api/compat/v1`.

### Existing architecture-proof gap

* `artifacts/architecture/architecture_snapshot.keys_only.json` records one `adapter/factory.py` blueprint registration: `bp`.  
* The same artifact records Reader and compatibility registrations for `adapter/wsgi.py` and `adapter/http_reader.py`.  
* `tools/evidence/generate_architecture_snapshot.py` classifies known registrations but does not require the selected factory to register the required blueprint set.  
* `tests/evidence/test_architecture_snapshot.py` asserts the `adapter/wsgi.py` registration set but does not assert the selected `adapter/factory.py` set.  
* The current architecture analyzer therefore reports `pass` despite the selected-factory route divergence.

## Root Cause Analysis

### What went wrong

The production/local selected factory maintains its own route-registration list and registers only the Reader blueprint. Other factory implementations independently register both Reader and compat. No selected-entrypoint regression binds launcher selection, required route inventory, and the existing compatibility contract.

### How it manifested

* Production and local launchers resolve to `adapter.factory:create_app()`.  
* `/reader` and `/internal/version` are mounted through `bp`.  
* `/api/compat/v1` is absent from that factory.  
* Compatibility tests exercise adjacent factories and do not fail on the selected factory.  
* The architecture snapshot records the divergent registration but does not treat it as a failing invariant.

### Root causes

* Proximate implementation cause: independently maintained factory registration lists diverged.  
* Proximate test cause: route-contract and parity coverage excluded the selected factory.  
* Proximate evidence cause: architecture validation classified registrations but did not enforce selected-factory route-mount parity.  
* Historical cause: Unknown. The available sources do not establish why `adapter/factory.py` was left narrower.

### Documentation ignored

Not established. PF02 contains the applicable architecture rule, but the available evidence does not prove that an implementer knowingly disregarded it.

### Documentation incorrect

Not established. PF02 already requires a canonical production factory and mounting of the existing compat surface.

### Documentation missing

PF10 Addendum 2.23 identifies a mechanics clarification gap: PF14 does not explicitly connect service-factory correctness to required route-mount parity for the factory selected by production and documented local launchers. This is a later-drain candidate only and does not block the DEV remediation.

## Remediation Implementation Plan

### Step Overview

| Step ID | Step name | Step type | Step intent | Owner/role | Depends on | Cross-lane dependency | Outputs |
| :---: | :---- | :---: | :---: | :---- | :---: | :---: | :---- |
| S1 | Canonical adapter factory route-mount parity | DEV | CHANGE | Implementation Agent | None | None | Code, tests, refreshed architecture evidence, coherent index/mirror bindings |

### Step S1 Details

Step ID: S1

Step name: Canonical adapter factory route-mount parity

Step type: DEV

Step intent: CHANGE

Owner/role: Implementation Agent

Preconditions:

* This r1 plan has received ASK OK approval.  
* Work begins from a clean implementation checkout based on the then-current approved branch.  
* Before editing, revalidate that the three selection anchors still choose `adapter.factory:create_app()` and that `adapter/factory.py` still omits `compat_blueprint`.  
* If either embedded fact has changed, stop without mutation and return the source drift to the PO. Do not improvise a different remediation.  
* Use closed rails and an explicit dev test context: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* Do not rely on an ambient or default `APP_ENV`. The explicit `APP_ENV=dev` value applies only to repo-local remediation verification and does not change deployment configuration.

Inputs:

* Current repository checkout.  
* The self-contained Observed Evidence Snapshot in this plan.  
* Existing Reader blueprint from `adapter/http_reader.py`.  
* Existing compatibility blueprint from `engine/http/compat_handler.py`.  
* Existing Endpoint Catalog entry for `/api/compat/v1`.  
* Existing architecture snapshot generator, schema, tests, and evidence updater.

Canon constraints:

* Preserve one adapter HTTP home and the single Presenter byte authority.  
* Mount the existing compatibility blueprint; do not duplicate its handlers.  
* Preserve `/api/compat/v1` as an internal/admin surface.  
* Do not change public Reader bytes or introduce a public route.  
* Preserve internal-route ETag stripping in the selected factory.  
* Do not add a schema, evidence root, acceptance token, environment variable, vendor call, DB action, or OPS dependency.  
* Do not make PF or board files part of the PR.

Actions:

1. Update `adapter/factory.py` so the factory selected by `Procfile`, `scripts/start_web.sh`, and `run_flask.py` mounts both the existing Reader blueprint and the existing `compat_blueprint`.  
2. Keep the change at the route-wiring boundary. Reuse `engine/http/compat_handler.py`; do not copy handlers or create a second compatibility implementation.  
3. Preserve the current Reader mount, `/internal/version` behavior, internal-route ETag handling, and existing launcher targets.  
4. Update `tests/http/test_compat_endpoint_contract.py` so its HTTP route-contract client exercises `adapter.factory:create_app()`. Pure compute tests in that file remain unchanged.  
5. Update `tests/adapter/test_compat_http_parity.py` so the selected factory participates in the existing compatibility parity checks. Add a fail-closed required-route assertion covering:  
   * `GET /reader`.  
   * `GET /internal/version`.  
   * `POST /api/compat/v1`.  
6. Bind the assertion to the launch-selected factory. A test that checks only `adapter.http_reader` or `adapter.wsgi` is insufficient.  
7. Update `tools/evidence/generate_architecture_snapshot.py` so validation fails when the selected `adapter/factory.py` registration set lacks either the Reader blueprint or `compat_blueprint`. Use the existing snapshot structure; do not change `schemas/architecture_snapshot.keys_only.v1.json`.  
8. Update `tests/evidence/test_architecture_snapshot.py` to prove the selected factory registration invariant and its fail-closed negative case.  
9. Regenerate the existing architecture snapshot with the existing producer.  
10. Refresh all changed governed evidence through `tools/evidence/update_evidence_index.py`. Do not hand-write path proofs.  
11. Run the targeted tests, architecture check, canonical updater check, evidence-path/hash/schema checks, and existing nineteen-stage release-sanity gate.  
12. Inspect the final diff and confirm that it contains only the approved code, test, tooling, architecture evidence, sanity-log, and governed index/mirror refresh surfaces.

Outputs required:

Code, test, and tooling changes:

* `adapter/factory.py`.  
* `tests/http/test_compat_endpoint_contract.py`.  
* `tests/adapter/test_compat_http_parity.py`.  
* `tools/evidence/generate_architecture_snapshot.py`.  
* `tests/evidence/test_architecture_snapshot.py`.

Regenerated governed evidence:

* `artifacts/architecture/architecture_snapshot.keys_only.json`.  
* `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
* `audit/gates/sanity_pipeline/sanity_pipeline.log`.  
* `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`.  
* `docs/evidence/INDEX.json`.  
* `docs/evidence/INDEX.json.path_proof.txt`.  
* `docs/evidence/INDEX.sha256`.  
* `docs/evidence/INDEX.sha256.path_proof.txt`.  
* `artifacts/evidence_index.jsonl`.  
* `artifacts/evidence_index.jsonl.path_proof.txt`.  
* `artifacts/evidence_index.jsonl.sha256`.  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`.

Indexing posture:

* The architecture snapshot and sanity log are existing indexed governed artifacts.  
* No new artifact key, evidence family, schema, or root is created.  
* The Human Index remains authoritative.  
* The Machine Mirror remains the single canonical mirror.  
* The canonical updater owns index, mirror, checksum, and path-proof refreshes.

Verification:

Run under the closed and deterministic environment pins stated in Preconditions.

Environment declaration:

* `export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`

Targeted behavior and parity:

* `python -m pytest -q tests/http/test_compat_endpoint_contract.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py`

Architecture evidence:

* `python tools/evidence/generate_architecture_snapshot.py`  
* `python -m pytest -q tests/evidence/test_architecture_snapshot.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/generate_architecture_snapshot.py --check`  
* `python tools/evidence/update_evidence_index.py --check`

Final governed validation:

* `python tools/evidence/run_sanity_pipeline_gate.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python ci/checks/check_mirror_schema.sh`  
* `bash ci/checks/check_evidence_index_hash.sh`  
* `python tools/evidence/orientation_demo.py --check`  
* `ci/checks/check_final_lf.sh`

Verification success criteria:

* `adapter.factory:create_app()` exposes `GET /reader`, `GET /internal/version`, and `POST /api/compat/v1`.  
* Existing compatibility contract tests pass through the production/local selected factory.  
* Selected-factory responses remain parity-compatible with the existing dev and WSGI factory proof surfaces for the tested compatibility cases.  
* The architecture snapshot records both selected-factory registrations and fails closed if either is removed.  
* The architecture snapshot remains canonical, keys-only, secret-free, schema-valid, and indexed.  
* The Human Index, hash sentinel, Machine Mirror, mirror checksum, and all listed sibling path proofs are coherent.  
* The existing nineteen-stage sanity pipeline ends with `first_failed_stage:NONE` and `summary:PASS`.  
* No vendor call, DB action, OPS action, deployment, QA execution, PF edit, board edit, new route, new public contract, or schema change occurs.

Failure handling:

* Any targeted contract, route-inventory, parity, architecture, evidence, or sanity failure blocks the remediation PR.  
* Do not weaken or remove an existing test, route requirement, safety rail, evidence check, or failure condition to obtain a passing result.  
* Do not reclassify a missing required route as documentation-only.  
* If the minimal route-mount change requires a new route, new handler, schema change, launcher change, PF decision, external operation, or broader factory refactor, stop and return the scope expansion for PO approval.  
* A passing selected-factory test without coherent regenerated architecture and index/mirror evidence is incomplete.  
* A coherent evidence refresh without selected-factory behavior proof is incomplete.

In-flight determinations:

* No ADR is required for mounting the existing compat blueprint in the selected factory; PF02 and PF10 already establish the required direction.  
* No OPS dependency exists.  
* No public-surface decision exists.  
* The implementation may choose the smallest internal wiring form that preserves the constraints above, but it may not change the approved outputs or broaden the contract.

## Sequencing and Handoff

1. ASK OK approval of this plan.  
2. Execute and merge remediation `PR-01`.  
3. Reassess QA readiness against the new merged head using the existing readiness decision process.

Step 3 is not QA execution and is not an additional DEV or OPS step in this plan. This plan does not declare `QA READY`; it removes the single currently identified implementation blocker so a later readiness decision can be made from the merged result.

## Non-Mandatory Doc Delta Candidates

These are documentation/status drainage only. They are not PR outputs, required follow-up tasks, acceptance conditions, or QA-entry blockers.

* PF09.6 candidate: add a properly assigned Distillation task/subtask for canonical adapter factory route-mount parity. Do not invent the ID or status in this plan.  
* PF14 candidate: clarify that service-factory correctness includes the required route inventory for the factory selected by production and documented local launchers.  
* Pre-existing HDE-EPIC038 PF09 status drainage remains separate and is not reopened by this remediation.

## PF Docs Consulted

* PF02 \- HDE Architecture, v2.3.8.  
* PF09.6 \- HDE Build Checklist Distillation, v1.1.2.  
* PF10 \- HDE Build Notes, v12.4.3, Addendum 2.23.  
* PF10 \- HDE Build Notes, Addendum 2.25.  
* PF23 \- Canon Reality Audits, v1.1.8, planning-time provenance only.  
* PF27 \- Canon Plan Templates, v1.9.5 \- consulted; no Epic Remediation Plan template exists.  
* HDE-EPIC038 Epic Plan r1.  
* HDE-EPIC038 Implementation Plan r6.

## ADRs Requiring Approval

None.

The remediation direction is already controlled by existing PF02 architecture and PF10 exact-topic live truth. This plan creates no canon-resolution decision, external task, new surface, new token, or OPS authorization.

## Approval Boundary

Approval authorizes only the single DEV remediation step and its embedded verification/evidence refresh.

Approval does not authorize QA execution, OPS work, deployment, production mutation, PF edits, board edits, acceptance, PF09 status movement, or Epic closure.

ASK OK?  
