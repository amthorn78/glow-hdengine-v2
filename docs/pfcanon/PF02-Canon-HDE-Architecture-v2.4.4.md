# **0\. Front Matter**

**Title:** PF02-Canon-HDE-Architecture  
**Version:** v2.4.4

**Status:** Canon  
**Effective date:** 2026-08-11

**Last Update Gate:** 0808 refresh 4

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
PF02 uses `[Implemented]`, `[Required-Now]`, and `[Speculative]` as its closed status vocabulary. Claim-level state is authoritative. A subordinate heading carries a label only when all material claims in that section share that state. Mixed sections separate current repository behavior, current requirements, and speculative future support at claim level. Status labels do not prove runtime reachability, test passage, deployment, or production enablement.

The protected `[Required−Now]` spelling in H1 4 is a legacy typography alias of `[Required-Now]`, not a fourth status label. Editable and new text uses `[Required-Now]` with U+002D HYPHEN-MINUS.

**Routing by title only.**  
Operational/transport details, CLI/Reader bytes, vendor specifics, QA tokens, and process policy are referenced by title only to their owning documents (for example: HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Schemas & Artifacts, HDE-Mechanics Guide, Glow QA Guide, HDE-Phased Epics, Epic-Process-Guide, Glow Infrastructure).

**Rendered escape artifact posture (architecture identity).**  
When reviewing PF02-owned component homes, endpoint catalog paths, route strings, or boundary strings, display-layer escape characters are not source evidence. Source-level proof is required before an escaped character may be treated as an architecture defect. Rendered backslashes in assistant output, markdown output, review prose, preview panes, or copied chat text do not prove that a component home, endpoint catalog path, or boundary string is wrong and do not create redline, blocker, or remediation obligations by themselves.

**Architecture plan-review blocker posture.**

Architecture blockers require a real boundary, public/private, service, endpoint, adapter, route-home, component-home, or contract defect. Command syntax, helper-code syntax, heredoc form, shell syntax, escaped command examples, paste-readiness, indentation, markdown rendering, code-block formatting, and non-literal example invocations are not architecture blockers by themselves. During plan review, preserve architecture scope, proof identity, rails posture, evidence intent, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture without requiring literal executable command syntax. Syntax normalization during execution is allowed when those architecture and proof boundaries remain unchanged.

**Pack/bytes ownership (out of scope here).**  
Canonical JSON policy, pack/manifest, and the machine Evidence Index (JSONL mirror schema and parity) are owned outside Architecture and cited by title, primarily in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

**Endpoint Catalog (single home; routing note).**  
Success-endpoint discovery and A7 proofs are catalog-driven. The Endpoint Catalog is designated as the single home for the canon set of client-callable endpoints and their coarse operational metadata. It is an internal artifact (not user-facing), and PF02 documents it only as a wiring map. It does not define its access-control posture or its exact request/response contracts. The designated home is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256` sidecar and sibling path-proof transcripts at `docs/ENDPOINTS_CATALOG.json.path_proof.txt` and `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`. Endpoint-generation tooling and derived inventories MUST consume or validate this home and MUST NOT independently hard-code a second endpoint inventory. If the catalog shape or ownership changes, it must be corrected at the single home and its governed derivatives regenerated.

**A7 invariants (routing note).**  
Success proofs require `Vary: Authorization, Accept-Encoding`, strong quoted ETag on 200, HEAD 200 parity (`Content-Type == GET`, `Content-Length == len(identity 200 body)`), and 304 (after prior 200\) omitting both `Content-Type` and `Content-Length`. Encoding-invariance holds: for the same canonical LF-terminated body, the ETag identity and effective `Content-Length` are stable across accepted encodings. Concrete contracts remain in HDE-Governance and HDE-CLI-API-Vendor-Ref.

**DB runtime resolver (routing note).**  
Resolver semantics are environment-aware:

* **All environments:** `DATABASE_URL` is the sole canonical HDE database endpoint key, and direct PostgreSQL through the Glow-owned psycopg provider is the sole active database transport.  
* **Fail-closed selection:** if the direct endpoint is absent, invalid, unavailable, or unauthorized, database access fails closed without selecting a bridge, alternate HTTP database transport, vendor path, or inferred endpoint.  
* **Retired bridge configuration:** `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are retired. Their presence is configuration drift and is reported by key name only before any provider attempt or database I/O; no value is printed or retained.

Evidence (headers/records only) is owned by HDE-Mechanics Guide and HDE-Build Checklist and indexed per HDE-Schemas & Artifacts. The full BodyGraph lifecycle flow is described in the System Overview section.

---

## **Change control \[Required-Now\] (titles-only cross-refs; no duplicated bytes)**

**PF02 owns wiring and flows only; all contract bytes, schemas, and tokens are routed by title to their single-home PF documents.**

**Transport / contract bytes.**  
Owned outside Architecture: HDE-Governance and HDE-CLI-API-Vendor-Ref. Acceptance tokens are single-home in HDE-Governance. Plans, acceptance artifacts, and step logs MUST NOT mint, invent, or claim unregistered token names. If a token is desired, it MUST be registered first (with semantics) and only then adopted by plans and evidence bindings. Any token name used outside the registry MUST match spelling exactly (no aliases). Evidence-only deliverables (for example, guard proofs or consult records) may be required and evidenced without becoming tokens unless and until Governance registers them as tokens.

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
`catalog/manifest.json` is the sole tracked release-identity input. `release_id` is the SHA-256 of its canonical bytes, and runtime derives that identity from the packaged manifest; no evidence path, environment variable, generated constant, or mutable attestation file is an identity input.

The dependency direction is `tracked source -> canonical manifest -> release ID -> external attestation`. A normal release cut changes only `catalog/manifest.json`; current release-bound derivatives are built outside tracked source through `tools/evidence/build_release_attestation.py`. Checked-in EPIC022 release evidence remains frozen historical evidence, and registry/configuration evidence remains release-agnostic. Exact manifest, attestation, evidence, and release mechanics remain in HDE-Schemas & Artifacts, HDE-Mechanics Guide, Glow QA Guide, and HDE-Governance by title.

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

CLI↔Reader parity is a current architecture requirement. Architecture keeps the single-emitter rule and routes CLI surface and parity-proof mechanics by title to HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide. PF02 does not assert an open or closed process status for parity work.

## 1.1 Single homes

**engine/** —  deterministic compute single-homes, plus sanctioned seams.

Purity rule (normative). Any module designated as deterministic compute (including sampler core and Engine Core modules) MUST be pure-compute: no time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. Inputs are pure data; outputs are pure data; side effects are forbidden.

BodyGraph seam carve-out (normative). BodyGraph resolution and ingest MAY perform vendor and DB I/O through the DB abstraction as a sanctioned seam, including when implemented under `engine/bodygraph/`. This carve-out does not relax purity requirements for deterministic compute modules.

**Non-BodyGraph chart loader classification \[Required-Now\].** At repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`, `engine/charts/loader.py` is implementation drift, not a sanctioned Engine I/O seam. Environment and rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging, and filesystem writes belong to Adapter-owned application or infrastructure orchestration and must use the existing sanctioned BodyGraph resolver/ingest boundary where vendor or database acquisition is required. Pure chart validation or normalization may remain under Engine ownership only as explicit data-in/data-out computation with no time, randomness, environment, network, provider, logging, or filesystem side effects. The checked-in loader remains current repository reality until separately remediated; this classification does not claim that relocation, caller migration, or removal has occurred. The BodyGraph seam carve-out does not relax purity for Engine Core, sampler core, or other deterministic compute modules.

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
All public JSON is UTF-8 (no BOM), keys sorted in ASCII order, compact separators, and ends with exactly one newline (LF). Arrays used as sets are deduplicated and ASCII-sorted. Canonicalization rules are owned by HDE-Schemas & Artifacts (titles-only).

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
Public surfaces expose only the approved Reader envelope (bands-only, numeric-free) produced by the Presenter. Internal/dev surfaces exist for diagnostics and local harnesses and are not public data planes. The internal-ops identity route `/internal/version` is governed in HDE-Governance; PF02 stays contract-free and does not restate headers (titles-only routing).

**Endpoint Catalog (success) proofs.**  
A7 proofs run only on a cataloged Endpoint Catalog (JSON success) route, named and owned in HDE-CLI-API-Vendor-Ref. PF02 does not enumerate routes or bytes; it routes discovery/proofs by title and keeps contract bytes out of Architecture.

**Keys-only outputs (Engine).**  
The Engine, including sampler core and Engine Core modules, never emits narratives or free text; it produces only structured keys and metrics that the Presenter serializes. Public bytes are produced exclusively by the Presenter’s single emitter (shared by Adapter and CLI).

**Aux Narrative surface (concept-only).**  
Narrative text (when present) is served only via Aux/CLI (not on Reader 200). Endpoint bytes live in HDE-CLI-API-Vendor-Ref; suppression carve-out and A7 posture live in HDE-Governance. PF02 remains contract-free and routes by title only. Engine outputs remain keys-only; Aux surfaces interpret those keys together with narrative packs (HDE Narratives Guide, HDE-Mechanics Guide, and HDE-Schemas & Artifacts by title).

**No leakage across boundaries.**  
Adapter does not reveal internal state or non-public fields; Engine math remains isolated from runtime concerns; no cross-role fields or headers leak into public envelopes. Narratives and Aux surfaces sit above Engine outputs and are not visible to Engine or Reader 200\.

**Locale & canon seams.**  
All canonicalization and byte compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Presenter emits canonical JSON; canonical JSON policy and the machine Evidence Index (JSONL mirror schema and parity) are owned by HDE-Schemas & Artifacts (titles-only).

**Routing (titles-only).**

* Headers/transport and acceptance tokens → HDE-Governance (single-home roster).  
    
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

**Sampler and Engine Core modules (names-only)**

**Names & roles.**

* The canonical sampler behavior lives in a single module under the `engine/` tree, referred to here as the **sampler core module** (currently `engine.sampler.core`). It owns sampler/ranker behavior: pool formation, eligibility, ordering, and sampling decisions.  
    
* The canonical Engine Core behavior lives at `engine.core.core`, with `engine.core.core.compute_core` as its canonical entrypoint. It owns the core compatibility computation: neutral and directional metrics, category-framework and per-channel mechanics integration, AB↔BA parity, and the normalized result structure consumed by Presenter and evidence tooling.

Current repository discrepancy: at repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`, checked-in runtime public, HTTP compat, and CLI paths use `engine.compat.ts_v0` or `engine.compat.compute` rather than `engine.core.core.compute_core`. This does not change the canonical single-home requirement or claim that migration has occurred.

**Behavior-only boundary.**

* Both modules are required to be **pure compute**: no time, network, file I/O, randomness, or environment reads at compute time; no import-time side effects. They accept normalized inputs and return normalized structures; they do not know about CLI commands, HTTP routes, rails, or evidence files. This is a normative boundary and does not by itself assert repository alignment.  
    
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
* The high-level compat path follows §2.2 (Reader/CLI → Engine Core → Presenter), while §2.4 supplies the BodyGraph lifecycle used by that path; concrete shapes and tokens live in **HDE-CLI-API-Vendor-Ref**, **HDE-Math-Spec**, and **HDE-Schemas & Artifacts** by title.

---

### **2.2.2 Proofs & routing (titles-only)**

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
    
* Suppression semantics (200 with no body and no ETag, optional policy header) are governed in **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**; PF02 does not restate headers or payloads.

**Ops exclusion.**

* `/internal/version` is excluded from A7 proofs and is not A7-eligible; PF02 does not define its access-control posture.  
* Ops behaviour and headers are governed in **HDE-Governance**.

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

**HumanDesignAPI v2 conformance posture (architecture-level).** Configured-v2 request routing, deterministic ChartResult adaptation, source-neutral projection, closed-rails refusal, and bounded non-production mapped-cache persistence are current static architecture surfaces. Their presence does not establish live-vendor conformance, production writes, public Reader change, QA acceptance, or PO-only open-rails evidence. Runtime, deployment, and acceptance claims remain separate.

**No-AI runtime boundary for this vendor conformance path.** HumanDesignAPI v2 conformance is deterministic vendor integration only. It does not add OpenAI, LLM, AI-agent, chatbot, prompt, embedding, model-call, or AI-enablement architecture inside the HD Engine, Glow App, Reader, vendor adapter, cache, sampler, compat engine, narrative machinery, public surfaces, or admin runtime surfaces. Vendor documentation files or pages aimed at AI or LLM consumers may be inspected only as documentation-discovery context and must not be treated as product or runtime scope.

### **Adapter source policy (env-aware)**

* **Prod / non-dev:**  
    
  * The database is the **canonical source** for BodyGraphs on request paths.  
      
  * The Adapter uses the direct-only DB runtime resolver to locate the canonical BodyGraph store. `DATABASE_URL` is the only database endpoint considered, and direct PostgreSQL through the Glow-owned psycopg provider is the only selectable provider. Missing, invalid, unavailable, or unauthorized direct access fails closed without an alternate provider; retired bridge keys are rejected before any provider attempt.  
      
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

1. When a request needs a BodyGraph, Adapter/CLI first consults the database using the DB runtime resolver.  
     
2. On a **cache hit** containing a valid BodyGraph for the normalized input, Adapter passes that BodyGraph into Engine; no vendor call is made.  
     
3. On a **miss** or expiry, source policy controls the next step:  
     
   * Production request paths do not call the vendor inline. An explicit out-of-band refresh path owns any vendor request.  
       
   * A permitted non-production or out-of-band flow may call the vendor through the vendor seam.  
       
   * A permitted vendor result is normalized before Engine use.  
       
   * Any durable write uses the existing BodyGraph store through the DB resolver.

Dev versus production rails, vendor routes, and retry/timeout policy are governed outside PF02; this section fixes only architectural ordering and responsibility.

### **Durability objects (names-only)**

* `body_graphs` — persistent BodyGraph records.  
    
* `body_graphs_current` — view selecting the latest stored BodyGraph record per user/vendor identity.

Row fields, constraints, validity and TTL rules, normalization, fingerprints, and additional schema details are single-home in **HDE-Schemas & Artifacts**; PF02 names only the objects and their architectural roles.

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

## **3.1 Compat v1**

**Role & purpose \[Required-Now\].**  
`/api/compat/v1` is the adapter’s compatibility surface. It calls the Engine in-proc and returns the public compatibility envelope emitted by the single canonical Presenter emitter. It does **not** expose internals or narratives.

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the selected application factory registers the compat blueprint. The checked-in GET handler returns a JSON success body, while the POST handler invokes compatibility computation and sends its result through the shared public emitter.

**Validation (high level) \[Required-Now\].**

* **GET (probe-only):** health-only probing. It MUST NOT compute compat and MUST NOT include a JSON body.  
    
* **POST (compute; internal/admin):** the only method that computes compat. Expects a valid pair definition and viewer preferences that are:  
    
  * well-formed  
      
  * complete (all ten Magic-10 keys)  
      
  * within allowed ranges


* **Endpoint Catalog binding (high level):** the Endpoint Catalog entry for `/api/compat/v1` binds the POST compute surface and MUST include a non-empty env gate field. Env-gate proof is headers-only.  
    
* Malformed or incomplete inputs are rejected. (Detailed shapes live in **HDE-CLI-API-Vendor-Ref**.)

**Current repository discrepancy.**  
The checked-in GET handler emits `{"ok":true,"schema":"v1"}` through the JSON writer path, which conflicts with the required bodyless health-only probe.

**Static inspection cannot establish.**  
Static repository bytes do not establish whether the GET handler is runtime-reachable in any environment.

**Viewer-preference normalization handoff (high level) \[Required-Now\].**

Compat and CLI compatibility flows normalize viewer preferences before candidate-selection, sampler, or ranker behavior consumes them. Zero-weight intent is carried as normalized input truth into the existing sampler/ranker behavior home; sampler/ranker remains the owner of candidate exclusion behavior. This handoff uses existing CLI and compat call paths and does not create a new public surface, route, serializer path, or public contract.

**Threshold ownership handoff (high level) \[Required-Now\].**

Compat threshold symbols used by compat and CLI compatibility flows are compatibility-facing shims over the existing Magic-10 threshold source in the Engine math layer. `engine.compat.thresholds.THRESHOLDS_V1` derives from `engine.magic10.thresholds.THRESHOLD_EDGES`, and `engine.compat.thresholds.BANDS` derives from `engine.magic10.thresholds.BANDS`. This preserves one threshold home, keeps threshold arithmetic and constants-pack ownership outside Architecture, and does not create a new public route, flag, serializer path, public contract, or second threshold source.

**Presenter rule \[Required-Now\].**  
The adapter never hand-crafts public JSON. Only the Presenter’s single emitter serializes public bytes for **all** callers (HTTP and CLI).

**Conjunction compute contract (internal) \[Required-Now\].**

Conjunction computation is an internal Engine surface. It does not create a new production HTTP endpoint and it emits public bytes via the same Presenter emitter used everywhere else.

* Location: `engine/compat/compute.py`  
    
* Entry points (names-only):  
    
  * `conjunction_public` (pure compute over resolved BodyGraphs)  
      
  * `conjunction_public_resolved` (local-first resolution via the existing BodyGraph resolver path, then compute; SAFE rails apply)

**Birth-only no-user boundary (architecture-level) \[Required-Now\].**

`conjunction_public_resolved` is the sanctioned no-user resolver boundary for local compatibility proof when caller input provides a complete birth tuple and provides no `person_uid`, `user_id`, or app user ID. The boundary may derive deterministic internal metadata before strict Engine compute, including an internal `person_uid`, but that metadata stays internal and is not a caller input, public field, public route contract, CLI flag, or serializer path. Existing internal `user_id` flows remain separate and unchanged.

**Parity expectations \[Required-Now\].**

* For identical inputs, public bytes match CLI output (byte identity).  
    
* Output is non-empty canonical JSON (LF-terminated).  
    
* Locale pins for byte checks: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Routing (titles-only).**

* Request/response details, field lists, examples, CLI↔Reader byte-parity rules → **HDE-CLI-API-Vendor-Ref**  
    
* A7 validators and header behaviour → **HDE-Governance**  
    
* Canonical JSON policy → **HDE-Schemas & Artifacts**  
    
* Process & PR workflow (PR-first; Evidence Index and mirror updated in the same PR) → **Epic-Process-Guide**

See §2.2 for the high-level Reader/CLI → Engine Core → Presenter flow and §2.4 for the BodyGraph lifecycle used by this surface.

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

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the checked-in adapter defines `/reader`, emits through the shared Reader emitter, gates non-dev `APP_ENV` values while treating an absent `APP_ENV` as `dev`, and loads local chart files. The Endpoint Catalog classifies `GET /reader` and `HEAD /reader` as internal `dev_harness` routes with `APP_ENV=dev`.

**Current repository discrepancy.**  
The checked-in Reader is a dev fixture surface, not the required public DB-backed Reader. Its handler reads caller-supplied local chart paths and does not implement the DB-backed BodyGraph lifecycle required above.

**Static inspection cannot establish.**  
Static repository bytes do not establish runtime reachability, deployment, or production enablement for the Reader surface.

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

## **3.3 Sample (dev harness) (dev-only)**

**Intent \[Required-Now\].**  
A local, non-public developer harness on the adapter for manual and automated checks during development. It shares the single canonical emitter with CLI and Reader so public bytes are identical for identical inputs.

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the selected Reader blueprint defines `POST /internal/dev/sampler` and the three dev conjunction GET routes named below. Their handlers use `_dev_admin_gate()`, and the Endpoint Catalog lists the four routes as internal `dev_harness` surfaces that are not A7-eligible.

**Responsibilities (conceptual) \[Required-Now\].**

* Provide minimal endpoints or commands to exercise Engine paths with fixture inputs.  
    
* Perform lightweight structural validation before calling the Engine in-proc.  
    
* Emit results via the single canonical emitter (no alternate serializers or formatting).  
    
* Maintain CLI↔harness parity for identical inputs and environment (bytes owned elsewhere).

**Non-goals \[Required-Now\].**

* No public availability.  
    
* No narrative text.  
    
* No transport or policy bytes are defined in PF02.  
    
* No uncontrolled vendor/network calls. Rails are closed by default; acquisition is permitted only when explicitly enabled under SAFE rails, and only through the existing BodyGraph resolver seam described in §2.4.  
    
* No new persistence surfaces. Any writes are limited to the existing BodyGraph cache upsert described in §2.4.

**Gating & posture (dev-only; titles-only routing) \[Required-Now\].**

* Harness is dev-only; never mounted in production.  
* Harness routes MUST deny when `APP_ENV` is not one of: `dev`, `test`, `local`.  
* Canonical internal/dev sampler route (HTTP POST; names-only):  
  * POST /internal/dev/sampler  
* Dev-only conjunction routes (HTTP GET; names-only):  
  * `GET /dev/sampler/conjunction`  
  * `GET /dev/reader/conjunction`  
  * `GET /dev/writer/conjunction`  
* **Writer readback parity flow (names-only).** The dev conjunction writer/readback proof path remains inside the dev harness surface family, using `GET /dev/writer/conjunction` together with `GET /dev/reader/conjunction`. PF02 records only the route names and adapter ownership here; writer/readback bytes and proof artifacts remain out of scope here.  
* **Current repository catalog \[Implemented\].** Endpoint Catalog entries for these dev conjunction endpoints are classified as `dev_harness` and are not A7-eligible.  
* Rails are closed by default (for example, `SAFE_MODE=1`, `ALLOW_NETWORK=0`). Dev-only conjunction endpoints MAY run under open rails only when explicitly enabled (for example, `SAFE_MODE=0`, `ALLOW_NETWORK=1`).  
* Optional GET/HEAD/304 captures are allowed for the GET dev harness endpoints, but A7 proofs are not run here. A7 proofs run on the cataloged JSON success route (Endpoint Catalog) and are driven by the Catalog.  
* Locale is optional; when present, it is advisory only and does not affect canonical JSON bytes.

**Current repository discrepancy.**  
The selected factory registers the Reader blueprint without an environment-specific unmount. The dev route handlers enforce a request-time gate, but static repository bytes do not establish that the routes are never mounted in production or that any route is runtime-reachable.

**Required architecture \[Required-Now\].**  
Sample harness uses the same Presenter emitter and Engine Core behaviour as compat v1. Dev-only conjunction preview endpoints emit canonical JSON bytes; rails are closed by default unless explicitly opened. Sample harness is never used for A7 proofs; see §2.4 and §5 for compat flow and evidence-plane details.

**Routing (titles-only).**

* Dev-harness routing/guards and optional GET semantics → **HDE-CLI-API-Vendor-Ref**  
    
* A7 proof surface policy and ops exception (`/internal/version`) → **HDE-Governance**  
    
* Canonical JSON policy, Evidence Index/mirror discipline (same-PR parity) → **HDE-Schemas & Artifacts**

---

## **3.4 Internal ops signals**

**Future concepts \[Speculative\].**

* `/internal/healthz` — **liveness.** Constant-time “process is up” probe; no Engine invocation; no disk or network; no PII.  
    
* `/internal/readyz` — **readiness.** “Can serve traffic” probe; checks prerequisites such as config loaded, emitter path available, and rails posture sane without running compat math or touching vendors.

**Governed identity surface \[Required-Now\].**

* `/internal/version` — **identity.** Build and config snapshot for drift detection. Reads identity fields only and is side-effect-free. No secrets. It is ops-only, identity-only, and non-A7.

**Boundary \[Required-Now\].**  
Any adopted internal ops signal MUST NOT touch Engine Core, sampler core, or vendor; these are liveness, readiness, or identity-only surfaces.

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the selected application factory mounts the Reader blueprint that defines `/internal/version`. Definitions for `/internal/healthz` and `/internal/readyz` occur in the alternate `adapter/wsgi.py` factory, not in the selected factory.

**Static inspection cannot establish.**  
Static repository bytes do not establish runtime reachability, deployment, or a truthful readiness predicate.

**Non-goals \[Required-Now\].**  
No payload or header matrices, auth policy, or acceptance tables in this section. These are ops signals, not product surfaces.

**Routing (titles-only).**  
All concrete transport or policy details for these signals, including `/internal/version` posture and acceptance, are owned by **HDE-Governance**.

---

## **3.5 Internal-ops identity and refusal (route-only)**

**Purpose \[Required-Now\].**  
Record the adopted internal-ops routes and bounded repository drift without turning checked-in diagnostic routes into architectural interfaces. These are not public data planes.

**Adopted routes \[Required-Now\].**

* `/internal/version` is the ops-only, identity-only, non-A7 surface.  
    
* `/ops/rails/refusal` is the canonical closed-rails refusal probe.

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the selected application factory mounts the Reader blueprint. That blueprint defines `/internal/version`, `/ops/db/unavailable`, `/ops/rails/refusal`, `/ops/probe/env`, and `/ops/writer/diagnostic`.

**Current repository discrepancy.**  
The checked-in `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic` routes are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog. Their continued presence in the selected blueprint is repository drift; this document does not describe them as supported ops, admin, diagnostic, evidence, product, or public interfaces. No repository removal, test migration, deployment convergence, or catalog mutation is claimed.

**Static inspection cannot establish.**  
Static repository bytes do not establish runtime reachability, deployment, production exposure, or external consumers for any route.

**Responsibility split \[Required-Now\].**

* Adapter wires adopted routes and applies guards.  
    
* Presenter emits canonical JSON when applicable.  
    
* Engine remains pure compute. No cross-role leakage.

**Governance pointer.**  
Behaviour, headers, and acceptance tokens for the adopted routes are governed by **HDE-Governance**. PF02 remains contract-free and does not restate header/body rules.

**Contract posture (titles-only).**  
HDE-Governance governs invariants for the identity surface (for example, no-store, no ETag, HEAD 200 with `Content-Type` parity and `Content-Length == identity GET`, conditionals ignored / never 304\) and owns the identity-surface acceptance/evidence posture. It also governs the closed-rails refusal semantics for `/ops/rails/refusal`. PF02 points by title only.

**Evidence & indexing (titles-only).**  
Proof artifacts and success-endpoint snapshots are indexed per **HDE-Governance** / **HDE-Schemas & Artifacts**; the human Evidence Index and the machine JSONL mirror must remain 1:1 (updated in the same PR).

For `/internal/version` coupling \+ two-run identity, the governed proof surface is the internal\_version evidence bundle under `artifacts/ops/internal_version/`. Canonical member filenames (and any explicitly permitted alias files) are owned by HDE-Schemas & Artifacts and governed by HDE-Governance; ad-hoc filename variants are prohibited. PF02 names this evidence surface for architectural traceability and continues to route all token semantics and detailed proof formats by title to their single-home documents.

**Non-goals \[Required-Now\].**  
No public contract bytes, no payload schemas, no alternate emitters, no persistence, and no vendor/network calls from the adopted surfaces.

**Routing (titles-only).**

* Identity and refusal invariants, acceptance, and evidence posture **→ HDE-Governance**  
    
* Endpoint Catalog / success JSON → **HDE-CLI-API-Vendor-Ref**  
    
* Canonical JSON and machine mirror → **HDE-Schemas & Artifacts**

---

## **3.6 Aux Narrative (concept-only, route-only)**

**Role \[Required-Now\].**  
Serve deterministic narrative text **outside** the public Reader surface. No narratives appear on Reader 200\.

**Current repository behavior \[Implemented\].**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, the selected adapter blueprint defines `GET /api/aux/narrative` and `GET /aux/narrative`. The HTTP handler and `aux-preview` CLI both call `engine.narratives.emit_public_aux`, which emits LF-terminated text when a narrative is available and an empty body when suppressed.

**Responsibilities (conceptual) \[Required-Now\].**

* Adapter wires the PF05-owned canonical Aux route and alias; Presenter owns the public Aux byte-emission boundary; Engine Core remains pure compute (keys only).  
* Text constraints: no CR characters; LF-terminated output (schema/constraints routed by title).  
* Maintain CLI admin preview parity (bytes owned elsewhere; titles-only routing).

**Current repository discrepancy.**  
The checked-in Aux byte-emission helper is under `engine/narratives/` rather than the Presenter boundary, and the inspected Aux HTTP handler contains no `v=1` selector enforcement. Current canon adopts the text surface; these checked-in facts remain implementation drift, not authority to weaken the Presenter or version-selection requirements.

**Route and proof posture (route-only; titles-only) \[Required-Now\].**

* **Canonical route and alias.**  
  **HDE-CLI-API-Vendor-Ref** owns `GET /api/aux/narrative?v=1` as canonical and `/aux/narrative?v=1` as its byte-identical alias.  
    
* **Representation.**  
  Aux returns `text/plain; charset=utf-8` when text is shown. When suppressed, Aux returns 200 with no body and no ETag; a policy header is optional. Exact bytes remain in their owning documents.  
    
* **A7 separation.**  
  A7 proofs run only on a cataloged JSON success route. Aux HEAD and 304 are out of scope for EPIC-010; the Aux text route is not recast as the cataloged JSON success proof surface.  
    
* **Catalog posture.**  
  The Endpoint Catalog is internal-only and env-gated; non-prod entries must be unreachable in prod — capture a headers-only env-gate proof for the selected A7 catalog route.  
    
* **Ops exclusion.**  
  `/internal/version` is excluded from A7 proofs and is not A7-eligible; PF02 does not define its access-control posture.

**Static inspection cannot establish.**  
Static repository bytes do not establish runtime reachability, deployment, alias parity, or production enablement for the Aux routes.

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

Engine compatibility and sampler outputs are keys and structured metrics. Narrative loading, composition, and preview code is isolated under `engine/narratives/`; it remains outside Engine Core and sampler core. Aux surfaces interpret Engine outputs in combination with narrative packs (owned by the Narratives Guide, **HDE-Mechanics Guide**, and **HDE-Schemas & Artifacts** by title) to produce text. Reader 200 stays narrative-free; narrative suppression returns 200 with an empty body by design.

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

**Current repository discrepancy.**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, `dev/reader_harness/app.py` silently treats an absent `APP_ENV` as `dev`, registers only the Reader blueprint under `/api`, calls `app.getattr` instead of `app.register_blueprint`, and does not mount the compat blueprint. The root `run_flask_dev.sh` and `run_flask.py` helpers start `adapter.factory:create_app` rather than the dedicated harness. These checked-in facts do not satisfy the required dedicated-harness contract.

**Static inspection cannot establish.**  
Static repository bytes do not establish that any dev/QA service is running or reachable.

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
    
* Evidence generators and determinism pipelines MUST invoke Engine Core and sampler core in ways that preserve these invariants; they MUST use the **same computation** required by runtime architecture, only with pinned fixtures and closed rails.

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
    
* **PF10-HDE-Build-Notes** — Applicable, active, non-superseded addenda control only the exact points they explicitly address; silence leaves the permanent PF canon in control.  
    
* **Glow QA Guide / HDE-Phased Epics / PF23 Reality-Audits** — QA tokens, D-goals, and Reality Audit posture that consume the ledger; PF02 routes by title only and does not define tokens or audit scripts.

**Architecture evidence boundary.**

* PF02 records only the evidence plane's participation and connections. Evidence paths, record shapes, token tables, commands, schedules, acceptance results, per-epic histories, and operating contracts remain in their canonical owners.  
    
* Current architecture, governed proof, and historical record are separate claim states. Historical evidence, a reused baseline, path discoverability, or a current artifact does not independently establish current architecture support, runtime correctness, QA PASS, acceptance, HDE Build Checklist movement, or epic closure.  
    
* Governed evidence-family and artifact-path contracts live in **PF12-Canon-HDE-Schemas-and-Artifacts**; PR and evidence-process mechanics live in **PF06-Canon-Epic-Process-Guide**; QA rules and QA-relevant history live in **PF19-Canon-Glow-QA-Guide**; per-epic historical intent and evidence pointers live in **PF20-Reference-HDE-Phased Epics**.

## 5.4 Evidence & determinism flows (concept only)

**Offline plane.**

* Determinism and evidence pipelines run **offline**, in a plane parallel to runtime requests.  
* They do not introduce new runtime surfaces or alter Reader/CLI behaviour; they only exercise existing Engine behaviour under controlled conditions.  
* Epic-close and acceptance-ledger generators belong to this same offline evidence plane. They consume and bind already-existing proof families from runtime surfaces rather than introducing new runtime routes, alternate emitter paths, or replacement transport surfaces.  
* **Canonical behavior only.** The offline plane MUST exercise the same canonical behavior homes required by supported runtime architecture: `engine.core.core` for Engine Core behavior, `engine.sampler.core` for sampler behavior, `project_bodygraph()` where mapped BodyGraph inputs converge, and the single Presenter when public bytes are produced. It MUST NOT create or legitimize a second Human Design compute, projection, presentation, or public-byte implementation.  
* **Source-neutral convergence.** Independently mapped inputs that converge on BodyGraph output MUST pass through `project_bodygraph()`. Projection creates neither persistence nor public bytes; when output becomes public, it remains under the single Presenter boundary.  
* **Proof consumption and non-inflation.** The offline plane consumes or exercises governed proofs of existing behavior; it does not create that behavior or its conformance. Historical evidence, reused baselines, path discoverability, and current artifact presence do not independently establish architecture support, runtime correctness, QA PASS, acceptance, HDE Build Checklist movement, deployment, or epic closure.  
* **Architecture-only boundary.** Evidence generation, acceptance, closeout, inventory, and ledger activity do not create or widen runtime routes, public APIs, emitter paths, persistence behavior, or public bytes. PF02 records participation and connection only; mechanics and operating contracts remain with their canonical owners.

**Behaviour source.**

Computation-derived evidence tools or jobs (named by title only in Mechanics/Checklists and Build Notes) MUST call:

* `engine.core.core` for Engine Core behaviour, and  
    
* `engine.sampler.core` for sampler/ranker behaviour,

using deterministic fixtures and **closed rails** (no network, no clocks, no env-driven branching). These calls MUST use the same pure-compute modules required by runtime architecture; they do not re-implement logic.

**Artifact families.**

* Outputs are written into governed evidence families under `artifacts/<EVIDENCE_FAMILY_SUBPATH>`, registered in **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide** (titles only).  
    
* Family names, schema shapes, and path patterns are defined there, not in Architecture.

**Index & mirror linkage.**

Whenever these pipelines produce or regenerate artifacts:

* The human Evidence Index and the machine mirror must be updated in the **same PR**. When the machine mirror changes, its governed companion files (`artifacts/evidence_index.jsonl.sha256` and `artifacts/evidence_index.jsonl.path_proof.txt`) MUST update in that same PR, per **HDE-Schemas & Artifacts** and **Epic-Process-Guide**.

PF02’s role is to assert that:

* Computation-derived Engine and sampler evidence invokes the respective single behavior homes.  
    
* Public-envelope evidence uses the single Presenter emitter.

Catalog, transport, environment, index, release-identity, and other non-computation evidence follow their own owning components and documents. PF02 does **not** define pipeline names, schedules, tokens, or acceptance criteria; it maps only the participating components and their connections.

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

* **Sole active binding:** `DATABASE_URL` is the only HDE database endpoint considered, and direct PostgreSQL through the psycopg provider is the only active database transport.  
* **Fail-closed direct selection:** if the endpoint is absent, invalid, unavailable, or unauthorized, DB access fails closed; no bridge, alternate HTTP database transport, vendor path, or inferred endpoint is selected.  
* **Retired bridge keys:** `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, and `DB_ALLOW_BRIDGE_IN_PROD` are configuration drift. Their presence fails before any provider attempt, and diagnostics expose key names only.  
* **DBAccess façade posture (architecture only).** `DBAccess` remains the direct-only façade for DB provider selection and operations against the canonical BodyGraph store. It creates no second BodyGraph store, DB home, or request-path mode.

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

**HumanDesignAPI v2 adapter, compat, and cache-persistence boundary (architecture-level).** Configured-v2 BodyGraph-detail work distinguishes four separate architecture states:

* v2 dry-run mapping works when a supported v2 ChartResult payload is mapped by the deterministic adapter into HDE BodyGraph/person/cache-shaped data.  
* v2 mapped output can feed compatibility computation when the mapped parties are accepted by the existing compat path under governed proof.  
* A bounded configured-v2 persistence path writes only adapter-mapped HDE BodyGraph/cache payloads to the existing BodyGraph store under explicit `--upsert`, open rails, and requested/process non-production guards; it then reads back, reprojects, and verifies canonical parity and repeated-write idempotence. Raw HumanDesignAPI envelopes are not persisted.  
* Production and production-like mapped-cache writes remain refused unless a later production authorization decision and governed runtime evidence explicitly reopen that posture.

The BodyGraph cache remains persistent Engine input storage, not a raw HumanDesignAPI envelope store. The bounded path creates no public Reader change, new public route, second persistence home, app-side HumanDesignAPI ownership, AI scope, or broad HumanDesignAPI platform conformance.

**Source-neutral BodyGraph projection boundary (architecture-level).** Configured-v2 vendor `ChartResult` data mapped through the existing v2 adapter and deterministic mapped-cache representations converge through the pure internal `engine/bodygraph/projection.py` boundary. `project_bodygraph()` accepts only already-mapped HDE data and returns a `CanonicalBodyGraph` composed of a `BodyGraphFields` `bodygraph`, `person`, and `person_uid`. It returns a deep-copied canonical projection, omits permitted top-level `source` provenance, rejects unsafe or unknown transport, vendor, request, response, credential, header, and raw metadata, enforces closed shapes and person UID agreement, and reports stable, value-free projection errors. It performs no network, database, filesystem, clock, environment, randomness, logging, serialization, or persistence work.

Projected values reach public bytes only through the existing Presenter emitter. This boundary creates no second adapter, emitter, serializer, public route, transport contract, or production identity.

This projection boundary performs no durable write. The separate bounded mapped-cache persistence owner projects already-mapped HDE data before writing it to the existing BodyGraph store, reads the stored row back, reprojects it, and verifies canonical equality. Repeated same-identity writes remain idempotent. Database I/O and persistence authorization remain outside the projection boundary and Engine Core; production and production-like writes remain refused.

Exact schemas, payload bytes, CLI behavior, write/read-back evidence, path proofs, QA acceptance posture, rails policy, and future task ownership live in HDE-Schemas & Artifacts, HDE-Mechanics Guide, HDE-CLI-API-Vendor-Ref, HDE-Build Checklist Fermentation, Glow QA Guide, HDE-Governance, and later phased build checklists by title.

Boundary classification is architecture-level and must distinguish `allowed`, `forbidden`, `unknown / fail-closed`, and `out of scope`. Boundary analysis must be based on discovered current repo surfaces and must report the adapter, presenter, engine, vendor-seam, and evidence-tool loci inspected. Earlier planning text or hard-coded expected path lists are not sufficient by themselves.

PF02 owns the architectural boundary rule only. Boundary analyzers, renderer separation, table-driven taxonomy, generated evidence artifacts, path proofs, tests, and validation mechanics live in HDE-Mechanics Guide, HDE-Schemas & Artifacts, HDE-Build Checklist Fermentation, and Glow QA Guide by title.

**`bg:resolve --source vendor` route-policy boundary (architecture-level).** HDE-EPIC037 records configured-v2 `bg:resolve --source vendor` as an adapter-backed v2 chart flow for dry-run resolution. When the configured HumanDesignAPI base is v2, the resolver selects the recommended v2 chart route family, the version-neutral `charts` resource path, and the deterministic ChartResult adapter. When the configured base is non-v2, the legacy BodyGraph fallback remains explicit legacy behavior.

Closed rails must refuse before outbound I/O. Configured-v2 request construction must not fall back to legacy `bodygraphs` as a substitute for v2 BodyGraph-detail behavior, and generic ingest must not silently treat v2 chart requests as legacy BodyGraph ingest. Resolver and vendor-client architecture may classify route family, auth posture, payload family, and adapter result, but exact CLI flags, command bytes, outbound headers, request/response shapes, error codes, evidence artifacts, and QA workflows remain owned by HDE-CLI-API-Vendor-Ref, Glow Infrastructure, HDE-Schemas & Artifacts, HDE-Mechanics Guide, HDE-Build Checklist Fermentation, and Glow QA Guide by title.

This posture does not prove durable mapped-cache persistence, production writes, a new HTTP home, public Reader change, public route, app-side HumanDesignAPI ownership, AI scope, raw payload persistence approval, or broad HumanDesignAPI platform conformance.

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

PF02 maps ownership and does not reproduce external contracts. Cross-document routing uses exact owner titles.

* Math and scoring → **PF01-Canon-HDE-Math-Spec**.  
    
* Catalogs, manifests, schemas, governed artifacts, and evidence indexing → **PF12-Canon-HDE-Schemas-and-Artifacts**.  
    
* CLI, Reader, vendor, and Endpoint Catalog wire contracts → **PF05-Canon-HDE-CLI-API-Vendor-Ref**.  
    
* Governance, transport and operations policy, validation, and acceptance-token semantics → **PF04-Canon-HDE-Governance**.  
    
* QA principles, checklists, and cross-component playbooks → **PF19-Canon-Glow-QA-Guide**.  
    
* Historical epic records and trace pointers → **PF20-Reference-HDE-Phased Epics**.  
    
* Epic delivery and PR-first process → **PF06-Canon-Epic-Process-Guide**.  
    
* Mechanical components, tooling, and build tasks → **PF14-Canon-HDE-Mechanics-Guide**.  
    
* Infrastructure inventory → **PF07-Canon-Glow-Infrastructure**.  
    
* Narrative mechanics and semantics → **PF17-Canon-HDE-Narratives-Guide**.  
    
* Invocation text → **PF-Invocation**.

Auxiliary evidence-looking roots (for example `parity/`, `errors/`, `proofs/`, `reports/`, and `scan_reports/`) are non-authoritative by default unless **HDE-Schemas & Artifacts** explicitly catalogs them into the governed evidence model or another PF single home explicitly routes authority there.

Governed payload truth remains under the governed evidence model and its Human Evidence Index / Machine Evidence Index discoverability surfaces. Auxiliary support roots and derived views do not create alternate mirror, close-pack, or canonical-gate homes.