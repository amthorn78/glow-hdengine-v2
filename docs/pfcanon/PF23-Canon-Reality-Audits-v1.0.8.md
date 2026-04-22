# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.8

**Status:** Canon

**Effective date:** 2026-04-17

**Last Update Gate:** HDE-EPIC029

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

# 1\) \- HD Engine Current Audit 

**Date:** 2026-04-17

**Last Epic:** HDE-EPIC029

## Audit Snapshot Metadata

* Repo root confirmed: pwd returned /workspace/glow-hdengine-v2.  
* Commit: git rev-parse HEAD → eab6f0b2a333bd3bf88f483af0b5ce8f84cd17c6.  
* Branch: git rev-parse \--abbrev-ref HEAD → work.  
* Working tree cleanliness: git status \--porcelain returned empty output (clean).  
* Timestamp (UTC): date \-u \+"%Y-%m-%dT%H:%M:%SZ" → 2026-04-17T11:00:37Z.  
* Execution environment:  
  * uname \-srmo → Linux 6.12.47 x86\_64 GNU/Linux  
  * python3 \--version → Python 3.10.19  
  * node \--version → v22.21.1

---

## Top-level Repo Map

### Expected HD Engine families

* engine/ — Present. Core runtime, compat, sampler, db, bodygraph, CLI, serializer, presenter modules are present under this package. Anchors: engine/cli/main.py, engine/compat/compute.py, engine/bodygraph/ingest.py.  
* adapter/ — Present. Flask-facing HTTP surfaces and app factory wiring exist here. Anchors: adapter/http\_reader.py, adapter/factory.py, adapter/wsgi.py.  
* presenter/ (top-level) — Present. Reader v1 emitter and JSON compare utility exist here. Anchors: presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py.  
* CLI package location(s) — Present. Declared console script hdctl \= engine.cli.main:cli, plus script wrapper scripts/hdctl.py.  
* docs/ — Present. Contracts, schemas, pfcanon, evidence, acceptance maps are present. Anchors: docs/evidence/INDEX.json, docs/ENDPOINTS\_CATALOG.json, docs/pfcanon/ directory listing observed.  
* artifacts/ — Present. Large generated/governed output home including evidence mirror, cli artifacts, proofs, ingest logs. Anchors: artifacts/evidence\_index.jsonl, artifacts/cli/showcompat/, artifacts/proofs/.  
* audit/ — Present. Gate logs, QA roots, close-pack artifacts, and epic audit trees. Anchors: audit/gates/json\_gate/canonical/, audit/qa/hde-epic027/, audit/EPIC-024\_close\_report.md (referenced by harness).  
* tools/ — Present. Evidence/indexing, QA harnesses, config and registry generators. Anchors: tools/evidence/update\_evidence\_index.py, tools/evidence/run\_sanity\_pipeline.py, tools/qa/run\_hde\_epic024\_harness.py.  
* ci/ \+ .github/workflows — Present. Shell/python checks and GH Actions workflows are present. Anchors: .github/workflows/ci.yml, ci/checks/check\_env\_pins.sh.  
* tests/ — Present. Broad suite with adapter/http/cli/evidence/db/qa/etc roots. Anchors: tests/http/test\_compat\_endpoint\_contract.py, tests/evidence/test\_evidence\_skeleton.py, tests/cli/test\_showcompat\_parity\_and\_identity.py.  
* scripts/ — Present. Runner utilities, CLI wrappers, DB jobs, and ops scripts. Anchors: scripts/hdctl.py, scripts/bodygraph/run\_refresh\_worker.py, scripts/db/run\_retention\_job.py.

### Root discipline capture (truth-home-looking roots observed)

From top-level listing, evidence/governed-output-looking roots include:  
audit/, artifacts/, docs/, tools/, scripts/, parity/, errors/, proofs/, reports/, scan\_reports/.  
---

## Packaging and Entrypoints

### 3.1 Packaging / build configuration

* pyproject.toml declares setuptools build backend, project metadata, console script hdctl, and package discovery include engine\*, adapter\*, presenter\*.  
* requirements.txt includes runtime deps (psycopg\[binary\], Flask, gunicorn).  
* requirements-dev.txt includes jsonschema, pytest, pytest-cov, pytest-mock.  
* pytest.ini sets markers and explicit testpaths across many test families.

### 3.2 Entrypoint inventory

* HTTP startup (prod): Procfile runs gunicorn with adapter.factory:create\_app().  
* HTTP startup (dev): run\_flask.py imports adapter.factory.create\_app, runs app.run(...).  
* App factories:  
  * adapter.factory:create\_app registers reader \+ compat blueprints and common headers.  
  * adapter.http\_reader:create\_app also builds app and mounts reader/compat blueprints.  
  * adapter.wsgi:create\_app mounts reader/compat and internal header strip hook.  
* CLI console script: hdctl \-\> engine.cli.main:cli.  
* CLI module entrypoint: engine/cli/\_\_main\_\_.py:main calls cli() and exits with status code.  
* Scheduled/background jobs relevant to evidence/indexing/ingest:  
  * scripts/bodygraph/run\_refresh\_worker.py:run\_refresh (out-of-band bodygraph refresh worker).  
  * scripts/db/run\_retention\_job.py:main runs retention and writes artifacts/db/retention/retention\_run.log.  
  * tools/evidence/update\_evidence\_index.py updates index/sentinel/mirror paths constants for docs/artifacts evidence indices.

---

## Engine Modules

### 4.1 Sampler

* Module: engine/sampler/core.py.  
* Primary symbols and roles:  
  * ViewerProfile, CandidateFeatures, SamplerConfig, CandidatePoolEntry, CandidatePool, RankedCandidate, RankedCandidates: typed state carriers for sampling/ranking stages.  
  * build\_candidate\_pool(...): filters zero-weight/ineligible candidates into pool.  
  * rank\_candidates(...): deterministic sort/rank with comparator chain.  
  * sample\_and\_rank(...): convenience wrapper pool-\>rank pipeline.

### 4.2 Core compute

* Compatibility metrics/result structure: engine/compat/compute.py:compat\_public(...) builds category list (id/score/band/...) plus meta.  
* AB↔BA parity/symmetry: compat\_public normalizes pair via normalize\_pair \+ pair\_key; conjunction\_public also normalizes left/right pair before compat call.  
* Boundary normalization/canonicalization: score generation uses deterministic hash of pair\_key:category; output category ordering follows CATEGORIES\_ORDER\_V1 iteration.  
* Conjunction resolution path: conjunction\_public\_resolved(...) handles local lookup, resolver acquisition, and vendor error mapping.

### 4.3 Determinism hazards inventory (engine modules sampled)

Observed in sampled engine paths:

* Time usage  
  * engine/bodygraph/vendor\_client.py uses time.monotonic, time.gmtime, time.sleep.  
  * engine/bodygraph/ingest.py uses time.monotonic and timestamp formatting for logs.  
* Network calls  
  * HdApiClient.fetch builds urllib.request.Request and performs HTTP request via \_request.  
* File I/O  
  * Ingest appends logs to artifacts/ingest/\* and writes JSONL logs.  
* Randomness  
  * No random module usage observed in sampled engine files (engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/\* sampled).

---

## Adapter / HTTP Surfaces

### 5.1 Route registration map

* Router/app creation modules  
  * adapter/http\_reader.py:create\_app() creates Flask app and registers bp \+ compat\_blueprint.  
  * adapter/factory.py:create\_app() also registers reader\_bp \+ compat\_blueprint.  
  * adapter/wsgi.py:create\_app() registers both blueprints too.  
* Path prefixes  
  * Compat blueprint has url\_prefix="/api/compat/v1" in engine/http/compat\_handler.py.  
  * Reader blueprint mounted with empty prefix in app factories (url\_prefix="" or default).

### 5.2 Surface classification

* Reader-like JSON success: /reader GET/HEAD in reader\_v1, emits JSON with ETag semantics. Handler: reader\_v1.  
* Aux/narrative: /api/aux/narrative and /aux/narrative, handler aux\_narrative, returns text/plain with narrative headers.   
* Admin/internal: /internal/version; /ops/writer/diagnostic; /ops/probe/env; /ops/db/unavailable; /ops/rails/refusal.  
* Dev/diagnostic harness: /internal/dev/sampler, /dev/\*/conjunction gated by \_dev\_admin\_gate.  
* Compat API surface: /api/compat/v1 GET/POST/HEAD/OPTIONS in engine/http/compat\_handler.py.

### 5.3 Transport semantics hooks

* HEAD vs GET parity  
  * /reader has explicit HEAD branch returning empty body \+ GET-equivalent Content-Length.  
  * /internal/version has explicit HEAD branch with same content type and Content-Length from GET bytes.  
* Conditional responses / 304  
  * /reader parses If-None-Match and returns 304 on strong match (with body removed).  
* ETag generation/quoting  
  * /reader: etag \= "\\"" \+ sha256(body) \+ "\\"".  
  * Aux narrative sets ETag from digest and quoted string.  
* Cache-control rules  
  * Reader success: private, max-age=0, must-revalidate; errors/internal many paths set no-store.  
* Content-Type rules  
  * Reader success sets application/json; charset=utf-8; aux narrative sets text/plain; charset=utf-8; writer paths enforce strict JSON content-type check. 

---

## Presenter / Emitter

* Engine emitter: engine/presenter/emitter.py  
  * emit\_public delegates canonical serialization (canon.sercanon), default sorted keys.  
  * emit\_public\_with\_envelope, emit\_compact\_json wrappers.  
* Canonical serializer: engine/serializer/canon.py:sercanon delegates to stable serializer and documents UTF-8/sorted keys/compact/one LF behavior.  
* Reader v1 emitter: presenter/reader\_v1/emitter.py:emit\_reader\_v1 builds preimage, hashes preimage bytes, appends idempotence\_hash, re-emits canonical bytes.   
* Callers/surfaces  
  * HTTP adapter imports engine.presenter.emitter.emit\_public.  
  * Compat handler imports from engine.presenter import emit\_public.  
  * Runtime public emits reader via presenter.reader\_v1.emitter.emit\_reader\_v1.  
  * CLI uses engine.presenter.emitter for stdout payloads.

---

## CLI Surfaces

* Console script: hdctl from pyproject.toml.  
* Main parser & commands: \_build\_parser defines subcommands:  
  * showcompat (+ \--pair-file, \--a-file/--b-file, \--source, \--conjunction, \--user-a/--user-b, vendor birth args, dump args).  
  * aux-preview (+ narrative args/pair-file/admin-out).  
  * bg:resolve (+ \--user, \--source, \--upsert, \--dry-run, birth args).  
  * dev:sampler (+ viewer/candidates-file/seed).  
* Entrypoints and chain  
  * cli() parses and dispatches to handler; CliError maps to stderr token and exit code.  
  * showcompat path calls loader(s) → compat\_public/conjunction\_public\_resolved → emitter → stdout bytes LF/CRLF guards.  
* Output surfaces  
  * Writes optional files: \--dump-reader path and \--dump-admin-dir artifacts via canon\_dump.  
  * Stdout writes canonical bytes via \_emit\_stdout\_bytes.  
  * Nonzero exits on parse/missing args/errors via argparse remap \+ CliError.

---

## Vendor Seam & BodyGraph Storage

### 8.1 Vendor client

* HTTP client module: engine/bodygraph/vendor\_client.py.  
* Key symbols: HdApiClient, VendorRequest, VendorResult, VendorError.  
* Inputs from env/config: HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, optional RELEASE\_ID.  
* Request shaping: build\_request canonicalizes date, creates JSON body \+ headers.   
* Response parsing: fetch expects status 200 JSON body, maps non-200/network to typed vendor errors. 

### 8.2 BodyGraph persistence/caching

* DB adapter layer: engine/db/adapter.py with provider selection (psycopg / bridge), attempts snapshot at artifacts/db\_bridge/adapter\_selection.snapshot.json.  
* Ingest persistence: ingest\_vendor\_bodygraph writes to hde.body\_graphs table via \_persist\_bodygraph; then reads row count/payload for parity comparison.   
* Cache key/idempotency form: \_idempotency\_key builds ${user\_id}:${vendor}:${vendor\_version}:${fingerprint}.  
* Read cached vs call vendor: conjunction\_public\_resolved tries local\_lookup first, then calls resolve\_bodygraph(...source="vendor"... ) on miss. 

### 8.3 Offline posture / vendor gating

* Explicit gating observed:  
  * ingest\_vendor\_bodygraph refuses when SAFE\_MODE true (PROVIDER\_REFUSED) or ALLOW\_NETWORK false (PROVIDER\_NETWORK\_BLOCKED).  
  * resolve\_bodygraph vendor path returns explicit error payloads for closed rails / network blocked.  
  * HTTP conjunction path sets rails env and only preloads local people when rails open (SAFE\_MODE=0 and ALLOW\_NETWORK=1).

---

## Evidence, Indices, Catalogs

### 9.1 Evidence homes inventory

* docs/evidence/: human index and hash sentinel (INDEX.json, INDEX.sha256), appears generated from tooling (index updater references exact paths).  
* artifacts/: machine mirror (evidence\_index.jsonl), CLI/compat/proofs/sanity/ingest outputs; mixed generated snapshots/logs. Example mirror file exists with JSONL artifact records.  
* audit/: gates and epic QA roots (audit/gates/\*, audit/qa/\*), includes canonical JSON gate directories and close packs referenced by harnesses/tools. 

### 9.2 Evidence index structures

* docs/evidence/INDEX.json exists (JSON array content on line 1 in current file).  
* docs/evidence/INDEX.sha256 exists and stores hash sentinel line format (\<sha\> docs/evidence/INDEX.json).  
* artifacts/evidence\_index.jsonl exists with machine mirror records (artifact\_key, discovered\_physical\_path, etc.).  
* Tooling read/write/validate  
  * Updater constants and logic in tools/evidence/update\_evidence\_index.py.  
  * Orientation coherence checks use mirror \+ index in tools/evidence/orientation\_demo.py.  
  * Mirror schema checker validates JSONL keys/order/path proofs in ci/checks/check\_mirror\_schema.sh.

### 9.3 Endpoint catalog

* Catalog file: docs/ENDPOINTS\_CATALOG.json with top-level endpoints and success\_endpoints; each endpoint includes path/method/classification/gates metadata.  
* Referenced by tests: tests/http/test\_endpoint\_catalog.py and tests/http/test\_compat\_endpoint\_contract.py read this catalog via Path(...).read\_text(...). (Found via repo search output.)

### 9.4 Proof/snapshot artifacts

* Mirror contains A7 snapshots such as artifacts/proofs/success\_get.txt, success\_head.txt, success\_304.txt etc (artifact keys shown in mirror lines).  
* Producer linkage: tools in tools/evidence/\* include index/gate/orientation generators; canonical JSON gate writes audit artifacts and path proofs using updater helper. 

---

## Tests, QA Harness, CI/Checks

### 10.1 Tests map

* Test roots present include tests/adapter, tests/http, tests/cli, tests/evidence, tests/qa, tests/transport, tests/db, etc (directory listing).  
* Compat/reader endpoint tests  
  * tests/http/test\_reader\_a7\_transport.py, tests/http/test\_compat\_endpoint\_contract.py, tests/adapter/test\_reader\_parity.py, tests/adapter/test\_compat\_http\_dev.py (found via search output).  
* CLI outputs/canonical bytes tests  
  * tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/cli/test\_cli\_canonical\_bytes.py, tests/cli/test\_serializer\_guards.py (also directly run in CI job).  
* Determinism gates  
  * Core determinism tests reference ensure\_determinism\_env (search hits in tests/core/test\_engine\_core\_determinism.py).  
* Evidence index/catalog tests  
  * tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py, tests/http/test\_endpoint\_catalog.py (search hits).

### 10.2 CI workflows

* Workflow file: .github/workflows/ci.yml defines multiple jobs (test, compat-conj-pr01-closure, epic020, compat-http-epic020, epic020-evidence-bundles, sanity-pipeline).  
* Evidence discipline checks in CI: env pins, canonical gate, evidence index update/check, orientation check, mirror schema, final LF checks.   
* EPIC020 acceptance job runs explicit adapter/cli/transport/qa tests list. 

### 10.3 Script/check inventory (QA-relevant, read-only)

* ci/checks/check\_env\_pins.sh: invokes determinism env checker against audit/gates/determinism/env\_pins.log.  
* ci/checks/check\_evidence\_index\_hash.sh: verifies INDEX.json sha against INDEX.sha256.  
* ci/checks/check\_mirror\_schema.sh: validates machine mirror structure/ordering/path proof relations and self-record logic.   
* tools/evidence/run\_sanity\_pipeline.py: orchestrates deterministic step sequence, writes artifacts/sanity/sanity.log, refreshes evidence index post-log.   
* tools/evidence/run\_canonical\_json\_gate.py: checks canonical byte conformance across target artifacts and writes gate outputs/path proofs.   
* tools/qa/run\_hde\_epic024\_harness.py: QA harness writing per-check logs, manifests, doc deltas, close-pack files under audit roots. 

---

## Flows & Call Chains

### 1\) Reader success flow (HTTP)

adapter/http\_reader.py:reader\_v1 → engine/runtime/public.py:emit\_reader\_public\_bytes → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine/presenter/emitter.py:emit\_public

* Route /reader is registered in reader blueprint.  
* Handler validates params/files and builds engine identity values from env/defaults.  
* Calls emit\_fn defaulted to emit\_reader\_public\_bytes.  
* Sets ETag and conditional/HEAD/200 behavior in transport layer.   
* Runtime module computes harmony band and delegates reader v1 emitter for canonical bytes. 

### 2\) Compat API flow (HTTP)

engine/http/compat\_handler.py:post\_json → engine/compat/compute.py:compat\_public → engine/presenter.emit\_public

* Compat blueprint mounted at /api/compat/v1.  
* POST validates mixed input modes and viewer prefs; resolves ids to person payloads.   
* Calls compat\_public(...) to compute categories/meta and adds keys list.   
* Emits JSON envelope via \_writer\_payload with no-store and cleared ETag. 

### 3\) CLI showcompat / compat preview flow

engine/cli/main.py:cli → showcompat → (source loader) → compat\_public / conjunction\_public\_resolved → emitter.emit\_public → stdout

* cli() dispatches parsed command to handler.   
* showcompat supports file/stdin/db/vendor/auto source selection and conjunction mode switch.   
* Standard compat path computes compat payload and canonical bytes (emitter.emit\_public).  
* Output guard enforces exactly one LF and rejects CRLF before stdout write.   
* Optional file writes occur for \--dump-reader and admin dump dir. 

### 4\) Vendor acquisition flow (BodyGraph ingest)

engine/cli/main.py:showcompat(source=vendor) → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.fetch → engine/db/adapter.py:DBAccess

* Vendor source path builds VendorInputs from birth args and calls ingest in dry-run for showcompat vendor path.   
* Ingest enforces rails (SAFE\_MODE, ALLOW\_NETWORK) before network client usage.   
* Client env config requires HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY; request built then fetched via HTTP.   
* Non-dry-run ingest persists into hde.body\_graphs, then verifies parity and logs artifacts. 

### 5\) Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py → docs/evidence/INDEX.json \+ docs/evidence/INDEX.sha256 \+ artifacts/evidence\_index.jsonl → tools/evidence/orientation\_demo.py \--check \+ ci/checks/check\_mirror\_schema.sh

* Updater defines canonical human index, sentinel, mirror paths.   
* CI runs updater write/check and orientation check in sequence.   
* Orientation demo loads mirror/index and validates coherence and proofs.   
* Mirror schema check validates required keys, sorting, proofs, self-record semantics. 

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: presenter logic exists in both engine/presenter/\* and top-level presenter/\*.  
  Impact (factual): This creates two presenter code roots in the repo tree.  
* Observed: HTTP surfaces are split across adapter/http\_reader.py and engine/http/compat\_handler.py then mounted together by adapter factories.  
  Impact: Routing ownership is distributed across adapter and engine package paths.

### Surface drift

* Observed: endpoint catalog marks /api/compat/v1 as internal\_admin and /reader as dev-harness A7-eligible; dev conjunction routes are cataloged as dev\_harness.  
  Impact: Surface classes are heterogeneous (public-like, internal, dev-harness) within one catalog file.

### Evidence drift

* Observed: governed/evidence-like outputs are spread across docs/, artifacts/, and audit/; updater/orientation/check scripts coordinate across these homes.  
  Impact: Evidence lifecycle depends on multi-root synchronization.

### Determinism drift

* Observed: determinism rails are explicitly pinned in runtime \+ CI (LC\_ALL/LANG/TZ/SAFE\_MODE/ALLOW\_NETWORK) while some modules still use clock functions for logs/retries.   
  Impact: Determinism posture includes both strict environment pins and time-based operational logging behavior.

### Vendor seam drift

* Observed: vendor acquisition is in engine/bodygraph/\*; adapter layer calls into engine.compat.compute.conjunction\_public\_resolved that can trigger resolver/vendor path depending on rails/local lookup.  
  Impact: Vendor seam is not isolated to a single adapter-only module path.

### Path-case drift

* Observed: top-level includes mixed-case file names (e.g., AcceptanceMap.md, Run, README.md) and lowercase directory patterns together (from listing output).  
  Impact: Case-style is mixed across root artifacts.

### Root proliferation (fact report)

* Observed: 10 top-level roots that look like evidence/truth homes: audit, artifacts, docs, tools, scripts, parity, errors, proofs, reports, scan\_reports.  
  Impact: Multiple roots exist for audit/evidence-related material.

---

## Negative-Claim Proof Appendix

1. No setup.cfg found  
   * Search token: setup.cfg  
   * Method: rg \--files \-g 'setup.cfg'  
   * Scope: repo root (/workspace/glow-hdengine-v2)  
   * Result: 0 hits (command returned no output, exit code 1).  
2. No setup.py found  
   * Search token: setup.py  
   * Method: rg \--files \-g 'setup.py'  
   * Scope: repo root  
   * Result: 0 hits.  
3. No package.json found  
   * Search token: package.json  
   * Method: rg \--files \-g 'package.json'  
   * Scope: repo root  
   * Result: 0 hits.  
4. No pnpm-workspace.yaml found  
   * Search token: pnpm-workspace.yaml  
   * Method: rg \--files \-g 'pnpm-workspace.yaml'  
   * Scope: repo root  
   * Result: 0 hits.  
5. No poetry.lock found  
   * Search token: poetry.lock  
   * Method: rg \--files \-g 'poetry.lock'  
   * Scope: repo root  
   * Result: 0 hits.  
6. No top-level vendor/ or db/ directory found  
   * Search tokens: directory names vendor, db  
   * Method: find . \-maxdepth 1 \-mindepth 1 \-type d \-name 'vendor' \-o \-name 'db'  
   * Scope: repo root  
   * Result: 0 hits.

---

## Commands run (audit checks)

* ✅ pwd  
* ✅ rg \--files \-g 'AGENTS.md'  
* ✅ git rev-parse HEAD  
* ✅ git rev-parse \--abbrev-ref HEAD  
* ✅ git status \--porcelain  
* ✅ date \-u \+"%Y-%m-%dT%H:%M:%SZ"  
* ✅ uname \-srmo  
* ✅ python3 \--version  
* ✅ node \--version  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-printf '%P\\n' | sort  
* ✅ find engine \-maxdepth 3 \-type f | sort  
* ✅ find presenter \-maxdepth 4 \-type f | sort  
* ✅ find docs/artifacts/audit ... (bounded-depth directory inventories)  
* ✅ find .github/workflows \-maxdepth 2 \-type f | sort  
* ✅ find tests \-maxdepth 2 \-type d | sort  
* ✅ find ci/checks \-maxdepth 2 \-type f | sort  
* ✅ find tools \-maxdepth 3 \-type f | sort  
* ✅ find scripts \-maxdepth 2 \-type f | sort  
* ✅ rg \-n "\<route/entrypoint/test tokens\>" tests ... (scoped grep)  
* ✅ rg \--files \-g 'setup.cfg' \-g 'setup.py' \-g 'package.json' \-g 'pnpm-workspace.yaml' \-g 'poetry.lock' . (negative-claim proof)  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-type d \-name 'vendor' \-o \-name 'db' (negative-claim proof)  
* 

