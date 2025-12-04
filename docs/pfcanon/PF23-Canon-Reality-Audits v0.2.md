# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v0.2

**Status:** Canon

**Effective date:** 2025-12-03

**Last Update Gate:** HDE-EPIC019

---

## Intent & scope \[Required-Now\]

These are Codex audits performed at the closure of each epic to bridge the gap between reality and expectation. These will be archived for history.

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

**Date: 2025-12-03**

**Last Epic: HDE-019**

### 1\. Repo map

**Top-level roots observed**

* `engine/` — Present. Core compute modules (sampler, core logic), runtime emitters, CLI, bodygraph resolver/ingest, presenter/serializer, etc.

* `adapter/` — Present. Flask adapter surfaces including Reader, aux narrative, internal ops, and dev sampler endpoints, plus app factory and guards.

* `presenter/` — Present. Reader v1 emitter and JSON canon comparison helpers reused by runtime/public surfaces.

* `docs/` — Present. Acceptance maps and governed evidence index files for artifacts and QA.

* `artifacts/` — Present. Evidence index JSONL and generated artifacts (ingest logs, catalogs, etc.).

* `catalog/` — Present. Catalog JSON describing channels, gates, manifests, and narrative packs used by the engine surfaces.

* `scripts/` — Present. Operational, QA, and release helper scripts (CLI wrappers, sanity gates, ingest helpers).

* Other notable roots:

  * `tests/` (pytest suite)

  * `schemas/` (data schemas)

  * `migrations/` (DB migrations)

  * `audit/` (QA logs)

**Expected layout status**

* `engine/` — Present. Houses deterministic sampler/core plus compat and runtime emitters.

* `adapter/` — Present. Flask HTTP surfaces and guards.

* `presenter/` — Present under `engine/presenter/` and shared `presenter/reader_v1/` emitters.

* CLI package — Present at `engine/cli/` with `hdctl` entrypoint defined in `pyproject.toml`.

* `docs/` — Present with acceptance maps and evidence index.

* `artifacts/` — Present with evidence index JSONL and generated artifacts.

* `scripts/` — Present with QA/dev/release utilities.

* `audit/qa/` — Present within `audit/` containing QA gates (see evidence index entries).

---

### 2\. Engine modules

* **Sampler (`engine/sampler/core.py`):**  
   Defines frozen dataclasses for viewer/candidate/config, builds eligible candidate pools, ranks deterministically via weight/compat/band/ID comparators, and provides a `sample_and_rank` helper.

* **Engine core (`engine/core/core.py`):**  
   Pure-compute functions and dataclasses for participant state, config, perspective breakdown, and `compute_core` that enforces AB/BA ordering, neutral scores, band ordering, and shared trait canonicalization.

* **Duplication check:**  
   No duplicate sampler/core modules observed; each has a single primary implementation.

---

### 3\. Adapter / HTTP surfaces

* **Flask blueprint (`adapter/http_reader.py`):**

  * `/reader`

    * GET/HEAD dev-only Reader harness loading charts from local fixtures and emitting canonical Reader bytes with ETag handling.

  * `/api/aux/narrative` and `/aux/narrative`

    * Emit public aux narratives with ETags when not suppressed.

  * `/internal/dev/sampler` (POST)

    * Dev/admin sampler harness calling sampler core directly with writer-style envelopes on error.

  * Ops/admin endpoints:

    * `/ops/rails/refusal`

    * `/ops/probe/env`

    * `/ops/writer/diagnostic`

    * `/internal/version` for identity metadata.

* **Compatibility writer blueprint (`engine/http/compat_handler.py`):**  
   Exposes `/api/compat/v1` GET/POST/HEAD/OPTIONS producing compat JSON with writer-style envelopes.

---

### 4\. Presenter / emitter

* **Canonical JSON emitter (`engine/presenter/emitter.py`):**  
   Centralizes `emit_compact_json` and `emit_public` for LF-terminated canonical bytes using serializer canon.

* **Serializer (`engine/serializer/canon.py`):**  
   Wraps stable serializer for canonical JSON used by all surfaces.

* **Reader-specific emitter (`presenter/reader_v1/emitter.py`):**  
   Builds preimage, computes idempotence hash, and emits final Reader v1 envelope via canonical emitter; used by runtime public helper.

* **Emitter sharing:**  
   Single emitter stack appears shared across HTTP (Reader/aux) and CLI outputs via `emit_public` / runtime helpers.

---

### 5\. CLI surfaces

* **Entry point:**  
   `hdctl` (`engine/cli/main.py` via `pyproject.toml`) with subcommands:

  * `showcompat`

    * Builds or resolves BodyGraphs (file/db/vendor), computes compat payload, emits compat JSON and Reader bytes, with optional admin dumps.

  * `aux-preview`

    * Previews aux narratives for compat payloads (uses same emitters; not shown but adjacent).

  * `bg:resolve`

    * Returns BodyGraph resolution envelope using resolver logic without real IO under closed rails.

  * `dev:sampler`

    * Dev/admin sampler harness loading candidates from file and emitting ranked list via serializer.

* **Dispatch:**  
   Command dispatch handled by `cli()` parsing args and invoking handlers with error mapping.

---

### 6\. Vendor seam & BodyGraph storage

* **Vendor HTTP client (`engine/bodygraph/vendor_client.py`):**  
   Constructs HTTPS requests with API keys and geo key, pinned retries/timeouts, and typed errors; `build_request` normalizes birth data and fingerprints payloads.

* **Ingest pipeline (`engine/bodygraph/ingest.py`):**  
   Enforces SAFE/ALLOW rails, builds vendor request via client, emits canonical payload, persists to DB (when not dry-run), logs parity, and computes idempotency key; includes DB helper functions and synthetic ID normalization.

* **Resolver (`engine/bodygraph/resolver.py`):**  
   Decides source (auto/db/vendor), enforces rails, gathers inputs (env or args), normalizes IDs, invokes ingest (dry-run for CLI), and wraps result in status envelope.

* **DB access layer:**  
   Accessed via `engine.db` within ingest (not detailed here); adapter HTTP surfaces avoid direct vendor/DB calls.

---

### 7\. Evidence & catalogs

* **Evidence index:**  
   `docs/evidence/INDEX.json` (single-line governed index) with SHA sidecars.

* **Machine mirror:**  
   `artifacts/evidence_index.jsonl` with artifact keys, paths, hashes, roles, and sizes.

* **Catalogs:**  
   Catalog files under `catalog/` include manifest and channel/gate listings for runtime/reference use.

* **Endpoint catalog:**  
   Endpoint catalog file **not found**; no `ENDPOINTS_CATALOG` observed.

---

### 8\. Flows & call chains

* **Reader success (dev harness):**  
   HTTP GET `/reader` (`adapter/http_reader.py:reader_v1`)  
   → loads local charts, enforces version/env  
   → calls `emit_reader_public_bytes` (default from `engine/runtime/public.py`)  
   → computes bands via compat TS  
   → emits Reader v1 envelope through `presenter/reader_v1/emitter.emit_reader_v1` using canonical emitter/serializer  
   → returns HTTP response with ETag.

* **CLI compatibility flow:**  
   `hdctl showcompat` (`engine/cli/main.py`)  
   → loads parties (file/db/vendor)  
   → computes TS features  
   → calls `compat_public` for compat payload  
   → emits public compat bytes via `emitter.emit_public`  
   → emits Reader bytes via `emit_reader_public_envelope`  
   → optionally writes admin dumps for proofs.

* **Vendor ingest flow:**  
   CLI vendor path  
   → builds `VendorInputs`  
   → calls `ingest_vendor_bodygraph` (dry-run unless configured)  
   → constructs vendor request via `HdApiClient`  
   → fetches payload, fingerprints and logs  
   → optionally persists to DB  
   → returns outcome; resolver wraps this in a status envelope for CLI output.

---

### 9\. Reality vs expectations (drift summary)

* **Engine/adapter/presenter split:**  
   *Aligned.* Deterministic engine modules are separated from Flask adapter and shared canonical emitter/serializer stack.

* **Single emitter for surfaces:**  
   *Aligned.* Both HTTP and CLI use `engine.presenter.emitter` and runtime Reader helpers feeding `presenter/reader_v1` emitter.

* **Vendor seam outside engine core:**  
   *Partial.* Vendor client/ingest live under `engine/bodygraph` (inside engine package) but remain separate from sampler/core; they perform network/DB IO guarded by rails.

* **Evidence layout:**  
   *Aligned.* Governed evidence index and artifact mirror present under `docs/evidence` and `artifacts/`.

* **Adapter exposure:**  
   *Aligned.* Reader/aux/internal dev harness exposed via Flask; compatibility writer also exists under `engine/http`.

* **Surprises:**

  * IO-heavy vendor ingest code resides inside `engine/bodygraph` package (not a separate adapter layer).

  * Reader public surface is gated to dev with fixture-based charts rather than external inputs.

