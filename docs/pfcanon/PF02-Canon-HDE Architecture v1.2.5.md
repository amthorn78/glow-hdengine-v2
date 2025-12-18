# **0\. Front Matter**

**Title:** PF02-Canon-HDE Architecture  
 **Version:** v1.2.5  
 **Status:** Canon  
**Effective date:** 2025-12-13

 **Last Update Gate:** BN 8.3 Drain A10-14

---

## Intent & scope \[Required-Now\]

**What PF02 is.**  
 PF02 is the canonical map of the Glow HD Engine: which components exist (engine, adapter, presenter, caches, dev/QA surfaces, offline pipelines), what each is responsible for, and how data and control move between them in real flows. It stops short of contract bytes and detailed mechanics, which are owned by other PF-Canon documents; instead, it shows how those documents’ subjects are wired together inside one engine.

**Flows PF02 owns (architecture level only).**  
 PF02 defines component boundaries and scenario-level flows at the level of names and paths (not schemas or tokens) for:

* BodyGraph ingest & refresh (DB resolver, vendor seam, Engine, cache)

* Compat request (Reader and CLI surfaces over Engine Core \+ Presenter)

* Sampler & Engine Core evidence pipelines (offline determinism and QA artifacts)

* Narratives load & serve (Aux/CLI over Engine outputs and narrative packs)

* Dev/QA surface selection (Reader vs CLI vs dev harness for Live QA)

**Single homes (components).**  
 PF02 honors the single-home rule for:

* `engine/` — deterministic core and pure-compute modules (including sampler core and Engine Core)

* `adapter/` — single HTTP home (Reader, compat v1, internal/dev surfaces)

* `presenter/` — single canonical emitter (used by Adapter and CLI)

* the BodyGraph cache — the persistent store for Engine inputs (DB; not owned here in detail)

**Supersession rule (PF10 addenda).**  
 Where PF10 includes multiple numbered addenda on the same topic, the later number supersedes earlier guidance. PF02 reflects the latest position and routes work to canonical homes by title only (no version numbers).

**Contract-free.**  
 PF02 never carries headers, payload schemas, status matrices, exit codes, SLAs, or acceptance tables. It describes wiring and flows only; bytes, tokens, and schemas are always owned by other PF documents.

**Section labels.**  
 Each section is tagged with a status label to separate current behavior from near-term goals and future support.

**Routing by title only.**  
 Operational/transport details, CLI/Reader bytes, vendor specifics, QA tokens, and process policy are referenced by title only to their owning documents (for example: HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Schemas & Artifacts, HDE-Mechanics Guide, Glow QA Guide, HDE-Phased Epics, Epic-Process-Guide, Glow Infrastructure).

**Pack/bytes ownership (out of scope here).**  
 Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) are owned outside Architecture and cited by title, primarily in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

**Endpoint Catalog (single home; routing note).**  
 Success-endpoint discovery and A7 proofs are catalog-driven. The single home is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256` sidecar. The Catalog is internal-only and env-gated; non-prod entries are unreachable in prod (headers-only env-gate proofs). A7 proofs run only on a cataloged JSON success route; `/internal/version` is ops-only and excluded. Titles-only details live in HDE-CLI-API-Vendor-Ref and HDE-Governance; indexing discipline lives in HDE-Schemas & Artifacts. If a given repo state does not yet contain `docs/ENDPOINTS_CATALOG.json`, treat this path as reserved and required; its creation and wiring to A7 proofs are tracked via HDE-Build Checklist and HDE-Phased Epics, not by changing PF02.

**A7 invariants (routing note).**  
 Success proofs require `Vary: Authorization, Accept-Encoding`, strong quoted ETag on 200, HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), and 304 (after prior 200\) omitting both `Content-Type` and `Content-Length`. Encoding-invariance holds: for the same canonical LF-terminated body, the ETag identity and effective `Content-Length` are stable across accepted encodings. Concrete contracts remain in HDE-Governance and HDE-CLI-API-Vendor-Ref.

**DB runtime resolver (routing note).**  
 Resolver semantics are environment-aware:

* **Non-dev:** selection by presence only in this order: `DATABASE_URL → DB_BRIDGE_URL →` typed error (no connectivity probe).

* **Dev:** when `APP_ENV=dev` and `DATABASE_URL` is present but unusable, the resolver falls back to `DB_BRIDGE_URL` and proceeds (keys-only diagnostics; secrets/payloads never logged).

Evidence (headers/records only) is owned by HDE-Mechanics Guide and HDE-Build Checklist and indexed per HDE-Schemas & Artifacts. The full BodyGraph lifecycle flow is described in the System Overview section.

---

## Change control \[Required-Now\] (titles-only cross-refs; no duplicated bytes)

**PF02 owns wiring and flows only; all contract bytes, schemas, and tokens are routed by title to their single-home PF documents.**

**Transport / contract bytes.**  
 Owned outside Architecture: HDE-Governance and HDE-CLI-API-Vendor-Ref. Acceptance tokens are single-home in HDE-Governance §2.0; PF02 never enumerates tokens.

**Canonical JSON / pack / mirror.**  
 Policies, manifest shape, and the Evidence Index/mirror live in HDE-Schemas & Artifacts.

**PR-first posture.**  
 Epic-Process-Guide governs PR-first cadence. CodEx opens the PR automatically (one PR per epic/slice). Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`) must update **in the same PR** whenever proofs/artifacts change.

**Mirror hygiene (titles-only).**  
 The machine mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, one trailing LF), rejects unknown keys, and each record includes a `proof_anchor` to a path-proof stored alongside the artifact. A human-index hash sentinel may be enforced (see HDE-Schemas & Artifacts).

**Math semantics.**  
 Idempotence (preimage recipe), ordering, banding, and scoring live in HDE-Math-Spec.

**Enforcement & CI.**  
 Jobs, guards, allow-lists, and evidence procedures live in the HDE-Mechanics Guide.

**Infrastructure.**  
 Names/locations live in Glow Infrastructure; operational evidence/policy remain owned by HDE-Governance.

**Process & PR workflow.**  
 Epic-Process-Guide governs PR-first cadence; Appendix D (human) and the machine mirror must be updated in the same PR.

**Freeze-pack linkage (release identity).**  
 Release identity is pack-derived; any change to frozen constants, the direct Motor→Throat set, thresholds, or catalog membership/order requires an HDE-Schemas & Artifacts manifest update and yields a new `release_id` (titles-only).

**Endpoint proofs & ops exclusion (routing).**  
 A7 proofs run only on a cataloged Endpoint Catalog (JSON success) route (HDE-CLI-API-Vendor-Ref); `/internal/version` is ops-only and not A7-eligible (titles-only to HDE-Governance).

**Narratives routing (titles-only).**  
 Reader remains narrative-free. Narrative bytes are carried via Aux/CLI and live in HDE-CLI-API-Vendor-Ref; suppression/A7 policy for Aux lives in HDE-Governance. PF02 stays contract-free.

**Cross-doc referencing.**  
 Use titles only; do not include version numbers.

**No contract bytes here.**  
 Any change that would introduce contract bytes or duplicate content is rejected; instead, add or update a titles-only reference to the owning document.

# 1\. Architectural Principles \[Required-Now\] 

CLI parity work remains open; Architecture keeps the single-emitter rule while HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide close parity on the CLI path.

## 1.1 Single homes

**engine/** — deterministic core and pure-compute modules.  
 No time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. Inputs are pure data; outputs are pure data; side effects are forbidden.

Within `engine/`, the sampler core module and Engine Core module are single homes for their behaviors:

* **Sampler core module** (names-only). A pure-compute module under `engine/` that owns sampler/ranker behavior: pool formation, eligibility, ordering, and sampling decisions. It does not import transport, CLI, HTTP, evidence tooling, or environment.

* **Engine Core module** (names-only). A pure-compute module under `engine/` that owns neutral and directional compatibility metrics, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling. It does not import transport, CLI, HTTP, evidence tooling, or environment.

All runtime surfaces and offline pipelines that need sampler or Engine Core behavior must call these modules in-process; they MUST NOT reimplement sampling or compat logic.

**adapter/** — single HTTP home.  
 Mounts runtime surfaces and applies guards/rails. Calls the Engine (including sampler core and Engine Core modules) in process and never hand-crafts public JSON; only the Presenter’s emitter produces public bytes. No alternate HTTP homes and no duplicate or legacy trees.

**presenter/** — single canonical emitter.  
 One code path produces public JSON for all callers (HTTP and CLI). No alternate serializers, formatters, or per-surface emitters.

**BodyGraph cache** — persistent Engine input store (names-only).  
 The BodyGraph cache (database) is the single persistent store for BodyGraph inputs to the Engine. Adapter/CLI read and write BodyGraphs through the DB runtime resolver; Engine remains stateless with respect to source. The lifecycle of BodyGraph data (vendor fetch, cache, refresh) is described in the System Overview; DB instance and schema names live in Glow Infrastructure.

**Guards (normative).**

* Deny-list legacy trees: `core/`, `server/`, `adapters/` (plural) and any alternate HTTP homes; CI must fail on imports from these paths.  
* Single-emitter allow-list: only the Presenter’s emitter entrypoint may serialize public bytes; all other serializers are forbidden on public paths.  
* No ad-hoc serialization on public paths: forbid direct `json.dumps(...)`, `jsonify(...)`, templating, or string-built JSON.  
* Role boundaries: Adapter owns route registration and vendor/DB wiring; Presenter owns emission; Engine (including sampler core and Engine Core modules) owns math and pure-compute behavior. No cross-role leakage.  
* **Repo layout note (HTTP surfaces).** Implementation may temporarily host some HTTP handlers in modules outside the `adapter/` directory, but Architecture still treats all HTTP entrypoints as belonging to the adapter component. There MUST NOT be a second HTTP home: new or refactored HTTP surfaces must converge under adapter responsibilities and must not bypass adapter-level guards or the single Presenter emitter.

**Routing (titles-only).**

* Enforcement guards and CI procedures live in HDE-Mechanics Guide.

* Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) live in HDE-Schemas & Artifacts.

* DB instance names, schemas, and environment wiring live in Glow Infrastructure.

* Math semantics (including compatibility and sampler math) live in HDE-Math-Spec.

  ---

  ## 1.2 Determinism & parity

**Canonical JSON.**  
 All public JSON is UTF-8 (no BOM), keys sorted in ASCII order, compact separators, and ends with exactly one newline (LF). Arrays used as sets are deduplicated and ASCII-sorted. Canonicalization rules are owned by HDE-Schemas & Artifacts §4 (titles-only).

**Two-step idempotence.**  
 Build the idempotence preimage (excluding `idempotence_hash`), canonicalize it, compute `sha256(preimage_bytes)`, then insert `idempotence_hash` and re-emit the final LF-terminated body. The preimage recipe and hashing posture are owned by HDE-Math-Spec (titles-only).

**Single emitter entrypoint.**  
 CLI and Adapter call the same Presenter emitter symbol; Architecture forbids alternate public-byte code paths (no ad-hoc serializers on public paths).

**Reader↔CLI parity.**  
 For mirrored surfaces where the CLI emits Reader v1 bytes (stdout or reader-dump, per HDE-CLI-API-Vendor-Ref), those CLI bytes are byte-identical to the Reader 200 body (single emitter).

**AB↔BA parity.**  
 For the same pair of inputs in either order, the public bytes are identical (pair normalization).

**Two-run identity.**  
 Re-emitting the same logical representation produces byte-identical output.

**Locale pins (required).**  
 All canonicalization and compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Offline pipelines & evidence generators.**  
 Offline pipelines and evidence generators (for example, determinism jobs and evidence-family generators) MUST invoke Engine Core and sampler core modules with pinned fixtures and MUST honor the same canonical JSON, idempotence, AB↔BA, two-run identity, and locale pins as runtime requests. They produce governed artifacts into evidence families and update the human Evidence Index and machine mirror in the same PR as the code changes; schemas, artifact families, and gating rules live in HDE-Schemas & Artifacts, HDE-Mechanics Guide, HDE-Build Checklist, and Epic-Process-Guide.

**Routing (titles-only).**  
 Payload schemas, category construction, and transport/header rules live in HDE-CLI-API-Vendor-Ref and HDE-Governance; canonical JSON, pack/manifest, and the machine Evidence Index live in HDE-Schemas & Artifacts; idempotence preimage and math live in HDE-Math-Spec. Architecture remains contract-free and describes invariants only.

---

## 1.3 Separation of surfaces \[Required-Now\]

**Public vs internal/dev.**  
 Public surfaces expose only the approved Reader envelope (bands-only, numeric-free) produced by the Presenter. Internal/dev surfaces exist for diagnostics and local harnesses and are not public data planes. The internal-ops identity route `/internal/version` is governed in HDE-Governance §10.5; PF02 stays contract-free and does not restate headers (titles-only routing).

**Endpoint Catalog (success) proofs.**  
 A7 proofs run only on a cataloged Endpoint Catalog (JSON success) route, named and owned in HDE-CLI-API-Vendor-Ref. PF02 does not enumerate routes or bytes; it routes discovery/proofs by title and keeps contract bytes out of Architecture.

**Keys-only outputs (Engine).**  
 The Engine, including sampler core and Engine Core modules, never emits narratives or free text; it produces only structured keys and metrics that the Presenter serializes. Public bytes are produced exclusively by the Presenter’s single emitter (shared by Adapter and CLI).

**Aux Narrative surface (concept-only).**  
 Narrative text (when present) is served only via Aux/CLI (not on Reader 200). Endpoint bytes live in HDE-CLI-API-Vendor-Ref; suppression carve-out and A7 posture live in HDE-Governance. PF02 remains contract-free and routes by title only. Engine outputs remain keys-only; Aux surfaces interpret those keys together with narrative packs (HDE Narratives Guide, HDE-Mechanics Guide, and HDE-Schemas & Artifacts by title).

**No leakage across boundaries.**  
 Adapter does not reveal internal state or non-public fields; Engine math remains isolated from runtime concerns; no cross-role fields or headers leak into public envelopes. Narratives and Aux surfaces sit above Engine outputs and are not visible to Engine or Reader 200\.

**Locale & canon seams.**  
 All canonicalization and byte compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Presenter emits canonical JSON; canonical JSON policy and the machine Evidence Index (JSONL mirror schema and parity) are owned by HDE-Schemas & Artifacts §4 (titles-only).

**Routing (titles-only).**

* Headers/transport and acceptance tokens → HDE-Governance (single-home roster in §2.0).

* Public Reader/CLI bytes and the Endpoint Catalog → HDE-CLI-API-Vendor-Ref.

* Canonical JSON, pack/manifest, and the machine mirror → HDE-Schemas & Artifacts.

Architecture remains contract-free.

# **2\. System Overview (Blocks & Flows) \[Required-Now\]**

## **2.1 Components & responsibilities (single homes)**

**engine/** (deterministic core). Computes compatibility and related math in process with no time, network, file I/O, or randomness. Accepts normalized inputs and returns normalized structures.

**adapter/** (single HTTP home). Hosts runtime surfaces and guards. Performs lightweight input validation, then calls the Engine synchronously. It never hand crafts public JSON. Routing (titles only): service start-command symbol, exposure posture, and infrastructure locations live in **Glow Infrastructure**; operational policy and evidence ownership live in **HDE-Governance**.

**presenter/** (canonical emitter). Provides the one serializer and emitter used by all surfaces (CLI and HTTP). Ensures canonical formatting, idempotence preimage discipline, and AB↔BA parity at the byte level. Routing (titles only): emitter invocation/validation runs and infrastructure locations live in **Glow Infrastructure**; operational policy and evidence ownership live in **HDE-Governance**.

**database** (persistent BodyGraph cache). An external store for BodyGraphs enabling reuse of previously computed results. The Adapter reads from and writes to this database (on BodyGraph fetches) so that subsequent requests can retrieve the cached BodyGraph instead of calling the vendor. The Engine remains stateless – it simply consumes whatever BodyGraph data the Adapter provides from this cache or a live call.

### **Repo map (normative)**

engine/ \# math only  
 adapter/ \# single HTTP home  
 presenter/ \# single emitter entrypoint for all public bytes

**Sampler and Engine Core modules (names-only)**

**Names & roles.**

* The canonical sampler behavior lives in a single module under the `engine/` tree, referred to here as the **sampler core module** (currently `engine.sampler.core`). It owns sampler/ranker behavior: pool formation, eligibility, ordering, and sampling decisions.

* The canonical Engine Core behavior lives in a single module under the `engine/` tree, referred to here as the **Engine Core module** (currently `engine.core.core`). It owns the core compatibility computation: neutral and directional metrics, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling.

**Behavior-only boundary.**

* Both modules are **pure compute**: no time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. They accept normalized inputs and return normalized structures; they do not know about CLI commands, HTTP routes, rails, or evidence files.

* These modules are the **single homes** for sampler and Engine Core behavior. Any CLI, HTTP, or dev harness that needs sampler/core behavior MUST call into these engine modules rather than reimplementing sampling or core logic.

**Surfaces vs evidence (concept-only).**

* CLI and HTTP harnesses that expose sampler or Engine Core behavior live outside `engine/` (for example, in adapter/ or CLI trees) and are responsible for:

  * collecting and validating inputs,

  * enforcing rails and APP\_ENV gating, and

  * invoking the sampler/Engine Core modules in-process.

* Evidence families, determinism pipelines, and acceptance maps that speak about sampler/core proofs treat these engine modules as the behavior source. The **shapes and paths** of those evidence artifacts are single-home in **HDE-Schemas & Artifacts**, the **HDE-Mechanics Guide**, and the **HDE-Build Checklist**, not in Architecture.

**Routing (titles-only).**

* Detailed sampler/core mechanics, including evidence generators and determinism pipelines → **HDE-Mechanics Guide**.

* Evidence schemas, artifact keys, and indices/mirror discipline for sampler/core families → **HDE-Schemas & Artifacts**.

* QA tokens and epic D-goals for sampler/core behavior and evidence → **Glow QA Guide** and **HDE-Phased Epics**.

* CLI and HTTP harness bytes for sampler/core behavior → **HDE-CLI-API-Vendor-Ref**.

### **Deny-list (normative)**

The following paths MUST NOT exist or be imported on public paths: `core/`, `server/`, `adapters/` (plural), or any alternate HTTP home. CI MUST fail on imports from these paths.

### **Emitter rule (normative)**

Only the presenter’s emitter entrypoint MAY serialize public bytes. All other serializers and any ad hoc `json.dumps(...)`, `jsonify(...)`, templating, or string-built JSON on public paths are FORBIDDEN.

### **Routing (titles only)**

Concrete guard checks and scripts live in **HDE-Mechanics Guide**, and process/PR workflow (CodEx staging, PR-first merging, repo-docs/Evidence Index updates) lives in **Epic-Process-Guide**.

---

## **2.2 High-level flow (request → compute → persist → emit)**

This subsection defines the **generic architecture template** for how requests move through the Engine. It is the pattern specialised later by:

* BodyGraph lifecycle (§2.3)

* Compat requests (§2.4)

* Offline determinism/evidence flows (§2.x)

* Narratives (§3.5–§3.7)

It remains **contract-free** and routes bytes and schemas by **title only**.

1. **Collect & validate inputs**

    CLI or Adapter gathers inputs and performs minimal structural checks (required fields present, types coherent).

   * Detailed payload shapes and schema ownership are routed by title (**HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**).

   * No secrets in payload logs.

   * Malformed inputs fail closed.

2. **Compute in Engine (pure)**

    Adapter/CLI calls Engine functions in-process.

   * Engine modules (including `engine.core.core` and `engine.sampler.core`) run pure: **no I/O, clocks, environment reads, randomness, or import-time side effects**.

   * They accept **normalized data structures** and return **normalized results** (including pair normalization for AB↔BA neutrality).

   * Side effects are forbidden.

3. **Persist derived state (if applicable)**

    For flows that produce durable state (for example BodyGraphs), the Adapter persists the Engine result and metadata to the database cache using the DB runtime resolver seam.

   * For BodyGraph flows specifically, the Adapter **upserts** the BodyGraph and its metadata, then consults this cache on subsequent requests with the same normalized inputs to avoid unnecessary vendor calls.

   * This persistence is part of the **canonical flow in all environments**, not a toggle.

   * Detailed BodyGraph behaviour is described in §2.3 and in **HDE-Schemas & Artifacts** and **HDE-Governance** by title.

4. **Emit via Presenter (single emitter)**

    Presenter uses the **single canonical emitter** shared by Adapter and CLI.

   * No ad-hoc serializers on public paths.

   * No test-only bypasses.

5. **Canonicalization:**

   * UTF-8 (no BOM)

   * ASCII-sorted keys

   * Compact separators

   * Arrays-as-sets deduped and ASCII-sorted

   * Exactly **one** trailing LF

6. **Idempotence:**

   * Build the canonical preimage excluding `idempotence_hash`.

   * Compute `sha256(preimage_bytes)`.

   * Insert `idempotence_hash`.

   * Re-emit the LF-terminated body.

7. All canonicalization and byte-level comparisons run with:

   * `LC_ALL=C`

   * `LANG=C`

   * `TZ=UTC`

8. **Return response (streams discipline)**

   * **CLI:**

     * Write the public envelope to **stdout** (exact bytes; one LF).

     * Typed JSON errors go to **stderr**; a successful command never writes to stderr.

   * **Adapter:**

     * Return the same bytes to the client.

     * Error surfaces use typed JSON.

9. For mirrored surfaces, **Reader↔CLI parity holds**: both consume the same Engine modules and Presenter emitter and must produce **byte-identical public output** for identical inputs.

---

### **2.2.5 Alpha surfaces**

Compat v1 via Adapter, plus `showcompat` in CLI, both use the same Presenter emitter path over Engine Core outputs.

For mirrored compat surfaces:

* Output must be non-empty canonical JSON.

* Reader and CLI bytes must be identical for the same normalized inputs (single-emitter rule).

* The compat request flow is detailed in §2.4 (Reader/CLI → Engine Core → Presenter) and remains contract-free; concrete shapes and tokens live in **HDE-CLI-API-Vendor-Ref**, **HDE-Math-Spec**, and **HDE-Schemas & Artifacts** by title.

---

### **2.2.6 Proofs & routing (titles-only)**

**Policy.**  
 PF02 describes **where** and **how** proofs attach to the architecture but keeps all proof bytes out of Architecture. A7 and other transport-level proofs are routed by **title only** to their single homes; PF02 remains contract-free.

**Success-endpoint proofs (A7).**

* A7 proofs run only on a **cataloged JSON success route** named in the Endpoint Catalog (`docs/ENDPOINTS_CATALOG.json` and its `.sha256` sidecar).

* The Catalog is internal-only and env-gated; evidence must show that non-prod entries are **unreachable in prod** (headers-only env-gate proof).

* `/internal/version` is operator-only and **not A7-eligible**.

* Endpoint naming, exposure posture, and validator details live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**.

**A7 invariants (route-only).**

Architecture requires that success endpoints that claim A7 compliance obey:

* Strong quoted ETag on 200\.

* HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`).

* 304 only after a prior 200, omitting both `Content-Type` and `Content-Length`.

* `Vary: Authorization, Accept-Encoding`.

* Encoding-invariance: for the same canonical LF-terminated body, ETag identity and effective `Content-Length` remain stable across accepted encodings.

Concrete header matrices, status tables, and validator implementations live in **HDE-Governance** and **HDE-CLI-API-Vendor-Ref** by title.

**Aux Narrative proofs.**

* Aux narrative success routes follow the same **Catalog-based success-route rule**.

* Suppression semantics (200 with no body and no ETag, optional policy header) are governed in **HDE-Governance §10.4** and **HDE-CLI-API-Vendor-Ref**; PF02 does not restate headers or payloads.

**Ops exclusion.**

* `/internal/version` is operator-only and explicitly **excluded** from A7 proofs.

* Ops behaviour and headers are governed in **HDE-Governance §10.5**.

**Public envelope construction & schemas.**

* The public envelope (six-key Reader/CLI envelope, bands-only, numeric-free) and its schema live in **HDE-CLI-API-Vendor-Ref** and **HDE-Schemas & Artifacts**.

* PF02 treats them as contract surfaces and refers to them by title only.

**Idempotence & math.**

* The idempotence preimage recipe, ordering, banding, and scoring semantics live in **HDE-Math-Spec**.

* Architecture requires that all public bytes emitted by Presenter honor those semantics; it does **not** redefine them here.

---

## **2.3 What this document does not contain (route by title)**

PF02 is **intentionally contract-free**. It names components, flows, and invariants, but it does **not** define transport or policy bytes. It does **not** carry:

* HTTP header matrices, caching or writers rules, conditional delivery (200/304/HEAD), error envelope schemas, or auth policy.

* CLI command bytes, exit codes or streams, admin sidecar formats, or payload field examples.

* Vendor request or response shapes, timeouts or retries, or rate-limit behaviour.

All such details are owned elsewhere and are referenced by **title only** from this document.

Even in the scenario flows above (and those that follow for BodyGraph, compat, offline pipelines, and narratives), PF02 deliberately omits specific payload schemas, evidence schemas, QA tokens, and SLAs. Those live in:

* **HDE-CLI-API-Vendor-Ref**

* **HDE-Schemas & Artifacts**

* **Glow QA Guide**

* **HDE-Phased Epics**

by title only.

---

## **2.4 BodyGraph ingest & durability \[Required-Now\]**

This subsection describes the BodyGraph lifecycle at the architecture level:

request → DB runtime resolver → vendor (when needed) → Engine → DB persist → subsequent requests

It ties together the DB cache, vendor seam, and Engine’s stateless contract.

### **Adapter source policy (env-aware)**

* **Prod / non-dev:**

  * The database is the **canonical source** for BodyGraphs on request paths.

  * The Adapter uses the DB runtime resolver (presence-based selection: `DATABASE_URL → DB_BRIDGE_URL → typed error`) to locate the store.

  * Vendor calls occur only via **explicit triggers or scheduled refresh jobs**, never inline on the public request path.

* **Dev:**

  * Direct vendor calls are allowed on request paths under SAFE rails.

  * On successful vendor fetch and Engine computation, the Adapter **upserts** the resulting BodyGraph and metadata into the DB cache for repeatability.

In all environments, this persistent caching is **canonical**, not a feature toggle.

* Policy/tokens live in **HDE-Governance**.

* Exposure rules live in **HDE-CLI-API-Vendor-Ref**.

* Evidence and checklist hooks live in **HDE-Mechanics Guide** and **HDE-Build Checklist**.

* Indices and mirror ownership live in **HDE-Schemas & Artifacts**.

### **Lifecycle: DB resolver → vendor seam → Engine → DB**

1. When a request needs a BodyGraph, Adapter/CLI first consults the database using the DB runtime resolver (env-aware; see the resolver routing note in §1).

2. On a **cache hit** (valid BodyGraph found for the normalized input fingerprint), the Adapter passes that BodyGraph into the Engine; no vendor call is made.

3. On a **miss** or TTL expiry, the Adapter:

   * Calls the vendor through the vendor seam owned by **HDE-Mechanics Guide**, **HDE-CLI-API-Vendor-Ref**, and **HDE-Governance** (titles only).

   * Normalises the response into the BodyGraph input shape.

   * Passes that data into Engine.

   * **Upserts** the computed BodyGraph into the DB with TTL/SWR and circuit-breaker semantics.

Dev vs prod rails, vendor routes, and retry/timeout policies are governed outside PF02; this section only fixes the **architectural ordering and responsibilities**.

### **Durability objects (names-only)**

* `body_graphs`

  * Rows include `user_id`, `vendor`, `vendor_version`, `input_fingerprint`, `payload`, `created_at`, `refreshed_at`, `ttl_at`.

  * Uniqueness on `{user_id, vendor, vendor_version, input_fingerprint}`.

* `body_graphs_current`

  * Materialised view or table representing the latest valid BodyGraph per `{user, vendor}`.

Normalization, fingerprinting, and any additional fields are single-home in **HDE-Schemas & Artifacts**; PF02 only names the objects and their architectural roles.

### **Refresh posture (out-of-band)**

* Refreshes are performed **out-of-band** from the main request path.

* Uses TTL and stale-while-revalidate semantics and a circuit breaker (`fail`, `window_s`, `cooldown_s`) to respect vendor rate limits and stability.

* Inline vendor calls on prod Reader/compat success paths are **forbidden**; refresh jobs and admin tools own vendor traffic.

* Evidence families (records-only) for refresh behaviour are indexed and governed in **HDE-Schemas & Artifacts** and wired into QA via **HDE-Mechanics Guide** and **HDE-Build Checklist**.

### **Source invariance (concept)**

For the same normalized inputs, **DB-sourced and vendor-sourced BodyGraphs** must render to **identical canonical bytes** once passed through Engine and Presenter (single emitter).

* The Adapter is responsible for consistent normalization and cache semantics.

* Engine and Presenter treat inputs as pure data and do not see the source.

* Proof routing lives in **HDE-Mechanics Guide** and **Glow QA Guide**; public bytes live in **HDE-CLI-API-Vendor-Ref**.

### **Engine stateless contract**

* The Engine has **no internal mode or toggle** for data source or environment.

* It always runs against the BodyGraph data the Adapter/CLI provides.

* It never alters behaviour based on dev vs prod or cache vs vendor.

* All source-selection logic resides in the Adapter/CLI layer; PF02 treats this separation as a **hard architectural boundary**.

---

## **2.5 What this document does not contain (route by title)**

This subsection is the **canonical home** for PF02’s non-goals. It reiterates that Architecture names **components, flows, and invariants**, but never carries concrete contracts. PF02 does **not** define:

* HTTP header matrices, caching or writers rules, conditional delivery patterns (200/304/HEAD), error envelope schemas, or auth policy.

* CLI command bytes, exit codes or streams, admin sidecar formats, or payload field examples.

* Vendor request or response shapes, timeout/retry policies, or rate-limit behaviour.

* Specific schemas for BodyGraph rows, compat envelopes, sampler/core evidence families, or QA tokens.

All such details are owned in their respective single-home documents and referenced by **title only**:

* Transport, A7 posture, auth, and ops: **HDE-Governance**.

* Public Reader/CLI surfaces, request/response schemas, and admin/dev routes: **HDE-CLI-API-Vendor-Ref**.

* Canonical JSON rules, pack/manifest shape, BodyGraph and evidence schemas, and INDEX/Mirror layout: **HDE-Schemas & Artifacts**.

* QA tokens, rails, and process: **Glow QA Guide**, **HDE-Phased Epics**, **HDE-Mechanics Guide**, **HDE-Build Checklist**, and **Epic-Process-Guide**.

Even where PF02 introduces concrete flows (BodyGraph lifecycle, compat request flow, offline pipelines, narratives), it **deliberately** omits payload schemas, evidence schemas, byte-level contracts, and QA tokens. Those are always routed by **title only** to their owning PF-Canon documents.

# **3\. Runtime surfaces (by responsibility, not bytes)**

This section names runtime surfaces and their responsibilities. It remains **contract-free**. Any payload shapes, header matrices, status codes, conditional delivery behaviour, or CLI/Reader specifics are routed by title to:

* **HDE-CLI-API-Vendor-Ref** (public envelope, request/response shapes, CLI/Reader semantics)

* **HDE-Governance** (A7 validators, evidence posture, transport acceptance, ops signals)

* **HDE-Schemas & Artifacts** (canonical JSON policy, pack/manifest, machine Evidence Index schema and parity)

Titles only; **no bytes restated here**.

---

## **3.1 Compat v1 \[Implemented\]**

**Role & purpose.**  
 `/api/compat/v1` is the adapter’s compatibility surface. It calls the Engine in-proc and returns the public compatibility envelope emitted by the single canonical Presenter emitter. It does **not** expose internals or narratives.

**Validation (high level).**

* **GET:** must not include a JSON body.

* **POST:** expects a valid pair definition and viewer preferences that are:

  * well-formed

  * complete (all ten Magic-10 keys)

  * within allowed ranges

* Malformed or incomplete inputs are rejected. (Detailed shapes live in **HDE-CLI-API-Vendor-Ref**.)

**Presenter rule.**  
 The adapter never hand-crafts public JSON. Only the Presenter’s single emitter serializes public bytes for **all** callers (HTTP and CLI).

**Parity expectations.**

* For identical inputs, public bytes match CLI output (byte identity).

* Output is non-empty canonical JSON (LF-terminated).

* Locale pins for byte checks: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Routing (titles-only).**

* Request/response details, field lists, examples, CLI↔Reader byte-parity rules → **HDE-CLI-API-Vendor-Ref**

* A7 validators and header behaviour → **HDE-Governance**

* Canonical JSON policy → **HDE-Schemas & Artifacts**

* Process & PR workflow (PR-first; Evidence Index and mirror updated in the same PR) → **Epic-Process-Guide**

See §2.4 for the compat request flow, including how BodyGraph, Engine Core, and Presenter interact for this surface.

---

## **3.2 Reader v1 \[Required-Now\] (public success route)**

**Intent.**  
 A public Reader surface on the adapter that uses the same canonical emitter path as the CLI. It exposes the six-key public envelope for client apps without duplicating computation or serialization logic.

**Responsibilities (conceptual).**

* Accept normalized inputs or references and perform lightweight structural checks before calling the Engine in-proc.

* Return the public envelope via the canonical emitter (no narratives, no internal fields, no side effects).

* Maintain CLI↔Reader byte parity for identical inputs and environment; parity is a requirement (bytes owned elsewhere).

* Obey A7 success-route posture (routing notes below).

* Use DB-backed BodyGraphs for compat computation, following the BodyGraph lifecycle (no inline vendor I/O on Reader 200).

**Non-goals.**

* No alternate serializers, payload shaping, or per-surface formatters.

* No direct vendor/network calls on the public success route.

**A7 proof surface (route-only; titles-only).**

* **Cataloged route only.**  
   Reader success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (**HDE-CLI-API-Vendor-Ref**). The Catalog’s single home is `docs/ENDPOINTS_CATALOG.json` (+ `.sha256` sidecar). Proofs target a route listed there; `/internal/version` remains excluded. Env-gate proof is mandatory (headers-only).

* **Catalog posture.**  
   The Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod. Capture a headers-only env-gate proof.

* **A7 invariants to satisfy.**  
   Require:

  * `Vary: Authorization, Accept-Encoding`

  * Encoding invariance of identity (ETag) and effective `Content-Length` across accepted encodings

  * HEAD 200 validator parity with `Content-Type == GET` and `Content-Length == len(identity 200 body)`

  * 304 only after prior 200, with no body and omitting both `Content-Type` and `Content-Length`

* **Ops exclusion.**  
   `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* Field definitions, examples, conditional delivery, and parity proofs → **HDE-CLI-API-Vendor-Ref**

* A7 acceptance policy and tokens → **HDE-Governance**

* Canonical JSON policy, pack/manifest, and machine mirror discipline → **HDE-Schemas & Artifacts**

Reader’s public success route uses the same Engine Core \+ Presenter flow as compat v1. **HDE-CLI-API-Vendor-Ref** and **HDE-Governance** own success envelope bytes and A7 posture by title, and Reader obtains BodyGraphs via the DB-backed lifecycle described in §2.3.

---

## **3.3 Sample (dev harness) \[Implemented\] (dev-only)**

**Intent.**  
 A local, non-public developer harness on the adapter for manual and automated checks during development. It shares the single canonical emitter with CLI and Reader so public bytes are identical for identical inputs.

**Responsibilities (conceptual).**

* Provide minimal endpoints or commands to exercise Engine paths with fixture inputs.

* Perform lightweight structural validation before calling the Engine in-proc.

* Emit results via the single canonical emitter (no alternate serializers or formatting).

* Maintain CLI↔harness parity for identical inputs and environment (bytes owned elsewhere).

**Non-goals.**

* No public availability.

* No vendor/network calls.

* No persistence of user data.

* No narrative text.

* No transport or policy bytes are defined in PF02.

**Gating & posture (dev-only; titles-only routing).**

* Harness is dev-only; never mounted in production.

* Rails closed by default (for example, `SAFE_MODE=1`, `ALLOW_NETWORK=0`); no vendor I/O.

* Optional GET/HEAD/304 captures may be used for local evidence, but authoritative A7 proofs do **not** run here; they run on a cataloged JSON success route (Endpoint Catalog).

* All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`; LF-terminated canonical JSON via the shared emitter.

Sample harness uses the same Presenter emitter and Engine Core behaviour as compat v1 but runs under closed rails and is never used for A7 proofs; see §2.4 and §5 for compat flow and evidence-plane details.

**Routing (titles-only).**

* Dev-harness routing/guards and optional GET semantics → **HDE-CLI-API-Vendor-Ref**

* A7 proof surface policy and ops exception (`/internal/version`) → **HDE-Governance**

* Canonical JSON policy, Evidence Index/mirror discipline (same-PR parity) → **HDE-Schemas & Artifacts**

  ---

  ## **3.4 Internal ops signals (speculative, future support)**

**Names & roles (concept only).**

* `/internal/healthz` — **liveness.** Constant-time “process is up” probe; no Engine invocation; no disk or network; no PII.

* `/internal/readyz` — **readiness.** “Can serve traffic” probe; checks prerequisites such as config loaded, emitter path available, and rails posture sane without running compat math or touching vendors.

* `/internal/version` — **identity.** Build and config snapshot for drift detection. Reads identity fields only and is side-effect-free. No secrets.

These routes do not touch Engine Core, sampler core, or vendor; they are liveness/identity-only surfaces.

**Non-goals.**  
 No payload or header matrices, auth policy, or acceptance tables in this section. These are ops signals, not product surfaces.

**Routing (titles-only).**  
 All concrete transport or policy details for these signals are owned by **HDE-Governance**. See **HDE-Governance** §10.5 for `/internal/version` posture and acceptance.

---

## **3.5 Internal-ops identity (route-only)**

**Purpose.**  
 Adapter exposes internal-ops identity/diagnostic routes for operations and monitoring. These are not public data planes.

**Responsibility split.**

* Adapter wires the route and applies guards.

* Presenter emits canonical JSON when applicable.

* Engine remains pure compute. No cross-role leakage.

**Governance pointer.**  
 Behaviour, headers, and acceptance tokens are governed by **HDE-Governance**. PF02 remains contract-free and does not restate header/body rules.

**Contract posture (titles-only).**  
 **HDE-Governance** governs invariants for the identity surface (for example, no-store, no ETag, HEAD 200 with `Content-Type` parity and `Content-Length == identity GET`, conditionals ignored / never 304\) and owns A7 evidence. PF02 points by title only.

**Evidence & indexing (titles-only).**  
 Proof artifacts and success-endpoint snapshots are indexed per **HDE-Governance** / **HDE-Schemas & Artifacts**; the human Evidence Index and the machine JSONL mirror must remain 1:1 (updated in the same PR).

**Non-goals.**  
 No public contract bytes, no payload schemas, no alternate emitters, no persistence, and no vendor/network calls from this surface.

**Routing (titles-only).**

* Identity invariants, acceptance, A7 evidence → **HDE-Governance**

* Endpoint Catalog / success JSON → **HDE-CLI-API-Vendor-Ref**

* Canonical JSON and machine mirror → **HDE-Schemas & Artifacts**

  ---

  ## **3.6 Aux Narrative (concept-only, route-only) \[Speculative\]**

**Role.**  
 Serve deterministic narrative text **outside** the public Reader surface. No narratives appear on Reader 200\.

**Responsibilities (conceptual).**

* Adapter wires the Aux route; Presenter emits text via the single canonical emitter; Engine remains pure compute (keys only).

* Text constraints: no CR characters; LF-terminated output (schema/constraints routed by title).

* Maintain CLI admin preview parity (bytes owned elsewhere; titles-only routing).

**Proof surface (route-only; titles-only).**

* **Cataloged route only.**  
   Aux success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (**HDE-CLI-API-Vendor-Ref**).

* **Catalog posture.**  
   The Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof.

* **Suppression carve-out.**  
   When suppressed, Aux returns 200 with no body and no ETag (policy header optional).

* **Ops exclusion.**  
   `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* Endpoint route bytes and CLI admin preview → **HDE-CLI-API-Vendor-Ref**

* Suppression carve-out and A7 posture for Aux → **HDE-Governance**

* Composer response/schema & narratives pack catalogs → **HDE-Schemas & Artifacts**

  ---

  ## **3.7 Narratives architecture (two-plane; concept-only)**

**Planes.**

* **Authoring plane (DB-backed):** intake, lints, preview, publish pointer, audit.

* **Runtime plane (file-backed):** engine loads a sealed pack by `pack_sha`; no DB reads on the hot path.

**Identity & store (names-level).**

* Manifest-driven identity: `pack_sha = sha256(canonical manifest bytes)`.

* Authoritative path: object storage at `/narratives/<pack_sha>/…`; the repo carries the manifest \+ evidence.

* Loader: fetch → verify → atomic symlink swap → load; on any verify mismatch, fail-closed (keep previous pack); keys-only logs.

* Ops: CLI-first operations; admin HTTP optional later.

* Reader posture: Reader stays narrative-free; Aux suppression returns 200 empty, no ETag (policy by title).

Engine outputs are keys and structured metrics; narratives never live in `engine/`. Aux surfaces interpret Engine outputs in combination with narratives packs (owned by the Narratives Guide, **HDE-Mechanics Guide**, and **HDE-Schemas & Artifacts** by title) to produce text. Reader 200 stays narrative-free; narrative suppression returns 200 with an empty body by design.

**Ownership & indexing (titles-only).**

* Evidence/indexing discipline → **HDE-Schemas & Artifacts**

* Mechanics for loading, swapping, and failure modes → **HDE-Mechanics Guide**

* Narrative posture, authoring semantics, and pack contents → **Narratives Guide**

  ---

  ## **3.8 Reader dev/QA posture & services \[Required-Now\]**

**Intent.**  
 Record, at the architectural level, how the Reader runs in dev/QA environments and how Live QA chooses between Reader and other entrypoints, while keeping PF02 contract-free. Concrete commands, ports, and environment wiring remain single-home in other documents and are referenced here by title only.

### **3.8.1 Dev/QA Reader availability**

* Reader v1 is exposed through the adapter process as one of the runtime surfaces named in this section. It uses the single canonical Presenter emitter and never hand-crafts public JSON.

* In any dev/QA console that plans to exercise Reader or other HTTP runtime surfaces, the adapter/Reader process **must** be started explicitly using the canonical start command and environment described in **Glow Infrastructure** and the **HDE-Mechanics Guide**. Live QA **must not** rely on guessing hostnames or ports.

* PF02 does not introduce service names, ports, or commands. Those details are single-home in **Glow Infrastructure**, the **HDE-Mechanics Guide**, and any field guides that describe running the adapter and Reader inside a dev container (including Codespaces). This document only records the responsibility that HTTP-based tests must target a known, running Reader instance.  
* In dev/QA, the adapter/Reader stack is hosted by a concrete framework development HTTP server (currently a Flask dev server) that exposes the same Reader and internal/dev sampler routes as the production adapter. Architecture treats this dev server as part of the adapter and dev harness component: it is a real, required piece of the system in dev/QA, but the choice of framework and all start commands, ports, and environment wiring remain the responsibility of **Glow Infrastructure** and **HDE-Mechanics Guide**, not PF02.  
* The dev Reader harness used in dev/QA consoles (including Codespaces) MUST expose the canonically required dev/internal HTTP surfaces for QA, using the same Presenter emitter and error-handling semantics as the production/stable adapter app. In particular, the harness is responsible for mounting the compat HTTP surface (`/api/compat/v1`) as defined in **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide** by title. This requirement applies to the set of dev/internal HTTP routes needed for QA; it does not require the dev harness to expose every production-only surface. PF02 records this responsibility at the architectural level and continues to route all concrete route shapes and error envelopes by title to their single-home documents.

  ### **3.8.2 QA entrypoints (concept-only)**

For epics whose D-goals involve Reader/HTTP behaviour, compat behaviour, or dev sampler behaviour, Live QA uses canonical entrypoints only:

* **Reader v1** (public success route) for HTTP-level compat envelopes.

* **Compat CLI surfaces** (as described in **HDE-CLI-API-Vendor-Ref**) for terminal-based compat flows that emit Reader-identical bytes.

* **Dev sampler harnesses** (CLI and HTTP) for sampler-specific behaviour, always through Engine Core and the single Presenter emitter.

All of these entrypoints:

* Call the same Engine modules (Engine Core and sampler core, where applicable).

* Emit bytes via the single Presenter emitter.

* Run under explicitly pinned rails (for example, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`) that are logged as part of QA evidence (owned by **Glow QA Guide** and **HDE-Phased Epics** by title).

PF02 does not define which entrypoint satisfies any particular D-goal; that choice and its evidence requirements are owned by **HDE-Phased Epics**, the **Glow QA Guide**, and **HDE-Governance**. Architecture only requires that any surface chosen for Live QA be canonical and emitter-backed.

### **3.8.3 Live QA surface selection**

For epics whose D-goals include live vendor behaviour or Reader/HTTP behaviour, Live QA **must** either:

* Start and use a Reader (or other HTTP) surface that reaches the Engine through the adapter and the single Presenter emitter, **or**

* Use a CLI entrypoint that exercises the same Engine and Presenter path and is documented in **HDE-CLI-API-Vendor-Ref**.

Reader and CLI surfaces are **peers** with respect to the single-emitter rule: both call the same Presenter emitter symbol. PF02 does not define which surface satisfies any particular D-goal; that choice and its evidence requirements are owned by **HDE-Phased Epics**, the **Glow QA Guide**, and **HDE-Governance**.

### **3.8.4 Discovery vs guessing**

Environment and service discovery for dev/QA is **canon-first**. Before designing high-stakes HTTP QA steps, implementers and QA must consult:

* **HDE Architecture**

* **Glow Infrastructure**

* **HDE-Mechanics Guide**

* “GitHub Codespaces in a QA Workflow” (where relevant)

to determine how to start and reach Reader and other services.

HTTP QA against “Reader” or dev harness surfaces is considered misconfigured if there is **no running adapter/Reader process** discoverable through the documented commands and ports. Attempts to hit guessed URLs or ports are a plan defect, not a property of the Engine or Presenter.

**Routing (titles-only).**

* Service start commands, ports, and environment wiring for dev/QA consoles → **Glow Infrastructure**, **HDE-Mechanics Guide**

* Live QA process, discovery baselines, and rails posture (for example, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`) → **Epic-Process-Guide**, **Glow QA Guide**

* CLI and Reader surface bytes, request/response shapes, and admin surfaces used for Live QA → **HDE-CLI-API-Vendor-Ref**

* 

### **3.8.4 Discovery vs guessing**

Environment and service discovery for dev/QA is **canon-first**. Before designing high-stakes HTTP QA steps, implementers and QA must consult:

* **HDE Architecture**

* **Glow Infrastructure**

* **HDE-Mechanics Guide**

* “GitHub Codespaces in a QA Workflow” (where relevant)

to determine how to start and reach Reader and other services.

HTTP QA against “Reader” or dev harness surfaces is considered misconfigured if there is **no running adapter/Reader process** discoverable through the documented commands and ports. Attempts to hit guessed URLs or ports are a plan defect, not a property of the Engine or Presenter.

**Routing (titles-only).**

* Service start commands, ports, and environment wiring for dev/QA consoles → **Glow Infrastructure**, **HDE-Mechanics Guide**

* Live QA process, discovery baselines, and rails posture (for example, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`) → **Epic-Process-Guide**, **Glow QA Guide**

* CLI and Reader surface bytes, request/response shapes, and admin surfaces used for Live QA → **HDE-CLI-API-Vendor-Ref**

  # **4\. Boundaries & Contracts (Conceptual) \[Required−Now\]**

  ## **4.1 Boundary guarantees (no bytes)**

## 

* **Engine → Adapter.**

  * Engine computes deterministically; no time/network/IO/randomness at compute time.

  * Inputs are pure data; outputs are normalized structures; no narratives or free text.

* **Adapter → Clients (and CLI parity).**

  * Adapter calls the Engine in-proc and never hand-crafts public JSON.

  * Adapter does not emit non-canonical JSON; all public bytes come from the single canonical emitter.

  * Adapter does not leak internals or non-public fields.

* **Presenter (canonical emitter) → All surfaces.**

  * One emitter path for CLI and HTTP surfaces; UTF-8, sorted keys, compact, exactly one LF.

  * Idempotence preimage and AB↔BA parity are preserved by construction.

  * Compat v1, Reader v1, dev sampler harnesses, and offline determinism/evidence pipelines all route through the same Engine Core and sampler core modules; no surface is allowed to fork or reimplement core math. Differences are in rails, environment, and evidence policy only (owned in other PF docs by title).

**Adapter → BodyGraph source (env-aware).**  
 **Prod:** request path **does not** call vendor; BodyGraph comes from **DB**; refresh is **out-of-band** (policy by title).  
 **Dev:** direct vendor allowed; on success, **upsert** to DB.  
 Adapter and CLI follow the **BodyGraph lifecycle** in §2.3 to decide when to read from DB vs call vendor and refresh; Engine remains stateless with respect to source and always consumes normalized BodyGraph inputs. Offline determinism and evidence pipelines respect the same boundary: they work with DB-backed or fixture BodyGraphs and never call vendor directly; rails/guards, evidence families, and indices live in their single homes (PF04/PF12/PF14/PF19/PF20 by title).

* **Internal ops signals → Ops tooling.**  
   Liveness/readiness/version are side-effect-free; no compat math, no vendor calls, no PII, no secrets.

  ## **4.2 Correlation ID propagation (concept only)**

* A correlation ID is accepted and propagated end to end across CLI, Adapter, and—when rails are open—vendor calls to enable traceability.

* It is non-PII, opaque, and bounded. It is deterministic per invocation, order-neutral for AB vs BA, and stable across two runs of the same invocation.

* It is not part of public payloads, not included in the idempotence preimage or ETag identity, and not persisted as user data.

* Logging is keys-only. The correlation ID is captured only as metadata; no other payload values, header values, or secrets are logged.

* It is a transport-only carrier. Forward it as a single pinned header or metadata field. Do not duplicate across carriers.

**Routing (titles only).**

* Carrier name, exact casing, format bounds, and generation/validation rules live in **HDE-CLI-API-Vendor-Ref**.

* Logging posture, redaction rules, metrics cardinality, and evidence live in **HDE-Governance**.

  ## **4.3 Non-goals (kept out of Architecture)**

* No HTTP header matrices, status/error schemas, caching/writers rules, CLI streams/exit codes, or vendor timeouts/retries.

* No persistence policy, rate-limit values, or SLAs. These details are owned by other documents and referenced by **title only**.

# 5\. Determinism & Identity Proofs \[Required-Now\]

## 5.1 Idempotence preimage (concept only)

**Two-step rule.** Public bytes are produced by:

1. Computing a canonical preimage (UTF-8, ASCII-sorted keys, compact separators, exactly one trailing `\n`) **without** `idempotence_hash`, then

2. Computing the hash over those bytes and re-emitting with `idempotence_hash` inserted.

**Scope.**

* Applies to **all public emissions** (CLI and HTTP) via the single canonical emitter.

* No alternate serializers are permitted.

* Evidence generators and determinism pipelines must invoke Engine Core and sampler core in ways that preserve these invariants; they use the **same computation** as runtime requests, only with pinned fixtures and closed rails.

---

## 5.2 AB↔BA parity (expectation)

**Pair symmetry.**

* For identical inputs presented as AB or BA, the resulting public bytes are **bit-for-bit identical**.

**Deterministic recompute.**

* Re-emitting the same logical representation (same inputs, same environment) yields **byte-identical** output.

---

## **5.3 Evidence posture (titles/paths only)**

**Ledger-centric evidence surfaces (titles/paths only).**  
 Architecture records ownership and posture; concrete bytes and repository paths are maintained in their single homes and are not duplicated here. Reference by **title** (no version numbers), with paths only where a single canonical location is part of the contract. For the HD Engine, the primary evidence “ledger” surfaces are:

* The **Human Evidence Index** at `docs/evidence/INDEX.json` (plus its `.sha256` sentinel), which lists governed evidence artifacts (including bundles) in a human-readable, text-based form.

* The **Machine Evidence Index** at `artifacts/evidence_index.jsonl`, a records-only, canonical JSONL mirror of the ledger, which includes per-record `proof_anchor` fields pointing to path proofs maintained alongside governed artifacts.

* **Evidence bundles and bundle manifests** (textual, typically JSON/JSONL) under governed paths (for example, `artifacts/**`, `docs/evidence/**`, `audit/**`) that group related evidence members and enumerate them by logical artifact key, hash, and size. Architecture treats bundles and manifests as governed artifacts in their own right; PF02 routes all schema/field details by title to other PF documents and stays contract-free.

These surfaces together form the **ledger-centric, deterministic, text-based evidence posture** for the Engine: any acceptance decision for an epic must ultimately be justified by entries in the Human Index and Machine Mirror (and, where used, bundle manifests) that a human operator or a ChatGPT-class agent can inspect per PR. Detailed schema and tokenisation remain single-home elsewhere.

**Where proofs live (titles/paths only).**

* **HDE-Math-Spec** — Determinism & evidence (two-run identity, AB↔BA parity, preimage/identity recipe).

* **HDE-Governance** — Transport/ops evidence posture and acceptance tokens (A7 success-route proofs; writers/errors `no-store`/no ETag; ops `/internal/version` behaviour).

* **HDE-CLI-API-Vendor-Ref** — Endpoint Catalog (JSON success) ownership; public Reader/CLI envelope (titles only) and header semantics (contract lives here).

* **HDE-Schemas & Artifacts** — Human Evidence Index (`docs/evidence/INDEX.json`) and Machine Evidence Index (`artifacts/evidence_index.jsonl`) as single homes for ledger listings and mirror schema; optional human-index hash sentinel; bundle and bundle-manifest schemas; and path-proof semantics for governed artifacts and bundles.

* **Epic-Process-Guide** — PR-first cadence (CodEx opens PR), required same-PR updates for Doc-Delta \+ indices, and CI parity/guardrails.

* **HDE-Build Notes** — Current-epic evidence requirements and token sets (append-only; later lettered addenda supersede earlier).

* **Glow QA Guide / HDE-Phased Epics / PF23 Reality-Audits** — QA tokens, D-goals, and Reality Audit posture that consume the ledger; PF02 routes by title only and does not define tokens or audit scripts.

**Discipline & hygiene (contract-free posture).**

* **Same-PR parity.** Whenever proofs or governed artifacts (including bundles and manifests) change, the Human Evidence Index and the Machine Evidence Index MUST be updated **in the same PR** that carries the code/evidence change.

* **Canonical serialization.** The Machine Evidence Index is canonical JSONL: UTF-8, ASCII-sorted keys, compact separators, exactly one trailing LF, and unknown-key rejection. Bundle manifests and other governed JSON/JSONL artifacts referenced from the ledger follow the same canonical discipline (owned by HDE-Schemas & Artifacts).

* **Bundle-level path proofs.** Path proofs live at the governed artifact level, which includes bundles. Each Machine Evidence Index record includes a `proof_anchor` that points to a bundle-level (or artifact-level) path-proof stored alongside the governed file; file name and location for these proofs are owned by HDE-Schemas & Artifacts.

* **Agent-readability.** Governed evidence for the HD Engine that Codex/ChatGPT is expected to reason about MUST remain text-based and PR-local: Human Index entries, Machine Mirror records, bundle manifests, and key QA logs are all plain-text artifacts under governed paths. Binary or compressed bundles may exist as supplemental artifacts, but they MUST NOT be the sole governed evidence for any acceptance token that expects automated review.

**A7 success-route evidence (routing note).**  
 For epics that deliver or modify Reader success routes, capture GET/HEAD/304 headers on the **cataloged JSON success route** (not `/internal/version`), including:

* Strong ETag on 200\.

* HEAD 200 parity.

* 304 with both `Content-Type` and `Content-Length` omitted.

* `Vary: Authorization, Accept-Encoding`.

* Encoding-invariance of ETag and effective `Content-Length`.

* Headers-only env-gate proof that non-prod entries are unreachable in prod.

Concrete artifact names/paths, bundle usage for A7 families, and tokenisation are maintained in **HDE-Governance**, **HDE-Schemas & Artifacts**, **HDE-Build Checklist**, and **HDE-Build Notes** (titles only). PF02 remains contract-free.

**Contract-free reminder.**

* No matrices, token rosters, schemas, bundle field lists, or byte-level details appear in PF02.

* PF02 describes **which evidence surfaces exist and how they connect to the architecture**, but always routes concrete shapes, schemas, and tokens by **document title** to their single-home PF documents.

## 5.4 Evidence & determinism flows (concept only)

**Offline plane.**

* Determinism and evidence pipelines run **offline**, in a plane parallel to runtime requests.

* They do not introduce new runtime surfaces or alter Reader/CLI behaviour; they only exercise existing Engine behaviour under controlled conditions.

**Behaviour source.**

Tools or jobs (named by title only in Mechanics/Checklists and Build Notes) call:

* `engine.core.core` for Engine Core behaviour, and

* `engine.sampler.core` for sampler/ranker behaviour,

using deterministic fixtures and **closed rails** (no network, no clocks, no env-driven branching). These calls use the **same pure-compute modules** as runtime requests; they do not re-implement logic.

**Artifact families.**

* Outputs are written into governed evidence families under `artifacts/...`, registered in **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide** (titles only).

* Family names, schema shapes, and path patterns are defined there, not in Architecture.

**Index & mirror linkage.**

Whenever these pipelines produce or regenerate artifacts:

* The human Evidence Index and the machine JSONL mirror must be updated in the **same PR**, per **HDE-Schemas & Artifacts** and **Epic-Process-Guide**.

PF02’s role is to assert that:

* All determinism/evidence flows treat Engine Core and sampler core as the **single behaviour homes**, and

* All evidence and identity proofs ultimately flow through those modules and the single Presenter emitter, even though their schemas, tokens, and job wiring are owned by other canonical documents.

PF02 does **not** define pipeline names, schedules, tokens, or acceptance criteria; it only maps **which components participate and how they connect**.

---

# 6\. Vendor & BodyGraph architecture \[Required-Now\]

## 6.1 BodyGraph ingest & refresh posture (concept only)

**BodyGraph as canonical cache.**

* The BodyGraph is the canonical cached representation of a user’s human-design state.

* Adapter reads/writes BodyGraphs in the database so later requests can reuse cached results instead of calling the vendor.

* Engine stays stateless and just consumes whatever BodyGraph the adapter hands it.

**Prod posture (no inline vendor on the hot path).**

In production:

* The request path for compat/Reader surfaces **does not** call the vendor inline.

* BodyGraphs come from the database (via the DB runtime resolver); refresh runs out-of-band.

* TTL/SWR, rate-limits, and circuit-breaker behaviour (`fail/window_s/cooldown_s`) are enforced outside PF02, by Governance, Infrastructure, and Mechanics.

**Dev posture (inline allowed, but cached).**

In dev and similar non-prod environments:

* Direct vendor calls are allowed under SAFE rails and appropriate env pins.

* On a successful vendor fetch \+ Engine compute, Adapter upserts the resulting BodyGraph and metadata into the DB so later requests can reuse it.

* This keeps Engine behaviour identical across environments: it always acts on BodyGraphs handed in by Adapter, regardless of how they were obtained.

**DB runtime resolver (env-aware, titles-only).**

Adapter uses an environment-aware resolver to decide how to connect to the BodyGraph store:

* **Non-dev:** selection by presence only, in order:  
   `DATABASE_URL → DB_BRIDGE_URL →` typed error (no connectivity probe).

* **Dev:** when `APP_ENV=dev` and `DATABASE_URL` is present but unusable, the resolver may fall back to `DB_BRIDGE_URL` and proceed with keys-only diagnostics (no secrets in logs).

Resolver semantics, connection details, and evidence live in **Glow Infrastructure**, **HDE-Governance**, and **HDE-Mechanics Guide**. PF02 only records that such a resolver exists, that the database is the canonical BodyGraph source, and that vendor calls do not bypass it in production.

**Flow ownership (by title).**

* The end-to-end BodyGraph ingest and durability flow (including schemas, fingerprints, and indices) lives in the BodyGraph ingest/durability section of this document and in **HDE-Schemas & Artifacts** and **HDE-Governance**.

* Section 6 names the posture and boundaries; detailed flows remain single-home elsewhere.

---

## **6.2 Vendor seam (concept only)**

**Shaping and calling (bounded).**  
 The vendor seam shapes requests, normalises responses, and is the **only place** in the Engine/Adapter stack where live HTTP calls to the vendor may occur. Live HTTP and database access are **never performed in Engine Core or sampler core modules**; they are confined to vendor seam modules that sit alongside Adapter and obey the same rails and Governance posture.

**Responsibilities.**

* Adapter (or a dedicated provider module at the seam) constructs URLs, headers, and bodies by policy.

* The vendor seam normalises vendor responses into BodyGraphs or other internal structures that match the schemas owned in other documents.

* Engine Core and sampler core receive only normalised data structures; they never see vendor transport details or directly open sockets or database connections.

**Repo-local seam location (names-only).**

The BodyGraph ingest/resolution seam MAY be implemented under `engine/bodygraph/`. Even though this path sits under the top-level `engine/` package, Architecture treats `engine/bodygraph/` as a **non-core I/O seam component**, not part of Engine Core or sampler core “pure compute.” The seam is allowed to orchestrate vendor HTTP and BodyGraph cache DB reads/writes (subject to rails and policy owned elsewhere), while all deterministic compute remains in the pure modules (Engine Core and sampler core) and all public bytes remain emitted by the single Presenter emitter.

**Engine purity preserved.**  
 Engine Core and sampler core remain in-proc, deterministic, and free of network/time/IO concerns and environment-based behaviour:

* No engine runtime modes or hidden toggles for dev/prod; logic is identical in all environments.

* Engine Core has no knowledge of whether inputs came from vendor or cache; it always treats them as pure data.

* Any source-selection logic (DB vs vendor, TTL enforcement, stale-while-revalidate) lives in Adapter/CLI and the vendor seam, not in Engine Core.

Even if vendor seam modules live in the same top-level package as Engine Core, Architecture treats them as a **separate component**. Moving them or refactoring their location must not change Engine Core behaviour.

**Operational hygiene.**  
 Vendor seams must honour Governance posture:

* No secrets or PII in logs (keys-only traces where allowed).

* Rails must be explicitly open before any live HTTP is attempted.

* Fail-closed behaviour on misconfiguration or closed rails (typed refusal, no network touch) is enforced at the seam; PF02 records the existence of this boundary but does not define error bytes or token semantics.  
* 

---

## 6.3 Non-goals / routing

**Not defined here.**

PF02 does **not** define:

* Timeouts, retries/backoff, rate limits, or circuit-breaker thresholds.

* Header or payload details, conditional delivery rules, error taxonomy/mapping, or auth policy.

* Vendor request or response shapes, SLAs, or persistence/retention policy.

**Route by title.**

* Transport and public envelope bytes (CLI/Reader/vendor) → **HDE-CLI-API-Vendor-Ref**

* Acceptance and ops policy (including A7 validators, caching for 200/HEAD, no-store on writers/errors, required evidence) → **HDE-Governance**

* BodyGraph table shapes, fingerprints, indices, evidence families, and mirror bindings → **HDE-Schemas & Artifacts** and related Mechanics/Checklist docs

**Contract-free stance.**

This section names **responsibilities, posture, and component boundaries only**. It does not duplicate payload or transport bytes and does not introduce new tokens; it routes by **document title** to the single homes that own contracts, schemas, and evidence.

# **7\. Security & Privacy Principles \[Required-Now\]**

## **7.1 Public surfaces: no PII; keys-only logs**

No PII in public outputs. Public envelopes expose only approved fields. They must not contain free-text narratives or user-identifying data.

Keys-only logging. Logs (including offline evidence pipelines and BodyGraph ingest flows) may record route names, step IDs, evidence family names, timings, and opaque identifiers (for example, a correlation id). Logs must never record payload contents, raw birth data, vendor payloads, derived personal attributes, or secrets.

BodyGraph ingest logs & metrics (routing only). BodyGraph ingest and refresh logs are keys-only (no raw birth data; no vendor payloads; secrets never logged). Metrics cover refresh outcomes, rate-limit throttles, circuit-breaker trips, vendor latency histograms, and staleness gauges. Governance and Schemas & Artifacts own evidence/indexing. Glow Infrastructure owns providers/secrets posture. See §2.4 **BodyGraph ingest & durability** and §5 **Determinism & identity proofs** for how these flows are wired.

## **7.2 Secrets & side effects: strict hygiene**

No secrets in logs/artifacts. API keys, tokens, credentials, and other secrets must not appear in logs, artifacts, or error messages. This applies equally to runtime surfaces and to offline evidence and determinism jobs.

No import-time I/O in engine math. Engine code performs no file, network, or time access (and no randomness) at import or compute time. Computations are pure and deterministic. Offline evidence generators invoke the same pure Engine and sampler behavior with pinned fixtures and do not introduce new side effects.

# **8\. Repository & Ownership Routing \[Required-Now\]**

## **8.1 Ownership of “bytes” (route by title)**

PF02 is contract-free. Use titles only for cross-doc references. Do not copy headers, schemas, status matrices, tokens, or paths here. Concrete bytes and locations live in their single homes below.

Math & scoring (arithmetic, banding, presets, extractors, preimage/idempotence, ordering) → **HDE-Math-Spec**.

Pack catalogs & manifest (freeze-pack identity, checksums, canonical JSON policy, human `docs/evidence/INDEX.json`, machine `artifacts/evidence_index.jsonl` schema/parity) → **HDE-Schemas & Artifacts**.

CLI / Reader / vendor route bytes (public six-key envelope, request/response shapes & examples, streams/exits, Endpoint Catalog (JSON success) ownership and route titles, CLI admin preview, vendor request shaping, parity rules) → **HDE-CLI-API-Vendor-Ref**.

A7 transport & ops policy (ETag/200, 304 header omissions, HEAD parity, Vary: Authorization, Accept-Encoding, encoding-invariance, writers no-store/no ETag, /internal/version ops-only posture, acceptance tokens) → **HDE-Governance**.

QA tokens & D-goals (Live QA token semantics, rails posture, and per-epic D-goal records and acceptance conditions) → **Glow QA Guide** and **HDE-Phased Epics**.

Guards & ops how-to / CI (capture scripts, serializer path allow-lists/denylists, dev-harness ops posture, PR-first workflow with CodEx-opened PR and same-PR Evidence Index updates) → **Epic-Process-Guide** and **HDE-Mechanics Guide**.

Infrastructure names/locations (providers, projects, services, repos, domains, DB schemas) → **Glow Infrastructure**.

Narratives surface (Aux route & Composer), suppression rule (200 with no body, no ETag), and A7 posture for Aux → **HDE Narratives Guide** (and **HDE-Governance** for policy).

Invocation tag / covenant text → **PF-Invocation**.

Endpoint Catalog (JSON success) single home & env-gate proof → **HDE-CLI-API-Vendor-Ref** (route titles) and **HDE-Schemas & Artifacts** (path `docs/ENDPOINTS_CATALOG.json` \+ `.sha256`, env-gate proof indexing). PF02 pins this location only.

BodyGraph evidence families (source-selection snapshot, source-invariance proofs, refresh-policy snapshot, ingest metrics/log samples) → **HDE-Mechanics Guide** / **HDE-Build Checklist** (what to capture, when), **HDE-Schemas & Artifacts** (indices/mirror discipline). Schema names for durability live in **Glow Infrastructure** (names-only).

