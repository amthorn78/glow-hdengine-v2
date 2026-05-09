# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.9

**Status:** Canon

**Effective date:** 2026-04-24

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

**Date:** 2026-04-24

**Last Epic:** HDE-EPIC030

## Audit Snapshot Metadata

* Repo root confirmation: pwd and git rev-parse \--show-toplevel both returned /workspace/glow-hdengine-v2.  
* Commit: da4761b4f9aa1fdc26fe97e9b470c730b3841d67 (git rev-parse HEAD)  
* Branch: work (git rev-parse \--abbrev-ref HEAD)  
* Working tree cleanliness: clean (git status \--porcelain returned no paths)  
* Timestamp (UTC): 2026-04-24T17:03:54Z  
* Execution environment (facts):  
  * OS/kernel: Linux 6.12.47 x86\_64 GNU/Linux (uname \-srmo)  
  * Python: Python 3.10.19 (python \--version / python3 \--version)  
  * Node: v22.21.1 (node \--version)

---

## Top-level Repo Map

Top-level entries were enumerated via find . \-maxdepth 1 \-mindepth 1 | sort (showing roots like engine, adapter, presenter, docs, artifacts, audit, tools, ci, tests, scripts, etc.).

### Expected architecture families

* engine/ — Present  
  * Contains engine code for compat/core/sampler/bodygraph/runtime/CLI (engine/compat/compute.py, engine/sampler/core.py, engine/cli/main.py).  
* adapter/ — Present  
  * HTTP/app layer and transport helpers (adapter/wsgi.py, adapter/http\_reader.py, adapter/etag\_core.py).  
* presenter/ — Present  
  * Presenter package with reader emitter (presenter/reader\_v1/emitter.py) plus canon-compare tool (presenter/json\_canon\_compare.py).  
* CLI package location(s) — Present  
  * Packaged CLI at engine/cli/main.py and script entry files under scripts/ (e.g., scripts/hdctl.py, scripts/hd\_cli.py).  
* docs/ — Present  
  * Canon/docs/evidence files, including docs/evidence/INDEX.json and docs/ENDPOINTS\_CATALOG.json.  
* artifacts/ — Present  
  * Generated evidence/log/snapshot-style artifacts (artifacts/evidence\_index.jsonl, artifacts/audit/..., artifacts/cli/...).  
* audit/ — Present  
  * Epic manifests/close reports/gates/QA outputs (audit/EPIC-027\_MANIFEST.json, audit/gates/..., audit/qa/...).  
* tools/ — Present  
  * Evidence/config/QA generators and checks (tools/evidence/update\_evidence\_index.py, tools/qa/run\_hde\_epic024\_harness.py).  
* ci/ \+ .github/workflows/ — Present  
  * CI checks and workflow (ci/checks/check\_env\_pins.sh, .github/workflows/ci.yml).  
* tests/ — Present  
  * Large test surface across adapter/cli/http/evidence/vendor/etc. (tests/http/test\_endpoint\_catalog.py, tests/cli/test\_showcompat\_sources.py).  
* scripts/ — Present  
  * Operational/dev/DB/QA scripts (scripts/ingest/run\_vendor\_ingest.py, scripts/release\_id\_recompute.py, scripts/dev\_start\_reader.sh).

### Root discipline capture (governed-output-like homes observed)

audit/, artifacts/, docs/, tools/, scripts/, catalog/, parity/, proofs/.  
---

## Packaging and Entrypoints

### 3.1 Packaging / build config

* pyproject.toml  
  * Declares project and console script:  
    * name \= "glow-hdengine" (line 6\)  
    * \[project.scripts\] hdctl \= "engine.cli.main:cli" (lines 13–14)  
    * package discovery includes engine\*, adapter\*, presenter\* (line 18).  
* requirements.txt  
  * Runtime deps: psycopg\[binary\], Flask, gunicorn.  
* requirements-dev.txt  
  * Test/dev deps: jsonschema, pytest, pytest-cov, pytest-mock.

### 3.2 Entrypoint inventory

* HTTP app startup  
  * adapter/wsgi.py:create\_app registers reader and compat blueprints:  
    * app.register\_blueprint(reader\_bp) and app.register\_blueprint(compat\_blueprint) (lines 23–24).  
* CLI console script  
  * engine/cli/main.py:cli is the console entrypoint from pyproject.toml.  
* CLI subcommands  
  * \_build\_parser() defines showcompat, aux-preview, bg:resolve, dev:sampler (lines 85, 133, 145, 173).  
* Evidence/indexing scheduled-like entrypoints (script-style)  
  * tools/evidence/update\_evidence\_index.py has argparse main (if \_\_name\_\_ \== "\_\_main\_\_").  
  * tools/evidence/run\_sanity\_pipeline.py, tools/evidence/orientation\_demo.py, tools/evidence/run\_canonical\_json\_gate.py similarly expose CLI entrypoints.

---

## Engine Modules

### 4.1 Sampler

* engine/sampler/core.py  
  * build\_candidate\_pool(...): filters zero-weight and ineligible candidates (lines 126–151).  
  * rank\_candidates(...): deterministic rank using comparator chain (lines 170–194).  
  * sample\_and\_rank(...): wrapper pool+rank (lines 196–204).  
  * Data classes: ViewerProfile, CandidateFeatures, SamplerConfig, CandidatePoolEntry, RankedCandidate.

### 4.2 Core compute

* engine/compat/compute.py  
  * compat\_public(...) builds category scores/bands/meta; normalizes pair first (normalize\_pair, lines 39–41).  
  * band\_for(score) maps score to Cool/Open/Warm/Glow (lines 17–21).  
  * AB↔BA normalization anchor: comment \+ call (\# AB↔BA identity by normalization, line 39; normalize\_pair, line 40).  
* engine/core/core.py  
  * compute\_core(...) computes deterministic CoreResult with ordered pair/bands/shared traits (lines 101–136).  
  * \_ordered\_pair and \_ordered\_bands provide symmetry/canonical ordering (lines 74–89).

### 4.3 Determinism hazards inventory (engine paths sampled)

Observed hazards (factual presence only):

* Current time  
  * engine/charts/loader.py: datetime.now(\_dt.UTC) (line 49).  
  * engine/bodygraph/vendor\_client.py: \_utc\_iso uses time.gmtime() (line 46).  
* Network calls  
  * engine/bodygraph/vendor\_client.py: urlrequest.urlopen(...) in \_default\_request (line 355).  
  * engine/db/providers/bridge\_provider.py: urllib.request.urlopen(...) (line 39 from grep hit).  
* File I/O  
  * engine/bodygraph/ingest.py: writes logs via with path.open("a", ...) (line 66).  
  * engine/cli/main.py: reads input files via Path(path).read\_text(...) (lines 985, 994).  
* Randomness without explicit seeding  
  * No random usage found in engine/sampler/core.py, engine/core/core.py, engine/compat/compute.py sampled paths.

---

## Adapter / HTTP Surfaces

### 5.1 Route registration map

* App creation/mounting  
  * adapter/wsgi.py:create\_app creates Flask(\_\_name\_\_) and mounts blueprints.  
* Mounted route groups  
  * Reader blueprint from adapter/http\_reader.py (bp \= Blueprint("reader\_v1", \_\_name\_\_)).  
  * Compat blueprint from engine/http/compat\_handler.py with prefix url\_prefix="/api/compat/v1" (line 11).

### 5.2 Surface classification

* Reader-like JSON success  
  * /reader in adapter/http\_reader.py (@bp.get("/reader"), line 330).  
* Aux/narrative  
  * /api/aux/narrative and /aux/narrative handlers (@bp.get(...), lines 392–394).  
* Admin/internal  
  * /api/compat/v1 POST in engine/http/compat\_handler.py (@compat\_blueprint.route("", methods=\["POST"\], ...), line 90).  
  * /internal/version GET/HEAD in adapter/http\_reader.py (line 874).  
* Dev/diagnostic harness  
  * /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction (lines 766/774/782).  
  * /ops/\* and /internal/dev/sampler in same module.

### 5.3 Transport semantics hooks

* HEAD vs GET parity  
  * Reader handler explicitly branches on HEAD and sets Content-Length from GET body size (adapter/http\_reader.py lines 377–383).  
  * /internal/version HEAD branch returns empty body with GET-equivalent length (lines 886–890).  
* Conditional / 304  
  * Reader checks If-None-Match, returns 304 with empty body and strips content headers (lines 365–375).  
* ETag generation  
  * Reader ETag from SHA256 of body bytes: etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"" (line 364).  
  * Aux narrative route sets ETag via digest in unsuppressed path (lines 429–432).  
* Cache-Control  
  * Common headers set Cache-Control: no-store in adapter/wsgi.py (line 27).  
  * Narrative sets private/no-store depending on suppression (lines 428, 435).  
* Content-Type rules  
  * Common JSON content-type default in adapter/wsgi.py (line 28).  
  * Writer/transport handlers remove Content-Type for specific 204/405 cases in compat handler (lines 37, 50).

---

## Presenter / Emitter

* engine/presenter/emitter.py  
  * emit\_public(...) delegates to canonical serializer (canon.sercanon) (lines 6–13).  
* engine/serializer/canon.py  
  * sercanon(...) delegates to engine.stable.sercanon.serialize with comments for sorted keys/compact separators/newline (lines 6–15).  
* engine/stable/sercanon.py  
  * serialize(...) guarantees exactly one trailing \\n and UTF-8 bytes (lines 15–19).  
* presenter/reader\_v1/emitter.py  
  * emit\_reader\_v1(...) builds preimage, hashes it, injects idempotence\_hash, emits canonical bytes (lines 54–65).

Callers observed:

* HTTP routes call emit\_public in adapter and compat handlers (adapter/wsgi.py lines 42/48/55; engine/http/compat\_handler.py line 15).  
* CLI uses emitter.emit\_public(...) and sercanon(...) (engine/cli/main.py lines 848, 969).

---

## CLI Surfaces

* Packaged command: hdctl via pyproject.toml \-\> engine.cli.main:cli.  
* Subcommands and args: defined in \_build\_parser:  
  * showcompat with \--pair-file, \--a-file, \--b-file, \--source, \--conjunction, etc. (lines 85–131).  
  * aux-preview (lines 133–144).  
  * bg:resolve with required \--user and optional \--source, \--birth\* (lines 145–171).  
  * dev:sampler with required \--viewer, \--candidates-file (lines 173–190).  
* Call chain anchors  
  * showcompat path calls compat\_public(...) and canonical emitter (engine/cli/main.py lines 833–849), then writes stdout via \_emit\_stdout\_bytes (line 874).  
  * bg:resolve calls resolve\_bodygraph(...) and emits JSON to stdout (lines 224–236).  
  * dev:sampler calls sample\_and\_rank(...) and writes canonical JSON to stdout (lines 972–980).  
* Output surfaces  
  * Writes files: \--dump-reader (\_dump\_reader\_bytes, lines 553–559), admin dump directory via canon\_dump(...) (lines 586–589).  
  * Stdout: \_emit\_stdout\_bytes and sys.stdout.buffer.write(...) (lines 559–565, 969).  
  * Non-zero exits on argument issues: parser errors normalized to exit 64 (lines 251–253), typed CliError returns configured nonzero (lines 260–262).

---

## Vendor Seam & BodyGraph Storage

### 8.1 Vendor client

* HTTP client module: engine/bodygraph/vendor\_client.py  
  * HdApiClient.from\_env(...) reads HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, optional RELEASE\_ID (lines 149–152, 161).  
  * fetch(...) performs POST request/retry/backoff/error mapping (lines 212–280).  
* Request shaping  
  * build\_request(...) canonicalizes date, builds JSON body and headers (HD-Api-Key, HD-Geocode-Key) (lines 179–210, 201–203).  
* Response parsing  
  * JSON parse in fetch and typed error mapping on failures (lines 237–240, 243+).

### 8.2 BodyGraph persistence/caching

* DB layer modules  
  * engine/db/adapter.py, engine/db/providers/psycopg\_provider.py, engine/db/providers/bridge\_provider.py.  
* Ingest/persistence logic  
  * engine/bodygraph/ingest.py writes into hde.body\_graphs with ON CONFLICT DO NOTHING (lines 214–220).  
  * Reads latest from hde.body\_graphs\_current in CLI DB source path (engine/cli/main.py lines 373–380).  
* Key/fingerprint logic  
  * input\_fingerprint from request body SHA256 (vendor\_client.py line 197).  
  * idempotency key format {user}:{vendor}:{version}:{fingerprint} (ingest.py line 270).  
* Decision logic: cached vs vendor  
  * conjunction\_public\_resolved tries local lookup first, then resolver acquisition (compute.py lines 147–150, 172–179, 198–203).

### 8.3 Offline/network gating posture

* Explicit gating observed:  
  * resolve\_bodygraph vendor path refuses on SAFE rails or blocked network:  
    * PROVIDER\_REFUSED when SAFE\_MODE truthy (resolver.py lines 108–117),  
    * PROVIDER\_NETWORK\_BLOCKED when network disabled (lines 118–127).  
  * ingest\_vendor\_bodygraph enforces same before vendor call (ingest.py lines 125–131).

---

## Evidence, Indices, Catalogs

### 9.1 Evidence homes inventory

* docs/evidence/  
  * Contains INDEX.json, INDEX.sha256, path proofs, epic evidence docs.  
  * Mixed: machine index \+ authored docs.  
* artifacts/  
  * Contains large generated-style snapshots/logs/proofs (artifacts/evidence\_index.jsonl, artifacts/\*/\*.path\_proof.txt, epic bundles).  
* audit/  
  * Contains manifests, close reports, gate logs, QA trees (audit/EPIC-\*.json, audit/gates/..., audit/qa/...).  
* Other evidence-like homes present  
  * parity/, proofs/, catalog/, and test snapshots under tests/transport/headers/\*.snap.

### 9.2 Evidence index structures

* docs/evidence/INDEX.json  
  * JSON array of artifact records (first entry begins with keys like artifact\_key, discovered\_physical\_path, epic\_id, sha256).  
* docs/evidence/INDEX.sha256  
  * Hash sentinel checked by ci/checks/check\_evidence\_index\_hash.sh.  
* artifacts/evidence\_index.jsonl  
  * Line-delimited machine mirror with fields including artifact\_key, discovered\_physical\_path, proof\_anchor, sha256.  
* Tooling  
  * tools/evidence/update\_evidence\_index.py defines HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH constants (lines 24–26).  
  * CI validation in ci/checks/check\_evidence\_index\_hash.sh and ci/checks/check\_mirror\_schema.sh.

### 9.3 Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * Top-level shape: {"endpoints":\[...\], "success\_endpoints":\[\]}; entries include path, method, classification, env\_gate, a7\_eligible.  
* Referenced by tests/tooling  
  * tests/http/test\_endpoint\_catalog.py reads this file directly (line 6).  
  * Indexed in artifacts/evidence\_index.jsonl entries (artifact\_key":"endpoints.catalog"...).

### 9.4 Proof/snapshot artifact examples

* Examples present by listing:  
  * tests/transport/headers/aux\_text\_200.snap  
  * tests/transport/headers/aux\_suppression\_200.snap  
  * artifacts/ops/internal\_version/headers\_get.txt (seen in mirror lines)  
* Producer anchors:  
  * tests/http/test\_endpoint\_catalog.py asserts catalog contents.  
  * CI runs evidence generators/checks from .github/workflows/ci.yml (e.g., python tools/evidence/update\_evidence\_index.py, python tools/evidence/run\_canonical\_json\_gate.py).

---

## Tests, QA Harness, CI/Checks

### 10.1 Tests map (selected loci)

* HTTP/reader/compat  
  * tests/adapter/test\_compat\_http\_dev.py, tests/http/test\_compat\_endpoint\_contract.py, tests/compliance/test\_reader\_etag\_and\_conditional.py.  
  * Example assertion: reader GET→304 with empty body and HEAD parity (test\_reader\_etag\_and\_conditional.py, lines 24–35).  
* CLI outputs/canonical bytes  
  * tests/cli/test\_cli\_canonical\_bytes.py, tests/cli/test\_showcompat\_parity\_and\_identity.py, tests/cli/test\_serializer\_guards.py.  
* Determinism/env gates  
  * tests/invariance/test\_determinism\_env\_helper.py, tests/core/test\_engine\_core\_determinism.py.  
* Evidence index/catalog  
  * tests/evidence/test\_evidence\_index\_snapshot.py, tests/ops/test\_evidence\_index.py, tests/http/test\_endpoint\_catalog.py.  
* Vendor/network-related fixtures  
  * tests/bodygraph/test\_vendor\_client.py uses mocked request function and monkeypatched env (lines 11–23, 33–38), indicating simulated vendor I/O rather than live network.

### 10.2 CI workflows

* Workflow file: .github/workflows/ci.yml  
* Jobs/checks referenced  
  * test job runs env pins, CLI help, canonical JSON gate, evidence index update/check, mirror/final-LF checks, and selected pytest suites (lines 23–63).  
  * compat-conj-pr01-closure, epic020, compat-http-epic020, epic020-evidence-bundles, sanity-pipeline jobs define additional closed-rails test/evidence runs.

### 10.3 Script/check inventory (QA-relevant)

* ci/checks/\*  
  * check\_env\_pins.sh: runs determinism env checker with log path (python \-m engine.runtime.determinism\_env ..., lines 3–12).  
  * check\_mirror\_schema.sh: validates JSONL mirror rows/keys/proofs (required key set lines 8–16).  
  * check\_evidence\_index\_hash.sh: compares INDEX.sha256 against INDEX.json hash.  
* tools/evidence/\*  
  * Includes generators/validators such as update\_evidence\_index.py, orientation\_demo.py, run\_sanity\_pipeline.py, run\_canonical\_json\_gate.py, validate\_evidence\_paths.py.  
* scripts/\*  
  * Includes ingestion/release/QA and CLI proof scripts, e.g., scripts/ingest/run\_vendor\_ingest.py, scripts/release\_id\_recompute.py, scripts/qa/dev\_sampler\_live\_qa.py.

---

## Flows & Call Chains

### 1\) Reader success flow (HTTP)

adapter/wsgi.py:create\_app → adapter/http\_reader.py:reader\_v1 → (emit\_fn default emit\_reader\_public\_bytes) → Response

* /reader handler checks query/env and builds body (adapter/http\_reader.py lines 330–363).  
* ETag computed from body SHA and conditional logic applied (lines 364–375).  
* HEAD path emits empty body with GET Content-Length (lines 377–383).  
* Response is JSON with transport headers and cache semantics.

### 2\) Compat API flow (HTTP)

adapter/wsgi.py:create\_app → engine/http/compat\_handler.py:post\_json → engine.compat.compute:compat\_public → engine.presenter.emit\_public

* Mounted as blueprint with prefix /api/compat/v1 (compat\_handler.py line 11).  
* POST validates payload/id forms/viewer prefs (lines 95–120).  
* Calls compat\_public(...) to compute categories/meta (lines 121–124).  
* Writes JSON envelope via \_writer\_payload (emit\_public, lines 14–21).

### 3\) CLI showcompat / preview flow

engine/cli/main.py:cli → showcompat → compat\_public \+ emit\_reader\_public\_envelope → emitter.emit\_public/\_emit\_stdout\_bytes

* Parser maps showcompat to handler (line 131).  
* Showcompat loads source (files/db/vendor/auto) and canonicalizes pair (lines 746–804, 826–829).  
* Computes compat and emits canonical bytes (lines 833–849).  
* Optionally dumps reader/admin files (lines 858–872), then writes stdout with LF/CRLF guards (line 874; guard lines 559–564).

### 4\) Vendor acquisition / BodyGraph ingest flow

engine.cli.main:bg\_resolve or showcompat(source=vendor) → engine.bodygraph.resolver:resolve\_bodygraph → engine.bodygraph.ingest:ingest\_vendor\_bodygraph → engine.bodygraph.vendor\_client:HdApiClient.fetch → engine.db.DBAccess

* Resolver enforces SAFE/network rails before vendor path (resolver.py lines 108–127).  
* Ingest enforces rails again, builds request, fetches vendor payload, canonical-emits, persists DB row (ingest.py lines 125–135, 166–175, 214–233).  
* Client fetch loop performs HTTP POST and retries with typed mapping (vendor\_client.py lines 226–236, 243–280).

### 5\) Evidence index update/validation flow

.github/workflows/ci.yml:test job → tools/evidence/update\_evidence\_index.py (write/check) → ci/checks/check\_evidence\_index\_hash.sh \+ ci/checks/check\_mirror\_schema.sh

* CI step sequence includes:  
  * python tools/evidence/update\_evidence\_index.py (line 31),  
  * ... \--check (line 33),  
  * hash check (line 52),  
  * mirror schema check (line 54).  
* Tool constants bind human+machine index paths (update\_evidence\_index.py lines 24–26).

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Both top-level presenter/ and engine/presenter/ exist.  
  * Proof: file listings include presenter/reader\_v1/emitter.py and engine/presenter/emitter.py.  
  * Impact (factual): This creates two presenter module roots in the repository structure.

### Surface drift

* Observed: Endpoint catalog classifies /reader as dev\_harness and APP\_ENV=dev.  
  * Proof: docs/ENDPOINTS\_CATALOG.json entry for /reader has "classification":"dev\_harness","env\_gate":"APP\_ENV=dev","a7\_eligible":true.  
  * Impact: Reader route classification is explicitly tied to dev-gated catalog metadata.

### Evidence drift

* Observed: Evidence-like artifacts exist across multiple top-level homes (docs/, artifacts/, audit/, plus tests/transport/headers snapshots).  
  * Proof: listings and index entries show all these homes populated.  
  * Impact: Evidence records are distributed across multiple roots.

### Determinism drift

* Observed: Engine tree contains modules with time/network/file I/O (engine/bodygraph/vendor\_client.py, engine/bodygraph/ingest.py, engine/charts/loader.py) alongside pure-compute modules (engine/core/core.py, engine/sampler/core.py).  
  * Proof anchors listed in Engine section.  
  * Impact: Deterministic and I/O-bearing concerns coexist inside the engine/ tree.

### Vendor seam drift

* Observed: Vendor seam is implemented in engine/bodygraph/vendor\_client.py and called from engine/bodygraph/ingest.py and resolver/CLI paths.  
  * Proof: imports/calls in engine/bodygraph/ingest.py lines 16, 132–134; resolver lines 145–146.  
  * Impact: Vendor access is within engine namespace rather than an external top-level vendor package.

### Path-case drift

* Observed: Mixed naming styles at root/audit (EPIC-027\_MANIFEST.json, EPIC017\_MANIFEST.json, hde-epic0xx folders).  
  * Proof: find outputs under audit/.  
  * Impact: Naming conventions are mixed across evidence artifacts.

### Root proliferation

* Observed: 7 top-level “truth-home-like” roots identified: audit/, artifacts/, docs/, tools/, scripts/, catalog/, proofs/.  
  * Proof: top-level listing output.  
  * Impact: Repository uses multiple top-level homes for code, artifacts, and governance/evidence material.

### Alignment summary (expected areas)

| Expectation area | Status | Anchor |
| :---- | :---- | :---- |
| engine/adapter/presenter split exists | Aligned (structural presence) | top-level engine/, adapter/, presenter/ found |
| CLI entrypoint packaging | Aligned | pyproject.toml \[project.scripts\] hdctl \= "engine.cli.main:cli" |
| vendor seam present | Aligned | engine/bodygraph/vendor\_client.py, ingest.py |
| evidence index \+ mirror pair | Aligned | docs/evidence/INDEX.json \+ artifacts/evidence\_index.jsonl \+ updater/check scripts |
| single presenter root | Partial | both presenter/ and engine/presenter/ exist |
| single evidence home | Partial | evidence artifacts in docs/, artifacts/, audit/, plus test snapshots |

---

## Negative-Claim Proof Appendix

1. setup.cfg not found  
   * Token searched: setup.cfg  
   * Method: rg \--files \-g 'setup.cfg' | wc \-l  
   * Scope: repo root  
   * Result: 0  
2. setup.py not found  
   * Token searched: setup.py  
   * Method: rg \--files \-g 'setup.py' | wc \-l  
   * Scope: repo root  
   * Result: 0  
3. Monorepo/workspace manager config files not found (searched set)  
   * Tokens searched: package.json, pnpm-workspace.yaml, poetry.lock  
   * Method: rg \--files \-g 'package.json' \-g 'pnpm-workspace.yaml' \-g 'poetry.lock' | wc \-l  
   * Scope: repo root  
   * Result: 0  
4. (Verification, not negative) expected exact top-level dirs exist  
   * find . \-maxdepth 1 \-type d \-name 'engine' | wc \-l \=\> 1  
   * find . \-maxdepth 1 \-type d \-name 'adapter' | wc \-l \=\> 1  
   * find . \-maxdepth 1 \-type d \-name 'presenter' | wc \-l \=\> 1

---

### Checks run

* ✅ pwd && git rev-parse \--show-toplevel && git rev-parse HEAD && git rev-parse \--abbrev-ref HEAD && git status \--porcelain && date \-u \+"%Y-%m-%dT%H:%M:%SZ" && uname \-srmo && (python \--version 2\>/dev/null || true) && (python3 \--version 2\>/dev/null || true) && (node \--version 2\>/dev/null || true)  
* ✅ find . \-maxdepth 1 \-mindepth 1 | sed 's\#^./\#\#' | sort  
* ✅ rg \--files \-g 'pyproject.toml' \-g 'setup.cfg' \-g 'setup.py' \-g 'requirements\*.txt'  
* ✅ rg \-n "\\\[project\\\]|\\\[project\\.scripts\\\]|console\_scripts|entry\_points|dependencies|name\\s\*=\\s\*\\"|requires-python" pyproject.toml requirements.txt requirements-dev.txt  
* ✅ find engine \-maxdepth 3 \-type f | sort  
* ✅ find adapter \-maxdepth 3 \-type f | sort  
* ✅ find presenter \-maxdepth 3 \-type f | sort  
* ✅ find tests \-maxdepth 3 \-type f | sort  
* ✅ find .github/workflows \-maxdepth 2 \-type f | sort && find ci \-maxdepth 3 \-type f | sort  
* ✅ printf 'setup.cfg hits: '; rg \--files \-g 'setup.cfg' | wc \-l; printf 'setup.py hits: '; rg \--files \-g 'setup.py' | wc \-l; printf 'workspace config hits: '; rg \--files \-g 'package.json' \-g 'pnpm-workspace.yaml' \-g 'poetry.lock' | wc \-l; printf 'top-level adapter dir exact: '; find . \-maxdepth 1 \-type d \-name 'adapter' | wc \-l; printf 'top-level presenter dir exact: '; find . \-maxdepth 1 \-type d \-name 'presenter' | wc \-l; printf 'top-level engine dir exact: '; find . \-maxdepth 1 \-type d \-name 'engine' | wc \-l

