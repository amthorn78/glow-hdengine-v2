# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1

**Status:** Canon

**Effective date:** 2026-05-11

**Last Update Gate:** HDE-EPIC031

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

**Date:** 2026-05-11

**Last Epic:** HDE-EPIC031

## Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2 confirmed by pwd output: /workspace/glow-hdengine-v2.  
* Commit: 86b7d7d8fc0bb80bd10ad77e2664a8373d537e6a (git rev-parse HEAD).  
* Branch: work (git rev-parse \--abbrev-ref HEAD).  
* Working tree: clean. git status \--porcelain printed no changed paths.  
* Timestamp UTC: 2026-05-11T16:37:05Z.  
* Environment facts:  
  * OS/kernel: Linux 2f94215b59ba 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64...  
  * Python: Python 3.14.4  
  * Node: v24.15.0

Read-only posture: this audit used static inspection only. No files were modified and no tests were executed.  
Checks / inspection commands used:

* ✅ pwd; git rev-parse HEAD; git rev-parse \--abbrev-ref HEAD; git status \--porcelain; date \-u \+%Y-%m-%dT%H:%M:%SZ; uname \-a; python \--version; node \--version  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort  
* ✅ find engine adapter presenter tools ci scripts tests docs/evidence audit/qa artifacts \-maxdepth 2 \-type f | sort  
* ✅ rg \-n "Flask\\\\(|FastAPI\\\\(|APIRouter|Blueprint|@app\\\\.|@.\*route|console\_scripts|argparse|click|Typer|if \_\_name\_\_ \== .\_\_main\_\_.|def main\\\\(" ...  
* ✅ nl \-ba \<selected files\> | sed \-n '\<ranges\>p'  
* ✅ find . \-maxdepth 2 \-name '\<packaging/workspace token\>' \-print | wc \-l

## Top-level Repo Map

Repository listing proof: top-level output included .github, adapter, artifacts, audit, ci, docs, engine, presenter, scripts, tests, tools, pyproject.toml, requirements.txt, requirements-dev.txt, run\_flask.py, README.md, AGENTS.md, and many root artifact/report files.

### Expected HD Engine families

* engine/ — Present. Contains the main Python package for CLI, compat compute, sampler, BodyGraph, DB, runtime, serializers, presenter alias, provider code, and HTTP compat handler. Listing proof includes engine/cli/main.py, engine/compat/compute.py, engine/sampler/core.py, engine/bodygraph/vendor\_client.py, engine/db/adapter.py, engine/http/compat\_handler.py.  
* adapter/ — Present. Contains Flask app wiring, reader HTTP blueprint, DB access helper, env guards, ETag helpers, WSGI entrypoint. Listing proof includes adapter/http\_reader.py, adapter/factory.py, adapter/wsgi.py, adapter/db\_access.py, adapter/etag\_core.py.  
* presenter/ — Present. There is a top-level presenter directory and an engine presenter package. Listing / code proof includes engine/presenter/emitter.py; main output also showed presenter/json\_canon\_compare.py:112:if \_\_name\_\_ \== "\_\_main\_\_":.  
* CLI package location — Present. pyproject.toml declares hdctl \= "engine.cli.main:cli" and engine/cli/main.py defines def cli(argv: list\[str\] | None \= None) \-\> int: at lines 239–259.  
* docs/ — Present. Contains evidence index, endpoint catalog, PF canon, contracts, schemas, architecture docs. Directory listing proof includes docs/evidence, docs/pfcanon, docs/contracts, docs/schemas, and file proof includes docs/ENDPOINTS\_CATALOG.json.  
* artifacts/ — Present. Contains many evidence/proof/generated-looking outputs: CLI captures, DB snapshots, bodygraph logs, evidence mirror, proof path siblings. Directory listing proof includes artifacts/evidence\_index.jsonl, artifacts/proofs/success\_get.txt, artifacts/bodygraph, artifacts/db, artifacts/cli/showcompat.  
* audit/ — Present. Contains QA and gate outputs. Directory listing proof includes audit/gates, audit/qa/hde-epic020 through audit/qa/hde-epic031, audit/ops.  
* tools/ — Present. Contains evidence, CLI, QA, presenter, order, error-generation tooling. Listing proof includes tools/evidence/update\_evidence\_index.py, tools/evidence/run\_sanity\_pipeline.py, tools/cli/generate\_showcompat\_artifacts.py, tools/qa/run\_hde\_epic024\_harness.py.  
* ci/ and .github/ — Present. .github/workflows/ci.yml exists; ci/checks contains shell/Python gates such as check\_env\_pins.sh, check\_mirror\_schema.sh, check\_evidence\_index\_hash.sh.  
* tests/ — Present. Test listing includes tests/adapter, tests/cli, tests/compat, tests/bodygraph, tests/evidence, tests/db, tests/transport.  
* scripts/ — Present. Script listing includes scripts/ingest/run\_vendor\_ingest.py, scripts/db/run\_retention\_job.py, scripts/hdctl.py, scripts/release\_id\_recompute.py.

### Important top-level files

* pyproject.toml — Present. Declares package metadata and console script: snippet name \= "glow-hdengine" and \[project.scripts\] hdctl \= "engine.cli.main:cli".  
* requirements.txt — Present. Declares runtime dependencies: psycopg\[binary\]\>=3.1,\<3.3, Flask\>=2.3,\<3.0, gunicorn\>=21,\<22.  
* requirements-dev.txt — Present. Declares test dependencies: jsonschema==4.23.0, pytest\>=7.4,\<9.0, pytest-cov\>=4.1,\<5.0, pytest-mock\>=3.12,\<4.0.  
* run\_flask.py — Present. Main-module search showed ./run\_flask.py:24:if \_\_name\_\_ \== "\_\_main\_\_":.  
* AGENTS.md — Present. Top-level listing included AGENTS.md.

### Root discipline capture: top-level roots that look like truth/evidence/tool homes

Observed roots include:

* audit/ — QA/gates/ops evidence.  
* artifacts/ — generated snapshots, logs, proofs, mirrors, CLI captures, DB artifacts.  
* docs/ — PF canon, schemas, endpoint catalog, evidence human index.  
* tools/ — evidence and QA generation/validation tools.  
* scripts/ — operational, DB, ingest, release, QA, validation scripts.  
* ci/ and .github/ — CI gates and workflows.  
* catalog/ — release manifest home; top listing included catalog.  
* schemas/, goldens/, fixtures/, parity/, proofs/, reports/, validation/, scan\_reports/ — root-level artifact/support homes observed in listing.

## Packaging and Entrypoints

### Packaging / build configuration

* Python packaging: pyproject.toml.  
  * Declares build backend: \[build-system\] requires \= \["setuptools\>=68", "wheel"\], build-backend \= "setuptools.build\_meta".  
  * Declares project: name \= "glow-hdengine", version \= "0.0.0", requires-python \= "\>=3.10", dependencies \= \[\].  
  * Declares console script: hdctl \= "engine.cli.main:cli".  
  * Declares packages: \[tool.setuptools.packages.find\] where \= \["."\] include \= \["engine\*", "adapter\*", "presenter\*"\].  
* Runtime dependency file: requirements.txt contains Flask, gunicorn, psycopg.  
* Dev dependency file: requirements-dev.txt contains pytest/jsonschema-related dependencies.  
* Not found: setup.cfg, setup.py, package.json, pnpm-workspace.yaml, yarn.lock, poetry.lock, uv.lock. Negative proof in appendix.

### Entrypoint inventory

* HTTP app factory / server startup  
  * adapter/app.py: imports and instantiates create\_app; snippet lines 2–5: from adapter.wsgi import create\_app and app \= create\_app().  
  * adapter/factory.py:create\_app: lines 4–7 create Flask(\_\_name\_\_) and app.register\_blueprint(bp, url\_prefix="").  
  * adapter/http\_reader.py:create\_app: lines 944–955 create Flask app, register bp at url\_prefix="", then register compat\_blueprint.  
  * adapter/http\_reader.py main-module entry exists at line 994 per main-module search.  
  * run\_flask.py main-module entry exists at line 24 per main-module search.  
* CLI console script  
  * pyproject.toml: hdctl \= "engine.cli.main:cli".  
  * engine/cli/main.py:cli: lines 239–259 parse argv and dispatch to subcommand handler.  
  * engine/cli/\_\_main\_\_.py: main-module search showed ./engine/cli/\_\_main\_\_.py:14:if \_\_name\_\_ \== "\_\_main\_\_":.  
* Evidence/index scheduled or background-style jobs  
  * tools/evidence/update\_evidence\_index.py:main: search output showed def main(argv: list\[str\] | None \= None) \-\> None at line 993 and constants HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH at lines 24–28.  
  * tools/evidence/orientation\_demo.py:main: search output showed def main(argv: list\[str\] | None \= None) \-\> None at line 170 and writes ORIENTATION\_PATH.write\_text at line 167\.  
  * scripts/bodygraph/run\_refresh\_worker.py: main-module search showed scripts/bodygraph/run\_refresh\_worker.py:290:if \_\_name\_\_ \== "\_\_main\_\_":.  
  * scripts/db/run\_retention\_job.py: main-module search showed scripts/db/run\_retention\_job.py:88:if \_\_name\_\_ \== "\_\_main\_\_".

## Engine Modules

### Sampler

* engine/sampler/core.py  
  * Module docstring describes “Pure-compute sampler core” and says it “enforces zero-weight rules,” “eligibility checks,” and deterministic ranking at lines 3–18.  
  * Primary data structures:  
    * ViewerProfile lines 30–35: minimal viewer state with person\_uid.  
    * CandidateFeatures lines 38–48: normalized candidate state with weight, compat\_score, band, diversity\_key, is\_recent, categories.  
    * SamplerConfig lines 51–59: min score, excluded/allowed bands, diversity key requirement, band priority.  
    * CandidatePoolEntry, CandidatePool, RankedCandidate, RankedCandidates lines 62–92.  
  * Primary functions:  
    * build\_candidate\_pool lines 126–151 filters zero-weight and ineligible candidates and returns CandidatePool.  
    * \_compare\_entries lines 159–167 orders by weight, compat score, band rank, then compare\_ids.  
    * rank\_candidates lines 170–193 sorts candidates; docstring lines 171–175 states no randomness/clocks/external state are consulted.  
    * sample\_and\_rank lines 196–204 builds pool then ranks.

### Core compute

* engine/compat/compute.py  
  * band\_for lines 17–21 maps numeric score to Cool, Open, Warm, Glow using thresholds.  
  * \_score\_for lines 23–30 derives category score from stable SHA-256 of pair\_key:category, applies viewer weight, clamps/rounds.  
  * compat\_public lines 36–48 normalizes pair (normalize\_pair), builds category records in CATEGORIES\_ORDER\_V1, and returns categories plus meta.  
  * conjunction\_public\_resolved appears in line excerpts around 162–220: it accepts env, local lookup, resolves parties, and calls resolve\_bodygraph(... source="vendor" ...) on local miss.  
* engine/compat/categories.py  
  * CATEGORIES\_ORDER\_V1 lines 8–19 defines ordered category IDs: heat, harmony, communication, etc.; line 20 defines CATEGORIES\_SET\_V1 \= set(CATEGORIES\_ORDER\_V1).  
* engine/compat/ordering.py  
  * Imported by compute.py line 9: normalize\_pair, pair\_key; this is the AB↔BA normalization seam used by compat\_public.  
* engine/runtime/public.py  
  * Called by CLI and HTTP via emit\_reader\_public\_bytes / emit\_reader\_public\_envelope; adapter/http\_reader.py imports emit\_reader\_public\_bytes at line 9 and engine/cli/main.py imports emit\_reader\_public\_envelope at line 36\.

### Determinism hazards inventory

Observed hazards in sampled engine paths:

* Current time in BodyGraph ingest: engine/bodygraph/ingest.py imports time line 5; \_utc\_iso uses time.strftime(... time.gmtime()) lines 72–73; ingest\_vendor\_bodygraph uses time.monotonic() at lines 131, 140, 176\.  
* File I/O in BodyGraph ingest: \_append\_jsonl creates directories and appends to files at lines 62–67; ingest logs to SUCCESS\_LOG, RETRY\_LOG, and CANON\_COMPARE\_LOG declared lines 48–51.  
* Network call in vendor client: engine/bodygraph/vendor\_client.py:fetch builds urllib.request.Request and calls self.\_request(req, timeout) lines 318–320.  
* Network / DB provider IO: engine/db/providers/bridge\_provider.py uses urllib.request.urlopen(req, timeout=10) lines 39–40; engine/db/providers/psycopg\_provider.py imports psycopg and connects with psycopg.connect(self.\_dsn, connect\_timeout=5) lines 25–29.  
* Current process time in HTTP reader: adapter/http\_reader.py sets \_PROCESS\_STARTED\_AT \= datetime.now(timezone.utc) line 22 and exposes it in /ops/probe/env payload line 528\.  
* File I/O in CLI: engine/cli/main.py:\_read\_file uses Path(path).read\_text lines 983–989; \_dump\_reader\_bytes writes bytes at lines 553–556; admin dumps call canon\_dump lines 586–589.  
* No randomness observed in sampled sampler path: engine/sampler/core.py:rank\_candidates docstring states “No randomness, clocks, or external state are consulted” lines 171–175, and implementation uses sorted(...) line 179\.

Sampled paths reviewed for this inventory: engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/ingest.py, engine/bodygraph/vendor\_client.py, engine/db/adapter.py, engine/db/providers/bridge\_provider.py, engine/db/providers/psycopg\_provider.py, engine/cli/main.py, adapter/http\_reader.py.

## Adapter / HTTP Surfaces

### Route registration map

* Reader/internal/dev/ops blueprint  
  * adapter/http\_reader.py:get\_reader\_bp creates Blueprint("reader\_v1", \_\_name\_\_) at line 328\.  
  * Routes:  
    * GET /reader → reader\_v1, lines 330–331.  
    * GET /api/aux/narrative and GET /aux/narrative → aux\_narrative, lines 392–394.  
    * POST /reader → reader\_v1\_post, lines 441–444.  
    * GET /ops/db/unavailable → ops\_db\_unavailable, lines 469–470.  
    * GET|POST /ops/rails/refusal → ops\_rails\_refusal, lines 514–515.  
    * GET /ops/probe/env → ops\_probe\_env, lines 522–523.  
    * POST /internal/dev/sampler → dev\_sampler\_internal, lines 698–699.  
    * GET /dev/sampler/conjunction → dev\_sampler\_conjunction, lines 766–767.  
    * GET /dev/reader/conjunction → dev\_reader\_conjunction, lines 774–775.  
    * GET /dev/writer/conjunction → dev\_writer\_conjunction, lines 782–783.  
    * GET|HEAD /internal/version → internal\_version, lines 874–875.  
    * POST|HEAD|OPTIONS /ops/writer/diagnostic → diagnostic\_writer, diagnostic\_writer\_head, diagnostic\_writer\_options, lines 898–940.  
  * Mounting:  
    * adapter/http\_reader.py:create\_app registers bp at url\_prefix="" lines 944–949.  
    * adapter/factory.py:create\_app registers bp at url\_prefix="" lines 4–7.  
* Compat blueprint  
  * engine/http/compat\_handler.py defines compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1") line 11\.  
  * Routes:  
    * GET /api/compat/v1 → get\_ids\_only, lines 82–88.  
    * POST /api/compat/v1 → post\_json, lines 90–127.  
    * HEAD /api/compat/v1 → post\_json\_head, lines 130–132.  
    * OPTIONS /api/compat/v1 → post\_json\_options, lines 135–137.  
  * Mounting:  
    * adapter/http\_reader.py:create\_app registers compat\_blueprint lines 953–955.

### Surface classification

* Reader-like JSON success  
  * adapter/http\_reader.py:reader\_v1 emits reader public bytes through emit\_fn(...) lines 357–363 and returns JSON response lines 385–390.  
* Aux/narrative  
  * adapter/http\_reader.py:aux\_narrative calls emit\_public\_aux lines 406–415 and returns text/plain; charset=utf-8 headers lines 417–431.  
* Admin/internal  
  * adapter/http\_reader.py:internal\_version builds internal version payload lines 883–895 with Cache-Control: no-store.  
  * engine/http/compat\_handler.py:post\_json is cataloged as internal admin in docs/ENDPOINTS\_CATALOG.json sample: classification: internal\_admin, path: /api/compat/v1.  
  * adapter/http\_reader.py:diagnostic\_writer handles /ops/writer/diagnostic lines 898–913.  
* Dev/diagnostic harness  
  * adapter/http\_reader.py:dev\_sampler\_internal docstring says “Dev-only sampler harness” lines 698–706.  
  * Dev conjunction routes at lines 766–788 are gated through \_dev\_admin\_gate lines 541–547.

### Transport semantics hooks

* HEAD vs GET parity  
  * adapter/http\_reader.py:reader\_v1 handles HEAD parity at lines 377–383, setting Content-Length to len(body).  
  * adapter/http\_reader.py:internal\_version handles HEAD at lines 886–890, setting content length equal to GET body bytes.  
  * engine/http/compat\_handler.py explicitly returns writer HEAD response for compat at lines 68–75 and lines 130–132.  
* Conditional responses / 304  
  * adapter/http\_reader.py:reader\_v1 parses If-None-Match and returns 304 if ETag matches lines 364–375.  
* ETag generation / quoting  
  * adapter/http\_reader.py:reader\_v1 builds quoted ETag via etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"" line 364\.  
  * adapter/http\_reader.py:aux\_narrative calls resp.set\_etag(digest) and then sets resp.headers\["ETag"\] \= f'"{digest}"' lines 429–431.  
* Cache-Control  
  * Reader 200 helper \_set\_reader\_200\_headers sets Cache-Control: private, max-age=0, must-revalidate lines 28–31.  
  * Writer responses set Cache-Control: no-store in \_emit\_writer\_response lines 75–79.  
  * Compat writer payload sets Cache-Control: no-store in engine/http/compat\_handler.py lines 14–20.  
* Content-Type  
  * Reader helper sets Content-Type: application/json; charset=utf-8 lines 28–30.  
  * Aux narrative uses Content-Type: text/plain; charset=utf-8 lines 417–425.  
  * Writer response sets Content-Type: application/json; charset=utf-8 lines 75–78.

## Presenter / Emitter

* engine/presenter/emitter.py  
  * emit\_public lines 6–13 delegates to canon.sercanon and documents LF-terminated UTF-8, sorted keys by default.  
  * emit\_public\_with\_envelope lines 16–20 returns canonical bytes and original envelope.  
  * emit\_compact\_json lines 23–28 is a compatibility alias.  
  * Callers:  
    * HTTP reader imports emit\_public at adapter/http\_reader.py line 7\.  
    * Compat HTTP imports emit\_public at engine/http/compat\_handler.py line 5\.  
    * CLI imports from engine.presenter import emitter at engine/cli/main.py line 35\.  
    * BodyGraph ingest imports from engine.presenter import emitter at engine/bodygraph/ingest.py line 14\.  
* engine/serializer/canon.py  
  * sercanon lines 6–15 delegates to stable serializer and documents UTF-8 bytes, ensure\_ascii=False, sorted keys by default, compact separators, exactly one trailing newline.  
* engine/runtime/public.py  
  * Runtime reader emitter is re-exported by engine/runtime/\_\_init\_\_.py lines 1–3: emit\_reader\_public\_bytes, emit\_reader\_public\_envelope.  
  * HTTP reader imports emit\_reader\_public\_bytes line 9; CLI imports emit\_reader\_public\_envelope line 36\.

Multiple emitters exist by usage:

* Public canonical JSON emitter: engine/presenter/emitter.py.  
* Canonical serializer: engine/serializer/canon.py.  
* Reader-specific runtime emitter: engine/runtime/public.py, exposed via engine/runtime/\_\_init\_\_.py.  
* Top-level presenter compare script: presenter/json\_canon\_compare.py appears as a runnable script from main-module search.

## CLI Surfaces

### Entrypoints and parser

* Console script: hdctl declared in pyproject.toml as engine.cli.main:cli.  
* Parser: engine/cli/main.py:\_build\_parser lines 73–84 creates argparse.ArgumentParser(prog="hdctl", ...) and required subparsers.  
* Dispatcher: engine/cli/main.py:cli lines 239–259 handles \--version, parses args, and calls handler. Missing/parse errors return 64 at lines 251–257; CliError writes code to stderr and returns err.exit\_code lines 260–262.

### Relevant commands

* hdctl showcompat  
  * Parser lines 85–131 define subcommand and arguments:  
    * \--pair-file, \--a-file, \--b-file, \--a, \--b lines 90–94.  
    * \--dump-reader lines 96–99.  
    * \--dump-admin-dir lines 100–104.  
    * \--source {db,vendor,auto} lines 106–109.  
    * \--conjunction lines 111–117.  
    * \--viewer-prefs-file lines 119–122.  
    * \--user-a, \--user-b, birth fields lines 123–130.  
  * Handler: show.set\_defaults(handler=showcompat) line 131\.  
  * Call chain facts:  
    * Loads viewer prefs via \_load\_viewer\_prefs line 675\.  
    * Conjunction path calls conjunction\_public\_resolved lines 810–820 and emits emitter.emit\_public lines 821–824.  
    * Non-conjunction path computes compat\_public lines 833–841 and emits emitter.emit\_public(compat\_payload) line 848\.  
    * It also builds reader bytes with emit\_reader\_public\_envelope lines 850–856.  
  * Output:  
    * Writes reader dump if \--dump-reader line 858–859.  
    * Writes admin dumps through \_emit\_admin\_dumps lines 861–872; \_emit\_admin\_dumps writes .bodygraph.json, .composite.bodygraph.json, .compat.proof.json lines 586–589.  
    * Prints canonical bytes to stdout via \_emit\_stdout\_bytes(compat\_bytes) line 874\.  
    * \_emit\_stdout\_bytes rejects missing LF/CRLF and writes to sys.stdout.buffer lines 559–564.  
* hdctl aux-preview  
  * Parser lines 133–144 defines \--category, \--band, \--perspective, \--pair-file, \--show-narrative, \--admin-out.  
  * Handler aux\_preview emits narrative bytes to stdout lines 624–638 and writes admin sidecar via canon\_dump(args.admin\_out, sidecar) lines 640–655.  
* hdctl bg:resolve  
  * Parser lines 145–171 defines required \--user, \--source, \--upsert, \--dry-run, birth args.  
  * Handler bg\_resolve requires birth tuple for vendor source lines 218–223, calls resolve\_bodygraph lines 224–233, writes public JSON to stdout lines 234–236.  
* hdctl dev:sampler  
  * Parser lines 173–190 defines required \--viewer, required \--candidates-file, optional \--seed.  
  * Handler dev\_sampler\_run lines 972–980 gates dev/admin env, loads candidates, calls sample\_and\_rank, and emits serializer output.  
  * \_emit\_sampler\_output writes sercanon(payload) to stdout line 969\.

## Vendor Seam & BodyGraph Storage

### Vendor client

* engine/bodygraph/vendor\_client.py:HdApiClient.from\_env  
  * Reads env names HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, RELEASE\_ID lines 238–255.  
  * Missing config raises VendorError("PROVIDER\_CONFIG\_MISSING", ...) lines 243–249.  
* Request shaping  
  * build\_request lines 270–301 requires birthdate, birthtime, location, transforms date to vendor format lines 275–285, serializes JSON with sorted keys/compact separators plus newline line 287, hashes fingerprint line 288, sets headers including HD-Api-Key, HD-Geocode-Key, User-Agent lines 289–295, and targets f"{self.\_base\_url}/bodygraphs" line 297\.  
* Response fetch/parsing  
  * fetch lines 303–335 performs POST request lines 318–320, maps non-200 to vendor errors lines 323–329, parses JSON lines 330–333, logs success line 334\.

### BodyGraph persistence/caching

* Resolution control flow  
  * engine/bodygraph/resolver.py:resolve\_bodygraph lines 36–46 takes user\_id, source, upsert, dry\_run, env, and optional birth fields.  
  * For source \== "vendor", it calls \_resolve\_vendor lines 70–80.  
  * For non-vendor auto/db, it returns stub DB envelope with note “BodyGraph DB resolution is stubbed for Phase S8a; no IO performed” lines 82–91.  
* Persistence  
  * engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph calls DBAccess.for\_current\_env() line 166, counts rows line 167, persists bodygraph line 168, fetches payload line 171, and compares canonical emitted bytes lines 172–175.  
  * \_persist\_bodygraph inserts into hde.body\_graphs with columns user\_id, vendor, vendor\_version, input\_fingerprint, payload lines 214–229.  
* Cache / key formation visible  
  * adapter/cache\_keys.py:build\_cache\_key returns orientation-safe tuple (min\_user, max\_user, release\_id, fp\_min, fp\_max) lines 10–17.  
  * engine/bodygraph/ingest.py:\_idempotency\_key is invoked at line 138 to combine user/vendor/version/fingerprint; exact function body was not included in sampled excerpt.  
* DB provider layer  
  * engine/db/adapter.py:DBAccess.for\_current\_env reads DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD lines 131–137.  
  * Provider order defaults to \["psycopg", "bridge"\] lines 147–153.  
  * Bridge allowed if forced, dev env, or prod allow flag line 158\.  
  * Selection snapshot writes to default artifacts/db\_bridge/adapter\_selection.snapshot.json line 124 and \_write\_snapshot lines 73–78.  
  * engine/db/providers/psycopg\_provider.py executes SQL through psycopg lines 25–29 and query/exec/tx methods lines 58–108.  
  * engine/db/providers/bridge\_provider.py uses HTTPS only; rejects non-https bridge URL lines 69–75 and sends JSON requests lines 79–113.

### Offline / vendor-required posture

* Vendor SAFE rails enforcement  
  * engine/bodygraph/ingest.py checks SAFE\_MODE and ALLOW\_NETWORK lines 124–130; safe mode raises PROVIDER\_REFUSED, no network raises PROVIDER\_NETWORK\_BLOCKED.  
  * engine/bodygraph/resolver.py:\_resolve\_vendor returns error payload for SAFE rails closed lines 105–117 and network disabled lines 118–127.  
  * adapter/http\_reader.py:\_emit\_conjunction\_response constructs rails env from SAFE\_MODE and ALLOW\_NETWORK lines 643–646 and maps VendorError to writer error response lines 669–684.  
* Determinism env pins  
  * engine/runtime/determinism\_env.py defines expected rails LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0 lines 9–15 and raises mismatch at lines 50–55.

## Evidence, Indices, Catalogs

### Evidence homes inventory

Observed evidence-like homes from directory listing:

* docs/evidence/ — human evidence index and hash. Proof: tooling constants HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json" and HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256" in tools/evidence/update\_evidence\_index.py lines 24–25.  
* docs/ENDPOINTS\_CATALOG.json — endpoint catalog. JSON shape proof: loaded as dict with keys endpoints, success\_endpoints; sample endpoint contains path, method, classification, blueprint\_module, env\_gate.  
* artifacts/ — broad generated/mixed evidence home. Directory proof includes artifacts/evidence\_index.jsonl, artifacts/proofs/success\_get.txt, artifacts/proofs/success\_head.txt, artifacts/bodygraph/\*.path\_proof.txt, artifacts/db/\*, artifacts/cli/showcompat.  
* artifacts/evidence\_index.jsonl — machine mirror. Tooling constant MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl" at tools/evidence/update\_evidence\_index.py line 26\.  
* audit/ — QA and gate home. Directory proof includes audit/gates/canonical\_json, audit/gates/evidence\_index\_snapshot, audit/qa/hde-epic020 through audit/qa/hde-epic031.  
* audit/qa/\*\* — epic-specific QA evidence logs. Directory proof lists many epic folders, including audit/qa/hde-epic027, audit/qa/hde-epic030, audit/qa/hde-epic031.  
* artifacts/proofs/ — proof snapshots. Listing proof includes artifacts/proofs/success\_get.txt, artifacts/proofs/success\_head.txt, and path-proof siblings.  
* artifacts/ops/internal\_version/ — internal version HTTP proof snapshots. Listing proof includes body\_get.json.path\_proof.txt, headers\_get.txt.path\_proof.txt, headers\_head.txt.path\_proof.txt, conditional header proofs, and request-chain manifest proof.

Generated vs hand-authored posture by pattern only:

* Generated-looking: .path\_proof.txt, .sha256, .jsonl, logs, snapshots under artifacts/ and audit/gates/.  
* Mixed: docs/ contains hand-authored canon/docs plus generated docs/evidence/INDEX.json and endpoint catalog.

### Evidence index structures

* docs/evidence/INDEX.json  
  * Present. Head shows JSON array records with keys such as artifact\_key, discovered\_physical\_path, epic\_id, notes, produced\_at\_utc, record\_type, sha256, tokens.  
* docs/evidence/INDEX.sha256  
  * Present. Hash gate reads it; ci/checks/check\_evidence\_index\_hash.sh lines 4–10 check both files and compare sha256 over INDEX.json.  
* artifacts/evidence\_index.jsonl  
  * Present. tools/evidence/validate\_evidence\_paths.py reads ROOT / "artifacts" / "evidence\_index.jsonl" lines 38–40 and errors if missing.  
  * ci/checks/check\_mirror\_schema.sh uses index\_path \= Path("artifacts/evidence\_index.jsonl") lines 72–74.  
* Regeneration / validation tooling  
  * tools/evidence/update\_evidence\_index.py declares HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH, MIRROR\_SHA\_PATH lines 24–28 and writes mirror/index/hash in later lines 1042–1052.  
  * tools/evidence/orientation\_demo.py reads mirror lines 34 and 151, writes orientation path line 167\.  
  * ci/checks/check\_evidence\_index\_hash.sh validates INDEX.sha256 against INDEX.json lines 4–10.  
  * ci/checks/check\_mirror\_schema.sh validates mirror schema lines 67–74.

### Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * Present. Loaded as dict with keys endpoints, success\_endpoints; sample records include a7\_eligible, blueprint\_module, classification, description, env\_gate, method, path, rails\_profile.  
  * Sample record: path: /api/compat/v1, method: POST, blueprint\_module: engine.http.compat\_handler, classification: internal\_admin.  
* artifacts/audit/ENDPOINTS\_CATALOG.json  
  * Present. Same loaded shape: dict with endpoints, success\_endpoints; sample endpoint matches docs catalog sample.  
* References  
  * Tool/test/doc search found many ENDPOINTS\_CATALOG references in docs/PF canon and tooling; exact code-reader references beyond the loaded catalog shape were not exhaustively expanded in this read-only snapshot.

### Proof / snapshot artifacts

* artifacts/proofs/success\_get.txt and artifacts/proofs/success\_head.txt  
  * Present by find output, with .path\_proof.txt siblings.  
* artifacts/proofs/success\_304.txt.path\_proof.txt  
  * Present by find output.  
* artifacts/ops/internal\_version/\*  
  * Present proof set includes headers\_get.txt.path\_proof.txt, headers\_head.txt.path\_proof.txt, cond\_if\_none\_match\_headers.txt.path\_proof.txt, request\_chain\_manifest.json.path\_proof.txt.  
* Producer evidence  
  * PF canon references in search output name artifacts/proofs/success\_get.txt and success\_head.txt, but this audit did not expand a single producing script for those specific filenames beyond file existence and PF/tool references.

## Tests, QA Harness, CI/Checks

### Tests map

Test roots are under tests/; repo does not uniformly label unit/integration/contract in filenames, so categories below are based on path names and test names only.

* Adapter / HTTP reader / compat  
  * tests/adapter/test\_reader\_parity.py, tests/adapter/test\_headers\_and\_determinism.py, tests/compliance/test\_reader\_etag\_and\_conditional.py, tests/compliance/test\_reader\_etag\_compression\_invariance.py.  
  * Compat HTTP tests: tests/adapter/test\_compat\_http\_dev.py, tests/adapter/test\_compat\_http\_parity.py, tests/adapter/test\_compat\_writer\_transport.py.  
* CLI outputs  
  * tests/cli/test\_cli\_canonical\_bytes.py, tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/cli/test\_cli\_usage\_and\_errors.py, tests/cli/test\_cli\_file\_inputs.py, tests/cli/test\_showcompat\_sources.py.  
* Canonical JSON / bytes  
  * tests/compat/test\_compat\_public\_lf\_bom.py, tests/compat/test\_cli\_public\_bytes\_identity.py, tests/canon/test\_report\_determinism.py, tests/cli/test\_serializer\_guards.py.  
* Determinism gates  
  * tests/core/test\_engine\_core\_determinism.py, tests/cli/test\_cli\_env\_pins\_epic021.py, tests/evidence/test\_sanity\_pipeline.py, tests/evidence/test\_evidence\_index\_env.py.  
* Evidence index / catalogs  
  * tests/evidence/test\_evidence\_index\_snapshot.py, tests/evidence/test\_machine\_mirror\_self\_proof.py, tests/evidence/test\_orientation\_demo.py, tests/evidence/test\_sanity\_evidence\_index.py, tests/ops/test\_evidence\_index.py referenced by CI.  
* Vendor / DB  
  * tests/bodygraph/test\_ingest.py, tests/bodygraph/test\_resolver\_vendor.py, tests/bodygraph/test\_vendor\_client.py.  
  * tests/db/test\_adapter\_contract.py, tests/db/test\_adapter\_selection.py, tests/db/test\_no\_import\_time\_connect.py, tests/db/test\_rw\_smoke\_guard.py.

Fixture/vendor reliance evidence:

* Vendor client tests exist under tests/bodygraph/test\_vendor\_client.py; DB tests include test\_no\_import\_time\_connect.py, indicating explicit coverage for import-time DB behavior by filename.  
* CI sets SAFE\_MODE: "1" and ALLOW\_NETWORK: "0" in jobs, e.g. .github/workflows/ci.yml lines 6–12 and 90–95.

### CI workflows

* .github/workflows/ci.yml  
  * Workflow name: ci, trigger on: \[push, pull\_request\] lines 1–2.  
  * Job test lines 3–63:  
    * Sets closed rails env lines 6–12.  
    * Installs requirements and editable package lines 18–22.  
    * Runs ci/checks/check\_env\_pins.sh line 23\.  
    * Runs serializer/emitter guards lines 25–27.  
    * Runs canonical JSON gate line 29\.  
    * Runs evidence index update/check lines 31–34.  
    * Runs evidence hash, bridge consistency, mirror schema, final LF checks lines 52–55.  
    * Runs selected pytest suites lines 59–62.  
  * Job compat-conj-pr01-closure lines 63–86:  
    * Runs compat identity-hash and evidence-index pytest commands lines 83–86.  
  * Job epic020 lines 87–117:  
    * Runs EPIC020 acceptance pytest suite: adapter JSON schema, CLI usage/errors/canonical/showcompat, internal version, QA docs lines 107–117.  
  * Job compat-http-epic020 lines 118–142:  
    * Runs tests/adapter/test\_compat\_http\_dev.py and test\_compat\_http\_parity.py.  
  * Job epic020-evidence-bundles lines 143–167:  
    * Builds EPIC020 bundles, updates evidence index, checks mirror schema, runs bundle index integration test.  
  * Job sanity-pipeline lines 168–187:  
    * Runs python tools/evidence/run\_sanity\_pipeline.py.

### Script/check inventory

Representative QA-relevant checks and scripts:

* ci/checks/check\_env\_pins.sh — invoked by CI line 23 and many jobs; enforces closed rails.  
* ci/checks/check\_evidence\_index\_hash.sh — lines 4–10 check docs/evidence/INDEX.json against INDEX.sha256.  
* ci/checks/check\_mirror\_schema.sh — validates artifacts/evidence\_index.jsonl; search output shows index\_path \= Path("artifacts/evidence\_index.jsonl").  
* ci/checks/check\_final\_lf.sh — invoked by CI line 55\.  
* ci/checks/check\_bridge\_consistency.py — loads artifacts/db\_bridge/adapter\_selection.snapshot.json, artifacts/runtime/env\_connectivity.snapshot.json, and artifacts/db\_bridge/provider\_parity.proof.json lines 44–48.  
* tools/evidence/update\_evidence\_index.py — maintains human index, hash sentinel, machine mirror lines 24–28.  
* tools/evidence/orientation\_demo.py — reads mirror and writes orientation artifact; search snippets show mirror reads and ORIENTATION\_PATH.write\_text.  
* tools/evidence/validate\_evidence\_paths.py — checks artifacts/evidence\_index.jsonl exists lines 38–40.  
* tools/evidence/run\_canonical\_json\_gate.py — invoked by CI line 29\.  
* tools/evidence/run\_sanity\_pipeline.py — invoked by CI line 187\.  
* tools/cli/serializer\_grep\_guard.py and tools/cli/emitter\_symbol\_proof.py — invoked by CI lines 26–27.  
* tools/qa/run\_hde\_epic024\_harness.py — search output shows commands for pytest readiness, env pins, canonical JSON gate, sampler evidence, evidence index, mirror schema, final LF checks around lines 926–1018.  
* scripts/ingest/run\_vendor\_ingest.py — main-module search showed an executable ingest script at line 152\.  
* scripts/bodygraph/run\_refresh\_worker.py — main-module search showed background/worker-style entry at line 290\.  
* scripts/db/run\_retention\_job.py — main-module search showed DB retention job entry at line 88\.

## Flows & Call Chains

### 1\. Reader success flow (HTTP)

adapter/http\_reader.py:create\_app → adapter/http\_reader.py:get\_reader\_bp → adapter/http\_reader.py:reader\_v1 → engine/runtime:emit\_reader\_public\_bytes → Response(body, status=200)

* create\_app registers bp at root lines 944–949.  
* get\_reader\_bp defaults emit\_fn \= emit\_reader\_public\_bytes lines 321–328.  
* reader\_v1 requires v=1, APP\_ENV=dev, and a/b params lines 332–340.  
* It loads chart files via \_safe\_load\_chart lines 342–343.  
* It emits body bytes through emit\_fn(...) lines 357–363.  
* It sets quoted SHA-256 ETag line 364 and returns 200 with JSON headers/content length lines 385–390.

### 2\. Compat API flow (HTTP)

adapter/http\_reader.py:create\_app → engine/http/compat\_handler.py:compat\_blueprint → post\_json → engine.compat.compute:compat\_public → engine.presenter.emit\_public → \_writer\_payload

* compat\_blueprint is declared with URL prefix /api/compat/v1 line 11\.  
* App registers compat\_blueprint lines 953–955.  
* post\_json rejects prod with ERR\_NOT\_FOUND lines 92–94.  
* It accepts a/b or a\_id/b\_id and rejects mixing lines 95–115.  
* It validates/normalizes viewer prefs lines 116–120.  
* It calls compat\_public lines 121–124.  
* It wraps output with \_writer\_payload, which emits public JSON and sets no-store/no ETag/content length lines 14–20.

### 3\. CLI showcompat / compat preview flow

pyproject.toml hdctl → engine/cli/main.py:cli → \_build\_parser/showcompat → showcompat → compat\_public / emit\_reader\_public\_envelope → emitter.emit\_public → \_emit\_stdout\_bytes

* Console script maps hdctl to engine.cli.main:cli.  
* Parser defines showcompat and file/source/conjunction args lines 85–131.  
* showcompat loads viewer prefs and engine identity lines 674–676.  
* Non-conjunction path canonicalizes pair lines 826–829, computes TS features lines 830–832, calls compat\_public lines 833–841.  
* It emits compat payload through emitter.emit\_public line 848\.  
* It also builds reader envelope via emit\_reader\_public\_envelope lines 850–856.  
* It optionally writes reader/admin dump files lines 858–872.  
* It prints stdout bytes through \_emit\_stdout\_bytes line 874; \_emit\_stdout\_bytes enforces LF/no CRLF lines 559–564.

### 4\. Vendor acquisition flow (BodyGraph ingest)

engine/cli/main.py:bg\_resolve or showcompat source=vendor → engine.bodygraph.resolver.resolve\_bodygraph → \_resolve\_vendor → ingest\_vendor\_bodygraph → HdApiClient.from\_env/build\_request/fetch → DBAccess.for\_current\_env → \_persist\_bodygraph

* bg\_resolve calls resolve\_bodygraph with source/upsert/dry-run/env/birth fields lines 224–233.  
* resolve\_bodygraph dispatches vendor source to \_resolve\_vendor lines 70–80.  
* \_resolve\_vendor blocks SAFE rails closed or network disabled lines 105–127.  
* ingest\_vendor\_bodygraph blocks safe mode/no network lines 124–130.  
* It builds vendor client from env and fetches request lines 132–134.  
* It canonicalizes vendor payload and hashes it lines 135–138.  
* It writes DB row via \_persist\_bodygraph lines 166–169 and SQL insert lines 214–229.  
* It logs success/canonical compare via \_append\_jsonl lines 177–198.

### 5\. Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py:main → writes docs/evidence/INDEX.json / INDEX.sha256 / artifacts/evidence\_index.jsonl → tools/evidence/orientation\_demo.py \--check → ci/checks/check\_evidence\_index\_hash.sh → ci/checks/check\_mirror\_schema.sh

* Tool constants define human index, hash sentinel, mirror, mirror sha lines 24–28.  
* Search snippets show writes for index hash/mirror at lines 1042–1052.  
* orientation\_demo.py reads MIRROR\_PATH lines 34 and 151 and writes orientation artifact line 167\.  
* CI runs update/check/orientation lines 31–34.  
* CI runs evidence hash check line 52 and mirror schema line 54\.  
* check\_evidence\_index\_hash.sh compares INDEX.sha256 to sha256sum docs/evidence/INDEX.json lines 4–10.

### 6\. Dev sampler HTTP flow

adapter/http\_reader.py:create\_app → dev\_sampler\_internal → ViewerProfile/CandidateFeatures → sample\_and\_rank → emit\_public → Response

* Route /internal/dev/sampler is registered lines 698–699.  
* Docstring states dev-only sampler harness lines 700–706.  
* \_dev\_admin\_gate allows only dev, test, local APP\_ENV lines 541–547.  
* Handler reads JSON with allowed keys viewer\_id, candidate\_ids, seed lines 715–718.  
* It builds ViewerProfile and CandidateFeatures list lines 738–750.  
* It calls sample\_and\_rank line 752\.  
* It emits response with emit\_public(... sort\_keys=True) and no-store/no ETag lines 760–764.

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Expected split directories engine/, adapter/, and presenter/ all exist, but presenter code exists both as top-level presenter/ scripts and as engine/presenter/ package.  
  Proof: package include includes presenter\* in pyproject.toml; code proof engine/presenter/emitter.py lines 6–13 defines canonical emitter; main-module search shows presenter/json\_canon\_compare.py:112:if \_\_name\_\_ \== "\_\_main\_\_".  
  Impact: This creates ambiguity about whether “presenter” refers to top-level scripts or package-level runtime emitter.

### Surface drift

* Observed: /reader is mounted at root by adapter/http\_reader.py:create\_app, while compat is mounted under /api/compat/v1.  
  Proof: app.register\_blueprint(bp, url\_prefix="") lines 944–949; compat\_blueprint \= Blueprint(... url\_prefix="/api/compat/v1") line 11\.  
  Impact: This creates ambiguity about API prefix conventions across reader and compat surfaces.

### Evidence drift

* Observed: Evidence-like outputs are spread across docs/evidence, artifacts, audit/gates, audit/qa, artifacts/audit, artifacts/proofs, artifacts/ops/internal\_version.  
  Proof: directory listing shows docs/evidence, artifacts/proofs, artifacts/ops/internal\_version, audit/gates, audit/qa/hde-epic020 through hde-epic031.  
  Impact: This creates ambiguity about evidence home boundaries without consulting the governing tools/catalogs.

### Determinism drift

* Observed: Sampler core is deterministic by code comment and implementation, while BodyGraph ingest/vendor/DB paths include time, file IO, network IO, and DB IO.  
  Proof: sampler docstring says “No randomness, clocks, or external state are consulted” lines 171–175; ingest uses time.monotonic() lines 131/140/176 and appends JSONL lines 62–67; vendor fetch calls request lines 318–320.  
  Impact: Determinism depends on which layer is invoked: pure sampler/compat paths differ from acquisition/persistence paths.

### Vendor seam drift

* Observed: Vendor acquisition is under engine/bodygraph/\*, and compat conjunction resolution in engine/compat/compute.py can call resolve\_bodygraph(... source="vendor" ...) on local miss.  
  Proof: engine/compat/compute.py imports resolve\_bodygraph line 5 and calls it with source="vendor" lines 192–197 in the sampled excerpt; vendor client is engine/bodygraph/vendor\_client.py.  
  Impact: This creates ambiguity about whether vendor seam is outside the engine package or inside engine subpackages.

### Path-case drift

* Observed: Lowercase epic QA paths are present under audit/qa/hde-epic0xx; root also contains mixed-case/top-level report filenames such as EPIC023\_D12\_close\_pack\_manifest\_FINAL\_EVIDENCE.md and Approved Remediation Plan EPIC029.md.  
  Proof: top listing included those exact mixed-case root files; directory listing included lowercase audit/qa/hde-epic020 through audit/qa/hde-epic031.  
  Impact: This creates ambiguity about case conventions for repo-root reports versus governed QA directories.

### Root proliferation

* Observed: At least 10 top-level roots or root-adjacent homes hold truth/evidence/tooling material: audit, artifacts, docs, tools, scripts, catalog, schemas, goldens, fixtures, parity, plus root report/proof files.  
  Proof: top-level listing included all named roots and many root files such as manifest\_pre.sha256, manifest\_post.sha256, changes\_report.txt, patch.diff, temp\_run.\*.  
  Impact: This creates ambiguity about which homes are authoritative without following the repo’s governed-tool rules.

### Alignment summary table

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package exists | Aligned | engine/compat/compute.py, engine/sampler/core.py, engine/bodygraph/vendor\_client.py listed |
| Adapter HTTP layer exists | Aligned | adapter/http\_reader.py routes at lines 330, 392, 698, 874 |
| Presenter/emitter exists | Partial | engine/presenter/emitter.py lines 6–13 plus top-level presenter/json\_canon\_compare.py main entry |
| CLI entrypoint exists | Aligned | pyproject.toml hdctl \= "engine.cli.main:cli"; engine/cli/main.py:cli lines 239–259 |
| Vendor seam outside pure compute | Partial | vendor code under engine/bodygraph/vendor\_client.py; compat conjunction can call resolver/vendor path |
| DB/cache layer exists | Aligned | engine/db/adapter.py:DBAccess, adapter/cache\_keys.py:build\_cache\_key |
| Evidence index layout exists | Aligned/complex | docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, and tooling constants lines 24–28 |

## Negative-Claim Proof Appendix

* setup.cfg not found  
  * Token searched: setup.cfg  
  * Method: find . \-maxdepth 2 \-name "setup.cfg" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* setup.py not found  
  * Token searched: setup.py  
  * Method: find . \-maxdepth 2 \-name "setup.py" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* package.json not found  
  * Token searched: package.json  
  * Method: find . \-maxdepth 2 \-name "package.json" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* pnpm-workspace.yaml not found  
  * Token searched: pnpm-workspace.yaml  
  * Method: find . \-maxdepth 2 \-name "pnpm-workspace.yaml" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* yarn.lock not found  
  * Token searched: yarn.lock  
  * Method: find . \-maxdepth 2 \-name "yarn.lock" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* poetry.lock not found  
  * Token searched: poetry.lock  
  * Method: find . \-maxdepth 2 \-name "poetry.lock" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* uv.lock not found  
  * Token searched: uv.lock  
  * Method: find . \-maxdepth 2 \-name "uv.lock" \-print | wc \-l  
  * Scope: repo root, max depth 2  
  * Result: 0  
* 

