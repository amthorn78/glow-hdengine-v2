# Exact redlines — PF02 from v2.4.5

Run: `gtwpe-20261009-pf10-v13-5 / T-PF02 / baseline-v2.4.5 / package-r2`. Assigned ledger row: `T-PF02`.

Preparation contract: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.

Original: `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.5.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; Git blob `f74aace7d277047c9a0198043cdd89289288f11c`; 137395 bytes; SHA-256 `d57fd3547573b8b8e3076b8f3fa4a34423a8b677c10bca93ff58eb6d4d867c6f`.

Originating preparer: the same Nathan-started ChatGPT Work document session, executing agent `/root`, workspace `/workspace/scratch/72573cef6712`. No platform conversation URL is exposed; none is inferred. Correction returns to this preparer under the same pinned Drain prompt.

Scope: the thirteen complete selected units recorded in the companion proof log. Apply only these original-bound operations. All operations are REPLACE with expected block occurrence one. Byte ranges use UTF-8, zero-based start and exclusive end. Line ranges are secondary aids; the full literal OLD block and exact raw heading path are the locators. Every literal payload below includes its final LF immediately before the closing fence; fencing and labels are not payload. Do not unescape Markdown, trim whitespace or normalize line endings. Metadata is reserved for TW-APPLY-10.

Baseline controls: version `v2.4.5`; effective date `2026-08-25`; Last Update Gate `BN 12.8.9`; status `Canon`; invocation tag `INV-f2ac55d77ce9aacc`. Ordered change-source provenance: `PF10-HDE-Build-Notes-v13.5.md` (v13.5); `HDE-EPIC040-specification-v1.1-approved.md`; `HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`. No native revision-history entry is required by this target. See the companion report for validation and save completeness.

## Redline RL-001

Operation: `REPLACE`. Classification: `CONSISTENCY`.

Original heading path (literal authored headings):

- `# **0\. Front Matter**`
- `## Intent & scope \[Required-Now\]`

Original location: lines 44–46; bytes [1793, 2175). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A30 (T-PF02).

Rationale: Replace the superseded internal-locator citation rule while preserving scoped supersession and PF02 ownership.

OLD

````````text
**Supersession rule (PF10 addenda).**

Where PF10 includes multiple numbered addenda on the same topic, the later number supersedes earlier guidance. Reference PF10 addenda by **addendum number \+ addendum title** (do not anchor to PF10 file versions or PF10 section numbers). PF02 reflects the latest position and routes work to canonical homes by title only (no version numbers).
````````

NEW

````````text
**Supersession rule (HDE Build Notes).**

HDE Build Notes governs only the points its active, non-superseded guidance explicitly covers. A higher-numbered addendum controls overlapping scope or scope it explicitly supersedes; earlier guidance remains authoritative for distinct scope. PF02 reflects the effective position and references **HDE Build Notes** by document title only, without addendum numbers, addendum titles, section numbers, or file-version locators. When HDE Build Notes is silent on a PF02-owned point, PF02 governs.
````````

## Redline RL-002

Operation: `REPLACE`. Classification: `CONSISTENCY`.

Original heading path (literal authored headings):

- `# **0\. Front Matter**`
- `## **Change control \[Required-Now\] (titles-only cross-refs; no duplicated bytes)**`

Original location: lines 100–100; bytes [9233, 9726). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A38 (T-PF02).

Rationale: Read the PR-opening actor by function; preserve cadence, same-PR duties and mutation boundaries.

OLD

````````text
Epic-Process-Guide governs PR-first cadence. CodEx opens the PR automatically (one PR per epic/slice). Doc-Delta, Appendix D (human), the human Evidence Index (`docs/evidence/INDEX.json`), and the machine mirror (`artifacts/evidence_index.jsonl`) must update in the same PR whenever proofs/artifacts change. When the machine mirror changes, its governed companion files (`artifacts/evidence_index.jsonl.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt`) MUST update in that same PR.
````````

NEW

````````text
Epic-Process-Guide governs PR-first cadence. The executing agent opens the PR automatically (one PR per epic/slice). Doc-Delta, Appendix D (human), the human Evidence Index (`docs/evidence/INDEX.json`), and the machine mirror (`artifacts/evidence_index.jsonl`) must update in the same PR whenever proofs/artifacts change. When the machine mirror changes, its governed companion files (`artifacts/evidence_index.jsonl.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt`) MUST update in that same PR.
````````

## Redline RL-003

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# 1\. Architectural Principles \[Required-Now\]`
- `## 1.1 Single homes`

Original location: lines 204–204; bytes [20044, 20349). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A03, A13, S07, S12 (T-PF02).

Rationale: Separate intrinsic mechanics from application eligibility, narrative augmentation and projection; remove the misleading directional-core ownership.

OLD

````````text
* **Engine Core module** (names-only). A pure-compute module under `engine/` that owns neutral and directional compatibility metrics, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling. It does not import transport, CLI, HTTP, evidence tooling, or environment.
````````

NEW

````````text
* **Engine Core module** (names-only). A pure-compute module under `engine/` that owns intrinsic Gate-based compatibility computation, AB↔BA neutrality, and the complete ordered ten-category score-and-band result. Person identity, viewer preferences, directional narrative routing, eligibility decisions, and surface serialization are outside intrinsic computation. It does not import transport, CLI, HTTP, evidence tooling, or environment.
````````

## Redline RL-004

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **2\. System Overview (Blocks & Flows) \[Required-Now\]**`
- `## **2.1 Components & responsibilities (single homes)**`
- `### **Repo map (normative)**`

Original location: lines 325–327; bytes [32080, 32790). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A03, A13, A22, A24, A26, S07, S12 (T-PF02).

Rationale: Describe the delivered pure-core/admission/consumer split using bounded baseline code inspection; retain distribution and runtime limits.

OLD

````````text
* The canonical Engine Core behavior lives at `engine.core.core`, with `engine.core.core.compute_core` as its canonical entrypoint. It owns the core compatibility computation: neutral and directional metrics, category-framework and per-channel mechanics integration, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling.

Current repository discrepancy: at repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`, checked-in runtime public, HTTP compat, and CLI paths use `engine.compat.ts_v0` or `engine.compat.compute` rather than `engine.core.core.compute_core`. This does not change the canonical single-home requirement or claim that migration has occurred.
````````

NEW

````````text
* The canonical Engine Core behavior lives at `engine.core.core`, with `engine.core.core.compute_core(member_a, member_b, mechanics_bundle, release_id)` as its four-argument entrypoint. It consumes two normalized Gate members and one injected immutable admitted mechanics bundle with its release identity, and returns one complete intrinsic result. It does not accept precomputed scores, caller-selected configurations, or an alternate scoring authority.

**Admitted-release boundary [Required-Now].** Bundle loading and release admission occur outside pure Engine Core. Admission binds the manifest-derived release identity to the pinned release metadata and complete member cut, validates captured member bytes and executable-source equivalence, and supplies immutable typed registries and mechanics to the caller. Invalid or incomplete admission fails closed before intrinsic computation; it does not activate, repair, or promote a release. Freeze-Pack membership, canonical bytes and schemas remain owned by **HDE-Schemas & Artifacts**; loader and admission mechanics remain owned by **HDE-Mechanics Guide**.

**Current repository behavior [Implemented].** At repository commit `e7265a090ad0cc8de5f36de2f19481216aa3d073`, Reader and `hdctl showcompat` use `engine.compat.compute.evaluate_pair` as the application boundary. It decides eligibility before core, intrinsic-cache or narrative-router access, loads the admitted bundle outside the core, invokes the four-argument `engine.core.core.compute_core`, and augments the complete result without rescoring. `engine.config.registry_loader.load_active_mechanics_bundle` supplies the immutable admitted bundle. This inspected wiring supersedes the earlier unmigrated-core observation for these consumers; it does not establish other surfaces' runtime behavior, distribution completeness, deployment, or release activation.
````````

## Redline RL-005

Operation: `REPLACE`. Classification: `CONSISTENCY`.

Original heading path (literal authored headings):

- `# **2\. System Overview (Blocks & Flows) \[Required-Now\]**`
- `## **2.1 Components & responsibilities (single homes)**`
- `### **Routing (titles only)**`

Original location: lines 369–369; bytes [35972, 36164). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A38 (T-PF02).

Rationale: Replace the staging actor by function without changing the process route.

OLD

````````text
Concrete guard checks and scripts live in **HDE-Mechanics Guide**, and process/PR workflow (CodEx staging, PR-first merging, repo-docs/Evidence Index updates) lives in **Epic-Process-Guide**.
````````

NEW

````````text
Concrete guard checks and scripts live in **HDE-Mechanics Guide**, and process/PR workflow (executing-agent staging, PR-first merging, repo-docs/Evidence Index updates) lives in **Epic-Process-Guide**.
````````

## Redline RL-006

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **2\. System Overview (Blocks & Flows) \[Required-Now\]**`
- `## **2.2 High-level flow (request → compute → persist → emit)**`

Original location: lines 403–407; bytes [37117, 37794). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A03, A13, S07, S12 (T-PF02).

Rationale: Make the pure pipeline and application-owned eligibility explicit without copying error tokens, schemas or mathematical formulas.

OLD

````````text
   * Engine modules (including `engine.core.core` and `engine.sampler.core`) run pure: **no I/O, clocks, environment reads, randomness, or import-time side effects**.  
   * They accept **normalized data structures** and return **normalized results** (including pair normalization for AB↔BA neutrality).  
   * Side effects are forbidden.  
   * **Magic-10 pure Engine Core flow:** `BodyGraph Gates -> Channel states -> signal wire values -> category scores -> bands -> surface projection`.  
   * Adapter, HTTP handlers, CLI, Presenter, and narrative layers MAY validate, call, or project this result. They MUST NOT calculate, weight, round, band, or rescore independently.
````````

NEW

````````text
   * Engine modules (including `engine.core.core` and `engine.sampler.core`) run pure: **no I/O, clocks, environment reads, randomness, or import-time side effects**.  
   * They accept **normalized data structures** and return **normalized results**. Intrinsic compatibility is AB↔BA neutral and independent of person identity, viewer preferences and narrative orientation.  
   * Side effects are forbidden.  
   * **Magic-10 pure Engine Core flow:** `BodyGraph Gates -> Channel states -> signal wire values -> category scores -> bands`. Surface projection follows outside the core.  
   * The application caller resolves and validates both complete inputs and decides eligibility before Engine Core, intrinsic-cache access or narrative routing. A valid self-pair produces no intrinsic result; malformed or inconsistent inputs fail closed rather than becoming an ordinary ineligible pair.  
   * Adapter, HTTP handlers, CLI, Presenter, and narrative layers MAY validate, call, augment, or project the complete result. They MUST NOT calculate, weight, round, band, or rescore independently.
````````

## Redline RL-007

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **2\. System Overview (Blocks & Flows) \[Required-Now\]**`
- `## **2.2 High-level flow (request → compute → persist → emit)**`
- `### **2.2.1 Alpha surfaces**`

Original location: lines 501–501; bytes [40485, 40736). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A23, A24, S07 (T-PF02).

Rationale: Add Reader v2 projection while preserving Reader v1 and the existing CLI dump/parity boundary.

OLD

````````text
* Reader v1 bytes are the numeric-free public success envelope and are emitted by the Reader success route. When the CLI emits Reader v1 bytes for parity, it does so via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).  
````````

NEW

````````text
* Reader v1 and Reader v2 are bands-only, numeric-free public projections over the same complete intrinsic result. Reader v1 semantics remain unchanged. Reader v2 exposes the complete ordered ten-category band matrix through the same production Reader route; it adds no narrative text or internal scores. The CLI's dedicated Reader dump remains Reader v1 for parity (titles-only; see **HDE-CLI-API-Vendor-Ref**).
````````

## Redline RL-008

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **2\. System Overview (Blocks & Flows) \[Required-Now\]**`
- `## **2.2 High-level flow (request → compute → persist → emit)**`
- `### **2.2.2 Proofs & routing (titles-only)**`

Original location: lines 552–552; bytes [44996, 45303). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A23, A24, S07, S12 (T-PF02).

Rationale: Route versioned Reader contracts to their owning PFs without copying payload fields or preimage bytes.

OLD

````````text
* The public envelope (six-key **Reader v1** envelope, bands-only, numeric-free) and its schema live in **HDE-CLI-API-Vendor-Ref** and **HDE-Schemas & Artifacts**. When the CLI emits Reader v1 bytes for parity, it does so via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).  
````````

NEW

````````text
* Reader v1 and Reader v2 public envelopes, their canonical serialization, idempotence preimages and schemas live in **HDE-CLI-API-Vendor-Ref**, **HDE-Math-Spec**, and **HDE-Schemas & Artifacts**. Reader v1 and its CLI dump/parity contract remain unchanged; Reader v2 uses the same Presenter emitter over the complete intrinsic result. PF02 owns wiring and projection boundaries only.  
````````

## Redline RL-009

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **3\. Runtime surfaces (by responsibility, not bytes)**`
- `## **3.2 Reader v1 \[Required-Now\] (public success route)**`

Original location: lines 795–872; bytes [59315, 65102). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A13, A23, A24, A26, S07, S12, C1 (T-PF02).

Rationale: Replace superseded dev-only/current-route and alias claims with inspected production v1/v2 wiring, preserve dev/A7 obligations by owner and keep closure/live-readiness limits explicit.

OLD

````````text
## **3.2 Reader v1 \[Required-Now\] (public success route)**

**Intent.**  
A public Reader surface on the adapter that uses the same canonical emitter path as the CLI. It exposes the six-key public envelope for client apps without duplicating computation or serialization logic.

**Responsibilities (conceptual).**

* Accept normalized inputs or references and perform lightweight structural checks before calling the Engine in-proc.  
    
* Return the public envelope via the canonical emitter (no narratives, no internal fields, no side effects).  
    
* Maintain CLI↔Reader byte parity for identical inputs and environment; parity is a requirement (bytes owned elsewhere).  
    
* Obey A7 success-route posture (routing notes below).  
    
* Use DB-backed BodyGraphs for compat computation, following the BodyGraph lifecycle (no inline vendor I/O on Reader 200).

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the checked-in adapter defines `/reader`, emits through the shared Reader emitter, gates non-dev `APP_ENV` values while treating an absent `APP_ENV` as `dev`, and loads local chart files. The Endpoint Catalog classifies `GET /reader` and `HEAD /reader` as internal `dev_harness` routes with `APP_ENV=dev`.

**Current repository discrepancy.**  
The checked-in Reader is a dev fixture surface, not the required public DB-backed Reader. Its handler reads caller-supplied local chart paths and does not implement the DB-backed BodyGraph lifecycle required above.

**Static inspection cannot establish.**  
Static repository bytes do not establish runtime reachability, deployment, or production enablement for the Reader surface.

**Non-goals.**

* No alternate serializers, payload shaping, or per-surface formatters.  
    
* No direct vendor/network calls on the public success route.

**Reader route posture (route-only).**

* **Canonical route:** `GET /reader` is the canonical Reader route for the v1 Reader success surface.  
* **Governed proof-surface role:** `/reader` is the governed Reader success-proof surface when it is the selected cataloged Reader success route for the target environment. Co-location with dev or internal routes in the same adapter module does not make `/reader` a dev-harness-only route class.  
* **Version selection:** Reader v1 is selected via query parameter `v=1` on the Reader route; the route path does not change for v1 selection.  
* **Optional `/api` mount alias:** when the Reader blueprint is mounted under an `/api` prefix in a given runtime configuration, `/api/reader` is an alias of the same Reader surface (not a distinct contract or separate proof surface).  
* **No invented reader-proof path:** there is no `/api/reader-proof/v1` route. Treat references to that path as drift and correct them to the canonical Reader route (`/reader`, or `/api/reader` only when that is the configured mount).  
* **Proof-surface selection:** any proof that depends on a Reader success route must reference the actual reachable Reader route for the target environment. Do not invent alternate proof routes or second designation carriers. When an Endpoint Catalog is used, select the proof route from catalog entries that correspond to real mounted routes; if that inventory is missing an explicit governed-surface designation, treat the gap as documentation drift to correct at the inventory home rather than inventing a second mechanism in Architecture or QA.  
* **Scope note:** this posture records canonical Reader surface routing for planning and QA, preserves the existing Reader success surface, and does not introduce new routes, new flags, or writer-side surfaces.

**A7 proof surface (route-only; titles-only).**

* **Cataloged route only.**  
    
* Reader success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (HDE-CLI-API-Vendor-Ref). The Catalog’s single home is `docs/ENDPOINTS_CATALOG.json` (+ `.sha256` sidecar). The `.sha256` sidecar must reference `docs/ENDPOINTS_CATALOG.json` for repo-root verification. Proofs target a route listed there; `/internal/version` remains excluded. When the selected cataloged proof route is `/reader`, `/reader` is the governed Reader success-proof surface for that scope, env gated to dev (`APP_ENV=dev`), and A7-eligible. This does not classify `/reader` as a dev-only conjunction or preview route. Env-gate proof is mandatory (headers-only).  
    
* **Catalog posture.**  
  The Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod. Capture a headers-only env-gate proof.  
    
* **A7 invariants to satisfy.**  
  Require:  
    
  * `Vary: Authorization, Accept-Encoding`  
      
  * Encoding invariance of identity (ETag) and effective `Content-Length` across accepted encodings  
      
  * HEAD 200 validator parity with `Content-Type == GET` and `Content-Length == len(identity 200 body)`  
      
  * 304 only after prior 200, with no body and omitting both `Content-Type` and `Content-Length`


* **Ops exclusion.**  
  `/internal/version` is excluded from A7 proofs and is not A7-eligible; PF02 does not define its access-control posture.

**Routing (titles-only).**

* Field definitions, examples, conditional delivery, and parity proofs → **HDE-CLI-API-Vendor-Ref**  
    
* A7 acceptance policy and tokens → **HDE-Governance**  
    
* Canonical JSON policy, pack/manifest, and machine mirror discipline → **HDE-Schemas & Artifacts**

Reader’s public success route uses the same Engine Core \+ Presenter flow as compat v1. **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** own success envelope bytes and A7 posture by title, and Reader obtains BodyGraphs via the DB-backed lifecycle described in §2.4.

---

````````

NEW

````````text
## **3.2 Reader v1 \[Required-Now\] (public success route)**

**Intent.**  
Public Reader v1 and Reader v2 use the same adapter-owned production route, application evaluation boundary and canonical Presenter emitter. Their public projections are bands-only, numeric-free and narrative-free; computation and serialization have no per-version alternate home.

**Responsibilities (conceptual) [Required-Now].**

* Accept only the governed party references and version selection, validate them at the application boundary, and resolve both complete BodyGraph projections read-only from the canonical current-row store. Reader performs no write, request-time vendor call, arbitrary identity conversion or silent fallback.
* Decide eligibility before Engine Core, intrinsic-cache access or narrative routing. A valid self-pair produces the governed ineligible public projection without an intrinsic result; malformed or inconsistent projections fail closed under the owning error contract.
* For an eligible pair, call the admitted-release consumer path in §2.1 and project its complete result without recalculation, reweighting, rounding, banding or rescoring.
* Reader v1 retains its existing harmony-only public projection and CLI-dump byte-parity obligation. Reader v2 projects all ten category bands in the canonical order; it does not expose numeric scores, signals, weights, narratives or internal identities. Reader v2 does not change the Reader v1 CLI dump contract.
* Emit both versions through the same governed Presenter emitter. Envelope fields, ordering, idempotence preimages, serialization, error bytes and transport policy remain in their owning PF documents.

**Current repository behavior [Implemented].**  
At repository commit `e7265a090ad0cc8de5f36de2f19481216aa3d073`, `adapter/factory.py` mounts the production Reader blueprint under `/api`. `adapter/http_reader.py` implements `POST /api/reader` with Reader v1 or Reader v2 selection, read-only current-row BodyGraph resolution, `engine.compat.compute.evaluate_pair`, and the shared Reader presenter. The presenter delegates canonical byte emission to the existing emitter; version selection does not create a second calculator or serializer.

**Dev fixture surface [Implemented].**  
The same baseline retains env-gated `GET /reader?v=1` as a local-chart dev/proof surface. It does not expose Reader v2. `POST /reader` remains a refusal stub, not an alias of the production Reader. Dev fixture and production DB-backed Reader proof classes remain distinct.

**Static inspection cannot establish.**  
Inspected wiring does not establish runtime reachability, deployment, production enablement, live current-row readiness, or successful live DB-backed Reader v1/v2 calls. The supplied exceptional EPIC040 closure does not discharge the deferred current-row/live Reader proof, constitute an ordinary close pack, or authorize activation, deployment or PF09 status movement.

**Non-goals.**

* No alternate serializers, payload shaping, per-surface formatters, or public numeric/internal results.
* No direct vendor/network acquisition, writes, or new persistence surface on the public Reader request path.

**Reader route posture (route-only) [Required-Now].**

* **Production route:** `POST /api/reader`, with version selection on the same path for Reader v1 or Reader v2. Production POST transport remains non-conditional under **HDE-CLI-API-Vendor-Ref**; adding Reader v2 creates no route, writer surface or alternate emission path.
* **Dev route:** `GET /reader?v=1` remains the separate env-gated Reader v1 fixture surface. It is not a production POST alias, live DB proof, or Reader v2 proof.
* **No invented reader-proof path:** there is no `/api/reader-proof/v1` route.
* **Proof-surface selection:** select the actual reachable route and version for the target environment. Where an Endpoint Catalog is required, use entries corresponding to the real mounted routes and the required proof class. Missing inventory designation is drift at the inventory home, not authority to invent another route or designation carrier in Architecture.

**A7 proof surface (route-only; titles-only).**

* A7 proofs run only on an A7-eligible cataloged JSON success route, selected through the Endpoint Catalog owned by **HDE-CLI-API-Vendor-Ref**. Adding Reader v2 to the production POST route does not confer GET/HEAD conditional proof semantics on that route.
* Catalog and non-prod env-gate obligations remain in force. Non-prod entries must be unreachable in production and require the governed headers-only env-gate proof. A dev Reader fixture proof supplements its selected scope; it does not prove production current-row behavior.
* A7 validator, conditional-delivery and encoding-invariance obligations remain governed by **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**. PF02 does not duplicate their header matrices.
* `/internal/version` remains excluded from A7 proofs. PF02 does not define its access-control posture.

**Routing (titles-only).**

* Request/response fields, version selection, error envelopes, transport and Reader v1 parity proofs → **HDE-CLI-API-Vendor-Ref**
* Eligibility, complete intrinsic result, category order and idempotence semantics → **HDE-Math-Spec**
* Public schemas, pack/manifest and evidence-index/mirror discipline → **HDE-Schemas & Artifacts**
* A7 acceptance policy and tokens → **HDE-Governance**

Reader's public success route uses the same admitted Engine Core result and Presenter flow for both versions. The read-only production Reader consumes the DB-backed BodyGraph lifecycle in §2.4; acquisition and refresh stay outside its request path.

---

````````

## Redline RL-010

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **3\. Runtime surfaces (by responsibility, not bytes)**`
- `## **3.3 Sample (dev harness) (dev-only)**`

Original location: lines 923–923; bytes [68582, 68895). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A24 (T-PF02).

Rationale: Record admitted dev-conjunction identity and the bounded optional resolver seam without granting production or open-rails authority.

OLD

````````text
Sample harness uses the same Presenter emitter and Engine Core behaviour as compat v1. Dev-only conjunction preview endpoints emit canonical JSON bytes; rails are closed by default unless explicitly opened. Sample harness is never used for A7 proofs; see §2.4 and §5 for compat flow and evidence-plane details.
````````

NEW

````````text
Sample harness uses the same Presenter emitter and Engine Core behaviour as compat v1. Dev-only conjunction preview endpoints emit canonical JSON bytes and use the real admitted manifest-derived release identity. Their resolver seam is dev-only and absent by default; it does not create a production Reader input or fallback. Rails are closed by default unless explicitly opened. Sample harness is never used for A7 proofs; see §2.4 and §5 for compat flow and evidence-plane details.
````````

## Redline RL-011

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **3\. Runtime surfaces (by responsibility, not bytes)**`
- `## **3.8 Reader dev/QA posture & services \[Required-Now\]**`
- `### **3.8.1 Dev/QA Reader availability**`

Original location: lines 1102–1102; bytes [79294, 79483). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A23, A24 (T-PF02).

Rationale: Keep dev/QA Reader availability consistent with versioned production wiring.

OLD

````````text
* Reader v1 is exposed through the adapter process as one of the runtime surfaces named in this section. It uses the single canonical Presenter emitter and never hand-crafts public JSON.  
````````

NEW

````````text
* Production Reader v1 and Reader v2 are exposed through the adapter-owned production route; the separate dev fixture route remains Reader v1. All use the single canonical Presenter emitter and never hand-craft public JSON.  
````````

## Redline RL-012

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **3\. Runtime surfaces (by responsibility, not bytes)**`
- `## **3.8 Reader dev/QA posture & services \[Required-Now\]**`
- `### **3.8.2 QA entrypoints (concept-only)**`

Original location: lines 1126–1126; bytes [82977, 83051). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A23, A24 (T-PF02).

Rationale: Name both production Reader proof surfaces without extending CLI parity to v2 or conflating fixtures with live DB behavior.

OLD

````````text
* **Reader v1** (public success route) for HTTP-level compat envelopes.  
````````

NEW

````````text
* **Reader v1 or Reader v2** on the production success route for the selected HTTP-level public projection. The separate Reader v1 fixture route supplies only its dev proof class.
````````

## Redline RL-013

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **3\. Runtime surfaces (by responsibility, not bytes)**`
- `## **3.8 Reader dev/QA posture & services \[Required-Now\]**`
- `### **3.8.3 Live QA surface selection**`

Original location: lines 1156–1158; bytes [87875, 88669). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A33 (T-PF02).

Rationale: Replace the superseded generic live-boundary/exemption minimum with mandatory bounded synthetic live-vendor coverage while retaining approval, authorization and proof-class separation.

OLD

````````text
**Production-affecting architecture classification.** When an epic affects deployed behavior, public or app-facing behavior, runtime request/response behavior, Engine compute, vendor ingest, external integration, DB persistence/retrieval, app/engine integration, or secret/environment binding, PF02 classifies the affected flow as production-affecting for QA planning. Production-affecting architecture requires live validation of at least one relevant production-facing boundary or an explicit authorized exemption.

PF02 owns this architecture classification only. Exact Live QA steps, open-rails evidence shape, exemption handling, PASS/FAIL semantics, and closeout proof rules live in Glow QA Guide, HDE-Governance, Epic-Process-Guide, HDE-Schemas & Artifacts, and Plan Templates by title.
````````

NEW

````````text
**Production-affecting architecture classification.** When work touches production-functional surfaces, including deployed behavior, public or app-facing behavior, runtime request/response behavior, Engine compute, vendor ingest, external integration, DB persistence/retrieval, app/engine integration, or secret/environment binding, PF02 classifies the affected flow as production-affecting for QA planning. Every such QA Plan MUST include at least one bounded live-vendor open-rails test using synthetic data only, with `SAFE_MODE=0` and `ALLOW_NETWORK=1`. Fixtures, mocks, static inspection, closed-rails replay, and DB-backed or deployed non-vendor behavior do not substitute for this vendor test; the earlier exemption alternative does not satisfy this scope.

The plan identifies the relevant vendor flow, authorized live target, bounded request scope, secret-safety posture, captured evidence, and what the test proves and does not prove. This is a QA-plan approval-readiness condition, not execution authorization or a QA/closure verdict. Role, session, credential, rails and mutation permissions remain unchanged. PF02 owns architecture-level classification and surface selection only; exact test steps, evidence shape, PASS/FAIL semantics and closeout proof rules remain in **Glow QA Guide**, **HDE-Governance**, **Epic-Process-Guide**, **HDE-Schemas & Artifacts**, and **Plan Templates** by title.
````````

## Redline RL-014

Operation: `REPLACE`. Classification: `CANON_UPDATE`.

Original heading path (literal authored headings):

- `# **4\. Boundaries & Contracts (Conceptual) \[Required−Now\]**`
- `## **4.1 Boundary guarantees (no bytes)**`

Original location: lines 1299–1299; bytes [106819, 107131). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A13, A23, A24, S07, S12 (T-PF02).

Rationale: Extend the existing single-compute/single-emitter guarantee to Reader v2 and keep sampler/core invocation applicable to the actual surface.

OLD

````````text
  * Compat v1, Reader v1, dev sampler harnesses, and offline determinism/evidence pipelines all route through the same Engine Core and sampler core modules; no surface is allowed to fork or reimplement core math. Differences are in rails, environment, and evidence policy only (owned in other PF docs by title).
````````

NEW

````````text
  * Compat v1, Reader v1, Reader v2, dev sampler harnesses, and offline determinism/evidence pipelines call the same Engine Core and sampler core modules where applicable; no surface is allowed to fork or reimplement core math. Public Reader versions project the same complete intrinsic result without rescoring. Rails, environment and evidence policy remain owned in other PF documents by title.
````````

## Redline RL-015

Operation: `REPLACE`. Classification: `CONSISTENCY`.

Original heading path (literal authored headings):

- `# 5\. Determinism & Identity Proofs \[Required-Now\]`
- `## **5.3 Evidence posture (titles/paths only)**`

Original location: lines 1376–1376; bytes [112097, 112489). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A38 (T-PF02).

Rationale: Preserve inspectable evidence standing while expressing the agent function independently of provider.

OLD

````````text
These surfaces together form the **ledger-centric, deterministic, text-based evidence posture** for the Engine: any acceptance decision for an epic must ultimately be justified by entries in the Human Index and Machine Mirror (and, where used, bundle manifests) that a human operator or a ChatGPT-class agent can inspect per PR. Detailed schema and tokenisation remain single-home elsewhere.
````````

NEW

````````text
These surfaces together form the **ledger-centric, deterministic, text-based evidence posture** for the Engine: any acceptance decision for an epic must ultimately be justified by entries in the Human Index and Machine Mirror (and, where used, bundle manifests) that a human operator or the executing agent can inspect per PR. Detailed schema and tokenisation remain single-home elsewhere.
````````

## Redline RL-016

Operation: `REPLACE`. Classification: `CONSISTENCY`.

Original heading path (literal authored headings):

- `# 5\. Determinism & Identity Proofs \[Required-Now\]`
- `## **5.3 Evidence posture (titles/paths only)**`

Original location: lines 1388–1388; bytes [113341, 113484). Expected literal OLD count: 1; producer-observed count: 1.

Source-ledger references: A38 (T-PF02).

Rationale: Make the repeated process-routing actor consistent with functional governance.

OLD

````````text
* **Epic-Process-Guide** — PR-first cadence (CodEx opens PR), required same-PR updates for Doc-Delta \+ indices, and CI parity/guardrails.  
````````

NEW

````````text
* **Epic-Process-Guide** — PR-first cadence (the executing agent opens PR), required same-PR updates for Doc-Delta \+ indices, and CI parity/guardrails.  
````````

END OF REDLINES
