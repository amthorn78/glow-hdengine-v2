# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v0.8

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

#### Top-level contents

Top-level contents (via ls): engine source plus adapter, presenter, artifacts, docs, audit, scripts, config, tests, etc. (repo root ls).

#### Core directories (expected and observed)

* **engine/** — Present. Core packages for compat, sampler, core math, presenter/emitter, runtime, DB, bodygraph vendor logic, CLI, and validation utilities (engine/ tree from ls engine).  
* **adapter/** — Present. Flask-based HTTP adapter, blueprints, env/no-IO guards, ETag helpers, and WSGI/app factories (adapter/).  
* **presenter/** — Present but under top-level `presenter/reader_v1/`, providing Reader emitter used by runtime (`presenter/reader_v1/emitter.py`).  
* **cli** — Present as `engine/cli/`, Typer/argparse CLI exposed via `hdctl` script in pyproject (`engine/cli/main.py`; `pyproject.toml`).  
* **docs/** — Present. Evidence/index docs, run catalogs, adapter/db references, acceptance maps (`docs/`, `docs/evidence/INDEX.json`, `docs/run/PROD_ENDPOINTS.json`).  
* **artifacts/** — Present. Evidence index mirror, proofs, compat captures, sampler/core logs, release artifacts (`artifacts/evidence_index.jsonl`, numerous artifacts referenced in INDEX).  
* **scripts/** — Present. Dev/QA helpers (not deeply inspected).  
* **audit/qa/** — Present under `audit/qa/`, includes QA logs/matrices for epics and compat (`audit/qa/hde-epic019/**`, `audit/qa/hde-epic022/**`, `audit/qa/hde-epic023/**`).

#### Other notable directories

* `catalog/` (release manifest)  
* `config/`  
* `ci/` (checks)  
* `tests/` (transport/contracts)  
* `fixtures/` (sample charts)

---

### Engine modules

#### Sampler core

`engine/sampler/core.py` defines dataclasses `ViewerProfile`, `CandidateFeatures`, `SamplerConfig`, `CandidatePool`, `RankedCandidates`; functions `build_candidate_pool` (eligibility/zero-weight filtering), `rank_candidates` (deterministic ordering by weight, compat score, band priority, ID tie-break), and `sample_and_rank` (helper) (`engine/sampler/core.py`).

#### Engine Core

`engine/core/core.py` defines `ParticipantState`, `CoreConfig`, `PerspectiveBreakdown`, `CoreResult` and `compute_core` (neutral score, AB/BA ordering via `compare_ids`, band ordering, shared trait canonicalization) with helpers `_ordered_pair`, `_ordered_bands`, `_neutral_score`, `_shared_traits` (`engine/core/core.py`).

#### Duplication check

No duplicate sampler/core modules observed.

---

### Adapter / HTTP surfaces

#### Reader/ops blueprint (adapter/http\_reader.py)

Primary Flask blueprint bp from `adapter/http_reader.py:get_reader_bp` registered in `create_app`; routes:

* GET /reader (dev harness): validates v=1 and APP\_ENV dev, loads charts from fixtures, enforces TZ, calls emit\_reader\_public\_bytes, sets ETag/304/HEAD handling (adapter/http\_reader.py lines \~300–380).  
* GET /aux/narrative and /api/aux/narrative: emits Aux narratives via engine.narratives.emit\_public\_aux with headers/provenance, suppression handling (adapter/http\_reader.py lines \~382–430).  
* POST /reader: method-not-allowed error envelope (adapter/http\_reader.py lines \~432–439).  
* Ops/rails probes: /ops/db/unavailable forced DB failure snapshot, /ops/rails/refusal returns rails\_closed envelope, /ops/probe/env exposes process/env snapshot (adapter/http\_reader.py lines \~441–536).  
* Dev-only sampler harness: POST /internal/dev/sampler uses Sampler core; gated by APP\_ENV dev/test/local; returns sorted candidate IDs via emit\_public (adapter/http\_reader.py lines \~538–618).  
* /internal/version GET/HEAD returns identity JSON without ETag; builds payload from artifacts/identity and catalog manifest (adapter/http\_reader.py lines \~610–724).  
* Writer diagnostic transport: POST/HEAD/OPTIONS /ops/writer/diagnostic handles admin auth, idempotence hash caching, strict transport rules (adapter/http\_reader.py lines \~726–820).

#### Compat HTTP API (engine/http/compat\_handler.py)

Blueprint compat\_blueprint at /api/compat/v1 in `engine/http/compat_handler.py`; GET for ids-only compat, POST for payload compat; guards HEAD/OPTIONS; uses compat\_public and emit\_public for responses (`engine/http/compat_handler.py`).

#### Application factory

`adapter/http_reader.py:create_app` mounts reader blueprint at root and compat blueprint, with 404/405 scoped handlers removing ETags on internal routes (adapter/http\_reader.py lines \~782–840).

---

#### Presenter / emitter

#### Canonical emitter

`engine/presenter/emitter.py` exposes `emit_public` (canonical JSON via serializer with optional sort\_keys), `emit_public_with_envelope`, and alias `emit_compact_json`; used across HTTP, CLI, runtime (`engine/presenter/emitter.py`).

#### Serializer

`engine/serializer/canon.py` delegates to stable sercanon for canonical JSON (UTF-8, sorted, compact, LF) (`engine/serializer/canon.py`).

#### Reader-specific emitter

`presenter/reader_v1/emitter.py` builds Reader v1 preimage, computes idempotence\_hash, emits canonical bytes via `emitter.emit_public`; dedupes/sorts categories (`presenter/reader_v1/emitter.py`).

#### Shared usage

HTTP reader route uses runtime emit\_reader\_public\_bytes → presenter.reader\_v1.emitter → engine.presenter.emitter (adapter/http\_reader.py; engine/runtime/public.py). CLI showcompat emits via engine.presenter.emitter.

---

### CLI surfaces

#### Entry point

Entry point hdctl defined in `pyproject.toml` pointing to `engine.cli.main:cli` (`pyproject.toml`).

#### Commands (engine/cli/main.py, argparse)

* showcompat: loads BodyGraphs from files/stdin/db/vendor/auto, computes compat\_public, emits Reader envelope via runtime emit\_reader\_public\_envelope, writes optional dumps, outputs compat JSON via emitter.emit\_public (engine/cli/main.py lines \~609–730).  
* aux-preview: renders Aux narrative text via emit\_public\_aux, optional sidecar dumps (engine/cli/main.py lines \~470–560).  
* bg:resolve: resolves BodyGraphs via resolver (DB/vendor/auto), optional dry-run planning (engine/cli/main.py lines \~140–240).  
* dev:sampler: dev/admin sampler harness mirroring HTTP; loads candidates JSON, calls sampler.sample\_and\_rank, outputs canonical JSON via sercanon (engine/cli/main.py lines \~760–830).

Admin dump helper `_admin_dump.canon_dump` for writing sha sidecars; used by showcompat/aux-preview (`engine/cli/_admin_dump.py`).

Module `engine/cli/__main__.py` simply runs cli (not shown but typically).

---

### Vendor seam & BodyGraph storage

#### Vendor client

`engine/bodygraph/vendor_client.py` implements HdApiClient with HTTPS-only base URL, env config via HDAPI\_BASE\_URL/HD\_API\_KEY/GEO\_API\_KEY, request building from birth tuple, retries/timeouts, fetch via urllib with exponential backoff; raises VendorError with codes; optional retry log (`engine/bodygraph/vendor_client.py`).

#### Ingest flow

`engine/bodygraph/ingest.py` uses HdApiClient.from\_env respecting SAFE\_MODE/ALLOW\_NETWORK, builds request, computes idempotency key, optionally dry-run; persists payload via DBAccess, writes success/retry logs and canon compare logs; uses emitter.emit\_public\_with\_envelope for canonical serialization; resolve\_db\_user\_id handles synthetic IDs (`engine/bodygraph/ingest.py`).

#### DB access

`engine/db/adapter.py` provides DBAccess with provider selection between psycopg and bridge, env/force flags, snapshots; methods health/query/exec/tx/introspect; uses provider classes (bridge, psycopg) and AdapterError hierarchy (`engine/db/adapter.py`).

BodyGraph resolver/retention modules (not deeply traced) under `engine/bodygraph/` support storage/access pattern.

---

### Evidence & catalogs

#### Evidence index and mirror

* `docs/evidence/INDEX.json` (human index listing artifacts/tokens/paths)  
* `artifacts/evidence_index.jsonl` (machine mirror JSONL)  
* `docs/evidence/INDEX.sha256` sidecar (not viewed directly) present

(`docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`).

#### Core evidence artifacts

`artifacts/core/abba/ab_ba_parity.json`, `artifacts/core/purity/purity_report.json`, `artifacts/core/two_run/identity.json`, with schemas under `docs/schemas/core/*.schema.json` (docs/evidence/INDEX.json entries).

#### Sampler evidence

Artifacts under `artifacts/sampler/` (pool snapshots, abba parity, diversity requirements, two\_run, seed\_replay) with schemas under `docs/schemas/sampler/` (docs/evidence/INDEX.json).

#### Endpoint catalog (run catalog)

`docs/run/PROD_ENDPOINTS.json` with `.path_proof` sidecar capturing production endpoints metadata (`docs/run/PROD_ENDPOINTS.json`).

#### Other governed artifacts

Catalogs under `catalog/` (manifest), artifacts/identity/..., audit acceptance maps and QA matrices per epics (entries in `docs/evidence/INDEX.json`).

---

### Flows & call chains

#### Reader success (dev harness)

HTTP GET /reader → adapter/http\_reader.py:reader\_v1 validates version/env, loads fixture charts, calls emit\_reader\_public\_bytes → engine/runtime/public.emit\_reader\_public\_envelope computes band via compat ts\_v0 and builds enriched envelope → presenter/reader\_v1/emitter.emit\_reader\_v1 adds idempotence\_hash → engine/presenter/emitter.emit\_public produces canonical bytes returned with ETag handling (adapter/http\_reader.py; engine/runtime/public.py; presenter/reader\_v1/emitter.py; engine/presenter/emitter.py).

#### CLI compatibility/preview

hdctl showcompat (engine/cli/main.py) loads BodyGraphs (files/db/vendor), normalizes pair via compat ordering, computes compat\_public, calls emit\_reader\_public\_envelope for Reader bytes, writes optional dumps, emits compat JSON via engine.presenter.emitter.emit\_public to stdout (engine/cli/main.py lines \~609–735).

#### Vendor ingest / BodyGraph acquisition

CLI or ingest call resolves inputs → engine/bodygraph/ingest.ingest\_vendor\_bodygraph enforces SAFE\_MODE/ALLOW\_NETWORK, builds HdApiClient request, HdApiClient.fetch performs HTTPS request with retry/backoff (engine/bodygraph/vendor\_client.py), response serialized via emitter, idempotency key computed; if not dry-run, uses engine.db.DBAccess.for\_current\_env to persist payload and compare canonical shas, logging to artifacts (engine/bodygraph/ingest.py; engine/db/adapter.py).

#### HTTP dev sampler

POST /internal/dev/sampler → adapter/http\_reader.py:dev\_sampler\_internal gates APP\_ENV, validates payload, constructs ViewerProfile/CandidateFeatures, calls sampler.sample\_and\_rank, emits canonical JSON via emitter.emit\_public to HTTP response (adapter/http\_reader.py; engine/sampler/core.py; engine/presenter/emitter.py).

#### Compat HTTP API

GET/POST /api/compat/v1 → engine/http/compat\_handler.py resolves ids/payloads, validates viewer prefs, calls compat\_public (not detailed) and returns via emit\_public with writer-style transport headers (engine/http/compat\_handler.py).

---

### Reality vs Expectations (drift summary)

* Engine/adapter/presenter split: Aligned — distinct engine (pure compute modules), adapter (Flask HTTP), presenter (emitter plus Reader-specific presenter) are present and referenced consistently (engine/\*, adapter/http\_reader.py, presenter/reader\_v1/emitter.py).  
* Sampler/core purity: Aligned — sampler/core modules are pure compute with deterministic ordering, no I/O or network; used by CLI and internal HTTP harness (engine/sampler/core.py, engine/core/core.py).  
* Adapter surfaces: Partial — adapter centers in adapter/http\_reader.py rather than a standalone adapter/ dir split; includes multiple ops/aux/dev routes plus compat blueprint housed in engine/http; still matches expected HTTP layer but route mix extends beyond pure adapter (adapter/http\_reader.py, engine/http/compat\_handler.py).  
* Presenter/emitter reuse: Aligned — single canonical emitter in engine/presenter/emitter.py used by runtime, HTTP, CLI; Reader-specific emitter layered on top (engine/runtime/public.py, presenter/reader\_v1/emitter.py, engine/cli/main.py).  
* Vendor seam outside engine core: Partial — vendor client/ingest live under engine/bodygraph and perform network I/O guarded by SAFE\_MODE/ALLOW\_NETWORK; core compat/sampler modules remain pure compute, so seam is separated though still under engine namespace (engine/bodygraph/vendor\_client.py, engine/bodygraph/ingest.py).  
* Evidence layout: Aligned — evidence index/mirror present, governed artifacts under artifacts/core, sampler, presenter, ops, QA; acceptance maps and catalog manifest exist (docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, catalog/manifest.json).  
* CLI presence: Aligned — hdctl exposes compat, aux, bodygraph resolve, dev sampler commands using shared engine/presenter modules (pyproject.toml, engine/cli/main.py).  
* HTTP adapter expectations: Partial — reader dev harness gated to APP\_ENV dev and fixture files (not general public API); compat API exists with writer-style transport; internal/ops routes mix rails probes and writer diagnostic in same blueprint (adapter/http\_reader.py, engine/http/compat\_handler.py).  
* Multiple emitters: Drift minimal — canonical emitter shared; Reader-specific emitter separate but layered, not conflicting (engine/presenter/emitter.py, presenter/reader\_v1/emitter.py).

