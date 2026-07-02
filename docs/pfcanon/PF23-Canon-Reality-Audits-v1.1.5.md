# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.5

**Status:** Canon

**Effective date:** 2026-06-29

**Last Update Gate:** HDE-EPIC035

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

**Date:** 2026-06-29

## Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2; confirmed by pwd and git rev-parse \--show-toplevel both returning /workspace/glow-hdengine-v2.  
* Commit: 64dbb7c0387c945c16581ddec2816f0c94d9160b (git rev-parse HEAD).  
* Working tree cleanliness: clean; git status \--porcelain produced no output.  
* Branch: work (git rev-parse \--abbrev-ref HEAD).  
* Timestamp UTC: 2026-06-29T14:51:09Z (date \-u \+%Y-%m-%dT%H:%M:%SZ).  
* Execution environment:  
  * OS/kernel: Linux 15d1d2210d08 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 ...  
  * Python: Python 3.14.4  
  * Node: v24.15.0

Scope/posture used for this audit: read-only static inspection; no code execution, package installation, tests, refactors, or file edits.  
---

## Top-level Repo Map

Top-level listing proof: repo root contains adapter, artifacts, audit, ci, docs, engine, presenter, pyproject.toml, requirements-dev.txt, requirements.txt, run\_flask.py, scripts, tests, and tools in the find . \-maxdepth 1 output.

### Expected HD Engine families

* engine/ — Present.  
  * Contains core engine packages for bodygraph, compat, sampler, DB, provider, runtime, serializer, CLI, and presenter.  
  * Anchor listing: engine/compat/compute.py, engine/sampler/core.py, engine/bodygraph/vendor\_client.py, engine/db/adapter.py, engine/cli/main.py.  
  * Excerpt: engine/compat/compute.py:36-48 defines compat\_public(...) and returns {"categories": cats, "meta": ...}.  
* adapter/ — Present.  
  * Contains Flask app factories, WSGI wiring, HTTP reader routes, cache/ETag helpers, DB access, env guards.  
  * Anchor listing: adapter/factory.py, adapter/http\_reader.py, adapter/wsgi.py.  
  * Excerpt: adapter/wsgi.py:16-29 creates Flask(\_\_name\_\_), installs logging/env guards, and registers reader\_bp plus compat\_blueprint.  
* presenter/ — Present.  
  * Top-level presenter package exists alongside engine-local presenter.  
  * Anchor listing: presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py, plus engine/presenter/emitter.py.  
  * Excerpt: presenter/reader\_v1/emitter.py:54-65 defines emit\_reader\_v1(...) and returns canonical public bytes plus final envelope.  
* CLI package location(s) — Present.  
  * Primary installed console script points to engine.cli.main:cli.  
  * Anchor: pyproject.toml:\[project.scripts\] hdctl \= "engine.cli.main:cli".  
  * Additional script wrappers/backups are listed under scripts/hdctl.py, scripts/hdctl.clean.py, scripts/hdctl.backup.py.  
* docs/ — Present.  
  * Contains acceptance maps, endpoint catalog, evidence index, PF canon, architecture/contracts/ops docs.  
  * Anchors: docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, docs/ENDPOINTS\_CATALOG.json, docs/pfcanon/.  
* artifacts/ — Present.  
  * Contains generated/log-like evidence families, snapshots, path proofs, CLI captures, vendor and DB bridge artifacts.  
  * Anchors: artifacts/evidence\_index.jsonl, artifacts/vendor/hdapi\_v2/, artifacts/db\_bridge/provider\_parity.proof.json, artifacts/proofs/success\_get.txt.path\_proof.txt.  
* audit/ — Present.  
  * Contains close reports, manifests, QA evidence by epic, gates, ops evidence, doc deltas.  
  * Anchors: audit/qa/hde-epic035/, audit/gates/json\_gate/, audit/EPIC-024\_MANIFEST.json.  
* tools/ — Present.  
  * Contains evidence, QA, CLI, config, and generator scripts.  
  * Anchor: tools/evidence/update\_evidence\_index.py:23-27 defines canonical index/mirror paths.  
* ci/ and .github/ — Present.  
  * CI checks and workflow files exist.  
  * Anchors: .github/workflows/ci.yml, ci/checks/check\_mirror\_schema.sh, ci/jobs/rails\_closed\_refusal.yml.  
* tests/ — Present.  
  * Broad pytest suite roots for adapter, bodygraph, CLI, compat, DB, evidence, HTTP, serializer, sampler, etc.  
  * Anchors from listing: tests/adapter/test\_compat\_http\_dev.py, tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/evidence/test\_sanity\_pipeline.py.  
* scripts/ — Present.  
  * Operational and legacy/utility scripts, including CLI wrappers and ingest/probe scripts.  
  * Anchors from search/listing: scripts/ingest/run\_vendor\_ingest.py, scripts/hdapi\_cli.py, scripts/probe\_internal\_version.py.

### Root discipline capture: governed/truth-home-looking roots observed

Observed top-level roots that hold docs, generated artifacts, audit outputs, tools, scripts, schemas, or validation material:

* audit/  
* artifacts/  
* docs/  
* tools/  
* scripts/  
* catalog/  
* schemas/  
* config/  
* fixtures/  
* goldens/  
* reports/  
* scan\_reports/  
* validation/  
* proofs/  
* math/  
* release/  
* freeze/  
* migrations/  
* .github/  
* ci/

---

## Packaging and Entrypoints

### Packaging / build configuration

* pyproject.toml  
  * Declares Python package metadata: name \= "glow-hdengine", version \= "0.0.0", requires-python \= "\>=3.10".  
  * Declares console script: hdctl \= "engine.cli.main:cli".  
  * Declares package discovery includes: \["engine\*", "adapter\*", "presenter\*"\].  
  * Proof: pyproject.toml:1-15.  
* requirements.txt, requirements-dev.txt  
  * Present at repo root per PKG listing.  
  * The audit did not expand dependency contents because the requested focus is architecture wiring and no install/test execution was allowed.  
* Workspace/monorepo manager config  
  * No package manager workspace file was identified in the packaging scan output. Negative proof in appendix.

### Entrypoint inventory

* HTTP server startup: adapter/wsgi.py:create\_app  
  * Role: creates Flask app, installs logging/env guards, registers reader and compat blueprints, adds health/ready routes and error handlers.  
  * Proof: adapter/wsgi.py:16-29, adapter/wsgi.py:45-55, adapter/wsgi.py:57-73.  
* HTTP alternate startup: adapter/factory.py:create\_app  
  * Role: creates Flask app and registers adapter.http\_reader.bp at root.  
  * Proof: adapter/factory.py:4-7.  
* Flask dev runner: run\_flask.py  
  * Role: imports adapter.factory:create\_app, sets dev defaults, and calls app.run(...).  
  * Proof: run\_flask.py:97-130.  
* CLI console script: engine.cli.main:cli  
  * Role: argparse-based hdctl entrypoint; dispatches subcommands.  
  * Proof: pyproject.toml:\[project.scripts\], engine/cli/main.py:73-191, engine/cli/main.py:239-260.  
* Evidence/indexing job entrypoint: tools/evidence/update\_evidence\_index.py:main  
  * Role: updates/checks docs evidence index, hash sentinel, and machine mirror.  
  * Proof: tools/evidence/update\_evidence\_index.py:23-27 defines HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH, and MIRROR\_SHA\_PATH.

---

## Engine Modules

### Sampler

* engine/sampler/core.py  
  * ViewerProfile: dataclass for viewer state; proof engine/sampler/core.py:30-36.  
  * CandidateFeatures: normalized candidate input; proof engine/sampler/core.py:38-49.  
  * SamplerConfig: sampler knobs; proof engine/sampler/core.py:51-60.  
  * build\_candidate\_pool(...): filters zero-weight/ineligible candidates into a pool; proof engine/sampler/core.py:126-151.  
  * rank\_candidates(...): deterministic sort/rank of candidates; proof engine/sampler/core.py:170-193.  
  * sample\_and\_rank(...): helper chaining pool build then rank; proof engine/sampler/core.py:196-204.  
  * Code comment states “No randomness, clocks, or external state are consulted”; proof engine/sampler/core.py:170-176.

### Core compute / compatibility

* engine/compat/compute.py  
  * band\_for(score): maps score thresholds to band labels; proof engine/compat/compute.py:17-21.  
  * \_score\_for(cat, pair\_k, weights): derives stable score from sha256(f"{pair\_k}:{cat}"); proof engine/compat/compute.py:23-30.  
  * compat\_public(...): normalizes AB/BA, computes category scores/bands/keys, returns categories/meta; proof engine/compat/compute.py:36-48.  
  * conjunction\_public(...): builds deterministic conjunction contract payload; proof engine/compat/compute.py:69-98.  
  * conjunction\_public\_resolved(...): local lookup first, then resolver acquisition when rails allow; proof engine/compat/compute.py:141-160, engine/compat/compute.py:172-217.  
* AB↔BA parity / symmetry  
  * compat\_public calls normalize\_pair(a,b) before pair\_key; proof engine/compat/compute.py:39-41.  
  * conjunction\_public also normalizes left/right before computing compat; proof engine/compat/compute.py:80-83.

### Determinism hazards inventory

Observed in sampled engine paths:

* Current time / process time  
  * engine/bodygraph/vendor\_client.py:133-139 defines \_now\_ms() using time.monotonic() and \_utc\_iso() using time.gmtime(...).  
  * engine/bodygraph/ingest.py:131-140 records start \= time.monotonic() and computes duration\_ms.  
  * engine/bodygraph/ingest.py:72-73 builds UTC timestamp from time.gmtime().  
* Network calls  
  * engine/bodygraph/vendor\_client.py:442-444 builds urlrequest.Request(... method="POST") and calls self.\_request(req, timeout).  
  * engine/bodygraph/ingest.py:132-134 constructs HdApiClient.from\_env(...), builds request, and calls client.fetch(request).  
* File I/O  
  * engine/bodygraph/vendor\_client.py:205-214 appends retry logs to a Path.  
  * engine/bodygraph/ingest.py:62-69 writes JSONL log records.  
  * engine/db/adapter.py:80-85 writes adapter-selection snapshot text.  
* Randomness without explicit seeding  
  * No randomness call was observed in sampled core paths engine/sampler/core.py and engine/compat/compute.py; sampler comment explicitly says no randomness/clocks/external state at engine/sampler/core.py:170-176.

---

## Adapter / HTTP Surfaces

### Route registration map

* App creation: adapter/wsgi.py:create\_app  
  * Registers:  
    * reader\_bp from adapter.http\_reader  
    * compat\_blueprint from engine.http.compat\_handler  
  * Proof: adapter/wsgi.py:10-11, adapter/wsgi.py:16-29.  
* Alternate app creation: adapter/factory.py:create\_app  
  * Registers adapter.http\_reader.bp at url\_prefix="".  
  * Proof: adapter/factory.py:4-7.  
* Compat blueprint  
  * Base prefix: /api/compat/v1.  
  * Defined in engine/http/compat\_handler.py.  
  * Proof: engine/http/compat\_handler.py:11 has Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
  * Handlers:  
    * \_compat\_writer\_transport\_guard  
    * get\_ids\_only  
    * post\_json  
    * post\_json\_head  
    * post\_json\_options  
  * Proof: engine/http/compat\_handler.py:68-76, 82-88, 90-127, 130-137.  
* Reader/dev/internal blueprint  
  * Defined in adapter/http\_reader.py.  
  * Routes found:  
    * /reader GET and POST; proof adapter/http\_reader.py:330-331, 441-442.  
    * /api/aux/narrative and /aux/narrative; proof adapter/http\_reader.py:392-393.  
    * /ops/db/unavailable; proof adapter/http\_reader.py:469.  
    * /ops/rails/refusal; proof adapter/http\_reader.py:514.  
    * /ops/probe/env; proof adapter/http\_reader.py:522.  
    * /internal/dev/sampler; proof adapter/http\_reader.py:698.  
    * /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction; proof adapter/http\_reader.py:766-782.  
    * /internal/version; proof adapter/http\_reader.py:874-875.  
    * /ops/writer/diagnostic; proof adapter/http\_reader.py:898, 916, 928\.

### Surface classification

* Reader-like JSON success  
  * /reader in adapter/http\_reader.py; endpoint catalog classifies it as “Reader success route (dev-only)”.  
  * Proof: docs/ENDPOINTS\_CATALOG.json:1 includes path "/reader", classification "dev\_harness", description "Reader success route (dev-only)".  
* Compat API  
  * /api/compat/v1 in engine/http/compat\_handler.py.  
  * Proof: docs/ENDPOINTS\_CATALOG.json:1 classifies it as "internal\_admin" with description "Compat pair endpoint (internal admin)".  
  * Handler calls compat\_public(...); proof engine/http/compat\_handler.py:121-127.  
* Aux/narrative  
  * /api/aux/narrative and /aux/narrative in adapter/http\_reader.py.  
  * Proof: route decorators at adapter/http\_reader.py:392-393; imports emit\_public\_aux, get\_pack at adapter/http\_reader.py:10.  
* Admin/internal  
  * /internal/healthz, /internal/readyz in adapter/wsgi.py.  
  * Proof: adapter/wsgi.py:45-55.  
  * /internal/version in adapter/http\_reader.py.  
  * Proof: adapter/http\_reader.py:874-875.  
* Dev/diagnostic harness  
  * /internal/dev/sampler and /dev/\*/conjunction routes in adapter/http\_reader.py.  
  * Proof: adapter/http\_reader.py:698, 766-782.  
  * Dev gate: \_dev\_admin\_gate allows only dev, test, local; proof adapter/http\_reader.py:541-547.

### Transport semantics hooks

* HEAD vs GET / method handling  
  * Compat route has explicit HEAD response returning 405 and Allow: POST, OPTIONS; proof engine/http/compat\_handler.py:32-40, 68-76, 130-132.  
  * /internal/version supports GET and HEAD; proof adapter/http\_reader.py:874-875.  
* Conditional responses / 304  
  * adapter/http\_reader.py:188-195 parses If-None-Match tokens.  
  * Proof of 304 artifacts exists under artifacts/proofs/success\_304.txt.path\_proof.txt from evidence listing.  
* ETag behavior  
  * Internal routes strip ETag in adapter/factory.py:7-10.  
  * Writer responses remove ETag in adapter/http\_reader.py:78-80 and engine/http/compat\_handler.py:17-19.  
  * WSGI common headers include no-store defaults; proof adapter/wsgi.py:31-43.  
* Cache-Control  
  * Reader 200 headers set private, max-age=0, must-revalidate; proof adapter/http\_reader.py:28-32.  
  * Writer responses set no-store; proof adapter/http\_reader.py:76-79, engine/http/compat\_handler.py:16-18.  
* Content-Type  
  * Writer/reader responses use application/json; charset=utf-8; proof adapter/http\_reader.py:76-77, adapter/http\_reader.py:28-29, engine/http/compat\_handler.py:16.

---

## Presenter / Emitter

* engine/serializer/canon.py:sercanon  
  * Canonical JSON serializer wrapper.  
  * Proof: docstring says UTF-8 bytes, ensure\_ascii=False, sorted keys by default, compact separators, exactly one trailing newline at engine/serializer/canon.py:6-15.  
* engine/presenter/emitter.py:emit\_public  
  * Governed public JSON byte emitter delegating to canonical serializer.  
  * Proof: engine/presenter/emitter.py:6-13.  
  * Used by HTTP compat: engine/http/compat\_handler.py:5, 14-21.  
  * Used by adapter reader/writer: adapter/http\_reader.py:7, 68-86.  
  * Used by CLI: engine/cli/main.py:35, 234-235.  
* presenter/reader\_v1/emitter.py:emit\_reader\_v1  
  * Reader v1 envelope emitter that dedupes/sorts categories and computes idempotence\_hash.  
  * Proof: presenter/reader\_v1/emitter.py:9-31, 54-65.  
  * It imports engine.presenter.emitter; proof presenter/reader\_v1/emitter.py:5.  
* Multiple emitter locations observed  
  * Engine-local canonical emitter: engine/presenter/emitter.py.  
  * Top-level reader-v1 emitter: presenter/reader\_v1/emitter.py.  
  * Serializer layer: engine/serializer/canon.py.  
  * These are distinct by usage: serializer emits canonical bytes, engine presenter wraps public envelopes, reader\_v1 builds reader-specific envelope/hash.

---

## CLI Surfaces

### Installed console script

* Command: hdctl  
* Entrypoint: engine.cli.main:cli  
* Proof: pyproject.toml:\[project.scripts\] hdctl \= "engine.cli.main:cli".

### Argparse command inventory

* hdctl showcompat  
  * Defined at engine/cli/main.py:85-131.  
  * Arguments include \--pair-file, \--a-file, \--b-file, aliases \--a, \--b, \--dump-reader, \--dump-admin-dir, \--source {db,vendor,auto}, \--conjunction, \--viewer-prefs-file, \--user-a, \--user-b, birth tuple fields.  
  * Handler: show.set\_defaults(handler=showcompat) at engine/cli/main.py:131.  
  * Output: CLI writes to stdout in handlers such as bg\_resolve with sys.stdout.write(output) at engine/cli/main.py:234-235; showcompat output paths are evidenced by parser args \--dump-reader and \--dump-admin-dir at engine/cli/main.py:95-104.  
* hdctl aux-preview  
  * Defined at engine/cli/main.py:133-144.  
  * Arguments: \--category, \--band, \--perspective, \--pair-file, \--show-narrative, \--admin-out.  
  * Handler: aux.set\_defaults(handler=aux\_preview) at engine/cli/main.py:144.  
* hdctl bg:resolve  
  * Defined at engine/cli/main.py:145-171.  
  * Required argument: \--user; proof engine/cli/main.py:150.  
  * Source choices: auto, db, vendor; proof engine/cli/main.py:152-155.  
  * Vendor source requires full birth tuple; proof engine/cli/main.py:218-224.  
  * Calls resolve\_bodygraph(...); proof engine/cli/main.py:224-233.  
  * Emits canonical payload to stdout; proof engine/cli/main.py:234-235.  
* hdctl dev:sampler  
  * Defined at engine/cli/main.py:173-190.  
  * Required args: \--viewer, \--candidates-file; proof engine/cli/main.py:178-183.  
  * Optional \--seed is “echoed only”; proof engine/cli/main.py:184-188.  
  * Handler: dev\_sampler.set\_defaults(handler=dev\_sampler\_run) at engine/cli/main.py:190.

### CLI errors / exit

* Missing/invalid argparse usage maps SystemExit to return 64 when parser exits nonzero; proof engine/cli/main.py:248-253.  
* CliError carries an exit\_code, default 64; proof engine/cli/main.py:55-61.

---

## Vendor Seam & BodyGraph Storage

### Vendor client

* engine/bodygraph/vendor\_client.py:HdApiClient  
  * HTTP client with pinned retry/backoff and typed error mapping.  
  * Proof: class docstring at engine/bodygraph/vendor\_client.py:222-223.  
  * Env inputs:  
    * HD\_API\_BASE\_URL / compatibility alias HDAPI\_BASE\_URL; proof engine/bodygraph/vendor\_client.py:141-146, 275-279.  
    * HD\_API\_KEY; proof engine/bodygraph/vendor\_client.py:277-285.  
    * GEO\_API\_KEY; proof engine/bodygraph/vendor\_client.py:278, 411-418.  
    * RELEASE\_ID; proof engine/bodygraph/vendor\_client.py:288-292.  
  * Request shaping:  
    * Route contracts for bodygraphs, bodygraphs/simple, charts, charts/simple, charts/coordinates; proof engine/bodygraph/vendor\_client.py:88-94.  
    * build\_contract\_route\_request(...) validates fields and builds canonical JSON body; proof engine/bodygraph/vendor\_client.py:317-425.  
  * HTTP call:  
    * fetch(...) creates a POST urlrequest.Request and calls configured request function; proof engine/bodygraph/vendor\_client.py:427-459.

### BodyGraph persistence/caching

* DB access façade: engine/db/adapter.py:DBAccess  
  * Protocol supports health, query, exec, tx, introspect; proof engine/db/adapter.py:35-53.  
  * Provider selection uses DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD; proof engine/db/adapter.py:138-165.  
  * Writes adapter-selection snapshot by default to artifacts/db\_bridge/adapter\_selection.snapshot.json; proof engine/db/adapter.py:127-132.  
* BodyGraph ingest persistence: engine/bodygraph/ingest.py  
  * Uses DBAccess and Statement; proof engine/bodygraph/ingest.py:12.  
  * Persistence target is hde.body\_graphs; proof SQL insert at engine/bodygraph/ingest.py:214-220.  
  * Idempotency/fingerprint fields include vendor, vendor\_version, input\_fingerprint; proof engine/bodygraph/ingest.py:138, 167-171, 214-220.

### Offline / vendor gating posture

* engine/bodygraph/resolver.py:\_resolve\_vendor refuses vendor when SAFE\_MODE is closed and when network is not allowed.  
  * SAFE\_MODE refusal: PROVIDER\_REFUSED; proof engine/bodygraph/resolver.py:105-117.  
  * Network disabled: PROVIDER\_NETWORK\_BLOCKED; proof engine/bodygraph/resolver.py:118-127.  
* engine/bodygraph/ingest.py:124-130 also enforces SAFE\_MODE and ALLOW\_NETWORK, raising PROVIDER\_REFUSED or PROVIDER\_NETWORK\_BLOCKED.

---

## Evidence, Indices, Catalogs

### Evidence homes inventory

* docs/evidence/  
  * Contains human evidence index and hash sentinel.  
  * Proof: tools/evidence/update\_evidence\_index.py:23-26 names docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
* artifacts/  
  * Contains machine mirror, snapshots, proof files, CLI captures, DB/vendor/runtime evidence.  
  * Proof: tools/evidence/update\_evidence\_index.py:26-28 names artifacts/evidence\_index.jsonl and .sha256.  
  * Listing includes many .path\_proof.txt files such as artifacts/vendor/policies\_pinned.md.path\_proof.txt and artifacts/proofs/success\_get.txt.path\_proof.txt.  
* audit/  
  * Contains manifests, close reports, QA evidence, gates, ops, doc deltas.  
  * Proof: tools/evidence/update\_evidence\_index.py:52-68 indexes audit/EPIC-022\_close\_report.md, audit/EPIC-022\_MANIFEST.json, audit/qa/hde-epic022/token\_evidence\_matrix.md, and docs/acceptance\_map\_epic022.json.  
* audit/qa/\*\*  
  * Per-epic QA roots are present from listing: audit/qa/hde-epic017 through audit/qa/hde-epic035.  
* audit/gates/\*\*  
  * Gate evidence roots are present: audit/gates/json\_gate, audit/gates/canonical\_json, audit/gates/evidence\_index\_snapshot, etc.

Based on file patterns (\*.path\_proof.txt, \*.snapshot.json, logs, manifests, acceptance maps), the evidence homes are mixed generated/governed artifact storage and hand-authored documentation.

### Evidence index structures

* docs/evidence/INDEX.json  
  * Human evidence index path defined in tooling.  
  * Proof: tools/evidence/update\_evidence\_index.py:23-25.  
* docs/evidence/INDEX.sha256  
  * Hash sentinel path defined in tooling.  
  * Proof: tools/evidence/update\_evidence\_index.py:24-26.  
* artifacts/evidence\_index.jsonl  
  * Machine mirror path defined in tooling.  
  * Proof: tools/evidence/update\_evidence\_index.py:26-28.  
* Tooling that regenerates/validates  
  * tools/evidence/update\_evidence\_index.py describes hardening the index/hash/mirror.  
  * Proof: module docstring at tools/evidence/update\_evidence\_index.py:1-12.

### Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * Shape: top-level object with endpoints array and success\_endpoints array.  
  * Proof: docs/ENDPOINTS\_CATALOG.json:1.  
  * Routes listed include /api/compat/v1, /dev/reader/conjunction, /dev/writer/conjunction, /dev/sampler/conjunction, /internal/version, /reader.  
  * Referenced by tests: listing includes tests/http/test\_endpoint\_catalog.py.

### Proof / snapshot artifacts

Examples observed in listing:

* artifacts/proofs/success\_get.txt.path\_proof.txt  
* artifacts/proofs/success\_head.txt.path\_proof.txt  
* artifacts/proofs/success\_304.txt.path\_proof.txt  
* artifacts/bodygraph/metrics.snapshot.json  
* artifacts/bodygraph/refresh\_policy.snapshot.json  
* artifacts/db\_bridge/adapter\_selection.snapshot.json  
* artifacts/vendor/hdapi\_v2/\*  
* artifacts/runtime/env\_connectivity.snapshot.json

Producer evidence examples:

* engine/db/adapter.py:127-132 defaults DB adapter snapshot path to artifacts/db\_bridge/adapter\_selection.snapshot.json.  
* tools/evidence/update\_evidence\_index.py:35-75 includes baseline/epic artifact records for registry, sanity, close reports, manifests, token matrices, and acceptance maps.

---

## Tests, QA Harness, CI/Checks

### Tests map

Test roots are organized by domain, not explicitly by unit/integration labels in the listing. Observed loci:

* Adapter / HTTP  
  * tests/adapter/test\_compat\_http\_dev.py, tests/adapter/test\_reader\_parity.py, tests/http/test\_compat\_endpoint\_contract.py, tests/http/test\_reader\_a7\_transport.py.  
  * Role from filenames: compat/reader HTTP behavior and transport contract tests.  
* CLI  
  * tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/cli/test\_cli\_canonical\_bytes.py, tests/hdctl/test\_cli\_streams\_and\_exits.py.  
  * Role from filenames: showcompat parity, canonical bytes, streams/exits.  
* Canonical JSON / bytes  
  * tests/infra/test\_sercanon\_bytes.py, tests/infra/test\_serializer\_guard.py, tests/compat/test\_compat\_public\_lf\_bom.py.  
  * Role from filenames: serializer/canonical byte discipline and LF/BOM checks.  
* Determinism  
  * tests/core/test\_engine\_core\_determinism.py, tests/config/test\_registry\_report\_determinism.py, tests/compat/test\_abba\_parity.py.  
  * Role from filenames: engine determinism, registry report determinism, AB/BA parity.  
* Evidence index / catalogs  
  * tests/evidence/test\_sanity\_evidence\_index.py, tests/evidence/test\_evidence\_index\_snapshot.py, tests/evidence/test\_machine\_mirror\_self\_proof.py, tests/http/test\_endpoint\_catalog.py.  
  * Role from filenames: evidence index, snapshot, mirror proof, endpoint catalog.  
* Vendor/network fixtures  
  * tests/bodygraph/test\_vendor\_client.py, tests/bodygraph/test\_ingest.py, tests/bodygraph/test\_resolver\_vendor.py, tests/evidence/test\_hdapi\_v2\_live\_conformance.py.  
  * Role from filenames: vendor client, ingest, resolver, live conformance evidence paths.

### CI workflows

* .github/workflows/ci.yml  
  * Present in CI listing.  
* ci/checks/\*\*  
  * Present checks:  
    * ci/checks/check\_env\_pins.sh  
    * ci/checks/check\_evidence\_index\_hash.sh  
    * ci/checks/check\_mirror\_schema.sh  
    * ci/checks/check\_release\_identity.sh  
    * ci/checks/check\_final\_lf.sh  
    * ci/checks/check\_cli\_help.sh  
    * ci/checks/check\_bridge\_consistency.py  
* ci/jobs/\*\*  
  * Present jobs:  
    * ci/jobs/rails\_closed\_refusal.yml  
    * ci/jobs/rails\_open\_conformance.yml  
    * ci/jobs/logs\_keys\_only\_redaction.yml

### Script/check inventory

Representative QA/evidence scripts observed:

* tools/evidence/update\_evidence\_index.py — index/hash/mirror hardening; proof docstring tools/evidence/update\_evidence\_index.py:1-12.  
* tools/evidence/check\_lf\_endings.py — LF-ending check script; present in CLI search output with def main.  
* tools/evidence/orientation\_demo.py — orientation demo generator/check; present in CLI search output with def main.  
* tools/evidence/generate\_sampler\_evidence.py — sampler evidence generator; proof search output shows parser description “Generate sampler evidence artifacts”.  
* tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py — HDAPI v2 contract inventory generator; proof search output shows argparse description “Generate HDE-EPIC033 HDAPI v2 contract-inventory evidence”.  
* scripts/ingest/run\_vendor\_ingest.py — vendor ingest runner; present in CLI search output with def main.  
* scripts/probe\_internal\_version.py — internal version probe; search output shows argparse with \--base-url and \--out.

---

## Flows & Call Chains

### 1\. Reader success flow / closest HTTP reader flow

* adapter/wsgi.py:create\_app → adapter.http\_reader:bp → /reader handler → engine.runtime.emit\_reader\_public\_bytes / engine.presenter.emitter.emit\_public → Flask Response.  
* Anchors:  
  * Blueprint registration: adapter/wsgi.py:27-29.  
  * /reader route: adapter/http\_reader.py:330-331.  
  * Reader imports: adapter/http\_reader.py:7-13.  
  * Reader header helper: adapter/http\_reader.py:28-32.  
* Observations:  
  * Endpoint catalog classifies /reader as "dev\_harness" and "Reader success route (dev-only)"; proof docs/ENDPOINTS\_CATALOG.json:1.  
  * Adapter code imports sampler and compat modules directly; proof adapter/http\_reader.py:12-13.

### 2\. Compat API flow

* adapter/wsgi.py:create\_app → engine.http.compat\_handler:compat\_blueprint → post\_json → engine.compat.compute.compat\_public → engine.presenter.emit\_public → Flask Response.  
* Anchors:  
  * Register compat blueprint: adapter/wsgi.py:27-29.  
  * Prefix: engine/http/compat\_handler.py:11.  
  * POST handler: engine/http/compat\_handler.py:90-127.  
  * Engine call: engine/http/compat\_handler.py:121-124.  
  * Emitter call: engine/http/compat\_handler.py:14-21.  
* Observations:  
  * Production env returns not-found envelope before compute; proof engine/http/compat\_handler.py:92-94.  
  * GET exists and returns {"ok": True, "schema": "v1"}; proof engine/http/compat\_handler.py:82-88.  
  * HEAD/OPTIONS are explicitly transport-shaped; proof engine/http/compat\_handler.py:32-53.

### 3\. CLI showcompat / compat preview flow

* pyproject.toml console script → engine.cli.main:cli → \_build\_parser subcommand showcompat → showcompat handler → compat\_public / conjunction\_public\_resolved / emit\_reader\_public\_envelope / engine.presenter.emitter.  
* Anchors:  
  * Console script: pyproject.toml:\[project.scripts\].  
  * Parser/subcommand: engine/cli/main.py:73-131.  
  * Imports: engine/cli/main.py:13-42.  
  * Argparse dispatch: engine/cli/main.py:248-260.  
* Observations:  
  * showcompat supports pair-file, split files, stdin-like file inputs, vendor/db/auto source selection, conjunction, and dump outputs; proof engine/cli/main.py:90-130.  
  * CLI exit handling maps parser failures to 64; proof engine/cli/main.py:248-253.

### 4\. Vendor acquisition flow / BodyGraph ingest

* engine.cli.main:bg\_resolve → engine.bodygraph.resolver.resolve\_bodygraph → \_resolve\_vendor → engine.bodygraph.ingest.ingest\_vendor\_bodygraph → HdApiClient.from\_env → HdApiClient.build\_request → HdApiClient.fetch → DBAccess.for\_current\_env → SQL insert into hde.body\_graphs.  
* Anchors:  
  * CLI call: engine/cli/main.py:218-235.  
  * Resolver branch: engine/bodygraph/resolver.py:70-80.  
  * Rails gates: engine/bodygraph/resolver.py:105-127.  
  * Ingest call: engine/bodygraph/resolver.py:144-145.  
  * Client/env setup: engine/bodygraph/ingest.py:131-134, engine/bodygraph/vendor\_client.py:265-305.  
  * DB persistence: engine/bodygraph/ingest.py:166-173, 214-220.  
* Observations:  
  * Vendor source requires birth tuple at CLI layer; proof engine/cli/main.py:218-223.  
  * SAFE/network gates can stop before network; proof engine/bodygraph/resolver.py:108-127.  
  * Ingest writes success/canon logs; proof engine/bodygraph/ingest.py:177-198.

### 5\. Evidence index update/validation flow

* tools/evidence/update\_evidence\_index.py:main → constants HUMAN\_INDEX / HASH\_SENTINEL / MIRROR\_PATH → baseline/epic artifact records → writes/checks index/mirror/hash.  
* Anchors:  
  * Tool purpose: tools/evidence/update\_evidence\_index.py:1-12.  
  * Paths: tools/evidence/update\_evidence\_index.py:23-28.  
  * Baseline entries: tools/evidence/update\_evidence\_index.py:35-48.  
  * Epic entries: tools/evidence/update\_evidence\_index.py:49-75, 76-118, 119-150.  
* Observations:  
  * The tool imports determinism pins via engine.runtime.determinism\_env; proof tools/evidence/update\_evidence\_index.py:34.  
  * Mirror path is artifacts/evidence\_index.jsonl; proof tools/evidence/update\_evidence\_index.py:26-27.  
  * Human index path is docs/evidence/INDEX.json; proof tools/evidence/update\_evidence\_index.py:23-25.

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Adapter and presenter are both top-level packages and engine-internal packages also exist (engine/presenter, engine/http, engine/cli).  
  * Proof: listing shows presenter/reader\_v1/emitter.py and engine/presenter/emitter.py; engine/http/compat\_handler.py; adapter/http\_reader.py.  
  * Impact: This creates ambiguity about whether “presenter” means top-level presenter/ or engine/presenter/ in architecture discussions.

### Surface drift

* Observed: Compat HTTP route lives under engine/http/compat\_handler.py, while app registration is in adapter/wsgi.py.  
  * Proof: engine/http/compat\_handler.py:11 defines compat\_blueprint; adapter/wsgi.py:27-29 registers it.  
  * Impact: HTTP surface code is split between adapter/ and engine/http/.

### Evidence drift

* Observed: Governed/evidence-like outputs are spread across docs/, artifacts/, audit/, plus root-level reports and proof-like files.  
  * Proof: top-level listing includes docs, artifacts, audit, proofs, reports, scan\_reports, AcceptanceMap.md, multiple hde-epic023\_\_...step\_report.md.  
  * Impact: This creates ambiguity about evidence home boundaries without consulting index tooling.

### Determinism drift

* Observed: Core sampler states no clocks/random/external state, while vendor/ingest paths use time, network, DB, and file logs.  
  * Proof: engine/sampler/core.py:170-176; engine/bodygraph/vendor\_client.py:427-459; engine/bodygraph/ingest.py:131-140, 166-198.  
  * Impact: Deterministic compute paths and operational acquisition paths have different side-effect profiles.

### Vendor seam drift

* Observed: Vendor client and bodygraph ingest live inside engine/bodygraph/, not a top-level vendor/ package.  
  * Proof: engine/bodygraph/vendor\_client.py:222-223; engine/bodygraph/ingest.py:112-123.  
  * Impact: Vendor seam is engine-internal by path, while route/app wiring remains adapter-level.

### Path-case drift

* Observed: Most audit QA epic paths are lowercase audit/qa/hde-epic\#\#\#, while root contains mixed-case/symbol-heavy markdown filenames.  
  * Proof: listing shows audit/qa/hde-epic035 and root files such as Approved Remediation Plan EPIC029.md, EPIC023\_D12\_close\_pack\_manifest\_FINAL\_EVIDENCE.md.  
  * Impact: Path naming conventions differ between governed QA roots and root-level report files.

### Root proliferation

* Observed: 18 top-level roots look like possible truth/evidence/tooling homes: audit, artifacts, docs, tools, scripts, catalog, schemas, config, fixtures, goldens, reports, scan\_reports, validation, proofs, math, release, freeze, migrations.  
  * Proof: top-level listing output.  
  * Impact: Multiple roots contain architecture/evidence/runtime support material.

### Alignment summary table

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package exists | Aligned | engine/compat/compute.py, engine/sampler/core.py listing |
| Adapter package exists | Aligned | adapter/wsgi.py:16-29 |
| Presenter exists | Partial | engine/presenter/emitter.py:6-13 and presenter/reader\_v1/emitter.py:54-65 |
| CLI entrypoint exists | Aligned | pyproject.toml script hdctl \= "engine.cli.main:cli" |
| Vendor seam outside compute core | Partial | Vendor path is engine/bodygraph/vendor\_client.py, compute path imports resolver for conjunction at engine/compat/compute.py:4-6 |
| Evidence layout | Partial | Index tooling binds docs/evidence, artifacts/evidence\_index.jsonl, and audit/...; proof tools/evidence/update\_evidence\_index.py:23-28, 49-75 |

---

## Negative-Claim Proof Appendix

* Workspace/monorepo manager config not found  
  * Searched tokens/files: package.json, plus Python packaging files.  
  * Method: find . \-maxdepth 2 \\( \-name 'pyproject.toml' \-o \-name 'setup.cfg' \-o \-name 'setup.py' \-o \-name 'requirements\*.txt' \-o \-name 'package.json' \\).  
  * Scope: repo root, max depth 2\.  
  * Result: output listed ./pyproject.toml, ./requirements-dev.txt, ./requirements.txt, and ./.audit\_src/requirements-dev.txt; no package.json, no setup.cfg, no setup.py.  
* Top-level vendor/ directory not found  
  * Searched token/path: top-level directory name vendor.  
  * Method: find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort.  
  * Scope: repo root top level.  
  * Result: listing includes engine, adapter, presenter, artifacts, etc.; no top-level vendor.  
* Working tree changes not found  
  * Searched state: dirty paths.  
  * Method: git status \--porcelain.  
  * Scope: current git repository.  
  * Result: 0 output lines; reported clean.  
  *   
  * Result: 0 output lines; reported clean.

