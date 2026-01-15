# **0\. Front Matter**

## **0.1 Header**

**Title:** PF19-Canon-Glow-QA-Guide

**Status:** Canon

**Version:** v1.8.5

**Effective date:** 2026-01-13

**Last Update Gate:** BN 9.3.4 Drain 54-57

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

* PF16 — HDE Epics Map (historical context only)

* PF17 — HDE Narratives Guide

**Epics and phased planning (titles-only).**  
 PF19 treats epic planning and phase mapping as outside its scope. For HD Engine epic history, **HDE Phased Epics** is **historical-only**: it MUST contain only **completed** epic records (formally closed per **Epic-Process-Guide**, titles-only) and is updated only at epic close (no in-flight placeholders). **HDE Epics Map** is maintained as historical context only and must not be used as the source of truth for new work. In particular:

* **HDE-EPIC011 — Vendor Ingest & Data Durability** is recorded as a **failed epic**; its acceptance roster (DB posture, ingest idempotence, evidence discipline, partition plan, SAFE rails, BodyGraph invariance) did not reach a fully green, production-ready state.

* **HDE-EPIC012–HDE-EPIC014** are preserved as “won’t do” (historical design), and any residual work they described must be captured as recorded debt or re-scoped into a future epic, not treated as open acceptance here.

**Role boundary (normative; no governance / no tokens / no planning).**  
 PF14 is a mechanics/components reference only. It:

* MUST NOT define, rename, alias, or curate acceptance token spellings.

* MUST NOT act as a planning authority (it may inform planning, but does not govern epic plan structure, acceptance rosters, or close gates).

* When PF14 needs to mention governance or acceptance, it MUST route to the governing document by **title** (and section if needed) and remain descriptive about component fields and mechanical responsibilities only.

PF19 may reference these epics by title when describing QA history or preservation surfaces, but any **new** epic-level QA decision (for example, where to land future PK, partition, or Catalog/A7 work) MUST be captured in the epic’s in-flight planning and QA ledger artifacts and then reflected in the archived epic record at close. HDE Epics Map is historical-only and MUST NOT be treated as a home for new decisions. HDE Phased Epics is historical-only and MUST NOT be treated as an in-flight tracker.

PF19 owns QA principles, checklists, and cross-component playbooks; it routes all transport, math, schema, and token details to those single homes.

**Reality Audits vs QA tokens (titles-only).**  
 PF19 treats **Reality Audits** as a **separate axis** from QA token semantics. Reality Audits (as defined in **Reality Audits**) are PO-only, post-epic architecture reviews that may be **in scope** or **out of scope** for a given epic or implementation plan. Decisions to run, skip, narrow, or broaden a Reality Audit for a specific epic:

* do **not** add, remove, or weaken any QA Acceptance Tokens in this guide;

* do **not** change which QA tokens exist in the PF19 registry, how they are named, or what evidence they require; and

* do **not** change the requirement that epic acceptance maps and manifests bind tokens to governed evidence families as described in §9.2.12.

PF23 scope choices are local to a plan or epic and must be recorded there (for example in **HDE Phased Epics** or **HDE-Build Notes** by title). PF19’s QA tokens and their governance rules remain global and unaffected by per-epic Reality Audit decisions.

**Planning posture: mandatory PF23 consult (components \+ pathnames).**  
 This rule applies to all planning artifacts, including (non-exhaustive): QA plans, remediation guides, implementation guides, EPIC records, and stepwise runbooks.

* Planning for QA, remediation, development, or any execution work MUST consult **Reality Audits** as a primary input for:

  * component boundaries (what the “thing” is),

  * canonical pathnames and repo loci (where the “thing” lives), and

  * audit-provided component metadata needed to avoid drift.

* **Freshness posture (normative).** PF23 is updated at the end of each EPIC for every product component. Plans MUST treat PF23 as the freshest source for component/pathname reality at the time of planning.

* **How to use PF23 in plans (trace only; no duplication).** Planning documents SHOULD include a short “PF23 Anchors” subsection that lists:

  * the component(s) consulted from PF23, and

  * the key pathnames/loci pulled from PF23 that the plan will touch.

* This is a traceability anchor only. It MUST NOT duplicate PF23 contents.  
* **PF23 consult is planning-time only (no Live QA deliverables).** Live QA plans MUST NOT require any PF23 consult capture artifact (e.g., `pf23_consult.md`) and MUST NOT include PF23 operator commands as execution steps. If present, the “PF23 Anchors” note is informational only (names-only) and MUST be non-gating.  
* **Ownership (normative).** PF23 is PO-maintained. Planning documents MUST NOT create tasks that assign PF23 updates. If PF23 appears stale or missing required component coverage, the plan MAY note that as an observation, but must not assign it as agent work.

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

### 0.4.3 Core principles (names-only). 

PF19 assumes and reinforces these core QA principles.

PF19 is titles-only for cross-references. It does not duplicate bytes or schemas and always routes to the owning PF by title. PF19 never redefines wire contracts or token semantics. Those definitions remain in the owning PF homes (for example the CLI/API reference, schemas and artifacts, governance, and the build checklist).

Determinism and env pins apply in all environments whenever governed bytes are produced. All canonicalization, hashing, header snapshotting, and governed evidence capture must run with `LC_ALL=C`, `LANG=C`, and `TZ=UTC` in dev, stage, prod, and CI. Interpreter/runtime knobs such as `PYTHONHASHSEED` must not be treated as required rails pins unless a specific step explicitly depends on hash-iteration determinism. If such a knob is present, plans may record it as observed context. If absent, plans must not fail or block on that basis.

Evidence is governed by same-PR parity and completeness, not just formatting. The Human Evidence Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) must be updated together in the same PR whenever evidence changes, and QA must treat “code change without evidence parity” as a failure, not a warning. For every governed artifact under a governed evidence root declared in the Evidence Catalog (titles-only, with schemas and semantics defined only in HDE Schemas and Artifacts), QA must ensure the triple is complete: one Human Evidence Index entry, one Machine Mirror record, and one co-located `path_proof.txt` whose path is referenced by the Mirror record’s `proof_anchor`. This also applies to lifecycle and OPS-managed artifacts (for example backup/restore/retention runs). If any leg is missing, QA must treat the evidence as incomplete and block tokens that depend on it.

Path-proof freshness is normative for the Human Evidence Index and its hash sentinel. `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` are governed artifacts, and their co-located path-proof transcripts (`docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt`) must be refreshed whenever the index or sentinel bytes change, in the same PR. Stale INDEX path-proofs are merge-blocking evidence integrity failures and must be remediated by rerunning canonical evidence tooling, not by hand-editing proofs.

Baseline HD Engine evidence must remain agent-readable at the PR level. The primary evidence ledger must be expressed through plain-text artifacts under governed paths (`docs/**`, `artifacts/**`, `audit/**`), such as the Human Evidence Index, the Machine Mirror, bundle manifests, and key QA logs and step transcripts. Binary or compressed bundles may exist as supplementary artifacts, but they must not be the only governed evidence for any acceptance token that requires payload inspection by an agent. Hash-only or status-only proof families are acceptable only when the evidence consumer does not need to inspect payload content. Otherwise, they must be paired with at least one governed text artifact (for example a bundle manifest, QA log, or summary) that exposes the relevant payloads at the evidence ledger level. Titles and schemas for these artifacts remain in HDE Schemas and Artifacts, the build checklist, and related PF docs.

Live QA evidence should be mechanical, and narrative belongs elsewhere. Live QA and bootstrap evidence should be logs, JSON, exit codes, tree/env snapshots, and scripted notes written under `audit/qa/<epic-id>/…`, not hand-edited prose by the PO. Narrative QA addenda and synthesis (for example epic QA reviews, build-note summaries, PF20 closeouts) are authored by QA personas and Leads in PF10 (build notes) and HDE Phased Epics (titles-only), not in Live QA notes files.

CI runs with rails closed by default. CI pipelines run with `SAFE_MODE=1` and `ALLOW_NETWORK=0` unless explicitly opened. Any job that opens rails must pin SAFE policy (timeouts/retries/backoff from closed domains, no jitter) as defined in governance, attach governed evidence, and update the Human Index and Machine Mirror in the same PR.

A7 is Catalog-only and is gated by the Endpoint Catalog. A7 proofs run only on a cataloged JSON success route and do not treat `/internal/*` routes (including `/internal/version`) as an A7 surface. Aux HEAD/304 are out of scope under EPIC-010. A7 QA runs only when `docs/ENDPOINTS_CATALOG.json` exists and is valid per HDE Schemas and Artifacts, and the Catalog row for the Reader JSON success surface exists and is marked as a JSON success route. If those conditions are not met, QA treats the A7 suite as gated off: no A7 tokens are claimed for that PR, and the missing or invalid Catalog entry is reported as a QA failure, not a cosmetic skip.

Industry anchors are reference-only. PF19 aligns its QA rules and proofs with IETF RFC 9110/9111 for HTTP semantics and caching, RFC 8785 (JCS) as an external anchor for JSON canonicalization, OWASP ASVS for FE/BE security verification, and NIST SSDF and SLSA for supply-chain QA and provenance expectations. PF19 remains titles-only: bytes, schemas, and token definitions stay in their owning PF homes (for example PF05, PF12, PF04, PF09).

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

  * **Epics map (historical-only).** For HD Engine epics, **HDE Epics Map** is **historical-only**; it records past epic allocations, including **HDE-EPIC011** as a failed epic and **HDE-EPIC012–HDE-EPIC014** as “won’t do”. **HDE Phased Epics** is also **historical-only**: it contains only completed epic records and is updated only at epic close (no in-flight records). QA must treat these documents as historical context and MUST NOT use them for in-flight tracking or as a planning gate.

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
* **Import-time dependency failures are tooling, not behavior.**  
   If a pytest run fails during collection/import (for example `ModuleNotFoundError: jsonschema`) before any tests execute, QA MUST classify this as a tooling failure (FAIL\_TOOLING / TOOLING\_BLOCKED). Acceptable remediation patterns are:  
  * **Required dependency mode:** treat the dependency as required for the relevant CI job and ensure CI installs the required dependency set (for example dev requirements) so the tests actually run; or  
  * **Optional dependency mode:** guard optional dependencies so pytest collection succeeds and the relevant tests either run or skip with an explicit, actionable install hint (for example `pytest.importorskip("jsonschema", reason="install requirements-dev.txt to run schema validation")`).

QA MUST NOT treat “collection died due to missing optional dependency” as a product behavior failure.

### **2.2.6 Rails posture in CI (default CLOSED)**

* Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default.

* If any pre-commit job opens rails (network I/O), it **MUST** produce governed evidence and index it in the same PR (titles-only routing to PF12/PF09).

  ### **2.2.7 Machine mirror quick-check (includes path-proofs)**

* Verify `artifacts/evidence_index.jsonl` exists and is the **only** mirror file; records are canonical JSONL (sorted keys, compact, one LF, unknown-key reject, pinned field order).

* Verify each record’s `proof_anchor` points to an adjacent stored path-proof; fail CI if any proof is missing.

* Enforce “governed roots only”: all indexed artifacts MUST live under a governed evidence root **declared in the Evidence Catalog** (HDE Schemas & Artifacts, titles-only). Indexed artifacts MUST NOT use transient/generator paths or ad-hoc roots that are not cataloged.

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

For PRs that change governed evidence artifacts (Index, Mirror, or other governed roots), CI MUST run under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`):

1. **Generate ordering artifacts (write, then check, when in scope).**

   * Run the ordering generator once in write mode (no `--check`) to refresh ordering artifacts from the current sources (catalogs, manifests, and Engine math).

   * Then run the same generator again with its `--check` mode to verify that an unchanged tree produces no changes to the ordering artifacts.

2. **Update Evidence Index and Mirror (write, then check).**

   * Run the Evidence Index/Mirror tool once in write mode to refresh Index, Mirror, and their path proofs from the current on-disk bytes, including (at minimum):

     * `docs/evidence/INDEX.json.path_proof.txt`

     * `docs/evidence/INDEX.sha256.path_proof.txt`

   * Then run the same tool again with `--check` to confirm a stable second pass (no drift, no dangling artifacts, no missing proofs, no schema violations).

3. **Run topology orientation checks (write, then check).**

   * Run the orientation demo tool once in write mode to refresh `docs/topology/orientation_demo.txt` from the current Index/Mirror state.

   * Then run the same tool again with `--check` to confirm it matches the current Index/Mirror state and does not drift on a second run.

4. **Enforce Mirror schema and path-proof discipline.**

   * Run the Mirror-schema quick-check (see §10.5) to validate canonical JSONL, schema strictness, required fields, pinned field order, stable line endings, mirror file, and `proof_anchor` alignment with `*.path_proof.txt`.

5. **Run ordering/evidence test suites.**

   * Run the pytest suites that cover ordering properties and evidence correctness (titles-only); treat any failure as a CI failure for governed artifacts.

6. **Enforce release identity and Freeze-Pack Manifest coherence (fail-closed; when in scope).**

   * When the PR touches release-identity surfaces (manifest, release\_id artifacts, recompute tooling, or the governed evidence copy), CI MUST run the canonical release-identity gate under closed rails.

   * The gate MUST validate, at minimum (titles-only for schema/semantics):

     * the Freeze-Pack Manifest SoT is `catalog/manifest.json` (no alternate SoT),

     * the governed evidence copy is byte-identical to the SoT (no derived semantics),

     * the `release_id` value is derived from canonical manifest bytes, and

     * the recompute check fails closed on any mismatch.

   * The gate MUST also require the canonical release-identity evidence outputs to exist and be non-empty (see §4.2 for capture expectations).

PF19 defines the required sequence at the QA level; PF09 — HDE-Build Checklist, PF12 — HDE-Schemas & Artifacts, and HDE-Mechanics Guide provide the concrete tool names and CI job definitions.

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

Every EPIC’s PO specifies what rails posture must be used to accept the epic (open rails vs closed rails). This posture is non-negotiable: it informs which tests must be run and how results are interpreted.

* If an EPIC requires open-rails testing (SAFE\_MODE=0; ALLOW\_NETWORK=1), then QA MUST confirm those rails are actually in effect for any Live QA run used for acceptance.

* If only closed-rails tests are run (SAFE\_MODE=1; ALLOW\_NETWORK=0) when open rails are required, then the run cannot be used as open-rails acceptance evidence. The step’s primary log (and any token claims) MUST record this explicitly via its `status` and a clear reason (in the header or at the top of the log body).

**Rails evidence (normative):**

* Each Live QA step’s primary log **MUST** include a `captured_env` header field as described in §4.4, capturing at least:

  * SAFE\_MODE

  * ALLOW\_NETWORK

  * APP\_ENV

  * LC\_ALL

  * LANG

  * TZ

This is canonical evidence of which rails were actually in effect for that step. It must be present even when Rails posture is “obvious” from context, because reviewers cannot accept implicit environment assumptions.

* When mandated rails cannot be met due to environment constraints (e.g., SAFE\_MODE is enforced on CI runners), the QA plan must either (a) route that step to a compatible environment, or (b) mark the affected steps as TOOLING\_BLOCKED / FAIL\_TOOLING in their headers with a clear reason (in the header or log body) (see §7.2), referencing the rail mismatch.

# 3\. Post-commit QA (staging/prod)

## 3.1 Intent

Prove **route posture**, **capture evidence**, and **update indices in the same PR** once changes are deployed to a staging or production-like environment.

Post-commit QA focuses on:

* confirming each surface behaves as promised (status, headers, body)

* capturing stable evidence (snapshots and proof JSON)

* updating both the **human index** and the **machine mirror** in the **same PR** that carries the evidence

Concrete schemas, tokens, and CI wiring live in PF04, PF09, and PF12 (titles-only); PF19 defines the shared checklist.

**Workflow placement (Live QA runbooks; normative).**  
 Live QA is a required Close Gate activity when an epic’s acceptance requires it. Live QA runbooks (commands, step-by-step checks, QA\_ROOT structure, behavior-run vs artifact capture/analysis, and step deliverables) MUST be authored as separate QA work products during the Close Gate stage and stored under `audit/qa/<epic-id>/…`.

Epic Plans and implementation plans MUST NOT embed a Live QA runbook. They MUST include only a single statement that Live QA is required for eventual epic close, and may reference the governing documents by title (Epic-Process-Guide; Glow QA Guide).

Reviewers MUST NOT reject or block an Epic Plan solely because it lacks a detailed Live QA runbook, provided the plan clearly marks Live QA as required for close and routes to the governing documents by title.

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

  *  **Governed roots only:** all indexed artifacts must reside under a governed evidence root declared in the Evidence Catalog (HDE Schemas & Artifacts, titles-only); transient/generator paths are forbidden as evidence sources.  
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

This section describes a **manual Live QA execution pattern** that is generalized across epics. It is designed to produce **mechanical, reviewable evidence** under the epic QA root without introducing hidden dependencies, git gates, or non-canonical runners.

### **3.4.1 Execution pattern: one command → one primary artifact**

Each manual Live QA check consists of:

* one CLI command, or

* one HTTP command, or

* a very small, self-contained inline script (embedded in the step and written under the epic QA root before execution),

run from a Codespace attached to the engine repo.

Each check MUST identify:

* one **primary artifact** under `audit/qa/<epic-id>/…` that is mechanically produced, and

* clear PASS/FAIL predicates expressed only in terms of the bytes/content of that primary artifact (no screen-only acceptance).

* Determinism predicate targets (normative; ADR-001 surfaces lock; no wrappers/markers): determinism remediation predicates for D16–D18 MUST validate the canonical emitted surfaces below and MUST NOT require wrapper bundles or extra non-canon marker lines. Canonical predicate targets (required surfaces \+ required sibling path-proofs) include:

  * D16 orientation demo: `audit/gates/topology/orientation_demo.txt` (+ `audit/gates/topology/orientation_demo.txt.path_proof.txt`)  
    * If a plan requires EPIC-scoped orientation demo artifacts, they MUST be treated as **supporting artifacts** (not replacement predicate surfaces) and MUST be derived from `audit/gates/topology/orientation_demo.txt` (example: `artifacts/hde-epic023_orientation_demo/orientation_demo_report.json`, `artifacts/hde-epic023_orientation_demo/sample_result.json`).

  * D17 env pins: `audit/gates/determinism/env_pins.log` (+ `audit/gates/determinism/env_pins.log.path_proof.txt`)

    * The first JSON record MUST be a compact object with keys: `env` (object), `status` (string), `suites` (array). Validators MUST NOT require schema, rails, or other wrapper fields.

  * D18 sanity: `artifacts/sanity/sanity.log` (+ `artifacts/sanity/sanity.log.path_proof.txt`)

    * Validators MUST accept the canonical structure (header `sanity_pipeline`, then `env:`, then one-or-more check …, ending with `summary:PASS`) and MUST NOT require `run:sanity-pipeline` or `env_pins:` marker lines.  
  * D19 canonical JSON gate check log: `audit/gates/canonical_json/json_canonical_check.log` (+ `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`)  
    * Minimal predicate: the file parses as **JSON-per-line** and contains **at least one** record with `status: "pass"` (do not tighten beyond “pass observed”).  
  * D20 canonical JSON gate compare log: `audit/gates/canonical_json/json_canon_compare.log` (+ `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`)  
    * Minimal predicate: the file parses as **JSON-per-line** and contains **at least one** record with `status: "pass"`. Additional compare facts MAY be logged, but MUST NOT be required by validators.  
  * Path-proof naming is locked: for these canonical surfaces, the path-proof MUST be the full filename plus `.path_proof.txt` (including the original extension), e.g., `env_pins.log.path_proof.txt` (not `env_pins.path_proof.txt`).

  * **HDE Phased Epics** MUST NOT be cited to define evidence surface paths, evidence shapes, or remediation predicate targets. Plans/remediations MUST cite the governing single homes (for example: **HDE Build Notes**, **HDE-Build Checklist**, **Epic-Process-Guide**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Governance**) as applicable.

If a check needs more than one primary artifact, it is not a single check; split it.

### **3.4.2 Tooling discipline (normative; no hidden dependencies)**

Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is explicitly canon-named by repo path (titles-only routing here; the plan must provide the explicit path).

**No invented entrypoints (normative).** A plan MUST NOT require an executable entrypoint (examples: `python -m <module>`, `bash <script.sh>`, `./<tool>`) unless one of the following is true:

* **Repo-proven:** the entrypoint is a real, versioned repo surface (module/script) that exists at the specified path/module name at execution time, or

* **Canon-defined:** the entrypoint is explicitly defined by PF canon as a required tool surface, or

* **Explicitly created:** the plan includes explicit creation instructions for the entrypoint (either as a prior DEV PR task that adds it to the repo, or as an OPS step that creates an ephemeral helper under `/tmp`).

**Evidence roots are not code roots (normative).** `audit/**` and `artifacts/**` are evidence/output roots. A plan MUST NOT treat files under `audit/**` or `artifacts/**` as pre-existing runnable code (scripts/modules). If an OPS procedure needs helper code, it MUST be created ephemerally under `/tmp`, and only the resulting evidence outputs are written under `audit/**` or `artifacts/**`.

If a check needs tooling beyond baseline CLI/HTTP commands, it MUST be either:

* a canon-named entrypoint by explicit path, or

* an inline tool whose full source is embedded in the step and written under `audit/qa/<epic-id>/…` before execution (no hidden dependencies).

**QA vs remediation separation (normative).** Remediation plans MAY instruct reruns of QA checks, but they MUST use the approved QA plan’s canonical command(s) or an existing repo harness. Remediation plans MUST NOT mint new “QA runner” entrypoints purely to mirror check IDs (for example `python -m …check_<id>…`) unless a DEV PR explicitly introduces those entrypoints as versioned repo code.

**Preflight existence check (normative).** Any OPS step that invokes a repo-provided entrypoint MUST include a preflight check that proves it exists before attempting the run. Examples:

* For Python modules: `python -c "import <module>; print('OK')"`

* For scripts: `test -f <path> && test -x <path> || (echo "MISSING"; exit 2)`

If the entrypoint does not exist, the run is `TOOLING_BLOCKED` and the operator MUST stop and capture the transcript as evidence.

Plans that reference non-canon script paths as “required tooling” are non-conforming and MUST be rewritten to avoid the dependency (prefer baseline commands).

This rule does not forbid canon tooling already in-repo; it forbids invented harness scripts, unproven helper paths, and non-existent entrypoints.

### **3.4.3 Evidence layout: current-state first (new posture)**

Run-id discipline is not a correctness mechanism. The canonical evidence posture is **current-state** under the epic QA root:

* `audit/qa/<epic-id>/`

Each check’s canonical primary evidence is a single primary log/artifact referenced by the epic-level step-log manifest:

* `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
* `audit/qa/<epic-id>/checks/<check_id>/primary.log (one canonical primary log per check_id; referenced by the manifest)`

**KISS evidence posture (normative).** Live QA plans MUST minimize required outputs to the per-check primary log and the step-logs manifest. Nothing else is auto-required unless canon explicitly pins a governed evidence family/path. Any additional required artifact must be explicitly justified as acceptance-decisive and must be canonized (PF10 or PF-canon) as a governed evidence family/path.

Optional per-run directories MAY exist for history retention:

* `audit/qa/<epic-id>/runs/<run_id>/…`

but they are non-canon unless explicitly promoted. Plans and reviewers MUST NOT require per-run nesting to validate correctness.

### **3.4.4 Primary artifact discipline (what counts as evidence)**

The primary artifact for a check is mechanically generated by the command, and its presence/contents determine PASS/FAIL for that check.

* Any supplemental artifacts (stdout/stderr captures, helper JSON, diffs, secondary logs) are additive but do not replace the primary artifact.  
* Evidence must be deterministic and stable. Unstable output (nondeterministic ordering, timestamps, random salts) is a bug in the step/toolchain, not a reason to weaken QA rails.  
* Canonicalization is required for governed bytes (hash inputs, snapshot payloads, indexed artifacts). Canonicalization must be mechanical and described in the check.

### **3.4.5 Command transcript requirements (mechanical; no screen-only acceptance)**

Each check MUST capture a command transcript at minimum:

* the command line invoked,  
* the exit code,  
* stdout/stderr (or references to captured files).

Transcripts MUST be stored under `audit/qa/<epic-id>/…` and referenced by the primary artifact (or be the primary artifact when the check is log-based).

For commands that may be noisy or long-running, tee stdout/stderr to a log file under the epic QA root (example pattern: `audit/qa/<epic-id>/checks/<check_id>/stdout.log`), but keep the primary artifact definition unchanged.

### **3.4.6 Step-level Deliverables (no screen-only acceptance)**

For any QA guide, runbook, or PF10 QA addendum that defines stepwise QA execution, each check MUST include a Deliverables subsection naming the **minimal evidence set** created or updated by that check.

**Requirements (normative):**

* **Fully-qualified paths:** Every deliverable MUST be listed with a repo-relative, fully-qualified path (for example `audit/qa/hde-epic021/checks/d3_internal_version/primary.log`).  
* **Presence rules:** A deliverable is either required to exist, required to be absent, or required to have a specific content signature. Vague phrasing ("should", "nice-to-have") is forbidden.  
* **Primary artifact discipline:** Each step MUST define exactly one primary artifact (the canonical evidence surface) and may optionally define supporting artifacts.  
* **No screen-only acceptance:** Screenshots are allowed as supporting evidence, but MUST NOT be the sole basis for PASS/FAIL.

### **3.4.7 Command formatting (copy/paste-ready)**

* All shell commands MUST be presented in copy/paste-ready form. A reviewer must be able to run the command(s) without reconstructing punctuation, flags, or paths.

  * Fenced code blocks are OPTIONAL and MUST NOT be treated as an approval gate.

  * If the plan may be consumed in a plain-text venue (or rendering is unknown), avoid markup that breaks copy/paste (e.g., do not wrap every line in backticks).

* Commands MUST avoid placeholders like `<...>`. If a path varies, provide the exact expected path shape and at least one fully-qualified concrete example.

* If a command is destructive (writes to governed artifacts), include an explicit “STOP if output contains …” line before it, describing what would invalidate the step.

### **3.4.8 Rails posture for manual Live QA (EPIC017 example; generalized rule)**

Manual Live QA steps that touch production endpoints run with open rails as required by the command (for example `ALLOW_NETWORK=1`, `SAFE_MODE=0`).

Manual Live QA MUST NOT modify code or configuration **except** for minimal, in-session remediation under the **Moon Loop** policy below. Evidence outputs MUST still be written under `audit/qa/**` for governed evidence.

**Moon Loop (allowed; minimal in-session remediation to unblock QA):**

Live QA may include a small remediation loop when a check fails due to an execution-blocking mismatch, only to the extent required to produce a PASS-grade proof for the already-approved scope.

The only goal is to unblock the existing QA check and prove the existing implementation works.

**Hard boundary: no scope expansion.** In-session remediation MUST NOT:

* add new features or acceptance criteria

* change public contracts

* mint new tokens

* introduce new evidence families

* turn QA into a second remediation plan

**Allowed remediation actions (minimum set):**

* Create small helper scripts under `/tmp` for parsing or glue (strictly ephemeral; never treated as evidence).

* Adjust the QA check procedure to use the canonical emitted surfaces (paths and shapes) already required by canon and implementation.

* Apply the smallest code or script change that is required for the check to execute and validate behavior, when the failure is clearly a tooling or expectation mismatch (not a new feature).

* Re-run the affected check(s) and capture the PASS-grade evidence artifacts.

**Evidence posture for in-session remediation.** If remediation occurs inside a QA session, the existing primary evidence artifacts MUST make it auditable without additional documents:

* The failing check’s primary log MUST include the failure signature (short excerpt).

* The same log (or the session transcript) MUST include a one-line remediation note that names exactly what changed (file paths) and why.

* The rerun output showing PASS MUST be captured in the same evidence stream.

* If any repo files were changed, capture a minimal delta artifact under a lowercase governed path, for example:

  * `audit/qa/<epic-id>/remediation/moon_loop/patch.diff` (or equivalent)

  * `audit/qa/<epic-id>/remediation/moon_loop/changed_files.txt` (paths \+ sha256)

  * This delta capture must not discuss branches, commits, or PR workflow.

**Stop condition.** If the remediation required is not “minimal” (multiple files, unclear root cause, or changes beyond the failing surface), stop the Moon Loop and escalate to a normal remediation plan.

**/tmp helper scripts (allowed; execution-only; non-evidence):**

QA agents MAY create ephemeral helper scripts under `/tmp` during Live QA execution.

These scripts are execution-only and MUST NOT be treated as deliverables or governed evidence.

* Outputs under `/tmp` MUST NOT be indexed, mirrored, path-proofed, or referenced as acceptance binding surfaces.

* Any evidence artifacts produced by a step MUST still be written under the epic QA root (for example under `audit/qa/<epic-id>/…` as used throughout this guide).

* `/tmp` helper scripts MUST NOT print or persist secrets.

Closed-rails testing (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) remains the responsibility of:

* CI jobs wired in the repo, and

* pre-merge QA on PRs implementing the epic.

Manual Live QA does not attempt to replicate the full closed-rails surfaces via open-rails commands from Codespaces into Railway.

### **3.4.9 No VCS workflow content (normative; artifact-based PASS/FAIL)**

Live QA Plans MUST be artifact- and evidence-driven. They MUST NOT embed version-control workflow steps.

* **No VCS workflow content (hard).** A Live QA Plan MUST NOT instruct on, assume, or require any version-control workflow, including:

  * branches, commits, pushes, PR creation/updates, merges/rebases, conflict resolution, or “git workflow” steps  
  * requirements about “what branch to be on” or “what commit SHA to record”

* **No PASS/FAIL gated on VCS state (hard).** PASS/FAIL MUST NOT be determined by working-tree cleanliness, branch name, commit hash, or any other VCS state. These are not behavioral evidence and can vary between execution environments.  
* **Optional non-gating repo-root sanity checks (allowed).** A plan MAY include a small read-only sanity check to confirm it is running in a repository (e.g., `git rev-parse --show-toplevel`). If such a sanity check fails:

  * classify the affected check as `TOOLING_BLOCKED` (not `FAIL_BEHAVIOR`)  
  * continue with other non-dependent steps when possible  
     A plan using a sanity check MUST NOT mutate repo state (`git checkout`, `git commit`, `git clean`, etc) and MUST NOT require PR metadata or a specific branch/commit.

* **Known Codespaces packaging artifacts.** Codespaces sometimes includes `.codespaces/.persistedshare` and/or `*.tar` artifacts that can trigger `git status` noise. These are non-blocking for QA; do not gate on them.

If a plan currently requires “clean git status” as a precondition, update it. The plan should focus on the artifacts it produces and the behavior it verifies.

### **3.4.10 Plan validity lint (blockers-only; deterministic)**

Before execution, QA reviewers MUST treat the following as hard blockers (plan is not valid until corrected):

* References acceptance tokens that are undefined or not present in the canonical registry.

* Contains unverifiable claims (“works”, “should”, “looks good”) without an artifact path or exact command to reproduce.

* Depends on helper scripts or harnesses outside the canonical harness directory without a pinned version/path reference.

* Requires writing outside the governed QA write roots (`audit/**` or `artifacts/**`).

* Contains VCS workflow content (branches/commits/PRs) or gates PASS/FAIL on VCS state.

  * Exception: an optional read-only repo-root sanity check is allowed if it is explicitly non-gating; if it fails, the outcome MUST be `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`.

* References required artifact/file paths that are not canon-defined and are not explicitly created by the plan under the governed QA write roots (no fabricated paths).  
* Requires any PF23 consult capture deliverable (e.g., `pf23_consult.md`) or includes PF23 operator commands as execution steps (PF23 consult is planning-time only; any trace belongs in plan text only and MUST be non-gating).  
* Declares Step-0 artifacts as required but does not specify how/where they are produced and recorded (see PF27 — Plan Templates and, for Codespaces runs, §14.6).  
* Assigns PASS to a step without any evidence capture (log path, output file, or deterministic command output).

### **3.4.11 Vendor and DB safety constraints (names-only)**

Even under open rails:

* Vendor/production write flows that resemble real user writes remain out of scope unless explicitly permitted by current product posture.  
* Live QA must use dry-run or closed-rails stubs where the canon requires it.

### **3.4.12 Doc-alignment steps (mechanical, not narrative)**

For doc-alignment Live QA steps:

* Steps MUST rely on mechanical commands (ls, grep, find, python tooling) that generate tree listings, filtered file lists, or diffs.  
* Outputs MUST be written under `audit/qa/<epic-id>/…` as primary or helper artifacts.  
* Close report requirements (validator-bound; mechanical): epic close reports (for example `audit/EPIC-023_close_report.md`) MUST include:  
  * the heading `QA Rails — Open/Close (Final PR)` (verbatim), and  
  * an “Acceptance and evidence pointers” list containing the epic’s canonical pointer strings (exact text). Example (EPIC-023):  
    * `docs/acceptance_map_epic023.json`  
    * `audit/qa/hde-epic023/token_evidence_matrix.md`

  * `audit/qa/hde-epic023/acceptance_map_viability.log`

  * `audit/qa/hde-epic023/qa_step_logs_manifest.json`

* The close report check validates required pointer strings as literal substrings; missing any required pointer is a mechanical FAIL for the close report check.  
*   
* PO/operator must not be required to write prose summaries as part of execution. Narrative synthesis belongs in the close report and canon updates (titles-only routing).

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

**Auth posture is not yet canonized (non-invention rule).**  
 PF canon defines the `/internal/version` transport and content contract, but access-control semantics are not yet canonized. Until a canon decision is made, Live QA plans, remediation guides, and operational tooling MUST NOT assume whether `/internal/version` is unauthenticated public, operator-network gated without auth, or auth-header required.

If an auth header is used in an operational context, it MUST be treated as observed evidence only: record presence-only (never the value) and do not encode the posture as canon in runbooks.

**Evidence required to canonize auth posture (secret-free).**  
 To canonize `/internal/version` auth posture, capture headers for the canonical deployment context(s) under two conditions:

* with no auth header, and

* with the expected auth header present (value redacted or presence-only noted).

The evidence MUST be secret-free and stored in-repo under a lowercase audit path under the epic QA root. The evidence must be sufficient to decide the intended posture and the expected failure mode for missing or invalid access (status code and headers).

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

**/internal/version acceptance token names (canonical; non-aliasable).**  
 Acceptance token names for `/internal/version` MUST match the names defined in **HDE-Governance**. Tools, guides, matrices, and acceptance maps MUST NOT invent aliases.

* Canonical conditional semantics token name (normative): `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`  
   Any other name intended to mean “conditionals return 200 and never 304” (including `INTERNAL_VERSION_COND_200_NO_304_OK`) is non-canon and MUST NOT be emitted or required in acceptance artifacts.

* If a tool currently emits a non-canon alias, remediation MUST treat that as a defect and plan to converge to the canonical naming.

**/internal/version proof surface: explicit invariant checklist (required).**  
 Any remediation guide, QA step, or probe tool that produces `/internal/version` governed evidence MUST explicitly enumerate and verify the canon-critical invariants below. It is not acceptable to imply these checks by referencing PF sections only.

Canon-critical invariants (minimum set) for the canonical `/internal/version` identity response:

A) Transport

* GET MUST return 200\.

* HEAD MUST return 200 and satisfy parity expectations.

* Conditional requests (`If-None-Match`, `If-Modified-Since`) MUST NOT yield 304; they MUST return 200\.

B) Headers

* `Cache-Control: no-store` MUST be present.

* `Content-Type: application/json; charset=utf-8` MUST be present.

* `ETag` MUST be absent.  
* `docs/ENDPOINTS_CATALOG.json` MUST include `/internal/version`, and the catalog entry MUST set `a7_eligible: false` (inventory posture; `/internal/version` is not an A7 surface).

* `Last-Modified` MUST be absent.

C) Body (identity payload)

* Body MUST be fixed-schema JSON with exactly these keys (no extras):  
   `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`

* Body bytes MUST satisfy the canon “identity bytes” posture where applicable to the proof surface (canonical bytes, including LF termination).

**Token emission gating (no “false OK”).**  
 A tool MUST NOT emit any `*_OK` token unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run.

**FAIL\_TOOLING semantics (normative).**  
 If the run status is `FAIL_TOOLING` (or equivalent), the tool MUST NOT emit `*_OK` tokens for invariants that did not pass. In particular, it MUST NOT emit “integrity success” tokens (for example path-proof match or two-run identity) unless those checks demonstrably passed on the produced artifacts.

**Coupling requirement (anti-mixed-target / anti-redirect drift).**  
 For each probe run, the evidence must be coupled such that the emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit `*_OK` tokens

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

The QA plan **MUST** then describe how artifacts from the behavior environment are brought into the canonical QA tree under `audit/qa/<epic-id>/…` and analyzed. At minimum, Live QA instructions **MUST** include copy/paste-ready commands (fenced blocks optional) that:

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

**Ops gap / service readiness (prod/internal surfaces; normative).**

Some HTTP surfaces (especially prod/internal endpoints) can appear “blocked” due to operational enablement gaps (unknown auth posture, unknown token sourcing, missing allowlists) rather than code regressions. QA MUST treat these as TOOLING until enablement is established.

When an HTTP surface is unreachable or returns an access error and the operational enablement posture is not established, QA MUST:

* classify the step as `TOOLING_BLOCKED` / `FAIL_TOOLING` (not `FAIL_BEHAVIOR`), and

* record it explicitly as an **ops gap** (missing or unclear enablement), not as a product behavior regression.

**Deferred-auth token sourcing contract (non-invention; normative).**

If a runbook or tool uses an auth header (or any credential input) for an HTTP surface, it MUST state where that input is sourced from (role/owner and mechanism) and how it is enabled.

If token sourcing is not established, the runbook MUST treat the auth header as optional evidence only:

* do not require it as a prerequisite for planning or execution, and

* only use it as a branch condition when the surface returns 401/403 and the runbook is explicitly testing the authenticated path.

Credential values MUST never be recorded in PF19 or QA evidence; presence-only is permitted where needed.

**HTTP capture hygiene (stderr separation; normative).**

Header/body evidence artifacts MUST be parser-safe:

* Header capture files intended to represent HTTP headers MUST contain only the HTTP status line and header lines. Tool warnings and stderr output MUST be captured separately.

* If a tool emits warnings during a capture, store them in a dedicated stderr artifact under `audit/qa/<epic-id>/…` and do not interleave them into the header evidence file.

This rule is about evidence portability and preventing false failures in downstream validators.

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

  * classify the step as a tooling/infra failure in the log header using `status: FAIL_TOOLING` or `status: TOOLING_BLOCKED` (per §4.4) and include a short `reason`, and

  * route the failure as an infra/service readiness remediation item (for example missing dev harness wiring, wrong port/protocol, or missing start command), not as an application behavior failure.

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

* classify the step as a behavior failure in the log header using `status: FAIL_BEHAVIOR` (per §4.4) and include a short `reason`, and

* route the failure through the normal bug/epic remediation process (for example PF10 addendum, HDE Phased Epics update, code fixes).

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
   * Live QA plans MUST NOT invent flags or subcommands that do not appear in the current help output.  
4. **Record environment posture and rails intent.**  
   * Capture a short, mechanical summary of the intended rails posture for Live QA in this epic (for example, “Codespaces open-rails: SAFE\_MODE=0, ALLOW\_NETWORK=1” or “CLI runs only in closed dev harness”).  
   * Use a simple command such as:  
     * `env | sort | grep -E 'SAFE_MODE|ALLOW_NETWORK|APP_ENV|HDE_BASE_URL'`  
   * Store this in `audit/qa/<epic-id>/d0-planning/d0-env-rails.txt`.  
5. **Verify .gitignore rails for `audit/qa/<epic-id>`.**  
   * Inspect the repo’s `.gitignore` (and any additional ignore files) to confirm that canonical QA trees under `audit/qa/<epic-id>/…` are **not** ignored:  
     * there are no broad ignore patterns that match `audit/qa/**` without corresponding allow rules, and  
     * `audit/qa/<epic-id>/…` is visible to git without requiring forced adds.  
   * Capture the relevant `.gitignore` excerpts and a short mechanical check under, for example:  
     * `audit/qa/<epic-id>/d0-planning/d0-gitignore-audit-qa.txt`  
   * Git commands MAY be used for inspection only during D0 introspection (including in the Codex prompt that produces the plan). Results are traceability-only and MUST NOT be used as gates.  
   * (for example by using `grep` and optionally `git check-ignore` to show that `audit/qa/<epic-id>` is not matched by any ignore entry; this check is informative only and MUST NOT block planning or execution).  
   * If existing ignore patterns hide canonical QA roots (for example legacy `Audit/QA/**` or `audit/qa/**` rules), the IA must:  
     * coordinate with the build/infra owner to tighten or remove those patterns so that `audit/qa/<epic-id>/…` is tracked; and  
     * capture the change and its rationale in PF10 build notes or PF20 acceptance records (titles-only), referencing this section of PF19.

**D0 QA tooling bootstrap (names-only)**

Before a Live QA plan can be treated as runnable (and before any dependent acceptance tokens can be claimed), the IA SHOULD run a short, mechanical QA tooling bootstrap and capture the result as a governed planning artifact under the epic QA tree.

*Intent.*  
Prove that the QA console environment can actually execute the plan’s harness entrypoints; failure is classified as **tooling**, not as a behavior failure.

*Minimum bootstrap checks (names-only).*  
The bootstrap SHOULD verify at least:

* the preferred test invocation works in the environment (see §2.2.5 guidance on `python -m pytest`), and  
* the plan’s required QA harness entrypoints (tests/scripts) are present and runnable under the intended rails.

*Bootstrap log requirements (minimum fields).*  
The bootstrap **MUST** produce one primary bootstrap log file (governed artifact under the epic QA tree) that includes a header block with at least:

* `qa_root` (the intended QA\_ROOT for the run, even if the run has not been created yet),  
* `command` (the bootstrap command(s) actually executed),  
* `rails` (the rails posture, including env pins), and  
* `status` (PASS or FAIL\_TOOLING / TOOLING\_BLOCKED).

If bootstrap fails, the plan **MUST** treat all dependent steps as blocked by tooling, and the epic must not claim tokens that depend on the blocked harness.

**Acceptance-map / QA-plan viability check (names-only)**

For any epic that uses an acceptance map and QA harness scaffolding, the IA **MUST** run an explicit **viability check** before Live QA:

*Intent.*  
Prevent “plan references assets that do not exist” failures by verifying that acceptance-map and plan references resolve to real scripts, real pytest nodes, and real QA tree paths in the current branch.

*Minimum viability behavior.*  
The viability check MUST:

* walk the epic acceptance map file under `docs/` (for example `docs/acceptance_map_epic0xx.json`) and any referenced manifest(s), and  
* verify that every referenced script path, test path or node (pytest discovery), and QA-tree path is resolvable on disk in the branch being tested.

*Viability report artifact.*  
The viability check MUST emit a deterministic, reviewable viability report under the epic QA tree (for example `audit/qa/<epic-id>/acceptance_map_viability.log`). The report MUST include:

* the acceptance map path examined,  
* a summary of resolved references, and  
* a list of any missing or broken references.

If any referenced asset is missing or non-runnable, the viability report MUST classify this as **FAIL\_TOOLING / TOOLING\_BLOCKED**, and Live QA MUST NOT proceed until the plan or the referenced assets are corrected.

These two gates are required planning artifacts for epics that claim acceptance scaffolding is complete: without a passing tooling bootstrap and a passing acceptance-map viability report, QA must treat the epic’s harness as non-viable for Live QA and for token claims that depend on it.

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

* treat `hdctl --version` output as canonical identity evidence; or  
* treat `hdctl --version` output as a release contract; or  
* treat `hdctl --version` output as a gating signal for pass/fail.

If `hdctl --version` is run at all during D0, its behavior is informational only and MUST NOT be used as a basis for pass/fail judgments.

*Planning rule.*

* The D0 CLI baseline step’s primary log header (see §4.4) MUST describe the baseline in these terms (presence and help, not version semantics).  
* If captured help output disagrees with the commands/flags used in the draft plan, the IA MUST revise the plan and treat the mismatch as a planning defect requiring clarification before involving the PO in Live QA, not as a behavior failure in later steps.

This pattern applies to EPIC020 and to all future epics that require D0 CLI baseline: the plan’s CLI baseline MUST be **“derived from canon and repo reality”**, not undocumented `--version` behavior.

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

## **4.2 What to capture**

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

* **Conditional capture: release identity and Freeze-Pack Manifest (when in scope).**

   If a QA plan, CI gate, or acceptance claim depends on release identity or Freeze-Pack Manifest coherence, the run MUST capture the canonical release-identity surfaces as governed evidence (titles-only for schema/semantics):

  * SoT manifest: `catalog/manifest.json`

  * Freeze-Pack Manifest evidence copy (byte-identical to SoT): `artifacts/math/freeze_pack_manifest.json`

  * Release identity value: `artifacts/math/release_id.txt`

  * Release identity recompute log: `artifacts/math/release_id_recompute.log`

* These files MUST be produced mechanically by canonical tooling and MUST be indexed and path-proved like other governed artifacts.

   Evidence-only summaries (for example manifest snapshot summaries) MUST NOT be substituted as identity inputs or treated as Freeze-Pack SoT.

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
  * **Stale timestamp drift after a byte-changing refresh is blocking.** If a governed artifact’s bytes change (regenerated or refreshed) but its corresponding `*.path_proof.txt` (or the Mirror/Index record for that path) still reports older carried-forward `produced_at_utc` / `mtime_utc`, treat this as a provenance/audit-trail defect and rerun the evidence tooling in write mode to regenerate proofs and refresh Index/Mirror entries. Do not hand-edit timestamps. This does not apply to no-op runs where the underlying bytes did not change.

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

### **4.3.2 PROOF\_SHA mismatch triage (CI failures)**

PROOF\_SHA mismatches are **merge-blocking evidence integrity failures**. A typical signature is:

* `SystemExit: PROOF_SHA: <some.path_proof.txt> expected: <sha> found: <sha>`

When this occurs, QA MUST treat it as “evidence toolchain or governed evidence is not coherent” (not as a flaky test).

**Case A — Normal artifact mismatch (most common).**  
 If the failing path-proof is for a normal governed artifact (not the mirror self-record):

* The most likely cause is stale or hand-edited path-proof/index/mirror content or an incomplete same-PR regeneration.  
* **Common drift class (sha/size mismatch, not “just formatting”).**  
   A frequent root cause is that a governed `*.path_proof.txt` (and the corresponding mirror row) records the wrong `sha256` and/or `size_bytes` for an unchanged on-disk artifact. This can cause validators to fail or, worse, to certify incorrect evidence if checks are incomplete. Examples recorded during EPIC022 close-pack follow-ups include:  
  * ordering artifact proof drift: `artifacts/engine/order/abba_identity.bytes.path_proof.txt` recorded metadata that did not match the actual `artifacts/engine/order/abba_identity.bytes` bytes, and the mirror record required refresh to match; and  
  * stale human-index proofs: `docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt` were left stale after regenerating INDEX bytes.

**Remediation is always the same:** regenerate Index, Mirror, and path-proofs via the canonical evidence tooling until check mode passes. Do not hand-edit proofs or mirror rows to “make the error go away.”

* Remediation is to regenerate governed evidence (Index, Mirror, and path-proofs) using the canonical evidence toolchain and then re-run the check sequence (write, then check) as described in §2.2.11. Do not patch the PROOF\_SHA line by hand.

**Case B — Mirror self-record / evidence self-reference mismatch (high-risk special-case).**  
 If the mismatch involves the machine mirror’s own self-record or a proof that is derived from mirror hashing semantics:

* Treat it as an evidence-tooling / validator coherence issue.

* Any PR that changes evidence index/mirror generation or validation MUST update/confirm the dedicated regression test for self-record semantics (for example a “machine mirror self proof” test) and must include a log excerpt of that validation passing in the PR evidence.

**Non-canonical mirror path warning.**  
 PF19’s canonical machine mirror is `artifacts/evidence_index.jsonl` (single file). If CI output references a path such as `docs/evidence/INDEX.machine_mirror.jsonl.path_proof.txt`, QA MUST treat that as a contract ambiguity or mis-invocation:

* do not bind acceptance tokens to that path, and

* restore the canonical posture: single mirror file at `artifacts/evidence_index.jsonl`, indexed and proven via its canonical path-proof.

**Interactive-shell safety (normative; operator-facing QA instructions).**

QA plans, Live QA guides, and remediation guides often include copy/paste-ready commands intended for execution in an interactive terminal session (PO or IA). Those instruction blocks MUST be “interactive-safe”:

* Do not include shell-terminating control flow in paste blocks (for example `exit`, `return` used as a hard stop, or constructs that intentionally close the operator’s shell).

* If a strict enforcement check needs a failing exit status, it MUST be isolated so it cannot terminate the operator’s session. Acceptable patterns include:

  * run the enforcement in a subshell and capture its exit status into a file under `audit/qa/<epic-id>/…`, or

  * write an explicit PASS/FAIL status artifact (plus stderr/stdout captures) and let the operator continue the session.

* Operator-facing instructions MUST treat “session survival” as a first-class constraint: evidence capture MUST continue even when a check fails.

This rule is about runbook safety and evidence completeness. It does not weaken any QA predicates or acceptance criteria.

## **4.4 QA evidence file structure and step logs**

PF19 expects QA evidence to be not only complete and indexed (§4.2–§4.3), but also reviewable. QA Plans and Live QA runs MUST adopt a consistent step-log structure under the epic’s QA root inside the governed audit tree.

### **4.4.1 Epic QA root and current-state posture (normative)**

**Epic QA root (canonical):**  
`audit/qa/<epic-id>/`

**Current-state is canonical.**  
QA evidence is governed primarily as **current-state** under the epic QA root. “Run-id discipline” is not a correctness mechanism. Optional per-run directories MAY exist for history retention, but they are non-canon unless explicitly promoted.

**What PF19 requires at the epic root:**

* A per-epic step-log manifest at:  
  `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
* Canonical per-check primary logs referenced by that manifest (see §4.4.3).  
* Epic-level QA ledger artifacts (token/evidence matrix, viability log) as applicable (titles-only routing to their owning PFs).

PF19 does not prescribe a single naming convention for optional per-run retention. It requires that the epic-level, current-state evidence is unambiguous and reviewable without hunting across ad hoc trees.

### **4.4.2 Optional retention: per-run directories vs evidence buckets (clarification)**

Under `audit/qa/<epic-id>/`, an epic MAY keep:

* **Optional per-run retention directories:**  
  `audit/qa/<epic-id>/runs/<run_id>/...`  
  These exist for operator convenience/history retention only. They are non-canon by default. They MUST NOT be required for closure and MUST NOT be used for canonical keying.  
* **Evidence bucket directories:**  
  Directories (for example `live-qa/`, `snapshots/`, `bundles/`) that hold auxiliary materials. These are not “runs,” and they are not required to contain bootstrap or step logs.

Tools and reviewers MUST NOT infer run history or current status by enumerating subdirectories. The per-epic manifest is the authoritative index of current-state step evidence.

### **4.4.3 Per-epic QA step logs manifest (qa\_step\_logs\_manifest.json)**

**Canonical path:** `audit/qa/<epic-id>/qa_step_logs_manifest.json`

**Purpose:** A machine-readable index of all per-check “primary logs” under the epic’s QA root, used by review tooling and by the QA acceptance map to link checks → evidence.

**Routing (normative):** Live QA runbook template structure and step-log header schema are owned by PF27 — Plan Templates; this guide does not define alternate header schemas.

**Requirements (normative):**

* The manifest MUST be valid JSON and MUST be an object keyed by `check_id`.

* There MUST be at most one entry per `check_id`.

* Each entry MUST include:

  * `check_id`

  * `log_path` (relative path from `audit/qa/<epic-id>/` to the canonical primary log)

* `log_path` MUST be a relative path within the epic QA root and MUST NOT point outside `audit/qa/<epic-id>/…`.

* **No fabricated paths (normative):**

  * Plans and runbooks MUST NOT mint required artifact paths. A `log_path` entry MUST point to a real canonical primary log produced by the corresponding check, under the governed QA root.

  * If a required log path is missing at evaluation time, it MUST be treated as a tooling/prerequisite failure (e.g., `TOOLING_BLOCKED` for missing prerequisite inputs/artifacts, or `FAIL_TOOLING` when the harness/tooling fails), not `FAIL_BEHAVIOR`.

* Plans MUST distinguish pre-existing inputs (which may be presence-checked before running a step) from QA-produced artifacts (which MUST NOT be required to exist prior to the step that produces them).

* This manifest is current-state only. Old run logs may be retained under `runs/<run_id>/…`, but are non-canonical and MUST NOT be referenced by `log_path`.

* A uniqueness validation failure (duplicate `check_id` keys) is a FAIL\_TOOLING / TOOLING\_BLOCKED condition. Downstream tools MUST NOT consume a manifest that violates uniqueness.

### **4.4.4 Primary step logs (one per check\_id; canonical)**

**One primary log per check.**  
For each QA check that produces evidence, there MUST be exactly one **canonical primary log** referenced by the manifest for that `check_id`.

**Canonical path (normative; KISS default for Live QA checks)`:`**

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
* This `primary.log` \+ `qa_step_logs_manifest.json` requirement applies even when a step is posture-only / `TOOLING_BLOCKED` (for example when validation logic is not yet implemented): the canonical `primary.log` MUST still be emitted and the manifest MUST still be updated.  
* For posture-only / `TOOLING_BLOCKED` steps, `intended_tokens` and `claimed_tokens` MUST be empty (or omitted) and MUST NOT claim acceptance tokens.  
* Examples of posture-only check\_ids: `D22_canonical_json_gate_structured_record`, `D23_evidence_index_snapshot_artifact`.

For Live QA checks, the manifest log\_path MUST point to checks/\<check\_id\>/primary.log. If a canon-governed evidence family defines a different primary-log location, treat that location as the canonical log path and point the manifest to it.

A plan MAY store primary logs in another stable location under the epic QA root, but the manifest must point to the canonical log path.

**Non-empty requirement.**

* The primary log MUST be a non-empty, LF-terminated text file.  
* It MUST NOT be zero bytes.  
* If a step fails to complete or tooling fails, the primary log MUST STILL be written and MUST contain:  
  * a short summary of what the check attempted, and  
  * a terse failure description and final status line consistent with the status semantics below.

**Empty files.**  
Governed Live QA evidence files (primary logs, env snapshots, planning outputs) MUST NOT be empty:

* If a planned artifact is not produced, the file MUST be absent rather than present with size 0\.  
* Path-proofs and Machine Mirror records MUST NOT point to zero-byte QA artifacts.

Exception: clearly marked sentinel markers MAY be empty but MUST NOT be referenced by the Human Evidence Index or Machine Mirror, and MUST NOT be used as governed evidence for any QA token.

### **4.4.5 Step log header (required fields; token semantics are claims-safe)**

**Header normalization (allowed; reviewer-of-record; no rerun required).**  
 If a primary step-log header is missing any *defaultable* fields, a QA reviewer-of-record MAY mechanically normalize the header by adding the missing fields with empty defaults and re-serializing the header as canonical JSON.

Defaultable header fields (non-blocking; default to empty when omitted): `pf_refs`, `intended_tokens`, `claimed_tokens`.

Token-claim safety (normative): token claims MUST NOT be inferred. If `claimed_tokens` is missing or empty, treat the step as claiming **no** tokens. Normalization MAY include moving an explicitly stated claim into the correct header field (example: ensuring a stated token claim appears in `claimed_tokens`), but MUST NOT introduce new claims beyond what the log already asserts.

Status vocabulary (normative): `status` MUST be one of `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED`. Non-conforming status values MUST be normalized (or the step is not audit-usable).

Each per-check primary log MUST begin with a machine-readable header block on the first line, followed by the human-readable body.

**Routing (normative):** Live QA runbook template structure, the minimum step-log header schema, and the status vocabulary are owned by PF27 — Plan Templates. This guide does not define alternate header schemas.

**Minimum header fields (Plan Templates; required):**

* `check_id` — stable identifier for the check.

* `status` — a Plan Templates status value.

* `command` — the complete command/entrypoint executed for this check (copy/paste-ready).

* `captured_env` — structured snapshot of the rails/pins in effect for this check. At minimum, this MUST capture:

  * SAFE\_MODE

  * ALLOW\_NETWORK

  * APP\_ENV

  * LC\_ALL

  * LANG

  * TZ

**Token fields (optional; token-relevant only):**

Token lists are optional in runbooks and logs. Plans and reviewers MUST NOT gate approval on token-list completeness. If token fields are present, they MUST be names-only and MUST match canonical token spellings (no aliases, no near-matches).

* `intended_tokens` — tokens the check is designed to support (names-only; optional).

* `claimed_tokens` — tokens actually satisfied by verified evidence (names-only).

  * `claimed_tokens` MUST be present only when `status` is `PASS`.

  * If `status` is not `PASS`, `claimed_tokens` MUST be omitted (or present but empty).

  * When both are present, `claimed_tokens` MUST be a subset of `intended_tokens`.

* `tokens` — legacy alias for `intended_tokens` only. It MUST NOT be interpreted as claimed/satisfied tokens.

**Acceptance map — token identity and shape (normative):**

* The acceptance-map artifact MUST include a top-level `tokens` array.

* Each entry in `tokens` MUST be an object with a required `name` string field.

* `tokens[].name` is the authoritative token identity. It is case-sensitive and MUST match the token registry entry exactly.

* QA plans, validators, and token-evidence tooling MUST derive token identity from `tokens[].name` and MUST NOT infer token identity from matrix header labels or other non-registry aliases (for example `token_name`).

**Additional fields (allowed; non-gating):**

Additional header fields (e.g., `pf_refs`, a human `reason`, or other traceability fields) are allowed, but MUST NOT be required as a plan-approval condition unless PF27 — Plan Templates is updated to require them.

**Evidence-only guard proofs (normative):**

If a step claims PASS but its evidence depends on an assumption that could be false (e.g., “no output means success”), the step MUST include an explicit guard proof in the log body (e.g., a command that would have produced output on failure).

**Unregistered token handling (normative):**

If a step lists a token in `intended_tokens` or `claimed_tokens` that is not present in the registry:

* treat it as an invalid claim

* do not translate it into a “close” token name

* require the plan/PR to add the token to the registry (or to remove the claim)

**Status usage for missing paths vs wrong behavior (PF19 interpretation):**

When selecting a status value, use PF27 — Plan Templates vocabulary. PF19 relies on these distinctions when interpreting step logs and token claims:

* Missing declared prerequisites or missing required inputs/artifacts ⇒ `TOOLING_BLOCKED` (not `FAIL_BEHAVIOR`)

* Tool/harness failure that prevents running or evaluating the check ⇒ `FAIL_TOOLING`

* The check ran, but behavior contradicted the expected result ⇒ `FAIL_BEHAVIOR`

### **4.4.6 Log body and supporting artifacts**

All tests and checks for a check\_id (pytest output, grep blocks, curl output, size checks, diff results) SHOULD be appended into the same primary log in a clearly structured order (for example “=== TESTS \===”, “=== INDEX/MIRROR GREPS \===”, “=== MANIFEST CHECKS \===”).

Supporting files created by the check:

* SHOULD use a `tmp_` prefix or a clearly descriptive name (for example `tmp_sampler_request.json`, `tmp_sorted_candidates.txt`), and  
* SHOULD be either:  
  * co-located with the primary log, or  
  * placed under a single `tmp/` subdirectory inside the epic QA root.

A reviewer must be able to reconstruct what happened from the primary log alone, using supporting artifacts only when deeper inspection is needed.

### **4.4.7 Consolidation and QA quality**

A QA run that leaves behind multiple overlapping logs for the same check (for example multiple different log names in different folders without a manifest pointer) is poor-quality evidence.

To satisfy PF19 expectations:

* Each check\_id must have one clearly named primary log in the epic QA root.  
* No check should leave behind floating logs in ad hoc directories without a pointer from the manifest.  
* QA Plans MUST reference the check\_ids and where the canonical logs will live so operators and reviewers know exactly where to look.

This structure works together with the mechanical evidence rules (§4.3) and Live QA execution deliverables (§0.4.1) to make QA runs reproducible, reviewable, and easy to audit.

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

   * Update human index \+ `.sha256` and machine mirror; governed evidence roots only (roots must be declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only).

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

* Indexing discipline: update `docs/evidence/INDEX.json` \+ `.sha256` and `artifacts/evidence_index.jsonl` together; include `proof_anchor` path-proofs; governed evidence roots only (roots must be declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only).

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
* **Directory names must be lower-case ASCII (global).**  
   All directories in the repository and application codebase MUST use lower-case ASCII names. This applies to every directory, including (but not limited to): source code, scripts, schemas, catalogs, docs, artifacts, audit trees, and QA subtrees.  
* Under governed evidence roots (roots declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only), introducing any mixed-case or upper-case directory name is a QA failure, not cosmetic drift. Such directories MUST be normalized to lower-case and all affected evidence paths updated (Human Evidence Index, Machine Mirror, and path-proofs) in the same PR before any dependent QA tokens can be claimed.  
* If mixed-case directories already exist, treat them as legacy drift and normalize them to lower-case. Do not copy them forward into new specs, QA plans, or new evidence trees.  
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

---

# **9\. QA acceptance tokens**

## **9.1 Tokens glossary (names-only; sources in PF04/PF09)**

PF19 lists **names only** in this glossary. Token spellings and normative definitions live in **HDE-Governance** and **HDE-Build Checklist** (titles-only). Use this section as a quick reference; QA-facing definitions and evidence mapping live in §9.2.

### **9.1.1 Pre-commit**

* `QA_PRECOMMIT_CHECKLIST_OK`

* `DET_SERIALIZER_OK`

* `TWO_RUN_IDENTITY_OK`

* `COMPOSITE_ABBA_IDENTITY_OK`

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
* `QA_BOOTSTRAP_OK`  
* `QA_BOOTSTRAP_TOOLING_FAIL`  
* `QA_HARNESS_DISCIPLINE_OK`  
* `QA_ACCEPTANCE_MAP_VIABILITY_OK`

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
* `SANITY_PIPELINE_LOGGED_OK`  
* `QA_STEP_LOGS_CONSOLIDATED_OK`  
* `CONFIG_REGISTRY_OK`  
* `CONFIG_MAGIC10_OK`  
* `CONFIG_BUNDLES_DETERMINISTIC_OK`  
* `QA_BOOTSTRAP_OK`  
* `QA_BOOTSTRAP_TOOLING_FAIL`  
* `QA_HARNESS_DISCIPLINE_OK`  
* `QA_HARNESS_ENTRYPOINT_SELFTEST_OK`

### **9.1.7 App FE/BE (App QA docs)**

* `APP_FE_WCAG_AA_OK`

* `APP_FE_WEB_VITALS_OK`

* `APP_SEC_ASVS_MIN_OK`

*Note: App-layer token semantics live in App QA and security governance docs (titles-only); PF19 lists names only.*

---

## **9.2 QA Acceptance Tokens Registry (canonical QA token library)**

### **9.2.1 Intent**

This section is the canonical QA operational library for QA Acceptance Tokens: it provides QA-facing interpretation, evidence-family bindings, and runbook implications for the acceptance tokens used across Glow epics.

**Source-of-truth boundary (normative).** Canonical acceptance token names and their normative semantics are owned by **HDE-Governance** (and, where relevant, the **HDE-Build Checklist**). PF19 MUST mirror canonical token names exactly and MUST NOT introduce new acceptance token names or redefine existing ones.

PF19 MAY add QA-specific evidence mappings and operational guidance (what artifacts prove the token in Live QA), but those mappings MUST remain consistent with the governing definition.

If an apparently unregistered token name is discovered during planning or execution, record `CAVEAT: UNREGISTERED_TOKEN` (or `CAVEAT: UNREGISTERED_ACCEPTANCE_TOKEN` where applicable) and do not claim that token for acceptance until it is governance-registered.

---

### **9.2.2 Token metadata model (normative)**

Each token entry in this section uses the following fields:

* **Name** — canonical spelling of the token as defined in **HDE-Governance** (source of truth). PF19 MUST mirror the canonical name exactly (case, punctuation). Local aliases are non-canonical and MUST NOT be used in plans, acceptance maps, or QA logs.

* **Meaning** — short plain-English meaning.

* **QA definition** — QA-facing interpretation plus what must be demonstrated.

* **Evidence family** — the governed evidence family (and canonical artifact paths) that prove the token.

* **Operational notes** — how to run/validate in Live QA without inventing CLI or environments.

* **Owner/Source** — where to route changes (titles-only).

* **Status** — `[Required Now]`, Optional, Deprecated.

**Registry role boundary (normative).** **HDE-Governance** remains the single source of truth for acceptance token names and normative semantics. PF19 §9.2 is the canonical QA-level home for the QA operational mapping: how each token is evidenced, where outputs are stored in the QA evidence tree, and how reviewers verify the token mechanically.

Tokens MAY be referenced in acceptance maps, manifests, and QA logs only by their canonical name as defined in **HDE-Governance** (and mirrored here). PF19 MUST NOT treat a provisional or unregistered token name as acceptable for an acceptance claim.

**New token workflow (governance-first).** If Live QA planning or evidence requirements indicate that a new acceptance token is needed:

* Record the need as a doc delta item (see the Step-0 doc delta capture step required by **14.6 Ownership and maintenance**).

* Obtain governance registration of the token name/semantics in **HDE-Governance** before the token is used for acceptance claims.

* After governance registration, add/refresh the PF19 §9.2 operational entry (QA definition \+ evidence bindings) so the token can be verified mechanically.

During planning/execution, an unregistered token discovery is handled as `CAVEAT: UNREGISTERED_TOKEN` (do not block runnable behavior testing), but the token MUST NOT be claimed for acceptance until registered.

#### **9.2.2.1 Token value rubric (normative)**

QA Acceptance Tokens are for **enduring acceptance invariants**, not for workflow state, planning placeholders, or platform metadata.

A token MAY be added to this PF19 registry only if all of the following are true:

* **Value / safety invariant:** It corresponds to a user-visible value, safety property, or system invariant that must be true in shipped behavior.

* **Testable \+ evidence-bound:** It can be proven via concrete tests/CI/Live QA and governed evidence (i.e., it can be bound into §9.2.14 without inventing semantics).

* **Falsifiable \+ specific:** It has a clear pass/fail meaning; it is not “general progress”, “documentation exists”, or “someone performed a workflow step”.

* **Stable semantics:** It is expected to remain meaningful across epics (not just for a one-off implementation detail).

Tokens that fail this rubric MUST be captured as checklist items, step-log metadata, or process rails in their owning PF docs, and MUST NOT be minted as new QA Acceptance Tokens in this registry.

**Explicit non-token examples (normative).**

* **Guard proofs** are evidence-only deliverables unless and until HDE-Governance registers an acceptance token. Do not mint, request, or claim ad hoc “guard tokens.”

* **PF23 consult completion** is not an acceptance token. Plans and implementations MUST NOT mint, claim, or reference `REALITY_AUDIT_OK` (or any similar “PF23 consult completion” token) unless and until HDE-Governance registers such a token.

**Admission test (shortcut).**  
 If the answer to either question is “no”, the thing is not a QA Acceptance Token:

* “Would we ship if this token were not satisfied?”

* “Can we prove this token without inventing new token semantics?”

#### **9.2.2.2 Token retirement rubric (normative)**

A token may be marked `Deprecated` when it is redundant, superseded, or no longer represents a meaningful acceptance invariant.

Retirement rules:

* Deprecated tokens MUST NOT appear in new acceptance rosters or new token/evidence matrices.

* A deprecated token entry MUST remain in PF19 for traceability, with a brief deprecation note and (if applicable) a successor token named by canonical spelling.

* Deprecation MUST be accompanied by a migration plan in the consuming epic artifacts (acceptance maps / manifests) so that active work is not blocked by stale tokens.

This metadata model is authoritative for QA planning and EPIC acceptance.

---

### **9.2.3 Pre-commit / CI QA tokens**

#### **QA\_PRECOMMIT\_CHECKLIST\_OK**

**Owner PF:** HDE-Build Checklist  
 **Scope:** Pre-commit  
 **QA definition:** All required pre-commit checks (lint/format, canonical JSON/JSONL, determinism, env pins, mirror quick-check) have passed.  
 **Evidence:** CI logs and artifacts showing the PF09 pre-commit harness ran successfully (lint/format jobs, canonicalization checks, determinism suites, mirror quick-checks).

#### **DET\_SERIALIZER\_OK**

**Owner PF:** HDE-Mechanics Guide  
 **Scope:** Pre-commit  
 **QA definition:** The Engine serializer/composer emits byte-stable canonical JSON under determinism env pins.  
 **Evidence:** Two-run identity proofs for serializer outputs (governed JSON artifacts under `artifacts/**`), with matching Index/Mirror records and path-proofs.

#### **TWO\_RUN\_IDENTITY\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Mechanics Guide  
 **Scope:** Pre-commit  
 **QA definition:** Re-running the same CLI/API/Engine invocation yields identical governed bytes.  
 **Evidence:** Paired canonical JSON or bytes artifacts (for example `compat_ab.json` and a second-run copy) stored under `artifacts/**`, plus matching entries in the Human Index and Machine Mirror.

#### **COMPOSITE\_ABBA\_IDENTITY\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Mechanics Guide  
 **Scope:** Pre-commit  
 **QA definition:** AB and BA runs swap directional attributes correctly without unintended structural differences.  
 **Evidence:** `compat_ab.json` and `compat_ba.json` where non-directional fields match and directional fields swap as expected, with path-proofs and Mirror records aligned.

**Canonical name (normative).**  
 `COMPOSITE_ABBA_IDENTITY_OK` is the only canonical acceptance token name for AB/BA composite identity. Legacy variants (including `AB_BA_IDENTITY_OK`) MUST NOT appear as acceptance tokens in Epic Plans, acceptance maps, or token/evidence matrices.

If an epic inherits legacy wording from a document, the plan may include a one-line clarification (“legacy name → canonical `COMPOSITE_ABBA_IDENTITY_OK`”), but the claimed token name remains `COMPOSITE_ABBA_IDENTITY_OK`.

#### **ENV\_RAILS\_POLICY\_OK**

#### **Owner PF:** HDE-Governance / HDE-Build Checklist / HDE-Schemas & Artifacts  **Scope:** Pre-commit / CI  **QA definition:** The determinism env rails policy and implementation are enforced and proven using governed evidence tying CI posture to determinism-sensitive work.  **Evidence:** Combined proof that:

* #### a single canonical helper/module (for example `engine/runtime/determinism_env.py`, titles-only) defines the determinism env pins and is used by invariance/determinism tests; 

* #### invariance tests (for example under `tests/invariance/**`, titles-only) fail closed when pins are missing or mismatched and exercise log rendering/verification behavior; and 

* #### the env-rails log artifact (for example `audit/gates/determinism/env_pins.log` plus path-proof) is present, canonical JSON, indexed in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`, and consistent with the CI env posture enforced by the env-check script. 

#### These determinism env tokens work together with the general env-pin and evidence rules in §0.4.3, §2.2, and §4.3 to ensure determinism-sensitive QA always runs under a well-defined, audited env rails posture.

#### **EPIC022 example binding (closed-rails vendor refusal; normative when used as rails proof).**  If an epic uses `ENV_RAILS_POLICY_OK` to assert that explicit vendor requests are refused under closed rails, then the epic’s acceptance artifacts (acceptance map, token/evidence matrix, manifest bindings) MUST bind `ENV_RAILS_POLICY_OK` to both:

* #### the canonical determinism env pins evidence surface: 

  * #### `audit/gates/determinism/env_pins.log` (and its path-proof), and 

* #### at least one deterministic closed-rails vendor refusal scenario proof under the parity evidence family (for example `parity/errors_reader_cli.*`) plus the enforcing parity test node (for example `tests/cli/test_errors_parity.py::test_http_and_cli_parity`). 

#### This example does not redefine token semantics. It defines a QA binding expectation: “env pins exist” is not accepted as equivalent to “closed-rails vendor refusal is proven” when `ENV_RAILS_POLICY_OK` is used as the rails-proof token for a closed-rails vendor scenario.

#### 

#### **DETERMINISM\_ENV\_PINS\_OK**

**Owner PF:** HDE-Build Checklist  
 **Scope:** Pre-commit / CI  
 **QA definition:** Determinism env pins are enforced and proven using a single canonical governed evidence surface. This token is path-sensitive: it is satisfied only when acceptance artifacts bind the token to the canonical env-pins log and its path-proof.  
 **Evidence (single canonical surface; normative):**  
 `DETERMINISM_ENV_PINS_OK` MUST be satisfied only by:

* `audit/gates/determinism/env_pins.log`

* `audit/gates/determinism/env_pins.log.path_proof.txt`

When `DETERMINISM_ENV_PINS_OK` is claimed, all acceptance ledgers MUST bind to this exact path:

* the token/evidence matrix references `audit/gates/determinism/env_pins.log`

* `docs/evidence/INDEX.json` points the determinism env pins evidence entry to `audit/gates/determinism/env_pins.log`

* `artifacts/evidence_index.jsonl` mirrors that exact discovered physical path and uses `audit/gates/determinism/env_pins.log.path_proof.txt` as `proof_anchor`

`DETERMINISM_ENV_PINS_OK` MUST NOT be bound to `artifacts/proofs/env_pins.txt` (or any other similarly named file) or to any alternate path. Any deviation is a mechanical blocker.

**Clarification (non-authoritative).** Other env-pins snapshots may exist for other proof contexts. They do not satisfy `DETERMINISM_ENV_PINS_OK` unless they are the canonical surface defined above.

---

### **9.2.4 Evidence skeleton & sanity tokens**

#### **EVIDENCE\_INDEX\_UPDATED\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts  
 **Scope:** Pre-commit & post-commit  
 **QA definition:** Any change to governed evidence is accompanied by same-PR updates to the Human Evidence Index and the Machine Mirror.  
 **Evidence:** Updated `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`, with co-located path-proofs for all governed artifacts in the same PR.

#### **EVIDENCE\_INDEX\_HASH\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts  
 **Scope:** Pre-commit & post-commit  
 **QA definition:** The Human Evidence Index hash sentinel and the Machine Mirror body digest both reflect the current committed evidence index and mirror contents, as defined by PF12 Evidence Index & Machine Mirror semantics.  
 **Evidence:** A successful run of the canonical evidence-index check (for example `python tools/evidence/update_evidence_index.py --check`, titles-only) under closed rails, with no reported mismatches for the index hash sentinel or mirror body hash.

#### **MACHINE\_MIRROR\_UPDATED\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts  
 **Scope:** Pre-commit & post-commit  
 **QA definition:** The Machine Mirror and its self-record are coherent with the current set of governed artifacts and path-proofs: every mirror record has a matching index entry and path-proof, and the self-record for `artifacts/evidence_index.jsonl` reflects the current mirror body digest and size according to PF12 semantics.  
 **Evidence:** Successful combined runs of the canonical evidence-index and orientation checks (for example `update_evidence_index.py --check` and `orientation_demo.py --check`, titles-only) under closed rails, with no reported SHA/size mismatches or missing path-proofs.

#### **EVIDENCE\_PATHS\_VALIDATED\_OK**

**Owner PF:** HDE-Schemas & Artifacts  
 **Scope:** Evidence  
 **QA definition:** All governed artifacts have valid path-proofs with matching `sha256` and `size_bytes` and satisfy the monotone `mtime_utc` rules defined in PF12.  
 **Evidence:** Path-proof files and mirror-schema quick-check logs showing each governed artifact has exactly one consistent `path/sha256/size_bytes` triple and a valid `mtime_utc`.

#### **EVIDENCE\_LEDGER\_AGENT\_READABLE\_OK**

**Owner PF:** HDE-Governance / HDE-Build Checklist / HDE-Schemas & Artifacts  
 **Scope:** Evidence / post-commit  
 **QA definition:** Baseline HD Engine evidence for the epic or change set is captured in a text-based evidence ledger suitable for review by humans and Codex/ChatGPT-class agents: the Human Evidence Index, the Machine Mirror, any evidence bundle manifests, and key QA logs/step transcripts exist as plain-text files under governed paths and collectively expose the payloads and relationships required to reason about the associated QA Acceptance Tokens. Pure contract or token-only families are used only where the evidence consumer does not need to inspect payload contents; wherever payload inspection is required, at least one governed text artifact (for example a bundle manifest, QA log, or summary) must be present in the ledger for that token.  
 **Evidence:** Proof that, for the HD Engine surfaces and tokens in scope for the epic or plan:

* governed text artifacts exist under `docs/**`, `artifacts/**`, and/or `audit/**` (for example `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, bundle manifests, and per-step QA logs) and are wired into the Evidence Index and Machine Mirror according to HDE-Schemas & Artifacts and HDE-Build Checklist;

* any binary/compressed evidence bundles referenced by acceptance maps or manifests are paired with at least one governed text artifact that enumerates or summarizes their contents at the ledger level; and

* there are no QA Acceptance Tokens in scope whose satisfaction relies solely on non-textual or opaque artifacts when PF19 expects agent-readable payload inspection.

As with other tokens in this section, concrete schemas, bundle mechanics, and CI gates remain defined in HDE-Schemas & Artifacts and HDE-Build Checklist; PF19 defines the QA-facing condition that the HD Engine evidence ledger remains text-based and agent-readable at the PR level.

#### **CI\_CHECK\_MIRROR\_SCHEMA\_OK**

**Owner PF:** HDE-Schemas & Artifacts / HDE-Build Checklist  
 **Scope:** Evidence  
 **QA definition:** The machine mirror conforms to schema: pinned field order, one LF per record, canonical JSONL form, and unknown-key rejection, as enforced by PF12 mirror schema and PF09 CI wiring.  
 **Evidence:** CI mirror-schema verification artifacts for `artifacts/evidence_index.jsonl` showing all records pass schema validation and no unknown keys are present.

#### **CI\_CHECK\_FINAL\_LF\_OK**

**Owner PF:** HDE-Build Checklist  
 **Scope:** Pre-commit / Evidence  
 **QA definition:** All governed text artifacts end with exactly one trailing linefeed (one LF and no extras).  
 **Evidence:** CI logs or a dedicated LF-check harness that scans governed paths and confirms the one-LF rule for all relevant files.

#### **SANITY\_PIPELINE\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Governance  
 **Scope:** Pre-commit / CI (evidence skeleton)  
 **QA definition:** A closed-rails sanity pipeline entrypoint runs a deterministic sequence of checks over the evidence skeleton and determinism rails (serializer determinism tests, env pins checks, CLI serializer/emitter guards, and PF12 evidence index/mirror/path-proof checks) and completes successfully, producing a governed sanity log that reflects a fully coherent skeleton. SANITY\_PIPELINE\_OK is a composite CI token that assumes the underlying evidence tokens in this subsection are satisfied.  
 **Evidence:** Proof that:

* a dedicated sanity pipeline command (titles-only; for example `tools/evidence/run_sanity_pipeline.py`) is run under closed rails in CI;

* the pipeline log artifact (for example `artifacts/sanity/sanity.log`) and its path-proof exist, are canonical, and are indexed in `docs/evidence/INDEX.json` (+ `docs/evidence/INDEX.sha256`) and `artifacts/evidence_index.jsonl` with a `proof_anchor` pointing at the path-proof; and

* the pipeline log shows a PASS outcome (for example a `summary:PASS` line) for all configured steps, with any failure treated as a CI failure that blocks tokens such as `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and `CI_CHECK_MIRROR_SCHEMA_OK` until the skeleton is brought back into coherence.

  ### **SANITY\_PIPELINE\_LOGGED\_OK**

* **Meaning:** The epic’s current-state QA logs and manifest are present, and are sufficient for a reviewer to find and read evidence.

* **Evidence:**

  * `audit/qa/<epic-id>/qa_step_logs_manifest.json` exists and is valid JSON.

  * `audit/qa/<epic-id>/qa_step_logs_manifest.json` is keyed by `check_id` and points via `log_path` to each check’s canonical primary log under `audit/qa/<epic-id>/…`.

  * Each primary log is non-empty.

  * Each primary log begins with a Plan Templates step-log header as routed by §4.4.5 (including a complete `command` and `captured_env`), and has a clear status line in the header.

  #### **QA\_STEP\_LOGS\_CONSOLIDATED\_OK**

* **Meaning:** The epic’s QA evidence is consolidated to current-state canonical logs, with a manifest that provides deterministic pointers from checks → primary logs.

* **QA definition (strict):**

  * For each check required by the epic’s QA posture, there exists exactly one canonical primary log under `audit/qa/<epic-id>/…` (one per `check_id`), and it is referenced from the per-epic manifest.

  * The manifest is current-state only. Any per-run retention logs under `runs/<run_id>/…` are optional and non-canonical, and MUST NOT be referenced by `log_path`.

  * The step-log header schema and status vocabulary used in primary logs follow Plan Templates (routed by §4.4.5).

* **Evidence:**

  * The epic maintains `audit/qa/<epic-id>/qa_step_logs_manifest.json` as a per-epic index keyed by `check_id`, mapping each required check to its canonical primary log via `log_path`.

  * The manifest is deduplicated by `check_id` (at most one entry per `check_id`), and its `log_path` values all point within the epic QA root.

  * The acceptance map and token matrix bind required tokens to checks and reference the manifest \+ primary logs as the authoritative evidence surfaces.

**Live QA note (mechanics smoke tests).**  
 When the sanity pipeline (or its component scripts) are run in Live QA (for example from an open-rails Codespace during an epic’s D3/D4 steps), those invocations are treated as mechanics smoke tests, not as the canonical satisfaction of SANITY\_PIPELINE\_OK.

In this Live QA context, if the pipeline or a component script exits non-zero:

* QA MUST capture logs and exit codes mechanically under `audit/qa/<epic-id>/…` (for example `d3-cli-guards` or `d4-sanity` subtrees);

* QA MUST cross-check CI/closed-rails status for SANITY\_PIPELINE\_OK and related evidence tokens; and

* reviewers should treat the result as a QA finding (for example “env mismatch” or “harness not wired for open rails”), not automatically as an epic-blocking failure.

An epic’s acceptance roster in HDE Phased Epics may explicitly tie additional acceptance to a green Live QA run of the sanity pipeline. Only in that case should a non-zero Live QA result be treated as blocking acceptance for that epic; otherwise, the canonical satisfaction of SANITY\_PIPELINE\_OK continues to come from closed-rails CI evidence.

#### **CONFIG\_REGISTRY\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts  
 **Scope:** Pre-commit / CI (config \+ evidence)  
 **QA definition:** The canonical registry report (`registry.registry_report`) is generated under closed rails via the hardened registry/config generator, is canonical JSON, exhibits two-run identity, and is wired into the evidence skeleton and config acceptance map as the single source of truth for registry configuration.  
 **Evidence:** Proof that:

* the registry report artifact (for example `artifacts/registry/registry_report.json`) exists, is produced by the canonical generator under closed rails and serialized via the shared serializer, and is canonical JSON (sorted keys, compact separators, single trailing LF);

* the registry report passes its determinism and invariants tests (for example tests that check two-run identity, schema `registry_report.v1`, and expected coverage of registry entries); and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` contain a `registry.registry_report` entry with matching `sha256`, `size_bytes`, and `proof_anchor` to `artifacts/registry/registry_report.json.path_proof.txt`, and the config acceptance map (for example `audit/EPIC-018_config_acceptance_map.json`) references this artifact key and tokens in a canonical, validated way.

#### **CONFIG\_MAGIC10\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
 **Scope:** Pre-commit / CI (config \+ evidence)  
 **QA definition:** The Magic-10 and band-edges configs (`config.magic10`, `config.band_edges`) are generated under closed rails via the hardened registry/config generator, are canonical JSON, satisfy the Magic-10 and band invariants defined in the math/mechanics specs, and are wired into the evidence skeleton and config acceptance map as governed configuration artifacts.  
 **Evidence:** Proof that:

* the Magic-10 and band-edges artifacts (for example `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json`) exist, are produced by the canonical generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;

* config tests pass that validate domain invariants (for example Magic-10 order and caps cover the frozen category set with integer bounds and seed metadata, and band edges are sorted, span the clamp range, and match the Engine’s band definitions); and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` include `config.magic10`, `config.band_edges`, and the config acceptance map entry (for example `epic018.config.acceptance_map`), each with matching path-proofs, `sha256`, and `size_bytes`, and with references from the acceptance map to real artifact keys, known tokens (including CONFIG\_MAGIC10\_OK / CONFIG\_REGISTRY\_OK), and existing tests.

#### **CONFIG\_BUNDLES\_DETERMINISTIC\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
 **Scope:** Pre-commit / CI (config bundles \+ evidence)  
 **QA definition:** Typed frontend and backend config bundles (`config_bundle.fe`, `config_bundle.be`) are generated under closed rails from the governed config artifacts and registry loader, serialized via the canonical JSON emitter, satisfy two-run identity, and carry a sources block that links each bundle back to the precise digests and sizes of its upstream config artifacts and registry report.  
 **Evidence:** Proof that:

* the FE and BE bundle artifacts (for example `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`) exist, are produced by the canonical bundle generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;

* bundle tests pass that validate two-run identity, JSON structure, and domain invariants (for example tests under `tests/config/test_typed_bundles.py`, titles-only) and confirm that bundle contents (Magic-10, band edges, channels/centers/domains/alias policy for BE, slimmed bundle for FE) match the governed config artifacts and registry report; and

* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` include `config_bundle.fe` and `config_bundle.be` entries with matching `sha256`, `size_bytes`, and `proof_anchor` values pointing to their `.path_proof.txt` siblings, and that each bundle’s sources block lists only real governed artifacts with digests and sizes that match the evidence skeleton.

---

### **9.2.5 Transport / A7 tokens**

(Transport/A7 tokens, e.g. A7\_GET\_QUOTED\_ETAG\_OK, A7\_HEAD\_PARITY\_OK, A7\_304\_OMITS\_CT\_CL\_OK, A7\_VARY\_AUTH\_AE\_OK, A7\_ENCODING\_INVARIANCE\_OK, retain their existing QA definitions and evidence mapping: Reader Catalog JSON success posture, strong quoted ETag, HEAD/304 behavior, Vary headers, encoding invariance, and composite A7 proof artifacts. Text from prior PF19 remains, with numbering updated under §9.2.5.)

---

### **9.2.6 Aux & narrative tokens**

(Aux/narrative tokens, e.g. NARR\_200\_TEXT\_OK, NARR\_SUPPRESSED\_NO\_ETAG\_OK, COMPOSE\_IDS\_DETERMINISM\_OK, retain their existing QA definitions and evidence mapping: Aux text/suppression snapshots, ETag posture, and composition determinism. Text from prior PF19 remains, with numbering updated under §9.2.6.)

---

### **9.2.7 CLI/API & SDK tokens**

Existing CLI/API & SDK tokens such as CLI\_SHOWCOMPAT\_CANON\_OK, CLI\_READER\_EMITTER\_PARITY\_OK, CLI\_STDOUT\_LF\_OK, SDK\_READER\_PARITY\_OK, and SDK\_AUX\_PARITY\_OK retain their prior QA definitions and evidence mapping: canonical CLI JSON, emitter parity, stdout LF posture, and SDK parity artifacts, with normative semantics owned by HDE-Governance, HDE-Build Checklist, HDE-CLI-API-Vendor-Ref, and HDE-Schemas & Artifacts (titles-only).

#### **CLI\_STDOUT\_LF\_OK**

**Owner PF:** HDE-Build Checklist / HDE-CLI-API-Vendor-Ref / HDE-Governance  
 **Scope:** Pre-commit / CI (canonical CLI bytes)  
 **QA definition:** On CLI success paths, stdout is canonical bytes: the emitted success payload is serialized via the canonical emitter/serializer and ends with exactly one trailing linefeed. On success, stderr is empty.  
 **Evidence:** Combined proof that:

* CI enforces canonical-bytes posture for at least one representative success command (for example `hdctl showcompat`) via a CI-safe test that checks: stdout non-empty, stderr empty, and stdout ends with exactly one trailing LF; and

* governed stdout capture artifacts (and their checksums/args, where used) are stored under governed evidence roots and are bound in the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix) to concrete paths with no placeholders, with Index/Mirror/path-proofs kept in same-PR parity.

**EPIC022 D2 example (informative; not a semantic expansion).**  
 EPIC022 PR3 is the reference concretization pattern: deterministic showcompat stdout artifacts are captured under:

* `artifacts/cli/showcompat/stdout.json`

* `artifacts/cli/showcompat/stdout.json.sha256`

* `artifacts/cli/showcompat/args.json`

(with co-located `*.path_proof.txt`) and are bound to a canonical-bytes test (for example `tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical`) in the epic’s acceptance artifacts.

These are deterministic fixtures for stdout canonicalization. They MUST NOT be treated as release identity proofs; release identity remains governed by the `/internal/version` identity surface and its acceptance/evidence rules.

#### **CLI\_SHOWCOMPAT\_CANON\_OK (environment semantics)**

**Owner PF:** HDE-CLI-API-Vendor-Ref / HDE-Governance / HDE-Build Checklist  
 **Scope:** Pre-commit / CI / Live QA (compat behavior via CLI)  
 **QA definition:** CLI\_SHOWCOMPAT\_CANON\_OK asserts that `hdctl showcompat` behaves canonically for compat display in the environment declared as canonical for the epic:

* it produces governed compat JSON in the expected shape (categories, bands, scores, meta) for a fixed pair;

* it respects the environment’s source-selection rules (DB/packs vs vendor) as defined in PF05 and PF19 (§3.3, §5.6); and

* it exhibits two-run identity and, where applicable, AB↔BA parity for governed parts.

**Output posture (clarification; normative for QA interpretation).**

* `hdctl showcompat` **stdout** is the **compat payload** (admin/test surface). It **may include numeric-bearing fields** (for example numeric scores or weights) on success. Numeric-bearing success output is not treated as a covenant violation for this token.

* The **numeric-free** covenant applies to:

  * typed error envelopes, and

  * Reader v1 success envelopes (public success body).

* Reader v1 bytes are proven for CLI parity only via `--dump-reader` sidecars (and via the Reader surface), not by asserting that showcompat stdout “matches Reader bytes”.

**Exit-code posture (clarification; titles-only ownership).**

* CLI exit-code semantics are owned by the CLI contract (titles-only). PF19’s QA rule is: do not assume “typed failure exit code \= 2”.

* Repo-tested mapping used for QA documentation (docs-only alignment):

  * `0` on success.

  * `64` for usage, validation, and I/O failures raised via `CliError`.

  * For `showcompat`, vendor/engine failure paths return exit `1`.

  * Other non-zero exit codes remain command-specific. Do not generalize them across commands.

**Evidence:**

* Governed compat JSON artifacts from `hdctl showcompat` runs in the declared canonical environment for the epic, stored under `artifacts/cli/**`, with:

  * AB↔BA parity proofs where required;

  * two-run identity proofs for the canonical environment; and

  * Index/Mirror records and path-proofs in the same PR.

* Where Reader v1 parity is in scope for the epic, governed `--dump-reader` sidecar artifacts and their parity checks, bound in acceptance artifacts and indexed in the same PR.

* A short planning or acceptance note (for example in a `d0-*` planning artifact under `audit/qa/<epic-id>/d0-planning/`) stating which environment(s) are treated as canonical for CLI\_SHOWCOMPAT\_CANON\_OK in that epic.

#### **CLI\_ADMIN\_BUNDLE\_PARITY\_OK**

**Owner PF:** HDE-CLI-API-Vendor-Ref / HDE-Mechanics Guide  
 **Scope:** Post-commit / Live QA (CLI/API, admin surfaces)  
 **QA definition:** For a given match and admin credential, the CLI admin bundle command and the HTTP admin bundle route both call the canonical admin bundle builder and return byte-identical admin bundle JSON objects. No CLI-only or HTTP-only fields appear in the admin bundle payload, and any transport-level differences (for example HTTP headers) are outside the bundle JSON.  
 **Evidence:**

* A pair of governed admin bundle artifacts for at least one test match:

  * `artifacts/admin/cli_bundle_<pair>.json` (CLI), and

  * `artifacts/admin/http_bundle_<pair>.json` (HTTP),  
     produced under determinism env pins from the same QA console, both using a valid admin credential.

* A small parity artifact (for example `artifacts/admin/bundle_parity_<pair>.json` or an equivalent diff/proof) demonstrating structural and byte equality of the two JSON bundles after canonical re-serialization.

* Indexed entries for all three artifacts in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl`, each with a co-located path-proof and a Mirror record whose `proof_anchor` points at that proof.

#### **ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK**

**Owner PF:** HDE-Mechanics Guide / HDE-Schemas & Artifacts / HDE Narratives Guide  
 **Scope:** Post-commit / Live QA (admin bundle content)  
 **QA definition:** The admin bundle builder composes the full product payload for a single match into one JSON object. For each tested match, the admin bundle contains, at top level, at least `a_bodygraph`, `b_bodygraph`, `compat`, `narratives`, and `meta`, where:

* `a_bodygraph` and `b_bodygraph` are canonical BodyGraph JSON objects for each party (shape and mechanics per HDE-Mechanics Guide and HDE-Schemas & Artifacts);

* `compat` is the full Magic-10 compat result (category set, scores, bands, and compat meta) consistent with existing compat surfaces (titles-only);

* `narratives` is an array of exactly three Aux narrative compositions (two private, one shared) with composition IDs and pack SHA; and

* `meta` carries `engine_tag`, `release_id`, `invocation_tag` or equivalent, and bundle source/rails metadata.

No required component may be silently omitted or replaced with a placeholder.  
 **Evidence:**

* At least one governed admin bundle artifact (for example `artifacts/admin/cli_bundle_<pair>.json`) per test match, produced via the canonical admin bundle builder under determinism env pins.

* A QA harness or test that validates:

  * presence of the required top-level keys (`a_bodygraph`, `b_bodygraph`, `compat`, `narratives`, `meta`);

  * that `narratives` has length 3 and each element carries composition IDs and pack SHA; and

  * that the BodyGraph, compat, and narratives sections are consistent with their respective single-home surfaces (for example by cross-checking against separate BodyGraph/compat/narrative QA artifacts for the same match).

* Indexed entries and path-proofs for the admin bundle artifacts and any validation logs in the Human Index and Machine Mirror, in the same PR.

#### **ADMIN\_AUTH\_REQUIRED\_OK**

**Owner PF:** HDE-Governance  
 **Scope:** Post-commit / Live QA (auth & logging for admin surfaces)  
 **QA definition:** Neither the CLI admin bundle command nor the HTTP admin bundle route will return a full admin bundle JSON object unless the configured admin credential is presented. Unauthenticated and mis-authenticated attempts yield typed authentication/authorization errors only, and each successful admin bundle call is logged as an operations event with timestamp, caller identity (CLI vs GUI and user/account label), a high-level description of the inputs, and a correlation ID, in accordance with HDE-Governance logging and PII rules.  
 **Evidence:**

* Successful admin bundle runs (CLI and HTTP) for at least one test match with a valid admin credential, as described under CLI\_ADMIN\_BUNDLE\_PARITY\_OK and ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK.

* Negative auth runs:

  * CLI invocations of the admin bundle command without a credential and with an invalid credential, captured as governed artifacts (for example `artifacts/admin/auth_negative_cli_<pair>.json`) showing non-zero exit codes and typed auth errors, with no admin bundle JSON present.

  * HTTP invocations of the admin bundle route without a credential and with an invalid credential, captured as governed artifacts (for example `artifacts/admin/auth_negative_http_<pair>.json`) showing appropriate error status and typed error bodies, with no admin bundle JSON present.

* At least one redacted sample (or a path-proof-only record) demonstrating that successful admin bundle calls are logged with timestamp, caller identity, high-level input description, and correlation ID, and that logs are keys-only and free of raw birth data and secrets.

* Indexed entries and path-proofs for the negative auth artifacts and any log samples in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR as the admin bundle QA evidence.

---

### **9.2.8 App-layer QA tokens**

App-layer QA tokens are named here, but their normative definitions live in App QA governance/security docs (titles-only). PF19 does not define App-layer behavior; it only expects App-layer QA plans to map App tokens into this registry by name.

---

### **9.2.9 EPIC → token mapping (QA routing rule)**

An EPIC acceptance roster MUST list tokens by canonical name as defined in **HDE-Governance** (and mirrored in this PF19 token library). PF19 QA checks that token rosters and token/evidence matrices do not introduce aliases or midflight renames.

This is a routing and validation rule, not a permission: tokens still require evidence.

---

### **9.2.10 Forward plan**

This section was introduced to converge the Glow QA token ecosystem by:

* consolidating the QA operational mappings and evidence bindings into a single QA-facing list,

* binding each acceptance token to its governed evidence family,

* and extracting EPIC017 QA token operational guidance into this library where it was not already captured.

**HDE-Governance** remains the single source of truth for token names and normative semantics. PF19 §9.2 is the single QA-level home for the QA operational mapping (QA-facing meaning plus mechanical evidence expectations).

---

### **9.2.11 CLI guard tokens (D3 serializer/emitter guards)**

These tokens cover CLI guard tools (for example `serializer_grep_guard.py`, `emitter_symbol_proof.py`) that enforce closed determinism env rails and serializer/emitter wiring. Their canonical PASS condition is satisfied in CI/closed-rails runs, not in open-rails Live QA.

#### **CLI\_SERIALIZER\_GUARD\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Mechanics Guide  
 **Scope:** Pre-commit / CI (D3 guard stage)  
 **QA definition:** Under closed determinism rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`), the CLI serializer guard job (for example `serializer_grep_guard.py`, titles-only) exits successfully and reports no violations of the canonical serializer/emitter wiring or determinism env pins. A non-zero exit under closed rails indicates a real guard failure that must block D3 acceptance.  
 **Evidence:**

* CI job logs showing the guard script ran under determinism env pins and exited with status 0, with a PASS summary and no reported violations.

* Guard log artifacts (for example `artifacts/cli/guards/serializer_grep_guard.log`) stored under governed paths with co-located path-proofs.

* Index and Mirror entries for the guard artifacts in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl` in the same PR.

#### **SERIALIZER\_GREP\_GUARD\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Mechanics Guide  
 **Scope:** Pre-commit / CI (D3 guard stage)  
 **QA definition:** The serializer grep guard enforces that governed CLI/Engine paths only use the canonical serializer/emitter and do not introduce ad-hoc JSON encoding or unpinned env-dependent behavior. Under closed determinism rails, the guard must pass (exit 0\) with no forbidden patterns or missing serializer uses.  
 **Evidence:**

* Guard configuration and CI logs showing:

  * execution of the grep-based guard under determinism env pins, and

  * a PASS result for all monitored files and patterns.

* A governed guard summary artifact (for example `artifacts/cli/guards/serializer_grep_guard.summary.json` or similar, titles-only) indexed in the Human Index and Machine Mirror with matching path-proof.

#### **EMITTER\_SYMBOL\_PROOF\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Mechanics Guide  
 **Scope:** Pre-commit / CI (D3 guard stage)  
 **QA definition:** The emitter symbol proof guard confirms that CLI and HTTP emitters share a single canonical emitter implementation and that no extra emitter symbols or divergent code paths are used for governed surfaces. Under closed determinism rails, the emitter symbol proof must pass (exit 0\) and show that all expected emitter symbols are present and wired correctly, with no unexpected or missing emitters.  
 **Evidence:**

* CI job logs for the emitter symbol proof run under determinism env pins, showing exit status 0 and a PASS summary over the configured symbol set.

* A governed emitter symbol proof artifact (for example `artifacts/cli/guards/emitter_symbol_proof.txt`) indexed in `docs/evidence/INDEX.json` (+ `.sha256`) and `artifacts/evidence_index.jsonl`, with a co-located path-proof and a Mirror record whose `proof_anchor` points to that proof.

**Open-rails Live QA note (informational only).**  
 When these guard tools are run in open-rails Live QA environments (for example a PO or IA Codespace where `SAFE_MODE=0` and `ALLOW_NETWORK=1` by design), they are expected to enforce env pins and rails assumptions and fail closed (non-zero exit) when env pins do not match the closed determinism rails they require.

Such env-mismatch failures in open-rails Live QA are treated as informational env-enforcement checks, not as D3 acceptance failures:

* they do not satisfy the guard tokens above, and

* they must not be used to block PO Live QA sessions when the environment is intentionally open rails.

D3 guard tokens (CLI\_SERIALIZER\_GUARD\_OK, SERIALIZER\_GREP\_GUARD\_OK, EMITTER\_SYMBOL\_PROOF\_OK) are considered satisfied only by closed-rails CI runs with PASS outcomes; Live QA plans should reference CI/closed-rails evidence when asserting these tokens, not re-run D3 under open rails.

---

### **9.2.12 Manifests, acceptance maps, and token binding**

PF19 treats epic manifests and epic acceptance maps as complementary views of the same acceptance surface:

* The acceptance map (for example `docs/acceptance_map_epicXXX.json`, titles-only) is the design-time source that:

  * enumerates the epic’s D-goals/foundations (D1, D2, …),

  * lists the QA tokens relevant to each D-goal, and

  * names the governed evidence families (artifact keys, logs, indices) expected to satisfy those tokens.

* The epic manifest (for example `audit/EPICXXX_MANIFEST.json`, titles-only) is the run-time record that:

  * declares each token’s status for that epic, and

  * binds tokens to the concrete governed artifacts and tests that have actually been run.

**Close-pack manifest `key_outputs` bindings (normative; validator-bound).**  
 Epic close-pack manifests MUST represent their primary outputs via `key_outputs` as a dictionary of named bindings to exact path strings (not as a list or “membership” set). Validators are permitted to validate both the required binding keys and the exact bound path values.

Required binding keys (names-only; stable): `acceptance_map`, `token_matrix`, `acceptance_viability`, `step_logs_manifest`, `qa_doc_deltas`, `close_report`, `close_manifest`.

**Registry-level binding rule (normative).**  
 For each epic, the epic manifest MUST bind each QA token to artifacts that belong to the evidence families named for that token in the epic’s acceptance map (or in a PF-Canon section that the acceptance map points to by title). It is not acceptable to bind tokens to “generic” artifacts (for example a random sanity log or the Machine Mirror) when the acceptance map declares a different evidence family as the canonical home.

**Acceptance map ↔ manifest consistency (normative; automated).**  
 Acceptance maps and manifests MUST be kept consistent by automated tests, not by manual inspection:

* For every token listed in the acceptance map, there must be:

  * a corresponding manifest entry for that token; and

  * at least one artifact path in the manifest that belongs to the evidence family (or families) declared for that token in the acceptance map.

* For every token in the manifest, there must be:

  * a corresponding entry in the acceptance map (or in a clearly referenced PF-Canon section for that epic), and

  * evidence paths that resolve to real governed artifacts in those families (present in Index/Mirror with path-proofs and matching `sha256/size_bytes`).

Automated tests (for example `tests/audit/test_acceptance_map_epicXXX.py`, names-only) are expected to:

* validate the shape and contents of the acceptance map itself (epic id, foundations, token roster), and

* assert that the manifest’s token→artifact bindings match the evidence families and artifact paths declared in the acceptance map (or its canonical PF references).

**When new evidence families are introduced (normative).**  
 When an epic adds new evidence families (for example sampler or Engine Core evidence families defined in HDE-Schemas & Artifacts by title) and new tokens that depend on them, the corresponding PF12 and PF09/PF19 entries MUST be updated so that:

* the evidence families appear in the Evidence Catalog (PF12) with the correct artifact keys and paths;

* the acceptance map names those families and their tokens; and

* the manifest binds those tokens only to artifacts that belong to those families, with automated tests enforcing acceptance map ↔ manifest ↔ evidence skeleton consistency.

PF19 does not define manifest or acceptance map schemas; those live in HDE Phased Epics, HDE-Build Checklist, and HDE-Schemas & Artifacts (titles-only). PF19’s role is to make clear that:

* tokens are only Green when manifests bind them to the evidence families declared in the acceptance map, and automated tests prove that binding; and

* a manifest that binds tokens to unrelated artifacts, or that diverges from the acceptance map, is treated as a QA failure until corrected and covered by tests.

---

### **9.2.13 Live vendor & discovery tokens**

These tokens cover live vendor transport, open-rails env posture, and discovery baselines for epics that claim live vendor behavior or vendor-first PO Live QA.

#### **LIVE\_VENDOR\_TRANSPORT\_OK**

* **Meaning:** For a Live QA run, the set of vendor-facing transport behaviors required by the epic are exercised and produce evidence (API calls, logs, or side-effects) consistent with success.

* **Evidence:**

  * A declared list of vendor transport steps in the QA plan (each with a `check_id`).

  * For each such step, a canonical primary log exists under `audit/qa/<epic-id>/…` and is referenced by `qa_step_logs_manifest.json`.

  * Each such primary log includes the Plan Templates step-log header (routed by §4.4.5), and includes whatever evidence is required by the step (requests/responses, timestamps, outputs, etc).

  #### **OPEN\_RAILS\_ENV\_OK**

* **Meaning:** When open rails are required by the epic, the Live QA run’s evidence demonstrates that open rails were actually in effect for the acceptance-relevant checks.

* **Satisfied iff (strict):**

  * For each vendor-focused step that contributes to LIVE\_VENDOR\_TRANSPORT\_OK, the step’s primary log header `captured_env` shows:

    * SAFE\_MODE \= 0

    * ALLOW\_NETWORK \= 1

  * No step that claims open-rails acceptance may have contradictory rails values recorded in `captured_env`.

**Notes (non-normative):**

* A deterministic rails snapshot MUST be present in the step log header `captured_env`. If an additional environment snapshot file is produced and referenced, it is optional and non-gating; it MUST NOT be the sole source of rails evidence.

#### **DISCOVERY\_BASELINE\_OK**

**Owner PF:** HDE-Build Checklist / HDE-Schemas & Artifacts / HDE Phased Epics  
 **Scope:** Pre-run / planning (D0 discovery)  
 **QA definition:** DISCOVERY\_BASELINE\_OK asserts that a D0 discovery pass was performed and recorded before running Live QA steps for an epic, and that the discovery captured the repo and environment facts PF19 requires: governed config and bundle trees, guard/sanity runners, CLI help output, env rails intent, and `.gitignore` behavior for QA trees.  
 **Evidence:** A set of `d0-*` planning artifacts under `audit/qa/<epic-id>/d0-planning/` created before Live QA was finalized, including at least:

* `d0-config-tree.txt` and `d0-bundles-tree.txt` (or equivalent) showing `artifacts/config`, `artifacts/config_bundles`, `artifacts/registry` contents;

* `d0-guards-tree.txt` and `d0-sanity-runner-notes.txt` (or equivalent) showing guard scripts and sanity pipeline runners present in the repo;

* `d0-hdctl-help.txt`, `d0-showcompat-help.txt`, `d0-bg-resolve-help.txt` (or equivalent) capturing actual CLI help output so QA plans do not invent flags or subcommands; and

* `d0-env-rails.txt` plus `d0-gitignore-audit-qa.txt` showing the intended rails posture and confirming `audit/qa/<epic-id>/…` is not hidden by `.gitignore`.

Index/Mirror records and path-proofs for any of these `d0-*` artifacts that are treated as governed evidence (for example when they form part of the epic’s documented QA baseline and acceptance), and acceptance maps/manifests in HDE Phased Epics binding DISCOVERY\_BASELINE\_OK to these families.

#### **QA\_BOOTSTRAP\_OK**

* **Meaning:** The QA harness bootstraps successfully, producing the expected governed folder structure and at least one valid primary log for the bootstrap step.

* **Evidence:**

  * The harness creates the canonical epic QA root under `audit/qa/<epic-id>/…`.

  * The bootstrap step’s primary log exists under `audit/qa/<epic-id>/bootstrap/logs/bootstrap.primary.log` and begins with a valid Plan Templates step-log header as routed by §4.4.5 (including at minimum: `check_id`, `status`, `command`, `captured_env`).

  * The log body includes the bootstrap outputs (paths created, environment notes, and any relevant diagnostics).

#### **QA\_BOOTSTRAP\_TOOLING\_FAIL**

* **Meaning:** The harness attempted to bootstrap but failed due to tooling/environment issues (not behavior), and recorded an explicit blocked/tooling-failure status with evidence.

* **Evidence:**

  * The bootstrap step’s primary log exists and begins with a Plan Templates step-log header as routed by §4.4.5.

  * The bootstrap log records `status` as a tooling/prerequisite failure (e.g., `FAIL_TOOLING` or `TOOLING_BLOCKED`) and includes a clear reason in the header (if present) or at the top of the log body.

#### **QA\_HARNESS\_DISCIPLINE\_OK**

* **Meaning:** The plan/harness adheres to governed evidence discipline: canonical primary logs, manifest pointers, and token claims that are names-only and evidence-backed.

* **Evidence:**

  * The top-level epic QA output folder contains:

    * a consolidated step logs manifest (`audit/qa/<epic-id>/qa_step_logs_manifest.json`)

    * a canonical primary log per `check_id` (as referenced by the manifest)

    * an indexed evidence bundle via governed INDEX/Mirror (where applicable)

  * Each invoked step’s primary log begins with a Plan Templates step-log header as routed by §4.4.5 and includes:

    * a complete `command`

    * `captured_env` sufficient to prove rails posture for that step

    * a `status` value consistent with the evidence

  * If token fields are present in headers, they are names-only and use canonical spellings (`intended_tokens`, `claimed_tokens`, or legacy `tokens` as an alias for intended tokens only).

  ---

  ##### Evidence (names-only; current posture)

1. **Deterministic viability report (current-state; epic-level):**  
   A mechanically generated report exists at:  
* `audit/qa/<epic-id>/acceptance_map_viability.log`

The report MUST:

* name the acceptance map path examined (titles-only reference here),  
* report `status: PASS` when viable, and  
* when not viable, list missing/broken references and classify them as tooling-class failures that block Live QA until corrected.  
2. **Acceptance artifacts referenced (must exist and be consistent):**  
   The epic’s acceptance map and any acceptance-ledger artifacts referenced by the viability report (titles-only; owned by the epic acceptance posture).  
3. **Optional harness execution evidence (recommended when generated by harness; not required):**  
   If the viability report is produced as part of a harness run (not ad hoc manual inspection), also provide:  
* the primary step log for the viability check under the epic QA root (current-state), referenced by the manifest, and  
* an entry in `audit/qa/<epic-id>/qa_step_logs_manifest.json` for the viability check\_id pointing to that primary log.

Note: Under current QA posture, the manifest is a **current-state index keyed by check\_id**. Optional per-run retention paths under `audit/qa/<epic-id>/runs/<run_id>/…` may exist, but are not required for this token.

---

##### Relationships to other QA posture (names-only; no new scope)

This token supports “don’t start Live QA until the scaffolding is runnable.” It complements:

* baseline discovery context capture (D0 discovery / environment baseline), and  
* rails posture discipline (closed-rails by default; open-rails only where explicitly required),

by preventing “missing assets / non-runnable plan” failures before PO Live QA begins.

---

### **9.2.14 Token/evidence matrix and review rails**

**Intent.**  
 Make the relationship between QA tokens and evidence explicit and checkable at review time. Any epic that defines or consumes QA Acceptance Tokens MUST maintain a concrete, reviewable token/evidence matrix as part of its QA ledger.

**Scope.**  
 The token/evidence matrix requirement applies to:

* implementation plans,

* QA plans, and

* epic records and acceptance maps in HDE Phased Epics

whenever they introduce, rename, or consume QA Acceptance Tokens from this registry.

**Canonical artifact (HDE epics).**  
 For HD Engine epics that use acceptance maps and token-based acceptance rosters, the token/evidence matrix is not just a concept. It MUST exist as a governed, reviewable artifact under the epic QA tree:

* Canonical path pattern: `audit/qa/<epic-id>/token_evidence_matrix.md` (format may be Markdown table or another reviewable, machine-readable form).

The token/evidence matrix MUST NOT be embedded inside the Epic Plan document. Plans may reference the matrix by path, and may include a single placeholder pointer indicating it will be authored/updated during implementation and QA closeout.

**Scaffolding vs stage-gate strictness.**  
 Scaffolding PRs may seed a token/evidence matrix early (planned or token-incomplete rows, partial evidence titles) to establish the acceptance skeleton.

However:

* **PF19 MUST NOT be used to block plan approval** on the matrix being fully populated. Early matrices may be incomplete and serve only as scaffolding.

* The strict requirements below (complete rows, no implicit cells, and a normalized map suitable for approval) apply at **QA ledger completion / closeout readiness** and at **epic close**.

Within PF19, “QA ledger completion / closeout readiness” means the point at which the epic’s governed QA artifacts under `audit/qa/<epic-id>/…` are complete enough for final Live QA review and epic closeout.

No epic may claim token satisfaction while the matrix is still in a seeded, placeholder state.

**Token scope discipline (planning-time; normative).**  
 To prevent planning stall, any plan or QA ledger that references QA tokens MUST separate token mentions into:

* **In-scope acceptance tokens** — tokens that will be used as acceptance gates for the epic. These are the only tokens that get matrix rows and must be proven by QA ledger completion / closeout readiness.

* **Deferred tokens** — tokens that are desired but cannot be wired to concrete tests/CI/Live QA/evidence without inventing new semantics. Deferred tokens MUST NOT appear in the in-scope acceptance roster or matrix; they must be recorded as explicitly deferred in HDE Phased Epics.

* **Informative references** — non-gating metadata (workflow state, notes, or narrative pointers) that MUST NOT be treated as QA Acceptance Tokens and MUST NOT be placed into the token/evidence matrix.

**Token roster minimization (recommended).**  
 The in-scope acceptance roster SHOULD be small. For a typical epic, target ≤ 15 in-scope tokens. If an epic proposes a larger roster, the plan SHOULD include a brief justification and show why existing tokens cannot cover the required acceptance invariants.

#### **9.2.14.1 Matrix shape (per-token rows)**

For each QA acceptance token that is in scope for a plan or epic (one row per token), the matrix MUST capture at least:

* **PF19 registry name** — the canonical token spelling from this registry (no local aliases).

* **Epic-level acceptance map name** — the token name as it appears in the epic’s acceptance map (must be exactly the PF19 registry name).

* **Tests** — unit/integration tests that exercise the token’s behavior (for example specific test modules or cases).

* **CI jobs** — CI jobs that enforce the token’s behavior under closed rails, where applicable (names only; definitions live in HDE-Build Checklist).

* **Live QA steps (if applicable)** — Live QA steps that demonstrate the token’s behavior (for example D1/D3 steps in the epic QA plan), with references to their primary step logs under `audit/qa/<epic-id>/…`.

* **Evidence artifacts** — governed artifact paths under governed roots (for example `docs/**`, `artifacts/**`, `audit/**`) generated by those tests and steps.

* **Index/Mirror binding** — the Evidence Index and Machine Mirror records (by artifact key or path) that register those artifacts, including `proof_anchor` references to path-proofs.

**Proof transcripts are not primary evidence (normative).**  
 For most tokens, the matrix MUST bind the token to the primary artifacts and the tests/jobs/steps that generate and validate them. The corresponding `*.path_proof.txt` files are normally entailed via the Machine Mirror record’s `proof_anchor` and validated by the evidence tooling. Do not bind a token solely to a `*.path_proof.txt` transcript as the “evidence artifact,” unless that token’s own canonical evidence surface explicitly requires naming a proof transcript path (for example a single canonical surface token that is defined as path-sensitive).

The matrix may be rendered as a table, JSON, or other machine-readable structure, but it must be complete for all in-scope acceptance tokens by QA ledger completion / closeout readiness and at epic close.

#### **9.2.14.2 Ledger gate (no “e.g.” / “TBD” / implicit cells)**

At QA ledger completion / closeout readiness and at epic close, for tokens that remain in scope:

* No cell in the token/evidence matrix may be left blank, marked as “e.g.”, “TBD”, or described only in narrative prose. If a test, CI job, Live QA step, or evidence artifact does not yet exist, that gap must be called out explicitly and treated as a blocking issue, not as an implicit future task.   
* **Concretized-token hygiene (normative; EPIC022 anti-drift pattern).**  
   Once a token’s evidence bindings have been concretized (real artifact paths exist on disk and are being used for acceptance), acceptance artifacts MUST be single-authoritative and pattern-free:  
  * the token MUST appear at most once in each acceptance artifact (token/evidence matrix, acceptance map, manifest token roster); duplicate rows/entries are treated as ambiguous evidence and block closeout readiness;  
  * evidence lists MUST NOT contain placeholders or patterns (for example `{scenario}`, “TBD”, “pending”, or template strings) for any token whose concrete evidence is present; and  
  * CI-safe scaffold tests MAY enforce: (a) exactly one token row/entry exists per token, and (b) every listed evidence path resolves to a real file (existence \+ minimal parse checks) to prevent drift regressions.  
* **Acceptance-alignment validator (CI-safe; recommended).** CI-safe validator tests SHOULD enforce the following invariants to prevent drift regressions:  
  * **Map ↔ matrix ↔ manifest lockstep:** token rosters match exactly across acceptance map, token/evidence matrix, and manifest token roster (no extras/missing).  
  * **Token registry membership:** every token referenced by acceptance artifacts exists in the PF19 token registry.  
  * **Duplicate-free rosters:** acceptance map, matrix, and manifests must not contain duplicate token entries.  
  * **Implemented/covered evidence binding:** for tokens marked implemented/covered, every claimed governed evidence path MUST exist in both the Human Evidence Index (`docs/evidence/INDEX.json`) and the Machine Mirror (`artifacts/evidence_index.jsonl`), and the Mirror record MUST include a `proof_anchor` pointing to the corresponding `*.path_proof.txt`.  
  * **Proof transcripts not primary evidence:** enforce “Proof transcripts are not primary evidence (normative)” (see §9.2.14.1).  
  * **Determinism posture:** validator tests MUST be CI-safe (no network) and enforce determinism env pins/rails as required elsewhere in PF19 (SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ).  
     Planned tokens may skip the implemented/covered evidence-binding assertions, but they must still participate in roster/registry/duplicate checks. When a token flips to implemented/covered, the evidence-binding checks become mandatory.  
* A QA ledger / closeout record that contains any in-scope token with:

  * `e.g.` or `TBD` token names,

  * missing or implicit tests/CI/Live QA references, or

  * missing evidence/index/mirror bindings,  
     MUST NOT be marked complete (ASK OK) for that token. Completion can proceed only once the matrix row is fully populated and consistent with the acceptance map and manifest (§9.2.12).

Any attempt to treat an incomplete matrix row as “good enough for now” is a QA process violation at closeout readiness and close. Reviewers must either:

* require the gaps to be filled and re-review the QA ledger, or

* record a deliberate scope deferral in HDE Phased Epics and remove the token from the in-scope roster for that epic.

#### **9.2.14.3 Consistency with acceptance maps and manifests**

The token/evidence matrix is a per-plan view of the same relationships enforced globally by §9.2.12:

* Every PF19 registry name that appears in the matrix MUST also appear in the epic’s acceptance map token roster.

* Every evidence artifact listed in the matrix MUST belong to one of the evidence families named for that token in the acceptance map (or in a PF-Canon section the map points to by title), and must be present in the Human Index and Machine Mirror with a valid path-proof.

* Automated tests are expected to validate that matrix rows, acceptance maps, manifests, and the evidence skeleton remain in sync. Inconsistencies between these views — including missing rows, extra tokens, or mismatched artifact families — are QA failures, not documentation nits.

**Canonical evidence-path validation (preflight; pass/fail).**  
 Every token-to-artifact binding that appears in an epic’s acceptance artifacts (required evidence list, token/evidence matrix, and any manifest bindings) MUST be validated against the canonical Evidence Catalog defined in **HDE-Schemas & Artifacts** (titles-only) before approval or merge.

* If the Evidence Catalog defines a fixed canonical path for a token’s evidence surface, the acceptance artifacts MUST bind to that exact path.

* Any binding to a non-canonical path is a mechanical blocker and MUST be corrected before approval. If a non-canonical path is truly required, it MUST be routed as an explicit ADR and drained into the Evidence Catalog (by title) before acceptance can proceed.

**Plan ↔ matrix cross-check (local bundle deliverables).**  
 When a deliverable is described as a “local bundle” of governed artifacts under a directory root (for example `artifacts/ops/internal_version/**`), the epic’s required evidence list MUST explicitly name:

* the complete required local bundle paths (titles-only, full paths), and

* any shared/global governed evidence required outside the local bundle root (for example determinism env pins evidence),

so reviewers do not assume those dependencies are “implicit”.

The token/evidence matrix MUST mirror the same required-evidence path set. Missing shared/global dependencies or mismatched paths block QA ledger completion / closeout readiness and block epic close.

**Minimum agreement set when claiming a token (names-only).**  
 When an in-scope token is claimed as satisfied, the following MUST all agree on the same canonical artifact key/path:

* the epic’s required evidence list (in the epic’s acceptance artifacts),

* the token/evidence matrix row for the token,

* the Human Evidence Index entry for the bound artifact,

* the Machine Mirror record for the same artifact, and

* the corresponding path-proof referenced by the Mirror record (`proof_anchor`).

**Deterministic parity scenarios (normative).**  
 Any new or expanded error parity scenario used for acceptance (for example DB-unavailable or a closed-rails vendor attempt) MUST be reproducible under determinism env pins and closed rails, without reliance on external network or a live database.

Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts. If that is not feasible, use a deterministic stub only to the extent required to produce the canonical envelope and parity artifacts (no live I/O).

Acceptance proof MUST include stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and those artifacts MUST be indexable under governed evidence surfaces. Any added scenario MUST have a stable scenario identifier so stored artifacts do not churn.

**PF09 subtask closeout uses evidence-binding first (normative).**  
 When closing a PF09 subtask described as “captured elsewhere” or “piecemeal,” the default closure method is to bind existing governed evidence (tests and artifacts) into the epic’s acceptance artifacts (acceptance map and token/evidence matrix). Creating a new evidence family for closeout is allowed only if the epic includes an explicit gap statement (“what is missing from existing evidence”) and the new evidence aligns to governed artifact conventions (titles-only; owned elsewhere).

Closure is not complete unless the acceptance artifacts explicitly map the PF09 subtask to concrete evidence. Implicit “it exists somewhere else” is non-conforming.

**/internal/version coupling proof uses a single governed log artifact (normative).**  
 When an epic claims `/internal/version` coupling proof and/or two-run identity closure, the governed proof artifact is:

* `artifacts/ops/internal_version/two_run_identity.log`

This log MUST include, at minimum:

* an explicit two-run identity result (byte-identical or not), and the compared byte identifiers, and

* an explicit coupling verification result showing the six `/internal/version` fields match their governing identity sources (titles-only pointers), including release\_id coupling.

The log MUST include rails posture and determinism pins references (names-only pointers). The determinism pins themselves remain proven only by their canonical governed log surface.

No new acceptance tokens are introduced for “coupling proof.” The coupling proof is evidence-bound under the existing identity and internal-version token set.

This section upgrades the token/evidence matrix from a “good practice” to a required closeout gate: no epic that touches QA tokens is ready to be treated as QA ledger complete or ready for closeout until its token/evidence matrix is complete, consistent with the registry, and aligned with acceptance maps, manifests, and the evidence skeleton.

#### **9.2.14.4 Automated alignment guard (recommended)**

For epics that maintain both:

* a token/evidence matrix under `audit/qa/<epic-id>/token_evidence_matrix.md`, and

* an acceptance map (titles-only; see HDE Phased Epics),

teams SHOULD add an automated alignment check (meta-test or CI job) that:

* asserts the token sets in the matrix and acceptance map are identical,

* normalizes and compares token statuses, and

* verifies that any token marked implemented has non-empty evidence pointers in both artifacts.

This guard is intended to prevent “approval drift” where matrices and acceptance maps silently diverge between PRs.

---

### **9.2.15 Review rails for token blockers, scope waivers, and canonical names**

#### **9.2.15.1 Token blockers (must be treated as BLOCKING)**

Token issues are **acceptance-blocking** when a token is being claimed (for example: in an acceptance map, token/evidence matrix, or closeout request). The following must be treated as blocking for an acceptance claim:

* A token named in acceptance artifacts that does not exist in **HDE-Governance** (unregistered) or that does not match the canonical spelling. (Record `CAVEAT: UNREGISTERED_TOKEN` or `CAVEAT: UNREGISTERED_ACCEPTANCE_TOKEN` while it is unresolved; do not claim the token.)

* A token claim that is not backed by the governed evidence family for that token (wrong artifact family, missing required outputs, or evidence not produced mechanically).

* A token/evidence matrix row that binds a token to a non-canonical artifact path without a governed alias rule.

* Any token proof that relies on manual editing, hand-written PASS/FAIL prose, or other non-mechanical evidence.

Note: During **Live QA plan approval**, token issues are handled as caveats unless they make a step impossible to execute or impossible to verify (see **Plan validity lint** under **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**).

#### **9.2.15.2 Token scope waivers (allowed; must be explicit)**

Token scope waivers MAY be used when an epic intentionally does not validate a token that is listed in a broad acceptance roster. Waivers MUST:

* be explicitly listed (by canonical token name),

* state a clear reason, and

* avoid redefining the token or substituting an alias token name.

#### **9.2.15.3 Canonical name re-check**

Before raising a token name mismatch, the reviewer MUST retrieve (not excerpt) the full token roster in scope and the governing token definition in **HDE-Governance**.

If the reviewer cannot retrieve and cite the full governing source passage(s) necessary to substantiate a mismatch claim, record `CAVEAT: ORIENTATION_DRIFT` instead of asserting a mismatch.

If the roster includes a token name that appears unregistered or misspelled, record `CAVEAT: TOKEN_MISMATCH` or `CAVEAT: UNREGISTERED_TOKEN` and proceed with runnable behavior testing. Do not claim acceptance for an unregistered token until governance registration is complete.

#### **9.2.15.4 Token roster preflight (required; no midflight token invention)**

Token roster preflight is required for correctness, but it is **NOT** a Live QA plan-approval gate.

* Live QA plans MAY omit token lists entirely, and they MUST NOT be forced to enumerate full token rosters or per-step token claims as a condition of plan approval.

* If a plan chooses to reference tokens, it MAY list a partial set. Any token names used MUST use canonical spellings (no aliases).

* A missing/mismatched/unregistered token discovered during planning is a caveat (`CAVEAT: TOKEN_MISMATCH` / `CAVEAT: UNREGISTERED_TOKEN`). Proceed if the steps are runnable and verifiable; record the mismatch for drainage (see the Step-0 doc delta capture step required by **14.6 Ownership and maintenance**).

Midflight token invention is still forbidden:

* Do not introduce a brand-new token name inside a running plan, run log, or closeout request.

* If a new acceptance token is truly required, route it through governance registration first (see the governance-first workflow in **9.2.2 Token metadata model (normative)**), then update the plan/matrix using the registered canonical name.

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
* **Governed roots only.** All indexed artifacts MUST live under a governed evidence root declared in the Evidence Catalog (HDE Schemas & Artifacts, titles-only). Transient/generator paths are forbidden as sources for indexed evidence.  
* normalize header names to lower-case before persisting governed snapshots  
* For each new or changed governed artifact under a governed evidence root:  
  * create or update a co-located `path_proof.txt` file, and  
  * ensure there is exactly one Mirror record whose `proof_anchor` points at that `path_proof.txt`.  
* Treat “artifact present but no path\_proof” or “path\_proof present but no Mirror record” as **QA failures**, not as minor hygiene issues.  
* For lifecycle and OPS‑managed artifacts (for example backup/restore probes), confirm that the associated evidence changes (artifact \+ path\_proof \+ Mirror) land in the **same PR** as the code or configuration change they support.

---

## 10.3 Validated-tuple QA harness (Aux & CLI parity)

**Anchor.** “Validated-tuple QA harness for Aux & CLI parity”  
 **Purpose.** A small, repeatable harness that:

* takes fixed test tuples as inputs

* sets env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`)

* **harness must invoke the shared emitter path used by HTTP and CLI; no alternate serializers.**   
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

* run the mirror quick-check (§10.5). Failure to index or mirror any A7 artifact means the A7 gate is **not satisfied**, and no A7 tokens may be claimed for that PR.

---

## **10.5 Mirror schema quick-check**

### **Remediation Implementation Guides (DEV/OPS-only; verification embedded)**

This section defines the required posture and schema for Remediation Implementation Guides. It does not change Live QA plan formats.

**Scope (normative).** A Remediation Implementation Guide is an execution guide for implementing and verifying remediation work. It is DEV/OPS-only and must not introduce additional step lanes.

**Permitted step types (only).**

* A Remediation Implementation Guide MUST use only two step types: `DEV` and `OPS`.  
   No other step types are permitted (no QA, DOC, REVIEW, or “verification-only” steps).

**Verification embedding requirement (normative).**

* All verification MUST be embedded inside the owning `DEV` or `OPS` step.  
   Verification must reference the exact governed evidence outputs produced by that step (paths and filenames specified in the step).

**OPS posture linkage (normative).**

* OPS steps MUST follow the Ops execution posture: PO-only execution, IA-guided, secret-free evidence, lowercase audit paths (see the Ops tasks rule under §11.1).

**Strict lane separation (normative).**

* A step labeled `DEV` MUST contain only DEV actions.

* A step labeled `OPS` MUST contain only OPS actions.

* If a step depends on outputs produced by a prior step in the other lane, the dependent step MUST declare its dependency explicitly using the dependency-line rule below.

### **Canonical schema requirements (template rules)**

**Step Overview (mandatory).** The guide MUST include a Step Overview table that lists, at minimum:

* Step ID

* Step name

* Step type (`DEV` or `OPS`)

* Owner/role

* Depends on

* Cross-lane dependency (Yes/No)

* Outputs (governed artifact paths)

**Step Details schema (mandatory).** Each step MUST include a Step Details block with, at minimum:

* Step ID

* Step name

* Step type (`DEV` or `OPS`)

* Step intent (short; what the step accomplishes)

* Constraints / rails (what must remain true while executing)

* Actions (what-not-how; include exact commands only when required)

* Verification (embedded; mechanical checks and PASS condition)

* Evidence outputs (exact paths and filenames; secret-free)

* In-flight determinations (optional; only if new ADRs or decisions are required)

**Dependency-line rule (locked; required modification).**  
 If a step depends on outputs produced by a prior step in the other lane, the dependent step MUST include exactly one cross-lane dependency line in this exact form:

Inputs needed from Step S\<N\> during implementation: \<exact items\>

Rules for this line:

* `S<N>` MUST be the actual producing step ID (no placeholders such as `Sx`).

* The line MUST appear exactly once in the dependent step.

* The line MUST NOT be duplicated, nested, or prefixed by a placeholder field label.

* The `<exact items>` MUST name concrete artifacts or values produced by the referenced step (paths preferred), not vague phrases.

**PF docs consulted and ADRs.** A remediation guide SHOULD include:

* a short “PF Docs Consulted” list (titles-only), and

* an “ADRs Requiring Approval” list for any canon decisions or external task creation required by the remediation.

**ADR discipline (normative; no restate / no drift).**  
 When a remediation guide includes an “ADRs Requiring Approval” list:

* Each ADR MUST be a canon-resolution instruction and MUST include explicit drain targets (which PF canon doc(s) will be updated).

* ADRs MUST NOT be created to restate topics already canonized in **PF10 — HDE Build Notes** (or other PF canon).

* ADRs MUST NOT cite **PF20 — HDE Phased Epics** to define/justify evidence surfaces, acceptance tokens, QA log/schema requirements, plan template structure, or canon superseding rules.

* **PF20 — HDE Phased Epics** is a tracking ledger (scope/status/history) only; it is not an implementation/remediation planning authority.

**Anchor.** “Machine mirror schema quick-check”  
 **Purpose.** A small tool or CI step that:

* loads `artifacts/evidence_index.jsonl`

* verifies:

  * sorted keys and pinned field order

  * exactly one LF per record

  * canonical JSONL form

  * rejection of unknown keys

**Notes.**  
 PF19 names the required checks. The mirror record schema and field-order rules are defined in **HDE-Schemas & Artifacts** (titles-only). The repo provides the quick-check implementation.

**Invocation rule (normative; operator-facing).**  
 In the engine repo, `ci/checks/check_mirror_schema.sh` is an executable Python entrypoint (Python shebang). CI invokes it directly; use the same shape for operator runs. For example:

* `ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

If direct execution is not guaranteed in the environment (missing executable bit / shebang handling), the Python invocation is acceptable:

* `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

It MUST NOT be invoked via `bash ci/checks/check_mirror_schema.sh`. If acceptance artifacts or QA plans include the bash invocation, treat that as operator-doc drift and correct it before running QA.

### **Remediation Task Plans (DEV PRs \+ OPS tasks only)**

This section defines the canonical structure and approval rails for remediation task plans. It applies to remediation work that includes DEV PRs and/or OPS tasks.

**Task model (normative; only two types).**

A remediation task plan MUST contain only two task types:

* **DEV tasks** are PRs only and MUST be enumerated as `PR-01`, `PR-02`, … (no mixed-task steps).

* **OPS tasks** are PO-run procedures only and MUST be enumerated as `OPS-01`, `OPS-02`, … (no mixed-task steps).

Discovery is allowed but MUST be explicit per task as `DISCOVERY` vs `CHANGE`.

**Cross-lane dependencies (normative; exact line).**  
 Cross-lane dependencies MUST be explicitly declared in the dependent task using the exact line:

Inputs needed from Task \<ID\> during implementation: \<exact items\>

Rules:

* `<ID>` MUST be the actual producing task ID (no placeholders such as `Sx`, `TBD`, “to be determined”).

* Placeholders in this dependency line are a mechanical blocker.

* `<exact items>` MUST name concrete artifacts/values produced by the referenced task (paths preferred).

**Approval gate scope (tight; normative).**  
 For remediation task plans (DEV PRs \+ OPS tasks), approval MUST focus on:

* correct task model (OPS vs DEV; DISCOVERY vs CHANGE; no mixed tasks),

* correct sequencing and explicit cross-lane dependencies,

* concrete deliverables (lowercase paths \+ filenames), and

* concrete verification success criteria (what “done” means).

Detailed command lines and step-by-step failure handling are not required as plan-approval conditions. They MAY be developed in flight during execution, using repo reality and operator judgment, as long as the evidence posture remains intact.

**Evidence posture remains non-negotiable (normative).**  
 Even when commands/failure handling are developed in flight, OPS execution MUST still capture:

* the exact commands actually run (verbatim),

* stdout/stderr \+ exit code (or equivalent output),

* the produced artifacts at the declared output paths, and

* deviation notes needed to explain why a different command/flag was used.

This evidence MUST land under `audit/qa/...` (lowercase) with explicit filenames sufficient for later audit.

In-flight command flexibility does not permit:

* changing governed artifact locations or filenames,

* introducing new governed files without an explicit statement of indexing/mirror intent, or

* indexing remediation-only diagnostics into governed indices/mirror.

**Mechanical blockers (auto-reject if present anywhere in the plan).**

* Any `PR-xx` task missing a paste-ready Codex Prompt embedded inside that task.

* Any task that mixes DEV \+ OPS work in a single task.

* Any deliverable specified only as a directory (must be a concrete lowercase file path including filename, e.g., `audit/qa/<epic-id>/<task-id>/<filename>`).

* Any cross-lane dependency missing the exact dependency line above, or using non-concrete “exact items.”

* Any task that proposes a new file under governed surfaces without stating whether it is intended to appear in the indices/mirror (absence of that statement is a blocker).

**Remediation-only artifacts vs governed surfaces (normative).**  
 Remediation-only diagnostics/manifests MUST NOT be introduced under governed artifact surfaces unless explicitly framed as an ADR-worthy governance change. Default posture: remediation-only artifacts live under remediation audit paths (for example `audit/qa/.../remediation/...`) and do not enter governed evidence indices/mirror.

**EPIC022 remediation patterns (default posture; names-only).**  
 The following patterns are the default posture for remediation task plans unless a plan explicitly states why a different pattern is required.

**PR-01 (DISCOVERY-only) discovery report posture (copy/paste safety).**

* PR-01 deliverable is exactly one discovery report file under `audit/qa/<epic-id>/remediation/...`, with no code/test/script changes.

* If the report includes Evidence Index/Mirror update commands, the default copy/paste command MUST NOT include an epic-id flag from another epic.

  * If the evidence tooling supports an `--epic-id` flag, treat it as **optional** and **non-default** in the report. If included at all, it must match the current epic and must be clearly labeled as optional.

* If a placement decision is not yet enforced by tests (example: request-chain manifest placement), the discovery report MUST mark the location as **TBD** and constrain options to the smallest set that matches observed governed placement patterns and enforcing tests. Do not present an unverified “fits at \<path\>” as settled.

**OPS-01 host reachability probe (read-only discovery; evidence bundle).**

When an OPS task selects a single prod host/base\_url for follow-on runtime probes, the OPS evidence bundle SHOULD include:

* a host reachability matrix file and explicit selection outputs (for example `host_matrix.md`, `selected_base_url.txt`, `selected_host_label.txt`),

* a raw headers capture file that includes the HTTP status line and at least one header line (for example `headers_raw_SELECTED.txt`),

* a stderr capture for the HTTP tool (for example `curl_stderr_SELECTED.txt`), and

* a structured headers sample in JSON with lower-case header keys and required keys `status_line` and `headers` (for example `headers_internal_version_sample.json`).

**Evidence quality note (portability).**

* Artifacts MUST be file bytes written by commands. Avoid copy/paste noise.

* If a table or excerpt contains terminal control sequences, treat it as a portability risk. Regenerate the artifact so the on-disk file is plain text.

**OPS-02 runtime bundle capture (open rails; portable snapshot).**

When an OPS task runs a runtime probe and copies a governed artifact family into an audit bundle for portability, the bundle SHOULD include:

* a command transcript split into files (for example `run_command.txt`, `run_stdout.txt`, `run_exit_status.txt`),

* an expected-vs-actual artifact inventory (for example `expected_artifact_files.txt` and `file_list_actual.txt`),

* a remediation-only snapshot manifest that enumerates sha256 and size for each copied file (for example `remediation_only/manifest_snapshot.json` and `remediation_only/manifest_snapshot.json.sha256`), and

* any newly introduced governed artifacts plus their sibling path proofs when copied (for example `request_chain_manifest.json` and `request_chain_manifest.json.path_proof.txt` when present in the governed family).

If a plan claims “checksum validated” for a produced `.sha256` file, the OPS evidence bundle SHOULD include the verification command output as evidence (do not rely on a prose assertion).

**PR-03 Index/Mirror regeneration (integration summary \+ exclusion check).**

Any PR that regenerates governed Index/Mirror/proofs SHOULD include an integration summary artifact under the epic remediation QA tree that records:

* the exact regeneration and validation commands executed under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0` plus env pins), and

* an explicit inclusion check for any new required evidence family entries (for example request-chain manifest mirrored with a valid `proof_anchor`), and

* an explicit exclusion check that remediation-only bundle paths are not indexed (for example no matches for a remediation-only subtree across `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`).

Broad path-proof refresh touching other indexed artifacts is non-blocking when it is the natural outcome of running the canonical full regeneration.

### **Exact filenames rule for Evidence Index \+ path proofs (plans touching governed indices)**

Any remediation plan that includes tasks touching governed evidence indices/mirrors MUST explicitly name the exact index \+ path-proof filenames as task outputs and as embedded verification checks (inside OPS/DEV tasks; not as standalone verification-only tasks).

Canonical placement is co-located “sibling” path proofs: `<file>.path_proof.txt` MUST sit next to `<file>` and MUST NOT be placed in an alternate directory (for example `docs/evidence/path_proofs/...` is non-canon).

Canonical quick reference (must be used verbatim in plans where applicable):

Evidence index (human-readable):

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `docs/evidence/INDEX.json.path_proof.txt`

* `docs/evidence/INDEX.sha256.path_proof.txt`

Evidence index mirror (machine-readable):

* `artifacts/evidence_index.jsonl`

* `artifacts/evidence_index.jsonl.path_proof.txt`

**Evidence Index Refresh Flow reference lock (normative).**  
 Plans/remediations that invoke or reference the Evidence Index Refresh Flow MUST cite **PF12 — HDE-Schemas & Artifacts** — “Refresh sequence (normative)” (titles-only) and MUST NOT cite non-verifiable PF12 section numbers for this topic.

The plan MUST explicitly bind the refresh outputs (do not hand-wave): `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and all governed `*.path_proof.txt` transcripts regenerated by the refresh tooling run (including Index/Mirror path proofs when applicable).

Canonical invocations (plans MUST call out explicitly):

* Regeneration: `python tools/evidence/update_evidence_index.py` (write mode).

* Validation-only: `python tools/evidence/update_evidence_index.py --check`.

* Mirror schema check (when applicable): `python ci/checks/check_mirror_schema.sh` (NOT `bash ...`).

Plans MUST treat path-proof artifacts as first-class deliverables: if a task edits an index/mirror file, the sibling `.path_proof.txt` update is part of the same task’s outputs \+ verification.

### **Portability vs provenance for non-PF evidence (normative)**

Remediation guides and task plans may include a short “Evidence inventory reviewed (non-PF)” list for provenance, but MUST NOT require the reader/executor to open external files to perform the work.

If a remediation plan depends on any non-PF fact (command outputs, headers, error strings, file paths observed, specific status lines), the plan MUST embed that fact directly in the document as a short quote or precise paraphrase inside an “Observed Evidence Snapshot” section.

If an Artifact Map (or equivalent) is included, it MUST explicitly label non-PF inputs as:

provenance only; not required to execute

Otherwise it is treated as an execution dependency and becomes a portability blocker.

When a non-PF observation drives a branching decision, the plan MUST include:

* the observation to look for (exact string/status/shape),

* the decision rule, and

* the output artifact path where the observation is captured (lowercase file path including filename).

  ---

## 11\. Roles & RACI (QA)

### 11.1 QA roles (titles-only pointer to PF06)

#### Ops tasks (PO-only execution; IA-guided; evidence required)

**Definition (normative).** An Ops task is any work item that requires privileged access or external-system authority (for example: production environment controls, account-level configuration, credentials/secrets, production migrations, or other privileged state changes). A DevOps task is treated as an Ops task whenever it requires any of the above.

**Execution authority (normative).** Ops tasks MUST be executed by the PO (human operator) only. Automation agents and Codex-style tooling MUST NOT execute Ops tasks, MUST NOT claim completion, and MUST NOT simulate external state changes.

**IA facilitation posture (normative).** Ops tasks MAY be part of an epic, but they must be described and reviewed as PO-only execution with IA guidance. The IA’s job is to specify the task in a what-not-how manner and then work directly with the PO during execution.

**Ops task spec format (required fields).** Every Ops task record MUST include:

* Task ID (stable; referenced consistently)

* Owner: PO

* Facilitator: IA

* Constraints / safety rails (what must remain true while executing)

* Success criteria (observable outcomes, not assumptions)

* Evidence to capture (what artifacts prove completion and where they are stored)

* Rollback intent (what “revert” means at a high level)

* Secret handling note (explicitly: no plaintext secrets in docs or evidence)

**Evidence posture (required).** Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase audit path such as:

* `audit/ops/<epic-id>/...` for Ops execution evidence, or

* `audit/qa/<epic-id>/...` when the evidence is part of QA execution.

Evidence MUST NOT include secrets. If a setting/value is sensitive, capture it as presence-only, redacted, or hashed while still being sufficient for verification.

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

## **12.2 Supersession rule (PF10 addenda)**

* PF10 Build Notes are a living input stream. Do not reference PF10 by version strings.

* When referencing PF10 guidance in PF19 or in a Live QA plan, cite PF10 by **addendum number \+ addendum title** (stable unit), not by brittle subsection/paragraph anchors.

* When multiple PF10 addenda address the same topic, the later (higher-numbered) addendum supersedes the earlier.

   If an addendum is intended to supersede earlier guidance, it should explicitly name what it supersedes (to reduce ambiguity during drainage and review).

* When PF10 references QA acceptance tokens, canonical token names and normative semantics live in **HDE-Governance** (and other owner canon as applicable). PF19 §9.2 provides the QA operational mapping and evidence bindings.

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

## **13.4 HDE-EPIC022 — Separation Pass 2 — Evidence discipline, error parity, stdout capture, and /internal/version bundle (D0–D3)**

**Status.**  
 HDE-EPIC022 continues Separation-phase closure work by hardening evidence discipline and tightening parity between CLI and Reader-facing error surfaces, while keeping rails posture explicit (closed rails for CI and deterministic artifact generation).

**PR1 (D0) — Acceptance scaffolding (CI-safe).**

* D0 delivered the epic’s canonical acceptance scaffolding at the expected paths:

  * `audit/qa/hde-epic022/token_evidence_matrix.md`

  * `docs/acceptance_map_epic022.json`

  * `audit/EPIC-022_close_report.md`

  * `audit/EPIC-022_MANIFEST.json`

* A CI-safe presence/structure test validated that the scaffolding files exist and parse, without changing runtime behavior.

* Placeholders in matrix/map are permitted at D0, but are explicitly non-claimable: no token is treated as satisfied until bindings are concrete.

**PR2 (D1) — Error envelope parity expansion (two missing required scenarios).**

* D1 expanded the Reader↔CLI error-parity harness to include the two missing required scenarios:

  * forced DB-unavailable, and

  * closed-rails vendor attempt (explicit vendor request while rails are closed).

* The epic produced stored parity artifacts for the new scenarios and tightened tests to enforce:

  * a fixed scenario roster,

  * strict byte equality between runtime results and stored artifacts, and

  * stable token map snapshot parity.

**Key drift vectors encountered (and the canonical fixes).**

* **Evidence skeleton coupling (ORIENTATION\_DRIFT).**  
   When governed evidence (Index/Mirror and new parity artifacts) changed without refreshing the topology orientation demo artifact, `orientation_demo.py --check` detected drift and failed CI. The canonical remediation is same-PR refresh \+ check of the topology orientation evidence (see §2.2.11).  
* **Acceptance artifacts discipline (placeholders and duplicate rows).**  
   D0 placeholders are allowed only in scaffolding PRs. Once real evidence exists, acceptance artifacts must be concretized:  
  * no `{scenario}` or “TBD” placeholder evidence strings for implemented tokens, and   
  * no duplicate token rows in the token/evidence matrix.  
* **Token bindings must not cite \`\*.path\_proof.txt\` as primary evidence.** Proof transcripts are required, but acceptance bindings must point to primary artifacts and the validator tests. Proofs are referenced via `proof_anchor` and mirror/proof checks (see §9.2.14); they must not appear as token evidence titles.  
* **Rails policy proof must be behavioral when used as such.**  
   “Env pins exist” is not treated as equivalent to “closed-rails vendor refusal is proven” when the epic uses `ENV_RAILS_POLICY_OK` as the rails-proof token for closed-rails vendor scenarios. EPIC022 binds that token to concrete refusal parity artifacts plus the enforcing parity test (see `ENV_RAILS_POLICY_OK` entry in §9.2.3).

**PR3 (D2) — Deterministic CLI stdout capture and binding hygiene.**

* D2 introduced deterministic, closed-rails `showcompat` stdout capture artifacts as governed evidence (stdout bytes \+ sha256 sidecar \+ args capture) and bound `CLI_STDOUT_LF_OK` to concrete tests and artifacts.

Note: If compatibility with older automation requires a legacy alias checksum filename, emitting an additional alias copy is permitted. For showcompat, this means an additional `artifacts/cli/showcompat/stdout.sha256` may be emitted alongside the canonical `artifacts/cli/showcompat/stdout.json.sha256`. The canonical file remains the verification target; record `CAVEAT: FILENAME_ALIAS_OK` describing the alias mapping.

* D2 kept broader stream discipline as a non-token mechanical requirement anchored by existing stream discipline tests; it did not mint new stream-discipline tokens.

* D2 maintained evidence skeleton coherence in the same PR as the new artifacts (Index \+ Mirror \+ topology orientation evidence).

**PR4 (D3) — `/internal/version` evidence bundle and evidence-system hardening.**

* D3 implemented EPIC022 `/internal/version` evidence capture by generating and committing the canonical internal\_version bundle artifacts under `artifacts/ops/internal_version/`, including:

  * `artifacts/ops/internal_version/body_get.json`

  * `artifacts/ops/internal_version/body_get.sha256`

  * `artifacts/ops/internal_version/headers_get.txt`

  * `artifacts/ops/internal_version/headers_head.txt`

  * `artifacts/ops/internal_version/headers_cond_if_none_match.txt`

  * `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`

  * `artifacts/ops/internal_version/request_chain_manifest.json`

  * `artifacts/ops/internal_version/two_run_identity.log`

Note: Conditional header filenames use the PF12 canonical names (`headers_cond_if_*`). Legacy variants (for example `cond_if_none_match_headers.txt`, `cond_if_modified_since_headers.txt`) are non-canon; if legacy aliases must be preserved for compatibility, emit alias copies alongside the canonical filenames and record `CAVEAT: FILENAME_ALIAS_OK` while keeping the canonical filenames as verification targets.

Note: Checksums for identity artifacts are optional when the sha256 and size are already captured via path proofs and the Evidence Index/Mirror. For example, a separate artifacts/ops/internal\_version/body\_get.sha256 sidecar may be omitted without failure if the evidence system already records the sha256 for body\_get.json. If legacy filename aliases must be preserved for compatibility, alias copies are permitted provided canonical filenames are present; record `CAVEAT: FILENAME_ALIAS_OK` describing the alias mapping.

* D3 updated acceptance bindings (token/evidence matrix and acceptance map) so `/internal/version` tokens bind to concrete tests and these governed artifacts, and updated the Human Evidence Index and Machine Mirror in the same PR.

* D3 also exposed two repeat churn vectors and remediations:

  * **PROOF\_SHA mismatch loops** in evidence validation (centered on mirror self-record / proof SHA expectations), remediated by tightening evidence tooling/validation and adding a dedicated self-record regression test.

  * **Optional dependency causing pytest collection failure** (example: missing `jsonschema`), remediated by making schema validation import-safe (skip/guard behavior rather than hard-fail) and by clarifying dependency posture for CI vs local.

**Remediation sequence (OPS-01/OPS-02 and PR-01..PR-03; EPIC022 internal\_version hardening).**

* **OPS-01 (DISCOVERY):** host reachability probe for GET `/internal/version`, selecting exactly one production host/base\_url with `http_status=200` and recording the selection. Evidence bundle includes a host matrix plus selection files and header captures under `audit/qa/<epic-id>/remediation/...`.

* **PR-01 (DISCOVERY):** single repo discovery report under the epic remediation QA tree with loci, expected files, and safe copy/paste commands. Report frames any undecided placement (for example request-chain manifest location) as TBD with constrained options, and avoids presenting epic-id flags as defaults in evidence tooling commands.

* **PR-02 (CHANGE):** introduce request-chain manifest \+ sibling path proof under the governed `/internal/version` evidence family and harden the contract test to fail closed if required artifacts are missing. Remediation fixes remove direct token bindings to `*.path_proof.txt` and keep auth posture non-canonized in runbooks.

* **OPS-02 (CHANGE / evidence capture):** run the committed runtime probe against the selected production host under open rails (`SAFE_MODE=0`, `ALLOW_NETWORK=1`), copy the governed `/internal/version` evidence family into a portable audit bundle, and produce a remediation-only snapshot manifest (sha256 \+ size per file).

* **PR-03 (CHANGE / governed evidence surfaces):** regenerate governed Evidence Index \+ Machine Mirror \+ sibling path proofs under closed rails, add an integration summary recording exact commands used, ensure the request-chain manifest is mirrored with a valid `proof_anchor`, and prove remediation-only bundle paths are not indexed.

This remediation sequence is treated as a repeatable pattern for “runtime-backed evidence bundle \+ governed index/mirror integration” work.

**PR5–PR6 (post-D3) — Evidence integrity repairs (governed artifacts only).**

After D3, EPIC022 required narrowly scoped follow-up repairs to restore trust in governed evidence integrity. These changes were confined to evidence tooling and governed evidence artifacts (no runtime Engine, CLI, or API behavior changes implied).

* **Ordering artifact proof drift repair.**  
   `artifacts/engine/order/abba_identity.bytes.path_proof.txt` was corrected to match the actual on-disk `artifacts/engine/order/abba_identity.bytes` bytes (size and sha256), and the corresponding Machine Mirror record for `engine.order.abba_identity.bytes` was refreshed to match. This restores the invariant that path-proofs and mirror rows must reflect exact stored bytes.

* **Human Evidence Index proof freshness repair.**  
   `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` were regenerated, but their governed path-proofs were stale (`docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt`). Evidence tooling was updated so the canonical updater refreshes these proofs during normal runs and fails in check mode if they are stale.

* **Reported verification posture.**  
   Both repairs were verified by running the canonical evidence updater in write mode and in `--check` mode under closed rails and determinism pins.

**Note on identity vs fixtures (D2).**  
 Deterministic CLI stdout capture artifacts are fixtures for canonical-bytes proofs. They are not release identity proofs; release identity remains governed by the `/internal/version` identity surface and its acceptance/evidence rules.

# **14\. Codespaces QA environments (environment details)**

## **14.1 Intent**

Codespaces is a supported Live QA execution environment, but it introduces pitfalls: ephemeral state, container drift, and unclear prerequisite documentation. This section defines the canonical requirements for Codespaces-based Live QA, including:

**Minimum required content (normative):**

* A stable, documented Codespaces/devcontainer configuration and required secrets/env var names (names-only; no values).

* A reference to the authoritative environment profile in this PF (see §14.5) for the epic being tested.

* A Step-0 Doc Delta Capture posture for missing/ambiguous prerequisites discovered during planning (see §14.6).

* A maintenance rule: changes to prerequisites must be reflected in this PF in the same change-set as the code change.

**Conformance note (normative):** Codespaces conformance is evaluated using the Codespaces-specific requirements in §14.6; reviewers MUST NOT treat any optional snapshot artifacts as an approval gate.

## **14.2 Definitions (codespaces vs prod vs QA console)**

**Codespaces / QA console.** A Codespace is a **QA console and artifact sink**: it runs commands and stores QA artifacts under `audit/qa/<epic-id>/…` in-repo.

**Prod.** For Live QA, “prod” is the deployed service surface defined in infra canon — **not** the Codespaces container.

**Closed rails vs open rails.** Closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0` plus env pins) are the default for CI and determinism work; open rails from a QA console are allowed only for explicitly defined Live QA steps and mandated rails postures.

## **14.3 QA environment set (Codespaces)**

Glow QA uses **four QA environments** (each may correspond to a distinct repo/workspace and Codespace configuration):

1. **HD Engine**

2. **App Back End**

3. **App Front End — Web**

4. **App Front End — Mobile**

This section defines the **Codespaces configuration** for each environment and the minimum verification checks required before it is used for QA.

## **14.4 Shared invariants (apply to all four Codespaces QA environments)**

### **14.4.1 Determinism env pins for governed bytes**

Any job that produces governed snapshots or evidence MUST export:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

**Canonical set only (normative).** The pins above are the only determinism env pins required by PF19 for Live QA conformance.  
 Live QA plans MUST NOT introduce additional “required pins” (for example `PYTHONHASHSEED`) as rails, prerequisites, or approval gates.

**Determinism posture (normative).** If any governed bytes are nondeterministic, determinism MUST be achieved in the producing tool via explicit ordering (stable sorts, deterministic serialization), not via interpreter/environment knobs.  
 Treat nondeterminism as a repo/tooling defect to drain via canon.

### **14.4.2 QA root and write-scope rails**

* Codespaces is a QA console and artifact sink. It MUST NOT be treated as “prod.”

* The canonical Live QA evidence root is: `audit/qa/<epic-id>/…` (lower-case `<epic-id>`).

* Live QA steps MUST NOT write outside `audit/qa/<epic-id>/…` for evidence.

### **14.4.3 Step-0 “Codespaces snapshot” (optional; non-gating evidence)**

A Codespaces “snapshot” artifact may be useful for debugging and reviewer context, but it is **NOT** a required Live QA deliverable.

**Non-gating rule (normative):**

* Plans MUST NOT require, validate, or gate approval on a Codespaces snapshot artifact.

* Reviewers MUST NOT use the presence/absence/contents of a snapshot to decide PASS vs REMEDIATION.

**If produced (optional guidance):**

**Minimum contents:**

* codespace/repo identifier (names-only)

* devcontainer image hash (if available)

* `uname -a`

* `node -v`, `pnpm -v`, `python --version` (as applicable)

* key env var names present (names-only; no secret values)

* timestamp

**Output location (if produced):**

* `audit/qa/<epic-id>/step0/codespaces_snapshot.md`

This file is separate from (and MUST NOT replace) the Step-0 Doc Delta Capture output.

## **14.5 Environment profiles (Codespaces config \+ minimum checks)**

**Template rule:** Fields marked **REQUIRED** must be populated for an environment profile to be considered “defined.”  
 Fields marked **OPTIONAL** may be omitted if not applicable.

### **14.5.1 HD Engine — Codespaces QA environment**

**Purpose.**  
 REQUIRED: Describe whether this Codespace is used as:

* a QA console into prod (typical for “Codespaces → Railway” Live QA), and/or

* a local dev harness runner for closed-rails determinism checks.

**Primary repo / workspace.**

* REQUIRED: Repo name (names-only): `<ENGINE_REPO_NAME>`

* REQUIRED: Default branch: `<BRANCH>`

* OPTIONAL: Codespace naming convention: `<CODESPACE_NAME_PATTERN>`

**Toolchain & entrypoints.**

* REQUIRED: CLI entrypoints expected available (names-only): `<CLI_ENTRYPOINTS>`

* REQUIRED: Test runner(s) expected (names-only): `<TEST_RUNNERS>`

* OPTIONAL: Language/runtime versions: `<PYTHON_VERSION>`, `<NODE_VERSION>`, etc.

**Runtime targets (prod-facing vs local).**

* REQUIRED: Prod-facing target(s) used for Live QA (titles-only; infra-defined): `<PROD_TARGETS_BY_TITLE>`

* OPTIONAL: Local dev harness base URL(s): `<LOCAL_BASE_URLS>`

* OPTIONAL: Ports used (local only): `<PORTS>`

**Rails & secrets posture.**

* REQUIRED: Default rails posture: `<CLOSED_OR_OPEN>`

* REQUIRED: Allowed rails toggles (names-only): `<SAFE_MODE_RULES>`, `<ALLOW_NETWORK_RULES>`

* REQUIRED: Required secret names (names-only; no values): `<SECRET_KEYS>`

**Minimum verification checks (before using this environment for QA).**

* REQUIRED: Closed-rails bootstrap check(s) (names-only): `<BOOTSTRAP_CHECKS>`

* OPTIONAL (if Live QA uses prod): Step-0 “prod handshake” check and evidence location (titles-only pattern).

**Evidence sinks.**

* REQUIRED: QA\_ROOT pattern: `audit/qa/<epic-id>/…`

* REQUIRED: Where environment snapshots and rails posture are recorded (titles-only): `<ENV_SNAPSHOT_ARTIFACTS>`

**Known constraints / caveats.**

* OPTIONAL: `<CAVEATS>`

---

### **14.5.2 App Back End — Codespaces QA environment**

**Purpose.**  
 REQUIRED: Describe what the App BE Codespace is used for (local API runs, test harness, contract tests, integration checks with HDE, etc.).

**Primary repo / workspace.**

* REQUIRED: Repo name (names-only): `<APP_BE_REPO_NAME>`

* REQUIRED: Default branch: `<BRANCH>`

**Local runtime (if applicable).**

* OPTIONAL: Start command(s) (copy/paste-ready): `<START_COMMANDS>`

* OPTIONAL: Local base URL: `<LOCAL_BASE_URL>`

* OPTIONAL: Ports: `<PORTS>`

**Integration edges (if applicable).**

* OPTIONAL: If this environment proxies or calls HDE surfaces, list the integration boundary (titles-only): `<HDE_INTEGRATION_POINTS>`  
   (HDE contracts remain owned by HDE-titled PF docs; this section records environment wiring only.)

**Rails & secrets posture.**

* REQUIRED: Default rails posture: `<CLOSED_OR_OPEN>`

* REQUIRED: Required secret names (names-only): `<SECRET_KEYS>`

**Minimum verification checks.**

* REQUIRED: Closed-rails bootstrap check(s): `<BOOTSTRAP_CHECKS>`

* OPTIONAL: Local service “up” check artifact: `<UP_CHECK_ARTIFACT_PATHS>`

**Evidence sinks.**

* REQUIRED: QA\_ROOT pattern: `audit/qa/<epic-id>/…`

---

### **14.5.3 App Front End — Web — Codespaces QA environment**

**Purpose.**  
 REQUIRED: Describe FE-Web QA use (unit tests, build verification, local dev server for UI checks, API integration validation, etc.).

**Primary repo / workspace.**

* REQUIRED: Repo name (names-only): `<APP_FE_WEB_REPO_NAME>`

* REQUIRED: Default branch: `<BRANCH>`

**Local runtime (if applicable).**

* OPTIONAL: Start command(s): `<START_COMMANDS>`

* OPTIONAL: Local base URL: `<LOCAL_BASE_URL>`

* OPTIONAL: Ports: `<PORTS>`

**Toolchain.**

* REQUIRED: Package manager (names-only): `<PKG_MANAGER>`

* REQUIRED: Test runner(s) (names-only): `<TEST_RUNNERS>`

**Rails & secrets posture.**

* REQUIRED: Default rails posture: `<CLOSED_OR_OPEN>`

* REQUIRED: Required secret names (names-only): `<SECRET_KEYS>`

**Minimum verification checks.**

* REQUIRED: Build/test bootstrap: `<BOOTSTRAP_CHECKS>`

**Evidence sinks.**

* REQUIRED: QA\_ROOT pattern: `audit/qa/<epic-id>/…`

---

### **14.5.4 App Front End — Mobile — Codespaces QA environment**

**Purpose.**  
 REQUIRED: Describe Mobile QA use (static checks, unit tests, build verification, integration checks, etc.). If Codespaces cannot run required mobile runtime surfaces, state that explicitly and define the alternate QA console(s) by title.

**Primary repo / workspace.**

* REQUIRED: Repo name (names-only): `<APP_FE_MOBILE_REPO_NAME>`

* REQUIRED: Default branch: `<BRANCH>`

**Runtime constraints.**

* REQUIRED: Whether local app execution is supported in Codespaces: `<YES_NO>`

* OPTIONAL: If not supported, define the required non-Codespaces environment(s) by title: `<ALTERNATE_ENV_BY_TITLE>`

**Toolchain.**

* REQUIRED: Build system / tooling (names-only): `<BUILD_TOOLING>`

* REQUIRED: Test runner(s) (names-only): `<TEST_RUNNERS>`

**Rails & secrets posture.**

* REQUIRED: Default rails posture: `<CLOSED_OR_OPEN>`

* REQUIRED: Required secret names (names-only): `<SECRET_KEYS>`

**Minimum verification checks.**

* REQUIRED: Bootstrap checks: `<BOOTSTRAP_CHECKS>`

**Evidence sinks.**

* REQUIRED: QA\_ROOT pattern: `audit/qa/<epic-id>/…`

## **14.6 Ownership and maintenance**

For each environment profile above, record:

* **Responsible owner (role or team):** `<OWNER>`

* **Accountable reviewer (role):** `<ACCOUNTABLE>`

* **Update trigger(s)** (examples):

  * repo/toolchain change that affects QA steps

  * Codespaces base image change

  * secrets or env-var interface changes (names-only)

  * devcontainer changes that affect shells, entrypoints, or tooling availability

### **Same change-set rule (normative)**

Any change to Codespaces/devcontainer requirements, required env var names, required secret names, or other Live QA prerequisites MUST be reflected in this section (and the relevant profile in §14.5) in the same change-set that introduces the new requirement. “Plan-only” prerequisites and tribal knowledge are non-conforming.

### **Doc delta capture step (normative, planning allowed)**

Live QA planning is allowed even when Codespaces prerequisites are incomplete or unclear, but plans MUST NOT assume or invent missing details.

**Routing (normative):** Mandatory Step-0 artifacts (including Doc Delta Capture posture) are governed by PF27 — Plan Templates. This section adds Codespaces-specific requirements for how doc deltas are recorded.

Every Live QA plan executed in Codespaces MUST include a Step-0 **Doc Delta Capture** step that:

* lists each missing or ambiguous prerequisite discovered during planning, separated into:

  * **BLOCKERS** (execution cannot proceed without resolution)

  * **CAVEATS** (execution can proceed with constrained scope or reduced confidence)

* names the intended fix location for each item (either §14.5 profile fields, or an owning PF doc by title only)

* records a resolution status for each item (for example: unresolved, resolved by doc update, resolved by existing canonical reference)

The Doc Delta Capture step MUST write its output under `audit/qa/<epic-id>/…` (names-only; no secret values). If no deltas are found, the step MUST still produce an explicit “no deltas” output.

### **Conformance rule (normative)**

A Live QA run executed in Codespaces is non-conforming for approval if any of the following is true:

* the relevant environment profile in §14.5 is not defined (REQUIRED fields remain unpopulated or contradictory), or

* the plan did not include (and the run did not produce) the required Step-0 Doc Delta Capture output defined above

Environment details MUST be kept current so that QA plans do not rely on guessing. Missing or contradictory prerequisites MUST be captured as doc deltas during planning, and execution steps that depend on unresolved prerequisites MUST be treated as blocked until the prerequisites are resolved by canonical documentation.

