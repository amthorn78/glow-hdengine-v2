# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.3

**Status:** Canon

**Effective date:** 2026-02-06

**Last Update Gate:** HDE-EPIC025 v2

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

# A) HD Engine Audit Template

Template Version: 2026.02.05

## **1.1 — Audit Prompt**

You are Codex, auditing the Glow HD Engine repository.

Your job is **what, not how**:

* What exists now in this repo: directories, key files, and flows.

* Where it aligns or drifts from the expected HD Engine architecture (engine / adapter / presenter / CLI / vendor / DB / evidence).

Constraints:

* **Read-only analysis only.**

* **No changes, no refactors, no suggestions.**

* **Do not propose new files, flows, or designs.**

* **Do not infer intent.** Describe what you can point to in the repo.

Proof posture (required):

* Any concrete statement must be grounded in **a file path** plus **a brief cited excerpt** (line snippet), or in a **repo listing output** that shows the path exists.

* Any “not found” claim must include a **negative-claim proof** (search method \+ scope \+ 0 hits).

---

## **1.2 — Audit Snapshot Metadata (new; required)**

Record a minimal “snapshot header” so the audit can be tied to a point-in-time repo state.

Capture and report:

* Repo root: confirm you are at repo root (one line).

* Commit: `git rev-parse HEAD`

* Working tree cleanliness: `git status --porcelain` (if non-empty, report “dirty” and list the changed paths only).

* Branch (if available): `git rev-parse --abbrev-ref HEAD`

* Timestamp (UTC).

* Execution environment (brief, facts only):

  * OS/kernel (if visible)

  * Python version (if Python exists)

  * Node version (if Node exists)

No opinions here—just facts.

---

## **1.3 — Scope and Posture (expanded)**

Assume:

* Current working directory is the HD Engine repo root.

* Repo is read-only.

* Output is a descriptive architecture audit, not an implementation plan.

In-scope emphasis (clarified):

* HD Engine layer and direct callers:

  * Reader surface

  * Aux/narrative surfaces if they call engine

  * CLI(s)

  * Vendor seam

  * DB/cache for BodyGraph storage

  * Evidence/canon artifacts and indices

  * QA/test harnesses that validate determinism/contract

Out-of-scope (clarified):

* Unrelated FE/app code **unless** it directly calls into engine surfaces in a way that clarifies real flow wiring.

* Internal tooling unrelated to determinism/evidence unless it is invoked by CI/QA paths.

---

## **2 — Top-level Repo Map (expanded)**

Produce a top-level directory \+ important file map.

For each top-level directory and key file:

* Name (exact case)

* Present / Not found

* 1–2 sentences describing what actually lives there (based on files inside)

* 1–3 anchor paths inside (representative examples)

For expected HD Engine directories, explicitly classify:

* Present (summarize contents)

* Present but renamed (give actual name \+ proof)

* Not found (include negative-claim proof)

Minimum expected families to check (same as your list, plus a few audit-critical ones):

* engine/

* adapter/

* presenter/

* CLI package location(s)

* docs/

* artifacts/

* audit/

* tools/

* ci/ (or .github/ workflows)

* tests/

* scripts/

Root discipline capture (new):

* List every top-level root that looks like a “truth home” for governed outputs:

  * audit/**, artifacts/**, docs/**, tools/**, scripts/\*\*, etc.

* Do **not** judge; just list them. This gives later reviewers the raw material to assess “too many roots.”

---

## **3 — Packaging, Entrypoints, and Runtime Wiring (new; required)**

This section prevents the audit from being “file archaeology only” by forcing reality about how code is actually invoked.

### **3.1 Packaging / build configuration**

Identify and summarize:

* Python packaging file(s): `pyproject.toml`, `setup.cfg`, `setup.py`, requirements files.

* Any workspace/monorepo manager config if present.

For each packaging file found:

* Path

* What it declares (short): package names, entrypoints, scripts, dependencies sections.

### **3.2 Entrypoint inventory**

Identify entrypoints for:

* HTTP server startup (where routes get mounted)

* CLI console scripts (commands and subcommands)

* Any scheduled/background jobs relevant to evidence/indexing

For each entrypoint:

* File path

* Symbol name (function/class/module)

* One-sentence role statement based on code.

---

## **4 — Engine Modules (sampler/core) (expanded)**

Within whatever serves as the “engine package”:

### **4.1 Sampler**

Identify modules implementing sampler behavior (pool formation / eligibility / ordering / random selection).

For each:

* File path

* Primary classes/functions (list)

* One-sentence role per class/function

### **4.2 Core compute**

Identify modules implementing core compatibility behavior:

* Compatibility metrics and result structure

* AB↔BA parity / symmetry handling

* Normalization / canonicalization at the engine boundary (if any)

For each:

* File path

* Primary functions/classes \+ one-sentence roles

### **4.3 Determinism hazards inventory (new)**

Without proposing fixes, inventory obvious determinism hazards inside engine modules:

* Use of current time

* Randomness without explicit seeding

* Network calls

* File I/O

* Non-deterministic iteration ordering (unordered maps without sorting) where relevant

For each hazard you claim exists:

* File path \+ snippet anchor

If none observed:

* Say “No determinism hazards observed in the sampled paths” and list what you actually reviewed.

---

## **5 — Adapter / HTTP Surfaces (expanded)**

Locate the HTTP layer and describe **how routes are registered** and **what they call**.

### **5.1 Route registration map (new)**

Identify:

* The module(s) where the HTTP app/router is created

* Where routes/blueprints are mounted

* Any path prefixes applied during mounting

For each mounted route group:

* Base path/prefix (exact string)

* File path(s) where defined

* Handler symbols

### **5.2 Surface classification**

Classify each surface found:

* Reader-like JSON success

* Aux/narrative

* Admin/internal

* Dev/diagnostic harness

For each group:

* File path \+ handler names

* One-sentence role

### **5.3 Transport semantics hooks (new; factual)**

If the code implements or enforces any of the following, record where:

* HEAD vs GET parity handling

* Conditional responses / 304

* ETag generation and quoting behavior

* Cache-control rules

* Content-Type setting rules

Each claim must be anchored to a code location.

---

## **6 — Presenter / Canonical Emitter (expanded)**

Identify the module(s) that convert internal results to:

* JSON response bodies

* CLI output payload(s)

* Canonical JSON formatting rules (ordering, whitespace, encoding)

For each emitter:

* File path

* Primary functions/classes

* What surfaces call it (HTTP/CLI/etc.), based on imports/calls

If multiple emitters exist:

* List them and distinguish by usage and output semantics (do not recommend consolidation—just describe).

---

## **7 — CLI Surfaces (expanded)**

Find CLI entrypoints:

* console scripts (pyproject etc.)

* modules with `if __name__ == "__main__":`

* click/typer/argparse usage

For each CLI command relevant to compat/showcompat/reader-equivalent behaviors:

* Command name \+ subcommand structure

* File path

* Entrypoint symbol

* Arguments required (as evidenced by parser definitions)

* High-level call chain (CLI → adapter/engine → presenter/emitter)

Also capture **output surfaces**:

* Does the CLI write files? Where?

* Does it print to stdout?

* Does it exit nonzero on missing args?

Every statement must be anchored.

---

## **8 — Vendor Seam and BodyGraph Storage (expanded)**

### **8.1 Vendor client**

Identify where the repo calls the external vendor:

* HTTP client usage modules

* Request shaping functions/classes

* Response parsing

For each:

* File path

* Symbol names

* What input it needs (env var names only, config keys, etc.—no values)

### **8.2 BodyGraph persistence/caching**

Identify:

* DB layer modules (ORM, SQL, file cache, in-memory cache, etc.)

* How cache keys are formed (if visible)

* Decision logic: when it reads cached vs calls vendor

### **8.3 Offline posture / “vendor required” posture (new)**

If the repo has any explicit “offline mode” or “network disabled” gates:

* Identify where it is enforced

* What happens when network is disabled

If there is no such posture found:

* Report “No explicit offline/vendor gating posture found in the audited paths” and list what you checked.

---

## **9 — Evidence, Indices, Catalogs, and Governed Artifacts (expanded)**

This section should be **exhaustive** because evidence posture tends to be where drift hides.

### **9.1 Evidence homes inventory (new; required)**

Inventory all directories that appear to hold governed artifacts or evidence:

* docs/\*\*

* artifacts/\*\*

* audit/\*\* (including audit/qa/\*\* if present)

* any other evidence-like homes discovered

For each home:

* Path

* What kinds of files are inside (schemas, logs, indices, proofs)

* Whether it appears generated, hand-authored, or mixed (based on file patterns and comments)

### **9.2 Evidence index structures**

Look specifically for:

* docs/evidence/INDEX.json

* docs/evidence/INDEX.sha256

* artifacts/evidence\_index.jsonl (or equivalents)

* any tooling that regenerates/validates them

For each:

* Path

* Brief description (what it contains; do not paste full content)

* Tooling that reads/writes it (paths \+ symbols)

### **9.3 Endpoint catalog**

Search for endpoint catalog file(s) (e.g., docs/ENDPOINTS\_CATALOG.json or equivalents).

For each catalog:

* Path

* Schema/shape summary (routes listed, any metadata)

* Whether it is referenced by code/tooling/tests

### **9.4 Proof artifacts / snapshot artifacts**

Inventory “proof snapshot” artifacts (success\_get, success\_head, etc.) if present:

* Paths

* What produces them (test/tool/script, anchored)

Do not invent meanings—stick to filename and producer evidence.

---

## **10 — Tests, QA Harness, and CI/Checks (new; required)**

This is a major missing piece in your template: audits often name modules but fail to show **how reality is verified**.

### **10.1 Tests map**

Inventory test roots and categorize:

* Unit vs integration vs contract tests (only if the repo labels them; otherwise “uncategorized”)

* Identify tests that exercise:

  * compat/reader endpoints

  * CLI outputs

  * canonical JSON / canonical bytes

  * determinism gates

  * evidence index / catalogs

For each key test locus you name:

* Path \+ brief role

* What it asserts at a high level (one sentence)

* Any fixtures that imply vendor/network reliance

### **10.2 CI workflows**

Locate CI configuration:

* GitHub workflows or other CI config

* Identify jobs/checks that run the above tests or enforce evidence discipline

For each workflow/job you mention:

* File path

* Job/check name (as written)

* What it runs (commands or scripts referenced)

### **10.3 Script/check inventory (read-only)**

Inventory QA-relevant scripts under:

* ci/checks/\*\*

* tools/\*\*

* scripts/\*\*

* any “check\_*.sh” or “run\_*.py” patterns

For each:

* Path

* One-sentence role (based on comments/behavior)

---

## **11 — Flows and Call Chains (expanded)**

Reconstruct at least **five** representative flows (not three), because drift often appears only when you compare flows.

Required flows (if they exist; otherwise explain “closest equivalent found”):

1. Reader success flow (HTTP)

2. Compat API flow (HTTP)

3. CLI showcompat / compat preview flow

4. Vendor acquisition flow (BodyGraph ingest)

5. Evidence index update/validation flow

For each flow:

* Start point: file path \+ handler/entrypoint symbol

* Middle: adapter layer function(s)

* Engine: sampler/core calls

* Presenter/emitter

* Output: response or file writes (paths if any)

Keep each flow as:

* A short call chain line list: `file.py:func → file2.py:func → ...`

* Then 3–8 bullet notes with factual observations.

---

## **12 — Drift and Reality vs Expectations (expanded)**

Keep the neutral posture (“no suggestions”), but make drift reporting more structured so it’s actionable later without re-auditing.

### **12.1 Drift categories (new)**

Report drift findings under these headings:

* Directory/architecture drift (expected split vs actual)

* Surface drift (routes/entrypoints differ from expected)

* Evidence drift (multiple homes; unclear governance)

* Determinism drift (hazards or unclear gating)

* Vendor seam drift (vendor call location differs from expectation)

* Path-case drift (mixed-case paths, especially under audit/qa/ if present)

* Root proliferation (too many competing “homes” observed—report as fact: “N roots identified”, list them)

Each drift item must include:

* What you observed (one sentence)

* Proof anchor (path \+ excerpt)

* Impact (neutral, factual wording like “This creates ambiguity about …”)

### **12.2 Alignment summary table (optional but allowed)**

For each expectation area (engine/adapter/presenter split, single emitter, vendor seam outside engine, evidence layout):

* Aligned / Partial / Drift

* One anchor per classification

No recommended fixes.

---

## **13 — Negative-Claim Proof Appendix (new; required)**

Whenever you say “Not found” for:

* a directory

* a file

* a route string

* an entrypoint symbol

you must include a negative-claim proof block:

* What was searched (exact token)

* Search method (rg/find/tree)

* Scope (“repo root” or specific subtrees)

* Result (“0 hits”)

This appendix can be either:

* Per-section inline (preferred for readability), or

* Collected at the end (acceptable), as long as each “not found” claim is backed.

---

## **Output Format (updated)**

Structure output with these sections in order:

1. Audit Snapshot Metadata

2. Top-level Repo Map

3. Packaging and Entrypoints

4. Engine Modules

5. Adapter / HTTP Surfaces

6. Presenter / Emitter

7. CLI Surfaces

8. Vendor Seam & BodyGraph Storage

9. Evidence, Indices, Catalogs

10. Tests, QA Harness, CI/Checks

11. Flows & Call Chains

12. Drift and Reality vs Expectations

13. Negative-Claim Proof Appendix

Within each section:

* Prefer bullet lists \+ short paragraphs.

* Cite file paths and symbols.

* Avoid speculation.

# B) \- HD Engine Current Audit 

**Date:** 2026-02-06

**Last Epic:** HDE-EPIC025

Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2 (command: pwd → /workspace/glow-hdengine-v2).  
* Commit: 2c5d67a1fb114c2f6a4499b6182e380931f78fc0 (command: git rev-parse HEAD).  
* Working tree cleanliness: clean (command: git status \--porcelain → empty output).  
* Branch: work (command: git rev-parse \--abbrev-ref HEAD).  
* Timestamp (UTC): 2026-02-05T22:42:50Z (command: date \-u \+'%Y-%m-%dT%H:%M:%SZ').  
* Execution environment:  
  * OS/kernel: Linux 5ea4f3be4c0e 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 GNU/Linux (command: uname \-a).  
  * Python: Python 3.10.19 (command: python \--version).  
  * Node: v22.21.1 (command: node \--version).

Top-level Repo Map

* Top-level directories (present):  
  * .audit\_src/ — Snapshot copy of repo documents and artifacts; contains a README detailing repo overview and validation posture in that snapshot. Anchor: .audit\_src/README.md.  
  * .backup\_epic004/ — Backup set with timestamped README and change bundles for EPIC004. Anchor: .backup\_epic004/README.md.20251024121852.  
  * .devcontainer/ — Dev container configuration with environment pins and post-create command. Anchor: .devcontainer/devcontainer.json.  
  * .github/ — CI workflow definitions (e.g., GitHub Actions pipeline). Anchor: .github/workflows/ci.yml.  
  * .git/ — Git metadata (HEAD ref). Anchor: .git/HEAD.  
  * .venv/ — Local Python virtual environment files (activation script). Anchor: .venv/bin/activate.  
  * .vscode/ — Editor settings for the repo. Anchor: .vscode/settings.json.  
  * \_arch/ — Timestamped architecture snapshot bundles with a README explaining contents. Anchor: \_arch/README.md.  
  * \_archive/ — Archived EPIC003 trees (older server/core/adapters). Anchor: \_archive/EPIC003\_CLEAN\_20251017\_211719/server/app.py.  
  * adapter/ — Flask adapter and HTTP reader/app wiring. Anchor: adapter/http\_reader.py.  
  * artifacts/ — Governed artifacts/evidence including machine mirror JSONL. Anchor: artifacts/evidence\_index.jsonl.  
  * audit/ — QA/close-pack manifests and logs (example EPIC024 manifest). Anchor: audit/EPIC-024\_MANIFEST.json.  
  * catalog/ — Release manifest and catalog metadata (manifest listing files/hashes). Anchor: catalog/manifest.json.  
  * ci/ — CI checks scripts. Anchor: ci/checks/check\_env\_pins.sh.  
  * codex/ — Codex-related prompts and outputs. Anchor: codex/AGENTS\_RFI.md.  
  * config/ — Config JSON files (e.g., band config). Anchor: config/bands\_4B60\_v1.json.  
  * dev/ — Dev harness (reader harness app). Anchor: dev/reader\_harness/app.py.  
  * docs/ — Docs and acceptance maps (endpoint catalog and acceptance maps). Anchor: docs/ENDPOINTS\_CATALOG.json.  
  * engine/ — Engine core, compat compute, sampler, runtime, DB, etc. Anchor: engine/compat/compute.py.  
  * errors/ — Error token map and schema check artifacts. Anchor: errors/token\_map/token\_map.json.  
  * fixtures/ — Fixture inputs (example chart). Anchor: fixtures/charts/alice.json.  
  * freeze/ — Freeze pack metadata. Anchor: freeze/freeze\_pack\_v1.json.  
  * glow\_hdengine.egg-info/ — Python package metadata (entry points). Anchor: glow\_hdengine.egg-info/entry\_points.txt.  
  * goldens/ — Golden outputs (Reader v1 golden JSON). Anchor: goldens/reader/v1/g01\_minimal\_ineligible.json.  
  * handoff/ — Handoff bundles (evidence/patch guidance). Anchor: handoff/epic004\_live\_evidence\_20251022T202304Z/PATCH\_APPLY\_README.txt.  
  * internal/ — Internal contract snapshots (readyz). Anchor: internal/readyz/README.md.  
  * math/ — Math configuration (thresholds). Anchor: math/thresholds.json.  
  * migrations/ — SQL migrations (body\_graphs table). Anchor: migrations/011\_body\_graphs\_durability.sql.  
  * narratives/ — Narrative packs and manifests. Anchor: narratives/64e17c9c4d608f4feceedc16e43bff44e7a34208b2f32ebe49c81a8ee6ddc462/manifest.json.  
  * notes/ — QA discovery notes (vendor live QA discovery). Anchor: notes/d6\_vendor\_live\_qa\_discovery.md.  
  * parity/ — Error parity artifacts description. Anchor: parity/README.md.  
  * presenter/ — Presenter utilities and reader emitter. Anchor: presenter/reader\_v1/emitter.py.  
  * proofs/ — Proof markers (text tokens). Anchor: proofs/AB\_BA\_PARITY.txt.  
  * release/ — Release manifest (sorted). Anchor: release/manifest.sorted.json.  
  * reports/ — Token/QA reports. Anchor: reports/qa\_acceptance\_tokens.json.  
  * scan\_reports/ — Scan summaries (A7 scan). Anchor: scan\_reports/a7\_summary.txt.  
  * schemas/ — JSON schemas (Reader v1 schema). Anchor: schemas/reader.v1.schema.json.  
  * scripts/ — CLI/QA/ops scripts (hdctl wrapper). Anchor: scripts/hdctl.py.  
  * sql/ — SQL scripts (schema check). Anchor: sql/check\_schema.sql.  
  * tests/ — Test suites (reader transport tests). Anchor: tests/http/test\_reader\_a7\_transport.py.  
  * tools/ — Evidence/QA tooling (evidence index updater). Anchor: tools/evidence/update\_evidence\_index.py.  
  * validation/ — Acceptance map pointers (EPIC005 acceptance map). Anchor: validation/acceptance\_map.txt.  
* Key top-level files (present):  
  * AGENTS.md — Agent rules and governance pointers. Anchor: AGENTS.md.  
  * README.md — Repo overview and governance/evidence summary. Anchor: README.md.  
  * ARCHITECTURE.md — Repo architecture map and single-home guidance. Anchor: ARCHITECTURE.md.  
  * CHANGELOG.md — Change history and epic summaries. Anchor: CHANGELOG.md.  
  * Procfile — Gunicorn startup command. Anchor: Procfile.  
  * pyproject.toml — Python packaging and console script entrypoint (hdctl). Anchor: pyproject.toml.  
  * requirements.txt — Runtime dependencies. Anchor: requirements.txt.  
  * requirements-dev.txt — Dev/test dependencies. Anchor: requirements-dev.txt.  
  * pytest.ini — Pytest markers/testpaths. Anchor: pytest.ini.  
  * run\_flask.py — Dev Flask server script using adapter.factory.create\_app. Anchor: run\_flask.py.  
  * run\_flask\_dev.sh — Shell wrapper to run Flask dev server. Anchor: run\_flask\_dev.sh.  
  * VERIFY.sh — Local verification script for reader/transport invariants. Anchor: VERIFY.sh.  
  * adapters.DEPRECATED.md — Note about archived adapters. Anchor: adapters.DEPRECATED.md.  
* Expected HD Engine directories (classification):  
  * engine/ — Present. Anchor: engine/compat/compute.py.  
  * adapter/ — Present. Anchor: adapter/http\_reader.py.  
  * presenter/ — Present. Anchor: presenter/reader\_v1/emitter.py.  
  * CLI package location(s) — Present (engine/cli/main.py and console script in pyproject.toml).  
  * docs/ — Present. Anchor: docs/ENDPOINTS\_CATALOG.json.  
  * artifacts/ — Present. Anchor: artifacts/evidence\_index.jsonl.  
  * audit/ — Present. Anchor: audit/EPIC-024\_MANIFEST.json.  
  * tools/ — Present. Anchor: tools/evidence/update\_evidence\_index.py.  
  * ci/ and .github/workflows — Present. Anchor: .github/workflows/ci.yml.  
  * tests/ — Present. Anchor: tests/http/test\_reader\_a7\_transport.py.  
  * scripts/ — Present. Anchor: scripts/hdctl.py.  
* Root discipline capture (top-level “truth homes” identified):  
  * audit/, artifacts/, docs/, proofs/, parity/, reports/, scan\_reports/, validation/, catalog/, narratives/, internal/, scripts/, tools/. Anchors for each root are listed above in the directory map with file citations.

Packaging and Entrypoints  
3.1 Packaging / build configuration

* pyproject.toml — Defines project metadata and console script hdctl \= engine.cli.main:cli.  
* requirements.txt — Runtime dependencies include psycopg, Flask, gunicorn.   
* requirements-dev.txt — Dev/test dependencies include jsonschema and pytest-related packages.   
* glow\_hdengine.egg-info/entry\_points.txt — Console script entrypoint also recorded as hdctl \= engine.cli.main:cli.

3.2 Entrypoint inventory

* HTTP server startup:  
  * Procfile — Gunicorn launches adapter.factory:create\_app() on $PORT.  
  * adapter/factory.py:create\_app — Creates Flask app and registers reader blueprint.   
  * adapter/http\_reader.py:create\_app — Creates Flask app, registers reader and compat blueprints, and error handlers; also exposes app \= create\_app() and \_\_main\_\_ runner.   
  * adapter/wsgi.py:create\_app — Flask app with reader \+ compat blueprints and internal healthz/readyz.   
  * run\_flask.py — Dev runner that imports adapter.factory.create\_app and runs Flask.   
  * dev/reader\_harness/app.py:create\_app — Dev-only reader harness (APP\_ENV=dev) registering reader blueprint under /api.   
* CLI console scripts:  
  * pyproject.toml → hdctl \= engine.cli.main:cli.  
  * engine/cli/main.py:cli — CLI entrypoint dispatching to subcommands.   
  * scripts/hdctl.py:main — Wrapper to invoke engine.cli.main.cli.  
* Evidence/indexing entrypoints (executed via scripts/CI):  
  * tools/evidence/update\_evidence\_index.py — Evidence index/mirror updater.   
  * tools/evidence/run\_sanity\_pipeline.py — Orchestrates sanity steps and writes artifacts/sanity/sanity.log.   
  * tools/evidence/generate\_evidence\_index\_snapshot.py — Generates evidence index snapshot under audit/gates/evidence\_index\_snapshot/. 

Engine Modules (sampler/core)  
4.1 Sampler

* engine/sampler/core.py  
  * Classes: ViewerProfile, CandidateFeatures, SamplerConfig, CandidatePoolEntry, CandidatePool, RankedCandidate, RankedCandidates.  
  * Functions: build\_candidate\_pool, rank\_candidates, sample\_and\_rank (pooling \+ deterministic ranking).

4.2 Core compute

* engine/compat/compute.py  
  * band\_for maps scores to bands; compat\_public builds compat categories with meta.   
* engine/compat/ordering.py  
  * normalize\_pair enforces AB↔BA ordering and tie-breaker; pair\_key constructs normalized key. 

4.3 Determinism hazards inventory (observed in engine modules)

* Time dependence:  
  * Vendor client uses time.monotonic() and time.strftime() for timestamps.   
  * Ingest path uses time.monotonic()/time.strftime() for duration and logs.   
* Network calls:  
  * Vendor client uses urllib.request to POST to vendor endpoint.   
* File I/O:  
  * Ingest appends JSONL logs and writes artifacts. 

Adapter / HTTP Surfaces  
5.1 Route registration map

* App creation and blueprint registration:  
  * adapter/http\_reader.py:create\_app registers reader blueprint at root and compat blueprint (from engine).  
  * adapter/wsgi.py:create\_app registers reader\_bp and compat\_blueprint; adds internal healthz/readyz.   
* Blueprint definitions:  
  * Reader blueprint bp defines /reader, /aux/narrative, /api/aux/narrative, /internal/version, and /ops/writer/diagnostic.  
  * Compat blueprint compat\_blueprint is mounted with url\_prefix="/api/compat/v1".

5.2 Surface classification (based on code and endpoint catalog)

* Reader-like JSON success:  
  * /reader (GET/HEAD) — dev-only reader surface, uses canonical reader emission.   
* Aux/narrative:  
  * /aux/narrative and /api/aux/narrative — narrative text surface with headers and optional suppression.   
* Admin/internal:  
  * /internal/version — internal identity surface (GET/HEAD).   
  * /internal/healthz and /internal/readyz — health/readiness endpoints in adapter/wsgi.py.   
  * /ops/writer/diagnostic — admin writer diagnostic POST/HEAD/OPTIONS.   
* Compat admin surface:  
  * /api/compat/v1 — internal admin compat endpoint (POST, with GET probe).

5.3 Transport semantics hooks (factual)

* HEAD vs GET parity and conditional 304 handling (reader):  
  * adapter/http\_reader.py sets ETag, handles If-None-Match 304, and enforces HEAD parity with Content-Length.   
* Cache-control and content-type:  
  * \_set\_reader\_200\_headers sets Content-Type, Cache-Control, and Vary.   
  * Writer responses set Cache-Control: no-store and Content-Type with no ETag.   
* Internal/version no-ETag \+ no-store:  
  * /internal/version explicitly removes ETag and sets Cache-Control: no-store. 

Presenter / Emitter

* Canonical emitter:  
  * engine/presenter/emitter.py:emit\_public delegates to canonical serializer with sorted keys by default.   
* Reader v1 emitter:  
  * presenter/reader\_v1/emitter.py:emit\_reader\_v1 builds preimage, hashes it, and emits canonical bytes.   
* Canonical JSON serialization:  
  * engine/serializer/canon.py:sercanon delegates to stable serializer with canonical rules.   
  * engine/stable/sercanon.py:serialize ensures compact JSON and exactly one trailing LF.   
* Surfaces calling emitters:  
  * Reader HTTP path uses engine.runtime.emit\_reader\_public\_bytes and reader emitter.   
  * Compat HTTP path uses engine.presenter.emit\_public via engine.presenter. 

CLI Surfaces

* Console scripts:  
  * hdctl entrypoint in pyproject.toml points to engine.cli.main:cli.  
  * CLI parser defines subcommands showcompat, aux-preview, bg:resolve, and dev:sampler with their arguments.   
* CLI command behaviors and outputs:  
  * showcompat loads inputs, computes compat, emits canonical compat JSON to stdout, and optionally writes reader bytes to file (--dump-reader).   
  * \_emit\_stdout\_bytes enforces LF discipline on stdout.   
  * \_dump\_reader\_bytes writes reader bytes to the filesystem.   
* Call chain (CLI → engine → presenter):  
  * showcompat uses compat\_public and emit\_reader\_public\_envelope, then emitter.emit\_public to serialize. 

Vendor Seam & BodyGraph Storage  
8.1 Vendor client

* Vendor client implementation:  
  * engine/bodygraph/vendor\_client.py:HdApiClient with from\_env reading HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY.  
  * build\_request constructs POST to /bodygraphs with API keys in headers. 

8.2 BodyGraph persistence/caching

* DB persistence:  
  * Ingest uses \_persist\_bodygraph to insert into hde.body\_graphs via DBAccess.   
  * Migration defines hde.body\_graphs table with input\_fingerprint, payload, timestamps.   
* Cache key formation (orientation-safe):  
  * adapter/cache\_keys.py:build\_cache\_key returns a tuple keyed by oriented users and fingerprints. 

8.3 Offline posture / vendor gating

* Vendor ingest path enforces SAFE\_MODE and ALLOW\_NETWORK:  
  * ingest\_vendor\_bodygraph raises errors when SAFE\_MODE is true or ALLOW\_NETWORK is false.   
* Resolver gate:  
  * resolve\_bodygraph and \_resolve\_vendor return errors if SAFE\_MODE or network disallows vendor. 

Evidence, Indices, Catalogs  
9.1 Evidence homes inventory

* docs/ — Human evidence index and acceptance maps; endpoint catalog is in docs/ENDPOINTS\_CATALOG.json.  
* artifacts/ — Machine evidence mirror and generated logs/artifacts (JSONL mirror).  
* audit/ — QA close-pack manifest and QA logs (example EPIC024 manifest).  
* proofs/ — Proof tokens for CLI/reader parity.  
* parity/ — HTTP/CLI error parity artifacts description.   
* internal/ — Contract snapshots for internal readiness responses.   
* reports/ and scan\_reports/ — Token reports and scan summaries.   
* validation/ — Acceptance map pointer files. 

9.2 Evidence index structures

* Human index: docs/evidence/INDEX.json.  
* Human index hash: docs/evidence/INDEX.sha256.  
* Machine mirror: artifacts/evidence\_index.jsonl (JSONL records with proof\_anchor).  
* Tooling:  
  * tools/evidence/update\_evidence\_index.py manages index/mirror updates.   
  * tools/evidence/generate\_evidence\_index\_snapshot.py generates snapshot gate artifacts. 

9.3 Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json lists endpoints with classification and blueprint module.  
  * The catalog includes /internal/version, /api/compat/v1, and /reader entries with classifications.

9.4 Proof artifacts / snapshot artifacts

* HTTP transport proof snapshots exist in artifacts/proofs/, e.g. success\_get.txt.  
* The reader transport test includes optional proof writes when HDE\_WRITE\_A7\_PROOFS=1. 

Tests, QA Harness, CI/Checks  
10.1 Tests map (selected loci)

* Reader transport invariants: tests/http/test\_reader\_a7\_transport.py validates headers, ETag, 304, and HEAD parity.   
* Compat endpoint contract \+ catalog check: tests/http/test\_compat\_endpoint\_contract.py verifies /api/compat/v1 behavior and catalog entry.   
* CLI showcompat parity/identity: tests/cli/test\_showcompat\_parity\_and\_identity.py checks two-run identity and reader dump parity.   
* Reader emitter behavior: tests/reader\_v1/test\_emitter.py exercises emit\_reader\_v1 and schema.   
* Evidence index coverage: tests/ops/test\_evidence\_index.py checks index/mirror entries and path proofs. 

10.2 CI workflows

* .github/workflows/ci.yml runs determinism checks, evidence index updates, serializer guards, and test suites. 

10.3 Script/check inventory (QA-relevant)

* ci/checks/check\_env\_pins.sh — Runs determinism env pin log generation/verification.   
* ci/checks/check\_cli\_help.sh — Ensures python \-m engine.cli \--help exits cleanly with stdout and final LF.   
* ci/checks/check\_evidence\_index\_hash.sh — Validates INDEX.json sha256 sentinel.   
* ci/checks/check\_final\_lf.sh — Enforces final LF and no CR on key evidence files.   
* ci/checks/check\_mirror\_schema.sh — Validates evidence mirror schema/order and path-proof bindings.   
* ci/checks/check\_release\_identity.sh — Validates release identity inputs and recompute check.   
* ci/checks/check\_bridge\_consistency.py — Cross-checks DB bridge snapshots for consistency.   
* tools/evidence/update\_evidence\_index.py — Evidence index updater.   
* tools/evidence/run\_sanity\_pipeline.py — Closed-rails sanity pipeline runner.   
* tools/evidence/generate\_evidence\_index\_snapshot.py — Evidence index snapshot gate generator.   
* tools/qa/run\_hde\_epic024\_harness.py — EPIC024 QA harness entrypoint writing QA logs.   
* scripts/qa/d6\_live\_vendor\_qa.py — Open-rails vendor QA harness for EPIC019 D6 (writes audit logs).   
* scripts/qa/dev\_sampler\_healthcheck.py — Dev sampler healthcheck harness logging rails snapshots.   
* scripts/qa/dev\_sampler\_live\_qa.py — Closed-rails dev sampler QA harness logging outcomes under audit.   
* scripts/qa/epic009\_precommit.sh — Precommit QA script running evidence checks and validations. 

Flows & Call Chains

1. Reader success flow (HTTP)  
* Call chain: adapter/http\_reader.py:reader\_v1 → engine/runtime/public.py:emit\_reader\_public\_bytes → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine/presenter/emitter.py:emit\_public → engine/serializer/canon.py:sercanon → engine/stable/sercanon.py:serialize.  
* Notes:  
  * Reader endpoint checks APP\_ENV and required query args, then emits canonical bytes with ETag.   
  * HEAD and 304 semantics are implemented within the reader handler.   
  * Canonical serialization is centralized via sercanon/serialize.   
2. Compat API flow (HTTP)  
* Call chain: engine/http/compat\_handler.py:post\_json → engine/compat/compute.py:compat\_public → engine/presenter/emitter.py:emit\_public → Flask Response.  
* Notes:  
  * Compat blueprint mounted at /api/compat/v1.  
  * The handler validates inputs and returns a JSON payload with keys.   
  * Emission uses canonical emitter (emit\_public).   
3. CLI showcompat / compat preview flow  
* Call chain: engine/cli/main.py:showcompat → engine/compat/compute.py:compat\_public → engine/runtime/public.py:emit\_reader\_public\_envelope → engine/presenter/emitter.py:emit\_public → \_emit\_stdout\_bytes.  
* Notes:  
  * showcompat emits compat JSON to stdout and optionally writes reader bytes to file (--dump-reader).   
  * \_emit\_stdout\_bytes enforces LF/CRLF discipline on stdout payloads.   
4. Vendor acquisition flow (BodyGraph ingest)  
* Call chain: engine/bodygraph/resolver.py:resolve\_bodygraph → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.from\_env/build\_request/fetch → engine/db/adapter.py:DBAccess.for\_current\_env → \_persist\_bodygraph (SQL insert).  
* Notes:  
  * Vendor ingest path is gated by SAFE\_MODE/ALLOW\_NETWORK.   
  * DB persistence inserts into hde.body\_graphs defined in migrations.   
5. Evidence index update/validation flow  
* Call chain: tools/evidence/update\_evidence\_index.py → tools/evidence/run\_sanity\_pipeline.py (includes update\_evidence\_index steps) → ci/checks/check\_evidence\_index\_hash.sh and ci/checks/check\_mirror\_schema.sh.  
* Notes:  
  * Evidence mirror and human index are refreshed/validated via tooling and CI checks. 

Drift and Reality vs Expectations  
12.1 Drift categories

* Directory/architecture drift:  
  * Observation: vendor seam is implemented under engine/bodygraph/vendor\_client.py rather than a top-level vendor/ directory.   
  * Impact: This places vendor integration inside the engine package rather than a distinct top-level vendor directory, which may affect how the architecture is mapped to an expected vendor layer.   
* Surface drift (multiple HTTP app factories):  
  * Observation: multiple Flask app factories exist (adapter/http\_reader.py:create\_app, adapter/wsgi.py:create\_app, adapter/factory.py:create\_app, dev/reader\_harness/app.py:create\_app).   
  * Impact: There are multiple entrypoint surfaces to mount routes, which creates multiple concrete HTTP startup paths.   
* Evidence drift (multiple homes):  
  * Observation: governed/evidence-like outputs are stored across audit/, artifacts/, docs/, proofs/, parity/, reports/, scan\_reports/, validation/, catalog/, narratives/, and internal/.  
  * Impact: Evidence artifacts are distributed across multiple roots, which creates multiple homes for governed outputs.   
* Determinism drift (hazards present in engine modules):  
  * Observation: vendor ingest uses time and network (e.g., time.monotonic, urllib.request).  
  * Impact: These flows depend on time and external network calls in the vendor path.   
* Vendor seam drift (location within engine):  
  * Observation: vendor client is under engine/bodygraph/ and invoked from the CLI and ingest paths.   
  * Impact: Vendor integration is located within engine bodygraph modules rather than a separate top-level vendor module.   
* Root proliferation:  
  * Observation: 13 roots identified for governed/“truth home” outputs (audit/, artifacts/, docs/, proofs/, parity/, reports/, scan\_reports/, validation/, catalog/, narratives/, internal/, scripts/, tools/).  
  * Impact: Multiple top-level roots act as evidence/contract homes, which creates a multi-root evidence surface. 

12.2 Alignment summary table (optional)

* Engine/adapter/presenter split: Aligned (engine, adapter, presenter directories present with defined responsibilities).  
* Single emitter usage: Partial (canonical emitter exists; multiple entrypoints call it).  
* Vendor seam outside engine: Drift (vendor client under engine/bodygraph/).  
* Evidence layout: Partial (human index \+ mirror present, but multiple evidence roots).

Negative-Claim Proof Appendix

* Claim: No top-level vendor/ directory found.  
  * Search: find . \-maxdepth 1 \-type d \-name 'vendor'  
  * Scope: repo root  
  * Result: 0 hits (empty output)

Testing

