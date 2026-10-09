# PF04 redlines from v2.8.6

Run identity: T-PF04-20261009-01; preparation revision 1. Originating preparer: the executing document agent in Nathan's current T-PF04 Work conversation; no platform conversation ID is exposed or inferred.

Target: `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md` in `amthorn78/glow-hdengine-v2` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`. Original SHA-256 (native UTF-8 Git blob bytes): `e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696`. Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md`, row `T-PF04`, pinned at `f057d124176143b3e02ba7ad599880fd7e9991b1`. Source selection and complete coverage are recorded in the companion proof log.

Preparation: validated content batch; the companion proof log supplies the actual save/readback outcome. Header version, effective date and Last Update Gate are reserved for TW-APPLY-10. Apply derives v2.8.7 and 2026-10-09, with `BN 13.5` as the sole change-source gate; the Specification and closure record supply bounded support, not new generic rules.

Each location is an exact original heading path. Scope is the last heading's complete original section, including children, ending before the next same-or-higher-level heading. Headings in fences are excluded. Expected literal occurrence is one in that scope. The single LF immediately before each closing payload fence is framing: remove exactly that framing LF; every earlier LF and literal escape is payload. No operation rematches mutated text.

## RL-001 — REPLACE

**Original heading path:**

````
# **0 Document Control \[Required-Now\]**
## **0.2 Scope & boundaries \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**PF10-HDE-Build-Notes reference posture (stable unit: addendum entry).**

* Do not reference **PF10-HDE-Build-Notes** by version strings.  
* Prefer referencing **PF10-HDE-Build-Notes** by addendum number \+ addendum title (for example: “PF10-HDE-Build-Notes Addendum 2.10 — Token Load Reduction \[OMITTED: remaining title\]”).  
* Do not treat **PF10-HDE-Build-Notes** section numbers as durable anchors for external enforcement; the stable unit is the addendum entry itself.  
* When an addendum supersedes earlier **PF10-HDE-Build-Notes** guidance, it must explicitly name what it supersedes (by addendum number/title).  
* Legacy note: this document may contain legacy PF10-style labels (for example “PF10-A” / “PF10-AA”) inside headings or notes. Treat them as legacy identifiers only. Do not introduce new PF10-style labels. Replace them with addendum-number references when the correct mapping is known.


````

**NEW (literal):**

````
**HDE Build Notes reference posture (titles only).**

* This document names **HDE Build Notes** by title only. It does not cite an addendum number, section, heading, paragraph, version or other internal locator.
* **HDE Build Notes** is the canonical override and amendment mechanism. An applicable addendum governs conflicting earlier canon only within its scope.
* When an older PF passage supplies an addendum-number citation, search the current **HDE Build Notes** by subject and read the applicable addendum in full; do not resolve the old number against a different version.
* Dated historical records and provenance retain their original wording. Legacy PF10-style provenance identifiers are not current lookup instructions.


````

## RL-002 — REPLACE

**Original heading path:**

````
# **0 Document Control \[Required-Now\]**
## **0.4 Change policy**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Repository-native evidence artifacts whose owning contract requires governed publication MUST live under governed repo paths and retain the applicable Evidence Index/Mirror and proof bindings. “Single-home” refers to the authoritative binding between artifact keys and repo paths, not one directory. Off-repository change-process artifacts, reports and exports use §9.1.3 Library storage; that rule does not relocate repository-controlled evidence or replace its canonical writers.
````

**NEW (literal):**

````
Repository-native evidence artifacts whose owning contract requires governed publication MUST live under governed repo paths and retain the applicable Evidence Index/Mirror and proof bindings. “Single-home” refers to the authoritative binding between artifact keys and repo paths, not one directory. Change-process artifacts, reports and exports use repository storage under `docs/ephemeral/` as specified in §9.1.3; that rule does not relocate repository-controlled evidence or replace its canonical writers.
````

## RL-003 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
A repository-controlled canonical artifact on `main` governs only its declared artifact-content lane. Repository PF copies remain publication mirrors of the Drive authority and are usable as bounded QA/Ops execution sources under §9.1.4; repository presence does not confer independent PF editing authority. Artifact authority remains separate from implementation conformance, repository validation, QA acceptance and closure.
````

**NEW (literal):**

````
A repository-controlled canonical artifact on `main` governs only its declared artifact-content lane. Current PF documents in `docs/pfcanon/` on `main` are the PF authority for planning, governance authoring, review, QA readiness, task preparation, QA and operations execution. Repository presence does not confer independent PF editing authority. Artifact authority remains separate from implementation conformance, repository validation, QA acceptance and closure.
````

## RL-004 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
### **2.0.6 Evidence & indexing**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**Clarifications (evidence integrity; BN 8.5.3 Drain A19-22).**
````

**NEW (literal):**

````
**Clarifications (evidence integrity).**
````

## RL-005 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
### **2.0.10 Env / rails / infra**
````

**Expected occurrence:** 1

**OLD (literal):**

````
  * **Prod posture.** Production acceptance must **not** depend on rails-open settings; public Reader/Aux behavior and acceptance proofs assume closed rails for vendor HTTP. Admin-guarded vendor override windows are governed separately (§3.1) and must not weaken the public covenant.  
````

**NEW (literal):**

````
  * **Prod posture.** Public Reader/Aux behavior and their vendor-refusal proofs assume closed rails for vendor HTTP. That boundary does not replace the mandatory synthetic-data live vendor test in every QA plan touching a surface used to produce a production feature described as functional in PF canon (§3.4). Admin-guarded vendor override windows remain separately governed (§3.1) and must not weaken the public covenant.
````

## RL-006 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
### **2.0.11 Catalog hygiene (where applicable)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **RESONANCE\_PUBLIC\_POSTURE\_OK** — Reader v1 and CLI **public** surfaces obey the **numeric-free, narrative-free public covenant**: success payloads expose exactly six top-level keys (`reader_version, eligible, categories, meta, release_id, idempotence_hash`); `categories[*]` items are exactly `{ "id", "band" }` with `band ∈ {"Cool","Open","Warm","Glow"}`; no SR/XR or other numerics appear in public bodies; typed error envelopes are numeric-free (except optional `retry_after_ms` under governed vendor-rate-limit policy); and no prompts or narratives are emitted on **public** Reader/CLI surfaces. This token covers CLI output only when the CLI is emitting the **Reader v1 success envelope** (for example, via `--dump-reader` sidecars). This token does **not** govern `hdctl showcompat` stdout (the compatibility payload), which may include numeric scores/weights. This token also does **not** govern admin-only surfaces such as the admin bundle; those surfaces may include numeric scores and narrative text but must remain non-public and are covered by the admin-surface tokens in §2.0.17 and the logging/security rules in §7–§8. (Owned: Governance; HDE-Math-Spec; HDE-Schemas & Artifacts; Glow QA Guide)  
````

**NEW (literal):**

````
* **RESONANCE\_PUBLIC\_POSTURE\_OK** — Reader v1 and CLI **public** surfaces obey the **numeric-free, narrative-free public covenant**: success payloads expose exactly six top-level keys (`reader_version, eligible, categories, meta, release_id, idempotence_hash`); `categories[*]` items are exactly `{ "id", "band" }` with `band ∈ {"Cool","Open","Warm","Glow"}`; no SR/XR or other numerics appear in public bodies; Reader v1 and v2 errors use the closed, numeric-free four-key `error_v1` envelope (`schema`, `ok`, `code`, `error`), with `schema:"v1"`, `ok:false`, and no optional fields; and no prompts or narratives are emitted on **public** Reader/CLI surfaces. This token covers CLI output only when the CLI is emitting the **Reader v1 success envelope** (for example, via `--dump-reader` sidecars). This token does **not** govern `hdctl showcompat` stdout (the compatibility payload), which may include numeric scores/weights. This token also does **not** govern admin-only surfaces such as the admin bundle; those surfaces may include numeric scores and narrative text but must remain non-public and are covered by the admin-surface tokens in §2.0.17 and the logging/security rules in §7–§8. (Owned: Governance; HDE-Math-Spec; HDE-Schemas & Artifacts; Glow QA Guide)  
````

## RL-007 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
### **2.0.11 Catalog hygiene (where applicable)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **MAGIC10\_DOMAIN\_CLOSED\_OK** — The internal Magic-10 result domain is the closed ten-ID set in the frozen order: every eligible pair evaluation produces exactly one intrinsic score and band for each canonical category, with no extras, omissions, duplicates, defaults, or harmony-only substitution. Reader v1 is a numeric-free public projection of that complete internal matrix: when `eligible == true`, `categories` contains exactly one `{"id":"harmony","band":"Cool"|"Open"|"Warm"|"Glow"}` item; when `eligible == false`, it contains `[]`; it exposes neither scores nor the other nine categories. Evidence includes internal ten-ID closure and ordering checks, public harmony-only schema and validation checks, and fixtures that reject unknown, extra, missing, duplicate, or nonconforming IDs. (Owned: HDE-Math-Spec; Governance; Glow QA Guide; Evidence & Artifacts)
````

**NEW (literal):**

````
* **MAGIC10\_DOMAIN\_CLOSED\_OK** — The internal Magic-10 result domain is the closed ten-ID set in the frozen order: every eligible pair evaluation produces exactly one intrinsic score and band for each canonical category, with no extras, omissions, duplicates, defaults, or harmony-only substitution. Reader v1 is a numeric-free public projection of that complete internal matrix: when `eligible == true`, `categories` contains exactly one `{"id":"harmony","band":"Cool"|"Open"|"Warm"|"Glow"}` item; when `eligible == false`, it contains `[]`; it exposes neither scores nor the other nine categories. Reader v2 projects all ten bands in the governed category order and exposes no scores (§8.1). Evidence includes internal ten-ID closure and ordering checks, public harmony-only schema and validation checks, and fixtures that reject unknown, extra, missing, duplicate, or nonconforming IDs. (Owned: HDE-Math-Spec; Governance; Glow QA Guide; Evidence & Artifacts)
````

## RL-008 — REPLACE

**Original heading path:**

````
# **3\) Rails & Environments (Vendor posture) \[Required-Now\]**
## **3.3 Secrets & env validation \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Validate against canonical env and infrastructure homes (names-only allow-list).** Before any vendor action, validate required environment keys from the canonical env and infrastructure homes (names only; secrets not printed). `ALLOW_NETWORK`, `SAFE_MODE`, and `APP_ENV` are rails-governance keys. `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` are infrastructure/vendor configuration keys, not acceptance tokens. `HDAPI_BASE_URL` is deprecated compatibility spelling only where implementation or migration evidence explicitly records it. If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` are present with different values, fail closed with configuration ambiguity before network I/O. Unknown keys **must** be flagged in CI; missing required keys **must** fail at prod start.  
  **Required (examples):** `HD_API_BASE_URL` (vendor base URL), `HD_API_KEY` (secret), `GEO_API_KEY` (secret).  
  **Failure posture:** if rails are **open** but any required key is invalid/missing, the provider **MUST refuse** with a typed error; **do not** attempt partial requests or fallbacks.  
````

**NEW (literal):**

````
* **Validate environment configuration (presence only).** Before any vendor action, validate required environment keys by name without exposing values. `ALLOW_NETWORK`, `SAFE_MODE`, and `APP_ENV` are rails-governance keys. A vendor call requires two API keys, `HD_API_KEY` and `GEO_API_KEY`, plus the base URL from `HD_API_BASE_URL`; the base URL is configuration, not an API key. Use `HDAPI_BASE_URL` only as a compatibility alias when `HD_API_BASE_URL` is absent. If both base-URL variables hold different values, fail closed before network I/O. Use the execution environment's configuration; do not require the Product Owner to type, paste or re-enter values, and do not remove the environment's only base URL merely because rails change. Record `SET` or `UNSET` only. Passing the environment to the product process does not expose a plaintext secret; keep values off argument lists, chat, logs and committed evidence, and scan captured output before it enters evidence. If a required variable is missing, no vendor call runs; record the missing names by presence only and classify a begun step as `TOOLING_BLOCKED`. Manual secret entry is not a substitute. An environment template or infrastructure inventory does not prove the variables are present in the actual execution environment. Missing required keys must also fail at production start; unknown keys must be flagged in CI.
````

## RL-009 — REPLACE

**Original heading path:**

````
# **3\) Rails & Environments (Vendor posture) \[Required-Now\]**
## **3.4 Open rails (controlled) \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**Production-affecting epic live-proof requirement.** For any epic that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence or retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret-binding behavior, request shaping, response mapping, authentication or authorization, production-used CLI/API behavior, queues, workers, jobs, schedulers, runtime services, or any path that must work outside isolated closed-rails fixtures, the Live QA Plan MUST include at least one bounded open-rails live QA step before acceptance unless an explicit approved exemption is recorded.

Closed-rails tests, repo tests, static analysis, generated evidence artifacts, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repository inspection, Codex audit, implementation review approval, QA Plan approval, PF10 supportability notes, a written smoke procedure, or OPS discovery without live behavior proof may support the QA package, but they do not replace the required open-rails live QA step for production-affecting work.

The required live step must prove at least one real production-relevant behavior the epic could affect. It must be bounded, non-destructive unless explicitly approved, PO-authorized where secrets, external services, or deployed environments are involved, secret-safe, evidence-recorded, scoped to the actual production risk, clear about what it proves, and clear about what it does not prove.

Open-rails live QA proves only what it exercises. It does not mint new acceptance tokens, satisfy unrelated tokens, prove full vendor conformance, move unrelated PF09 rows to Done, complete epic closeout, change public Reader scope, authorize new routes, or complete PF-canon drainage by itself.

For this requirement, user or production surfaces include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor transport, vendor route policy, vendor request shaping, vendor response handling, HumanDesignAPI auth/header behavior, BodyGraph vendor ingest, vendor response normalization, vendor error/retry/rate-limit behavior, configured base URL behavior, environment-key binding behavior, database persistence or retrieval, runtime compute, deployed service behavior, and admin or ops-facing behavior that can affect production truth.

QA readiness, Live QA Plan approval, QA review, and closeout review MUST account for the required open-rails step. A Live QA Plan, QA-readiness review, or closeout-review posture is substantively blocked when the epic affects user or production surfaces, no bounded open-rails QA step is included, and no controlling PO-authorized or PF-canon exemption is recorded. The blocker language should state that open-rails QA is required because the epic affects user or production surfaces and closed-rails-only QA is insufficient, then identify the affected surface.

The open-rails requirement is not satisfied by closed-rails tests, unit tests, static validation, schema validation, evidence-index validation, Machine Mirror validation, path-proof validation, command syntax validation, dry-run-only closed-rails proof, fixture-only proof, mock-only proof, repo inspection, prior epic evidence not explicitly bound to the current epic’s open-rails proof need, OPS observation not bound into QA evidence, or a statement that open-rails QA is unnecessary without a recorded controlling exemption.

A valid exemption must be explicit. It must state why no open-rails behavior can be safely or meaningfully exercised, what risk is accepted, what proof substitutes for open-rails QA, why the substitute is sufficient for the epic, and what future work must still perform open-rails proof if any. Silence, reviewer preference, convenience, or closed-rails success is not an exemption.


````

**NEW (literal):**

````
**Production-functional epic live-proof requirement.** Every QA plan for an epic touching any surface used to produce a production feature that PF canon describes as functional MUST include an open-rails test. The test MUST make a live vendor call under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, using synthetic data only, with no real person, user or production data. Identification of the affected surfaces remains with the epic's Specification and plans. A plan without this test is not approval-ready.

Closed-rails tests, fixture replay, mocks or fake services, static analysis, generated or governed evidence artifacts, path-proof validation, Index or Mirror refresh, repository inspection, review approval, an unrun smoke procedure, and OPS discovery without a live vendor call do not satisfy this requirement. A non-vendor deployed-service check or database read does not satisfy it by itself. An exemption or closed-rails-only approval does not replace the required test within this scope. Any question about retaining an exemption ground remains for Product Owner determination; it is not permission to omit the test.

The live vendor step retains task-specific Product Owner authorization where secrets or external services are involved, a defined request limit, explicit step-local rails, synthetic inputs, redaction, secret scanning and quarantine, trustworthy evidence, stop checks and failure classification before any product-failure conclusion. It authorizes no load, stress or volume testing and raises no request limit. Open-rails Ops evidence remains Ops evidence; including or referencing it does not convert it into QA evidence.

A passing test proves only the behavior it exercises. It does not establish full vendor conformance, whole-change QA PASS, acceptance, PF09 movement, deployment, release activation, epic closure, public Reader behavior changes, new routes or flags, or PF-canon drainage.

**Other production-affecting scope.** Outside the mandatory production-functional scope above, the standing broader requirement remains: an epic that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence or retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret binding, request shaping, response mapping, authentication or authorization, production-used CLI/API behavior, queues, workers, jobs, schedulers, runtime services or another path that must work outside isolated fixtures requires at least one bounded open-rails live QA step before acceptance unless an explicit approved exemption is recorded. The step proves a real production-relevant behavior the epic can affect, retains the existing authorization and evidence controls, and is clear about its limits. Closed-rails-only QA is not approval-ready for that broader scope without the explicit exemption. A valid exemption states why no open-rails behavior can be safely or meaningfully exercised, the authorizing owner, accepted risk, substitute proof and why it is sufficient, the production claim withheld and any future live-proof obligation. Silence, reviewer preference, convenience or closed-rails success is not an exemption. This retained broader rule supplies no exemption from the mandatory synthetic-data live vendor test for production-functional surfaces.


````

## RL-010 — REPLACE

**Original heading path:**

````
# **3\) Rails & Environments (Vendor posture) \[Required-Now\]**
## **3.4 Open rails (controlled) \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
A Live QA Plan for a production-affecting epic is not approval-ready if it is closed-rails-only unless it records an explicit exemption. The exemption must state why open-rails live QA is omitted, who authorized the omission, what production claim is not being made, and whether a later open-rails QA step is required before closeout or release. This is a truth and proof requirement, not a formatting preference.
````

**NEW (literal):**

````
For the production-functional scope above, QA readiness, plan approval, QA review and closeout review must account for the mandatory live vendor test. Name the affected surface and the actual missing or unexecuted proof; closed-rails success and exemption language cannot make a plan without the required test approval-ready.
````

## RL-011 — REPLACE

**Original heading path:**

````
# **3\) Rails & Environments (Vendor posture) \[Required-Now\]**
## **3.4 Open rails (controlled) \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
A controlled vendor-backed no-user smoke MAY run only when explicitly approved for that slice and only after the required command discovery and remediation prerequisites are satisfied. It MUST be PO-only, IA-guided, limited to the explicit open-rails vendor step, and secret-free in persisted evidence. It MUST use no app user IDs, no caller-provided `person_uid`, no guessed command, no guessed host or port, no guessed URL, no guessed service binding, no guessed target, no guessed environment fact, and no unresolved placeholder-bearing command.
````

**NEW (literal):**

````
A controlled vendor-backed no-user smoke MAY run only when explicitly approved for that slice and only after the required command discovery and remediation prerequisites are satisfied. The Product Owner is the authorizing and accountable principal. When directed for the identified task, an automated session agent executes the live vendor call as executor and evidence producer, using environment-held configuration under §3.3. The smoke MUST be IA-guided, limited to the explicit open-rails vendor step, and secret-free in persisted evidence. It MUST use no app user IDs, no caller-provided `person_uid`, no guessed command, no guessed host or port, no guessed URL, no guessed service binding, no guessed target, no guessed environment fact, and no unresolved placeholder-bearing command. This creates no standing authority for an undirected vendor call and grants no AI-provider-call authority.
````

## RL-012 — REPLACE

**Original heading path:**

````
# **8\. Security & Privacy \[Required-Now\]**
## **8.1 Numeric-free public covenant \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
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
* **Resonance posture (public).** Public payloads **MUST NOT** expose SR/XR numerics. v1 ships **SR-only** (`alpha=1.0`); **hysteresis \\= 1** is armed for future XR and **not exposed**.

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


````

**NEW (literal):**

````
## **8.1 Numeric-free public covenant \[Required-Now\]**

**Principle (normative).** All public-facing **Reader v1 and v2** responses are **numeric-free** and **narrative-free**. Public payloads disclose **only** categorical results in the shape `{ "id", "band" }`. **No** scores, percentages, prompt text, or other numerics may appear on the public surface.

The product/payload-numeric-free definition for the internal audit-log families in §§7.3 and 7.4 does not alter this literal public covenant.

**Docs/review restatement for adjacent-surface changes.** When a plan, PR summary, docs sweep, review artifact, or closeout artifact changes or reviews adjacent narrative, DB, compat, admin, vendor, router, or internal evidence surfaces while the applicable Reader public contract remains unchanged, the artifact MUST state that boundary explicitly. The statement MUST distinguish adjacent internal, admin, compat, evidence, or deferred-vendor work from any public Reader contract change and MUST NOT imply public Reader enablement, public payload drift, HDAPI v2 conformance, or a new public surface unless that change is explicitly in scope and governed by the relevant contract update.

### **8.1.1 Scope**

* **Applies to:** all public responses from the Reader v1 and v2 surfaces (**HTTP 200 success** and all **typed errors**) and all **CLI stdout** outputs intended to mirror public bytes.  
* **Does not apply to:** internal compatibility math, presets, or bench diagnostics stored as **private artifacts or logs**. These remain internal only and **redacted** in public.

### **8.1.2 Requirements**

* **Categories array (public shape & domain).**  
  * Each item in `categories[*]` **MUST** be exactly `{ "id": <string>, "band": <enum> }`.  
  * `band ∈ {"Cool","Open","Warm","Glow"}`.  
  * `id` **MUST** be a **Magic-10 identifier** from the **closed set and order** (see PF-Canon-HDE-Schemas and Artifacts §2.6 / PF-01 §5.1).  
  * **v1 exposure rule:** if `eligible == true`, the array **MUST** contain **exactly one** item, `{"id":"harmony","band":<BAND>}` (PF-01 §2.2). If `eligible == false`, the array **MUST** be `[]`.  
  * **v2 exposure rule (C040-07):** the production route `POST /api/reader` selects Reader v2 with exactly one `v=2`. The success body's `reader_version` is the fixed string `"v2"`. An eligible pair MUST expose exactly ten items, one per canonical category in this governed order: `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. Each band comes from that category in the complete canonical intrinsic Magic-10 result. No omission, duplication, default fill, harmony-only substitution or viewer-preference mutation is allowed. The array is ordered; do not dedupe or ASCII-sort it as a set. An ineligible pair MUST expose `[]`.
  * **Version and route boundary:** production Reader v1 remains selected by `v=1` on `POST /api/reader`; dev `GET /reader` remains v1. Missing, unsupported, duplicated or malformed version selection is refused under the PF05-owned contract. Reader v2 inherits the v1 request contract, read-only resolution, eligibility decision, transport, conditional and error behavior. It adds no request-time vendor call, write, second presenter or second calculator.
  * **No numeric fields** are permitted (e.g., `score`, `score_pct`, `index`, `rank`).  
* **Top-level structure (success).** The success body contains **exactly six keys**:  
  `reader_version, eligible, categories, meta, release_id, idempotence_hash`.  
  No additional top-level fields may be introduced without a **versioned Reader contract** update.  
* **Typed errors (numeric-free).**  
  * Reader v1 and v2 use exactly the four-key `error_v1` envelope: `schema`, `ok`, `code`, `error`. `schema` is the fixed string `"v1"` even for Reader v2; `ok` is `false`; `code` and `error` are the governed token/message pair. No `retry_after_ms`, `details` or other extra field is permitted.  
  * Errors are numeric-free, secret-safe and non-echoing. Exact tokens, messages and bytes remain owned by **PF-Canon-HDE-CLI-API-Vendor-Ref**; this drainage adds no error taxonomy or emitted-byte change.  
* **Narratives and prompts.** Public payloads **MUST NOT** include prompt text, narratives, or user-facing messages generated by internal modules. These are **retired**.  
* **Resonance posture (public).** Public payloads **MUST NOT** expose SR/XR numerics. v1 ships **SR-only** (`alpha=1.0`); **hysteresis \\= 1** is armed for future XR and **not exposed**.

### **8.1.3 Validation (binary)**

* **Schema gate.** Verify success has **exactly six keys** and that `categories[*]` items are **only** `{id, band}`.  
* **Versioned category check.** Eligible v1 has one `harmony` item; eligible v2 has the exact ten IDs in governed order with each intrinsic band; both ineligible versions have `[]`. Reject missing, extra, duplicate, default-filled, reordered or substituted v2 items.  
* **Numeric-free grep-guard.** CI blocks any numeric fields or prompt text in public payloads.  
* **Canonical JSON.** Public bytes are serialized as **UTF-8 (no BOM)**, **sorted keys**, **compact**, **exactly one trailing LF**; arrays used as sets retain their owning normalization rules (PF-12 §4); Reader v2 `categories` preserves its governed order. Canonical serialization, the five-key public preimage, AB↔BA and two-run identity apply to both versions.  
* **Parity enforcement.** Existing Reader↔CLI dump parity remains a **Reader v1** family for identical inputs and environment under `LC_ALL=C`; Reader v2 creates no CLI flag or v2 dump-parity claim. HTTP error envelopes and CLI stderr tokens keep their own contracts; for the same mapped failure, token parity compares the CLI token with `error_v1.code`, not entire-envelope bytes.

**Delivered scope and limits.** C040-07 is decided and delivered by accepted-final PR06a; C040-08 is delivered by accepted-final PR06b. At source baseline `e7265a090ad0cc8de5f36de2f19481216aa3d073`, the checked-in Reader v1 schema admits only `harmony`, excludes `prompt`, closes the six-key success branch and requires the four-key `error_v1` branch with no `retry_after_ms`. The Reader v2 schema defines the ten IDs in governed order and the same `schema:"v1"` error-envelope identity. These static schema observations do not establish fresh runtime QA, deployed-service or live current-row readiness, release activation, acceptance or closure. The legacy CLI proof failure, HTML 404 observation, packaging gap and evidence-origin label question retain their actual owners and dispositions.

### **8.1.4 Routing (titles-only)**

Math and scoring details are defined in **PF-Canon-HDE-Math-Spec**. The public emission policy **lives here** and governs the Reader and CLI surfaces. Resonance constants and pack/manifest rules live in **PF-Canon-HDE-Schemas and Artifacts**.

**Acceptance & CI (titles-only)**  
`RESONANCE_PUBLIC_POSTURE_OK`, `CLI_READER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `PREFS_KEYSET_10_OK`, `MAGIC10_DOMAIN_CLOSED_OK`


````

## RL-013 — REPLACE

**Original heading path:**

````
# **0 Document Control \[Required-Now\]**
## **0.2 Scope & boundaries \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* The public resonance posture (Reader v1 is bands-only, numeric-free; SR-only α=1.0; hysteresis=1 armed for future XR and not exposed).
````

**NEW (literal):**

````
* The public resonance posture (Reader v1 is bands-only, numeric-free; SR-only α=1.0; hysteresis=1 armed for future XR and not exposed). Reader v2 exposes the complete ordered ten-band intrinsic projection under §8.1; Reader v1 remains unchanged.
````

## RL-014 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.2 Canon precedence and persistent sources \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
### **9.1.2 Canon precedence and persistent sources \[Required-Now\]**

Apply current active PF canon, including applicable independently scoped **HDE Build Notes** addenda, before conforming live non-canon guidance and then historical reference material. A native Google Doc, Markdown peer, repository location, repetition or operational map does not itself promote a new requirement into canon. A binding requirement needs its governing authority and controlled promotion.

For a real contradiction, identify the exact current sources, versions and conflicting scope. Follow the governing PF position immediately. Correct lower-authority live material only when the edit is authorized; otherwise report the precise conflict and stop the affected work. Do not change PF canon to match non-canon guidance or silently follow both. Preserve historical original wording and label its superseded applicability rather than rewriting it as a current instruction. An unanswered policy question remains visible with its owner and affected hold.

The persistent PFCanon authority is the controlled Drive collection. Native Google Docs are the source-editing surface; their Markdown publication peers are the controlled readable publications and the exact repository-mirror input. For an authorized publication, complete native editing, generate the version-matched Markdown peer beside it, review semantic and structural fidelity, transfer the exact Markdown bytes without rewriting to the authorized repository path, and verify the resulting blob. Native document, Markdown peer and mirror carry the same PF identity, version, status and effective date. Native-document semantic correspondence is distinct from Markdown byte identity; conversion or matching filenames do not prove the latter. Synchronization records adoption, not content approval, implementation, QA or closure. Report missing peers, duplicate current pairs, identity/version/content disagreement and unknown sources as drift; do not reconcile automatically. A PF absent from every authorized repository PF path and authorized in-flight publication moves to the established Core Docs Archive through an authorized action; a repository PF absent from Drive requires an exact pinned source. Do not infer permission to delete originals, register another repository or manufacture a peer.

Planning and governance authoring use the current authorized Drive sources. The bounded execution exception in §9.1.4 permits actual operator-prepared repository PF copies for QA/Ops execution; it does not make local repository canon the unrestricted planning authority. Operational procedure and source-publication mechanics remain in their controlled operational homes.


````

**NEW (literal):**

````
### **9.1.2 Canon precedence and persistent sources \[Required-Now\]**

Apply current active PF canon, including applicable independently scoped **HDE Build Notes** addenda, before conforming live non-canon guidance and then historical reference material. A native Google Doc, Markdown peer, repository location, repetition or operational map does not itself promote a new requirement into canon. A binding requirement needs its governing authority and controlled promotion.

For a real contradiction, identify the exact current sources, versions and conflicting scope. Follow the governing PF position immediately. Correct lower-authority live material only when the edit is authorized; otherwise report the precise conflict and stop the affected work. Do not change PF canon to match non-canon guidance or silently follow both. Preserve historical original wording and label its superseded applicability rather than rewriting it as a current instruction. An unanswered policy question remains visible with its owner and affected hold.

The persistent PF authority is `docs/pfcanon/` on `main`. Each document keeps the standing it declares; the current version is the version there, and repository history retains superseded versions after they leave that directory. Native Google Docs, Markdown exports, Drive folders, Notion pages and PF-named files elsewhere in the repository confer no PF authority. Adoption does not prove content approval, implementation, QA acceptance or closure. Resolving repository canon grants no tool, credential, network, rails, mutation or privileged-action permission; agents may edit PF canon only under the Product Owner's exact authority for the identified document and action.

At the start of each task and whenever its subject changes, search `docs/pfcanon/` and the change's in-flight documents by task terms, affected surfaces, environments and headings. Read governing sections in full before planning, authoring, reviewing, deciding or asking the Product Owner. Record the actual PF titles and sections relied on and claim conformance only to material read. Ask only when canon is silent or its precedence leaves a conflict unresolved, naming the searched sections.

In-flight documents in `docs/ephemeral/` are canon for their change: the approved Specification is its permanent intended-scope authority; approved Plans are working execution direction; actual reviews and Product Owner dispositions govern within their scope. Use current versions, preserve superseded history and apply the **Plan Templates** canon-precedence rule for conflicts. No Specification write is implied by PF drainage.

The Notion development board remains operational metadata. Board Cards maintain working state; Board History, the imported snapshot and stable historical pointers preserve lineage and navigation. PF16, PF20 and PF30 pointer pages resolve the applicable current repository PF document by PF identity and versionless title. Preserve the historical-source roles `PF16 historical map`, `PF20 phased history` and `PF30 CRD history`; do not assign a source by inference to a board-level event with no card. A board value, imported snapshot, pointer or history event independently proves neither canon nor implementation, QA, acceptance or closure. A `DONE` card does not replace its governed approved Specification or actual decision lineage. Board links must not depend on version-numbered PF filenames or version-specific Drive URLs.


````

## RL-015 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.3 Artifact storage and execution-surface selection \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
### **9.1.3 Artifact storage and execution-surface selection \[Required-Now\]**

Before the first write, classify each output and identify its authorized destination. The classification applies to content and operational role, not merely its filename or an approval status. When uncertain, use `EPHEMERAL_LIBRARY` unless controlling authority establishes another class. A task creating change-process files must explicitly prohibit Drive persistence.

| Class | Required destination and boundary |
| ----- | ----- |
| `EPHEMERAL_LIBRARY` | Every off-repository change-process artifact belongs in ChatGPT Library. This includes intake, kickoff, Specifications, Plans, audits, instructions, tasks, authoring/execution results, reviews, QA/evidence exports, approvals, coordination, recovery, reconciliation, drainage, closure and retrospective files. Approval, importance or a desire for long retention creates no Drive exception. |
| `REPOSITORY_CONTROLLED` | Source, tests, configuration, repository documentation and native governed outputs remain in their authorized repository homes under the applicable writer and evidence contracts. An exported review copy, report or evidence bundle is an off-repository artifact and belongs in Library. |
| `CONTROL_NOTION` | Concise navigation, current status, ownership, indexes, decisions and exact artifact references belong in their authorized Notion control surfaces. Notion does not become a store for complete change artifacts or a second substantive authority. |
| `DURABLE_DRIVE` | Current canonical and ongoing operational authorities belong in their controlled Drive homes. Change-process artifacts do not become this class through approval or archival intent. |
| `TRANSIENT_SCRATCH` | Active authoring, extraction and validation intermediates may use scratch. Anything needed for later review, continuity or handoff must be retained in Library before relying on it durably. |

Do not create a new off-repository change artifact or convenience copy in Drive. If required Library retention is unavailable, preserve completed safe work and report the exact durable-save blocker; do not substitute Drive, Notion or scratch as the durable handoff. Final results identify the actual saved file/version and retrieval reference. Linking a Library artifact from Notion, a tracker or another record does not change its class. These rules are prospective: retain legacy records and their original provenance; materially revised change-artifact versions use Library without automatically inventorying, migrating, duplicating, archiving or deleting earlier copies. Existing pointers may await ordinary maintenance; new pointers resolve the applicable Library version. If an unauthorized new persistent copy was made, stop duplication and retain the intended artifact in Library. Removal or archival of the unauthorized copy needs its ordinary mutation authority. Reviewers classify unauthorized Drive creation/duplication as a storage-policy failure; they do not silently delete it. Storage authority does not grant mutation or publication authority.

Every downstream-session prompt must receive task-specific human advice for execution surface, model and reasoning level from the complete work, applicable constraints, available capabilities and eligible alternatives. Compare total completion cost, including retrieval, verification, retries, handoff and human correction, while preserving acceptance quality. Model names, long inputs or connector presence alone do not determine capability or effort. Use relevant installed skills only when their actual interface and safeguards fit the task and improve the complete operation.

Local CLI eligibility remains bounded by directly verified skill/input access, task capability and net benefit after packaging, transfer, verification and review. A separate PO designation is not required merely for a prompt author to select that surface. Standard ChatGPT remains required for development, tasks assigned to a specific authoritative session role, PO decision/authorization packets, live Notion/Drive/Docs mutation, Library persistence/version management, prompt publication, registry/routing/activation/lifecycle work and runtime/production operations. PF mutation requires the actual exact-document/exact-action authority. QA is ordinarily on that surface; §9.1.4 permits bounded authorized QA/Ops execution, including a local client, without transferring another role or granting missing permissions. When a required skill, source or access boundary is unknown, select standard ChatGPT. A local handoff uses one dedicated output directory and compact archive containing the manifest, core deliverables, hashes, results and limitations; do not scatter Drive copies. Measure representative complete-task cost where needed without treating a capability audit as proof of savings. Advice never switches, restarts, reconfigures or creates a session and never authorizes delegation; do not claim a model/effort setting that was not actually observed. Current dated selection guidance remains in **Prompt Selection and Session Delegation Protocol** and **General Prompt Flow and Creation Guidelines**, in Glow / Ops.


````

**NEW (literal):**

````
### **9.1.3 Artifact storage and execution-surface selection \[Required-Now\]**

Before the first write, classify each output and identify its authorized destination by content and operational role. Change-process documents, including documents of uncertain class, use `REPOSITORY_CONTROLLED` storage under `docs/ephemeral/` and repository-path references. A change-process task must explicitly prohibit Drive persistence.

| Class | Required destination and boundary |
| ----- | ----- |
| `REPOSITORY_CONTROLLED` | Intake, kickoff, Specifications, Plans, audits, triage, readiness records, Guides, instructions, tasks, reviews, reports, RCAs, remediation, handoffs, redlines, dispositions, drainage, closure and retrospective work products belong under `docs/ephemeral/`. Persistent prompt-ecosystem management records belong under `docs/prompt_ecosystem_management/`. Code, tests, configuration and governed evidence retain their established paths, writers and integrity contracts. |
| `CONTROL_NOTION` | Authorized operational state, navigation, ownership, indexes and exact artifact references remain in Notion. It does not become the PF authority or a second store of complete change artifacts. Reusable GCFPE prompt bodies retain their separately governed Notion single home. |
| `TRANSIENT_SCRATCH` | Active authoring, extraction and validation intermediates may use scratch. Work needed for review, continuity or handoff is saved under the applicable repository home before durable reliance. |

ChatGPT Library and Google Drive are neither destinations nor authorities for change-process documents. A specific Product Owner direction may place an identified file in Drive; that file gains no authority. Legacy Library, Drive and Notion records retain their provenance. These rules authorize no automatic move, copy, re-homing, deletion or archive action. Save and read back the actual repository artifact, record its path and available commit, and report a durable-save blocker honestly if saving fails. Storage authority confers no mutation or publication permission. The repository home for ongoing non-PF operating procedures and externally cited selection guidance remains undecided; do not invent one or treat Drive as their authority.

Every downstream-session prompt must receive task-specific human advice for execution surface, model and reasoning level from the complete work, applicable constraints, available capabilities and eligible alternatives. Compare total completion cost, including retrieval, verification, retries, handoff and human correction, while preserving acceptance quality. Model names, long inputs or connector presence alone do not determine capability or effort. Use relevant installed skills only when their actual interface and safeguards fit the task and improve the complete operation.

Execution-surface eligibility is bounded by directly verified skill/input access, task capability and net benefit after packaging, transfer, verification and review. No governance rule requires a particular AI provider, product, model or effort level. Development, authoritative role work, decision packets, live document or Notion mutation, prompt publication, registry/routing/activation/lifecycle work, QA and runtime or production operations use any surface with the access, tools and actual authority required for the task. The surface confers no permission and transfers no role or session ownership. PF mutation retains exact-document/exact-action authority; §9.1.4 preserves bounded authorized QA/Ops execution. Unknown skill, source or access capability must be established for the chosen surface before relying on it.

A local handoff uses one dedicated output directory and compact archive containing the manifest, core deliverables, hashes, results and limitations; do not scatter Drive copies. Measure representative complete-task cost when needed; a capability audit is not proof of savings. Advice never switches, restarts, reconfigures or creates a session and never authorizes delegation. Do not claim an unobserved model or effort setting. Externally cited **Prompt Selection and Session Delegation Protocol** and **General Prompt Flow and Creation Guidelines** create no provider, product or model requirement; their placement remains undecided.

Governance actors and prompts are read by function. The executing agent audits, builds, tests and uses the authorized mutation route. The Implementation Agent retains its own role; a repository audit is read-only evidence for the change, and an implementation prompt is given to the executing agent. Product names in exact vocabulary values and fields retain their spelling and functional meaning: `CA vetted`, `Observed Evidence (Codex Audit)`, `Observed repo reality (Codex Audit)`, `Codex prompt`, `codex`, `codex_inputs` and `codex_can_see_pf_docs`. Historical records, provenance, examples, inventories and repository identifiers retain their wording. Capabilities of the chosen agent are established for the change; self-contained prompts, verbatim execution-critical material and Asset Draft Packs remain required under their owning contracts. Product boundaries excluding AI providers, LLMs, model calls and AI enablement from HD Engine and vendor runtime remain unchanged.


````

## RL-016 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.4 QA/Ops execution sources and substantive currentness \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
For bounded, already-authorized QA or Ops execution, an operator may use prepared `docs/pfcanon` copies when Drive is unavailable. Record the actual PF copies, versions or other available identifiers used and the access limitation. No Drive comparison certificate is required. This exception concerns execution source access only: it does not authorize unrestricted planning from a mirror, waive an actual canon conflict, widen scope or grant tools, credentials, mutation, network, rails or privileged-action permission.
````

**NEW (literal):**

````
All work, including planning, governance authoring, task preparation and bounded already-authorized QA or Ops execution, resolves current PF authority from `docs/pfcanon/` on `main`. Record the actual PF documents, versions or available identifiers used and any access limitation. No Drive comparison certificate is required. Canon resolution does not waive a conflict, widen scope or grant tools, credentials, mutation, network, rails or privileged-action permission.
````

## RL-017 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.6 Prompt ecosystem governance and provenance \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Reusable GCFPE development-flow and management prompt bodies, including human model headers, are single-homed in Notion and must not be published or mirrored as executable bodies in Drive or the repository. External reference instructions in those bodies and temporary repair/review/handoff prompts use the controlled directory, versionless document name and appropriate section. Do not substitute static hyperlinks, provider file/page IDs, version-pinned external filenames or mutable product facts for actual source resolution. The prompt's own version and human model header remain permitted. Temporary prompts may be retained in Library. Actual use/provenance records outside prompt bodies retain exact resolved versions and identities; a missing/ambiguous source follows its existing task contract without a new approval gate. This rule does not erase necessary exact source binding in run artifacts, reports or historical evidence.
````

**NEW (literal):**

````
Reusable GCFPE development-flow and management prompt bodies, including human model headers, are single-homed in Notion and must not be published or mirrored as executable bodies in Drive or the repository. External reference instructions in those bodies and temporary repair/review/handoff prompts use the controlled directory, versionless document name and appropriate section. Do not substitute static hyperlinks, provider file/page IDs, version-pinned external filenames or mutable product facts for actual source resolution. The prompt's own version and human model header remain permitted. Temporary change-process repair, review and handoff prompts are retained under `docs/ephemeral/`; reusable executable prompt bodies remain single-homed in Notion. Actual use/provenance records outside prompt bodies retain exact resolved versions and identities; a missing/ambiguous source follows its existing task contract without a new approval gate. This rule does not erase necessary exact source binding in run artifacts, reports or historical evidence.
````

## RL-018 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.6 Prompt ecosystem governance and provenance \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Update the map when a prompt is proposed, contracted, authored, independently reviewed, repaired, published, activated, held, superseded, retired or replaced by an immutable successor. Preserve exact identities and distinguish mutable Notion representations from immutable Library/registry artifacts. Each entry/review declares one active layer: `RUNTIME_PROMPT_CONTRACT` or `GOVERNANCE_REPAIR`. A consistency reviewer in the latter layer does not replace continuing runtime Thoth.
````

**NEW (literal):**

````
Update the map when a prompt is proposed, contracted, authored, independently reviewed, repaired, published, activated, held, superseded, retired or replaced by an immutable successor. Preserve exact identities and distinguish mutable Notion representations from immutable governed registry artifacts and retained historical records. Each entry/review declares one active layer: `RUNTIME_PROMPT_CONTRACT` or `GOVERNANCE_REPAIR`. A consistency reviewer in the latter layer does not replace continuing runtime Thoth.
````

## RL-019 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.6 Prompt ecosystem governance and provenance \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Keep each applicable human operator header's surface/model/effort guidance current at the established monthly review and relevant release changes, based on actual task workload and verified eligible options. Do not create a duplicate schedule. Preserve predecessor advice when still applicable; assess an expanded or materially different next task separately. Do not select a fixed model/effort solely from prompt ID or add fixed advice to PR-30. Known text defects, checked candidate corrections, published selection and observed runtime correction are separate states. Preserve the failing case for focused retest; runtime resolution needs its actual observed-behavior or user-confirmation condition. Static checks, publication readback and fictional walkthroughs are not runtime validation.
````

**NEW (literal):**

````
No agent or role maintains, reviews or refreshes human operator header surface, model or effort guidance on a monthly or release-driven schedule; that review is not a prerequisite for prompt selection, publication, maintenance or use. Known text defects, checked candidate corrections, published selection and observed runtime correction are separate states. Preserve the failing case for focused retest; runtime resolution needs its actual observed-behavior or user-confirmation condition. Static checks, publication readback and fictional walkthroughs are not runtime validation.
````

## RL-020 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.1 Single-home doctrine (routing by title)**
### **9.1.6 Prompt ecosystem governance and provenance \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Supporting skills retain their actual domain interfaces, owner and maintenance authorization; a maintenance action does not activate orchestration or grant runtime permissions. Ongoing operating procedures remain controlled Drive Markdown authorities. Preserve immutable historical R1 and predecessor material; authorized retirement moves originals intact to the established archive rather than deleting or copy-then-deleting them. Reconcile current navigation separately.
````

**NEW (literal):**

````
Supporting skills retain their actual domain interfaces, owner and maintenance authorization; a maintenance action does not activate orchestration or grant runtime permissions. Drive confers no authority on ongoing operating procedures; their repository placement remains undecided and is not assigned here. Preserve immutable historical R1 and predecessor material; authorized retirement moves originals intact to the established archive rather than deleting or copy-then-deleting them. Reconcile current navigation separately.
````

## RL-021 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**
### **2.0.0 Token admission & lifecycle (value-only)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**Operational discovery, open-rails, Codex Audit, and OPS evidence posture.** Operational discovery, bounded OPS evidence, PO-authorized open-rails evidence, and read-only repository observations MAY support planning, implementation, QA design, review, or drainage. They do not by themselves prove QA PASS, OPS completion, live-vendor truth, PF09 or PF30 status movement, epic or CRD closure, PF-canon drainage, or acceptance.
````

**NEW (literal):**

````
**Operational discovery, open-rails, read-only repository audit, and OPS evidence posture.** Operational discovery, bounded OPS evidence, PO-authorized open-rails evidence, and read-only repository observations MAY support planning, implementation, QA design, review, or drainage. They do not by themselves prove QA PASS, OPS completion, live-vendor truth, PF09 or PF30 status movement, epic or CRD closure, PF-canon drainage, or acceptance.
````

## RL-022 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **QA and acceptance classification posture.** QA plans, review artifacts, Live QA results, acceptance maps, token/evidence matrices, closeout reports, PR reviews, implementation plan reviews, and Codex prompts MUST NOT classify display-layer escape artifacts as `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, or closeout blocker. If raw source verification proves a substantive defect, classify the real underlying issue, not the display rendering.  
````

**NEW (literal):**

````
* **QA and acceptance classification posture.** QA plans, review artifacts, Live QA results, acceptance maps, token/evidence matrices, closeout reports, PR reviews, implementation plan reviews, and prompts for the executing agent MUST NOT classify display-layer escape artifacts as `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, or closeout blocker. If raw source verification proves a substantive defect, classify the real underlying issue, not the display rendering.  
````

## RL-023 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Codex prompt posture.** Codex prompts MUST treat escaped display text as non-authoritative unless the escaped text is inside a raw source file that Codex opens. Codex MUST NOT create alternate escaped paths or filenames, rename paths, remediate paths, or fix commands solely because assistant-rendered prompt text displayed backslashes.  
````

**NEW (literal):**

````
* **Implementation prompt posture.** Prompts for the executing agent MUST treat escaped display text as non-authoritative unless the escaped text is inside a raw source file that the executing agent opens. The executing agent MUST NOT create alternate escaped paths or filenames, rename paths, remediate paths, or fix commands solely because assistant-rendered prompt text displayed backslashes.  
````

## RL-024 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Template-hygiene materiality rule.** A planning artifact, implementation plan, QA plan, remediation guide, review artifact, or closeout planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table order, section phrasing, planning-only path labels, titles-only polish, or section-locator precision unless the defect materially changes source-of-truth authority, implementation scope, PF09 completion mapping, acceptance truth, exact-source identity, evidence trust, Codex portability, OPS/PR boundary, execution safety, public/private posture, canon-conflict handling, or closeout truth.  
````

**NEW (literal):**

````
* **Template-hygiene materiality rule.** A planning artifact, implementation plan, QA plan, remediation guide, review artifact, or closeout planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table order, section phrasing, planning-only path labels, titles-only polish, or section-locator precision unless the defect materially changes source-of-truth authority, implementation scope, PF09 completion mapping, acceptance truth, exact-source identity, evidence trust, portability for the executing agent, OPS/PR boundary, execution safety, public/private posture, canon-conflict handling, or closeout truth.  
````

## RL-025 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Valid blocker classes remain material.** Proven blockers include contradiction with active PF10 guidance; an unresolved source-authority conflict; unsupported Already Implemented or acceptance claims; reliance on unavailable non-PF material as execution authority; OPS work inside Codex PR work; an asserted repo locus without allowed proof or discovery-first posture; unsupported public-surface expansion; PF23 used as a deliverable or acceptance authority; PF20 used as current planning authority; unsafe execution; ambiguous candidate identity; missing applicable evidence; and acceptance or closeout claims that collapse distinct repository, CI, QA, approval, or lifecycle states.  
````

**NEW (literal):**

````
* **Valid blocker classes remain material.** Proven blockers include contradiction with active PF10 guidance; an unresolved source-authority conflict; unsupported Already Implemented or acceptance claims; reliance on unavailable non-PF material as execution authority; OPS work inside PR work of the executing agent; an asserted repo locus without allowed proof or discovery-first posture; unsupported public-surface expansion; PF23 used as a deliverable or acceptance authority; PF20 used as current planning authority; unsafe execution; ambiguous candidate identity; missing applicable evidence; and acceptance or closeout claims that collapse distinct repository, CI, QA, approval, or lifecycle states.  
````

## RL-026 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Implementation Plan review boundary.** Change-wide Implementation Plans must be more concrete than Specifications; detailed per-PR Plans are prepared in the dedicated engineering session, but formatting defects are not blockers unless they create real Codex or OPS ambiguity. If a plan tells Codex to consult CA or an audit, that is a blocker. If the plan embeds the needed fact and Codex can proceed without external documents, CA or audit provenance wording is not a blocker. If an Already Implemented claim relies on CA, the plan should embed enough proof in the plan itself. Imperfect CA quote-block formatting is not a blocker when the fact is clear, self-contained, and not used to smuggle in requirements.  
````

**NEW (literal):**

````
* **Implementation Plan review boundary.** Change-wide Implementation Plans must be more concrete than Specifications; detailed per-PR Plans are prepared in the dedicated engineering session, but formatting defects are not blockers unless they create real ambiguity in development or OPS execution. If a plan tells the executing agent to consult CA or an audit, that is a blocker. If the plan embeds the needed fact and the executing agent can proceed without external documents, CA or audit provenance wording is not a blocker. If an Already Implemented claim relies on CA, the plan should embed enough proof in the plan itself. Imperfect CA quote-block formatting is not a blocker when the fact is clear, self-contained, and not used to smuggle in requirements.  
````

## RL-027 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Audit provenance is not authority by itself.** Audit provenance MUST NOT be converted into PR instructions, OPS instructions, step-by-step execution procedure, Codex command source, privileged-action authority, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth, required deliverable authority, source of invented file or path existence, source of secrets, or source of external-state truth. If audit provenance points to current repo reality, the current repo claim must be validated by the allowed repo-validation route before it is used as current fact.  
````

**NEW (literal):**

````
* **Audit provenance is not authority by itself.** Audit provenance MUST NOT be converted into PR instructions, OPS instructions, step-by-step execution procedure, command source for the executing agent, privileged-action authority, acceptance authority, token authority, QA PASS proof, OPS completion proof, PF09 Done proof, closeout proof, current repo truth, required deliverable authority, source of invented file or path existence, source of secrets, or source of external-state truth. If audit provenance points to current repo reality, the current repo claim must be validated by the allowed repo-validation route before it is used as current fact.  
````

## RL-028 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Review burden for audit provenance blockers.** A blocker is valid only when the artifact uses audit provenance as execution authority or proof authority, requires Codex or OPS to consult the audit itself, or relies on the audit as current repo proof without validation. If the audit only explains why work exists, what risk was observed, what should be inspected, or why a proof is planned, the correct classification is no issue, note, context accepted, planning provenance accepted, repo validation required before execution, or keep out of PR/OPS instruction text.  
````

**NEW (literal):**

````
* **Review burden for audit provenance blockers.** A blocker is valid only when the artifact uses audit provenance as execution authority or proof authority, requires the executing agent or OPS to consult the audit itself, or relies on the audit as current repo proof without validation. If the audit only explains why work exists, what risk was observed, what should be inspected, or why a proof is planned, the correct classification is no issue, note, context accepted, planning provenance accepted, repo validation required before execution, or keep out of PR/OPS instruction text.  
````

## RL-029 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Plans are approval artifacts, not execution artifacts.** QA Plans, Epic or CRD Specifications, change-wide or detailed per-PR Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, and closure-review artifacts MUST NOT be blocked, rejected, returned for revision, or classified as `REVISE AND RESUBMIT` because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written. This applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly. Plans are approved on truth, proof, scope, authority, safety, acceptance posture, phase fidelity, and evidence identity. Plans are not blocked on syntax.  
````

**NEW (literal):**

````
* **Plans are approval artifacts, not execution artifacts.** QA Plans, Epic or CRD Specifications, change-wide or detailed per-PR Implementation Plans, remediation plans, review prompts, redline prompts, prompts for the executing agent, and closure-review artifacts MUST NOT be blocked, rejected, returned for revision, or classified as `REVISE AND RESUBMIT` because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written. This applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly. Plans are approved on truth, proof, scope, authority, safety, acceptance posture, phase fidelity, and evidence identity. Plans are not blocked on syntax.  
````

## RL-030 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Truth/proof blockers only.** Valid approval blockers remain limited to material truth, authority, scope, evidence, safety, phase, acceptance, public/private boundary, OPS/QA/PR category separation, applicable PF09 or approved CRD/IP accountability mapping, source-of-truth, token, canon-conflict, required-proof, or evidence-identity defects. Missing proof obligation, missing applicable in-scope work mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement under closed rails, secret exposure requirement, OPS work assigned to Codex, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, or unclear PASS/FAIL posture remain valid blockers when proven. They are not syntax issues.  
````

**NEW (literal):**

````
* **Truth/proof blockers only.** Valid approval blockers remain limited to material truth, authority, scope, evidence, safety, phase, acceptance, public/private boundary, OPS/QA/PR category separation, applicable PF09 or approved CRD/IP accountability mapping, source-of-truth, token, canon-conflict, required-proof, or evidence-identity defects. Missing proof obligation, missing applicable in-scope work mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement under closed rails, secret exposure requirement, OPS work assigned to the executing agent, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, or unclear PASS/FAIL posture remain valid blockers when proven. They are not syntax issues.  
````

## RL-031 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **In-flight normalization rule.** Syntax correction is ordinary execution hygiene. If a QA operator, Codex, Kronos, Product Owner, or implementation owner encounters a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue during execution, they may normalize it in flight as long as they preserve the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture. In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, or authority actually changes.  
````

**NEW (literal):**

````
* **In-flight normalization rule.** Syntax correction is ordinary execution hygiene. If a QA operator, the executing agent, Kronos, Product Owner, or implementation owner encounters a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue during execution, they may normalize it in flight as long as they preserve the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture. In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, or authority actually changes.  
````

## RL-032 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.9 Canonical evidence-path binding validation (acceptance integrity)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
  * **CA vetted:** an inline verbatim quote from the planning Codex audit that supports the asserted locus.  
````

**NEW (literal):**

````
  * **CA vetted:** an inline verbatim quote from the planning read-only repository audit that supports the asserted locus.  
````

## RL-033 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.9 Canonical evidence-path binding validation (acceptance integrity)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
  * The planning audit MUST NOT be referenced in final instructions given to Codex for implementation.  
````

**NEW (literal):**

````
  * The planning audit MUST NOT be referenced in final instructions given to the executing agent for implementation.  
````

## RL-034 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.7 Token fidelity & plan approval rails \[Required−Now\]**
### **9.7.9 Canonical evidence-path binding validation (acceptance integrity)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**Non-PF guidance is not a path authority.** QA guides and other non-PF documents may describe intent, but they MUST NOT be treated as canonical sources for required file path existence or naming. For plan-time locus support, the only permitted non-PF mechanism is an inline verbatim quote labeled “CA vetted” (planning Codex audit output) or “IP Approved” (the exact approved change-wide Implementation Plan). Any path supported by non-PF material still MUST be reconciled to PF canon single homes or be explicitly created under rule (3) before it can be treated as required.
````

**NEW (literal):**

````
**Non-PF guidance is not a path authority.** QA guides and other non-PF documents may describe intent, but they MUST NOT be treated as canonical sources for required file path existence or naming. For plan-time locus support, the only permitted non-PF mechanism is an inline verbatim quote labeled “CA vetted” (planning read-only repository audit output) or “IP Approved” (the exact approved change-wide Implementation Plan). Any path supported by non-PF material still MUST be reconciled to PF canon single homes or be explicitly created under rule (3) before it can be treated as required.
````

## RL-035 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.8 QA plans — step-level Deliverables (no screen-only acceptance) \[Required−Now\]**
### **9.8.2 Rule — Deliverables are mandatory per step**
````

**Expected occurrence:** 1

**OLD (literal):**

````
  * Command provenance vocabulary. If a governed step record includes a command provenance value, it MUST use one of: Codex prompt, Copy/paste from plan, or Explicitly created.  
````

**NEW (literal):**

````
  * Command provenance vocabulary. If a governed step record includes a command provenance value, it MUST use one of: Codex prompt, Copy/paste from plan, or Explicitly created.   The exact value `Codex prompt` denotes the prompt given to the executing agent, whichever product performs that function; preserve its spelling.
````

## RL-036 — REPLACE

**Original heading path:**

````
# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**
## **2.2 A4 — Reader↔CLI parity \[Required−Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
## **2.2 A4 — Reader↔CLI parity \[Required−Now\]**

* **Scope.** A4 parity applies to the **Reader v1 public success envelope** (`200`) and **typed error envelopes**. The CLI participates in this gate only when it is emitting **Reader v1 bytes** (for example via `--dump-reader` sidecars; byte/sidecar contract lives by title in **HDE-CLI-API-Vendor-Ref**). This gate does **not** compare `hdctl showcompat` stdout (compatibility payload) to Reader v1 bytes.  
* **Single presenter/emitter.** Reader and CLI MUST call the same emitter to produce Reader v1 success and typed error bodies; no ad-hoc dumps or parallel “mini-emitters.”  
* **Byte equality.** For identical inputs/environment, the Reader HTTP body MUST be byte-identical to the CLI-emitted Reader v1 body bytes (including the single LF). For this gate, “CLI-emitted Reader v1 body bytes” means the exact bytes captured via the CLI `--dump-reader` output (not `showcompat` stdout).  
* **Canonical JSON.** Public bytes are serialized with the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. All checks run under `LC_ALL=C`.  
* **Public resonance posture (v1).** No SR/XR numerics appear on Reader `200`. v1 ships SR-only (alpha \\= 1.0); hysteresis \\= 1 is armed for future XR and not exposed.

**Schema/shape gates**

1. **Success:** exactly the six keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*]` are exactly `{ "id", "band" }` (numeric-free; `band ∈ {"Cool","Open","Warm","Glow"}`).  
2. **Errors:** typed, numeric-free JSON; LF-terminated; no PII.

**Validation gates (binary)**

1. **Reader↔CLI compare:** byte-compare the Reader HTTP body against the CLI-emitted Reader v1 body bytes (captured via `--dump-reader`). Compare both success bodies and typed error bodies where the CLI emits Reader v1 bytes. All comparisons MUST include the single trailing LF.  
2. **Shape checks:** enforce success/error schemas above (reject extras, numerics, or missing fields).  
3. **Emitter proof:** CI/allowlist shows both surfaces invoke the same emitter symbol.

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---


````

**NEW (literal):**

````
## **2.2 A4 — Reader↔CLI parity \[Required−Now\]**

* **Scope.** A4 parity applies to the **Reader v1 public success envelope** (`200`) and mapped **typed failures** under their separate carriers. The CLI participates in this gate only when it is emitting **Reader v1 bytes** (for example via `--dump-reader` sidecars; byte/sidecar contract lives by title in **HDE-CLI-API-Vendor-Ref**). This gate does **not** compare `hdctl showcompat` stdout (compatibility payload) to Reader v1 bytes.  
* **Single presenter/emitter.** Reader and CLI MUST call the same emitter to produce Reader v1 success JSON; HTTP typed error bodies use the same canonical emission boundary, while CLI failures retain their LF-terminated stderr token contract; no ad-hoc dumps or parallel “mini-emitters.”  
* **Byte equality.** For identical inputs/environment, the Reader HTTP body MUST be byte-identical to the CLI-emitted Reader v1 body bytes (including the single LF). For this gate, “CLI-emitted Reader v1 body bytes” means the exact bytes captured via the CLI `--dump-reader` output (not `showcompat` stdout).  
* **Canonical JSON.** Public bytes are serialized with the canonical serializer (PF-Schemas & Artifacts §4): UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays used as sets are deduped and ASCII-sorted. All checks run under `LC_ALL=C`.  
* **Public resonance posture (v1).** No SR/XR numerics appear on Reader `200`. v1 ships SR-only (alpha \\= 1.0); hysteresis \\= 1 is armed for future XR and not exposed.

**Schema/shape gates**

1. **Success:** exactly the six keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`); `categories[*]` are exactly `{ "id", "band" }` (numeric-free; `band ∈ {"Cool","Open","Warm","Glow"}`).  
2. **Errors:** Reader HTTP uses the closed four-key numeric-free `error_v1` envelope with `schema:"v1"`, `ok:false`, governed `code`/`error` and no optional fields; one LF and no PII. CLI mapped failures use the owning stderr token contract.

**Validation gates (binary)**

1. **Reader↔CLI compare:** byte-compare the Reader HTTP body against the CLI-emitted Reader v1 body bytes (captured via `--dump-reader`). Compare success bodies where the CLI emits Reader v1 bytes. For the same mapped failure, compare the CLI stderr token with HTTP `error_v1.code`; do not require whole-envelope equality across different carriers. All comparisons MUST include the single trailing LF.  
2. **Shape checks:** enforce success/error schemas above (reject extras, numerics, or missing fields).  
3. **Emitter proof:** CI/allowlist shows both surfaces invoke the same emitter symbol.

*Tokens: see §2.0 Acceptance Tokens (A-gates roster).*

---


````

## RL-037 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
## **9.8 QA plans — step-level Deliverables (no screen-only acceptance) \[Required−Now\]**
### **9.8.2 Rule — Deliverables are mandatory per step**
````

**Expected occurrence:** 1

**OLD (literal):**

````
If a functional change touches a vendor seam, the functional Live QA step MUST exercise that seam (live or controlled mock) and capture evidence of the observed behavior. If functional proof requires opening SAFE rails (for example `ALLOW_NETWORK=1`), that is acceptable when required, but it MUST be explicit, bounded, and captured with a keys-only and secret-free evidence posture (see §3.1).
````

**NEW (literal):**

````
If a functional change touches a vendor seam, the functional Live QA step MUST exercise that seam and capture its observed behavior. For every QA plan touching a surface used to produce a production feature described as functional in PF canon, §3.4 additionally requires a live vendor call under `SAFE_MODE=0` and `ALLOW_NETWORK=1` using synthetic data only. A controlled mock may support another bounded check but cannot satisfy that mandatory test. Authorization, request limits, secret-safe evidence and classification controls remain in force.
````

## RL-038 — REPLACE

**Original heading path:**

````
# **10\. Transport Governance (Reader) \[Required-Now\]**
## **10.0 Canonical Reader surfaces and proof-route posture \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
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


````

**NEW (literal):**

````
## **10.0 Canonical Reader surfaces and proof-route posture \[Required-Now\]**

**Rule (normative).** The production Reader HTTP surface is `POST /api/reader`, selected by exactly one `v=1` or `v=2` query value under the PF05-owned request and version contract. Dev `GET /reader` remains Reader v1; it is not a production GET alias. A missing, unsupported, duplicated or malformed version is refused. Query versioning does not authorize invented path segments.

**Rule (normative).** The Aux Narrative HTTP surface is `GET /aux/narrative` (and `GET /api/aux/narrative` only when the Aux blueprint is mounted under `/api`).

**Prohibition (normative).** The route `/api/reader-proof/v1` does not exist and MUST NOT be referenced in catalogs, plans, or transport proofs. Proof routes MUST be selected from the actual configured mount and the endpoint catalog outputs (when used).

**Rule (normative).** When a proof or Live QA plan needs a Reader or Aux route, it MUST:

* name the actual method and route: production `POST /api/reader` with its selected version, dev `GET /reader` for v1 only, or the governed Aux route with `/api/**` only when configured  
* capture evidence from the real route surface, not from an invented substitute

**Governed Reader success-proof-surface designation (normative).** The cataloged production `POST /api/reader` success route, selected by `v=1` or `v=2`, is the governed production Reader success-proof surface for Reader transport proof selection and related QA interpretation.

* Governance MUST NOT require a second designation carrier, a second inventory home, a new route, or a new flag to recognize that surface.  
* If the Endpoint Catalog row for the canonical Reader route remains present and A7-eligible but the inventory or readout still does not make that governed proof-surface status explicit, treat that omission as catalog or canon drift to be drained. It is not a reason to block proof-surface determination, invent a substitute proof route, or widen remediation into runtime or writer work.  
* Supplemental dev-harness, preview, or lookup captures do not create a second Reader proof surface. Apply A7 success validators only where the selected method/route contract supports them; production POST is non-conditional and does not gain GET/HEAD/304 behavior from the dev harness. Reader A7 proofs remain bound to their cataloged JSON success route, and `/internal/version` remains ops-only and excluded from A7.


````

## RL-039 — REPLACE

**Original heading path:**

````
# **10\. Transport Governance (Reader) \[Required-Now\]**
## **10.1 Success (200) matrix \[Required-Now\]**
### **Body — success covenant**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Categories policy (v1).** `categories[*]` are exactly **{ id, band }** (numeric-free). If `eligible == true` in v1 Alpha, a single `{"id":"harmony","band":<BAND>}`; if `eligible == false`, `[]`.  
````

**NEW (literal):**

````
* **Categories policy (v1).** `categories[*]` are exactly **{ id, band }** (numeric-free). If `eligible == true` in v1 Alpha, a single `{"id":"harmony","band":<BAND>}`; if `eligible == false`, `[]`.   Reader v2 follows §8.1: ten intrinsic bands in governed order when eligible and `[]` when ineligible, with `reader_version:"v2"`; its array is not set-sorted.
````

## RL-040 — REPLACE

**Original heading path:**

````
# **10\. Transport Governance (Reader) \[Required-Now\]**
## **10.3 Writers and errors \[Required-Now\]**
### **Body — typed error shape (errors only)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Shape.** Typed, numeric-free error object (see CLI/Reader error model):  
  `{"ok": false, "code": "<TOKEN>", "error": "<non-PII message>"}`.  
  Optional `retry_after_ms` (integer ≥ 0\) only under a pinned vendor rate-limit policy.  

````

**NEW (literal):**

````
* **Reader error shape.** Reader v1 and v2 use the closed four-key `error_v1` object with `schema:"v1"`, `ok:false`, and the PF05-owned `code`/`error` pair. No `retry_after_ms`, `details` or other extra field is permitted on these Reader errors. Other surfaces retain their owning PF05/PF12 error contracts; this rule adds no optional vendor field.

````

## RL-041 — REPLACE

**Original heading path:**

````
# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**
## **11.1 Vendor request governance and exact-byte ownership \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
Existing SAFE rails, no-I/O refusal, typed error, keys-only logging, evidence-indexing, public Reader v1, and PO-only open-rails posture apply to HDAPI v2 vendor work. Plans, Implementation Plans, QA plans, reviews, acceptance maps, and closeout artifacts MUST distinguish contract-inventory proof, architecture update, closed-rails shaping proof, and PO-only open-rails vendor smoke.
````

**NEW (literal):**

````
Existing SAFE rails, no-I/O refusal, typed error, keys-only logging, evidence-indexing, public Reader v1/v2, and Product Owner-authorized open-rails posture apply to HDAPI v2 vendor work. Plans, Implementation Plans, QA plans, reviews, acceptance maps, and closeout artifacts MUST distinguish contract-inventory proof, architecture update, closed-rails shaping proof, and PO-only open-rails vendor smoke. For live vendor work, a task-directed automated agent is the executor and evidence producer under §3.3 and §3.4; the Product Owner remains authorizing and accountable principal. This grants no standing vendor-call authority.
````

## RL-042 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**
### **GATE:CORE-CANON — Canonical emission and comparators \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Arrays as sets:** dedupe by identity, then ASCII-sort; on value conflict, fail closed.
````

**NEW (literal):**

````
* **Arrays as sets:** dedupe by identity, then ASCII-sort; on value conflict, fail closed. Reader v2 `categories` is an ordered array and MUST retain the exact governed ten-category order without set sorting, deduplication or default fill.
````

## RL-043 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**
### **GATE:CORE-READER — Public covenant and transport hooks \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
**Scope.** Reader v1 public body and A7 transport validators. **Pass when (binary):**
````

**NEW (literal):**

````
**Scope.** Reader v1 and v2 public bodies and the transport validators applicable to each selected method/route. Existing Reader↔CLI dump parity remains v1. **Pass when (binary):**
````

## RL-044 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**
### **GATE:CORE-READER — Public covenant and transport hooks \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Errors:** typed, numeric-free JSON; canonical emission; one LF; no PII.
````

**NEW (literal):**

````
* **Errors:** Reader v1/v2 uses exactly `schema`, `ok`, `code`, `error`, with `schema:"v1"`, `ok:false`, governed token/message pairs and no optional fields; canonical numeric-free emission, one LF, no PII or secret echo.
````

## RL-045 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**
### **GATE:CORE-READER — Public covenant and transport hooks \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Error parity scenarios (deterministic acceptance).** Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor-attempt cases) MUST be reproducible under determinism pins and closed rails, without reliance on external network or a live database. Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts. Allowed fallback: a deterministic stub only to the extent required to produce the canonical error envelope (no live I/O). The acceptance proof MUST consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) with a stable scenario identifier, and Evidence Index \+ machine mirror MUST be updated in the same PR as any new parity artifacts.  
````

**NEW (literal):**

````
* **Error parity scenarios (deterministic acceptance).** Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor-attempt cases) MUST be reproducible under determinism pins and closed rails, without reliance on external network or a live database. Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts. Allowed fallback: a deterministic stub only to the extent required to produce the canonical error envelope (no live I/O). The acceptance proof MUST consist of stored artifacts for both sides of the mapped failure claim (Reader/HTTP `error_v1` and CLI stderr token), checking equality of the governed error code rather than entire-envelope byte equality with a stable scenario identifier, and Evidence Index \+ machine mirror MUST be updated in the same PR as any new parity artifacts.  
````

## RL-046 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.2 Evidence links (titles-only) \[Required-Now\]**
### **GATE:CORE-CANON — Canonical emission and comparators**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* Schema (success and error shapes): `schemas/reader.v1.schema.json`
````

**NEW (literal):**

````
* Schemas (versioned success and governed errors): `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`
````

## RL-047 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.2 Evidence links (titles-only) \[Required-Now\]**
### **GATE:CORE-READER — Public covenant and transport hooks**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* Schema and shape (six-key success; `{id, band}` only): `schemas/reader.v1.schema.json`
````

**NEW (literal):**

````
* Schema and shape (six-key success; `{id, band}` only; version-specific category cardinality/order; four-key Reader errors): `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`
````

## RL-048 — REPLACE

**Original heading path:**

````
# **13\. Versioning & Compatibility \[Required-Now\]**
## **13.1 Reader versioning (v1) \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
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


````

**NEW (literal):**

````
## **13.1 Reader versioning (v1 and v2) \[Required-Now\]**

**Principle (normative).**  
**Reader v1** is a **strict** public contract. Success bodies contain **exactly six** top-level keys and a **bands-only** `categories` array. Reader v2 is the approved, delivered full Magic-10 projection described in §8.1. Changes beyond an existing version's public shape or semantics require a separately governed versioned contract.

### **13.1.1 v1 success contract (strict)**

* **Six keys exactly:** `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`.  
* **`categories` items:** **exactly** `{ "id": <string>, "band": <"Cool"|"Open"|"Warm"|"Glow"> }` (numeric-free).  
* **Serialization:** canonical emitter (UTF-8, sorted keys, compact separators), **exactly one** trailing LF; `idempotence_hash` computed over the **five-key** preimage.  
* **v1 Alpha policy:** when `eligible==true`, public `categories` has **one** item with `id:"harmony"`; when `eligible==false`, `categories` **MUST** be `[]`.

### **13.1.2 Error contract (typed)**

* **Typed, numeric-free Reader error:** exactly `schema`, `ok`, `code`, `error`; `schema` is `"v1"` for both Reader versions and `ok` is `false`. Use the governed token/message pair; no `retry_after_ms`, `details` or other optional field. C040-08 reconciles the v1 schema with unchanged emitted bytes; it is not an error-byte or v1 contract change.  
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
* **Transport:** apply §10 validators to the actual selected method/route. Production POST remains non-conditional; dev GET/HEAD/304 rules do not create production methods. Reader errors use `no-store` and no ETag.  
* **Evidence:** goldens and scripts indexed in **Appendix D — Evidence Index** (titles/paths only).

### **13.1.6 Change control**

* **Public shape change ⇒ version bump.** Any proposal beyond the existing v1 or v2 contract **MUST** define the appropriate separately governed Reader version with updated schema, acceptance, and migration notes; land via Doc-Delta with full evidence.  
* **No silent drift.** Adding “optional” public fields under v1 is **prohibited**; clients and CI validate **strict equality** to the v1 schema.

### **13.1.7 v2 success contract and compatibility**

Reader v2 is selected by `v=2` on production `POST /api/reader` and fixes `reader_version` to `"v2"`. It keeps the same six top-level keys, item shape, band enum, read-only request resolution, eligibility decision, single emission path, five-key preimage and canonical serialization as v1. Eligible v2 exposes the complete ten intrinsic bands in the exact order and under the complete-or-fail-closed rules of §8.1; ineligible v2 exposes `[]`. AB↔BA, two-run identity and preimage recomputation apply to v2 bytes. V1 remains the unchanged single-harmony public contract, including dev `GET /reader`. V2 adds no CLI flag: existing Reader↔CLI dump parity remains v1. The owning v2 schema, goldens, release and evidence registration remain with **HDE-Schemas and Artifacts** and the existing writers; governance prose is not evidence regeneration, deployment or activation.


````

## RL-049 — REPLACE

**Original heading path:**

````
# **13\. Versioning & Compatibility \[Required-Now\]**
## **13.2 Presets/evolution policy \[Required-Now\]**
### **13.2.4 Versioning posture**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Reader version bump (v2+)** is required **only** if preset behavior would change the **public** contract (e.g., exposing additional public categories or public numerics). Such proposals must define the new version and land via Doc-Delta with full evidence (see §13.1).
````

**NEW (literal):**

````
* **Reader version bump (v2+)** is required **only** if preset behavior would change an existing version's **public** contract beyond the governed v1 or v2 projection. Such proposals must define the new version and land via Doc-Delta with full evidence (see §13.1).
````

## RL-050 — REPLACE

**Original heading path:**

````
# **12\. Gate Suites (Governance Gates) \[Required-Now\]**
## **12.1 CORE-CANON / CORE-DET / CORE-READER / CORE-MATCH**
### **GATE:CORE-MATCH — Compat math posture \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Public boundary:** no public numerics; Reader v1 remains `{id, band}` only (compat internals do not leak).
````

**NEW (literal):**

````
* **Public boundary:** no public numerics; Reader v1 and v2 remain `{id, band}` only under their version-specific category rules (compat internals do not leak).
````

## RL-051 — REPLACE

**Original heading path:**

````
# **15\. Open Toggles & Questions \[Open\]**
## **15.2 Open issues list**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **OI-001 — Reader v2 planning (full Magic-10 exposure).**  
  * *Owner:* Architecture \+ Math leads  
  * *Next step:* Draft a versioned `reader.v2` public schema, exact acceptance contract, and migration plan through an approved Doc-Delta. Keep Reader v1 unchanged. Reader v2 may expose the canonical complete ten-item intrinsic Magic-10 result only when every eligible pair has exactly the ten PF01 categories in canonical order, with no omission, duplication, default fill, harmony-only substitution, or viewer-preference mutation. Update PF01, PF05, PF12, tests, and Evidence Index entries in their owning surfaces.  
  * *Verified-as-of repository basis:* At pinned commit `0f89b37b222941e8da18759c02626d6b48c323a1`, `schemas/reader.v1.schema.json` exists and `schemas/reader.v2.schema.json` was not found in the complete tree. PF01 keeps full public Magic-10 exposure in a future Reader v2 versioned contract.  
  * *Status:* OPEN  

````

**NEW (literal):**

````
* **OI-001 — Reader v2 full Magic-10 exposure.**
  * *Decision:* C040-07 approved by the Product Owner on 2026-09-26; the ten-category exclusion is superseded for HDE-EPIC040, while the public-numeric exclusion stands.
  * *Delivery:* accepted-final PR06a delivered Reader v2 on `POST /api/reader?v=2`, the ordered ten-band projection, schema and goldens, the unchanged v1 covenant and the production route. Accepted-final PR06b delivered C040-08's v1 error-schema conformance without changing emitted bytes.
  * *Status:* CLOSED on PR06a delivery; this is closure of OI-001, not a fresh QA verdict, acceptance, deployment, release activation or ordinary Epic Close Gate claim.
  * *Owning drainage:* this PF04 revision records the governance rule. PF01, PF05, PF12 and consequential PF14/PF29 maintenance remain with their own maintainers; their publication is not performed or inferred here.

````

## RL-052 — REPLACE

**Original heading path:**

````
# **Appendix A — Transport Matrices (Reader) \[Required-Now\]**
## **A.2 Success (200) — body covenant**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Categories policy (v1):** `categories[*] == { id, band }` only (numeric-free); v1 Alpha: single `{"id":"harmony","band":<band>}` when `eligible == true`.  
````

**NEW (literal):**

````
* **Categories policy (v1):** `categories[*] == { id, band }` only (numeric-free); v1 Alpha: single `{"id":"harmony","band":<band>}` when `eligible == true`.   Ineligible v1 is `[]`. Reader v2 is ten intrinsic bands in the exact governed order when eligible and `[]` when ineligible (§8.1); it is not a set-sorted array.
````

## RL-053 — REPLACE

**Original heading path:**

````
# **Appendix A — Transport Matrices (Reader) \[Required-Now\]**
## **A.5 Writers & errors**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Errors.** `Content-Type: application/json; charset=utf-8`; typed errors only (numeric-free code/message object), LF-terminated; no PII; no vendor payload echo.  
````

**NEW (literal):**

````
* **Errors.** `Content-Type: application/json; charset=utf-8`; Reader errors use the closed four-key numeric-free `error_v1` envelope (`schema:"v1"`, `ok:false`, `code`, `error`) with no optional fields; other surfaces retain their owning error contract, LF-terminated; no PII; no vendor payload echo.  
````

## RL-054 — REPLACE

**Original heading path:**

````
# **Appendix B — Acceptance Gate Details \[Required-Now\]**
## **B.1 GATE:CORE-CANON — Canonical emission and comparators**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Checklist (binary):** single presenter/emitter; UTF-8; sorted keys; compact separators; one LF; arrays-as-sets deduped and ASCII-sorted; conflict ⇒ fail-closed; `LC_ALL=C`.  
````

**NEW (literal):**

````
* **Checklist (binary):** single presenter/emitter; UTF-8; sorted keys; compact separators; one LF; arrays-as-sets deduped and ASCII-sorted; ordered Reader v2 categories preserved exactly without set normalization; conflict ⇒ fail-closed; `LC_ALL=C`.  
````

## RL-055 — REPLACE

**Original heading path:**

````
# **Appendix B — Acceptance Gate Details \[Required-Now\]**
## **B.3 GATE:CORE-READER — Public covenant and transport hooks**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* **Checklist (binary):** success \\= six keys; `categories[*] == {id, band}` (numeric-free); typed error shape; Reader↔CLI byte-equality; A7 hooks present.  
````

**NEW (literal):**

````
* **Checklist (binary):** success \\= six keys; `categories[*] == {id, band}` (numeric-free); version-specific category cardinality and order; closed four-key Reader `error_v1`; existing Reader↔CLI dump byte-equality for v1; A7 hooks present.  
````

## RL-056 — REPLACE

**Original heading path:**

````
# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**
## **D.3 Idempotence coupling (preimage → sha256 → final)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* Schema (success, six keys): `schemas/reader.v1.schema.json`
````

**NEW (literal):**

````
* Schemas (success, six keys; version-specific projection): `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`
````

## RL-057 — REPLACE

**Original heading path:**

````
# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**
## **D.1 Parity (Reader↔CLI, AB↔BA, two-run)**
````

**Expected occurrence:** 1

**OLD (literal):**

````
* Goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`
````

**NEW (literal):**

````
* Goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`; v2 AB↔BA: `goldens/reader/v2/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v2/g02_ab_ba_parity_B.jsonl`. These v2 pointers do not extend CLI dump parity beyond v1.
````

## RL-058 — REPLACE

**Original heading path:**

````
# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**
> ## **9.3 Doc-Delta entries (what to record for any normative change)**
> ### **9.3.1 PF04 Governance Change Log \[Required-Now\]**
````

**Expected occurrence:** 1

**OLD (literal):**

````
An instantiated entry MUST contain no placeholder, blank required field, or “fill later” notation. An effective entry is complete only when the corresponding PF04 body change and local entry are both present, every required §9.4 field is concrete, and the class-specific authoritative record is complete. For `EPIC_BOUND`, close additionally requires byte identity between the two epic files. Proposals, candidates, unapplied edits, incomplete records, and speculative entries MUST NOT be logged as effective changes. Historical entries MUST NOT be reconstructed without direct evidence; when direct evidence is insufficient, the record MUST state bounded uncertainty instead of inventing precision.
````

**NEW (literal):**

````
An instantiated entry MUST contain no placeholder, blank required field, or “fill later” notation. An effective entry is complete only when the corresponding PF04 body change and local entry are both present, every required §9.4 field is concrete, and the class-specific authoritative record is complete. For `EPIC_BOUND`, close additionally requires byte identity between the two epic files. Proposals, candidates, unapplied edits, incomplete records, and speculative entries MUST NOT be logged as effective changes. Historical entries MUST NOT be reconstructed without direct evidence; when direct evidence is insufficient, the record MUST state bounded uncertainty instead of inventing precision.

v2.8.7 | GOV-20261009-gtwpe-pf04 | NON_EPIC | Scope: Reader v2 and errors; repository authority; vendor QA and execution; functional agent governance | Targets: §0.2, §0.4, §2.0, §2.2, §3.3–3.4, §8.1, §9.1.2–9.1.6, §9.7.7, §9.7.9, §9.8.2, §10, §11.1, §12–13, §15.2, Appendices A/B/D | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261009-gtwpe-pf04

> DOC-DELTA-ID: GOV-20261009-gtwpe-pf04
>
> Date / Author: 2026-10-09 / executing document agent in Nathan's T-PF04 conversation
>
> PF04 version: v2.8.7
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261009-gtwpe-pf04
>
> Scope: Public Contract/Transport; Vendor Ingest; Schema; Acceptance/Evidence; Governance/Documentation
>
> Targets (section anchors): §0.2, §0.4, §2.0, §2.2, §3.3–3.4, §8.1, §9.1.2–9.1.6, §9.7.7, §9.7.9, §9.8.2, §10, §11.1, §12–13, §15.2, Appendices A/B/D
>
> Summary (≤ 5 bullets):
>
> 1) Record the delivered Reader v2 ten-band projection, unchanged v1 contract, closed four-key Reader errors and OI-001 closure.
> 2) Resolve PF authority from repository main, store change-process artifacts in their repository home, and preserve board/pointer navigation boundaries.
> 3) Require the synthetic-data live vendor test for production-functional QA plans and task-directed agent execution using environment-held configuration.
> 4) Remove monthly/release-driven header-advice review and product-bound governance roles while retaining exact labels, permissions and generic downstream advice.
> 5) Apply title-only HDE Build Notes references and preserve independently owned proposals, history and nonclaims.
>
> Acceptance impact (binary gates to update or verify): C040-07 and C040-08 governance drainage; Reader v2 category cardinality/order, v1 category closure, four-key Reader errors, applicable canonical serialization, preimage, AB↔BA/two-run and route-specific transport criteria. Existing Reader↔CLI dump parity remains v1. Production-functional QA planning requires the live synthetic vendor test. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. Informative schema pointers include the delivered Reader v2 schema; existing owning writers and evidence contracts remain in force.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): Math and Architecture retain their owning rules. Exact transport, error and vendor bytes remain in HDE CLI/API Vendor Ref; schemas, release inputs and evidence registration remain in HDE Schemas and Artifacts. HDE Build Notes supplies the scoped overrides.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.6 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.7 | GOV-20261009-gtwpe-pf04 | NON_EPIC | Scope: Reader v2 and errors; repository authority; vendor QA and execution; functional agent governance | Targets: §0.2, §0.4, §2.0, §2.2, §3.3–3.4, §8.1, §9.1.2–9.1.6, §9.7.7, §9.7.9, §9.8.2, §10, §11.1, §12–13, §15.2, Appendices A/B/D | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261009-gtwpe-pf04

````

END OF REDLINES
