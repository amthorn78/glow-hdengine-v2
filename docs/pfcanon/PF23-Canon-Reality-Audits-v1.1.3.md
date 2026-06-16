# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.3

**Status:** Canon

**Effective date:** 2026-06-06

**Last Update Gate:** HDE-EPIC033

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

**Date:** 2026-06-06

**Last Epic:** HDE-EPIC033

## Audit Snapshot Metadata

* Repo root: confirmed current working directory and Git top-level are both /workspace/glow-hdengine-v2.  
  * Command proof: pwd && git rev-parse \--show-toplevel returned:  
    * /workspace/glow-hdengine-v2  
    * /workspace/glow-hdengine-v2  
* Commit: a937fc7f6eb7e3a81e610371c7e76752a82a485a.  
  * Command proof: git rev-parse HEAD.  
* Working tree cleanliness: clean.  
  * Command proof: git status \--porcelain returned no output.  
* Branch: work.  
  * Command proof: git rev-parse \--abbrev-ref HEAD.  
* Timestamp UTC: 2026-06-05T22:13:38Z.  
  * Command proof: date \-u \+%Y-%m-%dT%H:%M:%SZ.  
* Execution environment:  
  * OS/kernel: Linux ddf3911bc465 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 x86\_64 x86\_64 GNU/Linux.  
  * Python: Python 3.14.4.  
  * Node: v24.15.0.

Scope/posture used for this audit

* This was a read-only descriptive architecture audit. I did not edit files, run generators in write mode, run tests that could update governed artifacts, commit, or open a PR.  
* In scope: engine modules and direct callers, HTTP adapter surfaces, CLI, vendor seam, DB/cache path, evidence/canon artifacts and indices, and QA/CI checks.  
* Out of scope: unrelated FE/app code unless it directly clarifies engine surface wiring.

---

## Top-level Repo Map

### Command listing proof

The top-level listing command find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort shows these audit-relevant roots and files among others:

* engine  
* adapter  
* presenter  
* docs  
* artifacts  
* audit  
* tools  
* ci  
* tests  
* scripts  
* .github  
* pyproject.toml  
* requirements.txt  
* requirements-dev.txt  
* run\_flask.py  
* run\_flask\_dev.sh  
* README.md  
* AGENTS.md

### Expected HD Engine families

* engine/ — Present. It contains sampler, compatibility compute, bodygraph/vendor, DB, presenter wrapper, runtime, serializer, narratives, HTTP compat handler, and CLI code. The file inventory includes engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/vendor\_client.py, engine/db/adapter.py, engine/http/compat\_handler.py, and engine/cli/main.py from the command find engine adapter presenter \-maxdepth 3 \-type f | sort.  
* adapter/ — Present. It contains Flask app/wsgi wiring, reader blueprint, DB access/cache helpers, env/no-IO guards, and schemas. adapter/wsgi.py creates the Flask app and registers reader\_bp and compat\_blueprint.   
* presenter/ — Present. It contains a top-level presenter package separate from engine/presenter, including presenter/reader\_v1/emitter.py and presenter/json\_canon\_compare.py. The reader v1 emitter imports engine.presenter.emitter, described in-code as the component that “emits UTF-8 with exactly one trailing LF.”   
* CLI package location — Present but not as top-level cli/. The console script is hdctl \= "engine.cli.main:cli" in pyproject.toml, and engine/cli/main.py defines the parser and handlers.   
  Negative proof for a top-level cli/ directory is in the appendix.  
* docs/ — Present. It contains endpoint catalogs, acceptance maps, evidence index files, PF canon files, architecture docs, and schemas. Examples include docs/ENDPOINTS\_CATALOG.json, docs/evidence/INDEX.json, and docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.3.1.md from the command find docs \-maxdepth 2 \-type f | sort.  
* artifacts/ — Present. It contains generated or evidence-like outputs, including CLI captures, bodygraph snapshots, DB proofs, evidence mirror files, canonical JSON artifacts, and .path\_proof.txt siblings. The file count command showed artifacts 918 files and examples including artifacts/evidence\_index.jsonl.sha256, artifacts/logs/keys\_only\_sample.jsonl, and many artifact subtrees.  
* audit/ — Present. It contains manifests, close reports, QA run logs, doc deltas, preflight files, and evidence-like material. The file count command showed audit 2254 files and examples including audit/EPIC-024\_MANIFEST.json, audit/EPIC-027\_close\_report.md, and audit/qa/hde-epic033/....  
* tools/ — Present. It contains evidence generators/checkers, CLI guards, registry report tooling, QA harnesses, and artifact-producing scripts. tools/evidence/update\_evidence\_index.py declares the human index, hash sentinel, and machine mirror paths.   
* ci/ and .github/ — Present. .github/workflows/ci.yml defines GitHub Actions jobs, and ci/checks/ contains shell/Python gates. The workflow named ci runs on push and pull request.   
* tests/ — Present. It contains adapter, CLI, compat, bodygraph, evidence, DB, provider, transport, unit, and QA tests. The test listing includes tests/adapter/test\_reader\_parity.py, tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/bodygraph/test\_vendor\_client.py, and tests/evidence/test\_sanity\_pipeline.py.  
* scripts/ — Present. It contains runnable helper scripts including ingest, DB, QA, and sanity scripts. The QA-relevant listing includes scripts/ingest/run\_vendor\_ingest.py, scripts/db/run\_retention\_job.py, scripts/qa/d6\_live\_vendor\_qa.py, and scripts/run\_sanity.sh.

### Top-level root discipline capture: truth/evidence-like homes observed

Top-level roots that appear to hold governed outputs, source-of-truth docs, scripts, or evidence-like data:

* audit/  
* artifacts/  
* docs/  
* tools/  
* scripts/  
* ci/  
* .github/  
* catalog/  
* schemas/  
* goldens/  
* fixtures/  
* config/  
* migrations/  
* sql/  
* reports/  
* scan\_reports/  
* proofs/  
* math/  
* freeze/  
* release/  
* validation/

This is a factual inventory only.  
---

## Packaging and Entrypoints

### Packaging / build configuration

* pyproject.toml uses setuptools and wheel as build requirements and setuptools.build\_meta as the backend.   
* Project package name: glow-hdengine; version is 0.0.0; Python requirement is \>=3.10; runtime dependencies in pyproject.toml are empty.   
* Console script: hdctl \= "engine.cli.main:cli".   
* Package discovery: setuptools includes engine\*, adapter\*, and presenter\*.   
* Runtime requirements: requirements.txt lists psycopg\[binary\], Flask, and gunicorn.   
* Dev/test requirements: requirements-dev.txt lists jsonschema, pytest, pytest-cov, and pytest-mock.   
* Not found: setup.py, setup.cfg, top-level package.json, lock/workspace manager files were not found at repo root. Negative proof is in the appendix.

### Entrypoint inventory

#### HTTP server startup / app factory

* adapter/app.py exposes app \= create\_app() for flask \--app adapter.app run; it imports create\_app from adapter.wsgi.   
* adapter/wsgi.py:create\_app creates the Flask app, installs logging and env guard hooks, registers the reader and compat blueprints, defines /internal/healthz and /internal/readyz, and installs error handlers.   
* adapter/factory.py:create\_app is another Flask factory that registers adapter.http\_reader.bp with url\_prefix="" and strips ETags on /internal/ responses. 

#### CLI console script

* engine.cli.main:cli is the hdctl console script target.   
* engine/cli/\_\_main\_\_.py:main calls cli() and exits with its return code when invoked as a module. 

#### Evidence / indexing jobs

* tools/evidence/update\_evidence\_index.py defines HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH, and MIRROR\_SHA\_PATH, so it is the central evidence index/mirror updater/checker entrypoint.   
* tools/evidence/run\_sanity\_pipeline.py defines SANITY\_LOG \= Path("artifacts/sanity/sanity.log"), default sanity steps, and run\_pipeline.   
* CI invokes evidence jobs: .github/workflows/ci.yml runs tools/evidence/run\_canonical\_json\_gate.py, tools/evidence/update\_evidence\_index.py, tools/evidence/orientation\_demo.py \--check, ci/checks/check\_evidence\_index\_hash.sh, and ci/checks/check\_mirror\_schema.sh. 

---

## Engine Modules

### Sampler

* Primary module: engine/sampler/core.py.  
* Data structures: ViewerProfile, CandidateFeatures, SamplerConfig, CandidatePoolEntry, CandidatePool, RankedCandidate, and RankedCandidates are dataclasses defining sampler inputs, config, pool entries, and ranked outputs.   
* Pool formation: build\_candidate\_pool iterates raw candidates, skips zero-weight candidates, resolves bands, applies eligibility, and returns a CandidatePool.   
* Eligibility: \_is\_eligible checks minimum compatibility score, allowed bands, excluded bands, and required diversity key.   
* Ordering: \_compare\_entries sorts by weight, compatibility score, band priority, and compare\_ids; rank\_candidates uses sorted(..., cmp\_to\_key(...)) and assigns ranks.   
* Helper flow: sample\_and\_rank builds a candidate pool and immediately ranks it. 

### Core compatibility compute

* Primary module: engine/compat/compute.py.  
* Score/band helpers: \_score\_for derives a per-category score from sha256(pair\_key:category), applies viewer weight, rounds, and clamps; band\_for maps score thresholds to Cool, Open, Warm, or Glow.   
* Compatibility result: compat\_public normalizes the pair, computes category records in CATEGORIES\_ORDER\_V1, and returns categories plus metadata.   
* AB↔BA handling: compat\_public calls normalize\_pair; engine/compat/ordering.py normalizes by UID ordering and uses a stable hash tiebreaker when UIDs match.   
* Conjunction compatibility: conjunction\_public extracts person\_uid, normalizes left/right, calls compat\_public, and wraps the result under conjunction.   
* Boundary resolution: conjunction\_public\_resolved documents local lookup first, closed-rails refusal on missing local data, and open-rails resolver acquisition after local miss. 

### Determinism hazards inventory

Observed in sampled engine paths:

* Sampler core: no obvious time, randomness, network, or file I/O in engine/sampler/core.py; its docstring explicitly states ranking is deterministic and uses canonical comparators.   
  * Negative proof: rg \-n '\\brandom\\b|random\\.' engine/sampler engine/compat \-g '\*.py' returned 0 hits for randomness in sampled sampler/compat paths.  
* Compatibility core: engine/compat/compute.py is mostly hash/normalization compute, but conjunction\_public\_resolved can call resolve\_bodygraph(... source="vendor" ...) after local lookup misses.   
* Vendor/client path: engine/bodygraph/vendor\_client.py uses time and network primitives: time.monotonic, time.time, time.sleep, urlrequest.Request, and opener.open.   
* Ingest path: engine/bodygraph/ingest.py writes JSONL logs, uses UTC timestamps, measures duration with time.monotonic, and persists DB rows when not dry-run.   
* DB adapter: engine/db/adapter.py reads environment variables, writes adapter selection snapshots, and selects between psycopg and bridge providers. 

---

## Adapter / HTTP Surfaces

### Route registration map

* HTTP app creation: adapter/wsgi.py:create\_app creates Flask(\_\_name\_\_), installs logging/env guard, and registers reader\_bp and compat\_blueprint.   
* Reader blueprint creation: adapter/http\_reader.py:get\_reader\_bp creates Blueprint("reader\_v1", \_\_name\_\_), defaults emit\_fn to emit\_reader\_public\_bytes, and returns the blueprint.   
* Compat blueprint creation: engine/http/compat\_handler.py creates Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1"). 

Mounted route groups observed by rg \-n "@(bp|app|compat\_blueprint)\\.(get|post|route)|Blueprint\\(" adapter engine \-g '\*.py':

* /reader — adapter/http\_reader.py:reader\_v1 handles GET and HEAD parity inside the GET handler.   
* /reader POST — adapter/http\_reader.py:reader\_v1\_post returns method-not-allowed error.   
* /api/aux/narrative and /aux/narrative — adapter/http\_reader.py:aux\_narrative.   
* /api/compat/v1 — engine/http/compat\_handler.py:get\_ids\_only, post\_json, post\_json\_head, post\_json\_options.   
* /internal/version — adapter/http\_reader.py:internal\_version.   
* /internal/healthz, /internal/readyz — adapter/wsgi.py:internal\_healthz, internal\_readyz.   
* /internal/dev/sampler — adapter/http\_reader.py:dev\_sampler\_internal.   
* /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction — dev conjunction handlers.   
* /ops/db/unavailable, /ops/rails/refusal, /ops/probe/env, /ops/writer/diagnostic — ops/diagnostic surfaces. 

### Surface classification

* Reader-like JSON success: /reader returns canonical reader bytes, ETag, cache-control, Vary, and content length when v=1, APP\_ENV=dev, and chart files validate.   
* Aux/narrative: /api/aux/narrative and /aux/narrative call emit\_public\_aux, set text/plain headers, narrative pack headers, optional ETag, and no-store on suppression.   
* Admin/internal: /internal/version builds identity payloads and supports GET/HEAD; /internal/healthz and /internal/readyz emit JSON health payloads.   
* Compat/internal admin: /api/compat/v1 is the compat pair endpoint; POST is hidden in prod by returning ERR\_NOT\_FOUND, validates viewer prefs, calls compat\_public, and emits writer payload bytes.   
* Dev/diagnostic harness: /internal/dev/sampler gates by APP\_ENV through \_dev\_admin\_gate, reads candidate IDs, calls sample\_and\_rank, and emits candidate IDs.   
* Ops/diagnostic writer: /ops/writer/diagnostic requires admin scope, reads an empty JSON body with allowed keys, builds and persists an idempotence record, and emits {"ok": true, "message": "diagnostic"}. 

### Transport semantics hooks

* HEAD vs GET parity for /reader: reader\_v1 computes the GET body first, then for HEAD returns an empty body with ETag and content length equal to the GET body length.   
* Conditional 304 for /reader: \_parse\_if\_none\_match extracts strong ETags, and reader\_v1 returns 304 with empty body when the computed ETag matches.   
* ETag generation/quoting: /reader computes etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"", and aux narrative sets Flask ETag and then explicitly formats ETag with quotes.   
* Cache-control rules: reader 200 headers set private, max-age=0, must-revalidate; writer responses set no-store; wsgi common headers default to no-store.   
* Content-Type rules: reader headers set application/json; charset=utf-8; writer response helper sets the same; aux narrative uses text/plain; charset=utf-8.   
* Compat HEAD/OPTIONS semantics: compat writer transport guard returns 405 for HEAD and 204 for OPTIONS on /api/compat/v1. 

---

## Presenter / Emitter

### Emitters found

* engine/presenter/emitter.py is the central canonical public JSON emitter; emit\_public delegates to engine.serializer.canon.sercanon, sorts keys by default, and emits LF-terminated UTF-8 bytes.   
* engine/serializer/canon.py documents canonical JSON rules: UTF-8 bytes, ensure\_ascii=False, sorted keys by default, compact separators, and exactly one trailing newline.   
* presenter/reader\_v1/emitter.py builds reader v1 envelopes, dedupes/sorts categories by ID, computes an idempotence\_hash over the preimage bytes, and emits final bytes through engine.presenter.emitter.emit\_public.   
* engine/runtime/public.py bridges core mechanics to reader v1 presenter: it computes the harmony band from charts and calls emit\_reader\_v1.   
* engine/narratives/preview.py emits aux narrative text bytes with a trailing newline when text exists; it returns an AuxPublicEmission metadata object rather than canonical JSON bytes.   
* presenter/json\_canon\_compare.py is a CLI helper that canonicalizes JSON objects via emitter.emit\_public, hashes both sides, and appends comparison logs. 

### Callers

* HTTP reader imports emit\_public, emit\_reader\_public\_bytes, and emit\_public\_aux.   
* Compat HTTP imports emit\_public and compat\_public.   
* CLI imports engine.presenter.emitter, emit\_reader\_public\_envelope, sercanon, emit\_public\_aux, and sampler functions.   
* BodyGraph ingest uses emitter.emit\_public\_with\_envelope for vendor payload and DB-emitted payload parity. 

---

## CLI Surfaces

### Console scripts and module entrypoints

* Console command: hdctl, mapped to engine.cli.main:cli.   
* Module entrypoint: engine/cli/\_\_main\_\_.py calls cli() and exits with its code. 

### Parser/subcommands

* Parser: \_build\_parser uses argparse.ArgumentParser(prog="hdctl", description="Glow HD Engine compatibility CLI", allow\_abbrev=False).   
* Subcommands are required: parser.add\_subparsers(dest="command", required=True).   
* showcompat: accepts \--pair-file, \--a-file, \--b-file, aliases \--a/--b, \--dump-reader, \--dump-admin-dir, \--source {db,vendor,auto}, \--conjunction, viewer prefs, user IDs, and birth tuples.   
* aux-preview: accepts narrative category, band, perspective, pair-file, \--show-narrative, and \--admin-out.   
* bg:resolve: requires \--user, accepts \--source {auto,db,vendor}, \--upsert, \--dry-run, and birth tuple fields.   
* dev:sampler: requires \--viewer and \--candidates-file; accepts optional \--seed. 

### CLI behavior and output

* Missing args / parser errors: cli() catches SystemExit from argparse and maps nonzero parser exits to return code 64\.   
* Typed CLI errors: CliError carries code and exit\_code; cli() writes the error code to stderr and returns err.exit\_code.   
* showcompat normal flow: it loads or resolves source data, canonicalizes pair order, computes TS features, calls compat\_public, emits canonical compat bytes, computes reader bytes via emit\_reader\_public\_envelope, optionally writes reader/admin dumps, and writes compat bytes to stdout.   
* showcompat \--conjunction: it rejects dump flags, resolves conjunction inputs, calls conjunction\_public\_resolved, emits canonical bytes, and writes them to stdout.   
* CLI stdout guard: \_emit\_stdout\_bytes rejects payloads missing final LF or containing CRLF, then writes to sys.stdout.buffer.   
* File writes: \--dump-reader writes bytes to the target path after creating parent directories.   
* Admin dumps: \_emit\_admin\_dumps writes left/right bodygraph, composite bodygraph, and compat proof JSON files via canon\_dump.   
* bg:resolve: calls resolve\_bodygraph, emits result.payload through emitter.emit\_public, writes to stdout, and returns result.exit\_code.   
* dev:sampler: requires dev/test/local APP\_ENV through \_ensure\_dev\_admin\_env, loads candidate JSON from a file, calls sample\_and\_rank, and writes canonical sampler output to stdout. 

---

## Vendor Seam & BodyGraph Storage

### Vendor client

* Vendor HTTP module: engine/bodygraph/vendor\_client.py.  
* Client class: HdApiClient is documented as an HTTP client with pinned retry/backoff and typed error mapping.   
* Environment inputs: HdApiClient.from\_env reads HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, and RELEASE\_ID; missing required vendor config raises PROVIDER\_CONFIG\_MISSING.   
* Request shaping: build\_request requires birthdate, birthtime, and location, converts birthdate to vendor date format, builds compact JSON body bytes with a trailing LF, computes an input fingerprint, and sets headers including API/geocode keys and user agent.   
* Network call: fetch builds a urlrequest.Request and eventually the default request uses opener.open(req, timeout=timeout). 

### BodyGraph persistence/cache

* Resolver: engine/bodygraph/resolver.py:resolve\_bodygraph chooses source behavior for auto, db, and vendor; comments state Phase S8a treats auto as db while avoiding real IO.   
* Vendor ingest: engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph gates SAFE/network, builds a vendor request, fetches vendor result, emits canonical payload bytes, and either returns dry-run output or persists/fetches DB payload for parity.   
* DB table insert: \_persist\_bodygraph inserts into hde.body\_graphs (user\_id, vendor, vendor\_version, input\_fingerprint, payload) with ON CONFLICT DO NOTHING.   
* Cache/key identity: \_idempotency\_key is formatted as "{user\_id}:{vendor}:{vendor\_version}:{fingerprint}".   
* DB reads: \_row\_count and \_fetch\_payload query hde.body\_graphs by user\_id, vendor, vendor\_version, and input\_fingerprint.   
* DB provider facade: DBAccess.for\_current\_env reads DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, and DB\_ALLOW\_BRIDGE\_IN\_PROD, then selects psycopg or bridge providers and writes an adapter selection snapshot. 

### Offline / vendor-required posture

* Closed SAFE rails: resolve\_bodygraph refuses vendor source when SAFE\_MODE is truthy and returns PROVIDER\_REFUSED.   
* Network disabled: resolve\_bodygraph returns PROVIDER\_NETWORK\_BLOCKED when network is not allowed.   
* Ingest-level gate: ingest\_vendor\_bodygraph raises PROVIDER\_REFUSED when SAFE\_MODE is truthy and raises PROVIDER\_NETWORK\_BLOCKED when ALLOW\_NETWORK is false.   
* Conjunction resolver posture: conjunction\_public\_resolved documents that local lookup is first, closed rails refuse provider acquisition when local data is missing, and open rails allow resolver acquisition after local miss. 

---

## Evidence, Indices, Catalogs

### Evidence homes inventory

* docs/evidence/ contains human evidence index files, hash sentinel, path proofs, and evidence docs. update\_evidence\_index.py declares docs/evidence/INDEX.json and docs/evidence/INDEX.sha256 as the human index and hash sentinel.   
* artifacts/ contains generated evidence-like outputs, proofs, logs, CLI outputs, bodygraph snapshots, DB proofs, and the machine evidence mirror. The updater declares artifacts/evidence\_index.jsonl and artifacts/evidence\_index.jsonl.sha256.   
* audit/ contains epic manifests, close reports, QA logs, token matrices, doc deltas, preflight, and gate outputs. update\_evidence\_index.py hardcodes many audit/... artifact paths for epic acceptance artifacts.   
* audit/qa/\*\* contains per-epic QA trees; command listing showed audit/qa/hde-epic017 through audit/qa/hde-epic033, plus audit/qa/premerge.  
* artifacts/db\*, artifacts/bodygraph, artifacts/db\_bridge hold DB/bodygraph evidence such as snapshots, proofs, schema logs, and path proofs; these were shown in find engine adapter presenter docs artifacts audit tools ci tests scripts \-maxdepth 2 \-type f.  
* audit/gates/\*\* is referenced by CI and env pins tooling; ci/checks/check\_env\_pins.sh writes/checks audit/gates/determinism/env\_pins.log. 

### Evidence index structures

* Human index: docs/evidence/INDEX.json. Declared by HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json".   
* Hash sentinel: docs/evidence/INDEX.sha256. Declared by HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".   
* Machine mirror: artifacts/evidence\_index.jsonl. Declared by MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl".   
* Mirror schema check: ci/checks/check\_mirror\_schema.sh requires keys such as artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, and size\_bytes.   
* Path validation: tools/evidence/validate\_evidence\_paths.py checks whether artifact paths exist under the repo root and reports MISSING or PATH\_OUTSIDE\_ROOT.   
* CI reads/checks: .github/workflows/ci.yml runs update, check, orientation demo check, evidence hash check, and mirror schema check. 

### Endpoint catalog

* Catalog file: docs/ENDPOINTS\_CATALOG.json. It has top-level keys endpoints and success\_endpoints; a compact JSON line lists entries for /api/compat/v1, dev conjunction routes, /internal/version, and /reader.   
* Audit mirror: artifacts/audit/ENDPOINTS\_CATALOG.json exists and has the same top-level shape based on the JSON inspection command.  
* Referenced by tests: tests/http/test\_endpoint\_catalog.py reads docs/ENDPOINTS\_CATALOG.json and asserts metadata for /api/compat/v1, dev conjunction routes, and /reader. 

### Proof/snapshot artifacts

Observed evidence/proof patterns include:

* .path\_proof.txt siblings under docs, artifacts, and audit from top-level listings.  
* artifacts/evidence\_index.jsonl.path\_proof.txt, artifacts/evidence\_index.jsonl.sha256, and artifacts/evidence\_index.jsonl.sha256.path\_proof.txt from the artifacts listing.  
* Reader/transport snapshots under tests/transport/headers/\*.snap with .path\_proof.txt siblings.  
* CLI/presenter parity artifacts referenced by tests: artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/presenter/showcompat\_ab.bytes, artifacts/presenter/showcompat\_ba.bytes, and artifacts/presenter/reader\_cli\_parity.bytes.   
* Sanity pipeline output path: artifacts/sanity/sanity.log. 

---

## Tests, QA Harness, CI/Checks

### Tests map

* Adapter/HTTP tests: tests/adapter/test\_reader\_parity.py imports adapter.wsgi.create\_app, exercises /reader, and asserts ETag, LF-terminated bytes, cache/Vary headers, 304 behavior, and HEAD behavior.   
* Endpoint catalog tests: tests/http/test\_endpoint\_catalog.py reads docs/ENDPOINTS\_CATALOG.json and asserts classifications/methods/env gates for compat, dev conjunction, and reader entries.   
* CLI showcompat tests: tests/cli/test\_showcompat\_parity\_and\_identity.py invokes scripts/hdctl.py showcompat with vendor birth args and asserts two-run identity, empty stderr, LF, and canonical re-emission behavior when open rails are used.   
* Evidence tests: test listing includes tests/evidence/test\_sanity\_pipeline.py, tests/evidence/test\_machine\_mirror\_self\_proof.py, tests/evidence/test\_orientation\_demo.py, and tests/evidence/test\_evidence\_index\_snapshot.py.  
* Vendor/bodygraph tests: test listing includes tests/bodygraph/test\_vendor\_client.py, tests/bodygraph/test\_resolver\_vendor.py, tests/bodygraph/test\_ingest.py, and provider tests under tests/provider/.  
* Sampler tests: test listing includes tests/unit/test\_sampler\_core.py and tests/evidence/test\_sampler\_evidence.py.  
* DB tests: test listing includes tests/db/test\_adapter\_contract.py, tests/db/test\_adapter\_selection.py, tests/db/test\_no\_import\_time\_connect.py, and related DB resolver/env tests.

### CI workflows

* Workflow: .github/workflows/ci.yml, name ci, triggers on push and pull request.   
* Main job test: sets LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, and ALLOW\_NETWORK=0, installs requirements, installs the package, runs env pins, CLI help, serializer/emitter guards, canonical JSON gate, evidence index update/check, orientation check, PO-006 token registry check/report, mirror/hash/final-LF checks, and selected pytest suites.   
* Compat conjunction job: compat-conj-pr01-closure runs closed rails and specific pytest assertions for conjunction identity hash and evidence index compat artifacts.   
* EPIC020 job: epic020 acceptance suites (closed rails) sets closed rails and runs EPIC020 determinism-rails acceptance tests. 

### Script/check inventory

* ci/checks/check\_env\_pins.sh: runs python \-m engine.runtime.determinism\_env with \--log-path audit/gates/determinism/env\_pins.log and \--check-log.   
* ci/checks/check\_mirror\_schema.sh: validates artifacts/evidence\_index.jsonl key sets, sorting, duplicate entries, token references, and proof anchors.   
* tools/evidence/run\_sanity\_pipeline.py: runs canonical bytes, showcompat parity, invariance, env pins, release identity, sampler evidence, engine-core evidence, ordering, narrative registry diff, evidence index update/check, and orientation demo steps.   
* tools/evidence/update\_evidence\_index.py: central updater/checker for human index, hash sentinel, mirror, and mirror SHA.   
* tools/evidence/validate\_evidence\_paths.py: validates paths in the evidence index are within root and exist. 

---

## Flows & Call Chains

### 1\. Reader success flow — HTTP

Call chain  
adapter.wsgi:create\_app → adapter.http\_reader:get\_reader\_bp → reader\_v1 → \_safe\_load\_chart / \_require\_tz\_or\_raise → engine.runtime.emit\_reader\_public\_bytes → engine.runtime.public.emit\_reader\_public\_envelope → presenter.reader\_v1.emit\_reader\_v1 → engine.presenter.emitter.emit\_public → Flask Response.  
Observations

* adapter.wsgi:create\_app registers reader\_bp.   
* reader\_v1 requires query parameter v=1 and APP\_ENV=dev; otherwise it emits typed errors.   
* Chart paths are constrained under fixtures/charts and read via Path.read\_text.   
* The route passes charts and identity fields to emit\_fn, defaulting to emit\_reader\_public\_bytes.   
* Runtime computes harmony band and calls emit\_reader\_v1.   
* The route computes quoted SHA-256 ETag, handles conditional 304 and HEAD, and returns body bytes for GET. 

### 2\. Compat API flow — HTTP

Call chain  
adapter.wsgi:create\_app → engine.http.compat\_handler:compat\_blueprint → post\_json → validate\_viewer\_prefs / normalize\_viewer\_prefs → engine.compat.compute.compat\_public → \_writer\_payload → engine.presenter.emit\_public → Flask Response.  
Observations

* Compat blueprint is mounted at /api/compat/v1.   
* POST returns ERR\_NOT\_FOUND when APP\_ENV=prod.   
* POST validates id/payload mixing and required person\_uid shape.   
* Viewer preferences are validated/normalized before calling compat\_public.   
* compat\_public normalizes AB/BA and computes category records.   
* \_writer\_payload emits canonical bytes, sets no-store, removes ETag/content encoding, and sets content length. 

### 3\. CLI showcompat / compat preview flow

Call chain  
pyproject.toml:hdctl → engine.cli.main:cli → \_build\_parser → showcompat → \_load\_from\_source / \_load\_from\_files\_or\_stdin → \_canonical\_pair → compat\_public and emit\_reader\_public\_envelope → emitter.emit\_public → \_emit\_stdout\_bytes / optional dumps.  
Observations

* Console script maps hdctl to engine.cli.main:cli.   
* Parser defines showcompat and its file/source/conjunction/dump arguments.   
* showcompat supports source modes db, vendor, and auto; vendor source calls ingest\_vendor\_bodygraph(... dry\_run=True).   
* Normal flow computes TS features, compatibility payload, reader bytes, optional dumps, and stdout bytes.   
* \_emit\_stdout\_bytes enforces LF/no-CRLF before writing. 

### 4\. Vendor acquisition / BodyGraph ingest flow

Call chain  
engine.cli.main:bg\_resolve or showcompat \--source vendor → engine.bodygraph.resolver.resolve\_bodygraph or engine.bodygraph.ingest.ingest\_vendor\_bodygraph → HdApiClient.from\_env → HdApiClient.build\_request → HdApiClient.fetch → canonical emitter → optional DB persist/readback.  
Observations

* bg\_resolve requires full birth tuple for \--source vendor and calls resolve\_bodygraph.   
* resolve\_bodygraph gates vendor with SAFE\_MODE and ALLOW\_NETWORK.   
* Ingest reads env rails, refuses closed rails, builds HdApiClient.from\_env, shapes request, fetches vendor result, and emits canonical payload.   
* Dry-run writes a success log record with rows\_affected: 0 and returns an IngestOutcome without DB writes.   
* Non-dry-run persists into hde.body\_graphs, reads back, re-emits DB payload bytes, and records parity. 

### 5\. Evidence index update/validation flow

Call chain  
.github/workflows/ci.yml → python tools/evidence/update\_evidence\_index.py → python tools/evidence/update\_evidence\_index.py \--check → python tools/evidence/orientation\_demo.py \--check → ci/checks/check\_evidence\_index\_hash.sh → ci/checks/check\_mirror\_schema.sh.  
Observations

* CI runs update, check, orientation check, hash check, and mirror schema check.   
* update\_evidence\_index.py defines human index, sentinel, mirror, and mirror SHA paths.   
* check\_mirror\_schema.sh validates required/optional keys and duplicate/sort properties.   
* validate\_evidence\_paths.py checks evidence paths remain within root and exist. 

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: There is both a top-level presenter/ package and an engine/presenter/ package. The top-level reader v1 emitter imports engine.presenter.emitter.   
  Impact: This creates factual ambiguity about which presenter package is the primary home for public JSON emission without reading call sites.  
* Observed: CLI is under engine/cli/, not a top-level cli/ package; pyproject.toml maps hdctl to engine.cli.main:cli.   
  Impact: The expected CLI family exists, but its actual package home is nested under engine/.

### Surface drift

* Observed: /reader is mounted at root path /reader, while the endpoint catalog marks it as classification:"dev\_harness" and env\_gate:"APP\_ENV=dev".   
  Impact: The reader success route is present, but the repo evidence classifies it as dev-harness rather than a general public route.  
* Observed: Compat HTTP lives in engine/http/compat\_handler.py rather than under adapter/, while it is registered by adapter.wsgi.   
  Impact: The HTTP adapter split is partial: route registration is in adapter, while one HTTP route module is under engine.

### Evidence drift

* Observed: Governed/evidence-like material appears under docs/, artifacts/, and audit/, and tooling hardcodes all three homes.   
  Impact: Evidence identity is distributed across multiple roots, requiring index/mirror tooling to determine current bindings.

### Determinism drift

* Observed: Core sampler code states it uses no randomness/clocks/external state, but vendor/ingest paths use time, sleep, network, file logs, and DB writes.   
  Impact: Determinism posture differs by layer: sampler/core is pure-compute, while vendor/ingest paths rely on rails and injected/default side effects.

### Vendor seam drift

* Observed: Vendor acquisition appears in engine/bodygraph/\* and is also reachable from engine/compat/compute.py through conjunction\_public\_resolved.   
  Impact: Vendor acquisition is not confined to an adapter/ package; compatibility resolution can invoke bodygraph resolver paths.

### Path-case drift

* Observed: audit/qa/ contains many lowercase epic roots, but command find audit/qa \-path '\*\[A-Z\]\*' \-print | wc \-l returned 256 mixed-case paths under audit/qa.  
  Impact: Path case is mixed in QA evidence trees, which can matter for case-sensitive path proofs and reviewer searches.

### Root proliferation

* Observed: At least 18 top-level roots look evidence/truth/tooling-related: audit, artifacts, docs, tools, scripts, ci, .github, catalog, schemas, goldens, fixtures, config, migrations, sql, reports, scan\_reports, proofs, math, plus freeze, release, and validation depending on reviewer classification.  
  Impact: The repo has multiple factual homes for source, artifacts, evidence, and release/proof material.

### Alignment summary table

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package exists | Aligned | engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/vendor\_client.py, and engine/db/adapter.py exist in engine inventory. |
| Adapter package exists | Aligned | Flask app factory and blueprint registration are in adapter/wsgi.py.  |
| Presenter split | Partial | Both engine/presenter/emitter.py and presenter/reader\_v1/emitter.py participate in emission.  |
| CLI surface | Partial | CLI exists as engine.cli.main:cli, not top-level cli/.  |
| Vendor seam outside core compute | Partial | Vendor client is under engine/bodygraph, while compat conjunction resolution can call resolve\_bodygraph.  |
| Evidence layout | Partial | Evidence index tooling binds docs/evidence, artifacts, and audit homes.  |
| Determinism gates | Aligned for CI/gates | CI sets closed rails and runs env/evidence checks.  |

---

## Negative-Claim Proof Appendix

### Top-level cli/ directory not found

* Claim: No top-level cli/ directory exists.  
* Search token: cli  
* Method/scope: find . \-maxdepth 1 \-type d \-name 'cli' \-print | wc \-l from repo root.  
* Result: 0

### setup.py, setup.cfg, top-level JS workspace/package files not found

* Claim: No root setup.py, setup.cfg, package.json, pnpm-workspace.yaml, yarn.lock, or package-lock.json found.  
* Search token: setup.py, setup.cfg, package.json, pnpm-workspace.yaml, yarn.lock, package-lock.json  
* Method/scope: find . \-maxdepth 1 \\( \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'package.json' \-o \-name 'pnpm-workspace.yaml' \-o \-name 'yarn.lock' \-o \-name 'package-lock.json' \\) \-print | wc \-l from repo root.  
* Result: 0

### FastAPI app not found in audited HTTP code

* Claim: No FastAPI usage found in adapter/ or engine/ Python code.  
* Search token: FastAPI  
* Method/scope: rg \-n 'FastAPI' adapter engine \-g '\*.py' | wc \-l  
* Result: 0

### Randomness not found in sampled sampler/compat paths

* Claim: No random usage found in sampled engine/sampler and engine/compat Python paths.  
* Search token: \\brandom\\b|random\\.  
* Method/scope: rg \-n '\\brandom\\b|random\\.' engine/sampler engine/compat \-g '\*.py' | wc \-l  
* Result: 0

### Scheduled/background framework tokens not found, except incidental text hits

* Claim: No APScheduler token found in repo search scope used.  
* Search token: APScheduler  
* Method/scope: rg \-n \--fixed-strings 'APScheduler' . \-g '\!\*.json' \-g '\!\*.jsonl' \-g '\!artifacts/\*\*' \-g '\!audit/\*\*' \-g '\!docs/evidence/INDEX.json' | wc \-l  
* Result: 0  
* Claim: No FastAPI token found in the same broad scope.  
* Search token: FastAPI  
* Method/scope: same broad rg scope.  
* Result: 0

---

## Read-only Commands Used

* ✅ pwd && git rev-parse \--show-toplevel && git rev-parse HEAD && git status \--porcelain && git rev-parse \--abbrev-ref HEAD && date \-u \+%Y-%m-%dT%H:%M:%SZ && uname \-a && (python \--version || true) && (node \--version || true)  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort  
* ✅ find engine adapter presenter \-maxdepth 3 \-type f | sort  
* ✅ nl \-ba ... | sed \-n ... on audited source/test/config files  
* ✅ rg \-n "@(bp|app|compat\_blueprint)\\.(get|post|route)|Blueprint\\(" adapter engine \-g '\*.py'  
* ✅ rg \-n "emit\_public|emit\_reader\_v1|emit\_reader\_public" engine adapter presenter tests \-g '\*.py'  
* ✅ find tests \-maxdepth 3 \-type f | sort  
* ✅ find .github ci \-maxdepth 3 \-type f | sort  
* ✅ find tools ci/checks scripts \-maxdepth 2 \-type f \\( \-name 'check\_\*' \-o \-name 'run\_\*' \-o \-name '\*qa\*.py' \-o \-name '\*evidence\*.py' \\) | sort  
* ✅ rg/find negative-claim searches listed in the appendix

No tests were run, and no files were changed.