---
artifact_type: IMPLEMENTATION_PLAN
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN
plan_type: CRD_IMPLEMENTATION_PLAN
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: PLAN_PENDING
approval_sentinel: "ASK OK?"
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
author: whole-change Implementation Agent (IA) for HDE-CRD-0002 (session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; same author and session as the Audit)
reviewer: Isis, continuing Lead Developer, through IA-30 — Review Whole-Change Implementation Plan — 100926.1 (reviewer session may be assigned at that boundary; Specification author session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
prompt: IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0)
entry_mode: FIRST_ENTRY
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-12T20:31:21Z
repository_head_read: origin/main 982071b8203bfed961091811e24f57e99f92e593
specification_ref: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
thoth_decision_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md (INITIAL_APPROVE, 2026-10-12T19:39:51Z)
audit_ref: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (IMPLEMENTATION_AUDIT v1.0, AUDIT_COMPLETE; same invocation)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (v13.5.2; blob ec71eeecec8b0fcff1645d317211258bc708712c; addendum 2.1 only)
approved_base_plus_overlays: approved base = Specification v1.1 (approved); applicable PF10 overlays = NONE
canon_conflict_register: CR-1, CR-2, CR-3 carried (APPROVED_AS_CHANGED); treatment in §15
work_units: WU-PR-01, WU-PR-02, WU-PR-03, WU-PR-04, WU-PR-05, WU-PR-06, WU-PR-07, WU-PR-08, WU-DOC-01, WU-OPS-01
next_prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), REVIEW_MODE INITIAL_PLAN_REVIEW
---

# HDE-CRD-0002 — Implementation Plan v1.0 (initial, pending)

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Result and authority

**PLAN_PENDING.** This is the one change-wide `CRD_IMPLEMENTATION_PLAN` for HDE-CRD-0002, derived from the approved Specification v1.1 and the complete Implementation Audit v1.0 (HDE Governance §9.1.1). It identifies the planned PR, Ops and documentation work units, their purpose, bounded scope, outcomes, order, dependencies, handoffs, validation, migration, rollback and evidence obligations. It creates no PR, commit, merge, deployment or Ops effect, performs no work, approves nothing and is unapproved until Isis approves this exact version (IA-30). Detailed per-PR Implementation Plans are prepared later in each dedicated PR session (PR-10 → PR-20 → Product Owner `PR Implementation Proceed` → PR-30 → PR-35 → PR-40); this Plan does not pre-empt them with per-file edits or commands (HDE Governance §9.7.7 "Artifact-level detail"; Change Process Guide, "Implementation Plans must be concrete enough for the executing agent and OPS separation").

Stage: Stage A plan approval (HDE Governance §9.7.1). This Plan states what must be proven, the governing criteria and the evidence families; it embeds no QA runbook and requires no QA evidence production as implementation work (HDE Governance §9.7.7; Plan Templates, IP evidence limits).

## 2. Lineage and sources

| Item | Exact identity |
| :---- | :---- |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 approved; reviewed source `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md` (blob `8a3ef0a8…`) |
| Thoth decision | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`, INITIAL_APPROVE |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`, AUDIT_COMPLETE; its §5 facts, §6 dispositions, §7.1 engineering choices EC-1 to EC-12, §7.3 re-cut analysis, §8 AQ-1 and Appendices A and B are inputs to every unit below |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md`, read in full; addendum 2.1 governs §17 only; no overlay on the subject matter |
| Canon | as listed under "Canon relied on" |
| Repository state | `origin/main` `982071b8203bfed961091811e24f57e99f92e593`; release `1.3.0`, 45 members |
| Conflict register | CR-1 to CR-3 carried; §15 |

## 3. Delivery architecture

The change is delivered as eight PR work units in the four Specification phase blocks, one final repository-documentation unit and one bounded Ops unit, ordered so that CI sees every later change (S03–S05 first), evidence admission for the CRD exists before QA (S22 early), member-changing work lands before the version-bumping release cut (S01 unit last among code units), and the close-pack capability (S21) is in place before HDE-CRD-0002's own Close Gate.

- **Release-identity spine.** Admission compares every roster member's bytes with `catalog/manifest.json` (Audit §5.1), so a unit that changes a member byte must refresh the manifest in the same unit (a same-version cut through the cutter with `--roster-from-admission`, as HDE-EPIC040-PR06a's PR-35 did) and converge the generated evidence that binds the release identity (Audit §7.3 order). The single new release, `1.4.0` with new admission pins, is cut once, in WU-PR-08, after the last member-changing unit (Specification constraint "Release members"; Exclusions bullet 2). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member), WU-PR-08.
- **Coverage spine.** WU-PR-01 brings every test file into CI or retires it, so WU-PR-03 and WU-PR-04, which change surfaces tested today only by uncovered files (`tests/adapter/test_gate_auth.py`, `tests/bodygraph/test_resolver_vendor.py`), are verified by CI.
- **Evidence spine.** The canonical updater remains the sole Index/Mirror writer; WU-PR-02 extends its CRD admission to `audit/qa/hde-crd-0002/` and its provenance labels; WU-PR-07 adds the close-run evidence family under an ADR; every regenerated governed artifact is produced by its owner tool, never by hand (Specification constraint "Governed artifacts"; AGENTS.md).
- **Public-surface posture.** No Reader contract or payload change, no new public route, no new HTTP home; S02 changes only error shaping of unknown paths; S10 narrows a dev route; S15 documents existing routes (Exclusions bullet 1; Audit EC-8).
- **Rails posture.** Every implementation unit runs under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, vendor and database keys unset); no implementation unit makes a live vendor, production or database call; the bounded open-rails steps belong to the QA Plan and to WU-OPS-01 (Exclusions bullet 5).

## 4. Invariants (hold across every unit)

1. Public Reader v1 and v2 bodies stay bands-only and numeric-free; no public route, flag, payload or transport change (Exclusions; AGENTS.md "HDE-EPIC040 current posture").
2. Closed SAFE and network rails refuse before any vendor decision; the production override never opens a rail and never lets Reader or Aux traffic reach the vendor (HDE-CLI-API-Vendor-Ref §7.1.11).
3. `catalog/manifest.json` is the only release-identity input; it changes only through `scripts/cut_release_manifest.py`; admission constants change only in WU-PR-08 (AGENTS.md "Release identity"; `docs/adr/hde/release_attestation_scaling_adr.md`).
4. Governed evidence (Index, Mirror, path proofs, catalog and mirror, proofs, gate logs, close packs) is written only by its owning tool; frozen capture-time families stay frozen with nonclaims (Audit EC-6).
5. The Close Gate lifecycle stays feedback-free: no source → CI → source back-edge; the close candidate derives from tracked inputs only (Change Process Guide §3.5.1).
6. CRD identity: `HDE-CRD-0002`, QA root `audit/qa/hde-crd-0002/`, Ops evidence root `audit/ops/hde-crd-0002/<task_id>/`, close-pack prefix `CRD-0002` (HDE Schemas & Artifacts §1.2 and §8.17; CR-3 interim treatment).
7. No agent edits `docs/pfcanon/`; canon drift is recorded as doc-delta candidates (HDE Governance §9.7; AGENTS.md).
8. Every PR unit is self-contained, lands by ordinary pull request, is merged by the Product Owner only, and reports its actual checks truthfully (Change Process Guide §3.5.1; AGENTS.md PR-description rules).
9. Alchemical phase separation: each unit belongs to exactly one phase block; no unit mixes DEV and OPS work (Plan Templates §2A; §3 "Not a PR").

## 5. Important interfaces and data shapes

| ID | Interface | Shape (binding for the units; details in the per-PR plans) |
| :---- | :---- | :---- |
| IF-1 | `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>` | One value-bearing flag, accepted only with `--source vendor`; value `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`; empty, malformed, duplicated or inapplicable use is a CLI usage error (exit 64). Environment: `APP_ENV` canonical, `ENGINE_ENV` alias when `APP_ENV` blank; production-like `{prod, production, live}`, non-production `{dev, test, local, stage, staging}`; conflict or unknown → `PROVIDER_CONFIG_INVALID` before I/O. Matrix and evaluation order exactly as HDE-CLI-API-Vendor-Ref §7.1.11c–d; policy refusals `status="error"` envelope with one typed code, exit 1, `outbound_attempted: false`. |
| IF-2 | Vendor production-override audit record | Append-only, locally durable JSONL, one event per invocation reaching override evaluation, fields exactly `schema_version`, `event` (`vendor_prod_override`), `occurred_at`, `correlation_id`, `actor_principal`, `authorization_ref`, `command` (`bg:resolve`), `source` (`vendor`), `environment`, `safe_mode_open`, `network_open`, `route_family`, `resource_path`, `outcome` (`refused`/`allowed`/`failed`/`completed`), `error_code`, `outbound_attempted`; no subject, URL, header, token or raw provider data; CR/LF-sanitized; sink path from one operator environment key (name fixed at PR-20; Glow Infrastructure doc-delta candidate) with a default under the operator's state directory; persistence failure → `PROVIDER_AUDIT_UNAVAILABLE`. |
| IF-3 | Close candidate source v2 (`schemas/close_candidate_source.v2.json`) | `schema_version: close_candidate_source.v2`; `change_id` `^HDE-(EPIC[0-9]{3}|CRD-[0-9]{4,})$` mapped to the filename prefix (`EPIC-NNN` / `CRD-NNNN`) and the lower-case directory form; `plan_path`, `evidence_inputs[]` (tracked path + binding), `acceptance[]` (criterion id, tracked evidence paths, result, limitation), `deliverables[]`, `deferrals[]` (id, drain target or ADR status), `later_drain_statements[]` (fixed vocabulary of HDE Schemas & Artifacts §1.2), `closure_decision` (`SATISFIED`/`NOT SATISFIED` plus posture), `follow_ups[]`, `pointers[]`, `qa_rca` (embedded summary or exact path), `key_outputs` (close report, manifest); every causal field keeps the feedback-dependency refusal; candidate identity only by tracked-path digests. Writer outputs `audit/<PREFIX>_close_report.md` (with the verbatim heading `QA Rails — Open/Close (Final PR)` and an "Acceptance and evidence pointers" list) and `audit/<PREFIX>_MANIFEST.json` (with a `key_outputs` map); check mode writes nothing. |
| IF-4 | Close-run evidence home | `audit/qa/<change-id>/close/<check_id>/primary.log` (+ `.path_proof.txt`), a post-verdict family admitted by the S21 ADR and published by the canonical updater; it never adds a check to `qa_step_logs_manifest.json`. |
| IF-5 | Updater CRD admission | An explicit admitted-CRD table in `tools/evidence/update_evidence_index.py`: `HDE-CRD-0001 → audit/qa/hde-crd-0001, audit.qa.hde_crd_0001`; `HDE-CRD-0002 → audit/qa/hde-crd-0002, audit.qa.hde_crd_0002`; no directory discovery; publication refuses any other ID by name. |
| IF-6 | Endpoint catalog rows | Per-method records in the existing field set (`a7_eligible`, `blueprint_module`, `classification`, `description`, `env_gate`, `internal`, `method`, `path`, `rails_profile`, optional `route_id`), extended by the HDE-CLI-API-Vendor-Ref §5.6 projection for `/aux/narrative` (`classification: public_aux`, `internal: false`, `env_gate: not_applicable_public`, `aliases: ["/api/aux/narrative"]`); internal rows for `/ops/db/unavailable`, `/ops/rails/refusal`, `/ops/probe/env`, `/ops/writer/diagnostic` (`adapter.http_reader`) and `/internal/healthz`, `/internal/readyz` (`adapter.wsgi`); `/reader` rows' `env_gate` becomes `APP_ENV in {dev,test,local}`; `success_endpoints` stays `[GET /reader]`. |
| IF-7 | Machine Mirror release labels | Rows for captures the current release regenerates carry release-identifying fields (version and `release_id`, or an equivalent `release_binding`); frozen families unchanged (Audit EC-5). |
| IF-8 | Wheel layout | The 45 roster paths present in the built wheel at their roster-relative locations (`adapter/schemas/`, `catalog/narratives/`, `errors/token_map/`, `migrations/`, `schemas/`, `tools/bodygraph/` added); loader unchanged (Audit EC-11). |
| IF-9 | Pre-push check | `python tools/ci/prepush_check.py` with sub-reports: `lanes` (classifier delegation for given paths and base/head), `membership` (roster membership of given paths), `build-notes` (unique PF10 path and SHA-256), `sweep` (uncovered set in a throwaway export), `replay` (every `ci.yml` lane step in a throwaway worktree); writes only under a temporary directory; asserts a clean tree before and after; exit 0 only when every requested report succeeds. |
| IF-10 | Dev route gate | `GET /reader` served only for normalized `APP_ENV` in `{dev, test, local}`; otherwise `ERR_READER_FORBIDDEN` 403 (the `_dev_admin_gate` semantics); `scripts/dev_start_reader.sh` defaults `APP_ENV=dev`. |
| IF-11 | Not-found envelope on the production app | App-level 404 and 405 handlers on `adapter.factory` (and the `adapter/http_reader.py` factory) emitting `error_envelope("ERR_NOT_FOUND")` through `emit_public`, `Cache-Control: no-store`, no ETag, `application/json; charset=utf-8`, as `adapter/wsgi.py` does; existing compat shaping and the production Reader's governed 405 unchanged. |

## 6. Requirement traceability

| Requirement | Unit | Phase block | Live QA class (Specification table; Audit §7.4) |
| :---- | :---- | :---- | :---- |
| S01 | WU-PR-08 | Coagulation | production-affecting outside functional scope; exemption basis discoverable by WU-OPS-01 |
| S02 | WU-PR-03 | Conjunction | functional-feature |
| S03 | WU-PR-01 | Distillation | not production-affecting |
| S04 | WU-PR-01 | Distillation | not production-affecting |
| S05 | WU-PR-01 | Distillation | not production-affecting |
| S06 | WU-PR-02 | Distillation | not production-affecting |
| S07 | WU-PR-03 | Conjunction | functional-feature |
| S08 | WU-PR-04 | Fermentation | functional-feature |
| S09 | WU-PR-03 | Conjunction | not production-affecting |
| S10 | WU-PR-03 | Conjunction | functional-feature |
| S11 | WU-PR-02 | Distillation | not production-affecting |
| S12 | WU-PR-02 | Distillation | not production-affecting |
| S13 | WU-PR-02 | Distillation | not production-affecting |
| S14 | WU-PR-04 | Fermentation | functional-feature (mandatory live vendor call) |
| S15 | WU-PR-03 | Conjunction | catalog entries only (no route removed) |
| S16 | WU-PR-08 | Coagulation | not production-affecting |
| S17 | WU-PR-08 | Coagulation | not production-affecting |
| S18 | WU-PR-03 | Conjunction | not production-affecting |
| S19 | WU-PR-05 | Distillation | inherits the class of each fixed surface |
| S20 | WU-PR-06 | Distillation | not production-affecting |
| S21 | WU-PR-07 | Distillation | not production-affecting |
| S22 | WU-PR-02 | Distillation | not production-affecting |
| CD-1 | WU-PR-07 (resolved by S21) | — | — |
| CD-2 / CR-3 | interim treatment applied in every unit | — | — |
| CD-3 | WU-PR-02 (resolved by S22) | — | — |
| RD-1 | not delivered (GCFPE-MGMT-10 and the Product Owner) | — | — |
| Release re-cut | same-version refresh in each member-changing unit; version bump `1.4.0` in WU-PR-08 | — | — |
| Final documentation | WU-DOC-01 | — | — |
| QA placement | WU-OPS-01 | — | — |

## 7. Ordered work units

Order of landing on `main`: WU-PR-01 → WU-PR-02 → WU-PR-03 → WU-PR-04 → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10 readiness (§9). WU-PR-02, WU-PR-06 and WU-PR-07 have no code dependency on WU-PR-03 to WU-PR-05 and may be prepared in parallel, but they merge in the stated order so that each unit's CI runs on a known base and the two updater-changing units (WU-PR-02, WU-PR-07) do not race. Every PR unit is implemented in its own dedicated top-level PR session under the Product Owner's `PR Implementation Proceed` for that unit's detailed plan; this IA issues the PR Instructions (PR-10) from this approved Plan only.

Common to every PR unit unless stated: executor = the dedicated PR session; author of the PR Instruction = this IA; reviewer chain = Codex code review and security review on the PR, PR-35 for review resolution, PR-40 lineage review by this IA; environment = closed rails, Python 3.12, CI's install, detached worktree for test isolation, exact-head hosted CI with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; evidence = the PR result record under `docs/ephemeral/` naming every check actually run with counts, plus the regenerated governed artifacts in the PR; migration = none (no data migration in this change); rollback = revert of the squash commit by the Product Owner, with a same-version manifest refresh when the reverted unit changed a member; recovery = interruption resumes in the same PR session from its checkpoint, a bounded scope change goes through RS-10, abort only by the Product Owner's manual PR-50 instruction; nonclaims = no QA verdict, acceptance, PF09 movement, deployment, canon change or closure.

### WU-PR-01 — CI coverage of every test file (PR; Distillation)

- **Purpose.** Make every test file in the repository run in a CI lane or retire it with a recorded reason, and close the two classifier and workflow gaps that travel with it.
- **Bounded scope.** S03, S04, S05; Audit §5.2, §5.3, §5.7, Appendix A; EC-1, EC-3.
- **Inputs.** The 135-file inventory (Appendix A plus the five `pytest.ini`-root files); the sweep classification (Audit §5.7); the classifier's registration mechanisms (Audit §5.2).
- **Deliverables.** `.github/workflows/ci.yml` (lane lists; `paths-ignore` aligned to the classifier's eight documentation prefixes with negations for governed primaries); `ci/checks/classify_ci_changes.py` (owner and lane registrations for retained files; `tools/qa/` fail-closed treatment for `.py`, `.sh`, `.sql`; the inactive set resolved); `pytest.ini` where roots change; the retained test files, fixed where they fail or write tracked artifacts; the retired test files removed; `tests/retired_tests.md` (new ledger: path, reason, date, replacing coverage if any); `tests/evidence/test_rails_ci_workflow_integration.py` (pinned expectations, including the governed-primary negation test that reads `docs/evidence/INDEX.json`).
- **Dependencies and order.** First. No upstream dependency. WU-PR-03 and WU-PR-04 depend on it (their surfaces' tests are in the uncovered set).
- **Acceptance and verification (done means).** (1) The Audit §3(b) computation at the PR head returns zero files outside lane-or-target coverage, and the ledger explains every retirement. (2) Every retained file passes under closed rails in its lane shape in a detached worktree with `git diff --exit-code` and an empty status afterwards. (3) An unregistered `.sh` or `.sql` under `tools/qa/` fails classification in a unit test. (4) The classifier dry run on a documentation-only path set selects no lane, and the workflow's path filter ignores exactly the classifier's prefixes minus governed primaries. (5) All seven lanes green on the exact head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Evidence obligations.** PR result record with the before/after inventory (130/135 → 0), the per-file disposition table (lane or target, or retirement reason), the sweep transcript summary and the lane counts; no QA artifact.
- **Risks and recovery.** R-1 (size): the detailed plan may bound the unit by the Audit's classes and propose an RS-10 rescope if a real defect enlarges it; never skip, disable or quarantine a test to get green.
- **Nonclaims.** CI green is not QA; no PF09 mapping.

### WU-PR-02 — Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation)

- **Purpose.** Repair the release-evidence tooling defects HDE-EPIC040 carried and admit HDE-CRD-0002's QA root to the canonical evidence graph before QA.
- **Bounded scope.** S06, S11, S12, S13, S22; CD-3; Audit §5.6; EC-5.
- **Inputs.** O-10 reproduction method (Audit §6 S06); O-OPS01-01 (S13); the engine-core writer and test (S11); the updater's family registrations and CRD admission code (S12, S22); IF-5, IF-7.
- **Deliverables.** `tools/evidence/build_release_attestation.py` (wheel stage); `tools/evidence/regenerate_identity_closure.py` (root-bound probe); `tests/evidence/test_release_attestation.py`; `tests/evidence/test_engine_core_evidence.py` (release-identity assertion and negative case); `tools/evidence/update_evidence_index.py` (admitted-CRD table per IF-5; release-identifying labels per IF-7); `tests/evidence/test_evidence_index_missing_state.py` (both CRD IDs; foreign-scope and forgery cases); regenerated by the updater only: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, their `.path_proof.txt` companions and `audit/gates/topology/orientation_demo.txt`; Mirror schema companions only if IF-7 needs a schema field (the detailed plan decides and records it as a doc-delta candidate for HDE Schemas & Artifacts).
- **Dependencies and order.** Second; no code dependency on WU-PR-01; lands before WU-PR-07 (which extends the same updater) and before any member-changing unit's convergence relabels rows.
- **Acceptance and verification.** (1) A recorded reproduction of O-10 on a Debian interpreter fails before the change and the attestation builds and verifies after it; hosted CI's release lane still builds and verifies. (2) A test proves the closure probe follows the isolated copy with no ambient `engine` importable. (3) `test_engine_core_evidence.py` fails when the admitted `release_id` is monkeypatched to differ from the payloads. (4) Every Mirror row for a regenerated current-release capture carries the IF-7 fields; frozen families unchanged; `ci/checks/check_mirror_schema.sh`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh` exit 0. (5) Publication through `publish_crd_check_family` succeeds for a fixture `HDE-CRD-0002` root and for `HDE-CRD-0001`, and refuses `HDE-CRD-0003` by name; the absent real root publishes nothing.
- **Evidence obligations.** PR result record; the regenerated governed companions in the PR; no new evidence family.
- **Risks and recovery.** Mirror consumers rejecting added fields (run every read-only validator); S06 reproduction environment `discoverable by PR`.
- **Nonclaims.** No QA evidence is produced for HDE-CRD-0002; admission readiness only.

### WU-PR-03 — Public, dev and CLI surfaces (PR; Conjunction)

- **Purpose.** Correct the production app's not-found shaping, the dev route's environment gate, the showcompat help summary, the dev harness references, the endpoint catalog and the two stale operator documents' routing statements; carry the manifest refresh these member changes force.
- **Bounded scope.** S02, S07, S09, S10, S15, S18; EC-2, EC-4, EC-6, EC-8; IF-6, IF-10, IF-11; same-version manifest refresh and convergence (Audit §5.1, §7.3).
- **Inputs.** Audit §5.5, §5.6 (CLI conformance family), §6 S02/S07/S09/S10/S15/S18; HDE-CLI-API-Vendor-Ref §5.6 projection for the Aux record.
- **Deliverables.** `adapter/factory.py` and `adapter/http_reader.py` (IF-11 handlers; IF-10 gate; member); `engine/cli/main.py` (showcompat help; member); `tools/evidence/generate_a7_transport_proofs.py` (IF-6 rows and validator); regenerated by that owner then the updater: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`, `artifacts/audit/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `artifacts/reader/endpoints_snapshot.json`, the `artifacts/proofs/*` A7 family and their path proofs, Index and Mirror companions; `scripts/dev_start_reader.sh` (default `APP_ENV=dev`); `VERIFY.sh` (canonical runner); `dev/reader_harness/app.py` removed; `docs/acceptance/reader_a7_crib.md`; `docs/server/reader_v1.md`; `docs/ADAPTER_009.md` (the `COMPAT_GET_BODY_400_OK` line only; S17's lines belong to WU-PR-08); `ARCHITECTURE.md`; `docs/CLI_commands.md` (known-gap sentence); docstrings in `engine/emit_public.py` and `tests/runtime/test_emit_public_legacy_helper.py`; tests under `tests/http/`, `tests/cli/`, `tests/transport/` (including the route-enumeration test for the catalog); `catalog/manifest.json` refreshed at `1.3.0` / `2026-08-24T18:04:49Z` by the cutter and every evidence family the refresh regenerates, by its owner (Audit §7.3 order).
- **Dependencies and order.** Third; after WU-PR-01 (registered owners for `tests/adapter/test_gate_auth.py` and the http_reader owner guard) and WU-PR-02 (label model before rows are regenerated).
- **Acceptance and verification.** (1) Unknown paths on the production factory and the `adapter/http_reader.py` factory return the IF-11 envelope for GET, HEAD, POST and OPTIONS; the compat and `api_bp` behaviors are unchanged. (2) `GET /reader` is served for `dev`, `test`, `local` and refused (403, `ERR_READER_FORBIDDEN`) for unset, `prod`, `production`, `live` and arbitrary values; `scripts/dev_start_reader.sh` without `APP_ENV` starts a serving runner. (3) `hdctl --help` names the `magic10_compat_result.v1` stdout contract; `ci/checks/check_cli_help.sh` exits 0; `generate_cli_conformance_artifacts.py --check` exits 0 (frozen family untouched, nonclaim recorded). (4) `dev/reader_harness/app.py` no longer exists; `VERIFY.sh` runs against the canonical runner; no active file references the harness. (5) Every `(method, path)` rule of the three factories has a catalog row; the catalog validator accepts the IF-6 model; `docs/ENDPOINTS_CATALOG.json` equals its mirror byte for byte; `success_endpoints` unchanged. (6) The documents state `invalid_json`, the emitter's real return type, and the production mounts. (7) Admission at the PR head reports `1.3.0`, 45 members and the refreshed `release_id`; every convergence step byte-stable on a second run; `release_id_recompute.py --check-manifest-only` exits 0; all lanes green.
- **Evidence obligations.** PR result record naming the refreshed `release_id` and every regenerated family; the catalog diff; nonclaim for the frozen CLI help capture.
- **Risks and recovery.** Catalog validator and PF12 registration (R-7); the http_reader owner-guard tuple must include new consumer tests (Audit §7.5).
- **Nonclaims.** No public contract change; no Live QA performed; catalog membership proves no reachability (HDE-CLI-API-Vendor-Ref §5.6).

### WU-PR-04 — Provider gate and Aux preview (PR; Fermentation)

- **Purpose.** Implement the production vendor override exactly as HDE-CLI-API-Vendor-Ref §7.1.11a–f state it, and make `aux-preview --band` apply for pair-file input; carry the manifest refresh these member changes force.
- **Bounded scope.** S08, S14; EC-7; IF-1, IF-2; same-version manifest refresh and convergence.
- **Inputs.** Audit §6 S08 and S14 (current parser, handler, resolver rail order, dry-run path, existing `PROVIDER_CONFIG_INVALID` code); HDE-CLI-API-Vendor-Ref §7.1.11 in full.
- **Deliverables.** `engine/cli/main.py` (IF-1 parser and usage carrier; aux band override; member); `engine/bodygraph/resolver.py` (classification, matrix, evaluation order, envelope codes; member); `engine/bodygraph/vendor_audit.py` (new; IF-2 record, sink, actor principal); `tests/cli/test_bg_resolve.py`; `tests/cli/test_aux_preview.py`; `tests/bodygraph/test_resolver_vendor.py` (registered by WU-PR-01); `tests/bodygraph/test_vendor_prod_override.py` (new; the matrix and order tables with zero outbound attempts); `docs/CLI_commands.md` (flag and band wording); classifier registration for the new module's owner test; `catalog/manifest.json` refreshed at `1.3.0` and every family the refresh regenerates, by its owner.
- **Dependencies and order.** Fourth; after WU-PR-01 and WU-PR-03.
- **Acceptance and verification.** (1) Table-driven tests cover the eight matrix rows and the seven evaluation steps with a monkeypatched vendor client proving no client construction, DNS, socket or HTTP on any refusal; `outbound_attempted` false and exit 1 for policy refusals, exit 64 for usage errors; `ENGINE_ENV` alias and conflict; a vendor `--dry-run` in a production-like environment without the flag refuses `PROVIDER_PROD_OVERRIDE_REQUIRED`. (2) The audit record has exactly the IF-2 fields, is CR/LF-sanitized, contains no subject or secret data, and an unwritable sink yields `PROVIDER_AUDIT_UNAVAILABLE` before I/O. (3) Closed rails refuse first in every case; no Reader or Aux route gains a vendor path. (4) `aux-preview --pair-file … --band <band>` emits the flagged band; without the flag, the file's band. (5) Admission and convergence as WU-PR-03 (7); all lanes green.
- **Evidence obligations.** PR result record; no live call; no audit sink in the repository.
- **Risks and recovery.** Largest behavioral unit; argparse duplicate detection; the new environment key name recorded for the Glow Infrastructure doc-delta candidate; R-3 is a QA-time risk.
- **Nonclaims.** The flag is not exercised live in this unit; the live vendor call belongs to the QA Plan under the override-initiator constraint.

### WU-PR-05 — Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation)

- **Purpose.** Record one code security review of what #467, #492, #501 and #508 merged, read on `main`, and fix or route each confirmed finding.
- **Bounded scope.** S19; Audit Appendix B (48 paths) and §6 S19 (threat checklist); fixes inherit their surface's Live QA class.
- **Inputs.** The 48 files at the reviewed head; PR06b's later changes to four of them (Audit §6 S19); the existing tests as proof of behavior.
- **Deliverables.** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` (scope and head reviewed; checklist; findings table: id, file and line, description, severity, confirmed or not, disposition fixed-here or routed with owner and reason); fixes with regression tests at the paths the findings name (fixed at PR-20 time); `catalog/manifest.json` refreshed at `1.3.0` with convergence only if a fix changes a member.
- **Dependencies and order.** Fifth; after WU-PR-03 and WU-PR-04 so that fixes are judged against the surfaces' final shape and precede the version bump.
- **Acceptance and verification.** (1) The record covers all 48 paths with a per-file review line, even when no finding. (2) Every confirmed finding has a merged fix with a regression test, or a routing line with owner and reason. (3) No new review tooling or dependency is added (Exclusions bullet 6). (4) Lanes green; if a member changed, admission and convergence as WU-PR-03 (7).
- **Evidence obligations.** The review record is the deliverable; the PR result record names it.
- **Risks and recovery.** R-5 (enlargement); a finding that needs architectural change goes to RS-10 or routes to its owner.
- **Nonclaims.** The review is implementation-side assurance, not QA, not acceptance.

### WU-PR-06 — Read-only pre-push and pre-plan check (PR; Distillation)

- **Purpose.** Give every PR session one read-only command for its pre-push picture.
- **Bounded scope.** S20; EC-9; IF-9.
- **Inputs.** Audit §5.2, §5.3 (sweep definition), §6 S20; the classifier CLI; the `ci.yml` lane steps.
- **Deliverables.** `tools/ci/prepush_check.py` (new); `tests/tools/test_prepush_check.py` (new owner test); `ci/checks/classify_ci_changes.py` (lanes and owner for the new path).
- **Dependencies and order.** Sixth; after WU-PR-01 (lane lists and sweep definition final).
- **Acceptance and verification.** (1) Each IF-9 report runs and the repository tree is byte-identical before and after (asserted by the tool and by its test). (2) `lanes` output equals the classifier's for the same inputs; `membership` matches `ADMITTED_RELEASE_ROSTER`; `build-notes` resolves exactly one `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` and prints its SHA-256; `sweep` reproduces the Audit §3(b) set and runs it in a throwaway export; `replay` covers every lane step name in `ci.yml` (pinned by the test). (3) No hook, no writes, no network. (4) Lanes green (full validation, classifier changed).
- **Evidence obligations.** PR result record with one captured run.
- **Risks and recovery.** Drift from `ci.yml` (the pinning test).
- **Nonclaims.** The tool's green is not CI's green and not QA.

### WU-PR-07 — Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation)

- **Purpose.** Make the ordinary Close Gate reachable: a governed, feedback-free writer that produces a canon-conforming close report and manifest for an Epic or a CRD, and an admitted home for close-workflow run evidence that leaves approved QA manifests closed; draft the ADR the canon change needs.
- **Bounded scope.** S21; CD-1; EC-10; IF-3, IF-4; the ADR draft (approval is AQ-1, Product Owner).
- **Inputs.** Audit §5.6 and §6 S21 (B-1, B-2; canon requirements read in full); HDE-EPIC039's feedback-free rationale (weighed in the Audit).
- **Deliverables.** `schemas/close_candidate_source.v2.json` (new; IF-3); `schemas/epic_close_candidate_source.v1.json` retained; `tools/qa/generate_epic_close_pack.py` (v2 source, both identities, required headings and pointers, `key_outputs`, check mode non-writing); `tests/qa/test_generate_epic_close_pack.py`; `tools/evidence/update_evidence_index.py` and its tests (IF-4 family admission); `ci/checks/classify_ci_changes.py` (registrations for new files); `.github/workflows/epic-closeout-validation.yml` and the release-sanity stage that validates close packs, only where they read the schema version (`Unknown pending discovery`, resolved at PR-20); `docs/adr/hde/close_pack_writer_adr.md` (new; status `Proposed`; decision, affected canon homes with exact locators, drainage consequences, alternatives considered, nonclaims).
- **Dependencies and order.** Seventh; after WU-PR-02 (updater model). S21 completes before HDE-CRD-0002's ordinary Close Gate; the ADR's approval gates reliance on the writer's output, not this unit's merge.
- **Acceptance and verification.** (1) A dry run writes a complete close pack for a synthetic `HDE-CRD-0002` candidate and for a synthetic Epic candidate into `tmp_path`, with the verbatim `QA Rails — Open/Close (Final PR)` heading, the pointers list, the binary decision, deferrals, later-drain statements and a manifest `key_outputs` map. (2) The feedback-dependency refusal still rejects run, receipt, attestation and commit identities in causal fields; candidate identity is tracked-path digests only. (3) Check mode writes nothing and validates exact committed bytes. (4) The updater publishes and validates an IF-4 family under a fixture root without touching `qa_step_logs_manifest.json`. (5) The ADR draft names Change Process Guide §3.5.2, HDE Schemas & Artifacts §1.2 "Close-pack artifacts" and Glow QA Guide "Close-pack truthfulness and same-run execution" / "Close report requirements" as affected canon with drain targets. (6) Lanes green (qa, evidence, release and any full-validation trigger).
- **Evidence obligations.** PR result record; the dry-run outputs are test evidence, not governed artifacts (no retroactive close pack for HDE-EPIC040, Exclusions bullet 7).
- **Risks and recovery.** R-4 (ADR timing); canon drift among the three close-pack homes (the ADR names all three).
- **Nonclaims.** No close pack is produced for any real change here; the ADR is a draft until the Product Owner approves it; no canon is changed.

### WU-PR-08 — Packaging, environment template, operator documentation, release 1.4.0 (PR; Coagulation)

- **Purpose.** Ship every release member with the distribution, add the missing environment-template key, correct the readiness and port statements, and cut the single new release with new admission pins after all member-changing work has landed.
- **Bounded scope.** S01, S16, S17; EC-11, EC-12; IF-8; the version-bump re-cut and full convergence (Audit §7.3).
- **Inputs.** Audit §5.1, §5.4, §6 S01/S16/S17; PR06b §5.4 convergence order; `scripts/cut_release_manifest.py --help`; AGENTS.md "Release identity".
- **Deliverables.** `pyproject.toml` (IF-8); `tests/config/test_wheel_install_admission.py` (new: build, isolated install, admission and `hdctl --version` from the venv); `.env.example` (`GEO_API_KEY` entry only); `docs/ADAPTER_009.md` (readiness rules and port statements); `engine/config/registry_loader.py` (`ADMITTED_RELEASE_VERSION = "1.4.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC` = the cut time; roster unchanged; member); `catalog/manifest.json` cut with `--version 1.4.0 --built-at-utc <cut time> --roster-from-admission`; every evidence family the version bump regenerates, by its owner, in the Audit §7.3 order (config family, canonical JSON gate, updater, A7 family, determinism family, open-rails fixture proof with the `FROZEN_OPEN_ABBA_SHA256` refresh in `tools/evidence/generate_open_rails_abba_proof.py`, F07 writer evidence, engine-core artifacts, sanity log, Index/Mirror/path proofs); the pinned-identity tests rewritten to `1.4.0` (`tests/config/*`, `tests/scripts/test_cut_release_manifest.py`, `tests/evidence/test_sanity_pipeline.py`, `tests/evidence/test_canonical_json_gate_check_outputs.py`, `tests/runtime/test_identity.py`, and any other test the stale-binding sweep finds).
- **Dependencies and order.** Eighth and last code unit; after WU-PR-03, WU-PR-04 and WU-PR-05 (members final) and after WU-PR-02 (labels) and WU-PR-07 (updater families). `pyproject.toml` is a full-validation path: every lane runs.
- **Acceptance and verification.** (1) The wheel built from the PR head contains all 45 roster paths; installed `--no-index --no-deps` into a fresh venv with no checkout on `sys.path`, `load_active_mechanics_bundle()` admits with `release_id` equal to the manifest hash and `hdctl --version` runs. (2) `.env.example` has the one new entry and nothing else changed. (3) The readiness section describes `/internal/readyz` as implemented and on which app; the port statements match the runner and Procfile bindings. (4) Admission at the PR head reports `1.4.0`, 45 members and the new `release_id`; `release_id_recompute.py --check-manifest-only` and the cutter `--check` exit 0; every convergence producer is byte-stable on a second run; the stale-binding sweep finds no superseded identity outside `docs/`; the attestation builds and verifies into an external directory with `--require-clean`; all seven lanes green.
- **Evidence obligations.** PR result record naming the new `release_id`, the regenerated families and the convergence transcript summary.
- **Risks and recovery.** R-2 (convergence order; restart rules), R-6 (top-level data directories, documented).
- **Nonclaims.** The cut activates nothing in production; OPS verifies the deployed release separately; no QA verdict.

### WU-DOC-01 — Final repository documentation (DOC; after WU-PR-08)

- **Purpose.** Bring the operative repository documents to the delivered state (DOC-10 instructions, DOC-20 verification).
- **Bounded scope.** `README.md` (install into a dedicated environment; pre-push check usage; close-pack writer capability; test guidance); `CHANGELOG.md`; `AGENTS.md` operative passages (HDE-EPIC039 workflow posture → the extended close-pack capability and schema v2; HDE-EPIC040 current posture → release `1.4.0`; the CI-exempt paths note verified against the workflow; pytest guidance); `docs/EVIDENCE_INDEX.md` (CRD admission, Mirror labels, close-run family); `docs/CLI_commands.md` final pass; `docs/server/reader_v1.md` (not-found limitation line removed). No canon, no generated evidence, no governed artifact by hand.
- **Dependencies and order.** Ninth; after WU-PR-08 merges.
- **Acceptance and verification.** Each statement traces to a merged unit; `tests/unit/test_check_agents_md_citations.py` passes; DOC-20 verifies completion.
- **Nonclaims.** Documentation completion establishes no QA, acceptance or closure.

### WU-OPS-01 — Place the QA candidate and record the deployment facts (Ops; Coagulation; PO-only execution, IA-guided)

- **Task ID.** WU-OPS-01. **Owner:** PO. **Facilitator:** IA. **Executor:** PO, or a PO-delegated automated session agent under the same controls (Plan Templates §3 "Execution authority").
- **Intent.** The Railway HD Engine production service runs the exact accepted candidate (the `main` head after WU-PR-08 and WU-DOC-01 merge) so that the QA Plan's bounded open-rails live steps (S02, S10 refusal in the deployed target; S14's live vendor call from the operator shell against the production rails) exercise that candidate; and the deployment facts the QA Plan and S01's exemption basis need are recorded presence-only.
- **PF07 posture.** PF07-derived: provider Railway, project `ample-illumination`, service `glow-hdengine-v2`, base URL `https://glow-hdengine-v2-production.up.railway.app`, production bindings `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, key names `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL` (Glow Infrastructure §2.4, §3.1, §4.1); the ops identity surface `/internal/version` (§4.1). PF07-gap (discoverable by OPS): the service's deployment trigger (automatic on `main` or manual) and its configured build and start command (Glow Infrastructure §10 records the checked-in declarations and states the live setting is unverified; §4.1 build artifact "TBD"). The task discovers these facts from the Railway service settings and records them as a Glow Infrastructure doc-delta candidate; it does not guess them.
- **External execution classification.** Hosted-service operation (deployment or redeploy of the accepted commit; read of `/internal/version`; presence-only probe of the bindings). No vendor call, no database write.
- **Secret posture.** Presence-only; no values recorded; no raw request or response bodies.
- **Success criteria.** `GET /internal/version` on the base URL reports the candidate's identity (the `1.4.0` `release_id`); the recorded deployment trigger and build command; the presence-only binding probe; all captured under `audit/ops/hde-crd-0002/wu-ops-01/` with path proofs (Plan Templates §3 evidence posture; lower-case directory names).
- **Constraints.** No production configuration change by this task; if the discovered build command differs from the checked-in declarations, record it and stop (the QA Plan's S01 treatment depends on it). Rollback intent: redeploy the previously deployed commit.
- **Dependencies and order.** After WU-DOC-01; before the QA Plan's live steps; OPS-10 creates the detailed Ops Task record from this unit when the QA candidate is fixed; OPS-20 executes; OPS-30 reviews the receipt.
- **Nonclaims.** Delegation does not convert OPS into PR or QA work; the task claims no QA PASS, Live QA completion, acceptance, deployment success beyond the evidenced target or closeout.

## 8. Final repository documentation work

WU-DOC-01 (§7) is the only documentation unit; the per-requirement document corrections (S17, S18, the S07 sentence, the dev-runner and harness references) ride in the units that change the behavior they describe. No PF document update is a deliverable of any unit (HDE Governance §9.7 "Plans MUST NOT mandate PF document updates"); doc-delta candidates are listed in Audit §7.2 DD-C1 as non-mandatory, Product Owner-owned notes.

## 9. QA-readiness route

1. **Entry.** After WU-PR-08 and WU-DOC-01 have merged and their PR-40 lineage reviews are accepted, and WU-OPS-01 is planned (OPS-10) or executed, continuing Isis performs QA-10 (Glow QA Guide §3.1.1): a fresh complete implementation audit against this Plan and the approved Specification, the historical comparison with the HDE-EPIC040 records, the change-audit triage and the `QA_READINESS` result. This Plan and its approved amendments are the delivery baseline that QA-10 reconciles (Glow QA Guide "Change-lane QA applicability").
2. **What must be proven (per requirement).** The acceptance intents S01 to S22 as the Specification states them, each with the evidence family this Plan names: lane results on the exact head (CI), the regenerated governed artifacts and their companions (Index, Mirror, path proofs, catalog and mirror, A7 proofs, gate logs, sanity log, engine-core artifacts), the S19 review record, the wheel-install admission test, the catalog route-enumeration test, the vendor-override matrix tests, the close-pack dry-run tests, the retirement ledger, and the PR result records. QA execution evidence lives only under `audit/qa/hde-crd-0002/` and is published by the canonical updater (WU-PR-02).
3. **Production-affecting Live QA minimum.** The QA Plan (Kronos, QA-50, reviewed by Isis at QA-70) includes at least one bounded open-rails live step in the deployed target and the mandatory live vendor call under `SAFE_MODE=0`, `ALLOW_NETWORK=1` with synthetic data only, for the functional-feature class (S14; S02, S10, S07, S08; S15 catalog-only after EC-8), initiated for `--allow-prod-vendor` by an authenticated human Product Owner or an explicitly delegated human operations executor (HDE-CLI-API-Vendor-Ref §7.1.11e; Specification "Override initiator"); S01's class-2 step or its recorded exemption basis from WU-OPS-01's discovery; S19 fixes by their surface's class (Glow QA Guide §3.5.5; Change Process Guide §1.1.5A; Audit §7.4). This Plan designs none of those steps.
4. **Prerequisites that are not gates.** No QA Guide or QA Plan is a prerequisite of any PR unit; the S21 ADR's approval is a Close Gate prerequisite, not a QA-entry prerequisite; PF10 drainage is never a gate.
5. **Close Gate.** HDE-CRD-0002's own close pack is produced by the S21 writer after the ADR is approved (AQ-1); if the ADR is not approved by then, the ordinary Close Gate is not available and the Product Owner decides (Change Process Guide §3.5.1 "Exceptional closure record"); this Plan does not pre-decide it.

## 10. Release re-cut procedure (binding method for WU-PR-03, WU-PR-04, WU-PR-05 when a member changes, and WU-PR-08)

1. Member bytes final; `.json` members canonical bytes, `.py` members one final LF (cutter member-format rule).
2. Cut: `python scripts/cut_release_manifest.py --version <V> --built-at-utc <T> --roster-from-admission`, then `python scripts/release_id_recompute.py --check-manifest-only`, then the cutter with `--check`. `<V>`/`<T>` are the current constants for a refresh (`1.3.0` / `2026-08-24T18:04:49Z`) and the new constants for the version bump (`1.4.0` / the cut time, set in `engine/config/registry_loader.py` first).
3. Admission and goldens: real-root admission reports the version, 45 members and the new `release_id`; `tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>` exit 0.
4. Canonical JSON gate (`tools/evidence/run_canonical_json_gate.py`, then `--check-only`).
5. Updater (`tools/evidence/update_evidence_index.py`, then `--check`).
6. Config family (`generate_config_artifacts.py --publish-family`; updater `--check`).
7. Live producers under closed rails: A7 family (`HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`), determinism family, open-rails fixture proof (fixture mode, keys absent) with the `FROZEN_OPEN_ABBA_SHA256` refresh, F07 writer evidence; then the engine-core owner (`tools/evidence/generate_engine_core_evidence.py`).
8. Updater and every read-only check (`orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `check_lf_endings.py`, `check_final_lf.sh`, `refresh_step_logs_manifest.py --check`).
9. Sanity pipeline (non-canonical run must end `summary:PASS`, then the canonical run and its gate; updater `--check`).
10. Frozen families: `generate_showcompat_artifacts.py --check`, `generate_cli_conformance_artifacts.py --check`, `generate_rails_gate_evidence.py --check`, `generate_env_matrix_snapshot.py --check` exit 0 with no write.
11. Stale-binding sweep outside `docs/`, `.audit_src/`, `handoff/` for the superseded `release_id` and digests: none remain.
12. Tests and candidate-wide lanes on the exact head; attestation rehearsal into an external empty directory with `--require-clean`.
Any member byte change after step 2 restarts at step 2; any evidence-primary change restarts at step 5; steps 4–10 must be byte-stable on a second run. (Method proven by `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §5.4 and executed by PR06a and PR06b; an observed precedent, not canon.)

## 11. Risks

| ID | Risk | Unit | Treatment |
| :---- | :---- | :---- | :---- |
| R-1 | S03 enlarges beyond one PR (real defects, many retirements). | WU-PR-01 | Bound by the Audit's classes; RS-10 if needed; never skip or quarantine a test. |
| R-2 | Convergence run out of order or repeated with member changes in between. | WU-PR-03/04/05/08 | §10 restart rules; second-run byte stability. |
| R-3 | Audit sink or actor identity unavailable in the operator shell at Live QA. | QA | Specified refusal; the QA Plan verifies the sink before the live call. |
| R-4 | S21 ADR unapproved when HDE-CRD-0002 reaches closure. | closeout | §9.5; Product Owner decision. |
| R-5 | S19 findings enlarge the work after the surface units merged. | WU-PR-05 | Fixes precede the version bump; larger findings route with reasons or go to RS-10. |
| R-6 | Top-level wheel data directories collide in a shared site-packages. | WU-PR-08 | Dedicated-environment install documented in WU-DOC-01. |
| R-7 | Catalog validator extension precedes HDE Schemas & Artifacts registration of `public_aux` and `aliases`. | WU-PR-03 | Follow the HDE-CLI-API-Vendor-Ref §5.6 projection; doc-delta candidate; no conformance claim. |
| R-8 | Three or four manifest refreshes before the version bump multiply convergence effort. | WU-PR-03/04/05 | Accepted: admission's byte binding leaves no alternative without rewriting the loader (a member); units are ordered to minimize refreshes. |
| R-9 | Deployment trigger unknown delays Live QA placement. | WU-OPS-01 | OPS discovery is bounded and secret-safe; recorded as a PF07 doc-delta candidate. |

## 12. Exclusions (carried from the Specification; none added)

No Reader contract or payload change and no new public route; no release re-cut beyond the refreshes admission forces and the single `1.4.0` cut; no new evidence family, acceptance token or token matrix except the S21 ADR-admitted close-run home; no canon change beyond S21's ADR-covered close-pack change; as implementation work no deployment, production configuration change or live vendor call (the bounded Live QA steps and WU-OPS-01 are not implementation work); no change to the code-review tooling; no retroactive close pack for HDE-EPIC040; no PF09 mapping; no SessionStart hook; item 6(a) not delivered (RD-1); the "Not reopened" list of the Specification unchanged.

## 13. Unresolved decisions

| ID | Decision | Owner | Effect | Stage deadline |
| :---- | :---- | :---- | :---- | :---- |
| AQ-1 | Approval of the S21 ADR as WU-PR-07 drafts it (Audit §8). | Product Owner | Gates reliance on the new writer's output for any Close Gate; does not gate this Plan, WU-PR-07's merge or QA entry. | Before any Close Gate relies on S21's output. |

No engineering decision remains open at Plan level; EC-1 to EC-12 are recorded in Audit §7.1 and applied here. Isis may redline any of them. Infrastructure facts the Plan names are PF07-derived or classified `discoverable by OPS` (WU-OPS-01); none is left to an unnamed owner.

## 14. Migration and rollback

No data migration: no database schema, catalog content or stored BodyGraph changes. Rollback of any merged unit is the Product Owner's revert of its squash commit; a reverted member-changing unit needs a same-version manifest refresh (§10) in the revert PR; a reverted WU-PR-08 restores the `1.3.0` constants and manifest and re-converges. Generated evidence is never rolled back by hand.

## 15. Conflict-register treatment

CR-1, CR-2 and CR-3 are applied as the Specification's interim treatments state: no PF30 entry is created or required (CR-1); this Plan, not the Specification, carries the work units (CR-2); `HDE-CRD-0002` is the Product Owner-assigned ID and the Specification is the governing record wherever canon points at a PF30 record (CR-3; QA root `audit/qa/hde-crd-0002/`, close-pack prefix `CRD-0002`, Ops root `audit/ops/hde-crd-0002/`). Drainage stays with the Product Owner. No new canon conflict was found by the Audit; HDE-CLI-API-Vendor-Ref §5.6's dependency on an HDE Schemas & Artifacts registration (R-7) is a drainage item, not a conflict.

## 16. RECOVERY_ENVELOPE (checkpoint)

```yaml
paused_prompt: none — IA-10 (100926.1) Phase 2 complete; Plan awaits IA-30 review
phase: PLAN_PENDING
base_identity: Specification v1.1 approved (blob c4802a5a7fa33db38d42d8a7f64679cd18b50480); Audit v1.0 (docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md); PF10 v13.5.2, overlays NONE
checkpoint_identity: this artifact, docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md, repository head 982071b8203bfed961091811e24f57e99f92e593
completed_work: architecture, invariants, interfaces, traceability, ten ordered work units, QA-readiness route, re-cut procedure, risks, exclusions, unresolved decisions, migration and rollback, conflict-register treatment
open_question: AQ-1 (Product Owner; non-blocking for review)
evidence: Audit v1.0 §3, §5, Appendices A and B
answer_state: not required for continuation
remaining_work: IA-30 INITIAL_PLAN_REVIEW by Isis; on INITIAL_DENY, IA-40 by this same author
same_author_return: whole-change IA for HDE-CRD-0002, session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah
prerequisites: the Audit and this Plan on main; nothing else
```

## 17. TypeSafe reading for the receiving session (IA-30 review)

Action sent (v6): "Review, as the independent whole-change Implementation Plan reviewer, a new 120 KB Implementation Audit and a new 60 KB initial Implementation Plan for an approved 22-requirement CRD Specification (CI coverage of 135 uncovered test files, release-evidence tooling, production HTTP error shaping and a dev-route gate, a canon production vendor-override contract with audit, a code security review of four merged PRs, a pre-push check tool, a close-pack writer with an ADR, packaging and one release re-cut), checking every requirement's disposition and the ten ordered PR, Ops and documentation work units against canon and the repository, then approving or returning itemized redlines. No code is written and no live run occurs; a Product Owner Proceed per PR and independent QA follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 3.36 (confidence 0.57); rung probabilities low 0.00, medium 0.01, high 0.18, extra high 0.25, max 0.55, ultracode 0.01. Model probabilities Fable 5.1 0.29, Opus 5.5 0.71 (confidence 0.42). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.13, Opus 5.5 at extra high 0.18, Opus 5.5 at max 0.39, Opus 5.5 at ultracode 0.01, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.07, Fable 5.1 at max 0.16, Fable 5.1 at ultracode 0.00. Sent 2026-10-12T20:30:55Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T20:30:55Z; HTTP 200 in 0.63 s; 4276 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: none; the rule's cell (Opus 5.5 at extra high) differs from the single most probable cell (Opus 5.5 at max 0.39), as the skill allows.
- **One send:** this reading was taken once, before the Audit and the Plan were saved, and is recorded identically in both artifacts.
- **Nathan's pick for IA-30:** not stated.
- **Nathan's pick for this IA-10 session:** not stated (the reading for IA-10 is recorded in review v1.1 §7).

**Surface advice:** run IA-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the continuing Isis reviewer lineage. It reads the approved Specification, review v1.1, the Audit and the Plan from `main`, `docs/pfcanon/` on `main`, and the repository files the Audit cites (the classifier, `ci.yml`, the updater, the resolver and CLI parser, the attestation builder, the close-pack writer and schema, `pyproject.toml`); it needs no live vendor, production or database access and writes only its review artifact under `docs/ephemeral/`. The pull request carrying the Audit and the Plan should be merged to `main` first.

## Canon relied on

The Audit's "Canon relied on" block applies to this Plan in full (same head `982071b`, same reads); the sections this Plan additionally applies are:

- PF04-Canon-HDE-Governance v2.8.7: §9.1.1 (the change-wide Implementation Plan identifies planned PR work units and Ops tasks with purpose, bounded scope, outcomes, order, dependencies, handoffs and validation, migration, rollback and evidence obligations; it creates no PRs or effects; the Product Owner's only runtime approval point is the detailed per-PR Plan); §9.7.1 (Stage A); §9.7.7 (artifact-level detail; identifier and evidence proportionality; QA planning is post-implementation; no hidden acceptance; no scope laundering; no proof by intent); the planning-posture rules (no PF update mandates; documentation drainage never a gate; infrastructure source rule) and the mechanical-blocker list (concrete deliverable paths; no DEV + OPS mixing).
- PF06-Canon-Change-Process-Guide v2.5.4: §3 "IMPLEMENTATION PLAN" (the IA drafts; Isis approves once; tasks atomic; blockers and resolutions; Close Gate route-aware: PR-first, up to 10 PRs, each self-contained; feedback-free terminal lifecycle; exceptional closure record); the Live QA planning rules (PF07-derived / PF10-live / OPS-discoverable / PF07-gap postures; no placeholder ownership); §1.1.5A; §0.5.1 locus labels; §1.0.5 (ADR for a canon-changing CRD) and §1.0.6 (full QA; CI success is not QA acceptance).
- PF27-Canon-Plan-Templates v2.0.5: "Artifact execution boundary" (initial Implementation Plans define intended work, boundaries, dependencies and proof obligations, never Live QA runbooks); "Repository loci and file minting" (concrete filenames; no new top-level root without ADR and PO approval); "Unknowns, discovery, deferral, and open rails" (classification vocabulary; bounded open-rails work belongs to QA Plans and Ops); §2A "Alchemical phase separation", "Existing-template reuse and substitution", "Canon, QA, and closeout boundaries"; §3 "Ops Task Record (Template)" (execution authority, IA facilitation, not a PR, required fields, evidence posture); "CI lane classification and automated budget-control discipline".
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability"; §3.1.1 (QA-10 by continuing Isis); §3.5.5 (production-affecting Live QA minimum); "QA evidence and work-product path grammar"; the close-pack sections.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §7.1.11a–f (IF-1, IF-2); §5.6 (IF-6).
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: §1.2 close-pack artifacts and change-container compatibility (IF-3); §8.17 change-container identity (QA root); §8.12 (A7 proof write gating).
- PF07-Canon-Glow-Infrastructure v2.3.3: §2.4, §2.6, §3.1, §4.1, §10 (WU-OPS-01 facts and gaps).
- PF10-HDE-Build-Notes v13.5.2: addendum 2.1 (§17 only); silent on the subject matter.
- `AGENTS.md`: release identity and admission addition; sole Index/Mirror writer; HDE-EPIC039 workflow posture; PR-description rules; QA output placement; canon-first rule.

**In-flight documents:** the Specification (approved representation and reviewed source), review v1.1, the Audit v1.0 (same invocation), the class-selection record and briefs v1.2; HDE-EPIC040-PR06b plan v1.0 §5.4 and §6.2–6.4 (re-cut method, observed precedent). **Prompts read:** IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1; IA-30 — Review Whole-Change Implementation Plan — 100926.1. Prompt release: GCFPE-20261009.1 / 100926.1.

---

**State:** `PLAN_PENDING` — initial change-wide Implementation Plan for HDE-CRD-0002, unapproved, submitted to Isis for IA-30 `INITIAL_PLAN_REVIEW`.

**ASK OK?**
