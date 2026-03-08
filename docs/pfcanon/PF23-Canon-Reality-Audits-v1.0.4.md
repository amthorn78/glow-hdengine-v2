# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.4

**Status:** Canon

**Effective date:** 2026-02-21

**Last Update Gate:** HDE-EPIC026

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

**Date:** 2026-02-21

**Last Epic:** HDE-EPIC026

# **Audit Snapshot Metadata**

* Repo root confirmed: `/workspace/glow-hdengine-v2` (from `pwd`).  
* Commit: `2d7ebdc87547dbd9e2130ca608b9a4a5a8d38602` (from `git rev-parse HEAD`).  
* Working tree cleanliness: clean (`git status --porcelain` returned no changed paths).  
* Branch: `work` (from `git rev-parse --abbrev-ref HEAD`).  
* Timestamp (UTC): `2026-02-21T01:21:39Z`.  
* Execution environment facts:  
  * OS/kernel: Linux 6.12.47 ... x86\_64 GNU/Linux  
  * Python: Python 3.10.19  
  * Node: v22.21.1

---

# **Top-level Repo Map**

## **Architecture-critical families (presence \+ role summary)**

* `engine/` — Present. Contains core compatibility logic, sampler, bodygraph ingest/resolver/vendor client, DB adapter, runtime determinism env, HTTP compat blueprint, and CLI implementation.  
* `adapter/` — Present. Flask app factories and HTTP surfaces (reader, aux narrative, internal/version, ops/dev routes), plus env guard and logging filter integration.  
* `presenter/` — Present. Reader-v1 emitter and canonical JSON compare helper module (CLI utility).  
* CLI package location(s) — Present. `pyproject.toml` exposes `hdctl=engine.cli.main:cli`; CLI entry module is in `engine/cli/` and has `__main__.py` launcher.  
* `docs/` — Present. Includes evidence index, endpoint catalog, acceptance/architecture/contracts/schemas, and PF canon directory.  
* `artifacts/` — Present. Holds machine evidence/index mirror, presenter/CLI artifacts, math/release identity artifacts, and many audit outputs.  
* `audit/` — Present. Contains gates, epic QA roots, close-pack docs, and QA logs/manifests hierarchy.  
* `tools/` — Present. Evidence generation/validation tools, QA harnesses, showcompat artifact generators, registry report generator, config generators.  
* `ci/` — Present. Check scripts for env pins, evidence mirror hash/schema, LF endings, release identity, and CLI help checks.  
* `.github/workflows/` — Present. CI jobs include closed-rails test, epic020 suites, compat-http, evidence bundles, sanity pipeline.  
* `tests/` — Present. Extensive test roots spanning adapter/http, CLI, evidence, determinism, DB/provider, QA harnesses, endpoint catalogs.  
* `scripts/` — Present. Operational/dev scripts (dev reader start, release-id recompute, ingest jobs, QA scripts, DB scripts).

## **Expected family classification (explicit)**

* `engine/`: Present.  
* `adapter/`: Present.  
* `presenter/`: Present.  
* CLI package: Present (`engine/cli`, `pyproject.toml` `[project.scripts]`).  
* `vendor/` (top-level expected): Not found as top-level package; vendor seam exists under `engine/bodygraph/vendor_client.py` and related bodygraph modules.  
* DB layer: Present but nested as `engine/db/` (not top-level `db/` package for runtime code).

## **Root discipline capture (truth-home-like roots observed)**

Observed roots that hold governed/audit-like material:

* `audit/`  
* `artifacts/`  
* `docs/` (including `docs/evidence` and endpoint catalog)  
* generators/checks in `tools/` and `ci/checks/`  
* supporting operational scripts in `scripts/`

---

# **Packaging and Entrypoints**

## **Packaging/build config**

* `pyproject.toml`: setuptools build backend, project glow-hdengine, and console script `hdctl = engine.cli.main:cli`; package discovery includes `engine*`, `adapter*`, `presenter*`.  
* `requirements.txt`: runtime deps include psycopg, Flask, gunicorn.  
* `requirements-dev.txt`: test deps include pytest, pytest-cov, pytest-mock, and jsonschema.

## **Entrypoint inventory**

HTTP startup (factory):

* `adapter.wsgi:create_app` creates Flask app and mounts reader \+ compat blueprints.  
* `adapter.factory:create_app` mounts reader blueprint at root; referenced by Procfile and run scripts.

CLI startup:

* Console script `hdctl` → `engine.cli.main:cli`.  
* `engine/cli/__main__.py` calls `cli()` and exits with its code.

Evidence/indexing entrypoints (invoked by CI):

* `tools/evidence/run_sanity_pipeline.py`  
* `tools/evidence/update_evidence_index.py`  
* `tools/evidence/run_canonical_json_gate.py`

---

# **Engine Modules**

## **Sampler**

Module: `engine/sampler/core.py`

* build\_candidate\_pool: zero-weight filtering \+ eligibility filtering, builds candidate pool entries.  
* rank\_candidates: deterministic rank by weight, compat score, band priority, ID comparator tie-breaker.  
* sample\_and\_rank: helper chaining pool build then rank.

## **Core compute**

Module: `engine/compat/compute.py`

* compat\_public: computes category scores and bands from canonical pair key; returns categories \+ meta envelope.  
* conjunction\_public / conjunction\_public\_resolved: conjunction contract payload with normalization and resolver path (local lookup then bodygraph resolve).

Module: `engine/compat/ordering.py`

* normalize\_pair: AB↔BA canonical ordering by UID then stable payload hash tie-break.  
* pair\_key: normalized key builder.

## **Determinism hazards inventory (audited paths)**

Observed in sampled engine paths:

Time usage

* time.strftime/time.gmtime in ingest/vendor logs; time.monotonic used for durations/retry deadline.

Randomness without seeding

* Not observed in sampled engine modules (engine/sampler/core.py, engine/compat/compute.py, engine/bodygraph/\*, engine/runtime/determinism\_env.py) via token search (rg \-n "random|randint|uuid4|secrets" over engine/) with no relevant random module usage in those sampled files.

Network calls

* Vendor client uses urllib.request POST and error handling around network failures/timeouts.

File I/O

* Evidence/log append and artifact writes in ingest and DB adapter snapshot writer.

Iteration ordering

* Deterministic sorted key serialization is used in canonical emitters (sort\_keys=True default).

---

# **Adapter / HTTP Surfaces**

## **Route registration map**

App/router creation \+ mounts

* adapter.wsgi:create\_app registers reader\_bp and compat\_blueprint (compat has /api/compat/v1 prefix).  
* adapter/http\_reader.py:create\_app similarly registers bp and compat\_blueprint.

Mounted groups

* Reader \+ aux \+ internal/ops/dev routes on bp (root-mounted).  
* Compat writer routes under /api/compat/v1.

## **Surface classification**

Reader-like JSON success

* /reader returns reader payload with ETag/conditional semantics (dev-gated in handler).

Aux/narrative

* /api/aux/narrative and /aux/narrative return text/plain narrative payloads with headers and ETag behavior based on suppression path.

Admin/internal

* /internal/version, /internal/healthz, /internal/readyz, /ops/writer/diagnostic and ops probes.

Dev/diagnostic harness

* /internal/dev/sampler, /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction with \_dev\_admin\_gate APP\_ENV gating.

## **Transport semantics hooks**

HEAD vs GET parity

* /reader: explicit HEAD branch with empty body and content-length logic; 304 conditional branch on If-None-Match strong match.  
* /internal/version: GET/HEAD with HEAD content-length equal to GET bytes and no body.  
* Compat writer: HEAD/OPTIONS return transport guard responses (Allow, Content-Length=0).

Conditional responses / 304

* /reader checks parsed If-None-Match and returns 304 with empty body path.

ETag generation/quoting

* /reader: etag \= """ \+ sha256 \+ """, assigned to headers.  
* Aux narrative uses resp.set\_etag(digest) and explicit quoted ETag header set.

Cache-Control rules

* WSGI/common headers default Cache-Control: no-store; reader/aux set route-specific cache directives; compat writer sets no-store.

Content-Type rules

* JSON responses set application/json; charset=utf-8; aux narrative uses text/plain; charset=utf-8; writer head/options remove content-type for empty transport responses.

---

# **Presenter / Emitter**

* Primary canonical emitter: `engine/presenter/emitter.py`  
  * emit\_public delegates to canonical serializer; default sorted keys for determinism.  
  * emit\_public\_with\_envelope and alias emit\_compact\_json provided.  
* Serializer implementation: `engine/stable/sercanon.py`  
  * compact separators, optional sorted keys, exactly one trailing newline enforced by serialize.  
* Reader-specific envelope emitter: `presenter/reader_v1/emitter.py`  
  * builds reader preimage, computes idempotence\_hash, emits final bytes via engine presenter emitter.  
* Callers  
  * HTTP compat uses emit\_public; HTTP reader/internal uses emit\_public.  
  * CLI showcompat emits via emitter.emit\_public(...).  
  * Runtime reader path uses presenter.reader\_v1.emit\_reader\_v1.

---

# **CLI Surfaces**

Definition style: argparse in `engine/cli/main.py` with subparsers and required command selection.

Primary commands found

* showcompat (args include pair/file modes, source selection, conjunction mode, viewer prefs, user/birth inputs).  
* aux-preview (narrative preview args).

Entrypoint symbol

* cli(argv=None) \-\> int with parse and typed error exit behavior (64 usage, 1 unexpected).

Call chain (high-level)

* cli \-\> handler(showcompat) \-\> source loading (db/vendor/auto/files/stdin) \-\> compat\_public / conjunction resolver \-\> presenter emit \-\> stdout \+ optional dumps.

Output surfaces

* stdout bytes via \_emit\_stdout\_bytes (enforces LF and rejects CRLF).  
* optional reader file dump (--dump-reader) to path, and admin proof dumps (--dump-admin-dir).

Missing-args / parse failure exit

* argparse SystemExit mapped to exit 64 on parse errors; no handler also returns 64\.

---

# **Vendor Seam & BodyGraph Storage**

## **Vendor client**

Vendor HTTP seam module: `engine/bodygraph/vendor_client.py`

* HdApiClient.from\_env requires HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY.  
* build\_request shapes POST /bodygraphs request; fetch performs retries/timeouts/error mapping.

Resolver/ingest integration

* ingest\_vendor\_bodygraph instantiates client from env and fetches vendor result before DB persistence path.

## **BodyGraph persistence/caching**

DB layer: `engine/db/adapter.py` (DBAccess.for\_current\_env)

* selects psycopg vs bridge based on env and guards; snapshot of provider-selection written to artifact path.

Persistence logic: `engine/bodygraph/ingest.py`

* writes to hde.body\_graphs with ON CONFLICT DO NOTHING; queries row count and payload fetch by (user\_id,vendor,vendor\_version,input\_fingerprint).

Keying/idempotency visible

* idempotency\_key \= f"{user\_id}:{vendor}:{vendor\_version}:{fingerprint}".

## **Offline/vendor gating posture**

* Ingest rejects when SAFE\_MODE true or ALLOW\_NETWORK false with PROVIDER\_REFUSED / PROVIDER\_NETWORK\_BLOCKED.  
* Resolver vendor path enforces same posture before calling ingest/vendor path.

---

# **Evidence, Indices, Catalogs**

## **Evidence homes inventory**

* docs/evidence/: human index and hash sentinel with path proofs, plus epic evidence markdowns.  
* artifacts/: machine index mirror (evidence\_index.jsonl), plus many generated audit/proof directories.  
* audit/: gate logs (audit/gates/**) and epic QA roots (audit/qa/**) referenced by CI and tools.

Mixed/generated indicator

* Tooling explicitly writes/validates these indices (update\_evidence\_index.py, check\_mirror\_schema.sh, sanity pipeline hooks).

## **Evidence index structures**

* docs/evidence/INDEX.json: human-readable index records (artifact metadata objects).  
* docs/evidence/INDEX.sha256: hash sentinel companion (file present in docs/evidence set).  
* artifacts/evidence\_index.jsonl: machine mirror JSONL with per-artifact records including proof anchor and sha fields.

Regeneration/validation tooling

* tools/evidence/update\_evidence\_index.py declares paths for human index, hash sentinel, and mirror path constants.  
* CI runs check\_evidence\_index\_hash.sh and check\_mirror\_schema.sh.

## **Endpoint catalog**

* Catalog path: docs/ENDPOINTS\_CATALOG.json  
* Shape includes endpoints array with path/method/classification/env\_gate/rails metadata; includes compat and dev conjunction routes.  
* Mirror path: artifacts/audit/ENDPOINTS\_CATALOG.json (file exists per listing).

Referenced by tests

* tests/http/test\_endpoint\_catalog.py loads docs catalog and asserts compat \+ dev conjunction entries and classifications.

## **Proof/snapshot artifacts**

Examples found in evidence mirror rows

* artifacts/proofs/success\_get.txt, success\_head.txt, success\_304.txt, and success\_writers\_errors.txt appear as indexed artifacts with proof anchors.

Producer evidence

* Index/mirror update tool is explicit writer for index structures; specific proof producers are represented as indexed artifacts and CI evidence steps, including sanity/index refresh pipeline.

---

# **Tests, QA Harness, CI/Checks**

## **Tests map (selected loci)**

Reader/HTTP contract tests

* tests/adapter/test\_reader\_parity.py: validates /reader GET/304/HEAD behavior, ETag format, and cache/vary semantics.

CLI canonical/parity

* tests/cli/test\_showcompat\_parity\_and\_identity.py: exercises showcompat invocation and canonical bytes/parity artifacts path usage.

Evidence/determinism pipeline

* tests/evidence/test\_sanity\_pipeline.py: asserts sanity log includes closed-rails env line and pass/fail checks.

Endpoint catalog consistency

* tests/http/test\_endpoint\_catalog.py: checks catalog entries for compat and dev conjunction endpoints.

## **CI workflows**

Workflow file: .github/workflows/ci.yml

* test job: closed rails env, env pins check, CLI guards, canonical JSON gate, index/mirror checks, targeted pytest suites.  
* epic020, compat-http-epic020, epic020-evidence-bundles, sanity-pipeline jobs run acceptance suites and evidence/index tooling under closed rails.

## **Script/check inventory (QA-relevant)**

* ci/checks/check\_env\_pins.sh: invokes determinism env CLI with check-log mode against audit gate log.  
* ci/checks/check\_release\_identity.sh: validates canonical manifest bytes, freeze-pack identity copy, release id, and recompute check subprocess.  
* tools/evidence/run\_sanity\_pipeline.py: orchestrates deterministic step list and writes artifacts/sanity/sanity.log including env pins line.

---

# **Flows & Call Chains**

## **Reader success flow (HTTP)**

adapter/http\_reader.py:reader\_v1 → engine/runtime/public.py:emit\_reader\_public\_bytes → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine/presenter/emitter.py:emit\_public

* /reader validates query/env, loads charts, computes body bytes via emit\_fn (default reader public bytes), sets ETag/headers, and returns 200/304/HEAD paths.  
* Reader runtime computes harmony band from ts\_v0 and builds enriched envelope before reader-v1 emitter call.  
* Reader emitter computes idempotence hash from preimage and emits final canonical bytes.

## **Compat API flow (HTTP)**

adapter/wsgi.py:create\_app (mount) → engine/http/compat\_handler.py:post\_json → engine/compat/compute.py:compat\_public → engine/presenter/emitter.py:emit\_public

* Compat blueprint mounted at /api/compat/v1; POST validates payload/viewer prefs and computes compat categories/meta, then emits writer payload with no-store headers.  
* GET/HEAD/OPTIONS transport behavior is explicitly defined with writer guard paths.

## **CLI showcompat flow**

engine/cli/main.py:cli → showcompat → source loaders (\_load\_from\_source / \_load\_from\_files\_or\_stdin) → engine/compat/compute.py:compat\_public → engine/presenter/emitter.py:emit\_public

* Parser binds showcompat command and arguments for source/file/conjunction modes.  
* showcompat resolves input parties from db/vendor/auto/files/stdin and computes compat payload \+ optional reader/admin dumps; emits canonical bytes to stdout with LF guards.

## **Vendor acquisition \+ bodygraph ingest flow**

engine/compat/compute.py:conjunction\_public\_resolved → engine/bodygraph/resolver.py:resolve\_bodygraph → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.fetch → engine/db/adapter.py:DBAccess

* Conjunction resolved path attempts local lookup first, then vendor resolver path when needed, raising typed vendor errors on failures.  
* Resolver enforces SAFE/network posture before vendor ingest call path.  
* Ingest fetches vendor payload, computes hashes/idempotency key, and persists/re-reads DB payload for parity check in non-dry-run path.

## **Evidence index update/validation flow**

tools/evidence/run\_sanity\_pipeline.py:run\_pipeline → tools/evidence/update\_evidence\_index.py:main → docs/evidence/INDEX.json \+ docs/evidence/INDEX.sha256 \+ artifacts/evidence\_index.jsonl; validated by ci/checks/check\_mirror\_schema.sh

* Sanity pipeline includes update-index and orientation steps in default step list and writes sanity log with env pins info.  
* Update tool defines canonical target paths for human index, hash sentinel, and mirror JSONL.  
* CI executes mirror schema/hash checks after index update/check commands.

---

# **Drift and Reality vs Expectations**

Directory/architecture drift

* Observed: expected layers exist (engine, adapter, presenter) and are all active.  
* Anchor: package discovery includes all three families and code imports cross these layers.  
* Impact (neutral): split is present; runtime coupling spans both engine.presenter and top-level presenter.reader\_v1, so emitter responsibilities are distributed across two namespaces.

Surface drift

* Observed: compat API has GET route returning {ok,schema} alongside POST writer behavior, while catalog test expects compat endpoint as internal POST-only entry.  
* Anchor: compat GET handler exists in code; endpoint catalog tests assert internal-admin POST posture for /api/compat/v1.  
* Impact: creates a difference between route implementation breadth and catalog assertions for primary method posture.

Evidence drift

* Observed: evidence/governed-like material appears across multiple roots (docs/evidence, artifacts, audit, plus check/tooling under tools and ci/checks).  
* Anchor: index files and CI/tooling references show multi-root evidence flow.  
* Impact: multiple roots mean reviewers must trace governance state across several locations.

Determinism drift

* Observed: explicit closed-rails enforcement exists, but vendor/ingest modules contain clock and network logic (used under gated paths).  
* Anchor: determinism pins and guard tooling exist; vendor client uses network/monotonic time and ingest logs UTC timestamps.  
* Impact: determinism posture depends on gate enforcement and invocation mode selection.

Vendor seam drift

* Observed: no top-level vendor/ runtime package; vendor seam is in engine/bodygraph/vendor\_client.py plus resolver/ingest call path.  
* Anchor: vendor client and resolver integration modules under engine/bodygraph.  
* Impact: vendor boundary is implemented, but located within engine subtree rather than separate top-level vendor package.

Path-case drift

* Observed: mixed naming styles across roots (e.g., uppercase manifest/report filenames and lowercase tree dirs).  
* Anchor: CI and tooling reference uppercase close-report/manifests (EPIC-024\_\*, etc.) under audit/.  
* Impact: naming heterogeneity increases path lookup variance in scripts/reviews.

Root proliferation

* Observed: 6 primary governance-related roots observed in active flows: audit/, artifacts/, docs/, tools/, ci/checks/, scripts/.  
* Anchor: CI workflow and evidence tools explicitly read/write/validate across these roots.

---

# **Negative-Claim Proof Appendix**

Top-level vendor/ directory not found

* Token searched: vendor directory at repo root  
* Method: find . \-maxdepth 1 \-type d \-name 'vendor' \-print  
* Scope: repo root  
* Result: 0 hits

setup.py / setup.cfg / root package.json not found

* Token searched: setup.py, setup.cfg, package.json  
* Method: find . \-maxdepth 1 \-type f ( \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'package.json' ) \-print  
* Scope: repo root  
* Result: 0 hits

No explicit random module usage in sampled engine deterministic paths

* Token searched: random|randint|uuid4|secrets  
* Method: rg \-n "random|randint|uuid4|secrets" engine/ (review focus on sampler/compat/runtime/bodygraph files cited above)  
* Scope: engine/  
* Result: no relevant hits in sampled modules cited in Determinism Hazards section

---

# **Commands executed (audit checks)**

* ✅ pwd && git rev-parse HEAD && git status \--porcelain && git rev-parse \--abbrev-ref HEAD && date \-u \+"%Y-%m-%dT%H:%M:%SZ" && uname \-srvmo && python3 \--version && node \--version  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-printf '%P\\n' | sort  
* ✅ find . \-maxdepth 2 ( \-name 'pyproject.toml' \-o \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'requirements\*.txt' \-o \-name 'Pipfile' \-o \-name 'poetry.lock' \-o \-name 'package.json' ) \-print | sort  
* ✅ rg \-n "Flask(|FastAPI(|APIRouter(|Blueprint(|create\_app|app \= Flask|if **name** \== '**main**'|uvicorn|gunicorn" ...  
* ✅ find engine \-maxdepth 3 \-type f | sort  
* ✅ rg \-n "@bp.|Blueprint(|register\_blueprint|url\_prefix|@app.|route(" adapter/http\_reader.py engine/http/compat\_handler.py ...  
* ✅ find docs \-maxdepth 2 \-type d | sort ...; find artifacts ...; find audit ...  
* ✅ find .github/workflows ...; find ci/checks ...; find tools \-maxdepth 2 ...  
* ✅ find tests \-maxdepth 3 \-type f | sort  
* ✅ find . \-maxdepth 1 \-type d \-name 'vendor' \-print  
* ✅ find . \-maxdepth 1 \-type f ( \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'package.json' ) \-print

