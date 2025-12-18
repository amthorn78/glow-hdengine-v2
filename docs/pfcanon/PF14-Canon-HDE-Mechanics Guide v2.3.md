1. ## Document Control 

## 0.1 **Header**

 **Title:** PF14-Canon-HDE-Mechanics Guide  
 **Version:** v2.3  
 **Status:** Canon  
**Effective date:** 2025-12-17

**Last Update Gate:** BN 8.3.4 Drain A1-5  
 **Invocation tag:** INV-f2ac55d77ce9aacc

---

## 0.2 Purpose — Components & build tasks (mechanics scope)

 Mechanics is the **mechanical schematic** for the HD Engine and its tooling. This guide is the single place where we enumerate and describe **every component and build task that must exist in the engine repo** so that the Engine can run, be tested, and be proven for production.

This guide:

* Describes components, jobs, tools, and build tasks that must exist in the engine repo (including adapters, CLI, evidence tools, QA harnesses, and sanity/rails checks). This includes operational and infrastructure components as well as software.

* Specifies **mechanical responsibilities only**: what must be wired, what artifacts must be produced, and what evidence must be captured and checked.

* Does **not** restate math formulas or public transport bytes; those live in their single-home PF documents and are referenced here by title only. When a mechanic depends on math or transport, this guide names the component and its responsibilities and routes the details to the owning PF doc.

Public posture (Reader v1).  
 For Reader v1, this guide assumes and enforces:

* Bands-only, numeric-free public payloads (numbers remain admin-only).

* Resonance posture: SR-only (α \= 1.0).

* Hysteresis \= 1 is armed for future XR but not exposed in this version.

Routing rules.

* Cross-references in this guide are **titles-only** (no version numbers in prose).

* Single homes (route by title; do not duplicate):

  * Public bytes & HTTP contracts: **HDE-CLI-API-Vendor-Ref**

  * Math & algorithms: **HDE-Math-Spec**

  * Schemas, packs/manifests, canonical JSON, Evidence Index & Machine Mirror: **HDE-Schemas & Artifacts**

  * Governance, acceptance gates, A7/ops posture: **HDE-Governance**

References (titles-only).  
 This guide assumes, and routes mechanical responsibilities to, the following PF documents:

* **HDE-Governance**

* **HDE-CLI-API-Vendor-Ref**

* **HDE-Math-Spec**

* **HDE Architecture**

* **Glow Development Philosophy**

* **HD Engine Epics Map** (historical; epic planning now lives in **HDE-Phased Epics** by title)

* **Glow HD Engine — Build Notes & Integration Addenda (Living)**

Provenance & deltas (informative).  
 Mechanics here have been canonicalized from REVIEW addenda and aligned with **Glow HD Engine — Build Notes & Integration Addenda (Living)**. In particular, this guide:

* Rolled in previously optional items (Server Cache; Reader conditional-GET helper).

* Locked the A7 transport posture.

* Added the `/internal/version` ops posture (no-store, no ETag, conditionals ignored; HEAD 200 with `Content-Type` parity).

* Clarified optional `build_commit`.

* Expanded Evidence Index captures to require same-PR updates, Machine Mirror parity, and path-proofs.

This document should be read as the **full mechanical schematic** of the HD Engine and its repo: if a component, job, harness, or governed artifact must be built and kept working, it is accounted for here and wired by reference to its canonical PF homes.

---

## 0.3 Preamble — Product scope

Viewer inputs & presets.  
 Viewer presets are optional templates. Each viewer:

* Selects a top category from the closed Magic-10 set.

* Sets weights in the range `0..100` across the ten Magic-10 IDs (closed set and order; see **HDE-Schemas & Artifacts** §2.6 and **HDE-Math-Spec** §5.1 by title).

* Zero-weight rule: if a viewer sets a category’s weight to `0`, candidates whose \#1 category is that category are excluded.

Engine outputs (internal/admin).  
 Internally, the engine:

* Computes per-category numbers in `0..100`.

* Maps those numbers to bands (Cool, Open, Warm, Glow) using inclusive-high thresholds and `round_half_up` (see **HDE-Math-Spec** §5.3 by title).

* Selects two narrative keys per category (personal, shared).

The engine selects keys; it does not write copy. Resonance posture for v1 is SR-only (α \= 1.0); XR is dormant and not part of public output.

Public covenant (titles-only).

* Public Reader payloads are bands-only and numeric-free; underlying numbers remain admin-only.

* Public bytes & schemas live in **HDE-CLI-API-Vendor-Ref** by title.

Canonical JSON is required end-to-end:

* UTF-8, no BOM

* ASCII-sorted keys

* Compact separators

* Exactly one trailing LF

* Arrays used as sets are deduped and ASCII-sorted

Determinism posture:

* AB↔BA parity holds for pair-sensitive flows.

* Two-run identity holds under determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

* Reader↔CLI parity is required wherever both surfaces exist.

Math, transport, and ops details are routed to their single homes by title; this guide records the **mechanics expectations at the component level** (what must exist, how it plugs together, and what it must emit) and does not duplicate contracts or formulas.

## 0.4 HD Engine — the plain story

**What it is**

The HD Engine computes per-category compatibility and drives which copy lines appear. It selects and routes copy via a deterministic system. It does not generate text.

**What it is for**

* Power connection matching from user priorities and weights across ten categories.  
* Give explanations, not only scores: two short narrative lines per category (one personal, one shared) chosen by rules (no HD jargon in user copy).  
* Let admins tune numbers safely while user-visible results remain stable and **understandable.**

**What it does**

* Compute pair results across ten categories

  * A number from 0 to 100 per category for admin/test.  
  * A band per category (Cool, Open, Warm, Glow) derived from the number.  
* Drive narrative output (no copywriting)

  * Produce narrative keys and selection signals for each category and perspective (personal/shared) using viewer intent and routing flags.  
  * Determinism and AB↔BA parity for pair views.  
* Respect user intent

  * User chooses \#1 category and weights; zero-weight rule enforced.  
* Return stable compact JSON

  * Admin/test JSON may include per-category numbers and bands with narrative keys and minimal meta.  
  * Public Reader remains bands-only; public payload bytes are defined in CLI/API.  
* Support the swipe/feed

  * Rank candidates by viewer weights and diversify results.

**What it does not do**

* No copywriting; the engine selects keys only.  
* No public UI; the engine sits behind the app.  
* No direct Internet exposure.  
* No business policy beyond inputs; app controls product flow.

---

# 1\) Repository & Tooling Skeleton (capabilities, not paths)

**Scope (normative).** Mechanics requires a **set of capabilities** that enable determinism, transport acceptance, and evidence generation. The **concrete repository layout, file names, and tool targets are implementation-defined** and **must not be pinned** here. This section states *what must exist*, not *where or how*.

## 1.1 Capabilities the repo must provide

* **Adapter surface (HTTP only).** Wires Reader routes and the ops endpoint; **does not define public bytes** (route by title to PF-Canon-HDE-CLI-API-Vendor-Ref).  
* **Mechanics core.** Pure orchestration for math, comparators, config loader, and public emitter wiring (route math to PF-Canon-HDE-Math-Spec).  
* **Schemas & validation.** JSON-Schema validation for governed inputs; AJV (or equivalent) CI step that fails on schema drift (route schema/canonical rules to PF-Canon-HDE-Schemas & Artifacts).  
* **Evidence indices.**  
  * **Human index** (titles/paths only) in this repo, **updated in the same PR** as artifacts.  
  * **Machine JSONL mirror** (records-only) owned by PF-Canon-HDE-Schemas & Artifacts; CI enforces **1:1 parity** and **path-proofs** for every record.  
* **Ops artifacts.** Start-command capture (bytes \+ hash), health/ready checks; no secrets in logs; SAFE rails defaults enforced per Governance.  
* **Scriptable pipeline.** A single **sanity pipeline** (name is implementation-defined) that runs, in order: formatting → lint/type → unit/prop tests → schema checks → goldens/evidence capture → **index & mirror parity \+ path-proof validation**.

## 1.2 Environment & secrets (names-only)

**Env allow-list.**  
 Defined by title (HDE-Schemas & Artifacts / HDE-Governance). CI **fails** on unknown or missing required keys; secrets are never printed (keys-only logs with redaction).

**Rails posture (derives from PF07).**  
 Rails defaults follow the **Env Deployment Inventory** (titles-only): **dev & stage OPEN**, **prod CLOSED**, **CI CLOSED**. This guide does not restate the table; it defers to Infrastructure.

**CI default CLOSED & evidence.**  
 CI pipelines run with rails **CLOSED by default**. Any pre-commit/CI job that **opens rails** must pin timeout/retry/backoff policy (closed domain) and attach governed evidence **in the same PR** (titles-only routing to Governance/Schemas & Artifacts).

**Determinism pins (all environments).**  
 Any canonicalization, hashing, header snapshotting, or governed evidence capture **MUST** run with:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

Acceptance (names-only): `ENV_LC_ALL_C_OK`.

## 1.3 Evidence & CI coupling \[Required-Now\]

**Scope (normative).** Mechanics must keep human and machine evidence in lockstep for every artifact this guide produces (math proofs, goldens, headers‑only snapshots, scripts). Transport bytes and ops surfaces are routed by title only to **HDE‑CLI‑API‑Vendor Ref** and **HDE‑Governance**.

**Single homes**  
 **Human index.** `docs/evidence/INDEX.json` — titles and paths only; no payload bytes. Must maintain **1:1 parity** with the machine mirror (see §8.3).  
 **Machine mirror (records‑only).** `artifacts/evidence_index.jsonl` — fixed path; one JSON object per line; canonical JSON (UTF‑8, no BOM; sorted keys; compact; exactly one trailing `\n`). This section surfaces the minimum shape used by implementers; the **normative mirror schema lives in PF12**.

**Mirror discipline (normative).** The machine mirror is **one and only one** file at `artifacts/evidence_index.jsonl`; **records‑only canonical JSONL** (UTF‑8; **ASCII‑sorted keys**; compact; **exactly one LF per record**); **unknown keys are rejected**; **sort‑before‑write** by (`artifact_key`,`discovered_physical_path`).  
 **Exact field order (per PF12/PF10):**  
 `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

**Join rule.** (`artifact_key`, `discovered_physical_path`) in the mirror equals (`title`, `path`) in the human Index (**1:1**).  
 **Unknown keys.** Rejected (**fail CI**).

**Path‑proofs (MUST).** Store a `path_proof.txt` (or equivalent) alongside each artifact with a stat transcript (size, mtime, sha). Reference it via `proof_anchor` in the mirror record.

**Update discipline (same PR).** Whenever any golden, snapshot, or script moves or changes, **update Appendix D and the machine mirror in the same commit/PR**. CI fails on mismatch.

**Environment pins (determinism).** All captures and comparisons run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Arrays that represent sets are deduped and ASCII‑sorted before hashing and compare.

**Pipeline coupling (minimum sequence).**

1. Build and normalize.

2. Run unit and property tests.

3. Produce artifacts (goldens, headers‑only snapshots, logs).

4. Write or refresh **human Index** entries.

5. Write **mirror** records with path‑proofs.

6. CI parity check: 1:1 human↔machine, schema‑valid, canonical JSONL.

7. Fail closed on any drift.

**Acceptance and CI (titles‑only; token names live in HDE‑Governance §2.0).**  
 `EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_MIRROR_OK · EVIDENCE_PATHS_VALIDATED_OK · JSON_CANONICAL_CHECK_OK · EVIDENCE_INDEX_HASH_OK · MACHINE_MIRROR_UPDATED_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK · ENV_LC_ALL_C_OK`. *(Schema & tokens routed by title to PF12/PF09; this guide does not restate the mirror schema.)*

**Header snapshot normalization:** stored snapshots use **lower‑case header names**; values verbatim. **Acceptance:** `SNAPSHOT_HEADER_LOWERCASE_OK`.

**Routing (titles‑only).** Manifest and release identity and the mirror schema ownership live in **HDE‑Schemas & Artifacts**. Transport A7 proofs and `/internal/version` evidence live in **HDE‑CLI‑API‑Vendor Ref** and **HDE‑Governance**.

**Governed locations (normative).**

All QA/audit proofs **MUST** reside under governed paths:

* `artifacts/**`

* `audit/**`

* `docs/evidence/**`

Files under transient generators (for example, `codex/out/**`) **MUST NOT** be indexed. Human Index and Machine Mirror updates **MUST** occur in the **same PR**; the mirror is **records-only canonical JSONL** (UTF-8, ASCII-sorted keys, compact, exactly one LF), rejects **unknown keys**, and carries a `proof_anchor` to a path-proof file in the same directory. Mechanics must gate on `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, and `EVIDENCE_INDEX_HASH_OK` (schema and token semantics routed by title to **HDE-Schemas & Artifacts** and **HDE-Governance**).

**Core evidence must remain text-based and agent-readable.**

Core governed evidence for the HD Engine — including:

* the Human Evidence Index (`docs/evidence/INDEX.json`),

* the Machine Mirror (`artifacts/evidence_index.jsonl`),

* any evidence **bundles** and their **manifests**, and

* key QA logs and summary artifacts referenced by this guide —

**MUST** be stored as plain-text, UTF-8 files under these governed paths and remain suitable for inspection by humans and Codex/ChatGPT-class agents at the PR level. Binary or compressed bundles (for example, `.zip`, `.tar.gz`) MAY be produced as supplementary artifacts for local convenience, but **MUST NOT** serve as the only governed evidence for any acceptance token that relies on Engine evidence; there must always be at least one text-based bundle manifest, log, or summary file under a governed path that covers the token’s evidence needs.

This posture ensures that the ledger-centric evidence model (Human Index, Machine Mirror, bundle manifests, and QA logs) remains readable and auditable by both humans and automated agents, and it aligns Mechanics with the evidence and Reality Audit guidance in **HDE-Schemas & Artifacts**, **Glow QA Guide**, and the Reality Audits PF by title.

### **1.3.1 Evidence jobs (single-writer tools)**

**Scope (normative).**  
 Only a **small set of evidence tools** may write governed evidence artifacts (ordering artifacts, Evidence Index, Machine Mirror, bundles/manifests, and path-proofs). All other code — including tests and ad-hoc scripts — **MUST NOT** modify governed evidence directly.

**Evidence tools (titles-only).**

* **Ordering generator.**

  * A single ordering generator tool (for example, `tools/order/generate_ordering_artifacts.py`) is the **single writer** for ordering artifacts under `artifacts/engine/order/**` (for example, sorted snapshots, ordering logs, ABBA evidence).

* **Evidence skeleton tools.**

  * `tools/evidence/update_evidence_index.py` is the **single writer** for:

    * `docs/evidence/INDEX.json` (Human Index, titles/paths only),

    * `docs/evidence/INDEX.sha256` (hash sentinel),

    * `artifacts/evidence_index.jsonl` (Machine Mirror), and

    * governed `*.path_proof.txt` transcripts for artifacts listed in this guide.

  * In addition to per-artifact entries, `tools/evidence/update_evidence_index.py` **MUST**:

    * ingest one or more **bundle manifests** emitted by the bundle generator (see below),

    * compute hashes for bundle files and manifests under the same determinism pins as other evidence (§1.2),

    * write **bundle-level** Machine Mirror rows and bundle path-proofs for those bundles, and

    * preserve behaviour for non-bundled evidence families (backwards-compatible for legacy rows).

  * Index \+ Mirror parity checks (§1.3) **MUST** treat bundle rows and manifests as first-class governed artifacts: manifests must be valid JSON/JSONL, conform to the PF12 bundle manifest schema, contain no unknown keys, and obey any bundle-level invariants (for example, member count and deterministic ordering) defined there.

  * `tools/evidence/orientation_demo.py` owns the topology orientation demo artifact (`audit/gates/topology/orientation_demo.txt`) and its path-proof and **MUST NOT** be bypassed by ad-hoc edits.

* **Evidence bundle generator.**

  * A dedicated **bundle generator tool** (titles-only here; concrete name and path live in the repo) is responsible for:

    * collecting raw evidence outputs for one or more high-churn families (for example, ordering logs, sampler/core outputs, complex config dumps),

    * building a **textual bundle** (for example, JSONL, one logical artifact per line) under a governed path (`artifacts/**` or `docs/evidence/**`), and

    * emitting a **bundle manifest** (JSON/JSONL) that lists, for each member, at least: logical `artifact_key`, `sha256`, `size_bytes`, and any additional descriptors defined in PF12.

  * The bundle generator **MUST** run under the same determinism pins as other evidence tools (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, plus any rails pins from §1.2) and **MUST NOT** hand-edit existing governed artifacts. Its outputs (bundles and manifests) are consumed by `tools/evidence/update_evidence_index.py` as described above.

**Orientation demo and evidence skeleton coupling (normative).**

Mechanics treats the topology orientation demo as part of the same **evidence skeleton** as the Human Evidence Index and Machine Mirror. The following coupling rules apply:

* Any PR that runs `tools/evidence/update_evidence_index.py` in **write mode** to change governed evidence under `docs/evidence/**`, `artifacts/**`, or `audit/**` **MUST** also run `tools/evidence/orientation_demo.py` in **write mode** in the same PR and commit the updated `audit/gates/topology/orientation_demo.txt` and its `*.path_proof.txt` before invoking either tool’s `--check` mode.

* Index/Mirror changes without a matching, freshly generated orientation demo are **out of spec** and **MUST** be treated as drift: `tools/evidence/orientation_demo.py --check` is expected to fail with an orientation-drift error in such cases, and CI **MUST NOT** be forced green by skipping or bypassing the orientation demo.

* Evidence harnesses and scripts that wrap `tools/evidence/update_evidence_index.py` as a single job (for example, error evidence generators, sampler/core evidence generators, bundle generators, or combined evidence pipelines) **MUST** treat `tools/evidence/orientation_demo.py` as part of the **same single-writer chain** for the evidence skeleton: when they refresh governed artifacts and the Index/Mirror, they **MUST** also refresh the orientation demo in that same job and PR.

This clarification does not change which tools are allowed to write governed evidence; it makes explicit that `tools/evidence/update_evidence_index.py`, the bundle generator, and `tools/evidence/orientation_demo.py` together own the evidence skeleton for both per-artifact and bundle-level families, so that the topology orientation demo always reflects the current governed evidence skeleton and orientation-drift is caught and fixed in the same change that expands or shrinks the skeleton.

Mechanics **MUST NOT** hand-edit governed evidence artifacts (ordering artifacts, bundles, manifests, Index, mirror, path-proofs, topology orientation demo). Manual editing is reserved for canonical Doc-Delta work in PF documents; repository artifacts are **tool-generated only**.

### **1.3.2 Evidence change workflow**

**Scope (normative).**  
 Any PR that changes **governed artifacts** under `artifacts/**`, `docs/evidence/**`, or `audit/**` **MUST** follow the evidence change workflow. Governed artifacts include, at minimum, the ordering artifacts under `artifacts/engine/order/**`, the Evidence Index and Machine Mirror, topology orientation demo, sampler evidence families under `artifacts/sampler/**`, Engine Core evidence families under `artifacts/core/**`, their schemas under `docs/schemas/**`, and all `*.path_proof.txt` listed in this guide and in §37 Documentation Artifacts and Registry.

**Workflow (minimum sequence).**

For PRs that touch governed evidence:

1. **Ordering artifacts (when in scope).**

   * Run the ordering generator and its `--check` mode whenever ordering artifacts are in scope for the change.

   * Verify two-run identity for ordering artifacts under determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

2. **Sampler and Engine Core evidence (when in scope).**

   * When sampler evidence families (`artifacts/sampler/**`) and their schemas (`docs/schemas/sampler/**`) are in scope, run the sampler evidence generator under closed rails to refresh those artifacts and their schema files. Tools **MUST** call the sampler core in pure-compute mode and **MUST NOT** hand-edit sampler evidence or schemas.

   * When Engine Core evidence families are in scope, run `python tools/evidence/generate_engine_core_evidence.py` under closed rails to regenerate Engine Core evidence artifacts and their schemas (for example, purity, two-run identity, AB↔BA parity, and JSON-compare logs under `artifacts/core/**` with matching schemas under `docs/schemas/core/**`). Tools **MUST NOT** hand-edit Engine Core evidence artifacts or schemas.

   * After sampler and Engine Core evidence artifacts have been refreshed, `python tools/evidence/update_evidence_index.py --check` (see step 3 below) **MUST** be used to regenerate the Human Index, Machine Mirror, and path-proofs so that `produced_at_utc` in mirror records and path-proofs reflects the actual refresh time for both sampler and Engine Core evidence and is consistent across artifact payload, mirror record, and proof transcript.

3. **Evidence Index and mirror.**

   * Run `python tools/evidence/update_evidence_index.py --check` to regenerate:

     * `docs/evidence/INDEX.json` (Human Index, titles/paths only),

     * `docs/evidence/INDEX.sha256` (hash sentinel),

     * `artifacts/evidence_index.jsonl` (Machine Mirror), and

     * governed `*.path_proof.txt` from a single source of truth.

4. **Topology orientation demo.**

   * Run `python tools/evidence/orientation_demo.py --check` to validate that the on-disk orientation report (`audit/gates/topology/orientation_demo.txt`) is coherent with the current Index/Mirror state and not stale.

5. **Mirror schema and path-proofs.**

   * Run `ci/checks/check_mirror_schema.sh` to enforce:

     * the canonical mirror schema (field set, field order, canonical JSONL),

     * uniqueness of `(artifact_key, discovered_physical_path)`, and

     * correctness of `proof_anchor` and `.path_proof.txt` contents for all governed artifacts, including sampler and Engine Core families and their schemas.

6. **Evidence ledger.**

   * Record an evidence addendum in **Glow HD Engine — Build Notes & Integration Addenda (Living)** for the PR, describing new or changed governed artifacts and the evidence tools that produced them.

**Determinism & rails.**  
 The evidence change workflow **MUST** run under rails-closed, determinism-pinned CI environments (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), consistent with the rails posture described in §1.2 and the Evidence Index tokens in §1.3.

The release sanity pipeline harness (for example, `python tools/evidence/run_sanity_pipeline.py`) is treated as the scripted implementation of this workflow for sampler and Engine Core evidence under closed rails. It **MUST** call the sampler evidence generator and `tools/evidence/generate_engine_core_evidence.py` under the same determinism pins before refreshing the Evidence Index and Machine Mirror, so that the sanity pipeline log reflects the full suite of determinism and evidence checks for both sampler and Engine Core.

The determinism env-pins gate (`ci/checks/check_env_pins.sh`) **MUST** be wired to the same closed-rails suite set. It runs the expanded determinism and evidence checks (including sampler and Engine Core suites) and verifies that the env-pins log remains in sync with the on-disk evidence skeleton; the sanity pipeline log and env-pins log are treated as governed artifacts whose path-proofs and Machine Mirror records **MUST** track their canonical bytes over time.

This workflow makes the Evidence Index, Machine Mirror, ordering artifacts, sampler evidence, Engine Core evidence, and path-proofs move in **lockstep** and ensures that drift is caught early by CI, rather than after the fact.

**`mtime_utc` semantics (routing only).**  
 Evidence jobs that write or validate governed `*.path_proof.txt` **MUST** treat `mtime_utc` and `produced_at_utc` according to the canonical semantics defined in **HDE-Schemas & Artifacts** (Machine Evidence Mirror / path-proof schema) and **Glow QA Guide** (evidence CI rails and `mtime_utc` checks), summarised as:

* `mtime_utc` is the **refresh-time mtime** for the artifact: a UTC ISO-8601 timestamp truncated to seconds, with **microsecond \== 0**, captured when the evidence job refreshes that artifact. It is **not required** to remain equal to future `stat().st_mtime` values across clones, but CI checks MUST enforce that `parsed_mtime <= current_fs_mtime` at check time (monotone semantics).

* `produced_at_utc` is the **logical evidence refresh time** for the artifact (when the evidence job was run), also in UTC ISO-8601 form. For governed families such as sampler and Engine Core evidence, the artifact payload, mirror record, and path-proof transcript for a given artifact **MUST** agree on `produced_at_utc` for a given refresh; backdating or leaving mirror/proof `produced_at_utc` stale relative to the artifact’s refresh time is out of policy.

Mechanics does **not** redefine these semantics here; it routes to HDE-Schemas & Artifacts and the Glow QA Guide by title. The evidence change workflow in this section **assumes** that `tools/evidence/update_evidence_index.py`, `tools/evidence/generate_engine_core_evidence.py`, `ci/checks/check_mirror_schema.sh`, sampler and Engine Core evidence generators, the sanity pipeline harness, the env-pins check, and the evidence tests are wired to these `mtime_utc` and `produced_at_utc` rules and that any governed path-proofs they emit or validate satisfy the schema and monotone constraints pinned in those PF documents.

---

## 1.4 Routing (single homes; no duplication)

* **Public bytes:** PF-Canon-HDE-CLI-API-Vendor-Ref  
* **Math & preimage:** PF-Canon-HDE-Math-Spec  
* **Schemas, pack/manifest, canonical bytes, machine mirror:** PF-Canon-HDE-Schemas & Artifacts  
* **Governance (A7, ops posture, Evidence Index policy):** PF-Canon-HDE-Governance

## 1.5 Acceptance (tokens; titles-only)

* **Evidence & indices:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`  
* **Determinism:** `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`  
* **Rails posture:** `ENV_RAILS_POLICY_OK`  
* **Ops start-command:** `SERVICE_START_CMD_CAPTURED_OK`, `GUNICORN_APP_FACTORY_OK`, `ENV_PORT_REQUIRED_OK`

## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**

**Scope (normative).**  
 Mechanics requires a set of **QA tooling components** that support both CI and Live QA without relying on hand-edited commands or ad-hoc shells. This section defines the mechanical responsibilities for:

* a **QA tooling bootstrap harness** that verifies the basic test/tooling environment, and

* a **Live QA harness** that runs CLI/tests for QA, classifies failures as **tooling** vs **behavior**, and writes structured QA logs (including empties, exit codes, and stderr) under governed audit locations.

QA plans, acceptance tokens, and epic-specific QA steps remain single-homed in **Glow QA Guide**, **HDE-Build Checklist**, **HDE Phased Epics**, and **Glow Infrastructure** by title; this section records the components that must exist in the repo.

### **1.6.1 QA tooling bootstrap harness (PRE-step component)**

**Purpose (normative).**  
 Provide a single, scriptable **bootstrap step** that verifies the test tooling environment before any QA plan or Live QA flow runs tests or CLI commands against the Engine.

**Behavior (minimum).**

The QA tooling bootstrap harness **MUST**:

* **Activate the project environment.**

  * Activate the project’s Python environment (for example, via a venv or equivalent). Mechanics does not pin the exact activation command; it requires that the harness run under the same Python interpreter and environment that the Engine uses for tests and CLI tools.

* **Verify pytest availability via the Python interpreter.**

  * Run `python -m pytest --version` under the activated environment.

  * Treat any non-zero exit or import failure as a **tooling failure**, not a test failure. The harness **MUST NOT** proceed to project tests when this check fails.

* **Verify primary CLI/tool dependencies.**

  * Run `command -v hdctl` and `command -v jq` (or equivalent checks for the canonical CLI binary and JSON tool) and require **success** for each.

  * Treat missing CLI or missing `jq` as a **tooling failure**.

* **Write a QA tooling bootstrap log.**

  * Emit a structured log under an `audit/qa/**` prefix that records, at minimum:

    * the commands executed (`python -m pytest --version`, `command -v hdctl`, `command -v jq`),

    * their exit codes, and

    * a top-level classification field (for example, `tooling_failure: true/false` or an equivalent status enum).

  * When any bootstrap check fails, the log **MUST** mark the run as a **tooling failure** and identify which check failed; QA plans and tokens may then treat this as a **tooling/infra blocker**, not as an epic behavior failure.

Mechanics does **not** pin the exact file name or JSON schema for the bootstrap log; those live in **Glow QA Guide** and **HDE-Schemas & Artifacts** by title. This non-pinning applies only to the bootstrap log’s exact naming and schema, not to the existence of concrete QA run artifacts: the QA tooling bootstrap harness and Live QA harness ecosystem **MUST** still produce governed, non-empty evidence under `audit/qa/**` suitable for use by the QA plans, manifests, and viability checks routed by title to the QA and schemas documents.

**Preferred pytest invocation (Codespaces and similar dev environments).**

In environments like shared dev containers or Codespaces, Mechanics requires:

* Normative tests and QA flows **MUST** invoke pytest as `python -m pytest …`, using the same Python interpreter that runs the Engine.

* QA plans and CI jobs **SHOULD** standardize on `python -m pytest` for all test steps rather than calling `pytest` via a venv shim, to avoid “broken shim” failures where `.venv/bin/pytest` exists but is not executable.

* Any failure of `python -m pytest --version` in the bootstrap harness **MUST** be recorded and classified as a tooling failure in the bootstrap log; epic acceptance and behavior tokens **MUST NOT** be marked failed solely because pytest is missing or misconfigured.

### **1.6.2 Live QA harness (commands, classification, and logs)**

**Purpose (normative).**  
 Provide a reusable **Live QA harness** that runs CLI and other Engine-facing commands for QA (including PO-run Live QA sessions) in a way that is deterministic, copy/paste-ready, and distinguishable between tooling failures and behavior failures.

**Behavior (minimum).**

The Live QA harness **MUST**:

* **Depend on a successful bootstrap.**

  * Check the QA tooling bootstrap harness result before executing Engine tests or CLI commands.

  * If the most recent bootstrap log reports a tooling failure, the Live QA harness **MUST NOT** proceed to run tests or Engine commands and **MUST** surface that condition as a tooling problem (for example, via a `tooling_failure: true` or equivalent marker in its own logs).

* **Provide copy/paste-ready commands (no hand-editing).**

  * All PO-facing QA commands exposed by the harness **MUST** be fully concrete and copy/paste-ready (no `<PO: ...>` placeholders).

  * When commands require values that are present in tests or configs (for example, fixed VIEWER\_IDs, seeds, or candidate payloads), the harness **MUST** discover or construct those values programmatically by mirroring test semantics (for example, calling the same helpers that write candidate payloads) instead of asking the PO to hand-edit commands.

* **Reuse test semantics directly instead of scraping.**

  * When tests construct data dynamically (for example, writing candidates to a temporary file and passing that path into a CLI command), the Live QA harness **MUST** mirror the same construction logic directly (for example, by writing the same payload under an `audit/qa/**` path) rather than attempting to scrape arguments out of test source files.

  * For CLI QA flows, this means the harness should call the same underlying functions or fixtures that tests use to prepare inputs, so that QA inputs are deterministic and aligned with test coverage.

* **Capture exit codes, sizes, and stderr for QA artifacts.**

  * For each QA artifact that is expected to be non-empty (for example, JSON outputs, sorted candidate listings, or other CLI outputs under `audit/qa/**`), the harness **MUST**:

    * record the generating command and its exit code,

    * record the artifact’s size (for example, via `wc -c` or an equivalent size measurement), and

    * capture any stderr emitted by the command in a corresponding QA log entry.

  * If such an artifact is zero bytes, the harness **MUST** treat this as a **failure signal** (tooling or behavior) and record it explicitly; an empty artifact **MUST NOT** be left ambiguous.

* **Classify failures as tooling vs behavior.**

  * For each QA run, the Live QA harness **MUST** classify the outcome as either:

    * a **tooling failure** (for example, missing pytest, broken CLI entrypoint, environment not bootstrapped), or

    * a **behavior failure** (tests assertions failing, CLI returning incorrect JSON or exit codes).

  * This classification **MUST** be visible in the QA logs written under `audit/qa/**` (for example, through a `status` field or `tooling_failure: true/false`), so that Governance/QA documents and tokens can distinguish infra/tooling problems from Engine behavior problems.

Mechanics does **not** define the token names or acceptance rules associated with these logs; those remain single-homed in **Glow QA Guide**, **HDE-Build Checklist**, **HDE Phased Epics**, and **Glow Infrastructure** by title. This section requires that the QA bootstrap harness and Live QA harness exist as concrete components, that they enforce the behaviors listed above, and that their logs live under governed audit locations and are suitable for use by those documents.

**Routing (titles-only).**

* **QA plans, acceptance tokens, and epic-specific QA steps:** **Glow QA Guide**, **HDE-Build Checklist**, **HDE Phased Epics**.

* **Environment and Codespaces posture:** **Glow Infrastructure** and **GitHub Codespaces in a QA Workflow**.

* **Schemas and canonical JSON rules for QA logs (when governed):** **HDE-Schemas & Artifacts**.

Mechanics records the existence and behavior of the QA tooling bootstrap and Live QA harness here so that they are treated as first-class components of the HD Engine’s tooling skeleton, on par with the sanity pipeline, env-pins checks, and evidence tools.

### **1.6.3 Generic epic QA harness entrypoint (run directory, logs, manifest, viability)**

**Purpose (normative).**  
 Provide a single reusable **epic QA harness entrypoint** that can be invoked for any epic to execute a Live QA run under pinned rails and to reliably produce governed QA evidence under `audit/qa/**` without relying on hand-edited commands or ad-hoc shell state.

This component exists because “a harness that exits 0 but produces no run artifacts” is mechanically useless and must be prevented by construction.

**Behavior (minimum, normative).**  
 The epic QA harness entrypoint **MUST**:

* **Determine an epic id and run id.**

  * Accept an epic identifier and a run identifier via a documented interface (CLI args or environment override).

  * When a run id is not explicitly provided, derive a deterministic default (for example, a stable slug for “live-qa-1” or an equivalent policy owned by Glow QA Guide).

* **Create a run-scoped QA\_ROOT directory.**

  * Create a run directory under the governed audit root of the form:

    * `audit/qa/<epic-id>/<run-id>/`

  * Exact naming and lifecycle rules for `<epic-id>` and `<run-id>` are routed by title to Glow QA Guide and HDE-Schemas & Artifacts; Mechanics requires that a single run directory exists and is used consistently for that run.

* **Emit a per-run bootstrap log and step logs.**

  * Write a per-run bootstrap log (D0) inside the run directory.

  * Write the canonical sequence of per-step logs for the epic’s Live QA steps inside the same run directory.

  * Each step log **MUST** be non-empty, include a rails snapshot (at minimum SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, APP\_ENV), include the commands executed, capture exit codes, and end with an explicit step outcome classification (tooling vs behavior).

* **Maintain per-epic run manifest and viability outputs.**

  * Maintain a per-epic “step logs manifest” file under `audit/qa/<epic-id>/` that enumerates known runs and the paths to their run directories and primary step logs.

  * Maintain a per-epic “acceptance map viability” log under `audit/qa/<epic-id>/` that appends a summary line for each run, aligned to:

    * the epic’s acceptance map, and

    * the token to evidence matrix (titles-only; owned elsewhere).

  * Mechanics does not define the token names or viability semantics here; it requires that the harness update these per-epic artifacts so that QA reviewers can audit whether a run is viable and complete.

* **Fail closed on missing outputs.**

  * If the harness completes without creating the run directory, without producing non-empty step logs, or without updating the per-epic manifest and viability outputs, it **MUST** exit non-zero and record the reason as a tooling/harness failure.

* **Be reusable across epics.**

  * Epic-specific harness entrypoints may exist as thin wrappers for convenience, but they **MUST** delegate to the generic harness entrypoint and must not re-implement logging, QA\_ROOT layout, manifest updates, or viability updates in bespoke per-epic code.

**CI self-test (normative).**  
 The repo **MUST** include a CI test that executes the epic QA harness entrypoint under closed rails with a synthetic run id and asserts, at minimum:

* the run directory exists,

* the per-run bootstrap log exists and is non-empty,

* at least one step log exists and is non-empty,

* the per-epic step logs manifest is updated with an entry for the synthetic run id, and

* the per-epic acceptance map viability log contains a new summary line for the synthetic run id.

This self-test is required to prevent regressions where the harness exits successfully but produces no governed evidence.

**Routing (titles-only).**

* QA plan step sequences, deliverables, and token semantics: Glow QA Guide, HDE-Build Checklist, HDE Phased Epics.

* QA\_ROOT naming conventions and any governed schemas for QA artifacts: HDE-Schemas & Artifacts.

* Environment rails posture for CI and Codespaces: Glow Infrastructure.

  # 2\) Canonical Enumerations Registry

**Purpose.** Wire and prove the frozen domain registries (centers, gates, channels, categories) used by the engine. Mechanics validates and snapshots the domains; **HDE-Schemas and Artifacts** is the single home for authoritative catalogs and schemas. Developer notes in this repo are informative only (never authoritative).

---

## 2.1 Domain invariants (normative)

* **Centers:** closed set; `snake_case` identifiers; ASCII; unique.  
* **Gates:** closed domain; numeric identity per schema; unique; each attached to a single center by catalog.  
* **Channels:** closed set of edges; canonical `NN-NN` (zero-padded, min-first, ASCII hyphen); ASCII-sorted; unique; **no multi-hop encodings**.  
* **Categories (Magic-10):** closed ID set **with pinned order** (HDE-Schemas and Artifacts §2.6).  
* **Set semantics:** arrays that represent sets **MUST** be deduped and ASCII-sorted before hashing/compare (HDE-Schemas and Artifacts §4).  
* **Validation posture:** unknown IDs, duplicates, non-canonical channel forms, or schema mismatches **hard-fail** with typed errors.  
  ---

  ## 2.2 Validation & generation (mechanics)

Mechanics provides a single **registry job** that:

1. **Load & validate** each domain against its HDE-Schemas and Artifacts JSON-Schema (titles-only).  
2. **Normalize channels** to `NN-NN` min-first and enforce ASCII sort \+ dedupe for set-arrays.  
3. **Prove closure & uniqueness** (no extras/omissions, no duplicates, no cross-catalog drift).  
4. **Emit a registry snapshot** (records-only metadata: domain name, item counts, canonical `sha256/size` of each governed artifact) and **index it** in the machine mirror at `artifacts/evidence_index.jsonl`.  
5. **Update the human Evidence Index** (Appendix D) **in the same change**; CI enforces human↔machine **1:1 parity** and **path-proofs** (`discovered_physical_path` \+ `proof_anchor`).  
6. **Pins (determinism).** All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`; JSON is canonical (UTF-8 no BOM, sorted keys, compact, one LF).

**Seeds (catalogized; admin/test).** If Seeds are present in HDE-Schemas and Artifacts, they are admin/test-only and treated as **frozen inputs**; any change **bumps `release_id`** (HDE-Schemas and Artifacts §6; HDE-Math-Spec §5.1.1). Seeds are **not public** in Reader v1.

---

## 2.3 Artifacts (records-only; path-agnostic; indexed via the machine mirror)

List by **title/path** in Appendix D and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; one LF; canonical JSON).

* **`domain_snapshot`** — counts & identities (`sha256/size`) for centers/gates/channels/categories.  
* **`closure_report`** — proofs of domain closure & uniqueness; channel-normalization **reject corpus** (non-canonical inputs → errors).  
* **`registry_checksums`** — summarized checksums for governed artifacts (for quick diffing).  
  ---

  ## 2.4 Acceptance (tokens; titles-only)

* **Domains closed & frozen:** `CATALOG_DOMAIN_CLOSED_OK`, `M10_DEFS_OK`, `MAGIC10_NAMES_FROZEN_OK`.  
* **Orientation & normalization:** `CATALOG_ORIENTATION_CANON_OK` (channels `NN-NN` min-first; ASCII-sorted; deduped).  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Seeds (when present):** `M10_SEEDS_OK`, `RELEASE_ID_RECOMPUTE_OK` (manifest bump on change).  
  ---

# 3\) Programmatic Configuration System

**Purpose (normative).** Provide a **typed, deterministic configuration surface** for the engine and its clients. The system loads governed catalogs, **validates & normalizes** them, **fails on unknown/duplicate IDs**, and **emits typed artifacts** for FE/BE alongside a **registry report**. Concrete file names and directories are **implementation-defined** and **not pinned here**.

**Single homes (titles-only).**

* **Domains/schemas & canonical JSON rules:** PF-Canon-HDE-Schemas & Artifacts (§2, §4, §8).  
* **Math semantics (constants, ordering/banding):** PF-Canon-HDE-Math-Spec.  
* **Governance (evidence policy & tokens):** PF-Canon-HDE-Governance.

## 3.1 Loader behavior (normative)

* **Unknown/duplicate IDs → fail build.** The loader **MUST** hard-fail (typed error) on any unknown identifier, duplicate entry, schema mismatch, or non-canonical channel form.  
* **Alias policy \= OFF (default).** No implicit aliases. If an allow-list is explicitly enabled, only **declared aliases** are recognized; all others **fail**.  
* **Normalization.** Channel IDs normalize to **zero-padded `NN–NN` (min-first)**; arrays that represent sets are **deduped & ASCII-sorted** before hashing/compare.  
* **Determinism.** Output is **order-neutral (AB↔BA)**, **locale-neutral** (`LC_ALL=C`), and **two-run identical**; canonical JSON is **UTF-8 (no BOM), sorted keys, compact, exactly one LF** (PF-12 §4).

**Implementation note (informative).**

In the current Engine repo, the typed loader behavior described in this section is implemented by `engine.config.registry_loader.load_registry_config`. This reference is non-normative; the canonical rules remain those in PF-Canon-HDE-Schemas & Artifacts and this section.

## 3.2 Typed artifacts (codegen) — outputs, not paths

* **FE typed constants bundle.** A generated artifact that exposes **closed enums/domains** and **read-only constants** needed by the FE client (e.g., category IDs, band labels), typed and **immutable**.  
* **BE enums & constants bundle.** A generated artifact that exposes the same **frozen domains** to backend code (enums, discriminated unions), typed and **immutable**.  
   *(The exact filenames/locations are implementation-defined; Mechanics only requires that both bundles exist and are **consistent, typed, and deterministic**.)*

  ## 3.3 Registry report (records-only; machine-readable)

**Purpose (normative).** Emit a **registry report** that documents the **effective configuration** for this build: which catalogs and manifest were used, what domains and Magic-10 categories are present, and what alias policy is in effect. The report is **names-only** (no payload values) and is consumed by CI and auditors as a summary of the registry state.

**Single home & schema.**

* The registry report is a governed artifact at:

  * `artifacts/registry/registry_report.json` (titles-only; path/scheme details live in **HDE-Schemas and Artifacts §8.5**).

* The **canonical schema and field shapes** for `registry_report.v1` are defined in **HDE-Schemas and Artifacts**. Mechanics **must not** restate the full schema here. At a high level, the report:

  * declares a `schema` tag (for example `"registry_report.v1"`),

  * records `generated_at_utc`,

  * describes upstream `inputs` (catalogs and manifest), and

  * summarizes registry state under `artifacts.registry` (channels, gates/centers, domains and counts, Magic-10, alias\_policy),

  * with optional `notes` for internal commentary.

**Programmatic generation & determinism.**

* The registry report **MUST** be generated programmatically by the Programmatic Configuration System:

  * load and validate catalogs and manifest via the typed loader described in §3.1, and

  * construct the report object in memory and emit it via the **canonical serializer** (see §4 / §10.1).

* `generated_at_utc` **SHOULD** be stable across two runs in a determinism-pinned environment: tools **MUST** either **reuse the existing `generated_at_utc`** from a prior report when inputs have not changed, or use a **pinned time source** controlled by environment (for example, an epoch exposed via `SOURCE_DATE_EPOCH` or equivalent) so that two runs under the same conditions produce **byte-identical** JSON.

  * tools **MUST** either:

    * reuse the existing `generated_at_utc` from a prior report when inputs have not changed, or

    * use a pinned time source (for example, an epoch configured by environment) so that two runs under the same conditions produce identical bytes.

* Two-run identity **MUST** hold for the registry report:

  * running the generator twice with identical inputs and environment yields **byte-identical** JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

**Implementation note (informative).**

For the current Engine, the registry report generator is implemented by `tools/generate_registry_report.py`, which loads catalogs and manifest via the typed loader in §3.1 and emits `artifacts/registry/registry_report.json` through the canonical serializer. This reference is informative only; Mechanics remains implementation-agnostic and the governed rules are those in PF-Canon-HDE-Schemas & Artifacts and this section.

**Alias policy summary.**

* The report **MUST** expose a names-only alias policy summary under `artifacts.registry` (see HDE-Schemas and Artifacts for exact shape):

  * `mode` — `"off"` or `"allow_list"` (or equivalent closed set), and

  * `aliases` — a mapping from alias IDs to canonical channel IDs when the allow-list is enabled.

* This summary **reflects the loader’s alias behavior**:

  * aliases are **OFF by default**, and

  * when an allow-list is configured, only declared aliases are present; all others fail closed (see §3.1).

Mechanics does not carry alias ledger content or catalog values; it only enforces that the alias policy exposed in the report matches the loader behavior.

**Evidence & indexing (titles-only).**

* The registry report **MUST** be part of the **evidence skeleton**:

  * A human Evidence Index entry is present in `docs/evidence/INDEX.json` (titles/paths only), and

  * A Machine Mirror record is present in `artifacts/evidence_index.jsonl` with:

    * `artifact_key` (for example `"registry.registry_report"`),

    * `role:"snapshot"`,

    * `discovered_physical_path:"artifacts/registry/registry_report.json"`,

    * `sha256`, `size_bytes`, `produced_at_utc`, and

    * `proof_anchor` pointing to the corresponding path-proof transcript.

* Human Index, hash sentinel, mirror record, and path-proof for the report **MUST** be updated in the **same PR** as any change to the report; CI enforces human↔machine **1:1 parity**, canonical JSONL, and path-proof presence (tokens routed by title to **HDE-Governance** and **HDE-Schemas and Artifacts**).

**Routing (titles-only).**

* Catalog/manifest schemas and the token→evidence matrix: **HDE-Schemas and Artifacts**

* Loader error envelope \+ canonical JSON serialization rules: **HDE-Mechanics Guide**

* Evidence skeleton tokens and CI posture: **HDE-Governance**, **HDE-Build Checklist**, and **HDE-Phased Epics**.

## 3.4 Validation (binary)

1. **Schema & domain closure:** all catalogs validate; no unknown/duplicate IDs; channels canonicalized; categories match the **closed** Magic-10 set.  
2. **Alias policy:** `OFF` by default; if `ON`, only allow-listed aliases pass; all others fail.  
3. **Typed artifacts:** FE and BE bundles are **type-complete**, **immutable**, and **consistent** across runs (two-run identity).  
4. **Determinism:** re-running the loader yields identical bytes for codegen bundles and the registry report.  
5. **Evidence:** human Index and PF-12 mirror contain synchronized records with **path-proofs**; canonical JSON lints pass (UTF-8/no BOM, sorted keys, one LF).

## 3.5 Acceptance (tokens; titles-only)

* **Config loader/report:** `CONFIG_GEN_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`.  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.  
* **Domains closed/canonicalization (supporting):** `CATALOG_DOMAIN_CLOSED_OK`, `CATALOG_ORIENTATION_CANON_OK`, `M10_DEFS_OK`.

## 3.6 Routing (no duplication)

* Canonical rules & mirror schema: **PF-Canon-HDE-Schemas & Artifacts**.  
* Math semantics & constants: **PF-Canon-HDE-Math-Spec**.  
* Evidence policy & governance tokens: **PF-Canon-HDE-Governance**.

## **3.7 Config artifacts (Magic-10 and band edges)**

**Purpose (normative).**  
 The Programmatic Configuration System must emit **governed configuration artifacts** for the Magic-10 category configuration and band thresholds, alongside the registry report. These artifacts are the canonical, deterministic configuration views used by the engine math and by QA; schemas and artifact keys remain single-homed in HDE-Schemas & Artifacts, and token semantics remain in HDE-Governance and the Glow QA Guide.

### **3.7.1 Generator posture (closed rails, canonical JSON)**

The configuration generator responsible for producing governed config artifacts **MUST**:

* Run under closed rails and determinism pins before writing any governed config artifact:

  * SAFE\_MODE \= 1

  * ALLOW\_NETWORK \= 0

  * LC\_ALL \= C

  * LANG \= C

  * TZ \= UTC

* Use the typed loader behavior defined in §3.1 to read catalogs, manifest, and any thresholds inputs.

* Emit all config artifacts via the Canonical Serialization Package (see §4 and §10.1):

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact separators

  * exactly one trailing line feed

  * arrays that represent sets deduped and ASCII-sorted before emission

Two-run identity **MUST** hold for each governed config artifact: running the generator twice with identical inputs and environment yields byte-identical JSON.

Implementation note (informative).  
 In the current engine repository, this behavior is implemented by a closed-rails generator script in tools/config/generate\_config\_artifacts.py and helper functions in tools/config/artifacts.py. These names are informative only; the normative rules remain those in this section and in HDE-Schemas & Artifacts.

### **3.7.2 Magic-10 config artifact**

The configuration system **MUST** materialize a governed Magic-10 configuration artifact whose schema and artifact\_key are owned by HDE-Schemas & Artifacts (for example, magic10\_config.v1 and config.magic10). At a minimum, this artifact:

* Captures the **Magic-10 category order** exactly as used by the engine (closed set and pinned order).

* Records per-category configuration and bounds, including:

  * numeric caps for inputs and derived scores (integer bounds), and

  * any additional per-category configuration metadata required by the engine math.

* Records **seed metadata** for the Magic-10 configuration as a structured block, including at least:

  * template identifier (template\_id),

  * seed version (seed\_version),

  * updated\_at\_utc (UTC ISO time, semantics single-homed in HDE-Schemas & Artifacts and Glow QA Guide), and

  * checksum\_sha256 over the underlying config source or thresholds used to derive this artifact.

* Emits canonical, deterministic JSON governed by the rules in §3.7.1 and §4.

The Magic-10 config artifact is admin/test-only; the public Reader surface remains bands-only and numeric-free as described in the preamble and in HDE-CLI-API-Vendor-Ref.

### **3.7.3 Band-edges config artifact**

The configuration system **MUST** also materialize a governed band-edges configuration artifact whose schema and artifact\_key are owned by HDE-Schemas & Artifacts (for example, band\_edges.v1 and config.band\_edges). At a minimum, this artifact:

* Captures band labels and numeric edges for the engine’s banding policy (such as inclusive-high thresholds).

* Records, in a names-only form, the clamp and rounding behavior used by the engine (for example, clamp bounds and the rounding mode consistent with round\_half\_up in HDE-Math-Spec).

* Carries a version tag and a structured pointer back to the thresholds input used to derive it (for example, a reference to the thresholds pack or math thresholds source discussed in §7.3 and in HDE-Schemas & Artifacts).

* Emits canonical JSON governed by §3.7.1 and §4, under the same two-run identity requirements as the registry report.

Band-edges configuration is admin/test-visible only; band mechanics and public band behavior remain specified in HDE-Math-Spec and in the Category Framework (§7).

### **3.7.4 Evidence and acceptance map (routing only)**

Governed config artifacts participate in the same evidence skeleton as other artifacts described in §1.3 and §25:

* Each config artifact (registry report, Magic-10 config, band-edges config) **MUST** appear in the human Evidence Index with a title and discovered path, and have a corresponding record in the machine mirror with sha256, size\_bytes, produced\_at\_utc, role, and proof\_anchor.

* Each config artifact **MUST** have a co-located path-proof transcript referenced by proof\_anchor; governed evidence tools described in §1.3.1 are the only writers for these path-proofs and the mirror.

Mapping of PF09 tasks and QA tokens to config artifacts and tests lives in the config acceptance map and QA documents by title (HDE-Build Checklist, HDE-Schemas & Artifacts, Glow QA Guide, and HDE Phased Epics). PF14 records only that governed config artifacts exist, are generated under closed rails, are canonical and two-run identical, and are part of the evidence skeleton; it does not duplicate the acceptance map schema or token definitions.

## **3.8 Typed FE/BE config bundles (projections of governed config)**

**Purpose (normative).**  
 The Programmatic Configuration System must expose **typed configuration bundles** for backend and frontend consumers as **read-only projections** of the governed config artifacts and registry state described in §3.3 and §3.7. These bundles are canonical JSON snapshots used by internal code and adapters; schemas and artifact\_keys remain single-homed in HDE-Schemas & Artifacts, and token semantics remain in HDE-Governance and the Glow QA Guide.

### **3.8.1 Generator posture (closed rails, canonical JSON)**

The bundle generator responsible for producing FE/BE config bundles **MUST**:

* Run under closed rails and determinism pins before computing or writing any bundle:

  * SAFE\_MODE \= 1

  * ALLOW\_NETWORK \= 0

  * LC\_ALL \= C

  * LANG \= C

  * TZ \= UTC

* Load configuration exclusively through the typed loader described in §3.1 and the governed config artifacts described in §3.7 (registry report, Magic-10 config, band-edges config), without introducing new configuration sources.

* Emit both bundles using the Canonical Serialization Package (§4 / §10.1):

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact separators

  * exactly one trailing line feed

  * arrays that represent sets deduped and ASCII-sorted before emission

Two-run identity **MUST** hold for each bundle: generating FE and BE bundles twice with identical inputs and environment yields byte-identical JSON.

Implementation note (informative).  
 In the current engine repository, this behavior is implemented by a closed-rails bundle builder in engine/config/bundles.py and a CLI script in tools/config/generate\_bundles.py. These names are informative only; the normative rules remain those in this section and in HDE-Schemas & Artifacts.

### **3.8.2 Backend config bundle (internal scope)**

The backend bundle is a governed config snapshot whose artifact\_key and schema tag are owned by HDE-Schemas & Artifacts (for example, config\_bundle.be and config\_bundle.be.v1). At a minimum, this bundle:

* Includes the **full Magic-10 configuration** as derived from the Magic-10 config artifact:

  * closed category order,

  * per-category caps and other configuration parameters, and

  * the seed metadata block (template identifier, seed version, updated\_at\_utc, checksum) consistent with §3.7.2.

* Includes the **full band-edges payload** as derived from the band-edges config artifact:

  * band labels, edges, clamp behavior, rounding mode, version, and source pointer consistent with §3.7.3.

* Includes the **registry-backed domain view** needed by backend scoring and ordering logic, such as:

  * channels with ids, gates, centers, circuit\_primary/substream, primary\_domain, domains, and any flags required by the engine,

  * centers and domains as recorded in the registry report, and

  * alias\_policy in a names-only form consistent with §3.1 and §3.3.

* Carries a structured **sources** block that, for each upstream governed config artifact used (for example, registry\_report, Magic-10 config, band-edges config), records at least path, sha256, and size\_bytes values matching the current Evidence Index / Machine Mirror entries.

The backend bundle is internal/admin-visible only and serves as a typed configuration source for backend consumers; it does not define public Reader or CLI bytes.

### **3.8.3 Frontend config bundle (client-facing scope)**

The frontend bundle is a governed config snapshot whose artifact\_key and schema tag are owned by HDE-Schemas & Artifacts (for example, config\_bundle.fe and config\_bundle.fe.v1). At a minimum, this bundle:

* Provides a **slimmed view of Magic-10 configuration** suitable for clients:

  * Magic-10 category order and caps, and

  * any additional per-category configuration needed for UI behavior.

* Provides a **reduced band-edges view**:

  * band labels, edges, clamp behavior, rounding mode, and version, with a names-only reference back to the same thresholds source used for the backend bundle.

* Exposes **channel identifiers and related metadata** required by clients:

  * channel ids plus associated centers and domains, and

  * alias policy in the same names-only form as the backend bundle.

* Carries a **sources** block with the same structure and guarantees as the backend bundle, so clients can verify that FE config reflects the current governed config artifacts and registry state.

The frontend bundle is intended for FE/client consumption and must not introduce new semantics beyond what is already defined by the governed config artifacts and registry report. It remains an internal, governed artifact; public Reader and CLI contracts are still owned by HDE-CLI-API-Vendor-Ref.

### **3.8.4 Schemas and evidence (routing only)**

Typed bundle structures are validated in tests against JSON Schemas that live alongside the code, but those schemas are **not** PF-canonical until HDE-Schemas & Artifacts is updated to include them. For now:

* HDE-Schemas & Artifacts owns the canonical **artifact\_keys**, path conventions, and any future bundle schema catalogs; PF14 references bundles and their schemas by title only and does not restate the JSON schemas here.

* Each bundle **MUST**:

  * appear in the human Evidence Index with an artifact\_key and discovered\_physical\_path,

  * have a corresponding record in the machine mirror with sha256, size\_bytes, produced\_at\_utc, role, and proof\_anchor, and

  * have a co-located path-proof transcript referenced by proof\_anchor.

* Tests for typed bundles **MUST**:

  * prove canonical formatting and two-run identity,

  * validate bundle structures against the local JSON Schemas, and

  * assert that Magic-10, band-edges, channels, centers, domains, alias\_policy, and the sources block are consistent with the governed config artifacts and registry report described in §3.3 and §3.7.

PF14 does not introduce new acceptance tokens for bundles; token names and gating for config bundles remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

# 4\) Canonical Serialization Package

**One serializer and one emitter for all public bytes** (Reader, CLI, evidence artifacts).

## 4.1 Policy (normative)

* **Single presenter/emitter.** All public JSON bytes **MUST** be produced by one presenter/emitter entrypoint symbol. Reader and CLI **MUST** call this exact symbol (titles-only allow-list; no alternates). See §10.2 for the unified entrypoint and §10.1 for canonicalization; the preimage recipe is in §3.2.  
* **Canonical JSON.** UTF-8 (no BOM); ASCII-sorted keys; compact separators (`,` and `:` only); exactly one trailing LF (`\n`). Arrays that function as sets are **deduplicated and ASCII-sorted** by identity.  
* **Single source of bytes.** The same canonical serializer is used for Reader responses, CLI stdout on parity surfaces, and machine-generated evidence artifacts.  
* **Determinism.** **AB↔BA parity** and **two-run identity** **MUST** hold for identical inputs/environment. Run all canonicalization and byte-compares with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Tests use the same path.** Test code **MUST NOT** bypass the shared presenter/emitter.

## 4.2 Prohibited (hard fail)

* **No ad-hoc serialization on public paths.** No `json.dumps(`, no `jsonify(`, no templated/string-built JSON, no framework helpers that bypass the presenter, no pretty/indented output, **no test-only shims**.

## 4.3 Allow-list (code/CI owned)

* Maintain an explicit **allow-list of presenter/emitter symbols**. Only allow-listed symbols may serialize public bytes (allow-list owned in code/CI; not pinned here).

## 4.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **Symbol parity.** Reader & CLI resolve to the same emitter entrypoint → `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`.  
* **Canonical bytes.** Encoding, key order, compactness, single LF, arrays-as-sets proven by canonical re-serialization byte-compare → `JSON_CANONICAL_CHECK_OK`.  
* **Determinism.** `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`.  
* **Evidence discipline.** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

## 4.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)

List by **title/path** in **Appendix D: Evidence Index** and add **1:1** records in `artifacts/evidence_index.jsonl` (each with `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF). Examples:

* **`grep_guard/serializer`** — proves no ad-hoc serializers on public paths (CI regex results).  
* **`emitter_symbol/proof`** — import-graph/reflection proof that Reader and CLI call the same presenter symbol.  
* **`canonical_json/check`** — policy check (UTF-8/no BOM, sorted keys, compact, one LF).  
* **`canonical_json/compare`** — byte-compare of public bytes vs canonical re-serialization (expected empty diff).

## 4.6 Routing (titles-only)

Transport and HTTP behavior (headers, conditional delivery, caching) and CLI stream policy live in **HDE-CLI-API-Vendor Ref**; token roster in **HDE-Governance**.

---

# 5\) Deterministic Tie-Break & Total-Order Module \[Required-Now\]

**Purpose.** Provide reusable comparators and helpers that impose a total, deterministic order over strings, numeric tuples, and domain identities the Engine uses. These utilities are called wherever ordering is consumed (selection, aggregation, snapshotting, evidence), ensuring **AB↔BA** neutrality and **two-run** identity. All byte-sensitive checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

## 5.1 Comparator policy (normative)

* **Locale-free, bytewise order.** All string ordering is **ASCII byte order** (code-point ascending), case-sensitive, under `LC_ALL=C`. No locale collation; no Unicode normalization.  
* **Stable total order.** Comparators are **antisymmetric**, **transitive**, and **total** (every pair comparable). Equal inputs are **stable** (no reordering of equals).  
* **Arrays-as-sets discipline.** When an array is used as a set: **dedupe by identity**, then **ASCII-sort** with the appropriate comparator; never rely on map/set iteration order.  
* **No clocks/RNG.** Tie-breaks never consult time or randomness.

  ## 5.2 Domain comparators (exact)

* **IDs (general strings).** `cmp_id(a,b)` → ASCII bytewise comparison.  
* **Magic-10 categories.** `cmp_category(a,b)` → compare by **frozen Magic-10 rank** (titles-only to **HDE-Schemas and Artifacts §2.6** / **HDE-Math-Spec §5.1**); if still equal (should not occur), fall back to `cmp_id`.  
* **Centers (snake\_case).** `cmp_center(a,b)` → `cmp_id(a,b)` over center IDs.  
* **Channels (NN-NN).** `cmp_channel(a,b)` → compare first the **left NN** (two-digit ASCII), then the **right NN**. Inputs **must already be canonical** `NN-NN` (min-first, zero-padded, ASCII hyphen `-`).  
* **Numeric then id (tuples).** For `(value, id)` (for example, equal-score ties):  
  1. sort **numeric ascending** (integers `0..100`),  
  2. break ties with `cmp_id` (stability preserved).  
      *Descending variants* use an explicit **descending numeric comparator** (do not negate and re-sort), then the same `cmp_id` tie-break.

  ## 5.3 Helpers (reusable)

* **`dedupe_sort(set_like, cmp)`** → returns unique, ASCII-sorted array using `cmp`.  
* **`sort_pairs(pairs, key_cmp, val_cmp)`** → stable sort over `(key,val)` with `key_cmp` then `val_cmp`.  
* **`ensure_total_order(cmp, generator)`** → property-test harness asserting antisymmetry, transitivity, and totality for domain samples.  
* **`canonicalize_array(arr, cmp)`** → enforce set discipline (**dedupe \+ ASCII sort**) prior to canonical JSON emission.

  ## 5.4 Engine call-sites (must use)

* **Composite surfaces.** Ordering of `channels_defined`, `channels_em`, `centers_defined` **must** use `cmp_channel` / `cmp_center` before emission/evidence (see **Appendix E — Composite fingerprint**).  
* **Category iteration.** All multi-category passes **must** iterate in the **frozen Magic-10 order** (titles-only **HDE-Schemas and Artifacts §2.6**); never rely on hash iteration.  
* **Presenter paths.** Before canonical serialization, arrays-as-sets **must** pass through `dedupe_sort` with the appropriate comparator.

  ## 5.5 Determinism & neutrality

* **AB↔BA identity.** Using the same comparators on normalized `(A,B)` and `(B,A)` yields **identical** arrays/tuples.  
* **Two-run identity.** Re-running with the same inputs produces **byte-identical** sequences after canonicalization.  
* **Serializer coupling.** Canonical dumps use UTF-8 (no BOM), sorted keys, compact, exactly one LF (§4/§10.1), with arrays already **deduped & ASCII-sorted**.

  ## 5.6 Validation (binary & property tests)

1. **Property tests:** for each domain comparator, prove **antisymmetry**, **transitivity**, **totality** over generated samples.  
2. **Set discipline:** `dedupe_sort` removes duplicates and preserves canonical order (idempotent on already-canonical arrays).  
3. **Channel ordering:** given mixed `NN-NN` arrays, verify strictly increasing `(left,right)` pairs and **min-first** orientation; reject non-canonical tokens.  
4. **Category loop:** verify the iteration order equals the **frozen Magic-10** index sequence (titles-only **HDE-Schemas and Artifacts §2.6**).  
5. **ABBA / two-run:** byte-compare outputs for `(A,B)` vs `(B,A)` and across two identical runs (must match).  
6. **Serializer cross-check:** canonical re-serialization byte-compare (UTF-8, no BOM, one LF).

   ## 5.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (**records-only JSONL**; UTF-8 no BOM; sorted keys; compact; exactly one LF). Each mirror record includes:  
 `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update human Index and mirror **in the same PR**; CI enforces 1:1 parity and **path-proofs**.

* **`order/props_total_order`** — property-tests pass (antisymmetry/transitivity/totality).  
* **`order/channels_sorted`** — channel identity ordering proof.  
* **`order/categories_iter`** — Magic-10 loop order proof.  
* **`order/abba_identity`** — AB↔BA byte-equality using these comparators.  
* **`canonical/json_compare`** — canonical dump compare (arrays deduped & ASCII-sorted).

**Routing (titles-only).**

* Frozen Magic-10 order & IDs: **HDE-Schemas and Artifacts §2.6**, **HDE-Math-Spec §5.1**.  
* Canonical JSON rules & fingerprint shape: **HDE-Schemas and Artifacts §4**, **HDE-Math-Spec Appendix E**.  
* Governance tokens roster: **HDE-Governance §2.0 Acceptance Tokens**.

  ## **5.8 Dev sampler HTTP harness (internal/dev-only)**

**Purpose.**  
 Provide a dev/admin-only HTTP harness for the sampler core that mirrors the dev sampler CLI semantics while remaining a strictly internal surface. This harness is for local and dev/admin use; it is not part of the public API, is not listed in the Endpoint Catalog, and is not an A7 proof surface.

**Route and method.**

* Route: POST /internal/dev/sampler

* Method posture: POST only; non-conditional (no conditional headers are honored, and the route never returns 304).

* Transport posture: emitted via the same canonical serializer used elsewhere in this document (UTF-8, no BOM, ASCII-sorted keys, compact, exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted). Cache-control and error envelopes follow the writer/error posture defined elsewhere in this document (no-store, no ETag for errors).

**Environment gating (dev/admin only).**

The dev sampler HTTP harness is enabled only when APP\_ENV is explicitly one of:

* dev

* test

* local

Mechanics requires that:

* When APP\_ENV is any other value (including prod), or when APP\_ENV is missing or empty, POST /internal/dev/sampler returns a writer-style 403 forbidden response with the standard typed error envelope for refusal (numeric-free, canonical JSON), and does not call the sampler core.

* When APP\_ENV is allowed, the handler may proceed to parse the request body and invoke the sampler core as described below.

Detailed auth and env policy (including any additional guards applied to internal/dev routes) remain single-homed in HDE-Governance and Glow Infrastructure; this section records only that APP\_ENV gating is required and that prod/misconfigured environments must be refused.

**Dev Reader start helpers (APP\_ENV propagation).**

Infra-owned dev Reader start helpers (for example, scripts that launch `adapter.http_reader` in Codespaces or local dev) **MUST**:

* propagate `APP_ENV` from the calling environment **as-is**, including when it is explicitly set to `"dev"`, `"test"`, `"local"`, `"prod"`, an empty string, or left unset; and

* **MUST NOT** supply a default `APP_ENV` value (for example, forcing `APP_ENV=dev` when it is empty or unset).

The start helper **may** set SAFE rails (`SAFE_MODE`, `ALLOW_NETWORK`) and locale/time pins (`LC_ALL`, `LANG`, `TZ`) and **may** set `PORT`, but it **must not** override the caller’s choice of `APP_ENV`. APP\_ENV gating semantics for `/internal/dev/sampler` remain owned by this section and the adapter:

* when `APP_ENV ∈ {dev, test, local}`, the handler may proceed to validate the request body and invoke the sampler core;

* when `APP_ENV` is any other value (including `prod`, missing, or empty), the handler **must** return a 403 writer-style refusal and **must not** call the sampler core, as specified above.

Live QA harnesses (for example, dev sampler Live QA scripts) rely on this behavior to exercise and verify the full set of APP\_ENV modes (dev/test/local vs prod/empty/unset) required by Governance and QA rails (names and token semantics remain single-homed in Glow Infrastructure, Glow QA Guide, and HDE-Governance). This clarification ensures infra start helpers do not silently mask gating bugs by forcing `APP_ENV` to an allowed value.

**Request body (dev/admin only).**

The handler accepts a single JSON object body with these fields:

* viewer\_id — required non-empty string identifying the viewer in this dev/admin context.

* candidate\_ids — required non-empty array of non-empty string identifiers for the candidates to be ranked.

* seed — optional value used only as metadata for this dev harness; it does not alter eligibility or ordering.

Mechanics requires strict schema behavior:

* Missing or malformed viewer\_id, an empty candidate\_ids array, non-string candidate ids, or unknown extra top-level keys must be rejected with a 422 invalid\_input error using the standard error envelope and writer transport posture.

* No other fields are accepted on this route.

The intent is to drive the sampler core with IDs and fixed placeholder feature values for dev/admin inspection; this harness does not expose compat scores, bands, or any other internal numeric state.

**Behavior and payload.**

When APP\_ENV is allowed and the request body is valid, the handler:

* Builds in-memory sampler inputs (for example, a viewer profile and candidate feature records) from viewer\_id and candidate\_ids, using fixed safe placeholders for any features not specified by PF-Canon.

* Invokes the existing sampler core (for example, sample\_and\_rank) without changing its eligibility or ordering rules.

* Constructs a response payload with exactly these top-level keys:

  * viewer\_id — echo of the viewer\_id from the request.

  * meta — an object that, at minimum, includes:

    * seed — the provided seed value rendered as a string if present, or null if no seed was supplied.

  * candidate\_ids — an array of candidate ids in the ranked order returned by the sampler core.

Mechanics requires that:

* For a fixed viewer\_id, candidate\_ids set, and seed, repeated calls under the same environment produce byte-identical response bodies (two-run identity).

* For a fixed viewer\_id and candidate\_ids but different seeds, candidate\_ids remain identical; only meta.seed differs between responses.

* The response body is canonical JSON (UTF-8, ASCII-sorted keys, compact, one LF; arrays-as-sets deduped and ASCII-sorted).

**Dev harness start commands, base URLs, and responsibilities (dev/admin-only).**

For `/internal/dev/sampler` and any other internal/dev HTTP harness that is intended for QA or evidence flows and is not part of the public API, Mechanics requires a clear split of responsibilities between infra/ops and QA/PO, and concrete wiring for start commands and URLs.

**Infra-owned dev start commands (per environment).**

* For each environment where `/internal/dev/sampler` is intended to be used (at minimum: local dev and Codespaces), infra/ops **MUST** define and maintain a canonical dev Reader start command or service definition that:

  * starts the Reader process with APP\_ENV set to an allowed value for this harness (dev/test/local per §5.8), and

  * binds to a deterministic host and port for that environment (for example, `127.0.0.1:<port>` or the platform-assigned `$PORT`), consistent with the runtime posture in §32.

* This start command or service definition **MUST** be treated as infra-owned configuration:

  * PO and QA agents **MUST NOT** guess the dev harness start command, choose a port on their own, or “invent” a Reader process wiring for QA.

  * Changes to the start command, binding host, or port are infra changes and must be reflected in the same places that document other runtime wiring (Infrastructure docs by title).

The example runner shown elsewhere in this guide (for example, a local `python -m adapter.http_reader --bind 127.0.0.1:5000` command) is illustrative only; the normative requirement is that there is at least one **infra-owned** dev start command for each environment where this harness is intended to run.

**Base URLs and DEV\_SAMPLER\_URL (env wiring).**

* Infra/ops **MUST** derive and publish, for each such environment, a concrete base URL for the dev Reader process (for example, `http://127.0.0.1:<port>` in local dev or the appropriate forwarded port in Codespaces), and from that base URL define a concrete sampler harness URL:

  * `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler`

* `DEV_SAMPLER_URL` **MUST** be treated as an infra-owned configuration value:

  * QA plans and doc agents **MUST** consume `DEV_SAMPLER_URL` (or an equivalent infra-exposed value) as an input and **MUST NOT** guess hostnames, ports, or full URLs for `/internal/dev/sampler`.

  * Any change to the underlying dev Reader binding (host/port) **MUST** be reflected by infra in the published `DEV_SAMPLER_URL` value; QA and docs do not hard-code ports or recompute URLs independently.

Mechanics does not pin where `DEV_SAMPLER_URL` is stored (for example, env var, config file, or Codespaces devcontainer config), only that it exists as a single infra-owned binding for `/internal/dev/sampler` per environment and that QA/PO treat it as the authority for that harness URL.

**Infra validation of dev harness URLs (pre-QA).**

Before handing any `DEV_SAMPLER_URL` to QA or using it in QA plans, infra/ops **MUST** validate the dev sampler HTTP harness locally:

* Run the infra-owned dev Reader start command with APP\_ENV=dev (and, where feasible, the determinism pins used elsewhere in this guide: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`).

* Issue at least one simple HTTP/1.1 POST to `DEV_SAMPLER_URL` with:

  * `Content-Type: application/json; charset=utf-8`, and

  * a minimal, schema-valid request body consistent with §5.8 (for example, a non-empty `viewer_id` and a non-empty array of string `candidate_ids`, with or without `seed`).

* Confirm that the response:

  * uses canonical JSON output and the canonical serializer posture defined elsewhere in this guide (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted),

  * matches the request/response shape for `/internal/dev/sampler` described in §5.8 (top-level keys, types, and determinism requirements), and

  * carries headers consistent with internal/dev writer posture (for this dev harness: JSON `Content-Type`, `Cache-Control: no-store` for errors, no ETag).

If this validation fails, infra **MUST** treat the issue as an infra/tooling misconfiguration, not as an Engine/sampler behavior failure, and correct the wiring before any QA plan or doc step refers to `DEV_SAMPLER_URL`.

**Responsibility split (normative).**

* **Infra/ops agents** are responsible for:

  * defining and maintaining the dev Reader start commands for internal/dev harnesses (including `/internal/dev/sampler`) per environment,

  * choosing and wiring the base URL and port for the dev Reader process,

  * defining and updating `DEV_SAMPLER_URL` (and any similar dev harness URLs) to reflect actual Reader wiring, and

  * validating those URLs via local HTTP/1.1 JSON POSTs under the appropriate rails before they are handed to QA or docs.

* **PO and QA agents** are responsible for:

  * consuming `DEV_SAMPLER_URL` (and similar infra-defined URLs) as inputs in QA plans, scripts, and documentation steps, and

  * treating failures to reach or use `DEV_SAMPLER_URL` as **tooling/infra issues** to be escalated, not as sampler/core bugs, unless the infra validation above has already passed and QA has concrete behavior evidence.

Mechanics records these responsibilities so the dev sampler HTTP harness and any similar internal/dev harnesses are fully accounted for in the mechanical schematic: the harness route and behavior in §5.8, the dev Reader process and ports via infra-owned start commands, and the dev URLs (`DEV_SAMPLER_URL` and equivalents) wired and validated before QA exercises them.

**A7 and Endpoint Catalog posture.**

* POST /internal/dev/sampler is an internal/dev surface and is explicitly **not** a JSON success route in the Endpoint Catalog.

* No A7 proofs are run against this route, and it must not be referenced in the Catalog or any A7 composite proofs.

* Any headers-only captures for this route are local/dev diagnostics only and do not contribute to A7 acceptance tokens.

The CLI dev sampler remains the primary sampler harness; this HTTP dev harness is a convenience wrapper around the same sampler core for dev/admin workflows, subject to the same canonical JSON and determinism constraints.

---

# 6\) Deterministic Engine Core \[Required-Now\]

**Contract.** The Engine Core is **pure compute** (ops, scoring, aggregation). It performs **no I/O**, uses **no clocks**, reads **no globals/env**, and does **not** depend on system locale. All behavior is driven by **explicit inputs** and **frozen pack/preset constants** (titles-only to **PF-Canon-HDE-Schemas & Artifacts** / **PF-Canon-HDE-Math-Spec**).

## 6.1 Inputs & state (explicit only)

* **Explicit parameters.** All data (composite, feature flags, constants, viewer\_prefs) is passed **by value** or via a **typed config object**.  
* **No hidden sources.** Do **not** read files, environment variables, or the clock; do **not** mutate module globals or singletons.  
* **Preconditions satisfied upstream.** Alias normalization, tz resolution, and ingestion occur **before** the core (titles-only to PF-Canon-HDE-Schemas & Artifacts §2.1 / PF-Canon-HDE-CLI-API-Vendor-Ref §3.2).

  ## 6.2 Determinism pins

* **AB↔BA neutral.** Core results are **identical** when inputs `A,B` are swapped (AB \== BA after normalization).  
* **Two-run identity.** Two evaluations over the same inputs \+ constants produce **byte-identical** results.  
* **Stable iteration.** Do **not** rely on unspecified map/set iteration order: reduce over **ASCII-sorted keys**; arrays-as-sets are **deduped & ASCII-sorted**.  
* **Locale & serializer.** All canonicalization/compares run under **`LC_ALL=C`**. Any JSON the core emits for evidence uses the **canonical serializer** (UTF-8 no BOM, sorted keys, compact, **exactly one LF**).  
* **Numeric rules (titles-only).** Follow **PF-Canon-HDE-Math-Spec** for integerization and rounding (**round\_half\_up**); avoid floating-point accumulation for public-path numerics—use integer/fixed-point paths defined in **PF-01**.

  ## 6.3 Concurrency & parallelism

* **Allowed if deterministic.** Parallel evaluation is permitted **only** when reductions/merges are **order-invariant** (commutative/associative) and the final ordering is **stabilized (ASCII sort)** before exposure.  
* **No race-driven clocks/RNG.** Do **not** consult time or RNG; if samplers/rankers require stochastic behavior, they **must be seeded and isolated** (see local policy section on stochastic samplers).

  ## 6.4 Errors & logging (internal only)

* **Typed errors.** Fail fast with **typed, numeric-free** errors; do **not** include vendor payloads.  
* **No payload/secret logging.** Keys-only diagnostics; redact secrets; never echo request/response bodies.

  ## 6.5 Acceptance (binary)

1. **Two-run identity:** run core twice on the same inputs → **byte-equal** outputs.  
2. **ABBA:** swap `A,B` → outputs (and any core-level artifacts) **byte-equal**.  
3. **Stable order:** arrays-as-sets are **deduped & ASCII-sorted**; reductions use **sorted keys**.  
4. **Serializer check** (if core emits JSON artifacts): canonical re-serialization byte-compare (UTF-8, no BOM, **one LF**).  
5. **No I/O/clocks/globals:** static/grep-guard \+ import-graph proof show **no file/env/time** access in core modules.

   ## 6.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)

* **artifact\_key:** `engine/tworun_identity` — two-run proof.  
* **artifact\_key:** `engine/abba_identity` — ABBA compare.  
* **artifact\_key:** `canonical_json/compare` — canonical re-serialization proof (if core emits JSON artifacts).  
* **artifact\_key:** `guards/no_io_no_clock` — static/grep proof of **no I/O/clocks/globals**.  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`. The **human Evidence Index** (Appendix D) is updated **in the same change**; CI enforces **human↔machine 1:1 parity** and **path-proofs**.

**Routing (titles-only).**

* Numeric rules & public rounding/banding: **PF-Canon-HDE-Math-Spec**.  
* Canonical JSON & pack/manifest: **PF-Canon-HDE-Schemas & Artifacts**.  
* Governance tokens: **PF-04 — §2.0 Acceptance Tokens**.

## 6.7 Canonical Engine Core module and tests

**Scope (normative).**  
 The Dissolution engine work for tasks `HDE-DISS004.1–.3` realizes the Deterministic Engine Core described in this section as a **pure-compute module** under the `engine.core` package. Mechanics records the canonical implementation and test harness here so that future changes stay aligned with §6.1–§6.6.

**Canonical module and entrypoint.**

* The Engine Core module lives at `engine/core/core.py` and exports frozen dataclasses and helpers that implement the pure-compute contract in §6:

  * `ParticipantState` — frozen dataclass capturing the normalized state per party (for example, person identifier, compat score, band, and an immutable traits tuple).

  * `CoreConfig` — frozen dataclass carrying Engine Core configuration, including `band_priority`, which defaults to the canonical band ordering (for example, the `BANDS` tuple from compat thresholds).

  * `PerspectiveBreakdown` — frozen dataclass capturing perspective-specific metrics for one party (for example, party-local score, delta, and any supporting breakdowns).

  * `CoreResult` — frozen dataclass aggregating neutral metrics, ordered identifiers and bands, perspective breakdowns for both parties, and any shared-traits summary.

* The canonical Engine Core entrypoint is `engine.core.core.compute_core`. Mechanics and tests **MUST** treat this symbol as the single home for Engine Core behavior when evaluating the determinism and neutrality requirements in §6.2 and the acceptance checks in §6.5.

**Neutral metrics, ordering, and shared traits.**

* Neutral metrics are computed as **symmetric functions** of the two parties. In particular, the neutral compat score is an integer average of the two compat scores, and shared traits are derived via set intersection (using the existing canonical set helper and ID comparator) so that the shared traits tuple is identical for normalized AB and BA inputs.

* Identifier and band ordering use the deterministic ordering utilities from the Engine’s comparators and thresholds:

  * Party identifiers are canonicalized via `compare_ids`. When both identifiers are equal, the pair is mapped to the `ABBA_CANONICAL_PAIR` constant so that self-pairs have a fixed canonical representation.

  * Band pairs are ordered via a `_band_rank` function derived from `CoreConfig.band_priority` and then by band name, ensuring that for a fixed configuration, `ordered_bands` is identical for `compute_core(A,B, config)` and `compute_core(B,A, config)` and deterministic across runs.

These behaviors are **normative** for Engine Core; any future Engine Core changes **MUST** preserve AB↔BA neutrality and two-run identity as defined in §6.2.

**Dedicated Engine Core test suite (closed rails).**

* Purity tests live under `tests/core/test_engine_core_purity.py` and **MUST**:

  * import and reload `engine.core.core` under `ensure_determinism_env(apply=True)` to enforce determinism pins and closed rails,

  * use AST-based checks to reject imports whose root module is in `{os, time, datetime, random, socket, subprocess}`, and

  * scan the module source text for forbidden snippets such as `"os.environ"`, `"time."`, `"datetime."`, `"random."`, and `"socket."`.

* Together, these guards prove that the Engine Core performs **no file, network, clock, RNG, or env access** and does not introduce import-time side effects, satisfying the “no I/O/clocks/globals” requirement in §6.1 and §6.5.

* AB↔BA behavior tests live under `tests/core/test_engine_core_abba.py` and **MUST**:

  * construct asymmetric A/B inputs (different compat scores and bands) using `ParticipantState` and `CoreConfig`,

  * assert that neutral fields in `CoreResult` (for example, neutral score, `ordered_pair`, `ordered_bands`, and shared traits) are **identical** for `compute_core(A,B, config)` and `compute_core(B,A, config)`, and

  * assert that perspective-specific metrics in the `PerspectiveBreakdown` structures cross-swap as expected (for example, deltas for BA are the negation of the AB deltas) while remaining internally consistent.

* These tests are the canonical proof of AB↔BA neutrality for Engine Core and directly exercise the requirements in §6.2 and §6.5.

* Determinism and JSON-compatibility tests live under `tests/core/test_engine_core_determinism.py` and **MUST**:

  * call `compute_core` twice with identical inputs and `CoreConfig` under `ensure_determinism_env(apply=True)` and assert that the two `CoreResult` instances are equal,

  * serialize each result via `json.dumps(dataclasses.asdict(result), sort_keys=True)` and assert that the resulting JSON strings are **byte-identical**, and

  * verify that when `CoreConfig.band_priority` is customized, `ordered_bands` and `ordered_pair` remain deterministic and consistent with the configured band priority.

* These tests serve as the Engine Core’s two-run identity and JSON-compatibility proof under the determinism posture in §6.2 and §6.3. They demonstrate that `CoreResult` is safe for use with the canonical serializer and evidence tooling described elsewhere in this guide, even though the Engine Core evidence artifacts themselves are wired in a later epic.

**Evidence wiring (future epic).**

This subsection records the Engine Core’s pure-compute module and test harness only. The evidence artifacts and Machine Mirror records listed in §6.6 remain the long-term target for Engine Core evidence, but their wiring is explicitly assigned to a later epic (`HDE-DISS004.4`) and is **not** part of the mechanics recorded for the behavior-only work on `HDE-DISS004.1–.3`.

---

# 7\) Category Framework (internal) \[Required-Now\]

## 7.1 Closed list & scaffolds for per-category calculators

**Purpose.** Wire per-category **subtotal → band** calculators with precedence hooks; do **not** restate Math or public payload schemas.

**Frozen category set & order (titles-only).** All category logic addresses the ten **Magic-10** identifiers in their fixed canonical order. Iteration order is **normative** and **MUST** be enforced via the total-order utilities (ASCII / `cmp_category`; see §5 and **HDE-Schemas & Artifacts §2.6**, **HDE-Math-Spec §5.1**).

**Per-channel semantics (normative).** Calculators consume **channel-scoped** primitives: every “channel” reference is the canonical **NN-NN** edge (min-first, zero-padded), not a free-form string or unordered gate pair. Junction gates `{10,20,34,57}` may appear in multiple channels; treat each channel **independently**. Arrays of channels used as sets **MUST** be **deduped & ASCII-sorted** by canonical identity (see §5 comparators and canonicalization rules in §4; titles-only to **HDE-Schemas & Artifacts §2.1**).

**Public vs internal.** Category **subtotals** and **narrative keys** are internal/admin artifacts. The **public Reader** surface stays **bands-only, numeric-free** and is specified in **HDE-CLI-API-Vendor-Ref** (titles-only). Mechanics wires the allow-listed **presenter/emitter** (§4) and does **not** duplicate public JSON schema.

---

## 7.2 Compatibility Engine (pair) — contract

**Inputs (typed; titles-only).**

* `a, b` — each is either an **ID** or a **full person payload** (**HDE-CLI-API-Vendor-Ref** Reader schema). Do **not** mix ID and payload for the same party; mixed forms ⇒ typed `invalid_input` (**HDE-CLI-API-Vendor-Ref** error catalog, titles-only).

* `viewer_prefs` — `top_category ∈ Magic-10` and `weights` for **all ten** categories as integers `0..100` (key set **must equal** Magic-10). **Zero-weight rule:** if a viewer assigns `0` to a category, candidates whose \#1 equals that category are excluded. *(Titles-only: **HDE-Math-Spec §5.1**; **HDE-Schemas & Artifacts §2.6**; **HDE-CLI-API-Vendor-Ref**.)*

**Execution (internal math; titles-only).**

* **Subtotaling.** Compute per-category integer subtotals (`0..100`) via the Feature Framework and **pack-frozen constants** (**HDE-Math-Spec §5.4.2**; see channel semantics in §7.1; core is **I/O-free** per §6).

* **Banding.** Map each subtotal to a band using **inclusive-high** thresholds `(24/49/74/100)` with `round_half_up` (**HDE-Math-Spec §5.3**).

* **Narrative keys.** Select `{personal_key, shared_key}` per category from governed ledgers; if absent, flag `missing_narrative_key` (**no implicit fallback**).

**Outputs (admin/test surface only; titles-only).**  
 `categories[10]` in canonical Magic-10 order, each `{ id, score:int, band, personal_key, shared_key }`; plus `meta{ engine_tag, release_id }`.  
 **Public Reader** continues to emit **bands-only**. Contract bytes & schema are owned by **HDE-CLI-API-Vendor-Ref** and must be produced by the allow-listed **presenter/emitter** (§4). **Do not** embed JSON samples in this guide.

**Determinism & acceptance (binary).**

* **AB↔BA parity & two-run identity.** With identical inputs, **subtotals, bands, and any admin snapshots** are identical across `(A,B)` vs `(B,A)` and across runs; any emitted admin JSON is **canonical** (UTF-8/no-BOM, sorted keys, compact, one LF; arrays **deduped & ASCII-sorted**; `LC_ALL=C`).

* **Order.** Category arrays appear in the **frozen Magic-10 order**; tests assert this via §5 comparators.

* **Typed errors.** Mixed input forms ⇒ `invalid_input`; unknown IDs or malformed `viewer_prefs` ⇒ `invalid_input` (**HDE-CLI-API-Vendor-Ref** error catalog, titles-only).

**Tokens (titles-only).** `CATEGORY_FRAMEWORK_OK`, `M10_DEFS_OK`, `M10_MAPS_OK`, `M10_SYMMETRY_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.

**Evidence (records-only; path-agnostic).** ABBA fingerprint consumption (**HDE-Math-Spec Appendix E**), two-run logs, canonical-compare logs; **register mirror entries** and **update the human Evidence Index** in the same change (**HDE-Governance Appendix D: Evidence Index**; **HDE-Schemas & Artifacts** mirror).

---

## **7.3 Band thresholds and tuning (admin)**

**Registry only (titles-only).**  
 Mechanics maintains the authoring workflow for number-to-band thresholds (global or per-category) and the associated tooling; it does not restate numeric values. Band thresholds are internal/admin configuration only; the public Reader surface remains bands-only and numeric-free.

**Normative sources.**  
 Inclusive-high policy and global edges (for example, 24, 49, 74, 100\) are specified in HDE-Math-Spec. Per-category overrides and the constants pack live in HDE-Schemas & Artifacts (constants and manifest rules); Mechanics routes to those documents by title and does not duplicate numeric tables here.

**Config artifacts (governed snapshots).**  
 Band thresholds are materialized by the Programmatic Configuration System as a governed band-edges config artifact (see §3.7):

* The band-edges config artifact captures band names, numeric edges, clamp behavior, rounding mode, and a version tag, and includes a structured pointer back to the thresholds source used to derive it.

* The artifact is generated under closed rails with canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing line feed) and must satisfy two-run identity in determinism-pinned environments, consistent with §3.7 and §4.

* Schema, artifact\_key, and any additional metadata fields for the band-edges config artifact remain single-homed in HDE-Schemas & Artifacts; Mechanics only requires that such an artifact exist, be deterministic, and be wired into the evidence skeleton.

The same configuration system may also produce a governed Magic-10 config artifact (see §3.7) that defines per-category caps and seed metadata; band tuning and band-edges behavior must remain consistent with the Magic-10 configuration and the math rules in HDE-Math-Spec.

**Visibility and evidence.**  
 Thresholds and scores are admin/test-visible only. Mechanics provides helpers to dump and apply band-threshold sets and to capture identity and stability proofs, such as canonical snapshots and sha256 digests over compat bytes that include the final line feed. All tuning artifacts, including the band-edges config artifact and any supporting snapshots, must:

* be listed in the human Evidence Index with titles and paths,

* have corresponding machine-mirror records in artifacts/evidence\_index.jsonl with canonical JSONL records and path-proof anchors, and

* be updated together with their mirror records in the same PR, under the evidence discipline defined in §1.3 and §37.

Mechanics does not define additional acceptance tokens for band tuning; token names and their semantics remain single-homed in HDE-Governance, HDE-Build Checklist, and HDE Phased Epics.

---

# 8\) Public Presenter & Emitter \[Required-Now\]

Transforms engine outputs into the Reader/CLI public envelope and emits canonical JSON via the allow-listed presenter–emitter.

---

## 8.1 Role

* Single public presenter/emitter for Reader and CLI.

* Responsible for:

  * Building the public body from engine outputs.

  * Applying canonical serialization rules.

  * Injecting idempotence metadata (`idempotence_hash`, `release_id`, `meta.invocation_tag`).

  * Feeding evidence artifacts for parity and determinism.

---

## 8.2 Policy — Emitter & serializer

* **Single emitter.**  
   Reader and CLI **MUST** call the same presenter–emitter entrypoint symbol to build the public body.

  * CI maintains a symbol allow-list; no alternate emitters are allowed.

* **Canonical serializer.**  
   The presenter **MUST** use the Canonical Serialization Package (§4):

  * UTF-8 (no BOM).

  * ASCII-sorted keys.

  * Compact JSON (no pretty/indented output).

  * Exactly one trailing LF.

  * Arrays-as-sets deduped and ASCII-sorted.

  * All byte checks under `LC_ALL=C`.

* **Public shape (titles-only).**  
   The public payload shape is owned by:

  * **HDE-CLI-API-Vendor-Ref** (public contract, headers, success/error envelopes).

  * **HDE-Math-Spec** (Reader v1 preimage fields, bands, rounding).

* Mechanics does **not** duplicate those bytes here.

---

## 8.3 Idempotence & identity

* **Preimage (five keys).**  
   Compute `idempotence_hash` over the canonical preimage: an object with exactly:

  * `reader_version`

  * `eligible`

  * `categories`

  * `meta`

  * `release_id`

* (No `idempotence_hash` field yet. Preimage fields are defined in **HDE-Math-Spec**.)

* **Finalize.**  
   Insert `idempotence_hash` (lowercase 64-hex) into the object and re-emit canonically to produce the public bytes (LF-terminated).

* **Identity coupling.**

  * `release_id` is taken from the freeze-pack manifest (**HDE-Schemas and Artifacts** §6).

  * `meta.invocation_tag` participates in the preimage (**HDE-Math-Spec**).

---

## 8.4 Parity requirements

* **Reader↔CLI parity.**  
   On parity surfaces, CLI stdout **MUST** be byte-identical to the Reader 200 body.

* **AB↔BA parity.**  
   For pair-sensitive flows (e.g., compat), AB and BA **MUST** produce identical bytes.

* **Two-run identity.**  
   With identical inputs and environment, two serializations **MUST** produce bitwise-identical public bytes.

---

## 8.5 Prohibited practices

On governed public paths, the following are **not allowed**:

* Ad-hoc serialization (`json.dumps(...)`, templating helpers, framework-specific `jsonify`\-style calls).

* String-built JSON or partial concatenation.

* Pretty/indented output or multi-LF endings.

Only the allow-listed presenter/emitter may serialize public bytes.

---

## 8.6 Acceptance (tokens; titles-only)

Token semantics live in **HDE-Governance** (§2.0). Mechanics binds them to this component as follows:

* **Symbol parity (shared emitter):**

  * `CLI_READER_EMITTER_PARITY_OK`

  * `CLI_NO_ALT_JSON_OK`

* **Parity proofs (byte equality & determinism):**

  * `TWO_RUN_IDENTITY_OK`

  * `COMPOSITE_ABBA_IDENTITY_OK`

* **Canonical compare (canonical JSON invariants):**

  * `JSON_CANONICAL_CHECK_OK`

* **Evidence discipline (Index/mirror/path-proofs; same PR):**

  * `EVIDENCE_INDEX_UPDATED_OK`

  * `EVIDENCE_INDEX_MIRROR_OK`

  * `EVIDENCE_PATHS_VALIDATED_OK`

---

## 8.7 Evidence (records-only; path-agnostic; indexed via PF-12 Machine Mirror)

Evidence artifacts are indexed and mirrored according to **HDE-Schemas and Artifacts** (§8.3 / §8.6). Typical `artifact_key` families for this component:

* `parity/reader_cli` — Reader↔CLI byte-equality (public surface).

* `parity/abba_identity` — AB↔BA byte-equality.

* `parity/two_run_identity` — Two-run identity digest/log.

* `emitter_symbol/proof` — Import-graph/reflection proof of shared presenter symbol.

* `canonical_json/compare` — Canonical re-serialization byte-compare of the public body.

Each mirror record **MUST** include:

* `artifact_key`

* `sha256`

* `size_bytes`

* `produced_at_utc`

* `discovered_physical_path`

* `proof_anchor` (path to the co-located path-proof transcript)

The human Evidence Index (`docs/evidence/INDEX.json`) **MUST** be updated in the same change. CI enforces:

* Human↔machine **1:1 parity**, and

* Presence and correctness of path-proofs.

---

## 8.8 Routing (titles-only)

* **Public payload & headers:**  
   **HDE-CLI-API-Vendor-Ref**

* **Preimage / rounding / banding:**  
   **HDE-Math-Spec**

* **Evidence policy & tokens:**  
   **HDE-Governance**

This section governs **mechanics only**; all concrete bytes, tokens, and schemas are owned by the PF-Canon documents above.

---

# 9\) Reader & Compat endpoints

## **9.1 Endpoint Catalog (JSON success) \[Required-Now\]**

**Purpose (normative).**  
 Provide a **canonical machine-readable inventory** of HTTP endpoints in the Engine repo and, within that inventory, clearly identify which endpoints are **JSON success routes eligible for A7 proofs**. Entries are titles-only; bytes/examples and detailed contract semantics remain in their single homes.

This catalog exists to prevent drift between code, QA plans, and audits by making endpoint classification explicit and testable.

**Scope & rules**

* **Single home (inventory).** `docs/ENDPOINTS_CATALOG.json` is the only machine-readable inventory of HTTP endpoints for this repo. It must include, at minimum:

  * public Reader endpoints,

  * compat endpoints (internal/admin as applicable),

  * internal identity endpoints (for example, `/internal/version`),

  * ops probe endpoints (health/ready/diagnostics), and

  * dev harness endpoints (for example, `/internal/dev/sampler`).

* **A7-eligible subset.** A7 proofs apply only to endpoints explicitly marked as **A7-eligible JSON success routes** in this catalog. `/internal/*` endpoints are **never** A7-eligible; `/internal/version` is operator-only and not A7-eligible (see HDE-Governance §10.5).

* **Classification is mandatory.** Every catalog entry MUST be classified into one of the following endpoint classes (names are for catalog entries; PF docs still route by title):

  * `public_reader`

  * `internal_admin` (includes internal/admin compat surfaces)

  * `internal_identity`

  * `ops`

  * `dev_harness`

* **Mixing responsibilities is permitted but discouraged.** Implementations may mix endpoint classes in one Python module, but the catalog must still carry per-endpoint classification so CI and QA can enforce distinct rails and posture per class.

**Catalog entry minimum fields (titles-only; schema owned elsewhere)**

Each entry in `docs/ENDPOINTS_CATALOG.json` MUST include, at minimum:

* `path` — for example `/reader`, `/api/compat/v1`, `/internal/version`, `/ops/health`, `/internal/dev/sampler`

* `method` — `GET`, `POST`, `HEAD` (or a list if an endpoint supports multiple methods)

* `classification` — one of the endpoint classes above

* `blueprint_module` — titles-only pointer to the owning module (for example `adapter/http_reader.py`, `engine/http/compat_handler.py`)

* `rails_profile` — short, names-only summary of rails and gating expectations (for example “requires APP\_ENV=dev”, “ops-only”, “A7 success posture”, “writer no-store posture”)

* `a7_eligible` — boolean (true only for JSON success routes eligible for A7 proofs)

* `env_gate` — for entries where reachability is env-gated (titles-only; exact gating semantics are routed to Governance/Infrastructure)

Field-level schema and validation for this catalog are owned by HDE-Schemas & Artifacts (titles-only). This guide defines the mechanical requirement that the catalog exists, is complete, and is used as the single inventory source.

**A7 invariants to prove (titles-only; for `a7_eligible=true` entries only)**

* **200:** quoted, strong `ETag`; `Vary: Authorization, Accept-Encoding`; success cache headers

* **HEAD:** status 200; validators mirror 200 (including `Content-Type`); `Content-Length == len(identity 200 body)`

* **304:** only after prior 200-with-body; **omit** `Content-Type` and **omit** `Content-Length`; validators mirror cached 200

* **Encoding invariance:** for the same canonical LF-terminated body, `ETag` identity and effective `Content-Length` are stable across accepted `Accept-Encoding` (identity/gzip/br)

* **Writers/errors posture:** non-success writers and error routes carry `Cache-Control: no-store` (recorded as headers-only evidence)

**Catalog files (single home)**

* `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) — machine-readable endpoint inventory with mandatory classification and A7 eligibility flags

* `docs/ENDPOINTS_CATALOG.json.sha256` — sidecar hash of the canonical bytes

**Proof artifacts (headers-only; one LF each; for A7-eligible entries)**

* `artifacts/proofs/endpoints_env_gate_proof.log` — proves non-prod entries are unreachable in prod

* `artifacts/proofs/success_get.txt` — GET 200 proof (quoted strong ETag, Vary)

* `artifacts/proofs/success_head.txt` — HEAD parity with GET 200

* `artifacts/proofs/success_304.txt` — 304 omission proof (CT/CL omitted; validators mirror)

* `artifacts/proofs/success_encoding_invariance.txt` — identity/gzip/br invariance proof

* `artifacts/proofs/success_writers_errors.txt` — writers/errors no-store posture

**Test expectations (mechanics only; titles-only routing for tokens).**

Mechanics requires that:

* Endpoints classified as `public_reader` (and any A7-eligible entries) have tests that verify canonical emitter usage and the expected status/header/body posture for their class.

* Endpoints classified as `dev_harness` or `ops` have explicit gating tests (APP\_ENV or equivalent) and are not treated as public transport surfaces.

Token semantics and acceptance are owned by HDE-Governance and Glow QA Guide (titles-only); PF14 records only that classification and tests must exist to keep endpoint posture enforceable and non-ambiguous.

---

## 9.2 Reader (dev harness only) \[Implemented (dev-only)\]

* **Route (dev-only).** `GET|POST /api/reader?v=1` is a **dev harness** enabled only when `APP_ENV=dev`; rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`; no vendor I/O).  
* **Emitter.** Uses the **allow-listed shared presenter/emitter** (see §4 / §10.2); tests must **not** bypass the shared emitter.  
* **Dev error posture.** `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, **no ETag**.  
* **A7 proofs boundary.** Harness may capture headers for **local evidence**, but authoritative A7 proofs run on a **Catalog JSON success** route; `/internal/version` remains an ops exception (see HDE-Governance §10.5).  
* **Pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Rails posture.** Rails defaults follow the **Env Deployment Inventory** (titles-only). The dev harness **does not perform vendor I/O**; tests may run with rails closed for evidence capture, but the default environment posture itself is owned by Infrastructure.

**Optional GET semantics (for local evidence only)**  
 If an optional **GET** is exposed in the harness, it **must** follow PF10 invariants for captures, **without** becoming the A7 proof surface:

* **200:** strong, quoted `ETag`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`; canonical JSON, one LF.  
* **HEAD:** status 200; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF-terminated, pre-compression).  
* **304:** only after prior 200-with-body; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror cached 200\.  
* **Encoding invariance (optional evidence):** for the same canonical body, **ETag identity** and **effective Content-Length** are stable across accepted encodings (identity/gzip/br).  
* **POST (dev harness):** non-conditional; never returns 304\.

**Acceptance (tokens; titles-only)**

* Core harness: `JSON_CANONICAL_CHECK_OK`, `CLI_READER_EMITTER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`.  
* If GET captures are taken (local-only, non-authoritative): `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK` *(captures here are supplemental; authoritative proofs remain on the Catalog route per §9.1).*  
* Evidence discipline: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

**Evidence (records-only; machine mirror; same-PR rule)**

* `reader/dev/parity` — harness vs CLI stdout byte-compare (expected empty).  
* `canonical_json/compare` — canonical re-serialization compare (one LF).  
* *(Optional, if GET exposed)* `transport/headers_200`, `transport/headers_head`, `transport/headers_304`, `transport/encoding_invariance`.  
   List titles/paths in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (canonical JSONL, one LF) with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update human Index and mirror **in the same PR**, with **path-proofs**.

**Routing (titles-only)**

* Transport matrices & A7 policy: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.  
* Ops endpoint posture: **HDE-Governance §10.5**.  
* Domains, catalogs, canonical JSON rules: **HDE-Schemas & Artifacts**.

---

## 9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]

* **Route.** `POST /api/compat/v1` (pair) — internal/admin surface (**not public**).  
* **POST non-conditional.** POST carries no validators and never returns 304\.  
* **GET (health).** Any GET used for probing carries **no body**.  
* **Emitter.** Same shared presenter/emitter as Reader (§4 / §10.2). Public JSON is canonical: UTF-8 (no BOM), sorted keys, compact, **one LF**; arrays-as-sets deduped & ASCII-sorted; run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Determinism.** AB↔BA parity and two-run identity hold; category iteration follows the **frozen Magic-10 order**.

**Acceptance (tokens; titles-only).**  
 `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`.

**Evidence (records-only; machine mirror).**  
 `compat/parity/abba_identity`, `compat/parity/two_run_identity`, `canonical_json/compare`. Update human Index and mirror **in the same PR**, with **path-proofs**.

**Ownership (titles-only).** Production transport matrices and public payload bytes are owned by **HDE-CLI-API-Vendor Ref** and **HDE-Governance**. Mechanics enforces wiring/determinism (single emitter, canonical JSON, AB↔BA/two-run) and **does not duplicate** public schemas or bytes.

---

## 9.4 Internal ops: `/internal/version` (ops-only) \[Required-Now\]

**Purpose (normative).** Operator surface for identity and provenance. **Not** a JSON success route and **not** A7-eligible (see HDE-Governance §10.5).

**Behavior (prod posture)**

* **GET 200\.** `Content-Type: application/json; charset=utf-8`; `Cache-Control: no-store`; **no ETag**; **Last-Modified absent**; `Vary` optional.  
* **HEAD 200 (parity).** Mirrors GET validators; **no body**; `Content-Length == len(identity GET body)`; `Content-Type == GET`.  
* **Conditionals ignored.** Requests with `If-None-Match` / `If-Modified-Since` are ignored; **never 304**.  
* **Pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Evidence (records-only; machine mirror)**

* `artifacts/ops/internal_version/headers_get.txt` — raw GET headers (proves no-store, no ETag, correct `Content-Type`).  
* `artifacts/ops/internal_version/headers_head.txt` — raw HEAD headers (HEAD 200; `Content-Type == GET`; `Content-Length ==` identity GET).  
* `artifacts/ops/internal_version/body_get.json` — exact LF-terminated GET body (six keys in frozen order) \+ `artifacts/ops/internal_version/body_get.sha256`.  
* `artifacts/ops/internal_version/cond_if_none_match_headers.txt` — GET with `If-None-Match` (still 200).  
* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt` — GET with `If-Modified-Since` (still 200).  
* `artifacts/ops/internal_version/two_run_identity.log` — two-run byte identity log.  
   List each artifact by title/path in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` with `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor`. Update human Index and mirror **in the same PR**.

**Acceptance (titles-only; token names live in HDE-Governance §2.0)**  
`INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`, **`INTVER_CACHECTL_NOSTORE_OK`**, plus Index/Mirror parity tokens. *(Tokens roster lives in Governance.)*

**Routing (titles-only).** Policy lives in **HDE-Governance §10.5**; transport matrices for success routes live in **HDE-CLI-API-Vendor Ref** (A7 not applicable here).

---

# 10\) Writer Surfaces (API)

**Purpose.** Provide **minimal, idempotent** writer endpoints (e.g., **preferences**) with **strict schema validation** and **deterministic effects**. Mechanics wires determinism and validation; **public transport rules and error headers live in Governance/CLI-API** (titles-only).

## 10.1 Contract (normative)

* **Idempotent semantics.** Repeating the **same request** produces the **same effect** and response semantics (no double-writes, no drift).  
* **Strict schema.** Requests **MUST** validate against the governing schema (titles-only to PF-Canon-HDE-Schemas & Artifacts). **Unknown or extra keys are rejected** (typed error).  
* **Normalization.** Where arrays represent sets, **dedupe & ASCII-sort**; category/channel IDs must be **canonical** (Magic-10 closed set; `NN-NN` min-first for channels).  
* **Explicit inputs only.** Writers **do not** read clocks/env/files and **do not** depend on locale.

  ## 10.2 Transport posture (titles-only; owned by Governance)

**Routing only.** Transport behavior is governed in **HDE-Governance §10** and matrices live in **HDE-CLI-API-Vendor Ref**. This guide does not restate headers or validator details.

**Writers and errors**

* `Cache-Control: no-store`; **no `ETag`**.  
* Errors: `Content-Type: application/json; charset=utf-8`; typed, numeric-free error bodies (see **HDE-CLI-API-Vendor Ref** error model).  
* Writers have **no HEAD/304 semantics**.

**Success endpoints (A7 proofs)**

* Proofs run only on a cataloged **Endpoint Catalog (JSON success)** route (see **HDE-CLI-API-Vendor Ref §5.6 / Appendix A**).  
* Details such as 200 `ETag`, cache policy, `Vary`, 304 omission rules, and HEAD parity are referenced by title in Governance; do not duplicate here.

**Internal ops**

* `/internal/version` is operator-only, **not** A7-eligible; behavior is specified in **HDE-Governance §10.5**.

**Acceptance (titles-only; tokens live in HDE-Governance §2.0)**

* Writers/errors: `EVIDENCE_INDEX_UPDATED_OK` (evidence present), plus Governance A7 family excluded for writers.  
* Success routes (owned by Governance): `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `READER_VARY_ACCEPT_ENCODING_OK`, `READER_VARY_AUTHORIZATION_OK`.  
* Internal ops: `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`.  
  ---

## 10.3 Determinism & safety

* **Two-run identity (effect).** Two identical writer invocations over the same state produce **identical post-state** and the same response semantics.  
* **Order stability.** Any JSON emission (if the writer returns a body) uses the **Canonical Serialization Package** (§4): UTF-8 no BOM, **sorted keys**, compact, **one LF**; arrays-as-sets **deduped & ASCII-sorted**; checks under **`LC_ALL=C`**.  
* **No RNG/time.** Writers do **not** consult clocks or randomness; no non-deterministic merges.

## 10.4 Errors & logging (internal)

* **Typed errors only.** `invalid_input`, `invalid_json`, `unknown_key`, etc. (PF-05 titles-only); **no PII/secrets**.  
* **Keys-only logs.** Never log request/response bodies, header values, or secrets; redact references; bounded labels.

## 10.5 Validation (binary)

1. **Schema pass:** request validates; **unknown/extra keys → fail** (typed error).  
2. **A7 writers posture:** responses carry **`no-store`**, **no `ETag`** (titles-only to Governance).  
3. **Idempotence:** re-issuing the same request leaves state unchanged; response semantics unchanged.  
4. **Canonical bytes (if body present):** canonical re-serialization byte-compare passes (UTF-8/no BOM, sorted keys, **one LF**, arrays-as-sets).  
5. **No locale/I/O:** static/grep checks show **no** file/env/time use in writer modules.

## 10.6 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)

* **artifact\_key:** `writers/no_store_headers` — header proof (`no-store`, no `ETag`).  
* **artifact\_key:** `writers/schema_validation` — JSON-Schema validation log (unknown/extra → typed error).  
* **artifact\_key:** `writers/two_run_idempotence` — two-run idempotence/effect proof.  
* **artifact\_key:** `canonical_json/compare` — canonical re-serialization compare (if a body is returned).  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`. Update the **human Evidence Index** in the **same change**; CI enforces **human↔machine parity** and **path-proofs**.

**Routing (titles-only).**

* **Transport rules & error headers:** **PF-Canon-HDE-Governance** (A7; writers/errors).  
* **Error shapes & public bytes:** **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* **Schemas & canonical JSON:** **PF-Canon-HDE-Schemas & Artifacts**.

---

# 11\) Input Normalization & Validation Layer 

**Scope.** Normalize IDs and **validate payloads against schemas** (titles-only to **PF-Canon-HDE-Schemas & Artifacts**). Mechanics **wires** the checks; it **does not restate** schemas here.

## 11.1 Viewer prefs (normative)

**Closed set & types**

* `top_category ∈` **Magic-10** (frozen IDs; fixed order).  
* `weights` contains **exactly ten keys**, one per Magic-10 ID; each value is an **int `0..100`**.  
* `preset` is **optional** and, when present, is drawn from a **declared preset catalog** (titles-only).

**Zero-weight rule**

* If a weight is **0** for category **X**, candidates whose **\#1 \== X** are **excluded** (enforced in the sampler/ranker, §11.3).

**Aliases & unknowns**

* **Default alias policy \= OFF.** Unknown IDs **reject** with a **typed input error**.  
* If input aliases are **explicitly enabled**, they **must** normalize via the **declared alias ledgers** (titles-only to PF-Canon-HDE-Schemas & Artifacts A1/A4/A5). Outputs remain **canonical**.

**Canonicalization (inputs)**

* Input JSON is normalized to **UTF-8 (no BOM)**, **ASCII-sorted keys**, **compact**, **exactly one LF**; arrays-as-sets are **deduped & ASCII-sorted**. All byte checks run under **`LC_ALL=C`**.

**AB↔BA neutrality**

* Normalization **MUST** produce **identical normalized forms** for `(A,B)` and `(B,A)`.  
  ---

  ## 11.2 Validation (binary)

1. **Completeness.** `weights` includes **all ten** category keys; each value is **int `0..100`**.  
2. **Invalid shapes.** Malformed/missing keys or floats ⇒ **`invalid_prefs`** (typed error).  
3. **Schema pass.** Payloads validate against their owning schemas (titles-only to PF-Canon-HDE-Schemas & Artifacts).  
4. **Canonical bytes.** **Re-serialize canonically** and byte-compare (must match); **one LF**, **no BOM/ANSI**.  
5. **ABBA check.** Normalized forms for `(A,B)` vs `(B,A)` are **byte-identical**.

**Routing (titles-only).**

* Magic-10 IDs & order: **PF-Canon-HDE-Schemas & Artifacts §2.6**, **PF-Canon-HDE-Math-Spec §5.1**.  
* Public Reader contract: **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* Canonical JSON & pack: **PF-Canon-HDE-Schemas & Artifacts §4**.  
* Governance tokens: **PF-04 — §2.0 Acceptance Tokens**.  
  ---

  ## 11.3 Swipe Sampler & Ranker

**Purpose.** Build a candidate pool that respects viewer weights (including the **zero-weight rule**) and then **rank deterministically**. Deterministic \= **order-neutral (AB↔BA)** and **seedable** (when used in **dev/admin** flows); **seeds never affect public bytes**.

### 11.3.1 Sampling & exclusion

* **Zero-weight rule.** Exclude any candidate whose **\#1** equals a viewer weight of **0**.  
* **Pool formation.** Apply viewer **eligibility filters** (titles-only), then enforce **diversity** (§11.3.3) **before** ranking.

  ### 11.3.2 Scoring & ranking (deterministic)

* **Score function.** Deterministic **fixed-point** combination across the ten categories (integer path), consistent with **PF-01** rounding/banding (titles-only).  
* **\#1 influence.** The other party’s **\#1** may serve as a **stable tie-break** (integer/priority rule); the rule **must be pinned** and **stable**.  
* **Total order.** Sort by the specified **numeric** direction, then break ties by **ID comparator (ASCII)** to guarantee a **stable total order** (§5).  
* **Seedability.** Any stochastic element (if used in **non-public** flows) **must be seedable & isolated**; the seed does **not** alter public bytes.

  ### 11.3.3 Diversity acceptance (deterministic)

* **Sliding window:** `K = 50`.  
* **Cardinality bound:** at most `N = 2` share the same **design fingerprint** within the window.  
* **No recent repeats:** none repeat from the last `R = 20`.  
* **Fingerprint.** A **deterministic** function (titles-only to PF-Math/PF-Spec) used **only** for diversity checks (**never exposed**).

  ### 11.3.4 Dev-only sampling endpoint (optional harness)

* **Endpoint (dev-only).** `POST /api/sample/v1` with body containing `viewer_prefs{…}` and optional `seed:int`.  
* **Response.** List of **candidate IDs only**; the app hydrates details. If a seed was provided, **echo it in `meta`**.  
* **Determinism.** With the same inputs/seed, the output is **byte-identical**; **AB↔BA** has no effect on ordering.

  ### 11.3.5 Validation & evidence (binary; path-agnostic)

* **Zero-weight exclusion** demonstrably enforced.  
* **Stable order:** ABBA and two-run proofs; **comparator laws** honored (see §5).  
* **Diversity checks:** window `K`, bound `N`, and recent `R` constraints verified.  
* **Seed replay:** identical inputs/seed → **identical outputs**; seed echoed in `meta` when used.  
* **Canonical bytes:** outputs are canonical JSON (UTF-8 no BOM, sorted keys, compact, **one LF**).  
* **Evidence Index:** append artifacts (sampler snapshots, seed replay logs) **in the same PR**; **PF-12 machine mirror** lines present with **path-proofs**.

**Routing (titles-only).**

* Scoring/banding/rounding rules: **PF-Canon-HDE-Math-Spec**.  
* Public contract & transport: **PF-Canon-HDE-CLI-API-Vendor-Ref**, **PF-Canon-HDE-Governance (A7)**.  
* Canonical JSON rules: **PF-Canon-HDE-Schemas & Artifacts §4**.

### **11.3.6 Engine sampler core (pure-compute implementation)**

**Scope (normative).**  
 The Dissolution sampler/ranker behavior described in §11.3 is realized in the engine as a **pure-compute sampler core**. Mechanics records both the canonical module/entrypoints and the behavioral contract so that future work can change internals without breaking determinism, eligibility, or harness behavior.

**Canonical module and entrypoints.**

* The canonical sampler core module lives at `engine/sampler/core.py` and exports the pure-compute helpers that implement the contracted behavior in §11.3:

  * `build_candidate_pool` — constructs the in-memory candidate pool from viewer inputs and candidate feature records, enforcing zero-weight exclusion and eligibility filters.

  * `rank_candidates` — applies the deterministic ordering rules over the pool (weight, compat score, band priority, ID comparator) to produce a total order.

  * `sample_and_rank` — the main helper used by dev/admin harnesses to build the pool, apply diversity where configured, and produce a ranked list of candidates.

* CLI and HTTP sampler harnesses in this repo (including the dev/admin CLI sampler and the `/internal/dev/sampler` HTTP harness) **MUST** call these canonical helpers rather than reimplementing sampling or ranking logic locally. Mechanics treats `engine.sampler.core` as the **single home** for sampler/ranker behavior; harnesses add only I/O, env wiring, and evidence capture.

**Pure-compute contract.**

The sampler core operates on in-memory data structures (for example, viewer profile, candidate feature records, sampler configuration, candidate pool entries, and ranked candidates) and **returns new values only**. It does **not**:

* perform file or network I/O,

* read environment variables, clocks, or random sources, or

* mutate module-level state.

Zero-weight rules and basic eligibility are enforced **inside the core**:

* candidates with weight `<= 0` are excluded from the pool before any other checks (zero-weight rule),

* minimum compat score and band-based filters (allowed/excluded bands) are applied according to the sampler configuration, and

* optional diversity markers and recency flags are carried through in the pool entries for later diversity phases.

**Deterministic ordering.**

Deterministic ordering in the sampler core is implemented by:

* preferring higher weight, then higher compat score,

* applying a **band priority** derived from the canonical band ordering (for example, Glow \> Warm \> Open \> Cool, consistent with the `BANDS` tuple from compat thresholds), and

* using the existing **ID comparator** (ASCII comparator over person identifiers) as the final tie-break to guarantee a **total order**, in line with the comparator laws in §5.

These rules must be applied by `rank_candidates` and any helper that produces a ranked candidate list. For a fixed viewer profile, candidate feature set, and sampler configuration, running the sampler core twice with the same inputs and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`) **MUST** yield byte-identical ranked candidate sequences (two-run identity) and respect AB/BA sanity as described in §11.3.

**Harness usage (routing only).**

* Dev/admin CLI sampler and HTTP sampler harnesses **MUST**:

  * construct their in-memory inputs (viewer profile, candidate feature records, sampler configuration) and then call `sample_and_rank` (or the equivalent composition of `build_candidate_pool` and `rank_candidates`), and

  * treat any deviations from the canonical sampler core behavior (for example, alternative ordering or eligibility rules) as defects.

* Evidence and acceptance tokens for sampler behavior and sampler evidence families remain single-homed in **HDE-Schemas & Artifacts**, **HDE-Build Checklist**, **Glow QA Guide**, and **HDE Phased Epics** by title; this section records only that the sampler core behavior in §11.3 is implemented by the canonical `engine.sampler.core` module and its entrypoints and that all harnesses and evidence generators must call into that module under the determinism and closed-rails posture described elsewhere in this guide.  
  ---

  # 12\) Error Envelope & Token Set \[Required-Now\]

**Purpose.** Provide a **central formatter** for typed, numeric-free errors. Public error transport (writers/errors `no-store`, headers) lives in **PF-Canon-HDE-Governance** and **PF-Canon-HDE-CLI-API-Vendor-Ref** (titles-only). **Identity/Meta** content has been moved to **§13 (Identity & Provenance Module)** and **§14 (Internal Meta Surface)** to avoid duplication.

## 12.1 Error envelope (normative)

* **Shape (exact):** `{"ok": false, "code": "<lower_snake_token>", "error": "<human message>"}` — **only** these keys.  
* **Canonical JSON:** UTF-8 (no BOM), **ASCII-sorted keys**, compact, **exactly one trailing LF**; checks under **`LC_ALL=C`**.  
* **Numeric-free & secret-free:** never include stack traces, payload excerpts, header values, or secrets; keys-only logs (redacted).  
* **Deterministic mapping:** the same condition always yields the same `{code,error}` pair; **byte-stable** across Reader and CLI.

  ## 12.2 Token set (lower\_snake; examples)

**Tokens include (non-exhaustive):**

* `invalid_prefs` — malformed/missing/float/out-of-range weights.  
* `missing_narrative_key` — no mapping for `(category, band, personal|shared)`.  
* `invalid_json` — mixed id/payload for `a`/`b` (or schema violation at envelope root).

The canonical **token→message map** is tested and stored as evidence (titles-only). Add/retire tokens via Doc-Delta; message text is stable and versioned in the map.

## 12.3 Transport (titles-only)

* **Writers & errors posture:** `Cache-Control: no-store`; **no `ETag`**; `Content-Type: application/json; charset=utf-8` (PF-04).  
* **A7 success rules** are **not** restated here (see PF-04/PF-05).

  ## 12.4 Acceptance (binary; tokens & evidence are titles-only)

1. **Schema:** envelope has **exactly** `ok=false`, `code`, `error`; no extras; LF-terminated, canonical JSON.  
2. **Casing & map:** all tokens are **lower\_snake**; the **token→message** table matches the golden map (**exact bytes**).  
3. **Parity:** the same error emitted by **Reader and CLI** is **byte-identical**.  
4. **Two-run identity:** re-emitting the same error twice produces **bitwise-identical** bytes.  
5. **Transport coupling:** when the envelope appears in writers/errors, headers match PF-04 (no-store; no `ETag`).

**Gating tokens (titles-only):** `ERROR_TOKEN_MAP_OK`, `ERROR_JSON_CANON_OK`, `CLI_READER_EMITTER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

## 12.5 Evidence (records-only; path-agnostic; indexed via PF-12 machine mirror)

* **artifact\_key:** `errors/token_map` — canonical token→message snapshot (golden).  
* **artifact\_key:** `errors/schema_check` — JSON-Schema check for the envelope.  
* **artifact\_key:** `errors/canonical_check` — encoding/key-order/compact/LF proof.  
* **artifact\_key:** `parity/errors_reader_cli` — byte-equality for the same error via Reader and CLI.  
   Each mirror record includes `artifact_key, sha256, size_bytes, produced_at_utc, discovered physical_path, proof`; update the **human Evidence Index** in the **same change**; CI enforces **1:1 parity** and **path-proofs**.

**Routing (titles-only).**

* Error shapes & code map ownership: **PF-Canon-HDE-CLI-API-Vendor-Ref**.  
* Writers/errors transport posture: **PF-Canon-HDE-Governance**.  
* Canonical JSON & mirror rules: **PF-Canon-HDE-Schemas & Artifacts §4/§8**.  
* Engine identity & `/internal/version`: **§13** and **§14** (this guide does not duplicate those bytes).  
  ---

# 13\) Identity & Provenance Module \[Required-Now\]

**Purpose.** Single source of truth for **engine** and **release** identity. Values are **initialized once per cut** and are **read-only thereafter**; all public and operator surfaces **consume via helpers** (no direct env reads at emit time).

## 13.1 Fields (read-only after freeze; stable key order)

Expose and persist **exactly** these fields; **no extras**:

1. `engine_tag` — opaque engine identity string pinned at build.  
2. `build_commit` — VCS short SHA for bundled repo head at cut time (**optional** on public/ops; may be unset).  
3. `invocation_tag` — canonical **short** tag for the current Invocation (public meta carries the **tag only**).  
4. `invocation_sha256` — **SHA-256** of the canonical Invocation text/bytes captured at cut (stable per cut; **evidence/admin** use; not added to public meta).  
5. `emitter_sha256` — SHA-256 over the **allow-listed presenter/emitter** source captured at cut (**evidence/admin**; not public).  
6. `release_id` — lowercase hex-64 of `sha256(canonical_bytes("catalog/manifest.json"))` computed at freeze-pack.

**Source of truth (titles-only):** `release_id` derives **only** from the PF-12 pack manifest; Invocation tag/bytes come from the Invocation registry; `engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` are taken from the **build snapshot** at cut. No request-time hashing.

## 13.2 Accessors

* **`identity_meta()` →** `{"engine_tag","invocation_tag"}` — inserted into the **public** envelope **before** idempotence hashing (**PF-01 §3.2**).  
* **`identity_admin()` →** `{"engine_tag","release_id","invocation_tag","invocation_sha256","build_commit","emitter_sha256"}` — for **internal/admin** surfaces (e.g., **/internal/version**, evidence capture).

  ## 13.3 Flow & constraints

* **Fetch-only module.** Presenter (Reader) and CLI call this module’s helpers; **no direct env reads** at emit time; **no mutation** after freeze.  
* **Preimage coupling.** `identity_meta()` enters the **five-key preimage** (public path) **before** `idempotence_hash` is computed (PF-01 §3.2).  
* **Evidence coupling.** The same values flow into artifacts and audit evidence (titles-only); **do not duplicate** identity bytes in prose or ad-hoc files.

  ## 13.4 Prohibited

* **No recomputation of `release_id`** during request handling.  
* **No mutation** of identity fields after freeze.  
* **No alternative sources** (env vars, flags) on public paths.  
* **No request-time hashing** for `emitter_sha256` or `invocation_sha256` — compute at **build only**.

  ## 13.5 Acceptance (binary; titles-only)

1. **Two-run identity:** repeated emits with identical inputs yield **bitwise-identical** bytes (**one LF**).  
2. **`release_id` recompute:** equals **sha256(canonical manifest bytes)**; recompute job passes.  
3. **Reader↔CLI parity:** public bodies include `identity_meta()` and remain **byte-identical**.  
4. **Emitter/Invocation identities:** recorded `emitter_sha256` and `invocation_sha256` **match** their build-time evidence captures.

**Gating tokens:** `RELEASE_ID_RECOMPUTE_OK`, `TWO_RUN_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

## 13.6 Evidence (records-only; path-agnostic; indexed via the machine mirror)

**Scope (normative).** Identity artifacts are **records-only** and MUST be listed by title/path in **Appendix D: Evidence Index** and mirrored **1:1** in `artifacts/evidence_index.jsonl`. Mirror records are canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one trailing `\n`) and include: `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update the human Index and mirror **in the same commit/PR**; CI fails on mismatch or missing path-proofs. All captures run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Artifact keys (titles-only)**

* **`pack/manifest`** — canonical manifest bytes (freeze pack).  
* **`identity/release_id`** — frozen `release_id` (64-hex).  
* **`identity/release_id_recompute`** — recompute proof log (on-disk equals canonical; sha256 over canonical bytes).  
* **`identity/emitter_sha256`** — presenter/emitter source hash (proves single shared emitter).  
* **`identity/invocation_sha256`** — invocation canonical-bytes hash (admin provenance).  
* **`identity/service_identity`** — admin snapshot of identity fields (JSON; LF-terminated; numeric-free).  
* **`parity/two_run_identity`** — two-run identity digest/log (byte-equal outputs; LF-terminated).

**Mirror discipline (MUST)**

* One JSON object per line; reject unknown keys in mirror records.  
* `(artifact_key, discovered_physical_path)` in the mirror equals `(title, path)` in the human Index (strict 1:1 join).  
* A `path_proof.txt` (or equivalent) is stored alongside each artifact and referenced by `proof_anchor`.

**Routing (titles-only).**

* Pack/manifest & `release_id`: **HDE-Schemas and Artifacts §6**.  
* Invocation & preimage rules: **HDE-Math-Spec §3**.  
* Transport ops surface: **§14 Internal Meta Surface** (policy owned by **HDE-Governance**).  
  ---

# 14\) Internal Meta Surface \[Required-Now\]

## 14.1 Purpose & scope (normative)

Operator-only, side-effect-free endpoint exposing engine identity for diagnostics. **Single home:** `GET /internal/version`.

## 14.2 Payload (exact fields; frozen key order)

Expose **exactly six** provenance fields — **no extras** — in this **frozen order**:

1. `engine_tag`  
2. `build_commit`  
3. `invocation_tag`  
4. `invocation_sha256`  
5. `emitter_sha256`  
6. `release_id`

**Source of truth.** Values originate from the Identity & Provenance Module (§13) and are read-only after freeze (see **HDE-Schemas & Artifacts** for release identity rules).

## 14.3 Transport (ops posture)

* `Cache-Control: no-store`  
* **No ETag**; **Last-Modified absent**  
* `Content-Type: application/json; charset=utf-8`  
* **HEAD parity.** `HEAD /internal/version` returns **200** and mirrors 200 validators (incl. `Content-Type`); body is empty; `Content-Length == len(identity GET body)`  
* **Conditionals ignored.** `If-*` validators are ignored; this endpoint **never** serves 304  
* **Vary:** optional (MAY be present; not required for acceptance)  
   *(Policy owner: **HDE-Governance**; Mechanics reiterates here for ops wiring.)*

## 14.4 Posture

* Operator-only; minimal payload; no secrets; no side effects.  
* Body is **canonical JSON** (UTF-8/no BOM, compact, **exactly one LF**).  
* **Key order is frozen as in §14.2** (do **not** re-sort keys for this endpoint).

## 14.5 Example (informative)

**Request** `GET /internal/version`  
 **Response** `200 OK` `Cache-Control: no-store` `Content-Type: application/json; charset=utf-8`

{"engine\_tag":"hdengine-x.y.z","build\_commit":"\<shortsha\>","invocation\_tag":"INV-…","invocation\_sha256":"\<64hex\>","emitter\_sha256":"\<64hex\>","release\_id":"\<64hex\>"}

## 14.6 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **Headers/behavior:** `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`  
* **Body shape:** six fields in frozen order; canonical JSON; numeric-free; exactly one LF  
* **Stability:** two consecutive GETs produce byte-identical bodies (**two-run identity proof recorded**)  
* **Index discipline:** **Evidence Index (human)** and **machine mirror** updated in the **same PR**; human↔machine **1:1 parity** enforced

## 14.7 Evidence (records-only; path-agnostic; indexed via the machine mirror)

* `intver/headers_get` — raw GET headers (proves **no-store**, **no ETag**, correct `Content-Type`)  
* `intver/headers_head` — raw HEAD headers (200; `Content-Type == GET`; `Content-Length ==` identity GET)  
* `intver/body_get` — exact LF-terminated GET body bytes \+ digest record  
* `intver/cond_if_none_match` — conditional GET (`If-None-Match` ignored → 200\)  
* `intver/cond_if_modified_since` — conditional GET (`If-Modified-Since` ignored → 200\)  
* `intver/two_run_identity` — two-run identity log (byte-equal bodies)  
* `intver/provenance_note` — operator note (`release_id`, `invocation_tag`, optional `build_commit`, capture timestamp)

Each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`. Update the human Evidence Index in the **same change**; CI enforces **1:1 parity** and **path-proofs**.

## 14.8 Routing (titles-only)

* **HDE-Governance §10.5** — `/internal/version` policy (no-store, no ETag, conditionals ignored, HEAD parity)  
* **HDE-Math-Spec §3** — identity/preimage rules (single home for idempotence & identity semantics)  
* **HDE-Schemas & Artifacts §6** — pack/manifest coupling for `release_id`  
  ---

# 15\) Narrative Selection Router (keys only)

**Purpose**  
 Map viewer/context inputs to narrative keys without generating text.

**Inputs**

* `category`  
* `band`  
* `perspective` (exactly one of: `personal`, `shared`)  
* `viewer_top`  
* `flags`

**Output**

* `{ personal_key, shared_key }` — both drawn from the **Narrative Key Registry**.

**Rules**

* Deterministic; **no RNG**.  
* **Never** generates narrative text.  
* If a mapping is missing ⇒ return **`missing_narrative_key`** (no fallback).

**Routing & proofs (titles-only)**

* Authoring **DB plane** (intake, lints, preview) and runtime **file-backed pack** (sealed; no DB in hot path) live in the **Narratives Guide** / **Schemas & Artifacts**.  
* Mechanics proves **determinism** and **parity (CLI \= HTTP)**, and records **keys-only evidence** in the **same PR**.

# 16\) Narrative Key Registry and Manifests

**Purpose**

* Versioned registry guarantees **exactly one key** per `(category, band, perspective)`.  
* Manifests are **diffable**; **no prose** is stored in the engine.  
* **Build guard:** fail the build if any mapping is **missing** or **ambiguous**.

**Pack identity (routing)**

* Identity is **manifest-driven**: `pack_sha = sha256(canonical manifest bytes)`.  
* Files are uploaded to immutable object storage at `/narratives/<pack_sha>/…`.  
* Exporter/loader procedures and coverage policy are **routed by title**; Mechanics **does not restate bytes** here.  
* CLI Tooling \[Required-Now\]

**Scope.**

* The CLI uses the shared engine and the allow-listed presenter/emitter to produce public bytes.

* All byte checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Authoritative contract: the CLI must conform end-to-end to **PF05-Canon-HDE-CLI-API-Vendor-Ref** for commands/flags, payload shapes, error model, streams/exits, and help/version formatting (titles-only; PF05 governs).

* **Admin preview posture.** The narrative preview surface is enabled by default for admins across dev/stage/prod and uses the same emitter as Aux; bytes parity and LF discipline apply. (Bytes and route live in PF05 by title.)

  ---

  ## 16.1 Command catalog (titles-only; PF05 governs)

**Single home for commands.**  
 The complete CLI command/flag catalog and their status live in PF05 (for example, “Commands (by status)”, “CLI Overview & Conventions”). This guide does not enumerate all commands.

**Conformance expectation.**  
 CLI help/usage, flags, and behavior must match PF05; any divergence is a defect until corrected.

**Examples (non‑exhaustive).**

* `hdctl showcompat …` — prints the **compat JSON payload** (admin/test surface) to `stdout` as canonical JSON (UTF‑8, sorted keys, compact, one LF) and, when invoked with `--dump-reader`, writes the exact Reader v1 public body (six keys) using the shared presenter/emitter. Reader↔CLI parity is defined between the Reader API and the `--dump-reader` output; CLI determinism (AB↔BA and two‑run identity) is merge‑blocking until the associated tokens are green.

* `hdctl sample …` — prints the same deterministic selection/ordering as the corresponding Reader surface documented in PF05.

* Additional commands (for example, `read singlebg`, `list people`, disabled `fetch *`) are defined and governed in PF05; this document only illustrates conformance expectations.

---

## 16.2 Streams & exits

* **stdout (success):** public JSON body only, LF-terminated, no ANSI, no extra bytes.

* **stderr (failure):** typed JSON errors only; diagnostics without secrets/PII; success never writes to stderr.

* **Exit codes:** 0 success; 64 usage error; non-zero for other failures.

* **No mixed streams.** A run is either stdout-only success or stderr-only failure.

  ---

  ## 16.3 Determinism & parity

* **Reader↔CLI parity.** CLI stdout is byte-identical to the Reader 200 body for mirrored surfaces (single emitter).

* **AB↔BA identity.** Pair order neutrality holds for pair-sensitive inputs.

* **Two-run identity.** Identical inputs ⇒ identical bytes (single LF).

* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact separators, one LF; arrays-as-sets deduped and ASCII-sorted (see §4/§10.1).

* **Merge-blocking status.** `showcompat` remains merge-blocking until the parity/determinism acceptance tokens in §16.7 pass.

  ---

  ## 16.4 Inputs & schemas (titles-only)

* **IDs & catalogs.** Validate against **HDE-Schemas & Artifacts** (§2.1/§2.6).

* **Viewer prefs.** `--prefs` matches the closed 10-key weight map and `top_category ∈ Magic-10` (see **HDE-Math-Spec** §2.2/§5.x).

* **Rails.** Default SAFE rails; CLI must not open vendor rails unless explicitly configured (see §7.1/§7.3).

  ---

  ## 16.5 Installability & entrypoints

* **Console script.** `pyproject` console-script `hdctl` present and installable.

* **Module-run.** `python -m engine.cli` parity proven with console script.

* **Packaging.** Build/install in a clean env succeeds; help/version behave as specified.

  ---

  ## 16.6 Environment pins (runtime)

* **Pins.** `LC_ALL=C`, `LANG=C`, `TZ=UTC`; keys-only logs; no ANSI.

* **Allow-list.** CLI reads only documented env and fails-closed on unknowns (see §31.2).

  ---

  ## 16.7 Acceptance (titles-only; token names live in HDE-Governance §2.0)

**Entrypoints/install:**  
 `CLI_PYPROJECT_ENTRYPOINT_OK, CLI_MODULE_RUN_OK, CLI_INSTALL_OK, CLI_HELP_EXIT_0_OK, CLI_HELP_STDOUT_OK.`

**Streams/exits:**  
 `CLI_USAGE_ERR_EXIT64_OK, CLI_STDERR_ONLY_ON_ERROR_OK, CLI_STDOUT_LF_OK.`

**Parity/determinism:**  
 `CLI_READER_EMITTER_PARITY_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_AB_BA_PARITY_OK, JSON_CANONICAL_CHECK_OK, PREIMAGE_RECOMPUTE_OK, CLI_IMPLEMENTED_SET_OK.`

**Evidence discipline:**  
 `EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_PATHS_VALIDATED_OK.`

**Parity harness tokens:**  
 `CLI_INSTALL_OK, CLI_HELP_OK, CLI_SHOWCOMPAT_PRESENT, CLI_SHOWCOMPAT_CANON_OK, CLI_AB_BA_PARITY_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_READER_EMITTER_PARITY_OK.`  
 (Roster frozen in Governance.)

**Preview posture:**  
 `CLI_PREVIEW_ENABLED_OK · CLI_PREVIEW_INDEXED_OK.`

---

## 16.8 Evidence (records-only; machine mirror; same-PR rule)

List by title/path in **Appendix D: Evidence Index** and mirror 1:1 in `artifacts/evidence_index.jsonl` (record fields as per §1.3). The machine mirror is canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF), rejects unknown keys, and each record includes a `proof_anchor` to a co-located path-proof file. Update the human Index and machine mirror in the same PR.

Required artifacts:

* `artifacts/cli/ab.json` — canonical output for AB inputs (LF-terminated)

* `artifacts/cli/ba.json` — canonical output for BA inputs (must be byte-identical to AB)

* `artifacts/cli/summary.json` — canonical JSON with attempted commands, sha256 of `ab.json` / `ba.json`, and `ab_ba_equal: true`

* `artifacts/cli/guards/emitter_symbol_proof.txt` — single-emitter guard (presenter symbol)  
* `artifacts/cli/guards/serializer_grep_guard.log` — grep-guard proving there are no ad-hoc serializers on public paths

* `audit/gates/canonical/json_canonical_check.log` — canonical JSON checks

* `audit/gates/canonical/json_canon_compare.log` — canonical output comparisons

(Index human+machine in the same PR; mirror canonical JSONL; one LF; `proof_anchor` present.)

# 17\) CLI Components

## 17.1 Command catalog (titles‑only; PF05 governs)

**Single home for commands.**  
 The complete CLI command/flag catalog and their status live in **PF05 — HDE‑CLI‑API‑Vendor‑Ref** (for example, “CLI Overview & Conventions”, “Commands (by status)”). PF14 does **not** enumerate or norm all commands; it records mechanical expectations and routes to PF05 by title.

**Conformance expectation.**  
 CLI help/usage, flags, and behavior **must** match PF05. Any divergence between `hdctl` behavior and PF05 is a defect until corrected (or PF05 is updated).

**Examples (non‑exhaustive).**

* \* \`hdctl showcompat …\` — canonical compat harness for comparing two users and driving Aux narrative preview. On success, its primary success payload is a single compat JSON document on stdout (admin/test surface), emitted via the shared presenter/emitter as canonical JSON (UTF‑8, ASCII-sorted keys, compact, one LF; no ANSI). When \`--dump-reader \<path\>\` is present, it also writes the six-key Reader v1 success envelope to \`\<path\>\` using the same emitter; those bytes must be byte-identical to the Reader 200 body for the same inputs/environment. The command remains merge-blocking until the compat JSON determinism and Reader↔CLI parity tokens are passing.  
* Additional commands (for example, `read singlebg`, `list people`, `bg:resolve`, and disabled `fetch` variants) are defined and governed in PF05, including whether they are **Required‑Now** or **Speculative**. Implement and test them according to PF05 without redefining schemas or bytes here.

---

## 17.2 Streams & exits

* **stdout (success):** public JSON body only, LF‑terminated, no ANSI, no extra bytes.

* **stderr (failure):** typed JSON errors only; diagnostics without secrets or PII; successful runs never write to stderr.

* **Exit codes:**

  * `0` — success (canonical payload on stdout only).

  * `64` — usage error (bad flags/arguments; synopsis to stderr; stdout empty).

  * Other error codes are non‑zero and command‑specific as defined in PF05; in all cases stdout remains empty on failure.

* **No mixed streams.** A run is either **stdout‑only success** or **stderr‑only failure**; commands must not interleave diagnostics with public bytes.

---

## 17.3 Determinism & parity

* **Reader↔CLI parity.** For each mirrored surface where the CLI emits Reader v1 bytes (stdout or via a reader-dump path, as defined in \*\*HDE-CLI-API-Vendor-Ref\*\*), those CLI bytes are byte-identical to the Reader 200 body for the same inputs/environment (single shared emitter, canonical JSON, exactly one LF). For \`hdctl showcompat\`, parity is defined between Reader HTTP and the \`--dump-reader\` sidecar file; stdout compat JSON is governed separately by determinism and canonical-JSON tokens.

* **AB↔BA identity.** For pair‑sensitive inputs, swapping the parties (A/B) yields identical outputs once normalized.

* **Two‑run identity.** Repeating the same command with identical inputs and environment yields byte‑identical stdout (single LF).

* **Canonical JSON.** All success payloads use canonical JSON: UTF‑8 (no BOM), ASCII‑sorted keys, compact separators, exactly one trailing LF. Arrays used as sets are deduped and ASCII‑sorted (see PF14 §4/§10.1).

* **Merge‑blocking status.** `hdctl showcompat` remains merge‑blocking until the parity/determinism acceptance tokens in §17.7 are passing.

---

## 17.4 Inputs & schemas (titles‑only)

* **IDs & catalogs.** CLI commands that accept IDs or cataloged names validate them against **HDE‑Schemas & Artifacts** (§2.1/§2.6). This guide does not duplicate schema bytes.

* **Viewer prefs.** `--viewer-prefs-file` / `--prefs` flags must carry the closed 10‑key weight map with `top_category ∈ Magic‑10` and weights for all ten Magic‑10 categories (see **HDE‑Math‑Spec** §2.2/§5.x). PF05 owns the exact CLI flag shapes.

* **Rails.** CLI runs under SAFE rails by default and **must not** open vendor rails on its own. Any command that can reach vendor or external HTTP must honor the rails and override semantics defined in PF04/PF07/PF05 (§7.1/§7.3 here, and the rails sections in Governance/Infrastructure).

---

## 17.5 Installability & entrypoints

* **Console script.** The `pyproject` console‑script entrypoint `hdctl` is present and installable.

* **Module‑run.** `python -m engine.cli` behaves identically to the console script; parity is required for help, version, and command invocation.

* **Packaging.** Building and installing the CLI in a clean environment succeeds. `hdctl --help` and `hdctl --version` behave as specified in PF05 (exit 0; output to stdout; no stderr noise).

---

## 17.6 Environment pins (runtime)

* **Pins.** All CLI acceptance jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Logs are keys‑only, with no ANSI escapes.

* **Env allow‑list.** The CLI reads only documented environment variables and **fails closed** on unknown or malformed env that would affect behavior (see PF14 §31.2 and PF05 env/flags sections). Secrets are never echoed.

---

## 17.7 Acceptance (titles‑only; token names live in HDE‑Governance §2.0)

**Entrypoints/install:**  
 `CLI_PYPROJECT_ENTRYPOINT_OK, CLI_MODULE_RUN_OK, CLI_INSTALL_OK, CLI_HELP_EXIT_0_OK, CLI_HELP_STDOUT_OK.`

**Streams/exits:**  
 `CLI_USAGE_ERR_EXIT64_OK, CLI_STDERR_ONLY_ON_ERROR_OK, CLI_STDOUT_LF_OK.`

**Parity/determinism:**  
 `CLI_READER_PARITY_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_TWO_RUN_IDENTITY_OK, PARITY_AB_BA_OK, JSON_CANONICAL_CHECK_OK, PREIMAGE_RECOMPUTE_OK, CLI_IMPLEMENTED_SET_OK.`

**Evidence discipline:**  
 `EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_PATHS_VALIDATED_OK.`

**Parity harness tokens (public CLI harness):**  
 `CLI_INSTALL_OK, CLI_HELP_OK, CLI_SHOWCOMPAT_PRESENT, CLI_SHOWCOMPAT_CANON_OK, CLI_AB_BA_PARITY_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_READER_EMITTER_PARITY_OK.`  
 (Parity‑harness roster is frozen in Governance/Epics; PF05 describes where these are proved.)

**Preview posture (Aux narrative preview):**  
 `CLI_PREVIEW_ENABLED_OK, CLI_PREVIEW_INDEXED_OK.`

---

## **17.8 Evidence (records-only; machine mirror; same-PR rule)**

CLI components share the core evidence discipline:

* List each CLI evidence artifact by title and path in Appendix D: Evidence Index.

* Mirror artifacts 1:1 in artifacts/evidence\_index.jsonl (record fields as per PF12 and §1.3).

* Ensure the machine mirror is canonical JSONL (UTF-8, ASCII-sorted keys, compact, one LF), rejects unknown keys, and includes a proof\_anchor to a co-located path\_proof file.

* Update the human Index and machine mirror in the same PR; CI fails on mismatch, non-canonical JSONL, unknown keys, or missing path-proofs.

Required artifacts for the CLI parity and serializer-coupling harness include:

* Parity harness artifacts

  * artifacts/cli/ab.json — canonical output for AB inputs (LF-terminated).

  * artifacts/cli/ba.json — canonical output for BA inputs (must be byte-identical to AB).

  * artifacts/cli/summary.json — canonical JSON summarizing attempted commands, sha256 of AB/BA, and an ab\_ba\_equal: true marker.

* Serializer and emitter guard artifacts (canonical homes; see §37.6)

  * artifacts/cli/guards/serializer\_grep\_guard.log — grep guard log proving there are no ad-hoc serializers on governed CLI public paths.

  * artifacts/cli/guards/emitter\_symbol\_proof.txt — emitter symbol proof snapshot for governed CLI handlers, including the optional aux-preview exemption.

* Canonical JSON policy and compare logs

  * audit/gates/canonical/json\_canonical\_check.log — canonical JSON checks for CLI and related artifacts.

  * audit/gates/canonical/json\_canon\_compare.log — canonical re-serialization compare for public bytes and parity harness outputs.

Copies of the guard artifacts under audit/gates/guards/\*\* may exist for internal audit workflows, but those paths are secondary. Mechanics treats artifacts/cli/guards/\*\* as the canonical homes for CLI serializer/emitter guards; indexing and mirror records must use those canonical paths as discovered\_physical\_path, consistent with §37.6 and §1.3.

---

## **17.9 Stateless JSON QA mode (informative)**

**Status:** Informative, non-gating  
 This section records a future mechanics requirement from HDE-Build Notes (Addendum 11\) for a no-DB, stateless JSON QA mode. It does not add any new acceptance gates for the current engine or CLI posture.

### **17.9.1 Background and scope**

HDE-Build Notes observes that, in pre-Glow environments:

* There is no app-level user model or user IDs.

* There are no persistent user-bound BodyGraphs in production.

* We must not create app-like user records in production ahead of Glow App integration.

* Many earlier QA flows assumed DB-backed users  
   (for example, `showcompat --user-a/--user-b --source=db`, `bg:resolve --source=vendor --upsert`),  
   which cannot run under these constraints.

Current mechanics in this guide assume DB-backed flows for:

* CLI commands that resolve or store BodyGraphs via DB (or vendor+DB).

* Evidence capture tied to DB posture and runtime environment.

This section does not change those flows. It describes the additional stateless capabilities that a future epic is expected to add so that engine math can be exercised purely via CLI plus files, without DB.

---

### **17.9.2 Required capability: no-DB JSON QA mode**

Addendum 11 in HDE-Build Notes introduces a future requirement for a **stateless JSON QA mode**, consisting of three mechanical capabilities:

#### **a) Stateless BodyGraph export**

A future CLI flow must:

* Accept only birth data or vendor JSON (no user IDs, no DB lookup).

* Call engine math directly, without DB.

* Emit a canonical JSON BodyGraph export containing:

  * Raw birth/event details needed to reconstruct the chart.

  * Full BodyGraph topology (centers, gates, channels, lines, profile, authority, definition, type).

  * Stable identifiers consistent with the domain catalogs (IDs only; no prose).

* Write canonical JSON governed by **HDE-Schemas and Artifacts**  
   (UTF-8, no BOM, ASCII-sorted keys, compact, exactly one LF, arrays-as-sets deduped then ASCII-sorted).

#### **b) Stateless compat export**

A future CLI flow must:

* Accept two BodyGraph JSON files *or* two birth tuples.

* Compute compat and Reader v1 envelopes directly, without DB.

* Write canonical JSON compat output and Reader envelopes under governed paths.

* Preserve determinism and AB↔BA parity using the same canonical serializer and comparator rules defined in this guide (§4/§5/§6).

#### **c) Stateless vendor-to-engine pipeline**

A future CLI-driven pipeline must support:

`birth → vendor fetch (dry-run) → BodyGraph JSON → compat + Reader JSON`

Each stage must:

* Be invokable via CLI.

* Write only JSON files and logs under governed paths.

* Perform **no DB writes**, unless an explicit upsert path is chosen (and that upsert remains clearly separated from stateless QA flows and governed by vendor/DB posture sections (§19/§20) and Governance).

Mechanics does **not** define specific command names, flags, or paths for these flows.  
 It records that when implemented, they must reuse the shared emitter, canonical serializer, comparators, and deterministic engine posture defined in this guide.

---

### **17.9.3 Single homes for schemas and flows**

This guide records the mechanical requirement only. Ownership remains:

* **HDE-Schemas and Artifacts** — JSON schemas and artifact catalogs for stateless BodyGraph, compat, and any run-bundle exports.

* **HDE-CLI-API-Vendor-Ref** — CLI command shapes and behavior for stateless flows.

* **Glow QA Guide** and **HDE Phased Epics** — QA plans and acceptance wiring for stateless QA mode.

Mechanics MUST NOT define concrete paths or JSON schemas for these artifacts; it references the owning documents by title only.

---

### **17.9.4 Normative status and gating**

Until the stateless JSON QA mode is implemented and drained into the relevant PF documents:

* **No acceptance token** may treat the presence or absence of stateless JSON QA artifacts as a gate.

* PF14’s normative mechanics remain those of the current **DB-backed** engine and CLI flows.

* QA plans that cannot rely on DB users SHOULD:

  * Call out “no user IDs / no DB users” as an environment constraint.

  * Use birth-based and vendor dry-run patterns described in HDE-Build Notes and the QA documents, while continuing to satisfy all existing determinism and evidence checks defined in this guide.

## 17.10 Interim no-user QA mode (pre-Glow prod)

**Status (normative).**  
 This section is **normative for pre-Glow production environments** where there is **no app-level user model** and **no persistent user-bound BodyGraph rows** configured in the database. It constrains how existing mechanics are exercised in Live QA. It does **not** change the long-term semantics of DB-backed flows, which will be re-opened in a future epic once the Glow App is integrated (see **HDE Phased Epics** and **Glow QA Guide** by title).

**Assumptions (pre-Glow prod).**

* No app-level user IDs exist in production.

* No persistent user-bound BodyGraphs exist in production.

* Mechanics and QA **MUST NOT** create app-like user records in production ahead of Glow App integration.

### 17.10.1 Compat & Reader (prod QA)

For Live QA in pre-Glow prod:

* `hdctl showcompat` **MUST** be exercised with **birth arguments only** (for example, `--birthdate-a/-b`, `--birthtime-a/-b`, `--location-a/-b`).

* `--user-a/--user-b` and `--source=db` **MUST NOT** be used in production QA flows while the app user model is absent.

* QA **MUST** continue to verify:

  * canonical JSON on stdout (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF),

  * AB↔BA identity using swapped birth tuples, and

  * Reader v1 envelopes via `--dump-reader`, with Reader↔CLI parity proven via the shared presenter/emitter (§4, §8, §18).

These checks reuse the existing determinism and canonicalization rules in this guide and do not add new transport bytes.

### 17.10.2 Aux narratives (prod QA)

For Aux preview in pre-Glow prod:

* `hdctl aux-preview` **MUST** consume compat JSON produced from **birth-based** `showcompat` runs as described in §17.10.1.

* QA **MUST NOT** rely on DB-backed users to exercise Aux; the Aux preview surface remains a **file-based consumer** of compat JSON in this mode.

### 17.10.3 BodyGraph resolver & vendor ingest (prod QA)

In pre-Glow prod, BodyGraph resolver and vendor ingest QA flows **MUST** respect the following additional constraints (in addition to §19 Vendor Ingest Pipeline and §22 SAFE Rails and Provider Gate):

* CLI `--user` arguments passed to `bg:resolve` **MUST** be treated as **ephemeral QA keys only** (for example, `qa_epic017_resolve1`, `qa_epic017_vendor1`) and **MUST NOT** be interpreted as real app user IDs.

* Under **rails CLOSED**, any `bg:resolve --source=vendor` invocation **MUST** return a typed refusal and **MUST NOT** perform outbound HTTP.

* Under **rails OPEN** in pre-Glow prod, QA **MAY** run:

  * `bg:resolve` DB/auto **stub** checks (no real DB rows), and

  * `bg:resolve --source=vendor --dry-run` to exercise vendor shaping and ingest metadata **without writing DB rows**.

* `bg:resolve --source=vendor --upsert` **MUST NOT** be invoked in production until an app-level user model is live and a future epic re-opens user-bound DB coverage via **HDE Phased Epics** and **Glow QA Guide**.

These constraints are environment-specific; they do not change the long-term semantics of vendor upsert flows in dev or in future epics with a live app user model.

### 17.10.4 Evidence skeleton for CLI QA

For Live QA sessions in pre-Glow prod:

* Mechanics **MUST** snapshot the **Human Evidence Index** and **Machine Mirror** **before and after** CLI QA runs that exercise `showcompat`, `aux-preview`, or `bg:resolve` in this mode.

* Any mutation of governed evidence artifacts (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, or governed `*.path_proof.txt`) during such QA runs **MUST** be treated as a defect or unexpected side effect.

* CLI QA flows in this mode **MUST NOT** write governed evidence artifacts directly; they **only consume** the evidence skeleton defined in §1.3, §25, and §37, leaving governed paths unchanged.

### 17.10.5 Forward plan (routing only)

* Once the Glow App and user model are integrated, a future epic recorded in **HDE Phased Epics** and governed by the **Glow QA Guide** will:

  * use real app user IDs to exercise DB-backed `showcompat` and `bg:resolve --source=vendor --upsert` in prod or stage, and

  * close out any acceptance tokens that currently depend on DB-backed user flows (routing by title to **HDE-Governance** and **HDE Phased Epics**).

* Until that epic is live, QA requirements that assume “existing users in prod” **MUST** be treated as **blocked by environment** and satisfied instead using the no-user QA mode described in this section.

## 17.11 Admin QA bundle surfaces (full product payload)

**Status (normative, admin-only).**  
 This section defines an **admin-only bundle** and its CLI/HTTP consumers for pre-Glow QA. The bundle is a single canonical JSON object that combines BodyGraph JSON, compat results, and Aux narratives for a match. It is intended for **internal operators and PO only** and is not a public Reader or app surface. Reader v1’s public covenant (bands-only, numeric-free, six-key envelope) and existing app-facing contracts remain unchanged and continue to be governed by HDE-CLI-API-Vendor-Ref, HDE-Math-Spec, and Glow QA Guide by title.

### **17.11.1 Admin bundle builder (internal module)**

Mechanics defines an internal **admin bundle builder** that:

* Accepts a canonical pair input in the same compat input space as the Compatibility Engine (§7.2) and the CLI `showcompat` harness: two parties (IDs, BodyGraphs, or births as permitted by the existing compat contract) plus viewer preferences (top category and weights across the closed Magic-10 set).

* Uses the existing BodyGraph resolver mechanics (titles-only to the BodyGraph resolver sections of this guide and to HDE-Schemas & Artifacts / HDE-Math-Spec) to obtain **canonical BodyGraph JSON** for each party, as already required for `bg:resolve` and related flows.

* Calls the internal compat math (titles-only to Category Framework and Compatibility Engine) to compute the per-category compat result over the closed Magic-10 set, at minimum:

  * category identity,

  * integer score `0..100`,

  * band (Cool, Open, Warm, Glow), and

  * narrative keys `{personal_key, shared_key}` consistent with the main compat contract.

* Calls the Aux/Narratives system (titles-only to Narratives Guide and HDE Narrative Deliverables) to obtain **three narratives per match**:

  * a private A→B narrative,

  * a private B→A narrative, and

  * a shared narrative.

* Assembles a single in-memory **admin bundle** object with at least the following **top-level keys** (names are pinned here; detailed schemas remain in HDE-Schemas & Artifacts):

  * `a_bodygraph` — canonical BodyGraph JSON for person A, as produced by the resolvers.

  * `b_bodygraph` — canonical BodyGraph JSON for person B, as produced by the resolvers.

  * `compat` — the canonical compat JSON for the pair (categories in frozen Magic-10 order), where each category entry carries `{id, score, band, personal_key, shared_key}` and existing compat meta as defined by math and schemas.

  * `narratives` — an array of **exactly three** Aux narrative compositions for this match (A→B, B→A, shared). Each narrative entry includes, at minimum, the composition identifier and pack SHA (or equivalent identity) plus the narrative text; the exact narrative payload schema remains single-homed in the Narratives documents.

  * `meta` — build and environment metadata, including at minimum the engine identity (for example, `engine_tag`, `release_id`), invocation identity (for example, `invocation_tag` or equivalent), and a names-only description of the bundle source and rails posture (for example, whether the bundle was built locally or via a prod route, and whether SAFE rails were closed or open). Detailed field schemas for `meta` remain single-homed in HDE-Schemas & Artifacts and HDE-Governance.

The admin bundle builder is **pure mechanics**: it calls existing resolvers, compat, and Aux engines; it does not perform I/O, does not serve HTTP, and does not define transport or CLI flags. Its output is serialized only via the canonical serializer (§4 / §10.1) when consumed by CLI or HTTP surfaces:

* UTF-8, no BOM

* ASCII-sorted keys

* compact separators

* exactly one trailing line feed

* arrays-as-sets deduped and ASCII-sorted

AB↔BA parity and two-run identity **MUST** hold for the admin bundle under determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

All scores, BodyGraph JSON, narrative keys, and narrative text carried in this bundle are **admin/internal only**. They must never be exposed as public Reader or app payloads and must not alter the public Reader contracts described elsewhere by title.

### 17.11.2 CLI admin bundle experience (any terminal → Railway prod)

Mechanics requires that the CLI provide a **repeatable admin bundle experience** that can be run from any terminal capable of reaching the production Engine, subject to the usual secrets and rails posture governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide (titles-only):

* The CLI admin-bundle flow **MUST** use the admin bundle builder described in §17.11.1 as its source of truth. It may be implemented either as:

  * a dedicated aggregator command, or

  * a documented harness/composition of existing commands (`bg:resolve`, `showcompat`, Aux preview), as long as the composition is mechanically defined and stable.

* The CLI admin-bundle flow **MUST**:

  * accept a canonical pair input (fixture, births, or internal IDs consistent with existing compat/BodyGraph contracts),

  * obtain the bundle by calling the Engine (directly or via the admin HTTP route described in §17.11.3), and

  * emit the bundle as canonical JSON on stdout or to a single bundle file, subject to:

    * UTF-8, no BOM,

    * ASCII-sorted keys,

    * compact separators,

    * exactly one trailing LF, and

    * arrays-as-sets deduped and ASCII-sorted.

* The flow **MUST** be reproducible from:

  * a Codespaces image used for HDE QA, and

  * at least one “clean” local environment matching supported Python versions,

* using the same documented entrypoints described in the CLI sections of this guide and in HDE-CLI-API-Vendor-Ref.

* Rails and env posture for this flow (SAFE rails, vendor behavior, secrets) remain governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide. PF14 requires that the CLI admin-bundle flow:

  * respect SAFE rails and determinism pins (`SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, `TZ`) for any bundle generation used as evidence, and

  * not bypass the allow-listed presenter/emitter, canonical serializer, or existing CLI parity and serializer guards (§4, §16, §17.3, §18).

Evidence for the CLI admin bundle experience (for example, bundle JSON artifacts and canonical-compare logs) must be captured and indexed under the existing evidence skeleton rules (§1.3, §25, §37); token names and QA acceptance rosters remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

### 17.11.3 HTTP admin bundle route (GUI consumer)

Mechanics also requires an internal **HTTP admin bundle route** to serve the same admin bundle to a minimal Admin GUI:

* The route is an **internal admin/QA surface**, not a public user route:

  * it is not A7-eligible,

  * it is not a Reader v1 success route, and

  * it is protected by whatever authentication and authorization posture is defined in Governance/Infrastructure (titles-only).

* The route:

  * accepts a canonical pair input (fixture, births, or internal IDs consistent with existing BodyGraph and compat mechanics),

  * calls the admin bundle builder (§17.11.1) to construct the full product payload bundle, and

  * returns **JSON only**, with no HTML, using the canonical serializer (§4 / §10.1) and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`).

* The Admin GUI (which may live in a separate repo) is expected to:

  * call this route against the same production Engine on Railway that the Glow App will later use, and

  * render BodyGraphs, compat categories with numeric scores and bands, and three narratives (A→B, B→A, shared) from the returned bundle.

PF14 does not define the HTTP route name, auth model, or HTML/UX; those live in HDE-CLI-API-Vendor-Ref, Governance, and any Admin-UI epic records by title. PF14 only requires that such an admin bundle route exist, be wired to the admin bundle builder, use canonical JSON, and behave as an internal admin-only surface.

### 17.11.4 Posture vs Reader/App and evidence (routing only)

The admin bundle surfaces (builder, CLI experience, HTTP route) are strictly **admin QA** and **operator** tools:

* They may expose BodyGraph JSON, per-category scores, bands, and narrative keys/text for internal use.

* They **MUST NOT** be used directly as public app routes or as replacements for Reader v1 or Aux public contracts. App integration continues to go through the Reader/Aux paths governed in HDE-Math-Spec, HDE-CLI-API-Vendor-Ref, Narratives Guide, and Glow QA Guide.

* All admin bundle captures and parity checks (for example, CLI vs HTTP bundle equality for the same inputs) must follow the existing evidence skeleton rules for canonical JSON, AB↔BA and two-run identity, and Index/Mirror parity (§1.3, §25, §37). Any new tokens or epic-level acceptance criteria for admin bundle flows are defined in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics by title; PF14 does not define new token names here.

### **17.11.5 Authentication, authorization, and logging (admin surfaces)**

**Status (normative, pre-Glow).**  
 The admin bundle surfaces defined in §17.11 (builder, CLI experience, HTTP route) are **security-sensitive admin/QA tools**. Mechanics requires that they be protected by real authentication and authorization, that successful calls be logged for audit, and that credentials be rotatable and revocable without code changes. Exact credential schemes and policies remain single-homed in HDE-Governance, Glow QA Guide, and Glow Infrastructure by title.

#### **17.11.5.1 Authentication and authorization (no open admin endpoints)**

Mechanics requires that:

* The CLI admin-bundle flow (§17.11.2) and the HTTP admin bundle route (§17.11.3) **MUST NOT** be callable without an admin credential. An unauthenticated request **MUST NOT** be able to obtain the full admin bundle.

* The admin credential (for example, a token or equivalent secret) **MUST**:

  * be stored as a secret under the infrastructure and governance policies described by HDE-Governance and Glow Infrastructure (for example, Railway secrets), not checked into the repo, and

  * be required on every admin bundle call (CLI and HTTP), using a transport mechanism and header/field semantics pinned in HDE-CLI-API-Vendor-Ref and HDE-Governance.

* The same underlying authentication and authorization posture **MUST** apply to both admin surfaces:

  * CLI and Admin GUI both act as clients presenting the admin credential to the Engine, and

  * the Engine enforces that only authenticated and authorized admin callers may access the admin bundle route or equivalent CLI path.

Mechanics does not pick specific header names or token formats; it requires that admin bundle surfaces are never “open admin endpoints” in production and routes the detailed auth model to HDE-Governance, Glow Infrastructure, Glow QA Guide, and HDE-CLI-API-Vendor-Ref.

#### **17.11.5.2 Logging and audit of admin bundle calls**

Mechanics further requires that every **successful** admin bundle call (CLI or HTTP):

* be logged with, at minimum:

  * a timestamp,

  * a caller identity or account (for example, operator username, service account, or equivalent),

  * a high-level description of the input type (for example, “birth-based pair” vs “user-id pair” once user IDs exist, without logging raw birth details or other PII beyond what Governance allows), and

  * a correlation identifier that can be used to trace the call across logs.

* produce logs that are treated as **operations logs** and governed by the logging, retention, and PII rules in HDE-Governance and Glow QA Guide. Mechanics does not restate those policies; it assumes that any fields logged here comply with them.

Admin bundle logs must not capture secrets (credentials, tokens) or raw config values; they only record high-level audit information necessary for operational tracing.

#### **17.11.5.3 Credential rotation and revocation**

Admin credentials used for CLI and HTTP admin bundle surfaces **MUST** be:

* **Rotatable** without code changes:

  * credentials are loaded from environment or configuration governed by HDE-Governance and Glow Infrastructure, and

  * rotation of the secret value (for example, updating a Railway secret) does not require code deploys.

* **Revocable**:

  * removing or changing the admin credential in the secret store MUST immediately prevent old credentials from successfully calling the admin bundle surfaces, and

  * tests and QA harnesses for admin surfaces MUST assume that credentials can change between runs and MUST NOT bake secrets into test fixtures.

Mechanics does not define acceptance tokens for authentication, logging, or rotation; token names and QA playbooks (for example, admin-bundle auth required, CLI/HTTP parity, and “no open admin endpoints”) remain single-homed in HDE-Governance, Glow QA Guide, HDE-Build Checklist, and HDE Phased Epics by title. PF14 records the mechanical requirement that admin bundle surfaces are authenticated, logged, and backed by rotatable, revocable credentials in pre-Glow.

## **17.12 CLI as admin product surface (pre-Glow)**

**Status (normative, pre-Glow).**  
 In the pre-Glow era, the canonical CLI (for example, `hdctl` or its module-run equivalent, as defined in HDE-CLI-API-Vendor-Ref) is a **required admin-facing product surface**, not just a dev/QA tool. A build that cannot be exercised via this CLI from a terminal that can reach the production Engine on Railway fails Mechanics requirements for pre-Glow “product usable by humans” posture.

### **17.12.1 Terminal scope (any shell → Railway prod)**

Mechanics requires that:

* The CLI be runnable from **any shell** that can reach the production Engine on Railway (and, where applicable, its DB), subject to the secrets and rails posture governed by HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide (titles-only), not just from GitHub Codespaces.

* The same CLI mechanics defined in §16 and §17 (streams/exits, determinism, canonical JSON, parity) apply regardless of where the CLI is run (Codespaces, local machine, or other operator shell), provided environment pins and rails policy are satisfied.

* The CLI continue to respect all pre-Glow constraints recorded elsewhere in this guide and in Governance:

  * `--user` remains an ephemeral QA key in pre-Glow prod; it is not bound to an app-level user model.

  * `bg:resolve --source=vendor --upsert` **MUST NOT** be used in prod until a future epic explicitly re-opens user-bound upsert flows.

  * Any flows that open rails or reach vendor APIs must follow the SAFE rails and vendor posture defined in HDE-Governance, HDE-CLI-API-Vendor-Ref, Infrastructure, and Glow QA Guide.

This section does not add new commands or flags; it binds the existing CLI mechanics to a stronger product requirement: terminal CLI access to the Engine is part of the pre-Glow product surface.

### **17.12.2 Full product payload via CLI (within existing rails)**

Mechanics further requires that, in pre-Glow:

* The combination of CLI subcommands and harnesses defined in this guide and in HDE-CLI-API-Vendor-Ref be **sufficient to obtain the full product payload** for a match, consistent with:

  * Compatibility engine math and banding (titles-only to HDE-Math-Spec and §7.2).

  * BodyGraph resolver mechanics (titles-only to the BodyGraph resolver sections of this guide and to HDE-Schemas & Artifacts).

  * Aux/Narratives behavior (titles-only to Narratives Guide and HDE Narrative Deliverables).

* For a given pair input (fixture, births, or internal IDs allowed by existing contracts), an operator using only CLI subcommands (direct commands and/or a documented harness) can obtain, as structured output:

  * per-person BodyGraph JSON,

  * compat results with bands and numeric scores over the closed Magic-10 set, and

  * three narratives per match (two private, one shared), as already wired via the admin bundle builder (§17.11.1) and related Aux mechanics.

* These flows **MUST** operate within the pre-Glow rails posture described in §17.9, §17.10, §19.1, and in Governance/Infrastructure:

  * When no user model exists, they rely on birth-based and dry-run vendor flows; they do not create app-like user records in prod.

  * Any DB-writing flows remain governed by SAFE rails defaults and explicit rails-open windows as defined in Governance and Infrastructure; the requirement to support terminal CLI access does not relax those policies.

Mechanics treats the admin bundle surfaces in §17.11 as the preferred way to structure the full product payload for CLI, but does not require a single new command name. Whether the full payload is retrieved via a dedicated aggregator command or a documented composition of existing commands, the CLI must be able to produce the full product payload from a terminal in a way that satisfies the determinism, canonical JSON, and evidence discipline already defined in §4, §16, §17, §18, §25, and §37.

### **17.12.3 Evidence and planning (routing only)**

* Evidence that terminal CLI access is a functioning product surface (for example, bundle JSON produced from a non-Codespaces shell hitting Railway prod, plus canonical-compare logs) must be captured and indexed under the existing evidence skeleton rules (§1.3, §25, §37). Mechanics does not define new artifact names or paths here; it routes titles and token semantics to HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics.

* Epic-level planning and acceptance tokens for “CLI terminal access to full product payload” remain single-homed in HDE-Governance, HDE-Build Checklist, Glow QA Guide, and HDE Phased Epics. PF14 records the mechanical requirement that the CLI is a required admin product surface in pre-Glow and that its existing mechanics must support full product payload flows from any eligible terminal.

  # 18\) CLI Serializer Coupling \[Required-Now\]

**Scope.** Force all CLI public bytes through the **same allow-listed presenter/emitter** entrypoint used by Reader. Tests must not bypass the unified entrypoint.

## 18.1 Policy (normative)

* **Single entrypoint.** CLI **MUST** route every public body through the shared presenter/emitter symbol (see §10.2).  
* **Canonical rules apply.** §4/§10.1 canonicalization (UTF-8; sorted keys; compact; one LF; arrays-as-sets) **MUST** hold for CLI stdout.  
* **Surface parity.**  
  * `/api/compat/v1`: CLI stdout is **byte-identical** to the Reader 200 body.  
  * `/api/sample/v1`: CLI stdout uses the **same deterministic selection \+ ordering** as Reader.

  ## 18.2 Prohibited (hard fail)

* Any ad-hoc JSON on public paths: **no** `json.dumps(`, **no** `jsonify(`, **no** templating, **no** manual string building, **no** pretty/indented output.

  ## 18.3 Guards (CI)

* **Symbol allow-list.** Maintain a code/CI allow-list of presenter/emitter symbols; only these may serialize public bytes.  
* **Grep-guard.** CI **fails** on public paths if ad-hoc serialization is detected (regex for `\bjson\.dumps\(` and known alternates).

  ## 18.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **Coupling:** `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`.  
* **Surface parity:** `CLI_READER_EMITTER_PARITY_OK` (compat), ordering proof present (sample).  
* **Determinism:** `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.  
* **Evidence discipline:** `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

  ## **18.5 Evidence (records-only; machine mirror; same-PR rule)**

CLI serializer coupling evidence must demonstrate:

* AB↔BA and two-run identity for compat bytes under the shared presenter/emitter,

* canonical JSON on CLI stdout for governed commands, and

* that governed CLI handlers use the allow-listed emitter and do not call ad-hoc JSON serializers.

List evidence artifacts by title and path in Appendix D and mirror them 1:1 in artifacts/evidence\_index.jsonl (record fields as per §1.3). The machine mirror is canonical JSONL (UTF-8, ASCII-sorted keys, compact, one LF), rejects unknown keys, and each record includes a proof\_anchor to a co-located path\_proof file.

Required artifacts for CLI serializer coupling:

* CLI AB/BA parity artifacts (parity harness)

  * artifacts/cli/ab.json — canonical output for AB inputs (LF-terminated).

  * artifacts/cli/ba.json — canonical output for BA inputs (must be byte-identical to AB).

  * artifacts/cli/summary.json — canonical JSON with attempted commands, sha256 of ab.json and ba.json, and ab\_ba\_equal: true.

* Serializer and emitter guards (see §37.6 for guard tool behavior and roles)

  * artifacts/cli/guards/serializer\_grep\_guard.log — grep guard report proving no ad-hoc serializers on governed CLI public paths.

  * artifacts/cli/guards/emitter\_symbol\_proof.txt — emitter symbol proof listing governed handlers and their allow-listed emitter symbols (with aux-preview explicitly exempt when it lists none).

* Canonical JSON policy and compare logs

  * audit/gates/canonical/json\_canonical\_check.log — canonical JSON policy checks for CLI and evidence output.

  * audit/gates/canonical/json\_canon\_compare.log — canonical re-serialization compares for CLI parity and serializer coupling.

If audit/gates/guards/\*\* copies of the guard artifacts are present for internal audit workflows, they are secondary only. The artifacts/cli/guards/\*\* paths are the canonical locations for serializer/emitter guards; the Evidence Index and Machine Mirror must use those canonical paths as discovered\_physical\_path.

## 18.6 Routing (titles-only)

* Canonical serializer & unified entrypoint: **§4** and **§10.2**.  
* Public payload/transport: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.  
* Domain catalogs & prefs schema: **HDE-Schemas and Artifacts** / **HDE-Math-Spec**.  
  ---

  


  # 19\) Vendor Ingest Pipeline — source policy & proofs (normative)

## **19.1 Policy (normative)**

**Policy (env-aware)**

* **Prod.** Source of truth is the database. Vendor APIs run only on explicit triggers or scheduled refresh; never inline on the request path.

* **Pre-Glow prod (no users).** When there is no app-level user model integrated with the HD Engine and no persistent user-bound BodyGraph rows configured in production:

  * Mechanics and QA **MUST NOT** create app-like user records in prod via CLI or vendor ingest.

  * `bg:resolve --source=vendor --upsert` **MUST NOT** be invoked in prod; QA and ops flows in this environment MAY use only DB/auto stub behavior and vendor dry-run semantics as described below.

* **Dev.** Direct vendor calls are allowed; on success, ingest MUST upsert the BodyGraph to DB for repeatability.

* **SAFE rails.** SAFE rails apply in all environments; rails posture and acceptance tokens are owned by **HDE-Governance** (titles-only).

**BodyGraph I/O seam (normative).**

Mechanics treats BodyGraph resolution and ingest as a **sanctioned I/O seam** that is distinct from deterministic core compute:

* **Canonical seam location (implementation boundary).** BodyGraph vendor and DB I/O is permitted only within the BodyGraph seam (currently implemented under `engine/bodygraph/` in this repo). This seam is not part of the deterministic Engine Core or sampler core.

* **What may occur in the seam.** Code inside the BodyGraph seam MAY perform:

  * network I/O to vendor services (through a vendor client abstraction), and

  * DB reads/writes for BodyGraph storage (through a DB access abstraction).

* **Rails requirements for all I/O.** Any network or DB I/O in the BodyGraph seam MUST:

  * respect SAFE\_MODE and ALLOW\_NETWORK rails (no vendor calls when network rails are closed; fail-closed refusals when misconfigured),

  * use a small, well-defined set of seam abstractions (for example, vendor client and DBAccess-like components), and

  * keep logs and artifacts secret-free (keys-only posture; no credentials and no vendor payload bodies in governed artifacts).

* **Purity preserved elsewhere.** Deterministic decisions (eligibility, banding, compat math, narrative key selection, canonical JSON emission) MUST remain in the pure compute modules (core/sampler/compat/presenter/runtime) and MUST NOT be implemented inside the BodyGraph seam. The BodyGraph seam orchestrates I/O and normalization around those pure decisions.

This subsection does not redefine transport bytes, retry policy, or token semantics; it records the mechanical I/O boundary so audits and tests can enforce “no network/DB I/O leaks into core compute” while allowing BodyGraph resolution and ingest to operate under explicit rails.

**Per-call selection (explicit)**

* Source is chosen **per call** on operator surfaces (CLI flag / ops param); there are no engine “modes.”

* Any unknown `ENGINE_*` env **MUST** fail fast with a typed error (no vendor I/O).

* When rails are closed, any request that sets `source=vendor` **MUST** return a typed refusal and **MUST NOT** perform outbound HTTP.

* In **pre-Glow prod QA flows**, CLI `--user` values passed to `bg:resolve` **MUST** be treated as **ephemeral QA keys only** and **MUST NOT** be bound to real app user IDs; DB behavior remains stub-only until the Glow App is integrated.

* When rails are **OPEN** in pre-Glow prod QA flows:

  * `bg:resolve` DB/auto MAY be exercised in **stub** mode (no real DB rows), and

  * `bg:resolve --source=vendor --dry-run` MAY perform a single vendor call that returns ingest metadata and **MUST NOT** write DB rows.

Routing and token semantics for per-call selection are owned by **HDE-Governance** and **HDE-CLI-API-Vendor-Ref** (titles-only).

**Evidence (records-only)**

* `artifacts/bodygraph/source_selection.snapshot.json` capturing at least:

  * `app_env`

  * `attempted` (requested source)

  * `selected` (actual source used)

  * `reason` (closed enum explaining selection/fallback)

  * `upserted` (boolean indicating DB upsert)

* Canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing `\n`); unknown keys are rejected.

**Source invariance (single presenter/emitter)**

For the same normalized inputs, DB-sourced and vendor-sourced bodies **MUST** be byte-identical when emitted via the shared presenter/emitter.

Proofs live under `artifacts/bodygraph/source_invariance/` as at least:

* `ab.json` — DB body (reference side)

* `ba.json` — vendor body for the same inputs

* `summary.json` — summary (attempts, `sha256` digests, `ab_ba_equal: true` on success)

**Live vendor transport proofs (open-rails QA vs offline tests).**

For epics whose D-goals or QA acceptance explicitly require **live vendor activity** (for example, “prove that at least one flow hits the live vendor under open rails”), Mechanics adds the following mechanical requirements on top of the policy and evidence in this section:

* **Separation of offline ingest tests vs live vendor tests (normative).**

  * Offline ingest tests (for example, unit/integration tests, dry-run pipelines, and source invariance proofs that never open vendor rails) are **not sufficient** on their own to satisfy “live vendor activity” D-goals. They remain necessary for correctness and invariance, but count as **offline evidence only**.

  * A **live vendor transport proof** requires at least one run in which the Engine/Reader or CLI:

    * executes under **open rails** (for example, `ALLOW_NETWORK=1` with SAFE rails posture consistent with Governance and Infrastructure), and

    * actually sends a request from the Engine/Reader/CLI surface to a vendor endpoint, with the transport captured as governed evidence.

* **Required elements of a live vendor transport proof (mechanics only).**

   For any epic that claims live vendor coverage via this pipeline, Mechanics requires at least one governed evidence artifact (names and schemas single-homed in HDE-Schemas & Artifacts and Glow QA Guide) that records, at minimum:

  * **Rails snapshot at call time** — a names-only env log for the live-vendor step (for example, a D0/Dn env snapshot) including at least `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, and `TZ`, so that auditors can see that the vendor call actually ran under open rails and determinism pins.

  * **Vendor endpoint and method** — the vendor **hostname**, **scheme**, and **path** (for example, `https://<vendor_host>/<path>` or equivalent) and the **HTTP method** used (`GET`, `POST`, etc.), with any secrets (API keys, auth tokens) removed or redacted per Governance.

  * **Request/response status and headers** — a headers-only or structured log that captures:

    * the HTTP status code returned by the vendor,

    * selected response headers (for example, `Date`, `Content-Type`, and vendor-specific rate-limit headers where allowed), and

    * any vendor error codes or reason phrases that are needed to interpret the result,

  * again with secrets and PII stripped or redacted according to Governance and Glow QA Guide.

  * **Body visibility (names-only).** Bodies **MUST NOT** be logged verbatim for vendor responses; when bodies are needed for debugging or QA, Mechanics requires that they be down-sampled or transformed into names-only or bounded summaries consistent with the logging posture in this guide and Governance. Raw vendor payloads and PII must not appear in governed live-vendor proof artifacts.

* The exact artifact names, JSON shapes, and token mappings for these proofs are defined in **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Governance**, and **HDE-Build Checklist** by title; this section records that at least one such artifact **MUST** exist for any epic that claims live vendor coverage through this pipeline.

* **Surfaces and harnesses (CLI vs HTTP).**

  * A live vendor transport proof may be obtained via either:

    * a **CLI surface** that drives vendor ingest and records the evidence above, or

    * an **HTTP surface** (for example, a Reader or internal admin route) that drives vendor ingest and is exercised by a QA harness.

  * Mechanics requires that each epic’s QA plan declare **which surface(s)** are used for live vendor proofs (CLI and/or HTTP) and that the corresponding harness:

    * uses the same Vendor Ingest Pipeline mechanics and source-selection rules defined in this section,

    * runs under clearly logged rails (closed vs open, SAFE rails posture), and

    * writes the live-vendor proof artifacts as governed evidence under the existing evidence skeleton (Index/Mirror, path-proofs, same-PR rule), using **titles-only** routing for schemas and directories.

  * Pre-Glow constraints in §19.1 (no app-like users in prod, upsert disabled in pre-Glow prod, dry-run only in certain flows) remain fully in force; live vendor proofs **must respect** those environment rules and may use dry-run or non-upsert surfaces where required.

* **Routing (titles-only).**

  * The **names and schemas** for live vendor transport evidence families, their locations under `artifacts/**` or `audit/**`, and the **acceptance tokens** (for example, any “live vendor transport” or “open rails env” tokens) remain single-homed in:

    * **Glow QA Guide** (QA plans and token evidence requirements),

    * **HDE-Phased Epics** (epic-specific D-goals and acceptance),

    * **HDE-Build Checklist** (build and QA gates), and

    * **HDE-Schemas & Artifacts** (artifact schemas and catalog entries).

  * PF14 records that, when an epic requires live vendor activity, Mechanics expects at least one **open-rails vendor call** to be exercised from an Engine/Reader/CLI surface using this pipeline, with the transport-level evidence and rails snapshot captured as governed artifacts under the shared evidence skeleton and indexed in the same PR as other ingest evidence.

**Acceptance (titles-only)**

* `BG_SOURCE_SELECTION_OK`

* `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`

* `BG_DEV_DIRECT_CALLS_UPSERT_OK`

* `BG_SOURCE_INVARIANCE_OK`

Index/mirror parity uses the existing index tokens:  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`.

Routing for artifact schemas and indexing lives in **HDE-Schemas & Artifacts**; policy and tokens live in **HDE-Governance**.

---

## 19.2 Refresh, TTL & SWR (out‑of‑band; normative)

**Purpose.** Pin the invariants for the BodyGraph refresh worker (EPIC‑011), its policy, and the governed refresh policy snapshot. Mechanics, ADR values, and detailed schema live in the ADR, Build Notes, and HDE‑Schemas & Artifacts; this section states the mechanical invariants only.

#### **Guards (no inline vendor calls)**

A refresh worker MUST:

* Run **out‑of‑band**, off the hot Reader path; it MUST NOT perform inline vendor calls for request‑time reads.

* Respect all four guard classes:

  * **TTL**: when data becomes stale.

  * **SWR (stale‑while‑revalidate)**: when stale data may be served while a refresh runs.

  * **Rate‑limit**: how often refresh attempts may be made.

  * **Circuit‑breaker thresholds and cooldown**: behavior under sustained error conditions.

  #### **Policy snapshot (v1, titles‑only)**

The refresh policy is captured in the governed snapshot artifact:

* `artifacts/bodygraph/refresh_policy.snapshot.json`

HDE‑Schemas & Artifacts owns the path and JSON schema; PF14 references it by title only.

The snapshot uses a **v1 nested schema** pinned by ADR and tests:

* Top‑level TTL/SWR fields (for example, `ttl_s`, `swr_s`).

* Nested objects:

  * `rate_limit.{requests_per_window, window_s}`

  * `circuit_breaker.{fail_threshold, window_s, cooldown_s}`

A `sample_counts` block is attached to a copy of the policy, recording counters such as:

* `refresh_attempts`

* `refresh_successes`

* `refresh_failures`

* `breaker_tripped`

* `rate_limit_hits`

These values are enforced by governed evidence tests.

#### **Worker alignment rule (POLICY ↔ snapshot)**

The refresh worker implementation in `scripts/bodygraph/run_refresh_worker.py` MUST:

* Use a `POLICY` constant whose structure matches the v1 nested schema described above.

* Serialize that structure into `refresh_policy.snapshot.json` (plus `sample_counts`) using canonical JSON (UTF‑8, sorted keys, compact, exactly one LF).

The worker MUST NOT reintroduce the legacy flat layout (`rate_limit: 60`, `cb.{…}`) that predates the v1 schema. Any such regression would overwrite the governed snapshot with a schema that no longer matches the ADR and MUST be treated as out‑of‑policy.

Any future change to TTL/SWR, rate‑limit, or circuit‑breaker thresholds MUST:

1. Update the ADR and snapshot schema (HDE‑Mechanics, HDE‑CLI‑API‑Vendor‑Ref, HDE‑Build Notes) so they all describe the same v1‑compatible policy.

2. Update the refresh worker’s `POLICY` constant and its usages to match the updated schema and values.

Guard tests (for example `test_refresh_policy_snapshot_matches_adr`) MUST remain green; they enforce that the emitted snapshot matches the ADR‑pinned policy and that the worker reads from the same nested fields it writes.

#### **Determinism and environment**

The refresh worker runs under the same determinism pins and SAFE‑rails posture as other EPIC‑011 jobs:

* Determinism: `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* SAFE rails and vendor shaping policy remain governed by HDE‑Governance and HDE‑CLI‑API‑Vendor‑Ref (titles‑only).

  ---

  # 20\) Persistence Layer (DB posture, partition & bridge) \[Required‑Now\]

**Scope (normative).** Database mechanics for schema identity, runtime posture, partition stance, and bridge parity. Artifact schemas and indexing live in HDE‑Schemas & Artifacts; governance tokens live in HDE‑Governance and the Build Notes. PF14 owns the mechanics that produce and prove the posture.

## 20.1 DB posture mechanics (build‑time identity)

**Objective.** Capture the runtime DB schema, roles/grants, and boundary view posture in a deterministic way.

Mechanics MUST drive a posture harness that produces at least:

* `artifacts/db/ddl_fingerprint.json`

  * Normalized DDL snapshot of the runtime schema with stable ordering.

* `artifacts/db/grants.txt`

  * Baseline roles/grants listing.

* `artifacts/db/check_schema.txt`

  * Schema/search\_path echo and verification.

* `artifacts/db/check_constraints.txt`

  * Constraint checks (including FK, uniqueness, and any invariants called out in canon).

* `boundary_view.readonly.proof`

  * Proof artifact (path named in HDE‑Schemas & Artifacts) that the boundary view is read‑only and does not permit writes outside the HDE schema.

Schema details for these artifacts live in HDE‑Schemas & Artifacts; PF14 requires only that the mechanics harness drive them.

All posture captures MUST:

* Run with determinism pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Produce canonical JSON/text where applicable (UTF‑8; sorted keys; compact; exactly one trailing LF).

* Remain secret‑free; logs and artifacts contain no credentials.

  ## 20.2 Partition mechanics (EPIC‑011)

**Objective.** Enforce EPIC‑011’s non‑deferred partition stance under standard artifact paths.

The partition harness MUST produce:

* `artifacts/db/partition/partition_plan.txt`

  * Planned partition layout for HDE tables in scope.

* `artifacts/db/partition/partition_verify.log`

  * Verification output showing that the live DB matches the plan.

For EPIC‑011 there is **no** “defer partition” token: both a partition plan and verify log are required. Semantics of `PARTITION_PLAN_OK` remain defined in Governance/infra docs; PF14 owns the mechanics that generate these artifacts.

## 20.3 Bridge parity mechanics

**Objective.** Prove parity between direct DB reads and bridge‑mediated reads and capture env connectivity posture.

Mechanics MUST:

* Drive a parity harness that emits (paths by title only):

  * `artifacts/bodygraph/vendor_upsert.<alias>.json` — vendor upsert transcript for a chosen alias.

  * `artifacts/bodygraph/db_resolve.<alias>.json` — DB resolve transcript for the same alias.

  * `artifacts/presenter/json_canon_compare.log` — canonical JSON compare proving structural equality of the two bodies.

* Ensure that, in the same change window as parity captures, an env connectivity snapshot is produced:

  * `artifacts/runtime/env_connectivity.snapshot.json` — dev‑only, names‑only snapshot showing how DB connectivity was resolved (schema in HDE‑Schemas & Artifacts).

Bridge parity and env connectivity artifacts are indexed via HDE‑Schemas & Artifacts; PF14 requires only that the mechanics jobs produce them.

**Acceptance impact.** No new tokens. This section makes explicit the mechanics expected by existing posture/partition/bridge tokens (`DB_SCHEMA_FINGERPRINT_OK`, `DB_ROLE_OK`, `PARTITION_PLAN_OK`, `DB_CONN_ENV_OK`, etc.), which remain defined in HDE‑Governance and infra docs.

---

# 21\) BodyGraph refresh worker (dev‑only; policy‑aligned) \[Required‑Now\]

**Role.** `scripts/bodygraph/run_refresh_worker.py` is a dev‑only worker that refreshes BodyGraphs according to a governed policy. It is not wired into CI; policy and schema are governed by HDE‑Build Notes (ADR/Addenda 44–45) and HDE‑Schemas & Artifacts (snapshot schema).

## 21.1 Policy alignment (v1 schema)

The worker uses a `POLICY` dict whose structure and values MUST match the ADR and the governed `refresh_policy.snapshot.json` v1 schema:

* `schema` — `"v1"`.

* `ttl_s` / `swr_s` — time‑to‑live and stale‑while‑revalidate windows (values as defined in ADR).

* `rate_limit` — nested object with `requests_per_window` and `window_s`.

* `circuit_breaker` — nested object with `fail_threshold`, `window_s`, `cooldown_s`.

PF14 does not restate specific numeric values; they live in HDE‑Build Notes/ADR and in the snapshot schema in HDE‑Schemas & Artifacts. The worker MUST treat `POLICY` as the single source of truth for its behavior.

## 21.2 Behavior and sample counts

The worker:

* Uses `POLICY` to decide when to enqueue or skip refreshes (TTL/SWR), when to rate‑limit, and when to open/close the circuit breaker.

* Updates structured `sample_counts` for at least:

  * `refresh_failures`

  * `breaker_tripped`

  * `rate_limit_hits`

The exact metrics surface and aggregation are governed in infra/ops docs (PF07/PF19); PF14 records that these counts are produced and governed.

## 21.3 Schema stability and coordination

Mechanics MUST ensure:

* Running the worker never mutates the schema of `refresh_policy.snapshot.json`; reads are allowed, but writes to the snapshot happen only via the governed snapshot path in HDE‑Schemas & Artifacts.

* Any change to the policy shape or thresholds is coordinated with:

  * HDE‑Build Notes addenda (ADR and bugfix PR‑7R), and

  * HDE‑Schemas & Artifacts snapshot schema and tests,

* so that worker `POLICY`, ADR, and `refresh_policy.snapshot.json` remain in lock‑step.

**Acceptance impact.** No new tokens. This section clarifies the behavior assumed by existing refresh‑policy evidence and tests described in HDE‑Build Notes and HDE‑Schemas & Artifacts; the worker remains dev‑only and is not an acceptance gate in CI.

---

# 22\) SAFE Rails and Provider Gate

Refuse outbound/vendor work unless explicitly enabled. Provide open/close hooks for surfaces/providers and a posture sanity script.

* **Defaults.** Rails CLOSED for all tests and dev harness runs; vendor calls return typed refusals (numeric‑free).

* **Logging.** Keys‑only; no payloads, header values, or secrets.

* **Evidence.** Posture check log (rails closed) and at least one refusal fixture (typed, numeric‑free).

Policy, SAFE‑rails tokens, and vendor transport matrices remain single‑homed in HDE‑Governance and HDE‑CLI‑API‑Vendor‑Ref (titles‑only).

---

# 23\) Rate Limit and Backoff Component (429)

**Closed policy (normative)**

* **Retry/backoff family:** one of `{none, fixed, exponential}` with **integer** parameters; **no jitter**.

* **Retryable conditions:** **only** `{network_error, 5xx}`; other `4xx` do **not** retry.

* **429 handling:** record typed `PROVIDER_RATE_LIMITED` (optionally `retry_after_ms` if provided); **no auto-success path in this epic** (titles-only: EPIC-012 owns the 429 success-route).

* **Envelope & logs:** typed, numeric-free error; keys-only diagnostics (no payload bodies or header values; secrets always redacted).

# 24\) Caching and Transport Wiring \[Required-Now\]

## 24.1 Alpha posture (engine behind the app)

* **Compat surfaces.** Return **`200 OK`** deterministic JSON only (no validators).  
* **No conditionals.** Do **not** implement **304** or **HEAD** in alpha; do **not** attach validators; skip CDN ceremony.  
* **Determinism.** Canonical JSON (UTF-8 no BOM, sorted keys, compact, exactly one LF); AB↔BA and two-run identity hold (see §10.1 / §4).

  ## 24.2 Production posture (Reader / Compat)

**Scope (normative).** Mechanics wires and verifies runtime transport behavior for **JSON success routes** and companion surfaces. Full matrices live in **HDE-CLI-API-Vendor Ref (Appendix A)**; **A7 proofs run on a Catalog JSON success route** (not `/internal/version`).

* **200 (success).** `Content-Type: application/json; charset=utf-8`; include a **strong, quoted ETag** computed over the **LF-terminated** body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304 (conditional).** Only after a prior **200-with-body** for the same ETag; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror the cached 200; ETag present.  
* **HEAD parity.** **Status 200**; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF-terminated, pre-compression).  
* **Writers & errors.** `Cache-Control: no-store`; **no ETag**. Errors **must** include `Content-Type: application/json; charset=utf-8`.  
* **POST non-conditional.** Requests **do not** carry validators; responses **never** return 304 (ignore `If-*` conditionals).  
* **Encoding invariance.** For the same **canonical LF-terminated** body, **ETag identity** and the **effective `Content-Length`** are stable across accepted `Accept-Encoding` (identity/gzip/br). **Capture an encoding-invariance headers-only proof on a Catalog route.**

**Acceptance (titles-only; token names live in HDE-Governance §2.0).**  
 `A7_GET_QUOTED_ETAG_OK`, `READER_200_CTYPE_JSON_UTF8_OK`, `READER_200_CACHECTL_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`.

---

## 24.3 Proof surface & scope (titles-only routing)

* **Success route proofs.** Run on a route listed in `docs/ENDPOINTS_CATALOG.json` (**not** `/internal/version`). Include **GET**, **HEAD parity**, **304 omission**, **writers/errors posture**, and **encoding-invariance** captures; **index human \+ machine** in the **same PR**.  
* **Ops exclusion.** `/internal/version` is operator-only and **not** A7-eligible (see §14 / HDE-Governance §10.5).  
* **Matrices & bytes.** Owned by **HDE-Governance** / **HDE-CLI-API-Vendor Ref** (titles-only). This guide enforces wiring and evidence.

  ## 24.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **A7 success.** Governed by the **A7 token family** (200 `ETag`, HEAD parity, 304 omission, success cache/`Vary`).  
* **Writers/errors.** Governed by the **writers/error token family** (no-store, no `ETag`, error `Content-Type`).  
* **POST posture & invariance.** Governed by Governance tokens for **non-conditional POST** and **encoding/header invariance**.

  ## 24.5 Evidence (records-only; path-agnostic; indexed via the machine mirror)

* **Single home for titles/paths.** §36 **Documentation Artifacts and Registry** (“Reader success catalog & A7 proofs”).  
* **Indexing.** List titles/paths in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (canonical JSONL; one LF; each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`).  
* **Same-PR rule.** Update human Index and mirror **in the same commit/PR**; CI enforces parity and path-proofs.

  ## 24.6 Routing (titles-only)

* **Transport matrices & header rules.** **HDE-Governance** / **HDE-CLI-API-Vendor Ref**.  
* **Evidence registry & mirror discipline.** §1.3 and §36.

---

# 25\) Gate Scripts and Evidence Harness \[Required-Now\]

## 25.1 Scope & pins (capability-level)

Dev/run scripts (or CI jobs) produce **binary acceptance** and **records-only evidence** for the Engine. Script names and locations are implementation-defined (not pinned here).

All byte checks run with:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

JSON is canonical:

* UTF-8, no BOM

* ASCII-sorted keys

* Compact (no pretty-print)

* Exactly one trailing LF

  ---

  ## 25.2 What the harness must prove

* **Determinism (math & emission)**

  * AB↔BA parity (pair neutrality)

  * Two-run identity

  * Canonical re-serialization byte-compare

  * Preimage → hash → final reproducibility  
  * **Registry configuration snapshot:** a canonical `registry_report` (`registry_report.v1`) exists at `artifacts/registry/registry_report.json`, generated via the Programmatic Configuration System (§3), and participates in the same two-run identity and canonical-JSON checks as other governed artifacts.

    

* **CI rails posture.** CI runs **CLOSED** by default. Any job that **opens rails** must pin retry/timeout/backoff policy and must index all governed evidence **in the same PR** (titles-only routing to Governance/Schemas & Artifacts).

* **Transport A7 (success endpoints)**

  * **Proof surface:** run on a **Catalog JSON success** route (see §9.1).

  * `/internal/version` is ops-only and **not** A7-eligible (see §9.4; HDE-Governance §10.5).

* **A7 must prove:**

  * 200 has a strong quoted ETag, success cache headers, and `Vary: Authorization, Accept-Encoding`.

  * HEAD mirrors 200 validators; no body; `Content-Type == GET`; `Content-Length ==` identity 200 body.

  * 304 is served only after 200; no body; omit `Content-Type` and omit `Content-Length`; validators mirror cached 200\.

  * POST is non-conditional (never 304).

  * Writers/errors: `Cache-Control: no-store`; no ETag; errors include `Content-Type: application/json; charset=utf-8`.

  * Encoding invariance: for the same canonical body, ETag identity and effective `Content-Length` are stable across accepted encodings (identity/gzip/br); capture a headers-only proof.

  * Env-gating: capture a headers-only env-gate proof demonstrating non-prod entries are unreachable in prod.

* **Band edges**

  * Inclusive-high thresholds

  * Snapshot edges and diffs for each preset (see §5.3)

* **Reader↔CLI parity**

  * Shared emitter

  * CLI stdout equals Reader 200 body for mirrored surfaces

* **Serializer path guards**

  * Grep-guard denies ad-hoc serializers

  * Symbol proof shows Reader/CLI resolve to the same presenter/emitter

* **Narratives & architecture (keys-only)**

  * Deterministic 10×2 key table `{id, band, personal_key, shared_key}`

  * Architecture snapshot (LF-validated, no secrets)

* **Aux evidence scope (EPIC-010)**

  * Capture exactly **two** headers-only snapshots:

    * `tests/transport/headers/aux_text_200.snap`

    * `tests/transport/headers/aux_suppression_200.snap`

  * Aux HEAD/304 captures are **out of scope**

  * A7 proofs remain **Catalog JSON-success only**

  * (Bytes/policy routed by title to PF05/PF04)

  ---

  ## 25.3 Orchestration & ordering

The harness can be invoked standalone or as part of the sanity pipeline (see §26.5).

**Minimum ordering:**

1. Format

2. Lint/type

3. Unit/property tests

4. Schema checks

5. Goldens

6. Capture artifacts

7. Index \+ mirror parity check

8. Fail-closed on drift

   ---

   ## 25.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* **Determinism**

  * Governed by the determinism token family (AB↔BA, two-run, canonical compare)

* **Transport A7**

  * Governed by A7 tokens

  * Writers/errors posture governed by writers/error tokens

  * Encoding-invariance and Vary tokens required

  * Catalog posture (internal-only, env-gated) tokens required

* **Bands**

  * Governed by bands/edges tokens

* **CLI parity & serializer guards**

  * Governed by CLI/Emitter parity and no-alt-JSON tokens

* **Evidence discipline**

  * Governed by Index/Mirror tokens (human↔machine 1:1; canonical JSONL; path-proofs)

* **Aux/Narrative (EPIC-010)**

  * `NARR_200_TEXT_OK`

  * `NARR_SUPPRESSED_NO_ETAG_OK`

  * `NARR_VARY_AUTH_AE_OK`

  * `AUX_CANON_ALIAS_PARITY_OK`

  ---

  ## 25.5 Evidence & indexing (records-only; machine mirror; same-PR rule)

* **Single home for titles/paths**

  * §36 Documentation Artifacts and Registry

  * This guide does **not** pin file paths here

* **Indexing**

  * List artifact titles/paths in **Appendix D: Evidence Index**

  * Mirror 1:1 in `artifacts/evidence_index.jsonl` (canonical JSONL; exactly one LF)

* **Mirror record fields**

  * `artifact_key`

  * `sha256`

  * `size_bytes`

  * `produced_at_utc`

  * `discovered_physical_path`

  * `proof_anchor`

* **Parity gate**

  * Update human Index and mirror in the **same commit/PR**

  * CI fails on:

    * Mismatch

    * Non-canonical JSONL

    * Unknown keys

    * Missing path-proofs

* **Required titles to appear in Index \+ mirror** (examples, titles-only)

  * Endpoint Catalog snapshot

  * Env-gate proof

  * A7 headers (GET/HEAD/304/writers+errors)

  * Encoding-invariance proof

  * Reader↔CLI parity and canonical-compare artifacts

  * Band-edge snapshots

  * Serializer grep-guard and emitter-symbol proofs

  * `/internal/version` headers/body/two-run captures

* **Mirror field order note**

  * Mirror field order & CI tokens are pinned once in §1.3; this section routes by title only to PF12/PF10 for the exact order and gates.

  ---

  ## 25.6 Routing (titles-only)

* **Transport matrices & A7 policy**

  * HDE-CLI-API-Vendor-Ref

  * HDE-Governance

* **Domains & catalogs / canonical JSON rules**

  * HDE-Schemas & Artifacts

* **Math semantics (preimage, bands, comparators)**

  * HDE-Math-Spec

* **Ops endpoint posture**

  * HDE-Governance §10.5 (see §9.4 for PF14 ops block)

  ---

# 26\) Performance and Load Harness

Load tests for Reader, Compat, and Narrative Selection Router (keys-only). Microbenchmarks: `compat()` core computation \+ narrative key lookups.  
 **Outputs:** non-PII bench reports (bounded histograms \+ percentiles), thresholds, and regression flags.  
 **Routing:** SLO targets and failure posture live in Governance (titles only).

# 27\) Release and Provenance Packaging

**Purpose (normative).** Freeze the engine pack and prove that  
 `release_id = sha256(canonical_bytes("catalog/manifest.json"))`. Mechanics owns the **jobs and evidence**; manifest shape and canonical rules live in **HDE-Schemas and Artifacts** (titles only).

## 27.1 Manifest integrity checks

* **Canonical bytes.** The on-disk `catalog/manifest.json` **equals** its canonical serialization (UTF-8, no BOM; ASCII-sorted keys; compact separators; exactly one trailing `\n`).  
* **`files[]` order.** Entries are **ASCII-ascending by `path`**; **no duplicates** by `path`.  
* **No self-listing.** `catalog/manifest.json` **MUST NOT** appear in `files[]`.  
* **Path constraints.** Each `path` is **relative to `root:"catalog/"`** (no `catalog/` prefix), POSIX, no `..` or `//`, length ≤ 256 bytes.  
* **Entry identity.** For every `{path, sha256, size}`: `sha256` is **lowercase 64-hex of the artifact’s canonical bytes** and `size` matches those canonical bytes.  
* **Pins.** All checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

## 27.2 Recompute `release_id`

1. Read `catalog/manifest.json` in **binary**.  
2. Re-serialize to **canonical bytes** (see **HDE-Schemas and Artifacts §4**).  
3. **Verify** on-disk bytes **equal** canonical bytes (fail closed if not).  
4. Compute SHA-256 over canonical bytes → 64-hex **lowercase**; record as `release_id`.

## 27.3 Evidence & mirror (records-only; same-PR rule)

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF). Update human Index and mirror **in the same commit/PR**; CI fails on mismatch or missing path-proofs.

* `artifacts/math/freeze_pack_manifest.json` — evidence copy of `catalog/manifest.json`  
* `artifacts/math/release_id.txt` — recorded `release_id`  
* `artifacts/math/release_id_recompute.log` — recompute trace  
* `artifacts/math/checksums_audit.log` — per-entry verification (path/sha256/size)

* `artifacts/bodygraph/release_bindings.json` — `{release_id, data_source_policy, ttl_s, swr_s, snapshot_counts{fresh,swr,refresh_queued}}` (canonical JSON; one LF). *(Human+machine indices updated in the same PR.)*

## 27.4 Acceptance (titles-only; token names live in HDE-Governance §2.0)

* `RELEASE_ID_RECOMPUTE_OK`  
* `MANIFEST_SHA256_HEX64_OK`  
* `PACK_MANIFEST_NO_SELF_LISTING_OK`  
* `MANIFEST_PATH_ASCII_SORT_OK`, `MANIFEST_NO_DUP_PATHS_OK`  
* `PACK_ROOT_PINNED_OK` *(if `root` present)*  
* `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`

**Routing (titles-only).** Manifest shape, canonical JSON rules, and mirror schema: **HDE-Schemas and Artifacts**. Public transport remains in **HDE-CLI-API-Vendor Ref** / **HDE-Governance**.

## 27.5 Sanity pipeline (release & provenance) \[Required-Now\]

**Purpose (normative).** Provide a single, scriptable pipeline that verifies the release **end-to-end** and **fails closed** on any drift. It finishes by updating the human index and the machine mirror with **1:1 parity** and **path-proofs**.

**Ordered steps (minimal sequence)**

1. **Format** (code/docs)  
2. **Lint / type** checks  
3. **Unit \+ property tests** (determinism, comparators)  
4. **Schema validation** (domains, payloads as applicable)  
5. **Goldens** (AB↔BA, two-run, bands edges, canonical compare)  
6. **Capture artifacts** (this release):  
   * Pack identity: manifest evidence copy, `release_id` recompute, checksums audit (see 26.3)  
   * Transport proofs (A7) on a cataloged success route (see §9.1/§27.2)  
   * Internal-ops `/internal/version` snapshots (see §27.4/§14)  
   * DB posture artifacts (see §20/§27.5)  
7. **Index \+ mirror parity check**: update **Appendix D: Evidence Index** and write mirror records to `artifacts/evidence_index.jsonl` (**same commit/PR**), then verify:  
   * 1:1 join (title/path ↔ artifact\_key/discovered\_physical\_path)  
   * Canonical JSONL (UTF-8, sorted keys, compact, one LF)  
   * **Path-proofs** present and referenced by `proof_anchor`  
8. **Fail closed on drift** (non-canonical bytes, parity mismatch, missing path-proofs, changed digests, or schema violations)

**Evidence (records-only; machine mirror; same-PR rule)**

* `artifacts/proofs/sanity_pipeline.transcript.log` — pipeline transcript (ordered steps \+ pass/fail summary)  
* Existing artifacts produced in step 6 (see 26.3, §27, §20, §36) must also be indexed and mirrored **in this run**

When the sanity pipeline script (for example, `python tools/evidence/run_sanity_pipeline.py`) is invoked **from a Live QA harness** rather than as part of the release CI, Mechanics requires additional behavior on top of the release pipeline rules in this section:

* **Explicit QA log capture.**

  * Any QA step that invokes the sanity pipeline **MUST** capture a primary QA log under `audit/qa/<epic>/<run-id>/` (for example, `stepN_sanity_pipeline.log`), treated as the canonical evidence for that step.

  * The sanity pipeline script **MUST** emit a clear, parseable **pass/fail summary** suitable for inclusion in this log, either:

    * directly on stdout (so the harness can tee it into the QA log), or

    * to a deterministic, harness-readable log file that the QA harness then copies into `audit/qa/<epic>/...`.

  * The summary **MUST** include, at minimum, an overall status line (for example, a `status_final` value or equivalent) that allows QA and auditors to determine whether the pipeline completed successfully in that QA environment.

* **Classification of QA pipeline failures.**

  * If the QA harness invokes the sanity pipeline but **no output is captured** in the primary QA log (for example, the log remains empty or contains only a header with no pipeline summary), that QA step **MUST** be classified as a **tooling/harness failure** rather than as a behavioral failure of the engine or the sanity pipeline itself.

  * In that case, PF14 treats the step as **FAIL\_TOOLING** from a mechanics perspective: the harness or environment prevented the pipeline’s output from being captured, and the step remains blocked until the harness is fixed.

  * The semantics and exact vocabulary for `FAIL_TOOLING` vs `FAIL_BEHAVIOR` or `PASS` remain single-homed in **Glow QA Guide** and **HDE-Build Checklist**; this guide only requires that QA steps distinguish “pipeline could not be observed” (tooling) from “pipeline ran and failed tests” (behavior).

* **Routing to tokens and QA docs (titles-only).**

  * The acceptance tokens that depend on the sanity pipeline (for example, `SANITY_PIPELINE_OK`, `DETERMINISM_ENV_PINS_OK`, and related QA tokens) and their exact evidence requirements remain defined in **Glow QA Guide**, **HDE-Build Checklist**, and **HDE Phased Epics** by title.

  * PF14 records that, for QA-invoked runs, those tokens **must not** be treated as proven unless there is a captured sanity pipeline QA log with a clear pass/fail summary; if QA runs the pipeline and captures no output, that run is mechanics-wise a **tooling/harness issue** and cannot be used as evidence for those tokens.

These QA-specific requirements do **not** change the release/CI semantics of the sanity pipeline described earlier in this section. Release acceptance and the canonical pipeline transcript remain governed by the closed-rails CI posture; QA invocations add a second usage of the same pipeline script, with additional logging and classification requirements so that Live QA evidence is unambiguous and mechanics-complete.

**Acceptance (titles-only; token names live in HDE-Governance §2.0)**

* `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`  
* `JSON_CANONICAL_CHECK_OK` (mirror records and any JSON artifacts)  
* `RELEASE_ID_RECOMPUTE_OK` (pack identity verified)  
* Plus applicable transport/ops/DB tokens referenced by §9/§14/§20/§27

**Routing (titles-only).** Evidence and mirror schema: **HDE-Schemas and Artifacts**. Transport matrices and `/internal/version` policy: **HDE-CLI-API-Vendor Ref** / **HDE-Governance**. Domain/pack rules: **HDE-Schemas and Artifacts**.

---

# 28\) Post-deploy Smoke

**Purpose (normative).** Run a minimal, production-against-production verification immediately after deploy. Prove transport correctness on a **cataloged success route**, confirm **writers/errors** posture, verify **internal ops** surface, and spot-check **DB posture**. Mechanics captures artifacts and indexes them in the Evidence Index and machine mirror **in the same commit/PR**.

## 28.1 Scope & pins

* **Environment pins.** All captures/compares run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.  
* **Routing.** Transport matrices live in **HDE-CLI-API-Vendor Ref**; `/internal/version` policy in **HDE-Governance §10.5**; DB mechanics in **§20**.

## 28.2 Success route (A7) — transport smoke

* **Surface.** Use a route listed in the **Endpoint Catalog (JSON success)** (see §9.1).  
* **Prove (headers-only):**  
  * **200:** strong **quoted `ETag`**, `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`.  
  * **HEAD parity:** no body; validators mirror 200; **`Content-Type == GET`**; **`Content-Length == identity 200 body`**.  
  * **304:** served **only after** a prior 200; **no body; omit `Content-Type` and `Content-Length`**; validators mirror cached 200\.

## 28.3 Writers & errors — posture smoke

* **Writers/errors:** `Cache-Control: no-store`; **no `ETag`**.  
* **Errors:** `Content-Type: application/json; charset=utf-8`; typed, numeric-free error bodies (see Vendor Ref error model).

## 28.4 Internal ops `/internal/version` — ops-only smoke

* **GET 200:** JSON UTF-8; `Cache-Control: no-store`; **no `ETag`**; `Last-Modified` absent; `Vary` optional.  
* **HEAD 200:** mirrors GET validators; **no body**; **`Content-Length == identity GET body`**; **`Content-Type == GET`**.  
* **Conditionals:** `If-None-Match` / `If-Modified-Since` **ignored**; **never 304**.  
* **A7:** **not** a success route; **exclude** from A7 proofs.

## 28.5 Database posture — live checks

* **search\_path:** prove `hde, public` (unquoted, in that order).  
* **Roles/grants:** least-privilege at runtime (snapshot grants/constraints).  
* **Schema identity:** normalized DDL fingerprint captured (see §20.1).  
* **(Optional) RW smoke:** insert→delete round-trip against a scratch table (job-profile gated).

## 28.6 Evidence (records-only; machine mirror; same-PR rule)

List by **title/path** in **Appendix D: Evidence Index** and mirror **1:1** in `artifacts/evidence_index.jsonl` (each record: `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`; canonical JSONL; one LF).

**Success route (A7) proofs**

* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`

**Internal ops**

* `artifacts/ops/internal_version/headers_get.txt`  
* `artifacts/ops/internal_version/headers_head.txt`  
* `artifacts/ops/internal_version/cond_if_none_match_headers.txt`  
* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`  
* `artifacts/ops/internal_version/body_get.json` \+ `artifacts/ops/internal_version/body_get.sha256`  
* `artifacts/ops/internal_version/provenance_note.md`

**DB posture**

* `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`, `artifacts/db/check_constraints.txt`  
* `artifacts/db/partition_plan.txt` *(if used)*  
* `artifacts/db/db_rw_smoke.log` *(optional)*

**Pins & harness**

* `artifacts/proofs/env_pins.txt`

  ## 28.7 Acceptance (titles-only; tokens live in HDE-Governance §2.0)

* **Success route (A7).** Governed by the **A7 token family** in Governance (200 `ETag`, HEAD parity, 304 omission, success cache/`Vary`).  
* **Writers/errors.** Governed by the **writers/error token family** (no-store, no `ETag`, error `Content-Type`).  
* **Internal ops (`/internal/version`).** Governed by the **INTVER token family** (ops-only posture, HEAD parity, conditionals ignored).  
* **DB posture.** Governed by *DB\_ tokens*\* (connection/env, search\_path, roles, schema fingerprint; optional RW smoke if run).  
* **Evidence discipline.** Governed by **Index/Mirror tokens** (human↔machine 1:1; canonical JSONL; path-proofs).

This guide asserts capability-level conformance and **routes all token names to HDE-Governance §2.0**. Artifacts are captured per **§27.6** and indexed per **§1.3/§36**.

---

# 29\) Server Cache (Production) — rolled in

**Purpose.** Optional, private, composite-key cache for **Reader** and **Compat** that preserves A7 transport rules and deterministic invalidation.

### **Key**

* **Composite key fields.** `{ viewer_id | person_id(s) }`, `design_fingerprint`, `thresholds_identity`, `release_id`.  
* **Pair normalization.** Normalize `{a,b}` to a stable order (**AB↔BA**) before keying.  
* **Viewer scope.** Include `viewer_id` **only** when output depends on viewer preferences.  
* **Determinism.** Key construction is pure and reproducible; no clock, no randomness.

  ### **Transport (A7-consistent)**

* **200 (success).** `Content-Type: application/json; charset=utf-8`; **strong, quoted ETag** over the **LF-terminated** body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **304 (conditional).** Only after a prior **200-with-body** for the same ETag; **no body**; **omit `Content-Type` and omit `Content-Length`**; validators mirror the cached 200; ETag present.  
* **HEAD parity.** **Status 200**; **no body**; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)` (LF, pre-compression).  
* **Writers & errors.** `Cache-Control: no-store`; **no ETag**; writers bypass cache.  
* **Encoding invariance.** For the same canonical body, **ETag identity** and **effective `Content-Length`** are stable across accepted `Accept-Encoding` (identity/gzip/br).  
* **Ops exception.** `/internal/version` is operator-only and **never cached**.

  ### **Invalidation (deterministic)**

* **Triggers.** Any change to **`release_id`**, **`thresholds_identity`**, **input payloads** (incl. `viewer_prefs`), or **`design_fingerprint`**.  
* **Effect.** Invalidation is **immediate**; **no stale bytes** are served after an invalidation event.

  ### **Controls**

* **Default OFF.** Enable via a runtime flag.  
* **Metrics.** Emit counters for **hits**, **misses**, **invalidations**.  
* **Diagnostics (optional).** A keyed, redaction-safe debug log of cache decisions for local analysis (titles-only in indices).  
  ---

# 30\) Observability (Logs and Metrics)

**Logging (keys-only)**

* Structured, **keys-only** logs with correlation IDs (non-PII, bounded).  
* Surfaces: Reader, Compat, cache layer, rate-limit decisions.  
* **Guards:** grep-guards prevent payload/secret logging; only allow-listed labels.

**Metrics**

* **Counters/Histograms:** request counts, latencies, cache hits/misses, rate-limit outcomes.  
* **Dashboards:** quick views for transport health, cache efficacy, and error rates.

**BodyGraph ingest signals**

* **Counters:** refresh successes/failures; rate-limit throttles; circuit-breaker trips.  
* **Histograms:** vendor latency.  
* **Gauges:** staleness percentage.  
* **Evidence:** `artifacts/bodygraph/metrics.snapshot.json` (keys-only, canonical JSON, single LF).

# 31\) Security Posture

**Controls**

* Per-route rate limits  
* CSRF: rotate token and retry once on browser writers  
* Strict input validation  
* Writers: `Cache-Control: no-store`; typed errors; no `ETag`  
* Never log secrets or PII

**Packaging & Runtime**

* Dockerfile and process launch scripts  
* Health and readiness probes  
* Externalize only secrets/coordinates via environment variables  
* Generate typed config at build time

**Identity**

* `/internal/version` is operator-only; `Cache-Control: no-store`; no `ETag`  
* Provenance: `build_commit` is optional in production and may be unset/null

**Logs (ingest)**

* Keys-only logs; no raw birth data; no vendor payloads; secrets never logged  
* Provide a sanitized sample: `artifacts/bodygraph/keys_only.logs.sample`

# 32\) Packaging and Runtime \[Required-Now\]

**Scope.** Container packaging and runtime posture for the HD Engine. Mechanics owns image/process hardening, config plumbing, health/ready behavior, and operational guardrails. Public bytes, schemas, and transport matrices are referenced by title only. All byte-sensitive checks run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

## 32.1 Image & process posture

* **Deterministic build.** Reproducible container image; pin base; lock package indexes; emit SBOM.  
* **Least privilege.** Run as non-root; drop Linux capabilities; prefer read-only root FS with writable tmp/cache only if required.  
* **Single binary & emitter.** Wire the **allow-listed presenter/emitter** (see §4, §10.2); forbid ad hoc serialization in entrypoints.  
* **Locale pins.** Export `LC_ALL=C`, `LANG=C`, `TZ=UTC` for all emit/compare paths to preserve byte identity.  
* **Resource limits.** Set CPU/memory limits and graceful shutdown (SIGTERM → drain → exit 0).

## 32.1A Start command & service factory \[Required-Now\]

**Purpose (normative).** Capture the exact production start command and prove the app factory binds to **`$PORT`**.

* **Start-command capture (records-only).** Capture the exact launch command line used in production (no secrets). Store as canonical text (UTF-8; exactly one trailing `\n`). *(Evidence path listed in §36.)*  
* **Factory binding to `$PORT`.** Prove the service initializes via the factory `adapter.factory:create_app()` (titles only) and binds to **`$PORT`** from the environment (no hard-coded port).  
* **Runtime pins (minimal).** Record `PORT`, `APP_ENV`, and identity pins required for traceability as a keys-only text snapshot (UTF-8; one `\n`). *(Evidence path listed in §36.)*

## 32.2 Configuration & environment

* **Typed config at build.** Generate a typed runtime config artifact at build (defaults, switches, A7 posture) and vendor it into the image.  
* **Env allow-list (secrets/coordinates only).** Only read whitelisted keys at startup: `SAFE_MODE`, `ALLOW_NETWORK`, `HDAPI_BASE_URL`, `HD_API_KEY` (secret), `GEO_API_KEY` (secret), `PORT`, and explicitly documented toggles.  
* **Fail-closed on unknowns.** Unknown env keys or malformed values fail fast; do not partially boot.  
* **Rails posture.** Rails defaults derive from the **Env Deployment Inventory** (titles-only): **dev & stage OPEN**, **prod CLOSED**, **CI CLOSED**. In CI, any job that opens rails must pin policy and index governed evidence **in the same PR**. Determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`) apply in **all** environments that produce governed bytes.

## 32.3 Health/ready & lifecycle

* **HTTP probes.**  
   `/healthz`: liveness (process up, core initialized).  
   `/readyz`: readiness (emitter wired, pack loaded, manifest hashed, rails posture read).  
* **Probe bytes.** Minimal, numeric-free JSON; canonicalized (UTF-8/no BOM, sorted keys, compact, one LF).  
* **Graceful shutdown.** Stop accepting traffic on TERM; complete in-flight; emit final health with `status:"stopping"`; exit cleanly.

## 32.4 Security & observability

* **Keys-only logs.** No payload or header values in logs; secrets always REDACTED; bounded labels (route, outcome, rails\_state, timeout\_profile, attempt\_idx).  
* **Metrics (bounded).** Counters/timers/histograms for engine/presenter latency and transport outcomes; no PII.  
* **Tracing.** Optional `correlation_id` (non-PII) with bounded cardinality.

## 32.5 Transport & identity (titles-only)

* **Reader A7 (public).** See **HDE-CLI-API-Vendor Ref** and **HDE-Governance** (ETag over LF-terminated body; `Vary` policy; 304 omits `Content-Type` and `Content-Length`; HEAD parity; POST non-conditional).  
* **Internal ops `/internal/version`.** Operator-only; `Cache-Control: no-store`; **no `ETag`**; HEAD parity; conditionals ignored; body includes `engine_tag`, `release_id`, `invocation_tag`, `emitter_sha256`, optional `build_commit` (see §14).  
* **Identity.** `release_id` from canonical manifest (**HDE-Schemas and Artifacts §6**); `invocation_tag` participates in preimage (**HDE-Math-Spec §3**); presenter uses canonical serializer (§4).

## 32.6 Acceptance (binary)

* **Image & user.** SBOM produced; runs as non-root; read-only FS validated at runtime.  
* **Config discipline.** Only allow-listed env consumed; unknowns fail; typed config present; SAFE rails ON by default.  
* **Health/ready.** Probes return canonical JSON; liveness/readiness reflect emitter/pack state; graceful shutdown proven.  
* **Ops posture.** `/internal/version` headers/body match §14; **no-store**, **no `ETag`**, conditionals **ignored**, one LF; HEAD 200 parity.  
* **Start command & factory.** Start command captured; factory proven; **binds `$PORT`**.  
* **Determinism.** `LC_ALL=C`, `LANG=C`, `TZ=UTC` enforced; canonical re-serialization byte-compare passes for all public/ops surfaces emitted from this process.

**Acceptance tokens (titles-only; token names live in HDE-Governance §2.0)**  
 `SERVICE_START_CMD_CAPTURED_OK`, `GUNICORN_APP_FACTORY_OK`, `ENV_PORT_REQUIRED_OK`,  
 `DB_CONN_ENV_OK` *(if DB env validated here)*,  
 plus any applicable transport/ops tokens referenced by §14 and §9.

## 32.7 Evidence (titles/paths only)

**Single home for artifact titles/paths.** Do **not** pin file paths here. The authoritative registry of artifacts and their titles/paths lives in **§36 Documentation Artifacts and Registry**. Mechanics **MUST**:

* List artifacts by **title/path** in **Appendix D: Evidence Index** (human).  
* Write **records-only** mirror entries to `artifacts/evidence_index.jsonl` in the **same commit/PR** (machine).  
* Ensure each mirror record is canonical JSONL (UTF-8, no BOM; sorted keys; compact; exactly one LF) and includes:  
   `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor`.  
* Maintain strict **1:1 parity** between human Index and machine mirror; CI fails on mismatch or missing **path-proofs**.

**Routing (titles-only).** A7 and ops policies: **HDE-Governance**. Public bytes & preimage: **HDE-CLI-API-Vendor Ref** / **HDE-Math-Spec**. Pack/manifest: **HDE-Schemas and Artifacts**. Evidence registry/mirror discipline: **§1.3** and **§36**.

---

# 33\) SDKs (Client Libraries) — rolled in

Client libraries use the allow-listed presenter-emitter and enforce transport rules.

**TypeScript SDK (required)**

* `readPerson(id | payload)` — calls Reader; returns the exact public body bytes (LF-terminated). `await .json()` is available as a convenience parser.  
* `compat(a, b, prefs)` — calls `/api/compat/v1` with `POST` and `Content-Type: application/json`; returns the exact body bytes; `await .json()` available.  
* `sample(viewer_prefs, seed?)` — calls `/api/sample/v1` with `POST`; returns the exact body bytes; ordering matches service; `await .json()` available.

**conditionalGetHelper (Reader; production)**

* Implements conditional GET with `If-None-Match`.  
* On `200`: returns `{status:200, etag, body_bytes}`, updates cache.  
* On `304`: returns `{status:304, etag, body_bytes}` using cached bytes; server `304` has no body, omits `Content-Type`, and has `Content-Length 0` or absent.  
* Helpers surface the strong, quoted `ETag` for callers.

**Python SDK (ops/automation)**

* Mirrors `readPerson`, `compat`, `sample`; returns body bytes with optional `.json()` convenience.  
* Includes byte/order parity tests against the service.

**Policy**

* All SDK calls **MUST** preserve canonical JSON bytes (UTF-8, sorted keys, compact separators, exactly one trailing LF).  
* Application teams **SHOULD** use the SDK to guarantee byte/order parity with the single emitter and correct A7 transport behavior.

**Acceptance**

* TypeScript `compat()` and `sample()` bytes are bitwise-equal to service `200` bodies; `sample()` ordering matches.  
* `conditionalGetHelper` sends `If-None-Match` and handles `304` semantics exactly (no body, omit `Content-Type`, `Content-Length 0/absent`).  
* Python SDK parity tests pass for bytes and ordering across all three calls.

# **34\) Dev HTTP Harness (single home)**

Dev-only; bound to `127.0.0.1`; not public; CORS disabled; `APP_ENV=dev`; debug reloader **off** during captures. Emits canonical JSON via the allow-listed presenter-emitter (§4/§8).

**Routes**

* `GET|POST /api/reader` (person)

* `GET|POST /api/compat/v1` (pair; ids-only `GET`)

* `POST /api/sample/v1`

**Method posture**

* `GET` **MUST NOT** include a body.

* `POST` is **non-conditional** (no validators; never returns `304`).

**Dev error posture (Reader & Compat)**

* `Content-Type: application/json; charset=utf-8`

* `Cache-Control: no-store`

* **No `ETag`**

**Runner (local example only)**

* For local-only experimentation on a developer machine, you may start a dev Reader process with an example runner such as:

   `python -m adapter.http_reader --bind 127.0.0.1:5000`

   This command is an **illustrative local sample**, not an infra-canonical binding. Mechanics does **not** pin a specific port for the dev Reader harness; environment-specific start commands and host/port bindings (for example, Codespaces vs local dev) are infra-owned and are defined in **Glow Infrastructure** and related PF-Canon by title. QA plans and docs **must not** treat this 5000 example as authoritative for any environment; they must derive actual base URLs and ports from infra-owned configuration.

**Quick start (curl — local 5000 example)**

For local-only runs using the example runner above:

export APP\_ENV=dev

\# Pair (POST, invalid JSON/body as needed for tests)

curl \-s [http://127.0.0.1:5000/api/compat/v1](http://127.0.0.1:5000/api/compat/v1) \-H 'Content-Type: application/json'  
 \-X POST \-d '{"a":{…},"b":{…},"viewer\_prefs":{…}}' | jq .

\# Reader (POST body form)

curl \-s [http://127.0.0.1:5000/api/reader](http://127.0.0.1:5000/api/reader) \-H 'Content-Type: application/json'  
 \-X POST \-d '{"id":"…"}' | jq .

\# Sample with seed (POST)

curl \-s [http://127.0.0.1:5000/api/sample/v1](http://127.0.0.1:5000/api/sample/v1) \-H 'Content-Type: application/json'  
 \-X POST \-d '{"viewer\_prefs":{…},"seed":12345}' | jq .

For Codespaces and other shared environments, Mechanics requires that QA and docs use the **infra-provided dev start commands and URLs** (for example, values exposed via devcontainer or environment keys described in **Glow Infrastructure** and **HDE-Build Checklist** by title) instead of hard-coding hostnames or ports in plans or scripts.

# 35\) Runbooks (Operations)

Runbooks for elevated 5xx, slow Reader/Compat, stuck queue, DB lag. Fast rollback \+ data safety notes.  
 **Pointers:** rollback uses pointer-flip to last known-good `release_id` (titles only).

# 36\) Dashboards and Alerts

Dashboards for Reader, Compat, Narrative Router, and Server Cache latencies, error rates, hit/miss, and rate-limits. Actionable alerts for error spikes and budget breaches.  
 **Notes:** include A7 headers health and cache hit ratio panels.

---

# 37\) Documentation Artifacts and Registry \[Required-Now\] 

Registry for small, deterministic documentation artifacts and gate evidence. Titles-only cross-refs; bytes live in files. Mechanics keeps the human index and the machine mirror in lockstep (same-PR rule).

---

## 37.1 Purpose & scope

* Provide a **single registry** for governed documentation artifacts and gate evidence.

* Keep **Human Index** and **Machine Mirror** in 1:1 parity, updated in the **same commit/PR**.

* Act only on **governed paths**; transient generator outputs are never authoritative.

---

## 37.2 Governance & homes

* **Governed paths only**

  * `/artifacts/**` — public documentation snapshots and pack/identity evidence.

  * `/audit/gates/**` — gate evidence produced by §24 scripts (bands / canonical / props / etc.).

  * Transient generator paths (for example, `codex/out/**`) are **not authoritative** and **MUST NOT** be indexed.

* **Human Index (single home)**

  * `docs/evidence/INDEX.json` — titles/paths only; no payload bytes.

* **Machine Mirror (single home)**

  * `artifacts/evidence_index.jsonl` — records-only JSONL; one LF per record.

---

## 37.3 Conventions

* Deterministic filenames (lowercase, stable tokens).

* Allowed extensions: `.json`, `.log`, `.txt`, `.bytes`.

* Text artifacts end with **exactly one trailing LF** (`\n`).

* JSON is **canonical**:

  * UTF-8, no BOM

  * ASCII-sorted keys

  * compact (no pretty-printing)

  * exactly one trailing LF

* `.bytes` files mirror the exact body bytes (including the body’s own trailing LF, if present).

* Header snapshots follow §4.3 normalization (lower-cased keys, compact, one LF).

---

## 37.4 Machine Mirror (records-only)

Every artifact listed in this registry **MUST** have a 1:1 record in `artifacts/evidence_index.jsonl`:

* Required fields per record:

  * `artifact_key`

  * `role`

  * `sha256`

  * `size_bytes`

  * `produced_at_utc`

  * `discovered_physical_path`

  * `proof_anchor` (path-proof transcript)

* **Exact field order (normative)**

  * `artifact_key`

  * `discovered_physical_path`

  * `produced_at_utc`

  * `proof_anchor`

  * `role`

  * `sha256`

  * `size_bytes`

* **Discipline**

  * Sort-before-write by `(artifact_key, discovered_physical_path)`.

  * Unknown keys are **rejected**.

  * One LF per record; no blank lines.

  * Update the Human Index and Machine Mirror in the **same commit/PR**.

* **Acceptance tokens (titles-only)**

  * `MACHINE_MIRROR_UPDATED_OK`

  * `CI_CHECK_MIRROR_SCHEMA_OK`

  * `CI_CHECK_FINAL_LF_OK`

  * (plus index parity tokens already listed elsewhere: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`)

---

## 37.5 Required captures — Reader success catalog & A7 proofs

* **Catalog**

  * `docs/ENDPOINTS_CATALOG.json`

  * `docs/ENDPOINTS_CATALOG.json.sha256`

* **Env-gate proof**

  * `artifacts/proofs/endpoints_env_gate_proof.log`

    * Proves non-prod entries are unreachable in prod.

* **Success route proofs**

  * `artifacts/proofs/success_get.txt` — GET 200 proof.

  * `artifacts/proofs/success_head.txt` — HEAD 200 parity proof.

  * `artifacts/proofs/success_304.txt` — 304 omission proof (omits `Content-Type` and `Content-Length`).

  * `artifacts/proofs/success_writers_errors.txt` — writers/errors posture proof.

  * *(Optional)* `artifacts/proofs/encoding_invariance.txt` — encoding-invariance proof.

---

## **37.6 Serializer / emitter guards**

Serializer and emitter guards are the mechanical enforcement layer for CLI serializer coupling (see §4 and §18). They prove that:

* public CLI flows do not use ad-hoc JSON serializers, and

* governed CLI handlers call the allow-listed presenter/emitter symbols.

  ### **37.6.1 Guard tools (closed-rails, deterministic)**

Mechanics defines two canonical CLI guard tools:

* tools/cli/serializer\_grep\_guard.py

  * AST-based grep guard over the governed CLI scope (default roots under engine/cli).

  * Detects imports of the json module and call-sites that resolve to json.dumps or json.dump (including alias imports).

  * Renders a deterministic report with:

    * a single scope line describing the scanned roots, and

    * a summary line of the form “summary: PASS” or “summary: FAIL” followed by sorted violation lines when present.

  * The report contains no timestamps, environment echoes, or non-deterministic content.

* tools/cli/emitter\_symbol\_proof.py

  * AST-based emitter proof over the CLI module (engine/cli/main.py).

  * Tracks call-sites in the governed handlers (showcompat, aux\_preview, bg\_resolve) and records which allow-listed emitter symbols they invoke.

  * Emits deterministic lines of the form “handler:function:emitters” plus a summary line indicating PASS or FAIL for the non-optional handlers.

Both guard tools:

* import and call ensure\_determinism\_env from engine/runtime/determinism\_env.py at startup,

* require the determinism pins and closed rails to be satisfied (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0), and

* fail closed (non-zero exit) if the pins are not met.

CI must call these tools only under the closed-rails determinism posture described in §1.2 and §6.2; check\_env\_pins and related jobs enforce the pins before running the guards.

### **37.6.2 Guard artifacts (canonical paths and roles)**

The canonical guard artifacts and their roles are:

* artifacts/cli/guards/serializer\_grep\_guard.log

  * Role: log.

  * Contains the serializer grep guard report (scope line, summary line, and any sorted violation lines).

  * A PASS report demonstrates that the governed CLI scope has no direct json.dumps or json.dump usage and that public JSON flows pass through the canonical emitter.

* artifacts/cli/guards/emitter\_symbol\_proof.txt

  * Role: snapshot.

  * Contains the emitter symbol proof for the governed CLI handlers.

  * For showcompat and bg\_resolve, the proof must show at least one allow-listed emitter symbol (for example, emitter.emit\_public or emit\_reader\_public\_envelope) and must mark the summary as PASS.

  * aux-preview is treated as an optional emitter handler: when it has no canonical emitter, it is rendered as a handler line with a “none” emitter listing and is explicitly exempt in the PASS/FAIL decision, so the absence of an emitter for aux-preview does not cause the guard to fail, while still keeping the handler visible in the proof.

These artifacts are the paths of record for:

* Phase I serializer work,

* EPIC017 and EPIC018 CLI serializer acceptance, and

* evidence indexing for serializer/emitter guards.

The Evidence Index and Machine Mirror must use these paths as discovered\_physical\_path for the corresponding records; any other locations are copies only.

### **37.6.3 Indexing, mirror, and secondary locations**

Indexing and mirror discipline for guard artifacts follow §1.3 and §37.4:

* List guard artifacts by title and path in Appendix D: Evidence Index.

* Mirror them 1:1 in artifacts/evidence\_index.jsonl (canonical JSONL; UTF-8, ASCII-sorted keys, compact, one LF; unknown keys rejected; exact field order pinned in §1.3).

* Each mirror record includes a proof\_anchor pointing at a co-located path\_proof transcript for the guard artifact.

For backward compatibility:

* Implementations may also write copies of the guard artifacts under audit/gates/guards/\*\* for internal audit workflows.

* These audit/gates/guards/\*\* paths are secondary only and are not required for mechanics-level acceptance.

Future PF documents and epic records that reference CLI serializer/emitter guards should use the artifacts/cli/guards/\*\* paths as canonical and treat audit/gates/guards/\*\* as historical or auxiliary.

### **37.6.4 Live QA runs under open rails (informative)**

**Status (informative, mechanics-aware).**  
 The canonical pass condition for CLI serializer/emitter guards is defined under **closed determinism rails** in CI and other CLOSED-rails environments (see §1.2, §6.2, and §37.6.1). In deliberately open-rails Live QA environments (for example, PO-run Codespaces sessions used for hands-on product checks), Mechanics treats guard behavior differently:

* **Env-mismatch failures are expected.** When the determinism pins required by ensure\_determinism\_env are not satisfied (for example, SAFE\_MODE or ALLOW\_NETWORK differ from the closed-rails CI posture), the guard tools are expected to:

  * refuse to run in “PASS” mode, and

  * exit non-zero with logs that clearly indicate an environment mismatch rather than a serializer/emitter wiring error.

* **Open-rails Live QA is env-enforcement only.** Running the guards in an open-rails Live QA environment is allowed as an **env-enforcement check**:

  * A non-zero exit due solely to determinism env mismatch confirms that the guards are enforcing the closed-rails policy correctly.

  * Such runs do **not** contribute to the canonical guard acceptance condition and must not be interpreted as evidence of broken CLI serializer or emitter wiring.

* **Canonical acceptance remains CLOSED-rails.** The **authoritative acceptance** for CLI serializer/emitter guard tokens remains:

  * CI and other CLOSED-rails jobs that run the guard tools under the determinism pins described in §1.2 and §6.2, and

  * guard artifacts and mirror records produced in that posture, as described in §17.8, §18.5, and §37.6.2–§37.6.3.

Mechanics records this distinction so that PF-Canon and QA plans can treat open-rails guard runs as **informational** (env-pin enforcement) while continuing to rely on CLOSED-rails CI runs for normative D-stage/guard acceptance. PF14 does not define new tokens here; token semantics and QA expectations for guard runs remain single-homed in HDE-Governance, Glow QA Guide, HDE-Build Checklist, and HDE Phased Epics by title.

---

## 37.7 CLI parity & determinism (public bytes)

* **AB ↔ BA goldens**

  * `artifacts/cli/ab.json`

  * `artifacts/cli/ba.json` — LF-terminated canonical JSON; BA must be **byte-identical** to AB.

* **Parity summary**

  * `artifacts/cli/summary.json` — canonical JSON with:

    * attempted commands,

    * sha256 of AB/BA,

    * `ab_ba_equal: true`.

* **Two-run marker**

  * `artifacts/cards/A3/IDENTITY_OK.txt`

* **Canonical compare**

  * `audit/gates/canonical/json_canon_compare.log`

---

## 37.8 CLI Admin Preview (narrative)

* `artifacts/cli/narrative/stdout.txt` — LF-terminated text (no ANSI).

* `artifacts/cli/narrative/sidecar.json` — ids-only canonical JSON (no prose).

Both **must** be indexed in the Human Index and Machine Mirror in the same PR.

---

## 37.9 Canonical JSON checks

* **Policy check**

  * `audit/gates/canonical/json_canonical_check.log`

* **Canonical re-serialization compare**

  * `audit/gates/canonical/json_canon_compare.log`

---

## 37.10 Bands edges (inclusive-high)

* **Edges snapshot**

  * `audit/gates/bands/edges.snapshot.json`

* **Edges diff**

  * `audit/gates/bands/edges.diff.json`

---

## 37.11 Pack identity & provenance

* **Evidence copy of manifest**

  * `artifacts/math/freeze_pack_manifest.json`

* **Recomputed release\_id**

  * `artifacts/math/release_id.txt`

* **Recompute log**

  * `artifacts/math/release_id_recompute.log`

* **Checksums audit**

  * `artifacts/math/checksums_audit.log`

* *(Optional) SBOM (CycloneDX) \+ hash*

  * `sbom/cyclonedx.json`

  * `sbom/cyclonedx.json.sha256`

---

## 37.12 Identity & Math

* **Service identity (admin JSON)**

  * `artifacts/identity/service_identity.json`

* **Emitter SHA-256**

  * `artifacts/identity/emitter_sha256.txt`

---

## 37.13 Internal-ops `/internal/version` snapshots

* **GET headers**

  * `artifacts/ops/internal_version/headers_get.txt`

* **HEAD headers**

  * `artifacts/ops/internal_version/headers_head.txt`

* **Conditional headers**

  * `artifacts/ops/internal_version/cond_if_none_match_headers.txt`

  * `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

* **Body & hash**

  * `artifacts/ops/internal_version/body_get.json`

  * `artifacts/ops/internal_version/body_get.sha256`

* **Provenance note**

  * `artifacts/ops/internal_version/provenance_note.md`

---

## 37.14 Database proofs & ops pins

* **DDL snapshot**

  * `artifacts/db/ddl_fingerprint.json`

* **Grants/constraints checks**

  * `artifacts/db/grants.txt`

  * `artifacts/db/check_constraints.txt`

* **Schema check**

  * `artifacts/db/check_schema.txt`

* **Partition plan**

  * `artifacts/db/partition_plan.txt`

* **Start command capture**

  * `artifacts/proofs/start_command_capture.txt`

* **Environment pins**

  * `artifacts/proofs/env_pins.txt`

---

## 37.15 BodyGraph proofs

* **Source selection snapshot**

  * `artifacts/bodygraph/source_selection.snapshot.json`

* **Source invariance**

  * `artifacts/bodygraph/source_invariance/ab.json`

  * `artifacts/bodygraph/source_invariance/ba.json`

  * `artifacts/bodygraph/source_invariance/summary.json`

* **Refresh policy**

  * `artifacts/bodygraph/refresh_policy.snapshot.json`

* **Metrics**

  * `artifacts/bodygraph/metrics.snapshot.json`

* **Sanitized logs sample**

  * `artifacts/bodygraph/keys_only.logs.sample`

* **Release bindings**

  * `artifacts/bodygraph/release_bindings.json`

---

## 37.16 Narratives

* **Narratives coverage (router)**

  * `audit/gates/narratives/keys_10x4.table.json` — 10 categories × 4 bands.

* **Aux (EPIC-010 scope; headers-only)**

  * `tests/transport/headers/aux_text_200.snap`

  * `tests/transport/headers/aux_suppression_200.snap`

* *(No Aux HEAD/304 captures in EPIC-010; A7 remains Catalog-only.)*

---

## 37.17 Architecture capture

* **Snapshot root**

  * `audit/gates/arch/_arch/<epic>_<ts>/…`

---

## 37.18 Index & synchronization

* **Human Index**

  * `docs/evidence/INDEX.json` — titles/paths only.

* **Machine Mirror**

  * `artifacts/evidence_index.jsonl` — records-only JSONL.

* **Same-PR rule**

  * Any addition, removal, or relocation in this registry **must** update both Index and Mirror in the same commit/PR.

  * CI enforces:

    * Human↔machine 1:1 parity,

    * canonical JSONL,

    * unknown-key rejection,

    * presence and correctness of path-proofs.

