# 0 Document Control \[Required-Now\]

## 0.1 Header

**Title:** PF04-Canon-HDE-Governance  
**Version:** v2.8  
**Status:** Canon  
**Effective date:** 2026-08-11  
**Last Update Gate:** 0808 Refresh 4  
**Invocation tag:** `INV-f2ac55d77ce9aacc`

## 0.2 Scope & boundaries \[Required-Now\]

**Role.**  
This document defines **governance, validation, and operational policy** for the Glow HD Engine. It owns:

* Acceptance gates (A3 / A4 / A7 and Epic-level gates).  
    
* Evidence and release discipline (freeze-pack identity, rollback posture).  
    
* SAFE-rails posture and vendor HTTP policy.  
    
* Logging & privacy requirements (keys-only logs; no secrets/PII).  
    
* The public resonance posture (Reader v1 is bands-only, numeric-free; SR-only α=1.0; hysteresis=1 armed for future XR and not exposed).

**Supersession (PF10-HDE-Build-Notes addenda).**

**PF10-HDE-Build-Notes** is living. Authority operates at the level of independently scoped addenda. A higher-numbered applicable addendum governs only overlapping scope or guidance it explicitly supersedes; unrelated addenda and distinct unsuperseded portions remain authoritative. When the active base version is a lettered set, every document in the complete set must be consulted; a later letter extends the set and does not supersede an earlier document. This document integrates all applicable active **PF10-HDE-Build-Notes** positions and routes by **titles only** to single-home PF documents (no version numbers).

**PF10-HDE-Build-Notes reference posture (stable unit: addendum entry).**

* Do not reference **PF10-HDE-Build-Notes** by version strings.  
    
* Prefer referencing **PF10-HDE-Build-Notes** by addendum number \+ addendum title (for example: “PF10-HDE-Build-Notes Addendum 2.10 — Token Load Reduction \[OMITTED: remaining title\]”).  
    
* Do not treat **PF10-HDE-Build-Notes** section numbers as durable anchors for external enforcement; the stable unit is the addendum entry itself.  
    
* When an addendum supersedes earlier **PF10-HDE-Build-Notes** guidance, it must explicitly name what it supersedes (by addendum number/title).  
    
* Legacy note: this document may contain legacy PF10-style labels (for example “PF10-A” / “PF10-AA”) inside headings or notes. Treat them as legacy identifiers only. Do not introduce new PF10-style labels. Replace them with addendum-number references when the correct mapping is known.

**Ownership boundaries (titles-only routing).**

* **Transport & ops policy (this document).**  
  A7 invariants, cache & writers policy, conditional delivery rules, parity requirements, refusal posture, the Aux-suppression carve-out, and the `/internal/version` ops surface are governed here.  
  Exact wire bytes / presenter / CLI flows live in **PF05-Canon-HDE-CLI-API-Vendor-Ref**.  
    
* **Math & algorithms.**  
  Composite logic, scoring, bands, constants, and preimage definitions live in **PF01-Canon-HDE-Math-Spec**.  
    
* **Schemas, pack/manifest, canonical JSON, mirror schema.**  
  Catalog/manifest, canonical JSON rules (UTF-8, no BOM; ASCII-sorted keys; compact; one trailing LF; arrays-as-sets deduped & ASCII-sorted), and the machine-mirror schema & ordering live in **PF12-Canon-HDE-Schemas-and-Artifacts**.  
  All byte checks run under `LC_ALL=C`, `TZ=UTC` (and `LANG=C` where applicable).  
    
* **Architecture.**  
  Engine/adapter/presenter boundaries and flows live in **PF02-Canon-HDE-Architecture**; this document references those boundaries by title only.  
    
* **Endpoint Catalog (A7 proof surface).**  
  The Endpoint Catalog (JSON success) is the **single proof surface** for A7. The Catalog is internal-only and env-gated per entry; entries not gated for prod are unreachable in production.  
  A7 transport proofs **must** run on a Catalog JSON success route (titles-only; path-agnostic).  
  The `/internal/version` ops surface is explicitly excluded and governed in §10.5.  
  A headers-only env-gate proof is required to demonstrate non-prod entries are unreachable in prod.  
  For EPIC-010, Aux HEAD and 304 are explicitly out of scope; A7 proofs remain Catalog JSON success only.

**Single homes.**

* **Token roster.**  
  All governance tokens are listed **once** in §2.0 **Acceptance Tokens**. Other sections refer to §2.0 and do not restate token lists.  
    
* **Evidence Index & Machine Mirror (PF12-Canon-HDE-Schemas-and-Artifacts single home).**  
  **PF12-Canon-HDE-Schemas-and-Artifacts** is the single home for:  
    
  * Evidence titles/paths.  
      
  * The human Evidence Index (`docs/evidence/INDEX.json`) and its hash sentinel.  
      
  * The machine JSONL mirror (`artifacts/evidence_index.jsonl`).


* **PF12-Canon-HDE-Schemas-and-Artifacts** governs records-only JSONL, one trailing LF, unknown-key rejection, ASCII field order, sort-before-write, single mirror file, and required `proof_anchor` path-proofs.  
  **PF04-Canon-HDE-Governance** may reference required titles only; **PF12-Canon-HDE-Schemas-and-Artifacts** remains the single home for index/mirror schema and catalogs.

## 0.3 Tagging convention

Each section is tagged to show implementation status:

* \[Implemented\] — verified in repo and enforced by tests.  
    
* \[Required-Now\] — required for the current build or acceptance gates.  
    
* \[Speculative\] — design accepted for a future release; not yet wired.  
    
* \[OPEN\] — unresolved or gated pending Doc-Delta review.

## 0.4 Change policy

**Single homes; no duplication.**  
Math and Architecture bytes are not restated here. Transport bytes remain in **PF05-Canon-HDE-CLI-API-Vendor-Ref**. Artifacts and mirror schemas are owned by **PF12-Canon-HDE-Schemas-and-Artifacts**.

**Governed paths only.**

Evidence artifacts that participate in acceptance (tokens, gates, Doc-Delta proofs) MUST live under governed repo paths intended to be indexed and mirrored. “Single-home” refers to the Evidence Index and machine JSONL mirror being the single authoritative binding between artifact keys and repo paths, not to a single directory.

Default governed roots include `artifacts/**`, `docs/**`, and `audit/**`. Additional evidence roots (for example, `reports/**`, `validation/**`, `proofs/**`, `parity/**`, `scan_reports/**`, `catalog/**`, `narratives/**`, `internal/**`) are permitted only when they are explicitly treated as governed evidence families and are bound into the Evidence Index and machine mirror with co-located path-proofs.

`scripts/**` and `tools/**` are code and tooling roots by default. If any outputs under these roots are claimed as governed evidence, they MUST be re-homed under governed evidence roots or explicitly bound as governed evidence families with Evidence Index, mirror, and path-proof linkage.

Transient generator paths (for example, `codex/out/**`) are not authoritative and MUST NOT be indexed. Mirror entries pointing to non-governed paths fail CI.

**Lowercase directories (ASCII only).**

All directories in the repository and application codebase **MUST** use **lowercase ASCII** names. Introducing any mixed-case or upper-case directory name is **non-conforming**. Under governed roots (`docs/**`, `artifacts/**`, `audit/**`), mixed-case directories are a **QA failure**, not cosmetic drift.

This rail applies to **directory names** only (not filenames). Uppercase filenames are allowed unless separately forbidden by canon.

Automated enforcement MUST scan directory names (for example: `find <root> -type d`) rather than file paths (`-type f`).

**Remediation posture.**  
If mixed-case directories exist, treat them as legacy drift and **normalize to lowercase**. Do not copy mixed-case names forward into new work.

**Evidence coupling (same-PR).**  
Any directory rename that affects governed artifact paths **MUST** be accompanied by the required Evidence Index and machine mirror updates (and any affected path-proofs) in the **same PR/commit** as the rename.

**Determinism first.**  
Any change that affects byte identity (serializer path, schema keys, A7 headers, `/internal/version` headers) must include updated parity and idempotence evidence.

**Doc-Delta discipline.**  
All **normative** edits (math/public/acceptance/rails) require a Doc-Delta entry: scope, affected sections, acceptance impact, evidence updates, and freeze-pack effect.

**Evidence synchronization (PR-first).**  
When any golden or artifact path changes, the Evidence Index and mirror **must** be updated in the same PR/commit that changes those items, with a matching entry under the change-management rules in **PF06-Canon-Epic-Process-Guide**.

**Mirror hygiene (merge-blocking).**  
The machine mirror must be canonical JSONL (one trailing LF; unknown keys rejected). Each record must include a `proof_anchor` pointing to a path-proof stored alongside the artifact.  
Field order and sort/join rules live in **PF12-Canon-HDE-Schemas-and-Artifacts**; this document references policy only.

**Editorial vs normative.**  
Stylistic or non-functional rewordings need not be logged. Any change that modifies bytes, tests, or acceptance criteria must be logged via Doc-Delta and reflected in Evidence Index updates.

---

# 1\. Purpose & Single-Home Governance \[Required-Now\]

## 1.1 Purpose \[Required-Now\]

This governance document defines **how the HD Engine is built, validated, and released** under explicit Epic gates.

* Each Epic functions as a **governance gate**: a bounded set of features and acceptance tests that must be fully implemented, validated, and evidenced before the next Epic begins.  
    
* Governance, validation, and operations are inseparable: an Epic **closes** only when its governance and evidence gates pass.  
    
* Supersession rule: a higher-numbered applicable addendum governs only overlapping scope or guidance it explicitly supersedes; unrelated addenda and distinct unsuperseded portions remain authoritative. This document integrates the applicable positions from **PF10-HDE-Build-Notes** and preserves relevant historical context from **PF20-Reference-HDE-Phased Epics**.

This document owns:

* **Acceptance gates (A-gates and Epic gates).**  
    
  * A3 / A4 / A7 enforce determinism, Reader↔CLI parity, and transport correctness.  
      
  * Every Epic uses the same internal criteria: AB↔BA parity, two-run identity, canonical JSON discipline, and A7 transport compliance.  
      
  * Governance and testing during an Epic use the same binary proofs required for release acceptance.


* **Reader transport and A7 policy.**  
    
  * Governs public transport behavior (headers, conditional delivery, caching).  
      
  * Single proof surface: A7 proofs run on a Catalog JSON success route (see Endpoint Catalog in **PF05-Canon-HDE-CLI-API-Vendor-Ref**).  
      
  * The Catalog is internal-only and env-gated per entry; entries not gated for prod are unreachable in production.  
      
  * `/internal/version` is ops-only and excluded from A7; its posture is governed separately (§10.5).  
      
  * Required A7 posture includes, at minimum:  
      
    * Strong quoted ETag on 200\.  
        
    * `Vary: Authorization, Accept-Encoding`.  
        
    * HEAD 200 with validator parity and `Content-Length == len(identity 200 body)`.  
        
    * 304 only after 200, with no body, omitting both `Content-Type` and `Content-Length`.  
        
    * Writers/errors `Cache-Control: no-store` and **no ETag**.  
        
    * Success route non-conditional; encoding invariance (identity stable across accepted `Accept-Encoding` values).


* **Rails and environments (vendor posture).**  
    
  * SAFE-rails model for vendor HTTP: default closed, explicit open conditions, deterministic refusal semantics, and non-PII observability.


* **Public resonance posture (Reader v1).**  
    
  * Public surface is bands-only, numeric-free.  
      
  * Resonance is SR-only (α=1.0).  
      
  * Hysteresis=1 is armed for future XR and is not exposed.  
      
  * Any XR diagnostics, if supported, are CLI-only behind an admin guard (never present on Reader 200).


* **Operations and evidence.**  
    
  * Required evidence classes (parity, idempotence, transport, rails, band-edge, constants).  
      
  * CI hygiene (grep-guards, LF/encoding checks).  
      
  * Evidence Index single-home rule (**PF12-Canon-HDE-Schemas-and-Artifacts**) and requirement that Index updates land in the same PR as artifacts.


* **Release discipline.**  
    
  * Manages freeze-pack identity (`release_id`), immutable packaged-release promotion, exact-artifact rollback, and drift checks.  
      
  * Any frozen-math or manifest canonical-bytes change yields a new `release_id` (pack manifest is canonical JSON with `root:"catalog/"`, `version`, `built_at_utc`, and `files:[{path,sha256,size}]`).


* **Security and privacy.**  
    
  * Enforces the numeric-free public covenant.  
      
  * Keys-only logging; no secrets/PII in logs.  
      
  * Labels and correlation IDs remain bounded and deterministic.


* **Change management.**  
    
  * Defines the Doc-Delta workflow (scope, targets, acceptance, evidence, freeze-pack impact).  
      
  * Mandates that every normative change updates the Evidence Index in the same commit.

## 1.2 Single homes & routing \[Required-Now\]

**Ownership (this document).**  
Governance owns **operational and transport policy** for the HD Engine:

* A-gates (acceptance policy and token semantics).  
    
* Reader transport (headers, conditional delivery, caching).  
    
* Rails posture (enable/disable vendor HTTP).  
    
* Logging/privacy.  
    
* Bench/SLO posture.  
    
* Immutable packaged-release promotion and exact-artifact rollback policy.  
    
* Evidence/CI hygiene policy.

**Titles-only routing (no duplication).**

* **Math and architecture.**  
  Mathematical rules (scoring, thresholds, fixed-point/rounding, preimage definition) and architectural boundaries (engine/adapter/presenter responsibilities) are referenced by title only from **PF01-Canon-HDE-Math-Spec** and **PF02-Canon-HDE-Architecture**; they are not restated here.  
* **Aux Narrative.**  
  Aux Narrative payload and route bytes (examples, endpoint bytes, CLI admin flags) are documented in **PF05-Canon-HDE-CLI-API-Vendor-Ref** and **PF17-Canon-HDE-Narratives-Guide**. This document owns the acceptance matrices and policy carve-outs only (e.g., suppression posture).  
* **Admin bundle & admin surfaces.**  
  The internal **admin bundle builder** (composition of per-person BodyGraphs, compat JSON, narratives, and meta) and the concrete **CLI/HTTP admin bundle surfaces** are defined mechanically and byte-wise in **PF14-Canon-HDE-Mechanics-Guide** and **PF05-Canon-HDE-CLI-API-Vendor-Ref** (titles-only). Governance owns only the **policy** for these admin surfaces: authentication/authorization, logging/audit posture, and the applicable acceptance-token semantics in §2.0.17. Admin bundle bytes are not part of the Reader v1 public contract and are not A7 proof surfaces; they are admin-only internal surfaces.  
* **Serializer/emitter and schemas.**  
  Canonical serializer/emitter rules and public payload schemas are owned by **PF01-Canon-HDE-Math-Spec**, **PF12-Canon-HDE-Schemas-and-Artifacts**, and **PF05-Canon-HDE-CLI-API-Vendor-Ref** and are referenced by title here.

**Change discipline.**

* If a change touches **Math or Architecture**, it must be made in that home and routed here via Doc-Delta.  
* If a change alters **transport/ops** (including admin bundle auth/logging policy), it lands here with updated evidence and pointers, never by duplicating content across documents.

**Auditability.**

* All references to external homes are titles/anchors only.  
* Proofs (goldens, scripts, snapshots) are indexed in the Evidence Index governed by **PF12-Canon-HDE-Schemas-and-Artifacts** and kept in sync with repo changes.

## 1.3 EPIC-011 preservation surfaces \[Required-Now\]

EPIC-011 introduced a **preservation guard** over key public and admin surfaces. Under this Epic, certain contracts are treated as **frozen**:

* Governance and QA may **strengthen proofs and evidence**,  
    
* but **may not change wire contracts** for these surfaces within EPIC-011’s scope.

**Preserved surfaces (names-only).**

* **CLI admin preview (Aux preview).**  
  Wire bytes, stdout/sidecar contracts, and exit-code behavior for CLI admin preview are owned by **PF05-Canon-HDE-CLI-API-Vendor-Ref**. EPIC-011 allows QA and evidence changes only (additional proofs, harnesses), not contract changes.  
    
* **Vendor ingest wire bytes.**  
  Vendor HTTP request/response shapes, paths, and typed error envelopes are owned by **PF05-Canon-HDE-CLI-API-Vendor-Ref**. Governance ensures SAFE rails posture and observability; EPIC-011 does not change vendor wire contracts.  
    
* **Compat JSON surface.**  
  The compat surface used by `showcompat` and other callers is governed by **PF01-Canon-HDE-Math-Spec** and **PF05-Canon-HDE-CLI-API-Vendor-Ref**. EPIC-011 treats this as frozen; only QA evidence around compat (AB↔BA parity, two-run identity) may change.  
    
* **Aux narrative surface.**  
  Narrative packs, text, suppression rules, and Aux routes are governed by **PF17-Canon-HDE-Narratives-Guide** and **PF05-Canon-HDE-CLI-API-Vendor-Ref**. Under EPIC-011, narrative contracts are preserved; QA captures headers, packs, IDs, and transport proofs only.

**Governance stance.**

* Governance may tighten tests, add acceptance tokens, and require new evidence artifacts **without** changing preserved wire contracts.  
    
* Any change to a preserved surface’s contract must be treated as **out of scope** for EPIC-011 and routed through a future Epic. **PF20-Reference-HDE-Phased Epics** supplies historical context only and does not control current planning.

---

# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**

---

## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**

**Single home for governance tokens.** This roster centralizes token semantics; the bytes and tests live elsewhere and are referenced by title only. Other sections must reference §2.0 and must not restate token lists. Supersession: PF10 uses independently scoped numbered addenda; the highest-numbered applicable addendum governs only overlapping or explicitly superseded scope, while unrelated addenda and distinct unsuperseded portions remain authoritative. All token names are case-sensitive.

**Token Registry.** This section is the **Token Registry** for HDE acceptance tokens. Token names and semantics are **owned here**. **HDE-Schemas and Artifacts** mirrors these names and attaches acceptance hints to concrete artifacts; it does **not** change semantics. **HDE-Build Checklist** is strictly **consumer-only**: it lists and groups tokens by phase and Epic but may not introduce new token names. Any new acceptance token must be defined in this section first and then mirrored into **HDE-Schemas and Artifacts** and **HDE-Build Checklist** by title.

**Derived token roster exports (consumer-only).** Repo-generated token-roster exports (for example, `reports/qa_acceptance_tokens.json`) are derived/consumer artifacts and may lag, simplify, or omit PF04 Token Registry details. If a derived export disagrees with §2.0, PF04 governs. Treat export drift as consumer drift and fix the exporter/pipeline; do not mint, rename, or retire acceptance tokens based on derived exports.

**Canonical spelling in derived exports (no alias masking).** Derived token roster exports MUST preserve the canonical token spellings from §2.0. Exports that emit only legacy/alias token names MUST be treated as invalid consumer output; do not “map” aliases to canonical tokens as a substitute for correcting the exporter, because alias-only exports can mask missing canonical tokens.

---

### **2.0.0 Token admission & lifecycle (value-only)**

**Role.** This section defines the governance for admitting new Acceptance Tokens and for maintaining the Token Registry.

**Supersession.** The Token Registry is normative. It overrides informal usage in plans, PRs, and downstream docs.

**Types.** The registry contains:

1. **Acceptance tokens** (gated PASS/FAIL)  
     
2. **Execution harness tokens** (operational invariants for harness behavior)  
     
3. **Non-token markers** (labels that are explicitly not acceptance gates)

**Registry enforcement.** A token name is invalid for acceptance maps/manifests/evidence unless it is (a) registered here (§2.0), or (b) minted as a numbered addendum entry in PF10 (Glow HD Engine Build Notes). Plans may request new tokens via ADR, but those names MUST be clearly marked as requests until the token is minted in PF10 (or registered here).

**Terms (planning usage).** A token is an atomic PASS/FAIL acceptance predicate with a canonical name. A token claim is a plan's commitment to produce governed evidence that proves the token. An obligation is a concrete requirement stated without minting a new token name. Minting is the act of introducing a new token into PF10 addenda and draining it into this registry.

**No token invention.** Plans and acceptance artifacts MUST NOT mint, claim, or require new "guard tokens" unless the token exists in this Token Registry (§2.0) or has been minted as a numbered addendum entry in PF10 (pending drainage into §2.0).

**Guard proof tokens.** Some guard proofs are required deliverables but are not acceptance gates.

* **Evidence-only unless tokenized.** Guard proofs are required deliverables and MUST be mechanically generated and reviewable, but they MUST NOT create new token obligations unless Governance explicitly registers a token name and semantics for that guard proof in §2.0 (or mints it via PF10 addenda pending drainage into §2.0).  
    
* **No token invention.** Plans and acceptance artifacts MUST NOT mint, claim, or require new “guard tokens” unless the token exists in this Token Registry or has been minted as a numbered PF10 addendum pending drainage into §2.0.  
    
* **Future tokenization path.** If a guard proof must become a gated acceptance token, it must be explicitly admitted via governance and added to the registry with clear semantics.

**Retired database-bridge token and proof-label posture.** `DEV_DB_BRIDGE_FALLBACK_OK` is retired from current claimability. `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token historical proof labels only; they are not current bridge, transport, or acceptance predicates.

* No new implementation plan, PR summary, OPS record, QA log, acceptance map, token/evidence matrix, close report, close manifest, or governed evidence row may claim `DEV_DB_BRIDGE_FALLBACK_OK`, bridge availability, bridge parity, bridge consistency, bridge capability, bridge fallback, or successful bridge selection.  
* Historical evidence and historical token references MAY retain their accurate bridge-era names and results. They MUST remain historical, MUST NOT be rewritten merely to remove the retired names, and MUST NOT be relabeled as current evidence or current token satisfaction.  
* Retirement of the bridge does not mint a replacement bridge or direct-transport token. Current direct-only database transport remains an implementation and evidence obligation governed through applicable existing database, environment, evidence-integrity, and test-token semantics.  
* OPS-03 and any other bounded direct-only OPS evidence family do not mint, satisfy, replace, or expand an acceptance token by implication. OPS evidence remains subject to its explicit nonclaims and the general OPS-versus-QA and OPS-versus-acceptance separation rules.  
* Any future acceptance token for a distinct supported database-transport predicate MUST be expressly admitted through this Token Registry or minted by a numbered PF10 addendum before an acceptance artifact may claim it.

**Review-time requests vs close-out claims.** Planning-time requests for new tokens are allowed, but acceptance claims at epic close must reference registered tokens and governed evidence.

**Operational discovery, open-rails, Codex Audit, and OPS evidence non-token posture.** Operational discovery, bounded OPS evidence, PO-authorized open-rails evidence, and read-only repo-reality observations may support planning, implementation, QA design, review, or later-drain supportability, but they do not mint, satisfy, or expand acceptance tokens by themselves. If an operational fact can be safely discovered and recorded without exposing secrets, Governance does not require a new acceptance token merely to permit discovery.

Codex Audit observations and other read-only repo-reality observations may support bounded repo-reality facts when properly labeled, but they do not by themselves prove QA PASS, OPS completion, live vendor truth, PF09 status movement, epic closure, PF-canon drainage, or acceptance-token satisfaction. Governance review blocks only when such evidence is overclaimed as token, acceptance, closure, live-vendor, PF09, OPS-completion, or canon authority.

If a discovery proof, open-rails proof, Codex Audit observation, OPS evidence bundle, or repo-reality proof must become a gated acceptance token, the token must be admitted through this registry or minted in a numbered PF10 addendum before any plan, acceptance map, matrix, closeout artifact, or evidence log claims that token.

**Token claim semantic-fit rule.** Registering a token name does not make that token reusable for every artifact in the same PR, epic, proof family, evidence bundle, or acceptance map. A token may be claimed only where the bound artifact, validator, QA step, or evidence family directly proves the registered token semantics.

Generic privacy, logging, no-payload, no-I/O, canonical-JSON, path-proof, Evidence Index, Machine Mirror, and rails tokens must bind to the exact proof family that proves those predicates. Vendor field-sufficiency snapshots, adapter-contract snapshots, route-policy snapshots, parent-binding logs, nonclaim artifacts, doc-delta records, or acceptance maps MUST NOT claim `VENDOR_NO_PAYLOAD_LOGGING_OK`, `LOGS_KEYS_ONLY_OK`, `BG_PRIVACY_REDACTION_OK`, `NO_EXTERNAL_IO_ON_REFUSAL_OK`, or similar registered tokens unless the artifact itself or its paired validator directly proves the relevant no-payload logging, keys-only logging, privacy-redaction, or no-external-I/O predicate.

If an artifact records only scope, nonclaims, route selection, field sufficiency, adapter mapping, compatibility posture, parent evidence binding, or documentation deltas, it may record those facts without claiming unrelated generic governance tokens. Token arrays, token/evidence matrices, acceptance maps, evidence-index metadata, and closeout-support artifacts must preserve this semantic-fit boundary.

**Command syntax and helper-code non-token posture.** Command syntax, helper-code syntax, heredoc form, rendered escape characters, indentation damage, copied-chat formatting, command literalness, and paste-readiness are not acceptance-token conditions by themselves. Acceptance tokens depend on governed proof, evidence identity, proof target identity, executed-result truth, registered token semantics, and the required evidence family, not on literal plan-command bytes unless the plan or owning PF home explicitly makes exact command bytes the proof target.

A syntax, escape, helper-code, or command-literal issue may affect a token only when it changes or obscures the proof target, evidence family, artifact identity, executed result, rails posture, secret-safety posture, token semantics, PF09 scope, or public/private boundary. A reviewer who claims token impact from syntax or command-literal damage carries the burden to identify the separate non-syntax harm. If no such harm is proven, the issue is an in-flight normalization note, operator caution, caveat, suggestion, or nit, not a token failure.

### **2.0.1 Determinism & identity**

* **TWO\_RUN\_IDENTITY\_OK** — Two serializations of the same inputs produce identical bytes. (Owned: HDE-Math-Spec; HDE-Mechanics Guide; Evidence & Artifacts)  
    
* **COMPOSITE\_ABBA\_IDENTITY\_OK** — AB↔BA fingerprint byte-equality (no vendor flags in composite). (Owned: HDE-Math-Spec; Evidence & Artifacts) **Canonical name.** This is the only canonical acceptance token name for AB/BA composite identity. Any alternate spellings or legacy variants are non-canonical and MUST NOT appear as acceptance tokens in Epic Plans, acceptance maps, or token/evidence matrices. If an epic inherits legacy wording from a doc, the plan may include a one-line clarification (“legacy name → canonical COMPOSITE\_ABBA\_IDENTITY\_OK”), but the claimed token name remains canonical. Any proposal to introduce a new AB/BA identity token name is prohibited unless routed through ADR \+ conflict check \+ Governance Doc-Delta.  
    
* **JSON\_CANONICAL\_CHECK\_OK** — Canonical JSON everywhere: UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted wherever required. **Canonical name.** Any alias or near-match (for example `CANON_JSON_OK`) is non-canonical and MUST NOT appear as an acceptance token in Epic Plans, acceptance maps, token/evidence matrices, or step-log claims. (Owned: HDE-Mechanics Guide; Evidence & Artifacts)  
    
* **PREIMAGE\_RECOMPUTE\_OK** — Strip `idempotence_hash`, canonicalize the preimage (as defined in HDE-Math-Spec), recompute `sha256(preimage_bytes)`, and match the published hash; evidence includes recompute logs/scripts and mirror records under determinism pins. (Owned: HDE-Math-Spec; Evidence & Artifacts)

**DETERMINISM\_ENV\_PINS\_OK** — All **determinism-sensitive suites** (at minimum: serializer/idempotence proofs, AB↔BA identity, evidence ordering/orientation demos, and other invariance tests named in HDE-Mechanics Guide and Glow QA Guide) MUST run under the **closed determinism env pins**  
`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`  
as enforced by the canonical determinism env helper and CI rails harness.

**Canonical evidence surface (single valid binding).**  
`DETERMINISM_ENV_PINS_OK` MUST be satisfied only by the canonical governed log:

* `audit/gates/determinism/env_pins.log`  
    
* `audit/gates/determinism/env_pins.log.path_proof.txt`

`DETERMINISM_ENV_PINS_OK` MUST NOT be bound to `artifacts/proofs/env_pins.txt` (or any other similarly named env-pins artifact).

**Ledger \+ indexing parity (mechanical).** When this token is claimed, all acceptance ledgers MUST reference `audit/gates/determinism/env_pins.log`, and parity MUST be correct:

* token\_evidence\_matrix references `audit/gates/determinism/env_pins.log`  
    
* `docs/evidence/INDEX.json` points the determinism env pins artifact\_key to `audit/gates/determinism/env_pins.log`  
    
* `artifacts/evidence_index.jsonl` mirrors that exact discovered\_physical\_path and uses `audit/gates/determinism/env_pins.log.path_proof.txt` as proof\_anchor

Any deviation is a mechanical blocker. The binding must be corrected, not interpreted.

**Epic roster tokens (determinism suites; composite).**  
These tokens may appear in epic acceptance rosters and QA artifacts as **composite** determinism claims. They do not replace the canonical A-gate token names already defined in this section.

* **TK-ENGINE-SERIALIZER\_COMPOSER\_DETERMINISM\_2RUN** — The deterministic serializer/composer proof suites used for acceptance demonstrate two-run byte identity under the canonical determinism env pins. Minimum proof: a two-run byte-compare artifact and its backing test/harness are linked in the token/evidence matrix.  
    
* **TK-ENGINE-SERIALIZER\_COMPOSER\_DETERMINISM\_ABBA** — The deterministic serializer/composer proof suites used for acceptance demonstrate AB↔BA byte identity under the canonical determinism env pins. This is not a synonym for `COMPOSITE_ABBA_IDENTITY_OK`; where AB↔BA composite identity is claimed as a governance token, the canonical name remains `COMPOSITE_ABBA_IDENTITY_OK`.  
    
* **TK-ENGINE-SERIALIZER\_COMPOSER\_DETERMINISM\_CLOSED\_RAILS** — The determinism-sensitive suites used for acceptance run under the canonical closed determinism env pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and bind to the canonical env-pins evidence surface defined in `DETERMINISM_ENV_PINS_OK`.

---

### **2.0.2 Internal-ops identity (/internal/version)**

* **INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK** — `GET /internal/version` 200 uses `Content-Type: application/json; charset=utf-8`. (Owned: Governance; Mechanics Guide)  
* **INTERNAL\_VERSION\_HEAD\_PARITY\_OK** — `HEAD /internal/version` 200 mirrors GET validators (no body). (Owned: Governance; Mechanics Guide)  
* **INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK** — `If-None-Match` / `If-Modified-Since` are ignored; success uses 200 (never 304). This token name is canonical and non-aliasable: any other name intended to mean “conditionals return 200 and never 304” (including `INTERNAL\_VERSION\_COND\_200\_NO\_304\_OK`) is non-canon and MUST NOT be emitted or required in acceptance artifacts. (Owned: Governance; Mechanics Guide)  
* **INTERNAL\_VERSION\_NO\_ETAG\_OK** — No `ETag` on `GET`/`HEAD`. (Owned: Governance; Build Notes — Prod QA)  
* **INTERNAL\_VERSION\_NO\_STORE\_OK** — `Cache-Control: no-store` on `GET`/`HEAD`. (Owned: Governance; Build Notes — Prod QA)

**Epic roster tokens (/internal/version; composite).**  
These tokens may appear in epic acceptance rosters as **composite** claims over the `/internal/version` invariants and evidence bundle governed in §10.5 and Appendix D.6.

* **TK-SERV-PLATFORMS\_INTERNAL\_VERSION\_SURFACE** — A governed `/internal/version` capture \+ validation exists and is auditable: the canonical `/internal/version` evidence bundle is produced under the governed repo paths and is indexable/mirrored per the evidence rules.  
    
* **TK-SERV-PLATFORMS\_INTERNAL\_VERSION\_HEADERS\_OK** — `/internal/version` headers and caching invariants pass, including: `Cache-Control: no-store` present; `Content-Type: application/json; charset=utf-8` present (GET↔HEAD parity where applicable); `ETag` absent; `Last-Modified` absent; HEAD parity expectations satisfied; conditionals ignored (200, never 304).  
    
* **TK-SERV-PLATFORMS\_INTERNAL\_VERSION\_CANONICAL\_BYTES\_OK** — `/internal/version` body bytes are canonical and fixed-schema: exactly the six identity keys in the fixed order, UTF-8 (no BOM), compact, LF-terminated, and validated by the `/internal/version` proof surface invariants in §10.5.  
    
* **TK-SERV-PLATFORMS\_INTERNAL\_VERSION\_COUPLED\_TO\_RELEASE\_ID** — `/internal/version` identity is coupled to release identity: the `release_id` field in `/internal/version` matches the canonical freeze-pack `release_id` evidence, and the coupling verification is recorded in the governed coupling proof log for this surface (see §10.5).

*Naming cleanup.* The `INTVER_*` aliases are deprecated in favor of `INTERNAL_VERSION_*`. Use only the canonical names above going forward.

---

### **2.0.3 Reader A7 (Catalog JSON success; prove on the Endpoint Catalog)**

* **ENDPOINTS\_CATALOG\_OK** — Catalog of JSON success routes is present (titles-only in CLI/API Vendor Ref) and includes A7 eligibility metadata for A7 proof binding. (Owned: CLI/API Vendor Ref)  
    
* **ENDPOINTS\_CATALOG\_INTERNAL\_OK** — Catalog is internal-only; not a client contract. (Owned: Governance; CLI/API Vendor Ref)  
    
* **ENDPOINTS\_CATALOG\_ENV\_GATE\_OK** — Each entry declares an env gate; non-prod entries are unreachable in prod. (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_GET\_QUOTED\_ETAG\_OK** — `GET` 200 has strong, quoted ETag (identity over LF-terminated body; pre-compression). (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_HEAD\_PARITY\_OK** — `HEAD` 200 mirrors 200 validators (no body). (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_304\_OMITS\_CT\_CL\_OK** — 304 only after prior 200; omits both `Content-Type` and `Content-Length`. (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_ENCODING\_INVARIANCE\_OK** — For the same canonical body, identity (ETag) and effective `Content-Length` are stable across accepted encodings. (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_VARY\_AUTH\_AE\_OK** — `Vary: Authorization, Accept-Encoding` present. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_200\_CTYPE\_JSON\_UTF8\_OK** — `Content-Type: application/json; charset=utf-8` on 200\. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_200\_CACHECTL\_OK** — `Cache-Control` on 200/HEAD is policy-compliant. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_VARY\_ACCEPT\_ENCODING\_OK** — `Vary` includes `Accept-Encoding`. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_VARY\_AUTHORIZATION\_OK** — `Vary` includes `Authorization`. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_304\_NO\_CL\_OK** — 304 omits `Content-Length`. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_304\_NO\_CTYPE\_OK** — 304 omits `Content-Type`. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_HEAD\_ETAG\_MATCH\_OK** — HEAD validators (including ETag) match GET. (Owned: Governance; CLI/API Vendor Ref)  
    
* **READER\_HEAD\_CL\_MATCH\_OK** — HEAD `Content-Length` equals identity 200 body length. (Owned: Governance; CLI/API Vendor Ref)  
    
* **A7\_TRANSPORT\_PROOF\_OK** — Capture one full A7 proof set for a cataloged route (mechanically generated; gated behind an explicit flag). (Owned: CLI/API Vendor Ref; Evidence & Artifacts)

*Equivalence notes (titles-only).*

* `A7_304_OMITS_CT_CL_OK` ≡ (`READER_304_NO_CTYPE_OK` ∧ `READER_304_NO_CL_OK`)  
    
* `A7_VARY_AUTH_AE_OK` ≡ (`READER_VARY_AUTHORIZATION_OK` ∧ `READER_VARY_ACCEPT_ENCODING_OK`)

---

### **2.0.4 Aux Narrative transport (success \+ suppression; prove on Endpoint Catalog)**

*Tokens (Aux surface; names-only).*

* **NARR\_200\_TEXT\_OK**  
    
* **NARR\_SUPPRESSED\_NO\_ETAG\_OK**  
    
* **NARR\_VARY\_AUTH\_AE\_OK**  
    
* **AUX\_CANON\_ALIAS\_PARITY\_OK**

*Notes.* These replace legacy `AUX_*` names; one-release grace for `AUX_*` may be handled in HDE-Build Checklist. Aux HEAD/304 tokens are out-of-scope for EPIC-010; A7 remains Catalog-only.

---

### **2.0.5 Writers / refusal & ops posture (rails)**

* **WRITERS\_OPTIONS\_204\_NO\_BODY\_OK** — Writers’ `OPTIONS` returns 204 (no body). Never emit body/ETag/Vary/compression; HEAD 405 remains strict with `Content-Length: 0`. (Owned: Governance)  
    
* **ERROR\_CTYPE\_JSON\_UTF8\_OK** — Refusal responses use `Content-Type: application/json; charset=utf-8`. (Owned: Governance)  
    
* **NO\_CONTENT\_ENCODING\_OK** — No `Content-Encoding` on refusal. (Owned: Governance)  
    
* **NO\_EXTERNAL\_IO\_ON\_REFUSAL\_OK** — Refusal path performs no external I/O. (Owned: Governance)  
    
* **PF04\_LOG\_ALLOWLIST\_009\_OK** — Every request-scoped closed-rails refusal log contains exactly the seven-key allow-list `{at, route, status, duration_ms, idempotence_hash, release_id, correlation_id}` and no additional key. Applicable fixtures prove that `correlation_id` is present, non-empty, bounded, format-valid, and matches the carrier emitted for the same request; missing or malformed inbound values are replaced safely without echoing or logging the raw value; the value is not derived from personal or mathematical inputs, does not enter or alter a public or refusal body, `idempotence_hash`, `ETag`, Human Design computation, or Magic-10 result, and is not a metric label; no payload, header value, secret, PII, birth data, or free text is logged; and the refusal still performs no external I/O. General correlation validation and propagation policy remains in §7.2; this token does not define carrier bytes or header casing. (Owned: Governance)  
    
* **REFUSAL\_ROUTE\_PINNED\_OK** — Canonical refusal probe route is `/ops/rails/refusal` (GET/POST equivalent; OPTIONS/HEAD per matrix). (Owned: Governance)  
    
* **ERROR\_JSON\_CANON\_OK** — Typed error bodies (Reader and CLI) are canonical and numeric-free: they are emitted by the single presenter/emitter as UTF-8 JSON (no BOM), with sorted keys, compact separators, and exactly one trailing LF. Error bodies MUST conform to the typed error envelope policy (no PII, no secrets, no vendor payload echo). This token covers the **error body bytes**, complementing `ERROR_CTYPE_JSON_UTF8_OK` (error/refusal header posture). (Owned: Governance; HDE-CLI-API-Vendor-Ref; Evidence & Artifacts)  
    
* **ERROR\_TOKEN\_MAP\_OK** — Typed error `code` values are drawn from a single governed error token map shared by Reader and CLI surfaces. Unknown or unmapped codes MUST fail closed (no ad-hoc new codes). Changes to the error token map are normative and land only via Doc-Delta with updated evidence/index/mirror linkage. (Owned: Governance; HDE-CLI-API-Vendor-Ref; Evidence & Artifacts)

*Refusal proof artifact (shape & linkage).*

* **OPS\_REFUSAL\_FILE\_FORMAT\_OK**  
    
* **OPS\_REFUSAL\_HEADERS\_OK**  
    
* **OPS\_REFUSAL\_BODY\_OK**  
    
* **OPS\_REFUSAL\_MIRROR\_LINK\_OK**

---

### **2.0.6 Evidence & indexing**

**Single-home meaning (clarification).**  
Evidence artifacts MAY be stored across multiple governed roots. “Single-home” refers to the Evidence Index (human) and machine JSONL mirror being the single authoritative binding between artifact keys and repo paths, with one co-located `*.path_proof.txt` per governed artifact.  
Evidence layout is evaluated by index/mirror/path-proof completeness and coherence (plus same-PR coupling and path validation), not by whether files live in a single directory.

* **EVIDENCE\_INDEX\_UPDATED\_OK** — Human Evidence Index updated in the same change as artifacts. (Owned: Governance; Evidence & Artifacts)  
    
* **EVIDENCE\_INDEX\_MIRROR\_OK** — Machine JSONL mirror (records-only; sorted keys; one LF) present and valid. (Owned: Evidence & Artifacts)  
    
* **MACHINE\_MIRROR\_UPDATED\_OK** — The `index.machine_mirror` self-record in the machine JSONL mirror exists and is current: its `sha256` and `size_bytes` fields match the canonical body of `artifacts/evidence_index.jsonl`. (Owned: Evidence & Artifacts)  
    
* **EVIDENCE\_PATHS\_VALIDATED\_OK** — Evidence-index bindings are safe, contained, and resolvable. The canonical validator is `tools/evidence/validate_evidence_paths.py`, which loads `artifacts/evidence_index.jsonl` and MUST fail closed (non-zero) on the first violation. It MUST validate, for every mirror record:  
    
  * the JSONL line parses as a JSON object (dict); non-object lines are rejected,  
  * `discovered_physical_path` exists on disk at validation time and is repo-relative (no absolute paths),  
  * traversal segments are forbidden (`..` MUST NOT appear as a path segment),  
  * resolving the path against the repo root MUST NOT escape the root (out-of-root resolved paths are rejected),  
  * the validator runs under the closed-rails determinism env tuple (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC); missing pins are a validation failure.  
  * Human↔machine parity remains 1:1, and each governed record remains coupled to a co-located path-proof transcript (see `EVIDENCE_PATH_PROOFS_OK`). (Owned: Governance; Evidence & Artifacts)


* **CANONICAL\_JSON\_GATE\_UPDATED\_OK —** The canonical JSON gate coverage has been updated when the governed JSON surface changes. At minimum: the gate’s canonical outputs under `audit/gates/json_gate/canonical/` are refreshed to reflect the current checked target set, and any legacy-named summary outputs under `audit/gates/canonical_json/` that are still produced are also refreshed. (Owned: Governance; Evidence & Artifacts)  
    
* **CANONICAL\_JSON\_GATE\_PASSED\_OK —** The canonical JSON gate run passes for the current build, producing the canonical outputs under `audit/gates/json_gate/canonical/` and recording pass status for each checked target in the gate logs and structured record. (Owned: Governance; Evidence & Artifacts)  
    
  * When the canonical JSON gate run still produces more than one governed canonical-JSON family, `CANONICAL_JSON_GATE_PASSED_OK` requires same-change coherence across the full still-produced set: the authoritative family under `audit/gates/json_gate/canonical/` and any legacy family under `audit/gates/canonical_json/` that remains produced MUST both be present before and after the run, and the canonical gate writer MUST exit `0`.  
  * A successful writer exit alone is insufficient if any still-produced governed family disappears, is omitted from the run, or is no longer surfaced as a governed family in the same change.


* **EVIDENCE\_PATH\_PROOFS\_OK** — For every governed artifact indexed in the machine mirror, a co-located path-proof file exists and validates: each mirror record’s `proof_anchor` resolves to a `*.path_proof.txt` stored alongside the artifact, and the proof’s structured fields match the indexed artifact’s canonical bytes.  
    
  * Minimum required fields in each `.path_proof.txt`:  
      
    * `path` (repo-relative path to the artifact)  
        
    * `size_bytes` (byte length)  
        
    * `sha256` (hex digest of artifact bytes)  
        
    * `mtime_utc` (artifact mtime in UTC)  
        
    * `produced_at_utc` (proof capture time in UTC)

    

  * Additional fields MAY appear when required for provenance (for example orientation metadata), but MUST be deterministic and MUST NOT contradict the required fields.  
  * Missing, mismatched, or stale path-proofs **fail CI**. (Owned: Evidence & Artifacts; Governance)


* **`CI_CHECK_FINAL_LF_OK`** — All governed evidence artifacts and mirror lines are LF-terminated (exactly one trailing LF). The canonical gate wrapper is `tools/evidence/check_lf_endings.py`, which MUST run `ci/checks/check_final_lf.sh` under the closed-rails determinism env tuple (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) and exit non-zero on the first violation. Operator and acceptance artifacts MUST invoke it either:  
    
  * as direct execution: `tools/evidence/check_lf_endings.py`, or as an explicit interpreter invocation: `python tools/evidence/check_lf_endings.py`. (Owned: Evidence & Artifacts; Build Notes)


* **CI\_CHECK\_MIRROR\_SCHEMA\_OK** — Mirror records pass schema/role/field-order checks (unknown-key rejection). The retained validator path is `ci/checks/check_mirror_schema.sh`; the file is Python, and the `.sh` suffix is legacy path identity, not an interpreter declaration. The validator reads fixed input `artifacts/evidence_index.jsonl`, accepts no caller-selected mirror path, and MUST be run from the repository root.  
    
  * Supported invocations are `python ci/checks/check_mirror_schema.sh` and direct execution as `ci/checks/check_mirror_schema.sh` when Git executable mode and shebang handling are guaranteed. A Python harness SHOULD use its active interpreter with the equivalent of `[sys.executable, "ci/checks/check_mirror_schema.sh"]`.  
  * `bash ci/checks/check_mirror_schema.sh` and `sh ci/checks/check_mirror_schema.sh` are invalid. New plans, operator instructions, and harnesses SHOULD omit the unused mirror operand; its presence does not establish caller-selected input. A shell-parser failure or a missing-mirror result produced outside the repository root is an invocation or locus defect, not a Mirror-schema finding; rerun the supported command from the repository root and preserve the actual transcript.  
  * Any future migration to a `.py` path is an intentional compatibility change. It MUST introduce and validate the new entrypoint, update all active callers and current canon references, preserve historical evidence and transcripts, preserve both supported legacy call shapes during transition, rerun the owning closed-rails Mirror, Evidence Index, path, hash, and final-LF gates, and define an explicit deprecation and removal point. The legacy file MUST remain Python-compatible until explicit-Python callers have been drained or another compatibility mechanism preserves them. (Owned: Evidence & Artifacts; Build Notes)


* **EVIDENCE\_INDEX\_HASH\_OK** — Human index hash sentinel present and gating merges. (Owned: Governance; Evidence & Artifacts)  
    
* **SNAPSHOT\_HEADER\_LOWERCASE\_OK** — Stored header snapshots use lower-case header names; norm enforced by schema rules in HDE-Schemas and Artifacts. (Owned: HDE-Schemas and Artifacts)  
    
* **SANITY\_PIPELINE\_OK** — A closed-rails sanity pipeline entrypoint (`tools/evidence/run_sanity_pipeline.py`) **must** run and succeed as a single, deterministic orchestration of core governance checks (at minimum: serializer/idempotence invariants, determinism env pins checks, CLI serializer guards, evidence ordering/orientation checks, and PF12 evidence skeleton checks) under the canonical env tuple `SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC`. The pipeline writes a governed sanity log at `audit/gates/sanity_pipeline/sanity_pipeline.log` with a stable, canonical shape (first line begins with the canonical header prefix `run:sanity-pipeline`, one `env:` line with sorted pins, one `check <name>:OK|FAIL` line per step in a fixed order, and a final `summary:PASS|FAIL` line; no timestamps or env-dependent noise) and exits non-zero on the first failure. Evidence for this token consists of: (a) the sanity log and its co-located path-proof, (b) matching entries in `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` keyed by a reserved `artifact_key` for the sanity pipeline, and (c) a CI job that invokes the sanity pipeline under closed rails and is merge-gating for engine releases. PF04 owns the governance semantics and token; schemas, artifact field sets, and the QA token wiring live in **HDE-Schemas & Artifacts**, **Glow QA Guide**, and **HDE-Build Checklist** (titles-only).

**Clarifications (evidence integrity; BN 8.5.3 Drain A19-22).**  
These clarifications do not introduce new tokens. They make existing evidence tokens concrete for common drift failures.

1. **Human index and hash sentinel are governed artifacts with governed path-proofs.**  
   The following files are governed and MUST each have a co-located path-proof transcript:  
   * `docs/evidence/INDEX.json` and `docs/evidence/INDEX.json.path_proof.txt`  
   * `docs/evidence/INDEX.sha256` and `docs/evidence/INDEX.sha256.path_proof.txt`  
2. When either `INDEX.json` or `INDEX.sha256` changes bytes, its `*.path_proof.txt` MUST be regenerated in the same PR as the byte change. Stale or mismatched `INDEX.*.path_proof.txt` is a hard failure under the existing evidence/path-proof tokens in this section.  
3. **Machine mirror self-record must reflect the whole mirror file bytes.**  
   The `index.machine_mirror` self-record must represent the current `artifacts/evidence_index.jsonl` file, and its `sha256` and `size_bytes` must match the canonical bytes of the whole mirror file (file-bytes basis, not a “row-body” basis). Its `proof_anchor` must point to a co-located path-proof for the mirror file.  
4. **Remediation posture for evidence drift (merge-blocking).**  
   If any governed artifact’s `*.path_proof.txt` (including the INDEX path-proofs above) disagrees with the on-disk artifact bytes (sha256 or size), treat it as a mechanical blocker. Remediation is to regenerate evidence via the canonical evidence tooling (for example `tools/evidence/update_evidence_index.py` and its `--check` mode), not to hand-edit path proofs or machine mirror rows. When the same generation flow still produces more than one governed canonical-JSON evidence family, remediation and closeout MUST treat every changed still-produced family in that generation scope as in-scope. This includes any legacy-named canonical-JSON outputs that remain produced alongside the authoritative family. Closeout for a canonical-JSON-gate or evidence-indexing row may be stated only when the changed governed families in scope have been refreshed coherently in the same run, including their co-located `*.path_proof.txt` companions and any required index or mirror updates for changed artifacts. A green authoritative subfamily is insufficient if another changed still-produced family remains stale, unindexed, unmirrored, or missing current companion proofs.  
5. **Chronology correctness (produced\_at and proof timestamps)** These are clarifications of existing evidence tokens; no new tokens are introduced.  
* **No backdating.** A record MUST NOT claim an earlier `produced_at_utc` or proof timestamp for an artifact whose bytes were created or modified later; that is treated as an integrity failure.  
* **Proof capture is post-artifact (expected).** It is normal for a `*.path_proof.txt` transcript’s `produced_at_utc` (and related proof timestamps) to be later than the governed artifact’s filesystem `mtime`/`mtime_utc`; the proof is captured after file production. This is not “contradictory chronology.”  
* **Index family included.** If an `audit/**/_index/evidence_index.json` is used for acceptance, it is governed by `EVIDENCE_INDEX_PRESENT_OK` and its chronology fields apply.  
* **Acceptance artifacts included.** If an epic’s acceptance artifacts bind to this report as decisive evidence, the artifact MUST follow the evidence skeleton (path-proof, evidence-index update, etc.).  
* **Failure posture (merge-blocking).** If these fields are stale or contradictory (for example, a changed artifact whose proof timestamps or mirror `produced_at_utc` imply a prior production context), the merge is blocked until corrected (see §2.0.5 and **PF12-Canon-HDE-Schemas-and-Artifacts**).  
6. **Predicate-bound PASS for governed evidence generators.** A governed evidence generator, proof writer, or review harness MUST NOT emit `PASS`, an integrity-success signal, or any `*_OK`\-claiming record for a parity, identity-hash, canonical compare, path-proof, evidence-indexing, or binding family unless every decisive predicate for that family is evaluated against the current generated artifacts in the same run and passes. Parsed-object equality alone is insufficient when byte identity is the invariant; regex-only validation of a hash string is insufficient when the claim is that the hash matches the current artifact or preimage; a top-level binding status is insufficient when a linked canonical compare, parity, identity, index, or mirror predicate can fail independently. Required predicates MUST use byte-level comparison, recomputation, schema or canonical checks, and mirror or path-proof binding as applicable to the claimed evidence family.  
* **Final-artifact regeneration after generator changes.** If evidence-generator logic, predicate wiring, or PASS derivation changes, the final governed artifacts for that evidence family MUST be regenerated from the final logic path before acceptance may rely on them. A stale artifact produced by earlier generator logic is not sufficient proof after remediation, even if the generator code itself has been corrected.  
* **False-positive regression coverage for governed evidence generators.** When a governed evidence generator, proof writer, or review harness is corrected because it could emit `PASS` without evaluating a decisive predicate, the remediation MUST include a regression check that exercises the failure path for the omitted predicate. A PASS-path-only test is insufficient after a false-positive PASS defect. The regression check MUST fail the generated artifact or harness result when the decisive predicate fails and MUST prove that the top-level `PASS` or integrity-success signal is derived from the predicate set.  
* **Generated proof-family fail-closed coverage.** When a governed evidence generator, proof writer, or review harness produces or validates more than one generated proof family for an epic, a cross-family PASS claim MUST be held at `TOOLING_BLOCKED` or equivalent until every generated proof family used by the epic has explicit fail-closed proof coverage. Remediation MAY add missing fail-closed checks and rerun the affected suite when the work remains bounded to proving the approved evidence families. A PASS claim MUST NOT be issued while any generated proof family remains unproven for fail-closed behavior.  
* **Generated-evidence freshness before indexing.** When a governed evidence generator produces artifacts that are later indexed, mirrored, hashed, path-proven, or used as acceptance evidence, the governing pipeline or evidence run MUST execute the generator and its check mode before evidence-updater update or check steps rely on those artifacts. Index, mirror, hash, or path-proof checks alone are insufficient when the generator itself was not run or checked against the current source inputs in the same governed run. A PASS, acceptance, supportable-status, or PF09 supportability claim MUST show that the final generated artifacts were produced or checked before the evidence index, Machine Mirror, hash sentinels, path proofs, or closeout-support statements were used as proof.  
* **Closed-rails certification for governed evidence generators.** A governed evidence generator, proof writer, or review harness that claims closed-rails, no-live-call, deterministic provider, or provider-outcome evidence MUST enforce the closed determinism env tuple before emitting or certifying the artifact family. At minimum, that means `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC` are verified before check/write certification for the claimed closed-rails family. If the required rails or determinism pins are missing, open, ambiguous, or contradictory, the generator or harness MUST fail closed before issuing `PASS`, supportable-status language, or any integrity-success signal. A negative open-rails or network-enabled refusal case is required when the remediated defect class was that the generator could certify closed-rails evidence while rails were open.  
7. **Bounded evidence-refresh side effects.** Evidence-tool side effects outside the primary PR slice MAY be accepted only when they are produced by the canonical evidence tooling in the same coherent run, remain under existing governed artifact families, have current co-located path-proofs and required index or mirror updates, are explained as proof-refresh or updater-convergence side effects, and do not create new runtime scope, public-contract surface, route, flag, token, or artifact family obligation. Unexplained or unvalidated side effects remain evidence drift and MUST NOT be used to support acceptance or PF09 status posture.  
   1. **Classification content.** When an evidence updater, generator, or proof writer refreshes governed proof companions or corresponding Machine Mirror rows outside the direct target family, the run evidence MUST name each refreshed family, each affected proof-companion path, each affected artifact key, and each affected discovered path.  
   2. **Allowed classification values.** Each outside-family refresh MUST be classified as exactly one of `expected updater convergence`, `required dependency refresh`, or `unexpected drift`. Unclassified outside-family proof churn is non-conforming until classified or removed.  
   3. **Fail-closed acceptance.** A PASS, acceptance, supportable-status, or closeout-support claim MUST NOT rely on a classified side effect unless every classified side-effect path exists, every proof companion validates against its target, and every classified Machine Mirror row matches the expected artifact key, proof anchor, sha256, and size.  
   4. **Strict check-mode posture.** For self-generated governed artifacts, non-check generation MAY avoid write-time self-hash recursion, but check mode MUST validate final Machine Mirror sha256 and size bindings for every affected row before the evidence family may report PASS.  
8. **Evidence-family path isolation.** A governed evidence generator, updater, or PR slice MUST NOT overwrite, reuse, or repurpose another governed evidence family’s artifact paths to prove a different surface, route, schema, or acceptance claim. If vendor evidence, DB-bridge evidence, writer evidence, topology evidence, or any other governed family needs its own proof surface, it MUST use a distinct governed artifact family and be bound through the Human Evidence Index, Machine Mirror, and path-proof discipline.  
9. **Path-collision remediation posture.** If a generator or updater writes a governed artifact to a colliding path, remediation MUST move the new evidence to its own governed family or restore the original family’s path and schema, refresh the affected Index and Mirror rows, refresh co-located path proofs, and mark superseded colliding rows or artifacts as superseded or filtered according to the owning evidence tooling. A path-collision fix MUST NOT be summarized as PASS until the final Index and Mirror bindings point to the intended families and the shared family is no longer overwritten.  
10. **Acceptance-boundary metadata and nonclaim testability.** Any acceptance map, token/evidence matrix, viability log, OPS evidence binding log, evidence-loop closure artifact, or closeout-support artifact that supports Governance or acceptance posture MUST make its governance metadata and nonclaims testable when the artifact is machine-readable or mechanically generated. At minimum, the artifact family must preserve the correct epic identity, approved token set, forbidden local or vendor-specific token names, slice roles, evidence paths, and nonclaims for QA PASS, OPS completion, PF09 status movement, epic closeout, runtime conformance, public Reader scope, public route or flag expansion, and PF-canon drainage.

A narrative statement that nonclaims exist is insufficient when the artifact is machine-readable and the nonclaims can be checked mechanically. If a nonclaim cannot be mechanically verified, the artifact MUST state the nonclaim precisely and explain why mechanical verification is unavailable. Evidence-loop closure is supportable only when the same governed proof chain verifies Human Index presence, Machine Mirror presence, current sha or checksum binding, co-located path proof, and payload existence for the relevant evidence family.

---

### **2.0.7 Freeze-Pack & manifest**

* **PACK\_ROOT\_PINNED\_OK** — `root: "catalog/"` pinned. (Owned: Evidence & Artifacts — Manifest)  
    
* **PACK\_MANIFEST\_NO\_SELF\_LISTING\_OK** — Root manifest does not list itself or sidecars. (Owned: Evidence & Artifacts — Manifest)  
    
* **MANIFEST\_SHA256\_HEX64\_OK** — Each entry `sha256` is lowercase 64-hex of canonical bytes. (Owned: Evidence & Artifacts — Manifest)  
    
* **MANIFEST\_FILE\_EXISTS\_OK** — Each listed file exists at the path. (Owned: Evidence & Artifacts — Manifest)  
    
* **MANIFEST\_PATH\_ASCII\_SORT\_OK** — `files[]` ASCII-sorted by path. (Owned: Evidence & Artifacts — Manifest)  
    
* **RELEASE\_ID\_FROM\_MANIFEST\_OK** — `release_id` derives only from the manifest. (Owned: Evidence & Artifacts — Manifest)  
    
* **RELEASE\_ID\_RECOMPUTE\_OK** — Registered, but not currently claimable. Its former current-equality predicate against frozen historical checked-in identity evidence is superseded and MUST NOT be applied. Frozen historical identity artifacts MUST NOT be refreshed or relabeled as current. The token supplies no HDE-EPIC038 closure claim, records neither PASS nor FAIL, and MUST NOT be relied on by any future epic or closeout process until a separate canonical decision redefines, replaces, or retires it without reclassifying frozen historical evidence. (Owned: Governance)  
    
* **TWO\_RUN\_IDENTITY\_OK** — Two-run identity of the recompute step. (Owned: Evidence & Artifacts — Manifest)  
    
* **BAND\_MAX\_INCLUSIVE\_OK** — Band threshold maxima are inclusive-high and are validated against the current frozen threshold source before any public or admin band claim is accepted. Evidence MUST show the active maxima, the band order, and the same-change index and mirror bindings for the governed threshold artifact family when those artifacts change. (Owned: HDE-Math-Spec; HDE-Schemas & Artifacts; Evidence & Artifacts)  
    
* **BAND\_EDGE\_GOLDENS\_OK** — Band-edge golden evidence proves the governed threshold edges at `24`, `49`, `74`, and `100`, including the \+1 transitions for Cool→Open, Open→Warm, and Warm→Glow, and proves that `100` maps to Glow. Evidence MAY include band-edge binding logs and compact diff artifacts, but any claim of this token MUST be tied to current PASS evidence and governed index/mirror/path-proof bindings. (Owned: HDE-Math-Spec; HDE-Schemas & Artifacts; Evidence & Artifacts)

---

### **2.0.8 CLI/SDK parity harness**

* **CLI\_READER\_PARITY\_OK** — When CLI produces **Reader v1 parity bytes** (the numeric-free Reader v1 success envelope), those bytes MUST be byte-identical to the Reader v1 HTTP body for the same normalized inputs and environment (single emitter; exactly one trailing LF). Reader v1 parity bytes are produced via the CLI’s `--dump-reader` sidecar (bytes and sidecar contract live in **HDE-CLI-API-Vendor-Ref**). This token does **not** assert that `showcompat` stdout equals Reader v1 bytes. (Owned: Governance; CLI/API Vendor Ref)  
    
* **CLI\_NO\_ALT\_JSON\_OK** — `hdctl showcompat` emits only the canonical JSON compatibility envelope on stdout; legacy or alternative JSON shapes are disabled on this path. The compatibility envelope is an admin/test surface and may include numeric scores/weights. (Owned: Governance; CLI/API Vendor Ref)  
    
* **CLI\_SHOWCOMPAT\_CANON\_OK** — `hdctl showcompat` uses the same canonical emitter as Reader/aux for compatibility outputs; no ad-hoc serializers are permitted on this path. (Owned: Governance; CLI/API Vendor Ref)  
    
* **CLI\_STDOUT\_LF\_OK** — `hdctl showcompat` stdout is canonical: UTF-8, BOM-free, and terminated with exactly one LF. (Owned: Governance; Evidence & Artifacts)  
    
  * **CLI installability and conformance proof (normative).**  
    * When CLI installability or CLI help and version conformance is used as acceptance evidence, the proof posture MUST be positive and deterministic. Skipped, negative, or placeholder-only console-entrypoint posture does not satisfy installability proof.  
    * Governed CLI conformance evidence MAY cover module and console version or help surfaces, help and argument-policing captures, and deterministic sample semantics when those surfaces are in scope for acceptance. When such surfaces are claimed, the emitted proof and any derived metadata MUST be mutually coherent.  
    * Installability and console proof MUST NOT depend on ambient host `PATH` or other unpinned host-shell state. Any claimed console proof MUST resolve from the governed execution context used to produce the evidence.  
    * When both module and console surfaces are claimed, their captured version and help posture MUST remain single-sourced in meaning and MUST NOT be internally conflicting across the governed evidence family.  
    * If sample or sampler semantics are part of the governed CLI conformance surface, the emitted proof MUST preserve stable seed semantics, stable candidate-order semantics, and two-run equality when those properties are claimed.


* **CLI\_PREVIEW\_ENABLED\_OK** — CLI admin preview (for Aux narratives) is enabled only for admins and uses the same emitter as Aux. (Owned: Governance; CLI/API Vendor Ref)  
    
* **CLI\_PREVIEW\_INDEXED\_OK** — CLI admin preview outputs are captured and indexed as governed artifacts (stdout text \+ ids-only JSON). (Owned: Governance; Evidence & Artifacts)  
    
* **TK-HDE-EPIC022-RAGGED\_SHOWCOMPAT\_ARTIFACTS** — For HDE-EPIC022, the showcompat evidence surface required for acceptance is present and audit-ready: the compat JSON stdout artifact is produced canonically (LF-terminated; single emitter), its checksum sidecar naming follows governance posture (canonical name `stdout.json.sha256`; optional legacy alias permitted when explicitly required), and the backing tests/harness steps that validate the artifact set are linked in the token/evidence matrix. This token is epic-scoped and does not change the Reader v1 public covenant.

*Note.* `CLI_READER_EMITTER_PARITY_OK` is deprecated in favor of `CLI_READER_PARITY_OK`. Keep the legacy token only for historical boards and references.

---

### **2.0.9 Database posture**

* **DB\_CONN\_ENV\_OK** — HDE database access in every environment uses `DATABASE_URL` as the sole endpoint key and the Glow-owned direct psycopg provider as the sole active transport. `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are retired and MUST be absent. Their presence is configuration drift and MUST fail closed before provider construction or external I/O. A missing, invalid, unavailable, or unauthorized `DATABASE_URL` MUST produce a typed failure with no bridge, alternate HTTP transport, vendor path, or inferred-endpoint fallback. Connection selection and failures are captured through secret-free governed evidence; ad hoc connection logic is forbidden.  
* **DB\_RUNTIME\_SEARCH\_PATH\_OK** — Runtime `search_path = hde, public` (in that order). (Owned: Glow Infrastructure; Mechanics Guide; Evidence & Artifacts)  
* **DB\_ROLE\_OK** — Current DB role and privilege posture is **captured and indexed**, not assumed ideal. Grants, default privileges, `search_path`, and boundary views are documented via governed artifacts and included in the Evidence Index. Under EPIC-011, `DB_ROLE_OK` asserts accurate capture and review of the existing posture; known design debt (e.g., missing primary keys) is treated as documented debt, not an EPIC-011 blocker. A future PK-focused Epic in HDE Epics Map will tighten this token’s target state.  
* **DB\_SCHEMA\_FINGERPRINT\_OK** — Canonical DDL fingerprint captured for the EPIC-011 objects. (Owned: Evidence & Artifacts)  
* **DB\_BOUNDARY\_VIEW\_OK** — Boundary view (`public.hde_body_graphs_current`) is read-only; no rules/triggers allow writes outside the `hde` schema. (Owned: Governance; Glow Infrastructure; Evidence & Artifacts)  
* **DB\_WRITERS\_ISOLATED\_OK** — Only Engine roles can mutate `hde.*`; backend roles and other consumers have no DML rights on HDE data (write isolation enforced). (Owned: Governance; Glow Infrastructure; Evidence & Artifacts)  
* **PROD\_CONN\_SINGLE\_SOURCE\_OK** — In prod, connection source is single and explicit (no bridge fallback). (Owned: Governance; Glow Infrastructure)

---

### **2.0.10 Env / rails / infra**

* **ENV\_PORT\_REQUIRED\_OK** — Runtime `PORT` is present and bound. (Owned: Glow Infrastructure)  
    
* **SERVICE\_START\_CMD\_CAPTURED\_OK** — Production start command captured (bytes \+ sha256). (Owned: Glow Infrastructure; Evidence & Artifacts)  
    
* **GUNICORN\_APP\_FACTORY\_OK** — Adapter entry `adapter.factory:create_app()` binds `$PORT`. (Owned: Glow Infrastructure; Evidence & Artifacts)  
    
* **ENV\_RAILS\_POLICY\_OK** — Rails posture is explicit and deterministic across environments and surfaces:  
    
  * **Dev/QA rails posture.** Dev/QA environments **may** open rails for vendor HTTP under controlled profiles, but the rails state (`SAFE_MODE`, `ALLOW_NETWORK`) must always be explicit in env and captured in evidence. CI and test harnesses default to **closed rails** for determinism and evidence jobs unless a Doc-Delta names an integration profile that requires open rails.  
      
  * **Prod posture.** Production acceptance must **not** depend on rails-open settings; public Reader/Aux behavior and acceptance proofs assume closed rails for vendor HTTP. Admin-guarded vendor override windows are governed separately (§3.1) and must not weaken the public covenant.  
      
  * **Dev/admin APP\_ENV gating (NEW CANON).** Dev/admin-only surfaces (for example, CLI dev harnesses, internal/dev HTTP sampler endpoints, and similar tools named in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide) **MUST** enforce strict `APP_ENV` gating:  
      
    * Allowed values for dev/admin surfaces are exactly `{"dev","test","local"}`.  
        
    * If `APP_ENV` is **missing**, **empty**, or has any other value (including `"prod"` or typos), the dev/admin surface **MUST** treat this as a **rails violation**:  
        
      * fail closed with a typed, numeric-free error (for CLI) or a writer-style refusal envelope (for HTTP),  
          
      * **MUST NOT** silently assume `dev` or any other default, and  
          
      * **MUST NOT** perform underlying sampler/engine/vendor work.

      

    * Tests and QA evidence (named in Glow QA Guide and HDE-Build Checklist by title) **MUST** show that all dev/admin-only surfaces that call sampler/core or similar internals honor this gating behavior.


* Ownership: Mechanics Guide; Governance; Glow QA Guide; HDE-Build Checklist.  
    
* **ENV\_LC\_ALL\_C\_OK** — All determinism and evidence jobs run with canonical pins `LC_ALL=C`, `LANG=C`, `TZ=UTC` for HDE services and CI (env pins present and enforced). (Owned: Governance; Build Checklist; Mechanics Guide)  
    
* **BG\_VENDOR\_CALLS\_DISABLED\_IN\_PROD\_OK** — In production, **public Reader and Aux traffic is DB-backed only**: the Engine does **not** make live vendor HTTP calls to satisfy public requests. Any vendor-originated data used in prod public responses must arrive via prior ingest and the governed DB; live vendor calls in prod are limited to admin-guarded ops windows (for example, CLI runs under explicit rails-open profiles). Evidence includes env/config snapshots, connectivity proofs, and keys-only logs demonstrating that public prod routes do not open vendor sockets. (Owned: Governance; Glow Infrastructure; Glow QA Guide; Evidence & Artifacts)

For EPIC017 evidence and compat jobs, the default closed-rails profile for CLI, evidence, ordering, and registry jobs is:

`SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC`.

Acceptance tokens `ENV_RAILS_POLICY_OK` and `ENV_LC_ALL_C_OK` together assert that this tuple is enforced for those jobs unless a Doc-Delta explicitly opens rails for a specific integration profile. This directly encodes the “Default: `SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC` for CLI, evidence, ordering, and registry jobs” rule into PF04’s env section, and now additionally encodes dev/admin APP\_ENV gating for Dissolution-era dev/admin surfaces.

* **OBS\_KEYS\_ONLY\_OK** — Operational logs are keys-only and secret-free (no payload bodies or header values; secrets redacted), in accordance with Governance logging policy. (Owned: Governance)

*Observability & privacy tokens.*

* **LOGS\_KEYS\_ONLY\_OK** — Governed logs (including A7 proofs, BodyGraph diagnostics, and ops probes) are keys-only: no payload values, no PII. Payload bytes and PII must never appear in governed logs.  
    
* **BG\_PRIVACY\_REDACTION\_OK** — BodyGraph-specific logs and metrics apply privacy-preserving redaction rules as defined in Glow QA Guide; sensitive fields are omitted or redacted before emission.  
    
* **BG\_METRICS\_EXPOSED\_OK** — Exposed BodyGraph metrics are limited, non-PII, and consistent with infra/QA observability policy; metrics surfaces must not leak user-identifying or sensitive information.

*Rails-open SAFE tokens (vendor 429 & logging).*

* **VENDOR\_RETRY\_BACKOFF\_OK** — Vendor retry and backoff behavior is transport-level, deterministic, and bounded. Retryable classes MUST be explicitly pinned; a status or outcome MUST NOT be made retryable merely by being coerced into `network_error`. Non-200 HTTP statuses outside governed retry classes MUST remain separately typed and MUST NOT be retried. Provider redirects MUST NOT be silently followed in a way that bypasses governed status classification when the acceptance claim is status, retry, or typed-error behavior. No unbounded or ad-hoc retries are permitted.  
* **PROVIDER\_429\_TYPED\_OK** — Vendor `429` responses are parsed into a typed error envelope owned by HDE-CLI-API-Vendor-Ref. Governance asserts that prod traffic sees typed 429s, not opaque errors. A `429` outcome MUST remain distinguishable from real network exceptions and from other non-200 status classes.  
* **RETRY\_AFTER\_PARSE\_OK** — `Retry-After` headers on vendor `429` responses are parsed and enforced according to rules in HDE-CLI-API-Vendor-Ref. Unparseable values are handled under a safe default policy and never result in unbounded retry loops. Evidence MUST show whether the governed posture is retry, wait, omit, or refuse for the parsed value class.  
* **VENDOR\_NO\_PAYLOAD\_LOGGING\_OK** — Logging for vendor calls and vendor refusal paths is keys-only, bounded, and secret-free. Governed logs MUST NOT contain request bodies, response bodies, payload values, PII, plaintext secrets, raw secret header values, or unbounded labels. Payload bytes live only in transport-level artifacts and external vendor systems, not in logs. Evidence for this token MUST show bounded label posture and observable success or failure class without exposing payloads or secrets.

These tokens apply whenever SAFE rails are opened for vendor calls in any environment, including admin-guarded prod windows.

---

### **2.0.11 Catalog hygiene (where applicable)**

* **CATALOG\_ORIENTATION\_CANON\_OK** — Channel IDs canonical `NN-NN` (zero-padded, min-first); ASCII ordered. (Owned: Evidence & Artifacts — Catalogs)  
* **CATALOG\_DENOMINATORS\_FROZEN\_OK** — Pack denominators are present and frozen; no runtime overrides. (Owned: HDE Math Spec; Evidence & Artifacts)  
* **FEATURE\_NULL\_DEFAULT\_OK** — Default `null → 0` unless D3 explicitly overrides. (Owned: HDE Math Spec)  
* **BAND\_MAX\_INCLUSIVE\_OK** — Bands use inclusive-high thresholds. (Owned: HDE Math Spec)  
* **BAND\_EDGE\_GOLDENS\_OK** — Goldens at 24/49/74/100 pass. (Owned: HDE Math Spec; Evidence & Artifacts)  
* **PREFS\_KEYSET\_10\_OK** — Preference keyset is the canonical 10\. (Owned: HDE Math Spec; Governance)  
* **RESONANCE\_PUBLIC\_POSTURE\_OK** — Reader v1 and CLI **public** surfaces obey the **numeric-free, narrative-free public covenant**: success payloads expose exactly six top-level keys (`reader_version, eligible, categories, meta, release_id, idempotence_hash`); `categories[*]` items are exactly `{ "id", "band" }` with `band ∈ {"Cool","Open","Warm","Glow"}`; no SR/XR or other numerics appear in public bodies; typed error envelopes are numeric-free (except optional `retry_after_ms` under governed vendor-rate-limit policy); and no prompts or narratives are emitted on **public** Reader/CLI surfaces. This token covers CLI output only when the CLI is emitting the **Reader v1 success envelope** (for example, via `--dump-reader` sidecars). This token does **not** govern `hdctl showcompat` stdout (the compatibility payload), which may include numeric scores/weights. This token also does **not** govern admin-only surfaces such as the admin bundle; those surfaces may include numeric scores and narrative text but must remain non-public and are covered by the admin-surface tokens in §2.0.17 and the logging/security rules in §7–§8. (Owned: Governance; HDE-Math-Spec; HDE-Schemas & Artifacts; Glow QA Guide)  
* **MAGIC10\_DOMAIN\_CLOSED\_OK** — The internal Magic-10 result domain is the closed ten-ID set in the frozen order: every eligible pair evaluation produces exactly one intrinsic score and band for each canonical category, with no extras, omissions, duplicates, defaults, or harmony-only substitution. Reader v1 is a numeric-free public projection of that complete internal matrix: when `eligible == true`, `categories` contains exactly one `{"id":"harmony","band":"Cool"|"Open"|"Warm"|"Glow"}` item; when `eligible == false`, it contains `[]`; it exposes neither scores nor the other nine categories. Evidence includes internal ten-ID closure and ordering checks, public harmony-only schema and validation checks, and fixtures that reject unknown, extra, missing, duplicate, or nonconforming IDs. (Owned: HDE-Math-Spec; Governance; Glow QA Guide; Evidence & Artifacts)

---

### **2.0.12 Narratives — packs & gate**

* **NARR\_PACKS\_IN\_MANIFEST\_OK**  
    
* **NARR\_PACK\_SHA\_OK**  
    
* **NARR\_PACKS\_CANONICAL\_JSON\_OK**  
    
* **NARR\_PACK\_MANIFEST\_OK**  
    
* **NARR\_PACK\_IDENTITY\_OK**  
    
* **GRACE\_DELIVERABLES\_GATE\_OK**

*Naming cleanup.* `CLI_READER_EMITTER_PARITY_OK` is deprecated in favor of `CLI_READER_PARITY_OK`. Keep the legacy token only for historical boards and references.

### **2.0.13 Registry, ordering & doc-delta harness (EPIC017)**

* **CONFIG\_GEN\_OK** — The `registry_report.v1` configuration report is generated by the typed loader, written as canonical JSON, and present in evidence. (Owned: Governance; Evidence & Artifacts)  
    
* **UNKNOWN\_IDS\_FAIL\_CLOSED\_OK** — The registry loader rejects unknown IDs and fails closed; no unknown IDs are silently accepted into the registry. (Owned: Governance; Evidence & Artifacts)  
    
* **TIEBREAK\_TOTAL\_ORDER\_OK** — Ordering comparators are deterministic and total; tie-breaks are pinned and stable, as demonstrated by the EPIC017 ordering logs (for example, `engine.order.props_total_order.log`). (Owned: Governance; Evidence & Artifacts)  
    
* **DOC\_DELTA\_PRESENT\_OK** — For the current epic, doc-deltas MUST be represented as a **two-surface pair** (draft/staging \+ epic-scoped capture), with concrete filenames and explicit binding:  
    
  * **Draft/staging surface (token evidence binding).** A concrete PF-doc doc-delta draft file exists under `audit/docdeltas/` using a non-placeholder filename. Standard filename (preferred unless superseded by later canon):  
    `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase `<epic-id>`).  
    Placeholders such as `audit/docdeltas/<doc-delta>.md` are non-conforming.  
  * **Epic-scoped capture surface (stable QA record).** An epic-scoped doc-delta capture record exists at:  
    `audit/qa/<epic-id>/00_meta/doc_deltas.md`  
    This is the stable QA record surface for the epic and must list the draft/staging filename(s) and any discovered doc-delta requirements/caveats.  
  * **Binding rule (explicit).** Acceptance artifacts MUST bind `DOC_DELTA_PRESENT_OK` to the **draft/staging surface** under `audit/docdeltas/`. The epic-scoped capture file is an authoritative narrative/record surface, but it is **not** the primary token evidence binding surface.  
  * **Canonical name.** `DOC_DELTA_PRESENT_OK` is the canonical token spelling. Any alias or near-match (for example `DOC_DELTA_CAPTURED_OK`) is non-canonical and MUST NOT be used as an acceptance token name.  
  * **Evidence posture.** Both surfaces MUST be mechanically produced (no manual-fill templates). If either surface’s bytes change, indexing/mirror/path-proof discipline applies where these files are promoted to governed evidence for closure wiring. (Owned: Governance; Evidence & Artifacts)


* **TESTS\_PASS\_OK** — The current epic’s required automated test suite for the claimed slice has been executed and passed under the approved rails posture, with truthful governed evidence that identifies the concrete test commands or CI jobs supporting the claim. This token may be used in epic-close acceptance artifacts when it is bound to governed evidence. It does not subsume `QA_PRECOMMIT_CHECKLIST_OK` or `QA_POSTCOMMIT_CHECKLIST_OK`; those checklist tokens remain separately governed when the epic-close posture requires them. (Owned: Glow QA Guide; Evidence & Artifacts)

### **2.0.14 QA branches & diff-scoped CI**

* **QA\_EVIDENCE\_ONLY\_OK** — QA branches are **evidence-only**: changes are limited to governed evidence artifacts and their indices (for example, `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and new or rotated proofs under `artifacts/**`), plus any required `*.path_proof.txt` files. Application, presenter, schema, and runtime config bytes **must not** change on QA branches; CI and review confirm that diffs are restricted to governed evidence paths, and that human↔machine mirror parity still holds. (Owned: Governance; PF06 — HDE Epic-Process Guide; Glow QA Guide; Evidence & Artifacts)  
    
* **QA\_CI\_DIFF\_SCOPED\_OK** — CI on QA branches is **diff-scoped** to governed evidence files: jobs validate that only evidence/index/mirror artifacts have changed, that index ↔ mirror ↔ `proof_anchor` parity holds, and that no unapproved code/schema/config changes are introduced. QA CI remains merge-gating on evidence integrity, but intentionally limits test scope to the governed diffs for QA branches. (Owned: Glow QA Guide; Governance; PF12 — HDE-Schemas & Artifacts)

### **2.0.15 Config artifacts & acceptance map (EPIC018+)**

* **CONFIG\_REGISTRY\_OK** — The canonical registry report is generated under closed rails and governed as part of the evidence skeleton. The only accepted writer for this artifact is the config generator (`tools/config/generate_config_artifacts.py` or equivalent entrypoint named in HDE-Mechanics Guide). The generator **MUST** enforce the canonical determinism env pins (the closed-rails tuple in §2.0.10/§4.1.4) before emitting the registry report, load registry data via the hardened loader, and serialize the report as canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF) using the shared serializer. Evidence for this token consists of: (a) the governed registry report artifact (for example `artifacts/registry/registry_report.json`) written under closed rails, (b) its co-located path-proof, and (c) matching entries in `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` keyed by a reserved `artifact_key` for the registry report. PF12 — HDE-Schemas & Artifacts owns the schema, artifact\_key, and mirror mapping; PF19 — Glow QA Guide and PF09 — HDE-Build Checklist own the QA wiring and acceptance map that ties this token to specific tasks and tests. PF04 owns the token semantics and closed-rails governance.  
    
* **CONFIG\_MAGIC10\_OK** — The Magic-10 and band-edges config artifacts are generated under closed rails from the canonical math inputs and governed as part of the evidence skeleton. The config generator (`tools/config/generate_config_artifacts.py` or equivalent) **MUST**:  
    
  * enforce the canonical determinism env pins (closed-rails tuple in §2.0.10/§4.1.4),  
      
  * derive Magic-10 configuration and band-edges from the hardened registry/thresholds inputs defined by Math and Mechanics (titles-only), and  
      
  * serialize the resulting artifacts (for example `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json`) as canonical JSON using the shared serializer (UTF-8, no BOM; sorted keys; compact separators; exactly one trailing LF).


* Evidence for this token consists of: (a) the governed Magic-10 and band-edges config artifacts with co-located path-proofs, (b) matching entries in the human Evidence Index and machine mirror keyed by reserved `artifact_key` values for these configs, and (c) a validated EPIC-018 config acceptance map (for example `audit/EPIC-018_config_acceptance_map.json`) that maps PF09 config tasks (e.g. HDE-CALC004/HDE-CALC004.3/HDE-CALC004.7) to artifact keys, tokens, and tests without dangling references. PF12 owns schemas and artifact\_key mapping; PF19 and PF09 own the QA acceptance map; PF04 owns the governance token semantics and the closed-rails requirement.

### **2.0.16 Typed bundles (EPIC018+)**

* **CONFIG\_BUNDLES\_DETERMINISTIC\_OK** — Typed frontend and backend config bundles are generated under closed rails from the same governed config artifacts as EPIC018 D5 and are treated as **governed evidence artifacts**, not runtime switches. The only accepted writers for these bundles are the canonical bundle generator entrypoints named in **HDE-Mechanics Guide** (for example `engine/config/bundles.py` and `tools/config/generate_bundles.py`), which **MUST**:  
    
  * enforce the canonical closed-rails env tuple (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) before generating any bundle,  
      
  * derive all bundle contents **only** from hardened registry/config sources (the governed registry report and Magic-10/band-edges config artifacts defined by Math/Mechanics and governed in §2.0.15 / §4.1.9), and  
      
  * serialize the resulting frontend and backend bundles using the shared canonical serializer (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF), yielding deterministic bytes with **two-run identity** for each bundle.


* Evidence for this token consists of:  
    
  * governed bundle artifacts under a pinned path (for example `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`), each with a co-located `*.path_proof.txt`,  
      
  * corresponding entries in `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` keyed by reserved `artifact_key` values for the frontend and backend bundles, and  
      
  * tests and harnesses (named in **Glow QA Guide** and **HDE-Build Checklist**) that assert canonical formatting, two-run identity, schema conformance via local bundle schemas, and strict linkage back to the governed config artifacts (for example, a `sources` block in each bundle that records path, sha256, and size for the upstream config artifacts and matches the current skeleton).


* PF12 — HDE-Schemas & Artifacts owns the bundle schemas, artifact paths, and mirror mapping; PF19 — Glow QA Guide and PF09 — HDE-Build Checklist own the QA wiring and acceptance map for this token. PF04 owns the governance semantics: bundles are generated under closed rails from governed config inputs, contain no secrets or dynamic runtime state, and any change in bundle shape or semantics is treated as a config/evidence change that **must** refresh the evidence skeleton and associated tests in the same PR.

  ### **2.0.17 Admin bundle & admin surfaces (pre-Glow)**

* **ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK** — The internal **admin bundle builder** composes the full product payload for a match into a single JSON object using only the canonical components defined elsewhere by title: per-person BodyGraph JSON for each party, the full Magic-10 compat JSON for the pair (categories \+ compat meta), exactly three Aux narrative compositions selected for that match, and a `meta` block carrying engine/build identity (for example `engine_tag`, `release_id`, `invocation_tag` or equivalent) and a bounded description of the bundle source and rails posture. The admin bundle is emitted via the shared canonical serializer (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF) and is explicitly **admin-only**: it is not a Reader v1 public payload, is not an A7 proof surface, and may contain numeric scores and narrative text. Evidence for this token consists of shape/coverage tests for the admin bundle builder, plus governed artifacts (for example, fixture bundles and schema checks) showing that all required components are present and correctly wired to their single homes. Ownership: Governance (token semantics); **HDE-Mechanics Guide** (builder implementation and schema); **HDE-Schemas & Artifacts** (admin-bundle schema and evidence mapping); **Glow QA Guide** and **HDE-Build Checklist** (QA wiring).  
    
* **CLI\_ADMIN\_BUNDLE\_PARITY\_OK** — The canonical **CLI admin bundle command** and the **HTTP admin bundle route** both use the same internal admin bundle builder and canonical emitter and, given the same logical inputs and environment, produce **byte-identical** admin bundle JSON (including the single trailing LF). Pre-Glow, both surfaces target the Railway production engine and DB using the configuration names defined in **Glow Infrastructure** and **HDE-CLI-API-Vendor-Ref** (titles-only) rather than hard-coded hosts; any host with the same config and network reachability can exercise the CLI. Evidence includes: (a) governed parity runs that call CLI and HTTP admin surfaces with the same inputs and byte-compare the resulting bundles, and (b) machine-mirror entries for those parity captures. Ownership: Governance (parity semantics); **HDE-CLI-API-Vendor-Ref** (CLI/HTTP contracts); **HDE-Mechanics Guide** (builder wiring); **Glow QA Guide** and **HDE-Build Checklist** (tests and tasks); **HDE-Schemas & Artifacts** (evidence mapping).  
    
* **ADMIN\_AUTH\_REQUIRED\_OK** — All admin bundle surfaces are **authentication- and authorization-guarded**: neither the CLI admin bundle command nor the HTTP admin bundle route may return the admin bundle without a valid admin credential. Pre-Glow, this means a high-entropy admin secret (or equivalent credential) stored as a secret in Railway (names-only in Glow Infrastructure), not checked into the repo, and required on every admin-bundle request via a transport mechanism pinned in **HDE-CLI-API-Vendor-Ref** (for example, a single admin header). Missing or invalid credentials must produce a typed, numeric-free error; they must never return the bundle. The admin credential must be **rotatable** and **revocable** by configuration or secret management only (no code changes), and rotation must immediately invalidate prior values. Evidence for this token consists of: (a) QA harness runs that show unauthenticated and mis-authenticated CLI/HTTP admin-bundle calls fail closed with typed errors and do not emit bundles; (b) a governed description of the active admin credential source (titles-only; no secret values); and (c) machine-mirror entries linking these proofs to this token. Ownership: Governance (auth/rails semantics); **Glow Infrastructure** (secret names and storage, titles-only); **HDE-CLI-API-Vendor-Ref** (auth carrier and error mapping); **Glow QA Guide** and **HDE-Build Checklist** (QA playbook “Live QA via CLI and HTTP admin bundle”).

### **2.0.18 QA Acceptance Tokens & PF23 scope**

**PF04 vs Glow QA Guide vs Reality Audits.**

* PF04 §2.0 remains the **single home for governance acceptance tokens**. Token names and semantics are defined here once.  
    
* **Glow QA Guide** maintains a **QA Acceptance Tokens library** that organizes these tokens for QA use. For QA Acceptance Tokens, PF19 acts as the **operational registry** and must:  
    
  * reference token names exactly as they are defined in this section, and  
      
  * record QA-facing semantics and wiring without introducing new or divergent meanings.


* **HDE-Build Checklist** and **HDE-Phased Epics** are **consumers only**. They group and schedule tokens for phases and epics but must not introduce new token names, aliases, or synonyms for the same behavior.  
    
* **Reality Audits** (PF23) are a **separate axis**. Decisions to run, waive, or narrow a PF23 audit for a specific plan or epic:  
    
  * do **not** change which QA tokens exist,  
      
  * do **not** change how those tokens must be named, and  
      
  * do **not** relax the required wiring from tokens to tests, CI jobs, Live QA steps, or evidence.


* PF23 scope is local to the audited epic or plan and must never weaken the semantics or governance posture of tokens defined in this section or in the Glow QA Guide’s QA Acceptance Tokens library.

**Single-home restatement.**

* PF04 §2.0 is the **governance single home**: every acceptance token (including QA Acceptance Tokens) is introduced here first and is mirrored by **HDE-Schemas & Artifacts**, **Glow QA Guide**, and **HDE-Build Checklist** by title only.  
    
* Glow QA Guide is the **QA single home** for the QA Acceptance Tokens library: it must list every QA token used in acceptance maps and manifests, with semantics aligned to this section, and may not introduce new QA Acceptance Tokens that are absent from PF04. Any new QA Acceptance Token requires:  
    
  * a PF04 Doc-Delta entry in §9 that adds the token to this roster, and  
      
  * corresponding updates in Glow QA Guide, HDE-Schemas & Artifacts, and HDE-Build Checklist in the same change.

**PF23 consult is planning-time trace only (no execution-time QA artifacts; no `REALITY_AUDIT_OK`).**

A PF23 consult is a *planning-time trace posture* (what loci were consulted while reasoning about risk/behavior), not a Live QA execution artifact and not acceptance evidence by itself.

* Plans and implementations MUST NOT mint, claim, or reference any acceptance token such as `REALITY_AUDIT_OK` unless and until Governance explicitly registers such a token in §2.0.  
* Live QA Plans and Live QA execution MUST NOT require or produce PF23 consult artifacts under QA\_ROOT (including `audit/qa/<epic-id>/00_meta/pf23_consult.md`).  
* If a trace anchor is desired, the Live QA Plan MAY include a short “PF23 Anchors consulted” note in the plan body (names-only; no operator commands; no required Deliverables).  
  Any acceptance roster that includes `REALITY_AUDIT_OK` is non-conforming; treat that as an invalid acceptance configuration.

**PF23 consult scope (planning allowed and required; PR analysis disallowed).**

Reality Audits (PF23) are post-epic audits. They are updated at epic close and therefore reflect a latest closed-epic snapshot, not an in-flight PR truth source.

* PF23 MUST be consulted during:  
    
  * Epic planning (Epic Plan creation or revision).  
      
  * Implementation planning (Implementation Plans that define PR and OPS scope and acceptance posture).  
      
  * QA planning (including Live QA plans and runbooks).  
    In these contexts, PF23 may be used to ground component boundaries and canonical loci and to prevent fabricated repo paths and invented surfaces.


* PF23 MUST NOT be consulted for PR analysis, including:  
    
  * PR review.  
      
  * Remediation review.  
      
  * Diff-first approval loops.  
    PR analysis MUST rely on the owning PF canon homes (contracts, evidence families, mechanics) and repo reality for the PR under review, without using PF23 as a blocker source.

**Drift assessment trigger (PF23 contradictions vs PF canon).**

If any PF23 Reality Audit statement contradicts PF canon, that contradiction MUST be treated as development drift requiring evaluation, not as an automatic correction in either direction. The contradiction may represent exactly one of these conditions:

* Canon defect (PF canon is incorrect or outdated).  
    
* Implementation drift (the repo drifted away from canon without an approved change path).  
    
* Necessary reality shift (development changes were required in reality and canon has not yet been updated to reflect them).

**Drift assessment protocol (stub; required posture, not full process).**

Until a full protocol is published, use this minimal, non-optional stub whenever PF23 contradicts canon:

* Record the contradiction as a drift item with:  
    
  * PF23 claim (quote or precise paraphrase).  
      
  * The conflicting PF canon claim (quote or precise paraphrase).  
      
  * The impacted epic or surface.


* Classify the drift into exactly one bucket (tentative): canon defect, implementation drift, or necessary reality shift.  
    
* Do not fix by assumption. No plan, review, or QA artifact may treat the contradiction as resolved unless the PO explicitly adjudicates the resolution path.  
    
* Resolution routing is PO-owned. The PO decides whether the fix is a canon update, implementation remediation, or a formalized exception with canon follow-up.

**PF23 audit observation classification.**

PF23 audit findings MAY identify canon-routing or classification deltas without creating execution work. A PF23 audit finding MUST be routed to the owning PF canon home by subject and MUST NOT be converted into a PF09.x task delta, implementation remediation, OPS task, Live QA task, or PF20 historical correction by assumption. Such work exists only when an approved plan, PF10 addendum, Product Owner adjudication, or owning PF canon update explicitly creates it.

**Routing for PR analysis (when PF23 is out of scope).**

When PF23 is out of scope (PR analysis), reviewers MUST rely on the owning PF canon homes by title and repo reality for the PR under review. Typical anchors include: HDE Architecture, HDE Governance, HDE CLI/API Vendor Ref, HDE Schemas and Artifacts, HDE Build Checklist, HDE Mechanics Guide, Glow QA Guide, and HDE Epic-Process Guide.

### **2.0.19 QA bootstrap & harness (EPIC021+)**

These tokens govern **QA tooling bootstrap**, **QA\_ROOT harness discipline**, and **acceptance-map / QA-plan viability** for epics. They are QA Acceptance Tokens in the sense of §2.0.18: PF04 owns their names and governance semantics; **Glow QA Guide** owns the QA library entries and detailed harness procedures; **HDE-Build Checklist** and **HDE-Phased Epics** consume them in phase tasks and epic records.

**Canonical QA\_ROOT naming (normative).**  
Within §2.0.19, `<epic-id>` refers to the canonical epic QA root slug `hde-epic<NNN>`, where `<NNN>` is the zero-padded 3-digit epic number. Epic QA root directories MUST be lower-case and MUST use this canonical pattern:

* `audit/qa/hde-epic<NNN>/`

Plans and implementations MUST NOT introduce parallel alternate spellings for the same epic (examples of disallowed alternates include: `EPIC022`, `EPIC_022`, `audit/QA/...`, `audit/qa/HDE-EPIC022/...`). If legacy artifacts exist under non-canonical names, they are treated as deprecated; do not create new ones under the deprecated pattern.

**QA\_LIVE\_QA\_RUN\_OK** — An epic cannot close until it has executed a Live QA harness run and checked the resulting evidence into the repo under QA\_ROOT.

* Governance semantics.  
    
  * the Live QA workflow is a close gate work product owned by the Glow QA Guide and Mechanics; epic plans MAY include only the statement “Live QA run required” plus a pointer to the canonical runbook and the committed evidence paths.  
      
  * Live QA execution is proof-only validation. A Live QA step may prove, classify, or record the current governed state, including an approved bounded Moon Loop evidence correction, but its PASS record MUST NOT be treated as implementation work, product remediation work, PF-canon drainage, PF09 status movement, formal close-pack completion, or Product Owner closeout action. If Live QA discovers work that requires implementation, OPS, documentation drainage, or close-pack packaging, that work MUST remain a separate approved task, follow-up, or closeout slice.  
      
  * QA\_ROOT naming is normative: `audit/qa/<epic-id>/...`  
      
  * **KISS required outputs (current-state):**  
      
    * for each required Live QA check, the work MUST write a primary step log at `audit/qa/<epic-id>/checks/<check_id>/primary.log` (one primary log per check).  
    * the work MUST maintain a step-logs manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json` that lists each check id, its status, and the path to its primary step log. This file is **current-state** (not per-run history).  
    * when a check updates or refreshes the step-logs manifest for itself, the manifest entry for that check MUST be derived from that check’s governed \`primary.log\` header.  
    * the refresh MUST NOT be sourced from paraphrased summaries, copied verdict prose, or unguided manual transcription.  
    * if the manifest bytes change as part of that refresh, the co-located \`audit/qa/\<epic-id\>/qa\_step\_logs\_manifest.json.path\_proof.txt\` MUST be refreshed from the new manifest bytes before the step is treated as complete.  
    * if the epic is not claiming \*\*QA\_LIVE\_QA\_RUN\_OK\*\*, the manifest MAY set \`checks: \[\]\` to explicitly declare that no Live QA checks are being claimed. When \*\*QA\_LIVE\_QA\_RUN\_OK\*\* is claimed, \`checks\` MUST enumerate the required Live QA checks and MUST NOT be empty.  
    * the step-logs manifest MUST have a co-located path-proof transcript: `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`. The path-proof MUST record at minimum the manifest’s `path`, `size_bytes`, and `sha256`, and MUST match the current-state manifest bytes.  
    * when a step claims human-ledger, machine-ledger, or companion-proof refresh coherence for the current-state manifest, the canonical updater MUST exit \`0\`, the current-state manifest pair MUST exist, and the manifest MUST be positively discoverable in the updater, the human Evidence Index, and the machine mirror before the step may claim \`PASS\`.  
    * a positive discoverability check MUST be captured as a concrete step artifact for each of those three loci and MUST resolve affirmatively for the current-state manifest.  
    * nothing else is auto-required unless Governance explicitly pins a governed evidence family/path for the epic.  
    * if a tooling-state mismatch prevents those conditions from holding, an allowed Moon Loop MAY re-run the canonical updater under closed rails, rebuild the current-state manifest from governed \`primary.log\` headers, refresh the co-located manifest path-proof, regenerate the discoverability artifacts, and then rewrite the step \`primary.log\` from the refreshed concrete artifacts. This remediation MUST remain evidence-capture only and MUST NOT expand scope or change the acceptance target.

    

  * checks SHOULD prefer validating existing canon evidence families/paths over minting new QA artifacts; the check’s `primary.log` records PASS/FAIL and references the canonical evidence validated.  
      
  * planning-trace artifacts MUST NOT be required Deliverables for Live QA execution (e.g., no PF23 consult capture artifacts under QA\_ROOT).  
      
  * for Live QA runs executed in GitHub Codespaces: a “Codespaces snapshot” artifact is optional convenience-only and must not appear in required Deliverables lists and must not be used to decide PASS vs remediation.).  
      
  * This convenience-only snapshot rule does not prohibit a governed venue-provenance artifact when a closeout review, or an approved provenance-only closeout slice, must establish that at least one executed QA or closeout artifact family was produced from GitHub Codespaces.  
      
  * Such a venue-provenance artifact is closeout-only and non-default. Unless a plan or closeout review explicitly requires venue confirmation, it MUST NOT appear in required per-step Deliverables lists and MUST NOT decide PASS versus remediation for the underlying QA step.  
      
  * When used, it MUST bind to an existing governed artifact family, record the bound governed artifact path, the in-session command or command family, presence-only or redacted Codespaces session context, repo root and commit linkage, and any non-claim boundaries. If it is treated as governed closeout evidence, it MUST also carry a sibling `.path_proof.txt` transcript.  
      
  * A narrow rerun of one stable governed artifact family MAY be used to produce this provenance when the approved closeout slice explicitly allows it. That rerun MUST remain packaging/provenance only and MUST NOT reopen implementation scope or change QA verdicts.


* Acceptance.  
    
  * a Live QA workflow exists (owned by the Glow QA Guide and Mechanics).  
  * under QA\_ROOT, `audit/qa/<epic-id>/qa_step_logs_manifest.json` exists and enumerates the required checks with status and primary-log paths; for each enumerated check, `audit/qa/<epic-id>/checks/<check_id>/primary.log` exists at the referenced path.  
  * a co-located path-proof transcript exists for the manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` and matches the manifest bytes (size/sha256).  
    all required checks are PASS (as recorded in the manifest and evidenced in each check’s `primary.log`).  
  * the token/evidence matrix row for QA\_LIVE\_QA\_RUN\_OK references the manifest and/or the check primary logs as closure evidence for this token.

---

* **QA\_HARNESS\_ENTRYPOINT\_SELFTEST\_OK** — Any harness entrypoint command documented in a Live QA plan must have a corresponding CI test that proves the entrypoint actually produces the expected QA\_ROOT outputs under the canonical env pins.  
    
  **Scope.**  
    
  * Epic-level token. Required whenever an epic is subject to Live QA via harness (see `QA_LIVE_QA_RUN_OK`).


* **Governance semantics.**  
    
  * For the harness entrypoint command documented in the epic’s Live QA plan, the repo must include a CI test that:  
      
    * runs the entrypoint (or an equivalent invocation) under the canonical env pins, and  
        
    * asserts that the expected QA\_ROOT outputs are created and non-empty, and  
        
    * fails closed if harness behavior regresses (no “exit 0 but produced nothing” posture).


* **Acceptance.**  
    
  * `QA_HARNESS_ENTRYPOINT_SELFTEST_OK` is satisfied only when:  
      
    * the epic’s token/evidence matrix row lists the concrete CI test(s) and CI job(s) that exercise the documented harness entrypoint under closed rails, and  
        
    * those tests are wired and evidenced as governed artifacts per §9.7.2 (tests, CI jobs, evidence paths, Index/mirror linkage).


* Ownership: Governance (gate semantics); **Glow QA Guide** (entrypoint naming and Live QA patterns); **HDE-Mechanics Guide** (harness mechanics); **HDE-Build Checklist** (CI/QA enforcement tasks); **HDE-Schemas & Artifacts** (evidence indexing).

*Note.* `QA_STEP_LOGS_CONSOLIDATED_OK` is deprecated in favor of `QA_HARNESS_DISCIPLINE_OK`. Keep the legacy token only for historical boards and references; new acceptance artifacts MUST use the canonical token name.

---

* **QA\_BOOTSTRAP\_OK** — A closed-rails QA tooling bootstrap run for the epic has completed successfully and established that the **QA tooling is ready** (pytest/CLI/tooling) before deeper QA or Live QA steps proceed.  
    
  **Scope.**  
    
  * Epic-level token: claimed at epic close or when an epic’s QA plan is declared viable, not per PR.  
      
  * Applies to the epic’s canonical **QA\_ROOT** discipline (`audit/qa/<epic-id>/…`), not to ad-hoc local runs.


* **Governance semantics.**  
    
  * A canonical QA bootstrap harness exists for the epic (for example, `tools/qa/epic021_qa.py` as documented in Build Notes) and is wired under **closed rails** (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) using the same determinism env-pins discipline as `DETERMINISM_ENV_PINS_OK`.  
      
  * The harness runs a **bootstrap suite** (at minimum, pytests must pass on every machine); it yields the check primary log at `audit/qa/<epic-id>/checks/D00_bootstrap/primary.log` and records its status in the step-logs manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json`. (Optional: an additional human-friendly summary log MAY be maintained, but it is not required for acceptance unless explicitly governed.)  
      
  * Bootstrap logs are PF19-style: they carry a `run:` header, an `env:` line describing the closed-rails env, one or more `check …` lines, and a final `summary:PASS` line for a successful run. Exact header and field requirements live in **Glow QA Guide**; PF04 requires that they exist and that they are stable, records-only, and LF-terminated.


* **Acceptance.**  
    
  * `QA_BOOTSTRAP_OK` is **satisfied** only when:  
      
    * the closed-rails bootstrap harness has been run for the epic and produced a successful run (summary `PASS`),  
        
    * the canonical epic-level bootstrap log exists under `audit/qa/<epic-id>/…` and is non-empty, and  
        
    * Evidence Index and machine-mirror entries (PF12 single home) link the bootstrap log(s) and harness run to this token by name, using the token/evidence matrix rules in §9.7.2 (token row, artifacts, CI jobs/tests, QA\_ROOT logs, and proof\_anchor).


* Ownership: Governance (bootstrap semantics); **Glow QA Guide** (bootstrap harness procedure & log schema); **HDE-Build Checklist** (phase tasks); **HDE-Schemas & Artifacts** (artifact families, Index/mirror mapping).

---

**QA\_BOOTSTRAP\_TOOLING\_FAIL** — The QA bootstrap harness can distinguish **tooling failures** from **behavioral failures** and classifies bootstrap step results accordingly, so that blocked QA due to broken tools is visible as tooling debt rather than silently conflated with engine behavior.

**Scope.**

* Epic-level structural token: it does **not** assert that a particular run passed or failed, only that the harness and log format support distinct `FAIL_TOOLING` vs `FAIL_BEHAVIOR` classifications and that evidence of such classifications exists.

**Governance semantics.**

* The QA bootstrap harness uses a PF19-defined status classification (for example, `OK` / `FAIL` / `FAIL_TOOLING` in a `status` field per check) and emits those statuses into bootstrap logs under QA\_ROOT.  
    
* When the harness encounters a tooling-level failure (for example, pytest import error, missing dependency, or infrastructure misconfiguration), the corresponding log entries mark the step as tooling failure (e.g. `summary:FAIL_TOOLING` or equivalent PF19 encoding), and this is reflected in the epic’s token/evidence matrix and acceptance map notes rather than being treated as a behavior failure of the engine.  
    
* Tooling vs behavior mapping MUST NOT be inferred from exit codes alone. In particular: “missing pytest” is a tooling failure and MUST be classified as `FAIL_TOOLING` (not `FAIL_BEHAVIOR`) when detected.

**Acceptance.**

* `QA_BOOTSTRAP_TOOLING_FAIL` is **satisfied** when:  
    
  * the bootstrap harness and QA\_ROOT logs demonstrate distinct tooling vs behavior classifications in at least one controlled failure case (for example, a deliberate broken test in a harness run, as described in Build Notes), and the evidence includes at least one bootstrap log whose summary encodes tooling failure (for example `summary:FAIL_TOOLING` or equivalent PF19 encoding), and  
      
  * the epic’s token/evidence matrix row for this token enumerates the bootstrap evidence artifacts, CI job(s), and QA\_ROOT logs that show the classification semantics in action, even if the **current** epic run is green; a PASS-only bootstrap `primary.log` (used to satisfy `QA_BOOTSTRAP_OK`) cannot satisfy this token unless it contains explicit tooling-failure classification evidence.

Ownership: Governance (classification semantics at policy level); **Glow QA Guide** (exact statuses and log fields); **HDE-Build Checklist** (tasks that exercise FAIL\_TOOLING path); **PF10 — Glow HD Engine Build Notes** (per-epic harness implementation details).

---

* **QA\_HARNESS\_DISCIPLINE\_OK** — The epic’s **QA\_ROOT harness discipline** is in place: QA\_ROOT layout, per-step logs, and QA step classifications follow the PF19 patterns and PF12/PF09 evidence routing, with no stray or ambiguous QA artifacts.  
    
  **Scope.**  
    
  * Epic-level token for the epic’s QA\_ROOT directory (for example, `audit/qa/hde-epic021/`); not per-branch.


* **Governance semantics.**  
    
  * The epic has a canonical QA\_ROOT README (for example, `audit/qa/hde-epic021/README.md`) that:  
      
    * identifies the directory as the epic’s QA\_ROOT discipline home,  
        
    * lists the expected epic-level artifacts (at minimum: `token_evidence_matrix` artifact, tooling bootstrap log, and acceptance-map viability log), and  
        
    * clearly distinguishes QA\_ROOT paths from PF12-governed Evidence Index paths (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`).

    

  * QA step logs under QA\_ROOT follow PF19 header and classification rules: deterministic, timestamp-free records with PF19-style headers (run id, env, rails), per-step result lines, and a single `summary:` line per log; empty or partially written logs are treated as failures in PF19 semantics, not ignored.  
      
  * QA\_ROOT layout is **non-destructive**: each epic has its own root at `audit/qa/<epic-id>/`, and Live QA check outputs MUST be written to stable **current-state** paths (e.g., `audit/qa/<epic-id>/checks/<check_id>/primary.log` plus `audit/qa/<epic-id>/qa_step_logs_manifest.json`). Per-run `<run-id>/` subdirectories and history retention constructs are optional and non-gating unless Governance explicitly pins them. QA\_ROOT dirs from prior epics (e.g. EPIC020) remain intact.


* **Acceptance.**  
    
  * `QA_HARNESS_DISCIPLINE_OK` is **satisfied** only when:  
      
    * QA\_ROOT README and directory structure exist and match the discipline described above,  
        
    * QA step logs for the epic (including bootstrap, sanity, and viability steps) are present, non-empty, and follow PF19 header/summary rules, and  
        
    * the epic’s token/evidence matrix includes rows for this token that identify the QA\_ROOT logs, CI jobs/tests, and any QA harness scripts responsible for maintaining this discipline.


* Ownership: Governance (discipline semantics and token coupling to QA\_ROOT); **Glow QA Guide** (log shapes, header schemas, and QA patterns); **HDE-Build Checklist** (Calcination tasks HDE-CALC003.12–.15); **HDE-Schemas & Artifacts** (Index/mirror treatment of QA\_ROOT-linked artifacts, where applicable).

---

* **QA\_ACCEPTANCE\_MAP\_VIABILITY\_OK** — The epic’s **acceptance map and QA plan are viable**: for the epic, there is a governed acceptance map, a token/evidence matrix, and a viability check that proves coverage and coherent failure-mode semantics for all tokens in scope.  
    
  **Scope.**  
    
  * Epic-level token for the epic’s acceptance artifacts (for example, `docs/acceptance_map_epic021.json` and its token/evidence matrix under `audit/qa/<epic-id>/token_evidence_matrix.*`).


* **Governance semantics.**  
    
  * A **governed acceptance map** for the epic exists (for example, `docs/acceptance_map_epic021.json`) with:  
      
    * `epic_id` matching the epic id, and  
    * a top-level `tokens` array (required) whose `name` fields are PF04 §2.0 token names and whose `owner_pf` fields route to the proper PF homes.  
    * Token identity is derived from `tokens[].name` only; it is case-sensitive and MUST match the token registry entry exactly (do not infer tokens from table header labels such as `token_name`).

    

  * A **token/evidence matrix** artifact exists for the epic under the PF12-designated path (for EPIC021: `audit/qa/hde-epic021/token_evidence_matrix.md`), and satisfies the per-token fields required by §9.7.2 (PF owner, artifacts, CI jobs/tests, QA\_ROOT logs, status, notes).  
      
  * A viability check/harness (for example, `generate_acceptance_map_viability` as described in Build Notes) parses the matrix and acceptance map together and writes a viability log under QA\_ROOT (for example, `audit/qa/<epic-id>/acceptance_map_viability.log`) that:  
      
    * reports at least one classification line per token, and  
        
    * summarizes overall viability (for example, `summary:PASS` when all tokens in scope are wired and have evidence, or PF19-defined failure codes when gaps exist); the overall status MUST reflect detected issues (MUST NOT be unconditional PASS) and MUST gate the viability harness exit status (exit 0 only when the summary indicates PASS).


* **Acceptance.**  
    
  * `QA_ACCEPTANCE_MAP_VIABILITY_OK` is **satisfied** only when:  
      
    * every token listed in the epic’s acceptance map appears as a row in the token/evidence matrix, and vice versa, with no “orphan” tokens,  
    * the matrix rows for the epic’s QA Acceptance Tokens have no `"e.g."`/`"TBD"` placeholders and enumerate tests, CI jobs, QA\_ROOT logs, and evidence artifacts, as required by §9.7.2, and  
    * the viability log for the epic under QA\_ROOT exists, is non-empty, and indicates that all tokens in scope are wired and evidenced (PF19 owns the detailed viability thresholds and failure patterns).  
    * the current-epic acceptance binding is single-home across three authoritative governed artifacts only: the epic acceptance map at its canonical docs path, the epic token/evidence matrix under QA\\\_ROOT, and the epic viability log under QA\\\_ROOT. Step-scoped snapshots or convenience copies MAY be produced for review, but they are not alternate homes and MUST NOT be used as acceptance binding sources.  
    * the machine mirror MUST contain matching rows for all three authoritative binding artifacts before a step or closeout record claims that the current-epic acceptance binding is coherent.  
    * no alternate acceptance-map home is authoritative. If an alternate or convenience copy exists, it is non-binding and MUST NOT be used to satisfy acceptance-map presence or acceptance-binding coherence claims.


* Ownership: Governance (viability semantics and coupling to tokens/acceptance maps); **Glow QA Guide** (viability harness behavior and log format); **HDE-Schemas & Artifacts** (artifact family and Index/mirror mapping for token/evidence matrix and viability logs); **HDE-Build Checklist** (Calcination and later-phase tasks that wire acceptance maps and matrix artifacts); **HDE-Phased Epics** (D-goals and epic-level acceptance maps referencing this token).  
    
* **QA\_PRECOMMIT\_CHECKLIST\_OK** — The epic’s **precommit QA checklist** has been executed and passed under the required rails posture (closed rails unless the checklist explicitly scopes an open-rails probe), producing machine-generated evidence that the required governance preflights are in place. The checklist’s exact steps and log schema are owned by **Glow QA Guide** (titles-only).  
    
  **Scope.**  
    
  * Epic-level QA token (preflight).


* **Governance semantics.**  
    
  * The checklist is mechanical: command-produced outputs, no manual fill, and no non-canonical wrapper dependency (see §9.8.2).  
  * Outputs are written under QA\_ROOT and must be indexable via the token/evidence matrix rules in §9.7.2.


* **Acceptance.**  
    
  * A governed checklist log exists under `audit/qa/<epic-id>/...` with a PASS summary (Glow QA Guide encoding), and  
  * the epic’s token/evidence matrix row links that log (and its Index/mirror entries where applicable) to this token.


* Ownership: Governance (token semantics); **Glow QA Guide** (procedure/log shape); **HDE-Schemas & Artifacts** (index/mirror mapping); **HDE-Build Checklist** (phase consumption).  
    
  ---

    
* **QA\_POSTCOMMIT\_CHECKLIST\_OK** — The epic’s **postcommit QA checklist** has been executed and passed, producing machine-generated evidence that the close-pack and closeout acceptance artifacts are structurally coherent (no placeholders for in-scope tokens; required closeout artifacts present; viability checks satisfied where required). Exact steps and log schema are owned by **Glow QA Guide** (titles-only).  
  **Scope.**  
    
  * Epic-level QA token (post-close structural guard).


* **Governance semantics.**  
    
  * The checklist is mechanical and artifact-based: it uses governed files and tests as inputs and produces a governed checklist log under QA\_ROOT.


* **Acceptance.**  
    
  * A governed checklist log exists under `audit/qa/<epic-id>/...` with a PASS summary (Glow QA Guide encoding), and  
  * the epic’s token/evidence matrix row links that log (and any required Index/mirror entries) to this token.


* Ownership: Governance (token semantics); **Glow QA Guide** (procedure/log shape); **HDE-Schemas & Artifacts** (index/mirror mapping); **HDE-Build Checklist** (phase consumption).  
    
* Close-pack baseline artifacts (non-token; deterministic path-of-record). Close-pack presence is a baseline closure artifact requirement, not an acceptance token by default.  
    
  * Path-of-record (normative):  
      
    * `audit/EPIC-###_close_report.md`  
        
    * `audit/EPIC-###_MANIFEST.json`  
      (Where `###` is the zero-padded 3-digit epic number.)

    

  * **Closeout companion ledgers (recommended; may declare `None`).** When the epic closeout produces doc-delta and doc-drain planning ledgers, they SHOULD live under `audit/docdeltas/` using epic-scoped filenames, for example:  
      
    * `audit/docdeltas/<epic-id>_doc_deltas.md`  
        
    * `audit/docdeltas/<epic-id>_drain_targets.md`

    

  * **Close report minimal content (normative).** `audit/EPIC-###_close_report.md` MUST be a human-readable closure summary and MUST include:  
    * a brief delivered-work summary (what shipped in the epic),  
    * when the epic closes by reusing already-implemented governed scope, a reuse-boundary summary identifying which proof families or deliverable groups were inherited baseline versus newly closed in the epic,  
    * when closure is distributed across bounded PR or work slices, a PR-to-deliverable allocation summary that states which slice closed which governed deliverable family or acceptance-bound proof family,  
    * **Implementation-slice evidence and close-pack evidence are distinct.** When closure is distributed across bounded PR or work slices, the closeout record MUST keep implementation-slice evidence separate from close-pack evidence and Live QA close-gate evidence. PR-slice implementation evidence MAY support delivered-work summaries, supportable PF09 drainage posture, and closeout binding, but it MUST NOT be described as close-pack production, Live QA completion, final closeout, or epic-close proof unless those close-stage artifacts and checks are directly evidenced in the reviewed source set.  
    * an explicit deferrals list (including deferred item IDs when available),  
    * **Repo-supported completion summary (required when closeout is recommended from repo evidence)**.The closeout record MUST state whether the completion summary is limited to repo-supported completion and MUST distinguish repo-supported completion from canon drainage, formal close-pack completion, merge provenance, board state, Product Owner closeout action, and formal ops action.  
    * **Outcome-classification clarity.** The closeout summary MUST distinguish recorded, blocked, and no-claim outcomes for the relevant QA or closeout items and MUST NOT collapse those states into a single undifferentiated PASS narrative.  
    * **No over-claim rule.** The closeout record MUST NOT imply that canon drainage is complete, that formal close-pack completion is complete, that merge provenance is established, that board state has changed, that Product Owner closeout action has occurred, or that formal ops action has occurred unless those claims are directly evidenced by governed artifacts in the reviewed source set.  
    * **Bounded reclassification rule.** If a bounded Moon Loop or equivalent closeout remediation changes a false blocked classification caused by contextual or filename-based artifacts rather than a real blocking condition, the closeout record MUST preserve the contextual note as separate evidence, identify the trigger that caused the false blocked classification, record the Step-0B delta pair when that remediation path is used, and state the post-remediation classification explicitly.  
    * a pointer to the close-pack manifest `key_outputs` bindings in `audit/EPIC-###_MANIFEST.json`,  
    * pointers to any closeout companion ledgers used for the epic (including their canonical paths under `audit/docdeltas/`),  
    * explicit “canon pointer” fields when closing TI-002 (or other TI items) as satisfied in the closeout, including:  
      * a `PF09 pointers:` line listing the relevant PF09 pointer IDs,  
      * a `TI-002 pointers:` line listing the canon pointers used to evidence TI-002 (or a `TI-<id> pointers:` line for other TI items), and  
      * an `ADR status line:` line identifying the ADR governing the TI claim,  
    * **Coverage vs QA Plan accounting (required when the epic has a Live QA Plan or claims `QA_LIVE_QA_RUN_OK`).** The closeout record MUST include an explicit, step-by-step, complete, and auditable coverage ledger. It MUST list every planned QA step in plan order with a stable step identifier, a coverage status (`PASS`, `FAIL`, `BLOCKED`, or `NOT_RUN`), and the closeout impact for that step,  
    * **Accepted execution-deviation accounting (required).** When a step recorded in the coverage ledger as \`PASS\` materially diverged from the approved QA Plan but was still accepted, the closeout record MUST preserve the step’s coverage status and add a separate deviation note for that step.  
    * **Deviation note content (minimum).** The deviation note MUST identify the deviation type (for example a bounded Moon Loop rerun, a rails change, or a step-local dependency-preflight correction), the governing approval or PF10 addendum that accepted it, and the reason the accepted deviation did not change the acceptance target or the step’s closeout impact.  
    * **Original-versus-accepted receipt accounting (required for remediated steps).** When a planned QA receipt fails and a later remediation receipt becomes the accepted final basis, the coverage ledger, step-log manifest, closeout record, or equivalent review surface MUST distinguish the original planned receipt from the accepted remediation receipt. It MUST preserve the original failed receipt as context, identify which receipt is the final accepted basis, and avoid overwriting or collapsing both receipts into a single undifferentiated PASS row.  
    * **Step evidence rule for closeout.** For any step recorded as \`PASS\`, the closeout record MUST point to at least one step-scoped evidence artifact under the governed QA root for that exact step, or to an explicitly equivalent step-scoped evidence pointer line preserved in the epic’s primary QA record. Heading-only, summary-only, or result-JSON-only PASS statements are insufficient.  
      * When a closeout review asks the reviewer to approve an executed step cluster as \`PASS\`, the review record MUST surface the manifest entry, primary-log header, \`captured\_env\`, \`evidence\_artifacts\`, \`intended\_tokens\`, \`claimed\_tokens\`, and path-proof binding for every executed step in that cluster, or state why an explicitly equivalent governed proof is used.  
      * A result JSON that records \`PASS\` MAY be a supporting artifact, but it is not sufficient by itself when manifest, primary-header, rail, token, or path-proof trust is missing or unsurfaced.  
    * **Token/evidence matrix pointer (required when in-scope QA tokens exist).** The closeout record MUST point to the epic’s token/evidence matrix artifact and MUST identify any in-scope QA token rows that remain blocked, incomplete, or not applicable.  
    * **Closeout review inputs posture (required).** When a closeout recommendation is issued, the closeout record MUST state the source-of-truth posture used for that recommendation. At minimum:  
      * PF10 is primary for epic-specific recorded implementation, remediation, QA execution, closeout, and documented supersession of earlier closeout wording.  
      * PF19 is the QA process and RCA basis where PF10 is silent. PF19 governs QA evidence posture, current-state check roots, documentation drainage posture, and closeout readiness interpretation when PF10 does not provide an epic-specific event record.  
      * PF06 supplies the close-gate QA RCA and Doc Delta summary requirement when the epic closeout process requires that summary.  
      * PF23 is required for current-reality alignment of surfaces, component placement, entrypoints, evidence homes, and repo structure.  
      * PF-Canon is normative where PF10 is silent.  
      * The Implementation Guide is used for intended scope framing only.  
      * The QA Plan is used for intended QA requirement framing only.  
      * If a prompt-provided epic name, phase name, source label, Artifact Map value, or other non-authoritative input label conflicts with the current source-of-truth artifacts, the closeout record MUST state the mismatch explicitly, use the authoritative source posture for review identity and scope, and preserve the mismatched label only as provenance context. It MUST NOT treat the mismatched label as phase authority, scope authority, closure proof, blocker source, or acceptance source.  
      * PF23 is current-reality context only in closeout review. It may support alignment of surfaces, component placement, entrypoints, evidence homes, and repo structure, but it MUST NOT be treated as closure proof, a gate, an acceptance source, or closeout authority by itself.  
      * A closure-trace review, QA closeout review, or readiness recommendation may state that the reviewed trace is satisfied, ready, or ready with caveats only as review posture. It is not a Product Owner closeout action unless the Product Owner explicitly performs or records that closeout action.  
      * **Decisive PF10 addendum auditability note (required).** When a closeout recommendation relies on a PF10 addendum as the decisive epic-close authority, the closeout record MUST state whether that addendum provides direct evidence-pointer lines or only evidence-basis prose.  
      * **Evidence-basis-only caveat.** If the decisive PF10 addendum provides only evidence-basis prose, the closeout record MUST record that explicitly as an auditability caveat and MUST NOT imply pointer-complete support from that addendum alone. The record MUST also identify the governed evidence family or closeout companion artifacts used to complete the trace.  
    * **Required-elements checklist (when a closeout recommendation is issued).**  The closeout record MUST explicitly confirm the presence or absence of:  
      * the D0 Discovery artifact,  
      * current-state QA evidence under the governed QA root,  
      * a QA RCA / Doc Delta summary,  
      * indexed evidence for the claimed closeout artifacts,  
      * when the review requires venue confirmation, at least one governed artifact or closeout note that proves an executed QA or closeout artifact family was produced from the claimed venue, for example GitHub Codespaces,  
      * source-of-truth posture for the closeout analysis, including which sources are used for epic-specific event truth, process interpretation, intended QA framing, and normative canon where the live record is silent,  
      * Coverage vs QA Plan in plan order, including each planned step’s coverage status, deviations or mismatches, and closeout impact,  
      * a QA timeline that records QA steps, remediation loops, ADR or decision events, outcomes, and evidence pointers,  
      * findings with classification and evidence pointers,  
      * root cause analysis,  
      * remediation loop assessment,  
      * implementation gaps and proposed fixes,  
      * PF-canon doc deltas excluding PF10, and  
      * explicit verdict and recommendation.  
      * When the QA timeline uses reconstructed ordering, the closeout record MUST state the ordering basis. PF10 addendum order MAY be used as the fallback ordering basis only when exact timestamps are absent or incomplete, and the record MUST NOT imply timestamps were observed when they were not.  
    * **Readiness / closeout recommendation (required).** The closeout record MUST state an explicit overall recommendation, such as \`Ready\` or \`Not ready\`.  
    * **Blocker accounting for recommendation.** The closeout record MUST identify the unresolved blocker set that drives that recommendation, including any must-fix canon delta, stale closeout-blocking checklist state, or other unresolved governance blocker.  
    * **Readiness / closeout recommendation (required).** The closeout record MUST state an explicit overall recommendation, such as \`Ready\` or \`Not ready\`.  
    * **QA-first closeout ordering.** All required QA tasks, remediation loops, runtime-proof checks, and close-gate QA reviews MUST be completed before documentation drainage begins.  
    * **PF10 temporary truth home for undrained documentation deltas.** If a canon delta, checklist delta, guide delta, or other documentation correction is known but not yet drained, PF10 is the controlling temporary source of truth for that item until drainage occurs  
    * **Documentation drainage is non-blocking.** Undrained changes to canon, checklist rows, guides, summaries, or other documentation MUST NOT be used as a blocker for finishing QA execution, issuing step verdicts, issuing epic QA closeout review, or deciding epic close posture, provided PF10 explicitly records the truth of what happened and the required QA proof is otherwise complete.  
    * **Allowed blockers remain limited to QA truth and proof.** The closeout record MUST identify the unresolved blocker set that drives the recommendation. Allowed closeout blockers are limited to incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved \`FAIL\_BEHAVIOR\` / \`FAIL\_TOOLING\` / \`TOOLING\_BLOCKED\` conditions that affect acceptance, or missing required close-gate QA artifacts. Documentation drainage itself is not an allowed blocker.  
    * **Record, then drain later.** When a documentation mismatch or canon delta is found during QA or closeout, it MUST be recorded in PF10 as a follow-up, implementation gap, ADR note, or doc-delta item. It MUST NOT be converted into a pre-drain closure blocker solely because the destination PF document has not yet been updated.  
    * **Supportable versus drained status wording is required.** When repo evidence supports a status change for a checklist row, guide row, or other governed document state that has not yet been drained into the destination PF document, the closeout record and any related governance report MUST say so explicitly. It MUST distinguish “supportable from repo evidence” from “already drained into canon,” and it MUST NOT imply that the destination PF document has already been updated when it has not. Once the destination PF document is updated, the record MAY state the status as drained or canonical.  
    * **No artifact may require its own drainage to be valid.** A closeout record, approval artifact, review artifact, acceptance map, token↔evidence matrix, step log, OPS task, PR summary, or related governance artifact MAY recommend later drainage, note drain targets, or identify required future canon updates, but it MUST NOT require that those drains already be completed in order for the current artifact's verdict or recommendation to stand.  
    * **Drain-required wording is non-conforming.** Any wording that says or implies \`drain required before close\`, \`cannot pass until PF10 is drained\`, \`not ready because canon is not yet drained\`, \`PF update required before acceptance\`, or any equivalent formulation is non-conforming and MUST be corrected.  
    * **Later-drain update statement is required.** Any PR approval, OPS-task approval, remediation acceptance, close-pack approval, or other approval artifact that is intended to support later PF-canon drainage MUST include an explicit later-drain PF-canon update statement. Approval is not the drain itself, but the artifact MUST make the later drain concrete, reviewable, and non-ambiguous.  
    * **Required later-drain fields.** Such an approval artifact MUST state: the affected PF canon home or homes, the exact affected locator or locators, the current canon posture, exactly one supported later-drain action (\`change to Done\`, \`change to Partial\`, \`change to Not done\`, \`change to Consolidation pending\`, \`change to Optional\`, or \`No status change recommended\`), exactly one drain readiness classification (\`Supportable from repo evidence\`, \`Not yet supportable from repo evidence\`, or \`Already drained into PF-canon\`), the evidence basis for that posture, and the epic-close expectation (\`at epic close\`, \`after an additional PR or OPS slice\`, or \`after a separate canon-only drain step\`).  
    * **Pre-drain status distinction is mandatory.** Before PF09 is drained, review and closeout artifacts that speak about mapped PF09 work MUST distinguish the current PF09 recorded status, the supported later-drain status, the actual implemented state, the actual OPS state, and the actual governed evidence state. Vague approval language such as accepted, complete, merge-ready, approved, or no further remediation needed is non-conforming when the practical intent is to support a later PF-canon update but the later drain target is left unstated.  
    * **Single authoritative posture per governed evidence family.** For any single bounded task and any single claimed closure dimension, the governed evidence family MUST express exactly one authoritative posture. Contradictory \\\`closed\\\`, \\\`not yet closed\\\`, \\\`deferred\\\`, \\\`partial\\\`, or equivalent closure meanings for the same dimension inside the same governed family are non-conforming.  
    * **Mixed-state family blocks acceptance.** A review, consolidation artifact, or closeout artifact MUST NOT summarize or approve a governed evidence family that remains internally contradictory. It MUST classify that condition as a documentation/evidence failure until the family is normalized.  
    * **Documentation/evidence normalization may replace rerun when runtime facts are unchanged.** When the underlying runtime facts are unchanged and already evidenced, and no new runtime command, environment binding, route behavior, or ops action is being claimed, remediation MAY be a documentation/evidence normalization pass rather than a fresh runtime rerun. In that case, all affected governed artifacts in the family, plus any required Human Index, Machine Mirror, checksum, and sibling path-proof companions, MUST be refreshed coherently in the same change, and any prior contradictory bundle or report MUST be treated as superseded evidence rather than as a parallel truth surface.  
    * **Closure mode must be explicit when equivalence is used.** If a closure or supportability claim relies on equivalence rather than a separately exercised runtime, the approval artifact or governing plan MUST state that exact closure mode explicitly before the governed evidence family is rewritten.  
    * **Runtime failure versus documentation/evidence failure must be classified separately.** When runtime behavior is stable but the governed evidence family disagrees internally, the condition MUST be classified as a documentation/evidence failure rather than a runtime or implementation failure. Additional reruns are not required unless the runtime facts themselves are missing, changed, or contradicted.  
    * **Post-QA drain ordering is mandatory.** Drainage into canon, checklist rows, guides, or other document homes occurs only after all QA tasks for the epic are complete.  
    * **Truthfulness still applies.** This rule changes timing, not honesty requirements. PF10 MUST still state open doc deltas, remaining follow-ups, and any caveats plainly and explicitly.  
    * **QA-pass is necessary but not sufficient.** A positive step-level QA record does not by itself authorize epic closeout when the closeout record still identifies unresolved allowed blockers. If QA evidence is complete and trustworthy and all required QA tasks are complete, the epic MAY be recommended \`Ready\` even when undrained documentation deltas remain. Undrained documentation deltas alone do not justify a \`Not ready\` verdict.  
    * Truthfulness rule for workflow claims.  
      * If a close report states that governed evidence artifacts were refreshed, re-validated, or gate-checked, that statement MUST be backed by same-run governed execution evidence produced by the cited workflow. Template-generated or unconditional claims are non-conforming.  
    * Same-run evidence pointer rule.  
      * When the close slice touches the Evidence Index, hash sentinel, machine mirror, or their required proof companions, the close report MUST point directly, or via the manifest \`key\_outputs\` or token/evidence matrix, to the same-run gate or QA log evidence that proves the write/check workflow actually executed and passed.  
  * Close-pack manifest `key_outputs` shape (normative):  
      
    * `audit/EPIC-###_MANIFEST.json` MUST include `key_outputs` as a JSON object (map) from stable names → repo-relative artifact paths.  
        
    * `key_outputs` MUST NOT be a list.  
        
    * Additional `key_outputs` entries are allowed.  
        
    * All `key_outputs` entries MUST resolve to existing, non-empty files at closure time (no dangling references). Missing or dangling `key_outputs` targets are closure-blocking.  
        
    * When closeout companion ledgers exist under `audit/docdeltas/`, the close-pack SHOULD make them discoverable via either (a) `key_outputs` bindings or (b) explicit close-report pointers to their canonical paths.  
        
    * **Structural self-check (recommended).** The repo SHOULD maintain an automated guard (test or checklist input) that asserts the close-pack path-of-record exists and that every referenced `key_outputs` path resolves to a non-empty file, to catch partial applies or missing hunks before closeout.  
        
    * **No tokenization by default.** Plans, acceptance maps, token/evidence matrices, and step logs MUST NOT mint, claim, or require a `CLOSE_PACK_FILES_PRESENT_OK` token (or any similar close-pack presence token) unless Governance explicitly registers it as a token in §2.0 (which this drain explicitly does not do).  
        
    * **No relocation.** Do not relocate the close-pack pair into `audit/qa/**` or `artifacts/**` without an explicit canon change. Any extra copies elsewhere are convenience-only and MUST NOT be used for acceptance binding.  
        
    * **Packaging/evidence-only closeout slices.** A closeout slice whose sole purpose is to surface, bind, or verify the close-pack pair or companion closeout artifacts MUST remain packaging/evidence-only: it MUST NOT run or rerun QA checks, MUST NOT execute vendor calls, MUST NOT modify implementation files, MUST NOT edit PF-Canon, MUST NOT claim PF09 drainage, MUST NOT create new acceptance claims, MUST NOT reopen implementation scope, MUST NOT change step-level QA verdicts, and MUST NOT claim merge provenance unless merge proof is itself a required governed artifact of that slice.  
        
    * **Minimum Ops execution bundle.** When such a slice executes under \`audit/ops/\*\*\`, the governed Ops bundle MUST at minimum include \`commands.txt\`, \`stdout.log\`, \`stderr.log\`, \`exit\_codes.txt\`, and \`created\_files\_sha256.txt\` under a stable lowercase ops path.  
        
    * **Replayable command transcript.** The command transcript MUST be an executable, replayable, task-labeled record of the exact commands run. A transcript that contains an invalid command for a claimed action, or that cannot be mapped to the produced artifacts, is non-conforming until repaired or explicitly superseded by a corrected governed bundle.  
        
    * **Labeled output and exit-code mapping.** Stdout, stderr, and exit-code evidence MUST be labeled and mapped to the critical command actions. Bare exit codes, unlabeled stdout, missing stderr capture, or summaries that assert validation without the corresponding captured output are insufficient for OPS acceptance. Empty stderr MAY be valid only when it is explicitly captured or represented with an integrity-checkable empty-file posture.  
        
    * **Inventory provenance.** Any final evidence inventory or checksum ledger used by the close-pack slice MUST be generated by a command whose output structure matches the persisted artifact. If the transcript and artifact disagree on table shape, row count, checksum rows, or generation method, the inventory is not trustworthy until regenerated and path-proven from current bytes.  
        
    * **Final validation.** A packaging/evidence-only closeout slice MUST include a final validation artifact when the approved task requires one. The final validation artifact MUST reconcile, as applicable, file existence, close-pack manifest bindings, close report presence, path-proofs, final inventory, checksum ledger, and the OPS evidence bundle. The validation result MUST be captured, not merely asserted.  
        
    * **Binding rule.** Such a slice MUST bind the already-proven epic acceptance or QA evidence family via the close-pack manifest \`key\_outputs\` map or explicit close-report pointers. It MUST NOT invent a replacement closeout proof surface.  
        
    * **Verification posture.** Close-pack presence is verified mechanically by artifact existence and binding to the canonical filenames (see Appendix D.0), by trustable packaging evidence when the approved slice requires it, and by the closeout review process (titles-only).

---

## **2.1 A3 — Determinism gates \[Required-Now\]**

**Canonical serializer.** All public JSON MUST be emitted by the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact separators (,/:), exactly one trailing LF. Arrays that function as sets MUST be deduplicated and ASCII-sorted.

**Two-step idempotence (preimage recipe).** Build the five-key preimage object (reader\_version, eligible, categories, meta, release\_id) without `idempotence_hash`; serialize canonically to `preimage_bytes`; compute `idempotence_hash = sha256(preimage_bytes)` (lowercase 64-hex); add it; re-serialize canonically for the final bytes.

**Pattern constraints.** `release_id` and `idempotence_hash` MUST match lowercase 64-hex: `^[0-9a-f]{64}$`.

**AB↔BA parity.** Inputs are pair-normalized; for any pair AB and BA, both the Appendix-E composite fingerprint and the final public bytes MUST be byte-identical (including the single LF). Integration channel cases (10/20/34/57 combinations, for example 20-34 vs 20-57) MUST be covered.

**Two-run identity.** Two serializations of the same logical success envelope (same inputs/environment) MUST produce byte-identical output.

**Locale discipline.** All canonicalization and comparisons run under `LC_ALL=C`.

**On-disk equality.** Public outputs MUST match their canonical re-serialization byte-for-byte (no drift between emitted bytes and canonical dumps).

### **Validation gates (binary)**

* Preimage re-check: recompute `sha256(preimage_bytes)` and match the published `idempotence_hash`.  
* AB↔BA compare: byte-compare Appendix-E fingerprints and public outputs for AB vs BA (both must match; include Integration cases).  
* Two-run compare: byte-compare two runs with identical inputs (must match).  
* Serializer hygiene: UTF-8; sorted keys; compact; one LF; no BOM; arrays-as-sets deduped and ASCII-sorted.  
* Pattern check: `release_id`, `idempotence_hash` each match `^[0-9a-f]{64}$`.  
* Canonical re-serialization: emitted bytes equal canonical dumps (file-equals-canon).

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---

## **2.2 A4 — Reader↔CLI parity \[Required−Now\]**

* **Scope.** A4 parity applies to the **Reader v1 public success envelope** (`200`) and **typed error envelopes**. The CLI participates in this gate only when it is emitting **Reader v1 bytes** (for example via `--dump-reader` sidecars; byte/sidecar contract lives by title in **HDE-CLI-API-Vendor-Ref**). This gate does **not** compare `hdctl showcompat` stdout (compatibility payload) to Reader v1 bytes.  
    
* **Single presenter/emitter.** Reader and CLI MUST call the same emitter to produce Reader v1 success and typed error bodies; no ad-hoc dumps or parallel “mini-emitters.”  
    
* **Byte equality.** For identical inputs/environment, the Reader HTTP body MUST be byte-identical to the CLI-emitted Reader v1 body bytes (including the single LF). For this gate, “CLI-emitted Reader v1 body bytes” means the exact bytes captured via the CLI `--dump-reader` output (not `showcompat` stdout).  
    
* **Canonical JSON.** Public bytes are serialized with the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. All checks run under `LC_ALL=C`.  
    
* **Public resonance posture (v1).** No SR/XR numerics appear on Reader `200`. v1 ships SR-only (alpha \= 1.0); hysteresis \= 1 is armed for future XR and not exposed.

**Schema/shape gates**

1. **Success:** exactly the six keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*]` are exactly `{ "id", "band" }` (numeric-free; `band ∈ {"Cool","Open","Warm","Glow"}`).  
     
2. **Errors:** typed, numeric-free JSON; LF-terminated; no PII.

**Validation gates (binary)**

1. **Reader↔CLI compare:** byte-compare the Reader HTTP body against the CLI-emitted Reader v1 body bytes (captured via `--dump-reader`). Compare both success bodies and typed error bodies where the CLI emits Reader v1 bytes. All comparisons MUST include the single trailing LF.  
     
2. **Shape checks:** enforce success/error schemas above (reject extras, numerics, or missing fields).  
     
3. **Emitter proof:** CI/allowlist shows both surfaces invoke the same emitter symbol.

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---

## **2.3 A7 — Transport tokens \[Required-Now\]**

**Scope.** These rules apply to Reader success endpoints. Proofs MUST be run on an Endpoint Catalog (success JSON) route in **HDE-CLI-API-Vendor-Ref**. Internal-ops `/internal/version` is excluded and governed by §10.5.

* **ETag on 200 (identity of body bytes).** Reader 200 MUST include a strong, quoted ETag. Identity is computed over the final LF-terminated body (canonical JSON per PF-Schemas & Artifacts). Compression does not change the ETag (encoding-invariant).  
* **Cache headers on 200 and HEAD.** `Cache-Control: private, max-age=0, must-revalidate` MUST be present on 200 and HEAD.  
* **304 only after a 200-with-body.** 304 MAY be sent only after a successful 200 has established an ETag. 304 carries no body, omits `Content-Type` and `Content-Length`, and repeats validators from the cached 200\.  
* **HEAD parity.** HEAD returns the same validators as 200 and no body. `Content-Length` equals the identity 200 body length (canonical LF-terminated bytes). `Content-Type` on HEAD equals GET.  
* **Writers and errors: no-store; no ETag.** All writer and error responses MUST include `Cache-Control: no-store` and MUST NOT include an ETag. Error responses MUST include `Content-Type: application/json; charset=utf-8`.  
* **Content-Type on 200\.** Success 200 MUST include `Content-Type: application/json; charset=utf-8`.  
* **Vary policy.** Reader responses MUST set `Vary: Authorization, Accept-Encoding` to prevent cache mixing and prove encoding-invariance separately.  
* **POST is non-conditional.** POST MUST NOT honor conditional validators; treat as non-conditional write/compute.

**Validation gates (binary; prove on a cataloged success endpoint)**

1. 200: strong quoted ETag present; `Cache-Control: private, max-age=0, must-revalidate` present; `Content-Type: application/json; charset=utf-8` present; encoding-invariance proven (same ETag across accepted `Accept-Encoding`).  
2. 304: only after a prior 200; no body; validators mirror 200; omit `Content-Type` and `Content-Length`.  
3. HEAD: validators mirror 200; no body; `Content-Length` matches identity 200 body; `Cache-Control: private, max-age=0, must-revalidate` present; `Content-Type` equals GET.  
4. Writers and errors: `Cache-Control: no-store` present; no ETag; errors include `Content-Type: application/json; charset=utf-8`.  
5. POST: treated as non-conditional (ignore `If-*` conditionals).

*Tokens: see §2.0 Acceptance Tokens (A-gates roster; Reader A7 and READER\_* tokens).\*

# 3\) Rails & Environments (Vendor posture) \[Required-Now\]

## **3.1 SAFE rails default ON \[Required-Now\]**

SAFE rails for **vendor HTTP** are **default closed** in all environments. Opening rails is an explicit, governed action with evidence and tokens.

### **Public traffic (Reader/Aux)**

* Prod public surfaces (Reader JSON success, Aux narrative) must serve requests **without** vendor HTTP.  
    
* **BG\_VENDOR\_CALLS\_DISABLED\_IN\_PROD\_OK** asserts that public traffic in prod is **DB-backed only**; the Engine does not call vendor HTTP to satisfy public Reader/Aux requests.  
    
* Any vendor-originated data used in prod public responses must arrive via prior ingest and DB, not live vendor calls.

### **Admin ops windows (vendor override)**

* Ops may run vendor calls in prod.  
    
* Vendor override is driven by CLI flags.  
    
* When override is enabled:  
    
  * SAFE rails tokens in §2.0 apply:  
      
    * Bounded retry and backoff (**VENDOR\_RETRY\_BACKOFF\_OK**).  
        
    * Typed 429 handling (**PROVIDER\_429\_TYPED\_OK**).  
        
    * `Retry-After` parsing (**RETRY\_AFTER\_PARSE\_OK**).  
        
    * No payload logging (**VENDOR\_NO\_PAYLOAD\_LOGGING\_OK**, **LOGS\_KEYS\_ONLY\_OK**).

    

  * Observability and privacy tokens (**BG\_PRIVACY\_REDACTION\_OK**, **BG\_METRICS\_EXPOSED\_OK**) remain in force.

### **Governance stance**

* **BG\_VENDOR\_CALLS\_DISABLED\_IN\_PROD\_OK** scopes to **public traffic**. It does **not** forbid admin-guarded CLI commands that call vendor in prod.  
    
* All vendor override behavior must be evidenced and indexed via artifacts governed in **HDE-Schemas and Artifacts** and **Glow QA Guide**; PF04 owns the token semantics only.  
    
  ---

## **3.2 Refusal semantics (rails closed) \[Required-Now\]**

When rails are closed (i.e., `SAFE_MODE≠0` or `ALLOW_NETWORK≠1`), vendor paths **MUST NOT** open sockets, resolve DNS, or attempt HTTP (no external I/O). This applies to **all** vendor invocations, including manual or CLI requests that explicitly set `source="vendor"`; such attempts **MUST** produce a deterministic typed refusal and **MUST NOT** perform any upstream call.

Headers (ops/error surface).  
Cache-Control: `no-store` **MUST** be present.  
Content-Type: `application/json; charset=utf-8` **MUST** be used for the refusal body.  
No `ETag`, no `Vary`, no `Content-Encoding`.  
Exactly one blank line between headers and body (see PF12 §8.3.1 for the refusal proof format).

Body (typed, numeric-free).  
Return a typed error explaining that vendor access is disabled (numeric-free JSON; LF-terminated). Do not echo provider payloads or headers.

Logs (keys-only; no secrets).  
Logs **MUST NOT** contain API keys/tokens, request/response bodies, or header values.  
If keys are referenced, they **MUST** be redacted (e.g., `HD-Api-Key: REDACTED`).  
Labels remain bounded (e.g., `route`, `outcome`, `rails_state`); no PII.

Refusal log allow-list (frozen).  
Refusal logs are limited to the exact seven-key set: `{at, route, status, duration_ms, idempotence_hash, release_id, correlation_id}`.  
`correlation_id` MUST be one validated, opaque, bounded, non-PII request-scoped identifier selected or generated at the Adapter boundary and propagated unchanged for that request. Missing or invalid inbound values MUST be replaced safely and MUST NOT be logged raw. The value MUST NOT enter a public or refusal body, `idempotence_hash`, `ETag`, Human Design computation, Magic-10 results, or metric labels.  
`retry_after_ms` remains outside this refusal schema; it belongs only to 429 evidence.

Current implementation posture (static).  
The pinned repository's inspected logging paths and tests enforce six-key records and do not establish the seven-key refusal record. This remains a Required-Now implementation gap; static inspection does not establish runtime logging behavior.

Deterministic shaping (optional).  
Request shapes (endpoint, headers, body schema) may be computed without sending the request; shaping must be deterministic and order-neutral (AB↔BA).

Canonical probe route.  
Expose a single refusal probe at `/ops/rails/refusal`:

* `GET`/`POST` → 503 single-file capture (headers → blank line → LF-terminated JSON),  
    
* `OPTIONS` → 204 no body,  
    
* `HEAD` → 405 with `Content-Length: 0`,  
    
* no ETag/Vary/compression.

(Evidence artifact shape lives in PF12 §8.3.1.)

CI posture (must).  
CI must prove:

* No network I/O occurs under closed rails.  
    
* The typed refusal is produced with the required headers/body.  
    
* Logs are keys-only and secret-free (no payloads/headers).

Tokens (titles-only; see §2.0).  
`NO_EXTERNAL_IO_ON_REFUSAL_OK` · `ERROR_CTYPE_JSON_UTF8_OK` · `NO_CONTENT_ENCODING_OK` · `PF04_LOG_ALLOWLIST_009_OK` · `REFUSAL_ROUTE_PINNED_OK` · `OPS_REFUSAL_FILE_FORMAT_OK` · `OPS_REFUSAL_HEADERS_OK` · `OPS_REFUSAL_BODY_OK` · `OPS_REFUSAL_MIRROR_LINK_OK`

Routing (titles-only).  
Transport matrix & writers posture: §10 of this document.  
Evidence/mirror hygiene (same-PR, canonical JSONL, unknown-key reject, `proof_anchor`): **HDE-Schemas & Artifacts** / **Epic-Process-Guide**.  
Infrastructure names for admin credentials/rails: **Glow Infrastructure** (names-only).

---

## 3.3 Secrets & env validation \[Required-Now\]

* **Validate against canonical env and infrastructure homes (names-only allow-list).** Before any vendor action, validate required environment keys from the canonical env and infrastructure homes (names only; secrets not printed). `ALLOW_NETWORK`, `SAFE_MODE`, and `APP_ENV` are rails-governance keys. `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` are infrastructure/vendor configuration keys, not acceptance tokens. `HDAPI_BASE_URL` is deprecated compatibility spelling only where implementation or migration evidence explicitly records it. If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` are present with different values, fail closed with configuration ambiguity before network I/O. Unknown keys **must** be flagged in CI; missing required keys **must** fail at prod start.  
  **Required (examples):** `HD_API_BASE_URL` (vendor base URL), `HD_API_KEY` (secret), `GEO_API_KEY` (secret).  
  **Failure posture:** if rails are **open** but any required key is invalid/missing, the provider **MUST refuse** with a typed error; **do not** attempt partial requests or fallbacks.  
* **Environment-key drift is governance-relevant when it affects rails, secrets, or evidence.** A key-name mismatch, deprecated alias, ambiguous duplicate value, or missing canonical key is a governance-relevant operational risk when it can affect rails posture, secret handling, public/private boundary, acceptance evidence, or vendor request shaping. Treat that condition as configuration drift or tooling blockage, not as a reason to invent an acceptance token.  
* **Redaction rules (keys-only logs).** Never log secrets, request/response bodies, or header values. When secrets are referenced, print **redacted placeholders only**. Labels remain bounded; **no PII**, **no free-text** payloads.  
* **Deterministic diagnostics.** Configuration checks and refusal messages **MUST** be deterministic and order-neutral; **no** locale/time/random dependencies (run under `LC_ALL=C`).  
* **CI checks.** Add tests that (a) **fail fast** on missing/empty env, (b) assert refusal posture with **no network I/O**, and (c) **grep-guard** logs to ensure no secrets or payload bodies appear.

---

## 3.4 Open rails (controlled) \[Required-Now\]

* **Explicit enablement only.** Opening rails is **explicit** (env/config). Reader/CLI behavior and canonical bytes remain **unchanged** (same presenter/emitter; public payload numeric-free).  
* **Pinned network policy (by title).** When open, live calls follow **pinned timeouts, retries, and backoff**; vendor error mapping is **deterministic** and **typed**; **no** payloads/secrets in logs.  
* **Parity & idempotence remain intact.** Enabling rails **must not** change Reader↔CLI parity, **A7 conformance**, or **idempotence** proofs.  
* **Evidence.** Provide **records-only** machine-mirror entries for:  
  (a) **closed-rails refusal** proof,  
  (b) **open-rails conformance** run (with redaction checks), and  
  (c) **env-validator outputs** per environment.  
  *(PF12 single home; same-PR updates apply.)*

**PR-specific bounded development-proof exception.** An explicitly Product Owner-authorized, PR-specific, bounded open-rails vendor development proof MAY occur inside an implementation PR only when the authorization defines the non-production or override truth, an exact request limit, a secret-safe evidence shape, a prohibition on ordinary-CI live calls, and explicit nonclaims. This exception does not create recurring authority, does not create general agent OPS authority, and does not substitute for fixture-backed deterministic proof. It does not change the classification of ordinary open-rails vendor smoke as Ops evidence or convert OPS evidence into PR or QA evidence.

**HDAPI v2 open-rails vendor proof posture.** A controlled HDAPI v2 open-rails smoke is an Ops evidence task when it requires secrets or privileged runtime posture. It MUST be Product Owner-authorized, IA-guided, secret-safe, and stored under a lowercase audit ops path. “PO-only” identifies the Product Owner as the authorizing and accountable principal; it does not require the PO to be the physical executor after explicit delegation. A PO-delegated automated session agent MAY execute the exact authorized vendor call only within the task-specific scope, rails, request limit, stop checks, redaction, and evidence contract. No executor may claim completion without the required secret-free OPS evidence or simulate external state.

Before execution, the task record and evidence MUST prove the exact command or approved command family, PF07-backed target facts or an explicit PF07-gap blocker posture, safe secret posture, source-selection posture, v2 route family, expected request class, and acceptance target. Missing exact command, missing credentials, missing target facts, missing authorization, or unresolved placeholders classify the result as `TOOLING_BLOCKED` and the vendor call MUST NOT run.

The evidence bundle MUST capture commands, stdout, stderr, exit codes, redacted environment presence, request summary, result summary, and checksum inventory in a secret-free posture. It MUST NOT persist plaintext secrets, header values, request or response bodies beyond the approved evidence shape, or vendor payload echoes.

The result is `FAIL_TOOLING` if secret-bearing output is persisted. The result is `FAIL_BEHAVIOR` only when command, credentials, safe posture, source selection, target facts, and evidence shape are proven and the runtime behavior contradicts the expected vendor behavior. Open-rails success does not by itself claim QA PASS, Live QA completion, PF09 status change, epic closure, public Reader change, new route, new acceptance token, or PF-canon drainage.

**Production-affecting epic live-proof requirement.** For any epic that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence or retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret-binding behavior, request shaping, response mapping, authentication or authorization, production-used CLI/API behavior, queues, workers, jobs, schedulers, runtime services, or any path that must work outside isolated closed-rails fixtures, the Live QA Plan MUST include at least one bounded open-rails live QA step before acceptance unless an explicit approved exemption is recorded.

Closed-rails tests, repo tests, static analysis, generated evidence artifacts, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, Codex audit, implementation review approval, QA Plan approval, PF10 supportability notes, a written smoke procedure, or OPS discovery without live behavior proof may support the QA package, but they do not replace the required open-rails live QA step for production-affecting work.

The required live step must prove at least one real production-relevant behavior the epic could affect. It must be bounded, non-destructive unless explicitly approved, PO-authorized where secrets, external services, or deployed environments are involved, secret-safe, evidence-recorded, scoped to the actual production risk, clear about what it proves, and clear about what it does not prove.

Open-rails live QA proves only what it exercises. It does not mint new acceptance tokens, satisfy unrelated tokens, prove full vendor conformance, move unrelated PF09 rows to Done, complete epic closeout, change public Reader scope, authorize new routes, or complete PF-canon drainage by itself.

For this requirement, user or production surfaces include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor transport, vendor route policy, vendor request shaping, vendor response handling, HumanDesignAPI auth/header behavior, BodyGraph vendor ingest, vendor response normalization, vendor error/retry/rate-limit behavior, configured base URL behavior, environment-key binding behavior, database persistence or retrieval, runtime compute, deployed service behavior, and admin or ops-facing behavior that can affect production truth.

QA readiness, Live QA Plan approval, QA review, and closeout review MUST account for the required open-rails step. A Live QA Plan, QA-readiness review, or closeout-review posture is substantively blocked when the epic affects user or production surfaces, no bounded open-rails QA step is included, and no controlling PO-authorized or PF-canon exemption is recorded. The blocker language should state that open-rails QA is required because the epic affects user or production surfaces and closed-rails-only QA is insufficient, then identify the affected surface.

The open-rails requirement is not satisfied by closed-rails tests, unit tests, static validation, schema validation, evidence-index validation, Machine Mirror validation, path-proof validation, command syntax validation, dry-run-only closed-rails proof, fixture-only proof, mock-only proof, repo inspection, prior epic evidence not explicitly bound to the current epic’s open-rails proof need, OPS observation not bound into QA evidence, or a statement that open-rails QA is unnecessary without a recorded controlling exemption.

A valid exemption must be explicit. It must state why no open-rails behavior can be safely or meaningfully exercised, what risk is accepted, what proof substitutes for open-rails QA, why the substitute is sufficient for the epic, and what future work must still perform open-rails proof if any. Silence, reviewer preference, convenience, or closed-rails success is not an exemption.

**Route-family proof is not workflow proof.** A bounded open-rails vendor observation proves only the exact command family, route family, auth posture, credential-binding posture, request class, and evidence shape it exercises. A successful observation on one vendor route family MUST NOT be treated as proof that another CLI workflow, route family, adapter path, BodyGraph cache path, compat path, or app-integration path is conformant.

If a vendor observation shows that a workflow is exercising a legacy route family, an unsupported configured-base combination, or a route/header posture different from the intended v2 chart/geokey proof target, classify that result as a bounded runtime or request-shaping gap. Do not collapse it into full provider failure, full product failure, full v2 runtime conformance, or PF09 parent completion without a later governed proof that exercises the actual target path.

A Live QA Plan for a production-affecting epic is not approval-ready if it is closed-rails-only unless it records an explicit exemption. The exemption must state why open-rails live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release. This is a truth and proof requirement, not a formatting preference.

Secret safety remains mandatory. Open-rails live QA may record key names, redacted values, header names, redacted header-shape posture, environment label, endpoint family, status class, safe redacted response excerpts, and bounded result classifications. It MUST NOT record raw API keys, raw bearer tokens, raw database passwords, raw request secrets, raw private payloads, unapproved unredacted vendor response bodies, or uncontrolled production data.

**Controlled vendor-backed no-user validation.** When a remediation, OPS task, QA correction, or closeout review claims vendor-backed no-user behavior, PF04 distinguishes these proof classes:

* public numeric-free output proof  
* internal or admin compatibility-compute proof  
* vendor-backed no-user behavior proof

Local tests, grep checks, fixture-only `person_uid` injection, or internal compute evidence MAY prove their own labeled proof class only. They MUST NOT substitute for vendor-backed no-user behavior proof when the claim is live no-user behavior in a pre-App or no-user context.

**No-user meaning for controlled vendor smoke.** For a controlled vendor-backed no-user smoke, the caller-facing or operator-facing command input MUST be birth-data-only or otherwise identity-free according to the approved slice. It MUST NOT require app user IDs, `user_id`, caller-provided `person_uid`, DB-backed user records as caller input, source-db caller posture, or inline secret values. If implementation creates deterministic internal metadata inside the resolver or compute boundary from approved no-user input, that metadata MUST remain internal and MUST NOT become a caller contract, public route field, public flag, or public proof substitute.

**Discovery and prerequisite posture.** Discovery-only prerequisite work MAY complete its own bounded discovery purpose when it truthfully records the command candidate or unresolved disposition, command ledger, presence-only environment state, checksum inventory for captured files, and explicit non-claims. Discovery-only evidence MUST NOT be read as vendor behavior proof, QA PASS, Live QA completion, PF09 status change, or epic closure.

A controlled vendor-backed no-user smoke MAY run only when explicitly approved for that slice and only after the required command discovery and remediation prerequisites are satisfied. It MUST be PO-only, IA-guided, limited to the explicit open-rails vendor step, and secret-free in persisted evidence. It MUST use no app user IDs, no caller-provided `person_uid`, no guessed command, no guessed host or port, no guessed URL, no guessed service binding, no guessed target, no guessed environment fact, and no unresolved placeholder-bearing command.

**Target fact posture.** Before the smoke may run, the evidence record MUST prove the exact placeholder-free command, safe secret posture, required PF07-backed target facts or an explicit PF07-gap blocker posture, no-user input shape, explicit vendor source posture, and PO authorization for the controlled vendor step. If the target is a local CLI vendor smoke, hosted-service target facts are not required unless the command is changed to call a hosted HTTP service. If the target changes to a hosted HTTP service call, the evidence record MUST prove the PF07-backed hosted target facts or classify the result as blocked by missing infrastructure inventory before execution.

**Preflight and execution classification.** If the exact command is unresolved, placeholder-bearing, or missing; if required sample input is absent or incomplete; if required vendor credentials are false or uncaptured; if required target facts are missing; if the command includes forbidden user identity input; if the vendor source is not explicit; if the open-rails posture for the vendor step is absent; if determinism pins are absent; or if PO authorization is absent, the result is `TOOLING_BLOCKED` and the vendor call MUST NOT run.

If secret-bearing output is written to logs, summaries, command captures, stdout, stderr, JSON, or other persisted evidence, the result is `FAIL_TOOLING`. Any secret-bearing artifact MUST be quarantined, named in the result summary, and excluded from proof.

If command, credentials, safe posture, no-user input shape, vendor source, and target facts are proven and the runtime output contradicts the expected no-user vendor behavior, the result is `FAIL_BEHAVIOR`.

Use `PASS` only when all preflight rows pass, the exact command runs, exit code is `0`, the command uses the approved vendor source and no-user input shape, no app user ID, `user_id`, or caller-provided `person_uid` is supplied, no secret values are persisted, stdout is non-empty and parseable as JSON unless the command’s documented success output differs, and the result summary states that the evidence is implementation-validation evidence only.

**Evidence-output posture.** The governed evidence bundle for a controlled vendor-backed no-user smoke MUST record the exact command actually executed, the approved no-user input values or presence-only input posture, redacted environment presence as key names and booleans only, request summary, stdout, stderr, exit code, result summary, prerequisite or completion matrix, and checksum inventory for captured files. The evidence bundle MUST preserve command provenance and MUST NOT silently alter the acceptance target.

Do not edit the command after a failed run to force `PASS`. Do not retry with different flags, URLs, hostnames, ports, credentials, target facts, or input values unless the change is PF07-backed or PF10-backed and recorded in the result summary.

Controlled vendor-backed no-user smoke evidence is implementation-validation evidence only. It does not by itself claim QA PASS, Live QA completion, PF09 status change, epic closure, a new public route, a new public flag, a new public surface, a new CLI flag, a PF-canon drain, or a new acceptance token.

**Tokens:** see **§2.0 Acceptance Tokens** (A-gates roster).

---

# **4\) Evidence & Artifacts \[Required-Now\]**

## **4.1 Classes of evidence \[Required-Now\]**

What must be proved for every cut (**binary gates; no partial**). Index all governed artifacts through the Human Evidence Index and Machine Evidence Mirror owned by **HDE-Schemas & Artifacts**, and keep those evidence surfaces synchronized with repo changes. All byte-comparisons and hashes run with **LC\_ALL=C, TZ=UTC**, and **canonical JSON** (UTF-8 no BOM, ASCII-sorted keys, compact, **exactly one LF**; arrays-as-sets are deduped and ASCII-sorted).

### **4.1.1 Parity — Reader↔CLI, AB↔BA, two-run**

* **Reader↔CLI byte identity.** For identical inputs and environment, the Reader v1 HTTP body and CLI-emitted Reader v1 parity bytes captured via `--dump-reader` are bit-identical (single presenter/emitter; same `idempotence_hash`; one trailing LF). This comparison does not apply to `hdctl showcompat` stdout.  
* **AB↔BA identity.** Swapping pair order yields bit-identical bytes (pair normalization in effect). Include AB/BA composite fingerprint cases and a byte-compare log; cover integration channel examples.  
* **Two-run identity.** Two serializations of the same logical invocation produce bit-identical bytes.  
* **Evidence.** Parity runs and goldens; AB/BA and two-run logs; CI byte-diff jobs; **machine-mirror** records (records-only) for each capture.  
* **Tokens.** `CLI_READER_PARITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`.

**Checksum sidecars (naming and optionality).**

* **Showcompat parity artifacts.** The canonical checksum sidecar filename is `stdout.json.sha256` (JSON-filename-qualified). If a legacy alias is required for backward compatibility (for example `stdout.sha256`), it MUST be byte-identical to the canonical checksum sidecar and MUST NOT be the primary name used for Evidence Index bindings.  
    
* **Identity artifacts under `audit/qa/<epic-id>/artifacts/identity/`.** `.sha256` sidecars for JSON files are optional helper artifacts unless the epic acceptance roster explicitly lists them as required. Optional checksums MUST be generated mechanically (for example `sha256sum`) and may be indexed as helper artifacts; they MUST NOT be used as gating evidence unless registered as required by acceptance canon.

### **4.1.2 Idempotence recompute — preimage → sha256 → final**

* **Preimage check.** Remove `idempotence_hash`; canonicalize the defined preimage fields (see **HDE Math Spec**); verify `sha256(preimage_bytes) == idempotence_hash`.  
* **Evidence.** Recompute logs and script; env pins recorded (**LC\_ALL=C, TZ=UTC**); mirror records with sha256 and proof.  
* **Tokens.** `PREIMAGE_RECOMPUTE_OK`, `JSON_CANONICAL_CHECK_OK`.

### **4.1.3 A7 transport — validators and conditional delivery**

**Proof surface.** Prove on a **CLI/API/Vendor Ref Endpoint Catalog JSON success** route (titles-only). **/internal/version is excluded.** The Catalog is **internal-only** and **env-gated**; non-prod entries **must be unreachable in prod** (capture a headers-only **env-gate proof**).

* **200\.** Strong, quoted ETag over the LF-terminated body (**encoding-invariant**).  
* **200/HEAD.** `Cache-Control: private, max-age=0, must-revalidate` present.  
* **304\.** Only after a prior 200; **no body**; **omit both `Content-Type` and `Content-Length`**; validators mirror cached 200\.  
* **HEAD.** Validators mirror 200; no body; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
* **Writers/errors.** `Cache-Control: no-store`; **no ETag**; errors include `Content-Type: application/json; charset=utf-8`.  
* **Evidence.** Header snapshots for 200, HEAD, and 304; conditional sequences; **encoding-invariance** check; **Endpoint-Catalog snapshot** and **env-gate proof**; all indexed as records-only in the machine mirror.  
* **Tokens.** `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_INTERNAL_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_ENCODING_INVARIANCE_OK`, `A7_VARY_AUTH_AE_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `READER_HEAD_ETAG_MATCH_OK`, `READER_HEAD_CL_MATCH_OK`, `A7_TRANSPORT_PROOF_OK`.

**Equivalence (titles-only).** `A7_304_OMITS_CT_CL_OK` ≡ (`READER_304_NO_CTYPE_OK` ∧ `READER_304_NO_CL_OK`); `A7_VARY_AUTH_AE_OK` ≡ (`READER_VARY_AUTHORIZATION_OK` ∧ `READER_VARY_ACCEPT_ENCODING_OK`).

### **4.1.4 Rails posture — closed refusal; open conformance**

**Closed rails (default).**  
SAFE rails for vendor HTTP are **closed by default** in all environments. When rails are closed (`SAFE_MODE≠0` or `ALLOW_NETWORK≠1`):

* Vendor paths **MUST NOT** open sockets, resolve DNS, or attempt HTTP (no external I/O).  
* All attempts to call vendor, including explicit `source="vendor"` flows, **MUST** return a deterministic, numeric-free refusal body and **MUST NOT** perform upstream calls.  
* Refusal responses **MUST** use `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, and include **no** `ETag`, `Vary`, or `Content-Encoding`; the body is LF-terminated, numeric-free JSON.  
* Logs for refusal paths are **keys-only**, secret-free, and bounded (`route`, `outcome`, `rails_state`, etc.), with secrets redacted. (Tokens: `NO_EXTERNAL_IO_ON_REFUSAL_OK`, `VENDOR_NO_PAYLOAD_LOGGING_OK`, `LOGS_KEYS_ONLY_OK`, `BG_PRIVACY_REDACTION_OK`)

**Open rails (controlled).**  
Opening rails (`SAFE_MODE=0` and `ALLOW_NETWORK=1`) is an **explicit, governed action**:

* Network policy (timeouts, retries, backoff, 429 behavior) is pinned by Governance and **must** remain deterministic and keys-only in logs.  
* Live vendor calls **must not** change Reader↔CLI parity, A7 conformance, or idempotence proofs.  
* Evidence includes a governed **open-rails conformance** run (vendor success, retry, 429 paths) captured as records-only artifacts and indexed in the Evidence Index and machine mirror under the tokens listed in §2.0 (for example, `VENDOR_RETRY_BACKOFF_OK`, `PROVIDER_429_TYPED_OK`, `RETRY_AFTER_PARSE_OK`, `VENDOR_NO_PAYLOAD_LOGGING_OK`).

**Dev/admin APP\_ENV gating (dev/test/local only) NEW CANON.**

Dev/admin-only surfaces that exercise engine internals under controlled rails (for example, CLI dev harnesses, internal/dev HTTP sampler routes, and similar tools called out in **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide**) **MUST** enforce strict `APP_ENV` gating:

* Allowed `APP_ENV` values for these dev/admin surfaces are exactly `{"dev","test","local"}`.  
    
* If `APP_ENV` is **missing**, **empty**, or any other value (including `"prod"` or any unrecognized string):  
    
  * The surface **MUST** treat this as a **rails violation**,  
  * **MUST** fail closed with a typed, numeric-free error (for CLI) or a writer-style refusal envelope (for HTTP),  
  * **MUST NOT** assume a default (for example, treating missing/empty as `"dev"`), and  
  * **MUST NOT** perform sampler/core/vendor work on that invocation.


* Gating behavior is part of the rails contract: tests and QA harnesses (named by title in Glow QA Guide and HDE-Build Checklist) **MUST** prove that dev/admin-only surfaces cannot be invoked successfully when `APP_ENV` is missing, empty, or outside the allowed set.

This `APP_ENV` gating is a precondition for treating any dev/admin-only surface as “on-rails”; it couples to `ENV_RAILS_POLICY_OK` in §2.0.10 and applies regardless of whether vendor rails are open or closed.

**Determinism env pins harness (EPIC018 D2)**

For determinism-sensitive suites (serializer identity, AB↔BA, evidence ordering/orientation, and other invariance tests named in HDE-Mechanics Guide and Glow QA Guide), rails policy is further constrained.

Canonical determinism env pins. Determinism suites MUST run under the closed-rails env tuple:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* LC\_ALL=C  
* LANG=C  
* TZ=UTC

These pins are mandatory for any job that produces or verifies governed determinism evidence (including engine/order identity proofs and topology orientation demos). This tuple extends the EPIC017 default for CLI/evidence/ordering/registry jobs called out in §2.0.10.

Canonical implementation (helper \+ CI). The env pins are implemented by a single helper module (`engine/runtime/determinism_env.py`) that defines the pinned env map and exposes a typed API for checking/applying pins and rendering an env-pins log. CI wires this helper into determinism suites via job-level env in `.github/workflows/ci.yml` and a dedicated env-check script (for example `ci/checks/check_env_pins.sh`) that fails closed when pins are missing, mismatched, or unset. Mechanics and tests for this helper live in HDE-Mechanics Guide and the repo’s invariance test suite; PF04 owns only the policy and token semantics.

Evidence surfaces (single canonical surface). Determinism env pins produce a governed env-pins evidence artifact family. The only valid evidence surface for DETERMINISM\_ENV\_PINS\_OK is:

* `audit/gates/determinism/env_pins.log` (records-only; canonical JSON; LF-terminated; records the env map and determinism suite set), and  
* `audit/gates/determinism/env_pins.log.path_proof.txt` (proof\_anchor path-proof).

Other env pins snapshots may exist for other proof contexts. They do not satisfy DETERMINISM\_ENV\_PINS\_OK unless they are the canonical governed log surface above. Any binding to another path (for example, `artifacts/proofs/env_pins.txt`) is a mechanical blocker.

The evidence catalog entry (artifact\_key), schema, and Index/mirror mapping are owned by HDE-Schemas & Artifacts. PF04 pins the allowed binding and requires ledgers and indexes to reference it exactly (see §9.7.9).

The schema, artifact path, and Index/mirror mapping for this family live in HDE-Schemas & Artifacts and Glow QA Guide; PF04 references them by title only and treats them as the normative evidence surfaces for determinism env rails.

Tokens and coupling.

* ENV\_RAILS\_POLICY\_OK and ENV\_LC\_ALL\_C\_OK (see §2.0.10) together assert that the closed-rails tuple is enforced for determinism suites and that dev/admin APP\_ENV gating is in place for the relevant surfaces.  
* Determinism env-pins artifacts and their mirror records couple to DETERMINISM\_ENV\_PINS\_OK in §2.0.1, which remains the single determinism-env token for A-gates.

### **4.1.5 Bands — inclusive-high thresholds (by preset)**

* **Boundaries.** Proof goldens at **24/49/74/100**; show \+1 transitions (see **HDE Math Spec**); 100 → Glow.  
* **Evidence.** Band-edge snapshots and diffs; mirror records.  
* **Tokens.** `BAND_MAX_INCLUSIVE_OK`, `BAND_EDGE_GOLDENS_OK`.

### **4.1.6 Pack constants and release identity**

* **Constants pack.** Snapshot of frozen keys (limits, thresholds, resonance inputs as applicable) and hashes.  
* **Manifest and `release_id`.** `catalog/manifest.json` is the sole tracked release-identity input; recomputation proves `release_id = sha256(canonical_manifest_bytes)`.  
* **Current release provenance.** Current release-bound derivatives belong to an external `hde.release_attestation.v1` bundle produced outside the source tree from an exact clean source commit and independently verified against that exact source.  
* **Admission boundary.** The external CI artifact is exact-head PR evidence. It does not mint or satisfy an acceptance token, create release admission by implication, constitute a durable governed release-admission record, replace a required downstream evidence-admission action, or update PF09 or closeout status.  
* **Historical checked-in release evidence.** Existing checked-in release evidence and companions are frozen capture-time records. They are not current runtime identity inputs or current attestations, MUST NOT be relabeled as current provenance, and MUST NOT be regenerated merely because the manifest or release ID changes.  
* **Tokens.** `PACK_ROOT_PINNED_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `RELEASE_ID_FROM_MANIFEST_OK`.

### **4.1.7 Topology loader — orientation and graph invariants**

* **Orientation.** Channel IDs are min→max, zero-padded **NN-NN**; arrays-as-sets deduped and ASCII-sorted.  
* **Integration invariants.** Only gates **10/20/34/57** have degree \= 3; all others \= 1\. Center-pair multiplicities sum to **36**; fail closed on mismatch.  
* **Evidence.** Orientation demo; degree and multiplicity logs; machine-mirror entries.  
* **Tokens.** `CATALOG_ORIENTATION_CANON_OK` (and related topology tokens in Evidence & Artifacts).

**Pass criteria.** All classes pass (parity, idempotence, A7, rails, bands, pack constants/manifest, topology) with evidence cataloged through the Human Evidence Index and Machine Evidence Mirror owned by **HDE-Schemas & Artifacts** and CI gates enabled (grep-guards for ad hoc emitters; LF/encoding checks; A7 cache header and ETag/no-ETag checks).

### **4.1.8 Sanity pipeline & evidence skeleton (EPIC018+)**

**Scope.** This class covers a **closed-rails sanity pipeline** that orchestrates core governance checks in a single, deterministic run and proves that the evidence skeleton (INDEX, hash sentinel, machine mirror, and path-proofs) is coherent. It does **not** replace individual tests; it is an additional, merge-gating harness.

**Pipeline entrypoint (normative).**

* The canonical sanity entrypoint **MUST** be `python tools/evidence/run_sanity_pipeline.py`.  
    
* Before running any checks, the pipeline **MUST** assert and/or apply the canonical determinism env pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) via the determinism env helper; failures **MUST** stop the pipeline.  
    
* The pipeline **MUST** then run a fixed, ordered sequence of steps that at minimum covers:  
    
  * serializer determinism/idempotence checks (A3),  
      
  * determinism env pins verification (DETERMINISM\_ENV\_PINS\_OK),  
      
  * CLI serializer/guard checks for compat/Reader parity (A4),  
      
  * evidence index/mirror/path-proof checks and orientation/skeleton demos (PF12 evidence skeleton), and  
      
  * any additional invariance suites identified in **HDE-Mechanics Guide** and **Glow QA Guide** as part of D1–D4.


* The pipeline **MUST** be fail-fast: on the first failing step, it records the failure and emits a `summary:FAIL` line, then exits with a non-zero status code.

**Sanity log artifact (records-only; governed).**

* The pipeline **MUST** write a canonical sanity log at `audit/gates/sanity_pipeline/sanity_pipeline.log` (+ required sibling `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`). The log is treated as a governed artifact with a co-located path-proof and Index/mirror entries; PF12 owns the schema, path, and mirror mapping.  
    
* The log **MUST** be stable and records-only:  
    
  * first line identifying the pipeline with the canonical header prefix `run:sanity-pipeline`,  
      
  * exactly one `env:` line describing the determinism env pins in a canonical, sorted form,  
      
  * one `check <name>:OK|FAIL` line per step, in a fixed order, and  
      
  * a final `summary:PASS|FAIL` line.


* The log **MUST NOT** include timestamps, wall-clock data, or env-dependent noise that would break determinism. It is LF-terminated and BOM-free.

**Coupling to the evidence skeleton.**

* A **green sanity pipeline run** asserts that:  
    
  * the determinism env pins are in place and enforced (as per §4.1.4 and `DETERMINISM_ENV_PINS_OK`), and  
      
  * the evidence skeleton checks (INDEX/`INDEX.sha256`/mirror/path-proofs, including the mirror self-record) succeed under closed rails.


* PF12 remains the single home for INDEX/mirror schemas, path-proof format, and the `artifact_key` used for the sanity log; PF04 records only the policy and token coupling.

**CI posture and token coupling.**

* A dedicated CI job **MUST** run the sanity pipeline under the canonical closed-rails env tuple and **MUST** be merge-gating for engine releases and Epic-level gates that rely on the EPIC017 evidence skeleton.  
    
* `SANITY_PIPELINE_OK` is **satisfied** only when:  
    
  * the sanity pipeline job has completed successfully under closed rails,  
      
  * `audit/gates/sanity_pipeline/sanity_pipeline.log` and its path-proof exist and validate, and  
      
  * `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` have been updated and remain coherent in the same change (as enforced by the existing evidence tokens in §2.0.6).


* PF19 — Glow QA Guide owns the broader QA semantics and any composite QA tokens built on top of `SANITY_PIPELINE_OK`; PF04 is the single home for the governance token and its coupling to env pins and the evidence skeleton.

### **4.1.9 Config artifacts & acceptance map (EPIC018+)**

**Scope.** This class covers the governed **config artifacts** and the **EPIC-018 config acceptance map** that tie PF09 config tasks to concrete artifacts, tokens, and tests. It is part of the same evidence skeleton as the EPIC-017 artifacts: governed artifacts, path-proofs, the human Evidence Index, the hash sentinel, and the machine mirror must remain coherent under closed rails.

**Config generator (closed rails; titles-only).**

* The canonical generator for governed config artifacts **MUST** be a single, closed-rails entrypoint (for example `python tools/config/generate_config_artifacts.py` as named in HDE-Mechanics Guide).  
    
* Before writing any config artifact, the generator **MUST** enforce the canonical determinism env pins (closed-rails tuple in §2.0.10/§4.1.4): the generator and its tests run under the same closed-rails env profile used for determinism and evidence jobs.  
    
* The generator **MUST** read only from the hardened registry/threshold inputs defined by Math and Mechanics (for example the registry loader and thresholds catalog) and **MUST** emit artifacts using the shared canonical serializer (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing LF). PF12 — HDE-Schemas & Artifacts owns the schemas and specific artifact\_key mappings; PF04 records the governance policy only.

### **4.1.10 Typed FE/BE bundles (EPIC018+)**

**Scope.** This class covers the **typed frontend and backend config bundles** introduced in EPIC018 D6. These bundles are **projections of governed config artifacts**, not runtime configuration switches. They are part of the same evidence skeleton as the EPIC017/EPIC018 artifacts: governed artifacts with path-proofs, indexed in the human Evidence Index and machine mirror, maintained under closed rails.

**Bundle generation (closed rails; titles-only).**

* The canonical bundle generator for typed FE/BE bundles **MUST** be a single, closed-rails entrypoint (for example `python tools/config/generate_bundles.py`, with implementation owned by **HDE-Mechanics Guide**).  
    
* Before building any bundle, the generator **MUST** enforce the canonical determinism env pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) as described in §2.0.10 / §4.1.4.  
    
* The generator **MUST** derive bundle content **only** from the governed config artifacts and registry loader defined by EPIC018 D5:  
    
  * the registry report snapshot,  
      
  * the Magic-10 config artifact, and  
      
  * the band-edges config artifact,


* with structure and schema owned by **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide** (titles-only). Bundles **must not** introduce new configuration sources or ad-hoc inputs.  
    
* Bundles **MUST** be emitted via the shared canonical serializer (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF). Two runs with identical inputs and env pins **MUST** produce byte-identical bundles (two-run identity).

**Governed bundle artifacts (records-only; titles/paths only).**

* The frontend and backend bundles are treated as governed artifacts (for example: `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`, with exact paths and `artifact_key` mappings defined in **HDE-Schemas & Artifacts**).  
    
* Each bundle **MUST** have a co-located `*.path_proof.txt` file and **MUST** appear in both `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` with reserved `artifact_key` values, maintained exclusively by the canonical bundle generator and the evidence index updater under closed rails. Manual edits to bundle bytes, path-proofs, or mirror records are a governance violation and are expected to fail the evidence and config-bundle tokens in §2.0.6 and §2.0.16.

**Sources linkage (config → bundle).**

* Each bundle **MUST** carry a “sources” block (or equivalent structure defined by **HDE-Schemas & Artifacts**) that records, for each upstream governed config artifact used to build the bundle:  
    
  * the `artifact_key` of the source,  
      
  * the `path` within the repo, and  
      
  * the `sha256` and `size_bytes` of the source artifact.


* Validation tests (named in **Glow QA Guide** and **HDE-Build Checklist**) **MUST** assert that:  
    
  * the paths, hashes, and sizes in the bundle’s sources block exactly match the current governed config artifacts and the Evidence Index/mirror, and  
      
  * frontend/backend bundle contents for Magic-10 and band-edges agree with the underlying config artifacts (no drift).

**Coupling to tokens and skeleton.**

* `CONFIG_BUNDLES_DETERMINISTIC_OK` (see §2.0.16) is **satisfied** only when:  
    
  * the FE/BE bundles are generated under closed rails by the canonical bundle generator,  
      
  * FE/BE bundle artifacts and their path-proofs are present and coherent in the Evidence Index and mirror,  
      
  * bundle bytes are canonical JSON and pass two-run identity checks, and  
      
  * the sources block in each bundle correctly links to the current governed config artifacts and registry report (no dangling or mismatched references).


* The existing evidence and indexing tokens in §2.0.6 (including `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_FINAL_LF_OK`, and `CI_CHECK_MIRROR_SCHEMA_OK`) continue to govern the skeleton as a whole. This class adds bundle-specific constraints that ensure typed FE/BE bundles are **deterministic, closed-rails projections** of governed config artifacts and are always accompanied by up-to-date skeleton evidence.

**Governed config artifacts (records-only; titles/paths only).**

* The following config artifacts are treated as governed members of the evidence skeleton (names-only; PF12 owns exact schemas/paths):  
    
  * the registry report (for example `artifacts/registry/registry_report.json`),  
      
  * the Magic-10 config artifact (for example `artifacts/thresholds/magic10_config.json`), and  
      
  * the band-edges config artifact (for example `artifacts/thresholds/band_edges.json`).


* Each governed config artifact **MUST** have a co-located `*.path_proof.txt` and **MUST** appear in both `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` with a reserved `artifact_key`, maintained exclusively by the canonical generators/writers (config generator and evidence index updater) under closed rails. Manual edits to these artifacts, their path-proofs, or their mirror records are a governance violation and are expected to fail the evidence tokens in §2.0.6 and the config tokens in §2.0.15.

**EPIC-018 config acceptance map (records-only; titles/paths only).**

* The EPIC-018 config acceptance map (for example `audit/EPIC-018_config_acceptance_map.json`) is a governed artifact that ties PF09 config tasks (e.g. HDE-CALC004/HDE-CALC004.3/HDE-CALC004.7) to:  
    
  * specific `artifact_key` values for the registry report and config artifacts,  
      
  * config tokens (including `CONFIG_REGISTRY_OK` and `CONFIG_MAGIC10_OK`), and  
      
  * the tests or harnesses that back those tokens.


* The acceptance map **MUST** be canonical JSON (UTF-8, no BOM; sorted keys; compact separators; exactly one trailing LF), and validation tests **MUST** assert that:  
    
  * every task ID in the map is a known PF09 config task,  
      
  * every `artifact_key` in the map exists in `docs/evidence/INDEX.json` and in the machine mirror, and  
      
  * every test reference in the map corresponds to a real test file (and optional node) in the repo.


* As with other governed evidence, the acceptance map and its path-proof **MUST** be added to the human Evidence Index, hash sentinel, and machine mirror in the same change that updates them.

**Coupling to tokens and skeleton.**

* `CONFIG_REGISTRY_OK` is **satisfied** only when:  
    
  * the registry report has been generated under closed rails by the canonical config generator,  
      
  * the registry report artifact, its path-proof, and its Index/mirror entries are present and coherent, and  
      
  * the EPIC-018 config acceptance map links the registry report’s `artifact_key` to this token and to the associated tests without dangling references.


* `CONFIG_MAGIC10_OK` is **satisfied** only when:  
    
  * the Magic-10 and band-edges config artifacts have been generated under closed rails and serialized canonically from the math/threshold inputs,  
      
  * these artifacts and their path-proofs are present and correctly indexed in the Evidence Index and mirror, and  
      
  * the EPIC-018 config acceptance map ties the relevant PF09 config tasks to these artifacts, this token, and the backing tests with no broken links.


* The existing evidence and indexing tokens in §2.0.6 (including `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_FINAL_LF_OK`, and `CI_CHECK_MIRROR_SCHEMA_OK`) continue to govern the skeleton as a whole; this class adds **config-specific** constraints on how governed config artifacts and the acceptance map participate in that skeleton.

---

## **4.2 Evidence index rule \[Required-Now\]**

### **4.2.1 Evidence-index governance**

Whenever a governed artifact changes, the Human Evidence Index, its hash sentinel, the Machine Evidence Mirror, and required path proofs must be updated coherently in the same change. Their canonical paths, schemas, field sets, ordering, parity, and artifact catalog live in **HDE-Schemas & Artifacts**.

Appendix D is an informative routing aid only. It is not the Human Evidence Index, a schema home, or an authoritative artifact catalog.

### **4.2.6 Tokens**

See **§2.0 Acceptance Tokens**: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, **`CI_CHECK_FINAL_LF_OK`**, **`CI_CHECK_MIRROR_SCHEMA_OK`**, **`EVIDENCE_INDEX_HASH_OK`**.

---

## **4.3 CI hygiene \[Required-Now\]**

### **4.3.1 Grep guards (fail fast)**

* **No ad-hoc dumps/emitters.** Fail any public path containing `json.dumps(` (or equivalent) or a non-presenter emitter; allow-list the single presenter/emitter symbol.  
* **No payload/secret logging.** Fail on patterns that indicate request/response bodies, header values, or keys in logs; secrets must be redacted.

### **4.3.2 Encoding and termination checks**

* **UTF-8 only**, BOM/ANSI-free.  
* **Exactly one LF** at end of all success and error bodies.  
* **Header snapshot normalization.** JSON with **lower-cased header names**, compact separators, **one LF**; **values remain verbatim**.  
  * Acceptance (titles-only): SNAPSHOT\_HEADER\_LOWERCASE\_OK  
* **Canonical re-serialization compare.** Enforce sorted keys and compact separators by comparing to canonical dumps.  
* **Arrays-as-sets.** Where arrays represent sets, dedupe and ASCII-sort before hashing/compare.

### **4.3.3 Schema and shape gates**

* **Success.** Six keys exactly; `categories[*]` are `{id, band}` only (numeric-free).  
* **Errors.** Typed, numeric-free JSON (no PII), LF-terminated.

### **4.3.4 Parity and identity jobs**

* Reader↔CLI byte equality for identical inputs/environment (single presenter).  
* AB↔BA byte equality (pair normalization) — include integration channel cases.  
* Two-run identity (repeat run produces identical bytes).  
* Idempotence re-check. Recompute `sha256(preimage_bytes)` (preimage fields per HDE Math Spec) equals published `idempotence_hash`.

**Scoped closure lanes (bounded remediation; truthful CI).**

* When a bounded remediation or cleanup PR has already restored its approved in-scope net diff, but a residual merge-gating check outside that slice still blocks closure, CI MAY add a dedicated scoped closure lane that proves only the in-scope slice.  
    
* A scoped closure lane is additive only. It MUST NOT narrow, replace, or weaken the main lane that preserves repo-wide safeguards, fail-closed coverage, and global evidence validation.  
    
* If the main lane previously executed full-module or guard coverage, the final shipped posture MUST preserve that coverage in the main lane. The scoped lane MAY prove only the bounded slice, but it MUST NOT become the sole lane carrying global truthfulness checks.  
    
* A scoped closure lane MUST keep the net effective change-set scope-clean. It MUST NOT resolve a residual blocker by introducing governed artifact churn or state changes from an adjacent surface outside the bounded slice.  
    
* Final validation posture for such a remediation requires both:  
    
  * the scoped closure lane proves the bounded slice, and  
      
  * the preserved main lane remains green on the repo-wide safeguards that were in force before the scoped split.

### **4.3.5 A7 transport checks (Catalog success endpoint)**

* **200\.** Strong, quoted ETag present; `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304\.** Only after a prior 200-with-body; **no body**; validators mirror 200; **omit both `Content-Type` and `Content-Length`**.  
* **HEAD parity.** Validators mirror 200; no body; `Content-Length` matches identity 200 body; `Content-Type` equals GET.  
* **Writers and errors.** `Cache-Control: no-store`; **no ETag**; errors include `Content-Type: application/json; charset=utf-8`.  
* **Encoding invariance.** For the same body, identity (ETag) is stable across Accept-Encoding.  
* **POST non-conditional.** Ignore If-\* conditionals for POST.  
* **Env-gate proof.** Capture a headers-only proof that non-prod entries are unreachable in prod on the Endpoint Catalog route.

### **4.3.6 Rails posture jobs**

* **Closed rails (default).** Prove no network I/O, typed refusal, keys-only logs with secrets redacted.  
* **Open rails (integration profile).** Prove pinned timeouts/retries/backoff and deterministic vendor error mapping; logs contain no payloads or secrets; public bytes unchanged (parity/idempotence intact).

### **4.3.7 Topology integrity jobs**

* ID normalization demo. Verify high→low normalized to min→max **NN-NN** in orientation demo.  
* Integration degree check. Gates **10/20/34/57** ⇒ degree 3; all other gates ⇒ degree 1\.  
* Center-pair multiplicity. Unordered center-pair counts sum to **36**.

### **4.3.8 Environment pins \[Required−Now\]**

Record **LC\_ALL=C, LANG=C, TZ=UTC** for all determinism, transport, and evidence jobs and **fail** CI if any pin is missing.

For EPIC017 and later, CLI, evidence, ordering, and registry jobs MUST also run under closed rails by default:

`SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC`.

Evidence for this profile (for example, `env_matrix.snapshot.json` and dev connectivity snapshots) is indexed alongside other governed artifacts and mirrored in `artifacts/evidence_index.jsonl` in the same PR as any changes to these jobs.

This ties the EPIC017 env rule into the existing CI “pin and enforce env variables” gate.

---

# **5\) Release & Freeze-Pack Discipline \[Required-Now\]**

## **5.1 Release identity (manifest → release\_id) \[Required-Now\]**

**Definition (normative).** `release_id` is the lowercase 64-hex SHA-256 of the canonical freeze-pack manifest. It identifies exactly which frozen math inputs produced the public bytes for a release.

**Canonical manifest (construction)**

* **Top-level fields (required).** A single JSON object with:  
  `root: "catalog/"`, `version` (pack semver), `built_at_utc` (UTC ISO-8601 with `Z`), and  
  `files: [{path, sha256, size}]`. Do not self-list the manifest.  
* **Enumerate frozen math inputs (titles and paths only).** List every governed math artifact used by the engine: closed category set and order, band maxima (inclusive-high), topology catalogs (centers, gates, channels), **Motor→Throat sets** (and other denominators where applicable), preset catalog (if used), constants pack (limits, thresholds, resonance inputs as applicable), and any other normative math tables referenced by this governance. Transport and ops bytes are not part of the pack.  
* **Per-entry identity.** For each entry compute `sha256(canonical_bytes(entry))` and record:  
  `path` (repo-relative POSIX path under `catalog/`), `sha256` (lowercase 64-hex), `size` (integer byte length of the same canonical bytes).  
* **Canonical storage and hashing.** The manifest itself is stored canonically (see **Evidence & Artifacts**): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. Compute  
  `release_id = sha256(canonical_bytes("catalog/manifest.json"))`. All jobs run with `LC_ALL=C` and `TZ=UTC`.

**Single tracked release-identity source and acyclic evidence semantics.**

* **Single Source of Truth.** `catalog/manifest.json` is the sole tracked release-identity input. No evidence file, generated constant, environment variable, registry report, configuration bundle, or external attestation may act as a second source of release identity.  
* **Runtime derivation.** Runtime reads the packaged canonical manifest and derives `release_id = sha256(canonical_bytes(catalog/manifest.json))` directly from those bytes. Runtime MUST NOT read release identity from evidence paths, generated source constants, mutable attestations, or independent environment values.  
* **Acyclic dependency direction.** The required direction is `tracked source → canonical manifest → release_id → external attestation`. No generated attestation or release derivative may point back into tracked source or require recursive tracked-source regeneration.  
* **Terminal tracked cut.** An intentional manifest cut is the terminal tracked release-identity change after source stabilization. It does not require a generated release-ID constant, source-tree identity-closure writes, or regenerated checked-in release derivatives.  
* **Historical checked-in evidence.** Any retained checked-in release-evidence copy or derivative is a frozen capture-time record. It is not a current runtime input, current release-identity source, or current external attestation, and it MUST NOT be refreshed merely because the canonical manifest or release ID changes. Its existing historical integrity, canonical-byte, secret-safety, and provenance requirements remain binding.

**Change ⇒ new `release_id`**

* Any byte-level change to a frozen input (content, bounds, divisors or weights, thresholds, catalogs, seeds if catalogized), its schema or membership or order, or the manifest content or shape or order **MUST** produce a new `release_id`.  
* **Explicit rule.** Any change to constants, **Motor→Throat sets**, thresholds, or catalog membership or order **requires a manifest update in Evidence & Artifacts and yields a new `release_id`**.

**Determinism and scope**

* **Two-run identity.** Building the pack twice from identical sources yields the same `release_id`.  
* **Order-neutral.** `release_id` is independent of AB↔BA pairing and of presentation order in public bytes, as long as the pack is identical.  
* **Transport-independent.** HTTP headers, caching, and Reader or CLI mechanics do not enter the pack.

**Validation (binary)**

* **Pattern.** `release_id` matches `^[0-9a-f]{64}$`.  
* **Recompute.** Recompute `sha256(canonical_bytes(manifest))` and match the published `release_id`.  
* **Canonical file check.** The on-disk manifest equals the canonical serialization (UTF-8 no BOM, sorted keys, compact, one LF).  
* **Closure.** Every math input referenced at runtime resolves to an entry in `files[]`. No missing or ad hoc sources.  
* **No self-listing.** The manifest does not list itself.

**Tokens:** see §2.0: `RELEASE_ID_FROM_MANIFEST_OK`, `PACK_MANIFEST_NO_SELF_LISTING_OK`, `MANIFEST_SHA256_HEX64_OK`, `PACK_ROOT_PINNED_OK`, `JSON_CANONICAL_CHECK_OK`.

---

## **5.2 Immutable packaged-release promotion and rollback \[Required-Now\]**

**Purpose (normative).** Provide a deterministic, auditable procedure to promote one immutable packaged release containing the application and the exact manifest-bound frozen inputs it uses, and to revert safely if acceptance signals fail. The deployment platform selects an exact immutable artifact reference or digest; runtime derives `release_id` from the artifact's embedded canonical manifest. No separate active-pack selector or mutable pack pointer is authoritative.

### **5.2.1 Identity and ownership boundary**

| Concept | Governing rule | Authoritative home |
| :---- | :---- | :---- |
| Canonical manifest | The sole tracked release-identity input is `catalog/manifest.json`. | **HDE-Schemas & Artifacts** for manifest shape; §5.1 for release policy. |
| `release_id` | The lowercase 64-hex SHA-256 derived at runtime from the packaged canonical manifest. It is not a deployment selector, environment override, or second artifact locator. | §5.1. |
| Packaged release | One immutable deployable unit containing the application and the exact manifest-bound frozen inputs it uses. | Build and release implementation governed by this policy. |
| Deployment record | The platform fact that identifies which immutable packaged release is active in an environment. It records the artifact identity and derived `release_id` separately and does not create release identity. | Provider-specific name and location in **Glow Infrastructure**. |
| External attestation | A release-bound proof derived after source and package stabilization. It is not a runtime input or selector. | The manifest-derived external-attestation model governed by §5.1. |

The deployment artifact and `release_id` remain separate because a code-only change outside the manifest's frozen-input membership can produce a new application artifact without changing the mathematical `release_id`. Operators select and roll back by exact artifact identity, then verify the manifest-derived `release_id` inside that artifact. Selecting by `release_id` alone could select the wrong application build even when the math pack is unchanged.

If an operator-supplied expected release ID is retained for deployment verification, it is an assertion only. Runtime MUST derive the actual value from the packaged manifest and fail closed on mismatch. An environment value MUST NOT supply, replace, or override release identity. HDE Governance owns promotion, rollback, release-acceptance, and failure policy. **Glow Infrastructure** records provider-specific artifact and deployment names, locations, and bindings without becoming a second policy or identity source.

**Current implementation posture (static).** The pinned repository contains manifest-derived release-identity logic, but static inspection does not establish immutable build-once promotion of the same artifact or exact-artifact rollback. This deployment mechanism remains Required-Now; static inspection does not establish deployment or runtime state.

### **5.2.2 Promotion — required steps**

1. **Stabilize source and cut identity.**  
   • Stabilize tracked source, intentionally build the **canonical manifest** once, and compute and record its 64-hex `release_id`.  
   • Attach the manifest and `release_id` to the Change Log / Doc-Delta using titles and repo-relative paths only.  
     
2. **Build and bind one immutable artifact.**  
   • Build one immutable deployment artifact from the stabilized source and embedded manifest.  
   • Bind the source commit, artifact reference or digest, packaged-manifest digest, and derived `release_id` in release metadata or external attestation. No identifier may silently substitute for another.  
     
3. **Verify that exact artifact in staging.**  
   • Prove **A3 determinism**: preimage re-check per **PF-01**, AB↔BA identity, and two-run identity.  
   • Prove **A4 Reader↔CLI parity** on staging fixtures through the single presenter.  
   • Prove **A7 transport** on a **PF-05 Endpoint Catalog (success JSON)** route: `ETag` on 200, HEAD parity including `Content-Type`, and 304 omitting `Content-Type`.  
   • Record the governed artifacts in the Human Evidence Index and Machine Evidence Mirror, including required path proofs, under **HDE-Schemas & Artifacts** governance. A staging rebuild is not the production candidate.  
     
4. **Deploy a bounded canary when used.**  
   • Canary deployment is optional and recommended. Deploy complete instances of the candidate artifact to a bounded, time-boxed traffic slice.  
   • Each request MUST execute entirely against one complete release. A request, worker, or process MUST NOT combine old code with new math inputs or new code with an old manifest.  
   • Monitor keys-only metrics for regressions in parity, preimage pass rate, A7 invariants, and typed error mix.  
     
5. **Promote the validated artifact to production.**  
   • Promote the same artifact bytes or the same content-addressed artifact digest validated in staging.  
   • Promotion MUST NOT rebuild from a branch, tag, unlocked dependency set, or mutable workspace and MUST NOT modify code, schemas, runtime knobs, or manifest bytes during promotion.  
     
6. **Capture post-promotion evidence.**  
   • On live traffic or representative fixtures, re-prove A3, A4, and A7 and capture header snapshots by title only.  
   • Record the active deployment artifact identity and its manifest-derived `release_id` as separate fields. The deployment record observes the release; it does not create release identity.  
   • Update the Human Evidence Index, hash sentinel, Machine Evidence Mirror, and required path proofs coherently in the same change.

### **5.2.3 Rollback — required steps**

1. **Trigger conditions; any one is sufficient.**  
   • Reader↔CLI parity failure, AB↔BA or two-run failure, or preimage/idempotence mismatch.  
   • A7 violation, including a missing or incorrect `ETag`, a 304 without a prior 200, HEAD parity mismatch, or a 304 carrying `Content-Type`.  
   • Elevated typed failures attributable to the candidate release.  
     
2. **Select the exact last-known-good artifact.**  
   • Use the immutable artifact reference recorded during its successful promotion.  
   • If the exact prior artifact is unavailable, there is no proven rollback. Stop promotion and treat rollback readiness as failed. A source checkout, branch name, Git tag, or fresh rebuild is not an equivalent substitute.  
     
3. **Redeploy without mutation.**  
   • Redeploy the exact last-known-good artifact without rebuilding it, editing code, changing the manifest, changing runtime knobs to simulate old behavior, swapping a data pack inside a running release, or hot-patching the emitter.  
     
4. **Verify restored identity and behavior.**  
   • Verify that runtime derives the last-known-good `release_id` from the redeployed package and that the reported identity matches the deployment record.  
   • Re-run the applicable A3, A4, and A7 checks. Confirm that public bodies and validators match the last-known-good release and that identity bytes and `ETag` values reflect the restored artifact.  
     
5. **Record and investigate.**  
   • Record the rollback in the Change Log with a one-line reason, time, prior and restored artifact identities, and the corresponding `release_id` values.  
   • Preserve the failed candidate for investigation; do not mutate it in place or relabel it as the prior release. Open an investigation item linked to the failing evidence and do not re-promote until fixed.

### **5.2.4 Guardrails (normative)**

* **Immutability.** A published packaged release and its embedded manifest are immutable. Any math or frozen-input change produces a new `release_id` (§5.1); any application-artifact change produces a new artifact identity. No in-place edits.  
* **Single release-identity source.** Runtime derives `release_id` from the packaged canonical manifest. No separate active-pack selector, mutable pack pointer, release-identity environment value, deployment record, or external attestation may act as a second identity source.  
* **Exact-artifact selection.** Promotion and rollback select an immutable artifact reference or digest. A branch, tag, mutable workspace, or `release_id` alone is insufficient.  
* **No mixed releases.** Never serve a request from mixed application and manifest inputs. Canary scopes MUST remain bounded and time-boxed, and each instance MUST run one complete release.  
* **No in-process substitution.** Do not swap packs inside a running release, rebuild during promotion or rollback, or hot-patch a candidate or last-known-good artifact.  
* **Keys-only ops.** Release, canary, and rollback logs contain no payloads or secrets. Labels remain bounded, including route, outcome, and `rails_state`.  
* **Evidence first.** A promotion or rollback is incomplete until the Human Evidence Index, hash sentinel, Machine Evidence Mirror, and required path proofs are updated coherently in the same change and CI gates pass for parity, idempotence, A7, mirror parity, and path-proof validation.  
* **Artifact retention.** Promotion MUST NOT begin unless the exact candidate and last-known-good artifacts are retained and addressable for the required promotion and rollback actions.

### **5.2.5 Binary acceptance (pass or fail)**

A promotion is **Accepted** only if the exact validated artifact is promoted without rebuild, its deployment artifact identity and manifest-derived `release_id` are recorded separately, A3, A4, and A7 pass on staging and production, and the governed evidence surfaces and CI checks pass.

A rollback is **Accepted** only if the exact recorded last-known-good artifact is redeployed without rebuild, its manifest-derived `release_id` and deployment identity are verified, the applicable A3, A4, and A7 checks pass, and the governed evidence surfaces and CI checks pass.

Otherwise the change is **Rejected**. If the exact last-known-good artifact is available, redeploy it. If it is unavailable, stop and record rollback readiness as failed; do not claim that rollback occurred.

# **6\. Operations & SLOs \[Required-Now\]**

## **6.1 Bench harness (non-PII) \[Required-Now\]**

**Purpose (normative).** Provide a repeatable, deterministic harness for measuring engine performance and transport behavior without exposing PII or payload bytes. Bench results inform SLOs, release decisions, and regressions; they do not change the public contract.

**Implementation posture.** The benchmark contract is Required-Now. The pinned repository does not establish the benchmark harness, its named CI surfaces, benchmark results, or current SLO attainment.

### **6.1.1 Deterministic runs**

* **Inputs and seeds.** Use a fixed set of fixture pairs (titles and paths only), stable environment, and pinned config (serializer and emitter, rails posture). No wall-clock–dependent logic; no randomness.  
* **Warm-up and windowing.** Perform a fixed warm-up that is discarded, then a fixed measurement window; run counts are constant across cuts.  
* **Isolation.** Disable vendor calls (rails **closed**) for math and transport benches. The required deterministic comparison excludes live-vendor network timing. A separate scripted vendor-conformance profile may use a fixed-response test double with a fixed attempt sequence and fixed no-jitter backoff values; live-provider performance is observational operations data only.  
* **Fixture corpus and order.** Use the governed Human Design and compatibility corpus, not synthetic placeholder charts represented as complete BodyGraphs. Fixture identities and the fixture-manifest digest are fixed. Schedule fixtures in canonical ASCII order and repeat them round-robin; do not randomize order.  
* **Governed surfaces.** Measure Compat Engine Core computation, Presenter emission from an already computed result, Reader Adapter end-to-end execution in the controlled dev harness, and Narrative Selection Router key lookup and selection separately. For every eligible pair, the Core surface includes the complete internal ten-category Magic-10 result.  
* **Correctness before timing.** Before any latency comparison, require identical fixture identity and manifest digest, all ten canonical Magic-10 category IDs exactly once in pinned order with expected scores and bands, and exact passage of the applicable AB↔BA, two-run, Reader↔CLI, canonical-serialization, idempotence, and A7 predicates. `harmony` is one category and never substitutes for the other nine. A benchmark mode must not skip mathematics, omit a category, substitute cached partial results, alter weights, suppress feature extraction, or otherwise trade correctness for speed. Any correctness failure makes the profile `FAIL` before latency is evaluated.

### **6.1.2 Report set (bounded, non-PII)**

* **Latency histograms (bounded).**  
  * `engine.latency_ms` and `presenter.latency_ms`: bucketed histograms with the fixed edges below, plus p50, p95, and p99 derived in the harness and not logged per request.  
  * `reader.latency_ms` (dev harness only) with the same buckets.  
  * Narrative Selection Router lookup and selection latency, reported as a separate governed surface without narrative text.  
* **Outcome counters (bounded labels).**  
  * `reader.req_total`, `reader.req_ok`, `reader.req_error_{class}` where class ∈ {`usage`,`typed`,`transport`}.  
  * `cli.stdout_ok`, `cli.stderr_typed`.  
  * `transport.etag_ok`, `transport.cond_304`, `transport.head_parity_ok`, `transport.no_store_ok`.  
* **Label set (bounded).** `route`, `outcome ∈ {ok,usage,typed,transport}`, `rails_state ∈ {open,closed}`, `profile ∈ {default,small,long}`, and `attempt_idx` only for a separately governed scripted vendor-conformance profile. `correlation_id` is a log field and MUST NOT be a metric label.  
* **No payloads and no secrets.** Logs must not include request/response bodies, header values, or keys. Secrets are always redacted.

**Timer, histogram, and percentile contract.** Measure duration with a monotonic high-resolution timer and retain raw samples as integer nanoseconds. A wall-clock timestamp MUST NOT calculate duration. The cumulative histogram uses inclusive upper edges, in milliseconds:

`0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 300, 500, 750, 1000, 2000, 5000`

The first bucket is `0 <= value <= 0.25 ms`; each later finite bucket is `previous_edge < value <= current_edge`; the final overflow bucket is `value > 5000 ms`.

Compute p50, p95, and p99 from sorted raw integer-nanosecond samples by nearest rank:

`Q(p) = sorted_samples[ceil(p * N) - 1]`

Do not interpolate or reconstruct percentiles from histogram buckets. Convert the selected value to milliseconds with fixed three-decimal display precision; compare the unrounded nanosecond value.

**Required comparability fields.** Each report records the source commit, manifest-derived `release_id`, fixture-manifest digest, profile definition, Python implementation and version, dependency-lock digest, operating-system family and version, architecture, CPU model, logical CPU allocation, memory allocation, worker and thread counts, `LC_ALL`, `LANG`, `TZ`, rails and network posture, database-fixture posture, cache temperature, surface, process-replica count, warm-up count, measurement count, concurrency, timeout, timer unit, and histogram edges. In repeatability mode, the source commit and `release_id` also MUST match. In regression mode, those two fields identify the candidate and last-known-good releases and therefore differ as governed; every environment, fixture, profile, run-shape, timer, and histogram comparability field still MUST match.

### **6.1.3 Procedure (normative)**

1. **Prepare profiles.**  
     
   * **Math/transport profile:** rails **closed**; run fixture pairs through CLI and dev Reader; capture latency and parity/idempotence checks.  
   * **Vendor profile (optional):** use a scripted fixed-response test double with pinned timeouts, attempt sequence, and no-jitter backoff; capture typed mapping behavior with no payloads. Live-provider timing is excluded from deterministic comparison.

   

2. **Execute runs.** Use the exact run shapes below for each governed surface. Warm replicas execute sequentially so they do not contend with one another. Within a replica, client concurrency is fixed. Core, Presenter, Reader dev-harness, and Narrative Selection Router measurements use zero retries. A timeout is a failed sample that makes the profile `FAIL`; it is not retried or replaced.  
   

| Profile | Temperature | Independent process replicas or starts | Discarded warm-up invocations | Measured invocations | Client concurrency | Per-invocation timeout | Release use |
| :---- | :---- | ----: | ----: | ----: | ----: | ----: | :---- |
| `small` | warm | 2 replicas | 100 total, 50 per replica | 1,000 total, 500 per replica | 1 | 5,000 ms | Pull-request smoke only |
| `default` | warm | 5 replicas | 500 total, 100 per replica | 5,000 total, 1,000 per replica | 4 | 5,000 ms | Required release comparator |
| `long` | warm | 10 replicas | 1,000 total, 100 per replica | 20,000 total, 2,000 per replica | 8 | 5,000 ms | Capacity and pre-release evidence |
| `small` | cold | 20 fresh process starts | 0 | 20, one first invocation per process | 1 | 15,000 ms | Smoke observation |
| `default` | cold | 50 fresh process starts | 0 | 50, one first invocation per process | 1 | 15,000 ms | Required release cold-start comparator |
| `long` | cold | 100 fresh process starts | 0 | 100, one first invocation per process | 1 | 15,000 ms | Capacity and pre-release evidence |

   

3. **Validate comparability.** The two reports in a release-gating comparison MUST match every field required for the applicable repeatability or regression mode above and use an isolated or dedicated runner with no intentionally concurrent build, test, or benchmark workload. A missing or impermissibly mismatched field is `FAIL`, not a waivable review note. Timestamps and run identifiers may appear as provenance but are excluded from functional equality and comparator calculations.  
     
4. **Capture exact sample posture.** Require the exact sample count, zero timeouts, and zero missing or replacement samples. Capture metrics and byte-level assertions for AB↔BA, two-run identity, Reader↔CLI parity, and the other correctness predicates above.  
     
5. **Summarize.** Produce a bench report artifact (titles and paths only) with histograms, percentiles, counters, every decisive comparator input, calculated delta, limit, per-check result, and overall result. No raw payloads or secrets.

### **6.1.4 Acceptance (binary)**

* **Deterministic comparator.** Given the same two valid reports, the comparator MUST always return the same binary `PASS` or `FAIL`. Functional outputs, counters that are required to be deterministic, and all correctness predicates are exact. Latency uses the practical-equivalence rules below; the comparator MUST NOT emit probabilistic language such as “statistically identical,” “not statistically significant,” or “likely equivalent.”  
* **Parity and identity.** All A3 and A4 byte-level gates pass during the bench (AB↔BA, two-run, Reader↔CLI).  
* **A7 spot checks.** In the dev harness, validators for **200 with ETag**, **304**, **HEAD parity**, and **no-store** on writers/errors pass.  
* **Rails posture.** Closed-rails benches show no network I/O. Open-rails benches show pinned behavior and redacted logs only.

For reports `A` and `B`, compute cumulative histogram distance over every fixed edge:

`D = max(abs(cumulative_A / N_A - cumulative_B / N_B))`

Warm-profile practical equivalence requires all of these bounds:

| Statistic | Required bound |
| :---- | :---- |
| p50 | `abs(p50_A - p50_B) <= max(5% * min(p50_A, p50_B), 0.25 ms)` |
| p95 | `abs(p95_A - p95_B) <= max(10% * min(p95_A, p95_B), 1 ms)` |
| p99 | `abs(p99_A - p99_B) <= max(15% * min(p99_A, p99_B), 2 ms)` |
| Histogram distance | `D <= 0.05` |

Cold-profile practical equivalence requires all of these bounds:

| Statistic | Required bound |
| :---- | :---- |
| p50 | `abs(p50_A - p50_B) <= max(10% * min(p50_A, p50_B), 5 ms)` |
| p95 | `abs(p95_A - p95_B) <= max(15% * min(p95_A, p95_B), 10 ms)` |
| p99 | `abs(p99_A - p99_B) <= max(20% * min(p99_A, p99_B), 25 ms)` |
| Histogram distance | `D <= 0.10` |

The overall comparison is `PASS` only when every required surface, temperature, profile, correctness predicate, percentile bound, histogram-distance bound, and §6.2 absolute budget passes. There is no averaging of failures and no majority vote.

Repeatability compares two reports for the same candidate release with the symmetric bounds above. Regression compares the candidate against the exact last-known-good artifact in the same environment and profile; improvements are allowed, and only candidate degradation is tested with the corresponding percentage and absolute floor. Release performance admission requires two-report candidate repeatability, one-direction regression, every applicable §6.2 absolute target, and every Human Design, full Magic-10, determinism, parity, identity, transport, and rails correctness predicate.

### **6.1.5 Evidence and SLO coupling**

* **Artifacts.** Commit the bench report and metric snapshots as governed evidence. Update the Human Evidence Index, hash sentinel, Machine Evidence Mirror, and required path proofs coherently in the same change; their canonical paths, schemas, and ordering live in **HDE-Schemas & Artifacts**.

* ## **SLO link.** Compare p95 and p99 to the §6.2 targets. A candidate-correlated violation stops the canary or promotion and redeploys the exact recorded last-known-good immutable artifact when available; other breaches follow the mitigation and investigation posture in §6.2 and the deployment-based release policy in §5.2.

## 6.2 SLO targets and failure posture \[Required‑Now\]

### Scope (policy‑level).

Define service‑level objectives for Reader success routes and ops surfaces. PF04 owns SLI definitions, numerator and denominator rules, numeric objectives, evaluation windows, minimum samples, release budgets, error-budget and burn-rate policy, failure actions, and the minimum dashboard contract. Operator configuration implements these values and MUST NOT override them. All captures and compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Evidence and mirror hygiene live in **HDE-Schemas & Artifacts**; acceptance tokens live in §2.0.

Provider-specific monitoring project names, dashboard and alert-rule names or identifiers, locations, service and environment bindings, and genuinely required configuration-key names live in **Glow Infrastructure**. That infrastructure inventory MUST point to this policy without duplicating or redefining the targets. A configuration mismatch is visible drift, not a local SLO override.

The targets below are requirements. They do not claim that the pinned repository, a dashboard, or a deployment currently implements or attains them. Controlled measurements are labeled controlled and do not establish production SLO attainment.

### Hard correctness invariants with zero error budget

| Invariant | Required result |
| :---- | :---- |
| Eligible internal Magic-10 computation | All ten canonical categories are present exactly once in pinned order, with canonical scores and bands. |
| Human Design provenance | Inputs are complete normalized BodyGraphs obtained through the sanctioned boundary; synthetic or incomplete placeholder charts cannot prove product correctness. |
| Canonical math | Applicable Human Design extraction, Magic-10 aggregation, banding, and frozen-input rules pass. |
| Determinism and parity | AB↔BA, two-run, Reader↔CLI, canonical-byte, and idempotence requirements pass. |
| Release identity | Runtime identity derives from the packaged canonical manifest and matches the deployed artifact's recorded release metadata. |

These invariants are not degradable SLOs. Any detected violation stops a canary or release and requires redeployment of the exact last-known-good immutable artifact when it is available. A latency or availability budget MUST NOT authorize a faster wrong result.

### Initial service SLO target matrix

These are initial launch targets.

| SLI population | Objective | Evaluation window | Minimum data | Failure counted as |
| :---- | ----: | :---- | ----: | :---- |
| Valid eligible Reader requests reaching the service | Availability at least `99.5%` | Rolling 28 days | 1,000 eligible requests | Timeout, 5xx, malformed success, wrong or incomplete compatibility result, or missing required response bytes. Client-caused validation and authorization failures are excluded. |
| Reader full success response | p95 `<= 300 ms`; p99 `<= 750 ms` | Rolling 28 days and per-release canary | 1,000 successful responses | Successful response over the applicable latency target. Errors are tracked separately and never used to make latency appear faster. |
| Reader conditional `304` and `HEAD` success | p95 `<= 100 ms`; p99 `<= 250 ms` | Rolling 28 days and per-release canary | 1,000 successful conditional and HEAD responses combined, with a separate method breakdown visible | Successful conditional or HEAD response over target. |
| Internal Compat success surface | p95 `<= 200 ms`; p99 `<= 500 ms` | Rolling 28 days where enabled; otherwise controlled environment | 1,000 successful responses | Successful response over target or any incomplete ten-category internal result. |
| `/internal/version` success | p95 `<= 50 ms`; p99 `<= 100 ms` | Rolling 28 days | 1,000 successful responses | Successful response over target or identity mismatch. |
| Closed-rails refusal at the canonical refusal probe | p95 `<= 50 ms`; p99 `<= 100 ms` | Rolling 28 days where exercised; otherwise controlled evidence run | 1,000 refusals for SLO status | Refusal over target, external-I/O attempt, malformed typed refusal, or nonconforming seven-key log. |

When a production population has fewer than its minimum observations, report `insufficient data`, neither `PASS` nor `FAIL`. Controlled default-profile benchmark evidence governs release decisions until representative production volume exists, but it does not establish production SLO attainment.

Availability success requires both protocol success and semantic correctness. An HTTP `200` response with an incomplete Magic-10 calculation, wrong Human Design result, malformed canonical bytes, or wrong release identity is an error.

### Initial release benchmark budgets

These budgets apply to the §6.1 `default` warm profile in the matching controlled environment. They are release-admission limits, not public promises.

| Bench surface | p95 budget | p99 budget | Additional hard condition |
| :---- | ----: | ----: | :---- |
| Compat Engine Core, complete ten-category matrix | `<= 75 ms` | `<= 150 ms` | Every eligible result contains all ten categories and passes governed math goldens. |
| Presenter emission from a completed result | `<= 15 ms` | `<= 30 ms` | Canonical bytes and Reader↔CLI parity pass exactly. |
| Reader dev-harness end to end | `<= 300 ms` | `<= 750 ms` | A3, A4, applicable A7 assertions, and closed-rails no-I/O pass. |
| Narrative Selection Router lookup and selection | `<= 25 ms` | `<= 75 ms` | Observation is keys-only; narrative content, PII, and payload logging are absent. |

The candidate MUST satisfy these absolute budgets, the §6.1 repeatability comparator, the one-direction regression comparison against the exact last-known-good artifact, and every applicable correctness predicate. Passing one condition does not waive another.

### Error budget and alert policy

The `99.5%` Reader availability objective creates a `0.5%` request error budget over the rolling 28-day window.

* Burn rate at least `14.4x` over both a 1-hour window and its 5-minute confirmation window triggers an urgent page or automated canary stop.  
* Burn rate at least `6x` over both a 6-hour window and its 30-minute confirmation window triggers an urgent page.  
* Burn rate at least `1x` over 3 days creates an investigation ticket.  
* Any hard correctness violation immediately stops the canary or release and redeploys the exact last-known-good artifact when available, regardless of traffic volume or burn rate.

During a canary, a candidate-correlated breach stops the canary and restores the exact last-known-good artifact. In steady state, operators mitigate first and roll back when the active release is a plausible cause or exact-artifact rollback is the safest available recovery. An unrelated database, platform, or infrastructure incident MUST NOT trigger a blind application rollback.

### Required dashboard binding

Every environment in which HDE SLOs are evaluated has one canonical dashboard binding that displays, at minimum:

1. the active deployment artifact reference and manifest-derived `release_id` as separate values;  
2. Reader eligible-request volume, availability, error-budget remaining, and burn rate;  
3. successful and failed request latency separately, with p50, p95, p99, and the §6.1 fixed histogram buckets;  
4. Reader full-success, conditional and HEAD, Compat, `/internal/version`, and refusal populations separately;  
5. Engine Core, Presenter, Reader, and Narrative Selection Router benchmark budgets and last-known-good comparisons;  
6. error classes using bounded enums;  
7. saturation signals available from the selected infrastructure, including worker, CPU, memory, database-pool, or queue pressure where available, without fabricating an unavailable signal;  
8. the 5-minute, 30-minute, 1-hour, 6-hour, 3-day, and rolling 28-day views used by the burn policy; and  
9. annotations for promotions, canary changes, rollbacks, and target-version changes.

Metric attributes are bounded and low-cardinality. Permitted dimensions may include environment, canonical route class, outcome class, rails state, profile, and the small set of concurrently relevant release IDs. Raw URLs, query strings, user IDs, birth data, chart values, locations, relationship identifiers, payload content, and `correlation_id` MUST NOT be metric labels.

Target values appear as reference lines sourced from or validated against this Governance contract. Provider configuration that differs from the canonical targets produces an explicit drift result and MUST NOT silently redefine the SLO.

After the first 28 days with representative traffic and the minimum eligible sample count, the Product Owner and Lead Developer should review whether the initial values reflect actual user expectations, business stage, hosting cost, and the observed distribution. They may retain, tighten, or relax a reliability value only through a governed PF04 change. Telemetry does not rewrite a target automatically. The review MUST NOT relax the zero-budget Human Design, full Magic-10, determinism, parity, or release-identity invariants.

### Bench harness (evidence, titles‑only).

Bench outputs are evidence artifacts without payload bodies or PII; index them in the human Evidence Index and the machine mirror in the same PR (PF12 single home).

### Failure posture.

If a governed SLO is breached for a success route or ops surface, apply the mitigation, canary-stop, investigation, or exact-artifact redeployment policy above, capture an evidence snapshot of the failure envelope, and update the Human Evidence Index, hash sentinel, Machine Evidence Mirror, and required path proofs coherently in the same change. Mirror schemas and byte rules remain in **HDE-Schemas & Artifacts**.

### Acceptance tokens (names‑only; rostered in §2.0).

Register SLO/bench tokens as they are introduced; they are merge‑gating and must obey PF12 index/mirror discipline.

### Routing (titles‑only).

Evidence and index shapes and the merge-gating sentinel: **HDE-Schemas & Artifacts**. Process and PR flow: **Epic-Process-Guide**. Provider-specific dashboard and alert bindings: **Glow Infrastructure**. Transport bytes and success matrices: §10 and Appendix A of this document.

## 6.3 Database runtime posture (prod & dev) \[Required-Now\]

**Purpose (normative).** Pin connection-source policy and acceptance tokens for production and development, without duplicating schema/bytes. Evidence lives in **PF12**; infra names live in **Glow Infrastructure**.

### **6.3.1 Production (policy)**

* **Single source (presence-only; no probe).** Connection selection is **`DATABASE_URL → typed error`**. The **bridge is not used** in production.  
* **Search path.** Runtime `search_path` is exactly **`hde, public`** (in that order).  
* **Dev-only artifacts absent.** The dev connectivity snapshot (**`artifacts/runtime/env_connectivity.snapshot.json`**) **must not** be present in production evidence.

**Acceptance (titles-only).** `PROD_CONN_SINGLE_SOURCE_OK`, `DB_CONN_ENV_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`.  
**Evidence (titles-only; PF12 single home).**

* `artifacts/db/check_schema.txt` (search\_path)  
* `artifacts/db/grants.txt` (least-privilege grants)  
* `artifacts/db/ddl_fingerprint.json` (DDL fingerprint)  
* `artifacts/db/conn_env_selection.log` (selection proof; keys-only, no secrets)  
  See **Appendix D: D.7**.

### **6.3.2 Development and authorized OPS — direct-only with evidence**

**Direct-only rule.**  
In development and authorized OPS, HDE database selection is `DATABASE_URL → direct psycopg → typed failure`. `DATABASE_URL` is the only endpoint key and direct psycopg is the only selectable provider.

`DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are retired and MUST be absent. Their presence is configuration drift and MUST fail closed before provider construction or external I/O. A missing, invalid, unavailable, or unauthorized direct endpoint MUST fail closed without bridge fallback, alternate HTTP database transport, vendor routing, inferred endpoints, retry adapters, or silent compatibility behavior.

**Authorization and rails.**  
Development activity that accesses a live or shared Glow database remains OPS work when it crosses the repository boundary or uses privileged database credentials. The Product Owner may execute the task personally or explicitly delegate it to an automated session agent when the exact target, authorization, rails, commands, stop checks, and evidence contract are concrete. This creates no standing database access, SQL-write authority, migration authority, deployment authority, or waiver of task-specific approval.

**Diagnostics and failure handling.**  
Diagnostics are keys-only and secret-free. They MUST NOT retain passwords, DSNs, tokens, endpoint values, request or response bodies, raw SQL, or stack traces. Direct-provider failures MUST surface through the governed typed, numeric-free error posture rather than raw exceptions.

**Search path.**  
Runtime `search_path` remains exactly `hde, public`.

**EPIC-011 stance and future PK Epic.**  
Under EPIC-011, DB posture acceptance tokens, including `DB_SCHEMA_FINGERPRINT_OK`, `DB_BOUNDARY_VIEW_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_CONN_ENV_OK`, and `DB_ROLE_OK`, assert that the **current** posture is fully captured, reviewed, and indexed. They do **not** claim that the schema is ideal. Known structural debt, such as tables without primary keys, is treated as **documented debt**, not an EPIC-011 blocker. A future PK-focused Epic, owned in HDE Epics Map, will tighten posture requirements and evolve these tokens’ target state; PF04 records that future work but does not pre-empt it.

**Acceptance (titles-only).**

* `DB_CONN_ENV_OK`  
* `DB_RUNTIME_SEARCH_PATH_OK`  
* `DB_ROLE_OK`  
* `DB_SCHEMA_FINGERPRINT_OK`

**Evidence (titles-only; PF12 single home).**

* Current direct-selection evidence records direct-only provider selection, retired-key refusal before provider attempts, fail-closed missing and unavailable direct endpoints, zero alternate-transport attempts, and secret-value absence.  
* Retained bridge-era connectivity and provider evidence is historical only. It MUST NOT prove current bridge availability, fallback, parity, token satisfaction, or direct-only release admission.  
* The governed DDL fingerprint, grants, boundary-view, search-path, role, partition, Index, Mirror, checksum, and path-proof evidence remains owned by **PF12 — HDE-Schemas & Artifacts**.

**Implementation posture.** The direct-only behavior is Required-Now. At the pinned repository commit, `engine/db/adapter.py` statically confirms retired-key rejection, `DATABASE_URL`\-only selection, direct psycopg construction, and zero alternate-transport attempts in its selection records, but the exact required evidence path `artifacts/db/conn_env_selection.log` is absent. Static bytes do not establish every evidence artifact, deployed database state, role, grants, `search_path`, token satisfaction, or runtime success.

---

### 6.3.3 Routing (titles-only)

Tokens: §2.0 Acceptance Tokens.  
Evidence & mirror hygiene: **PF12 — HDE-Schemas & Artifacts** (human `INDEX.json` \+ hash sentinel \+ machine mirror updated in the same PR).  
Infra names/ownership: **Glow Infrastructure** (names-only).

---

## 6.4 QA branches (evidence-only) \[Required-Now\]

**Scope (cross-reference).** In QA branches, changes are **evidence-only** and CI is **diff-scoped to governed files**; do not modify application/presenter bytes, schemas, or runtime config outside an approved release epic. Permitted changes are limited to **updating the Human Evidence Index** (`docs/evidence/INDEX.json`), its **hash sentinel** (`docs/evidence/INDEX.sha256`), the **machine mirror** (`artifacts/evidence_index.jsonl`, records-only, canonical JSONL, one LF, unknown-key rejection, ASCII field order, sort-before-write, single file, each with a `proof_anchor` to a co-located path-proof), **proof artifacts under `artifacts/**` (e.g., A7 headers & composite JSON on Catalog success routes, rails refusal/conformance probes, DB posture & env-connectivity snapshots, start-command/env-pins, SBOM)**, and governed QA manifests and primary logs under **`audit/qa/**`**—all indexed in **PF12 §8.6** in the **same PR** per PF06. For process, **do not restate procedure here**: see **Epic-Process-Guide** (QA PR template, PR-first, same-PR evidence rule) and **PF06 §0.7** (QA branches are evidence-only; CI is **diff-scoped**). *Tokens:* see **§2.0** (`QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`). *Evidence hygiene:* mirror parity and hash-sentinel gating per **PF12 §8.3/§8.6**.

---

# 7\) Logging & Observability \[Required-Now\]

## **7.1 Keys-only logging \[Required-Now\]**

**Principle (normative).** Operational logs **MUST** be keys-only: no request/response payloads, no header values, and no secrets or PII. Messages use bounded labels and deterministic formats suitable for automated analysis.

### **7.1.1 Prohibitions**

* **No payload bodies.** Never log Reader or CLI JSON bodies, vendor requests, or vendor responses.  
* **No header values.** Never emit concrete header contents (e.g., `Authorization`, `HD-Api-Key`, `HD-Geocode-Key`, `Set-Cookie`, ETag payload).  
* **No secrets or PII.** API keys, tokens, user identifiers, free-text inputs, or locations are not logged.

### **7.1.2 Redaction and safe fields**

* **Secrets redacted.** If a secret key name must be mentioned, print a placeholder only (e.g., `HD-Api-Key: REDACTED`).  
* **Error objects.** Typed errors are logged as numeric-free `{code, message}` tuples; never echo vendor or body text.

### **7.1.3 Bounded label set (examples)**

Use a small, fixed set of labels. Values come from closed enums.

* `route` (e.g., `reader_v1`, `vendor_hdapi`)  
* `outcome ∈ {ok, usage, typed, transport, network_error, 4xx, 5xx, 429}`  
* `rails_state ∈ {open, closed}`  
* `timeout_profile ∈ {small, default, long}` (when rails are open)  
* `attempt_idx` — retry attempt as a small integer

`correlation_id` is a bounded, non-PII log field. It MUST NOT be a metric label.

### **7.1.4 Determinism and formatting**

* **Deterministic structure.** Emissions are stable key/value objects (JSON or equivalent), locale-neutral, and free of ANSI/BOM.  
* **No free text.** Avoid narrative strings; prefer tokens and enums.  
* **Time fields.** If present, use UTC ISO-8601/RFC timestamps. Never log wall-clock deltas derived from payload contents. Run checks under `LC_ALL=C`, `TZ=UTC`.

### **7.1.5 CI and enforcement**

* **Grep guards.** Fail the pipeline on patterns that indicate payload/body dumps, header value logging, or raw secrets.  
* **Allow-list.** Maintain an allow-list of safe labels. New labels require a Doc-Delta and tests.  
* **Spot checks.** Include redaction fixtures and log-shape tests in the Evidence Index. Verify no payloads or values appear in logs.

**Refusal vs 429 (keys-only) — scope note.**

* **Refusal (rails closed):** every request-scoped refusal log is limited to exactly the seven-key allow-list `{at, route, status, duration_ms, idempotence_hash, release_id, correlation_id}`. No additional key is allowed. The correlation identifier MUST be present, non-empty, bounded, format-valid, and equal to the correlation carrier emitted for that request.  
* **429:** `retry_after_ms` remains outside the refusal schema. A separately governed 429 log may include it only under its own rate-limit contract; never echo payload or header values.

**Tokens (titles-only; see §2.0).** `PF04_LOG_ALLOWLIST_009_OK`, `ERROR_CTYPE_JSON_UTF8_OK`, `NO_CONTENT_ENCODING_OK`, `NO_EXTERNAL_IO_ON_REFUSAL_OK`.

### 7.1.6 Privacy (BodyGraph/vendor inputs) \[Required-Now\]

* **No birth data.** Never log birth details or any BodyGraph input fields.  
* **No payload echo.** Do not log vendor request/response bodies or derived payload content.  
* **Secrets never logged.** API keys/tokens/credentials must not appear; if referenced, use redacted placeholders (e.g., `HD-Api-Key: REDACTED`).  
* **Bounded metrics families only.** Use fixed, low-cardinality metric families and labels; do not encode payload content or PII in labels.  
  *(Examples of bounded labels: `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`.)* `correlation_id` is a log field and MUST NOT be a metric label.

## **7.2 Correlation ID \[Required-Now\]**

**Principle (normative).** A non-PII, request-scoped correlation identifier ties together logs and traces across CLI, Reader, and (when rails are open) vendor calls. It is transport/ops-only, **never** part of the public payload or deterministic product inputs, and is propagated unchanged for one request.

### **7.2.1 Requirements**

* **Non-PII and secret-free.** The value **MUST NOT** encode personal data, tokens, or payload content.  
* **Stable propagation.** A single correlation ID **MUST** be generated/selected at entry and propagated unchanged through all downstream calls/logs for that invocation.  
* **Request independence and deliberate reuse.** Independently initiated `(A,B)` and `(B,A)` requests need not share an identifier. If a caller deliberately reuses one valid identifier for an AB/BA diagnostic, the Adapter MUST propagate it unchanged. Otherwise each request receives its own identifier.  
* **Payload-free.** The correlation ID **MUST NOT** appear in the Reader public body (success or error). It does not affect `idempotence_hash` or `ETag`.

### **7.2.2 Format and bounds**

* **Charset/length.** ASCII opaque token from a bounded alphabet (e.g., `[A-Z0-9-]`) with a fixed maximum length (e.g., ≤ 64).  
* **Selection, validation, and replacement.** Use a caller-supplied identifier only when it matches the bounded transport format. If the inbound value is missing or invalid, generate a safe replacement at the Adapter boundary and do not log or echo the unvalidated value. The identifier MUST NOT be derived from birth data, chart contents, user IDs, pair order, Human Design inputs, Magic-10 results, or any other personal or mathematical input.  
* **Bounded cardinality.** Use correlation ID as a field, never as a metric label.

### **7.2.3 Propagation (transport and logging)**

* **Transport.** Propagate via a single, pinned transport carrier owned by the CLI/Reader transport spec (titles-only routing).  
* **Logging.** Include the correlation ID in keys-only logs. Redact nothing except to enforce format/length bounds. **Do not** log header values.  
* **Vendor calls (rails open).** If a vendor call is made, forward the correlation ID as metadata only. Never echo vendor bodies or header values to logs.

### **7.2.4 Validation (binary)**

* **Presence & format.** When required, the emitted correlation ID **MUST** be present and match the pinned format bounds. Missing or malformed inbound values are replaced safely and are not echoed or logged raw.  
* **AB↔BA and two-run neutrality.** Deliberate reuse of one valid identifier is propagated unchanged, while independently initiated requests may use different identifiers. In every case the identifier does not change public bytes, `idempotence_hash`, `ETag`, Human Design computation, or Magic-10 results.  
* **CI checks.** Tests assert presence/format, no appearance in public payloads, and keys-only logging with no secrets or payloads.

**Implementation posture.** At the pinned repository commit, the inspected Adapter accepts an inbound correlation value without the bounded validation required here and generates a `uuid4` fallback; the two inspected HTTP logging helpers and the refusal-log test enforce the former six-key record and omit `correlation_id`. The selected application factory also does not install the inspected logging filter. Static inspection therefore does not establish conformance, runtime emission, or token satisfaction.

### **7.2.5 Routing (titles-only)**

Carrier name, precise header casing, and where/when it is set are defined in **HDE-CLI-API-Vendor-Ref** (transport section). Governance does not duplicate transport bytes.

## **7.3 Narratives persistence logging (admin-only) \[Required-Now\]**

**Rule.** Do **not** log narrative text or fragment content. Logs MUST be keys-only and **product/payload-numeric-free**. For this log family, that term means that a digit-bearing or numeric value is allowed only when the field is in the closed schema below, has exclusively operational meaning, has a fixed type and bound, cannot reveal or reconstruct product or user payload content, and is covered by positive and negative schema tests. It does not permit arbitrary operational numbers, semantic laundering into strings, hashes, buckets, prefixes, or free text, or reuse of general HTTP log fields by analogy.

This scoped internal audit-log definition does not alter the literal public Reader v1 numeric-free covenant in §8.1, the governed typed-error contract, or any general HTTP, refusal, benchmark, metric, or transport log schema outside §§7.3 and 7.4.

**Allowed fields in logs (closed keys-only eligibility allowlist).** This table defines which fields may be eligible for a narrative-persistence event; it does not make every field mandatory.

| Field | Type and bound |
| :---- | :---- |
| `at` | JSON string containing the event time in UTC RFC 3339 form with fixed millisecond precision, `YYYY-MM-DDTHH:MM:SS.sssZ`; it MUST match `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z$` and parse as a valid calendar timestamp. Local time, offsets other than `Z`, numeric epochs, free-text time, and request- or birth-derived time are prohibited. |
| `composition_id` | Governed bounded opaque string. |
| `fragment_ids.length` | JSON integer exactly `1` when present; booleans are invalid. It is present only for a governed PF17 Text composition with a fragment list and absent when no fragment list is exposed, including Suppressed output. |
| `pack_sha` | Governed bounded opaque digest string. |
| `release_id` | Governed bounded opaque release-identity string. |
| `dyad_id` | Governed opaque reference only; it MUST NOT expose or encode personal or birth data. |
| `request_id` | Governed bounded opaque request reference. |
| `writer` | Closed writer enum or bounded writer identifier; no free text. |
| `correlation_id` | Governed non-PII bounded correlation string. |

The former `timestamps` spelling is replaced by the single key `at`; it does not authorize an open class of time fields. `at` is operational audit metadata and MUST NOT enter BodyGraph calculation, narrative selection, Magic-10 results, `composition_id`, `idempotence_hash`, `ETag`, `release_id`, pack identity, or public bytes. Audit records are not required to be byte-identical across repeated invocations because event time changes; product and release bytes remain deterministic and time-independent.

**Prohibited logging.**

* The narrative text itself.  
* Any raw `fragment_ids` values or fragment content.  
* Payload echoes, secrets, or headers with credentials.  
* Birth data, locations, timezone-resolution inputs, coordinates, provider request data, BodyGraph inputs or intermediates, and planetary or ephemeris values.  
* Magic-10 results, bands, scores, percentages, weights, thresholds, caps, ranks, resonance values, eligibility values, category arrays, or scoring intermediates.  
* Narrative templates, candidates, prompts, positions, rankings, suppression details not admitted by a separately governed bounded enum, admin-bundle content, names, emails, raw account or session identifiers, database URLs, vendor text, stack traces, and any payload-derived count other than the exact `fragment_ids.length` permission above.

**Redaction and shaping.**

* Redact secret-bearing headers and payloads.  
* If a governed PF17 Text fragment list is present in an internal trace, record only `fragment_ids.length` with integer value exactly `1`; reject `0`, values greater than `1`, negative values, floats, strings, and booleans. Suppressed output omits the field.  
* Never emit the fragment array, an individual fragment or template key, narrative content, or a count derived from characters, words, sentences, candidates, ranking, suppression evaluation, or user data.  
* A future PF17 or PF12 contract that permits multiple fragments does not broaden this domain automatically. A normative PF04 Doc-Delta MUST define the new bound, privacy impact, schema change, and required tests before any other integer may be emitted.  
* Keep labels bounded and consistent to preserve cardinality discipline.

**Validation (binary).** Positive schema coverage MUST accept an otherwise valid allowlisted narrative-persistence record with a valid `at` and `fragment_ids.length: 1`. Negative coverage MUST reject every other fragment-count type or value; raw `fragment_ids`; narrative, fragment, template, candidate, prompt, or payload content; malformed, local, offset, epoch, request-derived, or birth-derived timestamps; undeclared numeric or digit-bearing fields; prohibited Human Design or Magic-10 values; names, emails, credentials, secrets, raw user identifiers, headers, and free text; and any encoded, hashed, truncated, bucketed, or stringified substitute for prohibited meaning. Log creation and timestamp generation MUST NOT influence engine output, narrative selection, canonical response bytes, identity hashes, `ETag`, or release identity. The structural count `1` does not prove correct composition, narrative quality, Human Design, or Magic-10 correctness.

**Evidence (titles/paths only).**

* `ci/jobs/logs_keys_only_redaction.yml` — required CI evidence locus; for this log family it MUST prove that logs contain no narrative text and only the allowed keys.  
* Optional audit sample demonstrating absence of text in logs.

Any audit sample used as evidence MUST follow the same policy, and redaction MUST NOT preserve enough structure to reconstruct a prohibited value. Log-shape evidence proves only logging conformance; it does not prove Human Design, Magic-10, narrative, transport, authentication, release, deployment, or runtime correctness.

**Implementation posture.** At the pinned repository commit, the named CI file exists but governs general safe-rails and vendor-log evidence; its checked-in content does not establish the narrative-persistence schema above. Exact searches did not find `fragment_ids.length` implementation. Static inspection does not establish implementation, test passage, evidence completeness, or acceptance-token satisfaction.

**Acceptance (titles-only).** Governed by logging/redaction tokens listed in §2.0 and the Evidence Index parity tokens (human ↔ machine, same PR).

**Routing (titles-only).**

* Field/length constraints for narratives: **HDE-Schemas & Artifacts** (composer response).  
* Storage locations and DB names: **Glow Infrastructure** (names-only).  
* Transport and A7 policy: **HDE-Governance** (this document) and **HDE-CLI-API-Vendor-Ref** for endpoint bytes.

## **7.4 Admin bundle audit logging (admin-only) \[Required−Now\]**

**Principle (normative).**  
Every **admin bundle** request (CLI or HTTP) that successfully returns a bundle **must** produce a single, bounded **audit log record** that is keys-only, secret-free, and **product/payload-numeric-free**, consistent with §7.1 and §8.2. For this log family, product/payload-numeric-free has the scoped meaning defined in §7.3: only fields in the closed schema below may carry digit-bearing or numeric operational metadata, and no product, user-payload, Human Design, Magic-10, narrative, arbitrary operational, or semantically laundered numeric content is permitted. Audit logs are ops-only and are never exposed on public surfaces. The successful-audit record uses the exact six-key base schema below.

### **7.4.1 Required audit fields (keys-only)**

For each successful admin bundle invocation, the audit record **MUST** contain exactly these six base fields:

* `at` — JSON string containing the event time in UTC RFC 3339 form with fixed millisecond precision, `YYYY-MM-DDTHH:MM:SS.sssZ`. It MUST match `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z$` and parse as a valid calendar timestamp. Local time, an offset other than `Z`, a numeric epoch, free-text time, and request- or birth-derived time are prohibited.  
    
* `route` — a bounded route identifier (for example, `cli_admin_bundle` or `http_admin_bundle`); no URLs or free text.  
    
* `caller` — a bounded, non-PII principal or service label represented as a string; not a name, email address, credential, session token, or raw user identifier.  
    
* `input_kind` — a closed enum describing only the high-level input class (for example, `birth_match` vs `user_match`); it must **not** contain input values, raw birth data, names, or locations.  
    
* `release_id` — the governed bounded, opaque, manifest-derived runtime release identity.  
    
* `correlation_id` — the correlation identifier described in §7.2 (non-PII; bounded charset/length).

No general-HTTP field such as `status`, `duration_ms`, `attempt_idx`, or `retry_after_ms` is imported by implication. No free-text narrative, payload excerpt, header value, product-derived number, or undeclared field is permitted.

Any additional admin-bundle audit field requires all of the following before adoption:

1. a normative PF04 Doc-Delta;  
2. a field name, type, semantic definition, and closed domain or numerical bound;  
3. a demonstrated operational need that cannot be met by the existing six keys;  
4. a privacy and security review showing that the value cannot expose or help reconstruct a payload, credential, PII, birth data, or Human Design result;  
5. positive and negative schema tests; and  
6. same-PR updates to the owning schema, allowlist, evidence references, and affected documentation.

There is no catch-all permission for additional numeric data.

**Validation (binary).** Positive schema coverage MUST accept both successful CLI and successful HTTP admin-bundle audit records containing exactly the six base keys with valid closed-enum and bounded opaque-string values, a valid canonical `at`, and a propagated bounded non-PII `correlation_id`. Negative coverage MUST reject every extra or undeclared field, including `status`, `duration_ms`, `attempt_idx`, and `retry_after_ms`; any malformed or request-derived timestamp; names, emails, credentials, session or raw user identifiers, headers, secrets, and free text; and any birth, location, BodyGraph, Magic-10, narrative, admin-bundle, meta, payload, or encoded substitute content. Audit creation MUST NOT influence product calculation, selection, serialization, hashing, `ETag`, release identity, or public emission.

### **7.4.2 Prohibitions (admin bundle)**

In addition to the general prohibitions in §7.1 and §8.2:

* **No birth data or BodyGraph inputs.** Admin bundle audit logs **must not** include birth dates, times, locations, or any BodyGraph input fields (see §7.1.6).  
    
* **No payload echo.** Do not log any part of the admin bundle JSON (BodyGraphs, compat payloads, narratives, or meta).  
    
* **No secrets.** Admin credentials (e.g. admin tokens) and HTTP header values (including `Authorization` or any admin header) must never appear in logs; if referenced, they must be redacted placeholders (e.g., `Admin-Token: REDACTED`).

### **7.4.3 Evidence and routing (titles-only)**

* Evidence: At least one governed sample of admin bundle audit logs (with payload/secret redaction) and a CI job or test that asserts the required fields are present and that no disallowed content appears.  
    
* Routing: Field-level schema and storage locations for admin bundle audit logs (files vs log streams) are owned by **HDE-Schemas & Artifacts**, **Glow Infrastructure**, and **Glow QA Guide** (titles-only). PF04 owns the policy for **what must be logged and what must not**; logging mechanics live elsewhere.

**Implementation posture.** At the pinned repository commit, exact searches did not find `cli_admin_bundle` or `http_admin_bundle` implementation, and current PF09.7 marks the governing admin-authentication and audit-logging work `Not done`. This section defines Required-Now policy; it does not claim implementation, QA passage, evidence completeness, deployment, admin-surface availability, or token satisfaction.

---

# **8\. Security & Privacy \[Required-Now\]**

## **8.1 Numeric-free public covenant \[Required-Now\]**

**Principle (normative).** All public-facing **Reader v1** responses are **numeric-free** and **narrative-free**. Public payloads disclose **only** categorical results in the shape `{ "id", "band" }`. **No** scores, percentages, prompt text, or other numerics may appear on the public surface.

The product/payload-numeric-free definition for the internal audit-log families in §§7.3 and 7.4 does not alter this literal public covenant.

**Docs/review restatement for adjacent-surface changes.** When a plan, PR summary, docs sweep, review artifact, or closeout artifact changes or reviews adjacent narrative, DB, compat, admin, vendor, router, or internal evidence surfaces while the Reader v1 public contract remains unchanged, the artifact MUST state that boundary explicitly. The statement MUST distinguish adjacent internal, admin, compat, evidence, or deferred-vendor work from any public Reader v1 contract change and MUST NOT imply public Reader enablement, public payload drift, HDAPI v2 conformance, or a new public surface unless that change is explicitly in scope and governed by the relevant contract update.

### **8.1.1 Scope**

* **Applies to:** all public responses from the Reader v1 surface (**HTTP 200 success** and all **typed errors**) and all **CLI stdout** outputs intended to mirror public bytes.  
* **Does not apply to:** internal compatibility math, presets, or bench diagnostics stored as **private artifacts or logs**. These remain internal only and **redacted** in public.

### **8.1.2 Requirements**

* **Categories array (public shape & domain).**  
    
  * Each item in `categories[*]` **MUST** be exactly `{ "id": <string>, "band": <enum> }`.  
  * `band ∈ {"Cool","Open","Warm","Glow"}`.  
  * `id` **MUST** be a **Magic-10 identifier** from the **closed set and order** (see PF-Canon-HDE-Schemas and Artifacts §2.6 / PF-01 §5.1).  
  * **v1 exposure rule:** if `eligible == true`, the array **MUST** contain **exactly one** item, `{"id":"harmony","band":<BAND>}` (PF-01 §2.2). If `eligible == false`, the array **MAY** be empty.  
  * **No numeric fields** are permitted (e.g., `score`, `score_pct`, `index`, `rank`).


* **Top-level structure (success).** The success body contains **exactly six keys**:  
  `reader_version, eligible, categories, meta, release_id, idempotence_hash`.  
  No additional top-level fields may be introduced without a **versioned Reader contract** update.  
    
* **Typed errors (numeric-free).**  
    
  * Error objects are numeric-free; only `{ ok:false, code, error }` are allowed.  
  * Optional `retry_after_ms` is the **sole integer** field, used **only** under controlled vendor retry policies (see **PF-Canon-HDE-CLI-API-Vendor-Ref**, titles-only).


* **Narratives and prompts.** Public payloads **MUST NOT** include prompt text, narratives, or user-facing messages generated by internal modules. These are **retired**.  
    
* **Resonance posture (public).** Public payloads **MUST NOT** expose SR/XR numerics. v1 ships **SR-only** (`alpha=1.0`); **hysteresis \= 1** is armed for future XR and **not exposed**.

### **8.1.3 Validation (binary)**

* **Schema gate.** Verify success has **exactly six keys** and that `categories[*]` items are **only** `{id, band}`.  
* **Closed-set check.** `id` values must belong to the **Magic-10** closed set (PF-12 §2.6 / PF-01 §5.1); **no extras/omissions**.  
* **Numeric-free grep-guard.** CI blocks any numeric fields or prompt text in public payloads.  
* **Canonical JSON.** Public bytes are serialized as **UTF-8 (no BOM)**, **sorted keys**, **compact**, **exactly one trailing LF**; arrays used as sets are **deduped and ASCII-sorted** (PF-12 §4).  
* **Parity enforcement.** **Reader↔CLI** parity gates confirm **identical numeric-free** payloads for the same inputs and environment, under **`LC_ALL=C`**.

**Implementation posture.** At the pinned repository commit, `schemas/reader.v1.schema.json` permits the four category identifiers `open_leader`, `warm_leader`, `cool_leader`, and `glow_leader`, excludes `harmony`, and still declares an optional `prompt` property. Those checked-in schema bytes do not conform to this section's v1 exposure and prompt-prohibition requirements. Static inspection does not establish runtime emission, validation passage, deployment state, or acceptance-token satisfaction.

### **8.1.4 Routing (titles-only)**

Math and scoring details are defined in **PF-Canon-HDE-Math-Spec**. The public emission policy **lives here** and governs the Reader and CLI surfaces. Resonance constants and pack/manifest rules live in **PF-Canon-HDE-Schemas and Artifacts**.

**Acceptance & CI (titles-only)**  
`RESONANCE_PUBLIC_POSTURE_OK`, `CLI_READER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `PREFS_KEYSET_10_OK`, `MAGIC10_DOMAIN_CLOSED_OK`

## **8.2 No PII or secrets in logs \[Required-Now\]**

**Principle (normative).** Operational logs MUST NOT contain PII or secrets under any circumstance. Logs are keys only and use bounded, deterministic labels (see §7.1).

### **8.2.1 Redaction rules**

* **Secrets.** Do not write API keys, tokens, session IDs, or header values. If a key name must appear, render as `REDACTED` (for example, `HD-Api-Key: REDACTED`).  
* **PII.** Do not emit names, birth data, locations, or free text copied from payloads.  
* **Bodies.** Never log Reader, CLI, or vendored request or response bodies.  
* **Typed errors.** Emit only numeric free code and message tuples. Never echo vendor text or payload fragments.

### **8.2.2 Safe fields and bounded labels**

* Allowed metric labels are a fixed allowlist (for example, `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`) with closed value domains. No high cardinality user identifiers.  
* `correlation_id` is non PII, bounded in length and charset, and used as a log field for stitching only; it MUST NOT be a metric label (see §7.2).

### **8.2.3 Audit hooks (prove and enforce)**

* **CI grep guards.** Fail on patterns indicating payload or body dumps, header value logging, or raw secrets.  
* **Structured log shape tests.** Verify logs are JSON or equivalent, BOM or ANSI free, and contain only allowlisted fields.  
* **Redaction fixtures.** Keep example log lines with redacted secrets under the Evidence Index (titles and paths only).  
* **Periodic review.** Run scheduled audits to confirm no PII or secrets. File a Doc-Delta if new labels are needed.

### **8.2.4 Incident posture**

* **Immediate containment.** If PII or secret leakage is detected, halt affected jobs, rotate credentials if applicable, and purge offending logs per policy.  
* **Evidence and follow up.** Record the incident (titles and paths only), add tests and guards to prevent recurrence, and document the fix in the Change Log or Doc-Delta.

**Routing.** This section governs ops logging only. Public payload rules remain in §8.1. Transport specifics and vendor behaviors are referenced by title only in the **PF-Canon-HDE-CLI-API-Vendor-Ref**.

## **8.3 Admin surfaces authentication & authorization \[Required−Now\]**

**Principle (normative).**  
Any surface that exposes the **full product payload** (admin bundle) is **admin-only** and **must be authentication- and authorization-gated**. An unauthenticated or unauthorized caller **MUST NOT** be able to obtain an admin bundle, regardless of network location or environment. Admin surfaces are not governed by the numeric-free public covenant in §8.1, but they remain subject to all logging and privacy rules in §7 and §8.

### **8.3.1 Admin surfaces in scope**

This section applies to:

* The **CLI admin bundle command** (titles-only in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide).  
    
* The **HTTP admin bundle route** used by the Admin GUI (titles-only in HDE-CLI-API-Vendor-Ref).

As a Required-Now contract, both surfaces MUST call the internal admin bundle builder defined in **HDE-Mechanics Guide** and MAY return BodyGraph JSON, compat JSON, narrative text, and meta. They are **not** Reader v1 public surfaces and are **not** A7 proof surfaces.

**Implementation posture.** At the pinned repository commit, bounded exact and concept searches did not find the admin bundle builder, CLI command, HTTP route, authentication guard, or dedicated audit implementation, and current PF09.7 marks the governing work `Not done`. This section specifies required behavior; it does not claim implementation, availability, QA passage, evidence completeness, deployment, or token satisfaction.

### **8.3.2 Pre-Glow minimal authentication posture**

Pre-Glow, admin surfaces **MUST** be protected by at least one high-entropy admin credential:

* The credential is stored as a **secret** in Railway or equivalent secret storage defined by **Glow Infrastructure** (names-only) and is **never** checked into the repo.  
    
* Every admin bundle request (CLI or HTTP) **MUST** present this credential via a transport mechanism pinned in **HDE-CLI-API-Vendor-Ref** (for example, a single admin header).  
    
* Missing, empty, or invalid credentials **MUST** result in a typed, numeric-free error; they must **never** return the admin bundle.  
    
* Admin credentials **MUST** be:  
    
  * **Rotatable** without code changes (via secret/config updates only), and  
      
  * **Revocable**, such that removing or changing the secret stops old credentials from working immediately.

Post-Glow, admin surfaces **MUST** align with the wider identity/auth model for app users and admins; this section records the minimum pre-Glow requirement that admin surfaces **must not remain open**.

### **8.3.3 Authorization and least privilege**

* Admin credentials and accounts used for admin bundle access **MUST NOT** be shared with end users or application-level identities.  
    
* Access to admin credentials **MUST** be limited to designated operators; storage locations and access control are governed by **Glow Infrastructure** and **Glow QA Guide** (titles-only).  
    
* Any future role-based or multi-tenant admin model must preserve the invariant that only authorized admin principals can call admin bundle surfaces.

### **8.3.4 Logging and privacy coupling**

Admin surfaces remain fully subject to:

* The **keys-only logging** rules and redaction posture in §7.1 and §8.2 (no payload bodies, no header values, no secrets or PII in logs).  
    
* The BodyGraph-specific privacy rules in §7.1.6 (no birth data or BodyGraph inputs in logs).  
    
* The admin bundle audit logging requirements in §7.4 (per-call audit record with timestamp, caller, input kind, release\_id, correlation\_id).

An authorized admin response may contain the full product data described in §8.3.1, but its audit and operational log records remain payload-free. The exact successful-audit schema remains in §7.4 and is not duplicated here.

Admin credentials themselves (for example, admin tokens) **must never** appear in logs or user-visible payloads; if mentioned, they must be fully redacted (e.g., `Admin-Token: REDACTED`).

### **8.3.5 Token coupling**

The **ADMIN\_AUTH\_REQUIRED\_OK** token in §2.0.17 is **satisfied** only when:

* Both CLI and HTTP admin bundle surfaces are protected by admin authentication as described above.  
    
* QA harnesses demonstrate that unauthenticated and mis-authenticated calls fail closed with typed, numeric-free errors and never return bundles.  
    
* Evidence of the active auth posture (titles and paths only) is present in the Evidence Index and machine mirror in the same PR as any change to admin auth behavior.

Routing for admin auth mechanics (credential shape, header names, GUI auth flows) lives in **HDE-CLI-API-Vendor-Ref**, **HDE-Mechanics Guide**, **Glow Infrastructure**, and **Glow QA Guide** (titles-only). PF04 owns the governance: admin surfaces are **never open**, and any change to their auth posture is a **normative change** that requires a Doc-Delta and updated evidence.

# 9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]

**Purpose.** Define the repo-level rules that keep governance, evidence, and code in lock-step. **PF12** remains the single home for index/mirror schemas and canonical JSON rules; this section pins the **policy and gates** (names-only routing to PF12 for bytes).

> ---

## 9.1 Single-home doctrine (routing by title)

**Ops tasks (PO-authorized execution; IA-guided; not PR work).**

An **Ops task** is any work item that requires privileged access to systems outside the repository. This includes service configuration, secrets and environment-variable changes, deploy or runtime settings, infrastructure-console actions, and privileged database operations such as role creation, grants, production migrations, or other external-state changes. The work remains OPS regardless of whether the Product Owner executes it personally or delegates execution.

1. **Execution authority and delegated executor.** Ops tasks MUST be authorized by the Product Owner. The PO may execute an authorized task personally or explicitly delegate execution to an automated session agent. “PO-only” identifies the owner of authorization, accountability, and acceptance; it does not require the PO to be the physical keystroke actor.  
     
   * A direct current PO instruction constitutes project-level delegation only when the task identity, objective, target, and approved scope are concrete; every required task-specific authorization exists and remains valid; the executor has the required tool capability, access, and credential presence without exposing credential values; required preconditions, stop checks, rollback controls where applicable, and evidence paths are concrete; and the action is permitted by external system, platform, host, service-provider, organizational, legal, and safety controls.  
   * When those predicates are satisfied, the delegated agent MUST proceed within the authorized scope and MUST NOT demand a second generic human-only approval solely because the operation is operational, privileged, live, mutating, deployment-related, configuration-related, secret-backed, or externally visible.  
   * The delegated agent MUST stop when an objective blocker invalidates execution, identify the concrete blocker, preserve completed safe work and evidence, and state the smallest PO input or external action required to resume. Product Owner authorization cannot override external controls, manufacture unavailable access or credentials, validate nonexistent artifacts, or make an unsafe or materially ambiguous command concrete.  
   * For mutating, privileged, deployment, configuration, database, or secret-backed work, the exact target and authorized effect MUST be concrete before dispatch; required rollback or recovery intent and any mandatory STOP CHECK MUST be concrete before the externally mutating boundary; secret values MUST remain out of commands, logs, chat output, and repository evidence unless securely injected without disclosure; and completion MUST be supported by the required secret-free OPS evidence.  
   * The Product Owner remains the authorizing principal and accountable owner. The delegated agent is the executor and evidence producer, not an independent approver.

   

2. **Not a PR.** Ops tasks are not PR work. Any implementation or remediation document that includes Ops work MUST separate Ops tasks from repository-local DEV work and label the Ops items as Product Owner-authorized execution, IA-guided.  
     
3. **Ops task record (required fields).** Every Ops task record MUST include: Task ID, Owner (PO), Facilitator (IA), target system/service (name only, no secrets), intent/end state, constraints/safety rails, success criteria (observable outcomes), evidence to capture (artifact paths), rollback intent, and a secret-handling note (no plaintext secrets in docs or evidence).  
     
   * When canon already provides concrete operator steps, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules for the task, the Ops task record MUST include those canon-grounded instructions explicitly rather than remaining only at the level of intent, constraints, or outcome.  
   * This does not authorize invented procedure. If canon is silent, incomplete, or ambiguous for the needed procedure, the Ops task record MUST state that the missing instruction is unknown and MUST NOT fabricate steps. Any PF references used for these instructions remain titles-only.

   

4. **Evidence posture (required).** Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase audit path such as `audit/ops/<epic-id>/...` (or `audit/qa/<epic-id>/...` when captured as part of QA execution). Evidence MUST NOT include secrets. If a setting/value is sensitive, evidence MUST be presence-only, redacted, or hashed, while still being sufficient to verify the intended state.  
     
   * **Environment-validation disposition rule.** When an Ops task exists to validate intended environment bindings or dev/admin harness reachability across one or more environments, the evidence bundle MUST record each intended environment separately as either `validated` or `not yet closed`, with an explicit reason for every `not yet closed` result.  
   * **No silent closure.** If the same run records a gating discrepancy, failed validation, missing prerequisite, or other unresolved condition for an intended environment, the Ops bundle MUST preserve that environment as `not yet closed` and MUST NOT present it as closed in any related binding-disposition or closeout surface.  
   * **No guessed binding in validation evidence.** If an intended environment does not have a published infra-owned binding, the Ops bundle MUST record that absence explicitly and MUST NOT guess a URL, hostname, or port in order to force a validation run.  
   * **Bounded meaning of a truthful validation slice.** A bounded Ops validation task MAY still be complete as an evidence-capture or classification slice when it truthfully records one or more environments as `not yet closed`, but that result MUST NOT be used to imply that the underlying PF09 scope or closeout claim is complete.

   

5. **No governance drift.** Ops tasks MUST NOT create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it MUST map to existing governance-defined acceptance posture and be proven via evidence artifacts.  
     
6. **Mechanics tracking.** Any Ops task included in an Epic MUST be represented as a component in the HDE-Mechanics Guide (titles-only) and have a related task or subtask in the HDE Build Checklist.

**Transport & ops policy live here (PF04).** A7 invariants, conditional rules, refusal posture, Aux suppression carve-out, and `/internal/version` ops semantics are governed in PF04.

**CLI/Reader wire bytes live in PF05.**

**Pack/manifest/mirror schemas live in PF12.**  
Use **titles-only** cross-references; **do not duplicate bytes** across documents.

> ---

## 9.2 What requires a Doc-Delta \[Required-Now\]

A Doc-Delta is **mandatory** for any normative change that can affect **identity, acceptance, or operations**. Open a Doc-Delta **before** making any of the following changes, and land it **only with updated evidence** (see §4) and a synchronized **Evidence Index** entry.

* **Math change (freeze-pack impact).** Any change to frozen math inputs or their canonicalization: category membership or order, band maxima, vocab tokens, fold or priority rules, dampener recipes, floors or caps, preset catalog or schema, or any manifest bytes that would yield a new `release_id` (§5.1). The Doc-Delta **MUST** include the new manifest digest and `release_id`.  
* **Public contract (Reader or CLI).** Any change to the public success or error shape, adding fields, changing categories policy, or altering the numeric-free covenant; any transport-visible behavior that modifies public bytes.  
* **Serializer or emitter path.** Any change to the single presenter emitter or its canonicalization rules (UTF-8, sorted keys, compact, one LF), or introducing/removing emitters on public paths.  
* **Schema gates.** Tightening or loosening public schemas (success or typed errors), changing allowed enums, or modifying validation that could alter acceptance outcomes.  
* **Transport policy (A7).** Changes to ETag identity, conditional delivery for 304 or HEAD, Cache-Control rules, or any header matrices that affect acceptance.  
* **Rails enablement (vendor posture).** Opening rails for live HTTP, changing timeouts, retries, backoff, or 429 policies; adding/changing typed vendor error mapping; any modification to redaction/observability that impacts acceptance.  
* **Security and logging.** Adjustments to keys-only logging, redaction rules, correlation propagation, or bounded label sets that alter operational guarantees.

**Landing conditions (binary).** A Doc-Delta is **Accepted** only when: (a) implicated A-gates pass (A3 or A4 or A7 as applicable), (b) governed evidence and all required PF12-owned Human Evidence Index, hash sentinel, Machine Evidence Mirror, and path-proof updates land in the same change, with PF04 Appendix D routing pointers refreshed when affected, and (c) **freeze-pack** impact is recorded if present. Otherwise it is **Rejected** and must not ship.

> ---

> ## 9.3 Doc-Delta entries (what to record for any normative change)

Every normative change **MUST** add a short “Doc-Delta” entry to **§9.3.1 PF04 Governance Change Log \[Required-Now\]** with:

* **Scope** (one line): what changed, at a glance.  
* **Targets** (anchors/sections by title).  
* **Acceptance impact:** which tokens are affected (names-only; token roster lives in §2.0).  
* **Evidence impact:** which artifacts/paths were added/rotated/removed (titles only).  
* **Freeze-pack impact:** whether `release_id` changed (PF12 owns bytes).

*Rationale:* PF10 addenda are living; a higher-numbered applicable addendum supersedes lower-numbered guidance only for overlapping or explicitly superseded scope, so the Doc-Delta ties **decision → bytes → evidence** in a single PR.

> ### 9.3.1 PF04 Governance Change Log \[Required-Now\]

This subsection is the canonical PF04 version-to-change ledger for every effective normative PF04 change. The PF04 normative body controls operative meaning if a local entry conflicts with the body. A local entry is an index and traceability surface; it does not by itself prove implementation, validation, evidence coherence, landing, deployment, QA, OPS, approval, or runtime state.

**Record class and authority.** Every effective entry MUST declare exactly one record class.

* **`EPIC_BOUND`.** `Epic ID` MUST be a concrete `HDE-EPIC<NNN>`. The draft or binding surface MUST be `audit/docdeltas/hde-epic<NNN>_doc_deltas.md`, and the stable record surface MUST be `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md`. Both epic files MUST carry the same `DOC-DELTA-ID` and complete PF04 semantic fields and MUST be byte-identical at close as required by **HDE Epic-Process Guide**. The local entry MUST carry the same PF04 version, ID, record class, summary facts, and pointer to the stable epic record. It MUST NOT duplicate execution, QA, or closeout history. An unapplied epic candidate MUST NOT appear as an effective local entry.  
    
* **`NON_EPIC`.** `Epic ID` MUST be `NOT APPLICABLE - NON_EPIC`; `Draft / binding surface` MUST be `NOT APPLICABLE - NON_EPIC`; and `Stable record surface` MUST be `PF04 §9.3.1 / <DOC-DELTA-ID>`. The local entry and its completed §9.4 record are the authoritative local record for the PF04 governance decision. The complete §9.4 record MUST be nested directly under the local summary line. This class MUST NOT mint a synthetic epic, path, token, QA status, board field, or evidence family, and it does not waive any obligation owned elsewhere.

**Stable identity and same-change coupling.** Each `DOC-DELTA-ID` MUST use `GOV-YYYYMMDD-<shortslug>`, be unique within §9.3.1, and remain immutable after landing. A correction MUST use a new ID and name the corrected ID. The PF04 body change, local entry, and every other required PF04 update MUST land in the same repository change or pull request. For `EPIC_BOUND`, the two epic files synchronize through the epic workflow and MUST preserve the same ID and facts.

**Local summary grammar.** Every entry MUST begin with exactly this one-line field order:

`<PF04-version> | <DOC-DELTA-ID> | <EPIC_BOUND|NON_EPIC> | Scope: <scope> | Targets: <titles/anchors> | Acceptance: <token names or None> | Evidence: <paths/titles or None> | Freeze-pack: <Yes|No> | Canonical record: <stable epic path or PF04 §9.3.1 / ID>`

An instantiated entry MUST contain no placeholder, blank required field, or “fill later” notation. An effective entry is complete only when the corresponding PF04 body change and local entry are both present, every required §9.4 field is concrete, and the class-specific authoritative record is complete. For `EPIC_BOUND`, close additionally requires byte identity between the two epic files. Proposals, candidates, unapplied edits, incomplete records, and speculative entries MUST NOT be logged as effective changes. Historical entries MUST NOT be reconstructed without direct evidence; when direct evidence is insufficient, the record MUST state bounded uncertainty instead of inventing precision.

> ---

> ## 9.4 Doc-Delta template \[Required-Now\]

Use this template for every normative change. Keep entries concise and action-oriented. All affected **binary gates** must pass (§4), and all required PF12-owned Human Evidence Index, hash sentinel, Machine Evidence Mirror, and path-proof updates must land in the same change. PF04 Appendix D is an informative routing aid and is refreshed when its pointers are affected.

> DOC-DELTA-ID: GOV-YYYYMMDD-\<shortslug\>  
>   
> Date / Author: \<YYYY-MM-DD\> / \<name\>  
>   
> PF04 version: \<version containing this effective change\>  
>   
> Record class: EPIC\_BOUND | NON\_EPIC  
>   
> Epic ID: \<HDE-EPICNNN | NOT APPLICABLE \- NON\_EPIC\>  
>   
> Draft / binding surface: \<concrete epic path | NOT APPLICABLE \- NON\_EPIC\>  
>   
> Stable record surface: \<concrete epic path | PF04 §9.3.1 / DOC-DELTA-ID\>  
>   
> Scope: Math | Public Contract/Transport | Serializer/Emitter | Vendor Ingest | Schema | Acceptance/Evidence | Security/Logging | Rails Enablement | Governance/Documentation  
>   
> Targets (section anchors): e.g., §2.3 A7, §5.1 release\_id, Appendix D  
>   
> Summary (≤ 5 bullets):  
>   
> 1\) \<Action verb \+ concrete change\>  
>   
> 2\) ...  
>   
> Acceptance impact (binary gates to update or verify):  
>   
> \- A3 Determinism. Preimage → sha256 → final; AB↔BA; two-run.  
>   
> \- A4 Reader↔CLI parity. Single emitter; byte equality; schema and shape gates.  
>   
> \- A7 Transport. ETag, 304, HEAD; no-store on writers and errors.  
>   
> \- Rails posture. Refusal closed; conformance open (timeouts, retries, backoff, 429).  
>   
> Evidence updates (titles and paths only):  
>   
> \- Goldens or scripts added or refreshed (AB↔BA, two-run, LF and encoding, preimage recompute).  
>   
> \- Header snapshots and transport sequences (A7).  
>   
> \- CI jobs or grep guards adjusted (no ad-hoc dumps or emitters; keys-only logs).  
>   
> \- PF12-owned Human Evidence Index, hash sentinel, Machine Evidence Mirror, and required path-proofs updated when affected (MUST); PF04 Appendix D routing pointers refreshed when affected.  
>   
> Freeze-pack impact: Yes/No  
>   
> \- If Yes: attach canonical manifest digest and new release\_id (§5.1); list affected pack entries by title and path.  
>   
> Routing (titles only confirmations):  
>   
> \- Math and Architecture rules are referenced by title only.  
>   
> \- Transport and ops bytes remain governed here.  
>   
> Rollout plan:  
>   
> \- Staging gates → optional canary (scope and duration) → promote the exact validated immutable artifact (§5.2).  
>   
> \- Backout or rollback plan (exact last-known-good immutable artifact reference; §5.2).  
>   
> \- Monitoring focus (bounded labels; no payloads or secrets).  
>   
> Change Log entry (one line): `<PF04-version> | <DOC-DELTA-ID> | <EPIC_BOUND|NON_EPIC> | Scope: <scope> | Targets: <titles/anchors> | Acceptance: <token names or None> | Evidence: <paths/titles or None> | Freeze-pack: <Yes|No> | Canonical record: <stable epic path or PF04 §9.3.1 / ID>`  
>   
> ---

> ## 9.5 Same-PR indexing (human ↔ machine parity)

When any golden/evidence path changes, update **in the same PR**:

* **Human Index:** `docs/evidence/INDEX.json`  
* **Hash sentinel:** `docs/evidence/INDEX.sha256` (merge-gating; must match `INDEX.json` bytes)  
* **Machine mirror:** `artifacts/evidence_index.jsonl` (**records-only** canonical JSONL; one LF; ASCII field order; sort-before-write; **unknown-key reject**; **single mirror file**; each record includes **`proof_anchor`** to a stored path-proof)

**Acceptance tokens (names-only).** `EVIDENCE_INDEX_UPDATED_OK` · `EVIDENCE_INDEX_HASH_OK` · `EVIDENCE_INDEX_MIRROR_OK` · `EVIDENCE_PATHS_VALIDATED_OK`. *(Roster lives in §2.0.)*

> ---

> ## 9.6 Pairing proofs with the A7 surface

A7 transport proofs **must** run on a **Catalog JSON success** route (not `/internal/version`). Pair the **composite A7 proof JSON** (PF12 schema) with:

* **Catalog snapshot** (titles-only)  
* **Headers-only env-gate** capture proving non-prod entries are unreachable in prod.

## **9.7 Token fidelity & plan approval rails \[Required−Now\]**

### **9.7.1 Scope**

These rails apply to any implementation plan, Epic Plan, QA plan, or epic record that introduces or consumes QA Acceptance Tokens (including tokens referenced in acceptance maps, manifests, tests, CI jobs, Live QA steps, or evidence artifacts).

They bind reviewers at two distinct decision points:

* **Stage A — Plan Approval (ASK OK):** governs whether a plan is approved to begin implementation. At this stage, plans are execution indexes (pointers) and must not rebuild canonical token libraries, evidence schemas, or QA playbooks. Titles-only references are sufficient.  
    
* **Stage B — QA Ledger Completion (token fidelity \+ evidence wiring):** governs whether the epic is token-complete and ready for epic-level acceptance / close gates. At this stage, token naming, evidence wiring, indexing, and proofs must be complete and non-placeholder.

Stage A plan approval MUST NOT be blocked on PF19/PF19-adjacent registry drainage work (Glow QA Guide token library updates), nor on post-implementation QA execution artifacts; those requirements are enforced at Stage B.

*Important:* PF23 reality-audit scope is an independent axis from QA token strictness. Waiving or narrowing a PF23 audit does not relax token naming, acceptance mapping, evidence wiring, or other canon-backed rails.

### **9.7.2 Token/evidence matrix (QA ledger; not embedded in the plan)**

A token/evidence matrix is a per-epic QA ledger artifact used to demonstrate (and later audit) how each in-scope QA Acceptance Token is enforced and proven end-to-end.

* The matrix is a standalone artifact and MUST NOT be embedded inside an Epic Plan. Plans may include a single pointer line to the matrix location, but MUST NOT duplicate the matrix content.  
    
* **Stage A (ASK OK):** Plan approval MUST NOT be blocked on the absence of an in-plan matrix. If a matrix is expected for this epic, the plan may include a placeholder pointer line (example: `Token/Evidence Matrix: audit/qa/<epic-id>/token_evidence_matrix.md`) indicating where it will be authored during implementation/QA/closeout.  
    
* **Stage B (QA Ledger Completion):** Before an epic is considered token-complete (and before any reviewer asserts epic-level acceptance for in-scope QA tokens), reviewers MUST verify that the matrix exists and is complete for all in-scope QA tokens. No token row may contain placeholder cells (“e.g.”, “TBD”, or implicit gaps).

For each in-scope token row, the matrix MUST include, at minimum:

* governance token name as defined in PF04 §2.0 (verbatim),  
    
* corresponding QA Acceptance Token entry in Glow QA Guide (same name; no aliases),  
    
* acceptance map name (must match; no local aliases),  
    
* tests that exercise the token’s behavior (unit/integration),  
    
* CI jobs that enforce it under closed rails,  
    
* Live QA steps that demonstrate it (if applicable),  
    
* evidence artifacts (repo-relative paths) generated by those tests/steps, and  
    
* Evidence Index and Machine Mirror entries (artifact\_key, epic\_id, tokens, proof\_anchor), as required by the evidence schema.

**Scope-binding versus token posture.** Acceptance maps and the governance-token column of the token/evidence matrix MUST contain only canonical governance token names. They MUST NOT mint epic-local token names, and they MUST NOT use PF09 task or subtask IDs as substitute token names. If a close slice needs to record bound PF09 scope, that scope MUST be recorded in a separate status-only or scope-binding section, or in related closeout or manifest artifacts, not as acceptance tokens.

**Complete scope-binding posture.** When a close slice records PF09 scope bindings, it MUST represent the full in-scope PF09 task and subtask set for that slice truthfully, including any unresolved or not-complete items. Omission of an in-scope PF09 binding is non-conforming.

**Temporary-token claim rule.** A token MAY be marked implemented, covered, satisfied, or equivalent in the acceptance map or token/evidence matrix only when the governed evidence artifacts at the bound canonical paths already exist and the linked validator run, checklist log, or QA primary log actually shows PASS. Planned, expected, or missing future evidence is insufficient.

**No implied scope completion.** Promoting a token to implemented or covered does not by itself promote any separate PF09 task or subtask to complete. When accepted Ops evidence or other governed evidence still shows part of the mapped PF09 scope as unresolved, not yet closed, or not complete, the acceptance artifacts and related closeout surfaces MUST preserve that unresolved status explicitly.

**Binding posture (proof anchors; acceptance artifacts).** In the token/evidence matrix and acceptance maps, tokens MUST bind to the **primary governed artifacts** and the **validator runs/tests** that produce or verify them. Tokens MUST NOT bind directly to `*.path_proof.txt` files as primary evidence surfaces. Path proofs are still required and merge-gating, but they are referenced via the machine mirror record’s `proof_anchor` for the bound artifact and are validated by the evidence index/mirror checks.

**Reuse-first acceptance-ledger binding.**

* If an epic acceptance or close slice depends on already-governed proof families, the acceptance map and token/evidence matrix MUST bind those reused proof families directly.  
    
* Binding only global evidence-skeleton or index-discipline tokens is insufficient when additional in-scope governed proof families materially support the claimed close slice.  
    
* The token/evidence matrix MUST identify the reused primary governed artifacts and the validator runs/tests or QA\_ROOT log anchors that establish each reused token, rather than replacing the reused family with slice-local substitute proofs.  
    
* The viability log MUST count those reused tokens as in scope and MUST NOT report full coverage while omitting them from the acceptance map or token/evidence matrix.

If any required cell is missing at Stage B, the epic is not token-complete and MUST NOT be closed as accepted.

### **9.7.3 Token naming and single-name usage**

Token names are governance artifacts. Plans and proofs MUST consume a single canonical spelling for each token, and MUST NOT mint local synonyms.

* Any token used in an acceptance map, manifest, evidence artifact, epic plan, or epic record MUST use the exact governance spelling from PF04 §2.0. During drainage windows, a newly minted token MAY be referenced only if it has been minted as a numbered addendum in PF10 (Glow HD Engine Build Notes) and the spelling is copied exactly from that addendum, pending drainage into PF04 §2.0.  
    
* Token inventory step (required). Before a plan is finalized, the plan owner MUST inventory every token name used in the plan and verify that each is present in PF04 §2.0 or in an applicable PF10 addendum, and that spelling matches exactly.  
    
* **Planning artifact ownership (Tracked Issues, ADR stubs).** Tracked Issues and ADR stubs are PO-owned planning artifacts. Agents MAY draft suggestions, but the PO is the owner and final maintainer for these artifacts.  
    
* Explicit non-canonical spellings (ban list; normalize on sight). The following spellings MUST NOT appear as claimed tokens in new plans or acceptance artifacts:  
    
  * `AB_BA_PARITY_OK` and `CLI_AB_BA_PARITY_OK` (normalize to `COMPOSITE_ABBA_IDENTITY_OK`).  
      
  * `CLI_READER_EMITTER_PARITY_OK` (normalize to `CLI_READER_PARITY_OK`).  
      
  * `CANON_JSON_OK` (normalize to `JSON_CANONICAL_CHECK_OK`).  
      
  * `CATEGORY_FRAMEWORK_OK` is not a token name. Use `MAGIC10_DOMAIN_CLOSED_OK` (domain closure) or `PREFS_KEYSET_10_OK` (keyset contract), depending on intent.


* Compatibility keyset contract posture. Plans MUST NOT mint a new "compat keyset contract" token. Prove the intent under existing tokens (e.g., `PREFS_KEYSET_10_OK`) and express any extra requirements as obligations or evidence requirements.  
    
* PF14 is not a token registry. Epic-specific guides may choose a spelling during drainage, but the governance spelling wins and all claims must converge on the governance spelling (see §9.7.6).  
    
* If an epic needs a new acceptance token, that need MUST be recorded as an ADR during planning. If approved, the token MUST be minted in PF10 as a numbered addendum before any plan claims it. The token remains canonical in PF10 until it is drained into PF04 §2.0 (Doc-Delta).

### **9.7.4 Blocking status and downgrades (stage-aware; no silent relaxation)**

Stage A and Stage B have different blocking standards. A plan must explicitly mark its stage. Reviewers must not silently relax blockers.

**Stage A — Plan Approval (PRE-IMPLEMENTATION) blockers include:**

* placeholder or non-canonical token names (e.g., “TBD\_TOKEN\_OK”, “SOMETHING\_OK”, “CATEGORY\_FRAMEWORK\_OK”)  
    
* token naming disputes left unresolved: the plan must choose a single token spelling for the epic via ADR, or defer the token  
    
* acceptance claims that are not tokenizable (no token name) or that are not tied to governed evidence  
    
* claiming acceptance or evidence that violates SAFE-rails (e.g., requiring vendor HTTP access for acceptance; claiming evidence from forbidden sources)  
    
* prohibited-character violations in any planning document under review: Unicode ellipsis character (U+2026), or any instance of three consecutive U+002E FULL STOP characters.

**Stage B — QA Ledger Completion (IMPLEMENTED \+ EVIDENCE OK) blockers include:**

* prohibited-character violations in any planning document or QA Ledger artifact under review: Unicode ellipsis character (U+2026), or any instance of three consecutive U+002E FULL STOP characters.  
    
* tokens used in acceptance maps/manifests/evidence that are neither registered in PF04 §2.0 nor minted (with exact spelling) in an applicable PF10 addendum,  
    
* evidence file paths that are not under canonical roots or do not exist  
    
* evidence artifacts that are not mechanically generated (hand-edited evidence)  
    
* token→evidence matrix cells left implicit (“we probably did it”, “it’s in the logs”, “TBD”)  
    
* results that claim “plausibly proven” for any gated token without a governed evidence artifact  
    
* a PR or remediation slice that leaves one or more assigned HDE-Build Checklist subtasks unresolved without an explicit per-subtask explanation that names each affected subtask ID, states exactly what was completed, states exactly what remains incomplete, describes the blocking condition or limiting constraint, explains why completion was not possible within the approved PR scope, and cites the concrete repo-grounded evidence or test result for that conclusion  
    
* silent omission of unresolved assigned subtasks, partial completion without that explanation, or any claim that the PR is complete while assigned subtasks remain unresolved

**Downgrades.** A blocker may only be downgraded if:

* the plan explicitly marks a downgrade rationale, and  
    
* the downgrade does not violate canonical acceptance rails.

Downgrades must be explicit and logged. If a blocker is downgraded due to uncertainty (e.g., a path must be discovered during implementation), the plan must mark an explicit recon step and a re-check gate.

**No silent relaxation.** If a reviewer chooses not to block on a known blocker (e.g., because it is a known-but-accepted deviation), the initial report should say so.

### **9.7.5 PF23 scope waivers (local, non-transitive)**

If the Product Owner or governance chooses to waive or narrow a canon requirement for a particular plan (for example, deciding that PF23 audits are out of scope for a given implementation plan), reviewers MUST:

* record that as a local scope directive (e.g., “PF23 audits are not part of this plan’s workflow”), and  
    
* explicitly state that other rails (PF04/PF19 token governance, evidence rules, epic D-goals, build rails) remain fully in force.

Such PF23 scope waivers MUST NOT be interpreted as permission to relax token naming, acceptance mapping, evidence wiring, or any other canon-backed rails.

### **9.7.6 Re-grounding before asserting “no canonical token name”**

Before any reviewer asserts that “no canonical token name exists yet” for a QA behavior, they MUST:

1. re-check the QA Acceptance Tokens library in Glow QA Guide, and  
     
2. re-read any epic-specific approvals or remediation guides that apply to the epic or defect in question, especially where those documents already chose a token name and semantics for that behavior.

If any such approval or remediation guide defines a token name and semantics for a behavior in scope for the current plan, that spelling is treated as the canonical spelling for this epic’s planning and review purposes. It MUST be used consistently across the plan and any acceptance maps/manifests/evidence authored under the plan, until the naming is drained into PF04 and Glow QA Guide via Doc-Delta.

### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**

Plan acceptance is a governance act. It must not thrash on low-signal edits, and it must not allow token drift.

* **Approval-submission sentinel.** Any planning artifact submitted for approval MUST include the explicit `ASK OK?` approval sentinel. This applies to approval-submitted Epic Plans, Implementation Plans, QA Plans, remediation plans, and other plan-form artifacts that request approval before execution.  
    
  * The presence of `ASK OK?` is required and non-blocking by default for approval-submitted plans.  
  * Reviewers MUST NOT classify `ASK OK?` as stray text, formatting noise, or a blocker merely because it appears in the plan.  
  * Missing the required approval sentinel remains a blocker.  
  * The in-plan `ASK OK?` approval-submission sentinel is distinct from a reviewer response final decision line such as `ASK OK` or `REVISE AND RESUBMIT`.


* **Plans are pointers.** Epic plans are a pointer map, not a full SOP.  
    
* **Token value and budget discipline.** Plans should use only meaningful acceptance tokens. Do not add tokens "just in case."  
    
* **QA planning is post-implementation.** Stage A plans should not attempt to specify the entire QA script. They should specify what must be proven (tokens), and which evidence artifacts will be generated, with pointers to playbooks where relevant.  
    
* **Implementation planning must not require extensive QA evidence.** Epic Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts. These planning artifacts MAY state QA objectives and closeout proof obligations, but they MUST NOT embed a full QA runbook or require that QA evidence be generated as part of implementation planning.  
    
* **QA planning is separate.** QA planning and QA evidence production are owned by the Live QA Plan and QA execution artifacts. The Live QA Plan is where step intents, evidence expectations, and PASS/FAIL posture are specified and where governed QA evidence is produced and indexed.  
    
* **Ops tasks are not QA tasks.** Ops tasks are implementation tasks that change the runtime environment and cannot be performed by code changes alone (for example: service configuration, environment variable changes, secrets management, privileged infrastructure actions). Ops tasks MUST be tracked and evidenced as implementation work, not as QA work.  
    
  * Ops task completion evidence may be required for a feature to function, but it does not satisfy QA verification. QA verification still requires functional proof and the required QA evidence outputs defined in QA planning.


* **Separation rule (no category mixing).** Planning artifacts MUST keep these categories distinct:  
    
  * Implementation work and deliverables (code and implementation changes)  
  * Ops tasks (environment changes)  
  * QA planning (verification plan and evidence posture)  
  * QA execution (functional runs and governed QA evidence)


* **No hidden acceptance.** Plans must not embed ungoverned acceptance claims in prose. All acceptance claims must be surfaced as tokens.  
    
* **No scope laundering.** Plans must not offload difficult decisions to "implementation" while still claiming Stage B acceptance closure.  
    
* **No plan-local token minting.** A plan must not invent new token names or introduce local synonyms. If a new token is needed, it must be minted via the governance process.  
    
* **No "proof by intent."** Plans must not treat "we will test" or "we will validate" as evidence. Plans must name evidence artifacts and where they will live.  
    
* **Retrieval-first, proof-first review posture.** AI reviewers MUST NOT approve, block, downgrade, or assert drift for planning, remediation, QA, repo audit, closeout, or related review artifacts from memory, partial snippets, truncated excerpts, display-layer artifacts, or guessed repo reality.  
    
  * Source order: use PF10 first where it explicitly speaks; then read the current artifact under review end-to-end; then consult the owning PF canon home for each specific issue; then use repo-reality proof for any claimed path, command, endpoint, environment variable, test ID, artifact path, or component home.  
  * Tool order: use full-source retrieval first for uploaded documents and PF artifacts; use container inventory commands next when repo reality matters; use exact-string repo search with fixed-string matching for known IDs, headings, route strings, command strings, filenames, artifact keys, token names, and environment variables; use regex search only when exact-string search cannot prove or disprove the claim; use broader semantic or exploratory search only after exact search fails.  
  * Proof rules: do not rely on truncated viewer snippets or partial excerpts as proof; distinguish canon requirement, observed repo reality, and inference; leave any unproven locus, path, route, command, flag, token spelling, or environment variable as UNKNOWN or BLOCKED rather than guessing; anchor findings to verbatim source text and controlling proof; web lookup is not a substitute for uploaded-file truth or repo-local truth.


* Negative audit proof is valid proof when the reviewed artifact or audit records the claim being negated, the search or check scope, the controlling source or repo locus, the command or retrieval method used, and the observed negative result. Reviewers MUST NOT require a rerun, fallback audit, or substitute proof solely because the proof establishes absence rather than presence. A negative proof remains insufficient only when its scope, source, command, or result does not actually cover the claim, or when it is contradicted by stronger governed evidence.  
    
* **Template adherence is structural only.** For all planning artifacts that use PF templates (including Epic Plans and QA Plans), reviewers MUST evaluate template adherence only for structural completeness: required sections present, required end marker present, and required gates present. Header styling is not part of structural adherence.  
    
  * Header formatting is a Nit. Reviewers MUST NOT request redlines that only change heading levels, add or remove bold or italics in headings, or reformat headings for aesthetic alignment.  
  * This rule does not relax structural requirements, existence-claim citation rules, canon-precedence rules, or QA and evidence obligations. Missing required sections, missing required end markers, missing required canonical pointers where required (including required HDE Build Checklist and HDE Mechanics Guide pointers), invalid non-PF references, or ungrounded existence claims remain valid blockers under the normal gates.  
  * **Business Case section required (Epic Plans).** Epic Plans MUST include a Business Case section that states the product goal and justification in product terms.  
    * Minimum required contents (all MUST be present):  
        
      * Product goal: what ships.  
          
      * Why this work exists: the user pain or opportunity it addresses.  
          
      * Who benefits: the target users and scope.  
          
      * What changes if it ships: concrete user-level outcome.  
          
      * Why now: timing justification.  
          
      * If not done: expected consequence or risk.  
          
      * Non-goals: what will not be done in this epic.

      

    * Content constraints:  
        
      * The Business Case MUST be written in overall Glow product terms. It MUST NOT be replaced by a restatement of implementation tasks, tickets, file-level diffs, or subsystem-only justification.  
          
      * The Business Case is not a marketing pitch or ROI report; it SHOULD remain practical and falsifiable.

      

    * Review posture:  
      * If the Business Case section is missing, empty, or placeholder-only (for example "TBD" or "N/A"), reviewers MUST return the plan for revision and MUST NOT approve it.


* **Non-blocking presentation variance (including heading levels, markup wrappers, and rendered escape characters).** During planning review, presentation-only differences and rendered escape characters MUST NOT be treated as blockers to plan approval when required content, required ordering or adjacency, command identity, artifact identity, path identity, token identity, evidence identity, proof obligation, and meaning remain clear. Reviewers MAY request cosmetic cleanup as non-blocking "Nits" or suggestions only.  
    
  * Examples (non-blocking): bullet marker choice (hyphen vs asterisk), escaped Markdown list markers (for example a leading \* that renders as a bullet), backslashes inserted only for Markdown rendering or escaping, rendered or copied backslash escapes before underscores, redirection symbols, heredoc markers, command punctuation, Python syntax, shell snippets, quotes, parentheses, brackets, asterisks, or emphasis-sensitive text in otherwise recognizable machine-sensitive strings, inline backtick or inline-code wrappers around human-readable planning labels, backticks around PF titles, task IDs, subtask IDs, token names, or short literals used only for human-readable planning text, cosmetic whitespace differences (blank lines, indentation, alignment), bold or italic marker differences that do not change the underlying words, section ordering or adjacency that preserves required content and meaning, and Markdown heading levels.


* **Rendered escape characters are categorically non-blocking in AI review.** Acceptance review MUST NOT impose AI-rendered, markdown-rendered, transcript-rendered, quote-rendered, or assistant-output escape characters as author obligations. A reviewer MUST NOT block approval, request author revision, cite non-runnability, or cite non-portability solely because the reviewer’s rendered view, copied quote, chat transcript, assistant output, or markdown display shows escape characters in a machine-sensitive string.  
    
* **Reviewer burden for escape-related issues.** The burden is on the reviewer to prove a substantive non-rendering defect. If the only visible defect is a backslash or escaped character in rendered review text, the reviewer has not met the burden and MUST NOT emit a blocker. The reviewer MAY ignore the rendered escape layer internally and continue evaluating the actual proof target.  
    
* **Source-level proof requirement for escape-character blockers.** Before any escape-character issue may be treated as a blocker, defect, remediation requirement, acceptance failure, token-spelling failure, quote-verbatim failure, path-proof failure, canonical path failure, PF locator failure, command defect, artifact defect, or governance defect, the reviewer MUST inspect the raw source artifact or governed binding directly. Allowed proof forms include raw repo-file inspection, byte-preserving plain-text read, exact read-only command against the repo file, direct uploaded-source inspection, actual pasted-document inspection after paste, or governed evidence inspection through the governed artifact, Human Evidence Index binding, Machine Mirror record, or path-proof transcript.  
    
* **Default identity posture.** When a path, command, token, artifact key, environment variable, route, endpoint, heading, quote line, filename, PF09 task ID, PF09 subtask ID, ADR ID, JSON key, command argument, config key, or other machine-sensitive string appears with display-layer escape characters in assistant-visible output, the default assumption is that the assistant, markdown renderer, transcript, preview, or copied-review layer introduced the escape. The intended canonical identity remains the unescaped string unless raw source inspection proves otherwise.  
    
* **Required blocker proof.** A valid escape-character blocker MUST identify the raw source file, governed artifact, governed record, pasted document text, or canonical binding inspected; the exact read-only command or source-view method used; the raw line or field that contains the unwanted escape character; why that character changes executable, governed, canonical, or semantic identity; and why the defect is not merely assistant or markdown rendering. Without those elements, the issue is invalid and MUST be withdrawn or downgraded.  
    
* **Quote and redline posture.** IG Approved quotes, CA vetted quotes, PF proof excerpts, Doc A placement lines, Doc B review quotes, redline placement quotes, First line, Last line, Disambiguation line, and proof excerpts MUST be evaluated against raw source text. If the only difference is assistant-rendered escaping, the quote or placement proof is source-equivalent. A redline to remove escape characters is allowed only when the raw target document, raw Doc A source, or raw governed artifact actually contains the unwanted escape character.  
    
* **QA and acceptance classification posture.** QA plans, review artifacts, Live QA results, acceptance maps, token/evidence matrices, closeout reports, PR reviews, implementation plan reviews, and Codex prompts MUST NOT classify display-layer escape artifacts as `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, or closeout blocker. If raw source verification proves a substantive defect, classify the real underlying issue, not the display rendering.  
    
* **Codex prompt posture.** Codex prompts MUST treat escaped display text as non-authoritative unless the escaped text is inside a raw source file that Codex opens. Codex MUST NOT create alternate escaped paths or filenames, rename paths, remediate paths, or fix commands solely because assistant-rendered prompt text displayed backslashes.  
    
* **Reviewer self-check before escape-related issues.** Before issuing any issue that mentions escaped characters, backslashes, markdown escaping, rendered paths, rendered shell syntax, or rendered code syntax, the reviewer MUST remove the apparent rendering escapes mentally, re-read the command, path, token, artifact identity, or proof obligation, and ask whether the issue would still be a blocker if the escape characters vanished. If not, the reviewer MUST NOT emit the issue.  
    
* **Author obligation limit.** If the command identity, artifact identity, path identity, token identity, evidence identity, and proof obligation are clear after ignoring rendered escapes, the plan passes that review dimension. Reviewers MUST NOT ask the Product Owner or plan author to revise rendered escape characters, and MUST NOT use them as evidence of non-runnability, non-portability, or invalid proof posture.  
    
* **Substantive defects remain blocking.** This posture does not allow broken plans to pass. A blocker remains valid when the substantive issue is independent of rendering escapes and concerns missing or ambiguous command identity, an unproven repo locus, a missing required deliverable, a missing PASS or FAIL criterion, a required non-attached non-PF source, contradiction with PF10 or controlling PF canon, assignment of QA execution where only planning is allowed, unsafe public-surface or provider-rails posture, or a proof target that remains unclear after ignoring rendered escapes.  
    
* **Formatting exceptions (still blocking).** This non-blocking posture does not apply to formatting or text that changes meaning, hides required content, breaks execution, prevents verification, violates prohibited-character rules (see §9.7.4), or affects any of the following:  
    
  * Missing or incorrect required fields, required section order, required adjacency, PF09.x documents, task IDs, subtask IDs, PF14 references, dispositions, token spellings, path strings, endpoint strings, command strings, schemas, JSON, or code.  
  * Commands or code expressly required by an owning contract to run as written, when the defect changes command identity, proof target, artifact family, PASS/FAIL predicate, or intended output.  
  * Evidence outputs, filenames, or required lowercase ASCII paths.  
  * Portability rules (for example references to external attachments).  
  * Quoted-carryover blocks that must be verbatim (for example “IG Approved” or “CA vetted” quote lines).  
  * Any statement of obligation (MUST/SHOULD) or acceptance posture.


* **Template-hygiene materiality rule.** A planning artifact, implementation plan, QA plan, remediation guide, review artifact, or closeout planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table order, section phrasing, path labels used only for planning, titles-only polish, or section-locator precision unless the defect materially changes source-of-truth authority, implementation scope, PF09 completion mapping, acceptance-token truth, evidence identity, evidence trust, Codex portability, OPS/PR boundary, execution safety, public/private surface posture, canon conflict handling, or closeout truth.  
    
* **Acceptance-token review materiality.** Missing token-inventory rows should be corrected, but they are blockers only when they create token overclaim, missing acceptance truth, unregistered token usage, canonical token-spelling drift, or a missing governed evidence obligation. A missing token row is not a blocker by itself when the plan does not overclaim the token and the relevant evidence family is otherwise scoped.  
    
* **Valid blocker classes remain material.** The following remain blockers when proven: contradiction with active PF10 guidance; an ADR left open after PF10 resolves the exact topic; routing a topic to a new PF10 addendum when an applicable PF10 addendum already exists; claiming an unregistered token as an acceptance token; marking work Already Implemented without embedded proof or an allowed proof form; requiring Codex to consult CA, audit files, attachments, chat history, implementation guides, or other non-PF sources; requiring OPS work inside Codex PR work; asserting an existing repo locus without allowed proof or discovery-first posture; creating or widening public surface scope without canon support; making PF23 a deliverable, token source, blocker source, or acceptance authority; or using PF20 as current planning, token, evidence, acceptance, rails, or required-now authority.  
    
* **Epic Plan review boundary.** Epic Plans are planning records. They are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Plan review should not block on QA-runbook-level precision, close-pack-level evidence path completeness, or template inventory polish unless the prompt or PF canon explicitly makes that information necessary for current planning truth.  
    
* **Implementation Plan review boundary.** Implementation Plans must be more concrete than Epic Plans, but formatting defects are not blockers unless they create real Codex or OPS ambiguity. If a plan tells Codex to consult CA or an audit, that is a blocker. If the plan embeds the needed fact and Codex can proceed without external documents, CA or audit provenance wording is not a blocker. If an Already Implemented claim relies on CA, the plan should embed enough proof in the plan itself. Imperfect CA quote-block formatting is not a blocker when the fact is clear, self-contained, and not used to smuggle in requirements.  
    
* **Audit provenance planning-context boundary.** Audit provenance may appear in Epic Plans, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives as planning context, risk context, discovery context, source-trace context, rationale for a Tracked Issue or ADR stub, rationale for a workstream, rationale for a QA proof obligation, rationale for a repo-validation check, or rationale for PF-canon drainage. A reviewer MUST NOT block an artifact solely because it includes audit provenance in that contextual role.  
    
* **Audit provenance is not authority by itself.** Audit provenance MUST NOT be converted into PR instructions, OPS instructions, step-by-step execution procedure, Codex command source, privileged-action authority, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth, required deliverable authority, source of invented file or path existence, source of secrets, or source of external-state truth. If audit provenance points to current repo reality, the current repo claim must be validated by the allowed repo-validation route before it is used as current fact.  
    
* **Review burden for audit provenance blockers.** A blocker is valid only when the artifact uses audit provenance as execution authority or proof authority, requires Codex or OPS to consult the audit itself, or relies on the audit as current repo proof without validation. If the audit only explains why work exists, what risk was observed, what should be inspected, or why a proof is planned, the correct classification is no issue, note, context accepted, planning provenance accepted, repo validation required before execution, or keep out of PR/OPS instruction text.  
    
* **Plans are approval artifacts, not execution artifacts.** QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, and closure-review artifacts MUST NOT be blocked, rejected, returned for revision, or classified as `REVISE AND RESUBMIT` because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written. This applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly. Plans are approved on truth, proof, scope, authority, safety, acceptance posture, phase fidelity, and evidence identity. Plans are not blocked on syntax.  
    
* **Severity mapping and review burden.** `Blocker` is reserved for issues that change truth, proof, acceptance, execution, source authority, portability, evidence trust, scope, or closeout truth. `Caveat` means a real risk with a safe default that does not prevent approval. `Suggestion` means clarity, consistency, or maintainability improvement. `Nit` means cosmetic, template-polish, or wording-level only. A reviewer who blocks approval MUST state the non-syntax material harm.  
    
* **Truth/proof blockers only.** Valid approval blockers remain limited to material truth, authority, scope, evidence, safety, phase, acceptance, public/private boundary, OPS/QA/PR category separation, PF09 completion mapping, source-of-truth, token, canon-conflict, required-proof, or evidence-identity defects. Missing proof obligation, missing in-scope PF09 mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement under closed rails, secret exposure requirement, OPS work assigned to Codex, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, or unclear PASS/FAIL posture remain valid blockers when proven. They are not syntax issues.  
    
* **PF09 accountability for task-like future work.** Backlog, future, deferred, optional, follow-up, remediation, runtime-gap, adapter-gap, vendor-gap, QA-discovered, OPS-discovered, evidence-gap, build-improvement, and later-work labels are scheduling or disposition labels only. They do not remove PF09 accountability when the item is task-like and affects implementation, QA, OPS, runtime behavior, evidence behavior, vendor behavior, architecture behavior, or product behavior.  
    
* **Required task-like item classification.** A plan, remediation guide, QA-readiness review, retrospective, closeout review, or future-work section that contains a task-like item MUST classify it as one of: mapped to an exact phased PF09 task or subtask, PF09 gap, out of HDE phased build scope, or documentation/status drainage only. If a relevant PF09 parent and subtask both exist, subtask-level mapping is required. Parent-task-only mapping is insufficient when a relevant subtask exists.  
    
* **Token and acceptance posture do not substitute for PF09 mapping.** Acceptance-token posture, evidence availability, QA PASS, OPS evidence, PF10 supportability notes, board status, closeout recommendations, or documentation-drainage status MUST NOT be used as a substitute for exact PF09 task or subtask mapping where PF09 accountability is required. A reviewer may block an artifact that creates unaccounted task-like backlog when the item affects implementation, QA, OPS, runtime, evidence, vendor, architecture, or product behavior and is not mapped, marked PF09 gap, classified out of phased build scope, or classified documentation/status drainage only.  
    
* **Syntax, paste-readiness, and helper-code concerns are non-blocking.** Command exactness, paste-readiness, literal executability, shell syntax, Python syntax, heredoc form, helper-code syntax, helper-code formatting, interpreter invocation, code-block formatting, quote formatting, wrapping, whitespace, punctuation, copied command exactness, non-literal examples, assistant-introduced syntax artifacts, renderer-introduced syntax artifacts, and formatting introduced during review, redline, or paste workflows MUST NOT be classified as `Blocker`, approval blocker, QA readiness blocker, implementation readiness blocker, closure blocker, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, acceptance failure, path-proof failure, evidence failure, token failure, PF locator failure, or command-validity failure requiring plan revision.  
    
* **Allowed syntax severity classes.** For any plan artifact, command/syntax concerns may be classified only as `Non-issue`, `Note`, `In-flight normalization`, or `Operator caution` unless the reviewer identifies a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, canon-conflict, or evidence-identity defect.  
    
* **QA step literalness rule.** QA steps do not need to be paste-ready, literal executable commands, final runnable syntax, or exact shell, Python, or tool syntax. QA steps may express the intended proof action in operational language, pseudocode, structured prose, or approximate command form, provided the proof target, scope boundary, rails or boundary posture, and expected kind of verification are clear. A QA Plan is not disqualified because a command block needs in-flight normalization during execution.  
    
* **In-flight normalization rule.** Syntax correction is ordinary execution hygiene. If a QA operator, Codex, Kronos, Product Owner, or implementation owner encounters a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue during execution, they may normalize it in flight as long as they preserve the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture. In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, or authority actually changes.  
    
* **Live QA Plan approval is operational-readiness review.** A Live QA Plan should be approved when it is safe, self-contained, phase-bounded, and clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict. Reviewers MUST NOT treat Live QA Plan approval as byte-perfect command lint, template-polish review, closeout-time evidence-byte validation, or literal command-transcript review.  
    
* **Live QA Plan approval blockers are operational only.** A Live QA Plan approval Blocker is valid only when the issue affects safe execution, required QA step coverage, required deliverable existence, explicit PASS or FAIL verdictability, rails posture, secret handling, live-provider or external-action boundary, public/private surface boundary, token truth, acceptance overclaim, source authority, self-contained execution, evidence trust, proof target identity, repo-locus truth where the plan requires an existing locus, OPS/QA/implementation category separation, phase scope, or closeout truth.  
    
* **Non-blocking Live QA Plan approval issues.** Rendered escape characters, markdown or AI-rendered backslashes, heading style, bullet style, table style, quote-block formatting, code-block formatting, whitespace, punctuation, line wrapping, command syntax polish, command invocation style, interpreter choice that does not change operational behavior, exact shell spelling, exact command ordering that is not required for safety or proof, evidence-ledger byte-shape polish, path-proof transcript field polish, canonical JSON compactness wording, and step-log header polish are Caveats, Suggestions, Nits, notes, operator cautions, or in-flight normalization items unless they create a real operational defect.  
    
* **Command posture for Live QA Plan approval.** Commands in a Live QA Plan are operational instructions, not canon contracts, unless the plan explicitly states that a command is an exact required invocation and the owning PF home requires exactness for the operational result. Exact-command mismatch is a Blocker only when it would likely run the wrong tool, prove the wrong target, open unsafe rails, expose secrets, mutate prohibited state, prevent the check from running, or create a false PASS or false FAIL with no safe fallback. Otherwise, exact-command mismatch belongs in Caveats, Suggestions, execution notes, operator cautions, or in-flight normalization notes. The actual command used during QA execution MUST be captured in the QA evidence.  
    
* **QA-created harness posture.** A Live QA Plan MAY create QA-only harness scaffolding during Step 0 when the harness is limited to QA evidence capture and does not create product behavior. Reviewers MUST NOT require repo-existence proof for a QA-created harness that the plan explicitly creates during the QA run. A QA-created harness issue is a Blocker only when the creation instructions are not executable enough to create the harness, the harness would perform unsafe or out-of-scope work, the harness changes implementation behavior, the harness proves the wrong target, the harness cannot emit a verdict, or the harness cannot produce or point to required governed evidence.  
    
* **Evidence identity at approval.** Live QA Plan approval requires evidence identity, not final closeout perfection. At approval time, the plan must identify what each check proves, what result counts as PASS, what result counts as FAIL, where the QA run records the decisive receipt, which evidence family or evidence class supports the verdict, and how token claims are avoided unless registered and in scope. Final byte-level details of canonical JSON compactness, field ordering, path-proof transcript shape, step-log header shape, mirror-record shape, and final evidence-index refresh mechanics may still fail QA execution or closeout validation, but they are approval blockers only when the plan lacks evidence identity, lacks a decisive receipt, relies on ungoverned evidence as decisive proof, or explicitly rejects required governed-evidence discipline.  
    
* **Live QA Plan review burden.** A reviewer who blocks a Live QA Plan MUST state the operational harm. Invalid blocker framing includes objections that only say the command is not paste-ready, the heredoc syntax is wrong, the Python indentation is wrong, the shell line would not run exactly as written, the command includes escaped hyphens or escaped redirection, the markdown escaped the command, the helper code is syntactically invalid, the code block would need cleanup before running, the example command is not exact, the tool invocation style should be different, the command should use another interpreter, the plan has command syntax defects, the plan has source-byte escape defects, the plan is not executable as pasted, the QA-created helper needs formatting normalization, or the reviewer can prove the raw text has escape characters. These findings may be recorded as execution notes, operator cautions, or in-flight normalization notes only, unless a separate non-syntax truth/proof defect is proven.  
    
* **Evidence-bound QA steps (Live QA Plans).** Every required acceptance token MUST have at least one explicit QA step that produces evidence for that token, and each QA step MUST either map to a required token or be explicitly labeled as non-blocking informational only.  
    
* **Prefer standard playbooks.** Where a suitable QA playbook exists in the Glow QA Guide (PF19), Live QA Plans SHOULD reuse it. Novel steps SHOULD be proposed for inclusion rather than remaining one-off.  
    
* **Acceptance criteria must be tokenized.** Acceptance claims in plans MUST be expressed using governance token names (PF04 §2.0 and, when applicable, newly minted PF10 addenda tokens). Freeform acceptance language is not a substitute for token claims.

### **9.7.8 Evidence bundle cross-check for local-bundle deliverables**

When a deliverable claims a **local bundle** of governed artifacts under a specific directory (example: `artifacts/ops/internal_version/*`), the Epic Plan **MUST** explicitly state:

* the complete required bundle paths (titles-only, full paths, no byte restatement), sourced from the canonical bundle definition, and  
    
* any shared/global governed artifacts required for acceptance (example: determinism env pins), including their canonical paths, when they do not live under the local bundle root.

**No implicit dependencies.** If any required evidence lives outside the deliverable’s local bundle directory, the plan MUST name that evidence explicitly and give its canonical path.

**Titles-only references allowed, but completeness remains required.** If the plan references a canonical bundle definition section by title instead of listing all paths, it MUST still list:

* any overrides, exclusions, or additions, and  
    
* any shared/global evidence required outside the local bundle root.

**Consistency requirement.** The token\_evidence\_matrix, Evidence Index, machine mirror, and path-proofs MUST reflect the same canonical paths for any evidence referenced by acceptance.

### **9.7.9 Canonical evidence-path binding validation (acceptance integrity)**

**Plan locus validation (paths, roots, module loci).**

* Plans and planning reviews MUST NOT fabricate repo file paths, directory roots, or module loci.  
    
* Every asserted file path or “where this lives” claim in a plan MUST be validated using exactly one method:  
    
  * **Canon-cited (preferred):** a direct citation to PF canon that defines the home or locus.  
      
  * **CA vetted:** an inline verbatim quote from the planning Codex audit that supports the asserted locus.  
      
  * **IG Approved:** an inline verbatim quote from an Implementation Guide that supports the asserted locus.


* If the plan uses “CA vetted” or “IG Approved”, the supporting material MUST be quoted verbatim. Paraphrase is not permitted for these labels.  
    
* Mandatory consult set (before asserting roots or loci): HDE Architecture and Reality Audits.  
    
  * Plans MUST align placement decisions to Architecture single-home constraints and repo reality, and MUST NOT introduce alternate roots by assumption (for example, a “src/” tree).


* Planning Codex audit posture:  
    
  * Each planning session begins with a planning Codex audit (performed once at the start). Findings MAY be referenced inside planning documents as “CA vetted” only when accompanied by an inline verbatim quote.  
      
  * The planning audit MUST NOT be referenced in final instructions given to Codex for implementation.  
      
  * Codex execution prompts MUST be self-contained and MUST NOT reference “CA vetted”, “IG Approved”, the planning audit, or any attachments. Execution prompts MUST rely only on PF canon references and repo paths.


* File and directory minting posture:  
    
  * Minting new files under existing canon-established homes is normal and expected when required by the Epic scope, provided the home is validated (Canon-cited, CA vetted, or IG Approved).  
      
  * New top-level roots and second homes are prohibited by default. A plan MUST NOT propose a new surface root unless it includes: (1) an Architecture-aligned justification, (2) a CA vetted quote that supports the absence of an appropriate existing canonical home, (3) an explicit statement of why existing canonical homes cannot be used, and (4) an explicit ADR (or explicit waiver) approving the new root, with justification and an accountable owner.  
      
  * If a plan proposes a new file path, the plan MUST state that the file is new and include an absence-proof check that demonstrates the path did not previously exist (or explicitly declares intentional overwrite) with an explicit PASS/FAIL predicate.


* Evidence output naming (clarity without clutter):  
    
  * Plans MUST name the primary governed evidence outputs that will be committed and indexed (exact paths and filenames), and MUST avoid wildcards or vague “family” phrases.  
      
  * For high-churn evidence families, plans MAY treat a deterministic manifest or bundle as the primary governed artifact if it enumerates its member logs deterministically; the manifest or bundle path MUST be named explicitly and governed as the decisive output.


* Review gate: any unvalidated asserted path, root, or module locus is a mechanical planning-review blocker until corrected to one of the permitted validation methods above.

**Incident record (informative).** A prior plan in this scope asserted a “src/” surface root for HTTP, adapter, and presenter placement. This is severe canon drift. Plans MUST treat `adapter/` as the single HTTP home per Architecture and must derive concrete loci via Canon-cited or CA vetted validation, not invented roots.

**No fabricated required paths (canon-proof or explicit creation only).**  
A plan MUST NOT reference any file path as **required** unless one of the following is true:

1. **Canon-defined:** the path (or path pattern) is explicitly defined by PF canon, or  
     
2. **Audit-proven:** the path’s existence is proven by an existing canon-recognized audit artifact family (for example: a governed manifest, an Evidence Index/mirror entry, or a canonized proof transcript family), or  
     
3. **QA-created:** the plan includes inline, explicit creation instructions and validation for the path (exact `mkdir` \+ write instructions with no placeholders, a one-line purpose, and explicit PASS/FAIL predicates tied to the file contents).

**Proven or created, otherwise forbidden.** If a path is neither canon-defined nor audit-proven, it MUST be QA-created under rule (3) or it MUST NOT appear as required in the plan.

**QA write scope (hard).** QA-created folders/files may be written only under `audit/**` or `artifacts/**`. Any instruction that implies writing outside `audit/**` or `artifacts/**` is non-conforming.

**Separate pre-existing vs QA-run artifacts (hard).** Plans MUST separate pre-existing artifacts (expected before execution) from QA-run artifacts (created during execution). Preflight presence checks MUST gate only on pre-existing artifacts. A QA-run artifact MUST NOT be required in preflight unless the plan creates it within that same preflight step.

**Non-PF guidance is not a path authority.** QA guides and other non-PF documents may describe intent, but they MUST NOT be treated as canonical sources for required file path existence or naming. For plan-time locus support, the only permitted non-PF mechanism is an inline verbatim quote labeled “CA vetted” (planning Codex audit output) or “IG Approved” (Implementation Guide). Any path supported by non-PF material still MUST be reconciled to PF canon single homes or be explicitly created under rule (3) before it can be treated as required.

**Evidence-path authority order (path-of-record resolution; deterministic).**  
When two or more surfaces imply different canonical paths for the same evidence artifact family (or when path proofs block due to ambiguity), resolve the canonical required path using this authority order (highest wins):

1. **Repo manifests** — machine-readable, version-controlled manifest surfaces that define canonical paths (for example, the Freeze-Pack Manifest SoT `catalog/manifest.json`, and other manifest-style SoT surfaces defined in PF canon).  
     
2. **Audit manifests** — governed manifests written under `audit/**` during QA/closeout (for example, `audit/EPIC-###_MANIFEST.json` and `audit/qa/<epic-id>/qa_step_logs_manifest.json`).  
     
3. **Rendered reports** — human-readable narrative reports derived from manifests/evidence (for example, the close report).  
     
4. **QA Plan text** — plan step prose and pointers (lowest authority; must be updated to match higher tiers).

This authority order determines the path-of-record; it does **not** permit requiring paths that are otherwise forbidden by the rules in this section (canon-defined, audit-proven, or QA-created).

**Blocking posture (no “dual-home” acceptance).**  
If authority-order resolution changes a path referenced by the plan (or reveals a plan-required path is wrong/ambiguous), the result is plan drift and MUST be handled explicitly (Doc-Delta, plan update, or remediation). Reviewers MUST NOT “average” sources, accept ambiguous dual-home binding, or treat rendered reports / plan prose as overrides for manifest-defined canonical paths.

**New artifact families (recurring).** If a new recurring artifact family/path is genuinely needed for future QA, it MUST be introduced via a Build Notes addendum (or the owning PF canon home) and drained into the owning PF document before plans may require it.

**Canonical JSON gate directory (single home; no dual-home binding).**

Canonical governed artifact family (fixed paths):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
    
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
    
* `audit/gates/json_gate/canonical/json_gate_structured_record.json`  
    
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`  
    
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`  
    
* `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`

Canonical runner entrypoint (Live QA / CI; do not invent alternate runner paths):

* `python tools/evidence/run_canonical_json_gate.py`

Live QA binding note (example check id: `D02_canonical_json_gate`). When this gate is exercised as a Live QA check, plan-level PASS predicates may bind to runner exit code `0` \+ the governed canonical-json artifacts above \+ the per-check primary log under QA root (for example `audit/qa/<epic-id>/checks/D02_canonical_json_gate/primary.log`) recording a header `status:"PASS"`.

Conjunction CLI targets (canonical JSON gate coverage; required when present):

* The canonical JSON gate target list and comparisons MUST include conjunction-related CLI artifacts (including BA variants where applicable) when they are part of the governed evidence surface for the build.  
    
* Conjunction-related artifact paths surfaced in this build note series include:  
    
  * `artifacts/audit/cli/pair.json` and `artifacts/audit/cli/pair_ba.json`  
      
  * `artifacts/audit/cli/showcompat_ab.json` and `artifacts/audit/cli/showcompat_ba.json`  
      
  * `artifacts/cli/out.json` and `artifacts/cli/out_ba.json`  
      
  * `artifacts/cli/abba_sidecar.json`


* Evidence Index keys for this family include: `cli.conjunction.pair_ab`, `cli.conjunction.pair_ba`, `cli.conjunction.showcompat_ab`, `cli.conjunction.showcompat_ba`, `cli.conjunction.output_ab`, `cli.conjunction.output_ba`. The Evidence Index remains authoritative for the exact key set and path mapping.  
    
* Each artifact above MUST have a co-located `.path_proof.txt` transcript and MUST satisfy `EVIDENCE_PATH_PROOFS_OK` and `EVIDENCE_PATHS_VALIDATED_OK`.

Legacy naming (do not require in Live QA plans):

* `audit/gates/canonical_json/json_canonical_check.log` is a legacy catalog-check report path preserved for backward compatibility; it MUST NOT be required by Live QA Plans and MUST NOT be treated as the canonical gate-family output (use `audit/gates/json_gate/canonical/`).  
    
* `audit/gates/canonical_json/canonical_json.gate.json` and `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt` are legacy-named supplemental summaries. They MAY be produced, indexed, and path-proved, but MUST NOT be used as the plan-binding gate-family output. Live QA plans MUST NOT require this legacy family unless canon explicitly reinstates it via PF12.  
    
* `audit/gates/canonical/` remains legacy/compat-only; do not create new canonical outputs there.

Minimum canonical artifact set (fixed filenames):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
    
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
    
* `audit/gates/json_gate/canonical/json_gate_structured_record.json`

Path proofs (required; sibling; fixed naming):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`  
    
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`  
    
* `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`

Canonical runner entrypoint (Live QA / CI; do not invent alternate runner paths):

* `python tools/evidence/run_canonical_json_gate.py`

Live QA binding note (example check id: `D02_canonical_json_gate`). When this gate is exercised as a Live QA check, the plan-level PASS predicates may bind to:

* runner exit code `0`, and  
    
* the governed gate log at `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, and  
    
* the per-check primary log under QA root (for example `audit/qa/<epic-id>/checks/D02_canonical_json_gate/primary.log`) recording a header `status:"PASS"`.

Legacy naming (do not require in Live QA plans):

* `audit/gates/canonical_json/json_canonical_check.log` is a legacy catalog-check report path preserved for backward compatibility; it MUST NOT be required by Live QA Plans and MUST NOT be treated as the canonical gate-family output (use `audit/gates/json_gate/canonical/`).  
    
* `audit/gates/canonical_json/canonical_json.gate.json` and `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt` are legacy/non-authoritative naming and MUST NOT be required by Live QA Plans unless canon explicitly reinstates this naming via PF12.  
    
* `audit/gates/canonical/` remains legacy/compat-only; do not create new canonical outputs there.

**Determinism env pins gate (single home; plan path authority).**

Canonical governed artifact set (fixed filenames):

* `audit/gates/determinism/env_pins.log`  
    
* `audit/gates/determinism/env_pins.log.path_proof.txt`

Canonical runner entrypoint (Live QA / CI; do not invent alternate runner paths):

* `python tools/evidence/run_env_pins_gate.py`

Observed baseline implementation (allowed):

* `ci/checks/check_env_pins.sh` (invoked under closed rails; see `DETERMINISM_ENV_PINS_OK`)

Live QA binding note (example check id: `D01_env_pins_gate`). When this gate is exercised as a Live QA check, plan-level PASS predicates may bind to runner exit code `0` \+ the governed env-pins artifacts above \+ the per-check primary log under QA root recording a header `status:"PASS"`.

**Showcompat artifacts (single home; plan path authority).**

Canonical artifact family (epic-scoped directory; fixed filenames):

* `artifacts/showcompat/<epic-id>/showcompat_manifest.json`  
    
* `artifacts/showcompat/<epic-id>/showcompat_symbols.json`

Path proofs (recommended; required when used as acceptance-bound evidence):

* `artifacts/showcompat/<epic-id>/showcompat_manifest.json.path_proof.txt`  
    
* `artifacts/showcompat/<epic-id>/showcompat_symbols.json.path_proof.txt`

Canonical runner entrypoint (Live QA / CI; do not invent alternate runner paths):

* `python tools/evidence/run_showcompat_artifacts.py`

**Rails posture for functional showcompat QA (vendor seam; required until local BodyGraph storage exists).**  
Current limitation: Live QA cannot rely on precomputed BodyGraph inputs being locally available for showcompat runs. If BodyGraph data is not already available, showcompat requires vendor-sourced BodyGraph acquisition to compute compatibility.  
Any Live QA step that executes showcompat in this state MUST run that step with vendor rails open (open network rails) so the vendor can be called. Closed rails must be treated as an expected `BLOCKED` outcome for functional showcompat runs under this limitation. The rails change MUST be explicit and scoped to only the showcompat step(s). After the step, restore the default rails posture.

**Arguments required (no zero-arg invocation).**  
showcompat MUST NOT be executed as a zero-argument command in QA plans or QA runs. Required arguments are defined in **HDE-CLI-API-Vendor-Ref**.

**Conjunction mode (showcompat \--conjunction).**  
showcompat conjunction mode MUST be treated as a read-only compatibility check for two parties. It MUST NOT write or mutate stored user state.

* **Inputs (both parties required).** Conjunction mode MUST be provided two parties via one supported input form (as defined by the CLI contract):  
    
  * `--user-a <id>` and `--user-b <id>`  
      
  * `--pair-file <path>` (pair JSON)  
      
  * `--a-file <path>` and `--b-file <path>` (sidecar JSON)  
      
  * stdin payload containing both parties in left/right form


* **Deterministic failure contract.** Missing or invalid inputs MUST fail deterministically with stable error code semantics (for example `INVALID_ARGUMENT`), MUST write the diagnostic to stderr, and MUST emit empty stdout.  
    
* **SAFE rails contract (closed rails).** Under closed rails, conjunction mode MUST NOT attempt vendor acquisition. If `--source vendor` or `--source auto` would require vendor data and the required BodyGraphs are not locally available, it MUST deterministically refuse with error code `PROVIDER_REFUSED`, MUST emit empty stdout, and MUST NOT create partial outputs. When this refusal occurs, classify the run as BLOCKED per the rule below.  
    
* **Open-rails posture.** Under open rails, conjunction mode MAY access vendor data as defined by the CLI contract, but governed JSON outputs (when emitted as governed artifacts) MUST remain deterministic and canonicalized.

**QA classification and evidence posture.**  
If showcompat is attempted under closed rails or without required arguments, classify the outcome as a tooling/environment or usage defect for that step, not a product behavior failure. Record the rails posture used (names-only) and the failure signature in the step log.

**Future posture.**  
Once local BodyGraph storage and replay exists and showcompat can be provided BodyGraph inputs without vendor calls, Live QA may exercise showcompat under closed rails for determinism proofs.

Live QA binding note (example check id: `D03_showcompat_artifacts`). When exercised as a Live QA check, plan-level PASS predicates may bind to runner exit code `0` \+ existence/non-emptiness of the two artifacts above \+ the per-check primary log under QA root recording a header `status:"PASS"`.

**Arrays-as-sets drift report (single home; plan path authority).**

Canonical report artifact (stable surface):

* `artifacts/canonical/arrays_as_sets_report.log`

Observed runner (Live QA; accepted command surface):

* `python -m pytest tests/compare/test_arrays_as_sets.py`

Non-canonical plan naming (do not require unless canon explicitly reinstates):

* `python tools/evidence/run_arrays_as_sets_check.py` (reported “File not found” in observed execution)  
    
* `audit/gates/arrays_as_sets/arrays_as_sets_report.md` (reported missing; actual report surface is under `artifacts/canonical/`)

**Indexing discipline (when used for acceptance).** If an epic’s acceptance artifacts bind to this report as decisive evidence, the artifact MUST follow the standard evidence skeleton discipline (co-located `*.path_proof.txt` \+ Evidence Index \+ machine mirror updates in the same PR as any byte change)

### 9.7.10 Token roster validation (preflight) and no midflight additions

**Token roster validation (acceptance-claim gate; not a Live QA plan-approval blocker by default).**  
Token name validation is case- and spelling-exact. Aliases and near-matches are not permitted.

**What must validate (when present).**  
Any token name that appears in:

* the plan’s acceptance roster (Stage A, if present), and  
    
* the token/evidence matrix (Stage B, when present), and  
    
* any epic record acceptance roster that the plan is claiming against (titles-only), and  
    
* any step log / close artifact that claims a token,

MUST be validated against the canonical Token Registry in §2.0.

**Live QA planning posture (token load reduction).**  
Live QA plans MUST NOT require per-step token claims and MUST NOT require a full token roster in the plan body as a prerequisite for approval. Tokens are an optional indexing layer for QA execution. Token roster drift discovered during planning is recorded as a `CAVEAT:` item (see §9.8) and is not a plan-approval blocker unless token validity is required to determine pass/fail for a specific check.

**Unregistered acceptance token (canon gap; bridge posture).**  
If an epic acceptance roster references a token name that is not present in §2.0, classify it as `UNREGISTERED_ACCEPTANCE_TOKEN` for that epic until drained. Live QA evidence collection may proceed for behavior verification, but:

* the plan MUST NOT claim that token in step logs, matrices, acceptance maps, or close-pack checks, and  
    
* the plan MUST record the gap in the plan’s Doc-Delta Capture output as a blocking canon gap (no substitution/renaming).

**Mechanical blocker (token claims).**  
If any token is claimed in the plan’s matrix, acceptance artifacts, or step logs and is not present in the canonical Token Registry, that claim is mechanically invalid for acceptance and MUST be corrected. Reviewers must not “interpret” intent.

**Review source-retrieval guard (no excerpt-based claims).**  
A reviewer MUST NOT assert token roster drift (missing/wrong token names or token semantics mismatch) unless they have retrieved the full epic acceptance roster section and the relevant Token Registry entries for the tokens in question.

**No midflight token invention.**  
During an Epic planning revise/resubmit loop, the plan MUST NOT introduce new **acceptance tokens** (in-scope gating tokens) unless:

1. explicitly requested by Lead review, or  
     
2. required due to a clearly identified canon gap.

Default posture when a behavior must be enforced but no token exists: state it as a **non-token mechanical requirement** under the deliverable and prove it via tests/evidence, rather than tokenizing it.

**If a new token is genuinely required, it must be routed, not invented.**  
A plan may propose a new token only when all of the following are true:

* An ADR is present in the plan’s ADR list stating: token name, one-sentence semantics, intended evidence surface(s), and drain targets.  
    
* The ADR is a canon-resolution instrument (not a restatement or commentary). If the topic is already canonized (e.g., PF10 or an owning PF-Canon home), the ADR MUST be removed and the Plan/Remediation MUST cite the canon directly.  
    
* The ADR MUST NOT cite HDE-Phased Epics as the authority for token semantics, evidence surfaces/path proofs, or QA log schema/validator requirements.  
    
* A conflict check is performed against existing canonical tokens (no duplicates, synonyms, or near matches).  
    
* The token is registered via Doc-Delta in §2.0 before it can be required as an acceptance claim (i.e., before it can appear as an in-scope gating token). Until then, it must be treated as deferred or as a request, not as a claimed acceptance token.

### **9.7.11 Acceptance artifact hygiene (no placeholders; no duplicate rows)**

This subsection governs the **acceptance artifacts** themselves (acceptance maps and token/evidence matrices), independent of whether the Epic Plan embeds them (it must not; see §9.7.2).

**PF23 consult representation (non-token).**  
PF23 consult MUST NOT be represented as an acceptance token (forbid `REALITY_AUDIT_OK`). PF23 consult is planning-time trace only: Live QA Plans and Live QA execution MUST NOT require or produce PF23 consult artifacts under QA\_ROOT (including `audit/qa/<epic-id>/00_meta/pf23_consult.md`). If a trace anchor is desired, include a names-only “PF23 Anchors” list in the plan body (no operator commands; no required Deliverables).

**No placeholders once evidence exists (Stage B).**  
When a token is **in-scope (gating)** for an epic (Stage B readiness), the acceptance artifacts MUST NOT contain placeholder evidence references. Treat any of the following as placeholders and therefore non-conforming for in-scope tokens:

* `"TBD"`, `"pending"`, `"PR1 scaffold"`, `"{}"` (or empty object markers)  
    
* template variables such as `{scenario}` or any other pattern that is not a concrete path or artifact key  
    
* implicit “it exists somewhere” references without explicit paths

For in-scope tokens, evidence lists MUST contain only **concrete, repo-relative paths** (and, where applicable, the canonical `artifact_key` bindings governed by HDE-Schemas & Artifacts).

**Uniqueness (single-authoritative rows).**  
Each acceptance token name MUST appear **at most once** in:

* the token/evidence matrix for the epic, and  
    
* the acceptance map for the epic.

Duplicate rows for the same token are a mechanical blocker because they create ambiguity about which row governs closeout.

**CI-safe guard posture (allowed).**  
It is permitted (and recommended) to enforce these rules with CI-safe scaffold tests that assert:

* token names are unique in each acceptance artifact, and  
    
* in-scope tokens have no placeholders and point only to concrete artifacts that exist on disk.

**Planning posture — mandatory Reality Audits consult (components \+ pathnames).**  
This rule applies to all planning artifacts, including (non-exhaustive): QA plans, remediation guides/task plans, implementation guides, EPIC records, and any stepwise runbooks produced in support of an EPIC.

* When planning for QA, remediation, development, or any other execution work, agents MUST consult **Reality Audits** as a primary input for:  
    
  * component boundaries (what the “thing” is),  
      
  * canonical pathnames and repo loci (where the “thing” lives), and  
      
  * audit-provided component metadata needed to avoid drift.


* Planning documents SHOULD include a short **“PF23 Anchors”** subsection that lists:  
    
  * the component(s) used from Reality Audits, and  
      
  * the key pathnames/loci pulled from those audits that the plan will touch.  
    This is a traceability anchor only; it must not duplicate audit contents.


* Reality Audits are PO-maintained. Planning documents MUST NOT create tasks that assign Reality Audits updates. If an audit appears stale or missing required component coverage, the plan MAY note that as an observation, but must not assign it as agent work.  
    
* Plans MAY check PF documents during planning and review, including read-only checks against Reality Audits, to confirm what PF currently states.  
    
* Plans MUST NOT mandate PF document updates. Planning artifacts MUST NOT require updates to any PF documents as part of PR or OPS deliverables, acceptance posture, tracked issues, “confirming artifacts,” or completion criteria.  
    
* **Documentation drainage is never a planning or approval gate.** Planning artifacts, implementation guides, QA plans, review artifacts, remediation guides, OPS tasks, closeout artifacts, acceptance maps, token↔evidence matrices, step logs, PR summaries, and epic artifacts MUST NOT treat PF10 drain or any other post-QA documentation drainage as a prerequisite, required deliverable, required check, acceptance condition, blocker, or readiness condition by itself.  
    
* Updates to Reality Audits are a manual PO operation only. PR scope MUST NOT include Reality Audits edits, and plans MUST NOT mandate or schedule Reality Audits updates inside PR or OPS work.  
    
* Plans MAY include a “Doc deltas capture” or “Doc delta candidates” note, but these notes MUST be explicitly non-mandatory and MUST NOT be expressed as required PR or OPS tasks. Any PF doc maintenance implied by those notes is PO-owned and out of plan scope.  
    
* Coding agents and implementation agents MAY NOT directly modify PF-Canon documents. If implementation work reveals canon drift, missing canon coverage, or a needed canon change, the agent MUST record that explicitly as a drift note or Doc-Delta candidate in its report and MUST NOT edit the PF-Canon document directly.  
    
* Mapped PF09 completion posture for review and acceptance. When a PR, OPS task, remediation pass, closeout record, or related review artifact speaks about a mapped PF09.x task or subtask, the governing question is whether the mapped work is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review or approval artifacts. The current pre-drain PF09 status text is canon-as-recorded only and MUST NOT by itself be used as a PR acceptability gate, OPS acceptability gate, QA-entry gate, or closure gate.  
    
* PF10 live-truth posture for mapped work. Where PF10 explicitly records the live in-flight truth for the mapped work, review and approval language MUST follow that live truth until later drainage occurs. PF09 remains the checklist-mapping and later-drain record; it is not the live in-flight status surface.  
    
* Review unit and scope for bounded tasks. During review of a PR or OPS task, the reviewer MUST review only the approved task in question and its explicitly approved scope. The reviewer MUST NOT widen the review to later PRs, later OPS tasks, later validation runs, or whole-epic closure work unless the approved task explicitly includes them.  
    
* Approved non-closure steps are judged on their own purpose. If the approved task is a bounded non-closure step, such as validation, gap classification, sequencing correction, evidence capture, repo-side wiring, or another explicitly non-closure step, the reviewer MUST judge that task on whether it truthfully and correctly completes its own approved job. If the approved task’s job is not to bring a mapped PF09.x task or subtask to closure, then PF09 closure is not a review gate for that task and may be skipped in that review as an approved scoping boundary.  
    
* Required truth posture for non-closure steps. For approved non-closure steps, the reviewer MUST verify that the task stays within approved scope, does not overclaim closure, preserves any still-open PF09.x row truthfully as open, contributory, intermediate, validation-only, sequencing-only, evidence-only, deferred, or equivalent approved posture, and does not silently imply that later closure work is already complete.  
    
* Closure-gate trigger for task review. A PF09 closure gate applies in task review only when the approved task explicitly claims that it brings a mapped PF09.x task or subtask to Done, supports a Done recommendation now, or performs final closure, final binding, final acceptance promotion, or other explicitly closure-claiming work. It is non-conforming to hold a bounded approved task to later closure work that belongs to a different approved task or a later approved step.  
    
* Review-language discipline before drain. Before the mapped work is complete in substance, allowed posture words for the mapped PF09.x row are limited to contributory, intermediate, review-clean, bounded, and supportable from repo evidence. Acceptable-status language such as acceptable, accepted, satisfied, complete-for-close, or supportable for later drain to Done MUST be used for the mapped PF09.x row only when the mapped work is complete in substance and governed evidence supports later drainage. Task-level acceptance of an approved non-closure step MUST remain explicitly distinct from PF09 closure status of the mapped row, and the same rule applies to OPS tasks.  
    
* Current PF09 wording may be cited, but only as current canon record. A review or closeout artifact MAY cite the current PF09 row text to show what canon currently records before drain, but it MUST NOT treat that recorded text as proof that the work remains incomplete when approved implementation state, approved OPS state where applicable, and governed evidence already prove the later-drain posture.  
    
* **Infrastructure source rule for plans and related artifacts.** When a plan, implementation guide, QA plan, review artifact, remediation guide, or epic document names an infra or ops dependency (for example provider, project, service, repository, base URL, port, database instance or schema, config key, QA root, or start-command dependency), it MUST use exactly one of these two postures:  
    
  * **PF07-derived posture.** The exact required value is already present in **Glow Infrastructure**, and the document cites or copies that fact directly.  
  * **PF07-gap posture.** The exact required value is not yet present in **Glow Infrastructure**. The document MUST identify the exact missing value set and mark the affected step or claim blocked by missing infrastructure inventory. It MUST NOT leave the item as an executable dependency to be provided later by an unspecified infra or ops owner.


* The following placeholder postures are non-conforming in plans and related documents: vague external-owner instructions such as “infra to provide”, “ops to confirm”, “ask infra”, “await ops details”, guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or `TBD` values treated as executable infra inputs.  
    
* Any infra or ops task described in a plan MUST name the concrete bound value or its exact value source. When the required value is missing from **Glow Infrastructure**, the document MUST identify the missing facts explicitly, mark the dependency blocked by missing infrastructure inventory, and route the needed update as a Doc-Delta candidate or PO follow-up rather than inventing an external owner.  
    
* QA plans and Live QA artifacts MUST NOT guess or redefine infrastructure-owned environment or service bindings. This includes bindings such as `DEV_SAMPLER_URL`, `HDE_BASE_URL`, `DATABASE_URL`, and `DB_BRIDGE_URL`, plus production service base URLs, environment-specific host or port bindings, and canonical QA-root patterns.  
    
* A plan or review artifact that treats an infra or ops dependency as executable without a concrete infrastructure fact or an explicit blocked-gap statement is non-conforming.  
    
* How plans MUST express “reality/existence confirmation.” If a plan requires confirming whether a component, route, contract, or locus exists, the plan MUST express confirmation in one of these allowed forms:  
    
  * PF check (allowed): “Check Reality Audits for the current recorded existence/locus statement.” This is a read-only check and MUST NOT imply an update.  
      
  * Repo-local evidence (required when PF is silent or insufficient): capture confirmation as repo-local evidence (for example deterministic command output recorded into an audit artifact, a governed gate log, a QA step-log entry, or a test or probe result). The plan MUST NOT require turning that result into a PF update.


* PF check (allowed): “Check Reality Audits for the current recorded existence/locus statement.” This is a read-only check and MUST NOT imply an update.  
    
* Repo-local evidence (required when PF is silent or insufficient): capture confirmation as repo-local evidence (for example deterministic command output recorded into an audit artifact, a governed gate log, a QA step-log entry, or a test or probe result). The plan MUST NOT require turning that result into a PF update.

---

**Remediation task plans (DEV PRs \+ OPS tasks) — canonical model and approval gate.**  
This rule applies to remediation task plans that combine repo-local DEV work and PO-run OPS work.

**Task model (two task types only).**

* DEV tasks are PRs only and MUST be enumerated as `PR-01`, `PR-02`, ... (no mixed-task steps).  
    
* OPS tasks are PO-run procedures only and MUST be enumerated as `OPS-01`, `OPS-02`, ... (no mixed-task steps).  
    
* Discovery is allowed but MUST be explicit per task as `DISCOVERY` vs `CHANGE`.  
    
* Cross-lane dependencies MUST be explicitly declared in the dependent task using the exact line:  
  `Inputs needed from Task <ID> during implementation: <exact items>`  
  Placeholders (e.g., “TBD”, “to be determined”) in this line are a mechanical blocker.

**Approval gate scope (tight; no thrash).**  
For remediation task plans, approval MUST focus on:

* correct task model (OPS vs DEV; DISCOVERY vs CHANGE; no mixed tasks),  
    
* correct sequencing and explicit cross-lane dependencies,  
    
* concrete deliverables (lowercase paths \+ filenames), and  
    
* concrete verification success criteria (what “done” means).

Detailed command lines and step-by-step failure handling are not required as a plan-approval condition. In-flight operational detail is allowed (OPS command selection, exact CLI flags, and procedural failure handling) as long as the evidence posture remains intact.

**Mechanical blockers (auto-reject if present anywhere in the plan).**

* Any `PR-xx` task missing a paste-ready Codex Prompt embedded inside that task.  
    
* Any deliverable that is specified only as a directory (deliverables must be a concrete lowercase file path including filename, e.g., `audit/qa/<epic>/<task_id>/<filename>`).  
    
* Any cross-lane dependency missing the exact dependency line above, or using non-concrete “exact items.”  
    
* Any task that mixes DEV \+ OPS work in a single task.

**Evidence posture remains non-negotiable (even when commands are developed in flight).**

* OPS execution MUST capture:  
  * the produced artifacts at the declared output paths,  
  * any deviation notes needed to explain why a different command/flag was used.  
  * The exact commands actually run (verbatim) SHOULD be captured as a dedicated deliverable file when the approved plan requires it. If the approved plan’s required deliverables do not include a command transcript file and all required deliverables are otherwise complete and auditable, omission is a provenance Caveat (record as `CAVEAT: PROVENANCE_THIN`) and is not, by itself, a blocker.  
* Evidence MUST land under `audit/qa/...` (lowercase) with explicit filenames sufficient for later audit.  
* In-flight command flexibility does not permit:  
  * changing governed artifact locations or filenames,  
  * introducing new governed files without explicit statement of indexing/mirror intent, or  
  * indexing remediation-only diagnostics into governed indices/mirror.

**Remediation-only artifacts vs governed surfaces (default posture).**  
Remediation-only diagnostics/manifests MUST NOT be introduced under governed artifact surfaces unless explicitly framed as a governance change. Default posture: remediation-only artifacts live under remediation audit paths (e.g., `audit/qa/.../remediation/...`) and do not enter the governed Evidence Index or machine mirror.

**Determinism remediation predicate targets (D16–D20; canonical emitted surfaces; no wrappers/markers).**

* D16 — orientation ordering demo (demo-only, deterministic): `audit/gates/topology/orientation_demo.txt` (+ required sibling `audit/gates/topology/orientation_demo.txt.path_proof.txt`)  
    
* D17 — env pins: `audit/gates/determinism/env_pins.log` (+ required sibling `audit/gates/determinism/env_pins.log.path_proof.txt`)  
    
* D18 — sanity pipeline log: `audit/gates/sanity_pipeline/sanity_pipeline.log` (+ required sibling `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`)  
    
* D19 — canonical JSON gate check log: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` (+ required sibling `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`)  
    
* D20 — canonical JSON gate compare log: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` (+ required sibling `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`)

---

**Remediation plans that touch Evidence Index / mirror: “exact filenames” rule (deliverables \+ verification).**  
Any remediation plan that includes tasks touching governed evidence indices/mirrors MUST explicitly name the exact index \+ path-proof filenames as task outputs and as embedded verification checks.

Canonical quick reference (use verbatim when applicable):

Evidence index (human-readable):

* `docs/evidence/INDEX.json`  
    
* `docs/evidence/INDEX.sha256`  
    
* `docs/evidence/INDEX.json.path_proof.txt`  
    
* `docs/evidence/INDEX.sha256.path_proof.txt`

Evidence index mirror (machine-readable):

* `artifacts/evidence_index.jsonl`  
    
* `artifacts/evidence_index.jsonl.path_proof.txt`

Canonical placement is co-located sibling path proofs: `<file>.path_proof.txt` MUST sit next to `<file>` and MUST NOT be placed in an alternate directory.

If a plan proposes a new file under governed surfaces, it MUST state whether it is intended to appear in the indices/mirror. Absence of that statement is a blocker.

---

**Portability vs provenance (non-PF evidence).**  
Remediation guides and task plans may include a short “Evidence inventory reviewed” list for provenance, but MUST NOT require the reader/executor to open external files to perform the work.

* If a remediation plan depends on any non-PF fact (command outputs, headers, error strings, file paths observed, status lines), the plan MUST embed that fact directly in the document as a short quote or precise paraphrase inside an **Observed Evidence Snapshot** section.  
    
* If an Artifact Map (or equivalent) is included, it MUST explicitly label non-PF inputs as:  
  “provenance only; not required to execute”  
  Otherwise it is treated as an execution dependency and becomes a portability blocker.  
    
* When a non-PF observation drives a branching decision, the plan MUST include:  
    
  * the observation to look for (exact string/status/shape),  
      
  * the decision rule, and  
      
  * the output artifact path where the observation is captured (lowercase file path including filename).

## **9.8 QA plans — step-level Deliverables (no screen-only acceptance) \[Required−Now\]**

### **9.8.1 Scope**

**Routing note (templates and step-log header schema).**  
Live QA plan template headings/structure and the minimum step-log header schema are owned by **Plan Templates** (titles-only). This document does not define a competing header schema field list; it defines governance posture (what counts as a blocker, what evidence is required, and how token claims behave when present).

Governance rules for the **Plan Templates**\-owned primary step-log reference and token fields (not a complete header schema; empty lists allowed):

* `pf_refs` (MUST be present; `[]` allowed)  
    
* `intended_tokens` (MUST be present; `[]` allowed)  
    
* `claimed_tokens` (MUST be present; `[]` allowed)

When a step claims no tokens, both `intended_tokens` and `claimed_tokens` MUST still appear as empty lists (`[]`).

**Intended vs claimed token alignment.**

* When `claimed_tokens` is non-empty, every token in `claimed_tokens` MUST also appear in `intended_tokens`.  
    
* A step MUST NOT introduce unplanned token claims.  
    
* If `intended_tokens` and `claimed_tokens` differ, the step record MUST explicitly explain the delta. Without that explanation, the step MUST NOT be treated as a clean `PASS`.

If any of the required keys above are omitted, that omission MUST be recorded explicitly as an evidence-format deviation (do not treat omission as “implicitly empty”).

These rails apply to any document that defines **stepwise QA execution**, including:

* QA Implementation Plans  
    
* Live QA Guides  
    
* QA addenda that include explicit step lists (including PF10 QA addenda)

This section governs **approval posture** and **minimum evidence hygiene** for QA steps. Detailed QA playbooks, log schemas, and token libraries live in **Glow QA Guide** (titles-only).

### **9.8.2 Rule — Deliverables are mandatory per step**

For every QA step in a Live QA plan, the operator MUST produce the deliverables the plan specifies for that step. Deliverables are not advisory.

**Objective-first Live QA Plans (directive posture).**  
Live QA Plans are objective-first, not command-string-first. Each step MUST specify:

* objective (what is being proven),  
    
* proof obligations: required deliverables and evidence outputs,  
    
* explicit PASS and FAIL predicates.

**Dependency posture is required per step.**

* If a QA step depends on an executable dependency, the step MUST name the dependency set explicitly.  
* The step MUST perform a dependency preflight before behavior evaluation. The plan MUST state the exact readiness check or checks that prove the dependency is present and runnable.  
* When the execution venue allows activation or installation, the step MUST state the exact activation or installation action to take if the preflight fails.  
* When activation or installation is not allowed or not known, the plan MUST say so explicitly. If readiness cannot be established, the step MUST be classified as `FAIL_TOOLING` or `TOOLING_BLOCKED`, as appropriate.  
* Behavior verdicts MUST NOT be issued before dependency readiness is established. A dependency readiness failure MUST NOT be classified as `FAIL_BEHAVIOR`.  
* A shared bootstrap step does not remove per-step responsibility. Each later step MUST either include its own dependency preflight or explicitly depend on the bootstrap and rerun a short step-local readiness check before the main behavior command.  
* The dependency preflight result and any activation or installation action taken MUST be captured in the step’s governed evidence.  
* **Execution-time dependency discovery.** If a Live QA step discovers an executable, import, interpreter, package, toolchain, or system-level dependency that was not named in the approved plan, the final step may still be reviewed as `PASS` only when the execution venue permits activation or installation, the activation or installation restores readiness, the same approved proof target is rerun, the required deliverables and PASS/FAIL predicates remain unchanged, and the action does not change rails posture, acceptance-token posture, public/private surface posture, evidence-family identity, or scope.  
* **Plan gap is preserved.** Accepted execution-time dependency activation does not erase the plan defect. The review record MUST preserve both truths: final PASS evidence may be valid, and the approved plan omitted a dependency, preflight, or activation action. The original dependency-readiness failure MUST NOT be recast as product behavior failure, and it MUST NOT be hidden under the final PASS.  
* **Evidence requirements for dependency activation.** The governed step evidence MUST name the missing dependency, the readiness failure or failure signature, the activation or installation action taken, the rerun command or proof target, the final deliverables, and the final PASS, FAIL, or TOOLING classification. If readiness cannot be restored, the step MUST be classified as `FAIL_TOOLING` or `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`.

Steps MUST use general command-line directives, not literal command strings. A plan MAY include example command forms, but reviewers MUST NOT require verbatim, syntax-perfect command lines as an approval gate. Execution-time command resolution is authoritative. The step log is authoritative for the exact command or commands executed and the produced artifacts.

A command syntax defect in a Live QA Plan, QA Plan, remediation plan, or plan-review artifact MUST NOT be treated as a Blocker when command identity, target check, proof obligation, evidence family, and PASS or FAIL or TOOLING classification remain clear, and when the defect is limited to syntax, quoting, escaping, punctuation, rendered markup, or a small local expression repair that the QA executor can correct without inventing a new repo locus, command source, route, artifact family, acceptance predicate, or PASS or FAIL criterion.

QA-correctable syntax defects include shell quoting or escaping cleanup, markdown-rendering artifacts inside a command note, obvious local expression punctuation repair, heredoc or JSON quoting normalization, wrapper syntax that does not alter the command target, inputs, outputs, or PASS or FAIL predicate, and similar syntax-layer issues that preserve the approved command identity.

The following remain blocking: an unproven executable repo locus; ambiguous command identity; a command that points to the wrong artifact, route, evidence family, check, or predicate; a defect that requires inventing replacement execution logic; a defect that changes acceptance semantics; a plan dependency on unavailable non-PF documents for command reconstruction; or a plan that requires guessing missing paths, endpoints, test names, token names, or repo loci.

When QA corrects a plan command syntax defect during execution, the governed step evidence MUST record the exact command actually executed, the command provenance, the reason for the correction, the produced evidence artifacts, and the final PASS, FAIL, or TOOLING classification. The correction MUST NOT silently alter the acceptance target.

Plans SHOULD minimize locus strings in step text. Avoid naming specific script paths or test file paths unless they are canon-defined or are fixed-path obligations. If a step must name a repo locus string, the repo loci proof gate still applies.

**QA planning reality posture (repo-locus lock; narrower than §9.7.9).**

* In Live QA planning artifacts (plans, prompts, reviews, runbooks, and checklists), the ONLY allowed provenance sources for repo-reality claims are:  
    
  * PF10 — HDE Build Notes  
      
  * PF canon  
      
  * the initial QA Audit for the epic (repo reality and readiness proof)


* PF23 — Reality Audits MUST still be consulted during QA planning as a read-only input for repo-reality context and existence or locus framing, but PF23 does not by itself authorize a repo-resident locus claim unless that claim is also grounded in the allowed provenance sources above.  
    
* This QA-specific provenance rule applies to repo-resident or repo-reality strings, including:  
    
  * file and directory paths  
      
  * endpoint names and routes  
      
  * module and component identifiers  
      
  * script names, runbook names, and command strings  
      
  * check and test identifiers, CI job names  
      
  * environment variable names when treated as already-existing  
      
  * fixed output locations when treated as already-existing  
      
  * negative existence claims


* No invention, no inference, no memory. A Live QA planning artifact MUST NOT introduce, guess, infer, paraphrase, normalize, or fill in any repo-resident locus string. If the exact locus string does not appear verbatim in an allowed provenance source, it MUST NOT appear as a repo-resident claim in the plan.  
    
* Verbatim-only requirement. When a repo-resident locus string is used, it MUST be copied character-for-character from an allowed provenance source. No renaming, case folding, wildcard expansion, or invented variants.  
    
* Conflict posture. If PF10, PF canon, the initial QA Audit, or PF23 appear inconsistent, treat the situation as a reality ambiguity. The plan MUST NOT assert a reconciled locus as fact; it MUST either route the uncertainty to a discovery step or return for revision.

**Discovery-first posture (mandatory).**

* Live QA Plans MUST assume that any repo detail not proven is unknown until discovered during the run. Plans MUST prefer real-time discovery and observation over pre-specifying implementation guesses.  
    
* When a step depends on a repo-resident locus that is not proven at planning time, the plan MUST:  
    
  * state the discovery intent (what must be located or verified),  
      
  * state the discovery acceptance (what counts as sufficient proof),  
      
  * require recording the discovered locus string verbatim in the check evidence before use, and  
      
  * define PASS, FAIL, and BLOCKED outcomes for the discovery itself.


* Command-line minimalism is required. Live QA Plans SHOULD describe the goal of the action, the observable outputs that matter, and the evidence that must be captured. The executor MUST record the exact commands actually used into the check evidence at runtime. If a plan includes an exact command string, that string MUST be proven by an allowed provenance source.  
    
* Blocking posture. Any Live QA plan that includes a repo-resident locus string not proven verbatim by an allowed provenance source, a speculative topology claim, a placeholder locus, or an invented script MUST be returned for revision.

**Plan-created artifacts are allowed, but MUST be explicit.**

* The repo-locus provenance lock applies only to loci asserted to already exist in the repo. It does not prohibit plan-created deliverables or evidence outputs.  
    
* If a QA plan requires creating a file, it MUST include:  
    
  * the exact repo-relative path and filename,  
      
  * runnable creation instructions that produce the file at that path, creating parent directories if needed, and  
      
  * one sentence stating why the file is required.


* The plan SHOULD label each mentioned file path as repo-resident or plan-created. Missing labels are non-blocking only when the file is clearly a run-produced deliverable and the plan already provides the required how and why.  
    
* A plan MUST NOT say “create a helper script”, “write a manifest”, or “generate a report” without also providing the exact creation path, the creation process, and the reason it is created.  
    
* If a plan-created file is evidence-bearing, the creation instructions MUST be deterministic enough to reproduce the file unambiguously.  
    
* Live QA Plans MUST NOT invent or assume helper scripts exist. A plan-created script is permitted only when a required deliverable cannot be produced without one. In that case the plan MUST name the exact repo-relative path and filename, include runnable creation instructions, state why the script is required, and keep the script minimal and purpose-bound to the deliverable.

This posture does not relax existing requirements for functional Live QA, evidence capture, SAFE rails, or explicit pass/fail criteria.

**Functional Live QA is mandatory for functional changes.**  
If an epic includes a runtime-visible behavioral change (a functional change), at least one Live QA step MUST execute the runtime path and capture evidence of the behavior. Artifact-only outputs (for example catalogs, headers, or static snapshots) are insufficient by themselves for functional changes.

If a functional change touches a vendor seam, the functional Live QA step MUST exercise that seam (live or controlled mock) and capture evidence of the observed behavior. If functional proof requires opening SAFE rails (for example `ALLOW_NETWORK=1`), that is acceptable when required, but it MUST be explicit, bounded, and captured with a keys-only and secret-free evidence posture (see §3.1).

**Step-local rails deviations must be explicit and bounded.**

* When a Live QA step executes under a rails posture that differs from the approved plan default for that step, the deviation MUST be recorded explicitly as a step-local deviation rather than silently treated as conforming execution.  
* A step MAY still be reviewed or recorded as `PASS` under such a deviation only when all of the following are true:  
  * the deviation is explicitly PO-approved for that step,  
  * the actual executed rails are captured in the governed step evidence,  
  * the step’s required deliverables are complete and trustworthy,  
  * the step’s stated PASS and FAIL predicates are still evaluated against the actual evidence, and  
  * the deviation does not expand scope, weaken the secret-free or keys-only evidence posture, or change the acceptance target.  
* When the deviation is introduced via a Moon Loop or equivalent step-local approval, the governed evidence MUST include the approval entry or equivalent step-scoped note under the step’s QA root.  
* In that posture, the deviation is a planning or execution caveat and MUST be called out as such in the review record. It is not automatically a trust failure or automatic remediation trigger.  
* If the deviation is unapproved, unrecorded, or changes the acceptance target, the step MUST NOT be treated as `PASS`.

**Step-local evidence deviations and path-equivalence corrections must be explicit.**

* A bounded Moon Loop or equivalent step-local approval MAY correct an evidence-scoped defect, restore a missing precondition artifact, or align a stale planned artifact path to the current implemented evidence family only when the approval is step-scoped, the correction remains under existing governed roots, no new route, public surface, evidence root, acceptance target, or PF-canon edit is introduced, and the required PASS and FAIL predicates remain unchanged.  
* If a planned deliverable path is stale but the same proof goal is satisfied by a current PF10-supported or plan-approved evidence artifact, the governed step evidence MUST record the stale path, the replacement artifact path, the source that makes the replacement authoritative for the step, and the search or proof showing why the stale path is not the final governing artifact.  
* If the deviation restores a required precondition artifact before rerunning the approved step, the governed step evidence MUST name the precondition artifact, the remediation action, the final step deliverables, and the final PASS, FAIL, or TOOLING classification.  
* The earlier blocked or failed condition remains part of the record and MUST NOT be hidden. It is not a blocker by itself once the bounded rerun is clearly evidenced, the approved criteria are met, and the review record states why the deviation did not change the acceptance target.

**Live QA failure routing after failed checks.**

* A bounded Moon Loop may correct only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under the approved QA root. It MUST NOT be used to relabel product-code, repo-test, repo-evidence-generator, non-QA-root governed-artifact, public-contract, PF-document, acceptance-token, or multi-subsystem remediation as QA-only correction.  
* A change to product code, repo tests, repo evidence generators, governed artifacts outside the approved QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction.  
* Non-QA-root remediation after a Live QA failure MUST be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before it can be treated as the basis for a final PASS-grade QA run. The later QA record may cite that remediation only when the remediation path is explicit and the QA record does not claim the remediation was performed by the Live QA step itself.  
* When final PASS proof relies on a non-QA-root governed evidence refresh, the final PASS receipt MUST cite the routing receipt or equivalent approved routing artifact before the post-refresh proof lines. It MUST also preserve the failed pre-routing receipt as context, identify which refreshed non-QA-root evidence family was relied on, and state that the final proof relies on routed refresh rather than unapproved Moon Loop correction.  
* If a Live QA check fails because a governed repo artifact lacks a required structural field, the check MUST NOT be satisfied by raw string-presence wording alone. The QA plan, remediation guide, or follow-up work item MUST define the structural predicate that proves the field is present and semantically tied to the intended source.  
* If a Live QA check fails because a proof command used a brittle exact-string match against governed prose, including casing-only or wording-only mismatch, the final classification MUST preserve the distinction between the proof-harness defect and the intended behavior under review. A casing-only or prose-phrasing mismatch MUST NOT be treated as final `FAIL_BEHAVIOR` until the raw artifact, intended semantic proof target, and governing PASS or FAIL predicate have been reviewed.  
* When the intended proof target is a boundary posture recorded in prose, the preferred proof form is a stable machine-readable field, canonical structural predicate, or case-normalized semantic check that preserves the approved proof target. If a bounded rerun or remediation is accepted, the remediation record MUST preserve the original failed proof, state why the failure was a proof-harness defect, and show that the accepted proof did not change the acceptance target, evidence family, rails posture, token posture, or scope.  
* When the structural field is `selection_order`, the evidence MUST be structural adapter-selection evidence derived from observed adapter attempts or provider order and MUST NOT create a new acceptance-token claim.  
* If the initial failing artifact is overwritten or unavailable by the time remediation begins, the remediation record MUST state that the initial failure artifact is unavailable. It MUST NOT reconstruct missing logs, hashes, timestamps, or result bodies.

**Requirements (binary):**

* **Git discipline (strict)**. All referenced deliverables MUST be committed under the audit roots unless a token explicitly allows a local-only artifact. Deliverables MUST be path-addressable.  
    
* **Deliverable naming**. Deliverables must be deterministic and include enough scope in the filename to prevent collisions across steps.  
    
* **Copy/paste hygiene (execution venue)**. Planning documents and plan-derived excerpts MUST NOT use fenced code blocks. Commands and snippets MUST be presented as plain text lines. Review and approval MUST bind to command identity and semantic intent, not to perfect terminal pasteability; wrapping, indentation, and whitespace-only defects are handled via the Live QA Moon Loop when they do not change meaning.  
    
* **No vague phrases.** Do not use phrases like "capture logs", "check output", or "run the test suite" without naming the exact artifact(s), path(s), and pass/fail criteria.

Binary means: If a required deliverable is missing, the check is mechanically invalid.

**Deliverables list authority (step-local artifact obligations).**

* Only artifacts explicitly named in the step’s Deliverables list, or explicitly bound by the step’s PASS or FAIL criteria, are required deliverables for that step.  
    
* An artifact path that appears only inside a source excerpt, example command, shell redirection, or operator note does not become a required deliverable unless the plan also names it in the Deliverables list or explicitly binds PASS or FAIL to it.  
    
* Such artifacts MAY still be produced as auxiliary provenance artifacts. If present, they MAY be reviewed as supplemental evidence. If absent, their absence is non-blocking unless the plan expressly made them required.  
    
* Reviewers MUST evaluate step completeness against the step’s stated Deliverables and PASS or FAIL rules, not against every incidental artifact mentioned inside example commands or source excerpts.

**Plan-level intended-token rosters vs step-local proof obligations.**

* A Runbook Check Matrix or similar plan-level intended-token roster MAY list intended tokens for a step without making token-by-token proof lines mandatory in the step report.  
    
* When a step’s Deliverables list and PASS or FAIL criteria are deliverable-based, reviewers MUST judge the step using those step-local obligations and the governed step evidence actually captured for that step.  
    
* In that posture, the absence of token-by-token proof lines in the step report is a documentation clarity issue and is non-blocking.  
    
* If the step report or the step’s PASS or FAIL criteria explicitly require token-by-token proof lines, those lines become required evidence for that step.  
    
* This rule does not relax the governed `intended_tokens` and `claimed_tokens` alignment rules for step records.

**Conditional deliverables and branch-specific evidence.**

* A Live QA plan MAY declare a deliverable as conditional only when the triggering condition is named explicitly in the step.  
    
* A deliverable gated behind a named condition is required only when that condition is met.  
    
* If the condition is met and the deliverable is absent, the step has a required-evidence failure for that branch.  
    
* If the condition is not met, the plan MUST require an explicit branch artifact or note that records the unmet condition and the resulting posture (not applicable, skipped, or blocked, as appropriate). That branch artifact becomes the required evidence for the unmet branch.  
    
* Reviewers MUST NOT treat absent conditional outputs as missing evidence when the unmet condition is explicitly recorded and the plan defines the conditional branch correctly.  
    
* Plans MUST NOT hide unconditional evidence behind vague or implicit conditionals.

**Reconciliation rules and guardrails (non-negotiable):**

* **Repo reality precedence.** If a plan expects a deliverable or shape that does not match the repo’s reality, the repo wins. Do not block approval unless the mismatch prevents pass/fail evaluation. Document the mismatch as a caveat and update the plan or code accordingly.  
    
* **Product-input availability gate.** When a Live QA step’s PASS path depends on current-product inputs or identifiers, the plan MUST establish that those inputs are valid and currently obtainable in the product surface, or MUST frame the step as an explicit input-availability gate.  
    
* If authoritative run evidence shows the required inputs are not valid product inputs for the current surface, or should not be expected for the run, the outcome MUST be classified as `BLOCKED` due to input availability or planning defect, not as a product behavior failure.  
    
* In that posture, artifacts from the unexecuted branch are not actionable remediation targets. Their absence is an expected consequence of the blocked precondition and MUST be recorded as such in the step evidence.  
    
* Review posture. A plan whose PASS criteria depend on unavailable or non-product inputs, without declaring an input-availability gate, MUST be returned for revision because its PASS path is structurally unreachable.  
    
* Re-run posture. Re-run only when valid product inputs become available or the plan is revised to use a supported and currently obtainable input form.  
    
* **Step logs status posture.** Status is `PASS` / `FAIL` / `BLOCKED` and is a claim. If status is `PASS`, required deliverables must exist and show the required evidence.  
    
* **PASS requires step-scoped evidence.** A Live QA step MUST NOT be marked `PASS` unless the step record includes at least one step-scoped evidence pointer under the governed QA root for that exact step, or an explicitly equivalent step-scoped evidence pointer line preserved in the epic’s primary QA record.  
    
* **Record-integrity rule for PASS.** The step identifier in the heading, decision summary, primary-log path, and any step-scoped evidence pointer MUST agree. If a step record is mislabeled, duplicated, or contaminated with unrelated content such that the step-to-evidence mapping is ambiguous, the step MUST NOT be treated as `PASS` until corrected.  
    
* **Blocked-step minimum fields.** When a step is recorded as `BLOCKED`, or when a review uses `UNEXECUTABLE` as a narrative label for the blocked posture, the canonical status remains `BLOCKED` and the step record MUST include:  
    
  * the blocking precondition,  
      
  * why it cannot currently be satisfied,  
      
  * whether the blockage is closeout-blocking, and  
      
  * the required follow-up, classified as plan change, implementation change, or input-availability follow-up.


* **Document-structure remediation evidence.** When remediation corrects a mislabeled, duplicated, or contaminated step record, the remediation evidence MUST include:  
    
  * the incorrect snippet,  
      
  * the correction rationale, and  
      
  * a post-fix verification artifact or log line showing that the step id, heading, and evidence pointers now align.


* **Step-log header writer env exports (per-check; required when used).** If a Live QA plan uses a step-log header writer that reads per-check metadata from environment variables, the plan MUST export the complete required set immediately before header generation for each check and MUST NOT rely on prior step state.  
    
  * Minimum per-check exports (names must match the header writer contract): `CHECK_ID`, `CHECK_NAME`, `PASS_FAIL`, `COMMANDS_JSON`, `ARTIFACTS_JSON`, `PF_REFS_JSON`.  
  * Command-sequence fidelity. If a check executes multiple commands, the governed step record MUST preserve the exact ordered multi-command sequence that was actually run. When represented in a single field, the sequence MUST be captured as an explicit pipeline or explicit joined sequence that preserves execution order. Paraphrased command summaries are non-conforming.  
  * Command provenance vocabulary. If a governed step record includes a command provenance value, it MUST use one of: Codex prompt, Copy/paste from plan, or Explicitly created.  
  * Artifact self-listing invariant: when `PASS_FAIL` is `PASS`, `ARTIFACTS_JSON` MUST include the on-disk path to that check's `primary.log` under the audit roots. If missing, treat as an evidence-schema defect and remediate via the allowed Moon Loop header regeneration before asserting `PASS`.  
  * If the defect is discovered mid-run (for example a check already executed but `primary.log` is missing the canonical header or has the wrong check ID), a Moon Loop deviation is allowed to export the required header vars for that check, regenerate the JSON header, and reassemble `primary.log` by prepending the corrected header while preserving the existing body verbatim.  
  * Record the deviation as evidence-capture only. Do not modify product behavior, test assertions, or acceptance criteria to compensate for missing header metadata.  
  * Anti-drift: if the plan uses the header writer, the export contract above is required for every check that uses it. Do not rely on global state from prior steps.


* **Checks-only evidence layout (hard).** Check-scoped Live QA evidence MUST live under a single epic-scoped QA root and be organized by `check_id`. Evidence paths MUST be stable across re-runs. Re-running QA MUST NOT create a new run root, timestamped run directory, or any parallel per-run evidence tree.  
    
* **History is not correctness.** Deliverables and step logs are canonical by check and by named artifact. Plans MUST NOT introduce `run_id` (or `RUN_ID`) as an input, step header field, evidence selector, correctness dimension, or directory discriminator. Optional per-execution nesting is disallowed. Check-scoped plan-created outputs MUST live under the stable check directory unless Governance explicitly pins a different canonical home.  
    
* **No invented executable surfaces (baseline commands only).** Live QA plans, runbooks, and reviews MUST NOT invent scripts, modules, tests, harnesses, endpoints, CI jobs, or helper commands. If a plan mentions an executable locus, it MUST name the repo-resident locus and it MUST exist at review time. If the locus does not exist, the plan MUST mark it as a deliverable ("needs creation") and the plan MUST NOT proceed as if it already exists.  
    
  * Evidence roots are not code roots: do not treat `audit/**` or `artifacts/**` as pre-existing runnable toolchains.  
      
  * Preflight (required): before declaring a step executable, verify that each invoked repo entrypoint exists and is discoverable in the repo. Do not reference directories like `tools/qa/**` or `scripts/**` unless they are present and proven in-repo.  
      
  * Missing entrypoint posture: if an invoked repo entrypoint does not exist, the step outcome is `TOOLING_BLOCKED`. The operator MUST stop and capture the failure transcript as evidence. Do not mint a new helper script during QA execution to "make the plan work".  
      
  * Remediation path (repo-first): missing tooling must be addressed by delivering the required repo entrypoint and updating the plan to reference the real locus. Repo-provided QA harness entrypoints are Mechanics-owned surfaces and must exist in-repo before Live QA can reference them. In-session remediation is limited to syntax-layer corrections that preserve meaning; it MUST NOT introduce new executable entrypoints.  
      
  * “Baseline commands” means standard invocations that exist without repo invention (for example `python -m`, `pytest`, `curl`, `jq`), and do not imply a repo toolchain unless explicitly proven.


* **Live QA Moon Loop (syntax remediation).** Default posture is that the plan is executed as written. If execution fails due to syntax-layer defects introduced by Markdown transport (for example wrapping, indentation, quoting, or JSON-carrying environment variable assignments that do not parse), the operator MUST use a bounded remediation loop:  
    
  * capture the failure signature (stderr/stdout \+ the exact command form used)  
      
  * apply the minimum semantic-preserving fix  
      
  * re-run and capture the successful transcript and artifacts  
      
  * record the remediation as a caveat in the step log


* stop condition: if remediation exceeds scope (meaning changes, requires new tooling, or expands blast radius), mark the step `BLOCKED` and escalate. This posture relaxes execution posture only. It does not relax evidence requirements, safety rails, or acceptance criteria.

---

#### **Execution detail precedence and step-log rules**

Commands are treated as plain text lines. The plan is executed in a terminal, but the approval venue is Markdown. Execution authority precedence order is:

1. The step log header fields and explicit PASS/FAIL criteria.  
     
2. The emitted artifacts under audit roots (paths \+ content hashes when applicable).  
     
3. The step-by-step prose.

Hard rules:

* A step log must always enumerate the deliverables and must link each to an on-disk path under the audit roots.  
    
* If prose contradicts emitted artifacts, artifacts win.  
    
* If a command line in prose differs from the actual invoked command captured in the step log, the step log wins (but the discrepancy must be called out as a caveat).  
    
* A plan MUST NOT include placeholder tokens like `<FILL THIS IN>` or invented path roots.  
    
* Branch/commit workflow is out of scope. No plan step should require PR operations.

---

### **9.8.3 Review gate (blocking)**

**Blocker definition (Live QA planning / plan approval).**

A Blocker is only an issue that prevents the operator from executing the plan in the target environment or prevents reviewers from determining pass/fail for the in-scope behavior with confidence.

A plan MUST be rejected (and returned for revision) if any of the following hold:

* required operator inputs are missing from the plan header (see §9.8.1)  
    
* pass/fail criteria are missing or not checkable from Deliverables  
    
* the Deliverables list is missing required evidence paths or uses vague artifact language  
    
* the plan contains prohibited truncation markers or prohibited characters (see §9.7.4), including the Unicode ellipsis character (U+2026) and three consecutive U+002E FULL STOP characters  
    
* the plan uses fenced code blocks anywhere (planning documents, reviews, or plan-derived excerpts)  
    
* the plan introduces `run_id` or `RUN_ID` as a required input, step header field, evidence selector, acceptance key, per-run directory discriminator, or operator-set per-run evidence root, or otherwise introduces per-run directory nesting, timestamped run directories, or any “fresh directory for this run” posture for Live QA evidence  
    
* the plan introduces or depends on unapproved environment variable names as required inputs, required evidence schema keys, or required step-log header writer inputs (including any `MODO_*` name). Environment variable names are governed interface. A plan MUST NOT mint new environment variable names during Live QA or Moon Loop. If a new env var is required, treat it as a development change and revise the plan only after the variable is canon-approved.  
    
  * Legacy exception (HDE-EPIC025 only): the already-approved HDE-EPIC025 Live QA Plan contains inert `MODO_*` placeholders. They MUST NOT be required for PASS/FAIL, treated as required evidence schema keys, or used as proof of rails posture or execution configuration. They MUST be removed from the plan/template at the next revision. This exception MUST NOT be replicated.


* commands are semantically ambiguous (cannot be tied to a real baseline tool \+ a repo-proven locus) or are unsafe/destructive without an explicit authorized token  
    
* the plan relies on unproven repo file paths (not present in repo; see §9.7.9) or names an invented endpoint route  
    
* the plan proposes VCS workflow as a QA step (branch/commit/PR chatter)  
    
* the plan includes paths that are neither known canon roots nor explicitly QA-created evidence outputs with creation instructions \+ purpose \+ pass/fail (see §9.7.9)  
    
* the plan requires forbidden rails behavior (for example secrets-in-logs) or violates SAFE rails posture  
    
* omission of the Doc-Delta Capture deliverable required by **Plan Templates** (when applicable)  
    
* the plan depends on a helper/wrapper script or harness as a required step entrypoint unless the script is repo-proven and explicitly named in the plan; plans MUST NOT instruct writing a new repo script during QA execution

**Formatting is not an approval gate, except for explicit prohibitions.**

Reviewers MUST NOT block approval based on line wrapping, indentation, bullet styling, or whitespace-only issues, as long as command identity, loci, and pass/fail are clear. The explicit formatting prohibitions are:

* prohibited characters that signal truncation or corruption (see §9.7.4)  
* fenced code blocks (prohibited)

Everything else is a Caveat. Caveats must be recorded in the plan header or the step log (as applicable), but do not block approval.

**Review source-retrieval guard (no excerpt-based claims).**

Reviews must reference the governing passages. Reviewers MUST retrieve (by opening the authoritative source) the exact section being cited. Reviews MUST NOT assert conclusions based only on partial excerpts or UI-snipped fragments.

If a relied-on excerpt shows truncation signals (mid-sentence cutoffs, missing section structure, or truncation markers described in §9.7.4), treat it as a tooling failure and re-retrieve until the full relied-on passage is visible before drafting or approving.

**Markdown sanitation guard (presentation vs semantic escapes).**

Review excerpts may remove presentation-only Markdown escapes for readability. Reviews MUST NOT unescape or rewrite semantic characters inside executable commands (quotes, backslashes, JSON escapes, or shell-sensitive characters) unless the change is explicitly justified by the semantic form used in execution evidence.

**Conflict note (explicit override).**

If any template/checklist/process language causes non-execution issues to be treated as Blockers, this section governs Live QA plan approval.

**Rule (template semantics; normative). NOT RUN / DEFERRED is not missing evidence.**

* Plans and “normative” closure templates may enumerate artifacts for steps that have not executed yet.  
    
* Any plan template that enumerates step-scoped evidence paths MUST explicitly label future-step artifacts as **NOT RUN** (or **DEFERRED**) until the producing step has executed.  
    
* **NOT RUN / DEFERRED** MUST NOT be treated as a missing-evidence failure.  
    
* **Missing evidence** is reserved for the case where the producing step executed, and the artifact that step is supposed to emit is absent or unproven.

**Rule (closure and rollup steps; normative). State separation and no dangling evidence pointers.**

* Closure and rollup templates MUST separate (at minimum) these states:  
    
  * PRESENT: artifact exists and is referenced by path.  
      
  * MISSING: producing step executed, artifact absent or unproven.  
      
  * NOT RUN / DEFERRED: producing step not executed yet (no artifact expected).


* Closure records and rollups MUST NOT include path references to artifacts that do not exist at the time the record is produced.  
    
  * If a check is deferred, list it by check id and state, not by a non-existent file path.


* If a template’s evidence-pointer list implies that future-step artifacts are PRESENT or required evidence now, reviewers MUST treat this as a plan defect.  
    
  * Treat it as a Blocker only if it prevents execution or prevents pass/fail determination under the plan’s stated criteria.  
      
  * Otherwise, record as a Caveat and proceed, then drain the defect into the governing template and canon.

**Rule (prompt-family separation; normative). AUTHORING vs REVIEW modes are not interchangeable.**

* Every QA prompt MUST declare its mode as one of:  
    
  * AUTHORING: runbook or PO instructions.  
      
  * REVIEW: receipt or verdict; evidence evaluation.


* The agent MUST output only the mode’s required structure.  
    
* If the prompt mode is REVIEW, the agent MUST NOT produce new runbooks or commands, except for the REVIEW-mode remediation exception where commands are copied verbatim from the plan or recorded caveats.

**Workflow recommendation (non-normative; strongly advised). Mode enforcement gate.**

* Enforce mode with a mechanical gate (header token plus required section list).  
    
* If the required sections do not match the declared mode, fail fast.

**Rule (QoS escalation stop-rule; normative).**

* If an epic QA plan requires repeated structural remediation for the same failure mode (template semantics, artifact map source-of-truth, prompt-family mode churn), the process MUST escalate from incremental plan edits to a systems RCA plus template and canon update.  
    
* Default escalation threshold (plan↔evidence mismatch count): if more than 3 plan↔evidence mismatches occur in a single epic QA run, STOP and do RCA plus template and canon update, not additional plan addenda.  
    
* Canon update MUST target the class of failure, not the individual incident.

### **9.8.4 Interaction with existing evidence rails (titles-only)**

* For steps intended for external AI review, Deliverables lists must still respect any existing evidence batching constraints defined in the QA process and evidence policy (titles-only in **Glow QA Guide** and **HDE Epic-Process Guide**).  
    
* For HTTP-centric steps, any required derived review artifacts (for example, AI-readable summaries) must be explicitly listed in Deliverables alongside canonical local evidence.  
    
* Any environment or rails verification step (pins, refusal posture, gating proofs) **MUST** write its result to named files under `audit/qa/**` and those files must appear in the Deliverables list for the step.

# 10\. Transport Governance (Reader) \[Required-Now\]

## **10.0 Canonical Reader surfaces and proof-route posture \[Required-Now\]**

**Rule (normative).** The canonical Reader HTTP surface is `GET /reader`.

* If the Reader blueprint is mounted under `/api`, `GET /api/reader` is an alias of the same contract. It is not a distinct surface with distinct semantics.

* Reader proof-surface selection is performed via query parameter versioning (for example `v=1`), not by inventing path segments.

**Rule (normative).** The Aux Narrative HTTP surface is `GET /aux/narrative` (and `GET /api/aux/narrative` only when the Aux blueprint is mounted under `/api`).

**Prohibition (normative).** The route `/api/reader-proof/v1` does not exist and MUST NOT be referenced in catalogs, plans, or transport proofs. Proof routes MUST be selected from the actual configured mount and the endpoint catalog outputs (when used).

**Rule (normative).** When a proof or Live QA plan needs a Reader or Aux route, it MUST:

* name the canonical route (`/reader` or `/aux/narrative`), with `/api/**` used only when that is the configured mount

* capture evidence from the real route surface, not from an invented substitute

**Governed Reader success-proof-surface designation (normative).** The canonical Reader route named above, including `/api/reader` only when `/api` is the configured mount, is the governed Reader success-proof surface for Reader transport proof selection and related QA interpretation.

* Governance MUST NOT require a second designation carrier, a second inventory home, a new route, or a new flag to recognize that surface.  
* If the Endpoint Catalog row for the canonical Reader route remains present and A7-eligible but the inventory or readout still does not make that governed proof-surface status explicit, treat that omission as catalog or canon drift to be drained. It is not a reason to block proof-surface determination, invent a substitute proof route, or widen remediation into runtime or writer work.  
* Supplemental dev-harness, preview, or lookup captures do not create a second Reader proof surface. Reader A7 proofs remain bound to the cataloged JSON success route, and `/internal/version` remains ops-only and excluded from A7.

## 10.1 Success (200) matrix \[Required-Now\]

 **Purpose (normative).** Govern the required headers and body properties for a **200 OK** Reader response on a **Catalog JSON success** route. These are governance rules; transport bytes and concrete route lists live by title in **HDE-CLI-API-Vendor-Ref** and are validated via **A7** acceptance tokens (§2.0). **A7 proofs run on a Catalog JSON success route; `/internal/version` is excluded.**

### Headers — required

* **Content-Type: application/json; charset=utf-8** — UTF-8 JSON; BOM/ANSI-free.  
* **ETag: "\<strong, quoted\>"** — identity over the **final LF-terminated canonical JSON** body (pre-compression); encoding-invariant.  
* **Vary: Authorization, Accept-Encoding** — required; additional Vary members allowed.  
* **Content-Length: \<len(identity 200 body)\>** — required; equals the identity 200 body length (final LF-terminated canonical JSON; pre-compression); encoding-invariant.  
* **Cache-Control: private, max-age=0, must-revalidate** — required on 200 success.

### Body — success covenant

* **Six keys exactly.** Top-level object contains only: **reader\_version, eligible, categories, meta, release\_id, idempotence\_hash**.  
* **Categories policy (v1).** `categories[*]` are exactly **{ id, band }** (numeric-free). If `eligible == true` in v1 Alpha, a single `{"id":"harmony","band":…}`; if `eligible == false`, `[]`.  
* **Serialization.** Canonical emitter: UTF-8, **sorted keys**, compact separators, **exactly one trailing LF** (`\n`).  
* **Idempotence coupling.** `idempotence_hash = sha256(preimage_bytes)` where the preimage fields are defined in **HDE-Math-Spec** (do not restate here). **Re-serialize canonically after insertion.**

**Acceptance (binary gates)**

1. **Headers present and correct.** `Content-Type`, `Content-Length`, **quoted strong** `ETag`, `Vary: Authorization, Accept-Encoding`, and `Cache-Control: private, max-age=0, must-revalidate` are present.  
2. **Body covenant.** Six keys only; `categories[*] == { id, band }`; LF-terminated; canonical serialization.  
3. **Idempotence re-check.** Remove `idempotence_hash`, canonicalize the **HDE-Math-Spec** preimage, and verify `sha256(preimage_bytes)` equals the published hash.  
4. **Encoding invariance.** Identity (`ETag`) is unchanged by `Accept-Encoding` selection for the same body.  
5. **No `no-store` on success.** Confirm `Cache-Control: no-store` is **absent** on 200 success (reserved for writers/errors).  
6. **Tokens:** see §2.0 **Reader A7** and **READER\_\*** tokens.

## 10.2 Conditional delivery \[Required-Now\]

 **Purpose (normative).** Define when and how conditional responses are served on a **Catalog JSON success** route. Governance rules live here; transport bytes live by title in **HDE-CLI-API-Vendor-Ref**. **A7 proofs run on a Catalog JSON success route; `/internal/version` is excluded.**

### **304 Not Modified — only after a prior 200-with-body**

* **Precondition.** A prior 200 success with a **strong, quoted ETag** exists, and the request presents a matching `If-None-Match`.  
* **Body.** None.  
* **Headers.**  
  * `ETag` present (matches the cached 200\)  
  * Mirror 200 validators (`Cache-Control`, `Vary`)  
  * **Omit `Content-Type`**  
  * **Omit `Content-Length`**  
* **No writers/errors.** 304 is **never** used for writer or error responses (writers/errors use `Cache-Control: no-store` and carry **no `ETag`**).

### **HEAD parity — headers mirror 200; no body**

* **Header parity.** HEAD returns the same validators as GET for the same resource (**strong quoted ETag**, `Vary`, `Cache-Control: private, max-age=0, must-revalidate`, and `Content-Type` identical to GET).  
* **Body/length.** No body; **`Content-Length == len(identity 200 body)`** (canonical LF-terminated bytes, pre-compression).  
* **Encoding invariance.** Choice of `Accept-Encoding` does not change identity (`ETag`) for the same body.

### **Acceptance (binary gates)**

1. **304-after-200.** Server returns 304 only when a prior 200-with-body exists and `If-None-Match` matches the strong, quoted `ETag`; 304 carries **no body**, mirrors validators, and **omits** `Content-Type` **and** `Content-Length`.  
2. **HEAD parity.** Headers mirror 200; **no body**; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
3. **Invariant identity.** `ETag` is stable across encodings for the same body.  
4. **No misuse.** 304 is **never** used for writers/errors; those responses are governed by `no-store` and **no `ETag`**.

**Tokens:** see §2.0 **Reader A7** tokens.

---

## 10.3 Writers and errors \[Required-Now\]

 **Purpose (normative).** Govern headers and body shape for writer and error responses. Governance rules live here; transport bytes live by title in **HDE-CLI-API-Vendor-Ref**. Writers/errors are **no-store** and **not** part of A7 success proofs.

**Acceptance-bound writer proof families (normative).**

* When writer-surface completion is claimed for acceptance, the governed proof family MAY include writer envelope proof, writer idempotence proof, write and readback parity proof, writer evidence-indexing proof, and explicit confirmation that writer surfaces remain outside A7 success proofs.

* Any writer proof generator or harness MUST NOT silently force open rails. If open rails are required for a writer proof path, they MUST be supplied explicitly by the caller and treated as part of the declared proof posture for that run.

* Any writer proof generator or harness MUST pin every environment field that can influence emitted writer bytes. Omitting byte-affecting env fields is non-conforming.

* Writer-surface proof generation MUST NOT widen the writer contract or widen the A7 proof surface. A writer proof path may validate writer behavior, but it does not convert writer surfaces into A7 success routes.

* When writer evidence-indexing proof is part of acceptance, the writer proof family and its governed index or path-proof companions MUST remain internally coherent as one acceptance-bound evidence family.

### **Headers — required**

* **Writers and errors:** `Cache-Control: no-store` (**MUST**).  
* **Errors only:** `Content-Type: application/json; charset=utf-8`.  
* **Writers and errors:** **no `ETag`** (identity caching does not apply).

### **Body — typed error shape (errors only)**

* **Shape.** Typed, numeric-free error object (see CLI/Reader error model):  
   `{"ok": false, "code": "<TOKEN>", "error": "<non-PII message>"}`.  
   Optional `retry_after_ms` (integer ≥ 0\) only under a pinned vendor rate-limit policy.  
* **Serialization.** Canonical emitter (UTF-8, sorted keys, compact separators), **exactly one trailing LF**.  
* **No payload echo.** Do **not** include vendor payloads, header values, or secrets.

### **Writers (success-without-body semantics)**

* **No body required.** Writers commonly return **204 No Content**. If a body is emitted for diagnostics, it must remain **typed, minimal, numeric-free,** and **canonically serialized**.  
* **Always no-store.** Caching must be disabled. **Never** send an `ETag`.

### **Writers — OPTIONS/HEAD semantics (normative)**

* **OPTIONS → 204 (no body).** Writers’ OPTIONS responses **must** return 204 with no body; **forbid** `ETag`/`Vary`/compression. Under HTTP/2, `Content-Length: 0` may be omitted.  
* **HEAD 405 (strict).** Writers’ HEAD on non-HEAD writers is **405**; when emitted, include `Content-Length: 0`.

### **Acceptance (binary gates)**

1. **Headers.** `Cache-Control: no-store` present on writers and errors; **no `ETag`**; errors include `Content-Type: application/json; charset=utf-8`.  
2. **Errors.** Body is a typed, numeric-free error object; canonical emission; one LF; **no secrets/PII**.  
3. **Writers.** If body is absent, transport is compliant. If present, it honors the numeric-free covenant and canonical emission.  
4. **No misuse of 304\.** Writer and error responses **must not** use 304; conditional delivery applies **only** to cached 200s (see §10.2 and §2.0).  
5. **OPTIONS (writers).** 204, no body; under HTTP/2 `Content-Length: 0` may be omitted; **no** `ETag`/`Vary`/compression.  
6. **HEAD (writers).** Non-HEAD writers return 405 with `Content-Length: 0`.

**Tokens:** see §2.0 **Writer/Error & rails** tokens, including `WRITERS_OPTIONS_204_NO_BODY_OK`.

---

## 10.4 Aux Narrative suppression (carve-out) — Reader scope note

 **Purpose (normative).** Define the suppression behavior for the **Aux Narrative** surface **without changing** the Reader matrices.

**Behavior.**  When text is present: 200 text/plain; charset=utf-8 with a strong, quoted ETag and Vary: Authorization, Accept-Encoding. When suppressed: 200 with an empty body and no ETag; Vary: Authorization, Accept-Encoding is still present. A policy header may be present as a generic signal (X-Narrative-Policy: suppressed). This carve-out applies only to Aux Narrative. Reader transport rules in §10.1–§10.3 remain unchanged and are fully governed by A7 (success on Catalog routes only). Aux HEAD and 304 are out of scope for EPIC-010.

**Acceptance (binary)**

1. **Suppression case.** Header snapshot shows `200`, **no body**, **no `ETag`**.  
2. **Non-suppressed cases.** Reader responses continue to meet **§10.1–§10.3**.

**Evidence (titles-only).** Add a **suppression header snapshot** entry in PF12 (update **human** `docs/evidence/INDEX.json` \+ **hash sentinel** and **machine** `artifacts/evidence_index.jsonl` **in the same PR**).

**Tokens (titles-only).** `AUX_A7_GET_QUOTED_ETAG_OK` · `AUX_A7_HEAD_PARITY_OK` · `AUX_A7_304_OMITS_CT_CL_OK` · `AUX_200_SUPPRESS_EMPTY_NO_ETAG_OK`.

---

## **10.5 `/internal/version` ops surface (identity only; non-A7) \[Required−Now\]**

#### **Intent and scope**

`/internal/version` is an **ops-only identity route**, used by operators to inspect the running release identity. It is **not** a public Reader success route, and **A7 does not apply**. A7 transport proofs run only on the Endpoint Catalog JSON success surface (see HDE-CLI-API-Vendor-Ref and HDE-Schemas and Artifacts by title).

**nterim auth posture (operator-network-only; token auth deferred).**

* **Interim posture (now).** `/internal/version` has **no application-layer auth**. It is treated as **operator-network-only**: access is restricted by operator-controlled network and service configuration (owned outside this document by titles-only single homes).

* **Runbook restriction (non-negotiable until token auth exists).** Runbooks, remediation guides, and operational tooling MUST NOT require an auth header for `/internal/version`. If an auth header is mentioned, it MUST be explicitly labeled **optional** and treated as **Observed Evidence (non-PF)** only.

* **Non-canonical language guard.** Any document language that implies “auth required” for `/internal/version` is non-canonical unless/until the implementation exists and is canonized via Doc-Delta.

* **Future hardening (deferred).** A future epic may introduce an auth-gated token header with explicit 401/403 behavior. Until that epic lands, the interim operator-network-only posture governs.

---

#### **Methods and status**

* `GET /internal/version` and `HEAD /internal/version` **always return 200** on success.

* Conditional request headers (`If-None-Match`, `If-Modified-Since`, and similar) are **ignored**; `/internal/version` **never returns 304**.

* `HEAD /internal/version`:

  * Returns `200` with the same validators as `GET` (where present).

  * May carry `Content-Length` equal to `len(identity GET body)` (LF-terminated bytes).

  * Has an empty body.

---

#### **Headers and caching**

* All successful responses **must** include:

  * `Cache-Control: no-store`.

  * **No** `ETag`.

  * **No** `Last-Modified`.

* `Vary` is optional on this surface (it may be present but is not required for acceptance).

---

#### **Payload (frozen minimal identity)**

The JSON body is a **frozen minimal identity envelope**. It exposes exactly **six** provenance fields and **no extras**:

* `engine_tag`

* `build_commit`

* `invocation_tag`

* `invocation_sha256`

* `emitter_sha256`

* `release_id`

The body is emitted via the **canonical JSON serializer** and must satisfy:

* UTF-8 encoding (no BOM).

* **Fixed key order:** the six fields **must appear in the order listed above**, with no additional top-level keys. For `/internal/version` this fixed ordering is **normative** and is the sole exception to the global “sorted keys” rule for canonical JSON.

* Compact separators and exactly one trailing `\n` (LF).

All other canonical JSON rules (no BOM, LF-termination, deterministic bytes under closed rails) still apply; only the general “ASCII-sorted keys” requirement is relaxed here in favor of this fixed identity field order.

---

#### **Acceptance (binary gates)**

Names-only; token semantics live in this document, bytes and tests live elsewhere by title.

**Proof surface invariants (explicit checklist; minimum set).**  
 Any remediation guide, QA step, or probe tool that produces governed `/internal/version` evidence MUST explicitly enumerate and verify these invariants. It is not acceptable to imply these checks by referencing PF sections only.

A. Transport

* `GET` MUST return 200\.

* `HEAD` MUST return 200 and satisfy parity expectations.

* Conditional requests (`If-None-Match`, `If-Modified-Since`) MUST NOT yield 304; they MUST return 200\.

B. Headers

* `Cache-Control: no-store` MUST be present.

* `Content-Type: application/json; charset=utf-8` MUST be present (and satisfy GET↔HEAD parity expectations).

* `ETag` MUST be absent.

* `Last-Modified` MUST be absent.

C. Body (identity payload)

* Body MUST be fixed-schema JSON with exactly these keys (no extras): `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`.

* Body bytes MUST satisfy the canon “identity bytes” posture (including LF termination) where applicable to the proof surface.

**Token emission gating (no “false OK”).**

* A tool MUST NOT emit any `*_OK` token unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run.

* If the run status is `FAIL_TOOLING` (or equivalent failure), the tool MUST NOT emit `*_OK` tokens for invariants that did not pass. In particular, it MUST NOT emit integrity-success signals (for example, path-proof match or two-run identity) unless those checks demonstrably passed on the produced artifacts.

* Coupling requirement (anti-mixed-target / anti-redirect drift): for each probe run, the evidence must be coupled such that the emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit `*_OK` tokens.

*Applicability:* These rules apply equally to DEV and OPS steps when they produce governed `/internal/version` evidence.

* **INTERNAL\_VERSION\_200\_CTYPE\_JSON\_UTF8\_OK**  
   `GET /internal/version` 200 includes `Content-Type: application/json; charset=utf-8`.

* **INTERNAL\_VERSION\_HEAD\_PARITY\_OK**  
   `HEAD /internal/version` returns 200; mirrors GET validators; empty body; `Content-Length == len(identity GET body)`; `Content-Type == GET`.

* **INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK**  
   `If-None-Match` / `If-Modified-Since` are ignored; on success, the route always returns 200 (never 304).

* **INTERNAL\_VERSION\_NO\_ETAG\_OK**  
   No `ETag` on `GET` or `HEAD`.

* **INTERNAL\_VERSION\_NO\_STORE\_OK**  
   `Cache-Control: no-store` is present on `GET` and `HEAD`.

---

#### **Evidence and A7 separation**

`/internal/version` is **not** an A7 proof surface. A7 transport proofs run only on the Endpoint Catalog JSON success route owned by **HDE-CLI-API-Vendor-Ref** and indexed in **HDE-Schemas and Artifacts**.

Evidence for `/internal/version` is records-only and titles-only at this level; bytes and schemas live in **HDE-Schemas and Artifacts** and **Glow QA Guide**.

**No extra governed narrative artifacts.** The governed `/internal/version` evidence surface is exactly the canonical bundle enumerated below plus its required indexing and path proofs. Do not introduce additional governed narrative artifacts for this surface (for example, a `provenance_note.md`) unless a Doc-Delta explicitly registers the new evidence surface and the evidence catalog defines it.

**Filenames (canonical set \+ permitted aliases).**  
 The canonical filename set for the `/internal/version` evidence bundle is registered in **HDE-Schemas & Artifacts** (titles-only). This section lists the governance-required bundle contents; where filename expectations differ across consumers during a drain window, the following posture applies:

* Live QA MUST produce the canonical filenames.  
* Live QA MAY additionally emit alias copies for compatibility. The only permitted aliases at this level are the conditional header snapshot filenames listed in this section (`cond_if_none_match_headers.txt` and `cond_if_modified_since_headers.txt`) when the canonical filenames differ elsewhere.  
* Evidence indexing MUST bind to the canonical filenames; alias files are compatibility-only and MUST be byte-identical to the canonical artifacts they mirror.  
* No other filename variants are permitted.

**Evidence artifacts (canonical paths; records-only):**

* `artifacts/ops/internal_version/body_get.json` — exact `GET` body bytes (LF-terminated; six keys; fixed identity-field order).  
* `artifacts/ops/internal_version/body_get.sha256` — SHA-256 sidecar for the exact `body_get.json` bytes.

* `artifacts/ops/internal_version/headers_get.txt` — raw `GET /internal/version` response headers (must include the HTTP status line and header lines).  
* `artifacts/ops/internal_version/headers_head.txt` — raw `HEAD /internal/version` response headers (must include the HTTP status line and header lines). If capture tooling emits non-header diagnostic lines, validators must ignore lines that are not a status line or `Key: value` header lines.  
* `artifacts/ops/internal_version/headers_cond_if_none_match.txt` — `GET` with `If-None-Match` (still 200; conditionals ignored). (Legacy alias permitted only when explicitly required: `cond_if_none_match_headers.txt`.)  
* `artifacts/ops/internal_version/headers_cond_if_modified_since.txt` — `GET` with `If-Modified-Since` (still 200; conditionals ignored). (Legacy alias permitted only when explicitly required: `cond_if_modified_since_headers.txt`.)  
* `artifacts/ops/internal_version/request_chain_manifest.json` — deterministic request-chain manifest for the `/internal/version` proof surface (indexable/mirrored as a primary artifact with a co-located path proof).  
* `artifacts/ops/internal_version/two_run_identity.log` — two-run byte identity log for the body, including the coupling verification result described in this section.

Indexing requirements:

* For each artifact above:

  * Add a titles/paths entry in `docs/evidence/INDEX.json` and update `docs/evidence/INDEX.sha256`.

  * Add or update a Machine Mirror record in `artifacts/evidence_index.jsonl` with:

    * `artifact_key`,

    * `discovered_physical_path`,

    * `produced_at_utc`,

    * `proof_anchor` (path to the co-located `*.path_proof.txt`),

    * `role`, `sha256`, `size_bytes`.

* Mirror rules (single file, canonical JSONL, sorted keys, unknown-key rejection) and path-proof schema are defined in **HDE-Schemas and Artifacts**; PF04 governs only the token and routing semantics.

---

#### **Routing (titles-only)**

* Contract bytes (examples and schema) for `GET /internal/version` live in **HDE-CLI-API-Vendor-Ref**.

* Operational policy, acceptance tokens, and runbook semantics live here in **HDE-Governance**.

* Evidence artifacts and their indexing rules live in **HDE-Schemas and Artifacts** and **Glow QA Guide** (names-only at this level).

#### **Coupling proof (two-run identity \+ identity coupling) \[Required−Now\]**

For any epic that claims `/internal/version` identity coupling and/or two-run identity closure, the governed proof artifact is a single log:

* `artifacts/ops/internal_version/two_run_identity.log`

* `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt`

This log MUST include, at minimum:

* **Two-run identity result:** an explicit statement that two consecutive invocations produce byte-identical identity output (or not), including the compared digests/byte identifiers.

* **Coupling verification result:** explicit pass/fail checks that the `/internal/version` identity is coupled to the required identity sources by title/path reference, including release identity coupling where applicable.

* **Rails posture \+ determinism pins reference:** names-only pointers to the applicable rails posture and determinism pins evidence surfaces (the determinism pins themselves remain proven by their canonical log).

No new acceptance tokens are introduced for “coupling proof.” This evidence is bound under the existing internal-version acceptance posture. Acceptance artifacts MUST bind coupling claims to this log (and other required governed identity artifacts) rather than inventing new token names or alternate proof artifacts.

---

#### **Prod QA note**

In production, `/internal/version`:

* Returns `application/json; charset=utf-8`.

* Uses `Cache-Control: no-store`.

* Never emits `ETag` or `Last-Modified`.

* Ignores conditional request headers (`If-None-Match`, `If-Modified-Since`); never returns 304\.

* Ensures `HEAD` 200 mirrors GET validators and may carry `Content-Length == len(identity GET body)` with an empty body.

# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**

## **11.1 Request shaping (owned here) \[Required-Now\]**

**Scope (normative).** This section pins the bytes used to construct HDAPI requests and to remap provider outcomes into typed, numeric-free errors. Rails posture (open/closed) is governed in §3; live-call behavior (timeouts/retries/backoff) is in §11.2.

**HDAPI v2 conformance pending governance posture.** Until the vendor v2 conformance work is implemented and evidenced, HDE vendor architecture MUST be treated as legacy, partially conforming, or pending v2 conformance, not v2-conformant. Documentation consolidation, vendor research, or contract inventory alone MUST NOT be used as runtime conformance proof.

Existing SAFE rails, no-I/O refusal, typed error, keys-only logging, evidence-indexing, public Reader v1, and PO-only open-rails posture apply to HDAPI v2 vendor work. Plans, implementation guides, QA plans, reviews, acceptance maps, and closeout artifacts MUST distinguish contract-inventory proof, architecture update, closed-rails shaping proof, and PO-only open-rails vendor smoke.

**HDAPI v2 response-envelope proof posture.** Response-envelope mapping proof may show that a governed vendor response shape preserves response type, success status, error-code posture, data identity posture, and route variant. That proof is not by itself a normalized-data-path proof, downstream BodyGraph compatibility proof, live vendor conformance proof, public Reader proof, open-rails smoke proof, or AI transformation proof.

Response-envelope evidence must be governed, closed-rails unless explicitly scoped otherwise, and secret-safe. It MUST NOT persist raw vendor payload bodies, raw request bodies, raw response bodies, plaintext secrets, or unbounded vendor excerpts. If a schema or compatibility gap remains between chart data and existing internal BodyGraph-compatible flows, the evidence must record the gap plainly and MUST NOT hide it by inference.

**ChartResult and ChartSimpleResult adapter/schema gap posture.** A governed evidence slice may truthfully record that ChartResult or ChartSimpleResult adapter/schema mapping remains incomplete. That gap record may support a bounded evidence or planning posture, but it MUST NOT be reused as proof that v2 chart data already feeds the existing BodyGraph cache, person/bodygraph compute input, compatibility helpers, Glow app integration, or full HD Engine runtime conformance.

ChartSimpleResult may be used for bounded live smoke, authentication proof, geocode-key proof, provider availability proof, or minimal route-family confirmation when those are the explicitly scoped proof targets. ChartSimpleResult MUST NOT be treated as sufficient for the full BodyGraph/person/cache contract unless a future governed adapter/schema proof demonstrates that it contains every required field and that the HD Engine maps those fields into the normalized internal contract without uncontrolled raw payload persistence.

Future runtime, production, app-integration, or BodyGraph-resolution claims require a bounded adapter/schema proof or implementation. That proof must identify the vendor payload family used, the response fields required, the internal BodyGraph/person/cache fields populated, the fields intentionally absent or unsupported, whether the adapter is sufficient for HD Engine compute, whether any legacy fallback remains, whether raw vendor payloads are persisted, redacted, summarized, or excluded, and what normalized internal output contract is produced. The proof must remain governed and secret-safe.

No vendor-v2-specific acceptance token may be claimed unless it exists in §2.0 or has been minted in PF10 pending drainage. HDE-FERM006 through HDE-FERM008 consume existing Governance tokens unless Governance explicitly registers a new token. If a future AI-related token is proposed, it is a separate PO-approved product decision outside HDAPI v2 conformance.

**Future Glow app integration boundary.** HumanDesignAPI vendor acquisition, request shaping, auth/header handling, vendor response normalization, BodyGraph persistence and retrieval, and HD Engine computation remain HD Engine-governed responsibilities unless a future PF10 addendum or permanent PF canon explicitly approves a narrower exception. Glow app integration may request or consume HD Engine outputs through controlled integration surfaces, but it must not create a parallel HumanDesignAPI client, parallel credential path, parallel vendor request-shaping layer, parallel BodyGraph normalization layer, or direct app-side raw vendor persistence path by assumption.

HumanDesignAPI credentials, geocode credentials, raw vendor auth headers, raw vendor request payloads, and raw vendor response payloads remain inside the HD Engine infrastructure and governance boundary unless an explicit future data contract authorizes a different exposure with security, privacy, evidence, and public/private-surface proof. App-facing or public-facing surfaces must receive normalized, app-safe outputs rather than ungoverned vendor secrets or raw vendor payloads.

This conformance work does not authorize OpenAI, LLMs, AI agents, prompts, embeddings, chatbots, model calls, AI-provider credentials, AI-specific rails, AI evidence families, AI QA obligations, or Glow App AI features. Vendor AI/LLM-oriented documentation, including documentation-discovery files, may be used only as documentation-structure context and MUST NOT be interpreted as product or runtime scope.

**HDAPI vendor boundary-proof governance.** A vendor-seam boundary proof is structural validation, not runtime conformance. It must prove that the vendor seam does not create a new HTTP home, bypass adapter guards, bypass the presenter boundary, introduce ad-hoc serialization, authorize external I/O inside pure compute modules, or silently change public Reader routes or public payloads.

Boundary proof models must be conservative and fail closed. Unknown, unsupported, ambiguous, or unclassified current boundary behavior MUST NOT render as PASS. Public-route drift, presenter provenance drift, serializer drift, guard-provenance drift, external-I/O drift, evidence-family binding drift, or unsupported-scope claims must be classified explicitly before any PASS or supportable language may be used.

A proof-model failure is a validation failure even when no live runtime failure has been proven. Boundary-proof evidence may support a later-drain or review posture only when it preserves its own non-claim boundaries and does not claim live vendor conformance, open-rails success, public Reader expansion, PF09 status movement, acceptance-token satisfaction, epic closure, or PF-canon drainage by itself.

V2 endpoint bytes, auth names, request-body rules, response envelopes, rate-limit behavior, error mapping, and legacy-v1 fallback policy remain pending until their owning PF homes and governed evidence bind them. Existing v1 BodyGraph request shaping in this section MUST NOT be cited as v2 request shaping.

### **11.1.1 Vendor route family, resource path, and base URL posture**

* **Base URL resolution:** `HD_API_BASE_URL` is canonical. `HDAPI_BASE_URL` is deprecated compatibility spelling only where implementation or migration evidence explicitly records it. If both names are present with different values, the provider must fail closed with configuration ambiguity before network I/O.  
* **Configured API-version boundary:** the vendor API version belongs to the configured base URL, not to hardcoded runtime route constants. Runtime request construction must append version-neutral resource paths only and must preserve any path prefix already present in `HD_API_BASE_URL`.  
* **Governed resource paths:** current vendor request shaping distinguishes legacy BodyGraph resources `bodygraphs` and `bodygraphs/simple` from chart resources `charts`, `charts/simple`, and `charts/coordinates`. Legacy BodyGraph resources use the legacy BodyGraph auth posture. Chart resources use the Bearer auth posture.  
* **Determinism:** URL construction is order-neutral and locale-neutral. Auth family must be represented by governed route metadata or contract metadata, not inferred from string checks for vendor API-version path segments.

**`bg:resolve --source vendor` route-policy governance.** `bg:resolve --source vendor` remains an HD Engine workflow for resolving BodyGraph details. Future claims that this workflow works as a canonical vendor-backed BodyGraph-resolution path require an explicit vendor-route policy. The policy must classify the selected behavior as v2 chart-backed BodyGraph resolution, explicit legacy BodyGraph fallback, dual-route policy, or unsupported nonclaim.

`bg:resolve --source vendor` MUST NOT accidentally compose a legacy BodyGraph resource path against a configured v2 base URL and then treat the result as provider unavailability, full v2 runtime conformance, or acceptable final behavior. If the configured base URL is v2, appending a legacy BodyGraph resource is allowed only when vendor evidence and PF10 or permanent PF canon explicitly support that combination. If both v1 and v2 route families are required at runtime, the base-url and route-family configuration strategy must be defined explicitly and kept secret-safe.

Simple chart success may prove provider reachability, v2 auth posture, geocode-key posture, or route-family availability only when those are the scoped proof targets. It MUST NOT be treated as proof that `bg:resolve --source vendor` resolves complete BodyGraph data, feeds the BodyGraph/person/cache contract, replaces legacy BodyGraph ingest, or supports full vendor runtime conformance.

**Mapped-cache persistence boundary.** Scoped dry-run or evidence-flow proof that a configured-v2 chart route can be requested, mapped into HDE internal BodyGraph/person/cache/compat shape, and used for bounded compatibility evidence does not authorize durable BodyGraph cache persistence. Until a future governed implementation slice proves mapped-cache persistence, configured-v2 non-dry-run writes MUST remain fail-closed.

A future mapped-cache persistence slice MUST NOT simply turn on writes. It must design and prove a safe persistence path that writes adapter-mapped HDE data, not raw HumanDesignAPI v2 envelopes, raw vendor response bodies, raw request bodies, plaintext secrets, or uncontrolled vendor payloads. The proof must cover mapped-cache write, mapped-cache read-back, canonical-equivalence between pre-write mapped output and post-read cached output for governed fields, idempotence for repeated writes of the same normalized identity, no raw vendor-payload persistence, closed-rails refusal before outbound I/O, and preservation of explicit legacy fallback behavior.

Production persistence requires an additional authorization boundary. The safe path is dry-run evidence, then mapped-cache write and read-back proof, then controlled non-prod repeatability, then an explicit production authorization decision. Do not skip from configured-v2 dry-run evidence directly to production persistence, production upsert reopening, or durable reusable user BodyGraph data.

### **11.1.2 Auth and geocode header posture**

Send only governed header families for the selected route family; do not add other vendor auth headers unless explicitly pinned here or in the owning byte-contract home:

* `Accept: application/json`  
* `Content-Type: application/json; charset=utf-8`  
* `HD-Api-Key: REDACTED` for legacy BodyGraph resources only  
* `Authorization: Bearer REDACTED` for chart resources  
* `HD-Geocode-Key: REDACTED` when the governed route requires geocoding  
* `User-Agent: GlowHDEngine/RELEASE_ID` where RELEASE\_ID is derived from §5.1

**Redaction:** header names and redacted header shapes may be recorded. Raw header values, raw Bearer token values, raw API key values, raw geocode key values, request bodies, response bodies, and vendor payload dumps MUST NOT be logged or persisted except inside an explicitly approved governed evidence shape.

**Auth-family mismatch posture:** using `HD-Api-Key` for chart resources, using Bearer auth for legacy BodyGraph resources, omitting required geocode header posture, blurring the environment-variable name with the outbound header name, or deriving auth from a vendor API-version string is a governance-relevant request-shaping and secret-safety defect when it affects live vendor behavior, open-rails smoke, QA evidence, or acceptance claims.

### **11.1.3 Request body schema (exact three keys) \[Required-Now\]**

**Normative rule.** The request **MUST** contain exactly three top-level fields—no others—and they **MUST** be formatted as follows:

1. {"birthdate":"DD-MMM-YYYY","birthtime":"HH:MM","location":"City, Country"}  
     
* **birthdate** — English month abbreviations `Jan..Dec`; day zero-padded (`01..31`); four-digit year. Examples: `03-Jan-1980`, `21-Sep-1995`.  
* **birthtime** — 24-hour `HH:MM`; zero-padded hour and minute (`00..23`, `00..59`). Examples: `00:00`, `09:30`, `23:59`.  
* **location** — ASCII English `"City, Country"`; a **single** comma \+ space separator; no leading/trailing spaces. Examples: `Paris, France`, `New York, USA`.

**Do not send `tz`.** The vendor derives timezone from location via geocoding; any `tz` field **MUST NOT** be present.  
 **Determinism.** Body construction is order-neutral (AB↔BA) and locale-neutral; no floats, wall-clock, or platform-dependent formatting.

**Validation & failure posture.**

* If any field is missing, extra, or malformed, the client **MUST** fail locally with a **typed, numeric-free error** (LF-terminated) and **MUST NOT** attempt network I/O.  
* Whitespace and casing rules above are normative; violations are treated as schema errors.

  ### **11.1.4 Typed error mapping (provider → CLI/Reader)**

Provider outcomes **MUST** be remapped to these typed, numeric-free errors (no vendor payload echo):

* **401 → `PROVIDER_UNAUTHORIZED`**  
* **403 → `PROVIDER_FORBIDDEN`**  
* **404 → `PROVIDER_NOT_FOUND`**  
* **429 → `PROVIDER_RATE_LIMITED`**  
  * If a valid `Retry-After` header is present, deterministically parse (delta-seconds or RFC-date) to integer `retry_after_ms`; on invalid/unsupported header, omit the field.  
* **5xx → `PROVIDER_UNAVAILABLE`**  
* **Malformed / bad JSON → `PROVIDER_BAD_RESPONSE`** (schema/mapping failure)

**Emission.** Error objects are serialized by the **single presenter emitter** and LF-terminated (see A-gates and transport rules).

### **11.1.5 Rails coupling (pointer)**

* **Rails closed (default; §3.1):** perform **no network I/O**; it is permissible to compute deterministic shaping (URL/headers/body) for diagnostics, but return a **typed refusal** and keep logs secret-free (keys-only).  
* **Rails open:** request shaping remains identical; live-call policy is pinned in §11.2.

  ### **11.1.6 Acceptance (binary)**

To pass governance:

1. **Shaping is canonical:** endpoint, headers, and body exactly match §§11.1.1–11.1.3; order-/locale-neutral construction.  
2. **Typed mapping proven:** provider statuses remap only to the tokens above; optional `retry_after_ms` is parsed deterministically.  
3. **Logging hygiene:** no payloads or header values; secrets redacted; labels bounded (per §7.1/§8.2).  
4. **A-gates unaffected:** Reader↔CLI parity and idempotence (A3/A4) remain unchanged by vendor paths.  
5. **Evidence:** index redacted examples/mapping tests in Appendix D (titles/paths only); keep synchronized with repo changes.  
   ---

## **11.2 Live call policy \[Speculative\]**

**Scope (normative, draft).** This section defines the closed, deterministic policy for live vendor calls made **only** when rails are open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`). It pins enum domains and governance rules; exact numeric selections are chosen before enablement and recorded via Doc-Delta.

### **11.2.1 Prerequisites & posture**

* **Rails open:** both gates satisfied (see §3.1); required env present/non-empty (see §3.3).  
* **Shaping fixed:** endpoint, headers, and body exactly as in §11.1.  
* **Determinism first:** no locale/time/random dependencies in policy selection; no payload/secret logging (keys-only).

### **11.2.2 Timeouts (closed integers; pick one profile)**

* **Profiles (enum):** `timeout_profile ∈ {small, default, long}`.  
* **Domains (ms):**  
  * `connect_timeout_ms ∈ {1000, 2000, 5000}`  
  * `read_timeout_ms ∈ {2000, 5000, 10000}`  
  * `total_timeout_ms ∈ {5000, 10000, 15000, 30000}`  
* **Rule:** pick **one** profile per environment; no per-request adaptation. Respect `total_timeout_ms` for all scheduling.

### **11.2.3 Retries & backoff (closed, no jitter)**

* **Retries:** `max_attempts ∈ {0,1,2,3}` (includes the first try). Retry classes: `{network_error, 5xx, 429}` only.  
* **Backoff enum:** `backoff ∈ {none, fixed, exponential}`.  
* **Backoff params (ms):**  
  * `fixed_delay_ms ∈ {250, 500, 1000}`  
  * `exp_base_ms ∈ {250, 500}`, `exp_factor = 2`, `exp_ceiling_ms ∈ {1000, 2000, 4000}`  
* **Schedule:**  
  * `none → 0 ms`; `fixed →` repeat `fixed_delay_ms`;  
  * `exponential → min(exp_base_ms * 2^(n-1), exp_ceiling_ms)` for attempt `n ≥ 2`.  
* **Budget:** never exceed `total_timeout_ms`; **no jitter**.

### **11.2.4 429 handling (deterministic)**

* **Typed error:** map to `PROVIDER_RATE_LIMITED` (see §11.1.4); no payload echo.  
* **Retry-After parse:** if present, deterministically parse delta-seconds or HTTP-date → `retry_after_ms` (integer); invalid header → omit the field.  
* **Optional retry on 429:** enabled only when policy pins `retry_on_429=true`; then apply the same backoff and respect `max_attempts` and the total time budget.

### **11.2.5 Observability (non-PII; bounded labels)**

* **Counters/timers/histograms (examples):** `vendor.req_total`, `vendor.req_success`, `vendor.req_error_{class}`, `vendor.retry_attempts`, `vendor.latency_ms` (bounded buckets).  
* **Labels (bounded):** `route`, `outcome ∈ {ok, network_error, 4xx, 5xx, 429}`, `rails_state ∈ {open,closed}`, `timeout_profile`, `attempt_idx`.  
* **Keys-only logs:** never log request/response bodies or header values; secrets always redacted (see §7.1, §8.2).

### **11.2.6 Acceptance to flip rails (controlled integration)**

Before enabling live calls in any environment, a Doc-Delta **MUST** pin the selections and evidence must pass:

1. **Policy pinning:** choose one timeout profile, `max_attempts`, backoff, and 429 handling.  
2. **Redaction tests:** prove logs contain no secrets/payloads; only bounded labels.  
3. **Refusal proof:** with rails closed, show deterministic refusal and correct shaping (no I/O).  
4. **Open-rails conformance:** with rails open, prove success, retry, and 429 paths follow pinned policy; parity/idempotence (A3/A4) unaffected.  
5. **Evidence index:** update Appendix D (titles/paths only) and add a Change Log entry for the pinned selections.

### **11.2.7 Change control**

Any change to selected timeouts/retries/backoff/429 settings, observability labels, or logging posture is a **normative** change and **requires a Doc-Delta**; if the math pack is unaffected, no new `release_id` is needed, but evidence must be refreshed.

# **12\. Gate Suites (Governance Gates) \[Required-Now\]**

## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**

**Anchors.** Use these exact IDs in evidence and Doc-Delta targets: `GATE:CORE-CANON`, `GATE:CORE-DET`, `GATE:CORE-READER`, `GATE:CORE-MATCH`.  
 All gates inherit the serializer and locale pins: UTF-8, sorted keys, compact separators (`,` and `:`), exactly one LF, `LC_ALL=C`, `TZ=UTC`. Any historic prompt or uncertainty checks are retired.

### **GATE:CORE-CANON — Canonical emission and comparators \[Required-Now\]**

**Scope.** Canonical serializer and ordering rules across Reader and CLI. **Pass when (binary):**

* Public bytes are produced by the single presenter/emitter; no ad hoc `json.dumps(`, `jsonify(`, or alternate emitters on public paths.  
* **Objects:** keys ASCII-sorted; compact separators; UTF-8; BOM/ANSI-free; exactly one LF.  
* **Arrays as sets:** dedupe by identity, then ASCII-sort; on value conflict, fail closed.  
* **Environment pins:** `LC_ALL=C`, `TZ=UTC`.  
   **Evidence.** Canonical re-serialize comparison; grep-guards (no `json.dumps` on public paths); LF/encoding checks.

### **GATE:CORE-DET — Determinism and identity \[Required-Now\]**

**Scope.** Idempotence, AB↔BA, two-run identity. **Pass when (binary):**

* **Preimage recipe:** build the preimage (without `idempotence_hash`), canonicalize, verify `sha256(preimage_bytes) == idempotence_hash`; then re-serialize canonically.  
* **AB↔BA identity** (pair normalization) and **two-run identity** hold byte-for-byte.  
* No nondeterminism on public paths from time, locale, randomness, or floating-point behavior.  
   **Evidence.** Preimage recompute logs; AB/BA and two-run byte-compare goldens.

### **GATE:CORE-READER — Public covenant and transport hooks \[Required-Now\]**

**Scope.** Reader v1 public body and A7 transport validators. **Pass when (binary):**

* **Success body:** six keys exactly (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*] == {id, band}` only (numeric-free).  
* **Errors:** typed, numeric-free JSON; canonical emission; one LF; no PII.  
* **Error parity scenarios (deterministic acceptance).** Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor-attempt cases) MUST be reproducible under determinism pins and closed rails, without reliance on external network or a live database. Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts. Allowed fallback: a deterministic stub only to the extent required to produce the canonical error envelope (no live I/O). The acceptance proof MUST consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) with a stable scenario identifier, and Evidence Index \+ machine mirror MUST be updated in the same PR as any new parity artifacts.  
* **Reader↔CLI parity:** bytes equal for identical inputs/environment (same emitter).  
* **A7 hooks present:**  
  * 200 has strong, quoted `ETag`; **Cache-Control: private, max-age=0, must-revalidate**; **Vary: Authorization, Accept-Encoding**.  
  * 304 only after a prior 200-with-body; **no body; omit `Content-Type` and `Content-Length`; validators mirror** the cached 200\.  
  * HEAD mirrors 200 validators; **no body; `Content-Length` equals identity 200; `Content-Type` equals GET**.  
  * Writers/errors: **Cache-Control: no-store** and **no `ETag`**; errors include `Content-Type: application/json; charset=utf-8`.  
  * **POST is non-conditional** (ignore `If-*` conditionals).  
     **Evidence.** Schema/shape tests; Reader↔CLI parity runs; A7 header snapshots.

### **GATE:CORE-MATCH — Compat math posture \[Required-Now\]**

**Scope.** Engine math visible at governance level (design in **HDE Math Spec**, titles only). **Pass when (binary):**

* **Closed sets:** Magic-10 category IDs and order fixed; band thresholds are inclusive maxima.  
* **Validation:** `viewer_prefs.weights` covers all 10 IDs with integers `0..100`; invalid shapes ⇒ typed failure.  
* **Determinism:** AB↔BA and two-run identity hold for internal scoring; fixed-point arithmetic with round away-from-zero and clamp to `[0..100]`.  
* **Public boundary:** no public numerics; Reader v1 remains `{id, band}` only (compat internals do not leak).  
   **Evidence.** Validator tests; fixed-point boundary goldens; proofs of “no public numerics” in success bodies.

**Note.** Any previously listed gate checks for prompt or uncertainty are removed from governance. Those features are retired and must not appear in public payloads or acceptance criteria.

## **12.2 Evidence links (titles-only) \[Required-Now\]**

**Titles and paths only; no payload bytes.** Keep this list synchronized with **Appendix D: Evidence Index** (that index remains the single source of truth). Update both in the same commit/PR when any golden or script path moves.

### **GATE:CORE-CANON — Canonical emission and comparators**

* Tests: `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`  
* Grep-guards and allowlist: `ci/grep-guards/canonical_emitter.allowlist`, `ci/grep-guards/no_json_dumps_public.regex`  
* Schema (success and error shapes): `schemas/reader.v1.schema.json`

### **GATE:CORE-DET — Determinism and identity**

* Goldens (AB↔BA, two-run): `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Idempotence recompute and parity scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Identity marker (preimage → sha256 → final): `artifacts/cards/A3/IDENTITY_OK.txt`

### **GATE:CORE-READER — Public covenant and transport hooks**

* Schema and shape (six-key success; `{id, band}` only): `schemas/reader.v1.schema.json`  
* Reader↔CLI parity (dev harness and tests): `adapter/http_reader.py` (dev-only harness), `tests/reader_v1/test_emitter.py`, `tests/cli/test_cli_stdout_schema_and_lf.py`  
* A7 transport snapshots (validators):  
   `tests/transport/headers/etag_200.snap`,  
   `tests/transport/headers/cond_304.snap`,  
   `tests/transport/headers/head_parity.snap`,  
   `tests/transport/headers/no_store_writers_errors.snap`  
* For internal-ops transport evidence of `/internal/version`, see **Appendix D: D.6** (titles only).

### **GATE:CORE-MATCH — Compat math posture**

* Validation (viewer prefs, closed sets): `tests/validation/viewer_prefs/*`  
* Fixed-point boundary and rounding (away-from-zero; clamp): `tests/compat/fixed_point/*`  
* Band thresholds (inclusive maxima): `tests/compat/bands_thresholds/*`  
* Public numeric ban (no scores on success): `ci/grep-guards/public_numeric_ban.regex`

**Maintenance rule.** Whenever a golden, snapshot, or script path changes, **Appendix D: Evidence Index** **MUST** be updated in the same commit/PR, and add a one-line entry to **§9 Change Management: Doc-Delta Hooks**.

---

# **13\. Versioning & Compatibility \[Required-Now\]**

## **13.1 Reader versioning (v1) \[Required-Now\]**

**Principle (normative).**  
 **Reader v1** is a **strict** public contract. Success bodies contain **exactly six** top-level keys and a **bands-only** `categories` array. Any change that alters this public shape or its semantics is a **versioned change** (Reader v2+).

### **13.1.1 v1 success contract (strict)**

* **Six keys exactly:** `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`.  
* **`categories` items:** **exactly** `{ "id": <string>, "band": <"Cool"|"Open"|"Warm"|"Glow"> }` (numeric-free).  
* **Serialization:** canonical emitter (UTF-8, sorted keys, compact separators), **exactly one** trailing LF; `idempotence_hash` computed over the **five-key** preimage.  
* **v1 Alpha policy:** when `eligible==true`, public `categories` has **one** item with `id:"harmony"`; when `eligible==false`, `categories` **may** be empty.

### **13.1.2 Error contract (typed)**

* **Typed, numeric-free error:** `{ "ok": false, "code": "<token>", "error": "<non-PII message>" }` (+ optional `retry_after_ms` under pinned vendor policy).  
* **Same emitter rules:** canonical JSON; **one** trailing LF; **no** PII/secrets or payload echo.

### **13.1.3 What requires a Reader version bump (v2+)**

* Adding, renaming, or removing **any** top-level success key (beyond the six).  
* Adding **any** field to `categories[*]` (e.g., `score`, `prompt`, keys).  
* Changing the **allowed enum** for `band` or the **public** category exposure policy (e.g., exposing full Magic-10).  
* Changing the **canonical serialization** rules (UTF-8, sorted keys, compact, **one** LF) or the **preimage recipe**.  
* Changing the **typed error** public shape.

### **13.1.4 What does not require a Reader version bump (governed elsewhere)**

* Changing **math internals** (scores, presets, thresholds) while keeping the public v1 payload numeric-free and schema-conformant (may change `release_id`).  
* Changing **transport policy** within A7 (headers/conditional delivery as defined in §10) with no change to public body bytes.  
* Changing **rails** policy for vendor ingest (enablement, timeouts/retries/backoff) with no change to public body bytes.

> These changes still require a **Doc-Delta** and updated evidence; if they alter frozen math, they produce a new **`release_id`** (§5.1).

### **13.1.5 Compatibility & validation (binary)**

* **Schema gate:** v1 success bodies validate the six-key schema; `categories[*] == {id,band}` only.  
* **Parity/identity:** A3/A4 gates pass (AB↔BA, two-run, Reader↔CLI byte equality; preimage re-check).  
* **A7 transport:** v1 responses follow §10 (ETag on 200; 304-after-200; HEAD parity; `no-store` & no ETag on writers/errors).  
* **Evidence:** goldens and scripts indexed in **Appendix D — Evidence Index** (titles/paths only).

### **13.1.6 Change control**

* **Public shape change ⇒ version bump.** Any proposal to alter the v1 contract **MUST** define a **Reader v2** (or higher) with updated schema, acceptance, and migration notes; land via Doc-Delta with full evidence.  
* **No silent drift.** Adding “optional” public fields under v1 is **prohibited**; clients and CI validate **strict equality** to the v1 schema.

## **13.2 Presets/evolution policy \[Required-Now\]**

**Governance stance (normative).**  
 Presets are a **frozen, cataloged control surface** for internal scoring/aggregation. They **MUST NOT** change the public Reader v1 covenant (numeric-free; `{id, band}` only) and are promoted via the **freeze-pack** process. Arithmetic and schema details are **owned by Math** and are referenced here **by title only**.

### **13.2.1 Ownership & routing**

* **This document (Governance) owns:** enable/disable posture, promotion/rollback rules, evidence requirements, and Doc-Delta/process gates.  
* **Math (titles-only) owns:** preset **schema**, arithmetic (weights, caps/floors, dampeners, cross-family corrections, micro posture), and the closed vocab domains used by presets. No arithmetic is duplicated here.

### **13.2.2 Change control (freeze-pack impact)**

* **Preset changes ⇒ new `release_id`.** Adding/removing a preset, or changing preset **weights**, **caps/floors**, **dampeners**, **cross-family** hints, **micro** posture, or the preset **schema** is a **math change** and **MUST** be captured in the freeze-pack; promotion requires a **new `release_id`** (see §5.1).  
* **Precedence policy.** If presets co-exist with viewer weights, the **deterministic precedence policy** must be **pinned by title** (Math/CLI reference). Changing that policy requires a **Doc-Delta** and updated evidence.  
* **No public drift.** Preset evolution **MUST NOT** introduce public numerics or new public fields under Reader v1 (see §13.1).

  ### **13.2.3 Acceptance to land (binary)**

* Schema validation (titles-only). Every preset validates against the Math-owned schema (exact Magic-10 keys; integers 0..100; closed enums for caps/dampeners).  
* Determinism. Fixed-point arithmetic with **round away-from-zero**; AB↔BA and two-run identity hold under the selected preset(s).  
* Public covenant. Reader v1 success remains {id, band} only; no changes to six-key shape or error model.  
* Evidence. Update Appendix D — Evidence Index with preset schema passes, fixed-point boundary goldens, and parity/identity runs; add a Doc-Delta entry in §9.

### **13.2.4 Versioning posture**

* **No Reader version bump** is required for preset changes that keep the v1 public covenant intact (they still yield a new `release_id`).  
* **Reader version bump (v2+)** is required **only** if preset behavior would change the **public** contract (e.g., exposing additional public categories or public numerics). Such proposals must define the new version and land via Doc-Delta with full evidence (see §13.1).

# **14\. Retired Features \[Normative Notice\]**

## **14.1 Prompt \[Required-Now\]**

* **Status:** Removed from the public contract.  
* **Scope of removal:** The `prompt` field is **disallowed** in all public payloads and **must not** be preserved or injected by the Presenter. Any prior optional `categories[*].prompt` schema property is **deleted**; public items remain exactly `{id, band}`.  
* **Administrative surfaces:** `prompt` **must not** appear on admin/dev payloads either (keep parity with public).  
* **Rationale (one line):** Reader v1 is numeric-free and narrative-free; `prompt` risks drift without advancing the math contract.  
* **Effective date:** **2025-10-19**; first removed in the **Math & Technical Spec** (review) and retained through subsequent cuts (titles-only reference).

## **14.2 Uncertainty \[Required-Now\]**

* **Status:** Never shipped; any references are **excised** from this governance and related specs.  
* **Scope:** No uncertainty fields, tokens, or narratives are defined or permitted on public or admin surfaces.  
* **Rationale (one line):** Uncertainty signaling is out of scope for Reader v1 and introduces non-deterministic interpretations inconsistent with the fixed math contract.  
* **Effective date:** **2025-10-19**; scrub completed across **Review** documents. No operational impact on the current public contract.

# **15\. Open Toggles & Questions \[Open\]**

## **15.1 Feature toggles (default OFF)**

* **Default posture.** All feature toggles are **OFF by default** in all environments.  
* **Activation requirements (binary).** A toggle may be turned **ON** only with:  
  1. an **approved Doc-Delta** that pins scope and affected sections,  
  2. **new/updated goldens** and CI jobs for the implicated gates (A3/A4/A7/rails), and  
  3. updated **Evidence Index** entries (Appendix D) in the **same change**.  
* **Rollout guardrails.** Prefer **staged canary** with time-boxed scope; do **not** change public bytes or schemas under Reader v1; use **pointer-flip** rollback if acceptance fails (§5.2).

## **15.2 Open issues list**

> Keep this list short and actionable. Each item has an **owner**, a **next step**, and a **target Doc-Delta** or **deadline**.

* **OI-001 — Reader v2 planning (full Magic-10 exposure).**

  * *Owner:* Architecture \+ Math leads  
  * *Next step:* Draft v2 public schema \+ acceptance; define migration plan; Doc-Delta proposal  
  * *Status:* OPEN  
* **OI-002 — Preset precedence vs viewer weights (pinning).**

  * *Owner:* Math \+ CLI  
  * *Next step:* Route final policy by title (CLI/Math); add tests; Doc-Delta  
  * *Status:* OPEN  
* **OI-003 — Vendor open-rails pilot (timeouts/retries/backoff/429).**

  * *Owner:* Transport  
  * *Next step:* Pin profile enums; add integration job; Doc-Delta to flip rails; redaction proof  
  * *Status:* OPEN  
* **OI-004 — Serializer unification proof in CI (symbol allowlist).**

  * *Owner:* Platform  
  * *Next step:* Add symbol-level emitter check; extend grep-guards; refresh parity/idempotence goldens  
  * *Status:* OPEN  
* **OI-005 — A7 HEAD `Content-Length` verification on large bodies.**

  * *Owner:* Transport  
  * *Next step:* Add header snapshot test for edge cases; Doc-Delta if matrix changes  
  * *Status:* OPEN

> Update this list as items close; each closure should cite the Doc-Delta ID and the Evidence Index entries that were updated in the same change.

# **Appendices \[Informative / Reference\]**

## **Appendix A — Transport Matrices (Reader) \[Required-Now\]**

**Governance.** This appendix defines the required headers and conditional rules for Reader responses. Transport **bytes and examples** live by title in **HDE-CLI-API-Vendor-Ref**; this section governs policy only. No payload bytes appear in this document.

### **A.1 Success (200) — required headers**

* **Content-Type:** `application/json; charset=utf-8` — UTF-8 JSON; BOM/ANSI-free.  
* **ETag:** `"strong, quoted"` — identity over the final LF-terminated body (canonical JSON per HDE-Schemas & Artifacts, pre-compression); encoding-invariant.  
* **Vary:** `Authorization, Accept-Encoding` — at minimum.  
* **Cache-Control:** `private, max-age=0, must-revalidate` — required on 200 (and mirrored on HEAD; see A.4).

### **A.2 Success (200) — body covenant**

* **Six keys exactly:** `reader_version, eligible, categories, meta, release_id, idempotence_hash`.  
* **Categories policy (v1):** `categories[*] == { id, band }` only (numeric-free); v1 Alpha: single `{"id":"harmony","band":<band>}` when `eligible == true`.  
* **Canonical emission:** UTF-8, sorted keys, compact separators, exactly one LF.  
* **Idempotence:** `idempotence_hash = sha256(preimage_bytes)` where the preimage fields are defined in HDE-Math-Spec (no local restatement here).

### **A.3 304 Not Modified (conditional GET)**

* **Precondition (strong ETag).** A prior 200 OK with a strong, quoted `ETag` **MUST** exist for the same resource, and the request **MUST** present a matching `If-None-Match`.  
* **Shape.** **No body; omit both `Content-Type` and `Content-Length`.**  
* **Validators.** Repeat the validators from the cached 200 (for example, `ETag`, `Vary`, `Cache-Control`).  
* **Writers/errors excluded.** Never use 304 for writers or error responses; those responses **MUST** send `Cache-Control: no-store` and **MUST NOT** send `ETag`.

### **A.4 HEAD parity**

* **Headers mirror 200** (strong quoted `ETag`; `Vary: Authorization, Accept-Encoding`; `Cache-Control: private, max-age=0, must-revalidate`; `Content-Type: application/json; charset=utf-8`).  
* **No body;** `Content-Length == len(identity 200 body)` (canonical LF-terminated bytes, pre-compression).  
* **Encoding invariance.** Identity (`ETag`) is unchanged by accepted `Accept-Encoding` selections.

### **A.5 Writers & errors**

* `Cache-Control: no-store` on **all** writers and **all** error responses.  
* **No `ETag`** on writers/errors.  
* **Errors.** `Content-Type: application/json; charset=utf-8`; typed errors only (numeric-free code/message object), LF-terminated; no PII; no vendor payload echo.  
* **Writers (success-without-body).** Typically `204 No Content`; if a body is emitted for diagnostics, it **MUST** be typed, minimal, numeric-free, and canonically serialized (LF-terminated).  
* **POST is non-conditional.** Ignore `If-*` conditionals for POST; writers/errors never return 304\.

**Writers — OPTIONS/HEAD semantics (normative).**

* **OPTIONS → 204 (no body).** For writer resources, OPTIONS **MUST** return 204 with no body; no `ETag`/`Vary`/compression. Under HTTP/2, `Content-Length: 0` may be omitted.  
* **HEAD 405 (strict).** Writers’ HEAD on non-HEAD writer routes returns 405; include `Content-Length: 0`.

### **A.6 Examples (titles-only; no payload bytes)**

* Success \+ ETag (200) — Transport: Success 200 headers (cataloged endpoint)  
* Conditional GET (304) — Transport: Conditional 304 headers (cataloged endpoint)  
* HEAD parity — Transport: HEAD-vs-200 parity headers  
* Writers/errors — Transport: no-store \+ no-ETag headers  
   *(Keep these titles synchronized with Appendix D: Evidence Index and the machine JSONL mirror; update both in the same change when snapshots move.)*

### **A.7 Acceptance checklist (binary)**

1. **200:** strong, quoted `ETag`; body meets six-key covenant; LF/encoding OK; `Cache-Control: private, max-age=0, must-revalidate` present; `Vary` present; encoding-invariant `ETag`.  
2. **304:** served only **after 200**; **no body**; validators mirror 200; **`Content-Type` omitted; `Content-Length` omitted.**  
3. **HEAD:** mirrors all 200 validators (including `Content-Type`); no body; `Content-Length` matches identity 200\.  
4. **Writers/errors:** send `no-store` and no `ETag`; typed error shape and LF present.  
5. **Evidence:** snapshots exist and are indexed in Appendix D (titles/records only) and mirrored in the machine JSONL **with path-proofs**.  
6. **POST non-conditional:** POST responses never return 304 and do not honor request validators.  
7. **Proof endpoint:** A7 proofs are run on an **HDE-CLI-API-Vendor-Ref** Endpoint Catalog (success JSON) route (titles-only reference).

---

## **Appendix B — Acceptance Gate Details \[Required-Now\]**

Titles and paths only; no payload bytes. This appendix lists gate checklists and CI jobs that enforce them. Keep it synchronized with **Appendix D — Evidence Index** and CI config in the same change.

### **B.1 GATE:CORE-CANON — Canonical emission and comparators**

* **Checklist (binary):** single presenter/emitter; UTF-8; sorted keys; compact separators; one LF; arrays-as-sets deduped and ASCII-sorted; conflict ⇒ fail-closed; `LC_ALL=C`.  
* **CI jobs (titles-only):**  
  * `ci/jobs/canonical_emitter_symbol_check.yml`  
  * `ci/jobs/no_json_dumps_public_guard.yml`  
  * `ci/jobs/lf_and_encoding_check.yml`

### **B.2 GATE:CORE-DET — Determinism and identity**

* **Checklist (binary):** preimage (five-key) → `sha256` → final; AB↔BA byte-equality; two-run identity.  
* **CI jobs (titles-only):**  
  * `ci/jobs/preimage_recompute_and_compare.yml`  
  * `ci/jobs/ab_ba_parity_bytecompare.yml`  
  * `ci/jobs/two_run_identity_bytecompare.yml`

### **B.3 GATE:CORE-READER — Public covenant and transport hooks**

* **Checklist (binary):** success \= six keys; `categories[*] == {id, band}` (numeric-free); typed error shape; Reader↔CLI byte-equality; A7 hooks present.  
* **CI jobs (titles-only):**  
  * `ci/jobs/schema_shape_success.yml`  
  * `ci/jobs/schema_shape_error.yml`  
  * `ci/jobs/reader_cli_parity.yml`

### **B.4 A7 — Transport tokens (200 / 304 / HEAD / writers+errors)**

**Proof surface.** A7 proofs run on a **Catalog JSON success** route listed in PF05 §5.6 (titles-only); **not** on `/internal/version`.

* **Checklist (binary):**  
  * **200:** strong, quoted ETag present; `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
  * **304:** only after a prior 200-with-body; no body; validators mirror 200; **omit** `Content-Type`; **omit** `Content-Length`; ETag present.  
  * **HEAD:** validators mirror 200; no body; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
  * **Writers/Errors:** `Cache-Control: no-store`; no ETag; errors include `Content-Type: application/json; charset=utf-8`.  
  * **Encoding invariance:** for the same canonical body, identity (ETag) and effective length are stable across accepted `Accept-Encoding`.  
* **CI jobs (titles-only):**  
  * `ci/jobs/transport_etag_200.yml`  
  * `ci/jobs/transport_conditional_304.yml`  
  * `ci/jobs/transport_head_parity.yml`  
  * `ci/jobs/transport_no_store_writers_errors.yml`

### **B.5 Rails posture — Closed refusal / Open conformance**

* **Checklist (binary):** closed ⇒ no network I/O, typed refusal, keys-only logs; open ⇒ pinned timeouts/retries/backoff/429, deterministic mapping, no payload/secret logging; parity/idempotence unaffected.  
* **CI jobs (titles-only):**  
  * `ci/jobs/rails_closed_refusal.yml`  
  * `ci/jobs/rails_open_conformance.yml`  
  * `ci/jobs/logs_keys_only_redaction.yml`

### **B.6 GATE:CORE-MATCH — Compat math posture (titles-only; math owned in spec)**

* **Checklist (binary):** closed Magic-10 IDs/order; inclusive maxima thresholds; viewer prefs ints `0..100`; fixed-point with round away-from-zero and clamp `[0..100]`; no public numerics.  
* **CI jobs (titles-only):**  
  * `ci/jobs/validation_viewer_prefs.yml`  
  * `ci/jobs/fixed_point_rounding_and_clamp.yml`  
  * `ci/jobs/band_thresholds_inclusive.yml`  
  * `ci/jobs/public_numeric_ban_guard.yml`

**Maintenance rule (MUST).** When a gate’s golden/snapshot/script path changes, update **Appendix D — Evidence Index** and the corresponding CI job references here **in the same change**, and add a one-line entry in **§9 Change Management — Doc-Delta Hooks**.

### **B.7 EPIC017 token/test mapping (compat, registry, ordering, evidence)**

*Compat & CLI tokens*

* **CLI\_NO\_ALT\_JSON\_OK**, **CLI\_SHOWCOMPAT\_CANON\_OK**, **CLI\_STDOUT\_LF\_OK**, **CLI\_READER\_PARITY\_OK**  
   *Tests/scripts (titles-only):* `tests/test_emitter_determinism.py`, `tests/test_reader_transport.py`, `tests/cli/test_cli_showcompat.py`.

*Determinism & composite tokens*

* **JSON\_CANONICAL\_CHECK\_OK**, **TWO\_RUN\_IDENTITY\_OK**, **COMPOSITE\_ABBA\_IDENTITY\_OK**, **TIEBREAK\_TOTAL\_ORDER\_OK**  
   *Tests/scripts (titles-only):* `tools/order/generate_ordering_artifacts.py`, `tests/order/test_ordering_artifacts.py`, `cli.showcompat.*` determinism tests.

*Registry tokens*

* **CONFIG\_GEN\_OK**, **UNKNOWN\_IDS\_FAIL\_CLOSED\_OK**  
   *Tests/scripts (titles-only):* `tools/generate_registry_report.py`, `tests/config/test_registry_report_determinism.py`, `tests/config/test_registry_report_exists_and_is_canonical.py`.

*Evidence and mirror tokens*

* **EVIDENCE\_INDEX\_UPDATED\_OK**, **MACHINE\_MIRROR\_UPDATED\_OK**, **EVIDENCE\_INDEX\_HASH\_OK**, **EVIDENCE\_INDEX\_MIRROR\_OK**, **EVIDENCE\_PATHS\_VALIDATED\_OK**, **EVIDENCE\_PATH\_PROOFS\_OK**, **CI\_CHECK\_MIRROR\_SCHEMA\_OK**, **CI\_CHECK\_FINAL\_LF\_OK**  
   *Tests/scripts (titles-only):* `tools/evidence/update_evidence_index.py`, `tests/ops/test_evidence_index.py`, `tests/evidence/test_evidence_skeleton.py`.

*Doc-deltas & QA coverage tokens*

* **DOC\_DELTA\_PRESENT\_OK**, **TESTS\_PASS\_OK**  
   *Artifacts/tests (titles-only):* `audit/docdeltas/PF04_EPIC017_tokens_and_env.md`, `audit/docdeltas/PF04_EPIC017_tokens_and_env.md.path_proof.txt`, `qa.compat.coverage_summary`.

---

## **Appendix C — Bench & Ops Runbook \[Required-Now\]**

Titles/paths only — no payload bytes. This runbook defines how to run the bench harness and verify SLOs. Keep references synchronized with **Appendix D — Evidence Index** and CI config in the same change.

### **C.1 Purpose & scope**

* Prove determinism (A3), Reader↔CLI parity (A4), and transport invariants (A7) under load, without PII or payload logging.  
* Produce bounded latency histograms and percentile summaries (p95/p99).  
* Support promotion/rollback decisions (see §5.2).

  ### **C.2 Bench profiles (titles-only)**

* **Math/transport profile (rails closed).** Deterministic engine \+ presenter; no network I/O.  
* **Vendor profile (rails open).** Timeouts/retries/backoff per §11.2; typed mapping; keys-only logs. Pin profile names/arguments in repo scripts (see Appendix D).

  ### **C.3 Usage recipe (deterministic runs)**

1. **Prepare fixtures & env.** Fixed fixture set, pinned env; do not vary counts/data between cuts.  
2. **Warm-up then measure.** Discard warm-up; collect metrics during a fixed measurement window.  
3. **Collect checks.**  
   * Parity & identity: AB↔BA, two-run, Reader↔CLI byte-compare; preimage → sha256 → final.  
   * A7 spot checks (dev harness): ETag on 200; 304-after-200; HEAD parity; no-store on writers/errors.  
4. **Capture histograms/counters.** Engine/presenter/reader latency buckets; outcome counters with bounded labels.  
5. **Write artifacts (titles/paths only).** Bench report (percentiles \+ histogram snapshot), parity/identity logs, A7 header snapshots.

   ### **C.4 SLO verification (binary)**

* **Inputs:** bench report for current cut; pinned SLO targets (§6.2).  
* **Pass when:** (1) p95/p99 thresholds met by profile/metric; (2) A3/A4 pass in the same runs; (3) A7 spot checks pass; (4) rails posture honored.  
* **Fail posture:** stop canary or rollback via pointer-flip (§5.2); open investigation.

  ### **C.5 Reporting & evidence (titles-only)**

* **Bench report:** `artifacts/bench/bench_report_{release_id}.json`  
* **Parity/identity logs:** `artifacts/bench/parity_identity_{release_id}.log`  
* **Transport snapshots:** `artifacts/bench/transport_headers_{release_id}/…`  
* **Indexing:** update **Appendix D — Evidence Index** in the same change.

  ### **C.6 CI hooks (titles-only)**

* **Jobs:** `ci/jobs/bench_math_transport.yml` (rails closed) `ci/jobs/bench_vendor_open.yml` (rails open; policy pinned) `ci/jobs/slo_verify.yml` (compare report vs targets)  
* **Guards:** enforce keys-only logging; fail on payload/body/header-value patterns; assert one LF and canonical encoding on emitted JSON.

  ### **C.7 Ops notes**

* **No schema drift.** Bench harness must not alter public bytes or schemas.  
* **Keys-only logs.** Never log payloads or header values; secrets always redacted (see §7.1, §8.2).  
* **Pointer discipline.** Promotions/rollbacks are pointer flips to `release_id`; record outcomes in the Change Log and update Appendix D.

---

## **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**

**Single-home rule.** PF12 governs the **human Evidence Index** (`docs/evidence/INDEX.json`), the **hash sentinel** (`docs/evidence/INDEX.sha256`), and the **machine JSONL mirror** (`artifacts/evidence_index.jsonl`). **Update all three in the same PR** when any governed artifact changes. The mirror is **one file**, **records-only canonical JSONL** (UTF-8; sorted keys; compact; **one LF**); **ASCII field order**; **sort-before-write**; **unknown-keys rejected**; each record includes a **`proof_anchor`** to a co-located path-proof.

**Governed locations only.** Store proofs under `artifacts/**` or `docs/**`; ephemeral generator paths are **not** authoritative.

---

### **D.0 Close-pack & release manifests (admin)**

**Deterministic path-of-record (baseline close-pack pair; non-token).**  
 The canonical close-pack pair MUST live at the deterministic audit/ locations below. This is a baseline closure artifact requirement and is not tokenized by default.

* `audit/EPIC-###_close_report.md`

* `audit/EPIC-###_close_report.md.path_proof.txt`

* `audit/EPIC-###_MANIFEST.json`

* `audit/EPIC-###_MANIFEST.json.path_proof.txt`  
   (Where `###` is the zero-padded 3-digit epic number, e.g., `009`, `023`. The close report and manifest MUST each have a co-located `.path_proof.txt` sibling at the deterministic `audit/` location.)

**No relocation / no dual-home acceptance binding.**  
 These artifacts MUST NOT be relocated into `audit/qa/**` or `artifacts/**` without an explicit canon change. Any extra copies elsewhere are convenience-only and MUST NOT be used for acceptance binding.

---

### **D.1 Parity (Reader↔CLI, AB↔BA, two-run)**

* Goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Harness/tests: `tests/reader_v1/test_emitter.py`, `tests/cli/test_cli_stdout_schema_and_lf.py`  
* Byte-compare scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Composite fingerprint: `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`  
* Integration set: `fixtures/composite/integration_abba/*.json`, `audit/gates/determinism/abba_compare_integration.log`

---

### **D.2 LF & encoding discipline (UTF-8; one LF; no BOM/ANSI)**

* Checks/tests: `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`  
* CI guards: `ci/jobs/lf_and_encoding_check.yml`, `ci/grep-guards/no_ansi_no_bom.regex`

---

### **D.3 Idempotence coupling (preimage → sha256 → final)**

* Identity marker/logs: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Recompute scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Schema (success, six keys): `schemas/reader.v1.schema.json`

---

### **D.4 Endpoint Catalog & transport proofs (Reader A7)**

**Proof surface & posture (titles-only).**

* A7 proofs run **only** on a **cataloged JSON success** route (Endpoint Catalog; titles-only in CLI/API Vendor Ref).  
* The Catalog is **internal-only** and **env-gated**; **non-prod entries must be unreachable in prod** — capture a **headers-only env-gate** proof.  
* The `/internal/version` ops surface is **excluded** from A7.  
* Artifacts below are **records-only**; index each in the machine mirror; LF-terminated; header names **lower-case**; values **verbatim**.

**Catalog/A7 artifacts.**

* Catalog snapshot — `artifacts/reader/endpoints_snapshot.json`  
* Env-gate proof (headers-only; one LF) — `artifacts/proofs/endpoints_env_gate_proof.log`  
* Composite success proof (records-only JSON) — `artifacts/proofs/reader_success_get_head_304.json` *(PF12 schema; presence required)*  
* Optional encoding-invariance proof — `artifacts/proofs/encoding_invariance.txt`

**Aux Narrative (text) snapshots (headers-only).**

* `tests/transport/headers/aux_text_200.snap`  
* `tests/transport/headers/aux_head.snap`  
* `tests/transport/headers/aux_304.snap`  
* `tests/transport/headers/aux_suppression.snap`

**Catalog source and integrity (titles-only).**

Note: When Endpoint Catalog JSON bytes change, regenerate the checksum and path-proof sidecars in the same change. Any mismatch indicates stale sidecars and is a mechanical blocker.

* `docs/ENDPOINTS_CATALOG.json`

* `docs/ENDPOINTS_CATALOG.json.sha256`

* `docs/ENDPOINTS_CATALOG.json.path_proof.txt`

* `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`

* `artifacts/audit/ENDPOINTS_CATALOG.json`

* `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`

* `tests/http/test_endpoint_catalog.py`

**Writer/error posture (headers-only).**

* `tests/transport/headers/error_headers_utf8.snap`  
* `tests/transport/headers/no_store_writers_errors.snap`

**CI jobs (titles-only).**

* `ci/jobs/transport_etag_200.yml`  
* `ci/jobs/transport_conditional_304.yml`  
* `ci/jobs/transport_head_parity.yml`  
* `ci/jobs/transport_no_store_writers_errors.yml`

---

### **D.5 Rails posture (refusal & open conformance)**

* **Closed-rails refusal proof** (single-file canonical; headers → blank line → body): `artifacts/proofs/refusal_run.txt` *(format rules in PF12 §8.3.1)*  
* **Shaping correctness (closed rails):** `ci/jobs/logs_keys_only_redaction.yml`  
* **Open-rails conformance** (timeouts/retries/backoff profile): `ci/jobs/rails_open_conformance.yml`

---

### **D.6 Internal-ops surface: `/internal/version`**

* GET body capture — `artifacts/ops/internal_version/body_get.json` and `artifacts/ops/internal_version/body_get.sha256`  
* GET headers capture — `artifacts/ops/internal_version/headers_get.txt`  
  HEAD headers capture — `artifacts/ops/internal_version/headers_head.txt`  
* Conditional header captures (conditionals ignored; still 200\) — `artifacts/ops/internal_version/headers_cond_if_none_match.txt` and `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`  
* Request-chain manifest (proof surface coupling) — `artifacts/ops/internal_version/request_chain_manifest.json` and `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`  
* Coupling \+ two-run identity proof log (single governed surface) — `artifacts/ops/internal_version/two_run_identity.log` and `artifacts/ops/internal_version/two_run_identity.log.path_proof.txt`  
* Path proofs — each artifact above MUST have a co-located `*.path_proof.txt` file referenced by the machine mirror’s `proof_anchor`.

---

### D.7 Database runtime posture (prod & dev)

Env snapshot — `artifacts/runtime/env_matrix.snapshot.json` (singleton; one file representing the default rails settings across environments, using the canonical v3 schema with uppercase rails keys such as `SAFE_MODE` and `ALLOW_NETWORK` and labeled policy fields; governed by `ENV_RAILS_POLICY_OK` and `ENV_LC_ALL_C_OK`).  
 Current direct-selection snapshot — `artifacts/runtime/direct_db_selection.snapshot.json` (direct-only provider selection, retired-key refusal, fail-closed direct unavailability, zero alternate-transport attempts, and secret-value absence).  
 Historical bridge-era connectivity snapshot — `artifacts/runtime/env_connectivity.snapshot.json` (retained historical evidence only; not current bridge availability, support, fallback, parity, or token proof).  
 DDL/search\_path/grants set — `artifacts/db/check_schema.txt` (search\_path), `artifacts/db/grants.txt` (least-privilege), `artifacts/db/ddl_fingerprint.json` (normalized fingerprint), `artifacts/db/conn_env_selection.log` (selection proof)

(Tokens & policy live in §2.0 / §6.3.)

---

### **D.8 QA artifacts namespace (transient captures)**

* Namespace (titles-only): `artifacts/qa/` *(transient test-only; governed by PF12)*

---

### **D.9 BodyGraph adapter data-source & invariance (PF10-AA)**

* Source selection snapshot — `artifacts/bodygraph/source_selection.snapshot.json`  
* Source invariance (A→B) — `artifacts/bodygraph/source_invariance/ab.json`  
* Source invariance (B→A) — `artifacts/bodygraph/source_invariance/ba.json`  
* Summary — `artifacts/bodygraph/source_invariance/summary.json`  
* Release bindings — `artifacts/bodygraph/release_bindings.json`  
* Refresh/TTL/SWR policy snapshot — `artifacts/bodygraph/refresh_policy.snapshot.json`  
* Metrics snapshot (keys-only) — `artifacts/bodygraph/metrics.snapshot.json`  
* Keys-only logs sample (sanitized) — `artifacts/bodygraph/keys_only.logs.sample`

*(Narratives adapter/data-source policy is routed by title; evidence only.)*

---

### **D.10 Bands and thresholds (inclusive-high)**

* Edge proofs: `audit/gates/bands/edges.snapshot.json`, `audit/gates/bands/edges.diff.json` (boundaries at 24/49/74/100; see HDE Math Spec)  
* CI jobs: `ci/jobs/bands_edges_snapshot.yml`, `ci/jobs/bands_edges_diff.yml`

### **D.11 Pack constants and release identity**

* Constants pack (evidence snapshot): `artifacts/math/constants.json`, `artifacts/math/constants.json.sha256`  
* Current release-identity input: `catalog/manifest.json`  
* Current release provenance (external; no durable repository path): `hde.release_attestation.v1` exact-head CI artifact  
* Frozen historical checked-in release evidence: `artifacts/math/freeze_pack_manifest.json`, `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`

---

### **D.12 Topology loader: orientation and graph invariants**

* Orientation demo: `audit/gates/topology/orientation_demo.txt` (before/after high–low → min→max NN-NN; arrays-as-sets deduped and ASCII-sorted)  
* Integration degree check: `audit/gates/topology/degree_check.log` (verifies 10/20/34/57 ⇒ degree 3; all other gates ⇒ degree 1\)  
* Center-pair multiplicity: `audit/gates/topology/multiplicity_vector.log` (unordered center-pair counts sum to 36\)  
* **Coupling rule (merge-blocking).** If any governed evidence changes that require updates to `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, or `artifacts/evidence_index.jsonl`, the topology orientation demo artifact MUST be refreshed and remain coherent in the same PR. CI is expected to fail with an ORIENTATION\_DRIFT-class error if Index/Mirror changes without a matching orientation demo refresh.

---

**Indexing discipline (reminder).** Every artifact listed in this appendix **must** be added to the **human** index and mirrored in `artifacts/evidence_index.jsonl` **in the same PR**, with a `proof_anchor` pointing to a path-proof stored alongside the artifact.

