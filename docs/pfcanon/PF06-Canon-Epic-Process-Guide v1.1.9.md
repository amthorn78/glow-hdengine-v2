# **0\. Front Matter**

**Title:** PF06-Canon-Epic-Process-Guide 

**Version:** v1.1.9

**Status:** Canon

**Effective date**: 2025-12-07

**Last Update Gate:**  BN 8.1.9 Drain A14/15

**tag:** INV-f2ac55d77ce9aacc

## 0.1 Purpose and scope

 This guide defines the epic delivery process for a human \+ pair-programming \+ CodEx workflow. It supplies paste-ready headers, checklists, and prompts; requires an Audit and a Sandbox Build/Test in each epoch; and sets Close to be **PR-first**. **CodEx automatically opens the pull request** and attaches the close pack and the **acceptance tokens (PASS) list**.  
 This is **process guidance only**. It does not constrain execution environments, repository tooling, or any transport or payload bytes (those remain in their canonical homes).

---

## **0.2 Policy and principles**

**PR-first via CodEx.**  
 CodEx opens PRs automatically for each epic slice and pushes:

* Code changes

* Doc-Delta updates (repo docs)

* Both evidence indices:

  * Human: `docs/evidence/INDEX.json`

  * Machine: `artifacts/evidence_index.jsonl`

Implementation Agent analyzes PR bundles and produces PF-canon Doc Deltas.

* An epic **MAY** be delivered in a series of PRs (up to **10 PRs per epic**), each PR carrying a coherent slice of work with its own code \+ evidence parity.

* The **Lead Developer** gates; the **Product Owner** is the sole merger and uses **squash on PASS**.

* Agents do **not** run git and do **not** create PRs.

* The `main` branch is protected with required checks; **squash is the only merge mode**.

* Re-run proofs only on qualifying drift (**green-freeze**).

---

**Evidence parity in the same PR.**  
 Whenever proofs or artifacts change, update in the **same PR**:

* The human Evidence Index (`docs/evidence/INDEX.json`)

* The hash sentinel

* The machine JSONL mirror (`artifacts/evidence_index.jsonl`)

The machine mirror is:

* Records-only

* Canonical JSONL (UTF-8, sorted keys, compact, exactly one trailing LF)

* Strict: rejects unknown keys

Each mirror record includes:

* `artifact_key`

* `role`

* `sha256`

* `size_bytes`

* `produced_at_utc`

* `discovered_physical_path`

* `proof_anchor` (to a co-located path-proof)

---

**A7 proof surface (when applicable).**

* Run HTTP success-path proofs **only** on a cataloged JSON success route from the **Endpoint Catalog**.

* The `/internal/version` endpoint is **ops-only** and **not A7-eligible**.

---

**Single homes.**

* **Public transport & CLI/Reader bytes** → *HDE-CLI-API-Vendor-Ref*.

* **Governance & token semantics** → *HDE-Governance*.

* **Deterministic serializer/idempotence** → *HDE-Math-Spec*.

* **Architecture & single-emitter rules** → *HDE Architecture*.

* **Evidence index & mirror schema** → *HDE-Schemas & Artifacts*.

* **Infra and environment names** → *Glow Infrastructure*.

For HD Engine epics:

* “Prod” is the **production HD Engine service and its production database** as defined in *Glow Infrastructure*.

* PF06 does **not** redefine environment semantics and treats those names as the single home.

When epic docs or QA plans talk about **“prod via Codespaces”**:

* They must treat Codespaces as a **QA console** that talks to that production service and DB, **not** as a prod environment in its own right.

* In this guide, “prod via Codespaces” means:

   “Run commands from Codespaces that talk to the production HD Engine service/DB and store QA artifacts in the repo,”  
   consistent with PF10’s “Prod on Railway, QA via Codespaces” addendum.

---

**Baseline PR tokens (titles-only).**

* `PR_OPENED_OK`

* `TESTS_PASS_OK`

* `DOC_DELTA_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

---

**Deprecation.**  
 The **legacy `card_close` script** is retired and **not authoritative**.

---

## **0.3 Participants and responsibilities**

Implementation Agent (ChatGPT). Runs each epic end to end, prepares CRD-ready drafts, sets up CodEx asks (what, not how), verifies proofs and artifacts, ensures Doc-Delta and both indices are updated in the same PR, and escalates blockers to the Lead Developer. Does not run git or create PRs.

Lead Developer (AI). Defines intent and scope, approves the CRD and Implementation Plan once, performs the gate review on the PR, and otherwise steps out during CodEx execution.

CodEx. Executes in a sandbox, runs Audit and Build/Test, opens the PR automatically using the template, and attaches the close pack and the PASS list. Adapts within scope and reports all changes. Does not read PF docs directly.

Thoth (CRD authority). Owns CRD standards and architecture fit, confirms acceptance tokens and capsule homes by title.

Product Owner (human). Sole merger using squash; signs acceptance on PASS; informs the Scrum Master after merge.

Scrum Master (AI). Informed after merge; records the close; updates boards and the sprint report.

Communication rule. AIs do not contact one another directly. The Product Owner routes all messages.

---

## **0.4 Execution posture and flow (PR-first)**

Lead Developer publishes the Implementation Guide to the Implementation Agent.  
 IA → CodEx: Audit request with explicit formats and any verbatim components or schemas needed.  
 CodEx → IA: Audit report covering capabilities, gaps, and risks.  
 IA drafts the Implementation Plan; Lead Developer approves once and then acts only as PR gate.  
 IA → CodEx: Build instructions plus verbatim components and schemas. CodEx may adapt within scope and must report all changes; returns a detailed change report and artifacts and evidence.  
 IA requests changes or approves.  
 CodEx opens the PR `epic/<epic-id>-<slug>`, pushes code, Doc-Delta (repo docs), the human Evidence Index, the machine JSONL mirror, and the close-pack (`audit/EPIC-<ID>_close_report.md`, `audit/EPIC-<ID>_MANIFEST.json`). The machine mirror is records-only, canonical JSONL, one LF per line, unknown keys rejected, each record with a `proof_anchor`.  
 Lead Developer gate review. Verify PASS tokens; verify A7 proof surface on the cataloged JSON success route (not `/internal/version`); verify env-gate proof and encoding invariance; verify same-PR evidence parity. Verify Endpoint Catalog single home present (`docs/ENDPOINTS_CATALOG.json` \+ `.sha256`) and Reader A7 proof JSON is captured and indexed (human \+ machine, same PR).  
 Product Owner merge. Perform squash merge on PASS and notify the Scrum Master.  
 Closure. IA files the Closure Report; boards and sprint reports updated; suites green-freeze until a qualifying change lands.

Determinism pins  
 Set `LC_ALL=C` and `TZ=UTC` for all capture and CI checks to keep bytes stable.

### **0.4.1 Live QA discovery and RCA (execution requirements)**

For epics that include **Live QA** as part of their acceptance:

1. **Mandatory D0 Discovery artifact (Live QA epics).**

   * Before running any Live QA steps that exercise behavior or vendor flows, the epic **MUST** produce at least one **Discovery artifact** that captures the baseline environment and rails for the Live QA session.

   * At minimum, this Discovery artifact must:

     * Record the effective rails posture and runtime context (for example `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, locale/timezone pins, and any other env variables materially affecting Live QA behavior).

     * Summarize which services and surfaces are expected to be reachable for Live QA (for example “CLI only”, “Reader HTTP routes”, “Railway prod endpoints”) and any known constraints.

     * Capture the initial tool health for key entrypoints (for example CLI/`hdctl` help, test harness availability) so later failures can be distinguished from simple environment misconfiguration.

   * The Discovery artifact is a governed, mechanical file under the epic’s QA tree (titles-only; concrete paths and schemas are owned by other PF documents). It is part of the evidence that the Live QA session was run under known, documented conditions.

2. **Mandatory QA RCA & Doc Delta summary (all Live QA epics).**

   * Every Live QA epic **MUST** produce a **QA RCA & Doc Delta summary** as part of its execution deliverables, regardless of whether large gaps are observed.

   * At minimum, this summary must:

     * Describe the key Live QA findings at a level suitable for future readers (not just raw logs). When no substantial gaps are found, the summary **MUST** still state that fact explicitly (for example “No new PF-Canon deltas identified for this epic”).

     * Map each substantive finding that **does** imply a change in behavior, infra, or process to **explicit PF-Canon doc deltas by title** (for example entries to be added or updated in *HDE Phased Epics*, *HDE-Build Checklist*, *Glow QA Guide*, *HDE-Mechanics Guide*, *Glow Infrastructure*, *HDE-Schemas & Artifacts*).

     * Identify which follow-on cards or epics are expected to carry those PF updates, when they are not covered by the current epic.

   * The QA RCA & Doc Delta summary may live:

     * as a section of `audit/EPIC-<ID>_close_report.md`, **or**

     * as a separate governed artifact referenced from the close report,

   * but it is a **mandatory execution deliverable** for all Live QA epics. The level of detail is proportional to the findings (brief when no deltas, more extensive when multiple PF docs are impacted).

3. **Execution gate.**

   * For Live QA epics, the Close Gate (§3.5) **MUST** confirm:

     * that a D0 Discovery artifact exists for the Live QA session(s), and

     * that a QA RCA & Doc Delta summary exists and, where substantial gaps were found, points to concrete PF-Canon updates.

   * If either the Discovery artifact or the QA RCA & Doc Delta summary is missing, the epic **MUST NOT** be treated as fully accepted, even if code/tests/CI tokens are green.

---

## **0.5 Routing and evidence discipline**

Single homes (titles-only). Transport bytes & CLI/Reader flows → HDE-CLI-API-Vendor-Ref. Token semantics & ops policy (A7, refusal, writers) → HDE-Governance. Canonical JSON, pack/manifest, human Evidence Index and machine mirror → HDE-Schemas & Artifacts. Architecture boundaries & single-emitter rules → HDE Architecture. Do not restate bytes, schemas, or token tables here.

Governed locations only. Evidence artifacts and persisted logs must live under `artifacts/**` and `docs/**`. Transient/generator paths are disallowed. Header snapshots are normalized (lower-cased names; verbatim values), LF-terminated.  
 Path normalization. Proof files must live under governed paths (`artifacts/**` and `docs/**`). Transient/generator paths (e.g., `codex/out/**`) are not authoritative and MUST NOT be indexed; relocate before gating.

Same-PR parity (mandatory). When proofs or artifacts change, update all three in the same PR that carries the change:

* the human Evidence Index `docs/evidence/INDEX.json`,

* the hash sentinel `docs/evidence/INDEX.sha256` (merge-gating), and

* the machine mirror `artifacts/evidence_index.jsonl`.

CI enforces 1:1 join (human↔machine), and blocks on missing/mis-indexed items.

Mirror hygiene (PF12 schema). The mirror is records-only canonical JSONL (UTF-8, compact, exactly one LF), unknown-keys rejected, ASCII field order, sort-before-write, single mirror file. Each record must include: `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor` (transcript anchor \+ co-located path-proof).

Ops rails refusal proof (closed-rails). Capture a single-file refusal proof at `artifacts/proofs/ops_refusal_proof.txt` containing: required headers, one blank line, and an LF-terminated numeric-free JSON body. This artifact is governed by HDE-Governance (refusal/writers policy; tokens by title) and indexed per HDE-Schemas & Artifacts (mirror/`proof_anchor`, records-only JSONL, one LF, unknown-key reject).

Merge gate (path-proofs required). Every indexed artifact must have a co-located path-proof referenced by `proof_anchor`; CI blocks the merge if any path-proof is missing or mis-indexed. Same-PR parity (human index \+ hash sentinel \+ machine mirror) remains mandatory.

Proof surface routing (A7). Success-path proofs run only on a cataloged JSON success route (Endpoint Catalog). The `/internal/version` ops surface is excluded from A7 and governed by policy in Governance. Capture GET, HEAD, 304 (304 omits both Content-Type and Content-Length), required `Vary: Authorization, Accept-Encoding`, and encoding-invariance. Env-gate headers proof is required. (Titles-only pointers; bytes live in PF05; evidence lives in PF12.)

Endpoint Catalog single home (titles-only). The only authoritative Catalog path is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256`. The Catalog lists JSON success routes only, each with an env-gate; all `/internal/*` routes are excluded. A7 proofs must run on a Catalog success route, and an env-gate headers proof is required.

Reader A7 proof JSON (machine-checkable). Epics that ship Reader A7 must produce a single proof JSON (records-only, canonical) containing: `route_path`, `env_gate`, GET/HEAD/after-304 header captures, `ETag`, `vary_has_auth`, `vary_has_accept_encoding`, and `encoding_invariance_ok`. Proof JSON and indices update occur in the same PR.

CRD routing. Thoth receives the CRD only. Keep process artifacts (PLAN/CRD/Doc-Delta) titles-only and route to single homes for bytes/evidence.

Cross-doc references. Use titles only for all external references; do not duplicate transport bytes, schemas, or acceptance rosters in this guide.

---

## **0.6 Discipline**

### **0.6.1 Canon-first planning**

Implementation Agents **MUST** treat PF-Canon as the primary source of facts for epic planning and QA.

Before drafting any QA Plan or Implementation Plan for a Live QA epic, they **MUST**:

* Read **Glow Infrastructure**, **HDE-Build Notes**, **Glow QA Guide**, and **HDE Phased Epics** (by title) to collect:

  * environment and infrastructure facts,

  * QA tokens, and

  * epic D-goals and exclusions.

* Use canonical infra/env values (for example, production service name, base URL, and DB instance/schema) from those documents directly, instead of treating them as unknowns.

Implementation Agents **MUST NOT** treat canonical infra/env details that PF-Canon already defines (for example, prod base URL and DB for the HD Engine) as PO inputs unless PF-Canon explicitly marks them **OPEN/TBD**.

Any QA Plan or Implementation Plan that asks the PO to “provide” such a value **without** citing an OPEN/TBD gap in PF-Canon is **non-conforming** and must be corrected before use.

---

### **0.6.2 Rails and environments (closed-rails vs open-rails QA)**

QA Plans **MUST** distinguish between:

* **Closed-rails determinism checks** that run locally with rails closed  
   (for example, serializer and bundle determinism jobs), and

* **Open-rails production checks** that run from a console  
   (for example, Codespaces) against the production HD Engine service and DB  
   as defined in **Glow Infrastructure** and clarified in **HDE-Build Notes** (titles only).

Determinism pins (for example locale/time settings) apply to determinism-sensitive jobs.

When a step is explicitly described as “prod via Codespaces,” the plan **MUST**:

* assume an open-rails posture sufficient to reach prod, and

* prove determinism via repeatable runs and evidence, **not** by pretending that rails are closed.

---

### **0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)**

For Live QA epics:

* **Prod behavior runs in a prod-facing environment.**  
   Any D-goal that is about behavior (for example compat math, narrative generation, vendor ingest, “full product payload” for a pair) **MUST** define a primary **exercise context** that can reach the production HD Engine service and DB as defined in **Glow Infrastructure**.  
   Examples include:

  * a terminal with `hdctl` configured to call the production base URL, or

  * an admin GUI in a browser hitting a Railway route.

* **Codespaces is a console and artifact sink, not the prod executor.**  
   Codespaces **MAY**:

  * run offline tools against a checkout of the same code/commit as prod,

  * receive and store artifacts (logs, JSON, headers, transcripts) under `audit/qa/<epic-id>/...`, and

  * run offline validation (for example `python -m json.tool`, `cmp`, `sha256sum`) against those artifacts,

* but Codespaces **MUST NOT** be treated as “where prod runs” unless the step explicitly:

  * describes how the commands in Codespaces are reaching the production service over the network, and

  * uses that connection as the exercise context.

* **Behavior vs artifact phases.**  
   Live QA steps that refer to behavior **MUST** separate:

  * a **behavior run phase** (where the behavior is exercised in a prod-facing environment), and

  * an **artifact capture & analysis phase** (where artifacts from that run are copied or uploaded into the Codespace under `audit/qa/<epic-id>/...` and analyzed offline).

* The QA Plan **MUST** be clear about both phases for each such step.

* **Codespaces-only runs are local smoke checks.**  
   Steps that run `hdctl` or other logic **purely inside Codespaces** (for example under closed rails with no network) **MAY** be included as local smoke checks but **MUST NOT** be used to satisfy prod behavior tokens.

   When a token is about prod behavior, its satisfaction **MUST** be tied to a prod-facing behavior run as described above, with artifacts captured under `audit/qa/<epic-id>/...`.

---

### **0.6.4 PO Live QA vendor-first scope**

For epics that include **PO-run Live QA** sessions:

* **Purpose.**  
   PO Live QA is a **vendor-first** activity. Its primary and explicit goal is to exercise live vendor behavior against the production HD Engine and to capture mechanical evidence of that behavior.

* **What belongs in PO Live QA.**  
   Steps in a PO Live QA session **MUST** be scoped to vendor flows, including (as applicable to the epic):

  * vendor-backed BodyGraph resolution (for example `bg:resolve --source=vendor` in dry-run or controlled modes),

  * vendor-backed compat calculations (for example compat via vendor-backed inputs or the Admin bundle path once defined by other PF docs), and

  * vendor error conditions and edge cases (for example malformed input, missing data, timeouts) that the epic chooses to exercise.

* **What does not belong in PO Live QA.**  
   Steps whose only purpose is:

  * proving connectivity (for example `/internal/version` identity pings), or

  * re-running determinism, serializer/guard, or sanity checks that are already covered by CI/QA/infra,

* **MUST NOT** be treated as part of the PO’s Live QA workload.  
   These checks remain **CI/QA/infra** responsibilities and may be referenced as pre-work or prerequisites, but they are not, by themselves, a reason to convene a PO Live QA session.

* **Codespaces rails in PO Live QA.**  
   In the context of PO Live QA:

  * Codespaces is, by default, an **artifact sink and offline analysis console** (see §0.6.3).

  * Codespaces **MAY** temporarily open rails (for example setting `SAFE_MODE=0`, `ALLOW_NETWORK=1`, base URL pointing to production) **only when**:

    * the goal of that step is to exercise a live vendor flow as described above, and

    * the rail-opening is documented (env vars set, commands logged, and artifacts captured under `audit/qa/<epic-id>/logs/`).

  * For non-vendor behavior (serializer determinism, guard proofs, sanity pipeline), Codespaces **MUST NOT** be used as a surrogate “prod” environment in PO Live QA; those checks belong to CI/QA/infra.

Plans or runs that:

* assign non-vendor checks to the PO’s Live QA workload, or

* treat vendor-neutral smoke checks as PO Live QA,

are **non-conforming** and must be corrected by moving those checks into CI/QA and keeping the PO session focused on vendor behavior.

---

### **0.6.5 Fail-closed to spec gap**

If, during planning, PF-Canon appears ambiguous or incomplete:

* Implementation Agents **MUST** treat the affected check as **blocked by a spec gap**,

* capture enough evidence to describe the gap, and

* route it into **Build Notes** and/or **HDE Phased Epics** as a documented issue,

instead of improvising new rails, redefining environment semantics, or asking the PO to guess.

---

### **0.6.6 Filesystem naming (directories)**

PF-Canon and QA docs **MUST** use lowercase directory names in all canonical path examples and requirements.

In particular:

* Repository and artifact directories under the project root (for example `docs/`, `artifacts/`, `audit/qa/`, `schemas/`) and epic-specific QA directories (for example `audit/qa/hde-epic017/logs/`) **MUST** be spelled in lowercase ASCII.

* New specs, QA Plans, and evidence path examples **MUST NOT** introduce mixed-case or uppercase directory names (for example `Audit/QA/...` or `Audit/Qa/...`). Any remaining mixed-case directories are treated as legacy drift and **must** be normalized to the lowercase convention in remediation work, not copied forward into new epics.

This rule applies to **directory components only**; file names and extensions continue to follow their existing conventions unless otherwise governed by other PF documents.

---

### **0.6.7 Mechanical evidence (Live QA)**

For any Live QA epic, the QA Plan and Implementation Plan **MUST** treat evidence as mechanical and step-explicit:

* **Per-step evidence expectations.**  
   Every Live QA step in the QA Plan **MUST** include explicit mechanical evidence expectations: the commands to run and the expected artifacts (paths and filenames) under the canonical QA root `audit/qa/<epic-id>/...` for that step.

   It is not sufficient to say “take notes” or “observe output”; each step **must** name at least one concrete file it will produce.

* **PO actions → artifacts.**  
   Every PO action in a Live QA run (for example, running a CLI command, issuing a curl, changing rails, or approving a QA slice) **MUST** result in at least one inspectable artifact under `audit/qa/<epic-id>/...` (for example, a log, tree snapshot, or summary file).

   If a PO action does not currently produce an artifact, the QA Plan **must** add a mechanical capture command (for example, `echo` or a script) so the step becomes observable.

* **Mechanical, not manual.**  
   Live QA evidence files **MUST** be produced by commands (shell, scripts, CLI tools) rather than manual editing.

   Human notes are allowed only if they are written via mechanical commands into files under `audit/qa/<epic-id>/...` and treated as governed artifacts; free-form, untracked notes are **not** considered evidence.

Plans or runs that:

* omit per-step mechanical evidence expectations, or

* include PO actions without at least one corresponding artifact under `audit/qa/<epic-id>/...`,

are **non-conforming** and must be corrected before the Live QA work is considered acceptable.

---

### **0.6.8 Operational guardrails**

* **No background work.**  
   Agents do not perform unseen or open-ended work outside the documented epic process. All outputs must be paste-ready, reviewable, and traceable to PF-Canon and epic artifacts.

* **No manual git.**  
   Agents do not run git, do not create branches, and do not push commits.

* **No manually created PRs by agents.**  
   Pull requests are created by CodEx (for main epic slices) or by the PO in the CodEx UI as defined elsewhere in this guide; agents do not create PRs directly.

* **Main is protected.**  
   The `main` branch is protected; squash merge on PASS is the only close path for epic work.

---

## **0.7 QA branches posture**

Purpose. Define how to verify evidence and transport posture without touching production code.

Scope (evidence-only)

Allowed changes:  
 Indices & sentinels: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`.

Endpoint Catalog (single home): `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`.

A7 proofs (headers-only): `artifacts/proofs/success_get.txt`, `…/success_head.txt`, `…/success_304.txt`, `…/success_writers_errors.txt`, `…/success_encoding_invariance.txt`, `artifacts/proofs/endpoints_env_gate_proof.log`.

Ops (rails closed) refusal proof: `artifacts/proofs/ops_refusal_proof.txt` (headers → blank line → LF-terminated numeric-free JSON body).

CLI parity artifacts: `artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`.

DB posture (dev acceptable): `artifacts/runtime/env_matrix.snapshot.json` (singleton; titles-only, schema in HDE-Schemas & Artifacts), `artifacts/runtime/env_connectivity.snapshot.json`, `artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`.

BodyGraph evidence: `artifacts/bodygraph/source_selection.snapshot.json`, `artifacts/bodygraph/source_invariance/{ab.json,ba.json,summary.json}`, `artifacts/bodygraph/refresh_policy.snapshot.json`, `artifacts/bodygraph/metrics.snapshot.json`, `artifacts/bodygraph/keys_only.logs.sample`.

Forbidden: changes under app/service code, migrations/DDL writers, runtime configs, or vendor rails. No endpoint behavior changes.

APPEND — Path normalization. Transient/generator paths (e.g., `codex/out/**`) are forbidden as sources for governed proofs; relocate into `artifacts/**` / `docs/**` before indexing.

Branch and PR  
 Branch naming suggestion: `qa/<epic-id>-<slug>`.  
 Open a PR using §4.5 PR template — evidence-only QA. Keep all evidence and indices in the same PR (see §0.2 parity rule).

Determinism pins  
 Run all captures and CI with `LC_ALL=C`, `TZ=UTC` to keep bytes stable.

CI posture (diff-scoped)  
 CI validates governed files changed in the QA branch. At minimum:

* Mirror schema check (records-only JSONL, sorted keys, one LF, unknown keys rejected).

* Final-LF check on governed text artifacts.

* Appendix-D ↔ mirror 1:1 parity and `proof_anchor` path-proof linkage.

* A7 headers proofs on a cataloged JSON success route (not `/internal/version`), including GET/HEAD/304, `Vary: Authorization, Accept-Encoding`, and encoding-invariance of identity and effective length.

* Writers/errors posture headers: `no-store`; JSON errors, no ETag.

* When a QA branch or plan claims to exercise **prod via Codespaces** for an HDE epic, it **must** include at least one simple **prod handshake** that proves the commands are talking to the canonical production HD Engine service and DB (as defined in Glow Infrastructure). A typical handshake is a `curl` to the production HD Engine base URL’s `/internal/version` endpoint from within Codespaces, with the full response captured under `audit/qa/<epic-id>/logs/`. QA that omits this handshake is treated as **underspecified** until the handshake and its artifact are added.【13:WCXnEc3R2LFdFyBrPKcjx9†file-WCXnEc3R2LFdFyBrPKcjx9†L3-L7】

* Rails default: CI/test harness runs **CLOSED** by default; any job that opens rails must pin policy and attach evidence in the same PR.

Acceptance (titles only)  
 `QA_EVIDENCE_ONLY_OK` — branch contains evidence updates only (no production code).  
 `QA_CI_DIFF_SCOPED_OK` — CI restricted to changed governed files passed.

---

# 1\) EPIC PLAN → CRD (Lead Dev) 

## **1.1 Workflow at a glance**

### **1.1.1 Standard epic flow**

Before applying the steps below, every epic **MUST** perform a **canon inventory**:

* Read, by title, the current **Glow Infrastructure**, **HDE-Build Notes**, **Glow QA Guide**, and **HDE Phased Epics** entries that apply to this epic.

* Record, in the PLAN context header or adjacent notes, the key environment and infra facts, relevant QA tokens, and D-goals/exclusions discovered there.

* If any required fact appears missing or ambiguous, mark it as a **spec gap** per §0.6.5 (blocked-by-spec) instead of treating it as a PO input or improvising rails.

Only after this canon inventory is complete should the PLAN header and CRD be drafted.

1. **PLAN header (machine-ready).**  
    Draft the PLAN machine header as a single post.

2. **CRD with approved scope.**  
    After one review, issue the CRD with the approved scope and acceptance tokens **by title only** (for example `A3`, `A4`, `A7`); do **not** list bytes or payload shapes in the CRD.

3. **Code capsules before IP.**  
    Finalize code-capsules before IP approval; capsules **freeze at IP**.

4. **CodEx PR creation.**  
    CodEx runs **Audit \+ Sandbox Build/Test**, then opens the PR automatically using the standard template. In that PR, CodEx pushes, in a single slice:

   * Code

   * Doc-Delta (repo docs)

   * Human Evidence Index (`docs/evidence/INDEX.json`)

   * Machine JSONL mirror (`artifacts/evidence_index.jsonl`)

5. CodEx also attaches:

   * The close pack

   * The PASS token list

6. **Lead Developer gate.**  
    Lead Dev gates the PR by verifying, as applicable:

   * PASS token list is consistent and complete

   * A7 proof surface is correct (cataloged JSON success route only)

   * Env-gates and encoding invariance are respected for A7 proofs

   * 1:1 Evidence Index ↔ machine mirror parity with path-proofs

7. **PO merge and green-freeze.**  
    The Product Owner is the sole merger and uses **squash-merge on PASS**. After merge:

   * Scrum Master is informed

   * Suites are green-freeze unless a qualifying change lands

---

### **1.1.2 Multi-PR epics**

For some epics (for example EPIC017 and similar Calcination/Separation passes):

* The work may be split into a **series of PRs** (up to **10 PRs per epic**).

* Each PR must carry a **self-contained slice** with code \+ Doc-Delta \+ evidence.

* The **PR-first pattern and same-PR parity** (code \+ docs \+ Evidence Index \+ machine mirror) apply to **each PR**.

* **Epic-level acceptance** (as recorded in *HDE Phased Epics*) occurs **only after all required PRs for that epic have merged**.

---

### **1.1.3 “Prod via Codespaces” requirements (PLAN/CRD)**

When a PLAN or CRD for an HDE epic expects Live QA **“in prod via Codespaces”**, it must:

1. **Name prod surfaces by title.**

   * Name the production HD Engine service and base URL, and the production DB instance/schema by **title**, routing to *Glow Infrastructure* as the single home for those names.

   * Do **not** invent new environment labels.

2. **Clarify Codespaces role.**

   * State explicitly that **Codespaces is a QA console** that runs CLI/HTTP commands against that production service and DB.

   * Codespaces is **not** a prod environment in its own right.

3. **Describe the prod handshake & artifact location (identity-only).**  
* Describe, at a high level, the prod identity handshake step and where its artifact will live, for example:  
   *“Step 0: curl the production `/internal/version` endpoint from Codespaces and store the output under `audit/qa/<epic-id>/logs/` before running deeper QA.”*  
* Treat this handshake as an identity/pre-flight check only: it proves that the console can reach the production HD Engine, and records which `engine_tag`, `release_id`, commit, and `invocation_tag` are live at the time of QA.  
* Live QA plans MUST NOT use `/internal/version` to satisfy any D-goals related to behavior (for example compat math, narratives, vendor ingest, admin bundle). Those goals require separate behavior steps that exercise prod-facing behavior surfaces and produce their own artifacts under `audit/qa/<epic-id>/...`.

PLAN/CRD entries that refer to **“prod via Codespaces”** without these clarifications are **incomplete** and must be updated before the epic moves into implementation or Live QA.

For epics that intend to run **vendor-first Live QA** (as described in §0.6.4 and §1.1.6) using the “prod via Codespaces” pattern above, the PLAN/CRD **MUST ALSO** ensure that:

* The epic’s acceptance roster in **HDE Phased Epics** explicitly declares this posture by title (for example, an acceptance row that states that Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under `audit/qa/<epic-id>/...`), and

* The Live QA Plan includes at least one **vendor-focused step** that:

  * uses or references the prod identity handshake described above (for example the `/internal/version` artifact under `audit/qa/<epic-id>/logs/`) to anchor which engine instance is under test, **and**

  * demonstrates a **vendor-backed end-to-end flow** (for example vendor-backed resolve or compat) executed against the production HD Engine service, with its own mechanical artifacts captured under `audit/qa/<epic-id>/...` as required by §1.1.4–§1.1.6.

This identity+vendor step does **not** change the identity-only semantics of `/internal/version`: the handshake remains a pre-flight proof of “which engine is live,” while the vendor-backed flow in the same step (or tightly paired steps) is what satisfies the vendor behavior portion of the D-goals and is recorded in the PF20 acceptance roster.

---

### **1.1.4 Live QA mechanical evidence expectations**

For **Live QA epics**, the PLAN and CRD must make the **mechanical evidence expectations explicit**:

* For each Live QA step in the QA Plan, specify:

  * The **commands to run** (CLI/HTTP), and

  * The **concrete artifacts** (paths and filenames) that will be written under the canonical QA root:

    * `audit/qa/<epic-id>/...`

* Ensure that **every PO action** in the Live QA run produces at least one such artifact.

PLAN/CRD authors must:

* Reference §0.6 “Discipline” for the canonical requirements on mechanical evidence and directory casing.

* Treat any PLAN/CRD that describes Live QA **without per-step mechanical evidence expectations under** `audit/qa/<epic-id>/...` as **incomplete**; it must be corrected before Live QA starts.

### 1.1.5 Live QA behavior vs artifact pattern

For Live QA steps that exercise **behavior** (for example compat, narratives, vendor ingest, admin bundle), the PLAN and CRD **MUST** follow a two-part pattern and make both parts explicit:

1. Behavior run (prod-facing).

   * Describe **where** the behavior is exercised: for example, an admin CLI run on a machine that can reach the production HD Engine base URL, or an admin GUI action in a browser hitting a Railway route.

   * Specify the exact **inputs** and any expected **outputs** for that behavior run.

   * If possible, include a prescribed way to capture outputs at the behavior environment (for example, saving JSON response bodies or logs to files that will later be moved into the repo).

2. Artifact capture & analysis (Codespaces).

   * Provide fenced commands for Codespaces that:

     * Create or confirm the appropriate subdirectories under `audit/qa/<epic-id>/...` (for example `audit/qa/<epic-id>/d2-env/`, `.../d3-cli-guards/`, `.../logs/`).

     * Copy or upload the artifacts from the behavior environment into the Codespace (for example via `scp`, `gh` upload, or another documented mechanism).

     * Run offline validation against those artifacts (for example `python -m json.tool`, `cmp`, `sha256sum`, header checks), writing results to new files under `audit/qa/<epic-id>/...`.

     * Append any human-readable notes via mechanical commands (for example `echo` into `qa_notes.md`), not manual editing.

Plans **MUST NOT** conflate these two phases or imply that “running hdctl in Codespaces” alone is sufficient to satisfy prod behavior D-goals. Codespaces is the **artifact sink and analysis console**; the behavior itself must be exercised in a prod-facing environment, and the artifacts from that run must be brought into `audit/qa/<epic-id>/...` for analysis and evidence.

### 1.1.6 PO Live QA vendor-first scope

When a PLAN or CRD describes **PO Live QA** (a Live QA session that requires PO time), it **MUST**:

* **Declare PO Live QA as vendor-first.** Clearly state that PO Live QA for this epic is a short, focused session whose primary goal is to exercise **live vendor behavior** against the production HD Engine and capture mechanical evidence of that behavior.

* **Label vendor vs non-vendor steps.** For all Live QA steps, classify them into:

  * **Vendor-focused** (class 3): steps that exercise vendor-backed flows (for example vendor-backed BodyGraph resolution, compat, vendor error behavior).

  * **Ops/identity** (class 1): connectivity and identity checks (for example `/internal/version`).

  * **Internal functional/determinism** (class 2): serializer/guard/sanity/determinism checks that can run under CI/QA without involving the PO.

* **Identify the PO workload explicitly.** Identify the subset of Live QA steps that the PO is expected to run in a Live QA session:

  * This subset **MUST** consist only of vendor-focused steps.

  * Ops/identity and internal functional/determinism steps **MUST** be marked as **preconditions or CI/QA responsibilities**, not PO Live QA workload. They may be referenced as “pre-flight / internal” work but not scheduled into PO’s Live QA time.

* **Tie vendor steps to mechanical vendor evidence.** For each vendor-focused PO step:

  * Specify the **behavior run context** (prod-facing environment), per §1.1.5.

  * Specify the **artifact capture & analysis** commands in Codespaces, including the paths and filenames under `audit/qa/<epic-id>/...` where vendor-related artifacts will be stored (for example JSON bodies, logs, error responses).

  * Ensure that artifacts for vendor steps are clearly identifiable as vendor evidence (for example via a vendor-specific subdirectory or filename convention) so that they can be referenced from epic acceptance in *HDE Phased Epics* and from QA tokens in *Glow QA Guide* (titles-only).

Plans that:

* describe PO Live QA without labeling vendor vs non-vendor steps,

* assign ops/identity or internal determinism steps to the PO’s Live QA workload, or

* omit mechanical vendor evidence expectations for PO-run vendor steps under `audit/qa/<epic-id>/...`

are **incomplete** and must be corrected before PO Live QA is scheduled.

### **1.1.7 D3 CLI guard runs — CI vs open-rails Live QA**

Live QA planning **MUST** explicitly distinguish between:

1. **CI / closed-rails D3 guard runs (authoritative).**

   * D3 CLI guard tokens (for example the serializer and emitter guard tokens defined by title in the HDE-Build Checklist and HDE-Mechanics Guide) are **authoritatively satisfied by CI and closed-rails runs**.

   * The canonical D3 acceptance condition is: guard tools run under the closed determinism rails (for example `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` as defined by other PF docs) and **exit successfully**, with their evidence captured and indexed according to those documents.

   * Live QA Plans **MUST NOT** assume that an open-rails Live QA environment is responsible for re-satisfying these D3 guard tokens; instead, they **MUST** point to the CI/closed-rails evidence when claiming D3 acceptance.

2. **Open-rails Live QA guard runs (optional, env-enforcement only).**

   * In an intentionally **open-rails** Live QA environment (for example, a Codespace used for prod-facing behavior tests and artifact capture per §0.6.3–§0.6.4), running the CLI guard tools is **optional** and is treated as an **env-enforcement check only**.

   * In this context, a guard run that **fails solely due to env mismatch** (for example, exit code 1 because the environment is open rails instead of the closed determinism rails expected by CI) **MUST NOT** be treated as:

     * a wiring bug, or

     * a failure to satisfy D3 guard tokens.

   * Live QA Plans **MUST**:

     * State explicitly when a guard step is being run in an open-rails environment “for information only” (to confirm that guards enforce env pins), and

     * Tie D3 guard tokens back to the CI/closed-rails runs, not to these open-rails checks.

3. **Effect on PO Live QA.**

   * For PO-run Live QA sessions in open-rails environments:

     * Guard runs, if present, **MAY** be used to demonstrate that env pins are enforced,

     * Guard failures due solely to env mismatch **MUST NOT** block PO Live QA or be interpreted as D3 token failures, and

     * The Live QA Plan **MUST** refer back to the CI/closed-rails guard evidence as the source of truth for D3 acceptance.

Plans that:

* treat open-rails guard failures as D3 token failures, or

* omit the CI vs open-rails distinction for guard steps,

are **non-conforming** and **MUST** be corrected so that D3 acceptance is clearly anchored in CI/closed-rails runs, with open-rails guard runs documented as optional env-enforcement checks only.

### **1.1.8 CLI commands in QA Plans (canon-backed only)**

Live QA Plans frequently use `hdctl` or other CLI commands as entrypoints (for example D0 “CLI presence” checks, D1 error-stream checks, or vendor-facing steps).

To keep those steps aligned with PF-Canon and avoid inventing new CLI requirements, the following rules apply:

* **CLI bytes live in the CLI spec.**

  * All CLI commands, flags, and subcommands used in QA Plans **MUST** be traceable to at least one of:

    * *HDE-CLI-API-Vendor-Ref* (the single home for CLI/Reader bytes),

    * a governed CLI test harness or script in the repo, or

    * a CodEx audit snippet that lists the CLI shape as discovered behavior for this repo.

  * QA Plans **MUST NOT** introduce new CLI spellings or flags “by habit” (for example a generic `--version` check) that are not present in those sources.

* **D0 CLI presence checks: minimal and spec-backed.**

  * When D0 includes a “CLI presence” or “CLI baseline” step, that step **MUST**:

    * use command shapes that are explicitly documented as supported (for example a shell-level presence check or a help/usage invocation taken from the CLI spec or CodEx audit), and

    * phrase the Expected Outcome in terms of **what PF-Canon actually requires** (for example “CLI is installed and runnable under the pinned rails for later steps”), not in terms of extra behavior that is not a canonical requirement.

  * D0 steps **MUST NOT** assert stronger expectations (for example “must print a version string” or a particular banner) unless those behaviors are **explicitly tied** to PF-Canon requirements or epic acceptance tokens **by title**.

* **Plan authors: copy, do not invent, CLI shapes.**

  * Implementation Agents and QA Plan authors **MUST** derive every CLI command used in a QA Plan from:

    * the CLI spec,

    * an existing test or harness, or

    * a CodEx audit report for this repo,  
       and **MUST** copy those shapes exactly (command name, flags, argument structure), adjusting only concrete values like file paths or epic IDs.

  * Any time a Plan adds a new CLI usage that is not already present in those sources, the Plan **MUST** treat that as a **spec gap** and either:

    * update the CLI spec first, or

    * remove or replace the command with a canon-backed equivalent.

* **Plan reviewers: non-traceable CLI commands are blocking.**

  * During PLAN/CRD review for epics that include CLI steps (especially Live QA epics), Lead Dev and QA reviewers **MUST**:

    * spot-check CLI commands in the Plan against *HDE-CLI-API-Vendor-Ref*, tests, or CodEx audit output, and

    * treat any CLI command or flag that **cannot be traced** to one of those sources as a **blocking issue**.

  * Plans with non-traceable CLI commands **MUST** be corrected before approval:

    * either by replacing the command with a canon-backed usage, or

    * by first adding the missing behavior to the CLI spec and tests, and then updating the Plan to match.

* **Interaction with other sections.**

  * This section refines §0.6.1 “Canon-first planning” for CLI usage: CLI behavior in QA Plans must come from the CLI spec, tests, or CodEx audit, not from generic assumptions.

  * It complements §1.1.5–§1.1.7 by ensuring that:

    * CLI steps used for behavior runs and artifact capture follow **documented** command shapes, and

    * D3 CLI guard runs in Live QA (when present) still respect the CI vs open-rails distinction while using canon-backed commands.

Plans that:

* rely on CLI commands or flags that are not present in any PF-Canon CLI spec, test harness, or CodEx audit, or

* assert Expected Outcomes that go beyond PF-Canon requirements without naming the corresponding tokens or docs by title,

are **non-conforming** and **MUST** be revised before PLAN/CRD approval or Live QA scheduling.

### **1.1.9 Token fidelity rails for QA tokens and evidence**

This section defines **process rails for QA tokens** in epic planning and review. It applies to any:

* Implementation Plan

* QA Plan

* epic record (including acceptance maps and manifests)

that **introduces or consumes QA Acceptance Tokens**.

It does **not** redefine token semantics or schema; those remain in:

* *Glow QA Guide* (QA Acceptance Tokens registry and usage),

* *HDE-Governance* (token semantics and ops policy),

* *HDE-Schemas & Artifacts* (evidence schemas and mirror), and

* *HDE-Phased Epics* (epic-level D-goals and token rosters).

PF06’s role is to define how plans and reviews **must use and enforce** those single homes.

#### **1.1.9.1 PF23 audits vs PF19 token semantics**

* PF23 reality audits are **optional per-epic surfaces**; their scope is decided per epic or plan.

* Decisions to **waive, narrow, or skip** PF23 audits for a plan or epic are **local to that plan** and **MUST NOT** be interpreted as:

  * relaxing PF19 QA token semantics or names,

  * relaxing PF12 evidence or mirror rules, or

  * relaxing PF20 D-goal/token roster requirements.

* QA token names and semantics **MUST** still come from the QA Acceptance Tokens registry in *Glow QA Guide* and related PF docs (titles only), regardless of PF23 audit scope.

Any plan text that implies “PF23 is out of scope, so token/evidence strictness is optional” is **non-conforming** and must be corrected.

#### **1.1.9.2 Token/evidence matrix (mandatory for token-touching work)**

For any Implementation Plan, QA Plan, or epic record that **adds or consumes QA tokens**, reviewers **MUST** ensure a **token/evidence matrix** exists before approval.

At minimum, this matrix has one row per token in scope and the following fields (titles and paths only):

* **`pf19_token_name`** — the QA Acceptance Token name as defined in the *Glow QA Guide* registry.

* **`acceptance_map_name`** — the token name used in the epic’s acceptance map/manifest; **MUST match** `pf19_token_name` (no local aliases).

* **`tests`** — unit/integration tests that exercise the token’s behavior (by module or test id).

* **`ci_jobs`** — CI jobs that enforce the token under closed rails, when applicable.

* **`live_qa_steps`** — Live QA steps that demonstrate the token (if any), by step id/name, pointing to `audit/qa/<epic-id>/...`.

* **`evidence_artifacts`** — governed artifacts paths produced by those tests/steps (for example under `artifacts/**` or `audit/qa/<epic-id>/...`).

* **`index_and_mirror_entries`** — how those artifacts appear in the Evidence Index and machine mirror (artifact keys and token tags only).

Token-touching plans **MUST NOT** be approved while any token row is:

* missing,

* marked as “e.g.”, “TBD”, or similar placeholder, or

* only implicitly described in prose without a concrete row.

Such gaps are **blocking** for PLAN/CRD approval and must be resolved or explicitly scoped into new epics **before** proceeding.

#### **1.1.9.3 PF19 as single home for QA token names; epics only consume them**

* QA Acceptance Tokens are **centrally defined** in the QA Acceptance Tokens registry in *Glow QA Guide* and related PF docs (titles only).

* Epic-level artifacts (for example *HDE-Phased Epics* records, acceptance maps, manifests, PF10 addenda, and implementation plans):

  * **MUST reference tokens by their PF19 names only**, and

  * **MUST NOT invent local token names or synonyms** for the same semantics.

* If an epic requires a **new token**:

  * The need **MUST** be recorded as a PF19 doc delta (NEW CANON or CANON UPDATE, titles only).

  * That doc delta **MUST** be accepted and the token added to the PF19 registry **before** the epic is considered token-complete.

If an epic-specific remediation guide or approval has already chosen a token name for a behavior, plans and maps **MUST** use that name and treat PF19 as the drainage target; they may not introduce competing names for the same behavior.

#### **1.1.9.4 No silent downgrade of token/evidence blockers**

Once a reviewer has identified any of the following as **blocking**:

* open “e.g.” or “TBD” token names,

* use of tokens not present in the PF19 registry (or in approved PF19 doc deltas),

* missing rows in the token/evidence matrix, or

* incomplete wiring from tokens to tests/CI/Live QA/evidence/index/mirror,

that blocker:

* **MAY NOT** be downgraded to “non-blocking” in a later review for the **same** plan text or epic record, and

* **MAY ONLY** be cleared when:

  * the plan or epic text has been updated to resolve the issue (for example, names made normative, matrix completed), **or**

  * PF-Canon has been updated (for example, PF19 adding or changing the token definition).

Any downgrade of such a blocker **MUST** reference the specific change (plan diff or PF doc change) that resolved it. A change in reviewer interpretation or time alone is not sufficient.

#### **1.1.9.5 Scope waivers are explicit and non-transitive**

When the Product Owner or governance chooses to **waive or narrow** a canon requirement for a particular plan (for example, “PF23 audits are out of scope for this plan”):

* The waiver **MUST** be recorded in that plan as a **local scope directive** (for example “PF23 audits are not part of this plan’s workflow”), and

* The plan **MUST** state explicitly that other rails remain fully in force, including:

  * PF19 QA tokens,

  * PF12 evidence rules and mirror schema,

  * PF20 D-goals and token rosters, and

  * PF09 CI/QA rails that apply.

Such waivers **MUST NOT** be interpreted as permission to relax token naming, acceptance mapping, or evidence wiring. PF19/PF12/PF20/PF09 rules still apply unless they, too, are explicitly and locally waived by title.

#### **1.1.9.6 Re-ground before asserting “no canonical token name”**

Before any reviewer or plan text asserts that “no canonical token name exists yet” for a QA behavior, they **MUST**:

1. Re-check the QA Acceptance Tokens registry in *Glow QA Guide* for an existing token that covers that behavior.

2. Re-read any epic-specific approvals or remediation guides (for example, compat defect remediation guides for EPIC020) that might already have **chosen a token name and semantics** for that behavior.

If such an approval defines a token name, plans and acceptance maps **MUST**:

* treat that name as authoritative for the epic, and

* route future PF19 updates to add or refine that token, instead of inventing a new name.

#### **1.1.9.7 Plan and epic approval require token fidelity to be resolved**

For any plan or epic that touches QA tokens:

* Token names **MUST** be final (either existing PF19 names or names backed by explicit PF19 doc deltas).

* The token/evidence matrix **MUST** be complete, with each token wired to its tests, CI jobs, Live QA steps (if applicable), evidence artifacts, and index/mirror entries.

* Any recognized token gaps (missing PF19 entries, unclear semantics, or incomplete matrix fields) **MUST** be:

  * captured as PF19/PF20 doc deltas (titles only), and

  * treated as part of the epic’s scope and work, **not** as detached “future governance work.”

Plans or epic records that still contain open questions like:

* “which token name do we use here?”

* “these tokens are examples only,” or

* “token wiring TBD later”

are **not ready** and **MUST** be returned for revision. They **MUST NOT** be marked approved at PLAN/CRD or at Close Gate until token fidelity is fully resolved and reflected in the epic’s acceptance and evidence.

## ---

## 1.2 PLAN: Machine header (paste and fill, then post)

type: PLAN  
epic:  
  id: "EPIC-?.?"  
  title: ""  
goal\_one\_line: ""  
non\_goals: \["", "", ""\]  
context\_header: "D=\_\_ W=\_\_ IFC=\_\_ CU=\_\_ POC=\_\_ IC=\_\_ ESC=\_\_ APPLY\_STEPS=\_\_ VERIFY\_CHECKS=\_\_ Ambiguities=\_\_"

dependencies:  
  must\_have: \[""\]

blocks: \[""\]

interfaces\_public: \[""\]

outcomes\_vertical\_cuts:  
  \- ""  
  \- ""

/\# ≤5; titles only (no bytes)  
acceptance\_proofs:  
  \- "DET\_SERIALIZER\_OK"  
  \- "CLI\_READER\_PARITY\_OK"  
  \- "EVIDENCE\_INDEX\_UPDATED\_OK"  
  \- "EPIC\_IS\_GATE\_OK"  
  \- "A7\_GET\_QUOTED\_ETAG\_OK"   \# if the epic delivers a JSON success route

/\# Also include by title, as applicable (no version numbers in prose):  
also\_include:  
  pr\_baseline\_tokens:  
    \- "PR\_OPENED\_OK"  
    \- "TESTS\_PASS\_OK"  
    \- "DOC\_DELTA\_PRESENT\_OK"

    \# Index/mirror (same PR)  
    \- "EVIDENCE\_INDEX\_UPDATED\_OK"  
    \- "EVIDENCE\_INDEX\_HASH\_OK"  
    \- "MACHINE\_MIRROR\_UPDATED\_OK"  
    \- "CLOSE\_PACK\_FILES\_PRESENT\_OK"

  a7\_detail\_tokens:  
    \- "A7\_HEAD\_PARITY\_OK"  
    \- "A7\_304\_OMITS\_CT\_CL\_OK"  
    \- "A7\_VARY\_AUTH\_AE\_OK"  
    \- "A7\_ENCODING\_INVARIANCE\_OK"  
    \- "A7\_TRANSPORT\_PROOF\_OK"  
    \- "ENDPOINTS\_CATALOG\_INTERNAL\_OK"  
    \- "ENDPOINTS\_CATALOG\_OK"  
    \- "ENDPOINTS\_CATALOG\_ENV\_GATE\_OK"

  cli\_detail\_tokens:  
    \- "CLI\_INSTALL\_OK"  
    \- "CLI\_HELP\_OK"  
    \- "CLI\_SHOWCOMPAT\_PRESENT"  
    \- "CLI\_SHOWCOMPAT\_CANON\_OK"  
    \- "CLI\_AB\_BA\_PARITY\_OK"  
    \- "CLI\_TWO\_RUN\_IDENTITY\_OK"  
    \- "CLI\_READER\_EMITTER\_PARITY\_OK"

  db\_posture\_tokens:  
    \- "DB\_RUNTIME\_SEARCH\_PATH\_OK"  
    \- "DB\_ROLE\_OK"  
    \- "DB\_SCHEMA\_FINGERPRINT\_OK"  
    \- "DB\_CONN\_ENV\_OK"

risks: \["\<1–2 concise risks\>"\]  
open\_decisions: \["\<≤3; must resolve before IP\>"\]  
hd\_engine\_canon\_anchors: \["\<reader|aux|logs|meta|cache|sdk\>"\]

\# exchanged now (or in CRD); not after IP  
code\_capsules\_proposed:  
  \- id: "canon\_serializer\_v1"  
    status: "proposed"  
  \- id: "strong\_etag\_v1"  
    status: "proposed"

notes: |  
  PR-first via CodEx. CodEx opens the PR automatically after sandbox build/test.  
  Do not instruct humans to run git or create PRs.  
  Update Doc-Delta \+ human Evidence Index \+ hash sentinel \+ machine JSONL mirror in the same PR when artifacts/proofs change.  
  A7 proofs (if any) must run on a cataloged JSON success route; /internal/version is not A7-eligible.  
  Capture env-gate proof and prove encoding invariance (identity and effective length).  
  Governed locations only: artifacts/\*\* and docs/\*\*; no transient/generator paths.

---

## 1.3 CRD: Machine header (issued by Lead Dev after one review)

type: CRD  
epic\_id: "EPIC-?.?"  
objective: ""  
evidence\_minima:  
  \# Reader A7 work (if applicable)  
  \- "Endpoint Catalog present (docs/ENDPOINTS\_CATALOG.json \+ .sha256); A7 proof JSON captured and indexed (human+machine; same PR)"

  \# CLI parity (if applicable)  
  \- "CLI parity artifacts present: artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/cli/summary.json"

  \# DB posture  
  \- "db\_posture\_tokens:

  \- "DB\_RUNTIME\_SEARCH\_PATH\_OK"

  \- "DB\_ROLE\_OK"

  \- "DB\_SCHEMA\_FINGERPRINT\_OK"

  \- "DB\_CONN\_ENV\_OK"

  \- "DB\_BOUNDARY\_VIEW\_OK"

  \- "DB\_WRITERS\_ISOLATED\_OK"

  \# BodyGraph ingest (if applicable)  
  \- "BG evidence present: source\_selection.snapshot.json; source\_invariance/{ab.json,ba.json,summary.json}; refresh\_policy.snapshot.json; metrics/logs samples"

scope\_text: "\<what to deliver and prove, titles-only (no byte listings)\>"  
context\_header: "D=\_\_ W=\_\_ IFC=\_\_ CU=\_\_ POC=\_\_ IC=\_\_ ESC=\_\_ APPLY\_STEPS=\_\_ VERIFY\_CHECKS=\_\_ Ambiguities=\_\_"

/\# ≤5; titles only (no bytes)  
acceptance\_proofs:  
  \- "DET\_SERIALIZER\_OK"  
  \- "CLI\_READER\_PARITY\_OK"  
  \- "EVIDENCE\_INDEX\_UPDATED\_OK"  
  \- "EPIC\_IS\_GATE\_OK"  
  \- "A7\_GET\_QUOTED\_ETAG\_OK"   \# if the epic delivers a JSON success route

/\# Also require by title, as applicable:  
also\_require:  
  pr\_baseline\_tokens:  
    \- "PR\_OPENED\_OK"  
    \- "TESTS\_PASS\_OK"  
    \- "DOC\_DELTA\_PRESENT\_OK"

    \# Index/mirror (same PR)  
    \- "EVIDENCE\_INDEX\_UPDATED\_OK"  
    \- "EVIDENCE\_INDEX\_HASH\_OK"  
    \- "MACHINE\_MIRROR\_UPDATED\_OK"  
    \- "CLOSE\_PACK\_FILES\_PRESENT\_OK"

  a7\_detail\_tokens:  
    \- "A7\_HEAD\_PARITY\_OK"  
    \- "A7\_304\_OMITS\_CT\_CL\_OK"  
    \- "A7\_VARY\_AUTH\_AE\_OK"  
    \- "A7\_ENCODING\_INVARIANCE\_OK"  
    \- "A7\_TRANSPORT\_PROOF\_OK"  
    \- "ENDPOINTS\_CATALOG\_INTERNAL\_OK"

  ops\_endpoint\_tokens:  
    \- "INTVER\_200\_CTYPE\_JSON\_UTF8\_OK"  
    \- "INTVER\_HEAD\_PARITY\_OK"  
    \- "INTVER\_CONDITIONALS\_IGNORED\_OK"  
    \- "INTVER\_200\_NO\_ETAG\_OK"

notes\_for\_coder:  
  \- "Do not restate transport bytes or schemas here; route to HDE-CLI-API-Vendor-Ref / HDE-Governance / HDE-Schemas & Artifacts by title only."  
  \- "A7 proofs (if applicable) must target a cataloged JSON success route (not /internal/version); capture env-gate proof; prove ETag \+ Content-Length encoding invariance; ensure Vary: Authorization, Accept-Encoding present; 304 must omit both Content-Type and Content-Length."  
  \- "Ensure Doc-Delta \+ Evidence Index (human) \+ hash sentinel \+ machine JSONL mirror ride in the same PR as the code change; each mirror record must include a proof\_anchor to a path-proof file. Governed locations only (artifacts/\*\*, docs/\*\*)."

\# immutable after IP approval  
code\_capsules\_approved:  
  \- id: "canon\_serializer\_v1"  
    status: "approved"  
  \- id: "strong\_etag\_v1"  
    status: "approved"

---

## 1.4 Adjacent pre-start gates (titles-only)

 **Purpose.** Some epics depend on deliverables from adjacent roles/streams (e.g., EPIC-010 narrative copy gates).  
 **Rule.** Pre-start gates **must**: (a) name the deliverable by **title only**, (b) register acceptance tokens in **Governance**, and (c) require evidence entries (**human \+ mirror**) in the **same PR** that unblocks the epic. *(See Build Notes — Adjacent Subtask gate for EPIC-010.)*

---

## 1.5 Code capsules (PLAN/CRD samples)

canon\_serializer\_v1 (py)  
 import json  
 def canon\_dumps(obj):  
  return json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",",":")) \+ "\\n"  
contracts: CANON\_SERIALIZER\_LF, STABLE\_KEY\_ORDER  
anchors: IDENTITY\_OK, PREIMAGE\_OK  
notes: One import path repo-wide; replaces any ad-hoc dumps.

strong\_etag\_v1 (py)  
 import hashlib  
 def strong\_etag(body\_bytes\_lf: bytes) \-\> str:  
  return '"' \+ hashlib.sha256(body\_bytes\_lf).hexdigest() \+ '"'  
contracts: STRONG\_QUOTED, SHA256\_BODY\_LF  
anchors: HEADERS\_OK  
notes: Never emit ETag for writers/errors.

serializer\_ts\_v1 (ts)  
 export function canonDumps(obj: Record\<string, unknown\>): string {  
  const keys \= Object.keys(obj).sorted();  
  const ordered: Record\<string, unknown\> \= {};  
  for (const k of keys) ordered\[k\] \= (obj as any)\[k\];  
  return JSON.stringify(ordered) \+ "\\n";  
 }  
 // contracts: CANON\_SERIALIZER\_LF, STABLE\_KEY\_ORDER  
 // anchors: IDENTITY\_OK  
 // notes: SDKs must reproduce service bytes exactly.

# **2\) IMPLEMENTATION GUIDE (Lead Dev; posted immediately after CRD)**

Purpose

Define how the work proceeds **after CRD approval** in a way CodEx can execute **without direct access to these docs**. Lead Dev approves once, then steps out except for the PR gate review. **CodEx does not read PF docs**; therefore the Implementation Agent (IA) must **provide explicit formats and any verbatim components/schemas** during build sessions. CodEx may adapt within approved scope and **must deliver a detailed change report** at the end. **PR is created by the PO in the CodEx UI**. Repo-docs (indexes/cribs) and the **Evidence Index should be updated in the same PR** whenever proofs/artifacts change (preferred). If the UI cannot accommodate doc edits, **IA opens a follow-up docs PR immediately**.

## **2.1 Machine header**

type: IMPLEMENTATION\_GUIDE

epic\_id: "EPIC-?.?"

execution\_flow:

  \- "Lead Dev publishes this Implementation Guide to the Implementation Agent (IA)."

  \- "IA → CodEx: AUDIT REQUEST (explicit formats; attach any verbatim components/schemas required)."

  \- "CodEx → IA: AUDIT REPORT (capabilities, gaps, risks)."

  \- "IA drafts IMPLEMENTATION PLAN; Lead Dev approves once, then steps out (gate only)."

  \- "IA → CodEx: BUILD INSTRUCTIONS \+ VERBATIM COMPONENTS/SCHEMAS (CodEx may adapt within scope; must report all changes)."

  \- "CodEx: BUILD & TEST → returns DETAILED CHANGE REPORT \+ ARTIFACTS/EVIDENCE to IA."

  \- "IA: requests changes or APPROVES."

  \- "PR-first via CodEx: CodEx opens PR \`epic/\<epic-id\>-\<slug\>\` and pushes code \+ Doc-Delta (repo docs) \+ Evidence Index (human JSON) \+ Evidence Index hash sentinel \+ machine JSONL mirror (records-only, canonical, one LF, unknown keys rejected, ASCII field order, sort-before-write, single mirror file; each record has discovered\_physical\_path and a proof\_anchor to a path-proof file) \+ close-pack files (audit/EPIC-\<ID\>\_close\_report.md, audit/EPIC-\<ID\>\_MANIFEST.json)."

  \- "When A7 is in scope, the PR also carries: Endpoint Catalog file (docs/ENDPOINTS\_CATALOG.json \+ .sha256), env-gate headers proof, and the composite success proof JSON (artifacts/proofs/reader\_success\_get\_head\_304.json) validated against the PF12 schema."

  \- "Lead Dev: performs PR gate review; verifies PASS tokens (incl. CLI\_READER\_PARITY\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, CLOSE\_PACK\_FILES\_PRESENT\_OK), and—when applicable—A7 tokens (A7\_HEAD\_PARITY\_OK, A7\_304\_OMITS\_CT\_CL\_OK, A7\_VARY\_AUTH\_AE\_OK, A7\_ENCODING\_INVARIANCE\_OK, A7\_TRANSPORT\_PROOF\_OK, ENDPOINTS\_CATALOG\_INTERNAL\_OK). Confirms Catalog-only proof surface, /internal/version exclusion, env-gate proof, governed locations only."

  \- "PO: sole merger; squash-merge on PASS; informs Scrum Master after merge."

roles:

  lead\_dev: "Approves the Implementation Plan once; then acts as PR gate; ensures acceptance tokens and evidence requirements are met."

  implementation\_agent: "Coordinates with CodEx; supplies explicit formats and verbatim components/schemas; reviews change report; produces Closure Report; ensures Doc-Delta and indices are included in the same PR."

  codex: "Performs Audit and Build/Test; opens PR automatically per execution\_flow; adapts within scope; returns detailed change report \+ artifacts; does not read PF docs directly."

  po: "Routes comms; reviews and performs the squash-merge on PASS; not responsible for opening PRs."

evidence\_routing:

  interim: "Audit/Build/Test logs and observations returned by CodEx to IA."

  pr: "Close-pack in PR (report, manifest, proofs) with PASS token list visible; Human Index and hash sentinel updated; machine mirror updated in the same PR; each mirror record includes sha256, size\_bytes, produced\_at\_utc, discovered\_physical\_path, and a proof\_anchor to a path-proof file; governed locations only (artifacts/\*\*, docs/\*\*)."

  repo\_docs: "Doc-Delta (titles-only) is committed in the same PR as code and evidence; no separate docs-only PRs."

  final: "Merge on PASS; IA files Closure Report; Scrum Master updated; boards moved."

determinism\_pins:

  lc\_all: "C"

  tz: "UTC"

capsules\_scope: "All capsules finalized at IP approval; immutable thereafter. CodEx may propose scoped improvements but must record them in the change report."

codex\_can\_see\_pf\_docs: false

---

## **2.2 Audit (CodEx)**

**Goal.** Establish that the codebase can host the change without violating canon, and surface any gaps or risks **before** Build/Test. CodEx responds in prose and fills the output fields; the Implementation Agent (IA) provides the audit template and any verbatim snippets or schema fragments required for checks.

**Checklist (titles only for references; IA supplies exact formats/snippets as needed)**

* **Serializer posture.** One single import path for the canonical serializer (equivalent to `canon_serializer_v1`); flag duplicates or ad-hoc JSON dumps. (HDE-Math-Spec; HDE Architecture — single-emitter rule)

* **Idempotence posture.** Preimage \+ newline stance match HDE-Math-Spec (fields & ordering; trailing LF) and hashing stance matches **SHA-256 over the LF-terminated canonical body**.

* **Public transport (success path, A7).** Satisfiable **only** on a **cataloged JSON success route** (Endpoint Catalog by title); **not on `/internal/version`**. Confirm feasibility of:  
   – **Strong, quoted ETag** over LF-terminated body;  
   – **HEAD 200** mirroring validators, `Content-Type == GET`, `Content-Length == len(identity 200 body)`;  
   – **304 only after prior 200**, **omitting both** `Content-Type` **and** `Content-Length`;  
   – `Vary: Authorization, Accept-Encoding` supported;  
   – **Encoding invariance** feasible (ETag and **effective `Content-Length`** stable across accepted encodings). (HDE-Governance — A7; CLI/API Vendor Ref — transport bytes)

* **Endpoint Catalog posture (if A7 in scope).** Catalog is **internal-only** and **env-gated per entry**; non-prod entries **unreachable in prod**. Confirm a practical strategy for **headers-only env-gate proof**. (Governance; CLI/API Vendor Ref; Schemas & Artifacts — index path)

* **Composite success proof JSON.** Plan to emit a **records-only** composite proof (`reader_success_get_head_304.json`) and validate it against the **PF12 composite proof schema** (titles-only pointer). (Schemas & Artifacts)

* **Writers/Errors transport.** Writers are **no-store**, never 304; error responses carry `Content-Type: application/json; charset=utf-8` and **no ETag**. (Governance — writers)

* **Rails closed refusal.** On closed rails, refusal is **typed numeric-free JSON**, `no-store`, **no `ETag`/`Vary`/`Content-Encoding`**; confirm plan for the **single-file refusal proof** shape (headers block → blank line → one-line canonical JSON body). (Governance; Schemas & Artifacts)

* **Logs & security.** **Keys-only logging** (no payload bodies, no secrets); redaction & validation posture aligns with Governance; CI grep-guards exist.

* **Aux narrative (if in scope).** A7-equiv success path feasible (deterministic text, strong ETag on LF-text); **suppression \= 200 with no body and no ETag**; policy header supported. (Narratives Guide; Governance)

* **Dev DB bridge fallback (PF10-A).** In **dev**, if `DATABASE_URL` present but **unusable**, fall back to `DB_BRIDGE_URL`; refuse if neither is usable. Plan to capture **`artifacts/runtime/env_connectivity.snapshot.json`**; diagnostics keys-only, **no secrets**. (Governance; Schemas & Artifacts)

* **Evidence parity & PR readiness (PF12 single home).** Human Evidence Index (`docs/evidence/INDEX.json`), **hash sentinel** (`docs/evidence/INDEX.sha256`), and machine mirror (`artifacts/evidence_index.jsonl`) exist or can be emitted in the **same PR**; mirror is **records-only, canonical JSONL** (UTF-8, sorted keys, compact, one LF), **unknown-keys rejected**, **ASCII field order**, **sort-before-write**, **single mirror file**, and supports a `proof_anchor` pointing to a co-located path-proof file. CI has—or will add—parity/unknown-key checks. (Schemas & Artifacts; Build Notes)

* **Governed locations only.** All evidence under **`artifacts/**`** and **`docs/**`**; **no transient/generator paths**. (Schemas & Artifacts)

* **Gaps & proposals.** List missing components/schemas; propose minimal fixes or scoped improvements; call out any risks that would block CodEx from opening a PR and satisfying tokens.

---

**Output fields (CodEx fills; IA provides this structure)**

audit:

  serializer\_path: "\<module.path\>"

  duplicates: \["\<offending.symbol\>", "..."\]

  det\_serializer\_ok: true|false

  idempotence\_ok: true|false

  a7\_proof\_surface\_exists: true|false         \# cataloged JSON success route present

  a7\_vary\_auth\_ae\_ok: true|false              \# Vary: Authorization, Accept-Encoding feasible

  a7\_head\_parity\_ok: true|false

  a7\_304\_omits\_ct\_cl\_ok: true|false

  a7\_encoding\_invariance\_ok: true|false

  endpoints\_catalog\_file\_ready: true|false    \# docs/ENDPOINTS\_CATALOG.json \+ .sha256 plan

  composite\_proof\_json\_ready: true|false      \# reader\_success\_get\_head\_304.json \+ schema validation plan

  env\_gate\_proof\_ready: true|false            \# plan to prove non-prod endpoints unreachable

  writers\_errors\_semantics\_ok: true|false

  refusal\_proof\_ready: true|false             \# single-file refusal proof shape/plan

  logs\_keys\_only\_ok: true|false

  governed\_locations\_ok: true|false           \# artifacts/\*\* and docs/\*\* only (no transient paths)

  \# PF10-A dev DB fallback

  dev\_db\_bridge\_fallback\_ready: true|false

  dev\_connectivity\_snapshot\_ready: true|false \# artifacts/runtime/env\_connectivity.snapshot.json plan

  \# PF12 evidence plumbing

  human\_index\_wired: true|false               \# docs/evidence/INDEX.json present/wireable

  human\_index\_hash\_ready: true|false          \# docs/evidence/INDEX.sha256 merge-gating plan

  machine\_mirror\_wired: true|false            \# artifacts/evidence\_index.jsonl generation wired

  mirror\_schema\_ok: true|false                \# canonical JSONL, one LF, ASCII order, single file, unknown-key rejection

  path\_proofs\_ok: true|false                  \# proof\_anchor \+ co-located path\_proof.txt strategy

  missing\_components: \["\<title\>", "..."\]

  proposed\_fixes: \["\<short fix\>", "..."\]

  blockers: \["\<risk\>", "..."\]

---

## **2.3 Code Review (CodEx)**

**Goal.** Review proposed change style and safety against canon, given IA-supplied formats/snippets.

**Checklist**

* No numerics in public payload/narrative.  
* Writers/Errors responses follow Governance semantics (by title).  
* No RNG/time sources in deterministic paths.  
* No additional public interfaces beyond `interfaces_public` in the plan.

**Output**

code\_review:  
  public\_numeric\_free: true  
  writers\_errors\_semantics\_ok: true  
  deterministic\_paths\_ok: true  
  interfaces\_within\_limit: true  
  red\_flags: \[\]

## **2.4 Sandbox Build/Test (CodEx)**

**Describe, at a high level, what was built and what was verified.** Include a **Detailed Change Report** that IA can audit and file.

**Output**

sandbox:  
  build\_summary: "\<what was built and why\>"  
  tests:  
    ab\_ba\_identity\_ok: true  
    two\_run\_identity\_ok: true  
    transport\_parity\_simulated: true  
  artifacts\_recorded: \["build.log","test.log"\]  
  detailed\_change\_report:  
    files\_added: \["\<...\>"\]  
    files\_modified: \["\<...\>"\]  
    files\_removed: \["\<...\>"\]  
    deviations\_from\_instructions: \["\<...\>"\]       \# explain and justify  
    improvements\_made\_within\_scope: \["\<...\>"\]     \# list and justify  
    known\_limitations: \["\<...\>"\]  
    followups\_suggested: \["\<...\>"\]

---

# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**

## **3.1 Machine header**

{  
  "type": "IMPLEMENTATION\_PLAN",  
  "epic\_id": "EPIC-?.?",  
  "crd\_link": "\<pointer\>",  
  "digest": "\<≤1 page: how tasks satisfy proofs and surface/contract constraints\>",  
  "assumptions": \["\<...\>"\],  
  "context\_header": "D=\_\_ W=\_\_ IFC=\_\_ CU=\_\_ POC=\_\_ IC=\_\_ ESC=\_\_ APPLY\_STEPS=\_\_ VERIFY\_CHECKS=\_\_ Ambiguities=\_\_",  
  "code\_capsules\_finalized": \[  
    {"id": "canon\_serializer\_v1", "status": "approved"},  
    {"id": "strong\_etag\_v1", "status": "approved"},  
    {"id": "serializer\_ts\_v1", "status": "approved"}  
  \],  
  "codex\_inputs": {  
    "verbatim\_payloads": \["\<components\>", "\<schemas\>", "\<formats/snippets\>"\],  // CodEx cannot read PF docs  
    "instructions": "\<clear WHAT, scope limits, and acceptance expectations\>",  
    "freedom\_within\_scope": "CodEx may adapt/fix within scope; must report all changes at end",  
    "reporting\_requirements": "Return detailed\_change\_report \+ artifacts/evidence"  
  },  
  "pr\_expectations": {  
    "template\_required": true,  
    "acceptance\_tokens": \[  
      "DET\_SERIALIZER\_OK",  
      "TRANSPORT\_A7\_OK",  
      "CLI\_READER\_PARITY\_OK",  
      "INTVER\_NO\_STORE\_NO\_ETAG\_OK",  
      "EVIDENCE\_INDEX\_UPDATED\_OK"  
    \],  
    "close\_pack\_files": \[  
      "audit/EPIC-\<ID\>\_close\_report.md",  
      "audit/EPIC-\<ID\>\_MANIFEST.json"  
    \]  
  }  
}

## **3.2 Tasks (repeat per task; keep atomic)**

task:  
  name: "\<atomic task name\>"  
  description: "\<what changes conceptually\>"  
  inputs: \["\<docs or modules\>"\]  
  dependencies: \["\<tasks\>"\]  
  expected\_observables:  
    \- "\<what will be true if task succeeds\>"  
  proof\_coverage: \["DET\_SERIALIZER\_OK","TRANSPORT\_A7\_OK"\]  
  validation\_text: "\<how success will be reasoned and later reported\>"  
  capsules\_used: \["canon\_serializer\_v1","strong\_etag\_v1"\]

## **3.3 Blockers and resolutions**

blockers:  
  \- item: "\<description\>"  
    resolution: "\<resolve|waive|defer\>"

## **3.4 Approval**

ip\_approval:  
  lead\_dev\_decision: "APPROVED"  
  notes: "\<optional\>"  
  lead\_dev\_steps\_out: true

From this point, CodEx and IA proceed per the approved IP. Lead Dev returns only to gate the PR.

Here’s a tightened, more logically structured version that makes the per-PR vs final epic close much clearer, while keeping all the same requirements and tokens.

---

## **3.5 Close Gate (PR-first)**

### **3.5.1 Requirement**

1. For every epic, work is delivered **PR-first via CodEx**.

2. CodEx opens PRs automatically for each epic slice and pushes **code \+ Doc-Delta \+ evidence in the same PR**.

3. An epic **MAY** use up to **10 PRs** to deliver its full scope; each PR **MUST** be self-contained and follow the PR-first and parity rules in §0.2.

4. The **Product Owner (PO)** is the sole merger (squash on PASS).

5. Epic-level acceptance (as recorded in **HDE Phased Epics**) occurs **only after**:

   * all required PRs for that epic have merged, **and**

   * the **Close Gate** has been satisfied.

6. The Close Gate applies to the PR that carries the epic **close-out** (“close PR”).

   * All earlier PRs in the series must still be PR-first and parity-clean,

   * but **only the close PR** is required to carry the full close-pack and final PASS roster described below.

   ---

   ### **3.5.2 Close PR contents**

   #### **3.5.2.1 Close-pack files**

The close PR **MUST** include the epic close-pack:

* `audit/EPIC-<ID>_close_report.md`

* `audit/EPIC-<ID>_MANIFEST.json`

* PASS tokens section (final status; titles only, see §2.0 roster)

* `CLOSE_PACK_FILES_PRESENT_OK` (token confirming presence of the close-pack files)

  #### **3.5.2.2 Core determinism & parity tokens**

The close PR **MUST** demonstrate core determinism and parity via (titles only):

* `DET_SERIALIZER_OK`

* `CLI_READER_PARITY_OK`

* `TWO_RUN_IDENTITY_OK`

  #### **3.5.2.3 Index/mirror trio (same PR)**

The close PR **MUST** update the Evidence Index and machine mirror in the **same PR**, satisfying:

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

  #### **3.5.2.4 Repo-docs & evidence updates (same PR)**

The close PR **MUST** update, in the **same PR**:

* **Human Evidence Index:** `docs/evidence/INDEX.json`

* **Index hash sentinel:** `docs/evidence/INDEX.sha256`

  * hash **MUST** match the bytes of `INDEX.json`

* **Machine mirror:** `artifacts/evidence_index.jsonl`

  * records-only canonical JSONL

  * exactly one trailing LF

  * unknown keys rejected

  * ASCII field order

  * sort-before-write

  * single mirror file

  * each record has `discovered_physical_path` \+ `proof_anchor` to a co-located path-proof

* Repo index and acceptance crib notes

* Doc-Delta note (if applicable)

  #### **3.5.2.5 A7 tokens (when A7 is in scope — Catalog success route)**

When A7 is in scope for the epic, the close PR **MUST** satisfy the relevant A7 tokens (titles only), including:

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

* `ENDPOINTS_CATALOG_INTERNAL_OK`

* `A7_TRANSPORT_PROOF_OK`

  #### **3.5.2.6 /internal/version tokens (when in scope — ops surface)**

When `/internal/version` is in scope, the close PR **MUST** satisfy:

* `INTVER_200_CTYPE_JSON_UTF8_OK`

* `INTVER_HEAD_PARITY_OK`

* `INTVER_CONDITIONALS_IGNORED_OK`

* `INTVER_200_NO_ETAG_OK`

  #### **3.5.2.7 A7 artifacts (when A7 is in scope; titles only)**

When A7 is in scope, the close PR **MUST** include the governed A7 artifacts (titles only):

* **Endpoint Catalog file \+ checksum:**

  * `docs/ENDPOINTS_CATALOG.json`

  * `docs/ENDPOINTS_CATALOG.json.sha256`

* **Env-gate headers-only proof:**

  * `artifacts/proofs/endpoints_env_gate_proof.log`

* **Composite success proof JSON** (records-only; PF12 schema-validated):

  * `artifacts/proofs/reader_success_get_head_304.json`

  * covers:

    * success headers for **GET / HEAD / 304**,

    * writers/errors posture,

    * encoding-invariance capture.

  ---

  ### **3.5.3 Repo docs sweep (major epics)**

For **major epics** (for example, HDE-EPIC018), the close PR **MUST** also include a final **“repo docs sweep”** that:

1. **Aligns non-canonical repo docs.**  
    Brings top-level, non-canonical repo docs — for example:

   * `README.md`

   * `CHANGELOG.md`

   * `AGENTS.md`

   * non-pfcanon files under `docs/**`

2. into alignment with:

   * the epic’s manifest and close report, and

   * PF-Canon (by title).

3. **Updates or retires older epic-specific guidance.**  
    Brings older, epic-specific guidance (for example:

   * EPIC011/EPIC017-only notes,

   * Alpha/A7-only descriptions,

   * outdated evidence practices)

4. into line with the current epic’s rails and acceptance outcomes, **or** clearly retires it.

5. **Does not modify PF-Canon itself.**  
    The repo docs sweep **MUST NOT** modify any PF-Canon docs (for example files under `docs/pfcanon/**`). PF-Canon remains the single home for normative rules; the repo docs sweep is strictly an implementation-level alignment.

6. **Lives in the close PR.**  
    This repo docs sweep is part of the close-out tasks for such epics and is performed in the **same close PR** that carries:

   * the close-pack,

   * the index/mirror trio, and

   * other close-out evidence.

   ---

   ### **3.5.4 ADR block in the close-pack (all epics)**

The close PR **MUST** ensure that the epic’s close-pack includes a brief **ADR block** summarizing the key architectural and behavioral decisions made during the epic.

At minimum, this ADR block **MUST**:

1. **Use neutral, titles-only references back to PF-Canon**, for example:

   * *Glow Infrastructure*

   * *HDE-CLI-API-Vendor-Ref*

   * *Glow QA Guide*

   * *HDE Phased Epics*

2. **List each decision as a short item** with:

   * a **decision label** (for example “ADR — QA evidence root and directory casing”),

   * a **one–two sentence statement** of the decision, and

   * the **PF documents** that should receive the corresponding Doc Deltas (by title only).

3. **Location.**  
    The ADR block lives in the close report:

   * `audit/EPIC-<ID>_close_report.md`

4. and is part of the epic’s permanent record. Follow-on epics and doc-only work can then use it to drive PF-Canon deltas.

   ---

   ### **3.5.5 Remediation PR pattern (separate from Live QA)**

Structural remediations that do **not** change engine behavior — for example:

* directory casing normalization,

* path refactors,

* relocation of evidence files into governed roots —

**MUST** be handled as explicit **remediation PRs**, not buried inside Live QA runs.

1. **Separate remediation PRs.**  
    Each remediation PR should:

   * be tracked by its own card or PF10 addendum, and

   * be scoped narrowly to the remediation at hand.

2. **Live QA may depend on, but not perform, remediation.**  
    Live QA plans **may depend** on such remediation PRs (for example, “EPIC017 QA evidence is consolidated under `audit/qa/hde-epic017/logs/`”), but Live QA steps themselves **MUST NOT** perform large-scale structural migrations as part of a PO session.

3. **Close Gate responsibility.**  
    The Close Gate for the epic **MUST** confirm that:

   * any required remediation PRs have merged, and

   * the close-pack and Evidence Index/mirror reflect the **post-remediation state**.

4. Live QA evidence artifacts should assume those canonical paths, not improvise new ones.

Using a distinct remediation PR pattern keeps Live QA focused on behavior and evidence capture, while structural cleanups are performed once, auditable, and referenced by title from **HDE Phased Epics** and **Build Notes**.

---

### **3.5.6 Merge responsibilities**

At Close Gate, merge responsibilities are:

1. **Lead Dev.**  
    Performs the gate review on the close PR:

   * checks PASS tokens,

   * checks A7/ops applicability,

   * checks index/mirror hygiene,

   * verifies governed locations only.

2. **Product Owner (PO).**  
    Squashes the close PR on PASS.

3. **Scrum Master.**  
    Is informed after merge.

4. **Implementation Agent (IA).**  
    Files the Closure Report and confirms that docs and evidence are synchronized in the merged PR.

---

# 4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)

## 4.1 Machine header

type: PR\_COMMIT\_PLAN  
epic\_id: "EPIC-?.?"  
one\_line\_outcome: ""

precommit\_prereqs:  
  reader\_json\_success\_route\_registered: true   \# Endpoint Catalog entry exists (internal-only, env-gated)  
  reader\_a7\_matrix:  
    \- "200+STRONG\_ETAG"  
    \- "HEAD\_200\_PARITY"  
    \- "304\_OMIT\_CT\_CL"  
  a7\_vary\_auth\_ae\_ready: true                  \# Vary: Authorization, Accept-Encoding supported  
  a7\_encoding\_invariance\_ready: true           \# ETag & effective Content-Length stable across encodings  
  env\_gate\_proof\_ready: true                   \# Plan to capture headers proving non-prod endpoints are unreachable in prod  
  writers\_errors\_no\_store\_no\_etag: true  
  ab\_ba\_identity\_ok: true  
  two\_run\_identity\_ok: true  
  narrative\_policy\_ok: "\<if Aux in scope (200/no body/no ETag on suppression)\>"  
  logs\_keys\_only: true  
  indices\_ready\_same\_pr: true                  \# Human INDEX.json and machine evidence\_index.jsonl updated in same PR; mirror canonical JSONL (UTF-8, sorted keys, compact, one LF), unknown keys rejected; each record includes proof\_anchor to a path-proof file  
  single\_finalization\_scope: "\<precisely what is finalized by this PR (one coherent slice)\>"  
  revert\_concept: "\<simple revert path: single squash commit rollback; no data loss; how to disable feature flag if applicable\>"

## 4.2 Required pre-merge evidence (titles-only; CodEx supplies artifacts)

premerge\_evidence\_required:  
  \- name: "PR\_OPENED\_OK"                      \# PR opened by CodEx using epic template; PASS tokens listed in body  
  \- name: "DOC\_DELTA\_PRESENT\_OK"              \# Repo docs (indexes/cribs) updated in this PR  
  \- name: "CLOSE\_PACK\_FILES\_PRESENT\_OK"       \# audit/EPIC-\<ID\>\_close\_report.md and audit/EPIC-\<ID\>\_MANIFEST.json included in this PR  
  \- name: "EVIDENCE\_INDEX\_UPDATED\_OK"         \# docs/evidence/INDEX.json updated (titles/paths only)  
  \- name: "MACHINE\_MIRROR\_UPDATED\_OK"         \# artifacts/evidence\_index.jsonl present; canonical JSONL (one LF), unknown keys rejected; each record has proof\_anchor to a path-proof file  
  \- name: "EVIDENCE\_INDEX\_HASH\_OK"            \# docs/evidence/INDEX.sha256 updated; hash matches INDEX.json bytes

  \- name: "CLI\_READER\_PARITY\_OK"              \# Reader 200 body equals hdctl/glowctl showcompat stdout (LF-terminated)  
  \- name: "TWO\_RUN\_IDENTITY\_OK"               \# Two independent runs produce byte-identical bodies and ETag

  \- name: "A7\_GET\_QUOTED\_ETAG\_OK"             \# GET 200 returns strong quoted ETag over LF-terminated canonical body  
  \- name: "A7\_HEAD\_PARITY\_OK"                 \# HEAD 200 mirrors GET validators; Content-Type \== GET; no body; Content-Length \== length(identity 200 body)  
  \- name: "A7\_304\_OMITS\_CT\_CL\_OK"             \# 304 only after prior 200; no body; omits both Content-Type and Content-Length; validators mirror cached GET  
  \- name: "A7\_VARY\_AUTH\_AE\_OK"                \# Vary: Authorization, Accept-Encoding present  
  \- name: "A7\_ENCODING\_INVARIANCE\_OK"         \# ETag and effective Content-Length stable across accepted encodings  
  \- name: "ENDPOINTS\_CATALOG\_INTERNAL\_OK"     \# Catalog internal-only; entries env-gated; non-prod entries unreachable in prod (headers-only env-gate proof)

  \- name: "WRITERS\_ERRORS\_NOSTORE\_NOETAG\_OK"  \# Writers no-store; errors have Content-Type: application/json; charset=utf-8; no ETag

## 4.3 Guidance for PO (CodEx UI)

* Do **not** create a PR manually. Confirm CodEx has opened the PR for this epic (PR ID present) and that the close pack \+ PASS tokens appear in the PR body.

* Verify this PR contains:

  * Doc-Delta (repo docs),

  * Human Evidence Index update, and

  * Machine JSONL mirror update,  
     as required. If any index/doc was omitted, ask the IA to raise an immediate docs-only PR.

* Wait for the Lead Dev gate review (PASS).

* On PASS, perform a **squash merge**, then notify the Scrum Master.

## 4.4 PO approval and commit record

po\_approval:  
  decision: "APPROVED"  
  notes: ""

commit\_record:  
  pr\_id: ""  
  commit\_id: ""  
  closeout\_evidence\_pointer: "\<pointer to close pack / proof bundle in PR\>"

## 4.5 PR template — evidence-only QA

For PRs whose sole purpose is to verify evidence and transport posture **without** changing production code. Use titles only for cross-doc references. Keep the human Evidence Index \+ hash sentinel \+ machine mirror in the **same PR**.

Paste this as the PR body and fill in:

\# Evidence-only QA — \<short scope\> (EPIC-\<ID\> QA)

\#\# Summary  
\- Purpose: \<one paragraph describing what is being verified and why\>  
\- Scope: evidence-only; no production code changes  
\- Determinism pins set for all captures and CI: LC\_ALL=C, TZ=UTC

\#\# Artifacts included (titles and repo-relative paths only)

\#\#\# Indexes (must update in the same PR)  
\- Evidence Index (human) — docs/evidence/INDEX.json  
\- Evidence Index hash sentinel — docs/evidence/INDEX.sha256  
\- Machine Evidence Index (JSONL) — artifacts/evidence\_index.jsonl

\#\#\# Endpoint Catalog (A7 proof surface; Catalog-only)  
\- Catalog file (records-only) — docs/ENDPOINTS\_CATALOG.json  
\- Catalog checksum — docs/ENDPOINTS\_CATALOG.json.sha256  
\- Endpoint Catalog snapshot (titles-only) — artifacts/reader/endpoints\_snapshot.json  
\- Env-gate proof (headers-only) — artifacts/proofs/endpoints\_env\_gate\_proof.log

\#\#\# A7 proofs on a cataloged JSON success route (headers-only)  
\- GET (200) — artifacts/proofs/success\_get.txt  
\- HEAD (200) — artifacts/proofs/success\_head.txt  
\- 304 — artifacts/proofs/success\_304.txt  
\- Writers/errors posture — artifacts/proofs/success\_writers\_errors.txt  
\- Encoding-invariance — artifacts/proofs/encoding\_invariance.txt  
\- Composite success proof JSON — artifacts/proofs/reader\_success\_get\_head\_304.json    
  \# (records-only; validated against PF12 composite proof schema)

\#\#\# Ops — rails refusal proof (closed-rails)  
\- Refusal probe capture — artifacts/proofs/ops\_refusal\_proof.txt    
  \# headers → blank line → LF-terminated numeric-free JSON body; titles-only routing to HDE-Governance for policy/tokens and HDE-Schemas & Artifacts for indexing/mirror rules

\#\#\# CLI / Reader parity & determinism  
\- CLI parity set (AB/BA/summary) — artifacts/cli/ab.json; artifacts/cli/ba.json; artifacts/cli/summary.json  
\- Reader vs CLI parity diff (expected empty) — artifacts/cli/showcompat/reader\_vs\_cli.diff  
\- CLI showcompat stdout (LF-terminated; non-empty) — artifacts/cli/showcompat/stdout.json  
\- CLI two-run identity log — artifacts/cli/showcompat/two\_run\_identity.log  
\- Preimage recompute log — artifacts/cli/showcompat/preimage\_recompute.log

\#\#\# DB evidence (if in scope)  
\- DDL fingerprint — artifacts/db/ddl\_fingerprint.json  
\- Grants snapshot — artifacts/db/grants.txt  
\- Schema/search\_path echo — artifacts/db/check\_schema.txt  
\- Connection env selection proof — artifacts/db/conn\_env\_selection.log  
\- Dev connectivity snapshot (PF10-A) — artifacts/runtime/env\_connectivity.snapshot.json

\#\# PASS tokens (check what applies)

\#\#\# Index/mirror gates (same PR)  
\- \[ \] PR\_OPENED\_OK  
\- \[ \] DOC\_DELTA\_PRESENT\_OK  
\- \[ \] EVIDENCE\_INDEX\_UPDATED\_OK  
\- \[ \] EVIDENCE\_INDEX\_HASH\_OK  
\- \[ \] MACHINE\_MIRROR\_UPDATED\_OK

\#\#\# Determinism & parity  
\- \[ \] CLI\_READER\_PARITY\_OK  
\- \[ \] TWO\_RUN\_IDENTITY\_OK

\#\#\# A7 (Catalog-only)  
\- \[ \] ENDPOINTS\_CATALOG\_OK  
\- \[ \] ENDPOINTS\_CATALOG\_INTERNAL\_OK  
\- \[ \] A7\_GET\_QUOTED\_ETAG\_OK  
\- \[ \] A7\_HEAD\_PARITY\_OK  
\- \[ \] A7\_304\_OMITS\_CT\_CL\_OK  
\- \[ \] A7\_VARY\_AUTH\_AE\_OK  
\- \[ \] A7\_ENCODING\_INVARIANCE\_OK  
\- \[ \] A7\_TRANSPORT\_PROOF\_OK

\#\#\# Writers/errors posture  
\- \[ \] WRITERS\_ERRORS\_NOSTORE\_NOETAG\_OK

\#\#\# QA process (branches)  
\- \[ \] QA\_EVIDENCE\_ONLY\_OK  
\- \[ \] QA\_CI\_DIFF\_SCOPED\_OK

\#\#\# Close-pack (use N/A for QA if not an epic close)  
\- \[ \] CLOSE\_PACK\_FILES\_PRESENT\_OK    \# audit/EPIC-\<ID\>\_close\_report.md; audit/EPIC-\<ID\>\_MANIFEST.json

\#\# Human↔Machine parity checks  
\- \[ \] 1:1 parity between Appendix D entries and mirror records  
\- \[ \] Mirror JSONL is canonical: UTF-8, compact, exactly one LF; ASCII field order; sort-before-write; single mirror file  
\- \[ \] Unknown keys rejected in mirror schema  
\- \[ \] Each record has discovered\_physical\_path and proof\_anchor to a path-proof stored with the artifact  
\- \[ \] All listed paths exist and are repo-relative; governed locations only (artifacts/\*\*, docs/\*\*)

\#\# Diff-scoped CI status at time of landing  
catalog\_schema: pass|fail  
domain\_closure: pass|fail  
topology: pass|fail  
arrays\_as\_sets: pass|fail  
canonical\_json: pass|fail  
mirror\_schema: pass|fail        \# CI\_CHECK\_MIRROR\_SCHEMA\_OK  
final\_lf: pass|fail             \# CI\_CHECK\_FINAL\_LF\_OK  
env\_pins: pass|fail             \# LC\_ALL=C, LANG=C, TZ=UTC

\#\# Reviewer checklist  
\- A7 proofs run only on a cataloged JSON success route (not /internal/version)  
\- Catalog file \+ .sha256 present; env-gate proof captured  
\- GET, HEAD, and 304 captured; 304 omits both Content-Type and Content-Length  
\- Vary: Authorization, Accept-Encoding present on success route  
\- Encoding-invariance of identity (ETag) and effective length proven  
\- Composite success proof JSON present and schema-validated (PF12)  
\- Writers are no-store; error responses have Content-Type: application/json; charset=utf-8 and no ETag  
\- Reader and CLI share a single emitter and produce byte-equal bodies for identical inputs  
\- Two-run identity holds for body and ETag  
\- Evidence Index and hash sentinel updated in this same PR  
\- Machine mirror updated in this same PR and passes schema checks (records-only, unknown-key reject, ASCII order, sort-before-write, single file)

\#\# Notes  
Cross-doc references (titles only):

\- Governance and A7 policy — HDE-Governance  
\- Evidence mirror and artifacts — HDE-Schemas & Artifacts  
\- CLI and Reader contract — HDE-CLI-API-Vendor-Ref  
\- Math and serializer rules — HDE-Math-Spec

---

# 5\) Quick reference: where code exchange is allowed

* **Plan and CRD.** Propose/refine **code-capsules**.  
* **Implementation Plan (IP).** Finalize the capsule list; package verbatim components/schemas for CodEx. After IP approval, **capsules become immutable**. CodEx may apply scoped fixes but must record every change in the Detailed Change Report.  
* **Build.** IA provides instructions \+ verbatim materials. CodEx does **not** read PF docs directly.  
* **PR & Commit.** **CodEx opens the PR automatically**; no new code exchange beyond what CodEx built. PO performs **squash merge** after Lead Dev gate passes.  
* **Escalation.** PO may direct CodEx to inspect code/processes at any time. IA keeps docs synchronized (Doc-Delta \+ indices).

# **6\) PHASE EXIT DISCIPLINE (ALCHEMICAL PHASES)**

This section defines **how** the Product Owner and Lead Developer decide that an alchemical phase is ready to “exit” for planning purposes.

It does not redefine what the phases are; that remains in *Glow Development Philosophy* and *7 Phases of Alchemical Engineering* (titles only). It does not move epic records, issues, or task status out of *HDE Phased Epics* or *HDE-Build Checklist*; those remain the single homes for phase and epic data.

## **6.1 When this section applies**

Use this section whenever the PO and Lead Dev are asking:

* “Are we done enough with this phase to move the next epics into the next phase?”

* “Can we stop opening new epics tagged with this phase and carry the remaining work forward as debt?”

If the checks below cannot be evaluated from PF-Canon and governed evidence, the phase exit decision is **blocked-by-spec**, per §0.6.5. Do not treat “gut feel” or informal summaries as sufficient.

## **6.2 Phase exit is canon-first and evidence-backed**

Before declaring a phase exit-ready, the PO and Lead Dev **MUST** perform a canon inventory, exactly as in §1.1.1, with explicit attention to:

* *HDE Phased Epics* — phase, epics, D-goals, exclusions, tracked issues, and cross-epic issues.

* *HDE-Build Checklist* — phase tasks and statuses (Done / Partial / Consolidation pending / Not done / Won’t Do).

* *HDE-Schemas & Artifacts* and *HDE-Build Checklist* — Evidence Index, machine mirror, close packs, and governed roots only.

If any of the later checks (close-out epic, foundations, Partial/Consolidation rows, tracked issues) cannot be evaluated from this canon inventory, the phase **MUST NOT** be treated as exit-ready.

## **6.3 Close-out epic required**

Each phase **MUST** have at least one **close-out epic** in that phase that satisfies **all** of the following:

1. The epic is **Status: Done** in *HDE Phased Epics* for that phase, with D-goals and exclusions clearly recorded.

2. Its **tokens and evidence roster** for D-goals is complete in *HDE Phased Epics* and is consistent with the epic’s acceptance map and manifest.

3. The epic’s **close pack**:

   * lives under governed roots (for example `audit/EPIC-<ID>_close_report.md` and `audit/EPIC-<ID>_MANIFEST.json`), and

   * is indexed in both:

     * the human Evidence Index `docs/evidence/INDEX.json`, and

     * the machine mirror `artifacts/evidence_index.jsonl`,

4. per *HDE-Schemas & Artifacts* and *HDE-Build Checklist* (titles only).

If no epic in the phase meets these conditions, the phase **MUST NOT** be considered exit-ready.

## **6.4 Foundation tasks: “Not done” vs explicit decisions**

*HDE-Build Checklist* is the single home for phase tasks.

For the phase under review:

* All **foundation tasks** defined for that phase in *HDE-Build Checklist* **MUST** be:

  * marked **Done**, **or**

  * explicitly re-scoped or dropped, as below.

* Any **Not done** rows for that phase **MUST** be resolved one of two ways:

  * **Re-scoped:** the work is moved into a later phase by recording it explicitly in one or more future epics in *HDE Phased Epics* (new scope).

  * **Won’t Do:** the work is not going to be done and is recorded as **Won’t Do** in *HDE Phased Epics* with a short rationale and reflected in *HDE-Build Checklist*.

A phase **MUST NOT** be treated as exit-ready if there are foundation rows that are still Not done in *HDE-Build Checklist* without a matching re-scope or Won’t Do decision in *HDE Phased Epics*.

## **6.5 Partial / Consolidation pending rows as controlled debt**

For the phase under review, **Partial** and **Consolidation pending** rows in *HDE-Build Checklist* are treated as **debt, not blockers**, **only if**:

1. The notes for those rows show that the remaining work is **enhancement, tuning, or consolidation**, not missing foundational behavior.

2. Each such row is explicitly carried by one of:

   * a cross-epic **Outstanding Issue** or similar issue entry in *HDE Phased Epics* for that phase, **or**

   * a future epic record in *HDE Phased Epics* that names the work as “Existing work / Debt to absorb” in its scope.

If a Partial or Consolidation pending row has no such carrier, treat it like a missing foundation task: resolve it or re-scope it before calling the phase exit-ready.

## **6.6 Tracked issues must be disposed of, not dropped**

Before treating a phase as exit-ready:

* Every **Done** epic in that phase in *HDE Phased Epics* **MUST** list its tracked issues.

* Every tracked issue for those epics **MUST** record one of:

  * **Completed under \<EPIC\>** — resolved within that epic.

  * **Carried forward to \<EPIC\>** — moved into a later epic’s scope.

  * **Promoted to ISSUE-XXX** — promoted to a cross-epic or cross-phase issue with its own identifier.

  * **Explicitly dropped (with rationale)** — intentionally not carried forward, with a short explanation.

If a Done epic has real, unresolved issues that are not covered by one of these dispositions, phase exit is **not** allowed. Treat that as a spec gap and resolve it before re-evaluating.

## **6.7 Phase exit as a planning decision**

When §6.3–§6.6 are satisfied:

* Phase exit is treated as a **planning decision only**:

  * It says “the core aim of this phase has been achieved and its remaining work is tracked as debt,”

  * It does **not** say “all work tagged with this phase is finished forever.”

* Any remaining work that properly “belongs” to this phase **MUST** be handled as:

  * cross-epic or cross-phase issues recorded in *HDE Phased Epics*, **or**

  * explicit **inputs to the next phase’s epics** (for example, “carry sampler tuning from Dissolution into Separation error-envelope work”).

Once a phase is declared exit-ready under this section:

* New epics **MUST** be opened in the **next** phase, not the old phase.

* Those new epics **MUST** name the carried-forward work in their scope, so that acceptance and evidence for that work live entirely in the new phase.

This follows the instruction in *Glow Development Philosophy* to avoid over-tuning and silent drift and the expectation in *7 Phases of Alchemical Engineering* that phases do not mix: once a phase’s core aim is achieved and its debt is explicit, planning moves forward, and that phase stops accumulating new epics.

# Appendices

---

## Appendix A — Large Schemas & Assets (CodEx constraints)

**Purpose.** Define how to include large schemas or assets when CodEx cannot read PF docs or accept file attachments. CodEx consumes only **inline text** provided by the IA; this keeps work moving while preserving **ownership**, **auditability**, and **single-home** discipline.

### **Constraints (facts)**

* CodEx cannot see your docs and cannot accept file uploads; only IA-supplied **inline** text/snippets are visible to CodEx during build.  
* Only the **Product Owner (PO)** may load large files into the repo. Agents do **not** run git and do **not** create PRs.  
* CodEx may adapt **within scope** but **must report every change** in the Detailed Change Report.  
* **Governed locations only.** Assets and evidence **must live under** `artifacts/**` and `docs/**`. Transient/generator paths are **disallowed**.  
* **Single-PR parity.** Repo docs (Doc-Delta), the **human Evidence Index** (`docs/evidence/INDEX.json`), the **Evidence Index hash sentinel** (`docs/evidence/INDEX.sha256`), and the **machine mirror** (`artifacts/evidence_index.jsonl`) **must be updated in the same PR** when assets are introduced or moved. If the CodEx UI cannot include doc edits, the IA provides **verbatim text in the same PR body** for CodEx to commit.  
* **Mirror hygiene (PF12).** The mirror is **records-only canonical JSONL** (UTF-8, compact, **exactly one LF**), **unknown-keys rejected**, **ASCII field order**, **sort-before-write**, **single mirror file**; each record includes `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, **`discovered_physical_path`**, and a **`proof_anchor`** pointing to a co-located path-proof.

### **Roles & responsibilities**

**Lead Dev / IA**

* Prepare inline materials (formats, small schemas, snippets).  
* When assets are too large for inline use, create an **Asset Draft Pack** (fields below) for the PO to load.  
* Ensure the CodEx-opened PR captures **Evidence Index \+ hash sentinel \+ mirror** updates and single-home pointers. Avoid separate docs-only PRs.

**Product Owner**

* Load the Asset Draft Pack files **into the CodEx PR branch** at the specified targets.  
* Confirm the CodEx-opened PR and, after Lead Dev gate passes, **squash-merge**.

**CodEx**

* Uses only IA-provided inline materials during build.  
* Proposes scoped adjustments; lists every change in the Detailed Change Report (files added, modified, removed; deviations and improvements).  
* Does **not** read PF docs directly.

### **When to use an Asset Draft Pack**

Use a pack when any required artifact **cannot reasonably be pasted inline** for CodEx (e.g., large JSON/YAML schemas, binaries, long fixtures).

### **Asset Draft Pack — minimal fields**

*Paste verbatim to the PO and attach in the PR body; the PO loads these files to the PR branch.*

asset\_pack:  
  epic\_id: "EPIC-?.?"  
  owner: "IA or Lead Dev"  
  assets:  
    \- asset\_id: "schema\_user\_profile\_v3"  
      title: "User Profile Schema v3"  
      repo\_target\_location: "\<path/inside/repo\>"  
      size\_bytes: 123456  
      sha256: "\<64-hex\>"  
      license\_note: "\<source/license or 'internal'\>"  
      single\_home\_category: "Architecture"     \# route by category title only  
      notes: "Consumed by component X; CodEx will assume this location."

### **Guardrails**

* **No secrets or PII.** Include license and source.  
* Exactly **one single home per concept**; route by **category title** only, not by version numbers.  
* Keep paths **repo-relative** and stable; list **titles and paths** in the human Evidence Index.  
* For **governed assets**, add a mirror record (records-only JSONL) with a `proof_anchor` to a path-proof stored alongside the asset.

### **Flow (high level)**

1. Lead Dev → IA: approve scope; decide **inline** versus **Asset Pack**.  
2. IA → CodEx: send inline materials; name target paths for large assets.  
3. PO: load the Asset Pack at the target paths **in the CodEx PR branch**.  
4. CodEx: build & test; if something is missing, switch to **planning mode** and note stubs in the Detailed Change Report.  
5. IA: review the change report; request adjustments or approve.  
6. PO: confirm the CodEx-opened PR, then squash-merge after the Lead Dev gate passes.  
7. **Docs & evidence:** IA ensures **Doc-Delta**, **human Evidence Index \+ hash sentinel**, and **machine mirror** reflect the final assets **in the same PR**.

### **Planning mode (CodEx)**

Use to propose file trees, stub schemas, and integration points; surface gaps early. IA decides what to paste inline versus pack; planning output is **advisory**.

### **Acceptance and drift guards (titles only; tokens live in Governance)**

* **Evidence parity (same PR):** `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`.  
* **PR posture:** `PR_OPENED_OK`, `DOC_DELTA_PRESENT_OK`.  
* **Report completeness:** the Detailed Change Report lists **every** file added/modified/removed and **every** deviation from IA instructions.  
* **No surprises:** if an asset was not present at build time, CodEx records a **stub**; IA reconciles **before close**.

---

