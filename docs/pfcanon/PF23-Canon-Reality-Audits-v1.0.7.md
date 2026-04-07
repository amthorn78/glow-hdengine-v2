# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.7

**Status:** Canon

**Effective date:** 2026-03-28

**Last Update Gate:** HDE-EPIC028

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

**Date:** 2026-03-28

**Last Epic:** HDE-EPIC028

## Audit Snapshot Metadata

* Repo root confirmation: pwd and git rev-parse \--show-toplevel both returned /workspace/glow-hdengine-v2.  
* Commit: 969ce9d912ae9c49a11f5cd451b09f15afd8fb39 (git rev-parse HEAD).  
* Branch: work (git rev-parse \--abbrev-ref HEAD).  
* Working tree cleanliness: clean (git status \--porcelain returned no paths between porcelain-start and porcelain-end).  
* Timestamp (UTC): 2026-03-28T17:32:08Z (date \-u).  
* Execution environment facts:  
  * OS/kernel: Linux 6.12.47 x86\_64 GNU/Linux (uname \-srmo)  
  * Python: Python 3.10.19 (python3 \--version)  
  * Node: v22.21.1 (node \--version)

---

## Top-level Repo Map

### Top-level presence map (from find . \-maxdepth 1 \-mindepth 1\)

Observed major roots include: engine, adapter, presenter, docs, artifacts, audit, tools, ci, tests, scripts, .github, catalog, schemas, config, dev, fixtures, sql, migrations, plus many report/evidence files at root.

### Expected HD Engine families

* engine/ — Present.  
  * Contains core runtime, compat, sampler, bodygraph, DB, HTTP compat handler, CLI package, serializer, and deterministic env utilities.  
  * Representative anchors: engine/sampler/core.py, engine/compat/compute.py, engine/cli/main.py.  
* adapter/ — Present.  
  * Contains Flask adapter surfaces, app factory/wsgi composition, transport/header behavior, and helper modules.  
  * Anchors: adapter/http\_reader.py, adapter/wsgi.py, adapter/factory.py.  
* presenter/ — Present (top-level) and also engine/presenter/ present.  
  * Top-level presenter has reader\_v1/emitter.py; engine-level presenter has canonical emitter API.  
  * Anchors: presenter/reader\_v1/emitter.py, engine/presenter/emitter.py.  
* CLI package location(s) — Present.  
  * Packaged CLI entrypoint is engine.cli.main:cli; wrapper launcher exists at scripts/hdctl.py.  
* docs/ — Present.  
  * Contains acceptance maps, endpoint catalog, evidence index, architecture/contract docs.  
  * Anchors: docs/ENDPOINTS\_CATALOG.json, docs/evidence/INDEX.json, docs/acceptance\_map\_epic027.json.  
* artifacts/ — Present.  
  * Contains generated evidence outputs (CLI, proofs, math, registry, runtime, audit mirrors, etc.).  
  * Anchors: artifacts/evidence\_index.jsonl, artifacts/cli/ab.json, artifacts/math/release\_id.txt (path existence from listing).  
* audit/ — Present.  
  * Contains epic manifests/close reports, QA subtrees, gates, docdelta evidence.  
  * Anchors: audit/EPIC-027\_MANIFEST.json, audit/EPIC-024\_close\_report.md, audit/qa/... (path existence from listing).  
* tools/ — Present.  
  * Contains governed generators/checkers for evidence, QA, CLI conformance, config bundles.  
  * Anchors: tools/evidence/update\_evidence\_index.py, tools/evidence/run\_sanity\_pipeline.py, tools/qa/generate\_epic027\_close\_pack.py.  
* ci/ and .github/workflows — Present.  
  * CI scripts in ci/checks/\*; workflow in .github/workflows/ci.yml.  
* tests/ — Present.  
  * Large multi-domain suite across adapter/CLI/evidence/order/qa/etc.  
  * Anchor: test tree listing and individual tests below.  
* scripts/ — Present.  
  * Contains CLI wrappers, worker jobs, validation utilities, QA scripts.  
  * Anchors: scripts/hdctl.py, scripts/bodygraph/run\_refresh\_worker.py, scripts/db/run\_retention\_job.py.

### Root discipline capture (truth-home-like roots observed)

Factually observed top-level homes containing governed/evidence-like outputs or governance content:  
audit/, artifacts/, docs/, tools/, scripts/, catalog/, schemas/, ci/, plus some root-level report files (CANON\_CHECKSUMS.json, changes\_report.txt, etc.) from listing output.  
---

## Packaging and Entrypoints

### 3.1 Packaging / build configuration

* pyproject.toml found with setuptools build backend and one project script:  
  * Project name glow-hdengine, Python \>=3.10, no declared runtime deps, script hdctl \= engine.cli.main:cli, package discovery includes engine\*, adapter\*, presenter\*.  
* Root requirements files found: requirements.txt, requirements-dev.txt (filesystem listing).  
* setup.py not found and setup.cfg not found (see Negative-Claim appendix).

### 3.2 Entrypoint inventory

* HTTP startup / app assembly  
  * adapter/wsgi.py:create\_app creates Flask app, installs logging/env guard, registers reader\_bp and compat\_blueprint.  
  * adapter/http\_reader.py:create\_app registers reader/internal blueprint and compat blueprint, adds scoped error handlers.  
  * run\_flask.py imports adapter.factory:create\_app and runs development server in \_\_main\_\_.  
  * dev/reader\_harness/app.py:create\_app mounts reader blueprint at /api and enforces APP\_ENV=dev.  
* CLI console scripts  
  * Packaged hdctl entrypoint: engine.cli.main:cli.  
  * Module entrypoint exists at engine/cli/\_\_main\_\_.py (from grep listing), and script wrapper scripts/hdctl.py dispatches to engine.cli.main.  
* Background/scheduled jobs relevant to evidence/indexing/posture  
  * scripts/bodygraph/run\_refresh\_worker.py:run\_refresh writes refresh state/policy/metrics/log snapshots under artifacts/bodygraph and artifacts/logs.  
  * scripts/db/run\_retention\_job.py:main runs retention via run\_bodygraph\_retention and writes artifacts/db/retention/retention\_run.log.

---

## Engine Modules

### 4.1 Sampler

* Module: engine/sampler/core.py  
* Primary symbols and roles  
  * build\_candidate\_pool: filters raw candidates by weight/eligibility into pool entries.  
  * \_is\_eligible: applies compat threshold, allowed/excluded bands, diversity key gating.  
  * rank\_candidates: deterministic sort via weight/score/band/id tie-breakers.  
  * sample\_and\_rank: wrapper build \+ rank flow.

### 4.2 Core compute (compat/parity/normalization)

* Module: engine/compat/compute.py  
  * compat\_public: normalizes AB/BA pair via normalize\_pair, computes category scores, returns categories+meta payload.  
  * Uses pair\_key and deterministic hash-based scoring \_score\_for.  
  * conjunction\_public\_resolved: resolves unresolved conjunction parties through local lookup and resolver, then calls conjunction payload builder.  
* Ordering/normalization source  
  * AB↔BA normalization is imported from engine.compat.ordering.normalize\_pair.

### 4.3 Determinism hazards inventory (engine sampled paths)

Observed in sampled engine paths:

* Current time usage  
  * engine/bodygraph/vendor\_client.py uses time.monotonic, time.strftime helpers for timing and UTC strings.  
* Network calls  
  * Vendor client constructs urllib.request.Request and performs HTTP fetch/retries.   
* File I/O  
  * Retry logging writes JSON lines to file path via \_append\_retry\_log.  
* No explicit unseeded RNG observed in sampled engine files  
  * In sampled modules (engine/sampler/core.py, engine/compat/compute.py, engine/runtime/determinism\_env.py), no random usage was observed.

---

## Adapter / HTTP Surfaces

### 5.1 Route registration map

* App/router creation  
  * Flask app factories: adapter/http\_reader.py:create\_app, adapter/wsgi.py:create\_app, adapter/factory.py:create\_app.  
* Blueprint mounting  
  * Reader blueprint bp mounted at root (url\_prefix="") in adapter/http\_reader.py and adapter/factory.py.  
  * Compat blueprint has internal url\_prefix="/api/compat/v1" and is registered via app. 

### 5.2 Surface classification

* Reader-like JSON success  
  * /reader GET/HEAD style behavior inside get\_reader\_bp emits reader bytes and ETag/cache headers.   
* Aux/narrative  
  * /api/aux/narrative and /aux/narrative emit narrative text/plain with conditional ETag behavior for unsuppressed output.   
* Admin/internal  
  * /internal/version, /internal/dev/sampler, /ops/writer/diagnostic, /ops/db/unavailable, /ops/rails/refusal, /ops/probe/env.  
  * Compat admin-like writer endpoint at /api/compat/v1 POST in engine/http/compat\_handler.py.  
* Dev/diagnostic harness  
  * /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction, APP\_ENV-gated through \_dev\_admin\_gate.

### 5.3 Transport semantics hooks

* HEAD vs GET parity  
  * Reader route handles HEAD branch explicitly and sets Content-Length to GET body length.   
  * /internal/version supports GET/HEAD and sets HEAD Content-Length to GET body size.   
* Conditional responses / 304  
  * Reader route checks If-None-Match; on strong ETag match returns 304 empty body and strips Content-Type/Content-Length.  
* ETag generation and quoting  
  * Reader ETag computed as quoted SHA-256 hex of response body bytes.   
  * Narrative unsuppressed branch sets quoted ETag from body digest.   
* Cache-control rules  
  * Reader success: private, max-age=0, must-revalidate.  
  * Writer/error surfaces: no-store and ETag removed.   
* Content-Type setting rules  
  * Writer response helper sets JSON content type; reader and internal routes also set JSON mimetypes explicitly. 

---

## Presenter / Emitter

* Engine canonical emitter  
  * engine/presenter/emitter.py:emit\_public delegates to canonical serializer for LF-terminated UTF-8 bytes; default sorted keys.   
  * Aliases include emit\_public\_with\_envelope and emit\_compact\_json.  
* Canonical serializer implementation  
  * engine/stable/sercanon.py:serialize uses json.dumps(..., separators=(",", ":"), sort\_keys=...), strips extra trailing newlines, appends exactly one LF, UTF-8 encodes.   
* Additional presenter path  
  * presenter/reader\_v1/emitter.py:emit\_reader\_v1 builds preimage, hashes it, appends idempotence\_hash, emits canonical bytes via engine emitter.   
* Callers  
  * HTTP adapter imports and uses engine.presenter.emitter.emit\_public.  
  * CLI imports engine.presenter.emitter and writes emitted output to stdout. 

---

## CLI Surfaces

* Entrypoint  
  * hdctl command configured in pyproject.toml to engine.cli.main:cli.  
* Parser / subcommand structure in engine/cli/main.py  
  * Subcommands include showcompat, aux-preview, bg:resolve, dev:sampler.  
  * showcompat arguments include \--pair-file, \--a-file, \--b-file, \--dump-reader, \--dump-admin-dir, \--source, \--conjunction, \--user-a/--user-b, birth tuple args.   
* Output surfaces  
  * Writes canonical payloads to stdout via \_emit\_stdout/sys.stdout.buffer.write and guards LF/CRLF errors.   
  * Optional file writes:  
    * reader bytes dump via \_dump\_reader\_bytes (--dump-reader).  
    * admin proof dumps via \_emit\_admin\_dumps and canon\_dump (--dump-admin-dir).  
* Exit behavior  
  * Missing usage/subcommand returns code 64; CliError prints token to stderr and returns err.exit\_code; unexpected exception returns 1\.

---

## Vendor Seam & BodyGraph Storage

### 8.1 Vendor client

* HTTP client module: engine/bodygraph/vendor\_client.py  
  * HdApiClient.from\_env reads HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, RELEASE\_ID; missing config raises VendorError(PROVIDER\_CONFIG\_MISSING).  
  * build\_request shapes POST body from birth tuple and sets vendor headers including API keys/user-agent.  
  * fetch performs POST, parses JSON, applies retry/backoff/error mapping. 

### 8.2 BodyGraph persistence/caching

* DB facade module: engine/db/adapter.py  
  * Provider selection order controlled by env flags and presence of DATABASE\_URL / DB\_BRIDGE\_URL; attempts snapshot written to artifacts/db\_bridge/adapter\_selection.snapshot.json.  
  * Fallback logic chooses psycopg then bridge unless forced.   
* Decision logic read cached vs vendor  
  * In conjunction resolver path, local lookup attempted first; after miss it calls resolver acquisition (resolve\_bodygraph).  
  * \_fetch\_db\_bodygraph in CLI reads latest DB payload from hde.body\_graphs\_current; not found raises BODYGRAPH\_NOT\_FOUND.

### 8.3 Offline posture / vendor-required posture

* Explicit gating found in resolver:  
  * If SAFE\_MODE true → returns PROVIDER\_REFUSED.  
  * If network not allowed → returns PROVIDER\_NETWORK\_BLOCKED.  
* Conjunction emission in adapter passes rails env (SAFE\_MODE,ALLOW\_NETWORK) into resolver call path. 

---

## Evidence, Indices, Catalogs

### 9.1 Evidence homes inventory

* docs/evidence/  
  * Contains INDEX.json, INDEX.sha256, path proofs, and evidence markdowns. (directory listing \+ files)  
* artifacts/  
  * Contains mirrors and generated artifacts across domains (cli/, registry/, math/, proofs/, ops/, db\_bridge/, etc.), including machine mirror artifacts/evidence\_index.jsonl.  
* audit/  
  * Contains manifests/close reports, QA logs (audit/qa/\*\*), gates (audit/gates/\*\*), doc deltas.  
* Generation posture in tooling  
  * update\_evidence\_index.py defines human index, hash sentinel, mirror paths and writes path proofs; imports determinism env gate helper. 

### 9.2 Evidence index structures

* docs/evidence/INDEX.json  
  * JSON list of artifact records (single-line compact in current file).  
* docs/evidence/INDEX.sha256  
  * Present in docs/evidence/ listing.  
* artifacts/evidence\_index.jsonl  
  * Present and used as machine mirror with structured per-line records (observed sample line from file head and mirror schema checker).  
* Tooling that reads/writes  
  * Writer/validator: tools/evidence/update\_evidence\_index.py (HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH).  
  * CI schema validation: ci/checks/check\_mirror\_schema.sh checks required keys, proof anchors, ordering, self-record behavior. 

### 9.3 Endpoint catalog

* Catalog file found: docs/ENDPOINTS\_CATALOG.json  
  * Schema shape includes top-level endpoints array with fields like path, method, classification, env\_gate, rails\_profile, a7\_eligible.  
* Referenced by tooling/tests  
  * QA close-pack tools reference docs/ENDPOINTS\_CATALOG.json and .sha256. (grep output)  
  * Dev conjunction routes in catalog correspond to actual handlers in adapter. 

### 9.4 Proof snapshot artifacts

* Snapshot-like artifacts present in artifacts/proofs/ and artifacts/cards/A7/\* per listing.  
* Producer evidence:  
  * tools/qa/generate\_epic027\_close\_pack.py references A7 success files success\_get.txt, success\_head.txt, success\_304.txt in generated close-pack evidence text. (grep output)  
  * tools/evidence/run\_canonical\_json\_gate.py writes gate logs and structured records under audit/gates/... and path proofs. 

---

## Tests, QA Harness, CI/Checks

### 10.1 Tests map

* Test roots (uncategorized by folder naming, with many thematic dirs):  
  * tests/adapter, tests/cli, tests/evidence, tests/ops, tests/qa, tests/transport, tests/invariance, etc. (directory listing).  
* Compat/reader endpoint tests  
  * tests/adapter/test\_compat\_http\_dev.py validates malformed JSON behavior and success payload shape for /api/compat/v1.  
* CLI output / canonical bytes tests  
  * tests/cli/test\_cli\_canonical\_bytes.py runs scripts/hdctl.py showcompat, asserts LF/canonical bytes, checks dump/admin artifacts.  
* Evidence index/cat tests  
  * tests/ops/test\_evidence\_index.py checks required artifact key/path presence in docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl, plus proof sidecars. 

### 10.2 CI workflows

* Workflow file: .github/workflows/ci.yml  
* Key jobs/checks  
  * test job: env pins, CLI guards, canonical JSON gate, evidence index update/check, mirror schema check, pytest suites.   
  * epic020 job: EPIC020 determinism/CLI/transport/QA tests.   
  * sanity-pipeline job runs python tools/evidence/run\_sanity\_pipeline.py.

### 10.3 Script/check inventory (QA-relevant examples)

* ci/checks/check\_env\_pins.sh: invokes deterministic env checker and validates pinned rails log.   
* ci/checks/check\_mirror\_schema.sh: validates evidence mirror schema/order/proof consistency.   
* ci/checks/check\_release\_identity.sh: validates freeze-pack/release-id identity constraints and required evidence files.   
* tools/evidence/run\_sanity\_pipeline.py: executes ordered closed-rails checks and writes artifacts/sanity/sanity.log. 

---

## Flows & Call Chains

### Flow 1 — Reader success flow (HTTP)

Call chain:  
adapter/http\_reader.py:get\_reader\_bp.reader\_v1 → engine.runtime.emit\_reader\_public\_bytes → engine.runtime.public.emit\_reader\_public\_envelope → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine.presenter.emitter.emit\_public

* Route validates query/version and APP\_ENV gating before compute.   
* Loads chart files and TZ requirements from request inputs.   
* Emits canonical reader bytes, computes ETag, handles 304/HEAD/200 branches.   
* Runtime path computes band via ts\_v0 and constructs reader envelope.   
* Presenter layer adds idempotence hash and canonical serialization. 

### Flow 2 — Compat API flow (HTTP)

Call chain:  
engine/http/compat\_handler.py:post\_json → engine.compat.compute.compat\_public → engine.presenter.emit\_public

* Endpoint mounted at /api/compat/v1 blueprint prefix.   
* POST parses payload (a,b or ids), validates viewer prefs, computes compat payload.   
* Response built with no-store writer transport and no ETag. 

### Flow 3 — CLI showcompat / preview flow

Call chain:  
engine/cli/main.py:cli → showcompat → compat\_public / conjunction\_public\_resolved → engine.presenter.emitter.emit\_public → stdout (+ optional dumps)

* Parser binds showcompat to handler and includes file/user/source args.   
* showcompat resolves inputs (files/stdin/db/vendor/conjunction modes).   
* Emits stdout with LF/CRLF guards and optionally writes \--dump-reader and \--dump-admin-dir artifacts. 

### Flow 4 — Vendor acquisition / BodyGraph ingest flow

Call chain:  
engine.bodygraph.resolver.resolve\_bodygraph(source=vendor) → \_resolve\_vendor → ingest\_vendor\_bodygraph (from ingest module) → engine.bodygraph.vendor\_client.HdApiClient.fetch

* Resolver applies rails checks: SAFE\_MODE refusal and network block cases.   
* On open rails, resolves inputs and invokes ingest with normalized user id.   
* Vendor client fetch path performs HTTPS POST, retry handling, JSON decode, typed errors. 

### Flow 5 — Evidence index update/validation flow

Call chain:  
tools/evidence/update\_evidence\_index.py (write/check) → docs/evidence/INDEX.json \+ docs/evidence/INDEX.sha256 \+ artifacts/evidence\_index.jsonl → tools/evidence/orientation\_demo.py \--check → ci/checks/check\_mirror\_schema.sh

* update\_evidence\_index.py defines these artifacts as managed outputs and imports determinism env gate helper.   
* Orientation demo loads INDEX \+ mirror and validates coherence against proofs; \--check errors on mismatch/drift.   
* CI executes update/check/orientation/mirror schema checks in pipeline order. 

---

## Drift and Reality vs Expectations

### 12.1 Drift categories

#### Directory/architecture drift

* Observed: Both presenter/ (top-level) and engine/presenter/ exist and are active in call paths.  
  Proof: top-level presenter emitter imports engine emitter; runtime imports top-level presenter emitter.   
  Impact (factual): This creates two presenter namespaces in the codebase.

#### Surface drift

* Observed: Reader route is /reader (and compat /api/compat/v1), with additional dev conjunction routes and internal/ops routes in same adapter module.  
  Proof: Route decorators in adapter/http\_reader.py and compat blueprint prefix.   
  Impact (factual): Surface inventory spans reader \+ dev harness \+ ops/internal in one adapter module.

#### Evidence drift

* Observed: Governed artifacts are distributed across docs/evidence, artifacts/\*\*, and audit/\*\* with mirrored/paired index artifacts.  
  Proof: evidence index paths in tooling and listings.   
  Impact (factual): Evidence material is multi-home and requires index/mirror linkage to correlate.

#### Determinism drift

* Observed: Engine includes deterministic env pin enforcement, but sampled vendor/worker modules still use time/network/file I/O primitives.  
  Proof: env pins helper and vendor client/time/file/network usage.   
  Impact (factual): Determinism posture depends on rails and call-site gating, not pure compute everywhere.

#### Vendor seam drift

* Observed: Vendor seam appears under engine/bodygraph/vendor\_client.py and is invoked from resolver/compute/CLI paths rather than isolated adapter-only boundary.  
  Proof: imports/calls from compat compute and resolver to vendor-related symbols.   
  Impact (factual): Vendor access concerns are present in multiple engine subpackages.

#### Path-case drift

* Observed: Mixed epic filename patterns in audit/ (EPIC017\_\* and EPIC-0xx\_\*).  
  Proof: top-level audit listing includes both forms (command output showed both EPIC017\_\* and EPIC-023\_\*/EPIC-027\_\*).  
  Impact (factual): Naming pattern is non-uniform across audit artifacts.

#### Root proliferation

* Observed: Multiple roots contain architecture/governance/evidence-relevant material (audit, artifacts, docs, tools, scripts, ci, plus root-level reports).  
  Impact (factual): Repository truth surfaces are distributed across multiple top-level homes.

### 12.2 Alignment summary table

| Expectation area | Status | Anchor |
| :---- | :---- | :---- |
| Engine/adapter/presenter split exists | Partial | engine/, adapter/, presenter/ all present; plus engine/presenter/ in parallel. |
| Single emitter path | Partial | Canonical emitter in engine/presenter/emitter.py, but top-level presenter emitter wraps/uses it for reader envelope flow. |
| Vendor seam outside engine core compute | Partial | Vendor client in engine/bodygraph; compat compute imports resolver/vendor error paths.  |
| Evidence layout indexed/mirrored | Aligned (as implemented) | update\_evidence\_index.py manages docs/evidence/INDEX.json, INDEX.sha256, artifacts/evidence\_index.jsonl. |

---

## Negative-Claim Proof Appendix

1. Claim: setup.py not found.  
   * What searched: setup.py  
   * Method: find . \-name 'setup.py' | wc \-l  
   * Scope: repo root (.)  
   * Result: 0 hits  
2. Claim: setup.cfg not found.  
   * What searched: setup.cfg  
   * Method: find . \-name 'setup.cfg' | wc \-l  
   * Scope: repo root (.)  
   * Result: 0 hits  
3. Claim: No FastAPI/APIRouter framework usage in audited HTTP startup paths (adapter, engine, run\_flask.py).  
   * What searched: APIRouter|FastAPI  
   * Method: rg \-n "APIRouter|FastAPI" adapter engine run\_flask.py | wc \-l  
   * Scope: adapter/, engine/, run\_flask.py  
   * Result: 0 hits  
4. Claim: No monorepo JS workspace config files observed in shallow root scan.  
   * What searched: pnpm-workspace.yaml, turbo.json, package.json (maxdepth 2\)  
   * Method: find . \-maxdepth 2 \\( \-name 'pnpm-workspace.yaml' \-o \-name 'turbo.json' \-o \-name 'package.json' \\)  
   * Scope: repo root up to depth 2  
   * Result: no paths returned (0 hits)

---

### Commands used (audit evidence trail)

* Metadata/state: pwd, git rev-parse \--show-toplevel, git rev-parse HEAD, git rev-parse \--abbrev-ref HEAD, git status \--porcelain, date \-u, uname \-srmo, python3 \--version, node \--version.  
* Structure scans: find . \-maxdepth 1 ..., find engine|adapter|..., find tests \-maxdepth 2 \-type d.  
* Symbol/location scans: multiple rg \-n queries for routes, CLI, evidence, determinism, vendor, and endpoint catalog references.  
* Source inspection: nl \-ba \<file\> | sed \-n ... across adapter/engine/presenter/tools/ci/tests files.  
* Negative-claim proofs: find ... | wc \-l, rg ... | wc \-l, shallow find for workspace config names.

