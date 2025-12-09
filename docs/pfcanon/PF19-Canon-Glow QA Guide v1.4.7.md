# **0\. Front Matter**

## **0.1 Header**

**Title:** PF19-Canon-Glow QA Guide

**Status:** Canon

**Version:** 1.4.7

**Effective date:** 2025-12-08

**Last Update Gate:** HDE-EPIC020 Dev Retro

**Invocation tag:** INV-f2ac55d77ce9aacc

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

**Reality Audits vs QA tokens (titles-only).**  
 PF19 treats **Reality Audits** as a **separate axis** from QA token semantics. Reality Audits (as defined in **Reality Audits**) are PO-only, post-epic architecture reviews that may be **in scope** or **out of scope** for a given epic or implementation plan. Decisions to run, skip, narrow, or broaden a Reality Audit for a specific epic:

* do **not** add, remove, or weaken any QA Acceptance Tokens in this guide;

* do **not** change which QA tokens exist in the PF19 registry, how they are named, or what evidence they require; and

* do **not** change the requirement that epic acceptance maps and manifests bind tokens to governed evidence families as described in §9.2.12.

PF23 scope choices are local to a plan or epic and must be recorded there (for example in **HDE Phased Epics** or **HDE-Build Notes** by title). PF19’s QA tokens and their governance rules remain global and unaffected by per-epic Reality Audit decisions.

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

  ### **0.4.3 Core principles (names-only)**

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

* **Agent-readable evidence ledger (text-based).**

  Baseline HD Engine evidence **MUST** be inspectable via text artifacts at the PR level, suitable for review by humans and Codex/ChatGPT-class agents. In practice, this means that the primary evidence ledger for HD Engine acceptance is always expressed through plain-text artifacts under governed paths (`docs/**`, `artifacts/**`, `audit/**`), such as the Human Evidence Index, the Machine Mirror, bundle manifests, and key QA logs and step transcripts. Binary or compressed bundles may exist as supplementary artifacts, but they **MUST NOT** be the only governed evidence for any acceptance token that requires payload inspection by an agent. Pure contract/token-only families (for example “status-only” or hash-only proofs) are acceptable **only** when the evidence consumer does not need to inspect payload content; otherwise they **MUST** be paired with at least one governed text artifact (for example a bundle manifest, QA log, or summary) that exposes the relevant payloads at the evidence ledger level. Titles and schemas for these artifacts remain in **HDE-Schemas & Artifacts**, **HDE-Build Checklist**, and related PF docs.

* **Mechanical Live QA evidence; narrative belongs in PF10/PF20.**  
   Live QA and bootstrap evidence **MUST** be mechanical wherever possible: logs, JSON, exit codes, tree/env snapshots, and scripted notes (for example via `echo`) written under `audit/qa/<epic-id>/…`, not hand-edited by the PO in editors. POs are expected to run commands and produce mechanical artifacts; **they are not expected to write prose summaries** as part of acceptance. Narrative QA addenda and synthesis (for example EPIC QA reviews, build-note summaries, PF20 closeouts) are authored by QA personas and Leads in **PF10 — HDE-Build Notes** and **HDE Phased Epics** (titles-only), not in Live QA notes files.

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

## **1.3 HD Engine layer (HDE-only)**

HDE PF docs apply **only** to the Engine’s surfaces and their direct callers: **Catalog/Reader JSON success** (A7 surface), **Aux narrative text** (non-A7), **CLI admin preview** using the **same emitter**, and **admin bundle surfaces** (CLI and HTTP) that package the full product payload for a single match. Admin bundle surfaces are **admin-only**, explicitly **non-A7**, and are routed by PF19 to Governance, CLI/API, Mechanics, and Schemas & Artifacts by title only. App FE/BE are **out of scope** for HDE policy except where App endpoints **proxy HDE**; in those cases they must preserve HDE contracts.

* **HD Engine service (Reader, Aux, admin bundle HTTP route via BE).**  
   Core Engine HTTP surfaces, exposed to the App BE as internal services (Reader JSON, Aux narrative text, and the admin bundle HTTP route).

  * Implementation and deploy: engine service on Railway prod (names-only, see Glow Infrastructure).

  * Transport bytes and public routes (including the admin bundle HTTP route): **HDE-CLI-API-Vendor-Ref**.

  * Architecture and boundaries (including separation of Catalog/Reader, Aux, admin-only routes, and ops endpoints): **HDE Architecture**.

  * Governance, A7 policy, and admin-surface auth/logging posture: **HDE-Governance**.

  * Admin bundle builder mechanics and use of the canonical serializer/emitter: **HDE-Mechanics Guide** and **HDE-Schemas & Artifacts**.

  * All other Engine details: HDE-titled PF docs by title only.

  * **Epics map (historical vs current).**  
     For HD Engine epics, **HDE Epics Map** is **historical-only**; it records past epic allocations, including **HDE-EPIC011** as a failed epic and **HDE-EPIC012–HDE-EPIC014** as “won’t do”. The current source of truth for epic planning, phase mapping, and epic-level acceptance rosters is **HDE Phased Epics**. QA must:

    * treat any epic references in HDE Epics Map as **historical context only**, and

    * route new epic-level QA decisions and open work to **HDE Phased Epics**, not to HDE Epics Map.

* **Admin bundle CLI surface (admin-only).**  
   CLI entrypoint that calls the admin bundle builder and returns the full product payload for a single match as a single canonical JSON object.

  * Implementation: CLI admin-bundle subcommand (name and flags pinned in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide).

  * Target environment: Railway HD Engine prod service and DB, configured via infra canon (titles-only).

  * Governance and auth: HDE-Governance (admin token or equivalent credential required; numeric-bearing content remains admin-only and outside the Reader public covenant).

  * QA playbooks and tokens: this guide (PF19) and HDE-Build Checklist (titles-only).

* **HD Engine integration in App BE.**  
   Backend endpoints that call HDE are responsible for preserving HDE contracts at the integration boundary.

  * HDE contracts: defined only in HDE-titled PF docs (titles-only, no duplication).

  * App BE wrapping behavior: defined in backend API docs; PF19 treats it as part of App BE QA with additional checks that HDE contracts, including admin-only boundaries, are honored.

---

## **1.4 Shared tools and evidence system**

These pieces are cross-cutting. Some are HDE-specific in terms of contract, but they affect how QA is done across projects.

* **CLI/API and SDKs (dev tools).**  
   Developer-facing tools that exercise the Engine and App. QA focuses on parity with emitters and deterministic behavior.

  * Implementation: CLI and SDK repos (names-only).

  * Transport and CLI contracts for HDE flows: **PF05 — HDE-CLI-API-Vendor-Ref**.

  * For App-only tools, contracts live in app-specific docs; HDE PF docs only apply when the tool calls HDE.

  * For CLI/API & SDKs, PF19 treats **two equivalent QA surfaces**:

    * a Codespace attached to the engine repo acting as a **QA console**, and

    * any other terminal or shell that is configured (by infra canon) to reach the HD Engine prod service and DB on Railway.

  * Both surfaces are governed by the same CLI/API contracts (titles-only) and QA tokens; plans must not assume that CLI QA is restricted to Codespaces only when other terminals can reach the canonical Railway endpoints defined in infra canon.

* **Internal/dev HTTP harnesses (e.g. `/internal/dev/sampler`).**  
   Dev-only HTTP routes exposed by the Reader/adapter for internal QA or evidence flows (for example `POST /internal/dev/sampler` for sampler behavior).

  * Implementation and wiring (start commands, ports, host binding) live in infra-facing docs such as **Glow Infrastructure** and **HDE-Mechanics Guide** (internal/dev surfaces sections, titles-only).

  * Transport behavior and internal/dev HTTP semantics (JSON shape, writer-style error envelopes, headers such as `Cache-Control: no-store` and “no ETag” posture) live in **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide** (titles-only). PF19 does not restate these bytes; it only routes QA to them.

  * **Infra/ops ownership.**  
     For any internal/dev HTTP harness intended for QA or evidence:

    * Infra/ops **MUST** provide and own:

      * a canonical dev start command or service definition that runs the Reader process in dev/Codespaces with `APP_ENV=dev` (and any determinism rails required by Mechanics); and

      * a corresponding base URL and port per environment (for example Codespaces vs local dev), from which concrete URLs such as `DEV_SAMPLER_URL=http://127.0.0.1:<port>/internal/dev/sampler` can be derived.

    * These URLs **MUST NOT** be guessed by PO, QA, or doc agents. They **MUST** be derived from the actual Reader process wiring (ports and host binding) as configured by infra and captured in infra canon.

    * Before handing any dev harness URL to QA (for curl, scripts, or external tools), Infra/ops **MUST** validate it locally with a simple HTTP/1.1 JSON POST under appropriate rails (at minimum `APP_ENV=dev` and, where feasible, determinism env pins) and confirm that the response shape and headers match the internal/dev HTTP behavior specified by the owning PF docs (titles-only).

  * **QA consumption rule.**  
     QA and PO agents:

    * **MAY** consume infra-provided dev harness URLs in QA plans, scripts, and Live QA steps; but

    * **MUST NOT** define or change those URLs themselves. If a dev harness URL or start command is missing or unclear, QA must treat that as a **spec/infra gap** (see §11.3 canon-first rule), mark affected steps as **blocked by infra wiring**, and request an infra update rather than guessing ports or paths.

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

## **2.2 Checklist (to be instantiated in PF09 CI)**

### **2.2.1 Lint and format**

* Pre-commit pipelines **SHOULD** run language-appropriate linters/formatters and fail on style or syntax issues.

  ### **2.2.2 JSON/JSONL canonicalization and final-LF checks**

* Enforce canonical form for governed JSON/JSONL files.

* Require exactly **one** trailing linefeed on governed text artifacts.

* Reject non-canonical or mixed-style JSON in governed paths.

  ### **2.2.3 Deterministic, no-I/O unit tests**

* Pure paths **MUST NOT** depend on RNG, wall-clock time, external network, or filesystem state.

* Tests **SHOULD** prove two-run identity where applicable (same inputs → same outputs/bytes).

  ### **2.2.4 Env pins for snapshot generation**

* For any job that produces snapshots or evidence, export:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

* This applies to Engine, App, and shared tools whenever they emit governed artifacts.

  ### **2.2.5 Tooling vs behavior failures (pytest and harnesses)**

* QA plans and CI logs **MUST** distinguish **tooling failures** (for example, missing or non-executable test entrypoints such as `.venv/bin/pytest`) from **application/behavior failures** (for example, ingest tests failing assertions). A failure where the test harness cannot even start (for example, “cannot execute: required file not found” when invoking `.venv/bin/pytest`) **MUST** be classified and recorded as an environment/tooling defect, not as a red behavior verdict for the suite under test.

* In Codespaces and similar venv-based environments, the preferred invocation pattern for QA and CI is:

  * activate the venv (for example `source .venv/bin/activate`), and

  * run tests via `python -m pytest …` rather than relying on a wrapper script in `.venv/bin/pytest`.

* QA plans **SHOULD** use `python -m pytest` in copy/paste-ready commands for test-driven steps (including ingest tests), and PF09 CI harnesses **SHOULD** mirror this pattern where practical.

* When a tooling failure is encountered (for example `.venv/bin/pytest` is broken but `python -m pytest` succeeds):

  * the failure **MUST** be captured mechanically in a QA log under `audit/qa/<epic-id>/…` with a clear label (for example a `D0-...` or `D2-...` log entry noting “tooling failure: pytest shim unusable; rerun with python \-m pytest”);

  * the suite **MUST** be re-run once a working invocation (`python -m pytest …`) is available under the same intended rails (`SAFE_MODE`, `ALLOW_NETWORK`, env pins); and

  * only the rerun outcome (pass/fail under correct tooling and rails) is used to judge the behavior of the tests and to satisfy behavior tokens such as `TESTS_PASS_OK`. Tooling failures that are successfully bypassed via the canonical `python -m pytest` pattern **must not** be treated as ingest/behavior failures.

* If neither `.venv/bin/pytest` nor `python -m pytest` can run the required tests (for example pytest is not importable or the venv is missing), the affected checklist items and tokens (for example ingest-related DISS tasks) are considered **blocked by tooling** under PF19/PF09/PF07 until the environment is fixed. QA must record this as a tooling blocker (not as a red behavior verdict) and resolve the infra/venv issue before treating the underlying tests as truly failing.

  ### **2.2.6 Rails posture in CI (default CLOSED)**

* Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default.

* If any pre-commit job opens rails (network I/O), it **MUST** produce governed evidence and index it in the same PR (titles-only routing to PF12/PF09).

  ### **2.2.7 Machine mirror quick-check (includes path-proofs)**

* Verify `artifacts/evidence_index.jsonl` exists and is the **only** mirror file; records are canonical JSONL (sorted keys, one LF, unknown-key reject, pinned field order).

* Verify each record’s `proof_anchor` points to an adjacent stored path-proof; fail CI if any proof is missing.

* Enforce “governed paths only”: all indexed artifacts must live under `artifacts/**` or `docs/**`.

  ### **2.2.8 Snapshot hygiene (tolerant vs strict)**

* Classify snapshots as **strict** (must match exactly) or **tolerant** (pattern-based).

* Pin patterns where applicable (for example text posture harnesses; see §6.2 harness).

* Fail if strict snapshots drift unexpectedly.

  ### **2.2.9 Keys-only logs in tests**

* When tests exercise logging, ensure logs are **keys-only** and contain no payload bodies or secrets.

* Logging policy and redaction rules live in HDE-Governance; PF19 only requires that tests respect them.

  ### **2.2.10 Drift / schema enforcement for governed artifacts**

* Treat each of the following as a CI failure for governed artifacts:

  * unknown keys in the machine Mirror;

  * non-canonical snapshots under governed paths;

  * missing trailing LF on governed text.

* Schema and gate definitions live in HDE-Schemas & Artifacts and HDE-Build Checklist; PF19 requires CI to enforce them.

  ### **2.2.11 Evidence-governed CI sequence (names-only)**

For PRs that change governed evidence artifacts (Index, Mirror, ordering artifacts, path-proofs, orientation demo), the pre-commit/CI pipeline **SHOULD** follow this sequence under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`):

1. **Generate ordering artifacts (write, then check, when in scope).**

   * Run the ordering generator once in write mode (no `--check`) to refresh ordering artifacts in `artifacts/engine/order/**` from the current sources (catalogs, manifests, and Engine math).

   * Then run the same generator again with its `--check` mode (see HDE-Mechanics Guide) to prove two-run identity: a second run over an unchanged tree produces no changes to the ordering artifacts.

2. **Update Evidence Index and Mirror (write, then check).**

   * Run the Evidence Index/Mirror tool once in write mode to rewrite `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and all governed `*.path_proof.txt` from the current artifact set (single source of truth).

   * Then run the same tool again with `--check` to confirm that a second run is a no-op (no unindexed or dangling artifacts, no missing proofs, no schema violations).

3. **Run topology orientation checks.**

   * Run the orientation demo tool with `--check` to validate that `audit/gates/topology/orientation_demo.txt` is coherent with the current Index/Mirror state and not stale.

4. **Enforce Mirror schema and path-proof discipline.**

   * Run the Mirror-schema quick-check (see §10.5) to validate field set/order, canonical JSONL form, single Mirror file, and `proof_anchor` alignment with `*.path_proof.txt`.

5. **Run ordering/evidence test suites.**

   * Run the pytest suites that cover ordering properties and evidence skeleton behavior (titles-only); treat any failure as a CI failure for governed artifacts.

PF19 defines the required sequence at the QA level; PF09 — HDE-Build Checklist and HDE-Mechanics Guide provide the concrete tool names and CI job definitions.

### **2.2.12 Engine serializer/composer determinism**

* Prove two-run identity and AB↔BA parity (where defined) for Engine serializer/composer behavior.

* Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules.

* Tokens live in PF04/PF09; bytes in PF14/PF12.

  ### **2.2.13 Secrets & SCA/SAST/DAST**

* Run secrets scanning and composition analysis; add SAST/DAST appropriate to the repo.

* Keep test logs keys-only (no payloads/secrets). Governance lives in PF04; CI wiring in PF09.

  ### **2.2.14 Reproducibility & flake control**

* Fix seeds; avoid wall-clock; pin locale/timezone.

* Quarantine flakes with `QA_FLAKY_TEST_QUARANTINE_OK` until deflaked (token home PF09).

  ### **2.2.15 Test data & PII**

* Use synthetic fixtures where possible.

* Redact payloads.

* Enforce keys-only logs in tests (policy PF04).

## **2.3 Rails & environment posture — PO/epic mandated rails**

PF19’s default posture is **CLOSED rails** for CI and determinism-sensitive work (`SAFE_MODE=1`, `ALLOW_NETWORK=0` with env pins; see §0.4.3 and §2.2). For Live QA and epic-specific acceptance, **PO/epic-mandated rails are binding**:

* When a **PO or epic acceptance roster** explicitly mandates a rails posture for some or all QA steps (for example “open-rails Live QA only for vendor flows” or “all Live QA behavior tests must run with `APP_ENV=prod` and `ALLOW_NETWORK=1`”), those rails become the **acceptance rails** for the affected D-goals.

* In that case:

  * QA plans **MUST** design steps so that the mandated rails are actually in effect when the behavior is exercised (for example, vendor behavior steps must show `ALLOW_NETWORK=1` and the expected `APP_ENV` in their step logs, not just in planning notes).

  * If only closed-rails tests are run where open-rails behavior was mandated, the affected D-goals **MUST** be treated as **not satisfied**. The step’s primary log in QA\_ROOT (see §4.4) should record this explicitly via its `status` and `reason` fields (for example `status: FAIL` or `status: FAIL_TOOLING` with `reason: mandated open rails not available`).

  * Ignoring a mandated rails posture (for example running only closed-rails tests and treating them as equivalent to open-rails Live QA) is a **QA planning/execution failure**, not a benign variation. Any waiver or change in rails must be recorded explicitly in the epic’s acceptance roster (HDE Phased Epics) and in PF10/PF19 doc deltas, not inferred from ad-hoc deviations.

* Each Live QA step’s primary log **MUST** include a `rails` header field as described in §4.4, capturing at least:

  * `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`.

* This is the canonical evidence of which rails were actually in effect when the step ran; acceptance for rails-sensitive tokens (for example `OPEN_RAILS_ENV_OK`, `LIVE_VENDOR_TRANSPORT_OK`) is based on these logged rails, not on assumed defaults.

* When mandated rails **cannot** be met in the current environment (for example vendor connectivity or dev harness not available under open rails), QA must:

  * mark the affected steps as **TOOLING\_BLOCKED / FAIL\_TOOLING** in their headers with a clear `reason` (see §2.2.5 and §3.5.11), and

  * treat the corresponding D-goals as **blocked by tooling/infra**, not as silently passed.

This section aligns rails semantics across PF19: CI defaults to closed rails; Live QA may open rails where explicitly allowed; and PO/epic-mandated rails are binding acceptance rails that must be honored, logged, or explicitly blocked and remediated.

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

  ## **3.3 Environment constraints — pre-App, no-user QA mode**

In the current deployment posture, there is **no app-level user model** integrated with the HD Engine and **no persistent user-bound BodyGraph records** available for QA in production. Until the Glow App introduces a real user model and a future epic defines user-bound QA surfaces (see HDE Phased Epics), QA must follow a **no-user QA mode** for Engine and CLI Live QA.

**Reality (pre-App).**

* No app-level user IDs exist for the Engine to reference in prod.

* There are **no persistent BodyGraphs keyed to app users** that QA may rely on as fixtures.

* QA **must not create app-like user records in prod** ahead of Glow App integration.

**Effect on QA requirements.**

* Any QA requirement that assumes “existing users in prod” (for example, `showcompat --user-a/--user-b --source=db` or `bg:resolve` against real app user IDs) is treated as **blocked by environment**, not as failed acceptance.

* Those requirements must be explicitly called out in epic-level QA plans and deferred to a future epic once the app user model exists in **HDE Phased Epics** (titles-only).

* QA **must not** work around this by synthesizing “fake app users” in prod; doing so is considered a violation of this guide.

* In this pre-App, no-user environment, there is **no canonical DB-backed compat source** for live behavior tests. The only reliable, canonical source of **live compat/BodyGraph behavior** is the **vendor**. Engine “DB/auto” compat paths and CLI defaults that rely on a non-existent user model are **not valid** for Live QA behavior acceptance in this environment.

* CLI runs that **do not call vendor** (for example, pure serializer/math checks under closed rails) are allowed only as **local/offline** checks. They may satisfy determinism or canonicalization tokens, but they **do not** satisfy any token whose intent is “live product behavior with vendor rails active” and must be labeled accordingly in QA plans.

**Interim no-user QA mode (pattern).**

Until the app user model is live, use the following pattern for Engine/CLI QA in staging/prod-like environments.

1. **Compat & Reader from births only (vendor-backed behavior vs offline).**

   * For **live behavior tests** in this environment (including PO Live QA and any D-goals that assert “live compat behavior in prod”), use `hdctl showcompat` with:

     * **birth arguments only** (birthdate/time/location flags as defined in CLI/API docs; titles-only), and

     * an explicit **vendor source flag**, for example `showcompat --source=vendor` (exact flag spelling pinned in HDE-CLI-API-Vendor-Ref).

   * These runs are the **only** compat runs that count as “live behavior tests” in the pre-App environment.

   * `showcompat` runs that **do not** call vendor (for example, no `--source` flag and rails closed, or a purely local serializer path) are treated as **local/offline math/serializer checks**:

     * they may be used to prove canonical JSON, determinism, or AB↔BA identity, and

     * they **must** be explicitly labeled “local/offline (no vendor)” in QA plans and artifacts, and **must not** be used to satisfy tokens that assert live behavior.

   * In all cases, do **not** use `--user-a/--user-b` or `--source=db` in prod QA, because there are no app users or DB-backed BodyGraphs to rely on.

   * For vendor-backed compat Live QA runs, verify at minimum:

     * canonical JSON output on stdout,

     * AB↔BA identity by swapping the birth tuples (where required by the epic), and

     * Reader v1 envelopes via `--dump-reader` (shape and band-only posture per HDE-Math-Spec and HDE-CLI-API-Vendor-Ref; titles-only).

2. **Aux narratives from compat JSON (no DB users).**

   * Use `hdctl aux-preview --pair-file <compat.json>` (or equivalent API) based on **birth-generated compat JSON** from a vendor-backed compat run when testing behavior; in other cases, Aux QA may use compat JSON produced by offline checks as long as those runs are labeled “local/offline”.

   * Do **not** rely on DB users or user-bound records for Aux tests; treat compat JSON as the source of truth for Aux QA.

3. **BodyGraph resolver & vendor ingest (ephemeral QA keys and vendor-backed behavior).**

   * Treat any `--user` value used in `bg:resolve` during QA as an **ephemeral QA key**, not as a real app user ID. Keys should be clearly marked as QA (for example `qa_epic017_resolve1`, `qa_epic017_vendor1`).

   * In prod pre-App:

     * For **vendor-backed behavior tests**:

       * use explicit vendor-backed modes such as `bg:resolve --source=vendor` in dry-run or other controlled modes (exact flags and modes pinned in HDE-CLI-API-Vendor-Ref and HDE-Build Checklist);

       * ensure rails are open per Governance and infra canon for any step that intends to exercise live vendor behavior; and

       * store resolver/ingest metadata artifacts under `audit/qa/<epic-id>/…` with clear naming that indicates “vendor-backed behavior”.

     * For **offline/local checks** of resolver or ingest:

       * `bg:resolve` DB/auto **stub** behavior may be used only as a local/offline check (for example to smoke-test CLI wiring) and must be labeled as such; it does **not** satisfy live vendor behavior tokens in the pre-App environment.

       * `bg:resolve --source=vendor` under **closed rails** is expected to yield a typed refusal (no vendor calls) and may be used to prove refusal behavior and SAFE rails, but not live vendor behavior.

       * `bg:resolve --source=vendor --dry-run` under **open rails** may be used to prove live vendor behavior and ingest parity **without DB writes**.

     * `bg:resolve --source=vendor --upsert` remains **forbidden** in pre-Glow prod; vendor QA must use `--source=vendor --dry-run` or canonically defined closed-rails stubs. DB writes that resemble real app users remain out of scope until a Glow App user model exists (see this section and related addenda by title).

Live QA Guides and QA Plans that target live compat/BodyGraph behavior in this environment **must** adopt this pattern: any step that claims to be a **live behavior test** for compat or BodyGraph **must** call vendor explicitly, and any step that does not call vendor must be labeled clearly as **local/offline** and not used for behavior acceptance.

## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**

For **HDE-EPIC017**, manual Live QA converged on a specific pattern that PF19 adopts as the **reference pattern** for Engine Live QA.

### **Execution pattern (one command → one primary artifact)**

* Each manual Live QA step consists of a **single CLI or HTTP command** (or a very small, self-contained script) run from a Codespace attached to the engine repo.

* That command must write exactly **one primary evidence file** (log or JSON) under:

  * `audit/qa/HDE-EPIC017/logs/`, or

  * another clearly named subdirectory under `audit/qa/HDE-EPIC017/**`.

* The designated Live QA reviewer (for example a QA persona like Kronos) reviews that primary file and issues a short QA addendum (QA0X) summarizing:

  * which command was run,

  * what behavior was observed,

  * any document deltas, and

  * the QA verdict for that step.

* Any helper files for that step (for example parsed JSON derived from the log, pretty-printed variants, or computed diffs) also live under `audit/qa/HDE-EPIC017/**` and are referenced from the same addendum, but there is always **one** clearly identified **primary artifact** per step.

**Normative generalization (all Live QA epics).**

PF19 generalizes this EPIC017 pattern to **all Live QA epics**:

* Every Live QA step **MUST**:

  * define a **single primary command** (or very small script) that the operator runs;

  * identify **one primary artifact** under `audit/qa/<epic-id>/…` for that step (for example `d1-compat-001.log`, `d3-cli-guard-001.log`, `d7-docs-001-tree.txt`); and

  * treat all other files (parsed JSON, pretty prints, diffs) as **helper artifacts** that are clearly named and referenced from the primary artifact or QA addendum.

* Normative naming example:

  * primary artifact: `audit/qa/hde-epic018/d1-compat/d1-compat-001-run1.log`

  * helper artifacts:

    * `…/d1-compat-001-run1.json` (raw JSON),

    * `…/d1-compat-001-run1.pretty.json` (pretty-printed), and

    * `…/d1-compat-001-run1-vs-run2.diff` (determinism diff).

* In QA plans, “primary artifact” refers to the log or JSON named in the step header; helper artifacts are listed beneath it.

### **Command formatting (copy/paste-ready)**

Live QA instructions presented to a human operator (PO or IA) **MUST**:

* present commands in **copy/paste-ready form**:

  * one full shell command or pipeline per line or fenced block;

  * no inline mixing of narrative and shell on the same line; and

  * no line wrapping that changes semantics (for example breaking flags across lines without proper continuation).

* clearly mark any variable segments (for example `<pair-label>`, `<births-file>`) and describe how to substitute them.

* avoid “pseudo-shell” prose that cannot be copied as-is into a terminal.

PF19 treats **broken or ambiguous command formatting as a QA-plan defect**, not operator error. If the commands in a Live QA plan cannot be copied and run as-is on a canonical QA console, the plan must be corrected before the corresponding Live QA steps are executed.

### **Rails posture for manual Live QA (EPIC017 only)**

* Manual Live QA steps that touch **vendor** or **Railway** prod run with **open rails** in the Codespace as required by the command (for example `ALLOW_NETWORK=1`, `SAFE_MODE=0`):

  * CLI compat/Reader/Aux previews hitting Railway or vendor;

  * vendor dry-run ingest calls (`bg:resolve --source=vendor --dry-run`).

* Manual Live QA must **not** modify code or configuration and must **not** write outside `audit/qa/**` for evidence.

* Closed-rails testing (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) remains the responsibility of:

  * CI jobs wired in the repo (pytest suites, evidence tools, mirror checks, ordering tests, etc.), and

  * pre-merge QA on PRs implementing EPIC017 foundations.

Manual Live QA does **not** attempt to replicate those closed-rails tests; instead it focuses on demonstrating real prod behavior of key surfaces via open-rails commands from Codespaces into Railway.

### **Vendor and DB safety constraints**

* Even under open rails:

  * `bg:resolve --source=vendor --upsert` remains **forbidden** in pre-Glow prod; vendor QA must use `--source=vendor --dry-run` or canonically defined closed-rails stubs.

  * DB writes that resemble real app users remain out of scope until a Glow App user model exists (see pre-App no-user QA mode and related addenda by title).

### **Doc-alignment steps (mechanical, not narrative)**

For doc-alignment Live QA steps (for example EPIC018 D7):

* The step **MUST** rely on **mechanical commands** (for example `ls`, `grep`, `find`, `python` tooling) that:

  * generate tree listings, filtered file lists, or diffs; and

  * write their outputs under `audit/qa/<epic-id>/d7-docs/` (or an equivalent `dN-docs` subtree) as primary or helper artifacts.

* POs and IAs are **not expected** to write prose summaries of doc alignment during Live QA. Any narrative synthesis of manifest/closeout alignment belongs in:

  * **PF10 — HDE-Build Notes** (for build and QA addenda), or

  * **HDE Phased Epics** (for epic acceptance and closeout),

* authored by QA personas or Leads, not in `qa_notes.md` or d7-docs artifacts.

Teams designing Live QA for future epics **SHOULD** start from this EPIC017 pattern — one command → one primary artifact per step, copy/paste-ready commands, and mechanical doc-alignment artifacts under `audit/qa/<epic-id>/d*-…` — and adapt it only where epic-specific surfaces or rails require a different approach.

## **3.5 Live QA via Codespaces → Railway (cross-epic crib)**

This section generalizes the EPIC017 pattern into a required crib for any epic that uses “prod via Codespaces” (or an equivalent terminal) to exercise HD Engine prod behavior.

---

### **3.5.1 Prod and console roles**

**Prod**

* For Live QA, **prod** is the HD Engine service and DB defined in infra and build canon (by title, for example Glow Infrastructure and HDE-Build Notes), **not** the Codespaces container.

**Codespaces / QA console**

* A Codespace attached to the engine repo is a **QA console and artifact sink**:

  * it runs CLI/HTTP commands **from** Codespaces **to** the Railway HD Engine prod service and DB (when rails allow), and

  * it stores QA artifacts under `audit/qa/<epic-id>/…` in the repo, where `<epic-id>` is the lower-case epic identifier (for example `hde-epic018`).

* Any other terminal or shell that is configured (by infra canon) to reach the same Railway endpoints is an equivalent QA console. PF19’s CLI and admin-bundle playbooks apply equally to Codespaces and to such terminals.

* IAs and QA plans **MUST NOT** treat Codespaces itself as “prod”; any QA plan that does so is mis-aligned with this guide.

---

### **3.5.2 Step 0 — prod handshake (identity-only, not behavior)**

For any epic that claims to do “Live QA via Codespaces → Railway”:

* The QA plan **MUST** include a Step-0 “prod handshake” from a QA console:

  * calling the canonical HD Engine prod base URL (for example `/internal/version` on the Railway service defined in infra canon, titles-only), and

  * capturing the response under `audit/qa/<epic-id>/logs/…` as governed evidence.

* `/internal/version` is an **identity / pre-flight** endpoint. Its job in Live QA is to prove:

  * that the QA console (Codespaces or equivalent) can reach the prod engine, and

  * which `engine_tag`, `release_id`, commit, and `invocation_tag` are live at the time of QA (as already described in the EPIC017 QA history).

* Live QA plans **MUST NOT** present `/internal/version` as satisfying any D-goal or token related to behavior (compat math, narratives, vendor ingest, admin bundle, “full product payload”). It is a prerequisite and an identity anchor for later evidence, not a substitute for real behavior tests.

* If infra/build canon does not yet define the prod base URL or DB (or they conflict), the epic’s Live QA plan **must** mark prod handshake as **blocked by spec ambiguity** rather than guessing or asking the PO for values.

---

### **3.5.3 Closed-rails determinism vs open-rails behavior tests**

**Closed-rails determinism**

* Closed-rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0` with env pins) remain the default for CI and determinism jobs (serializer tests, env-pins checks, sanity pipeline, config determinism) and are covered in §2.2, §4.3, and §9.2.

* These jobs typically run in Codespaces or CI, **not** against prod.

**Open-rails behavior tests**

* Open-rails from a QA console into Railway are allowed **only** for Live QA steps explicitly described in the epic QA plan and governed by this guide and HDE-Governance (for example EPIC017’s compat/Reader/Aux/vendor dry-run checks, or the admin bundle flows described in §5.8).

* For **behavior D-goals** (compat, narratives, vendor ingest, full product payload, admin bundle) the **exercise context** must be a **prod-facing environment**, not “hdctl logic inside Codespaces with closed rails.” Examples of prod-facing exercise contexts:

  * an admin CLI running on a terminal that can reach the Railway HD Engine base URL defined in infra canon and is configured per HDE-CLI-API-Vendor-Ref / HDE-Mechanics Guide; or

  * an Admin GUI in a browser calling an admin route on the Railway service.

* Live QA plans that ignore this separation, omit the prod handshake, or treat canonical infra/env values as PO-supplied inputs are considered **underspecified** under PF19 and should be rejected or revised before implementation.

---

### **3.5.4 Artifact-first Live QA pattern (behavior vs artifacts)**

For any Live QA step that refers to **behavior**, QA plans **MUST** follow a two-part, artifact-first pattern.

#### **1\) Behavior run (prod-facing environment)**

The QA plan **MUST** specify **where** the behavior is exercised:

* for example, “run `hdctl` on an admin terminal that can reach `https://…railway.app` and is configured with the canonical env and secrets,” or

* “click the Admin GUI control that calls the admin bundle HTTP route.”

The plan must:

* describe the inputs (for example fixed birth tuples or, post user-model, user IDs), and

* describe the expected observable behavior at the prod-facing surface (status, body shape, high-level outcome).

Where possible, it should also prescribe how to **capture outputs** on that environment (for example writing JSON to a file, saving a log transcript, or exporting a report).

#### **2\) Artifact capture and analysis (Codespaces / QA console)**

The QA plan **MUST** then describe how artifacts from the behavior environment are brought into the canonical QA tree under `audit/qa/<epic-id>/…` and analyzed. At minimum, Live QA instructions **MUST** include fenced or clearly reproducible commands that:

* create any needed subdirectories under `audit/qa/<epic-id>/…` (all lower-case directories; see §8),

* copy or upload the behavior artifacts into those directories (for example via `scp`, `gh run download`, or equivalent),

* run offline validation in the QA console (for example `python -m json.tool`, `cmp`, `sha256sum`, header/posture checks) and write results to files in `audit/qa/<epic-id>/…`, and

* append step notes to `audit/qa/<epic-id>/logs/qa_notes.md` via commands (for example  
   `echo "HDE-EPIC018 Live QA – d1-compat-001 ..." >> qa_notes.md`), **not** via manual editing, consistent with §4.3.

**Key principle**

* Codespaces is where we **persist and analyze what happened** when we ran prod; it is **not** itself the authoritative behavior runtime.

* Live QA plans **MUST NOT** conflate these two phases. A step that only runs logic inside Codespaces under closed rails (for example, `hdctl showcompat` pointing at localhost with `SAFE_MODE=1`, `ALLOW_NETWORK=0`) may be used as a **local smoke check**, but **cannot** be used to satisfy tokens or D-goals that assert prod behavior (compat in prod, narratives in prod, vendor ingest in prod, full product payload from prod). Any such step must be explicitly labeled as a local smoke check in the QA plan and must not be used to claim prod behavior tokens.

---

### **3.5.5 Pre-Glow full-payload admin bundle flow (acceptance expectation)**

In the pre-Glow period (before the App is integrated with the HD Engine and before the Admin Bundle CLI/GUI surfaces are fully implemented), any epic that claims the product is usable or testable “in prod” **MUST** include at least one Live QA step that:

* exercises the **full product payload** for a single match via **prod-facing behavior**, and

* follows the **artifact-first pattern** described in §3.5.4,

* with **no** GUI-only shortcuts and **no** Codespaces-only behavior.

For epics executed **before** the admin bundle surfaces exist:

* This requirement is satisfied by the historical “full product payload” flows that compose BodyGraphs, compat, and narratives via individual CLI and HTTP calls on a prod-facing machine, as described in earlier PF19 and HDE-Build Notes addenda (titles-only).

* Once the admin bundle builder and admin surfaces are implemented and pinned in canon, **new epics MUST use the admin bundle surfaces** as the primary behavior paths, not reassemble the payload manually.

For this full-payload step, the Live QA plan **MUST** specify:

* **Behavior run**

  * A prod-facing environment (for example an admin terminal running the admin bundle CLI against Railway, or an Admin GUI in a browser calling the admin bundle HTTP route); and

  * The exact inputs used.

* **Artifact capture / analysis**

  * How the resulting admin bundle JSON and logs are brought into `audit/qa/<epic-id>/…` from the behavior environment; and

  * How parity and auth are checked, following §5.8 and the artifact-first pattern above.

Evidence for this step **MUST**:

* be captured under `audit/qa/<epic-id>/…`;

* be wired into the evidence skeleton (Index, mirror, path-proofs) in the same PR; and

* support the admin-bundle tokens from §9.1.5 and §9.2.7:

  * `CLI_ADMIN_BUNDLE_PARITY_OK` — CLI and HTTP admin bundles match for the same inputs and credential.

  * `ADMIN_BUNDLE_FULL_PAYLOAD_OK` — each admin bundle contains all required structural elements (BodyGraphs, compat, three narratives, meta) as defined in the owning PF docs.

  * `ADMIN_AUTH_REQUIRED_OK` — neither CLI nor HTTP admin surfaces return an admin bundle without the configured admin credential; unauthenticated and mis-authenticated attempts return typed errors only.

Any pre-Glow Live QA plan that does **not** demonstrate at least one such **artifact-first, prod-facing full-payload flow** is considered incomplete under PF19 once the admin bundle surfaces exist (or an equivalent full-payload behavior flow is defined), and must be revised before tokens depending on “product usable via admin bundle surfaces” or “full product payload from prod” can be claimed.

---

### **3.5.6 PO Live QA sessions (vendor-first rails)**

For EPIC018 and all future epics, **“PO Live QA” is vendor-first by definition**.

**Definition and scope**

* A PO-run Live QA session is a **short, focused session** whose primary and explicit goal is to exercise **live vendor behavior** against the production HD Engine and to capture mechanical evidence of that behavior.

* Live QA plans recognize three classes of checks:

  1. **Ops/identity checks**  
      (for example, `/internal/version` identity pings, env/rails snapshots).

  2. **Internal functional/determinism checks**  
      (serializer/compat determinism, sanity pipeline, CLI guards and invariants) that are already covered by CI and automated QA.

  3. **Vendor flows**  
      (vendor-backed BodyGraph resolution and compat, vendor error handling, live vendor rails checks in prod).

* **Only class (3) belongs in PO Live QA.** Classes (1) and (2) are useful to QA/infra/CI but **do not justify** PO Live QA time and **must not** be treated as part of the PO’s Live QA workload.

**Roles of each class**

* **Ops/identity steps (class 1\)**, including the `/internal/version` handshake:

  * are treated as **pre-flight / internal**;

  * are designed and executed by QA/infra (or CodEx) **before** PO Live QA; and

  * may be referenced in PO notes as preconditions, but are **not** counted as PO Live QA steps and **cannot** satisfy behavior D-goals.

* **Internal functional/determinism steps (class 2\)** such as serializer determinism, sanity pipeline, CLI guards, or evidence skeleton checks:

  * remain entirely within **CI/QA/infra** responsibility (PF09 and PF14 wiring); and

  * must **not** be scheduled as PO Live QA tasks, even if they are re-run in staging/prod. They are prerequisites, not PO targets.

* **Vendor-focused steps (class 3\)** such as:

  * vendor-backed BodyGraph resolution (for example `bg:resolve --source=vendor` in dry-run or other controlled modes),

  * vendor-backed compat calculations (for example `showcompat --source=vendor` or equivalent Admin Bundle based paths once defined), and

  * deliberately chosen vendor error conditions and edge cases (malformed input, missing data, vendor timeouts),

* are the **only** steps that may appear in PO Live QA as core workload.

**Codespaces in PO Live QA**

In PO Live QA, Codespaces has the same roles as in §3.5.1, with one additional constraint:

* By default, Codespaces is an **artifact sink and offline analysis console**. It is where:

  * QA directories under `audit/qa/<epic-id>/…` are created;

  * artifacts from prod-facing runs are stored; and

  * offline checks (`python -m json.tool`, `cmp`, `sha256sum`, header validation) are executed.

* Codespaces **MAY** temporarily act as a vendor client (for example, by setting `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and configuring a base URL to Railway prod) **only when all of the following are true**:

  * the goal of the step is to exercise a **live vendor flow** (class 3), not an identity or determinism check;

  * the rail-opening for that step is documented (env vars set, commands logged, and artifacts written under `audit/qa/<epic-id>/logs/…` or a vendor-specific subdirectory); and

  * the PO has agreed that this is an acceptable way to reach prod vendor rails for the current epic.

* For **non-vendor behavior** (serializer determinism, guards, sanity pipeline, closed-rails tests), Codespaces **MUST NOT** be used as a surrogate “prod” environment in PO Live QA. Those checks remain in the CI/QA/infra domain and are out of scope for PO Live QA sessions.

---

### **3.5.7 Vendor vs non-vendor steps in Live QA plans**

Any Live QA Guide or QA Plan for an epic **MUST**:

* clearly label each Live QA step as **vendor-focused** (class 3), **ops-only** (class 1), or **internal functional/determinism** (class 2); and

* explicitly indicate **which subset of steps is expected to be run by the PO** in Live QA, and **which steps are preconditions/CI responsibilities**.

For EPIC018 and forward, PO Live QA plans **MUST**:

* define the core PO workload as a small set of vendor-focused steps (for example, “Step V1: vendor dry-run resolve,” “Step V2: vendor-backed compat,” “Step V3: vendor error behavior”); and

* treat all non-vendor steps (identity, serializer determinism, sanity pipeline, CLI guards, closed-rails checks) as **pre-verified** by CI/QA; the PO is **not** expected to re-run these manually during Live QA.

If a Live QA plan includes non-vendor steps (for example, a pre-flight `/internal/version` handshake), those steps **MUST** be explicitly marked as:

* “Pre-flight / internal”; and

* “Handled by QA/infra outside PO’s Live QA time”.

These labels ensure that PO Live QA is reserved for vendor behavior, while CI/QA/infra continue to own identity, determinism, and guard checks.

---

### **3.5.8 Evidence expectations for vendor-focused PO steps**

Each vendor-focused PO step **MUST** produce at least one mechanical artifact under `audit/qa/<epic-id>/…` that directly reflects **vendor behavior**, in addition to any governed artifacts under `docs/**` or `artifacts/**`.

At minimum, for each vendor step QA must capture:

* a **request description** file (for example `audit/qa/<epic-id>/vendor-step-001-request.txt`) that names the command or GUI action, the environment used, and the inputs (birth tuples, synthetic IDs, or, once in scope, user IDs);

* the **raw outputs** in a governed file (for example `…/vendor-step-001-run1.json` or `…/vendor-step-001-run1.log`), and, where helpful, a **pretty-printed** form (for example `…/vendor-step-001-run1.pretty.json`);

* any **diff/cmp results** for determinism checks (for example `…/vendor-step-001-run1-vs-run2.diff`), when the step is meant to assert vendor determinism; and

* at least one `qa_notes.md` line, appended via commands (for example  
   `echo "HDE-EPIC018 PO Live QA – vendor-step-001: vendor-backed compat behaved as expected" >> audit/qa/<epic-id>/logs/qa_notes.md`), not via manual editing, consistent with §4.3.

Vendor-focused artifacts should live under a clear **vendor-specific subtree** of the QA directory (for example `audit/qa/<epic-id>/vendor/…` or a vendor-prefixed D-step directory) so that vendor evidence is easy to locate and reference from epic acceptance rosters (see HDE Phased Epics and PF20 by title).

All vendor-focused PO artifacts remain subject to the same evidence rules as other governed artifacts:

* directory names under governed roots are **lower-case** (§8);

* artifacts are eventually indexed in the Human Index and Machine Mirror with path-proofs in the same PR that relies on them (§4.2–§4.3); and

* Live QA plans treat “vendor evidence present but not indexed” as a QA failure that blocks tokens depending on that evidence.

---

### **3.5.9 Relationship to Admin Bundle / Admin CLI / Admin GUI (forward-looking)**

**Until** Admin Bundle, Admin CLI, and Admin GUI surfaces are fully implemented and pinned in canon:

* vendor-focused PO Live QA **MAY** continue to use existing CLI vendor paths (for example `bg:resolve --source=vendor --dry-run`, `showcompat --source=vendor`) as the primary behavioral rails, assembling any “full product payload” expectations (BodyGraphs \+ compat \+ narratives) from those primitives, with artifacts for each component stored under `audit/qa/<epic-id>/…` and indexed appropriately.

**Once** Admin Bundle / Admin CLI / Admin GUI are available:

* PO Live QA sessions **SHOULD** migrate to using those admin surfaces as the primary vendor behavioral rails (for example a single admin bundle call for full payload), while:

  * keeping Codespaces in the **artifact-sink and offline analysis** role defined earlier in this section; and

  * preserving the **vendor-first** constraint: the point of PO Live QA remains to exercise live vendor behavior, not to re-run identity or internal determinism checks already covered by CI/QA/infra.

### **3.5.10 CLI guard tools in open-rails Live QA (informational only)**

CLI guard tools such as `serializer_grep_guard.py` and `emitter_symbol_proof.py` are designed as **closed-rails determinism guards**. Their canonical **PASS** condition (exit code 0 with no violations) belongs to the **D3 guard stage in CI**, not to open-rails Live QA.

**Canonical role of guards (closed-rails CI).**

* Under **closed determinism rails** (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`), guard tools are expected to:

  * verify that CLI/Engine code uses the canonical serializer/emitter and no ad-hoc encoders;

  * enforce determinism env pins and wiring invariants; and

  * exit with status 0 when those invariants hold.

* The corresponding D3 guard tokens (`CLI_SERIALIZER_GUARD_OK`, `SERIALIZER_GREP_GUARD_OK`, `EMITTER_SYMBOL_PROOF_OK`) are satisfied **only** by such **closed-rails CI runs** (see §9.2.11), not by Live QA in open-rails environments.

**Guards in open-rails Live QA (PO/IA Codespaces).**

When guards are run from a QA console whose rails are intentionally **open** (for example a Codespace configured as in §3.5 for PO/IA Live QA):

* The environment **does not** match the closed determinism rails the guards expect.

* In that posture, the guards are expected to:

  * **fail closed** with a non-zero exit code (typically `1`) due to env-pin mismatch; and

  * log that the env rails do not match their closed-rails requirements, without asserting anything about serializer/emitter wiring correctness in CI.

* Such runs are treated as **informational env-enforcement checks only**:

  * they show that the guard tools correctly enforce env pins and refuse to silently “pass” under the wrong rails; and

  * they do **not** contribute to satisfying D3 guard tokens and must **not** be interpreted as D3 acceptance failures when the environment is intentionally open rails.

**QA planning and PO Live QA scope.**

* Live QA plans that include guard steps in open-rails environments **MUST**:

  * label those steps explicitly as **“open-rails guard env check (informational only)”**; and

  * record their artifacts (logs, exit-code files, and notes) under `audit/qa/<epic-id>/d3-cli-guards/` or an equivalent subtree, noting that exit codes reflect env mismatch, not serializer/emitter wiring.

* PO Live QA plans **MUST NOT** require guard exit code 0 in open-rails environments:

  * D3 guard tokens are satisfied by CI/closed-rails runs; PO Live QA may reference CI status for those tokens rather than re-running guards under closed rails.

  * A guard run that fails solely because rails are open **must not block** PO Live QA or be treated as a product behavior failure, provided CI has already produced passing D3 guard evidence.

* If Live QA discovers a guard failure that persists **under closed rails** (for example, by reproducing the failure in a closed-rails CI or dev environment), that failure belongs to the D3 guard tokens and must be handled as a CI/closed-rails issue, not as an open-rails Live QA responsibility.

This section keeps the separation clear: **CI/closed rails** are authoritative for D3 guard tokens and serializer/emitter wiring, while **open-rails Live QA** may invoke guards only to confirm env-pin enforcement, without treating their non-zero exit codes as D3 acceptance failures in that context.

### **3.5.11 Tooling vs behavior failures for HTTP surfaces (TOOLING\_BLOCKED)**

Live QA steps that exercise **HTTP surfaces** (for example internal/dev harnesses such as `/internal/dev/sampler`) can fail for two very different reasons:

* **Tooling/infra failures** — the required HTTP service is not running, not reachable, or speaking the wrong protocol on the assumed host/port; and

* **Behavior failures** — the service is reachable and returns a valid HTTP/1.x response, but the status/body/headers do not match the expected behavior defined in the owning PF docs.

PF19 requires QA plans and logs to **distinguish these cases explicitly**.

**HTTP tooling/infra failure (TOOLING\_BLOCKED / FAIL\_TOOLING).**

A Live QA step that targets an HTTP surface **MUST** be classified as a **tooling/infra failure** (TOOLING\_BLOCKED / FAIL\_TOOLING) when:

* the target URL cannot be reached as a valid HTTP/1.x service (for example curl reports `HTTP_STATUS:000`, “Received HTTP/0.9 when not allowed,” connection refused, or TLS handshake failure); or

* the response is not a valid HTTP/1.x response with status and headers (for example raw text with no status line or no headers), and logs indicate that the intended handler was never exercised.

In these cases:

* QA **MUST**:

  * capture a Live QA log under `audit/qa/<epic-id>/…` for the step (for example `D3-http-…`), and

  * include in the log header a clear marker such as:

    * `status: FAIL_TOOLING` (or `status: TOOLING_BLOCKED`), and

    * a short `reason` field describing the infra issue (for example `reason: dev Reader service not running on 127.0.0.1:3000; curl HTTP_STATUS:000`).

* The affected D-goal (for example “HTTP dev sampler behavior & gating”) **MUST** be treated as **unverified** in the epic’s acceptance roster:

  * acceptance for that D-goal **cannot** be closed, and

  * the **root cause** is recorded as infra/service readiness (dev harness missing or miswired), not as an application behavior bug.

* QA and Leads **MUST NOT**:

  * mark application-level behavior tokens as failed **solely** because the HTTP service was unavailable or speaking the wrong protocol; or

  * silently skip the step and treat the D-goal as implicitly passed.

Instead, the D-goal remains **blocked by tooling/infra** until infra wiring is corrected (see §1.4 and §11.2).

**HTTP behavior failure.**

A Live QA step is a **behavior failure** only when:

* the HTTP service is reachable and returns a valid HTTP/1.x response (status line, headers); and

* the observed status/body/headers clearly contradict the behavior specified in the owning PF docs (titles-only), for example:

  * wrong APP\_ENV gating (200 where 403 is expected or vice versa);

  * missing or malformed JSON body when a JSON envelope is required; or

  * incorrect header posture (`Cache-Control`, `Content-Type`, or refusal envelope mismatches).

In these cases, QA **MUST**:

* classify the step as a behavior failure in the log header (for example `status: FAIL_BEHAVIOR`), and

* route the failure through the normal bug/epic remediation process (for example PF10 addendum, PF20 epic update, code fixes).

**Planning implications.**

* Live QA plans **MUST** include a **service readiness check** (for example a simple `curl` health probe against the canonical dev/prod URLs defined in Glow Infrastructure and HDE-Mechanics Guide) before running behavior-focused HTTP steps. If the readiness check fails with tooling/infra symptoms (as above), subsequent behavior steps for that surface should be marked TOOLING\_BLOCKED rather than attempted blindly.

* When a dev harness or HTTP service does not yet exist or is not reachable in the target environment, the corresponding D-goals in **HDE Phased Epics** **MUST** be marked as “blocked by infra/service readiness” until Glow Infrastructure and Mechanics docs define and wire the harness (see §1.4 and §11.2). QA plans must not guess ports or URLs to “work around” missing infra.

This classification keeps responsibility clear: **Infra/Ops** own dev harness wiring and HTTP service readiness; **application teams** own behavior; QA makes the distinction explicit in logs and acceptance, and does not conflate missing or miswired services with application logic failures.

## **3.6 Repo introspection before Live QA plan (d0 planning artifacts)**

Before finalizing any Live QA plan for an epic, the Implementation Agent (or QA author) **MUST** perform a short, mechanical **repo introspection** and record the results as `d0-*` planning artifacts under the epic’s QA tree.

**Intent**

* Prevent path/CLI drift between PF-Canon and the **running repo snapshot**.

* Ensure Live QA plans reflect actual tools, configs, ignore rules, and governed artifacts that exist in the repo at the time of planning.

* Produce mechanical planning evidence under `audit/qa/<epic-id>/…` that later reviewers can consult.

**d0 introspection checklist**

For each epic that will have Live QA:

1. **Inspect governed config and bundles.**

   * Run mechanical commands (for example):

     * `ls artifacts/config`

     * `ls artifacts/config_bundles`

     * `ls artifacts/registry`

   * Capture outputs as planning artifacts under, for example:

     * `audit/qa/<epic-id>/d0-planning/d0-config-tree.txt`

     * `audit/qa/<epic-id>/d0-planning/d0-bundles-tree.txt`

2. **Locate guard scripts and sanity pipeline runners.**

   * Use `ls`/`grep`/`find` to discover:

     * CLI guard scripts (for example `serializer_grep_guard.py`, `emitter_symbol_proof.py`), and

     * sanity pipeline runners or evidence harnesses.

   * Capture outputs (paths and brief context) under, for example:

     * `audit/qa/<epic-id>/d0-planning/d0-guards-tree.txt`

     * `audit/qa/<epic-id>/d0-planning/d0-sanity-runner-notes.txt`

3. **Verify actual CLI options via help commands.**

   * Run the canonical `--help` or equivalent for the CLI:

     * for example `hdctl --help`, `hdctl showcompat --help`, `hdctl bg:resolve --help`.

   * Capture the help output (or relevant excerpts) as governed planning artifacts:

     * `audit/qa/<epic-id>/d0-planning/d0-hdctl-help.txt`

     * `audit/qa/<epic-id>/d0-planning/d0-showcompat-help.txt`

     * `audit/qa/<epic-id>/d0-planning/d0-bg-resolve-help.txt`

   * Live QA plans **MUST NOT** invent flags or subcommands that do not appear in the current help output.

4. **Record environment posture and rails intent.**

   * Capture a short, mechanical summary of the intended rails posture for Live QA in this epic (for example, “Codespaces open-rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`” or “CLI runs only in closed dev harness”).

   * Use a simple command such as:

     * `env | sort | grep -E 'SAFE_MODE|ALLOW_NETWORK|APP_ENV|HDE_BASE_URL'`

   * Store this in `audit/qa/<epic-id>/d0-planning/d0-env-rails.txt`.

5. **Verify .gitignore rails for `audit/qa/<epic-id>`.**

   * Inspect the repo’s `.gitignore` (and any additional ignore files) to confirm that canonical QA trees under `audit/qa/<epic-id>/…` are **not** ignored:

     * there are no broad ignore patterns that match `audit/qa/**` without corresponding allow rules, and

     * `audit/qa/<epic-id>/…` is visible to git without requiring forced adds.

   * Capture the relevant `.gitignore` excerpts and a short mechanical check under, for example:

     * `audit/qa/<epic-id>/d0-planning/d0-gitignore-audit-qa.txt`

   * (for example by using `grep`/`git check-ignore` to show that `audit/qa/<epic-id>` is not matched by any ignore entry).

   * If existing ignore patterns hide canonical QA roots (for example legacy `Audit/QA/**` or `audit/qa/**` rules), the IA must:

     * coordinate with the build/infra owner to tighten or remove those patterns so that `audit/qa/<epic-id>/…` is tracked; and

     * capture the change and its rationale in PF10 build notes or PF20 acceptance records (titles-only), referencing this section of PF19.

**D0 CLI baseline pattern (names-only)**

When a Live QA plan includes a **D0 “CLI baseline”** step, PF19 adopts the following pattern so that the baseline is **derived from canon and repo reality**, not assumptions:

*Baseline intent (Live QA).*  
 The D0 CLI baseline step exists to prove that:

* `hdctl` is present and executable on the QA console; and

* the CLI help surfaces needed by the plan (for example `hdctl --help`, `hdctl showcompat --help`, `hdctl bg:resolve --help`) match the commands and flags the plan intends to use, consistent with **HDE-CLI-API-Vendor-Ref** (titles-only).

D0 CLI baseline is **not** an identity or release check; version semantics belong to `/internal/version` and identity evidence, not to this step.

*Allowed baseline checks.*  
 A conforming D0 CLI baseline step SHOULD:

* run `hdctl --help` (and, where relevant, subcommand `--help` invocations) under the intended rails for later steps;

* capture that help output as governed d0 artifacts under `audit/qa/<epic-id>/d0-planning/` (for example `d0-hdctl-help.txt`, `d0-showcompat-help.txt`, `d0-bg-resolve-help.txt`); and

* derive the CLI commands and flags in the Live QA plan directly from those artifacts and from **HDE-CLI-API-Vendor-Ref**, not from remembered or guessed behavior.

The baseline MAY also include a simple presence check (for example `which hdctl` or checking the exit status of `hdctl --help`) recorded in the same d0 log.

*Forbidden assumptions.*  
 Unless and until **HDE-CLI-API-Vendor-Ref** explicitly defines it, D0 CLI baseline MUST NOT:

* assume that `hdctl --version` exists; or

* assert any specific `hdctl --version` format or semantics as an acceptance condition.

If `hdctl --version` is run at all during D0, its behavior MUST be treated as observational only and MUST NOT be used as a basis for pass/fail judgments.

*Planning rule.*

* The D0 CLI baseline step’s primary log header (see §4.4) MUST describe the baseline in these terms (presence and help, not version semantics).

* If captured help output disagrees with the commands/flags written in the draft Live QA plan, that mismatch MUST be treated as a D0 planning error to be corrected before involving the PO in Live QA, not as a behavior failure in later steps.

This pattern applies to EPIC020 and to all future epics that use a D0 CLI baseline: these steps prove **“CLI exists and help matches canon and repo reality”**, not undocumented `--version` behavior.

**Planning evidence and Live QA alignment**

* These `d0-*` artifacts are treated as **planning evidence**:

  * they are governed artifacts under `audit/qa/<epic-id>/…` and are subject to the mechanical evidence rules in §4.3; and

  * they must be present **before** Live QA steps are finalized and executed.

* Live QA plans **MUST**:

  * reference `d0-*` artifacts when specifying paths, scripts, CLI commands, and QA trees; and

  * revise the plan if repo introspection reveals different paths, options, harnesses, or ignore rules than canonical PF docs imply.

* If later QA steps (for example D5/D6) discover a mismatch between the plan and actual paths/options or `.gitignore` behavior, the IA must:

  * capture new mechanical evidence under `audit/qa/<epic-id>/d0-planning/` or a new `dN-*` planning step, and

  * update the Live QA plan and PF10/PF20 doc deltas accordingly, instead of continuing with stale or incorrect instructions or relying on forced git adds for QA evidence.  
  * 

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

**Mechanical QA artifacts and notes (Live QA and bootstrap).**

* All **Live QA and bootstrap steps** for an epic **MUST** produce **mechanical artifacts**: files created by commands or scripts (for example shell/Python tools, `echo`/redirection, or purpose-built QA harnesses), not by manual in-editor edits. Manual editing of governed evidence files or QA notes in place is considered a QA failure and must be remediated by regenerating the files mechanically and preserving any prior corrupted content as separate mechanical artifacts when needed.

* For each epic, the canonical QA evidence root for Live QA is `audit/qa/<epic-id>/…` with a lower-case `<epic-id>` (for example `hde-epic018`). Every PO- or IA-driven Live QA step **MUST** generate at least one new mechanical artifact under that root (such as a tree listing, environment snapshot, or step-specific log), in addition to any governed artifacts under `docs/**` or `artifacts/**` that are indexed via the Evidence Index and Machine Mirror.

* QA notes and logs that live under the QA tree (for example `qa_notes.md` or step-indexed markdown files in `audit/qa/<epic-id>/logs/`) are treated as part of the QA evidence. They **MUST** be maintained via scripted or shell commands (for example `echo "…step note…" >> qa_notes.md`) and are subject to the same env pins and indexing rules as other governed artifacts. Hand-editing these files (for example via an editor) is not allowed under PF19; if a note file is accidentally edited by hand, remediation must:

  * capture the pre-remediation content mechanically into a separate “original” or “corrupted” snapshot under `audit/qa/<epic-id>/logs/`, and

  * rewrite the live notes file via commands so that its current contents and history are fully reproducible from the QA plan and command log.

* The **bootstrap step** for each new epic’s QA plan (often labeled `d0-…` in the QA directory) **SHOULD** at minimum:

  * create the canonical QA tree under `audit/qa/<epic-id>/…` with the expected lower-case subdirectories; and

  * capture mechanical environment context for that bootstrap (for example a directory tree listing, the Python version in use, and the working directory for the Codespace or QA console) as files under `audit/qa/<epic-id>/logs/`.

* These bootstrap artifacts are governed evidence for the epic’s QA environment and must eventually be brought under the Evidence Index and Machine Mirror when they become part of the epic’s acceptance surface.

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

## **4.4 QA evidence file structure and step logs**

PF19 expects QA evidence to be not only complete and indexed (§4.2–§4.3), but also **reviewable**. To that end, QA Plans and Live QA runs **MUST** adopt a consistent, per-step log structure under a run root (“QA\_ROOT”) inside the epic’s QA tree.

**QA\_ROOT (per-run root).**

* For each Live QA run or QA Plan execution for an epic, QA defines a **QA\_ROOT directory** under the epic’s QA tree, for example:

  * `audit/qa/<epic-id>/live-qa-<date>/` or

  * `audit/qa/<epic-id>/run-<id>/`.

* All per-step logs for that run live **directly under** this QA\_ROOT (or a single, clearly named immediate subdirectory if the epic defines one), so reviewers can see the entire run at a glance without hunting across multiple ad hoc trees.

PF19 does not prescribe a single naming convention for QA\_ROOT; it requires only that each run choose a clear root and keep step logs consolidated under it.

**One primary log per step.**

For each QA Plan step (D-goal slice or numbered “Step N” in the plan):

* There **MUST** be exactly **one primary evidence log file** for that step under the run’s QA\_ROOT, named **deterministically** according to the epic’s convention. Acceptable patterns include:

  * `D0-<shortname>.log`, `D1-<shortname>.log`, …; or

  * `step0_<shortname>.log`, `step1_<shortname>.log`, …

* as long as the mapping from QA Plan steps to log filenames is obvious and documented in the plan.

* That primary log is the **canonical reference point** for QA review of the step. All other files (temporary JSON bodies, pretty-printed outputs, diffs, helper summaries) are treated as **supporting artifacts**, not as alternate primary logs.

**Required header fields.**

Each per-step primary log **MUST** begin with a machine-readable header block that includes at least:

* `check_id` — a stable identifier for the step (for example `D4_sampler_evidence_index`, `D0_vendor_ingest`).

* `command` — the full shell command (or small script entrypoint) that was run for this step; if multiple commands are required, the header must either:

  * list the main command and note that helper commands are described later in the log; or

  * list each command in a small, clearly labeled array.

* `rails` — a concise snapshot of the env/rails for this step (for example `SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC, APP_ENV=dev`), consistent with §0.4.3 and §2.2.

* `pf_refs` — titles-only references to relevant PF docs or sections (for example “PF19 §5.6 CLI/API & SDKs”, “PF12 Evidence Catalog”).

* `tokens` — the QA acceptance tokens this step is intended to exercise or support (names-only, from §9.1/§9.2).

* `status` — the current status of the step, with values drawn from a small, stable set such as:

  * `PENDING` — step defined but not yet run or reviewed.

  * `PASS` — step executed, evidence present, and behavior meets expectations.

  * `FAIL` — behavior failure (tests/assertions failed, HTTP surface reachable but incorrect).

  * `FAIL_TOOLING` or `TOOLING_BLOCKED` — step could not be executed or evaluated because required tooling or services were not available (for example pytest missing, CLI entrypoint broken, dev HTTP harness not reachable); see §2.2.5 and §3.5.11 for classification.

Steps may define additional, more granular status fields if needed, but they must not overload `PASS` or `FAIL` to mean tooling problems.

**Log body and supporting artifacts.**

* All tests and checks for a step (pytest output, `grep` blocks, `curl` output, size checks, diff results) **MUST** be appended into the **same** primary log, in a clearly structured order (for example “=== TESTS \===”, “=== INDEX/MIRROR GREPS \===”, “=== MANIFEST GREPS \===”).

* Temporary or helper files created by the step:

  * **SHOULD** use a `tmp_` prefix or a clearly descriptive name (for example `tmp_sampler_request.json`, `tmp_sorted_candidates.txt`), and

  * **SHOULD** be either:

    * co-located with the step log (so their relationship is obvious), or

    * placed under a single `tmp/` subdirectory inside QA\_ROOT when they are purely scratch.

* QA reviewers should always be able to reconstruct **what happened in the step** from the primary log alone (header, commands, rails, test output, greps), using supporting artifacts only as needed for deeper inspection.

**Consolidation and QA quality.**

* A QA run that leaves behind multiple, overlapping logs for the same step (for example `D4-...log`, `step4_...log`, `D1D2-...log` in different folders) without a clear primary log in QA\_ROOT is considered **poor-quality evidence** under PF19.

* To satisfy PF19’s expectations for QA evidence structure:

  * Each step must have **one** clearly named primary log in QA\_ROOT.

  * No step should leave behind “floating” logs in ad hoc subdirectories without a pointer from QA\_ROOT.

  * QA Plans **MUST** reference these primary log filenames explicitly so that operators and reviewers know exactly where to look.

This per-step log structure works together with the mechanical evidence rules (§4.3) and the Live QA patterns (§3.4–§3.6) to make QA runs reproducible, reviewable, and easy to audit: one run root, one primary log per step, clearly labeled headers and statuses, and supporting artifacts where needed.

## **4.5 External AI QA evidence batching (10-file limit, no zips)**

In some workflows, external AI QA reviewers (for example Kronos or other analysis agents) receive evidence via **manual file uploads** from the operator’s environment. That review channel has two hard constraints:

* **Per-batch file limit.** At most **10 files** can be uploaded in a single batch.

* **Zip archives are unreliable.** Zip files are not guaranteed to be unpacked or interpretable by the review tool. Reviewers only see the raw files they are explicitly given.

PF19 requires QA plans and evidence design to **respect these constraints** whenever external AI QA review is expected.

**Channel constraints (normative).**

* For external AI QA review flows:

  * Zip archives **MUST NOT** be relied on as the primary evidence transport. Raw files (text/JSON/etc.) are the only reliable inputs.

  * A single reviewable evidence slice **MUST fit into 10 files or fewer per upload batch**.

  * Reviewers cannot “see a folder”; they only see the files explicitly provided. QA plans must not assume the reviewer can browse directories.

**Step-level evidence sets (≤ 10 files).**

For any QA step or Live QA slice that is expected to be reviewed by an external AI QA persona:

* The QA Plan **MUST** define a **minimal evidence set** for that step that can be captured and reviewed in **10 files or fewer**.

* This minimal set **SHOULD** be explicitly listed in the QA Plan or Live QA Guide, using fully qualified paths (for example `audit/qa/<epic-id>/dev_sampler_http/D3_env_rails.log`).

* When a step naturally produces more than 10 governed artifacts, the QA Plan **MUST**:

  * identify a **priority subset** (≤ 10 files) that captures the essential behavior and rails for external review; and

  * treat any additional files as **optional or follow-up material**, not required for the primary verdict.

**No zip-only evidence.**

* QA Plans **MUST NOT** specify “zip the evidence directory and upload it” as the primary or only way to supply evidence to the reviewer.

* Zips **MAY** be created for local storage or human consumption, but the canonical external-review path **MUST** be through individual files that respect the 10-file limit.

**QA author responsibilities.**

When authors write or revise QA Implementation Plans or Live QA Guides for steps that will go to external AI QA review, they **MUST**:

* name the exact paths and filenames that constitute the minimal evidence set for each such step;

* confirm that the number of files in that set is **10 or fewer**; and

* avoid vague instructions such as “send all logs from this folder” or “upload all JSONL files”; instead, they must name a concrete, bounded set.

These batching rules do not change what local evidence must be captured or how it is indexed; they ensure that every QA step that needs external AI review has a **deterministic, reviewable evidence slice** that fits within the channel’s operational constraints.

## **4.6 Derived AI-readable evidence for HTTP response bodies**

Raw HTTP `.body` files (for example `D3_http_run1.body`, `compat_http_200.body`, `…_prod.body`) are often the **canonical local evidence** for HTTP behavior. PF19 requires those files to be written under `audit/qa/<epic-id>/…` and captured as governed artifacts where applicable. However:

* External AI QA reviewers cannot reliably open or process arbitrary raw `.body` files, and

* The **≤ 10-file** evidence limit for external review (§4.5) makes shipping large sets of `.body` files impractical.

PF19 therefore requires a small, structured, AI-readable **derived artifact** for HTTP-centric steps that will be reviewed by external AI QA.

**Scope.**

This section applies to QA steps that:

* use one or more `*.body` files as **acceptance evidence**, and

* are intended to be reviewed by an external AI QA reviewer.

Raw `.body` files remain the canonical local QA artifacts; derived summaries are **additional** review-layer artifacts.

**Principle.**

* Raw `*.body` files **MUST** continue to be written and preserved under `audit/qa/<epic-id>/…` as specified in QA Plans.

* External AI QA review **MUST** be performed on **small, derived, AI-readable summaries**, **not** on the raw `*.body` files themselves.

**Requirements for derived HTTP review artifacts.**

For each HTTP-centric QA step in scope:

* The QA Plan **MUST** define one or more **derived review artifacts** with all of the following properties:

  * **Location**

    * Stored alongside the `.body` files under the same evidence directory, for example:

      * `audit/qa/<epic-id>/<step-dir>/<step>_http_bodies_review.md`, or

      * `audit/qa/<epic-id>/<step-dir>/<step>_http_bodies_review.json`.

  * **Format**

    * Plain text (Markdown) or JSON only — no binary.

    * Structured enough that an AI can reason about it without seeing the raw bodies (for example simple tables or JSON objects per scenario).

  * **Contents (per scenario / family)**

     For each group of `*.body` files used in acceptance (for example, dev run1/run2, seed 111 vs 222, APP\_ENV=prod vs dev), the derived artifact **MUST** record:

    * A **scenario ID/name** (for example `two_run_identity_dev`, `seed_111`, `seed_222`, `prod_forbidden`).

    * **Source files:** exact filenames of the `*.body` files summarized for that scenario.

    * **HTTP outcome summary** (from the associated headers and QA expectations):

      * status code (for example `200`, `403`, `4xx/5xx`),

      * how the QA Plan treated it (for example “success”, “forbidden”, “error/vendor failure”).

    * **Shape summary:**

      * top-level keys present (for example `["viewer_id","candidate_ids","seed","scores"]` vs `["error","code","message"]`), and

      * a one-line description of whether the body is a sampler JSON payload, a vendor response, or an error envelope.

    * **Key field relationships required by the Plan**, such as:

      * two-run identity: “run1 vs run2 bodies: IDENTICAL / DIFFERENT”;

      * seed-only behavior: “viewer\_id equal? yes/no; candidate\_ids equal? yes/no; changed fields: …”;

      * gating: “prod/unset/empty bodies: sampler JSON? yes/no; error envelope? yes/no”.

    * **Optional but recommended:**

      * a hash (for example SHA-256) for each `.body` file to support identity checks without exposing contents.

* Each HTTP-centric QA step **MUST** limit itself to at most one or two such derived review artifacts so that the entire AI-review evidence set for that step still fits under the **≤ 10-file** constraint (§4.5).

* QA Plans **MUST NOT** require uploading raw `.body` files for external AI review. Raw bodies remain on disk as backing evidence and may be manually inspected by human operators or auditors.

**Guidance for QA Plan authors.**

When writing or updating QA Implementation Plans and Live QA Guides for HTTP-centric steps:

* Explicitly list:

  * the `*.body` files to be produced (local canonical evidence), and

  * the corresponding derived review artifact (for example `<step>_http_bodies_review.md` or `<step>_http_bodies_review.json`), with a short schema describing what must be recorded.

* In any “Evidence for external review” section, reference the derived artifact(s) instead of the raw `.body` files. For example:

  * “External AI QA evidence for Step 2 (dev sampler HTTP Live QA): `D3_env_rails.log`, `D3_http_bodies_review.md`, `D3_live_qa_run.log`, and the priority JSONL summaries; raw `.body` files remain on disk as backing evidence and are not required for external review.”

This derived-evidence requirement does not change the underlying acceptance criteria for HTTP surfaces (those still depend on the actual body content per PF01/PF14/PF20); it adds a **translation layer** between local QA artifacts and external AI review constraints, so that:

* QA Plans remain precise and deterministic,

* operators can keep using full `.body` files locally, and

* external AI reviewers can work with small, structured, privacy-respecting summaries instead of opaque raw payloads.

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

* Each call produced **one resolver+ingest metadata JSON artifact** under `audit/qa/HDE-EPIC017/logs/**` (names-only), which was treated as the primary evidence file for that QA step.

The resolver/ingest metadata for a successful dry-run vendor QA step is expected to show, at minimum:

* **Resolver:** `requested_source="vendor"`, `resolved_source="vendor"`, `allow_network=true`, `safe_mode=false`, `dry_run=true`, `upsert=false`, and `user_id` set to a clearly QA-scoped key (for example `qa_epic017_vendor1`).

* **Ingest:** `provider` (for example `hdapi`), `vendor_version` (version of the vendor schema), a realistic non-zero `duration_ms`, and `rows_written=0`, `db_rows_after=0` for dry-run.

* **Parity & hashing:** `input_fingerprint`, `payload_sha256`, and `db_emitted_sha256` all aligned, with an explicit `parity_match=true` flag indicating that “what came from the vendor” matches “what would be stored in DB shape” under non-dry-run settings.

* **Idempotency:** a composite `idempotency_key` including a UUID, provider, vendor\_version, and the input fingerprint, and a top-level `status="ok"`.

When these conditions are met and the artifact is:

* stored under governed paths (`audit/qa/<EPIC>/logs/**` and, if normalized, under `artifacts/**` or `docs/**`), and

* properly indexed in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` with a co-located path-proof,

PF19 considers the **vendor dry-run ingest requirement** for that EPIC slice satisfied: QA has proven that vendor ingest can be exercised in dry-run mode from Codespaces into Railway prod, that no DB rows are written, and that payload↔DB shape parity is correctly enforced for that call. Deeper idempotence and multi-run behavior remain the domain of future, more automation-focused epics and CI harnesses.

## **5.6 CLI/API & SDKs**

Cross-component; HDE CLI/API contracts and emitter bytes live in **PF05 — HDE-CLI-API-Vendor-Ref** (titles-only). Evidence plumbing for parity artifacts lives in **PF12 — HDE-Schemas & Artifacts** and **PF09 — HDE-Build Checklist**.

### **Intent**

Prove that:

* CLI and SDKs are exact clients of the shared emitters (Reader, Aux).

* AB/BA runs and two-run identity hold for CLI output.

* CLI preview and SDK calls are in parity with the underlying HTTP emitter bytes.

This playbook is about **transport parity and determinism**, not about business logic.

### **Inputs**

A dev or staging environment where:

* CLI is installed and can call HDE/App surfaces.

* SDKs (if present) can call the same routes programmatically.

Env pins for any capture:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

The CLI and SDK commands/entrypoints for:

* compatibility / match display

* any Aux narrative or Reader preview functions

### **Scope**

In scope:

* CLI parity snapshots for a fixed pair (AB and BA).

* Two-run identity of CLI outputs for the same inputs.

* Parity between CLI/SDK outputs and canonical emitter responses (Reader/Aux).

Out of scope:

* UI formatting in terminals beyond what is required for parity proof.

* Non-governed, ad-hoc scripts or experimental SDK functions.

### **Pre-App compat QA note (CLI-only)**

In **pre-App, no-user contexts**, QA uses `hdctl showcompat` with **explicit** `--source=vendor` and synthetic birth tuples (CLI flags and behavior defined in HDE-CLI-API-Vendor-Ref; titles-only) as the **canonical way to exercise live compat behavior**. In this environment:

* `showcompat --source=vendor` with birth arguments and appropriate rails is the **only compat CLI form that counts as a live behavior test**.

* `showcompat` runs that **do not call vendor** (for example, no `--source` flag, or runs under closed rails that never reach vendor) are treated as **local/offline math/serializer checks**:

  * they may be used to prove canonical JSON, determinism, or schema invariants; and

  * they **must** be labeled as **“local/offline (no vendor)”** in QA plans and artifacts and **must not** be used to satisfy tokens whose intent is “live product behavior with vendor rails active”.

* The `person_uid` values under `a` and `b` and any `compat.meta` identity fields in compat JSON are treated as **CLI-local identifiers** in this context (local/dev identity for the CLI session), not as Glow App user IDs and not as authoritative prod engine identity (which is governed by the `/internal/version` ops endpoint on Railway by title).

* Acceptance for this specific compat Live QA step in pre-App mode is **“vendor-backed compat JSON produced via `--source=vendor` for the chosen births”**; AB↔BA identity, Reader envelope proofs, and vendor ingest evidence are covered by separate QA steps and tokens in this playbook and elsewhere in PF19.

---

### **5.6.1 Steps**

1. **Establish a test pair and environment.**

   * Set env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`) for all captures.

   * In **pre-App, no-user contexts** (no app user IDs, no user-bound BodyGraphs):

     * choose **synthetic birth tuples** and CLI-local person labels as test inputs; and

     * treat any CLI `--user` values used during QA as **ephemeral QA keys**, not as real app user IDs.

   * In environments where the app user model is live and user-bound BodyGraphs exist, test IDs may include real user IDs **only** where those surfaces are explicitly defined by an epic in **HDE Phased Epics** (titles-only).

2. **Source selection (explicitness, vendor vs offline).**

   * When a DB/packs-backed BodyGraph exists and app user IDs are live:

     * run CLI **without** `--source=vendor` to exercise DB/packs → expect DB read; **no vendor call** in keys-only logs.

     * any CLI run that uses `--source=vendor` in this context must be called out explicitly in the QA plan as a **vendor-backed behavior test** and must obey the vendor rails and evidence rules defined in PF05/PF04.

   * In **pre-App, no-user contexts** (no DB users / no app user IDs):

     * treat DB-backed, user-ID-dependent flows as **blocked by environment**; do **not** attempt to synthesize app-like user records or rely on `showcompat --user-a/--user-b --source=db` for QA.

     * for **live behavior tests** (compat/Reader behavior in this environment), use **vendor-backed compat**:

       * `showcompat` with birth arguments **and** `--source=vendor` (or an equivalent vendor-only flag defined in HDE-CLI-API-Vendor-Ref); and

       * any invocation that omits explicit vendor source in this context is a **local/offline** check and **cannot** satisfy behavior D-goals or tokens whose intent is “live behavior with vendor rails active”.

     * for **local/offline checks** (serializer/math, canonical JSON, AB↔BA structure, etc.):

       * `showcompat` without `--source` may be used under closed rails or local-only configurations, but **must** be labeled **“local/offline (no vendor)”** in QA plans and artifacts and **must** be routed to determinism/canonicalization tokens, not to live behavior tokens.

   * With `--source=vendor` (or ops `source="vendor"`) in any environment:

     * when rails are open, expect a vendor call; if policy allows, results may be stored for durability in non-prod environments under governed evidence policies.

     * when rails are closed, expect a **typed refusal** (no outbound HTTP). These runs are useful to prove SAFE/rails posture, not live vendor behavior.

3. **Capture CLI AB/BA snapshots.**

   * Produce AB and BA governed outputs (JSON or normalized) for a fixed test pair:

     * in **pre-App** contexts, use **vendor-backed compat** (`showcompat --source=vendor` with birth arguments) as the source of truth for AB/BA behavior runs.

     * in environments with a user model and DB/packs in scope, AB/BA runs may exercise DB/packs or vendor-backed compat depending on the epic; QA plans must label which source is being exercised and whether the run is a **vendor-backed behavior test** or a **local/offline** check.

   * Store artifacts under `artifacts/cli/...` and register them in the Evidence Index and Machine Mirror in the same PR (see §4.2–§4.3).

4. **Check AB/BA parity.**

   * Verify symmetry where required and correct directional swap semantics (for example, personal vs shared narratives).

5. **Check two-run identity.**

   * Re-run AB and BA; outputs must be **byte-identical** for governed parts (no RNG/time/FS/network leakage).

6. **Verify emitter parity (CLI ↔ HTTP).**

   * Baseline against HTTP emitters (Reader/Aux) for at least one direction.

   * Verify structural/semantic parity between CLI output and HTTP response (bands, categories, narratives, and meta).

7. **Error parity (typed errors).**

   * Exercise:

     * a forced DB-unavailable scenario; and

     * a closed-rails vendor attempt (for example `--source=vendor` when `ALLOW_NETWORK=0`),

   * and verify CLI and HTTP error envelopes are aligned (typed, numeric-free) and respect refusal policy.

8. **Update CLI/API evidence indices.**

   * Add/update `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR for all governed CLI/API artifacts.

   * Ensure each Mirror record includes a `proof_anchor` to a co-located path-proof.

---

### **5.6.2 Evidence**

**CLI AB/BA artifacts**

* `artifacts/cli/compat_ab.json`

* `artifacts/cli/compat_ba.json`

* Optional: `artifacts/cli/compat_summary.json`

These should be annotated in the Human Index to indicate whether each run is **vendor-backed** or **local/offline**.

**SDK parity artifacts (if applicable)**

* `artifacts/sdk/python_compat_ab.json`

* `artifacts/sdk/typescript_compat_ab.json`

**Optional HTTP baselines**

* `artifacts/http/reader_compat_ab.json` or

* `artifacts/http/aux_ab.json`

(used internally to verify emitter parity, not necessarily shipped to users.)

**Indexing**

All governed artifacts above must be referenced by:

* `docs/evidence/INDEX.json` (+ `.sha256`), and

* `artifacts/evidence_index.jsonl`

with Human Index descriptions that clearly distinguish **vendor-backed** vs **local/offline** runs (schema in PF12 by title).

---

### **5.6.3 Tokens (names-only)**

Common tokens that gate CLI/API & SDK QA (definitions live in **HDE-Governance** / **HDE-Build Checklist**) include:

* `CLI_AB_BA_PARITY_OK`

* `CLI_TWO_RUN_IDENTITY_OK`

* `CLI_READER_EMITTER_PARITY_OK`

* `CLI_AUX_EMITTER_PARITY_OK`

* `SDK_READER_PARITY_OK`

* `SDK_AUX_PARITY_OK`

* `CLI_ADMIN_BUNDLE_PARITY_OK`

* `ADMIN_BUNDLE_FULL_PAYLOAD_OK`

* `ADMIN_AUTH_REQUIRED_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

---

### **5.6.4 Failures to watch**

* **AB/BA parity failures**

  * CLI outputs for AB and BA differ where they should be symmetric; or

  * directional narratives (for example personal vs shared) fail to swap as expected.

* **Two-run identity failures**

  * CLI outputs differ between repeated runs with identical inputs; or

  * timestamps, RNG, filesystem, or network noise leaks into governed sections.

* **Emitter parity failures**

  * CLI or SDK returns different bands, categories, or narratives than the HTTP emitter; or

  * missing categories or mismatched ordering relative to the emitter.

* **Misuse of `showcompat` in pre-App contexts**

  * Live QA plans that attempt to satisfy behavior tokens using `showcompat` **without** `--source=vendor` in pre-App, no-user environments.

  * QA artifacts that do not clearly label whether a compat run is **vendor-backed** or **local/offline**.

* **SDK-specific inconsistencies**

  * SDKs applying rounding or transformations not present in the emitters; or

  * SDKs silently dropping fields or adding extra computed ones without canonical backing.

* **Evidence hygiene issues**

  * Evidence artifacts added or modified without corresponding updates to the Human Index and Machine Mirror in the same PR.

  * Mirror records without path-proofs, or path-proofs without corresponding Mirror records.

**Normative note:**  
 **Emitter parity is normative.** CLI and SDK outputs **must** be in parity with HDE emitters (Reader/Aux); parity artifacts are governed evidence and must be captured and indexed accordingly.

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

## **5.8 Admin bundle surfaces (CLI & HTTP, HDE-only)**

Cross-component; the admin bundle builder and transport bytes live in **HDE-CLI-API-Vendor-Ref**, **HDE-Mechanics Guide**, and **HDE-Schemas & Artifacts** (titles-only). Auth and logging rails live in **HDE-Governance**; infra endpoints live in **Glow Infrastructure**. PF19 defines how QA proves parity, full payload, and auth for these admin-only surfaces.

### **Intent**

Prove that:

* the admin bundle builder composes the **full product payload** for a single match into one canonical JSON object;

* the **CLI admin bundle** command and the **HTTP admin bundle route** return the **same** admin bundle for the same inputs and admin credential; and

* admin surfaces are **not open**: a full admin bundle cannot be obtained without the configured admin credential, and each successful call is logged as an operations event.

This playbook is about pre-Glow admin/QA access to the full product payload, not about public Reader or App surfaces.

### **Inputs**

* A staging or prod-like environment where:

  * the HD Engine service and DB are reachable on Railway, and

  * the admin bundle HTTP route is deployed.

* A CLI environment (Codespaces or equivalent QA console) configured, via infra canon, to reach the same Railway HD Engine prod service and DB.

* A functioning admin bundle builder and its wiring in CLI and HTTP, as defined in HDE-Mechanics Guide and HDE-CLI-API-Vendor-Ref.

* A **secret admin credential** (token or equivalent) configured per HDE-Governance and Glow Infrastructure (for example in Railway secrets or app config; titles-only).

* Env pins for any governed evidence capture:

  * `LC_ALL=C`

  * `LANG=C`

  * `TZ=UTC`

### **Scope**

In scope:

* The internal admin bundle builder that composes:

  * per-person BodyGraphs for each party (canonical BodyGraph JSON shape),

  * full Magic-10 compat JSON (categories with `{id, score, band, personal_key, shared_key}` and compat meta), and

  * three narratives (Aux compositions with composition IDs and pack SHA) for the match,

  * plus a `meta` block (engine\_tag, release\_id, invocation\_tag or equivalent, bundle source, rails).

* The CLI admin bundle command and HTTP admin bundle route that expose this builder for admin use only.

Out of scope:

* Public Reader JSON envelopes, Aux public text posture, and A7 proofs (covered in other playbooks).

* Any GUI-specific behavior beyond verifying that the Admin GUI calls the admin bundle HTTP route correctly.

### **Steps**

1. **Admin config and handshake.**

   * From a QA console, perform the prod handshake described in §3.5 to confirm connectivity to the Railway HD Engine prod service.

   * Verify that a configured admin credential is present in the environment or configuration used by both CLI and Admin GUI (for example env variable or secret reference, titles-only); do **not** hard-code secrets in the repo.

2. **CLI admin bundle — success path.**

   * With env pins set and the admin credential configured, invoke the admin bundle CLI command for a single match:

     * Pre-Glow: use birth-tuple inputs for both parties (for example a births file or structured birth flags; exact flag names pinned in HDE-CLI-API-Vendor-Ref).

     * Post user-model: use user ID flags only once a PF-level user model is defined and in scope for the epic.

   * Expectations for the CLI call:

     * Exit status indicates success.

     * Output is a canonical JSON object (UTF-8, sorted keys, compact, one trailing LF) written to stdout or a governed output file.

     * Top-level keys include at least: `a_bodygraph`, `b_bodygraph`, `compat`, `narratives`, `meta`.

     * The `compat` section has the full Magic-10 category set and compat meta consistent with established compat surfaces (templates and banding remain governed by math/spec docs, titles-only).

     * The `narratives` array contains exactly three Aux narrative compositions (two private, one shared) with composition IDs and pack SHA.

     * The `meta` block carries engine\_tag, release\_id, invocation\_tag or equivalent identity and rails information appropriate to the environment.

   * Save the CLI admin bundle JSON as a governed artifact under a path such as `artifacts/admin/cli_bundle_<pair>.json`.

3. **HTTP admin bundle — success path.**

   * From the same QA console (or via the Admin GUI), call the admin bundle HTTP route on the Railway HD Engine prod service with the same inputs and admin credential as the CLI call:

     * Pre-Glow: birth-tuple-based request body.

     * Post user-model: user ID-based request body (once defined by epic canon).

   * Expectations for the HTTP call:

     * Response status is 200\.

     * `Content-Type` is JSON (`application/json; charset=utf-8` or equivalent per HDE-CLI-API-Vendor-Ref).

     * Response body is a canonical JSON object with the same top-level structure and semantics as the CLI admin bundle.

   * Save the HTTP admin bundle JSON as a governed artifact under a path such as `artifacts/admin/http_bundle_<pair>.json`.

4. **CLI ↔ HTTP admin bundle parity.**

   * Normalize both admin bundle JSON artifacts via the canonical serializer (for example pretty-print with sorted keys, titles-only tooling).

   * Compare the CLI and HTTP admin bundles for the same inputs:

     * All top-level keys and their nested content match, modulo any explicitly documented transport-only metadata.

     * In particular, the BodyGraphs, compat categories and meta, narratives (IDs, pack SHA, and text), and meta identity values are identical.

   * Record the result of this comparison (for example as `artifacts/admin/bundle_parity_<pair>.json` or a small parity log) and include it in the evidence skeleton.

5. **Auth gating — negative tests.**

   * Attempt to call the CLI admin bundle command **without** the admin credential (or with an invalid credential):

     * Expect a non-zero exit code and a typed authentication or authorization error.

     * Expect no full admin bundle JSON on stdout or in any governed output file.

   * Attempt to call the HTTP admin bundle route without the admin credential (or with an invalid credential):

     * Expect a typed 401/403-style response per HDE-Governance and HDE-CLI-API-Vendor-Ref.

     * Expect no full admin bundle JSON in the response body.

   * Capture these negative runs as governed evidence (for example small logs or JSON error samples) under `artifacts/admin/auth_negative/**`.

6. **Logging and audit.**

   * For at least one successful CLI and one successful HTTP admin bundle call, verify that:

     * an operations log entry is written, including:

       * timestamp,

       * who/what called it (CLI vs GUI and user/account label or identifier),

       * high-level input description (for example “birth-based match for two anon parties” or, post user-model, `user_a_id` and `user_b_id`), and

       * a correlation ID or trace identifier.

     * logs are **keys-only** and do not contain raw birth data, secrets, or unnecessary PII.

   * Store a redacted sample of these logs (if allowed by governance) under `artifacts/admin/logs.sample` as governed evidence, or record their existence and location via a path-proof-only record if log content must not be replicated.

7. **Evidence and indexing.**

   * Register all governed admin-bundle artifacts (CLI bundle, HTTP bundle, parity proof, auth-negative samples, and any log samples) in:

     * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

     * `artifacts/evidence_index.jsonl`

   * in the **same PR** that adds or refreshes them.

   * Ensure each mirror record has a `proof_anchor` pointing to a co-located `*.path_proof.txt` for the corresponding artifact.

### **Evidence**

Typical governed evidence for this playbook includes:

* `artifacts/admin/cli_bundle_<pair>.json` — CLI admin bundle.

* `artifacts/admin/http_bundle_<pair>.json` — HTTP admin bundle.

* `artifacts/admin/bundle_parity_<pair>.json` or equivalent small parity proof.

* `artifacts/admin/auth_negative_cli_<pair>.json` and `artifacts/admin/auth_negative_http_<pair>.json` — negative auth samples.

* Optional `artifacts/admin/logs.sample` — redacted operations log sample.

* Updated entries in:

  * `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`), and

  * `artifacts/evidence_index.jsonl`,

* with mirror records and path-proofs for each governed artifact.

### **Tokens (names-only)**

This playbook primarily satisfies:

* `CLI_ADMIN_BUNDLE_PARITY_OK` — CLI and HTTP admin bundles match for the same inputs and admin credential.

* `ADMIN_BUNDLE_FULL_PAYLOAD_OK` — admin bundle contains all required structural elements (BodyGraphs, compat, three narratives, meta) as defined in the owning PF docs.

* `ADMIN_AUTH_REQUIRED_OK` — admin surfaces do not yield an admin bundle without the configured admin credential; unauthenticated/mis-authenticated calls return typed errors only.

It also consumes the generic evidence tokens:

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

### **Failures to watch**

* CLI admin bundle succeeds but:

  * is not canonical JSON (wrong encoding, unsorted keys, missing final LF), or

  * is missing any of the required structural elements (BodyGraphs, compat, narratives, meta).

* HTTP admin bundle succeeds but:

  * diverges from the CLI bundle for the same inputs, or

  * lacks expected headers or content type.

* Admin surfaces return a full admin bundle when:

  * no admin credential is presented, or

  * an invalid or revoked credential is used.

* Operations logs are missing, lack correlation IDs, or contain raw birth data, secrets, or unnecessary PII.

* Admin-bundle evidence artifacts are created or updated without corresponding Human Index and Machine Mirror updates in the same PR, or without path-proofs.

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

  # **8\. Evidence & indexing reference (quick rules)**

* **Header names lower-case.** All governed header snapshots store header names in **lower-case**; values are verbatim. *Acceptance token:* `SNAPSHOT_HEADER_LOWERCASE_OK` (definition lives in PF05/PF09).

* **Directory names lower-case (governed roots).** All **new directories** created under governed roots **MUST** use **all-lower-case** directory names. This applies at minimum to:

  * `audit/` (including `audit/qa/<epic-id>/...` and its subtrees),

  * `docs/**`, and

  * `artifacts/**`.

* Introducing mixed-case or upper-case directory names anywhere under these roots is a **QA failure**, not cosmetic drift; such directories **MUST** be renamed to lower-case and any affected evidence paths updated (Index, mirror, and path-proofs) before QA tokens depending on those artifacts can be claimed.

* **Gitignore rails for QA roots.** Canonical QA evidence roots under `audit/qa`, including all per-epic trees such as `audit/qa/hde-epic018`, **MUST NOT** be hidden by `.gitignore`. Broad ignore patterns that match `audit/qa/**` are **forbidden** unless they are explicitly paired with allow rules that keep all per-epic QA evidence trees (`audit/qa/<epic-id>/...`) visible to git. When a new `audit/qa/<epic-id>` tree is introduced, the build/infra owner **MUST** ensure that `.gitignore` either (a) has no entries that match `audit/qa` at all, or (b) includes explicit allow patterns that prevent canonical QA trees from being ignored while still allowing narrowly targeted ignores for non-evidence scratch files. Older ignore patterns for `Audit/QA` or `audit/qa` **MUST** be reviewed and removed or tightened if they conflict with the canonical `audit/qa/<epic-id>/...` evidence convention.

* **Same-PR rule.**  
   The **Human Index** (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the **Machine Mirror** (`artifacts/evidence_index.jsonl`) **MUST** be updated in the **same PR** as any new or changed evidence artifacts.

* **Single-file machine mirror.** `artifacts/evidence_index.jsonl` is the **only** mirror file; canonical JSONL; one LF per record; fixed field order; **unknown-key reject**; each record includes a `proof_anchor`.

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
  * 

---

# **9\. QA acceptance tokens**

## **9.1 Tokens glossary (names-only; sources in PF04/PF09)**

PF19 lists **names only** in this glossary. Token spellings and normative definitions live in **HDE-Governance** and **HDE-Build Checklist** (titles-only). Use this section as a quick reference; QA-facing definitions and evidence mapping live in §9.2.

### **9.1.1 Pre-commit**

* `QA_PRECOMMIT_CHECKLIST_OK`

* `DET_SERIALIZER_OK`

* `TWO_RUN_IDENTITY_OK`

* `AB_BA_IDENTITY_OK`

### **9.1.2 Post-commit (general)**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_MIRROR_OK`

* `EVIDENCE_PATHS_VALIDATED_OK`

* `EVIDENCE_PATH_PROOFS_OK`

* `CI_CHECK_MIRROR_SCHEMA_OK`

* `CI_CHECK_FINAL_LF_OK`  
* `EVIDENCE_LEDGER_AGENT_READABLE_OK`

### **9.1.3 Aux**

* `NARR_200_TEXT_OK`

* `NARR_SUPPRESSED_NO_ETAG_OK`

* `COMPOSE_IDS_DETERMINISM_OK`

* `ENV_LC_ALL_C_OK`

* `NARR_VARY_AUTH_AE_OK`

### **9.1.4 Catalog/A7**

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

### **9.1.5 CLI/API & SDKs**

* `CLI_AB_BA_PARITY_OK`

* `CLI_TWO_RUN_IDENTITY_OK`

* `CLI_READER_EMITTER_PARITY_OK`

* `CLI_AUX_EMITTER_PARITY_OK`

* `SDK_READER_PARITY_OK`

* `SDK_AUX_PARITY_OK`

* `CLI_ADMIN_BUNDLE_PARITY_OK`

* `ADMIN_BUNDLE_FULL_PAYLOAD_OK`

* `ADMIN_AUTH_REQUIRED_OK`

### **9.1.6 Build/CI (PF09)**

* `QA_FLAKY_TEST_QUARANTINE_OK`

* `DETERMINISM_ENV_PINS_OK`

* `ENV_RAILS_POLICY_OK`

* `SANITY_PIPELINE_OK`

* `CONFIG_REGISTRY_OK`

* `CONFIG_MAGIC10_OK`

* `CONFIG_BUNDLES_DETERMINISTIC_OK`

### **9.1.7 App FE/BE (App QA docs)**

* `APP_FE_WCAG_AA_OK`

* `APP_FE_WEB_VITALS_OK`

* `APP_SEC_ASVS_MIN_OK`

*Note: App-layer token semantics live in App QA and security governance docs (titles-only); PF19 lists names only.*

---

## **9.2 QA Acceptance Tokens Registry (canonical QA token library)**

### **9.2.1 Intent**

This registry is the **single QA-level home** for acceptance tokens used across Engine, App, CI, transport, and evidence proofs. PF19 **does not** redefine transport bytes, schemas, or governance semantics; those remain in their single homes (**HDE-Governance**, **HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**, **HDE-Build Checklist**, **HDE Narratives Guide**, **HDE Phased Epics**, titles-only).  
 The registry provides QA-oriented descriptions: **scope**, **owner PF doc**, **what must be proven**, and **which evidence satisfies each token**.

### **9.2.2 Token metadata model (normative)**

Each QA acceptance token in this registry includes:

* **Name** — canonical spelling of the token (source of truth).

* **Owner PF (titles-only)** — the PF document that owns normative semantics (e.g. HDE-Governance, HDE-Build Checklist, HDE-Schemas & Artifacts, HDE-CLI-API-Vendor-Ref, HDE Narratives Guide, HDE Phased Epics).

* **Scope** — pre-commit, post-commit/live QA, evidence, transport/A7, App-layer, or multi-scope.

* **QA definition (1–3 sentences)** — what QA must prove for the token to be satisfied.

* **Evidence mapping** — the governed artifacts and checks required for satisfaction (titles-only).

**Central registry and naming rules (normative).**

* PF19’s registry is the **single QA-level home** for QA Acceptance Tokens. Tokens may be used in PF docs, epic acceptance maps, manifests, and QA plans **only** by the canonical name recorded here. Local aliases, abbreviated spellings, or epic-specific “helper names” for the same semantics are **forbidden**: acceptance maps, manifests, and QA plans **MUST NOT** invent new token names or synonyms.

* Normative governance semantics (writers/refusals policy, A7 semantics, App security posture, build/CI semantics) continue to live in their owning PF docs (typically **HDE-Governance**, **HDE-Build Checklist**, **HDE-Schemas & Artifacts**, **HDE-CLI-API-Vendor-Ref**, **HDE Narratives Guide**, **HDE Phased Epics**). PF19’s registry defines the QA-facing interpretation and evidence mapping for each token; it does **not** override the underlying governance semantics.

* If an epic or plan discovers that a new QA behavior needs a token (for example a new CLI guard, a new evidence family, or a new Live QA rail), that need **MUST** be recorded as a PF19 doc delta and resolved in this registry **before** the token is treated as live in any acceptance map or manifest. Using “example” or provisional token names in epic documentation (`e.g.`, `TBD`, or partial spellings) is permitted only while the PF19 doc delta is explicitly open; no epic or plan may claim acceptance on a token that does not yet have a canonical entry in this registry.

This metadata model is authoritative for QA planning and EPIC acceptance.

---

### **9.2.3 Pre-commit / CI QA tokens**

**QA\_PRECOMMIT\_CHECKLIST\_OK**

*Owner PF:* HDE-Build Checklist  
 *Scope:* Pre-commit  
 *QA definition:* All required pre-commit checks (lint/format, canonical JSON/JSONL, determinism, env pins, mirror quick-check) have passed.  
 *Evidence:* CI logs and artifacts showing the PF09 pre-commit harness ran successfully (lint/format jobs, canonicalization checks, determinism suites, mirror quick-checks).

**DET\_SERIALIZER\_OK**

*Owner PF:* HDE-Mechanics Guide  
 *Scope:* Pre-commit  
 *QA definition:* The Engine serializer/composer emits byte-stable canonical JSON under determinism env pins.  
 *Evidence:* Two-run identity proofs for serializer outputs (governed JSON artifacts under `artifacts/**`), with matching Index/Mirror records and path-proofs.

**TWO\_RUN\_IDENTITY\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Mechanics Guide  
 *Scope:* Pre-commit  
 *QA definition:* Re-running the same CLI/API/Engine invocation yields identical governed bytes.  
 *Evidence:* Paired canonical JSON or bytes artifacts (for example `compat_ab.json` and a second-run copy) stored under `artifacts/**`, plus matching entries in the Human Index and Machine Mirror.

**AB\_BA\_IDENTITY\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Mechanics Guide  
 *Scope:* Pre-commit  
 *QA definition:* AB and BA runs swap directional attributes correctly without unintended structural differences.  
 *Evidence:* `compat_ab.json` and `compat_ba.json` where non-directional fields match and directional fields swap as expected, with path-proofs and Mirror records aligned.

**DETERMINISM\_ENV\_PINS\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Governance  
 *Scope:* Pre-commit / CI  
 *QA definition:* All determinism-sensitive suites (serializer invariance, evidence ordering, orientation demo, and related invariance tests) run under **closed determinism rails**: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, as defined in Governance and wired via CI.  
 *Evidence:* CI job configuration and an env-check harness (for example `ci/checks/check_env_pins.sh`) showing these pins are exported and enforced, plus a governed env-rails log (for example `audit/gates/determinism/env_pins.log` \+ path-proof and Index/Mirror entries) recording the determinism env posture for the suites that ran.

**ENV\_RAILS\_POLICY\_OK**

*Owner PF:* HDE-Governance / HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Pre-commit / CI  
 *QA definition:* The determinism env rails **policy and implementation** are present and coherent: the canonical env pins are encoded in a single helper/module, enforced by tests, and captured as governed evidence tying CI posture to determinism-sensitive work.  
 *Evidence:* Combined proof that:

* a single canonical helper/module (for example `engine/runtime/determinism_env.py`, titles-only) defines the determinism env pins and is used by invariance/determinism tests;

* invariance tests (for example under `tests/invariance/**`, titles-only) fail closed when pins are missing or mismatched and exercise log rendering/verification behavior; and

* the env-rails log artifact (for example `audit/gates/determinism/env_pins.log` \+ path-proof) is present, canonical JSON, indexed in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`, and consistent with the CI env posture enforced by the env-check script.

These determinism env tokens work together with the general env-pin and evidence rules in §0.4.3, §2.2, and §4.3 to ensure determinism-sensitive QA always runs under a well-defined, audited env rails posture.

---

### **9.2.4 Evidence skeleton & sanity tokens**

**EVIDENCE\_INDEX\_UPDATED\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Pre-commit & post-commit  
 *QA definition:* Any change to governed evidence is accompanied by same-PR updates to the Human Evidence Index and the Machine Mirror.  
 *Evidence:* Updated `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`, with co-located path-proofs for all governed artifacts in the same PR.

**EVIDENCE\_INDEX\_HASH\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Pre-commit & post-commit  
 *QA definition:* The Human Evidence Index hash sentinel and the Machine Mirror body digest both reflect the **current** committed evidence index and mirror contents, as defined by PF12 Evidence Index & Machine Mirror semantics.  
 *Evidence:* A successful run of the canonical evidence-index check (for example `python tools/evidence/update_evidence_index.py --check`, titles-only) under closed rails, with no reported mismatches for the index hash sentinel or mirror body hash.

**MACHINE\_MIRROR\_UPDATED\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Pre-commit & post-commit  
 *QA definition:* The Machine Mirror and its self-record are coherent with the current set of governed artifacts and path-proofs: every mirror record has a matching index entry and path-proof, and the self-record for `artifacts/evidence_index.jsonl` reflects the current mirror body digest and size according to PF12 semantics.  
 *Evidence:* Successful combined runs of the canonical evidence-index and orientation checks (for example `update_evidence_index.py --check` and `orientation_demo.py --check`, titles-only) under closed rails, with no reported SHA/size mismatches or missing path-proofs.

**EVIDENCE\_PATHS\_VALIDATED\_OK**

*Owner PF:* HDE-Schemas & Artifacts  
 *Scope:* Evidence  
 *QA definition:* All governed artifacts have valid path-proofs with matching `sha256` and `size_bytes` and satisfy the monotone `mtime_utc` rules defined in PF12.  
 *Evidence:* Path-proof files and mirror-schema quick-check logs showing each governed artifact has exactly one consistent `path`/`sha256`/`size_bytes` triple and a valid `mtime_utc`.

**EVIDENCE\_LEDGER\_AGENT\_READABLE\_OK**

*Owner PF:* HDE-Governance / HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Evidence / post-commit

*QA definition:* Baseline HD Engine evidence for the epic or change set is captured in a **text-based evidence ledger** that is suitable for review by humans and Codex/ChatGPT-class agents: the Human Evidence Index, the Machine Mirror, any evidence bundle manifests, and key QA logs/step transcripts exist as plain-text files under governed paths and collectively expose the payloads and relationships required to reason about the associated QA Acceptance Tokens. Pure contract or token-only families are used **only** where the evidence consumer does not need to inspect payload contents; wherever payload inspection is required, at least one governed text artifact (for example a bundle manifest, QA log, or summary) must be present in the ledger for that token.

*Evidence:* Proof that, for the HD Engine surfaces and tokens in scope for the epic or plan:

* governed text artifacts exist under `docs/**`, `artifacts/**`, and/or `audit/**` (for example `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, bundle manifests, and per-step QA logs) and are wired into the Evidence Index and Machine Mirror according to **HDE-Schemas & Artifacts** and **HDE-Build Checklist**;

* any binary/compressed evidence bundles referenced by acceptance maps or manifests are paired with at least one governed text artifact that enumerates or summarizes their contents at the ledger level; and

* there are no QA Acceptance Tokens in scope whose satisfaction relies solely on non-textual or opaque artifacts when PF19 expects agent-readable payload inspection.

As with other tokens in this section, concrete schemas, bundle mechanics, and CI gates remain defined in **HDE-Schemas & Artifacts** and **HDE-Build Checklist**; PF19 defines the QA-facing condition that the HD Engine evidence ledger remains text-based and agent-readable at the PR level.

**CI\_CHECK\_MIRROR\_SCHEMA\_OK**

*Owner PF:* HDE-Schemas & Artifacts / HDE-Build Checklist  
 *Scope:* Evidence  
 *QA definition:* The machine mirror conforms to schema: pinned field order, one LF per record, canonical JSONL form, and unknown-key rejection, as enforced by PF12 mirror schema and PF09 CI wiring.  
 *Evidence:* CI mirror-schema verification artifacts for `artifacts/evidence_index.jsonl` showing all records pass schema validation and no unknown keys are present.

**CI\_CHECK\_FINAL\_LF\_OK**

*Owner PF:* HDE-Build Checklist  
 *Scope:* Pre-commit / Evidence  
 *QA definition:* All governed text artifacts end with exactly one trailing linefeed (one LF and no extras).  
 *Evidence:* CI logs or a dedicated LF-check harness that scans governed paths and confirms the one-LF rule for all relevant files.

**SANITY\_PIPELINE\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Governance

*Scope:* Pre-commit / CI (evidence skeleton)

*QA definition:* A **closed-rails sanity pipeline entrypoint** runs a deterministic sequence of checks over the evidence skeleton and determinism rails (serializer determinism tests, env pins checks, CLI serializer/emitter guards, and PF12 evidence index/mirror/path-proof checks) and completes successfully, producing a governed sanity log that reflects a fully coherent skeleton. `SANITY_PIPELINE_OK` is a **composite CI token** that assumes the underlying evidence tokens in this subsection are satisfied.

*Evidence:* Proof that:

* a dedicated sanity pipeline command (titles-only; for example `tools/evidence/run_sanity_pipeline.py`) is run under closed rails in CI;

* the pipeline log artifact (for example `artifacts/sanity/sanity.log`) and its path-proof exist, are canonical, and are indexed in `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`) and `artifacts/evidence_index.jsonl` with a `proof_anchor` pointing at the path-proof; and

* the pipeline log shows a PASS outcome (for example a `summary:PASS` line) for all configured steps, with any failure treated as a CI failure that blocks tokens such as `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and `CI_CHECK_MIRROR_SCHEMA_OK` until the skeleton is brought back into coherence.

**Live QA note (mechanics smoke tests).**

* When the sanity pipeline (or its component scripts) are run in **Live QA** (for example from an open-rails Codespace during an epic’s D3/D4 steps), those invocations are treated as **mechanics smoke tests**, not as the canonical satisfaction of `SANITY_PIPELINE_OK`.

* In this Live QA context, if the pipeline or a component script exits non-zero:

  * QA **MUST** capture logs and exit codes mechanically under `audit/qa/<epic-id>/…` (for example `d3-cli-guards` or `d4-sanity` subtrees);

  * QA **MUST** cross-check CI/closed-rails status for `SANITY_PIPELINE_OK` and related evidence tokens; and

  * reviewers should treat the result as a **QA finding** (for example “env mismatch” or “harness not wired for open rails”), not automatically as an epic-blocking failure.

* An epic’s acceptance roster in **HDE Phased Epics** **may** explicitly tie additional acceptance to a green **Live QA** run of the sanity pipeline. Only in that case should a non-zero Live QA result be treated as blocking acceptance for that epic; otherwise, the canonical satisfaction of `SANITY_PIPELINE_OK` continues to come from closed-rails CI evidence.

**CONFIG\_REGISTRY\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts  
 *Scope:* Pre-commit / CI (config \+ evidence)  
 *QA definition:* The canonical registry report (`registry.registry_report`) is generated under closed rails via the hardened registry/config generator, is canonical JSON, exhibits two-run identity, and is wired into the evidence skeleton and config acceptance map as the single source of truth for registry configuration.  
 *Evidence:* Proof that:

* the registry report artifact (for example `artifacts/registry/registry_report.json`) exists, is produced by the canonical generator under closed rails and serialized via the shared serializer, and is canonical JSON (sorted keys, compact separators, single trailing LF);

* the registry report passes its determinism and invariants tests (for example tests that check two-run identity, schema `registry_report.v1`, and expected coverage of registry entries); and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` contain a `registry.registry_report` entry with matching `sha256`, `size_bytes`, and `proof_anchor` to `artifacts/registry/registry_report.json.path_proof.txt`, and the config acceptance map (for example `audit/EPIC-018_config_acceptance_map.json`) references this artifact key and tokens in a canonical, validated way.

**CONFIG\_MAGIC10\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
 *Scope:* Pre-commit / CI (config \+ evidence)  
 *QA definition:* The Magic-10 and band-edges configs (`config.magic10`, `config.band_edges`) are generated under closed rails via the hardened registry/config generator, are canonical JSON, satisfy the Magic-10 and band invariants defined in the math/mechanics specs, and are wired into the evidence skeleton and config acceptance map as governed configuration artifacts.  
 *Evidence:* Proof that:

* the Magic-10 and band-edges artifacts (for example `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json`) exist, are produced by the canonical generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;

* config tests pass that validate domain invariants (for example Magic-10 order and caps cover the frozen category set with integer bounds and seed metadata, and band edges are sorted, span the clamp range, and match the Engine’s band definitions); and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` include `config.magic10`, `config.band_edges`, and the config acceptance map entry (for example `epic018.config.acceptance_map`), each with matching path-proofs, `sha256`, and `size_bytes`, and with references from the acceptance map to real artifact keys, known tokens (including `CONFIG_MAGIC10_OK` / `CONFIG_REGISTRY_OK`), and existing tests.

**CONFIG\_BUNDLES\_DETERMINISTIC\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
 *Scope:* Pre-commit / CI (config bundles \+ evidence)  
 *QA definition:* Typed frontend and backend config bundles (`config_bundle.fe`, `config_bundle.be`) are generated under closed rails from the governed config artifacts and registry loader, serialized via the canonical JSON emitter, satisfy two-run identity, and carry a `sources` block that links each bundle back to the precise digests and sizes of its upstream config artifacts and registry report.  
 *Evidence:* Proof that:

* the FE and BE bundle artifacts (for example `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`) exist, are produced by the canonical bundle generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;

* bundle tests pass that validate two-run identity, JSON structure, and domain invariants (for example tests under `tests/config/test_typed_bundles.py`, titles-only) and confirm that bundle contents (Magic-10, band edges, channels/centers/domains/alias policy for BE, slimmed bundle for FE) match the governed config artifacts and registry report; and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` include `config_bundle.fe` and `config_bundle.be` entries with matching `sha256`, `size_bytes`, and `proof_anchor` values pointing to their `.path_proof.txt` siblings, and that each bundle’s `sources` block lists only real governed artifacts with digests and sizes that match the evidence skeleton.

---

### **9.2.5 Transport / A7 tokens**

(Transport/A7 tokens, e.g. `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`, retain their existing QA definitions and evidence mapping: Reader Catalog JSON success posture, strong quoted ETag, HEAD/304 behavior, Vary headers, encoding invariance, and composite A7 proof artifacts. Text from prior PF19 remains, with numbering updated under §9.2.5.)

---

### **9.2.6 Aux & narrative tokens**

(Aux/narrative tokens, e.g. `NARR_200_TEXT_OK`, `NARR_SUPPRESSED_NO_ETAG_OK`, `COMPOSE_IDS_DETERMINISM_OK`, retain their existing QA definitions and evidence mapping: Aux text/suppression snapshots, ETag posture, and composition determinism. Text from prior PF19 remains, with numbering updated under §9.2.6.)

---

### **9.2.7 CLI/API & SDK tokens**

Existing CLI/API & SDK tokens such as `CLI_SHOWCOMPAT_CANON_OK`, `CLI_READER_EMITTER_PARITY_OK`, `CLI_STDOUT_LF_OK`, `SDK_READER_PARITY_OK`, and `SDK_AUX_PARITY_OK` retain their prior QA definitions and evidence mapping: canonical CLI JSON, emitter parity, stdout LF posture, and SDK parity artifacts, with normative semantics owned by **HDE-Governance**, **HDE-Build Checklist**, **HDE-CLI-API-Vendor-Ref**, and **HDE-Schemas & Artifacts** (titles-only).

**CLI\_SHOWCOMPAT\_CANON\_OK (environment semantics)**

*Owner PF:* HDE-CLI-API-Vendor-Ref / HDE-Governance / HDE-Build Checklist

*Scope:* Pre-commit / CI / Live QA (compat behavior via CLI)

*QA definition:* `CLI_SHOWCOMPAT_CANON_OK` asserts that `hdctl showcompat` behaves canonically for compat display in the **environment declared as canonical for the epic**:

* it produces governed compat JSON in the expected shape (categories, bands, scores, meta) for a fixed pair;

* it respects the environment’s source-selection rules (DB/packs vs vendor) as defined in PF05 and PF19 (§3.3, §5.6); and

* it exhibits two-run identity and, where applicable, AB↔BA parity for governed parts.

*Environment expectations:*

* In **pre-App, no-user contexts** (no app user IDs, no user-bound BodyGraphs), the only reliable source of **live compat behavior** is the **vendor**:

  * Live behavior tests that aim to satisfy `CLI_SHOWCOMPAT_CANON_OK` **MUST** use `showcompat` with birth arguments **and** `--source=vendor` (or the equivalent vendor-only flag defined in HDE-CLI-API-Vendor-Ref), with rails set according to Governance/Infra for vendor access.

  * `showcompat` runs that do **not** call vendor (for example no `--source` and closed rails, or purely local serializer paths) are treated as **local/offline math/serializer checks**; they may satisfy determinism/canonicalization tokens but **cannot** satisfy `CLI_SHOWCOMPAT_CANON_OK` as a **live behavior** token in pre-App mode and must be labeled “local/offline (no vendor)” in QA plans and artifacts.

* In environments where the **app user model is live** and user-bound BodyGraphs exist:

  * EPIC acceptance rosters in **HDE Phased Epics** **MUST** declare which environment is canonical for `CLI_SHOWCOMPAT_CANON_OK`:

    * **dev harness mode** (for example closed-rails harness calling a dev engine), or

    * **vendor-backed engine mode** (for example CLI calling a Railway engine with vendor rails open), or

    * a combination where dev harness is used for determinism/canonicalization and vendor-backed routes are used for live behavior.

  * QA plans must clearly label each `showcompat` run as:

    * **“canonical behavior env”** (counts toward `CLI_SHOWCOMPAT_CANON_OK` for that epic), or

    * **“local/offline”** (determinism/canonicalization only), and must not conflate the two.

*Evidence:*

* Governed compat JSON artifacts from `hdctl showcompat` runs in the declared canonical environment for the epic, stored under `artifacts/cli/**` (for example `artifacts/cli/compat_ab.json`, `artifacts/cli/compat_ba.json`, and an optional `compat_summary.json`), with:

  * AB↔BA parity proofs where required;

  * two-run identity proofs for the canonical environment; and

  * Index/Mirror records and path-proofs in the same PR.

* A short planning or acceptance note (for example in **HDE Phased Epics** or a `d0-*` planning artifact under `audit/qa/<epic-id>/d0-planning/`) stating which environment(s) are treated as canonical for `CLI_SHOWCOMPAT_CANON_OK` in that epic.

In addition, PF19 introduces the following **admin-bundle tokens** in the CLI/API & SDK family:

**CLI\_ADMIN\_BUNDLE\_PARITY\_OK**

*Owner PF:* HDE-CLI-API-Vendor-Ref / HDE-Mechanics Guide

*Scope:* Post-commit / Live QA (CLI/API, admin surfaces)

*QA definition:* For a given match and admin credential, the CLI admin bundle command and the HTTP admin bundle route both call the canonical admin bundle builder and return **byte-identical** admin bundle JSON objects. No CLI-only or HTTP-only fields appear in the admin bundle payload, and any transport-level differences (for example HTTP headers) are outside the bundle JSON.

*Evidence:*

* A pair of governed admin bundle artifacts for at least one test match:

  * `artifacts/admin/cli_bundle_<pair>.json` (CLI), and

  * `artifacts/admin/http_bundle_<pair>.json` (HTTP),

* produced under determinism env pins from the same QA console, both using a valid admin credential.

* A small parity artifact (for example `artifacts/admin/bundle_parity_<pair>.json` or an equivalent diff/proof) demonstrating structural and byte equality of the two JSON bundles after canonical re-serialization.

* Indexed entries for all three artifacts in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl`, each with a co-located path-proof and a Mirror record whose `proof_anchor` points at that proof.

**ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK**

*Owner PF:* HDE-Mechanics Guide / HDE-Schemas & Artifacts / HDE Narratives Guide

*Scope:* Post-commit / Live QA (admin bundle content)

*QA definition:* The admin bundle builder composes the **full product payload** for a single match into one JSON object. For each tested match, the admin bundle contains, at top level, at least `a_bodygraph`, `b_bodygraph`, `compat`, `narratives`, and `meta`, where:

* `a_bodygraph` and `b_bodygraph` are canonical BodyGraph JSON objects for each party (shape and mechanics per HDE-Mechanics Guide and HDE-Schemas & Artifacts);

* `compat` is the full Magic-10 compat result (category set, scores, bands, and compat meta) consistent with existing compat surfaces (titles-only);

* `narratives` is an array of exactly three Aux narrative compositions (two private, one shared) with composition IDs and pack SHA; and

* `meta` carries `engine_tag`, `release_id`, `invocation_tag` or equivalent, and bundle source/rails metadata.

No required component may be silently omitted or replaced with a placeholder.

*Evidence:*

* At least one governed admin bundle artifact (for example `artifacts/admin/cli_bundle_<pair>.json`) per test match, produced via the canonical admin bundle builder under determinism env pins.

* A QA harness or test that validates:

  * presence of the required top-level keys (`a_bodygraph`, `b_bodygraph`, `compat`, `narratives`, `meta`);

  * that `narratives` has length 3 and each element carries composition IDs and pack SHA; and

  * that the BodyGraph, compat, and narratives sections are consistent with their respective single-home surfaces (for example by cross-checking against separate BodyGraph/compat/narrative QA artifacts for the same match).

* Indexed entries and path-proofs for the admin bundle artifacts and any validation logs in the Human Index and Machine Mirror, in the same PR.

**ADMIN\_AUTH\_REQUIRED\_OK**

*Owner PF:* HDE-Governance

*Scope:* Post-commit / Live QA (auth & logging for admin surfaces)

*QA definition:* Neither the CLI admin bundle command nor the HTTP admin bundle route will return a full admin bundle JSON object unless the configured admin credential is presented. Unauthenticated and mis-authenticated attempts yield typed authentication/authorization errors only, and each successful admin bundle call is logged as an operations event with timestamp, caller identity (CLI vs GUI and user/account label), a high-level description of the inputs, and a correlation ID, in accordance with HDE-Governance logging and PII rules.

*Evidence:*

* Successful admin bundle runs (CLI and HTTP) for at least one test match with a valid admin credential, as described under `CLI_ADMIN_BUNDLE_PARITY_OK` and `ADMIN_BUNDLE_FULL_PAYLOAD_OK`.

* Negative auth runs:

  * CLI invocations of the admin bundle command without a credential and with an invalid credential, captured as governed artifacts (for example `artifacts/admin/auth_negative_cli_<pair>.json`) showing non-zero exit codes and typed auth errors, with no admin bundle JSON present.

  * HTTP invocations of the admin bundle route without a credential and with an invalid credential, captured as governed artifacts (for example `artifacts/admin/auth_negative_http_<pair>.json`) showing appropriate error status and typed error bodies, with no admin bundle JSON present.

* At least one redacted sample (or a path-proof-only record) demonstrating that successful admin bundle calls are logged with timestamp, caller identity, high-level input description, and correlation ID, and that logs are keys-only and free of raw birth data and secrets.

* Indexed entries and path-proofs for the negative auth artifacts and any log samples in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR as the admin bundle QA evidence.

---

### **9.2.8 App-layer QA tokens**

App-layer QA tokens are **named** here, but their normative definitions live in App QA governance/security docs (titles-only). PF19 does not define App-layer behavior; it only expects App-layer QA plans to map App tokens into this registry by name.

---

### **9.2.9 EPIC → token mapping (QA routing rule)**

For every EPIC in **HDE Phased Epics** (titles-only), the EPIC acceptance roster **must**:

* list required QA tokens **by canonical name** from this registry;

* not redefine or override token semantics; and

* provide evidence pointers (titles-only) showing how the EPIC satisfies each token.

---

### **9.2.10 Forward plan**

Outstanding work includes:

* extracting EPIC017 QA tokens fully into this registry where not already captured;

* backfilling definitions and evidence mapping for any missing canonical tokens; and

* updating HDE Phased Epics so EPIC entries point to this registry rather than duplicating token semantics.

This registry is now the single QA-level home for QA acceptance tokens going forward.

### **9.2.11 CLI guard tokens (D3 serializer/emitter guards)**

These tokens cover the **CLI guard tools** (for example `serializer_grep_guard.py`, `emitter_symbol_proof.py`) that enforce closed determinism env rails and serializer/emitter wiring. Their **canonical PASS condition** is satisfied in **CI/closed-rails runs**, not in open-rails Live QA.

**CLI\_SERIALIZER\_GUARD\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Mechanics Guide

*Scope:* Pre-commit / CI (D3 guard stage)

*QA definition:* Under **closed determinism rails** (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`), the CLI serializer guard job (for example `serializer_grep_guard.py`, titles-only) exits successfully and reports no violations of the canonical serializer/emitter wiring or determinism env pins. A non-zero exit under closed rails indicates a real guard failure that must block D3 acceptance.

*Evidence:*

* CI job logs showing the guard script ran under the determinism env pins (typically in the D3 guard stage) and exited with status 0, with a PASS summary and no reported violations.

* Guard log artifacts (for example `artifacts/cli/guards/serializer_grep_guard.log`) stored under governed paths with co-located path-proofs.

* Index and Mirror entries for the guard artifacts in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR.

**SERIALIZER\_GREP\_GUARD\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Mechanics Guide

*Scope:* Pre-commit / CI (D3 guard stage)

*QA definition:* The serializer grep guard enforces that governed CLI/Engine paths only use the canonical serializer/emitter and do not introduce ad-hoc JSON encoding or unpinned env-dependent behavior. Under closed determinism rails, the guard must pass (exit 0\) with no forbidden patterns or missing serializer uses.

*Evidence:*

* Guard configuration and CI logs showing:

  * execution of the grep-based guard under determinism env pins, and

  * a PASS result for all monitored files and patterns.

* A governed guard summary artifact (for example `artifacts/cli/guards/serializer_grep_guard.summary.json` or similar, titles-only) indexed in the Human Index and Machine Mirror with matching path-proof.

**EMITTER\_SYMBOL\_PROOF\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Mechanics Guide

*Scope:* Pre-commit / CI (D3 guard stage)

*QA definition:* The emitter symbol proof guard confirms that CLI and HTTP emitters share a single canonical emitter implementation and that no extra emitter symbols or divergent code paths are used for governed surfaces. Under closed determinism rails, the emitter symbol proof must pass (exit 0\) and show that all expected emitter symbols are present and wired correctly, with no unexpected or missing emitters.

*Evidence:*

* CI job logs for the emitter symbol proof run under determinism env pins, showing exit status 0 and a PASS summary over the configured symbol set.

* A governed emitter symbol proof artifact (for example `artifacts/cli/guards/emitter_symbol_proof.txt`) indexed in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl`, with a co-located path-proof and a Mirror record whose `proof_anchor` points to that proof.

**Open-rails Live QA note (informational only).**

* When these guard tools are run in **open-rails Live QA environments** (for example a PO or IA Codespace where `SAFE_MODE=0` and `ALLOW_NETWORK=1` by design), they are expected to:

  * **enforce env pins** and rails assumptions, and

  * **fail closed** (non-zero exit) when env pins do not match the closed determinism rails they require.

* Such env-mismatch failures in open-rails Live QA are treated as **informational env-enforcement checks**, not as D3 acceptance failures:

  * they do **not** satisfy the guard tokens above, and

  * they **must not** be used to block PO Live QA sessions when the environment is intentionally open rails.

* D3 guard tokens (`CLI_SERIALIZER_GUARD_OK`, `SERIALIZER_GREP_GUARD_OK`, `EMITTER_SYMBOL_PROOF_OK`) are considered satisfied **only** by **closed-rails CI runs** with PASS outcomes; Live QA plans should reference CI/closed-rails evidence when asserting these tokens, not re-run D3 under open rails.

### **9.2.12 Manifests, acceptance maps, and token binding**

PF19 treats **epic manifests** and **epic acceptance maps** as complementary views of the same acceptance surface:

* the **acceptance map** (for example `docs/acceptance_map_epicXXX.json`, titles-only) is the **design-time** source that:

  * enumerates the epic’s D-goals/foundations (D1, D2, …),

  * lists the QA tokens relevant to each D-goal, and

  * names the **governed evidence families** (artifact keys, logs, indices) that are expected to satisfy those tokens; while

* the **epic manifest** (for example `audit/EPICXXX_MANIFEST.json`, titles-only) is the **run-time** record that:

  * declares each token’s status for that epic, and

  * binds tokens to the **concrete governed artifacts** and tests that have actually been run.

PF19’s registry-level rule for all epics is:

* For each epic, the **epic manifest MUST bind each QA token to artifacts that belong to the evidence families named for that token in the epic’s acceptance map** (or in a PF-Canon section that the acceptance map points to by title). It is not acceptable to bind tokens to “generic” artifacts (for example a random sanity log or the Machine Mirror) when the acceptance map declares a different evidence family as the canonical home.

* Acceptance maps and manifests **MUST be kept consistent by automated tests**, not by manual inspection:

  * For every token listed in the acceptance map, there must be:

    * a corresponding manifest entry for that token; and

    * at least one artifact path in the manifest that belongs to the evidence family (or families) declared for that token in the acceptance map (for example manifest tokens for `CONFIG_REGISTRY_OK` reference the registry report family defined in PF12 and the config acceptance map; tokens for `SANITY_PIPELINE_OK` reference the sanity log family; tokens for evidence index/mirror reference the INDEX/Mirror families, and so on).

  * For every token in the manifest, there must be:

    * a corresponding entry in the acceptance map (or in a clearly referenced PF-Canon section for that epic), and

    * evidence paths that resolve to **real governed artifacts** in those families (present in INDEX/Mirror with path-proofs and matching `sha256`/`size_bytes`).

  * Automated tests (for example `tests/audit/test_acceptance_map_epicXXX.py`, names-only) are expected to:

    * validate the shape and contents of the acceptance map itself (epic id, foundations, token roster), and

    * assert that the manifest’s token→artifact bindings **match** the evidence families and artifact paths declared in the acceptance map (or its canonical PF references).

* When an epic adds new evidence families (for example sampler or Engine Core evidence families defined in **HDE-Schemas & Artifacts** by title) and new tokens that depend on them, the corresponding PF12 and PF09/PF19 entries **MUST** be updated so that:

  * the evidence families appear in the Evidence Catalog (PF12) with the correct artifact keys and paths;

  * the acceptance map names those families and their tokens; and

  * the manifest binds those tokens only to artifacts that belong to those families, with automated tests enforcing **acceptance map ↔ manifest ↔ evidence skeleton** consistency.

PF19 does not define manifest or acceptance map schemas; those live in **HDE Phased Epics**, **HDE-Build Checklist**, and **HDE-Schemas & Artifacts** (titles-only). PF19’s role is to make clear that:

* **Tokens are only Green when manifests bind them to the evidence families declared in the acceptance map, and automated tests prove that binding;**

* A manifest that binds tokens to unrelated artifacts, or that diverges from the acceptance map, is treated as a **QA failure** until corrected and covered by tests.

### **9.2.13 Live vendor & discovery tokens**

These tokens cover **live vendor transport**, **open-rails env posture**, and **discovery baselines** for epics that claim live vendor behavior or vendor-first PO Live QA.

**LIVE\_VENDOR\_TRANSPORT\_OK**

*Owner PF:* HDE-Governance / HDE-CLI-API-Vendor-Ref / HDE-Mechanics Guide / HDE Phased Epics

*Scope:* Post-commit / Live QA (vendor-focused epics)

*QA definition:* For a given epic that claims live vendor behavior in prod or prod-like environments, `LIVE_VENDOR_TRANSPORT_OK` asserts that there is **at least one concrete, governed proof of live vendor transport under open rails**. At minimum, QA must show that:

* a vendor-focused behavior step (class 3 under §3.5.6) ran under open rails (`ALLOW_NETWORK=1` with rails logged per §4.4), and

* a CLI or HTTP surface invoked a **real vendor endpoint** (as defined in PF05/PF14) and received a non-mocked response (success or controlled failure), with the request and response captured as governed evidence.

*Evidence:*

* A vendor-focused step log in QA\_ROOT (for example `D_vendor-001.log` or `stepV1_vendor_compat.log`) with header fields:

  * `check_id` pointing to the vendor behavior step,

  * `command` showing the CLI or HTTP call used (for example `hdctl showcompat --source=vendor ...` or a `curl` call to an HDE adapter route that triggers vendor transport),

  * `rails` including `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`,

  * `pf_refs` referencing vendor mechanics and transport docs by title, and

  * `status: PASS` once reviewed.

* Supporting artifacts under `audit/qa/<epic-id>/vendor/…` or an equivalent vendor-specific subtree, including:

  * a request description file (for example `vendor-step-001-request.txt`) naming the CLI/HTTP surface, environment, and inputs;

  * raw or header-stripped HTTP/CLI logs showing:

    * the vendor host or URL (names-only),

    * HTTP status code(s), and

    * any vendor response envelope that policy allows to be recorded (keys-only, no secrets);

  * a rails snapshot (either in the step log header or as a separate env snapshot referenced from the log) confirming open rails were in effect at the time of the vendor call.

* Indexing of any governed vendor proof artifacts (for example JSON/summary logs under `artifacts/**` or `docs/**`) in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl`, with path-proofs and Mirror records aligned, where the epic’s acceptance map and manifest bind `LIVE_VENDOR_TRANSPORT_OK` to these families.

**OPEN\_RAILS\_ENV\_OK**

*Owner PF:* HDE-Governance / HDE-Build Checklist / HDE Phased Epics

*Scope:* Pre-commit / Live QA (rails posture for vendor epics)

*QA definition:* For epics that **mandate open rails** for certain Live QA steps (for example vendor-first PO Live QA), `OPEN_RAILS_ENV_OK` asserts that the **open-rails environment was real, documented, and actually used** for the vendor-focused steps:

* there is a D0 or early Session env snapshot that records the intended rails posture (for example “Codespaces open-rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`”), and

* each vendor-focused step’s log in QA\_ROOT shows rails consistent with that mandate in its `rails` header field at the time of the behavior run.

*Evidence:*

* A discovery or env-rails planning artifact under `audit/qa/<epic-id>/d0-planning/` (for example `d0-env-rails.txt`) that records the intended rails posture for the session, as produced by commands such as `env | sort | grep -E 'SAFE_MODE|ALLOW_NETWORK|APP_ENV|HDE_BASE_URL'` per §3.6.

* For each vendor-focused step that contributes to `LIVE_VENDOR_TRANSPORT_OK`, a primary step log in QA\_ROOT whose header `rails` field shows:

  * `ALLOW_NETWORK=1` (or equivalent open-network posture) and

  * the intended `APP_ENV` (for example `APP_ENV=prod` or `APP_ENV=dev` per epic design),

* aligned with the mandated rails in the epic’s acceptance roster.

* Optional end-of-session env snapshot logs (for example `…/env_rails_end.log`) confirming rails were restored to the correct closed posture after Live QA.

**DISCOVERY\_BASELINE\_OK**

*Owner PF:* HDE-Build Checklist / HDE-Schemas & Artifacts / HDE Phased Epics

*Scope:* Pre-run / planning (D0 discovery)

*QA definition:* `DISCOVERY_BASELINE_OK` asserts that a **D0 discovery pass** was performed and recorded before running Live QA steps for an epic, and that the discovery captured the repo and environment facts PF19 requires: governed config and bundle trees, guard/sanity runners, CLI help output, env rails intent, and `.gitignore` behavior for QA trees.

*Evidence:*

* A set of `d0-*` planning artifacts under `audit/qa/<epic-id>/d0-planning/` created before Live QA was finalized, including at least:

  * `d0-config-tree.txt` and `d0-bundles-tree.txt` (or equivalent) showing `artifacts/config`, `artifacts/config_bundles`, `artifacts/registry` contents;

  * `d0-guards-tree.txt` and `d0-sanity-runner-notes.txt` (or equivalent) showing guard scripts and sanity pipeline runners present in the repo;

  * `d0-hdctl-help.txt`, `d0-showcompat-help.txt`, `d0-bg-resolve-help.txt` (or equivalent) capturing actual CLI help output so QA plans do not invent flags or subcommands; and

  * `d0-env-rails.txt` plus `d0-gitignore-audit-qa.txt` showing the intended rails posture and confirming `audit/qa/<epic-id>/…` is not hidden by `.gitignore`.

* Index/Mirror records and path-proofs for any of these `d0-*` artifacts that are treated as governed evidence (for example when they form part of the epic’s documented QA baseline and acceptance), and acceptance maps/manifests in HDE Phased Epics binding `DISCOVERY_BASELINE_OK` to these families.

These tokens work together with the vendor-first Live QA rules in §3.3 and §3.5 and the evidence/logging structure in §4.4 to ensure that:

* discovery and env rails baselines are captured up front (`DISCOVERY_BASELINE_OK`),

* open-rails posture is real and documented where epics require it (`OPEN_RAILS_ENV_OK`), and

* at least one governed live vendor proof exists for epics that claim live vendor behavior (`LIVE_VENDOR_TRANSPORT_OK`).

### **9.2.14 Token/evidence matrix and review rails**

**Intent.**  
 Make the relationship between QA tokens and evidence **explicit and checkable** at review time. Any plan, QA plan, or epic record that defines or consumes QA Acceptance Tokens **MUST** provide a concrete, reviewable **token/evidence matrix** before it can be approved.

**Scope.**

The token/evidence matrix requirement applies to:

* implementation plans,

* QA plans, and

* epic records and acceptance maps in **HDE Phased Epics**

whenever they **introduce, rename, or consume** QA Acceptance Tokens from this registry.

#### **9.2.14.1 Matrix shape (per-token rows)**

For each QA token **in scope** for a plan or epic (one row per token), the matrix **MUST** capture at least:

* **PF19 registry name** — the canonical token spelling from this registry (no local aliases).

* **Epic-level acceptance map name** — the token name as it appears in the epic’s acceptance map (must be exactly the PF19 registry name).

* **Tests** — unit/integration tests that exercise the token’s behavior (for example specific test modules or cases).

* **CI jobs** — CI jobs that enforce the token’s behavior under closed rails, where applicable (names only; definitions live in **HDE-Build Checklist**).

* **Live QA steps (if applicable)** — Live QA steps that demonstrate the token’s behavior (for example D1/D3 steps in the epic QA plan), with references to their primary step logs under `audit/qa/<epic-id>/…`.

* **Evidence artifacts** — governed artifact paths (under `docs/**` or `artifacts/**`) generated by those tests and steps.

* **Index/Mirror binding** — the Evidence Index and Machine Mirror records (by artifact key or path) that register those artifacts, including `proof_anchor` references to path-proofs.

The matrix may be rendered as a table, JSON, or other machine-readable structure, but it must be **complete** for all tokens in scope.

#### **9.2.14.2 Approval gate (no “e.g.” / “TBD” / implicit cells)**

For tokens that are **in scope** for a plan or epic:

* No cell in the token/evidence matrix may be left **blank**, marked as “`e.g.`”, “`TBD`”, or described only in narrative prose. If a test, CI job, Live QA step, or evidence artifact does not yet exist, that gap must be called out explicitly and treated as a **blocking issue**, not as an implicit future task.

* A plan, QA plan, or epic record that contains any in-scope token with:

  * `e.g.` or `TBD` token names,

  * missing or implicit tests/CI/Live QA references, or

  * missing evidence/index/mirror bindings,

* **MUST NOT** be marked approved (`ASK OK`) for that token. Approval can proceed only once the matrix row is fully populated and consistent with the acceptance map and manifest (§9.2.12).

* Any attempt to treat an incomplete matrix row as “good enough for now” is a **QA process violation**. Reviewers must either:

  * require the gaps to be filled and re-review the plan, or

  * record a deliberate scope deferral in **HDE Phased Epics** and remove the token from the in-scope roster for that epic.

#### **9.2.14.3 Consistency with acceptance maps and manifests**

The token/evidence matrix is a **per-plan view** of the same relationships enforced globally by §9.2.12:

* Every PF19 registry name that appears in the matrix **MUST** also appear in the epic’s acceptance map token roster.

* Every evidence artifact listed in the matrix **MUST** belong to one of the evidence families named for that token in the acceptance map (or in a PF-Canon section the map points to by title), and must be present in the Human Index and Machine Mirror with a valid path-proof.

* Automated tests are expected to validate that matrix rows, acceptance maps, manifests, and the evidence skeleton remain in sync. Inconsistencies between these views — including missing rows, extra tokens, or mismatched artifact families — are **QA failures**, not documentation nits.

This section upgrades the token/evidence matrix from a “good practice” to a **required approval gate**: no plan or epic that touches QA tokens is ready for approval until its token/evidence matrix is complete, consistent with the registry, and aligned with acceptance maps, manifests, and the evidence skeleton.

### **9.2.15 Review rails for token blockers, scope waivers, and canonical names**

#### **9.2.15.1 Previously identified token/evidence blockers**

Once a reviewer has identified a problem with token naming or token→evidence wiring and recorded it as a **blocking issue** (for example:

* a token used in an acceptance map that does not exist in the PF19 registry,

* a token row in the token/evidence matrix with `e.g.` names or missing evidence bindings, or

* a mismatch between manifest bindings and the evidence families declared in the acceptance map),

that blocker **MAY NOT** be downgraded to “non-blocking” in a later review **unless**:

* the plan, acceptance map, manifest, or QA plan has been updated to resolve the issue (for example, token names made canonical, matrix completed, or evidence wiring corrected); or

* PF-Canon has been explicitly updated (for example this registry or another owning PF doc) to change the token’s status, semantics, or required evidence.

Any such downgrade **MUST** reference the specific change (plan diff and/or PF doc delta) that resolved the blocker. A change in reviewer interpretation or scope alone is **not sufficient**.

#### **9.2.15.2 Scope waivers are explicit and non-transitive**

If the Product Owner or governance chooses to **waive or narrow a canon requirement** for a particular plan or epic (for example deciding that **Reality Audits** are out of scope for that implementation), reviewers **MUST**:

* record that as a **local scope directive** in the relevant epic documentation (for example in **HDE Phased Epics** or **HDE-Build Notes** by title), and

* explicitly state that other rails — including PF19 token rules, PF12 evidence rules, PF20 D-goals, and PF09 CI rails — remain fully in force.

Such waivers:

* do **not** weaken or modify PF19’s token semantics or evidence requirements;

* do **not** automatically extend to other epics, plans, or components; and

* must never be interpreted as permission to relax token naming, acceptance mapping, evidence wiring, or other PF-Canon backed rails.

Each new plan or epic must independently record any local scope waivers; there are no “silent inherited waivers” in PF19.

#### **9.2.15.3 Re-grounding before claiming “no canonical token name exists”**

Before any reviewer asserts that **“no canonical token name exists yet”** for a QA behavior, they **MUST**:

1. Re-check this registry (PF19 §9.1/§9.2) for an existing token that covers the behavior.

2. Re-read any epic-specific approvals or remediation guides that may have already chosen a token name and semantics for that behavior (for example epic remediation guides or PF10 addenda referenced by title).

If such an approval or guide already defines a token name and expected behavior, plans and acceptance maps **MUST** treat that name as canonical for QA purposes, even if the PF19 entry is still being backfilled via a doc delta. In that case:

* PF19 becomes the **drainage target** for the already-chosen name and semantics; and

* any attempt to invent a new local name for the same behavior is a violation of the registry rules in §9.2.2.

Claims that “no canonical token name exists” are only acceptable when:

* the behavior is genuinely new, and

* there is no existing PF19 entry, no epic-level approval, and no PF10/PF20 doc delta that already names and constrains it.

In that case, adding a new token **MUST** proceed via a PF19 doc delta as described in §9.2.2, and the plan or epic remains **token-incomplete** until the new registry entry lands.

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

  ## **11.2 Component ownership**

PF19 is the orchestration guide for QA. Day-to-day ownership of specific playbooks lives with the corresponding component leads; infra/ops own the underlying environment wiring and dev harness surfaces.

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

**Infra / Ops owner**

* Responsible for environment and service wiring that QA depends on, including:

  * Reader/service start commands and ports per environment (for example dev/Codespaces vs staging/prod), as documented in **Glow Infrastructure** and **HDE-Mechanics Guide** (titles-only); and

  * internal/dev HTTP harnesses (for example `/internal/dev/sampler`), including:

    * canonical dev start commands or service definitions that run the Reader with `APP_ENV=dev` and required determinism rails, and

    * infra-owned base URLs and ports from which concrete harness URLs (such as `DEV_SAMPLER_URL`) are derived and validated before use.

* Infra/Ops **MUST** validate dev harness URLs and start commands (for example via a simple HTTP/1.1 JSON POST and header/body checks against the owning PF docs, titles-only) **before** handing them to QA. QA/PO **MUST NOT** guess or redefine these URLs; missing or unclear dev harness wiring is treated as an infra/spec gap per §11.3, not as a QA improvisation task.

For each component:

* The component owner is **Responsible** for keeping its playbook or wiring up to date.

* The Lead Dev is **Accountable** that all required playbooks for an epic are applied and that environment wiring (including dev harness URLs) is in place before Live QA is attempted.

* The IA is **Responsible** for invoking the right playbooks, consuming infra-owned URLs and start commands, and wiring them into CodEx instructions without guessing.

* The Scrum Master is **Informed** about which playbooks and harnesses were run and what passed/failed.

  ## **11.3 Canon-first rule for Implementation Agents**

Implementation Agents are required to follow a **canon-first workflow** when planning QA for any epic.

**Canon-first inventory (before planning).**

* Before drafting a QA plan or asking the Product Owner for environment details, the IA **MUST** read, by title:

  * **Glow Infrastructure** for infra and environment facts (for example Railway service names, base URLs, DB instances and schemas),

  * **HDE-Build Notes** for relevant addenda and cross-epic QA guidance,

  * **HDE Phased Epics** for the epic’s D-goals and acceptance roster, and

  * this guide (**Glow QA Guide**) for QA tokens, rails, and playbooks.

* If those documents already specify an infra/env value (for example a prod base URL, DB name, or rails pattern) and do not mark it as OPEN/TBD, the IA **MUST NOT** treat that value as a PO input.

**Asking for information vs spec gaps.**

* IAs **MUST NOT** ask the PO to “fill in” canonical infra/env values that PF-Canon already defines; doing so is treated as a **spec violation**, not a harmless shortcut.

* If PF-Canon is missing or contradictory on a required detail, the IA must:

  * mark the affected QA step as **blocked by spec ambiguity**,

  * capture any available evidence, and

  * propose a PF10 or HDE Phased Epics gap note,

* rather than improvising new rails or asking the PO to guess.

**Separation of closed-rails determinism vs open-rails prod checks.**

* Closed-rails determinism (`SAFE_MODE=1`, `ALLOW_NETWORK=0` with env pins) is reserved for determinism-sensitive jobs (serializer determinism, env rails checks, sanity pipeline, config determinism), as described in this guide and HDE-Build Checklist.

* For PROD checks (for example Reader/Aux parity, CLI flows against prod), IAs must treat prod as the Railway service and DB defined in infra canon and design QA steps that use **open rails** from a QA console (such as Codespaces) to reach those prod surfaces, using determinism evidence (two-run identity and governed artifacts) rather than forcing `ALLOW_NETWORK=0`.

Any QA plan that ignores this canon-first rule or treats canonical infra/env values as PO-supplied inputs is **non-conforming** with PF19 and should be rejected or revised before implementation.

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

## **13.3 HDE-EPIC020 — Separation Pass 1 — Error & Identity Surfaces**

**Status.**  
 HDE-EPIC020 is chartered in **HDE Phased Epics** as “Separation Pass 1 — Error & Identity Surfaces.” It gives Separation-phase shape to three Engine surfaces — the error envelope and token set, the shared presenter/emitter, and the `/internal/version` identity surface — on top of prior Calcination/Dissolution work on determinism, canonical JSON, and evidence. The Dev Retrospective Summary and PF10 build notes record EPIC020’s QA verdict as **“READY WITH CAVEATS.”**

**Acceptance scaffolding and evidence.**

* EPIC020 wired its D-goals into acceptance scaffolding via an epic-level acceptance map and manifest (titles-only; for example `docs/acceptance_map_epic020.json` and `audit/EPIC020_MANIFEST.json`), listing D0–D3 tokens, PF references, and evidence families.

* A Candidate 1 evidence bundler and CI job integrate EPIC020’s bundles and manifests into the Evidence Index and Machine Mirror under closed rails, with D1/D2/D3 tokens and rails represented as governed bundle artifacts in line with PF09 and PF12.

* Live QA and planning evidence for this epic are rooted under `audit/qa/hde-epic020/...` (for example `d0-baseline/`, `d1-error-cli/`, `d2-cli-presenter/`, `d3-internal-version/`), giving a single QA tree for EPIC020.

**Surfaces and coverage (D0–D3).**

*D0 — Environment and rails baseline.*

* Live QA established a dev Codespaces baseline for EPIC020, proving rails (`APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`) and capturing evidence under `audit/qa/hde-epic020/d0-baseline/`.

* PF10 records a planning error where `hdctl --version` was assumed to be a canonical presence/identity check; EPIC020 treats that as a plan mis-spec, not a behavior failure. The D0 CLI baseline ADR that follows from this is encoded in §3.6 under **D0 CLI baseline pattern (names-only)**.

*D1 — Error envelope and CLI error semantics.*

* On the CLI side, EPIC020 delivers error discipline for at least one canonical usage error path (`hdctl showcompat` with a missing `--pair-file`): stderr/stdout/exit behavior and banded QA tokens (for example stderr-only-on-error, canonical JSON, LF on stdout) are wired into the acceptance map and Candidate 1 bundles.

* On the HTTP side, a dev Reader harness exposes `POST /api/compat/v1` on the canonical dev port, and EPIC020 proves malformed-JSON error handling and the associated compat JSON error envelope and headers, with evidence captured in tests and QA artifacts. Other HTTP error modes and happy-path coverage remain with existing CI and future epics.

*D2 — Presenter and CLI parity.*

* Implementation connects the shared presenter/emitter to `hdctl showcompat` and the Reader compat emitter, with pytest suites demonstrating canonical JSON emission, Reader↔CLI parity, and serializer guard observance.

* Live QA re-runs key CLI pytest suites under determinism rails from Codespaces and records evidence under `audit/qa/hde-epic020/d2-cli-presenter/`. An earlier plan that depended on a pre-generated `two_run_identity.log` artifact discovered that the log did not exist; that step was treated as a planning/tooling gap, not as a reason to weaken presenter parity expectations, and the missing log is recorded as debt for future work rather than as silently ignored scope.

*D3 — `/internal/version` identity and transport.*

* EPIC020 hardens `/internal/version` identity for the Engine by adding tests and tokens (for example covering content-type, header posture, and GET vs HEAD parity, titles-only) and by integrating identity evidence into bundles/manifests.

* Live QA exercises `/internal/version` GET and HEAD against the dev harness under pinned env rails and records identity evidence under `audit/qa/hde-epic020/d3-internal-version/`. Within EPIC020’s charter (dev harness, Engine behavior), D3 is treated as behavior-complete; multi-environment identity posture remains in earlier and future epics.

**QA verdict and caveats.**

* QA treats EPIC020’s D0–D3 goals as satisfied for its scope: D0 rails and environment baseline, D1 canonical CLI usage error and malformed-JSON compat envelope, D2 presenter/CLI parity via pytest, and D3 `/internal/version` identity at the dev harness all have governed evidence (Candidate 1 bundles, manifests, tests, and Live QA logs under `audit/qa/hde-epic020/...`).

* Several gaps are explicitly documented and parked rather than hidden:

  * broader CLI error matrix coverage beyond the single canonical usage error in Live QA;

  * additional compat HTTP error modes and happy paths beyond malformed JSON;

  * the missing legacy `two_run_identity.log` harness asset;

  * lack of vendor ingest Live QA for compat; and

  * the fact that EPIC020 operates under dev-only rails, leaving multi-environment identity proofs to other epics.

These caveats are recorded as future work in **HDE Phased Epics** and PF10/PF09 docs (titles-only), not treated as silent omissions.

**PF19 linkage.**

PF19 uses this EPIC020 history entry to:

* anchor the D0 CLI baseline pattern in §3.6 to a concrete EPIC020 ADR, so future epics avoid repeating the `--version` mis-spec;

* highlight EPIC020’s Candidate 1 bundle/manifest \+ closed-rails CI pattern as a Separation-phase example of integrating epic-specific evidence families into the Evidence Index and Machine Mirror; and

* document that, subject to the explicit caveats above, EPIC020’s Separation-phase QA for error envelopes, presenter parity, and `/internal/version` identity is functionally complete on its D-goals.

Normative homes for EPIC020’s acceptance tokens, D-goal definitions, and bundle schemas remain **HDE Phased Epics**, **HDE-Build Checklist**, **HDE-Schemas & Artifacts**, and **HDE-CLI-API-Vendor-Ref** (titles-only). PF19 records the QA posture and history; it does not redefine the underlying math or transport bytes.

