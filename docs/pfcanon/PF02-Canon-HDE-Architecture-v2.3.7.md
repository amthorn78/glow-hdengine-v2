# **0\. Front Matter**

**Title:** PF02-Canon-HDE-Architecture  
 **Version:** v2.3.7

 **Status:** Canon  
**Effective date:** 2026-07-03

 **Last Update Gate:** BN 11.9.9

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

**Rendered escape artifact posture (architecture identity).**  
 When reviewing PF02-owned component homes, endpoint catalog paths, route strings, or boundary strings, display-layer escape characters are not source evidence. Source-level proof is required before an escaped character may be treated as an architecture defect. Rendered backslashes in assistant output, markdown output, review prose, preview panes, or copied chat text do not prove that a component home, endpoint catalog path, or boundary string is wrong and do not create redline, blocker, or remediation obligations by themselves.

**Architecture plan-review blocker posture.**

Architecture blockers require a real boundary, public/private, service, endpoint, adapter, route-home, component-home, or contract defect. Command syntax, helper-code syntax, heredoc form, shell syntax, escaped command examples, paste-readiness, indentation, markdown rendering, code-block formatting, and non-literal example invocations are not architecture blockers by themselves. During plan review, preserve architecture scope, proof identity, rails posture, evidence intent, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture without requiring literal executable command syntax. Syntax normalization during execution is allowed when those architecture and proof boundaries remain unchanged.

**Pack/bytes ownership (out of scope here).**  
 Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) are owned outside Architecture and cited by title, primarily in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

**Endpoint Catalog (single home; routing note).**  
Success-endpoint discovery and A7 proofs are catalog-driven. The Endpoint Catalog is the single home for the canon set of client-callable endpoints and their coarse operational metadata. It is an internal artifact (not user-facing), and PF02 documents it only as a wiring map. It does not define its access-control posture or its exact request/response contracts. The single home is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256` sidecar and sibling path-proof transcripts at `docs/ENDPOINTS_CATALOG.json.path_proof.txt` and `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`. All other endpoint inventories are derived artifacts and MUST be regenerated from this home, not independently edited. If the catalog shape or ownership changes, it must be corrected at the single home (and the sha256 sidecar regenerated), not by changing PF02.

**A7 invariants (routing note).**  
 Success proofs require `Vary: Authorization, Accept-Encoding`, strong quoted ETag on 200, HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), and 304 (after prior 200\) omitting both `Content-Type` and `Content-Length`. Encoding-invariance holds: for the same canonical LF-terminated body, the ETag identity and effective `Content-Length` are stable across accepted encodings. Concrete contracts remain in HDE-Governance and HDE-CLI-API-Vendor-Ref.

**DB runtime resolver (routing note).**  
 Resolver semantics are environment-aware:

* **Production-like:** `APP_ENV` values `prod`, `production`, and `live` are production-like for DB bridge fallback guarding. In those environments, the resolver selects `DATABASE_URL` first; bridge fallback is disabled by default and may be used only when `DB_ALLOW_BRIDGE_IN_PROD=1` is explicitly set or when bridge use is explicitly forced by the owning resolver policy. If `DATABASE_URL` is unusable and bridge is not allowed, the resolver returns typed guard/error posture rather than selecting bridge.  
* **Non-production:** non-production resolver behavior may use `DB_BRIDGE_URL` when the owning environment policy allows it, but this remains a BodyGraph-store connection seam, not a second BodyGraph source.  
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

BodyGraph seam carve-out (normative). BodyGraph resolution and ingest MAY perform vendor and DB I/O through the DB abstraction as a sanctioned seam, including when implemented under `engine/bodygraph/`. This carve-out does not relax purity requirements for deterministic compute modules.

Non-BodyGraph loader-style I/O classification (normative). Loader-style modules under `engine/` that are outside the BodyGraph seam, including `engine/charts/loader.py` when observed, are not classified by assumption. Each must be explicitly adjudicated as a sanctioned loader seam, implementation drift, or future canon gap; until that classification is made, the BodyGraph seam carve-out does not authorize new I/O in Engine Core, sampler core, or other deterministic compute modules.

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

Governed evidence-generator PASS posture (architecture-level). Architecture recognizes an offline evidence family as PASS-grade only when the final governed artifact is produced by the final generator logic and the top-level PASS is derived from evaluated decisive predicates for that evidence family. Stale artifacts or partial local state do not create an architecture-valid proof surface. This is an offline-evidence classification rule only; it does not create a runtime route, acceptance token, OPS task, or blanket audit obligation.

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

* **Mounted-handler posture (names-only).** Adapter remains the single HTTP home even when individual route handlers are implemented outside `adapter/` and are mounted through adapter factories.  
* **Routing-authority posture (names-only).** Handler module placement does not create a second HTTP surface home or a second routing authority. Adapter-owned mounting remains the architectural boundary for Reader, compat, and internal/dev HTTP surfaces.

**presenter/** (canonical emitter). Provides the one serializer and emitter used by all surfaces (CLI and HTTP). Ensures canonical formatting, idempotence preimage discipline, and AB↔BA parity at the byte level. Routing (titles only): emitter invocation/validation runs and infrastructure locations live in **Glow Infrastructure**; operational policy and evidence ownership live in **HDE-Governance**.

**database** (persistent BodyGraph cache). An external store for BodyGraphs enabling reuse of previously computed results. The Adapter reads from and writes to this database (on BodyGraph fetches) so that subsequent requests can retrieve the cached BodyGraph instead of calling the vendor. The Engine remains stateless – it simply consumes whatever BodyGraph data the Adapter provides from this cache or a live call.

### **Repo map (normative)**

Repo map (normative)

**Sampler and Engine Core modules (names-only)**

**Names & roles.**

* The canonical sampler behavior lives in a single module under the `engine/` tree, referred to here as the **sampler core module** (currently `engine.sampler.core`). It owns sampler/ranker behavior: pool formation, eligibility, ordering, and sampling decisions.

* The canonical Engine Core behavior lives in a single module under the `engine/` tree, referred to here as the **Engine Core module** (currently `engine.core.core`). It owns the core compatibility computation: neutral and directional metrics, category-framework and per-channel mechanics integration, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling.

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
* **Presenter component home (names-only).** The presenter component is single-home by role and byte-authoritative emitter symbol, not by one literal repository path.  
* **Namespace split without serializer split.** Wrapper envelope builders MAY live under top-level `presenter/`, while the byte-authoritative emitter entrypoint MAY live under `engine/presenter/`, provided all public-byte emission delegates to the same governed emitter path.  
* **Failure condition.** A namespace split becomes architecture drift only if it introduces a second independent presenter component, a second serializer home, or an alternate public-byte path.  
* **Delegation proof routing.** Emitter-delegation proof, guard checks, and path evidence route by title to **HDE-Mechanics Guide** and **HDE-Schemas & Artifacts**; PF02 records the architecture classification only.

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
* Public, birth-facing, or no-user compat proof paths MUST NOT require caller-provided `person_uid`, `user_id`, or app user ID. If strict compatibility compute still needs internal metadata, a sanctioned resolver or adapter boundary MAY derive deterministic internal metadata before Engine Core compute; this does not make that metadata a public, birth-facing, or caller-supplied input.  
* Fixture-only `person_uid` injection is an internal-compute proof class only; it is not sufficient architecture proof for live no-user or birth-facing behavior.  
* Vendor-backed no-user smoke evidence is implementation-validation evidence through the governed vendor seam. It does not create a new public route, public flag, acceptance token, QA PASS, Live QA completion, or epic closure.  
* **Proof-class boundary (architecture-level).** Public Reader output, internal/admin compat compute output, and public or birth-facing no-user compatibility behavior are separate proof classes. Public Reader proof establishes bands-only, numeric-free Presenter output; internal/admin compat proof may validate Engine Core compute and admin/test compat payloads; no-user or birth-facing behavior proof validates the adapter or resolver boundary that supplies internal metadata without caller identity. Any UID-coupled internal ordering needed to stabilize strict compute remains an internal resolver or adapter concern and does not become a caller-facing identity requirement. Passing evidence in one proof class does not, by itself, satisfy the others or create a new public route.  
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

his subsection describes the BodyGraph lifecycle at the architecture level:

request → DB runtime resolver → vendor (when needed) → Engine → DB persist → subsequent requests

It ties together the DB cache, vendor seam, and Engine’s stateless contract.

**HumanDesignAPI v2 conformance posture (architecture-level).** HDE-FERM006 contract-inventory evidence may be complete while BodyGraph ingest and vendor-seam runtime architecture remains legacy BodyGraph-oriented until downstream HDE-FERM007 and HDE-FERM008 adapter shaping, response normalization, closed-rails proof, and PO-only open-rails smoke evidence are implemented and evidenced. PF02 must not describe the HDE vendor seam as runtime v2-conformant until those runtime conformance slices are complete. The inventory-complete posture may record recommended v2 chart routes, legacy v1 BodyGraph routes, validated source families, and contract-inventory evidence; it does not by itself create request shaping implementation, source selection implementation, live conformance, public Reader change, new HTTP home, AI product scope, or open-rails smoke proof.

**No-AI runtime boundary for this vendor conformance path.** HumanDesignAPI v2 conformance is deterministic vendor integration only. It does not add OpenAI, LLM, AI-agent, chatbot, prompt, embedding, model-call, or AI-enablement architecture inside the HD Engine, Glow App, Reader, vendor adapter, cache, sampler, compat engine, narrative machinery, public surfaces, or admin runtime surfaces. Vendor documentation files or pages aimed at AI or LLM consumers may be inspected only as documentation-discovery context and must not be treated as product or runtime scope.

### **Adapter source policy (env-aware)**

* **Prod / non-dev:**

  * The database is the **canonical source** for BodyGraphs on request paths.

  * The Adapter uses the DB runtime resolver (env-aware) to locate the BodyGraph store. Production-like aliases (`prod`, `production`, `live`) select `DATABASE_URL` first and keep bridge disabled by default unless explicitly allowed. Non-dev total-failure proof may validate observed provider attempt order, typed `BridgeUnavailable` / `missing_bridge_url` refusal, numeric-free failure posture, and secret-free evidence without creating a second BodyGraph store or a new request-path mode.

  * Vendor calls occur only via **explicit triggers or scheduled refresh jobs**, never inline on the public request path.

* **Dev:**

  * Direct vendor calls are allowed on request paths under SAFE rails.  
  * SAFE rails are closed by default. Open rails requires explicit env (for example, `SAFE_MODE=0`, `ALLOW_NETWORK=1`). If rails env is missing or empty, it MUST be treated as closed rails.  
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

**Viewer-preference normalization handoff (high level).**

Compat and CLI compatibility flows normalize viewer preferences before candidate-selection, sampler, or ranker behavior consumes them. Zero-weight intent is carried as normalized input truth into the existing sampler/ranker behavior home; sampler/ranker remains the owner of candidate exclusion behavior. This handoff uses existing CLI and compat call paths and does not create a new public surface, route, serializer path, or public contract.

**Threshold ownership handoff (high level).**

Compat threshold symbols used by compat and CLI compatibility flows are compatibility-facing shims over the existing Magic-10 threshold source in the Engine math layer. `engine.compat.thresholds.THRESHOLDS_V1` derives from `engine.magic10.thresholds.THRESHOLD_EDGES`, and `engine.compat.thresholds.BANDS` derives from `engine.magic10.thresholds.BANDS`. This preserves one threshold home, keeps threshold arithmetic and constants-pack ownership outside Architecture, and does not create a new public route, flag, serializer path, public contract, or second threshold source.

**Presenter rule.**  
 The adapter never hand-crafts public JSON. Only the Presenter’s single emitter serializes public bytes for **all** callers (HTTP and CLI).

**Conjunction compute contract (internal).**

Conjunction computation is an internal Engine surface. It does not create a new production HTTP endpoint and it emits public bytes via the same Presenter emitter used everywhere else.

* Location: `engine/compat/compute.py`

* Entry points (names-only):

  * `conjunction_public` (pure compute over resolved BodyGraphs)

  * `conjunction_public_resolved` (local-first resolution via the existing BodyGraph resolver path, then compute; SAFE rails apply)

**Birth-only no-user boundary (architecture-level).**

`conjunction_public_resolved` is the sanctioned no-user resolver boundary for local compatibility proof when caller input provides a complete birth tuple and provides no `person_uid`, `user_id`, or app user ID. The boundary may derive deterministic internal metadata before strict Engine compute, including an internal `person_uid`, but that metadata stays internal and is not a caller input, public field, public route contract, CLI flag, or serializer path. Existing internal `user_id` flows remain separate and unchanged.

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

* No narrative text.

* No transport or policy bytes are defined in PF02.

* No uncontrolled vendor/network calls. Rails are closed by default; acquisition is permitted only when explicitly enabled under SAFE rails, and only through the existing BodyGraph resolver seam described in §2.4.

* No new persistence surfaces. Any writes are limited to the existing BodyGraph cache upsert described in §2.4.

**Gating & posture (dev-only; titles-only routing).**

* Harness is dev-only; never mounted in production.  
* Harness routes are gated via the dev admin gate (`_dev_admin_gate()`), and MUST deny when `APP_ENV` is not one of: `dev`, `test`, `local`.  
* Canonical internal/dev sampler route (HTTP POST; names-only):  
  * POST /internal/dev/sampler  
* Dev-only conjunction routes (HTTP GET; names-only):  
  * `GET /dev/sampler/conjunction`  
  * `GET /dev/reader/conjunction`  
  * `GET /dev/writer/conjunction`  
* **Writer readback parity flow (names-only).** The dev conjunction writer/readback proof path remains inside the dev harness surface family, using `GET /dev/writer/conjunction` together with `GET /dev/reader/conjunction`. PF02 records only the route names and adapter ownership here; writer/readback bytes and proof artifacts remain out of scope here.  
  Endpoint Catalog entries for these dev conjunction endpoints are classified as `dev_harness` and are not A7-eligible.  
* Rails are closed by default (for example, `SAFE_MODE=1`, `ALLOW_NETWORK=0`). Dev-only conjunction endpoints MAY run under open rails only when explicitly enabled (for example, `SAFE_MODE=0`, `ALLOW_NETWORK=1`).  
* Optional GET/HEAD/304 captures are allowed for the GET dev harness endpoints, but A7 proofs are not run here. A7 proofs run on the cataloged JSON success route (Endpoint Catalog) and are driven by the Catalog.  
* Locale is optional; when present, it is advisory only and does not affect canonical JSON bytes.

Sample harness uses the same Presenter emitter and Engine Core behaviour as compat v1. Dev-only conjunction preview endpoints emit canonical JSON bytes; rails are closed by default unless explicitly opened. Sample harness is never used for A7 proofs; see §2.4 and §5 for compat flow and evidence-plane details.

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
* **Repo-side start-helper posture (names-only).** Dev Reader start helpers are part of the adapter/dev-harness boundary and MUST propagate `APP_ENV` exactly as supplied by the calling environment. They do not silently default `APP_ENV`.  
* **Infra-owned harness binding input (names-only).** Sampler healthchecks and other QA-side callers consume `DEV_SAMPLER_URL` (or an equivalent infra-owned binding) as the authoritative address for `/internal/dev/sampler`. Architecture records that this binding is separate from route ownership and does not permit guessed host or port reconstruction when the binding is absent or malformed.  
* PF02 does not introduce service names, ports, or commands. Those details are single-home in **Glow Infrastructure**, the **HDE-Mechanics Guide**, and any field guides that describe running the adapter and Reader inside a dev container (including Codespaces). This document only records the responsibility that HTTP-based tests must target a known, running Reader instance.  
* In dev/QA, the adapter/Reader stack is hosted by a concrete framework development HTTP server (currently a Flask dev server) that exposes the same Reader and internal/dev sampler routes as the production adapter. Architecture treats this dev server as part of the adapter and dev harness component: it is a real, required piece of the system in dev/QA, but the choice of framework and all start commands, ports, and environment wiring remain the responsibility of **Glow Infrastructure** and **HDE-Mechanics Guide**, not PF02.  
* The dev Reader harness used in dev/QA consoles (including Codespaces) MUST expose the canonically required dev/internal HTTP surfaces for QA, using the same Presenter emitter and error-handling semantics as the production/stable adapter app. In particular, the harness is responsible for mounting the compat HTTP surface (`/api/compat/v1`) as defined in **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide** by title. This requirement applies to the set of dev/internal HTTP routes needed for QA; it does not require the dev harness to expose every production-only surface. PF02 records this responsibility at the architectural level and continues to route all concrete route shapes and error envelopes by title to their single-home documents.

### **3.8.2 QA entrypoints (concept-only)**

For epics whose D-goals involve Reader/HTTP behaviour, compat behaviour, or dev sampler behaviour, Live QA uses canonical entrypoints only:

* **Reader v1** (public success route) for HTTP-level compat envelopes.  
* **Compat CLI surfaces** (as described in **HDE-CLI-API-Vendor-Ref**) for terminal-based compat flows. CLI stdout may be an admin/test compat payload (for example `showcompat`). When Reader-identical bytes are required for parity proofs, the CLI emits Reader v1 bytes via a dedicated dump sidecar output (titles-only; see **HDE-CLI-API-Vendor-Ref**).  
* **Controlled no-user vendor smoke (CLI proof class).** A PO-run `showcompat` vendor smoke is a CLI proof class through the vendor seam. For architecture purposes, it is not an HTTP Reader run, not a hosted-service proof, and not a new public route. If a future smoke changes from CLI vendor execution to an HD Engine HTTP service call, the target classification changes and must be grounded in the infrastructure home before execution. Concrete command flags, environment variables, credentials, and evidence outputs are routed by title to the owning CLI/API, infrastructure, QA, and build-checklist homes.  
* **Repo-local script launcher surface (names-only).** `scripts/hdctl.py` is a repo-local launcher over the same CLI family and is used for subcommand help and invocation flows such as `bg:resolve`. Architecture treats this launcher as part of the existing emitter-backed CLI entrypoint family, not as a second serializer, second contract, or distinct runtime surface.  
* **CLI entrypoint wiring (repo surface; names-only).** `pyproject.toml` exposes `hdctl = engine.cli.main:cli`, `engine/cli/main.py` is the repo-local wiring surface, and `python -m engine.cli` is the module-runner surface over the same CLI entrypoint family for conjunction-oriented `showcompat` flows. Architecture treats console-script and module-runner invocation as one emitter-backed CLI surface and keeps CLI bytes and argument contract out of scope here.  
* **Dev sampler harnesses** (CLI and HTTP) for sampler-specific behaviour. The HTTP harness is a non-public internal/dev surface under the adapter family, uses `POST /internal/dev/sampler` when HTTP evidence is required, is `APP_ENV`\-gated rather than public, and calls the sampler core in-process before bytes are emitted through the single Presenter emitter. CLI and HTTP harnesses do not create a new public route, second sampler implementation, or alternate serializer.  
* **Bounded conjunction closeout family (names-only).** For conjunction-bounded closure work, the canonical dev/QA surface family may include the Reader success surface, the internal/dev sampler surface (`POST /internal/dev/sampler`), and the dev-only conjunction routes (`GET /dev/sampler/conjunction`, `GET /dev/reader/conjunction`, and `GET /dev/writer/conjunction`). Using this existing family for Live QA or closeout does not create a new public route by itself.  
* **Surface-class distinction (names-only).** Reader-like success surfaces, compat API surfaces (for example `/api/compat/v1`), and dev/internal harness surfaces may coexist inside one adapter-mounted HTTP family without collapsing into one proof class. Architecture records the mounted family and the single-emitter boundary only; epic-specific proof-surface selection remains routed by title to the owning QA and governance documents.  
* **Closeout-impact posture (names-only).** Internal/dev harnesses can materially affect closure and evidence binding even when no new public route is introduced, because they still exercise the same adapter-mounted and Presenter-emitted architecture.

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

**Production-affecting architecture classification.** When an epic affects deployed behavior, public or app-facing behavior, runtime request/response behavior, Engine compute, vendor ingest, external integration, DB persistence/retrieval, app/engine integration, or secret/environment binding, PF02 classifies the affected flow as production-affecting for QA planning. Production-affecting architecture requires live validation of at least one relevant production-facing boundary or an explicit authorized exemption.

PF02 owns this architecture classification only. Exact Live QA steps, open-rails evidence shape, exemption handling, PASS/FAIL semantics, and closeout proof rules live in Glow QA Guide, HDE-Governance, Epic-Process-Guide, HDE-Schemas & Artifacts, and Plan Templates by title.

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

* **Default documented client-access address (non-prod local-style).** For dev and QA documentation that shows how to reach a non-prod local-style Reader or dev harness surface, the default documented client address is `127.0.0.1` plus the correct port and endpoint path.  
* **Access address versus service identity.** This documented loopback default is an access convention only. It does not redefine the service identity, provider or project names, or the server bind address used by the adapter process.  
* **Prod-facing exception.** If a QA console, runbook, or harness is targeting the real production service, the documented address stays the real hosted production URL rather than a loopback form.  
* **Binding-coverage distinction.** Environment-specific validation of a dev harness binding is separate from the architectural existence of the route. A dev or internal surface can exist in the adapter while a particular environment remains not yet closed until its infra-owned binding is published and validated.  
* **Codespaces Live QA posture (routing note).** Codespaces QA configuration and requirements are single-home in the **Glow QA Guide** (names-only; secrets recorded as presence-only, never values). A standalone Step-0 “Codespaces snapshot” artifact is **not required** and MUST be treated as optional and non-gating; plans MUST NOT require, validate, or gate approval on it.   
* **Environment variable discipline (Live QA).** Environment variable names MUST be treated as governed interface surfaces (like repo paths and endpoints), not free-text fields. QA plans, QA runbooks, and QA evidence schemas MUST NOT introduce, require, or depend on any `MODO_*` variable names for PASS or FAIL or required evidence structure; any `MODO_*` strings are non-canonical and inert.  
  * **No QA-time env var minting (hard).** New environment variable names MUST NOT be introduced during Live QA (including Moon Loop). If a QA step would require a new environment variable name to function, treat it as development work under PO approval and canonize the variable name before any plan depends on it.  
  * **Review posture (mechanical blocker).** Any unapproved environment variable name used as a required input, required header key, required manifest key, or required evidence schema key is a mechanical blocker for plan approval. Fix by removing it or replacing it with canon-approved variables only.  
  * **EPIC025 exception (grandfathered; non-binding only).** If the already-approved EPIC025 Live QA Plan references `MODO_*` keys, treat those keys as inert placeholders: they MUST NOT be required for PASS or FAIL, MUST NOT be required evidence keys, and MUST NOT be used as proof of rails posture or execution configuration. This exception MUST NOT be replicated in new plans.  
* **KISS required outputs (Live QA).** Live QA Plans MUST minimize required outputs to:  
  * one primary step log per check under `audit/qa/<epic-id>/checks/<check_id>/primary.log`,  
  * checks-only evidence layout under a single epic-scoped QA root, with no per-run nesting, no run-id directories, and no operator-set “fresh directory” posture for reruns,  
  * any required QA step-logs manifest and sibling path proof at the epic-scoped QA root (`audit/qa/<epic-id>/qa_step_logs_manifest.json` and `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt`), with each manifest entry mapping a `check_id` to its `checks/<check_id>/primary.log` path and with the manifest itself expected to be discoverable through the governed updater and the human and machine evidence ledgers when canon requires it,  
  * Nothing else is auto-required unless canon explicitly pins a governed evidence family or path. Any additional required artifact MUST be acceptance-decisive and MUST be canonized (PF10 or PF-Canon) as a governed evidence family or path.  
  * **Step-log header normalization (KISS).** Every `primary.log` MUST begin with a JSON header object that includes: `check_id`, `status`, `command`, `command_provenance`, `captured_env`, `evidence_artifacts`, `pf_refs`, `intended_tokens`, `claimed_tokens`. The `command` field MUST record the actual executed command sequence, not a paraphrase. If multiple commands were executed, `command` MUST be an explicit pipeline or an explicit `;`\-joined sequence that preserves the execution order. The four list fields MUST be present; empty lists (`[]`) are allowed and SHOULD be used when no refs/tokens are in play. `evidence_artifacts` MUST include the check’s own `primary.log` path. If any required list field is missing, treat it as an evidence-format gap; a reviewer-of-record MAY mechanically normalize the header by inserting missing empty lists and re-serializing the header as canonical JSON (no step rerun required). Token claims are never inferred: if `claimed_tokens` is missing or empty, token claims are treated as none. Status vocabulary remains gating (PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED).  
  * **Step-log header writer exports (per-check).** If a Live QA plan uses a step-log header writer that reads per-check metadata from environment variables, the plan MUST export the complete required set immediately before header generation for each check and MUST NOT rely on prior step state.  
    * Minimum per-check exports (names are governed by the writer contract): `CHECK_ID`, `CHECK_NAME`, `PASS_FAIL`, `COMMANDS_JSON`, `COMMAND_PROVENANCE`, `ARTIFACTS_JSON`, `PF_REFS_JSON`.  
    * Live QA handling (evidence-capture only): if a check ran successfully but `primary.log` is missing a required JSON header or contains incorrect check metadata due to missing exports, a reviewer-of-record MAY apply a minimal Moon Loop deviation to (1) export the required header vars, and (2) regenerate the JSON header and reassemble `primary.log` by prepending the corrected header while preserving the existing body verbatim.  
    * Anti-drift: plans MUST be internally consistent. Do not mix patterns where one check exports header variables and another does not while still calling the same header writer.  
  * **Prefer validating canon evidence over generating QA artifacts.** By default, if PF10/PF-canon already establishes an artifact family/path, the Live QA plan validates it (exists \+ minimal posture checks) and records PASS/FAIL in the check’s `primary.log`. QA creates new artifacts only when the check itself is about QA-run outputs (primary logs, step-logs manifest) or when canon explicitly requires a generated QA artifact. If a plan requires an EPIC-scoped derived artifact path to satisfy a predicate, the artifact MUST be mechanically derived from the canonical surface and MUST be treated as evidence-only (not a new governed evidence family/path) unless and until canon explicitly pins it.  
  * **Showcompat QA: vendor rails and arguments.** Current limitation: `showcompat` requires vendor-sourced BodyGraph data to compute compatibility. When a Live QA step executes `showcompat` and BodyGraph data is not already available, that step MUST run with vendor rails open (network allowed) so the vendor seam can be called. Treat closed network rails as an expected blocker for functional `showcompat` runs under this limitation.  
    * The rails change MUST be explicit and scoped only to the `showcompat` step(s); restore default rails posture after the step.  
    * In conjunction mode, \`showcompat\` is local-first and uses the same resolved-BodyGraph path as \`conjunction\_public\_resolved\`, respecting SAFE rails. If either party’s BodyGraph is missing locally, open rails are required to fetch; if rails are closed, the step MUST refuse deterministically and MUST NOT attempt network.  
    * When conjunction-mode \`showcompat\` succeeds, it MUST emit deterministic canonical JSON to stdout (byte-stable for identical inputs), enabling gated comparisons and traceable evidence artifacts.  
    * `showcompat` MUST NOT be executed as a zero-argument command in QA plans or QA runs. Follow the authoritative command and argument contract in **HDE-CLI-API-Vendor-Ref**.  
  * **PF23 consult is required in QA planning (read-only).** Reality Audits (PF23) MUST be consulted during QA planning and QA plan review as a primary input for repo-reality context and existence or locus framing. Plans and reviews MUST NOT treat PF23 consult as a required deliverable, a required check, or an acceptance token. Do not instruct the operator to run commands solely to prove PF23 consult.  
    * If a plan names repo-resident loci, reviewers SHOULD consult PF23 before approval to reduce fabricated or stale locus assumptions.  
    * Consultation is read-only; PF23 updates remain PO-only, and QA execution MUST NOT include PF23 updates as a required output.  
    * A plan MAY include a single “PF23 Anchors” note (components consulted and loci touched), but it is informational only and MUST NOT appear as a required check or required evidence output.  
    * If any PF23 Reality Audit statement contradicts PF canon, or appears inconsistent with other allowed repo-reality sources, record it as an explicit drift item requiring adjudication and treat the situation as reality ambiguity. Do not resolve contradictions by assumption or assert a reconciled locus as fact inside the plan.  
    * Record each contradiction as a set:  
      * PF23 claim (verbatim quote)  
      * Canon claim (verbatim quote plus PF canon citation)  
      * Impacted epic or surface  
      * Classification bucket: canon defect, implementation drift, or necessary reality shift  
    * **PF23 audit-classification routing (architecture-level).** PF23 repo-reality observations that implicate PF02 architecture, PF14 mechanics, PF05 transport, or PF12 schemas/artifacts MUST route to the owning canon home by title. Do not convert those observations into PF09.x task deltas, remediation work, implementation deltas, new evidence homes, or acceptance tokens by assumption.  
    * Adjudication is owned by the PO, who decides whether the resolution path is a canon update, implementation remediation, or a formalized exception with a canon follow-up.  
  * **No VCS workflow content (hard).** Live QA Plans MUST NOT instruct or discuss branches, commits, PRs, or any other VCS workflow steps, and MUST NOT gate PASS/FAIL on VCS state (for example “working tree clean” or “on correct branch”). Read-only, non-mutating git commands are allowed only as optional, non-gating repo-root sanity checks and must not rely on branch names, commit SHAs, or PR identifiers.  
  * **Discovery-first, objective-first Live QA plans.** Live QA Plans MUST specify intent and proof obligations per step and MUST treat any repo detail not proven at planning time as unknown until discovered during the run.  
    * Steps SHOULD use general command-line directives rather than brittle verbatim command text; execution-time command resolution and the recorded command transcript in `primary.log` are authoritative.

    * The plan SHOULD describe the goal of the action, the observable outputs that matter, and the evidence that must be captured.

    * Reduce plan brittleness by minimizing locus strings unless the locus is canon-defined or is a fixed-path obligation.

    * If a plan must include an exact command string, it MUST be proven by an allowed provenance source.

    * When a check requires interacting with a repo-resident locus that is not proven at planning time, the plan MUST state the discovery intent, state the discovery acceptance, require recording the discovered locus string verbatim into check evidence before using it, and provide PASS, FAIL, and BLOCKED outcomes for discovery itself.

    * Each check MUST be expressible as: Intent; Discovery step (only if needed); Minimal test step; Required evidence; PASS criteria; FAIL criteria; BLOCKED criteria when discovery cannot proceed without guessing.

    * Loci discovered during execution are valid for that run only and MUST NOT be treated as planning-time proof for future plans unless they are incorporated into an allowed provenance source.

    * Moon Loop may be used to remediate syntax and quoting mismatches, but MUST NOT change objectives, loci exercised, required outputs, or PASS or FAIL predicates.  
  * **Repo-locus provenance lock (MUST).** Planning documents and plans MUST NOT invent, guess, infer, paraphrase, normalize, or fill in any repo-resident locus string.  
    * The only allowed provenance sources for repo-reality claims are PF10 — HDE Build Notes, PF-Canon, and the initial QA Audit for the epic.

    * This rule applies to file paths, directory paths, endpoint names, routes, module and component identifiers, script names, runbook names, command strings, check and test identifiers, CI job names, environment variable names treated as already-existing, fixed output locations treated as already-existing, and negative existence claims.

    * When a repo-resident locus string is used, it MUST be copied character-for-character from an allowed provenance source. No renaming, no case folding, no “equivalent” substitutions, no wildcard expansions, and no invented variants.

    * Placeholder routes, placeholder file paths, placeholder module names, placeholder commands, invented scripts, and any statement that implies app topology certainty without proof are vetoed.

    * Review gate: any unvalidated or inferred locus claim is a mechanical blocker until corrected.

    * File minting is allowed and expected only for plan-created outputs. New files and directories MAY be created under canon-defined homes once the locus is validated. New roots and second homes MUST NOT be assumed.

    * Evidence output clarity: plans SHOULD name primary governed evidence outputs by exact path and filename and SHOULD avoid vague family phrases or wildcards in evidence-output lines.

    * A plan MUST NOT reference a file path as required unless it is canon-defined, audit-proven, or explicitly QA-created by the plan with exact repo-relative path and filename, runnable creation instructions, a one-line purpose, reproducible creation detail, and explicit PASS and FAIL predicates tied to file contents.

    * Governed evidence artifacts used to decide PASS or FAIL MUST be written under a concrete lowercase path under `audit/**` (preferred) or `artifacts/**`.

    * Plans MUST separate pre-existing artifacts (required to exist before execution) from QA-run artifacts (created during execution); preflight presence checks may gate only on pre-existing artifacts.

    * If a deliverable family or path is not canonized, the plan MUST treat it as non-gating posture-only (for example, log `UNPROVEN` or `TOOLING_BLOCKED`) and MUST NOT introduce new required paths to simulate it.  
  * **Plan-created scripts and helpers.** Live QA Plans MUST NOT invent or assume helper scripts exist. Plan-created scripts are permitted only when a required deliverable cannot be produced without one.  
    * A plan-created script MUST name the exact repo-relative path and filename where it will be created, include runnable creation instructions, state why the script is required, and keep the script minimal and purpose-bound to the deliverable.

    * QA agents MAY create ephemeral helper scripts under `/tmp` during Live QA execution, but `/tmp` scripts and outputs are execution-only: they MUST NOT be treated as deliverables or evidence, MUST NOT be indexed or mirrored, and MUST NOT be referenced as acceptance binding surfaces. `/tmp` helpers must not print or persist secrets (presence-only or redacted where applicable).

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
* EPIC026 evidence posture surfaces (addendum 10–15, 23–31)  
  * `audit/qa/hde-epic026/topology/topology_conjunction_demo.json` (topology demo output; governed evidence)  
    * Conjunction route-proof checks (examples): `audit/qa/hde-epic026/checks/po-005/route_proof.txt`, `audit/qa/hde-epic026/checks/po-005/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-005/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-005/pytest_rc.txt`; `audit/qa/hde-epic026/checks/po-006/route_proof.txt`, `audit/qa/hde-epic026/checks/po-006/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-006/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-006/pytest_rc.txt`.

    * Endpoint Catalog dev-endpoint verification (example): `audit/qa/hde-epic026/checks/po-007/catalog_extract_dev_endpoints.json`, `audit/qa/hde-epic026/checks/po-007/catalog_sha256_check.txt`, `audit/qa/hde-epic026/checks/po-007/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-007/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-007/pytest_rc.txt`.

    * CLI help and modifier-validation captures (example): `audit/qa/hde-epic026/checks/po-008/cli_help.txt`, `audit/qa/hde-epic026/checks/po-008/showcompat_help.txt`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stdout.log`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stderr.log`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_rc.txt`.

    * Conditional conjunction-output captures (example; only when runtime IDs are provided): `audit/qa/hde-epic026/checks/po-008/concat_output.json`, `audit/qa/hde-epic026/checks/po-008/concat_output_order_check.txt`.

    * Blocked-input conjunction captures (example): `audit/qa/hde-epic026/checks/po-009/open_rails_note.txt`, `audit/qa/hde-epic026/checks/po-009/po-009_input_constraint.log`.

    * Conjunction-help and dev-endpoint confirmation captures (example): `audit/qa/hde-epic026/checks/po-010/showcompat_help.txt`, `audit/qa/hde-epic026/checks/po-010/catalog_extract_dev_endpoints.json`.

    * Canonical-JSON gate and evidence-index refresh captures (example): `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stdout.log`, `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stderr.log`, `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_rc.txt`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stdout.log`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stderr.log`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_rc.txt`.  
  * Conjunction route-proof checks (examples): `audit/qa/hde-epic026/checks/po-005/route_proof.txt`, `audit/qa/hde-epic026/checks/po-005/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-005/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-005/pytest_rc.txt`; `audit/qa/hde-epic026/checks/po-006/route_proof.txt`, `audit/qa/hde-epic026/checks/po-006/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-006/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-006/pytest_rc.txt`.

  * Endpoint Catalog dev-endpoint verification (example): `audit/qa/hde-epic026/checks/po-007/catalog_extract_dev_endpoints.json`, `audit/qa/hde-epic026/checks/po-007/catalog_sha256_check.txt`, `audit/qa/hde-epic026/checks/po-007/pytest_stdout.log`, `audit/qa/hde-epic026/checks/po-007/pytest_stderr.log`, `audit/qa/hde-epic026/checks/po-007/pytest_rc.txt`.

  * CLI help and modifier-validation captures (example): `audit/qa/hde-epic026/checks/po-008/cli_help.txt`, `audit/qa/hde-epic026/checks/po-008/showcompat_help.txt`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stdout.log`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stderr.log`, `audit/qa/hde-epic026/checks/po-008/reject_nonjson_rc.txt`.

  * Conditional conjunction-output captures (example; only when runtime IDs are provided): `audit/qa/hde-epic026/checks/po-008/concat_output.json`, `audit/qa/hde-epic026/checks/po-008/concat_output_order_check.txt`.

  * Blocked-input conjunction captures (example): `audit/qa/hde-epic026/checks/po-009/open_rails_note.txt`, `audit/qa/hde-epic026/checks/po-009/po-009_input_constraint.log`.

  * Conjunction-help and dev-endpoint confirmation captures (example): `audit/qa/hde-epic026/checks/po-010/showcompat_help.txt`, `audit/qa/hde-epic026/checks/po-010/catalog_extract_dev_endpoints.json`.

  * Canonical-JSON gate and evidence-index refresh captures (example): `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stdout.log`, `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stderr.log`, `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_rc.txt`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stdout.log`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stderr.log`, `audit/qa/hde-epic026/checks/po-011/update_evidence_index_rc.txt`..  
  * Plan check step directories are organized under `audit/qa/hde-epic026/checks/po-0NN/` (for example: `po-005`, `po-006`, `po-007`, `po-008`, `po-009`, `po-010`, `po-011`, `po-012`) with a per-step `primary.log` plus step-specific artifacts (names and paths only).

* EPIC026 close-pack artifacts (mechanically generated)  
  * `tools/qa/generate_epic026_close_pack.py` (generator; emits close pack at fixed paths)

  * `audit/EPIC-026_MANIFEST.json` (enumerates key outputs \+ includes `pf23_sha256` for the PF23 anchor)

  * `audit/EPIC-026_close_report.md` (close report, ADR/TI mapping)

  * `audit/EPIC-026_MANIFEST.json.path_proof.txt` (path proof transcript; created by QA harness)

  * `audit/EPIC-026_close_report.md.path_proof.txt` (path proof transcript; created by QA harness)

  * `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json` (plan-required Step-0 manifest pair; stable check-scoped location)

  * `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json.path_proof.txt` (path proof transcript; stable check-scoped location)

  * `audit/qa/hde-epic026/qa_step_logs_manifest.json` and `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt` may exist as legacy traceability artifacts, but they are non-canonical for the Step-0 close-out deliverable surface.

  * Check-scoped close-pack verification copies (example; CHECK `po-012`): `audit/qa/hde-epic026/checks/po-012/generator_stdout.log`, `audit/qa/hde-epic026/checks/po-012/generator_stderr.log`, `audit/qa/hde-epic026/checks/po-012/generator_rc.txt`, `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_manifest.json`, `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_evidence_index.json`, `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json`, `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json.sha256`.

  * `audit/docdeltas/hde-epic026_doc_deltas.md` (doc delta ledger for epic; governed artifact)

  * `audit/docdeltas/hde-epic026_drain_targets.md` (doc delta drain targets)

  * `audit/qa/hde-epic026/00_meta/doc_deltas.md` (QA-meta doc delta ledger artifact)  
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
  * **Gate checked-target coverage includes conjunction CLI artifacts (names and paths only).** The Canonical JSON gate target surface includes the conjunction-related CLI artifacts below.  
    * `artifacts/audit/cli/pair.json`

    * `artifacts/audit/cli/pair_ba.json`

    * `artifacts/audit/cli/showcompat_ab.json`

    * `artifacts/audit/cli/showcompat_ba.json`

    * `artifacts/cli/out.json`

    * `artifacts/cli/out_ba.json`

    * `artifacts/cli/abba_sidecar.json`

    * Each listed artifact MUST have a sibling `.path_proof.txt` transcript and corresponding entries in both Evidence Indexes (`docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`).

    * Runner target definitions and artifact-key naming are owned by HDE-Mechanics Guide and HDE-Schemas & Artifacts by title.

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
* Epic-close and acceptance-ledger generators belong to this same offline evidence plane. They consume and bind already-existing proof families from runtime surfaces rather than introducing new runtime routes, alternate emitter paths, or replacement transport surfaces.  
* **Reuse-baseline posture.** When an epic treats already-implemented runtime surfaces as inherited baseline, later close-pack and evidence work continues to consume those existing surfaces rather than re-planning them as new architectural homes or new public surfaces.  
* **Same-run runtime-surface inventory posture.** When closeout or QA synthesis proves changed runtime behaviour, it does so by inventorying already-declared runtime surface families from the same run rather than by creating a proof-only surface. Architecture-level runtime synthesis may therefore bind the existing CLI surface, the dev conjunction route family, and the cataloged Reader success route when those are the changed surfaces under review.  
* **Bounded conjunction inventory posture (names-only).** For conjunction-slice inventory and bounded closeout review, the current JSON surface family is the cataloged Reader success route `GET /reader`, the dev-only conjunction routes `GET /dev/writer/conjunction`, `GET /dev/reader/conjunction`, `GET /dev/sampler/conjunction`, and the internal dev sampler route `POST /internal/dev/sampler`.  
* **Inventory-only posture for bounded conjunction review.** Grouping these existing routes for conjunction review does not create a new public surface, a separate proof carrier, or an alternate serializer or emitter path.  
* **No new public-surface inference from closeout inventory.** Catalog-surface and runtime-surface inventories are confirmatory only. They may show that no unexpected public success surface has appeared beyond the declared PF02 runtime surface set, but they do not create, widen, or rename that set.  
* **EPIC030 PR-01 normalization evidence surfaces (names-only).** The PR-01 normalization slice binds existing viewer-preference normalization and zero-weight handoff behavior through governed offline evidence at `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json`, `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log`, and `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This offline evidence family records normalized input truth, invalid-preference handling, and canonical-compare posture for existing CLI and compat call paths; it does not create a new public route, flag, serializer path, public contract, or second exclusion home.  
* **EPIC030 PR-02 dev-sampler evidence surfaces (names-only).** The PR-02 dev-sampler slice binds the existing internal/dev sampler harness through governed offline evidence at `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt`, `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json`, `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json`, and `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This offline evidence family records headers/body snapshot, seed-only metadata, and two-run identity posture for the existing `POST /internal/dev/sampler` dev harness; it does not create a public route, A7 proof surface, production mount, second sampler implementation, or alternate serializer.  
* **EPIC030 PR-03 compat evidence surfaces (names-only).** The PR-03 compat slice binds existing compat behavior through governed offline evidence at `audit/qa/hde-epic030/pr-03/category_order_binding.log`, `audit/qa/hde-epic030/pr-03/compat_identity_binding.log`, `audit/qa/hde-epic030/pr-03/compat_parity_binding.log`, and `artifacts/narratives/key_table_10x2.snapshot.json`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This offline evidence family records category-order, compat identity, compat parity, and narrative key-table snapshot linkage for existing compat/admin surfaces; it does not create a new public route, second compat surface, second Presenter path, or alternate evidence home.  
* **EPIC030 PR-04 band-threshold evidence surfaces (names-only).** The PR-04 threshold/tuning slice binds the existing compat threshold and band-order flow through governed offline evidence at `audit/qa/hde-epic030/pr-04/band_edges_binding.log`, `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json`, and `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This offline evidence family records threshold-source binding and AB↔BA identity posture for the existing compat/admin threshold surface; it does not create a new public route, flag, serializer path, public contract, close-pack surface, or second threshold home.  
* **EPIC030 PR-05 category-framework evidence surfaces (names-only).** The PR-05 category-framework slice binds existing category-framework and per-channel mechanics proof through governed offline evidence at `audit/qa/hde-epic030/pr-05/category_framework_binding.log`, `audit/qa/hde-epic030/pr-05/category_canonical_compare.log`, and `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This offline evidence family records canonical-compare and per-channel mechanics posture for existing Engine category-framework behavior; it does not create a new public route, flag, serializer path, close-pack surface, QA-ledger surface, Live QA runbook surface, PF-canon edit, or runtime proof route.  
* **EPIC030 QA check-surface binding (names-only).** CHECK po-006 through po-010 are check-scoped offline QA surfaces under `audit/qa/hde-epic030/checks/po-0NN/`. They bind already-existing proof families from OPS-02, PR-04, PR-05, and the PR-01 through PR-05 generated proof families; they do not create new runtime routes, public surfaces, A7 proof surfaces, or Presenter paths.  
* **EPIC030 no-user, threshold, and generated-proof-family checks (names-only).** CHECK po-006 binds public numeric-free compat proof and OPS-02 birth-only no-user implementation-validation evidence. CHECK po-007 and po-008 bind threshold ownership, band-edge binding, and band-threshold identity-hash evidence to the existing compat/admin threshold surface and Magic-10 threshold source. CHECK po-009 and po-010 bind category-framework, per-channel mechanics, and fail-closed generated-proof-family visibility to existing offline proof families. Check-scoped evidence remediations and accepted deviations inside these checks are offline ledger updates only; these checks do not create a second threshold home, second category-framework home, public route, flag, serializer path, public contract, epic-level QA PASS by themselves, Live QA completion by themselves, PF09 status change, or epic closure.  
* **Authoritative plus supplemental gate-family posture (names-only).** When one offline canonical-gate flow still produces both the authoritative `audit/gates/json_gate/canonical/` family and a supplemental legacy `audit/gates/canonical_json/` family, architecture treats both families as one same-change evidence event inside the offline plane.  
* **Coherence across still-produced families.** If either family changes, current companion path proofs and ledger refresh apply to every changed family that still participates in that run. The supplemental legacy family remains continuity evidence only; it does not create a second truth home, a second runtime surface, or a second Presenter path.  
* **Epic QA step-manifest surface (names-only).** Within this same offline evidence plane, the current-state epic QA ledger uses a `qa_step_logs_manifest.json` manifest with a sibling `qa_step_logs_manifest.json.path_proof.txt`, together with check-scoped `primary.log` files under the epic QA `checks/` subtree.  
* **EPIC030 traceability and reused-history QA-ledger surfaces (names-only).** CHECK po-011 binds traceability state across required PR-slice artifacts, Human Evidence Index, and Machine Evidence Index. CHECK po-012 classifies reused-history rows separately from active HDE-EPIC030 rows and records no new implementation claim for reused-history rows. These are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, new proof families, or close-pack completion by themselves.  
* **EPIC030 source-of-truth and all-slice coherence QA-ledger surfaces (names-only).** CHECK po-013 and CHECK po-014 are check-scoped offline QA surfaces under `audit/qa/hde-epic030/checks/po-013/` and `audit/qa/hde-epic030/checks/po-014/`. CHECK po-013 binds `primary.log` and `source_of_truth_posture.txt` to the separation between repo-supported completion, canon-drain completion, and formal close-pack completion. CHECK po-014 binds `primary.log`, `all_slice_coherence.json`, and `exit_code.txt` to the post-implementation all-slice coherence proof across prior primary logs and PR-01 through PR-05 core artifacts. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, new public routes, new proof families, PF-canon drainage, or close-pack completion by themselves.  
* **EPIC030 discovery, QA RCA, and documentation-drainage QA-ledger surfaces (names-only).** CHECK po-015, CHECK po-016, and CHECK po-017 are check-scoped offline QA surfaces under `audit/qa/hde-epic030/checks/po-015/` through `audit/qa/hde-epic030/checks/po-017/`. CHECK po-015 binds `primary.log`, `discovery.json`, and `discovery_validation.txt` to baseline execution-context discovery. CHECK po-016 binds `primary.log` and `audit/EPIC-030_QA_RCA.md` to final QA interpretation and required RCA sections. CHECK po-017 binds `primary.log` and `documentation_drainage_posture.txt` to the non-blocking documentation-drainage posture while preserving real truth-and-proof blockers. These surfaces do not create runtime routes, public surfaces, new Presenter paths, PF09.2 status changes, or close-pack completion by themselves.  
* **EPIC030 closeout proof-class separation (names-only).** For EPIC030 architecture, repo-supported completion, canon-drain completion, and formal close-pack completion are separate offline states. Runtime and implementation proof may support QA interpretation, but Architecture recognizes no PF09.2 drainage or close-pack completion unless the governed close-pack or later-drain surface is separately present and bound.  
* **Authoritative-family posture (names-only).** Within the offline evidence plane, any governed evidence family used for bounded closeout, OPS validation, or acceptance binding carries one authoritative closure posture at a time. Architecture does not recognize contradictory family states as a valid proof surface.  
* **Documentation/evidence normalization posture (names-only).** When runtime facts are unchanged and only closure interpretation changes, a bounded normalization pass may rewrite the affected governed family, its index or mirror companions, and required path proofs without creating a new runtime route, a new A7 surface, or a second truth home.  
* **EPIC030 OPS-03 close-pack surfacing surfaces (names-only).** OPS-03 is an evidence-packaging and close-pack surfacing surface for HDE-EPIC030. The canonical close-pack pair is `audit/EPIC-030_close_report.md` and `audit/EPIC-030_MANIFEST.json`, with sibling path proofs and a named `key_outputs` map binding close report, manifest, acceptance map, QA RCA, QA step manifest, token matrix, doc deltas, drain targets, OPS-03 final evidence inventory, and created-files checksum ledger outputs. This packaging surface binds existing QA and implementation proof families; it does not create a runtime route, public surface, A7 proof surface, Presenter path, implementation delta, PF-canon edit, PF09.2 drain, new acceptance claim, or vendor execution.  
* **EPIC030 OPS-03 support-evidence family (names-only).** The OPS-03 support family records corrected command transcript, labeled stdout, stderr, exit-code evidence, final evidence inventory, inventory path proof, final validation log, and created/refreshed file checksum ledger under `audit/ops/hde-epic030/ops-03/`. These artifacts are offline packaging and validation evidence only; they do not alter Reader, CLI, compat, sampler, BodyGraph, or Presenter runtime behavior.  
* **EPIC030 formal close-pack separation (names-only).** Formal close-pack surfacing can be recorded by the canonical close-pack pair and bound support family while PF09.2 later-drain support remains recorded but not drained. Architecture treats that as offline closure-state classification, not as an immediate checklist status change or new engine component.  
* **EPIC030 final closeout synthesis surface (names-only).** The HDE-EPIC030 final closure review, QA RCA, and Lead Dev Epic Retrospective are offline synthesis artifacts that consolidate PR-slice outcomes, Live QA check outcomes, remediation loops, OPS-02 and OPS-03 proof posture, closure-trace satisfaction, and ready-with-caveats recommendation. Architecture treats this synthesis as a traceability and interpretation surface over existing proof families; it does not create a runtime route, public surface, A7 proof surface, Presenter path, implementation delta, PF09.2 drainage, PO closeout action, or acceptance claim by itself.  
* **EPIC031 PR-01 provider-gate evidence surfaces (names-only).** HDE-EPIC031 PR-01 binds the existing vendor seam provider-gate proof through governed or indexed offline artifacts at `artifacts/vendor/policies_pinned.md`, `artifacts/vendor/retry_after_parse.log`, `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json`, `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json`, and `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json`, with Human Evidence Index and Machine Evidence Index linkage. This evidence family records local deterministic provider-gate posture, no-live-vendor proof, retry/backoff and typed-provider outcome posture, and classified proof-refresh side effects for the existing vendor seam; it does not create a runtime route, public Reader change, HDAPI v2 runtime-conformance claim, open-rails smoke, second evidence home, or PF09 status change by itself.  
* **EPIC031 PR-02 vendor observability evidence surfaces (names-only).** HDE-EPIC031 PR-02 binds the existing vendor seam log posture through governed offline artifacts at `audit/qa/hde-epic031/pr-02/bounded_label_observability.json`, `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`, `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`, `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`, and `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`, plus the local job definition `ci/jobs/logs_keys_only_redaction.yml`, with Human Evidence Index and Machine Evidence Index linkage. This evidence family records bounded labels, success/failure class observability, payload-body absence, plaintext-secret absence, raw-secret-header absence, and PR-specific vendor evidence binding for the existing vendor seam; it does not create a runtime route, public surface, second evidence home, or PF09 status change by itself.  
* **EPIC031 PR-03 evidence/index coherence surfaces (names-only).** HDE-EPIC031 PR-03 binds PR-01, PR-02, and PR-03 SAFE rails proof families through governed offline evidence at `audit/qa/hde-epic031/pr-03/evidence_family_map.json`, `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`, and `audit/qa/hde-epic031/pr-03/evidence_refresh.log`, with companion path proofs and Human Evidence Index, hash sentinel, Machine Evidence Index, checksum, and path-proof linkage. This family records evidence/index coherence for the existing vendor seam and SAFE rails proof families; it does not create a runtime route, public Reader change, HDAPI v2 runtime-conformance claim, Live QA runbook, closeout surface, token-matrix rows, PF-Canon edit, open-rails smoke, or PF09 status change by itself.  
* **EPIC031 PR-03 side-effect classification posture (names-only).** When PR-03 evidence refreshes outside-family governed proof companions, including writer, topology, and HDE-EPIC030 PR-03, PR-04, and PR-05 proof companion families, Architecture treats those refreshed families as bounded evidence-refresh side effects only when the run evidence names the affected proof-companion paths and matching Machine Evidence Index rows and classifies them as expected updater convergence, required dependency refresh, or unexpected drift. Side-effect validation is fail-closed: missing paths, invalid proof companions, or stale mirror `sha256` / `size_bytes` bindings do not produce a PASS-grade PR-03 coherence surface.  
* **EPIC031 shared-evidence path separation (names-only).** PR-specific vendor evidence for HDE-EPIC031 remains separate from shared DB-bridge evidence families; restoring shared paths and moving vendor samples under `audit/qa/hde-epic031/pr-02/` is architecture-neutral evidence binding and does not rename the DB-bridge surface or vendor seam.  
* **EPIC031 Step-0 setup and doc-delta QA-ledger surfaces (names-only).** Step-0A and Step-0B are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/step-0a-discovery/` and `audit/qa/hde-epic031/checks/step-0b-doc-delta/`, supported by `audit/qa/hde-epic031/00_meta/live_qa_harness.py`, `audit/docdeltas/hde-epic031_doc_deltas.md`, and `audit/qa/hde-epic031/00_meta/doc_deltas.md`. These surfaces bind discovery, stable check-root posture, and doc-delta capture for the existing HDE-EPIC031 SAFE rails evidence flow. They do not create runtime behavior, public surfaces, implementation deltas, HDAPI v2 runtime conformance, Live QA completion, or close-pack completion by themselves.  
* **EPIC031 first-slice boundary and closed-provider QA-ledger surfaces (names-only).** CHECK po-001, CHECK po-002, and CHECK po-003 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-001/` through `audit/qa/hde-epic031/checks/po-003/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-001 binds first Fermentation slice scope boundary and no public-surface widening. CHECK po-002 binds closed-by-default provider access, bounded opening evidence, and no-live-vendor policy. CHECK po-003 binds deterministic typed provider refusal before unsafe vendor input or ingest. These surfaces bind existing vendor seam and SAFE rails proof posture; they do not create a runtime route, public Reader change, public route, public flag, HDAPI v2 runtime conformance, open-rails smoke, second evidence home, PF09 status change, or close-pack completion by themselves.  
* **EPIC031 retry, rate-limit, and keys-only QA-ledger surfaces (names-only).** CHECK po-004, CHECK po-005, and CHECK po-006 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-004/` through `audit/qa/hde-epic031/checks/po-006/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-004 binds bounded retry/backoff, pinned attempts, and non-success classification. CHECK po-005 binds typed 429 handling and Retry-After parsing posture. CHECK po-006 binds keys-only vendor diagnostics and payload-body, plaintext-secret, and raw-secret-header absence. A Moon Loop correction inside po-006 is a QA-created harness and evidence-stream correction only; it does not alter product runtime behavior or create a new architecture surface.  
* **EPIC031 redaction and coherence QA-ledger surfaces (names-only).** CHECK po-007, CHECK po-008, and CHECK po-009 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-007/` through `audit/qa/hde-epic031/checks/po-009/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-007 binds sensitive-provider-material absence and live-vendor-call prohibition. CHECK po-008 binds governed evidence coherence, PR-03 coherence, validator success, hash-sentinel and path-proof posture, and an auditable Moon Loop from failure signature to rerun PASS. CHECK po-009 binds machine-mirror and human evidence-family-map alignment. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, HDAPI v2 runtime conformance, open-rails smoke, second evidence homes, PF09 status changes, or close-pack completion by themselves.  
* **EPIC031 fail-closed, acceptance-boundary, and subtask-support QA-ledger surfaces (names-only).** CHECK po-010, CHECK po-011, and CHECK po-012 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-010/` through `audit/qa/hde-epic031/checks/po-012/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-010 binds generated-proof fail-closed posture across PR-01, PR-02, and PR-03 after the prior PR-01 generator check-mode blocker is resolved. CHECK po-011 binds acceptance-claim boundary, no unsupported acceptance-token claim, and missing close-stage acceptance artifacts as non-runtime behavior posture. CHECK po-012 binds supportability for `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4` without claiming PF09.5 drainage. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, acceptance tokens, token-matrix rows, public routes, PF09.5 drainage, parent-task movement, or close-pack completion by themselves.  
* **EPIC031 truth-class and readiness-separation QA-ledger surfaces (names-only).** CHECK po-013, CHECK po-014, and CHECK po-015 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-013/` through `audit/qa/hde-epic031/checks/po-015/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-013 binds reused-foundation history-only posture and active-slice limitation to `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4`. CHECK po-014 binds prior-log presence and prevents final QA outcome from being inferred from implementation readiness alone. CHECK po-015 binds implementation readiness, QA readiness, final QA outcome, and documentation drainage as separate truth classes, with documentation drainage not acting as a QA blocker by itself. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, PF09.5 drainage, final QA outcome by implementation readiness alone, or close-pack completion by themselves.  
* **EPIC031 vendor-nonclaim and proof-only QA-ledger surfaces (names-only).** CHECK po-016, CHECK po-017, and CHECK po-018 are check-scoped offline QA surfaces under `audit/qa/hde-epic031/checks/po-016/` through `audit/qa/hde-epic031/checks/po-018/`, each using `primary.log` and `result.json` as the check-local proof pair. CHECK po-016 binds vendor-version runtime conformance as not claimed and no-live-vendor policy as visible. CHECK po-017 binds live-vendor behavior as not claimed and live-vendor calls as forbidden. CHECK po-018 binds Live QA as proof-only and records no implementation, remediation, PF edit, or closeout action by Live QA. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, HDAPI v2 runtime conformance, live vendor behavior proof, Live QA remediation authority, PF-canon edits, or closeout completion by themselves.  
* **EPIC031 QA RCA, closeout review, and retrospective synthesis surface (names-only).** The HDE-EPIC031 QA RCA, final closeout review, Lead Dev Epic Retrospective, and docs-only final repo-docs sweep are offline synthesis and navigation artifacts that consolidate PR-01 provider policy, PR-02 log/redaction posture, PR-03 evidence/index coherence, Step-0A/Step-0B, PO-001 through PO-018, remediation loops, PF23 current-reality context, source-of-truth posture, path and surface ledgers, evidence and proof-boundary defects, repo-doc navigation updates, and ready-with-caveats interpretation. Architecture treats this synthesis as traceability and interpretation over existing proof families and check-scoped QA surfaces; it does not create a runtime route, public Reader contract, public route, public flag, public payload field, HDAPI v2 runtime-conformance claim, DB runtime acceptance, narrative/router closure, Live QA runbook, PF-Canon edit, implementation delta, acceptance claim, PF09.5 drainage, parent-task movement, formal close-pack completion, PO closeout action, or epic close by itself.  
* **EPIC031 satisfied closure-trace posture (names-only).** HDE-EPIC031 is recorded as SATISFIED for this review’s closure trace only. PF02 records that posture as an offline interpretation over existing proof families, not as a PO closeout action. PR-01, PR-02, and PR-03 support the active first-slice Fermentation subtasks `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4`; Step-0A, Step-0B, and PO-001 through PO-018 are recorded PASS, including accepted Moon Loop remediation where needed; PF10 records the final QA RCA verdict as READY WITH CAVEATS; and PF23 context does not override PF10’s QA outcome record.  
* **EPIC031 remaining-caveat separation (names-only).** Formal close-pack completion, PF09.5 drainage, parent `HDE-FERM001` status posture, HDAPI v2 runtime conformance, DB bridge/runtime acceptance, narrative/router closure, documentation drainage, PF09.5 status movement, and deferred later Fermentation work remain separate offline closeout, later-drain, or later-slice concerns. PF02 records no formal close-pack completion, PF09.5 drained status, parent-task movement, HDAPI v2 runtime conformance, DB runtime acceptance, narrative registry closure, router parity closure, PO closeout action, or epic close unless the governed close-pack, QA, or later-drain surface is separately present and bound.  
* **EPIC032 PR-01 narrative-router evidence surfaces (names-only).** HDE-EPIC032 PR-01 binds existing narrative-router behavior through governed offline evidence at `audit/gates/narratives/keys_10x4.table.json`, `artifacts/narratives/router/parity_abba.log`, and `artifacts/narratives/router/cli_http_parity.log`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This evidence family records 10-category by 4-band router matrix coverage, missing-key fail-closed behavior, two-run identity, AB↔BA coherence where applicable, CLI/HTTP parity where defined, keys-only and no-prose router evidence, canonical JSON proof, and public Reader unchanged posture for existing Aux/CLI narrative-router surfaces. It does not create PR-02 registry work, PR-03 or PR-04 DB work, HDAPI v2 work, OPS work, public Reader contract changes, a new public route, a new Presenter path, narrative registry closure, PF09 status change, or epic close by itself.  
* **EPIC032 PR-02 narrative-registry evidence surfaces (names-only).** HDE-EPIC032 PR-02 binds existing narrative registry diffing, Doc-Delta identity, and pack identity behavior through governed offline evidence at `audit/gates/narratives/registry.diff.json`, `audit/gates/narratives/pack_identity.txt`, and `audit/docdeltas/hde-epic032_doc_deltas.md`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This evidence family records keys-only and no-prose registry diffing, pack identity from canonical manifest bytes, same-bytes two-run identity, Doc-Delta binding, index and mirror binding, hash sentinels, path proofs, sanity-pipeline generator ordering, fail-closed registry validation, and orientation evidence remediation for existing narrative-pack and registry proof surfaces. It does not create new narrative runtime behavior, a public Reader contract change, a public route, a Presenter path, PR-03 or PR-04 DB work, HDAPI v2 work, OPS work, PF-Canon edits, acceptance tokens, PF09 status movement, narrative registry closure, or epic close by itself.  
* **EPIC032 PR-02 shared evidence-refresh posture (names-only).** Non-PR-02 path-proof, mirror, hash, orientation, or companion refreshes that occur in the same governed tooling run are architecture-neutral evidence refresh when classified as shared canonical tooling behavior. This includes refreshed PR-01 router proof companions, writer proof companions, historical EPIC030 proof companions, topology or orientation evidence, Human Evidence Index companions, and Machine Evidence Index companions. These refreshes do not reopen prior implementation scopes, rename prior surfaces, create new proof surfaces, or change runtime behavior.  
* **EPIC032 PR-03 DB bridge/provider-parity evidence surfaces (names-only).** HDE-EPIC032 PR-03 binds existing BodyGraph DB resolver and DB provider façade behavior through governed offline evidence at `artifacts/db_bridge/adapter_selection.snapshot.json`, `artifacts/db_bridge/provider_parity.proof.json`, and `artifacts/runtime/env_connectivity.snapshot.json`, with sibling path proofs and Human Evidence Index and Machine Evidence Index linkage. This evidence family records deterministic dev fallback from direct provider selection to bridge, bridge capability, deterministic direct/bridge provider corpus, provider-parity harnessing, false-PASS parity guards, structural adapter-selection `selection_order` derived from observed DBAccess attempts/provider order, canonical adapter-selection key posture, and secret-free evidence for the existing `DBAccess` façade and BodyGraph DB resolver. PR-routed remediation may stabilize the structural `selection_order` contract and fail-closed generator validation without converting that remediation into bounded Moon Loop correction. Unavailable direct-provider rows remain unavailable or skipped rather than false PASS. It does not create a new DB home, a second BodyGraph store, a new request-path mode, a production bridge exception, a live provider-parity PASS claim under closed rails, a public route, a Presenter path, an acceptance-token claim, a PF09 status change, QA PASS by itself, or epic close by itself.  
* **EPIC032 PR-03 shared evidence-refresh posture (names-only).** PR-03 may refresh path proofs, mirror rows, hash sentinels, orientation evidence, Human Evidence Index companions, Machine Evidence Index companions, PR-01 router proof companions, PR-02 registry and Doc-Delta proof companions, writer proof companions, and historical EPIC030 proof companions as governed evidence-tool churn when classified as shared refresh behavior. These refreshes do not reopen prior implementation scopes, rename prior surfaces, create new proof surfaces, alter runtime behavior, or change narrative, writer, topology, EPIC030, or EPIC032 PR-01/PR-02 behavior.  
* **EPIC032 PR-03 canonical adapter-selection key posture (names-only).** The canonical adapter-selection artifact key posture binds `artifacts/db_bridge/adapter_selection.snapshot.json` to the canonical `db_bridge.adapter_selection.snapshot` evidence identity. Superseded EPIC-specific adapter-selection keys are not recognized as alternate architecture surfaces. PF02 records the evidence-surface identity relationship only; mirror schema, proof-anchor mechanics, token posture, and CI enforcement remain outside Architecture.  
* **EPIC032 OPS-01 provider-parity closure evidence surfaces (names-only).** OPS-01 binds the existing BodyGraph DB resolver and DB provider façade through governed OPS evidence under `audit/ops/hde-epic032/db-provider-parity/`, including `provider_parity_closure_decision.json`, `provider_parity.proof.json`, `bridge_consistency_result.txt`, `created_files_sha256.txt`, command transcript, stdout/stderr, exit-code, env-posture, adapter-selection, and env-connectivity evidence. This closure packet records `provider_parity_closure_status: closed`, active corpus rows `grants`, `search_path`, `select_one`, and `ddl_fingerprint` as non-skipped matching rows, and OPS-01 as a close candidate. It is OPS evidence only and does not create QA PASS, PF09 status movement, epic closure, acceptance-token satisfaction, a new DB home, a second BodyGraph store, a public route, or a Presenter path.  
* **EPIC032 PR-04 non-dev failure and DB evidence-coherence surfaces (names-only).** HDE-EPIC032 PR-04 binds non-dev typed DB failure and DB evidence coherence through governed offline evidence at `artifacts/runtime/env_connectivity.nondev_failure.json`, together with PR-04 Human Evidence Index, Machine Evidence Index, hash-sentinel, and path-proof linkage, and OPS-01 closure-decision evidence as non-claiming OPS evidence. This evidence family records corrected `APP_ENV=stage` non-dev failure semantics, real observed DBAccess attempt order, typed `BridgeUnavailable` / `missing_bridge_url` refusal, no proactive probes, numeric-free public failure posture, secret-free artifact posture, fail-closed generator behavior, and targeted regression coverage. It does not create a new DB home, a second BodyGraph store, a new request-path mode, a production bridge exception, a live provider-parity PASS claim under closed rails, a public route, a Presenter path, an acceptance-token claim, a PF09 status change, or epic close by itself.  
* **EPIC032 PR-04 shared evidence-refresh posture (names-only).** PR-04 may refresh DB boundary, schema, DDL, grants, partition, provider-parity, bridge, writer, narrative-router, Doc-Delta, topology, historical EPIC030, Human Evidence Index, Machine Evidence Index, hash-sentinel, and path-proof companions as governed evidence-tool churn when classified as shared refresh behavior. These refreshes do not reopen prior implementation scopes, rename prior surfaces, create new proof surfaces, alter runtime behavior, or change narrative, writer, topology, EPIC030, or earlier EPIC032 PR behavior.  
* **EPIC032 implementation retrospective and docs-sweep surfaces (names-only).** The HDE-EPIC032 implementation retrospective and docs-only final repo-docs sweep are offline synthesis and navigation artifacts that consolidate Fermentation Pass 3 outcomes: PR-01 narrative router parity and indexing, PR-02 narrative registry diffing and identity, PR-03 DB bridge fallback and provider-parity harnessing, OPS-01 provider-parity closure evidence, PR-04 non-dev typed DB failure and evidence coherence, and repo-facing docs updates to README.md, CHANGELOG.md, AGENTS.md, and docs/INDEX.md. Architecture treats this synthesis as traceability over existing proof families and docs surfaces; it does not create a runtime route, public Reader contract change, public route, public flag, public payload field, HDAPI v2 runtime-conformance claim, implementation delta, PF-Canon edit, acceptance-token claim, PF09 status movement, or epic close by itself.  
* **EPIC032 combined-evidence QA-readiness supportability posture (names-only).** The combined PR-03, OPS-01, and PR-04 evidence chain supports `HDE-FERM004.2` to Done for QA-readiness purposes: PR-03 provides DB bridge fallback, bridge capability proof, deterministic provider-parity harnessing, false-PASS parity guards, evidence-index binding, and canonical adapter-selection key remediation; OPS-01 provides provider-parity closure evidence as OPS evidence; and PR-04 provides non-dev typed DB failure behavior plus DB evidence, index, mirror, and path-proof coherence. This records supportability for QA readiness only and does not claim PF09.5 has been edited, `HDE-FERM004.2` is already marked Done in PF09.5, QA has already passed, the epic is closed, live vendor behavior is proven, HDAPI v2 runtime conformance is complete, OPS-01 is QA evidence, or any DB proof-label string is a registered acceptance token.  
* **EPIC032 Step-0 setup and doc-delta QA-ledger surfaces (names-only).** Step-0A and Step-0B are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/step-0a-discovery/` and `audit/qa/hde-epic032/checks/step-0b-doc-delta/`, supported by `audit/qa/hde-epic032/00_meta/live_qa_harness.py`, `audit/qa/hde-epic032/qa_step_logs_manifest.json`, `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`, `audit/docdeltas/hde-epic032_doc_deltas.md`, and `audit/qa/hde-epic032/00_meta/doc_deltas.md`. Step-0A also records bounded Moon Loop harness correction evidence under `audit/qa/hde-epic032/00_meta/delta/`. These surfaces bind discovery, stable check-root posture, doc-delta capture, captured closed-rails environment, and remediated setup provenance for HDE-EPIC032 Live QA. They do not create runtime behavior, public surfaces, implementation deltas, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 first Live QA ledger surfaces (names-only).** CHECK po-001, CHECK po-002, and CHECK po-003 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-001/` through `audit/qa/hde-epic032/checks/po-003/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-001 binds Fermentation Pass 3 scope-boundary posture, Reader and dev Reader catalog visibility, OPS-evidence non-conversion into QA PASS, and DB proof-label non-conversion into acceptance tokens. CHECK po-002 binds narrative-router deterministic key-selection evidence. CHECK po-003 binds keys-only router proof, public Reader non-expansion, and `APP_ENV` gating visibility for internal/dev surfaces. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, public Reader expansion, acceptance tokens, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 narrative-router and registry Live QA ledger surfaces (names-only).** CHECK po-004, CHECK po-005, and CHECK po-006 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-004/` through `audit/qa/hde-epic032/checks/po-006/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-004 binds narrative-router identity criteria through `artifacts/narratives/router/parity_abba.log`. CHECK po-005 binds registry diff and pack identity through `audit/gates/narratives/registry.diff.json` and `audit/gates/narratives/pack_identity.txt`. CHECK po-006 binds registry non-overclaim and keys-only router proof through `audit/gates/narratives/keys_10x4.table.json`. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, public Reader contract changes, acceptance tokens, PF09.5 drainage, QA PASS by themselves, narrative registry closure by themselves, or close-pack completion by themselves.  
* **EPIC032 registry, DB bridge, and OPS-support Live QA ledger surfaces (names-only).** CHECK po-007, CHECK po-008, and CHECK po-009 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-007/` through `audit/qa/hde-epic032/checks/po-009/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-007 binds registry diff, pack/evidence support, and governed doc-delta posture. CHECK po-008 binds DB bridge/provider parity generator proof, provider-parity evidence, adapter-selection evidence, OPS closure visibility, and combined DB/OPS proof-chain posture without implementation-only or OPS-only overclaim. CHECK po-009 binds OPS provider parity evidence as visible support evidence while preserving no QA PASS, no checklist completion, and no epic-closure claim by OPS evidence alone. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, acceptance tokens, PF09.5 drainage, QA PASS by themselves, checklist completion by themselves, or close-pack completion by themselves.  
* **EPIC032 selection-order and supportability Live QA ledger surfaces (names-only).** CHECK po-010, CHECK po-011, and CHECK po-012 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-010/` through `audit/qa/hde-epic032/checks/po-012/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-010 binds structural `selection_order` evidence from `artifacts/db_bridge/adapter_selection.snapshot.json`, derived from observed adapter attempts/provider order, and records non-QA-root generator remediation as PR-routed rather than bounded Moon Loop-only correction. CHECK po-011 and CHECK po-012 bind the remaining supportability and evidence-boundary posture for the DB bridge/provider parity proof chain while preserving empty intended and claimed token posture. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, acceptance tokens, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 evidence-coherence, mirror-alignment, and fail-closed QA-ledger surfaces (names-only).** CHECK po-013, CHECK po-014, and CHECK po-015 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-013/` through `audit/qa/hde-epic032/checks/po-015/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-013 binds evidence-index coherence through Human Evidence Index, Machine Evidence Index, and command-check proof. CHECK po-014 binds Human/Machine evidence loci and Machine Mirror alignment proof. CHECK po-015 binds generated-proof fail-closed check posture through green generator and command checks. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, acceptance tokens, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 proof-label, fallback, and active-family QA-ledger surfaces (names-only).** CHECK po-016, CHECK po-017, and CHECK po-018 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-016/` through `audit/qa/hde-epic032/checks/po-018/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-016 binds DB proof-label non-token posture and prevents DB provider/bridge proof labels from being overread as acceptance tokens. CHECK po-017 binds dev bridge-fallback scope and prevents fallback proof from being broadened beyond its governed dev scope. CHECK po-018 binds active evidence-family presence while preserving PF09.5 physical drainage as not claimed. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, acceptance tokens, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 reused-foundation, truth-class, and vendor-nonclaim QA-ledger surfaces (names-only).** CHECK po-019, CHECK po-020, and CHECK po-021 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-019/` through `audit/qa/hde-epic032/checks/po-021/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-019 binds reused-foundation posture and prevents historical foundation work from being re-scoped as new HDE-EPIC032 implementation. CHECK po-020 binds truth-class separation across OPS evidence, QA result, PF09.5 drainage, and final closeout. CHECK po-021 binds vendor-version runtime conformance as not claimed. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, vendor-version runtime conformance, acceptance tokens, PF09.5 drainage, final closeout, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 live-provider, Reader non-expansion, and proof-only QA-ledger surfaces (names-only).** CHECK po-022, CHECK po-023, and CHECK po-024 are check-scoped offline QA surfaces under `audit/qa/hde-epic032/checks/po-022/` through `audit/qa/hde-epic032/checks/po-024/`, each using `primary.log`, `primary.log.path_proof.txt`, and `result.json` as the check-local proof set. CHECK po-022 binds live-provider behavior as not claimed from local proof. CHECK po-023 binds public Reader non-expansion by preserving `/reader` as visible and rejecting an invented proof route. CHECK po-024 binds Live QA as proof-only and records no implementation, PF edit, OPS edit, evidence-index edit, token-map edit, public route edit, Reader adapter edit, public payload edit, public flag edit, or closeout action by Live QA. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, public Reader contract changes, live-provider behavior proof, acceptance tokens, PF09.5 drainage, QA PASS by themselves, or close-pack completion by themselves.  
* **EPIC032 epic closure review, QA RCA, and retrospective synthesis surface (names-only).** The HDE-EPIC032 epic closure review, final QA closeout review, QA RCA, and Lead Dev Epic Retrospective are offline synthesis artifacts that consolidate Fermentation Pass 3 scope, the deliverables register, closure trace ledger, path and surface reality ledger, PF23 current-reality context, PR-01 through PR-04 implementation and remediation loops, OPS-01 provider-parity closure evidence, Step-0A/Step-0B, PO-001 through PO-024, manifest/header/path-proof trust restoration, token overclaim remediation, Moon Loop versus PR-routed remediation boundary, structural `selection_order` proof remediation, documentation drainage posture, and final READY recommendation. Architecture treats this synthesis as traceability and interpretation over existing proof families and check-scoped QA surfaces; it does not create a runtime route, public Reader contract change, public route, public flag, public payload field, HDAPI v2 runtime-conformance claim, implementation delta, PF-Canon edit, acceptance-token claim, PF09.5 drainage, PO closeout action, or epic close by itself.  
* **EPIC032 SATISFIED closure-trace posture (names-only).** HDE-EPIC032 is recorded as SATISFIED for this review’s closure trace only. The SATISFIED label maps the Implementation Guide deliverables to PF10-recorded implementation, ADR, remediation, QA, and evidence-pointer records; it does not perform PO closeout. PF10 records the full Live QA ladder from Step-0A/Step-0B through PO-024 as PASS, final readiness as Ready for epic closeout, DB provider/bridge proof-label names as non-token proof labels unless Governance admits them, PO-010 remediation as PR-routed structural `selection_order` proof, and PF23 as current-reality context rather than closure proof.  
* **EPIC032 final QA readiness and closeout-separation posture (names-only).** PF10 records all HDE-EPIC032 Live QA step clusters from Step-0A/Step-0B through PO-024 as PASS after remediation where applicable, and the final recommendation is READY for this review’s implementation posture. The strongest closeout proof clusters are PO-010/PO-011/PO-012 after PR-routed `selection_order` remediation, PO-013 through PO-018 after manifest/header proof remediation, PO-019 through PO-024 for non-claim boundaries and proof-only QA posture, and the closure trace ledger for all D1 through D5 deliverables. Documentation deltas and PF09.5 physical drainage are not closure blockers by themselves when PF10 has the relevant live supportability record. PF02 records no physical PF09.5 drainage, no formal close-pack completion, no direct current filesystem proof after the docs PR, no PO closeout action, and no epic close unless the governed close-pack, QA, or later-drain surface is separately present and bound.  
* **EPIC033 PR-01 HDAPI v2 contract-inventory evidence surfaces (names-only).** HDE-EPIC033 PR-01 binds HDE-FERM006 inventory-only vendor-contract evidence through governed offline artifacts at `artifacts/vendor/hdapi_v2/source_inventory.json`, `artifacts/vendor/hdapi_v2/source_inventory.md`, `artifacts/vendor/hdapi_v2/openapi_validation.log`, `artifacts/vendor/hdapi_v2/known_anomalies.md`, `artifacts/vendor/hdapi_v2/endpoint_reference.csv`, `artifacts/vendor/hdapi_v2/contract_map.json`, `docs/acceptance_map_epic033.json`, `audit/qa/hde-epic033/token_evidence_matrix.md`, `audit/qa/hde-epic033/acceptance_map_viability.log`, `audit/docdeltas/hde-epic033_doc_deltas.md`, `audit/qa/hde-epic033/00_meta/doc_deltas.md`, `docs/evidence/INDEX.json`, and `artifacts/evidence_index.jsonl`, with sibling path proofs, hash sentinels, and Human Evidence Index / Machine Evidence Index linkage. This evidence family records source inventory, route-spec validation, known-anomaly quarantine, endpoint reference, contract map, source-cache input binding, acceptance-map posture, token-evidence-matrix posture, and viability proof for the inventory-only HDE-FERM006 slice. It does not create HDE-FERM007 or HDE-FERM008 runtime request shaping, response normalization implementation, live vendor conformance, open-rails vendor smoke, public Reader changes, new HTTP homes, vendor-v2-specific tokens, AI scope, PF09 status movement, or epic close by itself.  
* **EPIC033 PR-01 route-family inventory posture (names-only).** The contract inventory distinguishes recommended v2 chart route families (`POST /v2/charts`, `POST /v2/charts/simple`, `POST /v2/charts/coordinates`) from explicit legacy v1 BodyGraph route families (`POST /v1/bodygraphs`, `POST /v1/bodygraphs/simple`). PF02 records that inventory relationship only; request fields, auth model, geocode-key requirement, tiers, success/error envelopes, source specs, validation logs, and schema/mirror mechanics remain routed by title to owning documents.  
* **EPIC033 PR-01 documentation-discovery and shared-refresh posture (names-only).** AI/LLM-oriented vendor documentation, including `llms.txt` and `llms-full.txt` when inspected, is documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope. Collateral path-proof, orientation, index, mirror, or companion refreshes outside the HDAPI v2 family are architecture-neutral evidence-tooling convergence when validated and classified as refresh behavior; they do not alter product behavior, introduce feature or contract scope, reopen prior implementation scope, rename prior surfaces, create new proof surfaces, or change runtime behavior.  
* **EPIC033 implementation retrospective, Lead Dev retrospective, and docs-sweep surfaces (names-only).** The HDE-EPIC033 implementation retrospective, Lead Dev Epic Retrospective, and repo-facing docs sweep are offline synthesis and navigation artifacts that consolidate Fermentation Pass 4 outcomes: HDE-FERM006 inventory-only HumanDesignAPI v2 and legacy v1 contract evidence, PR-01 source inventory and contract-map proof, source-cache and quarantine posture, generated evidence/index/mirror/path-proof updates, deliverables register D1 through D5, QA verification register Step-0B through qa-16, PF10 result register, and repo-doc updates to README.md, CHANGELOG.md, AGENTS.md, docs/INDEX.md, and docs/EVIDENCE\_INDEX.md. Architecture treats this synthesis as traceability over existing proof families and docs surfaces; it does not create runtime v2 conformance, request shaping implementation, response normalization implementation, public Reader changes, open-rails vendor smoke, new HTTP homes, AI scope, implementation deltas, PF-Canon edits, PF09 status movement, formal close-pack completion, PO closeout action, or epic close by itself.  
* **EPIC033 HDE-FERM006 supportability and closeout-separation posture (names-only).** HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 are supportable to Done for this closure trace from the PR-01 inventory-only evidence family and PF10-recorded QA results. PF02 records no physical PF09.5 drainage, no formal close-pack completion, no PO closeout action, no runtime HumanDesignAPI v2 conformance, and no epic close unless the governed checklist, close-pack, QA, or later-drain surface is separately present and bound. HDE-FERM007 and HDE-FERM008 remain future work for source selection, request shaping, response normalization, adapter-boundary proof, closed-rails adapter proof, live conformance, and PO-only open-rails conformance evidence.  
* **EPIC033 Step-0B doc-delta QA-ledger surface (names-only).** CHECK step-0b-doc-delta-capture is a check-scoped offline QA surface under `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/`, with `primary.log`, `primary.log.path_proof.txt`, `audit/docdeltas/hde-epic033_doc_deltas.md`, `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`, `audit/qa/hde-epic033/00_meta/doc_deltas.md`, and `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`. This surface binds doc-delta capture, path-proof trust, governed audit-root posture, closed-rails execution, and no-delta baseline posture for PR-01 contract-inventory evidence binding. It does not create runtime behavior, implementation deltas, PF09.5 drainage, QA PASS beyond this step, formal close-pack completion, or broader HDE-EPIC033 closure by itself.  
* **EPIC033 source-inventory, AI-boundary, and test QA-ledger surfaces (names-only).** CHECK po-001, CHECK po-002, and CHECK po-003 are check-scoped offline QA surfaces under `audit/qa/hde-epic033/checks/po-001/` through `audit/qa/hde-epic033/checks/po-003/`, each using `primary.log` and sibling path-proof evidence as the check-local receipt set. CHECK po-001 binds source inventory grounding through closed-rails source-cache evidence, `source_inventory.json`, `source_inventory.md`, route source-cache files, `cache_path`, and `cache_sha256`. CHECK po-002 binds AI/LLM vendor documentation as documentation-discovery-only context that creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope. CHECK po-003 binds targeted test posture for the PR-01 contract-inventory evidence family. These checks are offline QA-ledger classifications only; they do not create runtime v2 conformance, source-selection implementation, request shaping, public Reader changes, open-rails vendor smoke, new HTTP homes, AI scope, PF09.5 drainage, or broader HDE-EPIC033 closure by themselves.  
* **EPIC033 quarantine, route-family, and contract-map QA-ledger surfaces (names-only).** CHECK po-004, CHECK po-005, and CHECK po-006 are check-scoped offline QA surfaces under `audit/qa/hde-epic033/checks/po-004/` through `audit/qa/hde-epic033/checks/po-006/`, each using `primary.log`, sibling path-proof evidence, and referenced governed vendor-contract artifacts as the check-local receipt set. CHECK po-004 binds suspect OpenAPI source quarantine and non-authority posture while preserving validated YAML route specs as first-precedence authority for the inventory slice. CHECK po-005 binds the five route rows and v2/v1 route-family separation for the contract inventory. CHECK po-006 binds contract-map parseability, final-LF posture, canonical JSON check posture, non-conformance claim, and no-runtime-request-shaping boundary through the accepted Moon Loop remediation receipt. These checks are offline QA-ledger classifications only; they do not create runtime request shaping, response normalization, live conformance, public Reader changes, open-rails vendor smoke, new HTTP homes, PF09.5 drainage, or broader HDE-EPIC033 closure by themselves.  
* **EPIC033 evidence-binding, token-posture, and HDE-FERM006 supportability QA-ledger surfaces (names-only).** CHECK po-007, CHECK po-008, and CHECK po-009 are check-scoped offline QA surfaces under `audit/qa/hde-epic033/checks/po-007/` through `audit/qa/hde-epic033/checks/po-009/`, each using `primary.log`, sibling path-proof evidence, and referenced governed evidence artifacts as the check-local receipt set. CHECK po-007 binds Human Evidence Index, Machine Evidence Index, hash, LF, evidence-path validation, and path-proof PASS posture for source inventory, contract map, and related HDE-EPIC033 artifacts. CHECK po-008 binds baseline existing-token posture and confirms no vendor-v2-specific acceptance-token minting. CHECK po-009 binds HDE-FERM006.1 through HDE-FERM006.4 supportability from repo evidence only, with no runtime v2 conformance claim and no PF09.5 drainage claim. These checks are offline QA-ledger classifications only; they do not create runtime v2 conformance, live vendor behavior proof, new acceptance tokens, public Reader changes, PF09.5 drainage, formal close-pack completion, QA PASS beyond these recorded check groups, or broader HDE-EPIC033 closure by themselves.  
* **EPIC033 runtime-nonclaim and remediation QA-ledger surfaces (names-only).** CHECK po-010, CHECK po-011, and CHECK po-012 are check-scoped offline QA surfaces under `audit/qa/hde-epic033/checks/po-010/` through `audit/qa/hde-epic033/checks/po-012/`, with accepted remediation receipts under `audit/qa/hde-epic033/checks/po-010-remediation-r1/` and `audit/qa/hde-epic033/checks/po-012-remediation-r1/` where applicable. CHECK po-010 binds later adapter architecture, runtime request shaping, live vendor smoke, and runtime v2 conformance as unclaimed by this epic. CHECK po-011 binds the contract inventory as inventory-only and not runtime vendor conformance. CHECK po-012 binds live vendor smoke, public Reader change, new HTTP home, and AI runtime or evidence scope as outside this epic. PO-010 and PO-012 accepted bounded QA evidence-harness remediation for brittle phrase matching while preserving the original proof targets inside the QA root. These checks are offline QA-ledger classifications only; they do not create runtime v2 conformance, live vendor behavior proof, public Reader changes, new HTTP homes, AI scope, acceptance tokens, PF09.5 drainage, QA PASS beyond these recorded check groups, formal close-pack completion, PO closeout, or broader HDE-EPIC033 closure by themselves.  
* **EPIC033 routing, non-expansion, and closeout-deliverable QA-ledger surfaces (names-only).** CHECK po-013, CHECK po-014, and CHECK qa-16-close-out-deliverables are check-scoped offline QA surfaces under `audit/qa/hde-epic033/checks/po-013/`, `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/`, `audit/qa/hde-epic033/checks/po-013-remediation-r3/`, `audit/qa/hde-epic033/checks/po-014/`, and `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/`, plus closeout support artifacts at `audit/qa/hde-epic033/qa_step_logs_manifest.json`, `audit/qa/hde-epic033/00_meta/discovery_artifact.md`, and `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md`. CHECK po-013 binds QA\_PLAN\_UPDATE routing before final R3 PASS proof, evidence-path validation, LF checks, orientation checks, mirror schema checks, evidence-index hash checks, and no runtime v2 conformance, public Reader surface change, or AI scope. CHECK po-014 binds no implementation work, no PF document edit, no runtime vendor conformance, no public Reader change, no new HTTP home, no AI scope, and no epic-closure action. CHECK qa-16 binds closeout manifest, discovery artifact, QA RCA / Doc Delta summary, and sibling path-proof posture without claiming PO closeout or broader epic closure. These checks are offline QA-ledger classifications only; they do not create runtime behavior, implementation deltas, public routes, runtime v2 conformance, public Reader changes, new HTTP homes, AI scope, PF document edits, acceptance tokens, PF09.5 drainage, formal close-pack completion, PO closeout, or broader HDE-EPIC033 closure by themselves.  
* **EPIC033 final QA closeout review, QA RCA, and Lead Dev retrospective synthesis surface (names-only).** The HDE-EPIC033 final QA closeout review, QA RCA, and Lead Dev Epic Retrospective are offline synthesis artifacts that consolidate Fermentation Pass 4 scope, PR-01 inventory-only evidence, Step-0B, PO-001 through PO-014, qa-16 closeout deliverables, deliverables register D1 through D5, PF10 results register, source-of-truth posture, PF23 current-reality context, bounded QA evidence-harness remediations for PO-006, PO-010, and PO-012, QA\_PLAN\_UPDATE-routed PO-013 remediation, rendered-escape review posture, dependency-readiness deviations, PF19 closeout/RCA requirements, coverage-vs-plan accounting, implementation gaps, remediation-loop assessment, and final READY WITH CAVEATS recommendation. Architecture treats this synthesis as traceability and interpretation over existing proof families and check-scoped QA surfaces; it does not create a runtime route, public Reader contract change, public route, public flag, public payload field, HDAPI v2 runtime-conformance claim, implementation delta, PF-Canon edit, acceptance-token claim, PF09.5 drainage, PO closeout action, or epic close by itself.  
* **EPIC033 SATISFIED closure-trace posture (names-only).** HDE-EPIC033 is recorded as SATISFIED for this review’s closure trace only. The SATISFIED label maps the HDE-FERM006 inventory-only deliverables, PR-01 evidence family, Step-0B through qa-16 QA evidence, PF10 result claims, and Lead Dev closure trace to an offline closure interpretation. It is not a PO closeout action, not a board update, not merge provenance, not formal close-pack completion, and not physical PF09.5 drainage. PF23 may support current-reality context for engine, vendor seam, evidence roots, and QA roots, but it does not provide or replace closure proof.  
* **EPIC033 final readiness and caveat-separation posture (names-only).** PF10 records PR-01 evidence readiness, Step-0B PASS, PO-001 through PO-014 PASS, qa-16 closeout-deliverables PASS, PR-01 final PR acceptance posture, HDE-FERM006 supportability to Done, and no product-runtime defect for the completed inventory-only scope. PF02 records the final posture as READY WITH CAVEATS for this review’s implementation and QA-readiness interpretation. Physical PF09.5 status drainage, formal close-pack completion, merge provenance, HDE-FERM007 implementation proof, HDE-FERM008 live conformance and open-rails proof, explicit PF10 docs-PR coverage, public Reader changes, new HTTP homes, runtime v2 adapter conformance, live vendor conformance, and AI scope remain separate offline closeout, later-drain, or future-slice concerns unless separately present and bound.  
* **EPIC027 acceptance-ledger close-pack surfaces (names-only).** The EPIC027 close-pack binds existing runtime proof families through governed offline artifacts at `docs/acceptance_map_epic027.json`, `audit/qa/hde-epic027/token_evidence_matrix.md`, `audit/qa/hde-epic027/acceptance_map_viability.log`, `audit/EPIC-027_close_report.md`, and `audit/EPIC-027_MANIFEST.json`. These are offline ledger surfaces only and do not create new runtime routes, new Presenter paths, or new public transport surfaces.  
* **EPIC028 Reader acceptance-ledger surfaces (names-only).** The EPIC028 Reader closeout binds existing Reader runtime proof families through governed offline artifacts at `docs/acceptance_map_epic028.json`, `audit/qa/hde-epic028/token_evidence_matrix.md`, and `audit/qa/hde-epic028/acceptance_map_viability.log`. These are offline ledger surfaces only; they preserve the existing Reader route, Endpoint Catalog and env-gate, and Reader A7 proof family without creating new runtime routes, new Presenter paths, or writer-side surfaces.  
* EPIC028 single-home acceptance binding posture (names-only). The current-epic Reader acceptance binding remains single-home at docs/acceptance\_map\_epic028.json, audit/qa/hde-epic028/token\_evidence\_matrix.md, and audit/qa/hde-epic028/acceptance\_map\_viability.log. Matching Machine Evidence Index rows for all three belong to the same offline discoverability posture, and Architecture does not recognize an alternate acceptance-map home for EPIC028.  
* **EPIC028 close-pack baseline surfaces (names-only).** The surfaced EPIC028 close-pack baseline consists of `audit/EPIC-028_close_report.md`, `audit/EPIC-028_MANIFEST.json`, `audit/EPIC-028_close_report.md.path_proof.txt`, and `audit/EPIC-028_MANIFEST.json.path_proof.txt`.  
* **EPIC028 close-pack binding posture (names-only).** These packaging artifacts bind to the already-proven EPIC028 evidence family, including `docs/acceptance_map_epic028.json`, `audit/qa/hde-epic028/token_evidence_matrix.md`, `audit/qa/hde-epic028/acceptance_map_viability.log`, `audit/qa/hde-epic028/qa_step_logs_manifest.json`, `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`, and `audit/qa/hde-epic028/checks/po-010/final_summary.txt`, rather than inventing a replacement proof surface.  
* **Packaging-only posture.** These close-pack baseline surfaces remain offline packaging artifacts only. They do not reopen implementation scope, create new runtime routes, or replace the existing Reader success, acceptance-binding, or epic QA manifest surfaces.  
* **EPIC029 conjunction writer evidence surfaces (names-only).** The EPIC029 conjunction writer slice reuses the existing dev-only `GET /dev/writer/conjunction` and `GET /dev/reader/conjunction` family and binds it through governed offline artifacts at `artifacts/writer/conjunction_write_readback.log` and `artifacts/writer/conjunction_writer_summary.json`, together with their sibling path proofs.  
* **EPIC029 writer evidence boundary posture (names-only).** Shared Human Evidence Index, Machine Evidence Index, and topology-orientation companion refreshes that occur in the same evidence run remain part of this same offline evidence event. The writer slice does not widen into a new runtime route, a new public success surface, or a new A7 proof surface.  
* **EPIC029 ops environment-binding evidence surfaces (names-only).** The EPIC029 dev/internal harness environment-validation slice records governed offline evidence at `audit/ops/hde-epic029/ops-01/commands.txt`, `audit/ops/hde-epic029/ops-01/stdout.log`, `audit/ops/hde-epic029/ops-01/stderr.log`, `audit/ops/hde-epic029/ops-01/exit_codes.txt`, `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`, `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`, `audit/ops/hde-epic029/ops-01/binding_disposition.md`, and `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`.  
* **EPIC029 OPS-01 authoritative closure posture (names-only).** Within that governed ops family, `codespaces` is closed by direct runtime validation and `local_dev` is closed by binding-equivalence, with `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` and no separate local-dev runtime executed in that evidence pass.  
* **EPIC029 OPS-01 normalization posture (names-only).** `commands.txt`, `stdout.log`, `stderr.log`, `exit_codes.txt`, `codespaces_dev_sampler_url.md`, `local_dev_sampler_url.md`, `binding_disposition.md`, `created_files_sha256.txt`, and their index or mirror companions move together to one authoritative closure posture. A mixed-state OPS-01 family is not a valid proof surface and does not create a new runtime route or proof surface.  
* **EPIC029 bounded-family coverage limit (names-only).** The bounded conjunction inventory and the current canonical JSON gate remain family-scoped proofs for the named conjunction route family and its governed offline artifacts. They do not, by themselves, prove exhaustive all-surface HTTP emitter coverage for every adapter route.  
* **EPIC029 ops classification evidence surfaces (names-only).** The EPIC029 blocker-classification slice records governed offline evidence at `audit/ops/hde-epic029/ops-02/W-001_action_log_and_evidence_output_run2.md`, `audit/ops/hde-epic029/ops-02/W-001_classification_run2.md`, `audit/ops/hde-epic029/ops-02/commands_w001_run2.txt`, `audit/ops/hde-epic029/ops-02/exit_codes_w001_run2.txt`, `audit/ops/hde-epic029/ops-02/stdout_w001_run2.log`, and `audit/ops/hde-epic029/ops-02/stderr_w001_run2.log`.  
* **EPIC029 ops classification posture (names-only).** These offline classification artifacts assess blocker posture for existing conjunction and dev/internal harness surfaces. They do not create new runtime routes or replace the separately bound OPS-01 and close-pack closure surfaces.  
* **EPIC029 close-pack baseline surfaces (names-only).** The EPIC029 close-pack baseline consists of `audit/EPIC-029_close_report.md`, `audit/EPIC-029_MANIFEST.json`, `audit/EPIC-029_close_report.md.path_proof.txt`, and `audit/EPIC-029_MANIFEST.json.path_proof.txt`.  
* **EPIC029 acceptance-binding surfaces (names-only).** The EPIC029 close-pack binds the conjunction slice through `docs/acceptance_map_epic029.json`, `docs/acceptance_map_epic029.json.path_proof.txt`, `audit/qa/hde-epic029/token_evidence_matrix.md`, `audit/qa/hde-epic029/token_evidence_matrix.md.path_proof.txt`, `audit/qa/hde-epic029/acceptance_map_viability.log`, `audit/qa/hde-epic029/acceptance_map_viability.log.path_proof.txt`, `audit/qa/hde-epic029/qa_step_logs_manifest.json`, and `audit/qa/hde-epic029/qa_step_logs_manifest.json.path_proof.txt`.  
* **EPIC029 canonical epic-close QA logs (names-only).** Within that same offline evidence plane, the EPIC029 close-pack binding consumes the canonical QA logs at `audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log`, `audit/qa/hde-epic029/checks/po-precommit/primary.log`, and `audit/qa/hde-epic029/checks/po-postcommit/primary.log` as existing governed proof members rather than as new runtime surfaces.  
* **EPIC029 step-scoped bounded-closeout QA surfaces (names-only).** The bounded closeout slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-001/`: `primary.log`, `conjunction_json_surface_inventory.snapshot.md`, `endpoints_catalog.snapshot.json`, and `route_snapshot.txt`.  
* **EPIC029 step-scoped canonical-JSON QA surfaces (names-only).** The canonical JSON slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-002/`: `primary.log`, `run_canonical_json_gate.output.log`, `run_canonical_json_gate.rc.txt`, `json_gate_structured_record.snapshot.json`, and `json_canonical_check.snapshot.log`.  
* **EPIC029 step-scoped writer QA surfaces (names-only).** The writer slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-003/`: `primary.log`, `generate_conjunction_writer_evidence.output.log`, `generate_conjunction_writer_evidence.rc.txt`, `test_dev_conjunction_http.output.log`, `test_dev_conjunction_http.rc.txt`, `conjunction_write_readback.snapshot.log`, and `conjunction_writer_summary.snapshot.json`.  
* **EPIC029 step-scoped sampler-harness QA surfaces (names-only).** The internal sampler slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-004/`: `primary.log`, `test_dev_sampler_http.output.log`, `test_dev_sampler_http.rc.txt`, `dev_start_reader.snapshot.sh`, and `dev_sampler_healthcheck.snapshot.py`.  
* **EPIC029 step-scoped OPS binding QA surfaces (names-only).** The OPS-01 closure slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-005/`: `primary.log`, `commands.snapshot.txt`, `exit_codes.snapshot.txt`, `codespaces_dev_sampler_url.snapshot.md`, `local_dev_sampler_url.snapshot.md`, and `binding_disposition.snapshot.md`.  
* **EPIC029 step-scoped transport-boundary QA surfaces (names-only).** The formal proof-boundary slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-006/`: `primary.log`, `test_endpoint_catalog.output.log`, `test_endpoint_catalog.rc.txt`, and `endpoints_catalog.snapshot.json`.  
* **EPIC029 step-scoped transport-boundary posture (names-only).** Within that check-scoped proof slice, `/reader` remains the formal cataloged A7 success surface, while `GET /dev/writer/conjunction` stays `dev_harness` and not A7-eligible, and `POST /internal/dev/sampler` remains outside the formal transport-proof family.  
* **EPIC029 step-scoped functional-harness QA surfaces (names-only).** The real functional-harness slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-007/`: `primary.log`, `functional_bundle.output.log`, and `functional_bundle.rc.txt`.  
* **EPIC029 step-scoped functional-harness posture (names-only).** This proof slice demonstrates at least one real functional harness over the existing dev/internal conjunction family without creating a new public surface, a new writer-runtime design, or a second proof route.  
* **EPIC029 step-scoped close-binding QA surfaces (names-only).** The bounded close-binding slice records governed check-scoped artifacts under `audit/qa/hde-epic029/checks/po-008/`: `primary.log`, `acceptance_map.snapshot.json`, `token_evidence_matrix.snapshot.md`, `acceptance_map_viability.snapshot.log`, `qa_step_logs_manifest.snapshot.json`, `close_report.snapshot.md`, `close_manifest.snapshot.json`, `po_epic_close_live_qa.snapshot.log`, `po_precommit.snapshot.log`, and `po_postcommit.snapshot.log`.  
* **EPIC029 step-scoped close-binding posture (names-only).** This snapshot family stays on one bounded Conjunction acceptance surface, reuses the existing close-pack and acceptance-binding homes, and consumes the canonical epic-close QA logs as governed proof members rather than as new runtime routes or a widened transport surface.  
* **EPIC029 step-scoped QA proof posture (names-only).** These check-scoped snapshot families are governed offline proof members for the existing conjunction route family, the dev-only writer and sampler harness surfaces, and the OPS-01 closure record. They do not create new runtime routes, new proof-only transport surfaces, or an alternate serializer or emitter path.  
* **EPIC029 closeout-support posture (names-only).** These offline acceptance-binding, close-pack, and OPS-01 surfaces record the EPIC029 conjunction slice as supportable from repo evidence for later PF09 drain at epic close, specifically `HDE-CONJ009.1` / `HDE-CONJ009`, `HDE-CONJ008.1` / `HDE-CONJ008`, and `HDE-CONJ001.4`. Refreshing them does not create new runtime routes, prove new transport bytes, or create a new A7 proof surface.  
* **EPIC029 binding-coverage posture (names-only).** Within that same offline evidence plane, `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`, `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt`, `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`, and `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md.path_proof.txt` remain binding-coverage surfaces for the bounded conjunction route family and the normalized OPS-01 environment-binding posture. They do not create new runtime routes, new proof surfaces, or a second truth home for the EPIC029 closure record.  
* **Ledger discoverability posture.** Close-pack and evidence-discipline jobs consume this manifest family as governed offline evidence only when it is discoverable through the Human Evidence Index and the Machine Evidence Index. PF02 records that names-and-paths linkage only; updater logic, record fields, and token claims remain out of scope here

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

* **Dev:** when `APP_ENV=dev` and `DATABASE_URL` is present but unusable, the resolver may fall back to `DB_BRIDGE_URL` and proceed with keys-only diagnostics (no secrets in logs).  
* **Production-like guard:** `APP_ENV` values `prod`, `production`, and `live` receive guarded bridge posture. Production-like resolver flow is `DATABASE_URL` first and bridge-disabled by default unless `DB_ALLOW_BRIDGE_IN_PROD=1` is explicitly set or bridge use is explicitly forced by the owning resolver policy. `APP_ENV=live` is a hardening alias, not permissive drift.  
* **Sanctioned dev bridge-fallback shape (architecture only).** When this fallback is taken, adapter-side selection may still present as `psycopg` while runtime connectivity resolves through `bridge`. PF02 treats that as an allowed resolver outcome inside the existing dev fallback path, not as a second canonical BodyGraph store, a new request-path mode, or a production-path exception.  
* **DBAccess façade posture (architecture only).** `DBAccess` remains the provider-agnostic façade for DB provider selection and DB operations. Dev fallback, bridge capability proof, and provider-parity harnessing prove behavior through that façade and do not create a second BodyGraph store, a second DB home, or a bypass around Adapter-owned BodyGraph cache wiring.

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

**Future Glow app integration ownership (architecture-level).** Unless a future ADR or PF canon supersedes this posture, the HD Engine owns HumanDesignAPI vendor acquisition, request shaping, BodyGraph/chart response normalization, BodyGraph storage and retrieval, and HD computation. The Glow app is the product shell and consumer of HD Engine outputs; it may request or trigger Engine behavior and receive normalized, app-safe outputs.

Direct Glow app HumanDesignAPI calls, app-owned raw BodyGraph persistence, parallel vendor clients, parallel credential paths, or app-side reimplementation of vendor request shaping require a future ADR. The exact integration transport between the Glow app and the HD Engine is not decided here and remains future architecture or implementation scope.

**HumanDesignAPI vendor API version boundary (architecture-level).** The vendor API version boundary is configuration-owned, not runtime-route-owned. `HD_API_BASE_URL` is the canonical base URL key for the HumanDesignAPI version boundary; runtime request construction must append only version-neutral resource paths to the configured base URL and must preserve any path prefix already present there.

PF02 may name vendor endpoint families for source-selection, legacy-isolation, and documentation-provenance context. Versioned route strings such as `POST /v2/charts` and `POST /v1/bodygraphs` may appear only as vendor documentation, route-family labels, legacy/provenance text, or test inputs proving configurable-version behavior. They must not drive active runtime URL construction, auth selection, evidence-generator route construction, OPS instructions, PR prompts, or QA prompts.

Auth selection must be represented by explicit route metadata or contract metadata, not by inspecting whether a runtime path starts with `/v1` or `/v2`. Exact environment bindings, outbound auth header bytes, request bodies, response envelopes, rate-limit behavior, retry posture, and error bytes remain owned by HDE-CLI-API-Vendor-Ref, Glow Infrastructure, HDE-Governance, and HDE-Schemas & Artifacts by title.

**HumanDesignAPI v2 adapter/schema gap posture (architecture-level).** HDE-EPIC035 records v2 ChartResult and ChartSimpleResult evidence as an adapter/schema gap, not as a normalized data-path proof. PF02 must not describe v2 chart payloads as feeding the existing BodyGraph cache, person/bodygraph compute inputs, compatibility/conjunction flows, or app integration until a bounded adapter/schema proof or implementation maps the selected vendor payload family into the existing internal BodyGraph/person/cache contract.

A future proof or implementation must distinguish the vendor payload family, required response fields, populated internal fields, unsupported fields, whether the adapter is sufficient for HD Engine compute, whether any legacy fallback remains, and whether raw vendor payloads are persisted, redacted, summarized, or excluded. Exact schemas, evidence artifacts, payload bytes, and QA acceptance posture live in HDE-Schemas & Artifacts, HDE-Mechanics Guide, HDE-CLI-API-Vendor-Ref, HDE-Build Checklist Fermentation, and Glow QA Guide by title.

Boundary classification is architecture-level and must distinguish `allowed`, `forbidden`, `unknown / fail-closed`, and `out of scope`. Boundary analysis must be based on discovered current repo surfaces and must report the adapter, presenter, engine, vendor-seam, and evidence-tool loci inspected. Earlier planning text or hard-coded expected path lists are not sufficient by themselves.

PF02 owns the architectural boundary rule only. Boundary analyzers, renderer separation, table-driven taxonomy, generated evidence artifacts, path proofs, tests, and validation mechanics live in HDE-Mechanics Guide, HDE-Schemas & Artifacts, HDE-Build Checklist Fermentation, and Glow QA Guide by title.

**`bg:resolve --source vendor` route-policy boundary (architecture-level).** HDE-EPIC036 records an explicit `bg:resolve --source vendor` route-policy classification. When the configured HumanDesignAPI base is v2, this path selects `unsupported_runtime_nonclaim` rather than constructing a legacy `bodygraphs` request and treating that as valid BodyGraph-detail behavior. When the configured base is non-v2, the existing legacy BodyGraph fallback remains explicit legacy behavior.

This posture does not prove that v2 chart data feeds the BodyGraph cache, compatibility inputs, app integration, or full HumanDesignAPI v2 runtime conformance. It also does not create a new HTTP home, public Reader change, public route, app-side HumanDesignAPI ownership, AI scope, raw payload persistence approval, or broad vendor-conformance claim. Future work that wants v2-backed BodyGraph resolution must implement or prove a bounded adapter/schema path from v2 ChartResult or ChartSimpleResult into the existing internal BodyGraph/person/cache contract, or adopt a future ADR-defined route policy.

Exact CLI flags, command bytes, outbound headers, request/response shapes, error codes, evidence artifacts, and QA workflows remain owned by HDE-CLI-API-Vendor-Ref, Glow Infrastructure, HDE-Schemas & Artifacts, HDE-Mechanics Guide, HDE-Build Checklist Fermentation, and Glow QA Guide by title.

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
* **EPIC031 provider-gate posture (names-only).** HDE-EPIC031 PR-01 proves the SAFE-rails provider-gate slice for the existing vendor seam under local deterministic no-live-vendor posture. The provider-gate proof class may exercise pinned policy, retry/backoff domains, typed provider outcomes, Retry-After parsing, original-status classification, and redirect-suppression behavior, but PF02 treats those as seam-policy and evidence facts routed by title to the owning transport, mechanics, governance, and build-checklist homes. This proof does not create a public Reader change, an HDAPI v2 runtime-conformance claim, a PO-only open-rails vendor smoke, or a new runtime surface.  
* **EPIC031 vendor log posture (names-only).** HDE-EPIC031 PR-02 proves the SAFE-rails observability slice for the existing vendor seam. Vendor logs and evidence samples are bounded and keys-only, may record route names, rails state, timeout profile, bounded status/error class labels, and opaque identifiers, and must not record payload bodies, raw secret headers, plaintext secrets, or vendor payloads. This proof does not create a new vendor route, public surface, evidence home, or runtime mode.

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

Auxiliary evidence-looking roots (for example `parity/`, `errors/`, `proofs/`, `reports/`, and `scan_reports/`) are non-authoritative by default unless **HDE-Schemas & Artifacts** explicitly catalogs them into the governed evidence model or another PF single home explicitly routes authority there.

Governed payload truth remains under the governed evidence model and its Human Evidence Index / Machine Evidence Index discoverability surfaces. Auxiliary support roots and derived views do not create alternate mirror, close-pack, or canonical-gate homes.

