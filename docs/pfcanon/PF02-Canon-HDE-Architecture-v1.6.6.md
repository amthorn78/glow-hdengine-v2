# **0\. Front Matter**

**Title:** PF02-Canon-HDE-Architecture  
 **Version:** v1.6.6

 **Status:** Canon  
**Effective date:** 2026-02-09

 **Last Update Gate:** BN 9.8.2 Drain A49-51

**Invocation tag:** INV-f2ac55d77ce9aacc

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

* `engine/` — deterministic compute single-homes (including sampler core and Engine Core); sanctioned seams (for example BodyGraph ingest & refresh) are carved out explicitly in §1.1

* `adapter/` — single HTTP home (Reader, compat v1, internal/dev surfaces)

* `presenter/` — single canonical emitter (used by Adapter and CLI)

* the BodyGraph cache — the persistent store for Engine inputs (DB; not owned here in detail)

**Supersession rule (PF10 addenda).**

Where PF10 includes multiple numbered addenda on the same topic, the later number supersedes earlier guidance. Reference PF10 addenda by **addendum number \+ addendum title** (do not anchor to PF10 file versions or PF10 section numbers). PF02 reflects the latest position and routes work to canonical homes by title only (no version numbers).

**Contract-free.**  
 PF02 never carries headers, payload schemas, status matrices, exit codes, SLAs, or acceptance tables. It describes wiring and flows only; bytes, tokens, and schemas are always owned by other PF documents.

**Section labels.**  
 Each section is tagged with a status label to separate current behavior from near-term goals and future support.

**Routing by title only.**  
 Operational/transport details, CLI/Reader bytes, vendor specifics, QA tokens, and process policy are referenced by title only to their owning documents (for example: HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Schemas & Artifacts, HDE-Mechanics Guide, Glow QA Guide, HDE-Phased Epics, Epic-Process-Guide, Glow Infrastructure).

**Pack/bytes ownership (out of scope here).**  
 Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) are owned outside Architecture and cited by title, primarily in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

**Endpoint Catalog (single home; routing note).**  
Success-endpoint discovery and A7 proofs are catalog-driven. The single home is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256` sidecar. The Catalog is internal-only and env-gated; non-prod entries are unreachable in prod (headers-only env-gate proofs). A7 proofs run only on a cataloged JSON success route; `/internal/version` is excluded from A7 proofs, and PF02 does not define its access-control posture. Titles-only details live in HDE-CLI-API-Vendor-Ref and HDE-Governance; indexing discipline lives in HDE-Schemas & Artifacts. If a given repo state does not yet contain `docs/ENDPOINTS_CATALOG.json`, treat this path as reserved and required; its creation and wiring to A7 proofs are tracked via HDE-Build Checklist and HDE-Phased Epics, not by changing PF02.

**A7 invariants (routing note).**  
 Success proofs require `Vary: Authorization, Accept-Encoding`, strong quoted ETag on 200, HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), and 304 (after prior 200\) omitting both `Content-Type` and `Content-Length`. Encoding-invariance holds: for the same canonical LF-terminated body, the ETag identity and effective `Content-Length` are stable across accepted encodings. Concrete contracts remain in HDE-Governance and HDE-CLI-API-Vendor-Ref.

**DB runtime resolver (routing note).**  
 Resolver semantics are environment-aware:

* **Non-dev:** selection by presence only in this order: `DATABASE_URL → DB_BRIDGE_URL →` typed error (no connectivity probe).

* **Dev:** when `APP_ENV=dev` and `DATABASE_URL` is present but unusable, the resolver falls back to `DB_BRIDGE_URL` and proceeds (keys-only diagnostics; secrets/payloads never logged).

Evidence (headers/records only) is owned by HDE-Mechanics Guide and HDE-Build Checklist and indexed per HDE-Schemas & Artifacts. The full BodyGraph lifecycle flow is described in the System Overview section.

---

## **Change control \[Required-Now\] (titles-only cross-refs; no duplicated bytes)**

**PF02 owns wiring and flows only; all contract bytes, schemas, and tokens are routed by title to their single-home PF documents.**

**Transport / contract bytes.**  
 Owned outside Architecture: HDE-Governance and HDE-CLI-API-Vendor-Ref. Acceptance tokens are single-home in HDE-Governance §2.0. Plans, acceptance artifacts, and step logs MUST NOT mint, invent, or claim unregistered token names. If a token is desired, it MUST be registered first (with semantics) and only then adopted by plans and evidence bindings. Any token name used outside the registry MUST match spelling exactly (no aliases). Evidence-only deliverables (for example, guard proofs or consult records) may be required and evidenced without becoming tokens unless and until Governance registers them as tokens.

**Legacy spelling / alias handling:** any token-like string not present in the HDE-Governance acceptance token roster is non-canonical drift until registered or drained. In particular, `QA_STEP_LOGS_CONSOLIDATED_OK` is a deprecated doc-only alias and MUST NOT be minted; for closure treat it as `QA_HARNESS_DISCIPLINE_OK`. Plans, acceptance maps, and acceptance matrices MUST claim `QA_HARNESS_DISCIPLINE_OK` (exact spelling) and MUST NOT claim `QA_STEP_LOGS_CONSOLIDATED_OK`. If an epic’s evidence mentions the deprecated alias, acceptance artifacts MUST normalize to `QA_HARNESS_DISCIPLINE_OK` and record a doc-delta note per HDE-Governance.

**Canonical JSON / pack / mirror.**  
 Policies, manifest shape, and the Evidence Index/mirror live in HDE-Schemas & Artifacts.

**PR-first posture.**

Epic-Process-Guide governs PR-first cadence. CodEx opens the PR automatically (one PR per epic/slice). Doc-Delta, Appendix D (human), the human Evidence Index (`docs/evidence/INDEX.json`), and the machine mirror (`artifacts/evidence_index.jsonl`) must update in the same PR whenever proofs/artifacts change. When the machine mirror changes, its governed companion files (`artifacts/evidence_index.jsonl.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt`) MUST update in that same PR.

**Doc-Delta artifacts (EPIC024; fixed paths).**  
 For EPIC024, Doc-Delta capture uses two fixed-path artifacts:

* `audit/docdeltas/hde-epic024_doc_deltas.md` (fixed location; governed candidate)

* `audit/qa/hde-epic024/00_meta/doc_deltas.md` (fixed location; governed under epic QA root)

When a Live QA plan includes Step-0B “Doc Delta Capture” (CHECK po-011\_doc\_delta\_capture: PO-011), the step MUST treat these exact paths as the required deliverables and MUST NOT invent alternates. For EPIC024, plan-defined PASS predicates include byte-identity (no diff) and content completeness per the plan’s manual validation obligations (each entry includes PF refs, or explicitly states “no deltas”); the step’s governed primary log is captured at `audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log` (titles-only; detailed criteria remain owned outside PF02).

**Mirror hygiene (titles-only).**

The machine mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, one trailing LF), rejects unknown keys, and each record includes a proof\_anchor to a path-proof stored alongside the artifact. The canonical mirror home is `artifacts/evidence_index.jsonl` with companion `artifacts/evidence_index.jsonl.sha256` and sibling path proof `artifacts/evidence_index.jsonl.path_proof.txt`; any other mirror path strings are non-canonical drift until drained. A human-index hash sentinel may be enforced (see HDE-Schemas & Artifacts).

**Proof-anchor semantics (acceptance bindings).**

 `proof_anchor` points to the governed path-proof transcript for the primary artifact (or bundle) listed in the ledger. Acceptance bindings (for example, token-evidence matrices and acceptance maps) MUST bind tokens to the primary governed artifacts and/or tests, not to the path-proof transcript itself (for example, `*.path_proof.txt`). Proof transcripts are referenced indirectly via the ledger (Human Index entry \+ Machine Evidence Index `proof_anchor`) unless a dedicated evidence family explicitly treats proof transcripts as first-class governed artifacts.

Acceptance maps (when required) are governed artifacts and MUST use the canonical path-of-record `docs/acceptance_map_epic<NNN>.json` with sibling path proof `docs/acceptance_map_epic<NNN>.json.path_proof.txt` (titles-only; see Glow Infrastructure). Alternate acceptance-map filenames/locations are non-canonical drift until drained. For EPIC024, the canonical acceptance map file is `docs/acceptance_map_epic024.json`.

**Math semantics.**  
 Idempotence (preimage recipe), ordering, banding, and scoring live in HDE-Math-Spec.

**Enforcement & CI.**  
 Jobs, guards, allow-lists, and evidence procedures live in the HDE-Mechanics Guide.

**Infrastructure.**  
 Names/locations live in Glow Infrastructure; operational evidence/policy remain owned by HDE-Governance.

**Freeze-pack linkage (release identity).**  
 Release identity is pack-derived from the Freeze-Pack Manifest SoT at `catalog/manifest.json` (canonical bytes). `artifacts/math/freeze_pack_manifest.json` is a governed evidence copy of that manifest and MUST be byte-identical; it MUST NOT be treated as an alternate manifest contract or as a separate identity input. Any change to frozen constants, the direct Motor→Throat set, thresholds, or catalog membership/order requires an HDE-Schemas & Artifacts manifest update and yields a new `release_id` (titles-only).

**Endpoint proofs & ops exclusion (routing).**  
 A7 proofs run only on a cataloged Endpoint Catalog (JSON success) route (HDE-CLI-API-Vendor-Ref); `/internal/version` is excluded from A7 proofs and is not A7-eligible, and PF02 does not define its access-control posture (titles-only to HDE-Governance).

**No invented entrypoints (MUST).**  
 A plan MUST NOT require an executable surface (script/module/CLI) unless it is either: (a) repo-proven (exists in the checked-out workspace), (b) canon-defined (by title) as an entrypoint for the step, or (c) explicitly created by the plan as an ephemeral helper under `/tmp` (execution-only; never evidence). Command provenance MUST be treated like path provenance: plans MUST NOT invent wrapper entrypoints (for example `python -m hde.qa.check_*`) to simulate missing tooling.

**Evidence roots are not code roots.**  
 Plans MUST NOT treat `audit/**` or `artifacts/**` as import roots, executable entrypoint locations, or script roots. They are evidence roots.

**Preflight existence check (MUST).**  
 Any step that invokes a repo-proven entrypoint MUST include a preflight existence check that proves the entrypoint exists (importable module, existing executable file, etc.). If the entrypoint does not exist, the step MUST be classified as TOOLING\_BLOCKED, the failure transcript MUST be captured in the primary log, and execution MUST stop (do not fabricate replacement entrypoints).

**Live QA Moon Loop (allowed; bounded).**  
 Live QA may include a small in-session remediation loop to unblock a check when the failure is a tooling/setup mismatch or an expectation mismatch with canon.

**Hard boundary (no scope expansion).**  
 Moon Loop changes MUST be the smallest local fix necessary to unblock the already-scoped check. Do not add features, expand acceptance, redesign architecture, or introduce new governed deliverable families/paths.

**Required evidence (MUST, if used).**  
 In the primary log, capture: (1) the failure signature, (2) a remediation note naming exactly what changed (file paths) and why, and (3) the successful re-run output. If repo files changed, also write a minimal delta artifact under `audit/qa/<epic-id>/remediation/moon_loop/`:

* `patch.diff` — unified diff of changes

* `changed_files.txt` — file paths and sha256 hashes

Delta capture MUST NOT include VCS workflow content (branches/commits/PR mechanics); it is an evidence record only.

**Stop condition.**  
 If remediation cannot remain minimal (multiple files, broad refactor, or scope expansion), stop Moon Loop and escalate to a normal remediation plan.

**Narratives routing (titles-only).**  
 Reader remains narrative-free. Narrative bytes are carried via Aux/CLI and live in HDE-CLI-API-Vendor-Ref; suppression/A7 policy for Aux lives in HDE-Governance. PF02 stays contract-free.

**Cross-doc referencing.**  
 Use titles only; do not include version numbers.

**Ellipsis prohibition (canonical docs and plans).**

Canonical documents and plans MUST NOT contain any of the following:

* the Unicode ellipsis character (U+2026)

* any instance of three consecutive U+002E FULL STOP characters

This is a prohibited-character rule, not a minor formatting preference. Treat any violation as a mechanical blocker for review acceptance until removed. Review posture: if a viewer or reviewer shows prohibited characters in canonical text, treat it as a read failure until the full source text is visible. If an example would require prohibited characters, do not embed it in the doc or plan: rewrite the example or move it into a repo source file or governed evidence artifact and reference it by path.

When omitted content must be represented, use explicit markers like `[OMITTED]`, `[SNIP]`, `[LIST CONTINUES]`, or `<PLACEHOLDER_NAME>`. For file paths, prefer `<REPO_ROOT>` and explicit placeholders; do not abbreviate paths.

**No contract bytes here.**  
 Any change that would introduce contract bytes or duplicate content is rejected; instead, add or update a titles-only reference to the owning document.

# 1\. Architectural Principles \[Required-Now\]

CLI parity work remains open; Architecture keeps the single-emitter rule while HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide close parity on the CLI path.

## 1.1 Single homes

**engine/** —  deterministic compute single-homes, plus sanctioned seams.

Purity rule (normative). Any module designated as deterministic compute (including sampler core and Engine Core modules) MUST be pure-compute: no time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. Inputs are pure data; outputs are pure data; side effects are forbidden.

BodyGraph seam carve-out (normative). BodyGraph resolution and ingest MAY perform vendor and DB I/O through the DB abstraction as a sanctioned seam, including when implemented under `engine/bodygraph/`. This carve-out does not relax purity requirements for deterministic compute modules

Within `engine/`, the sampler core module and Engine Core module are single homes for their behaviors:

* **Sampler core module** (names-only). A pure-compute module under `engine/` that owns sampler/ranker behavior: pool formation, eligibility, ordering, and sampling decisions. It does not import transport, CLI, HTTP, evidence tooling, or environment.

* **Engine Core module** (names-only). A pure-compute module under `engine/` that owns neutral and directional compatibility metrics, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling. It does not import transport, CLI, HTTP, evidence tooling, or environment.

All runtime surfaces and offline pipelines that need sampler or Engine Core behavior must call these modules in-process; they MUST NOT reimplement sampling or compat logic.

**adapter/** — single HTTP home.  
 Mounts runtime surfaces and applies guards/rails. Calls the Engine (including sampler core and Engine Core modules) in process and never hand-crafts public JSON; only the Presenter’s emitter produces public bytes. No alternate HTTP homes and no duplicate or legacy trees.

**presenter/** — single byte-authoritative emitter entrypoint.

One allow-listed emitter entrypoint symbol produces canonical public JSON bytes for all callers (HTTP and CLI). Wrapper envelope builders MAY exist (for example Reader v1 envelope emission), but they MUST delegate byte emission to the allow-listed emitter entrypoint and MUST NOT introduce alternate serializers on public paths.

**BodyGraph cache** — persistent Engine input store (names-only).  
 The BodyGraph cache (database) is the single persistent store for BodyGraph inputs to the Engine. Adapter/CLI read and write BodyGraphs through the DB runtime resolver; Engine remains stateless with respect to source. The lifecycle of BodyGraph data (vendor fetch, cache, refresh) is described in the System Overview; DB instance and schema names live in Glow Infrastructure.

**Guards (normative).**

* Deny-list legacy trees: `core/`, `server/`, `adapters/` (plural) and any alternate HTTP homes; CI must fail on imports from these paths.  
* Single-emitter allow-list: only the Presenter’s emitter entrypoint may serialize public bytes; all other serializers are forbidden on public paths.  
* No ad-hoc serialization on public paths: forbid direct `json.dumps(<ARGS>)`, `jsonify(<ARGS>)`, templating, or string-built JSON.  
* Role boundaries: Adapter owns route registration and transport wiring; Presenter owns emission. Deterministic compute modules (including sampler core and Engine Core modules) own math and pure-compute behavior. The BodyGraph seam owns vendor fetch and cache refresh and MAY perform vendor and DB I/O through the DB abstraction. No cross-role leakage.  
* **Repo layout note (HTTP surfaces).** Single HTTP home means the adapter component owns route registration, guard rails, and surface mounting. Multiple `create_app` implementations MAY exist for dev harnesses or wrappers, but production startup MUST delegate to one canonical adapter app factory entrypoint to avoid divergent route mounting. Implementation may temporarily host some HTTP handlers in modules outside the `adapter/` directory, but Architecture still treats all HTTP entrypoints as belonging to the adapter component. There MUST NOT be a second HTTP home: new or refactored HTTP surfaces must converge under adapter responsibilities and must not bypass adapter-level guards or the single Presenter emitter.

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

For mirrored surfaces, the CLI emits Reader v1 bytes only via a dedicated reader-dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**). When the CLI emits Reader v1 bytes in that mode, those bytes MUST be byte-identical to the Reader 200 body for the same normalized inputs (single emitter). CLI stdout is not assumed to be Reader v1 bytes; admin and test compat payloads (for example `showcompat`) may be emitted on stdout and may include numeric scores and weights.

**AB↔BA parity.**  
 For the same pair of inputs in either order, the public bytes are identical (pair normalization).

**Two-run identity.**  
 Re-emitting the same logical representation produces byte-identical output.

**Locale pins (required).**  
All canonicalization and compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. These are the canonical determinism pins for governed bytes and evidence. Do not add non-canonical environment variables (for example, `PYTHONHASHSEED`) as required rails or determinism pins for Live QA plan approval or execution. If any QA step or repo tool produces nondeterministic output due to hash-order dependence, fix ordering explicitly (sort keys, sort lists, avoid unordered set iteration) rather than relying on interpreter knobs. If `PYTHONHASHSEED` is ever used, treat it as diagnostic-only and non-governed.

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

Only the presenter’s emitter entrypoint MAY serialize public bytes. All other serializers and any ad hoc `json.dumps(<ARGS>)`, `jsonify(<ARGS>)`, templating, or string-built JSON on public paths are FORBIDDEN.

### **Routing (titles only)**

Concrete guard checks and scripts live in **HDE-Mechanics Guide**, and process/PR workflow (CodEx staging, PR-first merging, repo-docs/Evidence Index updates) lives in **Epic-Process-Guide**.

---

## **2.2 High-level flow (request → compute → persist → emit)**

This subsection defines the **generic architecture template** for how requests move through the Engine. It is the pattern specialised later by:

* BodyGraph lifecycle (§2.4)

* Compat requests (§3.1–§3.3)

* Offline determinism/evidence flows (§5.3–§5.4)

* Narratives (§3.6–§3.7)

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

   * Detailed BodyGraph behaviour is described in §2.4 and in **HDE-Schemas & Artifacts** and **HDE-Governance** by title.  
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

     * Write the command’s **success payload** to **stdout** (exact bytes; one LF).

     * If the CLI is configured to emit **Reader v1 bytes** for parity, those Reader bytes are written to a dedicated **dump sidecar output** (titles-only; see **HDE-CLI-API-Vendor-Ref**). Stdout remains the command’s success payload.

     * Typed JSON errors go to **stderr**; a successful command never writes to stderr.  
   * **Adapter:**

     * Return the same bytes to the client.

     * Error surfaces use typed JSON.

9. For mirrored surfaces, **Reader↔CLI parity holds**: both consume the same Engine modules and Presenter emitter and must produce **byte-identical public output** for identical inputs.

---

### **2.2.1 Alpha surfaces**

Compat v1 via Adapter, plus `showcompat` in CLI, both use the same Presenter emitter path over Engine Core outputs.

For mirrored compat surfaces:

* Output must be non-empty canonical JSON.  
* `showcompat` stdout is a compat payload (admin/test surface) and may include numeric scores and weights.  
* Reader v1 bytes are the numeric-free public success envelope and are emitted by the Reader success route. When the CLI emits Reader v1 bytes for parity, it does so via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).  
* Byte identity for “Reader↔CLI parity” refers to the Reader 200 body vs the CLI’s dumped Reader v1 bytes for the same normalized inputs (single-emitter rule). It does not refer to `showcompat` stdout.  
* The compat request flow is detailed in §2.4 (Reader/CLI → Engine Core → Presenter) and remains contract-free; concrete shapes and tokens live in **HDE-CLI-API-Vendor-Ref**, **HDE-Math-Spec**, and **HDE-Schemas & Artifacts** by title.

---

### **2.2.3 Proofs & routing (titles-only)**

**Policy.**  
 PF02 describes **where** and **how** proofs attach to the architecture but keeps all proof bytes out of Architecture. A7 and other transport-level proofs are routed by **title only** to their single homes; PF02 remains contract-free.

**Success-endpoint proofs (A7).**

* A7 proofs run only on a **cataloged JSON success route** named in the Endpoint Catalog (`docs/ENDPOINTS_CATALOG.json` and its `.sha256` sidecar).  
* The Catalog is internal-only and env-gated; evidence must show that non-prod entries are **unreachable in prod** (headers-only env-gate proof).  
* `/internal/version` is **not A7-eligible**. PF02 does not define its access-control posture (public vs operator-network gated vs auth-header required) **or** the expected failure mode when access is missing/invalid.  
* Endpoint naming, exposure posture, and validator details live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**

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

* `/internal/version` is excluded from A7 proofs and is not A7-eligible; PF02 does not define its access-control posture.  
* Ops behaviour and headers are governed in **HDE-Governance §10.5**.

**Public envelope construction & schemas.**

* The public envelope (six-key **Reader v1** envelope, bands-only, numeric-free) and its schema live in **HDE-CLI-API-Vendor-Ref** and **HDE-Schemas & Artifacts**. When the CLI emits Reader v1 bytes for parity, it does so via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).

* PF02 treats them as contract surfaces and refers to them by title only.

**Idempotence & math.**

* The idempotence preimage recipe, ordering, banding, and scoring semantics live in **HDE-Math-Spec**.

* Architecture requires that all public bytes emitted by Presenter honor those semantics; it does **not** redefine them here.  
---

## **2.3 What this document does not contain (route by title)**

PF02 is **intentionally contract-free**. It names components, flows, and invariants, but it does **not** define transport or policy bytes.

This section is a short reminder only. The complete non-goals list and titles-only routing for those topics is consolidated in §2.5.

PF02 does **not** carry:

* HTTP header matrices, caching or writers rules, conditional delivery (200/304/HEAD), error envelope schemas, or auth policy.

* CLI command bytes, exit codes or streams, admin sidecar formats, or payload field examples.

* Vendor request or response shapes, timeouts or retries, or rate-limit behaviour.

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

* **GET (probe-only):** health-only probing. It MUST NOT compute compat and MUST NOT include a JSON body.

* **POST (compute; internal/admin):** the only method that computes compat. Expects a valid pair definition and viewer preferences that are:

  * well-formed

  * complete (all ten Magic-10 keys)

  * within allowed ranges

* **Endpoint Catalog binding (high level):** the Endpoint Catalog entry for `/api/compat/v1` binds the POST compute surface and MUST include a non-empty env gate field. Env-gate proof is headers-only.  
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

**Reader route posture (route-only).**

* **Canonical route:** `GET /reader` is the canonical Reader route for the v1 dev/proof surface.

* **Version selection:** Reader v1 is selected via query parameter `v=1` on the Reader route; the route path does not change for v1 selection.

* **Optional `/api` mount alias:** when the Reader blueprint is mounted under an `/api` prefix in a given runtime configuration, `/api/reader` is an alias of the same Reader surface (not a distinct contract or separate proof surface).

* **No invented reader-proof path:** there is no `/api/reader-proof/v1` route. Treat references to that path as drift and correct them to the canonical Reader route (`/reader`, or `/api/reader` only when that is the configured mount).

* **Proof-surface selection:** any proof that depends on a Reader success route must reference the actual reachable Reader route for the target environment. Do not invent alternate proof routes. When an Endpoint Catalog is used, select the proof route from catalog entries that correspond to real mounted routes.

* **Scope note:** this posture records canonical Reader surface routing for planning and QA and does not introduce new routes or restate public contract bytes.

**A7 proof surface (route-only; titles-only).**

* **Cataloged route only.**  
  Reader success proofs run only on a cataloged JSON success route named in the Endpoint Catalog (HDE-CLI-API-Vendor-Ref). The Catalog’s single home is `docs/ENDPOINTS_CATALOG.json` (+ `.sha256` sidecar). The `.sha256` sidecar must reference `docs/ENDPOINTS_CATALOG.json` for repo-root verification. Proofs target a route listed there; `/internal/version` remains excluded. In EPIC025, the selected proof route is `/reader` (dev-harness internal), env gated to dev (`APP_ENV=dev`), and marked A7-eligible. Env-gate proof is mandatory (headers-only).

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
HDE-Governance governs invariants for the identity surface (for example, no-store, no ETag, HEAD 200 with `Content-Type` parity and `Content-Length == identity GET`, conditionals ignored / never 304\) and owns the identity-surface acceptance/evidence posture. PF02 points by title only.

**Evidence & indexing (titles-only).**  
 Proof artifacts and success-endpoint snapshots are indexed per **HDE-Governance** / **HDE-Schemas & Artifacts**; the human Evidence Index and the machine JSONL mirror must remain 1:1 (updated in the same PR).

For `/internal/version` coupling \+ two-run identity, the governed proof surface is the internal\_version evidence bundle under `artifacts/ops/internal_version/`. Canonical member filenames (and any explicitly permitted alias files) are owned by HDE-Schemas & Artifacts and governed by HDE-Governance; ad-hoc filename variants are prohibited. PF02 names this evidence surface for architectural traceability and continues to route all token semantics and detailed proof formats by title to their single-home documents.

**Non-goals.**  
 No public contract bytes, no payload schemas, no alternate emitters, no persistence, and no vendor/network calls from this surface.

**Routing (titles-only).**

* Identity invariants, acceptance, and evidence posture **→ HDE-Governance**

* Endpoint Catalog / success JSON → **HDE-CLI-API-Vendor-Ref**

* Canonical JSON and machine mirror → **HDE-Schemas & Artifacts**

  ---

## **3.6 Aux Narrative (concept-only, route-only) \[Speculative\]**

**Role.**  
 Serve deterministic narrative text **outside** the public Reader surface. No narratives appear on Reader 200\.

**Responsibilities (conceptual).**

* Adapter wires the Aux route (`/aux/narrative`); Presenter emits text via the single canonical emitter; Engine remains pure compute (keys only).  
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
  `/internal/version` is excluded from A7 proofs and is not A7-eligible; PF02 does not define its access-control posture.

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

* Authoritative path: object storage at `/narratives/<pack_sha>/<OBJECT_KEY>`; the repo carries the manifest \+ evidence.

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
* **Compat CLI surfaces** (as described in **HDE-CLI-API-Vendor-Ref**) for terminal-based compat flows. CLI stdout may be an admin/test compat payload (for example `showcompat`). When Reader-identical bytes are required for parity proofs, the CLI emits Reader v1 bytes via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).  
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
* **Reality Audits (components \+ canonical pathnames/loci; planning input)**  
* **Glow QA Guide** (Codespaces QA configuration and execution rails)  
* “GitHub Codespaces in a QA Workflow” (where relevant)

to determine how to start and reach Reader and other services.

HTTP QA against “Reader” or dev harness surfaces is considered misconfigured if there is **no running adapter/Reader process** discoverable through the documented commands and ports. Attempts to hit guessed URLs or ports are a plan defect, not a property of the Engine or Presenter.

* **Codespaces Live QA posture (routing note).** Codespaces QA configuration and requirements are single-home in the **Glow QA Guide** (names-only; secrets recorded as presence-only, never values). A standalone Step-0 “Codespaces snapshot” artifact is **not required** and MUST be treated as optional and non-gating; plans MUST NOT require, validate, or gate approval on it.   
* **Environment variable discipline (Live QA).** Environment variable names MUST be treated as governed interface surfaces (like repo paths and endpoints), not free-text fields. QA plans, QA runbooks, and QA evidence schemas MUST NOT introduce, require, or depend on any `MODO_*` variable names for PASS or FAIL or required evidence structure; any `MODO_*` strings are non-canonical and inert.  
  * **No QA-time env var minting (hard).** New environment variable names MUST NOT be introduced during Live QA (including Moon Loop). If a QA step would require a new environment variable name to function, treat it as development work under PO approval and canonize the variable name before any plan depends on it.  
  * **Review posture (mechanical blocker).** Any unapproved environment variable name used as a required input, required header key, required manifest key, or required evidence schema key is a mechanical blocker for plan approval. Fix by removing it or replacing it with canon-approved variables only.  
  * **EPIC025 exception (grandfathered; non-binding only).** If the already-approved EPIC025 Live QA Plan references `MODO_*` keys, treat those keys as inert placeholders: they MUST NOT be required for PASS or FAIL, MUST NOT be required evidence keys, and MUST NOT be used as proof of rails posture or execution configuration. This exception MUST NOT be replicated in new plans.  
* **KISS required outputs (Live QA).** Live QA Plans MUST minimize required outputs to:  
  * one primary step log per check under `audit/qa/<epic-id>/checks/<check_id>/primary.log`, and  
  * the QA step-logs manifest at `audit/qa/<epic-id>/qa_step_logs_manifest.json` listing check IDs, status, and primary log paths (every referenced primary log path MUST exist under `audit/qa/<epic-id>/` at review time), plus its sibling path proof `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`  
  * Nothing else is auto-required unless canon explicitly pins a governed evidence family/path. Any additional required artifact MUST be acceptance-decisive and MUST be canonized (PF10 or PF-Canon) as a governed evidence family/path.  
  * **Step-log header normalization (KISS).** Every `primary.log` MUST begin with a JSON header object that includes: `check_id`, `status`, `command`, `captured_env`, `pf_refs`, `intended_tokens`, `claimed_tokens`. The three list fields MUST be present; empty lists (`[]`) are allowed and SHOULD be used when no refs/tokens are in play. If any required list field is missing, treat it as an evidence-format gap; a reviewer-of-record MAY mechanically normalize the header by inserting missing empty lists and re-serializing the header as canonical JSON (no step rerun required). Token claims are never inferred: if `claimed_tokens` is missing or empty, token claims are treated as none. Status vocabulary remains gating (PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED).  
  * **Step-log header writer exports (per-check).** If a Live QA plan uses a step-log header writer that reads per-check metadata from environment variables, the plan MUST export the complete required set immediately before header generation for each check and MUST NOT rely on prior step state.  
    * Minimum per-check exports (names are governed by the writer contract): `CHECK_ID`, `CHECK_NAME`, `PASS_FAIL`, `COMMANDS_JSON`, `ARTIFACTS_JSON`, `PF_REFS_JSON`.  
    * Live QA handling (evidence-capture only): if a check ran successfully but `primary.log` is missing a required JSON header or contains incorrect check metadata due to missing exports, a reviewer-of-record MAY apply a minimal Moon Loop deviation to (1) export the required header vars, and (2) regenerate the JSON header and reassemble `primary.log` by prepending the corrected header while preserving the existing body verbatim.  
    * Anti-drift: plans MUST be internally consistent. Do not mix patterns where one check exports header variables and another does not while still calling the same header writer.  
  * **Prefer validating canon evidence over generating QA artifacts.** By default, if PF10/PF-canon already establishes an artifact family/path, the Live QA plan validates it (exists \+ minimal posture checks) and records PASS/FAIL in the check’s `primary.log`. QA creates new artifacts only when the check itself is about QA-run outputs (primary logs, step-logs manifest) or when canon explicitly requires a generated QA artifact. If a plan requires an EPIC-scoped derived artifact path to satisfy a predicate, the artifact MUST be mechanically derived from the canonical surface and MUST be treated as evidence-only (not a new governed evidence family/path) unless and until canon explicitly pins it.  
  * **Showcompat QA: vendor rails and arguments.** Current limitation: `showcompat` requires vendor-sourced BodyGraph data to compute compatibility. When a Live QA step executes `showcompat` and BodyGraph data is not already available, that step MUST run with vendor rails open (network allowed) so the vendor seam can be called. Treat closed network rails as an expected blocker for functional `showcompat` runs under this limitation.  
    * The rails change MUST be explicit and scoped only to the `showcompat` step(s); restore default rails posture after the step.  
    * `showcompat` MUST NOT be executed as a zero-argument command in QA plans or QA runs. Follow the authoritative command and argument contract in **HDE-CLI-API-Vendor-Ref**.  
  * **No planning-trace deliverables (PF23).** Reality Audits (PF23) are post-epic audits (a closed-epic snapshot), not an in-flight PR truth source. PF23 MAY be consulted during epic planning, implementation planning, and QA planning to ground component boundaries and canonical loci, but plans and reviews MUST NOT treat PF23 consult as a required deliverable, a required check, or an acceptance token. Do not instruct the operator to run commands solely to “prove PF23 consult.”  
    * A plan MAY include a single “PF23 Anchors” note (components consulted and loci touched), but it is informational only and MUST NOT appear as a required check or required evidence output.  
    * If any PF23 Reality Audit statement contradicts PF canon, record it as an explicit drift item requiring adjudication. Do not resolve contradictions by assumption.  
    * Record each contradiction as a set:  
      * PF23 claim (verbatim quote)  
      * Canon claim (verbatim quote plus PF canon citation)  
      * Impacted epic or surface  
    * Classify each contradiction into exactly one bucket pending adjudication:  
      * Canon defect (PF canon is wrong or incomplete)  
      * Implementation drift (repo or runtime deviates from canon)  
      * Necessary reality shift (PF canon must be updated to reflect ground truth)  
    * Adjudication is owned by the PO, who decides whether the resolution path is a canon update, implementation remediation, or a formalized exception with a canon follow-up.  
  * **No VCS workflow content (hard).** Live QA Plans MUST NOT instruct or discuss branches, commits, PRs, or any other VCS workflow steps, and MUST NOT gate PASS/FAIL on VCS state (for example “working tree clean” or “on correct branch”). Read-only, non-mutating git commands are allowed only as optional, non-gating repo-root sanity checks and must not rely on branch names, commit SHAs, or PR identifiers.  
  * **Objective-first Live QA plans.** Live QA Plans MUST specify objectives and proof obligations per step (required evidence outputs and explicit PASS or FAIL predicates) and MUST NOT require syntax-perfect command strings.  
    * Steps SHOULD use general command-line directives rather than brittle verbatim command text; execution-time command resolution and the recorded command transcript in `primary.log` are authoritative.  
    * Reduce plan brittleness by minimizing locus strings (paths, test filenames, long command fragments) unless the locus is canon-defined or is a fixed-path obligation; when a plan must assert a locus, the repo-loci proof gate still applies.  
    * Moon Loop may be used to remediate syntax and quoting mismatches, but MUST NOT change objectives, loci exercised, required outputs, or PASS or FAIL predicates.  
  * **No fabricated paths (MUST).** Planning documents and plans MUST NOT fabricate repo file paths, directory roots, or module loci, whether the path is asserted as required evidence or as an “expected locus” in narrative text.  
    * Every asserted path or “where this lives” statement in a plan MUST be validated using exactly one of the following methods:  
      * direct PF canon citation (preferred)  
      * `CA vetted`: a verbatim quote from the planning Codex audit included inline in the plan  
      * `IG Approved`: a verbatim quote from the Implementation Guide included inline in the plan  
    * If a plan uses `CA vetted` or `IG Approved`, the supporting quote MUST be verbatim. Paraphrase is not permitted for these labels. Review gate: any unvalidated locus claim is a mechanical blocker until corrected  
    * Mandatory consult before asserting implementation loci (paths, surface roots, directories): consult HDE Architecture and Reality Audits at minimum. Plans MUST align expected loci to these touchpoints and MUST NOT introduce alternate roots by assumption (example: do not assume a `src/` tree exists).  
    * File minting is allowed and expected: new files and directories MAY be created under canon-defined homes once the locus is validated. New roots and second homes MUST NOT be assumed; they require explicit justification aligned to single-home constraints.  
    * Planning Codex audit portability: a planning Codex audit may be referenced inside plan narrative only via verbatim quotes; it MUST NOT be referenced in the final instructions given to Codex for implementation. Implementation prompts MUST be self-contained, relying only on PF canon references and repo paths.  
    * Evidence output clarity: plans SHOULD name primary governed evidence outputs by exact path and filename and SHOULD avoid vague family phrases or wildcards in evidence-output lines. If a tool produces a high-churn set of member logs, prefer a single primary governed artifact (for example, a manifest or bundle) that enumerates or references members, provided canon supports the surface and the evidence binding remains deterministic.  
    * A plan MUST NOT reference a file path as required unless it is canon-defined, audit-proven (for example via a governed manifest, Evidence Index/Mirror entry, or canonized proof transcript family), or explicitly QA-created by the plan with exact mkdir/write instructions, a one-line purpose, and explicit PASS and FAIL predicates tied to file contents.  
    * Governed evidence artifacts used to decide PASS/FAIL MUST be written under a concrete lowercase path under `audit/**` (preferred) or `artifacts/**`.  
    * QA agents MAY create ephemeral helper scripts under `/tmp` during Live QA execution, but `/tmp` scripts and outputs are execution-only: they MUST NOT be treated as deliverables or evidence, MUST NOT be indexed/mirrored, and MUST NOT be referenced as acceptance binding surfaces. `/tmp` helpers must not print or persist secrets (presence-only or redacted where applicable).  
    * Plans MUST separate pre-existing artifacts (required to exist before execution) from QA-run artifacts (created during execution); preflight presence checks may gate only on pre-existing artifacts.  
    * If a deliverable family/path is not canonized, the plan MUST treat it as non-gating posture-only (for example, log `UNPROVEN` / `TOOLING_BLOCKED`) and MUST NOT introduce new required paths to simulate it.

**Routing (titles-only).**

* Live QA Plan template structure and step-log header schema (minimum) → Plan Templates  
  Codespaces QA configuration, required pins/variables (names-only), and execution rails → Glow QA Guide  
* Service start commands, ports, and environment wiring for dev/QA consoles → **Glow Infrastructure**, **HDE-Mechanics Guide**  
* Live QA process, discovery baselines, and rails posture → **Epic-Process-Guide**, **Glow QA Guide**  
* CLI and Reader surface bytes, request/response shapes, and admin surfaces used for Live QA → **HDE-CLI-API-Vendor-Ref**

# **4\. Boundaries & Contracts (Conceptual) \[Required−Now\]**

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

  * Compat v1, Reader v1, dev sampler harnesses, and offline determinism/evidence pipelines all route through the same Engine Core and sampler core modules; no surface is allowed to fork or reimplement core math. Differences are in rails, environment, and evidence policy only (owned in other PF docs by title).

**Adapter → BodyGraph source (env-aware).**  
 **Prod:** request path **does not** call vendor; BodyGraph comes from **DB**; refresh is **out-of-band** (policy by title).  
 **Dev:** direct vendor allowed; on success, **upsert** to DB.  
 Adapter and CLI follow the **BodyGraph lifecycle** in §2.4 to decide when to read from DB vs call vendor and refresh. Engine remains stateless with respect to source and always consumes normalized BodyGraph inputs. Offline determinism and evidence pipelines respect the same boundary: they work with DB-backed or fixture BodyGraphs and never call vendor directly; rails/guards, evidence families, and indices live in their single homes (**HDE-Governance**, **HDE-Schemas & Artifacts**, **HDE-Mechanics Guide**, **Glow QA Guide**, **HDE-Phased Epics** by title).

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

* The **Machine Evidence Index** at `artifacts/evidence_index.jsonl`, a records-only, canonical JSONL mirror of the ledger. The mirror has a companion sha256 sentinel at `artifacts/evidence_index.jsonl.sha256` and a sibling path-proof transcript at `artifacts/evidence_index.jsonl.path_proof.txt`. Each record includes a `proof_anchor` field pointing to a path-proof transcript maintained alongside the governed primary artifact. Any other mirror path strings are non-canonical drift until drained.

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

* **EPIC025 evidence discipline surfaces (addenda 14–16, 42–48).** EPIC025 records repo-proven evidence-discipline gate entrypoints and closure surfaces under a dedicated QA evidence root (names and paths only; schemas and tokens remain owned outside PF02 by title).  
  * Repo-local gate entrypoints (tools).  
    * `tools/evidence/check_lf_endings.py` — wrapper for `ci/checks/check_final_lf.sh` executed under determinism env pins; captures its primary log at `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log`.  
    * `tools/evidence/validate_evidence_paths.py` — validates evidence-index path bindings by loading `artifacts/evidence_index.jsonl` and verifying each record’s resolved physical path is safe and exists. Minimum safety rails: reject traversal segments and require repo-root containment after resolution; require each JSONL line to parse as a JSON object before field inspection. Captures its primary log at `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`.  
  * Normalized QA evidence root (EPIC025).  
    * QA step-logs manifest: `audit/qa/hde-epic025/qa_step_logs_manifest.json` mapping check IDs to `primary.log` paths, with sibling path proof `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`.  
    * Gate and preflight logs are organized under `audit/qa/hde-epic025/checks/` with `gate_*` and `preflight_*` families; on success, gate `primary.log` transcripts record an exit status (0) and a compact output summary.  
    * Plan check step directories are organized under `audit/qa/hde-epic025/checks/po-0NN/` (for example: `po-008`, `po-009`, `po-010`, `po-011`, `po-012`, `po-013`) with a per-step `primary.log` plus step-specific artifacts (names and paths only).  
      * A7 proof snapshots (example): `audit/qa/hde-epic025/checks/po-008/success_head.txt`, `audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256`, `audit/qa/hde-epic025/checks/po-008/success_get.txt`, `audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256`.  
      * Canonical JSON gate transcript capture (example): `audit/qa/hde-epic025/checks/po-009/canonical_json_gate_stdout.txt` with `audit/qa/hde-epic025/checks/po-009/canonical_json_gate_stdout.txt.sha256`.  
      * Determinism env pins and sanity pipeline transcripts (example): `audit/qa/hde-epic025/checks/po-010/env_pins.log` (+ `.sha256`), `audit/qa/hde-epic025/checks/po-010/env_pins_check_stdout.txt` (+ `.sha256`), `audit/qa/hde-epic025/checks/po-010/sanity_pipeline_stdout.txt` (+ `.sha256`).  
    * Endpoint catalog and index snapshot artifacts (example): `audit/qa/hde-epic025/checks/po-012/endpoints_catalog.json` (+ `.sha256`), `audit/qa/hde-epic025/checks/po-012/index.sha256` (+ `.sha256`).  
  * Epic-scoped meta artifacts for deferred execution posture are stored under `audit/qa/hde-epic025/00_meta/`. Example: `audit/qa/hde-epic025/00_meta/deferred_scope_posture.md` with check-scoped sha at `audit/qa/hde-epic025/checks/po-013/deferred_scope_posture.md.sha256`.  
  * Epic closure record: `audit/qa/hde-epic025/epic_closure_record.md` with sibling `audit/qa/hde-epic025/epic_closure_record.md.sha256`. If later checks are intentionally not executed, the closure record may mark checks as NOT RUN instead of listing file-path evidence pointers to missing step logs (prevents dangling links at time of writing).  
* EPIC025 close-pack artifacts (mechanically generated).  
  * Close-pack pair: `audit/EPIC-025_MANIFEST.json` and `audit/EPIC-025_close_report.md`.  
  * Close-pack pair path-proof siblings: audit/EPIC-025\_close\_report.md.path\_proof.txt and audit/EPIC-025\_MANIFEST.json.path\_proof.txt (required siblings; titles-only; see Glow Infrastructure).  
  * Doc-delta closeout artifact: `audit/docdeltas/hde-epic025_doc_deltas.md`.  
  * Canonical JSON gate output path proofs live under `audit/gates/json_gate/canonical/` with sibling `.path_proof.txt` transcripts.


* **EPIC024 QA runner provenance notes (addenda 14–29).** The following runner/path mismatches were observed in PASS-grade EPIC024 Live QA evidence and are recorded here to prevent plan drift:.  
  * **D09\_generate\_evidence\_index\_snapshot** — plan-named runner `python tools/evidence/run_evidence_index_snapshot.py`; observed runner `python tools/evidence/run_evidence_index_snapshot_gate.py`.  
  * **D13\_acceptance\_map\_viability** — plan-named runner `python tools/evidence/run_acceptance_map_viability.py`; observed runner `python tools/evidence/run_acceptance_map_viability_gate.py`.  
  * **D14\_harness\_selftest** — plan-named runner `python tools/evidence/run_harness_selftest.py`; observed runner `python tools/evidence/run_harness_selftest_gate.py`.  
  * **D16\_close\_pack** — plan-named runner `python tools/evidence/run_close_pack.py`; observed runner `python tools/evidence/run_close_pack_gate.py`.  
  * **D04\_sampler\_evidence** — plan posture is review-only ("Commands: None required"), but PASS-grade evidence includes generation via `python tools/evidence/run_sampler_evidence.py`. Plan-required fixed outputs: `artifacts/sampler/epic024/sampler_evidence.json`, `artifacts/sampler/epic024/manifest.json`; primary log: `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`  
  * **D07\_sanity\_pipeline** — plan command `python tools/evidence/run_sanity_pipeline.py`; observed operator entrypoint `python tools/evidence/run_sanity_pipeline_gate.py` (wrapper). Gate surface: `audit/gates/sanity_pipeline/sanity_pipeline.log`; primary log: `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`..  
  * **D08\_cli\_guardrail** — plan-required deliverable `cli/main.py` was validated at repo path `engine/cli/main.py` (architectural alias). An extra wrapper script `tools/evidence/run_cli_guardrail.py` was created to match EPIC024 evidence patterns (not a plan-required deliverable). Primary log: `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log`.  
* **EPIC024 validator/check family surfaces & named-report drift (addenda 19–31).** The following check-family directories and fixed-path outputs are part of the EPIC024 governed evidence surface (paths only; no schemas):  
  * **PO-006 token registry validity (`PO-006`; plan step: `po-006_token_registry_validity`).** Closeout posture: recorded as FAIL\_BEHAVIOR (deferred blocker) when acceptance-map tokens are missing from the registry. Report-only folder surfaces observed in EPIC024: `audit/qa/hde-epic024/checks/PO-006_mirror_compliance/` and `audit/qa/hde-epic024/checks/PO-006_mirror_compliance_reports/` (folder naming drift; do not infer semantics from the directory label).  
  * **`D23 evidence index snapshot.`** `Check dir: audit/qa/hde-epic024/checks/D23_evidence_index_snapshot/ (primary log and evidence_index_snapshot.json).`  
  * **Evidence path binding validation.** Check dir: `audit/qa/hde-epic024/checks/evidence_path_binding_validation/` and fixed report output path: `audit/qa/hde-epic024/00_meta/evidence_path_binding_report.json`.  
  * **QA step-logs manifest refresh.** Check dir: `audit/qa/hde-epic024/checks/qa_step_logs_manifest_refresh/` and fixed output path: `audit/qa/hde-epic024/00_meta/qa_step_logs_manifest.json`.  
  * **D01 env pins gate (`D01_env_pins_gate`).** Plan-required runner `python tools/evidence/run_env_pins_gate.py`; fixed output paths: `audit/gates/env_pins/env_pins_report.json` \+ `audit/gates/env_pins/env_pins_report.path_proof.json`.  
  * **D03 showcompat artifacts (`D03_showcompat_artifacts`).** Plan-required runner: `python tools/evidence/run_showcompat_artifacts.py`; fixed output paths: `artifacts/showcompat/epic024/showcompat_manifest.json` \+ `artifacts/showcompat/epic024/showcompat_symbols.json` and check primary log: `audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log`.  
  * **D04 sampler evidence (`D04_sampler_evidence`).** Fixed outputs: `artifacts/sampler/epic024/sampler_evidence.json`, `artifacts/sampler/epic024/manifest.json`. Check primary log: `audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log`.  
  * **D07 sanity pipeline (`D07_sanity_pipeline`).** Plan command: `python tools/evidence/run_sanity_pipeline.py` (operator entrypoint may be a wrapper; see runner provenance notes above). Gate surface: `audit/gates/sanity_pipeline/sanity_pipeline.log`. Check primary log: `audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log`.  
  * **D08 CLI guardrail (`D08_cli_guardrail`).** Plan command: `python tools/cli/serializer_grep_guard.py`. Guard output log: `artifacts/cli/guards/serializer_grep_guard.log`. Check primary log: `audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log`.  
  * **OPS rerun transcript (remedial OPS-01).** Check dir: `audit/qa/hde-epic024/checks/OPS-01_rerun_transcript/` and fixed transcript path: `audit/qa/hde-epic024/00_meta/OPS_rerun_transcript.json`.  
  * **PO-017 lowercase directory naming (`po-017_lowercase_naming`).** Check dir: `audit/qa/hde-epic024/checks/po-017_lowercase_naming/` (includes `primary.log`, `find_audit_uppercase.txt`, `find_artifacts_uppercase.txt`, `find_docs_uppercase.txt`). Scan posture refinement (EPIC024 evidence): directory names only (`find <value> -type d`); uppercase filenames are allowed unless separately forbidden by canon.  
* **Binding authority order (titles-only).** Canonical artifact paths and sibling naming (including the machine mirror and the path-proof transcript suffix) are owned by HDE-Schemas & Artifacts (SoT). HDE-Mechanics Guide defines CI mechanics and evidence gating but MUST NOT introduce alternate canonical paths that conflict with Schemas & Artifacts. Glow QA Guide defines validator execution semantics and status vocabulary. HDE-Build Checklist defines which checks are required for closure, but it binds to the canonical surfaces defined above.  
* **Validator failure posture (path binding).** If a validator runs and finds the required evidence but at a non-canonical path, classify as FAIL\_BEHAVIOR. If required canonical inputs are missing, classify as TOOLING\_BLOCKED. (Status vocabulary is owned by **Glow QA Guide**.)  
* **EPIC024 closeout caveats and deferred hardening (addenda 30–31).** Closure decision was recorded as SATISFIED with explicit deferral of QA determinism hardening. The items below are recorded here because they impact architecture-level evidence binding and validator determinism (titles/paths only):  
  * **OI-001 — PO-006 token registry validity (blocker-grade).** Recorded FAIL\_BEHAVIOR due to 11 acceptance tokens referenced by the acceptance map not present in the registry. Deferred focus: reconcile acceptance-map token set to the registry and make the validator deterministic.  
  * **OI-002 — Remove rg dependency.** Replace text-grep evidence capture with deterministic parsers (avoid rg missing or grep substitution).  
  * **OI-003 — Acceptance map viability enforcement.** Correct the "phantom pass" bug and ensure the check is harness-correct and gating.  
  * **OI-004 — Evidence index snapshot contract and deprecated-path cleanup.** Enforce the single canonical gate path and reject deprecated snapshot files.  
  * **OI-005 — Evidence path binding validation enforcement.** Add automated validation to enforce PF10 authority order and fail early on deprecated path usage.  
  * **OI-006 — Acceptance-token alias cleanup.** Normalize to canonical token spellings and forbid deprecated aliases in acceptance maps and registries (ties directly to PO-006).  
  * **OI-007 — Re-audit PF23 evidence surfaces.** Capture PF23 audit outputs deterministically (evidence index, machine mirror, catalogs) under governed `audit/qa/hde-epic<NNN>/` paths in the next epic.  
* **Evidence index snapshot artifact family (gates-only; tokenless).** The Evidence Index snapshot is a mechanical PASS/FAIL validator artifact used as closure-proof evidence for D23. It MUST NOT mint or claim an acceptance token unless **HDE-Governance** registers one. The schema and PASS/FAIL predicate are owned by **HDE-Schemas & Artifacts** and **Glow QA Guide**; PF02 records only the surface and routing. Status posture: PASS when the predicate holds; FAIL\_BEHAVIOR when the predicate fails; TOOLING\_BLOCKED when required inputs are missing. Any EPIC-local copies (for example under `audit/qa/hde-epic<NNN>/<RUN_SUBDIR>/evidence_index_snapshot.json`) and deprecated snapshot file paths recorded in PF10 (for example `artifacts/INDEX_SNAPSHOT.json` and `audit/evidence_index_snapshot/evidence_index_snapshot.json`) are non-canonical and MUST NOT be treated as alternate contract surfaces.  
  * **Evidence index snapshot** — Canon surface: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` / Path proof: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`  
* **Canonical JSON gate artifacts (gates-only).** Canonical JSON gate artifacts MUST use the `audit/gates/json_gate/canonical/` family (see **HDE-Mechanics Guide**, **Glow QA Guide**, **HDE-Schemas & Artifacts**). The legacy naming under `audit/gates/canonical_json/<LEGACY_SUBPATH>` MUST NOT be treated as a canonical surface unless explicitly re-registered as such. The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log` (legacy; not a canonical predicate surface).  
  * **Gate check log** — Canon surface: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
    * Path proof: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`  
  * **Gate compare log** — Canon surface: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
    * Path proof: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`  
  * **Gate structured record** — Canon surface: `audit/gates/json_gate/canonical/json_gate_structured_record.json`  
    * Path proof: `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`  
* **Arrays-as-sets report artifact surface (gates-only; tokenless).** Codespaces Live QA evidence shows the arrays-as-sets check produces a stable report artifact at `artifacts/canonical/arrays_as_sets_report.log` (log format). The plan-named report path `audit/gates/arrays_as_sets/arrays_as_sets_report.md` was observed as missing and MUST NOT be treated as a governed predicate surface unless explicitly canonized.  
  * Observed runner (recorded in the D05 `primary.log` header): `python -m pytest tests/compare/test_arrays_as_sets.py`  
  * Plan-named runner (observed missing): `python tools/evidence/run_arrays_as_sets_check.py`  
* **Determinism predicate surfaces lock (ADR-001).** Determinism remediation predicates for **D16–D18** MUST validate the **canonical emitted evidence surfaces** and their sibling **path proofs**, and MUST NOT require wrapper bundles, wrapper schemas, or additional non-canon marker lines.  
  * **D16 (orientation demo)** — Canon surface: `audit/gates/topology/orientation_demo.txt`  
     Path proof: `audit/gates/topology/orientation_demo.txt.path_proof.txt`  
  * **D17 (env pins)** — Canon surface: `audit/gates/determinism/env_pins.log`  
     Path proof: `audit/gates/determinism/env_pins.log.path_proof.txt`  
  * **D18 (sanity log)** — Canon surface: `artifacts/sanity/sanity.log`  
     Path proof: `artifacts/sanity/sanity.log.path_proof.txt`  
* **Path-proof naming is locked.** Canonical sibling transcript naming is `<artifact_filename>.path_proof.txt` (the path proof filename MUST preserve the full surface filename and append `.path_proof.txt`; example: `env_pins.log.path_proof.txt`, not `env_pins.path_proof.txt`). Any mention of `<artifact_filename>.path_proof.json` is non-canonical.  
* **Routing constraint (evidence surfaces & predicate targets).** **HDE-Phased Epics** MUST NOT be cited to define evidence surface paths, evidence shapes, or remediation predicate targets. Plans/remediations MUST cite the owning canon documents by **title** (e.g., **HDE-Build Notes**, **HDE-Build Checklist**, **Epic Process Guide**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Governance**) as applicable.  
* **Ledger-backed evidence bindings.** When an acceptance artifact binds a token to a governed evidence path, that governed path MUST exist in both the Human Evidence Index (`docs/evidence/INDEX.json`) and the Machine Evidence Index (`artifacts/evidence_index.jsonl`), and the mirror record MUST include `proof_anchor`. A governed evidence binding is invalid if the path is missing from either registry.  
* **Guard proofs (evidence-only by default).** Serializer/emitter guard checks MUST emit mechanically produced guard-proof artifacts with a single primary artifact per guard check and an explicit PASS or FAIL classification. Guard proofs do not create new acceptance token obligations unless and until Governance registers tokens and defines semantics. If a guard proof is used for closure wiring (for example referenced by an acceptance map, token-evidence matrix, or close pack), it MUST follow normal governed-evidence discipline (stable path, index/mirror parity, and sibling path-proof transcripts where required).  
* **Index exclusion (remediation-only run-bundle copies).** Any “remediation-only” directory copies captured under `audit/qa/**` for runtime/remediation portability (for example, a `remediation_only/` subtree inside a run bundle) MUST NOT be indexed in `docs/evidence/INDEX.json` or `artifacts/evidence_index.jsonl`. The ledger indexes the primary governed artifacts (and their `proof_anchor`s), not remediation-only bundle copies.  
* **Mechanical-only evidence.** Any file treated as QA evidence (including close artifacts) MUST be mechanically produced from commands and MUST NOT contain manual-fill placeholders (for example, “fill in PASS/FAIL”). If a result is “no deltas,” the artifact MUST say so explicitly (as a produced output).  
* **Same-PR parity.** Whenever proofs or governed artifacts (including bundles and manifests) change, the Human Evidence Index and the Machine Evidence Index MUST be updated **in the same PR** that carries the code/evidence change.  
* Human index proof freshness. The Human Evidence Index (docs/evidence/INDEX.json) and its hash sentinel (docs/evidence/INDEX.sha256) are governed artifacts. Each MUST have a co-located, governed path-proof transcript, and those transcripts MUST be refreshed whenever the index/sentinel bytes change (in the same PR). PF02 records this requirement at the architecture level; concrete proof file naming and the canonical updater/validator behavior are owned by HDE-Schemas & Artifacts and HDE-Mechanics Guide by title.  
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

* Outputs are written into governed evidence families under `artifacts/<EVIDENCE_FAMILY_SUBPATH>`, registered in **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide** (titles only).

* Family names, schema shapes, and path patterns are defined there, not in Architecture.

**Index & mirror linkage.**

Whenever these pipelines produce or regenerate artifacts:

* The human Evidence Index and the machine mirror must be updated in the **same PR**. When the machine mirror changes, its governed companion files (`artifacts/evidence_index.jsonl.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt`) MUST update in that same PR, per **HDE-Schemas & Artifacts** and **Epic-Process-Guide**.

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

A7 transport & ops policy (ETag/200, 304 header omissions, HEAD parity, Vary: Authorization, Accept-Encoding, encoding-invariance, writers no-store/no ETag, /internal/version identity endpoint posture (excluded from A7 proofs), acceptance tokens) → **HDE-Governance**.

QA tokens & D-goals (Live QA token semantics, rails posture, and per-epic D-goal records and acceptance conditions) → **Glow QA Guide** and **HDE-Phased Epics**.

Guards & ops how-to / CI (capture scripts, serializer path allow-lists/denylists, dev-harness ops posture, PR-first workflow with CodEx-opened PR and same-PR Evidence Index updates) → **Epic-Process-Guide** and **HDE-Mechanics Guide**.

Infrastructure names/locations (providers, projects, services, repos, domains, DB schemas) → **Glow Infrastructure**.

Narratives surface (Aux route & Composer), suppression rule (200 with no body, no ETag), and A7 posture for Aux → **HDE Narratives Guide** (and **HDE-Governance** for policy).

Invocation tag / covenant text → **PF-Invocation**.

Endpoint Catalog (JSON success) single home & env-gate proof → **HDE-CLI-API-Vendor-Ref** (route titles) and **HDE-Schemas & Artifacts** (path `docs/ENDPOINTS_CATALOG.json` \+ `.sha256`, env-gate proof indexing). PF02 pins this location only.

BodyGraph evidence families (source-selection snapshot, source-invariance proofs, refresh-policy snapshot, ingest metrics/log samples) → **HDE-Mechanics Guide** / **HDE-Build Checklist** (what to capture, when), **HDE-Schemas & Artifacts** (indices/mirror discipline). Schema names for durability live in **Glow Infrastructure** (names-only).

