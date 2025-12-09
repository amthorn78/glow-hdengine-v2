# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v0.4

**Status:** Canon

**Effective date:** 2025-12-07

**Last Update Gate:** HDE-EPIC020

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

**Date: 2025-12-07**

**Last Epic: HDE-020**

**Repo map**

* `engine/` — Present. Core Python package with compatibility math, sampler, presenter/emitter, runtime helpers, BodyGraph ingest/resolver, CLI, serializer, and supporting modules.

* `adapter/` — Present. Flask HTTP layer with reader/aux/admin/writer/dev sampler routes plus app factory and compat blueprint registration.

* `presenter/` — Present (separate top-level package) housing Reader v1 emitter and JSON compare helper.

* `engine/presenter/` — Present (inside `engine`) providing the canonical JSON emitter for public envelopes.

* **CLI package** — Present under `engine/cli` with argparse-based `hdctl` commands.

* `docs/` — Present with evidence index/checksums and runtime endpoint data.

* `artifacts/` — Present with evidence index mirror and core artifact families (`abba` / `json_compare` / `purity` / `two_run`).

* `scripts/` — Present with helper scripts (listed at top level).

* `audit/` — Present with audit materials (and nested `AGENTS`).

* Other top-level roots (`adapter` HTTP schemas, `ci/`, `tests/`, `tools/`, `fixtures/`, etc.) are present, reflecting QA and support assets.

---

## **Engine modules**

**Sampler (`engine/sampler/core.py`).**  
 Defines data classes (`ViewerProfile`, `CandidateFeatures`, `SamplerConfig`) and deterministic pool/ranking helpers (`build_candidate_pool`, `rank_candidates`, `sample_and_rank`) that filter zero-weight/ineligible candidates and sort by weight, compat score, band priority, and ID tie-breakers.

**Engine Core (`engine/core/core.py`).**  
 Provides pure-compute metrics via `compute_core`, with participant state structures, AB/BA-neutral ordering, band priority handling, shared trait canonicalization, and perspective breakdown.

---

## **Adapter / HTTP surfaces**

**Reader dev harness (`adapter/http_reader.py`).**

* Blueprint exposes `GET/HEAD /reader` (dev-gated) returning canonical Reader bytes from `emit_reader_public_bytes`, including ETag handling.

**Aux narrative.**

* Same blueprint handles `GET /api/aux/narrative` and `/aux/narrative`, emitting `text/plain` narratives or suppressed responses with provenance headers.

**Rails/admin probes.**

* `/ops/rails/refusal` and `/ops/probe/env` return writer-style envelopes or environment snapshots, gating via `NoIoGuard` and environment state.

**Dev sampler harness.**

* `POST /internal/dev/sampler` (`APP_ENV` dev/test/local) validates payload, builds sampler inputs, calls `sample_and_rank`, and returns ranked candidate IDs in JSON.

**Internal version.**

* `/internal/version` `GET/HEAD` emits engine identity JSON without ETag.

**Diagnostic writer.**

* `/ops/writer/diagnostic` `POST/HEAD/OPTIONS` provides admin-idempotent writer surface with JSON envelope and cache/length rules.

**Compat routes (`engine/http/compat_handler.py`).**

* Registers `compat_blueprint` at `/api/compat/v1`, offering `GET` ids-only and `POST` JSON compatibility responses with writer-style transport guards and `HEAD/OPTIONS` handling.

**App factory.**

* `create_app()` in `adapter/http_reader.py` mounts reader/internal/admin routes and compat blueprint, plus scoped `404/405` handlers.

---

## **Presenter / emitter**

**Canonical emitter (`engine/presenter/emitter.py`).**

* Serializes public envelopes via canonical serializer, optionally returning envelope along with bytes.

* Used across HTTP, CLI, and vendor ingest paths.

**Reader-specific emitter (`presenter/reader_v1/emitter.py`).**

* Builds Reader preimage, computes idempotence hash, and emits canonical bytes, invoked by runtime public helper.

**Shared usage.**

* HTTP Reader route uses `emit_reader_public_bytes` → Reader emitter.

* CLI `showcompat` writes compat JSON via `engine.presenter.emitter.emit_public` and Reader envelope via runtime helper.

* Vendor ingest uses `emit_public_with_envelope` for payloads and DB parity.

---

## **CLI surfaces**

**Entry script (`engine/cli/main.py`, `hdctl`).**

Defines subcommands:

* `showcompat`

  * Loads payloads from files/DB/vendor, computes compat via `compat_public`, emits Reader envelope via `emit_reader_public_envelope`, optionally dumps admin artifacts, and writes compat JSON to stdout.

* `aux-preview`

  * Previews narrative text for compat outputs using `emit_public_aux` (definition not shown but imported).

* `bg:resolve`

  * Resolves BodyGraphs through resolver or vendor ingestion (with dry-run support).

* `dev:sampler`

  * Dev/admin-only harness that loads candidate payloads, normalizes categories, runs `sample_and_rank`, and emits JSON via presenter emitter.

**Dispatcher.**

* `engine/cli/__main__.py` dispatches to `main` (present but not detailed).

* Entry advertised via pyproject console script (per instructions in `AGENTS`, not re-opened here).

---

## **Vendor seam & BodyGraph storage**

**Vendor client (`engine/bodygraph/vendor_client.py`).**

* Constructs HTTPS requests, validates inputs, and performs retries/timeouts for HD API calls (dataclasses `VendorRequest` / `Result` / `RetryConfig` / `Timeouts`) — invoked by ingest.

**Ingest path (`engine/bodygraph/ingest.py`).**

* Gathers inputs, checks SAFE/ALLOW rails, builds request via `HdApiClient.from_env`, fetches vendor payload, computes idempotency keys, optionally writes to DB via `DBAccess` with row counts and parity checks, and logs success/canon-compare records.

**Storage.**

* `_persist_bodygraph` / `_fetch_payload` (not shown in snippet) operate through `DBAccess`.

* Parity between vendor bytes and DB-emitted bytes is verified before returning `IngestOutcome`.

**Resolver/CLI.**

* `showcompat` uses `ingest_vendor_bodygraph(..., dry_run=True)` when `--source=vendor`, passing payloads to compat/presenter without DB writes.

---

## **Evidence & catalogs**

**Evidence index.**

* `docs/evidence/INDEX.json` and checksum/path proofs exist; mirror index at `artifacts/evidence_index.jsonl`.

**Core artifacts.**

* `artifacts/core/abba/ab_ba_parity.json`,

* `artifacts/core/json_compare/`,

* `artifacts/core/purity/`,

* `artifacts/core/two_run/` directories are present as parity/purity/two-run evidence families (names imply scope).

**Endpoint catalog.**

* `docs/run/PROD_ENDPOINTS.json` lists production base URL/provider with path proof sidecar.

---

## **Flows & call chains**

**Reader success (dev harness).**

* HTTP `GET /reader` in `adapter/http_reader.py`  
   → validates query/`APP_ENV`  
   → loads charts  
   → calls `emit_reader_public_bytes` from `engine.runtime.public`  
   → computes band via `ts_v0`  
   → delegates to `presenter.reader_v1.emit_reader_v1`  
   → canonical emitter  
   → response with ETag/headers.

**CLI compatibility (`hdctl showcompat`).**

* `engine/cli/main.py:showcompat`  
   → loads inputs (files/DB/vendor)  
   → canonicalizes pair  
   → computes compat via `compat_public`  
   → emits compat JSON via canonical emitter  
   → generates Reader bytes via `emit_reader_public_envelope` (runtime → Reader emitter)  
   → writes outputs/dumps.

**Vendor ingest/acquisition.**

* CLI `showcompat --source=vendor`  
   → `_vendor_inputs_from_args`  
   → `ingest_vendor_bodygraph` (rails checks, `HdApiClient.build_request`/fetch, payload emission/idempotency)  
   → returns payload to CLI  
   → CLI converts to person/chart and feeds compat/runtime emitters.

**Dev sampler HTTP harness.**

* `POST /internal/dev/sampler`  
   → validates viewer/candidate IDs  
   → constructs `ViewerProfile` / `CandidateFeatures`  
   → calls `sample_and_rank` (sampler core)  
   → emits ranked IDs with canonical emitter.

---

## **Reality vs Expectations (drift summary)**

* `engine/` present and pure-compute sampler/core align with expectations (no I/O, deterministic ordering).

* `adapter/` HTTP layer present with reader/aux/admin/dev/writer endpoints plus compat blueprint; aligns with adapter role, though writer/admin/dev surfaces are co-located in the same module.

* `presenter/` emitter split exists, with canonical emitter shared across HTTP/CLI/ingest; additional reader-specific emitter under `presenter/reader_v1` maintains a shared path — aligned.

* CLI surface is present; it uses engine runtime/presenter and vendor ingest/DB access directly, consistent with expected `hdctl` behaviour.

* Vendor seam lives outside engine core via ingest \+ `HdApiClient` with DB persistence; relies on environment rails for network, which matches separation expectations.

* Evidence structure present (`INDEX` and `artifacts/core`) with mirrors/checksums; endpoint catalog exists but under `docs/run` rather than a top-level catalog filename — partial alignment.

* Architecture expectations are largely met; minor drift: Reader dev harness only (`APP_ENV` dev), admin/writer endpoints co-located with Reader blueprint, and vendor ingest includes DB writes within ingest module rather than a separate adapter layer.

   
