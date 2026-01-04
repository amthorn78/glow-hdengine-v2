# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v0.7

**Status:** Canon

**Effective date:** 2025-12-30

**Last Update Gate:** HDE-EPIC021-2

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

**Date: 2025-12-30**

**Last Epic: HDE-022**

### Repo map

Top-level items include core code directories (`engine/`, `adapter/`, `presenter/`), docs/evidence (`docs/`, `artifacts/`, `audit/`), tooling (`scripts/`, `tools/`, `ci/`), and support assets (`fixtures/`, `schemas/`, `narratives/`, `parity/`).

#### Expected directories

* **`engine/`** — Present. Houses deterministic core modules, sampler, compat logic, runtime, presenter, serializer, and DB/provider helpers.  
* **`adapter/`** — Present. Flask HTTP app/blueprints, env/ETag guards, and schemas for request/response handling.  
* **`presenter/`** — Present but split: canonical emitter in `engine/presenter/` plus legacy reader emitter under top-level `presenter/reader_v1/`.  
* **CLI package** — Present under `engine/cli/` with console script `hdctl` defined in `pyproject.toml` (`project.scripts`).  
* **`docs/`** — Present with acceptance maps, PF canon docs, and evidence index materials.  
* **`artifacts/`** — Present with governed evidence indexes, math/release artifacts, sampler/core evidence, etc.  
* **`scripts/`** — Present for dev/QA helpers (listed at top level).  
* **`audit/qa/`** — QA assets live under `audit/qa/` alongside epic manifests and close reports.

---

### Engine modules

#### Sampler core

`engine/sampler/core.py` defines pure-compute dataclasses (`ViewerProfile`, `CandidateFeatures`, `SamplerConfig`) and deterministic functions `build_candidate_pool`, `rank_candidates`, `sample_and_rank`, using compat bands and canonical ID ordering; no randomness or I/O.

#### Engine core

`engine/core/core.py` provides `ParticipantState`, `CoreConfig`, and `compute_core` that derive neutral scores, ordered IDs/bands, shared traits, and perspective deltas via canonical comparators; also pure-compute, no side effects.

---

### Adapter / HTTP surfaces

#### Primary adapter blueprint and internal routes

Main Flask app in `adapter/http_reader.py` builds blueprint `bp` with multiple routes:

* `/reader` dev-only compatibility emitter  
* `/api/aux/narrative` text surface  
* `/internal/version`  
* ops diagnostics (rails/db)  
* dev sampler harness  
* writer diagnostic endpoints

Uses canonical emitters and NoIo guards where applicable.

#### Compat writer surface

Compat writer surface in `engine/http/compat_handler.py` exposes `/api/compat/v1` `GET/POST/HEAD/OPTIONS` with writer-style envelopes and validation, returning compat payloads computed via `engine.compat.compute.compat_public`.

#### App factory posture

App factory registers both reader/ops blueprint and compat blueprint, with error handlers scoped to compat paths and internal ETag stripping.

#### Route classifications

* **Reader-like JSON:** `/reader` (dev-only) returns canonical reader bytes and ETag handling.  
* **Aux/narrative:** `/api/aux/narrative` and `/aux/narrative` emit narrative text with pack metadata headers.  
* **Admin/internal:** `/internal/version`, `/ops/db/unavailable`, `/ops/rails/refusal`, `/ops/probe/env`, `/ops/writer/diagnostic` for rails/identity probes and writer diagnostics.  
* **Dev/diagnostic harness:** `/internal/dev/sampler` `POST` for deterministic sampler testing gated by `APP_ENV`.

---

### Presenter / emitter

#### Canonical emitter

Canonical emitter is `engine/presenter/emitter.emit_public`, delegating to canonical serializer for LF-terminated JSON; variants return envelopes alongside bytes.

#### Serializer

`engine/serializer/canon.py` wraps `engine.stable.sercanon` to enforce deterministic UTF-8 JSON with optional key sorting.

#### Reader-specific emitter

Reader-specific emitter lives in `presenter/reader_v1/emitter.py`, producing reader envelopes with idempotence hash based on preimage bytes, using the canonical emitter for serialization.

#### Shared usage

HTTP adapters and CLI both rely on `emit_public` for JSON emission; reader bytes are built via `engine.runtime.public.emit_reader_public_envelope/bytes` which delegate to the `reader_v1` emitter.

---

### CLI surfaces

Console script `hdctl` wired to `engine.cli.main:cli` with subcommands:

* `showcompat` builds compat payloads from files/stdin or DB/vendor sources, calls `compat_public`, and also emits reader bytes; optional admin dumps and reader dumps supported.  
* `aux-preview` renders narrative text and optional admin sidecar based on compat outputs or explicit inputs.  
* `bg:resolve` drives BodyGraph resolution stub via `resolve_bodygraph`, emitting JSON envelope.  
* `dev:sampler` runs deterministic sampler over provided candidates and emits canonical JSON listing ranks.

**Call chains:** CLI entry parsing → handler functions → engine/bodygraph resolution or compat computations → emitters/serializer for output.

---

### Vendor seam & BodyGraph storage

#### Vendor HTTP client

Vendor HTTP client implemented in `engine/bodygraph/vendor_client.py` (`HdApiClient`) with HTTPS requirement, retry/backoff, and JSON parsing; exposes `build_request` and `fetch` that log attempts and map statuses to typed errors.

#### Ingest flow

Ingest flow `engine/bodygraph/ingest.py` orchestrates vendor call via `HdApiClient`, canonicalizes payload bytes, computes idempotency key, and persists results to `hde.body_graphs` table via `DBAccess`; dry-run path logs without DB writes.

#### Resolver

Resolver `engine/bodygraph/resolver.py` chooses source (vendor vs auto/db stub), enforcing rails flags; vendor path normalizes user id, calls ingest, and wraps outcome in resolver envelope with exit codes.

#### DB access selection vs vendor

Resolver returns vendor error envelopes if SAFE\_MODE or network blocked; otherwise proceeds to ingest; auto/db path is stubbed as “no IO performed.”

---

### Evidence & catalogs

* Evidence index and mirror artifacts present: `docs/evidence/INDEX.json` with path proofs/sha sidecars, mirrored by `artifacts/evidence_index.jsonl` and its path proof; rooted in evidence governance docs.  
* Artifacts contain core/sampler evidence families (e.g., `artifacts/core`, `artifacts/sampler`), math/release identity files, and ops/ingest logs; directories enumerated in artifacts listing.  
* Endpoint catalog present as `docs/run/PROD_ENDPOINTS.json` with prod base URL metadata plus path-proof sidecar.

---

### Flows & call chains

#### Reader success (dev) HTTP

`adapter/http_reader.py:reader_v1` validates params/env, loads charts, and calls `emit_reader_public_bytes` → `engine/runtime/public.emit_reader_public_envelope` (computes band via `compat.ts_v0`) → `presenter/reader_v1/emitter.emit_reader_v1` → `engine/presenter/emitter.emit_public` for bytes returned with ETag handling.

#### CLI compatibility flow

`engine/cli/main.py:showcompat` resolves parties (files/db/vendor via ingest), computes features and compat via `compat_public`, builds reader bytes through `emit_reader_public_envelope`, and writes canonical compat JSON to stdout (and optional dumps) via `engine.presenter.emitter`.

#### Vendor ingest/BodyGraph acquisition

`resolve_bodygraph` (source vendor) → `_resolve_inputs` and `resolve_db_user_id` → `ingest_vendor_bodygraph` (rails checks, `HdApiClient.fetch`, payload hash/idempotency, DB persistence) → returns `IngestOutcome` embedded in resolver payload.

---

### Reality vs Expectations (drift summary)

* Engine/adapter/presenter split largely present: deterministic compute modules in `engine/`, HTTP adapters in `adapter/`, canonical emitter in `engine/presenter/`, with reader-specific emitter under legacy top-level `presenter/` (partial naming drift).  
* Single emitter shared across surfaces: both HTTP and CLI use `emit_public` plus reader runtime wrapper; aligns with expectation of canonical serialization.  
* Vendor seam separated from engine core: network/DB calls live in `engine/bodygraph/*` and not in sampler/core modules (aligned).  
* Evidence layout conforms to governed index/mirror pairs with path proofs; catalogs and acceptance artifacts present (aligned).  
* Partial drift: presenter naming split across `engine/presenter` and top-level `presenter/reader_v1`; adapter includes numerous ops/internal routes beyond core Reader/compat surfaces.

   
