# 0\) Document Control

## 0.1 **Header**

**Title:** PF14-Canon-HDE-Mechanics-Guide  
**Version:** v3.4.7

**Status:** Canon  
**Effective date:** 2026-08-08

**Last Update Gate:** BN 12.6.2 A28-44  
**Invocation tag:** INV-f2ac55d77ce9aacc

---

## 0.2 Purpose — Components & build tasks (mechanics scope)

Mechanics is the mechanical schematic for the HD Engine and its tooling. This guide is the single place where we enumerate and describe every component and build task that must exist in the engine repo so that the Engine can run, be tested, and be proven for production.

This guide:

* Describes components, jobs, tools, and build tasks that must exist in the engine repo (including adapters, CLI, evidence tools, QA harnesses, and sanity/rails checks). This includes operational and infrastructure components as well as software.  
* Specifies mechanical responsibilities only: what must be wired, what artifacts must be produced, and what evidence must be captured and checked.  
* Does not restate math formulas or public transport bytes; those live in their single-home PF documents and are referenced here by title only. When a mechanic depends on math or transport, this guide names the component and its responsibilities and routes the details to the owning PF doc.

Scope boundary (normative).  
 This guide is a mechanics/components reference. It MUST NOT function as governance, a token registry, or an epic-planning authority.

* Acceptance token registry, token naming, and token semantics are owned by HDE-Governance (titles-only). Newly minted tokens are canonical in HDE-Build Notes (titles-only) until drained into HDE-Governance. This guide MUST NOT list or curate acceptance tokens.  
* Epic planning structure and baseline close requirements are owned by Glow QA Guide, HDE-Phased Epics, and HDE-Build Checklist (titles-only). This guide MUST NOT add planning prerequisites or planning checklists.  
* Evidence families and acceptance token mapping are owned by Glow QA Guide and HDE-Build Checklist (titles-only). This guide MUST NOT redefine acceptance criteria.  
* Live QA runbooks are not epic-plan prerequisites. This guide may describe Live QA harness mechanics, but Live QA runbook planning lives in QA artifacts governed by Glow QA Guide (titles-only) and must not be treated as a prerequisite for epic planning.  
* Mechanics proof and helper-syntax posture. For PF14-owned mechanics, reviewers and writers must distinguish the mechanic being proven from helper-code formatting, shell wrapper form, heredoc formatting, indentation, rendered escape characters, or command-literal copy/paste defects. Correctable helper syntax may be normalized during execution or review when the mechanic, proof target, rails posture, evidence identity, public/private boundary, no-secret posture, and no-new-scope posture remain unchanged. Test and evidence helpers must report executed truth and must not rely on plan-byte literalism.  
* PF09 accountability for mechanics gaps. When PF14 text, reviews, audits, implementation guidance, or future-work notes identify task-like mechanics work, the item must map to a phased PF09 task/subtask, be marked as a PF09 gap for PO/canon adjudication, or be clearly classified as out of PF09 scope. PF14 does not create PF09 rows, assign PF09 status, or turn free-floating recommendations into acceptance obligations by itself.

Directory naming (normative).  
All repository directories MUST use lowercase ASCII names. Mixed-case directories are non-conforming and must not be introduced by examples in this guide. This rule is directory-only. Filenames may contain uppercase characters unless another canon explicitly forbids them.

Public posture (Reader v1).  
For Reader v1, this guide assumes and enforces:

* Bands-only, numeric-free public payloads (numbers remain admin-only).  
* Resonance posture: SR-only (α \= 1.0).  
* Hysteresis \= 1 is armed for future XR but not exposed in this version.

Routing rules.  
Cross-references in this guide are titles-only (no version numbers in prose).

Single homes (route by title; do not duplicate):

* Public bytes & HTTP contracts: HDE-CLI-API-Vendor-Ref  
* Math & algorithms: HDE-Math-Spec  
* Schemas, packs/manifests, canonical JSON, Evidence Index & Machine Mirror: HDE-Schemas & Artifacts  
* Governance, acceptance gates, A7/ops posture: HDE-Governance

References (titles-only).  
This guide assumes, and routes mechanical responsibilities to, the following PF documents:

* HDE-Governance  
* HDE-CLI-API-Vendor-Ref  
* HDE-Math-Spec  
* HDE Architecture  
* Glow Development Philosophy  
* HD Engine Epics Map (historical; epic planning now lives in HDE-Phased Epics by title)  
* Glow HD Engine — Build Notes & Integration Addenda (Living)

Provenance & deltas (informative).  
Mechanics here have been canonicalized from REVIEW addenda and aligned with Glow HD Engine — Build Notes & Integration Addenda (Living). In particular, this guide:

* Rolled in previously optional items (Server Cache; Reader conditional-GET helper).  
* Locked the A7 transport posture.  
* Added the /internal/version ops posture (no-store, no ETag, conditionals ignored; HEAD 200 with Content-Type parity).  
* Clarified optional build\_commit.  
* Expanded Evidence Index captures to require same-PR updates, Machine Mirror parity, and path-proofs.

This document should be read as the full mechanical schematic of the HD Engine and its repo: if a component, job, harness, or governed artifact must be built and kept working, it is accounted for here and wired by reference to its canonical PF homes.

## 0.3 Preamble — Product scope

Viewer inputs & presets.  
Viewer presets are optional templates. Each viewer:

* Selects a top category from the closed Magic-10 set.  
* Sets weights in the range 0..100 across the ten Magic-10 IDs (closed set and order; see HDE-Schemas & Artifacts §2.6 and HDE-Math-Spec §5.1 by title).  
* Zero-weight rule: if a viewer sets a category’s weight to 0, candidates whose \#1 category is that category are excluded.

Engine outputs (internal/admin).  
Internally, the engine:

* Computes per-category numbers in 0..100.  
* Maps those numbers to bands (Cool, Open, Warm, Glow) using inclusive-high thresholds and round\_half\_up (see HDE-Math-Spec §5.3 by title).  
* Selects two narrative keys per category (personal, shared).

The engine selects keys; it does not write copy. Resonance posture for v1 is SR-only (α \= 1.0); XR is dormant and not part of public output.

Public covenant (titles-only).

* Public Reader payloads are bands-only and numeric-free; underlying numbers remain admin-only.  
* Public bytes & schemas live in HDE-CLI-API-Vendor-Ref by title.

Canonical JSON is required end-to-end:

* UTF-8, no BOM  
* ASCII-sorted keys  
* Compact separators  
* Exactly one trailing LF  
* Arrays used as sets are deduped and ASCII-sorted

Determinism posture:

* AB↔BA parity holds for pair-sensitive flows.  
* Two-run identity holds under determinism pins (LC\_ALL=C, LANG=C, TZ=UTC).  
* Reader↔CLI parity is required wherever both surfaces exist.

Math, transport, and ops details are routed to their single homes by title; this guide records the mechanics expectations at the component level (what must exist, how it plugs together, and what it must emit) and does not duplicate contracts or formulas.

## 0.4 HD Engine — the plain story

What it is

* The HD Engine computes per-category compatibility and drives which copy lines appear.  
* It selects and routes copy via a deterministic system.  
* It does not generate text.

What it is for

* Power connection matching from user priorities and weights across ten categories.  
* Give explanations, not only scores: two short narrative lines per category (one personal, one shared) chosen by rules (no HD jargon in user copy).  
* Let admins tune numbers safely while user-visible results remain stable and understandable.

What it does

* Compute pair results across ten categories.  
  * A number from 0 to 100 per category for admin/test.  
  * A band per category (Cool, Open, Warm, Glow) derived from the number.  
* Drive narrative output (no copywriting).  
  * Produce narrative keys and selection signals for each category and perspective (personal/shared) using viewer intent and routing flags.  
  * Determinism and AB↔BA parity for pair views.  
* Respect user intent.  
  * User chooses \#1 category and weights; zero-weight rule enforced.  
* Return stable compact JSON.  
  * Admin/test JSON may include per-category numbers and bands with narrative keys and minimal meta.  
  * Public Reader remains bands-only; public payload bytes are defined in CLI/API.  
* Support the swipe/feed.  
  * Rank candidates by viewer weights and diversify results.

What it does not do

* No copywriting; the engine selects keys only.  
* No public UI; the engine sits behind the app.  
* No direct Internet exposure.  
* No business policy beyond inputs; app controls product flow.

---

# 1\) Repository & Tooling Skeleton (capabilities, not paths)

**Scope (normative).** Mechanics requires a **set of capabilities** that enable determinism, transport acceptance, and evidence generation. The **concrete repository layout, file names, and tool targets are implementation-defined** and **must not be pinned** here. This section states *what must exist*, not *where or how*.

## 1.1 Capabilities the repo must provide

* Adapter surface (HTTP only). Wires Reader routes and the ops endpoint; does not define public bytes (route by title to PF-Canon-HDE-CLI-API-Vendor-Ref).  
* Mechanics core. Pure orchestration for math, comparators, config loader, and public emitter wiring (route math to PF-Canon-HDE-Math-Spec).  
* Schemas & validation. JSON-Schema validation for governed inputs; AJV (or equivalent) CI step that fails on schema drift (route schema/canonical rules to PF-Canon-HDE-Schemas & Artifacts).  
* Evidence indices.  
  * Human index (titles/paths only) in this repo, updated in the same PR as artifacts.  
  * Machine JSONL mirror (records-only) owned by PF-Canon-HDE-Schemas & Artifacts; CI enforces 1:1 parity and path-proofs for every record.  
* Ops artifacts. Start-command capture (bytes \+ hash), health/ready checks; no secrets in logs; SAFE rails defaults enforced per Governance.  
* Scriptable pipeline. A single sanity pipeline (name is implementation-defined) that runs, in order: formatting → lint/type → unit/prop tests → schema checks → goldens/evidence capture → index & mirror parity \+ path-proof validation.

Audit classification for I/O-bearing engine seams. Mechanics audits MUST classify modules by sanctioned seam responsibilities, not by a blanket “engine is pure compute” rule. Pure-compute obligations apply to Engine Core and sampler core modules. Resolver, ingest, vendor, catalog, and loader-style modules under `engine/` may be I/O-bearing only when HDE Architecture or this guide explicitly authorizes that responsibility.

BodyGraph and loader seam posture. BodyGraph resolution and ingest remain the sanctioned BodyGraph I/O seam described in §19.1. Non-BodyGraph loader-style I/O observed under `engine/`, including loader modules such as `engine/charts/loader.py`, MUST be classified as exactly one of: sanctioned loader seam, implementation drift, or future canon gap requiring PO adjudication. The classification MUST NOT be resolved by assumption and MUST NOT authorize new I/O in pure compute modules.

Non-task posture. This audit-classification note creates no new token, no new HDE-Build Checklist task, and no remediation plan by itself.

PF23 audit classification posture. Mechanics observations drawn from Reality Audits or other repo-reality audits MUST be routed to the owning PF canon home by subject. Such observations MUST NOT be converted into HDE-Build Checklist task deltas, implementation scope, remediation scope, OPS scope, evidence homes, or acceptance-token obligations by assumption. A PO or later canon decision is required before any such observation becomes executable work.

Operational unknowns and OPS discovery posture. Mechanics planning MUST distinguish discoverable operational facts from real mechanics or design gaps. Missing environment, credential, base-url, vendor-account, endpoint-family, open-rails, or OPS-root facts are not mechanics gaps by themselves when they can be safely discovered by a bounded PO-run OPS task. This guide may describe the mechanical dependency and fail-closed behavior required around the unknown, but it MUST NOT convert the unknown into a deferral, acceptance token, PF09 status movement, implementation scope, QA PASS claim, OPS completion claim, or closure proof by itself.

Codex Audit repo-reality posture. Codex Audit observations may identify current mechanics or component surfaces for planning, existing-locus support, reuse posture, and implementation scoping. They remain repo-reality observations. PF14 remains the mechanics authority; Codex Audit evidence does not prove QA PASS, OPS completion, acceptance-token satisfaction, PF09 drainage, runtime conformance, or canon authority.

HDAPI v2 vendor conformance mechanics posture (pending, mechanics-only). HumanDesignAPI v2 conformance is pending until the owning Fermentation checklist rows are implemented and evidenced. This guide does not declare the HDE runtime v2-conformant, does not define vendor bytes, does not assign PF09 statuses, and does not create acceptance tokens. It defines the mechanical capabilities the repo must provide so the owning PF homes can later prove conformance.

HDAPI v2 source and contract inventory mechanics. The repo MUST provide a governed vendor-contract inventory workflow for HumanDesignAPI v2 and legacy v1. That workflow MUST:

* Discover and record same-origin HumanDesignAPI documentation sources needed for conformance, including `v2-routes.yaml`, `v1-routes.yaml`, v2 and v1 overview pages, endpoint pages, authentication, rate limiting, error handling, response format, migration, and related vendor-contract pages.  
* Treat `llms.txt`, `llms-full.txt`, and any AI-agent or LLM-oriented vendor documentation as documentation-discovery context only, never as product scope, runtime scope, AI enablement, or acceptance evidence for AI features.  
* Validate machine-readable v2 and v1 route artifacts before using them as source authority.  
* Apply source precedence in this order: validated v2 and v1 YAML route specs first, rendered endpoint pages second, high-level guide pages third, and suspect artifacts quarantined.  
* Quarantine `api-reference/openapi.json` unless domain, title, server, and path-family validation prove it is a HumanDesignAPI artifact.  
* Treat unavailable or non-200 suspect `api-reference/openapi.json` input as quarantined rather than blocking promoted contract inventory when validated v2 and v1 route specs remain usable.  
* Produce a source-backed endpoint reference that distinguishes recommended v2 chart endpoints from legacy v1 BodyGraph endpoints.  
* Cover at minimum `POST /v2/charts`, `POST /v2/charts/simple`, `POST /v2/charts/coordinates`, `POST /v1/bodygraphs`, and `POST /v1/bodygraphs/simple`.  
* Record the auth model, geocode-key requirement, request-content type, request fields, success envelope, error-code model, route version, and source proof for each covered endpoint without defining byte contracts in this guide.  
* Preserve source-cache evidence for rendered pages, route specs, `llms.txt`, and the bounded `llms-full` endpoint-tier excerpt. Each source-inventory row that depends on a cached source MUST carry cache path and cache checksum evidence so closed-rails replay does not rely on metadata-only rendered documentation.  
* Parse endpoint-tier handling from the current cached endpoint-tier table cell rather than from fixed substring defaults.

HDAPI v2 vendor seam mechanics. The repo MUST provide one sanctioned vendor seam for HumanDesignAPI integration. That seam MUST route source selection, request shaping, response normalization, cache writes, CLI surfaces, and internal/admin compat flows through the existing architecture boundaries. It MUST NOT create a second HTTP home, bypass the Adapter, bypass the Presenter, or authorize I/O in pure compute modules.

HDAPI v2 request-shaping and response-mapping mechanics. The repo MUST provide deterministic request-shaping and response-mapping proofs for the pending v2 vendor path. These mechanics MUST:

* Use `HD_API_BASE_URL` as the canonical mechanics-facing HumanDesignAPI base URL key. `HDAPI_BASE_URL` is deprecated drift and MUST NOT be used as canonical mechanics language.  
* If temporary compatibility fallback is implemented, resolve base URL configuration canonical-first: read `HD_API_BASE_URL`; read deprecated `HDAPI_BASE_URL` only when the canonical key is absent; use the canonical value when both exist and match; fail closed with configuration ambiguity when both exist and differ.  
* Treat `HD_API_BASE_URL` as owning the vendor API version and any configured path prefix. Runtime request construction MUST preserve the configured prefix and append only version-neutral resource identifiers.  
* Runtime request construction MUST NOT hardcode `/v1` or `/v2` as active route-construction constants, append versioned vendor paths to `HD_API_BASE_URL`, double-prefix configured versions, normalize away configured prefixes, or infer runtime behavior from vendor API version path strings.  
* Versioned vendor endpoint strings MAY remain as source inventory, contract provenance, historical evidence, artifact-family naming, test input, or non-driving legacy labels. They MUST NOT drive active runtime URL construction.  
* Route-family auth selection MUST be represented as route metadata or contract metadata. It MUST NOT be inferred by checking whether a path starts with `/v1` or `/v2`.  
* Evidence generators and tests for this mechanics family MUST prove configured-base path preservation, no double-version prefix, route-metadata auth, and no-live-vendor or no-public-Reader-change posture where the proof family claims those predicates.  
* Derive endpoint selection, base-url use, auth-header use, geocode-key handling, and request-body shaping from governed contract inventory and the owning bytes document, not from guesses.  
* Project `HD_API_KEY` into `Authorization` Bearer auth for HumanDesignAPI v2 chart routes.  
* Project `HD_API_KEY` into `HD-Api-Key` auth for legacy HumanDesignAPI v1 BodyGraph routes.  
* Project `GEO_API_KEY` into `HD-Geocode-Key` only where the governed route requires geocoding.  
* Preserve v1 BodyGraph behavior as explicit legacy behavior until the owning architecture and byte-contract homes decide whether v1 remains a fallback or is retired.  
* BodyGraph resolver route-policy classification. `bg:resolve --source vendor` is a BodyGraph resolver workflow, not the canonical v2 chart/geokey validation path.  
* For configured v2 vendor bases, `bg:resolve --source vendor --dry-run` MAY use the version-neutral `charts` route and deterministic v2 ChartResult adapter to produce mapped HDE BodyGraph/person/cache/compat evidence without writing DB rows.  
* For configured v2 vendor bases, a non-dry-run mapped-cache write MAY proceed only through the bounded persistence path. The caller MUST provide explicit `--upsert` intent, rails MUST be open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`), and both the requested environment and process environment MUST be non-production. `prod`, `production`, and `live` MUST fail closed before vendor or database I/O.  
* Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback only as a legacy route-family posture with `HD-Api-Key` auth, governed geokey handling, and no v2 BodyGraph-detail compatibility claim.  
* Dual-route behavior is not implemented by this mechanics posture. Any future dual-route, v2 chart-backed BodyGraph-detail, or v2-to-internal BodyGraph/person/cache mapping behavior requires a future ADR or owning-canon decision before PF14 may treat it as a supported mechanic.  
* Keep source-selection and response-mapping mechanics from collapsing v1 and v2 auth behavior, route-family identity, or evidence posture into a generic vendor-auth path.  
* Map the standard v2 response envelope into HDE internal structures only after the mapping is proven.  
* Preserve the distinction between response-envelope proof, adapter proof, resolver dry-run proof, compat proof, durable cache-persistence proof, and production-write authorization proof.  
* HDE-EPIC037-style mapped dry-run proof may support scoped BodyGraph/person/cache/compat evidence flows. It does not by itself prove durable BodyGraph cache persistence, production writes, production upsert authorization, public Reader changes, new public routes, app-side HumanDesignAPI ownership, or broad HumanDesignAPI v2 platform conformance.  
* `ChartResult` StandardResponse data MUST NOT be persisted directly as reusable user data. The bounded persistence owner MUST accept adapter-mapped HDE data only, apply the pure source-neutral BodyGraph projection before persistence, and write no raw vendor envelope, raw request body, raw response body, transport metadata, or credential material.  
* `ChartSimpleResult` MAY be used for bounded live smoke, auth/geokey proof, route-family confirmation, or provider availability proof only with explicit nonclaims for full BodyGraph detail unless it proves every required field.  
* Configured-v2 mapped-cache persistence MUST use the existing BodyGraph store through the sanctioned `DBAccess` seam and one persistence owner. It MUST NOT create a second cache, database transport, public route, emitter, serializer, or durable-write authority.  
* The persistence owner MUST project the mapped input before writing, read back the stored row, and compare canonical bytes for the governed BodyGraph, person, and person-identity fields.  
* Repeated same-identity writes MUST be idempotent. After a successful initial insert, a second same-identity write MUST insert zero rows, identity cardinality MUST remain one, and canonical write/read-back equality MUST remain true.  
* Local evidence MUST be generated from deterministic fixtures under hermetic rails. The proof producer MUST arm the complete lower-seam canary set, including database, vendor, socket, DNS, HTTP, and shared-log protections, so an unintended external call or shared-log mutation fails closed.  
* Evidence writes MUST be failure-atomic. The focused producer MUST stage its bounded primary set before replacement, preserve the previous governed set on failure, remove temporary residue, and keep check mode read-only.  
* The canonical evidence updater remains the sole owner of sibling path proofs, Human Index rows, Machine Mirror rows, and Index/Mirror hashes for this family. Feature producers MUST NOT write those companions.  
* The bounded path and its local or OPS evidence do not authorize production writes, create QA PASS, satisfy an acceptance token, move PF09 status, or establish broad HumanDesignAPI v2 conformance.  
* Preserve the public Reader contract. No public Reader byte change is implied by this mechanics posture.  
* HDE-EPIC037-style mapped dry-run proof may support scoped BodyGraph/person/cache/compat evidence flows. It does not by itself prove durable BodyGraph cache persistence, production writes, production upsert authorization, public Reader changes, new public routes, app-side HumanDesignAPI ownership, or broad HumanDesignAPI v2 platform conformance.  
* `ChartResult` StandardResponse data MUST NOT be written into the durable BodyGraph cache as reusable user data until a bounded mapped-cache persistence slice proves adapter-mapped HDE data, write/read-back parity, idempotence, no raw v2 vendor envelope persistence, no raw request or response body persistence, closed-rails refusal preservation, and governed evidence loop updates.  
* `ChartSimpleResult` MAY be used for bounded live smoke, auth/geokey proof, route-family confirmation, or provider availability proof only with explicit nonclaims for full BodyGraph detail unless it proves every required field.  
* Future mapped-cache persistence mechanics, if implemented, MUST write adapter-mapped HDE BodyGraph/cache payloads, not raw HumanDesignAPI v2 envelopes. The proof family must include mapped output before write, cached output after DB read, canonical-equivalence evidence for governed fields, idempotence evidence, no-secret and no-raw-vendor-payload evidence, and Human Evidence Index and Machine Mirror updates when new governed artifacts are created.  
* Preserve the public Reader contract. No public Reader byte change is implied by this mechanics posture.

HDAPI v2 rails and Live QA mechanics. The repo MUST provide closed-rails and open-rails proof mechanics for HumanDesignAPI v2 conformance. Closed-rails mechanics MUST prove deterministic refusal and no outbound I/O when rails are closed.

Default open-rails posture. Open-rails vendor smoke, when required, is PO-only execution and MUST be treated as an OPS task, not ordinary PR work and not QA substitution. The mechanics MUST require secret-safe, governed evidence for any PO-run open-rails smoke, including command transcript, stdout, stderr, exit code, redacted or presence-only secret posture, request summary, result summary, and file checksums, while avoiding plaintext secrets and unapproved vendor payload storage.

Narrow implementation-PR exception. One PR-specific open-rails vendor development proof MAY occur inside an implementation PR only when the Product Owner explicitly authorizes that exact capture in advance and the bounded proof:

* records either independently proven non-production posture or the explicit Product Owner override truth without inventing environment provenance;  
* defines and enforces a strict request ceiling;  
* stores no plaintext secret, raw request body, or raw vendor response payload;  
* keeps ordinary CI non-live;  
* preserves fixture-backed deterministic proof as a separate required proof surface;  
* grants no recurring, inferred, or general agent authority for later open-rails execution; and  
* makes no QA PASS, OPS-completion, acceptance-token, PF09-status, deployment, production-conformance, or epic-closeout claim.

Production/user-surface open-rails proof posture. Mechanics affecting runtime compute, BodyGraph resolution, vendor ingest, route-policy behavior, CLI/operator-facing runtime behavior, deployed behavior, or other production/user surfaces MUST distinguish closed-rails control-flow proof from open-rails runtime behavior proof. When the owning epic or QA plan affects such a surface, PF14 expects the relevant mechanics to support at least one bounded, intentional, secret-safe, evidence-recorded open-rails QA proof for the affected runtime behavior. PF14 records the mechanical proof distinction only; QA planning, acceptance tokens, gates, and closeout posture remain owned by their single homes.

Selected-route behavior proof. For BodyGraph/vendor mechanics, the proof family MUST show the actual selected runtime route behavior and preserve nonclaims for any route family, payload family, adapter/schema mapping, public surface, OPS execution, runtime conformance, durable cache-write behavior, or production posture not proven by that evidence.

HDAPI v2 error, retry, and rate-limit mechanics. The repo MUST provide deterministic mapping proofs for v2 vendor HTTP outcomes, error envelope behavior, Retry-After behavior, rate-limit headers, malformed responses, and typed HDE errors. These proofs MUST avoid vendor payload echo, avoid secrets in logs, and preserve deterministic output. This guide names the mechanical responsibility only; token semantics remain owned by HDE-Governance.

HDAPI provider retry and status classification mechanics. The vendor seam MUST classify provider HTTP outcomes deterministically before retry decisions. Retryable outcomes are limited to actual `network_error` and `5xx` outcomes. `429` and all other `4xx` outcomes MUST NOT be retried. Non-200 HTTP statuses outside `4xx` and `5xx` MUST be classified as `http_status_other` with provider error posture and MUST NOT be retried.

HDAPI redirect handling mechanics. The default vendor request path MUST NOT follow redirects when provider status classification is the proof target. Redirect responses such as `302` with `Location` MUST surface the original response status and bounded metadata to the vendor seam so the seam can classify the original outcome. HTTPError responses returned by the underlying request library MUST be converted into status, body, and header tuples before classification, without treating redirect-following as proof of provider behavior.

HDAPI provider policy proof mechanics. Provider policy evidence MUST cover pinned timeout profiles, pinned max-attempt domains, deterministic jitter-free backoff, typed `429`, Retry-After parsing for delta-seconds and HTTP-date forms, invalid Retry-After omission, closed-rails refusal, no-live-vendor local proof posture, and the non-retry behavior for `429`, other `4xx`, non-200 non-5xx statuses, and redirect responses.

HDAPI SAFE-rails log posture mechanics. Vendor SAFE-rails logs MUST be keys-only, bounded, and secret-safe. They MUST NOT record request bodies, response bodies, raw secret headers, plaintext secret values, or unbounded labels. They MUST expose bounded diagnostic keys sufficient to prove rails state, route family, timeout profile, and success or failure class observability, including observed `none`, `network_error`, `4xx`, `5xx`, and `429` classes where the proof family claims that coverage.

HDAPI log evidence collision guard. Vendor-specific log samples and rails-scope evidence MUST use PR-specific governed evidence families when they would otherwise collide with shared DB-bridge or cross-epic evidence paths. Shared evidence paths MUST NOT be overwritten by vendor-specific proof payloads. If a collision is discovered, the final proof family MUST restore the shared path contents, move vendor-specific evidence to its scoped family, and regenerate Human Index, Machine Mirror, hash sentinel, path proofs, and orientation evidence from the final state.

HDAPI v2 evidence mechanics. The repo MUST provide evidence generators and validators for the HDAPI v2 contract inventory, request shaping, response mapping, source selection, legacy-v1 guard, adapter-boundary proof, closed-rails refusal proof, open-rails smoke summary where PO-executed, error mapping, rate-limit mapping, normalized data path proof, source-cache replay, source-cache checksum proof, endpoint-tier parsing, anomaly quarantine, and index or mirror binding. Governed paths, schemas, path-proof naming, Human Evidence Index binding, Machine Mirror binding, canonical JSON rules, and evidence catalog ownership remain routed to HDE-Schemas & Artifacts and HDE-Build Checklist by title. PF14 does not pin future runtime repository paths for this family; records-only closure traces may list observed paths.

HDAPI v2 evidence generators MUST fail closed when:

* Required source inventory is missing.  
* A required source-inventory row lacks the cache body, cache path, or cache checksum needed for closed-rails replay.  
* `v2-routes.yaml` or `v1-routes.yaml` validation fails.  
* The suspect `api-reference/openapi.json` has not been validated but is being used as authority.  
* Unavailable or non-200 suspect `api-reference/openapi.json` input blocks promoted inventory despite validated v2 and v1 route specs remaining usable.  
* Endpoint tiers are inferred from fixed substring defaults instead of parsed from the current cached endpoint-tier excerpt.  
* Recommended v2 chart routes are collapsed into legacy v1 BodyGraph routes without an explicit legacy decision.  
* Required path-proof, Human Index, or Machine Mirror binding is absent for governed evidence.  
* Closed-rails proof attempts outbound I/O.  
* A governed closed-rails evidence generator certifies check or write output without enforcing deterministic closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) before rendering, checking, or writing the evidence.  
* Open-rails evidence is not PO-executed, secret-safe, and governed.  
* Any AI, OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, or AI evidence family is introduced under this conformance work.  
* Any AI, OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, or AI evidence family is introduced under this conformance work.

HDAPI adapter/presenter boundary-proof mechanics. Boundary-proof mechanics for the HDAPI vendor seam MUST use a conservative, fail-closed posture. Unknown public routes, response-producing paths, serializer paths, external-I/O paths, guard provenance, presenter provenance, adapter route registrations, or evidence-binding postures MUST NOT be silently treated as PASS.

Analyzer and renderer separation. Boundary analysis MUST be separated from governed evidence rendering. The analyzer owns boundary truth classification and should return explicit findings, unknowns, public-route deltas, responder provenance, serializer findings, external-I/O findings, guard provenance, evidence-family bindings, and verdict status. The evidence renderer may render analyzer output into governed artifacts, path proofs, and index or mirror rows, but MUST NOT independently decide architecture-boundary truth.

Boundary taxonomy mechanics. The boundary proof MUST use a table-driven taxonomy and invariant suite that covers route registration surfaces, public route signatures, response-producing paths, presenter-valid paths, presenter-bypass paths, serializer families, external-I/O families, import and alias forms, cross-file helper chains, vendor guard provenance, pure-compute forbidden operations, public/internal route classification, and evidence-family binding for the applicable PR proof family. Missing or unsupported taxonomy categories must remain visible as unknown or fail-closed outcomes, not be hidden by a PASS renderer.

AI boundary for HDAPI v2 mechanics. OpenAI will not be used inside the HD Engine under this conformance work. AI remains a Glow development tool only. No mechanics, generator, QA harness, vendor seam, config key, evidence family, acceptance posture, or architecture flow may infer OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, or AI-enablement scope from HumanDesignAPI documentation.

Observed PR-01 paths include:

* `artifacts/vendor/policies_pinned.md`  
* `artifacts/vendor/retry_after_parse.log`  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json`  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json`  
* `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

Observed PR-01 proof posture. The PR-01 family records no live vendor call, fixture-backed or local proof for open exception posture, pinned timeout and max-attempt policy, deterministic retry/backoff domains, typed `429`, Retry-After parsing, closed-rails refusal, non-retry behavior for `429`, other `4xx`, and non-200 non-5xx statuses, and provider classification as `http_status_other` for statuses outside `4xx` and `5xx`.

Observed PR-01 remediation posture. The final PR-01 state records retry classes limited to `network_error` and `5xx`, default request redirect following disabled for provider classification, HTTPError responses converted into classifiable status/body/header tuples, and regression coverage for both injected and default `302` behavior.

Observed PR-01 evidence-refresh posture. The final PR-01 evidence family removes stale ingest side-effect classification and names remaining cross-family proof refreshes as expected updater convergence or required dependency refresh, including writer, topology, and HDE-EPIC030 PR-03, PR-04, and PR-05 proof companions. The final state records Human Index, Machine Mirror, hash sentinel, path-proof, evidence-path, mirror-schema, LF-ending, orientation, evidence generator, and `git diff --check` validation as green.

HDE-EPIC031 PR-02 keys-only log posture proof family observed (records-only). PF14 records these paths as the observed PR-02 proof family for the completed SAFE-rails observability slice. This is a records-only closure trace for HDE-EPIC031 PR-02 and does not pin future HDAPI v2 conformance paths.

Observed PR-02 paths include:

* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json`  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`  
* `ci/jobs/logs_keys_only_redaction.yml`  
* `docs/evidence/INDEX.json`  
* `artifacts/evidence_index.jsonl`

Observed PR-02 proof posture. The PR-02 family records closed rails, no live vendor calls, bounded log labels, success and failure class observability, keys-only vendor samples, no forbidden hits, no key violations, payload-body absence, plaintext-secret absence, raw-secret-header absence, deterministic redaction scan, and PR-specific vendor rails-scope evidence.

Observed PR-02 collision-remediation posture. The final PR-02 state moves vendor-specific log sample and vendor rails-scope evidence to PR-specific files under `audit/qa/hde-epic031/pr-02/`, restores the shared DB-bridge paths, filters superseded colliding entries, and keeps the final Human Index and Machine Mirror rows bound to the PR-specific vendor evidence family.

Observed PR-02 validation posture. The final PR-02 state records the targeted BodyGraph test suite, the PR-02 evidence generator check, Evidence Index update check, topology orientation check, evidence path validation, mirror schema check, evidence index hash check, LF and final-LF checks, evidence skeleton test, and `git diff --check` as passing.

HDE-EPIC031 PR-03 SAFE rails evidence and indexing proof family observed (records-only). PF14 records these paths as the observed PR-03 proof family for the completed SAFE-rails evidence/indexing slice. This is a records-only closure trace for HDE-EPIC031 PR-03 and does not pin future HDAPI v2 conformance paths, create acceptance tokens, change public Reader scope, or introduce AI/LLM/OpenAI/model-call scope.

Observed PR-03 paths include:

* `audit/qa/hde-epic031/pr-03/evidence_family_map.json`  
* `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`  
* `audit/qa/hde-epic031/pr-03/evidence_refresh.log`  
* companion `*.path_proof.txt` files for the PR-03 evidence artifacts  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Observed PR-03 proof posture. The PR-03 family records governed SAFE rails evidence and indexing coherence by binding PR-01, PR-02, and PR-03 SAFE rails artifacts through the Human Evidence Index, hash sentinel, Machine Mirror, co-located path proofs, evidence-family map, coherence artifact, and refresh log.

Observed PR-03 remediation posture. The final PR-03 state records bounded side-effect classification for writer proof companions, topology orientation refreshes, and HDE-EPIC030 PR-03, PR-04, and PR-05 proof companions, including associated Machine Mirror artifact keys and discovered paths.

Observed PR-03 validation posture. The final PR-03 evidence family records PASS only when side-effect paths exist, proof companions validate against their targets, and classified Machine Mirror rows match artifact key, proof anchor, sha256, and size. The final state records generator write/check, Evidence Index updater write/check, orientation write/check, evidence path validation, mirror schema, evidence hash, LF check, py-compile, and `git diff --check` validation as green.

## 1.2 Environment & secrets (names-only)

Env allow-list.

* Defined by title (HDE-Schemas & Artifacts / HDE-Governance). CI fails on unknown or missing required keys; secrets are never printed (keys-only logs with redaction).

MODO\_ prefix (non-canonical).

* Any environment variable name beginning with MODO\_ is non-canonical and MUST NOT be required or interpreted as meaningful by repo components, QA harness entrypoints, step-log schemas, or governed evidence.

* If MODO\_ variables appear in captured\_env due to legacy scripts or wrapper state, they MUST be treated as inert traceability-only values (not required keys, not rails proof, and not acceptance gating).

No QA-time env var minting.

* QA execution and Moon Loop evidence repair MUST NOT mint new environment variable names at runtime. If an execution flow requires a new environment variable name, it must be defined in the env allow-list (titles-only) before any governed QA artifact depends on it.

Rails posture (derives from PF07).

* Rails defaults follow the Env Deployment Inventory (titles-only): dev & stage OPEN, prod CLOSED, CI CLOSED. This guide does not restate the table; it defers to Infrastructure.

CI default CLOSED & evidence.

* CI pipelines run with rails CLOSED by default. Any pre-commit/CI job that opens rails must pin timeout/retry/backoff policy (closed domain) and attach governed evidence in the same PR (titles-only routing to Governance/Schemas & Artifacts).

Determinism pins (all environments).  
Any canonicalization, hashing, header snapshotting, or governed evidence capture MUST run with:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Live QA rails: no non-canonical determinism env pins (normative).  
Canonical determinism pins are limited to the canon set. Live QA steps that produce governed bytes or governed evidence MUST NOT add additional required env pins beyond the canonical pins defined here (locale and timezone pins, plus rails variables where applicable).

In particular:

* PYTHONHASHSEED MUST NOT be added as a required rail/pin for Live QA plan approval or execution. It is not part of the canonical determinism env pins set.

Determinism must be achieved by explicit ordering in code and tools (sorted keys, sorted lists, no unordered set/map iteration on governed bytes), not by interpreter hash-order controls. If PYTHONHASHSEED is used for one-off diagnostics, it MUST be explicitly labeled diagnostic-only and MUST NOT be interpreted as satisfying or extending the canonical determinism env pins evidence surface.

Acceptance for determinism pins is governed by HDE-Governance and proven via governed evidence and QA checks (titles-only). This guide does not list token names.

## 1.3 Evidence & CI coupling \[Required-Now\]

Scope (normative). Mechanics must keep human and machine evidence in lockstep for every artifact this guide produces (math proofs, goldens, headers-only snapshots, scripts). Transport bytes and ops surfaces are routed by title only to HDE-CLI-API-Vendor Ref and HDE-Governance.

Single homes

* Human index. docs/evidence/INDEX.json — titles and paths only; no payload bytes. Must maintain 1:1 parity with the machine mirror (see §8.3).  
* Human index hash sentinel. docs/evidence/INDEX.sha256 — hash sentinel for the Human Evidence Index. This file is governed and MUST be updated whenever docs/evidence/INDEX.json changes.  
* Machine mirror (records-only). artifacts/evidence\_index.jsonl — fixed path; one JSON object per line; canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing \\n). This section surfaces the minimum shape used by implementers; the normative mirror schema lives in PF12.

No alternate mirror copies (normative).  
The Machine Mirror has exactly one canonical file path: artifacts/evidence\_index.jsonl. Tools and CI MUST NOT write, validate, index, or bind acceptance evidence to any second “mirror” file under docs/evidence/\*\* (for example, docs/evidence/INDEX.machine\_mirror.jsonl). If such a file appears, treat it as non-authoritative drift until and unless HDE-Schemas & Artifacts explicitly canonizes an additional mirror surface (titles-only).

Mirror discipline (normative).

* The machine mirror is one and only one file at artifacts/evidence\_index.jsonl; records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; exactly one LF per record).  
* Unknown keys are rejected; sort-before-write by (artifact\_key,discovered\_physical\_path).  
* Exact field order (per PF12/PF10): artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes.  
* Join rule. (artifact\_key, discovered\_physical\_path) in the mirror equals (title, path) in the human Index (1:1).  
* Unknown keys. Rejected (fail CI).

Path-proofs (MUST).

* Store a path\_proof.txt (or equivalent) alongside each artifact with a stat transcript (size, mtime, sha).  
* Reference it via proof\_anchor in the mirror record.

Update discipline (same PR).

* Whenever any golden, snapshot, or script moves or changes, update Appendix D and the machine mirror in the same commit/PR. CI fails on mismatch.

Environment pins (determinism).

* All captures and comparisons run with LC\_ALL=C, LANG=C, TZ=UTC.  
* Arrays that represent sets are deduped and ASCII-sorted before hashing and compare.

Pipeline coupling (minimum sequence).

1. Build and normalize.  
2. Run unit and property tests.  
3. Produce artifacts (goldens, headers-only snapshots, logs).  
4. Write or refresh human Index entries.  
5. Write mirror records with path-proofs.  
6. CI parity check: 1:1 human↔machine, schema-valid, canonical JSONL.  
7. Fail closed on any drift.

Acceptance and CI (routing only).  
Acceptance criteria and token naming are governed by HDE-Governance (titles-only). Evidence schemas, evidence catalog entries, and canonical path/mirror rules are governed by HDE-Schemas & Artifacts and Glow QA Guide (titles-only). This section specifies mechanics requirements only and does not list token names.

Header snapshot normalization (normative).

* Stored header snapshots MUST use lower-case header names; values are preserved verbatim.  
* Proof and acceptance binding are governed elsewhere (titles-only).

Files under transient generators (for example, codex/out/\*\*) MUST NOT be indexed. Human Index and Machine Mirror updates MUST occur in the same PR; the mirror is records-only canonical JSONL (UTF-8, ASCII-sorted keys, compact, exactly one LF), rejects unknown keys, and carries a proof\_anchor to a path-proof file in the same directory.

CI MUST fail closed on any of the following:

* Human Evidence Index ↔ Machine Mirror parity mismatch (1:1 join failure),  
* non-canonical JSON/JSONL,  
* unknown keys in mirror records, or  
* missing/invalid path-proofs (proof\_anchor).

Acceptance token naming and gating for these checks are owned by HDE-Governance (titles-only). This guide does not list token names.

Routing (titles-only). Manifest and release identity and the mirror schema ownership live in HDE-Schemas & Artifacts. Transport A7 proofs and /internal/version evidence live in HDE-CLI-API-Vendor Ref and HDE-Governance.

Governed locations (normative).  
All QA/audit proofs MUST reside under governed paths:

* artifacts/\*\*  
* audit/\*\*  
* docs/evidence/\*\*

Core evidence must remain text-based and agent-readable.

Core governed evidence for the HD Engine — including:

* the Human Evidence Index (docs/evidence/INDEX.json),  
* the Machine Mirror (artifacts/evidence\_index.jsonl),  
* any evidence bundles and their manifests, and  
* key QA logs and summary artifacts referenced by this guide —

MUST be stored as plain-text, UTF-8 files under these governed paths and remain suitable for inspection by humans and Codex/ChatGPT-class agents at the PR level. Binary or compressed bundles (for example, .zip, .tar.gz) MAY be produced as supplementary artifacts for local convenience, but MUST NOT serve as the only governed evidence for any acceptance token that relies on Engine evidence; there must always be at least one text-based bundle manifest, log, or summary file under a governed path that covers the token’s evidence needs.

This posture ensures that the ledger-centric evidence model (Human Index, Machine Mirror, bundle manifests, and QA logs) remains readable and auditable by both humans and automated agents, and it aligns Mechanics with the evidence and Reality Audit guidance in HDE-Schemas & Artifacts, Glow QA Guide, and the Reality Audits PF by title.

### 1.3.1 Evidence jobs (single-writer tools)

Scope (normative).  
Only a small set of evidence writers may write governed evidence artifacts (ordering artifacts, Evidence Index, Machine Mirror, bundles/manifests, and path-proofs). All other code — including tests and ad-hoc scripts — MUST NOT modify governed evidence directly.

Focused-owner allocation (normative).

* Every governed primary MUST have exactly one active producer with a bounded, documented primary write set.  
* The focused BodyGraph policy producer is the sole active primary owner for source selection, source invariance, refresh policy, metrics, and keys-only BodyGraph evidence.  
* The shared Presenter-history primary MUST have one dedicated owner that reconstructs it from one immutable, closed-shape, four-record source fixture. The owner MUST validate record count and order, unique record IDs, per-row hashes, complete output size, and complete output hash before replacement.  
* Shared Presenter-history writes MUST use a same-directory temporary file, flush and fsync before atomic replacement, preserve the prior destination on failure, remove temporary residue, and make `--check` read-only.  
* General Presenter comparisons MUST be stdout-only when the caller does not supply a diagnostic log path. Mutable diagnostic comparisons MUST use caller-supplied task-scoped paths and MUST NOT default to the governed shared-history primary.  
* A retired broad evidence generator MUST remain non-writing, perform no import-time generation or delegation for side effects, return nonzero, and emit a stable diagnostic directing callers to the focused generators. Active invocations MUST migrate to focused owners; historical references remain provenance.  
* Current database-selection evidence MUST use the direct-only focused producer. Superseded bridge-era generators, dedicated bridge receipts, and direct-versus-bridge current-proof claims MUST NOT be restored or presented as active owners.  
* Sibling path proofs, the Human Evidence Index, the Human Index hash sentinel, the Machine Mirror, the Mirror checksum, and orientation/index companions remain solely owned by the canonical evidence updater.  
* Focused write-set tests MUST prove disjoint primary ownership, read-only check behavior, failure atomicity, no implicit governed diagnostic destination, and fixed-point output across every allowed producer order.  
* Unknown active invocations, overlapping write sets, direct companion writes, stale current keys, wrong shared-history bytes, mutable shared-history defaults, or updater divergence MUST fail closed.

Exception (narrow, explicit).  
 A7 proof artifacts under artifacts/proofs/ may be emitted only by the focused A7 transport test harness when `HDE_WRITE_A7_PROOFS=1`. Default test runs MUST NOT write these files. The harness MUST NOT update the Evidence Index, Machine Mirror, ordering artifacts, or path-proofs; those remain single-writer outputs of the evidence tools.

Evidence tools (titles-only).  
Ordering generator.

* A single ordering generator tool (for example, tools/order/generate\_ordering\_artifacts.py) is the single writer for ordering artifacts under artifacts/engine/order/\*\* (for example, sorted snapshots, ordering logs, ABBA evidence).

Evidence skeleton tools.  
tools/evidence/update\_evidence\_index.py is the single writer for:

* docs/evidence/INDEX.json (Human Index, titles/paths only),  
* docs/evidence/INDEX.sha256 (hash sentinel),  
* artifacts/evidence\_index.jsonl (Machine Mirror), and  
* governed \*.path\_proof.txt transcripts for artifacts listed in this guide.

Evidence generator direct-invocation posture (normative). Repo-owned evidence generators MUST be directly runnable from the repository root using their documented Python invocation without requiring callers to set PYTHONPATH. If a generator imports repo modules, it MUST establish repository-root importability before those imports and fail as tooling if it cannot.

Updater fixed-point convergence (normative). `tools/evidence/update_evidence_index.py` MUST converge to a deterministic fixed point from a clean checkout in CI-like order. The updater MUST centralize Human Index, hash sentinel, Machine Mirror, and governed path-proof writes inside one bounded convergence loop and MUST NOT require a second manual rerun to settle stale in-memory or pre-write proof metadata.

Check-mode equivalence (normative). `python tools/evidence/update_evidence_index.py --check` MUST validate the same ordered write model used by normal generation. A `--check` failure caused by updater self-instability, rather than by true artifact drift, is a mechanics defect.

Evidence generator PASS predicate and refresh coherence (normative). Governed evidence generators MUST emit PASS only when all decisive predicates for the claimed family evaluate true. A generator MUST NOT use parsed-object equality as a substitute for canonical-byte equality when bytes are the acceptance subject, and MUST NOT accept a lowercase 64-hex value as identity proof without recomputing the expected hash from the final governed artifacts. When an artifact claims AB↔BA identity-hash equality, current AB and BA body hashes MUST be compared in that run and the match result MUST be part of the PASS predicate. When a binding artifact summarizes canonical compare evidence, the top-level binding status MUST include the canonical compare result and MUST NOT report PASS if the canonical compare result is FAIL.

Final-artifact regeneration. When a generator hardening change alters decisive predicates, binding status, or generated log content, the final governed artifacts, sibling path proofs, Human Evidence Index, Machine Mirror rows, hash sentinel, and orientation snapshot MUST be regenerated from the final generator logic in the same governed pass. Stale proof, stale binding logs, or stale mirror metadata after regenerated artifact bytes is a mechanics defect.

Evidence-generator failure-path coverage. Governed evidence generators that emit PASS for identity, binding, canonical compare, index/mirror, or path-proof families MUST include targeted negative-path tests for the decisive predicates that could otherwise falsely pass. At minimum, generators that compare AB and BA bodies MUST test a mismatched-body failure path, and generators that summarize canonical compare or binding evidence MUST test a failure path where a lower-level compare fails and the top-level binding also fails.

Adjacent-generator audit trigger. When a false-positive PASS pattern is found in one EPIC-style evidence generator, the adjacent generators in that family or pattern class MUST be reviewed for the same omitted-predicate class and either receive targeted negative-path coverage or record a bounded no-impact finding in the governed PR evidence. This review creates no new acceptance token and no standalone HDE-Build Checklist task by itself.

Epic-specific mirror validation scope. Evidence skeleton tests MAY enforce an epic-specific acceptance-roster subset only against mirror records that belong to that exact epic. Non-target epic records MUST remain subject to mirror schema validation, field-set validation, uniqueness validation, sort-order validation, path-proof existence, and proof-anchor matching, but MUST NOT be compared against an unrelated epic’s acceptance roster. This rule is structural only and does not define, rename, or curate token names.

Bounded evidence-refresh side effects. When the evidence updater or generator refreshes governed proof companions outside the direct target family, the run evidence MUST name those refreshed families and classify them as expected updater convergence, required dependency refresh, or unexpected drift. Unclassified side-effect churn that obscures the direct evidence family is a mechanics defect until classified.

Bounded side-effect validation. When side-effect classifications are part of a governed evidence family’s PASS posture, the generator or updater check MUST validate the classified side-effect paths, their proof companions, and any affected Machine Mirror rows before reporting PASS. A classified side effect MUST NOT be treated as coherent if the path is missing, if the proof companion fails against its target, or if the Machine Mirror row does not match the expected artifact key, proof anchor, sha256, and size. This rule applies to normal generation and `--check` mode; self-generated artifact recursion concerns may affect write ordering, but they MUST NOT allow check mode to skip validation of final mirror bindings.

Scope of convergence (required). This fixed-point rule applies to:

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* governed `*.path_proof.txt` companions refreshed by the updater in that run

Additional evidence-discipline tools (normative):

* `tools/evidence/validate_evidence_paths.py` is the evidence-index path validator. It MUST load `artifacts/evidence_index.jsonl` and verify that each record’s `discovered_physical_path` is safe and exists on disk.

* Minimum rails include: reject absolute paths; reject traversal segments (`..`); resolve the candidate path and enforce repo-root containment via `resolved.relative_to(root)`.

* It MUST fail closed if any JSONL line is not a JSON object (dict), and MUST exit non-zero via `SystemExit` for invalid input.

* `tools/evidence/check_lf_endings.py` is the LF-ending gate wrapper. It MUST run `ci/checks/check_final_lf.sh` under determinism environment pins and MUST exit non-zero on failure.

Index and sentinel path-proofs (normative).  
docs/evidence/INDEX.json and docs/evidence/INDEX.sha256 are governed artifacts and MUST each have an up-to-date \*.path\_proof.txt. tools/evidence/update\_evidence\_index.py MUST refresh the path-proofs for the Human Evidence Index and its hash sentinel during both write and check passes, so their proofs cannot be left stale after regeneration.

In addition to per-artifact entries, tools/evidence/update\_evidence\_index.py MUST:

* ingest one or more bundle manifests emitted by the bundle generator (see below),  
* compute hashes for bundle files and manifests under the same determinism pins as other evidence (§1.2),  
* write bundle-level Machine Mirror rows and bundle path-proofs for those bundles, and  
* preserve behaviour for non-bundled evidence families (backwards-compatible for legacy rows).

Index \+ Mirror parity checks (§1.3) MUST treat bundle rows and manifests as first-class governed artifacts: manifests must be valid JSON/JSONL, conform to the PF12 bundle manifest schema, contain no unknown keys, and obey any bundle-level invariants (for example, member count and deterministic ordering) defined there.

tools/evidence/orientation\_demo.py owns the topology orientation demo artifact (audit/gates/topology/orientation\_demo.txt) and its path-proof and MUST NOT be bypassed by ad-hoc edits.

Evidence bundle generator.  
A dedicated bundle generator tool (titles-only here; concrete name and path live in the repo) is responsible for:

* collecting raw evidence outputs for one or more high-churn families (for example, ordering logs, sampler/core outputs, complex config dumps),  
* building a textual bundle (for example, JSONL, one logical artifact per line) under a governed path (artifacts/\*\* or docs/evidence/\*\*), and  
* emitting a bundle manifest (JSON/JSONL) that lists, for each member, at least: logical artifact\_key, sha256, size\_bytes, and any additional descriptors defined in PF12.

The bundle generator MUST run under the same determinism pins as other evidence tools (LC\_ALL=C, LANG=C, TZ=UTC, plus any rails pins from §1.2) and MUST NOT hand-edit existing governed artifacts. Its outputs (bundles and manifests) are consumed by tools/evidence/update\_evidence\_index.py as described above.

Orientation demo and evidence skeleton coupling (normative).  
Mechanics treats the topology orientation demo as part of the same evidence skeleton as the Human Evidence Index and Machine Mirror. The following coupling rules apply:

* Any PR that runs tools/evidence/update\_evidence\_index.py in write mode to change governed evidence under docs/evidence/**, artifacts/**, or audit/\*\* MUST also run tools/evidence/orientation\_demo.py in write mode in the same PR and commit the updated audit/gates/topology/orientation\_demo.txt and its \*.path\_proof.txt before invoking either tool’s \--check mode.  
* Index/Mirror changes without a matching, freshly generated orientation demo are out of spec and MUST be treated as drift: tools/evidence/orientation\_demo.py \--check is expected to fail with an orientation-drift error in such cases, and CI MUST NOT be forced green by skipping or bypassing the orientation demo.  
* Evidence harnesses and scripts that wrap tools/evidence/update\_evidence\_index.py as a single job (for example, error evidence generators, sampler/core evidence generators, bundle generators, or combined evidence pipelines) MUST treat tools/evidence/orientation\_demo.py as part of the same single-writer chain for the evidence skeleton: when they refresh governed artifacts and the Index/Mirror, they MUST also refresh the orientation demo in that same job and PR.

This clarification does not change which tools are allowed to write governed evidence; it makes explicit that tools/evidence/update\_evidence\_index.py, the bundle generator, and tools/evidence/orientation\_demo.py together own the evidence skeleton for both per-artifact and bundle-level families, so that the topology orientation demo always reflects the current governed evidence skeleton and orientation-drift is caught and fixed in the same change that expands or shrinks the skeleton.

Mechanics MUST NOT hand-edit governed evidence artifacts (ordering artifacts, bundles, manifests, Index, mirror, path-proofs, topology orientation demo). Manual editing is reserved for canonical Doc-Delta work in PF documents; repository artifacts are tool-generated only.

### 1.3.2 Evidence change workflow

Scope (normative)  
Any PR that changes governed artifacts under artifacts/**, docs/evidence/**, or audit/\*\* MUST follow the evidence change workflow.

Governed artifacts include, at minimum:

* ordering artifacts under artifacts/engine/order/\*\*  
* the Human Evidence Index and Machine Mirror  
* topology orientation demo  
* sampler evidence families under artifacts/sampler/\*\*  
* Engine Core evidence families under artifacts/core/\*\*  
* their schemas under docs/schemas/\*\*  
* all \*.path\_proof.txt listed in this guide and in §37 Documentation Artifacts and Registry

Workflow (minimum sequence)  
For PRs that touch governed evidence:

Ordering artifacts (when in scope)

* Run the ordering generator and its \--check mode whenever ordering artifacts are in scope for the change.  
* Verify two-run identity for ordering artifacts under determinism pins (LC\_ALL=C, LANG=C, TZ=UTC).

Sampler and Engine Core evidence (when in scope)  
When sampler evidence families (artifacts/sampler/**) and their schemas (docs/schemas/sampler/**) are in scope:

* run the sampler evidence generator under closed rails to refresh those artifacts and their schema files.  
* tools MUST call the sampler core in pure-compute mode and MUST NOT hand-edit sampler evidence or schemas.

When Engine Core evidence families are in scope:

* run python tools/evidence/generate\_engine\_core\_evidence.py under closed rails to regenerate Engine Core evidence artifacts and their schemas (for example, purity, two-run identity, AB↔BA parity, and JSON-compare logs under artifacts/core/\*\* with matching schemas under docs/schemas/core/\*\*).  
* tools MUST NOT hand-edit Engine Core evidence artifacts or schemas.

After sampler and Engine Core evidence artifacts have been refreshed:

* python tools/evidence/update\_evidence\_index.py \--check (see below) MUST be used to regenerate the Human Index, Machine Mirror, and path-proofs so that produced\_at\_utc in mirror records and path-proofs reflects the actual refresh time for both sampler and Engine Core evidence and is consistent across artifact payload, mirror record, and proof transcript.

Evidence Index and mirror  
Run python tools/evidence/update\_evidence\_index.py \--check to validate and refresh:

* docs/evidence/INDEX.json (Human Index, titles/paths only)  
* docs/evidence/INDEX.sha256 (hash sentinel)  
* artifacts/evidence\_index.jsonl (Machine Mirror)  
* all governed \*.path\_proof.txt transcripts from a single source of truth, including:  
  * docs/evidence/INDEX.json.path\_proof.txt  
  * docs/evidence/INDEX.sha256.path\_proof.txt

If the Index or sentinel path-proofs are stale or do not match the on-disk bytes, treat this as governed-evidence drift and stop. The correct remediation is regeneration via the canonical evidence tooling (do not hand-edit proofs or mirror rows).

Topology orientation demo  
Run python tools/evidence/orientation\_demo.py \--check to validate that the on-disk orientation report (audit/gates/topology/orientation\_demo.txt) is coherent with the current Index/Mirror state and not stale.

Mirror schema and path-proofs  
Run python ci/checks/check\_mirror\_schema.sh to enforce:

* (Canonical invocation: python ci/checks/check\_mirror\_schema.sh. bash ci/checks/check\_mirror\_schema.sh is invalid and MUST NOT be used.)  
* the canonical mirror schema (field set, field order, canonical JSONL)  
* uniqueness of (artifact\_key, discovered\_physical\_path)  
* correctness of proof\_anchor and .path\_proof.txt contents for all governed artifacts, including sampler and Engine Core families and their schemas

Mirror self-record semantics (normative; special case)  
Evidence validation MUST treat self-referential evidence artifacts as a special case (for example, validations involving the Machine Mirror file itself and any self-record rules defined in the mirror schema). The special-case semantics are owned by HDE-Schemas & Artifacts (titles-only). Mechanics requires that:

* CI and local validators MUST include explicit self-record handling (not an implied side effect of generic hashing).  
* CI MUST include a dedicated regression test that exercises the self-record case and fails with a diagnostic that explicitly mentions “self-record” when violated (to prevent “mystery PROOF\_SHA mismatch” loops).  
* When the self-record check fails, the validator MUST surface expected vs found values and identify the self-record rule as the governing constraint (titles-only).

Schema validator dependency posture (normative).  
Evidence schema validation MUST be import-safe and CI-repeatable. A missing optional dependency MUST NOT cause pytest collection errors or validator crashes that prevent the evidence workflow from running. Any evidence schema validator MUST either:

* declare its dependency set as required for CI and ensure CI installs it, or  
* skip cleanly when the dependency is absent, with an explicit skip reason and an install hint.

When a validator cannot run due to missing optional dependencies, QA harnesses and CI logs MUST classify this as a tooling/environment issue (not an engine behavior failure) and must surface the install hint.

Evidence ledger  
Record an evidence addendum in Glow HD Engine — Build Notes & Integration Addenda (Living) for the PR, describing new or changed governed artifacts and the evidence tools that produced them.

Determinism & rails  
The evidence change workflow MUST run under rails-closed, determinism-pinned CI environments:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* LC\_ALL=C  
* LANG=C  
* TZ=UTC

This is consistent with the rails posture described in §1.2 and the Evidence Index tokens in §1.3.

The release sanity pipeline harness (for example, python tools/evidence/run\_sanity\_pipeline.py) is treated as the scripted implementation of this workflow for sampler and Engine Core evidence under closed rails. It MUST:

* call the sampler evidence generator and tools/evidence/generate\_engine\_core\_evidence.py under the same determinism pins, then  
* refresh the Evidence Index and Machine Mirror,  
  so that the sanity pipeline log reflects the full suite of determinism and evidence checks for both sampler and Engine Core.

The determinism env-pins gate (ci/checks/check\_env\_pins.sh) MUST be wired to the same closed-rails suite set. It runs the expanded determinism and evidence checks (including sampler and Engine Core suites) and verifies that the env-pins log remains in sync with the on-disk evidence skeleton; the sanity pipeline log and env-pins log are treated as governed artifacts whose path-proofs and Machine Mirror records MUST track their canonical bytes over time.

Plan-required Python entrypoint wrapper for the env-pins gate (EPIC024 D01). This entrypoint MUST emit the canonical env-pins evidence surface defined below.

* `python tools/evidence/run_env_pins_gate.py` (wraps `ci/checks/check_env_pins.sh`, including required env setup)

* audit/qa/hde-epic024/checks/D01\_env\_pins\_gate/primary.log

Determinism env pins evidence surface (normative)  
The canonical governed evidence surface for determinism env pins is:

* audit/gates/determinism/env\_pins.log  
* audit/gates/determinism/env\_pins.log.path\_proof.txt

Validator posture (normative; minimal predicate surface).  
The env\_pins.log predicate surface MUST be a single-line JSON object that is schema-valid as determinism\_env\_pins.v1 and includes a rails object capturing the pinned run posture (at minimum: ALLOW\_NETWORK, SAFE\_MODE, LC\_ALL, LANG, TZ).

This is the only acceptable binding for determinism env pins in acceptance ledgers and indexing:

* the Human Evidence Index MUST reference audit/gates/determinism/env\_pins.log, and  
* the Machine Mirror MUST mirror that exact discovered\_physical\_path and use audit/gates/determinism/env\_pins.log.path\_proof.txt as proof\_anchor.

Other “env pins” snapshots may exist for other proof contexts, but they MUST NOT be treated as the determinism env pins acceptance surface.

This workflow makes the Evidence Index, Machine Mirror, ordering artifacts, sampler evidence, Engine Core evidence, and path-proofs move in lockstep and ensures that drift is caught early by CI, rather than after the fact.

Portable path-proof semantics (routing only)  
 Evidence jobs that write or validate governed \*.path\_proof.txt MUST apply the canonical path-proof schema and ownership rules defined in HDE-Schemas & Artifacts and Glow QA Guide. A governed path proof is correct when it has:

* the exact governed path;  
* the exact SHA-256 of the governed bytes;  
* the exact byte size;  
* all required companion fields;  
* the canonical field structure; and  
* valid UTC timestamp shapes.

mtime\_utc remains capture-time provenance and MAY seed a newly produced proof. Git does not preserve filesystem mtimes, so a later clone’s, cache restore’s, or CI checkout’s stat().st\_mtime is not an evidence input and MUST NOT be compared with the recorded mtime\_utc as a validity predicate.

produced\_at\_utc remains the logical evidence-production time. Where an artifact payload, Machine Mirror record, and path-proof transcript carry produced\_at\_utc for the same refresh, those governed values MUST remain coherent under the owning schema.

An unchanged proof whose path, SHA-256, size, required companion fields, canonical structure, and timestamp shapes remain valid MUST NOT be rewritten or re-timestamped merely to make a later checkout pass.

The canonical updater remains the owner of updater-generated path proofs. Checks MUST detect path, hash, size, field, schema, or companion drift and MUST NOT hand-edit proofs, compare clone-local mtimes, or repair unrelated governed evidence during validation.

---

## **1.4 Routing (single homes; no duplication)**

Public bytes: PF-Canon-HDE-CLI-API-Vendor-Ref; Math & preimage: PF-Canon-HDE-Math-Spec; Schemas, pack/manifest, canonical bytes, machine mirror: PF-Canon-HDE-Schemas & Artifacts; Governance (A7, ops posture, Evidence Index policy): PF-Canon-HDE-Governance

## **1.5 Acceptance (tokens; titles-only)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names.

The mechanics obligations in §1 require that acceptance proofs exist for:

* evidence/index parity and path-proof enforcement  
* determinism (two-run identity, AB↔BA neutrality, canonical JSON discipline)  
* rails posture enforcement for CI and QA environments  
* runtime/start-command wiring and readiness/health posture

## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**

Scope (normative): Mechanics requires a set of QA tooling components that support both CI and Live QA without relying on hand-edited commands or ad-hoc shells.

This section defines the mechanical responsibilities for:

* a QA tooling bootstrap harness that verifies the basic test/tooling environment  
* a Live QA harness that runs CLI/tests for QA, classifies failures as tooling vs behavior, and writes structured QA logs (including empties, exit codes, and stderr) under governed audit locations

QA plans, acceptance tokens, and epic-specific QA steps remain single-homed in Glow QA Guide, HDE-Build Checklist, HDE Phased Epics, and Glow Infrastructure by title; this section records the components that must exist in the repo.

Mechanical evidence requirement (normative; Live QA): Live QA evidence artifacts under audit/qa/\*\* MUST be produced by commands (tools/scripts/harness steps). Manual editing in an editor is prohibited for any artifact treated as QA evidence.

This applies specifically to:

* any “notes” artifacts required by a QA plan (for example D0 discovery notes or QA RCA/doc-delta summaries)  
* any Live QA summary artifact (for example QA\_SUMMARY.md)

Placeholders that imply human fill (for example “Result: (fill PASS/FAIL)” or “fill manually as run proceeds”) are non-conforming. PASS/FAIL must be derivable mechanically from command exit codes, existence checks, and captured logs.

Mechanics does not define QA plan content or token semantics here. It requires that the repo’s Live QA harness provide generator steps that produce these artifacts mechanically from machine-readable inputs.

### **1.6.1 QA tooling bootstrap harness (PRE-step component)**

Purpose (normative): Provide a single, scriptable bootstrap step that verifies the test tooling environment before any QA plan or Live QA flow runs tests or CLI commands against the Engine.

Behavior (minimum): The QA tooling bootstrap harness MUST:

* Activate the project environment.  
* Activate the project’s Python environment (for example, via a venv or equivalent). Mechanics does not pin the exact activation command; it requires that the harness run under the same Python interpreter and environment that the Engine uses for tests and CLI tools.  
* Verify pytest availability via the Python interpreter by running python \-m pytest \--version under the activated environment.  
* Treat any non-zero exit or import failure as a tooling failure, not a test failure, and MUST NOT proceed to project tests when this check fails.  
* Verify primary CLI/tool dependencies by running command \-v hdctl and command \-v jq (or equivalent checks for the canonical CLI binary and JSON tool) and requiring success for each.  
* Treat missing CLI or missing jq as a tooling failure.  
* Write a QA tooling bootstrap log by emitting a structured log under an audit/qa/\*\* prefix that records, at minimum:  
  * the commands executed (python \-m pytest \--version, command \-v hdctl, command \-v jq)  
  * their exit codes  
  * a top-level classification field (for example, tooling\_failure: true/false or an equivalent status enum)  
* When any bootstrap check fails, the log MUST mark the run as a tooling failure and identify which check failed; QA plans and tokens may then treat this as a tooling/infra blocker, not as an epic behavior failure.

Mechanics does not pin the exact file name or JSON schema for the bootstrap log; those live in Glow QA Guide and HDE-Schemas & Artifacts by title. This non-pinning applies only to the bootstrap log’s exact naming and schema, not to the existence of concrete QA run artifacts: the QA tooling bootstrap harness and Live QA harness ecosystem MUST still produce governed, non-empty evidence under audit/qa/\*\* suitable for use by the QA plans, manifests, and viability checks routed by title to the QA and schemas documents.

Preferred pytest invocation (Codespaces and similar dev environments): In environments like shared dev containers or Codespaces, Mechanics requires:

* Normative tests and QA flows MUST invoke pytest as python \-m pytest \<PYTEST\_ARGS\>, using the same Python interpreter that runs the Engine.  
* QA plans and CI jobs SHOULD standardize on python \-m pytest for all test steps rather than calling pytest via a venv shim, to avoid “broken shim” failures where .venv/bin/pytest exists but is not executable.  
* Any failure of python \-m pytest \--version in the bootstrap harness MUST be recorded and classified as a tooling failure in the bootstrap log; epic acceptance and behavior tokens MUST NOT be marked failed solely because pytest is missing or misconfigured.

Pytest mark registry (normative). Any pytest mark used by governed test suites MUST be registered in the repo’s pytest mark registry (implementation-defined) to avoid mark warnings in strict CI postures.

### **1.6.2 Live QA harness (commands, classification, and logs)**

Purpose (normative): Provide a reusable Live QA harness that runs CLI and other Engine-facing commands for QA (including PO-run Live QA sessions) in a way that is deterministic, copy/paste-ready, and distinguishable between tooling failures and behavior failures.

Behavior (minimum): The Live QA harness MUST satisfy the requirements below.

Depend on a successful bootstrap:

* Check the QA tooling bootstrap harness result before executing Engine tests or CLI commands.  
* If the most recent bootstrap log reports a tooling failure, the Live QA harness MUST NOT proceed to run tests or Engine commands and MUST surface that condition as a tooling problem (for example, via a tooling\_failure: true or equivalent marker in its own logs).

Per-step dependency posture (normative):

* Every QA step that depends on an executable dependency (for example, `python`, `pytest`, `jq`, `curl`, an importable module, a virtual environment, or a repo-provided helper) MUST declare the dependency set required by that step.  
* Every such step MUST include an explicit preflight check that proves each dependency is present and runnable before the main behavior command runs.  
* When the execution venue allows activation or installation remediation, the step MUST include the exact activation or installation action to take if the dependency preflight fails.  
* When activation or installation remediation is not allowed or cannot be truthfully specified, the step MUST say so explicitly and MUST classify the step as tooling-blocked if readiness cannot be established.  
* A QA step is non-conforming if it assumes dependency availability without checking it.

Bootstrap dependency semantics (normative):

* A shared bootstrap step MAY satisfy the first dependency pass for later checks, but it does not remove per-step responsibility.  
* Each later QA step MUST either include its own dependency preflight and activation or install-remediation logic inline, or explicitly depend on the bootstrap artifact and rerun a short step-local readiness check before the main command.  
* Behavior verdicts MUST NOT be issued before dependency readiness is established. If preflight fails and remediation does not resolve the issue, the step MUST be classified as `FAIL_TOOLING` or `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`.

Governed evidence capture (normative):

* The dependency preflight result, any activation or installation action taken, and the final ready or not-ready disposition MUST be captured in the step’s governed QA evidence stream.  
* QA plans and step artifacts that omit dependency preflight and activation or install-remediation posture for a required dependency are mechanics-nonconforming and not approval-ready.

Provide copy/paste-ready commands (no hand-editing):

* All PO-facing QA commands exposed by the harness MUST be fully concrete and copy/paste-ready (no \<PO: FILL\_ME\> placeholders).  
* When commands require values that are present in tests or configs (for example, fixed VIEWER\_IDs, seeds, or candidate payloads), the harness MUST discover or construct those values programmatically by mirroring test semantics (for example, calling the same helpers that write candidate payloads) instead of asking the PO to hand-edit commands.

No VCS workflow content; optional non-gating repo-root sanity checks allowed (normative):

* Live QA runbooks and harness steps MUST NOT instruct or discuss branches, commits, PRs, or any other VCS workflow steps. VCS workflow is handled manually by the PO.  
* Live QA PASS/FAIL MUST NOT be gated on VCS state (for example: “working tree clean,” “on correct branch,” “commit matches expected,” or any similar VCS-derived condition).  
* Limited git commands are allowed only as optional non-gating sanity checks, and only if all are true:  
  * Read-only and non-mutating (no checkout/reset/commit/push/pull).  
  * Do not print or rely on branch names, commit SHAs, or PR identifiers.  
  * Used only to confirm “this is a repo” / “repo root exists” (sanity), never as evidence or acceptance criteria  
* If the sanity check fails, the check outcome is TOOLING\_BLOCKED (tooling), not FAIL\_BEHAVIOR (behavior).  
* If git information is captured at all, it is traceability-only and MUST NOT block execution.  
* Known Codespaces packaging artifacts (including glow\_hdengine.egg-info/PKG-INFO and the containing glow\_hdengine.egg-info/ directory) are explicitly non-blocking and MUST NOT be deleted, restored, or used as a QA gating signal.  
* The only write-scope rail for Live QA evidence remains: audit/qa/.

Reuse test semantics directly instead of scraping:

* When tests construct data dynamically (for example, writing candidates to a temporary file and passing that path into a CLI command), the Live QA harness MUST mirror the same construction logic directly (for example, by writing the same payload under an audit/qa/\*\* path) rather than attempting to scrape arguments out of test source files.  
* For CLI QA flows, this means the harness should call the same underlying functions or fixtures that tests use to prepare inputs, so that QA inputs are deterministic and aligned with test coverage.

Capture exit codes, sizes, and stderr for QA artifacts:

* For each QA artifact that is expected to be non-empty (for example, JSON outputs, sorted candidate listings, or other CLI outputs under audit/qa/\*\*), the harness MUST:  
  * record the generating command and its exit code  
  * record the artifact’s size (for example, via wc \-c or an equivalent size measurement)  
  * capture any stderr emitted by the command in a corresponding QA log entry  
* If such an artifact is zero bytes, the harness MUST treat this as a failure signal (tooling or behavior) and record it explicitly; an empty artifact MUST NOT be left ambiguous.

Classify failures as tooling vs behavior:

* For each QA run, the Live QA harness MUST classify the outcome as either:  
  * a tooling failure (for example, missing pytest, broken CLI entrypoint, environment not bootstrapped), or  
  * a behavior failure (tests assertions failing, CLI returning incorrect JSON or exit codes)  
* This classification MUST be visible in the QA logs written under audit/qa/\*\* (for example, through a status field or tooling\_failure: true/false), so that Governance/QA documents and tokens can distinguish infra/tooling problems from Engine behavior problems.

Moon Loop (minimal in-session remediation to unblock Live QA; normative; bounded):

* If a Live QA step fails because a QA-created evidence harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defect under the approved QA root blocks an otherwise observable proof target, an in-session Moon Loop is permitted to restore canon-aligned QA evidence capture and re-run the step to produce the canonical evidence surface.  
* Allowed actions in the Moon Loop are strictly limited to:  
  * creating ephemeral helper code under `/tmp` to compute or verify an already-canonized artifact surface  
  * adjusting a QA check or QA harness procedure under the approved QA root to validate the canonical emitted surface already owned by canon  
  * repairing QA-created evidence harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under the approved QA root  
  * recording bounded deviation evidence that preserves the same proof target, check ID, rails posture, evidence paths, and tokenless posture  
* A change to product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction.  
* Non-QA-root remediation MUST be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE, as applicable to the affected surface, before the final PASS-grade QA receipt relies on that remediation.  
* When final PASS proof relies on non-QA-root evidence refresh, the final receipt MUST cite the routing receipt before post-refresh gate checks and MUST preserve the failed pre-routing receipt as context. A step-log manifest or coverage artifact MUST represent original planned receipts and accepted remediation receipts separately rather than overwriting failed original receipts.  
* If a Live QA check fails because a governed repo artifact lacks a required structural field, the check MUST NOT be satisfied by raw string-presence wording alone. The governing QA plan or remediation guide should define the structural predicate that proves the field is present and semantically tied to the intended source.  
* If a Live QA check fails because a QA evidence harness uses brittle case-sensitive prose matching against a governed artifact while the raw artifact preserves the intended semantic boundary, the remediation MAY normalize the semantic phrase check inside the QA root only. The remediation MUST preserve the original proof target, evidence paths, check ID, rails posture, tokenless posture, and failing receipt context.  
* If an initial failing artifact is overwritten or unavailable by the time remediation begins, the remediation record MUST state that the initial failure artifact is unavailable. It MUST NOT reconstruct missing logs, hashes, timestamps, or result bodies.  
* Evidence posture (minimum):  
  * The failing check’s primary.log MUST include a clear failure signature excerpt when that failing artifact remains available.  
  * A one-line remediation note MUST be recorded in the same log, remediation note, or session transcript, naming the changed file path(s) and the reason for the change.  
  * The rerun output showing the restored PASS MUST be captured in the log.  
  * If any QA-root files were changed, capture a minimal delta under the approved QA evidence root with changed file paths and final-content sha256 values.  
* Stop condition: if unblocking requires product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, multiple implementation subsystems, unclear root cause, or expanded scope, stop the Moon Loop and route to normal remediation planning.  
* Moon Loop changes do not change token semantics, acceptance rules, or plan approval structure; they only allow minimal QA evidence remediation to produce the governed evidence surface.

QA-created Step 0 harness scaffolding (mechanics-only; bounded). A Live QA run MAY create QA-only harness scaffolding during Step 0 when the scaffolding is limited to QA evidence capture and does not create or alter product behavior. Absence of prior repo-existence proof for that scaffolding is not a PF14 mechanics defect when the plan explicitly creates it during the QA run and the created harness remains QA-only. The created harness MUST still be executable, safe, phase-bounded, target-correct, able to emit a verdict, and able to produce or point to required governed evidence under the QA evidence root. A QA-created harness is mechanics-nonconforming if it cannot be created, performs unsafe or out-of-scope work, changes implementation behavior, proves the wrong target, cannot emit a verdict, or cannot produce or point to required governed evidence.

Mechanics does not define the token names or acceptance rules associated with these logs; those remain single-homed in Glow QA Guide, HDE-Build Checklist, HDE Phased Epics, and Glow Infrastructure by title. This section requires that the QA bootstrap harness and Live QA harness exist as concrete components, that they enforce the behaviors listed above, and that their logs live under governed audit locations and are suitable for use by those documents.

Routing (titles-only):

* QA plans, acceptance tokens, and epic-specific QA steps: Glow QA Guide, HDE-Build Checklist, HDE Phased Epics.  
* Codespaces QA configuration and requirements (single home): Glow QA Guide (titles-only).  
* Services and base URL inventory: Glow Infrastructure (titles-only).  
* Codespaces operational reference: GitHub Codespaces in a QA Workflow (reference only; requirements remain single-homed in Glow QA Guide).  
* Schemas and canonical JSON rules for QA logs (when governed): HDE-Schemas & Artifacts.

Mechanics records the existence and behavior of the QA tooling bootstrap and Live QA harness here so that they are treated as first-class components of the HD Engine’s tooling skeleton, on par with the sanity pipeline, env-pins checks, and evidence tools.

### **1.6.3 Generic epic QA harness entrypoint (per-check primary logs, manifest, viability)**

Purpose (normative): Provide a single reusable epic QA harness entrypoint that can be invoked for any epic to execute a Live QA run under pinned rails and to reliably produce governed QA evidence under audit/qa/\*\* without relying on hand-edited commands or ad-hoc shell state.

This component exists because “a harness that exits 0 but produces no run artifacts” is mechanically useless and must be prevented by construction.

Behavior (minimum, normative): The epic QA harness entrypoint MUST:

* Determine an epic id (names-only) by accepting an epic identifier via a documented interface (CLI args or environment override).

* Create or reuse the canonical epic QA root by creating or reusing the governed epic QA root directory of the form `audit/qa/hde-epic<NNN>/`.

* Use the canonical epic QA root (normative): `hde-epic<NNN>` where `<NNN>` is a zero-padded 3-digit epic number (example: `hde-epic022`), and epic QA root directories MUST be lower-case ASCII.

* Enforce no parallel spellings: implementations MUST NOT introduce alternate epic directory spellings for the same epic (examples: audit/QA/, audit/qa/HDE-EPIC022/, audit/qa/EPIC022/). Legacy paths may exist; do not create new ones.

KISS evidence posture for Live QA (no per-run history constructs):

* Within an epic, check IDs are the stable handle. There is no additional “run identity” dimension in mechanics.  
* A per-epic “step logs manifest” (see §1.6.3) MAY be emitted to map check IDs to the current canonical log filenames. This is a convenience index for reviewers; it is not required for correctness and MUST be current-state only, not per-run history.

* run\_id is prohibited: Live QA plans and artifacts MUST NOT introduce or require run\_id (or RUN\_ID) as an operator input, step-log header field, manifest field, or correctness key.  
* History retention MUST NOT become a correctness dimension. Any optional per-execution history nesting must remain non-canonical and non-gating; acceptance binds only to canonical check-centric evidence surfaces.

**Template semantics for future-step evidence references (NOT RUN / DEFERRED):**

* Any plan template that enumerates step-scoped evidence paths MUST explicitly label future-step artifacts as NOT RUN (or DEFERRED) until the producing step has executed.

* Templates and closure/rollup artifacts MUST separate these states:

  * Present: the artifact exists and is referenced by path.

  * Missing evidence: the producing step executed, but the required artifact is absent or unproven.

  * NOT RUN / DEFERRED: the producing step has not executed yet (so the artifact is not expected to exist yet).

NOT RUN / DEFERRED MUST NOT be treated as missing evidence, and MUST NOT block closure until the producing step has actually executed. Forward references for NOT RUN / DEFERRED steps are informational only and MUST NOT be placed in any required-artifacts list or missing-evidence list.

* If forward references are included, they MUST be grouped under a clearly labeled section such as “Deferred checks” or “Expected in future run” and MUST be explicitly excluded from any “missing evidence” counts.

EPIC024 fixed paths (normative):

* audit/qa/hde-epic024/qa\_step\_logs\_manifest.json

* audit/qa/hde-epic024/qa\_step\_logs\_manifest.json.path\_proof.txt

EPIC024 refresh/check entrypoint (records-only):

* `python tools/evidence/refresh_step_logs_manifest.py --check`

EPIC025 fixed check-log paths (records-only):

* `audit/qa/hde-epic025/checks/gate_evidence_index_update/primary.log`

* `audit/qa/hde-epic025/checks/gate_mirror_schema/primary.log`

* `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`

* `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log`

* `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log`

* `audit/qa/hde-epic025/checks/preflight_p4_evidence_endpoints/primary.log`

* `audit/qa/hde-epic025/checks/preflight_e1_http_compat/primary.log`

* `audit/qa/hde-epic025/checks/preflight_e3_cli_entrypoint/primary.log`

* `audit/qa/hde-epic025/checks/preflight_e5_a7_transport_invariants/primary.log`

* `audit/qa/hde-epic025/checks/preflight_e6_evidence_index_mirror/primary.log`

Nothing else is mechanically required unless canon explicitly pins an additional governed evidence family/path (titles-only; owned elsewhere).

EPIC025 additional Live QA evidence paths observed (records-only; plan-defined):

* checks/d0\_discovery:

  * `audit/qa/hde-epic025/checks/d0_discovery/primary.log`

* checks/po-008:

  * `audit/qa/hde-epic025/checks/po-008/primary.log`

  * `audit/qa/hde-epic025/checks/po-008/success_head.txt`

  * `audit/qa/hde-epic025/checks/po-008/success_head.txt.sha256`

  * `audit/qa/hde-epic025/checks/po-008/success_get.txt`

  * `audit/qa/hde-epic025/checks/po-008/success_get.txt.sha256`

* checks/po-009:

  * `audit/qa/hde-epic025/checks/po-009/primary.log`

  * `audit/qa/hde-epic025/checks/po-009/canonical_json_gate_stdout.txt`

  * `audit/qa/hde-epic025/checks/po-009/canonical_json_gate_stdout.txt.sha256`

* checks/po-010:

  * `audit/qa/hde-epic025/checks/po-010/primary.log`

  * `audit/qa/hde-epic025/checks/po-010/env_pins.log`

  * `audit/qa/hde-epic025/checks/po-010/env_pins.log.sha256`

  * `audit/qa/hde-epic025/checks/po-010/env_pins_check_stdout.txt`

  * `audit/qa/hde-epic025/checks/po-010/env_pins_check_stdout.txt.sha256`

  * `audit/qa/hde-epic025/checks/po-010/sanity_pipeline_stdout.txt`

  * `audit/qa/hde-epic025/checks/po-010/sanity_pipeline_stdout.txt.sha256`

* checks/po-011:

  * `audit/qa/hde-epic025/checks/po-011/primary.log`

  * `audit/qa/hde-epic025/epic_closure_record.md`

  * `audit/qa/hde-epic025/epic_closure_record.md.sha256`

* checks/po-012:

  * `audit/qa/hde-epic025/checks/po-012/primary.log`

  * `audit/qa/hde-epic025/checks/po-012/endpoints_catalog.json`

  * `audit/qa/hde-epic025/checks/po-012/endpoints_catalog.json.sha256`

  * `audit/qa/hde-epic025/checks/po-012/index.sha256`

  * `audit/qa/hde-epic025/checks/po-012/index.sha256.sha256`

* checks/po-013:

  * `audit/qa/hde-epic025/checks/po-013/primary.log`

  * `audit/qa/hde-epic025/00_meta/deferred_scope_posture.md`

  * `audit/qa/hde-epic025/checks/po-013/deferred_scope_posture.md.sha256` (hash line targets `audit/qa/hde-epic025/00_meta/deferred_scope_posture.md`)

* checks/po-014 (referenced as deferred; expected path only until executed):

  * `audit/qa/hde-epic025/checks/po-014/primary.log`

EPIC026 early Live QA evidence paths observed (records-only):

* checks/po-000:

  * `audit/qa/hde-epic026/checks/po-000/primary.log`

  * `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

  * `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json.path_proof.txt`

  * `audit/qa/hde-epic026/checks/po-000/doc_deltas.md`

  * `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`

* checks/po-001:

  * `audit/qa/hde-epic026/checks/po-001/primary.log`

  * `audit/qa/hde-epic026/checks/po-001/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-001/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-001/pytest_rc.txt`

* checks/po-002:

  * `audit/qa/hde-epic026/checks/po-002/primary.log`

  * `audit/qa/hde-epic026/checks/po-002/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-002/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-002/pytest_rc.txt`

  * `audit/qa/hde-epic026/checks/po-002/catalog_api_compat_entry.json`

* checks/po-003:

  * `audit/qa/hde-epic026/checks/po-003/primary.log`

  * `audit/qa/hde-epic026/checks/po-003/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-003/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-003/pytest_rc.txt`

* checks/po-004:

  * `audit/qa/hde-epic026/checks/po-004/primary.log`

  * `audit/qa/hde-epic026/checks/po-004/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-004/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-004/pytest_rc.txt`  
* `checks/po-005:`  
  * `audit/qa/hde-epic026/checks/po-005/primary.log`

  * `audit/qa/hde-epic026/checks/po-005/route_proof.txt`

  * `audit/qa/hde-epic026/checks/po-005/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-005/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-005/pytest_rc.txt`  
* `checks/po-006:`  
  * `audit/qa/hde-epic026/checks/po-006/primary.log`

  * `audit/qa/hde-epic026/checks/po-006/route_proof.txt`

  * `audit/qa/hde-epic026/checks/po-006/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-006/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-006/pytest_rc.txt`  
* `checks/po-007:`  
  * `audit/qa/hde-epic026/checks/po-007/primary.log`

  * `audit/qa/hde-epic026/checks/po-007/catalog_extract_dev_endpoints.json`

  * `audit/qa/hde-epic026/checks/po-007/catalog_sha256_check.txt`

  * `audit/qa/hde-epic026/checks/po-007/pytest_stdout.log`

  * `audit/qa/hde-epic026/checks/po-007/pytest_stderr.log`

  * `audit/qa/hde-epic026/checks/po-007/pytest_rc.txt`  
* `checks/po-008:`  
  * `audit/qa/hde-epic026/checks/po-008/primary.log`

  * `audit/qa/hde-epic026/checks/po-008/cli_help.txt`

  * `audit/qa/hde-epic026/checks/po-008/showcompat_help.txt`

  * `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stdout.log`

  * `audit/qa/hde-epic026/checks/po-008/reject_nonjson_stderr.log`

  * `audit/qa/hde-epic026/checks/po-008/reject_nonjson_rc.txt`

  * `Conditional when valid USER_A_ID and USER_B_ID inputs are supplied for the step:`  
    * `audit/qa/hde-epic026/checks/po-008/concat_output.json`

    * `audit/qa/hde-epic026/checks/po-008/concat_output_order_check.txt`  
* `checks/po-009 (blocked input-availability family):`  
  * `audit/qa/hde-epic026/checks/po-009/primary.log`

  * `audit/qa/hde-epic026/checks/po-009/open_rails_note.txt`  
  * `checks/po-009 (rails verification family):`  
    * `audit/qa/hde-epic026/checks/po-009/primary.log`

    * `audit/qa/hde-epic026/checks/po-009/open_rails_ab_rc.txt`

    * `audit/qa/hde-epic026/checks/po-009/open_rails_ba_rc.txt`

    * `audit/qa/hde-epic026/checks/po-009/closed_rails_classification.txt`

    * `audit/qa/hde-epic026/checks/po-009/open_rails_ab_canonical_json_check.txt`

    * `audit/qa/hde-epic026/checks/po-009/open_rails_ba_canonical_json_check.txt`

    * `audit/qa/hde-epic026/checks/po-009/abba_identity_check.txt`

    * `Conditional-only when the open-rails lane cannot run due to provider or gate:`  
      * `audit/qa/hde-epic026/checks/po-009/open_rails_note.txt`

  * `audit/qa/hde-epic026/checks/po-009/po-009_input_constraint.log`

EPIC026 later Live QA evidence paths observed (records-only):

* `checks/po-010:`

  * `audit/qa/hde-epic026/checks/po-010/primary.log`

  * `audit/qa/hde-epic026/checks/po-010/showcompat_help.txt`

  * `audit/qa/hde-epic026/checks/po-010/catalog_extract_dev_endpoints.json`

  * `audit/qa/hde-epic026/checks/po-010/po-010_manifest.json`

* `checks/po-011:`

  * `audit/qa/hde-epic026/checks/po-011/primary.log`

  * `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stdout.log`

  * `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_stderr.log`

  * `audit/qa/hde-epic026/checks/po-011/canonical_json_gate_rc.txt`

  * `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stdout.log`

  * `audit/qa/hde-epic026/checks/po-011/update_evidence_index_stderr.log`

  * `audit/qa/hde-epic026/checks/po-011/update_evidence_index_rc.txt`

EPIC026 step-scope and non-canonical-path posture (normative for the observed families above):

* For the Step-0 family above, the check-scoped manifest pair under `audit/qa/hde-epic026/checks/po-000/` is the plan-required step artifact pair.

* This does not replace any separately governed per-epic or close-pack manifest surface recorded elsewhere in this guide.

* If a legacy root-level pair also exists under `audit/qa/hde-epic026/qa_step_logs_manifest.json` and `audit/qa/hde-epic026/qa_step_logs_manifest.json.path_proof.txt`, treat that pair as legacy traceability for the Step-0 family unless the owning QA canon explicitly binds it as the authoritative surface for the step in question.

* Earlier-attempt or appendix artifacts under `artifacts/hde-epic026/checks/**` are non-canonical for these Live QA step families and MUST NOT replace the canonical audit/qa paths above.

EPIC027 early Live QA evidence paths observed (records-only):

* checks/po-001:

  * `audit/qa/hde-epic027/checks/po-001/primary.log`

  * `audit/qa/hde-epic027/checks/po-001/route_inventory.txt`

  * `audit/qa/hde-epic027/checks/po-001/dev_conjunction_http.txt`

  * `audit/qa/hde-epic027/checks/po-001/endpoint_catalog.txt`

* checks/po-002:

  * `audit/qa/hde-epic027/checks/po-002/primary.log`

  * `audit/qa/hde-epic027/checks/po-002/compat_surface.txt`

  * `audit/qa/hde-epic027/checks/po-002/compat_identity_discovery.txt`

* checks/po-003:

  * `audit/qa/hde-epic027/checks/po-003/primary.log`

  * `audit/qa/hde-epic027/checks/po-003/cli_emitter_proof.txt`

  * `audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt`

  * `audit/qa/hde-epic027/checks/po-003/showcompat_help.txt`

Shared per-epic current-state manifest pair refreshed by po-001 to po-003:

* `audit/qa/hde-epic027/qa_step_logs_manifest.json`

* `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`

Maintain per-epic step logs manifest (current-state):

* The harness MUST update the per-epic step logs manifest so that it provides a mapping from check\_id to (at minimum) status and log\_path, and MUST enforce uniqueness of check\_id.

* The manifest MUST point to the check’s primary.log path under audit/qa/hde-epic\<NNN\>/checks/\<check\_id\>/.

* The manifest MUST be idempotent per check\_id (no duplicates). On rerun, the harness MUST replace the prior record for that check id so the manifest reflects the latest status and log\_path.

Emit per-check primary logs:

* For each check/step executed by the harness, ensure the check directory exists at audit/qa/hde-epic\<NNN\>/checks/\<check\_id\>/ and write the check’s primary log to primary.log in that directory.

Each primary log MUST:

* Be non-empty.  
* Begin with a JSON header object whose fields follow the Plan Templates Live QA step-log header schema (titles-only), with this gating posture:  
  * Required header fields (hard): check\_id, status, command, captured\_env, artifacts  
  * Artifacts list invariant (hard): artifacts MUST be a JSON array of step-directory relative filenames, MUST include primary.log, and MUST NOT list files that are absent in the step directory.  
  * Defaultable header fields (non-blocking): pf\_refs, intended\_tokens, claimed\_tokens  
  * If any of these three fields are missing, they MUST be interpreted as empty lists for review purposes: \[\].  
  * A QA reviewer-of-record MAY mechanically normalize a non-conforming header by inserting missing defaultable fields and re-serializing the header as canonical JSON (evidence-format repair only; no rerun required). If artifacts is missing, normalization MAY insert an artifacts list containing at minimum primary.log, plus any other step-directory files that are present and unambiguously part of the check output.  
  * Token claims are never inferred: if claimed\_tokens is missing or empty, treat claims as none; reviewers MUST NOT infer token claims from transcript text, other artifacts, or filenames.  
  * Header rebuild may occur as evidence-format repair (including Moon Loop deviations). If a primary.log header is rebuilt by prepending a corrected JSON header line, the resulting file MAY contain more than one JSON header line.  
  * Downstream parsers and reviewers MUST treat only the first line of primary.log as the governed header and MUST NOT assume that the file contains a single header line.  
* Require captured\_env to include a rails snapshot (at minimum SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, APP\_ENV).  
* Enforce status vocabulary as gating (names-only): PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, PARKED.  
* Prohibit ad-hoc statuses for core execution state; if status is outside this set, normalization MAY set it only when the transcript unambiguously indicates the correct status (for example, contains a single definitive PASS: line and no FAIL\_ lines). Otherwise status remains Unclear and the step is not acceptable.  
* Require that if token names appear, they are names-only and not invented or aliased (token registry is single-homed in HDE-Governance by title), and claimed\_tokens (if present) MUST be empty unless status=PASS.  
* Allow additional header fields beyond this minimum, but they MUST NOT be required as a plan-approval condition unless Plan Templates is updated to require them.  
* Header-writer input discipline (normative). If the harness uses a step-log header writer that reads per-check metadata from env vars, the harness MUST export the complete required set immediately before header generation for each check and MUST NOT rely on prior step state. Minimum per-check exports (names must match the header writer contract): CHECK\_ID, CHECK\_NAME, PASS\_FAIL, COMMANDS\_JSON, ARTIFACTS\_JSON, PF\_REFS\_JSON.  
* Moon Loop header regeneration (evidence-format repair only). If the JSON header is missing or contains incorrect per-check metadata due to missing exports, a reviewer-of-record MAY export the required env vars and regenerate the header, then reassemble primary.log by writing the corrected JSON header as the first line and appending the existing body transcript verbatim. This MUST NOT change the executed commands and MUST NOT rerun the check.  
* Include the commands executed (copy/paste-ready; no placeholders).  
* When a command depends on a repo-provided entrypoint (script/module/CLI), include a preflight existence check transcript proving the entrypoint is present and runnable before execution. If the preflight fails, set status=TOOLING\_BLOCKED, capture the transcript, and MUST NOT attempt the failing command.  
* Capture exit codes.  
* End with an explicit step outcome classification (tooling vs behavior).

Rerun posture (normative; current-state):

* If a check id is executed more than once (a rerun), treat checks/\<check\_id\>/primary.log as the current-state primary artifact and MAY overwrite it on rerun.  
* If the harness also preserves prior attempts for traceability (for example, attempt2.log), those artifacts MUST NOT be treated as required outputs and MUST NOT be used as plan gating surfaces.  
* After a rerun, the step logs manifest MUST reflect the latest status and primary log path for that check id.

Non-canonical env pins in logs (normative): Step logs MAY record additional env fields for traceability, but only the canonical determinism pins defined in §1.2 are required for governed bytes and governed evidence. PYTHONHASHSEED MUST NOT be treated as a required pin; if present, it is diagnostic-only.

Optional generated artifacts (only when canonized by the owning docs): Mechanics does not require run-scoped event logs, per-run folders, or history-retention outputs. If a specific epic’s QA plan (single-homed by title) requires generated artifacts such as summaries or notes, the harness MUST generate them mechanically from command outputs and captured logs (no manual editing) and MUST place them under audit/qa/\*\* using governed paths/schemas owned by the relevant PF documents (titles-only).

No manual-fill placeholders (hard rule): Any placeholder fields such as “(fill PASS/FAIL)” or “fill manually” are forbidden in generated evidence artifacts. Generated artifacts MUST be complete at write time.

Generated-artifact header (required): Each generated summary/notes artifact MUST begin with a clear header such as: AUTO-GENERATED. DO NOT EDIT. Re-run the harness/generator to update.

Fail closed on missing outputs: If the harness completes without producing at least one non-empty per-check primary.log under audit/qa/hde-epic/checks/ or without updating the per-epic step logs manifest, it MUST exit non-zero and record the reason as a tooling/harness failure.

Be reusable across epics: Epic-specific harness entrypoints may exist as thin wrappers for convenience, but they MUST delegate to the generic harness entrypoint and must not re-implement logging, QA\_ROOT layout, or manifest updates in bespoke per-epic code.

CI self-test (normative): The repo MUST include a CI test that executes the epic QA harness entrypoint under closed rails and asserts, at minimum:

* the epic QA root exists under audit/qa/hde-epic/  
* at least one check primary log exists at audit/qa/hde-epic/checks/\<check\_id\>/primary.log and is non-empty  
* the per-epic step logs manifest exists under audit/qa/hde-epic/ and contains current-state entries that point to the primary log path(s)  
* the epic-scoped close-pack and acceptance scaffold artifacts (when required by the invoked harness mode) exist at their canonical paths (see §37.2) and are minimally parseable (CI-safe structural checks only; token semantics are owned elsewhere)

Codespaces snapshot artifacts are optional and non-gating. CI self-tests MUST NOT require, validate, or gate on any Step-0A “Codespaces snapshot” file.

This self-test is required to prevent regressions where the harness exits successfully but produces no governed evidence.

Routing (titles-only):

* Live QA plan template structure and the minimum step-log header schema \+ status vocabulary: Plan Templates.  
* QA plan step sequences, deliverables, and token semantics: Glow QA Guide, HDE-Build Checklist, HDE Phased Epics.  
* QA\_ROOT naming conventions and any governed schemas for QA artifacts: HDE-Schemas & Artifacts.  
* Codespaces QA configuration and requirements: Glow QA Guide.  
* Services and base URL inventory for targets reached from Codespaces: Glow Infrastructure.

# 2\) Canonical Enumerations Registry

Purpose. Wire and prove the frozen domain registries (centers, gates, channels, categories) used by the engine. Mechanics validates and snapshots the domains; HDE-Schemas and Artifacts is the single home for authoritative catalogs and schemas. Developer notes in this repo are informative only (never authoritative).

## **2.1 Domain invariants (normative)**

Centers: closed set; snake\_case identifiers; ASCII; unique.

Gates: closed domain; numeric identity per schema; unique; each attached to a single center by catalog.

Channels: closed set of edges; canonical NN-NN (zero-padded, min-first, ASCII hyphen); ASCII-sorted; unique; no multi-hop encodings.

Categories (Magic-10): closed ID set with pinned order (HDE-Schemas and Artifacts §2.6).

Set semantics: arrays that represent sets MUST be deduped and ASCII-sorted before hashing/compare (HDE-Schemas and Artifacts §4).

Validation posture: unknown IDs, duplicates, non-canonical channel forms, or schema mismatches hard-fail with typed errors.

## **2.2 Validation & generation (mechanics)**

Mechanics provides a single registry job that:

* Load & validate each domain against its HDE-Schemas and Artifacts JSON-Schema (titles-only)

* Normalize channels to NN-NN min-first and enforce ASCII sort \+ dedupe for set-arrays

* Prove closure & uniqueness (no extras/omissions, no duplicates, no cross-catalog drift)

* Emit a registry snapshot (records-only metadata: domain name, item counts, canonical sha256/size of each governed artifact) and index it in the machine mirror at artifacts/evidence\_index.jsonl

* Update the human Evidence Index (Appendix D) in the same change; CI enforces human↔machine 1:1 parity and path-proofs (discovered\_physical\_path \+ proof\_anchor)

* Pins (determinism). All checks run with LC\_ALL=C, LANG=C, TZ=UTC; JSON is canonical (UTF-8 no BOM, sorted keys, compact, one LF)

* Seeds (catalogized; admin/test). If Seeds are present in HDE-Schemas and Artifacts, they are admin/test-only and treated as frozen inputs; any change bumps release\_id (HDE-Schemas and Artifacts §6; HDE-Math-Spec §5.1.1). Seeds are not public in Reader v1.

## **2.3 Artifacts (records-only; path-agnostic; indexed via the machine mirror)**

List by title/path in Appendix D and mirror 1:1 in artifacts/evidence\_index.jsonl (each record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor; one LF; canonical JSON).

domain\_snapshot — counts & identities (sha256/size) for centers/gates/channels/categories.

closure\_report — proofs of domain closure & uniqueness; channel-normalization reject corpus (non-canonical inputs → errors).

registry\_checksums — summarized checksums for governed artifacts (for quick diffing).

## **2.4 Acceptance (tokens; titles-only)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names.

The mechanics obligations in §2 require that acceptance proofs exist for:

* closed-domain validation (centers/gates/channels/categories)

* canonical channel orientation and set-order discipline

* release identity coupling for any seed-bearing inputs

* evidence/index discipline for the registry snapshots and reports produced by this section

# 3\) Programmatic Configuration System

Purpose (normative). Provide a typed, deterministic configuration surface for the engine and its clients. The system loads governed catalogs, validates & normalizes them, fails on unknown/duplicate IDs, and emits typed artifacts for FE/BE alongside a registry report. Concrete file names and directories are implementation-defined and not pinned here.

Single homes (titles-only):

* Domains/schemas & canonical JSON rules: PF-Canon-HDE-Schemas & Artifacts (§2, §4, §8)

* Math semantics (constants, ordering/banding): PF-Canon-HDE-Math-Spec

* Governance (evidence policy & tokens): PF-Canon-HDE-Governance

## **3.1 Loader behavior (normative)**

Unknown/duplicate IDs → fail build. The loader MUST hard-fail (typed error) on any unknown identifier, duplicate entry, schema mismatch, or non-canonical channel form.

Alias policy \= OFF (default). No implicit aliases. If an allow-list is explicitly enabled, only declared aliases are recognized; all others fail.

Normalization. Channel IDs normalize to zero-padded NN–NN (min-first); arrays that represent sets are deduped & ASCII-sorted before hashing/compare.

Determinism. Output is order-neutral (AB↔BA), locale-neutral (LC\_ALL=C), and two-run identical; canonical JSON is UTF-8 (no BOM), sorted keys, compact, exactly one LF (PF-12 §4).

Implementation note (informative). In the current Engine repo, the typed loader behavior described in this section is implemented by engine.config.registry\_loader.load\_registry\_config. This reference is non-normative; the canonical rules remain those in PF-Canon-HDE-Schemas & Artifacts and this section.

## **3.2 Typed artifacts (codegen) — outputs, not paths**

FE typed constants bundle. A generated artifact that exposes closed enums/domains and read-only constants needed by the FE client (e.g., category IDs, band labels), typed and immutable.

BE enums & constants bundle. A generated artifact that exposes the same frozen domains to backend code (enums, discriminated unions), typed and immutable.

(The exact filenames/locations are implementation-defined; Mechanics only requires that both bundles exist and are consistent, typed, and deterministic.)

## **3.3 Registry report (records-only; machine-readable)**

Purpose (normative). Emit a registry report that documents the effective configuration for this build: which catalogs and manifest were used, what domains and Magic-10 categories are present, and what alias policy is in effect. The report is names-only (no payload values) and is consumed by CI and auditors as a summary of the registry state.

Single home & schema. The registry report is a governed artifact at artifacts/registry/registry\_report.json (titles-only; path/scheme details live in HDE-Schemas and Artifacts §8.5).

The canonical schema and field shapes for registry\_report.v1 are defined in HDE-Schemas and Artifacts. Mechanics must not restate the full schema here.

At a high level, the report:

* declares a schema tag (for example "registry\_report.v1")

* records generated\_at\_utc

* describes upstream inputs (catalogs and manifest)

* summarizes registry state under artifacts.registry (channels, gates/centers, domains and counts, Magic-10, alias\_policy)

* includes optional notes for internal commentary

Programmatic generation & determinism.

The registry report MUST be generated programmatically by the Programmatic Configuration System:

* load and validate catalogs and manifest via the typed loader described in §3.1

* construct the report object in memory and emit it via the canonical serializer (see §4 / §10.1)

generated\_at\_utc SHOULD be stable across two runs in a determinism-pinned environment. Tools MUST either:

* reuse the existing generated\_at\_utc from a prior report when inputs have not changed

* use a pinned time source controlled by environment (for example, an epoch exposed via SOURCE\_DATE\_EPOCH or equivalent) so that two runs under the same conditions produce byte-identical JSON

Two-run identity MUST hold for the registry report: running the generator twice with identical inputs and environment yields byte-identical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

Implementation note (informative). For the current Engine, the registry report generator is implemented by tools/generate\_registry\_report.py, which loads catalogs and manifest via the typed loader in §3.1 and emits artifacts/registry/registry\_report.json through the canonical serializer. This reference is informative only; Mechanics remains implementation-agnostic and the governed rules are those in PF-Canon-HDE-Schemas & Artifacts and this section.

Alias policy summary.

The report MUST expose a names-only alias policy summary under artifacts.registry (see HDE-Schemas and Artifacts for exact shape):

* mode — "off" or "allow\_list" (or equivalent closed set)

* aliases — a mapping from alias IDs to canonical channel IDs when the allow-list is enabled

This summary reflects the loader’s alias behavior:

* aliases are OFF by default

* when an allow-list is configured, only declared aliases are present; all others fail closed (see §3.1)

Mechanics does not carry alias ledger content or catalog values; it only enforces that the alias policy exposed in the report matches the loader behavior.

Evidence & indexing (titles-only).

The registry report MUST be part of the evidence skeleton:

* A human Evidence Index entry is present in docs/evidence/INDEX.json (titles/paths only)

* A Machine Mirror record is present in artifacts/evidence\_index.jsonl with:

  * artifact\_key (for example "registry.registry\_report")

  * role:"snapshot"

  * discovered\_physical\_path:"artifacts/registry/registry\_report.json"

  * sha256

  * size\_bytes

  * produced\_at\_utc

  * proof\_anchor pointing to the corresponding path-proof transcript

Human Index, hash sentinel, mirror record, and path-proof for the report MUST be updated in the same PR as any change to the report; CI enforces human↔machine 1:1 parity, canonical JSONL, and path-proof presence (tokens routed by title to HDE-Governance and HDE-Schemas and Artifacts).

Routing (titles-only):

* Catalog/manifest schemas and the token→evidence matrix: HDE-Schemas and Artifacts

* Loader error envelope \+ canonical JSON serialization rules: HDE-Mechanics Guide

* Evidence skeleton tokens and CI posture: HDE-Governance, HDE-Build Checklist, and HDE-Phased Epics

## **3.4 Validation (binary)**

Schema & domain closure: all catalogs validate; no unknown/duplicate IDs; channels canonicalized; categories match the closed Magic-10 set.

Alias policy: OFF by default; if ON, only allow-listed aliases pass; all others fail.

Typed artifacts: FE and BE bundles are type-complete, immutable, and consistent across runs (two-run identity).

Determinism: re-running the loader yields identical bytes for codegen bundles and the registry report.

Evidence: human Index and PF-12 mirror contain synchronized records with path-proofs; canonical JSON lints pass (UTF-8/no BOM, sorted keys, one LF).

## **3.5 Acceptance (tokens; titles-only)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names.

The mechanics obligations in §3 require that acceptance proofs exist for:

* deterministic config generation (two-run identical governed config artifacts)

* canonical JSON discipline for all governed outputs

* evidence/index parity for generated reports and bundles

## **3.6 Routing (no duplication)**

Canonical rules & mirror schema: PF-Canon-HDE-Schemas & Artifacts.

Math semantics & constants: PF-Canon-HDE-Math-Spec.

Evidence policy & governance tokens: PF-Canon-HDE-Governance.

## **3.7 Config artifacts (Magic-10 and band edges)**

Purpose (normative). The Programmatic Configuration System must emit governed configuration artifacts for the Magic-10 category configuration and band thresholds, alongside the registry report. These artifacts are the canonical, deterministic configuration views used by the engine math and by QA; schemas and artifact keys remain single-homed in HDE-Schemas & Artifacts, and token semantics remain in HDE-Governance and the Glow QA Guide.

### **3.7.1 Generator posture (closed rails, canonical JSON)**

The configuration generator responsible for producing governed config artifacts MUST:

* Run under closed rails and determinism pins before writing any governed config artifact:

  * SAFE\_MODE \= 1

  * ALLOW\_NETWORK \= 0

  * LC\_ALL \= C

  * LANG \= C

  * TZ \= UTC

* Use the typed loader behavior defined in §3.1 to read catalogs, manifest, and any thresholds inputs.

* Emit all config artifacts via the Canonical Serialization Package (see §4 and §10.1):

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact separators

  * exactly one trailing line feed

  * arrays that represent sets deduped and ASCII-sorted before emission

* Two-run identity MUST hold for each governed config artifact: running the generator twice with identical inputs and environment yields byte-identical JSON.

Implementation note (informative). In the current engine repository, this behavior is implemented by a closed-rails generator script in tools/config/generate\_config\_artifacts.py and helper functions in tools/config/artifacts.py. These names are informative only; the normative rules remain those in this section and in HDE-Schemas & Artifacts.

### **3.7.2 Magic-10 config artifact**

The configuration system MUST materialize a governed Magic-10 configuration artifact whose schema and artifact\_key are owned by HDE-Schemas & Artifacts (for example, magic10\_config.v1 and config.magic10).

At a minimum, this artifact:

* Captures the Magic-10 category order exactly as used by the engine (closed set and pinned order).

* Records per-category configuration and bounds, including:

  * numeric caps for inputs and derived scores (integer bounds)

  * any additional per-category configuration metadata required by the engine math

* Records seed metadata for the Magic-10 configuration as a structured block, including at least:

  * template identifier (template\_id)

  * seed version (seed\_version)

  * updated\_at\_utc (UTC ISO time, semantics single-homed in HDE-Schemas & Artifacts and Glow QA Guide)

  * checksum\_sha256 over the underlying config source or thresholds used to derive this artifact

* Emits canonical, deterministic JSON governed by the rules in §3.7.1 and §4.

The Magic-10 config artifact is admin/test-only; the public Reader surface remains bands-only and numeric-free as described in the preamble and in HDE-CLI-API-Vendor-Ref.

### **3.7.3 Band-edges config artifact**

The configuration system MUST also materialize a governed band-edges configuration artifact whose schema and artifact\_key are owned by HDE-Schemas & Artifacts (for example, band\_edges.v1 and config.band\_edges).

At a minimum, this artifact:

* Captures band labels and numeric edges for the engine’s banding policy (such as inclusive-high thresholds).

* Records, in a names-only form, the clamp and rounding behavior used by the engine (for example, clamp bounds and the rounding mode consistent with round\_half\_up in HDE-Math-Spec).

* Carries a version tag and a structured pointer back to the thresholds input used to derive it (for example, a reference to the thresholds pack or math thresholds source discussed in §7.3 and in HDE-Schemas & Artifacts).

* Emits canonical JSON governed by §3.7.1 and §4, under the same two-run identity requirements as the registry report.

Band-edges configuration is admin/test-visible only; band mechanics and public band behavior remain specified in HDE-Math-Spec and in the Category Framework (§7).

### **3.7.4 Evidence and acceptance map (routing only)**

Governed config artifacts participate in the same evidence skeleton as other artifacts described in §1.3 and §25:

* Each config artifact (registry report, Magic-10 config, band-edges config) MUST appear in the human Evidence Index with a title and discovered path, and have a corresponding record in the machine mirror with sha256, size\_bytes, produced\_at\_utc, role, and proof\_anchor.

* Each config artifact MUST have a co-located path-proof transcript referenced by proof\_anchor; governed evidence tools described in §1.3.1 are the only writers for these path-proofs and the mirror.

* Mapping of PF09 tasks and QA tokens to config artifacts and tests lives in the config acceptance map and QA documents by title (HDE-Build Checklist, HDE-Schemas & Artifacts, Glow QA Guide, and HDE Phased Epics). PF14 records only that governed config artifacts exist, are generated under closed rails, are canonical and two-run identical, and are part of the evidence skeleton; it does not duplicate the acceptance map schema or token definitions.

## **3.8 Typed FE/BE config bundles (projections of governed config)**

Purpose (normative). The Programmatic Configuration System must expose typed configuration bundles for backend and frontend consumers as read-only projections of the governed config artifacts and registry state described in §3.3 and §3.7. These bundles are canonical JSON snapshots used by internal code and adapters; schemas and artifact\_keys remain single-homed in HDE-Schemas & Artifacts, and token semantics remain in HDE-Governance and the Glow QA Guide.

### **3.8.1 Generator posture (closed rails, canonical JSON)**

The bundle generator responsible for producing FE/BE config bundles MUST:

* Run under closed rails and determinism pins before computing or writing any bundle:

  * SAFE\_MODE \= 1

  * ALLOW\_NETWORK \= 0

  * LC\_ALL \= C

  * LANG \= C

  * TZ \= UTC

* Load configuration exclusively through the typed loader described in §3.1 and the governed config artifacts described in §3.7 (registry report, Magic-10 config, band-edges config), without introducing new configuration sources.

* Emit both bundles using the Canonical Serialization Package (§4 / §10.1):

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact separators

  * exactly one trailing line feed

  * arrays that represent sets deduped and ASCII-sorted before emission

* Two-run identity MUST hold for each bundle: generating FE and BE bundles twice with identical inputs and environment yields byte-identical JSON.

Implementation note (informative). In the current engine repository, this behavior is implemented by a closed-rails bundle builder in engine/config/bundles.py and a CLI script in tools/config/generate\_bundles.py. These names are informative only; the normative rules remain those in this section and in HDE-Schemas & Artifacts.

### **3.8.2 Backend config bundle (internal scope)**

The backend bundle is a governed config snapshot whose artifact\_key and schema tag are owned by HDE-Schemas & Artifacts (for example, config\_bundle.be and config\_bundle.be.v1).

At a minimum, this bundle:

* Includes the full Magic-10 configuration as derived from the Magic-10 config artifact:

  * closed category order

  * per-category caps and other configuration parameters

  * the seed metadata block (template identifier, seed version, updated\_at\_utc, checksum) consistent with §3.7.2

* Includes the full band-edges payload as derived from the band-edges config artifact:

  * band labels

  * edges

  * clamp behavior

  * rounding mode

  * version

  * source pointer consistent with §3.7.3

* Includes the registry-backed domain view needed by backend scoring and ordering logic, such as:

  * channels with ids, gates, centers, circuit\_primary/substream, primary\_domain, domains, and any flags required by the engine

  * centers and domains as recorded in the registry report

  * alias\_policy in a names-only form consistent with §3.1 and §3.3

* Carries a structured sources block that, for each upstream governed config artifact used (for example, registry\_report, Magic-10 config, band-edges config), records at least path, sha256, and size\_bytes values matching the current Evidence Index / Machine Mirror entries.

The backend bundle is internal/admin-visible only and serves as a typed configuration source for backend consumers; it does not define public Reader or CLI bytes.

### **3.8.3 Frontend config bundle (client-facing scope)**

The frontend bundle is a governed config snapshot whose artifact\_key and schema tag are owned by HDE-Schemas & Artifacts (for example, config\_bundle.fe and config\_bundle.fe.v1).

At a minimum, this bundle:

* Provides a slimmed view of Magic-10 configuration suitable for clients:

  * Magic-10 category order and caps

  * any additional per-category configuration needed for UI behavior

* Provides a reduced band-edges view:

  * band labels

  * edges

  * clamp behavior

  * rounding mode

  * version

  * a names-only reference back to the same thresholds source used for the backend bundle

* Exposes channel identifiers and related metadata required by clients:

  * channel ids plus associated centers and domains

  * alias policy in the same names-only form as the backend bundle

* Carries a sources block with the same structure and guarantees as the backend bundle, so clients can verify that FE config reflects the current governed config artifacts and registry state.

The frontend bundle is intended for FE/client consumption and must not introduce new semantics beyond what is already defined by the governed config artifacts and registry report. It remains an internal, governed artifact; public Reader and CLI contracts are still owned by HDE-CLI-API-Vendor-Ref.

### **3.8.4 Schemas and evidence (routing only)**

Typed bundle structures are validated in tests against JSON Schemas that live alongside the code, but those schemas are not PF-canonical until HDE-Schemas & Artifacts is updated to include them.

For now: HDE-Schemas & Artifacts owns the canonical artifact\_keys, path conventions, and any future bundle schema catalogs; PF14 references bundles and their schemas by title only and does not restate the JSON schemas here.

Each bundle MUST:

* appear in the human Evidence Index with an artifact\_key and discovered\_physical\_path

* have a corresponding record in the machine mirror with sha256, size\_bytes, produced\_at\_utc, role, and proof\_anchor

* have a co-located path-proof transcript referenced by proof\_anchor

Tests for typed bundles MUST:

* prove canonical formatting and two-run identity

* validate bundle structures against the local JSON Schemas

* assert that Magic-10, band-edges, channels, centers, domains, alias\_policy, and the sources block are consistent with the governed config artifacts and registry report described in §3.3 and §3.7

PF14 does not introduce new acceptance tokens for bundles; token names and gating for config bundles remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

# 4\) Canonical Serialization Package

One serializer and one emitter MUST serve all public bytes (Reader, CLI, evidence artifacts).

## **4.1 Policy (normative)**

Single presenter/emitter (byte-authoritative). All public JSON bytes MUST be produced by one presenter/emitter entrypoint symbol. Reader and CLI MUST delegate byte emission to this exact symbol (titles-only allow-list; no alternate byte emitters). Wrapper envelope builders MAY exist, but they MUST NOT serialize public bytes outside the allow-listed entrypoint.

See §10.2 for the unified entrypoint and §10.1 for canonicalization; the preimage recipe is in §3.2.

Canonical JSON. UTF-8 (no BOM); ASCII-sorted keys; compact separators (, and : only); exactly one trailing LF (\\n). Arrays that function as sets are deduplicated and ASCII-sorted by identity.

Single source of bytes. The same canonical serializer is used for Reader responses, CLI stdout on parity surfaces, and machine-generated evidence artifacts.

Determinism. AB↔BA parity and two-run identity MUST hold for identical inputs/environment. Run all canonicalization and byte-compares with LC\_ALL=C, LANG=C, TZ=UTC.

Tests use the same path. Test code MUST NOT bypass the shared presenter/emitter.

## **4.2 Prohibited (hard fail)**

No ad-hoc serialization on public paths. No json.dumps(\<OBJECT\>), no jsonify(\<OBJECT\>), no templated/string-built JSON, no framework helpers that bypass the presenter, no pretty/indented output, and no test-only shims.

## **4.3 Allow-list (code/CI owned)**

Maintain an explicit allow-list of presenter/emitter symbols. Only allow-listed symbols may serialize public bytes (allow-list owned in code/CI; not pinned here).

## **4.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names.

The mechanics obligations in §4 require that acceptance proofs exist for:

* shared presenter/emitter coupling across Reader and CLI  
* canonical JSON discipline (UTF-8, sorted keys, compact, exactly one trailing LF, arrays-as-sets canonicalization)  
* determinism (AB↔BA neutrality and two-run identity)  
* evidence/index discipline for serializer and emitter guard artifacts

  ## **4.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

List by title/path in Appendix D: Evidence Index and add 1:1 records in artifacts/evidence\_index.jsonl (each with artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor; canonical JSONL; one LF).

Examples:

* grep\_guard/serializer — proves no ad-hoc serializers on public paths (CI regex results).  
* emitter\_symbol/proof — import-graph/reflection proof that Reader and CLI call the same presenter symbol.  
* canonical\_json/check — policy check (UTF-8/no BOM, sorted keys, compact, one LF).  
* canonical\_json/compare — byte-compare of public bytes vs canonical re-serialization (expected empty diff).

  ## **4.6 Routing (titles-only)**

Transport and HTTP behavior (headers, conditional delivery, caching) and CLI stream policy live in HDE-CLI-API-Vendor Ref; token roster in HDE-Governance.

# 5\) Deterministic Tie-Break & Total-Order Module \[Required-Now\]

Purpose. Provide reusable comparators and helpers that impose a total, deterministic order over strings, numeric tuples, and domain identities the Engine uses. These utilities are called wherever ordering is consumed (selection, aggregation, snapshotting, evidence), ensuring AB↔BA neutrality and two-run identity. All byte-sensitive checks run with LC\_ALL=C, LANG=C, TZ=UTC.

## **5.1 Comparator policy (normative)**

Locale-free, bytewise order. All string ordering is ASCII byte order (code-point ascending), case-sensitive, under LC\_ALL=C. No locale collation; no Unicode normalization.

Stable total order. Comparators are antisymmetric, transitive, and total (every pair comparable). Equal inputs are stable (no reordering of equals).

Arrays-as-sets discipline. When an array is used as a set: dedupe by identity, then ASCII-sort with the appropriate comparator; never rely on map/set iteration order.

No clocks/RNG. Tie-breaks never consult time or randomness.

## **5.2 Domain comparators (exact)**

* IDs (general strings). cmp\_id(a,b) → ASCII bytewise comparison.  
* Magic-10 categories. cmp\_category(a,b) → compare by frozen Magic-10 rank (titles-only to HDE-Schemas and Artifacts §2.6 / HDE-Math-Spec §5.1); if still equal (should not occur), fall back to cmp\_id.  
* Centers (snake\_case). cmp\_center(a,b) → cmp\_id(a,b) over center IDs.  
* Channels (NN-NN). cmp\_channel(a,b) → compare first the left NN (two-digit ASCII), then the right NN. Inputs must already be canonical NN-NN (min-first, zero-padded, ASCII hyphen \-).

Numeric then id (tuples). For (value, id) (for example, equal-score ties):

* sort numeric ascending (integers 0..100)  
* break ties with cmp\_id (stability preserved)  
* descending variants use an explicit descending numeric comparator (do not negate and re-sort), then the same cmp\_id tie-break

## **5.3 Helpers (reusable)**

* dedupe\_sort(set\_like, cmp) → returns unique, ASCII-sorted array using cmp.  
* sort\_pairs(pairs, key\_cmp, val\_cmp) → stable sort over (key,val) with key\_cmp then val\_cmp.  
* ensure\_total\_order(cmp, generator) → property-test harness asserting antisymmetry, transitivity, and totality for domain samples.  
* canonicalize\_array(arr, cmp) → enforce set discipline (dedupe \+ ASCII sort) prior to canonical JSON emission.

## **5.4 Engine call-sites (must use)**

* Composite surfaces. Ordering of channels\_defined, channels\_em, centers\_defined must use cmp\_channel / cmp\_center before emission/evidence (see Appendix E — Composite fingerprint).  
* Category iteration. All multi-category passes must iterate in the frozen Magic-10 order (titles-only HDE-Schemas and Artifacts §2.6); never rely on hash iteration.  
* Presenter paths. Before canonical serialization, arrays-as-sets must pass through dedupe\_sort with the appropriate comparator.

## **5.5 Determinism & neutrality**

AB↔BA identity. Using the same comparators on normalized (A,B) and (B,A) yields identical arrays/tuples.

Two-run identity. Re-running with the same inputs produces byte-identical sequences after canonicalization.

Serializer coupling. Canonical dumps use UTF-8 (no BOM), sorted keys, compact, exactly one LF (§4/§10.1), with arrays already deduped & ASCII-sorted.

## **5.6 Validation (binary & property tests)**

* Property tests: for each domain comparator, prove antisymmetry, transitivity, totality over generated samples.  
* Set discipline: dedupe\_sort removes duplicates and preserves canonical order (idempotent on already-canonical arrays).  
* Channel ordering: given mixed NN-NN arrays, verify strictly increasing (left,right) pairs and min-first orientation; reject non-canonical tokens.  
* Category loop: verify the iteration order equals the frozen Magic-10 index sequence (titles-only HDE-Schemas and Artifacts §2.6).  
* ABBA / two-run: byte-compare outputs for (A,B) vs (B,A) and across two identical runs (must match).  
* Serializer cross-check: canonical re-serialization byte-compare (UTF-8, no BOM, one LF).

## **5.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

List by title/path in Appendix D: Evidence Index and mirror 1:1 in artifacts/evidence\_index.jsonl (records-only JSONL; UTF-8 no BOM; sorted keys; compact; exactly one LF).

Each mirror record includes:

* artifact\_key  
* sha256  
* size\_bytes  
* produced\_at\_utc  
* discovered\_physical\_path  
* proof\_anchor

Update human Index and mirror in the same PR; CI enforces 1:1 parity and path-proofs.

* order/props\_total\_order — property-tests pass (antisymmetry/transitivity/totality).  
* order/channels\_sorted — channel identity ordering proof.  
* order/categories\_iter — Magic-10 loop order proof.  
* order/abba\_identity — AB↔BA byte-equality using these comparators.  
* canonical/json\_compare — canonical dump compare (arrays deduped & ASCII-sorted).

Routing (titles-only):

* Frozen Magic-10 order & IDs: HDE-Schemas and Artifacts §2.6, HDE-Math-Spec §5.1.  
* Canonical JSON rules & fingerprint shape: HDE-Schemas and Artifacts §4, HDE-Math-Spec Appendix E.  
* Governance tokens roster: HDE-Governance §2.0 Acceptance Tokens.

## **5.8 Dev sampler HTTP harness (internal/dev-only)**

Purpose. Provide a dev/admin-only HTTP harness for the sampler core that mirrors the dev sampler CLI semantics while remaining a strictly internal surface. This harness is for local and dev/admin use; it is not part of the public API, is not listed in the Endpoint Catalog, and is not an A7 proof surface.

Route and method. Route: POST /internal/dev/sampler. Method posture: POST only; unsupported methods return 405\. The route is non-conditional: no conditional headers are honored, and the route never returns 304\. Transport posture: emitted via the same canonical serializer used elsewhere in this document (UTF-8, no BOM, ASCII-sorted keys, compact, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted). Successful dev/admin responses carry JSON Content-Type, Cache-Control: no-store, and no ETag. Error envelopes follow the writer/error posture defined elsewhere in this document.

Environment gating (dev/admin only). The dev sampler HTTP harness is enabled only when APP\_ENV is explicitly one of:

* dev  
* test  
* local

Mechanics requires that:

* When APP\_ENV is any other value (including prod), or when APP\_ENV is missing or empty, POST /internal/dev/sampler returns a writer-style 403 forbidden response with the standard typed error envelope for refusal (numeric-free, canonical JSON), and does not call the sampler core.  
* When APP\_ENV is allowed, the handler may proceed to parse the request body and invoke the sampler core as described below.

Detailed auth and env policy (including any additional guards applied to internal/dev routes) remain single-homed in HDE-Governance and Glow Infrastructure; this section records only that APP\_ENV gating is required and that prod/misconfigured environments must be refused.

Dev Reader start helpers (APP\_ENV propagation). Infra-owned dev Reader start helpers (for example, scripts that launch adapter.http\_reader in Codespaces or local dev) MUST:

* propagate APP\_ENV from the calling environment as-is, including when it is explicitly set to "dev", "test", "local", "prod", an empty string, or left unset  
* MUST NOT supply a default APP\_ENV value (for example, forcing APP\_ENV=dev when it is empty or unset)

The start helper may set SAFE rails (SAFE\_MODE, ALLOW\_NETWORK) and locale/time pins (LC\_ALL, LANG, TZ) and may set PORT, but it must not override the caller’s choice of APP\_ENV.

APP\_ENV gating semantics for /internal/dev/sampler remain owned by this section and the adapter:

* when APP\_ENV ∈ {dev, test, local}, the handler may proceed to validate the request body and invoke the sampler core  
* when APP\_ENV is any other value (including prod, missing, or empty), the handler must return a 403 writer-style refusal and must not call the sampler core, as specified above

Live QA harnesses (for example, dev sampler Live QA scripts) rely on this behavior to exercise and verify the full set of APP\_ENV modes (dev/test/local vs prod/empty/unset) required by Governance and QA rails (names and token semantics remain single-homed in Glow Infrastructure, Glow QA Guide, and HDE-Governance). This clarification ensures infra start helpers do not silently mask gating bugs by forcing APP\_ENV to an allowed value.

Request body (dev/admin only). The handler accepts a single JSON object body with these fields:

* viewer\_id — required non-empty string identifying the viewer in this dev/admin context.  
* candidate\_ids — required non-empty array of non-empty string identifiers for the candidates to be ranked.  
* seed — optional value used only as metadata for this dev harness; it does not alter eligibility or ordering.

Mechanics requires strict schema behavior:

* Missing or malformed viewer\_id, an empty candidate\_ids array, non-string candidate ids, or unknown extra top-level keys must be rejected with a 422 invalid\_input error using the standard error envelope and writer transport posture.  
* No other fields are accepted on this route.

The intent is to drive the sampler core with IDs and fixed placeholder feature values for dev/admin inspection; this harness does not expose compat scores, bands, or any other internal numeric state.

Behavior and payload. When APP\_ENV is allowed and the request body is valid, the handler:

* Builds in-memory sampler inputs (for example, a viewer profile and candidate feature records) from viewer\_id and candidate\_ids, using fixed safe placeholders for any features not specified by PF-Canon.  
* Invokes the existing sampler core (for example, sample\_and\_rank) without changing its eligibility or ordering rules.  
* Constructs a response payload with exactly these top-level keys:  
  * candidate\_ids — an array of candidate ids in the ranked order returned by the sampler core.  
  * meta — an object that, at minimum, includes:  
    * seed — the provided seed value rendered as a string if present, or null if no seed was supplied.  
  * viewer\_id — echo of the viewer\_id from the request.

Mechanics requires that:

* For a fixed viewer\_id, candidate\_ids set, and seed, repeated calls under the same environment produce byte-identical response bodies (two-run identity).  
* For a fixed viewer\_id and candidate\_ids but different seeds, candidate\_ids remain identical; only meta.seed differs between responses.  
* The response body is canonical JSON (UTF-8, ASCII-sorted keys, compact, one LF; arrays-as-sets deduped and ASCII-sorted).

Dev harness start commands, base URLs, and responsibilities (dev/admin-only). For /internal/dev/sampler and any other internal/dev HTTP harness that is intended for QA or evidence flows and is not part of the public API, Mechanics requires a clear split of responsibilities between infra/ops and QA/PO, and concrete wiring for start commands and URLs.

Infra-owned dev start commands (per environment). For each environment where /internal/dev/sampler is intended to be used (at minimum: local dev and Codespaces), infra/ops MUST define and maintain a canonical dev Reader start command or service definition that:

* starts the Reader process with APP\_ENV set to an allowed value for this harness (dev/test/local per §5.8)  
* binds to a deterministic host and port for that environment (for example, 127.0.0.1:\<port\> or the platform-assigned $PORT), consistent with the runtime posture in §32

This start command or service definition MUST be treated as infra-owned configuration:

* PO and QA agents MUST NOT guess the dev harness start command, choose a port on their own, or invent a Reader process wiring for QA.  
* Changes to the start command, binding host, or port are infra changes and must be reflected in the same places that document other runtime wiring (Infrastructure docs by title).

The example runner shown elsewhere in this guide (for example, a local python \-m adapter.http\_reader \--bind 127.0.0.1:5000 command) is illustrative only; the normative requirement is that there is at least one infra-owned dev start command for each environment where this harness is intended to run.

Base URLs and DEV\_SAMPLER\_URL (env wiring). Infra/ops MUST derive and publish, for each such environment, a concrete base URL for the dev Reader process (for example, [http://127.0.0.1](http://127.0.0.1):\<port\> in local dev or the appropriate forwarded port in Codespaces), and from that base URL define a concrete sampler harness URL:

* DEV\_SAMPLER\_URL \= \<base\_url\>/internal/dev/sampler

DEV\_SAMPLER\_URL MUST be treated as an infra-owned configuration value:

* QA plans and doc agents MUST consume DEV\_SAMPLER\_URL (or an equivalent infra-exposed value) as an input and MUST NOT guess hostnames, ports, or full URLs for /internal/dev/sampler.  
* Any change to the underlying dev Reader binding (host/port) MUST be reflected by infra in the published DEV\_SAMPLER\_URL value; QA and docs do not hard-code ports or recompute URLs independently.

Mechanics does not pin where DEV\_SAMPLER\_URL is stored (for example, env var, config file, or Codespaces devcontainer config), only that it exists as a single infra-owned binding for /internal/dev/sampler per environment and that QA/PO treat it as the authority for that harness URL.

Repo-side dev sampler healthcheck posture (required). Any repo-owned helper or healthcheck that consumes `DEV_SAMPLER_URL` for `/internal/dev/sampler` MUST treat that value as authoritative and MUST NOT reconstruct, default, or guess an alternate URL.

The repo-side healthcheck MUST:

* trim `DEV_SAMPLER_URL` before validation  
* fail non-zero when `DEV_SAMPLER_URL` is missing or empty  
* require an explicit hostname and an explicit port in `DEV_SAMPLER_URL`  
* reject silent fallback to `127.0.0.1`, `localhost`, or any default port  
* record the effective `dev_sampler_url` and the rails snapshot before exercising the dev and prod checks

Negative-path coverage is required for the repo-side healthcheck family. The test suite for this healthcheck MUST include, at minimum:

* one failure-path test for missing or empty `DEV_SAMPLER_URL`  
* one failure-path test for a `DEV_SAMPLER_URL` value that lacks an explicit port

These repo-side helper and healthcheck requirements do not widen the `/internal/dev/sampler` route contract and do not promote the route into a public or A7 surface.

Infra validation of dev harness URLs (pre-QA). Before handing any DEV\_SAMPLER\_URL to QA or using it in QA plans, infra/ops MUST validate the dev sampler HTTP harness locally:

* Run the infra-owned dev Reader start command with APP\_ENV=dev (and, where feasible, the determinism pins used elsewhere in this guide: SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC).  
* Issue at least one simple HTTP/1.1 POST to DEV\_SAMPLER\_URL with:  
  * Content-Type: application/json; charset=utf-8  
  * a minimal, schema-valid request body consistent with §5.8 (for example, a non-empty viewer\_id and a non-empty array of string candidate\_ids, with or without seed)  
* Confirm that the response:  
  * uses canonical JSON output and the canonical serializer posture defined elsewhere in this guide (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted)  
  * matches the request/response shape for /internal/dev/sampler described in §5.8 (top-level keys, types, and determinism requirements)  
  * carries headers consistent with internal/dev writer posture (for this dev harness: JSON Content-Type, Cache-Control: no-store for errors, no ETag)

If this validation fails, infra MUST treat the issue as an infra/tooling misconfiguration, not as an Engine/sampler behavior failure, and correct the wiring before any QA plan or doc step refers to DEV\_SAMPLER\_URL.

Responsibility split (normative). Infra/ops agents are responsible for:

* defining and maintaining the dev Reader start commands for internal/dev harnesses (including /internal/dev/sampler) per environment  
* choosing and wiring the base URL and port for the dev Reader process  
* defining and updating DEV\_SAMPLER\_URL (and any similar dev harness URLs) to reflect actual Reader wiring  
* validating those URLs via local HTTP/1.1 JSON POSTs under the appropriate rails before they are handed to QA or docs

PO and QA agents are responsible for:

* consuming DEV\_SAMPLER\_URL (and similar infra-defined URLs) as inputs in QA plans, scripts, and documentation steps  
* treating failures to reach or use DEV\_SAMPLER\_URL as tooling/infra issues to be escalated, not as sampler/core bugs, unless the infra validation above has already passed and QA has concrete behavior evidence

Mechanics records these responsibilities so the dev sampler HTTP harness and any similar internal/dev harnesses are fully accounted for in the mechanical schematic: the harness route and behavior in §5.8, the dev Reader process and ports via infra-owned start commands, and the dev URLs (DEV\_SAMPLER\_URL and equivalents) wired and validated before QA exercises them.

EPIC030 PR-02 dev sampler evidence family (records-only). When this bounded PR-02 family is used to prove the dev sampler HTTP harness, Mechanics requires the governed evidence family to include these artifacts under `audit/qa/hde-epic030/pr-02/`, each with a sibling path proof:

* `dev_sampler_http_headers.txt`  
* `dev_sampler_http_body.json`  
* `dev_sampler_two_run_identity.json`  
* `dev_sampler_seed_only.json`

The evidence family MUST be bound into the existing Human Evidence Index and Machine Mirror homes in the same PR, with the hash sentinel, mirror sidecars, path proofs, LF validation, evidence-path validation, mirror-schema validation, and topology orientation refresh/check kept coherent with the final artifacts.

This records a local/dev evidence family only. It does not add a public route, does not add an Endpoint Catalog success route, does not make `/internal/dev/sampler` A7-eligible, and does not create close-stage acceptance-map or close-pack artifacts.

A7 and Endpoint Catalog posture. POST /internal/dev/sampler is an internal/dev surface and is explicitly not a JSON success route in the Endpoint Catalog.

No A7 proofs are run against this route, and it must not be referenced in the Catalog or any A7 composite proofs.

Any headers-only captures for this route are local/dev diagnostics only and do not contribute to A7 acceptance tokens.

The CLI dev sampler remains the primary sampler harness; this HTTP dev harness is a convenience wrapper around the same sampler core for dev/admin workflows, subject to the same canonical JSON and determinism constraints.

# 6\) Deterministic Engine Core \[Required-Now\]

Contract. The Engine Core is pure compute (ops, scoring, aggregation). It performs no I/O, uses no clocks, reads no globals/env, and does not depend on system locale. All behavior is driven by explicit inputs and frozen pack/preset constants (titles-only to PF-Canon-HDE-Schemas & Artifacts / PF-Canon-HDE-Math-Spec).

## **6.1 Inputs & state (explicit only)**

Explicit parameters. All data (composite, feature flags, constants, viewer\_prefs) is passed by value or via a typed config object. No hidden sources. Do not read files, environment variables, or the clock; do not mutate module globals or singletons. Preconditions satisfied upstream. Alias normalization, tz resolution, and ingestion occur before the core (titles-only to PF-Canon-HDE-Schemas & Artifacts §2.1 / PF-Canon-HDE-CLI-API-Vendor-Ref §3.2).

## **6.2 Determinism pins**

AB↔BA neutral. Core results are identical when inputs A,B are swapped (AB \== BA after normalization). Two-run identity. Two evaluations over the same inputs \+ constants produce byte-identical results. Stable iteration. Do not rely on unspecified map/set iteration order: reduce over ASCII-sorted keys; arrays-as-sets are deduped & ASCII-sorted. Locale & serializer. All canonicalization/compares run under LC\_ALL=C. Any JSON the core emits for evidence uses the canonical serializer (UTF-8 no BOM, sorted keys, compact, exactly one LF). Numeric rules (titles-only). Follow PF-Canon-HDE-Math-Spec for integerization and rounding (round\_half\_up); avoid floating-point accumulation for public-path numerics. Use integer/fixed-point paths defined in PF-01.

## **6.3 Concurrency & parallelism**

Allowed if deterministic. Parallel evaluation is permitted only when reductions/merges are order-invariant (commutative/associative) and the final ordering is stabilized (ASCII sort) before exposure. No race-driven clocks/RNG. Do not consult time or RNG; if samplers/rankers require stochastic behavior, they must be seeded and isolated (see local policy section on stochastic samplers).

## **6.4 Errors & logging (internal only)**

Typed errors. Fail fast with typed, numeric-free errors; do not include vendor payloads. No payload/secret logging. Keys-only diagnostics; redact secrets; never echo request/response bodies.

## **6.5 Acceptance (binary)**

Two-run identity: run core twice on the same inputs → byte-equal outputs. ABBA: swap A,B → outputs (and any core-level artifacts) byte-equal. Stable order: arrays-as-sets are deduped & ASCII-sorted; reductions use sorted keys. Serializer check (if core emits JSON artifacts): canonical re-serialization byte-compare (UTF-8, no BOM, one LF). No I/O/clocks/globals: static/grep-guard \+ import-graph proof show no file/env/time access in core modules.

## **6.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

artifact\_key: engine/tworun\_identity — two-run proof; artifact\_key: engine/abba\_identity — ABBA compare; artifact\_key: canonical\_json/compare — canonical re-serialization proof (if core emits JSON artifacts); artifact\_key: guards/no\_io\_no\_clock — static/grep proof of no I/O/clocks/globals.

Each mirror record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof. The human Evidence Index (Appendix D) is updated in the same change; CI enforces human↔machine 1:1 parity and path-proofs.

Routing (titles-only). Numeric rules & public rounding/banding: PF-Canon-HDE-Math-Spec. Canonical JSON & pack/manifest: PF-Canon-HDE-Schemas & Artifacts. Governance tokens: PF-04 — §2.0 Acceptance Tokens.

## **6.7 Canonical Engine Core module and tests**

Scope (normative). The Dissolution engine work for tasks HDE-DISS004.1–.3 realizes the Deterministic Engine Core described in this section as a pure-compute module under the engine.core package. Mechanics records the canonical implementation and test harness here so that future changes stay aligned with §6.1–§6.6.

Canonical module and entrypoint. The Engine Core module lives at engine/core/core.py and exports frozen dataclasses and helpers that implement the pure-compute contract in §6:

* ParticipantState — frozen dataclass capturing the normalized state per party (for example, person identifier, compat score, band, and an immutable traits tuple).

* CoreConfig — frozen dataclass carrying Engine Core configuration, including band\_priority, which defaults to the canonical band ordering (for example, the BANDS tuple from compat thresholds).

* PerspectiveBreakdown — frozen dataclass capturing perspective-specific metrics for one party (for example, party-local score, delta, and any supporting breakdowns).

* CoreResult — frozen dataclass aggregating neutral metrics, ordered identifiers and bands, perspective breakdowns for both parties, and any shared-traits summary.

The canonical Engine Core entrypoint is engine.core.core.compute\_core. Mechanics and tests MUST treat this symbol as the single home for Engine Core behavior when evaluating the determinism and neutrality requirements in §6.2 and the acceptance checks in §6.5.

Neutral metrics, ordering, and shared traits. Neutral metrics are computed as symmetric functions of the two parties. In particular, the neutral compat score is an integer average of the two compat scores, and shared traits are derived via set intersection (using the existing canonical set helper and ID comparator) so that the shared traits tuple is identical for normalized AB and BA inputs.

Identifier and band ordering use the deterministic ordering utilities from the Engine’s comparators and thresholds:

* Party identifiers are canonicalized via compare\_ids. When both identifiers are equal, the pair is mapped to the ABBA\_CANONICAL\_PAIR constant so that self-pairs have a fixed canonical representation.

* Band pairs are ordered via a \_band\_rank function derived from CoreConfig.band\_priority and then by band name, ensuring that for a fixed configuration, ordered\_bands is identical for compute\_core(A,B, config) and compute\_core(B,A, config) and deterministic across runs.

These behaviors are normative for Engine Core; any future Engine Core changes MUST preserve AB↔BA neutrality and two-run identity as defined in §6.2.

Dedicated Engine Core test suite (closed rails). Purity tests live under tests/core/test\_engine\_core\_purity.py and MUST:

* import and reload engine.core.core under ensure\_determinism\_env(apply=True) to enforce determinism pins and closed rails

* use AST-based checks to reject imports whose root module is in {os, time, datetime, random, socket, subprocess}

* scan the module source text for forbidden snippets such as "os.environ", "time.", "datetime.", "random.", and "socket."

Together, these guards prove that the Engine Core performs no file, network, clock, RNG, or env access and does not introduce import-time side effects, satisfying the “no I/O/clocks/globals” requirement in §6.1 and §6.5.

AB↔BA behavior tests live under tests/core/test\_engine\_core\_abba.py and MUST:

* construct asymmetric A/B inputs (different compat scores and bands) using ParticipantState and CoreConfig

* assert that neutral fields in CoreResult (for example, neutral score, ordered\_pair, ordered\_bands, and shared traits) are identical for compute\_core(A,B, config) and compute\_core(B,A, config)

* assert that perspective-specific metrics in the PerspectiveBreakdown structures cross-swap as expected (for example, deltas for BA are the negation of the AB deltas) while remaining internally consistent

These tests are the canonical proof of AB↔BA neutrality for Engine Core and directly exercise the requirements in §6.2 and §6.5.

Determinism and JSON-compatibility tests live under tests/core/test\_engine\_core\_determinism.py and MUST:

* call compute\_core twice with identical inputs and CoreConfig under ensure\_determinism\_env(apply=True) and assert that the two CoreResult instances are equal

* serialize each result via json.dumps(dataclasses.asdict(result), sort\_keys=True) and assert that the resulting JSON strings are byte-identical

* verify that when CoreConfig.band\_priority is customized, ordered\_bands and ordered\_pair remain deterministic and consistent with the configured band priority

These tests serve as the Engine Core’s two-run identity and JSON-compatibility proof under the determinism posture in §6.2 and §6.3. They demonstrate that CoreResult is safe for use with the canonical serializer and evidence tooling described elsewhere in this guide, even though the Engine Core evidence artifacts themselves are wired in a later epic.

Evidence wiring (future epic). This subsection records the Engine Core’s pure-compute module and test harness only. The evidence artifacts and Machine Mirror records listed in §6.6 remain the long-term target for Engine Core evidence, but their wiring is explicitly assigned to a later epic (HDE-DISS004.4) and is not part of the mechanics recorded for the behavior-only work on HDE-DISS004.1–.3.

# 7\) Category Framework (internal) \[Required-Now\]

## **7.1 Closed list & scaffolds for per-category calculators**

Purpose. Wire per-category subtotal → band calculators with precedence hooks; do not restate Math or public payload schemas.

Frozen category set & order (titles-only). All category logic addresses the ten Magic-10 identifiers in their fixed canonical order. Iteration order is normative and MUST be enforced via the total-order utilities (ASCII / cmp\_category; see §5 and HDE-Schemas & Artifacts §2.6, HDE-Math-Spec §5.1).

Per-channel semantics (normative). Calculators consume channel-scoped primitives: every “channel” reference is the canonical NN-NN edge (min-first, zero-padded), not a free-form string or unordered gate pair. Junction gates {10,20,34,57} may appear in multiple channels; treat each channel independently. Compromise direction and compromise gate fields are derived only from canonical gate ordering and do not create a secondary runtime compromise surface. Channel-scoped circuit metadata is derived from governed channel catalog data and stays attached to the channel record in category-framework proof artifacts. Arrays of channels used as sets MUST be deduped & ASCII-sorted by canonical identity (see §5 comparators and canonicalization rules in §4; titles-only to HDE-Schemas & Artifacts §2.1).

Public vs internal. Category subtotals and narrative keys are internal/admin artifacts. The public Reader surface stays bands-only, numeric-free and is specified in HDE-CLI-API-Vendor-Ref (titles-only). Mechanics wires the allow-listed presenter/emitter (§4) and does not duplicate public JSON schema.

## **7.2 Compatibility Engine (pair) — contract**

Inputs (typed; titles-only). a, b — each is either an ID or a full person payload (HDE-CLI-API-Vendor-Ref Reader schema). Do not mix ID and payload for the same party; mixed forms ⇒ typed invalid\_input (HDE-CLI-API-Vendor-Ref error catalog, titles-only). viewer\_prefs — top\_category ∈ Magic-10 and weights for all ten categories as integers 0..100 (key set must equal Magic-10). Zero-weight rule: if a viewer assigns 0 to a category, candidates whose \#1 equals that category are excluded. (Titles-only: HDE-Math-Spec §5.1; HDE-Schemas & Artifacts §2.6; HDE-CLI-API-Vendor-Ref.)

Execution (internal math; titles-only). Subtotaling. Compute per-category integer subtotals (0..100) via the Feature Framework and pack-frozen constants (HDE-Math-Spec §5.4.2; see channel semantics in §7.1; core is I/O-free per §6). Banding. Map each subtotal to a band using inclusive-high thresholds (24/49/74/100) with round\_half\_up (HDE-Math-Spec §5.3). Narrative keys. Select {personal\_key, shared\_key} per category from governed ledgers; if absent, flag missing\_narrative\_key (no implicit fallback).

Outputs (admin/test surface only; titles-only). categories\[10\] in canonical Magic-10 order, each { id, score:int, band, personal\_key, shared\_key }; plus meta{ engine\_tag, release\_id }. Public Reader continues to emit bands-only. Contract bytes & schema are owned by HDE-CLI-API-Vendor-Ref and must be produced by the allow-listed presenter/emitter (§4). Do not embed JSON samples in this guide.

Determinism & acceptance (binary). AB↔BA parity & two-run identity. With identical inputs, subtotals, bands, and any admin snapshots are identical across (A,B) vs (B,A) and across runs; any emitted admin JSON is canonical (UTF-8/no-BOM, sorted keys, compact, one LF; arrays deduped & ASCII-sorted; LC\_ALL=C). Order. Category arrays appear in the frozen Magic-10 order; tests assert this via §5 comparators. Typed errors. Mixed input forms ⇒ invalid\_input; unknown IDs or malformed viewer\_prefs ⇒ invalid\_input (HDE-CLI-API-Vendor-Ref error catalog, titles-only). Evidence (records-only; path-agnostic). ABBA fingerprint consumption (HDE-Math-Spec Appendix E), two-run logs, canonical-compare logs; register mirror entries and update the human Evidence Index in the same change (HDE-Governance Appendix D: Evidence Index; HDE-Schemas & Artifacts mirror).

## **7.3 Band thresholds and tuning (admin)**

Registry only (titles-only). Mechanics maintains the authoring workflow for number-to-band thresholds (global or per-category) and the associated tooling; it does not restate numeric values. Band thresholds are internal/admin configuration only; the public Reader surface remains bands-only and numeric-free.

Normative sources. Inclusive-high policy and global edges (for example, 24, 49, 74, 100\) are specified in HDE-Math-Spec. Per-category overrides and the constants pack live in HDE-Schemas & Artifacts (constants and manifest rules); Mechanics routes to those documents by title and does not duplicate numeric tables here.

Compat threshold source (normative). Internal compat threshold code MUST derive `THRESHOLDS_V1` from `engine.magic10.thresholds.THRESHOLD_EDGES` and `BANDS` from `engine.magic10.thresholds.BANDS`. Compat threshold code MUST NOT maintain a second hard-coded threshold home or a second band-order home.

Admin/public split. The admin/test compat surface may carry scores and threshold evidence. The public Reader-facing surface remains bands-only and numeric-free. PR-04 threshold/tuning mechanics MUST NOT add a public route, new flag, new serializer path, second threshold home, acceptance-map path, token-matrix path, viability-log path, doc-delta-ledger path, or close-pack path.

Config artifacts (governed snapshots). Band thresholds are materialized by the Programmatic Configuration System as a governed band-edges config artifact (see §3.7):

* The band-edges config artifact captures band names, numeric edges, clamp behavior, rounding mode, and a version tag, and includes a structured pointer back to the thresholds source used to derive it  
* The artifact is generated under closed rails with canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing line feed) and must satisfy two-run identity in determinism-pinned environments, consistent with §3.7 and §4  
* Schema, artifact\_key, and any additional metadata fields for the band-edges config artifact remain single-homed in HDE-Schemas & Artifacts; Mechanics only requires that such an artifact exist, be deterministic, and be wired into the evidence skeleton  
* The same configuration system may also produce a governed Magic-10 config artifact (see §3.7) that defines per-category caps and seed metadata; band tuning and band-edges behavior must remain consistent with the Magic-10 configuration and the math rules in HDE-Math-Spec

Visibility and evidence. Thresholds and scores are admin/test-visible only. Mechanics provides helpers to dump and apply band-threshold sets and to capture identity and stability proofs, such as canonical snapshots and sha256 digests over compat bytes that include the final line feed. All tuning artifacts, including the band-edges config artifact and any supporting snapshots, must:

* be listed in the human Evidence Index with titles and paths  
* have corresponding machine-mirror records in artifacts/evidence\_index.jsonl with canonical JSONL records and path-proof anchors  
* be updated together with their mirror records in the same PR, under the evidence discipline defined in §1.3 and §37

EPIC030 PR-04 band-threshold evidence family (records-only). When the bounded PR-04 threshold/tuning family is used, Mechanics requires these governed artifacts under `audit/qa/hde-epic030/pr-04/`, each with a sibling path proof:

* `band_edges_binding.log`  
* `band_thresholds_diff.json`  
* `band_thresholds_identity_hash.txt`

Binding requirements. The PR-04 evidence family MUST prove, at minimum:

* `band_edges_binding.log` binds compat thresholds to the constants-pack-backed threshold edges and records the resolved `THRESHOLDS_V1` and `BANDS` source posture.  
* `band_thresholds_diff.json` records compact threshold diffs for the governed edges and band order, and reports PASS only when all compared threshold and band values match the expected governed source.  
* `band_thresholds_identity_hash.txt` computes identity hashes over LF-terminated compat bodies, records whether current AB and BA hashes match, and reports PASS only when the current AB↔BA identity comparison is true.  
* The PR-04 evidence generator is directly runnable from the repository root and uses canonical JSON emission for JSON artifacts.  
* Targeted tests cover constants-pack threshold routing and the evidence-generator failure case where mismatched AB and BA compat bodies must produce a FAIL identity-hash result.

Indexing requirements. The PR-04 family MUST be registered in the existing evidence-index update path, loaded into the Human Evidence Index source set, mirrored into the Machine Mirror, covered by sibling path proofs, and refreshed through the existing updater, orientation, mirror-schema, evidence-path, and LF-ending checks.

Mechanics does not define additional acceptance tokens for band tuning; token names and their semantics remain single-homed in HDE-Governance, HDE-Build Checklist, and HDE Phased Epics.

## **7.4 EPIC030 PR-05 category-framework evidence and indexing family (records-only)**

Purpose. For the bounded PR-05 category-framework family, Mechanics records repo-side proof responsibilities only. This family stays on existing category-framework, compat/admin, evidence-generator, and evidence-index surfaces. It does not create a public route, new flag, serializer or emitter work, close-pack work, QA-ledger work, Live QA runbook work, or PF-canon edit work.

Required governed artifacts. The PR-05 family MUST include, at minimum, these artifacts under `audit/qa/hde-epic030/pr-05/`, each with a sibling path proof:

* `per_channel_mechanics.json`  
* `category_canonical_compare.log`  
* `category_framework_binding.log`

Per-channel mechanics proof. The `per_channel_mechanics.json` artifact MUST record a PASS result for the category-framework per-channel mechanics proof and MUST bind the proof to the relevant task and subtask identifiers. It MUST include canonical channel edges, compromise direction and gate fields derived only from canonical gate ordering, channel-scoped circuit metadata derived from governed catalog channel data, and a channel-record count sufficient to prove the closed category-framework channel set exercised by the generator.

Canonical compare proof. The `category_canonical_compare.log` artifact MUST prove canonical round-trip equality for the PR-05 category-framework targets recorded by the generator, including the per-channel mechanics snapshot and compat body target(s), and MUST report PASS only when those canonical comparisons pass.

Top-level binding proof. The `category_framework_binding.log` artifact MUST summarize the PR-05 family and derive its top-level status from decisive predicates that include, at minimum:

* Magic-10 order preserved for admin compat.  
* Public Reader posture remains bands-only and numeric-free.  
* Human Index binding is present.  
* Machine Mirror binding is present.  
* Per-channel mechanics status is PASS.  
* Canonical compare status is PASS.

The top-level binding artifact MUST carry `canonical_compare_status` and MUST NOT report PASS when the canonical compare status is FAIL.

Indexing and refresh requirements. The PR-05 family MUST be registered in the existing evidence-index update path, loaded into the Human Evidence Index source set, mirrored into the Machine Mirror, covered by sibling path proofs, and refreshed through the existing updater, orientation, mirror-schema, evidence-path, and LF-ending checks. If generator logic changes after artifact bytes are first produced, the final governed artifacts, path proofs, Human Index, Machine Mirror rows, hash sentinel, and orientation snapshot MUST be regenerated from the final generator flow.

---

# 8\) Public Presenter & Emitter \[Required-Now\]

Transforms engine outputs into the Reader/CLI public envelope and emits canonical JSON via the allow-listed presenter–emitter.

## **8.1 Role**

Single public presenter/emitter for Reader and CLI.

Responsible for:

* Building the public body from engine outputs

* Applying canonical serialization rules

* Injecting idempotence metadata (idempotence\_hash, release\_id, meta.invocation\_tag)

* Feeding evidence artifacts for parity and determinism

## **8.2 Policy — Emitter & serializer**

Single emitter (byte-authoritative). Reader and CLI public bytes MUST be emitted via the same presenter–emitter entrypoint symbol.

CI maintains a symbol allow-list of byte-emitter symbols; no alternate byte emitters are allowed. Wrapper envelope builders MAY exist, but they MUST delegate byte emission to the allow-listed emitter and MUST NOT introduce alternate serializers on public paths.

Canonical serializer. The presenter MUST use the Canonical Serialization Package (§4):

* UTF-8 (no BOM)

* ASCII-sorted keys

* Compact JSON (no pretty/indented output)

* Exactly one trailing LF

* Arrays-as-sets deduped and ASCII-sorted

* All byte checks under LC\_ALL=C

Public shape (titles-only). The public payload shape is owned by:

* HDE-CLI-API-Vendor-Ref (public contract, headers, success/error envelopes)

* HDE-Math-Spec (Reader v1 preimage fields, bands, rounding)

Mechanics does not duplicate those bytes here.

## **8.3 Idempotence & identity**

Preimage (five keys). Compute idempotence\_hash over the canonical preimage: an object with exactly:

* reader\_version

* eligible

* categories

* meta

* release\_id

(No idempotence\_hash field yet. Preimage fields are defined in HDE-Math-Spec.)

Finalize. Insert idempotence\_hash (lowercase 64-hex) into the object and re-emit canonically to produce the public bytes (LF-terminated).

Identity coupling. release\_id is taken from the freeze-pack manifest (HDE-Schemas and Artifacts §6). meta.invocation\_tag participates in the preimage (HDE-Math-Spec).

## **8.4 Parity requirements**

Reader↔CLI parity. On parity surfaces, CLI stdout MUST be byte-identical to the Reader 200 body.

AB↔BA parity. For pair-sensitive flows (e.g., compat), AB and BA MUST produce identical bytes.

Two-run identity. With identical inputs and environment, two serializations MUST produce bitwise-identical public bytes.

## **8.5 Prohibited practices**

On governed public paths, the following are not allowed:

* Ad-hoc serialization (json.dumps(\<OBJECT\>), templating helpers, framework-specific jsonify-style calls)

* String-built JSON or partial concatenation

* Pretty/indented output or multi-LF endings

Only the allow-listed presenter/emitter may serialize public bytes.

## **8.6 Acceptance (tokens; titles-only)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names.

The mechanics obligations in §8 require that acceptance proofs exist for:

* shared presenter/emitter coupling

* Reader↔CLI parity on parity surfaces

* AB↔BA neutrality and two-run identity

* evidence/index discipline for parity and serializer proof artifacts

## **8.7 Evidence (records-only; path-agnostic; indexed via PF-12 Machine Mirror)**

Evidence artifacts are indexed and mirrored according to HDE-Schemas and Artifacts (§8.3 / §8.6).

Typical artifact\_key families for this component:

* parity/reader\_cli — Reader↔CLI byte-equality (public surface).

* parity/abba\_identity — AB↔BA byte-equality.

* parity/two\_run\_identity — Two-run identity digest/log.

* emitter\_symbol/proof — Import-graph/reflection proof of shared presenter symbol.

* canonical\_json/compare — Canonical re-serialization byte-compare of the public body.

Each mirror record MUST include:

* artifact\_key

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor (path to the co-located path-proof transcript)

The human Evidence Index (docs/evidence/INDEX.json) MUST be updated in the same change.

CI enforces:

* Human↔machine 1:1 parity

* Presence and correctness of path-proofs

## **8.8 Routing (titles-only)**

Public payload & headers: HDE-CLI-API-Vendor-Ref

Preimage / rounding / banding: HDE-Math-Spec

Evidence policy & tokens: HDE-Governance

This section governs mechanics only; all concrete bytes, tokens, and schemas are owned by the PF-Canon documents above.

# 9\) Reader & Compat endpoints

## **9.1 Endpoint Catalog (JSON success) \[Required-Now\]**

Purpose (normative). Provide a canonical machine-readable inventory of HTTP endpoints in the Engine repo and, within that inventory, clearly identify which endpoints are JSON success routes eligible for A7 proofs. Entries are titles-only; bytes/examples and detailed contract semantics remain in their single homes.

This catalog exists to prevent drift between code, QA plans, and audits by making endpoint classification explicit and testable.

Scope & rules.

Single home (inventory). docs/ENDPOINTS\_CATALOG.json is the only machine-readable inventory of HTTP endpoints for this repo. It must include, at minimum:

* public Reader endpoints

* compat endpoints (internal/admin as applicable)

* internal identity endpoints (for example, /internal/version)

* ops probe endpoints (health/ready/diagnostics)

* dev harness endpoints (for example, /internal/dev/sampler)

A7-eligible subset. A7 proofs apply only to endpoints explicitly marked as A7-eligible JSON success routes in this catalog. /internal/\* endpoints are never A7-eligible; /internal/version is operator-only and not A7-eligible (see HDE-Governance §10.5).

Classification is mandatory. Every catalog entry MUST be classified into one of the following endpoint classes (names are for catalog entries; PF docs still route by title):

* public\_reader

* internal\_admin (includes internal/admin compat surfaces)

* internal\_identity

* ops

* dev\_harness

Mixing responsibilities is permitted but discouraged. Implementations may mix endpoint classes in one Python module, but the catalog must still carry per-endpoint classification so CI and QA can enforce distinct rails and posture per class.

Endpoint-class authority note (normative). Endpoint class, A7-eligibility posture, and dev/internal scope are per-endpoint catalog facts. They remain authoritative even when handlers are implemented in different repo modules and mounted together by adapter factories; handler package path or module placement MUST NOT be used to infer catalog class or proof-surface posture.

Crosswalk (mechanics-only; current canonized surface family):

* /reader — public\_reader; current Reader success surface; A7-eligibility is determined by the catalog entry for this route and its proof-surface rules.  
* /api/compat/v1 — internal\_admin; internal/admin compat surface; not a public proof surface by route family alone.  
* /internal/dev/sampler — dev\_harness; internal/dev harness; never A7-eligible.  
* /dev/\*/conjunction — dev\_harness bounded conjunction-family notation for the current canonized conjunction routes, including /dev/writer/conjunction, /dev/reader/conjunction, and /dev/sampler/conjunction; not A7-eligible unless a future canon change explicitly says so.

Bounded conjunction-family rule. The /dev/*/conjunction notation is a bounded catalog shorthand for the currently canonized conjunction-family dev routes only. It MUST NOT be interpreted as a reusable wildcard that automatically classifies future /dev/* routes as valid dev-harness surfaces or as outside the formal proof family by pattern alone.

Catalog entry minimum fields (titles-only; schema owned elsewhere). Each entry in docs/ENDPOINTS\_CATALOG.json MUST include, at minimum:

* path — for example /reader, /api/compat/v1, /internal/version, /ops/health, /internal/dev/sampler

* method — GET, POST, HEAD (or a list if an endpoint supports multiple methods)

* classification — one of the endpoint classes above

* blueprint\_module — titles-only pointer to the owning module (for example adapter/http\_reader.py, engine/http/compat\_handler.py)

* rails\_profile — short, names-only summary of rails and gating expectations (for example “requires APP\_ENV=dev”, “ops-only”, “A7 success posture”, “writer no-store posture”)

* a7\_eligible — boolean (true only for JSON success routes eligible for A7 proofs)

* env\_gate — for entries where reachability is env-gated (titles-only; exact gating semantics are routed to Governance/Infrastructure)

Route identifiers in the endpoint catalog (required). Where an endpoint has a stable route identifier (including dev-harness writer endpoints), the corresponding docs/ENDPOINTS\_CATALOG.json entry MUST include route\_id.

* /dev/writer/conjunction MUST be present in the catalog as a dev\_harness endpoint with route\_id \= dev.writer.conjunction.v1.

Tests (required). tests/http/test\_endpoint\_catalog.py MUST enforce that writer-path entries include their expected route\_id values.

Field-level schema and validation for this catalog are owned by HDE-Schemas & Artifacts (titles-only). This guide defines the mechanical requirement that the catalog exists, is complete, and is used as the single inventory source.

A7 invariants to prove (titles-only; for a7\_eligible=true entries only):

* 200: quoted, strong ETag; Vary: Authorization, Accept-Encoding; success cache headers  
* HEAD: status 200; validators mirror 200 (including Content-Type); Content-Length \== len(identity 200 body)  
* 304: only after prior 200-with-body; omit Content-Type and omit Content-Length; validators mirror cached 200  
* Encoding invariance: for the same canonical LF-terminated body, ETag identity and effective Content-Length are stable across Accept-Encoding identity and gzip. If br is supported for the same route, it MUST also be invariant and proven.  
* Writers/errors posture: non-success writers and error routes carry Cache-Control: no-store (recorded as headers-only evidence)

Catalog files (single home):

* docs/ENDPOINTS\_CATALOG.json (canonical JSON; one LF) — machine-readable endpoint inventory with mandatory classification and A7 eligibility flags  
* docs/ENDPOINTS\_CATALOG.json.sha256 — sidecar hash of the canonical bytes; MUST reference docs/ENDPOINTS\_CATALOG.json for `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256` verification from repo root  
* artifacts/audit/ENDPOINTS\_CATALOG.json — governed audit snapshot of the catalog (generated; not a second home); MUST be byte-identical to docs/ENDPOINTS\_CATALOG.json

Endpoint catalog updates for dev conjunction preview endpoints (required). The dev conjunction preview endpoints (/dev/reader/conjunction and /dev/sampler/conjunction) MUST be registered in docs/ENDPOINTS\_CATALOG.json as dev\_harness endpoints, and MUST be marked as not A7-eligible.

Integrity sidecars (required). Any change to docs/ENDPOINTS\_CATALOG.json bytes MUST be accompanied by regeneration of the integrity artifacts for the catalog in the same change-set:

* docs/ENDPOINTS\_CATALOG.json.sha256

* docs/ENDPOINTS\_CATALOG.json.path\_proof.txt

* docs/ENDPOINTS\_CATALOG.json.sha256.path\_proof.txt

* artifacts/audit/ENDPOINTS\_CATALOG.json (byte-identical mirror)

* artifacts/audit/ENDPOINTS\_CATALOG.json.sha256

Do not hand-edit checksums or path\_proof transcripts. Regenerate them via the approved integrity tooling so they match the updated catalog bytes.

Proof artifacts (headers-only; one LF each; for A7-eligible entries):

* artifacts/proofs/endpoints\_env\_gate\_proof.log — proves non-prod entries are unreachable in prod  
* artifacts/proofs/success\_get.txt — GET 200 proof (quoted strong ETag, Vary)  
* artifacts/proofs/success\_head.txt — HEAD parity with GET 200  
* artifacts/proofs/success\_304.txt — 304 omission proof (CT/CL omitted; validators mirror)  
* artifacts/proofs/success\_encoding\_invariance.txt — encoding-invariance proof (identity and gzip; include br only when supported)  
* artifacts/proofs/success\_writers\_errors.txt — writers/errors no-store posture

Proof generation (normative). Proof artifacts under artifacts/proofs/ are checked-in evidence outputs and MUST be generated, not hand-edited. Writing these files is allowed only in explicit write mode (`HDE_WRITE_A7_PROOFS=1`); default test runs MUST NOT write proof artifacts.

Test expectations (mechanics only; titles-only routing for tokens). Mechanics requires that:

* endpoints classified as dev\_harness include an allow-listed proof route and a deterministic “success proof” capture path (A7), and include a negative proof for the closed-rails posture (A7).

* endpoints classified as internal\_health, internal\_version, and ops\_health have explicit proof routes and proofs, including “no body on GET” checks where applicable.

Forbidden invented Reader proof route (drift guard). There is no /api/reader-proof/v1 route. Plans, endpoint catalogs, and runbooks MUST NOT reference /api/reader-proof/v1.

Proof-surface selection posture. Any QA proof that depends on a Reader success route MUST reference the actual reachable Reader route for the target environment. Do not invent alternate “proof” routes.

Token semantics and acceptance are owned by HDE-Governance and Glow QA Guide (titles-only); PF14 records only that classification and tests must exist to keep endpoint posture enforceable and non-ambiguous.

## **9.2 Reader (cataloged success surface) \[Implemented\]**

Route. GET /reader?v=1 is the governed Reader success-proof surface in current scope and the cataloged Reader success surface used for Reader success-body, Endpoint Catalog/env-gate, and A7 transport work. In current local capture posture, this route is exercised with APP\_ENV=dev; rails remain closed (SAFE\_MODE=1, ALLOW\_NETWORK=0; no vendor I/O).

Emitter. Uses the allow-listed shared presenter/emitter (see §4 / §10.2); tests must not bypass the shared emitter.

Current capture error posture. Content-Type: application/json; charset=utf-8, Cache-Control: no-store, no ETag.

A7 proofs boundary. Local harnesses may capture headers for evidence, but authoritative A7 proofs run on a Catalog JSON success route; /internal/version remains an ops exception (see HDE-Governance §10.5).

Pins. All captures/compares run with LC\_ALL=C, LANG=C, TZ=UTC.

Rails posture. Rails defaults follow the Env Deployment Inventory (titles-only). Local capture of the Reader route does not perform vendor I/O; tests may run with rails closed for evidence capture, but the default environment posture itself is owned by Infrastructure.

Optional GET semantics (for local evidence only). If optional GET captures are taken on this route, they must follow PF10 invariants for captures, without becoming the A7 proof surface:

* 200: strong, quoted ETag; Cache-Control: private, max-age=0, must-revalidate; Vary: Authorization, Accept-Encoding; canonical JSON, one LF  
* HEAD: status 200; no body; validators mirror 200; Content-Type \== GET; Content-Length \== len(identity 200 body) (LF-terminated, pre-compression)  
* 304: only after prior 200-with-body; no body; omit Content-Type and omit Content-Length; validators mirror cached 200  
* Encoding invariance (optional evidence): for the same canonical body, ETag identity and effective Content-Length are stable across accepted encodings (identity/gzip/br)  
* POST (dev harness): non-conditional; never returns 304

Acceptance (routing only). Acceptance is governed by HDE-Governance and Glow QA Guide (titles-only). This section does not list token names. Mechanics must have acceptance proofs for this route and any local capture harness that exercises it:

* canonical JSON and shared emitter use  
* deterministic output stability under determinism pins  
* when optional GET/HEAD/304 captures are taken, correct conditional-GET behavior captured as supplemental, non-authoritative evidence (authoritative A7 proofs remain on cataloged JSON success routes)

Evidence (records-only; machine mirror; same-PR rule):

* reader/dev/parity — harness vs CLI stdout byte-compare (expected empty)  
* canonical\_json/compare — canonical re-serialization compare (one LF)  
* (Optional, if GET exposed) transport/headers\_200, transport/headers\_head, transport/headers\_304, transport/encoding\_invariance

List titles/paths in Appendix D: Evidence Index and mirror 1:1 in artifacts/evidence\_index.jsonl (canonical JSONL, one LF) with sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor. Update human Index and mirror in the same PR, with path-proofs.

Routing (titles-only):

* Transport matrices & A7 policy: HDE-CLI-API-Vendor Ref / HDE-Governance  
* Ops endpoint posture: HDE-Governance §10.5  
* Domains, catalogs, canonical JSON rules: HDE-Schemas & Artifacts

Dev conjunction preview endpoints (dev harness only).

Routes (GET; dev harness):

* /dev/reader/conjunction

* /dev/sampler/conjunction

Gate (required). These endpoints MUST only be enabled when APP\_ENV is one of dev, test, or local, and they MUST be protected by the shared dev-admin gate.

Behavior (required).

* The endpoints MUST compute conjunction via the same resolved conjunction surface used by compat (conjunction\_public\_resolved), so that preview behavior matches the compat computation path.

* The endpoints MUST pass a rails environment derived from SAFE rails env vars (SAFE\_MODE and ALLOW\_NETWORK) into the conjunction resolution surface.

* When rails are closed and resolution would require network I/O, the endpoints MUST refuse (writer-style) and MUST not emit partial conjunction results.

* On success, the endpoints MUST emit canonical JSON using the standard emitter and MUST include a trailing newline.

Tests (required). tests/http/test\_dev\_conjunction\_endpoints.py MUST cover:

* 403 when APP\_ENV is outside the allow-list or when the dev-admin gate fails.

* 503 when rails are closed and resolution would require network I/O.

* 200 when rails are open and conjunction can be computed.

## **9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]**

Route. POST /api/compat/v1 (pair) — internal/admin surface (not public).

Probe-only route. GET /api/compat/v1 — fixed OK payload for local health probing; rejects request bodies; does not compute compatibility.

Prod gate (hard). If APP\_ENV=prod, /api/compat/v1 MUST return 404 (Not Found).

Input validation (POST; required). The compat handler MUST validate the provided pair IDs (a\_id/b\_id) against UID\_RE (compat handler UID regex) before resolution, and MUST return a typed 400 (Bad Request) on invalid or empty IDs (no 500 on empty IDs).

CORS disabled on dev harness.

Ownership (titles-only). Production transport matrices and public payload bytes are owned by HDE-CLI-API-Vendor Ref / HDE-Governance. Mechanics enforces wiring/determinism (single emitter, canonical JSON, AB↔BA/two-run) and does not duplicate public schemas or bytes.

Conjunction compute contract (internal; required). The engine MUST provide an internal conjunction computation surface (conjunction\_public) that produces a deterministic JSON envelope suitable for canonical emission.

* Canonicalization: conjunction\_public output MUST be emitted using the existing compat canonical JSON emitter path, not ad hoc JSON formatting.

* Determinism: repeated invocations over the same resolved inputs MUST yield byte-identical canonical JSON output.

* Pair normalization: the computation MUST normalize pair ordering so AB and BA inputs produce byte-identical canonical output after emission (AB↔BA identity).

* No new public transport: this is an internal surface. It does not introduce a new public endpoint or new public byte contract.

Birth-only no-user boundary (required for pre-App compatibility proof). The resolved conjunction surface MAY accept caller inputs that contain a complete birth tuple and no caller-supplied user identity. When no caller `person_uid`, `user_id`, app user ID, or DB-backed user BodyGraph is supplied, the boundary MUST derive deterministic internal metadata inside `engine/compat/compute.py` before strict compatibility compute. The boundary-produced internal identifier MUST stay internal and MUST NOT become a public route contract, public CLI flag, public Reader field, or caller obligation.

The accepted local proof for this boundary is a birth-only caller-input proof in which caller inputs include only `birthdate`, `birthtime`, and `location`, assert no `person_uid` and no `user_id` in caller objects, and prove AB↔BA stability. Existing internal user-ID flows remain valid internal flows and MUST NOT be weakened globally to satisfy no-user proof.

Public/admin separation remains unchanged. `/api/compat/v1` stays internal/admin, public Reader remains bands-only and numeric-free, and this boundary MUST NOT add a public compat route, new public flag, alternate serializer/emitter path, OPS action, governed evidence family, or PF-canon edit by itself.

Contract tests (required). tests/http/test\_compat\_endpoint\_contract.py MUST include a conjunction contract test that asserts:

* Same inputs, same bytes across two runs.

* Swapped-order inputs produce the same bytes (AB↔BA identity).

* The emitted bytes include a trailing newline (canonical JSON emission discipline).

## 

### **9.3.1 Compat identity-hash closure and evidence-index proof split**

Compat identity-hash artifact (required). When conjunction compat closure is proven, the governed compat artifact family MUST include `artifacts/compat/identity_hash.txt`, and the compat-scoped evidence target key for that family is `compat.conjunction.identity_hash`.

Evidence-index proof split (required). `tests/ops/test_evidence_index.py` MAY implement a compat/repo split as `COMPAT_TARGETS` and `REPO_TARGETS` only if all of the following remain true:

* the compat-scoped and repo-scoped assertions remain separately testable, including `test_evidence_index_has_required_compat_artifacts` and `test_evidence_index_has_required_repo_artifacts`

* the main CI lane continues to execute the full `tests/ops/test_evidence_index.py` module

* `test_write_if_changed_check_mode_fails_closed_for_missing_target` remains in the main-lane module coverage

* repo-wide evidence checks remain truthful and are not narrowed to compat-only coverage

Independent compat-only closure lane (required). A separate compat-only CI lane MAY be used to make conjunction closure independently auditable. When present, that lane MUST:

* run only the compat closure assertions for the conjunction identity-hash artifact family

* remain additive to the main CI lane rather than replacing it

* keep mirror-schema and bridge-consistency safeguards as repo-wide checks outside the compat-only lane

If the isolated lane is wired for the PR-01 compat closure slice, the dedicated job name is `compat-conj-pr01-closure`.

Compat closure proof (required). The compat-only closure assertions MUST continue to prove conjunction canonical-byte correctness and Evidence Index presence for the compat identity-hash artifact family.

### **9.3.2 Governed compat proof surface and rails posture**

When conjunction compat parity is proven for this internal/admin surface, the governing proof run MUST exercise `/api/compat/v1` directly and MUST NOT substitute `hdctl showcompat --source vendor` or any other vendor-open CLI path as the proof carrier for this compat surface.

Closed-rails posture (required). The governing compat proof run MUST execute under `SAFE_MODE=1` and `ALLOW_NETWORK=0`.

Harness shape (required). The proof MAY use an in-repo app client or equivalent direct route harness, but it MUST assert:

* AB↔BA byte equality for the emitted compat body  
* LF-terminated canonical JSON with no CRLF bytes  
* the governed compat artifacts remain part of the same PR and evidence-index refresh as the compat identity-hash family

### **9.3.3 EPIC030 PR-03 compat evidence and indexing family (records-only)**

Purpose. For the bounded compat evidence and indexing family, Mechanics records the repo-side proof responsibilities only. This family stays on existing compat/admin evidence surfaces and does not create a public route, new flag, new serializer path, public-surface redesign, or close-stage artifact family.

Required governed artifacts. The PR-03 family MUST include, at minimum:

* `audit/qa/hde-epic030/pr-03/category_order_binding.log` and its sibling path proof  
* `audit/qa/hde-epic030/pr-03/compat_identity_binding.log` and its sibling path proof  
* `audit/qa/hde-epic030/pr-03/compat_parity_binding.log` and its sibling path proof  
* `artifacts/narratives/key_table_10x2.snapshot.json` and its sibling path proof

Binding requirements. The category-order proof MUST bind the Magic-10 order and narrative-key-table linkage. The PR-03 family MUST be bound into the existing Human Evidence Index and Machine Mirror homes, including the hash sentinel and companion proof artifacts.

## **9.4 Internal ops: /internal/version (ops-only) \[Required-Now\]**

Purpose (normative). Operator surface for identity and provenance. Not a JSON success route and not A7-eligible (see HDE-Governance §10.5).

Behavior (prod posture).

GET 200\. Content-Type: application/json; charset=utf-8; Cache-Control: no-store; no ETag; Last-Modified absent; Vary optional.

HEAD 200 (parity). Mirrors GET validators; no body; Content-Length \== len(identity GET body); Content-Type \== GET.

Conditionals ignored. Requests with If-None-Match / If-Modified-Since are ignored; never 304\.

Pins. All captures/compares run with LC\_ALL=C, LANG=C, TZ=UTC.

Evidence (records-only; machine mirror):

* artifacts/ops/internal\_version/headers\_get.txt — raw GET headers (proves no-store, no ETag, correct Content-Type).

* artifacts/ops/internal\_version/headers\_head.txt — raw HEAD headers (HEAD 200; Content-Type==GET; Content-Length \== identity GET). Non-header diagnostic lines (if present) MUST be ignored by parsers.

* artifacts/ops/internal\_version/body\_get.json — exact LF-terminated GET body (six keys in frozen order) \+ artifacts/ops/internal\_version/body\_get.sha256.

* artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt — GET with If-None-Match (still 200).

* artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt — GET with If-Modified-Since (still 200).

* artifacts/ops/internal\_version/request\_chain\_manifest.json — deterministic request-chain manifest for this capture run (secret-free; indexable).

* artifacts/ops/internal\_version/two\_run\_identity.log — two-run identity \+ coupling proof (release\_id matches artifacts/math/release\_id.txt) and env pins reference.

Acceptance (routing only). Acceptance is governed by HDE-Governance (titles-only). This section does not list token names. /internal/version must have acceptance proofs for:

* GET 200 and HEAD 200 parity (no body; Content-Type \== GET; Content-Length \== len(identity GET body))

* conditionals ignored (never 304; conditionals still return 200\)

* required headers present (Cache-Control: no-store, Content-Type: application/json; charset=utf-8)

* forbidden headers absent (ETag absent, Last-Modified absent)

* identity body posture (exact six-key schema, no extras; frozen key order; UTF-8/no BOM; compact; exactly one trailing LF)

Routing (titles-only). Policy lives in HDE-Governance §10.5; transport matrices for success routes live in HDE-CLI-API-Vendor Ref (A7 not applicable here).

# 10\) Writer Surfaces (API)

Purpose. Provide minimal, idempotent writer endpoints (e.g., preferences) with strict schema validation and deterministic effects. Mechanics wires determinism and validation; public transport rules and error headers live in Governance/CLI-API (titles-only).

## **10.1 Contract (normative)**

Idempotent semantics. Repeating the same request produces the same effect and response semantics (no double-writes, no drift).

Strict schema. Requests MUST validate against the governing schema (titles-only to PF-Canon-HDE-Schemas & Artifacts). Unknown or extra keys are rejected (typed error).

Normalization. Where arrays represent sets, dedupe & ASCII-sort; category/channel IDs must be canonical (Magic-10 closed set; NN-NN min-first for channels).

Explicit inputs only. Writers do not read clocks/env/files and do not depend on locale.

## **10.2 Transport posture (titles-only; owned by Governance)**

Routing only. Transport behavior is governed in HDE-Governance §10 and matrices live in HDE-CLI-API-Vendor Ref. This guide does not restate headers or validator details.

Writers and errors:

* Cache-Control: no-store; no ETag.

* Errors: Content-Type: application/json; charset=utf-8; typed, numeric-free error bodies (see HDE-CLI-API-Vendor Ref error model).

* Writers have no HEAD/304 semantics.

Success endpoints (A7 proofs):

* Proofs run only on a cataloged Endpoint Catalog (JSON success) route (see HDE-CLI-API-Vendor Ref §5.6 / Appendix A).

* Details such as 200 ETag, cache policy, Vary, 304 omission rules, and HEAD parity are referenced by title in Governance; do not duplicate here.

Internal ops: /internal/version is operator-only, not A7-eligible; behavior is specified in HDE-Governance §10.5.

Acceptance (routing only; owned by Governance). Acceptance is governed by HDE-Governance and the public-byte contracts in HDE-CLI-API-Vendor-Ref (titles-only). This section does not list token names.

Writers and errors must have acceptance proofs for:

* no-store posture and “no validators on errors”

* typed numeric-free error envelopes

* correct separation between success-route transport proofs (A7 on cataloged JSON success routes) versus ops-only /internal/version posture

  ## **10.3 Determinism & safety**

Two-run identity (effect). Two identical writer invocations over the same state produce identical post-state and the same response semantics.

Order stability. Any JSON emission (if the writer returns a body) uses the Canonical Serialization Package (§4): UTF-8 no BOM, sorted keys, compact, one LF; arrays-as-sets deduped & ASCII-sorted; checks under LC\_ALL=C.

No RNG/time. Writers do not consult clocks or randomness; no non-deterministic merges.

## **10.4 Errors & logging (internal)**

Typed errors only. Writers emit only the typed error envelopes defined in HDE-CLI-API-Vendor-Ref (titles-only). This guide does not enumerate error codes.

Keys-only logs. Never log request/response bodies, header values, or secrets; redact references; bounded labels.

## **10.5 Validation (binary)**

* Schema pass: request validates; unknown/extra keys → fail (typed error).

* A7 writers posture: responses carry no-store, no ETag (titles-only to Governance).

* Idempotence: re-issuing the same request leaves state unchanged; response semantics unchanged.

* Canonical bytes (if body present): canonical re-serialization byte-compare passes (UTF-8/no BOM, sorted keys, one LF, arrays-as-sets).

* No locale/I/O: static/grep checks show no file/env/time use in writer modules.

  ## **10.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* artifact\_key: writers/no\_store\_headers — header proof (no-store, no ETag).

* artifact\_key: writers/schema\_validation — JSON-Schema validation log (unknown/extra → typed error).

* artifact\_key: writers/two\_run\_idempotence — two-run idempotence/effect proof.

* artifact\_key: canonical\_json/compare — canonical re-serialization compare (if a body is returned).

Each mirror record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered physical\_path, proof. Update the human Evidence Index in the same change; CI enforces human↔machine parity and path-proofs.

Routing (titles-only):

* Transport rules & error headers: PF-Canon-HDE-Governance (A7; writers/errors).

* Error shapes & public bytes: PF-Canon-HDE-CLI-API-Vendor-Ref.

* Schemas & canonical JSON: PF-Canon-HDE-Schemas & Artifacts.

Route (dev harness): /dev/writer/conjunction

Gate (required). This endpoint MUST only be enabled when APP\_ENV is one of dev, test, or local, and it MUST be protected by the shared dev-admin gate.

Behavior (required).

* The endpoint MUST compute conjunction via the resolved conjunction surface (conjunction\_public\_resolved).

* Pass-through on non-200: if the conjunction computation returns a non-200 response, the endpoint MUST return that response as-is, without wrapping it in a writer envelope.

* Writer envelope on success: if conjunction computation returns 200, the endpoint MUST wrap the conjunction result into a writer envelope with ok: true and writer metadata (including hash and route\_id).

* Route id constant: the writer metadata MUST include writer.route\_id \= dev.writer.conjunction.v1.

* Idempotence (required). The endpoint MUST build a request preimage using stable key ordering before hashing, so identical inputs yield the same writer hash across invocations.

Tests (required).

* tests/http/test\_dev\_conjunction\_http.py MUST cover /dev/writer/conjunction and include an idempotence check comparing repeated identical requests.

* tests/http/test\_endpoint\_catalog.py MUST assert that /dev/writer/conjunction and route\_id dev.writer.conjunction.v1 are present in the endpoint catalog.

### **10.6.1 Conjunction writer evidence family (dev harness only)**

Generation tool (normative). Canonical entrypoint: `python tools/evidence/generate_conjunction_writer_evidence.py`. The generator MUST reuse the existing dev writer and dev reader conjunction surfaces to produce governed writer proof artifacts. It MUST NOT widen the writer contract or turn the writer proof path into an A7 proof surface.

Required governed artifacts. The writer evidence family MUST include:

* `artifacts/writer/conjunction_write_readback.log`

* `artifacts/writer/conjunction_write_readback.log.path_proof.txt`

* `artifacts/writer/conjunction_writer_summary.json`

* `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

Writer proof posture (required). This family MUST prove:

* writer bytes two-run equality

* writer payload two-run equality

* writer-result and reader-readback equality for the conjunction proof path

Rails posture (required). The generator MUST NOT silently force open rails. It MUST require explicit caller-provided open rails for the proof run and fail before emission if that posture is absent.

Determinism env posture (required). The generator MUST preserve the conjunction identity env inputs that influence emitted bytes, including `ENGINE_TAG`, `RELEASE_ID`, and `PRODUCT_INVOCATION_TAG`, alongside the normal proof-run env needed for the conjunction capture.

Indexing family (required). The Human Index and Machine Mirror MUST carry explicit writer-family bindings for this evidence set. The canonical writer artifact keys are:

* `conjunction.writer.summary`

* `conjunction.writer.write_readback`

Any byte change to this family MUST refresh the corresponding Human Index, Machine Mirror, checksum, and path-proof companions in the same PR.

Chronology posture (required). Writer artifacts, their co-located path-proofs, and the changed index or mirror companion proofs MUST be regenerated with current chronology when bytes change. Backdated or stale chronology is a merge-blocking integrity failure.

Updater coupling (required). `python tools/evidence/update_evidence_index.py` MUST force-refresh the governed conjunction writer evidence artifacts and their co-located path-proofs during evidence regeneration whenever this family is part of the changed governed surface.

This updater-driven force-refresh MUST keep the writer-family chronology coherent with the Human Index, Machine Mirror, and the other same-run companion refreshes, rather than leaving stale writer-family timestamps after index regeneration.

Validation set (required when this family changes). Refreshing the conjunction writer evidence family MUST rerun and pass:

* `python -m pytest -q tests/http/test_dev_conjunction_http.py`

* `python -m pytest -q tests/http/test_endpoint_catalog.py`

* `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_conjunction_writer_evidence.py`

* `python tools/evidence/update_evidence_index.py`

* `python tools/evidence/update_evidence_index.py --check`

* `python tools/evidence/orientation_demo.py`

* `python tools/evidence/orientation_demo.py --check`

* `python tools/evidence/validate_evidence_paths.py`

* `python tools/evidence/check_lf_endings.py`

* `python ci/checks/check_mirror_schema.sh`

# 11\) Input Normalization & Validation Layer

Scope. Normalize IDs and validate payloads against schemas (titles-only to PF-Canon-HDE-Schemas & Artifacts). Mechanics wires the checks; it does not restate schemas here.

## **11.1 Viewer prefs (normative)**

Closed set & types:

* top\_category ∈ Magic-10 (frozen IDs; fixed order).

* weights contains exactly ten keys, one per Magic-10 ID; each value is an int 0..100.

* preset is optional and, when present, is drawn from a declared preset catalog (titles-only).

Zero-weight rule:

* If a weight is 0 for category X, candidates whose \#1 \== X are excluded (enforced in the sampler/ranker, §11.3).

Aliases & unknowns:

* Default alias policy \= OFF. Unknown IDs reject with a typed input error.

* If input aliases are explicitly enabled, they must normalize via the declared alias ledgers (titles-only to PF-Canon-HDE-Schemas & Artifacts A1/A4/A5). Outputs remain canonical.

Canonicalization (inputs). Input JSON is normalized to UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays-as-sets are deduped & ASCII-sorted. All byte checks run under LC\_ALL=C.

AB↔BA neutrality. Normalization MUST produce identical normalized forms for (A,B) and (B,A).

Normalization-side handoff helper. The viewer-prefs normalization module MUST expose `engine.validation.viewer_prefs.weight_for_candidate_top_category` as the repo-owned handoff helper from normalized viewer preferences to sampler/ranker behavior. The helper resolves the weight for a candidate's top category, fails closed for unknown category IDs, and does not exclude candidates itself. Candidate exclusion remains owned by the sampler/ranker mechanics in §11.3.

## **11.2 Validation (binary)**

* Completeness. weights includes all ten category keys; each value is int 0..100.

* Invalid shapes. Malformed/missing keys or floats ⇒ invalid\_prefs (typed error).

* Schema pass. Payloads validate against their owning schemas (titles-only to PF-Canon-HDE-Schemas & Artifacts).

* Canonical bytes. Re-serialize canonically and byte-compare (must match); one LF, no BOM/ANSI.

* ABBA check. Normalized forms for (A,B) vs (B,A) are byte-identical.

Routing (titles-only):

* Magic-10 IDs & order: PF-Canon-HDE-Schemas & Artifacts §2.6, PF-Canon-HDE-Math-Spec §5.1.

* Public Reader contract: PF-Canon-HDE-CLI-API-Vendor-Ref.

* Canonical JSON & pack: PF-Canon-HDE-Schemas & Artifacts §4.

* Governance tokens: PF-04 — §2.0 Acceptance Tokens.

## **11.3 Swipe Sampler & Ranker**

Purpose. Build a candidate pool that respects viewer weights (including the zero-weight rule) and then rank deterministically. Deterministic \= order-neutral (AB↔BA) and seedable (when used in dev/admin flows); seeds never affect public bytes.

### **11.3.1 Sampling & exclusion**

* Zero-weight rule. Exclude any candidate whose \#1 equals a viewer weight of 0\.

* Pool formation. Apply viewer eligibility filters (titles-only), then enforce diversity (§11.3.3) before ranking.

### **11.3.2 Scoring & ranking (deterministic)**

* Score function. Deterministic fixed-point combination across the ten categories (integer path), consistent with PF-01 rounding/banding (titles-only).

* \#1 influence. The other party’s \#1 may serve as a stable tie-break (integer/priority rule); the rule must be pinned and stable.

* Total order. Sort by the specified numeric direction, then break ties by ID comparator (ASCII) to guarantee a stable total order (§5).

* Seedability. Any stochastic element (if used in non-public flows) must be seedable & isolated; the seed does not alter public bytes.

### **11.3.3 Diversity acceptance (deterministic)**

* Sliding window: K \= 50\.

* Cardinality bound: at most N \= 2 share the same design fingerprint within the window.

* No recent repeats: none repeat from the last R \= 20\.

* Fingerprint. A deterministic function (titles-only to PF-Math/PF-Spec) used only for diversity checks (never exposed).

### **11.3.4 Dev-only sampling endpoint (optional harness)**

* Endpoint (dev-only). POST /api/sample/v1 with body containing viewer\_prefs{\<PREFS\_FIELDS\>} and optional seed:int.

* Response. List of candidate IDs only; the app hydrates details. If a seed was provided, echo it in meta.

* Determinism. With the same inputs/seed, the output is byte-identical; AB↔BA has no effect on ordering.

### **11.3.5 Validation & evidence (binary; path-agnostic)**

* Zero-weight exclusion demonstrably enforced.

* Stable order: ABBA and two-run proofs; comparator laws honored (see §5).

* Diversity checks: window K, bound N, and recent R constraints verified.

* Seed replay: identical inputs/seed → identical outputs; seed echoed in meta when used.

* Canonical bytes: outputs are canonical JSON (UTF-8 no BOM, sorted keys, compact, one LF).

* Evidence Index: append artifacts (sampler snapshots, seed replay logs) in the same PR; PF-12 machine mirror lines present with path-proofs.  
* Normalization-handoff evidence. Evidence generators that prove zero-weight handoff MUST call the repo-owned viewer-prefs handoff helper rather than a synthetic projection. The governed proof family MUST capture invalid viewer-preference failures, canonical normalization comparison, and zero-weight handoff into sampler/ranker behavior.  
* Same-PR binding. Those artifacts MUST include sibling path proofs, Human Evidence Index entries, Machine Mirror records, hash-sentinel refresh, and topology orientation refresh/check in the same PR that changes the evidence family.

Routing (titles-only):

* Scoring/banding/rounding rules: PF-Canon-HDE-Math-Spec.

* Public contract & transport: PF-Canon-HDE-CLI-API-Vendor-Ref, PF-Canon-HDE-Governance (A7).

* Canonical JSON rules: PF-Canon-HDE-Schemas & Artifacts §4.

### **11.3.6 Engine sampler core (pure-compute implementation)**

Scope (normative). The Dissolution sampler/ranker behavior described in §11.3 is realized in the engine as a pure-compute sampler core. Mechanics records both the canonical module/entrypoints and the behavioral contract so that future work can change internals without breaking determinism, eligibility, or harness behavior.

Canonical module and entrypoints. The canonical sampler core module lives at engine/sampler/core.py and exports the pure-compute helpers that implement the contracted behavior in §11.3:

* build\_candidate\_pool — constructs the in-memory candidate pool from viewer inputs and candidate feature records, enforcing zero-weight exclusion and eligibility filters.

* rank\_candidates — applies the deterministic ordering rules over the pool (weight, compat score, band priority, ID comparator) to produce a total order.

* sample\_and\_rank — the main helper used by dev/admin harnesses to build the pool, apply diversity where configured, and produce a ranked list of candidates.

CLI and HTTP sampler harnesses in this repo (including the dev/admin CLI sampler and the /internal/dev/sampler HTTP harness) MUST call these canonical helpers rather than reimplementing sampling or ranking logic locally. Mechanics treats engine.sampler.core as the single home for sampler/ranker behavior; harnesses add only I/O, env wiring, and evidence capture.

Pure-compute contract. The sampler core operates on in-memory data structures (for example, viewer profile, candidate feature records, sampler configuration, candidate pool entries, and ranked candidates) and returns new values only. It does not:

* perform file or network I/O

* read environment variables, clocks, or random sources

* mutate module-level state

Zero-weight rules and basic eligibility are enforced inside the core:

* candidates with weight \<= 0 are excluded from the pool before any other checks (zero-weight rule)

* minimum compat score and band-based filters (allowed/excluded bands) are applied according to the sampler configuration

* optional diversity markers and recency flags are carried through in the pool entries for later diversity phases

Deterministic ordering. Deterministic ordering in the sampler core is implemented by:

* preferring higher weight, then higher compat score

* applying a band priority derived from the canonical band ordering (for example, Glow \> Warm \> Open \> Cool, consistent with the BANDS tuple from compat thresholds)

* using the existing ID comparator (ASCII comparator over person identifiers) as the final tie-break to guarantee a total order, in line with the comparator laws in §5

These rules must be applied by rank\_candidates and any helper that produces a ranked candidate list. For a fixed viewer profile, candidate feature set, and sampler configuration, running the sampler core twice with the same inputs and determinism pins (LC\_ALL=C, LANG=C, TZ=UTC) MUST yield byte-identical ranked candidate sequences (two-run identity) and respect AB/BA sanity as described in §11.3.

Harness usage (routing only). Dev/admin CLI sampler and HTTP sampler harnesses MUST:

* construct their in-memory inputs (viewer profile, candidate feature records, sampler configuration) and then call sample\_and\_rank (or the equivalent composition of build\_candidate\_pool and rank\_candidates)

* treat any deviations from the canonical sampler core behavior (for example, alternative ordering or eligibility rules) as defects

Evidence and acceptance tokens for sampler behavior and sampler evidence families remain single-homed in HDE-Schemas & Artifacts, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics by title; this section records only that the sampler core behavior in §11.3 is implemented by the canonical engine.sampler.core module and its entrypoints and that all harnesses and evidence generators must call into that module under the determinism and closed-rails posture described elsewhere in this guide.

# 12\) Error Envelope & Token Set \[Required-Now\]

Purpose. Provide a central formatter for typed, numeric-free errors. Public error transport (writers/errors no-store, headers) lives in PF-Canon-HDE-Governance and PF-Canon-HDE-CLI-API-Vendor-Ref (titles-only). Identity/Meta content has been moved to §13 (Identity & Provenance Module) and §14 (Internal Meta Surface) to avoid duplication.

## **12.1 Error envelope (normative)**

* Shape (exact): {"ok": false, "code": "\<lower\_snake\_token\>", "error": "\<human message\>"} — only these keys.

* Canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; checks under LC\_ALL=C.

* Numeric-free & secret-free: never include stack traces, payload excerpts, header values, or secrets; keys-only logs (redacted).

* Deterministic mapping: the same condition always yields the same {code,error} pair; byte-stable across Reader and CLI.

## **12.2 Token set (lower\_snake; examples)**

The error-code set and the canonical token→message map are owned by HDE-CLI-API-Vendor-Ref (titles-only). This guide does not enumerate error codes. Mechanics requires only that error codes are lower\_snake, stable, and emitted deterministically through the shared presenter/emitter and canonical serializer.

## **12.3 Transport (titles-only)**

* Writers & errors posture: Cache-Control: no-store; no ETag; Content-Type: application/json; charset=utf-8 (PF-04).

* A7 success rules are not restated here (see PF-04/PF-05).

## **12.4 Acceptance (binary; tokens & evidence are titles-only)**

* Schema: envelope has exactly ok=false, code, error; no extras; LF-terminated, canonical JSON.

* Casing & map: all tokens are lower\_snake; the token→message table matches the golden map (exact bytes).

* Parity: the same error emitted by Reader and CLI is byte-identical.

* Two-run identity: re-emitting the same error twice produces bitwise-identical bytes.

* Transport coupling: when the envelope appears in writers/errors, headers match PF-04 (no-store; no ETag).

## **12.5 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)**

* artifact\_key: errors/token\_map — canonical token→message snapshot (golden).

* artifact\_key: errors/schema\_check — JSON-Schema check for the envelope.

* artifact\_key: errors/canonical\_check — encoding/key-order/compact/LF proof.

* artifact\_key: parity/errors\_reader\_cli — byte-equality for the same error via Reader and CLI.

Each mirror record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered physical\_path, proof; update the human Evidence Index in the same change; CI enforces 1:1 parity and path-proofs.

Routing (titles-only):

* Error shapes & code map ownership: PF-Canon-HDE-CLI-API-Vendor-Ref.

* Writers/errors transport posture: PF-Canon-HDE-Governance.

* Canonical JSON & mirror rules: PF-Canon-HDE-Schemas & Artifacts §4/§8.

* Engine identity & /internal/version: §13 and §14 (this guide does not duplicate those bytes).

# 13\) Identity & Provenance Module \[Required-Now\]

Purpose. Single production source of truth for engine and release identity. Production values are initialized once per cut, are read-only thereafter, and are consumed by production public and operator surfaces through the identity helpers. Production emit paths perform no direct identity environment reads.

Bounded compatibility identity (normative). A stable compatibility identity profile MAY exist for explicitly non-production compatibility and development harnesses. It is not a second production identity authority and MUST NOT supply production public or operator surfaces.

Injected-emitter seam (normative). Reader-emission helpers MAY accept identity keywords only as a sanctioned adapter or test-composition seam. Production defaults MUST originate from `identity_meta()`. Request data and environment identity keys MUST NOT select or mutate production identity at emit time.

## **13.1 Fields (read-only after freeze; stable key order)**

Expose and persist exactly these fields; no extras:

* engine\_tag — opaque engine identity string pinned at build.  
* build\_commit — VCS short SHA for bundled repo head at cut time (optional on public/ops; may be unset).  
* invocation\_tag — canonical short tag for the current Invocation (public meta carries the tag only).  
* invocation\_sha256 — SHA-256 of the UTF-8 bytes of `invocation_tag`, recomputed and verified against the governed Invocation record at evidence-generation time.  
* emitter\_sha256 — SHA-256 over the allow-listed presenter/emitter source captured at cut (evidence/admin; not public).  
* release\_id — lowercase hex-64 of sha256(canonical\_bytes("catalog/manifest.json")) computed at freeze-pack.

Source of truth (titles-only): release\_id derives only from the PF-12 pack manifest; Invocation tag and digest come from the governed Invocation record, with the digest recomputed from the UTF-8 tag bytes; engine\_tag, build\_commit, and emitter\_sha256 are taken from the build snapshot at cut. No request-time hashing.

## **13.2 Accessors**

* identity\_meta() → {"engine\_tag","invocation\_tag","release\_id"} — inserted into the public envelope before idempotence hashing (PF-01 §3.2).  
* identity\_admin() → {"engine\_tag","release\_id","invocation\_tag","invocation\_sha256","build\_commit","emitter\_sha256"} — for internal/admin surfaces (e.g., /internal/version, evidence capture).

  ## **13.3 Flow & constraints**

* Production authority. Production Presenter, Reader, CLI, and operator consumers call the production identity helpers; they do not read identity values directly from environment variables, request data, or flags.  
* Compatibility domain. Explicitly non-production compatibility and development harnesses MAY consume the bounded compatibility identity profile. That profile MUST NOT be presented as production identity or used to redefine release identity.  
* Injected-emitter composition. Adapter and test composition MAY provide explicit identity keyword values to the Reader-emission helper. Omitted values MUST resolve through `identity_meta()`. This seam MUST NOT perform request-controlled or environment-controlled identity discovery.  
* Preimage coupling. identity\_meta() enters the public preimage before idempotence\_hash is computed (PF-01 §3.2).  
* Evidence coupling. The same production values flow into artifacts and audit evidence (titles-only); do not duplicate identity bytes in prose or ad-hoc files.

  ## **13.4 Prohibited**

* No recomputation of release\_id during request handling.  
* No branching semantics for release identity. If any operator surface implements a fallback path (for example, when a precomputed release-id artifact is unavailable), that fallback MUST still use the single definition: release\_id \= sha256(canonical\_bytes(catalog/manifest.json)). The hash input MUST be canonical manifest bytes (serializer-backed), not raw or non-canonical bytes, and MUST NOT create alternate release-identity semantics.  
* No mutation of production identity fields after freeze.  
* No alternative production identity sources from environment variables, flags, request data, or compatibility defaults on production public or operator paths.  
* No promotion of the bounded compatibility identity or injected-emitter seam into a second production identity authority.  
* No request-time hashing for emitter\_sha256 or invocation\_sha256.

  ## **13.5 Acceptance (binary; titles-only)**

* Two-run identity: two separately materialized collections from the production identity authority yield bitwise-identical canonical bytes.  
* release\_id recompute: equals sha256(canonical manifest bytes); recompute job passes.  
* Reader↔CLI parity: public bodies include identity\_meta() and remain byte-identical.  
* Emitter/Invocation identities: recorded emitter\_sha256 matches its build-time evidence capture, and invocation\_sha256 equals SHA-256 of the UTF-8 invocation-tag bytes recorded in the governed Invocation record.  
* Domain separation: production surfaces resolve through the production authority; the bounded compatibility profile remains confined to explicitly non-production compatibility and development harnesses.  
* Injection posture: omitted Reader-emission identity keywords resolve through production identity helpers, while explicit injection remains a bounded adapter or test-composition seam.

  ## **13.6 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

Scope (normative). Identity artifacts are records-only and MUST be listed by title/path in Appendix D: Evidence Index and mirrored 1:1 in artifacts/evidence\_index.jsonl. Mirror records are canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one trailing \\n) and include: artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor. Update the human Index and mirror in the same commit/PR; CI fails on mismatch or missing path-proofs. All captures run with LC\_ALL=C, LANG=C, TZ=UTC.

Independent two-run collection (normative). The identity provenance job MUST call the production identity authority separately for run 1 and run 2, canonicalize each complete result independently, and compare the resulting bytes before reporting PASS. Reusing one materialized byte string as both runs is insufficient.

Identity dependency closure (normative). Production identity authority, public and admin helpers, Reader, CLI, internal-version consumers, identity provenance primaries, release-id recomputation, and their directly dependent governed evidence form one dependency closure. A change to identity semantics or bytes MUST regenerate and recheck every affected consumer, primary artifact, Human Index entry, Machine Mirror record, checksum, and path proof before the identity family may report PASS.

Artifact keys (titles-only):

* pack/manifest — canonical manifest bytes (freeze pack).  
* identity/release\_id — frozen release\_id (64-hex).  
* identity/release\_id\_recompute — recompute proof log (on-disk equals canonical; sha256 over canonical bytes).  
* identity/emitter\_sha256 — presenter/emitter source hash (proves single shared emitter).  
* identity/invocation\_sha256 — verified digest of the UTF-8 invocation-tag bytes from the governed Invocation record.  
* identity/service\_identity — admin snapshot of production identity fields (JSON; LF-terminated; numeric-free).  
* parity/two\_run\_identity — independent two-run identity digest/log (byte-equal outputs; LF-terminated).

Mirror discipline (MUST):

* One JSON object per line; reject unknown keys in mirror records.  
* (artifact\_key, discovered\_physical\_path) in the mirror equals (title, path) in the human Index (strict 1:1 join).  
* A path\_proof.txt (or equivalent) is stored alongside each artifact and referenced by proof\_anchor.

Routing (titles-only):

* Pack/manifest & release\_id: HDE-Schemas and Artifacts §6.  
* Invocation & preimage rules: HDE-Math-Spec §3.  
* Transport ops surface: §14 Internal Meta Surface (policy owned by HDE-Governance).

# 14\) Internal Meta Surface \[Required-Now\]

## **14.1 Purpose & scope (normative)**

Operator-only, side-effect-free endpoint exposing engine identity for diagnostics. Single home: GET /internal/version.

## **14.2 Payload (exact fields; frozen key order)**

Expose exactly six provenance fields, no extras, in this frozen order:

* engine\_tag

* build\_commit

* invocation\_tag

* invocation\_sha256

* emitter\_sha256

* release\_id

Source of truth. Values originate from the Identity & Provenance Module (§13) and are read-only after freeze (see HDE-Schemas & Artifacts for release identity rules).

## **14.3 Transport (ops posture)**

* Cache-Control: no-store

* No ETag; Last-Modified absent

* Content-Type: application/json; charset=utf-8

* HEAD parity. HEAD /internal/version returns 200 and mirrors 200 validators (incl. Content-Type). Body is empty. Content-Length \== len(identity GET body).

* Conditionals ignored. If-\* validators are ignored. This endpoint never serves 304\.

* Vary: optional (MAY be present; not required for acceptance)

Policy owner: HDE-Governance. Mechanics reiterates here for ops wiring.

## **14.4 Posture**

* Operator-only; minimal payload; no secrets; no side effects.

* Body is canonical JSON (UTF-8/no BOM, compact, exactly one LF).

* Key order is frozen as in §14.2. Do not re-sort keys for this endpoint.

Auth posture is not yet canonized (normative constraint). PF canon does not yet define whether /internal/version is unauthenticated public, operator-network gated without auth, or auth-header required, nor the expected failure mode when access is missing or invalid. Until canonized:

* remediation guides and operational tooling MUST NOT state auth requirements for /internal/version as canon

* any statement about auth posture MUST be explicitly labeled as Observed Evidence (non-PF)

Canonization requires OPS discovery evidence that captures status line and headers for the canonical deployment context(s) under two conditions: (a) with no auth header, and (b) with the expected auth header present (value redacted or presence-only noted). Evidence MUST be secret-free and stored in-repo under a lowercase audit path consistent with the Ops posture in this guide.

## **14.5 Example (informative)**

Request: GET /internal/version

Response: 200 OK Cache-Control: no-store Content-Type: application/json; charset=utf-8

{"engine\_tag":"hdengine-x.y.z","build\_commit":"\<shortsha\>","invocation\_tag":"INV-\<TAG\>","invocation\_sha256":"\<64hex\>","emitter\_sha256":"\<64hex\>","release\_id":"\<64hex\>"}

## **14.6 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names. /internal/version must have acceptance proofs for:

* exact six-field payload shape and frozen key order

* canonical JSON bytes (single trailing LF)

* no-store posture with no validators

* HEAD parity and conditionals ignored behavior

## **14.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

* intver/headers\_get — raw GET headers (proves no-store, no ETag, correct Content-Type)

* intver/headers\_head — raw HEAD headers (200; Content-Type \== GET; Content-Length \== identity GET)

* intver/body\_get — exact LF-terminated GET body bytes \+ digest record

* intver/cond\_if\_none\_match — conditional GET (If-None-Match ignored → 200\)

* intver/cond\_if\_modified\_since — conditional GET (If-Modified-Since ignored → 200\)

* intver/two\_run\_identity — governed coupling \+ two-run identity log for /internal/version. It MUST include (a) an explicit two-run byte-identity result (with the compared digests) and (b) explicit coupling verification that the six /internal/version fields match their governing identity sources described in §13/§14. It MUST also include a rails/determinism pins reference (names-only) and remain secret-free.

Token naming (normative; non-aliasable). Acceptance token names for /internal/version MUST match the names defined in HDE-Governance (titles-only). Tools, guides, matrices, and acceptance maps MUST NOT invent aliases.

To prevent recurring alias drift, this guide names one token explicitly:

* Canonical conditional-semantics token name (conditionals return 200 and never 304): INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK

Any other name intended to mean the same invariant (including INTERNAL\_VERSION\_COND\_200\_NO\_304\_OK) is non-canon and MUST NOT be emitted or required in acceptance artifacts.

Internal version proof surface checklist (normative; MUST be explicit in probes). Any remediation guide, QA step, or probe tool that produces governed /internal/version evidence MUST explicitly enumerate and verify the canon-critical invariants below against the same captured bytes that are written as governed artifacts for that run. It is not acceptable to imply these checks by referencing PF sections only.

A. Transport

* GET MUST return 200\.

* HEAD MUST return 200 and satisfy parity expectations (no body; Content-Type \== GET; Content-Length \== len(identity GET body)).

* Conditionals MUST be ignored: If-None-Match and If-Modified-Since MUST NOT yield 304\. They MUST return 200\.

B. Headers

* Cache-Control: no-store MUST be present.

* Content-Type: application/json; charset=utf-8 MUST be present.

* ETag MUST be absent.

* Last-Modified MUST be absent.

C. Body (identity payload)

* Body MUST be fixed-schema JSON with exactly these keys (no extras): engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id.

* Body bytes MUST satisfy the identity-bytes posture for this endpoint: UTF-8 (no BOM), compact JSON, exactly one trailing LF, and frozen key order as defined by §14.2 (do not re-sort keys).

Token emission gating (no “false OK”). A tool MUST NOT emit any \*\_OK token unless the corresponding invariant above has been verified against the same captured bytes written as governed artifacts for that run.

If the run status is FAIL\_TOOLING (or equivalent), the tool MUST NOT emit \*\_OK tokens for invariants that did not pass. In particular, it MUST NOT emit “integrity success” tokens (for example, path-proof match or two-run identity) unless those checks demonstrably passed on the produced artifacts.

Coupling requirement (anti-mixed-target / anti-redirect drift). For each probe run, the emitted tokens, captured headers, captured body, and any two-run identity digest MUST refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit \*\_OK tokens.

Each mirror record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor. Update the human Evidence Index in the same change; CI enforces 1:1 parity and path-proofs.

## **14.8 Routing (titles-only)**

* HDE-Governance §10.5 — /internal/version policy (no-store, no ETag, conditionals ignored, HEAD parity)

* HDE-Math-Spec §3 — identity/preimage rules (single home for idempotence & identity semantics)

* HDE-Schemas & Artifacts §6 — pack/manifest coupling for release\_id

# 15\) Narrative Selection Router (keys only)

Purpose. Map viewer/context inputs to narrative keys without generating text.

Inputs:

* category

* band

* perspective (exactly one of: personal, shared)

* viewer\_top

* flags

Output: { personal\_key, shared\_key } — both drawn from the Narrative Key Registry.

Rules:

* Deterministic; no RNG.

* Never generates narrative text.

* If a mapping is missing ⇒ return missing\_narrative\_key (no fallback).

Routing & proofs (titles-only):

* Authoring DB plane (intake, lints, preview) and runtime file-backed pack (sealed; no DB in hot path) live in the Narratives Guide / Schemas & Artifacts.

* Mechanics proves determinism and parity (CLI \= HTTP), and records keys-only evidence in the same PR.

# 16\) Narrative Key Registry and Manifests

Purpose:

* Versioned registry guarantees exactly one key per (category, band, perspective).

* Manifests are diffable; no prose is stored in the engine.

* Build guard: fail the build if any mapping is missing or ambiguous.

Pack identity (routing):

* Identity is manifest-driven: pack\_sha \= sha256(canonical manifest bytes).

* Files are uploaded to immutable object storage at /narratives/\<pack\_sha\>/\<OBJECT\_PATH\>.

* Exporter/loader procedures and coverage policy are routed by title. Mechanics does not restate bytes here.

Registry diff and identity evidence mechanics (required).

* Narrative registry diff evidence MUST be generated by a repo-owned evidence generator. The generator MUST produce keys-only, no-prose registry diff evidence for manifest changes and pack identity evidence for the same family.  
* Registry diff generation MUST fail closed on missing or unexpected manifest paths, unsupported category, band, perspective, or slot values, duplicate tuples, duplicate keys, missing supported groups, and incomplete expected tuple-grid coverage.  
* Pack identity evidence MUST prove identity from canonical manifest bytes and same-bytes two-run stability. A lowercase 64-hex value is not sufficient identity proof unless the generator recomputes the expected hash from the final governed artifact bytes.  
* When the narrative registry diff or pack identity family changes, the governed sanity pipeline MUST run the registry diff generator and the registry diff generator check before Evidence Index update and Evidence Index check. Accepting stale registry diff or pack identity bytes through index checks alone is a mechanics defect.  
* Narrative loader and generator tests for this family MUST cover canonical rendering, keys-only/no-prose posture, pack identity, and fail-closed negative cases for malformed or unsupported registry state.

CLI Tooling \[Required-Now\]

Scope.

* The CLI uses the shared engine and the allow-listed presenter/emitter to produce public bytes.

* All byte checks run with LC\_ALL=C, LANG=C, TZ=UTC.

* Authoritative contract: the CLI must conform end-to-end to PF05-Canon-HDE-CLI-API-Vendor-Ref for commands/flags, payload shapes, error model, streams/exits, and help/version formatting (titles-only; PF05 governs).

* Admin preview posture. The narrative preview surface is enabled by default for admins across dev/stage/prod and uses the same emitter as Aux; bytes parity and LF discipline apply. Bytes and route live in PF05 by title.

## **16.1 Command catalog (titles-only; PF05 governs)**

Single home for commands. The complete CLI command/flag catalog and their status live in PF05 (for example, “Commands (by status)”, “CLI Overview & Conventions”). This guide does not enumerate all commands.

Conformance expectation. CLI help/usage, flags, and behavior must match PF05. Any divergence is a defect until corrected.

Examples (non-exhaustive):

* hdctl showcompat \<ARGS\> — prints the compat JSON payload (admin/test surface) to stdout as canonical JSON (UTF-8, sorted keys, compact, one LF) and, when invoked with \--dump-reader, writes the exact Reader v1 public body (six keys) using the shared presenter/emitter. Reader↔CLI parity is defined between the Reader API and the \--dump-reader output. CLI determinism (AB↔BA and two-run identity) is merge-blocking until the associated tokens are green.

* hdctl sample \<ARGS\> — prints the same deterministic selection/ordering as the corresponding Reader surface documented in PF05.

* Additional commands (for example, read singlebg, list people, disabled fetch \*) are defined and governed in PF05. This document only illustrates conformance expectations.

## **16.2 Streams & exits**

* stdout (success): public JSON body only, LF-terminated, no ANSI, no extra bytes.  
  * LF is required: success bytes MUST end with a single \\n and MUST NOT emit a payload that is missing the trailing LF.  
  * CRLF is forbidden: success bytes MUST NOT contain `\r\n`.  
  * No blank-line padding: success bytes MUST NOT contain `\n\n`.  
  * Stdout emission MUST be centralized through a single enforcement helper (for example `_emit_stdout_bytes`) that validates bytes before writing, to prevent bypass and double-write drift. Formatting violations MUST raise a typed CLI error (for example `STDOUT_MISSING_LF` or `STDOUT_CRLF`) and MUST exit non-zero.  
* stderr (failure): typed JSON errors only; diagnostics without secrets or PII; successful runs never write to stderr.  
* Exit code. MUST be non-zero on failure and MUST be consistent with the error envelope.  
* No mixed streams. A run is either stdout-only success or stderr-only failure; commands must not interleave diagnostics with public bytes.

## **16.3 Determinism & parity**

* Reader↔CLI parity. CLI stdout is byte-identical to the Reader 200 body for mirrored surfaces (single emitter).

* AB↔BA identity. Pair order neutrality holds for pair-sensitive inputs.

* Two-run identity. Identical inputs ⇒ identical bytes (single LF).

* Canonical JSON. UTF-8 (no BOM), ASCII-sorted keys, compact separators, one LF; arrays-as-sets deduped and ASCII-sorted (see §4/§10.1).

* Merge-blocking status. showcompat remains merge-blocking until the governing parity and determinism acceptance checks pass (titles-only; acceptance token registry and semantics live in HDE-Governance).

## **16.4 Inputs & schemas (titles-only)**

* IDs & catalogs. Validate against HDE-Schemas & Artifacts (§2.1/§2.6).

* Viewer prefs. \--prefs matches the closed 10-key weight map and top\_category ∈ Magic-10 (see HDE-Math-Spec §2.2/§5.x).

* Rails. Default SAFE rails; CLI must not open vendor rails unless explicitly configured (see §7.1/§7.3).

## **16.5 Installability & entrypoints**

* Console script. pyproject console-script hdctl present and installable.

* Module-run. python \-m engine.cli parity proven with console script.

* Packaging. Build/install in a clean env succeeds; help/version behave as specified.

## **16.6 Environment pins (runtime)**

* Pins. LC\_ALL=C, LANG=C, TZ=UTC; keys-only logs; no ANSI.

* Allow-list. CLI reads only documented env and fails-closed on unknowns (see §31.2).

## **16.7 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

Acceptance is governed by HDE-Governance and CLI contracts in HDE-CLI-API-Vendor-Ref (titles-only). This section does not list token names. CLI tooling must have acceptance proofs for:

* installability and entrypoint behavior

* stdout/stderr separation and exit-code posture

* determinism (AB↔BA neutrality and two-run identity) for governed commands

* Reader↔CLI parity where defined

* evidence/index discipline for CLI proof artifacts

## **16.8 Evidence (records-only; machine mirror; same-PR rule)**

List by title/path in Appendix D: Evidence Index and mirror 1:1 in artifacts/evidence\_index.jsonl (record fields as per §1.3). The machine mirror is canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF), rejects unknown keys, and each record includes a proof\_anchor to a co-located path-proof file. Update the human Index and machine mirror in the same PR.

Required artifacts:

* artifacts/cli/ab.json — canonical output for AB inputs (LF-terminated)

* artifacts/cli/ba.json — canonical output for BA inputs (must be byte-identical to AB)

* artifacts/cli/summary.json — canonical JSON with attempted commands, sha256 of ab.json / ba.json, and ab\_ba\_equal: true

* artifacts/cli/guards/emitter\_symbol\_proof.txt — single-emitter guard (presenter symbol)

* artifacts/cli/guards/serializer\_grep\_guard.log — grep-guard proving there are no ad-hoc serializers on public paths

* audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson — canonical JSON policy checks for CLI and evidence output.

* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson — canonical output comparisons

* audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json — structured canonical JSON gate record

Index human+machine in the same PR; mirror canonical JSONL; one LF; proof\_anchor present.

# 17\) CLI Components

## **17.1 Command catalog (titles-only; PF05 governs)**

Single home for commands. The complete CLI command/flag catalog and their status live in PF05 — HDE-CLI-API-Vendor-Ref (for example, “CLI Overview & Conventions”, “Commands (by status)”). PF14 does not enumerate or norm all commands; it records mechanical expectations and routes to PF05 by title.

Conformance expectation. CLI help/usage, flags, and behavior must match PF05. Any divergence between hdctl behavior and PF05 is a defect until corrected (or PF05 is updated).

Examples (non-exhaustive).

* `hdctl showcompat <ARGS>` — canonical compat harness for comparing two users and driving Aux narrative preview. On success, its primary success payload is a single compat JSON document on stdout (admin/test surface), emitted via the shared presenter/emitter as canonical JSON (UTF-8, ASCII-sorted keys, compact, one LF; no ANSI). When `--dump-reader <path>` is present, it also writes the six-key Reader v1 success envelope to `<path>` using the same emitter; those bytes must be byte-identical to the Reader 200 body for the same inputs/environment. The command remains merge-blocking until the compat JSON determinism and Reader↔CLI parity tokens are passing.

Additional commands (for example, read singlebg, list people, bg:resolve, and disabled fetch variants) are defined and governed in PF05, including whether they are Required-Now or Speculative. Implement and test them according to PF05 without redefining schemas or bytes here.

## **17.2 Streams & exits**

* stdout (success): public JSON body only, LF-terminated, no ANSI, no extra bytes.

* stderr (failure): typed JSON errors only; diagnostics without secrets or PII; successful runs never write to stderr.

* Exit codes:

  * 0 — success (canonical payload on stdout only).

  * 64 — usage error (bad flags/arguments; synopsis to stderr; stdout empty).

  * Other error codes are non-zero and command-specific as defined in PF05; in all cases stdout remains empty on failure.

* No mixed streams. A run is either stdout-only success or stderr-only failure; commands must not interleave diagnostics with public bytes.

## **17.3 Determinism & parity**

* Reader↔CLI parity. For each mirrored surface where the CLI emits a corresponding success body, CLI stdout is byte-identical to the Reader 200 body for the same inputs/environment (single shared presenter/emitter). Acceptance authority for determinism and canonical JSON is owned by HDE-Governance and the public surface contracts in HDE-CLI-API-Vendor-Ref (titles-only).

* AB↔BA identity. For pair-sensitive inputs, swapping the parties (A/B) yields identical outputs once normalized.

* Two-run identity. Repeating the same command with identical inputs and environment yields byte-identical stdout (single LF).

* Canonical JSON. All success payloads use canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF. Arrays used as sets are deduped and ASCII-sorted (see PF14 §4/§10.1).

* Merge-blocking status. hdctl showcompat remains merge-blocking until the governing parity and determinism acceptance checks pass (titles-only; acceptance token registry and semantics live in HDE-Governance).

## **17.4 Inputs & schemas (titles-only)**

* IDs & catalogs. CLI commands that accept IDs or cataloged names validate them against HDE-Schemas & Artifacts (§2.1/§2.6). This guide does not duplicate schema bytes.

* Viewer prefs. \--viewer-prefs-file / \--prefs flags must carry the closed 10-key weight map with top\_category ∈ Magic-10 and weights for all ten Magic-10 categories (see HDE-Math-Spec §2.2/§5.x). PF05 owns the exact CLI flag shapes.

* Rails. CLI runs under SAFE rails by default and must not open vendor rails on its own. Any command that can reach vendor or external HTTP must honor the rails and override semantics defined in PF04/PF07/PF05 (§7.1/§7.3 here, and the rails sections in Governance/Infrastructure).

### **17.4.1 showcompat conjunction mode (mechanics only)**

PF05 owns the exact flag spellings, accepted payload shapes, and CLI bytes for conjunction mode. PF14 records the mechanics requirements for the conjunction execution branch only.

* `hdctl showcompat` MUST provide a conjunction branch that delegates to the resolved conjunction surface (`conjunction_public_resolved`) rather than introducing a parallel compute path.

* The conjunction branch MUST accept exactly one complete conjunction input family per invocation, using the existing showcompat input families routed by PF05. Mixed, incomplete, or mutually incompatible conjunction inputs MUST fail deterministically on the normal CLI failure path, with non-zero exit, stderr-only failure output, and empty stdout.

* Before emission, the conjunction branch MUST canonicalize pair ordering so equivalent A/B and B/A inputs produce byte-identical success output under the determinism pins in this guide.

* When required local BodyGraph inputs are missing, the conjunction branch MUST honor SAFE rails. Closed rails MUST refuse deterministically, without network I/O and without partial conjunction output. Open rails MAY resolve through the existing resolver path under the policy owned by HDE-Governance and HDE-CLI-API-Vendor-Ref.

* Source-resolution and payload-normalization failures in the conjunction branch MUST surface as deterministic typed CLI failure classes via the standard CLI error path. The conjunction branch MUST NOT leak unexpected exceptions or configuration-specific stderr.

* On success, the conjunction branch MUST emit canonical JSON through the shared presenter/emitter, with exactly one trailing LF and no stderr bytes.

Required tests.

* `tests/cli/test_cli_canonical_bytes.py` MUST cover conjunction-mode canonical stdout emission and deterministic closed-rails refusal when local inputs are missing.

* `tests/cli/test_showcompat_sources.py` MUST cover deterministic conjunction-mode failure surfacing for DB/query and invalid-payload classes.

## **17.5 Installability & entrypoints**

* Console script. The pyproject console-script entrypoint hdctl is present and installable.  
* Module-run. `python -m engine.cli` behaves identically to the console script; parity is required for help, version, and command invocation.  
* Deterministic installability proof. The CLI conformance tooling MUST be able to produce positive installability proof in a clean environment using a deterministic editable-install path. When this proof path is exercised, it MUST run with `PIP_NO_INDEX=1`, `--no-deps`, and `--no-build-isolation`, and it MUST fail closed if the installed `hdctl` console entrypoint is absent from the interpreter scripts directory.  
* Positive help and version proof. Installability proof is not complete unless both the console entrypoint and the module runner return help and version successfully with exit 0, stdout output, and no stderr noise, as routed by PF05.  
* Single-sourced installability metadata. The installability proof artifacts MUST report one coherent console-entrypoint result and MUST NOT write duplicate or conflicting help or version payloads across summary and installability outputs.

## **17.6 Environment pins (runtime)**

* Pins. All CLI acceptance jobs run with LC\_ALL=C, LANG=C, TZ=UTC. Logs are keys-only, with no ANSI escapes.

* Env allow-list. The CLI reads only documented environment variables and fails closed on unknown or malformed env that would affect behavior (see PF14 §31.2 and PF05 env/flags sections). Secrets are never echoed.

## **17.7 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

Acceptance is governed by HDE-Governance and CLI contracts in HDE-CLI-API-Vendor-Ref (titles-only). This section does not list token names. CLI components must have acceptance proofs for the same categories described in §16.7 (installability, streams/exits, determinism/parity, and evidence discipline), without PF14 enumerating token rosters.

## **17.8 Evidence (records-only; machine mirror; same-PR rule)**

CLI components share the core evidence discipline:

* List each CLI evidence artifact by title and path in Appendix D: Evidence Index.

* Mirror artifacts 1:1 in artifacts/evidence\_index.jsonl (record fields as per PF12 and §1.3).

* Ensure the machine mirror is canonical JSONL (UTF-8, ASCII-sorted keys, compact, one LF), rejects unknown keys, and includes a proof\_anchor to a co-located path\_proof file.

* Update the human Index and machine mirror in the same PR; CI fails on mismatch, non-canonical JSONL, unknown keys, or missing path-proofs.

Required artifacts for the CLI parity and serializer-coupling harness include:

* Parity harness artifacts:

  * artifacts/cli/ab.json — canonical output for AB inputs (LF-terminated).

  * artifacts/cli/ba.json — canonical output for BA inputs (must be byte-identical to AB).

  * artifacts/cli/summary.json — canonical JSON summarizing attempted commands, sha256 of AB/BA, and an ab\_ba\_equal: true marker.

* Serializer and emitter guard artifacts (canonical homes; see §37.6):

  * artifacts/cli/guards/serializer\_grep\_guard.log — grep guard log proving there are no ad-hoc serializers on governed CLI public paths.

  * artifacts/cli/guards/emitter\_symbol\_proof.txt — emitter symbol proof snapshot for governed CLI handlers, including the optional aux-preview exemption.

* Canonical JSON policy and compare logs:

  * audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson — canonical JSON policy check log.  
  * audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson — canonical JSON compare log.  
  * Legacy (compatibility-only; non-authoritative): audit/gates/canonical\_json/json\_canonical\_check.log

Copies of the guard artifacts under audit/gates/guards/\*\* may exist for internal audit workflows, but those paths are secondary. Mechanics treats artifacts/cli/guards/\*\* as the canonical homes for CLI serializer/emitter guards; indexing and mirror records must use those canonical paths as discovered\_physical\_path, consistent with §37.6 and §1.3.

## **17.9 Stateless JSON QA mode (informative)**

Status: Informative, non-gating. This section records a future mechanics requirement from HDE-Build Notes (Addendum 11\) for a no-DB, stateless JSON QA mode. It does not add any new acceptance gates for the current engine or CLI posture.

### **17.9.1 Background and scope**

HDE-Build Notes observes that, in pre-Glow environments:

* There is no app-level user model or user IDs.

* There are no persistent user-bound BodyGraphs in production.

* We must not create app-like user records in production ahead of Glow App integration.

* Many earlier QA flows assumed DB-backed users (for example, showcompat \--user-a/--user-b \--source=db, bg:resolve \--source=vendor \--upsert), which cannot run under these constraints.

Current mechanics in this guide assume DB-backed flows for:

* CLI commands that resolve or store BodyGraphs via DB (or vendor+DB).

* Evidence capture tied to DB posture and runtime environment.

This section does not change those flows. It describes the additional stateless capabilities that a future epic is expected to add so that engine math can be exercised purely via CLI plus files, without DB.

### **17.9.2 Required capability: no-DB JSON QA mode**

Addendum 11 in HDE-Build Notes introduces a future requirement for a stateless JSON QA mode, consisting of three mechanical capabilities.

a) Stateless BodyGraph export. A future CLI flow must:

* Accept only birth data or vendor JSON (no user IDs, no DB lookup).

* Call engine math directly, without DB.

* Emit a canonical JSON BodyGraph export containing:

  * Raw birth/event details needed to reconstruct the chart.

  * Full BodyGraph topology (centers, gates, channels, lines, profile, authority, definition, type).

  * Stable identifiers consistent with the domain catalogs (IDs only; no prose).

* Write canonical JSON governed by HDE-Schemas and Artifacts (UTF-8, no BOM, ASCII-sorted keys, compact, exactly one LF, arrays-as-sets deduped then ASCII-sorted).

b) Stateless compat export. A future CLI flow must:

* Accept two BodyGraph JSON files or two birth tuples.

* Compute compat and Reader v1 envelopes directly, without DB.

* Write canonical JSON compat output and Reader envelopes under governed paths.

* Preserve determinism and AB↔BA parity using the same canonical serializer and comparator rules defined in this guide (§4/§5/§6).

c) Stateless vendor-to-engine pipeline. A future CLI-driven pipeline must support: birth → vendor fetch (dry-run) → BodyGraph JSON → compat \+ Reader JSON.

Each stage must:

* Be invokable via CLI.

* Write only JSON files and logs under governed paths.

* Perform no DB writes, unless an explicit upsert path is chosen (and that upsert remains clearly separated from stateless QA flows and governed by vendor/DB posture sections (§19/§20) and Governance).

Mechanics does not define specific command names, flags, or paths for these flows. It records that when implemented, they must reuse the shared emitter, canonical serializer, comparators, and deterministic engine posture defined in this guide.

### **17.9.3 Single homes for schemas and flows**

This guide records the mechanical requirement only. Ownership remains:

* HDE-Schemas and Artifacts — JSON schemas and artifact catalogs for stateless BodyGraph, compat, and any run-bundle exports.

* HDE-CLI-API-Vendor-Ref — CLI command shapes and behavior for stateless flows.

* Glow QA Guide and HDE Phased Epics — QA plans and acceptance wiring for stateless QA mode.

Mechanics MUST NOT define concrete paths or JSON schemas for these artifacts; it references the owning documents by title only.

### **17.9.4 Normative status and gating**

Until the stateless JSON QA mode is implemented and drained into the relevant PF documents:

* No acceptance token may treat the presence or absence of stateless JSON QA artifacts as a gate.

* PF14’s normative mechanics remain those of the current DB-backed engine and CLI flows.

* QA plans that cannot rely on DB users SHOULD:

  * call out “no user IDs / no DB users” as an environment constraint

  * use birth-based and vendor dry-run patterns described in HDE-Build Notes and the QA documents, while continuing to satisfy all existing determinism and evidence checks defined in this guide.

## **17.10 Interim no-user QA mode (pre-Glow prod)**

Status (normative). This section is normative for pre-Glow production environments where there is no app-level user model and no persistent user-bound BodyGraph rows configured in the database. It constrains how existing mechanics are exercised in Live QA. It does not change the long-term semantics of DB-backed flows, which will be re-opened in a future epic once the Glow App is integrated (see HDE Phased Epics and Glow QA Guide by title).

Assumptions (pre-Glow prod).

* No app-level user IDs exist in production.

* No persistent user-bound BodyGraphs exist in production.

* Mechanics and QA MUST NOT create app-like user records in production ahead of Glow App integration.

### **17.10.1 Compat & Reader (prod QA)**

For Live QA and implementation-validation work in pre-Glow prod:

* hdctl showcompat MUST be exercised with birth arguments only when the proof claim is no-user or pre-App compatibility. Allowed caller or command inputs for the controlled vendor-backed no-user smoke are:  
  * `\--source vendor`  
  * `\--birthdate-a`  
  * `\--birthtime-a`  
  * `\--location-a`  
  * `\--birthdate-b`  
  * `\--birthtime-b`  
  * `\--location-b`  
* Forbidden caller or command inputs for the controlled vendor-backed no-user smoke are:  
  * `\--user-a`  
  * `\--user-b`  
  * `\--a-user`  
  * `\--b-user`  
  * app user IDs  
  * `user_id`  
  * `person_uid`  
  * DB-backed user BodyGraphs as caller input  
  * `\--source db`  
  * any inline secret value  
* Proof classes MUST remain separate:  
  * public numeric-free output proof  
  * internal/admin compatibility compute proof  
  * vendor-backed no-user behavior proof  
* The public or birth-facing compatibility path MUST NOT require caller-provided `person_uid`, `user_id`, app user IDs, or DB-backed user BodyGraphs as caller input.  
* Strict compatibility compute MAY remain internal only if a sanctioned no-user adapter or resolver boundary supplies deterministic internal metadata before compute.  
* Fixture-only `person_uid` injection or fixture-only `user_id` injection is not sufficient remediation for public or birth-facing no-user behavior proof.  
* Local pytest and grep checks MAY prove public numeric-free posture, canonicalization, serializer or math properties, and internal compute properties only when labeled as such. They MUST NOT be used as a substitute for vendor-backed no-user behavior proof when the claim is live behavior in the current pre-App no-user environment.  
* Rails posture for functional showcompat runs. Any Live QA step that executes showcompat in a context where BodyGraph data is not already available MUST run that step with vendor rails open so the vendor can be called. Closed rails must be treated as an expected blocker for functional showcompat runs under this limitation. This constraint applies until the Engine can store and replay BodyGraphs locally without vendor calls.  
* The rails change MUST be explicit and scoped to only the showcompat step or steps. After the step, restore the default rails posture.  
* showcompat requires arguments. hdctl showcompat MUST NOT be executed as a zero-argument command in QA runs. If showcompat is attempted under closed rails or without required arguments, classify the outcome as FAIL\_TOOLING or TOOLING\_BLOCKED for that step, not FAIL\_BEHAVIOR, and record the rails posture and failure signature in primary.log. The authoritative command and argument contract is owned by HDE-CLI-API-Vendor-Ref.

OPS-01 discovery posture.

* OPS-01 is discovery-only. It may capture command/help output, presence-only environment state, command-candidate disposition, discovery-summary posture, and checksums for captured files.  
* If exact no-user vendor command proof is not proven, OPS-01 MUST classify the command proof as unresolved and the result as TOOLING\_BLOCKED, not FAIL\_BEHAVIOR.  
* `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt` MUST contain either a concrete no-secret no-user vendor command candidate or the exact unresolved sentinel allowed by the governing plan.  
* `audit/ops/hde-epic030/ops-01/discovery_summary.md` MUST state whether command discovery is proven or unresolved and MUST preserve any blocked or TOOLING\_BLOCKED posture truthfully.  
* `audit/ops/hde-epic030/ops-01/commands.txt` MUST record the discovery commands and any remediation edit actions actually performed.  
* `audit/ops/hde-epic030/ops-01/env_presence.json` MUST contain key names and booleans only. It MUST NOT contain secret values.  
* `audit/ops/hde-epic030/ops-01/files_sha256.txt` MUST cover the OPS-01 captured files except itself.  
* OPS-01 evidence is not QA PASS, not Live QA completion, not a PF09 status change, and not epic closure.

PR-01 discovery posture.

* PR-01 boundary/source-skew discovery MAY be read-only. If it is read-only, it MUST NOT claim implementation, test execution, vendor execution, QA PASS, OPS completion, PF09 status change, or epic closure.  
* The discovery report MAY establish current source facts such as the `compat_public` signature, current caller metadata posture, `normalize_pair` user-identity requirements, source/evidence skew, public Reader versus internal/admin compat boundary, existing no-user proof gaps, and safe follow-up loci.  
* Discovery findings MUST keep the public Reader numeric-free proof, internal/admin compat compute proof, and vendor-backed no-user behavior proof separate.

PR-02 local proof posture.

* PR-02 local implementation proof may satisfy the birth-only boundary at implementation-proof level when it proves all of the following:  
  * caller inputs contain only `birthdate`, `birthtime`, and `location`  
  * caller inputs contain no `person_uid`  
  * caller inputs contain no `user_id`  
  * boundary-produced internal metadata is created inside the resolver boundary and stays internal  
  * public Reader remains bands-only and numeric-free  
  * `/api/compat/v1` remains internal/admin  
  * no vendor command is run by Codex or any automated agent  
* The accepted local proof name for this posture is `test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable`.  
* PR-02 proves the local boundary only. OPS-02 validates the vendor-backed runtime path and MUST NOT re-litigate the PR-02 local proof unless current evidence contradicts it.

Controlled vendor-backed no-user smoke posture.

* A controlled PO manual vendor-backed no-user smoke is allowed only after command discovery and PR remediation.  
* The controlled smoke MUST be PO-only, IA-guided, use explicit open rails only for the vendor step, use no app user IDs, use no caller-provided `person_uid`, use no caller-provided `user_id`, store no secret values, capture only presence-safe secret posture, and avoid any guessed command, host, port, URL, service binding, target, or environment fact.  
* OPS-02 MAY execute the controlled vendor-backed smoke only after the exact command, safe secret posture, target facts, no-user input shape, explicit vendor source posture, PR-02 local proof, and PO proceed authorization are proven.  
* For the exact CLI vendor smoke shape, the target is the HD Engine CLI running in the PO-controlled execution context using the vendor source through HDAPI.  
* Required target facts for the exact CLI vendor smoke shape:  
  * command target: `hdctl showcompat`  
  * data source: `\--source vendor`  
  * execution context: PO-controlled terminal with `hdctl` available  
  * vendor binding: `HD_API_BASE_URL`  
  * deprecated vendor binding, if compatibility fallback is still present: `HDAPI_BASE_URL` as legacy drift only  
  * vendor base-url ambiguity handling: if canonical and deprecated values both exist and differ, fail closed before vendor execution  
  * vendor credential presence: `HD_API_KEY`  
  * geocoding credential presence, if required by the command path: `GEO_API_KEY`  
  * deterministic capture pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`  
  * open rails for the vendor step only: `SAFE_MODE=0`, `ALLOW_NETWORK=1`  
  * application environment for this controlled smoke: `APP_ENV=dev`  
* `HDE_BASE_URL` is not required for the exact CLI vendor smoke unless the command is changed to call an HD Engine HTTP service.  
* If a future attempt changes the target from CLI vendor execution to an HD Engine HTTP service call, that change requires a PF07-backed target fact set before execution.

OPS-02 command and preflight requirements.

* `audit/ops/hde-epic030/ops-02/vendor_command.txt` MUST contain a fully substituted executable `hdctl showcompat --source vendor` command with birth-only flags. It MUST NOT contain unresolved placeholder tokens before execution.  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json` MUST contain the birth values used in the command. OPS-02 MUST NOT invent substitute birth values while that file exists.  
* `vendor_command.txt` MUST contain no `\--user-a`, `\--user-b`, `\--a-user`, `\--b-user`, `user_id`, `person_uid`, inline secret value, or DB-backed user input.  
* The command MUST contain `\--source vendor`.  
* The execution wrapper MUST set `SAFE_MODE=0` and `ALLOW_NETWORK=1` for the vendor command only.  
* The execution wrapper MUST set `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.  
* `redacted_env_presence.json` MUST record presence booleans for `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` as applicable. If deprecated `HDAPI_BASE_URL` is present during a compatibility window, the evidence may record its presence as legacy drift or fallback evidence, but MUST NOT treat it as the canonical base-url key.  
* `request_summary.txt` MUST record PO authorization before the command runs.  
* If `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt` contains the unresolved sentinel, OPS-02 MUST stop as TOOLING\_BLOCKED.

Use this execution wrapper only after every OPS-02 preflight requirement above is satisfied:

`set +e; SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -lc "$(cat audit/ops/hde-epic030/ops-02/vendor_command.txt)" > audit/ops/hde-epic030/ops-02/stdout.json 2> audit/ops/hde-epic030/ops-02/stderr.log; printf "%s\n" "$?" > audit/ops/hde-epic030/ops-02/exit_code.txt`

Execution rules:

* Do not edit the command after a failed run to force a PASS.  
* Do not retry with different flags, URLs, hostnames, ports, credentials, or birth data unless the change is PF07-backed or HDE-Build Notes-backed and recorded in `result_summary.md`.  
* Do not run the command through Codex or any automated agent.  
* Do not persist secret values.  
* Do not treat an exit-zero run as QA PASS or epic closure.

OPS-02 required evidence outputs. OPS-02 completion requires these files under `audit/ops/hde-epic030/ops-02/`:

* `vendor_command.txt`  
* `sample_birth_inputs.json`  
* `redacted_env_presence.json`  
* `request_summary.txt`  
* `stdout.json`  
* `stderr.log`  
* `exit_code.txt`  
* `result_summary.md`  
* `pfcanon_ops02_completion_matrix.md`  
* `files_sha256.txt`

Required content:

* `vendor_command.txt` must contain the exact executable command used.  
* `sample_birth_inputs.json` must contain the birth values substituted into the command.  
* `redacted_env_presence.json` must contain key names and booleans only.  
* `request_summary.txt` must state that explicit vendor source was used, no `person_uid` was supplied, no `user_id` or app user ID was supplied, birth-only input shape was used, and PO proceed authorization was present.  
* `stdout.json` must contain command stdout, if any.  
* `stderr.log` must contain command stderr, if any.  
* `exit_code.txt` must contain only the command exit code and trailing LF.  
* `result_summary.md` must classify the outcome as exactly one of: PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED.  
* `pfcanon_ops02_completion_matrix.md` must map each OPS-02 prerequisite to its PF canon or HDE-Build Notes basis and evidence status.  
* `files_sha256.txt` must include hashes for all OPS-02 evidence files except itself.

OPS-02 outcome classification.

* PASS may be used only when all preflight rows pass, the exact command runs, `exit_code.txt` records `0`, the command uses `\--source vendor`, the command uses birth-only flags, no app user ID, `user_id`, or caller-provided `person_uid` is supplied, no secret values are persisted, `stdout.json` is non-empty and parseable as JSON unless the command’s documented success output differs, and `result_summary.md` states this is implementation-validation evidence only.  
* FAIL\_BEHAVIOR may be used only when all prerequisites are proven, the command runs, no tooling or secret failure occurs, and runtime behavior shows that vendor-backed compatibility cannot be computed from the birth-only no-user command.  
* FAIL\_TOOLING may be used when OPS-02 execution or evidence is contaminated or invalid as a tool run, including inline secret values, persisted secret values, guessed command changes after failure, user identity input, missing evidence files after an attempted run, or env capture that stores secret values instead of booleans.  
* TOOLING\_BLOCKED may be used when OPS-02 cannot safely run, including unresolved or placeholder-bearing command, missing or incomplete `sample_birth_inputs.json`, required vendor env presence false or uncaptured, missing `hdctl`, absent PO authorization, missing or contradicted PR-02 accepted birth-only proof, or an HTTP-service target change without PF07-backed target facts.

Expected adoption evidence for this remediation path includes:

* PR-01 boundary report  
* PR-02 targeted test report  
* absence of caller-provided `person_uid`, `user_id`, or app user ID from the public or birth-facing no-user proof  
* `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`  
* `audit/ops/hde-epic030/ops-01/discovery_summary.md`  
* `audit/ops/hde-epic030/ops-01/commands.txt`  
* `audit/ops/hde-epic030/ops-01/env_presence.json`  
* `audit/ops/hde-epic030/ops-01/files_sha256.txt`  
* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`

These evidence outputs may support remediation verification. They do not by themselves claim QA PASS, Live QA completion, PF09 status change, or epic closure.

QA MUST continue to verify:

* canonical JSON on stdout (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF)  
* AB↔BA identity using swapped birth tuples  
* Reader v1 envelopes via \--dump-reader, with Reader↔CLI parity proven via the shared presenter/emitter (§4, §8, §18)

These checks reuse the existing determinism and canonicalization rules in this guide and do not add new transport bytes, public routes, public flags, acceptance tokens, QA PASS claims, Live QA completion claims, PF09 status-change claims, or epic-closure claims.

OPS-02 observed completion bundle (records-only). The controlled vendor-backed birth-only no-user smoke for HDE-EPIC030 OPS-02 records an implementation-validation PASS posture, with command execution through `hdctl showcompat --source vendor`, birthdate, birthtime, and location inputs only, no caller app user ID, no caller `user_id`, and no caller-provided `person_uid`.

Observed OPS-02 evidence paths include:

* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/target_disposition.md`  
* `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`  
* `audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `audit/ops/hde-epic030/ops-02/execution_classification.md`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

Observed OPS-02 proof facts include exit code `0`, non-empty parseable JSON stdout, empty stderr, recorded stdout SHA-256, boolean-only redacted environment presence, `secret_values_detected=false`, `vendor_call_executed=true`, `command_source_was_ops01=true`, and PR-02 runtime binding present.

This observed bundle may support remediation verification and later checklist review language. It remains implementation-validation evidence only and does not by itself claim QA PASS, Live QA completion, PF09 status change, acceptance-map closure, close-pack completion, or epic closure.

OPS-02 observed completion bundle (records-only). The controlled vendor-backed birth-only no-user smoke for HDE-EPIC030 OPS-02 records an implementation-validation PASS posture, with command execution through `hdctl showcompat --source vendor`, birthdate, birthtime, and location inputs only, no caller app user ID, no caller `user_id`, and no caller-provided `person_uid`.

Observed OPS-02 evidence paths include:

* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/target_disposition.md`  
* `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`  
* `audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `audit/ops/hde-epic030/ops-02/execution_classification.md`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

Observed OPS-02 proof facts include exit code `0`, non-empty parseable JSON stdout, empty stderr, recorded stdout SHA-256, boolean-only redacted environment presence, `secret_values_detected=false`, `vendor_call_executed=true`, `command_source_was_ops01=true`, and PR-02 runtime binding present.

This observed bundle may support remediation verification and later checklist review language. It remains implementation-validation evidence only and does not by itself claim QA PASS, Live QA completion, PF09 status change, acceptance-map closure, close-pack completion, or epic closure.

### **17.10.2 Aux narratives (prod QA)**

For Aux preview in pre-Glow prod:

* hdctl aux-preview MUST consume compat JSON produced from birth-based showcompat runs as described in §17.10.1.

* QA MUST NOT rely on DB-backed users to exercise Aux; the Aux preview surface remains a file-based consumer of compat JSON in this mode.

### **17.10.3 BodyGraph resolver & vendor ingest (prod QA)**

In pre-Glow prod, BodyGraph resolver and vendor ingest QA flows MUST respect the following additional constraints (in addition to §19 Vendor Ingest Pipeline and §22 SAFE Rails and Provider Gate):

* CLI \--user arguments passed to bg:resolve MUST be treated as ephemeral QA keys only (for example, qa\_epic017\_resolve1, qa\_epic017\_vendor1) and MUST NOT be interpreted as real app user IDs.

* Under rails CLOSED, any bg:resolve \--source=vendor invocation MUST return a typed refusal and MUST NOT perform outbound HTTP.

* Under rails OPEN in pre-Glow prod, QA MAY run:

  * bg:resolve DB/auto stub checks (no real DB rows)

  * bg:resolve \--source=vendor \--dry-run to exercise vendor shaping and ingest metadata without writing DB rows

* bg:resolve \--source=vendor \--upsert MUST NOT be invoked in production until an app-level user model is live and a future epic re-opens user-bound DB coverage via HDE Phased Epics and Glow QA Guide.

These constraints are environment-specific; they do not change the long-term semantics of vendor upsert flows in dev or in future epics with a live app user model.

### **17.10.4 Evidence skeleton for CLI QA**

For Live QA sessions in pre-Glow prod:

* Mechanics MUST snapshot the Human Evidence Index and Machine Mirror before and after CLI QA runs that exercise showcompat, aux-preview, or bg:resolve in this mode.

* Any mutation of governed evidence artifacts (docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, or governed \*.path\_proof.txt) during such QA runs MUST be treated as a defect or unexpected side effect.

* CLI QA flows in this mode MUST NOT write governed evidence artifacts directly; they only consume the evidence skeleton defined in §1.3, §25, and §37, leaving governed paths unchanged.

### **17.10.5 Forward plan (routing only)**

Once the Glow App and user model are integrated, a future epic recorded in HDE Phased Epics and governed by the Glow QA Guide will:

* use real app user IDs to exercise DB-backed showcompat and bg:resolve \--source=vendor \--upsert in prod or stage

* close out any acceptance tokens that currently depend on DB-backed user flows (routing by title to HDE-Governance and HDE Phased Epics)

Until that epic is live, QA requirements that assume “existing users in prod” MUST be treated as blocked by environment and satisfied instead using the no-user QA mode described in this section.

## **17.11 Admin QA bundle surfaces (full product payload)**

Status (normative, admin-only). This section defines an admin-only bundle and its CLI/HTTP consumers for pre-Glow QA. The bundle is a single canonical JSON object that combines BodyGraph JSON, compat results, and Aux narratives for a match. It is intended for internal operators and PO only and is not a public Reader or app surface. Reader v1’s public covenant (bands-only, numeric-free, six-key envelope) and existing app-facing contracts remain unchanged and continue to be governed by HDE-CLI-API-Vendor-Ref, HDE-Math-Spec, and Glow QA Guide by title.

### **17.11.1 Admin bundle builder (internal module)**

Mechanics defines an internal admin bundle builder that:

* Accepts a canonical pair input in the same compat input space as the Compatibility Engine (§7.2) and the CLI showcompat harness: two parties (IDs, BodyGraphs, or births as permitted by the existing compat contract) plus viewer preferences (top category and weights across the closed Magic-10 set).

* Uses the existing BodyGraph resolver mechanics (titles-only to the BodyGraph resolver sections of this guide and to HDE-Schemas & Artifacts / HDE-Math-Spec) to obtain canonical BodyGraph JSON for each party, as already required for bg:resolve and related flows.

* Calls the internal compat math (titles-only to Category Framework and Compatibility Engine) to compute the per-category compat result over the closed Magic-10 set, at minimum:

  * category identity

  * integer score 0..100

  * band (Cool, Open, Warm, Glow)

  * narrative keys {personal\_key, shared\_key} consistent with the main compat contract

* Calls the Aux/Narratives system (titles-only to Narratives Guide and HDE Narrative Deliverables) to obtain three narratives per match:

  * a private A→B narrative

  * a private B→A narrative

  * a shared narrative

* Assembles a single in-memory admin bundle object with at least the following top-level keys (names are pinned here; detailed schemas remain in HDE-Schemas & Artifacts):

  * a\_bodygraph — canonical BodyGraph JSON for person A, as produced by the resolvers

  * b\_bodygraph — canonical BodyGraph JSON for person B, as produced by the resolvers

  * compat — the canonical compat JSON for the pair (categories in frozen Magic-10 order), where each category entry carries {id, score, band, personal\_key, shared\_key} and existing compat meta as defined by math and schemas

  * narratives — an array of exactly three Aux narrative compositions for this match (A→B, B→A, shared). Each narrative entry includes, at minimum, the composition identifier and pack SHA (or equivalent identity) plus the narrative text; the exact narrative payload schema remains single-homed in the Narratives documents

  * meta — build and environment metadata, including at minimum the engine identity (for example, engine\_tag, release\_id), invocation identity (for example, invocation\_tag or equivalent), and a names-only description of the bundle source and rails posture (for example, whether the bundle was built locally or via a prod route, and whether SAFE rails were closed or open). Detailed field schemas for meta remain single-homed in HDE-Schemas & Artifacts and HDE-Governance

The admin bundle builder is pure mechanics: it calls existing resolvers, compat, and Aux engines; it does not perform I/O, does not serve HTTP, and does not define transport or CLI flags.

Its output is serialized only via the canonical serializer (§4 / §10.1) when consumed by CLI or HTTP surfaces:

* UTF-8, no BOM

* ASCII-sorted keys

* compact separators

* exactly one trailing line feed

* arrays-as-sets deduped and ASCII-sorted

AB↔BA parity and two-run identity MUST hold for the admin bundle under determinism pins (LC\_ALL=C, LANG=C, TZ=UTC).

All scores, BodyGraph JSON, narrative keys, and narrative text carried in this bundle are admin/internal only. They must never be exposed as public Reader or app payloads and must not alter the public Reader contracts described elsewhere by title.

### **17.11.2 CLI admin bundle experience (any terminal → Railway prod)**

Mechanics requires that the CLI provide a repeatable admin bundle experience that can be run from any terminal capable of reaching the production Engine, subject to the usual secrets and rails posture governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide (titles-only).

The CLI admin-bundle flow MUST use the admin bundle builder described in §17.11.1 as its source of truth. It may be implemented either as:

* a dedicated aggregator command

* a documented harness/composition of existing commands (bg:resolve, showcompat, Aux preview), as long as the composition is mechanically defined and stable

The CLI admin-bundle flow MUST:

* accept a canonical pair input (fixture, births, or internal IDs consistent with existing compat/BodyGraph contracts)

* obtain the bundle by calling the Engine (directly or via the admin HTTP route described in §17.11.3)

* emit the bundle as canonical JSON on stdout or to a single bundle file, subject to:

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact separators

  * exactly one trailing LF

  * arrays-as-sets deduped and ASCII-sorted

The flow MUST be reproducible from:

* a Codespaces image used for HDE QA

* at least one clean local environment matching supported Python versions

This uses the same documented entrypoints described in the CLI sections of this guide and in HDE-CLI-API-Vendor-Ref.

Rails and env posture for this flow (SAFE rails, vendor behavior, secrets) remain governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide. PF14 requires that the CLI admin-bundle flow:

* respect SAFE rails and determinism pins (SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ) for any bundle generation used as evidence

* not bypass the allow-listed presenter/emitter, canonical serializer, or existing CLI parity and serializer guards (§4, §16, §17.3, §18)

Evidence for the CLI admin bundle experience (for example, bundle JSON artifacts and canonical-compare logs) must be captured and indexed under the existing evidence skeleton rules (§1.3, §25, §37); token names and QA acceptance rosters remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

### **17.11.3 HTTP admin bundle route (GUI consumer)**

Mechanics also requires an internal HTTP admin bundle route to serve the same admin bundle to a minimal Admin GUI.

The route is an internal admin/QA surface, not a public user route:

* it is not A7-eligible

* it is not a Reader v1 success route

* it is protected by whatever authentication and authorization posture is defined in Governance/Infrastructure (titles-only)

The route:

* accepts a canonical pair input (fixture, births, or internal IDs consistent with existing BodyGraph and compat mechanics)

* calls the admin bundle builder (§17.11.1) to construct the full product payload bundle

* returns JSON only, with no HTML, using the canonical serializer (§4 / §10.1) and determinism pins (LC\_ALL=C, LANG=C, TZ=UTC)

The Admin GUI (which may live in a separate repo) is expected to:

* call this route against the same production Engine on Railway that the Glow App will later use

* render BodyGraphs, compat categories with numeric scores and bands, and three narratives (A→B, B→A, shared) from the returned bundle

PF14 does not define the HTTP route name, auth model, or HTML/UX; those live in HDE-CLI-API-Vendor-Ref, Governance, and any Admin-UI epic records by title. PF14 only requires that such an admin bundle route exist, be wired to the admin bundle builder, use canonical JSON, and behave as an internal admin-only surface.

### **17.11.4 Posture vs Reader/App and evidence (routing only)**

The admin bundle surfaces (builder, CLI experience, HTTP route) are strictly admin QA and operator tools:

* They may expose BodyGraph JSON, per-category scores, bands, and narrative keys/text for internal use.

* They MUST NOT be used directly as public app routes or as replacements for Reader v1 or Aux public contracts. App integration continues to go through the Reader/Aux paths governed in HDE-Math-Spec, HDE-CLI-API-Vendor-Ref, Narratives Guide, and Glow QA Guide.

* All admin bundle captures and parity checks (for example, CLI vs HTTP bundle equality for the same inputs) must follow the existing evidence skeleton rules for canonical JSON, AB↔BA and two-run identity, and Index/Mirror parity (§1.3, §25, §37).

Any new tokens or epic-level acceptance criteria for admin bundle flows are defined in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics by title; PF14 does not define new token names here.

### **17.11.5 Authentication, authorization, and logging (admin surfaces)**

Status (normative, pre-Glow). The admin bundle surfaces defined in §17.11 (builder, CLI experience, HTTP route) are security-sensitive admin/QA tools. Mechanics requires that they be protected by real authentication and authorization, that successful calls be logged for audit, and that credentials be rotatable and revocable without code changes. Exact credential schemes and policies remain single-homed in HDE-Governance, Glow QA Guide, and Glow Infrastructure by title.

#### **17.11.5.1 Authentication and authorization (no open admin endpoints)**

Mechanics requires that:

* The CLI admin-bundle flow (§17.11.2) and the HTTP admin bundle route (§17.11.3) MUST NOT be callable without an admin credential. An unauthenticated request MUST NOT be able to obtain the full admin bundle.

* The admin credential (for example, a token or equivalent secret) MUST:

  * be stored as a secret under the infrastructure and governance policies described by HDE-Governance and Glow Infrastructure (for example, Railway secrets), not checked into the repo

  * be required on every admin bundle call (CLI and HTTP), using a transport mechanism and header/field semantics pinned in HDE-CLI-API-Vendor-Ref and HDE-Governance

* The same underlying authentication and authorization posture MUST apply to both admin surfaces:

  * CLI and Admin GUI both act as clients presenting the admin credential to the Engine

  * the Engine enforces that only authenticated and authorized admin callers may access the admin bundle route or equivalent CLI path

Mechanics does not pick specific header names or token formats; it requires that admin bundle surfaces are never open admin endpoints in production and routes the detailed auth model to HDE-Governance, Glow Infrastructure, Glow QA Guide, and HDE-CLI-API-Vendor-Ref.

#### **17.11.5.2 Logging and audit of admin bundle calls**

Mechanics further requires that every successful admin bundle call (CLI or HTTP):

* be logged with, at minimum:

  * a timestamp

  * a caller identity or account (for example, operator username, service account, or equivalent)

  * a high-level description of the input type (for example, “birth-based pair” vs “user-id pair” once user IDs exist, without logging raw birth details or other PII beyond what Governance allows)

  * a correlation identifier that can be used to trace the call across logs

* produce logs that are treated as operations logs and governed by the logging, retention, and PII rules in HDE-Governance and Glow QA Guide

Mechanics does not restate those policies; it assumes that any fields logged here comply with them.

Admin bundle logs must not capture secrets (credentials, tokens) or raw config values; they only record high-level audit information necessary for operational tracing.

#### **17.11.5.3 Credential rotation and revocation**

Admin credentials used for CLI and HTTP admin bundle surfaces MUST be:

* Rotatable without code changes:

  * credentials are loaded from environment or configuration governed by HDE-Governance and Glow Infrastructure

  * rotation of the secret value (for example, updating a Railway secret) does not require code deploys

* Revocable:

  * removing or changing the admin credential in the secret store MUST immediately prevent old credentials from successfully calling the admin bundle surfaces

  * tests and QA harnesses for admin surfaces MUST assume that credentials can change between runs and MUST NOT bake secrets into test fixtures

Mechanics does not define acceptance tokens for authentication, logging, or rotation; token names and QA playbooks (for example, admin-bundle auth required, CLI/HTTP parity, and “no open admin endpoints”) remain single-homed in HDE-Governance, Glow QA Guide, HDE-Build Checklist, and HDE Phased Epics by title. PF14 records the mechanical requirement that admin bundle surfaces are authenticated, logged, and backed by rotatable, revocable credentials in pre-Glow.

## **17.12 CLI as admin product surface (pre-Glow)**

Status (normative, pre-Glow). In the pre-Glow era, the canonical CLI (for example, hdctl or its module-run equivalent, as defined in HDE-CLI-API-Vendor-Ref) is a required admin-facing product surface, not just a dev/QA tool. A build that cannot be exercised via this CLI from a terminal that can reach the production Engine on Railway fails Mechanics requirements for pre-Glow “product usable by humans” posture.

### **17.12.1 Terminal scope (any shell → Railway prod)**

Mechanics requires that:

* The CLI be runnable from any shell that can reach the production Engine on Railway (and, where applicable, its DB), subject to the secrets and rails posture governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide (titles-only), not just from GitHub Codespaces.

* The same CLI mechanics defined in §16 and §17 (streams/exits, determinism, canonical JSON, parity) apply regardless of where the CLI is run (Codespaces, local machine, or other operator shell), provided environment pins and rails policy are satisfied.

* The CLI continue to respect all pre-Glow constraints recorded elsewhere in this guide and in Governance:

  * \--user remains an ephemeral QA key in pre-Glow prod; it is not bound to an app-level user model.

  * bg:resolve \--source=vendor \--upsert MUST NOT be used in prod until a future epic explicitly re-opens user-bound upsert flows.

  * Any flows that open rails or reach vendor APIs must follow the SAFE rails and vendor posture defined in HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide.

* This section does not add new commands or flags; it binds the existing CLI mechanics to a stronger product requirement: terminal CLI access to the Engine is part of the pre-Glow product surface.

### **17.12.2 Full product payload via CLI (within existing rails)**

Mechanics further requires that, in pre-Glow, the combination of CLI subcommands and harnesses defined in this guide and in HDE-CLI-API-Vendor-Ref be sufficient to obtain the full product payload for a match, consistent with:

* Compatibility engine math and banding (titles-only to HDE-Math-Spec and §7.2).

* BodyGraph resolver mechanics (titles-only to the BodyGraph resolver sections of this guide and to HDE-Schemas & Artifacts).

* Aux/Narratives behavior (titles-only to Narratives Guide and HDE Narrative Deliverables).

For a given pair input (fixture, births, or internal IDs allowed by existing contracts), an operator using only CLI subcommands (direct commands and/or a documented harness) can obtain, as structured output:

* per-person BodyGraph JSON

* compat results with bands and numeric scores over the closed Magic-10 set

* three narratives per match (two private, one shared), as already wired via the admin bundle builder (§17.11.1) and related Aux mechanics

These flows MUST operate within the pre-Glow rails posture described in §17.9, §17.10, §19.1, and in Governance/Infrastructure:

* When no user model exists, they rely on birth-based and dry-run vendor flows; they do not create app-like user records in prod.

* Any DB-writing flows remain governed by SAFE rails defaults and explicit rails-open windows as defined in Governance and Infrastructure; the requirement to support terminal CLI access does not relax those policies.

Mechanics treats the admin bundle surfaces in §17.11 as the preferred way to structure the full product payload for CLI, but does not require a single new command name. Whether the full payload is retrieved via a dedicated aggregator command or a documented composition of existing commands, the CLI must be able to produce the full product payload from a terminal in a way that satisfies the determinism, canonical JSON, and evidence discipline already defined in §4, §16, §17, §18, §25, and §37.

### **17.12.3 Evidence and planning (routing only)**

Evidence that terminal CLI access is a functioning product surface (for example, bundle JSON produced from a non-Codespaces shell hitting Railway prod, plus canonical-compare logs) must be captured and indexed under the existing evidence skeleton rules (§1.3, §25, §37). Mechanics does not define new artifact names or paths here; it routes titles and token semantics to HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

Epic-level planning and acceptance tokens for “CLI terminal access to full product payload” remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics. PF14 records the mechanical requirement that the CLI is a required admin product surface in pre-Glow and that its existing mechanics must support full product payload flows from any eligible terminal.

# 18\) CLI Serializer Coupling \[Required-Now\]

Scope. Force all CLI public bytes through the same allow-listed presenter/emitter entrypoint used by Reader. Tests must not bypass the unified entrypoint.

## **18.1 Policy (normative)**

Single entrypoint. CLI MUST route every public body through the shared presenter/emitter symbol (see §10.2).

Canonical rules apply. §4/§10.1 canonicalization (UTF-8; sorted keys; compact; one LF; arrays-as-sets) MUST hold for CLI stdout.

Surface parity:

* /api/compat/v1: CLI stdout is byte-identical to the Reader 200 body.

* /api/sample/v1: CLI stdout uses the same deterministic selection \+ ordering as Reader.

## **18.2 Prohibited (hard fail)**

Any ad-hoc JSON on public paths is prohibited: no json.dumps(, no jsonify(, no templating, no manual string building, and no pretty/indented output.

## **18.3 Guards (CI)**

Symbol allow-list. Maintain a code/CI allow-list of presenter/emitter symbols; only these may serialize public bytes.

Grep-guard. CI fails on public paths if ad-hoc serialization is detected (regex for \\bjson.dumps( and known alternates).

## **18.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names. CLI serializer coupling must have acceptance proofs for:

* shared presenter/emitter usage for public bytes

* prohibition of ad-hoc serialization on governed public paths

* determinism (AB↔BA and two-run identity)

* evidence/index discipline for guard artifacts and parity proofs

## **18.5 Evidence (records-only; machine mirror; same-PR rule)**

CLI serializer coupling evidence must demonstrate:

* AB↔BA and two-run identity for compat bytes under the shared presenter/emitter

* canonical JSON on CLI stdout for governed commands

* that governed CLI handlers use the allow-listed emitter and do not call ad-hoc JSON serializers

List evidence artifacts by title and path in Appendix D and mirror them 1:1 in artifacts/evidence\_index.jsonl (record fields as per §1.3). The machine mirror is canonical JSONL (UTF-8, ASCII-sorted keys, compact, one LF), rejects unknown keys, and each record includes a proof\_anchor to a co-located path\_proof file.

Required artifacts for CLI serializer coupling:

CLI AB/BA parity artifacts (parity harness):

* artifacts/cli/ab.json — canonical output for AB inputs (LF-terminated).  
* artifacts/cli/ba.json — canonical output for BA inputs (must be byte-identical to AB).  
* artifacts/cli/summary.json — canonical JSON with attempted commands, sha256 of ab.json and ba.json, and ab\_ba\_equal: true.  
* artifacts/cli/reader\_cli\_parity.bytes — canonical parity artifact proving the governed Reader 200 body and CLI showcompat bytes are equal on the shared presenter/emitter path.

Serializer and emitter guards (see §37.6 for guard tool behavior and roles):

* artifacts/cli/guards/serializer\_grep\_guard.log — grep guard report proving no ad-hoc serializers on governed CLI public paths.  
* artifacts/cli/guards/emitter\_symbol\_proof.txt — emitter symbol proof listing governed handlers and their allow-listed emitter symbols (with aux-preview explicitly exempt when it lists none).

Regression and index-target enforcement (required).

* `tests/cli/test_serializer_guards.py` MUST assert the emitted allow-list proof line for `artifacts/cli/guards/emitter_symbol_proof.txt`.  
* `tests/ops/test_evidence_index.py` MUST explicitly assert Human Index and Machine Mirror coverage for:  
  * `cli.guard.serializer_grep` \-\> `artifacts/cli/guards/serializer_grep_guard.log`  
  * `cli.guard.emitter_symbol_proof` \-\> `artifacts/cli/guards/emitter_symbol_proof.txt`  
  * `cli.showcompat.reader_cli_parity` \-\> `artifacts/cli/reader_cli_parity.bytes`

Canonical JSON policy and compare logs:

* audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson — canonical JSON policy checks for CLI and evidence output.  
* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson — canonical re-serialization compares for CLI parity and serializer coupling.

If audit/gates/guards/\*\* copies of the guard artifacts are present for internal audit workflows, they are secondary only. The artifacts/cli/guards/\*\* paths are the canonical locations for serializer/emitter guards; the Evidence Index and Machine Mirror must use those canonical paths as discovered\_physical\_path.

## **18.6 Routing (titles-only)**

Canonical serializer & unified entrypoint: §4 and §10.2.

Public payload/transport: HDE-CLI-API-Vendor Ref / HDE-Governance.

Domain catalogs & prefs schema: HDE-Schemas and Artifacts / HDE-Math-Spec.

# 19\) Vendor Ingest Pipeline — source policy & proofs (normative)

## **19.1 Policy (normative)**

Policy (env-aware).

* Prod. Source of truth is the database. Vendor APIs run only on explicit triggers or scheduled refresh; never inline on the request path.

* Pre-Glow prod (no users). When there is no app-level user model integrated with the HD Engine and no persistent user-bound BodyGraph rows configured in production:

  * Mechanics and QA MUST NOT create app-like user records in prod via CLI or vendor ingest.

  * bg:resolve \--source=vendor \--upsert MUST NOT be invoked in prod; QA and ops flows in this environment MAY use only DB/auto stub behavior and vendor dry-run semantics as described below.

* Dev. Direct vendor calls are allowed; on success, ingest MUST upsert the BodyGraph to DB for repeatability.

* SAFE rails. SAFE rails apply in all environments; rails posture and acceptance tokens are owned by HDE-Governance (titles-only).

BodyGraph I/O seam (normative). Mechanics treats BodyGraph resolution and ingest as a sanctioned I/O seam that is distinct from deterministic core compute.

HD Engine ownership for Glow app integration. Vendor acquisition, BodyGraph persistence, BodyGraph retrieval, and HD computation remain HD Engine mechanics. Glow app integration consumes HD Engine outputs through controlled integration surfaces; it must not duplicate HumanDesignAPI vendor-client behavior, vendor normalization mechanics, raw vendor credential handling, or canonical raw BodyGraph persistence in the app layer unless a future ADR and owning canon explicitly change that boundary.

Canonical seam location (implementation boundary). BodyGraph vendor and DB I/O is permitted only within the BodyGraph seam (currently implemented under engine/bodygraph/ in this repo). This seam is not part of the deterministic Engine Core or sampler core.

What may occur in the seam. Code inside the BodyGraph seam MAY perform:

* network I/O to vendor services (through a vendor client abstraction)

* DB reads/writes for BodyGraph storage (through a DB access abstraction)

Rails requirements for all I/O. Any network or DB I/O in the BodyGraph seam MUST:

* respect SAFE\_MODE and ALLOW\_NETWORK rails (no vendor calls when network rails are closed; fail-closed refusals when misconfigured)

* use a small, well-defined set of seam abstractions (for example, vendor client and DBAccess-like components)

* keep logs and artifacts secret-free (keys-only posture; no credentials and no vendor payload bodies in governed artifacts)

Purity preserved elsewhere. Deterministic decisions (eligibility, banding, compat math, narrative key selection, canonical JSON emission) MUST remain in the pure compute modules (core/sampler/compat/presenter/runtime) and MUST NOT be implemented inside the BodyGraph seam. The BodyGraph seam orchestrates I/O and normalization around those pure decisions.

This subsection does not redefine transport bytes, retry policy, or token semantics; it records the mechanical I/O boundary so audits and tests can enforce “no network/DB I/O leaks into core compute” while allowing BodyGraph resolution and ingest to operate under explicit rails.

Per-call selection (explicit). Source is chosen per call on operator surfaces (CLI flag / ops param); there are no engine “modes.”

Any unknown ENGINE\_\* env MUST fail fast with a typed error (no vendor I/O).

When rails are closed, any request that sets source=vendor MUST return a typed refusal and MUST NOT perform outbound HTTP.

In pre-Glow prod QA flows, CLI \--user values passed to bg:resolve MUST be treated as ephemeral QA keys only and MUST NOT be bound to real app user IDs; DB behavior remains stub-only until the Glow App is integrated.

When rails are OPEN in pre-Glow prod QA flows:

* bg:resolve DB/auto MAY be exercised in stub mode (no real DB rows)

* bg:resolve \--source=vendor \--dry-run MAY perform a single vendor call that returns ingest metadata and MUST NOT write DB rows

Routing and token semantics for per-call selection are owned by HDE-Governance and HDE-CLI-API-Vendor-Ref (titles-only).

Evidence (records-only). artifacts/bodygraph/source\_selection.snapshot.json capturing at least:

* app\_env

* attempted (requested source)

* selected (actual source used)

* reason (closed enum explaining selection/fallback)

* upserted (boolean indicating DB upsert)

Canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing \\n); unknown keys are rejected.

Source-neutral projection boundary (normative). DB-sourced mapped-cache data and configured-v2 vendor data MUST converge through one pure projection of already-mapped HDE data before emission through the shared Presenter.

The projection MUST:

* accept mapped HDE data only and reject raw vendor envelopes;  
* deep-copy accepted input without mutating its caller-owned source;  
* produce exactly `bodygraph`, `person`, and `person_uid` at the top level;  
* produce exactly `authority`, `birthDateUtc`, `centers`, `channelsLong`, `channelsShort`, `definition`, `gates`, `profile`, `strategy`, and `type` inside `bodygraph`;  
* require the top-level and nested person UIDs to agree;  
* remove the permitted source label and recursively reject transport, vendor, request, response, credential, header, raw-payload, database, SQL, token, and secret metadata;  
* fail with stable value-free classifications for missing fields, unknown fields, UID mismatch, invalid shape, and unsafe fields; and  
* perform no network, database, filesystem, clock, environment, random, logging, serialization, or persistence work.

The existing Presenter remains the sole byte authority. Projected values MUST be emitted through the shared Presenter. The projection MUST NOT create a second adapter, emitter, serializer, public route, transport contract, production identity, durable-write authorization, or public Reader change.

Source invariance (single presenter/emitter). For the same normalized input, independently acquired DB and configured-v2 vendor representations MUST produce equal source-neutral projections and byte-identical output through the shared Presenter.

The focused BodyGraph policy producer is the sole active primary writer for this source-invariance family. The governed primary paths remain:

* artifacts/bodygraph/source\_invariance/ab.json — DB-first run record using the v2 run schema.  
* artifacts/bodygraph/source\_invariance/ba.json — vendor-first run record using the v2 run schema.  
* artifacts/bodygraph/source\_invariance/summary.json — v2 summary and negative-control receipt.

A valid source-invariance PASS MUST derive all of the following from current inputs and outputs:

* distinct DB and vendor source identities;  
* distinct canonical source-representation hashes;  
* one equal normalized-input SHA-256;  
* two independently materialized runs for each source, each reopening, deserializing, mapping or projecting, and emitting independently;  
* stable projection and emitted-byte hashes across both runs for each source;  
* equal source-neutral projections;  
* byte-identical shared-Presenter output;  
* reversed DB/vendor acquisition order between AB and BA;  
* absence of unsafe fields;  
* closed-schema validation with unknown fields rejected;  
* canonical UTF-8 JSON with sorted keys, compact separators, no BOM, and exactly one trailing LF; and  
* a required negative receipt proving that mutation of the governed DB BodyGraph profile field produces `BODYGRAPH_SOURCE_DIVERGENCE` without embedding raw values.

Top-level PASS and every subordinate run status MUST be derived from the current predicates. Constants, copied claims, label comparisons, parsed-object equality in place of required byte equality, one materialization hashed twice, missing negative controls, duplicate current keys, stale companions, or a partial v1/v2 migration MUST fail closed.

`BG_SOURCE_INVARIANCE_OK` remains a non-token proof label. This mechanics family does not mint or satisfy an acceptance token.

Primary producers MUST NOT write sibling path proofs, the Human Evidence Index, the Machine Mirror, checksum sentinels, or topology/index companions. Those outputs remain owned by the canonical evidence updater and MUST be refreshed only after the final source-invariance primaries and release binding are stable.

Live vendor transport proofs (open-rails QA vs offline tests). For epics whose D-goals or QA acceptance explicitly require live vendor activity (for example, “prove that at least one flow hits the live vendor under open rails”), Mechanics adds the following mechanical requirements on top of the policy and evidence in this section.

Separation of offline ingest tests vs live vendor tests (normative).

Offline ingest tests (for example, unit/integration tests, dry-run pipelines, and source invariance proofs that never open vendor rails) are not sufficient on their own to satisfy “live vendor activity” D-goals. They remain necessary for correctness and invariance, but count as offline evidence only.

A live vendor transport proof requires at least one run in which the Engine/Reader or CLI:

* executes under open rails (for example, ALLOW\_NETWORK=1 with SAFE rails posture consistent with Governance and Infrastructure)

* actually sends a request from the Engine/Reader/CLI surface to a vendor endpoint, with the transport captured as governed evidence

Required elements of a live vendor transport proof (mechanics only). For any epic that claims live vendor coverage via this pipeline, Mechanics requires at least one governed evidence artifact (names and schemas single-homed in HDE-Schemas & Artifacts and Glow QA Guide) that records, at minimum:

* Rails snapshot at call time — a names-only env log for the live-vendor step (for example, a D0/Dn env snapshot) including at least SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, LC\_ALL, LANG, and TZ, so that auditors can see that the vendor call actually ran under open rails and determinism pins.

* Vendor endpoint and method — the vendor hostname, scheme, and path (for example, https://\<vendor\_host\>/\<path\> or equivalent) and the HTTP method used (GET, POST, etc.), with any secrets (API keys, auth tokens) removed or redacted per Governance.

* Request/response status and headers — a headers-only or structured log that captures:

  * the HTTP status code returned by the vendor

  * selected response headers (for example, Date, Content-Type, and vendor-specific rate-limit headers where allowed)

  * any vendor error codes or reason phrases that are needed to interpret the result

* Body visibility (names-only). Bodies MUST NOT be logged verbatim for vendor responses; when bodies are needed for debugging or QA, Mechanics requires that they be down-sampled or transformed into names-only or bounded summaries consistent with the logging posture in this guide and Governance. Raw vendor payloads and PII must not appear in governed live-vendor proof artifacts.

The exact artifact names, JSON shapes, and token mappings for these proofs are defined in HDE-Schemas & Artifacts, Glow QA Guide, HDE-Governance, and HDE-Build Checklist by title; this section records that at least one such artifact MUST exist for any epic that claims live vendor coverage through this pipeline.

Surfaces and harnesses (CLI vs HTTP). A live vendor transport proof may be obtained via either:

* a CLI surface that drives vendor ingest and records the evidence above

* an HTTP surface (for example, a Reader or internal admin route) that drives vendor ingest and is exercised by a QA harness

Mechanics requires that each epic’s QA plan declare which surface(s) are used for live vendor proofs (CLI and/or HTTP) and that the corresponding harness:

* uses the same Vendor Ingest Pipeline mechanics and source-selection rules defined in this section

* runs under clearly logged rails (closed vs open, SAFE rails posture)

* writes the live-vendor proof artifacts as governed evidence under the existing evidence skeleton (Index/Mirror, path-proofs, same-PR rule), using titles-only routing for schemas and directories

Pre-Glow constraints in §19.1 (no app-like users in prod, upsert disabled in pre-Glow prod, dry-run only in certain flows) remain fully in force; live vendor proofs must respect those environment rules and may use dry-run or non-upsert surfaces where required.

Routing (titles-only). The names and schemas for live vendor transport evidence families, their locations under artifacts/\*\* or audit/\*\*, and the acceptance tokens (for example, any “live vendor transport” or “open rails env” tokens) remain single-homed in:

* Glow QA Guide (QA plans and token evidence requirements)

* HDE-Phased Epics (epic-specific D-goals and acceptance)

* HDE-Build Checklist (build and QA gates)

* HDE-Schemas & Artifacts (artifact schemas and catalog entries)

PF14 records that, when an epic requires live vendor activity, Mechanics expects at least one open-rails vendor call to be exercised from an Engine/Reader/CLI surface using this pipeline, with the transport-level evidence and rails snapshot captured as governed artifacts under the shared evidence skeleton and indexed in the same PR as other ingest evidence.

Acceptance (routing only). Acceptance is governed by HDE-Governance and Glow QA Guide (titles-only). This section does not list token names. Vendor ingest must have acceptance proofs for:

* correct source-selection behavior by environment and rails posture

* refusal behavior when rails are closed

* invariance between equivalent DB-sourced and vendor-sourced bodies when emitted via the shared presenter/emitter

* evidence/index discipline for vendor ingest proof artifacts

## **19.2 Refresh, TTL & SWR (out-of-band; normative)**

Purpose. Pin the invariants for the BodyGraph refresh worker (EPIC-011), its policy, and the governed refresh policy snapshot. Mechanics, ADR values, and detailed schema live in the ADR, Build Notes, and HDE-Schemas & Artifacts; this section states the mechanical invariants only.

Guards (no inline vendor calls). A refresh worker MUST:

* run out-of-band, off the hot Reader path; it MUST NOT perform inline vendor calls for request-time reads

* respect all four guard classes:

  * TTL: when data becomes stale

  * SWR (stale-while-revalidate): when stale data may be served while a refresh runs

  * rate-limit: how often refresh attempts may be made

  * circuit-breaker thresholds and cooldown: behavior under sustained error conditions

Policy snapshot (v1, titles-only). The refresh policy is captured in the governed snapshot artifact: artifacts/bodygraph/refresh\_policy.snapshot.json. HDE-Schemas & Artifacts owns the path and JSON schema; PF14 references it by title only.

The snapshot uses a v1 nested schema pinned by ADR and tests:

* Top-level TTL/SWR fields (for example, ttl\_s, swr\_s).

* Nested objects:

  * rate\_limit.{requests\_per\_window, window\_s}

  * circuit\_breaker.{fail\_threshold, window\_s, cooldown\_s}

A sample\_counts block is attached to a copy of the policy, recording counters such as:

* refresh\_attempts

* refresh\_successes

* refresh\_failures

* breaker\_tripped

* rate\_limit\_hits

These values are enforced by governed evidence tests.

Worker alignment rule (POLICY ↔ snapshot). The refresh worker implementation in scripts/bodygraph/run\_refresh\_worker.py MUST:

* use a POLICY constant whose structure matches the v1 nested schema described above

* serialize that structure into refresh\_policy.snapshot.json (plus sample\_counts) using canonical JSON (UTF-8, sorted keys, compact, exactly one LF)

The worker MUST NOT reintroduce the legacy flat layout (rate\_limit: 60, cb.{\<FIELDS\>}) that predates the v1 schema. Any such regression would overwrite the governed snapshot with a schema that no longer matches the ADR and MUST be treated as out-of-policy.

Any future change to TTL/SWR, rate-limit, or circuit-breaker thresholds MUST:

* update the ADR and snapshot schema (HDE-Mechanics, HDE-CLI-API-Vendor-Ref, HDE-Build Notes) so they all describe the same v1-compatible policy

* update the refresh worker’s POLICY constant and its usages to match the updated schema and values

Guard tests (for example test\_refresh\_policy\_snapshot\_matches\_adr) MUST remain green; they enforce that the emitted snapshot matches the ADR-pinned policy and that the worker reads from the same nested fields it writes.

Determinism and environment. The refresh worker runs under the same determinism pins and SAFE-rails posture as other EPIC-011 jobs:

* Determinism: LC\_ALL=C, LANG=C, TZ=UTC.

* SAFE rails and vendor shaping policy remain governed by HDE-Governance and HDE-CLI-API-Vendor-Ref (titles-only).


# 20\) Persistence Layer (DB posture, partition & bridge) \[Required-Now\]

Scope (normative). Database mechanics for schema identity, runtime posture, partition stance, direct-only provider selection, retired-transport enforcement, and current-versus-historical evidence separation. Artifact schemas and indexing live in HDE-Schemas & Artifacts; governance tokens live in HDE-Governance and the Build Notes. PF14 owns the mechanics that produce and prove the posture.

## **20.1 DB posture mechanics (build-time identity)**

Objective. Capture the runtime DB schema, roles/grants, and boundary view posture in a deterministic way.

Mechanics MUST drive a posture harness that produces at least:

* artifacts/db/ddl\_fingerprint.json — Normalized DDL snapshot of the runtime schema with stable ordering.  
* artifacts/db/grants.txt — Baseline roles/grants listing.  
* artifacts/db/check\_schema.txt — Schema/search\_path echo and verification.  
* artifacts/db/check\_constraints.txt — Constraint checks (including FK, uniqueness, and any invariants called out in canon).  
* boundary\_view.readonly.proof — Proof artifact (path named in HDE-Schemas & Artifacts) that the boundary view is read-only and does not permit writes outside the HDE schema.

Schema details for these artifacts live in HDE-Schemas & Artifacts; PF14 requires only that the mechanics harness drive them.

All posture captures MUST:

* Run with determinism pins LC\_ALL=C, LANG=C, TZ=UTC.  
* Produce canonical JSON/text where applicable (UTF-8; sorted keys; compact; exactly one trailing LF).  
* Remain secret-free; logs and artifacts contain no credentials.

  ## **20.2 Partition mechanics (EPIC-011)**

Objective. Enforce EPIC-011’s non-deferred partition stance under standard artifact paths.

The partition harness MUST produce:

* artifacts/db/partition/partition\_plan.txt — Planned partition layout for HDE tables in scope.  
* artifacts/db/partition/partition\_verify.log — Verification output showing that the live DB matches the plan.

For EPIC-011 there is no “defer partition” posture: both a partition plan and a partition verify output are required. Token naming and semantics for partition acceptance are owned by HDE-Governance (titles-only); this guide records the mechanics expectations only.

## **20.3 Direct-only database selection mechanics**

Objective. Prove that `DATABASE_URL` and the Glow-owned psycopg provider form the sole active HDE database transport and that retired transport controls cannot select or restore bridge behavior.

Runtime selection (normative).

* `DATABASE_URL` is the sole canonical HDE database endpoint key.  
* Direct PostgreSQL access through the Glow-owned psycopg provider is the sole selectable HDE database transport.  
* `DBAccess` remains the sanctioned façade for database selection and operations, but it MUST expose no active bridge fallback, bridge forcing, bridge-production override, or alternate HTTP database transport.  
* A configured direct endpoint is usable only under the applicable environment, rails, credential, and task-specific authorization controls.  
* Missing, invalid, unavailable, or unauthorized direct access MUST fail closed without alternate-provider selection.  
* No runtime path may open an HTTP request to a database bridge, synthesize a bridge URL, infer another endpoint, or recreate `pg-bridge` as an undocumented compatibility service.

The names-only retired-key roster is exactly:

* `DB_ALLOW_BRIDGE_IN_PROD`  
* `DB_BRIDGE_URL`  
* `DB_FORCE_BRIDGE`

Presence of any retired key, including an empty value, is configuration drift. Selection MUST fail with stable names-only `RetiredBridgeConfiguration` / `retired_bridge_configuration` posture before provider construction, direct endpoint use, or external I/O. A retired value MUST NOT be printed, retained, hashed into evidence, or silently ignored while success is reported.

Direct selection MUST distinguish these outcomes:

* Healthy direct selection makes one successful psycopg attempt and selects `psycopg`.  
* Missing `DATABASE_URL` makes one skipped psycopg attempt and fails with `PrimaryUnavailable` / `missing_database_url`.  
* Unavailable direct PostgreSQL makes one errored psycopg attempt and fails with `PrimaryUnavailable` / `primary_connect_failed`.  
* Retired-key presence makes zero provider attempts and fails with `RetiredBridgeConfiguration` / `retired_bridge_configuration`.

Alternate-transport attempts MUST equal zero in every passing proof case.

DDL truth for this family is projection-only under `hde.ddl_identity_projection.v1`. A direct-posture proof MUST NOT present a bounded DDL projection as full raw database equivalence or restore direct-versus-bridge parity semantics.

## **20.3.1 Current direct-selection evidence contract**

The current direct-selection family is:

* Schema identity: `hde_epic038.direct_db_selection.v1`  
* Schema path: `schemas/hde_epic038_direct_db_selection.v1.json`  
* Primary path: `artifacts/runtime/direct_db_selection.snapshot.json`  
* Artifact key: `epic038.pr06r.direct_db_selection`  
* Record type: `epic038_pr06r_direct_db_selection`  
* Sole primary producer: `tools/evidence/generate_hde_epic038_direct_db_selection.py`

The primary MUST contain exactly `schema`, `retired_keys`, `cases`, `predicates`, `result`, and `failure`. Unknown keys are rejected at every object level. Serialization is canonical UTF-8 without BOM, with ASCII-sorted object keys, compact separators, and exactly one trailing LF.

`cases` contains exactly these rows in order:

1. `healthy_direct`  
2. `missing_database_url`  
3. `unavailable_database_url`  
4. `retired_keys_present`

`predicates` contains exactly:

* `direct_only_provider`  
* `missing_direct_fails_closed`  
* `unavailable_direct_fails_closed`  
* `retired_keys_fail_before_provider_attempt`  
* `alternate_transport_attempts_zero`  
* `secret_values_absent`

`result` is `PASS` only when every predicate and exact case invariant is satisfied. A negative receipt MUST exit nonzero and MUST NOT be consumed as release, PF09-support, QA, OPS-completion, acceptance, or closeout proof.

The canonical updater is the sole owner of the direct-selection primary’s Human Evidence Index row, Machine Evidence Mirror row, sibling path proof, and Index/Mirror hash companions. The focused producer MUST NOT write those companions.

## **20.3.2 Historical bridge evidence quarantine**

Existing bridge-era primaries remain immutable historical records. This includes:

* artifacts/db\_bridge/\*\*  
* the bridge-era artifacts/runtime/env\_connectivity.snapshot.json  
* bridge Presenter comparisons and their schemas  
* audit/ops/hde-epic038/ops-01/\*\*

Their primary bytes, producer provenance, checksum identities, sibling path proofs, Human Evidence Index rows, and Machine Evidence Mirror rows MUST remain intact unless a separately authorized historical migration is approved.

Historical rows MAY be classified as `historical_bridge_evidence`. Their notes MUST state that they do not prove current service availability, runtime support, direct-versus-bridge parity, bridge consistency, bridge fallback, acceptance-token satisfaction, or a current OPS PASS.

Historical bridge evidence MUST NOT be regenerated through a retired transport and MUST NOT satisfy a current direct-only release gate. A historical-integrity stage may validate retained presence, exact hashes, canonical readability, and secret-safe nonclaims and may report only `HISTORICAL_INTEGRITY_OK`.

Bridge-era producers, bridge consistency checkers, bridge provider implementations, bridge-specific schemas, and failed OPS diagnostics MAY remain only where required for historical validation or provenance. They MUST NOT be imported, registered, invoked, or interpreted as active database transport.

## **20.3.3 Direct read-only OPS posture**

When current live database-posture evidence is required, execution remains a separately authorized OPS responsibility. The authorization MUST bind the exact source commit, runner, validator, interpreter, target, rails, query roster, expected counts, candidate root, argv vectors, and one-attempt posture before launch.

The bounded capture MUST use `DATABASE_URL` and psycopg only, run under the authorized non-production posture, set the transaction read-only before governed observations, make zero SQL writes, make zero retries, and make zero alternate-provider attempts. Secret values, DSNs, hosts, raw rows, and credential material MUST NOT enter retained evidence.

A pre-launch authorization, source, or rails mismatch produces no database call. A post-launch failure consumes that authorization, produces only an inadmissible temporary failure receipt, and requires new PO-approved authorization bytes before another attempt.

Live direct-posture evidence does not prove Railway inventory, authorize database writes, create QA PASS, satisfy an acceptance token, move PF09 status, deploy, migrate, complete OPS generally, or close an epic.

## **20.3.4 Release integration, rollback, and tests**

Current direct-selection evidence and historical bridge evidence MUST retain separate identities, owners, meanings, and release predicates.

The direct-only release chain MUST:

* consume the current direct-selection primary as current selection proof;  
* validate an admitted direct read-only OPS packet only where that packet is required;  
* validate bridge-era bytes only through the historical-integrity contract;  
* finalize all current primaries and schemas before the canonical updater runs;  
* keep sibling path proofs, Human Index, Machine Mirror, and hash companions under canonical-updater ownership; and  
* fail atomically on missing or duplicate records, historical-byte drift, schema drift, path-proof drift, checksum failure, updater failure, orientation failure, or release-stage failure.

Rollback MAY disable database entrypoints or return to another direct-only commit. It MUST NOT restore bridge selection, bridge forcing, bridge fallback, bridge parity, bridge-dependent release admission, or current bridge-success evidence.

Required focused coverage includes:

* healthy direct selection through psycopg;  
* typed missing-direct and unavailable-direct failures;  
* each retired key, including an empty value, refusing before provider construction or I/O;  
* zero alternate-provider attempts;  
* secret-free, names-only failures;  
* projection-only DDL identity;  
* read-only direct-posture packet validation where applicable;  
* immutable historical bridge hashes and historical-only classification;  
* disjoint current and historical evidence ownership;  
* canonical-updater-only companion writes; and  
* fail-closed release behavior without bridge restoration.

# 21\) BodyGraph refresh worker (dev-only; policy-aligned) \[Required-Now\]

Role. scripts/bodygraph/run\_refresh\_worker.py is a dev-only worker that refreshes BodyGraphs according to a governed policy. It is not wired into CI; policy and schema are governed by HDE-Build Notes (ADR/Addenda 44–45) and HDE-Schemas & Artifacts (snapshot schema).

## **21.1 Policy alignment (v1 schema)**

The worker uses a POLICY dict whose structure and values MUST match the ADR and the governed refresh\_policy.snapshot.json v1 schema:

* schema — "v1".

* ttl\_s / swr\_s — time-to-live and stale-while-revalidate windows (values as defined in ADR).

* rate\_limit — nested object with requests\_per\_window and window\_s.

* circuit\_breaker — nested object with fail\_threshold, window\_s, cooldown\_s.

PF14 does not restate specific numeric values; they live in HDE-Build Notes/ADR and in the snapshot schema in HDE-Schemas & Artifacts. The worker MUST treat POLICY as the single source of truth for its behavior.

## **21.2 Behavior and sample counts**

The worker:

* Uses POLICY to decide when to enqueue or skip refreshes (TTL/SWR), when to rate-limit, and when to open/close the circuit breaker.

* Updates structured sample\_counts for at least:

  * refresh\_failures

  * breaker\_tripped

  * rate\_limit\_hits

The exact metrics surface and aggregation are governed in infra/ops docs (PF07/PF19); PF14 records that these counts are produced and governed.

## **21.3 Schema stability and coordination**

Mechanics MUST ensure:

* Running the worker never mutates the schema of refresh\_policy.snapshot.json; reads are allowed, but writes to the snapshot happen only via the governed snapshot path in HDE-Schemas & Artifacts.

* Any change to the policy shape or thresholds is coordinated with HDE-Build Notes addenda (ADR and bugfix PR-7R) and HDE-Schemas & Artifacts snapshot schema and tests, so that worker POLICY, ADR, and refresh\_policy.snapshot.json remain in lock-step.

Acceptance impact. No new tokens. This section clarifies the behavior assumed by existing refresh-policy evidence and tests described in HDE-Build Notes and HDE-Schemas & Artifacts; the worker remains dev-only and is not an acceptance gate in CI.

# 22\) SAFE Rails and Provider Gate

Refuse outbound/vendor work unless explicitly enabled. Provide open/close hooks for surfaces/providers and a posture sanity script.

* Defaults. Rails CLOSED for all tests and dev harness runs; vendor calls return typed refusals (numeric-free).

* Logging. Keys-only; no payloads, header values, or secrets.

* Evidence. Posture check log (rails closed) and at least one refusal fixture (typed, numeric-free).

* Policy, SAFE-rails tokens, and vendor transport matrices remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref (titles-only).

Conjunction resolution surfaces (SAFE rails; required). A higher-level conjunction surface (conjunction\_public\_resolved) MAY accept unresolved inputs and MUST resolve them to person\_uid-bearing records before delegating to conjunction\_public.

Resolution and rails rules:

* Local-first: if an input can be satisfied from local lookup, it MUST be used without network I/O.

* Open acquisition: if local lookup misses and SAFE rails are explicitly open, the surface MAY acquire via resolver (resolve\_db\_user\_id and resolve\_bodygraph) and MUST treat that acquisition as a controlled exception.

* Close-back: after any open acquisition step, the surface MUST re-check local lookup and proceed under closed posture for subsequent steps.

* Default closed: if the provided rails environment is missing or empty, the surface MUST behave as if rails are closed.

* Explicit open: rails MUST only be considered open when an explicit rails environment indicates SAFE\_MODE=0 and ALLOW\_NETWORK=1.

Cache normalization rule (bug-class prevention; required). Local lookup can return a vendor-shaped record that lacks person\_uid. If a user\_id hint is available for that record, the surface MUST normalize the record into the resolved shape instead of raising. If no hint is available, the surface MUST return a deterministic refusal response rather than crashing.

Tests (required). The conjunction\_public\_resolved contract tests MUST cover:

* Rails closed refusal when resolution would require network I/O.

* Rails open acquisition success.

* Close-back behavior after open acquisition.

* rails\_env missing or empty defaults to closed.

* Vendor-shaped local cache hit normalization with a user\_id hint.

# 23\) Rate Limit and Backoff Component (429)

Closed policy (normative)

* Retry/backoff family: one of {none, fixed, exponential} with integer parameters; no jitter.

* Retryable conditions: only {network\_error, 5xx}; other 4xx do not retry.

* 429 handling: record typed PROVIDER\_RATE\_LIMITED (optionally retry\_after\_ms if provided); no auto-success path in this epic (titles-only: EPIC-012 owns the 429 success-route).

* Envelope & logs: typed, numeric-free error; keys-only diagnostics (no payload bodies or header values; secrets always redacted).

# 24\) Caching and Transport Wiring \[Required-Now\]

## **24.1 Alpha posture (engine behind the app)**

Compat surfaces. Return 200 OK deterministic JSON only (no validators).

No conditionals. Do not implement 304 or HEAD in alpha; do not attach validators; skip CDN ceremony.

Determinism. Canonical JSON (UTF-8 no BOM, sorted keys, compact, exactly one LF); AB↔BA and two-run identity hold (see §10.1 / §4).

## **24.2 Production posture (Reader / Compat)**

Scope (normative). Mechanics wires and verifies runtime transport behavior for JSON success routes and companion surfaces. Full matrices live in HDE-CLI-API-Vendor Ref (Appendix A); A7 proofs run on a Catalog JSON success route (not /internal/version).

200 (success). Content-Type: application/json; charset=utf-8; include a strong, quoted ETag computed over the LF-terminated body (pre-compression); Cache-Control: private, max-age=0, must-revalidate; Vary: Authorization, Accept-Encoding.

304 (conditional). Only after a prior 200-with-body for the same ETag; no body; omit Content-Type and omit Content-Length; validators mirror the cached 200; ETag present.

HEAD parity. Status 200; no body; validators mirror 200; Content-Type \== GET; Content-Length \== len(identity 200 body) (LF-terminated, pre-compression).

Writers & errors. Cache-Control: no-store; no ETag. Errors must include Content-Type: application/json; charset=utf-8.

POST non-conditional. Requests do not carry validators; responses never return 304 (ignore If-\* conditionals).

Encoding invariance. For the same canonical LF-terminated body, ETag identity and the effective Content-Length are stable across accepted Accept-Encoding (identity/gzip/br). Capture an encoding-invariance headers-only proof on a Catalog route.

Acceptance (routing only).

Acceptance is governed by HDE-Governance (titles-only). This section does not list token names. A7 success-route transport acceptance requires proofs for quoted strong ETag on 200, HEAD parity, 304 omission rules, writers/errors no-store posture, required Vary headers, and encoding invariance on a cataloged JSON success route.

## **24.3 Proof surface & scope (titles-only routing)**

Success route proofs. Run on a route listed in docs/ENDPOINTS\_CATALOG.json (not /internal/version). Include GET, HEAD parity, 304 omission, writers/errors posture, and encoding-invariance captures; index human \+ machine in the same PR.

Ops exclusion. /internal/version is operator-only and not A7-eligible (see §14 / HDE-Governance §10.5).

Matrices & bytes. Owned by HDE-Governance / HDE-CLI-API-Vendor Ref (titles-only). This guide enforces wiring and evidence.

## **24.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

A7 success. Governed by the A7 token family (200 ETag, HEAD parity, 304 omission, success cache/Vary).

Writers/errors. Governed by the writers/error token family (no-store, no ETag, error Content-Type).

POST posture & invariance. Governed by Governance tokens for non-conditional POST and encoding/header invariance.

## **24.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)**

Single home for titles/paths. §36 Documentation Artifacts and Registry (“Reader success catalog & A7 proofs”).

Indexing. List titles/paths in Appendix D: Evidence Index and mirror 1:1 in artifacts/evidence\_index.jsonl (canonical JSONL; one LF; each record includes artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor).

Same-PR rule. Update human Index and mirror in the same commit/PR; CI enforces parity and path-proofs.

## **24.6 Routing (titles-only)**

Transport matrices & header rules. HDE-Governance / HDE-CLI-API-Vendor Ref.

Evidence registry & mirror discipline. §1.3 and §36.

# 25\) Gate Scripts and Evidence Harness \[Required-Now\]

## **25.1 Scope & pins (capability-level)**

Dev/run scripts (or CI jobs) produce binary acceptance and records-only evidence for the Engine. Script names and locations are implementation-defined (not pinned here).

All byte checks run with:

* LC\_ALL=C

* LANG=C

* TZ=UTC

JSON is canonical:

* UTF-8, no BOM

* ASCII-sorted keys

* Compact (no pretty-print)

* Exactly one trailing LF

## **25.2 What the harness must prove**

Determinism (math & emission)

* AB↔BA parity (pair neutrality)

* Two-run identity

* Canonical re-serialization byte-compare

* Preimage → hash → final reproducibility

* Registry configuration snapshot.

* A canonical registry\_report (registry\_report.v1) exists at artifacts/registry/registry\_report.json, generated via the Programmatic Configuration System (§3), and participates in the same two-run identity and canonical-JSON checks as other governed artifacts.

* CI rails posture. CI runs CLOSED by default. Any job that opens rails must pin retry/timeout/backoff policy and must index all governed evidence in the same PR (titles-only routing to Governance/Schemas & Artifacts).

Transport A7 (success endpoints)

Proof surface.

* Run on a Catalog JSON success route (see §9.1).

* /internal/version is ops-only and not A7-eligible (see §9.4; HDE-Governance §10.5).

A7 must prove:

* 200 has a strong quoted ETag, success cache headers, and Vary: Authorization, Accept-Encoding.

* HEAD mirrors 200 validators; no body; Content-Type \== GET; Content-Length \== identity 200 body.

* 304 is served only after 200; no body; omit Content-Type and omit Content-Length; validators mirror cached 200\.

* POST is non-conditional (never 304).

* Writers/errors: Cache-Control: no-store; no ETag; errors include Content-Type: application/json; charset=utf-8.

* Encoding invariance: for the same canonical body, ETag identity and effective Content-Length are stable across accepted encodings (identity/gzip/br); capture a headers-only proof.

* Env-gating: capture a headers-only env-gate proof demonstrating non-prod entries are unreachable in prod.

Band edges

* Inclusive-high thresholds

* Snapshot edges and diffs for each preset (see §5.3)

Reader↔CLI parity

* Shared emitter

* CLI stdout equals Reader 200 body for mirrored surfaces

Reader↔CLI error-envelope parity (deterministic scenario roster; stored artifacts)

The harness MUST enforce a fixed, ordered scenario roster for error parity evidence and tests (scenario ids are harness-internal, not token names):

* invalid\_json

* invalid\_viewer\_prefs

* db\_unavailable

* vendor\_attempt\_closed\_rails

For each scenario, the harness MUST:

* generate or invoke the HTTP-side envelope deterministically under closed rails and determinism pins

* generate or invoke the CLI-side error deterministically under the same pins

* store the pair of artifacts at canonical governed paths (see §37.7)

* run a CI-safe parity test that asserts runtime results are exactly equal to stored artifacts (no “close enough”), including stdout \== "" for CLI error cases and the expected stderr marker

Deterministic triggering MUST NOT rely on live network or a live database. If a scenario requires simulating DB unavailability or a closed-rails vendor attempt, the harness MUST use deterministic injection (for example env-pinned triggers) so the resulting envelopes and stored artifacts are stable under closed rails.

These artifacts are governed evidence. Any change to the stored artifacts requires same-PR updates to the Human Evidence Index, Machine Mirror, and topology orientation demo per the evidence workflow (§1.3.2).

Serializer path guards

* Grep-guard denies ad-hoc serializers

* Symbol proof shows Reader/CLI resolve to the same presenter/emitter

Narratives & architecture (keys-only)

* Deterministic narrative-router matrix coverage MUST cover the fixed Magic-10 category roster across the four public bands, producing a 10×4 key-table proof that records keys only and no narrative prose.  
* Missing-key behavior MUST fail closed by returning `missing_narrative_key` for both `personal_key` and `shared_key` when the category, band, or perspective case is missing or unsupported.  
* Router evidence MUST prove two-run identity, AB↔BA coherence where applicable, and CLI/HTTP parity where parity is defined.  
* Router evidence artifacts MUST remain canonical JSON or text logs under governed paths and MUST be refreshed with Human Evidence Index, Machine Mirror, hash sentinel, and path-proof bindings in the same PR lifecycle.  
* Architecture snapshot (LF-validated, no secrets)

Aux evidence scope (EPIC-010)

Capture exactly two headers-only snapshots:

* tests/transport/headers/aux\_text\_200.snap

* tests/transport/headers/aux\_suppression\_200.snap

Aux HEAD/304 captures are out of scope.

A7 proofs remain Catalog JSON-success only.

(Bytes/policy routed by title to PF05/PF04)

## **25.3 Orchestration & ordering**

The harness can be invoked standalone or as part of the sanity pipeline (see §26.5).

Minimum ordering:

* Format

* Lint/type

* Unit/property tests

* Schema checks

* Goldens

* Capture artifacts

* Index \+ mirror parity check

* Fail-closed on drift

## **25.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* Determinism. Governed by the determinism token family (AB↔BA, two-run, canonical compare).

* Transport A7. Governed by A7 tokens.

* Writers/errors posture governed by writers/error tokens.

* Encoding-invariance and Vary tokens required.

* Catalog posture (internal-only, env-gated) tokens required.

* Bands. Governed by bands/edges tokens.

* CLI parity & serializer guards. Governed by CLI/Emitter parity and no-alt-JSON tokens.

* Evidence discipline. Governed by Index/Mirror tokens (human↔machine 1:1; canonical JSONL; path-proofs).

* Aux/Narrative (EPIC-010). Acceptance is governed by HDE-Governance and Glow QA Guide (titles-only). PF14 does not list token names. Mechanics requires that Aux evidence capture and suppression posture are provable via the limited headers-only snapshots and any associated parity checks defined in the governing docs.

## **25.5 Evidence & indexing (records-only; machine mirror; same-PR rule)**

Single home for titles/paths. §36 Documentation Artifacts and Registry (“Reader success catalog & A7 proofs”). This guide does not pin file paths here.

Indexing:

* List artifact titles/paths in Appendix D: Evidence Index.

* Mirror 1:1 in artifacts/evidence\_index.jsonl (canonical JSONL; exactly one LF).

Mirror record fields:

* artifact\_key

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor

Parity gate:

* Update human Index and mirror in the same commit/PR.

* CI fails on:

  * Mismatch

  * Non-canonical JSONL

  * Unknown keys

  * Missing path-proofs

Required titles to appear in Index \+ mirror (examples, titles-only):

* Endpoint Catalog snapshot

* Env-gate proof

* A7 headers (GET/HEAD/304/writers+errors)

* Encoding-invariance proof

* Reader↔CLI parity and canonical-compare artifacts

* Band-edge snapshots

* Serializer grep-guard and emitter-symbol proofs

* /internal/version headers/body/two-run captures

Mirror field order note. Mirror field order & CI tokens are pinned once in §1.3; this section routes by title only to PF12/PF10 for the exact order and gates.

## **25.6 Routing (titles-only)**

* Transport matrices & A7 policy: HDE-CLI-API-Vendor-Ref; HDE-Governance.

* Domains & catalogs / canonical JSON rules: HDE-Schemas & Artifacts.

* Math semantics (preimage, bands, comparators): HDE-Math-Spec.

* Ops endpoint posture: HDE-Governance §10.5 (see §9.4 for PF14 ops block).

# 26\) Performance and Load Harness

Load tests for Reader, Compat, and Narrative Selection Router (keys-only). Microbenchmarks: compat() core computation \+ narrative key lookups.

Outputs: non-PII bench reports (bounded histograms \+ percentiles), thresholds, and regression flags.

Routing: SLO targets and failure posture live in Governance (titles only).

# 27\) Release and Provenance Packaging

Purpose (normative). Use one canonical manifest as the tracked release-identity input, derive release\_id from those bytes, and build current release-bound derivatives only through an isolated external attestation. Manifest shape and canonical rules live in HDE-Schemas and Artifacts (titles only).

The required dependency direction is:

`tracked source -> canonical manifest -> release ID -> external attestation`

No generated attestation or release derivative may point back into tracked source as an identity input.

## **27.1 Canonical manifest and release cut**

`catalog/manifest.json` is the single release-identity input stored in Git.

Its top-level keys are exactly:

* `root`  
* `version`  
* `built_at_utc`  
* `files`

The manifest MUST:

* use canonical UTF-8 bytes with ASCII-sorted object keys, compact separators, no BOM, and exactly one trailing LF;  
* set `root` to `catalog/`;  
* keep `files[]` ASCII-ascending by path with no duplicate path;  
* exclude `catalog/manifest.json` from `files[]`;  
* use safe repo-relative POSIX paths with no absolute path, parent traversal, or unsafe symlink source;  
* bind each declared file to its exact SHA-256 and byte size; and  
* run its cut and validation mechanics under `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, and `ALLOW_NETWORK=0`.

A normal release cut uses:

`python scripts/cut_release_manifest.py --version <semver> --built-at-utc <UTC>`

The cut validates its explicit inputs, refreshes the declared file hashes and sizes, sorts the entries, and changes only `catalog/manifest.json`. It MUST NOT write release evidence, Index/Mirror companions, generated source constants, registry reports, or attestations.

Source validation is read-only:

`python scripts/release_id_recompute.py --check-manifest-only`

A change to a manifest-listed source file causes that audit to fail until one intentional final cut is made after source stabilization. A Git commit does not inherently change release identity; release identity changes only when the canonical manifest bytes change.

## **27.2 Runtime release identity**

The release identity is:

`release_id = sha256(canonical_bytes(catalog/manifest.json))`

Runtime MUST read the packaged manifest, validate its canonical and closed-shape contract, and derive release\_id directly from those bytes.

Runtime MUST NOT read checked-in evidence paths, release-identity environment variables, generated release-ID constants, registry reports, or mutable attestation files as release-identity inputs.

No request-time manifest hashing or request-controlled release identity is authorized. The packaged manifest is read through the bounded runtime identity mechanism and failure is closed when its contract is invalid.

## **27.3 External release attestation**

Current release-bound derivatives are generated only through:

`python tools/evidence/build_release_attestation.py --output <external-empty-directory> --require-clean`

The builder MUST:

* require one exact clean source commit;  
* refuse an output path inside the source repository;  
* refuse a non-empty destination and avoid overwriting existing output;  
* copy the exact tracked source into an isolated working area;  
* build and install the real packaged console entrypoint in isolation;  
* run the required legacy producer closure only inside the isolated copy;  
* prove a second read-only fixed point;  
* run the final release-sanity gate inside the isolated copy;  
* use a closed-rails, allowlisted child environment;  
* exclude database, bridge, vendor, credential, and unrelated `PYTHON*` environment names;  
* restrict generated writes to the governed isolated evidence roots; and  
* leave the source checkout byte-stable.

Direct source-tree execution of the write-capable identity closure is prohibited. It is internal to the isolated attestation build only.

The success contract is `hde.release_attestation.v1`. The failure contract is `hde.release_attestation.failure.v1`.

A successful bundle MUST bind at least:

* the exact source commit;  
* an exact-source tracked-tree digest;  
* the canonical manifest and derived release identity;  
* a sorted file inventory with hashes and sizes;  
* deterministic stage, command, and exit-code transcript facts;  
* canonical checksums;  
* the final release-admission posture; and  
* explicit nonclaims for OPS execution, database writes, deployment, migration, QA PASS, acceptance, PF09 status movement, and epic closeout.

Timing, raw subprocess output, secrets, DSNs, vendor values, and database observations MUST NOT be retained as attestation content. Repeated builds from the same exact source MUST produce the same content tree.

CI MUST build and independently verify the bundle outside the source tree and MAY publish it with bounded retention. That CI artifact is exact-head release evidence; it does not become a tracked identity input, a durable governed release-admission record, or an acceptance token by implication.

## **27.4 Tracked evidence boundary and rollback**

Existing checked-in EPIC022 release evidence and its companions are frozen capture-time records. This includes the historical manifest copy, recorded release ID, recompute trace, checksum audit, snapshots, Index/Mirror rows, hashes, and path proofs associated with that capture.

Frozen checked-in release evidence:

* is not a current runtime identity input;  
* is not regenerated for each later release;  
* retains its historical producer and capture meaning;  
* MUST NOT be relabeled as a current external release attestation;  
* MUST NOT be refreshed merely because the manifest or release ID changes; and  
* remains subject to historical integrity, secret-safety, and canonical-byte checks.

`artifacts/registry/registry_report.json` is configuration evidence, not release-identity evidence. Its loader may validate the manifest and catalog contract, but the report and derived config bundles MUST NOT embed the manifest digest, release ID, or manifest-listed source identities as incidental provenance. An otherwise unchanged registry family MUST NOT churn solely because of a release cut.

Host-specific generated development files are not source. Local `.venv` trees and generated `*.egg-info` metadata MUST remain ignored and untracked. Dependency or editable-package installation MUST NOT dirty the tracked repository or alter release identity.

Rollback MUST revert the runtime manifest derivation, release-cut command, isolated attestation builder, workflow publication, and attestation schemas together. Rollback MUST NOT restore a generated release-ID constant, source-tree identity-closure writes, recursive checked-in derivative regeneration, clone-local mtime validity checks, release identity embedded in registry/config evidence, or bridge-era current-evidence semantics.

Acceptance is governed by HDE-Governance and pack/manifest rules in HDE-Schemas & Artifacts (titles-only). This section creates no token, QA PASS, OPS completion, PF09 status movement, deployment, migration, or closeout claim.

Routing (titles-only). Manifest shape, canonical JSON rules, historical evidence schemas, and external-attestation schemas: HDE-Schemas and Artifacts. Public transport remains in HDE-CLI-API-Vendor Ref / HDE-Governance.

## **27.5 Sanity pipeline (release & provenance) Required−Now**

Purpose (normative). Provide one fail-closed, closed-rails final-admission gate for the direct-only evidence graph. The gate validates current governed bytes, separately validates frozen historical evidence, and does not execute OPS, perform external I/O, or repair an inconsistent evidence graph.

Before final admission:

* all current primaries and schemas MUST be finalized;  
* any authorized OPS packet MUST already have been independently admitted and copied exactly;  
* the canonical updater MUST run once as sole writer of the Human Evidence Index, Machine Evidence Mirror, sibling path proofs, and Index/Mirror hashes; and  
* topology orientation MUST be generated only after the final evidence skeleton exists.

The canonical entrypoint writes `audit/gates/sanity_pipeline/sanity_pipeline.log` and uses exactly these nineteen mandatory stages in order:

1. Environment pins.  
2. Identity and release provenance.  
3. Canonical JSON.  
4. Reader/CLI, AB/BA, two-run, and preimage determinism.  
5. A7 Catalog transport.  
6. CI rails.  
7. Direct DB selection contract.  
8. Direct DB posture artifacts.  
9. BodyGraph policy.  
10. Architecture snapshot.  
11. Configured-v2 mapped-cache local evidence.  
12. Historical bridge evidence integrity.  
13. OPS-02 mapped-cache packet validation.  
14. OPS-03 direct DB posture packet validation.  
15. Human Index and Machine Mirror refresh.  
16. Evidence-path validation.  
17. Mirror schema and Index/Mirror hash validation.  
18. Topology orientation validation.  
19. Final-LF validation.

The stage roster name for stage 15 is retained as pipeline identity. On the finalized tracked evidence graph, stage 15 MUST invoke the canonical updater in read-only check mode and MUST NOT regenerate or repair Index, Mirror, path-proof, or hash bytes during final admission.

Stage 12 may report only `HISTORICAL_INTEGRITY_OK`. It MUST NOT report current bridge availability, parity, capability, consistency, fallback, or current OPS PASS.

Stage 14 is mandatory for final PASS when the direct-posture packet is part of the release graph. No required stage may be skipped.

The pipeline MUST:

* run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, and `ALLOW_NETWORK=0`;  
* stop on the first failed stage;  
* make no vendor, database, bridge, deployment, migration, or other external call;  
* never rerun OPS-02 or OPS-03;  
* preserve separate current-direct and historical-bridge meanings;  
* validate canonical JSON, deterministic outputs, rails, direct selection, direct posture, BodyGraph policy, mapped-cache evidence, updater fixed point, portable paths, Mirror/Index hashes, topology, and final LF;  
* reject a missing, duplicate, stale, schema-invalid, hash-invalid, path-invalid, noncanonical, or partially generated evidence family; and  
* avoid committing any partial generated set.

The canonical log MUST:

* begin exactly with `run:sanity-pipeline`;  
* identify `HDE-EPIC038-PR06-release-sanity`;  
* identify the governed environment-pins artifact;  
* record all nineteen stage outcomes in order;  
* record `first_failed_stage:NONE` only when every required stage succeeds; and  
* end with `summary:PASS` only when the complete gate passes.

Current release-bound regeneration occurs only inside the external attestation builder’s isolated tracked-source copy. That builder MUST prove the closure write, a second read-only fixed point, and this final sanity gate before publishing the external bundle. Final source-tree CI checks remain detect-only and MUST leave the tracked checkout clean.

Evidence (records-only; machine mirror; same-PR rule)

* audit/gates/sanity\_pipeline/sanity\_pipeline.log — canonical compact sanity surface.  
* audit/gates/sanity\_pipeline/sanity\_pipeline.log.path\_proof.txt  
* artifacts/sanity/sanity.log.path\_proof.txt  
* artifacts/proofs/sanity\_pipeline.transcript.log — retained transcript surface where governed by the owning evidence schema.

Existing governed artifacts implicated by the nineteen stages MUST be indexed and mirrored before this final read-only gate runs.

# 28\) Post-deploy Smoke

Purpose (normative). Run a minimal, production-against-production verification immediately after deploy. Prove transport correctness on a cataloged success route, confirm writers/errors posture, verify internal ops surface, and spot-check DB posture. Mechanics captures artifacts and indexes them in the Evidence Index and machine mirror in the same commit/PR.

## **28.1 Scope & pins**

Environment pins. All captures/compares run with LC\_ALL=C, LANG=C, TZ=UTC.

Routing. Transport matrices live in HDE-CLI-API-Vendor Ref; /internal/version policy in HDE-Governance §10.5; DB mechanics in §20.

## **28.2 Success route (A7) — transport smoke**

Surface. Use a route listed in the Endpoint Catalog (JSON success) (see §9.1).

Prove (headers-only):

* 200: strong quoted ETag, Content-Type: application/json; charset=utf-8, Cache-Control: private, max-age=0, must-revalidate, Vary: Authorization, Accept-Encoding.

* HEAD parity: no body; validators mirror 200; Content-Type \== GET; Content-Length \== identity 200 body.

* 304: served only after a prior 200; no body; omit Content-Type and Content-Length; validators mirror cached 200\.

## **28.3 Writers & errors — posture smoke**

Writers/errors: Cache-Control: no-store; no ETag.

Errors: Content-Type: application/json; charset=utf-8; typed, numeric-free error bodies (see Vendor Ref error model).

## **28.4 Internal ops /internal/version — ops-only smoke**

GET 200: JSON UTF-8; Cache-Control: no-store; no ETag; Last-Modified absent; Vary optional.

HEAD 200: mirrors GET validators; no body; Content-Length \== identity GET body; Content-Type \== GET.

Conditionals: If-None-Match / If-Modified-Since ignored; never 304\.

A7: not a success route; exclude from A7 proofs.

## **28.5 Database posture — live checks**

search\_path: prove hde, public (unquoted, in that order).

Roles/grants: least-privilege at runtime (snapshot grants/constraints).

Schema identity: normalized DDL fingerprint captured (see §20.1).

(Optional) RW smoke: insert→delete round-trip against a scratch table (job-profile gated).

## **28.6 Evidence (records-only; machine mirror; same-PR rule)**

List by title/path in Appendix D: Evidence Index and mirror 1:1 in artifacts/evidence\_index.jsonl (each record: artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor; canonical JSONL; one LF).

Success route (A7) proofs

* artifacts/proofs/success\_get.txt

* artifacts/proofs/success\_head.txt

* artifacts/proofs/success\_304.txt

* artifacts/proofs/success\_writers\_errors.txt

Internal ops

* artifacts/ops/internal\_version/headers\_get.txt

* artifacts/ops/internal\_version/headers\_head.txt

* artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt

* artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt

* artifacts/ops/internal\_version/body\_get.json \+ artifacts/ops/internal\_version/body\_get.sha256

* artifacts/ops/internal\_version/request\_chain\_manifest.json

* artifacts/ops/internal\_version/two\_run\_identity.log

DB posture

* artifacts/db/ddl\_fingerprint.json

* artifacts/db/grants.txt

* artifacts/db/check\_schema.txt

* artifacts/db/check\_constraints.txt

* artifacts/db/partition\_plan.txt (if used)

* artifacts/db/db\_rw\_smoke.log (optional)

Pins & harness

* audit/gates/determinism/env\_pins.log

* audit/gates/determinism/env\_pins.log.path\_proof.txt

## **28.7 Acceptance (titles-only; tokens live in HDE-Governance §2.0)**

Success route (A7). Governed by the A7 token family in Governance (200 ETag, HEAD parity, 304 omission, success cache/Vary).

Writers/errors. Governed by the writers/error token family (no-store, no ETag, error Content-Type).

Internal ops (/internal/version). Governed by the INTVER token family (ops-only posture, HEAD parity, conditionals ignored).

DB posture. Governed by DB\_ tokens\* (connection/env, search\_path, roles, schema fingerprint; optional RW smoke if run).

Evidence discipline. Governed by Index/Mirror tokens (human↔machine 1:1; canonical JSONL; path-proofs).

This guide asserts capability-level conformance and routes all token names to HDE-Governance §2.0. Artifacts are captured per §27.6 and indexed per §1.3/§36.

# 29\) Server Cache (Production) — rolled in

Purpose. Optional, private, composite-key cache for Reader and Compat that preserves A7 transport rules and deterministic invalidation.

Key

Composite key fields. { viewer\_id | person\_id(s) }, design\_fingerprint, thresholds\_identity, release\_id.

Pair normalization. Normalize {a,b} to a stable order (AB↔BA) before keying.

Viewer scope. Include viewer\_id only when output depends on viewer preferences.

Determinism. Key construction is pure and reproducible; no clock, no randomness.

Transport (A7-consistent)

200 (success). Content-Type: application/json; charset=utf-8; strong, quoted ETag over the LF-terminated body (pre-compression); Cache-Control: private, max-age=0, must-revalidate; Vary: Authorization, Accept-Encoding.

304 (conditional). Only after a prior 200-with-body for the same ETag; no body; omit Content-Type and omit Content-Length; validators mirror the cached 200; ETag present.

HEAD parity. Status 200; no body; validators mirror 200; Content-Type \== GET; Content-Length \== len(identity 200 body) (LF, pre-compression).

Writers & errors. Cache-Control: no-store; no ETag; writers bypass cache.

Encoding invariance. For the same canonical body, ETag identity and effective Content-Length are stable across accepted Accept-Encoding (identity/gzip/br).

Ops exception. /internal/version is operator-only and never cached.

Invalidation (deterministic)

Triggers. Any change to release\_id, thresholds\_identity, input payloads (incl. viewer\_prefs), or design\_fingerprint.

Effect. Invalidation is immediate; no stale bytes are served after an invalidation event.

Controls

Default OFF. Enable via a runtime flag.

Metrics. Emit counters for hits, misses, invalidations.

Diagnostics (optional). A keyed, redaction-safe debug log of cache decisions for local analysis (titles-only in indices).

# 30\) Observability (Logs and Metrics)

Logging (keys-only)

Structured, keys-only logs with correlation IDs (non-PII, bounded).

Surfaces: Reader, Compat, cache layer, rate-limit decisions.

Guards: grep-guards prevent payload/secret logging; only allow-listed labels.

Metrics

Counters/Histograms: request counts, latencies, cache hits/misses, rate-limit outcomes.

Dashboards: quick views for transport health, cache efficacy, and error rates.

BodyGraph ingest signals

Counters: refresh successes/failures; rate-limit throttles; circuit-breaker trips.

Histograms: vendor latency.

Gauges: staleness percentage.

Evidence: artifacts/bodygraph/metrics.snapshot.json (keys-only, canonical JSON, single LF).

# 31\) Security Posture

Controls

Per-route rate limits

CSRF: rotate token and retry once on browser writers

Strict input validation

Writers: Cache-Control: no-store; typed errors; no ETag

Never log secrets or PII

Packaging & Runtime

Dockerfile and process launch scripts

Health and readiness probes

Externalize only secrets/coordinates via environment variables

Generate typed config at build time

Identity

/internal/version is operator-only; Cache-Control: no-store; no ETag

Provenance: build\_commit is optional in production and may be unset/null

Logs (ingest)

Keys-only logs; no raw birth data; no vendor payloads; secrets never logged

Provide a sanitized sample: artifacts/bodygraph/keys\_only.logs.sample

# 32\) Packaging and Runtime \[Required-Now\]

Scope. Container packaging and runtime posture for the HD Engine. Mechanics owns image/process hardening, config plumbing, health/ready behavior, and operational guardrails. Public bytes, schemas, and transport matrices are referenced by title only. All byte-sensitive checks run with LC\_ALL=C, LANG=C, TZ=UTC.

## **32.1 Image & process posture**

Deterministic build. Reproducible container image; pin base; lock package indexes; emit SBOM.

Least privilege. Run as non-root; drop Linux capabilities; prefer read-only root FS with writable tmp/cache only if required.

Single binary & emitter. Wire the allow-listed presenter/emitter (see §4, §10.2); forbid ad hoc serialization in entrypoints.

Locale pins. Export LC\_ALL=C, LANG=C, TZ=UTC for all emit/compare paths to preserve byte identity.

Resource limits. Set CPU/memory limits and graceful shutdown (SIGTERM → drain → exit 0).

## **32.1A Start command & service factory \[Required-Now\]**

Purpose (normative). Capture the exact production start command and prove the app factory binds to $PORT.

Start-command capture (records-only). Capture the exact launch command line used in production (no secrets). Store as canonical text (UTF-8; exactly one trailing \\n). (Evidence path listed in §36.)

Factory binding to $PORT. Prove the service initializes via the factory adapter.factory:create\_app() (titles only) and binds to $PORT from the environment (no hard-coded port).

Selected-factory route inventory. The factory selected by the production start command and documented local launchers MUST register the Reader blueprint and the existing `compat_blueprint`. Its mounted route inventory MUST include `GET /reader`, `GET /internal/version`, and `POST /api/compat/v1`. The compatibility route remains an existing `internal_admin` surface. This mechanic creates no new route, handler, payload, public contract, HTTP home, or launcher target.

Route-mount parity proof. Compatibility contract and parity coverage MUST exercise that selected factory. Mechanics evidence MUST record the selected factory and its mounted blueprint and route inventory against the Endpoint Catalog and HDE Architecture adapter responsibilities. Checks MUST fail closed if either required blueprint registration or any assigned route is absent. Alternate development or wrapper factories MUST NOT mask an omission from the selected factory.

Runtime pins (minimal). Record PORT, APP\_ENV, and identity pins required for traceability as a keys-only text snapshot (UTF-8; one \\n). (Evidence path listed in §36.)

## **32.2 Configuration & environment**

Typed config at build. Generate a typed runtime config artifact at build (defaults, switches, A7 posture) and vendor it into the image.

Env allow-list (secrets/coordinates only). Only read whitelisted keys at startup: SAFE\_MODE, ALLOW\_NETWORK, HDAPI\_BASE\_URL, HD\_API\_KEY (secret), GEO\_API\_KEY (secret), PORT, and explicitly documented toggles.

Fail-closed on unknowns. Unknown env keys or malformed values fail fast; do not partially boot.

Rails posture. Rails defaults derive from the Env Deployment Inventory (titles-only): dev & stage OPEN, prod CLOSED, CI CLOSED. In CI, any job that opens rails must pin policy and index governed evidence in the same PR. Determinism pins (LC\_ALL=C, LANG=C, TZ=UTC) apply in all environments that produce governed bytes.

## **32.3 Health/ready & lifecycle**

HTTP probes.

* /healthz: liveness (process up, core initialized).

* /readyz: readiness (emitter wired, pack loaded, manifest hashed, rails posture read).

Probe bytes. Minimal, numeric-free JSON; canonicalized (UTF-8/no BOM, sorted keys, compact, one LF).

Graceful shutdown. Stop accepting traffic on TERM; complete in-flight; emit final health with status:"stopping"; exit cleanly.

## **32.4 Security & observability**

Keys-only logs. No payload or header values in logs; secrets always REDACTED; bounded labels (route, outcome, rails\_state, timeout\_profile, attempt\_idx).

Metrics (bounded). Counters/timers/histograms for engine/presenter latency and transport outcomes; no PII.

Tracing. Optional correlation\_id (non-PII) with bounded cardinality.

## **32.5 Transport & identity (titles-only)**

Reader A7 (public). See HDE-CLI-API-Vendor Ref and HDE-Governance (ETag over LF-terminated body; Vary policy; 304 omits Content-Type and Content-Length; HEAD parity; POST non-conditional).

Internal ops /internal/version. Operator-only; Cache-Control: no-store; no ETag; HEAD parity; conditionals ignored; body includes engine\_tag, release\_id, invocation\_tag, emitter\_sha256, optional build\_commit (see §14).

Identity. release\_id from canonical manifest (HDE-Schemas and Artifacts §6); invocation\_tag participates in preimage (HDE-Math-Spec §3); presenter uses canonical serializer (§4).

## **32.6 Acceptance (binary)**

Image & user. SBOM produced; runs as non-root; read-only FS validated at runtime.

Config discipline. Only allow-listed env consumed; unknowns fail; typed config present; SAFE rails ON by default.

Health/ready. Probes return canonical JSON; liveness/readiness reflect emitter/pack state; graceful shutdown proven.

Ops posture. /internal/version headers/body match §14; no-store, no ETag, conditionals ignored, one LF; HEAD 200 parity.

Start command & factory. Start command captured; factory proven; binds $PORT.

Determinism. LC\_ALL=C, LANG=C, TZ=UTC enforced; canonical re-serialization byte-compare passes for all public/ops surfaces emitted from this process.

Acceptance token naming and semantics are owned by HDE-Governance (titles-only). This guide does not list token names. The acceptance obligations in §32 include start-command capture, app factory correctness, binding to $PORT, environment allow-list discipline, and ops posture for /internal/version, all proven via governed evidence.

## **32.7 Evidence (titles/paths only)**

Single home for artifact titles/paths. Do not pin file paths here. The authoritative registry of artifacts and their titles/paths lives in §36 Documentation Artifacts and Registry.

Mechanics MUST:

* List artifacts by title/path in Appendix D: Evidence Index (human).

* Write records-only mirror entries to artifacts/evidence\_index.jsonl in the same commit/PR (machine).

* Ensure each mirror record is canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one LF) and includes: artifact\_key, sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, proof\_anchor.

* Maintain strict 1:1 parity between human Index and machine mirror; CI fails on mismatch or missing path-proofs.

Routing (titles-only). A7 and ops policies: HDE-Governance. Public bytes & preimage: HDE-CLI-API-Vendor Ref / HDE-Math-Spec. Pack/manifest: HDE-Schemas and Artifacts. Evidence registry/mirror discipline: §1.3 and §36.

# 33\) SDKs (Client Libraries) — rolled in

Client libraries use the allow-listed presenter-emitter and enforce transport rules.

TypeScript SDK (required)

* readPerson(id | payload) — calls Reader; returns the exact public body bytes (LF-terminated). await .json() is available as a convenience parser.

* compat(a, b, prefs) — calls /api/compat/v1 with POST and Content-Type: application/json; returns the exact body bytes; await .json() available.

* sample(viewer\_prefs, seed?) — calls /api/sample/v1 with POST; returns the exact body bytes; ordering matches service; await .json() available.

conditionalGetHelper (Reader; production)

Implements conditional GET with If-None-Match.

* On 200: returns {status:200, etag, body\_bytes}, updates cache.

* On 304: returns {status:304, etag, body\_bytes} using cached bytes; server 304 has no body, omits Content-Type, and has Content-Length 0 or absent.

Helpers surface the strong, quoted ETag for callers.

Python SDK (ops/automation)

Mirrors readPerson, compat, sample; returns body bytes with optional .json() convenience.

Includes byte/order parity tests against the service.

Policy

All SDK calls MUST preserve canonical JSON bytes (UTF-8, sorted keys, compact separators, exactly one trailing LF).

Application teams SHOULD use the SDK to guarantee byte/order parity with the single emitter and correct A7 transport behavior.

Acceptance

TypeScript compat() and sample() bytes are bitwise-equal to service 200 bodies; sample() ordering matches.

conditionalGetHelper sends If-None-Match and handles 304 semantics exactly (no body, omit Content-Type, Content-Length 0/absent).

Python SDK parity tests pass for bytes and ordering across all three calls.

# 34\) Dev HTTP Harness (single home)

Current local capture posture is dev-only, bound to 127.0.0.1, not public, with CORS disabled and APP\_ENV=dev; debug reloader stays off during captures. This section inventories co-located route classes rather than declaring every listed route dev-only. `/reader` is the cataloged Reader success surface in current scope, and the existing endpoint inventory MUST designate `/reader` explicitly as the governed Reader success-proof surface rather than forcing that conclusion to be inferred from route existence plus A7 eligibility. Dev-only wording applies only to explicitly preview or conjunction routes. The Endpoint Catalog remains the single A7 proof surface for Reader success routes, the dev harness remains supplemental, and `/internal/version` remains ops-only. Emits canonical JSON via the allow-listed presenter-emitter (§4/§8).

Routes:

* GET /reader?v=1 (Reader; cataloged success surface in current scope)  
* GET /api/reader?v=1 (Reader alias when mounted under /api prefix)  
* GET|POST /api/compat/v1 (pair; ids-only GET)  
* POST /api/sample/v1

Aux route (context). The Aux narrative surface is served at `/aux/narrative` from the same adapter HTTP surface family.

Method posture:

* All /api routes are dev-only unless explicitly stated otherwise. The harness binds to 127.0.0.1:5000 by default and MUST NOT be exposed as a public interface.  
* GET MUST NOT include a body.

Error posture:

* Errors return JSON `{"error": "<MSG>"}` and MUST include a non-2xx HTTP status. (The harness is for dev; this is not a public error contract.)

Runner:

* The harness is implemented by `python -m adapter.http_dev_harness`.

Quick start (curl — local 5000):

* Pair (POST): `curl -s http://127.0.0.1:5000/api/compat/v1 -H 'Content-Type: application/json' -X POST -d '{"a":{}, "b":{}, "viewer_prefs":{}}' | jq .`  
* Pair (GET): `curl -s http://127.0.0.1:5000/api/compat/v1?id=<A_ID>&id=<B_ID>&viewer_prefs=<VP_JSON_URLENCODED> | jq .`  
* Sample with seed (POST): `curl -s http://127.0.0.1:5000/api/sample/v1 -H 'Content-Type: application/json' -X POST -d '{"seed": 1}' | jq.`  
  Reader (GET; v1): `curl -s http://127.0.0.1:5000/reader?v=1 | jq .`  
* Sample with seed (POST): `curl -s http://127.0.0.1:5000/api/sample/v1 -H 'Content-Type: application/json' -X POST -d '{"viewer_prefs":{}, "seed":12345}' | jq .`

For Codespaces and other shared environments, Mechanics requires that QA and docs use the infra-provided dev start commands and URLs (for example, values exposed via devcontainer or environment keys described in Glow Infrastructure and HDE-Build Checklist by title) instead of hard-coding hostnames or ports in plans or scripts.

# 35\) Runbooks (Operations)

Ops tasks (PO-only execution; IA-guided; not PR work).

Ops tasks (PO-only execution; IA-guided; not PR work).

Definition. An Ops task is any work item that requires privileged access to systems outside the repository and therefore cannot be performed by automated agents. This includes (non-exhaustive): service configuration, secrets and env var changes, deploy/runtime settings, infrastructure console actions, and certain database operations (creation, grants, production migrations, and other privileged state changes). A DevOps task is treated as an Ops task whenever it requires any of the above human-only access.

Execution authority (hard).

* Ops tasks MUST be executed by the PO (human operator) only.

* Automated agents MUST NOT attempt to perform Ops tasks, MUST NOT claim completion, and MUST NOT simulate external state changes.

IA facilitation posture (required). When Ops tasks are part of an epic, they are facilitated by the Implementation Agent (IA). The IA MUST specify intent, constraints, verification, and evidence requirements in a what-not-how manner, then work directly with the PO during execution.

Canon-grounded operator instructions when available (required). When the relevant PF canon already provides concrete operator instructions for an Ops task, the Ops task record or guide MUST include those canon-grounded instructions explicitly, in addition to the what-not-how fields in this section, rather than remaining only at the level of intent, constraints, or outcome.

This includes, when already available in canon:

* concrete operator steps  
* commands  
* required fields  
* safety rails  
* validation checks  
* evidence captures  
* canonical paths  
* decision rules

If the relevant canon is silent, incomplete, or ambiguous, the Ops task MUST state that the missing instruction is unknown and MUST NOT invent procedure. PF references used for these instructions remain titles-only.

Not a PR (required). Ops tasks are not Codex PRs. Any implementation or remediation guide MUST separate Ops tasks from PR work and clearly label Ops steps as: PO-only execution, IA-guided.

Ops task record format (what-not-how; required fields). Every Ops task record MUST include:

* Task ID (stable, referenced consistently)

* Owner: PO

* Facilitator: IA

* Target system/service (name only, no secrets)

* Intent / desired end state (what changes, and what “done” looks like)

* Constraints / safety rails (what must remain true while executing)

* Success criteria (observable outcomes, not assumptions)

* Evidence to capture (what artifact(s) will prove the change, and where stored)

* Rollback intent (what “revert” means at a high level)

* Secret handling note (explicitly: no plaintext secrets in docs or evidence)

Evidence posture (required). Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase path such as:

* audit/ops/\<epic-id\>/\<PATH\> for Ops execution evidence

* audit/qa/\<epic-id\>/\<PATH\> when the evidence is part of QA execution

Evidence MUST NOT include secrets. If a setting/value is sensitive, evidence MUST be presence-only, redacted, or hashed, while still being sufficient to verify the intended state.

Mechanics Guide tracking requirement (normative). Any Ops task included in an epic MUST be represented as a subtask record in this Mechanics Guide so it can be tracked and reused. The Mechanics Guide entry MUST use the same Task ID and MUST carry the same required fields listed above.

No governance drift (hard). Ops tasks MUST NOT create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it MUST map to existing governance-defined acceptance posture and be proven via evidence artifacts.

Clarification. If a change is fully achievable as code (including tests and deterministic artifacts), it is PR work. If any step requires human console or config action, that step is an Ops task (even if adjacent code changes exist). Ops tasks can be prerequisites for epic completion, but they are proven by evidence artifacts, not by agent execution claims.

# 36\) Dashboards and Alerts

Dashboards for Reader, Compat, Narrative Router, and Server Cache latencies, error rates, hit/miss, and rate-limits. Actionable alerts for error spikes and budget breaches.

Notes: include A7 headers health and cache hit ratio panels.

---

# 37\) Documentation Artifacts and Registry \[Required-Now\]

Registry for small, deterministic documentation artifacts and gate evidence. Titles-only cross-refs; bytes live in files. Mechanics keeps the human index and the machine mirror in lockstep (same-PR rule).

## **37.1 Purpose & scope**

* Provide a single registry for governed documentation artifacts and gate evidence.  
* Keep Human Index and Machine Mirror in 1:1 parity, updated in the same commit/PR.  
* Treat updater, orientation, and check tooling as the synchronization layer across the governed evidence roots used by the registry.  
* Roots that merely look like evidence or truth homes are non-authoritative unless this guide or HDE-Schemas & Artifacts explicitly routes them into the governed evidence model.  
* Act only on governed paths; transient generator outputs are never authoritative, and same-change synchronization applies to governed roots rather than to every top-level root that merely looks evidentiary.

## **37.2 Governance & homes**

Governed paths only:

* /artifacts/\*\* — public documentation snapshots and pack/identity evidence.

* /audit/gates/\*\* — gate evidence produced by §24 scripts (bands / canonical / props / etc.).

* /audit/qa/\*\* — epic-scoped Live QA artifacts (per-check primary logs, manifests, and QA meta outputs).

* /audit/docdeltas/\*\* — doc-delta capture artifacts used by Step-0B and close-pack workflows.  
* Transient generator paths (for example, codex/out/\*\*) are not authoritative and MUST NOT be indexed.

Per-epic close-pack and acceptance scaffolds (canonical names; mechanics-only).

Some governed artifacts are epic-scoped and must use canonical, non-ambiguous file paths so indexing and CI checks cannot drift.

Close-pack artifacts (epic-scoped; canonical filenames):

* audit/EPIC-\<NNN\>\_close\_report.md  
* audit/EPIC-\<NNN\>\_MANIFEST.json  
* audit/docdeltas/hde-epic\<NNN\>\_doc\_deltas.md

Conditional external QA RCA artifact (only when the QA RCA summary is not embedded in the close report):

* audit/EPIC-\<NNN\>\_QA\_RCA.md

Close-pack path-proof transcripts (minimum required):

* audit/EPIC-\<NNN\>\_close\_report.md.path\_proof.txt  
* audit/EPIC-\<NNN\>\_MANIFEST.json.path\_proof.txt

These path-proof siblings MUST be produced alongside the close-pack artifacts above and are treated as placement transcripts (CI-safe scaffold checks), not as primary evidence.

Where \<NNN\> is a zero-padded 3-digit epic number (example: 022). These are governed artifacts and must not be duplicated under alternate spellings.

Close-pack generator (mechanics; single-writer; normative): A deterministic generator entrypoint MUST exist to write the close-pack artifacts above (and any required path proofs) at their canonical paths. For EPIC-025, the close-pack generator entrypoint is `tools/qa/generate_epic025_close_pack.py`.

Close report (minimum content; generated): The close report MUST summarize deliverables, enumerate explicit deferrals (if any), and include a titled "Key outputs" section that points reviewers to the close-pack manifest’s key outputs bindings. The QA RCA and Doc Delta summary MAY be embedded inside the close report or emitted as `audit/EPIC-\<NNN\>\_QA\_RCA.md`; the separate file is required only when that summary is external to the close report.

Doc deltas capture file (minimum content; generated): The doc deltas capture file MUST enumerate canon deltas found during the run. If none exist, it MUST state: "Doc Deltas: None".

Close-pack manifest (minimum binding responsibilities; generated): The manifest MUST include a pointer to the close report and MUST expose a machine-discoverable set of key outputs bindings for primary artifacts. When a close-pack or related closeout surface records epic checklist coverage, it MUST express that coverage as PF09 scope and status-only bindings rather than as invented epic-local acceptance token names. Acceptance token names, token semantics, and any temporary bridge-token admission remain governed by HDE-Governance and HDE-Build Notes (titles-only). Close-pack outputs MAY point to the governing acceptance artifacts that carry token claims, but they MUST NOT substitute local invented token spellings for those artifacts. The manifest schema is owned by PF12-Canon-HDE-Schemas-and-Artifacts.

QA closeout summary (RCA) minimum structure (when required by the epic QA plan). The QA closeout summary MUST include, at minimum, the following titled sections:

* Compliance statement  
* Scope boundary and reference set  
* Source-of-Truth posture  
* Coverage vs QA Plan accounting  
* D0 discovery artifact accounting  
* Governed current-state QA evidence accounting under the canonical epic QA root  
* Functional runtime proof accounting for changed or reviewed runtime surfaces  
* Accepted plan-execution deviations (if any), including bounded Moon Loop reruns, rails changes, and step-local dependency-preflight corrections  
* Closeout decision trace  
* Moon Loop stop-condition assessment  
* Minimum stop-rule (QoS): If more than three (3) structural plan-to-evidence mismatches are discovered during a single closeout attempt, stop and repair the plan/templates and evidence-indexing artifacts before executing additional QA steps. Structural mismatches include: a required artifact is declared but absent; a required artifact path is spelled differently than the produced file; a closure record places NOT RUN / DEFERRED forward pointers under required artifacts; a primary.log header artifacts list omits primary.log.  
* The assessment MUST state the mismatch count, the first mismatch signature, and the remediation action taken (or state "not remediated; closeout halted").  
* Token and evidence posture (required tokens must be proven with explicit evidence pointers; missing required tokens must not be inferred)  
* Overall readiness or closeout recommendation  
* When a PF10 addendum is used as the decisive epic-close authority, the summary MUST state whether that addendum provides direct evidence-pointer lines or only evidence-basis prose. If only evidence-basis prose is available, the summary MUST record that fact explicitly as an auditability caveat and MUST NOT assume pointer completeness.

Additional sections are allowed, but the QA closeout summary MUST retain explicit evidence pointers for any claim that a required token is proven or that a deviation is accepted.

Documentation drainage posture for closeout artifacts (mechanics-only). Close reports, QA RCA summaries, acceptance maps, token-to-evidence matrices, step logs, repo-supported completion summaries, and related closeout artifacts MUST NOT encode PF10 drain or any other post-QA documentation drainage as a prerequisite, required deliverable, required check, acceptance condition, readiness condition, or blocker.

Allowed blocker posture (mechanics-only). These artifacts may treat only truth-and-proof failures as blockers, including incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR / FAIL\_TOOLING / TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.

Undrained delta posture (mechanics-only). When repo evidence supports a later canon, checklist, or guide status change that has not yet been drained, the artifact MUST treat PF10 as the temporary live-truth home, MAY list later drain targets, MUST use supportable from repo evidence wording for the undrained posture, and MUST NOT imply that drainage already happened or is required for the current verdict. Plans and closeout artifacts MUST NOT require PF document updates as execution or closeout outputs.

Acceptance scaffolds (epic-scoped; canonical locations):

* audit/qa/hde-epic\<NNN\>/token\_evidence\_matrix.md

* docs/acceptance\_map\_epic\<NNN\>.json

These are governed artifacts. PF14 does not define token semantics; it requires only that these artifacts exist, remain parseable, and do not introduce ambiguous duplicate rows or placeholder bindings once concrete evidence exists.

CI-safe scaffold checks (mechanics only).

The repo SHOULD include CI-safe tests that validate, at minimum:

* the epic-scoped close-pack and acceptance scaffold files exist at the canonical paths above

* the acceptance artifacts are structurally coherent (parseable, no duplicate token ids/rows)  
* the acceptance artifacts contain no Unicode ellipsis character (U+2026) and no sequences of three consecutive U+002E FULL STOP characters

* the acceptance map and token-to-evidence matrix are mutually consistent (no duplicate rows across artifacts, no placeholder bindings once concrete evidence exists, and no map/matrix misalignment that would require a reviewer to “interpret” intent). PF14 does not enumerate token names; this is a structural consistency requirement only.

* token-to-evidence bindings that reference non-placeholder evidence paths MUST be Index/Mirror backed: each referenced path MUST exist in docs/evidence/INDEX.json, and MUST have a corresponding Machine Mirror record in artifacts/evidence\_index.jsonl with a non-empty proof\_anchor (validators MUST NOT skip this check when a path is absent from both registries).

* token-to-evidence bindings MUST reference primary evidence artifacts (not their \*.path\_proof.txt transcripts). Path-proofs are required, but MUST be referenced via the machine mirror proof\_anchor (and/or mirror checks), not treated as primary evidence titles/bindings.

Token name validity (names-only). Any acceptance token name referenced by these acceptance scaffolds MUST match the HDE-Governance Token Registry exactly (titles-only) or, if newly minted and not yet drained, the canonical token spelling in HDE-Build Notes (titles-only). Aliases and near-matches are prohibited; correct the scaffold artifacts to the canonical token spelling. This guide does not list token names.

EPIC024 token-registry validity check (PO-006) fixed outputs (records-only):

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/rg\_acceptance\_map\_output.txt

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/rg\_registry\_output.txt

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/token\_comparison.json

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/primary.log

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/transcript.txt

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/primary.log.path\_proof.txt

* audit/qa/hde-epic024/checks/po-006\_token\_registry\_validity/transcript.txt.path\_proof.txt

Implementation note (mechanics-only). The `rg_`\-named output files above are EPIC024 records; future token-registry validity checks SHOULD avoid reliance on external grep-style tooling and SHOULD prefer deterministic parser-based checks while preserving equivalent evidence semantics.

Placeholder evidence strings are permitted only for D0 scaffolding; once an epic writes concrete governed evidence files, acceptance scaffolds must not retain placeholder bindings.

Human Index (single home):

* docs/evidence/INDEX.json — titles/paths only; no payload bytes.

* docs/evidence/INDEX.sha256 — hash sentinel for the Human Evidence Index.

Machine Mirror (single home):

* artifacts/evidence\_index.jsonl — records-only JSONL; one LF per record.

## **37.3 Conventions**

* Deterministic filenames (lowercase, stable tokens).

* Allowed extensions: .json, .log, .txt, .md, .bytes.

* Text artifacts end with exactly one trailing LF (\\n).

* JSON is canonical:

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact (no pretty-printing)

  * exactly one trailing LF

* .bytes files mirror the exact body bytes (including the body’s own trailing LF, if present).

* Header snapshots follow §4.3 normalization (lower-cased keys, compact, one LF).

Close-pack manifest key\_outputs is a named binding map (normative):

* audit/EPIC-\<NNN\>\_MANIFEST.json MUST include key\_outputs as a JSON object (map) where each key is a stable pointer name (string) and each value is a repo-relative artifact path (string).

* key\_outputs MUST NOT be a list.

For EPIC023, key\_outputs MUST include these bindings (keys \+ exact values):

* acceptance\_map: docs/acceptance\_map\_epic023.json

* token\_matrix: audit/qa/hde-epic023/token\_evidence\_matrix.md

* acceptance\_map\_viability: audit/qa/hde-epic023/acceptance\_map\_viability.log

* qa\_step\_manifest: audit/qa/hde-epic023/qa\_step\_logs\_manifest.json

* doc\_deltas: audit/docdeltas/hde-epic023\_doc\_deltas.md

* close\_report: audit/EPIC-023\_close\_report.md

* close\_manifest: audit/EPIC-023\_MANIFEST.json

Additional key\_outputs entries are allowed, but these bindings are the closure minimum for EPIC023.

For EPIC024, key\_outputs MUST include these bindings (keys \+ exact values):

* acceptance\_map: docs/acceptance\_map\_epic024.json

* token\_matrix: audit/qa/hde-epic024/token\_evidence\_matrix.md

* acceptance\_map\_viability: audit/qa/hde-epic024/acceptance\_map\_viability.log

* qa\_step\_manifest: audit/qa/hde-epic024/qa\_step\_logs\_manifest.json

* doc\_deltas: audit/docdeltas/hde-epic024\_doc\_deltas.md

* close\_report: audit/EPIC-024\_close\_report.md

* close\_manifest: audit/EPIC-024\_MANIFEST.json

Additional key\_outputs entries are allowed, but these bindings are the closure minimum for EPIC024.

EPIC024 Step-0B doc-delta capture (fixed paths):

* audit/docdeltas/hde-epic024\_doc\_deltas.md

* audit/qa/hde-epic024/00\_meta/doc\_deltas.md

Doc-delta capture validation (EPIC024 PO-011) (normative):

* The two doc-delta files above MUST be byte-identical (diff exit code 0).

* Doc-delta content MUST include PF refs per entry.

PO-011 primary log (fixed path):

* audit/qa/hde-epic024/checks/po-011\_doc\_delta\_capture/primary.log

Close-pack validation checks MUST validate the named bindings (keys \+ exact path values), not list membership.

EPIC024 close-pack validation check (D16) primary log (records-only):

* audit/qa/hde-epic024/checks/D16\_close\_pack/primary.log

EPIC026 close-pack generator (fixed outputs):

* tools/qa/generate\_epic026\_close\_pack.py

Generated close-pack outputs (records-only where applicable):

* audit/EPIC-026\_MANIFEST.json

* audit/EPIC-026\_MANIFEST.json.path\_proof.txt

* audit/EPIC-026\_close\_report.md

* audit/EPIC-026\_close\_report.md.path\_proof.txt

* audit/docdeltas/hde-epic026\_doc\_deltas.md  
* audit/EPIC-026\_close\_report.md.path\_proof.txt

* audit/EPIC-026\_close\_pack.md

* audit/docdeltas/hde-epic026\_doc\_deltas.md

* audit/docdeltas/hde-epic026\_drain\_targets.md

* audit/qa/hde-epic026/00\_meta/doc\_deltas.md

* audit/qa/hde-epic026/qa\_step\_logs\_manifest.json

* audit/qa/hde-epic026/qa\_step\_logs\_manifest.json.path\_proof.txt

Generator posture (normative):

* The generator MUST run under closed rails for governed close-pack regeneration:

  * SAFE\_MODE \= 1

  * ALLOW\_NETWORK \= 0

* The generator MUST regenerate the governed close-pack artifacts above as tool-produced outputs. Do not hand-edit the generated manifest, close report, doc-delta ledger outputs, or companion path-proof transcripts.

* Where the close-pack enumerates named output bindings, close-pack validation MUST validate named bindings and exact path values rather than list membership.

EPIC026 close-pack validation check (po-012) observed step outputs (records-only):

* `audit/qa/hde-epic026/checks/po-012/primary.log`

* `audit/qa/hde-epic026/checks/po-012/generator_stdout.log`

* `audit/qa/hde-epic026/checks/po-012/generator_stderr.log`

* `audit/qa/hde-epic026/checks/po-012/generator_rc.txt`

* `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_manifest.json`

* `audit/qa/hde-epic026/checks/po-012/close_pack_copy/epic-026_evidence_index.json`

* `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json`

* `audit/qa/hde-epic026/checks/po-012/close_pack_copy/endpoints_catalog.json.sha256`

Validation posture (records-only). This check uses step-scoped stdout, stderr, and rc captures to verify the close-pack generator entrypoint `python tools/qa/generate_epic026_close_pack.py`. The `close_pack_copy/` family is a validation copy set and does not replace the governed close-pack outputs listed above.

## **37.4 Machine Mirror (records-only)**

Every artifact listed in this registry MUST have a 1:1 record in artifacts/evidence\_index.jsonl.

Required fields per record:

* artifact\_key

* role

* sha256

* size\_bytes

* produced\_at\_utc

* discovered\_physical\_path

* proof\_anchor (path-proof transcript)

Exact field order (normative):

* artifact\_key

* discovered\_physical\_path

* produced\_at\_utc

* proof\_anchor

* role

* sha256

* size\_bytes

Discipline:

* Sort-before-write by (artifact\_key, discovered\_physical\_path).

* Unknown keys are rejected.

* One LF per record; no blank lines.

* Update the Human Index and Machine Mirror in the same commit/PR.

Acceptance (routing only). Acceptance token naming and semantics are owned by HDE-Governance (titles-only). This guide does not list token names. CI must enforce machine mirror canonical JSONL discipline, unknown-key rejection, fixed field set/order as defined by the mirror schema, and strict 1:1 parity with the Human Evidence Index, with path-proofs required.

EPIC027 early Live QA evidence paths observed (records-only):

* checks/po-001:

  * `audit/qa/hde-epic027/checks/po-001/primary.log`

  * `audit/qa/hde-epic027/checks/po-001/route_inventory.txt`

  * `audit/qa/hde-epic027/checks/po-001/dev_conjunction_http.txt`

  * `audit/qa/hde-epic027/checks/po-001/endpoint_catalog.txt`

* checks/po-002:

  * `audit/qa/hde-epic027/checks/po-002/primary.log`

  * `audit/qa/hde-epic027/checks/po-002/compat_surface.txt`

  * `audit/qa/hde-epic027/checks/po-002/compat_identity_discovery.txt`

* checks/po-003:

  * `audit/qa/hde-epic027/checks/po-003/primary.log`

  * `audit/qa/hde-epic027/checks/po-003/cli_emitter_proof.txt`

  * `audit/qa/hde-epic027/checks/po-003/showcompat_parity.txt`

  * `audit/qa/hde-epic027/checks/po-003/showcompat_help.txt`

* checks/po-004:

  * `audit/qa/hde-epic027/checks/po-004/primary.log`

  * `audit/qa/hde-epic027/checks/po-004/entrypoint_proof.txt`

  * `audit/qa/hde-epic027/checks/po-004/cli_install_help.txt`

  * `audit/qa/hde-epic027/checks/po-004/bg_resolve_test.txt`

  * `audit/qa/hde-epic027/checks/po-004/bg_resolve_help.txt`

* checks/po-005:

  * `audit/qa/hde-epic027/checks/po-005/primary.log`

  * `audit/qa/hde-epic027/checks/po-005/reader_a7_transport.txt`

  * `audit/qa/hde-epic027/checks/po-005/catalog_routes.txt`

* checks/po-006:

  * `audit/qa/hde-epic027/checks/po-006/primary.log`

  * `audit/qa/hde-epic027/checks/po-006/dev_conjunction_http.txt`

  * `audit/qa/hde-epic027/checks/po-006/writer_index_rows.txt`

* checks/po-007:

  * `audit/qa/hde-epic027/checks/po-007/primary.log`

  * `audit/qa/hde-epic027/checks/po-007/update_evidence_index_write.txt`

  * `audit/qa/hde-epic027/checks/po-007/update_evidence_index_check.txt`

  * `audit/qa/hde-epic027/checks/po-007/orientation_demo_write.txt`

  * `audit/qa/hde-epic027/checks/po-007/orientation_demo_check.txt`

  * `audit/qa/hde-epic027/checks/po-007/validate_evidence_paths.txt`

  * `audit/qa/hde-epic027/checks/po-007/check_lf_endings.txt`

  * `audit/qa/hde-epic027/checks/po-007/check_mirror_schema.txt`

  * `audit/qa/hde-epic027/checks/po-007/qa_step_manifest_lookup.txt`

* checks/po-008:

  * `audit/qa/hde-epic027/checks/po-008/primary.log`

  * `audit/qa/hde-epic027/checks/po-008/generate_close_pack.txt`

  * `audit/qa/hde-epic027/checks/po-008/close_pack_bindings.txt`

  * `audit/qa/hde-epic027/checks/po-008/qa_step_manifest_lookup.txt`

* checks/po-009:

  * `audit/qa/hde-epic027/checks/po-009/primary.log`

  * `audit/qa/hde-epic027/checks/po-009/catalog_surface_inventory.txt`

  * `audit/qa/hde-epic027/checks/po-009/token_inventory.txt`

* checks/po-010:

  * `audit/qa/hde-epic027/checks/po-010/primary.log`

  * `audit/qa/hde-epic027/checks/po-010/runtime_log_presence.txt`

  * `audit/qa/hde-epic027/checks/po-010/runtime_surface_inventory.txt`

EPIC027 current-state step notes (records-only).

* `checks/po-005` confirms `/reader` as the cataloged A7-eligible success-route target for the step and keeps `/internal/version` outside the A7 PASS target family.

* `checks/po-006` confirms the writer proof remains outside the A7 family and records writer-family discoverability in the Machine Mirror.

* `checks/po-007` records `epic027.qa_step_logs_manifest` coverage in `tools/evidence/update_evidence_index.py`, `docs/evidence/INDEX.json`, and `artifacts/evidence_index.jsonl`.

* `checks/po-008` records that the close-pack generator ran, that close-pack bindings point to the EPIC027 QA root and current canonical ledger files, that the EPIC027 qa-step manifest is ledger-bound, and that the blocked branch for this step cleared once `po-007` reached PASS.

* `checks/po-009` records PASS inventory checks for catalog surfaces, no unexpected public success surface, no non-canonical token names introduced, and manifest-pair refresh from the `po-009` primary.log governed header.

* `checks/po-010` records PASS runtime proof across CLI, dev-http-conjunction, and reader-a7 surfaces, with no missing prerequisite runtime logs and with the refreshed manifest pair returned to fresh internal provenance after the byte-changing refresh.

Shared per-epic current-state manifest pair refreshed by po-001 to po-010:

* `audit/qa/hde-epic027/qa_step_logs_manifest.json`

* `audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt`

EPIC028 early Live QA evidence paths observed (records-only):

* checks/d0:  
  * `audit/qa/hde-epic028/checks/d0/primary.log`  
  * `audit/qa/hde-epic028/checks/d0/runtime_context.txt`  
  * `audit/qa/hde-epic028/checks/d0/cli_health.txt`  
  * `audit/qa/hde-epic028/checks/d0/services_surfaces.txt`  
  * `audit/qa/hde-epic028/checks/d0/d0_exact_commands.sh`  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`  
* checks/po-001:  
  * `audit/qa/hde-epic028/checks/po-001/primary.log`  
  * `audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt`  
* checks/po-002:  
  * `audit/qa/hde-epic028/checks/po-002/primary.log`  
  * `audit/qa/hde-epic028/checks/po-002/reader_v1_emitter_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-002/runtime_public_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-002/emitter_symbol_proof_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-002/serializer_grep_guard_snapshot.txt`  
* checks/po-003:  
  * `audit/qa/hde-epic028/checks/po-003/primary.log`  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.txt`  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.stderr.txt`  
  * `audit/qa/hde-epic028/checks/po-003/hdctl_help.rc.txt`  
  * `audit/qa/hde-epic028/checks/po-003/showcompat_presence.txt`  
  * `audit/qa/hde-epic028/checks/po-003/emitter_symbol_proof_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-003/serializer_grep_guard_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-003/reader_cli_parity_probe.txt`  
* checks/po-004:  
  * `audit/qa/hde-epic028/checks/po-004/primary.log`  
  * `audit/qa/hde-epic028/checks/po-004/pytest_stdout.log`  
  * `audit/qa/hde-epic028/checks/po-004/pytest_stderr.log`  
  * `audit/qa/hde-epic028/checks/po-004/pytest_rc.txt`  
  * `audit/qa/hde-epic028/checks/po-004/success_encoding_invariance_snapshot.txt`  
* checks/po-005:  
  * `audit/qa/hde-epic028/checks/po-005/primary.log`  
  * `audit/qa/hde-epic028/checks/po-005/catalog_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-005/http_reader_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-005/context_note_pre_po010_moonloop.txt`  
* checks/po-006:  
  * `audit/qa/hde-epic028/checks/po-006/primary.log`  
  * `audit/qa/hde-epic028/checks/po-006/po_005_lookup.txt`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stdout.log`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_stderr.log`  
  * `audit/qa/hde-epic028/checks/po-006/pytest_rc.txt`  
  * `audit/qa/hde-epic028/checks/po-006/context_note_pre_po010_moonloop.txt`  
* checks/po-007:  
  * `audit/qa/hde-epic028/checks/po-007/primary.log`  
  * `audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json`  
  * `audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl`  
* checks/po-008:  
  * `audit/qa/hde-epic028/checks/po-008/primary.log`  
  * `audit/qa/hde-epic028/checks/po-008/json_gate_family_before.txt`  
  * `audit/qa/hde-epic028/checks/po-008/canonical_json_family_before.txt`  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stdout.log`  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.stderr.log`  
  * `audit/qa/hde-epic028/checks/po-008/run_canonical_json_gate.rc.txt`  
  * `audit/qa/hde-epic028/checks/po-008/json_gate_family_after.txt`  
  * `audit/qa/hde-epic028/checks/po-008/canonical_json_family_after.txt`  
* checks/po-009:  
  * `audit/qa/hde-epic028/checks/po-009/primary.log`  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stdout.log`  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.stderr.log`  
  * `audit/qa/hde-epic028/checks/po-009/update_evidence_index.rc.txt`  
  * `audit/qa/hde-epic028/checks/po-009/index_snapshot.json`  
  * `audit/qa/hde-epic028/checks/po-009/index_sha_snapshot.txt`  
  * `audit/qa/hde-epic028/checks/po-009/mirror_path_proof_snapshot.txt`  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`  
  * `audit/qa/hde-epic028/checks/po-009/manifest_updater_lookup.txt`  
  * `audit/qa/hde-epic028/checks/po-009/manifest_human_index_lookup.txt`  
  * `audit/qa/hde-epic028/checks/po-009/manifest_mirror_lookup.txt`  
* checks/po-010:  
  * `audit/qa/hde-epic028/checks/po-010/primary.log`  
  * `audit/qa/hde-epic028/checks/po-010/final_summary.txt`

Step-0B bounded Moon Loop delta artifacts (records-only):

* `audit/qa/hde-epic028/00_meta/delta/patch.diff`  
* `audit/qa/hde-epic028/00_meta/delta/changed_files.txt`

EPIC028 current-state step notes (records-only).

* `checks/d0` records the stable EPIC028 QA root, expected `/api/compat/v1`, `/reader`, and `/internal/version` surfaces, the step-manifest pair, and the no-nested-root posture.  
* `checks/po-001` captures `normalize_pair`, `pair_key`, `compat_public`, and `emit_public` on the governed internal compatibility emission path.  
* `checks/po-002` records Reader/public routing through the governed emitter path and PASS snapshots for the governed CLI emitter and serializer guards.  
* `checks/po-003` records `hdctl --help` success, showcompat presence, PASS guard snapshots, and a non-zero Reader↔CLI parity probe without introducing a new route or flag.  
* `checks/po-004` records a passing Reader transport test and a readable `success_encoding_invariance` snapshot without introducing a new public route or payload contract.  
* `checks/po-005` records a PASS governed Reader proof-surface designation for `/reader` in current EPIC028 scope, with the catalog row and adapter ownership snapshots captured under the check root; the later bounded Moon Loop preserves the contextual note in `context_note_pre_po010_moonloop.txt`.  
* `checks/po-006` records a PASS Reader transport proof run that depends on the resolved `po-005` lookup, with `pytest_rc.txt` equal to `0`; the later bounded Moon Loop preserves the contextual note in `context_note_pre_po010_moonloop.txt`.  
* `checks/po-007` records the current-epic single-home acceptance binding and the matching Machine Mirror rows for the EPIC028 acceptance map, token matrix, and viability log, with no alternate acceptance-map home detected.  
* `checks/po-008` records same-change coherence for the two governed canonical JSON gate families, with `run_canonical_json_gate.rc.txt` equal to `0` and both families present before and after the run.  
* `checks/po-009` records a PASS refresh of the Human ledger, Machine Mirror, and companion proof family, with `update_evidence_index.py` exiting `0`, the current-run step-manifest pair rebuilt under the EPIC028 QA root, and all three manifest lookup artifacts reporting `found=True`.  
* `checks/po-010` records a repo-supported completion summary with `repo_supported_completion_only: yes`, `canon_drain_complete: no_claim`, and `formal_close_pack_complete: no_claim`, and records `po_005=recorded`, `po_006=recorded`, and `po_009=recorded`.  
* The bounded Moon Loop rerun for `po-010` captures the Step-0B delta pair under `audit/qa/hde-epic028/00_meta/delta/` and removes the `blocked_note.txt` trigger files for `po-005` and `po-006` after preserving their context notes.

Shared per-epic current-state manifest pair refreshed through po-009:

* `audit/qa/hde-epic028/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`

### **EPIC029 bounded conjunction closure artifact (records-only)**

* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`

EPIC029 bounded conjunction inventory note (records-only).

* The artifact above records the required bounded minimum conjunction JSON loci `/reader`, `/dev/writer/conjunction`, and `/internal/dev/sampler`.  
* In the current observed state, the same artifact also records the same-family preview loci `/dev/reader/conjunction` and `/dev/sampler/conjunction` without widening the bounded minimum above.  
* The same inventory artifact records single-emitter verification for each included locus on the `emit_public -> sercanon` path.

EPIC029 early Live QA evidence paths observed (records-only):

* checks/po-001:  
  * `audit/qa/hde-epic029/checks/po-001/primary.log`  
  * `audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md`  
  * `audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json`  
  * `audit/qa/hde-epic029/checks/po-001/route_snapshot.txt`  
* checks/po-002:  
  * `audit/qa/hde-epic029/checks/po-002/primary.log`  
  * `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.output.log`  
  * `audit/qa/hde-epic029/checks/po-002/run_canonical_json_gate.rc.txt`  
  * `audit/qa/hde-epic029/checks/po-002/json_gate_structured_record.snapshot.json`  
  * `audit/qa/hde-epic029/checks/po-002/json_canonical_check.snapshot.log`  
* checks/po-003:  
  * `audit/qa/hde-epic029/checks/po-003/primary.log`  
  * `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.output.log`  
  * `audit/qa/hde-epic029/checks/po-003/test_dev_conjunction_http.rc.txt`  
  * `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.output.log`  
  * `audit/qa/hde-epic029/checks/po-003/generate_conjunction_writer_evidence.rc.txt`  
  * `audit/qa/hde-epic029/checks/po-003/conjunction_write_readback.snapshot.log`  
  * `audit/qa/hde-epic029/checks/po-003/conjunction_writer_summary.snapshot.json`  
  * `audit/qa/hde-epic029/checks/po-003/moon_loop_po_approval_entry.md`  
* checks/po-004:  
  * `audit/qa/hde-epic029/checks/po-004/primary.log`  
  * `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.output.log`  
  * `audit/qa/hde-epic029/checks/po-004/test_dev_sampler_http.rc.txt`  
  * `audit/qa/hde-epic029/checks/po-004/dev_start_reader.snapshot.sh`  
  * `audit/qa/hde-epic029/checks/po-004/dev_sampler_healthcheck.snapshot.py`  
* checks/po-005:  
  * `audit/qa/hde-epic029/checks/po-005/primary.log`  
  * `audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt`  
  * `audit/qa/hde-epic029/checks/po-005/exit_codes.snapshot.txt`  
  * `audit/qa/hde-epic029/checks/po-005/codespaces_dev_sampler_url.snapshot.md`  
  * `audit/qa/hde-epic029/checks/po-005/local_dev_sampler_url.snapshot.md`  
  * `audit/qa/hde-epic029/checks/po-005/binding_disposition.snapshot.md`  
* checks/po-006:  
  * `audit/qa/hde-epic029/checks/po-006/primary.log`  
  * `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.output.log`  
  * `audit/qa/hde-epic029/checks/po-006/test_endpoint_catalog.rc.txt`  
  * `audit/qa/hde-epic029/checks/po-006/endpoints_catalog.snapshot.json`  
* checks/po-007:  
  * `audit/qa/hde-epic029/checks/po-007/primary.log`  
  * `audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log`  
  * `audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt`

EPIC029 early Live QA current-state notes (records-only).

* checks/po-001 records a PASS bounded conjunction closeout slice by binding the conjunction inventory snapshot, Endpoint Catalog snapshot, and adapter route snapshot to the in-scope surface family under `audit/qa/hde-epic029/checks/po-001/`.  
* checks/po-002 records a PASS canonical JSON gate step by binding the gate return-code artifact and the governed structured and canonical snapshot pair under `audit/qa/hde-epic029/checks/po-002/`; the companion gate output log may be present as a zero-byte supplemental artifact when the governing pass criteria are satisfied by the return code and snapshot pair.  
* checks/po-003 records a PASS writer-envelope QA slice under `/dev/writer/conjunction`, with the HTTP test rc, writer evidence generator rc, readback snapshot, writer summary snapshot, and Moon Loop approval entry all bound under `audit/qa/hde-epic029/checks/po-003/`; the generator output log in this corrected family is non-empty.  
* checks/po-004 records a PASS dev sampler HTTP harness slice under `audit/qa/hde-epic029/checks/po-004/`, with the sampler HTTP test rc and output plus the repo-side `scripts/dev_start_reader.sh` and `scripts/qa/dev_sampler_healthcheck.py` snapshots bound as the required step artifacts; this step remains confined to the internal sampler family and does not promote `/internal/dev/sampler` into a public or cataloged proof surface.  
* checks/po-005 records a PASS normalized OPS-01 snapshot family under `audit/qa/hde-epic029/checks/po-005/`, with one published binding value `http://127.0.0.1:8000/internal/dev/sampler` captured in both environment URL snapshots and a binding-disposition snapshot that records direct runtime validation for `codespaces` and binding-equivalence closure for `local_dev`.  
* checks/po-006 records a PASS formal transport proof-surface step under `audit/qa/hde-epic029/checks/po-006/`, with the endpoint catalog test output and zero return code bound to the governed catalog snapshot; the snapshot confirms `/reader` as the formal A7 surface, keeps `/dev/writer/conjunction` not A7-eligible, and does not promote `/internal/dev/sampler` into the formal proof family.  
* checks/po-007 records a PASS functional-bundle step under `audit/qa/hde-epic029/checks/po-007/`, with the combined pytest output and zero return code bound to the governed step family; the accepted execution records a step-local dependency preflight in `primary.log` command provenance and does not add a second governed deliverable family beyond `primary.log`, `functional_bundle.output.log`, and `functional_bundle.rc.txt`.

EPIC030 early Live QA evidence paths observed (records-only):

* checks/po-001:  
  * `audit/qa/hde-epic030/checks/po-001/primary.log`  
  * `audit/qa/hde-epic030/checks/po-001/surface_inventory.txt`  
  * `audit/qa/hde-epic030/checks/po-001/exit_code.txt`  
* checks/po-002:  
  * `audit/qa/hde-epic030/checks/po-002/primary.log`  
  * `audit/qa/hde-epic030/checks/po-002/pytest_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-002/generator_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-002/pytest_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-002/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-002/exit_code.txt`  
  * `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json`  
* checks/po-003:  
  * `audit/qa/hde-epic030/checks/po-003/primary.log`  
  * `audit/qa/hde-epic030/checks/po-003/pytest_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-003/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-003/exit_code.txt`  
  * `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log`  
  * `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log`  
* checks/po-004:  
  * `audit/qa/hde-epic030/checks/po-004/primary.log`  
  * `audit/qa/hde-epic030/checks/po-004/pytest_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-004/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-004/exit_code.txt`  
  * `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json`  
  * `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt`  
* checks/po-005:  
  * `audit/qa/hde-epic030/checks/po-005/primary.log`  
  * `audit/qa/hde-epic030/checks/po-005/pytest_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-005/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-005/exit_code.txt`  
  * `audit/qa/hde-epic030/pr-03/compat_identity_binding.log`  
  * `audit/qa/hde-epic030/pr-03/compat_parity_binding.log`

EPIC030 early Live QA current-state notes (records-only).

* checks/po-001 records a PASS surface-inventory step under `audit/qa/hde-epic030/checks/po-001/`, with seeded route families present and no HDE-EPIC030 public-route widening recorded.  
* checks/po-002 records a PASS zero-weight handoff step under `audit/qa/hde-epic030/checks/po-002/`, with the PR-01 `zero_weight_handoff.json` proof showing zero-weight candidate exclusion while the positive-weight candidate remains in the sampler pool.  
* checks/po-003 records a PASS normalization evidence step under `audit/qa/hde-epic030/checks/po-003/`, with the PR-01 invalid-viewer-preferences and canonical-normalization comparison logs present and non-empty.  
* checks/po-004 records a PASS dev sampler harness step under `audit/qa/hde-epic030/checks/po-004/`, with the PR-02 two-run identity and dev/internal header artifacts present and non-empty, scoped to `/internal/dev/sampler`.  
* checks/po-005 records a PASS compatibility identity/parity step under `audit/qa/hde-epic030/checks/po-005/`, with the PR-03 identity and parity binding logs present and non-empty and recording order-neutral, identity-stable compatibility behavior for the implemented slice.

EPIC030 continued Live QA evidence paths observed (records-only):

* checks/po-006:  
  * `audit/qa/hde-epic030/checks/po-006/primary.log`  
  * `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json`  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.stderr`  
  * `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-006/pytest_rc.txt`  
  * `audit/qa/hde-epic030/pr-05/category_framework_binding.log`  
  * `audit/ops/hde-epic030/ops-02/files_sha256.txt`  
  * `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`  
* checks/po-007:  
  * `audit/qa/hde-epic030/checks/po-007/primary.log`  
  * `audit/qa/hde-epic030/checks/po-007/threshold_ownership.txt`  
  * `audit/qa/hde-epic030/checks/po-007/generator_stdout.log`  
  * `audit/qa/hde-epic030/checks/po-007/generator_stderr.log`  
  * `audit/qa/hde-epic030/checks/po-007/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-007/preflight.log`  
  * `audit/qa/hde-epic030/checks/po-007/exit_code.txt`  
  * `audit/qa/hde-epic030/pr-04/band_edges_binding.log`  
* checks/po-008:  
  * `audit/qa/hde-epic030/checks/po-008/primary.log`  
  * `audit/qa/hde-epic030/checks/po-008/status_gate.log`  
  * `audit/qa/hde-epic030/checks/po-008/preflight.log`  
  * `audit/qa/hde-epic030/checks/po-008/pytest_stdout.log`  
  * `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json`  
  * `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt`

EPIC030 continued Live QA current-state notes (records-only):

* checks/po-006 records a PASS public compatibility and OPS-02 validation step under `audit/qa/hde-epic030/checks/po-006/`, with public Reader bands-only numeric-free proof, OPS-02 evidence validation PASS, pytest and grep return codes `0`, and the OPS-02 complete evidence bundle bound for review. The bounded Moon Loop remediation for this step updated `audit/ops/hde-epic030/ops-02/files_sha256.txt` with a deterministic self-reference row, did not run a new vendor command, did not open network rails, and did not expand evidence roots.  
* checks/po-007 records a PASS threshold-ownership step under `audit/qa/hde-epic030/checks/po-007/`, with closed rails, required source loci present, `engine.compat.thresholds.THRESHOLDS_V1` as the governed compat threshold source, no duplicate threshold home introduced, generator return code `0`, and PR-04 `band_edges_binding.log` present with status PASS.  
* checks/po-008 records a PASS band-tuning proof step under `audit/qa/hde-epic030/checks/po-008/`, with generator, pytest, and artifact-presence return codes `0`, PR-04 `band_thresholds_diff.json` present, and PR-04 `band_thresholds_identity_hash.txt` accepted as the implemented identity-hash artifact. The bounded Moon Loop aligned the check from the stale planned `band_thresholds_identity.log` path to the implemented `band_thresholds_identity_hash.txt` path without code changes, PF-Canon edits, or new evidence roots.

EPIC030 final Live QA evidence paths observed for this slice (records-only):

* checks/po-009:  
  * `audit/qa/hde-epic030/checks/po-009/primary.log`  
  * `audit/qa/hde-epic030/checks/po-009/exit_code.txt`  
  * `audit/qa/hde-epic030/checks/po-009/generator_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-009/pytest_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-009/pytest_stdout.log`  
  * `audit/qa/hde-epic030/pr-05/category_framework_binding.log`  
  * `audit/qa/hde-epic030/pr-05/category_canonical_compare.log`  
  * `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json`  
* checks/po-010:  
  * `audit/qa/hde-epic030/checks/po-010/primary.log`  
  * `audit/qa/hde-epic030/checks/po-010/exit_code.txt`  
  * `audit/qa/hde-epic030/checks/po-010/fail_closed_visibility.txt`  
  * `audit/qa/hde-epic030/checks/po-010/pytest_rc.txt`  
  * `audit/qa/hde-epic030/checks/po-010/pytest_stdout.log`  
  * `tests/evidence/test_epic030_pr01_pr03_fail_closed_evidence.py`  
* checks/po-011:  
  * `audit/qa/hde-epic030/checks/po-011/primary.log`  
  * `audit/qa/hde-epic030/checks/po-011/traceability_summary.json`  
  * `audit/qa/hde-epic030/checks/po-011/exit_code.txt`  
* checks/po-012:  
  * `audit/qa/hde-epic030/checks/po-012/primary.log`  
  * `audit/qa/hde-epic030/checks/po-012/reused_history_classification.txt`  
  * `audit/qa/hde-epic030/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic030/00_meta/step_0b_primary.log`  
  * `audit/docdeltas/hde-epic030_doc_deltas.md`

EPIC030 final Live QA current-state notes for this slice (records-only):

* checks/po-009 records a PASS category-framework binding step under `audit/qa/hde-epic030/checks/po-009/`, with generator and pytest return codes `0`, primary log PASS, PR-05 `category_framework_binding.log` PASS, PR-05 `category_canonical_compare.log` PASS, per-channel mechanics PASS, public Reader bands-only numeric-free proof, and Human Index and Machine Mirror binding present.  
* checks/po-010 records a PASS generated-proof fail-closed step under `audit/qa/hde-epic030/checks/po-010/`. The first run correctly stopped at TOOLING\_BLOCKED because PR-01 through PR-03 lacked explicit fail-closed proof coverage. The accepted remediation added PR-01 through PR-03 fail-closed proof coverage, reran the full fail-closed suite with PR-01 through PR-05 proof families covered, recorded `fail_closed_visibility.txt` as proven for PR-01 through PR-05, and preserved non-claim posture for close-pack completion, PF-canon drainage completion, and acceptance-map closure.  
* checks/po-011 records a PASS traceability step under `audit/qa/hde-epic030/checks/po-011/`, with `traceability_summary.json` recording required PR-slice artifacts present, indexed in `docs/evidence/INDEX.json`, and mirrored in `artifacts/evidence_index.jsonl`, and with the primary log recording PASS, exit code `0`, and plan-copy command provenance.  
* checks/po-012 records a PASS reused-history classification step under `audit/qa/hde-epic030/checks/po-012/`, after bounded Step-0B precondition remediation restored `audit/docdeltas/hde-epic030_doc_deltas.md`, `audit/qa/hde-epic030/00_meta/doc_deltas.md`, and `audit/qa/hde-epic030/00_meta/step_0b_primary.log`. The final classification separates reused-history rows `HDE-DISS005.1`, `HDE-DISS006.1`, and `HDE-DISS006.2` from active HDE-EPIC030 rows and records `new_implementation_claim_for_reused_history: False`.

EPIC030 late Live QA evidence paths observed (records-only):

* checks/po-013:  
  * audit/qa/hde-epic030/checks/po-013/primary.log  
  * audit/qa/hde-epic030/checks/po-013/source\_of\_truth\_posture.txt  
* checks/po-014:  
  * audit/qa/hde-epic030/checks/po-014/primary.log  
  * audit/qa/hde-epic030/checks/po-014/all\_slice\_coherence.json  
  * audit/qa/hde-epic030/checks/po-014/exit\_code.txt  
* checks/po-015:  
  * audit/qa/hde-epic030/checks/po-015/primary.log  
  * audit/qa/hde-epic030/checks/po-015/discovery.json  
  * audit/qa/hde-epic030/checks/po-015/discovery\_validation.txt  
* checks/po-016:  
  * audit/qa/hde-epic030/checks/po-016/primary.log  
  * audit/EPIC-030\_QA\_RCA.md  
* checks/po-017:  
  * audit/qa/hde-epic030/checks/po-017/primary.log  
  * audit/qa/hde-epic030/checks/po-017/documentation\_drainage\_posture.txt

EPIC030 late Live QA current-state notes (records-only):

* checks/po-013 records a PASS source-of-truth posture step under audit/qa/hde-epic030/checks/po-013/, with repo-supported completion, canon-drain completion, and formal close-pack completion kept as separate states. The step records that documentation drainage is not a required execution gate before QA PASS.  
* checks/po-014 records a PASS all-slice coherence step under audit/qa/hde-epic030/checks/po-014/, with all prior po-001 through po-013 primary logs present, required PR-01 through PR-05 core artifacts present, and derived PASS status aligned with recorded primary-log status and exit code 0\.  
* checks/po-015 records a PASS baseline discovery step under audit/qa/hde-epic030/checks/po-015/, with discovery.json present and parseable, rails, paths, and surfaces present, and discovery\_validation.txt recording discovery validity.  
* checks/po-016 records a PASS QA RCA step under audit/qa/hde-epic030/checks/po-016/, with audit/EPIC-030\_QA\_RCA.md generated and containing Coverage vs QA Plan, Findings classification, Outcome meaning, evidence support, canon follow-up, and closeout-readiness interpretation.  
* checks/po-017 records a PASS documentation-drainage posture step under audit/qa/hde-epic030/checks/po-017/, with drainage\_blocker recorded as False, PF09.2 drainage before otherwise-proven QA PASS recorded as False, and real truth-and-proof blockers preserved as the relevant blocker class.  
* checks/po-015 and checks/po-016 record Plan \+ QA syntax correction command provenance for rendered Markdown exception-class syntax defects. The corrected executions preserve the approved proof targets, artifact families, and PASS/FAIL predicates, and the provenance is recorded in governed step evidence.

EPIC030 QA RCA and closeout interpretation posture (records-only). The QA RCA records source-of-truth posture, coverage vs QA Plan, QA timeline, findings classification, root cause analysis, remediation loop assessment, implementation gaps, doc deltas excluding PF10, and an explicit readiness recommendation. The recorded root cause class is proof-class and evidence-discipline separation across a Dissolution closeout, including no-user/vendor proof ambiguity, generated-proof fail-closed coverage gaps, and separation between repo-supported completion, PF09.2 drainage, and formal close-pack completion.

EPIC030 QA RCA remediation-loop notes (records-only):

* po-006 remediation updated audit/ops/hde-epic030/ops-02/files\_sha256.txt with a deterministic self-reference row and reran the existing tests, grep, OPS-02 validator, and header generation without running a new vendor command.  
* po-010 remediation changed an initial TOOLING\_BLOCKED posture to PASS after PR-01 through PR-03 generated proof families received explicit fail-closed coverage and the full po-010 suite reran.  
* po-011 and po-012 remediation used Step-0B precondition evidence to reduce ambiguity around reused-history and active-scope separation before final PASS.  
* The repeated evidence-generator lesson is that top-level PASS must derive from decisive predicate checks and not from partial or stale local state.

EPIC030 closeout readiness note (records-only). The recorded QA verdict is READY WITH CAVEATS. The caveats preserve that QA closeout readiness is not a claim that PF09.2 drainage is complete or that formal close-pack completion is proven beyond the surfaced close-pack artifacts and separate OPS review.

EPIC030 late Live QA evidence paths observed (records-only):

* checks/po-013:  
  * audit/qa/hde-epic030/checks/po-013/primary.log  
  * audit/qa/hde-epic030/checks/po-013/source\_of\_truth\_posture.txt  
* checks/po-014:  
  * audit/qa/hde-epic030/checks/po-014/primary.log  
  * audit/qa/hde-epic030/checks/po-014/all\_slice\_coherence.json  
  * audit/qa/hde-epic030/checks/po-014/exit\_code.txt  
* checks/po-015:  
  * audit/qa/hde-epic030/checks/po-015/primary.log  
  * audit/qa/hde-epic030/checks/po-015/discovery.json  
  * audit/qa/hde-epic030/checks/po-015/discovery\_validation.txt  
* checks/po-016:  
  * audit/qa/hde-epic030/checks/po-016/primary.log  
  * audit/EPIC-030\_QA\_RCA.md  
* checks/po-017:  
  * audit/qa/hde-epic030/checks/po-017/primary.log  
  * audit/qa/hde-epic030/checks/po-017/documentation\_drainage\_posture.txt

EPIC030 late Live QA current-state notes (records-only):

* checks/po-013 records a PASS source-of-truth posture step under audit/qa/hde-epic030/checks/po-013/, with repo-supported completion, canon-drain completion, and formal close-pack completion kept as separate states. The step records that documentation drainage is not a required execution gate before QA PASS.  
* checks/po-014 records a PASS all-slice coherence step under audit/qa/hde-epic030/checks/po-014/, with all prior po-001 through po-013 primary logs present, required PR-01 through PR-05 core artifacts present, and derived PASS status aligned with recorded primary-log status and exit code 0\.  
* checks/po-015 records a PASS baseline discovery step under audit/qa/hde-epic030/checks/po-015/, with discovery.json present and parseable, rails, paths, and surfaces present, and discovery\_validation.txt recording discovery validity.  
* checks/po-016 records a PASS QA RCA step under audit/qa/hde-epic030/checks/po-016/, with audit/EPIC-030\_QA\_RCA.md generated and containing Coverage vs QA Plan, Findings classification, Outcome meaning, evidence support, canon follow-up, and closeout-readiness interpretation.  
* checks/po-017 records a PASS documentation-drainage posture step under audit/qa/hde-epic030/checks/po-017/, with drainage\_blocker recorded as False, PF09.2 drainage before otherwise-proven QA PASS recorded as False, and real truth-and-proof blockers preserved as the relevant blocker class.  
* checks/po-015 and checks/po-016 record Plan \+ QA syntax correction command provenance for rendered Markdown exception-class syntax defects. The corrected executions preserve the approved proof targets, artifact families, and PASS/FAIL predicates, and the provenance is recorded in governed step evidence.

EPIC030 QA RCA and closeout interpretation posture (records-only). The QA RCA records source-of-truth posture, coverage vs QA Plan, QA timeline, findings classification, root cause analysis, remediation loop assessment, implementation gaps, doc deltas excluding PF10, and an explicit readiness recommendation. The recorded root cause class is proof-class and evidence-discipline separation across a Dissolution closeout, including no-user/vendor proof ambiguity, generated-proof fail-closed coverage gaps, and separation between repo-supported completion, PF09.2 drainage, and formal close-pack completion.

EPIC030 QA RCA remediation-loop notes (records-only):

* po-006 remediation updated audit/ops/hde-epic030/ops-02/files\_sha256.txt with a deterministic self-reference row and reran the existing tests, grep, OPS-02 validator, and header generation without running a new vendor command.  
* po-010 remediation changed an initial TOOLING\_BLOCKED posture to PASS after PR-01 through PR-03 generated proof families received explicit fail-closed coverage and the full po-010 suite reran.  
* po-011 and po-012 remediation used Step-0B precondition evidence to reduce ambiguity around reused-history and active-scope separation before final PASS.  
* The repeated evidence-generator lesson is that top-level PASS must derive from decisive predicate checks and not from partial or stale local state.

EPIC030 closeout readiness note (records-only). The recorded QA verdict is READY WITH CAVEATS. The caveats preserve that QA closeout readiness is not a claim that PF09.2 drainage is complete or that formal close-pack completion is proven beyond the surfaced close-pack artifacts and separate OPS review.

EPIC030 final closure review and retrospective bundle observed (records-only). The HDE-EPIC030 final closeout review records a satisfied closure trace for review purposes only. It is not a PO closeout action, not PF09.2 drainage, not a new QA PASS claim beyond the PF10-recorded check outcomes, and not a new acceptance-token source.

Final review source posture observed:

* PF10 is the primary record for epic-specific implementation events, remediation loops, ADRs, QA outcomes, evidence pointers, and review-close trace.  
* PF23 is current-reality context only and is not closure proof, a gate, or an acceptance source.  
* PF-Canon is normative where PF10 is silent.  
* PF19 and PF06 supplied QA RCA and close-gate interpretation where PF10 was silent.  
* The Implementation Guide and QA Plan were used only for intended scope, goals, requirements, and evidence framing.  
* PF20 was not used.

Final deliverable register observed:

* D1 zero-weight rule handoff.  
* D2 sampler endpoint harness.  
* D3 normalization evidence coverage.  
* D4 compatibility evidence and indexing.  
* D5 reused already-complete Dissolution foundations.  
* D6 band thresholds and tuning active carry-forward.  
* D7 category-framework active carry-forward.  
* Human Evidence Index and Machine Mirror governance.  
* Live QA close-stage proof.  
* Close-pack baseline, including `audit/EPIC-030_close_report.md`, `audit/EPIC-030_MANIFEST.json`, and sibling path proofs.

Final QA verification register observed:

* PO-001 boundary and no public widening.  
* PO-002 zero-weight handoff.  
* PO-003 normalization determinism.  
* PO-004 dev-only sampler harness.  
* PO-005 compatibility identity and order coherence.  
* PO-006 public numeric-free compatibility proof plus OPS-02 evidence.  
* PO-007 threshold ownership.  
* PO-008 tuning comparison and identity proof.  
* PO-009 category-framework proof.  
* PO-010 generated-proof fail-closed proof.  
* PO-011 governed evidence traceability.  
* PO-012 reused-history separation.  
* PO-013 drainage-state separation.  
* PO-014 all-slice coherence.  
* PO-015 baseline discovery and tool health.  
* PO-016 final QA interpretation.  
* PO-017 documentation-drainage non-blocker posture.

Final closure trace observed. D1 through D7, the public numeric-free compatibility proof, OPS-02 no-user vendor-backed implementation-validation evidence, D0 discovery and tool health, QA RCA and final QA interpretation, doc-delta non-blocker posture, close-pack pair and manifest, and PF09.2 later-drain support are all recorded as satisfied for the review trace. PF09.2 later-drain support remains not-drained and must not be described as already drained.

Final path and surface ledger observed. The review records these closure-relevant governed paths or surfaces as proven in PF10:

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `audit/qa/hde-epic030/checks/po-006/primary.log`  
* `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`  
* `audit/qa/hde-epic030/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic030/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/EPIC-030_close_report.md`  
* `audit/EPIC-030_close_report.md.path_proof.txt`  
* `audit/EPIC-030_MANIFEST.json`  
* `audit/EPIC-030_MANIFEST.json.path_proof.txt`  
* `audit/docdeltas/hde-epic030_doc_deltas.md`  
* `audit/docdeltas/hde-epic030_drain_targets.md`  
* `/api/compat/v1`  
* `/internal/dev/sampler`

Final path and surface context observed. The review records `/reader`, `presenter/reader_v1/emitter.py`, `engine/presenter/emitter.py`, `engine/bodygraph/vendor_client.py`, and `engine/charts/loader.py` as current-reality context rather than closure proof. The `engine/charts/loader.py` seam remains an unresolved reality/canon interpretation question unless adjudicated by the owning canon process.

Final closure decision observed. HDE-EPIC030 is recorded as SATISFIED for this review trace, with caveats. The caveats are later PF09.2 drainage and canonization of lessons learned. PF23 drift signals do not block the PF10-backed closure trace unless a later PO or canon decision turns them into executable work.

Final QA RCA mechanics lessons observed:

* The primary root cause was proof-class and evidence-discipline failure across a Dissolution closeout, not a single runtime failure.  
* The no-user environment made vendor-backed proof easy to confuse with user-ID or DB-backed proof.  
* Generated proof artifacts could appear green before decisive predicate binding was complete.  
* Implementation proof, QA proof, PF09.2 drain, and formal close-pack proof needed sharper separation.  
* po-006 Moon Loop was acceptable because it was bounded, PO-approved, evidence-scoped, did not open network rails, and did not expand evidence roots.  
* po-010 remediation was acceptable because it converted TOOLING\_BLOCKED into PASS by adding fail-closed coverage and rerunning the full po-010 suite.  
* po-011 and po-012 remediation were acceptable because Step-0B precondition remediation clarified reused-history and active-scope separation.  
* OPS-03 evidence-packaging remediation was acceptable because it repaired transcript, exit-code, stdout, inventory, and validation provenance defects while preserving packaging-only scope.

Final retrospective mechanics notes observed:

* The active implementation scope included normalization and zero-weight handoff, dev-only sampler harness, compatibility evidence and indexing, band-threshold and tuning carry-forward, and category-framework carry-forward.  
* The implementation was delivered as five PR slices and later Live QA checks po-001 through po-017.  
* OPS-01 remained TOOLING\_BLOCKED for exact no-secret no-user vendor command proof.  
* OPS-02 completed the vendor-backed no-user smoke as implementation-validation evidence.  
* OPS-03 completed close-pack evidence packaging and surfacing.  
* The evidence inventory includes PR-01 through PR-05 evidence families, po-001 through po-017 primary logs, the QA step-log manifest, QA RCA, close report, close manifest, doc-delta ledger, and drain-target ledger.  
* No closure-trace evidence gap remains visible in PF10.  
* PF09.2 actual drain is not proven and is intentionally non-claimed.  
* The strongest retained mechanics lessons are proof-class separation, governed evidence binding, generated-proof fail-closed posture, explicit no-user vendor-backed proof labels, multi-root evidence governance through index/mirror/path-proof discipline, and non-claim posture for PF09.2 drainage.

HDE-EPIC031 early Live QA evidence paths observed (records-only):

* checks/step-0a-discovery:  
  * `audit/qa/hde-epic031/00_meta/live_qa_harness.py`  
  * `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log`  
  * `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json`  
* checks/step-0b-doc-delta:  
  * `audit/docdeltas/hde-epic031_doc_deltas.md`  
  * `audit/qa/hde-epic031/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log`  
* checks/po-001:  
  * `audit/qa/hde-epic031/checks/po-001/primary.log`  
  * `audit/qa/hde-epic031/checks/po-001/result.json`  
* checks/po-002:  
  * `audit/qa/hde-epic031/checks/po-002/primary.log`  
  * `audit/qa/hde-epic031/checks/po-002/result.json`  
* checks/po-003:  
  * `audit/qa/hde-epic031/checks/po-003/primary.log`  
  * `audit/qa/hde-epic031/checks/po-003/result.json`  
* checks/po-004:  
  * `audit/qa/hde-epic031/checks/po-004/primary.log`  
  * `audit/qa/hde-epic031/checks/po-004/result.json`  
* checks/po-005:  
  * `audit/qa/hde-epic031/checks/po-005/primary.log`  
  * `audit/qa/hde-epic031/checks/po-005/result.json`  
* checks/po-006:  
  * `audit/qa/hde-epic031/checks/po-006/primary.log`  
  * `audit/qa/hde-epic031/checks/po-006/result.json`  
  * `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`  
  * `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`  
  * `audit/qa/hde-epic031/00_meta/doc_deltas.md`

HDE-EPIC031 early Live QA current-state notes observed (records-only).

* Step-0A and Step-0B record PASS under closed rails and deterministic capture pins, with no blocking or tooling states observed. Step-0A records discovery under `audit/qa/hde-epic031/checks/step-0a-discovery/`; Step-0B records the doc-delta pair and primary log under the governed roots listed above.  
* Step-0A records an accepted plan-execution drift: one plan action referenced `audit/qa/hde-epic031/00_meta/discovery.json`, while the plan-required deliverable and execution helper used `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json`. The final posture is non-blocking because the required check-root deliverable exists and current-state evidence remains under the stable check directory.  
* checks/po-001 records a PASS first-slice scope-boundary proof under `audit/qa/hde-epic031/checks/po-001/`, including no public-surface widening and no later vendor-version, database, router, close-pack, or acceptance expansion claim for this slice. It also records an accepted plan-guidance mismatch between the plan key `no_epic031_public_route` and the reported evidence key `no_epic031_public_surface`.  
* checks/po-002 records a PASS closed-by-default provider-access proof under `audit/qa/hde-epic031/checks/po-002/`, including closed-default refusal, bounded opening evidence, provider tests, and preserved no-live-vendor policy.  
* checks/po-003 records a PASS deterministic typed-provider-refusal proof under `audit/qa/hde-epic031/checks/po-003/`, including typed refusal markers and explicit refusal-before-input-or-ingest ordering evidence.  
* checks/po-004 records a PASS bounded retry/backoff and non-success-classification proof under `audit/qa/hde-epic031/checks/po-004/`, including pinned attempts, retry/backoff evidence, and non-success behavior not treated as success.  
* checks/po-005 records a PASS typed rate-limit and Retry-After proof under `audit/qa/hde-epic031/checks/po-005/`, including typed `429` handling, Retry-After parsing evidence, and behavior not reported as success.  
* checks/po-006 records a PASS keys-only provider diagnostics proof under `audit/qa/hde-epic031/checks/po-006/`, including `allowed_keys_present: true`, payload-body absence, plaintext-secret absence, raw-secret-header absence, and generator check return code `0`.  
* checks/po-006 records an accepted Moon Loop remediation of the QA-created harness predicate in `audit/qa/hde-epic031/00_meta/live_qa_harness.py`. The initial predicate produced a false `FAIL_BEHAVIOR` despite PR-02 generator and redaction evidence being PASS. The accepted remediation aligned `check_po006` with the canonical redaction schema fields `allowed_keys` and `status`, captured failure signature, remediation note, rerun PASS excerpt, patch, changed-files sha256 evidence, and doc-delta note, and stayed inside the already-scoped PO-006 evidence family.

HDE-EPIC031 continued Live QA evidence paths observed (records-only):

* checks/po-007:  
  * `audit/qa/hde-epic031/checks/po-007/primary.log`  
  * `audit/qa/hde-epic031/checks/po-007/result.json`  
* checks/po-008:  
  * `audit/qa/hde-epic031/checks/po-008/primary.log`  
  * `audit/qa/hde-epic031/checks/po-008/result.json`  
  * `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`  
  * `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`  
  * `audit/qa/hde-epic031/pr-03/evidence_family_map.json`  
  * `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`  
  * `audit/qa/hde-epic031/pr-03/evidence_refresh.log`  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
  * `artifacts/compat/AB.json`  
  * `artifacts/compat/BA.json`  
* checks/po-009:  
  * `audit/qa/hde-epic031/checks/po-009/primary.log`  
  * `audit/qa/hde-epic031/checks/po-009/result.json`  
* checks/po-010:  
  * `audit/qa/hde-epic031/checks/po-010/primary.log`  
  * `audit/qa/hde-epic031/checks/po-010/result.json`  
* checks/po-011:  
  * `audit/qa/hde-epic031/checks/po-011/primary.log`  
  * `audit/qa/hde-epic031/checks/po-011/result.json`  
* checks/po-012:  
  * `audit/qa/hde-epic031/checks/po-012/primary.log`  
  * `audit/qa/hde-epic031/checks/po-012/result.json`  
* checks/po-013:  
  * `audit/qa/hde-epic031/checks/po-013/primary.log`  
  * `audit/qa/hde-epic031/checks/po-013/result.json`  
* checks/po-014:  
  * `audit/qa/hde-epic031/checks/po-014/primary.log`  
  * `audit/qa/hde-epic031/checks/po-014/result.json`  
* checks/po-015:  
  * `audit/qa/hde-epic031/checks/po-015/primary.log`  
  * `audit/qa/hde-epic031/checks/po-015/result.json`  
* checks/po-016:  
  * `audit/qa/hde-epic031/checks/po-016/primary.log`  
  * `audit/qa/hde-epic031/checks/po-016/result.json`  
* checks/po-017:  
  * `audit/qa/hde-epic031/checks/po-017/primary.log`  
  * `audit/qa/hde-epic031/checks/po-017/result.json`  
* checks/po-018:  
  * `audit/qa/hde-epic031/checks/po-018/primary.log`  
  * `audit/qa/hde-epic031/checks/po-018/result.json`

HDE-EPIC031 continued Live QA current-state notes observed (records-only).

* checks/po-007 records a PASS sensitive-provider-data absence proof under `audit/qa/hde-epic031/checks/po-007/`, including redaction scan presence, sensitive provider material absence from QA-visible diagnostics, and live vendor calls remaining forbidden.  
* checks/po-008 records a PASS governed human and machine evidence-coherence proof under `audit/qa/hde-epic031/checks/po-008/`, after Moon Loop remediation. The final evidence records command success, PR-03 coherence status PASS, Human Evidence Index and Machine Mirror coherence, hash-sentinel presence, and changed-files proof for the affected evidence/index family.  
* checks/po-008 records an accepted Moon Loop remediation for governed coherence/index artifacts. The initial evidence recorded stale or proof-mtime failures while coherence status was PASS. The accepted remediation refreshed governed coherence/index artifacts under closed rails, normalized `artifacts/compat/AB.json` and `artifacts/compat/BA.json` filesystem mtimes with bytes unchanged, captured failure signature, remediation note, rerun PASS excerpt, patch, changed-files proof, and remained acceptable as an auditable in-session remediation.  
* checks/po-009 records a PASS machine-readable evidence alignment proof under `audit/qa/hde-epic031/checks/po-009/`, including family-map presence, family-map type `dict`, Machine Mirror presence, mirror mention of EPIC031, mirror path-proof existence, and mirror-schema success as reported in the adjacent governed evidence stream.  
* checks/po-010 records a PASS generated-proof fail-closed proof under `audit/qa/hde-epic031/checks/po-010/`. The current evidence resolves the prior PR-01 check-mode blocker with `pr01_generator_check_mode_present: true`, records PR-02 and PR-03 generator check return codes as `0`, records PR-03 evidence coherence success, and records final status PASS.  
* checks/po-011 records a PASS acceptance-claim boundary proof under `audit/qa/hde-epic031/checks/po-011/`. The check records no claimed tokens, keeps missing acceptance-map or token-matrix posture as close-stage rather than runtime behavior proof, and records `claims_limited_to_evidence_scope: true`.  
* checks/po-012 records a PASS active-Fermentation-subtask support proof under `audit/qa/hde-epic031/checks/po-012/`. The check records `hde_ferm001_2_supported: true`, `hde_ferm001_3_supported: true`, and `hde_ferm001_4_supported: true`, while explicitly recording `pf09_5_drain_claimed: false`.  
* checks/po-013 records a PASS reused-foundation boundary proof under `audit/qa/hde-epic031/checks/po-013/`. The check records reused foundation as history-only, no new implementation claim for the reused foundation, and active slice work limited to HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4.  
* checks/po-014 records a PASS implementation-readiness boundary proof under `audit/qa/hde-epic031/checks/po-014/`. The check records prior logs present, PO-014 preflight success, and implementation readiness not treated as final QA outcome.  
* checks/po-015 records a PASS truth-class separation proof under `audit/qa/hde-epic031/checks/po-015/`. The check records implementation readiness, QA readiness, final QA outcome, and documentation drainage as separate, and records PF09.5 drainage as not required before QA PASS.  
* checks/po-016 records a PASS vendor-version runtime non-claim proof under `audit/qa/hde-epic031/checks/po-016/`. The check records no vendor-version runtime conformance claim and visible no-live-vendor policy.  
* checks/po-017 records a PASS live-vendor-behavior non-claim proof under `audit/qa/hde-epic031/checks/po-017/`. The check records no live vendor behavior claim, local proof kept separate from live vendor proof, and live vendor calls forbidden.  
* checks/po-018 records a PASS Live QA proof-only boundary under `audit/qa/hde-epic031/checks/po-018/`. The check records no implementation, remediation, PF edit, or closeout action performed by Live QA, and records the Live QA role as proving current results only.  
* PO-013, PO-014, PO-015, PO-016, PO-017, and PO-018 primary logs record captured rails and determinism environment fields, including SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, LC\_ALL, LANG, and TZ.

HDE-EPIC031 final QA RCA and closeout interpretation observed (records-only).

* The QA RCA records PF10 as primary for HDE-EPIC031-specific QA events, outcomes, remediation loops, ADRs, and evidence pointers. It records PF19 as QA process and RCA basis where PF10 is silent, PF06 only for the close-gate QA RCA and Doc Delta summary requirement, no PF27 use, no Implementation Guide goal framing, and QA Plan use only for intended requirements framing.  
* The QA timeline is recorded in PF10 source order with no chronological reordering. The timeline records PR-01, PR-02, and PR-03 remediation loops, the HDE-EPIC031 retrospective, PF23 audit analysis, Step-0A and Step-0B, and PO-001 through PO-018 as the ordered QA and remediation chain.  
* The RCA records all QA Plan checks from Step-0A through PO-018 as fully evidenced. The recorded mismatches or deviations are non-blocking for closeout: Step-0A discovery sidecar path drift, PO-001 plan-key wording drift, PO-006 Moon Loop false FAIL predicate remediation, PO-008 Moon Loop evidence-coherence remediation, and PO-010 prior blocker remediation.  
* The RCA records the PR-01, PR-02, and PR-03 implementation evidence chain as strong: PR-01 provider policy proof, PR-02 log and redaction posture, and PR-03 evidence/index coherence.  
* The RCA root cause is proof-boundary and evidence-coupling difficulty in the first provider-control Fermentation slice: provider non-success statuses needed exact classification, redirect behavior needed default-path coverage, vendor-specific evidence needed PR-specific homes, generated proofs needed fail-closed side-effect validation, and Live QA needed to preserve separation between implementation readiness, final QA outcome, PF09.5 drainage, formal close-pack completion, vendor-version conformance, and live vendor behavior.  
* The RCA records why detection was hard: some failures appeared only when the proof path matched actual runtime or evidence-generator behavior. The injected request test did not expose default urllib redirect following, and generated evidence could look green unless side-effect paths, proof companions, and mirror rows were validated as a family.  
* The RCA records why closeout was hard: the closeout had to prove PASS while avoiding overclaims. It records no live vendor behavior, no vendor-version runtime conformance, no acceptance-token claim from tokenless Live QA checks, no PF09.5 drainage claim, and no formal close-pack completion claim from Live QA alone.  
* The RCA records remediation loops as useful because PR-01 fixed retry classification and redirect handling, PR-02 moved vendor evidence away from shared DB-bridge paths into PR-specific audit paths, PR-03 converted outside-family proof churn into explicit side-effect classification and fail-closed validation, PO-006 corrected a false FAIL\_BEHAVIOR harness predicate, PO-008 restored governed evidence coherence, and PO-010 resolved the prior generator check-mode blocker.  
* The RCA records no new PF-canon doc deltas required from the RCA itself.  
* The RCA verdict is Ready with caveats. The caveats are formal close-pack completion, PF09.5 drainage, parent-task posture, and deferred later Fermentation work, not failed Live QA behavior.  
* Deferred later Fermentation work remains visible as future scope only: HDAPI v2 runtime and live conformance, DB bridge and DB runtime acceptance, router parity, narrative registry closure, and parent HDE-FERM001 status posture. This records a no-claim boundary only; it does not create PF14 tasks, PF09 statuses, acceptance tokens, closeout gates, or future implementation scope by itself.

HDE-EPIC031 Lead Dev retrospective observed (records-only). The retrospective records HDE-EPIC031 as SATISFIED for this review’s closure trace only. It is not a PO closeout action, not PF09.5 drainage, not formal close-pack completion, not a new acceptance-token source, and not a claim of HDAPI v2 runtime conformance or live vendor behavior.

Final review source posture observed:

* PF10 is primary for HDE-EPIC031-specific implementation records, QA events, remediation loops, ADRs, outcomes, and evidence pointers.  
* PF23 is read-only current-reality context only. It may support or challenge component, pathname, surface, or evidence-surface interpretation, but it does not prove closure or create blockers by itself.  
* PF-Canon is normative where PF10 is silent.  
* The Implementation Guide is used only for intended scope framing.  
* The QA Plan is used only for intended QA requirements framing.  
* PF20 was not used.

Final Lead Dev deliverable and QA registers observed:

* The first Fermentation Pass 2 SAFE rails slice is recorded as limited to `HDE-FERM001.2`, `HDE-FERM001.3`, and `HDE-FERM001.4`.  
* PR-01 records the SAFE rails open posture and integration-gate slice.  
* PR-02 records the SAFE rails observability and secret-safe log posture slice.  
* PR-03 records SAFE rails governed evidence and indexing coherence.  
* CLI Aux preview is recorded as an already-complete reused foundation, not new implementation scope for this epic.  
* Deferred later Fermentation rows remain out of current scope: `HDE-FERM006`, `HDE-FERM007`, and `HDE-FERM008`.  
* No public Reader contract, route, flag, payload field, or HDAPI v2 runtime expansion is recorded for this slice.  
* Governed evidence binding is recorded through the Human Evidence Index, Machine Mirror, hash sentinel, and path proofs.  
* Step-0A, Step-0B, and PO-001 through PO-018 are recorded as PASS, including accepted Moon Loop remediation for PO-006 and PO-008 and resolved prior blocker posture for PO-010.  
* Final QA closeout posture is recorded as READY WITH CAVEATS.

Final Lead Dev path and surface ledger observed:

* `audit/qa/hde-epic031/`  
* `audit/qa/hde-epic031/checks/`  
* `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json`  
* `audit/qa/hde-epic031/00_meta/discovery.json` as framing-only drift, not closure proof  
* `audit/docdeltas/hde-epic031_doc_deltas.md`  
* `audit/qa/hde-epic031/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic031/checks/po-001/primary.log`  
* `audit/qa/hde-epic031/checks/po-006/primary.log`  
* `audit/qa/hde-epic031/checks/po-010/primary.log`  
* `audit/qa/hde-epic031/qa_step_logs_manifest.json`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`  
* `/reader` as public Reader route context, not closure proof by itself  
* `/api/compat/v1` as internal/admin compat context, not closure proof by itself  
* `engine/bodygraph/vendor_client.py` as vendor seam context, not closure proof by itself  
* `engine/bodygraph/ingest.py` as current-reality context only  
* `engine/bodygraph/resolver.py` as provider-gate context only  
* `engine/compat/compute.py` as current-reality seam context only  
* `presenter/` as namespace context only  
* `engine/presenter/` as namespace context only  
* `audit/EPIC-031_close_report.md` as framing-only caveat, not completed close-pack proof  
* `audit/EPIC-031_MANIFEST.json` as framing-only caveat, not completed close-pack proof

Final Lead Dev closure trace observed:

* The PR-01, PR-02, and PR-03 implementation evidence chain supports the three active Fermentation subtasks for this epic.  
* Step-0A, Step-0B, and PO-001 through PO-018 are recorded as PASS, including accepted Moon Loop remediation where needed.  
* The remaining caveats are formal close-pack completion, PF09.5 drainage, parent-task posture, and deferred later Fermentation work. Those caveats are not failed Live QA behavior.  
* PF23 context does not reveal an unresolved current-reality contradiction that overrides PF10’s QA outcome record.  
* Documentation drainage and PF09.5 status movement remain follow-up posture, not blockers to this review’s closure trace.

Final Lead Dev RCA and mechanics lessons observed:

* Provider status classification required tighter separation among rate-limit, retryable network, retryable server, and non-retryable provider status classes.  
* Redirect behavior matters because injected request tests may not cover default request behavior.  
* Secret-safe observability requires bounded labels plus proof of payload-body absence, plaintext-secret absence, and raw-secret-header absence.  
* Evidence generators need fail-closed behavior so missing or stale proof companions cannot silently produce accepted proof.  
* Side-effect evidence families must fail closed when target proof companions are missing or stale.  
* Human Evidence Index and Machine Mirror coherence are central to trusting SAFE rails evidence.  
* Current-state check roots reduce ambiguity when run-id or sidecar paths drift.  
* Moon Loop remediation is acceptable only when bounded, evidence-linked, and explicitly recorded with failure signature, remediation note, rerun proof, and changed-artifact proof.  
* Live QA must stay proof-only and must not drift into implementation, remediation, PF edits, or closeout action.  
* PF09 subtask supportability and permanent PF09 drainage remain distinct truth classes.  
* Public Reader and HDAPI v2 runtime boundaries must stay out of the SAFE first-slice proof unless explicitly scoped.  
* Vendor live behavior and local provider-control proof are separate proof classes.  
* Evidence roots can be multi-root when bound by governed index, mirror, and path-proof discipline.  
* PF23 reality context is useful for confirming surfaces and seams but does not replace PF10 QA evidence.

Final Lead Dev no-claim and future-scope boundaries observed:

* Preserve PF10’s no-claim posture for HDAPI v2 runtime conformance until a later Fermentation slice proves it.  
* Preserve PF10’s no-claim posture for live vendor behavior until a later scoped proof exists.  
* Do not mark PF09.5 permanent drainage complete until the actual PF09.5 row update is assigned and proven.  
* Parent `HDE-FERM001` status posture remains a later close or drain judgment.  
* Deferred later Fermentation work remains future scope only: HDAPI v2 runtime conformance, live vendor behavior, DB bridge and DB runtime acceptance, narrative/router parity, and registry closure.  
* Future cards may harden evidence side-effect classification patterns and generated-proof fail-closed conventions, but this retrospective does not create PF14 tasks, PF09 statuses, acceptance tokens, closeout gates, or future implementation scope by itself.  
* The retrospective records no current PF-Canon doc delta required from the PF23 audit pass or final QA RCA.

HDE-EPIC032 PR-01 narrative-router parity and evidence-indexing proof family observed (records-only). PF14 records these paths as the observed PR-01 proof family for the narrative-router slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, acceptance-token source, PR-02 registry claim, PR-03 or PR-04 DB claim, HDAPI v2 claim, OPS claim, or public Reader contract change.

Observed PR-01 paths include:

* `tests/unit/test_narratives_router.py`  
* `tools/evidence/generate_epic032_pr01_router_evidence.py`  
* `tools/evidence/update_evidence_index.py`  
* `audit/gates/narratives/keys_10x4.table.json`  
* `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`  
* `artifacts/narratives/router/parity_abba.log`  
* `artifacts/narratives/router/parity_abba.log.path_proof.txt`  
* `artifacts/narratives/router/cli_http_parity.log`  
* `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`

Observed PR-01 proof posture. The PR-01 family records fixed Magic-10 roster coverage, a 40-row key-table expectation, missing-key fail-closed behavior, two-run identity, AB↔BA coherence where applicable, CLI/HTTP parity where defined, canonical JSON proof, and Human Evidence Index, Machine Mirror, hash-sentinel, and path-proof binding.

Observed PR-01 remediation posture. The original PR produced the required router artifacts and evidence rows but included an unsupported registry-closure token claim in the key-table evidence row. The remedial PR removed the unsupported token claim from the evidence source row, regenerated the Human Evidence Index and Machine Mirror, refreshed hash sentinels and path proofs, preserved the approved router parity token posture for AB↔BA/two-run and CLI/HTTP parity rows, and reran the relevant tests and evidence checks.

Observed PR-01 validation posture. The final PR-01 record includes py-compile checks for the router test, router evidence generator, and evidence updater; targeted router, Aux preview, and Aux transport pytest; router evidence generation; Evidence Index update and check; mirror schema check; Evidence Index hash check; evidence path validation; LF check; and `git diff --check`.

Observed PR-01 side-effect refresh posture. Non-PR-01 path-proof and orientation refreshes are recorded as governed evidence-tool churn or derived evidence-count refresh, not as PR-01 behavior changes. The PR-01 proof family remains bounded to narrative-router parity and evidence indexing.

Observed PR-01 boundary posture. The combined PR-01 outcome does not implement PR-02 registry work, PR-03 or PR-04 DB work, HDAPI v2 work, OPS work, or public Reader contract changes. Public Reader contract files were checked as unchanged, and the record states no public Reader route, public flag, or public payload field was intentionally changed.

HDE-EPIC032 PR-02 narrative registry diff, pack identity, Doc-Delta, and evidence-indexing proof family observed (records-only). PF14 records these paths as the observed PR-02 proof family for the narrative registry slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, acceptance-token source, PR-03 or PR-04 DB claim, HDAPI v2 claim, OPS claim, or public Reader contract change.

Observed PR-02 paths include:

* `tests/unit/test_narratives_loader.py`  
* `tests/evidence/test_sanity_pipeline.py`  
* `tools/evidence/generate_narrative_registry_diff.py`  
* `tools/evidence/run_sanity_pipeline.py`  
* `tools/evidence/update_evidence_index.py`  
* `audit/gates/narratives/registry.diff.json`  
* `audit/gates/narratives/registry.diff.json.path_proof.txt`  
* `audit/gates/narratives/pack_identity.txt`  
* `audit/gates/narratives/pack_identity.txt.path_proof.txt`  
* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Observed PR-02 proof posture. The PR-02 family records deterministic narrative registry diff generation, Doc-Delta binding, pack identity from canonical manifest bytes, same-bytes two-run identity, keys-only/no-prose registry evidence, Human Evidence Index and Machine Mirror binding, hash sentinels, path proofs, sanity-pipeline generator ordering, and orientation evidence remediation.

Observed PR-02 remediation posture. The final PR-02 state records remediation for five proof defects: extra manifest rows could be copied into registry diff evidence without validation, unsupported categories and bands could be accepted, missing supported groups or partial slot sets could pass, the generator was not originally run in the governed sanity pipeline, and orientation evidence was stale after PR-02 added indexed artifacts. The accepted final state adds closed-set manifest validation, category, band, perspective, slot, duplicate-tuple, duplicate-key, and expected tuple-grid validation; wires generator write and check before evidence updater write and check; and regenerates orientation evidence and dependent governed index, mirror, hash, and path-proof state.

Observed PR-02 side-effect refresh posture. Existing Machine Mirror rows, Machine Mirror self/index rows, hash sentinels, PR-01 router path proofs, writer path proofs, EPIC030 historical path proofs, Human Evidence Index rows, and orientation proof companions refreshed during PR-02 are recorded as governed evidence-tool churn, derived evidence-count refresh, or historical evidence churn, not as PR-02 behavior expansion. The PR-02 proof family remains bounded to narrative registry diffing, Doc-Delta binding, pack identity, and evidence indexing.

Observed PR-02 validation posture. The final PR-02 record includes py-compile checks for the narrative loader tests, sanity-pipeline tests, registry diff generator, sanity pipeline, and evidence updater; targeted narrative loader and sanity-pipeline pytest; registry diff generation; Evidence Index update and check; orientation write and check; mirror schema check; Evidence Index hash check; evidence path validation; LF check; `git diff --check`; and public Reader contract file checks. The record states final validation commands passed.

Observed PR-02 boundary posture. The final PR-02 outcome uses approved token posture without creating PF14 token authority, records no new acceptance-token source, and records no public Reader contract files, public routes, public flags, or public payload fields changed.

HDE-EPIC032 PR-03 DB bridge fallback, bridge capability, provider parity, and evidence-indexing proof family observed (records-only). PF14 records these paths as the observed PR-03 proof family for the DB bridge/provider parity slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, acceptance-token source, PR-04 DB claim, OPS claim, HDAPI v2 claim, or public Reader contract change.

Observed PR-03 paths include:

* `engine/db/adapter.py`  
* `ci/checks/check_bridge_consistency.py`  
* `tests/db/test_adapter_selection.py`  
* `tests/db/test_adapter_contract.py`  
* `tests/unit/test_check_bridge_consistency.py`  
* `tests/ops/test_evidence_index.py`  
* `tools/evidence/generate_db_bridge_parity.py`  
* `tools/evidence/update_evidence_index.py`  
* `artifacts/db_bridge/adapter_selection.snapshot.json`  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt`  
* `artifacts/db_bridge/provider_parity.proof.json`  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt`  
* `artifacts/runtime/env_connectivity.snapshot.json`  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Observed PR-03 proof posture. The PR-03 family records DB bridge fallback, bridge capability proof, deterministic provider-parity harnessing, false-PASS parity guards, evidence-index binding, and CI remediation for canonical adapter-selection artifact-key posture. It preserves `DBAccess` as the provider-agnostic façade and proves dev fallback through that façade, direct/bridge comparison on a deterministic corpus, secret-free evidence, and live provider parity truthfully unavailable under closed rails rather than faked as passing.

Observed PR-03 runtime guard posture. The final PR-03 state treats `APP_ENV=live` as production-like by aligning `live` with `prod` and `production` for bridge fallback guarding. The record states this is a hardening change, not permissive drift, because bridge fallback is blocked for production-like runtime tags unless the production bridge override is explicitly enabled or bridge is explicitly forced by governed mechanics.

Observed PR-03 remediation posture. The final PR-03 state records two remediated failures: incomplete production-like alias handling for `live`, and a canonical adapter-selection evidence-key collision. The accepted remediation adds production alias handling, live/prod guard regression coverage, canonical adapter-selection registration under `db_bridge.adapter_selection.snapshot`, and stale EPIC-specific adapter-selection key filtering before dedupe and regeneration.

Observed PR-03 side-effect refresh posture. Existing Machine Mirror rows, Machine Mirror path proofs, Machine Mirror hash sentinels, PR-01 router path proofs, writer path proofs, PR-02 Doc-Delta and narrative path proofs, EPIC030 historical path proofs, Human Evidence Index rows, Human Evidence Index hash sentinels, and orientation proof companions refreshed during PR-03 are recorded as governed evidence-tool churn, shared evidence-tool churn, derived evidence-skeleton refresh, or historical evidence churn, not as PR-03 behavior expansion. The PR-03 proof family remains bounded to DB adapter selection, bridge consistency validation, deterministic evidence generation, and evidence-index wiring.

Observed PR-03 validation posture. The final PR-03 record includes DB adapter tests, bridge consistency tests, bridge provider capability coverage, evidence generator checks, Evidence Index updater write and check, orientation write and check, mirror schema check, Evidence Index hash check, evidence path validation, LF checks, `git diff --check`, and public contract boundary checks. The record states the DB adapter tests, evidence tests, evidence-index tests, and CI failure target passed after remediation.

Observed PR-03 boundary posture. The final PR-03 outcome records no PF-Canon edit, no public Reader contract change, no public route change, no public flag change, and no public payload field change. The record also states PR-03 alone does not move `HDE-FERM004.2` to Done because the row remains part of a wider epic slice and live provider parity remains unavailable under closed rails. This records a no-claim boundary only; it does not make PF14 a PF09 status authority.

HDE-EPIC032 OPS-01 provider parity closure evidence bundle observed (records-only). PF14 records these paths as the observed OPS-01 provider-parity closure evidence family for the DB bridge/provider parity slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, QA PASS claim, epic closure claim, acceptance-token source, PR-04 implementation claim, HDAPI v2 claim, or public Reader contract change.

Observed OPS-01 paths include:

* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity.proof.json`  
* `audit/ops/hde-epic032/db-provider-parity/bridge_consistency_result.txt`  
* `audit/ops/hde-epic032/db-provider-parity/parity_scope_rationale.txt`  
* `audit/ops/hde-epic032/db-provider-parity/non_claims.txt`  
* `audit/ops/hde-epic032/db-provider-parity/ops01_final_report.txt`  
* `audit/ops/hde-epic032/db-provider-parity/created_files_sha256.txt`  
* `audit/ops/hde-epic032/db-provider-parity/commands.txt`  
* `audit/ops/hde-epic032/db-provider-parity/stdout.log`  
* `audit/ops/hde-epic032/db-provider-parity/stderr.log`  
* `audit/ops/hde-epic032/db-provider-parity/exit_codes.txt`  
* `audit/ops/hde-epic032/db-provider-parity/redacted_env_presence.txt`  
* `audit/ops/hde-epic032/db-provider-parity/adapter_selection.snapshot.json`  
* `audit/ops/hde-epic032/db-provider-parity/env_connectivity.snapshot.json`

Observed OPS-01 proof posture. The OPS-01 family records `OPS-01 closure status: CLOSE CANDIDATE`, `provider_parity_closure_status: closed`, active corpus rows `grants`, `search_path`, `select_one`, and `ddl_fingerprint`, all active rows non-skipped, all active rows matching, and bridge consistency result `PASS`.

Observed OPS-01 remediation posture. The prior `ddl_fingerprint` loop is recorded as resolved through Path A: `ddl_fingerprint` remains included in the active corpus and now has `parity=match`, not `diff`. The closure path is recorded as active-row match evidence, not corpus exclusion.

Observed OPS-01 execution posture. The OPS-01 packet records working directory, command transcript, stdout status, stderr status, exit code, target environment `dev`, presence-only `DATABASE_URL`, presence-only `DB_BRIDGE_URL`, provider availability for direct `psycopg` and bridge providers, closure decision artifact, final report, and checksum ledger.

Observed OPS-01 safety and boundary posture. The OPS-01 packet records empty stdout and stderr, presence-only env posture, no plaintext secret values, no notable irreversible infrastructure change, no unsafe operation, no QA PASS claim, no PF09 status movement claim, no epic closure claim, and no acceptance-token satisfaction claim for DB proof labels.

HDE-EPIC032 PR-04 non-dev typed DB failure behavior and DB evidence-coherence proof family observed (records-only). PF14 records these paths as the observed PR-04 proof family for the non-dev typed DB failure and DB evidence-coherence slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, acceptance-token source, QA PASS claim, epic closure claim, OPS claim beyond bound OPS evidence, HDAPI v2 claim, or public Reader contract change.

Observed PR-04 paths include:

* `tools/evidence/generate_db_bridge_parity.py`  
* `tools/evidence/update_evidence_index.py`  
* `tests/evidence/test_generate_db_bridge_parity_nondev.py`  
* `tests/db/test_adapter_selection.py`  
* `artifacts/runtime/env_connectivity.nondev_failure.json`  
* `artifacts/runtime/env_connectivity.nondev_failure.json.path_proof.txt`  
* `artifacts/runtime/env_connectivity.snapshot.json`  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt`  
* `artifacts/db_bridge/adapter_selection.snapshot.json`  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt`  
* `artifacts/db_bridge/caps.snapshot.json.path_proof.txt`  
* `artifacts/db_bridge/provider_parity.proof.json`  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt`  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Observed PR-04 DB posture path-proof refresh paths include:

* `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`  
* `artifacts/db/check_schema.txt.path_proof.txt`  
* `artifacts/db/ddl_fingerprint.json.path_proof.txt`  
* `artifacts/db/grants.txt.path_proof.txt`  
* `artifacts/db/partition_plan.txt.path_proof.txt`  
* `artifacts/db/partition_verify.log.path_proof.txt`  
* `artifacts/db/provider_parity/bridge.json.path_proof.txt`  
* `artifacts/db/provider_parity/direct.json.path_proof.txt`  
* `artifacts/db/provider_parity/summary.json.path_proof.txt`

Observed PR-04 proof posture. The PR-04 family records corrected `APP_ENV=stage` non-dev failure evidence, no proactive probes, numeric-free public failure posture, secret-free or presence-only posture, real observed DBAccess attempt ordering, typed `BridgeUnavailable` / `missing_bridge_url`, fail-closed generator behavior, evidence regression tests, and governed evidence regeneration.

Observed PR-04 remediation posture. The PR-04 family records remediation of three prior defects: non-dev evidence used production posture, unexpected outcomes were serialized as synthetic evidence, and selection-order evidence was hardcoded instead of derived from real `DBAccess` attempts. The accepted state records stage posture, real adapter-attempt sequence, expected typed failure, hard fail behavior through `SystemExit`, and focused regression coverage.

Observed PR-04 evidence binding posture. The PR-04 family records `artifacts/runtime/env_connectivity.nondev_failure.json` bound through the Human Evidence Index, Machine Mirror, hash sentinels, path proofs, and path validation. It also records OPS-01 provider parity closure decision as OPS evidence only, without QA PASS, PF09 status movement, epic closure, or DB proof-label acceptance-token overclaim.

Observed PR-04 side-effect refresh posture. DB posture path-proof refreshes, DB bridge artifact refreshes, Human Evidence Index refreshes, Machine Mirror refreshes, hash-sentinel refreshes, topology orientation refreshes, narrative path-proof refreshes, writer path-proof refreshes, and historical EPIC030 path-proof refreshes are recorded as governed evidence-tool churn or carried-forward evidence refresh, not as PR-04 product-scope expansion.

Observed PR-04 validation posture. The final PR-04 record includes py-compile, focused pytest, generator run, Evidence Index generation and check, mirror schema check, evidence-index hash check, evidence-path validation, final-LF checks, and pass indicators for the targeted evidence and test set.

Observed PR-04 boundary posture. The PR-04 outcome is bounded to DB non-dev total-failure proof, tests, the DB bridge parity generator, evidence-index wiring, OPS-01 evidence binding as OPS evidence only, and DB evidence coherence. It records no public Reader contract change, no public route change, no public flag change, and no public payload field change. PF14 records the mechanics support and no-claim boundaries only; it does not make a PF09 status decision.

HDE-EPIC032 Remedial PR-01 DB selection-order contract stabilization observed (records-only). PF14 records these paths as the observed remedial PR proof family for the PO-010 selection-order failure. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, OPS claim, Live QA rerun claim, QA plan edit claim, PF edit claim, DOC\_UPDATE claim, public Reader expansion, vendor/live-provider expansion, acceptance-token source, or new token claim.

Observed Remedial PR-01 paths include:

* `engine/db/adapter.py`  
* `tests/db/test_adapter_selection.py`  
* `tests/evidence/test_generate_db_bridge_parity_nondev.py`  
* `tools/evidence/generate_db_bridge_parity.py`  
* `artifacts/db_bridge/adapter_selection.snapshot.json`

Observed Remedial PR-01 proof posture. The remedial PR records native `selection_order` emission in `DBAccess.for_current_env`, derived from observed adapter attempts/provider order, and structural validation in the DB bridge parity generator. It records `selection_order` as structural adapter-selection JSON, not raw string-presence proof or detached generator-only data.

Observed Remedial PR-01 remediation posture. The remedial PR records the PO-010 failure signature as `selection_order_missing` and the root cause as a contract mismatch: QA expected visible `selection_order`, while adapter evidence exposed attempts/order indirectly and the generator became responsible for deriving or backfilling `selection_order`. The accepted remediation makes adapter-selection evidence emit `selection_order`, tests that it equals `attempts[*].provider`, and fails generator validation on non-array or mismatched `selection_order`.

Observed Remedial PR-01 provider-parity truth posture. The remedial PR preserves provider parity truthfulness by testing unavailable direct rows as `parity_status: unavailable` with per-capability skips, and preserves DB proof-label non-token posture for DB provider and bridge proof labels.

Observed Remedial PR-01 validation posture. The final remedial PR record includes targeted pytest for `tests/db/test_adapter_selection.py` and `tests/evidence/test_generate_db_bridge_parity_nondev.py`, generator check, generator run, and `git diff --check` as passing.

Observed Remedial PR-01 boundary posture. The remedial PR stabilizes the DB bridge/provider parity evidence contract and contributes remediation evidence to `HDE-FERM004.2`, but it does not execute OPS work, Live QA, QA plan update, checklist drainage, a new provider parity acceptance close, or a PF09 status move. PF14 records the mechanics support and no-claim boundaries only; it does not make a PF09 status decision.

HDE-EPIC032 Implementation Retrospective observed (records-only). PF14 records the mechanics portions of the retrospective as a closure trace for the Fermentation Pass 3 implementation set. This block does not create a PF09 status action, PF09 drainage, acceptance-token source, QA PASS claim, epic closure claim, OPS authorization, HDAPI v2 claim, or public Reader contract change.

Final retrospective scope observed:

* HDE-EPIC032 was planned as a Fermentation implementation slice for narrative router parity and indexing, narrative registry diffing and identity indexing, DB bridge fallback and provider parity, non-dev typed DB failure behavior, and DB evidence, index, mirror, and path-proof coherence.  
* The public Reader contract remained unchanged. Narrative work stayed keys-only and registry or manifest-oriented. HDAPI v2 inventory, adapter architecture, live conformance, and PO-only open-rails v2 smoke remained deferred.  
* PF14’s adjacent HDE-EPIC032 PR and OPS records carry the exact observed path ledgers for PR-01, PR-02, PR-03, OPS-01, and PR-04.

Final retrospective mechanics and evidence ledger observed:

* PR-01 delivered narrative-router parity evidence: router matrix coverage, missing-key behavior, two-run identity, AB↔BA coherence, CLI/HTTP parity where defined, canonical JSON proof, and Human Evidence Index, Machine Mirror, hash-sentinel, and path-proof binding. It also remediated an unsupported registry-closure token overclaim without creating PF14 token authority.  
* PR-02 delivered narrative registry diffing and identity evidence: registry diff generation, pack identity from canonical manifest bytes, Doc-Delta binding, Human Evidence Index and Machine Mirror binding, sanity-pipeline ordering, orientation remediation, and governed path-proof posture.  
* PR-03 delivered DB bridge fallback and provider-parity harnessing: `DBAccess` façade preservation, dev and stage bridge fallback posture, bridge capability proof, deterministic provider-parity harnessing, false-PASS guard behavior, and `APP_ENV=live` hardening as production-like.  
* OPS-01 delivered provider-parity closure evidence as OPS evidence only, with active parity corpus rows `grants`, `search_path`, `select_one`, and `ddl_fingerprint` all matching, while preserving non-claim posture for QA, PF09 status movement, epic closure, and acceptance-token satisfaction.  
* PR-04 delivered non-dev typed DB failure proof and DB evidence coherence: `APP_ENV=stage` failure evidence, real `DBAccess` attempt ordering, fail-closed generator behavior, typed `BridgeUnavailable` / `missing_bridge_url`, Evidence Index, Machine Mirror, path-proof coherence, and OPS-01 evidence binding as non-claiming OPS evidence.

Final retrospective evidence groups observed:

* Narrative-router evidence centers on `audit/gates/narratives/keys_10x4.table.json`, `artifacts/narratives/router/parity_abba.log`, `artifacts/narratives/router/cli_http_parity.log`, and the PR-01 router evidence generator.  
* Narrative-registry evidence centers on `tools/evidence/generate_narrative_registry_diff.py`, `audit/gates/narratives/registry.diff.json`, `audit/gates/narratives/pack_identity.txt`, `audit/docdeltas/hde-epic032_doc_deltas.md`, sanity-pipeline ordering, and governed index and mirror refresh.  
* DB bridge and provider-parity evidence centers on `engine/db/adapter.py`, `tools/evidence/generate_db_bridge_parity.py`, `artifacts/db_bridge/adapter_selection.snapshot.json`, `artifacts/db_bridge/provider_parity.proof.json`, `artifacts/runtime/env_connectivity.snapshot.json`, and `artifacts/runtime/env_connectivity.nondev_failure.json`.  
* OPS provider-parity evidence centers on `audit/ops/hde-epic032/db-provider-parity/` and the provider-parity closure decision, provider-parity proof, bridge consistency result, parity scope rationale, non-claims, command, log, env-posture, final-report, and checksum-ledger artifacts recorded there.  
* Shared evidence trust centers on `tools/evidence/update_evidence_index.py` as the single writer, `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, and matching path-proof discipline.

Final retrospective mechanics lessons observed:

* Proof-label discipline must remain explicit before acceptance artifacts are written. PF14 records proof mechanics and no-claim boundaries only; governance and token semantics remain routed by title.  
* Narrative router and registry behavior moved from implicit behavior toward governed, path-proven evidence for coverage, identity, parity, and keys-only/no-prose posture.  
* DB runtime proof gained stronger fail-closed behavior and non-dev failure evidence rather than synthetic or hardcoded evidence.  
* A single machine-readable closure file can resolve an evidence loop more cleanly than interpretive prose when row-level evidence must prove closure.  
* Evidence generators must fail closed when expected behavior changes. They must not serialize synthetic accepted states for unexpected success, unexpected failure class, wrong typed error, wrong snapshot, or wrong attempt order.  
* Evidence path identity and artifact-key identity should be canonical when a repo-level canonical key exists. EPIC-specific keys must not displace a repo canonical artifact key for the same governed path.  
* OPS evidence must stay distinct from QA evidence, PF09 status moves, epic closure, and acceptance-token satisfaction.  
* Public Reader contract boundaries must remain explicit when adjacent narrative, DB, OPS, or internal/admin surfaces change.  
* Non-dev total failure must be proven in a non-production posture, with numeric-free public failure posture, secret-free or presence-only evidence posture, and real adapter attempt ordering.  
* The evidence system’s single-writer pattern is central to DB and narrative proof trust.

Final retrospective boundary posture observed:

* PR-03 and OPS-01 do not independently move `HDE-FERM004.2` to Done. Any combined-evidence status movement remains outside PF14 mechanics authority.  
* Permanent PF09.5 table status, PF09 drainage, parent-task posture, and Lead closeout questions remain outside PF14. PF14 may record mechanics support and no-claim boundaries, but it does not make checklist-status decisions.  
* DB proof-label posture may be collected, indexed, and reviewed as governed proof mechanics, but PF14 must not treat proof labels as acceptance tokens unless the owning governance home admits them.  
* Broad path-proof churn is recorded as governed evidence-tool churn when it is generated by canonical tooling and does not expand product behavior.  
* `APP_ENV=live` remains recorded as production-like bridge-guard hardening for the DB bridge mechanics family, not as a permissive runtime drift.  
* The retrospective did not create a new PF10 addendum, new PF14 task, new evidence home, new public route, new public flag, new public payload field, or new HDAPI v2 runtime-conformance claim.

HDE-EPIC032 early Live QA evidence paths observed (records-only):

* checks/step-0a-discovery:  
  * `audit/qa/hde-epic032/00_meta/live_qa_harness.py`  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
  * `audit/qa/hde-epic032/checks/step-0a-discovery/remediation_provenance.md`  
  * `audit/qa/hde-epic032/00_meta/delta/changed_files.txt`  
  * `audit/qa/hde-epic032/00_meta/delta/changed_files.sha256`  
  * `audit/qa/hde-epic032/00_meta/delta/remediation_note.txt`  
  * `audit/qa/hde-epic032/00_meta/delta/failure_signature.txt`  
* checks/step-0b-doc-delta:  
  * `audit/docdeltas/hde-epic032_doc_deltas.md`  
  * `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`  
* checks/po-001:  
  * `audit/qa/hde-epic032/checks/po-001/primary.log`  
  * `audit/qa/hde-epic032/checks/po-001/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-001/result.json`  
* checks/po-002:  
  * `audit/qa/hde-epic032/checks/po-002/primary.log`  
  * `audit/qa/hde-epic032/checks/po-002/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-002/result.json`  
* checks/po-003:  
  * `audit/qa/hde-epic032/checks/po-003/primary.log`  
  * `audit/qa/hde-epic032/checks/po-003/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-003/result.json`  
* checks/po-004:  
  * `audit/qa/hde-epic032/checks/po-004/primary.log`  
  * `audit/qa/hde-epic032/checks/po-004/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-004/result.json`  
  * `artifacts/narratives/router/parity_abba.log`  
* checks/po-005:  
  * `audit/qa/hde-epic032/checks/po-005/primary.log`  
  * `audit/qa/hde-epic032/checks/po-005/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-005/result.json`  
  * `audit/gates/narratives/registry.diff.json`  
  * `audit/gates/narratives/pack_identity.txt`  
* checks/po-006:  
  * `audit/qa/hde-epic032/checks/po-006/primary.log`  
  * `audit/qa/hde-epic032/checks/po-006/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-006/result.json`  
  * `audit/gates/narratives/keys_10x4.table.json`  
* shared QA evidence:  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

HDE-EPIC032 early Live QA current-state notes observed (records-only).

* Step-0A and Step-0B record PASS under closed rails and deterministic pins, with governed headers capturing SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, LC\_ALL, LANG, and TZ. The evidence is recorded under the stable epic QA root and check directories.  
* Step-0A records an accepted bounded Moon Loop contingency for a QA-created harness file after a placeholder-only helper body failed before first governed receipt emission. The accepted record preserves check IDs, rails, proof targets, evidence paths, and tokenless posture; records failure signature, remediation note, changed-files/hash capture, and same-stream rerun PASS evidence; and limits the change to `audit/qa/hde-epic032/00_meta/live_qa_harness.py`.  
* Step-0B records PASS for the doc-delta capture surface, including the canonical doc-delta draft, QA metadata doc-delta surface, primary log, path proof, and result sidecar.  
* checks/po-001 records PASS for the Fermentation Pass 3 scope-boundary proof, including visible Reader and dev Reader catalog surfaces, OPS evidence not treated as QA PASS by itself, and DB proof labels not treated as acceptance tokens.  
* checks/po-002 records PASS for narrative-router deterministic key selection, including router tests returning exit code 0, key-table evidence existence, and AB↔BA parity evidence existence.  
* checks/po-003 records PASS for keys-only router proof and public Reader non-expansion, including keys-only key-table evidence, Reader route posture visible without expansion into a new proof route, and APP\_ENV gating visible for internal/dev surfaces.  
* checks/po-004 records PASS for narrative-router identity criteria, including targeted router pytest success, repeated-run identity evidence, and AB↔BA identity evidence.  
* checks/po-005 records PASS for narrative registry diff and pack identity criteria, including registry generator check success, registry diff evidence bound to HDE-EPIC032, and pack identity posture recorded from canonical manifest bytes.  
* checks/po-006 records PASS for narrative registry non-overclaim criteria, including unsupported registry token-claim absence, no required-missing entries, keys-only key-table posture, and no acceptance-token claim fields in the key-table payload.  
* PO-001 through PO-006 primary headers record `intended_tokens: []` and `claimed_tokens: []`, preserving tokenless Live QA posture and avoiding acceptance-token, final QA outcome, PF09.5 drainage, or epic-closeout claims by the checks themselves.  
* The PO-001 through PO-006 manifest and header provenance gaps are recorded as remediated. The shared QA step-log manifest and manifest path proof bind executed check IDs to status PASS, primary-log paths, and primary-log path proofs.

HDE-EPIC032 continued Live QA evidence paths observed (records-only):

* checks/po-007:  
  * `audit/qa/hde-epic032/checks/po-007/primary.log`  
  * `audit/qa/hde-epic032/checks/po-007/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-007/result.json`  
  * `audit/gates/narratives/registry.diff.json`  
  * `audit/gates/narratives/pack_identity.txt`  
  * `audit/docdeltas/hde-epic032_doc_deltas.md`  
* checks/po-008:  
  * `audit/qa/hde-epic032/checks/po-008/primary.log`  
  * `audit/qa/hde-epic032/checks/po-008/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-008/result.json`  
  * `tools/evidence/generate_db_bridge_parity.py`  
  * `artifacts/db_bridge/provider_parity.proof.json`  
  * `artifacts/db_bridge/adapter_selection.snapshot.json`  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* checks/po-009:  
  * `audit/qa/hde-epic032/checks/po-009/primary.log`  
  * `audit/qa/hde-epic032/checks/po-009/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-009/result.json`  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt`  
* checks/po-010:  
  * `audit/qa/hde-epic032/checks/po-010/primary.log`  
  * `audit/qa/hde-epic032/checks/po-010/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-010/result.json`  
  * `artifacts/db_bridge/adapter_selection.snapshot.json`  
  * `artifacts/db_bridge/provider_parity.proof.json`  
* checks/po-011:  
  * `audit/qa/hde-epic032/checks/po-011/primary.log`  
  * `audit/qa/hde-epic032/checks/po-011/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-011/result.json`  
* checks/po-012:  
  * `audit/qa/hde-epic032/checks/po-012/primary.log`  
  * `audit/qa/hde-epic032/checks/po-012/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-012/result.json`  
  * `tools/evidence/generate_db_bridge_parity.py`  
* checks/po-013:  
  * `audit/qa/hde-epic032/checks/po-013/primary.log`  
  * `audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-013/result.json`  
  * `docs/evidence/INDEX.json`  
  * `artifacts/evidence_index.jsonl`  
* checks/po-014:  
  * `audit/qa/hde-epic032/checks/po-014/primary.log`  
  * `audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-014/result.json`  
  * `docs/evidence/INDEX.json`  
  * `artifacts/evidence_index.jsonl`  
* checks/po-015:  
  * `audit/qa/hde-epic032/checks/po-015/primary.log`  
  * `audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-015/result.json`  
  * `tools/evidence/generate_narrative_registry_diff.py`  
  * `tools/evidence/generate_db_bridge_parity.py`  
* shared QA evidence:  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

HDE-EPIC032 continued Live QA current-state notes observed (records-only).

* PO-007, PO-008, and PO-009 record PASS under closed rails with check-scoped current-state evidence, per-check primary logs, per-check path proofs, result sidecars, manifest entries, manifest path proof, and tokenless primary-header posture.  
* checks/po-007 records PASS for registry/doc-delta identity criteria, including registry diff binding, pack/evidence support, and no ungoverned doc-delta claim from the reviewed evidence.  
* checks/po-008 records PASS for the combined DB bridge/provider parity proof-chain criteria, including DB bridge parity generator check return code `0`, provider parity proof presence, adapter-selection evidence presence, and OPS closure status visibility without isolated implementation-only or OPS-only overclaim.  
* checks/po-009 records PASS for OPS evidence non-claim criteria, including visible OPS closure status, OPS support evidence not claiming QA PASS by itself, and OPS support evidence not claiming standalone checklist completion or epic closure.  
* The PO-007 through PO-009 report records a non-fatal `DeprecationWarning` from the harness timestamp helper, with no tooling-blocked, fail-tooling, or fail-behavior condition recorded.  
* PO-010, PO-011, and PO-012 record PASS with current result artifacts, no required-missing entries, no behavior failures, per-check primary-log path proofs, manifest entries, tokenless primary-header posture, and current-state evidence under the epic QA root.  
* checks/po-010 records structural `selection_order` proof in `artifacts/db_bridge/adapter_selection.snapshot.json`, with `selection_order` matching observed attempt providers. The evidence is recorded as structural adapter-selection evidence derived from observed adapter attempts/provider order, not raw string-presence proof and not a new acceptance-token claim.  
* The PO-010 generator/adapter remediation is recorded as PR-routed remediation, not bounded Moon Loop-only correction. The record ties the non-QA-root remediation to PR-labeled commit lineage plus stabilization on `main`, and records that the final report no longer treats the generator change as bounded Moon Loop-only correction.  
* DB provider/bridge proof labels in the PO-010 through PO-012 evidence remain non-token proof labels, with `DB_PROVIDER_PARITY_OK` recorded as `not_claimed` and `DB_BRIDGE_CAPS_OK` recorded as `proven_by_bridge_capability`, both with type `non_token`.  
* PO-012 records a brief TOOLING\_BLOCKED state during refresh because `artifacts/db_bridge/adapter_selection.snapshot.json` was missing, then returns to PASS after governed DB bridge evidence regeneration through `tools/evidence/generate_db_bridge_parity.py`.  
* PO-013, PO-014, and PO-015 record PASS under closed deterministic rails, with no tooling-blocked, fail-tooling, or fail-behavior state encountered.  
* checks/po-013 records PASS for evidence-index coherence posture, including Human Evidence Index presence, Machine Mirror presence, and command checks returning `0`.  
* checks/po-014 records PASS for Machine Mirror alignment posture, including human-machine loci presence and command checks returning `0`.  
* checks/po-015 records PASS for generated-proof check posture, including all command checks green and command checks returning `0`.  
* The PO-013 through PO-015 v2 report records remediation of prior manifest/header proof gaps by explicitly proving per-epic manifest, manifest path proof, manifest entries, captured\_env, evidence\_artifacts, intended\_tokens, and claimed\_tokens.  
* PO-007 through PO-015 primary headers record `intended_tokens: []` and `claimed_tokens: []`, preserving tokenless Live QA posture and avoiding acceptance-token, final QA outcome, PF09.5 drainage, or epic-closeout claims by the checks themselves.

HDE-EPIC032 final Live QA evidence paths observed (records-only):

* checks/po-016:  
  * `audit/qa/hde-epic032/checks/po-016/primary.log`  
  * `audit/qa/hde-epic032/checks/po-016/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-016/result.json`  
  * `artifacts/db_bridge/provider_parity.proof.json`  
  * `docs/evidence/INDEX.json`  
  * `artifacts/evidence_index.jsonl`  
* checks/po-017:  
  * `audit/qa/hde-epic032/checks/po-017/primary.log`  
  * `audit/qa/hde-epic032/checks/po-017/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-017/result.json`  
* checks/po-018:  
  * `audit/qa/hde-epic032/checks/po-018/primary.log`  
  * `audit/qa/hde-epic032/checks/po-018/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-018/result.json`  
  * `audit/gates/narratives/keys_10x4.table.json`  
  * `audit/gates/narratives/registry.diff.json`  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* checks/po-019:  
  * `audit/qa/hde-epic032/checks/po-019/primary.log`  
  * `audit/qa/hde-epic032/checks/po-019/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-019/result.json`  
  * `README.md`  
  * `CHANGELOG.md`  
  * `docs/INDEX.md`  
* checks/po-020:  
  * `audit/qa/hde-epic032/checks/po-020/primary.log`  
  * `audit/qa/hde-epic032/checks/po-020/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-020/result.json`  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* checks/po-021:  
  * `audit/qa/hde-epic032/checks/po-021/primary.log`  
  * `audit/qa/hde-epic032/checks/po-021/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-021/result.json`  
  * `artifacts/db_bridge/provider_parity.proof.json`  
* checks/po-022:  
  * `audit/qa/hde-epic032/checks/po-022/primary.log`  
  * `audit/qa/hde-epic032/checks/po-022/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-022/result.json`  
  * `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
  * `artifacts/db_bridge/provider_parity.proof.json`  
* checks/po-023:  
  * `audit/qa/hde-epic032/checks/po-023/primary.log`  
  * `audit/qa/hde-epic032/checks/po-023/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-023/result.json`  
  * `docs/ENDPOINTS_CATALOG.json`  
  * `adapter/http_reader.py`  
* checks/po-024:  
  * `audit/qa/hde-epic032/checks/po-024/primary.log`  
  * `audit/qa/hde-epic032/checks/po-024/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic032/checks/po-024/result.json`  
* shared QA evidence:  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

HDE-EPIC032 final Live QA current-state notes observed (records-only).

* PO-016, PO-017, and PO-018 record PASS with harness exit code `0`, stable check-scoped evidence, per-epic manifest entries, manifest path proof, per-check primary-header trust proof, path-proof sidecars, result sidecars, captured rails, evidence artifacts, intended tokens, claimed tokens, and tokenless posture.  
* checks/po-016 records PASS for DB proof-label non-token posture, including `db_labels_token_overclaim_detected: false`, no required-missing entries, and no behavior failures.  
* checks/po-017 records PASS for fallback-scope checking, including `fallback_scope_checked: true`, no required-missing entries, and no behavior failures.  
* checks/po-018 records PASS for active evidence-family presence while PF09 drainage is not claimed, including `active_evidence_families_present: true`, `pf09_drainage_not_claimed: true`, no required-missing entries, and no behavior failures.  
* PO-016 and PO-017 preserve DB proof-label and fallback-token scope boundaries. PO-018 preserves active-row supportability without claiming PF09.5 physical drainage.  
* PO-019, PO-020, and PO-021 record PASS with shell exit code `0`, current governed result artifacts, stable check-scoped evidence, manifest binding, manifest path proof, per-check primary-log headers, path-proof sidecars, tokenless posture, and final PASS disposition.  
* checks/po-019 records PASS for reused-foundation posture, including `reused_foundation_checked_from_repo_docs: true`, no required-missing entries, and no behavior failures.  
* checks/po-020 records PASS for truth-class separation, including `truth_classes_remain_separate: true`, no required-missing entries, and no behavior failures. The recorded truth classes keep OPS evidence, QA result, PF09.5 drainage, and final closeout from collapsing into a single claim.  
* checks/po-021 records PASS for vendor-version runtime non-claim posture, including `vendor_version_runtime_conformance_claimed: false`, no required-missing entries, and no behavior failures.  
* PO-019 preserves reused-foundation boundaries. PO-020 preserves truth-class separation. PO-021 preserves vendor-version runtime non-claim posture.  
* PO-022, PO-023, and PO-024 record PASS with shell exit code `0`, current governed result artifacts, manifest binding, manifest path proof, per-check primary-log headers, path-proof sidecars, tokenless posture, live-provider non-claim posture, public Reader non-expansion posture, and proof-only Live QA role posture.  
* checks/po-022 records PASS for live-provider non-claim posture, including `live_provider_behavior_claimed: false`, no required-missing entries, and no behavior failures. The record keeps local implementation proof, OPS evidence, and DB bridge evidence from being represented as live provider behavior.  
* checks/po-023 records PASS for public Reader non-expansion posture, including `reader_route_visible: true`, `invented_reader_proof_route_absent: true`, and no required-missing entries.  
* checks/po-024 records PASS for proof-only Live QA role posture, including `live_qa_role: prove_current_results_only`, no Live QA implementation action, no PF edit action, and no closeout action.  
* PO-022, PO-023, and PO-024 record no PF document edits, no acceptance-token claims, no vendor or live-provider rails opening, no public Reader route, flag, or payload edits, no Moon Loop use, and no code, OPS evidence, evidence index, token map, route, Reader adapter, public payload, public flag, or closeout artifact edits.  
* PO-022 through PO-024 record a Python 3.13 `datetime.utcnow` deprecation warning as non-blocking, with no TOOLING\_BLOCKED, FAIL\_TOOLING, or FAIL\_BEHAVIOR condition.  
* PO-016 through PO-024 primary headers record `intended_tokens: []` and `claimed_tokens: []`, preserving tokenless Live QA posture and avoiding acceptance-token, final QA outcome, PF09.5 drainage, or epic-closeout claims by the checks themselves.

HDE-EPIC032 final QA closeout review and QA RCA observed (records-only). PF14 records the mechanics-relevant closeout and RCA portions as a closure trace for HDE-EPIC032. This block does not create a PF09 status action, PF09 drainage, acceptance-token source, QA-plan authority, epic closeout action, OPS authorization, HDAPI v2 runtime-conformance claim, live vendor behavior claim, or public Reader contract change.

Final closeout source posture observed:

* PF10 is primary for HDE-EPIC032-specific QA events, implementation outcomes, remediation loops, ADRs, evidence posture, evidence pointers, and final closeout interpretation.  
* PF19 is the QA closeout, evidence trust, and RCA process basis where PF10 is silent.  
* The Implementation Guide is goals framing only.  
* The QA Plan is intended QA requirement framing only.  
* PF27 was not used for the final closeout/RCA.  
* PF06 was not used for the final closeout/RCA.  
* PF10 records the full Live QA ladder as PASS through Step-0A, Step-0B, and PO-001 through PO-024.  
* The final readiness line is Ready for epic closeout.  
* The root-cause category is evidence posture and scope-boundary drift, remediated through PR routing, governed evidence refresh, manifest/header proof, and non-claim discipline.

Final closeout coverage observed:

* Step-0A and Step-0B are fully evidenced as PASS.  
* PO-001, PO-002, and PO-003 are fully evidenced as PASS.  
* PO-004, PO-005, and PO-006 are fully evidenced as PASS.  
* PO-007, PO-008, and PO-009 are fully evidenced as PASS.  
* PO-010, PO-011, and PO-012 are fully evidenced as PASS after PR-routed selection-order remediation and post-remediation rerun evidence.  
* PO-013, PO-014, and PO-015 are fully evidenced as PASS after explicit manifest/header proof remediation.  
* PO-016, PO-017, and PO-018 are fully evidenced as PASS after explicit manifest, manifest path-proof, per-check primary-header, and tokenless-posture proof.  
* PO-019, PO-020, and PO-021 are fully evidenced as PASS, preserving reused-foundation boundaries, truth-class separation, and vendor-version runtime non-claim posture.  
* PO-022, PO-023, and PO-024 are fully evidenced as PASS, preserving live-provider non-claim, public Reader non-expansion, and proof-only Live QA posture.

Final RCA findings observed:

* PF10 records all requested Live QA step clusters from Step-0A and Step-0B through PO-024 as PASS, with governed evidence posture restored where initial reviews found gaps.  
* PR-01 initially overclaimed the unsupported `NARR_REGISTRY_CLOSURE_OK` token, then the remedial PR removed that token claim and regenerated Human Evidence Index, Machine Mirror, hash, and path-proof evidence.  
* PO-010 exposed a routing drift when `selection_order_missing` was remediated through a repo evidence generator outside the QA-created root; PF10 corrected the route by classifying non-QA-root generator change as remediation work, not bounded Moon Loop correction.  
* The PO-010 remediation PR added structural `selection_order` emission derived from observed adapter attempts/provider order and hardened generator validation.  
* Several Live QA review clusters initially required remediation for manifest/header provenance, then later PF10 entries recorded closure of those provenance gaps.  
* PF10 records that `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token proof labels unless Governance registers them or a later Build Notes addendum mints them.  
* Documentation drainage remains after PF10 addenda, but PF19 records undrained documentation deltas as non-blocking for closeout when QA evidence is complete and trustworthy.

Final RCA root cause observed:

* The primary root cause was evidence-boundary drift rather than one unremediated product defect.  
* Linked failure modes were an unsupported acceptance-token overclaim in PR-01 evidence, a Live QA routing drift around PO-010 where a non-QA-root generator fix was initially treated like QA-root Moon Loop correction, and repeated manifest/header provenance gaps before final PASS evidence became trustworthy.  
* Contributing factors included DB provider/bridge token-registry ambiguity, structural `selection_order` proof requiring semantic JSON evidence rather than raw string presence, and evidence trust requiring manifest/header proof rather than PASS labels alone.  
* The issue was hard to detect because several failures were boundary or provenance defects rather than pure behavior defects.  
* Closeout required step-scoped evidence pointers, manifest binding, path-proof sidecars, and primary-log header proof for every cluster.

Final RCA remediation-loop assessment observed:

* PR-01 remediation reduced uncertainty by removing the unsupported token claim and regenerating governed evidence surfaces.  
* PR-02 remediation reduced uncertainty by fixing orientation drift and passing evidence, mirror, hash, path, LF, and test checks.  
* PR-04 remediation reduced uncertainty for DB non-dev failure and evidence coherence while preserving non-claim posture.  
* PO-010 remediation reduced uncertainty only after PF10 routed the generator change through PR remediation instead of Moon Loop.  
* Manifest/header remediation loops created review churn early, but later reports reduced uncertainty by adding explicit manifest, header, path-proof, tokenless, and closed-rails proof.  
* The ADR pattern resolved unclear authority between QA-created Moon Loop correction and repo-level remediation.

Final RCA implementation-gap records observed:

* IMP-01 records unsupported token overclaim in a PR-01 evidence row. The expected behavior is that evidence rows must not claim unregistered acceptance tokens. The likely loci are `tools/evidence/update_evidence_index.py`, Machine Mirror, and Human Index. The proposed high-level fix is to keep acceptance-token validation and non-token proof-label review in the evidence-index generation path before evidence rows are accepted for closeout.  
* IMP-02 records the PO-010 `selection_order_missing` structural DB adapter-selection evidence gap. The expected behavior is that `selection_order` is structural adapter-selection evidence derived from observed adapter attempts/provider order, not string-presence or detached generator-only proof. The likely loci are `engine/db/adapter.py`, `tools/evidence/generate_db_bridge_parity.py`, `tests/db/test_adapter_selection.py`, and `tests/evidence/test_generate_db_bridge_parity_nondev.py`.  
* IMP-03 records early Live QA manifest/header proof remediation. The expected behavior is that each PASS check must be manifest-bound and primary-header-bound with captured\_env, evidence\_artifacts, intended\_tokens, and claimed\_tokens. The likely loci are the Live QA Deliverables Report evidence surface, `audit/qa/hde-epic032/qa_step_logs_manifest.json`, and per-check `primary.log`.

Final closeout verdict and recommendation observed:

* The final QA closeout verdict is READY FOR EPIC CLOSEOUT.  
* Strong PF10 evidence pointers exist for all Live QA step clusters from Step-0A and Step-0B through PO-024, with final PASS outcomes and trust posture restored where needed.  
* The strongest closeout proof clusters are PO-010 through PO-012 after PR-routed `selection_order` remediation, PO-013 through PO-018 after explicit manifest/header proof remediation, and PO-019 through PO-024 for non-claim boundaries and proof-only QA posture.  
* No key QA truth gap blocks closeout.  
* PF10 records previously blocking provenance, token, and remediation-routing concerns as resolved before final PASS.  
* Documentation deltas remain non-blocking when QA evidence is complete and trustworthy. The proposed deltas target PF19, PF04, PF09.5, and PF14 to prevent repeat ambiguity.  
* Future drainage follow-up is recorded as owner-home documentation work only. It does not create a PF14 task, PF09 status action, QA-blocking condition, acceptance-token claim, or closeout blocker.

HDE-EPIC032 Epic Closure Review and Lead Dev closure recommendation observed (records-only). PF14 records the mechanics-relevant closure review, path/surface ledger, ambiguity decisions, and Lead Dev recommendation as a closure trace for HDE-EPIC032. This block does not create a PO closeout action, PF09 status action, PF09 drainage, acceptance-token source, QA-plan authority, OPS authorization, HDAPI v2 runtime-conformance claim, live vendor behavior claim, public Reader contract change, or future implementation task.

Closure review source posture observed:

* Implementation Guide, QA Plan, and PF23 were provided to the closure review.  
* PF10 is recorded as primary for HDE-EPIC032-specific recorded events, evidence pointers, QA outcomes, remediation loops, ADRs, implementation results, and closeout interpretation.  
* PF23 is current-reality context only. It is not closure proof, not an acceptance source, and not a blocker source.  
* PF-Canon governs where PF10 is silent.  
* The Implementation Guide is scope framing only.  
* The QA Plan is intended QA requirement framing only.  
* The prompt label “Dissolution Pass 3” is recorded as invalid for the source epic name. PF10, PF23, the Implementation Guide, and the QA Plan identify HDE-EPIC032 as Fermentation Pass 3\.

Closure trace observed:

* HDE-EPIC032 is recorded as SATISFIED for this review’s closure trace only. That record is not a PO closeout action.  
* The Lead Dev implementation posture recommendation is READY.  
* D1 narrative router parity and indexing is recorded as satisfied through PR-01 evidence, key-table evidence, AB↔BA/two-run evidence, CLI/HTTP parity where defined, remedial token-overclaim correction, and later QA evidence/indexing clusters.  
* D2 narrative registry diffing, Doc-Delta identity, and indexing is recorded as satisfied through PR-02 registry diff, pack identity, sanity-pipeline ordering, canonical/indexed/mirrored/hashed/path-proven artifacts, and PO-013 through PO-015 PASS evidence.  
* D3 DB dev fallback, bridge capability, and provider parity is recorded as satisfied through the combined PR-03, OPS-01, PR-04, and ADR 2.10 evidence chain.  
* D4 non-dev total failure behavior and typed errors is recorded as satisfied through PR-04 non-dev typed failure behavior and related QA PASS evidence.  
* D5 DB posture acceptance, capture discipline, and Evidence Index/Mirror coherence is recorded as satisfied through PR-04 evidence coherence, manifest binding, primary-log headers, path-proof sidecars, tokenless posture, and PASS coverage across all QA clusters.  
* Deferred public Reader, HDAPI v2, and open-rails v2 scopes are recorded as satisfied by exclusion, not by implementation. The excluded scopes are not required deliverables for HDE-EPIC032.  
* The full Live QA ladder is recorded as PASS through Step-0A, Step-0B, and PO-001 through PO-024, with final readiness line “Ready for epic closeout.”  
* The DB provider/bridge token ambiguity is recorded as resolved for this epic by treating DB provider parity, bridge capability, and bridge fallback names as non-token proof labels unless Governance admits them.  
* PO-010 is recorded as remediated and reclassified correctly as PR-routed non-QA-root generator remediation, with structural `selection_order` proof.  
* Documentation drainage and PF09.5 physical drainage are recorded as non-blocking by themselves when PF10 has the relevant live supportability record.  
* PF23 supports current-reality context for key repo roots and components, but is not used as closure proof.

Path and surface closure ledger observed:

* QA manifest and manifest path-proof evidence center on `audit/qa/hde-epic032/qa_step_logs_manifest.json` and `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`.  
* PO-010 closure evidence centers on `audit/qa/hde-epic032/checks/po-010/result.json`, `audit/qa/hde-epic032/checks/po-010/primary.log`, and `audit/qa/hde-epic032/checks/po-010/primary.log.path_proof.txt`.  
* DB bridge and provider-parity closure evidence centers on `artifacts/db_bridge/adapter_selection.snapshot.json`, `artifacts/db_bridge/provider_parity.proof.json`, `artifacts/runtime/env_connectivity.nondev_failure.json`, `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`, `engine/db/adapter.py`, `tools/evidence/generate_db_bridge_parity.py`, `tests/db/test_adapter_selection.py`, and `tests/evidence/test_generate_db_bridge_parity_nondev.py`.  
* Evidence-index closure evidence centers on `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and `tools/evidence/update_evidence_index.py`.  
* Narrative closure evidence centers on `audit/gates/narratives/keys_10x4.table.json`, `artifacts/narratives/router/parity_abba.log`, `audit/gates/narratives/registry.diff.json`, and `audit/gates/narratives/pack_identity.txt`.  
* PF23 current-reality context records the repository root `/workspace/glow-hdengine-v2`, commit `eac3286958161f072e5d8eb6039f05c4d60423e9`, and observed top-level roots `adapter/`, `engine/`, `presenter/`, `docs/`, `artifacts/`, `audit/`, `tools/`, `ci/`, and `tests/` as context only.  
* Public Reader contract, HDAPI v2 inventory, HDAPI v2 adapter, HDAPI v2 live conformance, and open-rails v2 smoke remain deferred or boundary surfaces, not closure deliverables for this epic.

Lead Dev implementation report observed:

* PR-01 delivered narrative router parity/indexing after remedial token-overclaim correction.  
* PR-02 delivered narrative registry diffing, Doc-Delta identity, pack identity, and evidence indexing after validation bugs and orientation evidence drift were remediated.  
* PR-03 delivered DB bridge fallback, bridge capability, and provider parity as an accepted implementation slice, but did not itself move `HDE-FERM004.2`.  
* OPS-01 delivered provider parity closure evidence as OPS evidence only, not QA evidence, not PF09 status movement, not epic closure, and not token satisfaction.  
* PR-04 delivered non-dev typed DB failure behavior and DB evidence coherence, supporting `HDE-FERM004.3` and `HDE-FERM004.4` while not itself moving `HDE-FERM004.2`.  
* Remedial PR-01 stabilized structural DB adapter selection-order evidence after the PO-010 `selection_order_missing` failure and contributed to PO-010, PO-011, and PO-012 PASS evidence.  
* The evidence inventory repeats the narrative, DB, OPS, QA, Human Evidence Index, Machine Mirror, and per-check log families already recorded in PF14’s HDE-EPIC032 records.  
* The closure review records one evidence gap as Unknown: whether direct final repo path existence checks are current after the docs PR. This Unknown is recorded as a future audit or review concern, not a PF14 blocker or closure-proof source.

Lead Dev retrospective process lessons observed:

* PF10 captured a complete addendum chain from implementation through QA closeout.  
* Phase boundaries were preserved, and deferred HDAPI v2, live-provider, and public Reader scope were not absorbed.  
* Token ambiguity was surfaced early enough to prevent DB proof labels from becoming false acceptance tokens.  
* PR-03 did not overstate `HDE-FERM004.2`; the combined-evidence ADR resolved supportability instead of treating one PR as the entire proof.  
* OPS-01 remained OPS evidence and did not become QA evidence, PF09 status movement, epic closure, or token satisfaction.  
* PR-04 changed synthetic or permissive evidence behavior into fail-closed behavior.  
* Final QA evidence included manifest, path-proof, primary-header, rails, tokenless posture, and current-state evidence.  
* Remedial PR-01 correctly reclassified PO-010 non-QA-root generator work as PR remediation.  
* Documentation drainage stayed separated from execution and closure blockers.  
* Initial defects included unsupported token overclaim, validation bugs, orientation evidence drift, missing production-like `APP_ENV=live` handling, EPIC-specific adapter-selection key drift, provider parity `ddl_fingerprint` looping, wrong non-dev failure posture, hardcoded selection order, broad path-proof churn, string-presence versus structural-field mismatch, and unavailable initial PO-010 failure artifacts.

Lead Dev system lessons observed:

* Narrative router behavior can be proved through matrix, missing-key, identity, and parity tests.  
* Narrative registry identity depends on canonical manifest bytes and pack identity, not narrative prose payloads.  
* DB bridge path guard semantics must cover `prod`, `production`, and `live`.  
* Provider parity needs row-level closure evidence when active corpus rows are disputed.  
* Non-dev total failure should be proved in a non-production posture such as `APP_ENV=stage`, not production guard posture.  
* DB selection order must be derived from observed adapter attempts/provider order.  
* Evidence generators should hard-fail on unexpected behavior rather than serialize synthetic unexpected states.  
* Human Evidence Index and Machine Mirror coherence must be maintained as same-PR evidence discipline when governed artifacts change.  
* Public Reader contract boundaries remain stable even when narrative and DB runtime internals change.  
* Structural JSON proof is stronger than raw string-presence proof for governed evidence fields.  
* Single-writer Evidence Index and Machine Mirror discipline remains central to DB and narrative proof trust.

ADR and ambiguity resolution observed:

* HDE-FERM004.2 combined-evidence supportability is recorded with Option 3: combined PR-03, OPS-01, and PR-04 evidence. The final decision for this epic is that combined evidence supports `HDE-FERM004.2` to Done for QA-readiness purposes, while PF09.5 row drainage remains later non-blocking canon maintenance.  
* DB provider/bridge proof labels are recorded as non-token proof labels until Governance admits them.  
* PO-010 non-QA-root generator remediation is recorded as PR-routed remediation, not bounded Moon Loop correction.  
* Public Reader and HDAPI v2 scope remains deferred. No public Reader contract change and no HDAPI v2 or live-provider conformance expansion are recorded for this epic.

Future work and recommendation posture observed:

* Future structural JSON predicate checks, docs lint, broad path-proof churn reduction, reusable OPS closure packet patterns, DB provider/bridge proof-label drainage, `APP_ENV=live` production-like alias documentation, repo-only audit prompts, and PF23 drift routing remain future cards or owner-home documentation work. They do not create current PF14 implementation tasks, PF09 status moves, acceptance-token claims, QA-blocking conditions, or closeout blockers.  
* Implementation and process are recorded as strong enough to support phase-close for this review’s closure trace.  
* The epic delivered its in-scope Fermentation Pass 3 narrative/router, registry, DB runtime, and evidence-coherence objectives.  
* The strongest process improvements to carry forward are structural predicates, PR-routed non-QA-root remediation, token validation before evidence-row acceptance, and manifest/header/path-proof-first QA review.  
* Hard requirements before PO closeout action remain outside this review’s authority; the review does not perform PO closeout.  
* PF10 2.1, PF10 2.16, and the HDE-FERM004.2 combined-evidence decision are recorded as candidates for permanent PF-Canon memorialization when PO or TW assigns documentation work.  
* Deferred public Reader, HDAPI v2, and live-provider conformance work should remain deferred unless a later epic explicitly scopes it.

HDE-EPIC033 PR-01 HDAPI v2 and legacy v1 contract-inventory proof family observed (records-only). PF14 records these paths as the observed PR-01 proof family for the inventory-only HDE-FERM006 slice. This is a records-only closure trace and does not create a PF09 status action, PF09 drainage, acceptance-token source, runtime v2 conformance claim, runtime request-shaping claim, open-rails vendor-smoke claim, public Reader contract change, new HTTP home, HDE-FERM007 claim, HDE-FERM008 claim, or AI scope.

Observed PR-01 paths include:

* `tools/evidence/generate_hdapi_v2_contract_inventory.py`  
* `tests/evidence/test_hdapi_v2_contract_inventory.py`  
* `tools/evidence/update_evidence_index.py`  
* `artifacts/vendor/hdapi_v2/source_inventory.json`  
* `artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/source_inventory.md`  
* `artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/openapi_validation.log`  
* `artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* `artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv`  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/contract_map.json`  
* `artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/source_cache/api-reference.openapi.json`  
* `artifacts/vendor/hdapi_v2/source_cache/authentication.body`  
* `artifacts/vendor/hdapi_v2/source_cache/coordinates_guide.body`  
* `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`  
* `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`  
* `artifacts/vendor/hdapi_v2/source_cache/migration_v1_to_v2.body`  
* `artifacts/vendor/hdapi_v2/source_cache/rate_limiting.body`  
* `artifacts/vendor/hdapi_v2/source_cache/response_format.body`  
* `artifacts/vendor/hdapi_v2/source_cache/robots_preflight.body`  
* `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`  
* `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`  
* `artifacts/vendor/hdapi_v2/source_cache/v1_overview.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_coordinates_chart_page.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_full_chart_page.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_overview.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_simple_chart_page.body`  
* `docs/acceptance_map_epic033.json`  
* `docs/acceptance_map_epic033.json.path_proof.txt`  
* `audit/qa/hde-epic033/token_evidence_matrix.md`  
* `audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt`  
* `audit/qa/hde-epic033/acceptance_map_viability.log`  
* `audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt`  
* `audit/docdeltas/hde-epic033_doc_deltas.md`  
* `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`  
* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

Observed PR-01 proof posture. The PR-01 family records source inventory, OpenAPI validation, known-anomaly quarantine posture, endpoint reference, contract map, source-cache inputs, path proofs, acceptance map, token evidence matrix, Human Evidence Index updates, and Machine Evidence Mirror updates for HumanDesignAPI v2 and legacy v1 contract inventory.

Observed PR-01 inventory-only boundary posture. The PR-01 family completes the inventory-only HDE-FERM006 slice for this review record and preserves out-of-scope boundaries for HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader changes, new HTTP homes, and AI scope. The record states no runtime v2 request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route, public flag, public payload, new HTTP home, or AI runtime feature was introduced.

Observed PR-01 source and AI boundary posture. The source inventory records public same-origin HumanDesignAPI documentation sources only. It does not call credentialed runtime vendor endpoints and does not claim runtime v2 conformance. AI or LLM-oriented documentation, including `llms.txt` and `llms-full.txt`, is classified as documentation-discovery-only context and creates no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.

Observed PR-01 validation and anomaly posture. The PR-01 family records validated `v2-routes.yaml` and `v1-routes.yaml`, quarantined suspect `api-reference/openapi.json`, known-anomaly evidence, and route-spec gate PASS. Suspect OpenAPI unavailability is recorded as non-blocking when validated v2 and v1 route specs can still produce the promoted contract inventory.

Observed PR-01 endpoint and contract-map posture. The PR-01 family records required v2 and legacy v1 endpoints, including recommended v2 chart routes and legacy v1 BodyGraph routes. It distinguishes recommended v2 chart routes from legacy v1 BodyGraph routes and records auth, geocode posture, request fields, success envelopes, error codes, and source specifications without declaring runtime conformance.

Observed PR-01 generator remediation posture. The final PR-01 state records remediation for stale quarantine-test behavior, metadata-only closed-rails replay, hard-coded endpoint-tier handling, and suspect OpenAPI unavailability blocking promoted inventory generation. The accepted state requires closed-rails cache bodies and checksums for source-inventory rows, records cache paths and cache checksums for rendered pages, route specs, `llms.txt`, and the bounded `llms-full` endpoint-tier excerpt, parses current endpoint table cells for tier handling, and quarantines unavailable suspect OpenAPI input while allowing validated v2 and v1 route specs to proceed.

Observed PR-01 evidence binding posture. The PR-01 family records same-PR Human Evidence Index, hash sentinel, Machine Mirror, Machine Mirror hash sentinel, path-proof, and orientation refresh. Collateral path-proof refreshes are recorded as limited evidence-tooling convergence and not as feature or contract scope.

Observed PR-01 token and acceptance-map posture. The PR-01 family records existing registry-valid baseline tokens only and does not mint a vendor-v2-specific token. The acceptance viability evidence records no vendor-v2-specific tokens, no runtime v2 conformance claim, no public Reader surface change, and no AI scope.

Observed PR-01 validation posture. The final PR-01 record includes public-documentation refresh, closed-rails generator replay, targeted HDAPI contract-inventory tests, full evidence tests, Evidence Index updater check, orientation check, evidence path validation, LF checks, mirror schema check, evidence hash check, final-LF check, and `git diff --check` as passing.

Observed PR-01 PF09 status boundary. The Source Blob records a PF09 status recommendation for HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4. PF14 records only the mechanics support and no-claim boundaries; it does not make a PF09 status decision.

HDE-EPIC033 Implementation Retrospective observed (records-only). PF14 records the mechanics-relevant retrospective portions as a closure trace for the Fermentation Pass 4 HDE-FERM006 contract-inventory slice. This block does not create a PF09 status action, PF09 drainage, acceptance-token source, Lead closure decision, epic closeout action, runtime v2 conformance claim, runtime request-shaping claim, open-rails vendor-smoke claim, public Reader contract change, new HTTP home, HDE-FERM007 claim, HDE-FERM008 claim, or AI scope.

Final retrospective scope observed:

* HDE-EPIC033 focused on Fermentation Pass 4 and the HDE-FERM006 HumanDesignAPI v2 and legacy v1 contract-inventory slice, not runtime adapter implementation.  
* The implementation completed the inventory-only HDE-FERM006 slice for this review record and preserved the out-of-scope boundaries for HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader changes, new HTTP homes, and AI scope.  
* HDE-FERM006 creates a source-backed governed evidence base for later HumanDesignAPI v2 request-shaping and adapter work; it does not prove runtime v2 conformance.

Final retrospective PR and evidence ledger observed:

* PR-01 delivered the governed HumanDesignAPI v2 and legacy v1 contract-inventory evidence family: source inventory, OpenAPI validation, known-anomaly quarantine posture, endpoint reference, contract map, source-cache inputs, path proofs, acceptance map, token evidence matrix, Human Evidence Index updates, and Machine Evidence Mirror updates.  
* PR-01 created and regenerated HDAPI v2 artifacts, source metadata and cache, path proofs, Human Evidence Index, Machine Mirror, hash sentinels, and related proof timestamps.  
* PR-01 added generator logic and source-cache inputs for closed-rails replay, cache checksum verification, source-parsed tier handling, and non-blocking suspect OpenAPI quarantine.  
* PR-01 added regression tests for HDAPI v2 contract inventory, cache body verification, endpoint-tier parsing, unavailable suspect OpenAPI handling, index and path-proof binding, and mirror chronology.  
* PR-01 validation records generator refresh and replay, targeted HDAPI tests, full evidence tests, Evidence Index checks, orientation checks, path validation, LF checks, mirror schema checks, evidence hash checks, final-LF checks, and `git diff --check` as passing.  
* PR-01 final review records PR ACCEPTABLE and support for changing HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 to Done. PF14 records this as mechanics support and no-claim boundary only; PF14 does not make the PF09 status decision.

Final retrospective docs-sweep ledger observed:

* The final repo-docs sweep updated README.md, CHANGELOG.md, AGENTS.md, docs/INDEX.md, and docs/EVIDENCE\_INDEX.md to reflect HDE-EPIC033 PR-01 without expanding scope into runtime conformance.  
* The README update documented the HumanDesignAPI v2 and legacy v1 contract-inventory evidence family, verified evidence homes, source-cache posture, quarantine posture for suspect `api-reference/openapi.json`, AI and LLM documentation-discovery-only boundary, and HDE-FERM007/HDE-FERM008 follow-up boundary.  
* The CHANGELOG entry distinguished contract-inventory evidence from runtime v2 conformance, public Reader changes, open-rails vendor smoke, and AI scope.  
* AGENTS.md guidance covered inventory-only scope, evidence anchors, closed-rails source-cache replay, explicit public-doc refresh rails, AI and LLM context boundaries, OpenAPI quarantine posture, and rendered-escape review handling.  
* The docs sweep records no code, tests, schemas, generated evidence artifacts, implementation files, or PF canon files changed.

Final retrospective surface ledger observed:

* Vendor seam and HDAPI contract-inventory surfaces were affected through contract inventory artifacts, endpoint reference, contract map, source-cache inputs, and anomaly posture for HumanDesignAPI v2 and legacy v1.  
* Evidence surfaces were affected through governed evidence artifacts, path proofs, Human Evidence Index, Evidence Index hash sentinel, Machine Mirror, Machine Mirror checksum, and proof timestamps.  
* QA harness and evidence-tooling surfaces were affected through generator and regression-test coverage for HDAPI v2 inventory, cache bodies, endpoint-tier parsing, unavailable suspect OpenAPI handling, index/path-proof binding, and mirror chronology.  
* Repo docs were affected through README.md, CHANGELOG.md, AGENTS.md, docs/INDEX.md, and docs/EVIDENCE\_INDEX.md.  
* CLI runtime behavior, API runtime behavior, and DB runtime behavior are not evidenced as changed by this retrospective. The report records those runtime surfaces as Unknown or not evidenced for HDE-EPIC033.

Final retrospective mechanics lessons observed:

* The HD Engine needed a governed HumanDesignAPI v2 and legacy v1 contract inventory before runtime adapter changes could safely proceed.  
* Source precedence matters: validated v2 and v1 YAML route specs must be distinguished from rendered pages and suspect OpenAPI artifacts.  
* Suspect `api-reference/openapi.json` cannot be treated as authoritative unless validation proves HumanDesignAPI ownership.  
* `llms.txt` and `llms-full.txt` may support documentation discovery only; they must not introduce AI product scope, AI runtime scope, AI evidence families, AI-provider config keys, AI rails, AI tokens, or AI QA obligations.  
* HDE-FERM006 evidence does not equal runtime v2 conformance.  
* Endpoint reference evidence must record route family, auth model, geocode-key requirement, tier, request content type, request fields, success envelope, error codes, and source specification.  
* Contract-map evidence must bind the required v2 and v1 route families, including `POST /v2/charts`, `POST /v2/charts/simple`, `POST /v2/charts/coordinates`, `POST /v1/bodygraphs`, and `POST /v1/bodygraphs/simple`.  
* Human Evidence Index and Machine Mirror parity remains central for this evidence family.  
* Vendor documentation refresh remains sensitive to external source changes, but cache-body verification, tier parsing, unavailable suspect OpenAPI handling, and anomaly behavior tests reduce that risk.

Final retrospective missing or ambiguous evidence observed:

* A Lead closure decision is not present in the reviewed evidence. A Lead closure artifact, closure memo, board status update, or closure decision record would be needed to prove Lead closure.  
* PF09.5 still showed HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 as Not done in the referenced source, while Build Notes supported changing them to Done. A later PF09.5 drain, update, or closure artifact would be needed to prove physical status drainage.  
* HDE-FERM007 implementation proof was not present. Future artifacts would be needed for v2 source-selection policy, request shaping, response normalization, adapter-boundary proof, and closed-rails deterministic shaping.  
* HDE-FERM008 live conformance and open-rails proof were not present. Future PR or OPS evidence would be needed for closed-rails refusal, PO-only open-rails v2 smoke, error and rate-limit mapping, normalized data path proof, and v2 conformance indexing.  
* Runtime HumanDesignAPI v2 conformance is not evidenced by this epic. The inventory must not be treated as runtime implementation.  
* Explicit Build Notes coverage of the docs PR outcome was not present in the reviewed retrospective. The docs PR artifact supplies repo-docs evidence, but a later Build Notes addendum or closeout entry would be needed to record that docs PR outcome there.

Final retrospective boundary posture observed:

* PF14 records the implementation evidence, docs-sweep evidence, mechanics lessons, and no-claim boundaries only.  
* PF14 does not make Lead closure decisions, PF09.5 status moves, PF09.5 drainage, close-pack decisions, or downstream HDE-FERM007/HDE-FERM008 scope decisions.  
* PF14 does not treat docs-sweep outcomes, rendered-escape process risks, or historical close-record questions as mechanics tasks.  
* PF14 does not create a vendor-v2-specific acceptance token, token semantic, evidence-home authority, public Reader contract change, runtime v2 conformance claim, open-rails vendor-smoke claim, new HTTP home, AI scope, or future implementation task from this retrospective.

HDE-EPIC033 Live QA Step-0B through PO-009 evidence paths observed (records-only):

* checks/step-0b-doc-delta-capture:  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log`  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
  * `audit/docdeltas/hde-epic033_doc_deltas.md`  
  * `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`  
* checks/po-001:  
  * `audit/qa/hde-epic033/checks/po-001/primary.log`  
  * `audit/qa/hde-epic033/checks/po-001/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/source_inventory.json`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`  
* checks/po-002:  
  * `audit/qa/hde-epic033/checks/po-002/primary.log`  
  * `audit/qa/hde-epic033/checks/po-002/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-003:  
  * `audit/qa/hde-epic033/checks/po-003/primary.log`  
  * `audit/qa/hde-epic033/checks/po-003/primary.log.path_proof.txt`  
  * `tests/evidence/test_hdapi_v2_contract_inventory.py`  
* checks/po-004:  
  * `audit/qa/hde-epic033/checks/po-004/primary.log`  
  * `audit/qa/hde-epic033/checks/po-004/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-005:  
  * `audit/qa/hde-epic033/checks/po-005/primary.log`  
  * `audit/qa/hde-epic033/checks/po-005/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
* checks/po-006:  
  * `audit/qa/hde-epic033/checks/po-006/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-006-remediation-r3:  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-007:  
  * `audit/qa/hde-epic033/checks/po-007/primary.log`  
  * `audit/qa/hde-epic033/checks/po-007/primary.log.path_proof.txt`  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `docs/evidence/INDEX.json.path_proof.txt`  
  * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* checks/po-008:  
  * `audit/qa/hde-epic033/checks/po-008/primary.log`  
  * `audit/qa/hde-epic033/checks/po-008/primary.log.path_proof.txt`  
  * `docs/acceptance_map_epic033.json`  
  * `audit/qa/hde-epic033/token_evidence_matrix.md`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`  
* checks/po-009:  
  * `audit/qa/hde-epic033/checks/po-009/primary.log`  
  * `audit/qa/hde-epic033/checks/po-009/primary.log.path_proof.txt`  
  * `docs/acceptance_map_epic033.json`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`

HDE-EPIC033 Live QA Step-0B through PO-009 current-state notes observed (records-only).

* Step-0B records PASS for doc-delta capture with exit code `0`, final `primary.log` header status PASS, governed evidence under `audit/**`, a check-scoped primary log, a sibling primary-log path-proof transcript, two doc-delta surfaces, two doc-delta sibling path proofs, and no broader HDE-EPIC033 closure claim.  
* Step-0B records no deviation or Moon Loop repair, no FAIL\_BEHAVIOR, no FAIL\_TOOLING, no TOOLING\_BLOCKED, no missing required file, no stale or mismatched path proof, and no missing primary-log path proof.  
* PO-001, PO-002, and PO-003 record PASS with exit code `0`, final `primary.log` header status PASS, governed roots under `audit/**` and `artifacts/**`, check-scoped primary logs, sibling path-proof transcripts, closed rails, determinism pins, and no unplanned token claim.  
* checks/po-001 records PASS for source-inventory grounding, including closed-rails source-cache mode, `cache_path`, `cache_sha256`, required source-cache files, and source inventory artifacts.  
* checks/po-002 records PASS for AI and LLM vendor-documentation boundary posture, including `llms.txt` and `llms-full.txt` classified as documentation-discovery-only context and no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.  
* checks/po-003 records PASS for targeted HDAPI v2 contract-inventory tests, with `TESTS_PASS_OK` claimed by that step and with a recorded operational deviation where Ruby was installed by `sudo apt-get` to satisfy a pytest dependency before rerun to PASS. The deviation is recorded as acceptable for the step because it changed no required deliverable and did not change PASS or FAIL criteria.  
* PO-004, PO-005, and PO-006 record PASS for the step group, with PO-006 accepted through the Moon Loop Remediation R3 receipt as the final PO-006 proof basis.  
* checks/po-004 records PASS for suspect OpenAPI quarantine and non-authority posture. The suspect `api-reference/openapi.json` is recorded as quarantined and not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance, while validated YAML route specs remain first-precedence authority for the contract-inventory slice.  
* checks/po-005 records PASS for endpoint reference and contract-map posture, including all five required route rows and both route-family labels for recommended v2 chart routes and legacy v1 BodyGraph routes.  
* checks/po-006 records an initial FAIL\_BEHAVIOR context caused by a QA-harness-only brittle phrase-match defect, not by a product, repo-test, public-contract, or non-QA-root governed-artifact defect. The accepted R3 remediation stays within `audit/qa/hde-epic033/checks/`, preserves the same proof target, and satisfies contract-map parseability, final-LF, non-conformance, and no-runtime-request-shaping PASS criteria.  
* PO-006 Moon Loop remediation is recorded as bounded QA evidence-harness remediation under the approved QA root. It does not modify product code, repo tests, public contracts, PF documents, acceptance tokens, or governed non-QA-root artifacts.  
* PO-007, PO-008, and PO-009 record PASS with exit code `0`, final `primary.log` header status PASS, governed roots under `audit/**`, `docs/**`, and `artifacts/**`, check-scoped QA receipts, sibling path proofs, and no broader HDE-EPIC033 closure claim.  
* checks/po-007 records PASS for governed evidence binding, including Human Evidence Index presence, Machine Mirror presence, hash sentinels, path-proof files, and evidence-index or mirror artifacts.  
* checks/po-008 records PASS for acceptance-token posture, including baseline existing-token posture, vendor-v2-specific tokens recorded as NONE, existing registry-valid tokens only, and no minted vendor-v2-specific token.  
* checks/po-009 records PASS for HDE-FERM006 supportability posture, including HDE-FERM006.1 through HDE-FERM006.4 bound in the acceptance map, no runtime v2 conformance claim, repo-evidence-only supportability, and no PF09.5 drainage claim by the check.  
* PO-007 through PO-009 record no final FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, required-file absence, stale path proof, missing primary-log path-proof, or token-posture mismatch.  
* PO-007 through PO-009 record two acceptable execution deviations: a reconstructed PF27-compatible helper wrapper because the pasted helper transcript was truncated or malformed, and a PO-009 proof-posture append that added explicit `repo_evidence_supportable_only=true` and `pf09_5_drainage_claim=UNPROVEN_BY_THIS_CHECK` lines to the receipt. The deviations are recorded as bounded and do not alter required deliverables or PASS or FAIL posture.  
* PF14 records these Live QA entries as mechanics evidence records only. They do not create PF09 status movement, PF09 drainage, acceptance-token authority, final epic closure, runtime v2 conformance, runtime request shaping, open-rails vendor smoke, public Reader contract change, new HTTP home, HDE-FERM007 scope, HDE-FERM008 scope, or AI scope.

HDE-EPIC033 Live QA Step-0B through PO-009 evidence paths observed (records-only):

* checks/step-0b-doc-delta-capture:  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log`  
  * `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
  * `audit/docdeltas/hde-epic033_doc_deltas.md`  
  * `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md`  
  * `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`  
* checks/po-001:  
  * `audit/qa/hde-epic033/checks/po-001/primary.log`  
  * `audit/qa/hde-epic033/checks/po-001/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/source_inventory.json`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`  
  * `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`  
* checks/po-002:  
  * `audit/qa/hde-epic033/checks/po-002/primary.log`  
  * `audit/qa/hde-epic033/checks/po-002/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`  
  * `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-003:  
  * `audit/qa/hde-epic033/checks/po-003/primary.log`  
  * `audit/qa/hde-epic033/checks/po-003/primary.log.path_proof.txt`  
  * `tests/evidence/test_hdapi_v2_contract_inventory.py`  
* checks/po-004:  
  * `audit/qa/hde-epic033/checks/po-004/primary.log`  
  * `audit/qa/hde-epic033/checks/po-004/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/openapi_validation.log`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-005:  
  * `audit/qa/hde-epic033/checks/po-005/primary.log`  
  * `audit/qa/hde-epic033/checks/po-005/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/endpoint_reference.csv`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
* checks/po-006:  
  * `audit/qa/hde-epic033/checks/po-006/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-006-remediation-r3:  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log`  
  * `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* checks/po-007:  
  * `audit/qa/hde-epic033/checks/po-007/primary.log`  
  * `audit/qa/hde-epic033/checks/po-007/primary.log.path_proof.txt`  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * `docs/evidence/INDEX.json.path_proof.txt`  
  * `docs/evidence/INDEX.sha256.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.path_proof.txt`  
  * `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* checks/po-008:  
  * `audit/qa/hde-epic033/checks/po-008/primary.log`  
  * `audit/qa/hde-epic033/checks/po-008/primary.log.path_proof.txt`  
  * `docs/acceptance_map_epic033.json`  
  * `audit/qa/hde-epic033/token_evidence_matrix.md`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`  
* checks/po-009:  
  * `audit/qa/hde-epic033/checks/po-009/primary.log`  
  * `audit/qa/hde-epic033/checks/po-009/primary.log.path_proof.txt`  
  * `docs/acceptance_map_epic033.json`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`

HDE-EPIC033 Live QA Step-0B through PO-009 current-state notes observed (records-only).

* Step-0B records PASS for doc-delta capture with exit code `0`, final `primary.log` header status PASS, governed evidence under `audit/**`, a check-scoped primary log, a sibling primary-log path-proof transcript, two doc-delta surfaces, two doc-delta sibling path proofs, and no broader HDE-EPIC033 closure claim.  
* Step-0B records no deviation or Moon Loop repair, no FAIL\_BEHAVIOR, no FAIL\_TOOLING, no TOOLING\_BLOCKED, no missing required file, no stale or mismatched path proof, and no missing primary-log path proof.  
* PO-001, PO-002, and PO-003 record PASS with exit code `0`, final `primary.log` header status PASS, governed roots under `audit/**` and `artifacts/**`, check-scoped primary logs, sibling path-proof transcripts, closed rails, determinism pins, and no unplanned token claim.  
* checks/po-001 records PASS for source-inventory grounding, including closed-rails source-cache mode, `cache_path`, `cache_sha256`, required source-cache files, and source inventory artifacts.  
* checks/po-002 records PASS for AI and LLM vendor-documentation boundary posture, including `llms.txt` and `llms-full.txt` classified as documentation-discovery-only context and no AI product, runtime, evidence, token, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope.  
* checks/po-003 records PASS for targeted HDAPI v2 contract-inventory tests, with `TESTS_PASS_OK` claimed by that step and with a recorded operational deviation where Ruby was installed by `sudo apt-get` to satisfy a pytest dependency before rerun to PASS. The deviation is recorded as acceptable for the step because it changed no required deliverable and did not change PASS or FAIL criteria.  
* PO-004, PO-005, and PO-006 record PASS for the step group, with PO-006 accepted through the Moon Loop Remediation R3 receipt as the final PO-006 proof basis.  
* checks/po-004 records PASS for suspect OpenAPI quarantine and non-authority posture. The suspect `api-reference/openapi.json` is recorded as quarantined and not used as authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance, while validated YAML route specs remain first-precedence authority for the contract-inventory slice.  
* checks/po-005 records PASS for endpoint reference and contract-map posture, including all five required route rows and both route-family labels for recommended v2 chart routes and legacy v1 BodyGraph routes.  
* checks/po-006 records an initial FAIL\_BEHAVIOR context caused by a QA-harness-only brittle phrase-match defect, not by a product, repo-test, public-contract, or non-QA-root governed-artifact defect. The accepted R3 remediation stays within `audit/qa/hde-epic033/checks/`, preserves the same proof target, and satisfies contract-map parseability, final-LF, non-conformance, and no-runtime-request-shaping PASS criteria.  
* PO-006 Moon Loop remediation is recorded as bounded QA evidence-harness remediation under the approved QA root. It does not modify product code, repo tests, public contracts, PF documents, acceptance tokens, or governed non-QA-root artifacts.  
* PO-007, PO-008, and PO-009 record PASS with exit code `0`, final `primary.log` header status PASS, governed roots under `audit/**`, `docs/**`, and `artifacts/**`, check-scoped QA receipts, sibling path proofs, and no broader HDE-EPIC033 closure claim.  
* checks/po-007 records PASS for governed evidence binding, including Human Evidence Index presence, Machine Mirror presence, hash sentinels, path-proof files, and evidence-index or mirror artifacts.  
* checks/po-008 records PASS for acceptance-token posture, including baseline existing-token posture, vendor-v2-specific tokens recorded as NONE, existing registry-valid tokens only, and no minted vendor-v2-specific token.  
* checks/po-009 records PASS for HDE-FERM006 supportability posture, including HDE-FERM006.1 through HDE-FERM006.4 bound in the acceptance map, no runtime v2 conformance claim, repo-evidence-only supportability, and no PF09.5 drainage claim by the check.  
* PO-007 through PO-009 record no final FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, required-file absence, stale path proof, missing primary-log path-proof, or token-posture mismatch.  
* PO-007 through PO-009 record two acceptable execution deviations: a reconstructed PF27-compatible helper wrapper because the pasted helper transcript was truncated or malformed, and a PO-009 proof-posture append that added explicit `repo_evidence_supportable_only=true` and `pf09_5_drainage_claim=UNPROVEN_BY_THIS_CHECK` lines to the receipt. The deviations are recorded as bounded and do not alter required deliverables or PASS or FAIL posture.  
* PF14 records these Live QA entries as mechanics evidence records only. They do not create PF09 status movement, PF09 drainage, acceptance-token authority, final epic closure, runtime v2 conformance, runtime request shaping, open-rails vendor smoke, public Reader contract change, new HTTP home, HDE-FERM007 scope, HDE-FERM008 scope, or AI scope.

HDE-EPIC033 continued Live QA evidence paths observed (records-only):

* checks/po-010:  
  * `audit/qa/hde-epic033/checks/po-010/primary.log`  
  * `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`  
  * `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`  
* checks/po-011:  
  * `audit/qa/hde-epic033/checks/po-011/primary.log`  
  * `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/source_inventory.md`  
  * `artifacts/vendor/hdapi_v2/contract_map.json`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`  
* checks/po-012:  
  * `audit/qa/hde-epic033/checks/po-012/primary.log`  
  * `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`  
  * `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt`  
  * `artifacts/vendor/hdapi_v2/known_anomalies.md`  
  * `docs/acceptance_map_epic033.json`  
  * `audit/qa/hde-epic033/acceptance_map_viability.log`  
* checks/po-013:  
  * `audit/qa/hde-epic033/checks/po-013/primary.log`  
  * `audit/qa/hde-epic033/checks/po-013/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log`  
  * `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log`  
  * `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log.path_proof.txt`  
  * `docs/evidence/INDEX.json`  
  * `artifacts/evidence_index.jsonl`  
  * `audit/gates/topology/orientation_demo.txt`  
* checks/po-014:  
  * `audit/qa/hde-epic033/checks/po-014/primary.log`  
  * `audit/qa/hde-epic033/checks/po-014/primary.log.path_proof.txt`  
* checks/qa-16-close-out-deliverables:  
  * `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log`  
  * `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt`  
  * `audit/qa/hde-epic033/qa_step_logs_manifest.json`  
  * `audit/qa/hde-epic033/qa_step_logs_manifest.json.path_proof.txt`  
  * `audit/qa/hde-epic033/00_meta/discovery_artifact.md`  
  * `audit/qa/hde-epic033/00_meta/discovery_artifact.md.path_proof.txt`  
  * `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md`  
  * `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`

HDE-EPIC033 continued Live QA current-state notes observed (records-only).

* PO-010, PO-011, and PO-012 record PASS with final claimed tokens none and rails pinned to SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev, LC\_ALL=C, LANG=C, and TZ=UTC.  
* checks/po-010 records an initial FAIL\_BEHAVIOR receipt caused by a QA evidence-harness phrase-match defect. The accepted final proof is the remediation receipt under `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`, with runtime request shaping, live vendor smoke, and runtime v2 conformance remaining unclaimed.  
* checks/po-011 records PASS without Moon Loop remediation. The final proof posture keeps contract inventory evidence inventory-only and does not claim runtime vendor conformance.  
* checks/po-012 records an initial FAIL\_BEHAVIOR receipt caused by the same QA evidence-harness phrase-match defect. The accepted final proof is the remediation receipt under `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`, with live vendor smoke, public Reader change, new HTTP home, and AI runtime or evidence scope remaining outside this epic.  
* PO-010 and PO-012 remediation records preserve the original proof targets while normalizing a brittle case-sensitive request-shaping phrase check inside the QA root. The accepted remediation receipts and sibling path proofs are recorded separately from the original FAIL\_BEHAVIOR receipts.  
* PO-013, PO-014, and qa-16-close-out-deliverables record PASS, with PO-013 accepted through the R3 remediation proof after a QA\_PLAN\_UPDATE routing receipt proved routing before final PASS-grade proof.  
* checks/po-013 records the original planned receipt as FAIL\_BEHAVIOR with ORIENTATION\_MISMATCH. The accepted R3 proof records QA\_PLAN\_UPDATE\_ROUTING\_OK, message\_count=0, EVIDENCE\_PATHS\_VALIDATED\_OK, LF\_CHECKS\_OK, ORIENTATION\_CHECK\_OK, MIRROR\_SCHEMA\_OK, EVIDENCE\_INDEX\_HASH\_OK, runtime\_v2\_conformance\_claim=NONE, public\_reader\_surface\_change=NONE, and ai\_scope=NONE.  
* checks/po-014 records PASS, exit code 0, and non-claims for implementation work, PF document edit, runtime vendor conformance, public Reader change, new HTTP home, AI scope, and epic closure action.  
* qa-16-close-out-deliverables records PASS and creates the QA step-log manifest, discovery artifact, QA RCA and Doc Delta summary, and sibling path proofs. It represents original planned receipts and accepted remediation receipts separately and does not claim PO closeout.  
* PO-010 through qa-16 records are mechanics evidence records only. They do not create PF09 status movement, PF09 drainage, acceptance-token authority, final epic closure, runtime v2 conformance, runtime request shaping, open-rails vendor smoke, public Reader contract change, new HTTP home, HDE-FERM007 scope, HDE-FERM008 scope, or AI scope.

HDE-EPIC033 final QA closeout review and QA RCA observed (records-only). PF14 records the mechanics-relevant closeout and RCA portions as a closure trace for HDE-EPIC033. This block does not create a PF09 status action, PF09 drainage, acceptance-token source, QA-plan authority, epic closeout action, OPS authorization, runtime v2 conformance claim, live vendor behavior claim, public Reader contract change, new HTTP home, HDE-FERM007 claim, HDE-FERM008 claim, or AI scope.

Final closeout source posture observed:

* PF10 is primary for HDE-EPIC033 QA events, outcomes, remediation loops, ADRs, and evidence pointers where it speaks.  
* PF19 supplies QA process and RCA basis where PF10 is silent.  
* PF27 was not used.  
* PF06 was not used.  
* The Implementation Guide was used for goals framing only.  
* The QA Plan was used for intended requirements framing only.  
* The completed epic scope is the HDE-FERM006 inventory-only HumanDesignAPI v2 and legacy v1 contract-inventory slice, not runtime adapter implementation.  
* Overall readiness is Ready with caveats.  
* Root cause category is evidence, procedure, and harness fragility around exact-string proof checks, rendered escape review posture, dependency readiness, and non-QA-root routing. PF10 does not support a product-runtime defect for the completed inventory-only scope.

Final closeout coverage observed:

* Step-0B is fully evidenced as PASS.  
* PO-001, PO-002, and PO-003 are fully evidenced as PASS, with PO-003 dependency readiness deviation accepted as non-blocking.  
* PO-004, PO-005, and PO-006 are fully evidenced as PASS, with PO-006 accepted through bounded QA-root Moon Loop remediation.  
* PO-007, PO-008, and PO-009 are fully evidenced as PASS.  
* PO-010, PO-011, and PO-012 are fully evidenced as PASS, with PO-010 and PO-012 accepted through bounded QA-root Moon Loop remediation and PO-011 accepted without Moon Loop remediation.  
* PO-013 is fully evidenced as PASS through QA\_PLAN\_UPDATE routing plus R3 final proof after an initial ORIENTATION\_MISMATCH.  
* PO-014 is fully evidenced as PASS.  
* qa-16-close-out-deliverables is fully evidenced as PASS and provides the QA step-log manifest, discovery artifact, QA RCA and Doc Delta summary, and path-proof surfaces.

Final RCA findings observed:

* PR-01 delivered the HDE-EPIC033 contract-inventory evidence family and PF10 records the evidence posture as sufficient for final PR acceptance.  
* PR-01 implementation remediation addressed stale quarantine-test behavior, metadata-only closed-rails replay, hard-coded tier handling, and suspect OpenAPI unavailability blocking promoted inventory generation.  
* Rendered escape artifacts created false-blocker risk by making display-layer text look like raw command, path, token, quote, evidence, or identity defects.  
* PO-003 required operational dependency-readiness remediation because Ruby was installed before rerun to PASS.  
* PO-006, PO-010, and PO-012 hit brittle case-sensitive proof-string failures around `no runtime v2 request shaping` versus `No runtime v2 request shaping`; PF10 records accepted bounded QA-root remediations.  
* PO-013 initially failed with FAIL\_BEHAVIOR, exit code 1, and ORIENTATION\_MISMATCH; final PASS required QA\_PLAN\_UPDATE routing plus R3 final remediation proof.  
* A Lead closure decision is not present in the reviewed evidence. The report can recommend readiness but must not assert that formal epic closure already occurred.  
* PF09.5 status text still showed HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 as Not done while PF10 supported change to Done. Repo-supported completion and canon drain completion must remain distinct.  
* HDE-FERM007 and HDE-FERM008 evidence is absent because downstream adapter architecture, runtime request shaping, open-rails smoke, live conformance, public Reader changes, new HTTP homes, and AI scope remain out of scope for HDE-FERM006.  
* Explicit PF10 coverage of the docs PR outcome is missing, so docs PR history must not be used as PF10 execution proof unless a later record explicitly binds it.

Final RCA implementation-gap records observed:

* IMP-01 records HDE-FERM007 implementation proof as not present. Future work would need to prove v2 source-selection policy, request shaping, response normalization, adapter-boundary proof, and closed-rails deterministic shaping.  
* IMP-02 records HDE-FERM008 live conformance and open-rails proof as not present. Future work would need to prove closed-rails refusal, PO-only open-rails v2 smoke, error and rate-limit mapping, normalized data path proof, and v2 conformance indexing.  
* IMP-03 records brittle exact-case proof-string checks against governed prose. Future proof checks should validate stable semantic posture or canonical machine-readable fields where available rather than treating prose casing as behavior.  
* IMP-04 records that non-QA-root evidence refresh required explicit QA\_PLAN\_UPDATE routing before final PASS-grade proof. Future final proof receipts should include routing receipt pointers before post-refresh gate outputs when relying on refreshed governed evidence outside the check-scoped QA root.

Final closeout verdict and recommendation observed:

* Verdict is READY WITH CAVEATS.  
* Strong PF10 evidence pointers support PR-01 evidence readiness, Step-0B PASS, PO-001 through PO-014 PASS, and qa-16 closeout deliverables PASS.  
* The strongest PF10 evidence clusters are governed HDAPI v2 and legacy v1 contract-inventory evidence, evidence index, mirror, and path-proof coherence, QA Plan coverage through all Live QA steps, and explicit remediation records for PO-006, PO-010, PO-012, and PO-013.  
* Caveat: a Lead closure decision is not present in reviewed evidence.  
* Caveat: PF09.5 drain/status text is missing or unclear; repo-supported completion and PF10-supported Done posture are not the same as canon-drain completion.  
* Caveat: HDE-FERM007 and HDE-FERM008 remain out of scope and not evidenced. This epic must not be treated as runtime v2 adapter conformance, live vendor conformance, public Reader change, new HTTP home, or AI scope.  
* Caveat: PF10 does not explicitly cover the docs PR outcome; docs PR history must not be used as PF10 execution proof unless a later record explicitly binds it.  
* Suggested follow-up is owner-home documentation work only. It does not create a PF14 task, PF09 status action, QA-blocking condition, acceptance-token claim, or closeout blocker.

### **37.4.1 CLI help and argument-policing captures for conjunction-mode evidence**

When a governed review, QA step, or docs-evidence update depends on the shipped CLI syntax or CLI rejection behavior for conjunction flows, governed capture artifacts MUST be recorded for:

* `hdctl --help`

* `hdctl showcompat --help`

* any intentionally rejected unsupported conjunction-modifier invocation exercised by the step

The capture family MUST:

* record the exact command invoked

* capture stdout, stderr, and exit code as produced by the command

* live under a governed repo path

* be listed in the Human Index and mirrored 1:1 in the Machine Mirror with a co-located path-proof

* be refreshed in the same PR whenever the shipped help text, accepted conjunction modifiers, or CLI rejection behavior changes

Help captures are evidence of the shipped CLI help surfaces only. Rejection captures are evidence of CLI argument-policing behavior only. PF05 remains the single home for CLI contract bytes, flag semantics, and exit-code mappings.

### **37.4.2 CLI installability and conformance captures for conjunction-mode evidence**

Generation tool (normative). Canonical entrypoint: `python tools/cli/generate_cli_conformance_artifacts.py`. The generator MUST produce positive, non-skipped installability proof and MUST fail closed if the console entrypoint required by the run is missing.

Required governed artifacts. When CLI conformance evidence is refreshed for conjunction work, the governed capture family MUST include:

* `artifacts/cli/help/hdctl_help.txt`

* `artifacts/cli/help/showcompat_help.txt`

* `artifacts/cli/help/reject_nonjson.txt`

* `artifacts/cli/install/entrypoints.txt`

* `artifacts/cli/install/installability_summary.json`

* `artifacts/cli/summary.json`

Path-proofs (normative). Each artifact above MUST have a co-located `.path_proof.txt` transcript and MUST be listed in the Human Index and mirrored 1:1 in the Machine Mirror in the same PR as any byte change.

Installability coherence (normative). `artifacts/cli/install/entrypoints.txt` and `artifacts/cli/install/installability_summary.json` MUST remain single-sourced and internally coherent. When they report console-entrypoint proof, both artifacts MUST agree on whether the console entrypoint is available and, when available, on the concrete console-entrypoint path used for the proof.

Conformance summary (normative). `artifacts/cli/summary.json` MUST preserve conjunction CLI conformance sections for:

* installability

* `sampler_semantics`

The summary MUST continue to capture deterministic CLI parity facts required elsewhere in this guide and MUST be regenerated, not hand-edited.

## **37.5 Required captures — Reader success catalog & A7 proofs**

Catalog:

* docs/ENDPOINTS\_CATALOG.json

* docs/ENDPOINTS\_CATALOG.json.sha256

Env-gate proof:

* artifacts/proofs/endpoints\_env\_gate\_proof.log — proves non-prod entries are unreachable in prod.

Success route proofs:

* artifacts/proofs/success\_get.txt — GET 200 proof.  
* artifacts/proofs/success\_head.txt — HEAD 200 parity proof.  
* artifacts/proofs/success\_304.txt — 304 omission proof (omits Content-Type and Content-Length).  
* artifacts/proofs/success\_writers\_errors.txt — writers/errors posture proof.  
* artifacts/proofs/success\_encoding\_invariance.txt — encoding-invariance proof.

## **37.6 Serializer / emitter guards**

Serializer and emitter guards are the mechanical enforcement layer for CLI serializer coupling (see §4 and §18). They prove that:

* public CLI flows do not use ad-hoc JSON serializers, and

* governed CLI handlers call the allow-listed presenter/emitter symbols.

### **37.6.1 Guard tools (closed-rails, deterministic)**

Mechanics defines two canonical CLI guard tools:

* tools/cli/serializer\_grep\_guard.py

  * AST-based grep guard over the governed CLI scope (default roots under engine/cli).

  * Detects imports of the json module and call-sites that resolve to json.dumps or json.dump (including alias imports).

  * Renders a deterministic report with:

    * a single scope line describing the scanned roots

    * a summary line of the form “summary: PASS” or “summary: FAIL” followed by sorted violation lines when present

  * The report contains no timestamps, environment echoes, or non-deterministic content.

* tools/cli/emitter\_symbol\_proof.py

  * AST-based emitter proof over the CLI module (engine/cli/main.py).

  * Tracks call-sites in the governed handlers (showcompat, aux\_preview, bg\_resolve) and records which allow-listed emitter symbols they invoke.

  * Emits deterministic lines of the form “handler:function:emitters” plus a summary line indicating PASS or FAIL for the non-optional handlers.

Both guard tools:

* import and call ensure\_determinism\_env from engine/runtime/determinism\_env.py at startup

* require the determinism pins and closed rails to be satisfied (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0)

* fail closed (non-zero exit) if the pins are not met

CI must call these tools only under the closed-rails determinism posture described in §1.2 and §6.2; check\_env\_pins and related jobs enforce the pins before running the guards.

### **37.6.2 Guard artifacts (canonical paths and roles)**

The canonical guard artifacts and their roles are:

* artifacts/cli/guards/serializer\_grep\_guard.log

  * Role: log.

  * Contains the serializer grep guard report (scope line, summary line, and any sorted violation lines).

  * A PASS report demonstrates that the governed CLI scope has no direct json.dumps or json.dump usage and that public JSON flows pass through the canonical emitter.

* artifacts/cli/guards/emitter\_symbol\_proof.txt

  * Role: snapshot.

  * Contains the emitter symbol proof for the governed CLI handlers.

  * For showcompat and bg\_resolve, the proof must show at least one allow-listed emitter symbol (for example, emitter.emit\_public or emit\_reader\_public\_envelope) and must mark the summary as PASS.

  * aux-preview is treated as an optional emitter handler: when it has no canonical emitter, it is rendered as a handler line with a “none” emitter listing and is explicitly exempt in the PASS/FAIL decision, so the absence of an emitter for aux-preview does not cause the guard to fail, while still keeping the handler visible in the proof.

These artifacts are the paths of record for:

* Phase I serializer work

* EPIC017 and EPIC018 CLI serializer acceptance

* evidence indexing for serializer/emitter guards

The Evidence Index and Machine Mirror must use these paths as discovered\_physical\_path for the corresponding records; any other locations are copies only.

### **37.6.3 Indexing, mirror, and secondary locations**

Indexing and mirror discipline for guard artifacts follow §1.3 and §37.4:

* List guard artifacts by title and path in Appendix D: Evidence Index.

* Mirror them 1:1 in artifacts/evidence\_index.jsonl (canonical JSONL; UTF-8, ASCII-sorted keys, compact, one LF; unknown keys rejected; exact field order pinned in §1.3).

* Each mirror record includes a proof\_anchor pointing at a co-located path\_proof transcript for the guard artifact.

For backward compatibility:

* Implementations may also write copies of the guard artifacts under audit/gates/guards/\*\* for internal audit workflows.

* These audit/gates/guards/\*\* paths are secondary only and are not required for mechanics-level acceptance.

* Future PF documents and epic records that reference CLI serializer/emitter guards should use the artifacts/cli/guards/\*\* paths as canonical and treat audit/gates/guards/\*\* as historical or auxiliary.

### **37.6.4 Live QA runs under open rails (informative)**

Status (informative, mechanics-aware). The canonical pass condition for CLI serializer/emitter guards is defined under closed determinism rails in CI and other CLOSED-rails environments (see §1.2, §6.2, and §37.6.1). In deliberately open-rails Live QA environments (for example, PO-run Codespaces sessions used for hands-on product checks), Mechanics treats guard behavior differently:

Env-mismatch failures are expected. When the determinism pins required by ensure\_determinism\_env are not satisfied (for example, SAFE\_MODE or ALLOW\_NETWORK differ from the closed-rails CI posture), the guard tools are expected to:

* refuse to run in “PASS” mode

* exit non-zero with logs that clearly indicate an environment mismatch rather than a serializer/emitter wiring error

Open-rails Live QA is env-enforcement only. Running the guards in an open-rails Live QA environment is allowed as an env-enforcement check:

* A non-zero exit due solely to determinism env mismatch confirms that the guards are enforcing the closed-rails policy correctly.

* Such runs do not contribute to the canonical guard acceptance condition and must not be interpreted as evidence of broken CLI serializer or emitter wiring.

Canonical acceptance remains CLOSED-rails. The authoritative acceptance for CLI serializer/emitter guard tokens remains:

* CI and other CLOSED-rails jobs that run the guard tools under the determinism pins described in §1.2 and §6.2

* guard artifacts and mirror records produced in that posture, as described in §17.8, §18.5, and §37.6.2–§37.6.3

Mechanics records this distinction so that PF-Canon and QA plans can treat open-rails guard runs as informational (env-pin enforcement) while continuing to rely on CLOSED-rails CI runs for normative D-stage/guard acceptance. PF14 does not define new tokens here; token semantics and QA expectations for guard runs remain single-homed in HDE-Governance, Glow QA Guide, HDE-Build Checklist, and HDE Phased Epics by title.

## **37.7 CLI parity & determinism (public bytes)**

AB ↔ BA goldens:

* artifacts/cli/ab.json

* artifacts/cli/ba.json — LF-terminated canonical JSON; BA must be byte-identical to AB.

Parity summary:

* artifacts/cli/summary.json — canonical JSON with: attempted commands, sha256 of AB/BA, ab\_ba\_equal: true.

Two-run marker:

* artifacts/cards/a3/IDENTITY\_OK.txt

Canonical compare:

* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

Canonical surface (normative). Canonical JSON compare evidence MUST bind to this canonical path as the canonical acceptance surface for canonical JSON gate evidence.

Error parity (Reader↔CLI; stored artifacts; deterministic roster):

* parity/errors\_reader\_cli.invalid\_json.http.json

* parity/errors\_reader\_cli.invalid\_json.cli.txt

* parity/errors\_reader\_cli.invalid\_viewer\_prefs.http.json

* parity/errors\_reader\_cli.invalid\_viewer\_prefs.cli.txt

* parity/errors\_reader\_cli.db\_unavailable.http.json

* parity/errors\_reader\_cli.db\_unavailable.cli.txt

* parity/errors\_reader\_cli.vendor\_attempt\_closed\_rails.http.json

* parity/errors\_reader\_cli.vendor\_attempt\_closed\_rails.cli.txt

* errors/schema\_check/error\_envelope\_db\_unavailable.log

* errors/schema\_check/error\_envelope\_vendor\_attempt\_closed\_rails.log

* errors/token\_map/token\_map.json

Showcompat stdout capture (closed rails; deterministic fixture):

* artifacts/cli/showcompat/stdout.json

* artifacts/cli/showcompat/stdout.json.sha256

* artifacts/cli/showcompat/args.json

* (Compatibility-only alias; when required for backward compatibility) artifacts/cli/showcompat/stdout.sha256

Generation tool (normative). The showcompat stdout capture artifacts above MUST be generated (not hand-edited). Canonical entrypoint: `python tools/cli/generate_showcompat_artifacts.py`. The generator MUST enforce the stdout byte constraints in §16.2 and MUST update checksum sidecars from the exact emitted stdout.json bytes.

stdout.json.sha256 is the canonical checksum sidecar name (JSON-filename-qualified). If the alias stdout.sha256 is produced, it MUST be mechanically derived from the exact bytes of stdout.json, and evidence indexing MUST continue to reference stdout.json.sha256 as the canonical checksum artifact.

These showcompat capture artifacts are deterministic fixtures used to prove stdout canonical bytes (single trailing LF, stderr empty on success) and to support acceptance artifact binding hygiene. They are not release identity proofs; release identity remains governed by the pack manifest and the /internal/version evidence surfaces.

### **37.7.1 Conjunction CLI governed artifacts**

Conjunction CLI artifacts (required). When conjunction-mode CLI evidence is captured, the governed artifact family includes:

* `artifacts/audit/cli/pair.json`

* `artifacts/audit/cli/pair_ba.json`

* `artifacts/audit/cli/showcompat_ab.json`

* `artifacts/audit/cli/showcompat_ba.json`

* `artifacts/cli/abba_sidecar.json`

* `artifacts/cli/out.json`

* `artifacts/cli/out_ba.json`

Path-proofs (normative). Each artifact above MUST have a co-located `.path_proof.txt` transcript and MUST be listed in the Human Evidence Index and mirrored 1:1 in `artifacts/evidence_index.jsonl` in the same PR as any byte change.

Canonical JSON gate coverage (normative). `tools/evidence/run_canonical_json_gate.py` MUST include the conjunction CLI artifact family above in its checked target set whenever those artifacts are part of the governed evidence surface for the PR. Any change to that checked target set MUST refresh the canonical JSON gate outputs under `audit/gates/json_gate/canonical/` and the corresponding `.path_proof.txt` transcripts in the same PR.

Bounded conjunction route-probe extension (normative). When the governed evidence surface for a PR or remediation includes the bounded conjunction JSON surface inventory, `tools/evidence/run_canonical_json_gate.py` MUST extend the checked target set to the bounded conjunction HTTP surface family `/reader`, `/dev/writer/conjunction`, `/dev/reader/conjunction`, `/dev/sampler/conjunction`, and `/internal/dev/sampler`, in addition to the conjunction CLI artifact family above.

Expected-status posture (normative). Route-probe targets in this family MUST validate expected HTTP status in addition to canonical-byte equality. For `/internal/dev/sampler`, the probe MUST send JSON bytes with `Content-Type: application/json; charset=utf-8`, MUST fail closed when actual and expected status differ, and MUST record a passing posture only when `expected_http_status` and `http_status` both equal `200`.

Same-change regeneration (normative). Any change to the bounded conjunction checked target set or to the expected-status logic MUST rerun the canonical JSON gate and refresh the authoritative outputs under `audit/gates/json_gate/canonical/`, the compatibility-only legacy family under `audit/gates/canonical_json/` when emitted, the Human Index and Machine Mirror companions, and the corresponding `.path_proof.txt` transcripts in the same PR.

Validation set (required when this bounded route-probe family changes). Refreshing this family MUST rerun and pass:

* `python tools/evidence/run_canonical_json_gate.py`  
* `python -m pytest -q tests/http/test_dev_conjunction_http.py`  
* `python -m pytest -q tests/http/test_endpoint_catalog.py`  
* `python -m pytest -q tests/adapter/test_dev_sampler_http.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python tools/evidence/check_lf_endings.py`  
* `python ci/checks/check_mirror_schema.sh`

EPIC024 showcompat artifacts capture (D03) fixed outputs (records-only):

* `python tools/evidence/run_showcompat_artifacts.py` (command entrypoint)

* artifacts/showcompat/epic024/showcompat\_manifest.json

* artifacts/showcompat/epic024/showcompat\_manifest.json.path\_proof.txt

* artifacts/showcompat/epic024/showcompat\_symbols.json

* artifacts/showcompat/epic024/showcompat\_symbols.json.path\_proof.txt

* audit/qa/hde-epic024/checks/D03\_showcompat\_artifacts/primary.log

## **37.8 CLI Admin Preview (narrative)**

* artifacts/cli/narrative/stdout.txt — LF-terminated text (no ANSI).

* artifacts/cli/narrative/sidecar.json — ids-only canonical JSON (no prose).

Both must be indexed in the Human Index and Machine Mirror in the same PR.

## **37.9 Canonical JSON checks**

Canonical family root (normative):

* audit/gates/json\_gate/canonical/

Policy check:

* audit/gates/json\_gate/canonical/json\_gate\_check\_log.ndjson

Canonical compare:

* audit/gates/json\_gate/canonical/json\_gate\_compare\_log.ndjson

Structured record:

* audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json

Path proofs (normative). Each artifact above MUST have a co-located .path\_proof.txt transcript and MUST be indexed/mirrored under the Evidence Index \+ Machine Mirror.

No alternate filenames (normative). Future plans MUST validate these canonical surfaces and MUST NOT invent wrapper bundles or alternate filenames for canonical JSON gate evidence.

Legacy compatibility surfaces (non-authoritative). Until the migration away from audit/gates/canonical\_json/ is complete, the following compatibility-only legacy artifacts MAY continue to be emitted from the same canonical JSON gate run:

* audit/gates/canonical\_json/canonical\_json.gate.json

* audit/gates/canonical\_json/json\_canon\_compare.log

* audit/gates/canonical\_json/json\_canonical\_check.log

If these legacy artifacts are emitted, each MUST have a co-located .path\_proof.txt transcript and MAY remain indexed/mirrored as compatibility-only outputs during migration. Plans, acceptance binding, and close-pack checks MUST continue to bind to audit/gates/json\_gate/canonical/ as the canonical surface, and the legacy family MUST NOT be treated as permission to invent additional legacy filenames

Legacy same-run coherence (normative). If any artifact under `audit/gates/canonical_json/` is emitted or rewritten in a canonical JSON gate run, its co-located `.path_proof.txt` companion MUST be regenerated in that same run and MUST carry current `mtime_utc` and current `produced_at_utc`.

Broader same-change requirement (normative). When one canonical JSON gate run changes both the authoritative `audit/gates/json_gate/canonical/` family and the compatibility-only legacy `audit/gates/canonical_json/` family, the governed evidence family is not complete until both families are current, indexed or mirrored as applicable, and path-proven in the same PR.

### 37.9.1 Arrays-as-sets check (EPIC024)

Purpose (normative). Record a deterministic proof that set-like arrays are treated as sets (deduplicated and order-normalized) per the canonical JSON rules.

Report artifact (records-only; canonical path):

* artifacts/canonical/arrays\_as\_sets\_report.log

QA primary log (Live QA; EPIC024):

* audit/qa/hde-epic024/checks/D05\_arrays\_as\_sets/primary.log

Path proofs (normative). The report artifact above MUST have a co-located .path\_proof.txt transcript and MUST be indexed/mirrored under the Evidence Index \+ Machine Mirror.

Note (runner is not pinned). This check may be executed via the repository test harness (for example, python \-m pytest tests/compare/test\_arrays\_as\_sets.py). PF14 pins the evidence surfaces, not the runner command.

## **37.10 Bands edges (inclusive-high)**

Edges snapshot:

* audit/gates/bands/edges.snapshot.json

Edges diff:

* audit/gates/bands/edges.diff.json

## **37.11 Pack identity & provenance**

Evidence copy of manifest:

* artifacts/math/freeze\_pack\_manifest.json (Evidence-copy semantics are locked: artifacts/math/freeze\_pack\_manifest.json is a byte-identical evidence copy of the canonical bytes of catalog/manifest.json. It is not a derived manifest or alternate contract. See §27.3 for the normative semantics.)

Recomputed release\_id:

* artifacts/math/release\_id.txt

Recompute log:

* artifacts/math/release\_id\_recompute.log

Release-id evidence path canonicalization (normative). Release-id evidence is canonical at:

* artifacts/math/release\_id.txt

* artifacts/math/release\_id\_recompute.log

Any references to audit/gates/release/release\_id.txt (or similar audit/gates/release/\*\* paths) are deprecated and MUST NOT be used for evidence indexing or close-pack checks. If a transitional copy is required, it MUST be mechanically generated from the canonical artifacts/math/\*\* source (no manual editing), and indexing MUST reference the canonical artifacts/math/\*\* paths.

Checksums audit:

* artifacts/math/checksums\_audit.log

(Optional) SBOM (CycloneDX) \+ hash:

* sbom/cyclonedx.json

* sbom/cyclonedx.json.sha256

## **37.12 Identity & Math**

Service identity (admin JSON):

* artifacts/identity/service\_identity.json

Emitter SHA-256:

* artifacts/identity/emitter\_sha256.txt

## **37.13 Internal-ops /internal/version snapshots**

GET headers:

* artifacts/ops/internal\_version/headers\_get.txt

HEAD headers:

* artifacts/ops/internal\_version/headers\_head.txt

Conditional headers:

* artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt

* artifacts/ops/internal\_version/headers\_cond\_if\_modified\_since.txt

Body & hash:

* artifacts/ops/internal\_version/body\_get.json

* artifacts/ops/internal\_version/body\_get.sha256

Two-run identity & coupling proof:

* artifacts/ops/internal\_version/two\_run\_identity.log

Request-chain manifest:

* artifacts/ops/internal\_version/request\_chain\_manifest.jso

Filename aliases (compatibility-only; no ad-hoc variants). If an epic’s acceptance bindings require legacy names for the conditional header snapshot files (specifically, artifacts/ops/internal\_version/cond\_if\_none\_match\_headers.txt and/or artifacts/ops/internal\_version/cond\_if\_modified\_since\_headers.txt), the Live QA harness MAY emit explicitly defined alias copies as compatibility-only artifacts. Any such alias MUST be mechanically generated from the canonical files above (no manual edits), and evidence indexing MUST continue to reference the canonical filenames listed in this section. No other filename variants are permitted beyond the canonical set plus any explicitly defined aliases governed elsewhere (titles-only).

## **37.14 Database proofs & ops pins**

DDL snapshot:

* artifacts/db/ddl\_fingerprint.json

Grants/constraints checks:

* artifacts/db/grants.txt

* artifacts/db/check\_constraints.txt

Schema check:

* artifacts/db/check\_schema.txt

Partition plan:

* artifacts/db/partition\_plan.txt

Start command capture:

* artifacts/proofs/start\_command\_capture.txt

Environment pins:

* audit/gates/determinism/env\_pins.log

* audit/gates/determinism/env\_pins.log.path\_proof.txt

DB bridge and provider parity:

* `artifacts/db_bridge/adapter_selection.snapshot.json` — deterministic adapter-selection snapshot for the DB bridge parity family, secret-free and DSN-free.  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt` — co-located path-proof transcript for the adapter-selection snapshot.  
* `artifacts/db_bridge/provider_parity.proof.json` — provider parity and bridge capability proof, including deterministic harness cases and closed-rails live-unavailable posture.  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt` — co-located path-proof transcript for provider parity proof.  
* `artifacts/db_bridge/caps.snapshot.json.path_proof.txt` — co-located path-proof transcript for bridge capability snapshot evidence when refreshed by the governed family.  
* `artifacts/runtime/env_connectivity.snapshot.json` — runtime env connectivity snapshot proving secret-free dev fallback through `DBAccess`.  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt` — co-located path-proof transcript for env connectivity proof.  
* `artifacts/runtime/env_connectivity.nondev_failure.json` — canonical JSON non-dev total-failure proof for stage posture, no proactive probes, numeric-free public posture, presence-only secret posture, real adapter selection order, and typed `BridgeUnavailable` / `missing_bridge_url`.  
* `artifacts/runtime/env_connectivity.nondev_failure.json.path_proof.txt` — co-located path-proof transcript for non-dev total-failure proof.  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json` — OPS provider-parity closure decision artifact, records-only and non-claiming for QA PASS, PF09 status movement, epic closure, and DB proof-label acceptance-token satisfaction.  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt` — path-proof transcript for the OPS provider-parity closure decision when bound by the governed evidence family.  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity.proof.json` — OPS provider parity proof with active corpus rows and row-level parity values.  
* `audit/ops/hde-epic032/db-provider-parity/bridge_consistency_result.txt` — OPS bridge consistency result, including command, exit code, result, active corpus, and row parity summary.  
* `audit/ops/hde-epic032/db-provider-parity/parity_scope_rationale.txt` — OPS parity scope rationale and closure basis.  
* `audit/ops/hde-epic032/db-provider-parity/non_claims.txt` — OPS non-claims for QA PASS, PF09 status movement, epic closure, and acceptance-token satisfaction.  
* `audit/ops/hde-epic032/db-provider-parity/ops01_final_report.txt` — human-readable OPS final evidence summary.  
* `audit/ops/hde-epic032/db-provider-parity/created_files_sha256.txt` — checksum ledger for produced OPS evidence files.  
* `audit/ops/hde-epic032/db-provider-parity/commands.txt` — command transcript for OPS provider-parity capture.  
* `audit/ops/hde-epic032/db-provider-parity/stdout.log` — OPS stdout capture.  
* `audit/ops/hde-epic032/db-provider-parity/stderr.log` — OPS stderr capture.  
* `audit/ops/hde-epic032/db-provider-parity/exit_codes.txt` — OPS exit-code capture.  
* `audit/ops/hde-epic032/db-provider-parity/redacted_env_presence.txt` — presence-only environment posture capture.  
* `audit/ops/hde-epic032/db-provider-parity/adapter_selection.snapshot.json` — OPS adapter-selection snapshot for provider availability and selection posture.  
* `audit/ops/hde-epic032/db-provider-parity/env_connectivity.snapshot.json` — OPS environment connectivity and selection-order snapshot.  
* `docs/evidence/INDEX.json` — Human Evidence Index rows for the DB bridge, provider parity, OPS closure, and PR-04 non-dev failure families.  
* `docs/evidence/INDEX.sha256` — Human Evidence Index hash sentinel refreshed with the Human Evidence Index.  
* `docs/evidence/INDEX.json.path_proof.txt` — co-located path-proof transcript for the Human Evidence Index.  
* `docs/evidence/INDEX.sha256.path_proof.txt` — co-located path-proof transcript for the Human Evidence Index hash sentinel.  
* `artifacts/evidence_index.jsonl` — Machine Evidence Mirror rows for the DB bridge, provider parity, OPS closure, and PR-04 non-dev failure families.  
* `artifacts/evidence_index.jsonl.sha256` — Machine Evidence Mirror hash sentinel refreshed with the Machine Evidence Mirror.  
* `artifacts/evidence_index.jsonl.path_proof.txt` — co-located path-proof transcript for the Machine Evidence Mirror.  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` — co-located path-proof transcript for the Machine Evidence Mirror hash sentinel.  
* `audit/gates/topology/orientation_demo.txt` — topology orientation evidence refreshed when the governed evidence skeleton changes.  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — co-located path-proof transcript for topology orientation evidence.

Each listed DB bridge, provider parity, PR-04 non-dev failure, Human Index, Machine Mirror, and topology artifact or sentinel that is path-proofed by the governed evidence family MUST be paired with its matching co-located path-proof transcript when indexed. OPS-01 audit packet support files are recorded as OPS evidence and checksum-ledger items unless an owning evidence family indexes a path-proof companion.

HDAPI v2 vendor contract inventory:

* `artifacts/vendor/hdapi_v2/source_inventory.json` — canonical JSON source inventory for public same-origin HumanDesignAPI documentation sources, closed-rails source-cache mode, and source classification.  
* `artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt` — co-located path-proof transcript for the source inventory JSON.  
* `artifacts/vendor/hdapi_v2/source_inventory.md` — human-readable source inventory summary, including documentation-discovery-only classification for `llms.txt`, `llms-full.txt`, and AI or LLM-oriented vendor documentation.  
* `artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt` — co-located path-proof transcript for the source inventory summary.  
* `artifacts/vendor/hdapi_v2/openapi_validation.log` — validation log for `v2-routes.yaml`, `v1-routes.yaml`, route-spec gate status, and quarantined suspect OpenAPI posture.  
* `artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt` — co-located path-proof transcript for the OpenAPI validation log.  
* `artifacts/vendor/hdapi_v2/known_anomalies.md` — anomaly ledger for quarantined or suspect source artifacts.  
* `artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt` — co-located path-proof transcript for the anomaly ledger.  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv` — endpoint reference for required v2 and legacy v1 route families, auth model, geocode-key requirement, request content type, request fields, success envelope, error codes, tier, and source spec.  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt` — co-located path-proof transcript for the endpoint reference.  
* `artifacts/vendor/hdapi_v2/contract_map.json` — canonical JSON contract map binding validated vendor sources to required v2 and legacy v1 route families.  
* `artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt` — co-located path-proof transcript for the contract map.  
* `artifacts/vendor/hdapi_v2/source_cache/api-reference.openapi.json` — suspect OpenAPI source-cache input, quarantined unless validation proves HumanDesignAPI ownership.  
* `artifacts/vendor/hdapi_v2/source_cache/authentication.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/coordinates_guide.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt` — bounded endpoint-tier excerpt used for tier parsing.  
* `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body` — cached `llms.txt` source body.  
* `artifacts/vendor/hdapi_v2/source_cache/migration_v1_to_v2.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/rate_limiting.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/response_format.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/robots_preflight.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json` — source metadata for source-cache replay.  
* `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml` — legacy v1 route specification input.  
* `artifacts/vendor/hdapi_v2/source_cache/v1_overview.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml` — v2 route specification input.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_coordinates_chart_page.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_full_chart_page.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_overview.body` — cached public documentation source body.  
* `artifacts/vendor/hdapi_v2/source_cache/v2_simple_chart_page.body` — cached public documentation source body.  
* `docs/acceptance_map_epic033.json` — acceptance map for HDE-EPIC033 PR-01 inventory-only scope and downstream non-claims.  
* `docs/acceptance_map_epic033.json.path_proof.txt` — co-located path-proof transcript for the acceptance map.  
* `audit/qa/hde-epic033/token_evidence_matrix.md` — token evidence matrix using existing registry-valid baseline tokens only and no vendor-v2-specific token mint.  
* `audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt` — co-located path-proof transcript for the token evidence matrix.  
* `audit/qa/hde-epic033/acceptance_map_viability.log` — viability log recording no vendor-v2-specific tokens, no runtime v2 conformance claim, no public Reader surface change, and no AI scope.  
* `audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt` — co-located path-proof transcript for the viability log.  
* `audit/docdeltas/hde-epic033_doc_deltas.md` — Doc-Delta baseline for PR-01 contract-inventory evidence binding.  
* `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt` — co-located path-proof transcript for the Doc-Delta baseline.  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md` — QA metadata Doc-Delta baseline for PR-01 contract-inventory evidence binding.  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt` — co-located path-proof transcript for the QA metadata Doc-Delta baseline.  
* `docs/evidence/INDEX.json` — Human Evidence Index rows for the HDAPI v2 contract-inventory evidence family.  
* `docs/evidence/INDEX.sha256` — Human Evidence Index hash sentinel refreshed with the Human Evidence Index.  
* `docs/evidence/INDEX.json.path_proof.txt` — co-located path-proof transcript for the Human Evidence Index.  
* `docs/evidence/INDEX.sha256.path_proof.txt` — co-located path-proof transcript for the Human Evidence Index hash sentinel.  
* `artifacts/evidence_index.jsonl` — Machine Evidence Mirror rows for the HDAPI v2 contract-inventory evidence family.  
* `artifacts/evidence_index.jsonl.sha256` — Machine Evidence Mirror hash sentinel refreshed with the Machine Evidence Mirror.  
* `artifacts/evidence_index.jsonl.path_proof.txt` — co-located path-proof transcript for the Machine Evidence Mirror.  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt` — co-located path-proof transcript for the Machine Evidence Mirror hash sentinel.  
* `audit/gates/topology/orientation_demo.txt` — topology orientation evidence refreshed when the governed evidence skeleton changes.  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt` — co-located path-proof transcript for topology orientation evidence.

Each listed HDAPI v2 contract-inventory primary artifact, path-proof transcript, Human Index artifact, Machine Mirror artifact, hash sentinel, and topology artifact that is path-proofed by the governed evidence family MUST be paired with its matching co-located path-proof transcript when indexed. Source-cache input files are recorded as governed source inputs for the contract-inventory family when bound by source inventory, source metadata, index, mirror, and path-proof discipline.

## **37.15 BodyGraph proofs**

Source selection snapshot:

* artifacts/bodygraph/source\_selection.snapshot.json

Source invariance:

* artifacts/bodygraph/source\_invariance/ab.json

* artifacts/bodygraph/source\_invariance/ba.json

* artifacts/bodygraph/source\_invariance/summary.json

Refresh policy:

* artifacts/bodygraph/refresh\_policy.snapshot.json

Metrics:

* artifacts/bodygraph/metrics.snapshot.json

Sanitized logs sample:

* artifacts/bodygraph/keys\_only.logs.sample

Release bindings:

* artifacts/bodygraph/release\_bindings.json

## **37.16 Narratives**

Narratives coverage (router):

* audit/gates/narratives/keys\_10x4.table.json — router coverage snapshot for 10 categories × 4 bands, canonical JSON, keys-only/no-prose, including `missing_narrative_key` cases for governed category, band, and perspective cases.  
* artifacts/narratives/router/parity\_abba.log — AB↔BA and two-run identity log for router outputs, keys-only/no-prose.  
* artifacts/narratives/router/cli\_http\_parity.log — CLI/HTTP parity compare for router responses where parity is defined, using byte-identical canonical JSON.  
* docs/evidence/INDEX.json — Human Evidence Index, titles and paths only, refreshed for the router evidence family when artifacts change.  
* docs/evidence/INDEX.sha256 — Human Evidence Index hash sentinel, refreshed with the Human Evidence Index.  
* artifacts/evidence\_index.jsonl — Machine Evidence Mirror rows for the router evidence family, records-only and regenerated with corrected source posture when token posture changes.  
* artifacts/evidence\_index.jsonl.sha256 — Machine Evidence Mirror hash sentinel, refreshed with the Machine Evidence Mirror.

Each listed governed artifact and sentinel MUST be paired with its matching co-located path-proof transcript when indexed.

Narratives registry and pack identity (registry):

* audit/gates/narratives/registry.diff.json — compact canonical registry diff evidence, keys-only/no-prose, including truthful no-prior-baseline posture where applicable.  
* audit/gates/narratives/registry.diff.json.path\_proof.txt — co-located path-proof transcript for registry diff evidence.  
* audit/gates/narratives/pack\_identity.txt — pack identity evidence from canonical manifest bytes, including manifest identity, canonical size, two-run identity values, and two-run match.  
* audit/gates/narratives/pack\_identity.txt.path\_proof.txt — co-located path-proof transcript for pack identity evidence.  
* audit/docdeltas/hde-epic032\_doc\_deltas.md — Doc-Delta posture artifact for narrative registry diffing, Doc-Delta binding, pack identity, and evidence indexing.  
* audit/docdeltas/hde-epic032\_doc\_deltas.md.path\_proof.txt — co-located path-proof transcript for the Doc-Delta posture artifact.  
* audit/gates/topology/orientation\_demo.txt — topology orientation evidence refreshed when the governed evidence skeleton expands or shrinks.  
* audit/gates/topology/orientation\_demo.txt.path\_proof.txt — co-located path-proof transcript for topology orientation evidence.  
* docs/evidence/INDEX.json — Human Evidence Index rows for the registry and pack identity family.  
* docs/evidence/INDEX.sha256 — Human Evidence Index hash sentinel refreshed with the Human Evidence Index.  
* artifacts/evidence\_index.jsonl — Machine Evidence Mirror rows for the registry and pack identity family.  
* artifacts/evidence\_index.jsonl.sha256 — Machine Evidence Mirror hash sentinel refreshed with the Machine Evidence Mirror.

Each listed registry-family artifact and sentinel MUST be paired with its matching co-located path-proof transcript when indexed.

Aux (EPIC-010 scope; headers-only):

* tests/transport/headers/aux\_text\_200.snap

* tests/transport/headers/aux\_suppression\_200.snap

(No Aux HEAD/304 captures in EPIC-010; A7 remains Catalog-only.)

## **37.17 Architecture capture**

Snapshot root:

* audit/gates/arch/*arch/\<epic\>*\<ts\>/\<PATH\>

## **37.18 Index & synchronization**

Human Index:

* docs/evidence/INDEX.json — titles/paths only.

Machine Mirror:

* artifacts/evidence\_index.jsonl — records-only JSONL.

Evidence index snapshot (gate-family; canonical):

* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json

* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json.path\_proof.txt

### **37.18.1 EPIC027 close-pack and same-run ledger refresh**

Canonical close-pack generator (required). `python tools/qa/generate_epic027_close_pack.py` is the EPIC027 close-pack generator for the conjunction global-discipline slice.

Required close-pack artifacts. The generator MUST emit and refresh, at minimum:

* `docs/acceptance_map_epic027.json`

* `audit/qa/hde-epic027/token_evidence_matrix.md`

* `audit/qa/hde-epic027/acceptance_map_viability.log`

* `audit/EPIC-027_close_report.md`

* `audit/EPIC-027_MANIFEST.json`

Close-report truthfulness (required). The close-pack generator MUST NOT claim Human Index, Machine Mirror, checksum, path-proof, or same-run gate refresh unless that workflow was actually executed in the same run.

Same-run governed workflow (required). When the EPIC027 close-pack family changes, the bound close-pack workflow MUST execute and persist the same-run outputs for:

* `python tools/evidence/update_evidence_index.py`

* `python tools/evidence/update_evidence_index.py --check`

* `python tools/evidence/orientation_demo.py`

* `python tools/evidence/orientation_demo.py --check`

* `python tools/evidence/validate_evidence_paths.py`

* `python tools/evidence/check_lf_endings.py`

* `python ci/checks/check_mirror_schema.sh`

* the acceptance-map viability run that writes `audit/qa/hde-epic027/acceptance_map_viability.log`

Same-change ledger refresh (required). Any byte change in the EPIC027 close-pack family MUST refresh the Human Index, Machine Mirror, hash sentinels, and changed path-proof companions in the same PR.

Chronology posture (required). Changed close-pack, index, mirror, topology, checksum, and sibling path-proof artifacts in this family MUST carry current chronology after regeneration. Stale chronology is a merge-blocking integrity failure.

QA gate-log capture (required). The EPIC027 close-pack workflow MUST persist same-run QA gate logs for the executed close-pack and evidence-discipline checks. Artifact existence alone is not sufficient when the close report claims the gates ran.

Generator (normative). Generate with: python tools/evidence/generate\_evidence\_index\_snapshot.py. Plans and QA docs MUST NOT reference run\_evidence\_index\_snapshot.py for this gate-family.

Non-canonical epic-local variant (normative). audit/qa/hde-epic\<NNN\>/evidence\_index\_snapshot.json is non-authoritative and MUST NOT be required by future plans as a closure deliverable.

### **37.18.2 EPIC028 close-pack baseline and OPS closeout evidence**

EPIC028 close-pack baseline artifacts observed (records-only):

* `docs/acceptance_map_epic028.json`  
* `audit/qa/hde-epic028/token_evidence_matrix.md`  
* `audit/qa/hde-epic028/acceptance_map_viability.log`  
* `audit/qa/hde-epic028/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic028/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/qa/hde-epic028/checks/po-010/final_summary.txt`  
* `audit/EPIC-028_close_report.md`  
* `audit/EPIC-028_MANIFEST.json`  
* `audit/EPIC-028_close_report.md.path_proof.txt`  
* `audit/EPIC-028_MANIFEST.json.path_proof.txt`

Manifest-binding posture (records-only). The EPIC028 close-pack baseline binds to the existing EPIC028 acceptance and QA evidence family above through `key_outputs` and MUST NOT be treated as a replacement proof surface.

OPS-01 packaging and evidence execution bundle observed (records-only):

* `audit/ops/hde-epic028/ops-01/commands.txt`  
* `audit/ops/hde-epic028/ops-01/stdout.log`  
* `audit/ops/hde-epic028/ops-01/stderr.log`  
* `audit/ops/hde-epic028/ops-01/exit_codes.txt`  
* `audit/ops/hde-epic028/ops-01/created_files_sha256.txt`

OPS-01 posture (records-only). The execution bundle records packaging and evidence scope only, no reopened implementation scope, no QA verdict changes, and no merge provenance claim.

OPS-02 venue-provenance execution bundle observed (records-only):

* `audit/ops/hde-epic028/ops-02/commands.txt`  
* `audit/ops/hde-epic028/ops-02/repo_root.txt`  
* `audit/ops/hde-epic028/ops-02/repo_head.txt`  
* `audit/ops/hde-epic028/ops-02/python_version.txt`  
* `audit/ops/hde-epic028/ops-02/stdout.log`  
* `audit/ops/hde-epic028/ops-02/stderr.log`  
* `audit/ops/hde-epic028/ops-02/exit_codes.txt`  
* `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md`  
* `audit/ops/hde-epic028/ops-02/codespaces_harness_binding.md.path_proof.txt`

OPS-02 binding posture (records-only). The venue-provenance artifact binds to the rerun-produced EPIC028 governed QA artifact family under `audit/qa/hde-epic028/checks/po-010/`, with the primary bound artifact at `audit/qa/hde-epic028/checks/po-010/final_summary.txt`.

OPS-02 execution posture (records-only). The execution bundle records the final corrective command ledger as fully successful and captures repo identity plus presence-only Codespaces venue context.

### **37.18.3 EPIC029 close-pack baseline and OPS-01 dev-harness binding evidence**

EPIC029 close-pack baseline artifacts observed (records-only):

* `docs/acceptance_map_epic029.json`  
* `docs/acceptance_map_epic029.json.path_proof.txt`  
* `audit/qa/hde-epic029/token_evidence_matrix.md`  
* `audit/qa/hde-epic029/token_evidence_matrix.md.path_proof.txt`  
* `audit/qa/hde-epic029/acceptance_map_viability.log`  
* `audit/qa/hde-epic029/acceptance_map_viability.log.path_proof.txt`  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic029/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`  
* `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md.path_proof.txt`  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`  
* `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md.path_proof.txt`  
* `audit/EPIC-029_close_report.md`  
* `audit/EPIC-029_close_report.md.path_proof.txt`  
* `audit/EPIC-029_MANIFEST.json`  
* `audit/EPIC-029_MANIFEST.json.path_proof.txt`

Manifest-binding posture (records-only). The EPIC029 close-pack baseline binds the acceptance map, token-evidence matrix, viability log, QA step-manifest pair, dev-harness binding coverage artifact, and bounded conjunction inventory artifact as one governed closeout family and MUST NOT be treated as a replacement proof surface.

EPIC029 closeout QA logs observed (records-only):

* `audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log`  
* `audit/qa/hde-epic029/checks/po-precommit/primary.log`  
* `audit/qa/hde-epic029/checks/po-postcommit/primary.log`

EPIC029 closeout snapshot family observed (records-only):

* `audit/qa/hde-epic029/checks/po-008/primary.log`  
* `audit/qa/hde-epic029/checks/po-008/acceptance_map.snapshot.json`  
* `audit/qa/hde-epic029/checks/po-008/token_evidence_matrix.snapshot.md`  
* `audit/qa/hde-epic029/checks/po-008/acceptance_map_viability.snapshot.log`  
* `audit/qa/hde-epic029/checks/po-008/qa_step_logs_manifest.snapshot.json`  
* `audit/qa/hde-epic029/checks/po-008/close_report.snapshot.md`  
* `audit/qa/hde-epic029/checks/po-008/close_manifest.snapshot.json`  
* `audit/qa/hde-epic029/checks/po-008/po_epic_close_live_qa.snapshot.log`  
* `audit/qa/hde-epic029/checks/po-008/po_precommit.snapshot.log`  
* `audit/qa/hde-epic029/checks/po-008/po_postcommit.snapshot.log`

Closeout snapshot posture (records-only). checks/po-008 records a PASS final closeout snapshot family under `audit/qa/hde-epic029/checks/po-008/`, with `ready_for_close_binding` set true in the acceptance-map snapshot, the viability summary recorded as `COVERED=9 PLANNED=0 MISSING=0`, the three canonical QA log snapshots bound as token-support evidence for the closeout family, and the close\_report/close\_manifest snapshot pair kept on one bounded Conjunction acceptance surface without widening into a new public surface or writer-runtime redesign.

Closeout QA binding posture (records-only). The EPIC029 step-manifest pair records PASS for the three canonical closeout QA checks only when the three primary logs above exist at their governed paths, each primary log records `[exit_code] 0`, and the logs are bound into the close-pack family. File existence alone or a non-`MISSING` sentinel is insufficient for closeout completeness.

OPS-01 dev-harness binding bundle observed (records-only):

* `audit/ops/hde-epic029/ops-01/commands.txt`  
* `audit/ops/hde-epic029/ops-01/stdout.log`  
* `audit/ops/hde-epic029/ops-01/stderr.log`  
* `audit/ops/hde-epic029/ops-01/exit_codes.txt`  
* `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`  
* `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`  
* `audit/ops/hde-epic029/ops-01/binding_disposition.md`  
* `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

OPS-01 binding posture (records-only). The normalized bundle records the Codespaces dev-harness binding at `http://127.0.0.1:8000/internal/dev/sampler` closed by direct runtime validation. The same bundle records `local_dev` closed by binding-equivalence at the same published `DEV_SAMPLER_URL`, with explicit `Closure mode: binding-equivalence`, on the basis that the client access binding is identical to Codespaces for the same dev-only sampler harness.

Authoritative local-dev artifact posture (records-only). The normalized OPS-01 family MUST record that no separate local-dev runtime was executed in that evidence pass and MUST NOT preserve contradictory `not yet closed`, deferred, or equivalent posture anywhere in the same governed family.

OPS-02 blocker-classification validation bundle observed (records-only):

* `audit/ops/hde-epic029/ops-02/W-001_action_log_and_evidence_output_run2.md`  
* `audit/ops/hde-epic029/ops-02/W-001_classification_run2.md`  
* `audit/ops/hde-epic029/ops-02/commands_w001_run2.txt`  
* `audit/ops/hde-epic029/ops-02/exit_codes_w001_run2.txt`  
* `audit/ops/hde-epic029/ops-02/stdout_w001_run2.log`  
* `audit/ops/hde-epic029/ops-02/stderr_w001_run2.log`

OPS-02 classification posture (records-only). The read-only validation bundle records `HDE-CONJ009.1` as a mixed blocker because the bounded conjunction inventory and the current canonical JSON gate do not, by themselves, prove exhaustive all-surface HTTP emitter coverage. The same bundle records `HDE-CONJ008.1` as a governed approval or evidence blocker because writer-envelope behavior is already evidenced by tests and writer snapshots rather than by an open runtime defect.

OPS-02 execution posture (records-only). The bundle is read-only, captures inspection commands plus zero-exit read checks, uses repo facts only, and does not itself close PF09 rows or reopen implementation scope.

Generator and same-run workflow observed (records-only):

* `python tools/qa/generate_epic029_close_pack.py`  
* `python tools/evidence/update_evidence_index.py`  
* `python tools/evidence/update_evidence_index.py --check`  
* `python tools/evidence/orientation_demo.py`  
* `python tools/evidence/orientation_demo.py --check`  
* `python tools/evidence/validate_evidence_paths.py`  
* `python tools/evidence/check_lf_endings.py`  
* `python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`  
* `python -m pytest -q tests/qa/test_epic022_close_pack_ready.py`  
* `python -m json.tool audit/EPIC-029_MANIFEST.json > /dev/null`  
* `python -m json.tool docs/acceptance_map_epic029.json > /dev/null`

Observed W-002 reruns used closed rails and determinism pins: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

EPIC029 close-pack sequencing gate posture (records-only). The close-pack generator’s `ready_for_close_binding` gate is sequencing-only: it MUST require explicit PF09 row-closure proof markers for `HDE-CONJ009.1` and `HDE-CONJ008.1`, MUST require both `codespaces` and `local_dev` closed for `HDE-CONJ001.4`, and MUST keep the EPIC029 acceptance and close-pack outputs blocked or incomplete-planned under current evidence when those proofs are absent. The generator MUST NOT promote close-binding or token completion from generic readiness alone.

Same-change companion refreshes observed (records-only):

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `artifacts/evidence_index.jsonl`  
* `artifacts/evidence_index.jsonl.path_proof.txt`  
* `artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`

EPIC029 closeout posture (records-only). The close-pack family binds the governed QA and OPS evidence above under one authoritative OPS posture for `HDE-CONJ001.4`, rather than preserving parallel closed and not-yet-closed states.

Governed evidence-family posture (normative). Any governed evidence family that participates in acceptance binding MUST express one authoritative posture per claimed closure dimension. Mixed-state families are mechanically invalid: contradictory `closed`, `not yet closed`, deferred, partial, or equivalent postures for the same dimension MUST be normalized before acceptance binding or close-pack consolidation.

Documentation/evidence normalization posture (normative). When runtime facts are unchanged and only the closure interpretation changes, a documentation/evidence normalization pass MAY update the family without a new runtime rerun, provided the closure mode is explicit and every affected governed artifact, Index/Mirror entry, checksum companion, and path-proof is refreshed coherently in the same change.

EPIC030 close-pack baseline and OPS-03 evidence-packaging bundle observed (records-only).

EPIC030 close-pack and supporting closeout artifacts observed:

* audit/EPIC-030\_close\_report.md  
* audit/EPIC-030\_MANIFEST.json  
* audit/EPIC-030\_close\_report.md.path\_proof.txt  
* audit/EPIC-030\_MANIFEST.json.path\_proof.txt  
* audit/EPIC-030\_QA\_RCA.md  
* docs/acceptance\_map\_epic030.json  
* audit/qa/hde-epic030/token\_evidence\_matrix.md  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json  
* audit/docdeltas/hde-epic030\_doc\_deltas.md  
* audit/docdeltas/hde-epic030\_drain\_targets.md

OPS-03 evidence-packaging bundle observed:

* audit/ops/hde-epic030/ops-03/commands.txt  
* audit/ops/hde-epic030/ops-03/commands\_prev\_invalid.txt  
* audit/ops/hde-epic030/ops-03/stdout.log  
* audit/ops/hde-epic030/ops-03/stderr.log  
* audit/ops/hde-epic030/ops-03/exit\_codes.txt  
* audit/ops/hde-epic030/ops-03/final\_evidence\_inventory.md  
* audit/ops/hde-epic030/ops-03/final\_evidence\_inventory.md.path\_proof.txt  
* audit/ops/hde-epic030/ops-03/final\_validation.log  
* audit/ops/hde-epic030/ops-03/created\_files\_sha256.txt

OPS-03 packaging posture (records-only). The OPS-03 bundle is evidence packaging and close-pack surfacing only. It records closed deterministic rails, no QA reruns, no vendor calls, no implementation changes, no PF-Canon edits, no PF09.2 drain claims, and no new acceptance claims.

OPS-03 remediation posture (records-only). The R3 evidence remediates prior OPS-03 evidence blockers by replacing the invalid transcript with executable labeled heredoc command blocks, preserving the prior invalid transcript for audit, labeling stdout, stderr, and exit-code evidence by action, regenerating the three-column final inventory, regenerating its sibling path proof, and validating file existence, manifest bindings, close report text, path proofs, final inventory, and the OPS-03 evidence bundle.

Manifest and inventory posture (records-only). The EPIC030 close-pack manifest records key\_outputs as a named binding map for close-pack, QA, doc-delta, drain-target, and OPS-03 inventory/checksum outputs. The final inventory records 18 governed artifacts present and 0 missing. The checksum ledger records 12 files checksummed.

Drain posture (records-only). OPS-03 proves close-pack surfacing and drain-target recording. It does not by itself prove PF09.2 row status changes, PF09.2 drainage completion, QA rerun completion, new acceptance claims, or epic closure beyond the surfaced close-pack and OPS-03 evidence family.

Same-PR rule. Any addition, removal, or relocation in this registry must update both Index and Mirror in the same commit/PR.

CI enforces:

* Human↔machine 1:1 parity

* canonical JSONL

* unknown-key rejection

* presence and correctness of path-proofs

