Awesome — locking this in as the **canonical tasks doc**. Here’s the finalized, paste-ready version (v3), with metadata up top and the seven alchemical phases. Use this as the single source of truth in the repo.

# **HD Engine Tasks — Canonical Plan (v3)**

**Doc ID:** hd-engine-tasks-v3  
 **Version:** 2025.1 • **Engine Track:** v1.1  
 **Owner:** Nathan Amthor (PO \+ HD Coder)  
 **Scope:** Engine only (math core, envelopes, internal adapter, tooling). No FE, no BE DB.  
 **Non-goals:** Presenter copy, SPA wiring, payments, mobile app work.

---

## **I) Calcination — Truth & Determinism Bedrock**

**Goal:** Same inputs → byte-identical outputs anywhere.

### **Tasks**

* **Freeze & identity (single way to compute)**

  * Enumerate artifacts (freeze pack, catalogs, band windows/caps, **narrative-only list**, **Motor→Throat list**) via an explicit allowlist (exclude backups/transients).  
  * `release_id = sha256(stable_concat(ordered_artifacts_bytes))` using the stable canon in a **fresh, pinned** process.  
  * Emit `SYNC_LOG` (ordered filenames → sha256, release\_id) \+ `CHECKSUMS.txt`.  
* **Serialization canon (one source)**

  * `sercanon`: `stable_normalize`, `stable_dumps`, `stable_hash` with ordering rules:  
    * Dicts: lexicographic by key.  
    * Channels: `min-max` asc (normalized).  
    * Gates: `(NN, line)` asc (NN numeric; default line=0).  
  * **All emitters** (tests, CLI, adapter, artifacts) must use `sercanon`. **Ban ad-hoc sorts.**  
* **Idempotence hashing**

  * `idempotence_hash = sha256(stable_dumps({release_id,bands,meta}))`.  
  * Masks → **prune → drop-empties** for `_diagnostics`, `_why`, `_admin_debug`, `meta.trace`.  
  * Tests prove masks don’t change the hash.  
* **Schemas**

  * JSON Schemas for ChartV1, Result, freeze pack, bands; strict validation.  
  * ChartV1 canonicalizer (reject birth/tz/lat/lon; normalize names/ordering).  
* **Pins & goldens**

  * `ensure_env` fail-fast; pins authoritative.  
  * Seed goldens: (a) Drive-floor clamp, (b) narrative-only emphasis.

    ### **Hard gates**

* release\_id recomputes identically on a clean clone.  
* Goldens pass; AB↔BA symmetry \+ idempotence masks proven.

  ---

  ## **II) Dissolution — Boundaries & Interfaces**

**Goal:** Pure core separated from I/O; identical contracts across modes.

### **Tasks**

* **Public library API**

  * `compute_pair(chart_a: ChartV1, chart_b: ChartV1, release_id: str, *, diagnostics=False) -> Result`  
  * Exceptions: `ValidationError`, `UnsupportedReleaseError`, `EngineInternalError`.  
* **Unified envelopes (library & adapter)**

  * **Success:** `{ ok:true, release_id, engine_tag, bands, meta, idempotence_hash, duration_ms }`  
  * **Error:** `{ ok:false, engine_tag, release_id, error:{ code, message, details? }, correlation_id? }`  
  * Re-state idempotence mask rule in the envelope docs.  
* **Internal HTTP adapter (dev/staging only)**

  * `POST /internal/engine/v1/evaluate`, `GET /internal/{healthz,readyz,version}`.  
  * Limits: **≤64 KB** body, **3 s** budget; client retry **1× on 5xx/timeout**; 4xx terminal.  
  * Always echo `X-Correlation-Id`; set `Cache-Control: no-store`.  
  * **Dev-only:** private bind; never public.

    ### **Hard gates**

* Same envelopes verified across library & adapter.  
* `/internal/version` returns {release\_id, engine\_tag, repo-relative checksums}.

  ---

  ## **III) Separation — Core Math Modules**

**Goal:** Small, pure, fully-tested organs with clear boundaries.

### **Tasks**

* **Graph & reachability**

  * BFS route-to-Throat primitive; “voice present” truth exposed.  
* **Loaders & canonicalization**

  * Catalog loader reads **narrative-only** \+ **Motor→Throat** **from freeze**; no inline IDs in code/tests (schema-guard).  
  * Chart → FeatureVector using `sercanon`.  
* **Algorithm pipeline (strict sequence)**

  * EM partition (five domains for v1.1).

  * Directional loads (talk/pressure/scalars) from freeze weights.

  * **Q-Bridge (unified, monotonic law)**

    * Path normalization: `len_norm = {1:0.0, 2:0.5, ≥3:1.0}`.  
    * Inputs: `voice ∈ {0,1}`, `symmetry ∈ {0,1}`, `circuit_fit ∈ {0,1}`.  
    * *Q \= 0.35(1 − len\_norm) \+ 0.35voice \+ 0.20symmetry \+ 0.10\*circuit\_fit\`*\*, clipped \[0,1\].  
    * Tests enforce `Q(1) ≥ Q(2) ≥ Q(≥3)`.  
  * **Drive floor (inclusive guard)**

    * Pass if **direct Motor→Throat** OR (**shared-to-Throat** AND `Q ≥ 0.60`).  
    * Prevents “top band without voice”.  
  * **Band mapping**

    * Piecewise ladder (knee \~6) with per-lane caps; monotone around knees; continuity at the knee; no cliffs.  
* **Module tests**

  * Property tests: EM conservation; AB↔BA invariants; Q monotonicity; Drive predicate; band-ladder continuity; “no top-band without Throat”.

    ### **Hard gates**

* Each stage passes independently; knobs read from freeze/catalog (guard fails on inline constants).

  ---

  ## **IV) Conjunction — Facade, Composition & Tooling**

**Goal:** End-to-end deterministic; inspectable.

### **Tasks**

* Orchestrator: canonicalize → EM → loads → Q-Bridge → Drive floor → band map → stable serialize → idempotence\_hash (measure duration\_ms).  
* **CLI defaults:** console script `hd`; commands `hd pair`, `hd chart`, `hd verify`, `hd version`.  
* **Adapter defaults:** dev port **9001**; private bind.  
* **Fixture fetch (dev only):** provider endpoint configurable; cache TTL **24h**.  
* Golden runner (`hd verify`) does AB↔BA & byte-exact assertions.  
* Pre-commit: ruff \+ mypy \+ `pytest -q` slice.

  ### **Hard gates**

* CLI operational; golden sweep green; sanity artifacts deterministic.

  ---

  ## **V) Fermentation — Performance, Safety & Resilience**

**Goal:** Meet budgets; harden rails without changing outputs.

### **Tasks**

* **Performance gates (CI)**

  * Micro-bench over goldens; enforce `p95 ≤ 400 ms`, `p99 ≤ 800 ms` for `compute_pair`.  
* **Robustness**

  * Edge/negative tests: empty/degenerate charts, dupes, unknown keys → typed errors.  
  * Property fuzz over valid ChartV1 space.  
* **Security & privacy**

  * Static proof: core has **no** network/DB/FS imports.  
  * Keys-only logs; diagnostics gated; never hashed.

    ### **Hard gates**

* Perf gate passes; fuzz green; I/O-free core verified.

  ---

  ## **VI) Distillation — Packaging, Identity & Evidence**

**Goal:** Shippable, verifiable, self-describing.

### **Tasks**

* Packaging: pyproject/wheels; reproducible builds; console scripts.  
* Import-time checksum verification of freeze checksums; fail fast on mismatch.  
* Sanity artifacts (deterministic):  
   `sanity/SANITY.json`, `sanity/CHECKSUMS.txt`, `sanity/GOLDEN_REPORT.json`, `sanity/BENCH.json`.  
* **Adapter smoke in CI:** tiny POST `/internal/engine/v1/evaluate` with goldens.

  ### **Hard gates**

* Installable package; stable engine\_tag; sanity artifacts regenerate byte-identically.

  ---

  ## **VII) Coagulation — GA Readiness & Long-Term Discipline**

**Goal:** Freeze public API; prove long-term stability; lock releases.

### **Tasks**

* Stability & compatibility: freeze API signatures; regression tests keep shapes/signatures; prior goldens stay byte-identical across non-math patches.

* Release management:

  * Three identifiers: **doc plan version**, **math release\_id/engine\_tag**, **package version** (change matrix in README).  
  * Tag `engine/<engine_tag>`; publish; rollback doc (select older release\_id).  
* Canary & drift watch:

  * Nightly golden sweep; alert on any hash drift; NDJSON audit stream for batch checks.

    ### **Hard gates**

* GA tag \+ artifacts published; canary active; rollback validated.

  ---

  ## **Don’t-Regress Checklist (enforced)**

* No numerics/HD jargon to SPA — **bands \+ minimal meta only**.  
* One source of knobs: **freeze pack \+ catalog**; no inline IDs/weights.  
* Library is pure: **no I/O, network, DB, or secrets.**  
* Unified envelopes & typed errors across library \+ adapter.  
* `X-Correlation-Id` mandatory; adapter echoes; **no-store** on all Engine JSON.  
* Q-Bridge monotonicity \+ inclusive Drive floor (`Q ≥ 0.60` \+ valid voice route) pinned by tests.  
* **All emitters use `sercanon.stable_dumps`** (tests/CLI/adapter/artifacts are byte-aligned).

  ---

  ## **Closed “Outstanding Asks”**

* **CLI name:** `hd`  
* **Adapter dev port:** `9001` (private bind only)  
* **Fixture fetch (dev):** provider endpoint configurable; **cache TTL 24h**  
* **Pre-commit:** ruff \+ mypy \+ `pytest -q` slice

  ---

  ## **Change Log (this doc)**

* **v3:** Unified Q-Bridge law (monotonic `0.35*(1−len_norm)`); narrative-only & Motor→Throat lists are **freeze-only**; mandated `sercanon` for all emitters; band ladder continuity tests; adapter dev-only limits; identity computation wording tightened; CI adapter smoke added.

  ---

**Repo placement suggestion:** `docs/ENGINE_TASKS.md` (canonical).  
 **Commit suggestion:** `docs: adopt canonical HD Engine Tasks v3 (seven-phase plan, unified Q law)`

* 

