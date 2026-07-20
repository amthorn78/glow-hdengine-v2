# Rescoping CRD - HDE-EPIC038 - POST-PR359-REMEDIATION

## 1. Document Control

| Field | Value |
|---|---|
| CRD ID | `CRD-HDE-EPIC038-POST-PR359-REMEDIATION` |
| Version | `v1.4` |
| Supersedes | `v1.3` for the complete `POST-PR359-REMEDIATION` slice |
| Epic | `HDE-EPIC038` — Distillation Pass 3 |
| PR or slice ID | `POST-PR359-REMEDIATION` (the remediation of the merged PR-06 scope) |
| Author role | Sekhmet |
| PO rescoping authorization | `APPROVED` |
| Implementation Agent review | `PENDING` |
| Creation date | `2026-07-20` |
| Confirmed current finding IDs | `BUG-004`, `BUG-005`, `BUG-006`, `BUG-007`, `BUG-008`, `BUG-009` |
| Confirmed retained-repair IDs | `BUG-001`, `BUG-002`, `BUG-003` |
| Repo identity | `amthorn78/glow-hdengine-v2` |
| Repo root reviewed | Connected GitHub repository root `/` for `amthorn78/glow-hdengine-v2` |
| Observed HEAD | `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a` (`docs: update PF10 build notes to v12.3.2`) |
| Branch state | `main`; connected read-only repository view, not detached |
| Working-tree posture | Not applicable to the connected remote view. Inspection was read-only before and after; no local product-Repo working tree was used or changed. |
| PF-Canon source | Current `docs/pfcanon/**` at the observed HEAD, plus the current session-provided complete PF10 v12.3.2 where it governs the exact retired-bridge topic |
| Current plans used | `r1 Epic Plan HDE-EPIC038.md`; `r6 Implementation Plan HDE-EPIC038.md` |
| Prior CRD lineage used | `approved-rescoping-crd-hde-epic038-post-pr359-remediation-v1.3.md` |

### Source units used

- Current Debugging Context from the confirmed post-PR359 remediation findings through the PO's retirement of `pg-bridge`, the failed/ineligible OPS-01R outcome, the PF10 v12.3.2 adoption, and the present request to replace the obsolete bridge-dependent remediation.
- Repo loci: `engine/db/adapter.py`; `engine/db/errors.py`; `engine/db/providers/psycopg_provider.py`; `engine/db/providers/bridge_provider.py`; `adapter/db_access.py`; `scripts/db/capture_epic011_posture.py`; `scripts/ops/hde_epic038_ops01r.py`; `tools/evidence/hde_epic038_ops01_v5.py`; `tools/evidence/generate_db_bridge_parity.py`; `tools/evidence/generate_db_runtime_posture.py`; `tools/evidence/generate_v2_mapped_cache_evidence.py`; `tools/evidence/generate_architecture_snapshot.py`; `tools/evidence/run_sanity_pipeline.py`; `tools/evidence/update_evidence_index.py`; the directly affected tests and active operator guidance; the retained `audit/ops/hde-epic038/ops-01/**` and `ops-02/**` bindings.
- PF10 — HDE Build Notes, v12.3.2, §2.12 `pg-bridge and DB_BRIDGE_URL Deprecation and Retirement - Direct PostgreSQL Is the Sole Active HDE Database Transport`, read as a complete unit with its adoption and nonclaim boundaries.
- PF09.6 — Canon HDE Build Checklist Distillation, v1.1.2, §0.2 and complete rows `HDE-DIST001.4`, `HDE-DIST001.6`, `HDE-DIST001.9`, `HDE-DIST001.11`, and `HDE-DIST005.2`.
- PF07 — Glow Infrastructure, v2.2.4, §§4.1, 4.2, 7.0, 7.1, 8.1, and 9.2.
- PF12 — HDE Schemas and Artifacts, v2.7.8, §§8.6.3.4 and 8.7, including the bridge evidence, Index, Mirror, checksum, and path-proof units.
- PF14 — HDE Mechanics Guide, v3.4.3, §§20.3 and 20.3.1.
- The complete PR-06, OPS-01, OPS-02, PF09 Completion Scope, and D1/D8/D10/D12/D13 units of the current Implementation Plan.

Evidence pointer: Repo | connected GitHub commit `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a` | "docs: update PF10 build notes to v12.3.2"

Evidence pointer: PF10 - HDE Build Notes | §2.12, `Decision and effective posture` | "`DATABASE_URL` is the sole canonical HDE database endpoint key." | "Direct PostgreSQL access through the Glow-owned psycopg provider is the sole active HDE database transport."

## 2. Executive Summary

The previous v1.3 remediation was technically coherent for a bridge-dependent architecture, but that architecture has now been explicitly retired. Its proposed OPS-01R recapture and bridge-dependent v5 integration can no longer produce current completion evidence. At the same time, the current Repo still contains selectable bridge runtime code, a second bridge-capable resolver, bridge-only generators and validators, a bridge-required release stage, bridge-dependent mapped-cache safety instrumentation, and current evidence bindings that can still interpret the historical OPS-01 packet as a current direct-versus-bridge PASS. Current PF09.6 and the current Implementation Plan also still express direct-versus-bridge parity as the completion contract for `HDE-DIST001.9`.

The selected architecture is a complete direct-only cutover with one runtime façade, one active provider, one separately versioned direct-only local evidence artifact, one bounded direct-read OPS packet, and one atomic final integration. The minimum coherent execution sequence to be incorporated into a later authorized plan revision is:

1. **PR-06R-A — Direct-only source and capture tooling:** remove active bridge behavior and bridge execution surfaces; converge both DB resolver modules on direct-only selection; add strict retired-key refusal; create the direct-only local evidence producer, OPS-03 runner, independent validator, schemas, and tests; update the release pipeline structure without claiming final completion.
2. **OPS-03 — Direct PostgreSQL read-only posture capture:** on the exact merged PR-06R-A commit, perform one authorization-bound, no-retry, direct-only DB observation under a read-only transaction; produce a secret-free candidate packet outside the Repo; make no Railway CLI call and make no SQL write.
3. **PR-06R-B — Atomic evidence integration and release binding:** validate and copy the exact OPS-03 packet, switch the canonical sanity pipeline to the direct-only contract, retain old bridge material as historical integrity evidence only, refresh governed companions through the canonical updater, and produce the support needed for later PF09 status decisions.

This rescope cannot be deferred safely while claiming the affected rows closeable. Deferral leaves active code capable of selecting a removed service, keeps retired configuration names executable, makes the canonical release gate depend on a forbidden bridge target, and leaves `HDE-DIST001.9` impossible to satisfy truthfully. The change is bounded: it does not redesign PostgreSQL, change public Reader/CLI bytes, change durable BodyGraph payloads, rerun historical OPS-01 or OPS-02, prove Railway service inventory, perform database writes, or move PF09 status.

Canon effects are exact and bounded: `SUPERSEDES` for active bridge runtime and bridge-required evidence semantics; `EXTENDS` for the new direct-only OPS-03 evidence contract where current PF12 is silent; and `AMENDS` for the remaining direct-only meaning of PF09.6 rows `.4` and `.9`. The current `r1` plan remains the approved epic-scope baseline. The current `r6` plan must later be revised to replace its PR-06/OPS-01 bridge path with PR-06R-A → OPS-03 → PR-06R-B before implementation relies on this CRD.

Evidence pointer: Repo | `engine/db/adapter.py`, `DBAccess.for_current_env` | current order is `['psycopg', 'bridge']`; the method consumes `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD`.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py`, `STAGE_NAMES` and OPS-01 validation | current stage 09 is `DB-bridge parity`; current constants require direct provider `psycopg`, bridge provider `bridge`, and bridge-specific OPS-01 predicates.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `HDE-EPIC038 and OPS-01R disposition` | "The bridge-dependent HDE-EPIC038 OPS-01R lane is retired." | "the bridge-dependent PR-C packet-integration lane described in PF10 §2.9 is canceled and MUST NOT be executed"

## 3. Authority and Decision Posture

### PO rescoping authority

The PO has authorized bounded rescoping of the active HDE-EPIC038 post-PR359 remediation. The PO has also made the exact-topic architecture decision that `pg-bridge` and its control keys are retired. This authority permits Sekhmet to author this technical CRD. It does not prove the design correct, authorize implementation, execute OPS, or move PF09 status.

### Sekhmet proposed technical decisions

The architecture, APIs, schemas, paths, keys, producer assignments, migration order, validation predicates, rollback posture, and plan consequences in `RSC-002` through `RSC-005` and `ADR-CANON-005` through `ADR-CANON-008` are **Proposed CRD decisions**. They do not claim to exist in the current Repo. The retained non-bridge work in `RSC-001` is observed current Repo reality and is not proposed for reimplementation.

### Pending IA technical review

IA must approve or return this CRD based on technical accuracy, causal coverage, minimum scope, implementation feasibility, evidence completeness, ownership uniqueness, compatibility, migration safety, validation, rollback, plan consequences, canon effects, and preserved boundaries. Section 14 supplies the exact gate.

### Later authorities

After IA approval:

- a separately authorized next-version revision of the current Implementation Plan must incorporate the selected sequence and replace the obsolete bridge-dependent plan clauses;
- separate implementation authorization is required before either PR-06R slice is executed;
- task-specific PO authorization is required for the exact OPS-03 authorization bytes and execution target;
- permanent PF07, PF09.6, PF12, PF14, and PF04 wording drainage remains later PO-owned documentation work; and
- any PF09 status update remains a separate evidence-backed action after PR-06R-B, not an effect of CRD approval.

### Prohibited inference

Neither PO authorization nor IA approval means implementation complete, OPS complete, QA PASS, acceptance-token satisfaction, PF09 movement, deployment, migration, slice completion, epic closure, or closeout.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `Repository implementation consequences` | "This addendum authorizes no implementation by itself."

Evidence pointer: PF09.6 - Canon HDE Build Checklist Distillation | §0.2, `Supportable vs drained status notes` | "Supportable from repo evidence: repo evidence supports the status change, but PF09 has not yet been updated."

## 4. Debugging Flow Basis

### Complete finding and action disposition ledger

| ID | Material item | Classification | CRD disposition |
|---|---|---|---|
| `BUG-001` | EPIC024 acceptance bindings pointed at the obsolete sanity path. | Confirmed retained-scope repair | Resolved in current Repo: both the acceptance map and token matrix bind `audit/gates/sanity_pipeline/sanity_pipeline.log`. Preserve; do not rerun or reopen EPIC024. |
| `BUG-002` | Retained-evidence raw-marker matching missed non-JSON forms. | Confirmed retained-scope repair | Resolved in current Repo by `tools/evidence/retained_evidence_safety.py`; preserve its exact multi-syntax and secret-reference protections. |
| `BUG-003` | DDL parity used duplicated, unversioned, projection-only logic while presenting a broader match. | Confirmed retained-scope repair | The pure `engine/db/ddl_identity_projection.py` contract exists and remains required. Retain `ADR-CANON-004` only for the projector and projection-only truth semantics; supersede its bridge transport/evidence dependencies. |
| `BUG-004` | The primary DB façade still imports and selects `BridgeProvider` and consumes retired bridge keys. | Confirmed rescoping premise | Mandatory `RSC-002` / `ADR-CANON-005`. |
| `BUG-005` | `adapter/db_access.py` independently attempts DSN and HTTP bridge paths and can bypass the primary façade's provider policy. | Confirmed architectural conflict | Mandatory convergence under `RSC-002`; no second selection owner remains. |
| `BUG-006` | Active DB posture, parity, OPS-01R, validator, CI checker, and release-sanity tools still require bridge construction or bridge evidence. | Confirmed rescoping premise | Mandatory retirement/replacement under `RSC-002`, `RSC-003`, and `RSC-005`. |
| `BUG-007` | Current PF09.6 `.4` and `.9` and the current r6 D8/D10/PR-06/OPS-01 plan clauses still require active bridge fallback or direct-versus-bridge parity. | Confirmed canon/plan conflict | Mandatory bounded amendment under `RSC-005` / `ADR-CANON-008`; no status movement in this CRD. |
| `BUG-008` | The canonical updater and release pipeline bind the historical OPS-01 bridge packet as current PR-06 OPS evidence and derive a current bridge PASS. | Confirmed evidence-meaning conflict | Historical quarantine plus direct-only replacement under `RSC-003`, `RSC-004`, and `ADR-CANON-006`/`007`. |
| `BUG-009` | The mapped-cache evidence generator and tests import and intercept `BridgeProvider` as part of no-I/O safety proof. | Confirmed dependency conflict | Remove bridge imports while preserving generic external-I/O refusal and existing OPS-02 evidence under `RSC-002` and `RSC-005`. |
| `STALE-001` | The earlier shell-default secret-reference concern. | Stale/superseded | No new scope. Preserve current strict `SAFE_ENV_REFERENCE` regression coverage. |
| `STALE-002` | Earlier concern that direct/bridge labels were not source-bound. | Stale/superseded | No new bridge work. The entire current bridge label contract becomes historical. |
| `BLK-001` | Earlier reported temporary OPS-01R import failure and candidate uncertainty. | Superseded tooling/evidence blocker | PF10 truthfully retains the failed/ineligible attempt. It no longer justifies a recapture, discovery task, or bridge repair. No old candidate is accepted. |
| `ACT-001` | PR 359 merged the original PR-06 implementation. | Relevant completed action | Historical scope boundary only; PR 359 is not reopened. |
| `ACT-002` | The non-bridge v1.3 repairs were implemented in current Repo. | Relevant completed action | Preserve `BUG-001`/`002`/`003` repairs and their current evidence; do not duplicate them. |
| `ACT-003` | OPS-01R was attempted and did not produce an admissible v5 candidate. | Relevant failed action | Retain failure classification; no retry or relabeling. |
| `ACT-004` | The PO reports the Railway `pg-bridge` service has been removed. | PO-reported external action | Architecture premise only. This CRD does not claim external inventory proof and does not add Railway discovery to closure scope. |
| `ACT-005` | PF10 v12.3.2 §2.12 adopted direct-only HDE database transport and retired the bridge lane. | Current controlling exact-topic decision | Primary canon basis for this rescope. |

### Confirmed RCA conclusions

1. The current blocker is not a missing bridge observation. It is a contract split: current exact-topic canon is direct-only while executable source, current evidence semantics, PF09 wording, and the implementation plan still encode bridge fallback and parity.
2. Removing only `engine/db/providers/bridge_provider.py` would not close the conflict. A second resolver, DB posture producer, mapped-cache proof, OPS runner/validator, release pipeline, updater bindings, tests, and guidance would still import, execute, or require the retired path.
3. Reusing historical OPS-01 as current direct-only proof would be false. Its bridge fields and PASS predicates describe the architecture at capture time and must remain byte-stable history.
4. Another OPS-01R run cannot solve the current problem. It would exercise an explicitly retired target and produce an evidence family PF10 forbids as current completion evidence.
5. The remaining live fact needed for `.4`/redefined `.9` is direct PostgreSQL posture under read-only rails. It can be captured without Railway CLI discovery, bridge inventory, DB writes, or provider parity.
6. The direct-only implementation and the direct-only live packet must land in separate PR boundaries because OPS-03 must execute against immutable merged capture tooling, while final Index/Mirror and release binding must consume the exact reviewed packet without rerunning OPS.

### Rejected alternatives

- **Repair or recreate `pg-bridge`:** rejected; it contradicts current PF10 and the PO retirement decision.
- **Leave bridge code dormant:** rejected; retired keys could still select or revive it, tests would preserve it, and current evidence tooling would continue to make it an active contract.
- **Treat missing `DB_BRIDGE_URL` as sufficient closure:** rejected; configuration absence does not prove direct runtime behavior, direct DB posture, release integration, or Index/Mirror coherence.
- **Relabel OPS-01 or OPS-01R as direct-only evidence:** rejected; that rewrites historical meaning and violates PF10.
- **Eliminate OPS entirely:** rejected; Repo-local fixtures can prove selection semantics, but they cannot prove the live/shared direct database posture required for the DB runtime row.
- **Repeat Railway discovery before direct DB capture:** rejected; the retired service inventory is not a predicate of the remaining PF09 obligations, and Railway CLI discovery caused complexity without proving direct DB posture.
- **One implementation PR that also contains post-OPS evidence:** rejected; the OPS runner must exist at an immutable merged source identity before execution, and an implementation author must not fabricate later external evidence.

### Residual non-material unknowns

- Actual direct DB availability at OPS-03 execution is unknown until the authorized read-only capture. It does not change the architecture; failure produces a bounded negative receipt and blocks PR-06R-B.
- Current Railway service and variable inventory is not independently proven here. It is not a completion predicate in this rescope; any future need for that proof requires a separate task.
- OPS-03 run ID, timestamps, authorization hash, source hashes, and packet checksums are derived at execution. They are not design unknowns.

Evidence pointer: Repo | `docs/acceptance_map_epic024.json`, token `SANITY_PIPELINE_OK` | current evidence title is `audit/gates/sanity_pipeline/sanity_pipeline.log`.

Evidence pointer: Repo | `tools/evidence/retained_evidence_safety.py` | `_RAW_MARKER` accepts quoted or unquoted keys with `:` or `=`; `SAFE_ENV_REFERENCE` accepts only direct `$NAME` or `${NAME}` references.

Evidence pointer: Repo | `tools/evidence/generate_v2_mapped_cache_evidence.py` | current imports include `engine.db.providers.bridge_provider`; current I/O guards patch both bridge provider construction and bridge HTTP functions.

## 5. Current Contract and Observed Conflict

### Implemented contract

The current implementation has two DB-selection owners:

- `engine/db/adapter.py::DBAccess.for_current_env` selects in the default order `psycopg` then `bridge`, accepts `bridge_factory`, reads `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD`, and writes a bridge-named adapter-selection artifact by default.
- `adapter/db_access.py` independently implements `_try_dsn`, `_try_bridge`, `db_resolve`, `resolve_env_matrix`, and `db_rw_smoke`; its bridge path performs `urllib.request` calls and its result schema exposes both `dsn` and `bridge` branches.

The current evidence contract also has multiple active bridge owners:

- `scripts/db/capture_epic011_posture.py` captures both direct and bridge providers and writes current bridge parity artifacts.
- `tools/evidence/generate_db_bridge_parity.py` produces adapter selection, capabilities, provider parity, env connectivity, non-dev bridge failure, and presenter compare evidence.
- `scripts/ops/hde_epic038_ops01r.py` and `tools/evidence/hde_epic038_ops01_v5.py` implement the retired bridge-dependent recapture.
- `tools/evidence/run_sanity_pipeline.py` names stage 09 `DB-bridge parity`, invokes the bridge generator, and derives current OPS-01 PASS from bridge predicates.
- `tools/evidence/update_evidence_index.py` binds all OPS-01 and OPS-02 primaries under current `epic038_pr06_ops_evidence` records.

### Current canonical contract

PF10 v12.3.2 §2.12 controls the exact retired topic until permanent drainage. It requires `DATABASE_URL` and direct psycopg only; treats any retired bridge key as configuration drift; requires direct failure to fail closed; retires OPS-01R and bridge-dependent PR-C; freezes the existing OPS-01 packet as history; and requires any future direct-only evidence family to have a separate contract.

Older owning canon has not yet been drained:

- PF07 §§4.1, 4.2, 7.0, 7.1, 8.1, and 9.2 still list `pg-bridge`, bridge precedence, and `DB_BRIDGE_URL`.
- PF14 §§20.3 and 20.3.1 still require `BridgeProvider`, bridge fallback, bridge consistency, and current provider parity.
- PF12 §8.7 still catalogs the bridge evidence family and current bridge-related token posture.
- PF09.6 `.4` still names bridge fallback/provider parity in its semantic home; `.9` is still explicitly direct-versus-bridge parity.

These older rules are not silently discarded. PF10 expressly supersedes them on the exact retired topic, and `ADR-CANON-005` through `008` define the bounded implementation and later permanent drainage.

### Current plan contract

The current r6 plan maps:

- D8 / `HDE-DIST001.4` to PR-04, OPS-01, and PR-06;
- D10 / `HDE-DIST001.9` to PR-04, OPS-01, and PR-06 with live direct/bridge parity;
- D12 / `HDE-DIST001.11` to PR-05, OPS-02, and PR-06;
- D13 / `HDE-DIST001.6` to PR-06; and
- D1 / `HDE-DIST005.2` to PR-01 and PR-06.

Its PR-06 ordered stages and final evidence binding require OPS-01 and bridge parity. Those clauses are now stale. The plan remains authoritative for the affected deliverables, existing non-bridge dependencies, and final integration purpose; it is not authoritative for a retired architecture.

### Exact conflict

The current Repo can execute a bridge that current exact-topic canon forbids; the current release gate requires proof that current canon forbids producing; and the current PF09/plan completion language requires direct-versus-bridge parity against a service the PO retired. Therefore neither rerunning the old task nor merely deleting a service can create truthful completion support.

### Dependency preventing an isolated fix

The dependency graph is:

`retired environment keys` → `two DB resolvers` → `BridgeProvider` → `DB posture/parity producers` → `mapped-cache no-I/O instrumentation` → `OPS-01R runner/validator` → `release stage 09 and OPS-01 PASS derivation` → `updater record meaning` → `PF09.6 .4/.9 and r6 D8/D10 closure`.

Changing only one node leaves an executable or evidentiary path that can revive or require the retired contract. A coherent cutover must change the graph as one rescope while preserving immutable historical artifacts.

### Consequence and selected resolution posture

If deferred, direct DB failure can still attempt a removed HTTP service, retired keys remain effective inputs, the release pipeline cannot truthfully pass under current canon, and the affected PF09 rows remain uncloseable. The selected resolution is direct-only runtime convergence in PR-06R-A, bounded direct read-only live capture in OPS-03, and atomic direct-only release/evidence integration in PR-06R-B.

Evidence pointer: PF07 - Glow Infrastructure | §7.0 `Runtime posture (normative)` | "Stage/Test & Dev: select by availability with fallback: DATABASE_URL → DB_BRIDGE_URL(https) → typed error."

Evidence pointer: PF14 - HDE Mechanics Guide | §20.3.1 `Bridge-consistency checker fallback contract` | "The DB bridge parity family MUST preserve DBAccess as the provider-agnostic façade" | "DB bridge parity generator (required). tools/evidence/generate_db_bridge_parity.py is the governed generator"

Evidence pointer: Implementation Plan | PR-06, `Implementation requirements` | current ordered stages include `DB-bridge parity`; current OPS consumption validates both OPS-01 and OPS-02.

## 6. Causal Map

### CAUSE-001 — Active runtime can select a retired transport

- **Linked findings:** `BUG-004`, `BUG-005`.
- **Current contract:** PF10 §2.12 requires direct psycopg only and fail-closed direct unavailability.
- **Repo reality:** both `engine/db/adapter.py` and `adapter/db_access.py` consume `DB_BRIDGE_URL` and can construct or call an HTTP bridge; the primary façade also recognizes two bridge-control keys.
- **Conflict:** two active selection owners can violate the direct-only contract and disagree about rails, errors, attempts, and evidence.
- **Consequence:** a missing or failed direct connection may open forbidden I/O; merely removing the external service converts fallback into delay/failure rather than eliminating it.
- **Selected technical decision:** `RSC-002` makes `engine.db.adapter.DBAccess` the sole selection owner, rejects retired keys before provider construction, removes the bridge provider and bridge-capable compatibility path, and exposes only secret-free direct-selection evidence.
- **Affected dependency graph:** runtime imports, errors, adapter compatibility functions, DB posture tools, BodyGraph resolver consumers, CLI/HTTP DB paths, tests, and active guidance.
- **Current and retained owners:** Glow Repo implementation owns the cutover; direct PostgreSQL and current durable-data contracts remain unchanged; no `pg-bridge` owner is imported.
- **Validation:** focused selection/error tests, exact retired-key tests (including empty values), no-provider-call tests, no-alternate-I/O tests, source scan, secret scan, and current consumer tests.
- **Rollback:** fail closed by disabling DB access or reverting to the last direct-only commit; never restore a bridge-enabled build as an operational rollback.
- **Plan consequence:** allocate direct-only implementation to PR-06R-A before any replacement OPS.
- **Canon/ADR consequence:** `ADR-CANON-005` (`SUPERSEDES`).
- **Evidence pointers:** Repo `engine/db/adapter.py::DBAccess.for_current_env`; Repo `adapter/db_access.py::_try_bridge`; PF10 §2.12 `Runtime and configuration contract`.

### CAUSE-002 — Current evidence machinery assigns active meaning to retired bridge evidence

- **Linked findings:** `BUG-006`, `BUG-008`.
- **Current contract:** PF10 freezes old bridge artifacts as historical and requires a separate direct-only contract.
- **Repo reality:** current generators refresh bridge artifacts; the sanity pipeline derives OPS-01 bridge PASS; the updater binds OPS-01 under current PR-06 record semantics.
- **Conflict:** retaining historical bytes is required, but retaining their current acceptance meaning is forbidden.
- **Consequence:** release evidence can overclaim current bridge availability or require regeneration against a retired service.
- **Selected technical decision:** `RSC-003` introduces one separately named local direct-selection artifact and changes old bridge artifacts to immutable historical bindings; `RSC-005` changes release admission and updater semantics atomically.
- **Affected dependency graph:** direct/bridge generator, architecture snapshot, OPS-01 packet validation, sanity stage ordering, Index/Mirror records, hashes, path proofs, and tests.
- **Current and retained owners:** the original producers retain historical provenance but lose current execution ownership; the new direct producer owns only the new path; the canonical updater remains sole companion writer.
- **Validation:** old primary hashes remain unchanged; new schema is strict/canonical; no current row or release predicate claims bridge success; updater produces exactly one binding per path.
- **Rollback:** revert new direct evidence and generated companions as one PR-B unit while retaining old primaries and their historical bindings; do not regenerate old bridge bytes.
- **Plan consequence:** replace D10's bridge evidence with direct local and OPS-03 evidence; retain D1/D13 updater and release responsibilities.
- **Canon/ADR consequence:** `ADR-CANON-006` (`SUPERSEDES`).
- **Evidence pointers:** Repo `tools/evidence/run_sanity_pipeline.py` OPS-01 constants/derivation; Repo `tools/evidence/update_evidence_index.py::EPIC038_PR06_PRIMARY_ARTIFACTS`; PF10 §2.12 `Evidence and historical-artifact posture`.

### CAUSE-003 — PF09 and plan wording makes a retired parity target a closure condition

- **Linked finding:** `BUG-007`.
- **Current contract:** PF10 retires `.9`'s bridge requirements but leaves `.9` `Partial` pending permanent redefinition; PF09 status semantics allow a later `Done` only when the redefined slice behavior is implemented and evidenced.
- **Repo reality:** PF09.6 `.9` still requires direct/bridge BodyGraph parity; r6 D10 still assigns live direct/bridge parity to OPS-01.
- **Conflict:** current wording is impossible to satisfy without violating the controlling exact-topic rule.
- **Consequence:** even a correct direct-only implementation cannot support truthful PF09 drainage until the row and plan are amended.
- **Selected technical decision:** `RSC-005` and `ADR-CANON-008` redefine `.9` as direct database connectivity and retired-transport enforcement, remove bridge fallback from `.4`, and assign the replacement sequence without automatic status movement.
- **Affected dependency graph:** PF09 `.4`/`.9`, r6 D8/D10/D13, final sanity stages, OPS ownership, and later status notes.
- **Current and retained owners:** PF09/PF maintenance remains PO-owned; PR-06R implementation and OPS-03 produce support only; QA/acceptance/closeout remain downstream.
- **Validation:** exact row predicates and evidence crosswalk in §9; final status recommendation only after all evidence and updater checks pass.
- **Rollback:** if direct-only evidence is incomplete, leave statuses unchanged and retain the proposed wording decision for revision; never restore bridge parity as the fallback closure path.
- **Plan consequence:** later r6-lineage revision replaces PR-04/OPS-01/PR-06 bridge ownership with retained PR-04 evidence plus PR-06R-A/OPS-03/PR-06R-B.
- **Canon/ADR consequence:** `ADR-CANON-008` (`AMENDS`).
- **Evidence pointers:** PF09.6 `.9` complete row; Implementation Plan D10 and OPS-01 units; PF10 §2.12 `PF09 consequences`.

### CAUSE-004 — Mapped-cache safety proof depends on a provider that must be removed

- **Linked finding:** `BUG-009`.
- **Current contract:** `.11` requires safe mapped-cache persistence, read-back parity, idempotence, closed-rails refusal, and no raw vendor persistence; it does not require a bridge provider.
- **Repo reality:** `tools/evidence/generate_v2_mapped_cache_evidence.py` and its tests import and patch bridge classes/functions to prove I/O was not reached.
- **Conflict:** deleting the retired provider would break the safety generator even though bridge behavior is unrelated to mapped-cache semantics.
- **Consequence:** `.11` evidence and final release integration fail unless the no-I/O proof is made transport-neutral.
- **Selected technical decision:** PR-06R-A replaces bridge-specific hooks with generic direct DB/provider and outbound-I/O guards while preserving every existing mapped-cache predicate and the retained OPS-02 packet.
- **Affected dependency graph:** mapped-cache generator/tests, DBAccess, PsycopgProvider connection hook, retained evidence safety, OPS-02 validation, release stage.
- **Current and retained owners:** PR-05 implementation and OPS-02 historical execution are not reopened; PR-06R-A owns only compatibility of their current validator/tooling with the direct-only runtime.
- **Validation:** existing `.11` proof suite plus assertions that no retired provider module is imported and no live DB/vendor call occurs in Repo-local regeneration.
- **Rollback:** revert only the transport-neutral guard refactor if it weakens existing no-I/O checks; leave bridge source absent and fail the mapped-cache stage closed.
- **Plan consequence:** D12 remains PR-05/OPS-02 evidence consumed by PR-06R-B, with a narrow PR-06R-A tooling adaptation.
- **Canon/ADR consequence:** no independent durable-data canon change; covered by the unchanged boundaries of `ADR-CANON-005` and plan consequence in `ADR-CANON-008`.
- **Evidence pointers:** Repo `tools/evidence/generate_v2_mapped_cache_evidence.py` bridge imports and patch roster; PF09.6 `.11` complete row.

### CAUSE-005 — Final closure support requires a new live direct observation and atomic integration

- **Linked findings:** `BUG-006`, `BUG-007`, `BUG-008`.
- **Current contract:** `.4` requires DB posture, `.6` requires one-button release sanity, redefined `.9` requires direct connectivity/refusal posture, `.11` requires mapped-cache proof, and `.5.2` requires same-change Index/Mirror discipline.
- **Repo reality:** Repo fixtures can prove selection and failure semantics; existing OPS-01 cannot prove current direct-only posture; existing OPS-02 remains relevant to `.11`; final updater and sanity ownership already live in PR-06 surfaces.
- **Conflict:** combining implementation and live evidence in one PR would fabricate provenance; omitting live evidence leaves `.4`/`.9` unproven; integrating evidence piecemeal breaks Index/Mirror and release coherence.
- **Consequence:** the affected rows remain Partial/Optional even after source cleanup unless a new direct packet and final atomic binding exist.
- **Selected technical decision:** `RSC-004` defines OPS-03; `RSC-005` defines byte-for-byte PR-06R-B integration and row-specific supportability gates.
- **Affected dependency graph:** PR-06R-A source identity → PO authorization → OPS-03 candidate → independent validation → PR-06R-B copy → updater → sanity → later PF09 decision.
- **Current and retained owners:** PO-authorized executor owns the external read-only action; runner/validator own packet production/admission; PR-06R-B owns tracked integration; PF/QA/closeout owners remain separate.
- **Validation:** exact authorization/packet schemas, exact query roster, transaction read-only enforcement, no retry, candidate checksum, independent validation before and after copy, full release pipeline, updater/path/mirror/hash/LF checks.
- **Rollback:** no PR-06R-B on OPS failure; no partial evidence commit; if integration fails, revert the entire PR-B generated set and leave statuses unchanged.
- **Plan consequence:** explicit PR-06R-A → OPS-03 → PR-06R-B order replaces OPS-01R/PR-C.
- **Canon/ADR consequence:** `ADR-CANON-007` (`EXTENDS`) and `ADR-CANON-008` (`AMENDS`).
- **Evidence pointers:** PF10 §2.12 `Development and OPS access posture`; PF09.6 `.4`, `.6`, `.9`, `.11`, `.5.2`; Implementation Plan PR-06 parent-binding posture.

## 7. Requested Rescope

### RSC-001 — Preserve completed non-bridge remediation without reopening it

- **Requested addition:** No new implementation. Carry forward the current fixes for `BUG-001`, `BUG-002`, and the pure DDL identity projector portion of `BUG-003` as immutable prerequisites of the new remediation.
- **Canon effect:** `NO CANON CHANGE`.
- **Linked causes:** boundary condition for `CAUSE-002`, `CAUSE-004`, and `CAUSE-005`.
- **Reason required now:** a new CRD must not discard valid completed work merely because its bridge-dependent continuation is obsolete.
- **Existing loci:** `docs/acceptance_map_epic024.json`; `audit/qa/hde-epic024/token_evidence_matrix.md`; `tools/evidence/retained_evidence_safety.py`; `engine/db/ddl_identity_projection.py`; their existing tests and governed companions.
- **Contract impact:** none. Preserve current canonical sanity binding, multi-syntax secret/raw marker enforcement, and `hde.ddl_identity_projection.v1` projection-only semantics.
- **Compatibility/migration:** no regeneration except when an affected current producer legitimately changes bytes under PR-06R-B. Historical EPIC024 QA is not rerun.
- **Validation/evidence:** targeted regression tests confirm the current paths and semantics. Final release sanity consumes them as prerequisites.
- **Rollback:** not applicable; this item prohibits reimplementation or regression.
- **Downstream effect:** none beyond continued use.
- **Plan consequence:** the next plan marks prior `RSC-001`/`002` and pure projector work as landed prerequisites, not pending tasks.
- **Documentation consequence:** `ADR-CANON-004` remains applicable only to the pure projector and projection-only truth labeling; bridge-specific v5/OPS clauses are superseded by this CRD.
- **Nonclaims:** no historical QA rerun, new DDL proof, PF09 movement, or acceptance claim.

### RSC-002 — Direct-only runtime convergence and active bridge-surface retirement

- **Requested addition:** one coherent direct-only runtime cutover in PR-06R-A.
- **Canon effect:** `SUPERSEDES` through `ADR-CANON-005`.
- **Linked causes:** `CAUSE-001`, `CAUSE-004`.
- **Reason required now:** the external bridge is retired while current code can still select it; the runtime and evidence tools cannot be truthful until active selection is removed.

#### Proposed CRD decision — sole runtime owner and API

1. `engine/db/adapter.py` remains the sole provider-selection module.
2. Add exact constant `RETIRED_DB_TRANSPORT_KEYS: tuple[str, ...] = ('DB_ALLOW_BRIDGE_IN_PROD', 'DB_BRIDGE_URL', 'DB_FORCE_BRIDGE')`, stored in ASCII order.
3. Add `retired_db_transport_keys_present(environ: Mapping[str, str]) -> tuple[str, ...]`. Presence means key membership, even when the value is empty, `0`, or whitespace. The function returns names only, sorted; it never returns or formats values.
4. Add `engine.db.errors.RetiredBridgeConfiguration`, a subclass of `AdapterError`, with fixed code `retired_bridge_configuration` and a tuple property `retired_keys`. Its public message is exactly `retired_bridge_configuration:<comma-separated-sorted-key-names>` and contains no values.
5. Change `DBAccess.for_current_env` to the exact logical signature `for_current_env(*, environ: Mapping[str, str] | None = None, psycopg_factory: Callable[[str], Provider] | None = None) -> DBAccess`. Remove `bridge_factory` and `snapshot_path`.
6. Selection order is exact: inspect retired-key names; if any are present, raise `RetiredBridgeConfiguration` before reading the `DATABASE_URL` value or invoking a provider factory; otherwise require `DATABASE_URL`; construct one `PsycopgProvider`; run one health operation; return on success; raise typed `PrimaryUnavailable` on missing or failed direct access. No alternate provider, URL inference, retry, or fallback exists.
7. `DBAccess.attempts` contains zero rows on retired-key refusal; otherwise it contains exactly one row for provider `psycopg` with status `ok`, `skip`, or `error` and a stable names-only reason. `provider_name` can be only `psycopg` on success.
8. Add pure method `DBAccess.selection_evidence() -> Mapping[str, object]`. The returned object follows the `hde_epic038.direct_db_selection.v1` case contract below and performs no write. Runtime provider selection never writes governed evidence.
9. Preserve `query`, `exec`, `tx`, `introspect`, and the DDL projector APIs. Add `DBAccess.readonly_tx(statements: Sequence[Statement]) -> List[Sequence[Any] | None]` and the matching `Provider` protocol method. `PsycopgProvider.readonly_tx` uses one connection and cursor, requires the first normalized statement to be exactly `SET TRANSACTION READ ONLY`, accepts only the prevalidated `SET`, `SHOW`, and `SELECT` statement classes supplied by the OPS runner, never calls `commit`, and calls `rollback` in `finally` on success or failure. Existing `tx` semantics remain unchanged for separately authorized callers. This rescope does not broaden write permission.

#### Proposed CRD decision — compatibility resolver convergence

- Replace bridge logic in `adapter/db_access.py` with a thin internal compatibility layer over `engine.db.adapter.DBAccess`.
- `resolve_env_matrix()` retains its tuple return convention but emits schema `hde.db.env_selection.v2` with exact top-level keys `schema`, `ok`, `checks`, `result`, and `error`; unknown keys are rejected by its tests. `checks` contains `DATABASE_URL` plus the exact retired-key roster, each with `present_redacted`, `present_retired`, or `unset`; `result` is `{'provider':'psycopg'}` on success and `null` otherwise; `error` is `null` or exact `{class,code,retired_keys}` names-only data.
- `db_resolve()` returns exact top-level keys `schema`, `active`, `attempts`, and `error`; schema is `hde.db.resolve.v2`; `active` is `psycopg` or `none`; no `dsn` or `bridge` branch remains.
- `db_rw_smoke()` keeps the existing `DB_REQUIRED` gate and direct PostgreSQL behavior only. Remove the HTTP branch. Replace raw exception strings and returned row identifiers with stable names-only codes. No new write authorization is created.
- Update every current consumer and test of these functions in the same PR. Historical transcripts retaining old result shapes are not rewritten.

#### Proposed CRD decision — active retirement roster

- Delete active `engine/db/providers/bridge_provider.py`, `scripts/db_bridge/capture_introspection.py`, `scripts/ops/hde_epic038_ops01r.py`, `tools/evidence/hde_epic038_ops01_v5.py`, `tools/evidence/generate_db_bridge_parity.py`, and `ci/checks/check_bridge_consistency.py` after all current imports/registrations are removed.
- Delete the now-unreachable active `BridgeUnavailable` and `BridgeUnsupported` exception classes and their exports/tests from `engine/db/errors.py`; `RetiredBridgeConfiguration` is the only bridge-named runtime error because it reports prohibited configuration rather than offering a transport.
- Replace the last checker with proposed `ci/checks/check_direct_db_contract.py`, which checks active source and current guidance only. It excludes `audit/**`, `artifacts/**`, `docs/crd/**`, `docs/plans/**`, `docs/pfcanon/**`, historical design records, and changelog history. It fails on active imports, provider registration, HTTP bridge construction, executable bridge commands, or active guidance that instructs bridge use.
- Convert `scripts/db/capture_epic011_posture.py` to direct-only DB posture production. Preserve its current DB posture paths for DDL, grants, schema, constraints, partition, and boundary views; stop writing or refreshing `artifacts/db_bridge/**`, provider-parity direct/bridge captures, or `artifacts/runtime/env_connectivity.snapshot.json` as current evidence.
- Update `tools/evidence/generate_v2_mapped_cache_evidence.py` and tests to patch generic DB/provider and outbound-I/O seams without importing the deleted bridge module. Preserve every `.11` predicate and retained OPS-02 primary.
- Update `generate_env_matrix_snapshot.py`, architecture snapshot production, BodyGraph policy producers, `capture_rails_open_scope.py`, `adapter/http_reader.py`, active docs/guidance, packaging metadata when tracked, and all tests so no executable current path recognizes the retired keys as valid inputs. Retired names may remain only in refusal rosters, historical evidence, explicit history labels, and negative tests.

- **Contract impact:** internal DB selection and internal evidence schemas change; public Reader/CLI response bytes and durable DB payloads do not.
- **Compatibility/migration:** no bridge compatibility shim. Current callers move in the same PR. Direct callers keep the façade operations. Retired-key presence becomes an intentional typed failure.
- **Validation/evidence:** direct selection tests; empty-value retired-key tests; factory-not-called tests; primary failure/no-alternate tests; no-value-in-error tests; active-source scan; mapped-cache regressions; current consumer tests; architecture snapshot regeneration; proposed local evidence in `RSC-003`.
- **Rollback:** do not redeploy bridge-enabled source. If PR-06R-A must be backed out, restore the prior direct provider implementation with bridge selection hard-disabled, or disable DB entrypoints until corrected.
- **Downstream effect:** OPS-03 can observe only direct PostgreSQL; final sanity no longer needs a bridge.
- **Plan consequence:** new PR-06R-A owner and prerequisite to OPS-03.
- **Documentation consequence:** permanent PF07/PF14/PF04 drainage in `ADR-CANON-005`.
- **Nonclaims:** no external service proof, DB migration, DB write authorization, public API change, or status movement.

### RSC-003 — Separate direct-only local evidence and quarantine historical bridge evidence

- **Requested addition:** one new deterministic local direct-selection primary plus explicit historical evidence semantics.
- **Canon effect:** `SUPERSEDES` through `ADR-CANON-006` for current bridge-required evidence meaning; historical bytes remain in force as history.
- **Linked causes:** `CAUSE-002`, `CAUSE-003`.
- **Reason required now:** PF10 forbids mutating bridge packet semantics into a direct-only claim and requires a separate evidence contract.

#### Proposed CRD decision — direct DB selection artifact

| Contract item | Exact decision |
|---|---|
| Schema ID/version | `hde_epic038.direct_db_selection.v1` |
| Schema path | `schemas/hde_epic038_direct_db_selection.v1.json` |
| Primary path | `artifacts/runtime/direct_db_selection.snapshot.json` |
| Artifact key | `epic038.pr06r.direct_db_selection` |
| Record type | `epic038_pr06r_direct_db_selection` |
| Sole producer | `tools/evidence/generate_hde_epic038_direct_db_selection.py` |
| Consumers | `ci/checks/check_direct_db_contract.py`; `tools/evidence/run_sanity_pipeline.py`; `tools/evidence/update_evidence_index.py`; focused unit/evidence tests |
| Unknown-key posture | Reject at every object level |
| Serialization | UTF-8, no BOM, ASCII key sort, compact separators, exactly one trailing LF; arrays retain the contract order below |
| Companion owner | `tools/evidence/update_evidence_index.py` only |

The primary has exactly these top-level fields: `schema`, `retired_keys`, `cases`, `predicates`, `result`, and `failure`. `retired_keys` is the exact ASCII-sorted roster from `RSC-002`. `cases` contains exactly four rows in this order: `healthy_direct`, `missing_database_url`, `unavailable_database_url`, and `retired_keys_present`.

Every case has exactly: `case`, `app_env`, `database_url_presence`, `retired_keys_present`, `attempts`, `selected`, `error`, `alternate_transport_attempts`, and `result`. `database_url_presence` is `present_redacted` or `unset`. An attempt has exactly `provider`, `status`, and `reason`, where provider is only `psycopg`, status is `ok|skip|error`, and reason is a stable string or `null`. `selected` is `psycopg|none`. `error` is `null` or exactly `{class,code}`. `alternate_transport_attempts` is integer zero in every passing case.

The expected cases are exact:

1. `healthy_direct`: one `psycopg/ok/null` attempt, selected `psycopg`, no error.
2. `missing_database_url`: one `psycopg/skip/missing_database_url` attempt, selected `none`, `PrimaryUnavailable/missing_database_url`.
3. `unavailable_database_url`: one `psycopg/error/primary_connect_failed` attempt, selected `none`, `PrimaryUnavailable/primary_connect_failed`.
4. `retired_keys_present`: all three retired names present, zero provider attempts, selected `none`, `RetiredBridgeConfiguration/retired_bridge_configuration`.

`predicates` has exactly `direct_only_provider`, `missing_direct_fails_closed`, `unavailable_direct_fails_closed`, `retired_keys_fail_before_provider_attempt`, `alternate_transport_attempts_zero`, and `secret_values_absent`. `result` is `PASS` only when all predicates are true and all exact case invariants hold. `failure` is `null` on PASS. On failure it is exactly `{code,failed_predicates}` with sorted names-only codes; the producer writes the same path as a negative receipt, exits nonzero, and the release pipeline must not treat it as support.

The schema file is itself indexed under artifact key `epic038.pr06r.direct_db_selection_schema` and record type `epic038_pr06r_schema`.

#### Historical treatment

- Freeze existing primary bytes under `artifacts/db_bridge/**`, the existing bridge-era `artifacts/runtime/env_connectivity.snapshot.json`, bridge presenter comparisons/schemas, and `audit/ops/hde-epic038/ops-01/**` unless a separately authorized historical migration is approved.
- Preserve their existing sibling path proofs, checksums, Human Index rows, and Machine Mirror rows. Updater metadata must classify them as `historical_bridge_evidence` and notes must say they do not prove current service availability, runtime support, provider parity, or token satisfaction.
- The updater may change Index/Mirror record metadata to historical meaning, but it must not change the historical primary or its existing primary checksum ledger.
- The release pipeline validates historical file presence, exact retained checksum ledgers, canonical/readable posture, and secret-safe nonclaims only. It must not recompute bridge predicates or require bridge success.
- Non-governed OPS-01R diagnostics stay failure/decision-support records and are not imported into the governed evidence family.
- `DEV_DB_BRIDGE_FALLBACK_OK`, bridge proof labels, and bridge success fields are not claimable by new rows.

#### Index, Mirror, path-proof, checksum, and release effects

- The canonical updater adds exactly one Human Index and one Machine Mirror row for the new primary and schema, produces their sibling path proofs, and refreshes `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl.sha256`, and required index/mirror path proofs in the same PR.
- No manual companion writes are allowed.
- The release stage formerly named `DB-bridge parity` becomes `Direct DB selection contract` and requires the new primary `PASS`.
- A separate stage named `Historical bridge evidence integrity` checks retained bytes without a current bridge PASS claim.

- **Compatibility/migration:** direct switch in PR-06R-B after OPS-03 is present. No dual-current bridge/direct default. Historical rows remain queryable by their existing keys/paths but have historical record meaning.
- **Validation/evidence:** schema mutation tests, case mutation tests, canonical bytes, secret scan, exact updater cardinality, historical hash stability, release-stage semantic tests.
- **Rollback:** revert the new primary/schema and updater-generated companions as a unit; retain historical primaries and fail release admission. Never restore current bridge meaning.
- **Downstream effect:** supplies Repo-local selection/refusal proof for `.4` and redefined `.9`; live posture remains OPS-03.
- **Plan consequence:** PR-06R-A produces local artifact/tooling; PR-06R-B owns final tracked bytes and binding.
- **Documentation consequence:** PF12 §8.7 drainage through `ADR-CANON-006`.
- **Nonclaims:** fixture/local evidence is not live DB proof, Railway proof, QA PASS, token satisfaction, or PF09 movement.

### RSC-004 — OPS-03 direct PostgreSQL read-only posture packet

- **Requested addition:** one separately authorized, direct-only, read-only OPS capture after PR-06R-A merge.
- **Canon effect:** `EXTENDS` through `ADR-CANON-007`.
- **Linked cause:** `CAUSE-005`.
- **Reason required now:** current live DB posture cannot be inferred from Repo-local fixtures, and the old bridge packet cannot be repurposed.
- **Exact proposed implementation loci:** `scripts/ops/hde_epic038_ops03.py`; `tools/evidence/hde_epic038_ops03.py`; the schema paths below; focused tests under `tests/ops/` and `tests/evidence/`.
- **Operational target:** the HDE database reachable only through operator-supplied `DATABASE_URL`, `APP_ENV=dev`, schema `hde`, search path `hde, public`; no Railway CLI or bridge target.

#### Proposed CRD decision — authorization and launch boundary

The PO-approved authorization is canonical JSON with schema `hde_epic038.ops03.authorization.v1`, validated by `schemas/hde_epic038_ops03_authorization.v1.json`. It has exactly: `schema`, `run_id`, `authorized_at_utc`, `expires_at_utc`, `source_commit`, `runner_sha256`, `validator_sha256`, `interpreter`, `target`, `rails`, `retired_keys_required_absent`, `ordered_query_ids`, `expected_counts`, `candidate_root`, `exact_argv`, and `one_attempt`.

- `run_id` matches `^[a-z0-9][a-z0-9-]{15,63}$` and determines exact derived paths: run root `/tmp/hde-epic038-ops03/<run_id>/`; control root `/tmp/hde-epic038-ops03/<run_id>/control/`; candidate root `/tmp/hde-epic038-ops03/<run_id>/candidate/`; failure root `/tmp/hde-epic038-ops03/<run_id>/failure/`. `<run_id>` here denotes exact string concatenation of the validated field, not an unresolved operator substitution.
- `interpreter` has exactly `{resolved_path,sha256}`.
- `target` is exactly `{app_env:'dev',database_schema:'hde',search_path:['hde','public']}` and contains no host, DSN, password, or role value.
- `rails` is exactly `{safe_mode:'1',allow_network:'0',allow_db_write:'0',db_read_authorized:true}`. `ALLOW_NETWORK=0` forbids general HTTP/vendor/CLI network activity; `db_read_authorized` is the sole narrow exception for the one bound direct PostgreSQL provider path and never authorizes another target, provider, protocol, retry, or write.
- `retired_keys_required_absent` is the exact retired-key roster.
- `ordered_query_ids` is exactly: `set_transaction_read_only`, `set_search_path`, `connection_identity`, `search_path`, `runtime_role_grants`, `ddl_columns`, `ddl_constraints`, `boundary_views`, `partition_inventory`, `partition_verify`.
- `expected_counts` is exactly `{provider_selections:1,health_connections:1,health_sql_statements:1,posture_transactions:1,posture_sql_statements:10,direct_connections:2,sql_statements:11,sql_writes:0,retries:0,alternate_provider_attempts:0}`. The health statement is the existing exact `SELECT 1`; the ten posture statements are the ordered query roster.
- `candidate_root` must equal the exact derived candidate path above; it is not a Repo path.
- `exact_argv` binds three vectors in order: capture producer, receipt-emitting independent validator, and final read-only validator. Every Python vector uses the same resolved interpreter followed by exact `-I`, `-B`, the bound script path, and its bound mode/authorization/candidate arguments.
- `one_attempt` is literal `true`. A launch marker is written before provider selection. Any post-marker failure consumes this authorization; no retry occurs under the same bytes.

The runner starts from a clean child environment containing only the required locale/rails names, `APP_ENV`, and `DATABASE_URL`; no `PYTHON*` name is forwarded. The `DATABASE_URL` value is available only to the child provider and is never serialized. The runner verifies full source-manifest equality and no `__pycache__`/`.pyc` residue before and after capture. Writes are limited to the exact derived control, candidate, and failure roots. The launch marker and authorization-consumption record are control-root files; success primaries are candidate-root files; a failure receipt is a failure-root file. No source or Repo write is authorized.

#### Proposed CRD decision — read-only observation

The runner uses `DBAccess.for_current_env` once. Its existing health operation opens one direct connection and executes exactly `SELECT 1`. It then calls the proposed `DBAccess.readonly_tx` once with the exact ordered ten-statement posture roster. `set_transaction_read_only` is first and must succeed before every observation; `set_search_path` is second. The remaining eight statements are read-only `SHOW`/`SELECT` observations corresponding one-to-one to their query IDs, and the connection-identity observation includes `current_setting('transaction_read_only')` so the emitted predicate is observed rather than inferred. The provider never commits and rolls back in `finally` even on success. Static SQL classification and provider-level read-only enforcement both reject mutating SQL. Any statement beyond the one fixed health statement and ten fixed posture statements, or any extra connection, provider attempt, retry, or transaction, is a failure.

#### Proposed CRD decision — packet inventory and ownership

The candidate success root contains exactly these ten primaries; updater-owned companions are added only during PR-06R-B:

| Primary | Artifact key | Record type | Sole producer |
|---|---|---|---|
| `commands.txt` | `epic038.ops03.commands` | `epic038_ops03_text` | `scripts/ops/hde_epic038_ops03.py` |
| `stdout.log` | `epic038.ops03.stdout` | `epic038_ops03_log` | `scripts/ops/hde_epic038_ops03.py` |
| `stderr.log` | `epic038.ops03.stderr` | `epic038_ops03_log` | `scripts/ops/hde_epic038_ops03.py` |
| `exit_code.txt` | `epic038.ops03.exit_code` | `epic038_ops03_text` | `scripts/ops/hde_epic038_ops03.py` |
| `env_presence.json` | `epic038.ops03.env_presence` | `epic038_ops03_env_presence` | `scripts/ops/hde_epic038_ops03.py` |
| `db_posture_summary.json` | `epic038.ops03.db_posture_summary` | `epic038_ops03_db_posture` | `scripts/ops/hde_epic038_ops03.py` |
| `nonclaims.json` | `epic038.ops03.nonclaims` | `epic038_ops03_nonclaims` | `scripts/ops/hde_epic038_ops03.py` |
| `result_summary.json` | `epic038.ops03.result_summary` | `epic038_ops03_result` | `scripts/ops/hde_epic038_ops03.py` |
| `validation_receipt.json` | `epic038.ops03.validation_receipt` | `epic038_ops03_validation` | `tools/evidence/hde_epic038_ops03.py --emit-receipt` |
| `checksums.sha256` | `epic038.ops03.checksums` | `epic038_ops03_checksum` | `scripts/ops/hde_epic038_ops03.py` |

Tracked destination after admission is exactly `audit/ops/hde-epic038/ops-03/` plus each filename. The runner never writes that Repo path. PR-06R-B copies the validated bytes and does not become their producer.

Text contracts are exact:

- `commands.txt` has three LF-terminated lines `capture_argv=`, `receipt_argv=`, and `validate_argv=` followed by canonical JSON argv arrays; no shell interpolation or secret value.
- `stdout.log` and `stderr.log` are UTF-8/LF, secret-scanned, and contain only stable event/result codes. PASS requires empty `stderr.log`.
- `exit_code.txt` is exactly `0` plus LF on candidate success.
- `checksums.sha256` contains one ASCII-sorted `<64-lowercase-hex><two spaces><filename>` line for each of the preceding nine primaries and never lists itself.

JSON contracts are strict/canonical and reject unknown keys at every level:

- `env_presence.json`, schema `hde_epic038.ops03.env_presence.v1`, exact top-level fields `schema`, `run_id`, `app_env`, `rails`, `database_url_presence`, `retired_key_presence`, `determinism_pins`. It records `DATABASE_URL` only as `SET_REDACTED`; every retired key must be `UNSET`; rails and pins must equal authorization.
- `db_posture_summary.json`, schema `hde_epic038.ops03.db_posture_summary.v1`, exact top-level fields `schema`, `run_id`, `source_commit`, `provider`, `selection_attempts`, `ordered_query_ids`, `query_results`, `observations`, `counts`, `predicates`, `result`. Provider is `psycopg`; attempts contain one `ok` row; query IDs and counts equal authorization. Each query result has exactly `{query_id,status,row_count,canonical_sha256}`. Observations have exactly `connection_identity_presence`, `search_path`, `runtime_role_flags`, `ddl_identity`, `constraint_count`, `boundary_views`, `partition_posture`; values are names-only, booleans, counts, or hashes. DDL identity cites `hde.ddl_identity_projection.v1`. Predicates are exactly `authorization_match`, `direct_provider_only`, `read_only_transaction`, `search_path_exact`, `least_privilege_role`, `ddl_identity_valid`, `constraints_observed`, `boundary_views_readonly`, `partition_posture_observed`, `counts_exact`, `secret_values_absent`; all must be true for `PASS`.
- `nonclaims.json`, schema `hde_epic038.ops03.nonclaims.v1`, exact fields `schema`, `run_id`, `nonclaims`. The sorted exact roster is `acceptance_token_satisfaction`, `deployment`, `epic_closeout`, `migration`, `pf09_status_movement`, `production_write_authorization`, `qa_pass`, `railway_inventory_proof`, `retired_transport_availability`.
- `result_summary.json`, schema `hde_epic038.ops03.result_summary.v1`, exact fields `schema`, `run_id`, `source_commit`, `authorization_sha256`, `capture_result`, `decisive_predicates`, `primary_files`, `nonclaims_ref`. `capture_result` is `PASS`; all decisive predicates are true; `primary_files` is exactly `['commands.txt','db_posture_summary.json','env_presence.json','exit_code.txt','nonclaims.json','result_summary.json','stderr.log','stdout.log']` in that ASCII order. It excludes the later validator-owned receipt and final checksum ledger.
- `validation_receipt.json`, schema `hde_epic038.ops03.validation_receipt.v1`, exact fields `schema`, `run_id`, `authorization_sha256`, `validated_files`, `predicates`, `result`. Predicates are exactly `authorization_valid`, `source_identity_valid`, `schemas_valid`, `canonical_bytes_valid`, `inventory_valid`, `counts_valid`, `secret_scan_valid`, `nonclaims_valid`; all true for `PASS`.

Schema paths are exactly `schemas/hde_epic038_ops03_authorization.v1.json`, `schemas/hde_epic038_ops03_env_presence.v1.json`, `schemas/hde_epic038_ops03_db_posture_summary.v1.json`, `schemas/hde_epic038_ops03_nonclaims.v1.json`, `schemas/hde_epic038_ops03_result_summary.v1.json`, `schemas/hde_epic038_ops03_validation_receipt.v1.json`, and `schemas/hde_epic038_ops03_failure_receipt.v1.json`. Each tracked schema is indexed with key `epic038.ops03.schema.<basename-without-extension>` and record type `epic038_ops03_schema`.

#### Negative receipt and failure boundary

On pre-marker or post-marker failure, the runner emits exactly `/tmp/hde-epic038-ops03/<run_id>/failure/failure_receipt.json`; pre-marker failure performs no external DB operation, while post-marker failure also records the consumed authorization in the control root and stops. Schema is `hde_epic038.ops03.failure_receipt.v1` with exact fields `schema`, `run_id`, `authorization_sha256`, `phase`, `code`, `launch_consumed`, `candidate_admissible`, and `nonclaims`; `candidate_admissible` is always false. It contains no traceback, exception message, query rows, DSN, host, role name, or secret. Failure receipts are diagnostic, not copied to the success root, not indexed, and never transformed into PASS. A new attempt requires a new PO-approved authorization.

#### Validation, migration, rollback, and boundaries

- **Validation:** independent authorization validation precedes marker creation; receipt validation precedes checksum creation; final packet validation is read-only; PR-06R-B repeats validation before and after copy; mutation tests cover every field, count, path, argv, source hash, canonical byte, checksum, secret marker, SQL class, and extra-file case.
- **Updater-owned companions:** PR-06R-B creates sibling path proofs for all ten primaries and seven schemas, then refreshes Human Index, Machine Mirror, checksums, and their path proofs through `update_evidence_index.py` only.
- **Compatibility/migration:** new family only; no field or version inheritance from OPS-01/OPS-01R.
- **Rollback:** an OPS failure produces no tracked evidence and blocks PR-06R-B. A PR-B validation failure removes the staged copy from that proposed change before commit; no old packet is changed.
- **Downstream effect:** direct live support for `.4` and redefined `.9`; no QA or status effect by itself.
- **Plan consequence:** replace OPS-01R with OPS-03 after PR-06R-A and before PR-06R-B.
- **Documentation consequence:** PF12 permanent drainage under `ADR-CANON-007`.
- **Nonclaims:** no Railway inventory proof, DB writes, service mutation, deploy, QA PASS, token claim, PF09 movement, or closeout.

### RSC-005 — Atomic PR-06R-B release integration and PF09 supportability

- **Requested addition:** one final integration slice that consumes the exact direct-only implementation and OPS-03 packet, then closes the evidence graph required for later PF09 decisions.
- **Canon effect:** `AMENDS` through `ADR-CANON-008`; otherwise follows existing Index/Mirror and release discipline.
- **Linked causes:** `CAUSE-002`, `CAUSE-003`, `CAUSE-005`.
- **Reason required now:** source cleanup and an external packet are individually insufficient; the canonical release log, artifact bindings, historical semantics, and row-specific predicates must converge atomically.
- **Exact existing loci:** `tools/evidence/run_sanity_pipeline.py`; `tools/evidence/run_sanity_pipeline_gate.py`; `tools/evidence/update_evidence_index.py`; `tools/evidence/orientation_demo.py`; `tools/evidence/validate_evidence_paths.py`; current mirror/hash/final-LF checks; `tests/evidence/test_hde_epic038_release_sanity.py`.

#### Proposed CRD decision — final stage order

The canonical pipeline at `audit/gates/sanity_pipeline/sanity_pipeline.log` uses this exact ordered stage roster:

1. Environment pins.
2. Identity and release provenance.
3. Canonical JSON.
4. Reader/CLI, AB/BA, two-run, and preimage determinism.
5. A7 Catalog transport.
6. CI rails.
7. Direct DB selection contract.
8. Direct DB posture artifacts.
9. BodyGraph policy.
10. Architecture snapshot.
11. Configured-v2 mapped-cache local evidence.
12. Historical bridge evidence integrity.
13. OPS-02 mapped-cache packet validation.
14. OPS-03 direct DB posture packet validation.
15. Human Index and Machine Mirror refresh.
16. Evidence-path validation.
17. Mirror schema and index/mirror hash validation.
18. Topology orientation validation.
19. Final-LF validation.

Stage 12 may report only `HISTORICAL_INTEGRITY_OK`; it cannot report bridge availability, parity, capability, consistency, fallback, or current OPS PASS. Stage 14 is mandatory for final PASS. The pipeline stops at the first failure, has no required-stage skip, does not perform external I/O, and does not rerun OPS.

#### Proposed CRD decision — updater and release binding

- Replace current bridge rows used for release admission with the new local direct-selection primary and OPS-03 packet rows.
- Preserve old OPS-01 and bridge artifact bindings under historical record types/notes; retain their existing keys and paths where changing keys would break history.
- Preserve OPS-02 as current bounded support for `.11`; do not rerun it.
- Copy OPS-03 candidate bytes exactly, verify its external checksum ledger, invoke the canonical updater once after all primaries/schemas are final, regenerate orientation after the full evidence skeleton, and run all checks.
- A failed validator or updater produces no partial final commit. There is no hand-edited Index, Mirror, checksum, or path proof.

#### Proposed CRD decision — later PF09 support posture

PR-06R-B may state only `Supportable from repo evidence` when every row predicate in §9 is satisfied. It does not edit PF09. The intended later status actions are `.4 Partial -> Done`, `.6 Partial -> Done`, redefined `.9 Partial -> Done`, `.11 Optional -> Done`, and `.5.2 Partial -> Done` for the HDE-EPIC038 slice. These are recommendations for a separate PF09 maintenance action, not CRD or PR effects. Failure of any row-specific predicate leaves that row unchanged without blocking truthful support for an independently complete row.

- **Contract impact:** changes release stage semantics, current evidence bindings, and the proposed `.9` meaning; no public or durable-payload change.
- **Compatibility/migration:** one atomic switch after OPS-03; no permanent dual-current evidence family.
- **Validation/evidence:** full stage tests, historical/current semantic tests, packet validators, updater cardinality, exact path proofs, mirror schema/hash, Index hash, orientation, final LF, and row crosswalk.
- **Rollback:** revert PR-06R-B's new primary/schema copies and generated companions as one unit; retain PR-06R-A direct-only runtime and fail release closed. Never restore bridge selection.
- **Downstream effect:** supplies evidence for later PF09 review; QA, acceptance, PF documentation, and closeout remain separate.
- **Plan consequence:** replaces obsolete bridge-dependent PR-C and original PR-06 finalization clauses with PR-06R-B.
- **Documentation consequence:** permanent PF09.6 drainage plus r6-lineage plan revision; PF10 needs no further exact-topic decision to authorize the design.
- **Nonclaims:** no implementation performed here, no OPS executed here, no QA PASS, token satisfaction, PF09 movement, deployment, or closeout.

## 8. Ownership and Boundary Effects

### Work and ownership disposition

| Boundary | Exact disposition | Owner after IA approval and later plan authorization | Reopened or closed by this CRD |
|---|---|---|---|
| Direct-only runtime convergence | Moved into the current remediation as `PR-06R-A`; includes the primary façade, compatibility resolver, retired-key refusal, active bridge-surface removal, transport-neutral mapped-cache guards, new local evidence tooling, and OPS-03 tooling. | Implementation Agent for the separately authorized `PR-06R-A` implementation slice. | No. This CRD proposes scope only. |
| Direct live posture | Replaces OPS-01R with the separately authorized `OPS-03` one-attempt, read-only direct PostgreSQL capture. | PO-authorized OPS executor using the merged PR-06R-A runner; independent validator owns admission. | No. OPS is not executed here. |
| Final evidence and release integration | Moved into `PR-06R-B`; exact packet copy, current/historical binding split, canonical updater, final pipeline, and PF09 support crosswalk are atomic. | Implementation Agent for the separately authorized `PR-06R-B` integration slice. | No. |
| `BUG-001` acceptance-path repair | Retained exactly as current Repo state. | Existing EPIC024 evidence owners. | No; EPIC024 is not reopened. |
| `BUG-002` retained-evidence scanner repair | Retained exactly as current Repo state and used by the new evidence families. | `tools/evidence/retained_evidence_safety.py` and its existing consumers. | No. |
| `BUG-003` pure DDL identity projection | Retained under the non-transport portion of `ADR-CANON-004`. | `engine/db/ddl_identity_projection.py`; current producer and validator consumers. | No. Bridge-dependent v5 use is superseded. |
| OPS-01 | Reused only as immutable historical evidence with historical-integrity validation. No rerun, rewrite, reapproval, or current PASS semantics. | Original producer provenance remains historical; updater owns only classification/binding metadata. | No. |
| OPS-01R failed/ineligible attempt | Retained only as a failure/decision-support record outside the current governed PASS family. | Historical diagnostic owner. | No retry and no relabeling. |
| OPS-02 | Reused without rerun as the existing bounded live support for `.11`; its validators become compatible with direct-only source. | Existing OPS-02 producer provenance; PR-06R-B validator and updater consumers. | No. |
| PF09, PF-Canon, plan, QA, acceptance, board, and closeout work | Retained downstream. | Their existing human/process owners under separate authorization. | No status, document, token, QA, or closeout effect. |

### Producer and consumer ownership changes

| Artifact or contract | Sole producer after the proposed cutover | Consumers after the proposed cutover | Historical treatment |
|---|---|---|---|
| Runtime provider selection | `engine.db.adapter.DBAccess` | Reader, CLI, HTTP adapter, DB evidence producers, mapped-cache tooling | Bridge provider is not a compatibility producer. |
| `artifacts/runtime/direct_db_selection.snapshot.json` | `tools/evidence/generate_hde_epic038_direct_db_selection.py` | direct contract checker, sanity pipeline, updater, tests | New current primary; no bridge-field inheritance. |
| OPS-03 first eight runner primaries and `checksums.sha256` | `scripts/ops/hde_epic038_ops03.py` | independent validator, PR-06R-B exact-copy admission, updater, sanity pipeline | New current packet only. |
| OPS-03 `validation_receipt.json` | `tools/evidence/hde_epic038_ops03.py --emit-receipt` | final read-only validator, updater, sanity pipeline | New current packet only. |
| Human Evidence Index, Machine Mirror, sibling path proofs, index/mirror hashes | `tools/evidence/update_evidence_index.py` | release validation, auditors, later PF09 maintenance | Current and historical records coexist with distinct record meanings; no hand edits. |
| Architecture orientation | `tools/evidence/orientation_demo.py` | release validation and reviewers | Regenerated after the final evidence skeleton; it does not produce primaries. |
| `artifacts/db_bridge/**`, bridge-era env-connectivity evidence, OPS-01 primaries | Original historical producers; no current producer | historical-integrity stage, updater historical bindings, auditors | Primary bytes and their primary checksum ledgers are frozen. |

### Current and downstream boundaries

- **Moved into the current remediation:** only work needed to eliminate executable bridge behavior, establish direct-only local/live evidence, and bind that evidence into the final release graph.
- **Retained in the current remediation:** existing direct provider behavior, DDL identity projection, BodyGraph/Reader/CLI contracts, mapped-cache semantics, OPS-02 primaries, evidence updater discipline, path proofs, mirror/hash validation, topology, and final-LF checks.
- **Historical work reused without reopening:** merged PR 359 facts, OPS-01 bytes, OPS-01R failure classification, OPS-02 execution, EPIC024 evidence, and all earlier successful non-bridge remediation.
- **Downstream work retained elsewhere:** permanent plan revision, PF07/PF09.6/PF12/PF14/PF04 drainage, QA, acceptance-token review, board changes, deployment, migration, slice closeout, and epic closeout.
- **Evidence maintenance boundary:** an updater metadata change may distinguish historical from current rows, but it may not rewrite the facts, status, producer identity, or checksum meaning of a historical primary.

### PF09 status posture

The current statuses remain exactly `HDE-DIST001.4 Partial`, `HDE-DIST001.6 Partial`, `HDE-DIST001.9 Partial`, `HDE-DIST001.11 Optional`, and `HDE-DIST005.2 Partial`. IA approval, plan revision, source implementation, OPS-03 execution, or PR-06R-B integration alone does not move a row. PR-06R-B may produce a row-specific `Supportable from repo evidence` recommendation only when the exact predicates in §9 are all proven for that row. A later authorized PF09 maintenance action decides and records any status change.

Evidence pointer: PF09.6 - Canon HDE Build Checklist Distillation | complete rows `HDE-DIST001.4`, `.6`, `.9`, `.11`, and `HDE-DIST005.2` | observed statuses are `Partial`, `Partial`, `Partial`, `Optional`, and `Partial`.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `PF09 consequences` | the affected rows remain pending implementation, evidence, and permanent documentation drainage; the addendum does not itself move status.

### Prohibited completion claims

No owner may treat this CRD as proof of implementation, current external DB state, Railway inventory, OPS success, QA PASS, acceptance, token satisfaction, PF09 movement, deployment, migration, slice completion, epic completion, or closeout.

## 9. Implementation Requirements and Plan Consequences

### Source-grounded technical requirements

1. **One active transport:** every executable HDE DB path selects only `PsycopgProvider` through `engine.db.adapter.DBAccess`; no active import, registry entry, HTTP bridge request, fallback branch, or bridge execution command remains.
2. **Strict retired-key refusal:** membership of any retired key, including an empty-valued key, fails before the `DATABASE_URL` value is read, before provider construction, and before external I/O; reports include names only.
3. **One selection owner:** `adapter/db_access.py` delegates to the primary façade and cannot implement a second transport policy.
4. **No runtime evidence side effect:** runtime provider selection returns a pure secret-free evidence object when asked but never writes a governed file.
5. **Preserved external behavior:** Reader/CLI bytes, BodyGraph semantics, schema `hde`, DDL identity projection, write rails, mapped-cache durable payloads, and direct provider operations remain unchanged except for the intentional retired-key refusal.
6. **Separate current evidence identity:** direct-only selection evidence uses the exact v1 schema/path/key/producer in `RSC-003`; current PASS logic never consumes a bridge success field.
7. **Historical evidence integrity:** old bridge and OPS-01 primaries remain byte-stable and are checked only for integrity, provenance, secret safety, and historical nonclaims.
8. **Immutable capture source:** OPS-03 executes only after PR-06R-A is merged, with authorization bound to the exact commit, interpreter, runner, validator, argv vectors, query roster, counts, candidate root, and one-attempt rule.
9. **Read-only external action:** OPS-03 issues only the existing fixed health statement `SELECT 1` plus the authorized ten-statement posture roster, sets transaction read-only first within the posture transaction, rolls that transaction back, performs no retry, and writes only the authorized temporary packet/control locations.
10. **Independent admission:** the validator, not the runner, owns `validation_receipt.json`; PR-06R-B validates the source packet before and after exact copy.
11. **Atomic governed integration:** all new primaries and schemas exist before the updater runs once; the updater alone writes Index, Mirror, path proofs, and their hashes; orientation follows the complete evidence skeleton.
12. **Fail-closed release:** every mandatory stage is unskippable, stops on first failure, performs no OPS or external I/O, and cannot convert a negative receipt or historical bridge packet into current PASS.

### Plan-consequence matrix

The current `r1` Epic Plan remains the approved epic-scope baseline. The current `r6` Implementation Plan is the execution baseline whose bridge-dependent clauses require a separately authorized next-version revision. This matrix states what that revision must incorporate; it is not the revision itself.

| Affected deliverable / PF09 row | Current owner and status | Current r6 baseline | Proposed CRD decision and affected components | Evidence and validation change | Dependency/order change | Retained owner and exclusions |
|---|---|---|---|---|---|---|
| D8 / `HDE-DIST001.4` DB/runtime posture — `Partial` | PR-04 / OPS-01 / PR-06 | direct and bridge posture, grants, schema, and final binding | PR-06R-A removes bridge and produces local direct-selection/posture; OPS-03 supplies read-only live direct posture; PR-06R-B binds it | require `direct_db_selection` PASS, direct posture artifacts, OPS-03 PASS, retired-key refusal, grants/schema/views/partition predicates | retained PR-04 evidence → PR-06R-A → OPS-03 → PR-06R-B | DB migration, DB writes, Railway inventory, QA, and PF09 update excluded |
| D10 / `HDE-DIST001.9` DB–bridge parity — `Partial` | PR-04 / OPS-01 / PR-06 | live direct/bridge BodyGraph parity and bridge fallback proof | redefine the row for this slice as direct DB connectivity and retired-transport enforcement; preserve projection-only DDL truth | remove bridge comparison; require local direct cases, OPS-03 direct posture, zero alternate attempts, retired-key pre-I/O refusal, DDL projection validity | replace OPS-01/OPS-01R with PR-06R-A → OPS-03 → PR-06R-B | historical OPS-01 retained; no bridge reconstruction or current parity claim |
| D13 / `HDE-DIST001.6` one-button release — `Partial` | PR-06 | bridge stage, OPS-01/OPS-02 validation, updater and final release binding | PR-06R-B owns the exact 19-stage direct-only pipeline and current/historical semantic split | add direct-selection and OPS-03 validators; change bridge stage to historical integrity; retain OPS-02; require updater/path/mirror/hash/topology/LF checks | final integration only after validated OPS-03 packet | pipeline performs no external calls, OPS reruns, QA, deployment, or PF updates |
| D12 / `HDE-DIST001.11` mapped cache — `Optional` | PR-05 / OPS-02 / PR-06 | configured-v2 local and live mapped-cache evidence | preserve semantics and OPS-02; PR-06R-A makes no-I/O guards transport-neutral; PR-06R-B validates and binds existing packet | existing `.11` predicates remain exact; add no-retired-module-import assertion; no OPS-02 rerun | PR-05/OPS-02 retained → narrow PR-06R-A compatibility → PR-06R-B validation | no cache schema/payload redesign, provider dependency, or historical execution change |
| D1 / `HDE-DIST005.2` Index/Mirror discipline — `Partial` | PR-01 / PR-06 | same-change updater, path proof, checksums, mirror/index coherence | updater adds new direct/OPS-03 primaries and schemas, converts old current bridge bindings to explicit historical meaning, and refreshes all companions atomically | exact one-row-per-path cardinality; schema/canonical/path/hash validation; frozen historical primary hashes; no orphan/duplicate records | all primaries/schemas final → updater once → orientation → validation → final LF | updater remains sole companion owner; manual edits and partial generated sets excluded |

Evidence pointer: Implementation Plan | D8, D10, D12, D13, D1, PR-06, OPS-01, and OPS-02 units | current owners combine PR-06 with bridge-dependent OPS-01 and retained OPS-02; all mapped rows are intended to complete in this epic.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `HDE-EPIC038 and OPS-01R disposition` | OPS-01R and the bridge-dependent PR-C lane are retired; any direct-only replacement requires a separately specified contract.

### Dependency and adoption order

1. IA technically approves this CRD or returns it for revision.
2. The PO separately authorizes and approves an r6-lineage plan revision incorporating this matrix, exact PR-06R-A → OPS-03 → PR-06R-B boundaries, and the permanent drainage tasks.
3. PR-06R-A implements and validates the direct-only source, local evidence contract, OPS-03 tooling, schemas, and tests. It does not include live OPS-03 bytes or final support claims.
4. PR-06R-A is reviewed, merged, and fixed by exact source commit.
5. The PO supplies and approves the exact canonical OPS-03 authorization bytes for that commit and target.
6. OPS-03 executes once. Its independent validator emits the success receipt only if every authorization, source, rail, query, count, secret, schema, canonicalization, checksum, and nonclaim predicate passes.
7. PR-06R-B admits the exact candidate bytes, generates the local direct artifact and current posture artifacts at their final schemas, and finalizes all primaries.
8. The canonical updater runs once; orientation then regenerates; the full 19-stage pipeline and focused tests validate the complete graph.
9. Only after PR-06R-B is merged may a separate reviewer recommend row-specific `Supportable from repo evidence` outcomes and a separate PF maintainer drain plan/canon/status wording.

### Validation and evidence-generation order

1. Static active-source/guidance scan and dependency/import validation.
2. Runtime unit tests for direct selection, retired-key refusal, typed failures, one attempt, and absence of alternate I/O.
3. Consumer compatibility and mapped-cache no-I/O regression tests.
4. Direct-selection schema and producer mutation tests; canonical local primary generation.
5. OPS-03 authorization/runner/validator unit and mutation tests using fixtures only; no external call in PR validation.
6. PR-06R-A full applicable CI and immutable merge.
7. OPS-03 source/authorization validation, read-only capture, receipt emission, checksum finalization, and final candidate validation.
8. PR-06R-B pre-copy packet validation and exact byte/checksum comparison after copy.
9. Final generation of non-OPS current primaries and architecture snapshot.
10. One canonical updater invocation for all primary/schema bindings and companions.
11. Orientation generation after the evidence skeleton is complete.
12. Exact 19-stage release pipeline, focused release tests, path checks, mirror/index hashes, secret/raw-marker safety, topology, and final LF.

### Row-specific supportability predicates

| PF09 row | Every predicate required before `Supportable from repo evidence` may be stated |
|---|---|
| `HDE-DIST001.4` | active-source scan has no executable bridge path; retired keys fail before provider/I/O; direct-selection primary is `PASS`; direct DB posture primaries are current and schema-valid; OPS-03 is `PASS`; runtime grants, search path, DDL/constraint, boundary-view, and partition observations satisfy their current predicates; secrets are absent; all paths are indexed and mergeable. |
| `HDE-DIST001.6` | the exact 19 mandatory stages run in order from the canonical entrypoint; none is skipped; each reports its expected success code; the pipeline performs no OPS/external I/O; current and historical semantics are distinct; canonical JSON, determinism, rails, updater, path, mirror/hash, topology, and LF gates all pass. |
| `HDE-DIST001.9` | the row wording has been adopted as direct connectivity and retired-transport enforcement; healthy direct selection succeeds through `psycopg`; missing/unavailable direct fails closed; every retired key, including empty value, refuses before provider attempt; alternate attempts are zero; OPS-03 proves direct read-only posture; DDL comparison claims only the v1 projection; no current bridge parity/fallback claim remains. |
| `HDE-DIST001.11` | existing local mapped-cache and OPS-02 packet validators pass; write/read-back, idempotence, closed-rails refusal, no raw vendor persistence, and secret safety remain proven; the local generator imports no retired provider and performs no live provider/vendor I/O; current bindings remain complete. |
| `HDE-DIST005.2` | every new primary and schema has exactly one Human Index row, one Machine Mirror row, correct sibling path proof, correct checksum/hash linkage, and authorized record meaning; historical primaries retain exact checksums; there are no duplicates, orphans, manual companions, ignored required files, or path/schema/hash failures; updater and orientation order is proven. |

### Updater ownership and release-binding order

- Primary producers finish first and do not write Index, Mirror, path proofs, or index/mirror hashes.
- `tools/evidence/update_evidence_index.py` is the sole companion writer and runs once against the final inventory.
- It records new direct and OPS-03 rows as current, OPS-02 rows as retained current support for `.11`, and OPS-01/bridge rows as historical only.
- `tools/evidence/orientation_demo.py` runs only after the updater has created the final evidence graph.
- Release validation reads all resulting bytes; it never regenerates OPS material and never repairs an inconsistent graph.

### Rollback stops

- **PR-06R-A stop:** any active bridge reference, compatibility ambiguity, public-byte regression, retired-key value leak, provider call on refusal, or mapped-cache regression blocks merge. Operational rollback may disable DB entrypoints or revert to a direct-only commit; it may not restore bridge selection.
- **OPS-03 stop:** any authorization/source/rail mismatch before launch produces no DB call. Any post-marker error consumes the authorization, creates only a temporary inadmissible failure receipt, and requires new PO-approved bytes for another attempt.
- **PR-06R-B stop:** packet mismatch, validator failure, historical-byte change, duplicate/missing binding, updater failure, or release-stage failure blocks the whole integration. Revert the proposed PR-B primary/generated set together; keep PR-06R-A direct-only.
- **PF09 stop:** failure of a row predicate leaves that row's status unchanged and prohibits a supportability claim for that row.

### Exclusions

This rescope excludes bridge recreation, Railway inventory discovery, database mutation or migration, public Reader/CLI redesign, BodyGraph payload changes, mapped-cache schema redesign, OPS-01/OPS-01R/OPS-02 reruns, evidence fabrication or historical-primary rewriting, QA execution, deployment, PF/ADR/plan editing within implementation, PF09 movement, board work, acceptance/token decisions, and closeout.

## 10. PF-Canon, ADR, PF09.x, and PF10 Consequences

### Retained architecture record — `ADR-CANON-004`

The technically approved, implemented portion of `ADR-CANON-004 — Versioned Glow-Owned DDL Identity Projection for OPS Provider Evidence` remains in force only for `engine/db/ddl_identity_projection.py`, schema `hde.ddl_identity_projection.v1`, strict malformed-input rejection, the exact identity projection, and projection-only truth labeling. It does not retain a bridge provider, a direct-versus-bridge packet, OPS-01R, or full-DDL-parity semantics. Those transport/evidence dependencies are superseded by `ADR-CANON-005` through `ADR-CANON-008`. No reapproval or reimplementation of the projector is requested.

Evidence pointer: Repo | `engine/db/ddl_identity_projection.py` | the shared module and `hde.ddl_identity_projection.v1` contract are present at the observed HEAD.

Evidence pointer: Prior CRD lineage | `ADR-CANON-004`, selected bounded rule | `projection_match` proves only the versioned Glow-owned identity projection and does not claim full DDL semantic parity.

### ADR-CANON-005 — Direct PostgreSQL as the Sole Executable HDE Database Transport

**ADR ID:** `ADR-CANON-005`

**Title:** Direct PostgreSQL as the Sole Executable HDE Database Transport

**Status:** `PROPOSED - PENDING IA TECHNICAL APPROVAL`

**Linked IDs:** `BUG-004`, `BUG-005`, `BUG-009`; `CAUSE-001`, `CAUSE-004`; `RSC-002`.

**Canon effect:** `SUPERSEDES`.

**Current PF-Canon contract with exact title and locator:**

- PF07 — Glow Infrastructure, §4.1 `HDE bridge access`, §4.2 `Backend bridge`, §7.0 `Runtime fallback`, §7.1 `Same physical instance: direct or bridge`, §8.1 bridge configuration keys, and §9.2 service catalog currently define or permit `pg-bridge`, `DB_BRIDGE_URL`, or bridge fallback as active infrastructure.
- PF14 — HDE Mechanics Guide, §20.3 `Bridge parity mechanics` and §20.3.1 require an active `BridgeProvider`, bridge generator/checker, provider parity, and OPS closure packet.
- PF10 — HDE Build Notes, §2.12 `pg-bridge and DB_BRIDGE_URL Deprecation and Retirement - Direct PostgreSQL Is the Sole Active HDE Database Transport` explicitly establishes the newer exact-topic rule.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `Decision and effective posture` | "`DATABASE_URL` is the sole canonical HDE database endpoint key." | "Direct PostgreSQL access through the Glow-owned psycopg provider is the sole active HDE database transport."

**Exact rule superseded and remaining boundary:** the active-provider, active-service, runtime-fallback, environment-key, HTTP bridge, and provider-parity rules in the listed PF07/PF14 units are superseded for current HDE execution and current completion evidence. They remain descriptive only for historical artifacts captured while the bridge architecture existed. Their general requirements for explicit environment posture, least privilege, truthful row-level evidence, secret safety, fail-closed behavior, and non-overclaiming remain in force.

**Observed Repo reality:** `engine/db/adapter.py` imports and selects `BridgeProvider`, reads the three retired keys, and writes a bridge-named selection snapshot; `adapter/db_access.py` contains a separate HTTP bridge route; mapped-cache tooling imports bridge code to prove no I/O. Removing the external service did not remove these executable contracts.

**Problem:** two selectable owners can attempt a forbidden transport, revive retired configuration semantics, leak policy divergence, and leave direct-only behavior unprovable. Deleting one module alone breaks dependent tools while leaving the second resolver and current evidence semantics active.

**Alternatives considered:** repair/recreate bridge; leave bridge dormant; remove only `bridge_provider.py`; retain retired keys as ignored compatibility; make the compatibility resolver the owner; or converge on the existing primary façade. The first four preserve or obscure a retired contract, and the fifth duplicates policy. The selected façade convergence is the smallest solution that removes every active selection path without redesigning direct DB operations.

**Selected decision:** `engine.db.adapter.DBAccess` is the sole selection owner; `PsycopgProvider` is the sole provider; retired-key membership fails before provider construction or value access; missing/unavailable direct access fails closed; no fallback, retry, URL inference, or alternate transport exists; and runtime selection performs no governed write.

**Minimum-scope rationale:** the decision changes only HDE transport selection, bridge-dependent compatibility/tooling, and the evidence needed to prove that cutover. It preserves direct PostgreSQL, existing façade operations, public Reader/CLI bytes, BodyGraph semantics, durable payloads, schema ownership, and write rails.

**Exact implementation owner and loci:** PR-06R-A owns `engine/db/adapter.py`, `engine/db/errors.py`, `adapter/db_access.py`, removal of `engine/db/providers/bridge_provider.py`, bridge-dependent script/checker removals, active consumer/import changes, mapped-cache no-I/O guard changes, architecture/env posture producers, guidance, and focused tests.

**Exact API decision:**

- `RETIRED_DB_TRANSPORT_KEYS = ('DB_ALLOW_BRIDGE_IN_PROD', 'DB_BRIDGE_URL', 'DB_FORCE_BRIDGE')`.
- `retired_db_transport_keys_present(environ: Mapping[str, str]) -> tuple[str, ...]` returns sorted names only.
- `RetiredBridgeConfiguration(AdapterError)` has code `retired_bridge_configuration`, `retired_keys`, and the fixed names-only message specified in `RSC-002`.
- `DBAccess.for_current_env(*, environ=None, psycopg_factory=None) -> DBAccess` has no bridge factory or snapshot path.
- `DBAccess.selection_evidence() -> Mapping[str, object]` is pure.
- `DBAccess.readonly_tx(statements: Sequence[Statement]) -> List[Sequence[Any] | None]` and `Provider.readonly_tx` enforce the exact first-statement/read-only/always-rollback contract without changing existing `tx`.
- `adapter/db_access.py` exposes only the direct-only v2 compatibility shapes in `RSC-002`.

**Affected boundaries:** provider selection, retired configuration handling, internal compatibility result shapes, current DB posture producers, mapped-cache safety instrumentation, architecture snapshot, active guidance, tests, and release evidence inputs.

**Unchanged boundaries:** `DATABASE_URL` remains the endpoint name; direct psycopg operations, schema `hde`, DDL projector, Reader/CLI/HTTP presentation contracts, BodyGraph payloads, DB write authorization rails, mapped-cache payloads, evidence updater ownership, QA, tokens, PF09, deployment, and closeout remain unchanged.

**Source-adapter scope:** every current source adapter that reaches HDE DB access must delegate to `DBAccess`; there is no bridge source adapter. Historical parsers may read historical bridge artifacts but cannot create an executable transport.

**Persistence and durable-data effect:** none. Runtime selection writes no evidence. The direct-only local snapshot is produced separately under `ADR-CANON-006`. No database row, schema, migration, BodyGraph, cache payload, or public serialization changes.

**Compatibility:** direct callers retain façade methods. Internal consumers of the old resolver shapes migrate in PR-06R-A. No bridge compatibility shim is allowed. Retired-key presence intentionally changes from selectable/ignored behavior to typed refusal.

**Migration:** add refusal/error/API tests; converge all consumers; introduce the direct checker and evidence producer; remove bridge imports/registrations/generators/runners/checkers; regenerate only current non-historical architecture/posture evidence; freeze bridge primaries; then merge PR-06R-A before OPS-03.

**Producer and consumer ownership:** `DBAccess` owns selection; `PsycopgProvider` owns direct operations; active consumers call the façade; `selection_evidence()` supplies in-memory facts to the dedicated producer; the updater owns no runtime behavior.

**Validation:** exact API tests, empty-valued retired-key tests, factory-not-called assertions, missing/unavailable direct failure cases, one-attempt assertions, no alternate I/O, names-only error/secret scans, consumer regressions, mapped-cache safety, active-source/guidance scan, and architecture/env posture checks.

**Safeguards:** refusal precedes value access; values are never formatted; health failure cannot fall through; no active HTTP bridge module remains; source scan excludes historical/canon paths to avoid rewriting history while still failing on executable current references.

**Rollback or fail-closed posture:** if direct-only source is unsafe, block merge or disable DB entrypoints. Do not operationally roll back by restoring bridge selection, keys, HTTP calls, service dependence, or provider parity.

**Adoption sequence:** IA approval → authorized plan revision → PR-06R-A implementation/review/merge → OPS-03 authorization and execution → PR-06R-B integration → later documentation drainage.

**Plan consequences:** replace bridge implementation and repair work in D8/D10/PR-06 with PR-06R-A; make it the source prerequisite for OPS-03; retain PR-05/OPS-02 and current direct product owners.

**Permanent PF-Canon or ADR drainage:** after implementation evidence exists, update PF07 — Glow Infrastructure §§4.1, 4.2, 7.0, 7.1, 8.1, and 9.2; PF14 — HDE Mechanics Guide §§20.3 and 20.3.1; and PF04 — HDE Governance §2.0 `Acceptance Tokens` where bridge tokens remain active. Drain direct-only runtime first, then evidence and PF09 wording. Preserve general rails, secret safety, least privilege, and historical truth rules.

**Downstream effects:** direct-only OPS and release evidence become possible. The ADR does not prove the live DB, alter QA/acceptance, or move PF09.

**Nonclaims:** no implementation, service deletion proof, external inventory proof, DB migration/write, OPS, QA PASS, token satisfaction, PF09 movement, deployment, acceptance, or closeout.

### ADR-CANON-006 — Direct-Only Selection Evidence and Historical Bridge Quarantine

**ADR ID:** `ADR-CANON-006`

**Title:** Direct-Only Selection Evidence and Historical Bridge Quarantine

**Status:** `PROPOSED - PENDING IA TECHNICAL APPROVAL`

**Linked IDs:** `BUG-006`, `BUG-008`; `CAUSE-002`, `CAUSE-003`; `RSC-003`, `RSC-005`.

**Canon effect:** `SUPERSEDES`.

**Current PF-Canon contract with exact title and locator:** PF12 — HDE Schemas and Artifacts, §8.7 governs the current bridge evidence family, bridge environment connectivity, `db_bridge.adapter_selection.snapshot`, and bridge token posture; §8.6.3.4 governs the canonical sanity, DB/OPS evidence, Human Index, Machine Mirror, checksum, and path-proof family. PF14 — HDE Mechanics Guide §20.3 and §20.3.1 govern direct/bridge parity. PF10 — HDE Build Notes §2.12 now requires a separately named direct-only contract and freezes old bridge artifacts as historical.

Evidence pointer: PF12 - HDE Schemas and Artifacts | §8.7 | the current unit defines `artifacts/db_bridge/**`, bridge adapter selection/environment-connectivity evidence, and `DEV_DB_BRIDGE_FALLBACK_OK` as active evidence identities.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `Evidence and historical-artifact posture` | old OPS-01 and bridge artifacts remain historical and must not be rewritten or presented as current proof; direct-only evidence cannot inherit bridge predicates, fields, or counts.

**Exact rule superseded and remaining boundary:** current release admission and token semantics that require bridge selection, bridge capability, direct/bridge parity, or bridge availability are superseded. Existing bridge primary bytes, producer provenance, checksum identity, and time-of-capture historical meaning remain in force and immutable.

**Observed Repo reality:** current bridge generators can refresh `artifacts/db_bridge/**`; the release pipeline still derives a current bridge PASS; updater constants bind OPS-01 and OPS-02 together as current PR-06 evidence; the runtime façade writes a bridge-named selection snapshot.

**Problem:** a direct-only build needs current selection/refusal proof, but mutating old paths or labels would falsify history; maintaining bridge PASS would make completion impossible; allowing multiple producers or hand-edited companions would make the evidence graph untrusted.

**Alternatives considered:** reuse/rename old bridge artifacts; add direct fields to the old schema; let runtime write the snapshot; treat absence of a bridge URL as PASS; or create a distinct direct-only primary and historical classification. The first four conflate time, owner, or proof meaning. The separate family is minimal and preserves history.

**Selected decision:** create the exact direct-selection family in `RSC-003`; make its dedicated tool sole primary producer; let the canonical updater own companions; freeze historical bridge/OPS-01 primaries; and split release validation into current direct-contract PASS and historical-integrity-only success.

**Minimum-scope rationale:** one six-field primary with four deterministic cases is sufficient to prove direct selection/refusal semantics locally. Live DB posture is deliberately excluded and belongs to OPS-03. Historical rows remain available without supporting current claims.

**Exact implementation owner and locus:** PR-06R-A implements `schemas/hde_epic038_direct_db_selection.v1.json`, `tools/evidence/generate_hde_epic038_direct_db_selection.py`, the direct checker, and tests. PR-06R-B owns final generated primary bytes and the updater/release-binding migration.

**Exact schema/path/key/producer decision:** schema `hde_epic038.direct_db_selection.v1`; schema path `schemas/hde_epic038_direct_db_selection.v1.json`; primary `artifacts/runtime/direct_db_selection.snapshot.json`; key `epic038.pr06r.direct_db_selection`; record type `epic038_pr06r_direct_db_selection`; sole producer `tools/evidence/generate_hde_epic038_direct_db_selection.py`; strict fields/cases/predicates/failure and canonical bytes exactly as specified in `RSC-003`.

**Affected boundaries:** current DB selection evidence, schema registry, release stage names/predicates, Index/Mirror/path proofs/hashes, bridge row classification, current token interpretation, and related tests.

**Unchanged boundaries:** historical primary bytes/checksums/provenance; general canonical JSON, secret safety, Index/Mirror, path-proof, updater, orientation, and final-LF discipline; live DB proof remains outside this artifact.

**Source-adapter scope:** the producer uses injected/fake direct-provider cases and `DBAccess.selection_evidence()` only. It makes no external call and is not a runtime adapter.

**Persistence and durable-data effect:** one Repo-stored JSON primary and one schema plus updater-owned companions. No database, cache, public, or BodyGraph payload change.

**Compatibility:** old keys/paths remain queryable as historical. New current consumers switch atomically to the new key/path. No consumer may interpret a historical row as current PASS.

**Migration:** implement schema/producer/tests; stop active bridge generation; generate the direct primary; admit OPS-03; finalize all primaries/schemas; update historical record meaning and add new current rows in one updater run; regenerate orientation; validate every hash/path/release predicate.

**Producer and consumer ownership:** the direct producer owns only its primary; historical producers retain historical provenance but no current execution ownership; the updater solely owns companions and record classification; sanity/checker/tests consume; no shared primary writer exists.

**Validation:** strict schema and unknown-key mutation tests, exact case roster/order, every decisive predicate, canonical bytes, deterministic two-run identity, negative receipt behavior, secret scan, historical hash stability, one-row cardinality, path proofs, mirror/index hashes, semantic release tests, and no bridge-success claim.

**Safeguards:** names/presence only; no DSN values; strict unknown rejection; runtime has no write side effect; historical integrity is separately named; current and historical record types cannot alias; updater rejects duplicate paths/keys.

**Rollback or fail-closed posture:** revert the new primary/schema and all generated companion changes together; keep historical primaries untouched; release remains failed until a coherent direct graph exists. Never restore current bridge PASS semantics.

**Adoption sequence:** adopt ADR-CANON-005 runtime first; implement local evidence; capture/admit OPS-03; perform the atomic updater/release migration; then drain PF12/PF14/PF04 and PF09 wording.

**Plan consequences:** replace D10 bridge artifacts and OPS-01 current admission; retain D1/D13 updater/release ownership; separate PR-06R-A producer implementation from PR-06R-B final binding.

**Permanent PF-Canon or ADR drainage:** PF12 — HDE Schemas and Artifacts §8.7 for the new family and historical bridge posture; §8.6.3.4 for current DB/OPS bindings and path-proof identities; PF14 — HDE Mechanics Guide §§20.3 and 20.3.1 for removal of bridge-parity mechanics; PF04 — HDE Governance §2.0 `Acceptance Tokens` for retirement of bridge-only token semantics. Preserve canonical evidence, provenance, index/mirror, and secret-safety rules.

**Downstream effects:** later reviewers can distinguish current direct proof from historical bridge evidence; no automatic token or PF09 effect.

**Nonclaims:** local fixtures do not prove external DB availability, Railway inventory, QA PASS, acceptance, token satisfaction, PF09 movement, deployment, migration, or closeout.

### ADR-CANON-007 — Authorization-Bound OPS-03 Direct Read-Only Posture Packet

**ADR ID:** `ADR-CANON-007`

**Title:** Authorization-Bound OPS-03 Direct Read-Only Posture Packet

**Status:** `PROPOSED - PENDING IA TECHNICAL APPROVAL`

**Linked IDs:** `BUG-006`, `BUG-007`, `BUG-008`; `CAUSE-005`; `RSC-004`, `RSC-005`.

**Canon effect:** `EXTENDS`.

**Current PF-Canon contract with exact title and locator:** PF12 — HDE Schemas and Artifacts §8.6.3.4 governs DB/OPS evidence, Index/Mirror, checksums, and path proofs; its current HDE-EPIC038 topic and §8.7 describe the bridge-era packet, not a direct-only read-only packet. PF10 — HDE Build Notes §2.12 permits a separately specified direct-only evidence contract and forbids further OPS-01R/bridge capture.

**Canon-silence search:** searched exact case-sensitive `hde_epic038.ops03`, `hde_epic038_ops03`, `HDE-EPIC038-OPS-03`, and `audit/ops/hde-epic038/ops-03` across current `docs/pfcanon/**` and the current Repo with connected GitHub code search and complete topic-unit reading; result: 0 hits. The search proves absence of these exact identities, not absence of general OPS/evidence rails.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `HDE-EPIC038 and OPS-01R disposition` | no further OPS-01R discovery, retry, or v5 bridge capture is permitted; any direct-only replacement requires a separate contract.

**Observed Repo reality:** OPS-01/OPS-01R code and bindings are bridge-shaped; no current runner, validator, schema, root, or artifact key exists for the proposed OPS-03 identities. General isolated-Python, validator, checksum, Index/Mirror, secret-safety, and path-proof mechanisms are reusable.

**Problem:** Repo-local tests cannot prove current shared DB posture, while the old packet cannot be relabeled and a broad Railway discovery lane does not answer the remaining direct DB question. A live action must be narrowly authorized, deterministic, secret-safe, read-only, independently validated, and provenance-bound.

**Alternatives considered:** no live evidence; reuse OPS-01; repeat OPS-01R; use Railway CLI discovery; allow ad hoc SQL/manual screenshots; or define one direct-only packet. The first is insufficient, the next two violate the retired contract, discovery is irrelevant, and ad hoc evidence lacks deterministic/provenance controls. The exact packet is the minimum coherent extension.

**Selected decision:** create OPS-03 exactly as `RSC-004`: one source-bound authorization, one isolated capture, one direct provider selection, one health connection with the fixed `SELECT 1`, one always-rolled-back read-only posture transaction with ten exact statements, eleven SQL statements total, zero writes/retries/alternate providers, ten exact candidate primaries, independent receipt ownership, and exact tracked admission under `audit/ops/hde-epic038/ops-03/`.

**Minimum-scope rationale:** the query roster captures only the facts needed for `.4` and redefined `.9`: connection identity presence, search path, grants, DDL projection, constraints, boundary views, and partition posture. It excludes Railway inventory, bridge facts, data rows, writes, migration, QA, deployment, and product behavior.

**Exact implementation owner and loci:** PR-06R-A implements `scripts/ops/hde_epic038_ops03.py`, `tools/evidence/hde_epic038_ops03.py`, seven exact schemas, fixture tests, source-manifest/isolation controls, and packet validators. A PO-authorized executor owns the external run. PR-06R-B owns exact byte admission, not production.

**Exact API/schema/path/key/producer decision:** authorization schema, run-root derivation, exact argv, rails, expected counts, ordered query IDs, ten primary filenames/keys/record types/producers, seven schema paths, failure receipt, candidate root, and tracked root are exactly those in `RSC-004`; no unspecified field or file is permitted.

**Affected boundaries:** external read authority, source identity, temporary write contract, OPS packet schemas, evidence inventory, Index/Mirror rows, release validator, and later `.4`/`.9` support.

**Unchanged boundaries:** database write rails, data/schema migration, public behavior, Railway service/variable inventory, OPS-02, historical OPS-01, QA, acceptance, tokens, PF09 status, deployment, and closeout.

**Source-adapter scope:** only the merged direct-only `DBAccess`/`PsycopgProvider` path may be used. No CLI/provider discovery, bridge module, HTTP/vendor adapter, alternate DSN source, or retry adapter is permitted.

**Persistence and durable-data effect:** the DB transaction is read-only and rolled back. OPS persistence is limited to temporary control/candidate/failure locations and, after independent admission, the exact Repo-stored packet plus updater companions. No durable DB payload changes.

**Compatibility:** OPS-03 is a new family. It neither upgrades nor aliases OPS-01/OPS-01R. Validators reject old fields, extra files, alternate counts, or inherited bridge semantics.

**Migration:** merge immutable tooling; approve exact authorization; execute once; emit/validate/checksum the candidate; admit exact bytes in PR-06R-B; generate companions; switch release binding. There is no dual-current packet or field migration.

**Producer and consumer ownership:** the runner owns nine named primaries; the independent validator owns only `validation_receipt.json`; the updater owns companions; PR-06R-B copies bytes; sanity and later reviewers consume. Candidate and tracked copies must hash-identically.

**Validation:** authorization schema/hash/expiry/source/interpreter/argv/path validation; pre/post source manifest and bytecode-cache scans; retired-key absence; clean environment; static/runtime read-only SQL checks; exact connection/transaction/query counts; secret/raw-marker scans; strict/canonical schemas; exact inventory/checksums; independent receipt; pre/post-copy validation; mutation tests.

**Safeguards:** no DSN or value serialization; key names/presence only; `-I -B`; no `PYTHON*`; launch consumption; one attempt; no retry; transaction read-only before observation; rollback on success/failure; exact write roots; failure receipt is inadmissible and unindexed.

**Rollback or fail-closed posture:** pre-marker mismatch causes no DB call. Post-marker failure consumes authorization and yields no admissible packet. OPS failure blocks PR-06R-B. A copied packet that fails validation is removed from the proposed change and never indexed; existing historical evidence remains untouched.

**Adoption sequence:** ADR-CANON-005 and PR-06R-A first; exact PO authorization second; OPS-03 third; ADR-CANON-006/008 PR-06R-B integration fourth; PF drainage/status review later.

**Plan consequences:** replace OPS-01R and bridge-dependent OPS-01 completion ownership with OPS-03 between PR-06R-A and PR-06R-B; include exact artifact roster, authorization gate, one-attempt failure posture, and nonclaims.

**Permanent PF-Canon or ADR drainage:** PF12 — HDE Schemas and Artifacts §8.6.3.4 and §8.7 must register the OPS-03 schemas, root, keys, producers, companions, validation, and relation to historical OPS-01. PF04 — HDE Governance §2.0 `Acceptance Tokens` requires no new OPS-03 acceptance token; any bridge-only token is retired through ADR-CANON-006. PF10 §2.11's task-specific PO delegation and the existing general authorization, secret-safe, read-only, no-overclaim, and acceptance-separation rails remain unchanged.

**Downstream effects:** supplies live direct posture for later `.4`/`.9` review. It does not support `.11` in place of OPS-02 and cannot prove QA, tokens, or closeout.

**Nonclaims:** no OPS execution in this CRD, no Railway inventory, bridge availability, DB write, migration, deployment, QA PASS, acceptance, token satisfaction, PF09 movement, slice completion, epic completion, or closeout.

### ADR-CANON-008 — Direct-Only PF09.6 Completion Semantics and PR-06R Ownership

**ADR ID:** `ADR-CANON-008`

**Title:** Direct-Only PF09.6 Completion Semantics and PR-06R Ownership

**Status:** `PROPOSED - PENDING IA TECHNICAL APPROVAL`

**Linked IDs:** `BUG-007`, `BUG-008`; `CAUSE-003`, `CAUSE-005`; `RSC-005` and the plan consequences of `RSC-002` through `RSC-004`.

**Canon effect:** `AMENDS`.

**Current PF-Canon contract with exact title and locator:** PF09.6 — Canon HDE Build Checklist Distillation, row `HDE-DIST001.4` places bridge fallback/provider parity in the DB semantic home; row `HDE-DIST001.9` is titled `DB–bridge parity & env connectivity` and requires direct-versus-bridge BodyGraph parity; rows `HDE-DIST001.6`, `.11`, and `HDE-DIST005.2` govern release sanity, mapped cache, and Index/Mirror discipline. PF10 — HDE Build Notes §2.12 retires the bridge-dependent portions while leaving permanent PF09 redefinition pending.

Evidence pointer: PF09.6 - Canon HDE Build Checklist Distillation | `HDE-DIST001.9` complete row | current completion language requires direct/bridge BodyGraph parity and current status is `Partial`.

Evidence pointer: PF10 - HDE Build Notes | §2.12, `PF09 consequences` | bridge-dependent `.4`/`.9` wording is retired for the active design while current statuses remain unchanged pending implementation/evidence/drainage.

**Observed Repo and plan reality:** the current r6 D8/D10/PR-06/OPS-01 ownership still routes completion through bridge parity; the current release pipeline and updater still bind that packet; no plan row allocates the direct-only replacement sequence.

**Problem:** satisfying the current literal `.9` would violate the newer controlling topic decision, but removing bridge code without defining replacement predicates would make closure subjective. Plan ownership must reflect the source-before-OPS-before-integration provenance boundary.

**Alternatives considered:** leave `.9` permanently Partial; delete `.9`; mark it Done on bridge removal alone; reinterpret it informally; or define an exact direct-only row and sequence. The first abandons the epic outcome, deletion loses a required runtime concern, bridge absence alone is insufficient evidence, and informal reinterpretation is unreviewable. The exact amendment is minimum and testable.

**Selected decision:**

- Amend `.4` for HDE-EPIC038 by removing active bridge fallback/provider parity from the DB semantic home and requiring direct provider selection, strict retired-key refusal, typed direct failure, direct posture, least-privilege/search-path/DDL/constraint/view/partition observations, and current evidence binding.
- Rename/redefine `.9` for HDE-EPIC038 as **`Direct database connectivity & retired-transport enforcement`**. It proves `DATABASE_URL`/`psycopg` only; refusal of any retired key before provider I/O; typed fail-closed missing/unavailable direct access; zero alternate transport attempts; live direct read-only posture; projection-only DDL identity truth; and local plus OPS-03 evidence in Index/Mirror.
- Keep `.6`, `.11`, and `.5.2` meanings intact; update their current pipeline/tooling dependencies to the direct-only evidence graph.
- Assign implementation to PR-06R-A, live proof to OPS-03, and atomic final integration/support crosswalk to PR-06R-B.

**Minimum-scope rationale:** only the two bridge-dependent row meanings change. The other three rows need dependency/evidence updates, not semantic redesign. No unrelated Distillation row moves into scope.

**Exact implementation owner and locus:** PR-06R-A and PR-06R-B loci are those in §9; OPS-03 loci are in `RSC-004`; later PF09 wording/status maintenance is human-owned and separately authorized.

**Exact contract and evidence decision:** the row-specific predicates in §9 are normative for this CRD. The exact local path/key/schema/producer are in `ADR-CANON-006`; the exact live packet root/keys/schemas/producers are in `ADR-CANON-007`; the exact 19-stage release roster is in `RSC-005`.

**Affected boundaries:** PF09.6 `.4` and `.9` semantics; r6 D8/D10/D13/D12/D1 ownership and dependencies; current OPS/release/updater bindings; later row support statements.

**Unchanged boundaries:** PF09 general status semantics; `.6` one-button meaning; `.11` mapped-cache behavior; `.5.2` Index/Mirror discipline; all other PF09 rows; QA, acceptance, token, deployment, migration, board, and closeout authorities.

**Source-adapter scope:** no new product adapter beyond ADR-CANON-005. This ADR consumes the direct façade and evidence contracts; it does not create a second selection path.

**Persistence and durable-data effect:** none beyond the Repo evidence primaries/companions already specified. No database or product payload change.

**Compatibility:** historical PF09 support notes may cite OPS-01 only as time-bounded history. Current support uses the new predicates. No automatic reinterpretation of an old `Done` or token occurs; the affected rows are not currently Done.

**Migration:** approve CRD and plan revision; implement/merge PR-06R-A; execute/admit OPS-03; atomically integrate PR-06R-B; obtain final review; then update PF09 wording and status notes only for rows individually supported by evidence.

**Producer and consumer ownership:** implementation/evidence producers remain as ADR-CANON-005/006/007 define; PR-06R-B produces the support crosswalk; PF09 maintainer consumes it; no implementation or OPS actor writes PF09 status.

**Validation:** each row is independently evaluated against the §9 predicate table; final pipeline stage semantics are mutation-tested; current/historical evidence cannot alias; status recommendations cite exact current paths and validation results; an incomplete row remains unchanged.

**Safeguards:** no bulk all-rows completion claim; no bridge-absence shortcut; no current PASS from historical evidence; no plan text treated as implementation proof; no QA or token inference; distinct owner boundaries preserve provenance.

**Rollback or fail-closed posture:** if an implementation/evidence predicate fails, do not recommend that row. If PR-06R-B must be reverted, retain direct-only runtime, remove the proposed current evidence bindings atomically, and leave all PF09 statuses unchanged. Never restore bridge parity as rollback.

**Adoption sequence:** IA approval → authorized plan revision → PR-06R-A → OPS-03 → PR-06R-B → final technical/evidence review → permanent PF09/PF drainage and any status maintenance.

**Plan consequences:** the complete §9 matrix is mandatory input to the next r6-lineage revision. `r1` remains the epic-scope baseline. Obsolete OPS-01R/PR-C bridge clauses are removed, not carried as optional fallback.

**Permanent PF-Canon or ADR drainage:** PF09.6 — Canon HDE Build Checklist Distillation exact rows `HDE-DIST001.4` and `.9` receive the semantic amendments; `.6`, `.11`, and `.5.2` receive only evidence/dependency/status-note drainage. Ordering is runtime/evidence implementation → final support review → PF09 wording/status. All unrelated PF09 content remains unchanged.

**Downstream effects:** once fully proven, a later PF09 action may consider `.4 Partial -> Done`, `.6 Partial -> Done`, `.9 Partial -> Done` under the amended title, `.11 Optional -> Done`, and `.5.2 Partial -> Done`, each independently. No change is made here.

**Nonclaims:** no plan or PF edit, implementation, OPS, QA PASS, token satisfaction, PF09 movement, deployment, migration, board work, slice completion, epic completion, acceptance, or closeout.

### Consolidated permanent drainage and adoption order

| Order | Target | Exact locator | Decision requiring drainage | Effect | Unchanged canon |
|---|---|---|---|---|---|
| 1 | PF07 — Glow Infrastructure | §§4.1, 4.2, 7.0, 7.1, 8.1, 9.2 | `ADR-CANON-005` | `SUPERSEDES` active bridge/service/key/fallback rules | explicit environments, direct DB ownership, least privilege, fail-closed rails |
| 2 | PF14 — HDE Mechanics Guide | §§20.3, 20.3.1 | `ADR-CANON-005`, `006` | `SUPERSEDES` bridge provider/parity mechanics | truthful row-level proof, scope rationale, secret safety |
| 3 | PF12 — HDE Schemas and Artifacts | §§8.7, 8.6.3.4 | `ADR-CANON-006`, `007` | `SUPERSEDES` current bridge family; `EXTENDS` with direct local/OPS-03 families | canonical JSON, primary ownership, Human Index, Machine Mirror, checksums, path proofs |
| 4 | PF04 — HDE Governance | §2.0 `Acceptance Tokens` | `ADR-CANON-005`, `006` | retire bridge-only token semantics; do not mint an OPS-03 token by implication | canonical token ownership, acceptance separation, secret-safe and fail-closed rails |
| 5 | PF09.6 — Canon HDE Build Checklist Distillation | exact rows `.4`, `.6`, `.9`, `.11`, `.5.2` | `ADR-CANON-008` | `AMENDS` `.4`/`.9`; dependency/status-note drainage only for the others | general Done/supportable semantics and every unrelated row |
| 6 | Current Implementation Plan, r6 lineage | D1, D8, D10, D12, D13, PR-06, OPS-01/OPS-02 units | all four proposed ADRs | plan revision, not canon effect | r1 epic-scope baseline and unrelated deliverables |

### PF10 consequence

PF10 v12.3.2 §2.12 already supplies the exact-topic direct-only and retired-bridge decision used by this CRD. No new PF10 rule is required before IA can review the design. After implementation and evidence, a later PF10 living-context entry may record the adopted CRD/ADR lineage and observed completion posture, but it must not replace the required plan revision, permanent owning-PF drainage, evidence review, PF09 maintenance, QA, acceptance, or closeout.

### Adoption and nonmovement

Technical IA approval adopts none of these decisions into product source, plan text, permanent PF wording, ADR files, or PF09 rows. It only approves the bounded technical design as authoritative input to the next authorized plan revision. No status moves until implementation, OPS-03, atomic integration, final review, and separate PF09 maintenance establish and record row-specific support.

## 11. Evidence, Risks, and Residual Unknowns

### Factual evidence and Repo validation

| Evidence area | Observed fact | Evidence pointer |
|---|---|---|
| Repo identity | Connected read-only Repo is `amthorn78/glow-hdengine-v2`, branch `main`, HEAD `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a`. | Evidence pointer: Repo \| connected GitHub commit identity \| `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a`; `docs: update PF10 build notes to v12.3.2`. |
| Primary selection | `DBAccess.for_current_env` reads direct and bridge configuration, imports two providers, and defaults to `psycopg` then `bridge`. | Evidence pointer: Repo \| `engine/db/adapter.py`, `DBAccess.for_current_env` \| observed default order `['psycopg', 'bridge']` and retired-key reads. |
| Duplicate selection | The compatibility resolver separately implements DSN and HTTP bridge attempts. | Evidence pointer: Repo \| `adapter/db_access.py`, `_try_dsn`, `_try_bridge`, `db_resolve` \| observed `urllib` bridge I/O and dual result branches. |
| Active bridge provider | An executable HTTP bridge provider remains present. | Evidence pointer: Repo \| `engine/db/providers/bridge_provider.py` \| observed current provider module at HEAD. |
| Active bridge evidence | Current producer/checker/OPS/release surfaces still construct, validate, or require bridge evidence. | Evidence pointer: Repo \| `tools/evidence/generate_db_bridge_parity.py`; `scripts/ops/hde_epic038_ops01r.py`; `tools/evidence/hde_epic038_ops01_v5.py`; `tools/evidence/run_sanity_pipeline.py` \| observed active bridge generator, runner/validator, and `DB-bridge parity` stage. |
| Current updater meaning | OPS-01 and OPS-02 are bound under current PR-06 OPS evidence constants. | Evidence pointer: Repo \| `tools/evidence/update_evidence_index.py`, `EPIC038_PR06_PRIMARY_ARTIFACTS` \| observed current OPS-01 and OPS-02 primary roster. |
| Mapped-cache dependency | The local `.11` producer imports and patches bridge functions to enforce no I/O. | Evidence pointer: Repo \| `tools/evidence/generate_v2_mapped_cache_evidence.py` \| observed bridge-provider import and bridge HTTP guard patches. |
| Retained DDL repair | A versioned pure DDL identity projection exists. | Evidence pointer: Repo \| `engine/db/ddl_identity_projection.py` \| observed schema `hde.ddl_identity_projection.v1`. |
| Retained scanner repair | Raw-marker and safe environment-reference checks cover multiple current syntaxes. | Evidence pointer: Repo \| `tools/evidence/retained_evidence_safety.py` \| observed `_RAW_MARKER` and `SAFE_ENV_REFERENCE` contracts. |
| Current exact-topic canon | Direct psycopg is sole active transport; bridge keys/lane are retired; historical bytes cannot become current proof. | Evidence pointer: PF10 - HDE Build Notes \| §2.12 complete unit \| "Direct PostgreSQL access through the Glow-owned psycopg provider is the sole active HDE database transport." |
| PF09 conflict | `.4` and `.9` still encode bridge fallback/parity, and the mapped rows remain Partial/Optional. | Evidence pointer: PF09.6 - Canon HDE Build Checklist Distillation \| complete `.4`, `.6`, `.9`, `.11`, `.5.2` rows \| current `.9` title is `DB–bridge parity & env connectivity`; statuses are `Partial`, `Partial`, `Partial`, `Optional`, `Partial`. |
| Plan conflict | D8/D10/PR-06/OPS-01 still assign bridge parity and final binding; D12/OPS-02 remains the `.11` lane. | Evidence pointer: Implementation Plan \| D8, D10, D12, D13, PR-06, OPS-01, OPS-02 \| observed current bridge-dependent execution baseline and retained OPS-02 ownership. |

The connected remote view has no local working tree. All product-Repo inspection was read-only before and after. No Repo file, branch, index, evidence artifact, external service, database, or Git state was mutated during this CRD authoring.

### Diagnostics and negative searches

1. **Proposed direct local identities:** searched Repo for exact case-sensitive `generate_hde_epic038_direct_db_selection.py`, `direct_db_selection.snapshot.json`, and `hde_epic038_direct_db_selection.v1.json`; scope: current connected repository tree; method: connected GitHub code search; result: 0 hits. These are therefore proposed new loci, not observed files.
2. **Proposed OPS-03 identities:** searched Repo for exact case-sensitive `hde_epic038_ops03.py`, `hde_epic038.ops03`, and `audit/ops/hde-epic038/ops-03`; scope: current connected repository tree; method: connected GitHub code search; result: 0 hits. These are proposed new loci.
3. **Proposed retired-key error:** searched Repo for exact case-sensitive `RetiredBridgeConfiguration`; scope: current connected repository tree; method: connected GitHub code search; result: 0 hits. The type is a proposed CRD decision.
4. **PF12 OPS-03 silence:** searched current PF12 topic-owning §§8.6.3.4 and 8.7 for exact case-sensitive `hde_epic038.ops03`, `hde_epic038_ops03`, and `ops-03`; method: exact text search plus complete-unit reading; result: 0 hits. General PF12 evidence governance remains applicable.
5. **Active retired-key surface:** searched Repo for exact case-sensitive `DB_BRIDGE_URL`; scope: current product source, tools, CI checks, tests, and current docs/guidance; method: connected GitHub code search plus relied-on file inspection; result: multiple hits, including active runtime/tooling loci listed above. Historical/canon hits alone were not treated as executable defects.

Name-based zero-hit searches establish only that the exact proposed identities are new. The architecture selection rests on inspected semantics of the existing façade, compatibility resolver, providers, producers, validators, updater, and pipeline rather than names alone.

### Selected architecture rationale

The chosen design minimizes new mechanisms while separating three facts that cannot truthfully share one producer or time boundary:

1. **Runtime behavior** belongs to the existing primary façade and can be proven deterministically with local cases.
2. **Current external DB posture** belongs to a separately authorized read-only OPS execution against immutable merged tooling.
3. **Release and PF09 supportability** belong to a later atomic Repo integration that validates exact bytes and the complete evidence graph.

This separation prevents source code from fabricating later external evidence, prevents OPS from writing governed Repo companions, prevents a final integration from becoming the OPS producer, and preserves old bridge bytes without granting them current meaning.

### Rejected alternatives and why they remain rejected

| Alternative | Reason rejected |
|---|---|
| Recreate or repair `pg-bridge` | Contradicts PF10 §2.12 and the approved retirement premise; reintroduces operational complexity without satisfying the direct-only target. |
| Keep bridge code behind missing configuration | Retired-key presence can revive policy; executable source/tests/guidance continue to define it; release remains dependent on forbidden semantics. |
| Delete only the provider | Leaves duplicate resolver, generators, validators, pipeline bindings, mapped-cache imports, and PF09/plan conflict. |
| Treat service/key absence as proof | Does not prove provider selection, direct health, DB posture, failure behavior, evidence graph, or mergeable support. |
| Relabel historical OPS-01 | Falsifies time-of-capture meaning and violates PF10's explicit historical boundary. |
| Repeat OPS-01R/Railway discovery | Exercises a retired target and does not answer the remaining direct DB posture question. |
| No OPS | Local fixtures cannot establish current live/shared DB grants, schema, views, partitions, or connection posture. |
| Ad hoc direct SQL/manual report | Lacks exact source identity, one-attempt authority, strict schemas, secret controls, independent validation, and deterministic admission. |
| One combined source/evidence PR | Cannot contain external evidence produced after its own source is merged without breaking provenance. |
| Permanent dual-current bridge/direct families | Preserves ambiguous current meaning and producer/consumer collision. |

### Material risks, safeguards, and rollback

| Risk | Safeguard | Fail-closed or rollback posture |
|---|---|---|
| A retired key with an empty value bypasses refusal | detect mapping membership, not truthiness; test each key singly/combined at empty, `0`, whitespace, and nonempty values | any presence raises before provider/value access; no alternate path |
| Secret, DSN, host, role, or raw row leaks into evidence/errors | names/presence/count/hash only; strict schemas; stable codes; raw-marker and secret-reference scanner; canonical logs | validator rejects candidate/current primary; no indexing |
| Duplicate resolver retains hidden bridge I/O | compatibility layer delegates to sole façade; active-source/import/HTTP scan; remove provider and bridge runner/checker | block PR-06R-A; disable DB entrypoint rather than restore bridge |
| Direct failure silently falls through or retries | exact one-provider attempt and typed errors; counter assertions | fail immediately; zero alternate transport attempts |
| Runtime writes governed evidence | remove `snapshot_path`; pure `selection_evidence`; dedicated sole producer | test filesystem remains unchanged; block merge |
| Removing bridge breaks `.11` no-I/O proof | replace bridge-specific patches with generic provider/outbound-I/O guards; preserve existing `.11` predicates and OPS-02 | mapped-cache stage fails; no OPS-02 rerun or bridge restore |
| OPS-03 issues a write or extra SQL | exact ordered IDs, static classifier, transaction read-only first, exact count, rollback, validator mutation tests | authorization consumed; candidate inadmissible; no retry under same bytes |
| OPS-03 source or authorization drifts at dispatch | hash-bound commit/interpreter/scripts/argv; pre/post manifest; dispatch validation immediately before external call | pre-marker stop means no call; post-marker drift is failure |
| OPS evidence self-certifies | independent validator owns receipt; PR-B validates before/after copy | missing/failing receipt blocks admission |
| Historical bridge bytes are regenerated or overclaimed | frozen hashes; historical record type/notes; integrity-only stage with forbidden current bridge predicates | any byte/meaning drift blocks PR-06R-B; restore historical bytes only from trusted history, never regenerate |
| Index/Mirror has duplicate, missing, or partial rows | sole updater after complete primary inventory; exact cardinality/path/hash checks | revert entire PR-B generated set and fail release |
| Release reports PASS while mandatory direct stage is skipped | exact ordered 19-stage roster, no skip, first-failure stop, stage mutation tests | final result is FAIL; no supportability claim |
| PF09 rows move together despite independent evidence | exact row predicate table and separate support statements | leave each unsupported row unchanged |
| Rollback reintroduces bridge | explicit no-bridge rollback rule | retain direct-only code or disable DB functionality; bridge is never rollback target |
| External DB is unavailable | one-attempt negative receipt with stable code; no data/write side effect | no tracked success packet, no PR-06R-B, no status claim |

### Residual non-material Unknowns

1. **Direct DB availability at OPS-03 execution.** Discovery method: the exact authorized health connection and read-only transaction. Stop: any failure yields an inadmissible names-only failure receipt and blocks downstream integration. This cannot change the selected architecture, schemas, ownership, or rails.
2. **Derived run identities.** `run_id`, timestamps, authorization hash, resolved interpreter identity, merged source hashes, and primary checksums are derived from the later exact authorization/execution. Validators bind them; no unresolved literal is baked into a contract.
3. **Current Railway inventory.** Not independently observed in this CRD. It is intentionally not a closure predicate because no bridge service or Railway CLI participates in the selected architecture. If another owner later needs inventory proof, it requires a distinct bounded task and cannot delay or overclaim this direct-only evidence.

No residual Unknown can change a module, API, schema, path, key, producer, consumer, owner, migration, validation predicate, rollback rule, dependency, or safety boundary in this CRD.

## 12. Approval Limitations and Nonclaims

This CRD:

- does not implement `RSC-001` through `RSC-005` or any ADR decision;
- does not edit, create, move, or delete product, planning, PF-Canon, ADR, or PF09 files;
- does not revise the `r1` Epic Plan or `r6` Implementation Plan;
- does not move any PF09 status or create `Supportable from repo evidence` by itself;
- does not execute, simulate, approve, retry, or complete OPS-01, OPS-01R, OPS-02, or OPS-03;
- does not prove that `pg-bridge` or any Railway variable/service is absent externally;
- does not access, mutate, migrate, or deploy a database or another external object;
- does not authorize a production write, deployment, migration, external call, implementation merge, or release;
- does not regenerate, repair, rewrite, relabel, reapprove, or reopen historical evidence;
- does not create QA PASS or convert OPS evidence into QA evidence;
- does not satisfy an acceptance token, including a retired bridge token;
- does not accept provisional or future implementation;
- does not establish acceptance, release readiness, deployment readiness, or board status;
- does not close the remediation slice; and
- does not close HDE-EPIC038.

IA approval means only that the complete technical solution, causal scope, proposed architecture, schemas, paths, keys, producers, ownership, compatibility, migration, validation, safeguards, rollback, plan consequences, canon effects, and nonclaim boundaries are technically approved as input to a separately authorized plan revision.

## 13. Questions for the Implementation Agent

None.

## 14. Implementation Agent Review Gate

### `APPROVE`

IA may return `APPROVE` only if all of the following are true:

1. Every material debugging item in §4 has exactly one accurate disposition, and `BUG-004` through `BUG-009` are confirmed by the cited current Repo/canon/plan conflict.
2. The three-boundary sequence PR-06R-A → OPS-03 → PR-06R-B is the minimum coherent provenance-safe rescope; no bridge recreation, Railway discovery, or historical relabeling is needed.
3. `engine.db.adapter.DBAccess` is a feasible sole selection owner; the exact retired-key membership/refusal rule, typed error, direct-only API, compatibility v2 shapes, and removal roster are implementable without changing public/durable contracts.
4. The direct-selection evidence schema, path, key, producer, four cases, predicates, canonicalization, negative receipt, consumers, companion ownership, migration, and rollback in `RSC-003`/`ADR-CANON-006` are complete and collision-free.
5. OPS-03's authorization, exact roots, argv/source binding, rails, one-attempt semantics, query roster, counts, packet inventory, seven schemas, primary producers, validator ownership, canonical bytes, checksum, failure receipt, secret safety, read-only behavior, admission, and rollback in `RSC-004`/`ADR-CANON-007` are complete and feasible.
6. The current-versus-historical evidence split preserves old primary bytes/provenance while removing every current bridge PASS/fallback/token inference.
7. The exact 19-stage release roster, updater/orientation order, row-specific predicates, atomic integration, and rollback in `RSC-005` and §9 are sufficient to produce truthful support without executing OPS inside release.
8. Every ownership boundary has one producer, every consumer migration is stated, no permanent dual-current evidence family remains, and no downstream owner is silently moved or closed.
9. The plan-consequence matrix accounts for D1/D8/D10/D12/D13, PR-06, OPS-01, OPS-02, the five affected PF09 rows, dependency order, evidence outputs, validation, updater/release order, retained owners, and exclusions.
10. `ADR-CANON-005` through `ADR-CANON-008` each contain a complete independently reviewable decision, correct canon effect, exact supersession/amendment/extension boundary, exact loci/contracts, compatibility, migration, ownership, validation, safeguards, rollback, adoption, plan, drainage, downstream, and nonclaims.
11. The exact PF07/PF12/PF14/PF04/PF09.6 drainage targets and ordering are technically correct; current PF10 §2.12 is used only for its exact retired-bridge topic; unrelated canon remains unchanged.
12. Current PF09 statuses remain unchanged, row support is independent, and no implementation, OPS, QA, token, acceptance, deployment, migration, closeout, or external-state claim is implied.

An `APPROVE` response must identify the CRD ID/version, explicitly approve `ADR-CANON-005`, `ADR-CANON-006`, `ADR-CANON-007`, and `ADR-CANON-008` with their effects, and repeat that approval is technical only and precedes the separately authorized plan revision and implementation.

### `RETURN FOR REVISION`

IA must return `RETURN FOR REVISION` if any causal premise is unsupported; any retained repair would regress; a bridge execution path or current bridge meaning remains; a material API/schema/path/key/producer/consumer/owner choice is absent or conflicting; the local/live/current/historical proof boundaries can alias; OPS-03 can leak a secret, issue a write, retry, drift, self-certify, or write outside its authorization; the evidence graph can be partially updated; a PF09 predicate is insufficient or overclaims; a canon effect/locator/drainage target is wrong or incomplete; the design requires an unstated external value; rollback can restore bridge; or any prohibited completion claim is implied.

Each return item must provide:

- `REV-###`;
- the exact affected `BUG`, `CAUSE`, `RSC`, and `ADR-CANON` IDs;
- the incomplete or incorrect decision;
- the current Repo/PF/plan evidence that contradicts it;
- the exact correction required;
- whether the correction changes canon effect, schema/path/key/producer, ownership, plan order, validation, rollback, PF09 support, or nonclaims; and
- the permanent drainage targets affected.

IA must not implement a correction inside the review, choose an unstated alternative on Sekhmet's behalf, approve only a subset while leaving a material cross-dependency unresolved, or treat a future implementation observation as current proof.

## 15. Revision History

| Version | Date | Author | State | Summary |
|---|---|---|---|---|
| `v1.0` | `2026-07-18` | Sekhmet | Superseded | Initial post-PR359 rescoping CRD derived from the then-current debugging flow, four submitted findings, DDL architecture analysis, failed OPS recapture RCA, current Repo/PF sources, and r1/r6 baselines. |
| `v1.1` | `2026-07-18` | Sekhmet | Superseded | Resolved initial IA findings by correcting authority, using bounded discovery for then-material Railway facts, reducing OPS controls, binding call vectors, and completing `ADR-CANON-004`. |
| `v1.2` | `2026-07-18` | Sekhmet | Superseded | Closed plan-adoption, provenance, authorization/policy, expected-identity, and failure-posture gaps while retaining exact DDL projection drainage. |
| `v1.3` | `2026-07-18` | Sekhmet | Superseded by this complete rescope | Closed source/write isolation and independent pre-boundary validation for the then-current bridge-dependent OPS-01R/PR-C design. Its pure DDL projection decision remains; its bridge-dependent execution and evidence decisions are obsolete after PF10 v12.3.2. |
| `v1.4` | `2026-07-20` | Sekhmet | Pending IA technical review | Complete replacement CRD derived from the full active debugging flow and supporting sources at Repo HEAD `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a`. It preserves completed non-bridge repairs, eliminates active bridge runtime/tooling/evidence semantics, defines direct-only local evidence and authorization-bound OPS-03, assigns atomic PR-06R-B integration, establishes row-specific PF09 supportability, and provides complete `ADR-CANON-005` through `ADR-CANON-008`. |

STATUS: APPROVED

# Approval Notes

# Rescoping CRD Review - HDE-EPIC038 - POST-PR359-REMEDIATION

## 1. Document Control

- **Review version:** `v1.4`
- **Reviewed CRD ID and version:** `CRD-HDE-EPIC038-POST-PR359-REMEDIATION` `v1.4`
- **Epic ID and name:** `HDE-EPIC038` — Distillation Pass 3
- **PR or slice ID:** `POST-PR359-REMEDIATION`
- **Reviewer role:** Glow Implementation Agent
- **PO approval posture:** PO authorization to rescope is established. It is treated as authority to submit and technically review the rescope, not as proof of correctness or implementation authorization.
- **CRD_FILE:** `rescoping-crd-hde-epic038-post-pr359-remediation-v1.4.md`
- **APPROVED_IMPLEMENTATION_GUIDE_FILE:** `r1 Epic Plan HDE-EPIC038.md`
- **CURRENT_IMPLEMENTATION_PLAN_FILE:** `r6 Implementation Plan HDE-EPIC038.md`
- **REPO_ROOT_OR_GITHUB:** `glow-hdengine-v2`
- **Repo inspection mode:** Connected GitHub repository, read-only. No local product-Repo worktree or command execution was used.
- **Observed Repo identity:** `amthorn78/glow-hdengine-v2`; default branch `main`
- **Observed Repo revision:** `d1c36af03dccc612f29b9ac4dcc002fb5b08d74a` — `docs: update PF10 build notes to v12.3.2`
- **Observed branch state:** `main`; connected remote view, not detached
- **Working-tree state:** Not applicable to the connected GitHub view. No product-Repo mutation occurred.
- **Current PF-Canon consulted:**
  - `PF10-HDE-Build-Notes`, Addendum 2.11 and Addendum 2.12
  - `PF09.6-Canon-HDE-Build-Checklist-Distillation`, §0.2 and rows `HDE-DIST001.4`, `HDE-DIST001.6`, `HDE-DIST001.9`, `HDE-DIST001.11`, and `HDE-DIST005.2`
  - `PF07-Canon-Glow-Infrastructure`, §§4.1, 4.2, 7.0, 7.1, 8.1, and 9.2
  - `PF12-Canon-HDE-Schemas-and-Artifacts`, §§8.6.3.4 and 8.7, plus the Human Evidence Index, Machine Evidence Mirror, checksum, and path-proof ownership units
  - `PF14-Canon-HDE-Mechanics-Guide`, §§20.3 and 20.3.1
  - `PF04-Canon-HDE-Governance`, §2.0 and the applicable rails, secret-safety, evidence, and OPS-policy units
  - `PF06-Canon-Epic-Process-Guide`, the PR/OPS separation, PF09-accountability, PF10-live-truth, and documentation-drainage units
- **Reviewed architecture decisions:**
  - `ADR-CANON-004` — **APPROVED, RETAINED WITH NARROWED DEPENDENCY BOUNDARY**. Its pure strict DDL identity projector and projection-only truth semantics remain governing; its bridge-dependent packet and OPS dependencies are superseded.
  - `ADR-CANON-005` — **APPROVED (`SUPERSEDES`)**. Direct PostgreSQL becomes the sole executable HDE database transport for the exact affected scope.
  - `ADR-CANON-006` — **APPROVED (`SUPERSEDES`)**. Current direct-only selection evidence is separated from frozen historical bridge evidence.
  - `ADR-CANON-007` — **APPROVED (`EXTENDS`)**. The authorization-bound OPS-03 direct read-only evidence contract is established for its exact scope.
  - `ADR-CANON-008` — **APPROVED (`AMENDS`)**. The affected PF09.6 completion semantics and PR-06R ownership are redefined without automatic status movement.

Evidence pointer: CRD | §1 `Document Control` | "CRD ID `CRD-HDE-EPIC038-POST-PR359-REMEDIATION`; Version `v1.4`; Epic `HDE-EPIC038` — Distillation Pass 3; PR or slice ID `POST-PR359-REMEDIATION`."

Evidence pointer: Repo | repository metadata and current default-branch commit | "repository=amthorn78/glow-hdengine-v2; default_branch=main" | "HEAD=d1c36af03dccc612f29b9ac4dcc002fb5b08d74a; docs: update PF10 build notes to v12.3.2"

Evidence pointer: PF10-HDE-Build-Notes | §2.12 `pg-bridge and DB_BRIDGE_URL Deprecation and Retirement - Direct PostgreSQL Is the Sole Active HDE Database Transport` | "`DATABASE_URL` is the sole canonical HDE database endpoint key." | "Direct PostgreSQL access through the Glow-owned psycopg provider is the sole active HDE database transport."

## 2. Review Decision

Decision: APPROVED

The CRD is technically ready to govern a separately authorized next-version revision of the Current Implementation Plan. It accurately identifies the conflict between the newly controlling direct-only PF10 posture and the still-bridge-capable current Repo, permanent PF-Canon, and Current Implementation Plan. It defines the minimum coherent correction as a source-first direct-only convergence, one bounded read-only OPS-03 capture, and one atomic evidence/release integration. The proposal preserves public and durable-data boundaries, gives each current and historical evidence surface one owner and one meaning, supplies exact APIs, schemas, paths, keys, producers, validation, rollback, and adoption order, and does not claim implementation, OPS completion, QA PASS, PF09 movement, acceptance, or closeout.

The broader changes are causally necessary rather than convenience expansion. Removing only the bridge provider would leave a second resolver, bridge-dependent generators and validators, a bridge-required release stage, bridge-coupled mapped-cache guards, current evidence bindings that reinterpret historical bridge artifacts as current PASS, and PF09/plan completion language that is no longer satisfiable. The CRD closes that dependency graph without broadening user-facing product scope.

Evidence pointer: CRD | §2 `Executive Summary` | "The selected architecture is a complete direct-only cutover with one runtime façade, one active provider, one separately versioned direct-only local evidence artifact, one bounded direct-read OPS packet, and one atomic final integration."

Evidence pointer: CRD | §3 `Prohibited inference` | "Neither PO authorization nor IA approval means implementation complete, OPS complete, QA PASS, acceptance-token satisfaction, PF09 movement, deployment, migration, slice completion, epic closure, or closeout."

Evidence pointer: Implementation Guide | `Scope boundaries` | "Out of scope: New public Reader behavior. New public routes. App-side HumanDesignAPI ownership. Broad HumanDesignAPI v2 platform conformance. PF document edits as implementation deliverables."

Evidence pointer: Implementation Plan | `Source posture` and `PR-06` / `OPS-01` units | "PF10 governs only where it explicitly speaks." | The current execution design still assigns a DB-bridge parity stage and a direct-versus-bridge OPS-01 packet to PR-06 completion.

## 3. Source Coverage and Conflicts

### Complete-source coverage

The Rescoping CRD, Approved Implementation Guide, and Current Implementation Plan were each read end-to-end. The review used the CRD as the sole submitted artifact under review. The two plans, current Repo, and task-relevant current PF sources were used only in their supporting authority lanes. No separate approval document, RCA, Repo export, evidence bundle, or extra-evidence artifact was used.

The relevant current PF units were retrieved as complete units before reliance. PF10 relevance was established by exact-topic coverage of HDE-EPIC038, `pg-bridge`, `DB_BRIDGE_URL`, direct PostgreSQL, OPS-01R, bridge evidence, and the affected PF09 rows. The latest PF10 addendum therefore controls those exact topics; permanent PF-Canon controls everything outside that bounded scope.

Evidence pointer: CRD | §1 `Source units used` | The CRD identifies the complete current plans, current Repo loci, PF10 Addendum 2.12, the exact affected PF09.6 rows, and the relevant PF07, PF12, and PF14 units.

Evidence pointer: PF10-HDE-Build-Notes | `Precedence and versioning` | "For any topic explicitly covered in this scratchpad, PF10 is the current authoritative source of truth and supersedes all other PF canon until that item is formally reviewed and drained."

### CRD item coverage

The review accounted for:

- retained findings `BUG-001`, `BUG-002`, and `BUG-003`;
- current findings `BUG-004` through `BUG-009`;
- causal chains `CAUSE-001` through `CAUSE-005`;
- rescope decisions `RSC-001` through `RSC-005`;
- all producer, consumer, historical/current, persistence, public-surface, and downstream boundaries in §8;
- all plan consequences, dependencies, validation sequences, row-specific supportability predicates, updater ordering, rollback stops, and exclusions in §9; and
- retained `ADR-CANON-004` plus proposed `ADR-CANON-005` through `ADR-CANON-008`.

No material CRD item was left unreviewed.

### Repo validation posture

Scoped direct GitHub inspection confirmed the material current-state premises:

- `engine/db/adapter.py` imports `BridgeProvider`, consumes `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD`, defaults to provider order `psycopg` then `bridge`, and writes a selection snapshot.
- `adapter/db_access.py` independently implements `_try_dsn`, `_try_bridge`, `db_resolve`, environment selection, and a bridge read/write-smoke branch.
- `engine/db/providers/bridge_provider.py` remains an executable HTTPS provider using `urllib.request`.
- `engine/db/errors.py` contains bridge-specific exceptions and does not yet contain the proposed retired-configuration exception.
- `PsycopgProvider` has existing query, exec, transaction, and introspection mechanics but not the proposed `readonly_tx` contract.
- `scripts/db/capture_epic011_posture.py` still captures direct and bridge providers and writes bridge/runtime parity artifacts.
- `tools/evidence/generate_db_bridge_parity.py` remains the current bridge evidence producer.
- `tools/evidence/run_sanity_pipeline.py` still contains a `DB-bridge parity` stage and validates a bridge-dependent OPS-01 packet.
- `tools/evidence/generate_v2_mapped_cache_evidence.py` still imports and patches bridge-specific seams as part of its hermetic guard.
- `engine/db/ddl_identity_projection.py` already contains the strict pure projector that the CRD correctly preserves rather than reimplementing.
- `tools/evidence/update_evidence_index.py` currently binds the runtime connectivity artifact with bridge-token/current-meaning metadata, while its established record model can support explicit historical reclassification without changing frozen primary bytes.
- the existing OPS-01R runner and validator remain bridge-dependent and therefore require retirement rather than execution.

Evidence pointer: Repo | `engine/db/adapter.py`, `DBAccess.for_current_env` | "order = ['psycopg', 'bridge']" | "bridge_url = (os.getenv('DB_BRIDGE_URL') or '').strip()"

Evidence pointer: Repo | `adapter/db_access.py`, `_try_bridge`, `db_resolve`, and `db_rw_smoke` | The second resolver reads `DB_BRIDGE_URL`, performs `urllib.request.urlopen`, can select `bridge`, and has a bridge write-smoke branch.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py`, `STAGE_NAMES`, `default_steps`, and OPS-01 constants | "09 DB-bridge parity" | Direct provider is `psycopg`; bridge provider is `bridge`; the current packet requires bridge-specific predicates and artifacts.

Evidence pointer: Repo | `engine/db/ddl_identity_projection.py` | `DDL_IDENTITY_PROJECTION_SCHEMA = "hde.ddl_identity_projection.v1"` | `project_ddl_identity()` strictly validates and deterministically sorts the included object and column identity fields.

### Plan and PF-Canon conflicts

The material conflicts are explicit and resolved rather than silently reconciled:

1. The Approved Implementation Guide and Current Implementation Plan authorized bridge fallback/parity mechanics within the epic's internal reliability scope.
2. Permanent PF07, PF09.6, PF12, and PF14 still encode active bridge infrastructure, mechanics, evidence, or completion language.
3. Later controlling PF10 Addendum 2.12 retires `pg-bridge`, the three bridge keys, OPS-01R, bridge-dependent integration, and current bridge evidence meaning.
4. The CRD responds with bounded `SUPERSEDES`, `EXTENDS`, and `AMENDS` decisions, exact permanent-drain targets, and a plan-revision requirement. It does not pretend that the plans or permanent PF documents have already changed.

Evidence pointer: PF07-Canon-Glow-Infrastructure | §§4.1, 7.0, 7.1, 8.1, and 9.2 | The current permanent infrastructure baseline still names the bridge service, `DB_BRIDGE_URL`, and environment-aware fallback.

Evidence pointer: PF09.6-Canon-HDE-Build-Checklist-Distillation | row `HDE-DIST001.9` | The current row is `DB–bridge parity & env connectivity`, requires direct-versus-bridge parity, and is recorded `Partial`.

Evidence pointer: PF14-Canon-HDE-Mechanics-Guide | §§20.3 and 20.3.1 | The current permanent mechanics baseline still defines bridge parity, fallback, checker, and provider mechanics.

Evidence pointer: PF10-HDE-Build-Notes | §2.12 `HDE-EPIC038 and OPS-01R disposition` | "The bridge-dependent HDE-EPIC038 OPS-01R lane is retired." | "the bridge-dependent PR-C packet-integration lane described in PF10 §2.9 is canceled and MUST NOT be executed"

### Evidence sufficiency and material unverified claims

The CRD distinguishes current Repo facts, approved decisions, proposed implementation decisions, historical evidence, and residual unknowns. Every current-Repo premise material to the rescope was directly confirmed. The residual unknowns identified in §4 and §11 are expressly non-material because the selected design does not depend on resolving them. No material claim remains `UNVERIFIED`.

The new OPS-03 evidence does not assume external availability. It makes availability an execution-time, authorization-bound observation; failure consumes the one-attempt authorization, yields no admissible packet, and blocks final integration. This is a fail-closed dependency, not an unsupported premise.

Evidence pointer: CRD | §3 `Sekhmet proposed technical decisions` | "They do not claim to exist in the current Repo."

Evidence pointer: CRD | §11 `Residual non-material Unknowns` | Unknown historical or external details are explicitly excluded from the selected decision's premises and do not authorize inference.

## 4. Review Gate Results

### Gate 1: Authority and source fidelity — PASS

**Rationale:** The CRD stays within the PO-authorized HDE-EPIC038 internal reliability and evidence scope. It treats the Approved Implementation Guide and Current Implementation Plan as baselines requiring a later authorized revision, not as already rewritten. It follows the current PF10-first rescoping posture and distinguishes PO authority, IA approval, plan revision, implementation, OPS execution, PF09 status, QA, acceptance, and closeout. The direct-only architectural change is not rejected merely because it changes permanent canon; it is expressed through explicit ADRs.

**Covered CRD material:** §1 document control and source units; §3 authority and decision posture; §12 approval limitations and nonclaims; §13 questions posture; §14 IA review gate.

Evidence pointer: CRD | §3 `Later authorities` | "a separately authorized next-version revision of the current Implementation Plan must incorporate the selected sequence" | "separate implementation authorization is required before either PR-06R slice is executed"

Evidence pointer: CRD | §12 `Approval Limitations and Nonclaims` | No implementation, plan revision, PF edit, QA PASS, OPS completion, deployment, token satisfaction, PF09 movement, acceptance, slice completion, epic completion, or closeout is claimed.

Evidence pointer: PF06-Canon-Epic-Process-Guide | `Closure axes remain separate` | QA evidence, PF09 drainage, PO closeout, board state, merge provenance, and PF-Canon drainage are separate axes and must not be collapsed.

### Gate 2: Conflict and causal accuracy — PASS

**Rationale:** The CRD identifies a specific current conflict and validates it against current Repo reality. It separates retained repairs from current defects, superseded findings from live premises, and material findings from non-material unknowns. Each mandatory addition has a complete causal chain joining the controlling contract, current implementation, conflict, consequence, minimum change, dependencies, ownership, validation, rollback, plan consequence, and documentation consequence.

**Covered CRD item IDs:** `BUG-001` through `BUG-009`; `CAUSE-001` through `CAUSE-005`.

Evidence pointer: CRD | §4 `Complete finding and action disposition ledger` | `BUG-004` through `BUG-009` are marked confirmed and each is routed to a specific RSC/ADR disposition; retained `BUG-001` through `BUG-003` are not reopened beyond their still-relevant boundaries.

Evidence pointer: Repo | `engine/db/adapter.py`; `adapter/db_access.py`; `engine/db/providers/bridge_provider.py`; `tools/evidence/run_sanity_pipeline.py` | Current executable bridge selection, duplicate resolver behavior, HTTP bridge transport, and bridge-required release validation directly corroborate the CRD's root premises.

Evidence pointer: PF10-HDE-Build-Notes | §2.12 `Decision and effective posture` | Direct PostgreSQL is the sole active HDE database transport; bridge service and keys are retired.

### Gate 3: Minimum coherent rescope — PASS

**Rationale:** Each requested addition is causally necessary and classified. `RSC-001` preserves completed non-bridge work without reopening it. `RSC-002` removes all executable bridge-selection paths and converges selection ownership. `RSC-003` creates one direct-only local truth surface while preserving historical bytes as history. `RSC-004` supplies the missing live direct, read-only observation through a bounded OPS lane. `RSC-005` makes final admission atomic and prevents current PASS from historical bridge evidence. The rescope excludes public behavior, product payload changes, DB writes, migration, deployment, historical reruns, broad cleanup, and unrelated PF09 rows.

**Covered CRD item IDs:** `RSC-001` through `RSC-005`.

Evidence pointer: CRD | §7 `Requested Rescope` | The five RSC items define retained work, runtime convergence, local evidence, OPS-03, and atomic integration as a closed dependency chain.

Evidence pointer: CRD | §2 `Executive Summary` | "This rescope cannot be deferred safely while claiming the affected rows closeable." | The stated consequence is active selection of a retired service, executable retired keys, a forbidden bridge release dependency, and an unsatisfiable `.9` contract.

Evidence pointer: Implementation Guide | `Business Case`, `Scope boundaries`, and `Non-goals` | The epic already covers DB posture, evidence, gates, BodyGraph/DB mechanics, and release sanity while excluding new public Reader behavior, new public routes, broad platform expansion, PF edits as implementation, and automatic status movement.

### Gate 4: Epic and slice boundaries — PASS

**Rationale:** The CRD preserves unique producer and consumer ownership; distinguishes current, historical, retained, canceled, and downstream work; does not reopen historical OPS-01/OPS-02; and keeps mapped-cache truth with its existing OPS-02 lineage. PR-06R-A owns source convergence, OPS-03 owns the live direct observation, and PR-06R-B owns atomic admission and the final support crosswalk. Historical bridge primaries remain frozen and cannot satisfy current gates. No downstream task or PF09 row is silently completed.

**Covered CRD material:** §8 `Ownership and Boundary Effects`; §9 `Dependency and adoption order`; the current/historical evidence boundaries in `RSC-003`; the PR-06R-A → OPS-03 → PR-06R-B sequence.

Evidence pointer: CRD | §8 `Producer and consumer ownership changes` | Runtime selection, local evidence, OPS-03 primaries, independent validation, canonical companions, release admission, and PF09 maintenance have distinct owners.

Evidence pointer: CRD | §8 `Current and downstream boundaries` | Historical bridge material remains provenance only; OPS-02 remains the mapped-cache live-evidence owner; no public, vendor, migration, deployment, or closeout boundary is imported.

Evidence pointer: PF12-Canon-HDE-Schemas-and-Artifacts | Human Evidence Index and Machine Evidence Mirror single-home rules | Current and historical records can remain separately bound with canonical paths, hashes, proof anchors, and explicit metadata without creating a second truth home.

### Gate 5: Implementation Plan executability — PASS

**Rationale:** The CRD is sufficiently concrete to revise the Current Implementation Plan without inventing material loci or decisions. It defines the sole runtime module, exact retired keys, exact refusal type/code/message, exact logical API signatures, selection order, direct transaction contract, compatibility resolver shape, files to retire, local evidence schema/path/key/producer, OPS-03 runner/validator/schema family/root/key/producer assignments, fixed query and connection counts, exact packet inventory, release stages, row-specific predicates, migration order, and rollback stops. Current Repo inspection confirms the named existing loci and reusable mechanics.

**Covered CRD material:** §9 `Implementation Requirements and Plan Consequences`, including the source-grounded requirements, plan-consequence matrix, dependency order, validation order, row-specific supportability predicates, updater order, rollback stops, and exclusions.

Evidence pointer: CRD | `RSC-002` `sole runtime owner and API` | Exact retired-key tuple, exact refusal semantics, exact logical `DBAccess.for_current_env` signature, direct-only selection order, evidence method, and `readonly_tx` contract are specified.

Evidence pointer: CRD | `RSC-003` and `RSC-004` | Exact schemas, paths, artifact keys, record types, producers, cases, predicates, roots, query IDs, connection/statement counts, packet files, and independent receipt ownership are specified.

Evidence pointer: Repo | `engine/db/adapter.py`; `engine/db/providers/psycopg_provider.py`; `scripts/db/capture_epic011_posture.py`; `tools/evidence/update_evidence_index.py` | Existing provider façade, direct provider/introspection mechanics, posture-query families, and canonical updater conventions provide the validated implementation loci and reusable patterns.

### Gate 6: Validation, evidence, and safeguards — PASS

**Rationale:** Validation follows the causal graph: source and static guards first, local direct evidence next, authorization-bound OPS-03 after merged source identity, independent candidate validation before copy, canonical updater convergence after primary integration, then direct-only release validation. The CRD defines strict canonical schemas, unknown-key rejection, exact inventory and checksum coverage, no-secret and no-raw-payload scans, immutable source/interpreter/argv binding, one attempt/no retry, retired-key refusal before provider I/O, read-only transaction enforcement, rollback on success or failure, exact write roots, historical/current alias prevention, row-specific supportability, and atomic rollback. No evidence producer is assigned updater-owned companions.

**Covered CRD material:** §9 validation, updater, supportability, and rollback units; §11 factual evidence, selected rationale, rejected alternatives, risks, safeguards, rollback, and residual unknowns.

Evidence pointer: CRD | `RSC-004` `Validation` and `Rollback or fail-closed posture` | Authorization identity, source and interpreter binding, static/runtime SQL checks, exact counts, strict schemas, checksums, independent receipt, and no admissible packet after failure are required.

Evidence pointer: CRD | §9 `Validation and evidence-generation order` | Source validation precedes OPS; candidate validation precedes copy; canonical updater and release validation follow primary admission.

Evidence pointer: PF04-Canon-HDE-Governance | governed paths, secret safety, rails, and OPS policy units | Acceptance evidence must be governed, secret-safe, fail-closed, and must not convert OPS evidence into QA or token claims.

Evidence pointer: PF12-Canon-HDE-Schemas-and-Artifacts | §8.3 and evidence-index ownership units | The Human Index, hash sentinel, Machine Mirror, mirror checksum, canonical JSON, and sibling path proofs remain canonical-updater-owned companion surfaces.

### Gate 7: Canon-changing ADRs, documentation consequences, and nonclaims — PASS

**Rationale:** Every canon-changing proposal is expressed as one complete ADR with linked causes/RSCs, exact baseline, engineering limitation, alternatives, selected decision, canon effect, bounded topic, unchanged boundary, compatibility, migration, ownership, implementation and plan consequences, validation, risks, safeguards, rollback, drainage targets, adoption order, and nonclaims. Exact PF09 mapping is limited to materially affected rows and no automatic status movement is claimed. Permanent PF drainage is ordered and remains later documentation work.

**Covered CRD item IDs:** `ADR-CANON-004`, `ADR-CANON-005`, `ADR-CANON-006`, `ADR-CANON-007`, and `ADR-CANON-008`.

#### ADR-CANON-004 — PASS

The retained decision is technically sound for the implemented pure DDL identity projector only. The CRD expressly narrows its dependency boundary: strict projection and projection-only truth remain; bridge provider, bridge packet, OPS-01R, and full-DDL-parity implications do not. This preserves implemented reusable architecture and avoids duplicate work.

Evidence pointer: CRD | §10 `Retained architecture record — ADR-CANON-004` | The approved, implemented portion remains only for `engine/db/ddl_identity_projection.py`, `hde.ddl_identity_projection.v1`, strict malformed-input rejection, exact identity projection, and projection-only truth labeling.

Evidence pointer: Repo | `engine/db/ddl_identity_projection.py` | The exact schema, included fields, unexamined fields, strict validation, duplicate rejection, alias conflict rejection, and deterministic sorting are present.

#### ADR-CANON-005 — PASS (`SUPERSEDES`)

The ADR has a causal need, exact superseded active-bridge rule, bounded scope, direct-only API and failure behavior, compatibility plan, file and key retirement consequences, validation, safeguards, rollback, adoption sequence, and permanent PF07/PF14/PF04 drainage. It changes internal transport architecture, not product intent or public scope.

Evidence pointer: CRD | `ADR-CANON-005 — Direct PostgreSQL as the Sole Executable HDE Database Transport` | Exact transport, key, resolver, exception, API, compatibility, validation, rollback, and drainage decisions are specified.

Evidence pointer: PF10-HDE-Build-Notes | §2.12 | The bridge service, bridge keys, fallback, bridge parity, and OPS-01R are retired for the exact topic.

#### ADR-CANON-006 — PASS (`SUPERSEDES`)

The ADR resolves the current/historical evidence conflict with a separate direct-only local evidence family, frozen historical bridge primary bytes, explicit updater metadata reclassification, and a release integrity-only stage. Its paths, keys, schema, producer, cases, predicates, negative receipt, companions, migration, and rollback are bounded and collision-free.

Evidence pointer: CRD | `ADR-CANON-006 — Direct-Only Selection Evidence and Historical Bridge Quarantine` | Current proof and historical provenance receive distinct identities and consumers; historical bridge material cannot satisfy a current direct gate.

Evidence pointer: PF12-Canon-HDE-Schemas-and-Artifacts | §8.7 and current index/mirror rules | The permanent baseline currently treats bridge artifacts as active; the ADR correctly identifies the exact later drainage needed while preserving normal canonical companion ownership.

#### ADR-CANON-007 — PASS (`EXTENDS`)

The ADR fills a real canon gap rather than inventing a second runtime contract. It defines a direct-only, authorization-bound, read-only OPS packet with exact source/interpreter/argv identity, rails, query roster, counts, write roots, packet inventory, seven schemas, producer split, validator, checksum, admission, failure receipt, safeguards, rollback, and nonclaims. The extension is evidence-only and does not authorize a DB write, deployment, or product change.

Evidence pointer: CRD | `ADR-CANON-007 — Authorization-Bound OPS-03 Direct Read-Only Posture Packet` | The complete contract and adoption sequence are specified.

Evidence pointer: PF10-HDE-Build-Notes | Addendum 2.11 `PO-Delegated OPS Execution Authority — PO Authorization Controls Executor Identity` | Delegation is permitted only with task-specific authorization, source identity, safety, and evidence controls; it does not waive missing facts or safeguards.

#### ADR-CANON-008 — PASS (`AMENDS`)

The ADR amends only the bridge-dependent meaning of `HDE-DIST001.4` and `.9`, leaves `.6`, `.11`, `.5.2`, general status semantics, and unrelated PF09 rows intact, and supplies exact row-specific predicates and ownership. It prevents both an impossible literal bridge closure and an unsupported bridge-absence shortcut. Status remains unchanged until final evidence and a later human PF09 action.

Evidence pointer: CRD | `ADR-CANON-008 — Direct-Only PF09.6 Completion Semantics and PR-06R Ownership` | `.9` becomes `Direct database connectivity & retired-transport enforcement`; implementation, live proof, integration, and later status maintenance have distinct owners.

Evidence pointer: PF09.6-Canon-HDE-Build-Checklist-Distillation | §0.2 `Supportable vs drained status notes` | Repo-supported status and already-drained PF09 status must remain explicitly distinct.

#### Documentation consequences and nonclaims — PASS

Permanent drainage targets are exact and ordered: PF07, PF14, PF12, PF04, PF09.6, then the Current Implementation Plan lineage. The CRD does not claim any target has already been edited. It makes no implementation, OPS, QA, acceptance-token, PF09, deployment, migration, board, slice-completion, epic-completion, or closeout claim.

Evidence pointer: CRD | §10 `Consolidated permanent drainage and adoption order` | Each target document, locator, ADR, canon effect, and unchanged boundary is identified.

Evidence pointer: CRD | §10 `Adoption and nonmovement` and §12 | Approval precedes plan revision and implementation; PF09 status and every closure axis remain unchanged.

## 5. Findings

None.

## 7. Nonblocking Notes

1. Direct database availability and authorization remain execution-time facts. The CRD correctly does not assume them: OPS-03 must stop before admission if source identity, authorization, target, direct connectivity, read-only enforcement, exact call counts, or packet validation fails. No CRD correction is required.
2. The Current Implementation Plan and permanent PF07, PF09.6, PF12, PF14, and PF04 wording remain stale for the newly approved architecture. Their revision or drainage is required later in the stated order, but documentation drainage is not proof of implementation and is not a prerequisite to this technical CRD approval.
3. Historical OPS-01 and bridge evidence remain valid only as historical provenance and integrity targets. This review approves their reclassification, not deletion, rewriting, or reuse as current direct-only PASS evidence.

## 8. Approval Scope and Nonclaims

This approval is technical approval of `CRD-HDE-EPIC038-POST-PR359-REMEDIATION v1.4` and the exact architectural decisions listed in §1 of this review.

`ADR-CANON-004` remains governing only for its strict pure DDL identity-projection boundary and projection-only truth semantics. `ADR-CANON-005`, `ADR-CANON-006`, `ADR-CANON-007`, and `ADR-CANON-008` govern their exact direct-only transport, evidence, OPS-03, PF09-semantics, ownership, migration, safeguard, and supersession boundaries pending permanent PF-Canon drainage. The absence of those later permanent edits does not invalidate the approved engineering decisions. No PF document was edited by this review.

Approval authorizes the CRD to govern a later, separately authorized Current Implementation Plan revision. It does not authorize implementation of PR-06R-A or PR-06R-B, execute or authorize OPS-03 by itself, create or merge a PR, perform QA, create QA PASS, execute deployment or migration, change database state, expose secrets, change public Reader/CLI bytes, change durable BodyGraph data, satisfy an acceptance token, move PF09 status, update the board, accept implementation, complete the remediation slice, complete HDE-EPIC038, or perform closeout.

## 9. Re-review Instructions

No re-review required.

DECISION: APPROVED
