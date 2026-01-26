# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0

**Status:** Canon

**Effective date:** 2026-01-17

**Last Update Gate:** HDE-EPIC024

---

**Intent & scope \[Required-Now\]**

These audits are **Codex review passes run by the Product Owner at the closure of each epic** to compare what actually shipped (code, evidence, repo layout) with what PF-Canon and the epic plan said should exist. Their purpose is to:

* Highlight any **gaps between reality and expectation** (missing evidence, drift from PF docs, unrecorded behavior, or unclosed issues).

* Produce a **historical record** of what was found at close (including any “unknowns” that become future work, PF10 addenda, PF20 issues, or PF09 updates).

* Feed back into canon and planning **after** the epic is closed, without blocking day-to-day execution.

These audits:

* Are **PO-only responsibilities**; they are **not** part of any agent plan, CRD, or implementation workflow.

* Do **not** introduce new acceptance gates for agents and must **not** be treated as tasks or subtasks in PF09 or PF20.

* Are **archived for history** as standalone artifacts (for example, under `audit/codex/...`) so future epics and doc updates can refer to them when reconciling drift.

Agents may **read** these audits as context when planning future work, but they do **not** schedule, trigger, or satisfy them.

# 1\) HD Engine

## 1.1 \- Audit Prompt

You are Codex, auditing the **Glow HD Engine** repository.

Your job is **“what, not how”**:

* **What exists now** in this repo: directories, key files, and flows.

* **Where it aligns or drifts** from the expected HD Engine architecture (engine / adapter / presenter / CLI / vendor / DB / evidence).

* **No changes, no refactors, no suggestions.** Read‑only analysis only.

Do **not** propose new files, flows, or designs. Just describe reality as it is.

---

### 1\. Scope and posture

Assume:

* Current working directory is the **HD Engine repo root**.

* You must treat the repo as **read‑only**.

* Your output is a **descriptive architecture audit**, not an implementation plan.

Stay focused on the **HD Engine** layer and its direct callers (Reader, Aux, CLI, vendor seam, evidence); ignore unrelated FE/app code except where it clearly calls into the engine.

---

### 2\. Top‑level repo map

1. Produce a **top‑level directory map** of the repo:

   * List all top‑level directories and important files (e.g. `engine/`, `adapter/`, `presenter/`, `cli/` or similar, `scripts/`, `docs/`, `artifacts/`, `audit/`, etc.).

   * For each, give a **1–2 sentence description** of what actually lives there (based on code, not assumptions).

2. For the following *expected* HD Engine directories, mark them clearly as:

   * `Present` (and summarize what’s inside),

   * `Present but renamed` (give actual name), or

   * `Not found`.

3. Check at least:

   * `engine/` – deterministic core math.

   * `adapter/` – HTTP/runtime surfaces and guards.

   * `presenter/` – canonical emitter / serializer.

   * Any CLI package (e.g. `cli/`, `hde_cli/`, `hde/cli/`).

   * `docs/` (especially evidence and schemas).

   * `artifacts/` (especially evidence index / core artifacts).

   * `scripts/` (dev and QA helper scripts).

   * `audit/qa/` (if present).

Report this section as a simple list, e.g.:

* `engine/` — Present. Summary…

* `adapter/` — Not found.

* `presenter/` — Present but under `src/hde/presenter/`. Summary…

* etc.

---

### 3\. Engine modules (sampler and core)

Within whatever serves as the **engine** package:

1. Identify the modules that implement:

   * **Sampler behavior** (pool formation / eligibility / ordering / random selection).

   * **Engine Core behavior** (compatibility metrics, AB↔BA parity, normalized result structure).

2. Specifically:

   * Look for modules named like `engine/sampler/core.py`, `engine/sampler/core/__init__.py`, or similar.

   * Look for modules named like `engine/core/core.py` or similar.

   * If those exact modules don’t exist, identify the best real equivalents and give their **file paths**.

3. For each identified engine module:

   * List the **primary classes/functions** and give a **one‑sentence role** for each (e.g. “`SampleRunner` – orchestrates selection given candidate pool and seed.”).

   * Note any **obvious splits or duplicates** (e.g. multiple sampler cores, multiple core modules doing similar work).

---

### 4\. Adapter / HTTP surfaces

1. Locate the **adapter / HTTP layer**:

   * Identify the directory or package that exposes HTTP entrypoints (e.g. FastAPI/Starlette/Flask router, Django views, or custom HTTP server).

   * Give the **main files and routes** (file paths \+ entrypoint symbols).

2. For each HTTP surface you find, classify it if possible:

   * **Reader‑like JSON success** (public compatibility response).

   * **Aux / narrative** (textual outputs).

   * **Admin / internal** endpoints (e.g. `/internal/*`).

   * **Dev or diagnostic harnesses** (e.g. `/internal/dev/sampler`).

3. For each major HTTP route group:

   * Provide the **file path** and the name of the **router/app object** and any key handler functions.

   * Briefly describe what each appears to do (based on code, not guesses).

---

### 5\. Presenter / canonical emitter

1. Identify the **canonical emitter / serializer** component:

   * Find the module(s) that turn internal engine results into final JSON responses or CLI output.

   * Give the file path(s) and primary functions / classes.

2. Check whether there is a **single shared emitter** for multiple surfaces:

   * Does the **HTTP adapter** call into the same emitter module as any **CLI** output?

   * If multiple emitters exist, enumerate them and describe how they differ.

3. Summarize:

   * “There appears to be **one emitter** at `<path>` used by: \[list surfaces\].”

   * Or: “There appear to be **multiple emitters**: \[list\], roles and differences…”

---

### 6\. CLI surfaces

1. Find any **CLI entrypoints** for the HD Engine:

   * Look for console scripts (e.g. in `pyproject.toml`, `setup.cfg`, `setup.py`), or `if __name__ == "__main__"` blocks, or click/typer/FastAPI CLIs.

   * Identify commands related to:

     * Compatibility evaluation / Reader‑equivalent behavior.

     * Admin preview / dumps.

     * Any vendor / BodyGraph tools wired into CLI.

2. For each CLI command:

   * Give the **command name**, **entrypoint function**, and **file path**.

   * Summarize the **call chain** at a high level (CLI → which adapter/engine modules → presenter/emitter).

---

### 7\. Vendor seam and BodyGraph storage

1. Identify where the repo **talks to the external vendor** for BodyGraph data:

   * Search for HTTP client usage (e.g. `requests`, `httpx`, `aiohttp`, etc.) and modules that mention “BodyGraph”, “vendor”, or similar.

   * List the files and functions that shape **vendor requests** and parse responses.

2. Identify the **BodyGraph database/cache** layer:

   * Files and modules implementing persistent storage or caching for BodyGraphs.

   * How the adapter decides between **reading from DB** vs **calling the vendor** (describe what you see, not what “should” happen).

3. Summarize the **actual vendor → adapter → DB → engine** seam:

   * For at least one representative path, show a **short call chain** with file paths and function names.

---

### 8\. Evidence, indices, and catalogs

Check for the **evidence and catalog structure**:

1. Evidence index and mirror:

   * `docs/evidence/INDEX.json`

   * `docs/evidence/INDEX.sha256`

   * `artifacts/evidence_index.jsonl`

2. For each that exists:

   * Confirm presence and give a **one‑sentence** description (e.g. “JSON index of governed artifacts with paths and keys.”).

3. Core evidence families:

   * Under `artifacts/core/**` and `docs/schemas/core/**`, list any **notable artifacts** (e.g. two‑run logs, ABBA logs, JSON compare logs).

   * Give their paths and a brief description of what they represent, based on file names and schema names.

4. Endpoint catalog:

   * Look for `docs/ENDPOINTS_CATALOG.json` and its `.sha256` sidecar (or any similar catalog files).

   * Summarize what you see in these files (route names, metadata), without restating full contents.

---

### 9\. Flows and call chains

For **at least three** representative flows, reconstruct **actual** call chains as they exist today:

1. **Reader success flow** (or closest equivalent):

   * Start from an HTTP Reader‑like route that returns compatibility JSON.

   * Show the chain:  
      `HTTP entrypoint (file:func) → adapter layer (file:func) → engine modules (sampler/core) → presenter/emitter → response`.

   * Include file paths and function/class names at each step.

2. **CLI compatibility / preview flow** (if any):

   * Start from a CLI command that produces Reader‑like output or admin preview.

   * Show the chain similarly.

3. **Vendor ingest / BodyGraph acquisition flow**:

   * Show how a vendor request is shaped and how the result is stored or passed to the engine, based on the real code.

For each flow:

* Use **real symbols and file paths** (e.g. `adapter/http_reader.py:handle_reader_request`).

* Keep descriptions factual and concise (“calls X, then Y, then passes Z to engine.core.core.compute\_pair”).

---

### 10\. Drift and reality check

Finally, produce a **“Reality vs Expectations”** summary:

1. For the canonical expectations implied above (engine/ / adapter/ / presenter/ split, single emitter, vendor seam outside engine, evidence layout, etc.), state for each:

   * `Aligned` – repo structure clearly matches that expectation.

   * `Partial` – some pieces exist, but with differences (summarize).

   * `Drift` – repo clearly does something else (summarize).

2. Call out any **surprises or red flags**, for example:

   * Engine modules doing I/O, network, or time.

   * Vendor HTTP calls being made from inside `engine/`.

   * Multiple emitters with diverging behavior.

   * Missing or empty evidence/index files.

   * Major canonical directories (engine/adapter/presenter) missing or merged.

3. Do **not** propose fixes or designs; just describe the drift in neutral, factual terms.

---

#### Output format

Structure your response in these sections:

1. Repo map

2. Engine modules

3. Adapter / HTTP surfaces

4. Presenter / emitter

5. CLI surfaces

6. Vendor seam & BodyGraph storage

7. Evidence & catalogs

8. Flows & call chains

9. Reality vs Expectations (drift summary)

Within each section, prefer **bullet lists** and **short paragraphs**. Avoid speculation; base everything on what you actually find in this repo.

## 1.2 \- Current Audit 

**Date: 2026-01-17**

**Last Epic: HDE-024**

# **Repo map**

## **Top-level directories (all present at repo root)**

For directories where I did not inspect contents, I state that explicitly (no claims beyond existence). For key HD Engine-related directories, I summarize based on code and artifacts.

* `_arch/` — Directory present; contents not inspected in this audit.  
* `_archive/` — Directory present; contents not inspected in this audit.  
* `_backup_1761350008.tgz` — Top-level backup file present (not inspected).  
* `_backup_corrupted_1761349750.tgz` — Top-level backup file present (not inspected).  
* `_backup_corrupted_1761349780.tgz` — Top-level backup file present (not inspected).  
* `adapter/` — Present. Flask adapter with app factories, HTTP routes, env guards, and WSGI wiring (e.g., `adapter/wsgi.py`, `adapter/http_reader.py`, `adapter/factory.py`).  
* `artifacts/` — Present. Evidence bundles, canonical artifacts, and generated outputs including evidence index mirror and multiple evidence families (e.g., `artifacts/evidence_index.jsonl`, core artifacts in `artifacts/core/*`).  
* `assert/` — Directory present; contents not inspected in this audit.  
* `audit/` — Present. QA and epic manifests/close reports, plus governed QA/evidence outputs under `audit/qa/*`.  
* `catalog/` — Directory present; contents not inspected in this audit.  
* `ci/` — Directory present; contents not inspected in this audit.  
* `codex/` — Directory present; contents not inspected in this audit.  
* `config/` — Directory present; contents not inspected in this audit.  
* `dev/` — Directory present; contents not inspected in this audit.  
* `docs/` — Present. Acceptance maps, evidence index, endpoint catalog, and PF canon docs; evidence index files live under `docs/evidence`.  
* `engine/` — Present. Engine core, sampler, compat, runtime, db, bodygraph, CLI, and HTTP compat handler live here (e.g., `engine/core/core.py`, `engine/sampler/core.py`, `engine/cli/main.py`).  
* `errors/` — Directory present; contents not inspected in this audit.  
* `fixtures/` — Directory present; contents not inspected in this audit.  
* `freeze/` — Directory present; contents not inspected in this audit.  
* `glow_hdengine.egg-info/` — Directory present; contents not inspected in this audit.  
* `goldens/` — Directory present; contents not inspected in this audit.  
* `handoff/` — Directory present; contents not inspected in this audit.  
* `import/` — Directory present; contents not inspected in this audit.  
* `internal/` — Directory present; contents not inspected in this audit.  
* `math/` — Directory present; contents not inspected in this audit.  
* `migrations/` — Directory present; contents not inspected in this audit.  
* `narratives/` — Directory present; contents not inspected in this audit.  
* `notes/` — Directory present; contents not inspected in this audit.  
* `parity/` — Directory present; contents not inspected in this audit.  
* `presenter/` — Present. Reader v1 emitter lives here (`presenter/reader_v1/emitter.py`).  
* `proofs/` — Directory present; contents not inspected in this audit.  
* `release/` — Directory present; contents not inspected in this audit.  
* `reports/` — Directory present; contents not inspected in this audit.  
* `scan_reports/` — Directory present; contents not inspected in this audit.  
* `schemas/` — Directory present; contents not inspected in this audit.  
* `scripts/` — Present. Dev/ops/QA helper scripts and release/evidence tooling entrypoints (e.g., `scripts/dev_start_reader.sh`, `scripts/release_id_recompute.py`).  
* `sql/` — Directory present; contents not inspected in this audit.  
* `tests/` — Directory present; test suite paths defined in `pytest.ini`.  
* `tools/` — Directory present; contents not inspected in this audit.  
* `validation/` — Directory present; contents not inspected in this audit.

## **Top-level important files**

* `AGENTS.md` — Repo-wide agent rules, evidence discipline, and EPIC guidance (governs agent behavior).  
* `README.md` — Describes repo posture, evidence tooling, CLI usage, and determinism/evidence artifacts (EPIC024 sweep).  
* `pyproject.toml` — Project metadata and CLI entrypoint (`hdctl = engine.cli.main:cli`).  
* `Procfile` — Declares Gunicorn launch command using `adapter.factory:create_app()`.  
* `pytest.ini` — Pytest config and test paths.  
* `requirements.txt` — Runtime deps (psycopg, Flask, gunicorn).  
* `requirements-dev.txt` — Dev/test-only deps (jsonschema).

## **Expected HD Engine directories (presence check)**

* `engine/` — Present. Deterministic core, compat, sampler, runtime, db, bodygraph, and CLI are in `engine/*` packages (e.g., `engine/core/core.py`, `engine/sampler/core.py`, `engine/cli/main.py`).  
* `adapter/` — Present. Flask adapter, HTTP routes, and env guard in `adapter/*`.  
* `presenter/` — Present. Reader v1 emitter in `presenter/reader_v1/emitter.py`.  
* CLI package — Present as `engine/cli` with entrypoint `engine.cli.main:cli` in `pyproject.toml`.  
* `docs/` — Present. Evidence index and endpoint catalog live here (`docs/evidence/INDEX.json`, `docs/ENDPOINTS_CATALOG.json`).  
* `artifacts/` — Present. Evidence index mirror and core artifacts (e.g., `artifacts/evidence_index.jsonl`, `artifacts/core/*`).  
* `scripts/` — Present. Release/evidence scripts and dev helper tooling live here.  
* `audit/qa/` — Present. QA outputs under `audit/qa/*` (e.g., EPIC024).

# **Engine modules**

## **Sampler behavior**

**Module:** `engine/sampler/core.py`

* `ViewerProfile` — Minimal viewer state for sampler inputs.  
* `CandidateFeatures` — Normalized candidate input fields (weight, score, band, diversity key, etc.).  
* `SamplerConfig` — Sampler config knobs (compat thresholds, band inclusion/exclusion, diversity key requirement).  
* `build_candidate_pool` — Filters candidates by zero weight and eligibility into `CandidatePool`.  
* `rank_candidates` — Deterministic ordering by weight, compat score, band priority, and ID tie-breaker.  
* `sample_and_rank` — Convenience wrapper calling pool \+ rank.

Duplicates/splits: No duplicate sampler core modules found; `engine/sampler/core.py` is the primary sampler core.

## **Engine core behavior**

**Module:** `engine/core/core.py`

* `ParticipantState` — Input state for viewer/candidate (id, score, band, traits).  
* `CoreConfig` — Config for band priority ordering.  
* `PerspectiveBreakdown` — Directional metrics (viewer/candidate delta).  
* `CoreResult` — Output structure (neutral score, ordered pair, ordered bands, shared traits, perspective).  
* `compute_core` — Core computation for AB↔BA neutrality, ordered bands, shared traits, and perspective breakdown.

Duplicates/splits: No duplicate core modules found; `engine/core/core.py` is the primary core module.

# **Adapter / HTTP surfaces**

## **Flask app factories and registration**

* `adapter/wsgi.py` — `create_app()` registers reader blueprint (`adapter/http_reader.py`) and compat blueprint (`engine/http/compat_handler.py`), sets common headers, and defines `/internal/healthz` and `/internal/readyz`.  
* `adapter/factory.py` — Minimal factory used in `Procfile` to register the reader blueprint and strip ETags on `/internal/*`.  
* `adapter/app.py` — Exposes `app = create_app()` for `flask --app` entrypoint.

## **HTTP routes in `adapter/http_reader.py`**

Reader-like public JSON success (dev-gated):

* `GET /reader` — Loads A/B charts from filesystem, emits Reader v1 canonical bytes via `emit_reader_public_bytes`.

Aux/narrative text output:

* `GET /api/aux/narrative` and `GET /aux/narrative` — Emits text narrative via `emit_public_aux` with narrative headers/ETags.

Admin/internal endpoints:

* `GET /internal/version` — Emits internal version payload (release id, engine tag, emitter sha, invocation tags).  
* `POST/HEAD/OPTIONS /ops/writer/diagnostic` — Admin-scoped idempotence/diagnostic writer endpoint.  
* `GET /ops/db/unavailable` — Simulates DB unavailable path and returns error envelope under No-IO guard.  
* `GET|POST /ops/rails/refusal` — Emits rails-closed refusal error envelope.  
* `GET /ops/probe/env` — Emits rails/environment probe info (pid, started\_at, rails state).

Dev/diagnostic harnesses:

* `POST /internal/dev/sampler` — Dev-only sampler harness using `engine.sampler.core.sample_and_rank`.

## **Compat HTTP surface (`engine/http/compat_handler.py`)**

Compat writer endpoints under `/api/compat/v1`:

* `GET /api/compat/v1` — Accepts `a_id`, `b_id`, builds default viewer prefs, uses `compat_public`.  
* `POST /api/compat/v1` — JSON body for a/b payloads or IDs; validates viewer prefs; uses `compat_public`.  
* `HEAD/OPTIONS` — Writer transport guard for POST semantics.

# **Presenter / emitter**

## **Canonical emitter**

**Module:** `engine/presenter/emitter.py` — canonical JSON emitter via `engine.serializer.canon.sercanon` used across adapter and CLI. Provides `emit_public`, `emit_public_with_envelope`, and `emit_compact_json`.

## **Reader v1 emitter**

**Module:** `presenter/reader_v1/emitter.py` — constructs Reader v1 envelope, computes idempotence hash, and emits canonical bytes through `engine.presenter.emitter`.

## **Shared use across surfaces**

* HTTP adapter: `adapter/http_reader.py` uses `engine.presenter.emitter.emit_public` for writer/error/aux responses and `engine.runtime.emit_reader_public_bytes` for Reader v1 responses.  
* Compat HTTP: `engine/http/compat_handler.py` uses `engine.presenter.emit_public` for compatibility payload envelopes.  
* CLI: `engine/cli/main.py` uses `engine.presenter.emitter.emit_public` for CLI output and `engine.runtime.emit_reader_public_envelope` for Reader v1 bytes.

Summary: There appear to be multiple emitters: a general canonical emitter at `engine/presenter/emitter.py` used by HTTP/CLI surfaces, and a Reader-specific emitter at `presenter/reader_v1/emitter.py` that wraps idempotence hashing for Reader v1 outputs.

# **CLI surfaces**

## **Entry point**

`hdctl` CLI is declared in `pyproject.toml` with entrypoint `engine.cli.main:cli`.

## **Commands and call chains (high-level)**

* `showcompat` — entrypoint: `engine.cli.main.showcompat`.  
  Flow: CLI parse → showcompat → (optional) vendor or DB ingestion → compute compat via `engine.compat.compute.compat_public` → emit compat JSON via `engine.presenter.emitter.emit_public` → emit Reader bytes via `engine.runtime.emit_reader_public_envelope`.  
* `aux-preview` — entrypoint: `engine.cli.main.aux_preview`.  
  Flow: CLI parse → aux\_preview → `engine.narratives.emit_public_aux` → outputs narrative text and optional admin sidecar.  
* `bg:resolve` — entrypoint: `engine.cli.main.bg_resolve`.  
  Flow: CLI parse → resolve\_bodygraph (control-flow stub) → emit JSON envelope via `engine.presenter.emitter.emit_public`.  
* `dev:sampler` — entrypoint: `engine.cli.main.dev_sampler_run`.  
  Flow: CLI parse → dev env gate → `engine.sampler.core.sample_and_rank` → output canonical JSON.

# **Vendor seam & BodyGraph storage**

## **Vendor request/response shaping**

Vendor client: `engine/bodygraph/vendor_client.py` defines `HdApiClient`, `VendorRequest`, `VendorResult`, and implements `build_request` (request shaping) and `fetch` (HTTP POST using urllib with retries/backoff).

## **Ingest and persistence**

Ingest pipeline: `engine/bodygraph/ingest.py` handles vendor calls via `HdApiClient`, computes hashes, and (when not dry-run) persists payloads to DB via `engine.db.DBAccess` using Statement transactions and row counts. It also records ingest logs and JSON canon compare logs.

# **DB adapter / storage layer**

* DB facade: `engine/db/adapter.py` provides `DBAccess.for_current_env` with provider selection (psycopg vs bridge), and exposes query/exec/tx/introspect.

Decision point: DB vs vendor

Resolver control-flow: `engine/bodygraph/resolver.py` chooses vendor or db based on source plus rails flags (SAFE\_MODE / ALLOW\_NETWORK), returning a structured envelope without direct IO for non-vendor paths; when `source="vendor"` and rails allow, it calls `ingest_vendor_bodygraph`.

Representative call chain (vendor ingest):

`engine/cli/main.py:showcompat (source=vendor)` → `engine/bodygraph/ingest.ingest_vendor_bodygraph` (dry\_run in CLI path) → `engine/bodygraph/vendor_client.HdApiClient.build_request` → `HdApiClient.fetch` for HTTP → (if non-dry-run) `engine.db.DBAccess` for persistence and parity checks.

# **Evidence & catalogs**

## **Evidence index and mirror**

* `docs/evidence/INDEX.json` — Human-readable evidence index (JSON array of artifact records).  
* `docs/evidence/INDEX.sha256` — Hash for `docs/evidence/INDEX.json`.  
* `artifacts/evidence_index.jsonl` — Machine mirror JSONL with artifact records and proof anchors.

## **Core evidence families**

Core artifacts (engine core): `artifacts/core/abba/ab_ba_parity.json`, `artifacts/core/json_compare/core_result_json_compare.json`, `artifacts/core/purity/purity_report.json`, `artifacts/core/two_run/identity.json`. These align with corresponding schemas under `docs/schemas/core/*.schema.json`.

Sampler evidence schemas also appear in `docs/schemas/sampler/*` (listed in evidence mirror).

## **Endpoint catalog**

`docs/ENDPOINTS_CATALOG.json` — Endpoint catalog currently listing `/internal/version` only (with methods, description, and eligibility flag).

# **Flows & call chains**

## **Reader success flow (HTTP)**

Route: `adapter/http_reader.py:reader_v1 (GET /reader)` → `engine.runtime.emit_reader_public_bytes` → `_compute_harmony_band` (ts\_v0 features) → `presenter.reader_v1.emitter.emit_reader_v1` → `engine.presenter.emitter.emit_public` → `engine.serializer.canon.sercanon` (via emitter).

## **CLI compatibility flow**

Command: `hdctl showcompat` → `engine.cli.main.showcompat` → `engine.compat.compute.compat_public` → `engine.presenter.emitter.emit_public` (compat payload) → `engine.runtime.emit_reader_public_envelope` (Reader bytes).

## **Vendor ingest / BodyGraph acquisition flow**

Command: `hdctl showcompat --source vendor` → `engine.cli.main.showcompat` → `engine.bodygraph.ingest.ingest_vendor_bodygraph` (dry\_run in CLI) → `engine.bodygraph.vendor_client.HdApiClient.build_request` → `HdApiClient.fetch` → (non-dry-run path would persist via `engine.db.DBAccess`).

# **Reality vs Expectations (drift summary)**

## **Structural expectations**

* Engine / adapter / presenter split: Aligned. Distinct `engine/`, `adapter/`, and `presenter/` packages exist with clear responsibilities (core logic, HTTP surface, and Reader emitter).  
* CLI package: Aligned. CLI entrypoint is defined in `pyproject.toml` and implemented in `engine/cli/main.py`.  
* Evidence layout: Aligned. Human index in `docs/evidence/INDEX.json` and mirror in `artifacts/evidence_index.jsonl`.  
* Docs / schemas presence: Aligned. Core schemas live under `docs/schemas/core/*`, and endpoint catalog exists.

## **Potential drift / surprises**

* Multiple emitters: Partial / Drift. There is a general canonical emitter (`engine/presenter/emitter.py`) and a Reader-specific emitter (`presenter/reader_v1/emitter.py`) with idempotence hash logic; this is more than a single emitter module.  
* Vendor I/O inside `engine/` tree: Drift. Network/vendor calls and DB persistence for BodyGraph ingest are implemented inside `engine/bodygraph/*` and `engine/db/*`, meaning I/O and network logic live under the engine/ package rather than purely in adapter layers.  
* Adapter vs engine HTTP surfaces: Partial. Adapter routes include Reader and ops/internal endpoints, while compat routes are defined under `engine/http/compat_handler.py` but registered by the adapter. This is a split of HTTP definition across adapter and engine.

# **Commands run (read-only discovery)**

* `ls`  
* `rg --files -g 'AGENTS.md'`  
* `cat AGENTS.md`  
* `ls engine`  
* `ls adapter`  
* `ls presenter`  
* `ls scripts`  
* `ls docs`  
* `ls artifacts`  
* `ls audit`  
* `ls engine/sampler`  
* `ls engine/core`  
* `nl -ba engine/sampler/core.py | sed -n '1,220p'`  
* `nl -ba engine/core/core.py | sed -n '1,260p'`  
* `nl -ba adapter/app.py | sed -n '1,240p'`  
* `nl -ba adapter/http_reader.py | sed -n '1,240p'`  
* `nl -ba adapter/wsgi.py | sed -n '1,200p'`  
* `nl -ba adapter/env_guard.py | sed -n '1,200p'`  
* `rg -n "bp|Blueprint|route|@bp" adapter/http_reader.py`  
* `nl -ba adapter/http_reader.py | sed -n '260,520p'`  
* `nl -ba adapter/http_reader.py | sed -n '520,820p'`  
* `nl -ba engine/http/compat_handler.py | sed -n '1,260p'`  
* `rg -n "def emit|class" engine/presenter -g '*.py'`  
* `nl -ba engine/presenter/emitter.py | sed -n '1,200p'`  
* `ls presenter/reader_v1`  
* `nl -ba presenter/reader_v1/emitter.py | sed -n '1,200p'`  
* `nl -ba engine/runtime/__init__.py | sed -n '1,200p'`  
* `nl -ba engine/runtime/public.py | sed -n '1,240p'`  
* `rg -n "\[project.scripts\]|console_scripts|entry_points" pyproject.toml setup.cfg setup.py`  
* `nl -ba pyproject.toml | sed -n '1,120p'`  
* `nl -ba engine/cli/main.py | sed -n '1,260p'`  
* `rg -n "def showcompat|def aux_preview|def dev_sampler_run" -n engine/cli/main.py`  
* `nl -ba engine/cli/main.py | sed -n '520,740p'`  
* `nl -ba engine/cli/main.py | sed -n '740,940p'`  
* `ls engine/bodygraph`  
* `nl -ba engine/bodygraph/__init__.py | sed -n '1,200p'`  
* `nl -ba engine/bodygraph/resolver.py | sed -n '1,260p'`  
* `nl -ba engine/bodygraph/ingest.py | sed -n '1,260p'`  
* `nl -ba engine/bodygraph/vendor_client.py | sed -n '1,260p'`  
* `ls engine/db`  
* `nl -ba engine/db/__init__.py | sed -n '1,200p'`  
* `nl -ba engine/db/adapter.py | sed -n '1,260p'`  
* `nl -ba engine/db/errors.py | sed -n '1,200p'`  
* `ls docs/evidence`  
* `nl -ba docs/ENDPOINTS_CATALOG.json | sed -n '1,200p'`  
* `nl -ba docs/evidence/INDEX.json | sed -n '1,120p'`  
* `nl -ba docs/evidence/INDEX.sha256 | sed -n '1,120p'`  
* `nl -ba artifacts/evidence_index.jsonl | sed -n '1,160p'`  
* `ls artifacts/core`  
* `ls docs/schemas/core`  
* `ls artifacts/core/abba`  
* `ls artifacts/core/json_compare`  
* `ls artifacts/core/purity`  
* `ls artifacts/core/two_run`  
* `ls audit/qa`  
* `rg -n "def compat_public|def band_for" engine/compat/compute.py`  
* `nl -ba engine/compat/compute.py | sed -n '1,200p'`  
* `nl -ba README.md | sed -n '1,120p'`  
* `nl -ba Procfile | sed -n '1,80p'`  
* `nl -ba pytest.ini | sed -n '1,120p'`  
* `nl -ba requirements.txt | sed -n '1,120p'`  
* `nl -ba requirements-dev.txt | sed -n '1,120p'`  
* `nl -ba adapter/factory.py | sed -n '1,200p'`

