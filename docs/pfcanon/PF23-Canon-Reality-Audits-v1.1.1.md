# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.1

**Status:** Canon

**Effective date:** 2026-05-20

**Last Update Gate:** HDE-EPIC032

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

**Date:** 2026-05-20

**Last Epic:** HDE-EPIC032

## Audit Snapshot Metadata

* Repo root confirmation: pwd returned /workspace/glow-hdengine-v2.  
* Commit: git rev-parse HEAD → eac3286958161f072e5d8eb6039f05c4d60423e9.  
* Branch: git rev-parse \--abbrev-ref HEAD → work.  
* Working tree cleanliness: git status \--porcelain returned empty output (clean).  
* Timestamp (UTC): 2026-05-20T03:08:37Z.  
* Execution environment facts:  
  * OS/kernel: Linux 6.12.47 x86\_64 GNU/Linux.  
  * Python: Python 3.14.4.  
  * Node: v24.15.0.

---

## Top-level Repo Map

### Top-level presence map (from find . \-maxdepth 1\)

Observed top-level roots include (non-exhaustive key set):  
adapter/, engine/, presenter/, docs/, artifacts/, audit/, tools/, ci/, tests/, scripts/, .github/, catalog/, schemas/, migrations/, sql/, config/, narratives/.

### Expected families classification

* engine/ — Present.  
  Contains core runtime, compat, sampler, CLI, HTTP compat handler, vendor/bodygraph, DB adapter package.  
  Anchors: engine/compat/compute.py, engine/sampler/core.py, engine/cli/main.py.  
* adapter/ — Present.  
  Contains Flask app wiring, reader routes, env/IO guard code, ETag/cache helpers.  
  Anchors: adapter/factory.py, adapter/http\_reader.py, adapter/etag\_core.py.  
* presenter/ — Present (plus engine-local presenter).  
  Top-level presenter/json\_canon\_compare.py exists, and primary emitter lives at engine/presenter/emitter.py.  
  Anchors: presenter/json\_canon\_compare.py, engine/presenter/emitter.py.  
* CLI package location(s) — Present.  
  Packaged script hdctl points to engine.cli.main:cli; engine/cli/\_\_main\_\_.py exists.  
  Anchors: pyproject.toml \[project.scripts\], engine/cli/main.py.  
* docs/ — Present.  
  Includes evidence index files and docs artifacts.  
  Anchors: docs/evidence/INDEX.json, docs/ENDPOINTS\_CATALOG.json (listed by repo and mirrored under artifacts).  
* artifacts/ — Present.  
  Contains generated evidence/proof-like outputs, sidecars, route probes, CLI captures.  
  Anchors: artifacts/evidence\_index.jsonl, artifacts/audit/ENDPOINTS\_CATALOG.json, artifacts/cli/\*.path\_proof.txt.  
* audit/ — Present.  
  Contains manifests, close reports, QA logs, gate outputs.  
  Anchors: audit/EPIC-027\_MANIFEST.json, audit/EPIC-027\_close\_report.md, audit/qa/\*\*.  
* tools/ — Present.  
  Contains evidence/index generators, QA harnesses, config artifact generators, CLI proof tools.  
  Anchors: tools/evidence/update\_evidence\_index.py, tools/evidence/run\_sanity\_pipeline.py, tools/config/generate\_bundles.py.  
* ci/ and .github/ — Present.  
  CI checks and jobs are in ci/checks/\* and ci/jobs/\*; .github root also exists.  
  Anchors: ci/checks/check\_env\_pins.sh, ci/jobs/rails\_closed\_refusal.yml.  
* tests/ — Present.  
  Large test suite spanning adapter, CLI, compat, evidence, db, compliance, etc.  
  Anchors: tests/adapter/test\_reader\_parity.py, tests/cli/test\_showcompat\_sources.py, tests/evidence/test\_evidence\_index\_snapshot.py.

### Root discipline capture (truth-home-like roots observed)

audit/, artifacts/, docs/, tools/, scripts/, catalog/, ci/.  
---

## Packaging and Entrypoints

### 3.1 Packaging/build config

* pyproject.toml found.  
  * Declares package: name \= "glow-hdengine".  
  * Declares console script: hdctl \= "engine.cli.main:cli".  
  * Setuptools package discovery includes engine\*, adapter\*, presenter\*.  
* Requirements files found: requirements.txt, requirements-dev.txt (existence from top-level listing).

### 3.2 Entrypoint inventory

* HTTP startup  
  * adapter/factory.py:create\_app creates Flask app and registers blueprint bp with url\_prefix="".  
  * adapter/wsgi.py:create\_app also registers reader \+ compat blueprints.  
  * run\_flask.py imports adapter.factory:create\_app and runs app.run(...).  
* CLI  
  * engine/cli/main.py:cli is packaged entrypoint.  
  * Parser defines subcommands including showcompat, aux-preview, bg:resolve, dev:sampler.  
* Evidence/indexing jobs (script entrypoints)  
  * tools/evidence/update\_evidence\_index.py has argparse main.  
  * tools/evidence/orientation\_demo.py, tools/evidence/run\_sanity\_pipeline.py, tools/evidence/run\_canonical\_json\_gate.py have argparse mains.

---

## Engine Modules

### 4.1 Sampler

* Module: engine/sampler/core.py.  
* Primary symbols observed: build\_candidate\_pool, rank\_candidates, sample\_and\_rank, dataclasses ViewerProfile, CandidateFeatures, SamplerConfig.  
* Role evidence: Docstring states “Pure-compute sampler core”; rank\_candidates uses deterministic sorting with compare\_ids.

### 4.2 Core compute

* Module: engine/compat/compute.py.  
* Primary symbols: compat\_public, conjunction\_public, conjunction\_public\_resolved, band\_for.  
* AB↔BA handling: compat\_public normalizes pair via normalize\_pair(a,b) then pair\_key(...).  
* Result structure: returns dict with "categories" and "meta" fields.

### 4.3 Determinism hazards inventory (observed in sampled engine paths)

* Current time usage found  
  * engine/bodygraph/ingest.py uses time.monotonic() and time.strftime(...).  
  * engine/bodygraph/vendor\_client.py uses time.monotonic(), time.gmtime(...).  
* Network calls found  
  * engine/bodygraph/vendor\_client.py imports and uses urllib.request machinery (urlrequest, redirect handler).  
* File I/O found  
  * engine/bodygraph/ingest.py writes JSONL logs via \_append\_jsonl and opens files.  
* Randomness without seed  
  * In sampled engine modules reviewed (engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/\*), no random usage was observed.  
* Non-deterministic iteration  
  * Sampled sort logic in sampler explicitly uses deterministic comparator chain and sorted(...).

---

## Adapter / HTTP Surfaces

### 5.1 Route registration map

* App/router creation  
  * adapter/factory.py:create\_app creates Flask(\_\_name\_\_), mounts bp (app.register\_blueprint(bp, url\_prefix="")).  
  * adapter/wsgi.py:create\_app registers reader\_bp and compat\_blueprint.  
* Mounted route groups  
  * Compat group prefix: /api/compat/v1 from engine/http/compat\_handler.py (Blueprint(..., url\_prefix="/api/compat/v1")).  
  * Reader/internal/ops/dev routes: defined in adapter/http\_reader.py with decorators on bp.

### 5.2 Surface classification (observed)

* Reader-like JSON success: adapter/http\_reader.py (reader blueprint \+ emitter usage).  
* Aux/narrative: adapter/http\_reader.py imports emit\_public\_aux, get\_pack.  
* Admin/internal: /internal/version route exists (@bp.route("/internal/version", methods=\["GET", "HEAD"\])).  
* Dev/diagnostic harness: routes include /internal/dev/sampler, /ops/writer/diagnostic, /ops/probe/env, /ops/rails/refusal.

### 5.3 Transport semantics hooks (anchored)

* HEAD vs GET handling  
  * Compat: before\_app\_request guard returns explicit HEAD/OPTIONS transport responses.  
* Conditional/304-related hooks  
  * ETag parsing helper in adapter reader module (\_parse\_if\_none\_match(...)).  
* ETag handling  
  * adapter/factory.py strips ETag for /internal/\* paths in after\_request.  
  * Writer responses remove ETag in compat handler and reader writer helper.  
* Cache-control rules  
  * Reader helper sets Cache-Control \= "private, max-age=0, must-revalidate".  
  * Writer paths set Cache-Control \= "no-store".  
* Content-Type rules  
  * Writer response helpers explicitly set application/json; charset=utf-8.  
  * JSON content-type check helper \_json\_content\_type\_ok(...) enforces exact normalized value.

---

## Presenter / Emitter

* Primary emitter module: engine/presenter/emitter.py.  
  * emit\_public(...) delegates to canonical serializer canon.sercanon(...).  
  * emit\_public\_with\_envelope(...) returns (bytes, envelope).  
  * emit\_compact\_json(...) aliases canonical emitter.  
* Canonical JSON formatting rules  
  * Serializer path: engine/serializer/canon.py (called by emitter).  
  * Emitter docstring claims LF-terminated UTF-8 canonical bytes and deterministic key sorting default.  
* Callers observed  
  * HTTP compat handler uses from engine.presenter import emit\_public.  
  * Ingest path uses emitter.emit\_public\_with\_envelope(...).  
  * CLI uses emitter output for stdout path in engine/cli/main.py.

---

## CLI Surfaces

* Console script: hdctl from pyproject.toml to engine.cli.main:cli.  
* Command structure (argparse)  
  * Subcommands: showcompat, aux-preview, bg:resolve, dev:sampler.  
  * \--version global flag behavior is custom-handled in cli(...).  
* \_\_main\_\_ module  
  * engine/cli/\_\_main\_\_.py exists (module-execution entry).  
* Output surfaces  
  * Stdout writes visible via sys.stdout.write(...) in command handlers.  
  * File outputs: showcompat parser includes \--dump-reader, \--dump-admin-dir.  
* Exit behavior  
  * CliError carries exit code; parser SystemExit remapped to code 64 for usage errors in cli(...).

---

## Vendor Seam & BodyGraph Storage

### 8.1 Vendor client

* HTTP client module: engine/bodygraph/vendor\_client.py.  
* Symbols: HdApiClient, VendorRequest, VendorResult, VendorError.  
* Input/env keys referenced: HDAPI\_BASE\_URL requirement indicated in error text; also api\_key, geo\_key, release\_id passed into client constructor paths.  
* Request/parse  
  * Request object has url, headers, body\_bytes, input\_fingerprint.  
  * Typed error mapping and retry/timeout pinning present.

### 8.2 BodyGraph persistence/caching

* Persistence module: engine/bodygraph/ingest.py.  
* DB access seam: imports engine.db.DBAccess, builds SQL INSERT INTO hde.body\_graphs ... ON CONFLICT DO NOTHING.  
* Decision logic  
  * ingest\_vendor\_bodygraph(...) checks rails, fetches vendor payload, persists via DB access unless dry\_run.  
  * Row count before/after used to compute rows\_written.  
* Cache/read path in conjunction resolve  
  * engine/compat/compute.py:conjunction\_public\_resolved attempts local lookup first; on miss calls resolver/vendor path, then re-checks local.

### 8.3 Offline/vendor gating posture

* Explicit gating found  
  * engine/bodygraph/ingest.py checks:  
    * if SAFE\_MODE truthy → raises VendorError("PROVIDER\_REFUSED", ...).  
    * if not ALLOW\_NETWORK truthy → raises VendorError("PROVIDER\_NETWORK\_BLOCKED", ...).

---

## Evidence, Indices, Catalogs

### 9.1 Evidence homes inventory

* docs/evidence/\*\*: contains INDEX.json, INDEX.sha256, path proofs, and epic evidence markdowns.  
* artifacts/\*\*: contains generated logs, snapshots, catalog mirrors, .path\_proof.txt, .sha256.  
* audit/\*\*: contains manifests, close reports, QA directories, gate files.  
* Mixed/generated indicators  
  * Generated-looking patterns: .path\_proof.txt, .sha256, \*\_MANIFEST.json, \*\_close\_report.md, JSONL indices.

### 9.2 Evidence index structures

* Found:  
  * docs/evidence/INDEX.json  
  * docs/evidence/INDEX.sha256  
  * artifacts/evidence\_index.jsonl (present in repo listing)  
* Tooling:  
  * tools/evidence/update\_evidence\_index.py (“Maintain the evidence index and mirror” in parser description).  
  * ci/checks/check\_evidence\_index\_hash.sh.  
  * ci/checks/check\_mirror\_schema.sh.

### 9.3 Endpoint catalog

* Catalog paths  
  * docs/ENDPOINTS\_CATALOG.json (repo instruction references it as source-of-truth).  
  * artifacts/audit/ENDPOINTS\_CATALOG.json mirror exists.  
* Referenced by tooling/tests  
  * Multiple QA/evidence scripts and tests refer to endpoint catalogs and checks (by naming in tests/ci listing).

### 9.4 Proof/snapshot artifacts

* Examples found:  
  * artifacts/audit/internal\_version\_probe.json  
  * artifacts/cli/reader\_cli\_parity.bytes  
  * artifacts/compat/AB.json, artifacts/compat/BA.json  
  * Many with .path\_proof.txt.  
* Producers (anchored by script names):  
  * tools/cli/generate\_showcompat\_artifacts.py  
  * tools/evidence/\* generators and run\_sanity\_pipeline.py  
  * scripts/probe\_internal\_version.py (writes probe output with \--out default artifacts).

---

## Tests, QA Harness, CI/Checks

### 10.1 Tests map (observed roots/loci)

* Adapter HTTP behavior: tests/adapter/\* (reader parity, headers, ETag, writer transport, env guard).  
* CLI behavior: tests/cli/\* (canonical bytes, usage/errors, showcompat sources).  
* Determinism/evidence/canonical checks: tests/evidence/\*, tests/compliance/\*, tests/canon/\*.  
* Vendor/DB seam: tests/bodygraph/\*, tests/db/\*.  
* Network reliance hints  
  * Vendor-client tests and bodygraph resolver tests imply vendor seam exercising (tests/bodygraph/test\_vendor\_client.py, tests/bodygraph/test\_resolver\_vendor.py).

### 10.2 CI workflows/jobs

* CI checks scripts  
  * ci/checks/check\_env\_pins.sh  
  * ci/checks/check\_evidence\_index\_hash.sh  
  * ci/checks/check\_mirror\_schema.sh  
  * ci/checks/check\_release\_identity.sh  
* Named jobs  
  * ci/jobs/rails\_closed\_refusal.yml  
  * ci/jobs/rails\_open\_conformance.yml  
  * ci/jobs/logs\_keys\_only\_redaction.yml  
* These file names and check names map directly to determinism/evidence governance surfaces.

### 10.3 Script/check inventory (sample)

* tools/evidence/run\_sanity\_pipeline.py — closed-rails sanity pipeline entry.  
* tools/evidence/update\_evidence\_index.py — index/mirror update/check logic.  
* tools/evidence/run\_canonical\_json\_gate.py — canonical JSON gate entry.  
* tools/generate\_registry\_report.py — registry report generator.  
* scripts/release\_id\_recompute.py — recompute/validate release identity.  
* scripts/probe\_internal\_version.py — probes internal version endpoint and writes artifact.

---

## Flows & Call Chains

### 1\) Reader success flow (HTTP)

adapter/factory.py:create\_app → adapter/http\_reader.py (bp handlers) → engine/runtime/emit\_reader\_public\_bytes \+ engine/presenter/emitter.py → Flask Response

* App mounts blueprint at /.  
* Reader module imports runtime/presenter functions.  
* Response headers set by reader helper include JSON content type \+ cache control.

### 2\) Compat API flow (HTTP)

adapter/wsgi.py:create\_app → engine/http/compat\_handler.py:compat\_blueprint POST/GET/HEAD/OPTIONS → engine/compat/compute.py:compat\_public → engine.presenter.emit\_public → Flask Response

* Prefix is /api/compat/v1.  
* HEAD/OPTIONS are intercepted with explicit transport response helpers.  
* POST path validates payload/id mode and viewer prefs before compute.

### 3\) CLI showcompat flow

pyproject.toml hdctl entry → engine/cli/main.py:cli → showcompat handler → compat/bodygraph helpers \+ emitter/serializer → stdout and optional dump files

* Parser defines showcompat with pair-file/a-file/b-file inputs and dump options.  
* Output bytes are canonical emitter-derived.  
* CLI maps typed failures to specific exit codes.

### 4\) Vendor acquisition / BodyGraph ingest flow

engine/compat/compute.py:conjunction\_public\_resolved (local lookup miss) → engine/bodygraph/resolver.py:resolve\_bodygraph → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.fetch \+ engine.db adapter write

* Resolver path attempts local lookup first.  
* Ingest enforces SAFE/ALLOW\_NETWORK gating before vendor fetch.  
* DB insert and row-count comparison are part of ingest outcome.

### 5\) Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py (write/check) → docs/evidence/INDEX.json \+ INDEX.sha256 \+ artifacts/evidence\_index.jsonl → ci/checks/check\_evidence\_index\_hash.sh \+ check\_mirror\_schema.sh

* Tool parser description states index/mirror maintenance.  
* CI check scripts exist to validate hash/schema constraints.  
* Path-proof discipline is represented by many sibling \*.path\_proof.txt artifacts.

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Both top-level presenter/ and engine/presenter/ exist; canonical emission code used by engine is in engine/presenter/emitter.py.  
* Impact (factual): This creates dual presenter-named locations in repo structure.

### Surface drift

* Observed: Compat writer surface is at /api/compat/v1 with POST/HEAD/OPTIONS logic; reader/internal/dev/ops routes are concentrated in adapter/http\_reader.py.  
* Impact: Route responsibilities are split across adapter and engine HTTP modules.

### Evidence drift

* Observed: Evidence/governed-like artifacts exist across docs/evidence/, artifacts/, and audit/.  
* Impact: Multiple roots exist for evidence material and mirrors.

### Determinism drift

* Observed: Engine modules include time/file/network behavior (ingest/vendor client), while sampler/core path is pure deterministic sorting logic.  
* Impact: Deterministic and non-deterministic concerns coexist across engine subpackages.

### Vendor seam drift

* Observed: Vendor seam is under engine/bodygraph/vendor\_client.py and called through resolver/ingest path; not under adapter-only layer.  
* Impact: Vendor acquisition logic resides in engine namespace.

### Path-case drift

* Observed: Mixed naming styles appear (EPIC017..., EPIC-027..., lowercase directories, uppercase file prefixes).  
* Impact: Case/pattern variability may affect path convention uniformity.

### Root proliferation

* Observed fact: 7 top-level truth-home-like roots identified: audit/, artifacts/, docs/, tools/, scripts/, catalog/, ci/.  
* Impact: Multiple governance-relevant roots exist simultaneously.

### Alignment summary (quick)

* Engine/adapter/presenter split: Partial (present, with some overlapping responsibility).  
* CLI present and packaged: Aligned.  
* Vendor seam outside adapter-only boundary: Partial/Drift vs strict adapter-only expectation.  
* Evidence layout single-home expectation: Drift (multi-home evidence structure observed).

---

## Negative-Claim Proof Appendix

I minimized “not found” assertions; where checked explicitly:

1. adapter/http/app.py not found  
   * Searched token/path: adapter/http/app.py  
   * Method: direct file read attempt (sed \-n ... adapter/http/app.py)  
   * Scope: repo root  
   * Result: sed: can't read adapter/http/app.py: No such file or directory (0 file found).  
2. adapter/http/routes.py not found  
   * Searched token/path: adapter/http/routes.py  
   * Method: direct file read attempt (sed \-n ... adapter/http/routes.py)  
   * Scope: repo root  
   * Result: sed: can't read adapter/http/routes.py: No such file or directory (0 file found).  
3. engine/db.py not found (db is a package directory instead)  
   * Searched token/path: engine/db.py  
   * Method: direct file read attempt (sed \-n ... engine/db.py) \+ file listing under engine/  
   * Scope: repo root  
   * Result: sed: can't read engine/db.py: No such file or directory; listing shows engine/db/\_\_init\_\_.py, engine/db/adapter.py, engine/db/errors.py.

---

### Commands used (audit trace)

* pwd  
* git rev-parse HEAD  
* git rev-parse \--abbrev-ref HEAD  
* git status \--porcelain  
* date \-u \+%Y-%m-%dT%H:%M:%SZ  
* uname \-srmo  
* python \--version  
* node \--version  
* find . \-maxdepth 1 \-mindepth 1 | sort  
* find adapter \-maxdepth 3 \-type f | sort  
* find engine \-maxdepth 2 \-type f | sort  
* find docs/evidence \-maxdepth 2 \-type f | sort  
* find artifacts \-maxdepth 2 \-type f | sort  
* find audit \-maxdepth 3 \-type f | sort  
* find ci \-maxdepth 3 \-type f | sort  
* find tests \-maxdepth 3 \-type f | sort  
* rg \-n "Blueprint|@bp.route|register\_blueprint|compat\_blueprint|..."  
* sed \-n on key files (pyproject.toml, run\_flask.py, adapter/factory.py, adapter/http\_reader.py, engine/cli/main.py, engine/http/compat\_handler.py, engine/sampler/core.py, engine/compat/compute.py, engine/presenter/emitter.py, engine/bodygraph/ingest.py, engine/bodygraph/vendor\_client.py).

