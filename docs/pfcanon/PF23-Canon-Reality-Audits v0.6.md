# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v0.6

**Status:** Canon

**Effective date:** 2025-12-11

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

**Date: 2025-12-11**

**Last Epic: HDE-021**

**Repo map**

* **`engine/`** — Present. Core computation (compatibility logic, sampler/core, runtime helpers), presenter/emitter, serializer, CLI, HTTP helpers, DB access, narratives, and validation utilities are under this package.

* **`adapter/`** — Present. Flask application wiring, reader/aux/sampler/internal routes, compat blueprint registration, environment guards, and logging filters live here.

* **`presenter/`** — Present at repository root for legacy utilities (e.g., `reader_v1` emitter), with the canonical emitter living in `engine/presenter`.

* **`cli/`** — Present as `engine/cli` package; contains `hdctl` CLI entrypoints and subcommands.

* **`docs/`** — Present with PF-canon references, acceptance maps, and evidence indexes (e.g., `docs/evidence/INDEX.json`).

* **`artifacts/`** — Present. Houses governed artifacts, evidence index JSONL, QA proofs, and bundle assets.

* **`scripts/`** — Present for helper scripts (not inspected in depth).

* **`audit/qa/`** — `audit/` directory present (QA subfolders exist but not reviewed here).

**Expected directories (observed):**

* `engine/` (Present)

* `adapter/` (Present)

* `presenter/` (Present at root and under `engine/`)

* CLI package (Present under `engine/cli`)

* `docs/` (Present)

* `artifacts/` (Present)

* `scripts/` (Present)

* `audit/qa/` (Present under `audit/`)

---

## **Engine modules**

* **Sampler**  
   `engine/sampler/core.py` defines dataclasses for viewer/candidate inputs, configuration, pool building, deterministic ranking, and a `sample_and_rank` helper combining pool formation and ranking.

* **Core**  
   `engine/core/core.py` offers pure-compute compatibility metrics with `ParticipantState` / `CoreConfig`, parity-preserving ordering, shared trait extraction, and `compute_core` for deterministic results.

---

## **Adapter / HTTP surfaces**

* **App factory & health endpoints**  
   `adapter/wsgi.py` creates the Flask app, installs logging/env guards, registers reader and compat blueprints, and exposes `/internal/healthz` and `/internal/readyz` along with `404/405` handlers applying common headers.

* **Reader blueprint**  
   `adapter/http_reader.py`’s `get_reader_bp` builds a blueprint exposing `GET/HEAD /reader` (dev-gated file-based harness) that loads charts, calls `emit_reader_public_bytes`, and handles ETag/HEAD semantics.

* **Aux \+ ops \+ sampler routes**  
   The same blueprint includes:

  * `/api/aux/narrative` (text aux output), and

  * ops probes (`/ops/rails/refusal`, `/ops/probe/env`) plus `/internal/dev/sampler` (dev-only sampler harness using `sampler.core`).

* **Compat blueprint**  
   `engine/http/compat_handler.py` defines `compat_blueprint` at `/api/compat/v1` with `GET/POST` routes producing `compat_public` outputs and writer-style transport responses (HEAD/OPTIONS handling).

---

## **Presenter / emitter**

* **Canonical emitter**  
   `engine/presenter/emitter.py` emits canonical JSON bytes using `serializer.canon` with optional envelope helpers; used across HTTP and CLI surfaces.

* **Reader emitter**  
   `presenter/reader_v1/emitter.py` builds Reader v1 envelopes, enforces category uniqueness, adds `idempotence_hash`, and returns canonical bytes; `engine/runtime/public` delegates here.

* **Shared emitter usage**  
   HTTP adapters and CLI both call the shared emitter stack via `engine/runtime/public` or directly through `engine/presenter/emitter` for compat outputs.

---

## **CLI surfaces**

* **Entry point**  
   `hdctl` (`engine/cli/main.py`) defines subcommands:

  * `showcompat` (computes `compat_public` and Reader envelopes, optional dumps)

  * `aux-preview` (narrative preview)

  * `bg:resolve` (BodyGraph resolution)

  * `dev:sampler` (deterministic sampler harness)

* **Command chain**

  * `showcompat` loads inputs (files/DB/vendor), normalizes parties, computes `compat_public`, emits Reader bytes via `emit_reader_public_envelope`, writes admin dumps if requested, and outputs compat bytes to stdout.

  * `dev:sampler` reuses `sampler.core` via `CandidateFeatures` / `ViewerProfile` normalization for CLI parity with the internal sampler route.

---

## **Vendor seam & BodyGraph storage**

* **Vendor HTTP client**  
   `engine/bodygraph/vendor_client.py` implements `HdApiClient` with HTTPS validation, request construction from birth tuple, retries/timeouts, and typed `VendorError` mapping for external vendor calls.

* **BodyGraph source selection**  
   `engine/cli/main.py`’s `showcompat` sources BodyGraphs from DB (`resolve_db_user_id` / `DBAccess`) or vendor via `ingest_vendor_bodygraph` depending on CLI flags, keeping vendor logic outside engine core.

---

## **Evidence & catalogs**

* `docs/evidence/INDEX.json`, `INDEX.sha256`, and path proofs present; they mirror governed evidence entries.

* `artifacts/evidence_index.jsonl` with path proof exists, listing epic artifacts and bundles (e.g., EPIC020 CLI and identity bundles).

* No `docs/ENDPOINTS_CATALOG.json` observed (`grep` returned none).

---

## **Flows & call chains**

* **Reader success (dev harness)**  
   HTTP `GET /reader` (`adapter/http_reader.py:reader_v1`)  
   → `engine/runtime/public.emit_reader_public_bytes` computes band via `ts_v0` and builds enriched envelope  
   → `presenter/reader_v1/emitter.emit_reader_v1` adds `idempotence_hash` using `engine/presenter/emitter` for canonical bytes  
   → Flask response with ETag.

* **CLI compatibility flow**  
   `hdctl showcompat`  
   → loads parties (files/DB/vendor)  
   → `compat_public` computation  
   → `emit_reader_public_envelope` for Reader bytes  
   → `emitter.emit_public` writes compat payload to stdout; optional dumps via helper functions.

* **Internal sampler dev flow**  
   `POST /internal/dev/sampler` (`adapter/http_reader.py`)  
   → payload validation/gating  
   → constructs `ViewerProfile` / `CandidateFeatures`  
   → calls `sampler.core.sample_and_rank` for deterministic ordering  
   → emits JSON via `emit_public`.

* **Vendor acquisition (CLI path)**  
   `showcompat` with vendor source builds `VendorInputs` and calls `ingest_vendor_bodygraph` (uses `vendor_client`), then maps outcomes into person/chart normalization before compat/Reader emission; DB alternative uses `resolve_db_user_id` and `DBAccess` to fetch stored BodyGraphs.

---

## **Reality vs Expectations (drift summary)**

* **Engine/adapter/presenter split** — Aligned; deterministic sampler/core modules are pure compute, adapters host HTTP, and emitters centralize serialization.

* **Single canonical emitter** — Aligned; `engine/presenter/emitter` underpins `reader_v1` emitter, HTTP responses, and CLI outputs.

* **Vendor seam outside engine core** — Aligned; `vendor_client` and `ingest` are separate from sampler/core, invoked by CLI paths before compat/Reader computation.

* **Evidence layout** — Present but complex; evidence index lives under `docs/evidence` and `artifacts/evidence_index.jsonl` with path proofs; endpoint catalog not found (partial alignment).

* **HTTP surfaces** — Adapter includes Reader, compat, aux, ops, and sampler dev endpoints; Reader is dev-gated and uses runtime emitter; compat blueprint uses writer transport style (aligned with adapter expectation).

* **Engine purity** — Core and sampler avoid I/O/time randomness (aligned); adapter handles I/O/DB/vendor guards. No notable red flags observed in reviewed files.

