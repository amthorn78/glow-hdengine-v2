# **0\. Front Matter**

## **0.1 Header**

**Title:** PF19-Canon-Glow QA Guide

**Status:** Canon

**Version:** 1.0.7

**Effective date:** 2025-11-25

**Invocation tag:** INV-f2ac55d77ce9aacc

**Last Update Gate:** BN 7.7.8 Drain A23

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

**Epics and phased planning (titles-only).**  
 PF19 treats epic planning and phase mapping as outside its scope. For HD Engine epics, the single home is **HDE Phased Epics**. **HDE Epics Map** is maintained as historical context only and must not be used as the source of truth for new work. In particular:

* **HDE-EPIC011 — Vendor Ingest & Data Durability** is recorded as a **failed epic**; its acceptance roster (DB posture, ingest idempotence, evidence discipline, partition plan, SAFE rails, BodyGraph invariance) did not reach a fully green, production-ready state.

* **HDE-EPIC012–HDE-EPIC014** are preserved as “won’t do” (historical design), and any residual work they described must be captured as recorded debt or re-scoped into new epics in **HDE Phased Epics**, not treated as open acceptance here.

PF19 may reference these epics by title when describing QA history or preservation surfaces, but any **new** epic-level QA decision (for example, where to land future PK, partition, or Catalog/A7 work) **must be routed by title to HDE Phased Epics**, not to HDE Epics Map.

PF19 owns QA principles, checklists, and cross-component playbooks; it routes all transport, math, schema, and token details to those single homes.

## **0.3 Acceptance tokens (names-only; initial)**

The following governance tokens apply to PF19 itself; definitions and semantics live in **HDE-Governance** and **HDE-Build Checklist**:

* `QA_GUIDE_INIT_OK`

* `QA_PRECOMMIT_CHECKLIST_OK`

* `QA_POSTCOMMIT_CHECKLIST_OK`

* `QA_EVIDENCE_HARNESS_OK`

  ---

## 0.4 Principles & Single Homes (routing only)

### 0.4.1 Intent

Pin what PF19 owns (**process, checklists, playbooks**) versus where **bytes** and **policy** live. PF19 stays names-only and routing-only.

PF19:

* stays **titles-only** for all external references, and

* never restates transport bytes, schemas, or token tables.

### 0.4.2 Single homes (titles-only)

PF19 routes to these existing single homes:

* **Transport bytes & public routes:** PF05 — HDE-CLI-API-Vendor-Ref

* **Schemas & artifacts** (catalogs, mirror, proof JSON): PF12 — HDE-Schemas & Artifacts

* **Governance** (A7 policy, refusal/writers, tokens): PF04 — HDE-Governance

* **Architecture** (single emitter, boundaries): PF02 — HDE Architecture

* **Build checklists & CI gates:** PF09 — HDE-Build Checklist

* **Narrative rules & surfaces:** PF17 — HDE Narratives Guide

* **Process (PR-first):** PF06 — Epic-Process-Guide

### 0.4.3 Core principles (names-only)

PF19 assumes and reinforces these core QA principles:

* **Titles-only cross-refs.**  
   No duplicated bytes or schemas; always route to the owning PF by title. PF19 never redefines wire contracts or token semantics.

* **Determinism & env pins (all environments).**  
   All canonicalization, hashing, header snapshotting, and governed evidence capture **MUST** run with:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* These pins apply in **dev, stage, prod, and CI** whenever governed bytes are produced. (Definitions/tokens live in HDE-Governance / HDE-Build Checklist; PF19 enforces their use in QA playbooks.)

* **Same-PR parity for evidence.**  
   The Human Evidence Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) are updated **together in the same PR** whenever evidence changes. Schema and CI rules live in HDE-Schemas & Artifacts / HDE-Build Checklist; PF19 requires QA to treat “code change without evidence parity” as a failure, not a warning.

* **Evidence completeness (Index ↔ Mirror ↔ path\_proof).**  
   For governed evidence, QA is responsible for **completeness**, not just formatting:

  * Every governed artifact under `docs/**` or `artifacts/**` **must** have:

    * one Human Evidence Index entry in `docs/evidence/INDEX.json`,

    * one Machine Mirror record in `artifacts/evidence_index.jsonl`, and

    * one co-located `path_proof.txt` whose path is referenced by the Mirror record’s `proof_anchor`.

  * Mirror entries and path-proofs follow schema and field semantics defined only in **HDE-Schemas & Artifacts** (titles-only).

  * Lifecycle and OPS-managed artifacts (for example backup/restore/retention runs) still follow the same triple: **artifact → path\_proof → Mirror record**. If any leg is missing, QA must treat the evidence as **incomplete** and block tokens that depend on it.

* **CI default CLOSED (rails).**  
   CI pipelines run with rails closed by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`). Any job that opens rails **must**:

  * pin SAFE policy (timeouts/retries/backoff from closed domains; no jitter) as defined in Governance, and

  * attach governed evidence and update Index \+ Mirror in the same PR.

* **A7 is Catalog-only.**  
   A7 proofs run only on a **cataloged JSON success route** (Catalog/A7 surface); Aux HEAD/304 are out of scope under EPIC-010. PF19 never treats `/internal/*` (including `/internal/version`) as an A7 surface; ops/posture rules for those routes live in Governance.

* **A7 depends on Endpoint Catalog.**  
   A7 QA only runs when **Endpoint Catalog artifacts** exist and declare the route under test:

  * `docs/ENDPOINTS_CATALOG.json` is present and valid per HDE-Schemas & Artifacts.

  * The Catalog row for the Reader JSON success surface exists and is marked as a JSON success route.

* If these conditions are not met, QA treats the A7 suite as **gated off**:

  * no A7 tokens are claimed for that PR, and

  * the missing or invalid Catalog entry is reported as a QA failure, not a cosmetic skip.

* **Industry anchors (reference-only).**  
   PF19’s QA rules and proofs align with:

  * **IETF RFC 9110/9111** for HTTP semantics and caching (ETag strength/quoting, HEAD parity, 304 header/body rules);

  * **RFC 8785 (JCS)** for JSON canonicalization (HDE-Schemas & Artifacts governs canonical JSON; PF19 cites JCS as an external anchor);

  * **OWASP ASVS** for App FE/BE security verification;

  * **NIST SSDF** and **SLSA** for supply-chain QA and provenance expectations.

* PF19 remains titles-only; bytes, schemas, and token definitions stay in PF05/PF12/PF04/PF09.

---

# 1\. Environments & surfaces map (names-only)

## 1.1 Intent

Name the QA-relevant **surfaces** and where their **ownership** lives, with a clear split between:

* **App layer** (FE/BE)

* **HD Engine layer** (HDE service and its callers)

* **Shared tools and evidence system**

HDE-titled PF docs apply **only** to **HD Engine** surfaces. They do **not** define contracts for pure App FE or non-HDE App BE endpoints. PF19 stays names-only here: no header matrices, no byte listings, no schemas.

---

## 1.2 App layer (FE and non-HDE backend)

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

## 1.3 HD Engine layer (HDE-only)

HDE PF docs apply **only** to the Engine’s surfaces and their direct callers: **Catalog/Reader JSON success** (A7 surface), **Aux narrative text** (non‑A7), and **CLI admin preview** using the **same emitter**. PF19 routes bytes to **PF05**, artifacts/mirror to **PF12**, governance to **PF04**, mechanics to **PF14**, narratives to **PF17**, and epics to **PF16** (titles‑only). App FE/BE are **out of scope** for HDE policy except where App endpoints **proxy HDE**; in those cases they must preserve HDE contracts.

* **HD Engine service (Reader, Aux via BE).**  
   Core Engine HTTP surfaces, exposed to the App BE as internal services (Reader JSON, Aux narrative text).

  * Implementation and deploy: `glow-hdengine-v2` service (names-only).

  * Transport bytes and public routes: **PF05 — HDE-CLI-API-Vendor-Ref**.

  * Architecture and boundaries: **PF02 — HDE Architecture**.

  * Governance and A7 policy: **PF04 — HDE-Governance**.

  * All other Engine details: HDE-titled PF docs (PF01, PF12, PF14, PF16, PF17) by title only.  
  * **Epics map (historical vs current).**  
     For HD Engine epics, **HDE Epics Map** is now **historical-only**; it records past epic allocations, including **HDE-EPIC011** as a failed epic and **HDE-EPIC012–HDE-EPIC014** as “won’t do”. The current source of truth for epic planning, phase mapping, and epic-level acceptance rosters is **HDE Phased Epics**. QA must:  
    * treat any epic references in HDE Epics Map as **historical context only**, and

    * route new epic-level QA decisions and open work to **HDE Phased Epics**, not to HDE Epics Map.

* **HD Engine integration in App BE.**  
   Backend endpoints that call HDE are responsible for preserving HDE contracts at the integration boundary.

  * HDE contracts: defined only in HDE-titled PF docs (titles-only, no duplication).

  * App BE wrapping behavior: defined in backend API docs; PF19 treats it as part of App BE QA with additional checks that HDE contracts are honored.

---

## 1.4 Shared tools and evidence system

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

# 2\. Pre-commit QA (local/CI)

## 2.1 Intent

Catch issues **before** PRs merge by enforcing a consistent local/CI QA baseline across all projects.

Pre-commit QA focuses on:

* code quality and formatting

* deterministic behavior (no hidden I/O or randomness)

* snapshot and evidence hygiene

* early detection of schema/contract drift

Concrete CI wiring and gates are instantiated in **PF09 — HDE-Build Checklist** (titles-only); PF19 defines the shared “what,” not the CI job syntax.

---

## 2.2 Checklist (to be instantiated in PF09 CI)

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

    

* **Evidence-governed CI sequence (names-only).**

  For PRs that change **governed evidence artifacts** (Index, mirror, ordering artifacts, path-proofs, orientation demo), the pre-commit/CI pipeline **SHOULD** follow this sequence under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`):

1. **Generate ordering artifacts (write, then check, when in scope).**

   * Run the ordering generator once in **write mode** (no `--check`) to refresh ordering artifacts in `artifacts/engine/order/**` from the current sources (catalogs, manifests, and Engine math).

   * Then run the same generator again with its **`--check`** mode (see HDE-Mechanics Guide) to prove **two-run identity**: a second run over an unchanged tree produces no changes to the ordering artifacts.

2. **Update Evidence Index and mirror (write, then check).**

   * Run the Evidence Index/mirror tool once in **write mode** to rewrite `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and all governed `*.path_proof.txt` from the current artifact set (single source of truth).

   * Then run the same tool again with **`--check`** to confirm that a second run is a no-op (no unindexed or dangling artifacts, no missing proofs, no schema violations).

3. **Run topology orientation checks.**

   * Run the orientation demo tool with `--check` to validate that `audit/gates/topology/orientation_demo.txt` is coherent with the current INDEX/mirror state and not stale.

4. **Enforce mirror schema and path-proof discipline.**

   * Run the mirror-schema quick-check (see §10.5) to validate field set/order, canonical JSONL form, single mirror file, and `proof_anchor` alignment with `*.path_proof.txt`.

5. **Run ordering/evidence test suites.**

   * Run the pytest suites that cover ordering properties and evidence skeleton behavior (titles-only); treat any failure as a CI failure for governed artifacts.

     PF19 defines the required sequence at the QA level; **PF09 — HDE-Build Checklist** and **HDE-Mechanics Guide** provide the concrete tool names and CI job definitions.  
* **Engine serializer/composer determinism.** Prove two‑run identity and AB↔BA parity (where defined). Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules. (Tokens live in PF04/PF09; bytes in PF14/PF12.)

* **Secrets & SCA/SAST/DAST.** Run secrets scanning and composition analysis; add SAST/DAST appropriate to the repo. Keep test logs **keys‑only** (no payloads/secrets). Governance in PF04; CI wiring in PF09.

* **Reproducibility & flake control.** Fix seeds; avoid wall‑clock; pin locale/timezone; quarantine flakes with **`QA_FLAKY_TEST_QUARANTINE_OK`** until deflaked (token home PF09).  
* **Test data & PII.** Use synthetic fixtures; redact payloads; enforce keys‑only logs in tests (policy PF04).

  # 3\. Post-commit QA (staging/prod)

  ## 3.1 Intent

Prove **route posture**, **capture evidence**, and **update indices in the same PR** once changes are deployed to a staging or production-like environment.

Post-commit QA focuses on:

* confirming each surface behaves as promised (status, headers, body)

* capturing stable evidence (snapshots and proof JSON)

* updating both the **human index** and the **machine mirror** in the **same PR** that carries the evidence

Concrete schemas, tokens, and CI wiring live in PF04, PF09, and PF12 (titles-only); PF19 defines the shared checklist.

---

## 3.2 Checklist

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

## 3.3 Environment constraints — pre-App, no-user QA mode

In the current deployment posture, there is **no app-level user model** integrated with the HD Engine and **no persistent user-bound BodyGraph records** available for QA in production. Until the Glow App introduces a real user model and a future epic defines user-bound QA surfaces (see HDE Phased Epics), QA must follow a **no-user QA mode** for Engine and CLI Live QA.

**Reality (pre-App).**

* No app-level user IDs exist for the Engine to reference in prod.

* There are **no persistent BodyGraphs keyed to app users** that QA may rely on as fixtures.

* QA **must not create app-like user records in prod** ahead of Glow App integration.

**Effect on QA requirements.**

* Any QA requirement that assumes “existing users in prod” (for example, `showcompat --user-a/--user-b --source=db` or `bg:resolve` against real app user IDs) is treated as **blocked by environment**, not as failed acceptance.

* Those requirements must be explicitly called out in epic-level QA plans and deferred to a future epic once the app user model exists in **HDE Phased Epics** (titles-only).

* QA **must not** work around this by synthesizing “fake app users” in prod; doing so is considered a violation of this guide.

**Interim no-user QA mode (pattern).**

Until the app user model is live, use the following pattern for Engine/CLI QA in staging/prod-like environments:

1. **Compat & Reader from births only.**

   * Use `hdctl showcompat` with **birth arguments only** (birthdate/time/location flags as defined in CLI/API docs; titles-only).

   * Do **not** use `--user-a/--user-b` or `--source=db` in prod QA, because there are no app users or DB-backed BodyGraphs to rely on.

   * Verify:

     * canonical JSON output on stdout,

     * AB↔BA identity by swapping the birth tuples, and

     * Reader v1 envelopes via `--dump-reader` (shape and band-only posture per HDE-Math-Spec and HDE-CLI-API-Vendor-Ref; titles-only).

2. **Aux narratives from compat JSON (no DB users).**

   * Use `hdctl aux-preview --pair-file <compat.json>` (or equivalent API) based on **birth-generated compat JSON**.

   * Do **not** rely on DB users or user-bound records for Aux tests; treat compat JSON as the source of truth for Aux QA.

3. **BodyGraph resolver & vendor ingest (ephemeral QA keys).**

   * Treat any `--user` value used in `bg:resolve` during QA as an **ephemeral QA key**, not as a real app user ID. Keys should be clearly marked as QA (for example `qa_epic017_resolve1`, `qa_epic017_vendor1`).

   * In prod pre-App:

     * Allow:

       * `bg:resolve` DB/auto **stub** behavior (no real DB dependency on app users).

       * `bg:resolve --source=vendor` under **closed rails** → typed refusal (no vendor calls).

       * `bg:resolve --source=vendor --dry-run` under **open rails** → single vendor call returning ingest metadata and **no DB writes**.

     * Disallow:

       * `bg:resolve --source=vendor --upsert` in prod, because it would create rows that look like real user records. These flows are **explicitly out of scope** until the app user model is live and owned by a future epic.

4. **Evidence discipline (no-user runs).**

   * Treat all compat/Aux/resolver artifacts produced under this mode as **governed evidence**:

     * capture them under `artifacts/**` or `docs/**` as appropriate,

     * update `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the **same PR**, and

     * ensure machine-mirror records include `proof_anchor` path-proofs.

   * Any mutation of the Evidence Index/Mirror caused by a no-user QA run must be deliberate and explained; accidental mutations are defects to be fixed before tokens depending on those artifacts are claimed.

**Forward plan (when users exist).**

* When the Glow App introduces a real user model and a future epic defines user-bound QA flows in **HDE Phased Epics**, this section remains as **historical pre-App posture**.

* At that point, new QA playbooks may introduce DB-backed compat and `bg:resolve --source=vendor --upsert` tests in prod/stage, but only under clearly defined epics and tokens.

## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**

For **HDE-EPIC017**, manual Live QA converged on a specific pattern that PF19 adopts as the reference pattern for Engine Live QA:

**Execution pattern (one command → one artifact).**

* Each manual Live QA step consists of a **single CLI or HTTP command** run from a Codespace attached to the engine repo.

* That command must write exactly **one primary evidence file** (log or JSON) under:

  * `audit/qa/hde-epic017/logs/`, or

  * another clearly named subdirectory under `audit/qa/hde-epic017/**`.

* The designated Live QA reviewer (for example a QA persona like Kronos) reviews that primary file and issues a short QA addendum (QA0X) summarizing:

  * which command was run,

  * what behavior was observed,

  * any document deltas, and

  * the QA verdict for that step.

* Any helper files for that step (for example parsed JSON derived from the log) also live under `audit/qa/hde-epic017/**` and are referenced from the same addendum, but there is always **one** clearly identified primary artifact per step.

**Rails posture for manual Live QA (EPIC017 only).**

* Manual Live QA steps that touch **vendor** or **Railway** prod run with **open rails** in the Codespace as required by the command (for example `ALLOW_NETWORK=1`, `SAFE_MODE=0`):

  * CLI compat/Reader/Aux previews hitting Railway or vendor;

  * vendor dry-run ingest calls (`bg:resolve --source=vendor --dry-run`).

* Manual Live QA must **not** modify code or configuration and must **not** write outside `audit/qa/**` for evidence.

* Closed-rails testing (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) remains the responsibility of:

  * CI jobs wired in the repo (pytest suites, evidence tools, mirror checks, ordering tests, etc.), and

  * pre-merge QA on PRs implementing EPIC017 foundations.

Manual Live QA does **not** attempt to replicate those closed-rails tests; instead it focuses on demonstrating real prod behavior of key surfaces via open-rails commands from Codespaces into Railway.

**Vendor and DB safety constraints.**

* Even under open rails:

  * `bg:resolve --source=vendor --upsert` remains **forbidden** in pre-Glow prod; vendor QA must use `--source=vendor --dry-run` or canonically defined closed-rails stubs.

  * DB writes that resemble real app users remain out of scope until a Glow App user model exists (see pre-App no-user QA mode and related addenda by title).

Teams designing Live QA for future epics **SHOULD** start from this EPIC017 pattern (one command → one artifact from Codespaces into Railway, with closed-rails tests delegated to CI) and adapt it only where epic-specific surfaces or rails require a different approach.

---

# 4\. Evidence & indexing (how to prove; titles-only for schemas)

## 4.1 Intent

Normalize **how** we capture and register evidence across projects, while keeping all **schemas and field definitions** in their existing single homes.

PF19 defines:

* what must be captured

* where it must live

* how it must be kept in sync

All schema details and field shapes remain in **PF12 — HDE-Schemas & Artifacts** and **PF09 — HDE-Build Checklist** (titles-only).

---

## 4.2 What to capture

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

## 4.3 Rules

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

### 4.3.1 Provenance vs filesystem time (`produced_at_utc` vs `mtime_utc`)

QA needs to distinguish **when evidence was produced** from **when files were last observed on disk**:

* `produced_at_utc` (Mirror field) records **when the evidence harness ran** and wrote that record. It is the logical “evidence refresh time”.

* `mtime_utc` (stored in `path_proof.txt` and summarized in the Mirror) records the artifact’s **refresh-time mtime** — the filesystem modification time observed when the evidence job refreshed that artifact.

**Rules (semantics from PF12 — HDE-Schemas & Artifacts).**

* `produced_at_utc` is a **logical timestamp** and MUST NOT be hand-edited. If the value is incorrect or missing, re-run the evidence harness; do not patch Mirror or proofs by hand.

* `mtime_utc` is a **refresh-time mtime**, not a long-lived replica of `stat().st_mtime`:

  * It is captured as a UTC ISO-8601 timestamp (`YYYY-MM-DDThh:mm:ssZ`) with **zero microseconds** (no fractional seconds).

  * On any evidence run or CI check, QA must ensure that `mtime_utc` parses as UTC and that the parsed time is **not later than** the artifact’s current filesystem `stat().st_mtime` (monotone semantics).

  * `mtime_utc` is **not required** to equal `stat().st_mtime` in later runs or on other machines; it may be earlier (for example, when a proof is carried forward after a no-op run), but it MUST NEVER lie in the future relative to the current filesystem mtime.

* QA checks for lifecycle or OPS-managed artifacts should always examine both:

  * `produced_at_utc` (“when did we prove this?”), and

  * `mtime_utc` (“what file state did we observe when we refreshed evidence?”),

* and treat any violation of the format or monotone constraints as a **blocking failure** for the affected tokens.

**Integrity criteria.**

The canonical acceptance criteria for path-proof integrity are now:

* **Hash/size equality:**

  * The `sha256` and `size_bytes` in the path-proof must match the artifact’s canonical bytes on disk and the Mirror record’s `sha256`/`size_bytes`.

* **Time semantics:**

  * The `mtime_utc` in the path-proof must satisfy the refresh-time/monotone rules above (valid UTC ISO, microsecond==0, `parsed_mtime <= current_fs_mtime`).

* **Single triple:**

  * Each path-proof contains exactly one `path`/`sha256`/`size_bytes` triple per artifact; multiple or conflicting sha/size pairs in a single proof file are not allowed.

If any of these checks fail (including `mtime_utc` format or monotonicity), QA MUST treat the corresponding tokens (for example `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`) as **not satisfied** and block the epic or PR until the evidence tooling and artifacts are corrected and re-run.

Any future change to `mtime_utc` semantics (for example, tightening the monotone rule) MUST be:

* specified in PF12 (Machine Evidence Index / path-proof schema),

* reflected in this section of PF19, and

* accompanied by coordinated changes to the evidence tools and tests, before QA treats the new behaviour as acceptable.

---

# 5\. Component playbooks (how to run QA per surface)

Each playbook follows the same pattern:  
 **Intent · Inputs · Steps · Evidence · Tokens (names-only) · Failures to watch · Where it lives (titles-only)**

PF19 describes how to run QA; all bytes, schemas, and detailed policy live in their single-home PF docs (titles-only).

---

## 5.1 HD Engine — Catalog/A7 (HDE-specific)

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

  ## 5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)

Cross-component; Aux bytes and emitter behavior live in **HDE-CLI-API-Vendor-Ref** and **HDE Narratives Guide** (titles-only). A7 remains **Catalog-only**; Aux HEAD/304 are out of scope.

### Intent

Prove that **Aux narrative text** and **Aux suppression** behave correctly at the shared emitter level, and that **CLI preview** reflects the same bytes.

This playbook is about:

* a minimal but **strict** header posture for Aux, and

* ensuring the CLI uses the **same emitter** and cannot silently “suppress” narratives due to missing tuples or mis-wired composition.

  ### Inputs

* A staging or prod-like environment where Aux can be invoked via BE/CLI.

* Env pins for all captures:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* A **validated-tuple QA harness** (CLI or script) that:

  * calls the shared Aux emitter for a known test pair, and

  * can emit headers snapshots for text and suppression cases.

  ### Scope

For **EPIC-010**, post-commit Aux QA covers **two snapshots only**:

* `tests/transport/headers/aux_text_200.snap`

  * 200, LF-terminated text body, **quoted strong ETag** over that body.

* `tests/transport/headers/aux_suppression_200.snap`

  * 200, **empty body**, **no ETag**.

Aux **HEAD/304** are not part of A7; A7 remains Catalog-only.

### Steps

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

   ### Evidence

* `tests/transport/headers/aux_text_200.snap`

* `tests/transport/headers/aux_suppression_200.snap`

* Optional CLI parity artifacts (e.g., `artifacts/cli/aux_preview.json`) if defined in PF09/PF12.

* Updated records in:

  * `docs/evidence/INDEX.json` (+ hash sentinel), and

  * `artifacts/evidence_index.jsonl`  
     in the **same PR** as the snapshots.

  ### Tokens (names-only)

Typical tokens used to gate Aux/CLI preview QA (definitions live in PF04/PF09):

* `NARR_200_TEXT_OK`

* `NARR_SUPPRESSED_NO_ETAG_OK`

* `COMPOSE_IDS_DETERMINISM_OK`

* `ENV_LC_ALL_C_OK`

  ### Failures to watch

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

  ## 5.3 App Backend (non-HDE endpoints)

App-specific; these endpoints are **not** governed by HDE PF docs unless they proxy or surface HD Engine responses. Transport contracts for pure App APIs live in App backend API docs. HDE docs may be used as patterns, not as authority, except where the App BE directly wraps HDE surfaces.

### Intent

Prove that **App Backend public APIs** (beyond HDE) behave consistently with their own contracts, and that any endpoints which **proxy HDE** respect HDE’s transport posture while still being owned by the App.

This playbook focuses on:

* pinning paths/versions for App BE endpoints

* capturing stable header/body snapshots

* enforcing the same evidence/index parity rules used elsewhere

  ### Inputs

* A staging or prod-like environment exposing App BE public APIs.

* A list of App BE endpoints, tagged as:

  * **pure App** (no HDE involvement), or

  * **HDE-adjacent** (proxying data from HDE surfaces).

* Env pins for all captures:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

  ### Scope

* **In scope:**

  * Public App BE APIs that clients call directly.

  * Integration behavior where App BE endpoints **wrap or proxy** HDE results.

* **Out of scope:**

  * HDE service routes themselves (covered under §5.1 Catalog/A7 and §5.2 Aux).

  * Internal-only service-to-service calls that are not part of any QA surface.

  ### Steps

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

   ### Evidence

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

### Tokens (names-only, App BE pattern)

Exact token names for App BE QA live in App-specific governance/build docs. PF19 recommends patterns such as:

* `APP_BE_ROUTE_200_OK`

* `APP_BE_ERROR_POSTURE_OK`

* `APP_BE_SNAPSHOTS_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

When App BE endpoints proxy HDE surfaces, additional HDE tokens (e.g., `CLI_READER_PARITY_OK`) may apply, but only where those endpoints are explicitly part of HDE integration.

### Failures to watch

* Path or version drift (documented path/version no longer matches implementation).

* Missing or stale snapshots for active endpoints.

* Error responses with unexpected status codes, missing `Content-Type`, or bodies that do not match declared error shapes.

* HDE-adjacent endpoints that:

  * leak HDE internals not meant for the App layer, or

  * diverge from HDE transport posture without clear App-specific policy.

* Evidence artifacts added without corresponding updates to the human index and machine mirror in the same PR.

  ## 5.4 App Frontend

App-specific; this playbook is a **names-only placeholder**. The FE team fills in concrete tools, routes, and thresholds.

### Intent

Prove that the **App Frontend** behaves correctly at a UI level in environments used for QA:

* routing and navigation work as expected

* feature flags and experiments are wired correctly

* basic accessibility and performance are within agreed limits

PF19 does **not** define FE tools or metrics. It only standardizes that FE QA runs produce governed artifacts and that those artifacts are indexed consistently.

### Inputs

* A staging or prod-like FE environment (URL and build identifier).

* The current FE routing and feature flag configuration (by title only).

* Chosen FE QA tools or scripts for:

  * routing sanity checks

  * feature-flag smoke

  * basic accessibility and performance probes

  ### Scope

* **In scope:**

  * UI-level checks for routing sanity, feature flags, core flows, and high level accessibility or performance smoke.

* **Out of scope:**

  * HD Engine routes and bytes (those live in HDE-titled PF docs).

  * Detailed UX specs, design review, or full accessibility audits (these are owned by product and design documents).

  ### Steps

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

   ### Evidence

* FE routing smoke artifacts (for example `artifacts/fe/routing_smoke_<env>.json`).

* Feature flags smoke artifacts (for example `artifacts/fe/feature_flags_smoke_<env>.json`).

* Accessibility and performance smoke artifacts (for example `artifacts/fe/a11y_perf_smoke_<env>.json`).

* Indexed entries in:

  * `docs/evidence/INDEX.json` (+ `.sha256`), and

  * `artifacts/evidence_index.jsonl`,  
     with FE artifacts described by **title only** per PF12.

  ### Tokens (names-only, FE pattern)

Concrete token names for FE QA live in FE governance or build docs. PF19 suggests patterns such as:

* `APP_FE_ROUTING_SMOKE_OK`

* `APP_FE_FEATURE_FLAGS_SMOKE_OK`

* `APP_FE_A11Y_PERF_SMOKE_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

  ### Failures to watch

* Core routes not reachable or redirecting incorrectly in staging or prod-like environments.

* Feature flags enabled but not visible, or disabled but still rendering.

* Smoke accessibility or performance checks failing beyond agreed thresholds.

* FE QA artifacts stored outside governed paths (not under `artifacts/**` or `docs/**`).

* FE QA artifacts added without corresponding updates to the human index and machine mirror in the same PR.

Got it — no code fences, just clean doc-style text you can drop straight into PF19.

Here’s a more coherent, consistently spaced version in the same style you’ve been using:

---

## 5.5 DB & Vendor ingest (authoring plane → DB / sealed pack)

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

### 5.5.1 Steps — A. BE ingest plane (vendor → DB / packs).

1. Run BE vendor ingest.

   * Keys-only logs confirm outbound vendor HTTP and DB writes / pack export.

2. Validate DB/pack outputs (spot-check).

   * Required fields, FKs, pack SHA-256s per PF12.

3. Index BE ingest evidence in the **same PR**.

   * Update human index \+ `.sha256` and machine mirror; governed paths only.

### 5.5.2 Steps — B. HDE as consumer & vendor-capable client.

1. **Source selection (explicit).**

   * Default without `--source=vendor`: use DB/packs if available (no vendor call).

   * With `--source=vendor` (or ops `source="vendor"`): perform live vendor call **only** if rails allow; otherwise return a typed refusal (keys-only).

   * **Pre-App, no-user note.** In the current pre-App posture (no app user IDs, no user-bound BodyGraphs), treat any CLI `--user` value used with `bg:resolve` as an **ephemeral QA key**, not as a real app user ID. Do **not** treat these keys as “users in prod,” and do not use this playbook to create app-like user records.

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

   * **Pre-App, no-user constraint (prod).** In production before the Glow App user model exists:

     * Vendor QA **must not** exercise `bg:resolve --source=vendor --upsert` against prod; any upsert-like flow that would create rows resembling user records is **out of scope** for this playbook and must be owned by a future epic once the app user model is defined in HDE Phased Epics.

     * Vendor QA **may** exercise:

       * closed-rails refusal posture (`--source=vendor` with rails closed → typed refusal, no outbound HTTP), and

       * open-rails `--source=vendor --dry-run` calls that return ingest metadata and **do not write DB rows**.

     * QA must explicitly record any requirement that assumes “existing users in prod” as **blocked by environment** and defer it to a later epic.

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

  ### **5.5.3 Vendor dry-run QA pattern (EPIC017 example)**

For EPIC017, vendor ingest QA followed a **single-command, single-artifact dry-run pattern**:

* One `hdctl bg:resolve --source=vendor --dry-run` call per synthetic birth tuple and QA user key (for example `qa_epic017_vendor1`), run from a Codespace attached to the engine repo with open rails (`ALLOW_NETWORK=1`, `SAFE_MODE=0` as required).

* Each call produced **one resolver+ingest metadata JSON artifact** under `audit/qa/hde-epic017/logs/**` (names-only), which was treated as the primary evidence file for that QA step.

The resolver/ingest metadata for a successful dry-run vendor QA step is expected to show, at minimum:

* **Resolver:** `requested_source="vendor"`, `resolved_source="vendor"`, `allow_network=true`, `safe_mode=false`, `dry_run=true`, `upsert=false`, and `user_id` set to a clearly QA-scoped key (for example `qa_epic017_vendor1`).

* **Ingest:** `provider` (for example `hdapi`), `vendor_version` (version of the vendor schema), a realistic non-zero `duration_ms`, and `rows_written=0`, `db_rows_after=0` for dry-run.

* **Parity & hashing:** `input_fingerprint`, `payload_sha256`, and `db_emitted_sha256` all aligned, with an explicit `parity_match=true` flag indicating that “what came from the vendor” matches “what would be stored in DB shape” under non-dry-run settings.

* **Idempotency:** a composite `idempotency_key` including a UUID, provider, vendor\_version, and the input fingerprint, and a top-level `status="ok"`.

When these conditions are met and the artifact is:

* stored under governed paths (`audit/qa/<epic>/logs/**` and, if normalized, under `artifacts/**` or `docs/**`), and

* properly indexed in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` with a co-located path-proof,

PF19 considers the **vendor dry-run ingest requirement** for that EPIC slice satisfied: QA has proven that vendor ingest can be exercised in dry-run mode from Codespaces into Railway prod, that no DB rows are written, and that payload↔DB shape parity is correctly enforced for that call. Deeper idempotence and multi-run behavior remain the domain of future, more automation-focused epics and CI harnesses.

## 5.6 CLI/API & SDKs

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

**Pre-App compat QA note (CLI-only).**  
 In pre-App, no-user contexts, QA uses `hdctl showcompat` with **explicit** `--source=vendor` and synthetic birth tuples (CLI flags and behavior defined in HDE-CLI-API-Vendor-Ref; titles-only) to validate that the compat engine produces a complete category set and neutral viewer preferences as defined in HDE-Math-Spec and HDE-Schemas & Artifacts (titles-only). The `person_uid` values under `a` and `b` and any `compat.meta` identity fields in this output are treated as **CLI-local identifiers** (local/dev identity for the CLI session), not as Glow App user IDs and not as authoritative prod engine identity (which is governed by the `/internal/version` ops endpoint on Railway by title). Acceptance for this specific QA step is **“compat JSON produced”** for the chosen births; AB↔BA identity, Reader envelope proofs, and vendor ingest evidence are covered by separate QA steps and tokens in this playbook and elsewhere in PF19.

### 5.6.1 Steps

1. **Establish a test pair and environment.**

   * Set env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`) for all captures.

   * In **pre-App, no-user contexts** (no app user IDs, no user-bound BodyGraphs):

     * choose **synthetic birth tuples** and CLI-local person labels as test inputs, and

     * treat any CLI `--user` values used during QA as **ephemeral QA keys**, not as real app user IDs.

   * In environments where the app user model is live and user-bound BodyGraphs exist, test IDs may include real user IDs **only** where those surfaces are explicitly defined by an epic in **HDE Phased Epics** (titles-only).

2. **Source selection (explicitness).**

   * When a DB/packs-backed BodyGraph exists and app user IDs are live:

     * run CLI **without** `--source=vendor` to exercise DB/packs → expect DB read; **no vendor call** in keys-only logs.

   * In **pre-App, no-user contexts** (no DB users / no app user IDs):

     * treat DB-backed, user-ID-dependent flows as **blocked by environment**; do **not** attempt to synthesize app-like user records or rely on `showcompat --user-a/--user-b --source=db` for QA.

     * instead, use **birth-based compat** (`showcompat` with birth arguments only) as the primary compat/Reader surface (see §3.3).

   * With `--source=vendor` (or ops `source="vendor"`):

     * when rails are open, expect a vendor call; if policy allows, results may be stored for durability in non-prod environments;

     * when rails are closed, expect a **typed refusal** (no outbound HTTP).

3. **Capture CLI AB/BA snapshots.**

   * Produce AB and BA governed outputs (JSON or normalized) for a fixed test pair:

     * in pre-App contexts, use **birth-based compat** as the source of truth for these runs;

     * where app users exist and DB-backed flows are in scope, AB/BA runs may also exercise DB/packs, but only under explicit epic guidance.

   * Store artifacts under `artifacts/cli/...`.

4. **Check AB/BA parity.**

   * Verify symmetry where required and correct directional swap semantics (for example, personal vs shared narratives).

5. **Check two-run identity.**

   * Re-run AB and BA; outputs must be byte-identical for governed parts (no RNG/time/FS/network leakage).

6. **Verify emitter parity (CLI ↔ HTTP).**

   * Baseline against HTTP emitter (Reader/Aux) for at least one direction.

   * Verify structural/semantic parity between CLI output and HTTP response (bands, categories, narratives, and meta).

7. **Error parity (typed errors).**

   * Exercise a forced DB-unavailable scenario and a closed-rails vendor attempt.

   * Verify CLI and HTTP error envelopes are aligned (typed, numeric-free) and respect refusal policy.

8. **Update CLI/API evidence indices.**

   * Add/update `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR for all governed CLI/API artifacts.

   * Ensure each mirror record includes a `proof_anchor` to a co-located path-proof.

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

* `artifacts/evidence_index.jsonl`,  
   referencing the above artifacts **by title only** in the human index.

**Tokens (names-only)**

Common tokens that gate CLI/API & SDK QA (definitions live in HDE-Governance / HDE-Build Checklist):

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

* Attempts to satisfy user-ID-dependent QA requirements in environments where **no app user model exists** (pre-App prod); these must be treated as environment-blocked and deferred rather than quietly bypassed.


  ### 5.6.2 Evidence

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

## 5.7 Prod QA playbook for EPIC‑011 (rails window)

**Anchor.** “Prod QA playbook (EPIC‑011 rails window)”

**Purpose.** Define the QA responsibilities around the **short, supervised rails-open window** used to validate EPIC‑011 in prod, using the admin/vendor QA harness.

**Single homes (titles-only)**

* Day‑of runbook: **docs/run/RUN\_PROD\_QA.md**.

* Vendor and DB call contracts: **PF05 — HDE‑CLI‑API‑Vendor‑Ref**.

* DB posture, connectivity, and bridge parity artifacts: **PF12 — HDE‑Schemas & Artifacts**, **PF04 — HDE‑Governance**, **PF09 — HDE‑Build Checklist**.

* SAFE rails policy and tokens: **PF04 — HDE‑Governance**.

### 5.7.1 Rails-open QA window (EPIC‑011)

During EPIC‑011, prod QA uses a **short rails-open window** with these constraints:

* **Closed by default.** Prod and CI run with SAFE rails closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) unless a specific, approved QA job opens them.

* **Narrow, supervised window.** For the prod QA run:

  * a single admin job opens rails for a bounded duration and a fixed test corpus;

  * only the documented Engine/BodyGraph/vendor routes are exercised;

  * no ad‑hoc or exploratory vendor calls are permitted.

* **Immediate return to closed rails.** After the QA run finishes:

  * rails are returned to the closed posture, and

  * refusal and DB connectivity checks are run under closed rails (see below).

QA’s job is to verify that the prod QA window followed this pattern and that evidence for both the rails‑open and rails‑closed runs was captured and indexed.

### 5.7.2 Admin/vendor QA harness (names-only)

The admin/vendor QA harness is implemented (names-only) as:

* `scripts/ops/admin_vendor_qa.py` — a scripted run that:

  * sets deterministic env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`);

  * uses synthetic identities and fixed tuples (see synthetic-identity docs and PF12) to exercise:

    * BodyGraph source selection and invariance,

    * compat math and Reader envelopes (via `showcompat` / Reader),

    * Aux narrative previews,

  * records governed artifacts under `artifacts/**` (for example CLI AB/BA/summary JSON, BodyGraph snapshots, A7 proofs).

The harness must **not** introduce its own retry or backoff policy; vendor SAFE behaviour and retry semantics remain defined only in PF04/PF05.

QA is responsible for:

* confirming that the harness ran with the expected env pins and rails posture;

* checking that the expected governed artifacts were produced and indexed (using the checklists in §9.2 and §9.5); and

* treating missing or extra artifacts as QA failures, not as optional noise.

### 5.7.3 Closed-rails proofs after the window

Immediately after the rails‑open run, QA must ensure that:

* a closed‑rails refusal proof is captured under the path defined in **PF12** (for example `artifacts/proofs/ops_refusal_proof.txt`, titles-only); and

* DB connectivity evidence is captured for prod, matching `DB_CONN_ENV_OK` semantics (presence‑order selection between direct DB and bridge, numeric‑free error on total failure).

Both sets of artifacts must be:

* indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` in the same PR; and

* accompanied by co-located `path_proof.txt` entries.

  # 6\. Catalog/A7 proofs (collected rules; HDE-specific bytes live elsewhere)

HDE-specific. Transport bytes and route contract live in **PF05 — HDE-CLI-API-Vendor-Ref**; policy and tokens in **PF04 — HDE-Governance**; schemas in **PF12 — HDE-Schemas & Artifacts** (titles-only).

## 6.1 Surface

**Surface.** The **only** A7 proof surface is the **Catalog JSON success route**, currently:

* Path: `/reader` (locked initially)

* Env-gate: each environment has a cataloged entry; non-prod entries must not be reachable in prod

`/internal/version` and other ops or Aux endpoints are **not** A7 surfaces.

---

## 6.2 What must be captured

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

  ## 6.3 Composite proof JSON

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

  ## 6.4 Failures to watch

* Missing or non-quoted ETag on GET 200

* HEAD posture diverging from GET (wrong `Content-Type` or `Content-Length`)

* 304 responses that include `Content-Type`, `Content-Length`, or a body

* Missing or incomplete `Vary: Authorization, Accept-Encoding`

* ETag or effective Content-Length changing with encoding

* Composite proof JSON failing PF12 schema validation

* Proof artifacts added without human index \+ mirror updates in the same PR

---

# 7\. BodyGraph refresh & observability QA

**Anchor.** “BodyGraph refresh & observability QA”

**Purpose.** Make the BodyGraph evidence and privacy guarantees testable, using the governed artifacts defined in PF12.

**Single homes (titles-only)**

* BodyGraph schemas and artifacts: **PF12 — HDE‑Schemas & Artifacts**.

* Vendor SAFE and BodyGraph source selection rules: **PF04 — HDE‑Governance**, **PF05 — HDE‑CLI‑API‑Vendor‑Ref**.

* Metrics and logs privacy posture: **PF04 — HDE‑Governance**.

## 7.1 Evidence artifacts (BodyGraph)

QA expects the following governed artifacts (paths are normative; schema lives in PF12):

* `artifacts/bodygraph/source_selection.snapshot.json`

* `artifacts/bodygraph/source_invariance/ab.json`

* `artifacts/bodygraph/source_invariance/ba.json`

* `artifacts/bodygraph/source_invariance/summary.json`

* `artifacts/bodygraph/refresh_policy.snapshot.json`

* `artifacts/bodygraph/metrics.snapshot.json`

* `artifacts/bodygraph/keys_only.logs.sample`

Each artifact must be indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` with a co-located `path_proof.txt` (see §4.3 and §9.2).

## 7.2 Refresh policy QA

For **refresh\_policy.snapshot.json**, QA must ensure that:

* the refresh worker (or equivalent job) has been run long enough in the target environment to populate non-trivial `sample_counts` (PF12 defines exact fields and semantics);

* the snapshot corresponds to the same release and BodyGraph configuration that will ship; and

* any change to refresh policy logic or thresholds is accompanied by a new snapshot and a new Mirror record in the same PR.

QA treats a zeroed or obviously stale `sample_counts` field as a failure to meet refresh-policy QA, not as a cosmetic issue.

## 7.3 Observability and privacy QA

For `metrics.snapshot.json` and `keys_only.logs.sample`, QA must:

* verify that metrics cover the BodyGraph flows exercised during QA (names and labels as defined in PF12/PF04);

* confirm that:

  * logs are **keys-only** (no raw birth data, no payload bodies, no secrets);

  * metrics and logs do not contain PII or secret values; and

  * labels are bounded and match the expected dimensions (for example `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`).

If any privacy or labeling violations are found, QA blocks the release until the logging/metrics configuration is corrected and new snapshots are captured and indexed.

---

**Acceptance / artifact impact**

* PF19 now codifies QA expectations around the BodyGraph artifacts already defined in PF12:

  * `artifacts/bodygraph/source_selection.snapshot.json`

  * `artifacts/bodygraph/source_invariance/*.json`

  * `artifacts/bodygraph/refresh_policy.snapshot.json`

  * `artifacts/bodygraph/metrics.snapshot.json`

  * `artifacts/bodygraph/keys_only.logs.sample`

* Tokens such as `BG_SOURCE_SELECTION_OK`, `BG_SOURCE_INVARIANCE_OK`, `BG_TTL_SWR_OK`, `BG_PRIVACY_OK`, `BG_METRICS_OK` remain defined in PF04/PF12; PF19 just grounds how QA should interpret them.

  # 8\. Evidence & indexing reference (quick rules)

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

* **`mtime_utc` semantics (names-only).**

  * Where Mechanics and PF12 schemas use `mtime_utc` in path-proof transcripts or evidence records, QA checks **MUST** treat it as an informational timestamp that is:

    * a valid UTC timestamp with seconds precision and zero microseconds, and

    * **monotone vs filesystem `stat()`** (not later than the current filesystem modification time, and non-decreasing across evidence refreshes).

  * QA **MUST NOT** treat exact equality between `mtime_utc` and `stat().st_mtime` as the acceptance condition; the canonical acceptance criteria remain **hash and size matching** between artifact, Mirror record, and the path-proof’s single `sha256`/`size_bytes` pair (see PF12).

  * Any future change to `mtime_utc` behavior (for example, adopting a different refresh-time policy) **MUST** be reflected in both the evidence tools and their tests before QA can accept new behavior.

---

# 9\. Tokens glossary (names-only; sources in PF04/PF09)

PF19 lists names only. Token spellings and normative definitions live in **PF04 — HDE-Governance** and **PF09 — HDE-Build Checklist**.

**Pre-commit**

* `QA_PRECOMMIT_CHECKLIST_OK`

* `DET_SERIALIZER_OK`

* `TWO_RUN_IDENTITY_OK`

* `AB_BA_IDENTITY_OK`

**Post-commit (general)**

**`Post-commit (general)`**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `EVIDENCE_PATH_PROOFS_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`

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

## 9A. QA Acceptance Tokens Registry (canonical QA token library)

### 9A.1 Intent

This registry is the **single QA-level home** for acceptance tokens used across Engine, App, CI, transport, and evidence proofs.  
 PF19 does **not** redefine transport bytes, schemas, or governance semantics; those remain in their single homes (PF04/PF05/PF12/PF09).  
 This registry provides QA-oriented token descriptions: **scope**, **owner PF doc**, **high-level definition**, and **evidence required for satisfaction**.

### 9A.2 Token metadata model (normative)

Each QA acceptance token in this registry includes:

* **Name** — canonical spelling of the token (source of truth).

* **Owner PF (titles-only)** — the PF document that holds the normative semantics (PF04, PF09, PF12, PF05, PF17, PF20).

* **Scope** — pre-commit, post-commit/live QA, evidence, transport/A7, App-layer, or multi-scope.

* **QA definition (1–3 sentences)** — what QA must prove for the token to be satisfied.

* **Evidence mapping** — the governed artifacts and checks required for satisfaction (titles-only).

This metadata model is authoritative for QA planning and EPIC acceptance.

---

### 9A.3 Pre-commit / CI QA tokens

QA\_PRECOMMIT\_CHECKLIST\_OK

*Owner PF:* PF09 — HDE-Build Checklist  
 *Scope:* Pre-commit  
 *QA definition:* All required pre-commit checks (lint/format, canonical JSON/JSONL, determinism, env pins, mirror quick-check) have passed.  
 *Evidence:* CI logs, updated governed artifacts under PF09 pre-commit harness.

DET\_SERIALIZER\_OK

*Owner PF:* PF14  
 *Scope:* Pre-commit  
 *QA definition:* Engine serializer/composer emits byte-stable canonical JSON under env pins.  
 *Evidence:* Two-run identity proofs; AB/BA parity where applicable.

TWO\_RUN\_IDENTITY\_OK

*Owner PF:* PF09/PF14  
 *Scope:* Pre-commit  
 *QA definition:* Re-running the same CLI/API/engine invocation yields identical governed bytes.  
 *Evidence:* Paired canonical JSON artifacts stored under `artifacts/**` with mirror/Index entries.

AB\_BA\_IDENTITY\_OK

*Owner PF:* PF09/PF14  
 *Scope:* Pre-commit  
 *QA definition:* AB and BA runs swap attributes correctly with no structural drift.  
 *Evidence:* `compat_ab.json` and `compat_ba.json` with identical non-directional fields; path-proofs \+ mirror records.

---

### 9A.4 Evidence skeleton tokens

EVIDENCE\_INDEX\_UPDATED\_OK

*Owner PF:* PF09/PF12  
 *Scope:* Pre-commit & post-commit  
 *QA definition:* Any evidence change is accompanied by same-PR updates to the Human Index and Machine Mirror.  
 *Evidence:* Updated `docs/evidence/INDEX.json`, `.sha256`, and `artifacts/evidence_index.jsonl` \+ path-proofs.

EVIDENCE\_PATHS\_VALIDATED\_OK

*Owner PF:* PF12  
 *Scope:* Evidence  
 *QA definition:* All governed artifacts have valid path-proofs with matching sha256/size and monotone `mtime_utc`.  
 *Evidence:* Path-proof files and mirror schema quick-check logs.

CI\_CHECK\_MIRROR\_SCHEMA\_OK

*Owner PF:* PF12/PF09  
 *Scope:* Evidence  
 *QA definition:* Machine mirror conforms to schema: pinned field order, one LF per record, unknown-key reject.  
 *Evidence:* CI mirror-schema verification artifacts.

CI\_CHECK\_FINAL\_LF\_OK

*Owner PF:* PF09  
 *Scope:* Pre-commit / Evidence  
 *QA definition:* All governed text artifacts end with exactly one LF.  
 *Evidence:* CI logs or dedicated LF-check harness results.

---

### 9A.5 Transport / A7 tokens

A7\_GET\_QUOTED\_ETAG\_OK

*Owner PF:* PF04/PF05  
 *Scope:* Post-commit / A7  
 *QA definition:* GET 200 for the Catalog JSON success route returns a strong, quoted ETag derived from the LF-terminated body.  
 *Evidence:* A7 GET header snapshot, composite proof JSON.

A7\_HEAD\_PARITY\_OK

*Owner PF:* PF04/PF05  
 *Scope:* A7  
 *QA definition:* HEAD 200 mirrors validators and `Content-Type`; `Content-Length` equals identity body length.  
 *Evidence:* HEAD header snapshot \+ composite proof JSON.

A7\_304\_OMITS\_CT\_CL\_OK

*Owner PF:* PF04/PF05  
 *Scope:* A7  
 *QA definition:* 304 responses omit both `Content-Type` and `Content-Length` and contain no body.  
 *Evidence:* 304 header snapshot \+ composite proof.

A7\_ENCODING\_INVARIANCE\_OK

*Owner PF:* PF04/PF05  
 *Scope:* A7  
 *QA definition:* ETag and effective body semantics remain stable across accepted encodings.  
 *Evidence:* A7 proof JSON \+ encoding tests.

---

### 9A.6 Aux & narrative tokens

NARR\_200\_TEXT\_OK

*Owner PF:* PF17  
 *Scope:* Post-commit  
 *QA definition:* Aux text responses produce LF-terminated bodies and a strong, quoted ETag.  
 *Evidence:* `aux_text_200.snap` \+ Index/Mirror updates.

NARR\_SUPPRESSED\_NO\_ETAG\_OK

*Owner PF:* PF17  
 *Scope:* Post-commit  
 *QA definition:* Suppressed narrative responses return 200 with **empty body** and **no ETag**.  
 *Evidence:* `aux_suppression_200.snap`.

COMPOSE\_IDS\_DETERMINISM\_OK

*Owner PF:* PF17  
 *Scope:* Determinism  
 *QA definition:* Composition IDs/keys remain stable across repeated Aux text runs.  
 *Evidence:* Paired Aux snapshots \+ mirror records.

---

### 9A.7 CLI/API & SDK tokens

CLI\_SHOWCOMPAT\_CANON\_OK

*Owner PF:* PF05/PF14  
 *Scope:* Pre-commit & post-commit  
 *QA definition:* `showcompat` emits canonical JSON with env pins, independent of user IDs in pre-App environments.  
 *Evidence:* CLI `compat_*.json`, path-proofs, mirror entries.

CLI\_READER\_EMITTER\_PARITY\_OK

*Owner PF:* PF05  
 *Scope:* Parity  
 *QA definition:* CLI Reader previews match HTTP Reader emitter bytes exactly.  
 *Evidence:* CLI snapshot \+ HTTP baseline.

CLI\_STDOUT\_LF\_OK

*Owner PF:* PF05/PF09  
 *Scope:* Determinism  
 *QA definition:* All governed CLI stdout surfaces end with exactly one LF.  
 *Evidence:* CLI stdout snapshot; LF check.

SDK\_READER\_PARITY\_OK

*Owner PF:* PF05  
 *Scope:* SDK parity  
 *QA definition:* SDK Reader calls mirror HTTP Reader emitter bytes.  
 *Evidence:* SDK artifacts \+ HTTP baseline.

---

### 9A.8 App-layer QA tokens

*(Names-only; definitions live in App QA governance docs.)*

* `APP_FE_ROUTING_SMOKE_OK`

* `APP_BE_ROUTE_200_OK`

* `APP_SEC_ASVS_MIN_OK`

---

### 9A.9 EPIC → Token mapping (QA routing rule)

For every EPIC in **HDE Phased Epics** (titles-only), the EPIC acceptance roster must:

1. List required QA tokens **by canonical name** from this registry;

2. Must not redefine or override token semantics;

3. Provide evidence pointers (titles-only) showing how the EPIC satisfies each token.

---

### 9A.10 Forward plan

Addendum 12 identifies missing work:

* Extract EPIC017 QA tokens into this registry;

* Backfill definitions and evidence mapping for any missing canonical tokens;

* Update PF20 so EPIC017 points to this registry rather than listing tokens ad-hoc.

This registry is now the single QA-level home for QA acceptance tokens going forward.

---

# 10\. Templates & harnesses (to be filled; titles-only anchors)

This section names the standard QA templates and harnesses. Concrete formats, scripts, and CI wiring live in **PF09 — HDE-Build Checklist** and **PF12 — HDE-Schemas & Artifacts** (titles-only).

## 10.1 Pre-commit checklist (CI job stub)

**Anchor.** “Pre-commit QA checklist (PF09 CI stub)”  
 **Purpose.** A copyable block that teams can drop into their CI config to enforce:

* lint \+ format

* JSON/JSONL canonicalization and final-LF checks

* deterministic, no-I/O tests

* snapshot hygiene and env pins

**Notes.**  
 PF19 defines the required items; PF09 provides the actual CI job template and examples.

---

## 10.2 Post-commit capture checklist (headers \+ index)

**Anchor.** “Post-commit evidence capture checklist”  
 **Purpose.** A step-by-step recipe to:

* capture headers/body snapshots (Text, Suppressed, A7 surfaces)

* generate composite proof JSON (when A7 is in scope)

* update `docs/evidence/INDEX.json` \+ `.sha256` and `artifacts/evidence_index.jsonl` **in the same PR**

* **Governed locations only.** All indexed artifacts **must** live under `artifacts/**` or `docs/**`. Transient/generator paths are **forbidden** as sources for indexed evidence. ← **added**

* normalize header names to lower-case before persisting governed snapshots  
* For each new or changed governed artifact under `docs/**` or `artifacts/**`:

  * create or update a co-located `path_proof.txt` file, and

  * ensure there is exactly one Mirror record whose `proof_anchor` points at that `path_proof.txt`.

* Treat “artifact present but no path\_proof” or “path\_proof present but no Mirror record” as **QA failures**, not as minor hygiene issues.

* For lifecycle and OPS‑managed artifacts (for example backup/restore probes), confirm that the associated evidence changes (artifact \+ path\_proof \+ Mirror) land in the **same PR** as the code or configuration change they support.

---

## 10.3 Validated-tuple QA harness (Aux & CLI parity)

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

## 10.4 A7 proof capture recipe

**Anchor.** “A7 proof capture recipe (Catalog /reader)”  
 **Purpose.** A reusable recipe that:

* captures GET/HEAD/304 headers for the Catalog JSON success route

* verifies strong quoted ETag, Vary, and encoding invariance

* captures env-gate proof (non-prod entries unreachable in prod)

* builds and validates composite A7 proof JSON against PF12 schema

**Preconditions (merge gate).**

Before capturing any A7 proofs, the harness must:

* verify that `docs/ENDPOINTS_CATALOG.json` exists and that the Reader JSON success route is present and marked as a Catalog JSON surface; and

* abort with a clear QA failure if the Catalog entry is missing or invalid (no partial A7 runs).

After capturing proofs, the harness must:

* update `docs/evidence/INDEX.json` \+ `.sha256` and `artifacts/evidence_index.jsonl` in the same PR, and

* run the mirror quick-check (§9.5). Failure to index or mirror any A7 artifact means the A7 gate is **not satisfied**, and no A7 tokens may be claimed for that PR.

---

## 10.5 Mirror schema quick-check

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

# 11\. Roles & RACI (QA)

## 11.1 QA roles (titles-only pointer to PF06)

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

  ## 11.2 Component ownership

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

  # 12\. Change control

  ## 12.1 Living document

* PF19 is a living QA guide.

* References to **PF10 — HDE-Build Notes** must always be **by title only** (no version numbers, no inlined content).

* When a PF10 item is “drained” into a canonical PF doc (for example PF04, PF09, PF12, etc.), PF19 must be updated to:

  * point at the new canonical home by title, and

  * remove or rewrite any stale notes that referenced the interim PF10 guidance.

* Apply **PF03 — Technical Writing Best Practices** discipline:

  * keep a single home for each rule,

  * avoid duplicating bytes/schemas/tokens,

  * use clear, minimal redlines when updating PF19.

    ## 12.2 Supersession rule (PF10 addenda)

* PF10 addenda are ordered. When multiple PF10 addenda address the same topic, the newer addendum supersedes the earlier.

* If PF10 addenda conflict, PF19 must follow the later addendum until that guidance is drained into canon.

* When updating PF19:

  * consult PF10 in addendum order,

  * resolve conflicts in favor of the latest addendum,

  * then route long-term rules to their canonical PF homes (PF04/PF09/PF12/… by title only).

When PF10 addenda reference QA acceptance tokens, their canonical definitions now live in **§9A — QA Acceptance Tokens Registry**. PF19 must route all PF10 token references to §9A and must not redefine token semantics locally.

# 13\. EPIC QA History

## 13.1 **HDE-EPIC011 — Vendor Ingest & Data Durability *(failed; historical QA posture only)***

**Status.** HDE-EPIC011 is recorded as a **failed epic**. Its acceptance roster (DB posture, ingest idempotence, evidence discipline, partition plan, SAFE rails, BodyGraph invariance) never reached a fully green, production-ready state, and the epic is not shippable under the original map.

**Preservation surfaces.** Under this epic, the following areas are treated as **preservation surfaces**:

* CLI transport and compat contracts defined in the HDE PF docs (no new compat or CLI contract changes land under this epic).

* Vendor ingest and retry/backoff contracts as defined in HDE Epics Map and HDE-CLI-API-Vendor-Ref.

* Compat math and Aux narrative surfaces as defined in HDE-Math-Spec and HDE Narratives Guide.

* BodyGraph observability and evidence discipline as defined in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

EPIC011 may add durability and evidence around these surfaces but **MUST NOT** change their public contracts; any change to those contracts must be owned by the single-home PF docs.

**QA posture.** QA treats:

* the EPIC011 evidence and build notes preserved in HDE-Build Notes as **historical record**, and

* any remaining work as **recorded debt** to be absorbed by future epics defined in **HDE Phased Epics**, not as open EPIC011 acceptance.

New QA epics that revisit EPIC011’s topics (for example, PK refinement, partition strategy, A7/Catalog extensions) **must be defined in HDE Phased Epics** with fresh acceptance rosters and tokens. PF19 references EPIC011 only to describe historical QA posture, not to define current acceptance criteria.

## **13.2 HDE-EPIC017 — Live QA summary (Codespaces → Railway)**

**Status.**  
 HDE-EPIC017 combines repo-level foundations (ordering, evidence skeleton, registry, manifest, close-out) with a focused Live QA pass from Codespaces into Railway prod. Live QA is **not** a replacement for CI; it demonstrates prod behavior of key Engine surfaces under the EPIC017 Live QA pattern (§3.4).

**Prod surfaces covered (Live QA evidence).**

EPIC017 has explicit Live QA evidence (Codespaces → Railway) for the following:

* **Ops identity endpoint `/internal/version` (Railway).**

  * GET, HEAD, and conditional GET (with `If-*` headers) all return `200 OK` with:

    * `Cache-Control: no-store`,

    * JSON `Content-Type`,

    * **no** `ETag` or `Last-Modified`, and

  * a stable body across GET/HEAD/conditional GET.

  * This proves transport, header, and conditional behavior for `/internal/version` in prod; body contract compliance remains separate (see “Known gaps”).

* **CLI availability and surfaces (Codespaces).**

  * `hdctl` is on PATH in the Codespace and exposes the expected commands (at least `showcompat`, `aux-preview`, `bg:resolve`).

  * CLI `--help` runs successfully and matches the surfaces assumed in EPIC017 QA plans.

* **Compat via CLI from births (vendor source).**

  * `hdctl showcompat --source=vendor` with synthetic birth tuples produces compat JSON with:

    * 10 Magic-10 categories, each with id/band/score and template keys, and

    * neutral viewer preferences and CLI-local meta (for example `engine_tag="hdengine-dev"`, `invocation_tag="INV-LOCAL"`, zeroed `release_id`).

  * Both AB and BA invocations yield complete compat payloads; JSON comparison and strict AB↔BA identity are primarily handled by repo-level harnesses, not manual Live QA.

* **Reader v1 envelope via CLI.**

  * `hdctl showcompat --source=vendor --dump-reader` for the same pair produces a Reader v1 envelope with the expected set of fields (titles-only, see HDE-Math-Spec and HDE-CLI-API-Vendor-Ref), harmony-only, numeric-free categories, and well-formed hashes, using CLI-local identity values.

* **Aux narratives and admin preview.**

  * `hdctl aux-preview --show-narrative` emits a short, present-tense, numeric-free narrative that matches Aux public tonality expectations.

  * `hdctl aux-preview --admin-out` emits a minimal admin JSON sidecar with:

    * composition identifiers and keys,

    * narratives pack SHA, and

    * CLI-local release/identity values,

  * aligned with the compat person IDs for the pair.

* **Vendor ingest via resolver dry-run.**

  * `hdctl bg:resolve --source=vendor --dry-run` with a synthetic birth tuple and QA user key (for example `qa_epic017_vendor1`) shows:

    * resolver selecting `source="vendor"` with open rails, `dry_run=true`, `upsert=false`, and QA-scoped `user_id`;

    * ingest using provider `hdapi` with a non-zero `duration_ms`;

    * `rows_written=0`, `db_rows_after=0`;

    * matching `input_fingerprint`, `payload_sha256`, `db_emitted_sha256` and `parity_match=true`;

    * a composite `idempotency_key` and `status="ok"`.

  * This proves that vendor ingest can be exercised in dry-run mode from Codespaces into Railway prod without mutating DB state, consistent with §5.5.3.

