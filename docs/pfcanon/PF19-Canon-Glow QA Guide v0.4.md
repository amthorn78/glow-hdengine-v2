

# **0\. Front Matter**

## **0.1 Header**

* **Title:** PF19 — Review: Glow QA Guide  
* **Status:** Canon  
* **Version:** 0.4  
* **Effective date:** 2025-11-17  
* **Last Update Gate:** BN 7.1 Drain

---

## 0.2 Purpose & scope

**Purpose.** Standardize pre-commit and post-commit QA across HDE, Catalog/A7, Aux, App FE/BE, DB/Vendor ingest, and CLI/API. This guide defines what to check and where to route policy; concrete bytes, schemas, and tokens remain in their existing single homes.

**Scope rule.** Any document with “HDE” in its title is HD Engine–specific. PF19 points to those documents by title only and does not duplicate their contents. PF19 itself covers all projects (Engine \+ App \+ shared tooling). HD Engine specifics are delegated, titles-only, to:

* PF01 — HDE-Math-Spec

* PF02 — HDE Architecture

* PF04 — HDE-Governance

* PF05 — HDE-CLI-API-Vendor-Ref

* PF09 — HDE-Build Checklist

* PF12 — HDE-Schemas & Artifacts

* PF14 — HDE-Mechanics Guide

* PF16 — HD Engine Epics Map

* PF17 — HDE Narratives Guide

PF19 owns QA principles, checklists, and cross-component playbooks; it routes all transport, math, schema, and token details to those single homes.

## **0.3 Acceptance tokens (names-only; initial)**

The following governance tokens apply to PF19 itself; definitions and semantics live in **HDE-Governance** and **HDE-Build Checklist**:

* `QA_GUIDE_INIT_OK`

* `QA_PRECOMMIT_CHECKLIST_OK`

* `QA_POSTCOMMIT_CHECKLIST_OK`

* `QA_EVIDENCE_HARNESS_OK`

  ---

  ## **0.4 Principles & Single Homes (routing only)**

  ### **0.4.1 Intent**

Pin what PF19 owns (**process, checklists, playbooks**) versus where **bytes** and **policy** live.

PF19:

* stays **titles-only** for all external references, and

* never restates transport bytes, schemas, or token tables.

  ### **0.4.2 Single homes (titles-only)**

PF19 routes to these existing single homes:

* **Transport bytes & public routes:** PF05 — HDE-CLI-API-Vendor-Ref

* **Schemas & artifacts** (catalogs, mirror, proof JSON): PF12 — HDE-Schemas & Artifacts

* **Governance** (A7 policy, refusal/writers, tokens): PF04 — HDE-Governance

* **Architecture** (single emitter, boundaries): PF02 — HDE Architecture

* **Build checklists & CI gates:** PF09 — HDE-Build Checklist

* **Narrative rules & surfaces:** PF17 — HDE Narratives Guide

* **Process (PR-first):** PF06 — Epic-Process-Guide

  ### **0.4.3 Core principles (names-only)**

PF19 assumes and reinforces these core QA principles:

* **Titles-only cross-refs.** No duplicated bytes or schemas; always route to the owning PF by title.

* **Determinism & env pins (all environments).**  
   All canonicalization, hashing, header snapshotting, and governed evidence capture **MUST** run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. These pins apply in **dev, stage, prod, and CI** whenever governed bytes are produced. (Definitions/tokens live in HDE-Governance / HDE-Build Checklist.)

* **Same-PR parity for evidence.**  
   The Human Evidence Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) are updated **together in the same PR** whenever evidence changes. (Schema/CI rules live in HDE-Schemas & Artifacts / HDE-Build Checklist.)

* **CI default CLOSED (rails).**  
   CI pipelines run with rails closed by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`). Any job that opens rails **must** pin policy and attach governed evidence **in the same PR**.

* **A7 is Catalog-only.** A7 proofs run only on a **cataloged JSON success route** (Catalog/A7 surface); **Aux HEAD/304 are out of scope under EPIC-010**.

**Industry anchors (reference‑only).** PF19’s QA rules and proofs align with: **IETF RFC 9110/9111** for HTTP semantics and caching (ETag strength/quoting, HEAD parity, 304 header/body rules); **RFC 8785 (JCS)** for JSON canonicalization (PF12 governs canonical JSON; PF19 cites JCS as an external anchor); **OWASP ASVS** for App FE/BE security verification; **NIST SSDF** and **SLSA** for supply‑chain QA and provenance expectations. PF19 remains titles‑only; bytes/schemas/tokens stay in PF05/PF12/PF04/PF09.

## 1\. Environments & surfaces map (names-only)

### **1.1 Intent**

Name the QA-relevant **surfaces** and where their **ownership** lives, with a clear split between:

* **App layer** (FE/BE)

* **HD Engine layer** (HDE service and its callers)

* **Shared tools and evidence system**

HDE-titled PF docs apply **only** to **HD Engine** surfaces. They do **not** define contracts for pure App FE or non-HDE App BE endpoints. PF19 stays names-only here: no header matrices, no byte listings, no schemas.

---

### **1.2 App layer (FE and non-HDE backend)**

These components use their **own** product and API docs. HDE PF docs are only relevant where the App talks **to** the Engine.

* **App FE (public web/app).**  
   Public-facing web and app experience. QA focuses on routing, feature flags, user flows, and integration with backend APIs.

  * Implementation and deploy: frontend repo and deploy target (names-only).

  * Contracts and behavior: app-level product and API docs (titles-only, non-HDE).

  * HDE docs: **not authoritative** for FE; only relevant at the points where FE calls backend endpoints that themselves proxy HDE.

* **App BE (service APIs beyond HDE).**  
   Application backend services that are **not** the HD Engine. QA focuses on API contracts, auth, data validation, and error posture.

  * Implementation and deploy: backend repo and service surface (names-only).

  * Contracts and behavior: backend API specs and app-specific docs (titles-only, non-HDE).

  * HDE docs: apply **only** to those BE endpoints that directly call or proxy HD Engine routes; all other BE endpoints are governed by app-specific docs, not HDE PF docs.

---

### **1.3 HD Engine layer (HDE-only)**

HDE PF docs apply **only** to the Engine’s surfaces and their direct callers: **Catalog/Reader JSON success** (A7 surface), **Aux narrative text** (non‑A7), and **CLI admin preview** using the **same emitter**. PF19 routes bytes to **PF05**, artifacts/mirror to **PF12**, governance to **PF04**, mechanics to **PF14**, narratives to **PF17**, and epics to **PF16** (titles‑only). App FE/BE are **out of scope** for HDE policy except where App endpoints **proxy HDE**; in those cases they must preserve HDE contracts.

* **HD Engine service (Reader, Aux via BE).**  
   Core Engine HTTP surfaces, exposed to the App BE as internal services (Reader JSON, Aux narrative text).

  * Implementation and deploy: `glow-hdengine-v2` service (names-only).

  * Transport bytes and public routes: **PF05 — HDE-CLI-API-Vendor-Ref**.

  * Architecture and boundaries: **PF02 — HDE Architecture**.

  * Governance and A7 policy: **PF04 — HDE-Governance**.

  * All other Engine details: HDE-titled PF docs (PF01, PF12, PF14, PF16, PF17) by title only.

* **HD Engine integration in App BE.**  
   Backend endpoints that call HDE are responsible for preserving HDE contracts at the integration boundary.

  * HDE contracts: defined only in HDE-titled PF docs (titles-only, no duplication).

  * App BE wrapping behavior: defined in backend API docs; PF19 treats it as part of App BE QA with additional checks that HDE contracts are honored.

---

### **1.4 Shared tools and evidence system**

These pieces are cross-cutting. Some are HDE-specific in terms of contract, but they affect how QA is done across projects.

* **CLI/API and SDKs (dev tools).**  
   Developer-facing tools that exercise the Engine and App. QA focuses on parity with emitters and deterministic behavior.

  * Implementation: CLI and SDK repos (names-only).

  * Transport and CLI contracts for HDE flows: **PF05 — HDE-CLI-API-Vendor-Ref**.

  * For App-only tools, contracts live in app-specific docs; HDE PF docs only apply when the tool calls HDE.

* **DB/Vendor ingest (authoring plane, sealed packs).**  
   Pipelines that turn vendor/bodygraph inputs and authored narratives into sealed, versioned packs used by the Engine.

  * Implementation: ingest and authoring jobs plus DB layer (names-only).

  * Schemas and artifacts (packs, manifests, proof JSON): **PF12 — HDE-Schemas & Artifacts**.

  * Vendor HTTP posture and ingest calls: **PF05 — HDE-CLI-API-Vendor-Ref**.

* **Evidence system (indices, mirror, proofs).**  
   Cross-project system that records what was proven, where, and when. Used by both Engine and App QA, but contracts are defined in HDE PF docs.

  * Human Evidence Index and hash sentinel: **PF09 — HDE-Build Checklist** (process) and **PF12 — HDE-Schemas & Artifacts** (schema).

  * Machine mirror, path-proofs, composite proof JSON: **PF12 — HDE-Schemas & Artifacts**.

*(Names-only section. No header tables, no byte or schema listings.)*

## **2\. Pre-commit QA (local/CI)**

### **2.1 Intent**

Catch issues **before** PRs merge by enforcing a consistent local/CI QA baseline across all projects.

Pre-commit QA focuses on:

* code quality and formatting

* deterministic behavior (no hidden I/O or randomness)

* snapshot and evidence hygiene

* early detection of schema/contract drift

Concrete CI wiring and gates are instantiated in **PF09 — HDE-Build Checklist** (titles-only); PF19 defines the shared “what,” not the CI job syntax.

---

### **2.2 Checklist (to be instantiated in PF09 CI)**

Pre-commit pipelines **SHOULD** include at least:

* **Lint and format.**  
   Run language-appropriate linters/formatters and fail on style or syntax issues.

* **JSON/JSONL canonicalization and final-LF checks.**

  * Enforce canonical form for governed JSON/JSONL files.

  * Require exactly one trailing linefeed on governed text artifacts.

  * Reject non-canonical or mixed-style JSON in governed paths.

* **Deterministic, no-I/O unit tests.**

  * Pure paths MUST NOT depend on RNG, wall-clock time, external network, or filesystem state.

  * Tests SHOULD prove two-run identity where applicable (same inputs → same outputs/bytes).

* **Env pins for snapshot generation.**

  * For any job that produces snapshots or evidence, **export**:

    * `LC_ALL=C`

    * `LANG=C`

    * `TZ=UTC`

  * This applies to Engine, App, and shared tools whenever they emit governed artifacts.

    

* **Rails posture in CI (default CLOSED).**

  * Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default.

  * If any pre-commit job opens rails (network I/O), it **must** produce governed evidence and index it in the same PR (titles-only routing to PF12/PF09).

* **Machine mirror quick-check (includes path-proofs).**

  * Verify `artifacts/evidence_index.jsonl` exists and is the **only** mirror file; records are canonical JSONL (sorted keys, one LF, unknown-key reject, pinned field order).

  * Verify each record’s `proof_anchor` points to an **adjacent stored path-proof**; fail CI if any proof is missing.

  * Enforce **“governed paths only”**: all indexed artifacts must live under `artifacts/**` or `docs/**`.

* **Snapshot hygiene (tolerant vs strict).**

  * Classify snapshots as **strict** (must match exactly) or **tolerant** (pattern-based).

  * Pin patterns where applicable (e.g., text posture harnesses; see §6.2 harness).

  * Fail if strict snapshots drift unexpectedly.

* **Keys-only logs in tests (where applicable).**

  * When tests exercise logging, ensure logs are **keys-only** and contain no payload bodies or secrets.

  * Logging policy and redaction rules live in **HDE-Governance**; PF19 only requires that tests respect them.

* **Fail on drift.**

  * Treat each of the following as a CI failure for governed artifacts:

    * Unknown keys in the machine mirror.

    * Non-canonical snapshots under governed paths.

    * Missing trailing LF on governed text.

  * Schema and gate definitions live in **HDE-Schemas & Artifacts** and **HDE-Build Checklist**; PF19 requires CI to enforce them.  
  * **Keys-only logs in tests.** Never log payload bodies or header values; follow Governance redaction rules.

* **Engine serializer/composer determinism.** Prove two‑run identity and AB↔BA parity (where defined). Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules. (Tokens live in PF04/PF09; bytes in PF14/PF12.)

* **Secrets & SCA/SAST/DAST.** Run secrets scanning and composition analysis; add SAST/DAST appropriate to the repo. Keep test logs **keys‑only** (no payloads/secrets). Governance in PF04; CI wiring in PF09.

* **Reproducibility & flake control.** Fix seeds; avoid wall‑clock; pin locale/timezone; quarantine flakes with **`QA_FLAKY_TEST_QUARANTINE_OK`** until deflaked (token home PF09).  
* **Test data & PII.** Use synthetic fixtures; redact payloads; enforce keys‑only logs in tests (policy PF04).

  ## **3\. Post-commit QA (staging/prod)**

  ### **3.1 Intent**

Prove **route posture**, **capture evidence**, and **update indices in the same PR** once changes are deployed to a staging or production-like environment.

Post-commit QA focuses on:

* confirming each surface behaves as promised (status, headers, body)

* capturing stable evidence (snapshots and proof JSON)

* updating both the **human index** and the **machine mirror** in the **same PR** that carries the evidence

Concrete schemas, tokens, and CI wiring live in PF04, PF09, and PF12 (titles-only); PF19 defines the shared checklist.

---

### **3.2 Checklist**

Post-commit QA SHOULD include at least:

* **Route probes.**

  * Confirm the **public path and version** are correct and stable.

  * Avoid alias drift: probes should target the **canonical route**, not ad-hoc aliases.

  * For any legacy alias that must exist, prove it resolves consistently without changing contract.

* **Header posture.**

  * Verify **Text** vs **Suppressed** rules for each surface (e.g., Aux text vs Aux suppression, Reader JSON vs error surfaces).

  * Confirm required headers (such as `Content-Type`, `Cache-Control`, `Vary`) match the owning PF doc and surface type.

  * Ensure suppressed responses obey the no-body / no-ETag rules where applicable.

  * **Header snapshot normalization.** Persist **lower-case header names** in governed snapshots; values remain verbatim.

* **ETag strength & quoting.**

  * Where ETags are required, prove they are **strong, quoted ETags** computed from the LF-terminated identity body and **stable across repeated GETs**.

* **HEAD/304 posture (A7 surfaces only).**

  * On Catalog JSON success routes, prove **HEAD 200** mirrors the identity response (`Content-Type` parity, effective `Content-Length`, no body).

  * Prove **304** occurs only after a prior 200 and **omits both `Content-Type` and `Content-Length`** (no body).

* **Evidence capture.**

  * Capture **headers/body snapshots** for each relevant route in staging/prod-like envs.

  * When A7 is in scope, capture the **composite proof JSON** (covering GET/HEAD/304 posture).

  * Update the **human Evidence Index** and the **machine mirror** in the **same PR** that adds or refreshes these captures.

* **Mirror gates.**

  * **Single file:** `artifacts/evidence_index.jsonl` only.

  * **Canonical JSONL:** UTF-8, compact, one LF per record; **unknown-key reject**; pinned ASCII field order.

  * **Path-proofs:** each record includes a `proof_anchor` that resolves to a stored, adjacent path-proof; CI fails if any proof is missing or mismatched.

  * **Governed paths only:** all indexed artifacts must reside under `artifacts/**` or `docs/**`; transient/generator paths are forbidden as evidence sources.

* **Env-gate proof (A7 scope).**

  * For A7-covered routes, capture a **headers-only env-gate proof** showing that:

    * non-prod entries are **unreachable in prod**, and

    * each cataloged success route is correctly gated to its intended environment.

  * Store the env-gate proof under governed paths and register it in both indices in the same PR.

* **Same-PR parity (merge-blocking).**

  * `docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl` **must** be updated in the **same PR** as the captured evidence.

---

## **4\. Evidence & indexing (how to prove; titles-only for schemas)**

### **4.1 Intent**

Normalize **how** we capture and register evidence across projects, while keeping all **schemas and field definitions** in their existing single homes.

PF19 defines:

* what must be captured

* where it must live

* how it must be kept in sync

All schema details and field shapes remain in **PF12 — HDE-Schemas & Artifacts** and **PF09 — HDE-Build Checklist** (titles-only).

---

### **4.2 What to capture**

Every QA run that produces governed evidence **SHOULD** capture at least:

* **Human Evidence Index.**

  * File: `docs/evidence/INDEX.json`

  * plus its **hash sentinel**: `docs/evidence/INDEX.sha256`

  * Indexed by human-readable keys and titles; used as the primary evidence catalog.

* **Machine mirror.**

  * File: `artifacts/evidence_index.jsonl`

  * **Single file** for the entire repo.

  * **Canonical JSONL**: UTF-8, compact, one LF per record.

  * **Unknown-key reject**: any record with unexpected fields MUST fail CI.

  * **Field order pinned** to the schema defined in PF12.

* **Path proofs.**

  * Per-artifact **path proof** files that show the concrete location and shape of an artifact.

  * Each machine-mirror record includes a **proof\_anchor** linking that record to its path-proof file.

---

### **4.3 Rules**

Evidence and indexing are governed by these rules:

**Canonical JSON note (titles-only).** PF12 governs canonical JSON/JSONL (sorted keys, compact, exactly one LF). PF19’s stance is compatible with RFC 8785 (JCS) for hashable/signable artifacts; PF12 remains the source of truth.  
 When computing hashes/signatures over JSON proofs, re-serialize with JCS (RFC 8785\) semantics to ensure byte-stable digests.

**Same-PR updates (merge-blocking).**

* `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` MUST be updated in the same PR as the evidence they describe.

* A PR that changes governed artifacts without updating both the human index and the mirror MUST NOT merge.

**Path-proofs required.**  
 Each machine-mirror record’s `proof_anchor` must point to a stored path-proof adjacent to the artifact (stat transcript). CI fails if missing.

**Header snapshot patterns for text posture.**

* For text surfaces (e.g., Aux Text vs Aux Suppressed), maintain pinned header snapshot patterns that distinguish:

  * strict posture (exact match required), and

  * tolerant posture (pattern-based, e.g., for dates or trace IDs).

* These patterns are designed to be adopted into PF09 CI harnesses so that snapshot drift becomes a CI failure instead of a manual surprise.

**Env pins for all captures.**

All snapshot and evidence-capture commands MUST run with:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

This applies to both Engine and App captures, ensuring that bytes and headers are stable across environments and CI runs.

---

## 5\. Component playbooks (how to run QA per surface)

Each playbook follows the same pattern:  
 **Intent · Inputs · Steps · Evidence · Tokens (names-only) · Failures to watch · Where it lives (titles-only)**

PF19 describes how to run QA; all bytes, schemas, and detailed policy live in their single-home PF docs (titles-only).

---

### **5.1 HD Engine — Catalog/A7 (HDE-specific)**

HDE-specific; bytes and policy live in **PF05 — HDE-CLI-API-Vendor-Ref**, **PF04 — HDE-Governance**, and **PF12 — HDE-Schemas & Artifacts** (titles-only).

**Intent**  
 Prove the A7 transport posture of the Catalog JSON success route for the HD Engine and capture machine-checkable evidence.

**Scope: Catalog JSON success route only (the Catalog/A7 surface).**

* `/internal/version` and any other ops or Aux endpoints are explicitly excluded from A7.

**Inputs**

* A staging or prod-like environment where the Catalog JSON success route is reachable.

* Env pins applied for all captures:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* The current Endpoint Catalog entry (by title only) that identifies the route and its env-gate.

**Steps**

**Probe the Catalog JSON success route.**

* Send a GET request to the cataloged JSON success route.

* Confirm:

  * 200 status,

  * JSON body, and

  * headers consistent with PF05/PF04 (titles-only).

**Capture GET headers and body.**

* Record the full header block and body bytes for the 200 response.

* Ensure the body is LF-terminated and matches the canonical JSON rules.

**Capture HEAD posture.**

* Send HEAD to the same route.

* Confirm:

  * 200 status,

  * headers mirror the GET response where required (Content-Type, validators),

  * `Content-Length` equals the identity 200 body length.

**Capture 304 behavior.**

* Replay GET with `If-None-Match`/`If-Modified-Since` as appropriate to elicit a 304\.

* Confirm 304:

  * has no body,

  * omits both `Content-Type` and `Content-Length`,

  * preserves validators and `Vary` as required.

* Omit both `Content-Type` and `Content-Length`; include validators only.

**Verify strong, quoted ETag.**

* Confirm `ETag` is:

  * present on 200,

  * derived from the LF-terminated body, and

  * in the form `"xxxxxxxx..."` (quoted strong ETag).

* Confirm `ETag` remains stable across repeated GETs with unchanged content.

**Verify Vary and encoding-invariance.**

* Confirm `Vary: Authorization, Accept-Encoding` (or equivalent) is present.

* Exercise accepted encodings (e.g., identity vs gzip) and prove:

  * `ETag` does not change with encoding, and

  * effective `Content-Length` (after decoding) remains consistent.

* If present, `Content-Length` on HEAD MUST equal the identity GET body length; otherwise omit it.

**Capture env-gate proof.**

* Produce a headers-only log showing that:

  * only the expected cataloged routes are reachable in this environment, and

  * non-prod entries in the Catalog are not reachable in prod.

**Build composite A7 proof JSON.**

* Generate a single composite JSON proof object (or records-only JSONL) with:

  * `route_path`, `env_gate`,

  * GET/HEAD/304 header captures,

  * ETag and Vary fields,

  * `encoding_invariance_ok` flag.

* Validate this proof against the schema in PF12 (titles-only).

**Evidence**

Headers and body snapshots for:

* GET 200,

* HEAD 200,

* 304 (no body).

A composite A7 proof JSON (or JSONL) capturing all required fields.

An env-gate proof artifact showing non-prod entries unreachable in prod.

Updated entries in:

* `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

* `artifacts/evidence_index.jsonl`

in the same PR that introduces or refreshes these artifacts.

**Tokens (names-only)**  
 The following tokens are typically used to gate A7 completion (definitions live in PF04/PF09):

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

**Failures to watch**

* Catalog route not reachable or returns incorrect status (non-200) for GET.

* Missing or unquoted `ETag`, or `ETag` that changes with encoding.

* HEAD response that diverges from GET posture (wrong `Content-Type` or `Content-Length`).

* 304 response that incorrectly includes `Content-Type` or `Content-Length`, or carries a body.

* Missing or incorrect `Vary: Authorization, Accept-Encoding`.

* Composite proof JSON missing required fields or failing PF12 schema validation.

* Evidence captured but not indexed in both human and machine indices in the same PR.

**Where it lives (titles-only)**

* Transport bytes and route contract: **PF05 — HDE-CLI-API-Vendor-Ref**

* A7 policy and governance details: **PF04 — HDE-Governance**

* Proof JSON schema, mirror schema, and evidence plumbing: **PF12 — HDE-Schemas & Artifacts**

  ### **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**

Cross-component; Aux bytes and emitter behavior live in **HDE-CLI-API-Vendor-Ref** and **HDE Narratives Guide** (titles-only). A7 remains **Catalog-only**; Aux HEAD/304 are out of scope.

#### **Intent**

Prove that **Aux narrative text** and **Aux suppression** behave correctly at the shared emitter level, and that **CLI preview** reflects the same bytes.

This playbook is about:

* a minimal but **strict** header posture for Aux, and

* ensuring the CLI uses the **same emitter** and cannot silently “suppress” narratives due to missing tuples or mis-wired composition.

  #### **Inputs**

* A staging or prod-like environment where Aux can be invoked via BE/CLI.

* Env pins for all captures:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* A **validated-tuple QA harness** (CLI or script) that:

  * calls the shared Aux emitter for a known test pair, and

  * can emit headers snapshots for text and suppression cases.

  #### **Scope**

For **EPIC-010**, post-commit Aux QA covers **two snapshots only**:

* `tests/transport/headers/aux_text_200.snap`

  * 200, LF-terminated text body, **quoted strong ETag** over that body.

* `tests/transport/headers/aux_suppression_200.snap`

  * 200, **empty body**, **no ETag**.

Aux **HEAD/304** are not part of A7; A7 remains Catalog-only.

#### **Steps**

1. **Run the validated-tuple QA harness for Aux Text.**

   * Invoke the harness to produce an Aux **text** response for a known test tuple.

   * Confirm:

     * 200 status,

     * `Content-Type` and `Cache-Control` per policy (titles-only),

     * LF-terminated text body present,

     * **strong, quoted ETag** derived from the LF body.

   * Save the full header block (and, if applicable, a checksum of the body) as  
      `tests/transport/headers/aux_text_200.snap`.

2. **Run the validated-tuple QA harness for Aux Suppression.**

   * Invoke the harness for a case that must suppress text (per PF17 rules).

   * Confirm:

     * 200 status,

     * **empty body**,

     * **no ETag** present,

     * headers otherwise consistent with suppression semantics.

   * Save the full header block as  
      `tests/transport/headers/aux_suppression_200.snap`.

3. **Verify CLI preview parity.**

   * Use the CLI to preview narratives for the same test cases.

   * Confirm that:

     * the CLI uses the **same emitter** as Aux (byte-identical text where applicable), and

     * CLI does not show narratives when suppression rules say it should be empty.

4. **Check composition determinism.**

   * For the Aux text case, run the harness **twice** and confirm:

     * same composition IDs and keys in the response metadata,

     * same text and header posture,

     * stable ETag.

   * This step guards against non-deterministic composition or missing tuples.

5. **Update evidence indices.**

   * Add/update entries for the Aux snapshots (and any CLI parity artifacts, if captured) in:

     * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

     * `artifacts/evidence_index.jsonl`.

   * Ensure these index updates occur in the **same PR** as the new or updated snapshots.

   #### **Evidence**

* `tests/transport/headers/aux_text_200.snap`

* `tests/transport/headers/aux_suppression_200.snap`

* Optional CLI parity artifacts (e.g., `artifacts/cli/aux_preview.json`) if defined in PF09/PF12.

* Updated records in:

  * `docs/evidence/INDEX.json` (+ hash sentinel), and

  * `artifacts/evidence_index.jsonl`  
     in the **same PR** as the snapshots.

  #### **Tokens (names-only)**

Typical tokens used to gate Aux/CLI preview QA (definitions live in PF04/PF09):

* `NARR_200_TEXT_OK`

* `NARR_SUPPRESSED_NO_ETAG_OK`

* `COMPOSE_IDS_DETERMINISM_OK`

* `ENV_LC_ALL_C_OK`

  #### **Failures to watch**

* `aux_text_200.snap` missing or showing:

  * no ETag,

  * non-quoted ETag, or

  * body not LF-terminated.

* `aux_suppression_200.snap` missing or showing:

  * non-empty body, or

  * an ETag on a suppressed response.

* CLI preview diverging from Aux emitter (different text or unexpected suppression).

* Non-deterministic composition IDs or ETag across repeated runs.

* Evidence snapshots added without corresponding updates to the human index and machine mirror in the same PR.

  ### **5.3 App Backend (non-HDE endpoints)**

App-specific; these endpoints are **not** governed by HDE PF docs unless they proxy or surface HD Engine responses. Transport contracts for pure App APIs live in App backend API docs. HDE docs may be used as patterns, not as authority, except where the App BE directly wraps HDE surfaces.

#### **Intent**

Prove that **App Backend public APIs** (beyond HDE) behave consistently with their own contracts, and that any endpoints which **proxy HDE** respect HDE’s transport posture while still being owned by the App.

This playbook focuses on:

* pinning paths/versions for App BE endpoints

* capturing stable header/body snapshots

* enforcing the same evidence/index parity rules used elsewhere

  #### **Inputs**

* A staging or prod-like environment exposing App BE public APIs.

* A list of App BE endpoints, tagged as:

  * **pure App** (no HDE involvement), or

  * **HDE-adjacent** (proxying data from HDE surfaces).

* Env pins for all captures:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

  #### **Scope**

* **In scope:**

  * Public App BE APIs that clients call directly.

  * Integration behavior where App BE endpoints **wrap or proxy** HDE results.

* **Out of scope:**

  * HDE service routes themselves (covered under §5.1 Catalog/A7 and §5.2 Aux).

  * Internal-only service-to-service calls that are not part of any QA surface.

  #### **Steps**

1. **Pin path and version per endpoint.**

   * For each App BE endpoint under QA:

     * Record its **canonical path** (e.g., `/api/app/matches/v1/...`).

     * Record its **version** (path or header-based).

   * Confirm documentation and implementation agree on path and version.

2. **Capture header/body snapshots (success).**

   * For each endpoint, send a representative **success** request.

   * Capture:

     * status code,

     * all response headers, and

     * the response body (or a checksum if sensitive).

   * Save snapshots under a governed location, for example:  
      `tests/transport/headers/app_be_<route>_200.snap` and  
      `tests/transport/body/app_be_<route>_200.json` (or `.txt`).

3. **Capture error posture proof.**

   * For each endpoint, send one or more requests that produce **typed errors** (e.g., validation error, unauthorized, internal error).

   * Capture:

     * status codes for each error case,

     * headers (especially `Content-Type`, `Cache-Control`, and any correlation IDs),

     * error body shape (field names, numeric/non-numeric posture).

   * Error semantics and policies are owned by App backend governance docs; where the endpoint proxies HDE errors, make sure those error responses either:

     * conform to App BE policy, or

     * clearly document that they surface HDE error posture (by title-only reference to PF05/PF04).

4. **Check HDE-adjacent endpoints.**

   * For endpoints that **proxy HDE** (e.g., match summaries derived from Reader), confirm that:

     * their upstream calls to HDE respect HDE contracts (PF05), and

     * they **do not weaken** HDE transport posture (e.g., no adding ETags to writers, no leaking internals).

   * These endpoints may choose to reframe data (new JSON shape), but they must not misrepresent HDE behavior.

5. **Update evidence indices.**

   * For each new or modified snapshot, add/update entries in:

     * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

     * `artifacts/evidence_index.jsonl`.

   * Ensure index updates occur in the **same PR** as the snapshots.

6. **Wire CI checks (via PF09).**

   * Add or update PF09 CI jobs to:

     * fail on missing snapshots for declared App BE endpoints,

     * fail on non-canonical or non-LF-terminated governed artifacts,

     * enforce that the Human Index and mirror entries exist for all governed App BE evidence.

   #### **Evidence**

* Success headers/body snapshots for each App BE endpoint:

  * e.g., `tests/transport/headers/app_be_<route>_200.snap`

  * e.g., `tests/transport/body/app_be_<route>_200.json`

* Error posture snapshots:

  * e.g., `tests/transport/headers/app_be_<route>_4xx.snap`

  * e.g., `tests/transport/body/app_be_<route>_4xx.json`

* Index updates in:

  * `docs/evidence/INDEX.json` (+ `.sha256`), and

  * `artifacts/evidence_index.jsonl`

All of the above must be present in the **same PR** as the code/config changes they describe.

#### **Tokens (names-only, App BE pattern)**

Exact token names for App BE QA live in App-specific governance/build docs. PF19 recommends patterns such as:

* `APP_BE_ROUTE_200_OK`

* `APP_BE_ERROR_POSTURE_OK`

* `APP_BE_SNAPSHOTS_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

When App BE endpoints proxy HDE surfaces, additional HDE tokens (e.g., `CLI_READER_PARITY_OK`) may apply, but only where those endpoints are explicitly part of HDE integration.

#### **Failures to watch**

* Path or version drift (documented path/version no longer matches implementation).

* Missing or stale snapshots for active endpoints.

* Error responses with unexpected status codes, missing `Content-Type`, or bodies that do not match declared error shapes.

* HDE-adjacent endpoints that:

  * leak HDE internals not meant for the App layer, or

  * diverge from HDE transport posture without clear App-specific policy.

* Evidence artifacts added without corresponding updates to the human index and machine mirror in the same PR.

  ### **5.4 App Frontend**

App-specific; this playbook is a **names-only placeholder**. The FE team fills in concrete tools, routes, and thresholds.

#### **Intent**

Prove that the **App Frontend** behaves correctly at a UI level in environments used for QA:

* routing and navigation work as expected

* feature flags and experiments are wired correctly

* basic accessibility and performance are within agreed limits

PF19 does **not** define FE tools or metrics. It only standardizes that FE QA runs produce governed artifacts and that those artifacts are indexed consistently.

#### **Inputs**

* A staging or prod-like FE environment (URL and build identifier).

* The current FE routing and feature flag configuration (by title only).

* Chosen FE QA tools or scripts for:

  * routing sanity checks

  * feature-flag smoke

  * basic accessibility and performance probes

  #### **Scope**

* **In scope:**

  * UI-level checks for routing sanity, feature flags, core flows, and high level accessibility or performance smoke.

* **Out of scope:**

  * HD Engine routes and bytes (those live in HDE-titled PF docs).

  * Detailed UX specs, design review, or full accessibility audits (these are owned by product and design documents).

  #### **Steps**

1. **Routing sanity run.**

   * Execute the FE routing test suite or script for the target environment.

   * Confirm that key routes load successfully (home, onboarding, match view, settings, etc).

   * Capture a concise summary and, if available, a machine-readable report (for example JSON or JUnit-style).

2. **Feature flag smoke.**

   * For the current flag configuration, run a minimal smoke test:

     * each flagged feature either renders or remains hidden according to its configuration

     * any experimental UI is reachable only under the expected conditions

   * Capture logs or reports that list which flags were exercised and with what outcomes.

3. **Accessibility and performance smoke.**

   * Run a light accessibility checker and performance probe for representative views.

   * Capture:

     * a summary score or classification

     * key issues or warnings (names only)

   * Deep audits and remediation are owned by FE/product; PF19 asks only for a repeatable smoke layer.

4. **Update evidence indices.**

   * Save FE QA outputs under governed paths. For example:

     * `artifacts/fe/routing_smoke_<env>.json`

     * `artifacts/fe/feature_flags_smoke_<env>.json`

     * `artifacts/fe/a11y_perf_smoke_<env>.json`

   * Add or update entries in:

     * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

     * `artifacts/evidence_index.jsonl`

   * Use **titles-only** descriptions for FE QA artifacts in the human index; schemas and mirror rules remain in PF12.

   #### **Evidence**

* FE routing smoke artifacts (for example `artifacts/fe/routing_smoke_<env>.json`).

* Feature flags smoke artifacts (for example `artifacts/fe/feature_flags_smoke_<env>.json`).

* Accessibility and performance smoke artifacts (for example `artifacts/fe/a11y_perf_smoke_<env>.json`).

* Indexed entries in:

  * `docs/evidence/INDEX.json` (+ `.sha256`), and

  * `artifacts/evidence_index.jsonl`,  
     with FE artifacts described by **title only** per PF12.

  #### **Tokens (names-only, FE pattern)**

Concrete token names for FE QA live in FE governance or build docs. PF19 suggests patterns such as:

* `APP_FE_ROUTING_SMOKE_OK`

* `APP_FE_FEATURE_FLAGS_SMOKE_OK`

* `APP_FE_A11Y_PERF_SMOKE_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

  #### **Failures to watch**

* Core routes not reachable or redirecting incorrectly in staging or prod-like environments.

* Feature flags enabled but not visible, or disabled but still rendering.

* Smoke accessibility or performance checks failing beyond agreed thresholds.

* FE QA artifacts stored outside governed paths (not under `artifacts/**` or `docs/**`).

* FE QA artifacts added without corresponding updates to the human index and machine mirror in the same PR.

Got it — no code fences, just clean doc-style text you can drop straight into PF19.

Here’s a more coherent, consistently spaced version in the same style you’ve been using:

---

### **5.5 DB & Vendor ingest (authoring plane → DB / sealed pack)**

Segmentation (names-only; titles-only routing).

* **App Backend (BE)** owns vendor ingest and the DB/packs.

* **HDE** must be capable of vendor calls when rails allow, but in **normal prod rails** reads **DB/packs** on `/reader` (transport/policy/tokens route by title).

Intent.  
 Prove that:

1. BE correctly ingests vendor data into DB and/or packs.

2. HDE can call the vendor when explicitly requested and rails permit.

3. In normal prod rails, HDE uses DB/packs (no live vendor on hot path).

Scope.

* **Per-call source selection only.** Source is chosen explicitly by the caller (CLI flag / ops param), not by engine “modes.” Unknown `ENGINE_*` envs fail fast. (Bytes/policy live in HDE-CLI-API-Vendor-Ref / HDE-Governance.)

* **Dev/test DB fallback (adapter).** In `APP_ENV=dev`, if `DATABASE_URL` is present but unusable, the adapter falls back to `DB_BRIDGE_URL(https)`; **no fallback** in prod unless guarded. Evidence is required.

* **Typed error on total DB failure.** Non-dev environments return a deterministic, numeric-free typed error; no proactive connectivity probe.

Inputs (names-only).

* A dev/stage environment for live posture (rails open as needed) and a prod-like environment (rails closed).

* Env pins for any governed capture: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Bridge base URL (names-only; lives in Infra) and CLI/ops entrypoints (titles-only).

Steps — A. BE ingest plane (vendor → DB / packs).

1. Run BE vendor ingest.

   * Keys-only logs confirm outbound vendor HTTP and DB writes / pack export.

2. Validate DB/pack outputs (spot-check).

   * Required fields, FKs, pack SHA-256s per PF12.

3. Index BE ingest evidence in the **same PR**.

   * Update human index \+ `.sha256` and machine mirror; governed paths only.

Steps — B. HDE as consumer & vendor-capable client.

1. **Source selection (explicit).**

   * Default without `--source=vendor`: use DB/packs if available (no vendor call).

   * With `--source=vendor` (or ops `source="vendor"`): perform live vendor call **only** if rails allow; otherwise return a typed refusal (keys-only).

2. **Dev fallback (adapter) when primary DSN fails.**

   * In `APP_ENV=dev`, simulate a broken `DATABASE_URL` with valid `DB_BRIDGE_URL(https)`.

   * Expect adapter to select the HTTPS bridge, proceed, and emit:

     * `artifacts/runtime/env_connectivity.snapshot.json` (attempts, outcome, selected).

     * Optional bridge capability snapshot (names-only routing).

   * Index evidence in the same PR (human \+ machine; path-proofs).

3. **Total DB failure (non-dev).**

   * Force both DSN/bridge to be unavailable.

   * Expect a typed, numeric-free error (no proactive probe). Confirm CLI exit code/patterns where applicable (titles-only).

4. **DB posture & durability (evidence).**

   * Prove runtime search\_path, grants, DDL fingerprint, and (if present) read-only boundary view; store canonical artifacts under governed paths and index in the same PR.

5. **Transport policy (vendor).**

   * Where vendor is called explicitly and rails allow, retry only on network/5xx per closed policy; **no jitter**; record 429 as a typed outcome (no auto-succeed in this epic). Keys-only logs throughout.

Evidence (titles/paths only; governed paths; index human+machine in same PR).

* DB posture & durability: `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`, optional `artifacts/db/db_rw_smoke.log`, and boundary-view proof if applicable.

* Dev fallback: `artifacts/runtime/env_connectivity.snapshot.json` (singleton snapshot for the event); optional `artifacts/db_bridge/adapter_selection.snapshot.json`, `artifacts/db_bridge/caps.snapshot.json`, and provider parity artifacts.

* Indexing discipline: update `docs/evidence/INDEX.json` \+ `.sha256` and `artifacts/evidence_index.jsonl` together; include `proof_anchor` path-proofs; governed paths only.

Tokens (names-only; definitions live in HDE-Governance / HDE-Build Checklist).

* **DB posture & durability:** `DB_SCHEMA_FINGERPRINT_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_GRANTS_OK`, `DB_BOUNDARY_VIEW_OK`, `DB_WRITERS_ISOLATED_OK`.

* **Dev fallback & bridge:** `DB_BRIDGE_FALLBACK_OK`, `DEV_DB_BRIDGE_FALLBACK_OK`, `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, optional `DB_RW_SMOKE_BRIDGE_OK`.

* **Connectivity & errors:** `DB_CONN_ENV_OK` (presence-only selection / typed error on total failure), `ENV_LC_ALL_C_OK`.

* **Index/mirror/path-proofs:** `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

Failures to watch.

* Vendor calls made without explicit `--source=vendor` (or ops equivalent) or while rails are closed.

* Missing `env_connectivity.snapshot.json` when dev fallback occurs.

* Non-deterministic retries (jitter), 429 auto-recovery in this epic, or logs with payload/secret content.

* Evidence captured but not indexed (human \+ mirror) in the same PR, or mirror records without path-proofs.

  


  ### **5.6 CLI/API & SDKs**

Cross-component; HDE CLI/API contracts and emitter bytes live in **PF05 — HDE-CLI-API-Vendor-Ref** (titles-only). Evidence plumbing for parity artifacts lives in **PF12 — HDE-Schemas & Artifacts** and **PF09 — HDE-Build Checklist**.

**Intent**  
 Prove that:

* CLI and SDKs are exact clients of the shared emitters (Reader, Aux).

* AB/BA runs and two-run identity hold for CLI output.

* CLI preview and SDK calls are in parity with the underlying HTTP emitter bytes.

This playbook is about **transport parity and determinism**, not about business logic.

**Inputs**

A dev or staging environment where:

* CLI is installed and can call HDE/App surfaces.

* SDKs (if present) can call the same routes programmatically.

Env pins for any capture:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

The CLI and SDK commands/entrypoints for:

* compatibility / match display,

* any Aux narrative or Reader preview functions.

**Scope**

In scope:

* CLI parity snapshots for a fixed pair (AB and BA).

* Two-run identity of CLI outputs for the same inputs.

* Parity between CLI/SDK outputs and canonical emitter responses (Reader/Aux).

Out of scope:

* UI formatting in terminals beyond what is required for parity proof.

* Non-governed, ad-hoc scripts or experimental SDK functions.

  #### **Steps**

1. **Establish a test pair and environment.**

   * Choose fixed test IDs; set env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

2. **Source selection (explicitness).**

   * Run CLI **without** `--source=vendor` when a cached BodyGraph exists → expect DB read; **no vendor call** observed in keys-only logs.

   * Run CLI **with** `--source=vendor` and rails open → expect vendor call; result is stored for durability where policy allows.

   * With rails closed, `--source=vendor` yields a **typed refusal** (no outbound HTTP).

3. **Capture CLI AB/BA snapshots.**

   * Produce AB and BA governed outputs (JSON or normalized); store under `artifacts/cli/...`.

4. **Check AB/BA parity.**

   * Verify symmetry where required and correct directional swap semantics.

5. **Check two-run identity.**

   * Re-run AB and BA; outputs must be byte-identical for governed parts.

6. **Verify emitter parity (CLI ↔ HTTP).**

   * Baseline against HTTP emitter (Reader/Aux) for at least one direction.

   * Verify structural/semantic parity between CLI output and HTTP response.

7. **Error parity (typed errors).**

   * Exercise a forced DB-unavailable scenario and a closed-rails vendor attempt.

   * Verify CLI and HTTP error envelopes are aligned (typed, numeric-free).

8. **Update CLI/API evidence indices.**

   * Add/update `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR.

**Evidence**

CLI AB/BA artifacts:

* `artifacts/cli/compat_ab.json`

* `artifacts/cli/compat_ba.json`

* Optional: `artifacts/cli/compat_summary.json`

SDK parity artifacts (if applicable):

* `artifacts/sdk/python_compat_ab.json`

* `artifacts/sdk/typescript_compat_ab.json`

Optional HTTP baseline:

* `artifacts/http/reader_compat_ab.json` or `artifacts/http/aux_ab.json`  
   (used internally to verify emitter parity, not necessarily shipped to users.)

Indexed records in:

* `docs/evidence/INDEX.json` (+ `.sha256`), and

* `artifacts/evidence_index.jsonl`

referencing the above artifacts **by title only** in the human index.

**Tokens (names-only)**

Common tokens that gate CLI/API & SDK QA (definitions live in PF04/PF09):

* CLI\_AB\_BA\_PARITY\_OK

* CLI\_TWO\_RUN\_IDENTITY\_OK

* CLI\_READER\_EMITTER\_PARITY\_OK

* CLI\_AUX\_EMITTER\_PARITY\_OK

* SDK\_READER\_PARITY\_OK

* SDK\_AUX\_PARITY\_OK

* EVIDENCE\_INDEX\_UPDATED\_OK

* MACHINE\_MIRROR\_UPDATED\_OK

**Failures to watch**

* CLI outputs for AB and BA that:

  * differ where they should be symmetric, or

  * fail to swap directional narratives correctly.

* Two-run identity failures:

  * CLI outputs differ between repeated runs with identical inputs,

  * timestamps or RNG leaking into governed sections.

* Emitter parity failures:

  * CLI or SDK returns different bands, categories, or narratives than the HTTP emitter,

  * missing categories or mismatched ordering relative to the emitter.

* SDK-specific inconsistencies:

  * one SDK applies rounding or transformation not present in the emitter,

  * SDK silently drops fields or adds extra computed ones without canonical backing.

* Evidence artifacts added or modified without corresponding updates to the human index and machine mirror in the same PR.

Emitter parity is normative. CLI and SDK outputs **must** be in parity with HDE emitters (Reader/Aux); parity artifacts are governed and indexed.

---

## **6\. Catalog/A7 proofs (collected rules; HDE-specific bytes live elsewhere)**

HDE-specific. Transport bytes and route contract live in **PF05 — HDE-CLI-API-Vendor-Ref**; policy and tokens in **PF04 — HDE-Governance**; schemas in **PF12 — HDE-Schemas & Artifacts** (titles-only).

### **6.1 Surface**

**Surface.** The **only** A7 proof surface is the **Catalog JSON success route**, currently:

* Path: `/reader` (locked initially)

* Env-gate: each environment has a cataloged entry; non-prod entries must not be reachable in prod

`/internal/version` and other ops or Aux endpoints are **not** A7 surfaces.

---

### **6.2 What must be captured**

For each environment where A7 is in scope, QA **MUST** capture:

* **GET 200 headers \+ body.**

  * JSON success response (cataloged)

  * Strong, quoted ETag over the LF-terminated body

  * Correct `Content-Type` and `Cache-Control` per policy

* **HEAD 200 headers.**

  * Mirrors GET’s validators and `Content-Type`

  * `Content-Length` equals the identity 200 body length

* **304 Not Modified.**

  * Elicited via `If-None-Match` / `If-Modified-Since`

  * **No body**

  * **No `Content-Type` or `Content-Length`**

  * Validators and `Vary` preserved as required

* **Quoted strong ETag.**

  * Present on 200 responses

  * Derived from LF-terminated body

  * Quoted form: `"…"`

* **Vary header.**

  * `Vary` includes at least `Authorization` and `Accept-Encoding` as required by policy

* **Encoding invariance.**

  * For all accepted encodings (identity/gzip/etc.):

    * ETag does not change with encoding

    * Effective Content-Length (after decoding) is stable

* **Env-gate proof.**

  * Headers-only proof that shows:

    * Only cataloged routes for that env are reachable

    * Non-prod entries from the Catalog are not reachable in prod

All captures must be done with env pins set:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

  ---

  ### **6.3 Composite proof JSON**

A single **composite A7 proof JSON** (or records-only JSONL) **MUST** be produced per environment:

* **Shape.**

  * Records-only, canonical JSON/JSONL (per PF12)

  * Each record includes at least:

    * `route_path`

    * `env_gate`

    * GET/HEAD/304 header snapshots

    * ETag and encoding flags

    * `vary_has_auth`, `vary_has_accept_encoding`

    * `encoding_invariance_ok`

* **Validation.**

  * Validated against the composite A7 proof schema defined in PF12 (titles-only)

  * CI must fail if the composite proof does not match the schema

* **Indexing (same PR).**

  * Composite proof JSON and all A7 headers snapshots are registered in:

    * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`)

    * `artifacts/evidence_index.jsonl`

  * Index updates occur in the **same PR** as the proof artifacts

  ---

  ### **6.4 Failures to watch**

* Missing or non-quoted ETag on GET 200

* HEAD posture diverging from GET (wrong `Content-Type` or `Content-Length`)

* 304 responses that include `Content-Type`, `Content-Length`, or a body

* Missing or incomplete `Vary: Authorization, Accept-Encoding`

* ETag or effective Content-Length changing with encoding

* Composite proof JSON failing PF12 schema validation

* Proof artifacts added without human index \+ mirror updates in the same PR

---

## **7\. Evidence & indexing reference (quick rules)**

* **Header names lower‑case.** All governed header snapshots store header names in **lower‑case**; values are verbatim. *Acceptance token:* **`SNAPSHOT_HEADER_LOWERCASE_OK`** (definition lives in PF05/PF09).  
* **Same-PR rule.**  
   The **Human Index** (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the **Machine Mirror** (`artifacts/evidence_index.jsonl`) **MUST** be updated in the **same PR** as any new or changed evidence artifacts.

* **Single‑file machine mirror.** `artifacts/evidence_index.jsonl` is the **only** mirror file; canonical JSONL; one LF per record; fixed field order; **unknown‑key reject**; each record includes a `proof_anchor`.

* **Capture posture & env pins.**

  * All evidence captures run with:

    * `LC_ALL=C`

    * `LANG=C`

    * `TZ=UTC`

  * Text surfaces (e.g., Aux Text vs Suppressed) should use **strict \+ tolerant** header snapshot patterns:

    * **strict** for exact posture checks,

    * **tolerant** for fields allowed to vary (dates, IDs).

  * These patterns are expected to be **adopted into PF09 CI harnesses** so drift is caught automatically.

---

## **8\. Tokens glossary (names-only; sources in PF04/PF09)**

PF19 lists names only. Token spellings and normative definitions live in **PF04 — HDE-Governance** and **PF09 — HDE-Build Checklist**.

**Pre-commit**

* `QA_PRECOMMIT_CHECKLIST_OK`

* `DET_SERIALIZER_OK`

* `TWO_RUN_IDENTITY_OK`

* `AB_BA_IDENTITY_OK`

**Post-commit (general)**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

**Aux**

* `NARR_200_TEXT_OK`

* `NARR_SUPPRESSED_NO_ETAG_OK`

* `COMPOSE_IDS_DETERMINISM_OK`

* `ENV_LC_ALL_C_OK`

* `NARR_VARY_AUTH_AE_OK` ← **added**

**Catalog/A7**

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

**CLI/API & SDKs** ← **new subsection**

* `CLI_AB_BA_PARITY_OK`

* `CLI_TWO_RUN_IDENTITY_OK`

* `CLI_READER_EMITTER_PARITY_OK`

* `CLI_AUX_EMITTER_PARITY_OK`

* `SDK_READER_PARITY_OK`

* `SDK_AUX_PARITY_OK`

**Build/CI (PF09):**

* `QA_FLAKY_TEST_QUARANTINE_OK`

**App FE/BE (App QA docs):**

* `APP_FE_WCAG_AA_OK`

* `APP_FE_WEB_VITALS_OK`

* `APP_SEC_ASVS_MIN_OK`

*Note: names‑only; definitions live in PF09 and App QA/security governance.*

---

## **9\. Templates & harnesses (to be filled; titles-only anchors)**

This section names the standard QA templates and harnesses. Concrete formats, scripts, and CI wiring live in **PF09 — HDE-Build Checklist** and **PF12 — HDE-Schemas & Artifacts** (titles-only).

### **9.1 Pre-commit checklist (CI job stub)**

**Anchor.** “Pre-commit QA checklist (PF09 CI stub)”  
 **Purpose.** A copyable block that teams can drop into their CI config to enforce:

* lint \+ format

* JSON/JSONL canonicalization and final-LF checks

* deterministic, no-I/O tests

* snapshot hygiene and env pins

**Notes.**  
 PF19 defines the required items; PF09 provides the actual CI job template and examples.

---

### **9.2 Post-commit capture checklist (headers \+ index)**

**Anchor.** “Post-commit evidence capture checklist”  
 **Purpose.** A step-by-step recipe to:

* capture headers/body snapshots (Text, Suppressed, A7 surfaces)

* generate composite proof JSON (when A7 is in scope)

* update `docs/evidence/INDEX.json` \+ `.sha256` and `artifacts/evidence_index.jsonl` **in the same PR**

* **Governed locations only.** All indexed artifacts **must** live under `artifacts/**` or `docs/**`. Transient/generator paths are **forbidden** as sources for indexed evidence. ← **added**

* normalize header names to lower-case before persisting governed snapshots

**Notes.**  
 PF19 describes the sequence; PF09 carries the concrete shell/CI snippets for running it.

---

### **9.3 Validated-tuple QA harness (Aux & CLI parity)**

**Anchor.** “Validated-tuple QA harness for Aux & CLI parity” ← **heading & anchor adjusted**  
 **Purpose.** A small, repeatable harness that:

* takes fixed test tuples as inputs

* sets env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`)

* **harness must invoke the shared emitter path used by HTTP and CLI; no alternate serializers.** ← **added**

* calls Aux via BE/CLI and writes snapshots under `tests/transport/headers/`:

  * `aux_text_200.snap`

  * `aux_suppression_200.snap`

**Notes.**  
 Runs without env-gates; the CLI preview is always available and calls the same emitter as Aux. Parity artifacts are indexed in the same PR.

---

### **9.4 A7 proof capture recipe**

**Anchor.** “A7 proof capture recipe (Catalog /reader)”  
 **Purpose.** A reusable recipe that:

* captures GET/HEAD/304 headers for the Catalog JSON success route

* verifies strong quoted ETag, Vary, and encoding invariance

* captures env-gate proof (non-prod entries unreachable in prod)

* builds and validates composite A7 proof JSON against PF12 schema

**Notes.**  
 PF19 defines what must be proven; PF09 and PF12 provide the concrete CLI/curl/runner scripts and schema.

---

### **9.5 Mirror schema quick-check**

**Anchor.** “Machine mirror schema quick-check”  
 **Purpose.** A small tool or CI step that:

* loads `artifacts/evidence_index.jsonl`

* verifies:

  * sorted keys and pinned field order

  * exactly one LF per record

  * canonical JSONL form

  * rejection of unknown keys

**Notes.**  
 PF19 names the required checks; PF12 defines the mirror schema, and PF09 supplies the quick-check implementation (e.g., a Python or Go verifier).

---

## **10\. Roles & RACI (QA)**

### **10.1 QA roles (titles-only pointer to PF06)**

Process flow, handoffs, and non-QA responsibilities are defined in **PF06 — Epic-Process-Guide**. PF19 only adds QA-specific duties.

**Implementation Agent (IA)**

* Responsible for designing the QA plan for each epic (what to prove, which playbooks apply).

* Responsible for making sure pre-commit and post-commit checklists are followed.

* Responsible for collecting QA artifacts (snapshots, logs, proof JSON) and placing them under governed paths.

* Responsible for updating the Human Index and Machine Mirror in the same PR as the evidence.

* Consulted on QA-relevant ambiguities during CodEx runs.

* Informed about any QA deviations CodEx introduces.

**CodEx**

* Responsible for executing QA steps defined by the IA:

  * running pre-commit and post-commit QA jobs,

  * capturing headers/snapshots/proof JSON,

  * generating CLI/SDK parity artifacts,

  * running mirror quick-checks.

* Responsible for reporting QA outcomes in the change report (what passed, what was skipped, what failed).

* Consulted on feasibility of QA harnesses and CI wiring.

* Informed about process constraints from PF06/PF19.

**Lead Developer**

* Accountable for QA coverage per epic: ensuring the right playbooks were applied and the right tokens are satisfied.

* **Accountable that HDE playbooks (§5.1/§5.2/§5.5/§5.6) ran and required tokens are satisfied; merge-block if same-PR evidence parity (human index \+ mirror) is missing.**

* Responsible for PR gate review on QA:

  * verifying tokens (names-only) such as `QA_PRECOMMIT_CHECKLIST_OK`, `A7_*_OK`, `NARR_*_OK`, `EVIDENCE_INDEX_*_OK`,

  * verifying evidence is present and indexed (same-PR rule).

* Consulted on any QA scope changes or exemptions.

* Informed of any QA failures that block merge.

**Product Owner (PO)**

* Accountable for accepting or rejecting an epic with its QA state.

* Responsible for merging only when QA tokens and artifacts meet the agreed bar.

* Informed about QA risks or exceptions flagged by Lead Dev/IA.

* Consulted when trade-offs are needed (e.g., partial QA vs timeline).

**Scrum Master**

* Responsible for tracking QA completion across epics (which tokens are satisfied, which playbooks have run).

* Responsible for reflecting QA state on boards and in sprint reports.

* Informed after merges so that QA outcomes are recorded.

* Consulted on QA workload, sequencing, and coordination between FE/BE/HDE teams.

  ---

  ### **10.2 Component ownership**

PF19 is the orchestration guide for QA. Day-to-day ownership of specific playbooks lives with the corresponding component leads:

**FE Lead / App Frontend owner**

* Responsible for keeping the App Frontend playbook (§5.4) accurate and current (tools, routes, thresholds).

**BE Lead / App Backend owner**

* Responsible for the App Backend (non-HDE) playbook (§5.3), including error posture proofs and endpoint coverage.

**HDE Lead / Engine owner**

* Responsible for the HDE Catalog/A7 (§5.1) and Aux & CLI preview (§5.2) playbooks, including reviewed tokens and proof surfaces.

**DB/Vendor ingest owner (usually BE)**

* Responsible for the DB & Vendor ingest playbook (§5.5), ensuring ingest jobs, DB schemas, and pack flows are accurately reflected.

**CLI/API & SDKs owner**

* Responsible for the CLI/API & SDKs playbook (§5.6), including AB/BA parity, two-run identity, and emitter parity artifacts.

For each component:

* The component owner is Responsible for keeping its playbook up to date.

* The Lead Dev is Accountable that all required playbooks for an epic are applied.

* The IA is Responsible for invoking the right playbooks and wiring them into CodEx instructions.

* The Scrum Master is Informed about which playbooks were run and what passed/failed.

  ---

  ## **11\. Change control**

  ### **11.1 Living document**

* PF19 is a living QA guide.

* References to **PF10 — HDE-Build Notes** must always be **by title only** (no version numbers, no inlined content).

* When a PF10 item is “drained” into a canonical PF doc (for example PF04, PF09, PF12, etc.), PF19 must be updated to:

  * point at the new canonical home by title, and

  * remove or rewrite any stale notes that referenced the interim PF10 guidance.

* Apply **PF03 — Technical Writing Best Practices** discipline:

  * keep a single home for each rule,

  * avoid duplicating bytes/schemas/tokens,

  * use clear, minimal redlines when updating PF19.

    ### **11.2 Supersession rule (PF10 addenda)**

* PF10 addenda are ordered. When multiple PF10 addenda address the same topic, the newer addendum supersedes the earlier.

* If PF10 addenda conflict, PF19 must follow the later addendum until that guidance is drained into canon.

* When updating PF19:

  * consult PF10 in addendum order,

  * resolve conflicts in favor of the latest addendum,

  * then route long-term rules to their canonical PF homes (PF04/PF09/PF12/… by title only).

