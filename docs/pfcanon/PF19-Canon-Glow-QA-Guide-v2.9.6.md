# **0\. Front Matter**

## **0.1 Header**

**Title:** PF19-Canon-Glow-QA-Guide  
**Status:** Canon  
**Version:** v2.9.6  
**Effective date:** 2026-08-13  
**Last Update Gate:** 0808 refresh 6  
**Invocation tag:** INV-f2ac55d77ce9aacc

## 0.2 Purpose & scope

Purpose. Standardize pre-commit and post-commit QA across HDE, Catalog/A7, Aux, App FE/BE, DB/Vendor ingest, and CLI/API. This guide defines what to check and where to route policy; concrete bytes, schemas, and tokens remain in their existing single homes.

Scope rule. Any document with “HDE” in its title is HD Engine–specific. PF19 points to those documents by title only and does not duplicate their contents. PF19 itself covers all projects (Engine \+ App \+ shared tooling).

HD Engine specifics are delegated, titles-only, to:

* PF01 — HDE-Math-Spec  
* PF02 — HDE Architecture  
* PF04 — HDE-Governance  
* PF05 — HDE-CLI-API-Vendor-Ref  
* PF09 — HDE-Build Checklist  
* PF12 — HDE-Schemas & Artifacts  
* PF14 — HDE-Mechanics Guide  
* PF16 — HDE Epics Map (historical context only)  
* PF17 — HDE Narratives Guide  
* PF09 phased reference rule (normative).  
  * The former single-document PF09 is retired for active reference use.  
  * New QA plans, review artifacts, remediation guides, and future PF19 updates MUST reference the relevant phased PF09 document or documents, identified as PF09.1 through PF09.7, rather than the retired single-document PF09.  
  * Existing PF19 mentions of “PF09 — HDE-Build Checklist” should be read as family references to the phased PF09.x documents until those mentions are drained to the narrower phase-specific home.  
  * Where a QA question crosses phase boundaries, the artifact MUST name the exact phased PF09.x document or documents consulted rather than treating the retired single-document PF09 as the active source.

Epics and phased planning (titles-only).

PF19 treats epic planning and phase mapping as outside its scope.

For HD Engine epic history:

* HDE Phased Epics is historical-only: it MUST contain only completed epic records (formally closed per Epic-Process-Guide, titles-only) and is updated only at epic close (no in-flight placeholders).  
* HDE Epics Map is maintained as historical context only and must not be used as the source of truth for new work.

In particular:

* HDE-EPIC011 — Vendor Ingest & Data Durability is recorded as a failed epic; its acceptance roster (DB posture, ingest idempotence, evidence discipline, partition plan, SAFE rails, BodyGraph invariance) did not reach a fully green, production-ready state.  
* HDE-EPIC012–HDE-EPIC014 are preserved as “won’t do” (historical design), and any residual work they described must be captured as recorded debt or re-scoped into a future epic, not treated as open acceptance here.

Role boundary (normative; no governance / no tokens / no planning).

PF14 is a mechanics/components reference only. It:

* MUST NOT define, rename, alias, or curate acceptance token spellings.  
* MUST NOT act as a planning authority (it may inform planning, but does not govern epic plan structure, acceptance rosters, or close gates).  
* When PF14 needs to mention governance or acceptance, it MUST route to the governing document by title (and section if needed) and remain descriptive about component fields and mechanical responsibilities only.

PF19 may reference these epics by title when describing QA history or preservation surfaces, but any new epic-level QA decision (for example, where to land future PK, partition, or Catalog/A7 work) MUST be captured in the epic’s in-flight planning and QA ledger artifacts and then reflected in the archived epic record at close. HDE Epics Map is historical-only and MUST NOT be treated as a home for new decisions. HDE Phased Epics is historical-only and MUST NOT be treated as an in-flight tracker.

PF19 owns QA principles, checklists, and cross-component playbooks; it routes all transport, math, schema, and token details to those single homes.

Reality Audits vs QA tokens (titles-only).

PF19 treats Reality Audits as a separate axis from QA token semantics. Reality Audits (as defined in Reality Audits) are PO-only, post-epic architecture reviews that may be in scope or out of scope for a given epic or implementation plan.

Decisions to run, skip, narrow, or broaden a Reality Audit for a specific epic:

* do not add, remove, or weaken any QA Acceptance Tokens in this guide;  
* do not change which QA tokens exist in the PF19 registry, how they are named, or what evidence they require; and  
* do not change the requirement that epic acceptance maps and manifests bind tokens to governed evidence families as described in §9.2.12.

PF23 scope choices are local to a plan or epic and must be recorded there (for example in HDE Phased Epics or HDE-Build Notes by title). PF19’s QA tokens and their governance rules remain global and unaffected by per-epic Reality Audit decisions.

Planning posture: mandatory PF23 consult (components \+ pathnames).

PF23 is a consultative reality audit. It is a required consult step for QA planning, including drafting, reviewing, and approving Live QA Plans, but it does not itself define QA acceptance and it MUST NOT be treated as acceptance proof.

Freshness posture (informative). PF23 is often fresher than PF19 and older epic plans for repo-reality context, but PF canon remains authoritative when there is a conflict.

How to use PF23 in QA planning (plan lint: no invented claims):

* If PF23 is cited, anchor to a specific PF23 section and heading.  
    
* Use direct quotes (verbatim) and label them explicitly as PF23 consult input.  
    
* PF23 may be used to identify component boundaries, canonical pathnames, and repo loci, but any repo-resident locus in the plan MUST still satisfy the locus provenance rules in this guide.  
    
* Reviewers SHOULD consult PF23 before approving any plan that names repo-resident loci.  
    
* PF23 MUST NOT be consulted during PR analysis or review of code diffs.

PF23 consult is planning-time only (no Live QA deliverables). Live QA plans MUST NOT require any PF23 consult capture artifact (for example `pf23_consult.md`) and MUST NOT include PF23 operator commands as execution steps. If present, a “PF23 Anchors” note is informational only and MUST be non-gating.

Deconflicting PF23 vs PF canon (drift protocol stub). If PF23 appears inconsistent with other allowed repo-reality sources, treat the situation as a reality ambiguity and DO NOT guess or assert a reconciled locus as fact in the plan. Record a drift note with the PF23 anchor, the conflicting canon reference (by title and section), and the adjudication owner. Do not treat the QA plan or Live QA execution as the adjudication venue.

Ownership (normative). PF23 is PO-maintained. Planning documents MUST NOT create tasks that assign PF23 updates. If PF23 appears stale or missing required component coverage, the plan MAY note that as an observation, but must not assign it as agent work.

## 0.3 Acceptance tokens (names-only; initial)

The following governance tokens apply to PF19 itself; definitions and semantics live in HDE-Governance and HDE-Build Checklist:

* QA\_PRECOMMIT\_CHECKLIST\_OK  
* QA\_POSTCOMMIT\_CHECKLIST\_OK

## 0.4 Principles & Single Homes (routing only)

### 0.4.1 Intent

Pin what PF19 owns (process, checklists, playbooks) versus where bytes and policy live. PF19 stays names-only and routing-only.

PF19:

* stays titles-only for all external references, and  
* never redefines transport bytes, schemas, or token semantics; §9 may mirror registered names only for QA operational mapping and must identify the owning source.

### 0.4.2 Single homes (titles-only)

PF19 routes to these existing single homes:

* Transport bytes & public routes: PF05 — HDE-CLI-API-Vendor-Ref  
* Schemas & artifacts (catalogs, mirror, proof JSON): PF12 — HDE-Schemas & Artifacts  
* Governance (A7 policy, refusal/writers, tokens): PF04 — HDE-Governance  
* Architecture (single emitter, boundaries): PF02 — HDE Architecture  
* Build checklists & CI gates: PF09 — HDE-Build Checklist  
* Narrative rules & surfaces: PF17 — HDE Narratives Guide  
* Process (PR-first): PF06 — Epic-Process-Guide

### 0.4.3 Core principles (names-only).

PF19 assumes and reinforces these core QA principles.

PF19 is titles-only for cross-references. It does not duplicate bytes or schemas and always routes to the owning PF by title. PF19 never redefines wire contracts or token semantics. Those definitions remain in the owning PF homes (for example the CLI/API reference, schemas and artifacts, governance, and the build checklist).

Determinism and env pins apply in all environments whenever governed bytes are produced. All canonicalization, hashing, header snapshotting, and governed evidence capture must run with LC\_ALL=C, LANG=C, and TZ=UTC in dev, stage, prod, and CI. Interpreter/runtime knobs such as PYTHONHASHSEED must not be treated as required rails pins unless a specific step explicitly depends on hash-iteration determinism. If such a knob is present, plans may record it as observed context. If absent, plans must not fail or block on that basis.

Evidence is governed by same-PR parity and completeness, not just formatting. The Human Evidence Index (docs/evidence/INDEX.json \+ docs/evidence/INDEX.sha256) and the Machine Mirror (artifacts/evidence\_index.jsonl) must be updated together in the same PR whenever evidence changes, and QA must treat “code change without evidence parity” as a failure, not a warning.

For every governed artifact under a governed evidence root declared in the Evidence Catalog (titles-only, with schemas and semantics defined only in HDE Schemas and Artifacts), QA must ensure the triple is complete:

* one Human Evidence Index entry,  
* one Machine Mirror record, and  
* one co-located path\_proof.txt whose path is referenced by the Mirror record’s proof\_anchor.

This also applies to lifecycle and OPS-managed artifacts (for example backup/restore/retention runs). If any leg is missing, QA must treat the evidence as incomplete and block tokens that depend on it.

Path-proof freshness is normative for the Human Evidence Index and its hash sentinel. docs/evidence/INDEX.json and docs/evidence/INDEX.sha256 are governed artifacts, and their co-located path-proof transcripts (docs/evidence/INDEX.json.path\_proof.txt and docs/evidence/INDEX.sha256.path\_proof.txt) must be refreshed whenever the index or sentinel bytes change, in the same PR. Stale INDEX path-proofs are merge-blocking evidence integrity failures and must be remediated by rerunning canonical evidence tooling, not by hand-editing proofs.

Baseline HD Engine evidence must remain agent-readable at the PR level. The primary evidence ledger must be expressed through plain-text artifacts under governed paths (docs/**, artifacts/**, audit/\*\*), such as the Human Evidence Index, the Machine Mirror, bundle manifests, and key QA logs and step transcripts.

Binary or compressed bundles may exist as supplementary artifacts, but they must not be the only governed evidence for any acceptance token that requires payload inspection by an agent. Hash-only or status-only proof families are acceptable only when the evidence consumer does not need to inspect payload content. Otherwise, they must be paired with at least one governed text artifact (for example a bundle manifest, QA log, or summary) that exposes the relevant payloads at the evidence ledger level. Titles and schemas for these artifacts remain in HDE Schemas and Artifacts, the build checklist, and related PF docs.

Live QA evidence should be mechanical, and narrative belongs elsewhere. Live QA and bootstrap evidence should be logs, JSON, exit codes, tree/env snapshots, and scripted notes written under `audit/qa/<epic-id>/<EPIC_QA_SUBPATH>/`, not hand-edited prose by the PO. Narrative QA addenda and synthesis (for example epic QA reviews, build-note summaries, PF20 closeouts) are authored by QA personas and Leads in PF10 (build notes) and HDE Phased Epics (titles-only), not in Live QA notes files.

CI runs with rails closed by default. CI pipelines run with SAFE\_MODE=1 and ALLOW\_NETWORK=0 unless explicitly opened. Any job that opens rails must pin SAFE policy (timeouts/retries/backoff from closed domains, no jitter) as defined in governance, attach governed evidence, and update the Human Index and Machine Mirror in the same PR.

A7 is Catalog-only and is gated by the Endpoint Catalog. A7 proofs run only on a cataloged JSON success route and do not treat /internal/\* routes (including /internal/version) as an A7 surface. Aux HEAD/304 are out of scope under EPIC-010. A7 QA runs only when docs/ENDPOINTS\_CATALOG.json exists and is valid per HDE Schemas and Artifacts, and the Catalog row for the Reader JSON success surface exists and is marked as a JSON success route. If those conditions are not met, QA treats the A7 suite as gated off: no A7 tokens are claimed for that PR, and the missing or invalid Catalog entry is reported as a QA failure, not a cosmetic skip.

Industry anchors are reference-only. PF19 aligns its QA rules and proofs with IETF RFC 9110/9111 for HTTP semantics and caching, RFC 8785 (JCS) as an external anchor for JSON canonicalization, OWASP ASVS for FE/BE security verification, and NIST SSDF and SLSA for supply-chain QA and provenance expectations. PF19 remains titles-only: bytes, schemas, and token definitions stay in their owning PF homes (for example PF05, PF12, PF04, PF09).

---

# 1\. Environments & surfaces map (names-only)

## **1.1 Intent**

Name the QA-relevant surfaces and where their ownership lives, with a clear split between:

* App layer (FE/BE)  
* HD Engine layer (HDE service and its callers)  
* Shared tools and evidence system

HDE-titled PF docs apply only to HD Engine surfaces. They do not define contracts for pure App FE or non-HDE App BE endpoints. PF19 stays names-only here: no header matrices, no byte listings, no schemas.

## **1.2 App layer (FE and non-HDE backend)**

These components use their own product and API docs. HDE PF docs are only relevant where the App talks to the Engine.

* App FE (public web/app).  
  * Public-facing web and app experience. QA focuses on routing, feature flags, user flows, and integration with backend APIs.  
  * Implementation and deploy: frontend repo and deploy target (names-only).  
  * Contracts and behavior: app-level product and API docs (titles-only, non-HDE).  
  * HDE docs: not authoritative for FE; only relevant at the points where FE calls backend endpoints that themselves proxy HDE.  
* App BE (service APIs beyond HDE).  
  * Application backend services that are not the HD Engine. QA focuses on API contracts, auth, data validation, and error posture.  
  * Implementation and deploy: backend repo and service surface (names-only).  
  * Contracts and behavior: backend API specs and app-specific docs (titles-only, non-HDE).  
  * HDE docs: apply only to those BE endpoints that directly call or proxy HD Engine routes; all other BE endpoints are governed by app-specific docs, not HDE PF docs.

## **1.3 HD Engine layer (HDE-only)**

HDE PF docs apply only to the Engine’s surfaces and their direct callers: Catalog/Reader JSON success (A7 surface), Aux narrative text (non-A7), CLI admin preview using the same emitter, and the Required-Now admin bundle CLI and HTTP surfaces that package the full product payload for a single match. Admin bundle surfaces are admin-only, explicitly non-A7 requirements and are routed by PF19 to Governance, CLI/API, Mechanics, and Schemas & Artifacts by title only. App FE/BE are out of scope for HDE policy except where App endpoints proxy HDE; in those cases they must preserve HDE contracts.

* HD Engine service (Reader and Aux; Required-Now admin bundle HTTP route not found in the inspected repository).  
  * Current Engine HTTP surfaces exposed to the App BE as internal services include Reader JSON and Aux narrative text. The Required-Now admin bundle HTTP route remains an implementation gap in the inspected repository.  
  * Implementation and deploy: engine service on Railway prod (names-only, see Glow Infrastructure).  
  * Transport bytes and public routes (including the admin bundle HTTP route): HDE-CLI-API-Vendor-Ref.  
  * Architecture and boundaries (including separation of Catalog/Reader, Aux, admin-only routes, and ops endpoints): HDE Architecture.  
  * Governance, A7 policy, and admin-surface auth/logging posture: HDE-Governance.  
  * Admin bundle builder mechanics and use of the canonical serializer/emitter: HDE-Mechanics Guide and HDE-Schemas & Artifacts.  
  * All other Engine details: HDE-titled PF docs by title only.  
  * Epics map (historical-only). For HD Engine epics, HDE Epics Map is historical-only; it records past epic allocations, including HDE-EPIC011 as a failed epic and HDE-EPIC012–HDE-EPIC014 as “won’t do”. HDE Phased Epics is also historical-only: it contains only completed epic records and is updated only at epic close (no in-flight records). QA must treat these documents as historical context and MUST NOT use them for in-flight tracking or as a planning gate.  
* Admin bundle CLI surface (admin-only; Required-Now).  
  * Required behavior: call the admin bundle builder and return the full product payload for a single match as a single canonical JSON object.  
  * Implementation posture: `hdctl admin-bundle` was not found in `engine/cli/main.py` at the pinned commit. Its exact invocable and remote-request bytes remain `OPEN` in HDE-CLI-API-Vendor-Ref.  
  * Target environment: Railway HD Engine prod service and DB, configured via infra canon (titles-only).  
  * Governance and auth: HDE-Governance (admin token or equivalent credential required; numeric-bearing content remains admin-only and outside the Reader public covenant).  
  * QA playbooks and tokens: this guide (PF19) and HDE-Build Checklist (titles-only).  
* HD Engine integration in App BE.  
  * Backend endpoints that call HDE are responsible for preserving HDE contracts at the integration boundary.  
  * HDE contracts: defined only in HDE-titled PF docs (titles-only, no duplication).  
  * App BE wrapping behavior: defined in backend API docs; PF19 treats it as part of App BE QA with additional checks that HDE contracts, including admin-only boundaries, are honored.

## **1.4 Shared tools and evidence system**

These pieces are cross-cutting. Some are HDE-specific in terms of contract, but they affect how QA is done across projects.

* CLI/API and SDKs (dev tools).  
  * Developer-facing tools that exercise the Engine and App. QA focuses on parity with emitters and deterministic behavior.  
  * Implementation: CLI and SDK repos (names-only).  
  * Transport and CLI contracts for HDE flows: PF05 — HDE-CLI-API-Vendor-Ref.  
  * For App-only tools, contracts live in app-specific docs; HDE PF docs only apply when the tool calls HDE.  
  * For CLI/API and SDKs, PF19 treats two equivalent QA surfaces:  
    * a Codespace attached to the engine repo acting as a QA console, and  
    * any other terminal or shell that is configured (by infra canon) to reach the HD Engine prod service and DB on Railway.  
  * Both surfaces are governed by the same CLI/API contracts (titles-only) and QA tokens; plans must not assume that CLI QA is restricted to Codespaces only when other terminals can reach the canonical Railway endpoints defined in infra canon.  
* Internal/dev HTTP harnesses (e.g. /internal/dev/sampler).  
  * Dev-only HTTP routes exposed by the Reader/adapter for internal QA or evidence flows (for example POST /internal/dev/sampler for sampler behavior).  
  * Implementation and wiring (start commands, ports, host binding) live in infra-facing docs such as Glow Infrastructure and HDE-Mechanics Guide (internal/dev surfaces sections, titles-only).  
  * Transport behavior and internal/dev HTTP semantics (JSON shape, writer-style error envelopes, headers such as Cache-Control: no-store and “no ETag” posture) live in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide (titles-only). PF19 does not restate these bytes; it only routes QA to them.  
  * Infra/ops ownership. For any internal/dev HTTP harness intended for QA or evidence:  
    * Infra/ops MUST provide and own:  
      * a canonical dev start command or service definition that runs the Reader process in dev/Codespaces with APP\_ENV=dev (and any determinism rails required by Mechanics), and  
      * a corresponding base URL and port per environment (for example Codespaces vs local dev), from which concrete URLs such as DEV\_SAMPLER\_URL=[http://127.0.0.1](http://127.0.0.1):\<port\>/internal/dev/sampler can be derived.  
    * These URLs MUST NOT be guessed by PO, QA, or doc agents. They MUST be derived from the actual Reader process wiring (ports and host binding) as configured by infra and captured in infra canon.  
    * Before handing any dev harness URL to QA (for curl, scripts, or external tools), Infra/ops MUST validate it locally with a simple HTTP/1.1 JSON POST under appropriate rails (at minimum APP\_ENV=dev and, where feasible, determinism env pins) and confirm that the response shape and headers match the internal/dev HTTP behavior specified by the owning PF docs (titles-only).  
  * QA consumption rule. QA and PO agents:  
    * MAY consume infra-provided dev harness URLs in QA plans, scripts, and Live QA steps, but  
    * MUST NOT define or change those URLs themselves. If a dev harness URL or start command is missing or unclear, QA must treat that as a spec/infra gap (see §11.3 canon-first rule), mark affected steps as blocked by infra wiring, and request an infra update rather than guessing ports or paths.  
* DB/Vendor ingest (authoring plane, sealed packs).  
  * Pipelines that turn vendor/bodygraph inputs and authored narratives into sealed, versioned packs used by the Engine.  
  * Implementation: ingest and authoring jobs plus DB layer (names-only).  
  * Schemas and artifacts (packs, manifests, proof JSON): PF12 — HDE-Schemas & Artifacts.  
  * Vendor HTTP posture and ingest calls: PF05 — HDE-CLI-API-Vendor-Ref.  
* Evidence system (indices, mirror, proofs).  
  * Cross-project system that records what was proven, where, and when. Used by both Engine and App QA, but contracts are defined in HDE PF docs.  
  * Human Evidence Index and hash sentinel: PF09 — HDE-Build Checklist (process) and PF12 — HDE-Schemas & Artifacts (schema).  
  * Machine mirror, path-proofs, composite proof JSON: PF12 — HDE-Schemas & Artifacts.

(Names-only section. No header tables, no byte or schema listings.)

# 2\. Pre-commit QA (local/CI)

## **2.1 Intent**

Catch issues before PRs merge by enforcing a consistent local/CI QA baseline across all projects.

Pre-commit QA focuses on:

* code quality and formatting  
    
* deterministic behavior (no hidden I/O or randomness)  
    
* snapshot and evidence hygiene  
    
* early detection of schema/contract drift

Concrete CI wiring and gates are instantiated in PF09 — HDE-Build Checklist (titles-only); PF19 defines the shared “what,” not the CI job syntax.

## **2.2 Checklist (to be instantiated in PF09 CI)**

### **2.2.1 Lint and format**

Pre-commit pipelines SHOULD run language-appropriate linters/formatters and fail on style or syntax issues.

### **2.2.2 JSON/JSONL canonicalization and final-LF checks**

* Enforce canonical form for governed JSON/JSONL files.  
    
* Require exactly one trailing linefeed on governed text artifacts.  
    
* Reject non-canonical or mixed-style JSON in governed paths.

### **2.2.3 Deterministic, no-I/O unit tests**

* Pure paths MUST NOT depend on RNG, wall-clock time, external network, or filesystem state.  
    
* Tests SHOULD prove two-run identity where applicable (same inputs → same outputs/bytes).

### **2.2.4 Env pins for snapshot generation**

For any job that produces snapshots or evidence, export:

* `LC_ALL=C`  
    
* `LANG=C`  
    
* `TZ=UTC`

This applies to Engine, App, and shared tools whenever they emit governed artifacts.

### **2.2.5 Tooling vs behavior failures (pytest and harnesses)**

QA plans and CI logs MUST distinguish tooling failures (for example, missing or non-executable test entrypoints such as `.venv/bin/pytest`) from application/behavior failures (for example, ingest tests failing assertions). A failure where the test harness cannot even start (for example, “cannot execute: required file not found” when invoking `.venv/bin/pytest`) MUST be classified and recorded as an environment/tooling defect, not as a red behavior verdict for the suite under test.

In Codespaces and similar venv-based environments, the preferred invocation pattern for QA and CI is:

* Activate the venv (for example `source .venv/bin/activate`).  
    
* Run tests via `python -m pytest <args>` rather than relying on a wrapper script in `.venv/bin/pytest`.

QA plans SHOULD use `python -m pytest` in copy/paste-ready commands for test-driven steps (including ingest tests), and PF09 CI harnesses SHOULD mirror this pattern where practical.

When a tooling failure is encountered (for example `.venv/bin/pytest` is broken but `python -m pytest` succeeds):

* The failure MUST be captured mechanically in a QA log under `audit/qa/<epic-id>/<EPIC_QA_SUBPATH>` with a clear label (for example a `D0-<id>` or `D2-<id>` log entry noting “tooling failure: pytest shim unusable; rerun with python \-m pytest”).  
    
* The suite MUST be re-run once a working invocation (`python -m pytest <args>`) is available under the same intended rails (`SAFE_MODE`, `ALLOW_NETWORK`, env pins).  
    
* Only the rerun outcome (pass/fail under correct tooling and rails) is used to judge the behavior of the tests and to satisfy behavior tokens such as `TESTS_PASS_OK`. Tooling failures that are successfully bypassed via the canonical `python -m pytest` pattern must not be treated as ingest/behavior failures.

If neither `.venv/bin/pytest` nor `python -m pytest` can run the required tests (for example pytest is not importable or the venv is missing), the affected checklist items and tokens (for example ingest-related DISS tasks) are considered blocked by tooling under PF19/PF09/PF07 until the environment is fixed. QA must record this as a tooling blocker (not as a red behavior verdict) and resolve the infra/venv issue before treating the underlying tests as truly failing.

Import-time dependency failures are tooling, not behavior.

If a pytest run fails during collection/import (for example `ModuleNotFoundError: jsonschema`) before any tests execute, QA MUST classify this as a tooling failure (`FAIL_TOOLING` / `TOOLING_BLOCKED`). Acceptable remediation patterns are:

* Required dependency mode: treat the dependency as required for the relevant CI job and ensure CI installs the required dependency set (for example dev requirements) so the tests actually run.  
    
* Optional dependency mode: guard optional dependencies so pytest collection succeeds and the relevant tests either run or skip with an explicit, actionable install hint (for example `pytest.importorskip("jsonschema", reason="install requirements-dev.txt to run schema validation")`).

QA MUST NOT treat “collection died due to missing optional dependency” as a product behavior failure.

Proof-string checks against governed prose are harness checks, not behavior proof by themselves. A casing-only, punctuation-only, whitespace-only, or phrase-shape mismatch against governed prose MUST NOT be classified as final `FAIL_BEHAVIOR` until the raw artifact, intended semantic proof target, and governed source posture have been reviewed. When the intended proof target is preserved and the mismatch is a QA evidence-harness defect, the final verdict must come from the accepted rerun or remediation receipt, and the original failed proof must remain preserved as failure context rather than being erased or treated as product behavior failure.

This is also a plan-review requirement for executable QA steps.

* Any pytest-backed or tool-backed QA step MUST declare the exact dependency set it requires, the explicit preflight check or checks that prove each dependency is present and runnable, and the exact activation or installation action to use when the dependency is missing and remediation is allowed in the execution venue.  
* If the plan cannot truthfully specify the activation or installation action, it MUST say so explicitly and MUST classify a failed preflight as `FAIL_TOOLING` or `TOOLING_BLOCKED`. It MUST NOT invent installation commands and it MUST NOT let dependency failure collapse into `FAIL_BEHAVIOR`.  
* Per-step enforcement is required. A shared bootstrap step does not remove step-local responsibility. Each later QA step MUST either include its own dependency preflight and remediation logic inline or explicitly depend on the bootstrap step and rerun a short step-local readiness check before the main command.  
* The dependency preflight result, any install or activation action taken, and the final ready or not-ready outcome MUST be captured in the step’s governed QA evidence stream.  
* Any QA plan or QA step that omits dependency preflight and install or remediation posture for a required dependency is non-conforming and blocked for approval.

### **2.2.6 Rails posture in CI (default CLOSED)**

Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default.

If any pre-commit job opens rails (network I/O), it MUST produce governed evidence and index it in the same PR (titles-only routing to PF12/PF09).

### **2.2.7 Machine mirror quick-check (includes path-proofs)**

* Verify `artifacts/evidence_index.jsonl` exists and is the only mirror file; records are canonical JSONL (sorted keys, compact, one LF, unknown-key reject, pinned field order).  
    
* Verify each record’s `proof_anchor` points to an adjacent stored path-proof; fail CI if any proof is missing.  
    
* Enforce “governed roots only”: all indexed artifacts MUST live under a governed evidence root declared in the Evidence Catalog (HDE Schemas & Artifacts, titles-only). Indexed artifacts MUST NOT use transient/generator paths or ad-hoc roots that are not cataloged.

### **2.2.8 Snapshot hygiene (tolerant vs strict)**

* Classify snapshots as strict (must match exactly) or tolerant (pattern-based).  
    
* Pin patterns where applicable (for example text posture harnesses; see §6.2 harness).  
    
* Fail if strict snapshots drift unexpectedly.

### **2.2.9 Keys-only logs in tests**

When tests exercise logging, ensure logs are keys-only and contain no payload bodies or secrets.

Logging policy and redaction rules live in HDE-Governance; PF19 only requires that tests respect them.

### **2.2.10 Drift / schema enforcement for governed artifacts**

Treat each of the following as a CI failure for governed artifacts:

* unknown keys in the machine Mirror  
    
* non-canonical snapshots under governed paths  
    
* missing trailing LF on governed text

Schema and gate definitions live in HDE-Schemas & Artifacts and HDE-Build Checklist; PF19 requires CI to enforce them.

### **2.2.11 Evidence-governed CI sequence (names-only)**

For PRs that change governed evidence artifacts, authorized local or pre-commit authoring and hosted CI verification are separate phases. Both phases MUST run under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

An authorized authoring phase MAY run canonical writers to prepare governed artifacts. Hosted CI MUST verify the exact committed source under review and MUST NOT repair, refresh, or rewrite tracked source to make a decisive committed-state check pass.

* Generate ordering artifacts when in scope.  
  * During authorized authoring, run the canonical ordering writer once and then run its actual check entrypoint to prove a stable fixed point.  
  * Hosted CI MUST run the check entrypoint against the committed ordering artifacts. Missing, stale, or drifting artifacts MUST fail the check rather than being repaired in the source checkout.  
* Treat every non-writing check as non-mutating.  
  * A non-writing check MUST NOT mutate the repository or external state. Prohibited external-state actions include opening a database connection, executing SQL, committing a transaction, applying a migration, or mutating an external service.  
  * When a verifier executes a route with a persistence seam, direct side-effect interception tests MUST prove that the persistence seam is not invoked.  
* Update the Human Evidence Index and Machine Mirror during authorized authoring, then verify them without repair.  
  * The authorized writer MUST refresh the Index, Mirror, and applicable path proofs from the final on-disk bytes, including at minimum:  
    * `docs/evidence/INDEX.json.path_proof.txt`  
    * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * The writer’s actual check entrypoint MUST then confirm a stable second pass with no drift, dangling artifacts, missing proofs, or schema violations.  
  * Hosted CI MUST execute that check entrypoint against the committed bytes and MUST fail rather than regenerate a stale or inconsistent evidence graph.  
* Run topology orientation during authorized authoring, then verify it without repair.  
  * The authorized writer MUST refresh `audit/gates/topology/orientation_demo.txt` only after the final Index and Mirror state exists.  
  * The writer’s actual check entrypoint MUST confirm that the orientation output matches the final Index and Mirror and remains stable.  
  * Hosted CI MUST run the check entrypoint against the committed orientation output and MUST fail rather than refresh it.  
* Enforce Mirror schema and path-proof discipline.  
  * Run the Mirror-schema quick-check described in §10.5 to validate canonical JSONL, schema strictness, required fields, pinned field order, stable line endings, the single Mirror file, and `proof_anchor` alignment with `*.path_proof.txt`.  
* Run ordering and evidence test suites.  
  * Run the pytest suites that cover ordering properties and evidence correctness. Any failure is a CI failure for the affected governed artifacts.  
* Keep scoped closure lanes additive.  
  * A scoped CI or QA lane MAY provide additional proof for a governed evidence subset.  
  * The main lane MUST continue to run the full repo-wide evidence and fail-closed coverage applicable to the touched governed surfaces.  
  * QA MUST NOT narrow the main lane to the scoped subset or treat the scoped lane as a substitute for broader evidence correctness, Mirror discipline, or retained global safeguards.  
  * A scoped closure result is trustworthy only when the scoped lane and the retained main-lane safeguards are green.  
* Verify proof producers through their real entrypoints.  
  * Each governed artifact family MUST have one deterministic writer.  
  * Authorized authoring MUST exercise the writer’s actual write and check entrypoints. Hosted CI MUST exercise the actual check entrypoint against committed bytes.  
  * A failed predicate MUST leave no partial writes.  
  * Write-capable execution MUST require explicit write authorization where applicable.  
  * Every decisive transport predicate MUST have a direct malformed-response test.  
* Enforce manifest-derived release identity and exact-head external attestation when in scope.  
  * `catalog/manifest.json` is the single tracked release-identity input. CI MUST derive and verify the release ID read-only from its canonical bytes.  
  * Release verification MUST NOT require a generated release-ID source constant, regenerated checked-in release derivatives, source-tree execution of an identity-closure writer, or release identity embedded in registry or configuration evidence.  
  * The external attestation MUST be bound to the exact clean source commit under review. Any required producer closure MUST run only in an isolated tracked-file copy outside the source checkout, and the source checkout MUST remain byte-stable.  
  * When packaged-entrypoint verification is part of the release claim, the attestation process MUST build the real wheel, install it in an isolated environment without ambient package inheritance, and exercise the registered `hdctl` console entrypoint rather than a shim or source-tree substitute.  
  * Repeated attestation builds for the same exact source MUST produce the same content tree.  
  * The external artifact is bounded exact-head PR evidence. Its existence does not by implication establish QA PASS, acceptance-token satisfaction, OPS completion, PF09 status movement, or durable final release admission.  
* Verify the complete HDE-EPIC038 release-sanity family when in scope.  
  * The governed release-sanity log at `audit/gates/sanity_pipeline/sanity_pipeline.log` MUST contain exactly one ordered result for each of the nineteen configured stages, followed by `first_failed_stage:NONE` and `summary:PASS`. An omitted, duplicated, reordered, or non-OK stage MUST fail release-sanity validation.  
  * The nineteen-stage log and the exact-head external attestation are distinct evidence surfaces. Neither surface, alone or together, establishes QA PASS, acceptance-token satisfaction, OPS completion, PF09 status movement, release admission, or closeout by implication.  
* Enforce generated development and packaging cleanliness.  
  * Local `.venv` trees and generated `*.egg-info` metadata MUST remain ignored and untracked.  
  * A tracked virtual-environment root or tracked generated package metadata is repository contamination and MUST fail source-inventory or clean-tree validation.

PF19 defines the required sequence at the QA level. PF09 — HDE-Build Checklist, PF12 — HDE-Schemas & Artifacts, and HDE-Mechanics Guide provide the concrete tool names, schemas, artifact ownership, and CI job definitions.

### **2.2.12 Engine serializer/composer determinism**

Prove two-run identity and AB↔BA parity (where defined) for Engine serializer/composer behavior. Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules. Tokens live in PF04/PF09; bytes in PF14/PF12.

### **2.2.13 Secrets & SCA/SAST/DAST**

Run secrets scanning and composition analysis; add SAST/DAST appropriate to the repo. Keep test logs keys-only (no payloads/secrets). Governance lives in PF04; CI wiring in PF09.

### **2.2.14 Reproducibility & flake control**

Fix seeds; avoid uncontrolled wall-clock dependence; pin locale and timezone. Treat flakiness as an unresolved condition. Quarantine MAY be used only as temporary containment under a traceable record that identifies the test, observed failure, responsible owner, tracking item, review or expiry condition, and dequarantine criterion. Preserve every attempt result and classify a fail-then-pass result as flaky, not passed. Quarantine does not satisfy `TESTS_PASS_OK`; if the quarantined test protects an in-scope acceptance predicate, that predicate remains unresolved until the test is deflaked and passes under the governed rails, or the acceptance scope is changed by separate authority.

### **2.2.15 Test data & PII**

* Use synthetic fixtures where possible.  
    
* Redact payloads.  
    
* Enforce keys-only logs in tests (policy PF04).

## **2.3 Rails & environment posture — PO/epic mandated rails**

Every EPIC’s PO specifies what rails posture must be used to accept the epic (open rails vs closed rails). This posture is non-negotiable: it informs which tests must be run and how results are interpreted.

If an EPIC requires open-rails testing (`SAFE_MODE=0`; `ALLOW_NETWORK=1`), then QA MUST confirm those rails are actually in effect for any Live QA run used for acceptance.

If only closed-rails tests are run (`SAFE_MODE=1`; `ALLOW_NETWORK=0`) when open rails are required, then the run cannot be used as open-rails acceptance evidence. The step’s primary log (and any token claims) MUST record this explicitly via its status and a clear reason (in the header or at the top of the log body).

Rails posture must be operator-visible and tool-neutral.

* QA helpers, evidence generators, and review harnesses MUST NOT silently flip rails from closed to open on the operator’s behalf.  
    
* When an acceptance-relevant proof lane requires open rails, the command or step definition MUST require caller-provided `SAFE_MODE=0` and `ALLOW_NETWORK=1`, and MUST fail closed if those rails are absent.  
    
* If the emitted bytes for the proof lane depend on additional environment fields beyond the base rails pins, the step MUST capture and pin those influencing fields or treat the result as nondeterministic and non-claimable.  
    
* This applies to internal/dev writer or readback proof lanes as well as CLI or vendor behavior checks.  
    
* Explicit open-rails writer proof does not widen A7 scope or change the owning surface classification.

Rails evidence (normative) is required: each Live QA step’s primary log MUST include a `captured_env` header field as described in §4.4, capturing at least:

* `SAFE_MODE`  
    
* `ALLOW_NETWORK`  
    
* `APP_ENV`  
    
* `LC_ALL`  
    
* `LANG`  
    
* `TZ`

This is canonical evidence of which rails were actually in effect for that step. It must be present even when Rails posture is “obvious” from context, because reviewers cannot accept implicit environment assumptions.

When mandated rails cannot be met due to environment constraints (for example, `SAFE_MODE` is enforced on CI runners), the QA plan must either (a) route that step to a compatible environment, or (b) mark the affected steps as `TOOLING_BLOCKED` or `FAIL_TOOLING` in their headers with a clear reason (in the header or log body) (see §7.2), referencing the rail mismatch.

# 3\. Post-commit QA (staging/prod)

## **3.1 Intent**

Prove route posture, capture evidence, and update indices in the same PR once changes are deployed to a staging or production-like environment.

Post-commit QA focuses on:

* confirming each surface behaves as promised (status, headers, body)  
    
* capturing stable evidence (snapshots and proof JSON)  
    
* updating both the human index and the machine mirror in the same PR that carries the evidence

Concrete schemas, tokens, and CI wiring live in PF04, PF09, and PF12 (titles-only); PF19 defines the shared checklist.

Workflow placement (Live QA runbooks; normative) is as follows:

* Live QA is a required Close Gate activity when an epic’s acceptance requires it. Live QA runbooks (commands, step-by-step checks, QA\_ROOT structure, behavior-run vs artifact capture/analysis, and step deliverables) MUST be authored as separate QA work products during the Close Gate stage and stored at `docs/qa/<epic-id>-live-qa-plan.md`. The authored runbook is a planning and review work product, not execution evidence or a manifest entry.  
    
* Functional Live QA is mandatory for functional changes: if a change alters runtime behavior (CLI, HTTP surface, vendor ingest, DB mutation or rejection posture), the Close Gate MUST include a runtime functional proof on that surface (or a CI-sourced runtime proof that executes the surface). Artifact-only close without functional proof is non-conforming.  
    
* Epic Plans and implementation plans MUST NOT embed a Live QA runbook. They MUST include only a single statement that Live QA is required for eventual epic close, and may reference the governing documents by title (Epic-Process-Guide; Glow QA Guide).  
    
* Epic Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts. They MAY state QA objectives and closeout proof obligations, but QA planning and QA evidence capture remain separate QA work products owned by Live QA Plans and QA execution artifacts.  
    
* Ops tasks are implementation work, not QA steps. Ops evidence is required and must be tracked and evidenced as implementation work, and it does not substitute for required QA evidence or PASS/FAIL evaluation. Keep categories distinct: implementation work, ops tasks, QA planning, QA execution.  
    
* Reviewers MUST NOT reject or block an Epic Plan solely because it lacks a detailed Live QA runbook, provided the plan clearly marks Live QA as required for close and routes to the governing documents by title.

Post-QA document drainage and closeout ordering (normative) is as follows.

* Required QA completion comes first. All required QA tasks, remediation loops, runtime-functional-proof checks, and close-gate QA reviews MUST be completed before documentation drainage begins.  
    
* PF10 — HDE-Build Notes is the temporary truth home for known but undrained canon, checklist, guide, summary, or other documentation corrections until those items are drained into their canonical homes.  
    
* Undrained documentation deltas MUST NOT, by themselves, block step verdicts, epic QA closeout review, or close posture, provided the governing QA evidence is complete and trustworthy and PF10 records the undrained delta plainly.  
    
* Allowed close blockers remain limited to QA truth and proof failures, such as incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved `FAIL_BEHAVIOR`, `FAIL_TOOLING`, or `TOOLING_BLOCKED` conditions that affect acceptance, or missing required close-gate QA artifacts.  
    
* When a documentation mismatch or canon delta is discovered during QA or closeout, it MUST be recorded as a follow-up, implementation gap, ADR note, or doc-delta item in PF10. It MUST NOT be converted into a pre-drain close blocker solely because the destination PF document has not yet been updated.  
    
* No QA artifact may require its own drainage to be valid. A Live QA plan, review artifact, closeout report, acceptance map, token↔evidence matrix, or step log MAY note later drain targets or required future canon updates, but it MUST NOT require those drains already to be complete in order for the current step verdict, epic readiness judgment, repo-supported completion recommendation, canon-supported recommendation, or closeout recommendation to stand.  
    
* QA plans and other QA artifacts MUST NOT mandate PF document edits as required outputs for QA execution, step completion, or closeout readiness.  
    
* Any QA wording that says or implies `drain required before close`, `cannot pass until PF10 is drained`, `not ready because canon is not yet drained`, `PF update required before acceptance`, or equivalent drain-required posture is non-conforming.  
    
* Post-QA drain ordering is mandatory. Drainage into canon, checklist rows, guides, or other documentation homes occurs only after the epic’s required QA tasks are complete.  
    
* Truthfulness still applies. Closeout records and temporary truth homes MUST state any open documentation deltas, remaining follow-up work, and caveats plainly and explicitly.  
    
* If QA evidence is complete and trustworthy and all required QA tasks are complete, the epic may be recommended as ready for closeout even when undrained documentation deltas remain. Those undrained deltas alone do not justify a not-ready verdict.

## **3.2 Checklist**

Post-commit QA SHOULD include at least:

* Route probes:  
    
  * Confirm the public path and version are correct and stable.  
      
  * Avoid alias drift: probes should target the canonical route, not ad-hoc aliases.  
      
  * For any legacy alias that must exist, prove it resolves consistently without changing contract.


* Header posture:  
    
  * Verify Text vs Suppressed rules for each surface (e.g., Aux text vs Aux suppression, Reader JSON vs error surfaces).  
      
  * Confirm required headers (such as Content-Type, Cache-Control, Vary) match the owning PF doc and surface type.  
      
  * Ensure suppressed responses obey the no-body / no-ETag rules where applicable.  
      
  * Header snapshot normalization: persist lower-case header names in governed snapshots; values remain verbatim.


* ETag strength and quoting:  
    
  * Where ETags are required, prove they are strong, quoted ETags computed from the LF-terminated identity body and stable across repeated GETs.


* HEAD/304 posture (A7 surfaces only):  
    
  * On Catalog JSON success routes, prove HEAD 200 mirrors the identity response (Content-Type parity, effective Content-Length, no body).  
      
  * Prove 304 occurs only after a prior 200 and omits both Content-Type and Content-Length (no body).


* Evidence capture:  
    
  * Capture headers/body snapshots for each relevant route in staging/prod-like environments.  
      
  * When A7 is in scope, capture the composite proof JSON (covering GET/HEAD/304 posture).  
      
  * Update the human Evidence Index and the machine mirror in the same PR that adds or refreshes these captures.


* Mirror gates:  
    
  * Single file: `artifacts/evidence_index.jsonl` only.  
      
  * Canonical JSONL: UTF-8, compact, one LF per record; unknown-key reject; pinned ASCII field order.  
      
  * Path-proofs: each record includes a `proof_anchor` that resolves to a stored, adjacent path-proof; CI fails if any proof is missing or mismatched.  
      
  * Governed roots only: all indexed artifacts must reside under a governed evidence root declared in the Evidence Catalog (HDE Schemas & Artifacts, titles-only); transient/generator paths are forbidden as evidence sources.


* Env-gate proof (A7 scope):  
    
  * For A7-covered routes, capture a headers-only env-gate proof showing that:  
      
    * non-prod entries are unreachable in prod, and  
        
    * each cataloged success route is correctly gated to its intended environment.

    

  * Store the env-gate proof under governed paths and register it in both indices in the same PR.


* Same-PR parity (merge-blocking):  
    
  * `docs/evidence/INDEX.json` plus `docs/evidence/INDEX.sha256` and `artifacts/evidence_index.jsonl` must be updated in the same PR as the captured evidence.

## **3.3 Environment constraints — pre-App, no-user QA mode**

In the current deployment posture, there is no app-level user model integrated with the HD Engine and no persistent user-bound BodyGraph records available for QA in production. Until the Glow App introduces a real user model and a future epic defines user-bound QA surfaces (see HDE Phased Epics), QA must follow a no-user QA mode for Engine and CLI Live QA.

Reality (pre-App) is as follows:

* No app-level user IDs exist for the Engine to reference in prod.  
    
* There are no persistent BodyGraphs keyed to app users that QA may rely on as fixtures.  
    
* QA must not create app-like user records in prod ahead of Glow App integration.

Effect on QA requirements is as follows:

* Any QA requirement that assumes “existing users in prod” (for example, `showcompat --user-a/--user-b --source=db` or `bg:resolve` against real app user IDs) is treated as blocked by environment, not as failed acceptance.  
    
* Those requirements must be explicitly called out in epic-level QA plans and deferred to a future epic once the app user model exists in HDE Phased Epics (titles-only).  
    
* QA must not work around this by synthesizing “fake app users” in prod; doing so is considered a violation of this guide.  
    
* In this pre-App, no-user environment, there is no canonical DB-backed compat source for live behavior tests. The only reliable, canonical source of live compat and BodyGraph behavior is the vendor.  
    
* Engine “DB/auto” compat paths and CLI defaults that rely on a non-existent user model are not valid for Live QA behavior acceptance in this environment.  
    
* CLI runs that do not call vendor (for example, pure serializer/math checks under closed rails) are allowed only as local/offline checks. They may satisfy determinism or canonicalization tokens, but they do not satisfy any token whose intent is “live product behavior with vendor rails active” and must be labeled accordingly in QA plans.

Interim no-user QA mode (pattern) is as follows:

* Until the app user model is live, use the following pattern for Engine and CLI QA in staging or production-like environments.  
    
* Compat and Reader use births only (vendor-backed behavior vs offline):  
    
  * For live behavior tests in this environment (including PO Live QA and any D-goals that assert “live compat behavior in prod”), use `hdctl showcompat` with:  
      
    * birth arguments only (birthdate/time/location flags as defined in CLI/API docs; titles-only), and  
        
    * an explicit vendor source flag, for example `showcompat --source=vendor` (exact flag spelling pinned in HDE-CLI-API-Vendor-Ref).

    

  * These runs are the only compat runs that count as “live behavior tests” in the pre-App environment.  
      
  * A functional `showcompat` run requires explicit input tuples and an explicit vendor source; a “zero-arg showcompat” invocation is always a usage error and is not acceptable as functional proof.  
      
  * Until local BodyGraph storage exists, vendor-backed `showcompat` Live QA MUST run with vendor rails open (typically `ALLOW_NETWORK=1` and `SAFE_MODE=0`). If rails are closed and vendor cannot be reached, classify as `TOOLING_BLOCKED` (or equivalent rail/tooling failure), not as a behavior failure.  
      
  * `showcompat` runs that do not call vendor (for example, no `--source` flag and rails closed, or a purely local serializer path) are treated as local/offline math and serializer checks:  
      
    * they may be used to prove canonical JSON, determinism, or AB↔BA identity, and  
        
    * they must be explicitly labeled “local/offline (no vendor)” in QA plans and artifacts, and must not be used to satisfy tokens that assert live behavior.

    

  * No-user compatibility remediation claims must keep these proof classes separate:  
      
    * public numeric-free output proof  
    * internal or admin compatibility compute proof  
    * vendor-backed no-user behavior proof

    

  * Local pytest, grep, serializer, canonicalization, or internal-compute checks may prove their own offline or internal claims when labeled as such, but they must not be used as substitutes for vendor-backed no-user behavior proof. Fixture-only `person_uid` injection is not sufficient remediation for a no-user behavior claim.  
      
  * For a controlled vendor-backed no-user smoke, birth-only caller and command proof means the external command and caller-facing evidence use explicit vendor source posture and birthdate, birthtime, and location inputs only. The command MUST NOT require app user IDs, caller-provided `user_id`, caller-provided `person_uid`, DB-backed user BodyGraphs as caller input, `--source db`, or inline secret values.  
      
  * Boundary-generated deterministic internal metadata is allowed only when the implementation creates or consumes it inside the resolver boundary from birth-only input. It MUST NOT become caller input, public contract input, or proof that caller-provided user identity is acceptable.  
      
  * A controlled vendor-backed no-user smoke is implementation validation only. It is not a QA rerun, not a Live QA plan, not a closure decision, not a PF09 or PF09.2 status change, and not a substitute for final QA. It may run only after command discovery and remediation establish the exact executable command, birth-only input shape, safe secret posture, explicit vendor source posture, required target facts, accepted local implementation proof, and PO authorization.  
      
  * Controlled vendor-backed no-user smoke execution is PO-only and IA-guided. It must use explicit open rails only for the vendor step, capture determinism pins, store no secret values, capture only presence-safe secret posture, and avoid guessed commands, hosts, ports, URLs, service bindings, targets, credentials, birth values, or environment facts.  
      
  * Controlled vendor-backed no-user smoke preflight MUST prove the exact executable command, birth-only input values, absence of user-identity inputs, absence of inline secrets, explicit vendor source, open rails for the vendor step only, determinism pins, required vendor environment presence as booleans, safe secret posture, accepted local implementation proof, and PO proceed authorization. Missing or unproven prerequisite evidence is `TOOLING_BLOCKED`; user-identity input or secret persistence is `FAIL_TOOLING` before behavior is evaluated.  
      
  * Controlled vendor-backed no-user smoke evidence MUST include the executed command, substituted birth-input record, redacted environment-presence record, request summary, stdout capture, stderr capture, exit-code capture, result summary with one explicit classification, prerequisite matrix, and checksum ledger. These are OPS evidence unless the governing QA plan separately defines how they feed QA evidence.  
      
  * Use `PASS` only when all preflight rows pass, the exact command runs, exit code is zero, the command uses explicit vendor source and birth-only flags, no user identity or secret value is supplied or persisted, stdout is non-empty and parseable as the expected success output, and the result summary preserves the non-claims above.  
      
  * Use `FAIL_BEHAVIOR` only when all prerequisites are proven, the command runs, no tooling or secret failure occurs, and observed runtime behavior shows that vendor-backed compatibility cannot be computed from the birth-only no-user command.  
      
  * Use `FAIL_TOOLING` when execution or evidence is contaminated or invalid as a tool run, including secret persistence, user-identity input, evidence files missing after an attempted run, or command changes by guesswork after failure. Secret-bearing artifacts must be quarantined and excluded from proof.  
      
  * Use `TOOLING_BLOCKED` when the smoke cannot safely run, including unresolved or placeholder-bearing command, missing or incomplete birth inputs, uncaptured or false required vendor environment presence, unavailable command target, absent PO authorization, missing or contradicted local implementation proof, or a changed HTTP-service target without the required infrastructure-backed target facts.  
      
  * OPS or vendor-backed steps must not be delegated to Codex-style tooling or automated agents, and no command may be modified by guesswork to force a PASS. Documentation drainage may record or later route the posture, but it is not a substitute for PR work, OPS execution, QA execution, or closure evidence.  
      
  * In all cases, do not use `--user-a/--user-b` or `--source=db` in prod QA, because there are no app users or DB-backed BodyGraphs to rely on.  
      
  * For vendor-backed compat Live QA runs, verify at minimum:  
      
    * canonical JSON output on stdout,  
        
    * AB↔BA identity by swapping the birth tuples (where required by the epic), and  
        
    * Reader v1 envelopes via `--dump-reader` (shape and band-only posture per HDE-Math-Spec and HDE-CLI-API-Vendor-Ref; titles-only).


* Aux narratives come from compat JSON (no DB users):  
    
  * Use `hdctl aux-preview --pair-file <compat.json>` (or equivalent API) based on birth-generated compat JSON from a vendor-backed compat run when testing behavior; in other cases, Aux QA may use compat JSON produced by offline checks as long as those runs are labeled “local/offline”.  
      
  * Do not rely on DB users or user-bound records for Aux tests; treat compat JSON as the source of truth for Aux QA.


* BodyGraph resolver and vendor ingest use ephemeral QA keys and vendor-backed behavior:  
    
  * Treat any `--user` value used in `bg:resolve` during QA as an ephemeral QA key, not as a real app user ID. Keys should be clearly marked as QA (for example `qa_epic017_resolve1`, `qa_epic017_vendor1`).  
      
  * In prod pre-App:  
      
    * For vendor-backed behavior tests:  
        
      * use explicit vendor-backed modes such as `bg:resolve --source=vendor` in dry-run or other controlled modes (exact flags and modes pinned in HDE-CLI-API-Vendor-Ref and HDE-Build Checklist),  
          
      * ensure rails are open per Governance and infra canon for any step that intends to exercise live vendor behavior, and  
          
      * store resolver and ingest metadata artifacts under the responsible vendor-behavior check at `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>`, with clear naming that indicates “vendor-backed behavior”. The approved Live QA plan MUST resolve `<check_id>` and `<explicit_filename>` to concrete values.

      

    * For offline/local checks of resolver or ingest:  
        
      * `bg:resolve` DB/auto stub behavior may be used only as a local/offline check (for example to smoke-test CLI wiring) and must be labeled as such; it does not satisfy live vendor behavior tokens in the pre-App environment.  
          
      * `bg:resolve --source=vendor` under closed rails is expected to yield a typed refusal before outbound I/O and may be used to prove refusal behavior and SAFE rails, but not live vendor behavior.  
          
      * `bg:resolve --source=vendor --dry-run` under open rails may be used only for the exact BodyGraph resolver or ingest-path behavior it actually exercises. In the current configured-v2 HDAPI posture, dry-run resolver behavior may use the version-neutral `charts` resource, route-metadata auth posture, deterministic v2 ChartResult adapter, redacted request posture, mapped-no-raw-vendor-payload cache posture, and compatibility-path proof when those artifacts are present. This is a bounded dry-run runtime proof, not public Reader expansion, production deployment, broad HumanDesignAPI v2 platform conformance, app-side vendor ownership, raw payload persistence, PF09 status movement, or closeout.  
          
      * `bg:resolve --source=vendor --dry-run` with a non-v2 configured base may preserve explicit legacy BodyGraph fallback when the owning PF homes and repo evidence support that posture. QA must keep configured-v2 chart-backed dry-run behavior and non-v2 legacy fallback behavior separate.  
          
      * `bg:resolve --source=vendor --upsert` and other non-dry-run v2 chart-backed writes remain forbidden until a future epic explicitly implements and proves safe mapped-cache persistence, DB read-back parity, idempotence, no raw vendor payload persistence, environment discipline, rollback posture, and any required production or production-like authorization.


* Live QA Guides and QA Plans that target live compat and BodyGraph behavior in this environment must adopt this pattern: any step that claims to be a live behavior test for compat or BodyGraph must call vendor explicitly, and any step that does not call vendor must be labeled clearly as local/offline and not used for behavior acceptance.

## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**

This section describes a manual Live QA execution pattern that is generalized across epics. It is designed to produce mechanical, reviewable evidence under the epic QA root without introducing hidden dependencies, git gates, or non-canonical runners.

### **3.4.1 Execution pattern: one command → one primary artifact**

This rule produces repeatable close-pack evidence and prevents wandering QA that cannot be audited.

Each manual Live QA check MUST be expressible as:

* Intent  
    
* Discovery step, only if needed  
    
* Minimal test step  
    
* Required evidence  
    
* PASS criteria  
    
* FAIL criteria  
    
* BLOCKED criteria when discovery cannot proceed without guessing

Repo-resident loci are planning-time claims, not things to be filled in later. The only allowed provenance sources for repo-reality claims in Live QA planning are:

* PF10 — HDE Build Notes  
    
* PF-Canon, including Reality Audits  
    
* the initial QA Audit for the epic

Repo-resident loci include file paths, directory paths, endpoint routes, module or component identifiers, script names, runbook names, command strings, check or test identifiers, CI job names, environment variable names when treated as already existing, fixed output locations when treated as already existing, and negative existence claims.

No invention, no inference, no memory. If the exact locus string does not appear verbatim in an allowed provenance source, the plan MUST NOT present it as a repo-resident fact. Unknown loci MUST be handled by discovery during the run, not by guessing.

Each check MUST identify:

* the primary artifact path to be produced  
    
* the evidence that proves the step  
    
* the PASS, FAIL, and BLOCKED outcomes

The exact command or commands actually used MUST be recorded in step evidence at runtime. A plan MAY describe the goal and required outputs without freezing syntax-perfect commands, unless an exact command string is itself proven by allowed provenance.

### **3.4.2 Tooling discipline (normative; no hidden dependencies)**

Live QA plans MUST NOT depend on helper or wrapper scripts unless the plan includes a preflight existence check showing the tool exists at the referenced path in the current workspace.

A locus is invented if the plan or runbook treats it as executable or authoritative without verbatim proof from an allowed provenance source or without a discovery step that records the resolved locus for the current run.

Plan-created artifacts are allowed and expected. If a plan requires creating any file, it MUST include all of the following:

* the exact repo-relative path and filename to be created  
    
* runnable creation instructions  
    
* one sentence explaining why the file is required  
    
* enough detail to reproduce the file deterministically when it is evidence-bearing

Plan-created scripts are permitted only when a required deliverable cannot be produced without one. A plan-created script MUST be minimal, purpose-bound to the deliverable, and treated as a plan-created output, not as a repo-resident helper.

Live QA plans MUST NOT invent or assume helper scripts already exist. They MUST NOT create new repo-resident scripts, modules, checks, or test files and then treat those loci as if they were pre-existing.

If required tooling is missing, or discovery cannot resolve the correct locus without guessing, the step is TOOLING\_BLOCKED. The plan MUST be revised, or the missing tooling shipped, before QA can proceed.

Preflight check requirements (minimum):

* `ls` or equivalent of each referenced existing tool path  
    
* `--help` or equivalent for each referenced existing entrypoint, when safe  
    
* explicit capture of the preflight output in the check evidence directory

Helper and check-registration preflight requirements apply when a Live QA Plan uses a repo-provided harness, dispatcher, helper, or wrapper that executes checks by `check_id`, step name, subcommand, or selector.

Minimum proof requirements are:

* prove the helper or harness exists at the referenced path in the current workspace;  
* prove the helper or harness recognizes each planned check ID, step name, subcommand, or selector before behavior validation begins;  
* capture the registration or listing output in the relevant check evidence directory, or in a D0/preflight artifact that the check evidence references;  
* if registration cannot be proven without running the check, record the first safe invocation result and classify unknown check or unknown selector failures as tooling or plan-validity failures, not product behavior failures.

A missing helper registration is `TOOLING_BLOCKED` or a plan-validity defect until corrected. If a bounded Moon Loop correction adds or repairs registration for an already-approved check, the final evidence must record the deviation, the corrected registration or invocation proof, the rerun result, and the fact that the correction did not change the proof target, rails posture, evidence identity, acceptance posture, public/private boundary, no-secret posture, or scope.

Approval blocking posture. Any plan that includes invented or speculative repo-resident loci, invented scripts, or required plan-created files without exact path, creation instructions, and stated reason is invalid for approval and MUST be returned for revision.

This rule does not forbid canon tooling already in-repo or minimal plan-created outputs. It forbids invented repo-resident helpers, unproven helper paths, speculative loci, and non-existent entrypoints.

### **3.4.3 Evidence layout: current-state first (new posture)**

Run-id discipline is not a correctness mechanism. The canonical evidence posture is current-state under the epic QA root:

* `audit/qa/<epic-id>/`

Each check’s canonical primary evidence is a single primary log or artifact referenced by the epic-level step-log manifest:

* `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
    
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` (required whenever the step-log manifest is created, refreshed, or governed)  
    
* `audit/qa/<epic-id>/checks/<check_id>/primary.log` (one canonical primary log per `check_id`; referenced by the manifest)

KISS evidence posture (normative). Live QA plans MUST minimize required outputs to the per-check primary log and the step-log manifest. Nothing else is auto-required unless canon explicitly pins a governed evidence family or path. Any additional required artifact must be explicitly justified as acceptance-decisive and canonized as a governed evidence family or path.

Per-run nesting is disallowed. Live QA plans, QA prompts, and QA reviews MUST NOT introduce, require, or depend on run-id directories, timestamped run directories, fresh run roots, or operator-set per-run root variables.

Checks-only evidence layout is mandatory. Re-running QA MUST update the stable check directory for the relevant `check_id`, not create a new run root.

Plan-created deliverables are allowed, but they MUST live under the stable check directory for the step that creates them and MUST be named explicitly in the plan.

#### **QA evidence and work-product path grammar (normative)**

The controlling root is `EPIC_QA_ROOT = audit/qa/<epic-id>/`. For HDE, `<epic-id>` is the canon-defined lower-case epic identifier. The metavariables below express PF grammar only; every executable plan MUST resolve each applicable `<epic-id>`, `<check_id>`, slug, and filename to a concrete value before approval.

| Artifact or work-product class | Approved destination | Binding rule |
| :---- | :---- | :---- |
| Authored Live QA plan or runbook | `docs/qa/<epic-id>-live-qa-plan.md` | One stable version-controlled work product. It is not execution evidence, a manifest entry, or proof that QA ran. Existing historical plan files are not moved automatically. |
| Epic current-state manifest | `audit/qa/<epic-id>/qa_step_logs_manifest.json` | One stable root manifest and the authoritative current-state index by `check_id`. |
| Manifest path proof | `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` | Generate or refresh it whenever the manifest is created, refreshed, or governed. |
| Optional step-0 manifest copy | `audit/qa/<epic-id>/checks/po-000/qa_step_logs_manifest.json` | Allowed only when an approved plan explicitly requires this PF12-defined copy. It does not create a second general grammar. |
| Decisive receipt for an evidence-producing check | `audit/qa/<epic-id>/checks/<check_id>/primary.log` | Exactly one current-state primary log per evidence-producing check. The directory value equals the manifest `check_id`. |
| Primary-log path proof | `audit/qa/<epic-id>/checks/<check_id>/primary.log.path_proof.txt` | Required whenever the primary log is governed evidence. |
| Required check-created output other than `primary.log` | `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>` | The approved plan names the concrete filename, creation method, purpose, and PASS and FAIL predicates. The primary log references the output. |
| Auxiliary check output | Prefer `audit/qa/<epic-id>/checks/<check_id>/tmp_<explicit_filename>` | Auxiliary output never replaces `primary.log`. Optional material under `results/` is not required or decisive unless an owning canon expressly promotes it. |
| Stable epic-level mechanical metadata | `audit/qa/<epic-id>/00_meta/<canon_defined_filename>` | Use only for an exact owning-canon metadata path. It is not a catch-all or a substitute for check evidence. |
| Remediation staging | `audit/qa/<epic-id>/remediation/<lowercase_slug>/` | Staging only. It is excluded from the Human Evidence Index and Machine Mirror unless an owning canon expressly governs a concrete file. A decisive remediation receipt remains in the responsible check's `primary.log`. |
| Existing evidence family outside the epic QA root | Its existing PF12-cataloged or audit-proven owning path | Reference it from the check receipt. Do not copy, rename, or re-home it for visual uniformity. |
| New recurring evidence family | No destination until introduced by PF10 or the owning PF canon | H1 3 and a derived plan MUST NOT create a recurring family by example, convenience, or repository guesswork. |

Every new or refreshed current-state manifest entry MUST contain at least `check_id`, `status`, and `log_path`. Its `log_path` value MUST be the full repository-relative path `audit/qa/<epic-id>/checks/<check_id>/primary.log`; a new or refreshed entry MUST NOT use a root-relative value such as `checks/<check_id>/primary.log`. This rule does not select a new JSON envelope. Existing top-level maps, nested maps, and arrays are historical coexistence, not authority for envelope normalization.

`check_id` values and directory segments MUST use lower-case ASCII. New plan-owned slugs use hyphens by default; an underscore is permitted only to retain an exact existing canon slug. Uppercase task labels may remain in filenames or prose, not directory segments. H1 3 does not mint a universal check identifier: the approved plan owns and resolves each concrete `check_id`.

The generic current-state structural families `logs/`, `vendor/`, `d3-cli-guards/`, and `d0-planning/` are retired for new or refreshed H1 3 evidence. A handshake, HTTP capture, command transcript, vendor capture, guard receipt, D0 result, warning stream, exit code, and mechanically generated note belongs to the check that produced or judged it. A shared root-level `logs/qa_notes.md` MUST NOT be used for new or refreshed evidence.

#### **Migration and historical treatment (normative)**

New Live QA plans, H1 3 examples, and refreshed current-state evidence use the approved grammar immediately.

Migrate existing evidence only when an epic remains active, its evidence is being refreshed, or the evidence must become current for a new acceptance decision. The authorized migration sequence is:

1. Inventory every source path, consumer, manifest pointer, index row, mirror row, path proof, checksum, close-pack pointer, and historical reference.  
2. Classify each source as a primary receipt, required check output, auxiliary output, external governed family, non-evidence work product, remediation staging, or historical record.  
3. Reuse the approved plan's existing `check_id`. If none exists, the plan owner defines it before migration; do not infer it from a directory name.  
4. Create the stable check directory mechanically.  
5. Preserve the original transcript and verdict. If a primary log must be assembled, generate the required single JSON header and retain the original body bytes verbatim wherever possible.  
6. Copy or move required check-created outputs into the check directory and record source and destination SHA-256 values. Path migration alone MUST NOT change behavior, status, token claims, or Human Design results.  
7. Update the root manifest with the full repository-relative primary-log path and truthful current status.  
8. Regenerate the manifest path proof and every affected governed path proof, checksum, Human Evidence Index entry, and Machine Mirror row in the same authorized change when those artifacts are in scope.  
9. Keep the old location as historical until every consumer and retention obligation is resolved. It MUST NOT remain a second current-state authority.  
10. Do not use symlinks, duplicate manifest bindings, or a latest pointer to create two current homes.  
11. Remove an old path only through a separate, explicit, preservation-complete change. This rule does not authorize destructive evidence deletion.

Do not rewrite closed historical evidence only to make old trees look current. Existing bytes retain their historical meaning and version context. Old manifest envelopes and root-relative `log_path` values may remain in immutable closed evidence, but MUST NOT be copied as templates for new or refreshed runs. If a closed epic is formally reopened and its QA results become current again, migrate the affected current-state surfaces under the sequence above while preserving original receipts and prior statuses.

#### **Approved exceptions and external evidence families (normative)**

The approved exceptions are limited to:

1. the root manifest and its sibling path proof;  
2. the exact PF12-defined optional `po-000` manifest copy;  
3. exact owner-defined epic metadata under `00_meta/`;  
4. optional auxiliary files under `results/` when they do not substitute for required check evidence;  
5. exact owner-defined closeout surfaces;  
6. remediation staging that is expressly non-binding unless separately promoted;  
7. exact PF12-cataloged or audit-proven evidence families in their existing owning homes; and  
8. immutable historical paths retained for provenance and retention.

There is no wildcard exception. Repository coexistence, convenience, a prior example, or an equivalent-subtree phrase does not create one. A check may reference an already governed family such as `docs/evidence/**`, `artifacts/evidence_index.jsonl`, `artifacts/vendor/**`, `audit/gates/**`, or a PF12-cataloged close-pack artifact without re-homing it. Conflicting legacy path examples in other PF text are documentation drift and do not override PF12.

Arrays-as-sets check (current-state; canonized runner \+ report surface). When Live QA includes an arrays-as-sets check, the canonical runner and report artifact are:

* Runner (executed command): `python -m pytest tests/compare/test_arrays_as_sets.py`  
    
* Report artifact (log format): `artifacts/canonical/arrays_as_sets_report.log`

Plan drift note. Some plans may name `python tools/evidence/run_arrays_as_sets_check.py` and `audit/gates/arrays_as_sets/arrays_as_sets_report.md`. Those were not used in the observed execution captured in evidence; treat them as plan drift and correct to the canonical runner and report artifact before running QA.

### **3.4.4 Primary artifact discipline (what counts as evidence)**

The primary artifact for a check is mechanically generated by the command, and its presence/contents determine PASS/FAIL for that check.

Any supplemental artifacts (stdout/stderr captures, helper JSON, diffs, secondary logs) are additive but do not replace the primary artifact.

Evidence must be deterministic and stable. Unstable output (nondeterministic ordering, timestamps, random salts) is a bug in the step/toolchain, not a reason to weaken QA rails.

Canonicalization is required for governed bytes (hash inputs, snapshot payloads, indexed artifacts). Canonicalization must be mechanical and described in the check.

Generated proof artifacts used to support PASS are primary-artifact evidence for the claimed proof family. A generated proof artifact MUST derive any top-level PASS posture from explicit decisive predicate checks for that family. If a decisive predicate is missing, stale, contradicted, not evaluated, or not bound to the final governed artifact bytes, the generated proof artifact MUST NOT report PASS. It MUST classify the outcome by failure class as `FAIL_TOOLING`, `TOOLING_BLOCKED`, or `FAIL_BEHAVIOR`, and the QA verdict MUST follow that classification.

Generated proof artifacts that classify outside-family governed evidence refreshes MUST fail closed on the classified evidence family. If the proof family claims that a side-effect refresh is expected updater convergence, required dependency refresh, or unexpected drift, the generated proof artifact MUST validate the side-effect paths, proof companions, affected Machine Mirror artifact keys, discovered paths, proof anchors, `sha256`, and `size_bytes` needed for that claim. Check mode MUST validate the final governed bytes and final Machine Mirror bindings, even when non-check generation must avoid write-time self-hash recursion. Missing paths, invalid proof companions, stale mirror rows, or unvalidated side-effect classifications MUST NOT produce PASS.

### **3.4.5 Command transcript requirements (mechanical; no screen-only acceptance)**

Each check MUST capture a command transcript at minimum:

* the command line invoked  
    
* the exit code  
    
* stdout/stderr (or references to captured files)

Each check’s decisive transcript MUST be stored in `audit/qa/<epic-id>/checks/<check_id>/primary.log`. Any separate stdout or stderr capture MUST use an explicit filename in the same `checks/<check_id>/` directory and be referenced by that primary log.

For commands that may be noisy or long-running, tee stdout/stderr to a log file under the epic QA root (example pattern: `audit/qa/<epic-id>/checks/<check_id>/stdout.log`), but keep the primary artifact definition unchanged.

### **3.4.6 Step-level Deliverables (no screen-only acceptance)**

For any QA guide, runbook, or PF10 QA addendum that defines stepwise QA execution, each check MUST include a Deliverables subsection naming the minimal evidence set created or updated by that check.

Requirements (normative):

* Fully-qualified paths: every deliverable MUST be listed with a repo-relative, fully-qualified path (for example `audit/qa/hde-epic021/checks/d3_internal_version/primary.log`).  
    
* Presence rules: a deliverable is either required to exist, required to be absent, or required to have a specific content signature. Vague phrasing ("should", "nice-to-have") is forbidden.  
    
* Primary artifact discipline: each step MUST define exactly one primary artifact (the canonical evidence surface) and may optionally define supporting artifacts.  
    
* No screen-only acceptance: screenshots are allowed as supporting evidence, but MUST NOT be the sole basis for PASS/FAIL.

### **3.4.7 Command formatting (copy/paste-ready)**

Live QA Plans are objective-first: each step MUST state the directive, proof target, success criteria, evidence family, output artifact identity, rails posture, safety posture, and PASS, FAIL, or TOOLING meaning. Plans MUST NOT be required to provide verbatim, syntax-perfect command lines for every step.

Commands and helper snippets in plans are intent carriers unless the plan explicitly states that exact command bytes are the proof target. A reviewer MUST NOT block plan approval solely because a command line, helper snippet, heredoc, shell fragment, Python fragment, indentation block, markdown rendering, escaped character, or copied chat text is not byte-perfect, paste-ready, or directly executable as written.

Correctable syntax is handled as in-flight execution normalization when proof identity is unchanged. The exact command actually executed, its exit code, and its captured output belong in governed execution evidence.

The causal source controls classification. A syntax-origin defect remains non-blocking even when the literal text fails to parse or execute, appears to change command identity, invokes an incorrect apparent form, or cannot reach the intended behavior. If faithful syntax normalization reveals an independently proven non-syntax defect affecting the proof target, evidence family, artifact identity, verdict meaning, rails posture, safety posture, source authority, PF09 scope, public/private boundary, route family, endpoint family, repo locus, or acceptance posture, evaluate only that separate defect. The syntax-origin defect itself MUST NOT be classified as `TOOLING_BLOCKED` or approval-blocking.

Fenced code blocks are OPTIONAL and MUST NOT be treated as an approval gate.

If the plan may be consumed in a plain-text venue (or rendering is unknown), avoid markup that breaks copy/paste (for example, do not wrap every line in backticks).

If a plan includes a runnable command line, it MUST avoid placeholders like `<PLACEHOLDER>`. If a path varies, provide the exact expected path shape and at least one fully-qualified concrete example.

If a command is destructive (writes to governed artifacts), include an explicit “STOP if output contains \<INVALIDATION\_SIGNATURE\>” line before it, describing what would invalidate the step.

### **3.4.8 Rails posture for manual Live QA (EPIC017 example; generalized rule)**

Manual Live QA steps that touch production endpoints run with open rails as required by the command (for example `ALLOW_NETWORK=1`, `SAFE_MODE=0`).

Manual Live QA MUST NOT modify code or configuration except for minimal, in-session remediation under the Moon Loop policy below. Plan-created evidence outputs MUST be written under the responsible `audit/qa/<epic-id>/checks/<check_id>/` directory; separately governed evidence families remain in their owning paths.

Moon Loop (allowed; minimal in-session remediation to unblock QA). Live QA may include a small remediation loop when a check fails due to an execution-blocking mismatch, only to the extent required to produce a PASS-grade proof for the already-approved scope. The only goal is to unblock the existing QA check and prove the existing implementation works.

Entrypoint existence preflight (normative; plan-validity blocker). Before executing any QA Plan step that references a repo-provided harness or entrypoint, the plan MUST preflight that the referenced entrypoint exists and is runnable in the stated environment.

* Existence: the referenced path exists in the repo workspace at plan time.  
    
* Runnability: the plan specifies a runnable invocation mode for that environment (executable bit for scripts, or an explicit interpreter invocation such as `python -m <module>` or `python <script.py>`).

If either check fails, treat it as a plan validity blocker. Do not classify it as a runtime behavior failure. Stop and repair the plan and/or environment wiring before continuing Live QA.

Hard boundary: no scope expansion. In-session remediation MUST NOT:

* add new features or acceptance criteria  
    
* change public contracts  
    
* mint new tokens  
    
* introduce new evidence families  
    
* turn QA into a second remediation plan

Allowed remediation actions (minimum set):

* create small helper scripts under `/tmp` for parsing or glue (strictly ephemeral; never treated as evidence)  
* create or correct QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly files under the approved QA root when the defect is in those QA-created surfaces  
* adjust the QA check procedure to use the canonical emitted surfaces (paths and shapes) already required by canon and implementation  
* re-run the affected check(s) and capture the PASS-grade evidence artifacts

Non-QA-root remediation boundary. A change to product code, repo tests, repo evidence generators, governed artifacts outside the approved QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction. Non-QA-root remediation MUST be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before it can be treated as the basis for a final PASS-grade QA run.

When a final Live QA PASS receipt relies on refreshed governed evidence outside the approved QA root, the receipt MUST cite the approved routing receipt or work item that made the refresh valid for QA use. Valid routing classes include `QA_PLAN_UPDATE`, PR, OPS, and DOC\_UPDATE. The final PASS receipt MUST preserve the failed or blocked pre-routing receipt as context and must not relabel the non-QA-root refresh as a bounded Moon Loop correction.

Examples (informative; Moon Loop plan vs repo drift patterns):

* Runner naming drift (run\_ vs generate\_). If an Approved Plan references a runner named `run_<name>.py` under `audit/qa/<epic-id>/checks/<check_id>/`, but the repo provides `generate_<name>.py` (or equivalent), the operator MAY run the repo runner that exists, provided it produces the plan-required governed outputs at the plan-required paths and does not introduce new output filenames. The operator MUST record the runner-path mismatch as a Plan-vs-Repo mismatch (Moon Loop), not as a behavior failure.  
    
* Embedded harness runner and missing auxiliary log. If an Approved Plan references a standalone runner file (for example `tests/audit/run_harness_selftest.py`) and expects a separate auxiliary log artifact, but the harness runner is embedded elsewhere and the auxiliary log is not produced, the step MAY still PASS if PASS-grade primary evidence exists (token/evidence matrix binding plus the primary check output) and the primary output contains a PASS result with concrete evidence pointers. The operator MUST record the missing runner path and missing auxiliary log as a tooling expectation drift and proceed only if the canonical primary evidence surfaces are complete.  
    
* Sanity pipeline evidence surface drift (D07\_sanity\_pipeline). A Live QA primary log under `audit/qa/<epic-id>/checks/D07_sanity_pipeline/primary.log` is valid as a Plan Templates step log, but it does not satisfy `SANITY_PIPELINE_OK`. For the current HDE-EPIC038 release-sanity family, the governed token-evidence surface is `audit/gates/sanity_pipeline/sanity_pipeline.log` together with `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`, indexed in the Human Evidence Index and Machine Mirror. The governed log MUST contain exactly one ordered result for stages 01 through 19 and end with `first_failed_stage:NONE` and `summary:PASS`. Live QA plans MUST NOT treat `audit/qa/` execution logs and the governed release-sanity surface as interchangeable. If both are referenced, label the `audit/qa/` log as execution evidence and the governed release-sanity log as the token-evidence surface. Codespaces prerequisite: if the sanity runner is invoked from Codespaces, `pytest` must be available in that environment; missing `pytest` is a Step-0 Doc Delta blocker.

Evidence posture for in-session remediation. If remediation occurs inside a QA session, the existing primary evidence artifacts MUST make it auditable without additional documents:

* The failing check’s primary log MUST include the failure signature (short excerpt).  
    
* The same log (or the session transcript) MUST include a one-line remediation note that names exactly what changed (file paths) and why.  
    
* The rerun output showing PASS MUST be captured in the same evidence stream.

If any repo files were changed, the responsible remediation check’s `primary.log` and explicit check-scoped sidecars MUST record the changed paths, why they changed, and required hashes. Optional non-binding staging copies MAY also use these lower-case examples:

* `audit/qa/<epic-id>/remediation/moon_loop/patch.diff` (staging example)  
    
* `audit/qa/<epic-id>/remediation/moon_loop/changed_files.txt` (staging example; paths plus sha256)

The primary log MUST identify any staging copy. Staging does not replace the decisive check receipt and is excluded from acceptance unless an owning evidence catalog expressly promotes the concrete file. This delta capture must not discuss branches, commits, or PR workflow.

Stop condition. If the remediation required is not “minimal” (multiple files, unclear root cause, or changes beyond the failing surface), stop the Moon Loop and escalate to a normal remediation plan.

PO-approved Extended Moon Loop remediation (normative).

An ordinary Moon Loop still stops at the boundary above. After that stop, a separately authorized Extended Moon Loop MAY continue the same remediation lineage only after fresh, explicit Product Owner direction has been recorded before the corresponding action class is first used.

A PO-approved Extended Moon Loop is an event-bound, repository-anchored, routed continuation of one identified QA or hosted-CI failure, blocker, or evidenced safety defect. It does not relabel non-QA-root remediation as ordinary Moon Loop correction.

Functional drift means a material difference between the approved proof objective and the integrated plan, bootstrap, implementation, evidence generator, governed companion graph, or CI behavior encountered during execution. Causal uncertainty means uncertainty that could not be resolved reliably during plan review and becomes observable only while executing the approved proof or its required integration gates.

The authorization MUST identify or make unambiguous:

* the epic and QA check or hosted-CI run;  
* the repository or routed-source anchor;  
* the triggering failure, blocker, or safety discovery;  
* the unchanged proof objective and PASS or FAIL meaning;  
* the permitted causal scope;  
* the rails, network, credential, and data-safety posture;  
* whether investigation, code write, external call, PR publication, merge, OPS, deployment, or rerun is authorized;  
* the completion gate; and  
* each one-time authority that expires separately.

Approval of investigation or one action class does not imply any omitted action class. A later record may bind authority that was granted before an action; it cannot create authority retroactively.

The Extended Moon Loop may correct a separately evidenced root cause, together with the minimum regression tests and canonical companion refreshes required to prevent recurrence, only when all of the following are true:

1. The defect is produced by, blocks, or invalidates the original correction or a required downstream gate.  
2. Its relationship to the original proof chain is recorded.  
3. Correcting it does not change the proof objective, acceptance surface, public contract, endpoint family, evidence family, or substantive epic scope.  
4. The correction is routed according to the kind of file or system changed.

An independent or opportunistic defect requires separate Product Owner disposition. A new remediation plan is not required while causal closure, proof identity, acceptance meaning, and scope remain stable. Replanning is required when the desired proof, product behavior, acceptance criteria, public boundary, endpoint family, evidence family, or substantive epic scope changes.

Code, repository tests, evidence generators, and governed artifacts outside the QA root remain routed remediation. They MUST be carried through the applicable PR, OPS, `QA_PLAN_UPDATE`, or `DOC_UPDATE` posture before they can support the affected check’s final PASS.

The execution record MUST preserve:

* the original failed, blocked, or pre-routing receipt;  
* each material root-cause finding;  
* the exact changed paths or reviewable diff;  
* canonical generator commands for governed outputs;  
* local regression results;  
* PR, routing, and merge receipts;  
* intermediate hosted-CI failures;  
* the final accepted QA receipt; and  
* the final clean hosted-CI source and run when CI cleanliness is a completion condition.

An Extended Moon Loop does not by itself authorize another vendor, database, deployment, migration, service-start, OPS, publication, merge, or external-call action. It MUST NOT create a new feature, route, public contract, payload field, acceptance criterion, token, evidence family, PF09 movement, board movement, deployment claim, acceptance claim, or epic-close claim.

The loop completes only when:

1. the original approved proof satisfies its final predicates;  
2. every required routed correction is present in the validation workspace;  
3. applicable canonical evidence companions are coherent;  
4. the named local regression gates pass;  
5. final hosted CI passes on the routed or merged source when CI cleanliness is a completion condition; and  
6. the record preserves the complete receipt lineage without converting an earlier failure into PASS.

Extended authority expires at completion. One-time live, OPS, publication, merge, or deployment authorities expire according to their own narrower terms and are never extended or renewed by implication.

Structural predicate and missing-artifact truthfulness. If a Live QA check fails because a governed repo artifact lacks a required structural field, the check MUST NOT be satisfied by raw string-presence wording alone. The QA plan, remediation guide, or follow-up PR MUST define the structural predicate that proves the field is present and semantically tied to the intended source.

If an initial failing artifact is overwritten or unavailable by the time remediation begins, the remediation record MUST state that the initial failure artifact is unavailable. It MUST NOT reconstruct missing logs, hashes, timestamps, result bodies, or failure artifacts.

For DB bridge and provider parity proof-label posture, `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` remain non-token proof labels unless HDE-Governance registers them or PF10 explicitly mints them. A Live QA correction or remediation note MUST NOT convert those labels into acceptance-token claims.

`/tmp` helper scripts (allowed; execution-only; non-evidence):

* QA agents MAY create ephemeral helper scripts under `/tmp` during Live QA execution.  
    
* These scripts are execution-only and MUST NOT be treated as deliverables or governed evidence.  
    
* Outputs under `/tmp` MUST NOT be indexed, mirrored, path-proofed, or referenced as acceptance binding surfaces.  
    
* Any evidence artifacts produced by a step MUST still be written under the responsible check at `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>` and referenced by that check’s `primary.log`.  
    
* `/tmp` helper scripts MUST NOT print or persist secrets.

Closed-rails testing (`SAFE_MODE=1`, `ALLOW_NETWORK=0`) remains the responsibility of:

* CI jobs wired in the repo, and  
    
* pre-merge QA on PRs implementing the epic

Manual Live QA does not attempt to replicate the full closed-rails surfaces via open-rails commands from Codespaces into Railway.

### **3.4.9 No VCS workflow content (normative; artifact-based PASS/FAIL)**

Live QA Plans MUST be artifact- and evidence-driven. They MUST NOT embed version-control workflow steps.

No VCS workflow content (hard). A Live QA Plan MUST NOT instruct on, assume, or require any version-control workflow, including:

* branches, commits, pushes, PR creation/updates, merges/rebases, conflict resolution, or “git workflow” steps  
    
* requirements about “what branch to be on” or “what commit SHA to record”

No PASS/FAIL gated on VCS state (hard). PASS/FAIL MUST NOT be determined by working-tree cleanliness, branch name, commit hash, or any other VCS state. These are not behavioral evidence and can vary between execution environments.

Optional non-gating repo-root sanity checks (allowed). A plan MAY include a small read-only sanity check to confirm it is running in a repository (for example `git rev-parse --show-toplevel`). If such a sanity check fails:

* classify the affected check as `TOOLING_BLOCKED` (not `FAIL_BEHAVIOR`)  
    
* continue with other non-dependent steps when possible

A plan using a sanity check MUST NOT mutate repo state (`git checkout`, `git commit`, `git clean`, and similar) and MUST NOT require PR metadata or a specific branch/commit.

Known Codespaces packaging artifacts. Codespaces sometimes includes `.codespaces/.persistedshare` and/or `*.tar` artifacts that can trigger git status noise. These are non-blocking for QA; do not gate on them.

If a plan currently requires “clean git status” as a precondition, update it. The plan should focus on the artifacts it produces and the behavior it verifies.

### **3.4.10 Plan validity lint (blockers-only; deterministic)**

Blockers (reject the plan until corrected):

* Missing required sections, required end marker, or required gates as defined by Plan Templates.  
    
* Contains the Unicode ellipsis character (U+2026) or the ASCII triple-dot sequence (three consecutive period characters) outside code spans; or uses implicit truncation markers instead of explicit markers like `[SNIP: <n> lines omitted]`.  
    
* Treats a truncation token as intended content in any relied-on passage. Any truncation token in any relied-on passage is a read-failure signal; the reviewer MUST re-open and replace the relied-on passage with complete text before approval, execution, or doc edits.  
    
* Introduces or requires `run_id`or `RUN_ID`as an operator input, step-log header field, manifest field, or correctness key.  
    
* Introduces, requires, or treats as meaningful any unapproved environment variable name (including any `MODO_*`variable) as a required plan input, required step-log header field, required manifest field, or required evidence schema field; env var names are governed loci and MUST NOT be minted during Live QA or Moon Loop.  
    
* Mandates updates to any PF document (including Reality Audits) as a required plan deliverable, PR deliverable, OPS deliverable, acceptance criterion, or close condition. Plans MAY record doc-delta candidates, but MUST label them as non-mandatory and PO-owned.  
    
* Uses wildcarded evidence paths, variable placeholders, or “latest” semantics for required artifacts, proofs, or manifests.  
    
* Uses a closure template or plan template that enumerates step-scoped evidence paths for steps that have not executed yet without explicitly labeling those artifacts as NOT RUN (or DEFERRED). Future-step artifacts may be listed, but MUST be marked NOT RUN / DEFERRED and MUST NOT be treated as missing evidence.  
    
* Uses an entrypoint, harness, command, test file, test node, endpoint path, check name, or CI job name that does not exist at the time of planning.  
    
* Mixes canon policy statements with plan-only details or fails to route bytes to their single canonical home.

Non-blocking review constraints (do not fail the plan for these):

* Minor whitespace, indentation, and Markdown formatting defects are syntax-origin conditions and are non-blocking. If the plan separately omits a required semantic dependency, governed byte identity, or evidence obligation, evaluate that independent non-syntax defect on its own evidence.  
* Heading-level differences, heading styling differences, and other cosmetic Markdown variations are non-blocking when the semantic heading identity and required section set remain unchanged.  
* Uppercase letters in filenames are non-blocking; the lowercase constraint applies to directory names only.  
* Fenced code blocks and code-block formatting are non-blocking presentation choices. When execution requires exact bytes, the exact executed command or helper bytes belong in governed execution evidence rather than becoming a plan-approval formatting gate.  
* Copy-and-paste artifacts, presentation escapes, AI-rendered escapes, Markdown-rendered escapes, transcript-formatting escapes, quote-formatting escapes, assistant-output escapes, preview-pane escapes, and review-prose escapes are syntax- or rendering-origin conditions and are non-blocking.  
* Reviewers MUST evaluate the syntax-normalized semantic intent of the plan rather than the malformed literal representation.  
* Raw-source confirmation may establish where a syntax-origin defect appears. It does not convert that defect into a substantive defect or make it blocking.  
* Machine-sensitive strings MUST still be checked against raw artifacts and governed bindings. If a source specifies the wrong path, filename, token, command, environment variable, endpoint, PF09 identifier, or artifact identity independently of syntax or formatting, evaluate that separate non-syntax defect after faithful normalization.  
* The causal source controls classification. Syntax, quoting, escaping, shell grammar, tokenization, command-wrapper form, heredoc form, helper-code form, variable interpolation, indentation, whitespace, Markdown rendering, code-block formatting, backslash insertion, copy-and-paste corruption, interpreter invocation form, and literal command presentation remain syntax-origin defects.  
* A syntax-origin defect remains non-blocking even when the literal text fails to parse, fails to execute, appears to change command identity or meaning, invokes an incorrect apparent form, loses delimiters, cannot reach the intended behavior, or would produce a different literal result.  
* QA plans, review artifacts, Live QA results, acceptance maps, token-evidence matrices, closeout reports, PR reviews, remediation reviews, and implementation-plan reviews MUST NOT classify syntax-origin or rendered-escape defects as `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, QA failure, token failure, path-proof failure, canonical-path failure, quote-verbatim failure, PF-locator failure, acceptance failure, implementation blocker, or closeout blocker.  
* For each apparent command-form issue, the reviewer MUST:  
  1. identify the intended objective, operation, semantic inputs, outputs, rails posture, evidence target, and PASS or FAIL predicate;  
  2. assume a syntactically valid representation that preserves those semantics;  
  3. determine whether the alleged defect remains after normalization;  
  4. exclude the syntax-origin issue from the review decision when normalization removes it; and  
  5. report a substantive finding only when an independently proven non-syntax defect remains.  
* A substantive blocker is allowed only when an independent non-syntax defect survives faithful normalization. The finding MUST state the syntax-normalized intended operation, the governing requirement or contract, the independent evidence proving the remaining defect, and the material harm.  
* A mixed finding MUST be separated. Discard the syntax component and evaluate only the independently proven non-syntax component.  
* Plans may be approved without repairing syntax. During execution, the operator may normalize syntax when the semantic contract remains unchanged, and the governed evidence MUST capture the exact command actually executed, command provenance, reason for normalization, produced artifacts, exit code, output, and final verdict.

Reviewer hygiene rules (clarification):

* Template adherence is structural only. It means the required sections are present, the required end marker is present, and any required gates are present. It does NOT mean that headings must match a specific styling.  
    
* Header formatting is a Nit. Reviewers MUST NOT request redlines that only change heading levels, add or remove bold or italics, or reformat headings for aesthetics. These are not plan-approval conditions and must not change the binary approval outcome.  
    
* Plans MAY include read-only PF checks, including Reality Audits, to confirm current guidance. Plans MUST express PF checks as consult-only and MUST NOT require turning the check result into a PF update.  
    
* Existence confirmation inside plans MUST be expressed as either a read-only PF check or repo-local evidence capture. Plans MUST NOT require turning existence confirmation into a PF document edit.  
    
* Ellipsis tokens are permitted inside code spans only when they represent a literal being discussed. Outside code spans, ellipsis tokens are prohibited and treated as truncation signals, not as content.  
    
* Approved omission markers are `[SNIP: lines omitted]` and `[SNIP: paragraph omitted]`. Any other omission marker is treated as non-canon.  
    
* Approval binds to semantic command identity, not command syntax. Plans MAY include a command-snippets section as a de-duplication mechanism; the authoritative execution record is the exact command captured in governed evidence.  
    
* If a plan uses JSON-carrying environment variables, quoting and escaping defects remain syntax-origin and non-blocking at approval time. The exact executed bytes MUST be captured before PASS is claimed.  
    
* Template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table formatting, heading style, punctuation, spacing, bold markers, presentation style, and inventory-row ordering are non-blocking. A separately proven source-authority, scope, PF09-mapping, token-truth, evidence-identity, evidence-trust, portability, authorization, safety, public/private-boundary, or closeout defect may be evaluated independently.  
    
* Epic Plans are planning records. They are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Plan review MUST NOT block on QA-runbook-level precision, close-pack-level evidence-path completeness, template inventory polish, or a missing Epic QA root declaration unless an independent planning-truth, QA-execution, or evidence-production requirement establishes the defect.  
    
* Implementation Plans must be more concrete than Epic Plans, but formatting-origin defects remain non-blocking. An independent non-formatting defect involving Codex or OPS ambiguity, external-source dependency, token overclaim, proof identity, execution context, or acceptance truth may block when separately proven.  
    
* A reviewer who blocks a planning artifact MUST state the independently proven non-syntax defect and material harm. Syntax-origin concerns MUST NOT be used as Caveats, required Nits, Expected fixes, revision conditions, or bases for `REVISE AND RESUBMIT`.  
    
* When a QA executor normalizes syntax during execution, the governed step evidence MUST record the exact command actually executed, command provenance, the reason for correction, produced evidence artifacts, and the final PASS, FAIL, or TOOLING classification. The correction MUST NOT silently alter the acceptance target.  
    
* Live QA Plan approval is an operational-readiness review. A Live QA Plan should be approved when it is safe, self-contained, phase-bounded, and semantically clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict.  
    
* Live QA Plan approval MUST NOT block solely on rendered escape characters, Markdown or AI-rendered backslashes, heading style, bullet style, table style, quote-block formatting, code-block formatting, whitespace, punctuation, line wrapping, command-syntax polish, command invocation style, exact shell spelling, evidence-ledger byte-shape polish, path-proof transcript-field polish, canonical-JSON wording, or step-log header polish.  
    
* A Live QA Plan approval Blocker is valid only when an independent non-syntax defect materially affects safe execution, required QA coverage, deliverable existence, verdictability, rails posture, secret handling, external-action boundaries, public/private boundaries, token truth, source authority, evidence trust, proof-target identity, repo-locus truth, category separation, phase scope, or closeout truth.  
    
* An exact command mismatch caused by syntax or literal presentation remains non-blocking regardless of its apparent execution effect. A separately intended selection of the wrong tool, proof target, rails posture, secret posture, mutation boundary, or verdict predicate may be evaluated only when independent non-syntax evidence proves that semantic defect after normalization.  
    
* A QA-created harness may be part of a Live QA Plan when it is limited to QA evidence capture and does not create product behavior. Reviewers MUST NOT require repo-existence proof for a QA-created harness that the plan explicitly creates during the QA run.  
    
* A QA-created harness issue is a Blocker only when an independent non-syntax defect in its semantic creation requirements would make the harness unsafe, out of scope, behavior-changing, unable to prove the intended target, unable to emit a verdict, or unable to produce or identify required governed evidence. Malformed syntax or presentation alone does not satisfy that standard.  
    
* Live QA Plan approval requires evidence identity, not final closeout perfection. The plan must identify what each check proves, what counts as PASS, what counts as FAIL, where the QA run records the decisive receipt, which evidence family supports the verdict, and how token claims are avoided unless registered and in scope.  
    
* Syntax- or presentation-origin defects in canonical-JSON, field-order, path-proof, step-log, Mirror-record, or evidence-index wording are non-blocking. Independently missing evidence identity, decisive receipts, governed-evidence discipline, or proof bindings may block when separately proven.  
    
* A reviewer who blocks a Live QA Plan MUST state the independent non-syntax defect and operational harm. `REVISE AND RESUBMIT` is reserved for independently proven truth, authority, scope, evidence, acceptance, phase, authorization, or safety defects.  
    
* Plans are not execution artifacts. QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, and closure-review artifacts MUST NOT be blocked, rejected, returned for revision, or classified as `REVISE AND RESUBMIT` because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, Markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written.  
    
* This syntax and paste-readiness rule applies even when the issue appears in raw source text, even when the reviewer believes the command would fail if pasted directly, and even when the issue involves escape characters, backslashes, Markdown escaping, shell redirection, heredoc syntax, command options, interpreter invocation, indentation, Python snippets, Bash snippets, code-block formatting, quote formatting, wrapping, whitespace, punctuation, copied-command exactness, non-literal examples, assistant-introduced syntax artifacts, renderer-introduced syntax artifacts, or formatting introduced during review, redline, or paste workflows.  
    
* QA steps do not need to be literal executable commands. They may express the intended proof action in operational language, pseudocode, structured prose, or approximate command form when the proof target, scope boundary, rails posture, evidence intent, and expected verdict posture are clear enough for the assigned operator to execute the QA run and produce governed evidence.  
    
* Syntax correction is ordinary execution hygiene. A QA operator, Codex, Kronos, PO, or implementation owner may normalize a non-runnable command, escaped string, indentation defect, heredoc issue, shell-syntax issue, or helper-code formatting issue in flight when the proof target, QA-step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, secret posture, token posture, and scope posture remain unchanged.  
    
* In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or QA Plan revision. If normalization reveals an underlying change to proof target, scope, source authority, rails posture, evidence identity, acceptance posture, or safety boundary, evaluate that separate non-syntax defect independently.  
    
* Valid plan blockers remain independently proven truth, authority, scope, evidence, acceptance, phase, authorization, or safety defects. A reviewer MUST NOT disguise syntax, paste-readiness, escaping, helper-code formatting, heredoc form, indentation, interpreter choice, or command-exactness complaints as truth or proof blockers.  
    
* Syntax concerns may be recorded only as neutral, non-gating notes or in-flight normalization records. They MUST NOT be classified or used as a Blocker, Caveat, required Nit, Expected fix, approval condition, QA-readiness condition, implementation-readiness condition, closure condition, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, acceptance failure, path-proof failure, evidence failure, token failure, PF-locator failure, command-validity failure, or revision basis.  
    
* Any reviewer returning `REVISE AND RESUBMIT` MUST state the independently proven non-syntax truth or proof defect and its material harm. If faithful syntax normalization removes the objection, it is not a blocker, Caveat, required Nit, Expected fix, or revision basis.  
    
* For HDE-EPIC033 and later HDE work, QA Plan review must preserve the distinction between contract inventory and runtime v2 conformance, preserve HDE-FERM007 and HDE-FERM008 deferral, and preserve no live vendor smoke, no runtime request shaping, no public Reader expansion, no new HTTP home, no AI scope, and no vendor-v2-specific acceptance-token minting. It must not block on command paste-readiness, raw or rendered escape characters, helper-code indentation, heredoc validity, command exactness, or syntax that can be normalized in flight.  
    
* Template semantics: NOT RUN / DEFERRED is not missing evidence. Missing evidence is reserved for: the producing step executed, and the artifact that step is supposed to emit is absent or unproven. Closure and rollup steps MUST separate these states clearly:  
    
  * PRESENT — artifact exists and is referenced by path  
      
  * MISSING — producing step executed, artifact absent or unproven  
      
  * NOT RUN / DEFERRED — producing step not executed yet (no artifact expected)


* Prompt-family separation (hard guardrail): every QA prompt MUST declares its mode as one of AUTHORING or REVIEW, and the agent MUST output only the mode's required structure. If the prompt mode is REVIEW, the agent MUST NOT produce new runbooks or commands, except for the remediation exception where commands are copied verbatim from the plan or caveats.  
    
* Workflow recommendation (strong; non-blocking): enforce mode with a mechanical gate (header token plus required section list). If required sections do not match mode, fail fast.  
    
* QoS escalation (stop-rule): if the planning and review loop fails to converge and requires repeated structural remediation for the same failure mode (example: template lists future-step artifacts as required now), stop patching and escalate to systems RCA plus template or canon drain. Capture the failure class and drain targets explicitly.  
    
* Drain targets recorded (titles-only): Plan Templates; Epic Process Guide; Reality Audits.  
    
* When tool output escapes Markdown (example: backslash-escaped underscores), treat the escapes as presentation only. Do not treat the escaped form as a distinct path, token, or identifier.

### **3.4.11 Vendor and DB safety constraints (names-only)**

Even under open rails:

* Vendor/production write flows that resemble real user writes remain out of scope unless explicitly permitted by current product posture.  
    
* Live QA must use dry-run or closed-rails stubs where the canon requires it.

  ### **3.4.12 Doc-alignment steps (mechanical, not narrative)**

For doc-alignment Live QA steps:

* Steps MUST rely on mechanical commands (`ls`, `grep`, `find`, Python tooling) that generate tree listings, filtered file lists, or diffs.  
    
* Outputs MUST be written under the responsible `audit/qa/<epic-id>/checks/<check_id>/` directory as the check’s `primary.log` or explicit check-scoped sidecars.

Close-pack truthfulness and same-run execution (normative). If an epic close report or close-pack artifact states that Human Index, Machine Mirror, checksum, path-proof, or governed close-gate refresh occurred, the same run MUST have actually executed the corresponding workflow and preserved mechanical evidence for those executions under the epic QA root.

Artifact presence alone is not sufficient when the close report claims the underlying gates ran. The evidence set MUST include same-run primary logs or step-scoped mechanical outputs that capture the exact commands executed and the resulting PASS, FAIL, or BLOCKED posture for the claimed close-pack and evidence-discipline checks.

When the close-pack family changes, the close-pack family consists at minimum of the epic acceptance map, token/evidence matrix, acceptance-map viability log, close report, close manifest, and any changed governed Human Index, Machine Mirror, hash-sentinel, or sibling path-proof companions. These surfaces MUST refresh coherently in the same change.

A closeout record MUST NOT over-claim freshness. If the close-pack family is refreshed but any corresponding path-proof, Index, or Mirror surface still carries older produced\_at\_utc or mtime\_utc values, treat the closeout as a provenance defect and regenerate the governed evidence tooling outputs before PASS is claimed.

If follow-up canon or checklist deltas remain outside the close-pack family, the close report MUST record them explicitly as follow-up or doc-delta items. They MUST NOT be silently conflated with missing or unexecuted close-pack proof.

Close report requirements (validator-bound; mechanical). Epic close reports (for example `audit/EPIC-023_close_report.md`) MUST include:

* the heading `QA Rails — Open/Close (Final PR)` (verbatim), and  
    
* an “Acceptance and evidence pointers” list containing the epic’s canonical pointer strings (exact text)

Example (EPIC-023 historical audited surface; not reusable current-state grammar):

* `docs/acceptance_map_epic023.json`  
    
* `audit/qa/hde-epic023/token_evidence_matrix.md`  
    
* `audit/qa/hde-epic023/acceptance_map_viability.log`  
    
* `audit/qa/hde-epic023/qa_step_logs_manifest.json`

The close report check validates required pointer strings as literal substrings; missing any required pointer is a mechanical FAIL for the close report check.

PO/operator must not be required to write prose summaries as part of execution. Narrative synthesis belongs in the close report and canon updates (titles-only routing).

### **3.4.13 Lowercase directory naming guardrail (NEW)**

Scope (normative). This guardrail governs directory names under governed QA evidence roots, including `audit/qa/` and `artifacts/`.

Directory rule (normative). Directory names MUST be lowercase. A directory segment is non-conforming if it contains any uppercase ASCII letter.

Filename rule (clarification). This guardrail applies to directories only. Filenames may contain uppercase letters unless a separate canon rule forbids them.

Plan-writing rule (normative). Live QA plans and remediation guides MUST:

* use lowercase directory segments for all governed evidence locations  
    
* if a task is labeled with uppercase (for example OPS-01), map it to a lowercase directory segment (for example `ops-01/`) and keep the uppercase label in the filename or in plan prose

Examples (informative):

* Allowed staging example: `audit/qa/<epic-id>/remediation/ops-01/OPS-01_selected_host_label.txt` (non-binding unless separately promoted)  
    
* Non-conforming staging example: `audit/qa/<epic-id>/remediation/OPS-01/selection.txt`

Implementation note (informative). Automated scans for this guardrail MUST scan directories and MUST NOT scan files. For example, scan directories using `find audit/qa -type d -name '*[A-Z]*'`.

### **3.4.14 Tokens-first QA planning and deterministic acceptance (normative)**

Acceptance criteria MUST be expressed using canonical acceptance token names (names-only). Freeform acceptance statements are not allowed as acceptance criteria.

Planning tiering (normative):

* Epic planning artifacts MUST define the in-scope acceptance token roster and the evidence families to be captured, but MUST NOT embed a full step-by-step Live QA execution script.  
* The Live QA plan is the home for step-by-step execution. Steps MUST exist to claim one or more acceptance tokens and to capture the required evidence surfaces.

Minimum viable Live QA plan requirements (normative):

* Token roster: list the in-scope acceptance tokens by canonical name (see §9.2 canonical naming rules). If a required token is not registered, it MUST be marked as unclaimable and routed through the governance workflow; do not invent a plan-local token alias.  
* Evidence binding: for each token, identify the primary governed evidence artifact (or an approved manifest/bundle) under the governed QA write roots.  
* Step discipline: every step MUST map to an acceptance token claim or an evidence capture requirement. “For completeness” steps with no token or evidence binding are non-conforming. Conversely, each in-scope token MUST be covered by at least one step.

Deterministic acceptance posture (normative):

* Prefer deterministic, repeatable evidence artifacts (governed output files, deterministic command output, pinned environment values) over narrative descriptions.  
* Prose-only claims do not satisfy acceptance tokens.

Validated reference posture (normative):

* Plans MUST NOT invent repo paths. Any repo path referenced in the plan MUST be backed by canon citation, a verbatim consult quote that is explicitly labeled as consult input, or a captured inspection transcript stored under governed QA write roots.

## **3.5 Live QA via Codespaces → Railway (cross-epic crib)**

This section generalizes the EPIC017 pattern into a required crib for any epic that uses “prod via Codespaces” (or an equivalent terminal) to exercise HD Engine prod behavior.

### **3.5.1 Prod and console roles**

Prod is defined as follows: for Live QA, prod is the HD Engine service and DB defined in infra and build canon (by title, for example Glow Infrastructure and HDE-Build Notes), not the Codespaces container.

Codespaces / QA console is defined as follows: a Codespace attached to the engine repo is a QA console and artifact sink:

* it runs CLI/HTTP commands from Codespaces to the Railway HD Engine prod service and DB (when rails allow)  
    
* it stores each check’s QA artifacts under `audit/qa/<epic-id>/checks/<check_id>/` in the repo, where \<epic-id\> is the lower-case epic identifier (for example `hde-epic018`) and the approved plan resolves the concrete \<check\_id\>

Any other terminal or shell that is configured (by infra canon) to reach the same Railway endpoints is an equivalent QA console. PF19’s CLI and admin-bundle playbooks apply equally to Codespaces and to such terminals.

IAs and QA plans MUST NOT treat Codespaces itself as “prod”; any QA plan that does so is mis-aligned with this guide.

### **3.5.2 Step 0 — prod handshake (identity-only, not behavior)**

Auth posture is not yet canonized (non-invention rule). PF canon defines the /internal/version transport and content contract, but access-control semantics are not yet canonized. Until a canon decision is made, Live QA plans, remediation guides, and operational tooling MUST NOT assume whether /internal/version is unauthenticated public, operator-network gated without auth, or auth-header required.

If an auth header is used in an operational context, it MUST be treated as observed evidence only: record presence-only (never the value) and do not encode the posture as canon in runbooks.

Evidence required to canonize auth posture (secret-free) is as follows: capture headers for the canonical deployment context(s) under two conditions:

* with no auth header  
    
* with the expected auth header present (value redacted or presence-only noted)

The evidence MUST be secret-free and stored in-repo under a lowercase audit path under the epic QA root. The evidence must be sufficient to decide the intended posture and the expected failure mode for missing or invalid access (status code and headers).

For any epic that claims to do “Live QA via Codespaces → Railway”, the QA plan MUST include a Step-0 “prod handshake” from a QA console:

* calling the canonical HD Engine prod base URL (for example /internal/version on the Railway service defined in infra canon, titles-only)  
    
* capturing the response in the handshake check’s `audit/qa/<epic-id>/checks/<handshake_check_id>/primary.log`, with any separate response body or headers stored under the same check directory using explicit filenames

/internal/version is an identity / pre-flight endpoint. Its job in Live QA is to prove:

* that the QA console (Codespaces or equivalent) can reach the prod engine  
    
* which engine\_tag, release\_id, commit, and invocation\_tag are live at the time of QA (as already described in the EPIC017 QA history)

Live QA plans MUST NOT present /internal/version as satisfying any D-goal or token related to behavior (compat math, narratives, vendor ingest, admin bundle, “full product payload”). It is a prerequisite and an identity anchor for later evidence, not a substitute for real behavior tests.

If infra/build canon does not yet define the prod base URL or DB (or they conflict), the epic’s Live QA plan must mark prod handshake as blocked by spec ambiguity rather than guessing or asking the PO for values.

Internal version acceptance token names are canonical and non-aliasable. Acceptance token names for /internal/version MUST match the names defined in HDE-Governance. Tools, guides, matrices, and acceptance maps MUST NOT invent aliases.

Canonical conditional semantics token name (normative) is INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK. Any other name intended to mean “conditionals return 200 and never 304” (including INTERNAL\_VERSION\_COND\_200\_NO\_304\_OK) is non-canon and MUST NOT be emitted or required in acceptance artifacts.

If a tool currently emits a non-canon alias, remediation MUST treat that as a defect and plan to converge to the canonical naming.

Internal version proof surface uses an explicit invariant checklist (required). Any remediation guide, QA step, or probe tool that produces /internal/version governed evidence MUST explicitly enumerate and verify the canon-critical invariants below. It is not acceptable to imply these checks by referencing PF sections only.

Canon-critical invariants (minimum set) for the canonical /internal/version identity response are:

* Transport  
    
  * GET MUST return 200\.  
      
  * HEAD MUST return 200 and satisfy parity expectations.  
      
  * Conditional requests (If-None-Match, If-Modified-Since) MUST NOT yield 304; they MUST return 200\.


* Headers  
    
  * Cache-Control: no-store MUST be present.  
      
  * Content-Type: application/json; charset=utf-8 MUST be present.  
      
  * ETag MUST be absent.  
      
  * docs/ENDPOINTS\_CATALOG.json MUST include /internal/version, and the catalog entry MUST set a7\_eligible: false (inventory posture; /internal/version is not an A7 surface).  
      
  * Last-Modified MUST be absent.


* Body (identity payload)  
    
  * Body MUST be fixed-schema JSON with exactly these keys (no extras): engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id.  
      
  * Body bytes MUST satisfy the canon “identity bytes” posture where applicable to the proof surface (canonical bytes, including LF termination).

Token emission gating (no “false OK”) is required. A tool MUST NOT emit any \*\_OK token unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run.

FAIL\_TOOLING semantics (normative) apply. If the run status is FAIL\_TOOLING (or equivalent), the tool MUST NOT emit \*\_OK tokens for invariants that did not pass. In particular, it MUST NOT emit “integrity success” tokens (for example path-proof match or two-run identity) unless those checks demonstrably passed on the produced artifacts.

Coupling requirement (anti-mixed-target / anti-redirect drift) applies. For each probe run, the evidence must be coupled such that the emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit \*\_OK tokens.

### **3.5.3 Artifact-first Live QA pattern (behavior vs artifacts)**

For any Live QA step that refers to behavior, QA plans MUST follow a two-part, artifact-first pattern.

1. Behavior run (prod-facing environment). The QA plan MUST specify where the behavior is exercised, for example:  
     
* “run hdctl on an admin terminal that can reach \<HDE\_PROD\_BASE\_URL\> and is configured with the canonical env and secrets,” or  
    
* “click the Admin GUI control that calls the admin bundle HTTP route.”

The plan must:

* describe the inputs (for example fixed birth tuples or, post user-model, user IDs), and  
    
* describe the expected observable behavior at the prod-facing surface (status, body shape, high-level outcome)

Where possible, it should also prescribe how to capture outputs on that environment (for example writing JSON to a file, saving a log transcript, or exporting a report).

2. Artifact capture and analysis (Codespaces / QA console). The QA plan MUST then describe how artifacts from the behavior environment are brought into the responsible judging check under `audit/qa/<epic-id>/checks/<check_id>/` and analyzed. The approved plan MUST resolve the concrete `check_id`. At minimum, Live QA instructions MUST include copy/paste-ready commands (fenced blocks optional) that:  
     
* create any needed subdirectories only under the responsible `audit/qa/<epic-id>/checks/<check_id>/` directory (all lower-case directories; see §8)  
    
* copy or upload the behavior artifacts into those directories (for example via scp, gh run download, or equivalent)  
    
* run offline validation in the QA console (for example python \-m json.tool, cmp, sha256sum, header/posture checks) and write results to explicit files in `audit/qa/<epic-id>/checks/<check_id>/`  
    
* generate step notes mechanically in `audit/qa/<epic-id>/checks/<check_id>/primary.log`, or in an explicit check-scoped sidecar referenced by that log; do not use a shared root-level notes file or manual editing, consistent with §4.3

Key principle: Codespaces is where we persist and analyze what happened when we ran prod; it is not itself the authoritative behavior runtime.

Live QA plans MUST NOT conflate these two phases. A step that only runs logic inside Codespaces under closed rails (for example hdctl showcompat pointing at `127.0.0.1` with SAFE\_MODE=1, ALLOW\_NETWORK=0) may be used as a local smoke check, but cannot be used to satisfy tokens or D-goals that assert prod behavior (compat in prod, narratives in prod, vendor ingest in prod, full product payload from prod). Any such step must be explicitly labeled as a local smoke check in the QA plan and must not be used to claim prod behavior tokens.

### **3.5.4 Pre-Glow full-payload admin bundle flow (acceptance expectation)**

In the pre-Glow period (before the App is integrated with the HD Engine and before the Admin Bundle CLI/GUI surfaces are fully implemented), any epic that claims the product is usable or testable “in prod” MUST include at least one Live QA step that:

* exercises the full product payload for a single match via prod-facing behavior, and  
    
* follows the artifact-first pattern described in §3.5.3, and  
    
* uses no GUI-only shortcuts and no Codespaces-only behavior

For epics executed before the admin bundle surfaces exist, this requirement is satisfied by the historical “full product payload” flows that compose BodyGraphs, compat, and narratives via individual CLI and HTTP calls on a prod-facing machine, as described in earlier PF19 and HDE-Build Notes addenda (titles-only).

Once the admin bundle builder and admin surfaces are implemented and pinned in canon, new epics MUST use the admin bundle surfaces as the primary behavior paths, not reassemble the payload manually.

For this full-payload step, the Live QA plan MUST specify:

* Behavior run  
    
  * a prod-facing environment (for example an admin terminal running the admin bundle CLI against Railway, or an Admin GUI in a browser calling the admin bundle HTTP route), and  
      
  * the exact inputs used


* Artifact capture / analysis  
    
  * how the resulting admin bundle JSON and logs are brought into `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>` under the responsible full-payload check from the behavior environment, and  
      
  * how parity and auth are checked, following §5.8 and the artifact-first pattern above

Evidence for this step MUST:

* be captured under the responsible `audit/qa/<epic-id>/checks/<check_id>/` directory  
    
* be wired into the evidence skeleton (Index, mirror, path-proofs) in the same PR  
    
* support the admin-bundle tokens from §9.1.5 and §9.2.7:  
    
  * CLI\_ADMIN\_BUNDLE\_PARITY\_OK — CLI and HTTP admin bundles match for the same inputs and credential.  
      
  * ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK — each admin bundle contains all required structural elements (BodyGraphs, compat, three narratives, meta) as defined in the owning PF docs.  
      
  * ADMIN\_AUTH\_REQUIRED\_OK — neither CLI nor HTTP admin surfaces return an admin bundle without the configured admin credential; unauthenticated and mis-authenticated attempts return typed errors only.

Any pre-Glow Live QA plan that does not demonstrate at least one such artifact-first, prod-facing full-payload flow is considered incomplete under PF19 once the admin bundle surfaces exist (or an equivalent full-payload behavior flow is defined), and must be revised before tokens depending on “product usable via admin bundle surfaces” or “full product payload from prod” can be claimed.

### **3.5.5 PO Live QA sessions (vendor-first rails)**

For EPIC018 and all future epics, “PO Live QA” is vendor-first by definition.

Definition and scope are as follows: a PO-run Live QA session is a short, focused session whose primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.

Live QA plans recognize three classes of checks:

* Ops/identity checks (for example, /internal/version identity pings, env/rails snapshots).  
    
* Internal functional/determinism checks (serializer/compat determinism, sanity pipeline, CLI guards and invariants) that are already covered by CI and automated QA.  
    
* Vendor flows (vendor-backed BodyGraph resolution and compat, vendor error handling, live vendor rails checks in prod).

Only class (3) belongs in PO Live QA. Classes (1) and (2) are useful to QA/infra/CI but do not justify PO Live QA time and must not be treated as part of the PO’s Live QA workload.

Roles of each class are as follows:

* Ops/identity steps (class 1), including the /internal/version handshake:  
    
  * are treated as pre-flight / internal  
      
  * are designed and executed by QA/infra (or CodEx) before PO Live QA, and  
      
  * may be referenced in PO notes as preconditions, but are not counted as PO Live QA steps and cannot satisfy behavior D-goals


* Internal functional/determinism steps (class 2\) such as serializer determinism, sanity pipeline, CLI guards, or evidence skeleton checks:  
    
  * remain entirely within CI/QA/infra responsibility (PF09 and PF14 wiring), and  
      
  * must not be scheduled as PO Live QA tasks, even if they are re-run in staging/prod; they are prerequisites, not PO targets


* Vendor-focused steps (class 3\) such as:  
    
  * vendor-backed BodyGraph resolution (for example bg:resolve \--source=vendor in dry-run or other controlled modes)  
      
  * vendor-backed compat calculations (for example showcompat \--source=vendor or equivalent Admin Bundle based paths once defined), and  
      
  * deliberately chosen vendor error conditions and edge cases (malformed input, missing data, vendor timeouts)  
      
  * are the only steps that may appear in PO Live QA as core workload

Codespaces in PO Live QA has the same roles as in §3.5.1, with one additional constraint. By default, Codespaces is an artifact sink and offline analysis console. It is where:

* responsible vendor-behavior check directories under `audit/qa/<epic-id>/checks/<check_id>/` are created  
    
* artifacts from prod-facing runs are stored, and  
    
* offline checks (python \-m json.tool, cmp, sha256sum, header validation) are executed

Codespaces MAY temporarily act as a vendor client (for example, by setting SAFE\_MODE=0, ALLOW\_NETWORK=1, and configuring a base URL to Railway prod) only when all of the following are true:

* the goal of the step is to exercise a live vendor flow (class 3), not an identity or determinism check  
    
* the rail-opening for that step is documented in the relevant vendor check’s `primary.log`, with environment variables, commands, and any explicit sidecars written under `audit/qa/<epic-id>/checks/<check_id>/`, and  
    
* the PO has agreed that this is an acceptable way to reach prod vendor rails for the current epic

For non-vendor behavior (serializer determinism, guards, sanity pipeline, closed-rails tests), Codespaces MUST NOT be used as a surrogate “prod” environment in PO Live QA. Those checks remain in the CI/QA/infra domain and are out of scope for PO Live QA sessions.

Production-affecting Live QA minimum is as follows.

For any epic that can affect real production functionality, deployed runtime behavior, external integrations, vendor ingest, vendor route policy, external API transport, DB persistence or retrieval, public or app-facing behavior, CLI behavior, operator-facing CLI surfaces, runtime request or response behavior, compute used by production, admin or ops-facing behavior that can affect production, or secret or environment binding, the Live QA Plan MUST include at least one bounded open-rails live QA step that proves a real production-relevant behavior in the deployed or live environment.

Closed-rails proof remains required where applicable, but closed-rails proof alone is not sufficient for a production-affecting epic unless the plan records an explicit authorized exemption. A valid exemption must state why open-rails live QA is not safe or not applicable, what closed-rails proof remains available, what production claim is not being made, and what follow-up is required before the omitted production-facing claim can be made.

The open-rails live QA step must be scoped, PO-authorized, secret-safe, mechanically evidenced, and clear about what it proves and does not prove. It must not rely only on mocked fixtures, closed-rails replay, static analysis, generated artifacts, documentation review, repo-local inspection, PF09 supportability language, or a written but unexecuted smoke procedure.

### **3.5.6 Vendor vs non-vendor steps in Live QA plans**

Any Live QA Guide or QA Plan for an epic MUST:

* clearly label each Live QA step as vendor-focused (class 3), ops-only (class 1), or internal functional/determinism (class 2), and  
    
* explicitly indicate which subset of steps is expected to be run by the PO in Live QA, and which steps are preconditions/CI responsibilities

For EPIC018 and forward, PO Live QA plans MUST:

* define the core PO workload as a small set of vendor-focused steps (for example, “Step V1: vendor dry-run resolve,” “Step V2: vendor-backed compat,” “Step V3: vendor error behavior”), and  
    
* treat all non-vendor steps (identity, serializer determinism, sanity pipeline, CLI guards, closed-rails checks) as pre-verified by CI/QA; the PO is not expected to re-run these manually during Live QA

If a Live QA plan includes non-vendor steps (for example, a pre-flight /internal/version handshake), those steps MUST be explicitly marked as:

* “Pre-flight / internal”, and  
    
* “Handled by QA/infra outside PO’s Live QA time”

These labels ensure that PO Live QA is reserved for vendor behavior, while CI/QA/infra continue to own identity, determinism, and guard checks.

### **3.5.7 Evidence expectations for vendor-focused PO steps**

Each vendor-focused PO step MUST produce at least one mechanical artifact under its relevant `audit/qa/<epic-id>/checks/<vendor_check_id>/` directory that directly reflects vendor behavior, in addition to any governed artifacts under `docs/**` or `artifacts/**`. The approved plan MUST resolve `<vendor_check_id>` to a concrete value.

At minimum, for each vendor step QA must capture:

* a request description file (schematic example: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_request.txt`) that names the command or GUI action, the environment used, and the inputs (birth tuples, synthetic IDs, or, once in scope, user IDs)  
    
* the raw outputs in a governed file (schematic examples: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_run1.json` or `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_run1.log`), and, where helpful, a pretty-printed form (schematic example: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_run1.pretty.json`)  
    
* any diff/cmp results for determinism checks (schematic example: `audit/qa/<epic-id>/checks/<vendor_check_id>/vendor_run1-vs-run2.diff`), when the step is meant to assert vendor determinism, and  
    
* at least one mechanically generated note in the vendor check’s `primary.log`, or in an explicit check-scoped notes sidecar referenced by that log, not via manual editing, consistent with §4.3

Vendor-focused artifacts MUST live under the responsible vendor-behavior check directory, with explicit filenames and vendor-subject labels, so that vendor evidence is easy to locate and reference from epic acceptance rosters (see HDE Phased Epics and PF20 by title). A root-level `vendor/` structural family is not current-state grammar.

All vendor-focused PO artifacts remain subject to the same evidence rules as other governed artifacts:

* directory names under governed roots are lower-case (§8)  
    
* artifacts are eventually indexed in the Human Index and Machine Mirror with path-proofs in the same PR that relies on them (§4.2–§4.3), and  
    
* Live QA plans treat “vendor evidence present but not indexed” as a QA failure that blocks tokens depending on that evidence  
    
* HDAPI v2 vendor-conformance QA posture is pending until the relevant implementation and governed evidence exist. QA plans, reviews, and closeout artifacts MUST NOT claim HDE runtime v2 conformance from documentation consolidation, research notes, endpoint pages, or source inventory alone.  
    
* HDAPI v2 QA plans MUST distinguish at least these proof classes: contract-inventory proof, source-precedence and artifact-sanity proof, v2 request-shaping proof, v2 response-normalization proof, closed-rails refusal and deterministic shaping proof, PO-only open-rails vendor-smoke proof, v2 error, retry, and rate-limit mapping proof, and evidence-index plus path-proof coherence.  
    
* Source-precedence proof MUST treat validated v2 and v1 YAML specifications as first-order vendor-contract evidence, rendered endpoint pages as second-order evidence, and high-level guide pages as third-order evidence. Suspect artifacts, including an advertised OpenAPI artifact that fails domain, title, server, or path-family validation, MUST be quarantined and MUST NOT define vendor bytes, QA obligations, or architecture conformance.  
    
* QA must preserve v2 and v1 distinction. Vendor conformance proof MUST distinguish recommended v2 chart routes from legacy v1 BodyGraph routes, and MUST NOT silently collapse v2 chart behavior into legacy BodyGraph assumptions. Exact endpoint bytes, auth header names, request-body fields, response-envelope bytes, and credential names remain routed to their single homes.  
    
* HDAPI vendor QA plans MUST use `HD_API_BASE_URL` as the canonical HumanDesignAPI base URL key. QA may check for `HDAPI_BASE_URL` only as deprecated alias, compatibility fallback, migration evidence, or drift evidence. QA MUST NOT treat `HDAPI_BASE_URL` as canonical. If `HD_API_BASE_URL` and `HDAPI_BASE_URL` both exist with conflicting values, QA must classify the result as configuration ambiguity, not product behavior failure.  
    
* HDAPI v2 request-shaping proof and v2 open-rails smoke proof MUST distinguish auth-header family. QA may record that v2 chart routes used the `Authorization` Bearer header family, that legacy v1 BodyGraph routes used the `HD-Api-Key` header family, and that `HD-Geocode-Key` was present when geocoding was required. QA MUST NOT record raw header values, raw API keys, raw bearer token values, or unredacted vendor secrets.  
    
* A wrong auth-header family is a request-shaping or auth setup failure, not vendor unavailability. If a v2 chart route is tested with the legacy `HD-Api-Key` header family, classify the finding as request-shaping or OPS setup failure. If a legacy v1 BodyGraph route is tested with the Bearer header family without an explicit future canon decision, classify the finding as legacy request-shaping or OPS setup failure.  
    
* HDAPI versioning proof must treat `HD_API_BASE_URL` as the owner of the vendor API version boundary. QA plans, OPS instructions, evidence generators, tests, and review prompts MUST NOT require hardcoded active runtime route-construction constants such as `/v1/bodygraphs`, `/v2/charts`, `/v2/charts/simple`, or `/v2/charts/coordinates`. Runtime proof should expect version-neutral resource paths such as `bodygraphs`, `bodygraphs/simple`, `charts`, `charts/simple`, and `charts/coordinates`, joined to the configured base URL without discarding, replacing, double-prefixing, or reinterpreting the configured base path.  
    
* Literal `/v1` and `/v2` strings are allowed only when classified as historical evidence text, artifact-family name, non-runtime documentation or provenance, test input proving configurable version behavior, or legacy route-family label that does not drive active runtime URL construction. If a remaining `/v1` or `/v2` string participates in active runtime URL construction, auth-header selection, QA prompt expectations, evidence-generator route construction, or test route construction, QA must classify it as architecture drift unless a later owning canon decision explicitly permits it.  
    
* Closed-rails HDAPI v2 proof shows deterministic source selection, request shaping, typed refusal, and no DNS, socket, HTTP, or other external I/O under closed rails. Closed-rails refusal proof is not a substitute for PO-authorized open-rails vendor conformance when live vendor behavior is the claim.  
    
* Open-rails HDAPI v2 vendor smoke is PO-only execution, IA-guided. Automated agents may define intent, safety rails, success criteria, evidence requirements, and rollback intent, but MUST NOT execute the vendor call, handle plaintext secrets, or claim completion without PO-run evidence.  
    
* Open-rails HDAPI v2 smoke evidence MUST be secret-safe and mechanically reviewable. At minimum, QA or OPS evidence must preserve command provenance, stdout, stderr, exit code, redacted or presence-only environment posture, request summary, result summary, classification, and checksum or path-proof coverage. OPS evidence is not QA evidence unless the governing QA plan explicitly defines how it feeds QA evaluation.  
    
* HDAPI v2 response-normalization proof MUST either show the exact adapter/schema gap or prove a bounded adapter path into the HDE BodyGraph/person/cache shape. A field-sufficiency proof that records `INSUFFICIENT_FAIL_CLOSED` remains a gap-recording proof only. It may support fail-closed posture and later adapter work, but it does not by itself prove resolver wiring, live vendor behavior, compatibility computation, mapped-cache persistence, public Reader behavior, QA PASS, OPS completion, PF09 status movement, parent-task Done, or closeout.  
    
* A deterministic v2 adapter proof may prove that a selected `ChartResult` payload maps into an HDE-resolved BodyGraph/person/cache shape when explicit internal context is supplied and no raw vendor payload is persisted. That proof remains bounded to adapter behavior unless a separate resolver, compatibility, OPS, or persistence proof is present. `ChartSimpleResult` remains insufficient for full BodyGraph-detail claims unless later evidence proves the missing detail fields are no longer required or are supplied by a governed adapter path.  
    
* A configured-v2 resolver proof may prove that `bg:resolve --source vendor --dry-run` selects the version-neutral `charts` resource, uses route-metadata auth posture, calls the deterministic v2 adapter, emits redacted request posture, and preserves explicit nonclaims. That proof does not authorize non-dry-run writes, production persistence, app-side vendor ownership, new public routes, public Reader payload changes, raw payload persistence, or broad HumanDesignAPI v2 platform conformance.  
    
* A v2-to-compat proof may prove that mapped v2 adapter outputs feed the existing internal compatibility computation path under closed rails, including two-run identity, pair-order identity, and admin/public boundary checks when those artifacts are present. It does not change public Reader bytes, create a new HTTP home, prove live vendor success, prove production deployment, or by itself perform QA PASS, OPS completion, PF09 status movement, parent-task Done, or closeout.  
    
* A bounded PO-produced open-rails smoke may prove the exact live runtime behavior it exercised, including v2 `charts` request posture, mapped adapter status, mapped-no-raw-vendor-payload cache posture, accepted compatibility path, redacted secret posture, and exit-code result when the evidence says so. It remains bounded to that smoke and MUST NOT be treated as broad HumanDesignAPI v2 platform conformance, production deployment, public Reader expansion, or app-side credential ownership.  
    
* Non-dry-run v2 chart-backed mapped-cache writes remain unproven until a future scoped implementation proves safe mapped-cache persistence. QA must keep that boundary visible: dry-run mapping, adapter-backed compatibility proof, live smoke, mapped-cache write persistence, DB read-back parity, idempotence, and production upsert authorization are separate proof classes.  
    
* HDAPI v2 error, retry, and rate-limit proof MUST avoid vendor payload echo, avoid secrets in logs, preserve deterministic typed errors, and bind any governed snapshots through the Human Evidence Index, Machine Mirror, and path-proof discipline before a token or closeout claim depends on them.  
    
* QA plans MUST NOT guess unresolved vendor-conformance facts. Unknown epic or card assignment, missing credential or config key names, unresolved v1 legacy fallback or retirement posture, absent vendor-v2 token registration, or unproven v2 response schema mapping MUST remain an open decision, doc-delta item, or `TOOLING_BLOCKED` prerequisite rather than a `PASS` claim or `FAIL_BEHAVIOR` result.  
    
* Discoverable operational unknowns for HDAPI v2 QA MUST be classified before deferral. If a missing vendor, credential, config-key, base-url, endpoint-family, account-tier, route-family, open-rails, or OPS-evidence fact can be safely discovered by the PO through bounded OPS discovery, the QA Plan or QA-readiness artifact MUST route that discovery as a dependency instead of treating the fact as automatic deferral, `PASS`, `FAIL_BEHAVIOR`, or product failure. A bounded OPS discovery task must state the exact fact to discover, why it matters, who owns discovery, whether secrets are involved, what may be recorded, what must not be recorded, the downstream PR, QA, OPS, or planning item that depends on it, and the safe evidence or summary that resolves the unknown.  
    
* Open-rails QA is allowed when live operational verification is necessary for the proof. A QA Plan may include a bounded PO-run OPS open-rails task for live vendor reachability, endpoint availability, credential-binding confirmation, account or tier posture, error-envelope confirmation, open-rails versus closed-rails contrast, or other acceptance evidence that cannot honestly be proven closed-rails only. The task MUST be PO-authorized, secret-safe, scoped to the narrow question, and mechanically evidenced. It MUST NOT become uncontrolled vendor probing, public Reader expansion, a new HTTP home, a new acceptance token, or a broader runtime-conformance claim.  
    
* An open-rails failure is not automatically a product behavior failure. QA MUST classify the failure before acting. Valid classifications include credential issue, config issue, vendor account or tier limitation, endpoint unavailability, vendor contract mismatch, request-shaping defect, response-mapping defect, infrastructure gap, rate-limit or retry posture, external outage, product implementation defect, or QA plan expectation mismatch. Do not collapse those categories into a single `FAIL_BEHAVIOR` result without proof.  
    
* No vendor-v2-specific acceptance token may be claimed unless it exists in HDE-Governance or is explicitly minted in HDE-Build Notes pending drainage. Existing token names may be consumed only with their canonical meanings.  
    
* HDAPI v2 conformance work does not create a public Reader route and does not change Reader v1 bands-only, numeric-free posture.  
    
* OpenAI, LLMs, AI agents, prompts, embeddings, chatbots, model calls, and AI enablement are outside HD Engine and Glow App runtime scope for this conformance work. Vendor documentation-discovery files such as `llms.txt` or `llms-full.txt`, and any vendor page written for AI or LLM consumers, may be used only as documentation-structure context. They MUST NOT create AI-provider config keys, credentials, rails, evidence families, acceptance tokens, QA obligations, architecture flows, or product/runtime work.

### **3.5.8 Relationship to Admin Bundle / Admin CLI / Admin GUI (forward-looking)**

Until Admin Bundle, Admin CLI, and Admin GUI surfaces are fully implemented and pinned in canon, vendor-focused PO Live QA MAY continue to use existing CLI vendor paths (for example bg:resolve \--source=vendor \--dry-run, showcompat \--source=vendor) as the primary behavioral rails, assembling any “full product payload” expectations (BodyGraphs \+ compat \+ narratives) from those primitives, with each component’s artifacts stored under its responsible `audit/qa/<epic-id>/checks/<check_id>/` directory and indexed appropriately.

Once Admin Bundle / Admin CLI / Admin GUI are available, PO Live QA sessions SHOULD migrate to using those admin surfaces as the primary vendor behavioral rails (for example a single admin bundle call for full payload), while:

* keeping Codespaces in the artifact-sink and offline analysis role defined earlier in this section, and  
    
* preserving the vendor-first constraint: the point of PO Live QA remains to exercise live vendor behavior, not to re-run identity or internal determinism checks already covered by CI/QA/infra

### **3.5.9 CLI guard tools in open-rails Live QA (informational only)**

CLI guard tools such as serializer\_grep\_guard.py and emitter\_symbol\_proof.py are designed as closed-rails determinism guards. Their canonical PASS condition (exit code 0 with no violations) belongs to the D3 guard stage in CI, not to open-rails Live QA.

Canonical role of guards (closed-rails CI) is as follows. Under closed determinism rails (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0), guard tools are expected to:

* verify that CLI/Engine code uses the canonical serializer/emitter and no ad-hoc encoders  
    
* enforce determinism env pins and wiring invariants, and  
    
* exit with status 0 when those invariants hold

The corresponding D3 guard tokens (CLI\_SERIALIZER\_GUARD\_OK, SERIALIZER\_GREP\_GUARD\_OK, EMITTER\_SYMBOL\_PROOF\_OK) are satisfied only by such closed-rails CI runs (see §9.2.11), not by Live QA in open-rails environments.

Guards in open-rails Live QA (PO/IA Codespaces) behave differently. When guards are run from a QA console whose rails are intentionally open (for example a Codespace configured as in §3.5 for PO/IA Live QA):

* the environment does not match the closed determinism rails the guards expect  
    
* the guards are expected to fail closed with a non-zero exit code (typically 1\) due to env-pin mismatch, and  
    
* the guards are expected to log that the env rails do not match their closed-rails requirements, without asserting anything about serializer/emitter wiring correctness in CI

Such runs are treated as informational env-enforcement checks only:

* they show that the guard tools correctly enforce env pins and refuse to silently “pass” under the wrong rails, and  
    
* they do not contribute to satisfying D3 guard tokens and must not be interpreted as D3 acceptance failures when the environment is intentionally open rails

QA planning and PO Live QA scope rules apply:

* Live QA plans that include guard steps in open-rails environments MUST label those steps explicitly as “open-rails guard env check (informational only)”.  
    
* Live QA plans that include guard steps in open-rails environments MUST record the decisive informational receipt at `audit/qa/<epic-id>/checks/<guard_check_id>/primary.log`, with any explicit logs, exit-code files, and notes under the same check directory, noting that exit codes reflect env mismatch, not serializer/emitter wiring.  
    
* PO Live QA plans MUST NOT require guard exit code 0 in open-rails environments.  
    
* D3 guard tokens are satisfied by CI/closed-rails runs; PO Live QA may reference CI status for those tokens rather than re-running guards under closed rails.  
    
* A guard run that fails solely because rails are open must not block PO Live QA or be treated as a product behavior failure, provided CI has already produced passing D3 guard evidence.  
    
* If Live QA discovers a guard failure that persists under closed rails (for example, by reproducing the failure in a closed-rails CI or dev environment), that failure belongs to the D3 guard tokens and must be handled as a CI/closed-rails issue, not as an open-rails Live QA responsibility.

This section keeps the separation clear: CI/closed rails are authoritative for D3 guard tokens and serializer/emitter wiring, while open-rails Live QA may invoke guards only to confirm env-pin enforcement, without treating their non-zero exit codes as D3 acceptance failures in that context.

### **3.5.10 Tooling vs behavior failures for HTTP surfaces (TOOLING\_BLOCKED)**

Ops gap / service readiness (prod/internal surfaces; normative) applies. Some HTTP surfaces (especially prod/internal endpoints) can appear “blocked” due to operational enablement gaps (unknown auth posture, unknown token sourcing, missing allowlists) rather than code regressions. QA MUST treat these as TOOLING until enablement is established.

When an HTTP surface is unreachable or returns an access error and the operational enablement posture is not established, QA MUST:

* classify the step as TOOLING\_BLOCKED or FAIL\_TOOLING (not FAIL\_BEHAVIOR), and  
    
* record it explicitly as an ops gap (missing or unclear enablement), not as a product behavior regression

Deferred-auth token sourcing contract (non-invention; normative) applies. If a runbook or tool uses an auth header (or any credential input) for an HTTP surface, it MUST state where that input is sourced from (role/owner and mechanism) and how it is enabled.

If token sourcing is not established, the runbook MUST treat the auth header as optional evidence only:

* do not require it as a prerequisite for planning or execution, and  
    
* only use it as a branch condition when the surface returns 401/403 and the runbook is explicitly testing the authenticated path

Credential values MUST never be recorded in PF19 or QA evidence; presence-only is permitted where needed.

HTTP capture hygiene (stderr separation; normative) applies. Header/body evidence artifacts MUST be parser-safe:

* header capture files intended to represent HTTP headers MUST contain only the HTTP status line and header lines  
    
* tool warnings and stderr output MUST be captured separately  
    
* if a tool emits warnings during a capture, store parser-safe headers, the response body, and stderr in separate explicitly named files under the responsible `audit/qa/<epic-id>/checks/<http_check_id>/` directory, and do not interleave stderr into the header evidence file

This rule is about evidence portability and preventing false failures in downstream validators.

Live QA steps that exercise HTTP surfaces (for example internal/dev harnesses such as /internal/dev/sampler) can fail for two very different reasons:

* Tooling/infra failures: the required HTTP service is not running, not reachable, or speaking the wrong protocol on the assumed host/port.  
    
* Behavior failures: the service is reachable and returns a valid HTTP/1.x response, but the status/body/headers do not match the expected behavior defined in the owning PF docs.

PF19 requires QA plans and logs to distinguish these cases explicitly.

HTTP tooling/infra failure (TOOLING\_BLOCKED / FAIL\_TOOLING) applies. A Live QA step that targets an HTTP surface MUST be classified as a tooling/infra failure (TOOLING\_BLOCKED / FAIL\_TOOLING) when:

* the target URL cannot be reached as a valid HTTP/1.x service (for example curl reports HTTP\_STATUS:000, “Received HTTP/0.9 when not allowed,” connection refused, or TLS handshake failure), or  
    
* the response is not a valid HTTP/1.x response with status and headers (for example raw text with no status line or no headers), and logs indicate that the intended handler was never exercised

In these cases, QA MUST:

* classify the step as a tooling/infra failure in the log header using status: FAIL\_TOOLING or status: TOOLING\_BLOCKED (per §4.4) and include a short reason, and  
    
* route the failure as an infra/service readiness remediation item (for example missing dev harness wiring, wrong port/protocol, or missing start command), not as an application behavior failure

The affected D-goal (for example “HTTP dev sampler behavior and gating”) MUST be treated as unverified in the epic’s acceptance roster:

* acceptance for that D-goal cannot be closed, and  
    
* the root cause is recorded as infra/service readiness (dev harness missing or miswired), not as an application behavior bug

QA and Leads MUST NOT:

* mark application-level behavior tokens as failed solely because the HTTP service was unavailable or speaking the wrong protocol, or  
    
* silently skip the step and treat the D-goal as implicitly passed

Instead, the D-goal remains blocked by tooling/infra until infra wiring is corrected (see §1.4 and §11.2).

HTTP behavior failure applies only when:

* the HTTP service is reachable and returns a valid HTTP/1.x response (status line, headers), and  
    
* the observed status/body/headers clearly contradict the behavior specified in the owning PF docs (titles-only), for example:  
    
  * wrong APP\_ENV gating (200 where 403 is expected or vice versa)  
      
  * missing or malformed JSON body when a JSON envelope is required, or  
      
  * incorrect header posture (Cache-Control, Content-Type, or refusal envelope mismatches)

In these cases, QA MUST:

* classify the step as a behavior failure in the log header using status: FAIL\_BEHAVIOR (per §4.4) and include a short reason, and  
    
* route the failure through the normal bug/epic remediation process (for example PF10 addendum, HDE Phased Epics update, code fixes)

Planning implications apply. Live QA plans MUST include a service readiness check (for example a simple curl health probe against the canonical dev/prod URLs defined in Glow Infrastructure and HDE-Mechanics Guide) before running behavior-focused HTTP steps. If the readiness check fails with tooling/infra symptoms (as above), subsequent behavior steps for that surface should be marked TOOLING\_BLOCKED rather than attempted blindly.

When a dev harness or HTTP service does not yet exist or is not reachable in the target environment, the corresponding D-goals in HDE Phased Epics MUST be marked as “blocked by infra/service readiness” until Glow Infrastructure and Mechanics docs define and wire the harness (see §1.4 and §11.2). QA plans must not guess ports or URLs to “work around” missing infra.

This classification keeps responsibility clear: Infra/Ops own dev harness wiring and HTTP service readiness; application teams own behavior; QA makes the distinction explicit in logs and acceptance, and does not conflate missing or miswired services with application logic failures.

## **3.6 Repo introspection before Live QA plan (d0 planning artifacts)**

Before finalizing any Live QA plan for an epic, the Implementation Agent (or QA author) **MUST** perform a short, mechanical **repo introspection** and record the results as `d0-*` planning artifacts under the epic’s QA tree.

**Intent**

* Prevent path/CLI drift between PF-Canon and the **running repo snapshot**.  
* Ensure Live QA plans reflect actual tools, configs, ignore rules, and governed artifacts that exist in the repo at the time of planning.  
* Produce mechanical planning evidence under `audit/qa/<epic-id>/` that later reviewers can consult.

**Codex Audit observed evidence (planning-time only)**

A supplied Codex Audit may support QA planning context and pre-QA repo-reality framing for existing paths, components, tests, helpers, evidence helpers, governed artifacts, index or mirror files, and expected loci that QA should later verify. Acceptable labels include “Observed Evidence (Codex Audit)” and “Observed repo reality (Codex Audit).”

Codex Audit observed evidence does not by itself prove QA PASS, acceptance-token satisfaction, Live QA execution, OPS completion, PF09 status movement, epic closure, live vendor truth, production truth, secret validity, runtime conformance beyond observed repo reality, or canon authority. Those claims still require the owning PF source, governed QA evidence, OPS evidence, PO confirmation, or later closeout evidence as applicable.

QA plan reviewers MUST NOT reject a plan solely because repo-reality context came from a supplied Codex Audit. Reviewers must block only when the observation is overclaimed beyond repo reality, materially ambiguous, stale without a planned current check, contradictory to PF10 or PF-Canon, or used as acceptance, QA, OPS, closure, PF09-drainage, canon, or live-vendor proof without the owning source.

**Audit provenance in QA planning (planning context only)**

Audit provenance may be used in QA Plans, QA Guides, review artifacts, retrospectives, proof-obligation rationale, Tracked Issues, ADR stubs, and planning notes when it explains why work exists, what prior review observed, what risk or ambiguity was surfaced, what repo area should be inspected, what PF-canon or PF09 mapping may need attention, or why a future proof obligation exists.

Audit provenance is not a blocker merely because it appears in a plan or review artifact. It becomes a blocker only when the artifact turns the audit into PR instructions, OPS instructions, step-by-step execution procedure, command source, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth without repo validation, source of invented file or path existence, required deliverable authority, privileged live action authority, or source of secrets or external state.

QA reviewers MUST distinguish audit provenance from operative task language. If audit context is needed for execution, convert it into neutral QA or implementation language such as inspect the current repo state, validate the current route policy, prove the current behavior, update governed evidence, preserve the nonclaim, or bind the evidence under the governed root.

**d0 introspection checklist**

The path examples in this checklist are schematic path classes. The approved Live QA plan MUST replace `<d0_check_id>` and every example filename with a concrete check identity and exact filename before approval.

For each epic that will have Live QA:

1. **Inspect governed config and bundles.**  
   * Run mechanical commands (for example):  
     * `ls artifacts/config`  
     * `ls artifacts/config_bundles`  
     * `ls artifacts/registry`  
   * Capture outputs as planning artifacts under, for example:  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-config-tree.txt`  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-bundles-tree.txt`  
2. **Locate guard scripts and sanity pipeline runners.**  
   * Use `ls`/`grep`/`find` to discover:  
     * CLI guard scripts (for example `serializer_grep_guard.py`, `emitter_symbol_proof.py`), and  
     * sanity pipeline runners or evidence harnesses.  
   * Capture outputs (paths and brief context) under, for example:  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-guards-tree.txt`  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-sanity-runner-notes.txt`  
3. **Verify actual CLI options via help commands.**  
   * Run the canonical `--help` or equivalent for the CLI:  
     * for example `hdctl --help`, `hdctl showcompat --help`, `hdctl bg:resolve --help`.  
   * Capture the help output (or relevant excerpts) as governed planning artifacts:  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-hdctl-help.txt`  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-showcompat-help.txt`  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-bg-resolve-help.txt`  
   * Live QA plans MUST NOT invent flags or subcommands that do not appear in the current help output.  
4. **Record environment posture and rails intent.**  
   * Capture a short, mechanical summary of the intended rails posture for Live QA in this epic (for example, “Codespaces open-rails: SAFE\_MODE=0, ALLOW\_NETWORK=1” or “CLI runs only in closed dev harness”).  
   * Use a simple command such as:  
     * `env | sort | grep -E 'SAFE_MODE|ALLOW_NETWORK|APP_ENV|HDE_BASE_URL'`  
   * Store this in `audit/qa/<epic-id>/checks/<d0_check_id>/d0-env-rails.txt`.  
5. **Verify .gitignore rails for `audit/qa/<epic-id>`.**  
   * Inspect the repo’s `.gitignore` (and any additional ignore files) to confirm that canonical QA trees under `audit/qa/<epic-id>/` are **not** ignored:  
     * there are no broad ignore patterns that match `audit/qa/**` without corresponding allow rules, and  
     * `audit/qa/<epic-id>/` is visible to git without requiring forced adds.  
   * Capture the relevant `.gitignore` excerpts and a short mechanical check under, for example:  
     * `audit/qa/<epic-id>/checks/<d0_check_id>/d0-gitignore-audit-qa.txt`  
   * Git commands MAY be used for inspection only during D0 introspection (including in the Codex prompt that produces the plan). Results are traceability-only and MUST NOT be used as gates.  
   * (for example by using `grep` and optionally `git check-ignore` to show that `audit/qa/<epic-id>` is not matched by any ignore entry; this check is informative only and MUST NOT block planning or execution).  
   * If existing ignore patterns hide canonical QA roots (for example legacy `Audit/QA/**` or `audit/qa/**` rules), the IA must:  
     * coordinate with the build/infra owner to tighten or remove those patterns so that `audit/qa/<epic-id>/` is tracked; and  
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
The bootstrap **MUST** produce one primary bootstrap log at `audit/qa/<epic-id>/checks/<tooling_bootstrap_check_id>/primary.log` that includes a header block with at least:

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
The viability check MUST record its decisive result in `audit/qa/<epic-id>/checks/<viability_check_id>/primary.log`. If its producing tool requires a separate report, that report MUST use an explicit filename in the same check directory (schematic example: `audit/qa/<epic-id>/checks/<viability_check_id>/acceptance_map_viability.log`). The report MUST include:

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
* capture that help output as governed D0 artifacts under `audit/qa/<epic-id>/checks/<d0_check_id>/` (for example `d0-hdctl-help.txt`, `d0-showcompat-help.txt`, `d0-bg-resolve-help.txt`); and  
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
  * they are governed artifacts under `audit/qa/<epic-id>/` and are subject to the mechanical evidence rules in §4.3; and  
  * they must be present **before** Live QA steps are finalized and executed.  
* Live QA plans **MUST**:  
  * reference `d0-*` artifacts when specifying paths, scripts, CLI commands, and QA trees; and  
  * revise the plan if repo introspection reveals different paths, options, harnesses, or ignore rules than canonical PF docs imply.  
* If later QA steps (for example D5/D6) discover a mismatch between the plan and actual paths/options or `.gitignore` behavior, the IA must:  
  * capture new mechanical evidence under the responsible `audit/qa/<epic-id>/checks/<check_id>/` directory or a new `dN-*` planning step, and  
  * update the Live QA plan and PF10/PF20 doc deltas accordingly, instead of continuing with stale or incorrect instructions or relying on forced git adds for QA evidence.

---

# 4\. Evidence & indexing (how to prove; titles-only for schemas)

## **4.1 Intent**

Normalize how we capture and register evidence across projects, while keeping all schemas and field definitions in their existing single homes.

PF19 defines:

* what must be captured  
    
* where it must live  
    
* how it must be kept in sync

All schema details and field shapes remain in PF12 — HDE-Schemas & Artifacts and PF09 — HDE-Build Checklist (titles-only).

## **4.2 What to capture**

Every QA run that produces governed evidence SHOULD capture at least:

* Human Evidence Index  
    
  * File: `docs/evidence/INDEX.json`  
      
  * plus its hash sentinel: `docs/evidence/INDEX.sha256`  
      
  * Indexed by human-readable keys and titles; used as the primary evidence catalog.


* Machine mirror  
    
  * File: `artifacts/evidence_index.jsonl`  
      
  * Single file for the entire repo.  
      
  * Canonical JSONL: UTF-8, compact, one LF per record.  
      
  * Unknown-key reject: any record with unexpected fields MUST fail CI.  
      
  * Field order pinned to the schema defined in PF12.


* Path proofs  
    
  * Per-artifact path proof files that show the concrete location and shape of an artifact.  
      
  * Each machine-mirror record includes a `proof_anchor` linking that record to its path-proof file.


* Conditional capture: manifest-derived release identity and external attestation (when in scope)  
    
  * When a QA plan, CI gate, or release claim depends on release identity, QA MUST treat the canonical bytes of `catalog/manifest.json` as the single tracked release-identity input and verify the derived release ID read-only.  
  * Current release-bound proof belongs to the exact-source external attestation produced and independently verified outside the tracked source checkout. The attestation MUST remain external CI or PR evidence and MUST NOT become a mutable tracked identity input.  
  * Existing checked-in EPIC022 release evidence and its companions are frozen historical capture-time records. They MUST NOT be treated as current runtime identity inputs, regenerated for each later release, or relabeled as current release attestations.  
  * Registry and configuration evidence is release-agnostic. It MUST NOT be treated as release-identity evidence or required to embed the manifest digest, release ID, or manifest-listed source identities.  
  * External-attestation presence does not create QA PASS, acceptance-token satisfaction, OPS completion, PF09 status movement, release admission, or closeout by implication. Each such claim requires its own applicable predicates and authority.  
  * Schemas, artifact fields, and ownership for external attestation and historical release evidence remain in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

## **4.3 Rules**

Evidence and indexing are governed by these rules:

* Canonical JSON note (titles-only). PF12 governs canonical JSON/JSONL (sorted keys, compact, exactly one LF). PF19’s stance is compatible with RFC 8785 (JCS) for hashable/signable artifacts; PF12 remains the source of truth. When computing hashes/signatures over JSON proofs, re-serialize with JCS (RFC 8785\) semantics to ensure byte-stable digests.  
    
* Same-PR updates (merge-blocking).  
    
  * `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` MUST be updated in the same PR as the evidence they describe.  
      
  * A PR that changes governed artifacts without updating both the human index and the mirror MUST NOT merge.


* Path-proofs required.  
    
  * Each machine-mirror record’s `proof_anchor` must point to a stored path-proof adjacent to the artifact (stat transcript). CI fails if missing.


* Governed artifact location and dual-home anchor discipline:  
    
  * Governed artifacts (primary logs, manifests, gate outputs, path proofs) must keep a single canonical home under audit/ or the applicable governed directory.  
      
  * Docs-facing anchors (INDEX.md, stable navigation pages) may reference governed artifacts, but must not copy or fork the governed bytes. Prefer pointer records that carry: canonical path, hash, and proof\_anchor.  
      
  * If an artifact is referenced from both audit/ and docs/ during drain, treat one location as canonical (usually audit/) and treat the docs location as pointer or summary. Record the dual-home condition explicitly as a doc delta so drift is visible.  
      
  * Moving or renaming governed artifacts requires updating all pointers in the same PR (evidence index, machine mirror, docs anchors) and providing an updated path proof for the new location.


* Header snapshot patterns for text posture.  
    
  * For text surfaces (e.g., Aux Text vs Aux Suppressed), maintain pinned header snapshot patterns that distinguish:  
      
    * strict posture (exact match required)  
        
    * tolerant posture (pattern-based, e.g., for dates or trace IDs)

    

  * These patterns are designed to be adopted into PF09 CI harnesses so that snapshot drift becomes a CI failure instead of a manual surprise.


* Env pins for all captures.  
    
  * All snapshot and evidence-capture commands MUST run with:  
      
    * `LC_ALL=C`  
        
    * `LANG=C`  
        
    * `TZ=UTC`

    

  * This applies to both Engine and App captures, ensuring that bytes and headers are stable across environments and CI runs.


* Mechanical QA artifacts and notes (Live QA and bootstrap).  
    
  * All Live QA and bootstrap steps for an epic MUST produce mechanical artifacts: files created by commands or scripts (for example shell/Python tools, echo/redirection, or purpose-built QA harnesses), not by manual in-editor edits.  
      
  * Manual editing of governed evidence files or QA notes in place is considered a QA failure and must be remediated by regenerating the files mechanically and preserving any prior corrupted content as separate mechanical artifacts when needed.  
      
  * For each epic, the canonical Live QA evidence root is `audit/qa/<epic-id>/`, with a lower-case `<epic-id>` (for example `hde-epic018`). Every PO- or IA-driven evidence-producing Live QA check MUST write its decisive receipt to `audit/qa/<epic-id>/checks/<check_id>/primary.log` and MUST generate at least one new mechanical artifact for the check. Required check-created outputs belong in the same check directory unless canon names a different governed family or path. This is in addition to governed artifacts under `docs/**`, `artifacts/**`, or another owner-defined evidence family that are indexed through the Human Evidence Index and Machine Mirror.  
      
  * QA notes and logs under the QA tree are part of the QA evidence. They MUST be produced mechanically and attributed to the check that created them. Put the decisive transcript in `audit/qa/<epic-id>/checks/<check_id>/primary.log`; when a separate note or capture is genuinely required, use an explicitly named, mechanically generated sidecar in the same check directory and reference it from `primary.log`. These artifacts remain subject to the same env pins and indexing rules as other governed evidence.  
      
  * Hand-editing these files is not allowed under PF19. If a check-scoped note or log is accidentally edited by hand, remediation must:  
      
    * capture the pre-remediation content mechanically into an explicitly named `original` or `corrupted` sidecar in the same check directory, and  
        
    * regenerate the live artifact through commands so that its current contents and history are reproducible from the QA plan and command transcript.

    

  * The bootstrap step for each new epic's QA plan (often labeled `d0-<id>`) SHOULD at minimum:  
      
    * create `audit/qa/<epic-id>/`, the stable root manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json`, and the bootstrap check's `checks/<check_id>/` directory with lower-case structural directory names, and  
        
    * capture mechanical environment context for that bootstrap (for example a directory tree listing, the Python version in use, and the working directory for the Codespace or QA console) in the bootstrap check's `primary.log` or explicitly named sidecars in the same check directory.

    

  * These bootstrap artifacts are governed evidence for the epic’s QA environment and must eventually be brought under the Evidence Index and Machine Mirror when they become part of the epic’s acceptance surface.  
      
  * Docs-only PR evidence posture (recommended):  
      
    * Docs-only changes that assert contract behavior, endpoint rosters, token names, or governed artifact paths SHOULD include a minimal verification proof (for example a markdown sanity check output, or a cited pass-proof excerpt for the relevant tests) captured in the PR artifacts.  
    * If a docs-only PR ships with no captured verification proof, record it explicitly as an evidence gap (do not imply green by omission) and list the follow-up action in the close report or in the epic’s debt tracking.  
    * Nice-to-have: for non-obvious doc claims, link each claim to the test or governed artifact that proves it.

    

  * Review-flagged gaps routing (recommended):  
      
    * If review identifies a concrete regression risk that is not covered by an explicit test, record it as a test-gap item and route it to the epic plan or backlog.  
    * If review identifies a release-note or migration-comms question, route it to the PO for adjudication and record the decision in the appropriate release artifact.

### **4.3.1 Provenance vs filesystem time (produced\_at\_utc vs mtime\_utc)**

QA needs to distinguish when evidence was produced from the capture-time timestamp retained in its path proof:

* produced\_at\_utc records when the evidence harness produced the governed record. It is the logical evidence refresh time.  
* mtime\_utc is capture-time provenance recorded when a path proof is produced or refreshed. It is not a portable statement about a later checkout’s filesystem metadata.

Rules (semantics from PF12 — HDE-Schemas & Artifacts):

* produced\_at\_utc MUST NOT be hand-edited. If it is incorrect or missing, rerun the authorized evidence harness.  
* mtime\_utc MUST be a valid UTC ISO-8601 timestamp (`YYYY-MM-DDThh:mm:ssZ`) with zero microseconds.  
* Git does not preserve filesystem mtimes. QA MUST NOT compare mtime\_utc with a later checkout’s `stat().st_mtime`, require equality or a monotone ordering between those values, or rewrite an unchanged proof merely to make a clone, cache restore, or CI checkout pass.  
* An unchanged proof MUST NOT be re-timestamped. When governed artifact bytes change, the authorized evidence writer MUST refresh the corresponding path proof and every affected Human Evidence Index or Machine Mirror entry from the final changed bytes.

**Whole-family same-change freshness is required (normative).** When an authorized write run changes more than one governed artifact participating in the claimed evidence family, QA MUST treat the full changed set as one same-change family.

* It is not enough to refresh only the primary artifact when another participating companion or summary changed in the same run.  
* PASS requires every changed participating artifact, its path-proof companion, and every affected Human Evidence Index or Machine Mirror entry to reflect the same authorized generation context.  
* A preserved-valid branch does not make a separately changed stale branch acceptable.  
* The authorized writer MUST converge the complete changed family and then pass its check entrypoint. Hosted CI MUST verify the committed fixed point without repairing it.

QA checks for lifecycle or OPS-managed artifacts should examine both produced\_at\_utc and mtime\_utc as provenance fields. They MUST validate field presence, required timestamp shape, and binding to the applicable generated family without using clone-local filesystem mtime as evidence.

Integrity criteria.

The canonical QA acceptance criteria for path-proof integrity are:

* Exact governed path.  
* Exact SHA-256 and exact size agreement among the artifact’s canonical bytes, the path proof, and the corresponding Machine Mirror record.  
* Presence of required companion fields and canonical field structure.  
* A valid UTC timestamp shape for mtime\_utc.  
* Exactly one path/sha256/size\_bytes triple per artifact. Multiple or conflicting hash or size pairs in one proof are prohibited.

If any portable integrity check fails, QA MUST treat the corresponding tokens, including `EVIDENCE_PATH_PROOFS_OK` and `CI_CHECK_MIRROR_SCHEMA_OK` when applicable, as not satisfied and block the epic or PR until the authorized evidence tooling is corrected and the complete affected family passes its check entrypoint.

Any future change to mtime\_utc semantics MUST be specified in PF12, reflected in this section, and accompanied by coordinated evidence-tool and test changes before QA treats the new behavior as acceptable.

### **4.3.2 PROOF\_SHA mismatch triage (CI failures)**

PROOF\_SHA mismatches are merge-blocking evidence integrity failures. A typical signature is:

* `SystemExit: PROOF_SHA: <some.path_proof.txt> expected: <sha> found: <sha>`

When this occurs, QA MUST treat it as “evidence toolchain or governed evidence is not coherent” (not as a flaky test).

Case A — Normal artifact mismatch (most common).

If the failing path-proof is for a normal governed artifact (not the mirror self-record), the most likely cause is stale or hand-edited path-proof/index/mirror content or an incomplete same-PR regeneration.

Common drift class (sha/size mismatch, not “just formatting”).

A frequent root cause is that a governed path\_proof.txt (and the corresponding mirror row) records the wrong sha256 and/or size\_bytes for an unchanged on-disk artifact. This can cause validators to fail or, worse, to certify incorrect evidence if checks are incomplete. Examples recorded during EPIC022 close-pack follow-ups include:

* ordering artifact proof drift: `artifacts/engine/order/abba_identity.bytes.path_proof.txt` recorded metadata that did not match the actual `artifacts/engine/order/abba_identity.bytes` bytes, and the mirror record required refresh to match  
    
* stale human-index proofs: `docs/evidence/INDEX.json.path_proof.txt` and `docs/evidence/INDEX.sha256.path_proof.txt` were left stale after regenerating INDEX bytes

Remediation is always the same: regenerate Index, Mirror, and path-proofs via the canonical evidence tooling until check mode passes. Do not hand-edit proofs or mirror rows to “make the error go away.”

Remediation is to regenerate governed evidence (Index, Mirror, and path-proofs) using the canonical evidence toolchain and then re-run the check sequence (write, then check) as described in §2.2.11. Do not patch the PROOF\_SHA line by hand.

Case B — Mirror self-record / evidence self-reference mismatch (high-risk special-case).

If the mismatch involves the machine mirror’s own self-record or a proof that is derived from mirror hashing semantics:

* treat it as an evidence-tooling / validator coherence issue.  
    
* any PR that changes evidence index/mirror generation or validation MUST update/confirm the dedicated regression test for self-record semantics (for example a “machine mirror self proof” test) and must include a log excerpt of that validation passing in the PR evidence.

Non-canonical mirror path warning.

PF19’s canonical machine mirror is `artifacts/evidence_index.jsonl` (single file). If CI output references a path such as `docs/evidence/INDEX.machine_mirror.jsonl.path_proof.txt`, QA MUST treat that as a contract ambiguity or mis-invocation:

* do not bind acceptance tokens to that path, and  
    
* restore the canonical posture: single mirror file at `artifacts/evidence_index.jsonl`, indexed and proven via its canonical path-proof.

Interactive-shell safety (normative; operator-facing QA instructions).

QA plans, Live QA guides, and remediation guides often include copy/paste-ready commands intended for execution in an interactive terminal session (PO or IA). Those instruction blocks MUST be “interactive-safe”:

* Do not include shell-terminating control flow in paste blocks (for example exit, return used as a hard stop, or constructs that intentionally close the operator’s shell).  
    
* If a strict enforcement check needs a failing exit status, it MUST be isolated so it cannot terminate the operator’s session. Acceptable patterns include:  
    
  * run the enforcement in a subshell and capture its exit status in the producing check's `audit/qa/<epic-id>/checks/<check_id>/primary.log` or an explicitly named sidecar in that same directory, or  
      
  * write an explicit PASS/FAIL status artifact (plus stderr/stdout captures) and let the operator continue the session.


* Operator-facing instructions MUST treat “session survival” as a first-class constraint: evidence capture MUST continue even when a check fails.

This rule is about runbook safety and evidence completeness. It does not weaken any QA predicates or acceptance criteria.

## **4.4 QA evidence file structure and step logs**

PF19 expects QA evidence to be not only complete and indexed (§4.2–§4.3), but also reviewable. QA Plans and Live QA runs MUST adopt a consistent step-log structure under the epic’s QA root inside the governed audit tree.

### **4.4.1 Epic QA root and current-state posture (normative)**

Epic QA root (canonical): `audit/qa/<epic-id>/`

Current-state is canonical. QA evidence is governed primarily as stable, check-scoped current-state evidence under the epic QA root. Run-id discipline is not a correctness mechanism, and per-run nesting is disallowed for canonical Live QA evidence.

What PF19 requires at the epic root:

* A per-epic step-log manifest at: `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
    
* Canonical per-check primary logs referenced by that manifest (see §4.4.3).  
    
* Epic-level QA ledger artifacts (token or evidence matrix, viability log) as applicable, with titles-only routing to their owning PFs.

Each check’s canonical evidence MUST live under `audit/qa/<epic-id>/checks/<check_id>/`. Plan-created deliverables are allowed, but they MUST live under the stable check directory for the step that creates them unless canon names a different governed family or path.

Reviewers MUST be able to evaluate current-state evidence without hunting across ad hoc trees.

Final review report sufficiency for executed step clusters. A final QA review report, closeout review, or step-cluster review that asks the reviewer to approve PASS for executed Live QA steps MUST surface the current manifest entry, canonical primary-log header, `captured_env`, `evidence_artifacts`, `intended_tokens`, `claimed_tokens`, and path-proof binding for every executed step cluster it asks the reviewer to approve. A report that summarizes a result as PASS without surfacing those proof surfaces is insufficient for final PASS review, even when the result JSON itself says PASS.

### **4.4.2 Checks-only canonical layout (clarification)**

Under `audit/qa/<epic-id>/`, canonical Live QA evidence is organized only by `check_id`.

* Canonical check directories: `audit/qa/<epic-id>/checks/<check_id>/`

Per-run directories, run-id directories, timestamped run roots, or fresh directories for a given run are non-conforming for canonical Live QA evidence and MUST NOT be required by plans, prompts, or reviews.

Auxiliary materials may exist only when canon or the plan explicitly requires them, but they do not change the check-centric layout and they are not a substitute for required primary logs or manifest entries.

Tools and reviewers MUST NOT infer run history or current status by enumerating subdirectories. The per-epic manifest and the canonical check directories are the authoritative current-state evidence surfaces.

### **4.4.3 Per-epic QA step logs manifest (qa\_step\_logs\_manifest.json)**

Canonical path: `audit/qa/<epic-id>/qa_step_logs_manifest.json`

Purpose: a machine-readable index of all per-check “primary logs” under the epic’s QA root, used by review tooling and by the QA acceptance map to link checks to evidence.

Routing (normative): Live QA runbook template structure and step-log header schema are owned by PF27 — Plan Templates; this guide does not define alternate header schemas.

Requirements (normative):

* The manifest MUST be valid JSON and MUST be an object keyed by check\_id.  
    
* There MUST be at most one entry per check\_id.  
    
* Each entry MUST include:  
    
  * check\_id  
  * log\_path (the full repository-relative path `audit/qa/<epic-id>/checks/<check_id>/primary.log` to the canonical primary log)  
  * status — the canonical step status for that check.  
  * status MUST match the first-line header status in the referenced primary.log for that check.


* `log_path` MUST be a full repository-relative path under `audit/qa/<epic-id>/checks/<check_id>/` and MUST point to that check's `primary.log`.  
    
* Plans and runbooks MUST NOT mint required artifact paths. A log\_path entry MUST point to a real canonical primary log produced by the corresponding check, under the governed QA root.  
    
* If a required log path is missing at evaluation time, it MUST be treated as a tooling/prerequisite failure (e.g., TOOLING\_BLOCKED for missing prerequisite inputs/artifacts, or FAIL\_TOOLING when the harness/tooling fails), not FAIL\_BEHAVIOR.  
    
* Plans MUST distinguish pre-existing inputs (which may be presence-checked before running a step) from QA-produced artifacts (which MUST NOT be required to exist prior to the step that produces them).  
    
* This manifest is current-state only. Old run logs may be retained under `runs/<run_id>/<RUN_SUBPATH>`, but are non-canonical and MUST NOT be referenced by log\_path.  
    
* A uniqueness validation failure (duplicate check\_id keys) is a FAIL\_TOOLING / TOOLING\_BLOCKED condition. Downstream tools MUST NOT consume a manifest that violates uniqueness.

Bounded step-cluster manifest generation (normative).

A manifest and its path proof MAY be generated before every planned check has executed when a bounded review requires a current proof surface for a named executed cluster. This posture is valid only when:

* every executed check inside the reviewed cluster has one canonical manifest entry and corresponding primary log;  
* no unexecuted check is represented as executed or PASS;  
* the review record or shared summary explicitly identifies every remaining planned check as `NOT RUN` and outside the reviewed cluster;  
* the record states truthfully which generation and finalization phases ran and which did not; and  
* every failed, blocked, or pre-routing receipt relevant to the reviewed cluster remains preserved.

Partial-cluster generation establishes only the current-state proof surface for the named executed cluster. It MUST NOT by implication establish manifest finalization, ledger-bound or close-pack posture, whole-plan PASS, acceptance-token satisfaction, closeout readiness, or epic closure. The bounded review remains subject to §4.4.1 and to the manifest ledger-coverage proof below for every claim it actually makes.

Manifest ledger-coverage proof (normative).

* When a check, close-pack step, or review claims that `qa_step_logs_manifest.json` is ledger-bound or governed evidence for the current epic QA root, PASS requires explicit lookup proof that the current manifest is discoverable in the canonical evidence updater/source, the Human Evidence Index, and the Machine Mirror.  
    
* Presence on disk, a refreshed `qa_step_logs_manifest.json.path_proof.txt`, or a manifest entry alone is not sufficient for this claim.  
    
* If any required lookup is missing, the affected step MUST be classified as `TOOLING_BLOCKED` or `FAIL_TOOLING` according to the failure cause, and the manifest MUST NOT be over-claimed as ledger-coherent or close-pack-ready.

### **4.4.4 Primary step logs (one per check\_id; canonical)**

One primary log per check.

For each QA check that produces evidence, there MUST be exactly one canonical primary log referenced by the manifest for that check\_id.

Canonical path (normative; KISS default for Live QA checks): `audit/qa/<epic-id>/checks/<check_id>/primary.log`

This primary.log plus qa\_step\_logs\_manifest.json requirement applies even when a step is posture-only / TOOLING\_BLOCKED (for example when validation logic is not yet implemented): the canonical primary.log MUST still be emitted and the manifest MUST still be updated.

For posture-only / TOOLING\_BLOCKED steps, intended\_tokens and claimed\_tokens MUST be empty (or omitted) and MUST NOT claim acceptance tokens.

Example of a posture-only `check_id`: `d22-canonical-json-gate-structured-record`.

For Live QA checks, the manifest `log_path` MUST point to `audit/qa/<epic-id>/checks/<check_id>/primary.log`. If a canon-governed evidence family defines a different primary-log location, treat that location as canonical and use its full repository-relative path in the manifest.

Non-empty requirement.

The primary log MUST be a non-empty, LF-terminated text file. It MUST NOT be zero bytes.

If a step fails to complete or tooling fails, the primary log MUST still be written and MUST contain:

* a short summary of what the check attempted, and  
    
* a terse failure description and final status line consistent with the status semantics below.

Empty files.

Governed Live QA evidence files (primary logs, env snapshots, planning outputs) MUST NOT be empty. If a planned artifact is not produced, the file MUST be absent rather than present with size 0\.

Path-proofs and Machine Mirror records MUST NOT point to zero-byte QA artifacts.

Exception: clearly marked sentinel markers MAY be empty but MUST NOT be referenced by the Human Evidence Index or Machine Mirror, and MUST NOT be used as governed evidence for any QA token.

### **4.4.5 Step log header (required fields; token semantics are claims-safe)**

Header normalization (allowed; reviewer-of-record; no rerun required).

If a primary step-log header is missing any defaultable fields, a QA reviewer-of-record MAY mechanically normalize the header by adding the missing fields with empty defaults and re-serializing the header as canonical JSON.

Defaultable header fields (non-blocking; default to empty when omitted): pf\_refs, intended\_tokens, claimed\_tokens.

Token-claim safety (normative): token claims MUST NOT be inferred. If claimed\_tokens is missing or empty, treat the step as claiming no tokens. Normalization MAY include moving an explicitly stated claim into the correct header field (example: ensuring a stated token claim appears in claimed\_tokens), but MUST NOT introduce new claims beyond what the log already asserts.

Status vocabulary (normative): status MUST be one of PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED. Non-conforming status values MUST be normalized (or the step is not audit-usable).

Each per-check primary log MUST begin with a machine-readable header block on the first line, followed by the human-readable body.

Routing (normative): Live QA runbook template structure, the minimum step-log header schema, and the status vocabulary are owned by PF27 — Plan Templates. This guide does not define alternate header schemas.

Header writer input wiring (normative): If a Live QA plan uses a script or helper to assemble the step-log JSON header from environment variables, the plan MUST explicitly set or export the header-writer inputs per check (do not assume inherited shell state). Minimum export set (names-only): `CHECK_ID`, `CHECK_NAME`, `PASS_FAIL`, `COMMANDS_JSON`, `ARTIFACTS_JSON`, `PF_REFS_JSON`.

Evidence trust gate (clarification): A primary.log missing a canonical JSON header (or missing required header fields) is not audit-usable evidence for PASS, even if underlying tests pass. If a header is rebuilt after execution as an approved deviation, preserve the body verbatim and record the deviation; downstream consumers SHOULD treat only the first line as the authoritative header, and MUST NOT assume that subsequent JSON-looking lines are headers.

Environment variable drift (normative): Step-log header `captured_env` MUST NOT include non-canon or hallucinated keys (example: any `MODO_*` variable). If such keys exist in historical artifacts, treat them as inert noise; do not make them required rails, pins, header fields, manifests, or evidence-schema keys going forward.

Minimum header fields (Plan Templates; required):

* check\_id — stable identifier for the check.  
    
* status — a Plan Templates status value.  
    
* command — the complete command/entrypoint executed for this check (copy/paste-ready).  
    
* command\_provenance — one of `Codex prompt`, `Copy/paste from plan`, or `Explicitly created`.  
    
* If multiple commands were executed for one check, `command` MUST preserve the exact ordered sequence as one explicit command string, either as a pipeline or as an explicit `;`\-joined sequence that preserves execution order.  
    
* evidence\_artifacts — array of one or more evidence paths produced for this check. For a PASS step, this MUST include the check's own `primary.log` path.  
    
* captured\_env — structured snapshot of the rails/pins in effect for this check. At minimum, this MUST capture:  
    
  * SAFE\_MODE  
      
  * ALLOW\_NETWORK  
      
  * APP\_ENV  
      
  * LC\_ALL  
      
  * LANG  
      
  * TZ

Token fields (optional; token-relevant only):

* Token lists are optional in runbooks and logs. Plans and reviewers MUST NOT gate approval on token-list completeness. If token fields are present, they MUST be names-only and MUST match canonical token spellings (no aliases, no near-matches).  
    
* intended\_tokens — tokens the check is designed to support (names-only; optional).  
    
* claimed\_tokens — tokens actually satisfied by verified evidence (names-only).  
    
* claimed\_tokens MUST be present only when status is PASS.  
    
* If status is not PASS, claimed\_tokens MUST be omitted (or present but empty).  
    
* When both are present, claimed\_tokens MUST be a subset of intended\_tokens.  
    
* tokens — legacy alias for intended\_tokens only. It MUST NOT be interpreted as claimed/satisfied tokens.

Acceptance map — token identity and shape (normative):

* The acceptance-map artifact MUST include a top-level tokens array.  
    
* Each entry in tokens MUST be an object with a required name string field.  
    
* tokens\[\].name is the authoritative token identity. It is case-sensitive and MUST match the token registry entry exactly.  
    
* QA plans, validators, and token-evidence tooling MUST derive token identity from tokens\[\].name and MUST NOT infer token identity from matrix header labels or other non-registry aliases (for example token\_name).

Additional fields (allowed; non-gating):

* Additional header fields (e.g., pf\_refs, a human reason, or other traceability fields) are allowed, but MUST NOT be required as a plan-approval condition unless PF27 — Plan Templates is updated to require them.

Evidence-only guard proofs (normative):

* If a step claims PASS but its evidence depends on an assumption that could be false (e.g., “no output means success”), the step MUST include an explicit guard proof in the log body (e.g., a command that would have produced output on failure).

Unregistered token handling (normative):

* If a step lists a token in intended\_tokens or claimed\_tokens that is not present in the registry:  
    
  * treat it as an invalid claim  
      
  * do not translate it into a “close” token name  
      
  * require the plan/PR to add the token to the registry (or to remove the claim)

Status usage for missing paths vs wrong behavior (PF19 interpretation):

* Missing declared prerequisites or missing required inputs/artifacts implies TOOLING\_BLOCKED (not FAIL\_BEHAVIOR).  
    
* Tool/harness failure that prevents running or evaluating the check implies FAIL\_TOOLING.  
    
* The check ran, but behavior contradicted the expected result implies FAIL\_BEHAVIOR.

### **4.4.6 Log body and supporting artifacts**

All tests and checks for a check\_id (pytest output, grep blocks, curl output, size checks, diff results) SHOULD be appended into the same primary log in a clearly structured order (for example “=== TESTS \===”, “=== INDEX/MIRROR GREPS \===”, “=== MANIFEST CHECKS \===”).

Supporting files created by the check:

* SHOULD use a tmp\_ prefix or a clearly descriptive name (for example tmp\_sampler\_request.json, tmp\_sorted\_candidates.txt), and  
    
* SHOULD be either:  
    
  * co-located with the primary log, or  
      
  * placed under a single `tmp/` subdirectory inside the check's stable directory.

A reviewer must be able to reconstruct what happened from the primary log alone, using supporting artifacts only when deeper inspection is needed.

### **4.4.7 Consolidation and QA quality**

A QA run that leaves behind multiple overlapping logs for the same check (for example multiple different log names in different folders without a manifest pointer) is poor-quality evidence.

To satisfy PF19 expectations:

* Each `check_id` must have one clearly named primary log at `audit/qa/<epic-id>/checks/<check_id>/primary.log`.  
    
* No check should leave behind floating logs in ad hoc directories without a pointer from the manifest.  
    
* QA Plans MUST reference the check\_ids and where the canonical logs will live so operators and reviewers know exactly where to look.

This structure works together with the mechanical evidence rules (§4.3) and Live QA execution deliverables (§0.4.1) to make QA runs reproducible, reviewable, and easy to audit.

## **4.5 External AI QA evidence batching (10-file limit, no zips)**

Glow external-AI review packages use a conservative, tool-independent packaging profile. Each independently reviewable slice contains no more than 10 explicitly enumerated individual files, does not rely on ZIP extraction or folder browsing, and uses small Markdown or JSON review artifacts when canonical evidence is not suitable for direct review. These are Glow project constraints, not claims about an external platform's current capabilities.

Channel constraints (normative).

For external-AI QA review flows:

* A single independently reviewable evidence slice MUST contain 10 individual files or fewer.  
    
* Every file in the slice MUST be named explicitly. A plan MUST NOT say only "send the folder," "send all logs," or equivalent.  
    
* The review package MUST be designed as if only the explicitly enumerated files are available. This planning rule does not assert that an external platform cannot browse folders.  
    
* A ZIP MAY exist for local storage or human convenience, but it MUST NOT be the primary or only external-review transport.  
    
* Canonical local evidence remains at its governed repository path and remains subject to the Human Evidence Index, hash sentinel, Machine Mirror, and path-proof rules owned elsewhere. These packaging rules do not reduce the required local evidence set.

Step-level evidence sets.

For any QA step or Live QA slice intended for external-AI review, the QA Plan MUST:

* list the exact fully qualified paths and filenames in each review slice, for example `audit/qa/<epic-id>/checks/<check_id>/primary.log` and explicitly named check-scoped supporting files;  
    
* confirm that each slice contains 10 files or fewer; and  
    
* avoid vague folder, wildcard, or "all logs" instructions.

If the evidence needed for a truthful verdict does not fit in one slice, the author MUST either:

* construct a deterministic derived Markdown or JSON artifact that preserves every decisive predicate and exact source relationship; or  
    
* divide the work into numbered, self-contained review slices of 10 files or fewer.

No complete verdict may be issued until every required slice has been reviewed. The file ceiling MUST NOT cause required canonical evidence to be dropped, relabeled as optional, or excluded from the acceptance basis. Missing reviewer-visible evidence needed to evaluate a predicate is an incomplete or tooling-blocked review condition, not a behavior PASS.

Review packaging MUST remain secret-safe and privacy-preserving. Prefer synthetic fixtures. Do not export plaintext secrets, access tokens, credentials, real-person birth data, raw user identifiers, unrestricted BodyGraphs, or other PII merely to make an external-AI review convenient.

Policy ownership and review cadence.

* Policy owner and accountable role: Lead Developer.  
    
* Operational enforcement: the Implementation Agent for the QA plan; the applicable component owner is responsible for the content of its review slice.  
    
* Decision date: 2026-08-11.  
    
* Scheduled review: at least once every six months; the next review is due no later than 2027-02-11.  
    
* Event-triggered review: review sooner if the external-review workflow, disclosure or privacy rules, evidence tooling, or PF19 packaging process materially changes.  
    
* A later platform capability does not silently relax this policy. Relaxation requires an explicit PF19 decision and source-backed wording.

## **4.6 Derived AI-readable evidence for HTTP response bodies**

Raw HTTP `.body` files (for example `D3_http_run1.body`, `compat_http_200.body`, or `<SOME>_prod.body`) may be canonical local evidence for HTTP behavior. Write each plan-created body under the producing check's `audit/qa/<epic-id>/checks/<check_id>/` directory and treat it as governed evidence when the owning plan or evidence contract requires that posture.

When canonical response-body evidence is not suitable for direct external review, PF19 requires a small, structured Markdown or JSON review artifact for an HTTP-centric step. This is a Glow packaging rule, not a claim about an external platform's current ability to process raw response bodies.

Scope.

This section applies to QA steps that:

* use one or more `*.body` files as acceptance evidence, and  
    
* are intended to be reviewed by an external-AI reviewer.

Raw `.body` files remain canonical local QA artifacts. A derived artifact is an additional review layer; it does not replace, rewrite, supersede, or become the canonical source artifact.

Principle.

* Raw `*.body` files MUST continue to be written and preserved at their approved governed paths.  
    
* The external-review slice SHOULD use the derived artifact instead of relying on direct review of every raw body.  
    
* Canonical evidence remains available for human audit and for every owning validator, acceptance predicate, index, mirror, hash, and path-proof requirement.

Requirements for derived HTTP review artifacts.

For each HTTP-centric QA step in scope, the QA Plan MUST define one or more derived review artifacts with all of the following properties:

* Location  
    
  * stored in the producing check's directory alongside the source bodies, for example:  
      
    * `audit/qa/<epic-id>/checks/<check_id>/<check_id>_http_bodies_review.md`, or  
        
    * `audit/qa/<epic-id>/checks/<check_id>/<check_id>_http_bodies_review.json`.


* Format  
    
  * Markdown or JSON only; no binary.  
      
  * structured so that the reviewer can evaluate every decisive predicate while retaining exact source-file relationships.

Contents (per scenario or family).

For each group of `*.body` files used in acceptance (for example, dev run1/run2, seed 111 vs 222, or `APP_ENV=prod` vs dev), the derived artifact MUST record:

* A scenario ID or name (for example `two_run_identity_dev`, `seed_111`, `seed_222`, or `prod_forbidden`).  
    
* Source files: exact filenames of the `*.body` files represented by that scenario.  
    
* HTTP outcome summary from the associated headers and QA expectations:  
    
  * status code (for example 200, 403, or 4xx/5xx), and  
      
  * how the QA Plan classified it (for example success, forbidden, or error/vendor failure).


* Shape summary:  
    
  * top-level keys present (for example `["viewer_id","candidate_ids","seed","scores"]` vs `["error","code","message"]`), and  
      
  * a one-line description of whether the body is a sampler JSON payload, vendor response, or error envelope.


* Key field relationships required by the Plan, such as:  
    
  * two-run identity: run1 vs run2 bodies are IDENTICAL or DIFFERENT,  
      
  * seed-only behavior: whether `viewer_id` and `candidate_ids` are equal and which fields changed, and  
      
  * gating: whether prod, unset, or empty bodies contain sampler JSON or an error envelope.

A SHA-256 hash for each `.body` file is recommended to support identity checks without exposing contents unless the owning plan or evidence schema makes it mandatory.

Prefer at most one or two derived review artifacts for an HTTP-centric step. If every decisive predicate cannot fit within one 10-file slice, use the deterministic derivation or numbered-slice rules in §4.5. Do not drop required bodies or predicates to meet the file ceiling.

Guidance for QA Plan authors.

When writing or updating QA Implementation Plans and Live QA Guides for HTTP-centric steps:

* explicitly list:  
    
  * the `*.body` files to be produced as local canonical evidence, and  
      
  * the corresponding derived review artifact, with a short schema describing what it records.


* In an "Evidence for external review" section, reference the derived artifact instead of requiring the raw `.body` files in the review slice. For example:  
    
  * "External-AI QA evidence for Step 2: `D3_env_rails.log`, `D3_http_bodies_review.md`, `D3_live_qa_run.log`, and the explicitly named priority JSONL summaries; raw `.body` files remain at their governed paths as backing evidence."

The derived artifact MUST remain privacy-preserving and MUST NOT calculate, reinterpret, or correct Human Design output. When the proof target is a complete internal Magic-10 result, it must preserve the exact ten-category identity and order, with every category exactly once and no extras, omissions, duplicates, defaults, or harmony-only substitution. A public Reader v1 review must preserve its narrower numeric-free public projection. The derived layer must not blur those surfaces.

This requirement does not change the underlying acceptance criteria for HTTP surfaces. It provides a deterministic, structured review layer while preserving the complete canonical evidence and its owning contracts.

# 5\. Component playbooks (how to run QA per surface)

Each playbook follows the same pattern: Intent · Inputs · Steps · Evidence · Tokens (names-only) · Failures to watch · Where it lives (titles-only).

PF19 describes how to run QA; all bytes, schemas, and detailed policy live in their single-home PF docs (titles-only).

## **5.1 HD Engine — Catalog/A7 (HDE-specific)**

HDE-specific; bytes and policy live in PF05 — HDE-CLI-API-Vendor-Ref, PF04 — HDE-Governance, and PF12 — HDE-Schemas & Artifacts (titles-only).

Within PF19, §5.1 is the authoritative detailed Catalog/A7 QA playbook. Section 6 remains physically present pending a separate preservation-complete drainage and is non-authoritative where it conflicts with §5.1 or the external owning canon. This selection does not delete any §6 content.

### **Intent**

Prove the A7 transport posture of the Catalog JSON success route for the HD Engine and capture machine-checkable evidence.

Scope is Catalog JSON success route only (the Catalog/A7 surface).

/internal/version and any other ops or Aux endpoints are explicitly excluded from A7.

### **Inputs**

* A staging or prod-like environment where the Catalog JSON success route is reachable.  
    
* Env pins applied for all captures:  
    
  * `LC_ALL=C`  
      
  * `LANG=C`  
      
  * `TZ=UTC`


* The current Endpoint Catalog entry (by title only) that identifies the route and its env-gate.

  ### **Steps**

* Probe the Catalog JSON success route.  
    
  * Send a GET request to the cataloged JSON success route.  
      
  * Confirm:  
      
    * 200 status  
        
    * JSON body  
        
    * headers consistent with PF05/PF04 (titles-only)


* Capture GET headers and body.  
    
  * Record the full header block and body bytes for the 200 response.  
      
  * Ensure the body is LF-terminated and matches the canonical JSON rules.


* Capture HEAD posture.  
    
  * Send HEAD to the same route.  
      
  * Confirm:  
      
    * 200 status  
        
    * headers mirror the GET response where required (Content-Type, validators)  
        
    * Content-Length equals the identity 200 body length


* Capture 304 behavior.  
    
  * After a prior 200 response provides a strong, quoted ETag, replay GET with a matching `If-None-Match` value to elicit a 304\.  
      
  * Confirm 304:  
      
    * has no body  
        
    * omits both Content-Type and Content-Length  
        
    * preserves validators and Vary as required

    

  * Omit both Content-Type and Content-Length; include validators only.  
      
  * The omission of both `Content-Type` and `Content-Length` is the stricter Glow A7 contract; it is not a claim that HTTP generally forbids either field on every 304 response.


* Verify strong, quoted ETag.  
    
  * Confirm ETag is:  
      
    * present on 200  
        
    * derived from the LF-terminated body  
        
    * in the form "\<etag\>" (quoted strong ETag)

    

  * Confirm ETag remains stable across repeated GETs with unchanged content.


* Verify Vary and encoding-invariance.  
    
  * Confirm Vary: Authorization, Accept-Encoding (or equivalent) is present.  
      
  * Exercise accepted encodings (e.g., identity vs gzip) and prove:  
      
    * ETag does not change with encoding  
        
    * effective Content-Length (after decoding) remains consistent

    

  * `Content-Length` on HEAD MUST be present and equal the identity GET body length.


* Capture env-gate proof.  
    
  * Produce a headers-only log showing that:  
      
    * only the expected cataloged routes are reachable in this environment  
        
    * non-prod entries in the Catalog are not reachable in prod


* Build composite A7 proof JSON.  
    
  * Generate a single composite JSON proof object (or records-only JSONL) with:  
      
    * route\_path  
        
    * env\_gate  
        
    * GET, HEAD, 304 header captures  
        
    * ETag and Vary fields  
        
    * encoding\_invariance\_ok flag

    

  * Validate this proof against the schema in PF12 (titles-only).

These steps are normative proof requirements. At repository commit `4b7d57a91c43607fc2df1c63e88df334131f0321`, `adapter/http_reader.py` statically shows matching `If-None-Match` handling, removal of `Content-Type` and `Content-Length` on 304, and HEAD `Content-Length` derived from the identity body length. Static inspection does not prove deployment, route reachability, middleware behavior, test passage, or live conformance.

### **Evidence**

* Headers and body snapshots for:  
    
  * GET 200  
      
  * HEAD 200  
      
  * 304 (no body)


* A composite A7 proof JSON (or JSONL) capturing all required fields.  
    
* An env-gate proof artifact showing non-prod entries unreachable in prod.  
    
* Updated entries in:  
    
  * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
      
  * artifacts/evidence\_index.jsonl


* Index updates must be in the same PR that introduces or refreshes these artifacts.

  ### **Tokens (names-only)**

The following tokens are typically used to gate A7 completion (definitions live in PF04/PF09):

* `A7_GET_QUOTED_ETAG_OK`  
    
* `A7_HEAD_PARITY_OK`  
    
* `A7_304_OMITS_CT_CL_OK`  
    
* `A7_VARY_AUTH_AE_OK`  
    
* `A7_ENCODING_INVARIANCE_OK`

  ### **Failures to watch**

* Catalog route not reachable or returns incorrect status (non-200) for GET.  
    
* Missing or unquoted ETag, or ETag that changes with encoding.  
    
* HEAD response that diverges from GET posture (wrong Content-Type or Content-Length).  
    
* 304 response that incorrectly includes Content-Type or Content-Length, or carries a body.  
    
* Missing or incorrect Vary: Authorization, Accept-Encoding.  
    
* Composite proof JSON missing required fields or failing PF12 schema validation.  
    
* Evidence captured but not indexed in both human and machine indices in the same PR.

  ### **Where it lives (titles-only)**

* Transport bytes and route contract: PF05 — HDE-CLI-API-Vendor-Ref  
    
* A7 policy and governance details: PF04 — HDE-Governance  
    
* Proof JSON schema, mirror schema, and evidence plumbing: PF12 — HDE-Schemas & Artifacts

## **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**

Cross-component; Aux bytes and emitter behavior live in HDE-CLI-API-Vendor-Ref and HDE Narratives Guide (titles-only). A7 remains Catalog-only; Aux HEAD/304 are out of scope.

### **Intent**

Prove that Aux narrative text and Aux suppression behave correctly at the shared emitter level, and that CLI preview reflects the same bytes.

This playbook is about:

* a minimal but strict header posture for Aux, and  
    
* ensuring the CLI uses the same emitter and cannot silently “suppress” narratives due to missing tuples or mis-wired composition.

  ### **Inputs**

* A staging or prod-like environment where Aux can be invoked via BE/CLI.  
    
* Env pins for all captures:  
    
  * `LC_ALL=C`  
      
  * `LANG=C`  
      
  * `TZ=UTC`


* A validated-tuple QA harness (CLI or script) that:  
    
  * calls the shared Aux emitter for a known test pair, and  
      
  * can emit header snapshots for text and suppression cases.

  ### **Scope**

For EPIC-010, post-commit Aux QA covers two snapshots only:

* tests/transport/headers/aux\_text\_200.snap  
    
  * 200, LF-terminated text body, quoted strong ETag over that body.


* tests/transport/headers/aux\_suppression\_200.snap  
    
  * 200, empty body, no ETag.

Aux HEAD/304 are not part of A7; A7 remains Catalog-only.

### **Steps**

* Run the validated-tuple QA harness for Aux Text.  
    
  * Invoke the harness to produce an Aux text response for a known test tuple.  
      
  * Confirm:  
      
    * 200 status  
        
    * Content-Type and Cache-Control per policy (titles-only)  
        
    * LF-terminated text body present  
        
    * strong, quoted ETag derived from the LF body

    

  * Save the full header block (and, if applicable, a checksum of the body) as tests/transport/headers/aux\_text\_200.snap.


* Run the validated-tuple QA harness for Aux Suppression.  
    
  * Invoke the harness for a case that must suppress text (per PF17 rules).  
      
  * Confirm:  
      
    * 200 status  
        
    * empty body  
        
    * no ETag present  
        
    * headers otherwise consistent with suppression semantics

    

  * Save the full header block as tests/transport/headers/aux\_suppression\_200.snap.


* Verify CLI preview parity.  
    
  * Use the CLI to preview narratives for the same test cases.  
      
  * Confirm that:  
      
    * the CLI uses the same emitter as Aux (byte-identical text where applicable), and  
        
    * CLI does not show narratives when suppression rules say it should be empty.


* Check composition determinism.  
    
  * For the Aux text case, run the harness twice and confirm:  
      
    * same composition IDs and keys in the response metadata  
        
    * same text and header posture  
        
    * stable ETag

    

  * This step guards against non-deterministic composition or missing tuples.


* Update evidence indices.  
    
  * Add/update entries for the Aux snapshots (and any CLI parity artifacts, if captured) in:  
      
    * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
        
    * artifacts/evidence\_index.jsonl.

    

  * Ensure these index updates occur in the same PR as the new or updated snapshots.

  ### **Evidence**

* tests/transport/headers/aux\_text\_200.snap  
    
* tests/transport/headers/aux\_suppression\_200.snap  
    
* Optional CLI parity artifacts (e.g., artifacts/cli/aux\_preview.json) if defined in PF09/PF12.  
    
* Updated records in:  
    
  * docs/evidence/INDEX.json (plus hash sentinel), and  
      
  * artifacts/evidence\_index.jsonl


* Index updates must be in the same PR as the snapshots.

  ### **Tokens (names-only)**

Typical tokens used to gate Aux/CLI preview QA (definitions live in PF04/PF09):

* `NARR_200_TEXT_OK`  
    
* `NARR_SUPPRESSED_NO_ETAG_OK`  
    
* `ENV_LC_ALL_C_OK`

Composition identifiers, keys, text, header posture, and ETag stability across identical normalized inputs and governed state remain testable obligations. `COMPOSE_IDS_DETERMINISM_OK` is a non-token validation label unless Governance admits it; it MUST NOT be claimed as an acceptance token or silently mapped to another token.

### **Failures to watch**

* aux\_text\_200.snap missing or showing:  
    
  * no ETag  
      
  * non-quoted ETag  
      
  * body not LF-terminated


* aux\_suppression\_200.snap missing or showing:  
    
  * non-empty body  
      
  * an ETag on a suppressed response


* CLI preview diverging from Aux emitter (different text or unexpected suppression).  
    
* Non-deterministic composition IDs or ETag across repeated runs.  
    
* Evidence snapshots added without corresponding updates to the human index and machine mirror in the same PR.

## **5.3 App Backend (non-HDE endpoints)**

App-specific; these endpoints are not governed by HDE PF docs unless they proxy or surface HD Engine responses. Transport contracts for pure App APIs live in App backend API docs. HDE docs may be used as patterns, not as authority, except where the App BE directly wraps HDE surfaces.

### **Intent**

Prove that App Backend public APIs (beyond HDE) behave consistently with their own contracts, and that any endpoints which proxy HDE respect HDE’s transport posture while still being owned by the App.

This playbook focuses on:

* pinning paths/versions for App BE endpoints  
    
* capturing stable header/body snapshots  
    
* enforcing the same evidence/index parity rules used elsewhere

  ### **Inputs**

* A staging or prod-like environment exposing App BE public APIs.  
    
* A list of App BE endpoints, tagged as:  
    
  * pure App (no HDE involvement), or  
      
  * HDE-adjacent (proxying data from HDE surfaces).


* Env pins for all captures:  
    
  * `LC_ALL=C`  
      
  * `LANG=C`  
      
  * `TZ=UTC`

  ### **Scope**

In scope:

* Public App BE APIs that clients call directly.  
    
* Integration behavior where App BE endpoints wrap or proxy HDE results.

Out of scope:

* HDE service routes themselves (covered under §5.1 Catalog/A7 and §5.2 Aux).  
    
* Internal-only service-to-service calls that are not part of any QA surface.

  ### **Steps**

* Pin path and version per endpoint.  
    
  * For each App BE endpoint under QA:  
      
    * record its canonical path (e.g., /api/app/matches/v1/\<PATH\_SUFFIX\>)  
        
    * record its version (path or header-based)  
        
    * confirm documentation and implementation agree on path and version


* Capture header/body snapshots (success).  
    
  * For each endpoint, send a representative success request.  
      
  * Capture:  
      
    * status code  
        
    * all response headers  
        
    * the response body (or a checksum if sensitive)

    

  * Save snapshots under a governed location, for example:  
      
    * tests/transport/headers/app\_be\_\<route\>\_200.snap, and  
        
    * tests/transport/body/app\_be\_\<route\>\_200.json (or .txt)


* Capture error posture proof.  
    
  * For each endpoint, send one or more requests that produce typed errors (e.g., validation error, unauthorized, internal error).  
      
  * Capture:  
      
    * status codes for each error case  
        
    * headers (especially Content-Type, Cache-Control, and any correlation IDs)  
        
    * error body shape (field names, numeric/non-numeric posture)

    

  * Error semantics and policies are owned by App backend governance docs; where the endpoint proxies HDE errors, make sure those error responses either:  
      
    * conform to App BE policy, or  
        
    * clearly document that they surface HDE error posture (by title-only reference to PF05/PF04).


* Check HDE-adjacent endpoints.  
    
  * For endpoints that proxy HDE (e.g., match summaries derived from Reader), confirm that:  
      
    * their upstream calls to HDE respect HDE contracts (PF05), and  
        
    * they do not weaken HDE transport posture (e.g., no adding ETags to writers, no leaking internals).

    

  * These endpoints may choose to reframe data (new JSON shape), but they must not misrepresent HDE behavior.


* Update evidence indices.  
    
  * For each new or modified snapshot, add/update entries in:  
      
    * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
        
    * artifacts/evidence\_index.jsonl.

    

  * Ensure index updates occur in the same PR as the snapshots.


* Wire CI checks (via PF09).  
    
  * Add or update PF09 CI jobs to:  
      
    * fail on missing snapshots for declared App BE endpoints  
        
    * fail on non-canonical or non-LF-terminated governed artifacts  
        
    * enforce that the Human Index and mirror entries exist for all governed App BE evidence

  ### **Evidence**

Success headers/body snapshots for each App BE endpoint:

* tests/transport/headers/app\_be\_\<route\>\_200.snap  
    
* tests/transport/body/app\_be\_\<route\>\_200.json

Error posture snapshots:

* tests/transport/headers/app\_be\_\<route\>\_4xx.snap  
    
* tests/transport/body/app\_be\_\<route\>\_4xx.json

Index updates in:

* docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
    
* artifacts/evidence\_index.jsonl

All of the above must be present in the same PR as the code/config changes they describe.

### **Tokens (names-only, App BE pattern)**

Exact token names for App BE QA live in App-specific governance/build docs. PF19 recommends patterns such as:

* `APP_BE_ROUTE_200_OK`  
    
* `APP_BE_ERROR_POSTURE_OK`  
    
* `APP_BE_SNAPSHOTS_PRESENT_OK`  
    
* `EVIDENCE_INDEX_UPDATED_OK`  
    
* `MACHINE_MIRROR_UPDATED_OK`

When App BE endpoints proxy HDE surfaces, additional HDE tokens (e.g., CLI\_READER\_PARITY\_OK) may apply, but only where those endpoints are explicitly part of HDE integration.

### **Failures to watch**

* Path or version drift (documented path/version no longer matches implementation).  
    
* Missing or stale snapshots for active endpoints.  
    
* Error responses with unexpected status codes, missing Content-Type, or bodies that do not match declared error shapes.  
    
* HDE-adjacent endpoints that:  
    
  * leak HDE internals not meant for the App layer, or  
      
  * diverge from HDE transport posture without clear App-specific policy.


* Evidence artifacts added without corresponding updates to the human index and machine mirror in the same PR.

## **5.4 App Frontend**

App-specific; this playbook is a names-only placeholder. The FE team fills in concrete tools, routes, and thresholds.

### **Intent**

Prove that the App Frontend behaves correctly at a UI level in environments used for QA:

* routing and navigation work as expected  
    
* feature flags and experiments are wired correctly  
    
* basic accessibility and performance are within agreed limits

PF19 does not define FE tools or metrics. It only standardizes that FE QA runs produce governed artifacts and that those artifacts are indexed consistently.

### **Inputs**

* A staging or prod-like FE environment (URL and build identifier).  
    
* The current FE routing and feature flag configuration (by title only).  
    
* Chosen FE QA tools or scripts for:  
    
  * routing sanity checks  
      
  * feature-flag smoke  
      
  * basic accessibility and performance probes

  ### **Scope**

In scope:

* UI-level checks for routing sanity, feature flags, core flows, and high level accessibility or performance smoke.

Out of scope:

* HD Engine routes and bytes (those live in HDE-titled PF docs).  
    
* Detailed UX specs, design review, or full accessibility audits (these are owned by product and design documents).

  ### **Steps**

* Routing sanity run.  
    
  * Execute the FE routing test suite or script for the target environment.  
      
  * Confirm that key routes load successfully (home, onboarding, match view, settings, and similar).  
      
  * Capture a concise summary and, if available, a machine-readable report (for example JSON or JUnit-style).


* Feature flag smoke.  
    
  * For the current flag configuration, run a minimal smoke test:  
      
    * each flagged feature either renders or remains hidden according to its configuration  
        
    * any experimental UI is reachable only under the expected conditions

    

  * Capture logs or reports that list which flags were exercised and with what outcomes.


* Accessibility and performance smoke.  
    
  * Run a light accessibility checker and performance probe for representative views.  
      
  * Capture:  
      
    * a summary score or classification  
        
    * key issues or warnings (names only)

    

  * Deep audits and remediation are owned by FE/product; PF19 asks only for a repeatable smoke layer.


* Update evidence indices.  
    
  * Save FE QA outputs under governed paths, for example:  
      
    * artifacts/fe/routing\_smoke\_\<env\>.json  
        
    * artifacts/fe/feature\_flags\_smoke\_\<env\>.json  
        
    * artifacts/fe/a11y\_perf\_smoke\_\<env\>.json

    

  * Add or update entries in:  
      
    * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
        
    * artifacts/evidence\_index.jsonl

    

  * Use titles-only descriptions for FE QA artifacts in the human index; schemas and mirror rules remain in PF12.

  ### **Evidence**

* FE routing smoke artifacts (for example artifacts/fe/routing\_smoke\_\<env\>.json).  
    
* Feature flags smoke artifacts (for example artifacts/fe/feature\_flags\_smoke\_\<env\>.json).  
    
* Accessibility and performance smoke artifacts (for example artifacts/fe/a11y\_perf\_smoke\_\<env\>.json).  
    
* Indexed entries in:  
    
  * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
      
  * artifacts/evidence\_index.jsonl,  
    with FE artifacts described by title only per PF12.

  ### **Tokens (names-only, FE pattern)**

Concrete token names for FE QA live in FE governance or build docs. PF19 suggests patterns such as:

* `APP_FE_ROUTING_SMOKE_OK`  
    
* `APP_FE_FEATURE_FLAGS_SMOKE_OK`  
    
* `APP_FE_A11Y_PERF_SMOKE_OK`  
    
* `EVIDENCE_INDEX_UPDATED_OK`  
    
* `MACHINE_MIRROR_UPDATED_OK`

  ### **Failures to watch**

* Core routes not reachable or redirecting incorrectly in staging or prod-like environments.  
    
* Feature flags enabled but not visible, or disabled but still rendering.  
    
* Smoke accessibility or performance checks failing beyond agreed thresholds.  
    
* FE QA artifacts stored outside governed paths (not under artifacts/\*\* or docs/\*\*).

* ## FE QA artifacts added without corresponding updates to the human index and machine mirror in the same PR.

## **5.5 DB & Vendor ingest (authoring plane → DB / sealed pack)**

Segmentation (names-only; titles-only routing) is as follows:

* HD Engine owns HumanDesignAPI vendor acquisition, request shaping, auth/header handling, BodyGraph or chart normalization, BodyGraph persistence and retrieval, and HD computation for HDE-owned flows.  
* App Backend may invoke or consume HD Engine integration surfaces and owns app-specific orchestration, but it does not become the HumanDesignAPI vendor client, raw vendor credential holder, BodyGraph normalization owner, or canonical raw vendor-data persistence owner unless a future ADR changes that boundary.

Intent is to prove that:

* HD Engine correctly owns HumanDesignAPI vendor acquisition, request shaping, auth and header handling, BodyGraph or chart normalization, BodyGraph persistence and retrieval, and HD computation for HDE-owned flows.  
* App Backend and app-facing flows consume HD Engine outputs or invoke HD Engine integration surfaces without becoming the HumanDesignAPI vendor client, raw vendor credential holder, BodyGraph normalization owner, or canonical raw vendor-data persistence owner.  
* Future Glow app integration QA must prove that the app does not bypass the HD Engine for vendor calls and must distinguish app-side UI success from HD Engine vendor acquisition proof.  
* In normal prod rails, HDE uses DB/packs or governed persisted inputs on the hot path unless an explicitly scoped vendor path is requested and rails permit it.

Scope is as follows:

* Per-call HDE data-source selection remains explicit where the owning CLI or ops contract permits it. This source selection does not create an alternate database transport.  
    
* In every environment, database connection selection is `DATABASE_URL` to the Glow-owned direct psycopg provider or a typed failure. `DATABASE_URL` is the sole endpoint key; there is no bridge fallback or alternate HTTP database transport.  
    
* `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are retired and MUST be absent. Their presence fails closed before provider construction or external I/O.

Inputs (names-only) are as follows:

* A dev/stage environment for live posture (rails open as needed) and a prod-like environment (rails closed).  
    
* Env pins for any governed capture: LC\_ALL=C, LANG=C, TZ=UTC.  
    
* Presence-only `DATABASE_URL` posture and the CLI or ops entrypoints defined by their owning canon; secret values are never captured.

### **5.5.1 Steps — A. BE ingest plane (vendor → DB / packs)**

* Run BE vendor ingest.  
    
* Keys-only logs confirm outbound vendor HTTP and DB writes / pack export.  
    
* Validate DB/pack outputs (spot-check).  
    
* Required fields, FKs, pack SHA-256s per PF12.  
    
* Index BE ingest evidence in the same PR.  
    
* Update human index \+ .sha256 and machine mirror; governed evidence roots only (roots must be declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only).

### **5.5.2 Steps — B. HDE as consumer & vendor-capable client**

Source selection is explicit:

* Default without \--source=vendor: use DB/packs if available (no vendor call).  
    
* With \--source=vendor (or ops source="vendor"): perform live vendor call only if rails allow; otherwise return a typed refusal (keys-only).

Pre-App, no-user note: in the current pre-App posture (no app user IDs, no user-bound BodyGraphs), treat any CLI \--user value used with bg:resolve as an ephemeral QA key, not as a real app user ID. Do not treat these keys as “users in prod,” and do not use this playbook to create app-like user records.

Database connection and failure posture is as follows:

* In every environment, `DATABASE_URL` is the sole endpoint key and the Glow-owned direct psycopg provider is the sole active database transport.  
    
* `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are retired and MUST be absent. Their presence is configuration drift and MUST fail closed before provider construction or external I/O.  
    
* A missing, invalid, unavailable, or unauthorized `DATABASE_URL` MUST produce a typed failure without bridge fallback, alternate HTTP database transport, vendor routing, or inferred endpoints.

DB posture & durability (evidence) is as follows:

* Prove runtime search\_path, grants, DDL fingerprint, and (if present) read-only boundary view; store canonical artifacts under governed paths and index in the same PR.

Transport policy (vendor) is as follows:

* Where vendor is called explicitly and rails allow, retry only on network/5xx per closed policy; no jitter; record 429 as a typed outcome (no auto-succeed in this epic). Keys-only logs throughout.

Pre-App, no-user constraint (prod) is as follows: in production before the Glow App user model exists:

* Vendor QA must not exercise bg:resolve \--source=vendor \--upsert against prod; any upsert-like flow that would create rows resembling user records is out of scope for this playbook and must be owned by a future epic once the app user model is defined in HDE Phased Epics.  
    
* Vendor QA may exercise:  
    
  * closed-rails refusal posture (--source=vendor with rails closed → typed refusal, no outbound HTTP), and  
      
  * open-rails \--source=vendor \--dry-run calls that return ingest metadata and do not write DB rows.


* QA must explicitly record any requirement that assumes “existing users in prod” as blocked by environment and defer it to a later epic.

Evidence (titles/paths only; governed paths; index human+machine in same PR) is as follows:

* DB posture & durability: artifacts/db/ddl\_fingerprint.json, artifacts/db/grants.txt, artifacts/db/check\_schema.txt, optional artifacts/db/db\_rw\_smoke.log, and boundary-view proof if applicable.  
    
* Connectivity posture: secret-free evidence that `DATABASE_URL` is the only endpoint key, direct psycopg is the only selected provider, retired bridge keys are absent, and missing, invalid, unavailable, or unauthorized direct connectivity yields a typed failure without fallback.  
    
* Indexing discipline: update docs/evidence/INDEX.json \+ .sha256 and artifacts/evidence\_index.jsonl together; include proof\_anchor path-proofs; governed evidence roots only (roots must be declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only).

Tokens (names-only; definitions live in HDE-Governance / HDE-Build Checklist) include:

* DB posture & durability: `DB_SCHEMA_FINGERPRINT_OK`, `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_BOUNDARY_VIEW_OK`, `DB_WRITERS_ISOLATED_OK`.  
    
* Retired bridge names: `DEV_DB_BRIDGE_FALLBACK_OK` is not currently claimable; `DB_BRIDGE_FALLBACK_OK`, `DB_PROVIDER_PARITY_OK`, and `DB_BRIDGE_CAPS_OK` are historical non-token proof labels. Current database connection acceptance uses `DB_CONN_ENV_OK` and MUST prove the direct-only posture above.  
    
* Connectivity & errors: DB\_CONN\_ENV\_OK (presence-only selection / typed error on total failure), ENV\_LC\_ALL\_C\_OK.  
    
* Index/mirror/path-proofs: EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, CI\_CHECK\_MIRROR\_SCHEMA\_OK, CI\_CHECK\_FINAL\_LF\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK.

Failures to watch include:

* Vendor calls made without explicit \--source=vendor (or ops equivalent) or while rails are closed.  
* Missing direct-selection evidence, retired bridge keys present, an alternate-transport attempt, or a missing typed failure for unavailable direct connectivity.  
* Non-deterministic retries (jitter), 429 auto-recovery in this epic, or logs with payload/secret content.  
* Boundary proofs that can report `PASS` while unknown or unclassified adapter, presenter, public-route, serializer, external-I/O, guard-provenance, or evidence-binding categories remain unresolved. QA must classify this as proof-model failure, not live vendor runtime failure. A boundary proof may support acceptance language only when unknown categories fail closed or are explicitly classified as allowed, forbidden, unknown/fail-closed, or out of scope, and when the proof reports the current repo surfaces it actually inspected.  
* Evidence captured but not indexed (human \+ mirror) in the same PR, or mirror records without path-proofs.

### **5.5.3 Vendor dry-run QA pattern (EPIC017 example)**

For EPIC017, the historical vendor-ingest QA record used a single-command, single-artifact dry-run pattern:

* One `hdctl bg:resolve --source=vendor --dry-run` call per synthetic birth tuple and QA user key (for example `qa_epic017_vendor1`), run from a Codespace attached to the engine repository with open rails (`ALLOW_NETWORK=1`, `SAFE_MODE=0` as required).  
    
* Each call produced one resolver and ingest metadata JSON artifact under the historical `audit/qa/hde-epic017/logs/<LOG_SUBPATH>` family. This path is preserved as historical provenance and MUST NOT be copied as a current-state template; new or refreshed evidence-producing checks use the canonical check-scoped path grammar.

The resolver/ingest metadata for a successful dry-run vendor QA step is expected to show, at minimum:

* Resolver: requested\_source="vendor", resolved\_source="vendor", allow\_network=true, safe\_mode=false, dry\_run=true, upsert=false, and user\_id set to a clearly QA-scoped key (for example qa\_epic017\_vendor1).  
    
* Ingest: provider (for example hdapi), vendor\_version (version of the vendor schema), a realistic non-zero duration\_ms, and rows\_written=0, db\_rows\_after=0 for dry-run.  
    
* Parity & hashing: input\_fingerprint, payload\_sha256, and db\_emitted\_sha256 all aligned, with an explicit parity\_match=true flag indicating that “what came from the vendor” matches “what would be stored in DB shape” under non-dry-run settings.  
    
* Idempotency: a composite idempotency\_key including a UUID, provider, vendor\_version, and the input fingerprint, and a top-level status="ok".

The historical EPIC017 record treated the conditions above as satisfied when the artifact was:

* retained at its governed historical path, while any new or refreshed evidence-producing check uses `audit/qa/<epic-id>/checks/<check_id>/primary.log` and places required check-created outputs in that check directory unless an owning canon defines another family, and  
    
* properly indexed in `docs/evidence/INDEX.json` plus its hash sentinel and in `artifacts/evidence_index.jsonl`, with a co-located path proof.

That historical posture records the EPIC017 slice's intended proof: a vendor dry-run from Codespaces, no DB rows written, and payload-to-DB-shape parity for that call. It does not establish current runtime, deployment, QA PASS, token satisfaction, or deeper idempotence and multi-run behavior. Those latter predicates remain for their owning current epics and harnesses.

## **5.6 CLI/API & SDKs**

Cross-component; HDE CLI/API contracts and emitter bytes live in PF05 — HDE-CLI-API-Vendor-Ref (titles-only). Evidence plumbing for parity artifacts lives in PF12 — HDE-Schemas & Artifacts and PF09 — HDE-Build Checklist.

Intent is to prove that:

* CLI Reader bytes and CLI Aux preview behavior use their governed shared emitters.  
    
* Each supported SDK is an exact client of the Reader success and typed-error contracts; SDK-to-Aux parity applies only if that SDK exposes an Aux client.  
    
* AB/BA runs and two-run identity hold for the governed CLI outputs.  
    
* CLI preview and supported SDK calls preserve the applicable underlying HTTP emitter contract without inventing an alternate serializer, narrative emitter, fallback, or product surface.

This playbook is about transport parity and determinism, not business logic.

Inputs are as follows:

* A dev or staging environment where:  
    
  * CLI is installed and can call HDE/App surfaces.  
      
  * SDKs (if present) can call the same routes programmatically.

Current phase posture: HDE-Build Checklist — Coagulation task `HDE-COAG002` is `Not done`, and its epic or card is `Unknown`. This playbook states the Required-Now SDK Reader and error requirements; it does not claim that either SDK exists or conforms.

* Env pins for any capture: LC\_ALL=C, LANG=C, TZ=UTC.  
    
* The CLI and SDK commands/entrypoints for:  
    
  * compatibility / match display  
      
  * any Aux narrative or Reader preview functions

Scope is as follows:

* CLI parity snapshots for a fixed pair (AB and BA).  
    
* Two-run identity of CLI outputs for the same inputs.  
    
* Parity between CLI outputs and the applicable canonical Reader or Aux emitter; supported SDKs must match Reader and typed errors, and must match Aux only if an SDK Aux surface exists.

Installability and entrypoint conformance are also in scope when the epic or check claims CLI installability, command-catalog conformance, or help/version proof.

* QA MUST require positive proof for both the module-runner path and the console entrypoint. A skipped or negative console proof is not installability acceptance.  
    
* Installability, help, version, and entrypoint artifacts MUST be single-sourced and internally coherent. Conflicting summaries or duplicate payload writers are non-conforming.  
    
* Installability proof MUST NOT depend on ambient host PATH. The executed environment or captured artifacts must make the resolved CLI entrypoint path explicit and stable.  
    
* When CLI conformance artifacts are regenerated, any preserved sampler/parity artifacts plus the Human Index, the Machine Mirror, and companion path-proofs MUST be refreshed coherently in the same PR.  
    
* Packaging drift between the declared CLI entrypoint, any launcher script, and the conformance artifact generator is a QA finding and MUST be treated as non-passing until the surfaces agree.

Out of scope is as follows:

* UI formatting in terminals beyond what is required for parity proof.  
    
* Non-governed, ad-hoc scripts or experimental SDK functions.

Pre-App compat QA note (CLI-only) is as follows: in pre-App, no-user contexts, QA uses hdctl showcompat with explicit \--source=vendor and synthetic birth tuples (CLI flags and behavior defined in HDE-CLI-API-Vendor-Ref; titles-only) as the canonical way to exercise live compat behavior. In this environment:

* showcompat \--source=vendor with birth arguments and appropriate rails is the only compat CLI form that counts as a live behavior test.  
    
* showcompat runs that do not call vendor (for example, no \--source flag, or runs under closed rails that never reach vendor) are treated as local/offline math/serializer checks:  
    
  * they may be used to prove canonical JSON, determinism, or schema invariants, and  
      
  * they must be labeled as “local/offline (no vendor)” in QA plans and artifacts and must not be used to satisfy tokens whose intent is “live product behavior with vendor rails active”.


* The person\_uid values under a and b and any compat.meta identity fields in compat JSON are treated as CLI-local identifiers in this context (local/dev identity for the CLI session), not as Glow App user IDs and not as authoritative prod engine identity (which is governed by the /internal/version ops endpoint on Railway by title).

Acceptance for this specific compat Live QA step in pre-App mode is “vendor-backed compat JSON produced via \--source=vendor for the chosen births.” AB↔BA identity, Reader envelope proofs, and vendor ingest evidence are covered by separate QA steps and tokens in this playbook and elsewhere in PF19.

### **5.6.1 Steps**

* Establish a test pair and environment.  
    
  * Set env pins (LC\_ALL=C, LANG=C, TZ=UTC) for all captures.  
      
  * In pre-App, no-user contexts (no app user IDs, no user-bound BodyGraphs):  
      
    * choose synthetic birth tuples and CLI-local person labels as test inputs, and  
        
    * treat any CLI \--user values used during QA as ephemeral QA keys, not as real app user IDs.

    

  * In environments where the app user model is live and user-bound BodyGraphs exist, test IDs may include real user IDs only where those surfaces are explicitly defined by an epic in HDE Phased Epics (titles-only).


* Source selection (explicitness, vendor vs offline).  
    
  * When a DB/packs-backed BodyGraph exists and app user IDs are live:  
      
    * run CLI without \--source=vendor to exercise DB/packs; expect DB read; no vendor call in keys-only logs.  
        
    * any CLI run that uses \--source=vendor in this context must be called out explicitly in the QA plan as a vendor-backed behavior test and must obey the vendor rails and evidence rules defined in PF05/PF04.

    

  * In pre-App, no-user contexts (no DB users / no app user IDs):  
      
    * treat DB-backed, user-ID-dependent flows as blocked by environment; do not attempt to synthesize app-like user records or rely on showcompat \--user-a/--user-b \--source=db for QA.  
        
    * for live behavior tests (compat/Reader behavior in this environment), use vendor-backed compat: showcompat with birth arguments and \--source=vendor (or an equivalent vendor-only flag defined in HDE-CLI-API-Vendor-Ref).  
        
    * any invocation that omits explicit vendor source in this context is a local/offline check and cannot satisfy behavior D-goals or tokens whose intent is “live behavior with vendor rails active”.  
        
    * for local/offline checks (serializer/math, canonical JSON, AB↔BA structure, and similar), showcompat without \--source may be used under closed rails or local-only configurations, but must be labeled “local/offline (no vendor)” in QA plans and artifacts and must be routed to determinism/canonicalization tokens, not to live behavior tokens.

    

  * With \--source=vendor (or ops source="vendor") in any environment:  
      
    * when rails are open, expect a vendor call; if policy allows, results may be stored for durability in non-prod environments under governed evidence policies.  
        
    * when rails are closed, expect a typed refusal (no outbound HTTP). These runs are useful to prove SAFE/rails posture, not live vendor behavior.


* Capture CLI AB/BA snapshots.  
    
  * Produce AB and BA governed outputs (JSON or normalized) for a fixed test pair:  
      
    * in pre-App contexts, use vendor-backed compat (showcompat \--source=vendor with birth arguments) as the source of truth for AB/BA behavior runs.  
        
    * in environments with a user model and DB/packs in scope, AB/BA runs may exercise DB/packs or vendor-backed compat depending on the epic; QA plans must label which source is being exercised and whether the run is a vendor-backed behavior test or a local/offline check.

    

  * Store artifacts under artifacts/cli/\<CLI\_ARTIFACT\_SUBPATH\> and register them in the Evidence Index and Machine Mirror in the same PR (see §4.2–§4.3).


* Check AB/BA parity.  
    
  * Verify symmetry where required and correct directional swap semantics (for example, personal vs shared narratives).


* Check two-run identity.  
    
  * Re-run AB and BA; outputs must be byte-identical for governed parts (no RNG/time/FS/network leakage).


* Verify emitter parity.  
    
  * Compare CLI Reader v1 bytes produced through the governed `--dump-reader` sidecar with the Reader v1 HTTP body for the same normalized inputs and environment. `showcompat` stdout is a richer compatibility envelope and MUST NOT be required to equal the Reader six-key body.  
      
  * Compare CLI Aux preview with the canonical Aux behavior for the same normalized case: narrative text is byte-identical when text is emitted, and suppression remains suppression without placeholder prose.  
      
  * For each supported SDK, compare Reader success bytes and typed errors with the owning Reader contract. If, and only if, that SDK exposes an Aux client, also compare its success, suppression, provenance, direction, and error behavior with canonical Aux.


* Error parity (typed errors).  
    
  * Exercise:  
      
    * a forced DB-unavailable scenario, and  
        
    * a closed-rails vendor attempt (for example \--source=vendor when ALLOW\_NETWORK=0),  
      and verify CLI and HTTP error envelopes are aligned (typed, numeric-free) and respect refusal policy.


* Update CLI/API evidence indices.  
    
  * Add/update docs/evidence/INDEX.json (+ .sha256) and artifacts/evidence\_index.jsonl in the same PR for all governed CLI/API artifacts.  
      
  * Ensure each Mirror record includes a proof\_anchor to a co-located path-proof.

### **5.6.2 Evidence**

CLI AB/BA artifacts:

* artifacts/cli/compat\_ab.json  
    
* artifacts/cli/compat\_ba.json  
    
* Optional: artifacts/cli/compat\_summary.json

These should be annotated in the Human Index to indicate whether each run is vendor-backed or local/offline.

SDK parity artifacts (if applicable):

* artifacts/sdk/python\_compat\_ab.json  
    
* artifacts/sdk/typescript\_compat\_ab.json

Optional HTTP baselines:

* artifacts/http/reader\_compat\_ab.json, or  
    
* artifacts/http/aux\_ab.json

These are used internally to verify emitter parity, not necessarily shipped to users.

Indexing: all governed artifacts above must be referenced by docs/evidence/INDEX.json (+ .sha256) and artifacts/evidence\_index.jsonl, with Human Index descriptions that clearly distinguish vendor-backed vs local/offline runs (schema in PF12 by title).

### **5.6.3 Tokens (names-only)**

Common admitted tokens that may gate applicable CLI/API or SDK QA, when their exact registered predicates are proved, include:

* `COMPOSITE_ABBA_IDENTITY_OK`  
    
* `TWO_RUN_IDENTITY_OK`  
    
* `CLI_READER_PARITY_OK`  
    
* `CLI_ADMIN_BUNDLE_PARITY_OK`  
    
* `ADMIN_BUNDLE_FULL_PAYLOAD_OK`  
    
* `ADMIN_AUTH_REQUIRED_OK`  
    
* `EVIDENCE_INDEX_UPDATED_OK`  
    
* `MACHINE_MIRROR_UPDATED_OK`

`CLI_AUX_EMITTER_PARITY_OK` and `SDK_AUX_PARITY_OK` are non-token obligation labels, not admitted acceptance tokens. The CLI-to-Aux obligation remains current. SDK-to-Aux parity applies only when an SDK Aux surface exists; absence of that surface cannot support a PASS.

**Proposed token request, not currently claimable:** `SDK_READER_PARITY_OK`. Current PF04 and PF10 do not admit this name. Until Governance registers it in PF04 or mints it in a numbered PF10 addendum, SDK-to-Reader parity remains a requirement and evidence obligation only. The spelling MUST NOT appear in `claimed_tokens`, acceptance maps, manifests, token/evidence matrices, closeout claims, or `*_OK` PASS artifacts.

The future request is owned by the CLI/API and SDKs owner, requires Lead Developer review, and may be raised when `HDE-COAG002` is assigned to a real epic or card. Admission must check for conflict with existing canonical JSON, Reader parity, determinism, error-contract, and evidence tokens and must define one exact public-Reader predicate and evidence family. This proposal does not define current token semantics.

The requested future scope is limited to the public Reader contract: each supported SDK's governed success bytes match the Reader v1 six-key envelope for the same normalized inputs and environment; public output remains numeric-free and does not expose the complete internal ten-category matrix; canonical JSON and exactly one trailing LF are preserved where the owning contract requires bytes; typed errors add, omit, or rename no governed fields; and determinism and conditional-request behavior remain governed by their existing owners.

### **5.6.4 Failures to watch**

AB/BA parity failures:

* CLI outputs for AB and BA differ where they should be symmetric, or  
    
* directional narratives (for example personal vs shared) fail to swap as expected.

Two-run identity failures:

* CLI outputs differ between repeated runs with identical inputs, or  
    
* timestamps, RNG, filesystem, or network noise leaks into governed sections.

Emitter parity failures:

* CLI or SDK returns different bands, categories, or narratives than the HTTP emitter, or  
    
* missing categories or mismatched ordering relative to the emitter.

Misuse of showcompat in pre-App contexts:

* Live QA plans that attempt to satisfy behavior tokens using showcompat without \--source=vendor in pre-App, no-user environments.  
    
* QA artifacts that do not clearly label whether a compat run is vendor-backed or local/offline.

SDK-specific inconsistencies:

* SDKs applying rounding or transformations not present in the emitters, or  
    
* SDKs silently dropping fields or adding extra computed ones without canonical backing.

Evidence hygiene issues:

* Evidence artifacts added or modified without corresponding updates to the Human Index and Machine Mirror in the same PR.  
    
* Mirror records without path-proofs, or path-proofs without corresponding Mirror records.

Normative note: emitter parity is required for the surfaces that exist and are in scope. CLI Reader bytes and CLI Aux preview must match their governed emitters; supported SDKs must match Reader success and typed errors, and must match Aux only if an SDK Aux surface exists. Parity artifacts are governed evidence and must be captured and indexed accordingly.

## **5.7 Prod QA playbook for EPIC-011 (rails window)**

Anchor is “Prod QA playbook (EPIC-011 rails window)”.

Purpose: define the QA responsibilities around the short, supervised rails-open window used to validate EPIC-011 in prod, using the admin/vendor QA harness.

Single homes (titles-only) are as follows:

* Day-of runbook: docs/run/RUN\_PROD\_QA.md.  
    
* Vendor and DB call contracts: PF05 — HDE-CLI-API-Vendor-Ref.  
    
* DB posture and direct-only connectivity artifacts: PF12 — HDE-Schemas & Artifacts, PF04 — HDE-Governance, PF09 — HDE-Build Checklist.  
    
* SAFE rails policy and tokens: PF04 — HDE-Governance.

### **5.7.1 Rails-open QA window (EPIC-011)**

During EPIC-011, prod QA uses a short rails-open window with these constraints:

* Closed by default. Prod and CI run with SAFE rails closed (SAFE\_MODE=1, ALLOW\_NETWORK=0) unless a specific, approved QA job opens them.  
    
* Narrow, supervised window. For the prod QA run:  
    
  * a single admin job opens rails for a bounded duration and a fixed test corpus  
      
  * only the documented Engine/BodyGraph/vendor routes are exercised  
      
  * no ad-hoc or exploratory vendor calls are permitted


* Immediate return to closed rails. After the QA run finishes:  
    
  * rails are returned to the closed posture, and  
      
  * refusal and DB connectivity checks are run under closed rails (see below)

QA’s job is to verify that the prod QA window followed this pattern and that evidence for both the rails-open and rails-closed runs was captured and indexed.

### **5.7.2 Admin/vendor QA harness (names-only)**

The repository contains `scripts/ops/admin_vendor_qa.py` as a partial harness scaffold. It is not conforming acceptance evidence until its CLI invocation, rail and pin enforcement, canonical base-URL handling, prod command shape, and governed evidence-writing defects are resolved. Its intended behavior is to:

* fail closed unless `LC_ALL=C`, `LANG=C`, and `TZ=UTC` are explicitly set and captured before governed bytes are produced  
    
* use synthetic identities and fixed tuples (see synthetic-identity docs and PF12) to exercise:  
    
  * BodyGraph source selection and invariance  
      
  * compat math and Reader envelopes (via showcompat / Reader)  
      
  * Aux narrative previews


* record governed artifacts under artifacts/\*\* (for example CLI AB/BA/summary JSON, BodyGraph snapshots, A7 proofs)

The harness must not introduce its own retry or backoff policy; vendor SAFE behaviour and retry semantics remain defined only in PF04/PF05.

QA is responsible for:

* confirming that the harness ran with the expected env pins and rails posture  
    
* checking that the expected governed artifacts were produced and indexed (using the checklists in §9.2 and §9.5), and  
    
* treating missing or extra artifacts as QA failures, not as optional noise

### **5.7.3 Closed-rails proofs after the window**

Immediately after the rails-open run, QA must ensure that:

* a closed-rails refusal proof is captured under the path defined in PF12 (for example artifacts/proofs/ops\_refusal\_proof.txt, titles-only), and  
    
* DB connectivity evidence is captured for prod, matching `DB_CONN_ENV_OK`: `DATABASE_URL` is the sole endpoint, direct psycopg is the sole provider, retired bridge keys are absent, and missing, invalid, unavailable, or unauthorized connectivity produces a typed numeric-free failure without fallback.

Both sets of artifacts must be:

* indexed in docs/evidence/INDEX.json and mirrored in artifacts/evidence\_index.jsonl in the same PR, and  
    
* accompanied by co-located path\_proof.txt entries.

## **5.8 Admin bundle surfaces (CLI & HTTP, HDE-only)**

Cross-component; the admin bundle builder and transport bytes live in HDE-CLI-API-Vendor-Ref, HDE-Mechanics Guide, and HDE-Schemas & Artifacts (titles-only). Auth and logging rails live in HDE-Governance; infra endpoints live in Glow Infrastructure. PF19 defines how QA proves parity, full payload, and auth for these admin-only surfaces.

**Implementation posture.** The CLI command and HTTP route are Required-Now target surfaces. At repository commit `4b7d57a91c43607fc2df1c63e88df334131f0321`, `engine/cli/main.py` does not register `admin-bundle`, `adapter/http_reader.py` does not define `/internal/admin/bundle/v1`, and `docs/ENDPOINTS_CATALOG.json` has no row for that route. Until the owning implementation, configuration, and governed prerequisites exist, an attempted execution of this playbook is `TOOLING_BLOCKED`. These bounded static findings do not prove runtime, deployment, QA, acceptance, or token state.

### **Intent**

Prove that:

* the admin bundle builder composes the full product payload for a single match into one canonical JSON object  
    
* the CLI admin bundle command and the HTTP admin bundle route return the same admin bundle for the same inputs and admin credential  
    
* admin surfaces are not open: a full admin bundle cannot be obtained without the configured admin credential, and each successful call is logged as an operations event

This playbook is about pre-Glow admin/QA access to the full product payload, not about public Reader or App surfaces.

### **Inputs**

Execution prerequisites include a staging or prod-like environment where:

* the HD Engine service and DB are reachable on Railway, and  
    
* the admin bundle HTTP route is deployed

A CLI environment (Codespaces or equivalent QA console) configured, via infra canon, to reach the same Railway HD Engine prod service and DB.

A functioning admin bundle builder and its wiring in CLI and HTTP, as defined in HDE-Mechanics Guide and HDE-CLI-API-Vendor-Ref.

The CLI credential `HDE_ADMIN_TOKEN` and the server-side `HDE_ADMIN_TOKENS` and `HDE_ADMIN_SCOPES` registries configured through managed secrets per HDE-CLI-API-Vendor-Ref, HDE-Governance, and Glow Infrastructure. Secret values MUST NOT enter repository bytes or evidence.

Env pins for any governed evidence capture:

* `LC_ALL=C`  
    
* `LANG=C`  
    
* `TZ=UTC`

### **Scope**

In scope:

* The internal admin bundle builder that composes one closed `admin_bundle_v1` object with exactly the top-level keys `a_bodygraph`, `b_bodygraph`, `compat`, `meta`, `narratives`, `schema`, and `viewer_prefs`:  
    
  * complete canonical BodyGraphs for both parties,  
      
  * the full Magic-10 compat result with exactly ten ordered categories and compat meta,  
      
  * exactly three ordered narrative results for `shared`, `a_to_b`, and `b_to_a`, each preserving a valid Text or Suppressed result and its governed identity, and  
      
  * the closed meta block defined by HDE-CLI-API-Vendor-Ref, including engine, invocation, release, pack, build, emitter, input-kind, bundle-source, and rails identity.


* The CLI admin bundle command and HTTP admin bundle route that expose this builder for admin use only.

Out of scope:

* Public Reader JSON envelopes, Aux public text posture, and A7 proofs (covered in other playbooks).  
    
* Any GUI-specific behavior beyond verifying that the Admin GUI calls the admin bundle HTTP route correctly.

### **Steps**

* Admin config and handshake.  
    
  * From a QA console, perform the prod handshake described in §3.5 to confirm connectivity to the Railway HD Engine prod service.  
      
  * Verify that `HDE_ADMIN_TOKEN` is present for the CLI client and that the server registries are valid. An Admin GUI must call the route from a confidential backend; browser-delivered code MUST NOT receive or retain the admin token. Do not hard-code secrets in the repository.


* CLI admin bundle: success path.  
    
  * With env pins set and the admin credential configured, invoke `hdctl admin-bundle` for a single match.  
      
  * Pre-Glow: use one of the exact birth-tuple input forms defined in HDE-CLI-API-Vendor-Ref.  
      
  * Future user-ID inputs remain outside `admin_bundle_v1` until a later versioned contract defines them.  
      
  * Expectations for the CLI call:  
      
    * Exit status indicates success.  
        
    * Without `--out`, stdout is the exact canonical LF-terminated HTTP entity body. With `--out`, the governed output file contains those exact bytes and stdout contains only the closed receipt.  
        
    * The response has exactly the closed `admin_bundle_v1` top-level keys: `a_bodygraph`, `b_bodygraph`, `compat`, `meta`, `narratives`, `schema`, and `viewer_prefs`.  
        
    * The compat section contains exactly the full ten-category Magic-10 result in its frozen semantic order and the closed compat meta.  
        
    * The narratives array contains exactly three ordered perspective slots, each carrying a valid Text or Suppressed result without fabricated fallback prose.  
        
    * The meta block matches the closed HDE-CLI-API-Vendor-Ref schema and excludes request-specific clocks, correlation IDs, caller identity, transport headers, output paths, and other forbidden fields.

    

  * Save the CLI admin bundle JSON as a governed artifact under a path selected by its owning evidence contract, such as `artifacts/admin/cli_bundle_<pair>.json` when that path is approved.


* HTTP admin bundle: success path.  
    
  * From the same QA console, call `POST /internal/admin/bundle/v1` on the configured Railway HD Engine service with the same logical birth-tuple inputs and admin credential as the CLI call.  
      
  * The request body MUST conform to the closed `admin_bundle_request_v1` contract. User-ID inputs are not part of v1 and require a later versioned contract.  
      
  * Expectations for the HTTP call:  
      
    * Response status is 200\.  
        
    * `Content-Type` is exactly `application/json; charset=utf-8`.  
        
    * Response body is a canonical JSON object with the same top-level structure and semantics as the CLI admin bundle.

    

  * Save the HTTP admin bundle JSON under an owner-approved governed evidence path, such as `artifacts/admin/http_bundle_<pair>.json` when that path is approved.


* CLI to HTTP admin bundle parity.  
    
  * Compare the LF-terminated `admin_bundle_v1` HTTP entity body directly with the bytes copied by the CLI for the same logical inputs and environment.  
      
  * Require byte identity for the complete closed object, including BodyGraphs, viewer preferences, all ten ordered compat categories, three ordered narrative results, and the closed meta block.  
      
  * Do not pretty-print, normalize, reconstruct, or reserialize either success body for the parity decision. HTTP framing and headers, the CLI file receipt, audit records, and filesystem metadata are outside the parity subject.  
      
  * Record the byte-comparison result under an owner-approved governed path and include it in the evidence skeleton.


* Auth gating: negative tests.  
    
  * Attempt to invoke `hdctl admin-bundle` without `HDE_ADMIN_TOKEN` and with a malformed credential:  
      
    * Expect non-zero exit status and the governed `ERR_ADMIN_AUTH_REQUIRED` stderr token.  
        
    * Expect no full admin bundle JSON on stdout or in any governed output file.

    

  * Attempt to call the HTTP admin bundle route without a credential and with invalid or revoked credentials:  
      
    * Expect the governed `401` `ERR_ADMIN_AUTH_REQUIRED` response. A separately authenticated credential lacking `admin:bundle:read` must produce the governed `403` `ERR_ADMIN_BUNDLE_FORBIDDEN` response.  
        
    * Expect no full admin bundle JSON in any refusal response.

    

  * Capture these negative runs as governed evidence (for example small logs or JSON error samples) under artifacts/admin/auth\_negative/\<AUTH\_NEG\_SUBPATH\>.


* Logging and audit.  
    
  * For at least one successful CLI-mediated request and one direct HTTP admin-bundle request, verify that the server durably commits the required audit record before releasing success bytes.  
      
  * Verify the closed audit fields and values defined by HDE-CLI-API-Vendor-Ref: `at`, `caller`, `client`, `correlation_id`, `input_kind`, `outcome`, `release_id`, and `route`.  
      
  * Confirm that caller and client identity come from the trusted credential registry, that `input_kind` is the bounded contract value, and that the route identity is `internal.admin.bundle.v1`.  
      
  * Confirm audit and log records exclude raw birthdate or time, location, timezone, BodyGraphs, `person_uid`, viewer weights, narrative text, composition or fragment IDs, request or response bodies, credentials, authorization values, raw failed key IDs, output paths, vendor payloads, and remote IP addresses.  
      
  * Store a redacted sample only if its owning governance and evidence contract permits replication; otherwise record the governed audit evidence through its approved non-payload proof surface.


* Evidence and indexing.  
    
  * Register all governed admin-bundle artifacts (CLI bundle, HTTP bundle, parity proof, auth-negative samples, and any log samples) in:  
      
    * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256), and  
        
    * artifacts/evidence\_index.jsonl

    

  * Ensure these index updates occur in the same PR that adds or refreshes the artifacts.  
      
  * Ensure each mirror record has a proof\_anchor pointing to a co-located \<artifact\>.path\_proof.txt for the corresponding artifact.

### **Evidence**

Typical governed evidence for this playbook includes:

* artifacts/admin/cli\_bundle\_\<pair\>.json — CLI admin bundle.  
    
* artifacts/admin/http\_bundle\_\<pair\>.json — HTTP admin bundle.  
    
* artifacts/admin/bundle\_parity\_\<pair\>.json or equivalent small parity proof.  
    
* artifacts/admin/auth\_negative\_cli\_\<pair\>.json and artifacts/admin/auth\_negative\_http\_\<pair\>.json — negative auth samples.  
    
* Optional artifacts/admin/logs.sample — redacted operations log sample.  
    
* Updated entries in docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256) and artifacts/evidence\_index.jsonl, with mirror records and path-proofs for each governed artifact.

### **Tokens (names-only)**

This playbook primarily satisfies:

* CLI\_ADMIN\_BUNDLE\_PARITY\_OK — CLI and HTTP admin bundles match for the same inputs and admin credential.  
    
* ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK — admin bundle contains all required structural elements (BodyGraphs, compat, three narratives, meta) as defined in the owning PF docs.  
    
* ADMIN\_AUTH\_REQUIRED\_OK — admin surfaces do not yield an admin bundle without the configured admin credential; unauthenticated/mis-authenticated calls return typed errors only.

It also consumes the generic evidence tokens:

* EVIDENCE\_INDEX\_UPDATED\_OK  
    
* MACHINE\_MIRROR\_UPDATED\_OK  
    
* EVIDENCE\_PATHS\_VALIDATED\_OK  
    
* CI\_CHECK\_MIRROR\_SCHEMA\_OK

### **Failures to watch**

* The playbook is executed before the Required-Now command, route, auth registries, closed schemas, builder wiring, or governed evidence prerequisites exist; classify that condition as `TOOLING_BLOCKED`, not as behavior PASS or token satisfaction.  
    
* CLI admin bundle succeeds but is not canonical JSON (wrong encoding, unsorted keys, missing final LF).  
    
* CLI admin bundle succeeds but is missing any required closed structural element (`a_bodygraph`, `b_bodygraph`, `compat`, `meta`, `narratives`, `schema`, or `viewer_prefs`).  
    
* HTTP admin bundle succeeds but diverges from the CLI bundle for the same inputs.  
    
* HTTP admin bundle succeeds but lacks expected headers or content type.  
    
* Admin surfaces return a full admin bundle when no admin credential is presented.  
    
* Admin surfaces return a full admin bundle when an invalid or revoked credential is used.  
    
* Operations logs are missing, lack correlation IDs, or contain raw birth data, secrets, or unnecessary PII.  
    
* Admin-bundle evidence artifacts are created or updated without corresponding Human Index and Machine Mirror updates in the same PR, or without path-proofs.

# 6\. Catalog/A7 proofs (collected rules; HDE-specific bytes live elsewhere)

HDE-specific. Transport bytes and route contract live in PF05 — HDE-CLI-API-Vendor-Ref; policy and tokens in PF04 — HDE-Governance; schemas in PF12 — HDE-Schemas & Artifacts (titles-only).

## **6.1 Surface**

Surface. The only A7 proof surface is the Catalog JSON success route.

* Path: /reader (locked initially)  
    
* Env-gate: each environment has a cataloged entry; non-prod entries must not be reachable in prod.  
    
* Exclusions: /internal/version and other ops or Aux endpoints are not A7 surfaces.

### **6.1.1 Canonical Reader route and proof-route selection**

* Canonical Reader route: `/reader` (GET).  
    
* Reader v1 selection is performed via query parameter `v=1` on the Reader route.  
    
* `/api/reader` is an alias only when a given runtime mounts Reader under `/api`; it must not be treated as a distinct proof surface from `/reader`.  
    
* Aux narrative route: `/aux/narrative` (separate surface; not a Reader proof route).  
    
* Forbidden invented route: `/api/reader-proof/v1` (must not appear in QA plans, endpoint catalogs, runbooks, or proof scripts).  
    
* Proof-surface selection MUST name a reachable route for the target environment. If the Endpoint Catalog is used for routing, select the Reader route from the catalog entry and prove reachability for that route.

## **6.2 What must be captured**

For each environment where A7 is in scope, QA MUST capture:

* GET 200 headers and body:  
    
  * JSON success response (cataloged).  
      
  * Strong, quoted ETag over the LF-terminated body.  
      
  * Correct Content-Type and Cache-Control per policy.


* HEAD 200 headers:  
    
  * Mirrors GET’s validators and Content-Type.  
      
  * Content-Length equals the identity 200 body length.


* 304 Not Modified:  
    
  * Elicited after a prior 200 by presenting its matching strong quoted ETag in `If-None-Match`.  
      
  * No body.  
      
  * No Content-Type or Content-Length.  
      
  * Validators and Vary preserved as required.


* Quoted strong ETag:  
    
  * Present on 200 responses.  
      
  * Derived from LF-terminated body.  
      
  * Quoted form: "\<ETAG\>".


* Vary header:  
    
  * Vary includes at least Authorization and Accept-Encoding as required by policy.


* Encoding invariance:  
    
  * For all accepted encodings (identity/gzip/etc.):  
      
    * ETag does not change with encoding.  
        
    * Effective Content-Length (after decoding) is stable.


* Env-gate proof:  
    
  * Headers-only proof that shows:  
      
    * only cataloged routes for that env are reachable, and  
        
    * non-prod entries from the Catalog are not reachable in prod.


* Env pins for all captures:  
    
  * `LC_ALL=C`  
      
  * `LANG=C`  
      
  * `TZ=UTC`

## **6.3 Composite proof JSON**

A single composite A7 proof JSON (or records-only JSONL) MUST be produced per environment.

* Shape:  
    
  * Records-only, canonical JSON/JSONL (per PF12).  
      
  * Each record includes at least:  
      
    * route\_path  
        
    * env\_gate  
        
    * GET/HEAD/304 header snapshots  
        
    * ETag and encoding flags  
        
    * vary\_has\_auth, vary\_has\_accept\_encoding  
        
    * encoding\_invariance\_ok


* Validation:  
    
  * Validated against the composite A7 proof schema defined in PF12 (titles-only).  
      
  * CI must fail if the composite proof does not match the schema.


* Indexing (same PR):  
    
  * Composite proof JSON and all A7 header snapshots are registered in:  
      
    * docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256)  
        
    * artifacts/evidence\_index.jsonl

    

  * Index updates occur in the same PR as the proof artifacts.

## **6.4 Failures to watch**

* Missing or non-quoted ETag on GET 200\.  
    
* HEAD posture diverging from GET (wrong Content-Type or Content-Length).  
    
* 304 responses that include Content-Type, Content-Length, or a body.  
    
* Missing or incomplete Vary: Authorization, Accept-Encoding.  
    
* ETag or effective Content-Length changing with encoding.  
    
* Composite proof JSON failing PF12 schema validation.  
    
* Proof artifacts added without human index \+ mirror updates in the same PR.

# 7\. BodyGraph refresh & observability QA

Anchor: “BodyGraph refresh & observability QA”.

Purpose: make the BodyGraph evidence and privacy guarantees testable, using the governed artifacts defined in PF12.

Single homes (titles-only):

* BodyGraph schemas and artifacts: PF12 — HDE-Schemas & Artifacts.  
    
* Vendor SAFE and BodyGraph source selection rules: PF04 — HDE-Governance, PF05 — HDE-CLI-API-Vendor-Ref.  
    
* Metrics and logs privacy posture: PF04 — HDE-Governance.

## **7.1 Evidence artifacts (BodyGraph)**

QA expects the following governed artifacts (paths are normative; schema lives in PF12):

* artifacts/bodygraph/source\_selection.snapshot.json  
    
* artifacts/bodygraph/source\_invariance/ab.json  
    
* artifacts/bodygraph/source\_invariance/ba.json  
    
* artifacts/bodygraph/source\_invariance/summary.json  
    
* artifacts/bodygraph/refresh\_policy.snapshot.json  
    
* artifacts/bodygraph/metrics.snapshot.json  
    
* artifacts/bodygraph/keys\_only.logs.sample

Each artifact must be indexed in docs/evidence/INDEX.json and mirrored in artifacts/evidence\_index.jsonl with a co-located \<artifact\>.path\_proof.txt (see §4.3 and §9.2).

## **7.2 Refresh policy QA**

For refresh\_policy.snapshot.json, QA must ensure that:

* the refresh worker (or equivalent job) has been run long enough in the target environment to populate non-trivial sample\_counts (PF12 defines exact fields and semantics).  
    
* the snapshot corresponds to the same release and BodyGraph configuration that will ship.  
    
* any change to refresh policy logic or thresholds is accompanied by a new snapshot and an updated Machine Mirror record for that artifact in the same PR.

QA treats a zeroed or obviously stale sample\_counts field as a failure to meet refresh-policy QA, not as a cosmetic issue.

## **7.3 Observability and privacy QA**

For metrics.snapshot.json and keys\_only.logs.sample, QA must:

* verify that metrics cover the BodyGraph flows exercised during QA (names and labels as defined in PF12/PF04).  
    
* confirm that:  
    
  * logs are keys-only (no raw birth data, no payload bodies, no secrets)  
      
  * metrics and logs do not contain PII or secret values  
      
  * labels are bounded and match the expected dimensions (for example route, outcome, rails\_state, timeout\_profile, attempt\_idx)

If any privacy or labeling violations are found, QA blocks the release until the logging/metrics configuration is corrected and new snapshots are captured and indexed.

### **Acceptance / artifact impact**

PF19 now codifies QA expectations around the BodyGraph artifacts already defined in PF12:

* artifacts/bodygraph/source\_selection.snapshot.json  
    
* artifacts/bodygraph/source\_invariance/\*.json  
    
* artifacts/bodygraph/refresh\_policy.snapshot.json  
    
* artifacts/bodygraph/metrics.snapshot.json  
    
* artifacts/bodygraph/keys\_only.logs.sample

The BodyGraph evidence obligations above remain governed by their owning canon. PF19 MUST NOT present `BG_SOURCE_SELECTION_OK`, `BG_SOURCE_INVARIANCE_OK`, `BG_TTL_SWR_OK` or `BG_TTL_SWR_POLICY_OK`, `BG_PRIVACY_OK`, or `BG_METRICS_OK` as acceptance tokens unless it cites an exact current registry row or explicitly minting addendum for each name.

# 8\. Evidence & indexing reference (quick rules)

## Header names lower-case

All governed header snapshots store header names in lower-case; values are verbatim. Acceptance token: SNAPSHOT\_HEADER\_LOWERCASE\_OK (definition lives in PF05/PF09).

## Directory names must be lower-case ASCII (global)

All directories in the repository and application codebase MUST use lower-case ASCII names. This applies to every directory, including (but not limited to): source code, scripts, schemas, catalogs, docs, artifacts, audit trees, and QA subtrees.

Under governed evidence roots (roots declared in the Evidence Catalog in HDE Schemas & Artifacts, titles-only), introducing any mixed-case or upper-case directory name is a QA failure, not cosmetic drift. Such directories MUST be normalized to lower-case and all affected evidence paths updated (Human Evidence Index, Machine Mirror, and path-proofs) in the same PR before any dependent QA tokens can be claimed.

If mixed-case directories already exist, treat them as legacy drift and normalize them to lower-case. Do not copy them forward into new specs, QA plans, or new evidence trees.

## Gitignore rails for QA roots

Canonical QA evidence roots under audit/qa (including all per-epic trees such as audit/qa/hde-epic018) MUST NOT be hidden by .gitignore.

Broad ignore patterns that match audit/qa/\*\* are forbidden unless they are explicitly paired with allow rules that keep every canonical per-epic QA evidence root (`audit/qa/<epic-id>/`) visible to git.

When a new audit/qa/\<epic-id\> tree is introduced, the build/infra owner MUST ensure that .gitignore has no entries that match audit/qa, unless explicit allow rules keep per-epic QA evidence trees visible to git while still allowing narrowly targeted ignores for non-evidence scratch files.

Older ignore patterns for Audit/QA or audit/qa MUST be reviewed and removed or tightened if they conflict with the canonical `audit/qa/<epic-id>/` evidence-root convention.

## Same-PR rule

The Human Index (docs/evidence/INDEX.json \+ docs/evidence/INDEX.sha256) and the Machine Mirror (artifacts/evidence\_index.jsonl) MUST be updated in the same PR as any new or changed evidence artifacts.

## Single-file machine mirror

artifacts/evidence\_index.jsonl is the only mirror file; canonical JSONL; one LF per record; fixed field order; unknown-key reject; each record includes a proof\_anchor.

## Capture posture and env pins

All evidence captures run with:

* `LC_ALL=C`  
    
* `LANG=C`  
    
* `TZ=UTC`

Text surfaces (e.g., Aux Text vs Suppressed) should use strict \+ tolerant header snapshot patterns:

* strict for exact posture checks  
    
* tolerant for fields allowed to vary (dates, IDs)

These patterns are expected to be adopted into PF09 CI harnesses so drift is caught automatically.

## mtime\_utc semantics (names-only)

Where Mechanics and PF12 schemas use mtime\_utc in path-proof transcripts or evidence records, QA checks MUST treat it as capture-time provenance that:

* has a valid UTC timestamp shape with seconds precision and zero microseconds; and  
* records the timestamp retained when the proof was produced or refreshed.

QA MUST NOT compare mtime\_utc with a later checkout’s filesystem `stat().st_mtime`, require equality or monotonicity between those values, or rewrite an unchanged proof merely to satisfy a clone, cache restore, or CI checkout.

The canonical QA acceptance criteria are exact governed path, matching SHA-256 and size, required companion fields, canonical field structure, valid UTC timestamp shape, and the path proof’s single sha256/size\_bytes pair.

Any future change to mtime\_utc behavior MUST be reflected in the owning schema, the evidence tools, and their tests before QA can accept the new behavior.

# 9\. QA acceptance tokens

## **9.1 Tokens glossary (names-only; sources in PF04/PF09)**

PF19 lists names only in this glossary. Token spellings and normative definitions live in HDE-Governance and HDE-Build Checklist (titles-only). Use this section as a quick reference; QA-facing definitions and evidence mapping live in §9.2.

### **9.1.1 Pre-commit**

* `QA_PRECOMMIT_CHECKLIST_OK`  
    
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
    
* `QA_BOOTSTRAP_OK`  
    
* `QA_BOOTSTRAP_TOOLING_FAIL`  
    
* `QA_HARNESS_DISCIPLINE_OK`  
    
* `QA_ACCEPTANCE_MAP_VIABILITY_OK`

  ### **9.1.3 Aux**

* `NARR_200_TEXT_OK`  
    
* `NARR_SUPPRESSED_NO_ETAG_OK`  
    
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
    
* `CLI_READER_EMITTER_PARITY_OK`  
    
* `CLI_ADMIN_BUNDLE_PARITY_OK`  
    
* `ADMIN_BUNDLE_FULL_PAYLOAD_OK`  
    
* `ADMIN_AUTH_REQUIRED_OK`

  ### **9.1.6 Build/CI (PF09)**

* `QA_HARNESS_DISCIPLINE_OK`  
    
* `QA_HARNESS_ENTRYPOINT_SELFTEST_OK`

  ### **9.1.7 App FE/BE (App QA docs)**

PF19 lists no App-layer acceptance-token name until the exact current App QA or security owner and its versioned semantics, assessed scope, verification method, evidence family, and claim rules are available. This unavailable owner proof is a documentation dependency, not a product PASS, FAIL, waiver, or extinction of accessibility, performance, or security responsibility.

## **9.2 QA Acceptance Tokens Registry (canonical QA token library)**

### **9.2.1 Intent**

This section is the canonical QA operational library for QA Acceptance Tokens: it provides QA-facing interpretation, evidence-family bindings, and runbook implications for the acceptance tokens used across Glow epics.

Source-of-truth boundary (normative). Canonical acceptance token names and their normative semantics are owned by HDE-Governance (and, where relevant, the HDE-Build Checklist). If a token spelling is not yet present in HDE-Governance, it MUST be sourced from a PF10 — HDE-Build Notes addendum that explicitly mints the token (titles-only) until it is drained into HDE-Governance. PF19 MUST mirror canonical token names exactly and MUST NOT introduce new acceptance token names or redefine existing ones.

PF19 MAY add QA-specific evidence mappings for registered tokens, but it MUST NOT change the token definition or rename tokens.

**Deprecated alias handling (normative).** `QA_STEP_LOGS_CONSOLIDATED_OK` is a deprecated doc-only alias for `QA_HARNESS_DISCIPLINE_OK`.

* Acceptance artifacts (acceptance maps, token/evidence matrices, close-pack manifests, and QA step logs) MUST claim `QA_HARNESS_DISCIPLINE_OK` and MUST NOT claim or emit `QA_STEP_LOGS_CONSOLIDATED_OK`.  
    
* If the alias appears in a consumer doc or CI output, QA MUST normalize to `QA_HARNESS_DISCIPLINE_OK` for acceptance claims and record the legacy spelling as a doc-delta item (titles-only: HDE-Governance — Document deltas), rather than propagating the alias into acceptance artifacts.

If an apparently unregistered token name is discovered during planning or execution, record CAVEAT: UNREGISTERED\_TOKEN (or CAVEAT: UNREGISTERED\_ACCEPTANCE\_TOKEN where applicable) and do not claim that token for acceptance until it is registered in HDE-Governance or explicitly minted in a PF10 addendum (titles-only).

### **9.2.2 Token metadata model (normative)**

Each token entry in this section uses the following fields:

* Name — canonical spelling of the token as defined in HDE-Governance (source of truth). If a token spelling is not yet present in HDE-Governance, it MUST be sourced from a PF10 — HDE-Build Notes addendum that explicitly mints the token (titles-only) until drained. PF19 MUST mirror the canonical name exactly (case, punctuation). Local aliases are non-canonical and MUST NOT be used in plans, acceptance maps, or QA logs.  
    
* Meaning — short plain-English meaning. This meaning must match HDE-Governance  
    
* QA definition — QA-facing interpretation plus what must be demonstrated.  
    
* Evidence family — the governed evidence family (and canonical artifact paths) that prove the token.  
    
* Operational notes — how to run/validate in Live QA without inventing CLI or environments.  
    
* Owner/Source — where to route changes (titles-only).  
    
* Status — \[Required Now\], Optional, Deprecated.

Registry role boundary (normative). HDE-Governance remains the single source of truth for acceptance token names and normative semantics. PF19 §9.2 is the canonical QA-level home for the QA operational mapping: how each token is evidenced, where outputs are stored in the QA evidence tree, and how reviewers verify the token mechanically.

Tokens MAY be referenced in acceptance maps, manifests, and QA logs only by their canonical name as defined in HDE-Governance (and mirrored here). PF19 MUST NOT treat a provisional or unregistered token name as acceptable for an acceptance claim.

New token workflow (governance-first). If Live QA planning or evidence requirements indicate that a new acceptance token is needed:

* Record the need as a doc delta item (see the Step-0 doc delta capture step required by 14.6 Ownership and maintenance).  
    
* Obtain governance registration of the token name/semantics in HDE-Governance before the token is used for acceptance claims.  
    
* After governance registration, add/refresh the PF19 §9.2 operational entry (QA definition \+ evidence bindings) so the token can be verified mechanically.

During planning/execution, an unregistered token discovery is handled as CAVEAT: UNREGISTERED\_TOKEN (do not block runnable behavior testing), but the token MUST NOT be claimed for acceptance until registered.

#### **9.2.2.1 Token value rubric (normative)**

QA Acceptance Tokens are for enduring acceptance invariants, not for workflow state, planning placeholders, or platform metadata.

A token MAY be added to this PF19 registry only if all of the following are true:

* Value / safety invariant: It corresponds to a user-visible value, safety property, or system invariant that must be true in shipped behavior.  
    
* Testable \+ evidence-bound: It can be proven via concrete tests/CI/Live QA and governed evidence (i.e., it can be bound into §9.2.14 without inventing semantics).  
    
* Falsifiable \+ specific: It has a clear pass/fail meaning; it is not “general progress”, “documentation exists”, or “someone performed a workflow step”.  
    
* Stable semantics: It is expected to remain meaningful across epics (not just for a one-off implementation detail).

Tokens that fail this rubric MUST be captured as checklist items, step-log metadata, or process rails in their owning PF docs, and MUST NOT be minted as new QA Acceptance Tokens in this registry.

DB bridge and provider parity label posture (PF04-backed; normative). `DEV_DB_BRIDGE_FALLBACK_OK` is retired from current claimability. `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token historical proof labels only; that retirement does not mint a replacement token.

* Current implementation plans, PR summaries, OPS evidence, QA logs, acceptance maps, token-evidence matrices, and closeout artifacts MUST NOT claim any of those four names as satisfied acceptance tokens.  
* Historical artifacts MAY retain those labels as provenance and MUST NOT be rewritten solely because of the retirement.  
* Provider parity, bridge capability, and fallback proof MAY remain as historical governed evidence without claiming acceptance-token status.  
* If a new gated acceptance predicate is needed, HDE-Governance or a numbered PF10 addendum MUST define it before any current acceptance artifact claims it.

Explicit non-token examples (normative):

* Guard proofs are evidence-only deliverables unless and until HDE-Governance registers an acceptance token. Do not mint, request, or claim ad hoc “guard tokens.”  
    
* PF23 consult completion is not an acceptance token. Plans and implementations MUST NOT mint, claim, or reference REALITY\_AUDIT\_OK (or any similar “PF23 consult completion” token) unless and until HDE-Governance registers such a token.

Admission test (shortcut). If the answer to either question is “no”, the thing is not a QA Acceptance Token:

* “Would we ship if this token were not satisfied?”  
    
* “Can we prove this token without inventing new token semantics?”

#### **9.2.2.2 Token retirement rubric (normative)**

A token may be marked Deprecated when it is redundant, superseded, or no longer represents a meaningful acceptance invariant.

Retirement rules:

* Deprecated tokens MUST NOT appear in new acceptance rosters or new token/evidence matrices.  
    
* A deprecated token entry MUST remain in PF19 for traceability, with a brief deprecation note and (if applicable) a successor token named by canonical spelling.  
    
* Deprecation MUST be accompanied by a migration plan in the consuming epic artifacts (acceptance maps / manifests) so that active work is not blocked by stale tokens.

This metadata model is authoritative for QA planning and EPIC acceptance.

### **9.2.3 Pre-commit / CI QA tokens**

* `QA_PRECOMMIT_CHECKLIST_OK`  
    
  * Owner PF: HDE-Build Checklist  
      
  * Scope: Pre-commit  
      
  * QA definition: All required pre-commit checks (lint/format, canonical JSON/JSONL, determinism, env pins, mirror quick-check) have passed.  
      
  * Evidence: CI logs and artifacts showing the PF09 pre-commit harness ran successfully (lint/format jobs, canonicalization checks, determinism suites, mirror quick-checks).

**Serializer determinism QA condition (non-token).**

* Owner/source: HDE-Mechanics Guide and HDE-Schemas & Artifacts; acceptance-token semantics remain owned by HDE-Governance.  
    
* Scope: Pre-commit.  
    
* Requirement: Engine serializer and composer outputs use canonical UTF-8 JSON or JSONL as applicable, including governed key ordering, compact separators, no BOM, and the exact final-LF rule. Under declared determinism environment pins, identical inputs and governed state MUST yield byte-identical outputs; prohibited wall-clock, randomness, filesystem-order, ambient-locale, and float drift MUST NOT alter governed bytes.  
    
* Evidence: Two-run byte-identity proofs for the applicable serializer outputs under `artifacts/**`, with matching Human Index and Machine Mirror records and co-located path-proofs.  
    
* Failure posture: Any byte, pin, schema, or governed-evidence mismatch fails the applicable serializer QA condition closed. This condition does not alias or automatically satisfy any registered token.  
    
* `TWO_RUN_IDENTITY_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Mechanics Guide  
      
  * Scope: Pre-commit  
      
  * QA definition: Re-running the same CLI/API/Engine invocation yields identical governed bytes.  
      
  * Evidence: Paired canonical JSON or bytes artifacts (for example compat\_ab.json and a second-run copy) stored under artifacts/\*\*, plus matching entries in the Human Index and Machine Mirror.


* `COMPOSITE_ABBA_IDENTITY_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Mechanics Guide  
      
  * Scope: Pre-commit  
      
  * QA definition: AB and BA runs swap directional attributes correctly without unintended structural differences.  
      
  * Evidence: compat\_ab.json and compat\_ba.json where non-directional fields match and directional fields swap as expected, with path-proofs and Mirror records aligned.

Canonical name (normative). COMPOSITE\_ABBA\_IDENTITY\_OK is the only canonical acceptance token name for AB/BA composite identity. Legacy variants (including AB\_BA\_IDENTITY\_OK) MUST NOT appear as acceptance tokens in Epic Plans, acceptance maps, or token/evidence matrices. If an epic inherits legacy wording from a document, the plan may include a one-line clarification (“legacy name → canonical COMPOSITE\_ABBA\_IDENTITY\_OK”), but the claimed token name remains COMPOSITE\_ABBA\_IDENTITY\_OK.

* `ENV_RAILS_POLICY_OK`  
    
  * Owner PF: HDE-Governance / HDE-Build Checklist / HDE-Schemas & Artifacts  
      
  * Scope: Pre-commit / CI  
      
  * QA definition: The determinism env rails policy and implementation are enforced and proven using governed evidence tying CI posture to determinism-sensitive work.  
      
  * Evidence: Combined proof that:  
      
    * a single canonical helper/module (for example engine/runtime/determinism\_env.py, titles-only) defines the determinism env pins and is used by invariance/determinism tests;  
        
    * invariance tests (for example under tests/invariance/\*\*, titles-only) fail closed when pins are missing or mismatched and exercise log rendering/verification behavior; and  
        
    * the env-rails log artifact (for example audit/gates/determinism/env\_pins.log plus path-proof) is present, canonical JSON, indexed in docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl, and consistent with the CI env posture enforced by the env-check script.

    

  * These determinism env tokens work together with the general env-pin and evidence rules in §0.4.3, §2.2, and §4.3 to ensure determinism-sensitive QA always runs under a well-defined, audited env rails posture.

EPIC022 example binding (closed-rails vendor refusal; normative when used as rails proof). If an epic uses ENV\_RAILS\_POLICY\_OK to assert that explicit vendor requests are refused under closed rails, then the epic’s acceptance artifacts (acceptance map, token/evidence matrix, manifest bindings) MUST bind ENV\_RAILS\_POLICY\_OK to both: the canonical determinism env pins evidence surface (audit/gates/determinism/env\_pins.log and its path-proof), and at least one deterministic closed-rails vendor refusal scenario proof under the parity evidence family (for example parity/errors\_reader\_cli.\*) plus the enforcing parity test node (for example tests/cli/test\_errors\_parity.py::test\_http\_and\_cli\_parity). This example does not redefine token semantics. It defines a QA binding expectation: “env pins exist” is not accepted as equivalent to “closed-rails vendor refusal is proven” when ENV\_RAILS\_POLICY\_OK is used as the rails-proof token for a closed-rails vendor scenario.

* `DETERMINISM_ENV_PINS_OK`  
    
  * Owner PF: HDE-Build Checklist  
      
  * Scope: Pre-commit / CI  
      
  * QA definition: Determinism env pins are enforced and proven using a single canonical governed evidence surface. This token is path-sensitive: it is satisfied only when acceptance artifacts bind the token to the canonical env-pins log and its path-proof.  
      
  * Evidence (single canonical surface; normative): DETERMINISM\_ENV\_PINS\_OK MUST be satisfied only by: audit/gates/determinism/env\_pins.log and audit/gates/determinism/env\_pins.log.path\_proof.txt.  
      
  * When DETERMINISM\_ENV\_PINS\_OK is claimed, all acceptance ledgers MUST bind to this exact path:  
      
    * the token/evidence matrix references audit/gates/determinism/env\_pins.log  
        
    * docs/evidence/INDEX.json points the determinism env pins evidence entry to audit/gates/determinism/env\_pins.log  
        
    * artifacts/evidence\_index.jsonl mirrors that exact discovered physical path and uses audit/gates/determinism/env\_pins.log.path\_proof.txt as proof\_anchor

    

  * DETERMINISM\_ENV\_PINS\_OK MUST NOT be bound to artifacts/proofs/env\_pins.txt (or any other similarly named file) or to any alternate path. Any deviation is a mechanical blocker.

Clarification (non-authoritative). Other env-pins snapshots may exist for other proof contexts. They do not satisfy DETERMINISM\_ENV\_PINS\_OK unless they are the canonical surface defined above.

### **9.2.4 Evidence skeleton & sanity tokens**

* `EVIDENCE_INDEX_UPDATED_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts  
      
  * Scope: Pre-commit & post-commit  
      
  * QA definition: Any change to governed evidence is accompanied by same-PR updates to the Human Evidence Index and the Machine Mirror.  
      
  * Evidence: Updated docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, and artifacts/evidence\_index.jsonl, with co-located path-proofs for all governed artifacts in the same PR.


* `EVIDENCE_INDEX_HASH_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts  
      
  * Scope: Pre-commit & post-commit  
      
  * QA definition: The Human Evidence Index hash sentinel and the Machine Mirror body digest both reflect the current committed evidence index and mirror contents, as defined by PF12 Evidence Index & Machine Mirror semantics.  
      
  * Evidence: A successful run of the canonical evidence-index check (for example python tools/evidence/update\_evidence\_index.py \--check, titles-only) under closed rails, with no reported mismatches for the index hash sentinel or mirror body hash.


* `MACHINE_MIRROR_UPDATED_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts  
      
  * Scope: Pre-commit & post-commit  
      
  * QA definition: The Machine Mirror and its self-record are coherent with the current set of governed artifacts and path-proofs: every mirror record has a matching index entry and path-proof, and the self-record for artifacts/evidence\_index.jsonl reflects the current mirror body digest and size according to PF12 semantics.  
      
  * Evidence: Successful combined runs of the canonical evidence-index and orientation checks (for example update\_evidence\_index.py \--check and orientation\_demo.py \--check, titles-only) under closed rails, with no reported SHA/size mismatches or missing path-proofs.


* `EVIDENCE_PATHS_VALIDATED_OK`  
    
  * Owner PF: HDE-Schemas & Artifacts  
      
  * Scope: Evidence  
      
  * QA definition: Evidence Index and Machine Mirror records reference only safe, in-repo physical paths. Each record’s `discovered_physical_path` MUST be a relative path that resolves under the repo root (no absolute paths, no path traversal segments, and no root escapes), and the referenced file MUST exist on disk at validation time. Each Evidence Index JSONL line MUST parse as a JSON object and include required keys (including `file_id` and `discovered_physical_path`).  
      
  * Evidence: A passing run of the evidence-path validator (for example `tools/evidence/validate_evidence_paths.py`, titles-only), recorded as a CI step log or as a per-check `primary.log` under the epic’s QA evidence root.  
      
  * Notes: This token covers Evidence Index and Mirror path safety, not path-proof integrity. Path-proof integrity (sha256, `size_bytes`, and `mtime_utc` discipline) is governed separately (see §4.3.1 and `EVIDENCE_PATH_PROOFS_OK`).

**Evidence inspectability condition (non-token).**

* Owner/source: HDE-Schemas & Artifacts and HDE-Build Checklist; acceptance-token semantics remain owned by HDE-Governance.  
    
* Scope: Evidence / post-commit.  
    
* Requirement: Baseline HD Engine evidence for the epic or change set remains inspectable through governed text artifacts suitable for human and AI-agent review. The Human Evidence Index (`docs/evidence/INDEX.json`), Machine Mirror (`artifacts/evidence_index.jsonl`), required manifests, and key QA logs or step transcripts MUST expose the payloads and relationships needed to evaluate the applicable acceptance predicates.  
    
* Governed text artifacts under `docs/**`, `artifacts/**`, and/or `audit/**` MUST be wired into the Human Evidence Index and Machine Mirror under their owning schemas. A binary or compressed bundle MAY supplement that evidence, but MUST NOT be the sole governed proof when payload inspection is required; at least one governed text manifest, log, or summary MUST enumerate or summarize the relevant contents and relationships.  
    
* Pure contract or token-only evidence families MAY remain sufficient only when the evidence consumer does not need to inspect payload contents. No acceptance claim may rely solely on a non-textual or opaque artifact when content inspection is required. Concrete schemas, bundle mechanics, paths, and CI gates remain in HDE-Schemas & Artifacts and HDE-Build Checklist.  
    
* Privacy and safety boundary: inspectability does not authorize raw birth data, personal information, vendor payloads, secrets, or private narrative content in logs. Text evidence MUST remain minimal, governed, redacted, and sufficient for the predicate under review.  
    
* `CI_CHECK_MIRROR_SCHEMA_OK`  
    
  * Owner PF: HDE-Schemas & Artifacts / HDE-Build Checklist  
      
  * Scope: Evidence  
      
  * QA definition: The machine mirror conforms to schema: pinned field order, one LF per record, canonical JSONL form, and unknown-key rejection, as enforced by PF12 mirror schema and PF09 CI wiring.  
      
  * Evidence: CI mirror-schema verification artifacts for artifacts/evidence\_index.jsonl showing all records pass schema validation and no unknown keys are present.


* `CI_CHECK_FINAL_LF_OK`  
    
  * Owner PF: HDE-Build Checklist  
      
  * Scope: Pre-commit / Evidence  
      
  * QA definition: All governed text artifacts end with exactly one trailing linefeed (one LF and no extras).  
      
  * Evidence: A passing run of the final-LF check harness (for example `tools/evidence/check_lf_endings.py` calling `ci/checks/check_final_lf.sh`, titles-only), recorded as a CI step log or as a per-check `primary.log` under the epic’s QA evidence root.


* `SANITY_PIPELINE_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Governance  
      
  * Scope: Pre-commit / CI (evidence skeleton)  
      
  * QA definition: For the current HDE-EPIC038 release-sanity family, a closed-rails sanity pipeline entrypoint runs nineteen ordered checks over identity, determinism, rails, direct DB posture, BodyGraph policy, architecture, mapped-cache evidence, retained historical evidence, OPS packets, the Human Index and Machine Mirror, path validation, schema and hash validation, topology orientation, and final-LF validation. `SANITY_PIPELINE_OK` remains a composite CI token and assumes the applicable underlying evidence tokens in this subsection are satisfied.  
      
  * Evidence: Proof that:  
      
    * the dedicated sanity pipeline entrypoint is run under closed rails in CI;  
    * `audit/gates/sanity_pipeline/sanity_pipeline.log` and `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt` exist, are canonical, and are represented in the Human Evidence Index and Machine Mirror with the Mirror `proof_anchor` pointing to that path proof;  
    * the log contains exactly one ordered result for each configured stage from 01 through 19 and ends with `first_failed_stage:NONE` and `summary:PASS`; and  
    * any missing, duplicated, reordered, or non-OK stage is a CI failure that blocks the applicable underlying evidence tokens until the governed family is coherent.

    

  * The nineteen-stage log and the exact-head external attestation are separate evidence surfaces. Their presence does not by itself establish QA PASS, acceptance-token satisfaction, OPS completion, PF09 status movement, release admission, or closeout.

**QA log discoverability and completeness condition (non-token).**

* The epic current-state manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json` MUST exist and be valid JSON.  
    
* The manifest MUST be keyed by `check_id`. For every required evidence-producing check, `log_path` MUST be the full repository-relative canonical path `audit/qa/<epic-id>/checks/<check_id>/primary.log`.  
    
* Every required primary log MUST exist, MUST be non-empty, and MUST begin with the Plan Templates step-log header routed by §4.4.5. The header MUST record the exact check identity, complete command, captured environment, classification, and clear status.  
    
* Missing, empty, malformed, ambiguously targeted, or unclassified logs fail as tooling evidence; they MUST NOT be treated as a silent behavior PASS.  
    
* Manifest or log presence alone does not satisfy `SANITY_PIPELINE_OK`, establish QA PASS, prove epic acceptance, or complete closeout.  
    
* `QA_HARNESS_DISCIPLINE_OK`  
    
  * Legacy-name note: `QA_STEP_LOGS_CONSOLIDATED_OK` is deprecated and may appear only for historical traceability; current acceptance artifacts MUST use `QA_HARNESS_DISCIPLINE_OK`.  
      
  * Meaning: The epic’s QA evidence is consolidated to current-state canonical logs, with a manifest that provides deterministic pointers from checks → primary logs.  
      
  * QA definition (strict):  
      
    * For each check required by the epic’s QA posture, there exists exactly one canonical primary log at `audit/qa/<epic-id>/checks/<check_id>/primary.log` (one per `check_id`), and it is referenced from the per-epic manifest by its full repository-relative `log_path`.  
        
    * The manifest is current-state only. Any per-run retention logs under runs/\<run\_id\>/\<RUN\_SUBPATH\> are optional and non-canonical, and MUST NOT be referenced by log\_path.  
        
    * The step-log header schema and status vocabulary used in primary logs follow Plan Templates (routed by §4.4.5).

    

  * Evidence:  
      
    * The epic maintains audit/qa/\<epic-id\>/qa\_step\_logs\_manifest.json as a per-epic index keyed by check\_id, mapping each required check to its canonical primary log via log\_path.  
        
    * The manifest is deduplicated by check\_id (at most one entry per check\_id), and its log\_path values all point within the epic QA root.  
        
    * The acceptance map and token matrix bind required tokens to checks and reference the manifest \+ primary logs as the authoritative evidence surfaces.

Live QA note (mechanics smoke tests). When the sanity pipeline (or its component scripts) is run in Live QA (for example from an open-rails Codespace during an epic’s D3/D4 steps), those invocations are mechanics smoke tests, not the canonical satisfaction of SANITY\_PIPELINE\_OK. In this Live QA context, if the pipeline or a component script exits non-zero: QA MUST capture logs and exit codes mechanically in the responsible check’s `audit/qa/<epic-id>/checks/<check_id>/primary.log` and any explicitly named check-scoped sidecar; QA MUST cross-check CI/closed-rails status for SANITY\_PIPELINE\_OK and related evidence tokens; and reviewers should treat the result as a QA finding (for example “env mismatch” or “harness not wired for open rails”), not automatically as an epic-blocking failure. An epic’s acceptance roster in HDE Phased Epics may explicitly tie additional acceptance to a green Live QA run of the sanity pipeline. Only in that case should a non-zero Live QA result be treated as blocking acceptance for that epic; otherwise, canonical satisfaction of SANITY\_PIPELINE\_OK continues to come from closed-rails CI evidence.

* `CONFIG_REGISTRY_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts  
      
  * Scope: Pre-commit / CI (config \+ evidence)  
      
  * QA definition: The canonical registry report (registry.registry\_report) is generated under closed rails via the hardened registry/config generator, is canonical JSON, exhibits two-run identity, and is wired into the evidence skeleton and config acceptance map as the single source of truth for registry configuration.  
      
  * Evidence: Proof that:  
      
    * the registry report artifact (for example artifacts/registry/registry\_report.json) exists, is produced by the canonical generator under closed rails and serialized via the shared serializer, and is canonical JSON (sorted keys, compact separators, single trailing LF);  
        
    * the registry report passes its determinism and invariants tests (for example tests that check two-run identity, schema registry\_report.v1, and expected coverage of registry entries); and  
        
    * docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl contain a registry.registry\_report entry with matching sha256, size\_bytes, and proof\_anchor to artifacts/registry/registry\_report.json.path\_proof.txt, and the config acceptance map (for example audit/EPIC-018\_config\_acceptance\_map.json) references this artifact key and tokens in a canonical, validated way.


* `CONFIG_MAGIC10_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
      
  * Scope: Pre-commit / CI (config \+ evidence)  
      
  * QA definition: The Magic-10 and band-edges configs (config.magic10, config.band\_edges) are generated under closed rails via the hardened registry/config generator, are canonical JSON, satisfy the Magic-10 and band invariants defined in the math/mechanics specs, and are wired into the evidence skeleton and config acceptance map as governed configuration artifacts.  
      
  * Evidence: Proof that:  
      
    * the Magic-10 and band-edges artifacts (for example artifacts/thresholds/magic10\_config.json and artifacts/thresholds/band\_edges.json) exist, are produced by the canonical generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;  
        
    * config tests pass that validate domain invariants (for example Magic-10 order and caps cover the frozen category set with integer bounds and seed metadata, and band edges are sorted, span the clamp range, and match the Engine’s band definitions); and  
        
    * docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl include config.magic10, config.band\_edges, and the config acceptance map entry (for example epic018.config.acceptance\_map), each with matching path-proofs, sha256, and size\_bytes, and with references from the acceptance map to real artifact keys, known tokens (including CONFIG\_MAGIC10\_OK / CONFIG\_REGISTRY\_OK), and existing tests.


* `CONFIG_BUNDLES_DETERMINISTIC_OK`  
    
  * Owner PF: HDE-Build Checklist / HDE-Schemas & Artifacts / HDE-Mechanics Guide  
      
  * Scope: Pre-commit / CI (config bundles \+ evidence)  
      
  * QA definition: Typed frontend and backend config bundles (config\_bundle.fe, config\_bundle.be) are generated under closed rails from the governed config artifacts and registry loader, serialized via the canonical JSON emitter, satisfy two-run identity, and carry a sources block that links each bundle back to the precise digests and sizes of its upstream config artifacts and registry report.  
      
  * Evidence: Proof that:  
      
    * the FE and BE bundle artifacts (for example artifacts/config\_bundles/fe\_bundle.json and artifacts/config\_bundles/be\_bundle.json) exist, are produced by the canonical bundle generator under closed rails and serialized via the shared serializer with sorted keys and a single trailing LF;  
        
    * bundle tests pass that validate two-run identity, JSON structure, and domain invariants (for example tests under tests/config/test\_typed\_bundles.py, titles-only) and confirm that bundle contents (Magic-10, band edges, channels/centers/domains/alias policy for BE, slimmed bundle for FE) match the governed config artifacts and registry report; and  
        
    * docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl include config\_bundle.fe and config\_bundle.be entries with matching sha256, size\_bytes, and proof\_anchor values pointing to their .path\_proof.txt siblings, and that each bundle’s sources block lists only real governed artifacts with digests and sizes that match the evidence skeleton.

### **9.2.5 Transport / A7 tokens**

Transport/A7 tokens (for example A7\_GET\_QUOTED\_ETAG\_OK, A7\_HEAD\_PARITY\_OK, A7\_304\_OMITS\_CT\_CL\_OK, A7\_VARY\_AUTH\_AE\_OK, A7\_ENCODING\_INVARIANCE\_OK) retain their existing QA definitions and evidence mapping: Reader Catalog JSON success posture, strong quoted ETag, HEAD/304 behavior, Vary headers, encoding invariance, and composite A7 proof artifacts. Text from prior PF19 remains, with numbering updated under §9.2.5.

### **9.2.6 Aux & narrative tokens**

Registered Aux and narrative tokens, including `NARR_200_TEXT_OK` and `NARR_SUPPRESSED_NO_ETAG_OK`, retain their existing QA definitions and evidence mapping for Aux text and suppression snapshots, ETag posture, and their exact independently governed predicates. Prior PF19 operational mappings remain applicable under §9.2.6 except for the retired token-shaped composition label.

Composition determinism remains a non-token QA obligation. Identical normalized inputs and governed state MUST produce the same composition identifiers and keys, the same narrative text and header posture, and a stable strong quoted ETag when the body is unchanged. Time, randomness, filesystem order, ambient locale, and unrelated request metadata MUST NOT alter governed composition output. Required snapshots, repeated-run comparisons, same-PR Index and Machine Mirror updates, path-proofs, and failure behavior remain applicable.

### **9.2.7 CLI/API & SDK tokens**

Registered CLI/API tokens such as `CLI_SHOWCOMPAT_CANON_OK`, `CLI_READER_EMITTER_PARITY_OK`, and `CLI_STDOUT_LF_OK` retain their prior QA definitions and evidence mapping for canonical CLI JSON, exact emitter parity, stdout final-LF posture, and their independently governed predicates. Normative semantics and evidence ownership remain with HDE-Governance, HDE-Build Checklist, HDE-CLI-API-Vendor-Ref, and HDE-Schemas & Artifacts. CLI two-run byte identity remains a non-token QA obligation and MUST be proved directly for the applicable command and declared environment; it is not an alias for another token.

CLI-to-Aux parity remains a non-token QA obligation: the CLI Aux preview uses the same governed emitter as Aux; identical normalized cases produce byte-identical narrative text when text is emitted; suppression remains suppression rather than placeholder text; provenance identifiers and other governed output remain stable; applicable snapshots, parity comparisons, same-PR evidence indexing, and failure behavior remain required; and CLI/HTTP discrepancies remain failures to watch.

**Proposed token request, not currently claimable:** `SDK_READER_PARITY_OK`. Current PF04 and PF10 do not admit this name. Until Governance registers it in PF04 or mints it in a numbered PF10 addendum, SDK-to-Reader parity remains a requirement and evidence obligation only. The spelling MUST NOT appear in `claimed_tokens`, acceptance maps, manifests, token/evidence matrices, closeout claims, or `*_OK` PASS artifacts. The requested future scope is limited to supported SDK success bytes matching the Reader v1 public six-key envelope for identical normalized inputs and environment, numeric-free public output, canonical JSON and the contract’s final-LF rule, exact typed-error fields, and owner-governed determinism and conditional-request behavior. This paragraph requests future admission; it does not define current token semantics, prove SDK implementation, or change PF09.7 HDE-COAG002 from Not done.

If an owning source establishes a supported SDK Aux client, SDK-to-Aux parity becomes a non-token QA obligation for that surface: it MUST preserve governed Aux success, suppression, provenance, direction, and error behavior; MUST NOT create an alternate narrative emitter, fallback, or weakened suppression; and requires parity evidence and failure handling when in scope. If no SDK Aux surface exists, the condition is not activated and no PASS may be claimed from absence.

#### **CLI\_STDOUT\_LF\_OK**

* Owner PF: HDE-Build Checklist / HDE-CLI-API-Vendor-Ref / HDE-Governance.  
    
* Scope: Pre-commit / CI (canonical CLI bytes).  
    
* QA definition: On CLI success paths, stdout is canonical bytes: the emitted success payload is serialized via the canonical emitter/serializer and ends with exactly one trailing linefeed. On success, stderr is empty.  
    
* Evidence: Combined proof that:  
    
  * CI enforces canonical-bytes posture for at least one representative success command (for example hdctl showcompat) via a CI-safe test that checks: stdout non-empty, stderr empty, and stdout ends with exactly one trailing LF, and  
      
  * governed stdout capture artifacts (and their checksums/args, where used) are stored under governed evidence roots and are bound in the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix) to concrete paths with no placeholders, with Index/Mirror/path-proofs kept in same-PR parity.

EPIC022 D2 example (informative; not a semantic expansion) is as follows. EPIC022 PR3 is the reference concretization pattern: deterministic showcompat stdout artifacts are captured under:

* artifacts/cli/showcompat/stdout.json  
    
* artifacts/cli/showcompat/stdout.json.sha256  
    
* artifacts/cli/showcompat/args.json

These artifacts (with co-located \<artifact\>.path\_proof.txt siblings) are bound to a canonical-bytes test (for example tests/cli/test\_cli\_canonical\_bytes.py::test\_showcompat\_stdout\_is\_canonical) in the epic’s acceptance artifacts. These are deterministic fixtures for stdout canonicalization. They MUST NOT be treated as release identity proofs; release identity remains governed by the /internal/version identity surface and its acceptance/evidence rules.

#### **CLI\_SHOWCOMPAT\_CANON\_OK (environment semantics)**

* Owner PF: HDE-CLI-API-Vendor-Ref / HDE-Governance / HDE-Build Checklist.  
    
* Scope: Pre-commit / CI / Live QA (compat behavior via CLI).  
    
* QA definition: CLI\_SHOWCOMPAT\_CANON\_OK asserts that hdctl showcompat behaves canonically for compat display in the environment declared as canonical for the epic:  
    
  * it produces governed compat JSON in the expected shape (categories, bands, scores, meta) for a fixed pair  
      
  * it respects the environment’s source-selection rules (DB/packs vs vendor) as defined in PF05 and PF19 (§3.3, §5.6)  
      
  * it exhibits two-run identity and, where applicable, AB↔BA parity for governed parts

Output posture (clarification; normative for QA interpretation) is as follows:

* hdctl showcompat stdout is the compat payload (admin/test surface). It may include numeric-bearing fields (for example numeric scores or weights) on success. Numeric-bearing success output is not treated as a covenant violation for this token.  
    
* The numeric-free covenant applies to:  
    
  * typed error envelopes, and  
      
  * Reader v1 success envelopes (public success body).


* Reader v1 bytes are proven for CLI parity only via \--dump-reader sidecars (and via the Reader surface), not by asserting that showcompat stdout matches Reader bytes.

Exit-code posture (clarification; titles-only ownership) is as follows. CLI exit-code semantics are owned by the CLI contract (titles-only). PF19’s QA rule is: do not assume typed failure exit code equals 2\. Repo-tested mapping used for QA documentation (docs-only alignment) is:

* 0 on success.  
    
* 64 for usage, validation, and I/O failures raised via CliError.  
    
* For showcompat, vendor/engine failure paths return exit 1\.  
    
* Other non-zero exit codes remain command-specific. Do not generalize them across commands.

Evidence is as follows:

* Governed compat JSON artifacts from hdctl showcompat runs in the declared canonical environment for the epic, stored under artifacts/cli/\*\*, with:  
    
  * AB↔BA parity proofs where required  
      
  * two-run identity proofs for the canonical environment  
      
  * Index/Mirror records and path-proofs in the same PR


* Where Reader v1 parity is in scope for the epic, governed \--dump-reader sidecar artifacts and their parity checks, bound in acceptance artifacts and indexed in the same PR.  
    
* A short planning or acceptance note in an explicitly named check-scoped artifact under `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>` stating which environment or environments are treated as canonical for CLI\_SHOWCOMPAT\_CANON\_OK in that epic.

#### **CLI\_ADMIN\_BUNDLE\_PARITY\_OK**

* Owner PF: HDE-CLI-API-Vendor-Ref / HDE-Mechanics Guide.  
    
* Scope: Post-commit / Live QA (CLI/API, admin surfaces).  
    
* QA definition: For a given match and admin credential, the CLI admin bundle command and the HTTP admin bundle route both call the canonical admin bundle builder and return byte-identical admin bundle JSON objects. No CLI-only or HTTP-only fields appear in the admin bundle payload, and any transport-level differences (for example HTTP headers) are outside the bundle JSON.  
    
* Evidence:  
    
  * A pair of governed admin bundle artifacts for at least one test match:  
      
    * artifacts/admin/cli\_bundle\_\<pair\>.json (CLI), and  
        
    * artifacts/admin/http\_bundle\_\<pair\>.json (HTTP),  
      produced under determinism env pins from the same QA console, both using a valid admin credential.

    

  * A small parity artifact (for example artifacts/admin/bundle\_parity\_\<pair\>.json or an equivalent diff/proof) demonstrating structural and byte equality of the two JSON bundles after canonical re-serialization.  
      
  * Indexed entries for all three artifacts in docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256) and artifacts/evidence\_index.jsonl, each with a co-located path-proof and a Mirror record whose proof\_anchor points at that proof.

#### **ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK**

* Owner PF: HDE-Mechanics Guide / HDE-Schemas & Artifacts / HDE Narratives Guide.  
    
* Scope: Post-commit / Live QA (admin bundle content).  
    
* QA definition: The admin bundle builder composes the full product payload for a single match into one JSON object. For each tested match, the admin bundle contains, at top level, at least a\_bodygraph, b\_bodygraph, compat, narratives, and meta, where:  
    
  * a\_bodygraph and b\_bodygraph are canonical BodyGraph JSON objects for each party (shape and mechanics per HDE-Mechanics Guide and HDE-Schemas & Artifacts)  
      
  * compat is the full Magic-10 compat result (category set, scores, bands, and compat meta) consistent with existing compat surfaces (titles-only)  
      
  * narratives is an array of exactly three Aux narrative compositions (two private, one shared) with composition IDs and pack SHA, and  
      
  * meta carries engine\_tag, release\_id, invocation\_tag or equivalent, and bundle source/rails metadata


* No required component may be silently omitted or replaced with a placeholder.  
    
* Evidence:  
    
  * At least one governed admin bundle artifact (for example artifacts/admin/cli\_bundle\_\<pair\>.json) per test match, produced via the canonical admin bundle builder under determinism env pins.  
      
  * A QA harness or test that validates:  
      
    * presence of the required top-level keys (a\_bodygraph, b\_bodygraph, compat, narratives, meta)  
        
    * that narratives has length 3 and each element carries composition IDs and pack SHA  
        
    * that the BodyGraph, compat, and narratives sections are consistent with their respective single-home surfaces (for example by cross-checking against separate BodyGraph/compat/narrative QA artifacts for the same match)

    

  * Indexed entries and path-proofs for the admin bundle artifacts and any validation logs in the Human Index and Machine Mirror, in the same PR.

#### **ADMIN\_AUTH\_REQUIRED\_OK**

* Owner PF: HDE-Governance.  
    
* Scope: Post-commit / Live QA (auth & logging for admin surfaces).  
    
* QA definition: Neither the CLI admin bundle command nor the HTTP admin bundle route will return a full admin bundle JSON object unless the configured admin credential is presented. Unauthenticated and mis-authenticated attempts yield typed authentication/authorization errors only, and each successful admin bundle call is logged as an operations event with timestamp, caller identity (CLI vs GUI and user/account label), a high-level description of the inputs, and a correlation ID, in accordance with HDE-Governance logging and PII rules.  
    
* Evidence:  
    
  * Successful admin bundle runs (CLI and HTTP) for at least one test match with a valid admin credential, as described under CLI\_ADMIN\_BUNDLE\_PARITY\_OK and ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK.  
      
  * Negative auth runs:  
      
    * CLI invocations of the admin bundle command without a credential and with an invalid credential, captured as governed artifacts (for example artifacts/admin/auth\_negative\_cli\_\<pair\>.json) showing non-zero exit codes and typed auth errors, with no admin bundle JSON present.  
        
    * HTTP invocations of the admin bundle route without a credential and with an invalid credential, captured as governed artifacts (for example artifacts/admin/auth\_negative\_http\_\<pair\>.json) showing appropriate error status and typed error bodies, with no admin bundle JSON present.

    

  * At least one redacted sample (or a path-proof-only record) demonstrating that successful admin bundle calls are logged with timestamp, caller identity, high-level input description, and correlation ID, and that logs are keys-only and free of raw birth data and secrets.  
      
  * Indexed entries and path-proofs for the negative auth artifacts and any log samples in docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256) and artifacts/evidence\_index.jsonl in the same PR as the admin bundle QA evidence.

### **9.2.8 App-layer QA owner boundary**

PF19 defines no App-layer acceptance token locally. App-layer names may be added only after the exact current App QA or security owner establishes versioned semantics, assessed scope, verification method, evidence family, and claim rules, and current token authority admits each exact name. Until then, App QA plans MUST NOT infer, map, or claim an App token from this section.

### **9.2.9 EPIC → token mapping (QA routing rule)**

An EPIC acceptance roster MUST list tokens by canonical name as defined in HDE-Governance (and mirrored in this PF19 token library). PF19 QA checks that token rosters and token/evidence matrices do not introduce aliases or midflight renames. This is a routing and validation rule, not a permission: tokens still require evidence.

### **9.2.10 Forward plan**

This section was introduced to converge the Glow QA token ecosystem by:

* consolidating the QA operational mappings and evidence bindings into a single QA-facing list  
    
* binding each acceptance token to its governed evidence family  
    
* extracting EPIC017 QA token operational guidance into this library where it was not already captured

HDE-Governance remains the single source of truth for token names and normative semantics. PF19 §9.2 is the single QA-level home for the QA operational mapping (QA-facing meaning plus mechanical evidence expectations).

### **9.2.11 CLI guard tokens (D3 serializer/emitter guards)**

These tokens cover CLI guard tools (for example serializer\_grep\_guard.py, emitter\_symbol\_proof.py) that enforce closed determinism env rails and serializer/emitter wiring. Their canonical PASS condition is satisfied in CI/closed-rails runs, not in open-rails Live QA.

#### **CLI\_SERIALIZER\_GUARD\_OK**

* Owner PF: HDE-Build Checklist / HDE-Mechanics Guide.  
    
* Scope: Pre-commit / CI (D3 guard stage).  
    
* QA definition: Under closed determinism rails (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0), the CLI serializer guard job (for example serializer\_grep\_guard.py, titles-only) exits successfully and reports no violations of the canonical serializer/emitter wiring or determinism env pins. A non-zero exit under closed rails indicates a real guard failure that must block D3 acceptance.  
    
* Evidence:  
    
  * CI job logs showing the guard script ran under determinism env pins and exited with status 0, with a PASS summary and no reported violations.  
      
  * Guard log artifacts (for example artifacts/cli/guards/serializer\_grep\_guard.log) stored under governed paths with co-located path-proofs.  
      
  * Index and Mirror entries for the guard artifacts in docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256) and artifacts/evidence\_index.jsonl in the same PR.

#### **SERIALIZER\_GREP\_GUARD\_OK**

* Owner PF: HDE-Build Checklist / HDE-Mechanics Guide.  
    
* Scope: Pre-commit / CI (D3 guard stage).  
    
* QA definition: The serializer grep guard enforces that governed CLI/Engine paths only use the canonical serializer/emitter and do not introduce ad-hoc JSON encoding or unpinned env-dependent behavior. Under closed determinism rails, the guard must pass (exit 0\) with no forbidden patterns or missing serializer uses.  
    
* Evidence:  
    
  * Guard configuration and CI logs showing:  
      
    * execution of the grep-based guard under determinism env pins, and  
        
    * a PASS result for all monitored files and patterns.

    

  * A governed guard summary artifact (for example artifacts/cli/guards/serializer\_grep\_guard.summary.json or similar, titles-only) indexed in the Human Index and Machine Mirror with matching path-proof.

#### **EMITTER\_SYMBOL\_PROOF\_OK**

* Owner PF: HDE-Build Checklist / HDE-Mechanics Guide.  
    
* Scope: Pre-commit / CI (D3 guard stage).  
    
* QA definition: The emitter symbol proof guard confirms that CLI and HTTP emitters share a single canonical emitter implementation and that no extra emitter symbols or divergent code paths are used for governed surfaces. Under closed determinism rails, the emitter symbol proof must pass (exit 0\) and show that all expected emitter symbols are present and wired correctly, with no unexpected or missing emitters.  
    
* Evidence:  
    
  * CI job logs for the emitter symbol proof run under determinism env pins, showing exit status 0 and a PASS summary over the configured symbol set.  
      
  * A governed emitter symbol proof artifact (for example artifacts/cli/guards/emitter\_symbol\_proof.txt) indexed in docs/evidence/INDEX.json (plus docs/evidence/INDEX.sha256) and artifacts/evidence\_index.jsonl, with a co-located path-proof and a Mirror record whose proof\_anchor points to that proof.

Open-rails Live QA note (informational only) is as follows. When these guard tools are run in open-rails Live QA environments (for example a PO or IA Codespace where SAFE\_MODE=0 and ALLOW\_NETWORK=1 by design), they are expected to enforce env pins and rails assumptions and fail closed (non-zero exit) when env pins do not match the closed determinism rails they require. Such env-mismatch failures in open-rails Live QA are treated as informational env-enforcement checks, not as D3 acceptance failures: they do not satisfy the guard tokens above, and they must not be used to block PO Live QA sessions when the environment is intentionally open rails. D3 guard tokens (CLI\_SERIALIZER\_GUARD\_OK, SERIALIZER\_GREP\_GUARD\_OK, EMITTER\_SYMBOL\_PROOF\_OK) are considered satisfied only by closed-rails CI runs with PASS outcomes; Live QA plans should reference CI/closed-rails evidence when asserting these tokens, not re-run D3 under open rails.

### **9.2.12 Manifests, acceptance maps, and token binding**

PF19 treats epic manifests and epic acceptance maps as complementary views of the same acceptance surface:

* The acceptance map (for example docs/acceptance\_map\_epicXXX.json, titles-only) is the design-time source that:  
    
  * enumerates the epic’s D-goals/foundations (D1, D2, and similar),  
      
  * lists the QA tokens relevant to each D-goal, and  
      
  * names the governed evidence families (artifact keys, logs, indices) expected to satisfy those tokens.


* The epic manifest (for example audit/EPICXXX\_MANIFEST.json, titles-only) is the run-time record that:  
    
  * declares each token’s status for that epic, and  
      
  * binds tokens to the concrete governed artifacts and tests that have actually been run.

Close-pack manifest key\_outputs bindings (normative; validator-bound) are as follows. Epic close-pack manifests MUST represent their primary outputs via key\_outputs as a dictionary of named bindings to exact path strings (not as a list or membership set). Validators are permitted to validate both the required binding keys and the exact bound path values. Required binding keys (names-only; stable) are: acceptance\_map, token\_matrix, acceptance\_viability, step\_logs\_manifest, doc\_deltas, close\_report, close\_manifest.

Closeout-ledger completeness (normative) is as follows. For epic closeout, the acceptance map, token/evidence matrix, acceptance-map viability log, and manifest MUST describe the same in-scope token surface. A reduced global-only subset is non-conforming when the epic reuses broader in-scope D-goal proof families.

The token/evidence matrix MUST map each in-scope token to the concrete governed evidence families and any same-run QA log anchors used for closeout. Generic global-discipline artifacts alone are not enough unless the acceptance map names that family as the token’s canonical evidence home.

The acceptance-map viability log MUST evaluate coverage for the same in-scope closeout roster carried by the acceptance map and manifest. A viability result is non-conforming if it reports a smaller token surface than the acceptance map and manifest declare for that epic.

When remediation expands or corrects the in-scope closeout roster, the acceptance map, token/evidence matrix, acceptance-map viability log, and manifest MUST be regenerated together so all four views remain consistent.

Registry-level binding rule (normative) is as follows. For each epic, the epic manifest MUST bind each QA token to artifacts that belong to the evidence families named for that token in the epic’s acceptance map (or in a PF-Canon section that the acceptance map points to by title). It is not acceptable to bind tokens to generic artifacts (for example a random sanity log or the Machine Mirror) when the acceptance map declares a different evidence family as the canonical home.

Acceptance map ↔ manifest consistency (normative; automated) is as follows. Acceptance maps and manifests MUST be kept consistent by automated tests, not by manual inspection:

* For every token listed in the acceptance map, there must be:  
    
  * a corresponding manifest entry for that token, and  
      
  * at least one artifact path in the manifest that belongs to the evidence family (or families) declared for that token in the acceptance map.


* For every token in the manifest, there must be:  
    
  * a corresponding entry in the acceptance map (or in a clearly referenced PF-Canon section for that epic), and  
      
  * evidence paths that resolve to real governed artifacts in those families (present in Index/Mirror with path-proofs and matching sha256/size\_bytes).

Automated tests (for example tests/audit/test\_acceptance\_map\_epicXXX.py, names-only) are expected to:

* validate the shape and contents of the acceptance map itself (epic id, foundations, token roster), and  
    
* assert that the manifest’s token→artifact bindings match the evidence families and artifact paths declared in the acceptance map (or its canonical PF references).

When new evidence families are introduced (normative), and an epic adds new evidence families (for example sampler or Engine Core evidence families defined in HDE-Schemas & Artifacts by title) and new tokens that depend on them, the corresponding PF12 and PF09/PF19 entries MUST be updated so that:

* the evidence families appear in the Evidence Catalog (PF12) with the correct artifact keys and paths  
    
* the acceptance map names those families and their tokens  
    
* the manifest binds those tokens only to artifacts that belong to those families, with automated tests enforcing acceptance map ↔ manifest ↔ evidence skeleton consistency

PF19 does not define manifest or acceptance map schemas; those live in HDE Phased Epics, HDE-Build Checklist, and HDE-Schemas & Artifacts (titles-only). PF19’s role is to make clear that:

* tokens are only Green when manifests bind them to the evidence families declared in the acceptance map, and automated tests prove that binding, and  
    
* a manifest that binds tokens to unrelated artifacts, or that diverges from the acceptance map, is treated as a QA failure until corrected and covered by tests.

### **9.2.13 Live vendor and discovery QA conditions**

These non-token conditions govern bounded live-vendor transport evidence, authorized open-rails environment proof, and D0 discovery for epics whose approved QA scope includes live vendor behavior or vendor-first PO Live QA. They do not mint or satisfy acceptance tokens.

#### **Live-vendor transport evidence condition (non-token)**

* The approved QA plan MUST declare the bounded set of acceptance-relevant vendor-facing Live QA checks and the exact `check_id` for each check.  
* Each declared check MUST produce one canonical primary log at `audit/qa/<epic-id>/checks/<check_id>/primary.log`, and the root `audit/qa/<epic-id>/qa_step_logs_manifest.json` MUST reference that full repository-relative path.  
* Each primary log MUST contain the required Plan Templates step-log header and `captured_env`, plus evidence sufficient for the exact route and bounded behavior tested, such as the necessary bounded requests, responses, timestamps, outputs, or side effects. Capture MUST remain secret-safe, payload-minimal, and governed.  
* Evidence and status MUST distinguish observed live-transport success, provider failure, tooling failure, and offline evidence; none may be silently substituted for another.  
* A successful live HTTP interaction proves only the bounded transport behavior observed. It does not prove vendor correctness, BodyGraph normalization, astronomical calculation, Human Design mechanics, public Reader correctness, production authorization, QA PASS, epic acceptance, or acceptance-token satisfaction.

#### **Open-rails evidence condition (non-token)**

* For every authorized vendor-facing check that requires network access, the caller or operator MUST explicitly authorize open rails; open rails MUST NOT be a hidden default.  
* The check’s canonical primary-log header `captured_env` field MUST capture the complete applicable environment and MUST show `SAFE_MODE=0` and `ALLOW_NETWORK=1`.  
* Missing, contradictory, or ambiguous rails values in `captured_env` MUST fail the check’s environment proof; no open-rails posture may be inferred from an optional sidecar alone.  
* Any optional environment snapshot is non-gating and MUST NOT be the sole rails evidence. The check MUST also preserve its bounded route, credential, timeout, redaction, and evidence posture without exposing secrets.  
* Open rails proves only the authorized environment tuple for the bounded check. It does not imply a successful vendor call, behavior PASS, acceptance result, production authorization, or token satisfaction.

#### **D0 discovery gate (non-token)**

* Owner/source: HDE-Build Checklist, HDE-Schemas & Artifacts, and HDE Phased Epics.  
* Scope: Pre-run planning and tooling discovery.  
* Discovery MUST complete before Live QA plan finalization and execution. It MUST capture current repository and environment facts rather than guess them: the presence or absence of governed loci such as `artifacts/config`, `artifacts/config_bundles`, and `artifacts/registry`; current guard and sanity runners; actual CLI help for intended commands; rails intent; and `.gitignore` behavior for the epic QA root.  
* Each discovery activity MUST use a concrete stable check identity under `audit/qa/<epic-id>/checks/<check_id>/`. Its decisive receipt is `primary.log`; any required tree, runner, help, rails, or gitignore capture MUST be an explicitly named check-scoped sidecar referenced by that log.  
* Preserved example sidecar purposes and filenames include `d0-config-tree.txt`, `d0-bundles-tree.txt`, `d0-guards-tree.txt`, `d0-sanity-runner-notes.txt`, `d0-hdctl-help.txt`, `d0-showcompat-help.txt`, `d0-bg-resolve-help.txt`, `d0-env-rails.txt`, and `d0-gitignore-audit-qa.txt`, or explicit equivalent names selected by the approved plan.  
* Missing discovery or findings that contradict the proposed plan MUST block plan finalization or execution as a tooling or planning defect. Discovery output that becomes governed evidence MUST receive the required Human Index, Machine Mirror, and path-proof treatment, and the applicable acceptance map or manifest MUST bind the concrete check evidence.  
* Discovery evidence does not prove runtime PASS, live-vendor success, acceptance-token satisfaction, PF09 status movement, or epic completion.

#### **QA\_BOOTSTRAP\_OK**

* Meaning: The QA harness bootstraps successfully, producing the expected governed folder structure and current-state bootstrap artifacts under the epic QA root.  
    
* Evidence:  
    
  * The harness creates the canonical epic QA root under the governed audit/qa tree.  
      
  * The current-state bootstrap step’s primary log exists at `audit/qa/<epic-id>/checks/d0_discovery/primary.log` and begins with a valid Plan Templates step-log header as routed by §4.4.5, including at minimum `check_id`, `status`, `command`, and `captured_env`.  
      
  * The root manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json` exists, includes a `d0_discovery` entry whose `log_path` is the full repository-relative value `audit/qa/<epic-id>/checks/d0_discovery/primary.log`, and has the sibling path-proof transcript `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`.  
      
  * The epic QA-root meta file `00_meta/doc_deltas.md` exists as the bootstrap doc-delta capture for the QA root.  
      
  * The log body includes the bootstrap outputs, including paths created, environment notes, and any relevant diagnostics.

#### **QA\_BOOTSTRAP\_TOOLING\_FAIL**

* Meaning: The harness attempted to bootstrap but failed due to tooling or environment issues, not behavior, and recorded an explicit blocked or tooling-failure status with evidence.  
    
* Evidence:  
    
  * The current-state bootstrap step’s primary log exists at `audit/qa/<epic-id>/checks/d0_discovery/primary.log` and begins with a valid Plan Templates step-log header as routed by §4.4.5.  
      
  * The bootstrap log records status as a tooling or prerequisite failure, for example `FAIL_TOOLING` or `TOOLING_BLOCKED`, and includes a clear reason in the header if present or at the top of the log body.  
      
  * If bootstrap progresses far enough to refresh the epic QA-root manifest pair, that manifest evidence remains current-state under the epic QA root and continues to point to the bootstrap step’s canonical primary log path.

#### **QA\_HARNESS\_DISCIPLINE\_OK**

* Meaning: The plan/harness adheres to governed evidence discipline: canonical primary logs, manifest pointers, and token claims that are names-only and evidence-backed.  
    
* Evidence:  
    
  * The top-level epic QA output folder contains:  
      
    * a consolidated step logs manifest (audit/qa/\<epic-id\>/qa\_step\_logs\_manifest.json)  
        
    * a canonical primary log per check\_id (as referenced by the manifest)  
        
    * an indexed evidence bundle via governed INDEX/Mirror (where applicable)

    

  * Each invoked step’s primary log begins with a Plan Templates step-log header as routed by §4.4.5 and includes:  
      
    * a complete command  
        
    * captured\_env sufficient to prove rails posture for that step  
        
    * a status value consistent with the evidence

    

  * If token fields are present in headers, they are names-only and use canonical spellings (intended\_tokens, claimed\_tokens, or legacy tokens as an alias for intended tokens only).

Evidence (names-only; current posture) is as follows:

* Deterministic viability result (current-state): the viability check’s decisive receipt is `audit/qa/<epic-id>/checks/<check_id>/primary.log`. If the producing tool requires a separate report, it MUST use an explicitly named check-scoped sidecar at `audit/qa/<epic-id>/checks/<check_id>/<explicit_filename>` referenced by that primary log; a generic epic-root `acceptance_map_viability.log` is not a current-state evidence home.  
    
* The report MUST:  
    
  * name the acceptance map path examined (titles-only reference here),  
      
  * report status: PASS when viable, and  
      
  * when not viable, list missing/broken references and classify them as tooling-class failures that block Live QA until corrected.


* Acceptance artifacts referenced (must exist and be consistent): the epic’s acceptance map and any acceptance-ledger artifacts referenced by the viability report (titles-only; owned by the epic acceptance posture).  
    
* Optional harness execution evidence (recommended when generated by harness; not required): if the viability report is produced as part of a harness run (not ad hoc manual inspection), also provide:  
    
  * the current-state primary step log at `audit/qa/<epic-id>/checks/<check_id>/primary.log`, referenced by the manifest, and  
      
  * an entry in `audit/qa/<epic-id>/qa_step_logs_manifest.json` for the viability `check_id` whose `log_path` is that full repository-relative primary-log path.

Note: Under current QA posture, the manifest is a current-state index keyed by check\_id. Optional per-run retention paths under audit/qa/\<epic-id\>/runs/\<run\_id\>/\<RUN\_SUBPATH\> may exist, but are not required for this token.

Relationships to other QA posture (names-only; no new scope). This token supports “don’t start Live QA until the scaffolding is runnable.” It complements baseline discovery context capture (D0 discovery / environment baseline) and rails posture discipline (closed-rails by default; open-rails only where explicitly required), by preventing “missing assets / non-runnable plan” failures before PO Live QA begins.

---

### **9.2.14 Token/evidence matrix and review rails**

**Intent.** Make the relationship between QA tokens and evidence explicit and checkable at review time. Any epic that defines or consumes QA Acceptance Tokens MUST maintain a concrete, reviewable token/evidence matrix as part of its QA ledger.

**Scope.** The token/evidence matrix requirement applies to:

* implementation plans  
    
* QA plans  
    
* epic records and acceptance maps in HDE Phased Epics

This applies whenever those artifacts introduce, rename, or consume QA Acceptance Tokens from this registry.

**Canonical artifact (HDE epics).** For HD Engine epics that use acceptance maps and token-based acceptance rosters, the token/evidence matrix MUST exist as a governed, reviewable artifact under the epic QA tree.

* Canonical path pattern: `audit/qa/<epic-id>/token_evidence_matrix.md` (format may be Markdown table or another reviewable, machine-readable form)

The token/evidence matrix MUST NOT be embedded inside the Epic Plan document. Plans may reference the matrix by path, and may include a single placeholder pointer indicating it will be authored/updated during implementation and QA closeout.

**Scaffolding vs stage-gate strictness.** Scaffolding PRs may seed a token/evidence matrix early (planned or token-incomplete rows, partial evidence titles) to establish the acceptance skeleton. However:

* PF19 MUST NOT be used to block plan approval on the matrix being fully populated; early matrices may be incomplete and serve only as scaffolding.  
    
* The strict requirements below (complete rows, no implicit cells, and a normalized map suitable for approval) apply at QA ledger completion / closeout readiness and at epic close.  
    
* Within PF19, “QA ledger completion / closeout readiness” means the point at which the epic’s governed QA artifacts under `audit/qa/<epic-id>/` are complete enough for final Live QA review and epic closeout.  
    
* No epic may claim token satisfaction while the matrix is still in a seeded, placeholder state.

**Token scope discipline (planning-time; normative).** To prevent planning stall, any plan or QA ledger that references QA tokens MUST separate token mentions into:

* In-scope acceptance tokens — tokens that will be used as acceptance gates for the epic; these are the only tokens that get matrix rows and must be proven by QA ledger completion / closeout readiness.  
    
* Deferred tokens — tokens that are desired but cannot be wired to concrete tests/CI/Live QA/evidence without inventing new semantics; deferred tokens MUST NOT appear in the in-scope acceptance roster or matrix, and must be recorded as explicitly deferred in HDE Phased Epics.  
    
* Informative references — non-gating metadata (workflow state, notes, or narrative pointers) that MUST NOT be treated as QA Acceptance Tokens and MUST NOT be placed into the token/evidence matrix.

**Token roster minimization (recommended).** The in-scope acceptance roster SHOULD be small. For a typical epic, target ≤ 15 in-scope tokens. If an epic proposes a larger roster, the plan SHOULD include a brief justification and show why existing tokens cannot cover the required acceptance invariants.

#### **9.2.14.1 Matrix shape (per-token rows)**

For each QA acceptance token that is in scope for a plan or epic (one row per token), the matrix MUST capture at least:

* PF19 registry name — the canonical token spelling from this registry (no local aliases).  
    
* Epic-level acceptance map name — the token name as it appears in the epic’s acceptance map (must be exactly the PF19 registry name).  
    
* Tests — unit/integration tests that exercise the token’s behavior (for example specific test modules or cases).  
    
* CI jobs — CI jobs that enforce the token’s behavior under closed rails, where applicable (names only; definitions live in HDE-Build Checklist).  
    
* Live QA steps (if applicable) — Live QA steps that demonstrate the token’s behavior (for example D1/D3 steps in the epic QA plan), with references to their primary step logs under `audit/qa/<epic-id>/`.  
    
* Evidence artifacts — governed artifact paths under governed roots (for example docs/**, artifacts/**, audit/\*\*) generated by those tests and steps.  
    
* Index/Mirror binding — the Evidence Index and Machine Mirror records (by artifact key or path) that register those artifacts, including `proof_anchor` references to path-proofs.

**Proof transcripts are not primary evidence (normative).** For most tokens, the matrix MUST bind the token to the primary artifacts and the tests/jobs/steps that generate and validate them. The corresponding `<artifact>.path_proof.txt` files are normally entailed via the Machine Mirror record’s `proof_anchor` and validated by the evidence tooling. Do not bind a token solely to a path-proof transcript as the evidence artifact unless that token’s own canonical evidence surface explicitly requires naming a proof transcript path (for example a single canonical surface token that is defined as path-sensitive).

The matrix may be rendered as a table, JSON, or other machine-readable structure, but it must be complete for all in-scope acceptance tokens by QA ledger completion / closeout readiness and at epic close.

#### **9.2.14.2 Ledger gate (no “e.g.” / “TBD” / implicit cells)**

At QA ledger completion / closeout readiness and at epic close, for tokens that remain in scope, no cell in the token/evidence matrix may be left blank, marked as “e.g.”, marked as “TBD”, or described only in narrative prose. If a test, CI job, Live QA step, or evidence artifact does not yet exist, that gap must be called out explicitly and treated as a blocking issue, not as an implicit future task.

**Concretized-token hygiene (normative; EPIC022 anti-drift pattern).** Once a token’s evidence bindings have been concretized (real artifact paths exist on disk and are being used for acceptance), acceptance artifacts MUST be single-authoritative and pattern-free:

* The token MUST appear at most once in each acceptance artifact (token/evidence matrix, acceptance map, manifest token roster); duplicate rows/entries are treated as ambiguous evidence and block closeout readiness.  
    
* Evidence lists MUST NOT contain placeholders or patterns (for example {scenario}, “TBD”, “pending”, or template strings) for any token whose concrete evidence is present.  
    
* CI-safe scaffold tests MAY enforce exactly one token row/entry exists per token and every listed evidence path resolves to a real file (existence plus minimal parse checks) to prevent drift regressions.

**Acceptance-alignment validator (CI-safe; recommended).** CI-safe validator tests SHOULD enforce the following invariants to prevent drift regressions:

* Map ↔ matrix ↔ manifest lockstep: token rosters match exactly across acceptance map, token/evidence matrix, and manifest token roster (no extras/missing).  
    
* Token registry membership: every token referenced by acceptance artifacts exists in the PF19 token registry.  
    
* Duplicate-free rosters: acceptance map, matrix, and manifests must not contain duplicate token entries.  
    
* Implemented/covered evidence binding: for tokens marked implemented/covered, every claimed governed evidence path MUST exist in both the Human Evidence Index (`docs/evidence/INDEX.json`) and the Machine Mirror (`artifacts/evidence_index.jsonl`), and the Mirror record MUST include a `proof_anchor` pointing to the corresponding `<artifact>.path_proof.txt`.  
    
* Proof transcripts not primary evidence: enforce “Proof transcripts are not primary evidence (normative)” (see §9.2.14.1).  
    
* Determinism posture: validator tests MUST be CI-safe (no network) and enforce determinism env pins/rails as required elsewhere in PF19 (`SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, `TZ`).

Planned tokens may skip the implemented/covered evidence-binding assertions, but they must still participate in roster/registry/duplicate checks. When a token flips to implemented/covered, the evidence-binding checks become mandatory.

A QA ledger / closeout record that contains any in-scope token with:

* e.g. or TBD token names  
    
* missing or implicit tests/CI/Live QA references  
    
* missing evidence/index/mirror bindings

MUST NOT be marked complete (ASK OK) for that token. Completion can proceed only once the matrix row is fully populated and consistent with the acceptance map and manifest (§9.2.12).

Any attempt to treat an incomplete matrix row as “good enough for now” is a QA process violation at closeout readiness and close. Reviewers must either:

* require the gaps to be filled and re-review the QA ledger, or  
    
* record a deliberate scope deferral in HDE Phased Epics and remove the token from the in-scope roster for that epic.

#### **9.2.14.3 Consistency with acceptance maps and manifests**

The token/evidence matrix is a per-plan view of the same relationships enforced globally by §9.2.12:

* Every PF19 registry name that appears in the matrix MUST also appear in the epic’s acceptance map token roster.  
    
* Every evidence artifact listed in the matrix MUST belong to one of the evidence families named for that token in the acceptance map (or in a PF-Canon section the map points to by title), and must be present in the Human Index and Machine Mirror with a valid path-proof.  
    
* Automated tests are expected to validate that matrix rows, acceptance maps, manifests, and the evidence skeleton remain in sync. Inconsistencies between these views (including missing rows, extra tokens, or mismatched artifact families) are QA failures, not documentation nits.

**Canonical evidence-path validation (preflight; pass/fail) is required.** Every token-to-artifact binding that appears in an epic’s acceptance artifacts (required evidence list, token/evidence matrix, and any manifest bindings) MUST be validated against the canonical Evidence Catalog defined in HDE-Schemas & Artifacts (titles-only) before approval or merge.

* If the Evidence Catalog defines a fixed canonical path for a token’s evidence surface, the acceptance artifacts MUST bind to that exact path.  
    
* Any binding to a non-canonical path is a mechanical blocker and MUST be corrected before approval. If a non-canonical path is truly required, it MUST be routed as an explicit ADR and drained into the Evidence Catalog (by title) before acceptance can proceed.

**Plan ↔ matrix cross-check (local bundle deliverables).** When a deliverable is described as a local bundle of governed artifacts under a directory root (for example artifacts/ops/internal\_version/\*\*), the epic’s required evidence list MUST explicitly name:

* the complete required local bundle paths (titles-only, full paths), and  
    
* any shared/global governed evidence required outside the local bundle root (for example determinism env pins evidence),

so reviewers do not assume those dependencies are implicit. The token/evidence matrix MUST mirror the same required-evidence path set. Missing shared/global dependencies or mismatched paths block QA ledger completion / closeout readiness and block epic close.

**Minimum agreement set when claiming a token (names-only).** When an in-scope token is claimed as satisfied, the following MUST all agree on the same canonical artifact key/path:

* the epic’s required evidence list (in the epic’s acceptance artifacts)  
    
* the token/evidence matrix row for the token  
    
* the Human Evidence Index entry for the bound artifact  
    
* the Machine Mirror record for the same artifact  
    
* the corresponding path-proof referenced by the Mirror record (`proof_anchor`)

**Deterministic parity scenarios (normative).** Any new or expanded error parity scenario used for acceptance (for example DB-unavailable or a closed-rails vendor attempt) MUST be reproducible under determinism env pins and closed rails, without reliance on external network or a live database. Preferred posture is exercising the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts. If that is not feasible, use a deterministic stub only to the extent required to produce the canonical envelope and parity artifacts (no live I/O). Acceptance proof MUST include stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and those artifacts MUST be indexable under governed evidence surfaces. Any added scenario MUST have a stable scenario identifier so stored artifacts do not churn.

**PF09 subtask closeout uses evidence-binding first (normative).** When closing a PF09 subtask described as captured elsewhere or piecemeal, the default closure method is to bind existing governed evidence (tests and artifacts) into the epic’s acceptance artifacts (acceptance map and token/evidence matrix). Creating a new evidence family for closeout is allowed only if the epic includes an explicit gap statement describing what is missing from existing evidence and the new evidence aligns to governed artifact conventions. Closure is not complete unless the acceptance artifacts explicitly map the PF09 subtask to concrete evidence. An implicit claim that the evidence exists somewhere else is non-conforming.

**Assigned PF09-subtask coverage is all-or-explicit (normative).** If a PR, remediation slice, QA review, Live QA closeout review, or closeout record claims completion for a defined set of PF09 subtasks, QA MUST account for every assigned subtask explicitly.

* For each assigned subtask, the review or closeout record MUST either:  
  * show that the subtask is supportable as complete from governed repo evidence, or  
  * state that the subtask remains unresolved and explain that outcome in detail.  
* For any assigned subtask not completed, the record MUST identify:  
  * the exact phased PF09 task or subtask ID,  
  * exactly what was completed,  
  * exactly what remains incomplete,  
  * the blocking condition or limiting constraint,  
  * why completion was not possible within the approved PR, OPS, QA, or remediation scope, and  
  * the concrete repo evidence, test result, OPS evidence, QA log, or other mechanical basis for that conclusion.  
* Silent omission, partial completion without this detail, or a blanket claim that the PR, QA run, OPS task, remediation slice, or closeout is complete while assigned subtasks remain unresolved is non-conforming.  
* A review may record a subtask as supportable as Done from governed evidence without treating PF09 as already updated. Until the canon row is changed, the closeout record MUST distinguish support posture from current PF09 document state.

**QA-discovered follow-up work must be PF09-accounted (normative).** QA-discovered follow-up work, Live QA future-work notes, QA RCA recommendations, evidence-loop gaps, OPS-discovered gaps, route-policy gaps, adapter/schema gaps, artifact gaps, index or mirror gaps, path-proof gaps, and build improvements MUST carry either an exact phased PF09 task or subtask mapping or an explicit PF09 gap classification. Backlog, future-work, parking, deferral, or carry-forward language is scheduling posture, not scope authority. QA reports MUST NOT create free-floating backlog items without PF09 mapping or PF09 gap classification.

Explicit “it exists somewhere else” is non-conforming.

**/internal/version coupling proof uses a single governed log artifact (normative).** When an epic claims /internal/version coupling proof and/or two-run identity closure, the governed proof artifact is `artifacts/ops/internal_version/two_run_identity.log`.

This log MUST include, at minimum:

* an explicit two-run identity result (byte-identical or not), and the compared byte identifiers  
    
* an explicit coupling verification result showing the six /internal/version fields match their governing identity sources (titles-only pointers), including release\_id coupling

The log MUST include rails posture and determinism pins references (names-only pointers). The determinism pins themselves remain proven only by their canonical governed log surface. No new acceptance tokens are introduced for coupling proof; the coupling proof is evidence-bound under the existing identity and internal-version token set.

This section upgrades the token/evidence matrix from a good practice to a required closeout gate: no epic that touches QA tokens is ready to be treated as QA ledger complete or ready for closeout until its token/evidence matrix is complete, consistent with the registry, and aligned with acceptance maps, manifests, and the evidence skeleton.

#### **9.2.14.4 Automated alignment guard (recommended)**

For epics that maintain both a token/evidence matrix under `audit/qa/<epic-id>/token_evidence_matrix.md` and an acceptance map (titles-only; see HDE Phased Epics), teams SHOULD add an automated alignment check (meta-test or CI job) that:

* asserts the token sets in the matrix and acceptance map are identical  
    
* normalizes and compares token statuses  
    
* verifies that any token marked implemented has non-empty evidence pointers in both artifacts

This guard is intended to prevent approval drift where matrices and acceptance maps silently diverge between PRs.

#### **9.2.14.5 Token-governance addendum alignment (normative)**

If a token-governance addendum exists that changes any acceptance token naming, aliasing, or acceptance semantics, the Live QA token/evidence matrix and acceptance mapping MUST reflect it.

* Cite the governing addendum by addendum number and title in the matrix notes for each affected token.  
    
* Apply the addendum’s canonical token name and alias rules in all acceptance criteria, manifests, and evidence bindings.  
    
* In closeout, include an explicit note confirming the addendum was applied, and identify any resulting alias rule or waiver.

Failure to reflect an applicable token-governance addendum is a token blocker (see 9.2.15 Token blockers and waivers).

### **9.2.15 Review rails for token blockers, scope waivers, and canonical names**

#### **9.2.15.1 Token blockers (must be treated as BLOCKING)**

* References an acceptance token that does not exist in HDE-Governance and is not explicitly minted in a PF10 addendum (unregistered).  
* References a token name that differs from the canonical spelling in HDE-Governance or PF10 (case, punctuation, separators).  
* Defines acceptance criteria using freeform statements or plan-local aliases instead of canonical token names.

#### **9.2.15.2 Scope waiver notice (plan-time only)**

If a token is out of scope for a given Live QA plan, the plan MUST say so explicitly as a waiver note (do not “silently omit”). Waivers MUST name the token(s) being waived and the reason.

#### **9.2.15.3 Canonical name re-check (required)**

If a token blocker is raised due to spelling or registration:

* The reviewer MUST retrieve the governing token definition in HDE-Governance (titles-only). If the token is newly minted and not yet present in HDE-Governance, the reviewer MUST retrieve the PF10 addendum that explicitly mints the token (titles-only).  
* The reviewer MUST then update the plan/matrix using the canonical name and MUST NOT accept a plan-local alias.

#### **9.2.15.4 Token roster preflight (required)**

Token roster preflight is required for correctness. A Live QA plan MUST include a token roster (names-only) for all in-scope acceptance criteria, using canonical spellings.

A Live QA plan MAY omit per-step token annotations and MAY defer full token-to-step coverage detail, but it MUST NOT omit the token roster entirely and it MUST NOT invent plan-local token spellings.

* If a new acceptance token is truly required, route it through governance registration first (see the governance-first workflow in 9.2.2 Token metadata model (normative)), then update the plan/matrix using the registered canonical name (or the PF10-minted canonical spelling pending drain).

#### **9.2.15.5 Coverage vs QA Plan accounting (required; closeout gate)**

The Live QA closeout record MUST include an explicit Coverage vs QA Plan accounting that is complete, step-by-step, and auditable.

* List every QA Plan step in plan order with a stable step identifier.  
    
* Mark each step as COVERED or UNCOVERED.  
    
* For each COVERED step, point to the evidence artifact(s) produced under the governed QA root for the epic.  
    
* For each UNCOVERED step, include an explicit waiver reference (ADR title only) and a reason.  
    
* Coverage vs QA Plan accounting MUST separately identify any accepted plan-execution deviation that materially changed how a COVERED step was actually run, including bounded Moon Loop reruns, `QA_PLAN_UPDATE`\-routed remediation, rails changes, step-local dependency-preflight corrections, and accepted remediation receipts. For each such deviation, the closeout record MUST name the affected step, state the accepted deviation, identify the original planned receipt or failed receipt when one exists, identify the final accepted receipt or remediation receipt used as the PASS basis, and point to the governed evidence that preserves both the deviation and the final accepted basis.

Unreported gaps are non-conforming. A closeout record that omits this coverage accounting is blocked for approval.

#### **9.2.15.6 Final QA closeout review required elements (required; closeout gate)**

The final Live QA closeout review MUST include an explicit required-elements checklist that confirms the presence or absence of the following, with governed evidence pointers when present:

* the D0 discovery artifact for the epic  
* functional runtime proof on changed runtime surfaces  
* governed current-state QA evidence under the canonical epic QA root  
* the QA RCA and Doc Delta summary for the epic  
* the Coverage vs QA Plan accounting required in §9.2.15.5  
* the overall readiness or closeout recommendation  
* indexed evidence in the Human Evidence Index and the Machine Mirror  
* the execution-venue posture, evaluated as follows:  
  * Codespaces execution and governed Codespaces provenance are required only when venue is expressly material to the approved proof because the claim concerns a Codespaces-specific dependency, integration, operator promise, behavior difference, acceptance criterion, or operational-readiness assertion.  
  * When venue is normative, the review MUST surface the plan’s `Venue-specific claim`, `Why venue can affect the result`, `Required venue evidence`, and `Effect of missing venue evidence`.  
  * When Codespaces is material, the review MUST surface a governed, secret-safe artifact that binds the exact QA check or artifact, Codespaces venue, canonical repository association, execution-source identity, command or command family, material Codespaces-specific property, and sufficient event or chronology information.  
  * When venue is not material, the review MUST record `NOT CLAIMED`, `NOT APPLICABLE`, or `UNKNOWN - NON-MATERIAL`, as appropriate; MUST NOT infer the historical venue; and MUST NOT treat missing Codespaces provenance as an uncovered QA step, QA failure, or closeout blocker.

When a PF10 addendum is the decisive epic-close authority for a closure claim, the closeout review MUST state whether that addendum provides direct evidence-pointer lines or only evidence-basis prose. If the decisive addendum provides only evidence-basis prose, the closeout review MUST record that explicitly and treat it as an auditability caveat rather than silently assuming pointer-complete sourcing.

The closeout review MUST distinguish repo-supported completion from canon drain completion, formal close-pack completion, merge provenance, board state, PO closeout action, and formal OPS action. When any of those later closure axes are not being claimed, the review MUST say so explicitly rather than implying they are complete.

A repo-supported completion summary used for closeout MUST be explicit, reproducible, and limited to repo-supported facts. It MUST distinguish recorded, blocked, and no-claim outcomes, and it MUST NOT silently collapse a blocked or contextual state into PASS prose.

If a bounded Moon Loop remediation changed a step from false blocked to recorded or PASS, the closeout review MUST preserve the pre-remediation context as governed or context artifacts, record the minimal change set at the governed delta path, and make the rerun basis explicit.

#### **9.2.15.7 Acceptability language vs PF09 pre-drain status (required; review gate)**

Current PF09 recorded status text is not a closure gate by itself.

* A PR, OPS task, remediation slice, QA-readiness record, or closeout record MUST use acceptable-status language only when the exact mapped PF09.x task or subtask is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, truthful review and approval artifacts, and the live PF10 record where PF10 explicitly speaks.  
* PF10 is the live in-flight authority where it explicitly covers the mapped work. PF09 remains the checklist mapping and later-drain record.  
* This rule applies at the exact PF09.x mapping level. If a subtask exists, that subtask is the controlling unit. If a slice claims more than one mapped PF09.x subtask, each claimed subtask must independently satisfy this rule.  
* Green tests, bounded diff scope, evidence refresh, successful OPS execution, review-clean posture, token coverage, or green QA checks are necessary but not sufficient by themselves.  
* Before the mapped work is complete in substance, allowed posture language is limited to contributory, intermediate, review-clean, bounded, or supportable from repo evidence.  
* Acceptable, accepted, satisfied, complete-for-close, and supportable for later drain to Done are allowed only when the mapped work is complete in substance, governed evidence proves that posture, and the live PF10 record supports later drain to Done where PF10 speaks.  
* Current PF09 recorded status may be cited only as canon-as-recorded. It MUST NOT by itself block PR acceptability, OPS acceptability, QA entry, QA readiness, or epic close.  
* Review and closeout artifacts MUST distinguish current PF09 recorded status, supported later-drain status, actual implemented state, actual OPS state, and actual governed evidence state.  
* If a slice is not closure-ready, the blocker MUST be stated as real implementation, OPS, evidence, planning, or execution incompleteness. It MUST NOT be stated only as PF09 still saying `Not done` or `Partial`.  
* Review of a bounded approved task MUST stay inside the approved task scope unless the artifact explicitly claims closure. Reviewers MUST NOT widen a bounded PR, OPS task, remediation slice, or validation step to later PRs, later OPS tasks, later validation runs, or whole-epic closure work that the approved task did not claim.  
* If an approved task is explicitly validation-only, sequencing-only, evidence-only, contributory, or otherwise non-closure, PF09 row closure and later close-pack work are not review gates for that task. Reviewers MUST judge the artifact on whether it truthfully completes its own approved purpose, avoids overclaiming closure, and preserves any still-open mapped PF09.x work as open or no-claim where that posture is real.  
* This rule does not require PF09 to be edited in the same PR, OPS task, or QA step. PF09 drain remains later documentation work.

#### Closed-task revalidation `PASS_WITH_NOTE` interpretation (clarification).

For a PF09 task or subtask that is already recorded Done, a later closed-task revalidation may classify the item as supportable with note when all of the following are true:

* the review target is exactly mapped to the phased PF09 task or subtask under revalidation;  
    
* the review is scoped to supportability of an already-closed task, not new QA PASS, new OPS completion, new PF09 status movement, new acceptance-token satisfaction, or epic closeout;  
    
* current repo reality or OPS revalidation evidence proves the relevant behavior, artifacts, and linkage required by that closed task;  
    
* any closed deterministic rails used for local smoke or revalidation are recorded and do not imply live vendor execution, credentialed operation, deployment, migration, PR creation, issue creation, branch creation, board update, PF edit, repo edit by the review, or QA execution;  
    
* the Human Evidence Index contains at least the required key/path binding for each older relied-on artifact;  
    
* the Machine Mirror contains one matching record for each relied-on artifact with `sha256`, `size_bytes`, and `proof_anchor`;  
    
* each Machine Mirror `proof_anchor` points to the matching sibling path-proof transcript, and the mirror hash and size fields match the artifact and path proof;  
    
* the target under revalidation requires artifact existence, indexing, mirroring, and path-proof linkage, not new evidence regeneration or a retroactive Human Index schema migration for older artifacts.

In that situation, a minimal older Human Evidence Index row is a historical evidence-shape caveat, not an automatic downgrade reason. Reviewers may record `PASS_WITH_NOTE`, supportable with note, or equivalent supportability language, but MUST state the caveat and MUST NOT imply that richer Human Evidence Index rows already exist if they do not.

This interpretation does not apply when a relied-on artifact is missing, the Human Index key/path binding is absent, the Machine Mirror record is absent, the sibling path proof is absent, the mirror hash or size does not match, proof anchors do not point to the matching transcript, governed evidence families contradict each other, or the current task requires a new evidence regeneration or schema migration. In those cases, classify the issue as an evidence-integrity failure, tooling blocker, or unresolved supportability gap according to the actual defect.

#### **9.2.15.8 Governed evidence family coherence and documentation-only normalization (required; review gate)**

* For any bounded PR, OPS task, remediation slice, QA-readiness record, or closeout record that depends on a governed evidence family for one claimed closure dimension, that family MUST express exactly one authoritative posture at a time. Mixed-state families are invalid for review and acceptance.  
* If one governed artifact says `closed` while another artifact in the same bounded family says `not yet closed`, `deferred`, `partial`, or an equivalent contradictory posture for the same closure dimension, the family is mechanically non-acceptable until normalized.  
* A consolidation, review, or closeout record MUST NOT summarize contradictory source bytes as though they were one coherent truth surface. When runtime facts are stable but the governed family disagrees, reviewers MUST classify the defect as a documentation or evidence failure rather than as a new runtime failure.  
* Documentation or evidence normalization may be accepted instead of a rerun only when the relied-on runtime facts are unchanged and already evidenced, no new runtime command, route behavior, environment binding, or OPS action is being claimed, and every governed artifact in the affected family is refreshed to the same authoritative posture with coherent Human Index, Machine Mirror, checksum, and required path-proof updates in the same change.  
* When equivalence or substitution is used instead of an independently exercised runtime, the approval artifact or governing plan MUST state the closure mode explicitly before the governed evidence family is rewritten.  
* If the approved task is only to normalize documentation or evidence posture for a bounded slice, review MUST stay bounded to that task. Full epic closure is not a blocker unless the approved task explicitly claims full closure.

# 10\. QA checklists, harnesses, and review rules

PF19 is the canonical home for the QA checklists, QA harness requirements, evidence-quality and failure-classification rules, exact later-drain QA vocabulary, and QA review semantics in this section. `PF27-Canon-Plan-Templates` owns reusable structure for its declared plan, runbook, review, and closeout classes. `PF06-Canon-Epic-Process-Guide` owns process sequencing, `Remediation Task Plan` structure, and its declared PR review-pack structures. `PF12-Canon-HDE-Schemas-and-Artifacts` owns governed schemas, catalogs, artifact paths, canonical bytes, and evidence-refresh mechanics. This section states only the PF19-owned QA rule or the minimum applicability boundary needed to route safely; it does not reproduce owner-controlled template or schema contracts.

## 10.1 Pre-commit QA checklist

Anchor: “Pre-commit QA checklist”.

Purpose. A reusable checklist that teams can apply to CI configuration to enforce:

* lint \+ format  
    
* JSON/JSONL canonicalization and final-LF checks  
    
* deterministic, no-I/O tests  
    
* snapshot hygiene and env pins

Notes. PF19 defines the required QA items. The applicable phased PF09 document controls phase scope, `PF12-Canon-HDE-Schemas-and-Artifacts` controls governed evidence formats, and checked-in CI is the source for current implementation reality.

## 10.2 Post-commit evidence-capture checklist

Anchor: “Post-commit evidence-capture checklist”.

Purpose. A step-by-step recipe to:

* capture headers/body snapshots (Text, Suppressed, A7 surfaces)  
    
* generate composite proof JSON (when A7 is in scope)  
    
* update docs/evidence/INDEX.json \+ .sha256 and artifacts/evidence\_index.jsonl in the same PR

Governed roots only. All indexed artifacts MUST live under a governed evidence root declared by `PF12-Canon-HDE-Schemas-and-Artifacts`. Transient/generator paths are forbidden as sources for indexed evidence.

Header normalization. Normalize header names to lower-case before persisting governed snapshots.

For each new or changed governed artifact under a governed evidence root, the capture workflow MUST:

* create or update a co-located \<artifact\>.path\_proof.txt file, and  
    
* ensure there is exactly one Mirror record whose proof\_anchor points at that path\_proof.txt

Treat “artifact present but no path\_proof” and “path\_proof present but no Mirror record” as QA failures, not as minor hygiene issues.

For lifecycle and OPS-managed artifacts (for example backup/restore probes), confirm that the associated evidence changes (artifact \+ path\_proof \+ Mirror) land in the same PR as the code or configuration change they support.

`PF12-Canon-HDE-Schemas-and-Artifacts` controls the schemas, governed roots, canonical Index and Mirror bytes, path-proof contracts, and refresh mechanics used by this checklist.

## 10.3 Validated-tuple QA harness for Aux and CLI parity

Anchor: “Validated-tuple QA harness for Aux and CLI parity”.

Purpose. A small, repeatable harness that:

* takes fixed test tuples as inputs  
    
* sets env pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`)  
    
* invokes the shared emitter path used by HTTP and CLI (no alternate serializers)  
    
* calls Aux via BE/CLI and writes snapshots under tests/transport/headers/:  
    
  * aux\_text\_200.snap  
      
  * aux\_suppression\_200.snap

Notes. Runs without env-gates; the CLI preview is always available and calls the same emitter as Aux. Parity artifacts are indexed in the same PR.

## 10.4 A7 proof-capture recipe

Anchor: “A7 proof-capture recipe (Catalog /reader)”.

Purpose. A reusable recipe that:

* captures GET/HEAD/304 headers for the Catalog JSON success route  
    
* verifies strong quoted ETag, Vary, and encoding invariance  
    
* captures env-gate proof (non-prod entries unreachable in prod)  
    
* builds and validates composite A7 proof JSON against the schema owned by `PF12-Canon-HDE-Schemas-and-Artifacts`

Preconditions (merge gate). Before capturing any A7 proofs, the harness must:

* verify that docs/ENDPOINTS\_CATALOG.json exists and that the Reader JSON success route is present and marked as a Catalog JSON surface, and  
    
* abort with a clear QA failure if the Catalog entry is missing or invalid (no partial A7 runs)

After capturing proofs, the harness must:

* update docs/evidence/INDEX.json \+ .sha256 and artifacts/evidence\_index.jsonl in the same PR, and  
    
* run the mirror quick-check (§10.5)

Failure to index or mirror any A7 artifact means the A7 gate is not satisfied, and no A7 tokens may be claimed for that PR.

## 10.5 Machine Mirror schema quick-check

Anchor: Machine mirror schema quick-check.

Purpose. A small tool or CI step that:

* loads `artifacts/evidence_index.jsonl`  
    
* verifies:  
    
  * sorted keys and pinned field order  
      
  * exactly one LF per record  
      
  * canonical JSONL form  
      
  * rejection of unknown keys

Notes. PF19 names the required QA checks. `PF12-Canon-HDE-Schemas-and-Artifacts` defines the Mirror record schema and field-order rules. The repository provides the quick-check implementation.

### Invocation rule (normative; operator-facing)

In the engine repo, `ci/checks/check_mirror_schema.sh` is a Python entrypoint at a legacy stable path and begins with a Python shebang. The `.sh` suffix identifies the retained path; it does not declare the interpreter.

Run the gate from the repository root. The preferred explicit-Python form is:

* `python ci/checks/check_mirror_schema.sh`

Direct execution is also supported when executable mode and shebang handling are guaranteed:

* `ci/checks/check_mirror_schema.sh`

A Python harness SHOULD use its active interpreter explicitly, equivalent to:

* `[sys.executable, "ci/checks/check_mirror_schema.sh"]`

The validator reads the fixed repository-relative input `artifacts/evidence_index.jsonl`. It does not accept a caller-selected Mirror path. New plans, harnesses, and operator instructions MUST omit the unused `artifacts/evidence_index.jsonl` operand.

The following invocations are invalid:

* `bash ci/checks/check_mirror_schema.sh`  
    
* `sh ci/checks/check_mirror_schema.sh`

Shell-parser output from an invalid shell invocation is an invocation defect, not a Machine Mirror schema finding. A missing-Mirror result obtained outside the repository root is a locus defect until the supported command is evaluated from the repository root. Either defect may be normalized by rerunning the supported invocation from the correct locus. Only the supported invocation’s exit status and validator output may establish the Mirror-schema result.

Plans and governed evidence MUST preserve the command actually executed and MUST NOT rewrite a shell-parser failure as validator behavior.

`PF12-Canon-HDE-Schemas-and-Artifacts` \> `Refresh sequence (normative)` currently shows `ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`. That operand form does not match the checked-in fixed-input implementation or the current CI call sites and MUST NOT be copied into PF19. This is an out-of-section PF12 documentation discrepancy; this rule does not claim that PF12 has been corrected.

Any future migration to a `.py` path is an intentional compatibility change. It must update active CI, sanity orchestration, QA harnesses, tests, operator documentation, and current canon references; preserve historical evidence and command transcripts; and preserve both supported legacy call shapes until explicit-Python callers have been drained. No suffix-only cleanup or partial caller migration is authorized by this rule.

## 10.6 Remediation QA evidence and review rules

### Artifact and owner boundaries

`PF27-Canon-Plan-Templates` \> `4) Remediation Implementation Guide (Template)` is the single reusable template home for a `Remediation Implementation Guide`. `PF06-Canon-Epic-Process-Guide` Appendix B retains only the process purpose and scope. PF19 retains QA evidence quality, failure classification, review semantics, and QA standard playbooks that are not template shape. A `Remediation Implementation Guide` is not a `Remediation Task Plan` and is not an `Epic Remediation Plan`.

`PF06-Canon-Epic-Process-Guide` \> `Appendix C — Remediation Task Plans (DEV PRs + OPS tasks)`, including `Canonical Remediation Task Plan Template (paste-ready)`, is the canonical structure and approval-gate home for the distinct `Remediation Task Plan` artifact. PF06 controls its PR and OPS task model, `DISCOVERY` and `CHANGE` intent, cross-lane dependency line, execution-ready and approval gates, required outputs and verification, OPS authorization and evidence capture, in-flight command posture, mechanical blockers, remediation-only planning boundary, portability and provenance fields, and paste-ready fields. A `Remediation Task Plan` is not an alias, rename, or subtype of either PF27 remediation artifact.

`PF12-Canon-HDE-Schemas-and-Artifacts` controls governed evidence schemas, paths, canonical Index and Mirror bytes, path-proof contracts, and refresh mechanics. The applicable `PF27-Canon-Plan-Templates` or PF06 artifact class controls reusable review structure, wrapper guards, and an `ASK OK?` submission sentinel where its template requires one. PF19 does not reproduce those owner-controlled contracts. PF19 QA requires that missing, incoherent, stale, or misbound governed evidence cannot support the claimed result.

### Evidence-package caveats and failure history

Evidence-package caveat handling is as follows.

Uploaded deliverables packages, zipped check logs, generated archives, copied package listings, or exported report bundles are not standalone proof when their selected entries are missing, unreadable, empty, zero-byte, malformed, or otherwise not reviewable. A package defect is not automatically a product failure, but it is an evidence-package caveat that must be recorded.

A package caveat may be non-blocking only when all of the following are true:

* the caveat is recorded by PF10, the closeout review, or the QA RCA;  
    
* current repo evidence supplies the same proof target under governed roots;  
    
* the current repo evidence is readable and non-empty;  
    
* the current repo evidence is tied to the same QA event, check ID, proof target, or closeout step;  
    
* required path-proof, index, mirror, hash-sentinel, or manifest coverage remains coherent where applicable;  
    
* the closeout review names the package caveat and the alternate governed repo proof.

If any of those conditions is false, classify the package issue as an evidence-integrity defect, `TOOLING_BLOCKED`, or unresolved closeout evidence gap according to the actual defect.

When a failed QA check is later accepted through remediation or rerun evidence, the original failed primary log or failure record must remain visible as failure context unless it is genuinely unavailable. The final PASS basis must name the accepted remediation or rerun evidence and must not relabel the original failure as if it never occurred.

### EPIC022 remediation evidence patterns

These patterns are retained as PF19 QA playbook content rather than as the `Remediation Task Plan` template identity. They do not rename a PF06 task, invent current repository loci, or claim that an EPIC022 example is current implementation truth.

The following patterns are the default posture for remediation task plans unless a plan explicitly states why a different pattern is required.

PR-01 (DISCOVERY-only) discovery report posture (copy/paste safety):

* PR-01 deliverable is exactly one discovery report file under `audit/qa/<epic-id>/remediation/<REMEDIATION_SUBPATH>`, with no code/test/script changes.  
    
* If the report includes Evidence Index/Mirror update commands, the default copy/paste command MUST NOT include an epic-id flag from another epic.  
    
* If the evidence tooling supports an \--epic-id flag, treat it as optional and non-default in the report. If included at all, it must match the current epic and must be clearly labeled as optional.  
    
* If a placement decision is not yet enforced by tests (example: request-chain manifest placement), the discovery report MUST mark the location as TBD and constrain options to the smallest set that matches observed governed placement patterns and enforcing tests. Do not present an unverified fits at \<path\> as settled.

OPS-01 host reachability probe (read-only discovery; evidence bundle):

* When an OPS task selects a single prod host/base\_url for follow-on runtime probes, the OPS evidence bundle SHOULD include:  
    
  * a host reachability matrix file and explicit selection outputs (for example host\_matrix.md, selected\_base\_url.txt, selected\_host\_label.txt)  
      
  * a raw headers capture file that includes the HTTP status line and at least one header line (for example headers\_raw\_SELECTED.txt)  
      
  * a stderr capture for the HTTP tool (for example curl\_stderr\_SELECTED.txt)  
      
  * a structured headers sample in JSON with lower-case header keys and required keys status\_line and headers (for example headers\_internal\_version\_sample.json)

Evidence quality note (portability):

* Artifacts MUST be file bytes written by commands. Avoid copy/paste noise.  
    
* If a table or excerpt contains terminal control sequences, treat it as a portability risk. Regenerate the artifact so the on-disk file is plain text.

OPS-02 runtime bundle capture (open rails; portable snapshot):

* When an OPS task runs a runtime probe and copies a governed artifact family into an audit bundle for portability, the bundle SHOULD include:  
    
  * a command transcript split into files (for example run\_command.txt, run\_stdout.txt, run\_exit\_status.txt)  
      
  * an expected-vs-actual artifact inventory (for example expected\_artifact\_files.txt and file\_list\_actual.txt)  
      
  * a remediation-only snapshot manifest that enumerates sha256 and size for each copied file (for example remediation\_only/manifest\_snapshot.json and remediation\_only/manifest\_snapshot.json.sha256)  
      
  * any newly introduced governed artifacts plus their sibling path proofs when copied (for example request\_chain\_manifest.json and request\_chain\_manifest.json.path\_proof.txt when present in the governed family)


* If a plan claims checksum validated for a produced .sha256 file, the OPS evidence bundle SHOULD include the verification command output as evidence (do not rely on a prose assertion).

PR-03 Index/Mirror regeneration (integration summary \+ exclusion check):

* Any PR that regenerates governed Index/Mirror/proofs SHOULD include an integration summary artifact under the epic remediation QA tree that records:  
    
  * the exact regeneration and validation commands executed under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0` plus env pins), and  
      
  * an explicit inclusion check for any new required evidence family entries (for example request-chain manifest mirrored with a valid proof\_anchor), and  
      
  * an explicit exclusion check that remediation-only bundle paths are not indexed (for example no matches for a remediation-only subtree across `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`).


* Broad path-proof refresh touching other indexed artifacts is non-blocking when it is the natural outcome of running the canonical full regeneration.

When the approved work touches governed Index or Mirror evidence, use `PF12-Canon-HDE-Schemas-and-Artifacts` \> `Refresh sequence (normative)` for the complete output, path-proof, and refresh contract, and apply the no-operand Mirror invocation in `10.5`. Do not substitute a copied PF19 roster for the PF12 contract.

### Retrieval-first and negative-proof review

AI reviewers of QA plans, Live QA reviews, QA closeout analysis, remediation guides, repo audits, and related QA review artifacts MUST use a retrieval-first, proof-first workflow: use PF10 first where it explicitly speaks; read the current artifact end-to-end; consult the owning PF canon home for each specific issue; and prove repo-reality claims before asserting paths, commands, routes, environment variables, test IDs, artifact paths, or component homes. When repo reality matters, use exact-string search before broader search, and keep unproven loci as `UNKNOWN` or `BLOCKED` rather than guessing. Findings MUST distinguish canon requirement, observed repo reality, and inference, and MUST anchor to verbatim source text plus controlling proof.

When a QA review, repo audit, PF23 consult, or closeout check proves that a searched-for blocker, path, route, token, command, artifact, or contradiction is absent, that negative result is still proof if it is mechanically captured with source, search term, scope, and visible neighboring context. Reviewers MUST NOT trigger a rerun, fallback audit, or blocker solely because the proof is negative. If the negative proof is incomplete, ambiguous, or not mechanically captured, classify the issue as insufficient proof or `TOOLING_BLOCKED`, not as a behavior failure.

## 10.7 Later-drain QA semantics

PF19 governs the exact later-drain QA vocabulary and the evidence-sufficiency, failure-classification, and nonclaim semantics for a later-drain recommendation. `PF27-Canon-Plan-Templates` governs reusable field placement for its declared plan, review, and closeout classes. `PF06-Canon-Epic-Process-Guide` governs reusable field placement for its declared PR review-pack classes. Use the complete owner block where that class already has one and normalize its QA vocabulary to the exact PF19 values. Until the declared owner contains a complete destination, retain the missing field coverage here as an explicitly transitional compatibility rule. A later-drain recommendation does not perform a PF-canon update, move PF09 status, establish QA PASS, close an epic, or make documentation drainage a gate for the approved work.

A later-drain statement applies only when a covered approval artifact is intentionally being used to support a later PF-canon drain. It does not move the drain earlier or make drainage an implementation, approval, QA, OPS, merge, completion, or closeout prerequisite. Approval artifacts MUST NOT stop at vague language such as accepted, complete, merge-ready, approved, or no further remediation needed when the practical intent is to support a later PF-canon update.

### Artifact-class routing

| Covered artifact class | Durable field-placement owner | PF19 treatment |
| :---- | :---- | :---- |
| PF06 PR final review pack | `PF06-Canon-Epic-Process-Guide` `4.6 PR review pack template — provenance, diff review, RCA, and pass proof` | Use the owner’s complete field family, but normalize the two divergent value families to the exact PF19 vocabulary below. |
| PF06 docs-only PR final review pack | `PF06-Canon-Epic-Process-Guide` `4.7 PR review pack template — docs-only PR (Lead Dev gate)` | Retain only the missing fields as transitional compatibility coverage when the review intentionally supports later drain. |
| PR remediation acceptance review | `PF27-Canon-Plan-Templates` `5) Remediation Review Record (Template; REVIEW mode only)` | Use the complete owner block. Retain PF19 vocabulary, evidence sufficiency, and failure/nonclaim semantics without duplicating the fields. |
| Epic closure or final close-pack review | `PF27-Canon-Plan-Templates` `10) Epic Closure Review + Retrospective (Template; REVIEW mode only)` | Use the complete owner block. Retain PF19 evidence-sufficiency and no-overclaim semantics without duplicating the fields. |
| OPS task final review | `PF27-Canon-Plan-Templates` `11) Ops Task Final Review Record (Template; REVIEW mode only)` | Use the complete owner block. Apply PF19 interpretation only when QA evidence is in scope. |
| `Implementation Closeout Report` | `PF27-Canon-Plan-Templates` `7) Implementation Closeout Report (Template; REVIEW mode only)` | Retain only the missing fields as transitional compatibility coverage until the owner contains a complete destination. |
| `QA Pass Review Record` | `PF27-Canon-Plan-Templates` `8) QA Pass Review Record (Template; REVIEW mode only)` | Retain only the missing fields as transitional compatibility coverage when the review is intended to feed later drain. |
| `Final QA Closeout Review + QA RCA` | `PF27-Canon-Plan-Templates` `9) Final QA Closeout Review + QA RCA (Template; REVIEW mode only)` | Retain only the missing fields as transitional compatibility coverage when later drain is intended. |
| Implementation-plan or QA-plan approval artifact | Its applicable PF27 plan template and `Review guardrails` | Preserve the missing current-posture, readiness, and epic-close-expectation fields as transitional compatibility coverage; drainage remains non-gating. |

A general PR final or remediation review without a declared artifact identity MUST first be classified to the exact PF06 or PF27 type that matches its purpose. Do not apply one generic PF19 form across unlike review classes. An `Epic Remediation Plan` or another PF27 artifact not named above has no automatic `10.7` applicability; its intentional later-drain purpose and exact template applicability must be explicit.

### Exact PF19 QA vocabulary and semantics

`Supported later-drain action` MUST use exactly one of:

* `change to Done`  
* `change to Partial`  
* `change to Not done`  
* `change to Consolidation pending`  
* `change to Optional`  
* `No status change recommended`

`Drain readiness classification` MUST use exactly one of:

* `Supportable from repo evidence`  
* `Not yet supportable from repo evidence`  
* `Already drained into PF-canon`

`Epic-close expectation` MUST use exactly one of:

* `at epic close`  
* `after an additional PR or OPS slice`  
* `after a separate canon-only drain step`

`Supportable from repo evidence` is a recommendation posture, not a PF09 status change, edited PF document, board transition, token PASS, QA PASS, epic closure, completed PF10 drain, or Product Owner action. `Already drained into PF-canon` is valid only when the exact current canon bytes establish that the drain occurred. An epic-close expectation is a timing recommendation, not an accomplished close or drain.

PF06 §4.6 currently uses `Already drained into PF-Canon`, `Supportable from repo evidence only`, and `drain at epic close` as near-match variants. Those spellings are not additional allowed values. This is an out-of-section PF06 documentation discrepancy; this rule does not claim that PF06 has been corrected.

### Transitional compatibility fields

For a covered class whose durable owner lacks a complete, vocabulary-conforming destination, include only the fields missing from the owner’s current block, selected from this seven-field compatibility set:

* `Affected PF canon home(s)` — name only current canon homes actually affected by the evidence; do not infer ownership from filenames or plans.  
    
* `Exact affected locator(s)` — use exact, current, reviewable locators; unresolved locators remain unknown rather than guessed.  
    
* `Current canon posture` — derive this from current permanent canon plus an applicable active PF10 addendum where one explicitly speaks; if the reviewed evidence does not establish posture, say so explicitly.  
    
* `Supported later-drain action` — use exactly one value from the PF19 action vocabulary above. The recommendation does not perform the status move or canon drain.  
    
* `Drain readiness classification` — use exactly one value from the PF19 readiness vocabulary above. Current evidence controls supportability; current canon bytes alone establish `Already drained into PF-canon`.  
    
* `Evidence basis` — provide exact, readable, relevant, coherent, secret-safe evidence pointers. Vague approval language is not an evidence basis.  
    
* `Epic-close expectation` — use exactly one value from the PF19 timing vocabulary above. The value does not establish QA PASS, closure, a board move, or an accomplished drain.

Do not reproduce this compatibility set for PF27 sections 5, 10, or 11, or for another class whose owner already contains a complete, vocabulary-conforming block. Remove transitional PF19 coverage for a class only after its complete current owner destination is verified and its vocabulary is reconciled.

# 11\. Roles & RACI (QA)

## **11.1 QA roles (titles-only pointer to PF06)**

### **Ops tasks (QA-specific boundary; general process routed to PF06)**

PF06-Canon-Epic-Process-Guide defines general Ops task identity, authorization and execution, IA facilitation, required task-record fields, process flow, handoffs, and non-QA responsibilities. PF19 does not restate or override those rules.

QA-specific boundaries are as follows:

* An Ops task that supplies an input or result to QA remains Ops work. The Product Owner retains authorization, accountability, and acceptance. Execution may be performed by the PO or by an automated session agent only through the explicit delegation, scope, safety, evidence, redaction, and completion-claim controls in PF06-Canon-Epic-Process-Guide.  
* When applicable canon already provides concrete operator instructions, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules, the QA plan or QA-facing Ops record MUST carry those instructions explicitly. This does not authorize invention; missing or ambiguous instruction detail must remain identified as unknown.  
* Ops execution evidence is stored under `audit/ops/<epic-id>/<task_id>/`.  
* When QA consumes an Ops result, the QA check's governed receipt is `audit/qa/<epic-id>/checks/<check_id>/primary.log`; its required sibling proof is `audit/qa/<epic-id>/checks/<check_id>/primary.log.path_proof.txt`. The receipt points to the distinct Ops evidence instead of copying the Ops lane into an unclassified QA child directory.  
* Evidence MUST NOT include secret values. Sensitive settings are captured only as presence-only, redacted, or approved hashed posture while remaining sufficient for verification.  
* PF references remain titles-only.

### **Implementation Agent (IA)**

* Responsible for designing the QA plan for each epic (what to prove, which playbooks apply).  
* Responsible for making sure pre-commit and post-commit checklists are followed.  
* Responsible for collecting QA artifacts (snapshots, logs, proof JSON) and placing them under governed paths.  
* Responsible for updating the Human Index and Machine Mirror in the same PR as the evidence.  
* Consulted on QA-relevant ambiguities during CodEx runs.  
* Informed about any QA deviations CodEx introduces.

### **CodEx**

* Responsible for executing QA steps defined by the IA:  
  * running pre-commit and post-commit QA jobs  
  * capturing headers/snapshots/proof JSON  
  * generating CLI/SDK parity artifacts  
  * running mirror quick-checks  
* Responsible for reporting QA outcomes in the change report (what passed, what was skipped, what failed).  
* Consulted on feasibility of QA harnesses and CI wiring.  
* Informed about process constraints from PF06/PF19.

### **Lead Developer**

* Accountable for QA coverage per epic: ensuring the right playbooks were applied and the right tokens are satisfied.  
* Accountable that HDE playbooks (§5.1/§5.2/§5.5/§5.6) ran and required tokens are satisfied; merge-block if same-PR evidence parity (human index \+ mirror) is missing.  
* Responsible for PR gate review on QA:  
  * verifying tokens (names-only) such as QA\_PRECOMMIT\_CHECKLIST\_OK, A7\_*OK, NARROK, EVIDENCE\_INDEX*\*\_OK  
  * verifying evidence is present and indexed (same-PR rule)  
* Consulted on any QA scope changes or exemptions.  
* Informed of any QA failures that block merge.

### **Product Owner (PO)**

* Accountable for accepting or rejecting an epic with its QA state.  
* Responsible for merging only when QA tokens and artifacts meet the agreed bar.  
* Informed about QA risks or exceptions flagged by Lead Dev/IA.  
* Consulted when trade-offs are needed (e.g., partial QA vs timeline).

### **Scrum Master**

* Responsible for tracking QA completion across epics (which tokens are satisfied, which playbooks have run).  
* Responsible for reflecting QA state on boards and in sprint reports.  
* Informed after merges so that QA outcomes are recorded.  
* Consulted on QA workload, sequencing, and coordination between FE/BE/HDE teams.

## **11.2 Component ownership**

PF19 is the orchestration guide for QA. Day-to-day ownership of specific playbooks lives with the corresponding component leads; infra/ops own the underlying environment wiring and dev harness surfaces.

* FE Lead / App Frontend owner  
  * Responsible for keeping the App Frontend playbook (§5.4) accurate and current (tools, routes, thresholds).  
* BE Lead / App Backend owner  
  * Responsible for the App Backend (non-HDE) playbook (§5.3), including error posture proofs and endpoint coverage.  
* HDE Lead / Engine owner  
  * Responsible for the HDE Catalog/A7 (§5.1) and Aux & CLI preview (§5.2) playbooks, including reviewed tokens and proof surfaces.  
* DB/Vendor ingest owner (usually BE)  
  * Responsible for the DB & Vendor ingest playbook (§5.5), ensuring ingest jobs, DB schemas, and pack flows are accurately reflected.  
* CLI/API & SDKs owner  
  * Responsible for the CLI/API & SDKs playbook (§5.6), including AB/BA parity, two-run identity, and emitter parity artifacts.  
* Infra / Ops owner  
  * Responsible for environment and service wiring that QA depends on, including:  
    * Reader/service start commands and ports per environment (for example dev/Codespaces vs staging/prod), as documented in Glow Infrastructure and HDE-Mechanics Guide (titles-only), and  
    * internal/dev HTTP harnesses (for example /internal/dev/sampler), including:  
      * canonical dev start commands or service definitions that run the Reader with APP\_ENV=dev and required determinism rails, and  
      * infra-owned base URLs and ports from which concrete harness URLs (such as DEV\_SAMPLER\_URL) are derived and validated before use.  
  * Infra/Ops MUST validate dev harness URLs and start commands (for example via a simple HTTP/1.1 JSON POST and header/body checks against the owning PF docs, titles-only) before handing them to QA.  
  * QA/PO MUST NOT guess or redefine these URLs; missing or unclear dev harness wiring is treated as an infra/spec gap per §11.3, not as a QA improvisation task.

For each component:

* The component owner is Responsible for keeping its playbook or wiring up to date.  
* The Lead Dev is Accountable that all required playbooks for an epic are applied and that environment wiring (including dev harness URLs) is in place before Live QA is attempted.  
* The IA is Responsible for invoking the right playbooks, consuming infra-owned URLs and start commands, and wiring them into CodEx instructions without guessing.  
* The Scrum Master is Informed about which playbooks and harnesses were run and what passed/failed.

## **11.3 Canon-first rule for Implementation Agents**

Implementation Agents are required to follow a canon-first workflow when planning QA for any epic.

Canon-first inventory (before planning) is required. Before drafting a QA plan or asking the Product Owner for environment details, the IA MUST read, by title:

* Glow Infrastructure for infra and environment facts (for example Railway service names, base URLs, DB instances and schemas)  
* HDE-Build Notes for relevant addenda and cross-epic QA guidance  
* HDE Phased Epics for the epic’s D-goals and acceptance roster  
* this guide (Glow QA Guide) for QA tokens, rails, and playbooks

PF07-derived vs PF07-gap posture (normative).

* Any QA plan, Live QA runbook, review artifact, remediation guide, implementation guide, or epic QA document that includes an infra or ops dependency MUST bind that dependency in exactly one of two ways:  
  * PF07-derived posture: the exact required value already exists in Glow Infrastructure and is cited directly.  
  * PF07-gap posture: the exact required value is missing from Glow Infrastructure; the document identifies the exact missing value set and marks the affected step or claim blocked by missing PF07 inventory.  
* QA artifacts MUST NOT use placeholder language such as “infra to provide”, “ops to confirm”, “ask infra”, or “await ops details”.  
* QA artifacts MUST NOT guess hostnames, ports, service URLs, start commands, environment bindings, config-key values, or canonical QA-root patterns.  
* When an infra or ops dependency is executable rather than blocked, the artifact MUST name the concrete provider, project, service, base URL or port, config key, and governed QA root, as applicable.  
* When a PF07-gap exists, the document MUST stop at the gap, record the intended Glow Infrastructure update or doc-delta follow-up, and MUST NOT convert the missing value into an executable QA instruction.  
* This applies to bindings such as `DEV_SAMPLER_URL`, `HDE_BASE_URL`, `DATABASE_URL`, `DB_BRIDGE_URL`, production service URLs, environment-specific ports, and canonical QA-root patterns.

Documented client-access default for local-style dev and QA surfaces (normative).

* When a QA plan, Live QA runbook, remediation guide, or review artifact needs to show a non-prod client access address for a local or local-style surface, the default documented host MUST be `127.0.0.1`, not `localhost`.  
* This is a client-access convention only. It MUST NOT be used to redefine service identity, canonical infrastructure values, or the underlying server bind address.  
* The correct port, path, and any prod-facing target must still come from Glow Infrastructure or the other owning canon homes.  
* Production and other prod-facing surfaces MUST keep their real hosted service URLs or other real infrastructure addresses.  
* If a surface is not actually reachable at `127.0.0.1` from the intended operator context, the artifact MUST record an explicit exception and the real access route. It MUST NOT guess a forwarded hostname or alternate URL.

If those documents already specify an infra/env value (for example a prod base URL, DB name, or rails pattern) and do not mark it as OPEN/TBD, the IA MUST NOT treat that value as a PO input.

Asking for information vs spec gaps applies:

* IAs MUST NOT ask the PO to fill in canonical infra/env values that PF-Canon already defines; doing so is treated as a spec violation, not a harmless shortcut.  
* If PF-Canon is missing or contradictory on a required detail, the IA must:  
  * mark the affected QA step as blocked by spec ambiguity  
  * capture any available evidence, and  
  * propose a PF10 or HDE Phased Epics gap note,  
    rather than improvising new rails or asking the PO to guess.

Separation of closed-rails determinism vs open-rails prod checks applies:

* Closed-rails determinism (`SAFE_MODE=1`, `ALLOW_NETWORK=0` with env pins) is reserved for determinism-sensitive jobs (serializer determinism, env rails checks, sanity pipeline, config determinism), as described in this guide and HDE-Build Checklist.  
* For PROD checks (for example Reader/Aux parity, CLI flows against prod), IAs must treat prod as the Railway service and DB defined in infra canon and design QA steps that use open rails from a QA console (such as Codespaces) to reach those prod surfaces, using determinism evidence (two-run identity and governed artifacts) rather than forcing `ALLOW_NETWORK=0`.

Validated reference requirement (normative):

* Repo paths and file names referenced in plans and IA prompts MUST be backed by one of the following evidence categories:  
  * Canon citation: cite the PF doc title and the section that defines the path.  
  * Verbatim consult quote: a verbatim PF23 anchor quote that is explicitly labeled as consult input.  
  * Inspection transcript: a captured command output transcript stored under governed QA write roots.  
* Planning audits may be referenced in the plan narrative but must never appear in Codex or IA implementation prompts. Implementation prompts should be portable from canon plus explicit inspection transcripts.  
* If a path cannot be validated, the IA MUST treat it as BLOCKED and ask for the exact location rather than guessing.

Any QA plan that ignores this canon-first rule or treats canonical infra/env values as PO-supplied inputs is non-conforming with PF19 and should be rejected or revised before implementation.

# 12\. Change control

## **12.1 Living document**

* PF19 is a living QA guide.  
    
* References to PF10 — HDE-Build Notes must always be by title only (no version numbers, no inlined content).  
    
* When a PF10 item is “drained” into a canonical PF doc (for example PF04, PF09, PF12, etc.), PF19 must be updated to:  
    
  * point at the new canonical home by title, and  
      
  * remove or rewrite any stale notes that referenced the interim PF10 guidance.


* Apply PF03 — Technical Writing Best Practices discipline:  
    
  * keep a single home for each rule,  
      
  * avoid duplicating bytes/schemas/tokens,  
      
  * use clear, minimal redlines when updating PF19.

## **12.2 Supersession rule (PF10 addenda)**

* PF10 Build Notes are a living input stream. Do not reference PF10 by version strings.  
    
* When referencing PF10 guidance in PF19 or in a Live QA plan, cite PF10 by addendum number plus addendum title (stable unit), not by brittle subsection/paragraph anchors.  
    
* When multiple PF10 addenda address the same topic, a later (higher-numbered) applicable addendum governs only overlapping scope or guidance it explicitly supersedes; distinct unsuperseded portions remain authoritative.  
    
* If an addendum is intended to supersede earlier guidance, it should explicitly name what it supersedes (to reduce ambiguity during drainage and review).  
    
* When PF10 references QA acceptance tokens, canonical token names and normative semantics live in HDE-Governance (and other owner canon as applicable). If a token spelling is newly minted and not yet present in HDE-Governance, the canonical spelling MUST be sourced from the PF10 addendum that explicitly mints it (titles-only) until drained. PF19 §9.2 provides the QA operational mapping and evidence bindings.

# **13\. EPIC QA History**

This section is an event-bounded history and learning record. It is not a complete epic timeline, a current acceptance roster, a current PF09 status ledger, or a substitute for current owner canon.

Maintenance rule: preserve each selected epic's status posture at that event, preservation surfaces, material qualifications and nonclaims, and QA learnings or caveats needed to interpret future QA. Do not silently convert historical or advisory text into current work, current status, acceptance, closeout, or implementation claims.

## **Classification and current-owner routing**

The decision-unit identifiers below preserve the refresh guide's traceability. The classification is controlling:

* `H` means historical fact. The associated text records the named event and has no present acceptance effect.  
* `L` means reusable non-normative QA learning. The associated text is advisory and does not independently mandate a check, artifact, blocker, PASS predicate, status, or future task.  
* `C` means current requirement. The historical trigger remains in this section, while the current rule is controlled exclusively by the identified owner home.  
* Modal words retained inside an `H` or `L` event record describe the historical rule or learning only. They have no independent current normative force.  
* These classifications do not move PF09 status, create work or an acceptance token, establish QA PASS, change board state, or perform closeout.

### **Current-requirement owner routing**

| Unit | Current owner and bounded treatment |
| :---- | :---- |
| SRC-0144 | PF19 H1 13 opening, `Maintenance rule`. Keep this as the current local document-control rule for H1 13 only. |
| SRC-0189 | `PF27-Canon-Plan-Templates` \> `QA planning QoS guardrails - templates, deferred steps, and prompt-family separation` \> `Template semantics: future-step artifacts`. H1 13 keeps the EPIC025 provenance only. |
| SRC-0190 | The same PF27 guardrail section \> `Prompt-family separation: AUTHORING vs REVIEW modes for QA prompts` and `QoS stop-rule: iteration churn escalation`. H1 13 keeps the historical trigger only. |
| SRC-0191 | PF27-Canon-Plan-Templates \> `Evidence posture and directory structure` \> `Step-log header schema expectations (required; v2)` and `Template and correction boundaries`. `MODO_*` remains noncanonical. The EPIC025 six-variable header-writer export list is historical and must not override the v2 header contract. |
| SRC-0251 | PF19 10.6 \> `Artifact and owner boundaries`, together with PF12-Canon-HDE-Schemas-and-Artifacts 8.17 current-state path, manifest, proof, and refresh contracts. Stale, incoherent, or misbound current evidence cannot support the claimed result. |
| SRC-0356 | PF19 10.6 \> `Artifact and owner boundaries` and the Index/Mirror refresh boundary. Keep the EPIC030 example in history; current evidence-admissibility semantics remain in 10.6 and PF12-Canon-HDE-Schemas-and-Artifacts. |
| SRC-0363 | PF27-Canon-Plan-Templates \> `Step-log header schema expectations (required; v2)` \> `Exact status predicates`, plus PF19 10.6 evidence sufficiency. A top-level PASS must be derived from all decisive live predicates. |
| SRC-0397 | PF19 10.6 \> `Retrieval-first and negative-proof review`. Preserve the PR-01 source-skew event, but current source truth cannot be replaced by a stale logged failure shape. |
| SRC-0452 | PF19 10.6 \> `Retrieval-first and negative-proof review`. A PF23 observation is classification/context until current owner canon and current proof establish an actionable conflict. |
| SRC-0475 | PF19 10.6 \> `Retrieval-first and negative-proof review`. Preserve the EPIC031 source-use history, while current authority selection follows PF10 only where an applicable live addendum explicitly speaks and permanent owner canon otherwise. |
| SRC-0561 | PF19 10.6 \> `Retrieval-first and negative-proof review`. A prompt label cannot override current authoritative artifact identity or owner canon. |
| SRC-0639 | PF19 10.6 \> `Retrieval-first and negative-proof review`. An already-classified audit observation does not independently mint work, a blocker, a PF delta, or runnable evidence. |
| SRC-0657 | PF19 10.7 \> `Exact PF19 QA vocabulary and semantics`. QA evidence, later-drain posture, PF09 state, PO closeout, board state, merge provenance, and canon drainage remain separate axes. |
| SRC-0668 | PF19 10.7 \> `Exact PF19 QA vocabulary and semantics`. Repo documentation does not perform PF-canon drainage, PF09 movement, QA closeout, PO closeout, board movement, or merge provenance. |
| SRC-0679 | PF19 10.7 for no-overclaim semantics and PF27-Canon-Plan-Templates' exact status predicates for check PASS. H1 13 retains the EPIC036 result only; a QA-ladder PASS does not perform external closeout actions. |
| SRC-0696 | Current closure policy is owned by `PF09.7-Canon-HDE-Build-Checklist-Coagulation` \> `BodyGraph resolver and vendor ingest (bg:resolve)`. PF09.6-Canon-HDE-Build-Checklist-Distillation `HDE-DIST001.11 - v2 mapped-cache persistence hardening` establishes that the first prerequisite is now Done, but it explicitly does not authorize production writes. The remaining current gate is a future Coagulation epic that explicitly authorizes production or production-like upsert with environment, secrets, deployment, rollback, and operational evidence. H1 13 must not continue to describe mapped-cache persistence itself as still wholly future. |
| SRC-0701 | PF19 10.6 \> `Evidence-package caveats and failure history`. Unreadable, empty, malformed, or zero-byte package entries are not proof; alternate governed repo evidence is admissible only under the complete same-event, same-check, coherence, and caveat-recording conditions stated there. |

### **Complete flagged-unit classification ledger**

| Subsection | Source unit | Class | Required H1 13 treatment |
| :---- | :---- | :---- | :---- |
| 13 opening | SRC-0144 | C | Retain as H1 13's current maintenance rule. |
| 13.3 | SRC-0167 | L | Retain the plan-mis-spec versus behavior-failure lesson as guidance. |
| 13.3 | SRC-0170 | L | Retain caveat visibility and portability as guidance, not a new artifact gate. |
| 13.4 | SRC-0181 | L | Retain the fixture-versus-release-identity distinction; owner canon controls current identity proof. |
| 13.5 | SRC-0189 | C | Route current future-artifact semantics to PF27-Canon-Plan-Templates and retain EPIC025 provenance only. |
| 13.5 | SRC-0190 | C | Route current prompt modes and churn escalation to PF27-Canon-Plan-Templates and retain the historical trigger only. |
| 13.5 | SRC-0191 | C | Route current `MODO_*` and header rules to PF27-Canon-Plan-Templates; bind the old export list to EPIC025 history. |
| 13.6 | SRC-0201 | H | Retain the EPIC026 entry declaration as history. |
| 13.6 | SRC-0221 | L | Retain structural-integrity guidance; it does not independently create an acceptance gate. |
| 13.6 | SRC-0222 | L | Retain duplicated-heading and mapping hygiene as should-fix guidance. |
| 13.6 | SRC-0237 | H | Retain the then-unexcerpted docs evidence as an event fact, not a current drain item absent current proof. |
| 13.6 | SRC-0239 | L | Retain reconciliation advice for future reviewers. |
| 13.6 | SRC-0240 | H | Retain the snapshot's non-goals and historical owner routing. |
| 13.7 | SRC-0243 | H | Retain the EPIC027 entry declaration as history. |
| 13.7 | SRC-0251 | C | Point to PF19 10.6 and PF12-Canon-HDE-Schemas-and-Artifacts for current chronology and coherence requirements. |
| 13.7 | SRC-0264 | L | Retain the EPIC027 step-family deliverables pattern as guidance, not a universal roster. |
| 13.7 | SRC-0268 | L | Retain close-pack binding and lookup proof as reusable guidance. |
| 13.8 | SRC-0274 | H | Retain the EPIC028 entry declaration as history. |
| 13.8 | SRC-0287 | H | Retain the six-deliverable D0 PASS set as EPIC028-specific history. |
| 13.8 | SRC-0292 | H | Retain the temporary PF10 clarification as historical; PF10-HDE-Build-Notes has no current addenda. |
| 13.8 | SRC-0296 | L | Retain single-home acceptance-binding guidance; the current plan and owner define the binding home. |
| 13.9 | SRC-0312 | L | Retain the branch-truth and functional-anchor proof pattern as guidance. |
| 13.9 | SRC-0316 | L | Retain the separation of runtime correctness, evidence coherence, and scope cleanliness. |
| 13.9 | SRC-0331 | L | Retain sequencing-only remediation and no-premature-promotion guidance. |
| 13.9 | SRC-0341 | L | Retain PF23-Canon-Reality-Audits's confirmatory-use learning; current PF19/PF23-Canon-Reality-Audits authority remains independent. |
| 13.10 | SRC-0345 | H | Retain the EPIC030 entry declaration as history. |
| 13.10 | SRC-0356 | C | Point to PF19 10.6/PF12-Canon-HDE-Schemas-and-Artifacts for current evidence-churn and coherence treatment. |
| 13.10 | SRC-0359 | L | Retain canonical-byte binding versus regex-shape checking as compat-proof guidance. |
| 13.10 | SRC-0363 | C | Point to PF27-Canon-Plan-Templates's exact PASS predicates and PF19 evidence sufficiency. |
| 13.10 | SRC-0366 | L | Retain defect-exposing regression coverage as remediation guidance. |
| 13.10 | SRC-0370 | L | Retain repo-docs sweep and historical-labeling guidance. |
| 13.10 | SRC-0392 | L | Retain bounded discovery acceptance and `TOOLING_BLOCKED` interpretation as guidance. |
| 13.10 | SRC-0396 | L | Retain proof-class separation for public, compat, and vendor-backed claims. |
| 13.10 | SRC-0397 | C | Point to PF19 retrieval-first current-source rules; retain the PR-01 event context. |
| 13.11 | SRC-0425 | H | Retain the EPIC031 entry declaration as history. |
| 13.11 | SRC-0446 | H | Retain the EPIC031 docs-sweep outcome as a historical event. |
| 13.11 | SRC-0449 | L | Retain PR-specific governed-home and collision-risk guidance. |
| 13.11 | SRC-0450 | L | Retain explicit close-stage-gap and nonclaim guidance. |
| 13.11 | SRC-0452 | C | Point to PF19 retrieval-first/PF23-Canon-Reality-Audits classification posture. |
| 13.11 | SRC-0455 | H | Retain the Step-0A path-mismatch disposition as event-specific history. |
| 13.11 | SRC-0457 | H | Retain the PO-001 scope-boundary proof set as event-specific history. |
| 13.11 | SRC-0462 | H | Retain the PO-006 PASS/remediation facts as event-specific history. |
| 13.11 | SRC-0468 | H | Retain the PO-012 supportability and no-drain facts as event-specific history. |
| 13.11 | SRC-0474 | H | Retain PO-018's proof-only result as event-specific history. |
| 13.11 | SRC-0475 | C | Point to PF19 current source-precedence rules and keep EPIC031 application as history. |
| 13.11 | SRC-0478 | L | Retain proof-boundary and evidence-discipline RCA as reusable prevention guidance. |
| 13.11 | SRC-0481 | H | Retain EPIC031's vendor-conformance and live-call nonclaims as event-bounded history. |
| 13.12 | SRC-0488 | H | Retain the EPIC032 entry declaration as history. |
| 13.12 | SRC-0491 | H | Retain the EPIC032 audit classification outcome as history. |
| 13.12 | SRC-0506 | H | Retain the PR-02 orientation-count freshness requirement as slice-specific history. |
| 13.12 | SRC-0535 | H | Retain PO-001 through PO-003 PASS conditions as event-specific history. |
| 13.12 | SRC-0543 | H | Retain PO-007 through PO-009 PASS conditions as event-specific history. |
| 13.12 | SRC-0550 | H | Retain PO-010 through PO-012 PASS conditions as event-specific history. |
| 13.12 | SRC-0552 | H | Retain PO-011/PO-012 independent-evidence requirement as event-specific history. |
| 13.12 | SRC-0553 | H | Retain PO-013 through PO-015 remediated proof conditions as event-specific history. |
| 13.12 | SRC-0557 | H | Retain PO-016 through PO-018 PASS conditions as event-specific history. |
| 13.12 | SRC-0558 | H | Retain PO-019 through PO-021 PASS and nonclaim facts as event-specific history. |
| 13.12 | SRC-0559 | H | Retain PO-022 through PO-024 PASS and nonclaim facts as event-specific history. |
| 13.12 | SRC-0560 | H | Retain the EPIC032 closeout's source-use posture as historical application. |
| 13.12 | SRC-0561 | C | Point to PF19 current authority-resolution rules; retain the EPIC032 mislabel example. |
| 13.12 | SRC-0567 | H | Retain the EPIC032 documentation-only PR result as history. |
| 13.12 | SRC-0572 | H | Retain the EPIC032 close-stage gaps as event-bounded history. |
| 13.12 | SRC-0573 | L | Retain reusable-shape routing as guidance; PF19 does not own the schema. |
| 13.13 | SRC-0576 | H | Retain the EPIC033 entry declaration as history. |
| 13.13 | SRC-0578 | H | Retain the snapshot's source-use posture as historical application. |
| 13.13 | SRC-0615 | H | Retain `Ready with caveats` and its caveats as event-bounded history. |
| 13.13 | SRC-0617 | H | Retain the closure-trace meaning of `SATISFIED` as event-bounded history. |
| 13.13 | SRC-0620 | L | Retain the product-boundary retrospective as guidance; owner docs govern future work. |
| 13.13 | SRC-0622 | L | Retain PF23-Canon-Reality-Audits context-only use as a learning; current precedence is owned elsewhere. |
| 13.13 | SRC-0628 | H | Retain HDE-FERM007's then-future posture as history, not current state. |
| 13.13 | SRC-0629 | H | Retain HDE-FERM008's then-future posture as history, not current state. |
| 13.13 | SRC-0630 | H | Retain the EPIC033 docs-sweep outcome as history. |
| 13.13 | SRC-0634 | H | Retain the EPIC033 close-stage gaps as event-bounded history. |
| 13.13 | SRC-0635 | H | Retain the former future-work statement as history; later epics and current PF09.5 supersede its state. |
| 13.13 | SRC-0637 | H | Retain the EPIC033 audit classification outcome as history. |
| 13.13 | SRC-0639 | C | Point to PF19 current classification/non-work-minting rule. |
| 13.14 | SRC-0655 | H | Retain EPIC034 supportability and remaining-scope posture as historical state. |
| 13.14 | SRC-0657 | C | Point to PF19 10.7 for current closure-axis separation. |
| 13.15 | SRC-0660 | L | Retain provider, normalization, OPS, drainage, and closure proof-class separation as guidance. |
| 13.15 | SRC-0667 | L | Retain PF29 follow-up guidance; current PF29 controls actual user-guide requirements. |
| 13.15 | SRC-0668 | C | Point to PF19 10.7 for current repo-docs versus canon/closeout separation. |
| 13.15 | SRC-0670 | H | Retain HDE-EPIC035 final closeout supportability as event-bounded history. |
| 13.16 | SRC-0679 | C | Point to PF19 10.7/PF27-Canon-Plan-Templates for current check-PASS and no-external-action semantics. |
| 13.17 | SRC-0687 | L | Retain the EPIC037 proof-class separation as reusable guidance. |
| 13.17 | SRC-0696 | C | Point to the current PF09.7 production-upsert gate and reflect PF09.6 completion of its first prerequisite. |
| 13.17 | SRC-0699 | L | Retain the accepted evidence-assembly remediation pattern as guidance. |
| 13.17 | SRC-0701 | C | Point to PF19 10.6 evidence-package caveat and alternate-proof rules. |

## **13.1 HDE-EPIC011 — Vendor Ingest and Data Durability**

Status posture: failed epic; not shippable under the original acceptance map.

Preservation surfaces (no public contract changes under this epic):

* CLI transport and compat contracts defined in the HDE PF docs.  
    
* Vendor ingest and retry/backoff contracts as defined in HDE Epics Map and HDE-CLI-API-Vendor-Ref.  
    
* Compat math and Aux narrative surfaces as defined in HDE-Math-Spec and HDE Narratives Guide.  
    
* BodyGraph observability and evidence discipline as defined in HDE-Schemas and Artifacts and HDE-Mechanics Guide.

QA learnings:

* Treat EPIC011 artifacts and notes as historical record only. Do not treat remaining work as open EPIC011 acceptance.  
    
* Any revisit of EPIC011 topics must be re-scoped into a new epic with a fresh acceptance roster and tokens. PF19 references EPIC011 only to describe historical QA posture and preservation constraints.

## **13.2 HDE-EPIC017 — Live QA pattern from Codespaces to Railway**

Status posture: established a Live QA pass pattern demonstrating selected prod behaviors from a QA console. Live QA is not a replacement for CI.

Key QA learnings:

* Use Live QA to demonstrate prod-facing behavior for selected surfaces, while keeping evidence mechanical (logs, JSON outputs, exit codes, tree and env snapshots) under the epic QA root.  
    
* Live QA should validate a small set of integration facts that unblock confidence, such as reachability and basic transport posture for key endpoints, without attempting to re-prove every contract already covered by CI.  
    
* Treat CLI availability as a QA surface: verify the CLI exists in the QA console environment and can execute the expected commands under the intended rails.  
    
* When exercising vendor ingest from a QA console into prod, prefer a dry-run path that proves reachability and parity metadata without mutating DB state.  
    
* Where an invariant is primarily enforced by harnesses and tests, Live QA should confirm the harness can run and that evidence is captured correctly, rather than duplicating full proof logic manually.

## **13.3 HDE-EPIC020 — Separation Pass 1 for error and identity surfaces**

Status posture: ready with caveats.

Key QA learnings:

* Establish and evidence a rails baseline before making determinism or reproducibility claims (env pins and rails posture must be explicit and recorded).  
    
* Treat plan mis-spec as a planning defect, not a behavior failure. QA should preserve the learning and correct the pattern for future plans rather than weakening expectations.  
    
* Epic acceptance scaffolding plus a single epic QA tree is a repeatable pattern: acceptance map, manifest, and a consistent evidence root improve traceability and reduce drift.  
    
* When a planned harness artifact is missing, record it explicitly as debt and adjust the plan steps. Do not silently weaken parity expectations to accommodate missing assets.  
    
* Keep caveats visible and portable: gaps should be explicitly recorded as future work, not hidden by omission.

## **13.4 HDE-EPIC022 — Separation Pass 2 for evidence discipline, parity hardening, and identity bundles**

Status posture: Separation-phase hardening focused on evidence integrity and parity, under explicit rails posture.

Key QA learnings:

* Placeholder acceptance scaffolding is allowed only as scaffolding. Placeholders are non-claimable: no token is treated as satisfied until bindings are concrete.  
    
* Evidence systems are coupled: when governed evidence changes, keep the evidence index, mirror, and any required orientation or topology proofs coherent in the same PR, or QA should expect deterministic drift failures.  
    
* Acceptance bindings must point to primary artifacts and enforcing validator tests. Proof transcripts are required for auditability, but they must not replace primary evidence in token bindings.  
    
* Rails-proof claims must be backed by behavioral evidence when used as behavioral claims. Env pins existing is not equivalent to refusal or gating behavior being proven.  
    
* Canonical filenames matter for verification. If legacy alias copies are required for compatibility, keep canonical filenames as the verification targets and record the alias as an explicit caveat.  
    
* Evidence integrity repairs should be treated as governed-evidence-only work and verified under the intended rails in both write and check modes.  
    
* Dependency posture is QA posture: avoid situations where optional dependencies break test collection. Either require the dependency for the relevant job or guard it so collection succeeds with explicit skips and install guidance.  
    
* Identity vs fixtures: deterministic stdout capture artifacts are fixtures for canonical-bytes proofs, not release identity proofs. Release identity remains governed by the identity surface and its acceptance and evidence rules.

## **13.5 HDE-EPIC025 — QA learnings snapshot for compat contract hardening, deterministic stdout, and Reader A7 proofs**

Status posture: historical QA record derived from the PR review trail. This entry is learnings-only and does not define new acceptance criteria.

Key QA learnings:

* Step-review posture (addenda 2.30 to 2.48): `d0_discovery`, `po-001`, and `po-002`were reviewed PASS from step logs plus deliverables reports; `po-003`to `po-013`were reviewed PASS when plan-defined deliverables were present and audit-usable, with PF-Canon transcript trust gates satisfied in `primary.log`under `audit/qa/hde-epic025/checks/<step-id>/`. Notable PASS proofs in this addendum range include A7 /reader proof capture ( `po-008`), canonical JSON gate capture ( `po-009`), env pins plus sanity pipeline captures ( `po-010`), closure record plus sha verification ( `po-011`), final LF check plus endpoint catalog and index sha snapshots ( `po-012`), and deferred scope posture recording ( `po-013`). Where a plan's PASS predicate is keyed to exit code and sha presence for captured transcripts, an empty transcript snapshot is an observation only unless the plan defines non-empty as required.  
    
* Evidence-capture deviations (addenda 2.34 to 2.38): header-only `primary.log`rebuilds via Moon Loop are acceptable when the body is preserved and the deviation is recorded. Downstream consumers should tolerate a `primary.log`that begins with two JSON header lines when a header rebuild was applied and recorded. Treat the Approved Plan deliverables list versus header `artifacts`list mismatch as non-blocking when the close pack contains `primary.log`and required deliverables are present, but record the deviation and drain template clarity.  
    
* Live QA Plan posture changed to objective-first directives (addenda 2.37): plans define objectives, proof obligations, required evidence outputs, and explicit PASS or FAIL predicates. Steps use directives rather than syntax-frozen commands, and the step log is the authoritative record of the exact command(s) executed.  
    
* Reduce plan brittleness (addenda 2.37): minimize locus strings unless canon-defined or fixed-path obligations. If a plan must name a repo locus, the loci proof gate still applies. Syntax and quoting defects are non-blocking at plan review and are remediated in flight via Moon Loop while preserving objectives and proof obligations.  
    
* Template semantics and deferred steps (addenda 2.40.1, 2.46, 2.48): if a plan or closure template enumerates future-step artifacts, it MUST label them NOT RUN or DEFERRED until the producing step has executed. NOT RUN or DEFERRED is not missing evidence; missing evidence is reserved for executed steps whose required artifacts are absent or unproven. Closure and rollup outputs MUST separate PRESENT, MISSING, and NOT RUN or DEFERRED states, and MUST avoid introducing dangling references to evidence for deferred steps (for example by recording deferral posture explicitly under `00_meta/`rather than implying missing artifacts).  
    
* Prompt-family separation and QoS escalation (addenda 2.45, 2.40.2, 2.40.3): QA prompts must declare AUTHORING (runbook instructions) versus REVIEW (evidence evaluation and verdict) mode, and the agent must output only the mode's required structure. In REVIEW mode, new commands must not be invented; remediation commands may be used only when copied verbatim from the plan or its caveats and applied to achieve the plan's stated objective. Repeated structural remediation churn for the same failure mode MUST escalate to a systems RCA and a canonical drain targeting the failure class (template semantics, artifact-map source-of-truth, prompt-family separation), not the one-off incident.  
    
* Environment-variable governance and header discipline (addenda 2.33, 2.35, 2.42): `MODO_*`variables are non-canonical and MUST NOT be introduced or required by QA plans, QA runbooks, or QA evidence schemas. The approved EPIC025 plan contains legacy `MODO_*`references due to churn; treat them as inert placeholders only and do not replicate them. When a check uses the header writer, export required per-check env vars immediately before header generation (names-only: `CHECK_ID`, `CHECK_NAME`, `PASS_FAIL`, `COMMANDS_JSON`, `ARTIFACTS_JSON`, `PF_REFS_JSON`) and do not rely on prior step state.  
    
* Showcompat Live QA posture (addenda 2.39): until local BodyGraph storage or replay exists, functional `showcompat`steps require vendor rails open and explicit arguments (no zero-arg invocation). If attempted under closed rails or without arguments, classify the outcome as a rails or usage defect for that step, not a product behavior failure, and record rails posture and failure signature.  
    
* Proof pairing pattern: compat probe validation paired Endpoint Catalog discipline with a concrete proof artifact under `artifacts/proofs/`and step-local evidence under `audit/qa/hde-epic025/checks/`.  
    
* Internal contract changes must be aligned across implementation behavior, contract tests, and cataloged endpoint descriptions. Robust request validation belongs in the QA posture: prevent user-input errors from surfacing as 500s by enforcing early validation and typed error returns.  
    
* Governed evidence coherence and CI hygiene: when governed artifacts change, refresh governed artifacts and their checkers in the same PR. Evidence tooling changes that alter normalization or path handling have cross-epic blast radius and require explicit invariants proofs. CI hygiene (markers, warning posture) must be accounted for to avoid avoidable pipeline failures.  
    
* Close-pack and close-out artifacts should be mechanically generated from repo state (titles-only), not hand-authored. Prefer a repo generator that binds `key_outputs`to the exact reviewed bytes.  
    
* Deterministic stdout and proofs are QA surfaces: enforce canonical emission and newline posture, keep proof generation env-gated, and ensure conformance is proven by tests plus captured evidence. For A7 transport steps that rely on proof snapshots, copy the proof artifacts into the step check directory and sha them as step evidence rather than relying on the out-of-band proof tree.  
    
* Drain targets recorded (titles-only) in addenda 2.33, 2.37, 2.39, and 2.40.3: Glow QA Guide, HDE-Build Notes, Canon Plan Templates, Epic Process Guide, Glow Infrastructure, and HDE-CLI-API-Vendor-Ref.  
    
* When a behavior change implies documentation drift elsewhere, record it explicitly as a doc-delta for the owning document rather than letting the mismatch persist silently.

## **13.6 HDE-EPIC026 — QA learnings snapshot (addenda 2.5 to 2.33)**

PF19 records the EPIC026 learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

Vendor ingest and staging surfaces are explicitly out of scope for this epic.

These addenda focus on contract and evidence posture for conjunction-mode computation, the endpoint catalog suite, the evidence index and machine mirror, later step-review posture for `po-005` through `po-012`, and the final closeout and closure-review posture for the epic.

Key QA learnings:

* Close the contract first: PR01 and PR02 locked the conjunction surface behind a stable vendor-facing contract. This prevented later QA from debating what correct behavior means.  
    
* Prefer resolver-backed computation over patched stubs. QA should insist on the real resolver path as soon as it is viable.  
    
* Endpoint governance and catalog discipline remain the audit anchor for API behavior: keep route ids, request and response schemas, and transport bytes governed and versioned.  
    
* CLI surface is a distinct contract. Conjunction-mode behavior and flags must be validated explicitly; CLI evidence must include rails posture and deterministic output expectations.  
    
* Checks-only evidence layout is the trust baseline for later step reviews and final closure. For `po-005` through `po-012`, PASS depended on stable `audit/qa/<epic-id>/checks/<check_id>/` evidence, including step-local auxiliary directories such as `close_pack_copy/`, not on per-run roots or ad hoc evidence trees.  
    
* Plan-defined PASS criteria and plan-defined deliverables are authoritative. Supporting observations such as repo-locus proofs, rails snapshots, or appendix artifacts may strengthen provenance, but they do not replace the plan’s stated PASS test.  
    
* `po-005` and `po-006` reinforce route-proof posture: a dev-only conjunction route check is acceptable when the route proof and pytest results satisfy the plan predicate under canon-trustworthy evidence. A minor wording mismatch in the plan PASS bullet is non-blocking when the step title, intent, inputs, and captured evidence clearly identify the intended routes.  
    
* `po-007` reinforces endpoint-catalog review posture: baseline sha256 match plus exact extracted dev conjunction routes (`/dev/reader/conjunction`, `/dev/sampler/conjunction`, `/dev/writer/conjunction`) under closed rails is sufficient for PASS when the plan requires that comparison.  
    
* `po-008` establishes that CLI help surfaces and non-JSON modifier rejection are valid QA surfaces. `hdctl --help` and `hdctl showcompat --help` should be treated as audit-usable deliverables when the plan requires them, and non-JSON conjunction modifier rejection should be proven by non-zero exit plus captured stderr.  
    
* Optional or conditional lanes are non-blocking when the plan explicitly marks them conditional and the report records why they did not run. For `po-008`, conjunction output artifacts were correctly skipped when `USER_A_ID` and `USER_B_ID` were intentionally absent.  
    
* `captured_env` in the step header is part of evidence trust, not decoration. For closed-rails steps, reviewers should confirm the expected rails and environment keys are present in `primary.log`.  
    
* A documented deviation can still be acceptable when the exact plan command block cannot run as written, provided the executed command is semantically correct, the required deliverables exist, the plan’s PASS predicate is proven, and the report records what changed and why.  
    
* Early `po-009` review documented blocked input posture: when a step depends on product inputs that are not valid or not available, the correct interpretation is an input-availability gate and planning defect, not a demonstrated behavior defect. Re-run only when valid product inputs exist.  
    
* Final closure posture for `po-009`: closure became defensible only after `po-009` reached a plan-predicate-aligned PASS backed by governed check-scoped evidence under the canonical epic QA root and check directory. Do not convert a blocked lane to PASS by narrative reinterpretation alone.  
    
* Closeout defensibility depends on explicit Coverage vs QA Plan accounting, step-scoped evidence pointers under the governed QA root, and stable step identifiers. A PASS label or section heading alone is not sufficient proof.  
    
* Step-scoped deliverables reports are admissible closure proof only when they land under the canonical epic QA root and check directory and do not rely on per-run nesting as a correctness key.  
    
* Structural integrity of headings, check IDs, and mapping is closure-critical documentation, not cosmetic. It may be treated as non-blocking only when the underlying proof remains check-scoped, path-grounded, and unambiguous.  
    
* PF10 or other SoT structural drift increases review cost even when closure remains defensible. Duplicated or mislabeled check sections should be treated as should-fix documentation hygiene, not ignored as harmless formatting noise.  
    
* Closeout and manifest tooling must make executed checks auditable. Empty or ambiguous manifest enumeration increases manual reconstruction risk and should be treated as a should-fix even when closure can still be defended by other path-grounded proof.  
    
* A token or review-rail claim is not auditable without a concrete evidence pointer. Reviewers should anchor on content-level decision lines and governed evidence paths, not on headings or summary prose alone.  
    
* PR-06 docs-only alignment pass is still a QA surface: docs correctness must be backed by audit-usable evidence, not reviewer recollection.  
    
* Governed evidence updates must stay coherent: if you update evidence index, machine mirror, or path proofs, keep them in lockstep and ensure reviewers can follow pointers from plan to `primary.log` to deliverables to stored artifacts without guesswork.  
    
* ORIENTATION\_DRIFT is a first-class failure mode: any integration gate must treat mismatch between plan and execution as a blocker even if tests pass.  
    
* Prefer primary gate outputs over re-summarization: reviewers should anchor on `primary.log` transcript evidence and generated deliverables reports rather than ad hoc summaries.  
    
* Path-proof and proof\_anchor hygiene remain mandatory: path proofs must be adjacent to the referenced artifact, and machine mirror proof anchors must point to stored path proofs.  
    
* Doc delta handling: dual-home canonical JSON gate artifacts are allowed only when the canonical copy is protected from incidental edits and the legacy home is preserved for history.  
    
* Close-pack automation is useful but raises integrity sensitivity. Reviewers must treat diff bundle integrity as gating and must reject a corrupted re-export.  
    
* Close artifacts must include explicit closure mapping when required so closure can be audited without inference.  
    
* Verified-but-not-excerpted claims are not audit-usable. If a reviewer checks `--help` or similar CLI output, store the output excerpt as a governed evidence artifact.  
    
* Earlier closeout review proposed tighter PF19 deltas around step-scoped evidence and blocked-status handling. Later closure review found no new PF-canon deltas were required once `po-009` PASS was path-grounded and closure trust constraints were explicit. The durable lesson is to keep evidence-trust rules explicit in practice, not to rely on narrative reconstruction.  
    
* Recorded drain items (titles-only): dual-home policy tension for governed artifacts versus docs anchors; conjunction CLI mode and exit-code semantics canonicalization; epic closure pack content and TI-002 mapping expectations; later step-review posture for blocked input-dependent checks; and later closure-review posture for structural SoT drift and manifest auditability.

Known gaps (as recorded in addenda 2.14 to 2.33):

* Docs PR validation evidence was not excerpted for the reviewed help output; this remains a drain item for future review posture.  
    
* A doc-lint or markdown-lint transcript was not captured as a primary evidence artifact during the docs-only pass.  
    
* PF10 structural drift around duplicated or mislabeled check headings should be reconciled to reduce reviewer ambiguity in future closures.

Known non-goals: these addenda do not define token schemas or CI jobs; those remain governed by their single homes (PF09, PF12, PF04, PF05). They also do not define vendor ingestions; that remains a future epic.

* Normative homes: endpoint catalog schemas, route ids, and transport bytes remain governed by their single-home PF docs (titles-only). PF19 records the QA posture and the review learnings only.

## **13.7 HDE-EPIC027 — QA learnings snapshot for CLI installability and writer proof coherence**

PF19 records the EPIC027 learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on the close-slice proof families that drove the late EPIC027 QA passes: CLI installability/conformance, Catalog/A7 route proof, and internal/dev writer readback evidence.

Key QA learnings:

* CLI installability is a real QA surface. When an epic claims installability or command-catalog conformance, reviewers need positive module-runner and console-entrypoint proof; skipped or negative console proof is not enough.  
    
* Installability artifacts must be deterministic and single-sourced. Help, version, entrypoint, and installability summaries should agree with each other and must not depend on ambient PATH.  
    
* Preserve valid proof families while repairing a narrower defect. The durable PR02 pattern was to fix installability without discarding deterministic sampler semantics, parity artifacts, or governed indexing.  
    
* Internal/dev writer proof is a distinct non-A7 surface. It can prove two-run writer bytes and reader readback parity without widening Catalog A7 scope.  
    
* Open rails must be explicit for writer proof. A helper that silently flips SAFE\_MODE or ALLOW\_NETWORK is not acceptance-safe; the operator must provide the required rails and the proof must record them.  
    
* Evidence chronology is part of acceptance truth. Newly generated artifacts, human-index rows, mirror rows, and path-proofs must all reflect the current run context; stale or contradictory chronology is blocking.  
    
* Durable remediation proof should include both surface tests and evidence-tooling checks. For these slices, the stable pattern was route tests plus evidence update/check, path validation, LF validation, and mirror-schema validation.  
    
* Packaging/entrypoint drift and silent open-rails regressions are repeatable QA failure classes. Future reviewers should keep both as explicit regression checks rather than treat them as one-off incidents.

Additional step-review learnings from `po-001` to `po-003` are as follows.

* For dev-harness coherence checks, the durable PASS pattern was a governed `primary.log` that preserved the actual ordered multi-command sequence, used an allowed command provenance value when that field was present, and recorded closed-rails determinism pins, paired with route-inventory proof of the dev conjunction trio and related blueprint wiring plus named pytest results under the canonical check-scoped QA root. An earlier failed attempt was non-blocking when the final governed rerun was clearly distinguished and carried the PASS-grade evidence.  
    
* For compat discoverability checks, the durable PASS pattern was to prove the compat surface mount at `/api/compat/v1` and to show explicit updater or machine-mirror discoverability of the governed compat identity-hash family. When that discoverability proof was present, absence of a dedicated per-check manifest helper was treated as a planning or Moon Loop defect, not a QA blocker, so long as the report clearly documented reuse of the governed manifest-pair workflow and the required deliverables landed at the canonical paths.  
    
* For shared-emitter CLI checks, reviewers should expect a multi-part proof set under the check-scoped QA root: emitter-path proof showing shared `emit_public`, LF or CRLF guard proof, parity-test output, and `showcompat --help` output. These deliverables together were sufficient for PASS when the plan predicate was shared-emitter posture rather than installability or live-vendor behavior.

Additional step-review learnings from `po-004` to `po-006` are as follows.

* For CLI installability and conformance checks, the durable PASS pattern was a governed check-scoped evidence set under the canonical epic QA root: explicit console-entrypoint binding proof, passing install-help and `bg:resolve` test outputs, successful `bg:resolve --help` output, and a governed `primary.log` that preserved the ordered command sequence and closed-rails determinism pins. These deliverables were sufficient for PASS when the plan predicate was CLI installability and conformance rather than live-vendor behavior.  
    
* For Catalog/A7 proof steps, the durable PASS pattern was a passing A7 transport test plus catalog-route inventory showing the in-scope Reader success route and explicitly excluding non-A7 surfaces such as `/internal/version` from PASS treatment. Reviewers should reject any step that counts a non-cataloged or non-A7 route as satisfying A7 proof.  
    
* For internal/dev writer proof steps, the durable PASS pattern was a passing dev conjunction HTTP test plus explicit mirror discoverability of the governed writer artifact family, alongside catalog context showing the writer endpoint remained outside the A7 proof family. This preserved writer readback proof as a non-A7 surface while still requiring governed ledger visibility.

Additional step-review learnings from `po-007` are as follows.

* For evidence-ledger coherence checks, the durable PASS pattern was a governed `primary.log` under the canonical epic QA root that preserved an explicit ordered multi-command sequence, used the allowed `command_provenance` value `Explicitly created`, and recorded closed-rails determinism pins for the full evidence-discipline run.  
    
* The required deliverables pattern for this step family includes the governed `primary.log`, the current `qa_step_logs_manifest.json` pair, and the concrete helper outputs for `update_evidence_index`, `orientation_demo`, path validation, LF, mirror schema, and manifest lookup. Missing any required helper output is a tooling or prerequisite failure, not a behavior failure.  
    
* PASS for this step family requires both conditions together: the evidence-discipline jobs succeed, and the manifest-lookup proof shows that `epic027.qa_step_logs_manifest` is discoverable in the canonical evidence updater/source, the Human Evidence Index, and the Machine Mirror. Presence on disk or a refreshed path-proof alone is not sufficient.  
    
* When a passing governed `primary.log` records matching names-only `intended_tokens` and `claimed_tokens` for the evidence-discipline roster, reviewers may treat that as trustworthy step-level token-surface confirmation. If token fields are absent, incomplete, or non-canonical, reviewers must fall back to the step’s explicit deliverable-based PASS criteria and the general token-field rules in this guide.

Additional step-review learnings from `po-008` to `po-010` are as follows.

* For close-pack truthfulness checks, the durable PASS pattern was a governed close-pack generator run plus binding proof that the close-pack points to the canonical epic QA root and current ledger files, paired with explicit lookup proof that `qa_step_logs_manifest.json` is ledger-bound rather than merely present on disk.  
    
* For no-new-public-surface and no-new-acceptance-vocabulary checks, the durable PASS pattern was a passing catalog-surface inventory with no unexpected public success surface and a passing token inventory with no non-canonical token names, both captured under the canonical check-scoped QA root. When the step also refreshed the manifest pair, the refresh had to be header-driven from the step’s governed `primary.log`.  
    
* For runtime functional proof posture, the durable PASS pattern was a governed check-scoped evidence package that showed no missing prerequisite runtime logs and a runtime-surface inventory proving the required proof families were actually exercised in the same run.  
    
* For provenance-sensitive runtime closeout steps, `primary.log` had to preserve the exact ordered command string actually executed, and any byte-changing refresh to the manifest pair or related governed evidence had to be followed by refreshed path-proof and Index/Mirror records with internally consistent freshness values.

Known non-goals: these addenda do not redefine token semantics, A7 byte rules, or PF09 status rows. PF19 records the QA posture and review learnings only.

## **13.8 HDE-EPIC028 — QA learnings snapshot for compat proof-surface discipline and Reader evidence-family closeout**

PF19 records the EPIC028 learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on two late Conjunction proof clusters: PR01 compat or shared-emitter or showcompat closure and PR02 Reader evidence-family closeout.

Key QA learnings:

* Internal compat proof-surface discipline matters. When the claim is canonical compat JSON and AB↔BA parity for the internal or admin compat surface, the durable PASS pattern is a closed-rails app-client proof against `/api/compat/v1`. A vendor-backed `showcompat` path under open rails is the wrong proof surface for that claim.  
* Shared-emitter and showcompat closure is not satisfied by a generic parity claim alone. The durable PASS pattern required explicit handler-level allow-list enforcement, a governed allow-list proof artifact, direct serializer-guard regression coverage, and explicit evidence-index coverage for the serializer-grep and Reader↔CLI parity artifacts.  
* For this PR01 pattern, the stable validation bundle was a closed-rails set that paired targeted pytest with evidence update/check, orientation check, and mirror-schema validation, while preserving showcompat presence and canonical JSON or LF conformance. The proof posture stayed within compat and CLI scope and did not widen into Reader or writer implementation.  
* The direct PR02 blocker was evidence-family integrity, not Reader runtime behavior. The durable remediation pattern preserved the existing Reader success-body, catalog, and A7 runtime or test slice and repaired the evidence family without reopening Reader behavior or widening into writer work.  
* For this PR02 pattern, a supportable closeout required passing canonical generation, evidence update/check, orientation check, mirror-schema validation, and the targeted Reader or evidence pytest subset under the declared rails.

Additional retrospective learnings for this PR02 pattern are as follows.

* A rerun-only remediation is not enough when the defect sits inside writer or generator logic. Reviewers should look for the code-level writer fix, not repeated refresh-only attempts.  
* Plan-first remediation is useful when the changed evidence family is broader than the initially failing proof surface. Reviewers should separate the broader participating family before certifying closeout.  
* Canonical JSON gate timestamp behavior can be a single-point failure for chronology. A superficially refreshed proof set is not trustworthy if the writer still reuses stale gate timestamps.

Additional step-review learnings from `d0` to `po-005` are as follows.

* For D0 bootstrap checks, the durable PASS pattern was a current-state, check-scoped evidence set under the canonical epic QA root, with a governed `primary.log` that records the exact executed command sequence, uses `Explicitly created` command provenance when applicable, includes the step’s own primary log in `evidence_artifacts`, and captures the actual closed-rails environment. PASS also depended on the full six-deliverable bootstrap set at the plan-defined paths: runtime context, CLI help baseline, services or surfaces baseline, the current manifest pair, and confirmation that no per-run nested root was created.  
* For internal compatibility proof checks, the durable PASS pattern was a governed snapshot set that proves the order-neutral internal compat path end to end: `normalize_pair`, `pair_key`, `compat_public`, and `emit_public`, with the governed emitter snapshot delegating to the canonical serializer rather than an alternate serializer path.  
* For one-governed-emission-path checks, reviewers should require both halves of the proof together: Reader or public snapshots showing `emit_public` and `emit_reader_v1` routing, and CLI-side guard artifacts showing the governed emitter allow-list plus serializer-grep PASS posture. One side alone is not sufficient to prove one governed emission path across CLI, Reader, and internal compatibility.  
* For CLI compatibility-surface checks, the durable PASS pattern was `hdctl --help` evidence that exits 0 and exposes `showcompat`, paired with passing governed CLI guard artifacts and a non-zero Reader↔CLI parity probe. These steps remain valid only when they stay on existing CLI loci and do not invent new flags or new routes to satisfy the proof obligation.  
* For public Reader envelope checks, the durable PASS pattern was a passing Reader transport test plus an encoding-invariance snapshot, captured under the canonical check directory, with explicit confirmation that the step preserved the existing public success surface and six-part numeric-free payload rather than introducing a new route or payload contract.  
* For governed Reader proof-surface designation checks, the durable PASS pattern for this epic was to treat the open issue as a documentation or classification gap, not a new runtime defect. While the temporary PF10 clarification remained live, reviewers could treat `/reader` as the governed Reader success-proof surface for current EPIC028 scope when the approved lookup artifact proved route existence, `APP_ENV=dev` gating, and `a7_eligible:true`, without inventing a second designation mechanism, a new route, a new flag, or a new evidence family.  
* The `po-005` clarification did not change PASS criteria or evidence shape. The durable posture was PF10-first temporary canon plus downstream canon alignment: use the already-approved `po-005` evidence family to unblock the step now, then drain the explicit designation into canon later. A stale blocked-branch plan note was non-blocking once the rerun made the PASS basis explicit.

Additional step-review learnings from `po-006` to `po-008` are as follows.

* For governed public success-surface transport checks, the durable PASS pattern was to run the Reader transport proof only after `po-005` had already established the governed Reader success-proof surface. Reviewers should expect a passing transport test exit code together with an explicit statement that the blocked branch did not trigger. A stale blocked-lane command block was non-blocking once the rerun made the resolved branch explicit and introduced no new route, flag, or proof-surface carrier.  
* For current-epic acceptance-binding checks, the durable PASS pattern was single-home binding across the current epic acceptance trio: acceptance map, token/evidence matrix, and acceptance-map viability log, plus matching Machine Mirror rows for all three. Reviewers should treat alternate acceptance-map homes as a QA failure when the step’s PASS predicate is single-home acceptance binding.  
* For same-change coherence checks across changed governed evidence families, the durable PASS pattern was to validate the full participating family, not only the primary family: both the authoritative `audit/gates/json_gate/canonical` family and the legacy-but-still-governed `audit/gates/canonical_json` family had to remain present before and after the gate-writer run, with the writer exiting 0\.

Additional closeout and closure-support learnings from `po-009` to epic close are as follows.

* For repo-supported completion summary checks, the durable PASS pattern was an explicit, reproducible summary under the governed check directory that distinguished recorded, blocked, and no-claim outcomes and carried no-claim posture for canon drain and formal close-pack completion. Reviewers should not let later packaging or drainage work be implied as complete by a PASS label alone.  
* When a bounded Moon Loop remediation corrected a false blocked state caused by contextual `blocked_note.txt` files, the durable pattern was to preserve the contextual note content as separate context artifacts, remove only the trigger filenames, capture the governed Step-0B delta pair, and rerun the already-approved summary step under the same rails. Silent deletion or narrative-only reclassification is non-conforming.  
* A packaging-only OPS closeout lane was valid when it surfaced the formal close-pack baseline artifacts, kept reopened implementation, QA verdict changes, canon drain, and merge provenance as explicit no-claim boundaries, and bound the manifest to the already-proven epic evidence family rather than inventing a new proof surface.  
* A provenance-only OPS closeout lane was valid when it used a narrow rerun-based binding against one governed QA artifact family instead of a full QA rerun, and when the resulting provenance artifact carried the governed artifact path, in-session command family, Codespaces venue context, repo root and commit linkage, non-claim boundaries, and a sibling path-proof.  
* Codespaces venue provenance mattered only when the closeout claim depended on it. When an epic needed to prove a Codespaces-run closure step, at least one governed artifact had to bind the relied-on QA artifact to the Codespaces session context and the command family that produced it.  
* PF09 status lag after repo-proven completion was a closeout clarity issue, not a proof failure. Reviewers should distinguish supportable-as-Done posture from drained PF09 state and should not let that distinction collapse into an over-claim of canon completion.  
* Closeout defensibility depended on explicit Coverage vs QA Plan accounting, step-scoped evidence pointers under the governed QA root, and surfaced close-pack or provenance artifacts where required. A PASS heading, retrospective summary, or OPS verdict line alone was not sufficient proof.

Known non-goals: these addenda do not redefine token semantics, A7 byte rules, or PF09 status rows. PF19 records the QA posture and review learnings only.

## **13.9 HDE-EPIC029 — QA learnings snapshot for bounded conjunction closure and writer-evidence review cleanliness**

These addenda focus on the bounded EPIC029 closure slices that drove review and closeout: PR-01 conjunction JSON surface inventory and canonical JSON discipline, PR-02 conjunction writer-envelope posture, PR-03 repo-side dev harness binding and healthcheck closure, OPS-01 environment-validation truthfulness, and PR-04 final close-pack binding.

Key QA learnings:

* For bounded conjunction closure, reviewers should treat the approved surface family as explicit and minimal: the conjunction inventory artifact, the canonical JSON gate family, the shared Human Index and Machine Mirror refresh, topology orientation support, and only directly required companion path-proofs. Unrelated governed artifact churn outside that family is blocking even when the core slice is otherwise correct.  
* For canonical JSON gate route probes, byte equality alone is not sufficient. The durable PASS pattern required route-specific expected-status checks and failure when actual and expected HTTP status diverged, even when the returned bytes were otherwise canonical.  
* Green validation alone did not settle PR-01 acceptance when attempt-local remediation bundles still left current-diff provenance ambiguous. The durable closure pattern was a read-only branch-truth proof against `main`, an empty `main..HEAD` diff, and re-confirmation of the required functional anchors in repo state.  
* For PR-01, the required bounded minimum loci remained `/reader`, `/dev/writer/conjunction`, and `/internal/dev/sampler`. Additional same-family loci could be documented, but they did not replace the obligation to prove the approved minimum bounded set and single-emitter posture.  
* Canonical-gate and evidence-index refreshes can fail review through evidence integrity even when the intended runtime slice is right. Stale mirror hashes, stale writer-family or gate-family chronology, or mismatched freshness across governed companions are blocking defects until canonical tooling refreshes them coherently.  
* For writer-envelope closure, the durable PASS pattern was to preserve the already-correct runtime slice on `/dev/writer/conjunction`: typed numeric-free success and error envelopes, `no-store`, non-conditional posture, and explicit non-A7 scope. Corrective work belonged in the governed writer evidence family, not in reopening the runtime surface without cause.  
* Full named validation sets can be green while a slice is still non-passing if the current diff carries out-of-scope governed artifacts or stale chronology inside the approved evidence family. Reviewers should separate runtime correctness, evidence-family coherence, and scope cleanliness rather than treating any one of them as sufficient by itself.  
* When an approved slice is explicitly contributory or evidence-only, repo-supported merge readiness does not by itself justify a PF09 status drain. Reviewers SHOULD keep merge readiness separate from later checklist status updates.  
* Additional step-review learnings from `po-001` to `po-005` are as follows.  
  * For `po-001`, the durable PASS pattern was governed step evidence that paired a non-empty deliverables set with bounded-scope proof across the conjunction inventory snapshot, the Endpoint Catalog snapshot, and the recorded route slice. The receipt alone was not sufficient without those bounded-scope artifacts.  
  * For `po-002`, the durable PASS pattern was a gate return code of `0` plus both governed canonical JSON family snapshots present and non-empty. A zero-byte `run_canonical_json_gate.output.log` was non-blocking when the rc capture, the structured canonical record, and the legacy canonical check log all recorded pass posture.  
  * For `po-003`, a PO-approved Moon Loop rerun could still be accepted when the rails deviation was explicit, the governed evidence root remained intact, and the formerly empty generator output log was replaced by a non-empty governed artifact. A bounded rerun under this posture remained step-acceptable, but the deviation had to be surfaced rather than normalized away.  
  * For `po-004`, the durable PASS pattern was a passing sampler HTTP test plus non-empty start-helper and healthcheck snapshots under the governed step root. The `/internal/dev/sampler` harness stayed bounded to dev/admin scope, and the repeated `APP_ENV=prod` probe in the healthcheck remained a non-fatal gating diagnostic rather than a new public or cataloged proof surface.  
  * For `po-005`, the durable PASS pattern was exact agreement on one published `DEV_SAMPLER_URL` value across the environment snapshots, combined with an explicit disposition split: direct runtime closure for `codespaces` and approved `binding-equivalence` closure for `local_dev`. The step remained supportable only when that stated closure mode and the no-new-local-runtime-claim posture were both preserved.  
* For bounded validation or blocker-classification OPS lanes, the durable PASS pattern was a read-only validation run with an explicit action log, command ledger, exit codes, and a written classification result. These steps could be accepted for their bounded purpose even when they did not themselves close the mapped PF09.x rows.  
* For W-001-style blocker classification, reviewers had to separate mixed implementation-plus-evidence blockers from pure governed approval or evidence blockers. A bounded conjunction inventory plus artifact- or CLI-focused canonical JSON gate PASS was not enough to prove exhaustive all-surface HTTP emitter coverage for `HDE-CONJ009.1`, while directly evidenced writer-envelope behavior could leave `HDE-CONJ008.1` as an approval/evidence blocker rather than a runtime defect.  
* For repo-side dev harness closure slices, the durable PASS pattern was a bounded helper, script, and test change set only: no new public route, no route-contract redesign, no new governed evidence family, and `/internal/dev/sampler` left functionally unchanged.  
* For dev Reader start helpers, silent `APP_ENV` defaulting was non-conforming. The durable posture was to propagate `APP_ENV` exactly as supplied, including unset or empty states, and to make the effective state explicit in governed evidence.  
* For dev sampler healthcheck tooling, `DEV_SAMPLER_URL` was the authoritative input. Reviewers should reject helper logic that reconstructs a hostname or port implicitly. The durable posture required an explicit hostname and explicit port, loud-fail behavior when the binding was missing or blank, and negative tests that prove the no-guess posture.  
* For OPS environment-validation reruns, truthful disposition mattered more than optimistic closure language. A bundle that proved a real dev-mode exercise but also recorded a prod-gating discrepancy had to keep `codespaces` at `not yet closed` and preserve that discrepancy as the accepted OPS truth.  
* For local-dev environment validation, absence of a published infra-owned `DEV_SAMPLER_URL` remained a real blocker. Reviewers should preserve `not yet closed` posture and reject guessed local URLs.  
* For sequencing-only remediation on epic-close artifacts, the durable PASS pattern was to keep acceptance and close-pack outputs blocked or incomplete-planned under current evidence rather than promote tokens or closure state early. Reviewers should accept the sequencing correction when it makes the no-claim boundaries explicit and preserves still-open PF09.x scope and accepted `not yet closed` environment truth.  
* For close-binding gates, the durable PASS pattern was explicit proof requirements rather than permanent-false blocks or weak file-existence heuristics. `ready_for_close_binding` had to require explicit row-closure proof for `HDE-CONJ009.1` and `HDE-CONJ008.1`, plus environment closure for `HDE-CONJ001.4`, and Live QA completeness had to require governed primary logs with `[exit_code] 0` rather than mere log existence.  
* For PR-04 close-pack closure, invented epic-local acceptance token names were non-conforming. The durable PASS pattern used canonical or PF10-minted token names only, while representing `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4` as bound PF09 scope rather than as acceptance tokens.  
* For close-pack generators and other close-pack-producing tooling, the durable PASS pattern was to enforce canonical token posture and PF09 scope posture at generation time rather than correcting those surfaces only in late remediation. Reviewers should treat generator output that invents epic-local token names or turns bound PF09 scope into acceptance-token claims as non-conforming even when later remedial edits could restate the close-pack correctly.  
* For epic-close QA bridge tokens, promotion from planned or missing to implemented or covered required real governed QA logs at the canonical paths with passing results. Generator logic or close-pack structure alone was not sufficient.  
* For final close-pack binding of mixed QA and OPS truth, the durable PASS pattern preserved the accepted `not yet closed` environment state inside the close-pack rather than overclaiming environment closure because the QA bridge evidence had become green.  
* For PR-04, same-PR refresh of the Human Index, Machine Mirror, close-pack companions, and related path-proofs remained necessary but not sufficient. Unrelated cross-epic governed drift stayed blocking until it was removed from the final remedial bundle.  
* For bounded W-004 closure, `binding-equivalence` was an acceptable closure mode only when the approved `DEV_SAMPLER_URL` for `local_dev` matched the approved Codespaces value for the same dev-only sampler harness, no new local-dev-only runtime behavior was claimed, the closure mode was stated explicitly, and the governed OPS-01 family was normalized to one authoritative posture. This was the bounded basis for supportable later-drain `Done` posture on `HDE-CONJ001.4` at epic close.  
* For final EPIC029 closeout, once PF10 explicitly recorded the controlling Conjunction work as complete in substance and supportable for later drain at epic close, the closeout review had to use that live PF10 truth plus the governed repo evidence as the authoritative in-flight closure basis while keeping PF09 as the later-drain record until epic-end drain.  
* Under that final close posture, `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4` were treated as supportable from repo evidence for later-drain `Done`, not as already drained PF09 state.  
* For final EPIC029 closeout review, PF23 functioned only as a confirmatory repo-reality cross-check. It was used to verify the existence and current classification of the closure-critical runtime surfaces and the current evidence-update skeleton, and to confirm that those realities did not contradict the governing PF10 closure basis.  
* For the decisive PF10 close-authority addendum in EPIC029, evidence-basis prose without direct evidence-pointer lines remained a real auditability gap but not a closure-truth reversal. The durable review posture was to record that caveat explicitly and rely on the governed repo evidence plus the live PF10 authority rather than silently assuming pointer-complete sourcing.

Known non-goals: these addenda do not redefine token semantics, A7 byte rules, or PF09 status rows. PF19 records the QA posture and review learnings only.

## **13.10 HDE-EPIC030 — QA learnings snapshot for Dissolution implementation, OPS, Live QA, and closeout evidence discipline**

PF19 records the EPIC030 PR-01 through PR-05, OPS remediation, Live QA, close-pack surfacing, QA RCA, docs-sweep, retrospective, and audit-analysis learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on Dissolution proof clusters across normalization, dev-only sampler, compat, threshold and tuning, category-framework evidence, no-user vendor-smoke remediation, Live QA step closure, documentation-drainage posture, close-pack surfacing, QA RCA, repo-docs evidence navigation, and PF23 audit-classification routing.

Key QA learnings:

* EPIC030 was an internal, admin, and dev-only Dissolution evidence pass, not a public-surface redesign. Reviewers should preserve the public Reader boundary and reject interpretations that turn admin/test evidence, compat evidence, or dev harness proof into new public Reader enablement.  
* Five-PR sequencing was part of the durable bounded-review pattern: normalization first, dev sampler second, compat third, threshold and tuning fourth, and category framework fifth. A later review should preserve that dependency order when interpreting which proof family supports which slice.  
* For PR-01 normalization closure, the durable PASS pattern required a repo-owned normalization-side handoff for zero-weight intent, targeted invalid-prefs and canonical-compare evidence, sibling path proofs, Human Index binding, and Machine Mirror binding. Synthetic handoff projections and unbound evidence files were not closure-grade proof.  
* Zero-weight semantics are best reviewed as normalized input truth handed to sampler or ranker ownership, not as a second exclusion rule hidden inside validation. The review proof must show the handoff path without creating a new route, flag, serializer path, or public contract change.  
* For dev-only sampler harness closure, the durable PASS pattern stayed on the existing internal/dev surface: no new public route, no new cataloged success route, IDs-only candidate output, seed metadata preserved as metadata, no-store and no-ETag posture, and targeted route or sampler tests paired with governed evidence artifacts.  
* The direct sampler evidence pattern required all of the following to stay coherent as one proof family: headers snapshot, body snapshot, seed-only proof, two-run identity proof, sibling path proofs, Human Index binding, Machine Mirror binding, and the expected evidence validation checks. A route test alone or a refreshed ledger alone was not sufficient.  
* Seed handling for the dev sampler remained metadata-only unless a later approved scope says otherwise. Reviewers should require proof that changing the seed does not change `candidate_ids` when the approved slice claims seed-only metadata posture.  
* Evidence-generator portability is a QA concern. A governed evidence generator that requires caller-supplied `PYTHONPATH` for normal repo-root execution is not portable enough for the proof family. Durable remediation fixes the generator bootstrap or import order and keeps the governed output paths stable, rather than relying on ambient operator shell state.  
* Bounded evidence-side churn is non-blocking when it is the natural outcome of canonical updater convergence, remains inside existing governed homes, is explained in the review record, and does not introduce a new runtime surface, new evidence home, or new artifact-family claim. The same churn becomes blocking when current proof-family bytes, sibling path proofs, or mirror rows are stale or internally inconsistent.  
* For compat evidence and indexing closure, the durable PASS pattern stayed on existing compat or admin evidence surfaces: no new public route, no new flag, no new serializer path, no close-stage artifact family, and no public Reader contract widening. Required proof focused on compat parity binding, compat identity binding, category-order binding, the narrative key-table linkage snapshot, and governed Index or Mirror visibility.  
* Compat parity proof must be byte-level when the claim is deterministic bytes. Parsed-object equality can hide byte drift and is not sufficient for AB and BA byte-identity claims.  
* Compat identity proof must bind the digest to the current canonical AB and BA bytes. A regex-only check that the identity hash merely looks like lowercase hex is not sufficient.  
* For threshold and tuning closure, the durable PASS pattern required routing compat threshold constants through the existing constants-pack source, proving band edges and compact diffs, and rejecting a second threshold home. Reviewers should treat new public routes, flags, serializer paths, close-pack artifacts, or QA-ledger paths as scope drift unless explicitly approved.  
* For threshold and tuning slices, review should keep admin or test compat surfaces separate from the public Reader-facing covenant. Admin or test compat evidence may carry scores, while the public Reader posture must remain numeric-free and unwidened.  
* A band-threshold proof family is coherent only when the constants binding proof, compact threshold diff, AB and BA identity-hash proof, sibling path proofs, Human Index binding, Machine Mirror binding, and validation checks all agree. Code routing alone or green tests alone are not sufficient when the governed evidence family is incomplete.  
* Evidence-generator PASS is claim-bearing. A generator must not emit top-level `status: PASS` when decisive predicates such as current AB and BA identity equality or canonical compare status fail or were not evaluated. The PASS value has to be derived from the live predicate checks that define the evidence family.  
* After generator logic changes, reviewers should require final governed artifacts to be regenerated from the final generator logic path. A stale artifact produced by earlier logic is not sufficient proof after remediation, even when later tests pass.  
* False-positive evidence generators need regression tests that force the failure path, not just the expected PASS path. When a prior defect allowed green status without a decisive predicate, the durable fix includes a test that proves the generator fails closed when that predicate fails.  
* Missing targeted regression coverage remains a review blocker when the missing test is the proof that previously exposed the defect. Durable remediation includes the defect-exposing test in the final passing bundle, not only adjacent compat or evidence tests.  
* For category-framework closure, the durable PASS pattern required per-channel mechanics evidence, canonical JSON compare evidence, a binding log, sibling path proofs, Human Index rows, Machine Mirror rows, and validation checks to agree as one evidence family. A top-level binding log that passes while the canonical compare fails is not acceptable.  
* For PR-05 category-framework proof, final acceptance posture depended on the proof bytes being regenerated after the generator fix, not merely on the generator code being corrected. The final binding artifact, path proof, mirror rows, and validation outputs had to reflect the final generator behavior.  
* For bounded category-framework evidence, staying inside the approved slice mattered: no public-route work, flag work, serializer or emitter work, close-pack work, QA-ledger work, Live QA runbook work, or PF-canon edits were required to make the proof family reviewable.  
* Repo-docs sweeps are QA-relevant when they prevent future agents from misreading evidence families. The durable docs-sweep pattern was to surface landed PR-slice evidence after implementation evidence was stable, distinguish implementation-slice evidence from close-pack evidence, and keep historical close-pack or ledger material labeled as historical.  
* PR-slice evidence and close-pack evidence are separate closure axes. Implementation PR evidence can support later status-drain posture, but it does not by itself prove the epic close report, close manifest, close-pack validation, or Live QA close-gate artifacts.  
* Reviewers should distinguish supportable-from-repo-evidence posture from already-drained PF09.2 canon. A review may support later PF09.2 drainage while still recording that the PF09.2 rows were not proven drained in the reviewed source set.  
* Close-stage gaps must remain explicit. For EPIC030, unresolved or unproven close-pack artifacts, Live QA discovery and QA RCA or doc-delta summary evidence, final PF09.2 drainage, aggregate post-epic validation, and docs lint or link-check automation were review questions, not facts to silently assume complete.  
* Evidence Index and Machine Mirror work is same-change product, not clerical cleanup. A PR-specific PASS artifact is insufficient when the Human Index, Machine Mirror, hash sentinel, and sibling path proofs do not bind the final artifact bytes coherently.  
* Bounded evidence-tool side effects should be explained and validated. They are not automatically drift, but they increase review surface and should either remain inside known single-writer behavior or be accompanied by a clear side-effect manifest.  
* PF23 audit findings should be classified before they become blockers, PR work, OPS work, or PF09.x task deltas. A PF23 observation can require must-act-now doc classification without creating new dev or ops scope.  
* Presenter namespace findings belong to architecture classification before QA treats them as a second presenter or serializer home. The QA question is whether public-byte emission still delegates to the governed single emitter path, not whether two repository namespace strings exist.  
* Reader or Endpoint Catalog metadata that is dev-gated must not be treated as production public Reader enablement without a separate explicit contract and runtime state change. QA review should route that classification to the CLI/API contract home rather than infer public-surface expansion.  
* Multi-root evidence layouts are not automatically alternate evidence homes. QA review should ask whether governed artifacts are bound through the Human Evidence Index, Machine Mirror, path proofs, and same-PR parity rather than requiring all evidence-like files to live in one directory.  
* I/O-bearing modules under the engine tree require seam classification before QA treats them as determinism failures. Pure compute modules remain controlled by purity obligations, while BodyGraph resolver, ingest, vendor, catalog, or loader seams require architecture and mechanics classification.  
* Vendor access under the BodyGraph seam should be routed to architecture and mechanics classification before it is treated as new vendor remediation scope. PF19 records the review posture only and does not decide the seam classification.  
* Directory naming findings must distinguish directory segments from filenames. Uppercase close-pack filenames that follow canonical close-pack patterns should not be treated as directory-case drift unless the owning path canon says so.  
* Truth-home-like root findings require PF12 classification before they become blockers. The review question is whether a root is acting as an independent authoritative evidence home outside the governed catalog, index, mirror, and path-proof discipline.  
* EPIC030 status-drain staging must keep three states separate during review: supportable from governed repo evidence, already drained into PF09.2, and reused history-only foundations. Reviewers must not describe reused foundations as newly implemented by EPIC030, and must not claim PF09.2 drainage unless the updated PF09.2 rows are present.  
* Reused foundation rows remained review context, not new EPIC030 implementation scope. When a source identifies rows as already-complete and history-only foundations, QA review should preserve that posture instead of turning them into new PASS claims for the active epic.  
* Governed evidence generators must fail closed for the evidence family they claim. A generator must not emit PASS unless every decisive predicate for that evidence family is evaluated and passes, and final governed artifacts must be regenerated from the final generator logic after generator remediation. This posture does not mint a new acceptance token, create a new gate, create an OPS task, or require an immediate blanket audit of adjacent generators.  
* For po-001, durable PASS review depended on a governed primary log and surface inventory proving that the epic remained an internal, admin, and dev-only Dissolution closeout with no public surface widening.  
* For po-002, durable PASS review depended on zero-weight user intent being preserved through normalization into sampler exclusion behavior, with pytest and generator return codes at 0 and the zero-weight handoff artifact present.  
* For po-003, durable PASS review depended on invalid viewer-preference rejection and stable normalization evidence: pytest return code 0, generator return code 0, and both invalid-viewer-prefs and canonical-compare evidence present and non-empty.  
* For po-004, durable PASS review depended on the dev sampler remaining environment-bounded, deterministic, and internal/dev only: targeted adapter or CLI tests passed, generator return code was 0, two-run identity evidence existed, and the headers proof preserved no-store and no-ETag posture for the diagnostic surface.  
* For po-005, durable PASS review depended on compatibility identity and parity evidence: targeted AB and BA identity tests passed, generator return code was 0, and the governed PR-03 identity and parity artifacts proved order-neutral, identity-stable, and parity-coherent behavior for the implemented slice.  
* For OPS-01 no-user vendor-smoke discovery, the durable acceptable pattern was bounded discovery-only evidence: command and help capture, presence-only environment capture, explicit command-candidate disposition, discovery-summary alignment, command ledger, and checksum coverage. A discovery result may be acceptable for its bounded purpose even when it records `TOOLING_BLOCKED` because exact command proof remains unresolved.  
* For OPS-01, unresolved command posture is a tooling blocker for later vendor-smoke execution, not a product behavior failure. Reviewers should preserve the non-claims: no QA PASS, no Live QA completion, no PF09 or PF09.2 status change, no acceptance-token creation, and no epic closure.  
* For OPS-01 secret posture, a boolean-only environment-presence artifact is acceptable OPS evidence when it proves required key presence or absence without persisting secret values. Secret values in persisted OPS evidence would be a tooling failure, not acceptable proof.  
* For read-only PR-01 no-user remediation discovery, the durable acceptable pattern was a report-only boundary and source-skew inspection with no code edits, no tests, no vendor calls, no repo artifact requirement, and no git diff hunks. For that approved discovery-only slice, the relevant proof was the read-only command ledger and the discovery findings, not test or CI PASS evidence.  
* PR-01’s key QA lesson was proof-class separation: public numeric-free Reader proof, internal or admin compatibility compute proof, and vendor-backed no-user behavior proof must not collapse into one another. Discovery that current tests prove full-argument UID-backed compatibility is not proof of no-user behavior.  
* PR-01’s source-skew lesson was that a stale logged failure shape must not be treated as current source truth. The follow-on implementation still had to prove no-user behavior rather than merely prove full-argument compatibility with injected identifiers.  
* For PR-02 no-user boundary remediation, the durable acceptable pattern was a local implementation boundary that accepts caller input containing only birthdate, birthtime, and location, creates any required deterministic internal metadata inside the resolver boundary, and proves the caller supplied neither `person_uid` nor `user_id`.  
* For PR-02, the root proof defect was equating “no caller-provided `person_uid`” with “no user identity.” A test that still passes caller-provided `user_id` or synthetic lookup rows is not a pure birth-data no-user proof.  
* PR-02 remained bounded when it preserved the internal/admin `/api/compat/v1` separation, preserved the public Reader bands-only and numeric-free posture, added no public route, added no CLI flag, added no serializer or emitter path, and left vendor-smoke validation as PO-only OPS work.  
* PR-02 local tests may support merge readiness for the local boundary proof, but they do not by themselves authorize PF09 or PF09.2 status change, QA PASS, Live QA completion, or epic closure while OPS-only vendor validation and broader acceptance remain separate.  
* For OPS-02 status posture, a successful controlled vendor-backed birth-only no-user smoke may support later review language that `HDE-DISS005.2` has vendor-backed birth-only no-user implementation-validation evidence, pending final QA interpretation and later PF09.2 drain. It does not authorize an immediate PF09 or PF09.2 status change by itself.  
* If OPS-02 is `TOOLING_BLOCKED`, `FAIL_TOOLING`, or `FAIL_BEHAVIOR`, no PF09 or PF09.2 status change is supportable from that OPS result.  
* For OPS-02 controlled vendor-backed birth-only no-user smoke, the durable PASS pattern required an exact vendor-source birth-only command, no caller user identity, `CLI_LOCAL_VENDOR_SMOKE` target classification when the smoke is CLI-local rather than hosted-service validation, PR-02 runtime binding, redacted environment-presence proof, non-empty parseable stdout, exit code 0, empty or explained stderr, no secret-value persistence, a checksum ledger, and a consolidated report that preserved non-claims. A PASS may support later `HDE-DISS005.2` review language, but it does not by itself authorize QA PASS, Live QA completion, immediate PF09 or PF09.2 status change, or epic closure.  
* For po-006, durable PASS review depended on two proof classes remaining green together: public compatibility output stayed bands-only and numeric-free, and OPS-02 evidence proved birth-only vendor-backed no-user implementation-validation posture. A bounded Moon Loop remediation that added a deterministic self-reference row to the OPS-02 checksum ledger was acceptable only because it was PO-approved, evidence-scoped, ran no new vendor command, opened no network rails, expanded no evidence roots, and preserved the approved check contract.  
* For po-007, durable PASS review depended on closed rails, generator return code 0, threshold ownership evidence naming the existing threshold source files, and a band-edges binding log proving the governed compat threshold binding and edge values. The review posture was no duplicate threshold home, no new file or path, and no Moon Loop deviation.  
* For po-008, a stale plan-required identity artifact filename was a non-blocking planning failure when the final accepted evidence used the PF10-supported implemented identity-hash artifact that proved the same comparison and identity goal. A bounded Moon Loop alignment to the implemented identity-hash artifact was acceptable when it introduced no generator or test code change, no PF-canon edit, no new evidence root, and no new proof goal.  
* For po-009, durable PASS review depended on category-framework proof-family coherence: generator return code 0, pytest return code 0, primary log PASS, category-framework binding PASS, canonical compare PASS, public numeric-free posture, index binding, mirror binding, and per-channel mechanics PASS.  
* For po-010, durable PASS review required fail-closed proof coverage for every generated proof family used by the epic. The correct posture was to preserve `TOOLING_BLOCKED` until PR-01 through PR-03 fail-closed coverage was added alongside PR-04 and PR-05 coverage, then rerun the full fail-closed suite and require the visibility artifact not to classify any generated proof family as unproven.  
* For po-011, durable PASS review depended on traceability evidence proving that required active-slice artifacts were present, indexed in the Human Evidence Index, and mirrored in the Machine Mirror, with primary-log PASS posture and copy-from-approved-instructions command provenance.  
* For po-012, durable PASS review depended on clean separation between reused-history rows and active HDE-EPIC030 rows, with no new-implementation claim for reused-history rows. Step-0B precondition remediation was acceptable only when the precondition issue was recorded, the approved Step-0B commands produced the governed doc-delta artifacts, the approved po-012 command block was rerun under closed rails, and the final verdict stayed bounded to check execution and evidence outcomes.  
* For po-013, durable PASS review depended on truthful separation among repo-supported completion, canon-drain completion, and formal close-pack completion. Documentation drainage was not a required execution gate before QA PASS, but real truth-and-proof blockers still had to remain visible.  
* For po-014, durable PASS review depended on coherent full-state proof after all implementation slices and documentation-facing updates were considered together: prior primary logs present, required PR-01 through PR-05 core artifacts present, and derived status agreeing with recorded header status and exit code.  
* For po-015, durable PASS review depended on a baseline QA execution context artifact that was present, parseable, and structurally complete, including rails, paths, and surfaces under governed `audit/qa/**` evidence roots.  
* For po-016, durable PASS review depended on a complete QA RCA with required interpretation sections, bounded closeout-readiness posture, and no formal close-pack overclaim. QA-correctable command syntax repairs were acceptable only when preserved transparently in governed evidence and when command identity, proof target, deliverables, and PASS or FAIL predicates were unchanged.  
* For po-017, durable PASS review depended on documentation drainage being recorded as non-blocking by itself while preserving explicit real truth-and-proof blocker categories. A PASS on this posture is not permission to erase required QA, evidence, or close-gate blockers.  
* For OPS-03 evidence packaging, the durable acceptable pattern was packaging-only scope: no QA reruns, no vendor calls, no implementation changes, no PF-Canon edits, no PF09.2 drain claim, and no new acceptance claim. Corrected evidence had to include a replayable labeled command transcript, labeled stdout, stderr, exit-code evidence, final inventory provenance, checksum coverage, final validation, and sibling path proofs.  
* OPS-03 close-pack surfacing was acceptable when the manifest used a named `key_outputs` map, required close-pack and supporting evidence artifacts were present, and PF09.2 drainage was explicitly preserved as later-drain support rather than overclaimed as completed status drainage.  
* The final EPIC030 QA RCA classified the main risk as proof-class and evidence-discipline failure, not a single runtime failure. The durable review posture was to separate public numeric-free compatibility proof, internal/admin compatibility compute proof, OPS-02 birth-only no-user implementation-validation proof, generated-proof fail-closed proof, repo-supported completion, PF09.2 drainage, and formal close-pack completion.  
* Bounded remediation loops reduced uncertainty only when they preserved approved scope, captured the correction in governed evidence, avoided PF-canon edits during QA execution, and did not hide deviations under PASS. Future closeout reviews should continue surfacing such deviations explicitly in Coverage vs QA Plan.  
* A READY WITH CAVEATS QA closeout verdict means QA closeout readiness under the reviewed PF10, PF19, PF06, and QA Plan source set. It is not a claim that PF09.2 drainage is already complete or that formal close-pack completion is proven beyond the surfaced close-pack artifacts and any separately reviewed OPS evidence.  
* For the final HDE-EPIC030 closure review, `SATISFIED` meant satisfied for the review’s closure trace only, not a PO closeout action. The durable posture was to rely on PF10-recorded PASS outcomes and close-pack surfacing while preserving caveats for PF09.2 later-drain documentation and canonization of lessons learned.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, threshold values, public Reader posture, PF09 or PF09.2 status rows, exact close-pack artifacts, exact OPS command templates, exact OPS evidence paths, exact Live QA runbooks, exact QA RCA bytes, exact close-pack artifacts, or concrete PF02, PF05, PF06, PF07, PF09.2, PF12, PF14, or PF27 doc deltas. PF19 records the QA posture and review learnings only.

## **13.11 HDE-EPIC031 — QA learnings snapshot for Fermentation SAFE rails, evidence coherence, docs sweep, and closure-risk posture**

PF19 records the HDE-EPIC031 PR-01 through PR-03, PF23 audit-classification, Live QA Step-0A through PO-018, QA RCA, docs-sweep, retrospective, and closeout-interpretation learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on Fermentation proof clusters across PR-01 SAFE rails open posture and provider-gate policy proof, PR-02 SAFE rails observability plus keys-only secret-safe log posture, PR-03 governed evidence and indexing coherence, PF23 audit-classification posture, early Live QA discovery, doc-delta capture, PO-001 through PO-018 check evidence, QA RCA, remediation-loop interpretation, deferred-work posture, and docs or closeout posture for the first SAFE rails slice.

Key QA learnings:

* HDE-EPIC031 was scoped to the first Fermentation Pass 2 SAFE rails slice only: SAFE rails open posture, keys-only observability and log posture, and governed evidence and indexing coherence for `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4`. Reviewers should preserve that slice boundary.  
* HDE-EPIC031 did not add a public Reader contract, public route, flag, payload field, HDAPI v2 runtime conformance, PO-only open-rails v2 smoke, narrative router parity closure, DB bridge parity, or AI, LLM, OpenAI, prompt, embedding, chatbot, model-call, or AI-provider scope.  
* For PR-01 SAFE rails provider-gate proof, the durable PASS pattern stayed local and deterministic: no live vendor call, no public Reader change, no HDAPI v2 runtime conformance claim, and no PO-only open-rails v2 smoke. Closed-rails proof could establish the approved provider-policy slice without widening runtime scope.  
* Provider retry and error-class evidence must classify non-200 outcomes precisely. Non-200 HTTP statuses outside `4xx` and `5xx` were not valid `network_error` outcomes and therefore were not retryable under the accepted remediation. Reviewers should require the proof family to distinguish real network errors, `5xx`, `429`, `4xx`, and other non-200 statuses rather than collapsing them into one retry class.  
* Default HTTP client behavior matters for provider-gate proof. An injected request-function test was not enough when the default request path could follow `302` redirects before classification. Durable remediation disabled default redirect following, converted `HTTPError` responses into status, body, and header tuples, and added regression coverage for the default redirect path.  
* Governed evidence-refresh side effects must be classified. When an evidence updater or generator refreshes proof companions outside the direct target family, reviewers should require each refreshed family to be named and classified as expected updater convergence, required dependency refresh, or unexpected drift. Stale or overclaimed side-effect classifications are blocking evidence-discipline defects until corrected.  
* Evidence-index and Machine Mirror validation must preserve mirror schema discipline without applying an unrelated epic’s acceptance roster to every mirror record. Roster-subset checks should be scoped to the intended epic records while keeping field-set, uniqueness, sort-order, path-proof, and proof-anchor validation intact.  
* For PR-02 SAFE rails observability and keys-only log posture, the durable PASS pattern required bounded vendor log keys, bounded label domains, success and failure class observability, payload-body absence, plaintext-secret absence, raw-secret-header absence, governed redaction scans, PR-specific rails-scope artifacts, and targeted regression tests.  
* Vendor-specific evidence must not overwrite shared evidence families. The accepted PR-02 repair moved vendor log samples and vendor rails-scope evidence into PR-specific governed audit files, restored the shared DB-bridge evidence rows, and kept the final evidence family auditable through Human Index, Machine Mirror, hash, LF, and path-proof checks.  
* Local keys-only redaction job definitions are acceptable as deterministic proof lanes when they remain closed rails, require no live vendor call, and are backed by governed evidence artifacts and tests. They do not by themselves create new public routes, new transport contracts, or new token semantics.  
* For PR-03 SAFE rails governed evidence and indexing coherence, the durable PASS pattern required the evidence family map, coherence artifact, refresh log, Human Index, Human Index hash sentinel, Machine Mirror, checksum companions, and co-located path proofs to agree as one governed proof family.  
* For PR-03, tests alone were not sufficient. Review acceptance required governed evidence, index and mirror parity, path-proof coherence, side-effect classification, and closed-rails validation checks after remediation.  
* PR-03’s original blocker was unclassified outside-family governed proof-companion churn. The durable remediation posture was to name writer proof companions, topology orientation refreshes, and HDE-EPIC030 PR-03, PR-04, and PR-05 proof-companion families, then classify each as expected updater convergence, required dependency refresh, or unexpected drift.  
* PR-03 side-effect classification had to include Machine Mirror rows, not only proof-companion paths. A side-effect classification is incomplete when it omits affected artifact keys, discovered paths, proof anchors, hashes, or sizes needed to prove the final mirror state.  
* PR-03 generated evidence had to fail closed. The coherence payload could report PASS only when classified side-effect paths existed, proof companions validated against their targets, and classified Machine Mirror rows matched artifact key, proof anchor, `sha256`, and `size_bytes`.  
* PR-03 `--check` mode had to validate final self-generated artifacts and final Machine Mirror bindings. Avoiding write-time self-hash recursion during generation did not justify a relaxed check that could mask stale mirror rows.  
* PR-03 preserved scope boundaries: no live vendor call, no public Reader contract change, no HDAPI v2 runtime conformance, no Live QA runbook, no closeout content, no token-matrix work, and no PF-Canon edit.  
* For HDE-EPIC031 PR-01 through PR-03, supportable later PF09.5 drain was subtask-specific. PR-01 supported `HDE-FERM001.2`, PR-02 supported `HDE-FERM001.3`, and PR-03 supported `HDE-FERM001.4`. The parent `HDE-FERM001` still required Lead or closeout judgment after all three subtasks.  
* Repo-docs sweeps are QA-relevant when they prevent future agents from misreading evidence families. The HDE-EPIC031 docs-only sweep was acceptable only as repo documentation history: it updated public and developer-facing repo docs, did not edit PF-Canon, did not edit implementation artifacts, and did not replace close-pack or PF10 history.  
* Documentation updates should be repo-verified and scope-limited, not inferred from implementation intent alone. Any command, flag, workflow, file path, module path, service name, endpoint, config key, environment variable, artifact path, token name, or validation claim mentioned in docs must be verified in repo reality or PF10 or PF-Canon where it is a terminology or contract claim.  
* Evidence tooling is an active implementation surface, not clerical cleanup. Mirror rows, hash sentinels, path proofs, and mirror self-record coherence can block review when stale, ambiguous, or unclassified.  
* PR-specific evidence paths matter. A new slice that reuses a shared artifact family can create false collision risk unless vendor-specific or slice-specific evidence remains in a PR-specific governed home and the shared family remains separately bound.  
* Close-stage gaps must remain explicit. PR evidence for HDE-EPIC031 supported the first SAFE rails slice, but it did not itself prove close-pack production, Live QA close-gate execution, final PF09.5 drainage, parent-task status, or deferred future Fermentation work.  
* For HDE-EPIC031, close-pack and closure-ledger artifacts, Live QA close-gate evidence, actual PF09.5 drain state, and parent `HDE-FERM001` final status were known open decision areas for Lead or closeout review. They should not be silently inferred from PR-01 through PR-03 evidence.  
* HDE-EPIC031 PF23 audit findings were classification observations, not automatic blockers or new work. When current PF canon already classifies an ambiguity surface, reviewers should record that no new PF-canon delta is required and should not convert the observation into new dev, ops, runtime, infrastructure, test, runnable-evidence, PF09.x, PF14, PF02, PF12, PF05, or PF20 work.  
* For HDE-EPIC031 PF23 audit classification, the durable posture was to route presenter namespace interpretation to architecture classification, Reader and compat route-prefix interpretation to CLI/API contract classification, multi-root evidence interpretation and truth-home/root proliferation to schema and artifact classification, deterministic-compute versus sanctioned I/O seams to architecture and mechanics classification, vendor seam placement to architecture and mechanics classification, and path-case interpretation to schema and artifact classification.  
* For Step-0A and Step-0B Live QA bootstrap, the durable PASS pattern was governed check-root evidence under the epic QA root, PF27-shaped primary logs with PASS and exit code 0, required discovery and doc-delta deliverables present, required BLOCKERS and CAVEATS headings present on both doc-delta surfaces, and no `TOOLING_BLOCKED` or `FAIL_TOOLING` condition triggered.  
* A plan-internal discovery-path mismatch was non-blocking for Step-0A when the approved execution helper and required deliverables used the stable check-root discovery path, the run followed the approved execution command path, no additional loci were introduced, and current-state evidence remained evaluable under the check directory.  
* For PO-001 through PO-003, durable PASS review depended on closed-rails execution with deterministic pins, governed check-root deliverables, primary logs recording PASS and exit code 0, and result artifacts proving the first-slice scope boundary, closed-default provider access, explicit bounded opening, no-live-vendor policy, and refusal-before-input or refusal-before-ingest ordering where required.  
* For PO-001 scope-boundary checks, reviewers should expect explicit proof that later vendor-version/runtime expansion, database/runtime follow-up expansion, router or public-contract expansion, public-surface widening, close-pack work, and acceptance expansion remain excluded from the current QA execution.  
* For PO-002 provider-access checks, durable PASS review required provider tests to pass, closed-by-default refusal evidence to exist, bounded opening evidence to exist, and no-live-vendor policy to remain preserved.  
* For PO-003 refusal-ordering checks, durable PASS review required refusal-before-input or refusal-before-ingest ordering evidence under governed check-root paths, not only a generic provider-gate PASS claim.  
* For PO-004 and PO-005, durable PASS review depended on plan-defined behavior criteria passing without remediation: provider non-success outcomes classified precisely, pinned attempts and retry-backoff evidence present, typed 429 evidence present, Retry-After delta handling proven, and governed primary logs recording PASS and exit code 0\.  
* For PO-006 keys-only log posture, a QA-created harness predicate that falsely classified keys-only evidence as `FAIL_BEHAVIOR` could be corrected through bounded Moon Loop remediation when the generator check and redaction evidence were already PASS, the failure signature was captured in the same evidence stream, the remediation note explained the predicate correction, rerun PASS evidence was captured, and patch plus changed-files artifacts with hashes were preserved.  
* For PO-006, the durable PASS pattern was allowed-keys presence, payload-body absence, plaintext-secret absence, raw-secret-header absence, governed primary log PASS, result artifact PASS, and a doc-delta record explaining the Moon Loop predicate correction. A planning failure in the QA-created helper was non-blocking only because final evidence was current, governed, and auditable.  
* For PO-007, durable PASS review depended on sensitive-provider-data absence and live-vendor-call prohibition being proven together. The acceptable proof posture was generator return code 0, redaction scan presence, live vendor calls still forbidden, and check-scoped PASS evidence under closed rails.  
* For PO-008, durable PASS review depended on governed human and machine evidence coherence after Moon Loop remediation. The accepted remediation had to preserve the failure signature, remediation note, rerun PASS excerpt, changed-files proof with checksums, closed-rails refresh context, hash-sentinel posture, path-proof posture, and validator return codes. A plan mismatch around the intended narrow Moon Loop posture was non-blocking only because the final remediation was auditable in the same evidence stream.  
* For PO-009, durable PASS review depended on machine-readable evidence alignment: the family map had to be present, machine-readable, and aligned with the Machine Mirror, with mirror presence, EPIC031 discoverability, mirror path-proof posture, and mirror-schema success preserved in the governed evidence stream.  
* For PO-010, durable PASS review depended on generated-proof fail-closed posture. The prior generator check-mode blocker had to be resolved, PR-01 check-mode proof had to be present, PR-02 and PR-03 generator checks had to pass, and the final result had to record PASS rather than leaving the step in a blocked state.  
* For PO-011, durable PASS review depended on acceptance-claim boundary discipline. The check could pass only by recording no claimed tokens, limiting claims to the evidence scope, and preserving missing acceptance-map or token-matrix posture as close-stage artifact posture rather than runtime behavior failure.  
* For PO-012, durable PASS review depended on active Fermentation subtask supportability without PF09.5 drainage overclaim. The proof posture was that `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4` were supportable from current evidence while `pf09_5_drain_claimed` remained false.  
* For PO-013, durable PASS review depended on reused foundations remaining history-only. The proof posture had to show no new implementation claim for reused foundation rows and active work limited to `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4`.  
* For PO-014, durable PASS review depended on implementation readiness not being treated as final QA outcome. Required prior logs had to be present, and implementation-readiness posture had to remain separate from final QA outcome.  
* For PO-015, durable PASS review depended on truth-class separation: implementation readiness, QA readiness, final QA outcome, and documentation drainage remained separate, and PF09.5 drainage was not treated as required before QA PASS.  
* For PO-016, durable PASS review depended on preserving the vendor-version runtime non-claim. The check had to show no vendor-version runtime conformance claim and a visible no-live-vendor policy.  
* For PO-017, durable PASS review depended on preserving the live-vendor-behavior non-claim. The check had to show no live vendor behavior claim, live vendor calls forbidden, and local implementation proof kept separate from live vendor proof.  
* For PO-018, durable PASS review depended on Live QA staying proof-only. Live QA could prove current results, but it did not perform implementation, remediation, PF edit, or closeout action.  
* For HDE-EPIC031 QA RCA, durable closeout interpretation depended on using PF10 as primary where it explicitly speaks, PF23 as read-only current-reality context only, PF19 as QA process and evidence-posture basis, PF06 only for the QA RCA and Doc Delta summary requirement, PF-Canon where PF10 is silent, the Implementation Guide only for intended scope framing, and the QA Plan only for intended QA requirements framing. PF20 was not used.  
* Coverage vs QA Plan accounting had to list every Step-0A through PO-018 step in plan order, mark each covered step fully evidenced from PF10, and identify non-blocking mismatches or deviations without converting them into behavior failures.  
* Remediation-loop interpretation had to distinguish useful bounded remediation from papering over failure. PR-01 reduced uncertainty by fixing retry classification and redirect handling, PR-02 reduced evidence-collision risk by moving vendor evidence into PR-specific governed paths, PR-03 reduced churn by converting outside-family proof refreshes into explicit side-effect classification, Step-0A remained accepted planning ambiguity, PO-006 corrected a false harness predicate, PO-008 restored governed evidence coherence, and PO-010 resolved the prior generated-proof check-mode blocker.  
* The Lead Dev retrospective RCA for HDE-EPIC031 classified the recurring issue class as proof-boundary and evidence-discipline separation, not a single runtime failure. The durable prevention posture is to keep provider status classes separated, require generated proof to fail closed when decisive check-mode or companion evidence is missing, keep Moon Loop remediation bounded and evidence-linked, preserve current-state check-root discipline, keep PF23 as context rather than acceptance authority, and separate implementation supportability, QA result, close-pack packaging, PF09.5 drainage, and formal closeout posture.  
* Implementation gaps remained deferred work, not HDE-EPIC031 closeout facts. HDAPI v2 runtime conformance, DB bridge and DB runtime acceptance, router parity, narrative registry closure, and parent `HDE-FERM001` status posture each required later scoped evidence or close/drain judgment and could not be inferred from HDE-EPIC031 provider-control proof.  
* The final HDE-EPIC031 QA verdict posture was `READY WITH CAVEATS`. Strong PF10 evidence pointers existed for the three implementation clusters and all QA Plan check clusters, but formal close-pack completion, PF09.5 drainage, parent-task posture, and deferred later Fermentation work remained caveats rather than failed Live QA behavior.  
* Vendor-version runtime conformance and live vendor behavior MUST NOT be claimed from the HDE-EPIC031 closeout. The durable posture was that live vendor calls remained forbidden and vendor-version runtime conformance remained unclaimed.  
* Documentation drainage was not a blocker by itself when QA truth and proof were complete, but the closeout record still had to preserve the no-claim state for PF09.5 drainage and formal close-pack completion.  
* For the final HDE-EPIC031 closure trace, `SATISFIED` meant satisfied for that review trace only, not a PO closeout action. The durable posture was to rely on PF10-recorded PR-01, PR-02, and PR-03 supportability, Step-0A through PO-018 PASS posture, READY WITH CAVEATS QA/RCA verdict, and absence of unresolved PF23 contradiction, while preserving formal close-pack completion, PF09.5 drainage, parent `HDE-FERM001` status posture, and deferred later Fermentation work as caveats rather than failed Live QA behavior.  
* Phase-close posture with caveats means implementation and QA proof were strong enough for the reviewed closure trace and no hard requirement remained before that trace could be treated as satisfied. It does not claim PO closeout, completed PF09.5 drainage, formal close-pack completion beyond separately reviewed evidence, or completion of deferred HDAPI v2, DB bridge, narrative, or router lanes.

Known non-goals extension: these addenda do not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, HDAPI v2 runtime conformance, exact provider error bytes, exact evidence paths, exact tests, exact docs PR paths, exact close-pack artifacts, exact Live QA runbooks, exact QA RCA bytes, exact PF09.5 status rows, parent-task status, deferred HDAPI v2 work, deferred DB bridge or runtime work, deferred router or narrative work, or concrete PF05, PF06, PF09.5, PF12, PF14, or PF27 doc deltas. PF19 records the QA posture and review learnings only.

## **13.12 HDE-EPIC032 — QA learnings snapshot for narrative-router parity, registry diffing, DB provider parity, non-dev typed DB failure, audit classification, Live QA readiness, docs posture, and evidence-indexing discipline**

PF19 records the HDE-EPIC032 PR-01, PR-02, PR-03, OPS-01, PR-04, remedial PR-01, combined-evidence QA-readiness decision, Live QA Step-0A through PO-024, final QA closeout review, QA RCA, audit-review, docs-sweep, and implementation-retrospective learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on Fermentation proof clusters across PR-01 narrative-router parity and evidence-indexing token posture, PR-02 narrative registry diffing, Doc-Delta identity, pack identity, and evidence indexing, PR-03 DB bridge fallback and provider-parity harnessing, OPS-01 DB provider parity evidence capture, PR-04 non-dev typed DB failure plus DB evidence coherence, remedial PR-01 selection-order structural evidence, combined-evidence supportability for `HDE-FERM004.2`, Live QA readiness checks through PO-024, final QA closeout review, QA RCA, PF23-style audit classification, repo-docs evidence navigation, and close-risk posture.

Key QA learnings:

* For HDE-EPIC032 audit review, the durable posture was classification-only. Findings about presenter namespace, Reader and compat route responsibility, multi-root evidence, deterministic compute versus sanctioned I/O seams, vendor seam placement, path casing, and truth-home-like roots were already classified by current PF canon and did not create new dev, ops, runtime, infrastructure, test, runnable-evidence, PF09.x, PF14, PF02, PF12, PF05, or PF20 work.  
* Audit findings should route to their owning PF homes without becoming PF19 acceptance criteria. Presenter namespace and I/O seam findings route to HDE Architecture and, where mechanics are involved, HDE Mechanics Guide. Reader and compat surface classification routes to HDE-CLI-API-Vendor-Ref. Evidence-root, path-case, root-authority, Human Index, Machine Mirror, and path-proof classification routes to HDE-Schemas and Artifacts.  
* For narrative-router parity closure, the durable PASS pattern required fixed router matrix coverage, missing-key fail-closed behavior, two-run identity, AB and BA coherence where applicable, CLI and HTTP parity where defined, canonical JSON proof, and governed Human Index, Machine Mirror, hash, LF, and path-proof binding.  
* A router evidence generator and generated artifacts were not enough when the governed evidence row overclaimed an unsupported acceptance token. Evidence rows must use only registered or PF10-minted token names, even when the implementation behavior is otherwise correct.  
* The PR-01 failure class was acceptance-token overclaim inside governed evidence, not router behavior failure. Reviewers should separate implementation behavior from evidence-token posture when deciding remediation scope.  
* Durable PR-01 remediation required changing the evidence source row, regenerating the Machine Mirror and Human Index, refreshing hash sentinels and path proofs, rerunning targeted tests and evidence checks, and explicitly searching for the removed unsupported token in governed evidence surfaces.  
* The PR-01 key-table evidence row carried only the canonical JSON token after remediation. Approved parity rows retained their registered parity, two-run, and composite identity token posture.  
* Public Reader contract posture remained unchanged. PR-01 evidence did not implement registry work, DB work, HDAPI v2 work, OPS work, public Reader contract changes, or later epic slices.  
* Evidence refresh churn from prior or adjacent proof families was acceptable only where it was force-refresh or canonical-tooling churn and remained distinct from PR-01 behavior change. Reviewers should not treat unrelated evidence-tool churn as proof of new feature scope.  
* For HDE-EPIC032 PR-01, supportable later PF09.5 drain was subtask-specific. The combined Original PR and Remedial PR evidence supported later-drain `Done` posture for `HDE-FERM002.2`; it did not itself update the PF09.5 row.  
* For narrative registry diffing and Doc-Delta identity closure, the durable PR-02 PASS pattern required deterministic registry diff generation, Doc-Delta posture evidence, pack identity proof, evidence-index and Machine Mirror binding, sanity-pipeline generator ordering, orientation evidence remediation, hash sentinels, LF checks, path validation, and path-proof coherence.  
* Narrative registry diff proof had to fail closed on malformed or unsupported manifest and key state. A generator that copied manifest rows without validating file presence, sidecars, SHA, or size, accepted unsupported categories or bands, or inspected only already-present key groups was not trustworthy proof.  
* PR-02 registry proof required closed-set validation over category, band, perspective, slot, duplicate tuple, duplicate key, and the full expected tuple grid. Keys-only and no-prose registry evidence remained the intended proof posture.  
* Pack identity proof required canonical manifest bytes, `pack_sha = sha256(canonical manifest bytes)`, and same-bytes two-run identity. A pack identity artifact needed governed path-proof binding when used for acceptance support.  
* Narrative registry generation and generator check had to run before evidence index update and evidence updater check in the sanity pipeline. Index checks alone were not enough if stale registry diff or pack identity evidence could survive without rerunning the generator.  
* Orientation evidence freshness was acceptance-relevant for this slice. After PR-02 added three indexed artifacts, the orientation artifact had to refresh from the old artifact count to the current count and carry coherent path-proof, Index, Mirror, and hash updates.  
* Shared evidence-tool refresh churn from PR-01, writer, topology, EPIC030, Human Index, Machine Mirror, and path-proof families was non-blocking when it was canonical tooling refresh behavior, stayed governed, and did not reopen PR-02 behavior or scope.  
* PR-02 evidence rows used only approved PR-02 token names and did not introduce `NARR_REGISTRY_CLOSURE_OK` or any new acceptance token.  
* For HDE-EPIC032 PR-02, supportable later PF09.5 drain was subtask-specific. The PR-02 evidence supported later-drain `Done` posture for `HDE-FERM003.2`; it did not itself update the PF09.5 row.  
* For HDE-EPIC032 PR-02 final validation, durable PASS review depended on the full validation bundle passing after remediation: generator checks, evidence updater checks, orientation checks, mirror schema, hash validation, path validation, LF validation, pytest, and `git diff --check`. The validation bundle supported acceptability only because it ran after the registry diff, pack identity, Doc-Delta, Index, Mirror, path-proof, and orientation evidence surfaces had converged.  
* For PR-03 DB bridge fallback and provider-parity harnessing, the durable PASS pattern preserved `DBAccess` as the provider-agnostic façade, proved dev and stage bridge fallback through the adapter façade, proved bridge capability, compared direct and bridge providers on a deterministic corpus, avoided fake live parity, and kept evidence secret-free.  
* PR-03 hardening of `APP_ENV=live` was a production-like alias posture, not a separate new runtime policy. Reviewers should require the same bridge guard for `live`, `prod`, and `production` where the approved slice classifies those names as production-like.  
* PR-03 evidence had to keep bridge fallback, bridge capability, provider parity, adapter selection, and environment connectivity proof classes separated. Green DB adapter tests, bridge consistency tests, generator checks, evidence-index checks, orientation checks, mirror/hash/path/final-LF checks, and public contract boundary checks were collectively relevant, but no one check alone proved the full slice.  
* PR-03 was acceptable without supporting a PF09.5 status move for `HDE-FERM004.2`. Reviewers should preserve the distinction between implemented provider-parity harnessing and later checklist status movement.  
* For OPS-01 provider parity closure evidence, the durable acceptable pattern was an OPS evidence packet that recorded close-candidate posture, explicit active corpus rows, row-level parity matches, bridge consistency PASS, closure rationale, command transcript, stdout, stderr, exit code, target environment, redacted environment presence, final report, checksum ledger, and non-claims.  
* OPS-01 provider parity closure was accepted as OPS evidence only. It did not claim QA PASS, PF09 or PF09.5 status movement, epic closure, or acceptance-token satisfaction for DB bridge or provider parity proof labels.  
* The accepted OPS-01 parity posture kept `ddl_fingerprint` in the active corpus and resolved the previous ambiguity by proving active-row match, not by excluding the row.  
* OPS-01 safety posture depended on presence-only environment capture, no plaintext secret values, empty stdout and stderr, exit code 0, and no irreversible infrastructure change or unsafe operation evidenced.  
* DB provider parity and bridge proof labels remained non-token proof labels unless HDE-Governance registers them or PF10 explicitly mints them. Evidence may support provider parity, bridge capability, and fallback proof obligations without claiming those labels as acceptance tokens.  
* OPS-01 could support later review or closeout use, but it was not a standalone PF09.5 status move. Later PR, QA, closeout, or canon-drain work had to decide whether and how to use the OPS evidence for status posture.  
* For PR-04 non-dev typed DB failure behavior, the durable PASS pattern required non-dev posture under `APP_ENV=stage`, real observed DBAccess attempt ordering, typed deterministic `BridgeUnavailable` with `missing_bridge_url`, no proactive probes, numeric-free public failure posture, secret-free artifact posture, targeted regression tests, and governed path-proof binding.  
* PR-04’s root defects were proof-shape defects: using production posture for non-dev evidence, serializing unexpected behavior as synthetic outputs instead of failing closed, and hardcoding selection order instead of deriving it from observed DBAccess attempts.  
* Durable PR-04 remediation required fail-closed generator behavior. If the non-dev evidence path observes success, unexpected typed error class or code, mismatched snapshot, or mismatched attempt order, the generator must fail rather than serialize synthetic proof as accepted evidence.  
* PR-04 DB evidence coherence depended on Human Index refresh, Machine Mirror refresh, hash sentinels, path proofs, single-writer evidence updater use, and validation checks after DB posture and bridge artifacts were refreshed.  
* OPS-01 provider parity closure evidence could be bound in PR-04 only as non-claiming OPS evidence. It was not QA evidence, not PF09.5 status movement, not epic closure evidence by itself, and not acceptance-token satisfaction for unregistered DB proof labels.  
* Shared path-proof and evidence-tool refreshes across DB, DB bridge, logs, narrative router, writer, topology, and historical EPIC030 proof families were non-blocking only when they remained governed evidence-tool churn, did not change PR-04 behavior, and did not expand scope or token posture.  
* PR-04 validation was acceptable when py\_compile, focused pytest, generator run, Evidence Index generation and check, mirror schema, evidence-index hash, evidence-path validation, and final-LF checks all passed after remediation.  
* PR-04 remained bounded to non-dev typed DB failure behavior and DB evidence coherence. It did not implement PR-03 work, PR-04-adjacent OPS closure as QA proof, HDAPI v2 runtime work, public Reader contract changes, or DB proof-label acceptance-token satisfaction.  
* For HDE-EPIC032 PR-04, supportable later PF09.5 drain was subtask-specific. The PR-04 evidence supported later-drain `Done` posture for `HDE-FERM004.3` and `HDE-FERM004.4`; it did not itself update the PF09.5 rows and did not change `HDE-FERM004.2`.  
* For `HDE-FERM004.2`, the durable HDE-EPIC032 QA-readiness posture after the combined-evidence ADR is that the row is supportable to `Done` from the combined PR-03 plus OPS-01 plus PR-04 evidence. The earlier no-status-move language in individual PR and OPS records was slice-local and should not be read as blocking a later combined-evidence supportability decision.  
* The combined-evidence supportability decision means no additional implementation work, OPS work, evidence capture, or prerequisite PF-canon action is required before Live QA for `HDE-FERM004.2`. It does not claim PF09.5 has already been edited, QA has already passed, the epic is closed, live vendor behavior has been proven, HDAPI v2 runtime conformance has been completed, OPS-01 is QA evidence, or unregistered DB proof labels are acceptance tokens.  
* For HDE-EPIC032 QA-readiness classification after the combined-evidence ADR, `HDE-FERM002.2`, `HDE-FERM003.2`, `HDE-FERM004.2`, `HDE-FERM004.3`, and `HDE-FERM004.4` were each supportable to `Done` from the recorded evidence base, while physical PF09.5 drainage remained later canon maintenance.  
* For HDE-EPIC032 Step-0A and Step-0B Live QA bootstrap, the durable PASS pattern was closed-rails execution, deterministic pins, governed check-root evidence under the epic QA root, stable check directories, manifest entries, manifest path proof, PF27-shaped primary logs with PASS and exit code 0, required discovery and doc-delta deliverables, and no `TOOLING_BLOCKED` or `FAIL_TOOLING` condition.  
* Step-0A’s bounded Moon Loop contingency was acceptable only because it corrected a QA-created harness placeholder failure before first governed receipt emission, kept the same check ID, rails, proof target, evidence paths, and tokenless posture, captured failure signature, correction note, changed files and hashes, and rerun PASS evidence in the same governed evidence stream.  
* For PO-001 through PO-003, durable PASS review depended on closed-rails execution with deterministic pins, governed check-scoped evidence, current-state manifest and per-check primary-header proof, `captured_env`, `evidence_artifacts`, empty intended and claimed token headers, and PASS primary logs under the epic QA root.  
* For PO-001, durable PASS review depended on scope-boundary proof: Reader and dev Reader catalog surfaces visible, OPS evidence not treated as QA PASS by itself, and DB proof labels not treated as acceptance tokens.  
* For PO-002, durable PASS review depended on narrative-router deterministic key-selection proof: router tests returning exit code 0, key-table evidence existing, and AB and BA parity evidence existing.  
* For PO-003, durable PASS review depended on keys-only router proof and public Reader non-expansion: key-table evidence remained keys-only, Reader route posture was visible without expanding into a new proof route, and APP\_ENV gating remained visible for internal and dev surfaces.  
* For PO-004 through PO-006, durable PASS review depended on plan-defined deliverables under governed check directories, per-step primary logs with PASS and exit code 0, result sidecars, manifest and manifest path-proof posture, and empty intended and claimed token headers.  
* For PO-004, durable PASS review depended on narrative-router identity proof: router pytest returned exit code 0, AB and BA or identity marker evidence existed, and the parity log carried the approved two-run and composite identity posture.  
* For PO-005, durable PASS review depended on registry diff and pack identity proof: generator check returned exit code 0, registry diff evidence was bound to HDE-EPIC032, pack identity posture was recorded, and registry diff plus pack identity artifacts remained governed and reviewable.  
* For PO-006, durable PASS review depended on registry non-overclaim proof: registry evidence did not claim unsupported acceptance semantics, router key-table evidence did not overclaim `NARR_REGISTRY_CLOSURE_OK`, the keys table remained keys-only, and unsupported registry token claim posture was false.  
* For PO-007 through PO-009, durable PASS review depended on current-state, check-scoped evidence under the epic QA root, per-check primary logs and path proofs, per-check result sidecars, manifest entries, manifest path proof, captured environment fields, evidence-artifact headers, empty intended and claimed token headers, and no `TOOLING_BLOCKED`, `FAIL_TOOLING`, or `FAIL_BEHAVIOR` condition. A non-fatal harness timestamp deprecation warning did not drive the verdict when no tooling or behavior failure state was recorded.  
* For PO-007, durable PASS review depended on registry diff binding, pack or evidence support, and visible doc-delta surface posture without converting the evidence into an ungoverned doc-delta claim.  
* For PO-008, durable PASS review depended on DB bridge and provider parity proof-chain visibility: the generator check returned 0, OPS closure status was visible, and the evidence chain did not isolate implementation-only or OPS-only proof as QA success.  
* For PO-009, durable PASS review depended on OPS provider parity evidence remaining support evidence only. The step proved OPS status visibility and explicit non-claim posture; it did not make OPS evidence into QA PASS, checklist completion, acceptance-token satisfaction, or epic closure by itself.  
* For remedial PR-01 after the PO-010 selection-order failure, durable acceptability depended on PR-routed repo remediation rather than Moon Loop relabeling. The PR added native `selection_order` emission in `DBAccess.for_current_env`, derived the order from observed adapter attempts/provider order, hardened generator validation for structural shape and mismatch failure, and stayed within the approved PR-only scope.  
* Remedial PR-01’s core QA lesson was that adapter-selection evidence must be structural and attempt-derived. `selection_order` needed to exist as JSON evidence tied to observed attempts, not merely as raw string visibility or detached generator-only data.  
* Remedial PR-01 preserved provider parity truthfulness by keeping unavailable direct-provider rows unavailable or skipped, preserving non-token DB provider and bridge proof-label posture, and avoiding Live QA rerun, OPS work, QA plan edits, PF edits, DOC\_UPDATE work, public Reader expansion, vendor or live-provider expansion, and new acceptance-token claims.  
* For PO-010 through PO-012, durable PASS review depended on current PASS result artifacts, no required-missing entries, no behavior failures, tokenless primary-header posture, manifest entries, manifest path proof, per-check path-proof deliverables, and primary headers with captured environment, evidence artifacts, intended tokens, and claimed tokens.  
* For PO-010, durable PASS review additionally depended on structural `selection_order` evidence after PR-routed remediation: `selection_order` had to match observed attempt providers and remain a structural adapter-selection field derived from observed adapter attempts or provider order, not a new token claim.  
* For PO-011 and PO-012, durable PASS review depended on the same current-state manifest, header, tokenless, and path-proof posture as PO-010, without relying on the PR-routed selection-order remediation as a substitute for their own governed check-scoped PASS evidence.  
* For PO-013 through PO-015, durable PASS review depended on the prior manifest and primary-header proof gap being remediated: the per-epic manifest, manifest path proof, manifest entries, `captured_env`, `evidence_artifacts`, `intended_tokens`, and `claimed_tokens` all had to be explicitly evidenced in the current report.  
* For PO-013, durable PASS review depended on evidence-index coherence proof: Human Index presence, Machine Mirror presence, and command checks returning 0 under the governed check evidence stream.  
* For PO-014, durable PASS review depended on Machine Mirror alignment posture through human and machine loci proof plus command checks returning 0\.  
* For PO-015, durable PASS review depended on generated-proof check posture: all required commands were green, command checks returned 0, and the result sidecar recorded PASS after manifest and header provenance gaps were closed.  
* For PO-016 through PO-018, durable PASS review depended on current governed result artifacts, harness exit code 0, closed-rails posture, manifest entries, manifest path proof, per-check primary-header trust proof, path-proof sidecars, tokenless posture, and explicit proof that DB proof-label non-token posture, fallback-scope checking, and active evidence-family presence were preserved without PF09.5 drainage overclaim.  
* For PO-019 through PO-021, durable PASS review depended on current governed result artifacts, shell exit code 0, manifest and manifest path-proof posture, per-check primary-log headers, path-proof sidecars, tokenless posture, and final PASS disposition. The reusable posture was that reused-foundation checks, truth-class separation checks, and closeout-truth checks must remain support evidence rather than implicit PF09.5 drainage, epic closeout, vendor-version runtime conformance, or acceptance-token satisfaction.  
* For PO-022 through PO-024, durable PASS review depended on current governed result artifacts, shell exit code 0, manifest binding, manifest path proof, per-check primary-log headers, path-proof sidecars, tokenless posture, live-provider non-claim posture, public Reader non-expansion posture, and proof-only Live QA role posture. The checks proved live-provider behavior was not claimed, the invented proof route was absent while `/reader` remained visible, and Live QA did not perform implementation, remediation, PF edit, or closeout action.  
* For HDE-EPIC032 final closeout review, source-use posture had to remain explicit: PF10 was primary for epic-specific recorded events, evidence pointers, QA outcomes, remediation loops, ADRs, implementation results, and closeout interpretation; PF23 was current-reality context only, not closure proof, acceptance source, or blocker source; PF-Canon governed where PF10 was silent; the Implementation Guide supplied scope framing only; and the QA Plan supplied intended QA requirement framing only.  
* If an operator prompt mislabels the epic phase or pass name, reviewers should use current PF10 and the provided artifact identity as source truth while preserving the prompt label only as artifact-map context. For HDE-EPIC032, that meant reviewing Fermentation Pass 3 rather than treating the prompt’s Dissolution Pass 3 label as authoritative.  
* For HDE-EPIC032 final QA closeout review, durable readiness depended on PF10 recording the full Live QA ladder as PASS from Step-0A and Step-0B through PO-024, with governed evidence posture restored where initial step reviews found gaps. PF10 remained primary for epic-specific events and evidence pointers, while PF19 supplied QA process, evidence trust, RCA, post-QA drainage, and closeout-readiness posture where PF10 was silent.  
* For HDE-EPIC032 QA RCA, the durable root-cause framing was evidence posture and scope-boundary drift, not a single unresolved product defect. The recurring issue classes were unsupported acceptance-token overclaim, non-QA-root remediation initially treated like Moon Loop correction, structural adapter-selection evidence, and repeated manifest/header proof gaps. The accepted closeout posture required PR routing, governed evidence refresh, manifest and header proof, tokenless non-claim discipline, and explicit separation of QA PASS, PF09.5 drainage, formal close-pack completion, and Lead closeout.  
* For the HDE-EPIC032 final verdict, `READY FOR EPIC CLOSEOUT` meant no key QA truth gap blocked closeout under the reviewed source set. It did not erase later documentation deltas, PF09.5 drainage, PF10 permanent drain, formal close-pack completion, or Lead closeout decision work; those remained follow-up or non-blocking caveats when QA evidence was complete and trustworthy.  
* For the final HDE-EPIC032 closure trace, `SATISFIED` meant satisfied for that review trace only, not a PO closeout action. The durable posture was to rely on PF10-recorded implementation, OPS, remediation, Live QA, final closeout, and QA RCA evidence while preserving PF09.5 drainage, PF10 permanent drain, formal close-pack completion, and Lead closeout decision work as follow-up or non-blocking caveats where QA truth and proof were complete.  
* HDE-EPIC032 recurrence prevention depended on keeping the process rails explicit: non-QA-root generator or product changes route as remediation or PR work rather than bounded Moon Loop correction; structural JSON predicates are required for governed fields such as `selection_order`; token registry validation must precede acceptance-artifact claims; manifest, header, and path-proof evidence must be present before trusting PASS labels; OPS, QA, PF09.5, and closure categories remain separate; and public Reader plus HDAPI v2 expansion boundaries stay explicit when adjacent narrative or DB surfaces change.  
* Repo-docs sweeps are QA-relevant when they prevent future agents from misreading implementation evidence. The HDE-EPIC032 docs PR was acceptable as a documentation-only repo-facing sweep because it did not edit code, tests, schemas, generated evidence, PF-Canon, or implementation artifacts, and because it preserved the boundary between repo documentation history and close-pack or PF09.5 drainage.  
* Documentation updates should distinguish implementation evidence from close-stage proof. Repo-facing docs may summarize landed PR evidence, OPS evidence posture, proof-label posture, unchanged public surfaces, and evidence locations, but must not imply QA PASS, formal close-pack completion, PF09.5 status movement, epic closure, or acceptance-token satisfaction where those claims remain separate.  
* Docs-only validation is acceptable when it proves the docs-only changed-file set, path existence, environment/config references, and markdown sanity under the approved docs scope. Absence of a dedicated markdown lint command should be recorded as a caveat or manual sanity posture, not converted into a runtime or implementation blocker.  
* The HDE-EPIC032 implementation retrospective’s key QA lesson was proof-class separation. Narrative router parity, narrative registry identity, DB bridge fallback, provider parity harnessing, OPS provider-parity evidence, non-dev typed DB failure, repo docs, PF09.5 drainage, and close-pack completion were separate closure axes.  
* PF10 2.1 DB proof-label drain targets were documentation and canon-maintenance concerns, not execution blockers. Reviewers should not treat pending Governance, Fermentation checklist, or Mechanics wording drain as a behavior failure when the governing evidence is complete and the non-claim posture is explicit.  
* Close-stage gaps must remain explicit. Implementation PR evidence supported later status-drain posture, but it did not by itself prove final PF09.5 drain completion, PF10 2.1 permanent drain, current repo filesystem proof for docs paths, formal close-pack completion, or Lead closeout decisions.  
* OPS-01 provider parity closure artifact shape may be a candidate reusable expectation for future parity evidence loops, but PF19 does not decide that artifact schema or mechanics home. Reviewers should route reusable shape decisions to the owning evidence, mechanics, or governance home rather than silently promoting the pattern inside PF19.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, HDAPI v2 runtime conformance, exact router bytes, exact registry diff bytes, exact pack identity bytes, exact DB provider bytes, exact DB bridge bytes, exact evidence paths, exact tests, exact repo-docs paths, exact PF09.5 status rows, PF10 drain targets, OPS closeout authority, public Reader contract changes, reusable parity artifact schema, exact Live QA runbook bytes, exact step-log bytes, exact close-pack artifacts, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF17, or PF20 doc deltas. PF19 records the QA posture and review learnings only.

## **13.13 HDE-EPIC033 — QA learnings snapshot for HDAPI v2 contract inventory, Live QA contract checks, docs sweep, audit classification, closeout review, Lead Dev retrospective, and source-precedence evidence discipline**

PF19 records the HDE-EPIC033 PR-01, Live QA Step-0B through PO-014, qa-16 closeout deliverables, final QA closeout review, QA RCA, Lead Dev epic retrospective, docs-sweep, implementation-retrospective, and audit-classification learnings only as a durable QA reference for future reviewers and implementers, not as acceptance criteria.

These addenda focus on the inventory-only HDE-FERM006 proof cluster for HumanDesignAPI v2 and legacy v1 contract inventory, source precedence, anomaly quarantine, endpoint reference, contract map, governed evidence binding, step-level Live QA contract-inventory checks, qa-16 closeout deliverables, final QA closeout review and RCA, Lead Dev closure-trace interpretation, repo-docs evidence navigation, rendered-escape review posture, and PF23-style audit-classification posture.

Source-use posture for this snapshot: PF10 is primary for epic-specific implementation results, QA events, remediation loops, evidence pointers, and closeout posture where it explicitly speaks; PF23 is read-only current-reality context only and is not closure proof, acceptance proof, a blocker source, or a deliverable source; PF-Canon is normative where PF10 is silent; the Implementation Guide is used only for intended scope and goals framing; and the QA Plan is used only for intended QA step and expected evidence framing. When a prompt label conflicts with PF10 and the Implementation Guide, reviewers must use the source-supported epic name. For HDE-EPIC033, the source-supported name is HDE-EPIC033 / Fermentation Pass 4\.

Key QA learnings:

* HDE-EPIC033 PR-01 was inventory-only. The durable PASS posture preserved out-of-scope boundaries for HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader changes, new HTTP homes, and AI scope.  
* Source inventory proof required closed-rails source-cache bodies and checksums for the source rows used by the inventory. Metadata-only closed-rails replay was not sufficient proof once the generator claimed source-backed inventory.  
* Vendor documentation-discovery files such as `llms.txt` and bounded `llms-full` excerpts were documentation-discovery-only context. They did not create AI product scope, runtime scope, evidence scope, token scope, credential scope, rails scope, QA scope, prompt scope, embedding scope, chatbot scope, model-call scope, or provider scope.  
* Source-precedence proof had to preserve validated v2 and v1 route YAML specs as promoted contract-inventory sources while quarantining suspect OpenAPI input when it was unavailable or failed validation. Suspect OpenAPI unavailability was not allowed to block promoted inventory generation when validated route specs remained usable.  
* Endpoint reference and contract-map proof had to distinguish recommended v2 chart routes from legacy v1 BodyGraph routes. Inventory proof could identify required route families and source specs, but it did not by itself prove runtime v2 request shaping, runtime source selection, live conformance, public Reader change, open-rails vendor smoke, or public payload behavior.  
* Tier handling had to come from actual cached endpoint table cells, not hard-coded substring defaults. Generator remediation was trustworthy only when tests covered source-cell tier parsing and non-blocking suspect OpenAPI handling.  
* Evidence-family binding for this slice required the source inventory, OpenAPI validation, known-anomaly quarantine posture, endpoint reference, contract map, acceptance map, token evidence matrix, Human Evidence Index, Machine Mirror, hash sentinels, and path proofs to converge as one governed proof family.  
* Collateral path-proof and orientation refreshes were acceptable only as limited evidence-tooling convergence when validation passed and the refreshes did not introduce feature scope, public contract scope, runtime source-selection scope, or AI scope.  
* Token discipline remained baseline-only. PR-01 evidence used existing registry-valid token names and did not mint or claim any vendor-v2-specific acceptance token.  
* The durable final validation bundle for PR-01 included generator refresh and replay, targeted HDAPI tests, full evidence tests, Evidence Index check, orientation check, path validation, LF checks, mirror schema check, evidence-index hash check, final-LF check, and git diff check. The bundle supported acceptability only because it ran after the governed contract-inventory evidence family converged.  
* For HDE-EPIC033 PR-01, supportable later PF09.5 drain was task-specific to HDE-FERM006 and its in-scope subtasks. The PR-01 evidence supported later-drain `Done` posture for HDE-FERM006.1 through HDE-FERM006.4 and the parent HDE-FERM006 while preserving HDE-FERM007 and HDE-FERM008 as out of scope. It did not itself update the PF09.5 rows.  
* For Step-0B doc-delta capture, durable PASS review depended on governed `audit/**` evidence, the plan-governed check-scoped primary log, sibling path-proof transcripts, both doc-delta surfaces, both doc-delta path proofs, a primary-log header recording PASS and exit code 0, closed rails, determinism pins, and the claimed `DOC_DELTA_PRESENT_OK` token. Step-0B readiness did not make any broader HDE-EPIC033 closure claim.  
* For Step-0B, both doc-delta surfaces had to carry the required no-delta baseline line, and the report had to preserve that no `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, missing-file, stale path-proof, or missing primary-log path-proof condition occurred. Absence of a deviation or Moon Loop repair meant no deviation ADR was required for that branch.  
* For PO-001 through PO-003, durable PASS review depended on governed `audit/**`, `artifacts/**`, and `docs/**` evidence roots, check-scoped primary logs, sibling path-proof transcripts, PASS primary-log headers, exit code 0, closed rails, determinism pins, and no claimed tokens for PO-001 and PO-002.  
* For PO-001, durable PASS review depended on source-inventory grounding through the required source mode, `cache_path`, `cache_sha256`, and required source-cache files. For PO-002, durable PASS review depended on proof that AI and LLM vendor documentation remained documentation-discovery-only and did not create AI product, runtime, or evidence scope.  
* For PO-003, durable PASS review depended on v2 and v1 route validation, targeted pytest success, PASS primary-log posture, exit code 0, closed rails, determinism pins, and the claimed `TESTS_PASS_OK` token. The Ruby dependency installation before rerun was an acceptable operational deviation because it changed neither required deliverables nor PASS or FAIL criteria, produced final PASS evidence, and was recorded as a Doc Delta candidate.  
* For PO-004 through PO-006, durable PASS review depended on governed `audit/**` and `artifacts/**` evidence roots, check-scoped QA receipts, sibling path proofs, PASS headers, exit code 0, closed rails, evidence-artifact headers, and no broader HDE-EPIC033 closure claim.  
* For PO-004, durable PASS review depended on suspect OpenAPI quarantine proof: the OpenAPI source remained quarantined and non-authoritative while the step preserved contract-inventory scope. For PO-005, durable PASS review depended on endpoint-reference and contract-map proof, including the required route rows and route-family labels.  
* For PO-006, durable PASS review depended on bounded Moon Loop remediation for a QA-harness phrase-match defect. The deviation was acceptable only because the defect was QA-harness-only, remediation stayed entirely under the approved QA root, no governed root outside the QA root was edited, and the rerun produced a final PASS receipt.  
* For PO-006 remediation R3, durable PASS review depended on PASS and exit code 0, closed rails, the claimed `JSON_CANONICAL_CHECK_OK` token, retained initial and remediation receipts, sibling path proofs, contract map and anomaly ledger references, JSON parse and final-LF posture, `non_conformance_claim` proof, contract-inventory-only posture, and runtime request-shaping boundary text.  
* For PO-007 through PO-009, durable PASS review depended on governed `audit/**`, `docs/**`, and `artifacts/**` evidence roots, check-scoped QA receipts, sibling path proofs, index, mirror, and path-proof coherence, PASS primary-log posture, exit code 0, and no broader HDE-EPIC033 closure claim.  
* For PO-007, durable PASS review depended on all five intended and claimed evidence tokens being present with governed evidence bindings: `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and `EVIDENCE_PATH_PROOFS_OK`. The Human Evidence Index and Machine Mirror had to bind source inventory, contract map, and related HDE-EPIC033 artifacts, with hash sentinels and path-proof files present.  
* For PO-008, durable PASS review depended on baseline existing-token posture and absence of vendor-v2-specific token minting. Its primary header had to keep `intended_tokens` and `claimed_tokens` empty while preserving sibling path-proof evidence.  
* For PO-009, durable PASS review depended on proving HDE-FERM006.1 through HDE-FERM006.4 in the acceptance map, recording no runtime v2 conformance claim, and stating repo-evidence-only supportability with no PF09.5 drainage claim. The execution-time proof-posture append was acceptable because it supplied the missing planned proof text without changing the proof target or expanding scope.  
* PO-007 through PO-009 remained PASS-grade only because the report recorded no final `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, required-file absence, stale path proof, or token-posture mismatch. The reconstructed PF27-compatible helper wrapper and the PO-009 proof-posture append had to remain explicit execution deviations, not hidden PASS assumptions.  
* For PO-010 through PO-012, durable PASS review depended on governed `audit/**`, `artifacts/**`, and `docs/**` evidence roots, check-scoped primary receipts, sibling path-proof transcripts, evidence-artifact binding, final claimed tokens set to none, closed rails, determinism pins, and no broader HDE-EPIC033 closure claim.  
* For PO-010, durable PASS review depended on retaining the initial `FAIL_BEHAVIOR` receipt as failure context while using the accepted remediation receipt as final proof basis. The final posture kept later adapter architecture, runtime request shaping, live vendor smoke, and runtime v2 conformance unclaimed.  
* For PO-011, durable PASS review depended on the original receipt reporting PASS, exit code 0, no Moon Loop remediation, and no claimed tokens. The final posture kept contract-inventory evidence inventory-only and did not claim runtime vendor conformance.  
* For PO-012, durable PASS review depended on retaining the initial `FAIL_BEHAVIOR` receipt as failure context while using the accepted remediation receipt as final proof basis. The final posture kept live vendor smoke, public Reader change, new HTTP home, and AI runtime or evidence scope outside the epic.  
* PO-010 and PO-012 used bounded Moon Loop remediation for a QA evidence-harness phrase-match defect. The durable acceptable pattern preserved the original proof targets, stayed inside the QA root, normalized the semantic phrase check against the governed anomaly ledger, and kept the initial failure receipts visible as context rather than relabeling the defect as product behavior failure.  
* For PO-013, durable PASS review depended on accepting R3 remediation proof only after a `QA_PLAN_UPDATE` routing receipt proved the non-QA-root evidence refresh route. The final PASS proof had to rely on routed refresh, include the routing receipt before gate checks, and preserve the original planned `FAIL_BEHAVIOR` and `ORIENTATION_MISMATCH` receipt as context.  
* PO-013 R3 PASS proof depended on convergence gates, path validation, LF checks, orientation check, mirror schema, evidence-index hash, message count zero posture, and non-expansion boundaries for runtime v2 conformance, public Reader surface change, and AI scope.  
* For PO-014, durable PASS review depended on PASS, exit code 0, required non-claims, and proof that the check did not perform implementation work, PF document edit, runtime vendor conformance, public Reader change, new HTTP home, AI scope, or epic closure action.  
* For `qa-16-close-out-deliverables`, durable PASS review depended on manifest creation, discovery artifact creation, QA RCA and Doc Delta summary creation, sibling path proofs, generated manifest coverage for Step-0B through PO-014, its own receipt, and explicit no-claim posture for broader epic closure or PO closeout.  
* A closeout deliverables check can satisfy its plan-defined execution deliverables without proving PO closeout. Reviewers must keep qa-16 assembly proof separate from Lead closure, board update, merge provenance, PF09.5 drainage, and formal close-pack completion.  
* HDE-EPIC033 final QA closeout readiness was `Ready with caveats`. The durable posture was that PF10 supported PR-01 evidence readiness, Step-0B PASS, PO-001 through PO-014 PASS, and qa-16 closeout deliverables PASS, while still preserving caveats for Lead closure decision, PF09.5 drain or status text, HDE-FERM007 and HDE-FERM008 future work, docs PR outcome binding, and formal closure axes.  
* For HDE-EPIC033 closeout review, PF10 was primary for QA events, outcomes, remediation loops, ADRs, and evidence pointers. PF19 supplied the closeout record, coverage accounting, Moon Loop, final QA closeout review, and RCA expectations where PF10 was silent. The Implementation Guide supplied goals framing only, and the QA Plan supplied intended requirements framing only.  
* For the HDE-EPIC033 Lead Dev closure trace, `SATISFIED` meant satisfied under that review’s closure trace only, not PO closeout action. The durable posture was to rely on PF10-recorded PR-01 evidence readiness, Step-0B through PO-014 PASS, qa-16 closeout-deliverables PASS, final QA closeout review, and QA RCA while preserving PF09.5 drainage, Lead or PO closeout decision work, board state, merge provenance, formal close-pack completion, HDE-FERM007, and HDE-FERM008 as separate closure axes or future work.  
* For HDE-FERM006 supportability versus PF09.5 drainage, PF10-supported Done posture was sufficient for the reviewed closure trace while physical PF09.5 status drainage remained later canon maintenance. Reviewers should name supportability and drainage separately and must not treat missing PF09.5 drained status text as an execution or closure-trace blocker when PF10 evidence is complete and trustworthy.  
* The Lead Dev process retrospective classified the recurring process risk as evidence, procedure, and harness fragility rather than product-runtime failure. Durable prevention posture is to preserve failed receipts, routing receipts, and final accepted receipts; keep QA-root remediation visibly separate from non-QA-root refresh routing; keep PF23 as context rather than closure authority; and keep repo-supported completion, canon drainage, merge provenance, board state, and PO closeout action separate.  
* The Lead Dev system retrospective preserved the product boundary: HumanDesignAPI v2 work needs governed contract inventory before runtime request shaping; source inventory needs cache grounding; suspect OpenAPI artifacts need validation or quarantine before authority; evidence identity depends on Human Index and Machine Mirror coherence; HDE-FERM006 can close the inventory foundation without closing v2 adapter architecture; HDE-FERM008 requires future PR or OPS evidence; public Reader scope remains stable while vendor-contract evidence evolves; and AI or LLM-oriented vendor documentation remains documentation-structure context only.  
* The inventory-only ADR for this epic is that HDE-EPIC033 closes only the HDE-FERM006 contract-inventory slice. It does not close HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader changes, new HTTP homes, or AI scope.  
* The PF23 context ADR for this epic is that PF23 may support surface and current-reality review only. Closure proof remains PF10-recorded outcomes and evidence pointers where PF10 explicitly speaks, with PF-Canon normative where PF10 is silent.  
* The final recommendation posture was `READY WITH CAVEATS`: implementation and process were strong enough to support the HDE-EPIC033 / Fermentation Pass 4 closure trace, but the report did not perform PO closeout, board update, merge provenance assertion, or formal ops action.  
* Coverage vs QA Plan accounting had to mark Step-0B through qa-16 in plan order, point to PF10 evidence for each fully evidenced step, and preserve mismatches or deviations as non-blocking only when PF10 recorded accepted remediation, operational deviation, or routing proof.  
* The final RCA root-cause category was evidence, procedure, and harness fragility around exact-string proof checks, rendered escape review posture, dependency readiness, and non-QA-root routing. PF10 did not support a product-runtime defect for the completed inventory-only HDE-FERM006 scope.  
* Bounded remediation loops reduced uncertainty only when they preserved proof targets and stayed inside the approved QA root. For PO-006, PO-010, and PO-012, the recurring brittle phrase-match defect was QA evidence-harness fragility, not product behavior failure.  
* Non-QA-root evidence refresh required stronger routing. For PO-013, final PASS-grade proof became acceptable only after `QA_PLAN_UPDATE` routing plus R3 final proof were both present and recorded before the accepted PASS basis.  
* Future HDE-FERM007 work remains separate from HDE-FERM006 closeout readiness. HDE-FERM007 would require future evidence for v2 source-selection policy, request shaping, response normalization, adapter-boundary proof, and closed-rails deterministic shaping.  
* Future HDE-FERM008 work remains separate from HDE-FERM006 closeout readiness. HDE-FERM008 would require future PR or OPS evidence for closed-rails refusal, PO-only open-rails v2 smoke, error and rate-limit mapping, normalized data path proof, and v2 conformance indexing.  
* Repo-docs sweeps are QA-relevant when they prevent future agents from misreading implementation evidence. The HDE-EPIC033 docs sweep was acceptable as repo documentation history because it documented the contract-inventory evidence family, verified evidence homes, source-cache posture, OpenAPI quarantine posture, AI and LLM documentation-discovery-only boundary, and HDE-FERM007 and HDE-FERM008 follow-up boundary without expanding runtime conformance, public Reader scope, open-rails vendor smoke, or AI scope.  
* Documentation updates should distinguish implementation evidence from runtime and close-stage proof. Repo-facing docs may summarize landed PR evidence, evidence homes, source-cache posture, OpenAPI quarantine posture, AI and LLM documentation-discovery-only posture, and downstream follow-up boundaries, but must not imply runtime v2 conformance, public Reader changes, open-rails vendor smoke, AI runtime scope, PF09.5 drainage, or epic closeout.  
* Docs-only validation is acceptable when it proves the docs-only changed-file set, repo path claims, generator help posture, docs-only scope, PF-canon non-edit posture, and markdown sanity under the approved docs scope. Absence of a dedicated markdown lint command should be recorded as a caveat or manual sanity posture, not converted into a runtime, evidence, or implementation blocker.  
* The implementation retrospective’s key QA lesson was proof-class separation. Contract inventory, runtime v2 request shaping, open-rails vendor smoke, public Reader behavior, AI scope, repo-docs history, PF09.5 drainage, and Lead closeout were separate closure axes.  
* Close-stage gaps must remain explicit. PR-01 implementation evidence supported later HDE-FERM006 status-drain posture, but it did not by itself prove Lead closure, final PF09.5 drainage, future HDE-FERM007 implementation, future HDE-FERM008 live conformance, PF10 coverage of the docs PR, or any required close-pack artifacts.  
* HDE-FERM007 and HDE-FERM008 remained future work. Reviewers should not infer runtime source selection, request shaping, response normalization, adapter-boundary proof, closed-rails deterministic adapter proof, live conformance, open-rails smoke, error or rate-limit mapping, normalized data path proof, or v2 conformance indexing from HDE-FERM006 contract-inventory completion.  
* Rendered escape artifacts remained a recurring process risk for HDE-EPIC033. Reviewers should apply the rendered-escape rule before issuing blockers and should not treat display-layer escaping, assistant-rendered escaping, markdown escaping, or source-byte escape appearance as a blocker without a separately proven non-rendering defect.  
* For HDE-EPIC033 audit review, the durable posture was classification-only. Findings about presenter namespace, HTTP adapter placement, app factories, endpoint-class boundaries, multi-root governed evidence, deterministic compute versus sanctioned I/O seams, vendor seam reachability, path-case convention, and root authority were already classified by current PF canon and did not create new dev, ops, runtime, infrastructure, test, runnable-evidence, PF09.x, PF14, PF02, PF12, PF05, or PF20 work.  
* Audit findings should route to their owning PF homes without becoming PF19 acceptance criteria. Presenter namespace, HTTP adapter placement, app factory authority, deterministic compute seams, and vendor seam placement route to HDE Architecture and HDE Mechanics Guide where applicable. Reader, compat, route, and API surface classification routes to HDE-CLI-API-Vendor-Ref. Evidence-root, path-case, root-authority, Human Index, Machine Mirror, and path-proof classification routes to HDE-Schemas and Artifacts.  
* A PF23-style audit observation that is already classified by current PF canon should remain a classification observation. It should not be converted into Must-act-now work, new PF09.x task deltas, PF14 or PF02 deltas, PF12 or PF05 deltas, PF20 historical corrections, or runnable-evidence work.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, HDAPI v2 runtime conformance, exact vendor endpoint bytes, exact auth header names, exact request-body fields, exact response-envelope bytes, exact credential names, exact evidence paths, exact tests, exact docs PR paths, exact PF09.5 status rows, exact Live QA runbook bytes, exact Step-0B or PO-001 through PO-014 receipt bytes, exact qa-16 receipt bytes, exact final QA closeout report bytes, exact QA RCA bytes, HDE-FERM007 request-shaping work, HDE-FERM008 open-rails vendor-smoke work, AI runtime scope, public Reader changes, new HTTP homes, Lead closeout requirements, PF23 audit requirements, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, or PF20 doc deltas. PF19 records the QA posture and review learnings only.

## **13.14 HDE-EPIC034 — QA learnings snapshot for HDAPI v2 source selection, request shaping, response mapping, boundary proof, OPS discovery, closed-rails refusal, and vendor non-claims**

HDE-EPIC034 produced a durable QA posture around HDAPI v2 vendor-seam work. The durable lesson is proof-class separation. Source selection, OPS discovery, request shaping, response-envelope mapping, adapter and presenter boundary proof, closed-rails refusal, open-rails smoke, live runtime conformance, normalized data-path proof, error and rate-limit mapping, PF09.5 drainage, and epic closeout are separate closure axes.

Durable QA learnings are as follows:

* Source-selection proof may distinguish recommended v2 chart behavior from legacy v1 BodyGraph behavior, but it does not by itself prove request shaping, response mapping, open-rails smoke, runtime conformance, public Reader behavior, new HTTP homes, or AI scope.  
* OPS discovery evidence may unblock downstream PR or QA design when it is bounded, secret-safe, and mechanically evidenced, but it does not by itself prove QA PASS, acceptance-token satisfaction, PF09 status movement, OPS completion beyond its own task, or epic closure.  
* Request-shaping proof must preserve canonical environment-key posture, v1 versus v2 route-family distinction, v1 versus v2 auth-header family distinction, geocode-key conditions, closed-rails posture, and no-live-vendor-call non-claims unless a PO-authorized open-rails task supplies live evidence.  
* Response-envelope mapping proof may prove that response type, success posture, error posture, data identity posture, and route variant are preserved at the proof layer, but it must not smooth over schema or compatibility gaps by inference and must not claim normalized-data-path completion unless that path is separately proven.  
* Boundary proof must be conservative and fail closed. QA must treat a proof model that can report `PASS` while missing adapter bypass, presenter bypass, public route drift, ad-hoc serialization, pure-compute external I/O, stale evidence rows, or vendor guard weakness as proof-model failure, not as live vendor runtime failure.  
* Closed-rails refusal proof may prove deterministic no-external-I/O refusal for implemented vendor paths under closed rails. It is not open-rails vendor smoke, live vendor success, full v2 runtime conformance, or normalized data-path proof.  
* Vendor proof must preserve non-claims. HDE-EPIC034 review posture did not create public Reader expansion, public route expansion, public flag expansion, public payload expansion, new service-home creation, AI runtime scope, OpenAI scope, LLM scope, or model-call scope.  
* Evidence-ledger refreshes and broad path-proof churn are acceptable only when final validation preserves Human Index, Machine Mirror, hash sentinel, path-proof, canonical JSON, final-LF, and evidence-path coherence. Evidence refresh alone does not expand behavioral scope.  
* Version-neutral route remediation is now a reusable QA review pattern for HDAPI work. QA should verify that vendor API version ownership sits in `HD_API_BASE_URL`, that runtime route construction uses version-neutral resource paths, that doubled version prefixes cannot occur, and that auth-header selection is metadata-driven rather than inferred from `/v1` or `/v2` strings. Remaining `/v1` and `/v2` strings must be classified by use before they are treated as defects.  
* The OPS-02 open-rails smoke and PR-06 evidence binding pattern is bounded. It may support the exercised live vendor route, credential-binding, endpoint availability, redacted response-shape, command-to-output provenance, and later HDE-FERM008.2 drainage posture. It does not prove full HumanDesignAPI v2 conformance, HDE-FERM008 parent completion, HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, normalized-data-path completion, all error and retry behavior, or public Reader expansion.  
* Final QA closeout for HDE-EPIC034 was sufficient for Lead closure review because the evidence package preserved implementation evidence, OPS evidence, Live QA evidence, check-scoped QA logs, path proofs, QA manifest coverage, QA RCA and Doc Delta summary, explicit non-claims, and PF10-recorded status supportability. That sufficiency is a Lead review posture, not a claim that PO closeout, board update, merge provenance adjudication, PF-canon drainage, or formal PO close-pack action already occurred.  
* PF09.5 drainage support and PF19 QA posture remain separate. HDE-EPIC034 supportability may justify later PF09.5 drainage for HDE-FERM007.1 through HDE-FERM007.5, HDE-FERM008.1, and HDE-FERM008.2, while HDE-FERM008 parent completion, HDE-FERM008.3, HDE-FERM008.4, and HDE-FERM008.5 remain future and unclaimed. PF19 records the QA posture only.  
* Post-implementation audit observations are planning and classification inputs unless an owning PF home or later PO decision turns them into executable work. Audit-confirmed repo-reality drift that is already classified by PF canon should not become new QA obligations, PF09 task deltas, mechanics deltas, architecture deltas, evidence homes, or token obligations by assumption.  
* Closure axes must remain separate. QA evidence, PF09 status drainage, PO closeout, board state, merge provenance, and PF-canon drainage are distinct. Documentation drainage alone is not a QA, implementation, or closure-review gate when current live truth and governed evidence support the result and no truth, proof, execution, safety, secret, scope, token, phase, production-functionality, or source-of-truth ambiguity remains.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, HDAPI v2 runtime conformance, exact vendor endpoint bytes, exact auth header values, exact request-body fields, exact response-envelope bytes, exact credential values, exact evidence paths, exact tests, exact PF09.5 status rows, exact Live QA runbook bytes, final QA closeout report bytes, QA RCA bytes, AI runtime scope, public Reader changes, new HTTP homes, PF23 audit requirements, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF20, or PF27 doc deltas. PF19 records QA posture and review learnings only.

## **13.15 HDE-EPIC035 — QA learnings snapshot for HDAPI v2 provider outcomes, response-normalization gap evidence, open-rails OPS observation, evidence-loop binding, PF29 follow-up, and closure-axis separation**

HDE-EPIC035 produced a durable QA posture for the remaining HDAPI v2 Fermentation live-conformance sequence. The durable lesson is that provider outcome evidence, response-normalization evidence, OPS open-rails observation, evidence-loop binding, PF09.5 drainage support, PF29 usage-guide drainage, Lead closure review, and future runtime compatibility are separate proof classes.

Durable QA learnings are as follows:

* Provider-outcome proof may establish deterministic status mapping, provider-code mapping, retryability, Retry-After parsing, malformed-response classification, network-error posture, redirect classification, and keys-only observability under closed rails. It must enforce closed rails before certification and must maintain coherent path-proof, Human Index, Machine Mirror, and hash-sentinel chronology. It does not by itself prove live vendor success, full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, PF09 status movement, or epic closure.  
* Response-normalization proof may truthfully record an exact adapter/schema gap. That is acceptable when the scoped evidence slice is gap-recording. It is not proof that v2 ChartResult or ChartSimpleResult data feeds the existing BodyGraph cache, person/bodygraph compute input, compat path, sampler path, admin path, or Glow app integration. Future runtime compatibility claims require a bounded adapter/schema proof or implementation.  
* OPS open-rails evidence may contribute bounded live-provider truth when it is PO-authorized, secret-safe, mechanically captured, and mapped into governed evidence. HDE-EPIC035’s OPS posture distinguished v2 `charts/simple` provider availability and geocode/header evidence from `bg:resolve` legacy BodyGraph ingest-path behavior. OPS evidence contribution is not QA PASS, OPS completion beyond the task, PF09 status movement, HDE-FERM008 parent completion, full runtime conformance, or epic closure.  
* `bg:resolve --source vendor` must be classified by what it actually exercises. In the HDE-EPIC035 evidence frame, it was a legacy BodyGraph ingest-path observation against the configured v2 base, not canonical v2 chart/geokey validation and not ChartResult-to-BodyGraph normalization proof.  
* PR-03-style evidence-loop binding may bind already-produced PR and OPS evidence into governed acceptance-boundary artifacts, token-evidence matrices, viability logs, Human Index rows, Machine Mirror rows, hash sentinels, and path proofs. That binding can support a later PF09.5 drainage recommendation for a scoped subtask, but it must not claim QA PASS, OPS completion, PF09 status movement, parent-task Done, closeout, or public-surface change unless those axes are separately proven by their owning sources.  
* PF29 drainage is a usage-guide follow-up, not a PF19 replacement. PF29 may document runnable HD Engine workflows and known usage limitations, but PF19 remains the QA posture home. PF29 should preserve the distinction between evidence-generation workflows and user-facing runtime workflows, warn that `bg:resolve --source vendor` is not the canonical v2 chart/geokey validation path, and keep exact nonclaims around ChartResult or ChartSimpleResult adapter gaps.  
* Repo documentation and PF-canon drainage are separate. Repo docs can reduce future operator and agent drift, but they do not replace PF-canon drainage, PF09 status updates, QA closeout, PO closeout, board update, or merge provenance.  
* HDE-EPIC035 QA Pass 1 established a QA PASS posture for the selected Live QA ladder only. The durable QA pattern is that each selected check must have a check-scoped primary log, explicit PASS status, exit-code evidence, path-proof coverage, and a manifest entry under the governed QA root. A PASS review of QA evidence does not by itself perform PO closeout, board update, merge action, PF09 drain, PF-canon drain, OPS completion beyond the bounded OPS task, or full runtime conformance.  
* Final QA closeout review for HDE-EPIC035 was supportable for Lead closure review because the repo evidence, OPS evidence, Live QA logs, acceptance map, token-evidence matrix, evidence indexes, path proofs, QA RCA and Doc Delta summary, and nonclaim boundaries aligned for the scoped epic. That posture remains a QA and Lead review conclusion, not a claim that PF19 owns close-pack bytes, board state, PF09 status changes, merge provenance, or PF-canon drainage.  
* HDE-EPIC035 QA RCA preserved two durable failure-prevention lessons. First, syntax or helper-code formatting defects must be classified separately from proof defects when proof identity is clear. Second, evidence-loop closure must preserve explicit nonclaims for full HumanDesignAPI v2 runtime conformance, public Reader change, new public route, app-side vendor credential ownership, raw payload persistence, and AI scope.  
* HDE-EPIC035 post-implementation audit observations were classification observations, not new QA obligations by default. Audit findings about presenter or adapter namespace, route placement, evidence roots, deterministic compute boundaries, vendor seam placement, lower-case roots, and root proliferation should route to their owning PF homes and should not become PF19 acceptance criteria, new PF09 tasks, mechanics deltas, architecture deltas, evidence homes, token obligations, or runnable-evidence work by assumption.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, exact vendor endpoint bytes, exact auth header values, exact request-body fields, exact response-envelope bytes, exact credential values, exact evidence paths, exact tests, exact PF09.5 status rows, exact Live QA runbook bytes, final QA closeout report bytes, QA RCA bytes, AI runtime scope, public Reader changes, new HTTP homes, PF23 audit requirements, PF29 workflow text, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF20, PF27, or PF29 doc deltas. PF19 records QA posture and review learnings only.

## **13.16 HDE-EPIC036 — QA learnings snapshot for bg:resolve route-policy classification, evidence-loop binding, Live QA remediation, and closure-axis separation**

HDE-EPIC036 produced a durable QA posture for the remaining Fermentation route-policy gap around `bg:resolve --source vendor`. The durable lesson is that route-policy classification, BodyGraph-detail runtime compatibility, evidence-loop binding, Live QA PASS, helper remediation, non-QA-root evidence refresh routing, PF09 drainage, PO closeout, board update, and PF-canon drainage are separate proof classes.

Durable QA learnings are as follows:

* PR-01 route-policy proof may establish that `bg:resolve --source vendor` selects `unsupported_runtime_nonclaim` for configured v2 bases while preserving explicit legacy BodyGraph fallback for non-v2 bases. That proof is acceptable only when it preserves closed-rails refusal semantics, route-auth metadata posture, no accidental `/v2/bodygraphs` request construction, no public Reader change, no new HTTP home, no app-side HumanDesignAPI ownership, no AI scope, no raw payload persistence, no OPS execution, and no full HumanDesignAPI v2 runtime-conformance claim.  
* PR-02 evidence-loop binding may bind PR-01 route-policy evidence into governed acceptance-boundary artifacts, token-evidence matrices, viability logs, doc-delta surfaces, Human Index rows, Machine Mirror rows, hash sentinels, and path proofs. That binding may support later PF09.5 drainage for HDE-FERM008.6, but it does not itself perform PF09 status movement, HDE-FERM008 parent Done, epic closeout, OPS completion, public-surface change, or full runtime conformance.  
* Live QA PASS for HDE-EPIC036 was check-scoped. Step-0B through PO-009, PO-010, and PO-011 through qa-14 were PASS-grade only because each selected check had current governed evidence, check-scoped primary logs or artifacts, path proofs, manifest coverage where required, and explicit nonclaims. A PASS review of the QA ladder does not by itself perform PO closeout, board update, merge action, PF09 drain, PF-canon drain, OPS completion, production deployment, or final acceptance.  
* PO-010 proved a bounded open-rails route-policy behavior: `PROVIDER_ROUTE_UNSUPPORTED`, `unsupported_runtime_nonclaim`, redacted base posture, and redacted route-auth posture for the approved route-policy objective. It did not prove full HumanDesignAPI v2 runtime conformance, BodyGraph-detail compatibility, public Reader behavior, raw payload persistence, or AI scope.  
* HDE-EPIC036 exposed a helper-registration failure pattern. If a plan-defined check is referenced as executable but the helper or harness does not register the check ID, QA must classify the issue as tooling or plan-validity failure, not product behavior failure. A bounded Moon Loop correction may make the check runnable only when it preserves proof identity and records the deviation, corrected registration, rerun result, and final PASS evidence.  
* HDE-EPIC036 exposed a non-QA-root evidence-routing pattern. When final PASS-grade QA evidence depends on refreshed governed evidence outside the approved QA root, the PASS receipt must cite an approved routing receipt or work item. Such refreshes are PR, OPS, QA plan update, or documentation-update work as applicable; they must not be relabeled as bounded Moon Loop work merely because they unblock a QA PASS.  
* Post-implementation audit triage remained classification-only. Findings about presenter namespace ambiguity, CLI entrypoint versus auxiliary script ambiguity, split HTTP or adapter placement, route concentration, multi-root evidence interpretation, deterministic compute versus sanctioned I/O seams, vendor or DB seam placement, path-case conventions, and truth-home-like root proliferation should route to owning PF homes and should not become PF19 acceptance criteria, new PF09 tasks, mechanics deltas, architecture deltas, evidence homes, token obligations, or runnable-evidence work by assumption.  
* Final closeout posture was ready with caveats for Lead review. The evidence package was strong enough to support phase-close review under the recorded closure-trace standard, but the recommendation did not perform PO closeout, board update, PF09 status movement, PF-canon update, OPS completion, production deployment, or final acceptance.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, exact vendor endpoint bytes, exact auth header values, exact request-body fields, exact response-envelope bytes, exact credential values, exact evidence paths, exact tests, exact PF09.5 status rows, exact Live QA runbook bytes, final QA closeout report bytes, QA RCA bytes, AI runtime scope, public Reader changes, new HTTP homes, PF23 audit requirements, PF29 workflow text, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF20, PF27, or PF29 doc deltas. PF19 records QA posture and review learnings only.

## **13.17 HDE-EPIC037 — QA learnings snapshot for HDAPI v2 BodyGraph-detail runtime conformance, mapped adapter proof, compatibility proof, open-rails smoke, parent evidence binding, and mapped-cache persistence boundary**

HDE-EPIC037 produced the durable QA posture for the final Fermentation HDAPI v2 runtime-conformance chain. The durable lesson is that field sufficiency, adapter mapping, resolver wiring, compatibility proof, open-rails runtime smoke, parent-level evidence binding, PF09 drainage support, QA PASS, PO closeout, board state, production deployment, broad HumanDesignAPI platform conformance, and future mapped-cache persistence are separate proof classes.

Durable QA learnings are as follows:

* Field-sufficiency proof comes first. HDE-EPIC037 PR-01 corrected unsupported token overclaim and aligned negative fixtures with evaluator behavior. A field-sufficiency artifact may prove fail-closed typed insufficiency, schema/adapter gap classification, no raw vendor payload body in evidence, and governed evidence linkage. It does not prove runtime adapter implementation, resolver rewiring, open-rails behavior, QA PASS, OPS completion, public Reader behavior, PF09 status movement, parent-task Done, or closeout.  
* Adapter proof is bounded. HDE-EPIC037 PR-02 implemented a pure v2 ChartResult adapter and evidence slice. That proof may show deterministic adapter mapping, typed unsupported or fail-closed outcomes, context-backed cache posture, no raw vendor payload persistence, and public Reader nonchange. It does not prove resolver wiring, live vendor behavior, compatibility computation, OPS completion, QA PASS, PF09 status movement, or parent-level closure unless later evidence binds those axes.  
* Resolver proof changed configured-v2 `bg:resolve` posture. HDE-EPIC037 PR-03 wired `bg:resolve --source vendor` for configured v2 bases to the version-neutral `charts` route and deterministic v2 adapter, while preserving explicit legacy fallback for non-v2 bases and closed-rails refusal before outbound I/O. QA must preserve the distinction between configured-v2 chart-backed dry-run behavior, non-v2 legacy fallback, generic BodyGraph ingest, and non-dry-run mapped-cache writes.  
* Compatibility proof is not public Reader drift. HDE-EPIC037 PR-04 proved that mapped v2 ChartResult adapter outputs can feed the existing internal compatibility computation path under closed rails, including deterministic identity and boundary artifacts. That proof does not create a public Reader change, new public route, new public flag, public payload change, new HTTP home, production deployment, or broad HumanDesignAPI v2 platform conformance.  
* OPS-01 open-rails evidence was PO-produced and bounded. It may support the exercised live v2 chart-backed `bg:resolve --source vendor --dry-run` smoke, including exit code zero, parseable JSON with status ok, v2 charts request posture, mapped adapter status, mapped-no-raw-vendor-payload cache posture, accepted compatibility path, redacted secret posture, command provenance, stdout, stderr, exit-code capture, checksums, and repo-resident evidence pointers. It does not by itself prove QA PASS, OPS completion outside the PO execution record, PF09 status movement, parent-task Done, epic closeout, production deployment, public Reader expansion, app-side vendor credential ownership, raw payload persistence, AI scope, or broad HumanDesignAPI platform conformance.  
* Parent evidence binding should happen last. HDE-EPIC037 PR-05 bound PR-01 through PR-04 evidence and PO-produced OPS-01 evidence into parent-level HDE-FERM008 evidence artifacts, with parent posture recorded as supportable to Done for later PF09 drainage only. Parent binding does not itself move PF09 status, perform QA PASS, execute OPS, close the epic, update the board, deploy to production, or drain permanent PF canon.  
* Evidence claims must stay tied to proving artifacts. HDE-EPIC037 showed that nonclaims snapshots cannot stand in for generic log/privacy/no-payload evidence, inspected-loci hashes are evidence facts rather than independent authority, and unsupported token claims must be removed rather than normalized by wording.  
* Mapped-cache persistence was later-phase work in the HDE-EPIC037 record. PF09.6-Canon-HDE-Build-Checklist-Distillation now records `HDE-DIST001.11 — v2 mapped-cache persistence hardening` as Done for the bounded non-production or controlled-rails slice, including adapter-mapped persistence, write/read-back parity, idempotence, secret safety, closed-rails refusal, and legacy fallback preservation. That completion explicitly does not authorize production-facing writes. PF09.7-Canon-HDE-Build-Checklist-Coagulation, under `BodyGraph resolver and vendor ingest (bg:resolve)`, keeps production or production-like `bg:resolve --source vendor --upsert` closed until a future Coagulation epic explicitly authorizes the posture with environment, secrets, deployment, rollback, and operational evidence.  
* Closure axes remain separate. Evidence support, token-evidence matrix support, PF09 status drainage support, QA PASS, PO closeout, board update, merge action, PF-canon drainage, production deployment, and epic closeout must not be collapsed. HDE-EPIC037 evidence may support later PF09.5 drainage for HDE-FERM008.7 through HDE-FERM008.12 and parent HDE-FERM008, but PF19 records QA posture only.  
* HDE-EPIC037 post-implementation audit classification was contextual, not new QA obligation creation. The audit mapped nine findings and marked zero as Must-act-now. The durable QA posture is that audit themes such as presenter namespace ambiguity, CLI entrypoint versus auxiliary scripts, cataloged dev routes versus route-discovery evidence, compat HTTP placement, multi-root evidence interpretation, deterministic compute versus sanctioned I/O, vendor seam spread, path-case conventions, and truth-home-like root proliferation should route to their owning PF homes when they require action. They do not become PF19 acceptance criteria, new PF09 tasks, new mechanics deltas, new architecture deltas, new evidence homes, token obligations, or runnable-evidence work by assumption.  
* HDE-EPIC037 QA Pass 1 accepted a remediation pattern for an evidence-assembly failure. The initial po-002 `FAIL_BEHAVIOR` remained preserved as failure context, the root cause was Step-0B overwriting generator-owned doc-delta evidence with a no-deltas template, and the accepted remediation restored the proof-bearing surfaces and reran the affected validation path. The durable QA posture is that final PASS support can come from accepted remediation and post-remediation suite evidence only when the original failure stream remains visible and the product behavior, public surface, governed index, and path-proof boundaries are not silently changed.  
* HDE-EPIC037 PO-007 was a bounded live runtime smoke, not broad platform proof. It may support the exercised open-rails `bg:resolve --source vendor --dry-run` runtime result, mapped ChartResult adapter status, redacted request posture, mapped-no-raw-vendor-payload cache posture, and status-ok evidence. It does not by itself prove production deployment, durable mapped-cache writes, broad HumanDesignAPI v2 platform conformance, public Reader expansion, app-side credential ownership, PF09 status movement, PO closeout, board update, or epic closeout.  
* HDE-EPIC037 final QA pass review accepted a package caveat only because current governed repo evidence supplied the proof. Zero-byte or unreadable uploaded package entries were not treated as proof. The durable QA posture is to validate current repo evidence, preserve the package caveat, and use readable governed repo artifacts only when they match the same check, proof target, evidence root, and nonclaim boundaries.  
* HDE-EPIC037 final QA closeout review was ready with caveats. The root cause category was evidence posture and proof-boundary fragility, not an unresolved product runtime defect. The closeout trace could be satisfied for review while still preserving separate follow-up for PF09 status drainage, PO closeout, board update, formal close-pack completion, merge provenance, PF-canon drainage, durable mapped-cache persistence, and production write reopening.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, exact vendor endpoint bytes, exact auth header values, exact request-body fields, exact response-envelope bytes, exact credential values, exact evidence paths, exact tests, exact PF09.5 status rows, exact Live QA runbook bytes, final QA closeout report bytes, QA RCA bytes, AI runtime scope, public Reader changes, new HTTP homes, PF23 audit requirements, PF29 workflow text, mapped-cache implementation work, production upsert authorization, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF20, PF27, or PF29 doc deltas. PF19 records QA posture and review learnings only.

# 14\. Codespaces QA environments (environment details)

## **14.1 Intent**

Codespaces is a supported Live QA execution environment, but it introduces pitfalls: ephemeral state, container drift, and unclear prerequisite documentation. This section defines the canonical requirements for Codespaces-based Live QA.

HDE Live QA execution-environment contract (normative).

GitHub Codespaces remains the canonical and preferred shared HDE QA console. `Canonical` and `preferred` do not mean `exclusive` or `mandatory for every epic`.

HDE Live QA may execute in Codespaces or in another execution environment permitted by the owning Live QA Plan or applicable QA authority, provided that the environment satisfies the plan’s material environment contract and produces governed, reproducible evidence.

Exact Codespaces execution and venue provenance are mandatory only when Codespaces is material to the approved proof. Codespaces is material when at least one of the following is expressly part of the proof scope:

1. The epic changes or validates the devcontainer, Codespaces bootstrap, Codespaces base image, Codespaces-specific tool availability, or another Codespaces-specific runtime dependency.  
2. The claim concerns Codespaces secret injection, environment provisioning, network egress, forwarded ports, repository mounting, filesystem behavior, provider identity, or another provider-specific integration.  
3. A supported operator workflow promises that the relevant harness, command, service, or application surface works in Codespaces.  
4. The behavior or defect is reasonably capable of differing in Codespaces because of the container, operating system, architecture, shell, dependency, filesystem, networking, or provider configuration.  
5. The Live QA Plan defines a venue-specific acceptance criterion and explains why venue can affect the result.  
6. The closeout claim asserts a Codespaces-run capability or relies on Codespaces execution as proof of operational readiness.

Codespaces is not made material merely because a plan names it as the intended venue, infrastructure canon calls it canonical or preferred, a command can run there, the repository contains a devcontainer, a secret name may be provisioned there, an optional dependency command uses a devcontainer script, a governed QA path exists, a current Codespace can inspect an earlier artifact, or a reviewer prefers uniform provider provenance.

A Live QA Plan that makes venue normative MUST state all four of the following:

* `Venue-specific claim`  
* `Why venue can affect the result`  
* `Required venue evidence`  
* `Effect of missing venue evidence`

Without those four statements, an execution-venue field records an intended or preferred operator surface. It does not create an acceptance criterion or closeout blocker.

Every governed HDE Live QA execution MUST capture the material environment facts required to interpret and reproduce the result, including as applicable:

1. the stable QA step or check identity;  
2. the exact source, commit, release, manifest, or other required source identity;  
3. the governed entrypoint, command, command family, endpoint, or harness invocation used;  
4. the required repository root or working locus;  
5. interpreter, runtime, toolchain, and dependency readiness;  
6. deterministic environment pins;  
7. rails and network posture;  
8. the external target identity when the check reaches an external service, database, or vendor;  
9. secret-presence or binding posture without secret values;  
10. the applicable PASS or FAIL predicate;  
11. actual exit status and result output;  
12. governed evidence paths and required manifest, index, hash, or path-proof bindings; and  
13. any accepted execution deviation that materially changed how the planned check ran.

When Codespaces is material, at least one governed, secret-safe artifact MUST bind the exact check or governed artifact, the Codespaces venue, the canonical repository association, the execution-source identity, the command or command family, the Codespaces-specific property being proven, and sufficient event or chronology information to connect execution to the evidence. A present-day Codespaces session does not retroactively prove an earlier venue.

Moving execution to another permitted environment is a material plan deviation only when venue is a proof axis, the substitution changes a material dependency, target, rails, network, secret, or runtime condition, or the plan forbids substitution for a supported reason. Otherwise, substitution is acceptable when the complete environment contract and all check predicates remain satisfied and the actual posture is recorded truthfully.

When venue is not material:

* absence of Codespaces provenance is not a QA failure;  
* absence of Codespaces provenance is not a closeout blocker;  
* an otherwise supported result MUST NOT be downgraded solely because the hosted or physical venue is unknown;  
* reviewers MUST NOT infer where execution occurred; and  
* the venue MUST be recorded as `NOT CLAIMED`, `NOT APPLICABLE`, or `UNKNOWN - NON-MATERIAL`, as appropriate.

Minimum required content (normative) is as follows:

* A stable, documented Codespaces/devcontainer configuration and required secrets/env var names (names-only; no values).  
    
* A reference to the authoritative environment profile in this PF (see §14.5) for the epic being tested.  
    
* A Step-0 Doc Delta Capture posture for missing/ambiguous prerequisites discovered during planning (see §14.6).  
    
* A maintenance rule: changes to prerequisites must be reflected in this PF in the same change-set as the code change.

Conformance note (normative): Codespaces conformance is evaluated using the Codespaces-specific requirements in §14.6; reviewers MUST NOT treat any optional snapshot artifacts as an approval gate.

## **14.2 Definitions (codespaces vs prod vs QA console)**

Definitions in this section are as follows:

* Codespaces / QA console. A Codespace is a QA console and artifact sink: it runs commands and stores ordinary Live QA evidence under the canonical `audit/qa/<epic-id>/` root and its PF12-Canon-HDE-Schemas-and-Artifacts-authorized children.  
    
* Prod. For Live QA, prod is the deployed service surface defined in infra canon, not the Codespaces container.  
    
* Closed rails vs open rails. Closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0` plus env pins) are the default for CI and determinism work; open rails from a QA console are allowed only for explicitly defined Live QA steps and mandated rails postures.

## **14.3 QA environment set (Codespaces)**

PF19 recognizes four product QA environment classes. A class is supported for Codespaces-based QA only when its profile is explicitly marked `Defined/supported` and every required field is populated from owner-authorized facts. At this revision, only the HD Engine Codespaces profile is defined/supported. The three App profiles are recognized but unsupported/undefined for Codespaces use.

* HD Engine — `Defined/supported`  
* App Back End — `Unsupported/undefined`  
* App Front End — Web — `Unsupported/undefined`  
* App Front End — Mobile — `Unsupported/undefined`

`Unsupported/undefined` is a configuration-status boundary. It does not claim that the product component is unsupported, absent, or untestable. Planning may identify the missing profile facts, but a check that materially depends on an undefined profile is `TOOLING_BLOCKED` until owner-authorized facts and a complete profile are canonized. Another execution environment may be used only when its owning plan or authority defines the complete material environment contract; it must not be represented as Codespaces conformance.

## **14.4 Shared invariants (apply to every Defined/supported Codespaces QA profile)**

### **14.4.1 Determinism env pins for governed bytes**

Any job that produces governed snapshots or evidence MUST export:

* `LC_ALL=C`  
    
* `LANG=C`  
    
* `TZ=UTC`

Canonical set only (normative): the pins above are the only determinism env pins required by PF19 for Live QA conformance. Live QA plans MUST NOT introduce additional required pins (for example PYTHONHASHSEED or any `MODO_*` variable) as rails, prerequisites, or approval gates.

Determinism posture (normative): if any governed bytes are nondeterministic, determinism MUST be achieved in the producing tool via explicit ordering (stable sorts, deterministic serialization), not via interpreter/environment knobs. Treat nondeterminism as a repo/tooling defect to drain via canon.

### **14.4.2 QA root and write-scope rails**

Codespaces is a QA console and artifact sink. It MUST NOT be treated as prod.

The canonical Live QA evidence root is `audit/qa/<epic-id>/`, with a lowercase `<epic-id>`. Check evidence belongs under `audit/qa/<epic-id>/checks/<check_id>/`; stable epic metadata belongs under `audit/qa/<epic-id>/00_meta/`; the current-state manifest remains `audit/qa/<epic-id>/qa_step_logs_manifest.json`.

Ordinary Live QA evidence MUST remain under the canonical epic QA root and its PF12-Canon-HDE-Schemas-and-Artifacts-authorized children. The standard external-path exception is the draft/staging Doc Delta at `audit/docdeltas/<epic-id>_doc_deltas.md`; its stable QA counterpart is `audit/qa/<epic-id>/00_meta/doc_deltas.md`.

A separately authorized `QA_PLAN_UPDATE`, `DOC_UPDATE`, PR, or Ops route may create or refresh governed evidence outside the QA root only under its owning canon and approved work item. That routed output is not a generic QA-subpath exception, and the final QA receipt MUST identify the route before relying on it.

### **14.4.3 Step-0 “Codespaces snapshot” (optional; non-gating evidence)**

A Codespaces snapshot artifact may be useful for debugging and reviewer context, but it is not a required Live QA deliverable.

Non-gating rule (normative) is as follows:

* Plans MUST NOT require, validate, or gate approval on a Codespaces snapshot artifact.  
* Reviewers MUST NOT use the presence, absence, or contents of a snapshot to decide PASS vs REMEDIATION.

If produced, the snapshot MUST use the current-state path `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json` and conform to the complete canonical JSON, schema, capture, and indexing contract in PF12-Canon-HDE-Schemas-and-Artifacts under `8.17.5 Codespaces snapshot (Step-0; current-state) [Optional]`. It records effective rails and deterministic pins, tool versions, and presence-only required environment or secret names without values. Static configuration does not prove that the Codespace launched, a service ran, a secret exists, or a QA predicate passed.

The optional snapshot is separate from, and MUST NOT replace, the per-check `primary.log`, required path proofs, current-state manifest, Human Evidence Index, Machine Mirror, exact check proof, or Step-0 Doc Delta Capture outputs.

## **14.5 Environment profiles (Codespaces config \+ minimum checks)**

A profile is usable for Codespaces-based QA only when it is marked `Defined/supported` and every required fact is owner-authorized and populated. Optional facts may be omitted when not applicable.

### **14.5.1 HD Engine — Codespaces QA environment**

Profile status: `Defined/supported`.

#### **Purpose and boundaries**

* The profile supports a QA console into the PF07-Canon-Glow-Infrastructure-defined Railway production targets for expressly approved Live QA steps.  
* The profile supports a local dev-harness runner for closed-rails deterministic checks.  
* Codespaces is a client/console and artifact workspace. It is not production.  
* Codespaces is canonical and preferred for shared HDE QA, but it is not automatically material to every proof and is not mandatory when the owning plan authorizes an equivalent complete environment contract.

#### **Primary repository and workspace**

* Repo name: `amthorn78/glow-hdengine-v2`  
* Default branch: `main`  
* Current devcontainer name: `Glow HD Engine Codespace`  
* Codespace naming convention: not defined; this optional field is omitted.

#### **Toolchain and entrypoints**

* CLI entrypoints: `hdctl`; `python -m engine.cli`  
* Test runner: `pytest`  
* Devcontainer image: `mcr.microsoft.com/devcontainers/python:3.11`  
* Runtime posture: Python 3.11 in the current devcontainer; project floor Python `>=3.10`.  
* Node is not a required HDE profile runtime merely because a generic snapshot schema can report a Node version when applicable.

#### **Runtime targets**

* Railway project: `ample-illumination`  
* HD Engine service: `glow-hdengine-v2`  
* Production base URL: `https://glow-hdengine-v2-production.up.railway.app`  
* Production database instance: `ample-illumination/production/postgres`  
* HD Engine database schema: `hde`  
* Local configured dev-sampler endpoint: `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`  
* Local port when that dev sampler is used: `8000`

Listing a target does not authorize access, prove reachability, prove secret presence, or establish runtime success. The plan selects only the target needed by the check.

#### **Rails, environment, and secrets**

* Default rails posture: closed rails.  
* Closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
* Allowed rails-toggle names: `SAFE_MODE` and `ALLOW_NETWORK`.  
* Open rails: `SAFE_MODE=0` and `ALLOW_NETWORK=1`, only for an expressly approved step whose owner, target, authorization, secret-safety, evidence, and rollback boundaries are defined. Privileged or external-system mutation remains PO-authorized Ops work; execution follows PF06-Canon-Epic-Process-Guide, including its explicit-delegation controls.  
* `APP_ENV` is propagated exactly when a check requires it. Infra helpers MUST NOT silently default an empty or unset value. Local/dev HDE checks that require the dev-gated surface use the owner-defined `APP_ENV=dev` posture.  
* Required secret names for the base closed-rails profile: none.  
* Check-specific secret names: the applicable plan lists the exact owner-defined names. Current known names such as `DATABASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` are required only when the selected check uses their target; they are not universal profile prerequisites.  
* Secret values MUST NOT appear in PF19, snapshots, primary logs, manifests, Doc Deltas, or other governed evidence. Use presence-only, redacted, or approved hashed posture.

#### **Minimum bootstrap and readiness checks**

Before a newly created or materially changed HDE Codespace is treated as ready for a selected QA check:

1. `.devcontainer/scripts/post-create.sh` completes successfully.  
2. The virtual environment and repository dependencies install successfully from `requirements.txt`, `requirements-dev.txt`, and editable project installation.  
3. `.venv/bin/python -m pytest --version` exits successfully.  
4. `.venv/bin/python -m engine.cli --help` exits successfully.  
5. The effective deterministic pins are captured and equal `LC_ALL=C`, `LANG=C`, and `TZ=UTC` for governed-byte production.  
6. If the check uses the local dev sampler, capture the exact `DEV_SAMPLER_URL` binding and perform the plan-defined service/up check. The static devcontainer value does not prove that a service is running.  
7. If the check reaches Railway, a database, or a vendor, execute the plan-defined Step-0 handshake or prerequisite proof under the approved rails. Static PF07-Canon-Glow-Infrastructure inventory does not prove reachability or authorization.

Failure of a mandatory prerequisite is `TOOLING_BLOCKED` unless attempted tooling itself is defective, in which case the applicable PF27-Canon-Plan-Templates failure classification controls.

#### **Evidence sinks and environment records**

* QA root: `audit/qa/<epic-id>/`  
* Per-check directory: `audit/qa/<epic-id>/checks/<check_id>/`  
* Per-check receipt and environment/rails record: `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
* Required receipt proof: `audit/qa/<epic-id>/checks/<check_id>/primary.log.path_proof.txt`  
* Current-state manifest: `audit/qa/<epic-id>/qa_step_logs_manifest.json`  
* Required manifest proof: `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`  
* Optional non-gating Codespaces snapshot: `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`  
* Draft/staging Doc Delta: `audit/docdeltas/<epic-id>_doc_deltas.md`  
* Stable epic Doc Delta record: `audit/qa/<epic-id>/00_meta/doc_deltas.md`

The two Doc Delta files are byte-identical where PF12-Canon-HDE-Schemas-and-Artifacts requires the QA-root copy. The optional Codespaces snapshot does not replace the receipt, manifest, path proofs, Human Evidence Index, Machine Mirror, or exact selected-check proof.

#### **Ownership**

* Responsible for environment wiring and profile currency: `Infra / Ops owner`  
* Responsible for HDE CLI, test, and playbook content consumed by the profile: `HDE Lead / Engine owner`  
* Accountable reviewer: `Lead Developer`  
* The Product Owner retains authorization, accountability, and acceptance for privileged Ops actions. Any delegated execution follows PF06-Canon-Epic-Process-Guide.

### **14.5.2 App Back End — Codespaces QA environment**

Profile status: `Unsupported/undefined`.

PF19 recognizes the App Back End QA environment class but does not define a conforming Codespaces profile. The missing required fact classes are:

* App Back End Codespaces purpose and supported QA uses  
* owner-authorized repository name and default branch  
* default rails posture  
* required secret names, names-only  
* closed-rails bootstrap checks  
* responsible owner and accountable reviewer

If local runtime or HDE integration is required, its start command, base URL, ports, integration boundary, and up-check evidence must also be owner-authorized before use. HDE contracts remain owned by the HDE-titled PF documents. A materially dependent check is `TOOLING_BLOCKED` until the complete profile is canonized. Evidence uses the canonical root and check grammar in §14.4.2 only after that gate is met.

### **14.5.3 App Front End — Web — Codespaces QA environment**

Profile status: `Unsupported/undefined`.

PF19 recognizes the App Front End — Web QA environment class but does not define a conforming Codespaces profile. The missing required fact classes are:

* FE-Web Codespaces purpose and supported QA uses  
* owner-authorized repository name and default branch  
* package manager and test runners  
* default rails posture  
* required secret names, names-only  
* build and test bootstrap checks  
* responsible owner and accountable reviewer

No start command, local base URL, port, package-manager choice, test-runner choice, rails value, secret, or bootstrap command may be inferred. A materially dependent check is `TOOLING_BLOCKED` until the complete profile is canonized. Evidence uses the canonical root and check grammar in §14.4.2 only after that gate is met.

### **14.5.4 App Front End — Mobile — Codespaces QA environment**

Profile status: `Unsupported/undefined`.

PF19 recognizes the App Front End — Mobile QA environment class but does not define a conforming Codespaces profile or an alternate mobile QA console. The missing required fact classes are:

* Mobile Codespaces purpose and supported QA uses  
* whether Codespaces supports the required mobile runtime surfaces  
* owner-authorized repository name and default branch  
* required alternate QA console by title when Codespaces cannot support the needed runtime  
* build system or tooling and test runners  
* default rails posture  
* required secret names, names-only  
* bootstrap checks  
* responsible owner and accountable reviewer

No mobile runtime-support claim, alternate environment, repository, branch, build tool, test runner, rails value, secret, or bootstrap command may be inferred from HDE repository state. A materially dependent check is `TOOLING_BLOCKED` until the Codespaces profile or a complete owner-authorized alternate environment contract is canonized. An alternate environment must not be represented as Codespaces conformance.

## **14.6 Ownership and maintenance**

Profile ownership and future-definition gates are as follows:

| Profile | Responsible owner | Accountable reviewer | Definition gate |
| :---- | :---- | :---- | :---- |
| HD Engine | `Infra / Ops owner` for environment wiring and `HDE Lead / Engine owner` for HDE CLI, tests, and playbooks | `Lead Developer` | Keep every defined field current and update this profile in the same change-set as a changed prerequisite. |
| App Back End | `BE Lead / App Backend owner`, with Infra/Ops for environment wiring | `Lead Developer` | Complete every required §14.5.2 fact from the owning App repository and infrastructure canon in one coordinated change. |
| App Front End — Web | `FE Lead / App Frontend owner`, with Infra/Ops for environment wiring | `Lead Developer` | Complete every required §14.5.3 fact from the owning App repository and infrastructure canon in one coordinated change. |
| App Front End — Mobile | `Mobile/App Frontend owner`, with Infra/Ops for environment wiring | `Lead Developer` | Establish whether Codespaces supports the required mobile surfaces and, if not, canonize the alternate QA console before completing §14.5.4. |
| Update trigger(s) include: |  |  |  |

* repo/toolchain change that affects QA steps  
    
* Codespaces base image change  
    
* secrets or env-var interface changes (names-only)  
    
* devcontainer changes that affect shells, entrypoints, or tooling availability

Same change-set rule (normative) is as follows: any change to Codespaces/devcontainer requirements, required env var names, required secret names, or other Live QA prerequisites MUST be reflected in this section (and the relevant profile in §14.5) in the same change-set that introduces the new requirement. Plan-only prerequisites and tribal knowledge are non-conforming.

Doc delta capture step (normative, planning allowed) is as follows: Live QA planning is allowed even when Codespaces prerequisites are incomplete or unclear, but plans MUST NOT assume or invent missing details.

Routing (normative) is as follows: mandatory Step-0 artifacts (including Doc Delta Capture posture) are governed by PF27 — Plan Templates. This section adds Codespaces-specific requirements for how doc deltas are recorded.

Every Live QA plan executed in Codespaces MUST include a Step-0 Doc Delta Capture step that:

* lists each missing or ambiguous prerequisite discovered during planning, separated into:  
    
  * BLOCKERS (execution cannot proceed without resolution)  
      
  * CAVEATS (execution can proceed with constrained scope or reduced confidence)


* names the intended fix location for each item (either §14.5 profile fields, or an owning PF doc by title only)  
    
* records a resolution status for each item (for example unresolved, resolved by doc update, resolved by existing canonical reference)

The Doc Delta Capture step MUST produce two artifacts: `audit/docdeltas/<epic-id>_doc_deltas.md` (canonical doc-delta ledger record) and `audit/qa/<epic-id>/00_meta/doc_deltas.md` (in-epic QA copy). The two files MUST be byte-identical. Both artifacts MUST be names-only (no secret values). If no deltas are found, the step MUST still produce an explicit no deltas output.

Step-0 Doc Delta Capture must preserve existing proof-bearing doc-delta surfaces.

If generator-owned, PR-owned, OPS-owned, QA-owned, or previously produced doc-delta surfaces already exist for the same epic, Step-0B MUST NOT overwrite them with a generic no-deltas template. Step-0B may verify them, copy them when explicitly required, append a clearly labeled capture section when the owning plan permits it, or produce its own additional record. It must not silently erase proof-bearing content.

A no-deltas output is valid only when the run has inspected the relevant approved surfaces and no proof-bearing doc-delta surface exists or no delta is actually present. If a Step-0B command overwrites a proof-bearing doc-delta surface, classify the result as an evidence-assembly or tooling failure until remediated. Remediation must preserve the original failed evidence, identify the overwritten path or paths, restore or reconstruct only from authoritative current sources, and rerun the affected check or accepted validation path.

Conformance rule (normative) is as follows: a Live QA run executed in Codespaces is non-conforming for approval if either of the following is true:

* the relevant environment profile is `Unsupported/undefined`, retains missing or contradictory required facts, and the check materially depends on that profile; or  
* the plan did not include, and the run did not produce, the required Step-0 Doc Delta Capture output defined above.

A check that materially depends on an unresolved profile prerequisite is `TOOLING_BLOCKED` until owner-authorized canonical documentation resolves the prerequisite. Missing or contradictory prerequisites MUST be captured as Doc Deltas during planning. Environment details for a Defined/supported profile MUST be kept current so QA plans do not rely on guessing.

