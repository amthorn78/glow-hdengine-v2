# **0\. Front Matter**

**Title:** PF02-Canon-HDE Architecture  
 **Version:** v1.0.9  
 **Status:** Canon  
**Effective date:** 2025-11-16

**Last Update Gate:** BN 7.1 Drain

---

## **Intent & scope \[Required-Now\]**

What PF02 is. The architectural map of the Glow HD Engine at the level of components, boundaries, and principles. It honors single homes:

* engine/ — deterministic math,  
* adapter/ — single HTTP home,  
* presenter/ — single canonical emitter (used by Adapter and CLI).

Supersession rule (PF10 addenda). Where PF10 includes multiple numbered addenda on the same topic, the **later number supersedes earlier guidance**. PF02 reflects the latest position and routes work to canonical homes **by title only** (no version numbers).

Contract-free. PF02 never carries headers, payload schemas, status matrices, exit codes, SLAs, or acceptance tables.

Section labels. Each section is tagged , , or to separate current behavior from near-term goals and future support.

Routing by title only. Operational/transport details, CLI/Reader bytes, vendor specifics, and process policy are referenced by **title only** to their owning documents.

Pack/bytes ownership (out of scope here). Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) are owned outside Architecture and cited by title.

**Endpoint Catalog (single home; routing note).** Success-endpoint discovery and A7 proofs are **catalog-driven**. The **single home** is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; **one LF**) with `docs/ENDPOINTS_CATALOG.json.sha256` sidecar. The Catalog is **internal-only** and **env-gated**; **non-prod entries are unreachable in prod** (capture a headers-only **env-gate proof**). A7 proofs run **only** on a **cataloged JSON success** route; `/internal/version` is **ops-only** and excluded. Titles-only details live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**; indexing discipline lives in **HDE-Schemas & Artifacts**.

**A7 invariants (routing note).** Success proofs require **`Vary: Authorization, Accept-Encoding`**, **strong quoted ETag on 200**, **HEAD 200 parity** (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), and **304** (after prior 200\) **omitting** both `Content-Type` and `Content-Length`. **Encoding-invariance** holds: for the same canonical LF-terminated body, the **ETag identity** and effective **`Content-Length`** are stable across accepted encodings. Concrete contracts remain in **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**.

---

## **Change control \[Required-Now\] (titles-only cross-refs; no duplicated bytes)**

Transport / contract bytes. Owned outside Architecture: **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**. Acceptance tokens are single-home in **HDE-Governance §2.0**; PF02 never enumerates tokens.

Canonical JSON / pack / mirror. Policies, manifest shape, and the evidence index/mirror live in **HDE-Schemas & Artifacts**.

PR-first posture. **CodEx opens the PR automatically** (one PR per epic/slice). **Doc-Delta**, the **human Evidence Index** (`docs/evidence/INDEX.json`), and the **machine JSONL mirror** (`artifacts/evidence_index.jsonl`) **must update in the same PR** whenever proofs/artifacts change.

Mirror hygiene (titles-only). The machine mirror is **records-only**, **canonical JSONL** (UTF-8, sorted keys, compact, **one trailing LF**), **rejects unknown keys**, and each record includes a **`proof_anchor`** to a path-proof stored alongside the artifact. A human-index hash sentinel may be enforced (see Schemas & Artifacts).

Math semantics. Idempotence (preimage recipe), ordering, banding, and scoring live in **HDE-Math-Spec**.

Enforcement & CI. Jobs, guards, allow-lists, and evidence procedures live in the **HDE-Mechanics Guide**.

Infrastructure. Names/locations live in **Glow Infrastructure**; operational evidence/policy remain owned by **HDE-Governance**.

Process & PR workflow. **Epic-Process-Guide** governs PR-first cadence; **Appendix D (human)** and the **machine mirror** must be updated **in the same PR**.

Freeze-pack linkage (release identity). Release identity is pack-derived; any change to frozen constants, the direct Motor→Throat set, thresholds, or catalog membership/order requires a **Schemas & Artifacts** manifest update and yields a new `release_id` (titles-only).

Endpoint proofs & ops exclusion (routing). A7 proofs run only on a **cataloged** Endpoint Catalog (JSON success) route (Vendor Ref); `/internal/version` is ops-only and not A7-eligible (titles-only to Governance §10.5).

Narratives routing (titles-only). Reader remains narrative-free. Narrative bytes are carried via Aux/CLI and live in **HDE-CLI-API-Vendor-Ref**; suppression/A7 policy for Aux lives in **HDE-Governance**. PF02 stays contract-free.

Cross-doc referencing. Use **titles only**; do **not** include version numbers.

No contract bytes here. Any change that would introduce contract bytes or duplicate content is rejected; instead, add or update a **titles-only** reference to the owning document.

**DB runtime resolver (routing note).** Resolver semantics are **environment-aware**: • **Non-dev:** selection by **presence only** in this order: `DATABASE_URL → DB_BRIDGE_URL → typed error` (**no connectivity probe**). • **Dev:** when `APP_ENV=dev` and `DATABASE_URL` is present **but unusable**, the resolver **falls back** to `DB_BRIDGE_URL` and proceeds (keys-only diagnostics; secrets/payloads never logged). Evidence (headers/records only) is owned by **Mechanics/Checklist** and indexed per **Schemas & Artifacts**. 

ent.

---

# **1\. Architectural Principles \[Required-Now\]**

CLI parity work remains open; Architecture keeps the single-emitter rule while PF05/PF14 close parity on the CLI path.

## **1.1 Single homes**

* **engine/** — deterministic math only. No time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. Inputs are pure data; outputs are pure data; side effects are forbidden.  
* **adapter/** — single HTTP home. Mounts runtime surfaces and applies guards/rails. Calls the Engine in process and never hand-crafts public JSON; only the Presenter’s emitter produces public bytes. No alternate HTTP homes and no duplicate or legacy trees.  
* **presenter/** — single canonical emitter. One code path produces public JSON for all callers (HTTP and CLI). No alternate serializers, formatters, or per-surface emitters.

**Guards (normative).**

* **Deny-list legacy trees:** `core/`, `server/`, `adapters/` (plural) and any alternate HTTP homes; CI must fail on imports from these paths.  
* **Single-emitter allow-list:** only the Presenter’s emitter entrypoint may serialize public bytes; all other serializers are forbidden on public paths.  
* **No ad-hoc serialization on public paths:** forbid direct `json.dumps(...)`, `jsonify(...)`, templating, or string-built JSON.  
* **Role boundaries:** Adapter owns route registration; Presenter owns emission; Engine owns math. No cross-role leakage.

**Routing (titles-only).**

* Enforcement guards and CI procedures live in **PF14 — HDE Mechanics Guide**.  
* Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) live in **PF12 — HDE Schemas & Artifacts**.

## **1.2 Determinism & parity**

* **Canonical JSON.** All public JSON is UTF-8 (no BOM), keys sorted in ASCII order, compact separators, and ends with **exactly one** newline (LF). Arrays used as sets are **deduplicated and ASCII-sorted**. Canonicalization rules are owned by **HDE-Schemas and Artifacts §4** (titles-only).  
* **Two-step idempotence.** Build the idempotence **preimage** (excluding `idempotence_hash`), canonicalize it, compute `sha256(preimage_bytes)`, then insert `idempotence_hash` and re-emit the final LF-terminated body. The preimage recipe and hashing posture are owned by **HDE-Math-Spec** (titles-only).  
* **Single emitter entrypoint.** CLI and Adapter **call the same Presenter emitter symbol**; Architecture forbids alternate public-byte code paths (no ad-hoc serializers on public paths).  
* **Reader↔CLI parity.** For mirrored surfaces, CLI stdout is **byte-identical** to the Reader 200 body (single emitter).  
* **AB↔BA parity.** For the same pair of inputs in either order, the public bytes are **identical** (pair normalization).  
* **Two-run identity.** Re-emitting the same logical representation produces **byte-identical** output.  
* **Locale pins (required).** All canonicalization and compares run with **`LC_ALL=C`, `LANG=C`, `TZ=UTC`**.

**Routing (titles-only).** Payload schemas, category construction, and transport/header rules live in **HDE-CLI-API-Vendor Ref** and **HDE-Governance**; canonical JSON, pack/manifest, and the machine Evidence Index live in **HDE-Schemas and Artifacts**; idempotence preimage and math live in **HDE-Math-Spec**. Architecture remains **contract-free**.

---

## **1.3 Separation of surfaces \[Required-Now\]**

**Public vs internal/dev.**  
 Public surfaces expose only the approved **Reader** envelope (bands-only, numeric-free) produced by the **Presenter**. Internal/dev surfaces exist for diagnostics and local harnesses and are **not** public data planes. The internal-ops identity route **`/internal/version`** is governed in **HDE-Governance §10.5**; PF02 stays **contract-free** and **does not restate headers** (titles-only routing).

**Endpoint Catalog (success) proofs.**  
 A7 proofs run **only** on a cataloged **Endpoint Catalog (JSON success)** route, named and owned in **HDE-CLI-API-Vendor-Ref**. PF02 does **not** enumerate routes or bytes; it routes discovery/proofs by title and keeps contract bytes out of Architecture.

**Keys-only outputs (Engine).**  
 The **Engine** never emits narratives or free text; it produces only **structured keys** that the Presenter serializes. Public bytes are produced exclusively by the Presenter’s **single emitter** (shared by Adapter and CLI).

**Aux Narrative surface (concept-only).**  
 Narrative **text** (when present) is served only via **Aux/CLI** (not on Reader 200). Endpoint bytes live in **HDE-CLI-API-Vendor-Ref**; suppression carve-out and A7 posture live in **HDE-Governance**. PF02 remains contract-free and routes by title only.

**No leakage across boundaries.**  
 Adapter does not reveal internal state or non-public fields; Engine math remains isolated from runtime concerns; no cross-role fields or headers leak into public envelopes.

**Locale & canon seams.**  
 All canonicalization and byte compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Presenter emits **canonical JSON**; canonical JSON policy and the **machine Evidence Index** (JSONL mirror schema and parity) are owned by **HDE-Schemas & Artifacts §4** (titles-only).

**Routing (titles-only).**

* Headers/transport and acceptance tokens → **HDE-Governance** (single-home roster in §2.0).

* Public Reader/CLI bytes and the Endpoint Catalog → **HDE-CLI-API-Vendor-Ref**.

* Canonical JSON, pack/manifest, and the machine mirror → **HDE-Schemas & Artifacts**.  
   Architecture remains **contract-free**.

  ---

# **2\. System Overview (Blocks & Flows) \[Required-Now\]**

## **2.1 Components & responsibilities (single homes)**

**engine/** (deterministic core). Computes compatibility and related math in process with no time, network, file I/O, or randomness. Accepts normalized inputs and returns normalized structures.

**adapter/** (single HTTP home). Hosts runtime surfaces and guards. Performs lightweight input validation, then calls the Engine synchronously. It never hand crafts public JSON. Routing (titles only): service start-command symbol, exposure posture, and infrastructure locations live in PF07-Canon-Glow-Infrastructure; operational policy and evidence ownership live in PF04-Canon-HDE-Governance.

**presenter/** (canonical emitter). Provides the one serializer and emitter used by all surfaces (CLI and HTTP). Ensures canonical formatting, idempotence preimage discipline, and AB↔BA parity at the byte level. Routing (titles only): emitter invocation/validation runs and infrastructure locations live in PF07-Canon-Glow-Infrastructure; operational policy and evidence ownership live in PF04-Canon-HDE-Governance.

**database** (persistent BodyGraph cache). An external store for BodyGraphs enabling reuse of previously computed results. The Adapter reads from and writes to this database (on BodyGraph fetches) so that subsequent requests can retrieve the cached BodyGraph instead of calling the vendor. The Engine remains stateless – it simply consumes whatever BodyGraph data the Adapter provides from this cache or a live call.

### **Repo map (normative)**

engine/ \# math only  
 adapter/ \# single HTTP home  
 presenter/ \# single emitter entrypoint for all public bytes

### **Deny-list (normative)**

The following paths MUST NOT exist or be imported on public paths: `core/`, `server/`, `adapters/` (plural), or any alternate HTTP home. CI MUST fail on imports from these paths.

### **Emitter rule (normative)**

Only the presenter’s emitter entrypoint MAY serialize public bytes. All other serializers and any ad hoc `json.dumps(...)`, `jsonify(...)`, templating, or string-built JSON on public paths are FORBIDDEN.

### **Routing (titles only)**

Concrete guard checks and scripts live in **PF-Canon — Mechanics Guide to the HD Engine (Build Guide)**, and process/PR workflow (CodEx staging, PR-first merging, repo-docs/Evidence Index updates) lives in **PF06-Canon-Epic-Process-Guide**.

---

## **2.2 High-level flow (request → compute → emit)**

1. **Collect & validate inputs.** CLI or Adapter gathers inputs and performs minimal structural checks (required fields present). Detailed payload shapes and schema ownership are routed by title (**HDE-CLI-API-Vendor Ref** / **HDE-Schemas and Artifacts**). No secrets in payload logs; fail-closed on malformed inputs.

2. **Compute in Engine (pure).** Adapter/CLI calls Engine functions in-process; Engine runs pure (no I/O, clocks, env, randomness) and returns a normalized result (pair normalization for AB↔BA neutrality). No side effects and no import-time effects.

3. **Persist BodyGraph result (if applicable).** After a successful vendor fetch and Engine computation of a BodyGraph, the Adapter **upserts** the resulting BodyGraph and its metadata into the database cache. On subsequent requests with the same inputs, the Adapter will first check this cache and use it if available (avoiding unnecessary vendor calls). This persistence step is part of the canonical flow for all environments – not optional.

4. **Emit via Presenter (single emitter).** Presenter uses the single canonical emitter shared by Adapter and CLI; no ad-hoc serializers on public paths and no test-only bypasses. Canonicalization: UTF-8 (no BOM), ASCII-sorted keys, compact separators, arrays-as-sets deduped & ASCII-sorted, exactly one trailing LF. Idempotence: build the canonical preimage excluding `idempotence_hash`, compute `sha256(preimage_bytes)`, insert `idempotence_hash`, then re-emit the LF-terminated body. Locale pins (required): run all canonicalization and byte-compares with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

5. **Return response (streams discipline).** CLI: write the public envelope to stdout (exact bytes; one LF); write typed JSON errors to stderr; success never writes to stderr. Adapter: return the same bytes to the client; error surfaces use typed JSON. Reader↔CLI parity holds (single emitter).

### **2.2.5 Alpha surfaces**

Compat v1 via Adapter, plus `showcompat` in CLI, both using the same emitter path. Ensure non-empty canonical JSON and byte identity between Reader and CLI for mirrored surfaces.

### **2.2.6 Proofs & routing (titles-only)**

**Policy.** Proofs and byte-level contracts are routed by title only to their single homes. PF02 remains contract-free.

**Success-endpoint proofs (A7).** Proofs run only on a cataloged JSON success route named in the Endpoint Catalog; the Catalog is internal-only and env-gated; capture a headers-only env-gate proof demonstrating non-prod entries are unreachable in prod. `/internal/version` is ops-only and not A7-eligible.

**A7 invariants (route-only).** Prove GET/HEAD/304 semantics with: strong quoted ETag on 200, HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), 304 only after prior 200 omitting both `Content-Type` and `Content-Length`, `Vary: Authorization, Accept-Encoding`, and encoding-invariance (ETag identity and effective `Content-Length` stable across accepted encodings). Concrete contracts remain external (titles-only).

**Aux Narrative proofs.** Follow the same Catalog success-route rule. Suppression semantics are governed in **HDE-Governance §10.4** (200 with no body and no ETag, optional policy header) and **PF05** for route titles.

**Ops exclusion.** `/internal/version` is operator-only and not A7-eligible. See **HDE-Governance §10.5** for ops headers and behavior.

**Public envelope construction & schemas.** See **HDE-CLI-API-Vendor-Ref** (six-key public envelope; Reader/CLI parity; titles-only) and **HDE-Schemas & Artifacts** (canonical JSON policy, schema/manifest ownership).

**Idempotence & math.** Preimage recipe, ordering, banding, and scoring live in **HDE-Math-Spec**.

## **2.3 What this document does not contain (route by title)**

This Architecture is contract-free. It does not define transport or policy bytes, including but not limited to:

* HTTP header matrices, caching or writers rules, conditional delivery (200/304/HEAD), error envelope schemas, or auth policy.  
* CLI command bytes, exit codes or streams, admin sidecar format, or payload field examples.  
* Vendor request or response shapes, timeouts or retries, or rate-limit behavior.

All such details are owned elsewhere and are referenced by title only from this document.

---

## **2.4 BodyGraph ingest & durability \[Required-Now\]**

Adapter source policy (env-aware). Prod: source is the database; vendor calls occur only on explicit triggers or scheduled refresh (never inline on the request path). Dev: direct vendor calls allowed; on success, upsert to DB for repeatability. SAFE rails apply. **This persistent caching is canonical – part of the standard data flow rather than a toggle.** Titles-only ownership: Governance (policy/tokens), CLI/API Vendor Ref (exposure), Mechanics/Checklist (evidence), Schemas & Artifacts (indices/mirror).

Durability objects (names-only). `body_graphs` (rows: `user_id`, `vendor`, `vendor_version`, `input_fingerprint`, `payload`, `created_at`, `refreshed_at`, `ttl_at`; uniqueness on `{user_id, vendor, vendor_version, input_fingerprint}`) and `body_graphs_current` (latest valid per `{user,vendor}`). Normalization and fingerprint rules are single-home in **Schemas & Artifacts**.

Refresh posture (out-of-band). Enforce TTL and SWR; run refreshes out-of-band with vendor rate-limits and a circuit breaker (`fail`, `window_s`, `cooldown_s`). No inline vendor calls in prod. Evidence families (records-only) live by title and are indexed per **Schemas & Artifacts**.

Source invariance (concept). For the same normalized inputs, DB-sourced and vendor-sourced bodies must render to identical canonical bytes (single Presenter/emitter). Proof routing lives in **Mechanics/Checklist**; bytes in **CLI/API Vendor Ref**.

Engine stateless contract. The Engine has no internal mode or toggle for data source or environment; it always runs with whatever input data the Adapter provides and never alters behavior based on dev/prod context. All source-selection logic resides in the Adapter/CLI layer.

## **2.5 What this document does not contain (route by title)**

This Architecture is contract-free. It does not define transport or policy bytes, including but not limited to:

* HTTP header matrices, caching or writers rules, conditional delivery (200/304/HEAD), error envelope schemas, or auth policy.  
* CLI command bytes, exit codes or streams, admin sidecar format, or payload field examples.  
* Vendor request or response shapes, timeouts or retries, or rate-limit behavior.

All such details are owned elsewhere and are referenced by **title only** from this document.

# **3\. Runtime surfaces (by responsibility, not bytes)**

This section names runtime surfaces and their responsibilities. It remains contract-free. Any payload shapes, header matrices, status codes, conditional delivery, or CLI/Reader specifics are routed by title to **HDE-CLI-API-Vendor Ref** (public envelope, request/response shapes) and **HDE-Governance** (A7 validators, evidence, transport acceptance). Titles only; no bytes restated here.

## **3.1 Compat v1 \[Implemented\]**

**Role & purpose.** `/api/compat/v1` is the adapter’s compatibility surface. It calls the Engine in-proc and returns the public compatibility envelope emitted by the single canonical Presenter emitter. It does not expose internals or narratives.

**Validation (high level).**

* **GET:** must not include a JSON body.  
* **POST:** expects a valid pair definition and viewer preferences that are well-formed, complete (all ten Magic-10 keys), and within allowed ranges; malformed or incomplete inputs are rejected. *(Detailed shapes live in HDE-CLI-API-Vendor Ref.)*

**Presenter rule.** The adapter never hand-crafts public JSON. Only the Presenter’s single emitter serializes public bytes for all callers (HTTP and CLI).

**Parity expectations.** For identical inputs, public bytes match CLI output (byte identity). Output is non-empty canonical JSON (LF-terminated). Locale pins for byte checks: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Routing (titles-only).** Request/response details, field lists, examples, and CLI↔Reader byte-parity rules: **HDE-CLI-API-Vendor Ref**. A7 validators and header behavior: **HDE-Governance**. Canonical JSON policy: **HDE-Schemas and Artifacts**. Process & PR workflow (PR-first; Evidence Index and mirror updated in the same PR): **Epic-Process-Guide**.

## **SAFE Rails & Provider Posture \[Required-Now\]**

## **6.1 Rails concept**

## 

## **3.2 Reader v1 \[Required-Now\] (public success route)**

**Intent.** A public Reader surface on the adapter that uses the same canonical emitter path as the CLI. It exposes the six-key public envelope for client apps without duplicating computation or serialization logic.

**Responsibilities (conceptual).**

* Accept normalized inputs or references and perform lightweight structural checks before calling the Engine in-proc.  
* Return the public envelope via the canonical emitter. **No narratives, no internal fields, no side effects.**  
* Maintain **CLI↔Reader byte parity** for identical inputs and environment; parity is a requirement (bytes owned elsewhere).  
* Obey **A7 success-route posture** (routing notes below).

**Non-goals.**

* No alternate serializers, payload shaping, or per-surface formatters.  
* No direct vendor/network calls.

**A7 proof surface (route-only; titles-only).**

* **Cataloged route only.** Reader success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (Vendor Ref).  
   **Append (Catalog tie-in):** The Catalog’s **single home** is `docs/ENDPOINTS_CATALOG.json` (+ `.sha256` sidecar). Proofs target a route listed there; `/internal/version` remains excluded. **Env-gate proof is mandatory** (headers-only).  
* **Catalog posture.** Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod. Capture a headers-only env-gate proof.  
* **A7 invariants to satisfy.** Require `Vary: Authorization, Accept-Encoding`; prove **encoding invariance** of identity (ETag) and effective `Content-Length` across accepted encodings; **HEAD 200** validator parity with `Content-Type == GET` and `Content-Length == len(identity 200 body)`; **304** only after prior 200, with no body and **omit** both `Content-Type` and `Content-Length`.  
* **Ops exclusion.** `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* Field definitions, examples, conditional delivery, and parity proofs: **HDE-CLI-API-Vendor-Ref**.  
* A7 acceptance policy and tokens: **HDE-Governance**.  
* Canonical JSON policy, pack/manifest, and the machine mirror discipline: **HDE-Schemas & Artifacts**.

## **3.3 Sample (dev harness) \[Implemented\] (dev-only)**

**Intent.** A local, non-public developer harness on the adapter for manual and automated checks during development. It shares the single canonical emitter with CLI and Reader so public bytes are identical for identical inputs.

**Responsibilities (conceptual).**

* Provide minimal endpoints or commands to exercise Engine paths with fixture inputs.  
* Perform lightweight structural validation before calling the Engine in-proc.  
* Emit results via the single canonical emitter. **No alternate serializers or formatting.**  
* Maintain CLI↔harness parity for identical inputs and environment (bytes owned elsewhere).

**Non-goals.**

* No public availability. No vendor/network calls. No persistence of user data. No narrative text.  
* No transport or policy bytes are defined in PF02.

**Gating & posture (dev-only; titles-only routing).**

* Harness is dev-only; never mounted in production.  
* Rails closed by default (e.g., `SAFE_MODE=1`, `ALLOW_NETWORK=0`); no vendor I/O.  
* Optional GET/HEAD/304 captures may be used for local evidence, but **authoritative A7 proofs do not run here**; they run on a **cataloged JSON success route** (Endpoint Catalog).  
* All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`; LF-terminated canonical JSON via the shared emitter.

**Routing (titles-only).**

* Dev-harness routing/guards and optional GET semantics: **HDE-CLI-API-Vendor-Ref**.  
* A7 proof surface policy and ops exception (`/internal/version`): **HDE-Governance**.  
* Canonical JSON policy, evidence index/mirror discipline (same-PR parity): **HDE-Schemas & Artifacts**.

## **3.4 Internal ops signals (speculative, future support)**

**Names & roles (concept only).**

* **/internal/healthz —** liveness. Constant-time “process is up” probe; no Engine invocation; no disk or network; no PII.  
* **/internal/readyz —** readiness. “Can serve traffic” probe; checks prerequisites such as config loaded, emitter path available, and rails posture sane without running compat math or touching vendors.  
* **/internal/version —** identity. Build and config snapshot for drift detection. Reads identity fields only and is side-effect-free. **No secrets.**

**Non-goals.** No payload or header matrices, auth policy, or acceptance tables in this section. These are ops signals, not product surfaces.

**Routing (titles-only).** All concrete transport or policy details for these signals are owned by **HDE-Governance**. See **HDE-Governance §10.5** for `/internal/version` posture and acceptance.

## **3.5 Internal-ops identity (route-only)**

**Purpose.** Adapter exposes internal-ops identity/diagnostic routes for operations and monitoring. These are not public data planes.

**Responsibility split.** Adapter wires the route and applies guards; Presenter emits canonical JSON when applicable; Engine remains pure compute. No cross-role leakage.

**Governance pointer.** Behavior, headers, and acceptance tokens are governed by **HDE-Governance**. PF02 remains contract-free and does not restate header/body rules.

**Contract posture (titles-only).** HDE-Governance governs invariants for the identity surface (e.g., **no-store**, **no ETag**, **HEAD 200** with `Content-Type` parity and `Content-Length ==` identity GET, conditionals ignored / **never 304**) and owns A7 evidence. PF02 points by title only.

**Evidence & indexing (titles-only).** Proof artifacts and success-endpoint snapshots are indexed per **HDE-Governance / HDE-Schemas and Artifacts**; the human Evidence Index and the machine JSONL mirror must remain **1:1 (updated in the same PR).**

**Non-goals.** No public contract bytes, no payload schemas, no alternate emitters, no persistence, and no vendor/network calls from this surface.

**Routing (titles-only).** **HDE-Governance** (identity invariants, acceptance, A7 evidence); **HDE-CLI-API-Vendor Ref** (Endpoint Catalog / success JSON); **HDE-Schemas and Artifacts** (canonical JSON and machine mirror).

## **3.6 Aux Narrative (concept-only, route-only) \[Speculative\]**

**Role.** Serve deterministic narrative text outside the public Reader surface. **No narratives appear on Reader 200\.**

**Responsibilities (conceptual).**

* Adapter wires the Aux route; Presenter emits text via the single canonical emitter; Engine remains pure compute (**keys only**).  
* **Text constraints:** no CR characters; LF-terminated output (schema/constraints routed by title).  
* Maintain **CLI admin preview parity** (bytes owned elsewhere; titles-only routing).

**Proof surface (route-only; titles-only).**

* **Cataloged route only.** Aux success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (Vendor Ref).  
* **Catalog posture.** The Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof.  
* **Suppression carve-out.** When suppressed, Aux returns **200 with no body and no ETag** (policy header optional).  
* **Ops exclusion.** `/internal/version` is ops-only and not A7-eligible.

**Routing (titles-only).**

* Endpoint route bytes and CLI admin preview: **HDE-CLI-API-Vendor-Ref**.  
* Suppression carve-out and A7 posture for Aux: **HDE-Governance**.  
* Composer response/schema & narratives pack catalogs: **HDE-Schemas & Artifacts**.

## **3.7 Narratives architecture (two-plane; concept-only)**

**Planes.**

* **Authoring plane (DB-backed):** intake, lints, preview, publish pointer, audit.  
* **Runtime plane (file-backed):** engine loads a sealed **pack** by `pack_sha`; **no DB reads** on the hot path.

**Identity & store (names-level).**

* **Manifest-driven identity:** `pack_sha = sha256(canonical manifest bytes)`.  
* **Authoritative path:** object storage at `/narratives/<pack_sha>/…`; the repo carries the manifest \+ evidence.  
* **Loader:** fetch → verify → atomic symlink swap → load; on any verify mismatch, **fail-closed** (keep previous pack); **keys-only** logs.  
* **Ops:** CLI-first operations; admin HTTP optional later.  
* **Reader posture:** Reader stays **narrative-free**; Aux suppression returns **200 empty, no ETag** (policy by title).

**Ownership & indexing (titles-only).** Evidence/indexing discipline lives in **Schemas & Artifacts**; mechanics in the **Mechanics Guide**; narrative posture in the **Narratives Guide**.

# **4\. Boundaries & Contracts (Conceptual) \[Required-Now\]**

## **4.1 Boundary guarantees (no bytes)**

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

**Adapter → BodyGraph source (env-aware).**  
 **Prod:** request path **does not** call vendor; BodyGraph comes from **DB**; refresh is **out-of-band** (policy by title).  
 **Dev:** direct vendor allowed; on success, **upsert** to DB.  
 Rails/guards, evidence, and indices live in their single homes (titles-only routing).

* **Internal ops signals → Ops tooling.**

Liveness/readiness/version are side-effect-free; no compat math, no vendor calls, no PII, no secrets.

## **4.2 Correlation ID propagation (concept only)**

* A correlation ID is accepted and propagated end to end across CLI, Adapter, and—when rails are open—vendor calls to enable traceability.  
* It is non-PII, opaque, and bounded. It is deterministic per invocation, order-neutral for AB vs BA, and stable across two runs of the same invocation.  
* It is not part of public payloads, not included in the idempotence preimage or ETag identity, and not persisted as user data.  
* Logging is keys-only. The correlation ID is captured only as metadata; no other payload values, header values, or secrets are logged.  
* It is a transport-only carrier. Forward it as a single pinned header or metadata field. Do not duplicate across carriers.

**Routing (titles only).**

* Carrier name, exact casing, format bounds, and generation/validation rules live in **PF05-Canon-HDE-CLI-API-Vendor-Ref**.  
* Logging posture, redaction rules, metrics cardinality, and evidence live in **PF04-Canon-HDE-Governance**.

## **4.3 Non-goals (kept out of Architecture)**

* No HTTP header matrices, status/error schemas, caching/writers rules, CLI streams/exit codes, or vendor timeouts/retries.

* No persistence policy, rate-limit values, or SLAs. These details are owned by other documents and referenced by **title only**.

  # **5\. Determinism & Identity Proofs \[Required-Now\]**

  ## **5.1 Idempotence preimage (concept only)**

* **Two-step rule.** Public bytes are produced by (1) computing a canonical preimage (UTF-8, ASCII-sorted keys, compact separators, exactly one trailing `\n`) without `idempotence_hash`, then (2) computing the hash over those bytes and re-emitting with `idempotence_hash` inserted.  
* **Scope.** Applies to all public emissions (CLI and HTTP) via the single canonical emitter. No alternate serializers are permitted.

  ## **5.2 AB↔BA parity (expectation)**

* **Pair symmetry.** For identical inputs presented as AB or BA, the resulting public bytes are bit-for-bit identical.  
* **Deterministic recompute.** Re-emitting the same logical representation (same inputs, same environment) yields byte-identical output.

  ## **5.3 Evidence posture (titles/paths only)**

**Where proofs live (titles/paths only).** Architecture records ownership and posture; **concrete bytes and repository paths are maintained in their single homes** and are not duplicated here. Reference by **title** (no version numbers), with paths only where a single canonical location is part of the contract:

* **HDE-Math-Spec** — Determinism & evidence (two-run identity; AB↔BA parity; preimage/identity recipe).  
* **HDE-Governance** — Transport/ops evidence posture and acceptance tokens (A7 success-route proofs; writers/errors `no-store`/no-ETag; ops `/internal/version` behavior).  
* **HDE-CLI-API-Vendor-Ref** — Endpoint Catalog (JSON success) ownership; public Reader/CLI envelope (titles only) and header semantics (contract lives here).  
* **HDE-Schemas & Artifacts** — **Human Evidence Index** (`docs/evidence/INDEX.json`) and **machine Evidence Index** (`artifacts/evidence_index.jsonl`) as **single homes** for artifact listings and mirror schema; optional human-index hash sentinel.  
* **Epic-Process-Guide** — PR-first cadence (CodEx opens PR), required **same-PR** updates for Doc-Delta \+ indices, and CI parity/guardrails.  
* **HDE-Build Notes** — Current-epic evidence requirements and token sets (append-only; later lettered addenda supersede earlier).

**Discipline & hygiene (contract-free posture).**

* **Same-PR parity.** Whenever proofs/artifacts change, the **human index** and the **machine JSONL mirror** **must be updated in the same PR** that carries the code/evidence change.  
* **Canonical serialization.** Evidence artifacts are **LF-terminated** and **key-ordered**; comparisons are on raw bytes. Header snapshots follow Governance CI normalization (lower-cased header names, compact separators, exactly one trailing LF).  
* **Mirror hygiene.** The machine JSONL mirror is **records-only**, **canonical JSONL** (UTF-8, sorted keys, compact, **one trailing LF**) and **rejects unknown keys**; each record includes a **`proof_anchor`** that points to a path-proof stored alongside the artifact (file name and location owned by HDE-Schemas & Artifacts).  
* **A7 success-route evidence (routing note).** For epics that deliver or modify Reader success routes, capture **GET/HEAD/304** headers on the **cataloged JSON success** route (not `/internal/version`), including: **strong ETag on 200; HEAD 200 parity; 304 with both `Content-Type` and `Content-Length` omitted; `Vary: Authorization, Accept-Encoding`; encoding-invariance of ETag and effective `Content-Length`; and a headers-only env-gate proof that non-prod entries are unreachable in prod**. Concrete artifact names/paths and tokenization are maintained in Governance, Schemas & Artifacts, and Build Notes (titles only).

**Contract-free reminder.** No matrices, token rosters, or byte-level details appear in PF02. Where needed, **route by title** (and, for indices, by canonical path) to the owning document.

# **6\. SAFE Rails & Provider Posture \[Required-Now\]**

## **6.1 Rails concept**

Vendor HTTP is allowed only when rails are open. Callers must verify rails before any attempt.  
 Default posture: rails are closed in tests/CI; no live network is attempted in those contexts.  
 Early refusal: when rails are closed, the provider path returns a typed refusal without touching network code.  
 Persistence posture. The only required DB connection is the primary `DATABASE_URL` (the canonical storage for BodyGraphs). EPIC011 introduced an optional bridge URL for dev/test (e.g. `DB_BRIDGE_URL`) and a guard flag for production use. By default, production remains on the primary DB only (no bridge). Additional DB environment variables are documented in Glow-Infrastructure.  
 Routing (titles only). Infrastructure names/locations live in PF07-Canon-Glow-Infrastructure. DB evidence, versioning, and runbook ownership live in PF04-Canon-HDE-Governance (Appendix D).  
 Refresh discipline (routing only). Refreshes run out-of-band under TTL/SWR with vendor rate-limits and a circuit breaker (fail/window\_s/cooldown\_s). PF02 names the posture; detailed schedules/guards and evidence are owned by Governance, Infrastructure, and Mechanics.

## **6.2 Vendor seam (concept only)**

Shaping, not calling. The provider interface shapes requests (URL, headers, body) and normalizes responses; live HTTP is not performed in core.

Engine purity preserved. The Engine remains in-proc, deterministic, and free of network/time/IO concerns and remains free of any environment-based behavior. **There are no engine runtime modes or hidden toggles** – the Engine’s logic is identical in all environments, with the Adapter responsible for any data source selection.

Operational hygiene. No secrets or PII in logs; keys-only trace where applicable.

## **6.3 Non-goals / routing**

* Not defined here. Timeouts, retries/backoff, rate limits, header or payload details, conditional delivery, error taxonomy/mapping, vendor request shaping, or auth policy are not specified in this document.

* Route by title.  
  * Transport and public envelope bytes (CLI/Reader/vendor) live in PF-Canon-HDE-CLI-API-Vendor-Ref.  
  * Acceptance and ops policy, including A7 validators, caching for 200/HEAD, no-store on writers/errors, and required evidence, live in PF-Canon-HDE-Governance.  
* Contract-free stance. This document names responsibilities only and does not duplicate payload or transport bytes.


  

# **7\. Security & Privacy Principles \[Required-Now\]**

## **7.1 Public surfaces: no PII; keys-only logs**

* **No PII in public outputs.** Public envelopes expose only approved fields; no free-text narratives or user-identifying data.

* **Keys-only logging.** Logs may record route names, timings, and opaque identifiers (e.g., correlation id), but **never** payload contents or derived personal attributes.  
* **BodyGraph ingest logs & metrics (routing only).** Logs are **keys‑only** (no raw birth data; no vendor payloads; secrets never logged). Metrics cover refresh outcomes, rate‑limit throttles, circuit‑breaker trips, vendor latency histograms, and staleness gauges. Governance/Schemas own evidence/indexing; Infrastructure owns providers/secrets posture.

## **7.2 Secrets & side effects: strict hygiene**

* **No secrets in logs/artifacts.** API keys, tokens, and credentials must not appear in logs, artifacts, or error messages.

* **No import-time I/O in engine math.** Engine code performs **no** file/network/time access (and no randomness) at import or compute time; computations are pure and deterministic.

# **9\. Repository & Ownership Routing \[Required-Now\]**

## **9.1 Human map (repo)**

* **Location (titles-only).** The human architecture map lives at the repository root (titles-only pointer; **no filename pinned here**).  
* **Purpose.** It provides the tree overview and narrative orientation (**no contract bytes**). This document (**HDE Architecture**) holds the canonical architectural principles.  
* **Routing rule.** References to owners are **by title only** (no version numbers). **Artifact titles/paths live in HDE-Schemas and Artifacts (Appendix D) and the machine mirror; PF02 does not pin paths.** Guard scripts, checklists, and runbooks are owned in the **Field Guide** and **HDE-Mechanics Guide** (titles only).  
  ---

## **9.2 Ownership of “bytes” (route by title)**

**PF02 is contract-free.** Use **titles only** for cross-doc references; do **not** copy headers, schemas, status matrices, tokens, or paths here. Concrete bytes and locations live in their single homes below.

* **Math & scoring** (arithmetic, banding, presets, extractors, preimage/idempotence, ordering) → **HDE-Math-Spec**.  
* **Pack catalogs & manifest** (freeze-pack identity, checksums, canonical JSON policy, human `docs/evidence/INDEX.json`, machine `artifacts/evidence_index.jsonl` schema/parity) → **HDE-Schemas & Artifacts**.  
* **CLI / Reader / vendor route bytes** (public six-key envelope, request/response shapes & examples, streams/exits, **Endpoint Catalog (JSON success) ownership and route titles**, CLI admin preview, vendor request shaping, parity rules) → **HDE-CLI-API-Vendor-Ref**.  
* **A7 transport & ops policy** (ETag/200, **304 header omissions**, **HEAD parity**, **`Vary: Authorization, Accept-Encoding`**, **encoding-invariance**, writers `no-store`/no ETag, **`/internal/version` ops-only** posture, acceptance tokens) → **HDE-Governance**.  
* **Guards & ops how-to / CI** (capture scripts, serializer path allow-lists/denylists, dev-harness ops posture, PR-first workflow with **CodEx-opened PR** and **same-PR Evidence Index updates**) → **Epic-Process-Guide** and **HDE-Mechanics Guide**.  
* **Infrastructure names/locations** (providers, projects, services, repos, domains, DB schemas) → **HDE-Glow-Infrastructure**.  
* **Narratives surface** (Aux route & Composer), **suppression rule** (200 with no body, no ETag), and A7 posture for Aux → **PF17-Canon-HDE-Narratives Guide** (and **HDE-Governance** for policy).  
* **Invocation tag / covenant text** → **PF-Invocation**.  
* **Endpoint Catalog (JSON success) single home & env‑gate proof** → **HDE‑CLI‑API‑Vendor‑Ref** (route titles) and **HDE‑Schemas & Artifacts** (path `docs/ENDPOINTS_CATALOG.json` \+ `.sha256`, env‑gate proof indexing). PF02 pins this location only.  
* **BodyGraph evidence families** (source‑selection snapshot, source‑invariance proofs, refresh‑policy snapshot, ingest metrics/log samples) → **HDE‑Mechanics Guide / HDE‑Build Checklist** (what to capture, when), **HDE‑Schemas & Artifacts** (indices/mirror discipline). **Schema names** for durability live in **Glow Infrastructure** (names‑only).

