# **0\. Front Matter**

**Title:** PF06-Canon-Epic-Process-Guide 

**Version:** v1.2.8

**Status:** Canon

**Effective date**: 2025-12-23

**Last Update Gate:**  BN 8.5.3 Drain A26-29

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

**Repo-doc and docs-only changes must be evidence-backed.**  
 Any PR that changes repo documentation (including “docs-only” PRs) **MUST** ensure that substantive behavioral claims are grounded and reviewable. In particular, claims about CLI behavior, exit codes, payload shapes, numeric posture, and parity expectations **MUST** be supported by at least one of:

* a titles-only pointer to the canonical PF doc that owns the claim, **or**

* a targeted repo test run whose output is referenced in the PR summary (commands and outcomes), **or**

* an existing governed evidence artifact path already committed under governed roots.

**Canon mismatch posture (docs-only PRs).** If a docs-only PR documents current repo behavior that appears to diverge from a canonical PF home (for example CLI exit codes vs *HDE-CLI-API-Vendor-Ref*), the PR **MUST**:

* state plainly that the text reflects **repo-tested behavior** (citing the test/evidence used), and

* state that the PF doc remains the **single home** for the normative contract (titles only), and

* include a Doc-Delta note routing the reconciliation into the canonical home (update canon or update code) rather than implying “canon is satisfied.”

Docs-only PRs **MUST NOT** claim “conforms to PF-Canon” when the PR’s own evidence indicates an implementation-vs-canon mismatch.

Docs-only PRs **MUST NOT** introduce unverified assumptions (for example inventing unsupported CLI flags or asserting output formats not proven by canon/tests/evidence). If the evidence is missing, treat it as a spec gap and fix the spec or add the proof, rather than “fixing docs by habit.”

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

**PF14 scope guard (doc roles).** *HDE-Mechanics Guide* (PF14) is a components and operational-surface reference. It **MUST NOT** define, rename, alias, or curate acceptance tokens, and it **MUST NOT** be used as a planning authority for acceptance language. Token registry, naming, semantics, and enforcement remain governed by their single homes (titles only).

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

CodEx. Executes in a sandbox, runs Audit and Build/Test, opens the PR automatically using the template, and attaches the close pack and the PASS list. Adapts within scope and reports all changes. CodEx can read PF docs. Even so, the IA **SHOULD** paste execution-critical material verbatim during build sessions (formats, schemas, exact token names, commands, and artifact paths) to keep a stable, unambiguous in-session reference and to reduce drift.

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

Live QA via a QA harness is a required Close Gate stage for **every epic**. See §3.5.2.8 for the harness-run and evidence-landing requirements.

These requirements are execution and Close Gate deliverables. They MUST NOT be treated as prerequisites for Epic Plan approval and MUST NOT force a detailed Live QA runbook into PLAN/CRD or Implementation planning.

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

### **Single homes (titles-only)**

* Transport bytes and CLI/Reader flows → HDE-CLI-API-Vendor-Ref.  
* Token semantics and ops policy (A7, refusal, writers) → HDE-Governance.  
* Canonical JSON, pack/manifest, Human Evidence Index, and machine mirror → HDE-Schemas & Artifacts.  
* Architecture boundaries and single-emitter rules → HDE Architecture.

Do not restate bytes, schemas, or token tables here.

---

### **Governed locations only**

Evidence artifacts and persisted logs must live under `artifacts/**` and `docs/**`. Transient/generator paths are disallowed. Header snapshots are normalized (lower-cased names; verbatim values), LF-terminated.

**Path normalization.**  
Proof files must live under governed paths (`artifacts/**` and `docs/**`). Transient/generator paths (e.g., `codex/out/**`) are not authoritative and MUST NOT be indexed; relocate before gating.

---

### **Same-PR parity (mandatory)**

When proofs or artifacts change, update all three in the same PR that carries the change:

* the human Evidence Index `docs/evidence/INDEX.json`,  
* the hash sentinel `docs/evidence/INDEX.sha256` (merge-gating), and  
* the machine mirror `artifacts/evidence_index.jsonl`.

CI enforces 1:1 join (human↔machine), and blocks on missing/mis-indexed items.

---

### **Human Evidence Index and sentinel are governed artifacts (path-proofs required)**

The following files are governed artifacts and MUST each have a co-located path-proof transcript that matches their on-disk bytes:

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.sha256.path_proof.txt`

Whenever either `INDEX.json` or `INDEX.sha256` changes, their corresponding `*.path_proof.txt` files MUST be refreshed in the same PR. The canonical evidence updater is expected to refresh these proofs during normal runs and to fail in check mode if they are stale.

---

### **Mirror hygiene (PF12 schema)**

The mirror is records-only canonical JSONL (UTF-8, compact, exactly one LF), unknown-keys rejected, ASCII field order, sort-before-write, single mirror file.

Each record must include:

* artifact\_key  
* role  
* sha256  
* size\_bytes  
* produced\_at\_utc  
* discovered\_physical\_path  
* proof\_anchor (transcript anchor \+ co-located path-proof)

---

### **Governed evidence drift remediation (hard stop)**

If any governed evidence artifact’s recorded metadata (sha256 or size) does not match the physical bytes on disk (for example a `*.path_proof.txt` transcript or a machine mirror record disagrees with the artifact), treat it as a hard stop:

* Do not hand-edit governed artifacts (Index, mirror, path-proofs) to “make checks pass.”  
* Remediate by regenerating using the canonical evidence tooling (single writer) so that:  
  * artifact bytes,  
  * co-located path-proof transcripts, and  
  * machine mirror metadata  
    are coherent.  
* After regeneration, run the tool’s check mode under determinism pins and closed rails (titles-only routing) to confirm the drift class is resolved before merge.

---

### **Evidence validation special cases (self-record \+ validator dependencies)**

**Canonical machine mirror path (single home).**  
The only canonical machine mirror file is `artifacts/evidence_index.jsonl`. Plans/PRs MUST NOT introduce alternate “mirror” files under `docs/evidence/**` (for example `docs/evidence/INDEX.machine_mirror.jsonl`). If such a path appears in tools/CI output, treat it as drift or a tooling bug and resolve it before close.

**Self-record proof semantics (high-risk).**  
The Evidence Index and the machine mirror are themselves governed artifacts that may be indexed and path-proofed. When a PR changes evidence tooling or changes how index/mirror/path-proofs are generated or validated, the PR MUST include an explicit self-record regression check (for example a dedicated test that validates mirror self-record proof SHA semantics) and must capture diagnostics that clearly show expected vs found digests when failures occur.

**Validator dependency policy (CI stability).**  
Any evidence validator (scripts or tests) that depends on non-core packages MUST have an explicit dependency posture:

* Either the dependency is required and installed in CI, or  
* the validator must skip cleanly with an explicit message (no import-time hard failure).

This prevents CI-only failures that block merges without changing product behavior.

---

### **Ops rails refusal proof (closed-rails)**

Capture a single-file refusal proof at `artifacts/proofs/ops_refusal_proof.txt` containing: required headers, one blank line, and an LF-terminated numeric-free JSON body. This artifact is governed by HDE-Governance (refusal/writers policy; tokens by title) and indexed per HDE-Schemas & Artifacts (mirror/proof\_anchor, records-only JSONL, one LF, unknown-key reject).

---

### **Merge gate (path-proofs required)**

Every indexed artifact must have a co-located path-proof referenced by proof\_anchor; CI blocks the merge if any path-proof is missing or mis-indexed. Same-PR parity (human index \+ hash sentinel \+ machine mirror) remains mandatory.

---

### **Proof surface routing (A7)**

Success-path proofs run only on a cataloged JSON success route (Endpoint Catalog). The `/internal/version` ops surface is excluded from A7 and governed by policy in Governance. Capture GET, HEAD, 304 (304 omits both Content-Type and Content-Length), required `Vary: Authorization, Accept-Encoding`, and encoding-invariance. Env-gate headers proof is required. (Titles-only pointers; bytes live in PF05; evidence lives in PF12.)

---

### **Endpoint Catalog single home (titles-only)**

The only authoritative Catalog path is `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256`. The Catalog lists JSON success routes only, each with an env-gate; all `/internal/*` routes are excluded. A7 proofs must run on a Catalog success route, and an env-gate headers proof is required.

---

### **Reader A7 proof JSON (machine-checkable)**

Epics that ship Reader A7 must produce a single proof JSON (records-only, canonical) containing: route\_path, env\_gate, GET/HEAD/after-304 header captures, ETag, vary\_has\_auth, vary\_has\_accept\_encoding, and encoding\_invariance\_ok. Proof JSON and indices update occur in the same PR.

---

### **CRD routing**

Thoth receives the CRD only. Keep process artifacts (PLAN/CRD/Doc-Delta) titles-only and route to single homes for bytes/evidence.

---

### **Cross-doc references**

Use titles only for all external references; do not duplicate transport bytes, schemas, or acceptance rosters in this guide.

---

### **Evidence skeleton coherence (Index/Mirror \+ topology orientation)**

When a PR adds or changes governed evidence and therefore updates any of: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, or `artifacts/evidence_index.jsonl`, the PR MUST also refresh the topology orientation demo artifact and its co-located path-proof:

* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

If the orientation demo is not refreshed to match the current evidence skeleton, the standard check fails with ORIENTATION\_DRIFT.

---

## **0.5.1 Epic path normalization (close-pack \+ QA root)**

This guide uses normalized epic identifiers for file paths. Plans, QA ledgers, Evidence Index entries, and machine mirror records MUST use these canonical patterns and MUST NOT introduce alternate spellings.

### **Epic number ()**

is the zero-padded 3-digit epic number (example: 022). When an epic ID is HDE-EPIC022, then is 022\.

### **Close-pack filenames (canonical)**

Epic close-pack artifacts MUST use:

* `audit/EPIC-<NNN>_close_report.md`  
* `audit/EPIC-<NNN>_MANIFEST.json`

Do not create parallel close-pack artifacts under alternate spellings (examples of disallowed alternates: EPIC022, EPIC\_022, audit/epic-022/...).

### **Epic QA root (canonical)**

Epic QA root directories MUST be lower-case and MUST use:

* `audit/qa/hde-epic<NNN>/` (example: `audit/qa/hde-epic022/`)

When this guide uses `audit/qa/<epic-id>/...`, `<epic-id>` means the canonical lower-case QA root slug `hde-epic<NNN>`.

Plans and implementations MUST NOT introduce parallel alternate spellings for the same epic (examples of disallowed alternates: audit/QA/..., audit/qa/HDE-EPIC022/..., audit/qa/hde-epic022-v2/...).

### **Legacy artifacts**

If legacy artifacts exist under non-canonical names, treat them as deprecated. Do not create new artifacts under deprecated patterns.

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

**Deterministic parity scenario requirement (acceptance).** Any new or expanded error parity scenario used for acceptance (including DB-unavailable and closed-rails vendor attempt scenarios) **MUST** be reproducible under determinism pins \+ **closed rails**, without reliance on external network or a live database.

Preferred posture: exercise the real codepath using a deterministic failure trigger (controlled injection or harness-level deterministic failure), producing stable envelopes and stable stored artifacts.

Allowed fallback: if real-codepath deterministic triggering is not feasible, use a deterministic stub layer only to the extent required to produce the canon error envelope and parity artifacts (no live I/O).

Acceptance proof **MUST** consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and must be indexable under governed evidence surfaces (human index \+ machine mirror in the same PR).

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
* Codespaces Step-0 snapshot (required for Codespaces Live QA).  
  * When Live QA steps are executed from Codespaces (whether as a prod-facing console or as an artifact sink), the Live QA runbook **MUST** begin with a mechanical Step-0 “Codespaces snapshot” capture that records the run-relevant environment context (rails posture, determinism pins, required variable presence/absence, and tool health signals) into the epic QA root under `audit/qa/<epic-id>/...`.  
  * This guide does not define the Codespaces configuration checklist or the snapshot schema. The **Glow QA Guide** is the single home for Codespaces configuration and requirements; this guide only requires that the runbook performs the Step-0 snapshot and that the snapshot artifact is stored under the canonical QA root and referenced from the run’s evidence.  
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

**Rule (global).** All directories in the repository and application codebase **MUST** use lowercase ASCII names.

* Introducing any mixed-case or uppercase directory name is **non-conforming**.  
* Under governed roots (for example `audit/**`, `docs/**`, `artifacts/**`), mixed-case directories are a **QA failure**, not cosmetic drift.

**Remediation posture (when drift exists).** If mixed-case directories exist, they are treated as legacy drift and **MUST** be normalized to lowercase, not copied forward into new work.

**Evidence discipline for renames.** Any renames that affect governed artifact paths **MUST** be accompanied by the required index and mirror updates (Human Evidence Index, Machine Mirror, and path-proofs) in the same PR, per the evidence discipline.

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
* Live QA execution is **gitless** (runbook scope). Live QA runbooks **MUST NOT** include git operations of any kind, including (non-exhaustive): `git status` gating, branch creation, add/commit/push, or PR creation.  
* Live QA PASS/FAIL **MUST NOT** be determined by working-tree cleanliness.  
* If any git information is captured at all, it is **traceability-only** and **MUST NOT** block execution or acceptance decisions.  
* Known Codespaces packaging artifacts are **non-blocking**. If the working tree shows environment-generated changes during a Live QA run (for example Python packaging metadata), runbooks **MUST** treat them as non-QA noise and **MUST NOT** delete, restore, or “clean” them as part of Live QA.  
* Live QA evidence gating remains **artifact-based**. Runbooks **MUST** validate steps by the presence and contents of mechanically generated artifacts under the canonical QA root (`audit/qa/<epic-id>/...`), not by repository state.

### **0.6.9 Plans are pointers; QA planning is post-implementation**

**Core rule:** An Epic PLAN and CRD are *pointers* to canon and governed artifacts. They are not the place to restate or rebuild canon (token definitions, schemas, CLI semantics, env matrices, etc.).

1. **Do not rebuild canon inside an Epic PLAN/CRD**

* The PLAN/CRD may reference canonical docs by **title only** and point to canonical artifact paths.

* If review “needs” more definition than canon provides, the correction is a **doc-delta** (update canon) or a governed artifact — not duplicating canonical content inside the PLAN/CRD.

2. **QA planning happens after implementation (and after D0 discovery)**

* A step-by-step QA plan (Live QA step lists, per-step Deliverables blocks, copy/paste command blocks, harness invocation details, etc.) is **not** an Epic Planning deliverable.

* The PLAN/CRD SHOULD provide only:

  * titles-only acceptance intent (what must be true),

  * the QA posture (e.g., “Live QA required”), and

  * pointers to where QA artifacts will live.

* The detailed **QA Plan** is authored/updated during implementation and QA work, and must satisfy the mechanical evidence requirements in §0.6.7 and §1.1.4–§1.1.8.

3. **Approval posture: avoid planning stalls**

* Reviewers SHOULD NOT block PLAN/CRD approval by demanding:

  * a full token/evidence matrix embedded in the PLAN/CRD, or

  * a fully specified Live QA step list before implementation exists.

* If a token name/semantics is unclear at planning time, treat it as **Deferred** (out of scope) and capture the dispute as an ADR/doc-delta rather than debating inside the PLAN.

4. **Token/evidence matrix is a QA ledger artifact**

* When a token/evidence matrix is required for an epic, it is maintained as a governed QA ledger under the epic’s QA root (see §1.1.9). The PLAN may contain a one-line pointer; it must not embed the matrix. The QA root will be filled in during implementation.

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

* When a QA branch or plan claims to exercise **prod via Codespaces** for an HDE epic, it **must** include at least one simple **prod handshake** that proves the commands are talking to the canonical production HD Engine service and DB (as defined in Glow Infrastructure). A typical handshake is a `curl` to the production HD Engine base URL’s `/internal/version` endpoint from within Codespaces, with the full response captured under `audit/qa/<epic-id>/logs/`. QA that omits this handshake is treated as **underspecified** until the handshake and its artifact are added.

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

For Live QA epics, **mechanical, step-explicit QA** is still required — but it belongs in the **QA Plan** (and, where relevant, the **Implementation Plan**), not embedded inside the Epic **PLAN/CRD**.

**PLAN/CRD posture (planning-time)**

* The Epic PLAN/CRD SHOULD NOT embed the Live QA step list or command blocks.

* The Epic PLAN/CRD MUST provide:

  * titles-only acceptance intent,

  * the QA posture (e.g., “Live QA required”), and

  * a pointer to the QA Plan (titles-only reference) and the epic QA root (`audit/qa/<epic-id>/...`).

**QA Plan posture (execution-time)**  
 For each Live QA step, the QA Plan MUST specify:

* **Command(s) to run** (copy/paste runnable; no guessing).

* **Pass/fail checks** (what is asserted, and what constitutes failure).

* **Deliverables**: exact file artifacts to be produced/updated, with paths under `audit/qa/<epic-id>/...`.

* Any required **context** (env assumptions, flags discovered in D0, required fixtures), expressed as concrete preconditions.

No manual-result placeholders (hard rule).  
 Live QA plans and runbooks **MUST NOT** include instructions that require the operator to manually fill results (for example “Result: (fill PASS/FAIL/SKIPPED)” or equivalent). Step outcomes must be determined mechanically from the step’s commands and the resulting artifacts under `audit/qa/<epic-id>/...`.

If a plan cannot express a step outcome as commands \+ checks \+ deliverables, that step is **non-conforming** and must be rewritten or removed.

If a QA Plan step cannot be expressed mechanically (commands \+ deliverables \+ checks), it is not a valid Live QA step in this process.

### **1.1.5 Live QA behavior vs artifact pattern**

For Live QA work, **runtime behavior** and **governed evidence artifacts** are not the same thing. The QA Plan MUST describe them as two distinct phases where applicable.

1. **Behavior execution phase**

* Run the system/endpoint/harness step that exercises the behavior being tested.

* Treat this phase as producing *signals* (responses, logs, outputs) that inform what evidence must be captured, but do not treat “it worked when I ran it” as the evidence artifact.

2. **Artifact capture \+ analysis phase**

* Capture governed evidence artifacts under `audit/qa/<epic-id>/...` (and related required closeout artifacts).

* Perform analysis offline (e.g., in Codespace), producing the required summaries, diffs, and verification notes as governed artifacts.

**Rule:** A Live QA step is not complete unless the artifact phase produces the specified deliverables in the QA root (or other governed locations referenced by Evidence Index/Machine Mirror), even if the behavior phase “looked correct” during execution.

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

This section defines **planning \+ review \+ closeout rails** for epics that introduce or consume **QA Acceptance Tokens**.

#### **1.1.9.1 Two axes reminder: PF23 audit scope vs PF19 token semantics**

* **PF23 audits** govern whether particular audit steps are required and how they are executed.

* **QA Acceptance Tokens** remain governed by their canonical registry (names \+ semantics). Waiving, narrowing, or skipping PF23 audits does **not** waive token fidelity requirements.

#### **1.1.9.2 Token scope discipline (prevent planning stall)**

Every Epic PLAN/CRD or Implementation Plan that references QA Acceptance Tokens MUST classify referenced tokens into exactly one of these sets:

* **In-scope tokens**  
   Tokens this epic will **claim** (i.e., tokens that appear as acceptance proofs / closeout claims).

* **Deferred tokens**  
   Tokens identified during planning/discovery, but explicitly **out of scope** for this epic. Deferred tokens must not be claimed as acceptance proofs for this epic.

* **Informative tokens**  
   Tokens mentioned only for context (e.g., “related existing token exists”), but not claimed and not evidence-wired for this epic.

**Planning-time rule (no invention):** If a token’s canonical name/semantics cannot be identified via canon or an explicit epic-specific approval, it MUST be treated as **Deferred** (or removed). Do not invent local aliases/synonyms.

**Reviewer rule (anti-stall):** Token naming disputes should not stall PLAN/CRD approval; classify the token as Deferred and capture the dispute as ADR/doc-delta rather than debating inside the PLAN.

#### **1.1.9.3 Split the checkpoints: Plan approval vs QA ledger completion**

This process separates two checkpoints, but token fidelity is enforced at both.

**Stage A — PLAN/CRD approval (planning-time)**  
 A PLAN/CRD may be approved only if:

* It includes a titles-only acceptance roster (what must be true), and

* It includes a Token Scope block with stable names for in-scope tokens, and

* For any epic that introduces or consumes **QA Acceptance Tokens**, reviewers MUST construct (explicitly or as a checked artifact) a **token/evidence matrix** for all **in-scope** tokens.

Stage A token/evidence matrix rule (hard):

* **No in-scope token** may have any cell in the token/evidence matrix marked as “e.g.”, “TBD”, or left implicit at approval time.

* If a token row cannot be completed without guessing, that token **MUST** be removed from in-scope and treated as **Deferred**.

* A PLAN/CRD **MUST NOT** be marked approved (ASK OK) **for that token** while any row is incomplete or uses placeholders.

Stage A may still defer detailed Live QA runbooks into QA execution artifacts per §1.1.4–§1.1.6, but token naming and token→evidence wiring (by titles/paths/keys) must be explicit.

**Stage B — Closeout readiness / Live QA completion (execution-time)**  
 Before an epic is considered closeout-ready, the QA ledger must be complete for all in-scope tokens, and the token/evidence matrix must match reality:

* the planned tests/CI jobs/Live QA steps exist and were executed as applicable,

* the governed evidence artifacts exist under governed roots, and

* the Evidence Index \+ Machine Mirror entries referenced by the matrix exist and are coherent.

Stage B is verification of the Stage A matrix against produced evidence; it is not a second chance to “finish naming” or “decide token spellings.”

#### **1.1.9.4 Token/evidence matrix is a QA ledger artifact (not embedded in the PLAN)**

The token/evidence matrix is the governed QA ledger that binds each **in-scope QA Acceptance Token** to:

* tests (unit/integration),

* CI enforcement under closed rails,

* Live QA steps (if applicable),

* governed evidence artifacts (paths), and

* Evidence Index \+ Machine Mirror entries (keys and proof anchors).

The matrix MUST NOT be embedded inside the Epic PLAN/CRD. The PLAN may include a pointer line to the matrix location (typically under the epic QA root).

**Matrix completeness rule (applies at Stage A for in-scope tokens).**  
 For every token that is **in scope** for the epic at PLAN/CRD approval time, the token/evidence matrix MUST have a complete row. No “e.g.”, “TBD”, “??”, or implicit cells are permitted for in-scope tokens at approval time.

**Row schema (minimum required fields).** Each in-scope token row MUST include:

* **PF19 registry name** — the canonical QA token name (no aliases).

* **Acceptance map / manifest token name** — MUST exactly match the PF19 registry name (no epic-local synonyms).

* **Tests** — the unit/integration tests that exercise the behavior (by identifier or path).

* **CI jobs** — the CI job(s) that enforce the behavior under closed rails (by job name).

* **Live QA steps** — step identifiers that demonstrate the token (if applicable), pointing to the epic QA root.

* **Evidence artifacts (paths)** — governed repo-relative artifact paths produced by those tests/steps.

* **Evidence Index \+ Machine Mirror entries** — the `artifact_key`(s) and the expected proof anchoring posture for each artifact:

  * `artifact_key`

  * `epic_id`

  * `tokens` (the PF19 token name)

  * `proof_anchor` (to the co-located path-proof)

If any in-scope token cannot satisfy this schema without guessing, the token MUST be removed from in-scope (Deferred) before approval.

**Uniqueness requirement (always).**  
 The token/evidence matrix MUST contain exactly one row per in-scope token. Duplicate rows for the same token are mechanical blockers and must be removed before approval.

**Draft scaffolds (not approvable).**  
 Draft matrices may exist during plan drafting, but a PLAN/CRD cannot be marked approved (ASK OK) for any token while its row contains placeholders or missing fields.

#### **1.1.9.5 PF19 is the single home for token semantics (no local synonyms)**

QA Acceptance Tokens are centrally defined in the QA Acceptance Tokens registry in the Glow QA Guide (PF19). Epics only consume them.

Rules:

* Any QA Acceptance Token used in an acceptance map or manifest MUST use the PF19 registry name exactly.

* Epic-level documents (HDE-Phased Epics records, acceptance maps, manifests, build notes addenda, implementation plans) MUST NOT invent epic-local token names, aliases, or synonyms for existing PF19 semantics.

* If an epic truly needs a new token, that need MUST be recorded as a PF19 doc delta (NEW CANON or CANON UPDATE) and resolved in PF19 before the epic is considered token-complete for that token.

Epic-specific approvals may select a token name for the epic ahead of PF19 drainage (see §1.1.9.8), but they do not authorize multiple competing spellings or local aliases.

#### **1.1.9.6 No silent downgrades**

Once a reviewer has identified token naming or token→evidence wiring as a **blocking issue** (for example missing PF19 entry for a used token, placeholder “e.g./TBD” cells in the token/evidence matrix, or incomplete token→artifact bindings), that blocker MUST NOT be downgraded to “non-blocking” in a later review unless:

* the plan/acceptance artifacts have been updated to resolve the issue, **or**

* PF-Canon has been explicitly updated to resolve the issue (for example PF19 registry update).

Any downgrade MUST reference the specific resolving change (plan diff and/or PF-Canon change). A change in reviewer interpretation or scope alone is not sufficient.

#### **1.1.9.7 Scope waivers must be explicit and non-transitive**

If the Product Owner or governance chooses to waive or narrow a canon requirement for a particular plan (for example, “PF23 audits are out of scope for this plan”), reviewers MUST:

1. Record the waiver as a local scope directive in the PLAN/CRD, and

2. State explicitly that other rails remain fully in force, including:

   * PF19 QA token naming/semantics (Glow QA Guide),

   * PF12 evidence/index/mirror rules (HDE-Schemas & Artifacts),

   * PF20 D-goals and token rosters (HDE-Phased Epics), and

   * PF09 CI/QA rails (HDE-Build Checklist).

Such waivers MUST NOT be interpreted as permission to relax token naming, acceptance mapping, evidence wiring, or index/mirror discipline.

#### **1.1.9.8 Re-ground before asserting “no canonical token name exists”**

Before any reviewer asserts “no canonical token name exists yet” for a QA behavior, they MUST:

1. Re-check the PF19 QA Acceptance Tokens registry for an existing token that covers the behavior, and

2. Re-read any epic-specific approvals or remediation guides that may already have selected a token name and semantics for this behavior.

If an epic-specific approval defines a token name (even if PF19 has not yet been updated):

* Plans, acceptance maps, and token/evidence matrices MUST treat that name as canonical for the epic (no alternate spellings), and

* PF19 becomes the drainage target (doc-delta) to register/standardize the token; PF19 is not a license to invent new names in the meantime.

If neither PF19 nor an epic-specific approval provides a token name that can be used without guessing, the token MUST be deferred out of scope rather than invented.

#### **1.1.9.9 Token value rubric \+ token budget (reduce token sprawl)**

**Do not admit noise tokens.** A QA Acceptance Token should represent an acceptance invariant that can be mechanically evidenced. Do not create tokens for workflow facts (e.g., “docs were read”, “PR was opened”, “a human checked something”).

**Default token budget:** 0 new tokens per epic.  
 **Exception:** up to **≤ 3** new tokens may be introduced only with explicit justification and an ownership plan (doc-delta path). More than 3 requires an explicit governance decision.

#### **1.1.9.10 AB/BA composite identity token name (canonical)**

The only canonical acceptance token name for AB/BA composite identity is:

* `COMPOSITE_ABBA_IDENTITY_OK`

Any alternate spellings or legacy variants are non-canonical and **MUST NOT** appear as acceptance tokens in:

* Epic Plans,

* acceptance maps, or

* token/evidence matrices.

If an epic inherits legacy wording from a document, the PLAN may include a one-line clarification (example: “legacy name → canonical `COMPOSITE_ABBA_IDENTITY_OK`”), but the claimed token name remains canonical.

### **1.1.10 PLAN submission preflight (mechanical gate: tokens \+ evidence paths)**

This section defines a **mandatory preflight** that must pass before an Epic PLAN is considered approvable. It is designed to prevent plan churn caused by missing close-pack items, unregistered tokens, and misbound evidence paths.

#### **1.1.10.1 Close-pack completeness (plan-authoring gate)**

A PLAN is **non-conforming** unless it explicitly includes the close-pack baseline:

* the complete close-pack file set (by path, titles-only), and  
* the required close-pack acceptance marker (titles-only).

This is a plan submission gate, not a “later Close Gate reminder.”

#### **1.1.10.2 Token registry validation (no unregistered acceptance tokens)**

Acceptance tokens referenced in an Epic PLAN are governance-controlled names and **MUST** match the canonical token roster.

**Validation gate (mechanical).** Every token name listed in:

* the PLAN acceptance roster (Stage A), and

* the token/evidence matrix (Stage B, when used)

**MUST** be validated against the canonical token roster before a plan can be approved.

* Unregistered token names are **mechanical blockers**. They are not style issues and must not be “interpreted.”

**No ad-hoc new tokens during revise/resubmit.** During a revise/resubmit planning loop, the plan **MUST NOT** introduce new acceptance tokens unless:

* explicitly requested by Lead review, **or**

* required due to a clearly identified canon gap.

Default posture when a behavior must be enforced and no token exists:

* state it as a **non-token mechanical requirement** under the deliverable and prove it via tests/evidence, rather than tokenizing it.

**If (and only if) a new token is genuinely required, it must be routed, not invented.** A plan may propose a new token only when all of the following are true:

1. **ADR present in the plan.** The ADR explicitly states:

   * proposed token name,

   * one-sentence semantics,

   * intended evidence surface(s) (paths/titles only), and

   * drain targets (titles only).

2. **Conflict/synonym check performed.** The plan records that the proposed token name does not duplicate or alias an existing canonical token.

3. **Doc-Delta required.** The token is registered via Doc-Delta in the canonical token home **before** it can be required as an acceptance claim.

Until registered, the token may be tracked as a proposed ADR item, but it **MUST NOT** appear as a required acceptance claim in PLAN/CRD, acceptance maps, or token/evidence matrices.

#### **1.1.10.3 Evidence bundle completeness for local-bundle deliverables**

When a deliverable claims a “local bundle” of governed artifacts under a directory (example: `artifacts/ops/internal_version/*`), the PLAN **MUST** explicitly state:

* the complete required bundle paths (titles-only, full paths, no byte restatement), sourced from the canonical bundle definition, and  
* any shared or global governed artifacts required for acceptance that live outside the local bundle root, including canonical paths.

If the plan references a canonical bundle definition section by title instead of listing all paths, it must still list:

* any overrides, exclusions, or additions, and  
* any shared/global evidence outside the local bundle root.

#### **1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)**

Every acceptance token to artifact binding that appears in an Epic Plan and in the token/evidence matrix **MUST** be validated against the canonical evidence catalog before approval or merge.

If the evidence catalog defines a fixed canonical path for a token’s evidence surface:

* the plan and matrix **MUST** bind to that exact path.

**Determinism env pins is a single canonical evidence surface.** 

When `DETERMINISM_ENV_PINS_OK` is claimed, the only valid evidence surface is:

* `audit/gates/determinism/env_pins.log`

* `audit/gates/determinism/env_pins.log.path_proof.txt`

`DETERMINISM_ENV_PINS_OK` **MUST NOT** be bound to `artifacts/proofs/env_pins.txt` (or any other similarly named file).

When `DETERMINISM_ENV_PINS_OK` is claimed, all acceptance ledgers and indices **MUST** bind to the canonical log path, and parity **MUST** be consistent across:

* token/evidence matrix row,

* `docs/evidence/INDEX.json`,

* `artifacts/evidence_index.jsonl`, and

* the `proof_anchor` path-proof.

Any deviation is a mechanical blocker: fix the binding, do not reinterpret.

Any binding to a non-canonical path is a mechanical blocker and must be corrected before approval. If a non-canonical path is truly required, it must be routed via ADR and drained into the correct canonical home.

When a token is claimed as satisfied, the following artifacts **MUST agree** (paths and keys must match):

* Epic Plan required evidence list (per deliverable)  
* token/evidence matrix row for the token  
* `docs/evidence/INDEX.json` entry for the bound artifact  
* `artifacts/evidence_index.jsonl` mirror record for the same `artifact_key` and `discovered_physical_path`  
* the path-proof file referenced by `proof_anchor`

This validation is enforced as a human review checklist line (pass/fail). An automated validator may be added, but the rule does not depend on automation

#### **1.1.10.5 PF09 subtask closeout (evidence-binding first)**

When an epic claims closure of a PF09 task or subtask that is described as “captured elsewhere” or “piecemeal,” the default closure method is:

* bind existing governed evidence (tests \+ artifacts) into the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix), rather than creating new evidence families.

Creating a new evidence family for closeout is allowed only if:

* the PLAN includes an explicit gap statement (“what is missing from existing evidence”), and

* the new evidence aligns to governed artifact conventions (titles-only routing to the evidence catalog).

Closure is not considered complete unless the acceptance artifacts explicitly map the PF09 task/subtask to concrete evidence (no implicit “it exists somewhere else” posture).

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

## **1.3 CRD: Machine header (copy/paste)**

epic\_id: "HDE-EPIC0XX"  
 crd\_id: "HDE-CRD0XX"  
 type: CRD  
 scope\_mode: FULL | PATCH | VERIFY  
 acceptance\_proofs:  
 \# "A7\_PROOF\_PRESENT" etc (titles only)  
 \- "..."

evidence\_minima:  
 \# Reader A7 proofs (required when any A7 proof token is claimed)  
 \- "Endpoint Catalog present under `audit/qa/<epic-id>/endpoint_catalog.json` (or equivalent) and referenced in Evidence Index"

\# CLI parity artifacts (required when CLI parity is in scope)  
 \- "CLI parity evidence: a CLI output capture \+ a REST response capture (paired) for each in-scope endpoint"

\# DB posture  
 \- "DB posture tokens evidenced (titles-only): DB\_RUNTIME\_SEARCH\_PATH\_OK, DB\_ROLE\_OK, DB\_SCHEMA\_FINGERPRINT\_OK, DB\_CONN\_ENV\_OK, DB\_BOUNDARY\_VIEW\_OK, DB\_WRITERS\_ISOLATED\_OK"

\# BodyGraph ingest (required when BG ingestion is in scope)  
 \- "BodyGraph ingest evidence: ingestion logs, payload snapshots (redacted), and verification artifacts under `audit/qa/<epic-id>/...`"

ops\_endpoints:  
 \- "..."

notes\_for\_coder:  
 \- "Short list: routing references, required harness notes, and any non-obvious constraints"

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

Define how the work proceeds after CRD approval in a way Codex can execute with minimal inference. Lead Dev approves once, then steps out except for the PR gate review. Codex can read PF docs. Even so, the Implementation Agent (IA) **SHOULD** paste execution-critical material verbatim during build sessions (explicit formats, schemas, exact token names, commands, and artifact paths) so the session has an unambiguous reference and avoids drift. Codex may adapt within approved scope and **MUST** deliver a detailed change report at the end. PR-first via Codex: Codex opens the PR automatically and attaches the close pack and PASS list; the PO is the sole merger (squash on PASS). Repo-docs (Doc-Delta) and the evidence index/mirror trio **MUST** be updated in the same PR whenever proofs or governed artifacts change.

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

codex: "Performs Audit and Build/Test; opens PR automatically per execution\_flow; adapts within scope; returns detailed change report \+ artifacts; can read PF docs, but relies on IA-pasted verbatim formats/snippets for execution-critical material to avoid ambiguity."

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

codex\_can\_see\_pf\_docs:true

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
"verbatim\_payloads": \["\<components\>", "\<schemas\>", "\<formats/snippets\>"\], // CodEx can read PF docs; still paste execution-critical material verbatim to keep an unambiguous in-session reference  
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

The close PR **MUST** include the epic close-pack (canonical filenames):

* `audit/EPIC-<NNN>_close_report.md`

* `audit/EPIC-<NNN>_MANIFEST.json`

Where `<NNN>` is the zero-padded 3-digit epic number (see §0.5.1).

The close PR **MUST** also include:

* PASS tokens section (final status; titles only; see §0.2 “Baseline PR tokens (titles-only)” and the PLAN/CRD machine headers)

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

  #### **3.5.2.8 Live QA via harness (required for epic closeout)**

Every epic **MUST** complete a Live QA stage via a QA harness before it can be considered closeout-ready.

This section is process guidance only. It does not define harness implementation details; those are owned by the Glow QA Guide and the HDE-Mechanics Guide (titles only).

**Workflow placement (Close Gate work product).** The detailed Live QA plan/runbook (commands, step checks, QA\_ROOT structure, and evidence landing mechanics) is authored as a separate QA artifact during the Close Gate stage. It **MUST NOT** be treated as an Epic Plan prerequisite and **MUST NOT** be embedded into PLAN/CRD or Implementation planning. See §0.4.1 for required Live QA execution deliverables.  
 Minimum requirements (all epics):

1. **Live QA plan exists (titles-only).**  
    The epic **MUST** have a Live QA plan (runbook) that specifies:

   * the QA harness invocation (for example `--epic <id>`, `--run-id <id>` or equivalent),

   * closed-rails posture (env pins), and

   * expected evidence under `audit/qa/<epic-id>/...`.

2. **If the epic claims QA Acceptance Tokens, the plan must name the QA ledger artifacts by path.**  
    This includes the token/evidence matrix location (titles-only semantics) and any other governed ledgers required for close.

3. **Mandatory D0 Discovery artifact and QA RCA summary are present.**  
    The epic **MUST** satisfy the Live QA execution deliverables in §0.4.1:

   * a governed **D0 Discovery artifact** under the epic’s QA tree, and

   * a **QA RCA & Doc Delta summary** (as part of the close report or as a governed artifact referenced by it).

4. **At least one harness run executed in Codespaces.**  
    Before epic closeout, the plan’s harness entrypoint **MUST** be executed at least once in a GitHub Codespace attached to the canonical repo, producing governed evidence under `audit/qa/<epic-id>/<run-id>/...`.

5. **Live QA evidence landing is PR-first and parity-clean.**  
    Live QA evidence **MUST** land under governed roots and follow the same-PR evidence parity rule:

   * Live QA artifacts under `audit/qa/<epic-id>/...`, and

   * the index/mirror trio updates (Human Evidence Index, hash sentinel, Machine Mirror)  
      MUST land in the same PR.

6. Live QA evidence may land either:

   * inside the epic close PR, **or**

   * in an evidence-only QA PR (see §0.7 and §4.5) that merges before the close PR.

7. **Entrypoint regression test exists in CI (no governed evidence writing).**  
    Every entrypoint command documented in the Live QA plan **MUST** have a corresponding CI test that:

   * runs the entrypoint (or a logically equivalent variant) under the canonical env pins,

   * asserts that the expected QA\_ROOT layout and outputs are created and non-empty, and

   * fails if harness behavior regresses.

8. CI tests **MUST NOT** be treated as a source of governed evidence and **MUST NOT** require committing `audit/qa/<epic-id>/...` outputs to the repo.

9. **No QA-only epics that only test themselves.**  
    QA-heavy epics must deliver shared value. If an epic’s QA work does not upgrade shared QA tools/harnesses and does not strengthen Live QA coverage across multiple existing surfaces, the PLAN/CRD **MUST** be returned as non-conforming and re-scoped before approval.

Close Gate check:

* The close PR **MUST** confirm that Live QA evidence exists under governed roots and is indexed (Human Evidence Index \+ hash sentinel \+ Machine Mirror), and it must ensure the epic’s close-pack references the existence of this Live QA evidence by title and path (no URLs required).  
   

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

#### **3.5.2.6 /internal/version tokens (when in scope — ops surface)**

When `/internal/version` is in scope, the close PR **MUST** satisfy (titles only):

* `INTVER_200_CTYPE_JSON_UTF8_OK`

* `INTVER_HEAD_PARITY_OK`

* `INTVER_CONDITIONALS_IGNORED_OK`

* `INTVER_200_NO_ETAG_OK`

**Coupling \+ two-run identity proof (single governed artifact).** The governed proof artifact for `/internal/version` coupling \+ two-run identity is a single log artifact:

* `artifacts/ops/internal_version/two_run_identity.log`

This log **MUST** include, at minimum:

* Two-run identity result (explicit pass/fail that two consecutive captures are byte-identical, with compared digests/identifiers).

* Coupling verification result (explicit pass/fail checks that the `/internal/version` fields match their governing identity sources by title/path reference, including `release_id` coupling).

* Rails posture \+ determinism pins reference (names-only pointers; determinism pins themselves remain proven by their canonical evidence surface).

No new acceptance tokens are introduced for “coupling proof.” Coupling proof is evidence bound under the existing `/internal/version` token set and identity acceptance posture.

When this log is produced or updated, it **MUST** be indexed and mirrored (human index \+ hash sentinel \+ machine mirror) in the same PR.

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

* If any required governed file or index/mirror update is missing, **do not merge**. Ask the IA to have CodEx amend the current PR so the missing items land in the same PR before squash-merge.

* Verify this PR contains, as required:

  * Doc-Delta (repo docs)

  * Human Evidence Index update (`docs/evidence/INDEX.json`)

  * Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`)

  * Machine JSONL mirror update (`artifacts/evidence_index.jsonl`)

* Wait for the Lead Dev gate review (PASS).

* On PASS, perform a squash merge, then notify the Scrum Master.

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

\#\#\# Ops — /internal/version coupling proof (if in scope)  
\- /internal/version two-run identity \+ coupling proof — artifacts/ops/internal\_version/two\_run\_identity.log  
\# single governed log artifact; bound under existing /internal/version token set; indexed \+ mirrored in the same PR when produced/updated

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
* **Build.** IA provides instructions \+ verbatim materials. CodEx can read PF docs. Even so, paste execution-critical material verbatim to keep an unambiguous in-session reference (formats, schemas, exact token names, commands, and artifact paths).  
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

**Purpose.** Define how to include large schemas or assets when content is too large to paste inline or when the workflow cannot rely on file attachments. This appendix preserves ownership, auditability, and single-home discipline while keeping execution mechanical and repeatable.

### **Constraints (facts)**

* CodEx can read PF docs, but may not have reliable access to large external assets via attachment workflows. Execution-critical formats and small schemas should still be pasted inline by the IA to keep an unambiguous in-session reference.  
* CodEx cannot accept file uploads as part of the build interaction; only IA-provided **inline** text/snippets and repo contents are used during build.  
* Only the **Product Owner (PO)** may load large files into the repo/PR branch when needed. Agents do **not** run git and do **not** create PRs.  
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

* Can read PF docs, but the IA **SHOULD** still paste execution-critical formats and small schemas/snippets inline to keep an unambiguous in-session reference and reduce drift.

* Uses IA-provided inline materials and repo contents during build.

* Proposes scoped adjustments; lists every change in the Detailed Change Report (files added, modified, removed; deviations and improvements).

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

