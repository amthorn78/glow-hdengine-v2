# Glow HD Engine Architecture and Design

## State of Application Development

Got it. I’ve revised your doc with everything we’ve learned since the first audit—identity guard \+ constants, the stable serialization canon, the internal WSGI adapter \+ unified envelopes, the voice/Q-bridge/drive primitives, and the greenfield path. I also reclassified issues (what’s fixed vs. still open) and added a short “fresh repo” note at the end.

---

# **Glow HD Engine — Architecture & Design (repo audit, updated)**

**Timestamp:** Wed, Sep 24, 2025 • 04:30 EEST (Europe/Tallinn)  
 **Scope:** Engine-only (math \+ envelopes \+ internal adapter). No FE/BE/DB code lives here.

## **Environment**

* **Host image (from bundle):** Ubuntu 24.04.2 LTS (`/etc/os-release`)  
* **Python toolchain:** Python 3.12.1; virtualenv none (by design)  
* **Pins (authoritative):** `pytest==7.4.4 • jsonschema==4.22.0 • ruff==0.5.6 • mypy==1.10.0 • typing_extensions==4.12.2`  
* **Pin status:** ✅ Enforced by `scripts/ensure_env.py` (writes `artifacts/env_check.txt`); drift is a test failure.  
* **Identity:** ✅ Import-time guard in `hd_core/stable/identity.py` compares a **repo-relative composite** of freeze artifacts to baked constants in `hd_core/stable/identity_constants.py`.  
  * Allowlist is explicit (no backups/transients); artifacts:  
     `policy/freeze_pack_v1_1.json`, `config/bands_4B60_v1.json`, `catalog/channels_catalog_v1.json`, `catalog/motor_throat_v1.json`, `schemas/channels_catalog_v1.schema.json`  
  * `scripts/identity_bump.py` is the **only** way to update constants; it recomputes → writes `artifacts/identity.txt` \+ `artifacts/CHECKSUMS.txt` → self-verifies in a fresh interpreter → appends `docs/SYNC_LOG.md`.

Static signals:

* `cloc ~2.5k` LOC Python (+ JSON/TOML/MD)  
* mypy clean; (prior “duplicate-module” warning addressed by package layout)  
  ---

  ## **Design Strategy**

Deterministic, standalone core library.

* **Pure functions only** (no network/DB/PII).  
* **Freeze pack** governs math knobs & guardrails (EM domains, talk weights, ethics caps, Q-bridge params, windows).  
* **Stable serialization canon** (sercanon): normalize → `stable_dumps` → `stable_hash`; idempotence hash **masks \+ prunes** `(_diagnostics|_why|_admin_debug|meta.trace)` and drops empties.  
* **Unified envelopes**: one success/error shape used by library and internal HTTP adapter.  
* **Internal-only adapter**: pure WSGI, strict headers (`Cache-Control: no-store`), 64 KiB body cap, `X-Correlation-Id` echo.  
* **Evidence over claims**: SYNC\_LOG, artifacts, golden byte-identity checks.

Operating principles (applied):

* One lane at a time; tiny reversible changes; proof before promises.  
* Byte-determinism (stable key order, minified JSON, fixed hashing).  
* Contract clarity lives in freeze packs \+ schemas; no hard-coded knobs.  
  ---

  ## **Structure (current)**

1. hd\_core/  
2.   stable/  
3.     identity\_constants.py   \# GENERATED ONLY (bump script)  
4.     identity.py             \# import-time guard, composite verification  
5.     sercanon.py             \# stable\_normalize/dumps/hash \+ idempotence masks  
6.     freeze.py               \# iter\_artifacts(), repo-relative checksums  
7.   voice/  
8.     path.py                 \# BFS route-to-throat (hop binning 1/2/≥3)  
9.   bridge\_law/  
10.     qbridge.py              \# candidates \+ monotone Q (len/voice/sym/circ)  
11.     drive.py                \# inclusive drive floor gate  
12.   envelope/  
13.     types.py                \# make\_success / make\_error (unified shape)  
14.     errors.py               \# typed exceptions \+ map\_exception  
15.   adapter/  
16.     internal\_http.py        \# pure WSGI: /internal/{healthz,readyz,version}  
17. packs/v1/  
18.   policy/freeze\_pack\_v1\_1.json  
19.   config/bands\_4B60\_v1.json  
20.   catalog/channels\_catalog\_v1.json  
21.   catalog/motor\_throat\_v1.json  
22.   schemas/channels\_catalog\_v1.schema.json  
23. scripts/  
24.   ensure\_env.py  
25.   identity\_bump.py  
26.   print\_separation\_artifacts.py  
27. docs/  
28.   RUN.md            \# includes “Sanity & Benchmarks”  
29.   SYNC\_LOG.md  
30. artifacts/          \# outputs only (git-ignored)  
31. tests/  
32.   test\_sercanon.py  
33.   test\_voice\_qbridge\_drive.py  
34.   test\_envelope\_errors.py  
35.   test\_envelope\_success.py  
36.   test\_adapter\_internal.py  
    

Build/Run posture:

* **Library-first** (tests & scripts import package).  
* **Internal WSGI adapter** for ops-only endpoints; compute endpoints can be added later.  
* No DB, no network dependencies; inputs are JSON packs; outputs are artifacts.  
  ---

  ## **What’s new (landed since prior audit)**

* ✅ **Identity bedrock** with constants module \+ bump script; repo-relative composite; SYNC\_LOG; import-time guard.  
* ✅ **Serialization canon** unified (no duplicates); idempotence masks prune & drop empties → diagnostics never change digest.  
* ✅ **Voice/Q-bridge/Drive** primitives: BFS throat reachability; monotone Q; **inclusive** drive floor (direct Motor→Throat OR throat-touching \+ Q≥threshold).  
* ✅ **Unified envelopes \+ adapter**: one JSON shape across modes; 64 KiB cap; `no-store`; `X-Correlation-Id` echo; `/internal/{healthz,readyz,version}` byte-stable.  
* ✅ **Determinism evidence**: sample artifacts emitted (`envelope_success`, `envelope_error`, `adapter_version_payload`); tests assert byte identity across runs.  
  ---

  ## **Outstanding Issues (reclassified)**

1. **Pins** — **GREEN**  
    Enforced via `ensure_env.py`; failures are explicit.

2. **Identity compute vs file source** — **YELLOW**  
    The **authoritative** ops gate uses `artifacts/identity.txt`. Code path also recomputes from `freeze.iter_artifacts()` and should match; keep a small check in tests to prevent regressions.

3. **Catalog/data health** — **YELLOW**  
    Current catalog snapshot may produce “no motor centers present” in certain fixtures (observed during separation tests). This is dataset-level, not math; confirm catalog completeness in the next freeze.

4. **Entry point docs** — **GREEN**  
    `docs/RUN.md` points to library/adapter usage (no stale `main.py` references).

5. **Band windows/caps file** — **YELLOW**  
    Windows/caps exist in freeze; if you want per-band tuning outside policy, add a small `scoring_config_v1.json` \+ schema (build-time only).

6. **Error code catalog** — **YELLOW**  
    The envelope maps typed exceptions to `{BadRequest|TooLarge|Timeout|Validation|Internal}`; finalize the table and keep BE mapping 1:1.

   ---

   ## **Appendix — Repo Audit Intake (refreshed)**

* Latest audit bundles confirm: pins OK; identity artifacts present; version endpoint returns repo-relative checksums; envelope samples byte-stable.  
  ---

  # **Glow HD Engine — Architecture Plan (unchanged core; clarified)**

**Mode:** Dev via API · Prod via DB & Library  
 **Editors:** Isis (PO/Lead), Pair Coder

## **1\) Scope & Intent**

* **Dev/Staging:** backend ↔ engine via internal HTTP (easy smoke/ops).  
* **Prod:** engine as an **in-proc library**; inputs are stored **ChartV1** (no birth/timezone); compute-on-write for charts; cached pair results.

  ## **2\) Principles (non-negotiables)**

Stateless core; determinism \+ idempotence hash; privacy (no PII/bodies); single math truth via freeze; presentation out of scope.

## **3\) Integration Modes**

**3.1 Internal HTTP (dev/staging)**

* `POST /internal/engine/v1/evaluate` (private) with strict headers; ≤64 KB; 3s budget; 1× retry on 5xx/timeout only.

**3.2 Library (production)**

* `compute_pair(chart_a, chart_b, release_id, *, diagnostics=False) -> {bands, meta, idempotence_hash, …}`  
* Envelopes identical to HTTP mode; no CSRF in library.

  ## **4\) Data Strategy — Compute-on-Write \+ Cached Pairs**

* `chart_snapshot(user_id, release_id)` holds canonical chart JSON \+ provenance pins (provider, version, fingerprint).  
* `pair_evaluation(min_user, max_user, release_id)` caches results; invalidated on chart change or release change.

  ## **5\) Human Design API Ingest (ChartBuilder)**

* BE owns input validation \+ geocoding UX (FE assists); **Engine never receives birth/timezone in prod**.  
* Store normalized chart \+ provenance pins; version payloads (`chart_version`, `chart_fingerprint`).

  ## **6\) Engine Interfaces (Shared Envelopes)**

* **HTTP** request/response shapes (dev convenience).  
* **Library** consumes ChartV1 (centers, channels, gates, profile, authority, \+ provenance pins); ignores unknown keys.

  ## **7\) Backend Workflows (BE)**

* **Birth update:** call Chart API → normalize/store snapshot → invalidate pairs → audit (keys only).  
* **Match request:** load snapshots → check `pair_evaluation` → compute & persist (on miss).  
* **Release change:** lazy recompute (default) or backfill.

  ## **8\) DB Notes (minimal contract)**

Tables: `birth_data`, `chart_snapshot`, `pair_evaluation`.  
 Invariants: one current birth; namespaced by `release_id`; canonical min/max pair ordering.  
 Indexes & TTLs per prior draft.

## **9\) Security, Privacy, Headers**

* CSRF enforced at BE only; engine JSON always `Cache-Control: no-store`; `X-Correlation-Id` everywhere; no bodies/PII in logs; secrets live only in BE env.

  ## **10\) Performance & Limits**

* Engine compute p95 ≤ 400 ms; p99 ≤ 800 ms (library).  
* HTTP adapter: 3 s timeout; ≤64 KB; 1× retry on 5xx/timeout.  
* Payloads compact; stable key order; minified for hashing.

  ## **11\) Observability & Ops**

* Structured logs (keys only); metrics (counts/errors/latency, cache hit rates).  
* Internal endpoints: `/internal/{healthz,readyz,version}`; version carries `release_id` \+ repo-relative checksums.  
* Determinism checks baked into sanity run.

  ## **12\) Open Items (do not block)**

* Finalize adapter error table & BE mapping.  
* Confirm Postgres pool/backup cadence; Redis namespaces/TTLs; pair cache retention.  
* Release policy: how many prior `release_id`s accepted during rollout.  
* Logging retention & redaction windows.

  ## **13\) Summary**

* **Dev:** internal HTTP with strict limits & typed errors.  
* **Prod:** in-proc library; charts computed on write; pairs cached; determinism & costs optimized.  
* Clean boundaries, low latency, auditable outputs, with HTTP adapter as a fallback.

  ## **Appendix A — Chart API ↔ ChartV1 (mapping, unchanged)**

Persist: type, profile, authority/strategy, definition, signature/not\_self, centers, channels, gates, incarnation\_cross, activations, plus variables you’ll use. Normalize to minimal ChartV1; keep provenance pins; validate with JSON Schema.

---

## **Greenfield note (decision tracked)**

Given prototype churn and legacy paths, a **fresh repository** is planned:

* Seed only the **proven** modules (identity, sercanon, envelopes/adapter, voice/Q/drive) \+ tests.  
* Freeze packs live under `packs/v1/` with an explicit allowlist.  
* Scripts are ritualized (`identity_bump.py`, sanity/audit, card reporter).  
* Determinism gates and artifacts are required on `main`.  
  ---

  ## **Next tiny, reversible steps (updated)**

1. **Freeze integrity:** run `scripts/identity_bump.py`; attach SYNC\_LOG tail & artifacts (proof).  
2. **Sanity & goldens:** emit / verify `envelope_*` and `/internal/version` byte identity; commit artifacts.  
3. **Catalog pass:** confirm motor centers presence in `catalog/*` (data check only) before the next freeze.  
4. **Error table:** finalize adapter/library code list and BE mapping (typed → HTTP).  
5. **Greenfield init:** scaffold new repo per “Greenfield note”; copy modules \+ tests only; run identity \+ sanity gates.

   # **Glow HD Engine — Plan & Reference (Table of Contents)**

1. **Document Meta**

   * Purpose & scope · Owners · Versioning · Release identity (hash) · Changelog pointers

2. **Executive Summary**

   * Vision & philosophy · Product covenant (presenter boundaries, no numbers) · Ethics & safety caps

3. **System Overview**

   * End-to-end architecture (FE, BE, Engine, Chart API) · Lake vs Writers model · Data flow at a glance

4. **Core Architecture (Engine)**

   * Module map · Public interfaces (library \+ internal HTTP) · Dependencies & boundaries (no PII, no network/DB)

5. **Data Model & Contracts**

   * **ChartV1 schema** (engine input)

   * Result envelope (bands \+ meta)

   * Deterministic hashing & idempotence fields

6. **Chart Ingest (Human Design API)**

   * API boundary & provenance pins (provider, version, fingerprint)

   * Birth-update workflow · Storage in `chart_snapshot` · Error mapping (no PII)

7. **Persistence Model (Glow DB)**

   * Tables: `birth_data`, `chart_snapshot`, `pair_evaluation` (keys, invariants, indexes)

   * Invalidation rules · Retention policy · Release namespacing

8. **Algorithms & Mathematical Foundations**

   * Domains/weights/priors · EM partition · Directional loads

   * Q-bridge & drive floor · Band mapping · Windows/caps

   * Invariants & proofs (at a glance)

9. **Determinism & Reproducibility**

   * Freeze pack & schemas · Stable ordering & byte-identical outputs

   * `release_id` lifecycle · SYNC\_LOG & evidence

10. **Configuration (Programmatic, Build-time)**

    * Freeze files & scoring config · Field/enum registry (codegen rules)

    * No runtime client config · Emergency switches (server-side only)

11. **Integration with Glow App**

    * **Production mode:** in-proc library (charts-in → scores-out)

    * **Dev/Staging mode:** internal HTTP adapter

    * Error model, retries, headers · Performance SLOs & limits

12. **FE/BE Contracts (Lake & Writers)**

    * Lake response shape (bands-only \+ `engine_tag`)

    * Writers pattern (204 \+ `no-store`, then lake refetch)

    * Typed errors & FE handling (401/403/429/5xx)

13. **Security, Privacy & Compliance**

    * PII boundaries · `Cache-Control: no-store` discipline

    * Logging/redaction policy · Secrets handling · Third-party & licensing notes

14. **Observability & Operations**

    * Logs (keys only), metrics, tracing · Correlation IDs

    * Health/ready/version endpoints (HTTP mode) · Runbooks & incident basics

15. **Performance & Scalability**

    * Targets (engine p95/p99) · Concurrency & body-size limits

    * Cache hit rates · Backfill strategies (lazy vs eager)

16. **Testing & Quality Gates**

    * Unit, property, golden fixtures · Idempotence/byte-stability checks

    * Lint/type/security scanning · Sanity script & deterministic artifacts

    * PO Scenario Execution & post-deploy smoke

17. **Command Line & Developer Tools**

    * CLI surface (run, inspect, verify) · Local dev harness (API fixture fetch)

    * Repo tasks & make/audit scripts

18. **Release Management & Versioning**

    * Version scheme · Freeze process · Backward compatibility window

    * Deprecation rules · Rollback & pinning

19. **Conventions & Contribution Guide**

    * Code style & repo hygiene · Branching & PR review

    * ADR format · Commit message norms

20. **Decision Log & Open Questions**

    * ADR index · Current open decisions (limits, retention, rollout policy)

21. **Risk Register**

    * Top risks, owners, mitigations, triggers

22. **Appendices**

    * Glossary & acronyms · Sample envelopes & fixtures

    * Reference tables (IDs/constants) · Change log snapshot

    

# **Document Meta**

## **Purpose & Scope**

**Purpose.** Establish the authoritative architecture contract for the Glow HD Engine so we can implement, integrate, and operate it safely and deterministically.

**Scope (included).**

* Engine boundaries and integration modes (Dev: internal HTTP; Prod: in-process library).

* Data contracts: **ChartV1** (engine input) and the **Result** envelope (bands \+ meta).

* Persistence strategy: `chart_snapshot` (compute-on-write) and `pair_evaluation` (cached pairs).

* Security, privacy, observability, performance targets, and operational constraints.

* Interfaces with Glow FE/BE and the external Human Design API (ChartBuilder).

**Out of scope.**

* Sprint planning or resourcing.

* End-user copy/UX.

* Full DB migration scripts (we specify only tables/keys/invariants required by contracts).

---

## **Owners**

* **Owner & Sole Stakeholder:** **Nathan Amthor**

New reviewers/approvers will be added here with role and area of responsibility.

---

## **Versioning (this document)**

* **Doc version:** **2025.1**

* **Status labels:** `draft` → `reviewed` → `approved`.

* **Approval gate:** transition to `approved` requires explicit sign-off by **Nathan Amthor** (dated entry in the Change Log).

---

## **Release Identity (engine math)**

**Intent.** Every engine math release is reproducible and provable.

**Canonicalization rules**

* Inputs serialized as **minified JSON with lexicographically sorted keys**, UTF-8, LF newlines.

* Hash algorithm: **SHA-256**.

**Artifacts included in the release hash**

* `policy/freeze_pack_*.json`

* `catalog/channels_catalog_*.json` (and any catalog files the freeze references)

* `config/bands_*.json`

* `config/scoring_config_*.json` (if present)

**Identifiers**

* **release\_id (hash):** `sha256:<64-hex>` over the concatenation of canonicalized artifacts in the fixed order above.

* **engine\_tag (human-readable):** `HD-2025.1-YYYYMMDD-<7hex>` where `<7hex>` is the first 7 chars of `release_id`.

**Evidence**

* A SYNC\_LOG entry records: each component filename \+ SHA-256, the exact concatenation order, the resulting `release_id`, and the `engine_tag`.

---

## **Changelog & Evidence Locations**

* **Change Log (human-readable):** `docs/CHANGELOG.md`

  * Entry per release: date, `engine_tag`, high-level notes, migration/compatibility remarks.

* **SYNC\_LOG (hash evidence):** `docs/SYNC_LOG.md`

  * For each release: component table (filename → SHA-256), concatenation order, computed `release_id`, `engine_tag`, signer (Nathan), and timestamp.

* **Release bundle (optional):** `release/<engine_tag>/`

  * Frozen copies of the artifacts used, plus the SYNC\_LOG excerpt for that tag.

---

## **Cross-references**

* **Integration Constraints:** this doc references and governs them; updates to either must be reflected in `docs/CHANGELOG.md`.

* **Decision Log (ADRs):** architectural decisions live under `docs/adr/` and are linked from the Change Log when they affect the release.

---

**Effective immediately:** version **2025.1** is the working document version; the next math freeze will produce a corresponding `engine_tag` following the scheme above.

# **Executive Summary**

## **Vision & Philosophy**

Glow’s HD Engine exists to **help people connect with clarity and kindness**. It translates two canonical Human Design charts into a small, stable set of **human-readable bands** and supporting **meta**—nothing more. The engine is:

* **Deterministic:** same inputs → byte-identical outputs, stamped with a `release_id`.

* **Minimal & private:** charts-in → bands/meta-out; no PII, no birth/timezone at runtime.

* **Operationally sane:** compute-on-write for charts, cached pair results, and a clean fallback HTTP adapter for dev/ops.

* **Upgradable without drift:** every change to math is frozen, hashed, and auditable.

## **Product Covenant (Presenter Boundaries, No Numbers)**

* **Bands, not scores.** The engine emits qualitative **bands** (e.g., “Warm / Open / Cool”) and carefully scoped **meta** for trace/explanation. **No numeric scores, ranks, or percentiles** are exposed to end users.

* **Private math.** Internal weights, windows, and thresholds remain private; we surface only what a person needs to navigate a relationship respectfully.

* **Charts-only input.** Production inputs are **stored chart JSON** (ChartV1) with provenance; birth/timezone never touch the engine at runtime.

* **Lake-first reads.** The SPA consumes a single lake response that includes a short **matching summary** and an `engine_tag`; raw WHY/debug traces never leave the server.

* **Deterministic language.** Presenter copy is owned outside the engine; the engine never generates open-ended advice or medical/therapeutic claims.

## **Ethics & Safety Caps**

* **Respect & non-harm.** Outputs avoid labeling, pathologizing, or determinism about people. Language is neutral, non-prescriptive, and refrains from “should/shouldn’t.”

* **No sensitive inferences.** Engine inputs and outputs **exclude** PII and protected attributes. We do **not** infer mental health, medical status, or traits beyond the HD chart domain.

* **Guardrails (caps) enforced in math:**

  * **No absolute judgments:** band mapping avoids extremes that imply permanence or value judgments.

  * **Symmetry checks:** AB/BA swap must not produce contradictory meta (proof in tests).

  * **Window/cap constraints:** limits on directional loads and bridge interpretations prevent overconfident narratives.

* **Privacy-by-default.** `Cache-Control: no-store` on all engine JSON that could reflect a person’s relationships; logs contain **keys only** (no bodies/PII).

* **Transparency & audit.** Every release includes a **SYNC\_LOG** (hashes) and a human **Change Log**. If the freeze changes, results explicitly carry the new `release_id` and `engine_tag`.

* **Operational safety.** Rate limits on writers; idempotency for engine requests; graceful degradation on upstream outages (serve last-known-good pair result if policy allows, or a safe “unavailable” response).

* **Use boundaries.** The engine is a **relationship signal**, not diagnosis, therapy, or guarantee of outcomes. Product copy must include this boundary; the engine will not emit content that violates it.

**Bottom line:** We deliver a **small, predictable, and humane** signal layer over charts—one that people can trust, teams can operate confidently, and we can prove has not drifted.

# **System Overview**

## **Components (end-to-end)**

* **Frontend (FE)** — React \+ Vite on Vercel

  * Reads from the **Lake** endpoint only.

  * Sends `X-Correlation-Id`, carries CSRF token on writers.

* **Backend (BE)** — Flask on Railway (Gunicorn), Postgres \+ Redis

  * Owns sessions, CSRF, CORS, error mapping, and persistence.

  * Calls **Human Design API** (“ChartBuilder”) on birth create/update.

  * In **dev/staging**, can call Engine via **internal HTTP**; in **prod**, imports Engine **as a library**.

  * Exposes **Writers** (mutations) and a single **Lake** (read) surface to FE.

* **Engine** — Glow HD Engine core (stateless, deterministic)

  * **Prod:** library function `compute_pair(chart_a, chart_b, release_id)`; charts-in → bands/meta-out.

  * **Dev:** internal HTTP adapter for testing/ops (`POST /internal/engine/v1/evaluate`).

  * No PII, no network/DB; always `Cache-Control: no-store`; echoes `X-Correlation-Id`.

* **Human Design API (ChartBuilder)** — External service

  * `POST /bodygraphs` (or `/simple`) from BE only.

  * Returns canonical chart JSON that BE stores with provenance pins.

---

## **Lake vs Writers model**

* **Lake (read model)**

  * **One** canonical FE read: `GET /api/auth/me` (example) returns user state \+ **matching summary** (bands/top3/prompt/`engine_tag`).

  * FE **never** assembles state from writer responses; after any writer, FE **refetches the Lake**.

  * Engine WHY/debug traces never surface to FE.

* **Writers (mutation model)**

  * Small, idempotent endpoints (e.g., update birth data, connect/disconnect people).

  * Return `204 No Content` (or `200 {"status":"ok"}`) with `Cache-Control: no-store`.

  * FE pattern: submit writer → on success, **refetch Lake**.

---

## **Data flows at a glance**

### **A) Birth Create/Update (compute-on-write for charts)**

1. **FE → BE (Writer):** user submits birth data (+ CSRF).

2. **BE → Chart API:** validate → call `/bodygraphs` (auth headers).

3. **BE (DB):** normalize & fingerprint → **upsert** `chart_snapshot(user_id, release_id)` with `{chart_provider, chart_version, chart_fingerprint}`.

4. **BE (DB):** **invalidate** `pair_evaluation` rows where this user participates.

5. **BE → FE:** `204` \+ `no-store`.

6. **FE:** **refetch Lake** → Lake includes updated **matching summary** (after on-demand pair compute if needed).

### **B) Match Request (charts-in → scores-out, cached)**

1. **BE (DB):** read `chart_snapshot` for A & B at **current `release_id`**; refresh via Chart API if missing/stale.

2. **BE (DB):** check `pair_evaluation(min(A,B), release_id)` and chart fingerprints.

   * **Hit (fresh):** return cached result.

   * **Miss/Stale:** call **Engine library** `compute_pair(chartA, chartB, release_id)` → persist `{bands_json, meta_json, idempotence_hash, duration_ms, fingerprints}` → return.

3. **Lake:** exposes **bands-only** summary \+ `engine_tag` to FE.

### **C) Release Change (math upgrade)**

1. **Ops:** mark new **`release_id`** active (freeze pack hashed & logged).

2. **Lazy recompute (default):**

   * Charts recomputed **on first access**; pairs recomputed **on demand**.

3. **Eager (optional):** backfill charts for active users in background; pairs still recompute on access.

4. **Lake:** reflects new `engine_tag` once pair results exist for the new release.

### **D) Dev/Staging path (internal HTTP adapter)**

1. **BE → Engine HTTP:** `POST /internal/engine/v1/evaluate` (JSON, ≤64 KB).

2. **Headers:** `Content-Type`, `Accept`, `Cache-Control: no-store`, `X-Correlation-Id` (+ optional `Idempotency-Key`).

3. **Policy:** timeout 3 s; one retry on 5xx/timeout; no retry on 4xx.

4. **Use:** local dev, CI smoke, incident isolation.

---

## **Interfaces & boundaries (trust lines)**

* **FE ↔ BE:**

  * **Writers:** CSRF (double-submit), CORS allow-list, typed errors, `no-store`.

  * **Lake:** bands-only \+ `engine_tag`; no raw WHY; `X-Correlation-Id` propagated.

* **BE ↔ Chart API:**

  * Server-to-server; keys in BE env; request/response hashed for audit (minus secrets).

* **BE ↔ Engine (Prod):**

  * **Library call** only; process boundary is BE.

  * Inputs: two **ChartV1** payloads \+ `release_id`.

  * Output: bands \+ meta \+ `idempotence_hash` \+ duration.

* **BE ↔ Engine (Dev):**

  * Internal HTTP; same envelopes; strict headers; `no-store`.

---

## **Observability (threaded through flows)**

* **Correlation:** FE generates `X-Correlation-Id` → BE logs/echoes → Engine logs/echoes.

* **Logs (keys-only):** route/function, `release_id`, `correlation_id`, `duration_ms`, `ok`, `code`. No bodies/PII.

* **Metrics:** request counts, error codes, latency histograms (p50/p95/p99), **cache hit rate** for `pair_evaluation`.

* **Health/Ready/Version (HTTP mode):** `/internal/healthz`, `/internal/readyz`, `/internal/version`.

---

## **Invariants (must always hold)**

* Engine sees **charts only** (no birth/timezone) in production.

* All Engine JSON (dev or prod surfaced) is sent with **`Cache-Control: no-store`**.

* **Determinism:** same charts \+ `release_id` → same output and `idempotence_hash`.

* **Namespacing:** `chart_snapshot` and `pair_evaluation` are keyed by **`release_id`**; pairs use **canonical min/max** ordering.

* **Lake-first UX:** after any writer, FE **refetches Lake**; writers never shape FE state directly.

This is the systems blueprint we’ll build and test against.

# **Core Architecture (Engine)**

## **Module Map (authoritative, current repo shape)**

* **`hd_core/`** — production math (pure functions)  
  * **`policy_loader.py`** — loads & validates the **freeze pack** (`policy/freeze_pack_*.json`); exposes an immutable policy object (domains, weights, caps, windows, ids).  
  * **`catalog_loader.py`** — loads **catalogs** (e.g., channels/centers), normalizes identifiers, enforces vocabulary, and provides lookup helpers.  
  * **`centers/graph.py`** — center graph & reachability utilities (e.g., “route to Throat”).  
  * **`bridges/qbridge.py`** — computes bridge candidates and **Q-bridge meta** (length, voice, symmetry flags).  
  * **`bridges/drive.py`** — drive floor / boundary checks (ethics/safety caps integration).  
  * **`loads/api.py`** — computes **directional loads** from charts (talk/pressure/scalars) under policy constraints.  
  * **`features/api.py`** — the **façade** that composes EM partition \+ directional loads \+ Q-bridge \+ drive floor; also performs canonicalization, AB↔BA symmetry check, and stable key ordering before hashing.  
  * **`hashing.py`** (or within façade) — computes **`idempotence_hash`** over minified, sorted JSON outputs (SHA-256).  
* **`hd_core_proto/`** — experimental adapters (kept separate from core to avoid drift)  
  * **HTTP adapter glue** (dev/staging only).  
  * **Canonicalization helpers** used by tests and fixtures.  
* **`policy/`** — frozen knobs & guardrails  
  * **`freeze_pack_*.json`** — single source of math truth (domains, weights, caps, windows, ids).  
* **`catalog/`** — canonical reference data (e.g., `channels_catalog_*.json`, motor/throat sets).  
* **`config/`** — bands map and optional scoring config (programmatic, build-time only).  
* **`tests/`** — env pins; schema/guardrails; EM partition; façade shape/symmetry/idempotence; bridge/display.

Design intent: **core stays small and strictly pure**; anything operational or environment-specific lives in protos, adapters, or the BE.

---

## **Public Interfaces**

### **A) Library API (production)**

Importable, pure functions. No network, no DB, no file I/O at runtime.

* **`compute_pair(chart_a: ChartV1, chart_b: ChartV1, release_id: str, *, diagnostics: bool = False) -> Result`**

  * **Inputs**  
    * `chart_a`, `chart_b`: canonical **ChartV1** objects (stored charts; no birth/timezone/PII).  
    * `release_id`: selects the frozen math (must match loaded freeze pack).  
    * `diagnostics` (optional): include limited meta needed by ops; never WHY copy.  
  * **Output**  
    * `Result` JSON:  
       `{ ok: true, release_id, bands: {...}, meta: {...}, idempotence_hash, duration_ms }`  
  * **Contract**  
    * **Deterministic** for the same `(chart_a, chart_b, release_id)`.  
    * **Symmetric** under AB↔BA where specified (proved by tests).  
    * **Stable key order**; `idempotence_hash` is SHA-256 of minified, sorted JSON.  
* *(Optional utility, non-blocking)* **`version_info() -> dict`**  
   Returns `{ release_id, engine_tag }` from the loaded freeze pack (used by BE for observability).

### **B) Internal HTTP Adapter (development & staging only)**

Mirrors the library contract for local/CI/ops isolation.

* **`POST /internal/engine/v1/evaluate`**

  * **Headers:** `Content-Type: application/json`, `Accept: application/json`, `Cache-Control: no-store`, `X-Correlation-Id` (echoed), optional `Idempotency-Key`.  
  * **Body (dev convenience):** either charts (`{a_chart, b_chart, release_id}`) **or** birth payload used by the harness to fetch charts in dev; **production never uses birth here**.  
  * **Responses:**  
    * `200` with **Result** (as above).  
    * Typed errors with `{ ok:false, code, error, details?, release_id, correlation_id }`.  
  * **Operational policy:** timeout 3s; one retry on 5xx/timeout; no retry on 4xx. Always `no-store`.  
* **`GET /internal/healthz` · `GET /internal/readyz` · `GET /internal/version`**  
   Lightweight health, readiness (freeze loaded), and version exposure (`release_id`, checksums). Dev/staging only.

---

## **Dependencies & Boundaries**

### **Hard boundaries (must never be crossed by core)**

* **No PII.** Core never accepts names, emails, or birth/timezone/place in production; inputs are **charts only**.  
* **No side effects.** No network calls, no DB/Redis access, no filesystem writes/reads at runtime.  
* **No runtime config from clients.** All scoring knobs live in the **freeze pack**; client “preferences” cannot alter math.  
* **No presenter copy.** Engine emits **bands \+ scoped meta**; UX copy is external.

### **Allowed dependencies (core)**

* **Python standard library** only (e.g., `typing`, `json`, `hashlib`, `dataclasses`, `functools`, `itertools`, `math`, `copy`).  
* **Local JSON artifacts** loaded at **process start** (freeze pack, catalogs, config) via `policy_loader`/`catalog_loader`.  
* **Test-only** tooling (pytest, mypy, ruff) and proto adapters live outside `hd_core/`.

### **Invariants enforced by the façade**

* **Determinism:** stable ordering → byte-identical outputs for identical inputs.  
* **Symmetry:** AB vs BA checks where the domain requires it; meta cannot contradict across swap.  
* **Caps & ethics:** directional loads, bridges, and drive floor respect safety caps defined in the freeze pack.  
* **Namespacing:** behavior is a pure function of `(chart_a, chart_b, release_id)`; release changes alone can change outputs.

---

## **Load/Init Lifecycle (how math becomes “live”)**

1. **Startup:** `policy_loader` reads `freeze_pack_*.json`; `catalog_loader` reads required catalogs; both are validated and normalized to immutable structures.  
2. **Activation:** `release_id` is computed/verified (checksums match SYNC\_LOG); **engine\_tag** is exposed for observability.  
3. **Serve:** library calls (prod) or HTTP adapter (dev) use the in-memory frozen policy; no further disk/network access.

---

## **Error Model (engine-local)**

* **Validation:** `validation_error` (schema/unknown ids/unsupported release).  
* **Resource:** `payload_too_large` (dev HTTP only).  
* **Compute:** `compute_timeout` (guard) or `internal_error` (unexpected path).  
* **Rate:** `rate_limited` (dev HTTP only; prod library does not rate-limit).  
   All error envelopes exclude PII and include `release_id` and (when present) `correlation_id`.

---

**Summary.** The Engine is a **small, pure, deterministic** library. In production it receives **two charts and a release**, returns **bands \+ meta** with a stable hash, and performs no I/O. A thin HTTP skin exists only for development and operational isolation, mirroring the same contract. Boundaries around PII, networking, and configuration keep the core safe, auditable, and easy to upgrade.

# **Data Model & Contracts**

## **1\) ChartV1 (engine input)**

**Intent.** Production inputs to the Engine are **stored charts** (not birth/timezone). ChartV1 is a compact, canonical shape derived from the Human Design API response and stored in `chart_snapshot`. Provenance pins ensure auditability and drift control.

### **1.1 Definition (informative)**

* **Required**  
  * `release_id` — the frozen math identity (SHA-256 over freeze artifacts).  
  * `centers` — map of center → `"defined"|"open"` (no other values).  
  * `channels` — array of canonical channel ids, e.g. `"10-20"`, `"57-20"`.  
  * `gates` — array of gate or gate.line strings, e.g. `"10"`, `"10.3"`.  
* **Recommended provenance pins**  
  * `chart_provider` — e.g., `"HDAPI"`.  
  * `chart_version` — provider version/ephemeris tag.  
  * `chart_fingerprint` — `sha256:` of the **minified+sorted** chart payload you store.  
* **Optional (the engine may use or ignore)**  
  * `profile` — e.g., `"4/6"`.  
  * `authority` — string label from the provider.

### **1.2 JSON Schema (authoritative, minimal)**

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/engine/chartv1.schema.json",  
  "title": "ChartV1",  
  "type": "object",  
  "required": \["release\_id", "centers", "channels", "gates"\],  
  "additionalProperties": true,  
  "properties": {  
    "release\_id": {  
      "type": "string",  
      "pattern": "^sha256:\[0-9a-f\]{64}$"  
    },  
    "centers": {  
      "type": "object",  
      "additionalProperties": false,  
      "patternProperties": {  
        "^\[A-Za-z\]\[A-Za-z0-9 \_-\]{0,24}$": {  
          "type": "string",  
          "enum": \["defined", "open"\]  
        }  
      },  
      "minProperties": 1  
    },  
    "channels": {  
      "type": "array",  
      "items": {  
        "type": "string",  
        "pattern": "^\\\\d{1,2}-\\\\d{1,2}$"  
      },  
      "minItems": 0,  
      "uniqueItems": true  
    },  
    "gates": {  
      "type": "array",  
      "items": {  
        "type": "string",  
        "pattern": "^\\\\d{1,2}(?:\\\\.\[1-6\])?$"  
      },  
      "minItems": 0,  
      "uniqueItems": true  
    },  
    "profile": {  
      "type": "string",  
      "pattern": "^\[1-6\]/\[1-6\]$"  
    },  
    "authority": {  
      "type": "string",  
      "minLength": 1,  
      "maxLength": 64  
    },  
    "chart\_provider": {  
      "type": "string",  
      "minLength": 1,  
      "maxLength": 64  
    },  
    "chart\_version": {  
      "type": "string",  
      "minLength": 1,  
      "maxLength": 64  
    },  
    "chart\_fingerprint": {  
      "type": "string",  
      "pattern": "^sha256:\[0-9a-f\]{64}$"  
    }  
  }  
}

### **1.3 Example (canonicalized)**

{  
  "release\_id": "sha256:1b7a8c3e1d7b2f3b5c9f4e6a7b8c9d0e1f2a3b4c5d6e7f8090a1b2c3d4e5f607",  
  "centers": { "Throat": "defined", "G": "open", "Sacral": "defined" },  
  "channels": \["10-20", "57-20"\],  
  "gates": \["10.3", "20.5", "57.2"\],  
  "profile": "4/6",  
  "authority": "Emotional",  
  "chart\_provider": "HDAPI",  
  "chart\_version": "1.1.204",  
  "chart\_fingerprint": "sha256:0f3bd0c6a9f4e2d1c8b7a6e5d4c3b2a10987fedcba9876543210fedcba987654"  
}

---

## **2\) Result envelope (bands \+ meta)**

**Intent.** The Engine outputs a small, stable **signal** suitable for the Lake’s matching summary. No numbers, no PII, and strictly deterministic.

### **2.1 Definition (informative)**

* **Required**  
  * `ok` — always `true` on success.  
  * `release_id` — echoes the frozen math identity used.  
  * `bands` — object mapping category ids → band strings (band values must exist in the loaded bands map).  
  * `meta` — compact, non-PII trace fields used by the app (e.g., bridge symmetry); no WHY narratives.  
  * `idempotence_hash` — SHA-256 over the **core** result fields (see §3).  
* **Recommended**  
  * `duration_ms` — engine compute time in milliseconds.

### **2.2 JSON Schema (authoritative, minimal)**

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/engine/result.schema.json",  
  "title": "EngineResult",  
  "type": "object",  
  "required": \["ok", "release\_id", "bands", "meta", "idempotence\_hash"\],  
  "additionalProperties": false,  
  "properties": {  
    "ok": { "type": "boolean", "const": true },  
    "release\_id": {  
      "type": "string",  
      "pattern": "^sha256:\[0-9a-f\]{64}$"  
    },  
    "bands": {  
      "type": "object",  
      "minProperties": 1,  
      "patternProperties": {  
        "^\[a-z\]\[a-z0-9\_\]{1,31}$": { "type": "string", "minLength": 1, "maxLength": 32 }  
      },  
      "additionalProperties": false  
    },  
    "meta": {  
      "type": "object",  
      "additionalProperties": false,  
      "properties": {  
        "qbridge": {  
          "type": "object",  
          "additionalProperties": false,  
          "properties": {  
            "len\_hops": { "type": "integer", "minimum": 0 },  
            "sym": { "type": "string", "enum": \["both", "none", "a\_only", "b\_only"\] }  
          },  
          "required": \["len\_hops", "sym"\]  
        },  
        "throat\_route": { "type": "boolean" },  
        "caps": {  
          "type": "object",  
          "additionalProperties": { "type": "boolean" }  
        }  
      },  
      "required": \["qbridge"\]  
    },  
    "idempotence\_hash": {  
      "type": "string",  
      "pattern": "^sha256:\[0-9a-f\]{64}$"  
    },  
    "duration\_ms": { "type": "integer", "minimum": 0 }  
  }  
}

### **2.3 Example**

{  
  "ok": true,  
  "release\_id": "sha256:1b7a8c3e1d7b2f3b5c9f4e6a7b8c9d0e1f2a3b4c5d6e7f8090a1b2c3d4e5f607",  
  "bands": {  
    "harmony": "Warm",  
    "drive": "Cool",  
    "communication": "Open"  
  },  
  "meta": {  
    "qbridge": { "len\_hops": 2, "sym": "both" },  
    "throat\_route": true,  
    "caps": { "no\_throat\_59\_6": true }  
  },  
  "idempotence\_hash": "sha256:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  
  "duration\_ms": 183  
}

**Presenter boundary:** The FE’s Lake surfaces a **bands-only summary** (plus `engine_tag`). The full `meta` stays server-side unless explicitly needed for server-rendered explanations.

---

## **3\) Deterministic hashing & idempotence**

### **3.1 What is hashed**

`idempotence_hash` is computed over the **core, stable** subset of the success result:

{  
  "release\_id": "...",  
  "bands": { ... },   // keys sorted lexicographically  
  "meta":  { ... }    // keys sorted recursively  
}

Fields that vary by execution (**excluded** from the hash): `duration_ms`, any transport headers, `correlation_id`, request identifiers, timestamps.

### **3.2 Canonicalization**

* Serialize the **hash material** as **minified JSON** with **lexicographically sorted keys** at every level.  
* Strings are UTF-8; booleans lowercase; no trailing zeros are added/removed (we avoid floats).  
* Apply **SHA-256** to the resulting bytes and prefix with `sha256:`.

### **3.3 Stability guarantees**

* For identical `(chart_a, chart_b, release_id)` the engine produces **bit-identical** `bands` and `meta`, yielding the **same `idempotence_hash`**.  
* AB↔BA swap obeys symmetry rules encoded in policy; where symmetry is required, the hashed core must not contradict between orders.

### **3.4 Chart fingerprints (input provenance)**

* `chart_fingerprint` is computed by the BE over the **stored chart payload** (`chart_json`) as **minified+sorted JSON**, `sha256:`.  
* `pair_evaluation` stores both `a_chart_fingerprint` and `b_chart_fingerprint`. If either differs from the current snapshots, the pair result is treated as **stale** and recomputed.

---

**Contract summary**

* **Inputs:** `ChartV1` ×2 \+ `release_id` (no birth/timezone/PII).  
* **Outputs:** `ok=true`, `release_id`, `bands`, `meta`, `idempotence_hash` (+ `duration_ms`).  
* **Determinism:** `idempotence_hash = sha256(minified_sorted({release_id,bands,meta}))`.  
* **Audit:** every chart and pair row carries SHA-256 fingerprints; every engine release is tied to a `release_id` with SYNC\_LOG evidence.

# **Chart Ingest (Human Design API) — updated with FE geocoding assist**

## **1\) API boundary**

**Provider.** Human Design API (ChartBuilder)  
 **Base.** `https://api.humandesignapi.nl/v1/`  
 **Auth headers (BE → provider):**

* `HD-Api-Key: *****`  
* `HD-Geocode-Key: *****`

**Endpoints we use**

* `POST /bodygraphs` — full chart payload (type, profile, centers, channels, gates, activations, …).  
* `POST /bodygraphs/simple` — lean payload (type, profile, centers, channels\_short, gates) for dev/smoke.

**Request body (birth input)**

* `birthdate` (YYYY-MM-DD)  
* `birthtime` (HH:MM\[:SS\])  
* `location` (string) — **FE will usually send a *disambiguated, normalized place name*** (see FE geocoding assist below).  
  * The provider still performs its own geocoding; BE does not send lat/lon unless the API explicitly supports it (not assumed here).

**Response**

* JSON chart object (full or simple). We normalize and store; the Engine **never** sees birth inputs.

**Provider error statuses**  
 Documented examples include **400/401/403/404/500** with JSON bodies (we map these server-side; see §5).

---

## **2\) Provenance pins (audit & drift control)**

Every stored chart snapshot carries immutable provenance:

* `chart_provider` — e.g., `"HDAPI"`.  
* `chart_version` — provider version/ephemeris **if available** (otherwise we record `ingest_contract_version`, e.g., `hdapi-v1.bodygraphs`).  
* `chart_fingerprint` — `sha256:` of the **minified, sorted** stored `chart_json`.

**Fingerprinting rules**

1. Strip transient/unneeded fields.  
2. Serialize as **minified JSON with lexicographically sorted keys**, UTF-8, LF.  
3. Compute **SHA-256** → store `sha256:<64-hex>`.

---

## **3\) Birth-update workflow (compute-on-write)**

1. **FE (geocoding assist):** as the user types a place, FE offers geocoded **suggestions** and requires selecting a **specific, normalized place name** (partial strings are rare but still possible).  
2. **FE → BE (writer):** submit birth data \+ the **chosen normalized place name** \+ CSRF.  
3. **BE validates** syntax/sanity (date/time/tz/place) and rejects obviously ambiguous/partial strings.  
4. **BE → Chart API:** call `/bodygraphs` (prod) or `/simple` (dev).  
5. **Normalize** provider response → our stored chart JSON (only fields we rely on \+ harmless extras).  
6. **Attach provenance** (`chart_provider`, `chart_version` or `ingest_contract_version`, `chart_fingerprint`).  
7. **Upsert** `chart_snapshot(user_id, release_id)`.  
8. **Invalidate pairs** where this `user_id` participates (or mark stale by fingerprint mismatch).  
9. **Respond** `204 No Content` with `Cache-Control: no-store`.  
10. **FE refetches Lake**; BE computes pair on demand if cache is empty/stale.

**Prod rule:** no Chart API calls on reads. Charts are built **once** per birth update (and per `release_id` change).

---

## **4\) Storage in `chart_snapshot`**

**Key:** `(user_id, release_id)` (one current row per tuple).  
 **Fields:** `chart_json`, `computed_at` (UTC), `chart_provider`, `chart_version` (or `ingest_contract_version`), `chart_fingerprint`.  
 **Invariants:** namespaced by `release_id`; fingerprint changes when any field that affects Engine computation changes.

---

## **5\) Error mapping (PII-safe)**

We never expose provider error bodies to clients. BE translates to a canonical envelope:

| Provider | Typical cause | BE → FE response |
| ----- | ----- | ----- |
| 400 | Bad birth fields / unresolvable place | `422 Unprocessable Entity` \+ `{error:"validation_error"}` |
| 401/403 | Bad/expired keys | `503 Service Unavailable` \+ `{error:"upstream_auth"}` |
| 404 | Route not found (provider) | `503 Service Unavailable` \+ `{error:"upstream_route"}` |
| 500 | Provider error | `503 Service Unavailable` \+ `{error:"upstream_error"}` |

**Logging (server-side, keys-only):** route, `correlation_id`, provider status, **hashed** request skeleton (no secrets), response hash, `duration_ms`. No bodies/PII.

---

## **6\) Determinism & idempotence ties**

* Engine `idempotence_hash` \= SHA-256 over minified+sorted `{release_id,bands,meta}`.  
* `pair_evaluation` stores `a_chart_fingerprint` and `b_chart_fingerprint`; if either snapshot fingerprint changes, pair cache is **stale** and recomputed.  
* On **release change**, charts/pairs are namespaced by the new `release_id`; recompute occurs on access (lazy) unless we backfill.

---

## **7\) Items for further testing & validation**

We will **explicitly test and document** the following before locking this section as final:

1. **Provider version signal**

   * Does the API expose a stable version/ephemeris identifier suitable for `chart_version`?  
   * **Plan:** capture headers/body across multiple days; verify consistency; fall back to `ingest_contract_version` if absent.  
2. **Rate limits & backoff**

   * What are the provider’s rate limits and burst behavior?  
   * **Plan:** controlled load (dev keys) to observe throttle thresholds; confirm backoff windows and max retries.  
3. **FE geocoding vs provider geocoding divergence**

   * With FE-assisted normalized place strings, how often does the provider still reject or reinterpret the location?  
   * **Plan:** table-driven tests with ambiguous locales (e.g., multiple “Springfield”s):  
     * FE-selected normalized place → provider acceptance/rejection → resulting chart differences.  
     * Define BE policy: reject clearly partial inputs upfront; on mismatch, return `422 validation_error` with a **friendly prompt to refine the location** (no provider body leaked).

Great question. Short answer: **store the chart as a single canonical JSON (JSONB) in `chart_snapshot`**. You do **not** need separate tables for centers/channels/gates for the Engine to work. If later you want fast “find users with Gate 10.3”, we can add a small **projection** (view/index or helper table) without touching the Engine.

Here’s the concrete guidance to add to the spec.

---

# **What to store from the Chart (and why)**

## **Tier 1 — Engine-core (required)**

These are the only fields the Engine needs to produce bands/meta. Persist them under a canonical shape we called **ChartV1**:

* **`centers`** — map `{CenterName: "defined"|"open"}`  
* **`channels`** — array of canonical `"NN-NN"` ids (e.g., `"10-20"`, `"57-20"`)  
* **`gates`** — array of `"NN"` or `"NN.L"` strings (e.g., `"10"`, `"10.3"`)  
* **`profile`** — string like `"4/6"` *(optional for Engine, useful for UX later)*  
* **`authority`** — e.g., `"Emotional"` *(optional for Engine, useful for UX later)*

Engine ignores unknown keys, so this can safely be a **superset** of what it reads today.

## **Tier 2 — Deluxe superset (recommended to keep)**

Not required for the Engine, but valuable for future UX/analytics without another API call:

* **`type`**, **`definition`**, **`signature`**, **`not_self`**  
* **`incarnation_cross`**  
* **`activations`** (personality/design gate.line lists)  
* Any provider **variables/motivation** fields you care about

Keeping these in the same JSON makes the DB your “source of truth” for a user’s chart across releases.

## **Provenance pins (mandatory for reproducibility)**

Stored alongside the JSON:

* **`chart_provider`** (e.g., `"HDAPI"`)  
* **`chart_version`** *(if the provider exposes one; else `ingest_contract_version`)*  
* **`chart_fingerprint`** \= `sha256:` of **minified, sorted** `chart_json` (used to validate caches)

---

# **How to store it (DB shape)**

* **Single row per `(user_id, release_id)`** in `chart_snapshot` with one **`chart_json` JSONB** column containing **all** fields above.  
* Add the simple relational columns we already defined: `chart_provider`, `chart_version`/`ingest_contract_version`, `chart_fingerprint`, `computed_at`.

**Why single JSONB?**

* Engine reads **whole charts**—no joins needed.  
* Schema agility: provider adds a field? We store it, fingerprint it, and the Engine still works.  
* Less migration churn; all normalization happens in the BE ingest step.

---

# **Do we ever need separate tables?**

**Not for the Engine.** Only consider projections if you need **fast queries across many users** (e.g., “all users with Channel 10-20”). If/when that shows up, use one of these **add-on** options:

### **Option A — Generated columns \+ indexes (lightweight)**

* Add generated columns with arrays extracted from JSONB (e.g., `channels_short`, `gates_short`).  
* Index them (`GIN` on arrays).  
* Zero duplication logic in app code.

### **Option B — Read-only materialized view (periodic refresh)**

* View that projects `user_id, release_id, channels[], gates[], centers_defined[]`.  
* Index for search.  
* No change to write paths.

### **Option C — Helper table `chart_features` (denormalized)**

* One row per `(user_id, release_id)` with compact bitsets/arrays for gates/channels.  
* Populated in the same transaction as `chart_snapshot` insert (or via background job).  
* Only if you truly need sub-100ms cohort queries at scale.

We **do not** recommend fully normalizing into `user_gates`, `user_channels`, etc. It adds write-time complexity without benefiting the Engine.

---

# **Canonicalization rules (so hashes and queries are stable)**

* **Centers:** canonical names; values strictly `"defined"` or `"open"`.  
* **Channels:** always `"min-max"` (numeric ascending, no leading zeros), de-duplicated, sorted ascending.  
* **Gates:** `"NN"` or `"NN.L"` where `L ∈ [1..6]`, de-duplicated, sorted by `(NN, L)`.  
* **Key order:** when storing and when hashing, use **minified JSON with lexicographically sorted keys** at every level.  
* **Fingerprint:** compute after canonicalization.

---

# **Decision (to put in the doc)**

* **Storage model:** **Single JSONB** per `(user_id, release_id)` in `chart_snapshot`, containing the **Engine-core** fields plus the **Deluxe superset**, with provenance pins and a SHA-256 **`chart_fingerprint`**.  
* **Normalization:** performed once at ingest; the Engine consumes the same canonical JSON.  
* **No separate tables** for centers/channels/gates unless/ until we need cross-user search performance—then add a **projection** (generated columns / view / helper table) without touching Engine contracts.

Great—here’s a concise, implementation-ready **canonicalization map** your BE coder can follow when ingesting a chart from the provider into our **ChartV1** format. It’s written to be robust even if the provider adds extra fields; we only lift what we need and we canonicalize it deterministically.

# **Provider → ChartV1 Canonicalization Map**

Goal: take the **provider chart JSON** and emit a single **`chart_json`** (ChartV1 superset) that the Engine and DB will store under `chart_snapshot.chart_json`.  
 We do **not** touch tz/lat/lon; we do **not** store birth inputs.  
 We compute a **`chart_fingerprint`** over the canonicalized `chart_json`.

## **A) Field mapping table**

| Provider field (path) | Transform / Canonicalization | ChartV1 key | Notes |
| ----- | ----- | ----- | ----- |
| `profile` (string, may be `"4/6"` or `"4-6"`) | Trim; convert `"A-B"` → `"A/B"` | `profile` | Optional for Engine (kept for UX). |
| `authority` (string) | Trim; preserve case as provided | `authority` | Optional for Engine. |
| `centers` (object or array) | **Normalize names** (see list below); values to `"defined"` or `"open"`; **drop anything else** | `centers` (object) | If provider returns an array, convert to `{name: state}`. |
| `channels` (array of ids or objects) | Extract numeric pair; **order ascending** `min-max`; **dedupe**; **sort** ascending | `channels` (array of strings) | Accept inputs like `"20-10"`, `"10–20"`, `{ "id": "10-20" }`. |
| `gates` (array) **and/or** `activations.personality[]`, `activations.design[]` | Emit `"NN"` or `"NN.L"` strings; **merge** personality+design if separate; **dedupe**; **sort** by `(NN, L)` | `gates` (array of strings) | If provider lacks lines, use `"NN"`. If lines exist, prefer `"NN.L"`. |
| (any other provider fields you want to keep, e.g., `type`, `definition`, `signature`, `not_self`, `incarnation_cross`) | Shallow copy (trim strings), do **not** modify semantics | same key names under top level | Safe to keep for product/analytics; ignored by Engine. |
| Provider version signal (header or body) | If present, capture as-is | `chart_version` | If absent, leave null. |
| Our ingest contract descriptor | Literal string, e.g., `"hdapi-v1.bodygraphs"` or `"hdapi-v1.simple"` | `ingest_contract_version` | **Required** if `chart_version` is null. |
| Provider id (static) | Literal `"HDAPI"` | `chart_provider` | Constant. |

### **Center name normalization (exact canonical keys)**

Use exactly these keys; map provider synonyms to them:

* `Head`, `Ajna`, `Throat`, `G`, `Heart` (aka **Ego/Will** → `Heart`), `Spleen`, `Solar Plexus` (aka **Emotional** → `Solar Plexus`), `Sacral`, `Root`.

Any unknown center names → **drop** (and log a validator error for visibility).

---

## **B) Algorithmic rules (determinism)**

1. **Key casing & spacing**

   * Trim all strings; normalize whitespace to single spaces.  
   * Keep provider’s capitalization for user-facing fields (e.g., `authority`), but center **keys** must match the canonical list above.  
2. **Channels**

   * Accept formats: `"10-20"`, `"20-10"`, `"10–20"` (en dash), `{ "id": "10-20" }`.  
   * Extract the two integers; **reorder** to `min-max` (e.g., `"20-10"` → `"10-20"`).  
   * **Deduplicate**; **sort** ascending lexicographically by the `min-max` string.  
3. **Gates**

   * Accept `"NN"` or `"NN.L"` (where `NN` is 1–64 and `L` is 1–6). For objects, pull an `id` string if present.  
   * If provider gives personality/design separately, **merge** both arrays into one set.  
   * **Deduplicate**; **sort** by `(NN, L)`—when `L` missing, treat as `0` for sorting.  
4. **Centers**

   * Convert any boolean/state to exactly `"defined"` or `"open"`. If provider returns `"Undefined"`, map to `"open"` (case-insensitive).  
   * Output object must be **only** the canonical center keys that appeared; no extras; **no nulls**.  
5. **ChartV1 envelope**

   * Include: `release_id`, `centers`, `channels`, `gates`.  
   * Optionally include (kept verbatim after trim): `profile`, `authority`, `type`, `definition`, `signature`, `not_self`, `incarnation_cross`, and a pass-through `activations` object if desired.  
6. **Stable ordering**

   * Before hashing, ensure **lexicographically sorted keys** at every object level (including inside `centers`, `activations`, etc.). Arrays are already sorted by rules above.  
7. **Fingerprinting**

   * `chart_fingerprint = "sha256:" + SHA256(minified_sorted(chart_json))` where `chart_json` is the **post-canonicalization** ChartV1 superset.

---

## **C) Validator checks (fail fast, PII-safe)**

* `centers.*` ∈ `{ "defined", "open" }` only.  
* `channels[*]` matches `^\d{1,2}-\d{1,2}$` and both parts ∈ `[1..64]`.  
* `gates[*]` matches `^\d{1,2}(\.[1-6])?$` and `NN` ∈ `[1..64]`.  
* `profile` (if present) matches `^[1-6]/[1-6]$`.  
* `authority` (if present) non-empty, ≤ 64 chars.  
* No tz/lat/lon fields persisted.

Log validator errors with `correlation_id` and a short code (e.g., `bad_gate_id`), **never** log the full body.

---

## **D) Tiny example (illustrative)**

**Provider (excerpt, shapes may vary)**

{

  "type": "Manifesting Generator",

  "profile": "4-6",

  "authority": "Emotional",

  "centers": { "Throat": "Defined", "G Center": "Undefined", "Sacral": true },

  "channels": \["20-10", {"id":"57-20"}\],

  "activations": {

    "personality": \["10.3","20.5"\],

    "design": \["57.2","10.3"\]

  }

}

**ChartV1 (stored)**

{

  "release\_id": "sha256:\<64hex\>",

  "type": "Manifesting Generator",

  "profile": "4/6",

  "authority": "Emotional",

  "centers": { "Throat": "defined", "G": "open", "Sacral": "defined" },

  "channels": \["10-20", "57-20"\],

  "gates": \["10.3", "20.5", "57.2"\],

  "chart\_provider": "HDAPI",

  "ingest\_contract\_version": "hdapi-v1.bodygraphs",

  "chart\_fingerprint": "sha256:\<64hex\>"

}

*(Note: `"G Center"` → `"G"`, `"Undefined"` → `"open"`, `"4-6"` → `"4/6"`, `"20-10"` → `"10-20"`, merged+deduped gates with line numbers.)*

---

## **E) Implementation checklist (BE ingest)**

1. Parse provider JSON → **strip unknown top-level keys?** *(optional; we usually keep benign extras)*  
2. Canonicalize **centers**, **channels**, **gates** as per rules above.  
3. Normalize `profile`, `authority` (trim; profile dash→slash).  
4. Assemble **ChartV1 superset**; enforce sorted keys and sorted arrays.  
5. Compute **`chart_fingerprint`**.  
6. Persist to `chart_snapshot(user_id, release_id)` with `chart_provider`, `chart_version` (if present) or `ingest_contract_version`.  
7. Invalidate `pair_evaluation` for this user (lazy or eager).  
8. Respond `204` \+ `Cache-Control: no-store`; FE refetches Lake.

---

# **Algorithms & Mathematical Foundations**

This section captures the math we’ve frozen for the HD Engine, focusing on what the engine consumes (ChartV1), what it produces (bands \+ meta), and the scoring pipeline that turns two charts into a small set of interpretable bands. Anything marked **\[to test\]** is an explicit follow-up we’ll exercise with fixtures before we stamp the next release.

---

## **1\) Domains, Weights, Priors**

We score across five conceptual domains; each domain consumes only information present in a chart (centers, channels, gates, profile/authority when relevant). The engine never sees birth inputs or PII.

* **Domains (v1.1)**

  * **Communication (Talk)** — signal for easy exchange, clarity, and “finding words together.”  
  * **Narrative** — alignment in life-story arc and pacing (uses the narrative-only trio).  
  * **Bonding Feel** — warmth/comfort patterns (affective cohesion without prying into PII).  
  * **Action/Voice** — bias toward initiating or voicing action (Motor→Throat dynamics).  
  * **Rhythm** — cadence/synchrony indicators (light-weight; capped to prevent overreach).  
* **Talk-style weights (Communication)**

  * `logic = 1.00`, `insight = 0.70`, `abstract = 0.50`, `existential = 0.45`, `narrative = 0.40`.  
  * **Head penalty**: negative adjustment when only head-center talk exists and **no** shared talk is present (suppressed if any shared talk exists).  
* **Narrative-only set**

  * Trio (v1.1): `01-08`, `13-33`, `31-07` are treated as *narrative carriers*; they do **not** lift Communication directly.  
* **Priors / caps**

  * Each domain has a conservative prior (leaning slightly cool) and a **hard cap** so no single motif dominates global scoring.  
  * Ethics caps apply where a combination could otherwise over-signal intimacy or certainty.

**\[to test\]** Finalize priors per domain using golden fixtures; re-confirm that narrative-only channels are excluded from Talk in all code paths (loaders \+ façade).

---

## **2\) EM Partition & Directional Loads**

We partition “effective material” (EM) to avoid double counting and to respect directionality (A→B vs B→A).

* **Projection split rule**

  * When a feature touches multiple domains, we **push 100% of its EM** into the domains it truly touches. We never assign “both” in a way that exceeds 100% total; global projection sums remain conserved.  
* **Directional loads**

  * We compute **A→B** and **B→A** loads independently for talk/pressure-like features.  
  * **Tilt**: a small, saturating directional advantage (e.g., \+3% per step, max \+9%) applies when A carries connective load *into* B.  
    * **Antisymmetry clamp** ensures `score(A→B) + score(B→A)` remains stable and bounded.

**\[to test\]** Re-exercise antisymmetry under edge cases (all load on one side vs distributed), and confirm EM conservation when a feature maps to multiple domains.

---

## **3\) Q-Bridge (Definition Bridges) & Drive Floor**

**Q-Bridge** estimates the “effort” to bridge the parties’ definitions:

* **Inputs**: each party’s channels/centers/circuits and whether a **voice** (Throat) is reachable together.  
* **Signal**:  
  * **Hops/gaps** to connect A and B into a moving definition.  
  * **Voice presence** (`voice = 0/1`) and **symmetry** (`A`, `B`, or `both`) if both can supply the bridging element.  
  * **Circuit bonus** for compatible circuit participation (kept deliberately small).  
  * **Split salience / relief** if a dominant split is bridged by the other party.

**Drive Floor** is a predicate that guards over-optimistic results:

* **Floor condition (v1.1)**: require either  
  * a **direct Motor→Throat** path present between the pair (`34-20`, `21-45`, `12-22`, `35-36`), **or**  
  * a **shared-to-Throat route** (both can reach Throat together) **and** `Q_bridge ≥ 0.60`.  
* If unmet, we clamp upper bands so the pair cannot read as universally “Warm/Glow” on talk/action despite nice static overlaps.

**\[to test\]** Verify floor behavior on pairs that only share associative head/ajna activity with no route to Throat; re-audit the Motor→Throat list and ensure it’s frozen in the catalog.

---

## **4\) Band Mapping, Windows & Caps**

All domain scores are mapped into four human-readable bands with a deliberately soft mid-zone:

* **Piecewise mapping** with a knee around **6**:  
   values below the knee compress toward **Cool**, the mid-region expands **Open**, and the top plateaus into **Warm/Glow** with gentle slopes (prevents “spiky” jumps).  
* **Windows** (do/don’t-care regions) exist for a small set of well-known tension pairs (e.g., `12-22`, `35-36`, `41-30`, `39-55`), so we neither over-nor under-react.  
* **Caps & clamps**  
  * Domain-specific **hard caps** apply if a prerequisite motif is missing (e.g., no route to Throat ⇒ **Communication** cannot exceed a mid-band).  
  * **Ethics caps** ensure certain intimate motifs cannot lift a band beyond a safe bound alone.

**\[to test\]** Re-plot band curves against synthetic ladders to confirm monotonicity, knee continuity, and cap interactions (no cross-domain leakages).

---

## **5\) End-to-End Scoring Pipeline (At a Glance)**

1. **Canonicalize** charts A/B → sorted, minified internal form (stable hashing).  
2. **Partition** EM by domain; build **directional loads** (A→B, B→A).  
3. **Compute Q-Bridge** meta (hops, voice, symmetry, circuit bonus, relief).  
4. **Apply Drive Floor** predicate → cap or pass.  
5. **Aggregate** domain scores → map to bands via piecewise windows/caps.  
6. **Emit Result**: bands \+ meta \+ `release_id` \+ `idempotence_hash` \+ `duration_ms`.

---

## **6\) Invariants & “Proofs” (Executable)**

We enforce these as property tests and golden fixtures. The engine will fail its own gate if any invariant breaks.

* **Determinism**: identical inputs → byte-identical outputs \+ identical `idempotence_hash`.  
* **Swap symmetry (meta)**: `qbridge.sym` and *non-directional* meta are invariant under A↔B.  
* **Directional antisymmetry (tilt)**: the tilt advantage applied to A→B is mirrored when swapping parties; global totals remain within bounds.  
* **Conservation**: projection split never inflates EM; domain totals stay ≤ 100% of available EM.  
* **Drive-floor safety**: if floor predicate fails, top bands cannot be achieved (verified across fixtures).  
* **No PII**: outputs and logs never echo inputs beyond deterministic hashes and chart-native IDs.  
* **Band monotonicity**: small feature deltas cannot cause large band jumps near the knee.

**\[to test\]**  
 – Re-run “minute-probe” uncertainty around borderline birth times on our *fixture charts only* (we do not use birth in production engine; this validates that Chart→Score is smooth where charts differ trivially).  
 – Validate that FE geocoding reduces partial-place frequency; when partial strings slip through, the BE’s Chart API call must either resolve them deterministically or return a typed validation error without passing ambiguity into the engine.

---

## **7\) What We’ll Re-verify Before Next Freeze (v1.1 → v1.2)**

* **Narrative-only enforcement** across loaders and the façade. **\[to test\]**  
* **Motor→Throat list** is correct and complete for our catalog. **\[to test\]**  
* **Tilt** parameters (step %, saturation) keep antisymmetry within intended bounds. **\[to test\]**  
* **Window/cap interactions** don’t create hidden discontinuities. **\[to test\]**  
* **Q-Bridge threshold (0.60)** remains an accurate “floor” cut after we add new golden pairs. **\[to test\]**

---

## **8\) Ethics Guardrails (Math-Level)**

* No single intimate motif may produce a “Glow” band alone; it must be corroborated by broader communicative structure (Drive Floor \+ caps enforce this).  
* Scoring is **band-only** (no public numerics); internal numerics are used solely for mapping and for test assertions.  
* All thresholds, weights, and caps are **freeze-packed** and versioned under `release_id` for auditability and rollback.

---

## **9\) Implementation Notes (Determinism)**

* All internal structures are **sorted** and **minified** prior to hashing (`idempotence_hash = sha256(stable_json(result))`).  
* Unknown fields in ChartV1 are ignored; strict schema validation runs at the BE when persisting charts, not inside the engine.  
* Every release ships with:  
   (a) **golden chart set**, (b) **golden pair set**, (c) **band plots** for windows/caps, (d) **SYNC\_LOG** of checksums.

---

# **Determinism & Reproducibility**

This section defines exactly how we guarantee “same inputs → same bytes” across time and environments, and how anyone can prove a result came from a specific math release.

---

## **1\) Freeze pack & schemas (single source of math truth)**

**Freeze artifacts (immutable per release):**

* `policy/freeze_pack_*.json` — domains, weights, windows/caps, narrative-only rules, talk-style weights, safety clamps.  
* `catalog/*.json` — canonical reference data (e.g., channels, motor→throat sets).  
* `config/bands_*.json` — band labels and mapping definitions.  
* `config/scoring_config_*.json` *(if present)* — any tunable thresholds/knobs that affect scoring.

**Schemas (authoritative contracts):**

* `ChartV1` JSON Schema — what the Engine can read.  
* `EngineResult` JSON Schema — what the Engine returns.  
* Optional internal schemas for freeze artifacts (so a bad knob can’t ship).

**Rules:**

* Freeze artifacts are **read-only** after release; any change requires a **new release** (new `release_id`).  
* All artifacts and schemas are committed in the repo and validated at startup; boot fails fast on mismatch.

---

## **2\) Stable ordering & byte-identical outputs**

**Canonicalization (inputs and outputs):**

* **Objects:** serialize with **lexicographically sorted keys**, minified JSON, UTF-8, LF newlines.  
* **Arrays:** deterministically sorted:  
  * `channels`: `"min-max"` ascending (numeric).  
  * `gates`: by `(NN, line)` with `line` empty \< `1..6`.  
  * any other arrays explicitly sorted by documented rules.  
* **Strings:** trimmed; normalized whitespace (single spaces).  
* **Numbers:** we avoid floats in public structures (no rounding drift).  
* **Unknown fields:** ignored by Engine; do not affect hashing.

**Idempotence hash (success results):**

* `idempotence_hash = sha256( stable_json({ release_id, bands, meta }) )`  
  * Excludes run-variant fields like `duration_ms`, timestamps, correlation IDs.  
  * `stable_json` \= minified JSON with sorted keys at every level.

**Determinism gates (executable):**

* Golden fixtures for `ChartV1` and pairs assert **byte-identical** results and **unchanged** `idempotence_hash`.  
* AB↔BA invariants: meta symmetry and bounded directional tilt.  
* No-randomness: core uses no RNG; any optional diagnostics must not alter core outputs.

---

## **3\) `release_id` lifecycle**

**Identity:**

* `release_id = sha256( concat( canonical(freeze_pack), canonical(catalogs), canonical(bands), canonical(scoring_config?) ) )`  
  * Each component is canonicalized (sorted/minified JSON) **before** concatenation.  
  * We also publish a human tag `engine_tag` (e.g., `HD-2025.1-YYYYMMDD-<7hex>` where `<7hex>` is the first 7 chars of `release_id`).

**States:**

* **draft** → **candidate (RC)** → **active** → **deprecated**.  
  * **candidate:** all tests/fixtures pass; SYNC\_LOG entry prepared.  
  * **active:** BE sets this `release_id` for production; DB namespaces (`chart_snapshot`, `pair_evaluation`) implicitly follow.  
  * **deprecated:** kept for audit/rollback; not accepted for new computations unless explicitly allowed by ops.

**Acceptance policy (default):**

* BE accepts **exactly one active `release_id`** for compute.  
* (Optional rollback window—accept previous release for a short period—will be decided via ADR before enabling.)

**On change:**

* New `release_id` **does not mutate** prior rows; recomputation happens **lazy** on access (or **eager** by backfill).

---

## **4\) SYNC\_LOG & evidence (provable builds)**

**SYNC\_LOG entry (one per release):**

* Table of components with **filename → SHA-256** (canonicalized content).  
* The **concatenation order** used to compute `release_id`.  
* The resulting **`release_id`** and **`engine_tag`**.  
* Sign-off: “Prepared/approved by Nathan Amthor”, timestamp.

**Locations:**

* **Human change log:** `docs/CHANGELOG.md` — narrative of what changed and why.  
* **SYNC evidence:** `docs/SYNC_LOG.md` — the checksums and identities.  
* **Optional bundle:** `release/<engine_tag>/` — copies of the freeze artifacts used, golden fixtures, and a machine-readable manifest.

**Repro recipe (anyone can verify):**

1. Check out the repo at the tag that corresponds to `engine_tag`.  
2. Verify each artifact’s SHA-256 matches the SYNC\_LOG.  
3. Independently canonicalize \+ concatenate → recompute **`release_id`**; assert equality.  
4. Load the Engine and run the published golden pairs; assert **`idempotence_hash`** and band outputs match exactly.

---

## **5\) Environment pinning (to avoid “it works on my machine”)**

* Toolchain versions are pinned (Python \+ dev tools) and validated at startup via our env check.  
* CI runs the **sanity harness** (lint/type/tests/schema) and writes deterministic artifacts ending with `SANITY: OK`.  
* Any tool bump or schema tweak triggers a new **release** if it can affect outputs; otherwise it’s documented as non-math (dev-only) in the change log.

---

## **6\) What counts as a “math change”**

Any edit that can change `{bands, meta}` for any valid `ChartV1`:

* Freeze weights/windows/caps, narrative-only set, circuit lists, motor→throat set.  
* Catalog content or normalization rules that touch Engine features.  
* Band mapping curves/knees, tilt magnitudes, drive-floor threshold.  
* Any code path that changes canonicalization or EM partition.

**If it can change outputs, it requires a new `release_id`.** Everything else is operational and should **not** alter `idempotence_hash` for given inputs.

---

**Result:** With these rules and artifacts, we can prove—at any later date—that a specific pair result came from a specific math release, and anyone can reproduce the exact bytes from the public repo plus the SYNC evidence.

# **Configuration (Programmatic, Build-time)**

Configuration is **code**. Clients never fetch config at runtime; anything that can change outputs is frozen, hashed, and versioned. Everything else is generated at **build time** with deterministic codegen.

---

## **1\) Freeze files & scoring config (math that affects outputs)**

These artifacts are immutable per release and contribute to `release_id`.

* **`policy/freeze_pack_*.json`**  
   Domains, weights, priors, directional tilt, narrative-only list, safety caps, drive-floor threshold.

* **`catalog/*.json`**  
   Canonical reference (channels, motor→throat, center names).

* **`config/bands_*.json`**  
   Band names and mapping curves/knees.

* **`config/scoring_config_*.json`** *(optional)*  
   Any additional windows/caps or thresholds not in the freeze pack.

**Rules**

* Validated against internal JSON Schemas at build/startup; failure halts the process.  
* Canonicalized (sorted/minified JSON) and hashed; changes require a **new `release_id`**.  
* Never overridden by env vars or flags.

---

## **2\) Field/Enum Registry (single source of truth for product surface)**

A **registry** defines user-facing fields and enums used by FE/BE (“lake” and “writers”). It **does not** change engine math; it governs API surfaces and presentation.

### **2.1 Structure (example)**

{  
  "$schema": "https://glow/registry.schema.json",  
  "version": "2025.1",  
  "fields": \[  
    {  
      "id": "matching.categories",              // dot path in lake response  
      "owner": "BE",  
      "surface": \["lake"\],  
      "type": "array",  
      "items\_enum": \["harmony","drive","communication","balance"\],  
      "exposure": "public",  
      "pii": false  
    },  
    {  
      "id": "matching.engine\_tag",  
      "owner": "BE",  
      "surface": \["lake"\],  
      "type": "string",  
      "pattern": "^HD-\\\\d{4}\\\\.\\\\d-\\\\d{8}-\[0-9a-f\]{7}$",  
      "pii": false  
    },  
    {  
      "id": "writer.birth.time\_precision",  
      "owner": "BE",  
      "surface": \["writer"\],  
      "type": "enum",  
      "enum": \["full","hour","none"\],  
      "pii": false  
    }  
  \]  
}

### **2.2 Codegen rules (deterministic)**

From `registry.json`, generate at build time:

* **FE (TypeScript):**

  * `types/registry.ts`: literal union types, `as const` enums, validators.  
  * Fails build if FE references a non-registry field/enum.  
* **BE (Python):**

  * `glow_registry.py`: `Enum` classes, `TypedDict`/`pydantic` models, compiled regexes.  
  * Fails build if BE exposes a field not in the registry or violates a regex/enum.  
* **Schemas & docs:**

  * Machine JSON Schemas for lake/writer payloads.  
  * Human README with auto-listed fields and owners.

**Determinism**

* Codegen output is formatted with pinned formatters, stable field ordering (lexicographic), and checked into source to keep builds auditable.

**What triggers failure**

* FE/BE import of an enum value not in registry.  
* Attempt to add/remove fields without modifying the registry.  
* Registry version change without bumping doc version (2025.1 → …).

---

## **3\) No runtime client config**

* **Clients (FE)** never call `/config` or similar.  
* All needed constants/enums are bundled at build time via codegen.  
* Runtime toggles visible to users are derived from **server state** (lake), not client config files.

---

## **4\) Emergency switches (server-side only, non-math)**

Allowed **only** for operational safety; must **not** alter engine outputs.

* **Examples**

  * `ENGINE_ADAPTER_MODE = {http, library}` (dev ops only).  
  * `DISABLE_MATCH_WRITER = true` (temporarily blocks new matches).  
  * `ENGINE_TIMEOUT_MS` (caps HTTP adapter timeout in dev/staging).  
  * `LAKE_INCLUDE_DEBUG = false` (never ships PII; controls inclusion of harmless diagnostics).  
* **Prohibited**

  * Any env that changes weights, caps, windows, or band curves.  
  * Any flag that changes canonicalization (sorting/normalization).  
  * Any knob that changes `ChartV1` semantics.

**Policy**

* Emergency switches live in **BE env** (Railway) with documented defaults.  
* Changing a switch does not change `release_id`.  
* Every toggle has a runbook line and is audited in logs (key only, no values that imply PII).

---

## **5\) Build & validation pipeline (summary)**

1. **Validate** registry, freeze files, catalogs, bands, scoring\_config against schemas.  
2. **Codegen** FE/BE artifacts from the registry (deterministic).  
3. **Compute** component SHA-256s → compose **`release_id`** and `engine_tag`.  
4. **Run sanity**: lint/type/tests plus schema round-trip; write `SANITY: OK` artifacts.  
5. **Fail fast** if: schema mismatch, codegen drift, unpinned tool versions, or non-deterministic output.

---

## **6\) What requires a new `release_id` vs not**

* **Requires new `release_id`:** any edit to freeze files, catalogs, bands, scoring\_config; anything that can change `{bands, meta}`.  
* **Does not require new `release_id`:** registry changes (fields/enums), FE copy, BE lake/writer shapes (so long as engine outputs are unchanged), emergency switch defaults.

---

**Result:** Config is **programmatic, reproducible, and auditable**. Engine math stays frozen; FE/BE surfaces stay consistent via a single registry with deterministic codegen. No client-side runtime configuration, and only narrowly scoped server-side toggles for operational safety.

# **Integration with Glow App**

This section is the **authoritative contract** for how the Engine plugs into Glow in **production** and **dev/staging**. It locks headers, envelopes, retry rules, and performance limits. Where something is still TBD by infrastructure, I call it out explicitly.

---

## **1\) Production mode — in-process library (charts-in → scores-out)**

**Caller:** Glow Backend (Flask/Gunicorn on Railway).  
 **Boundary:** Function call inside the BE worker process (no HTTP, no network).

**Public function**

* `compute_pair(chart_a: ChartV1, chart_b: ChartV1, release_id: str, *, diagnostics: bool=False) -> Result`

**Inputs**

* `chart_a`, `chart_b`: canonical ChartV1 (from `chart_snapshot`); **no birth/timezone/PII**.  
* `release_id`: the active math release (BE supplies).  
* `diagnostics`: default `False`; when `True`, meta may include extra non-PII toggles for ops. Never includes WHY text.

**Output (`Result`)**

* `{ ok:true, release_id, bands, meta, idempotence_hash, duration_ms }`  
* Deterministic: same inputs → **byte-identical** `{bands, meta}` and **same** `idempotence_hash`.

**Error surface (library)**

* The library **raises typed exceptions**; BE **must** map them to its canonical envelope for clients:  
  * `ValidationError` → 400 / `{error:"validation_error"}`  
  * `UnsupportedReleaseError` → 409 / `{error:"unsupported_release"}`  
  * (Internal faults) `EngineInternalError` → 500 / `{error:"internal_error"}`  
* Library does **not** do retries; there’s nothing to retry in-proc. BE handles caching (see below).

**BE call pattern (production)**

1. Load `chart_snapshot` for A & B by **active `release_id`**.  
2. Check `pair_evaluation(min(A),max(B),release_id)`:  
   * If **present** and `a_chart_fingerprint`/`b_chart_fingerprint` match current snapshots → **return cached**.  
   * Else `compute_pair()` → **upsert** row with new result \+ fingerprints → return.  
3. Surface **bands-only** summary (plus `engine_tag`) to the Lake. Do **not** leak raw `meta` to the SPA.

**Performance targets (prod library)**

* Engine p95 ≤ **400 ms**, p99 ≤ **800 ms** (per call, within a BE worker).  
* Start-of-day safe throughput: **\~50 rps** aggregated across workers (increase with horizontal scale).  
* No body size limits internally (inputs are in-memory dicts); **ChartV1** should remain small (\<10 KB typical).

**Security**

* Library never touches network/DB/FS; no PII; no secrets.  
* Deterministic hashing; `Cache-Control: no-store` is enforced **by BE** on any response that includes Engine data.

---

## **2\) Dev/Staging mode — internal HTTP adapter**

**Purpose:** local dev, CI smoke, incident isolation. **Never** exposed to the public Internet.

**Endpoint**

* `POST /internal/engine/v1/evaluate`

**Required headers**

* `Content-Type: application/json`  
* `Accept: application/json`  
* `Cache-Control: no-store`  
* `X-Correlation-Id: <uuid>` (adapter **echoes** this)  
* *(Optional)* `Idempotency-Key: <opaque>` (adapter echoes; no server-side persistence in Engine)

**Body (two allowed shapes; pick one per environment)**

* **Prod-like** (preferred):  
   `{ "release_id": "...", "a_chart": <ChartV1>, "b_chart": <ChartV1>, "diagnostics": false }`  
* **Dev convenience** (if you wire it):  
   `{ "release_id": "...", "a": { "birth": {...} }, "b": { "birth": {...} } }`  
   *(dev harness fetches charts; **never** used in production.)*

**Responses**

* **200** `{ ok:true, release_id, bands, meta, idempotence_hash, duration_ms, correlation_id }`  
* **Typed errors** (no PII):  
  * **400** `{ ok:false, code:"validation_error", ... }`  
  * **409** `{ ok:false, code:"unsupported_release", ... }`  
  * **413** `{ ok:false, code:"payload_too_large", ... }`  
  * **504** `{ ok:false, code:"compute_timeout", ... }`  
  * **429** `{ ok:false, code:"rate_limited", ... }` *(if you enable a dev-only limiter)*  
  * **500** `{ ok:false, code:"internal_error", ... }`

**Adapter limits & retries**

* **Body size cap:** **≤ 64 KB** request & response.  
* **Timeout:** **3000 ms** per request.  
* **Retry policy (caller \= BE only):** **1 retry** on 5xx or timeout; **no retries** on 4xx.  
* Always send/propagate `X-Correlation-Id`; always set `Cache-Control: no-store`.

**Aux endpoints (dev only)**

* `GET /internal/healthz` (lightweight)  
* `GET /internal/readyz` (freeze loaded)  
* `GET /internal/version` (`{release_id, engine_tag, checksums?}`)

---

## **3\) Common contract — headers, errors, retries**

**Headers (must)**

* `X-Correlation-Id`: generated by FE; echoed by BE and Engine (HTTP mode).  
* `Cache-Control: no-store`: on any Engine JSON surfaced to clients.  
* **No** CSRF/Authorization in Engine HTTP adapter (it is **internal**). CSRF remains **BE-only**.

**Error model (canonical codes)**

* `validation_error` — bad ChartV1 or dev birth payload.  
* `unsupported_release` — `release_id` not recognized/loaded.  
* `payload_too_large` — request exceeds 64 KB (HTTP mode only).  
* `compute_timeout` — exceeded adapter timeout (HTTP mode only).  
* `rate_limited` — adapter’s dev limiter (optional).  
* `internal_error` — unexpected fault.

In production, the **library raises exceptions** and the BE maps to its standard envelope (e.g., `{ok:false, code, error}`) before returning to FE.

**Retry rules**

* **Library (prod):** no retries inside Engine; BE **does not retry** exceptions—fix inputs or fall back to cached pair if policy allows.  
* **HTTP (dev/staging):** exactly **one retry** on 5xx/timeout; no retries on 4xx.

---

## **4\) Integration checklist (BE)**

1. **Active release**: store/get the active `release_id`; pass it to both chart lookups and `compute_pair()`.  
2. **Load charts**: fetch `chart_snapshot` for A & B (same `release_id`); if missing/stale, (a) call Chart API to refresh snapshot, then (b) proceed.  
3. **Cache check**: read `pair_evaluation(min,max,release_id)`; validate fingerprints against snapshots.  
4. **Compute** (if miss/stale): call `compute_pair()`; upsert result with `idempotence_hash` \+ fingerprints.  
5. **Lake**: respond with **bands-only** summary \+ `engine_tag`.  
6. **Headers**: ensure `Cache-Control: no-store` and `X-Correlation-Id` are on the client response.  
7. **Logging**: structured, keys-only (route, `release_id`, `correlation_id`, `duration_ms`, `ok`, `code`). Never log bodies/PII.

---

## **5\) Performance SLOs & limits (Engine integration)**

**Library (production)**

* **SLO:** p95 ≤ **400 ms**, p99 ≤ **800 ms** per pair compute.  
* **Concurrency:** governed by Gunicorn workers; the library is CPU-bound and **single-threaded** per call.  
* **Cache hit goal:** ≥ **80%** on steady traffic (with pair\_evaluation).  
* **Memory:** inputs/outputs are small; Engine keeps only frozen artifacts in memory.

**HTTP adapter (dev/staging)**

* **Request/response size:** ≤ **64 KB**.  
* **Timeout:** **3000 ms**; **1 retry** on 5xx/timeout.  
* **QPS:** modest (CI smoke, local dev). Use BE rate-limit if you open it to a team network.

**Unknowns to confirm (does not block)**

* Gunicorn **worker count** & **worker timeout** in Railway.  
* BE **body-size caps** and compression policy.  
* Expected **concurrency/throughput** targets at launch.  
   *(Once you provide these, I’ll lock them here and, if needed, tune adapter limits.)*

---

## **6\) Security posture**

* Engine never sees birth/timezone/PII; only charts.  
* Engine HTTP adapter is **internal only** (private network / auth gate if needed in staging).  
* All Engine JSON sent toward clients carries `Cache-Control: no-store`.  
* Secrets (Chart API keys) live in **BE** env; never in Engine.

---

**Bottom line:**

* **Production \= library call** from BE with two stored charts and the active `release_id`; results cached in `pair_evaluation`.  
* **Dev/Staging \= internal HTTP** with strict headers, limits, and one-retry policy for ops convenience.  
   Both paths share the **same envelopes and determinism guarantees**, so we can swap modes without changing outcomes.

# **FE/BE Contracts (Lake & Writers)**

This section locks the **client–server contract**: one **Lake** read surface for the SPA, a handful of **Writers** (mutations), strict headers, and FE behavior for errors. It follows our “bands-only to clients” rule and the “write → refetch Lake” model.

---

## **1\) Lake response shape (bands-only \+ `engine_tag`)**

**Endpoint (example):** `GET /api/auth/me`  
 **Cache:** `Cache-Control: no-store`  
 **Headers (BE → FE):** echoes `X-Correlation-Id`

### **1.1 JSON (authoritative, minimal)**

{  
  "ok": true,  
  "user": {  
    "id": "u\_123",  
    "email\_verified": true  
  },  
  "matching": {  
    "categories": \[  
      { "id": "harmony",       "band": "Warm" },  
      { "id": "communication", "band": "Open" },  
      { "id": "drive",         "band": "Cool" }  
    \],  
    "top3\_shared": \["harmony","communication","drive"\],  
    "eligible": true,  
    "prompt": "A short, human line.",  
    "engine\_tag": "HD-2025.1-20250923-1a2b3c4"  
  },  
  "server\_time": "2025-09-23T20:05:12Z",  
  "correlation\_id": "b7c1…"  
}

**Notes**

* Lake **never** includes raw Engine WHY/debug. Bands-only \+ `engine_tag`.  
* If a pair context is present (e.g., viewing another profile), BE may return that pair’s **bands-only** under a sibling object (same schema), but **still no meta** to the SPA.  
* All identifiers/enums must come from the **Field/Enum Registry** (build-time codegen).

---

## **2\) Writers pattern (204 \+ `no-store`, then Lake refetch)**

**General rule:** Writers are **small and idempotent**. They **do the work** server-side, return **no body**, then FE **refetches Lake** to render the updated state.

**Headers (FE → BE, required)**

* `Content-Type: application/json`  
* `Accept: application/json`  
* `X-CSRF-Token: <from glow_csrf cookie>`  
* `X-Correlation-Id: <uuid-v4>`

**Response (BE → FE)**

* `204 No Content`  
* `Cache-Control: no-store`  
* Echo `X-Correlation-Id`

### **2.1 Writer: Update birth data**

**Request**

PUT /api/me/birth

{  
  "birth\_date": "1990-01-01",  
  "birth\_time\_local": "14:30",         // nullable if time\_precision \!= "full"  
  "time\_precision": "full",            // enum: "full"|"hour"|"none"  
  "place\_text": "Tallinn, Estonia"     // FE-normalized place string  
}

**Response**

204 No Content  
Cache-Control: no-store

**FE behavior**

1. Submit writer.  
2. On `204`, immediately **refetch Lake**.  
3. Render from Lake only.

### **2.2 Writer: Connect/Disconnect (example)**

POST /api/me/connect  
{ "target\_user\_id": "u\_987" }

DELETE /api/me/connect  
{ "target\_user\_id": "u\_987" }

* Same headers/response pattern.  
* FE refetches Lake afterward.

Engine computations (chart compute on write, pair compute on demand) run **inside BE**. Writers never return Engine results directly.

---

## **3\) Typed errors & FE handling**

All BE responses include `X-Correlation-Id` for support. FE must read it and surface a friendly, **non-PII** message.

### **3.1 Error envelope (BE → FE)**

{  
  "ok": false,  
  "error": "validation\_error",  
  "message": "Please check your inputs.",  
  "retry\_after\_ms": 0,  
  "correlation\_id": "b7c1…"  
}

### **3.2 Status mapping & UX rules**

| HTTP | `error` | When it happens (examples) | FE behavior (must) |
| ----- | ----- | ----- | ----- |
| 400 | `bad_request` | Malformed JSON; missing required field | Show inline form error; do **not** retry |
| 401 | `unauthorized` | Session expired | Redirect to login; preserve return path |
| 403 | `csrf_violation` | CSRF check failed | **Rotate CSRF once** → retry request once; if still 403, show friendly “please refresh” |
| 403 | `forbidden` | Auth OK but not allowed | Show “not allowed”; do not retry |
| 404 | `not_found` | Route or resource | Show generic not-found |
| 409 | `conflict` | Version conflict, e.g., stale write | Refetch Lake; let user retry after |
| 422 | `validation_error` | Invalid birth fields / ambiguous `place_text` | Highlight fields; show actionable copy |
| 429 | `rate_limited` | Too many requests | Read `retry_after_ms`; backoff; show gentle limiter |
| 500 | `internal_error` | Unexpected server fault | Show “Something broke”; **do not** auto-retry writers |
| 502/503/504 | `upstream_*` | Chart API outage, provider auth, timeout | Friendly outage message; optional “try again” after a short delay |

**Special cases**

* **429**: FE must **respect `retry_after_ms`** (if present). No hammering.  
* **CSRF 403**: FE regenerates token once, retries the writer **once**, then stops.  
* **Upstream errors**: FE should *not* expose provider details; just show a plain outage message.

---

## **4\) FE fetch wrapper (single source of truth)**

The SPA uses one wrapper so all calls behave consistently.

* Adds `X-Correlation-Id` per request (UUID v4).  
* Reads `glow_csrf` cookie; sets `X-CSRF-Token` on writers.  
* On writer success (`204` or `200 {"status":"ok"}`): **refetch Lake** and render from it.  
* Centralized error handling with the table above; logs the `correlation_id` for support.  
* Disallows optimistic UI for writers that affect Engine-visible state.

*Pseudologic*

try writer()  
  if 204: refetchLake()  
catch 403 csrf\_violation:  
  rotateCsrfOnce()  
  retry writer once  
  if still 403: show refresh prompt  
catch 429:  
  wait retry\_after\_ms (if any), then let user retry  
catch 5xx:  
  show friendly error; do not auto-retry writer

---

## **5\) Headers & limits (recap)**

* **Always send:** `X-Correlation-Id`.  
* **Writers send:** `X-CSRF-Token` (double-submit), `Content-Type: application/json`.  
* **All sensitive JSON (Lake & writers):** `Cache-Control: no-store`.  
* **Dev HTTP adapter (if used by BE):** body ≤ **64 KB**, timeout **3 s**, at most **1 retry** on 5xx/timeout.

---

## **6\) Contract guarantees**

* Lake is the **only** FE read for Engine-derived state.  
* Writers **never** return Engine results; FE refetches Lake.  
* Bands-only to clients; `engine_tag` identifies the math release; no raw meta/WHY in SPA.  
* Determinism and privacy are preserved: **no PII** from Engine, **no caching** of sensitive JSON in clients.

If you want, I can generate **schemas** for the Lake and the two writer payloads above (JSON Schema 2020-12) so FE/BE can validate at build time.

Awesome—here are **ready-to-drop JSON Schemas (2020-12)** for the Lake and the two Writers we defined. I’ve also included the **shared Error envelope** schema FE can use for centralized handling.

---

# **1\) Lake response schema (bands-only \+ `engine_tag`)**

**File:** `schemas/lake.response.schema.json`

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/schemas/lake.response.schema.json",  
  "title": "LakeResponse",  
  "type": "object",  
  "required": \["ok", "user", "matching", "server\_time", "correlation\_id"\],  
  "additionalProperties": false,  
  "properties": {  
    "ok": { "type": "boolean", "const": true },  
    "user": {  
      "type": "object",  
      "required": \["id", "email\_verified"\],  
      "additionalProperties": true,  
      "properties": {  
        "id": { "type": "string", "minLength": 1, "maxLength": 128 },  
        "email\_verified": { "type": "boolean" }  
      }  
    },  
    "matching": {  
      "type": "object",  
      "required": \["categories", "eligible", "engine\_tag"\],  
      "additionalProperties": false,  
      "properties": {  
        "categories": {  
          "type": "array",  
          "minItems": 1,  
          "items": {  
            "type": "object",  
            "required": \["id", "band"\],  
            "additionalProperties": false,  
            "properties": {  
              "id": {  
                "type": "string",  
                "pattern": "^\[a-z\]\[a-z0-9\_\]{1,31}$"  
              },  
              "band": {  
                "type": "string",  
                "minLength": 1,  
                "maxLength": 32  
              }  
            }  
          }  
        },  
        "top3\_shared": {  
          "type": "array",  
          "items": { "type": "string", "pattern": "^\[a-z\]\[a-z0-9\_\]{1,31}$" },  
          "uniqueItems": true  
        },  
        "eligible": { "type": "boolean" },  
        "prompt": { "type": "string", "maxLength": 280 },  
        "engine\_tag": {  
          "type": "string",  
          "pattern": "^HD-\\\\d{4}\\\\.\\\\d-\\\\d{8}-\[0-9a-f\]{7}$"  
        }  
      }  
    },  
    "server\_time": { "type": "string", "format": "date-time" },  
    "correlation\_id": { "type": "string", "minLength": 1, "maxLength": 128 }  
  }  
}

---

# **2\) Writer: Update birth data (request)**

**File:** `schemas/writer.birth.update.request.schema.json`

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/schemas/writer.birth.update.request.schema.json",  
  "title": "WriterBirthUpdateRequest",  
  "type": "object",  
  "required": \["birth\_date", "time\_precision", "place\_text"\],  
  "additionalProperties": false,  
  "properties": {  
    "birth\_date": {  
      "type": "string",  
      "pattern": "^\\\\d{4}-\\\\d{2}-\\\\d{2}$"  
    },  
    "birth\_time\_local": {  
      "type": "string",  
      "pattern": "^\\\\d{2}:\\\\d{2}(:\\\\d{2})?$"  
    },  
    "time\_precision": {  
      "type": "string",  
      "enum": \["full", "hour", "none"\]  
    },  
    "place\_text": {  
      "type": "string",  
      "minLength": 2,  
      "maxLength": 128  
    }  
  },  
  "allOf": \[  
    {  
      "if": { "properties": { "time\_precision": { "const": "full" } } },  
      "then": { "required": \["birth\_time\_local"\] }  
    },  
    {  
      "if": { "properties": { "time\_precision": { "const": "hour" } } },  
      "then": {  
        "properties": {  
          "birth\_time\_local": { "pattern": "^\\\\d{2}:00(:00)?$" }  
        }  
      }  
    },  
    {  
      "if": { "properties": { "time\_precision": { "const": "none" } } },  
      "then": {  
        "not": { "required": \["birth\_time\_local"\] }  
      }  
    }  
  \]  
}

**Response:** HTTP **204 No Content** with `Cache-Control: no-store` (no body schema).

---

# **3\) Writer: Connect / Disconnect (request)**

**File:** `schemas/writer.connect.request.schema.json`

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/schemas/writer.connect.request.schema.json",  
  "title": "WriterConnectRequest",  
  "type": "object",  
  "required": \["target\_user\_id"\],  
  "additionalProperties": false,  
  "properties": {  
    "target\_user\_id": {  
      "type": "string",  
      "pattern": "^\[A-Za-z0-9\_-\]{3,64}$"  
    }  
  }  
}

**Response:** HTTP **204 No Content** with `Cache-Control: no-store` (no body schema).  
 *(Use the same schema for `POST /api/me/connect` and `DELETE /api/me/connect`.)*

---

# **4\) Shared Error envelope (for FE handling)**

**File:** `schemas/error.envelope.schema.json`

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "https://glow/schemas/error.envelope.schema.json",  
  "title": "ErrorEnvelope",  
  "type": "object",  
  "required": \["ok", "error", "message", "correlation\_id"\],  
  "additionalProperties": false,  
  "properties": {  
    "ok": { "type": "boolean", "const": false },  
    "error": {  
      "type": "string",  
      "enum": \[  
        "bad\_request",  
        "unauthorized",  
        "csrf\_violation",  
        "forbidden",  
        "not\_found",  
        "conflict",  
        "validation\_error",  
        "rate\_limited",  
        "internal\_error",  
        "upstream\_auth",  
        "upstream\_route",  
        "upstream\_error",  
        "upstream\_timeout"  
      \]  
    },  
    "message": { "type": "string", "minLength": 1, "maxLength": 280 },  
    "retry\_after\_ms": { "type": "integer", "minimum": 0 },  
    "correlation\_id": { "type": "string", "minLength": 1, "maxLength": 128 }  
  }  
}

---

## **Integration notes (build/validation)**

* Add these files under `schemas/` and wire them into your **build-time validation** (BE: `jsonschema`; FE: codegen to TypeScript types if desired).  
* Lake categories (`matching.categories[*].id`) and bands should align with the **Field/Enum Registry**; you can tighten the schema by generating an **enum** there and referencing it here if you want stricter validation.  
* Writers always return **204 \+ `Cache-Control: no-store`** on success; the SPA **must refetch Lake** afterward.

# **Observability & Operations**

This section sets **clear intentions and requirements** so we build the right rails as we go. It’s opinionated, privacy-first, and lightweight enough to implement quickly.

---

## **1\) Objectives (non-negotiable)**

* **Privacy:** no bodies/PII in logs or traces. Keys only.  
* **Traceability:** every request carries a **Correlation ID** end-to-end.  
* **Actionable signals:** a small set of SLIs/SLOs, few but meaningful alerts.  
* **Determinism evidence:** version (`engine_tag`, `release_id`) visible in logs and `/internal/version`.

---

## **2\) Logging Policy (structured, keys-only)**

**Format:** newline-delimited JSON (NDJSON).  
 **Level taxonomy:** `DEBUG` (dev), `INFO` (normal), `WARN`, `ERROR`, `FATAL` (crash).

**Required fields per log line**

ts, level, service, route|func, phase, correlation\_id,

release\_id, engine\_tag?, duration\_ms?, ok, code?,

user\_id? (hashed), pair\_key? (hashed), msg

* `service`: `fe`, `be`, `engine`, `adapter`, `job`.  
* `phase`: `request_in`, `engine_compute`, `db_query`, `response_out`, `background_job`.  
* `code`: error code on failures (e.g., `validation_error`, `upstream_error`).  
* `user_id` / `pair_key`: **hashed** (e.g., `sha256:user_123` or `sha256:min:max`)—no raw IDs in general logs.

**Never log**

* Request/response bodies, birth data, place text, chart JSON, secrets, cookies, CSRF tokens.

**Sampling**

* `INFO` full, `DEBUG` off in prod, error logs unsampled.

**Retention (ops placeholder)**

* App logs: **14 days** (bump to 30 if cost allows).  
* Access to logs gated; redact exports by default.

---

## **3\) Correlation IDs**

**Generation:** FE creates `X-Correlation-Id` (UUIDv4) per user action.  
 **Propagation:** FE → BE (request) → Engine (HTTP mode) → BE (response).  
 **Echo:** BE and Engine **echo** the ID in responses/adapter replies.  
 **Storage:** field `correlation_id` appears in logs, error envelopes, and (if needed) pair\_evaluation ops audit.

**Rule:** if missing, BE generates one and adds `X-Correlation-Id` to the response.

---

## **4\) Metrics (SLIs) & SLOs**

**Cardinal rule:** few, useful metrics with clear owners.

### **4.1 Engine / Matching**

* `engine_compute_seconds` — histogram (p50/p95/p99). **SLO:** p95 ≤ **400 ms**, p99 ≤ **800 ms**.  
* `engine_requests_total` — by `ok`, `code`.  
* `engine_cache_hit_ratio` — `pair_evaluation` hits / total. **Target:** ≥ **0.80** steady state.  
* `engine_errors_total` — by `code` (alert on sudden spikes).

### **4.2 BE / API**

* `writer_success_total` / `writer_failure_total` — by route & code.  
* `lake_latency_seconds` — histogram (p50/p95).  
* `csrf_violation_total`, `rate_limited_total`.

### **4.3 DB/Infra (Railway/Postgres/Redis)**

* `db_pool_in_use`, `db_latency_seconds` (p95).  
* `redis_ops_total`, `redis_latency_seconds`.

**Alerts (initial)**

* p95 `engine_compute_seconds` \> **600 ms** for 5 min (WARN), \> **900 ms** (PAGE).  
* `engine_errors_total{code="internal_error"}` \> **5/min** for 5 min (PAGE).  
* `engine_cache_hit_ratio` \< **0.5** for 15 min (WARN → investigate invalidation storm).  
* `lake_5xx_rate` \> **1%** for 10 min (PAGE).

---

## **5\) Tracing**

**Standard:** W3C `traceparent`/`tracestate` (optional now, plan to add).  
 **Spans to capture**

* BE request span (route).  
* DB query spans (aggregate, no SQL text).  
* Engine compute span (library call) with tags: `release_id`, `engine_tag`, `duration_ms`, `ok`, `code`.  
   **No bodies** in trace attributes.  
   **Correlation bridge:** `correlation_id` added as trace attribute for cross-tool joins.

---

## **6\) Health/Ready/Version (HTTP adapter only)**

* `GET /internal/healthz` → `200 {"ok":true}`  
  * Lightweight: process alive, event loop healthy.  
* `GET /internal/readyz` → `200 {"ok":true,"release_id":"…","freeze_loaded":true}`  
  * Verifies freeze pack & catalogs loaded and passes schema checks.  
* `GET /internal/version` → `200 {"release_id":"…","engine_tag":"…","components":[{"name":"freeze_pack","sha256":"…"},…]}`

**Headers:** `Cache-Control: no-store`.  
 **Security:** adapter is **internal**; gate with network policy or shared secret in staging if exposed.

---

## **7\) Runbooks & Incident Basics**

### **7.1 Severity levels**

* **SEV1**: user-visible outage (lake 5xx\>1% or login/critical writers failing).  
* **SEV2**: partial degradation (cache hit collapse, p95 latency breach).  
* **SEV3**: nuisance (single route noisy errors).

### **7.2 First 10 minutes (checklist)**

1. Confirm **SEV** & page owner (Nathan for now).  
2. Grab a **recent `correlation_id`** from a failing request.  
3. Check dashboards: lake 5xx, engine latency, cache hit, DB health.  
4. If Engine regression suspected: `GET /internal/version` to confirm `release_id`.  
5. **Mitigations:**  
   * If writer path failing due to provider: return `503 upstream_*` quickly; pause retries.  
   * If pair cache storm: temporarily **disable match writer** and raise DB pool.  
   * If adapter flapping: **switch to library only** path for affected env.

### **7.3 Rollback**

* **FE (Vercel):** revert to last good deployment.  
* **BE (Railway):** redeploy last known good image; confirm health.  
* **Engine math:** if needed, set BE **active `release_id`** back to previous (lazy recompute on access).

### **7.4 Communication**

* In-product banner (optional) for SEV1.  
* Note `correlation_id` in support replies; never share internals.

### **7.5 Post-incident (24–72h)**

* Write a **brief retro**: timeline, impact, root cause, fix, follow-ups.  
* Capture any config/infra changes in ADRs or ops docs.

---

## **8\) Operational Tests (we bake these into CI or a weekly job)**

* **Canary lake check**: 1/min synthetic request validates 200 \+ `engine_tag` present.  
* **Engine compute smoke**: run a golden pair via library; assert `idempotence_hash`.  
* **Cache behavior**: create a pair, edit one chart, ensure cache invalidates (hit ratio dip then recover).  
* **Headers discipline**: assert `Cache-Control: no-store` on Lake & writers; assert `X-Correlation-Id` echo.  
* **Adapter endpoints** (if running): `healthz/readyz/version` return within 50 ms.

---

## **9\) Ops Toggles (server-side, non-math)**

* `ENGINE_ADAPTER_MODE` \= `library` | `http` *(env: staging/dev only)*  
* `DISABLE_MATCH_WRITER` \= `false` *(guard during storms)*  
* `ENGINE_HTTP_TIMEOUT_MS` \= `3000` *(dev adapter)*  
* `ENGINE_HTTP_BODY_LIMIT` \= `65536` bytes

Toggles must not change math outputs; changes are logged (keys-only).

---

## **10\) Dashboards (initial)**

* **Overview:** Lake 2xx/4xx/5xx; p95 latency; `engine_cache_hit_ratio`; engine p95/p99.  
* **Errors:** top `code` by count; recent `correlation_id`s.  
* **DB/Redis:** pool usage, p95 query time; Redis ops/latency.

---

## **11\) Data & Privacy**

* Logs contain **no PII**; hashed identifiers only.  
* `Cache-Control: no-store` on all sensitive JSON.  
* Respect deletion requests: exclude soft-deleted users from new computations; stop logging their hashed IDs going forward.

---

### **Acceptance (we’re “observability-ready” when)**

* \[ \] Logs ship as structured JSON; redaction policy enforced.  
* \[ \] Correlation ID appears in FE, BE, Engine (HTTP) and error envelopes.  
* \[ \] Metrics and three alerts (latency, 5xx, engine internal errors) live.  
* \[ \] Adapter health/ready/version respond correctly (if enabled).  
* \[ \] Runbook exists with rollback steps and toggles documented.

This gives us a tight, privacy-respecting ops surface that’s easy to build now and extend later.

# **Testing & Quality Gates (2025.1)**

This section defines what “good” looks like at the command line and in CI. All tools are **pinned** for 2025.1 (pytest 7.4.x, ruff 0.5.x, mypy 1.10.x). Any change that can affect outputs is a **math change** and requires a new `release_id`.

---

## **1\) Test taxonomy**

* **Unit tests (fast, pure)**

  * Scope: partitioning, directional loads, Q-bridge, drive floor, band mapping.  
  * Rules: no I/O, no network, ≤50 ms/test typical.  
* **Golden fixtures (determinism proofs)**

  * Canonical charts and pairs (ChartV1 in, bands/meta out).  
  * Assert **byte-identical** `{bands, meta}` and unchanged `idempotence_hash`.  
* **Property tests**

  * AB↔BA invariants (meta symmetry; bounded directional tilt).  
  * EM conservation (projection never \>100%).  
  * Band mapping monotonicity (no “cliffs” near the knee).  
  * Drive-floor predicate enforcement.  
* **Schema tests**

  * Validate ChartV1 and Result envelopes.  
  * Validate freeze artifacts (freeze pack, catalogs, bands, scoring\_config) against their schemas.  
* **Adapter tests (dev HTTP mode only)**

  * `healthz/readyz/version` shape.  
  * 64 KB body cap → `payload_too_large`.  
  * Timeout path → `compute_timeout` (no PII).

---

## **2\) Fixtures & layout (authoritative)**

testdata/  
  golden/  
    charts/                 \# canonical ChartV1s  
    pairs/                  \# { a, b, release\_id, expected\_hash }  
  schemas/                  \# \*.schema.json (ChartV1, Result, freeze, bands)  
tests/  
  unit/                     \# pure math  
  golden/                   \# byte+hash assertions over pairs  
  props/                    \# invariants/properties  
  schemas/                  \# schema conformance  
adapter\_tests/              \# only when HTTP adapter runs

* All JSON fixtures use **lexicographic key order**, minified, LF newlines.  
* Golden pair files record the expected `idempotence_hash` for the active `release_id`.

---

## **3\) Idempotence & byte-stability checks**

* **Stable serialization:** objects with lexicographically sorted keys; arrays sorted by documented rules (channels `min-max`, gates by `(NN, line)`).  
* **Hash definition:**  
   `idempotence_hash = sha256( stable_json({ release_id, bands, meta }) )`  
   (excludes run-variant fields like `duration_ms`).  
* **Assertions:** per golden pair:  
  * exact byte equality for `bands` and `meta`,  
  * `idempotence_hash` equality,  
  * AB↔BA symmetry constraints hold.

---

## **4\) Lint, type, security scanning**

* **ruff**: no new warnings on changed lines; `noqa` requires inline justification.  
* **mypy**: clean types across `hd_core/**` and `policy/**`; no `Any` leakage on public interfaces.  
* **Secrets scan**: regex \+ entropy; fail build on confirmed secret.  
* **(Optional) package audit**: report-only; pins govern actual risk.

---

## **5\) Sanity script & deterministic artifacts**

A single runner proves the build and emits evidence.

* **Sanity runner responsibilities**  
  * Assert tool **pins** (python/pip/pytest/ruff/mypy).  
  * Run ruff \+ mypy.  
  * Run unit \+ schema tests.  
  * Run golden tests.  
  * Compute and print `release_id` and `engine_tag`.  
  * Emit artifacts (deterministic, sorted, LF):

artifacts/sanity/  
  SANITY.json        \# { passed, release\_id, engine\_tag, durations, tool\_versions, git:{sha,dirty}, created\_at }  
  CHECKSUMS.txt      \# sha256 of freeze artifacts & bands configs  
  GOLDEN\_REPORT.json \# per-pair results \+ hashes \+ timings

* **Exit behavior:** non-zero on any failure; artifacts still written for forensics when possible.

---

## **6\) CI pipeline (quality gates)**

**Sequential gates**

1. **Setup**: install **pinned** deps; verify pins.  
2. **Lint/Type**: ruff \+ mypy (hard fail on errors).  
3. **Unit/Schemas**: fast pytest suites.  
4. **Golden**: golden suite (shardable).  
5. **Sanity artifacts**: run sanity runner; upload `artifacts/sanity/*`.  
6. **(If adapter enabled)**: bring up adapter; hit `healthz/readyz/version`.

**Must pass to merge/deploy**

* All jobs green.  
* `SANITY.json.passed == true`.  
* `release_id` matches the concatenated checksums in `CHECKSUMS.txt`.  
* No secrets flagged.

*(Coverage target, informational to start: ≥85% lines on `hd_core/**`.)*

---

## **7\) PO Scenario Execution (manual, CLI-level)**

* **Sanity:** run the sanity runner; confirm “passed” and artifacts present.  
* **Golden spot-check:** run one published pair; verify `bands` and `idempotence_hash`.  
* **Swap probe:** swap A/B on that pair; verify symmetry rules.  
* **Drive-floor probe:** use a known non-Throat-route pair; verify clamp.  
* **Adapter ping (if enabled):** confirm `/internal/version` returns `release_id` \+ `engine_tag`.

---

## **8\) Post-deploy smoke (staging/prod)**

* **Lake GET:** 200, bands present, `engine_tag` present, `Cache-Control: no-store`.  
* **Compute smoke (library):** private admin task runs one golden pair; `idempotence_hash` matches.  
* **Cache path:** perform a birth update; next match recomputes, cache re-hydrates; logs show correlation chain.  
* **Headers discipline:** responses echo `X-Correlation-Id`; sensitive JSON is `no-store`.

---

## **9\) Acceptance checklist (we’re “quality-gated” when)**

* \[ \] Tool **pins** enforced & verified.  
* \[ \] Lint, type, secrets scans pass.  
* \[ \] Unit \+ schema \+ golden suites pass reliably.  
* \[ \] Sanity runner emits deterministic artifacts; CI publishes them.  
* \[ \] PO scenarios and post-deploy smoke are documented and reproducible.

---

## **Outstanding Asks (to lock this section)**

1. **Golden set seed**

   * Provide/confirm a minimal list of canonical **charts** and **pairs** we will treat as golden for 2025.1 (filenames \+ expected bands).  
   * Confirm whether golden pairs should include at least one **drive-floor clamp** case and one **narrative-only** emphasis case.  
2. **Schema files location**

   * Confirm final repo paths for **ChartV1**, **Result**, and **freeze** schemas (e.g., `schemas/…`) so tests can reference a stable `$id`.  
3. **Adapter decision (near-term)**

   * Confirm whether we enable the **HTTP adapter** in CI for the adapter tests; if **yes**, specify its **port/env** for the test harness.  
4. **Secrets policy toggle**

   * Confirm fail/allow behavior when the secrets scan flags something (default: **fail**).  
5. **Coverage reporting**

   * Do we want coverage thresholds to **block** merges now, or just report? (Default: **report-only** for 2025.1.)  
6. **CI environment**

   * Confirm runner image and CPU budget for the golden suite (so we don’t confuse perf with determinism).

# **Command Line & Developer Tools (2025.1)**

This section defines the **CLI surface**, the **local dev harness** for fetching chart fixtures from the provider (dev-only), and standard **repo tasks** for repeatable workflows. Everything is deterministic by default; any command that could touch the network is explicit and opt-in.

---

## **1\) CLI surface (run · inspect · verify)**

**Package/entrypoint**

* Python package: `hd_core`  
* Module entry: `python -m hd_core.cli …`  
* Optional console script: `hd …` (via `setup.cfg`/`pyproject` `console_scripts`)

### **1.1 `pair` — compute scores for two charts (library mode)**

Run the engine on two **ChartV1** files.

**Usage**  
 hd pair \\  
  \--a path/to/a.chart.json \\  
  \--b path/to/b.chart.json \\  
  \--release-id sha256:\<64hex\> \\  
  \[--pretty\] \[--hash-only\] \[--diagnostics\]

*   
* **Output**  
  * Default: minified JSON `{ok, release_id, bands, meta, idempotence_hash, duration_ms}`  
  * `--pretty`: pretty-printed JSON  
  * `--hash-only`: prints only `idempotence_hash`  
* **Exit codes**: `0` success · `2` validation error · `3` unsupported release · `4` internal fault

### **1.2 `chart` — validate/normalize/inspect a chart**

Validate a ChartV1, show canonical form, and compute its fingerprint.

**Usage**  
 hd chart \--in path/to/chart.json \[--print\] \[--fingerprint\]

*   
* **Output**  
  * With `--print`: canonical, **sorted** JSON (what the engine consumes)  
  * With `--fingerprint`: `sha256:<64hex>` of the canonical chart JSON  
* **Exit codes**: `0` valid · `2` schema/normalization error

### **1.3 `verify` — run golden determinism checks**

Execute the golden suite locally without full pytest.

**Usage**  
 hd verify \--pairs testdata/golden/pairs \--strict

*   
* **Behavior**  
  * Loads each `{a,b,release_id,expected_hash}` file  
  * Asserts **byte-identical** `{bands,meta}` and equal `idempotence_hash`  
  * `--strict` fails on any missing file or drift  
* **Exit codes**: `0` pass · `5` drift/failure

### **1.4 `version` — print release identity**

* **Usage**: `hd version`  
* **Output**: `{ "release_id": "...", "engine_tag": "...", "components": [{name, sha256}, ...] }`

### **1.5 `serve` (dev-only) — start internal HTTP adapter**

Runs the private adapter for local dev/CI smoke.

**Usage**  
 hd serve \--port 9001 \--release-id sha256:\<64hex\>

*   
* **Endpoints**  
  * `POST /internal/engine/v1/evaluate` (charts-in → result)  
  * `GET /internal/healthz`, `/internal/readyz`, `/internal/version`  
* **Limits**: body ≤ **64 KB**, timeout **3 s**, `Cache-Control: no-store`  
* **Never expose** to the public Internet

---

## **2\) Local dev harness (API fixture fetch · dev-only)**

Goal: generate **local chart fixtures** for tests without wiring BE. This is **opt-in** and **never** used in production.

### **2.1 `fetch` — call the provider to create a chart fixture**

**Usage**  
 hd fetch \\  
  \--birth-date 1990-01-01 \\  
  \--birth-time 14:30 \\  
  \--place "Tallinn, Estonia" \\  
  \[--endpoint bodygraphs|simple=bodygraphs\] \\  
  \--out testdata/golden/charts/alice.json

*   
* **Auth/env (required)**  
  * `HD_API_KEY` (env)  
  * `HD_GEOCODE_KEY` (env)  
* **Behavior**  
  * Sends request to provider `/v1/bodygraphs` (or `/simple`)  
  * Canonicalizes to **ChartV1**, computes `chart_fingerprint`  
  * Writes to `--out` (directories created as needed)  
* **Politeness**  
  * Built-in **rate limit** (e.g., 1 rps) and **retry with backoff** on 5xx  
  * Caches raw responses in `.cache/hdapi/` (TTL configurable) to avoid hammering  
* **Privacy**  
  * Never logs bodies or secrets; keys only with `correlation_id`

This command exists **only** to seed fixtures. Engine math never depends on live API calls.

---

## **3\) Repo tasks & scripts (Makefile / scripts)**

### **3.1 Make targets (authoritative)**

make ensure-env     \# pin check: python/pip/pytest/ruff/mypy  
make lint           \# ruff  
make type           \# mypy  
make test           \# pytest unit \+ schemas  
make test-golden    \# pytest golden  
make sanity         \# run scripts/make\_sanity.sh and emit artifacts  
make adapter        \# run hd serve (dev HTTP adapter) on a default port  
make audit          \# run scripts/make\_audit.sh to build audit bundle  
make fetch-sample   \# demo fixture fetch (requires API env vars)  
make clean          \# remove caches, artifacts

### **3.2 Scripts (shipped with the repo)**

* `scripts/ensure_env.py` — asserts **pinned** tool versions are active

`scripts/make_sanity.sh` — runs the quality gates and writes:  
 artifacts/sanity/  
  SANITY.json  
  CHECKSUMS.txt  
  GOLDEN\_REPORT.json

*   
* `scripts/make_audit.sh` — produces `audit_bundle_YYYYMMDDTHHMMSSZ.zip` with:  
  * `source_at_HEAD.zip`, git facts, env facts, `pip_freeze.txt`, layout (`tree.txt`/`du_sizes.txt`),  
  * optional tiny sample IO when `CREATE_SAMPLE=1`

### **3.3 Pre-commit (optional, recommended)**

* Hook chain: `ruff` → `mypy` (fast mode) → `pytest -q tests/unit`  
* Runs on changed files; blocks commit on failure

---

## **4\) CLI UX & determinism rules**

* **Default output**: minified JSON; `--pretty` for humans; NDJSON available via `--ndjson` where useful  
* **No randomness**: commands do not use RNG; timestamps excluded from hashes  
* **Stable ordering**: all objects serialized with **lexicographically sorted keys**; arrays sorted by documented rules  
* **Exit codes**: consistent across subcommands (see each command)  
* **Logs**: structured (keys-only), include `correlation_id`, never include PII or chart bodies

---

## **5\) File/dir conventions**

hd\_core/                 \# engine code  
policy/                  \# freeze packs (immutable per release)  
catalog/                 \# canonical reference data  
config/                  \# bands, scoring config (if used)  
schemas/                 \# JSON Schemas (ChartV1, Result, freeze, bands)  
testdata/golden/{charts,pairs}  
artifacts/sanity/        \# deterministic outputs from sanity runner  
scripts/                 \# ensure\_env, sanity, audit  
.cache/hdapi/            \# local dev cache for fetch (gitignored)

---

## **6\) Safety rails**

* Commands that touch the **network** (`hd fetch`) require explicit flags and env keys; otherwise they **fail fast**  
* The **HTTP adapter** is for **dev/staging** only; never bind to public interfaces  
* The CLI **never** writes or logs secrets; audit bundles exclude `.git`, caches, and secrets

---

## **Outstanding Asks** 

1. **CLI name**: confirm `hd` as the console script (vs `hdx`, `glow-hd`).  
2. **Adapter defaults**: confirm dev port (e.g., **9001**) and whether we enable it in CI smoke.  
3. **Fetch endpoint**: confirm default provider endpoint for fixtures (`bodygraphs` vs `simple`).  
4. **Cache TTL**: choose default TTL for `.cache/hdapi` (e.g., **24h**).  
5. **Makefile scope**: confirm the initial target set above; add/remove as needed.  
6. **Pre-commit**: decide whether to include and enforce it repo-wide.

# **Release Management & Versioning (2025.1)**

Authoritative policy for how we cut, audit, ship, roll back, and retire math releases of the HD Engine. This locks the version scheme, freeze process, compatibility windows, deprecation, and pinning.

---

## **1\) Version scheme (three identifiers)**

**A. Document/Plan version** — human-facing roadmap tag

* Format: `YYYY.N` (e.g., `2025.1`).  
* Used in this Architecture Plan, ADRs, and docs. Updates when we meaningfully evolve scope/process.

**B. Math release identity** — what proves a result

* `release_id` \= **SHA-256** over the canonical freeze artifacts (freeze pack, catalogs, bands, scoring\_config?).  
* `engine_tag` \= human label for the same release, e.g.  
   `HD-2025.1-YYYYMMDD-<7hex>` where `<7hex>` \= first 7 of `release_id`.  
* If **outputs can change for any ChartV1**, you must mint a **new** `release_id` and `engine_tag`.

**C. Package/build version** — code & distribution

* PEP 440 style: `2025.1.0`, `2025.1.1`, … for packaging/containers only.  
* **Rule:** Patch bumps (**.x**) must **not** change outputs; if they would, that’s a **new math release**.

**Change matrix**

| Change type | Examples | Bump |
| ----- | ----- | ----- |
| **Math-affecting** | weights/windows/caps; narrative-only set; Motor→Throat list; band curves; canonicalization rules | New `release_id` \+ new `engine_tag` (document stays `2025.1` unless scope changes) |
| **Non-math code** | perf; refactors; logging; CLI UX; adapter; tests | Package patch (`2025.1.x`). `release_id` and `engine_tag` **unchanged** |
| **Docs/process** | ADRs; runbooks; registry fields/enums | Doc version (maybe `2025.2` if scope materially expands); no math change |

---

## **2\) Freeze process (how a math release is made)**

1. **Propose**

   * Author an ADR describing the intended math change and expected qualitative effect. Owner: **Nathan**.  
2. **Implement behind a gate**

   * Edit freeze artifacts in a working branch; never half-land them on `main`.  
3. **Validate**

   * Run the pinned toolchain. All tests green: unit, property, schema, **golden**.  
   * Update/add golden pairs if the change is intentional; justify in ADR.  
4. **Compute identity**

   * Canonicalize \+ hash artifacts → compute **`release_id`**.  
   * Mint **`engine_tag`** for the release.  
5. **Evidence**

   * Write **SYNC\_LOG** entry (component sha256s, concatenation order, `release_id`, `engine_tag`).  
   * Produce `artifacts/sanity/` (`SANITY.json`, `CHECKSUMS.txt`, `GOLDEN_REPORT.json`).  
6. **Tag & package**

   * Git tag the commit: `engine/<engine_tag>`.  
   * Build/publish the library package `2025.1.X` (X increments even if math changed; math identity is the tag/id).  
7. **Stage → Prod**

   * **Staging:** BE sets `ACTIVE_RELEASE_ID=<release_id>`; run smoke (golden pair via library).  
   * **Prod:** flip `ACTIVE_RELEASE_ID`; lazy recompute on access (charts/pairs are namespaced by `release_id`).

---

## **3\) Backward compatibility window (acceptance policy)**

* **Production BE** accepts **exactly one** `release_id`: the **active** one.  
* **Staging BE** may accept **current \+ previous** `release_id` for a **14-day** test window (configurable).  
* Database retention (already set): keep prior-release `chart_snapshot` rows **30 days** for rollback; `pair_evaluation` will lazily recompute as accessed.

*(If you want dual-acceptance in prod for a short bake time, we can add it via ADR; default is **single-accept** for clarity.)*

---

## **4\) Deprecation rules**

* A release becomes **deprecated** once a newer release is **active** in prod for **30 days**.  
* Deprecated releases:  
  * Remain in **SYNC\_LOG** forever (audit).  
  * May be loadable in **dev/adapter** for **90 days** for investigation, but not in prod BE.  
  * Database rows older than the retention window may be **pruned** (charts and pairs), without affecting reproducibility (we can recompute offline if needed).

---

## **5\) Rollback & pinning**

**Fast rollback (no code changes):**

1. Set BE `ACTIVE_RELEASE_ID = <previous_release_id>`.  
2. Redeploy BE (or hot-reload env) and clear any intermediary caches.  
3. Traffic reads prior-release `chart_snapshot`; missing pairs recompute lazily.

**Package pinning:**

* BE depends on the Engine library pinned to the **git tag** `engine/<engine_tag>` (or package version **and** verifies `release_id` at import).  
* On import, Engine validates its local freeze checksums; startup **fails fast** if mismatched.

**Hotfixes:**

* If we ship a non-math patch (`2025.1.x`), **`release_id` and `engine_tag` do not change**.  
* We annotate with build metadata if needed (e.g., `+build.2`) but never change what clients see.

---

## **6\) Guardrails (what forces a new math release)**

* Any edit that can change `{bands, meta}`: freeze files, catalogs, band curves, canonicalization rules, drive-floor threshold, directional tilt, narrative-only list.  
* Any change that affects **stable ordering** or **hashing**.  
* Any change to **ChartV1** semantics used by the Engine.

If in doubt, treat it as math-affecting and mint a new `release_id`.

---

## **7\) Ship checklist (must be true to go live)**

* \[ \] All tests green (unit, property, schema, golden).  
* \[ \] `SANITY.json.passed == true`; `CHECKSUMS.txt` matches; `release_id` computed.  
* \[ \] SYNC\_LOG updated; `engine_tag` minted and git-tagged.  
* \[ \] Staging BE running with `ACTIVE_RELEASE_ID` \+ smoke passed.  
* \[ \] Prod BE flip planned during a quiet window; monitoring & rollback steps ready.

---

## **8\) Operational policy (post-ship)**

* Monitor `engine_compute_seconds` p95/p99, `engine_errors_total`, and **cache hit ratio** for 24–48h.  
* If regression: **rollback first**, investigate second.  
* Write a short note in CHANGELOG with impact and any band movement observed in golden pairs.

---

## **9\) Documentation & audit trail**

* `docs/CHANGELOG.md` — human narrative of what changed.  
* `docs/SYNC_LOG.md` — machine checksums and identities per release.  
* ADRs folder — decisions and rationales tied to each math change.  
* `release/<engine_tag>/` (optional) — frozen artifacts \+ manifest for that release.

---

### **Outstanding Asks (to finalize this policy)**

1. **Acceptance policy**: Keep prod as **single-accept** only, or allow a **7–14 day dual-accept** window?  
2. **Staging window length**: Confirm **14 days** for dual-accept in staging (or propose different).  
3. **Retention horizons**: Re-confirm `chart_snapshot` prior-release \= **30 days**; `pair_evaluation` TTL \= **90 days**.  
4. **Tag naming**: Approve `engine/<engine_tag>` as the git tag prefix.  
5. **Package channel**: Confirm how BE pins the engine (git tag vs PyPI package \+ `release_id` check at import).  
6. **Hotfix labeling**: Approve keeping `engine_tag` **unchanged** for non-math patches (use build metadata only).

# **Conventions & Contribution Guide (2025.1)**

Opinionated, light, and built to keep the math deterministic. When in doubt: **small, reversible PRs**; **prove** with tests; **no surprises** in production.

---

## **1\) Code style & repo hygiene**

### **Python style**

* **Formatter**: `ruff format` (pinned 0.5.x). No hand-formatting; no Black.  
* **Linter**: `ruff` (errors only; warnings allowed on legacy code but must not grow).  
* **Types**: `mypy` clean on `hd_core/**` and `policy/**`. Public interfaces are fully typed.  
* **Imports**: absolute, sorted by ruff; no wildcard imports; from-`__future__` not needed on 3.12+.  
* **Naming**: `snake_case` for funcs/vars, `CamelCase` for classes, `UPPER_SNAKE` for constants. Modules `snake_case.py`.  
* **Docstrings**: Google style for public functions; keep brief and factual.  
* **Errors**: raise typed exceptions from the Engine library; no bare `except`.  
* **I/O boundaries**: the core stays **pure** (no network/DB/FS/PII). Adapters and scripts handle I/O.

### **JSON & determinism**

* Sort keys **lexicographically**; minify; LF newlines; UTF-8.  
* Arrays sorted per contract (channels `min-max`, gates by `(NN, line)`).  
* **Never** add timestamps or random values to structures that affect hashing.

### **Repo structure (authoritative)**

hd\_core/              \# engine code (pure)

policy/               \# freeze packs (immutable per release)

catalog/              \# canonical reference data

config/               \# bands \+ scoring config (if used)

schemas/              \# JSON Schemas (ChartV1, Result, freeze, bands)

tests/                \# unit, golden, props, schemas

testdata/golden/      \# charts/ \+ pairs/ (canonical, minified)

scripts/              \# ensure\_env, make\_sanity, make\_audit

artifacts/            \# CI outputs (ignored by git)

### **Hygiene**

* No secrets, keys, or raw provider responses in the repo.  
* Do **not** commit `artifacts/`, caches, or `.venv/`. `.gitignore` is enforced.  
* Golden fixtures must be **small** and canonicalized (minified, sorted). Large test assets live outside the repo.

---

## **2\) Branching & PR review**

### **Strategy**

* **Trunk-based**: `main` is protected; all changes via short-lived branches \+ PRs.  
* **Small PRs**: aim \< **400 LOC** changed (excluding fixtures). Split otherwise.  
* **CI required**: pins, lint/type, unit/schemas, golden, sanity artifacts.

### **Reviews**

* **Required approvals**: 1 reviewer minimum; **Nathan** must approve any math change.  
* **What reviewers check**  
  * Determinism preserved (or explicitly versioned via new `release_id`).  
  * Scope is single-lane; no drive-by refactors.  
  * Tests cover changes; golden updated only with justification.  
  * No PII in logs; headers & contracts unchanged unless documented.

### **PR checklist (template)**

* \[ \] Scope: one lane only; why now?  
* \[ \] Tests: unit / schemas / golden (if math).  
* \[ \] Determinism: stable ordering preserved; hashes unaffected (or new release).  
* \[ \] Docs: ADR / SYNC\_LOG / CHANGELOG updated if needed.  
* \[ \] Security: no secrets; logs are keys-only.  
* \[ \] CI: all gates green.

---

## **3\) ADR format (Architecture Decision Record)**

**Filename**: `adr/YYYYMMDD-short-title.md`  
 **Template**

\# Title

\- Status: Proposed | Accepted | Superseded

\- Owner: Nathan Amthor

\- Date: 2025-09-23

\- Affects math outputs: Yes|No

\- Related: release\_id (if yes), engine\_tag, PRs

\#\# Context

(Problem, constraints, alternatives considered.)

\#\# Decision

(What we decided. If math-affecting, describe expected qualitative effect.)

\#\# Consequences

(Impact on Engine, BE, FE, DB, ops. Migration/backfill notes.)

\#\# Evidence

(Links to golden diffs, plots, SYNC\_LOG entry hash list.)

**Rule**: Any change that can alter `{bands, meta}` **must** have an ADR and will mint a new `release_id`.

---

## **4\) Commit message norms**

### **Conventional prefix (pragmatic)**

* `feat(engine): …` new engine capability (non-math or gated)  
* `fix(engine): …` bug fix (if math-affecting → new release\_id)  
* `perf(core): …` performance improvement (no output change)  
* `refactor(core): …` structure only; no behavior change  
* `docs(adr): …` ADR/CHANGELOG updates  
* `chore(ci): …` pins, tooling  
* `test(golden): …` add/update golden fixtures (explain *why*)

### **Body**

* Explain **why**, not just *what*.  
* Reference ADRs and issues: `Refs: ADR-20250923, #123`.  
* For math changes include:  
   `BREAKS_HASH: yes` and a one-line summary of band movement on key goldens.

### **Examples**

feat(engine): add drive-floor clamp to block top bands without route to Throat

Refs: ADR-20250923-drive-floor

fix(engine): correct narrative-only exclusion in talk loads

BREAKS\_HASH: yes

Refs: ADR-20250925-narrative-only

---

## **5\) PR size & sequencing rules**

* **One lane at a time**: math, infra, or docs—pick one.  
* If touching math and code, split into:  
  1. refactor PR (no output change),  
  2. math PR (goldens \+ SYNC\_LOG),  
  3. release wiring PR (BE `ACTIVE_RELEASE_ID` flip).  
* Avoid “rename \+ edit” in one PR; makes review impossible.

---

## **6\) Reviewable artifacts**

* For math PRs, attach:  
  * `GOLDEN_REPORT.diff` (before/after bands \+ hashes),  
  * Updated `CHECKSUMS.txt`,  
  * Proposed `release_id` and `engine_tag`.  
* For non-math PRs, prove no drift:  
  * Run `make sanity`; show `SANITY.json` with unchanged `release_id`.

---

## **7\) Security & privacy conventions**

* Keys-only logs; never bodies or PII (birth, place\_text, chart JSON).  
* Secrets only via env; never committed; `scripts/make_audit.sh` excludes them.  
* Error messages human-readable but generic; include `correlation_id`.

---

## **8\) Contributor onboarding (quick start)**

1. `make ensure-env`  
2. `make lint type test`  
3. `make test-golden` (if you touched math)  
4. `make sanity` (captures evidence)  
5. Open PR with checklist & artifacts

---

## **9\) Do / Don’t**

**Do**

* Write tests first for math changes; update golden intentionally.  
* Keep commit history clean and explanatory.  
* Use ADRs for any decision that affects outputs or contracts.

**Don’t**

* Slip in unrelated refactors.  
* Change JSON key order or array ordering rules.  
* Land math changes without a new `release_id` and SYNC evidence.

---

## **Outstanding Asks (to finalize this section)**

1. **Adopt Conventional Commits** formally? (Prefixes above)  
2. **Set PR size guardrail** in repo settings (soft/hard warning threshold).  
3. **Require CODEOWNERS** (e.g., `hd_core/**` → Nathan) and minimum 1 approval?  
4. **Adopt pre-commit** hooks repo-wide (ruff/mypy/fast unit)?  
5. **ADR storage path** confirm: `docs/adr/` vs `adr/` at repo root.  
6. **PR template** add to `.github/pull_request_template.md` with the checklist above?  
7. **Commit signing** (GPG/Sigstore) and/or DCO requirement?

# **Decision Log & Open Questions (2025.1)**

This section is the single place to see what we’ve decided (with ADRs) and what’s still open. It stays short, scannable, and brutally specific.

---

## **ADR Index (source of truth)**

File path: `docs/adr/ADR-YYYYMMDD-<slug>.md` · Owner: **Nathan Amthor** · Status: Proposed | Accepted | Superseded

| ADR ID | Title | Status | Affects Math? | Notes |
| ----- | ----- | ----- | ----- | ----- |
| **ADR-20250923-engine-integration** | Engine integration modes (Prod=library, Dev=HTTP adapter) | **Accepted** | No | FE never calls Engine; BE-only boundary. |
| **ADR-20250923-chart-storage** | Chart persistence as single JSONB (ChartV1 superset) | **Accepted** | No | `chart_snapshot(user_id, release_id)` \+ fingerprint. |
| **ADR-20250923-pair-cache** | Pair cache contract (`pair_evaluation`) | **Accepted** | No | Canonical min/max user order; fingerprints validate. |
| **ADR-20250923-no-tz** | No tz/lat/lon captured by Glow | **Accepted** | No | Store `place_text` only; provider does tz/geo. |
| **ADR-20250923-canonicalization** | Provider→ChartV1 canonicalization rules | **Accepted** | No | Centers/channels/gates normalization \+ hashing. |
| **ADR-20250923-determinism** | Freeze, release\_id, hashing & SYNC\_LOG | **Accepted** | **Yes** | What constitutes a math change. |
| **ADR-20250923-math-foundations** | Domains, tilt, Q-bridge, drive floor, bands/windows | **Proposed** | **Yes** | Becomes the basis for `release_id` when frozen. |
| **ADR-20250923-quality-gates** | Test taxonomy \+ sanity artifacts | **Accepted** | No | Pins, golden, schemas, CI gates. |
| **ADR-20250923-observability** | Logs/metrics/health \+ correlation policy | **Accepted** | No | Keys-only logs; `X-Correlation-Id` everywhere. |
| **ADR-20250923-release-policy** | Version scheme, acceptance window, rollback | **Proposed** | No | Single-accept in prod (default); staging dual-accept window TBD. |
| **ADR-20250923-cli-surface** | CLI commands \+ dev fetch harness | **Proposed** | No | \`hd pair |

When an ADR **affects math**, its merge must mint a new `release_id` and update SYNC\_LOG.

---

## **Current Open Decisions**

What we need to lock next. Each item shows the **decision**, the **current placeholder**, and the **where-to-record** home once decided.

### **A) Limits & Sizing**

| Decision | Current | Options / Guidance | Record in |
| ----- | ----- | ----- | ----- |
| Gunicorn **workers** (Railway) | TBD | Start `workers = vCPU` (or `ceil(vCPU×1.5)`); validate by load test | Ops docs \+ env |
| Gunicorn **worker timeout** | TBD | 60–120s typical; compute is CPU-bound, not I/O | Ops docs |
| BE **body-size cap** for API | TBD | 1–2 MB overall; Engine adapter remains **64 KB** | BE config |
| Engine HTTP **adapter timeout** | **3000 ms** | Keep 3s; single retry on 5xx/timeout | ADR-…-engine-integration |
| FE **retry/backoff** on 429 | TBD | Respect `retry_after_ms`; exponential backoff | FE wrapper doc |
| Provider **QPS limit (fixtures)** | TBD | Start 1 rps; backoff on 429/5xx | CLI fetch doc |

### **B) Retention & TTLs**

| Decision | Current | Rationale | Record in |
| ----- | ----- | ----- | ----- |
| `pair_evaluation` TTL | **90 days** | Evictable; recompute on access | DB note |
| `chart_snapshot` prior-release retention | **30 days** | Rollback window | DB note |
| `birth_data` history depth | **N=5** rows or 365d | PII minimization vs audit | DB note |

### **C) Rollout & Compatibility**

| Decision | Current | Options | Record in |
| ----- | ----- | ----- | ----- |
| **Prod acceptance window** | **Single-accept** only | Optional dual-accept (prev+current) for 7–14 days | ADR-…-release-policy |
| **Staging acceptance window** | **14 days** | 7–30 days acceptable | ADR-…-release-policy |
| **Backfill mode at cutover** | **Lazy** | Add throttled eager backfill after N active users | Ops/runbook |

### **D) CI & Quality Policy**

| Decision | Current | Options | Record in |
| ----- | ----- | ----- | ----- |
| Enable **HTTP adapter** in CI | TBD | If yes, set port & env | CI config |
| **Secrets scan** stance | **Fail build** | Allow with override tag? | Security policy |
| **Coverage** threshold | Report-only | Block at ≥80–85% later | CI policy |
| **Pre-commit** hooks | TBD | ruff/mypy/fast unit on changed files | Contrib guide |
| **Golden set seed** | Pending | Include at least one drive-floor clamp \+ narrative-only case | tests/golden |

### **E) Observability & Ops**

| Decision | Current | Options | Record in |
| ----- | ----- | ----- | ----- |
| Metrics backend | TBD | (e.g., Prometheus-compatible) | Ops doc |
| Trace backend | TBD | W3C `traceparent`; sampling rate | Ops doc |
| Log retention | **14 days** | 30 days if cost allows | Ops doc |
| Alert thresholds fine-tune | Drafted | Tune after first load test | Ops doc |

### **F) CLI & Dev Harness**

| Decision | Current | Options | Record in |
| ----- | ----- | ----- | ----- |
| Console **command name** | `hd` (proposed) | `hdx`, `glow-hd` | CLI ADR |
| Default **fetch endpoint** | `bodygraphs` | `simple` for fast seeds | CLI ADR |
| Fixture cache **TTL** | **24h** (proposed) | 6–72h | CLI ADR |

---

## **How to Add a Decision (fast path)**

1. Open a short PR adding/adjusting an ADR in `docs/adr/…` (use the template).  
2. If math-affecting: update golden, compute `release_id`, write SYNC\_LOG.  
3. Update this section’s **Open Decisions** or move an item to the **ADR Index** as **Accepted**.  
4. If operational: add env/config default \+ a one-liner in the runbook.

---

## **“Done” Definition for This Section**

* \[ \] ADRs above exist in the repo with the statuses shown.  
* \[ \] Every Open Decision has a named owner (default: **Nathan**) and a target PR.  
* \[ \] When an item is decided, it migrates from **Open Decisions** into the **ADR Index** with `Status: AcRisk Register (2025.1)`

`Scope: end-to-end risks across product, math, FE/BE, ops, data, and vendor.`  
 `Owner of all risks (for now): Nathan Amthor. Backup owner: TBD (pending partnership).`  
 `Scales: Likelihood = L/M/H, Impact = L/M/H/Critical. Exposure = quick RAG.`

---

### **`R-001 • Single-owner bus factor`**

* **`Category:`** `Org/People — Exposure: 🔴 High`  
* **`Why it matters:`** `One person holds context; delays or burnout halt progress.`  
* **`Triggers/indicators:`** `Slipping ETAs; >5 open ADRs; >2 weeks without CI green on main.`  
* **`Mitigations (proposed):`** `Lightweight onboarding pack; CODEOWNERS; PR template; weekly 1-pager status; document “golden path” setup.`  
* **`Contingency:`** `Pause scope; defer non-critical lanes; bring partner in with “first 7 tasks” playbook.`  
* **`Status:`** `Open`

  ### **`R-002 • Determinism regression (hash drift)`**

* **`Category:`** `Math/Quality — Exposure: 🟠 Medium-High`  
* **`Triggers:`** `Golden pair hash changes without SYNC_LOG; test flakes on CI.`  
* **`Mitigations:`** `Pin toolchain; golden fixtures; make_sanity artifacts; release_id hashing; no runtime config.`  
* **`Contingency:`** `Roll back ACTIVE_RELEASE_ID; re-run sanity; bisect last math change.`  
* **`Status:`** `Controls defined; needs CI gate fully wired`

  ### **`R-003 • Provider API outage / rate limits`**

* **`Category:`** `Vendor — Exposure: 🟠 Medium`  
* **`Triggers:`** `5xx/timeout spikes; 429s; elevated fetch retries.`  
* **`Mitigations:`** `Compute-on-write; fixture cache for dev; conservative backoff; queue births; user copy for outages.`  
* **`Contingency:`** `Return 503 upstream_*; disable birth writer temporarily; resume queued jobs later.`  
* **`Status:`** `Partial (copy/backoff TBD)`

  ### **`R-004 • Privacy/PII leakage in logs or responses`**

* **`Category:`** `Security/Privacy — Exposure: 🔴 High`  
* **`Triggers:`** `Body size logs; unredacted place_text; chart JSON in logs.`  
* **`Mitigations:`** `Keys-only logging; lint rule for logging; redaction unit test; no-store everywhere.`  
* **`Contingency:`** `Rotate keys; purge logs; incident note; tighten logger config.`  
* **`Status:`** `Policy set; enforcement tasks pending`

  ### **`R-005 • Cache incoherence (stale pair results)`**

* **`Category:`** `Data correctness — Exposure: 🟠 Medium-High`  
* **`Triggers:`** `Pair cache hit with fingerprint mismatch; complaints about “old match”.`  
* **`Mitigations:`** `Fingerprint validation; lazy invalidation on birth update; cache TTL; metrics on hit ratio.`  
* **`Contingency:`** `Drop affected pairs; rebuild on access; add eager invalidation for hot users.`  
* **`Status:`** `Design ready; needs implementation`

  ### **`R-006 • Schema drift (ChartV1 vs provider)`**

* **`Category:`** `Data contract — Exposure: 🟠 Medium`  
* **`Triggers:`** `New provider fields; centers/channels naming mismatch.`  
* **`Mitigations:`** `Canonicalization map; JSON Schema validation at ingest; strict unknown-field handling.`  
* **`Contingency:`** `Hotfix ingest map; re-ingest last N charts.`  
* **`Status:`** `Partial (schemas to land)`

  ### **`R-007 • Performance SLO breach (engine p95 > 400ms)`**

* **`Category:`** `Perf/Scale — Exposure: 🟡 Medium`  
* **`Triggers:`** `p95/p99 alarms; CPU >75% sustained; queueing in BE.`  
* **`Mitigations:`** `Horizontal workers; micro-profiling; ≥80% cache hit target; lazy backfill.`  
* **`Contingency:`** `Scale workers; shed non-critical paths; defer backfills.`  
* **`Status:`** `Targets set; load test pending`

  ### **`R-008 • Secrets exposure (repo/CI/env)`**

* **`Category:`** `Security — Exposure: 🔴 High`  
* **`Triggers:`** `Secret scan fail; env printed in logs; audit bundle includes creds.`  
* **`Mitigations:`** `Secrets scan = fail build; mask env in CI; audit script excludes secrets; least-privilege keys.`  
* **`Contingency:`** `Rotate; invalidate tokens; audit accesses; post-mortem.`  
* **`Status:`** `Policy defined; CI enforcement pending`

  ### **`R-009 • Release/rollback error (wrong release_id)`**

* **`Category:`** `Release mgmt — Exposure: 🟠 Medium`  
* **`Triggers:`** `BE active id mismatches Engine pack; startup warnings.`  
* **`Mitigations:`** `Engine validates checksums on import; /internal/version; staging dual-accept window (TBD).`  
* **`Contingency:`** `Flip ACTIVE_RELEASE_ID back; lazy recompute; add guard in BE init.`  
* **`Status:`** `Needs import-time check wired`

  ### **`R-010 • Legal/licensing ambiguity (provider ToS/IP)`**

* **`Category:`** `Legal/Vendor — Exposure: 🟠 Medium`  
* **`Triggers:`** `ToS change; usage cap changes; licensing queries.`  
* **`Mitigations:`** `Track provider version in chart_version; keep minimal stored fields; document use.`  
* **`Contingency:`** `Switch to alternative endpoint (/simple) or pause writers; review contract.`  
* **`Status:`** `Open`

  ### **`R-011 • FE error handling → thundering herd`**

* **`Category:`** `Client behavior — Exposure: 🟡 Medium`  
* **`Triggers:`** `429 storms; repeated retries; spike in BE load.`  
* **`Mitigations:`** `FE wrapper respects retry_after_ms; one-retry rules; jittered backoff.`  
* **`Contingency:`** `Temporary rate limits; circuit breaker in BE.`  
* **`Status:`** `Needs FE wrapper finalized`

  ### **`R-012 • DB integrity/backups`**

* **`Category:`** `Data/Infra — Exposure: 🔴 High`  
* **`Triggers:`** `Failed migrations; missing backups; high replication lag.`  
* **`Mitigations:`** `Minimal schema; indexes; nightly backup/restore drill; migration checklist.`  
* **`Contingency:`** `Restore from latest; rebuild pairs lazily from charts.`  
* **`Status:`** `Backup cadence TBD`

  ### **`R-013 • Vendor lock-in / platform outage (Railway/Vercel)`**

* **`Category:`** `Infra — Exposure: 🟡 Medium`  
* **`Triggers:`** `Regional incident; deploy pipeline down.`  
* **`Mitigations:`** `IaC notes (light); exportable build; documented rollback.`  
* **`Contingency:`** `Pause deploys; scale up single region; consider alt provider ADR.`  
* **`Status:`** `Open`

  ### **`R-014 • Ethics/covenant drift (numbers leak, over-assertive copy)`**

* **`Category:`** `Product/Ethics — Exposure: 🟠 Medium`  
* **`Triggers:`** `Numeric scores in UI; WHY text exposed; aggressive prompts.`  
* **`Mitigations:`** `Bands-only rule; copy review; registry gate for surface fields.`  
* **`Contingency:`** `Hotfix FE; content audit; add linter for banned fields.`  
* **`Status:`** `Policy set; guardrails to implement`

  ### **`R-015 • Place ambiguity at ingest`**

* **`Category:`** `Data Quality — Exposure: 🟡 Medium`  
* **`Triggers:`** `Partial place_text; provider returns 422; low match rate on first try.`  
* **`Mitigations:`** `FE geocoding assist; strict validation; typed error with suggestions.`  
* **`Contingency:`** `Queue retry with clarified place; save “needs attention” state.`  
* **`Status:`** `FE assist planned`  
  ---

  ## **`Heatmap (quick view)`**

* `🔴 High exposure: R-001, R-004, R-008, R-012`  
* `🟠 Medium-High: R-002, R-005, R-009, R-014`  
* `🟡 Medium: R-003, R-006, R-007, R-011, R-013, R-015`  
  ---

  ## **`Next Steps / Owners`**

* **`Convert top 6 risks into sprint cards`** `with concrete tasks:`  
   `R-001 (onboarding pack), R-004 (logger/redaction guard), R-008 (CI secret fail),`  
   `R-012 (backup + restore drill), R-002 (sanity artifacts in CI), R-005 (fingerprint check path).`  
* **`Partnership onboarding:`** `define backup owner and handoff list (R-001).`  
* **`Lock ops thresholds:`** `finalize alerting for R-007 and R-005.`

Here’s a tighter, accurate **Appendices** section—and a quick answer to your question:

**SPA \= Single-Page Application** (our React \+ Vite frontend on Vercel). It loads once and talks to the backend via JSON APIs; routing and state updates happen client-side.

---

# **Appendices (2025.1)**

## **A. Glossary & acronyms**

* **SPA** — Single-Page Application (React \+ Vite on Vercel).  
* **FE** — Frontend (the SPA).  
* **BE** — Backend (Flask/Gunicorn on Railway).  
* **Engine** — HD Engine core (pure, deterministic library; optional internal HTTP adapter for dev/staging only).  
* **ChartV1** — Canonical, provider-normalized chart JSON stored in `chart_snapshot` (no birth/timezone/PII).  
* **Lake** — Read surface the SPA queries (bands-only \+ `engine_tag`).  
* **Writer** — Mutating endpoint (returns `204 No Content`; SPA refetches Lake afterward).  
* **Freeze pack** — Versioned JSONs for math knobs (weights, windows/caps, lists), hashed into `release_id`.  
* **release\_id** — SHA-256 over freeze artifacts; proves math identity for outputs.  
* **engine\_tag** — Human label for a math release (e.g., `HD-2025.1-20250923-1a2b3c4`).  
* **Q-Bridge** — Definition-bridging meta (hops, voice, symmetry).  
* **Drive floor** — Predicate/cap preventing top bands without a Motor→Throat route.  
* **PII** — Personally Identifiable Information (Engine never sees PII).  
* **TTL** — Time to live (cache retention).  
* **ADR** — Architecture Decision Record.  
* **SYNC\_LOG** — Checksums \+ `release_id` evidence for a math release.  
* **Idempotence hash** — Deterministic SHA-256 over `{release_id,bands,meta}` (stable-serialized).

  ---

  ## **B. Sample envelopes & fixtures**

  ### **B1. Engine (HTTP adapter, dev/staging only)**

**Request (charts-in)**

{

  "release\_id": "sha256:\<64hex\>",

  "a\_chart": { "...": "ChartV1 (see B4)" },

  "b\_chart": { "...": "ChartV1 (see B4)" },

  "diagnostics": false

}

**Success**

{

  "ok": true,

  "release\_id": "sha256:\<64hex\>",

  "bands": { "communication": "Open", "harmony": "Warm", "drive": "Cool" },

  "meta": { "qbridge": { "len\_hops": 2, "voice": 1, "sym": "both" }, "throat\_route": true },

  "idempotence\_hash": "sha256:\<64hex\>",

  "duration\_ms": 187,

  "correlation\_id": "f2c6a9a2-..."

}

**Typed error**

{

  "ok": false,

  "code": "validation\_error",

  "message": "Please check your inputs.",

  "retry\_after\_ms": 0,

  "release\_id": "sha256:\<64hex\>",

  "correlation\_id": "f2c6a9a2-..."

}

### **B2. Lake (bands-only to SPA)**

{

  "ok": true,

  "user": { "id": "u\_123", "email\_verified": true },

  "matching": {

    "categories": \[

      { "id": "harmony", "band": "Warm" },

      { "id": "communication", "band": "Open" },

      { "id": "drive", "band": "Cool" }

    \],

    "eligible": true,

    "engine\_tag": "HD-2025.1-20250923-1a2b3c4"

  },

  "server\_time": "2025-09-23T20:05:12Z",

  "correlation\_id": "f2c6a9a2-..."

}

### **B3. Writer — Update birth (SPA → BE)**

*Request*

{

  "birth\_date": "1990-01-01",

  "birth\_time\_local": "14:30",

  "time\_precision": "full",

  "place\_text": "Tallinn, Estonia"

}

*Response*: `204 No Content` with `Cache-Control: no-store` (SPA immediately refetches Lake).

### **B4. ChartV1 (canonicalized example stored in DB)**

{

  "release\_id": "sha256:\<freeze\>",

  "type": "Manifesting Generator",

  "profile": "4/6",

  "authority": "Emotional",

  "centers": { "Throat": "defined", "G": "open", "Sacral": "defined" },

  "channels": \["10-20", "57-20"\],

  "gates": \["10.3", "20.5", "57.2"\],

  "chart\_provider": "HDAPI",

  "chart\_version": "v1.bodygraphs",

  "chart\_fingerprint": "sha256:\<64hex\>"

}

### **B5. Golden fixture (determinism)**

{

  "a": "testdata/golden/charts/alice.json",

  "b": "testdata/golden/charts/bob.json",

  "release\_id": "sha256:\<freeze\>",

  "expected": {

    "bands": { "communication": "Open", "harmony": "Warm", "drive": "Cool" },

    "idempotence\_hash": "sha256:\<64hex\>"

  }

}

---

## **C. Reference tables (IDs/constants)**

### **C1. Canonical center names**

| Canonical | Notes |
| ----- | ----- |
| Head |  |
| Ajna |  |
| Throat |  |
| G | aka “G Center” |
| Heart | aka Ego/Will |
| Spleen |  |
| Solar Plexus | aka Emotional |
| Sacral |  |
| Root |  |
| Values: `"defined"` or `"open"`. |  |

### **C2. Motor→Throat “direct” channels (v1.1)**

Used by the **drive floor** predicate.

* `34-20`, `21-45`, `12-22`, `35-36`  
   *(Frozen in catalog; changes require a new math release.)*

  ### **C3. Narrative-only trio (excluded from Talk lift)**

* `01-08`, `13-33`, `31-07`

  ### **C4. Bands & presentation (FE-only)**

* **Engine bands (strings):** `Cool`, `Open`, `Warm`, `Glow`.  
* **Color mapping:** **SPA-only design tokens** map bands → colors (no numerics, no colors from Engine/BE).

  ### **C5. Headers, cookies, identity patterns**

* **Request (SPA→BE):** `X-Correlation-Id`, `X-CSRF-Token` (writers), `Content-Type: application/json`, `Accept: application/json`.  
* **Response (BE/Engine JSON):** `Cache-Control: no-store`, echo `X-Correlation-Id`.  
* **Cookies:** `glow_session` (HttpOnly, Secure, SameSite=Lax), `glow_csrf` (Secure, JS-readable).  
* **engine\_tag:** `^HD-\d{4}\.\d-\d{8}-[0-9a-f]{7}$`  
* **release\_id:** `^sha256:[0-9a-f]{64}$`  
* **Correlation ID:** UUIDv4.

  ---

  ## **D. Change log snapshot (2025.1)**

* **2025-09-23** — Initial architecture locked.  
  * **Integration:** Prod \= in-proc library (charts-in → scores-out); Dev/Staging \= internal HTTP adapter.  
  * **Data model:** `chart_snapshot` stores single ChartV1 JSON (+ provenance pins); `pair_evaluation` caches pair results with chart fingerprints.  
  * **Determinism:** Freeze artifacts → `release_id`; outputs include `idempotence_hash`; SYNC\_LOG process defined.  
  * **Contracts:** Lake is bands-only; Writers return `204` then SPA refetches Lake.  
  * **Canon rules:** Center names normalized; channels `min-max`; gates `NN(.L)`; narrative-only trio frozen.  
  * **Ops:** Keys-only logs; `X-Correlation-Id` everywhere; adapter `healthz/readyz/version`.  
  * **Perf targets:** Engine p95 ≤ 400 ms, p99 ≤ 800 ms; pair cache hit ≥ 0.80.  
  * **Quality gates:** Unit \+ property \+ golden; sanity runner emits deterministic artifacts.  
  * **Release policy:** Single-accept in prod (default); staging dual-accept window TBD.


## Development Task List

