# **0\. Front Matter**

**Title:** PF06-Canon-Epic-Process-Guide 

**Version:** v1.0.2

**Status:** Canon

**Effective date**: 2025-11-25

**Last Update Gate:** BN 7.7.8 Drain A13

**tag:** INV-f2ac55d77ce9aacc

## 0.1 Purpose and scope

 This guide defines the epic delivery process for a human \+ pair-programming \+ CodEx workflow. It supplies paste-ready headers, checklists, and prompts; requires an Audit and a Sandbox Build/Test in each epoch; and sets Close to be **PR-first**. **CodEx automatically opens the pull request** and attaches the close pack and the **acceptance tokens (PASS) list**.  
 This is **process guidance only**. It does not constrain execution environments, repository tooling, or any transport or payload bytes (those remain in their canonical homes).

I get why your confidence is low here, and I’m going to keep this as simple and explicit as possible.

Below is **one cohesive block** for **§0.2–§0.7 of PF06**, with:

* **Markdown headings** (`## 0.2 …` etc.)

* **Your deltas applied**:

  * 0.2 fully replaced

  * 0.5 extended with ops-refusal \+ merge gate

  * 0.7 Allowed changes replaced \+ rails note in CI posture

* All other subsections (**0.3, 0.4, 0.6**) preserved.

You can paste this straight into your PF06 source and let Docs interpret `##` as Heading 2\.

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
 CodEx opens the PR `epic/<EPIC-ID>-<slug>`, pushes code, Doc-Delta (repo docs), the human Evidence Index, the machine JSONL mirror, and the close-pack (`audit/EPIC-<ID>_close_report.md`, `audit/EPIC-<ID>_MANIFEST.json`). The machine mirror is records-only, canonical JSONL, one LF per line, unknown keys rejected, each record with a `proof_anchor`.  
 Lead Developer gate review. Verify PASS tokens; verify A7 proof surface on the cataloged JSON success route (not `/internal/version`); verify env-gate proof and encoding invariance; verify same-PR evidence parity. Verify Endpoint Catalog single home present (`docs/ENDPOINTS_CATALOG.json` \+ `.sha256`) and Reader A7 proof JSON is captured and indexed (human \+ machine, same PR).  
 Product Owner merge. Perform squash merge on PASS and notify the Scrum Master.  
 Closure. IA files the Closure Report; boards and sprint reports updated; suites green-freeze until a qualifying change lands.

Determinism pins  
 Set `LC_ALL=C` and `TZ=UTC` for all capture and CI checks to keep bytes stable.

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

No background work.

No manual git.

No manually created PRs by agents.

Main is protected; squash merge is the only close path.

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
 Branch naming suggestion: `qa/<EPIC-ID>-<slug>`.  
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

* When a QA branch or plan claims to exercise **prod via Codespaces** for an HDE epic, it **must** include at least one simple **prod handshake** that proves the commands are talking to the canonical production HD Engine service and DB (as defined in Glow Infrastructure). A typical handshake is a `curl` to the production HD Engine base URL’s `/internal/version` endpoint from within Codespaces, with the full response captured under `Audit/QA/<EPIC-ID>/logs/`. QA that omits this handshake is treated as **underspecified** until the handshake and its artifact are added.【13:WCXnEc3R2LFdFyBrPKcjx9†file-WCXnEc3R2LFdFyBrPKcjx9†L3-L7】

* Rails default: CI/test harness runs **CLOSED** by default; any job that opens rails must pin policy and attach evidence in the same PR.

Acceptance (titles only)  
 `QA_EVIDENCE_ONLY_OK` — branch contains evidence updates only (no production code).  
 `QA_CI_DIFF_SCOPED_OK` — CI restricted to changed governed files passed.

---

# 1\) EPIC PLAN → CRD (Lead Dev) 

## 1.1 Workflow at a glance

 Draft the PLAN machine header (single post).  
 After one review, issue the CRD with the approved scope and acceptance tokens by title only (e.g., A3/A4/A7; no byte listings).  
 Finalize code-capsules before IP approval; capsules freeze at IP.  
 CodEx runs Audit \+ Sandbox Build/Test, then opens the PR automatically using the template. CodEx attaches the close pack and the PASS token list, and pushes code \+ Doc-Delta (repo docs) \+ human Evidence Index \+ machine JSONL mirror in the same PR.  
 Lead Dev gates the PR (verifies PASS tokens, A7 proof surface/env-gate/encoding-invariance when applicable, and 1:1 index↔mirror parity with path-proofs).  
 PO is the sole merger; squash-merge on PASS; inform Scrum Master. Suites green-freeze unless a qualifying change lands.

For some epics (for example, EPIC017 and similar Calcination/Separation passes), the work may be split into a **series of PRs (up to 10 PRs per epic)**, each PR carrying a self-contained slice with code \+ Doc-Delta \+ evidence. The PR-first pattern and same-PR parity apply to **each** PR; epic-level acceptance (as recorded in HDE Phased Epics) occurs only after all required PRs for that epic have merged.

When a PLAN or CRD for an HDE epic expects **Live QA “in prod via Codespaces,”** it **must** also:

* Name the production HD Engine **service and base URL** and the production **DB instance/schema** by title, routing to Glow Infrastructure as the single home for those names (do not invent new environment labels).

* State explicitly that **Codespaces is a QA console** that runs CLI/HTTP commands **against** that production service and DB, not a prod environment in its own right.

* Describe, at a high level, the **prod handshake** step and where its artifact will live (for example, “Step 0: `curl` the production `/internal/version` endpoint from Codespaces and store the output under `Audit/QA/<EPIC-ID>/logs/` before running deeper QA”).

PLAN/CRD entries that refer to “prod via Codespaces” without these clarifications are considered **incomplete** and must be updated before the epic moves into implementation or Live QA.

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

  \- "PR-first via CodEx: CodEx opens PR \`epic/\<EPIC-ID\>-\<slug\>\` and pushes code \+ Doc-Delta (repo docs) \+ Evidence Index (human JSON) \+ Evidence Index hash sentinel \+ machine JSONL mirror (records-only, canonical, one LF, unknown keys rejected, ASCII field order, sort-before-write, single mirror file; each record has discovered\_physical\_path and a proof\_anchor to a path-proof file) \+ close-pack files (audit/EPIC-\<ID\>\_close\_report.md, audit/EPIC-\<ID\>\_MANIFEST.json)."

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

### **3.5 Close Gate (PR-first)**

**Requirement.**

* For every epic, work is delivered **PR-first via CodEx**.

* CodEx opens PRs automatically for each epic slice and pushes **code \+ Doc-Delta \+ evidence** in the **same PR**.

* An epic MAY use **up to 10 PRs** to deliver its full scope; **each PR** must be self-contained and follow the PR-first and parity rules in §0.2.

* The Product Owner (PO) is the sole merger (squash on PASS).

* **Epic-level acceptance** (as recorded in **HDE Phased Epics**) occurs only after **all required PRs for that epic have merged** and the Close Gate has been satisfied.

The Close Gate applies to the **PR that carries the epic close-out** (“close PR”). All earlier PRs in the series must still be PR-first and parity-clean, but only the close PR is required to carry the full close-pack and final PASS roster described below.

---

**Close PR must contain**

**Close-pack files**

* `audit/EPIC-<ID>_close_report.md`

* `audit/EPIC-<ID>_MANIFEST.json`

* PASS tokens section (final status; titles only, see §2.0 roster)

**Core determinism & parity tokens**

* `DET_SERIALIZER_OK`

* `CLI_READER_PARITY_OK`

* `TWO_RUN_IDENTITY_OK`

**Index/mirror trio (same PR)**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK`

**Close-pack presence**

* `CLOSE_PACK_FILES_PRESENT_OK`

**When A7 is in scope (Catalog success route)**

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

* `ENDPOINTS_CATALOG_INTERNAL_OK`

* `A7_TRANSPORT_PROOF_OK`

**When `/internal/version` is in scope (ops surface)**

* `INTVER_200_CTYPE_JSON_UTF8_OK`

* `INTVER_HEAD_PARITY_OK`

* `INTVER_CONDITIONALS_IGNORED_OK`

* `INTVER_200_NO_ETAG_OK`

  ---

**Repo-docs & evidence updates (same PR)**

The close PR MUST update, in the **same PR**:

* Human Evidence Index: `docs/evidence/INDEX.json`

* Index hash sentinel: `docs/evidence/INDEX.sha256` (hash matches `INDEX.json` bytes)

* Machine mirror: `artifacts/evidence_index.jsonl` (records-only canonical JSONL; one LF; unknown keys rejected; ASCII field order; sort-before-write; single mirror file; each record has `discovered_physical_path` \+ `proof_anchor` to a co-located path-proof)

* Repo index and acceptance crib notes

* Doc-Delta note (if applicable)

**A7 artifacts** (include when A7 is in scope; titles only)

* Endpoint Catalog file \+ checksum:

  * `docs/ENDPOINTS_CATALOG.json`

  * `docs/ENDPOINTS_CATALOG.json.sha256`

* Env-gate headers-only proof:

  * `artifacts/proofs/endpoints_env_gate_proof.log`

* Composite success proof JSON (records-only; PF12 schema-validated):

  * `artifacts/proofs/reader_success_get_head_304.json`

  * Success headers: GET / HEAD / 304; writers/errors posture; encoding-invariance capture

  ---

**Merge**

* The **Lead Dev** performs the gate review on the close PR (checks PASS tokens, A7/ops applicability, index/mirror hygiene, governed locations only).

* The **PO** squashes on PASS.

* The **Scrum Master** is informed after merge.

* The **Implementation Agent (IA)** files the Closure Report and confirms that docs and evidence are synchronized in the merged PR.

---

Here’s a tightened, structured version of that whole block. I’ve kept every field, token, and artifact name; changes are only to wording, ordering, and clarity.

---

### **4\) PR & COMMIT PLAN (PR-first via CodEx; Lead Dev gates)**

#### **4.1 Machine header**

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

#### **4.2 Required pre-merge evidence (titles-only; CodEx supplies artifacts)**

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

#### **4.3 Guidance for PO (CodEx UI)**

* Do **not** create a PR manually. Confirm CodEx has opened the PR for this epic (PR ID present) and that the close pack \+ PASS tokens appear in the PR body.

* Verify this PR contains:

  * Doc-Delta (repo docs),

  * Human Evidence Index update, and

  * Machine JSONL mirror update,  
     as required. If any index/doc was omitted, ask the IA to raise an immediate docs-only PR.

* Wait for the Lead Dev gate review (PASS).

* On PASS, perform a **squash merge**, then notify the Scrum Master.

#### **4.4 PO approval and commit record**

po\_approval:  
  decision: "APPROVED"  
  notes: ""

commit\_record:  
  pr\_id: ""  
  commit\_id: ""  
  closeout\_evidence\_pointer: "\<pointer to close pack / proof bundle in PR\>"

#### **4.5 PR template — evidence-only QA**

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

