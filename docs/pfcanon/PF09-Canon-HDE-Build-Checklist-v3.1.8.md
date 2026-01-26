# 0\) Front Matter

## 0.1 Header

**Title:** PF09-Canon-HDE-Build-Checklist

**Version:** v3.1.8

**Status:** Canon

**Effective date:** 2026-01-23

**Last Update Gate:** BN 9.4.4 Drain A30-31

**Invocation tag:** INV-f2ac55d77ce9aacc

## **0.1 Scope**

Build-only, dependency-ordered checklist of HD Engine components and concrete implementation tasks required to reach a stable production run. This list excludes documentation and process chores and focuses on shipping code, wiring transport, enforcing determinism, and proving behavior with runnable evidence. Checklist items are organized by seven alchemical phases (Calcination, Dissolution, Separation, Conjunction, Fermentation, Distillation, Coagulation), and each task/subtask is tagged with a tracking ID of the form `HDE-<PHASE><NNN>` or `HDE-<PHASE><NNN>.<m>` (for example, `HDE-CALC001`, `HDE-CALC001.1`). These IDs are for traceability only and do not imply priority or status.

This document MUST include “jobs to be done”, including:

* Development

* Design

* Implementation

* Operations

## **0.2 Conventions**

**Statuses** are canonical and use the following values only:

**Done** — Required behavior is implemented and evidenced for the slice this row covers.

**Partial** — Some but not all of the required behavior or evidence for this row is implemented; notes explain the gap.

**Not done** — Behavior is specified in canon, but implementation and/or evidence are still absent.

**Consolidation pending** — Behavior exists in multiple slices and must be consolidated under a single epic or harness before it is treated as Done.

**Optional** — Non-blocking work that may be implemented without gating releases.

 **Deferral (closure-safe; no new status enums).** If a task is intentionally not completed for the current epic and is being pushed to a future epic, keep the **Subtask status** within the existing allowed values (typically **Not done** or **Optional**) and record deferral explicitly in **Notes** using this minimal form:

* `DEFERRED → <future-epic-id or backlog stub> — <short reason>; not a close blocker for <current epic-id>.`

This makes the remaining work visible without creating a false “failed close gate” interpretation when the epic record explicitly allows deferral.

**Deferred-issue posture (acceptance artifacts; EPIC022 bridge).** When an epic explicitly closes with deferred QA issues, those issues MUST be recorded as deferred in the acceptance artifacts and MUST NOT be claimed as satisfied.

For token drift deferrals: do not maintain “known unregistered tokens” lists in epic records; treat the registry-validation output as the authoritative evidence of whether a token is claimable.

**Tracking IDs:**

Tasks use `HDE-<PHASE><NNN>` (for example, `HDE-CALC001`, `HDE-DISS003`).

Subtasks use `HDE-<PHASE><NNN>.<m>` (for example, `HDE-CALC001.1`).

IDs are stable labels only and do **not** imply priority or status.

**“SoT: canon” usage:**

**SoT: canon** may appear only in Notes. Use it to mark behavior that is locked by spec (PF01/PF02/PF04/PF05/PF09/PF12/PF14/PF19; fast deltas: PF10). PF20 is an epic tracking ledger only (not a spec source). PF20 MUST NOT be cited to define evidence surface paths, evidence shapes, remediation predicate targets, or validator expectations; plans/remediations MUST cite PF10/PF09/PF06/PF12/PF19/PF04 (as applicable) for those requirements.

**Sequencing pattern:**

When reasoning about work, prefer the following order: **determinism first → transport parity → evidence**.

PF09 expresses this sequencing via tasks and subtasks; the underlying math, transport contracts, and token semantics remain in PF canon.

**QA acceptance tokens and ownership:**

PF09 is a **consumer of token names only**. It does **not** define token semantics.

**Ops tasks (PO-only execution; evidence required):**

An Ops task is any work item that requires privileged access outside the repository and cannot be executed by automated agents (examples: service configuration, secrets/env var changes, deploy/runtime settings, infrastructure console actions, privileged database operations).

Ops tasks MUST be executed by the PO (human operator) only. Automated agents MUST NOT attempt to perform them, MUST NOT claim completion, and MUST NOT simulate external state changes.

When an Ops task is required by an epic or checklist row:

* It MUST be treated as PO-only execution, IA-guided (not PR work).

* It MUST specify success criteria and evidence to capture.

* Completion MUST produce a repo-stored evidence artifact under a lowercase audit path such as `audit/ops/<epic-id>/` (or `audit/qa/<epic-id>/` when captured during QA).

* Evidence MUST be secret-free. If a setting/value is sensitive, evidence must be presence-only, redacted, or hashed while still proving the intended state.

**/internal/version auth posture is not canonized (non-invention rule):**

PF canon defines the /internal/version transport and content contract, but does not canonize its auth posture (public vs operator-network gated vs auth-header required) or the expected failure mode when access is missing/invalid.

Until canonized:

* Do not state auth requirements for /internal/version as canon.

* Any statement about auth posture MUST be explicitly labeled as Observed Evidence (non-PF).  
* Runbooks MUST treat any auth header for `/internal/version` as **optional** (never required) unless and until auth is implemented and canonized. Any doc language that implies “auth required” must be treated as non-canonical unless/until the implementation exists.

Canonization requires OPS discovery evidence in the canonical deployment context(s):

* status line and headers with no auth header, and

* status line and headers with the expected auth header present (value redacted or presence-only noted),

stored under a lowercase audit path and kept secret-free per the Ops-task posture above.

**Single source of truth (names \+ semantics).**  
 Acceptance token names and semantics live only in the Token Registry in **HDE-Governance §2.0**. Any token name used in PF09, epics, acceptance artifacts, or QA evidence logs MUST exist in that registry and match spelling exactly (no aliases or near-matches). New tokens must be registered in Governance (via ADR \+ registry update) before they may appear as required tokens anywhere.

**QA operational token library (non-governance).**  
 The **Glow QA Guide** is the canonical home for QA operational token guidance (metadata, wiring, runbook mapping, evidence expectations). It MUST reference token names exactly as defined in the Governance Token Registry and MUST NOT introduce new token names or divergent meanings.

**Guard proofs (serializer/emitter guards) are evidence-only by default.**

Serializer/emitter guard proofs are required deliverables and must be mechanically produced, reviewable, and PASS/FAIL classified, but they do not create new acceptance token obligations by default. Plans MUST NOT introduce or claim new “guard tokens” unless the token exists in the canonical token registry owned by HDE Governance. If a guard proof artifact is promoted into closure wiring (referenced by acceptance maps, token↔evidence matrices, or close packs), it MUST follow governed evidence discipline (stable path, index/mirror updates when bytes change, and sibling path-proof transcripts when required).

**Epic acceptance rosters (in-flight; names-only, registry-validated).**  
 In-flight epics MUST define their acceptance token rosters in the Epic Plan Acceptance section and/or the epic’s acceptance artifacts (acceptance map and token↔evidence matrix). Token spellings MUST match the Governance token registry exactly (no aliases, near-matches, or local tokens). If a token is absent from the registry, it MUST NOT be claimed as satisfied (evidence collection may still proceed).

**HDE-Phased Epics is historical-only (no in-flight epics).**  
 HDE-Phased Epics MUST contain only completed epic records. In-flight epics MUST NOT be added, updated, or required as a planning gate. Treat it as an archive-on-close ledger.

**Live QA bridge rule (token validity vs evidence collection).**  
 For Live QA planning and evidence: token claim validity is gated by the Governance token registry. If the epic’s acceptance roster contains any unregistered token, classify it as `UNREGISTERED_ACCEPTANCE_TOKEN`: evidence may still be collected and bound, but step logs and acceptance artifacts MUST NOT claim the token as satisfied until registry/roster reconciliation. Do not substitute or rename tokens locally; record the gap as a doc-delta item and keep the validator output as the authoritative evidence of claimability.

**Plan posture note (excerpt-aligned):** Epic plans are **execution indexes**, not single-source re-statements of canon. Do **not** reproduce canon checklists or re-embed governed QA ledger artifacts inside plans. In particular, the per-epic **token↔evidence matrix** is a governed QA ledger artifact and should be referenced by location/title rather than duplicated in plan documents. “Required evidence” rules must be expressed as **canonical checks/workflows** (CI gates, scripts, harness outputs), not as plan-time documentation burdens.

**Close-pack artifacts (deterministic path-of-record; baseline artifacts, not tokens):**  
 The close-pack pair MUST live at the canonical audit paths using the `EPIC-###` pattern (3 digits):

* `audit/EPIC-###_close_report.md`

* `audit/EPIC-###_MANIFEST.json`  
* `key_outputs` MUST be a JSON object (named map) of `binding_key` → `repo_relative_path` (strings). `key_outputs` MUST NOT be a list.  
* Close-pack validation MUST validate **named bindings** (keys \+ exact paths), not list membership.  
* EPIC023 required bindings (normative; exact key/value pairs):  
  * `acceptance_map`: `docs/acceptance_map_epic023.json`  
  * `token_matrix`: `audit/qa/hde-epic023/token_evidence_matrix.md`  
  * `acceptance_map_viability`: `audit/qa/hde-epic023/acceptance_map_viability.log`  
  * `qa_step_manifest`: `audit/qa/hde-epic023/qa_step_logs_manifest.json`  
  * `doc_deltas`: `audit/docdeltas/hde-epic023_doc_deltas.md`  
  * `close_report`: `audit/EPIC-023_close_report.md`  
  * `close_manifest`: `audit/EPIC-023_MANIFEST.json`  
  * `EPIC023 close report required anchors/paths (normative; exact strings; close report text MUST contain):`  
    * `QA Rails — Open/Close (Final PR)`  
    * `docs/acceptance_map_epic023.json`  
    * `audit/qa/hde-epic023/token_evidence_matrix.md`  
    * `audit/qa/hde-epic023/acceptance_map_viability.log`  
    * `audit/qa/hde-epic023/qa_step_logs_manifest.json`

**EPIC024 doc-delta artifacts (Step-0B existence check; titles-only):**  
 Addenda 10-13 BN 9.4.4 (EPIC024 QA Step-0B) records both fixed-path doc-delta artifacts exist:

* `audit/docdeltas/hde-epic024_doc_deltas.md`

* `audit/qa/hde-epic024/00_meta/doc_deltas.md`

Addenda 19-25 BN 9.4.4 (CHECK po-011\_doc\_delta\_capture: PO-011) records the capture step is `STATUS: PASS` and writes its governed primary log at:

* `audit/qa/hde-epic024/checks/po-011_doc_delta_capture/primary.log`

**EPIC024 close-pack artifacts (D16 close pack; titles-only):**  
 Addenda 19-25 BN 9.4.4 (CHECK D16\_close\_pack: PO-009) records all four plan-required close-pack deliverables exist at fixed paths (and the D16 primary log header contains "status":"PASS"):

* `audit/EPIC-024_MANIFEST.json`

* `audit/EPIC-024_close_report.md`

* `audit/EPIC-024_QA_RCA.md`

* `audit/qa/hde-epic024/checks/D16_close_pack/primary.log`

The same addenda notes internal-consistency verification: manifest `key_outputs` references resolve (for example: `docs/acceptance_map_epic024.json`, `audit/qa/hde-epic024/token_evidence_matrix.md`, `audit/qa/hde-epic024/qa_step_logs_manifest.json`, `audit/docdeltas/hde-epic024_doc_deltas.md`).

These are baseline close-pack artifacts (required closure artifacts), not acceptance tokens by default. Do not relocate these artifacts into alternative directory trees (for example `audit/qa/**` or `artifacts/**`) without an explicit canon change. Epic plans SHOULD cite PF12 path patterns at the point the close-pack baseline is declared so the path-of-record is not discretionary.

**PF23 consult (mandatory for planning artifacts; planning-time trace only):**

When planning for QA, remediation, development, or any other execution work, agents MUST consult PF23 — Reality Audits as a primary input for component boundaries and canonical repo pathnames.

Plans MUST NOT mint, claim, or reference REALITY\_AUDIT\_OK (or any similar “PF23 consult completion” acceptance token) unless and until Governance explicitly registers such a token in the canonical token registry.

PF23 consult is planning-time only. Live QA Plans MUST NOT include any required deliverable, required check, or operator command whose purpose is “PF23 consult capture,” “PF23 note,” or similar.

If a trace anchor is desired, it lives in the plan text only (names-only). A plan MAY include a single “PF23 Anchors” note (components consulted \+ loci touched), but it is informational only and MUST NOT appear as a required evidence output.

PF23 is PO-maintained; plans MUST NOT create tasks that assign PF23 updates. If PF23 appears stale or missing coverage, note it as an observation only.

**Remediation task plans (approval gate scope):**  
 For remediation task plans (DEV PRs \+ OPS tasks), approval MUST focus on: (1) correct task model (DEV PRs only; OPS tasks only; explicit DISCOVERY vs CHANGE; no mixed tasks), (2) correct sequencing and explicit cross-lane dependencies, (3) concrete deliverables (lowercase paths \+ filenames), and (4) concrete verification success criteria. Detailed command lines and step-by-step failure handling are not required as a plan-approval condition; they MAY be developed in flight during execution, but evidence posture remains non-negotiable.

**Portability vs provenance (non-PF evidence references):**  
 Plans may include a short “Evidence inventory reviewed (non-PF)” list for provenance, but MUST NOT require the reader/executor to open external files to perform the work. If a plan depends on any non-PF fact, the plan MUST embed that fact directly in the document as a short quote or precise paraphrase inside an “Observed Evidence Snapshot” section. If an Artifact Map is included, it MUST label non-PF inputs as: **“provenance only; not required to execute”**.

**Index/Mirror exact filenames in plans (when touched):**  
 Any plan that includes tasks touching governed Evidence Index/Mirror files MUST treat sibling `.path_proof.txt` artifacts as first-class outputs and embedded verification checks inside the same task, using the exact filenames pinned in §0.3. If a plan proposes a new file under governed surfaces, it MUST state whether it is intended to appear in the indices/mirror; absence of that statement is a blocker

Ownership routing (titles-only; do not duplicate definitions here):

* Acceptance token registry (names \+ semantics; single SoT): **HDE-Governance**

* QA operational token library (wiring/runbook/evidence expectations): **Glow QA Guide**

* **Epic acceptance rosters** (in-flight; names-only, registry-validated): Canon Plan Templates \+ epic acceptance artifacts (acceptance map \+ token↔evidence matrix \+ close-pack)

* Evidence catalog record types \+ canonical filenames: **HDE-Schemas & Artifacts**

* Evidence index writer workflow \+ topology coupling: **HDE-Mechanics Guide** \+ **HDE-Build Checklist**

Checklist rows in PF09 refer to tokens by name (for example `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`) to indicate which acceptance gates they participate in; meaning and acceptance constraints are taken from the Governance Token Registry and the owning PF-docs for each token family, and operational execution guidance is taken from the Glow QA Guide, not from PF09 itself.

---

## **0.3 Evidence Index and mirror (paths pinned)**

### **0.3.1 Human Index (authoritative)**

**Human Index.** `docs/evidence/INDEX.json` — titles and paths only; no payload bytes. **Single home for the listing:** see **PF12 §8.6 “Evidence Index entries (titles/paths only)”**. PF09 does **not** duplicate that list.

**Human Index hash sentinel.** `docs/evidence/INDEX.sha256` — sha256 over the exact bytes of `INDEX.json`. Update in the same PR as the Human Index. **Gate:** `EVIDENCE_INDEX_HASH_OK`.

**Human Index path-proofs (governed; merge-blocking).**

`docs/evidence/INDEX.json.path_proof.txt` — path-proof transcript for the Human Index. MUST be refreshed whenever `docs/evidence/INDEX.json` bytes change (same PR). A stale proof is a merge-blocking evidence integrity failure.

`docs/evidence/INDEX.sha256.path_proof.txt` — path-proof transcript for the hash sentinel. MUST be refreshed whenever `docs/evidence/INDEX.sha256` bytes change (same PR). A stale proof is a merge-blocking evidence integrity failure.

The canonical updater (`tools/evidence/update_evidence_index.py`) is responsible for refreshing these path-proofs during normal write runs, and `tools/evidence/update_evidence_index.py --check` MUST fail if either proof is stale.

### **0.3.2 Machine Mirror (records-only)**

**Machine mirror canonical home (governed; merge-blocking).**

`artifacts/evidence_index.jsonl` — Machine Evidence Index mirror (records-only JSONL). Governed companion: `artifacts/evidence_index.jsonl.sha256`.

**Machine mirror path-proofs (governed; merge-blocking).**

`artifacts/evidence_index.jsonl.path_proof.txt` — path-proof transcript for the Machine Mirror.

`artifacts/evidence_index.jsonl.sha256.path_proof.txt` — path-proof transcript for the mirror sha256 companion.

Path-proofs MUST be refreshed whenever the corresponding artifact bytes change (same PR). A stale proof is a merge-blocking evidence integrity failure. The canonical updater (`tools/evidence/update_evidence_index.py`) is responsible for refreshing these proofs during normal write runs, and `tools/evidence/update_evidence_index.py --check` MUST fail if any mirror path-proof is stale.

**Non-canonical mirror paths are invalid.** Any path like `docs/evidence/INDEX.machine_mirror.jsonl` is not a canonical mirror artifact. There MUST be exactly one machine mirror file at `artifacts/evidence_index.jsonl` (and its governed companion `artifacts/evidence_index.jsonl.sha256`). If any tool, test, or CI output references an alternate mirror path, treat it as a tooling/config bug and fix it before merge.

### **0.3.3 Mirror discipline (normative)**

The machine mirror is **one and only one** file at `artifacts/evidence_index.jsonl`.

Mirror content is **records-only canonical JSONL**:

UTF-8 (no BOM).

ASCII-sorted keys.

Compact separators.

Exactly one LF per record.

Unknown keys **rejected**.

**Sort-before-write** by `(artifact_key, discovered_physical_path)`.

**Exact field order** (per PF12/PF10):

`artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

### **0.3.4 Minimum mirror record fields (reject unknown keys)**

Each record in the machine mirror uses at least the following fields; unknown keys are rejected:

{

  "artifact\_key": "",

  "role": "\<proof|golden|snapshot|script|log\>",

  "sha256": "\<lowercase 64-hex\>",

  "size\_bytes": 0,

  "produced\_at\_utc": "",

  "discovered\_physical\_path": "",

  "proof\_anchor": ""

}

### **0.3.5 Field order and write discipline (merge-blocking)**

**ASCII field order (exact):**

 `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

**Sort-before-write** by the tuple `(artifact_key, discovered_physical_path)`.

**Single mirror file:** exactly one `artifacts/evidence_index.jsonl` in the repo.

**Uniqueness:** the pair `(artifact_key, discovered_physical_path)` is unique; duplicates fail CI.

**CI gate:** fail the PR on:

Missing human↔machine parity.

Non-canonical JSONL.

Unknown keys.

Missing path-proofs.

Wrong field order.

Unsorted records.

### **0.3.6 Parity and path-proofs**

**Same-PR parity.** Human Index ↔ Machine Mirror MUST be **1:1** in the **same PR** or commit that adds, moves, or renames artifacts.

**Path-proofs.** Store a `path_proof.txt` alongside each governed artifact and reference it via `proof_anchor`. The `proof_anchor` MUST exactly match the stored path-proof for that artifact.

**Governed locations only.** Index artifacts only from governed paths (`artifacts/**`, `audit/**`, `docs/evidence/**`). Transient generator paths (for example `codex/out/**`) are not authoritative and **MUST NOT** be indexed — relocate proofs under `artifacts/**` before gating.

### **0.3.7 Registry report (names-only)**

`artifacts/registry/registry_report.json` — canonical JSON; kept in sync and mirrored.

### **0.3.8 Governed record types**

**Single home:** **PF12 Appendix C “Governed artifact record types.”** PF09 does not define or duplicate governed record type schemas.

### **0.3.9 Locale pins for all byte checks**

All mirror/index checks and governed byte comparisons run with:

`LC_ALL=C`

`LANG=C`

`TZ=UTC`

### **0.3.10 Evidence bundles and manifests (ledger-centric evidence)**

For some high-churn evidence families, the HD Engine now uses a **bundle-centric evidence model** instead of writing and indexing every member artifact as its own file:

* An **evidence bundle** is a **textual file** (typically JSON or JSONL) under `artifacts/**` or `docs/evidence/**` that groups related evidence records (for example, ordering artifacts, sampler runs, or config dumps) into a single governed artifact.

* Each bundle has a companion **bundle manifest** (JSON/JSONL) that lists, for each logical member, at minimum: `artifact_key`, `sha256`, `size_bytes`, and any additional descriptors defined in HDE-Schemas & Artifacts by title.

For these families:

* The **governed artifacts** are the **bundle file and its manifest**, not each internal member file.

* The Human Evidence Index (`docs/evidence/INDEX.json`) and Machine Mirror (`artifacts/evidence_index.jsonl`) track **bundles and manifests** under the existing discipline:

  * Each bundle or manifest appears as a **single row** in the Mirror (one row per governed artifact or bundle, as defined in HDE-Schemas & Artifacts).

  * Each bundle or manifest has a co-located path-proof transcript referenced by `proof_anchor`, exactly as for discrete artifacts.

Bundle invariants:

* Bundles and manifests are **text-based and agent-readable** (UTF-8; canonical JSON/JSONL where applicable; LF-terminated); they live only under governed paths (`artifacts/**`, `audit/**`, `docs/evidence/**`).

* Bundle manifests must be valid JSON/JSONL, obey the Mirror schema (no unknown keys), and use deterministic ordering as defined in HDE-Schemas & Artifacts and HDE-Mechanics Guide (titles-only).

Impact on this checklist:

* All generic Index/Mirror rules in §0.3 and §0.5 apply equally to **discrete artifacts and bundle artifacts**.

* Checklist rows that consume tokens such as `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, and `EVIDENCE_PATHS_VALIDATED_OK` now implicitly cover **“governed artifact or bundle”** (as defined in HDE-Schemas & Artifacts), not only individual files.

PF09 still treats Evidence Index and Machine Mirror as **consumer-only** surfaces: schema, bundle-vs-member policy, and detailed token semantics remain single-homed in HDE-Schemas & Artifacts and HDE-Governance by title.

## **0.4 A7 proof surface (titles-only pointers)**

### **0.4.1 Single home (location & scope)**

**Catalog file.** `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256`.

**Scope.** The Endpoints Catalog is the canonical, machine-readable inventory of **HTTP endpoints** that are reachable in any environment, including, at minimum:

* `public_reader` (e.g. `/reader`)

* `internal_admin` (internal/admin compat and admin-only surfaces, e.g. `/api/compat/v1`)

* `internal_identity` (e.g. `/internal/version`)

* `ops` (e.g. `/ops/health` or equivalent probes)

* `dev_harness` (e.g. `/internal/dev/sampler`)

**Classification is mandatory.** Implementations may colocate multiple endpoint classes in one Python module, but the Catalog MUST still carry **per-endpoint** classification so CI and QA can enforce distinct rails and posture per class.

**Catalog entry minimum fields (titles-only; schema owned elsewhere).**  
 Each entry in `docs/ENDPOINTS_CATALOG.json` MUST include, at minimum:

* `path` — for example `/reader`, `/api/compat/v1`, `/internal/version`, `/ops/health`, `/internal/dev/sampler`

* `method` — `GET`, `POST`, `HEAD` (or a list if the endpoint supports multiple methods)

* `classification ∈ {public_reader, internal_admin, internal_identity, ops, dev_harness}`

* `blueprint_module` — titles-only pointer to owning module (for example `adapter/http_reader.py`, `engine/http/compat_handler.py`)

* `rails_profile` — short, names-only summary of rails and gating expectations (for example “requires APP\_ENV=dev”, “ops-only”, “A7 success posture”, “writer no-store posture”)

* `a7_eligible` — boolean (true only for JSON success routes eligible for A7 proofs)

* `env_gate` — for entries where reachability is env-gated (titles-only; exact gating semantics routed to Governance/Infrastructure)

**A7-eligible subset (explicit flag).**  
 A7 proofs apply only to endpoints explicitly marked as **A7-eligible JSON success routes** in this Catalog:

* A7 proofs run **only** on entries where `a7_eligible == true`.

* `/internal/*` endpoints are never A7-eligible; `/internal/version` MUST have `a7_eligible == false` (policy owned by Governance; referenced here by title only). Access-control semantics for `/internal/version` are not yet canonized; see Conventions.

**Proof surface.** A7 proofs run **only** on an A7-eligible route listed in the Catalog.

### **0.4.2 Env-gating proof (headers-only)**

`artifacts/proofs/endpoints_env_gate_proof.log` shows that non-prod and dev-harness entries are unreachable in prod (or otherwise blocked by the declared env gate for each entry).

Index in Human \+ Machine evidence in the same PR.

### **0.4.3 A7 invariants to prove (headers-only)**

For the Catalog JSON success route under test:

**200\.**

Strong **quoted** `ETag`.

`Vary: Authorization, Accept-Encoding`.

Policy-compliant success cache headers.

**HEAD.**

Status 200; no body.

Validators mirror 200\.

`Content-Type == GET`.

`Content-Length == len(identity 200 body)`.

**304\.**

Only after a prior 200 for the same resource.

**Omit** `Content-Type`.

**Omit** `Content-Length`.

Validators mirror the cached 200\.

**Encoding invariance.**

For the same canonical LF-terminated body, ETag identity and effective `Content-Length` are stable across accepted encodings (identity/gzip/br).

**Writers/errors posture.**

Writers and error routes carry `Cache-Control: no-store`.

### **0.4.4 Artifacts (headers-only; one LF each)**

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_encoding_invariance.txt`

`artifacts/proofs/success_writers_errors.txt`

Capture on an A7-eligible Catalog route; index Human+Machine in the same PR. The machine mirror remains records-only canonical JSONL (unknown-key rejection; each record has a `proof_anchor`).

### **0.4.5 Transport guidance — A7 rows & Catalog tie-in**

A7 rows apply **only** to endpoints declared in `docs/ENDPOINTS_CATALOG.json` that have `a7_eligible == true`.

`/internal/*` routes (including `/internal/version`) may appear in the Endpoints Catalog for inventory and audit, but they are never A7-eligible and are verified under ops posture: `Cache-Control: no-store`, no `ETag`, HEAD 200 parity, conditionals ignored.

When capturing A7 proofs:

Always cite the Catalog entry used (path, method, classification, `a7_eligible`, `blueprint_module`).

Include the env-gate proof in the same PR.

Ensure all artifacts are indexed and mirrored under the Evidence Index discipline above.

### **0.4.6 A7/Catalog acceptance (titles-only)**

A7/Catalog gating uses the following Governance tokens (names-only):

`ENDPOINTS_CATALOG_OK`

`ENDPOINTS_CATALOG_ENV_GATE_OK`

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_ENCODING_INVARIANCE_OK`

---

## **0.5 Index & mirror discipline**

Update the Human Evidence Index (`docs/evidence/INDEX.json`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) in the **same PR** whenever governed evidence changes. Governed evidence includes:

* **Discrete artifacts** (for example individual JSON/LOG files under `artifacts/**`, `audit/**`, `docs/evidence/**`), and

* **Evidence bundles and their manifests** as defined in HDE-Schemas & Artifacts (see §0.3.10 for bundle semantics).

Mirror rules (for all governed artifacts and bundles):

* Records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF).

* Unknown keys rejected.

* Each record includes at least:

  * `artifact_key`,

  * `discovered_physical_path`,

  * `produced_at_utc`,

  * `proof_anchor`,

  * `role`,

  * `sha256`,

  * `size_bytes`.

* The tuple `(artifact_key, discovered_physical_path)` is unique across the mirror.

* There is exactly one Machine Mirror file at `artifacts/evidence_index.jsonl`.

* `proof_anchor` always points to a co-located path-proof transcript for the governed object:

  * For **discrete artifacts**, the path-proof describes that specific file.

  * For **bundles**, the path-proof describes the bundle file; the bundle manifest is the canonical mapping from logical member IDs to hashes/sizes.

Locale pins apply to all byte checks and evidence tools that read or write these files:

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`

**Pre-approval evidence binding checks (pass/fail, checklist-level)**

These checks are required whenever an epic plan and/or token matrix claims acceptance tokens that bind to governed evidence.

**Filesystem naming (directories).**  
 All directories in the repository and application codebase MUST use lowercase ASCII names. Under governed roots (at minimum `audit/**`, `docs/**`, `artifacts/**`, and `schemas/**`), introducing any mixed-case or upper-case directory name is a QA failure. Any remaining mixed-case directories are treated as legacy drift and MUST be normalized to lowercase, not copied forward. If a rename affects governed evidence paths, update the Human Evidence Index, Machine Mirror, and path-proofs in the same PR.

**Canonical evidence path binding validation (acceptance integrity).**  
 Every acceptance token to evidence-path binding that appears in an Epic Plan and in `token_evidence_matrix` MUST be validated against the canonical evidence catalog before approval or merge.

* If the evidence catalog defines a fixed canonical path for a token’s evidence surface, the Epic Plan required-evidence list and the token matrix MUST bind to that exact path.

* For deliverables that claim a local bundle directory of governed artifacts, the required-evidence list MUST still explicitly name any shared or global governed artifacts required for acceptance that live outside the local bundle root (with canonical paths).

* When a token is claimed, the following MUST agree on the canonical path and identity of the bound artifact:

  * Epic Plan required-evidence list (per deliverable)

  * `token_evidence_matrix` row for the token

  * `docs/evidence/INDEX.json` entry for the bound artifact

  * `artifacts/evidence_index.jsonl` mirror record (`artifact_key` and `discovered_physical_path`)

  * the referenced path-proof file (`proof_anchor` and the corresponding `*.path_proof.txt`)

* Any binding to a non-canonical path is a mechanical blocker and MUST be corrected before approval. If a non-canonical path is truly required, it MUST be routed as an explicit ADR and drained into the governing canon before approval.

**Identity checksum sidecars (helper artifacts, unless explicitly required).**

For identity artifacts under `audit/qa/<epic-id>/artifacts/identity/`, `.sha256` sidecars for JSON files are optional helper artifacts unless the epic acceptance section explicitly lists them as required. If produced, checksum sidecars MUST be generated mechanically (e.g., `sha256sum`) and may be indexed as helper artifacts, but MUST NOT be treated as gating by default.

**Index/mirror acceptance (titles-only; tokens live in HDE-Governance / HDE-Schemas & Artifacts):**

These tokens now apply to **both** discrete artifacts and bundle-based families (bundles \+ manifests) and gate that Index, Mirror, and path-proofs are in sync for all governed evidence:

* `EVIDENCE_INDEX_UPDATED_OK` — Human Index updated for all governed artifacts **and bundles** affected in this PR.

* `EVIDENCE_INDEX_MIRROR_OK` — Machine Mirror rows present and consistent (one row per governed artifact or bundle).

* `EVIDENCE_INDEX_HASH_OK` — `docs/evidence/INDEX.sha256` matches the canonical bytes of `INDEX.json`.

* `EVIDENCE_PATHS_VALIDATED_OK` — every `discovered_physical_path` in the Mirror points to a real governed artifact or bundle.

* `EVIDENCE_PATH_PROOFS_OK` — each Mirror row has a valid `proof_anchor` to a co-located path-proof transcript for that artifact or bundle.

* `CI_CHECK_MIRROR_SCHEMA_OK` — CI schema checks enforce the Mirror’s field set, ordering, and unknown-key rejection, including bundle-specific fields defined in HDE-Schemas & Artifacts.

* `CI_CHECK_FINAL_LF_OK` — governed JSON/JSONL artifacts (including bundles/manifests) are LF-terminated and free of extra trailing bytes.

PF09 remains a **consumer** of these tokens and artifact definitions: token semantics, Mirror schema (including any bundle-specific fields), and the precise list of governed bundles and families are single-homed in HDE-Governance and HDE-Schemas & Artifacts by title.

---

# Phase I — Calcination (Foundations first) 

**Phase description:** Foundational mechanics for the HD Engine: freeze and validate core catalogs, stand up canonical serialization and total-order infrastructure, and wire repository/tooling skeleton plus the programmatic configuration system.

**Phase master status:** **Partial** 

**Notes:**

PF09 is consumer-only; math, schemas, governance tokens, and HTTP contracts live in PF01/PF12/PF04/PF05/PF14.

This phase focuses on determinism primitives (catalogs, serialization, comparators) and repository evidence infrastructure that later phases build on.

---

## Task HDE-CALC001 — Canonical Enumerations Registry

**Task name/label:** Canonical Enumerations Registry

**Task status:** **Done**

**Task ID:** HDE-CALC001

**Task description:**  
 Freeze and validate the enumerations registry (centers, gates, channels, categories) against PF12 catalogs and schemas, enforce canonical forms and set semantics, prove closure/uniqueness, and emit registry evidence artifacts indexed in the Evidence Index/Mirror system.

**Task notes:**

Enumerations are frozen in canon (HDE-Math-Spec; HDE-Schemas & Artifacts; titles-only).

The Registry structure and generation scripts are in place; this component is considered Done for Calcination.

### Subtask HDE-CALC001.1 — Registry validation job

**Subtask name/label:** Registry validation job

**Subtask description:**  
 Provide a single registry job that loads centers, gates, channels, and categories from PF12 catalogs and validates each domain against its JSON Schema, hard-failing on unknown IDs, duplicates, non-canonical channel forms, or schema mismatches.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (validation behavior; semantic tokens live in Governance/Schemas)

**Evidence / artifacts:**

Covered by registry evidence families listed below (domain\_snapshot, closure\_report, registry\_checksums).

**Notes:**  
 PF09 does not restate schemas; it requires the job to exist and enforce failure on invalid domain entries.

### Subtask HDE-CALC001.2 — Channel normalization & set semantics

**Subtask name/label:** Channel normalization & set semantics

**Subtask description:**  
 Normalize channels to canonical `NN–NN` (zero-padded, min-first) form and enforce ASCII sort \+ dedupe for any arrays that represent sets before hashing/compare.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (relates to canonicalization/ordering tokens tracked elsewhere)

**Evidence / artifacts:**

Reflected in `closure_report` and ordering evidence families.

**Notes:**  
 PF09 does not restate invariants; it requires that normalization and set semantics be enforced by this job.

### Subtask HDE-CALC001.3 — Closure & uniqueness

**Subtask name/label:** Domain closure & uniqueness

**Subtask description:**  
 Registry validation must prove closure and uniqueness across all domains (no extras or omissions, no duplicate IDs, no cross-catalog drift). Any drift must fail CI.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (closure-related tokens tracked in Governance)

**Evidence / artifacts:**

`closure_report` — proofs of domain closure & uniqueness; channel-normalization rejects.

**Notes:**  
 CI is expected to fail closed on any mismatch in domain closure or uniqueness.

### Subtask HDE-CALC001.4 — Registry evidence artifacts

**Subtask name/label:** Registry evidence artifacts

**Subtask description:**  
 Emit a records-only registry snapshot and supporting reports (closure and checksums) that capture domain counts and canonical sha256/size\_bytes for governed artifacts, and ensure they are indexed under the Evidence Index discipline (Human Index \+ Machine Mirror in the same PR, with path-proofs).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_INDEX_HASH_OK` (implied by Index updates)

**Evidence / artifacts:**

`engine.config.registry_loader` — typed loader implementation for PF12 catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations).

`tests/config/` loader tests (titles-only), including unknown-ID and duplicate-ID cases and alias-policy OFF/ON enforcement.

**Notes:**  
 PF09 does not restate loader schemas or typed error classes; those remain single-homed in PF12 and PF14. This subtask requires that the canonical loader and its tests exist and enforce the fail-closed behavior described above.

 Artifact paths and schemas live in HDE-Schemas & Artifacts; PF09 requires their presence and correct indexing.

### Subtask HDE-CALC001.5 — Determinism pins

**Subtask name/label:** Determinism pins for registry job

**Subtask description:**  
 Run registry validation and snapshot generation under determinism pins using canonical JSON: `LC_ALL=C`, `LANG=C`, `TZ=UTC`; UTF-8 (no BOM); sorted keys; compact; exactly one trailing LF.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK` (shared canonical JSON check family)

**Evidence / artifacts:**

Canonical JSON checks on registry artifacts (via shared canonical JSON evidence).

**Notes:**  
 Ensures registry artifacts are stable and canonical across runs.

### Subtask HDE-CALC001.6 — Indexing & mirror discipline (registry)

**Subtask name/label:** Registry Indexing & mirror discipline

**Subtask description:**  
 Index registry evidence in `docs/evidence/INDEX.json` and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; each record includes a `proof_anchor` to a co-located path-proof).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_INDEX_HASH_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

`*.path_proof.txt` for registry artifacts

**Notes:**  
 PF09 defers mirror schema details to PF12; this subtask enforces usage, not schema definition.

---

## **Task HDE-CALC002 — Canonical Serialization Package**

**Task name/label:** Canonical Serialization Package

**Task status:** **Partial**

**Task ID:** HDE-CALC002

**Task description:**  
 Provide a single canonical serializer/emitter for all public JSON bytes (Reader, CLI, evidence), enforce canonical JSON rules and arrays-as-sets semantics, and prove determinism (AB↔BA, two-run identity) with harness evidence; keep CLI/Reader parity under closed rails.

**Task notes:**

EPIC017 established the canonical JSON serializer and the first closed-rails determinism/parity harness for `hdctl showcompat` (AB↔BA parity, two-run identity, Reader↔CLI parity, preimage recompute), plus canonical guard artifacts for serializer/emitter discipline.

EPIC021 (D1; Addendum 6\) completes the Calcination-owned serializer consolidation across the EPIC021 surface set by extending and proving the same canonical emission and guard discipline for:

* `bg:resolve` canonical JSON output and canonical error envelopes under pinned env rails.

* Aux narratives CLI/Reader parity checks under pinned env rails (aux remains text on the public surface; parity is asserted across CLI and Reader).

* Serializer guards that now cover Reader adapter code as well as CLI, preventing ad-hoc JSON serializers on governed surfaces.

EPIC021 acceptance artifacts (token↔evidence matrix and acceptance map) now mark the D1 canonical JSON/parity token family as implemented with explicit test and evidence wiring for: `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`, `JSON_CANONICAL_CHECK_OK`, and `ERROR_JSON_CANON_OK`. Serializer/emitter guard proofs are still required, but per current posture they are treated as reviewable evidence artifacts (and governed evidence when promoted), not as automatically tokenized acceptance, unless and until Governance registers explicit guard tokens and semantics.

This row is considered Done at the Calcination foundation level: canonical serializer, shared emitter discipline, and D1 canonical JSON/error proofs are present and exercised under closed rails for the EPIC021 surface set. Later-phase transport proofs (A7 success route proofs, prod transport parity, and non-Calcination identity work) remain governed elsewhere in this checklist.

### **Subtask HDE-CALC002.1 — Shared presenter/emitter**

**Subtask name/label:** Single presenter/emitter for Reader & CLI

**Subtask description:**  
 Ensure a single presenter/emitter entrypoint symbol is shared between Reader and CLI for public JSON emission.

**Subtask status: Done**

**Epic or card:** EPIC-017 (D1)

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`

`CLI_NO_ALT_JSON_OK`

**Evidence / artifacts:**

`artifacts/cli/guards/emitter_symbol_proof.txt`

`artifacts/cli/guards/serializer_grep_guard.log`

`tests/cli/test_cli_canonical_bytes.py`

`tests/cli/test_showcompat_parity_and_identity.py`

**Notes:**  
 Codex Audit HDE-EPIC024 reports the shared emitter path is implemented (`engine/presenter/emitter.py` uses `emitter.emit_public`), with canonical-bytes/parity tests enforcing the single-emitter rule on governed CLI/Reader surfaces.

### **Subtask HDE-CALC002.2 — Canonical JSON rules**

**Subtask name/label:** Canonical JSON rules for public bytes

**Subtask description:**  
 Enforce canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, consistent float serialization, no extra whitespace, and exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted.

**Subtask status: Consolidation pending**

**Epic or card:** EPIC-017 (D1)

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Acceptance gates:**

* Canonical JSON check applies to:

  * canonical surfaces (registries, cache snapshots, evidence indexes, etc.)

  * transport payloads (if JSON is used as a payload form)

  * any persisted “public bytes” that are used as stable acceptance evidence

* Must verify canonicalization invariants and log violations (no silent coercion).

**Evidence / artifacts:**

`audit/gates/canonical_json/json_canonical_check.log`

`audit/gates/canonical_json/json_canon_compare.log`

**Notes:**  
 Harness and checks exist, but canonicalization must be proven across all surfaces before tokens are considered green.

Canonical JSON binding rule (split families): canonical JSON check artifacts MUST bind only under `audit/gates/canonical_json/` for acceptance maps, token↔evidence matrices, close packs, and Evidence Index/Mirror entries. Canonical JSON gate artifacts MUST bind under `audit/gates/json_gate/canonical/` (the `audit/gates/canonical_json/canonical_json.gate.json` family is non-authoritative legacy naming and MUST NOT be required unless canon explicitly reinstates it). `audit/gates/canonical/` is legacy/compat-only and MUST NOT be used as a canonical acceptance surface or indexed/mirrored as the canonical gate family.

Canonical compare posture: canonical JSON compare evidence MUST reuse canon-defined compare surfaces (for example `audit/gates/canonical_json/json_canon_compare.log`). Epics MUST NOT introduce epic-local compare proof paths as “the canonical compare proof” unless that new surface is explicitly introduced via Build Notes and drained into the owning canon homes.

### **Subtask HDE-CALC002.3 — Arrays-as-sets semantics**

**Subtask name/label:** Arrays-as-sets discipline

**Subtask description:**  
 Deduplicate and ASCII-sort arrays that function as sets before hashing or comparison.

**Subtask status: Consolidation pending**

**Epic or card:** EPIC-017 (D1)

**Tokens:** **Unknown** (implicit in canonicalization and tie-break module tokens)

**Evidence / artifacts:**

Shared canonical JSON compare logs (as above).

Arrays-as-sets governed proof surfaces (titles-only):

* `artifacts/canonical/arrays_as_sets_report.log`

* `tools/evidence/generate_arrays_as_sets_report.py`

* `tests/compare/test_arrays_as_sets.py`

QA closure logs (titles-only):

* `audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log`

**Notes:**  
 Addenda 6-9 BN 9.4.4 (PR02 HDE-EPIC024 Review) records a governed arrays-as-sets report exists under `artifacts/canonical/arrays_as_sets_report.log`, regenerated via `tools/evidence/generate_arrays_as_sets_report.py` under closed rails and covered by `tests/compare/test_arrays_as_sets.py`. Behavior remains tied to comparator and canonicalization work in other tasks.

Addenda 10-13 BN 9.4.4 (EPIC024 QA D05) records a PASS primary log header with `exit_code:0` for `audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log` and shows the executed command as `python -m pytest tests/compare/test_arrays_as_sets.py`. The Approved Plan’s named runner `python tools/evidence/run_arrays_as_sets_check.py` and planned report path `audit/gates/arrays_as_sets/arrays_as_sets_report.md` are reported missing/not used; do not bind to those surfaces as governed proof.

### **Subtask HDE-CALC002.4 — Determinism environment pins**

**Subtask name/label:** determinism environment pins

**Subtask description:**  
 Run all canonical dumps/compares under pinned determinism environment variables (LC\_ALL/LANG/TZ) and record proof in log artifacts.

**Subtask status: Done**

**Epic or card:** EPIC-018 (D1)

**Tokens:**  
 `DETERMINISM_ENV_PINS_OK`  
 `DETERMINISM_ENV_LC_ALL_C_OK`

**Evidence / artifacts:**  
 `audit/gates/determinism/env_pins.log`  
 `audit/gates/determinism/env_pins.log.path_proof.txt`  
 `ci/checks/check_env_pins.sh`  
 `tools/evidence/run_env_pins_gate.py`  
 `audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log`  
 `audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log.path_proof.txt`  
 Harness and CI configuration for determinism pins (PF10 Addenda; logs referenced above).

**Notes:**  
 Codex Audit HDE-EPIC024 confirms env pins enforcement and the governed env pins log at `audit/gates/determinism/env_pins.log`. Addenda 19-25 BN 9.4.4 records CHECK D01\_env\_pins\_gate: PO-012 as `STATUS: PASS` and notes the step created `tools/evidence/run_env_pins_gate.py` to match the plan specification.

### **Subtask HDE-CALC002.5 — Determinism and parity harness (hdctl showcompat)**

Subtask name/label: determinism and parity harness

Subtask description:  
 Run hdctl showcompat parity and identity checks under closed rails and ensure `identity_all:true` and `parity:true` is reported under controlled inputs.

Subtask status: Done

Epic provenance: EPIC-018 (D2)

Tokens:  
 `DETERMINISM_PARITY_OK`  
 `COMPOSITE_ABBA_IDENTITY_OK`

Evidence / artifacts:  
 audit/qa/hde-epic018/d2-compat/hdctl\_showcompat\_parity.json — governed compatibility check output  
 audit/qa/hde-epic018/d2-compat/hdctl\_showcompat\_parity.proof.txt — file hash and deterministic proof for parity output  
 audit/qa/hde-epic018/d2-compat/hdctl\_showcompat\_identity.json — governed identity check output  
 audit/qa/hde-epic018/d2-compat/hdctl\_showcompat\_identity.proof.txt — file hash and deterministic proof for identity output  
 reports/compat\_check.json — merged compatibility report

Scripts / entrypoints:  
 scripts/hdctl.py showcompat — primary CLI used in harness mode.  
 ci/checks/check\_cli\_determinism.sh — CI wrapper to enforce SAFE\_MODE=1, ALLOW\_NETWORK=0, TZ=UTC, LANG=C, LC\_ALL=C.

Tests:  
 tests/cli/test\_showcompat\_parity\_and\_identity.py — asserts parity/identity output contracts.  
 tests/cli/test\_showcompat\_sources.py — asserts showcompat sources and data ID stability.

CLI determinism and parity artifacts:  
 artifacts/cli/showcompat\_parity.json — parity JSON captured at build time (non-governed mirror of audit output).  
 artifacts/cli/showcompat\_identity.json — identity JSON captured at build time (non-governed mirror of audit output).  
 artifacts/cli/cli\_determinism\_pass.txt — CLI determinism check marker.  
 artifacts/cli/preimage\_recompute.log — preimage recompute log for Reader envelopes (computed\_sha256, stored\_sha256, match:true).

EPIC024 showcompat artifacts (fixed paths; D03 showcompat artifacts gate / PO-013):

artifacts/showcompat/epic024/showcompat\_manifest.json — governed showcompat manifest (fixed path).  
 artifacts/showcompat/epic024/showcompat\_manifest.json.path\_proof.txt — path-proof for showcompat manifest.  
 artifacts/showcompat/epic024/showcompat\_symbols.json — governed showcompat symbols (fixed path).  
 artifacts/showcompat/epic024/showcompat\_symbols.json.path\_proof.txt — path-proof for showcompat symbols.  
 audit/qa/hde-epic024/checks/D03\_showcompat\_artifacts/primary.log — governed check primary log (header contains "status":"PASS").  
 audit/qa/hde-epic024/checks/D03\_showcompat\_artifacts/primary.log.path\_proof.txt — path-proof for D03 primary log.  
 tools/evidence/run\_showcompat\_artifacts.py — runner created in-step to match plan spec; wraps scripts/hdctl.py showcompat and writes artifacts above.

Serializer guard artifacts (shared with HDE-CALC002.6):  
 audit/qa/hde-epic018/d3-serializer/serializer\_grep\_guard.log — serializer grep guard output.  
 audit/qa/hde-epic018/d3-serializer/serializer\_grep\_guard.proof.txt — file hash and deterministic proof for serializer guard.  
 audit/qa/hde-epic018/d3-serializer/serializer\_env\_lcall\_c.txt — environment pin proof for serializer guard.  
 audit/qa/hde-epic018/d3-serializer/serializer\_env\_lcall\_c.proof.txt — proof of LC\_ALL=C, LANG=C.

Notes:  
 Determinism checks require SAFE\_MODE=1 and ALLOW\_NETWORK=0; harness must set and log env pins. Use pfrails wrappers when calling scripts/hdctl.py.  
 This subtask is the required parity proof for showcompat outputs and must be passed before any acceptance map tokens are considered valid.

### **Subtask HDE-CALC002.6 — Canonical guard artifacts for CLI serializer/emitter**

Subtask name/label: Canonical guard artifacts for CLI serializer/emitter

Subtask description:  
 Treat the CLI serializer/emitter guard logs under `artifacts/cli/guards/**` as the canonical guard artifacts for CLI serializer coupling and ensure they are produced and verified via the canonical guard tools:

Canonical guard artifacts (homes):

`artifacts/cli/guards/serializer_grep_guard.log` — AST-based grep-guard report confirming there are no disallowed JSON serializers (for example `json.dumps`/`json.dump`) on governed CLI paths.

`artifacts/cli/guards/emitter_symbol_proof.txt` — AST-based emitter symbol proof documenting which canonical emitter symbols are used by governed CLI handlers (for example `showcompat`, `bg:resolve`, and `aux-preview`), including explicit `<none>` listing for optional emitters such as `aux-preview`.

Guard tools (titles-only):

`tools/cli/serializer_grep_guard.py` — runs under determinism env rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`) and scans the governed CLI scope (default `engine/cli/**`, plus optional extra paths) for disallowed JSON serialization; emits a stable PASS/FAIL log at `artifacts/cli/guards/serializer_grep_guard.log` with no timestamps or env-dependent content.

`tools/cli/emitter_symbol_proof.py` — runs under the same determinism env rails and analyzes the CLI module to prove that governed handlers route through allow-listed emitter symbols; emits a stable proof at `artifacts/cli/guards/emitter_symbol_proof.txt` listing handler→emitter mappings and a summary PASS/FAIL line.

CI integration (titles-only):

CI MUST invoke the guard tools under closed determinism rails (after `ci/checks/check_env_pins.sh`), failing the job if either guard reports violations.

CI MUST run `pytest tests/cli/test_serializer_guards.py`, which exercises both tools in clean and synthetic violation scenarios and asserts correct PASS/FAIL behavior and log contents.

Index/Mirror discipline (shared with the Evidence Index canon):

Evidence Index and Machine Mirror records for CLI serializer coupling MUST use `artifacts/cli/guards/serializer_grep_guard.log` and `artifacts/cli/guards/emitter_symbol_proof.txt` as their `discovered_physical_path` values.

Each guard artifact has a co-located `*.path_proof.txt` transcript that records at least the governed fields (path, size\_bytes, sha256, timestamps) and is referenced via the mirror record’s `proof_anchor`.

Mirror records for the guard artifacts obey the global mirror discipline (records-only canonical JSONL; UTF-8, sorted keys, compact, exactly one LF; unknown-key reject; fixed field order), as enforced by `ci/checks/check_mirror_schema.sh` and the evidence skeleton tests.

Implementations MAY also write copies of the guard logs under `audit/gates/guards/**` for internal audit workflows, but those locations are secondary and not required for mechanics-level acceptance in PF09.

Subtask status: Done

Epic or card: EPIC-017 (D1); EPIC-018 (D3 CLI serializer guards)

Tokens:

EVIDENCE\_PATHS\_VALIDATED\_OK  
 EVIDENCE\_INDEX\_UPDATED\_OK  
 EVIDENCE\_INDEX\_MIRROR\_OK

Notes:

EPIC017 D1 originally introduced the CLI guard logs under `artifacts/cli/guards/**` and wired them into the evidence skeleton. EPIC018 PR03 completes the D3 slice by adding canonical guard tools, determinism-rails integration, CI wiring, and `tests/cli/test_serializer_guards.py`, and by ensuring that each guard artifact has a governed path-proof and Index/Mirror entry.

Per current posture: guard proofs are **evidence-only deliverables** unless and until Governance explicitly registers guard tokens and defines their semantics. Closed-rails CI runs using the canonical guard tools and artifacts are the authoritative evidence surface for guard proof review; do not mint or claim new guard tokens from this row.

EPIC018 QA05 (D3 open-rails CLI guard step) runs the same guard tools from a Codespaces environment that is intentionally **open rails only** for Live QA (SAFE\_MODE=0, ALLOW\_NETWORK=1). In that environment, both guards exit with code `1` and their logs and exit-code files are stored under `audit/qa/hde-epic018/d3-cli-guards/`. These failures are expected and non-actionable: they show that the guards correctly enforce determinism env pins and **fail closed when rails are not pinned**, not that CLI serializer/emitter wiring is broken.

Live QA in open-rails environments may run the guards informationally (to confirm env-pin enforcement) and reference CI status; open-rails guard runs are not required to exit 0 and MUST NOT be treated as satisfying acceptance.

Evidence / artifacts:

Guard tools and tests (titles-only):

`tools/cli/serializer_grep_guard.py`

`tools/cli/emitter_symbol_proof.py`

`tests/cli/test_serializer_guards.py` — exercises guard behavior in clean and violation scenarios.

Guard artifacts and proofs (closed-rails CI acceptance):

`artifacts/cli/guards/serializer_grep_guard.log`

`artifacts/cli/guards/serializer_grep_guard.log.path_proof.txt`

`artifacts/cli/guards/emitter_symbol_proof.txt`

`artifacts/cli/guards/emitter_symbol_proof.txt.path_proof.txt`

Index/Mirror records (closed-rails CI acceptance):

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

Closed-rails Live QA (governed check log; EPIC024 PO-014):

`audit/qa/hde-epic024/checks/D08_cli_guardrail/primary.log` — governed QA check log for D08 CLI guardrail (PASS; evidence\_outputs includes `artifacts/cli/guards/serializer_grep_guard.log`).

Open-rails Live QA (informational, non-gating):

`audit/qa/hde-epic018/d3-cli-guards/d3-cli-guard-001-serializer_grep_guard.log`

`audit/qa/hde-epic018/d3-cli-guards/d3-cli-guard-001-serializer_grep_guard-exit.txt` (contains `1` under open rails).

`audit/qa/hde-epic018/d3-cli-guards/d3-cli-guard-001-emitter_symbol_proof.txt`

`audit/qa/hde-epic018/d3-cli-guards/d3-cli-guard-001-emitter_symbol_proof-exit.txt` (contains `1` under open rails).

`audit/qa/hde-epic018/qa_notes.md` — Step 3 entry noting that D3 CLI guards were run under an open-rails Codespaces environment.

Notes:

EPIC017 D1 originally introduced the CLI guard logs under `artifacts/cli/guards/**` and wired them into the evidence skeleton. EPIC018 PR03 completes the D3 slice by adding canonical guard tools, determinism-rails integration, CI wiring, and `tests/cli/test_serializer_guards.py`, and by ensuring that each guard artifact has a governed path-proof and Index/Mirror entry. For D3 guard tokens (`CLI_SERIALIZER_GUARD_OK`, `SERIALIZER_GREP_GUARD_OK`, `EMITTER_SYMBOL_PROOF_OK`), **closed-rails CI runs** using these tools and artifacts are the authoritative acceptance surface.

EPIC018 QA05 (D3 open-rails CLI guard step) runs the same guard tools from a Codespaces environment that is intentionally **open rails only** for Live QA (SAFE\_MODE=0, ALLOW\_NETWORK=1). In that environment, both guards exit with code `1` and their logs and exit-code files are stored under `audit/qa/hde-epic018/d3-cli-guards/`. These failures are expected and non-actionable: they show that the guards correctly enforce determinism env pins and **fail closed when rails are not pinned**, not that CLI serializer/emitter wiring is broken.

For PF09 and Governance:

D3 guard checklist items and guard tokens are **satisfied** by CI runs under closed determinism rails and the canonical guard artifacts in `artifacts/cli/guards/**` plus their Index/Mirror entries.

Live QA in open-rails environments may run the guards **informationally** (to confirm env-pin enforcement) and **reference** CI status for D3 acceptance; open-rails guard runs are not required to exit 0 and MUST NOT be treated as satisfying D3 guard tokens on their own.

Broader CLI/Reader parity and A7 transport behavior remain the responsibility of Conjunction and Distillation tasks (for example HDE-CONJ003, HDE-CONJ004, HDE-DIST001) that consume these guard artifacts and tokens; this subtask is scoped to the presence, correctness, and evidence discipline of the CLI serializer/emitter guard tools and logs.

---

## Task HDE-CALC003 — Repository & Tooling Skeleton

**Task name/label:** Repository & Tooling Skeleton

**Task status:** **Partial**

**Task ID:** HDE-CALC003

**Task description:**  
 Provide a deterministic repository/tooling skeleton with an ordered sanity pipeline, Human Evidence Index and Machine Mirror, strict mirror discipline, locale pins, per-run registry report, topology orientation demo, and CI gates that enforce evidence presence and parity.

**Task notes:**

Audit (v1 — 2025-11-17) originally flagged missing mirror/index and canonicalization tokens. EPIC017 PR02 (D2) implemented the **evidence skeleton**: `tools/evidence/update_evidence_index.py` now owns `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` is the single Machine Mirror, `.path_proof.txt` files are generated consistently, and the **topology orientation demo** (`audit/gates/topology/orientation_demo.txt`) is wired into CI.

Evidence skeleton CI now runs under rails-closed env (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and includes:

`python tools/evidence/update_evidence_index.py --check`

`python tools/evidence/orientation_demo.py --check`

`ci/checks/check_mirror_schema.sh`

`python ci/checks/check_release_identity.sh`

`python -m pytest tests/evidence tests/ops/test_evidence_index.py`

ensuring INDEX/sentinel/mirror/path-proofs/orientation demo are canonical and drift-free.

Task remains **Partial** until the ordered sanity pipeline (`scripts/make_sanity.sh` or equivalent), per-run registry\_report integration, and global locale pins for all lint/test/artifact jobs are fully implemented and evidenced.

### **Subtask HDE-CALC003.1 — Closed-rails sanity pipeline (ordered)**

**Subtask name/label:** Closed-rails sanity pipeline (ordered)

**Subtask description:**  
 Provide a single, closed-rails sanity pipeline entrypoint that orchestrates the core Calcination evidence harness under determinism env rails and fails closed on any drift:

**Canonical entrypoint (titles-only).**

Use `tools/evidence/run_sanity_pipeline.py` as the canonical sanity pipeline entrypoint for Calcination evidence (EPIC018 D4).

The pipeline MUST call `ensure_determinism_env()` from `engine.runtime.determinism_env` at startup and abort with a clear error if the determinism env pins are not satisfied.

**Ordered steps (minimum).**

Run a fixed sequence of steps that, at minimum, covers:

D1 serializer determinism and CLI canonical bytes tests.

D2 determinism env rails checks (env pins helper and `ci/checks/check_env_pins.sh`).

D3 CLI serializer/emitter guards.

PF12 evidence skeleton checks (Human Index, sentinel, Machine Mirror, path-proofs, orientation demo).

For each step, record a deterministic line in the sanity log such as `check <name>:OK` or `check <name>:FAIL`, and emit a final `summary:PASS` or `summary:FAIL` line; stop on the first failure.

The pipeline runs under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and MUST NOT perform vendor or external I/O.

**Sanity log artifact.**

Emit `artifacts/sanity/sanity.log` as a stable, canonical text log (LF-terminated, no timestamps or env-specific noise) containing:

A header line (for example `sanity_pipeline`).

A single `env:` line capturing the determinism env pins and suite set in a normalized form.

One `check <step>:OK|FAIL` line per step.

A final `summary:PASS|FAIL` line.

For `artifacts/sanity/sanity.log`, maintain a co-located `artifacts/sanity/sanity.log.path_proof.txt` transcript with governed fields (path, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`) consistent with PF12 semantics.

Validator posture (D18 canonical surface; no marker lines). Validators MUST accept the canonical structure described above (header `sanity_pipeline`, then `env:`, then one-or-more `check <step>:OK|FAIL` lines, ending with a `summary:PASS|FAIL` line; PASS predicates require `summary:PASS`) and MUST NOT require additional marker lines such as `run:sanity-pipeline` or `env_pins:`.

This subtask is gated, in part, by the QA acceptance token `SANITY_PIPELINE_LOGGED_OK` (semantics single-homed in Glow QA Guide): a sanity pipeline run that claims this token MUST produce a non-empty sanity log with the header, `env:` line, step `check` lines, and a final `summary:PASS|FAIL` line; a missing or empty sanity log is treated as a tooling/harness failure for that QA step (FAIL\_TOOLING under PF19) rather than as a green behavior run.

**Index/Mirror discipline.**

Treat the sanity log as a governed artifact:

Add an entry to `docs/evidence/INDEX.json` (for example `artifact_key: "sanity.pipeline.log"`, `discovered_physical_path: "artifacts/sanity/sanity.log"`).

Ensure `docs/evidence/INDEX.sha256` is updated to match the canonical `INDEX.json` bytes.

Ensure `artifacts/evidence_index.jsonl` contains a matching mirror record with correct `sha256`, `size_bytes`, and `proof_anchor` pointing to `artifacts/sanity/sanity.log.path_proof.txt`, following mirror field-order and canonical JSONL rules.

Any change to the sanity pipeline steps or log format MUST be accompanied by refreshed sanity log, path-proof, and Index/Mirror entries in the same PR, validated via `tools/evidence/update_evidence_index.py --check` and `tools/evidence/orientation_demo.py --check`.

**CI integration (titles-only).**

CI MUST include a dedicated sanity-pipeline job that runs `python tools/evidence/run_sanity_pipeline.py` under closed rails, alongside the underlying suites it orchestrates (serializer tests, env pins checks, CLI guards, evidence skeleton tests).

The sanity pipeline job is a “belt and suspenders” orchestrator: it does not replace the individual determinism/evidence jobs, but it MUST be green for D4 acceptance.

**Subtask status:** **Done**

**Epic or card:** **EPIC-018 (D4 — Evidence skeleton & sanity pipeline)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`SANITY_PIPELINE_LOGGED_OK` *(acceptance token; semantics and FAIL\_TOOLING classification live in Glow QA Guide and HDE-Phased Epics; PF09 is consumer-only)*

**Evidence / artifacts:**

`tools/evidence/run_sanity_pipeline.py` — Calcination sanity pipeline entrypoint.

`artifacts/sanity/sanity.log` — closed-rails sanity log (canonical text, LF-terminated).

`artifacts/sanity/sanity.log.path_proof.txt` — path-proof transcript for the sanity log.

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — Human Index and sentinel including the sanity log entry.

`artifacts/evidence_index.jsonl` — Machine Mirror record for `sanity.pipeline.log` with `proof_anchor` to the sanity log path-proof.

`audit/gates/sanity_pipeline/sanity_pipeline.log` — EPIC024 governed sanity pipeline log (D07 check requires `summary:PASS`).

`audit/qa/hde-epic024/checks/D07_sanity_pipeline/primary.log` — governed QA check log for D07 sanity pipeline (PASS; evidence\_outputs points to the fixed-path `audit/gates/sanity_pipeline/sanity_pipeline.log`).

CI evidence (titles-only):

`.github/workflows/ci.yml` sanity-pipeline job configuration.

`tests/evidence/test_sanity_pipeline.py` — unit tests for sanity pipeline orchestrator behavior (success and fail-fast cases).

`tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` — evidence skeleton and self-record invariants used by the pipeline.

**Notes:**  
 EPIC018 PR04 (“Evidence Index Self-Proof Coherence — sanity pipeline”) implements the closed-rails sanity pipeline entrypoint and wires it into CI, regenerates the Evidence Index/mirror and path-proofs (including the `index.machine_mirror` self-record), and fixes metadata drift for `engine.order.abba_identity.bytes` and the Machine Mirror self-record. Subsequent QA work (for example EPIC019 Step 7\) uses this pipeline and its log as a gate for epic-level sanity tokens; when QA harnesses invoke the pipeline but capture no output in step logs, PF19’s `SANITY_PIPELINE_LOGGED_OK` classification and the QA harness discipline subtask (HDE-CALC003.14) require that those steps be marked FAIL\_TOOLING and treated as blocked until the harness is fixed, rather than silently treating the pipeline as passed.

### Subtask HDE-CALC003.2 — Human Evidence Index

**Subtask name/label:** Human Evidence Index (titles/paths only)

**Subtask description:**  
 Maintain `docs/evidence/INDEX.json` as the single home for evidence titles/paths; update in the same PR as governed artifacts, without duplicating its entries in PF09.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_HASH_OK`

**Evidence / artifacts:**

`tools/evidence/update_evidence_index.py` — canonicalizes and writes `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`.

`docs/evidence/INDEX.json` — canonical list of `{artifact_key, discovered_physical_path}` objects.

`docs/evidence/INDEX.sha256` — sha256 over canonical `INDEX.json` bytes.

`tests/evidence/test_evidence_skeleton.py` — validates that on-disk INDEX matches canonical render and sentinel hash.

`tests/ops/test_evidence_index.py` — ops-level checks for Index/hash behavior.

**Notes:**  
 PF09 does not restate Index entries or schemas; those remain single-homed in PF12. This subtask records that the Human Index and sentinel now exist, are canonical, and are enforced by CI under rails-closed env.

### Subtask HDE-CALC003.3 — Evidence Index hash sentinel

**Subtask name/label:** Human Evidence Index hash sentinel

**Subtask description:**  
 Maintain `docs/evidence/INDEX.sha256` as sha256 over the exact bytes of `INDEX.json`; update in the same PR as the Human Index and gate on `EVIDENCE_INDEX_HASH_OK`.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`EVIDENCE_INDEX_HASH_OK`

**Evidence / artifacts:**

`tools/evidence/update_evidence_index.py` — computes and writes `docs/evidence/INDEX.sha256`.

`docs/evidence/INDEX.sha256` — single-line sentinel `<sha> docs/evidence/INDEX.json`.

`tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` — ensure sentinel matches canonical `INDEX.json`.

**Notes:**  
 CI will now fail on any mismatch between `INDEX.json` and `INDEX.sha256`, closing the loop PF09/PF12 describe for drift detection.

### Subtask HDE-CALC003.4 — Machine Evidence Index (JSONL)

**Subtask name/label:** Machine Evidence Index — JSONL (records-only)

**Subtask description:**  
 Provide `artifacts/evidence_index.jsonl` as a records-only Machine Mirror with one JSON object per line; canonical JSONL (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one LF); unknown keys rejected; maintain 1:1 parity with the Human Index; provide path-proofs.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`artifacts/evidence_index.jsonl` — the single Machine Mirror file.

`tools/evidence/update_evidence_index.py` — renders mirror records from the canonical Human Index.

`ci/checks/check_mirror_schema.sh` — enforces field set/order, canonical JSONL, and self-record behavior.

`tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` — validate mirror consistency, path-proof wiring, and self-record handling.

**Notes:**  
 Mirror schema and record-type semantics remain in PF12 Appendix C; PF09 enforces usage, parity, and CI behavior for the hardened Machine Mirror.

### Subtask HDE-CALC003.5 — Mirror discipline

**Subtask name/label:** Mirror discipline (field order & uniqueness)

**Subtask description:**  
 Enforce ASCII field order `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`; sort-before-write by `(artifact_key, discovered_physical_path)`; ensure uniqueness of that pair; keep `artifacts/evidence_index.jsonl` as the single Machine Mirror file.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`artifacts/evidence_index.jsonl` — hardened Machine Mirror.

`ci/checks/check_mirror_schema.sh` — asserts field set/order, uniqueness, and canonical JSONL.

**Notes:**  
 PF12 remains the single home for mirror schema; PF09 now reflects that mirror discipline is enforced and CI-gated via the EPIC017 D2 work.

### **Subtask HDE-CALC003.6 — Registry report (per-run)**

**Subtask name/label:** Registry report generation (names-only)

**Subtask description:**  
 Produce `artifacts/registry/registry_report.json` (canonical JSON) on every run.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC021 (D2 — evidence skeleton)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK` (when indexed)

**Evidence / artifacts:**

`artifacts/registry/registry_report.json` — governed registry report (canonical JSON).

`artifacts/registry/registry_report.json.path_proof.txt` — path proof transcript for the governed report.

Index/Mirror entries (titles-only; governed by Evidence Index discipline):

`docs/evidence/INDEX.json` includes `registry.registry_report` with expected discovered path and metadata.

`artifacts/evidence_index.jsonl` has a corresponding Machine Mirror record (sha256/size/proof\_anchor) for the same artifact.

Tests (titles-only; closed rails):

`tests/config/test_registry_report.py`

`tests/config/test_registry_report_determinism.py`

`tests/config/test_registry_report_indexing.py`

**Notes:**  
 EPIC021 D2 makes `registry_report` a first-class governed artifact and proves canonical bytes, two-run identity, and Index/Mirror/path-proof coupling under closed rails as part of the evidence skeleton completion.

### **Subtask HDE-CALC003.7 — Locale pins (repo-wide)**

**Subtask name/label:** Locale pins for all byte checks

**Subtask description:**  
 Export and enforce deterministic locale/env pins for all byte-sensitive checks, with explicit rails posture for determinism suites:

**Repo-wide intent.**

All lint/test/artifact jobs that produce or compare governed bytes SHOULD run under:

`LC_ALL=C`

`LANG=C`

`TZ=UTC`

PF09 does not enumerate every job; it requires that the CI configuration and scripts make these pins explicit and keep them stable for determinism-sensitive work.

**Determinism suites (Calcination evidence jobs).**

Determinism-sensitive suites (evidence skeleton, orientation, invariance, registry\_report, sanity pipeline) MUST run under closed rails:

`LC_ALL=C`, `LANG=C`, `TZ=UTC`

`SAFE_MODE=1`, `ALLOW_NETWORK=0`

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC021 (D2 — evidence skeleton env-pin enforcement)**

**Tokens:**

`DETERMINISM_ENV_PINS_OK` (token semantics live in Governance/QA canon; PF09 is consumer-only)

**Evidence / artifacts:**

Canonical implementation (titles-only):

`engine/runtime/determinism_env.py` — defines the pin set and helper functions (e.g., `ensure_determinism_env`, `render_env_log`, `record_env_log`).

`ci/checks/check_env_pins.sh` — asserts the determinism env pins and fails if they deviate.

**Canonical governed evidence surface for `DETERMINISM_ENV_PINS_OK` (single valid binding):**

`audit/gates/determinism/env_pins.log`

`audit/gates/determinism/env_pins.log.path_proof.txt`

Ledger/index/mirror parity (titles-only; required when the token is claimed):

`token_evidence_matrix` binds `DETERMINISM_ENV_PINS_OK` to `audit/gates/determinism/env_pins.log`.

`docs/evidence/INDEX.json` points the determinism env pins artifact key to `audit/gates/determinism/env_pins.log`.

`artifacts/evidence_index.jsonl` mirrors the exact `discovered_physical_path` and uses `audit/gates/determinism/env_pins.log.path_proof.txt` as `proof_anchor`.

Evidence that determinism pins are enforced for evidence jobs:

`tools/evidence/update_evidence_index.py` validates closed-rails env pins at startup via `ensure_determinism_env` (SAFE\_MODE, ALLOW\_NETWORK, and locale pins), preventing evidence jobs from running under unpinned envs.

`tests/evidence/test_evidence_index_env.py` — enforces env-pin posture for evidence-index jobs under closed rails (green in EPIC021 PR5 runs).

**Notes:**  
 SoT: canon — `DETERMINISM_ENV_PINS_OK` MUST be satisfied only by `audit/gates/determinism/env_pins.log` (with its `.path_proof.txt`) and MUST NOT be bound to `artifacts/proofs/env_pins.txt` (or any similarly named file). The first JSON record in the canonical `env_pins.log` surface MUST be a compact object with keys `env` (object), `status` (string), `suites` (array); validators MUST NOT require schema, rails, or other wrapper fields. Any deviation is a mechanical blocker; correct the binding, do not interpret it.

EPIC021 D2 closes env-pin enforcement for evidence jobs by making the evidence-index updater fail closed unless the determinism env pins are satisfied.

### Subtask HDE-CALC003.8 — Topology orientation demo

**Subtask name/label:** Topology orientation demo

**Subtask description:**  
 Add `audit/gates/topology/orientation_demo.txt` showing high→low normalized to min→max `NN–NN` (before/after) as a topology orientation demo.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

(Topology-orientation token name, if any, remains single-homed in Governance.)

**Evidence / artifacts:**

`tools/evidence/orientation_demo.py` — generates and checks `orientation_demo.txt`.

`audit/gates/topology/orientation_demo.txt` — deterministic report with header, `total_artifacts`, `status: ok|mismatch`, and sample/issue lines.

`audit/gates/topology/orientation_demo.txt.path_proof.txt` — path-proof transcript.

`tests/evidence/test_orientation_demo.py` — validates orientation demo behavior and mismatch detection.

**Notes:**  
 CI runs `python tools/evidence/orientation_demo.py --check` under pinned env; this subtask now represents a governed, drift-checked topology orientation demo as part of the evidence skeleton.

### **Subtask HDE-CALC003.9 — Wire local run targets**

**Subtask name/label:** Wire local run targets for sanity

**Subtask description:**  
 Standardize the canonical local sanity pipeline entrypoint and log semantics; keep any wrapper script wired to the ordered pipeline.

* Canonical entrypoint: `tools/evidence/run_sanity_pipeline.py` (writes `artifacts/sanity/sanity.log`).

* If `scripts/make_sanity.sh` is retained, it MUST invoke the canonical entrypoint without altering ordering or log semantics.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:** Unknown

**Evidence / artifacts:**  
 `tools/evidence/run_sanity_pipeline.py`  
 `artifacts/sanity/sanity.log`  
 `scripts/make_sanity.sh`

**Notes:**  
 Codex Audit HDE-EPIC024 reports the sanity pipeline entrypoint exists and produces the governed log; treat the python entrypoint as canonical, with wrapper scripts as optional aliases.

### **Subtask HDE-CALC003.10 — Indexing & parity CI gates**

**Subtask name/label:** Indexing & parity CI gates

**Subtask description:**  
 Update the Human Evidence Index and Machine Mirror in the same PR (records-only; with path-proofs); ensure governed locations only (`artifacts/**`, `audit/**`, `docs/evidence/**`); reject ungoverned `codex/out/**`; and fail CI if Index/Mirror miss entries, violate canonical JSONL, have unknown keys, missing path-proofs, wrong field order, or are unsorted.

**Subtask status:** **Partial**

**Epic or card:** **EPIC-017 (D2)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

CI evidence skeleton jobs and checks (titles-only):

`python tools/evidence/update_evidence_index.py --check`

`python tools/evidence/orientation_demo.py --check`

`ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl`

`python -m pytest tests/evidence tests/ops/test_evidence_index.py`

`epic020-evidence-bundles` (CI job in `.github/workflows/ci.yml`) — closed-rails EPIC020 Candidate 1 pipeline that runs the EPIC020 bundle/manifest generator, calls `python tools/evidence/update_evidence_index.py --epic-id HDE-EPIC020` followed by `python tools/evidence/update_evidence_index.py --check`, invokes the hardened mirror schema checker, and executes `python -m pytest tests/evidence/test_epic020_bundle_index_integration.py` under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `APP_ENV=ci`.

NOTE (mirror schema check invocation): `ci/checks/check_mirror_schema.sh` is intended to be executed **directly** (CI-direct invocation). Do **not** invoke it via `bash ci/checks/check_mirror_schema.sh <ARGS>` (bash will misinterpret the file). Keep operator guidance consistent with CI’s direct invocation. If an environment cannot execute the script directly (missing exec bit), treat it as a tooling/environment defect to remediate, not a reason to introduce alternate invocation patterns in docs.

 Hardened artifacts:

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl` / `artifacts/evidence_index.jsonl.sha256`

Sibling `*.path_proof.txt` transcripts for governed artifacts (including `docs/evidence/INDEX.json.path_proof.txt`, `docs/evidence/INDEX.sha256.path_proof.txt`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256.path_proof.txt`, and `audit/gates/topology/orientation_demo.txt.path_proof.txt`).

EPIC020 bundle generator invariants and tests (titles-only):

`tools/evidence/epic020_bundle.py` — EPIC020 Candidate 1 bundle/manifest generator used by the `epic020-evidence-bundles` job; must support both mapping and string artifact entries from `docs/acceptance_map_epic020.json`, honor `discovered_physical_path` for member discovery, and skip any acceptance-map entry whose `discovered_physical_path` points under `artifacts/epic020/bundles/**` with `.bundle.json` or `.manifest.json` suffixes.

`tests/tools/test_epic020_bundle_tool.py::test_epic020_bundle_handles_string_artifact_entries` — regression test that runs the bundle tool against the real `docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` pairing and asserts that string-valued `artifacts` entries are handled correctly and produce deterministic bundles without failures.

`tests/tools/test_epic020_bundle_tool.py::test_epic020_bundle_ignores_outputs_listed_as_artifacts` — regression test that writes a synthetic acceptance map where EPIC020 token `EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE` has both a real member and entries pointing at `artifacts/epic020/bundles/EPIC020.D1.HTTP_COMPAT_HTTP_BUNDLE.bundle.json` and `.manifest.json`, then asserts successful bundle build with exactly one member and no `discovered_physical_path` under `/epic020/bundles/`, codifying that bundle/manifest outputs are never re-ingested as members even when listed as governed artifacts.

`tests/evidence/test_epic020_bundle_index_integration.py` — EPIC020 bundle/manifest integration test that verifies running the bundle tool followed by the Index updater produces correct EPIC020 bundle/manifest records in both the Human Evidence Index and Machine Mirror (hashes, sizes, timestamps, and `tokens` lists matched to EPIC020 acceptance tokens and acceptance map `token_status` keys).

**Notes:**  
 EPIC017 PR02 wired the baseline Index/Mirror/Orientation evidence skeleton into CI under closed rails and satisfied a large part of this subtask by enforcing canonical JSONL, path-proof presence, and mirror schema across registry/config artifacts and FE/BE bundles. EPIC020 Candidate 1 extends the same discipline to error/presenter/internal-version evidence by introducing the `epic020-evidence-bundles` CI job and EPIC020 bundle/manifest records in the Index/Mirror, so that EPIC020 D1–D3 and QA/rails tokens can be proved from EPIC020 bundle artifacts rather than per-member rows.

This subtask remains **Partial**: the EPIC020-specific bundles and CI job are now part of the standard evidence skeleton, but broader sanity-pipeline integration (for example pack identity and A7 proofs, DB posture, BodyGraph evidence families, and extension of these patterns beyond EPIC020) is still owned by later Distillation tasks and future epics.

### **Subtask HDE-CALC003.11 — Evidence index touch discipline**

**Subtask name/label:** Evidence Index/Mirror touch discipline

**Subtask description:**  
 For any change that touches the Human Index, its sentinel, or the Machine Mirror, enforce a standard tool chain under closed rails in the same PR so that the Index, Mirror, and path-proofs stay in lockstep:

**Scope.**  
 This discipline applies to any PR that:

* Adds, removes, or edits:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

* Or calls `python tools/evidence/update_evidence_index.py` in **write mode** (directly or via an evidence generator such as `tools/errors/generate_error_artifacts.py`) and expects governed artifacts under `docs/evidence/**`, `artifacts/**`, or `audit/**` to change.

**Required commands (closed-rails env).**

1. Run `python tools/evidence/update_evidence_index.py` in **write** mode to regenerate the Human Index (`INDEX.json` and `INDEX.sha256`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) according to PF12 semantics.

2. Then run `python tools/evidence/update_evidence_index.py --check` to validate the regenerated Index and Mirror against the committed artifacts (including the mirror body hash and hash sentinel) under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`).

3. Run `python tools/evidence/orientation_demo.py` in **write** mode to regenerate the topology orientation report (`audit/gates/topology/orientation_demo.txt`) and any associated mirror-coherence evidence (including its path-proof transcript).

4. Then run `python tools/evidence/orientation_demo.py --check` to verify that Index entries, Mirror records, and path-proofs are coherent (including the `index.machine_mirror` self-record) under the same closed-rails env.

5. Run the machine-mirror self-record regression test(s) under the same closed-rails env (for example `python -m pytest -q tests/evidence/test_machine_mirror_self_proof.py`) to ensure self-proof hashing/proof semantics are still valid after any evidence-tooling change.

**Same-PR rule.**  
 All of the above commands MUST be run, and their outputs committed, in the **same PR** that changes the Human Index, sentinel, Machine Mirror, or governed artifacts referenced by the Index so that:

* `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and `*.path_proof.txt` remain consistent, and

* acceptance tokens `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, and `MACHINE_MIRROR_UPDATED_OK` continue to be satisfied for the current mirror body and Index.

**Subtask status:** **Partial**

**Epic or card:** EPIC-018 (D4 evidence skeleton & mirror)

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`  
 `EVIDENCE_INDEX_HASH_OK`  
 `MACHINE_MIRROR_UPDATED_OK`

**Evidence / artifacts:**

CI and local run logs for:

* `python tools/evidence/update_evidence_index.py` (write mode)

* `python tools/evidence/update_evidence_index.py --check`

* `python tools/evidence/orientation_demo.py` (write mode)

* `python tools/evidence/orientation_demo.py --check`

* `python -m pytest -q tests/evidence/test_machine_mirror_self_proof.py`

plus Index, sentinel, Mirror, and topology orientation artifacts:

* `docs/evidence/INDEX.json / docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.json.path_proof.txt / docs/evidence/INDEX.sha256.path_proof.txt`  
  `artifacts/evidence_index.jsonl / artifacts/evidence_index.jsonl.sha256`  
* `artifacts/evidence_index.jsonl.path_proof.txt / artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

**Notes:**  
 Codex Audit HDE-EPIC024 records that Evidence Index writer/check-mode semantics are implemented (`update_evidence_index.py --check` fails if stale), but EPIC024 QA step logs that demonstrate check-mode enforcement under `audit/qa/hde-epic024/` are not present.

Addendum 4 for HDE-EPIC020 PR 2b showed a real failure of this discipline: `update_evidence_index.py --check` passed after adding EPIC020 D1 error artifacts under `errors/*` and `parity/*`, but `orientation_demo.py --check` then failed with `ORIENTATION_DRIFT` because `orientation_demo.txt` and its path proof still reflected the pre-PR evidence skeleton. Going forward, any PR that uses `update_evidence_index.py` in write mode for governed artifacts (including error evidence generators such as `tools/errors/generate_error_artifacts.py`) is out of spec unless it also refreshes orientation demo in the same PR before CI. A future harness (tracked under EPIC018 D4 and EPIC020 follow-on work) is expected to wrap the error evidence generator, Index writer, and orientation demo into a single closed-rails job that runs `generate_error_artifacts`, `update_evidence_index.py` (write \+ `--check`), and `orientation_demo.py` (write \+ `--check`) as one atomic evidence step.

Evidence index refresh flow reference lock (plan-facing): Plan narratives and onboarding docs MUST bind the canonical refresh set (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, and all governed `*.path_proof.txt` regenerated by the refresh tooling) and MUST specify the canonical tool invocation (`python tools/evidence/update_evidence_index.py` in write mode; and `ci/checks/check_mirror_schema.sh` via direct invocation, not `bash <ARGS>`).

### **Subtask HDE-CALC003.12 — QA test tooling bootstrap (all QA Plans)**

**Subtask name/label:** QA test tooling bootstrap (all epics)

**Subtask description:**  
 Require every epic’s QA Plan to include a **standard test tooling bootstrap step** that runs before any test-driven QA steps and proves the basic tooling is present and importable:

* Activate the project virtual environment (for example `source .venv/bin/activate` or equivalent) so that the bootstrap harness runs under the same Python interpreter and environment the Engine uses for tests and CLI tools.

* Ensure pytest is installed and importable via `python -m pytest --version` (exit 0, no import error).

* Confirm that primary CLI tools exist on PATH (for example `command -v hdctl` and `command -v jq`).

If any of these checks fail, the QA tooling bootstrap harness MUST:

* Treat the situation as a **tooling/infra blocker**, not an application behavior failure for the epic.

* **MUST NOT** proceed to project tests or Engine/CLI commands for that QA flow; later steps in the QA Plan and Live QA harness MUST rely on the bootstrap result and abort when it reports a tooling failure.

* Record a governed bootstrap evidence log under `audit/qa/<epic>/test_tooling_bootstrap.log` (or equivalent) that:

  * lists each bootstrap command (at minimum `python -m pytest --version`, `command -v hdctl`, `command -v jq`) and its exit code, and

  * includes a top-level classification field (for example `tooling_failure: true|false` or a status enum) that clearly marks the run as a tooling failure when any check fails and identifies which check failed.

Epic behavior tokens remain pending until tooling is repaired and tests or CLI commands run under a healthy environment and updated bootstrap log.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC021 (D3 — QA bootstrap and viability logging)**

**Tokens:**

`QA_BOOTSTRAP_OK`  
 `QA_BOOTSTRAP_TOOLING_FAIL`

**Evidence / artifacts:**

Harness (titles-only):

`tools/qa/epic021_qa.py` — closed-rails QA harness that performs bootstrap checks and writes both per-run and epic-level bootstrap logs.

Bootstrap evidence (QA\_ROOT):

`audit/qa/hde-epic021/test_tooling_bootstrap.log` — canonical EPIC-level bootstrap pointer log.

`audit/qa/hde-epic021/<run-id>/D0_bootstrap.log` — per-run bootstrap log with env pins and summary PASS/FAIL.

Tests (titles-only; closed rails):

`tests/qa/test_tooling_bootstrap.py` — exercises the EPIC021 QA harness bootstrap/log emission and validates log formats and rails posture.

**Notes:**  
 EPIC021 provides the first end-to-end implemented instance of the PF09 bootstrap discipline: a closed-rails harness writes canonical bootstrap evidence under QA\_ROOT and keeps it refreshed as part of the epic’s D3 close workflow. Token semantics are governance/QA-owned; PF09 uses the canonical bootstrap tokens by name only.

---

### **Subtask HDE-CALC003.13 — Canonical pytest invocation for QA & CI**

**Subtask name/label:** Canonical pytest invocation (`python -m pytest`)

**Subtask description:**  
 In Codespaces and similar environments, require that QA Plans and CI jobs use **`python -m pytest`** as the canonical pattern for running tests, to avoid brittle `.venv/bin/pytest` shims:

* Test entries SHOULD use `python -m pytest <PYTEST_ARGS>` and/or `./scripts/run-tests` (if present) to avoid split brain between docs and automation.

* A failure of `python -m pytest --version` or an import error for pytest MUST be treated and logged as a **tooling failure**, not a behavior failure.

* When a `.venv/bin/pytest` shim exists but is broken, that failure MUST be captured in a tooling log and worked around by running the suite via `python -m pytest` once tooling is repaired; epic behavior tokens remain pending until tests run successfully under the canonical pattern.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (pytest/tooling tokens will be minted in Governance/QA canon)

**Evidence / artifacts:**

* CI job and QA Plan snippets (titles-only) showing `python -m pytest` used consistently for ingest, sampler, and other test suites.

* QA logs demonstrating broken `.venv/bin/pytest` shims being classified as tooling failures and successful reruns via `python -m pytest` under closed rails.

**Notes:**  
 EPIC019 Live QA showed that a broken `.venv/bin/pytest` shim can masquerade as “tests failed” without clear tooling classification; this subtask codifies `python -m pytest` as the canonical pattern and treats shim failures as infra/CI defects.

### **Subtask HDE-CALC003.14 — QA harness discipline (tooling vs behavior, commands, emptiness)**

**Subtask name / label:** QA harness discipline (tooling vs behavior, commands, emptiness)

**Subtask status:** **Partial**

**Epic provenance:** EPIC019 (live QA harness baseline)

**Tokens / gates:** `QA_HARNESS_DISCIPLINE_OK`

**Purpose:** Enforce the discipline that makes QA evidence verifiable and governed: correct and stable paths, stable command invocations, explicit manifests, and honest emptiness conventions. This is about behavior and guarantees, not just tooling.

**Acceptance criteria (what “Done” looks like):**

* QA steps emit governed logs under a stable root: `audit/qa/<epic-id>/checks/<step-name>/primary.log`

* Each log includes: `run_id`, `check_id`, `status` from the allowed vocabulary, and defaultable “emptiness” fields.

* A manifest exists (or is produced) that enumerates all QA step logs, with stable paths.

* Logs do not invent executables; they reference real repo paths and commands.

* Empty or absent artifacts are labeled explicitly (e.g., `NOT_FOUND`) and do not get silently “filled in”.

* Token claims in logs are present where applicable and remain non-gating unless explicitly required by policy.

**Implementation notes / constraints:**

* Status vocabulary is strict: `PASS` / `FAIL` / `WARN` / `BLOCKED` (and the PF09 allowed status vocabulary for tasks).

* “Governed paths” means the artifact path itself is part of the proof; avoid ad hoc locations.

* Evidence roots are not code roots. A log path like `audit/qa/...` must not be treated as a code path.

**How to pass the proof gate and earn the token:**

* QA ROOT step logs for QA Plan steps (titles/paths only), such as:

  * `audit/qa/hde-epic023/checks/D03_acceptance_map_viability/primary.log` — governed QA check log for `D03_acceptance_map_viability` (PASS; validates `audit/qa/hde-epic023/acceptance_map_viability.log`).

  * `audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log` — governed QA check log for `D05_step_logs_manifest` (PASS; writes `audit/qa/hde-epic023/qa_step_logs_manifest.json`).

  * `audit/qa/hde-epic024/checks/D19_step_logs_manifest/primary.log` — governed QA check log for `D19_step_logs_manifest` (PASS; validates `audit/qa/hde-epic024/qa_step_logs_manifest.json`).

  * `audit/qa/hde-epic024/checks/D14_harness_selftest/primary.log` — governed QA check log for `D14_harness_selftest` (PASS; plan-required `audit/gates/harness_selftest/harness_selftest.log` was missing).

  * `audit/qa/hde-epic024/checks/D09_generate_evidence_index_snapshot/primary.log` — governed QA check log for `D09_generate_evidence_index_snapshot` (PASS; validates `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`).

  * `audit/qa/hde-epic023/checks/D06_grounding_pack/primary.log` — governed QA check log for `D06_grounding_pack` (PASS; writes `audit/qa/hde-epic023/grounding_pack.json`).

  * `audit/qa/hde-epic023/checks/D09_pf23_consult_capture/primary.log` — governed QA check log for `D09_pf23_consult_capture` (PASS; validates `audit/qa/hde-epic023/consult_capture.md`).

  * `audit/qa/hde-epic023/checks/D12_close_pack/primary.log` — governed QA check log for `D12_close_pack` (PASS; validates `audit/qa/hde-epic023/close_pack.md`).  
  * `audit/qa/hde-epic024/checks/po-017_lowercase_naming/primary.log` — governed QA check log for `po-017_lowercase_naming` (PASS; directory-name casing scan).

  * `audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_audit_uppercase.txt` — empty scan output (no uppercase directory names under `audit/qa/**`).

  * `audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_artifacts_uppercase.txt` — empty scan output (no uppercase directory names under `artifacts/**`).

  * `audit/qa/hde-epic024/checks/po-017_lowercase_naming/find_docs_uppercase.txt` — out-of-scope note (docs scanning not required for PO-017).

* Manifest presence / linkage examples:

  * `audit/qa/hde-epic023/qa_step_logs_manifest.json` — required step logs manifest (see Addenda 10-13 BN 9.4.4: D05 proof).

  * `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt` — path proof used for audit-friendly verification of governed artifact location.

* Command/entrypoint provenance (no invented executables; evidence roots are not code roots):

  * Every referenced command path must exist in repo.

  * Preflight: `rg -n "python tools/qa/" docs/` and confirm each referenced script exists.

  * Preflight: `rg -n "audit/qa/" tools/` and confirm logs are not treated as source.

**Notes:**

Added from EPIC019 Live QA Addendum 11 and Addendum 14 and the HDE-Mechanics Guide “Live QA harness” section. This subtask is directly related to Token: QA\_HARNESS\_DISCIPLINE\_OK (EPIC024 PR-01 discovery treats QA\_STEP\_LOGS\_CONSOLIDATED\_OK as a deprecated alias for QA\_HARNESS\_DISCIPLINE\_OK). This subtask remains **Partial** until the discipline is applied consistently across all QA Plan steps and epics (minimum header \+ defaultable fields, status vocabulary, emptiness conventions, manifest linkage, and log path governance).

This subtask has been partially demonstrated by EPIC023’s governed QA logs and manifests (see Addenda 10-13 BN 9.4.4), but the discipline remains incomplete until the same shape is consistently produced across all required QA Plan steps and epics.

### **Subtask HDE-CALC003.15 — Acceptance map & QA harness viability check**

**Subtask name / label:** acceptance map & QA harness viability check

**Subtask description:**  
 Verify that a given epic has a viable acceptance map and that the QA harness can load it.

**Subtask status:** **Partial**

**Epic provenance:** EPIC023 (D13)

**Tokens:**  
 None (proof is the viability log in governed audit tree)

**Acceptance criteria:**  
 A viability run must succeed and emit a structured, single-file log in the governed audit tree.

**Evidence / artifacts:**

* `audit/qa/hde-epic023/viability/acceptance_map_viability.log` (proof of success; JSONL)

**Additional precedent:**  
 Addenda 14-18 BN 9.4.4 also records an EPIC024 viability run with the viability log at:

* `audit/qa/hde-epic024/checks/D13_acceptance_map_viability/primary.log`

**Notes:**  
 Addenda 19-25 BN 9.4.4 flags a viability-mode edge case: missing `token_sets.json` previously caused a crash (`FileNotFoundError`) rather than returning `TOOLING_BLOCKED`; remediation is to guard the missing token-sets case and return the tooling-blocked exit code (with test coverage) instead of raising.

Addenda 30-31 BN 9.4.4 records a correctness risk: acceptance map viability had a known “phantom pass” bug and needs a deterministic final posture for next epic hardening.

### **Subtask HDE-CALC003.16 — QA harness entrypoint repair & CI self-test (EPIC021 baseline)**

**Subtask name/label:** QA harness entrypoint repair & CI self-test

**Subtask description:**  
 Ensure the EPIC-level QA harness entrypoint behaves as a real, runnable command under closed rails and produces governed QA\_ROOT outputs.

Under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), `python tools/qa/epic021_qa.py` (with optional `EPIC021_QA_RUN_ID`) MUST:

* determine a `run_id` (default policy or from `EPIC021_QA_RUN_ID`),

* create `audit/qa/hde-epic021/<run-id>/`,

* emit `D0_bootstrap.log` plus the canonical `step_*.log` sequence for the EPIC021 D3 QA steps,

* append/update `audit/qa/hde-epic021/qa_step_logs_manifest.json` with a manifest entry for `<run-id>`,

* append/update `audit/qa/hde-epic021/acceptance_map_viability.log` with a summary aligned to the EPIC021 acceptance map and token↔evidence matrix.

Fail-closed behavior: if the entrypoint completes without creating the run directory, without producing non-empty `D0_bootstrap.log` and expected `step_*.log` files, or without updating the per-epic manifest and viability outputs, it MUST exit non-zero and record the reason as a tooling/harness failure.

A CI test in the QA suite MUST exercise the entrypoint with a synthetic run\_id and assert:

* the run directory exists and is non-empty,

* `D0_bootstrap.log` exists and is non-empty,

* all expected `step_*.log` files exist and are non-empty,

* the manifest contains an entry for the synthetic run\_id,

* the viability log is updated and non-empty.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC021 (D3 — QA bootstrap and viability logging)**

**Tokens:** **Unknown** (entrypoint self-test token family is governance/QA-owned; PF09 is consumer-only)

**Evidence / artifacts:**

Entrypoint implementation (titles-only):

`tools/qa/epic021_qa.py` — script entrypoint; validates determinism env pins via `ensure_determinism_env` and exits non-zero on missing pins, without producing QA\_ROOT artifacts for the failing run id.

Operator-observable QA\_ROOT artifacts:

`audit/qa/hde-epic021/<run-id>/D0_bootstrap.log`  
 `audit/qa/hde-epic021/<run-id>/step_*.log`  
 `audit/qa/hde-epic021/qa_step_logs_manifest.json`  
 `audit/qa/hde-epic021/acceptance_map_viability.log`

Tests (titles-only; closed rails):

`tests/qa/test_epic021_harness_entrypoint.py` — subprocess test: asserts exit 0 and QA\_ROOT artifacts on `selftest-run`, and asserts non-zero exit plus no run directory/manifest entry when `SAFE_MODE` is missing.

`tests/qa/test_tooling_bootstrap.py` — includes run-id selection coverage (env override, git SHA fallback, local fallback).

CI gate (titles-only):

`.github/workflows/ci.yml` includes a closed-rails step that sets `EPIC021_QA_RUN_ID=ci-selftest-epic021` and runs `python -m pytest tests/qa/test_epic021_harness_entrypoint.py`, so CI fails if the harness stops producing the expected QA\_ROOT artifacts.

**Notes:**  
 Added from Live QA escalation; remediated by PR1 and wired into CI by PR3 so this behavior fails closed if it regresses.

---

### **Subtask HDE-CALC003.17 — Generic QA harness module (all epics; config-driven)**

**Subtask name/label:** Generic QA harness (config-driven, reusable)

**Subtask description:**  
 Provide a generic epic QA harness module that centralizes env-pin capture, bootstrap/step logging, manifest management, and acceptance-map viability generation, so future epics do not create bespoke harness logic per epic.

Epic-specific QA harness behavior MUST be provided by configuration (epic id, QA\_ROOT, acceptance map path, token matrix path, step sequence), not by writing new per-epic harness modules.

Epic-specific harness entrypoints may exist as thin wrappers for convenience, but they MUST delegate to the generic harness module and must not re-implement logging, QA\_ROOT layout, manifest updates, or viability updates in bespoke per-epic code.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC021 (D3 — QA bootstrap and viability logging)**

**Tokens:** **Unknown** (generic harness token family is governance/QA-owned; PF09 is consumer-only)

**Evidence / artifacts:**

Generic harness module (titles-only):

`tools/qa/qa_harness.py` — shared harness helpers and config (`HarnessConfig`, step logging, manifest de-dupe, acceptance-map viability generation).

EPIC021 wrapper delegates to generic harness (titles-only):

`tools/qa/epic021_qa.py` — constructs HARNESS\_CONFIG (epic\_id, qa\_root, acceptance\_map\_path, token\_matrix\_path, step\_names) and uses generic harness helpers to write logs and update manifest/viability.

Tests (titles-only; closed rails):

`tests/qa/test_generic_qa_harness.py` — tests generic harness helpers (env-pin failure behavior, env logging \+ D0 log write, manifest de-duplication by run\_id, viability formatting).

**Notes:**  
 The generic harness exists and EPIC021 is the first client. No other epics are wired into the generic harness ye

### **Subtask HDE-CALC003.18 — EPIC023 D22: Canonical JSON gate structured record (PASS/FAIL)**

**Subtask name/label:** canonical JSON gate structured record

**Subtask description:**  
 Ensure the canonical JSON gate produces a stable structured record artifact (governed path) that includes:

* PASS/FAIL summary

* version and schema

* hash references to check and compare logs

* timestamp

* tool and invocation

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC023 (D22)**

**Tokens:** None

**Evidence / artifacts (canonical family present; legacy report retained):**

Canonical gate family outputs (titles-only):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt`

* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt`

* `audit/gates/json_gate/canonical/json_gate_structured_record.json`

* `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`

QA closure logs (titles-only):

* `audit/qa/hde-epic023/checks/D22_canonical_json_gate_structured_record/primary.log`

* `audit/qa/hde-epic023/qa_step_logs_manifest.json`

* `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log`

Legacy report surfaces (titles-only; non-authoritative):

* `audit/gates/canonical_json/json_canonical_check.log` (legacy catalog check report)

* `audit/gates/canonical_json/canonical_json.gate.json` (legacy record; non-authoritative)

**Notes:**  
 Addenda 6-9 BN 9.4.4 (PR01 HDE-EPIC024 Review) reports the canonical gate family exists under `audit/gates/json_gate/canonical/` with required artifacts and `.path_proof.txt` siblings, and demonstrates the gate runner passing (`python tools/evidence/run_canonical_json_gate.py` exits 0). The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log` and MUST NOT be rebound as the canonical gate-family predicate surface.

Addenda 10-13 BN 9.4.4 (EPIC024 QA D02) confirms the per-epic QA check log exists at `audit/qa/hde-epic024/checks/D02_canonical_json_gate/primary.log` and that the canonical gate runner exits 0 while writing the governed gate log under `audit/gates/json_gate/canonical/` (as listed above).

Accepted closure gaps/drain targets recorded in EPIC023 Epic Record that remain relevant to this surface:

* Legacy report location remains under `audit/gates/canonical_json/`; canonical gate-family outputs bind under `audit/gates/json_gate/canonical/`.

**Invariant / binding (canonical):**

* Canonical target family (authoritative; present): `audit/gates/json_gate/canonical/json_gate_structured_record.json`.

* Canonical companion log families (authoritative; present): `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` and `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson` (plus their `.path_proof.txt` siblings).

* Legacy report family (present): `audit/gates/canonical_json/json_canonical_check.log` (non-authoritative; MUST NOT be required as the canonical family).  
* 

  ### **Subtask HDE-CALC003.19 — EPIC023 D23: Evidence Index snapshot artifact (governed pointer)**

**Subtask status:** **Partial**

**What this does:** Ensures the governed D23 Evidence Index Snapshot artifacts exist and that their validation is mechanical (PASS / FAIL\_BEHAVIOR / TOOLING\_BLOCKED), tokenless, and schema-bound.

**Tokens / gates:** None (tokenless check)

**Governed artifacts (required):**

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

**D23 status mapping (QA vocabulary; tokenless):**

* `PASS` — snapshot artifacts exist and all mechanical predicates hold

* `FAIL_BEHAVIOR` — snapshot artifacts exist, but the predicate fails (schema invalid, binding mismatch, parity false, etc.)

* `TOOLING_BLOCKED` — required snapshot artifacts are missing, unreadable, or path-proof missing

**Snapshot schema (minimal required fields; schema\_version "1"):** `evidence_index_snapshot.json` MUST be a canonical JSON object with:

* `schema_version` (string; current: `"1"`)

* `generated_at_utc` (string; RFC3339 UTC; parses; MUST NOT be in the future)

* `inputs` (object) with:

  * `human_index_path` (string; MUST equal `docs/evidence/INDEX.json`)

  * `human_index_sha256` (string; 64 lowercase hex; MUST equal sha256 of `docs/evidence/INDEX.json`)

  * `machine_mirror_path` (string; MUST equal `artifacts/evidence_index.jsonl`)

  * `machine_mirror_sha256` (string; 64 lowercase hex; MUST equal sha256 of `artifacts/evidence_index.jsonl`)

* `parity` (object) with:

  * `artifact_keys_match` (boolean; MUST be `true` for `PASS`)

**PASS predicate (mechanical):** `PASS` iff snapshot \+ path-proof exist and match, schema fields validate, `inputs.*_path` bindings are exact, `inputs.*_sha256` values match computed sha256, `parity.artifact_keys_match` is `true`, and `generated_at_utc` parses and is not in the future.

**Notes:**  
 Addenda 30-31 BN 9.4.4 records this deliverable as not closed for the epic: "Status: Ambiguous (contract/path drift documented; final contract not closed here)". Treat this subtask as Partial until the contract is deterministic and closure-grade proof is produced.

### **Subtask HDE-CALC003.20 — EPIC024 PO-006: Token registry validity check**

**Subtask name / label:** token registry validity check (PO-006)

**Subtask description:**  
 Validate that all acceptance tokens referenced by the epic acceptance map are present as canonical tokens in the acceptance-token registry export. Emit a governed comparison artifact (`token_comparison.json`) and a primary log with PASS/FAIL\_BEHAVIOR/TOOLING\_BLOCKED status; non-PASS must exit nonzero for CI gating.

**Subtask status:** **Done**

**Epic provenance:** EPIC024 (PO-006)

**Tokens:**  
 None (governed check; returns PASS/FAIL\_BEHAVIOR/TOOLING\_BLOCKED in logs)

**Evidence / artifacts:**

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log`

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/primary.log.path_proof.txt`

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/token_comparison.json`

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/token_comparison.json.path_proof.txt`

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/transcript.txt`

* `audit/qa/hde-epic024/checks/po-006_token_registry_validity/transcript.txt.path_proof.txt`

* `tests/evidence/test_po_006_token_registry_validity.py` — alias masking and failure-mode coverage.

**Notes:**  
 Inputs are `docs/acceptance_map_epic024.json` and `reports/qa_acceptance_tokens.json`. Addenda 19-25 BN 9.4.4 PR02 notes an alias-masking failure mode (deprecated aliases in the registry can mask missing canonical tokens); validator behavior should compare canonicalized acceptance tokens against raw registry spellings so alias-only exports fail. The same addenda notes planned capture files (`rg_acceptance_map_output.txt`, `rg_registry_output.txt`) are not enumerated in the OPS01 report despite analogous artifacts existing under the governed check folder; treat these captures as optional unless required by the plan template.

Addenda 30-31 BN 9.4.4 records the EPIC024 outcome for PO-006 as FAIL\_BEHAVIOR due to 11 acceptance tokens referenced by the acceptance map not present in the registry (blocker-grade). This is recorded as deferred implementation while closing the epic with caveats.

## **Task HDE-CALC004 — Programmatic Configuration System**

**Task name/label:** Programmatic Configuration System

**Task status:** **Done**

**Task ID:** HDE-CALC004

**Task description:**  
 Provide a typed, deterministic configuration system that loads governed catalogs, validates/normalizes them, enforces alias policy, emits a registry report, and exposes typed FE/BE bundles, with evidence integrated into the Evidence Index/Mirror system.

**Task notes:**

EPIC017 PR03 (D3) implemented the PF12-aligned registry loader (`engine.config.registry_loader`), enforced explicit alias policy OFF/ON with allow-list ledgers, added the canonical `registry_report.v1` generator (`tools/generate_registry_report.py`), and wired `artifacts/registry/registry_report.json` into the Evidence Index/Mirror with a governed path-proof under rails-closed CI. Loader tests under `tests/config/` cover unknown IDs, duplicates, and alias policy behavior, and registry\_report tests cover canonical JSON and two-run identity.

EPIC018 D5 extended this by introducing the closed-rails config artifact generator (`tools/config/generate_config_artifacts.py` / `tools/config/artifacts.py`), materializing governed Magic-10 and band-edges config artifacts under `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json`, and validating canonical formatting and domain invariants via `tests/config/test_config_artifacts.py`. These artifacts are wired into the Evidence Index/Mirror with path-proofs, and the D5 config acceptance map (`audit/EPIC-018_config_acceptance_map.json`) ties PF09 config tasks to artifact\_keys, tokens, and tests.

EPIC018 D6 added typed FE/BE bundles via a closed-rails bundle generator (`engine/config/bundles.py` and `tools/config/generate_bundles.py`), emitting canonical FE/BE bundle JSON under `artifacts/config_bundles/` with a `sources` block that records digests for upstream config artifacts. `tests/config/test_typed_bundles.py` validates canonical JSON, two-run identity, JSON Schema conformance (local test schemas), and strict linkage back to governed config artifacts and the registry report. FE/BE bundles are wired into the Evidence Index/Mirror with path-proofs and tested under the same determinism env rails as other config artifacts.

From PF09’s perspective (code and evidence only), the Programmatic Configuration System as defined here is now complete: loader, alias policy, registry\_report (`registry_report.v1`), governed Magic-10 and band-edges configs, and typed FE/BE bundles all exist, run under closed rails, are canonical/deterministic, and are integrated into the Evidence Index/Mirror. Remaining gaps called out in D5/D6 and Addendum 27 are documentation-only (formalizing config/bundle tokens and artifact descriptions in PF19/PF12/PF20) and do not block this checklist task; any future configuration families will be handled via new epics and tasks, not by reopening HDE-CALC004.

---

### Subtask HDE-CALC004.1 — Unknown-ID hard-fail

**Subtask name/label:** Unknown-ID hard-fail

**Subtask description:**  
 Loader must hard-fail (typed error) on any unknown identifier.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D3)**

**Tokens:**

`UNKNOWN_IDS_FAIL_CLOSED_OK`

`CONFIG_GEN_OK`

**Evidence / artifacts:**

`engine.config.registry_loader` — typed loader implementation for PF12 catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations).

`tests/config/` loader tests (titles-only), including unknown-ID and duplicate-ID cases and alias-policy OFF/ON enforcement.

**Notes:**  
 PF09 does not restate loader schemas or typed error classes; those remain single-homed in PF12 and PF14. This subtask records that the canonical loader and its tests exist and enforce the fail-closed behavior described above.

### **Subtask HDE-CALC004.2 — Input-alias policy configuration**

**Subtask name/label:** Input-alias policy configuration

**Subtask description:**  
 Default alias policy **OFF**; if ON, normalize via declared alias ledgers; outputs remain canonical; reject unknown aliases and undeclared entries.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D3)**

**Tokens:**

`UNKNOWN_IDS_FAIL_CLOSED_OK`

**Evidence / artifacts:**

`tests/config/test_alias_policy_enforcement.py` (titles-only) — verifies alias policy OFF by default, OFF+empty ledger still fails, and allow-list policy with a non-empty ledger produces the expected `alias_map`.

**Notes:**  
 Alias-policy token semantics are single-homed in Governance/Schemas; PF09 records that the loader tests enforce the OFF/allow-list/fail-closed behavior.

### **Subtask HDE-CALC004.3 — Registry report emission**

**Subtask name/label:** Emit registry report each run

**Subtask description:**  
 Emit a names-only, canonical JSON registry report each run at `artifacts/registry/registry_report.json`, generated under closed rails via the hardened registry loader and shared serializer:

Use the canonical registry report generator (titles-only; for example `tools/generate_registry_report.py` or `tools/config/generate_config_artifacts.py`) to emit `registry_report.v1` under determinism env rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`).

Ensure the report is canonical JSON (UTF-8, no BOM; sorted keys; compact; exactly one trailing LF) and carries `schema: "registry_report.v1"` and stable identity fields (for example `generated_at_utc`) consistent with PF14’s registry invariants and two-run identity.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D3); EPIC-018 (D5 config artifacts)**

**Tokens:**

`CONFIG_GEN_OK`

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`CONFIG_REGISTRY_OK`

**Evidence / artifacts:**

`engine.config.registry_loader` — typed loader implementation for PF12 catalogs and manifest (fail-closed on unknown/duplicate IDs and schema violations).

Registry report generator (titles-only):

`tools/generate_registry_report.py` / `tools/config/generate_config_artifacts.py` — closed-rails generator for `artifacts/registry/registry_report.json`.

Registry report artifacts:

`artifacts/registry/registry_report.json` — `registry_report.v1` canonical JSON snapshot.

`artifacts/registry/registry_report.json.path_proof.txt` — path-proof transcript for the registry report artifact.

Registry report tests (titles-only):

`tests/config/test_registry_report.py` — canonical formatting and schema tests (`registry_report.v1`).

`tests/config/test_registry_report_determinism.py` — two-run identity tests for the registry report.

**Notes:**  
 EPIC017 D3 established the `registry_report.v1` generator and initial Index/Mirror wiring for `artifacts/registry/registry_report.json`. EPIC018 D5 extends this by running the generator under determinism env rails, enforcing canonical JSON and two-run identity via new tests, and integrating the registry report into the D5 config acceptance map (mapping HDE-CALC004.3 → `registry.registry_report` → `CONFIG_REGISTRY_OK` plus associated tests). This subtask is considered **Complete** for the registry report slice; additional configuration artifacts are tracked in separate subtasks under HDE-CALC004.

### **Subtask HDE-CALC004.4 — Magic-10 & band-edges config artifacts**

**Subtask name/label:** Magic-10 & band-edges config artifacts

**Subtask description:**  
 Generate governed Magic-10 and band-edges configuration artifacts under closed rails via the hardened config generator and ensure they satisfy canonical JSON and domain invariants:

Run the canonical config artifact generator (titles-only; for example `python tools/config/generate_config_artifacts.py`) under determinism env rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`).

Produce:

`artifacts/thresholds/magic10_config.json` (`schema: "magic10_config.v1"`) capturing the Magic-10 order, per-category caps (inputs and integer bounds), and seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256).

`artifacts/thresholds/band_edges.json` (`schema: "band_edges.v1"`) capturing band names, edges, clamp, rounding mode, version, and a source pointer back to `math/thresholds.json`.

Ensure both artifacts are canonical JSON (UTF-8, sorted keys, compact, exactly one trailing LF) and satisfy domain invariants (Magic-10 order matches FROZEN\_MAGIC10\_ORDER; caps cover all keys with integer bounds; band edges are sorted, span the clamp range, and match the engine’s BANDS constant).

**Subtask status:** **Done**

**Epic or card:** **EPIC-018 (D5 — Config artifacts & acceptance map)**

**Tokens:**

`CONFIG_MAGIC10_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

Config generator (titles-only):

`tools/config/generate_config_artifacts.py`

`tools/config/artifacts.py`

Config artifacts:

`artifacts/thresholds/magic10_config.json`

`artifacts/thresholds/magic10_config.json.path_proof.txt`

`artifacts/thresholds/band_edges.json`

`artifacts/thresholds/band_edges.json.path_proof.txt`

Config tests (titles-only):

`tests/config/test_config_artifacts.py` — canonical JSON and domain invariants for Magic-10 and band-edges configs.

**Notes:**  
 EPIC018 D5 introduces `tools/config/generate_config_artifacts.py` and the governed Magic-10 and band-edges config artifacts, with tests ensuring canonical formatting and domain invariants. This subtask records the existence and behavior of those artifacts; indexing and parity for these configs are handled in HDE-CALC004.7.

### **Subtask HDE-CALC004.5 — Typed FE bundle**

**Subtask name/label:** Typed FE bundle

**Subtask description:**  
 Generate a typed frontend config bundle under closed rails as a projection of governed config artifacts and the registry loader, and ensure it is canonical, deterministic, and correctly linked back to its sources:

Use the canonical bundle generator (titles-only; for example `python tools/config/generate_bundles.py`) under determinism env rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`) to produce a frontend bundle artifact (for example `artifacts/config_bundles/fe_bundle.json`).

Serialize the frontend bundle via the canonical JSON emitter (`canon.sercanon`), so bundle bytes are deterministic UTF-8 JSON with sorted keys, compact separators, and exactly one trailing LF.

Ensure the frontend bundle (`config_bundle.fe.v1`) exposes a reduced, client-appropriate view:

Magic-10 order and caps.

Band edges/bands/clamp/rounding/version.

Channel IDs plus centers/domains and alias policy needed by clients.

A `sources` block that records `path`, `sha256`, and `size_bytes` for each upstream governed artifact (at minimum Magic-10 config, band edges, and registry report), so bundles are provably derived from governed config and registry artifacts.

**Subtask status:** **Done**

**Epic or card:** **EPIC-018 (D6 — Typed FE/BE bundles)**

**Tokens:**

`CONFIG_BUNDLES_DETERMINISTIC_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

Bundle generator (titles-only):

`engine/config/bundles.py`

`tools/config/generate_bundles.py`

FE bundle artifacts:

`artifacts/config_bundles/fe_bundle.json`

`artifacts/config_bundles/fe_bundle.json.path_proof.txt`

FE bundle tests (titles-only):

`tests/config/test_typed_bundles.py::test_two_run_identity` — asserts two-run identity for FE/BE bundles.

`tests/config/test_typed_bundles.py::test_frontend_bundle_schema_and_sources` — validates frontend bundle schema and linkage to Magic-10, band edges, and registry report.

**Notes:**  
 EPIC018 D6 introduces typed FE/BE bundles built from governed config artifacts and the registry loader; this frontend bundle subtask is now Done for the D6 slice. PF09 does not restate JSON Schema details for bundles; those remain single-homed in PF12 and the local test schemas under `docs/schemas/`.

### **Subtask HDE-CALC004.6 — Typed BE bundle**

**Subtask name/label:** Typed BE bundle

**Subtask description:**  
 Generate a typed backend config bundle under closed rails as a full projection of governed config artifacts and the registry loader, and ensure it is canonical, deterministic, and strictly linked to its sources:

Use the canonical bundle generator (titles-only; for example `python tools/config/generate_bundles.py`) under determinism env rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`) to produce a backend bundle artifact (for example `artifacts/config_bundles/be_bundle.json`).

Serialize the backend bundle via the canonical JSON emitter (`canon.sercanon`), so bundle bytes are deterministic UTF-8 JSON with sorted keys, compact separators, and exactly one trailing LF.

Ensure the backend bundle (`config_bundle.be.v1`) exposes:

Full Magic-10 config (order, caps, seeds, schema).

Full band-edges payload (schema, source pointer to `math/thresholds.json`, bands, edges, clamp, rounding, version).

Full channel objects (id, gates, centers, circuit\_primary, substream, primary\_domain, domains, flags).

Centers, domains, and alias policy as needed by backend code.

A `sources` block that records `path`, `sha256`, and `size_bytes` for each upstream governed artifact (registry report, Magic-10 config, band edges, and any other config inputs), so backend bundles are provably derived from governed config and registry artifacts.

**Subtask status:** **Done**

**Epic or card:** **EPIC-018 (D6 — Typed FE/BE bundles)**

**Tokens:**

`CONFIG_BUNDLES_DETERMINISTIC_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

Bundle generator (titles-only):

`engine/config/bundles.py`

`tools/config/generate_bundles.py`

BE bundle artifacts:

`artifacts/config_bundles/be_bundle.json`

`artifacts/config_bundles/be_bundle.json.path_proof.txt`

BE bundle tests (titles-only):

`tests/config/test_typed_bundles.py::test_two_run_identity` — asserts two-run identity for FE/BE bundles.

`tests/config/test_typed_bundles.py::test_backend_bundle_schema_and_sources` — validates backend bundle schema and linkage to governed config artifacts and registry report.

**Notes:**  
 EPIC018 D6 introduces a typed backend bundle that mirrors governed config artifacts and registry structure for backend consumers. This subtask is now Done for the D6 slice; PF09 continues to route detailed schema and semantics for bundles and their tokens to PF12 and PF19 by title.

### **Subtask HDE-CALC004.7 — Indexing & parity (Programmatic Configuration System)**

**Subtask name/label:** Indexing & parity (Programmatic Configuration System)

**Subtask description:**  
 Update the Human Index and Machine Mirror in the same PR (records-only; with path-proofs) for registry report and configuration-related artifacts, including the D5 config artifacts and acceptance map, and ensure that configuration bundles built from these artifacts are treated as governed and indexed evidence; do not list entries in PF09, and treat PF12 §8.6 as the single home for Index/Mirror schema.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D3); EPIC-018 (D5 config artifacts & acceptance map; D6 typed FE/BE bundles)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

**Index/Mirror entries for registry report:**

`artifacts/registry/registry_report.json` — governed registry report (`registry_report.v1`), with:

`docs/evidence/INDEX.json` entry (for example `artifact_key: "registry.registry_report"`, `discovered_physical_path: "artifacts/registry/registry_report.json"`), and

matching `artifacts/evidence_index.jsonl` record whose `proof_anchor` points to `artifacts/registry/registry_report.json.path_proof.txt`.

**Index/Mirror entries for D5 config artifacts:**

`artifacts/thresholds/magic10_config.json` — governed Magic-10 config (`magic10_config.v1`), with:

`artifact_key: "config.magic10"` in `docs/evidence/INDEX.json`, and

a corresponding Machine Mirror record whose `proof_anchor` points to `artifacts/thresholds/magic10_config.json.path_proof.txt`.

`artifacts/thresholds/band_edges.json` — governed band-edges config (`band_edges.v1`), with:

`artifact_key: "config.band_edges"` in `docs/evidence/INDEX.json`, and

a corresponding Machine Mirror record whose `proof_anchor` points to `artifacts/thresholds/band_edges.json.path_proof.txt`.

**Config acceptance map:**

`audit/EPIC-018_config_acceptance_map.json` — EPIC018 config acceptance map tying PF09 config tasks (HDE-CALC004, HDE-CALC004.3, HDE-CALC004.7) to artifact\_keys, tokens, and tests, with:

`artifact_key: "epic018.config.acceptance_map"` in `docs/evidence/INDEX.json`, and

a Machine Mirror record pointing to `audit/EPIC-018_config_acceptance_map.json.path_proof.txt`.

`audit/EPIC-018_config_acceptance_map.json.path_proof.txt` — path proof for the acceptance map artifact.

`tests/config/test_config_acceptance_map.py` — tests ensuring the map is canonical JSON, that PF09 task IDs and token names are whitelisted, and that every `artifact_key` exists in `docs/evidence/INDEX.json` and every listed `test_names` entry refers to a real test node.

**Index/Mirror entries for typed FE/BE bundles:**

`artifacts/config_bundles/fe_bundle.json` — typed frontend bundle (`config_bundle.fe.v1`), with:

`artifact_key` (for example `config_bundle.fe`) and `discovered_physical_path: "artifacts/config_bundles/fe_bundle.json"` in `docs/evidence/INDEX.json`,

`artifacts/config_bundles/fe_bundle.json.path_proof.txt` as the governed path-proof, and

a Machine Mirror record that includes `proof_anchor` pointing to that path-proof and records `sha256` and `size_bytes` for the FE bundle.

`artifacts/config_bundles/be_bundle.json` — typed backend bundle (`config_bundle.be.v1`), with:

`artifact_key` (for example `config_bundle.be`) and `discovered_physical_path: "artifacts/config_bundles/be_bundle.json"` in `docs/evidence/INDEX.json`,

`artifacts/config_bundles/be_bundle.json.path_proof.txt` as the governed path-proof, and

a Machine Mirror record that mirrors this entry with a `proof_anchor` to the path-proof.

**Index/Mirror core artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — Human Index and hash sentinel covering registry report, Magic-10 config, band-edges config, EPIC018 config acceptance map, and typed FE/BE bundles.

`artifacts/evidence_index.jsonl` — Machine Mirror with 1:1 records for each of the artifacts above, following canonical JSONL rules (UTF-8; sorted keys; compact; exactly one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path-proof).

**Notes:**

EPIC017 D3 closed the indexing and parity story for the `registry_report` artifact by wiring `artifacts/registry/registry_report.json` into the Evidence Index/Mirror with a governed path-proof and enforcing mirror schema and parity via CI. EPIC018 D5 extended this subtask by adding governed Magic-10 and band-edges config artifacts and the EPIC018 config acceptance map, all wired into the Evidence Index/Mirror with path-proofs and validated by acceptance-map tests.

EPIC018 D6 further extends this indexing slice by adding typed FE/BE bundles under `artifacts/config_bundles/` and ensuring they are treated as governed artifacts: both bundles are canonical JSON (UTF-8; sorted keys; compact; exactly one LF), have `sources` blocks that link back to registry and thresholds artifacts, and are listed in the Human Index and mirrored in the Machine Mirror with co-located path-proofs and canonical mirror records.

With registry report, D5 config artifacts, EPIC018 config acceptance map, and D6 typed FE/BE bundles now all present, canonical, deterministic, and fully indexed, this subtask is considered **Done** for the Programmatic Configuration System slice. Future configuration-related artifacts (beyond the registry, thresholds, acceptance map, and typed FE/BE bundles) will be introduced and governed via new epics and tasks; HDE-CALC004.7 does not remain open as a catch-all for unspecified future config families.

---

## **Task HDE-CALC005 — Deterministic Tie-Break & Total-Order Module**

**Task name/label:** Deterministic Tie-Break & Total-Order Module

**Task status:** Done

**Task ID:** HDE-CALC005

**Task description:**  
 Provide ASCII-based comparators and helpers that impose deterministic, locale-free total order over IDs, centers, channels, and categories, and prove comparator properties with property tests and ABBA/two-run identity checks; ensure canonicalization respects arrays-as-sets semantics and is backed by ordering evidence families.

**Task notes:**

**Status lock (HDE-EPIC006 — Mechanics Foundations):** PF09 Phase-I “Deterministic tie-break & total-order module — Implement” is satisfied under **HDE-EPIC006**, which closed tie-break/total-order, comparators, invariance, and `/internal/version` HEAD/conditionals remediation for this module. This row is now history-only; any new comparator or ordering work is tracked in downstream epics and global-discipline tasks.

Audit (v1 — 2025-11-17) originally flagged missing `JSON_CANONICAL_CHECK_OK` / `TWO_RUN_IDENTITY_OK` tokens and the absence of comparator proofs and sorted ordering snapshots.

EPIC017 PR04 (WS-D4) introduced the **ordering layer** and hardened much of the **evidence plumbing** for this module:

A dedicated `engine/order` package now provides comparators and helpers for IDs, channels, categories, and arrays-as-sets.

`tools/order/generate_ordering_artifacts.py` is the **single writer** for ordering artifacts under `artifacts/engine/order/**`, generating:

`channels_sorted.snapshot.json`

`categories_iter.snapshot.json`

`props_total_order.log`

`abba_identity.bytes`

Ordering artifacts support a `--check` mode for two-run identity, and new tests (`tests/order/test_total_order_properties.py`, `tests/order/test_ordering_artifacts_stability.py`) cover total-order properties and artifact stability / ABBA parity.

`tools/evidence/update_evidence_index.py` is the **sole writer** for `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and governed `*.path_proof.txt`, and `ci/checks/check_mirror_schema.sh` enforces mirror schema and self-record rules as part of the evidence skeleton.

WS-D4b (EPIC017 PR04r) completed the **evidence remediation** for this task:

Finalized `mtime_utc` semantics for governed path-proofs as **refresh-time mtime** (UTC ISO-8601, truncated to seconds, microsecond==0, monotone `<= stat().st_mtime` at check time), aligned with PF12/PF19.

Regenerated all governed `*.path_proof.txt` to the `{path, size_bytes, sha256, mtime_utc, produced_at_utc}` schema and refreshed `artifacts/evidence_index.jsonl` so the Machine Mirror self-record and its proof match the body hash and file size.

Regenerated `artifacts/engine/order/abba_identity.bytes` via `tools/order/generate_ordering_artifacts.py` so its on-disk bytes, Mirror record, and path-proof all agree on a 32-byte artifact and canonical SHA, resolving the earlier ABBA mismatch.

Tracked issue posture (EPIC022): if any `abba_identity.bytes` (or other governed ordering artifact) is observed to have bytes/path-proof/mirror drift again, record the issue as deferred in the acceptance artifacts and do not claim ordering-evidence acceptance for that slice until the mismatch is re-verified and repaired.

Updated `tools/evidence/update_evidence_index.py`, `ci/checks/check_mirror_schema.sh`, and the evidence tests (`tests/evidence/test_evidence_skeleton.py`, `tests/ops/test_evidence_index.py`) to enforce the same `mtime_utc` semantics (format \+ monotone vs `stat()`), so mirror schema and evidence skeleton checks now pass under rails-closed CI.

As a result, WS-D4 tokens that depend on ordering math and generator ownership **and** on the hardened evidence skeleton (for example `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`, `ORDERING_ARTIFACTS_DETERMINISTIC_OK`, `EVIDENCE_PATH_PROOFS_OK`, `EVIDENCE_PATH_PROOFS_SHAPE_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`) are now **green** under the standard rails-closed CI pipeline. All subtasks HDE-CALC005.1–HDE-CALC005.6 are treated as Done for this Phase-I module; remaining ordering usage is enforced by higher-level “global discipline” tasks.

---

### **Subtask HDE-CALC005.1 — ASCII comparators**

**Subtask name/label:** ASCII domain comparators

**Subtask description:**  
 Implement ASCII comparators for:

IDs and centers (string-based)

channels (`NN–NN` min-first, zero-padded)

categories (frozen Magic-10 rank → ASCII)

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC006 (Mechanics Foundations); EPIC-017 (D4)**

**Tokens:** **Unknown**

**Evidence / artifacts:**

`order/channels_sorted`, `order/categories_iter` evidence families (see below).

---

### **Subtask HDE-CALC005.2 — Helpers for ordering**

**Subtask name/label:** Ordering helpers

**Subtask description:**  
 Provide helpers: `dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`, and require their use at all ordered emission sites (composites, categories, evidence).

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC006 (Mechanics Foundations); EPIC-017 (D4)**

**Tokens:** **Unknown**

**Evidence / artifacts:**

`order/props_total_order`, `canonical/json_compare` families; canonical JSON compare logs.

---

### **Subtask HDE-CALC005.3 — Property tests & ordering proofs**

**Subtask name/label:** Comparator property tests & ordering proofs

**Subtask description:**  
 Add property tests for antisymmetry, transitivity, and totality; prove channel order (min-first `NN–NN`) and category iteration loop equals the frozen order.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D4)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK` (once ordering effects are verified by byte compare)

**Evidence / artifacts:**

`order/props_total_order`

`order/channels_sorted`

`order/categories_iter`

**Notes:**  
 Comparator property tests and ordering snapshots are now driven by the EPIC017 ordering layer, run under the standard rails-closed CI pipeline, and wired into the EPIC017 D4 acceptance map; `JSON_CANONICAL_CHECK_OK` and `TWO_RUN_IDENTITY_OK` are satisfied via these artifacts.

---

### **Subtask HDE-CALC005.4 — Determinism checks**

**Subtask name/label:** AB↔BA & two-run identity checks

**Subtask description:**  
 Add AB↔BA and two-run identity checks for outputs produced under these comparators; canonical re-serialization byte-compare under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D1)** *(harness artifacts referenced)*

**Tokens:**

`TWO_RUN_IDENTITY_OK`

`COMPOSITE_ABBA_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/cli/ab.json`

`artifacts/cli/ba.json`

`artifacts/cli/summary.json`

`artifacts/cli/reader_dump.json`

`artifacts/cli/reader_cli_parity.bytes`

`artifacts/cli/preimage_recompute.log`

---

### **Subtask HDE-CALC005.5 — Canonical JSON & serializer determinism evidence**

**Subtask name/label:** Serializer determinism & canonical JSON evidence

**Subtask description:**  
 Provide tests and logs that prove serializer determinism and canonical JSON under these comparator policies.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D1)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

`tests/test_emitter_determinism.py`

`audit/gates/canonical_json/json_canonical_check.log`

`audit/gates/canonical_json/json_canon_compare.log`

`artifacts/cli/guards/serializer_grep_guard.log`

`artifacts/cli/guards/emitter_symbol_proof.txt`

**Notes:**  
 These artifacts run under rails-closed CI (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and are indexed with path-proofs. They now fully satisfy the `JSON_CANONICAL_CHECK_OK` acceptance token as recorded in the EPIC017 manifest and acceptance map.

---

### **Subtask HDE-CALC005.6 — Ordering & comparator evidence families**

**Subtask name/label:** Ordering & comparator evidence families

**Subtask description:**  
 Track ordering evidence families for the tie-break module and ensure they are generated by a single tool, are deterministic under pinned environment settings, and are indexed in the Evidence Index and mirrored 1:1 in the Machine Mirror in the same PR:

**Generator-owned ordering artifacts.**

`tools/order/generate_ordering_artifacts.py` is the **single writer** for ordering artifacts under `artifacts/engine/order/**`.

The governed ordering artifacts are:

`artifacts/engine/order/channels_sorted.snapshot.json` — channel ordering snapshot.

`artifacts/engine/order/categories_iter.snapshot.json` — Magic-10 category loop order.

`artifacts/engine/order/props_total_order.log` — comparator property-test proofs (antisymmetry, transitivity, totality).

`artifacts/engine/order/abba_identity.bytes` — AB↔BA byte-equality evidence for comparator outputs.

**Deterministic runs.**

The ordering generator MUST support a `--check` (or equivalent) mode and be deterministic under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; two successive runs with the same inputs produce byte-identical ordering artifacts (`ORDERING_ARTIFACTS_DETERMINISTIC_OK`).

**Index/Mirror & proofs.**

On each run, the generator (together with the evidence tools) rewrites the Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`), Machine Mirror (`artifacts/evidence_index.jsonl`), and associated `.path_proof.txt` files so that ordering artifacts, Index, mirror, and proofs move in lockstep.

Mirror records for the ordering artifacts follow PF12 mirror schema (fixed field set/order), include `proof_anchor` pointing to each ordering artifact’s path-proof transcript, and are validated (alongside proofs) by `ci/checks/check_mirror_schema.sh`.

PF09 does not define ordering schemas or comparator math; those remain single-homed in HDE-Math-Spec and HDE-Schemas & Artifacts. This subtask ensures that ordering artifacts and their evidence plumbing are generator-owned, deterministic, and fully integrated into the Evidence Index/Mirror system.

**Subtask status:** **Done**

**Epic or card:** **EPIC-017 (D4, WS-D4b — Evidence mtime re-alignment)**

**Tokens:**

`ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`

`ORDERING_ARTIFACTS_DETERMINISTIC_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`EVIDENCE_PATH_PROOFS_SHAPE_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

**Evidence / artifacts (titles-only; PF09 is consumer-only):**

**Generator & tools:**

`engine/order/__init__.py`, `engine/order/comparators.py`, `engine/order/artifacts.py` (or equivalent ordering modules).

`tools/order/generate_ordering_artifacts.py` — generator for ordering artifacts (write \+ `--check` modes).

`tools/evidence/update_evidence_index.py` — single writer for Index, sentinel, mirror, and governed path-proofs.

`tools/evidence/orientation_demo.py` — topology orientation demo and consistency checks.

`ci/checks/check_mirror_schema.sh` — mirror schema & path-proof shape/monotonicity check.

**Ordering artifacts (governed, generator-owned):**

`artifacts/engine/order/channels_sorted.snapshot.json`

`artifacts/engine/order/categories_iter.snapshot.json`

`artifacts/engine/order/props_total_order.log`

`artifacts/engine/order/abba_identity.bytes`

**Index/Mirror/Proofs:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

`artifacts/engine/order/channels_sorted.snapshot.json.path_proof.txt`

`artifacts/engine/order/categories_iter.snapshot.json.path_proof.txt`

`artifacts/engine/order/props_total_order.log.path_proof.txt`

`artifacts/engine/order/abba_identity.bytes.path_proof.txt`

**Tests:**

`tests/order/test_total_order_properties.py` — total-order property tests.

`tests/order/test_ordering_artifacts_stability.py` — ordering artifact stability / ABBA parity tests.

`tests/evidence/test_evidence_skeleton.py` — evidence skeleton & proof checks (now green for `mtime_utc` format/monotone semantics and path-proof shape).

`tests/ops/test_evidence_index.py` — Index/mirror consistency tests (now green for `mtime_utc` semantics).

**Notes:**

Common failure mode (merge-blocking): governed artifact drift. Never assume artifact sizes or hashes; do not hand-edit `*.path_proof.txt`. If a governed artifact’s on-disk bytes disagree with its path-proof and/or Machine Mirror record (`sha256` / `size_bytes`), treat it as a hard stop and regenerate proofs/records via `tools/evidence/update_evidence_index.py` (then rerun `tools/evidence/update_evidence_index.py --check`).

WS-D4 established the ordering layer, generator, and initial evidence plumbing. WS-D4b finalized the `mtime_utc` semantics for governed path-proofs (refresh-time, monotone, UTC ISO) and regenerated ABBA and path-proof artifacts so that artifact bytes, Mirror records, and `*.path_proof.txt` contents all agree.

Under the standard rails-closed CI pipeline (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), the ordering evidence families and their Index/Mirror wiring now satisfy all of the tokens listed above, including `CI_CHECK_MIRROR_SCHEMA_OK` and `EVIDENCE_PATH_PROOFS_SHAPE_OK`.

Further ordering-related work (for example, wiring comparators into all surfaces and the global discipline tasks) is tracked in other subtasks and tasks; this subtask specifically is considered **Done** for EPIC017 D4/D4b.

# **Phase II — Dissolution (Normalize and make it pure)**

**Phase description:** Normalize and validate all inputs, enforce canonical behavior for the sampler/ranker, engine core, band thresholds, and the internal category framework, using the deterministic primitives and evidence skeleton established in Phase I.

**Phase master status:** **Partial**

**Notes:**

* PF09 is consumer-only for Phase II behavior; math, schemas, governance tokens, and HTTP contracts for these components live in HDE-Math-Spec, HDE-Schemas & Artifacts, HDE-Governance, HDE-CLI-API-Vendor-Ref, and HDE-Mechanics Guide by title only.

* Several Phase II tasks (HDE-DISS001, HDE-DISS002, HDE-DISS004, HDE-DISS005, HDE-DISS006) are Done, while HDE-DISS003 remains Partial because diversity/window/recent constraints and related sampler discipline are still outstanding; the phase master status reflects this mix of Done and Partial work.


---

## Task HDE-DISS001 — Input Normalization & Validation Layer

**Task ID:** HDE-DISS001

**Task name/label:** Input Normalization & Validation Layer

**Task status:** **Done**

**Task description:**  
 Normalize IDs and viewer\_prefs, enforce schema-based validation, and guarantee canonical JSON forms and AB↔BA neutrality for normalized inputs, with hard-fail behavior for unknown IDs and invalid shapes.

**Task notes:**

IDs normalize via declared alias ledgers when normalization is enabled; otherwise, unknown IDs are rejected.

viewer\_prefs must satisfy:

`top_category ∈ Magic-10`, and

`weights` contains all ten Magic-10 keys with integer values 0..100 (no floats).

Zero-weight rule is enforced downstream by the sampler/ranker (PF14 §11, titles-only).

Normalized forms are re-serialized to canonical JSON:

UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF.

Arrays-as-sets deduped and ASCII-sorted.

Normalization is AB↔BA neutral: normalized JSON for (A,B) is byte-identical to (B,A).

**Task-level tokens (titles-only):**

`UNKNOWN_IDS_FAIL_CLOSED_OK`

`ALIAS_NORMALIZATION_OK` (when enabled)

`PREFS_KEYSET_10_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

### Subtask HDE-DISS001.1 — ID normalization & alias policy

**Subtask name/label:** ID normalization & alias policy

**Subtask description:**  
 Normalize IDs via declared alias ledgers when normalization is enabled; otherwise, reject unknown IDs with a typed error.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`UNKNOWN_IDS_FAIL_CLOSED_OK`

`ALIAS_NORMALIZATION_OK` (when enabled)

**Evidence / artifacts:**

Invalid shapes/IDs: service-side typed error tests (`invalid_prefs`, `invalid_json`)

Normalization snapshots and canonical-compare logs

**Notes:**  
 Behavior is governed by canon (PF14/PF12); PF09 records that the implementation enforces this.

### Subtask HDE-DISS001.2 — viewer\_prefs shape & keyset

**Subtask name/label:** viewer\_prefs validation

**Subtask description:**  
 Enforce that `viewer_prefs.top_category ∈ Magic-10` and `viewer_prefs.weights` contains exactly all ten Magic-10 keys with integer values 0..100 (no floats).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`PREFS_KEYSET_10_OK`

`UNKNOWN_IDS_FAIL_CLOSED_OK` (for bad IDs)

**Evidence / artifacts:**

Service-side typed error tests for `invalid_prefs` and `invalid_json`

**Notes:**  
 Zero-weight semantics are enforced in the sampler/ranker, not here.

### Subtask HDE-DISS001.3 — Zero-weight rule handoff

**Subtask name/label:** Zero-weight rule handoff to sampler/ranker

**Subtask description:**  
 Ensure that viewer\_prefs normalization preserves weight=0 semantics and that enforcement of “exclude candidates whose \#1 equals a 0-weight category” is delegated to the sampler/ranker.

**Subtask status:** **Done (SoT-level behavior; enforced downstream)**

**Epic or card:** **Unknown**

**Tokens:**

`TWO_RUN_IDENTITY_OK` (end-to-end identity relies on consistent handoff)

**Evidence / artifacts:**

Referenced sampler/ranker evidence families (see HDE-DISS003).

**Notes:**  
 This subtask is mainly a contract boundary: PF09 marks that enforcement happens downstream, not in the normalization layer.

### Subtask HDE-DISS001.4 — Canonical JSON normalization & ABBA

**Subtask name/label:** Canonical JSON & AB↔BA neutrality

**Subtask description:**  
 Re-serialize normalized inputs to canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays-as-sets are deduped and ASCII-sorted. Normalization must be AB↔BA neutral: (A,B) and (B,A) normalize to byte-identical JSON.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`tests/test_emitter/test_emitter_determinism.py` — success parity (CLI vs service)

Normalization snapshots and canonical-compare logs

**Notes:**  
 Shares canonicalization infrastructure with the Canonical Serialization Package from Phase I.

### Subtask HDE-DISS001.5 — Schema validation CI job

**Subtask name/label:** JSON-Schema validation CI job

**Subtask description:**  
 Maintain a JSON-Schema validation CI job that is present and passing for all governed input shapes (IDs, prefs, and other catalog-bound payloads); use an allowed JSON-Schema validator (e.g. AJV or equivalent); any schema drift or unknown field must fail the job.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`UNKNOWN_IDS_FAIL_CLOSED_OK` (unknown fields/IDs must fail)

`JSON_CANONICAL_CHECK_OK` (canonical lints shared across inputs)

**Evidence / artifacts:**

CI job configuration and logs (tool names/paths not pinned in PF09)

**Notes:**  
 PF09 does not pin tool names/paths; schemas and validator behavior are single-homed in HDE-Schemas & Artifacts and HDE-Mechanics Guide.

### Subtask HDE-DISS001.6 — Evidence coverage (normalization)

**Subtask name/label:** Normalization & validation evidence coverage

**Subtask description:**  
 Maintain evidence for normalization and validation behavior, including success parity, invalid shapes/IDs, and canonicalization logs, and index them under the global Evidence Index & mirror discipline.

**Subtask status:** **Done** (for the named artifacts)

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts (titles/paths only):**

`tests/test_emitter/test_emitter_determinism.py`

Service-side typed error tests (`invalid_prefs`, `invalid_json`)

Normalization snapshots & canonical-compare logs

**Notes:**  
 Indexing details follow the generic Evidence Index section; PF09 does not restate mirror schema here.

---

## Task HDE-DISS002 — Compatibility Engine (pair)

**Task ID:** HDE-DISS002

**Task name/label:** Compatibility Engine (pair)

**Task status:** **Done**

**Task description:**  
 Compute per-category integer scores and bands, select narrative keys, and emit ten categories in frozen Magic-10 order for a pair (a,b), with AB↔BA parity and canonical JSON behavior, using per-channel semantics and strict input typing.

**Task notes:**

Scope includes:

Per-category score (0..100) and band mapping via inclusive-high edges (e.g. 24/49/74/100) using `round_half_up`.

Selection of `personal_key` / `shared_key`.

Emission of 10 categories in frozen Magic-10 order (HDE-Schemas & Artifacts §2.6; HDE-Math-Spec §5.1).

Per-channel semantics:

Each channel is a canonical `NN-NN` edge (min-first, zero-padded).

Record compromise direction \+ gate.

Integration {10, 20, 34, 57} channels are independent and MUST be validated for AB↔BA parity.

Inputs:

`a`, `b` each: an ID or a full person payload (Reader schema).

Must not mix ID vs payload for the same party (mixed shape ⇒ `invalid_json`).

**Task-level tokens (titles-only):**

`JSON_CANONICAL_CHECK_OK`

`AB_BA_PARITY_OK` (including Integration cases)

`TWO_RUN_IDENTITY_OK`

### Subtask HDE-DISS002.1 — Per-category scoring & banding

**Subtask name/label:** Per-category scoring & band thresholds

**Subtask description:**  
 Compute per-category integer scores (0..100) and map each to a band using inclusive-high thresholds (e.g. 24/49/74/100) with `round_half_up`, consistent with PF-Math.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

Implied via compat identity hash (`artifacts/compat/identity_hash.txt`) and AB↔BA logs.

### Subtask HDE-DISS002.2 — Narrative key selection

**Subtask name/label:** Narrative key selection (10×2 table)

**Subtask description:**  
 Select `{personal_key, shared_key}` per category from governed narrative key ledgers, emitting ten categories in frozen Magic-10 order.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

`artifacts/narratives/key_table_10x2.snapshot.json` — 10×2 narrative key table

### Subtask HDE-DISS002.3 — Per-channel semantics & Integration ABBA

**Subtask name/label:** Per-channel semantics & Integration parity

**Subtask description:**  
 Treat each channel as canonical `NN-NN` (min-first, zero-padded), recording compromise direction \+ gate. Integration channels {10, 20, 34, 57} are independent and must be validated for AB↔BA parity.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`AB_BA_PARITY_OK` (including Integration cases)

**Evidence / artifacts:**

AB↔BA parity logs, including Integration channel pairs (e.g. 20-34 vs 20-57).

### Subtask HDE-DISS002.4 — Input typing & error semantics

**Subtask name/label:** Input typing & `invalid_json` enforcement

**Subtask description:**  
 For inputs `a` and `b`, ensure each is either an ID or a full person payload (Reader schema); do not mix ID vs payload for the same party; mixed shape must produce `invalid_json`.

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK` (error envelopes follow canonical JSON)

**Evidence / artifacts:**

Service-side typed error tests for `invalid_json` in compat flows.

### Subtask HDE-DISS002.5 — Canonical JSON & identity hash

**Subtask name/label:** Canonical JSON & compat identity hash

**Subtask description:**  
 Ensure compat output is canonical JSON (UTF-8/no BOM; sorted keys; compact; one LF; arrays-as-sets deduped & ASCII-sorted) and compute an `identity_hash` (sha256 of LF-terminated compat body).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/compat/identity_hash.txt` — sha256 of LF-terminated compat body

### Subtask HDE-DISS002.6 — Evidence & indexing (compat)

**Subtask name/label:** Compatibility Engine evidence & indexing

**Subtask description:**  
 Maintain compat evidence (narrative key table, compat identity hash, AB↔BA logs) and index them in the Evidence Index and Machine Mirror with path-proofs, per global Evidence Index discipline.

**Subtask status:** **Done** (for named artifacts)

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts (titles/paths only):**

`artifacts/narratives/key_table_10x2.snapshot.json`

`artifacts/compat/identity_hash.txt`

AB↔BA parity logs for compat (Integration channels included)

## **Task HDE-DISS003 — Swipe Sampler & Ranker**

**Task ID:** HDE-DISS003

**Task name/label:** Swipe Sampler & Ranker

**Task status:** **Partial**

**Task description:**  
 Build a deterministic swipe sampler/ranker that enforces the zero-weight rule, diversity constraints, deterministic scoring and ranking, optional seedability in dev/admin flows, and provides a dev-only sampling endpoint, with canonical JSON outputs and evidence integrated into the Evidence Index/Mirror.

**Task notes:**

Audit (v1 — 2025-11-17) originally reported that zero-weight enforcement, diversity checks, and sampler/ranker evidence were only specified in canon and not yet wired into a real engine harness.

**EPIC019 PR02 (D1 — “Sampler/ranker deterministic pool and scoring”)** introduces a pure-compute sampler core in `engine/sampler/core.py`, exported via `engine/sampler/__init__.py`, plus unit tests in `tests/unit/test_sampler_core.py`. The core:

Excludes zero-weight candidates from the pool (weight ≤ 0).

Applies basic eligibility rules based on compat score and band filters.

Ranks candidates deterministically using a fixed comparator that prefers higher weight, higher compat score, better band priority, and then uses `engine.order.comparators.compare_ids` as a final ASCII tie-breaker.

Includes an AB/BA sanity test that confirms that, for two mirrored viewer perspectives, the higher-compat counterpart is consistently ranked first and that top scores match across perspectives.

**EPIC019 PR03 (D2 — “Seedable dev/admin sampler flows”)** adds a dev/admin-only CLI harness `dev:sampler` to `hdctl` (implemented in `engine/cli/main.py` with tests in `tests/cli/test_dev_sampler_cli.py`):

Registers a `dev:sampler` subcommand with help text clearly marked “DEV/ADMIN ONLY: deterministic sampler harness (seedable).”

Gates the command by `APP_ENV`, allowing execution only when `APP_ENV ∈ {dev, test, local}` and raising a typed `CliError("DEV_ADMIN_ONLY")` otherwise.

Reads a JSON candidates file via existing CLI file helpers, normalizes payloads into `CandidateFeatures`, constructs a `ViewerProfile` from the `--viewer` argument, and calls the pure-compute sampler core (`sample_and_rank`) to obtain ranked candidates.

Emits canonical JSON to stdout via the shared serializer (`sercanon`), with a payload containing `viewer_id`, `seed` (echoed from CLI), and a `candidates` array, under closed determinism env pins.

Provides CLI tests that prove **two-run identity** and **seed-only impact** for the harness.

**EPIC019 PR04 (D3 — “Dev-only sampler HTTP endpoint harness”)** adds a dev/admin-only HTTP sampler harness at `POST /internal/dev/sampler` (implemented in `adapter/http_reader.py` with tests in `tests/adapter/test_dev_sampler_http.py`):

Registers `POST /internal/dev/sampler` as an internal, non-public route.

Uses a tightened `_dev_admin_gate` that permits only explicit `APP_ENV ∈ {dev, test, local}` and returns writer-style 403 forbidden envelopes for `APP_ENV="prod"`, missing `APP_ENV`, or empty `APP_ENV`.

Reads JSON bodies (`viewer_id`, `candidate_ids`, optional `seed`), validates shapes, builds `ViewerProfile` and `CandidateFeatures` from IDs, calls the sampler core, and returns IDs-only plus `meta.seed` in canonical JSON.

Adapter tests verify determinism, seed-only differences, and gating behavior.

**EPIC019 PR05 (D4 — “Sampler evidence & indexing”) and its bugfix** complete the sampler evidence and indexing slice by:

Introducing five governed sampler evidence families under `artifacts/sampler/**` (pool snapshots, two-run identity logs, ABBA logs, diversity artifacts, seed replay logs) with corresponding schemas under `docs/schemas/sampler/**`, all generated under closed rails and emitted as canonical JSON.

Extending `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` to include sampler evidence families, with path-proofs and canonical JSONL records following PF12’s field set/order and sort-before-write rules.

Adding sampler evidence tests (for example `tests/evidence/test_sampler_evidence.py`) that validate sampler artifacts against their schemas, assert Human Index entries and sentinel correctness, and verify that Mirror records and path-proofs exist and are shaped correctly.

Correcting a provenance bug in sampler Mirror records and path-proofs by updating `produced_at_utc` for sampler families and their schemas to reflect the actual evidence refresh time (e.g., `2025-11-30T03:58:47Z`) and regenerating path-proofs so `produced_at_utc` matches across artifact, path-proof, and Mirror, restoring PF12/PF14 provenance semantics.

As a result, HDE-DISS003 now has the following subtask posture:

**HDE-DISS003.1** (“Zero-weight enforcement in candidate pool”) — **Done** via EPIC019 PR02.

**HDE-DISS003.2** (“Pool formation & eligibility filters”) — **Done**: Sampler deterministic pool formation and diversity constraints are implemented and evidenced via sampler artifacts (pool snapshot baseline, diversity requirements, two-run identity).

**HDE-DISS003.3** (“Deterministic scoring & total order”) — **Done** via EPIC019 PR02.

**HDE-DISS003.4** (“Seedable dev/admin sampling”) — **Done** via EPIC019 PR03 (dev-only CLI harness).

**HDE-DISS003.5** (“Sampler endpoint harness”) — **Done** via EPIC019 PR04 (dev-only HTTP sampler harness).

**HDE-DISS003.6** (“Evidence & indexing (sampler/ranker)”) — **Done** via EPIC019 PR05 and its bugfix: sampler evidence families under `artifacts/sampler/**` with schemas under `docs/schemas/sampler/**` are generated under closed rails, validated against their schemas, and fully integrated into the Evidence Index/Mirror with path-proofs and provenance-correct `produced_at_utc`.

**Task-level tokens (titles-only):**

Determinism & parity: `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`

Canonical JSON & evidence: `JSON_CANONICAL_CHECK_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`

---

### **Subtask HDE-DISS003.1 — Zero-weight enforcement in candidate pool**

**Subtask name/label:** Zero-weight enforcement in candidate pool

**Subtask description:**  
 Enforce the zero-weight rule when forming the candidate pool: exclude any candidate whose effective weight corresponds to a viewer weight of 0 (or below) so that zero-weight candidates never enter the ranked pool.

**Subtask status:** **Done**

**Epic or card:** **EPIC-019 (D1 — sampler/ranker deterministic pool and scoring)**

**Tokens:**

`TWO_RUN_IDENTITY_OK` (end-to-end determinism depends on deterministic exclusion)

**Evidence / artifacts:**

**Sampler core implementation (titles-only):**

`engine/sampler/core.py` — pure-compute sampler core implementing zero-weight exclusion, pool formation, and deterministic ranking over in-memory dataclasses (no I/O, no clocks, no env/global state).

`engine/sampler/__init__.py` — exports for sampler types and functions (for example `build_candidate_pool`, `rank_candidates`, `sample_and_rank`) for reuse by later CLI/HTTP harnesses.

**Unit tests (titles-only):**

`tests/unit/test_sampler_core.py::test_zero_weight_candidates_are_excluded` — constructs a small candidate set including a zero-weight candidate and asserts that the candidate pool excludes zero-weight candidates and retains only positive-weight entries.

`tests/unit/test_sampler_core.py::test_rank_candidates_is_deterministic` — verifies that ranking is deterministic across repeated runs, with the same candidate ordering for identical inputs.

`tests/unit/test_sampler_core.py::test_ab_ba_parity_respects_total_order` — AB/BA sanity test showing that the higher-compat counterpart is consistently ranked first for mirrored viewer perspectives and that the top-ranked candidate’s score matches across those perspectives.

**Notes:**

EPIC019 PR02 implements the zero-weight rule at the engine layer via the sampler core: candidates with weight ≤ 0 are discarded before any band/eligibility checks, so they never appear in the candidate pool or final ranking. This is stricter than the minimal zero-weight rule handoff described in HDE-DISS001 and is consistent with PF-canon’s intent that 0-weight categories produce no candidates.

The zero-weight enforcement here is **pure compute** and is currently exercised only by engine-level unit tests; there is no CLI/HTTP harness or Evidence Index/Mirror wiring yet for sampler outputs. Those will be added in later EPIC019 deliverables and reflected in higher-phase sampler evidence subtasks (HDE-DISS003.6, Conjunction/Distillation tasks).

### **Subtask HDE-DISS003.2 — Pool formation & eligibility filters**

**Subtask name/label:** pool formation & eligibility filters

**Subtask description:**  
 Implement deterministic pool formation, eligibility filtering, and diversity constraints:

* Candidate pool is built deterministically from the Registry.

* Apply viewer eligibility filters (e.g., hide filtered, hide placeholder, hide flagged).

* Enforce diversity constraints before ranking: no more than N from same group inside window K, and enforce “recent R” rule.

* Produce governed evidence artifacts capturing pool snapshot and constraint checks.

**Subtask status:** **Done**

**Epic or card:** EPIC-019 (D1, PR02)

**Tokens:**  
 `SAMPLER_POOL_DETERMINISTIC_OK`  
 `SAMPLER_POOL_DIVERSITY_OK`  
 `TWO_RUN_IDENTITY_OK`

**Sampler core implementation:**

* `engine/sampler/core.py::build_candidate_pool(registry, config)`

* `engine/sampler/core.py::apply_eligibility_filters(items, config)`

* `engine/sampler/core.py::check_diversity_constraints(items, config)`

* Diversity/window/recent constraints are enforced and captured in governed evidence artifacts (see Evidence / artifacts).

**Evidence / artifacts:**

* Core sampler tests:

  * `tests/unit/test_sampler_core.py` (eligibility rules)

* Sampler evidence artifacts:

  * `artifacts/sampler/pool_snapshots/baseline.json`

  * `artifacts/sampler/pool_snapshots/baseline.json.sha256`

  * `artifacts/sampler/diversity/diversity_requirements.json`

  * `artifacts/sampler/two_run/identity.json`

**Producer tool (evidence generator):**  
 `tools/evidence/generate_sampler_evidence.py`

**Notes:**  
 Codex Audit HDE-EPIC024 reports sampler pool formation and diversity constraints are implemented and evidenced by the sampler artifact family under `artifacts/sampler/`; this closes the previously noted gap for this subtask.

### **Subtask HDE-DISS003.3 — Deterministic scoring & total order**

**Subtask name/label:** Deterministic scoring & total order

**Subtask description:**  
 Use a deterministic fixed-point score function across the ten categories (integer path); sort candidates by score in the specified direction, then break ties using the ID comparator to guarantee a stable total order.

**Subtask status:** **Done**

**Epic or card:** **EPIC-019 (D1 — sampler/ranker deterministic pool and scoring)**

**Tokens:**

`COMPOSITE_ABBA_IDENTITY_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

**Sampler core implementation (titles-only):**

`engine/sampler/core.py` — implements:

`_band_priority_map` and `_band_rank` to derive band priorities from the compat BANDS order (default `Glow > Warm > Open > Cool` via reversed BANDS).

`_compare_entries(a, b, cfg)` which compares `CandidatePoolEntry` values by:

Higher `weight` first.

Higher `compat_score` next.

Better band (higher band priority) next.

Finally, `engine.order.comparators.compare_ids(a.person_uid, b.person_uid)` as a stable ASCII tie-breaker.

`rank_candidates(config, pool)` which uses `sorted(<entries>, key=cmp_to_key(lambda a, b: _compare_entries(a, b, cfg)))` to impose a total order and returns `RankedCandidates`.

`sample_and_rank(config, candidates)` convenience wrapper that builds the candidate pool and returns ranked candidates, maintaining determinism across repeated runs.

**Unit tests (titles-only):**

`tests/unit/test_sampler_core.py::test_rank_candidates_is_deterministic` — constructs a set of candidates, runs `sample_and_rank` twice (using a deep copy of the inputs), and asserts that:

The two `RankedCandidates` results are equal.

The candidate ordering matches expectations based on weight and compat score, demonstrating deterministic total order.

`tests/unit/test_sampler_core.py::test_ab_ba_parity_respects_total_order` — AB/BA sanity test covering the sampler core:

Defines two viewer profiles and candidate sets such that, for each viewer, the counterpart with higher compat score should be ranked first.

Asserts that for viewer A and viewer B, the higher-compat counterpart is consistently the top-ranked candidate and that the top candidate’s score matches across both perspectives.

Confirms that the comparator \+ total-order logic is coherent with compat math and AB/BA neutrality expectations at D1.

**Notes:**

EPIC019 PR02 implements deterministic scoring and ranking as a pure-compute module, with no I/O, env reads, or global state. The comparator is fully specified and uses existing ordering utilities (`compare_ids`) to guarantee a stable total order that is independent of Python dict/set iteration or DB row ordering.

The D1 tests provide strong assurances about determinism (two-run identity) and AB/BA coherence for the sampler core itself. They do **not yet** produce sampler evidence artifacts or canonical JSON snapshots; those will be added by later PRs that wire the sampler into CLI/HTTP surfaces and Evidence Index/Mirror (HDE-DISS003.6 and Distillation harnesses).

With this implementation and test coverage in place, HDE-DISS003.3 is considered **Done** for the engine-layer total-order requirement; higher-phase work will reuse this core rather than re-implementing scoring logic.

### **Subtask HDE-DISS003.4 — Seedability (dev/admin only)**

**Subtask name/label:** Seedable dev/admin sampling

**Subtask description:**  
 For non-public flows, accept an optional seed input; with the same inputs and seed, sampler outputs must be byte-identical. Seed use must not alter public bytes.

**Subtask status:** **Done**

**Epic or card:** **EPIC-019 (D2 — Seedable dev/admin sampler flows)**

**Tokens:**

`TWO_RUN_IDENTITY_OK` (two-run identity for seedable dev/admin harness)

**Evidence / artifacts:**

**CLI harness implementation (titles-only):**

`engine/cli/main.py` — adds the `dev:sampler` subcommand and helper functions:

`_ensure_dev_admin_env()` — reads `APP_ENV` and restricts `dev:sampler` to `APP_ENV ∈ {dev, test, local}`, raising a typed `CliError("DEV_ADMIN_ONLY")` otherwise.

Parser wiring: registers `dev:sampler` with help text such as “DEV/ADMIN ONLY: deterministic sampler harness (seedable)” and arguments `--viewer`, `--candidates-file`, and optional `--seed`.

`_normalize_categories` and `_candidate_from_payload` — validate and normalize candidate payloads (IDs, bands, weights, compat scores, diversity keys) into `CandidateFeatures`, raising typed `CliError` codes on invalid shapes or types.

`_load_candidates_from_path` — reads the JSON candidates file using existing `hdctl` file helpers, accepting either a list of candidate records or a mapping with a `candidates` list, and converts to a list of `CandidateFeatures`.

`dev_sampler_run(args, env)` — orchestrates the harness:

Ensures dev/admin environment via `_ensure_dev_admin_env`.

Builds a `ViewerProfile` from `args.viewer`.

Loads and normalizes candidates from `args.candidates_file`.

Calls `engine.sampler.core.sample_and_rank(viewer_profile, candidates)` to obtain a `RankedCandidates` result.

Passes the result and `args.seed` to `_emit_sampler_output` for canonical JSON emission.

`_emit_sampler_output(viewer_id, seed, ranked_candidates)` — builds a payload `{viewer_id, seed, candidates:[<candidates>]}` and writes it using the canonical serializer (`sercanon`) to `stdout` as deterministic JSON (UTF-8, sorted keys, compact, exactly one trailing LF).

`engine/sampler/__init__.py` — exports `sample_and_rank` and related types so the CLI harness calls the pure-compute sampler core rather than re-implementing logic.

**CLI tests (titles-only):**

`tests/cli/test_dev_sampler_cli.py::test_dev_sampler_two_run_identity` — under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` with `APP_ENV=dev`), runs `python -m engine.cli dev:sampler --viewer <id> --candidates-file <path> --seed 111` twice on the same candidates file and asserts:

Both runs exit with code 0\.

`stdout` bytes are identical across runs.

Parsed JSON payloads have the same `viewer_id` and `seed` "111" and the same `candidates` array (order and fields).

`tests/cli/test_dev_sampler_cli.py::test_dev_sampler_seed_echo_changes_only_seed` — runs `dev:sampler` twice with the same candidates file but different seeds (e.g. `"111"` vs `"222"`) and asserts:

Both runs exit with code 0\.

Parsed `candidates` arrays are identical (same IDs, scores, weights, bands, etc.).

Parsed `seed` values differ and match the provided CLI arguments, confirming that seed is echoed as metadata only and does not change ranking.

`tests/cli/test_dev_sampler_cli.py::test_dev_sampler_command_is_namespaced` — runs `engine.cli --help` under dev rails and asserts:

Exit code 0\.

Help output includes the `dev:sampler` subcommand, and the help line clearly labels it as “DEV/ADMIN ONLY,” confirming that the harness is scoped to dev/admin usage and not part of the general user-facing catalog.

**Notes:**

EPIC019 PR03 satisfies the **seedable dev/admin sampling** requirement for this subtask:

The dev/admin-only `dev:sampler` command accepts an optional `--seed` argument, is explicitly gated by `APP_ENV` to non-production environments, and calls the pure-compute sampler core introduced in D1.

With the same inputs and seed, the harness produces **byte-identical** JSON output, as demonstrated by `test_dev_sampler_two_run_identity` (two-run identity under closed rails).

Changing the seed affects only the `seed` field in the output; the ranked `candidates` array remains invariant, ensuring that seed usage does not introduce non-deterministic behavior or alter any public bytes. This is exactly the “seed echo only” behavior planned for D2.

Seed semantics remain **metadata-only** in this PR: the sampler core itself does not take a seed, and the ranking logic is independent of seed. This is intentional for D2 and preserves all existing public contracts while establishing the seed interface and closed-rails CLI harness needed for future evidence and potential seed-based tie-breaking work.

This subtask is scoped to the dev/admin CLI harness; it does not introduce a public sampler endpoint, nor does it add sampler-specific evidence/indexing artifacts. Those aspects remain tracked under HDE-DISS003.5 and HDE-DISS003.6 and in future Distillation harness tasks.

### **Subtask HDE-DISS003.5 — Sampler endpoint harness**

**Subtask name/label:** Dev-only sampler endpoint harness

**Subtask description:**  
 Wire a dev-only sampling endpoint that returns candidate IDs only and echoes the seed in `meta` when present; CLI tooling remains the primary dev harness.

The dev sampler HTTP harness is implemented as `POST /internal/dev/sampler` on the Reader adapter and MUST:

* Treat the route as **dev/admin-only** (internal, non-public, not part of the Endpoint Catalog).

* Accept a JSON body with:

  * `viewer_id`: non-empty string, and

  * `candidate_ids`: non-empty list of non-empty strings, and

  * optional `seed`: string.

* Invalid shapes MUST yield typed 4xx invalid-input envelopes, not sampler output.

* Build a `ViewerProfile` and `CandidateFeatures` from IDs using fixed, non-conflicting placeholder values (weight/compat/band) so that sampler invariants are preserved while the HTTP payload stays IDs-only.

* Call the pure-compute sampler core (`engine.sampler.core.sample_and_rank`) to obtain ranked candidates; the HTTP harness MUST NOT reimplement eligibility or ranking logic.

* Construct a response payload:

  * `viewer_id`: the request viewer ID,

  * `meta.seed`: provided seed string or null when omitted, and

  * `candidate_ids`: ordered list of ranked candidate IDs.

* Emit the response via the canonical JSON emitter (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and sorted), under determinism env pins for tests and closed-rails QA (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`).

APP\_ENV gating semantics for this endpoint remain governed by Mechanics and Governance (dev/test/local allowed; `prod`/missing/empty refused) and are exercised more fully in the Phase IV dev/internal HTTP harness and SAFE-rails subtasks; this subtask focuses on the existence, determinism, and canonical JSON behavior of the endpoint harness itself.

**Subtask status:** **Partial**

**Epic or card:** **EPIC-019 (D3 — Dev-only sampler HTTP endpoint harness)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`  
 `TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

**Adapter/HTTP implementation (titles-only):**

`adapter/http_reader.py` — registers and implements `POST /internal/dev/sampler` as a dev/admin-only sampler harness that:

* Validates `viewer_id` and `candidate_ids` shapes as described above and returns typed invalid-input envelopes on error.

* Builds `ViewerProfile` and `CandidateFeatures` from IDs with fixed placeholder values and calls `engine.sampler.core.sample_and_rank` to obtain ranked candidates.

* Returns canonical JSON with `viewer_id`, `meta.seed`, and `candidate_ids` via the shared emitter, with `Cache-Control: no-store`, no `ETag`, and `Content-Type: application/json; charset=utf-8`.

**Determinism and seed behavior tests (titles-only):**

`tests/adapter/test_dev_sampler_http.py::test_dev_sampler_determinism` — under `APP_ENV=dev` and closed rails, posts the same valid payload twice and asserts:

* Both responses have status 200\.

* Response bodies are byte-identical (two-run identity).

* Parsed JSON payloads share the same `viewer_id`, `meta.seed`, and `candidate_ids` array.

`tests/adapter/test_dev_sampler_http.py::test_dev_sampler_seed_only_changes_seed` — posts the same viewer/candidate set with different seeds (e.g. `"111"` and `"222"`) and asserts:

* Both responses have status 200\.

* `candidate_ids` arrays are identical.

* `meta.seed` reflects the respective seed values, confirming seed-only differences.

**Closed-rails QA evidence for D3 (titles/paths only):**

`audit/qa/hde-epic019/dev_sampler_http/D3_env_rails.log` — rails snapshot for Step 2, showing `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `TZ=UTC`, and non-empty `DEV_SAMPLER_URL` (Codespaces dev sampler endpoint).

`audit/qa/hde-epic019/dev_sampler_http/D3_http_run1.headers`  
 `audit/qa/hde-epic019/dev_sampler_http/D3_http_run1.body`  
 `audit/qa/hde-epic019/dev_sampler_http/D3_http_run2.headers`  
 `audit/qa/hde-epic019/dev_sampler_http/D3_http_run2.body` — two-run identity slice: both runs return HTTP/1.1 200 with canonical JSON bodies that are byte-identical under closed rails for a fixed payload.

`audit/qa/hde-epic019/dev_sampler_http/D3_http_seed_111.body`  
 `audit/qa/hde-epic019/dev_sampler_http/D3_http_seed_222.body` — seed behavior slice: same `viewer_id` and `candidate_ids` ordering; only `meta.seed` differs between `"111"` and `"222"`.

**Notes:**

* The dev sampler HTTP harness exists, is wired to the pure-compute sampler core, and meets the determinism and seed behavior requirements for D3 under closed rails, as demonstrated by the Step 2 and Step 3 runs in the EPIC019 Live QA evidence set.

* **SoT: canon — APP\_ENV gating for `/internal/dev/sampler` remains dev/test/local-only; `APP_ENV="prod"`, missing, or empty MUST NOT yield sampler JSON.** Current Codespaces evidence (`forbidden_prod.jsonl` and related logs from the D3 harness) shows at least one scenario where `APP_ENV="prod"` still returns a 200 sampler payload body, which is inconsistent with that gating requirement. This defect is tracked at the epic/build level and via global rails and harness subtasks; until it is fixed and re-verified, this subtask is marked **Partial** even though `JSON_CANONICAL_CHECK_OK` and `TWO_RUN_IDENTITY_OK` are satisfied for the dev-mode harness.

* The APP\_ENV gating tokens themselves (such as `ENV_RAILS_POLICY_OK`) remain single-homed in the SAFE-rails and dev HTTP harness subtasks in later phases; PF09 records here that the endpoint harness’s core behavior and evidence are in place and that APP\_ENV gating behavior is still outstanding in at least one environment scenario documented by EPIC019 Live QA.


  ### **Subtask HDE-DISS003.6 — Evidence & indexing (sampler/ranker)**

**Subtask name/label:** Sampler/ranker evidence & indexing

**Subtask description:**  
 Index sampler/ranker evidence families in the Human Evidence Index and mirror them 1:1 in the Machine Mirror in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to a co-located `path_proof.txt`), under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`).

**Subtask status:** **Done**

**Epic or card:** **EPIC-019 (D4 — Sampler/ranker evidence & indexing)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`MACHINE_MIRROR_UPDATED_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts (titles/paths only):**

**Sampler evidence generator (closed rails; titles-only):**

`tools/evidence/generate_sampler_evidence.py` (or equivalent) — sampler evidence generator that runs under determinism env pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), calls the pure-compute sampler core (`engine.sampler.core`) plus the dev CLI/HTTP sampler harnesses (PR02/PR03/PR04), and emits sampler evidence artifacts and schemas.

**EPIC024 sampler evidence manifest (governed proof; PO-015):**

`artifacts/sampler/epic024/sampler_evidence.json` — EPIC024 sampler evidence manifest (reports `missing_artifacts: 0` when all required sampler evidence families are present).

`artifacts/sampler/epic024/manifest.json` — EPIC024 manifest referencing the sampler evidence manifest and listing the referenced sampler evidence families.

`audit/qa/hde-epic024/checks/D04_sampler_evidence/primary.log` — governed QA check log for D04 sampler evidence (PASS; command `python tools/evidence/run_sampler_evidence.py`).

`tools/evidence/run_sampler_evidence.py` — EPIC024 generator/wrapper used to produce the two fixed-path sampler evidence artifacts for the D04 check.

**Sampler evidence families and artifacts (all canonical JSON; UTF-8, sorted keys, compact, one LF):**

**sampler\_pool\_snapshots** — pool snapshots (eligibility and pool contents):

`artifacts/sampler/pool_snapshots/baseline.json` (and siblings) — snapshots showing viewer ID, candidate IDs, bands, compat scores, weights, eligibility flags, and diversity/recency markers as carried by the sampler core.

`docs/schemas/sampler/pool_snapshots.schema.json` — schema for pool snapshots, with `pool_snapshots.schema.json.path_proof.txt` as the path-proof transcript.

`artifacts/sampler/pool_snapshots/baseline.json.path_proof.txt` — path-proof for the baseline pool snapshot.

**sampler\_two\_run\_logs** — two-run identity logs for sampler outputs:

`artifacts/sampler/two_run/identity.json` — log proving that two runs with identical inputs and config produce byte-identical ranked candidate sequences.

`docs/schemas/sampler/two_run_logs.schema.json` — schema for two-run logs, with `two_run_logs.schema.json.path_proof.txt` as the path-proof transcript.

`artifacts/sampler/two_run/identity.json.path_proof.txt` — path-proof for the two-run identity log.

**sampler\_abba\_logs** — AB/BA/ABBA parity logs:

`artifacts/sampler/abba/ab_ba_parity.json` — AB/BA/ABBA sampler runs demonstrating parity and ABBA properties for a representative corpus.

`docs/schemas/sampler/abba_logs.schema.json` — schema for ABBA logs, with `abba_logs.schema.json.path_proof.txt`.

`artifacts/sampler/abba/ab_ba_parity.json.path_proof.txt` — path-proof for the ABBA parity log.

**sampler\_diversity\_artifacts** — diversity/window/recent constraint evidence:

`artifacts/sampler/diversity/diversity_requirements.json` — evidence that diversity/window/recent constraints are enforced by the sampler as PF-canon is clarified.

`docs/schemas/sampler/diversity_artifacts.schema.json` — schema for diversity artifacts, with `diversity_artifacts.schema.json.path_proof.txt`.

`artifacts/sampler/diversity/diversity_requirements.json.path_proof.txt` — path-proof for diversity artifacts.

**sampler\_seed\_replay\_logs** — seed replay logs from CLI/HTTP harnesses:

`artifacts/sampler/seed_replay/cli_http_seed_replay.json` — logs demonstrating that seeded dev sampler runs (CLI and HTTP) exhibit seed-echo semantics and candidate-set stability (same candidates and order; only seed metadata differs).

`docs/schemas/sampler/seed_replay_logs.schema.json` — schema for seed replay logs, with `seed_replay_logs.schema.json.path_proof.txt`.

`artifacts/sampler/seed_replay/cli_http_seed_replay.json.path_proof.txt` — path-proof for seed replay logs.

**Human Evidence Index & sentinel:**

`docs/evidence/INDEX.json` — Human Index entries for sampler evidence families, with artifact\_keys such as:

`"sampler_pool_snapshots"`

`"sampler_two_run_logs"`

`"sampler_abba_logs"`

`"sampler_diversity_artifacts"`

`"sampler_seed_replay_logs"`

`docs/evidence/INDEX.sha256` — sha256 sentinel over the canonical bytes of `INDEX.json`, regenerated by the sampler evidence tooling in the same PR.

**Machine mirror & provenance-correct path-proofs:**

`artifacts/evidence_index.jsonl` — Machine Mirror records for all sampler artifacts and schemas, one JSON object per line, canonical JSONL (UTF-8; sorted keys; compact; one LF; unknown-key reject), with fixed field order:

`artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

For each sampler artifact and schema, the mirror includes a record with:

`artifact_key` matching the Human Index entry.

`discovered_physical_path` matching the governed artifact path under `artifacts/sampler/**` or `docs/schemas/sampler/**`.

`produced_at_utc` equal to the evidence refresh time (for example `2025-11-30T03:58:47Z` after the bugfix), in sync with the corresponding path-proof.

`proof_anchor` pointing to the co-located `*.path_proof.txt`.

`sha256` and `size_bytes` matching the artifact’s canonical bytes.

**Notes:**

**Notes:**

* The dev sampler HTTP harness exists, is wired to the pure-compute sampler core, and meets the determinism and seed behavior requirements for D3 under closed rails, as demonstrated by the Step 2 and Step 3 runs in the EPIC019 Live QA evidence set (two-run identity and seed-only differences for a fixed viewer/candidate set).

* **SoT: canon — APP\_ENV gating for `/internal/dev/sampler` remains dev/test/local-only; `APP_ENV="prod"`, missing, or empty MUST NOT yield sampler JSON.** Current Codespaces evidence (`forbidden_prod.jsonl` and related logs from the D3 harness) shows at least one scenario where `APP_ENV="prod"` still returns a 200 sampler payload body, which is inconsistent with that gating requirement. This gating defect is tracked as **ISSUE-APPENV-D3-GATING — Dev sampler HTTP harness does not enforce APP\_ENV=prod/empty/unset gating** in the PF09 outstanding issues registry. Until that issue is fixed (adapter/Reader gating updated, tests extended for prod/empty/unset, and Live QA re-run) and re-verified, this subtask remains **Partial** even though `JSON_CANONICAL_CHECK_OK` and `TWO_RUN_IDENTITY_OK` are satisfied for the dev-mode harness.

* The APP\_ENV gating tokens themselves (such as `ENV_RAILS_POLICY_OK`) remain single-homed in the SAFE-rails and dev HTTP harness subtasks in later phases; PF09 records here that the endpoint harness’s core behavior and evidence are in place and that APP\_ENV gating behavior is still outstanding in at least one environment scenario documented by EPIC019 Live QA and ISSUE-APPENV-D3-GATING.


## **Task HDE-DISS004 — Deterministic Engine Core**

**Task ID:** HDE-DISS004

**Task name/label:** Deterministic Engine Core

**Task status:** **Done**

**Task description:**  
 Maintain a pure-compute core (ops, scoring, aggregation) with no I/O/clocks/globals, AB↔BA neutrality, two-run identity, stable reductions via ASCII sorting, and canonical JSON for any core-emitted evidence, with deterministic behavior proven by governed artifacts and Index/Mirror discipline.

**Task notes:**

**EPIC019 PR06 (Engine Core behavior — HDE-DISS004.1–.3)** introduced the pure-compute Engine Core module (`engine/core/core.py`) and a dedicated test suite under `tests/core/` that proves the core:

Does not perform file, network, clock, env, or global state access.

Implements neutral metrics and ordered IDs/bands using existing Phase II primitives (`engine.compat.thresholds.BANDS`, `engine.order.comparators.compare_ids`, `canonicalize_set`, `ABBA_CANONICAL_PAIR`).

Satisfies AB↔BA neutrality for neutral metrics and two-run identity for `CoreResult` under determinism pins via `ensure_determinism_env`.

Produces JSON-ready `CoreResult` dataclasses that serialize stably with `json.dumps(dataclasses.asdict(result), sort_keys=True)`.

**EPIC019 PR07 \+ bugfix (Engine Core evidence & indexing — HDE-DISS004.4)** add governed Engine Core evidence families under `artifacts/core/**` with schemas under `docs/schemas/core/**` and integrate them into the Human Evidence Index and Machine Mirror with path-proofs, mirroring the sampler evidence pattern. The new Engine Core families are:

`engine_core_purity_report` → `artifacts/core/purity/purity_report.json` (`engine_core_purity_report.schema.json`).

`engine_core_two_run_logs` → `artifacts/core/two_run/identity.json` (`engine_core_two_run_logs.schema.json`).

`engine_core_abba_logs` → `artifacts/core/abba/ab_ba_parity.json` (`engine_core_abba_logs.schema.json`).

`engine_core_json_compare_logs` → `artifacts/core/json_compare/core_result_json_compare.json` (`engine_core_json_compare_logs.schema.json`).

Each artifact is canonical JSON (UTF-8; sorted keys; compact; exactly one LF), has a sibling `*.path_proof.txt` transcript, and is indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` with a canonical JSONL record (fixed field order, unknown-key reject, `proof_anchor` pointing to the path-proof).

PR07 also extends the closed-rails sanity pipeline so that `tools/evidence/run_sanity_pipeline.py` invokes both sampler and Engine Core evidence generators under `ensure_determinism_env`, records their runs in `artifacts/sanity/sanity.log`, and ensures `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` remain in sync. The associated bugfix corrects out-of-date `sha256`/`size_bytes` metadata for `artifacts/sanity/sanity.log` in the EPIC019 manifest, so `SANITY_PIPELINE_OK` and `DETERMINISM_ENV_PINS_OK` now have coherent evidence and manifest bindings.

With the pure-compute Engine Core module, dedicated core tests, and the four Engine Core evidence families now present, canonical, and indexed with path-proofs, HDE-DISS004 is considered **Done** at the behavior \+ evidence level for this phase; further Engine Core usage is governed by higher-phase tasks and global discipline rows.

**Task-level tokens (titles-only):**

`NO_IO_NO_CLOCKS_OK`

`TWO_RUN_IDENTITY_OK`

`AB_BA_PARITY_OK`

`JSON_CANONICAL_CHECK_OK`

Evidence tokens (Engine Core slice): `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`

### **Subtask HDE-DISS004.1 — No I/O, no clocks, no globals**

**Subtask name/label:** Pure compute (no I/O/clocks/globals)

**Subtask description:**  
 Ensure the Engine Core performs no I/O and does not access clocks, environment, filesystem, network, or process-wide globals; prove via static/grep guard, import-graph analysis, and governed purity evidence.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC019 (PR06 behaviour \+ PR07 evidence)**

**Tokens:**

`NO_IO_NO_CLOCKS_OK`

**Evidence / artifacts:**

**Implementation and tests (titles-only):**

`engine/core/core.py` — pure-compute Engine Core module defining `ParticipantState`, `CoreConfig`, `PerspectiveBreakdown`, and `CoreResult`.

`tests/core/test_engine_core_purity.py` — purity tests that run under `ensure_determinism_env(apply=True)` and assert no forbidden imports (os, time, datetime, random, socket, subprocess) and no env/global references.

**Engine Core purity evidence family:**

`artifacts/core/purity/purity_report.json` — Engine Core purity report (canonical JSON) summarizing purity checks and invariants for the core.

`docs/schemas/core/engine_core_purity_report.schema.json` — JSON Schema for purity reports, with `engine_core_purity_report.schema.json.path_proof.txt`.

`artifacts/core/purity/purity_report.json.path_proof.txt` — path-proof transcript with `path`, `sha256`, `size_bytes`, `mtime_utc`, and `produced_at_utc` consistent with Mirror records.

**Index/Mirror:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — Human Index & sentinel with an `artifact_key` for `engine_core_purity_report`.

`artifacts/evidence_index.jsonl` — Machine Mirror records for purity artifacts and schemas, with canonical JSONL, fixed field order, and `proof_anchor` pointing to the purity path-proofs.

### **Subtask HDE-DISS004.2 — AB↔BA parity & two-run identity**

**Subtask name/label:** AB↔BA & two-run identity for Engine Core

**Subtask description:**  
 Prove that Engine Core executions are AB↔BA neutral for neutral metrics (swapping A,B yields identical neutral outputs) and satisfy two-run identity (running twice with same inputs yields identical outputs), with governed evidence.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC019 (PR06 behaviour \+ PR07 evidence)**

**Tokens:**

`TWO_RUN_IDENTITY_OK`

`AB_BA_PARITY_OK`

**Evidence / artifacts:**

**Implementation and tests (titles-only):**

`engine/core/core.py` — implements `_ordered_pair`, `_ordered_bands`, neutral score, and shared traits using Phase II comparators/utilities.

`tests/core/test_engine_core_abba.py` — AB↔BA tests that assert neutral fields (neutral score, ordered\_pair, ordered\_bands, shared traits) are identical for `compute_core(A,B,config)` and `compute_core(B,A,config)` and that perspective metrics cross-swap consistently.

`tests/core/test_engine_core_determinism.py` — determinism tests that call `compute_core` twice under `ensure_determinism_env(apply=True)` and assert equal `CoreResult` plus JSON-compatibility under `json.dumps(<obj>, sort_keys=True)`.

**Engine Core two-run & ABBA evidence families:**

`artifacts/core/two_run/identity.json` — two-run identity log for Engine Core under closed rails, showing identical CoreResult metrics across runs.

`docs/schemas/core/engine_core_two_run_logs.schema.json` — schema for two-run logs, with `engine_core_two_run_logs.schema.json.path_proof.txt`.

`artifacts/core/two_run/identity.json.path_proof.txt` — path-proof for the two-run log.

`artifacts/core/abba/ab_ba_parity.json` — AB/BA CoreResult parity log for Engine Core (canonical JSON).

`docs/schemas/core/engine_core_abba_logs.schema.json` — schema for ABBA logs, with `engine_core_abba_logs.schema.json.path_proof.txt`.

`artifacts/core/abba/ab_ba_parity.json.path_proof.txt` — path-proof for the ABBA parity log.

**Index/Mirror:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — entries and sentinel for Core two-run and ABBA families.

`artifacts/evidence_index.jsonl` — mirror records for Engine Core two-run/ABBA artifacts and schemas, with canonical JSONL and `proof_anchor` fields.

### **Subtask HDE-DISS004.3 — Canonical JSON for core-emitted evidence**

**Subtask name/label:** Canonical JSON compare for Engine Core artifacts

**Subtask description:**  
 Ensure any Engine Core JSON emitted for evidence is canonical (UTF-8/no BOM; sorted keys; compact; exactly one LF) and matches canonical re-serialization; prove this via a dedicated JSON-compare evidence family.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC019 (PR06 behaviour \+ PR07 evidence)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts (titles/paths only):**

Engine Core JSON-compatibility tests:

`engine/core/core.py` and `tests/core/test_engine_core_determinism.py` — verify that `CoreResult` dataclasses are JSON-ready and stable under determinism pins.

Engine Core JSON-compare evidence family:

`artifacts/core/json_compare/core_result_json_compare.json` — canonical JSON compare log for Engine Core results (e.g., re-serialization tests showing empty diffs).

`docs/schemas/core/engine_core_json_compare_logs.schema.json` — schema for JSON compare logs, with `engine_core_json_compare_logs.schema.json.path_proof.txt`.

`artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` — path-proof transcript.

Index/Mirror entries for `engine_core_json_compare_logs` and schema in `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`.

### **Subtask HDE-DISS004.4 — Evidence & indexing (engine core)**

**Subtask name/label:** Engine Core evidence & indexing

**Subtask description:**  
 Ensure Engine Core purity, ABBA, two-run identity, and JSON-compare artifacts are indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path-proofs), under closed rails.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC019 (PR07 \+ bugfix — Engine Core evidence & indexing)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`MACHINE_MIRROR_UPDATED_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

Engine Core evidence families (see HDE-DISS004.1–.3 above) and their schemas under `docs/schemas/core/**`.

Human Index and sentinel:

`docs/evidence/INDEX.json` — entries for Engine Core purity, two-run, ABBA, and JSON-compare artifacts and their schemas.

`docs/evidence/INDEX.sha256` — sha256 sentinel over canonical `INDEX.json` bytes including Engine Core entries.

Machine Mirror:

`artifacts/evidence_index.jsonl` — canonical JSONL records for Engine Core evidence artifacts and schemas, one JSON object per line with field order:

`artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.

Path-proofs:

`artifacts/core/**.path_proof.txt` and `docs/schemas/core/**.schema.json.path_proof.txt` — path-proof transcripts for all Engine Core artifacts and schemas, with `produced_at_utc` aligned to artifact refresh times and mirrored in the Machine Mirror.

**Notes:**

EPIC019 PR07 follows the same pattern as sampler evidence: Engine Core evidence is generated under closed rails via `tools/evidence/generate_engine_core_evidence.py`, indexed and mirrored alongside sampler evidence, and validated by the existing evidence skeleton and determinism/sanity pipeline harnesses.

This subtask is now considered **Done** for Engine Core evidence; future Engine Core enhancements (beyond purity/two-run/ABBA/JSON-compare) will be tracked in new epics and PF09 rows rather than reopening HDE-DISS004.

---

## Task HDE-DISS005 — Band Thresholds & Tuning (admin)

**Task ID:** HDE-DISS005

**Task name/label:** Band Thresholds & Tuning (admin)

**Task status:** Done

**Task description:** Admin-only band thresholds & tuning workflow: pin inclusive-high band policy with edge fixtures, route numeric thresholds to the constants pack, capture diffs and identity hashes for tuning runs, and index tuning artifacts under the Evidence Index.

**Task notes:**

**Status lock (PF16):** PF09 Phase-II “Band thresholds & tuning (admin)” is satisfied under **HDE-EPIC007 — Magic-10 Category Engine (Signals)** and is not carried forward to remaining epics.

**Historical audit:** Audit (v1 — 2025-11-17) remains as historical context only. Current canon treats this checklist task as fully closed by EPIC-007. Any new tuning work must be routed via **HDE Phased Epics**, not by reopening this row.

### **Subtask HDE-DISS005.1 — Band policy & edge fixtures**

**Subtask name/label:** Band edge fixtures (24/49/74/100)

**Subtask description:**  
 Pin inclusive-high band policy; add edge-case fixtures at 24/49/74/100 per preset (with \+1 transitions).

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`BAND_EDGE_GOLDENS_OK`

**Evidence / artifacts:**

`artifacts/thresholds/*.json`

`audit/gates/bands/edges.snapshot.json`

---

### **Subtask HDE-DISS005.2 — Route thresholds to constants pack**

**Subtask name/label:** Route thresholds to constants pack & keep public numeric-free

**Subtask description:**  
 Route numeric thresholds to the constants pack (HDE-Math-Spec / HDE-Schemas & Artifacts) and keep public output numeric-free.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`M10_MAPS_OK`

**Evidence / artifacts:**

`artifacts/thresholds/*.json` (constants pack-aligned)

---

### **Subtask HDE-DISS005.3 — Diffs & identity hash for tuning runs**

**Subtask name/label:** Tuning diffs & identity hash

**Subtask description:**  
 Capture compact diffs per change and compute `identity_hash` over the LF-terminated compat body for each tuning run.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`RELEASE_ID_RECOMPUTE_OK`

**Evidence / artifacts:**

`audit/gates/bands/edges.diff.json`

`artifacts/thresholds/identity_hash.txt`

---

### **Subtask HDE-DISS005.4 — Evidence & indexing (bands)**

**Subtask name/label:** Band thresholds evidence & indexing

**Subtask description:**  
 Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs) for all band thresholds artifacts, following Evidence Index & mirror discipline.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

---

## **Task HDE-DISS006 — Category Framework (internal)**

**Task ID:** HDE-DISS006

**Task name/label:** Category Framework (internal)

**Task status:** **Done**

**Task description:**  
 Implement per-category calculators and precedence hooks over Magic-10, enforce frozen category order and AB↔BA/two-run identity, and integrate per-channel mechanics for category-level behavior, with canonical JSON evidence and indexing.

**Task notes:**

**Status lock (HDE-EPIC007 — Magic-10 Category Engine (Signals)):**  
 PF09 Phase-II “Category framework” is satisfied under **HDE-EPIC007**; this checklist row is history-only and does not carry forward to remaining epics.

**Status (Audit v1 — 2025-11-17):**  
 Previously marked *Not done* and called out missing `CATEGORY_FRAMEWORK_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, and `TWO_RUN_IDENTITY_OK` tokens, as well as missing Magic-10 key table and compat parity evidence.  
 These audit notes are now historical context only; acceptance lives in the EPIC-007 exit set and associated manifest/acceptance maps.

**Task-level tokens (titles-only):**

`CATEGORY_FRAMEWORK_OK`

`JSON_CANONICAL_CHECK_OK`

`AB_BA_PARITY_OK` (category layer)

`TWO_RUN_IDENTITY_OK`

---

### **Subtask HDE-DISS006.1 — Per-category calculators & precedence hooks**

* **Subtask name/label:** Category calculators & precedence

* **Subtask description:**  
   Implement per-category calculators and precedence hooks; use total-order utilities (§5) for any ordered emission.

* **Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

* **Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

* **Tokens:**

  * `CATEGORY_FRAMEWORK_OK`

* **Evidence / artifacts:**

  * `artifacts/category/calculators.snapshot.json` — governed calculators snapshot (schema single-home: PF12)

---

### **Subtask HDE-DISS006.2 — Frozen Magic-10 order & ABBA / two-run**

**Subtask name/label:** Magic-10 order & symmetry

**Subtask description:**  
 Enforce frozen Magic-10 order at all emission points and enforce AB↔BA and two-run identity for category-level outputs.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`AB_BA_PARITY_OK` (category layer)

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/category/abba_identity.bytes` — ABBA identity evidence for category outputs.

---

### **Subtask HDE-DISS006.3 — Per-channel mechanics integration**

**Subtask name/label:** Per-channel category mechanics

**Subtask description:**  
 Integrate per-channel mechanics into the category framework:

Treat channels as canonical `NN-NN` edges.

Track compromise direction \+ gate.

Treat circuit as channel-scoped, with optional bridge/timing analytics for internal use.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`CATEGORY_FRAMEWORK_OK`

**Evidence / artifacts:**

Captured in category calculators snapshots and ABBA logs listed above.

---

### **Subtask HDE-DISS006.4 — Canonical JSON & evidence**

**Subtask name/label:** Category framework canonical JSON & evidence

**Subtask description:**  
 Ensure category framework evidence (calculators snapshot, ABBA identity, canonical-compare logs) uses canonical JSON and satisfies JSON re-serialization compare (UTF-8/no BOM; sorted keys; compact; one LF).

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts (titles/paths only):**

`artifacts/category/calculators.snapshot.json`

`artifacts/category/abba_identity.bytes`

Canonical-compare logs (paths owned by Evidence Index)

---

### **Subtask HDE-DISS006.5 — Evidence & indexing (category framework)**

**Subtask name/label:** Category framework evidence & indexing

**Subtask description:**  
 Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs) for category framework artifacts, using the global Evidence Index & mirror rules.

**Subtask status:** **Done (history-only; satisfied under HDE-EPIC007)**

**Epic or card:** **HDE-EPIC007 — Magic-10 Category Engine (Signals)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

---

# **Phase III — Separation (Public shape, identity, guardrails)**

**Phase description:**  
 Wire persistence, public presenter/emitter, error envelope, and internal ops identity surfaces so that public and operator-visible bytes are canonical, deterministic, and backed by indexed evidence.

**Phase master status:** **Partial**

**Notes:**

* This phase remains Partial due to remaining Phase III closure work outside `/internal/version` (see remaining Partial/Not done rows in this phase).

* EPIC022 D3 is now fully evidenced as PASS for the `/internal/version` closure slice:

  * D3.1 internal\_version\_bundle captured and validated the prod `/internal/version` surface with governed artifacts under `artifacts/ops/internal_version/`.

  * D3.2 evidence\_index\_update\_and\_validate completed index/mirror regeneration and validation under closed rails, including explicit checks that the PF12-canonical conditional-header filenames (`headers_cond_if_*`) are present in the governed indices.  
     Update Subtasks HDE-SEPA004.4 and HDE-SEPA004.5 to reflect this closure.

* Evidence/index parity must use the canonical Machine Mirror path `artifacts/evidence_index.jsonl` only; any alternate mirror path in tooling output is a blocker and must be corrected before merge.

---

## Task HDE-SEPA001 — Persistence Layer

**Task ID:** HDE-SEPA001

**Task name/label:** Persistence Layer

**Task description:**  
 Persist public results and provenance with canonical bytes, an explicit link to `release_id`, idempotent DB writes, and integrity checks that stored bodies equal emitted bodies, under least‑privilege DB posture and without logging secrets/PII.

**Task status:** Done 

**Task notes:**

Writer surfaces use `Cache-Control: no-store`.

DDL and grants are kept current; PF09 consumes but does not define token semantics.

### Subtask HDE-SEPA001.1 — Idempotent write path to DB

**Subtask ID:** HDE-SEPA001.1

**Subtask name/label:** Idempotent DB write path

**Subtask description:**  
 Ensure an idempotent write path to the DB for public payloads so that repeated writes do not produce double‑writes or drift.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:** Unknown (idempotent write tokens live in HDE-Governance; PF09 is consumer‑only).

**Evidence / artifacts:**

Implicit in DB and persistence tests (paths not pinned in PF09).

**Notes:**  
 The checklist calls out idempotence as an expectation, not by a specific token name.

### Subtask HDE-SEPA001.2 — Canonical byte-compare vs emitter

**Subtask ID:** HDE-SEPA001.2

**Subtask name/label:** Stored body equals emitter output

**Subtask description:**  
 Verify via canonical byte-compare that the stored public body in the DB is **byte‑for‑byte equal** to the emitter output.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:**

Likely uses `JSON_CANONICAL_CHECK_OK` indirectly (semantics live in canon; not named here).

**Evidence / artifacts:**

`artifacts/presenter/json_canon_compare.log`

### Subtask HDE-SEPA001.3 — Grants / DDL least-privilege posture

**Subtask ID:** HDE-SEPA001.3

**Subtask name/label:** DB grants & DDL posture

**Subtask description:**  
 Keep DB grants and DDL artifacts current and consistent with least‑privilege posture for persistence of public payloads.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:** Unknown (DB security tokens live in Governance).

**Evidence / artifacts:**

`artifacts/db/ddl_applied.sql`

`artifacts/db/grants.txt`

### Subtask HDE-SEPA001.4 — No secrets/PII in logs

**Subtask ID:** HDE-SEPA001.4

**Subtask name/label:** Logging discipline (no secrets/PII)

**Subtask description:**  
 Ensure that persistence and writer pathways do **not** emit secrets or PII into logs; logs are keys‑only and redacted as needed.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:** Unknown (log‑scrubbing tokens live in Governance).

**Evidence / artifacts:**

Logging configuration and tests (paths not pinned here).

### Subtask HDE-SEPA001.5 — Identity snapshot for services

**Subtask ID:** HDE-SEPA001.5

**Subtask name/label:** Service identity snapshot

**Subtask description:**  
 Maintain a service identity snapshot for persisted public results and provenance.

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:**

Supports identity/provenance tokens (e.g., `RELEASE_ID_RECOMPUTE_OK` indirectly; semantics elsewhere).

**Evidence / artifacts:**

`artifacts/identity/service_identity.json`

### Subtask HDE-SEPA001.6 — Persistence evidence indexing

**Subtask ID:** HDE-SEPA001.6

**Subtask name/label:** Evidence Index & Machine Mirror parity (persistence)

**Subtask description:**  
 Index persistence evidence in the Human Evidence Index and Machine Mirror in the same PR:

Update `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`.

Update `artifacts/evidence_index.jsonl` (records-only canonical JSONL; UTF‑8, one LF; unknown‑key reject; fixed field order; each record includes a `proof_anchor` to a co‑located path\_proof).

**Subtask status:** **Done**

**Epic or card:** Unknown

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## **Task HDE-SEPA002 — Error Envelope & Token Set**

**Task ID:** HDE-SEPA002

**Task name/label:** Error Envelope & Token Set

**Task description:**  
 Provide a central typed, numeric-free error envelope with canonical JSON, validated token map, Reader↔CLI parity, CLI stream discipline, and evidence indexed in the Evidence Index and Machine Mirror.

**Task status:** **Done**

**Task notes:**

Audit v1 (2025-11-17) originally called out missing CLI stream discipline and canonical JSON proof for the governed error/CLI surfaces (success stdout-only with one LF; errors stderr-only; usage exit 64; numeric-free, canonical JSON envelopes), plus the lack of hardened writers/errors header posture and error-envelope evidence families.

EPIC020 PR 1 and PR 2a introduced the governed error token map and `error_v1` envelope, routed writer and reader error surfaces (including 404/405) through a shared `error_envelope` helper and the canonical serializer, and normalized CLI error handling so that usage errors exit 64, success writes only to stdout, and errors write only to stderr, with EPIC020 D1 tokens initially marked **PARTIAL**.

EPIC020 PR 2b completes the D1 slice by:

* adding a governed error parity harness (`tools/errors/generate_error_artifacts.py` \+ `tests/cli/test_errors_parity.py`) under closed rails,

* generating deterministic error artifacts under `parity/errors_reader_cli.*`, `errors/schema_check/error_envelope_invalid_*.log`, and `errors/token_map/token_map.json` (with governed path-proofs and artifact keys such as `ERRORS_READER_CLI_PARITY_V1`, `ERROR_SCHEMA_CHECK_V1`, and `ERROR_TOKEN_MAP_V1`), and

* wiring these artifacts into the Human Evidence Index and Machine Mirror with EPIC020 metadata and determinism pins.

The EPIC020 D1 tokens `ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, `ERROR_TOKEN_MAP_OK`, `CLI_READER_EMITTER_PARITY_OK`, , `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK` are recorded as **DONE** in `docs/acceptance_map_epic020.json` and `audit/EPIC-020_MANIFEST.json`, each bound to specific tests and error evidence artifacts. PF09 does not mint or list unrostered tokens; stderr-only stream discipline is tracked as a behavioral requirement (tested and evidenced) and must not be represented by a non-roster token in PF09.

### **Subtask HDE-SEPA002.1 — Error envelope shape & numeric-free body**

**Subtask ID:** HDE-SEPA002.1

**Subtask name/label:** Typed, numeric-free error envelope

**Subtask description:**  
 Emit error bodies as typed, numeric-free JSON in the governed `error_v1` shape:

* Envelope shape: `{"schema": "v1", "ok": false, "code": "<ERR_*>", "error": "<message>"}` with an optional `details` field for bounded diagnostics when required.

* The allowed key set is fixed by the `error_v1` schema; error bodies do **not** introduce numeric fields, stack traces, or SR/XR numerics in public or admin responses.

* Error envelopes are LF-terminated and serialized by the single presenter/emitter via a shared `error_envelope` helper; governed error surfaces must call this helper rather than ad-hoc serializers.

* Error payloads do not echo request bodies or secrets and do not include PII.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — error envelope & token set, PR 1–2b)**

**Tokens:**

`ERROR_JSON_CANON_OK` (shape & canonicality)

**Evidence / artifacts:**

`engine/compat/errors.py` — `error_envelope` helper that canonicalizes tokens and emits `error_v1` bodies via the shared serializer (no ad-hoc JSON).

`engine/compat/error_tokens.py` — governed error token map used by `error_envelope` (see HDE-SEPA002.3).

`tests/adapter/test_jsonschema.py::test_error_envelope_schema_on_unauthorized_prod` — JSON-schema validation for `error_v1` envelopes on governed writer/error surfaces.

`tests/adapter/test_jsonschema.py::test_notfound_uses_error_schema` — verifies that `/nope` 404 responses use `error_v1` and match the error schema, with LF-terminated bodies.

`errors/schema_check/error_envelope_invalid_json.log` and `errors/schema_check/error_envelope_invalid_viewer_prefs.log` — schema-check logs for representative error scenarios, with governed path-proofs and artifact keys (for example `ERROR_SCHEMA_CHECK_V1`) single-homed in PF12.

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 entries marking `ERROR_JSON_CANON_OK` as **DONE** and binding it to the schema tests and error schema logs above.

**Notes:**  
 This row is treated as Done for the EPIC020 D1 slice: all governed D1 error surfaces (writer diagnostic route, reader error cases in scope, and 404\) now emit `error_v1` envelopes via the shared helper, are schema-checked, and satisfy `ERROR_JSON_CANON_OK` in the EPIC020 acceptance map and manifest. Future error scenarios and surfaces use the same envelope but are owned by later epics and Distillation tasks.

### Subtask HDE-SEPA002.2 — Error transport headers (writers/errors)

**Subtask ID:** HDE-SEPA002.2

**Subtask name/label:** Error transport headers (no-store, no ETag)

**Subtask description:**  
 For error responses on writers/errors routes (which are **not** Catalog-eligible; A7 success proofs stay bound to Catalog success routes only), enforce:

* `Content-Type: application/json; charset=utf-8`

* `Cache-Control: no-store`

* No `ETag` header

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — writers/errors header posture, PR 2b)**

**Tokens:**

Header posture tokens (names live in Governance; not restated here).

**Evidence / artifacts:**

`tests/transport/headers/no_store_writers_errors.snap` — canonical writer/error header snapshot with `[success]` and `[error]` sections capturing expected status and headers (no-store, UTF-8 JSON, no `ETag`, and `WWW-Authenticate` on 401).

`tests/transport/test_writers_errors_headers.py` — closed-rails header test that loads the snapshot, calls `/ops/writer/diagnostic` with correct vs wrong admin tokens, and asserts that actual headers match the snapshot sections and that `etag` is absent.

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 entries that bind the writer/error header tokens to these snapshot tests.

### **Subtask HDE-SEPA002.3 — Error token map & casing**

**Subtask ID:** HDE-SEPA002.3

**Subtask name/label:** Token map & canonical codes

**Subtask description:**  
 Maintain a canonical governed error token→message table and alias layer that:

* Uses **UPPER\_SNAKE** tokens of the form `ERR_*` as the canonical codes that appear in `error_v1.code` for governed Reader and writer/error surfaces.

* Preserves existing lower-snake names (for example `"invalid_json"`, `"invalid_prefs"`, `"forbidden"`) as internal aliases only; aliases are resolved via a helper (for example `canonical_token_for`) and are **not** emitted as `code` values in `error_v1` envelopes.

* Matches a golden token→message map byte-for-byte; any change to the token set or messages must go through a governed update (Doc-Delta \+ acceptance map changes), not ad-hoc edits.

* Clearly separates reader tokens (`ERR_READER_*`), writer/diagnostic tokens (`ERR_WRITER_*`), and generic tokens (for example `ERR_NOT_FOUND`), with semantics single-homed in HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide (titles-only).

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — error envelope & token set, PR 1–2b)**

**Tokens:**

`ERROR_TOKEN_MAP_OK`

**Evidence / artifacts:**

`engine/compat/error_tokens.py` — canonical `ERROR_TOKEN_MAP` defining reader (`ERR_READER_*`), writer (`ERR_WRITER_*`), and generic (`ERR_NOT_FOUND`) tokens plus legacy alias mappings.

`engine/compat/errors.py` — `canonical_token_for` helper that resolves legacy aliases into canonical `ERR_*` tokens before emitting `error_v1` envelopes.

`errors/token_map/token_map.json` — governed token map snapshot (JSON array of `{aliases, code, message}` records) with path-proof transcript; artifact key `ERROR_TOKEN_MAP_V1` (record-type semantics single-homed in PF12).

`tests/cli/test_errors_parity.py::test_token_map_snapshot_matches_canonical` — asserts that `errors/token_map/token_map.json` equals `render_token_map()` and that every `code` in the snapshot appears in `ERROR_TOKEN_MAP`.

`tests/adapter/test_diagnostic_writer.py` — diagnostic writer tests asserting canonical `ERR_WRITER_*` codes and messages for invalid content type, invalid JSON, invalid input shape, unknown keys, and oversized payloads.

`docs/acceptance_map_epic020.json` — EPIC020 D1 acceptance map listing `ERROR_TOKEN_MAP_OK` as **DONE** and binding it to the token map snapshot and diagnostic writer/parity tests.

`audit/EPIC-020_MANIFEST.json` — EPIC020 manifest entries mapping `ERROR_TOKEN_MAP_OK` to the same tests and artifacts.

**Notes:**  
 For the D1 slice, the governed error token map is now fully implemented, snapshotted, and indexed: `ERROR_TOKEN_MAP_OK` is satisfied by the combination of `ERROR_TOKEN_MAP`, the on-disk snapshot, and tests that prove equality and coverage. Reader/CLI parity for specific error scenarios is exercised via the parity harness (HDE-SEPA002.5); the semantics of individual `ERR_*` codes remain single-homed in Governance and Mechanics.

### **Subtask HDE-SEPA002.4 — Canonical JSON for error envelopes**

**Subtask ID:** HDE-SEPA002.4

**Subtask name/label:** Canonical JSON & re-serialization check

**Subtask description:**  
 Ensure that governed error responses are canonical JSON and pass re-serialization checks:

* UTF-8 (no BOM).

* ASCII-sorted keys.

* Compact separators; exactly one trailing LF.

* Arrays that function as sets are deduped and ASCII-sorted before hashing or comparison.

* Re-serializing an `error_v1` envelope via the canonical serializer must produce the same bytes (expected empty diff).

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — error envelope & token set, PR 1–2b)**

**Tokens:**

`ERROR_JSON_CANON_OK`  
 `JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

`tests/adapter/test_jsonschema.py::test_error_envelope_schema_on_unauthorized_prod` — asserts that unauthorized writer responses emit canonical `error_v1` JSON bodies that satisfy the error schema.

`tests/adapter/test_jsonschema.py::test_notfound_uses_error_schema` — asserts that 404 `/nope` responses emit LF-terminated `error_v1` bodies matching the JSON schema.

`tests/cli/test_cli_usage_and_errors.py` — CLI error usage and runtime tests confirming that success cases write canonical JSON to stdout (LF-terminated) with empty stderr and that error cases write LF-terminated JSON error envelopes to stderr with no stdout output.

`tests/cli/test_errors_parity.py::test_http_and_cli_parity` — closed-rails parity tests that assert HTTP and CLI error envelopes for EPIC020 scenarios are schema-valid, numeric-free, and exactly match stored artifacts.

`artifacts/cli/canonical/json_canon_compare.log` — canonical JSON compare log for error envelopes (encoding/key-order/compact/LF proof).

`errors/canonical_check/error_envelope_invalid_*.log` — canonicalization check artifacts for representative error scenarios (invalid JSON, invalid viewer prefs), each with governed path-proofs and artifact key `ERROR_SCHEMA_CHECK_V1` or equivalent (record-type semantics single-homed in PF12).

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 entries marking `ERROR_JSON_CANON_OK` and `JSON_CANONICAL_CHECK_OK` as **DONE** and binding them to the schema, parity, and canonicalization artifacts above.

**Notes:**  
 For EPIC020 D1, canonical JSON behavior is now implemented and evidenced for the writer, reader, health/not-found, and CLI error surfaces in scope, and the error canonicalization tokens are green in the acceptance map. Future epics may add additional error scenarios and flows (for example DB/vendor errors), but those will build on the same canonicalization infrastructure and are not required for this subtask’s D1 acceptance.

### **Subtask HDE-SEPA002.5 — Reader↔CLI error parity & two-run identity**

**Subtask ID:** HDE-SEPA002.5

**Subtask name/label:** Error parity & determinism

**Subtask description:**  
Ensure that for the same error condition:

* Reader and CLI emit **byte-identical** error envelopes.  
* Re-emitting the same error twice produces bitwise-identical bytes.

**Subtask status:** **Done**

**Epic or card:**  
**HDE-EPIC020 (D1 — baseline error parity harness, PR 2b)**  
**HDE-EPIC022 (D1 — required scenario expansion and concrete acceptance bindings)**

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`  
`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

Parity artifacts (stored under closed rails by the parity generator; concrete files must exist once evidence is present):

`parity/errors_reader_cli.invalid_json.http.json` / `.cli.txt`  
`parity/errors_reader_cli.invalid_viewer_prefs.http.json` / `.cli.txt`

EPIC022 D1 adds the two missing required scenarios and stores their parity artifacts (no placeholders once evidence exists):

`parity/errors_reader_cli.db_unavailable.http.json` / `.cli.txt`  
`parity/errors_reader_cli.vendor_attempt_closed_rails.http.json` / `.cli.txt`

Schema logs confirming parity scenarios use valid `error_v1` envelopes:

`errors/schema_check/error_envelope_invalid_*.log`  
`errors/schema_check/error_envelope_db_unavailable.log`  
`errors/schema_check/error_envelope_vendor_attempt_closed_rails.log`

Parity enforcement test (strict equality vs stored artifacts; scenario roster enforced by test logic):

`tests/cli/test_errors_parity.py::test_http_and_cli_parity`

Acceptance wiring (titles-only; canonical close-pack filenames):

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 entries for the baseline parity slice.

`docs/acceptance_map_epic022.json` / `audit/EPIC-022_MANIFEST.json` — EPIC022 acceptance artifacts, updated in PR2+ to bind D1 tokens to concrete tests/artifacts (no placeholders once evidence exists).

**Notes:**  
EPIC020 established the baseline parity harness and storage model; EPIC022 D1 closes the remaining required scenario coverage by adding **db\_unavailable** and **vendor\_attempt\_closed\_rails** and binding those scenarios to concrete parity artifacts and tests. D0 scaffolding may contain placeholders, but PR2+ acceptance bindings must be concrete once evidence exists, to avoid “pattern treated as evidence” drift.

Tracked issue (EPIC022 posture; deferred): the parity harness MUST be able to force the `db_unavailable` scenario deterministically (no flaky dependency on ambient DB/network state). Record as deferred in acceptance artifacts and do not claim it as satisfied until the forcing mechanism is deterministic and reviewable.

### **Subtask HDE-SEPA002.6 — CLI stderr/stdout discipline & usage exit 64**

*Subtask name/label:* CLI stderr/stdout discipline & usage exit code

*Subtask description:*

Enforce CLI stream and exit-code discipline for all CLI commands in alignment with the mechanics and CLI spec:

**Streams:**

* Successful runs write **only** the public JSON body to `stdout`, LF-terminated, with no ANSI escapes and no extra bytes.

* Error runs write typed, numeric-free JSON error envelopes to `stderr` only; successful runs **never** write to `stderr`.

* No mixed streams: a run is either stdout-only success or stderr-only failure.

**Exit codes:**

* `0` on success (canonical JSON body on stdout; stderr empty).

* `64` on usage errors (bad flags/arguments or invalid invocation); on usage error, stdout is empty and diagnostics appear only as a typed error envelope on stderr.

* Other failures use non-zero codes as defined in Governance/CLI specs; stdout remains empty on failure.

*Subtask status:* **Done**

*Epic or card:* **HDE-EPIC020 (D1 — error envelope & token set, PR 1–2b)**

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

 

*Evidence / artifacts (titles/paths only):*

`tests/cli/test_cli_usage_and_errors.py` — CLI error suite that:

* exercises success paths with LF-terminated JSON on stdout and empty stderr,

* covers usage-error cases (missing args, invalid flags) that exit 64 with empty stdout and usage/error text on stderr, and

* covers engine/file/JSON error cases that exit non-zero, write LF-terminated error envelopes to stderr, and leave stdout empty.

`tests/cli/test_errors_parity.py::test_http_and_cli_parity` — parity tests that confirm CLI error envelopes for EPIC020 scenarios are aligned with HTTP error envelopes and remain numeric-free under closed rails.

`docs/acceptance_map_epic020.json` — EPIC020 D1 acceptance map binding the tests above to the D1 CLI error slice (token roster validation applies).

`audit/EPIC-020_MANIFEST.json` — EPIC020 manifest entries binding the D1 CLI error slice to the tests above.

Notes: This row is now Done for the EPIC020 D1 CLI slice: stream and exit-code discipline is implemented and tested under closed rails. PF09 does not mint or list unrostered tokens; stderr-only discipline is a behavioral requirement and must not be represented by a non-roster token in PF09.

### **Subtask HDE-SEPA002.7 — Writers/errors headers posture validation**

**Subtask ID:** HDE-SEPA002.7

**Subtask name/label:** Writers/errors header posture proofs

**Subtask description:**  
 Prove that when the error envelope appears on writers/errors routes, response headers match Governance:

* `Cache-Control: no-store`

* No `ETag`

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — writers/errors header posture, PR 2b)**

**Tokens:**

Header posture tokens (names live in Governance).

**Evidence / artifacts:**

`tests/transport/headers/no_store_writers_errors.snap` — governed snapshot for writer/error success and error cases.

`tests/transport/test_writers_errors_headers.py` — enforcement test wiring the snapshot to the diagnostic writer route under closed rails.

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 acceptance entries that reference the snapshot and tests as header posture evidence.

**Notes:**  
 This row is now Done for the EPIC020 D1 writer diagnostic route; broader A7 transport behavior and other success routes remain governed by A7/Catalog and Distillation tasks.

### **Subtask HDE-SEPA002.8 — Error-envelope evidence & indexing**

**Subtask ID:** HDE-SEPA002.8

**Subtask name/label:** Error evidence families & indexing

**Subtask description:**  
 Maintain and index error-envelope evidence families:

* `errors/token_map` — canonical token→message snapshot (golden).

* `errors/schema_check` — JSON-Schema validation logs for error-envelope shape.

* `errors/canonical_check` — encoding/key-order/compact/LF proof for error envelopes.

* `parity/errors_reader_cli` — Reader↔CLI byte-equality and parity proofs for governed error scenarios.

List all in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; each record includes a `proof_anchor` to a co-located path\_proof transcript).

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D1 — error envelope & token set, PR 2b)**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`  
 `EVIDENCE_INDEX_MIRROR_OK`  
 `EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`errors/token_map/token_map.json` — error token map snapshot with governed path proof; artifact key `ERROR_TOKEN_MAP_V1` in the Evidence Index/Mirror.

`errors/schema_check/error_envelope_invalid_*.log` — error envelope schema-check logs with governed path proofs; artifact key family `ERROR_SCHEMA_CHECK_V1`.

`errors/canonical_check/error_envelope_*` — canonicalization logs for error envelopes (encoding/key-order/compact/LF), referenced by the EPIC020 acceptance map.

`parity/errors_reader_cli.{scenario}.http.json` and `.cli.txt` — HTTP and CLI parity artifacts for D1 error scenarios, each with governed path-proofs; artifact key family `ERRORS_READER_CLI_PARITY_V1`.

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — Human Index and hash sentinel entries for the error evidence families above.

`artifacts/evidence_index.jsonl` — Machine Mirror records for the error artifact keys, including `proof_anchor` references to their path-proofs.

`tests/evidence/test_evidence_skeleton.py` / `tests/ops/test_evidence_index.py` — skeleton and Index/Mirror tests that exercise the new error artifact keys.

`docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — EPIC020 D1 entries marking `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK` as **DONE** for the error evidence slice and binding them to the error skeleton tests and artifacts.

**Notes:**  
 This subtask is now Done for the EPIC020 D1 error evidence slice: the governed error artifacts live in the same Evidence Index/Mirror skeleton as sampler/core artifacts, have path-proofs, and are covered by skeleton tests. Future error evidence families (for new scenarios or epics) will extend, not replace, these entries and are tracked by their owning epics and PF12.

## **Task HDE-SEPA003 — Public Presenter / Emitter**

**Task ID:** HDE-SEPA003

**Task name/label:** Public Presenter / Emitter

**Task description:**  
 Ensure Reader and CLI share a single allow-listed presenter/emitter symbol, emit canonical JSON, enforce stream discipline, satisfy ABBA/two-run identity, and prove the preimage flow with indexed evidence.

**Task status:** **Partial**

**Task notes:**

EPIC017/EPIC018 D1 established the canonical serializer, determinism harness, and CLI serializer guards (AB↔BA and two-run identity, Reader↔CLI parity, preimage recompute, and AST-based serializer/ emitter guards under `artifacts/cli/guards/**`). EPIC020 D2 (“Public Presenter / Emitter”) extends this by:

* Centralizing governed public JSON emission behind `engine.presenter.emitter` so that Reader/compat HTTP routes and `hdctl showcompat` all call a single allow-listed emitter and canonical serializer, with no remaining ad-hoc `json.dumps` paths on governed surfaces.

* Adding a presenter harness (`tools/presenter/generate_presenter_artifacts.py`) that runs under closed rails and writes deterministic presenter artifacts under `artifacts/presenter/**` (AB/BA showcompat bytes, Reader/CLI parity bytes, preimage recompute logs, and a showcompat identity summary), registered via PRESENTER\_\* artifact\_keys in the Evidence Index and Machine Mirror.

* Wiring EPIC020 D2 tokens (`CLI_SHOWCOMPAT_CANON_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `PREIMAGE_RECOMPUTE_OK`) to CLI presenter tests and presenter artifacts in `docs/acceptance_map_epic020.json` and `audit/EPIC-020_MANIFEST.json`, where they are now marked **DONE**.

From PF09’s perspective, the presenter/emitter slice for Reader and `hdctl showcompat` is now fully wired and evidenced. The row remains **Partial** because compat/app-level test flows and any future presenter surfaces are still tracked under Conjunction-phase tasks (`HDE-CONJ002`, `HDE-CONJ003`); PF09 treats those as separate jobs to be closed before the overall presenter story is fully Done.

---

### **Subtask HDE-SEPA003.1 — Single shared presenter/emitter symbol**

**Subtask ID:** HDE-SEPA003.1

**Subtask name/label:** Shared emitter entrypoint

**Subtask description:**  
 Ensure Reader and CLI both call the **same** presenter/emitter entrypoint symbol, enforced via a CI allow-list and guard tools, so test harnesses and production both use the canonical presenter/emitter for public bytes.

**Subtask status:** **Done**

**Epic or card:**  
 HDE-EPIC020 (D2 — Public Presenter / Emitter, PR 3\)  
 EPIC-017 / EPIC-018 (D1 canonical serializer \+ D3 CLI guards, context only)

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`  
 `CLI_NO_ALT_JSON_OK`

**Evidence / artifacts:**

Guard tools and tests (titles-only; single home in Calcination subtasks):

* `tools/cli/serializer_grep_guard.py` — AST/grep guard for disallowed serializers on governed CLI paths.

* `tools/cli/emitter_symbol_proof.py` — emitter symbol proof for governed CLI handlers (including `showcompat`), listing handler→emitter mappings.

* `tests/cli/test_serializer_guards.py` — guard test module exercising both tools in clean and synthetic violation scenarios.

Guard artifacts (governed homes):

* `artifacts/cli/guards/serializer_grep_guard.log`

* `artifacts/cli/guards/emitter_symbol_proof.txt`

* Co-located `*.path_proof.txt` transcripts for both guard logs.

Index/Mirror records:

* `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` — Human Index entries for CLI guard artifacts.

* `artifacts/evidence_index.jsonl` — Machine Mirror records for CLI guard artifacts with `proof_anchor` set to the corresponding path-proofs (mirror discipline per PF09 front matter and PF12).

EPIC020 acceptance wiring (titles-only):

* `docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — D2 entries recording `CLI_READER_EMITTER_PARITY_OK` and `CLI_NO_ALT_JSON_OK` as **DONE** for the presenter slice, listing serializer guard tests and guard artifacts as evidence.

Notes:  
 This subtask is scoped to ensuring that governed Reader/compat HTTP routes and `hdctl showcompat` all use the same allow-listed presenter/emitter symbol as production, enforced by guard tools and tests. Compat-surface AB/BA parity and identity hashing (HDE-CONJ002) remain separate rows.

---

### **Subtask HDE-SEPA003.2 — Canonical JSON & non-empty showcompat**

**Subtask ID:** HDE-SEPA003.2

**Subtask name/label:** Canonical showcompat output

**Subtask description:**  
 Prove that `showcompat` emits non-empty, LF-terminated canonical JSON via the presenter/emitter:

* UTF-8 (no BOM).

* Compact JSON with exactly one trailing LF.

* Canonical key ordering and arrays-as-sets semantics enforced by the canonical serializer.

* Bytes on stdout exactly match `engine.presenter.emitter.emit_public` for the same payload.

**Subtask status:** **Done**

**Epic or card:**  
 HDE-EPIC020 (D2 — Public Presenter / Emitter)

**Tokens:**

`CLI_SHOWCOMPAT_CANON_OK`  
 `JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

CLI presenter tests (titles-only):

* `tests/cli/test_cli_canonical_bytes.py` — proves `hdctl showcompat` stdout is canonical JSON, LF-terminated, non-empty, and byte-identical to `emitter.emit_public(<payload>)`.

* `tests/cli/test_showcompat_parity_and_identity.py` — AB/BA and two-run identity tests for presenter/CLI showcompat, building on the canonical serializer harness.

Presenter harness and artifacts:

* `tools/presenter/generate_presenter_artifacts.py` — closed-rails presenter harness that writes deterministic presenter artifacts under `artifacts/presenter/**` (AB/BA showcompat bytes, Reader/CLI parity bytes, preimage recompute logs, identity summary).

* Presenter artifact families indexed via PRESENTER\_\* artifact\_keys in the Evidence Index and Machine Mirror (titles-only), referenced by EPIC020 D2 acceptance metadata.

EPIC020 acceptance wiring:

* `docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — D2 entries marking `CLI_SHOWCOMPAT_CANON_OK` as **DONE** with the canonical-bytes and identity tests above and the presenter artifacts listed as evidence.

---

### **Subtask HDE-SEPA003.3 — Streams discipline for presenter flows**

**Subtask name/label:** streams discipline (stdout/stderr)

**Subtask description:**  
 For presenter-driven CLI flows:

* Success payloads emit to stdout only (stderr empty).

* Errors emit to stderr only (stdout empty).

* No logs ever mix into the stdout payload stream.

* Errors are typed, numeric-free error envelopes on stderr only.

**Subtask status: Done**

**Epic or card:** EPIC-022 (T4)

**Tokens:**  
 `CLI_STDOUT_LF_OK`

**Evidence / artifacts:**

* `tests/cli/test_cli_canonical_bytes.py` (asserts stdout-only payload \+ stderr empty for showcompat)

* `tests/cli/test_cli_usage_and_errors.py` (asserts stderr-only failures / stdout empty on error)

* `tools/cli/showcompat.py` (canonical CLI path)

* `artifacts/cli/showcompat/*` (governed CLI artifacts; stdout payload)

**Notes:**  
 Codex Audit HDE-EPIC024 reports stream discipline is implemented and enforced by CLI tests (stdout-only success; stderr-only failure) for the governed showcompat surface; treat this subtask as Done.

IMPORTANT: Do not use or cite the token `CLI_STDERR_ONLY_ON_ERROR_OK` — it is forbidden/obsolete and does not exist.

DEFERRED \-\> BACKLOG: Consolidate evidence ownership closure (artifacts \+ QA logs) into EPIC024 close report / doc delta entry.

---

### **Subtask HDE-SEPA003.4 — AB↔BA and two-run identity for presenter**

**Subtask ID:** HDE-SEPA003.4

**Subtask name/label:** ABBA/two-run parity for presenter surfaces

**Subtask description:**  
 Re-prove that on presenter parity flows:

* `(A,B)` vs `(B,A)` produce identical public bytes (AB↔BA).

* Two runs with identical inputs produce bitwise-identical public bytes for showcompat and presenter parity samples.

**Subtask status:** **Done**

**Epic or card:**  
 HDE-EPIC020 (D2 — Public Presenter / Emitter)

**Tokens:**

`TWO_RUN_IDENTITY_OK`  
 `COMPOSITE_ABBA_IDENTITY_OK`

**Evidence / artifacts:**

Presenter/CLI identity tests:

* `tests/cli/test_showcompat_parity_and_identity.py` — AB/BA parity and two-run identity checks for showcompat under closed rails.

* `tests/cli/test_cli_canonical_bytes.py` — canonical bytes assertions reused for identity proofs.

Presenter artifacts (titles-only):

* AB and BA presenter bytes for showcompat and Reader/CLI parity cases under `artifacts/presenter/**`, as recorded in the Evidence Index and Machine Mirror.

* Presenter identity summary artifact capturing AB↔BA and two-run hashes for showcompat runs.

EPIC020 acceptance metadata:

* `docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — D2 entries marking `TWO_RUN_IDENTITY_OK` and `COMPOSITE_ABBA_IDENTITY_OK` as **DONE** for the presenter slice, binding them to the parity/identity tests and presenter artifacts above.

---

### **Subtask HDE-SEPA003.5 — Preimage recompute & identity coupling**

**Subtask ID:** HDE-SEPA003.5

**Subtask name/label:** Preimage recompute & identity proof

**Subtask description:**  
 Prove that preimage hashing (`idempotence_hash`) and identity coupling (for example `release_id`) are correct by recomputing preimage/digests from the presenter preimage logs and comparing against emitted bytes.

**Subtask status:** **Done**

**Epic or card:**  
 HDE-EPIC020 (D2 — Public Presenter / Emitter)

**Tokens:**

`PREIMAGE_RECOMPUTE_OK`

**Evidence / artifacts:**

* Presenter preimage recompute logs under `artifacts/presenter/**` written by the presenter harness.

* CLI/Reader preimage recompute checks in `tests/cli/test_showcompat_parity_and_identity.py` that recompute hashes and compare against stored digests and envelopes.

* EPIC020 D2 acceptance entries associating `PREIMAGE_RECOMPUTE_OK` with the presenter preimage logs and identity tests.

---

### **Subtask HDE-SEPA003.6 — Presenter evidence indexing**

**Subtask ID:** HDE-SEPA003.6

**Subtask name/label:** Presenter evidence & indexing

**Subtask description:**  
 Index presenter/emitter evidence artifacts in the Human Evidence Index and Machine Mirror in the same PR (records-only; with path-proofs), following global Evidence Index & mirror rules.

**Subtask status:** **Done**

**Epic or card:**  
 HDE-EPIC020 (D2 — Public Presenter / Emitter)

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`  
 `EVIDENCE_INDEX_MIRROR_OK`  
 `EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

* Presenter artifact families under PRESENTER\_\* artifact\_keys in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` (titles-only), with `proof_anchor` values pointing to co-located `*.path_proof.txt` files.

* Evidence skeleton tests (`tests/evidence/test_evidence_skeleton.py`, `tests/ops/test_evidence_index.py`) extended to cover the presenter artifact families for EPIC020 D2.

* `docs/acceptance_map_epic020.json` / `audit/EPIC-020_MANIFEST.json` — D2 entries marking `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK` as **DONE** for the presenter slice, binding them to the presenter artifact skeleton and tests.

---

## **Task HDE-SEPA004 — Internal Ops Surface /internal/version**

**Task ID:** HDE-SEPA004

**Task name/label:** Internal Ops Surface /internal/version

**Task description:**  
 Provide an operator-only, side-effect-free `/internal/version` endpoint that exposes engine identity, with no-store/no-ETag headers, HEAD parity, conditionals ignored, and fully indexed evidence.

**Task status:** **Partial**

**Task notes:**

Audit v1 (2025-11-17) originally listed missing `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`, and `INTVER_200_NO_ETAG_OK`, and noted that headers/body proofs were incomplete and no full GET/HEAD/conditional/identity proof set existed. Subsequent work updates that posture:

* EPIC017/EPIC018 QA (see Subtasks HDE-SEPA004.2 and HDE-SEPA004.3) proved conditional-ignore behavior and no-store/no-ETag headers for `/internal/version` on Railway prod, with governed logs under `audit/qa/hde-epic017/logs/**` and tokens `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK` and `INTVER_200_NO_ETAG_OK` marked **Done**.

* EPIC020 D3 (“Internal-ops identity”) adds dev-harness GET/HEAD identity and JSON content-type proofs for `/internal/version`, wiring tokens `INTVER_200_CTYPE_JSON_UTF8_OK` and `INTVER_HEAD_PARITY_OK` to header/body artifacts and Live QA Step 4 logs under `audit/qa/hde-epic020/**` and capturing those identity records in EPIC020 Candidate 1 bundles/manifests integrated into the Evidence Index and Machine Mirror.

From PF09’s perspective, the `/internal/version` ops surface now has:

* no-store/no-ETag posture and conditional-ignore behavior evidenced and indexed (EPIC017/EPIC018), and

* GET/HEAD 200 parity plus JSON content-type identity for the engine/Reader dev harness evidenced and indexed (EPIC020 D3).

The task remains **Partial** because:

* two-run identity and identity/provenance coupling for `/internal/version` across environments (body-shape contract, identity fields vs frozen identity artifacts) are explicitly tracked under **Subtask HDE-SEPA004.4** and EPIC018/prospective Reality Audit work, not EPIC020, and

* future cross-env `/internal/version` audits (e.g., staging/prod replays via PF23 Reality Audits) are intentionally deferred to later epics.

### **Subtask HDE-SEPA004.1 — GET/HEAD 200 parity**

**Subtask ID:** HDE-SEPA004.1

**Subtask name/label:** GET/HEAD header parity

**Subtask description:**  
 Implement HEAD parity for `/internal/version`:

`GET` returns 200 with JSON body.

`HEAD` returns 200, mirrors GET validators (including `Content-Type`), has no body, and `Content-Length == len(identity GET body)`.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC020 (D3 — `/internal/version` identity)**

**Tokens:**

`INTVER_200_CTYPE_JSON_UTF8_OK`

`INTVER_HEAD_PARITY_OK`

**Evidence / artifacts:**

`artifacts/ops/internal_version/headers_get.txt` — headers \+ status for `/internal/version` GET under pinned rails (JSON content type, no-store, no ETag).

`artifacts/ops/internal_version/headers_head.txt` — headers \+ status for `/internal/version` HEAD under pinned rails (200, matching validators including `Content-Type`, no body, `Content-Length == len(identity GET body)`).

`artifacts/ops/internal_version/body_get.json` — canonical JSON body for `/internal/version` GET under determinism pins (UTF-8, sorted keys, compact, one LF).

`artifacts/ops/internal_version/body_get.sha256` — sha256 over canonical `body_get.json` bytes for identity coupling.

EPIC020 D3 Live QA Step 4 logs under `audit/qa/hde-epic020/**` (titles-only) — dev-harness `/internal/version` GET/HEAD captures showing the same content-type and validator parity as the ops proofs, run under `APP_ENV=dev` with SAFE rails and env pins, as described in PF10 EPIC020 D3 QA addenda and the Dev Retrospective.

EPIC020 Candidate 1 bundles/manifests in `artifacts/epic020/bundles/*.bundle.json` / `*.manifest.json` — identity records tying `/internal/version` JSON to ops identity families and EPIC020 D3 tokens, integrated into the Evidence Index and Machine Mirror per PF12/PF09 evidence-bundle rules (titles-only).

### **Subtask HDE-SEPA004.2 — Conditionals ignored (never 304\)**

Subtask ID: HDE-SEPA004.2

Subtask name/label: Conditional-ignore behavior

Subtask description:  
 Ensure that `/internal/version` ignores conditional headers and never returns 304:

Requests with `If-None-Match` or `If-Modified-Since` still return 200 with the same body and headers as an ordinary GET.

Subtask status: Done

Epic or card: EPIC-017 (QA01 conditional GET verification)

Tokens:

INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK

Evidence / artifacts:

audit/qa/hde-epic017/logs/intver\_get\_conditional.txt — conditional GET `/internal/version` with `If-*` headers showing 200 OK, `Cache-Control: no-store`, no `ETag`/`Last-Modified`, and a JSON body identical to the non-conditional GET.

audit/qa/hde-epic017/logs/intver\_get\_full.txt — baseline non-conditional GET `/internal/version` headers/body for comparison.

audit/qa/hde-epic018/logs/qa\_dir\_casing\_normalization\_summary.md — QA01 review summary documenting that all EPIC017 Live QA logs for `/internal/version` (GET/HEAD/conditional) were moved from the legacy `Audit/QA/HDE-EPIC017/logs/` tree into the canonical `audit/qa/hde-epic017/logs/`root; path-only/doc-only remediation, tests explicitly “Not run (not requested)”.

Notes:  
 This QA evidence demonstrates that `/internal/version` ignores conditional headers for GET and never returns 304, while preserving header posture and body equality relative to non-conditional GET. The later QA01 casing normalization step only updated directory names and references; it did not change the observed behavior or acceptance tokens for this subtask. The remaining open work for `/internal/version` (body-shape contract and identity/two-run proof) is tracked at the task level and in other subtasks, not here.

### **Subtask HDE-SEPA004.3 — No-store & no ETag posture**

Subtask ID: HDE-SEPA004.3

Subtask name/label: No-store, no ETag headers

Subtask description:  
 Maintain ops-surface posture for `/internal/version`:

`Cache-Control: no-store`

No `ETag` header

No caching validators (no `Last-Modified`).

Subtask status: Done

Epic or card: EPIC-017 (QA01 conditional GET verification)

Tokens:

INTVER\_200\_NO\_ETAG\_OK

Evidence / artifacts:

audit/qa/hde-epic017/logs/intver\_get\_full.txt — GET `/internal/version` showing 200 OK, `Cache-Control: no-store`, JSON content type, and no `ETag`/`Last-Modified` headers.

audit/qa/hde-epic017/logs/intver\_head\_full.txt — HEAD `/internal/version` showing 200 OK, matching validators (including `Content-Type`) and no `ETag`/`Last-Modified`, with no body.

audit/qa/hde-epic017/logs/intver\_get\_conditional.txt — conditional GET `/internal/version` with `If-*` headers showing the same header posture (no-store, no validators, JSON content type) as the ordinary GET.

Notes:  
 Together, these artifacts show that `/internal/version` consistently uses `Cache-Control: no-store` and omits `ETag` and `Last-Modified` for GET, HEAD, and conditional GET in Railway prod. Directory casing normalization for the EPIC017 QA logs is recorded in the EPIC018 QA summary listed above; it does not alter the header posture proofs captured here. Body-shape compliance (adding `invocation_sha256`, frozen field order) is still outstanding and is handled by other tasks; this subtask is scoped only to header posture.

### **Subtask HDE-SEPA004.4 — Two-run identity & identity coupling**

The body values for `engine_tag`, `release_id`, `invocation_tag`, `build_commit`, `emitter_sha256`, and any additional identity fields required by the Identity and Provenance module match the frozen identity artifacts for this release (pack manifest, `release_id` artifacts, emitter hash, and service identity snapshot).

Subtask status: **Done**

Epic or card: **HDE-EPIC022** (D3 — `/internal/version` coupling proof \+ evidence bundle)

Tokens:

Supports `TWO_RUN_IDENTITY_OK` for identity components (token semantics live in Governance and Mechanics; PF09 is consumer-only).

Evidence / artifacts:

`artifacts/ops/internal_version/two_run_identity.log` — governed coupling \+ two-run identity proof log (D3 proof artifact).

Internal\_version bundle artifacts (governed):

`artifacts/ops/internal_version/body_get.json`  
 `artifacts/ops/internal_version/body_get.sha256`  
 `artifacts/ops/internal_version/headers_get.txt`  
 `artifacts/ops/internal_version/headers_head.txt`  
 `artifacts/ops/internal_version/headers_cond_if_none_match.txt`  
 `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`  
 `artifacts/ops/internal_version/request_chain_manifest.json`  
 plus the corresponding `*.path_proof.txt` files for governed bundle artifacts (where present).

Acceptance binding surfaces (names-only; content governed elsewhere):

`audit/qa/hde-epic022/token_evidence_matrix.md`  
 `docs/acceptance_map_epic022.json`

Evidence Index \+ Machine Mirror (same-PR parity; paths pinned in PF09 §0.3):

`docs/evidence/INDEX.json`  
 `docs/evidence/INDEX.sha256`  
 `artifacts/evidence_index.jsonl`

Notes:

* EPIC022 D3.1 is recorded as PASS with required predicates satisfied, including two-run identity and explicit coupling verification (including `release_id` coupling to `artifacts/math/release_id.txt`).

* Conditional header filenames are PF12-canonical (`headers_cond_if_*`) and are the indexed targets.

* Non-blocking caveat: `headers_head.txt` may contain a curl warning line; any parser/verifier must ignore non-header lines (non `key: value` lines).

### **Subtask HDE-SEPA004.5 — Internal ops evidence indexing**

**Subtask ID:** HDE-SEPA004.5

**Subtask name/label:** /internal/version evidence & indexing

**Subtask description:**  
 Index all `/internal/version` artifacts and related identity artifacts in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; with path-proofs).

**Subtask status:** **Done**

**Epic or card:** HDE-EPIC022 (D3 — `/internal/version` evidence bundle indexing \+ validator hardening)

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`  
 `EVIDENCE_INDEX_MIRROR_OK`  
 `EVIDENCE_INDEX_HASH_OK`  
 `MACHINE_MIRROR_UPDATED_OK`  
 `EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

Index \+ mirror updates (same PR):

`docs/evidence/INDEX.json`  
 `docs/evidence/INDEX.sha256`  
 `docs/evidence/INDEX.json.path_proof.txt`  
 `docs/evidence/INDEX.sha256.path_proof.txt`  
 `artifacts/evidence_index.jsonl`  
 `artifacts/evidence_index.jsonl.path_proof.txt`

Internal\_version governed artifacts that must be indexed/mirrored (canonical filenames):

`artifacts/ops/internal_version/body_get.json`  
 `artifacts/ops/internal_version/body_get.sha256`  
 `artifacts/ops/internal_version/headers_get.txt`  
 `artifacts/ops/internal_version/headers_head.txt`  
 `artifacts/ops/internal_version/headers_cond_if_none_match.txt`  
 `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`  
 `artifacts/ops/internal_version/two_run_identity.log`  
 `artifacts/ops/internal_version/request_chain_manifest.json`  
 plus co-located `*.path_proof.txt` files for the governed artifacts above (where present).

Acceptance binding surfaces:

`audit/qa/hde-epic022/token_evidence_matrix.md`  
 `docs/acceptance_map_epic022.json`

Validator hardening evidence (titles-only; canonical homes elsewhere):

* Evidence-index update \+ `--check` outputs and pytest logs produced by the D3.2 step bundle under `audit/qa/hde-epic022/` (step log \+ results \+ snapshots).

**Notes:**

* EPIC022 D3.2 is recorded as PASS and includes explicit validation outputs (index write, index check, pytest suites, and mirror schema check).

* D3.2 includes an explicit “canonical conditionals present” check confirming `headers_cond_if_none_match.txt` and `headers_cond_if_modified_since.txt` are present in the governed evidence indices (missing: \[\]).

* PR03 ensures `request_chain_manifest.json` is tracked in the Machine Mirror with a `proof_anchor` pointing to `request_chain_manifest.json.path_proof.txt`.

* Governance reminder (evidence binding hygiene): `*.path_proof.txt` files are required deliverables and must be validated via `proof_anchor`/mirror discipline, but token/evidence bindings must not cite `*.path_proof.txt` as primary evidence titles.

---

# **Phase IV — Conjunction (Surfaces and tools meet the core)**

**Phase description:**  
 Wire dev/test HTTP harnesses, compat and Reader public surfaces, CLI surfaces and tooling, and writer APIs to the deterministic engine core, enforcing canonical JSON, A7 transport posture, and Index/Mirror discipline.

**Phase master status:** **Partial**

**Done:** Dev HTTP Harness (single home)

**Not done:** Compat Surface (internal), CLI Serializer Coupling, CLI Conformance, Reader Surface (API), Caching & Transport Wiring (Reader), CLI Tooling (showcompat, sample), Writer Surfaces (API), Global discipline

**Notes:**

Many tasks in this phase share artifacts and tokens (especially CLI and Reader A7/A8 surfaces). This structure keeps them trackable as separate checklist rows while acknowledging shared evidence.

---

## Task HDE-CONJ001 — Dev HTTP Harness (single home)

**Task ID:** HDE-CONJ001

**Task name/label:** Dev HTTP Harness (single home)

**Task status:** **Done**

**Task description:**  
 Provide a single dev/QA HTTP harness for end-to-end validation of the Engine that exercises Reader/CLI surfaces without being a production surface, enforces no-store and canonical JSON, and maintains evidence and Index/Mirror entries.

**Task notes:**

Single home for local/QA validation of the Engine: end-to-end HTTP runs that exercise the Reader/CLI surfaces without being production surfaces.

Defaults:

`Cache-Control: no-store` on all harness responses.

Never exposes SR/XR numerics or other internal scores in public JSON.

Runs under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Supplemental only:

Authoritative A7 proofs live on the Catalog JSON success route.

Harness may call the same emitter and logic; A7 acceptance is driven by Catalog route artifacts and tokens.

PF09 is consumer-only; token semantics and schemas live in Governance/CLI/Schemas.

### **Subtask HDE-CONJ001.1 — Harness behavior & non-production posture**

**Subtask name/label:** Harness behavior & non-production posture

**Subtask description:**  
 Ensure the dev HTTP harness is the single home for local/QA Engine validation and remains strictly non-production:

**Dev-only posture.**

Bound only to loopback (for example `127.0.0.1`) and not exposed as a public surface.

CORS disabled for harness routes.

Runs with `APP_ENV=dev` when capturing evidence; debug reloader is OFF during evidence runs.

**Response and payload posture.**

Uses `Cache-Control: no-store` on all harness responses.

Never exposes SR/XR numerics or other internal scores in JSON outputs.

Emits canonical JSON via the shared presenter/emitter (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and sorted), under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

PF09 does not pin the exact set of dev routes or curl commands; those remain documented in Mechanics and CLI/API docs by title. This subtask requires that the harness be dev-only, loopback-bound, canonical, and non-public when used for evidence.

**Subtask status:** **Done** (behavioral target; evidence already exists for current harness)

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (rails, transport, and canonical JSON tokens live in Governance and other tasks; PF09 is consumer-only here)

**Evidence / artifacts:**

`tests/harness/test_end_to_end.py` (behavioral tests that exercise Reader/CLI surfaces through the harness)

### Subtask HDE-CONJ001.2 — Harness parity & canonicalization

**Subtask name/label:** Harness parity with CLI & canonical JSON

**Subtask description:**  
 Prove that the harness:

Matches CLI behavior for supported flows (harness parity with CLI).

Exhibits AB↔BA parity on compat payloads for pair inputs.

Passes canonicalization checks (canonical JSON, LF-termination, sorted keys, arrays-as-sets deduped and sorted).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (token semantics are referenced only by title)

**Evidence / artifacts:**

`audit/gates/parity/*.bytes`

`audit/gates/canonical_json/*.log`

### Subtask HDE-CONJ001.3 — Harness evidence indexing

**Subtask name/label:** Harness Evidence Index & Machine Mirror

**Subtask description:**  
 Index harness evidence in the human Evidence Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

**Subtask status:** **Done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-CONJ001.4 — Dev/internal HTTP harness infra wiring**

**Subtask name/label:** Dev/internal HTTP harness infra wiring

**Subtask description:**  
 Ensure that any **internal/dev HTTP harness** intended for QA or evidence flows (including, but not limited to, `POST /internal/dev/sampler`) has infra-owned start commands and URLs, so QA and PO are never guessing hosts, ports, or paths:

* **Infra-owned dev start command / service definition.**  
   Infra/ops MUST provide and maintain a canonical dev start command or service definition that runs the Reader process in dev/Codespaces (and other dev environments) with `APP_ENV` set by the caller and the determinism rails required by Mechanics and Governance (titles-only). PF09 does not pin the exact command; it requires that such a command or service definition exist, be documented, and be used when exercising internal/dev HTTP harnesses.

* **Base URL and `DEV_SAMPLER_URL` per environment (infra-owned).**  
   For each environment where an internal/dev HTTP harness is expected to be used (at minimum Codespaces and local dev), infra/ops MUST derive and publish a concrete **base URL** for the dev Reader process (for example `http://127.0.0.1:<port>` in local dev or the appropriate forwarded port in Codespaces) and from that base URL define a concrete sampler harness URL:

   `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler`

   `DEV_SAMPLER_URL` (and any similar dev harness URLs) MUST be treated as an **infra-owned configuration value**:

  * QA plans and documentation agents MUST consume `DEV_SAMPLER_URL` (or an equivalent infra-exposed binding) as an input and MUST NOT guess hostnames, ports, or full URLs for `/internal/dev/sampler`.

  * Any change to the underlying dev Reader binding (host or port) MUST be reflected by infra in the published `DEV_SAMPLER_URL` value; QA and docs do not hard-code ports or recompute URLs independently.

  * Mechanics does not pin where `DEV_SAMPLER_URL` lives (env var, config file, devcontainer config); it requires that there is a **single infra-owned binding** for `/internal/dev/sampler` per environment and that QA/PO treat it as the authority for that harness URL.

* **Codespaces dev: canonical home and value.**  
   For the Codespaces dev environment:

  * The **canonical home** for `DEV_SAMPLER_URL` MUST be the devcontainer configuration (for example a `containerEnv` block in `.devcontainer/devcontainer.json`); every shell in the Codespace MUST see the same default value without manual export.

  * The devcontainer binding MUST set `DEV_SAMPLER_URL` to the base URL derived from the dev Reader helper: for the current EPIC019 D3 wiring this is `http://127.0.0.1:8000/internal/dev/sampler`. Note: Shell-level overrides `export DEV_SAMPLER_URL=<DEV_SAMPLER_URL_OVERRIDE>` MAY be used for debugging but MUST NOT be used to justify omitting the `dev_sampler_url` field from canonical public results.

  * Dev sampler HTTP harnesses (healthcheck and D3 Live QA) MUST NOT reconstruct host/port internally or hardcode `DEV_SAMPLER_URL`; they MUST read it from the environment and treat any mismatch with the actual Reader binding as a tooling/infra issue.

* **Infra validation of dev harness URLs before QA.**  
   Before handing any `DEV_SAMPLER_URL` (or similar dev harness URL) to QA or using it in QA plans, infra/ops MUST validate it locally by:

  * Running the infra-owned dev Reader start command with determinism pins and a chosen `APP_ENV` (for example `APP_ENV=dev` for allowed-mode checks) using the same env rails described elsewhere in this checklist and in the Glow QA Guide by title (for example `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` for evidence runs).

  * Issuing at least one simple HTTP/1.1 `POST` to `DEV_SAMPLER_URL` with:

    * `Content-Type: application/json; charset=utf-8`, and

    * a minimal, schema-valid request body for the sampler harness (for example a non-empty `viewer_id` and a non-empty array of string `candidate_ids`, with optional `seed` when appropriate).

  * Confirming that the response:

    * uses canonical JSON output and the canonical serializer posture defined elsewhere in this checklist (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF; arrays-as-sets deduped and ASCII-sorted),

    * matches the `POST /internal/dev/sampler` request/response shape defined in CLI/API and Mechanics by title, and

    * carries headers consistent with the internal/dev writer posture for this harness (JSON `Content-Type`; `Cache-Control: no-store` for errors; no `ETag`).

* If this validation fails (for example the URL is unreachable, the response body/headers do not match Mechanics, or JSON is not canonical), infra MUST treat the issue as an **infra/tooling misconfiguration**, correct the wiring, and rerun validation before any QA plan or doc step relies on `DEV_SAMPLER_URL`.

* **Harness behavior when DEV\_SAMPLER\_URL is missing or mismatched.**  
   Dev sampler HTTP harnesses (including the dev sampler healthcheck and the D3 Live QA harness):

  * MUST read `DEV_SAMPLER_URL` directly from the environment and MUST NOT hardcode host/port or reconstruct the URL internally.

  * MUST treat a missing `DEV_SAMPLER_URL` (unset or empty) as a **tooling/infra failure** and fail loudly (non-zero exit code) with a clear log entry indicating that the binding is missing, rather than attempting to fall back to any default.

  * SHOULD treat obvious mismatches between `DEV_SAMPLER_URL` and the actual Reader binding (for example wrong host or port) as tooling/infra failures and log the discrepancy, since such mismatches indicate that infra and harness are out of sync.

  * MUST record the effective `DEV_SAMPLER_URL` value and rails (`APP_ENV`, `SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, `TZ`) in their QA logs under `audit/qa/<epic>/…` so that later audits can see exactly which dev Reader endpoint the harness spoke to and under which rails.

* **Clear responsibility split.**  
   Infra/ops agents are responsible for **defining, maintaining, and validating** dev Reader start commands and dev harness URLs (including `DEV_SAMPLER_URL`) in each environment. PO, QA, and documentation agents **consume** these URLs and MUST NOT define, change, or guess them in PF10, Glow QA Guide, HDE Phased Epics, PF09, or QA plans:

  * If infra has not yet provided a validated `DEV_SAMPLER_URL` for a given environment, this subtask remains **Not done** for that environment and the sampler HTTP harness is not considered ready for Live QA in that environment.

  * QA and PO treat failures to reach or use `DEV_SAMPLER_URL` as **tooling/infra issues** to be escalated back to infra unless there is already a passing infra validation log showing the harness is healthy and subsequent QA evidence clearly attributes a failure to sampler/core behavior.

**Subtask status:** **Partial**

**Epic or card:** **HDE-EPIC019 (D3 — Dev-only sampler HTTP endpoint harness), Remediation PR01/PR02A (dev Reader start command & DEV\_SAMPLER\_URL wiring and APP\_ENV forwarding for Codespaces)**

**Tokens:** **Unknown** (any infra/HTTP harness tokens for dev-only internal surfaces will be defined in Governance, Glow Infrastructure, and Mechanics; PF09 will reference them by title once minted)

**Evidence / artifacts:**

* Infra/ops documentation and dev tooling (titles-only) for **Codespaces dev**:

  * `scripts/dev_start_reader.sh` — canonical dev Reader start script that:

    * pins determinism env pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and `PORT` (default 8000), and

    * **forwards `APP_ENV` from the caller without forcing a default**, exporting `APP_ENV` only when it is present so that harnesses can exercise `APP_ENV=dev`, `APP_ENV=prod`, empty, and unset modes exactly as PF-canon defines.

    * logs `APP_ENV_DISPLAY` in its `[dev-start] APP_ENV=` line so operators and QA can see when `APP_ENV` is unset or empty.

  * `.devcontainer/devcontainer.json` — devcontainer configuration exporting an infra-owned `DEV_SAMPLER_URL` binding (`DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`) for Codespaces dev.

  * `scripts/qa/dev_sampler_healthcheck.py` — healthcheck/diagnostic harness that:

    * reads and validates `DEV_SAMPLER_URL` from the environment,

    * starts the Reader in `APP_ENV=dev` (and in `APP_ENV=prod` or other modes for gating diagnostics) under determinism pins,

    * issues HTTP/1.1 POSTs with a minimal sampler payload, and

    * logs rails and responses (including the effective `DEV_SAMPLER_URL` value) without modifying sampler behavior.

  * `tests/scripts/test_dev_sampler_healthcheck.py` — pytest that runs the healthcheck harness against a local Reader binding, asserts a 200 dev response, and checks for expected log lines (for example a `sampler_response mode=dev` marker) to prove infra validation is wired and test-covered.

* QA-facing configuration such as `DEV_SAMPLER_URL` bindings (titles-only) that are derived from infra-owned base URLs and ports, not guessed by QA.

* Infra or QA logs (titles-only) showing successful local validation POSTs to `DEV_SAMPLER_URL` in Codespaces dev, demonstrating:

  * `APP_ENV=dev` and determinism env pins where applicable.

  * Canonical JSON request/response bodies and correct sampler schema for dev runs.

  * Headers consistent with HDE-CLI-API-Vendor-Ref and HDE-Mechanics Guide internal/dev HTTP behavior.

* D3-specific QA logs (titles-only) under `audit/qa/hde-epic019/dev_sampler_http/` that:

  * record the effective `DEV_SAMPLER_URL` used for the dev sampler Live QA harness, and

  * capture the rails snapshot (`SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`) alongside request/response details, so D3 evidence clearly ties behavior to the configured endpoint and rails posture.

* Evidence Index and Machine Mirror entries for dev harness validation artifacts, once they are governed and indexed (titles/paths only); PF09 does not restate mirror schema.

**Notes:**  
 This subtask reflects the split between **infra wiring** and **behavioral gating** for the dev sampler HTTP harness. For EPIC019:

* Codespaces dev now has a canonical dev Reader start command that no longer overrides `APP_ENV`, a single infra-owned `DEV_SAMPLER_URL` binding via the devcontainer, and a healthcheck harness and pytest that validate the dev sampler HTTP harness behavior under `APP_ENV=dev`; these satisfy the infra/validation slice of this subtask for that environment.

* APP\_ENV gating for forbidden modes (for example `APP_ENV=prod`, empty, unset) remains a behavioral responsibility of the adapter and Mechanics; forwarding `APP_ENV` unchanged and treating missing/mismatched `DEV_SAMPLER_URL` as a tooling failure make those modes **testable** by Live QA harnesses instead of being silently remapped to dev. Once gating behavior is corrected and similar infra wiring exists for other environments (for example non-Codespaces local dev), this subtask can be revisited and moved from **Partial** to **Done**.

---

## Task HDE-CONJ002 — Compat Surface (internal)

**Task ID:** HDE-CONJ002

**Task name/label:** Compat Surface (internal)

**Task status:** **Not done**

**Task description:**  
 Implement an internal-only compat surface using the shared presenter/emitter, with canonical JSON, AB↔BA parity (including Integration channels), and identity\_hash capture, and index its evidence.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

Missing tokens (titles-only; tokens live in Governance/Schemas):

`CATEGORY_FRAMEWORK_OK`

`AB_BA_PARITY_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

No Magic-10 key table or compat parity logs recorded for this internal surface.

Internal endpoint for pair-compat emission and QA; not a public product surface.

Uses the same presenter/emitter as Reader/CLI.

Never exposes SR/XR numerics on Reader; any CLI-only diagnostic sidecar is flag-guarded and admin-only.

### Subtask HDE-CONJ002.1 — Compat endpoint semantics

**Subtask name/label:** Internal compat endpoint behavior

**Subtask description:**  
 Maintain an internal endpoint for pair-compat emission and QA that:

Uses the shared presenter/emitter.

Is not a public product surface.

Never exposes SR/XR numerics on Reader; CLI diagnostics (if any) are flag-guarded and admin-only.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown**

**Evidence / artifacts:**

Endpoint implementation and tests (paths not pinned here).

### Subtask HDE-CONJ002.2 — Canonical compat JSON & parity

**Subtask name/label:** Canonical compat output & ABBA parity

**Subtask description:**  
 Ensure internal compat responses:

Are canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays-as-sets deduped and sorted.

Obey AB↔BA parity on the full compat body, including Integration channel cases (e.g. `20–34` vs `20–57`).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CATEGORY_FRAMEWORK_OK`

`AB_BA_PARITY_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`tests/compat/test_abba_parity.py`

### Subtask HDE-CONJ002.3 — identity\_hash capture

**Subtask name/label:** identity\_hash for compat payloads

**Subtask description:**  
 Capture `identity_hash` for compat payloads as sha256 over the LF-terminated compat body for internal/admin evidence.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`AB_BA_PARITY_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/compat/identity_hash.txt`

### Subtask HDE-CONJ002.4 — Compat evidence indexing

**Subtask name/label:** Compat surface Evidence Index & mirror

**Subtask description:**  
 Index compat artifacts (`artifacts/compat/identity_hash.txt`, `tests/compat/test_abba_parity.py`) in the human Evidence Index and machine mirror in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-CONJ003 — CLI Serializer Coupling

**Task ID:** HDE-CONJ003

**Task name/label:** CLI Serializer Coupling

**Task status:** **Not done**

**Task description:**  
 Ensure CLI, Reader, and compat flows in tests all use the same presenter/emitter symbol as production, enforce an allow-list of emitters, and prove parity/determinism and absence of ad-hoc JSON via grep/symbol proofs and evidence.

**Task notes:**

**Status (Audit v1 — 2025-11-17).**

Test harnesses that exercise public JSON (Reader, CLI, compat) MUST call the same presenter/emitter symbol used in production.

No test-only serializers or bypass paths allowed for public bytes.

Maintain an explicit allow-list of presenter/emitter symbols; CI must enforce it and keep grep/symbol proofs consistent.

Missing tokens (titles-only):

`CLI_READER_EMITTER_PARITY_OK`

`CLI_NO_ALT_JSON_OK`

`CLI_SHOWCOMPAT_CANON_OK`

`TWO_RUN_IDENTITY_OK`

Grep/symbol proof artifacts not yet recorded.

Reader and CLI share one emitter:

CLI Reader surfaces (stdout or `--dump-reader`) must be byte-identical to the Reader body.

No ad-hoc serializers on public paths; guarded via grep and import-graph symbol proofs.

### Subtask HDE-CONJ003.1 — Shared emitter in tests

**Subtask name/label:** Test harness uses production presenter/emitter

**Subtask description:**  
 Ensure all test harnesses that exercise public JSON (Reader, CLI, compat) call the same presenter/emitter symbol used in production; no test-only serializers or bypass paths permitted.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`

`CLI_NO_ALT_JSON_OK`

**Evidence / artifacts:**

`tests/test_emitter_determinism.py`

### Subtask HDE-CONJ003.2 — Emitter allow-list & grep/symbol proofs

**Subtask name/label:** Emitter allow-list enforcement

**Subtask description:**  
 Maintain and enforce an explicit allow-list of presenter/emitter symbols for public bytes; CI uses grep/symbol proofs to ensure only allow-listed symbols serialize public bytes.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CLI_NO_ALT_JSON_OK`

**Evidence / artifacts:**

`artifacts/cli/guards/serializer_grep_guard.log`

`artifacts/cli/guards/emitter_symbol_proof.txt`

### Subtask HDE-CONJ003.3 — CLI/Reader parity & canonical JSON

**Subtask name/label:** CLI/Reader parity & canonical JSON checks

**Subtask description:**  
 Prove that CLI Reader surfaces (stdout / `--dump-reader`) are byte-identical to Reader bodies and that outputs are canonical JSON with LF-termination.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`

`CLI_SHOWCOMPAT_CANON_OK`

`JSON_CANONICAL_CHECK_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`tests/test_emitter_determinism.py`

`artifacts/cli/reader_cli_parity.bytes`

### Subtask HDE-CONJ003.4 — Serializer coupling evidence indexing

**Subtask name/label:** Serializer coupling Evidence Index & mirror

**Subtask description:**  
 Index `tests/test_emitter_determinism.py`, `serializer_grep_guard.log`, `emitter_symbol_proof.txt`, and `reader_cli_parity.bytes` in the human Evidence Index and machine mirror in the same PR (records-only JSONL; one LF; with path-proofs).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-CONJ004 — CLI Conformance

**Task ID:** HDE-CONJ004

**Task name/label:** CLI Conformance

**Task status:** **Not done**

**Task description:**  
 Prove CLI installation and entrypoints, showcompat wiring, canonical JSON output, CLI↔Reader parity, AB↔BA/two-run identity for CLI compat flows, and index the key CLI artifacts.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

No CLI conformance artifacts recorded for `ab.json` / `ba.json` / `summary.json`.

CLI parity/determinism harness exists as a plan; acceptance tokens not yet proven or indexed.

Goal:

`showcompat` present and wired.

CLI outputs LF-terminated canonical JSON.

Reader↔CLI parity established.

AB↔BA & two-run identity proven for CLI compat flows.

Installation and help flows exit cleanly.

### **Subtask HDE-CONJ004.1 — CLI install and entrypoints**

Subtask ID: HDE-CONJ004.1

Subtask name/label: CLI installation and entrypoint checks

Subtask description:  
 Validate CLI installation and entrypoints:

pyproject entrypoint is available and working.

python \-m entrypoint is available and working.

Installation path is correct for the target environment.

hdctl \--help exits with status 0 and prints help text to stdout.

Subtask status: Partial

Epic or card: EPIC-017 (QA02 CLI help availability)

Tokens:

CLI\_PYPROJECT\_ENTRYPOINT\_OK

CLI\_MODULE\_RUN\_OK

CLI\_INSTALL\_OK

CLI\_HELP\_EXIT\_0\_OK

CLI\_HELP\_STDOUT\_OK

CLI\_HELP\_OK

Evidence / artifacts:

EPIC017 QA02 hdctl help run (Codespaces → Railway): help banner showing hdctl is on PATH, runs successfully, and exposes the subcommands showcompat, aux-preview, and bg:resolve with concise, canon-consistent descriptions (stored under the EPIC017 QA logs area; path not pinned here).

Future CLI install and entrypoint logs (pyproject entrypoint, python \-m entrypoint, installation path) to be captured and indexed when those aspects are exercised.

Notes:

For EPIC017 QA02, the acceptance criterion for this slice is that the hdctl CLI entrypoint exists in the Codespace environment, runs without error, and exposes the three expected subcommands. That confirms CLI availability and shape so later QA steps can safely rely on hdctl for compat, aux-preview, and bg:resolve runs.

This subtask remains Partial because it still requires explicit evidence for pyproject and python \-m entrypoints and installation path across supported environments; those will be validated and indexed in future work. The help-related tokens (CLI\_HELP\_EXIT\_0\_OK and CLI\_HELP\_STDOUT\_OK) are considered covered for EPIC017 in the Codespaces → Railway QA setup, but the broader CLI installation and entrypoint tokens remain open until additional evidence is captured.

### **Subtask HDE-CONJ004.2 — showcompat canonical JSON and presence**

Subtask name/label: showcompat presence and canonical JSON

Subtask description:  
 Ensure showcompat is present and wired, emitting LF-terminated canonical JSON and participating in the CLI parity harness for compat flows.

Subtask status: Partial

Epic or card:

EPIC-017 (QA03 — showcompat from birth data)

EPIC-018 (QA04 — D1 compat spot-check for a synthetic pair)

Tokens:

CLI\_SHOWCOMPAT\_PRESENT

CLI\_SHOWCOMPAT\_CANON\_OK

JSON\_CANONICAL\_CHECK\_OK

Evidence / artifacts:

EPIC017 QA03 showcompat run in Codespaces:

hdctl showcompat \--source vendor with synthetic birth-only inputs producing a single compat JSON object (top-level keys a, b, compat, viewer\_prefs) with:

10 Magic-10 categories (heat, harmony, communication, alignment, comfort, consistency, expansion, creativity, drive, balance)

per-category band and score fields

viewer\_prefs with all ten categories in weights and integer values 50 (neutral)

compat.meta with engine\_tag \= hdengine-dev, invocation\_tag \= INV-LOCAL, and release\_id all zeros (CLI/dev identity).

EPIC018 QA04 D1 compat spot-check (Codespaces CLI QA environment, audit/qa/hde-epic018/d1-serializer/):

d1-serializer-compat-001-request.txt — describes the synthetic compat pair used for D1:

A: 1985-03-21 08:30 New York, USA

B: 1992-11-05 16:45 London, UK.

d1-serializer-compat-001-ab-run1.json and d1-serializer-compat-001-ab-run2.json — raw hdctl showcompat outputs for AB run 1 and run 2 using the request above, both:

parse cleanly into the same compat JSON shape (a, b, compat, viewer\_prefs)

show all 10 Magic-10 categories with band, score, personal\_key, shared\_key

have compat.meta with engine\_tag \= hdengine-dev, invocation\_tag \= INV-LOCAL, release\_id all zeros

have viewer\_prefs with top\_category \= "heat" and uniform weights 50\.

d1-serializer-compat-001-ab-run1.pretty.json and d1-serializer-compat-001-ab-run2.pretty.json — pretty-printed versions of the same JSON, used only for human inspection; their values match the raw JSON outputs.

d1-serializer-compat-001-ab-cmp-exit.txt — cmp exit code file containing only 0, confirming that the two raw JSON files for AB run 1 and AB run 2 are byte-identical (two-run identity for this compat payload in the CLI/dev context).

qa\_notes.md (under audit/qa/hde-epic018/qa\_notes.md) containing two mechanically appended Step 2 entries documenting that the D1 compat two-run identity check completed, including an entry that explicitly names hdctl showcompat \--source vendor.

Planned and existing CLI harness artifacts for canonical JSON and parity (mechanics-level evidence, shared with HDE-CALC002.5 and future Conjunction/Distillation tasks):

artifacts/cli/ab.json

artifacts/cli/ba.json

artifacts/cli/summary.json

Notes:

EPIC017 QA03 proves that showcompat is present and runnable in the Codespaces environment, and that showcompat \--source vendor from birth-only input produces a compat JSON payload with 10 Magic-10 categories, bands, scores, neutral viewer\_prefs, and a CLI-scoped meta section. For that QA step, the acceptance criterion is “compat JSON produced from births with explicit \--source vendor”; AB↔BA parity, Reader envelope checks, and vendor ingest traces are intentionally deferred to later QA steps.

EPIC018 QA04 builds on this by executing the D1 compat spot-check for a concrete synthetic pair and verifying that:

the compat JSON structure for hdctl showcompat matches PF-canon for that pair (10 Magic-10 categories, bands, scores, keys, meta, viewer\_prefs), and

two successive hdctl showcompat runs (AB run 1 and AB run 2\) produce byte-identical JSON, as shown by cmp exit code 0, with identity fields consistent with a local CLI/dev D1 check (engine\_tag hdengine-dev, invocation\_tag INV-LOCAL, release\_id all zeros).

In the current pre-App, no-user posture, any Live QA step that intends to test real compat behavior (for example D-goals about compat math or “full product payload” for a pair) MUST call the vendor explicitly. Practically, that means hdctl showcompat in Live QA behavior steps MUST include \--source vendor on birth-based runs; showcompat without an explicit vendor source is acceptable only as a local/offline math or serializer check and MUST NOT be used to satisfy behavior tokens or PO Live QA requirements in this environment.

The compat meta fields observed in EPIC017 QA03 and EPIC018 QA04 (engine\_tag \= hdengine-dev, invocation\_tag \= INV-LOCAL, release\_id zeros) are CLI/local identifiers and must not be confused with the Railway production engine identity, which is governed by the /internal/version ops surface on Railway. This split between “CLI as QA console” and “prod engine identity” is expected and consistent with canon.

D1 compat determinism and canonical JSON harnesses that run under closed rails without vendor (for example the artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/cli/summary.json family in HDE-CALC002.5) are explicitly local/offline checks: they prove math/serializer determinism and canonicality, but do not count as vendor-backed behavior tests. Tokens whose intent is to cover live vendor behavior in the current pre-App environment must be satisfied by vendor-backed runs (with \--source vendor) such as the EPIC017/EPIC018 QA slices above and future Live QA steps, not by local-only D1 serializer checks.

This subtask remains Partial because the full scope still requires:

canonical JSON enforcement and parity harness coverage for showcompat using artifacts/cli/ab.json, artifacts/cli/ba.json, and artifacts/cli/summary.json,

AB↔BA parity and Reader↔CLI parity proven and indexed, and

integration of these artifacts into the global Distillation gates and Index/Mirror discipline. Those aspects are covered mechanically by the Canonical Serialization Package and higher-phase tasks and will be reflected here by moving the status to Done once the CLI conformance harness and indexing are fully wired and passing.

### Subtask HDE-CONJ004.3 — CLI compat parity & determinism

**Subtask name/label:** CLI ABBA & two-run identity

**Subtask description:**  
 Prove Reader↔CLI parity and AB↔BA / two-run identity for CLI compat flows, using `ab.json`, `ba.json`, and `summary.json`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`

`CLI_AB_BA_PARITY_OK`

`CLI_TWO_RUN_IDENTITY_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/cli/ab.json`

`artifacts/cli/ba.json` (byte-identical to `ab.json`)

`artifacts/cli/summary.json`

### Subtask HDE-CONJ004.4 — CLI conformance evidence indexing

**Subtask name/label:** CLI conformance Evidence Index & mirror

**Subtask description:**  
 Index `ab.json`, `ba.json`, and `summary.json` in both the Human Index and machine mirror in the same PR (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-CONJ004.5 — PF05 command catalog conformance**

*Subtask name/label:* PF05 command catalog conformance

*Subtask description:*

Verify that the implemented CLI command set and behavior conform to **HDE-CLI-API-Vendor-Ref** (titles-only), treating any divergence as a defect until either the CLI implementation or HDE-CLI-API-Vendor-Ref is updated:

**Command catalog as single home.**

Use PF05’s command catalog and “CLI Overview & Conventions” sections as the single home for CLI commands, flags, and statuses.

Do not duplicate the catalog in PF09; this subtask only requires tests and evidence that compare actual CLI behavior to PF05.

**Conformance behavior.**

For each implemented command, ensure:

Help/usage text matches PF05 (names, flags, required/optional arguments, subcommand descriptions).

Exit codes and streams behavior follow PF05 and the error envelope rules (success on stdout only; errors on stderr only; exit 64 for usage errors).

Payload shapes and error models conform to PF05 and the mechanics/transport rules (titles-only; schemas live in PF05/PF12).

Treat any mismatch between `hdctl` behavior and PF05 as a failing test (defect) until corrected.

**Implemented set coverage.**

Ensure that the set of CLI commands implemented in the binary matches the PF05 catalog for the supported environment (no undocumented commands, no missing required commands).

Gate this via `CLI_IMPLEMENTED_SET_OK` to indicate that the implemented set is in sync with PF05.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

CLI conformance:

`CLI_PYPROJECT_ENTRYPOINT_OK`

`CLI_MODULE_RUN_OK`

`CLI_INSTALL_OK`

`CLI_HELP_EXIT_0_OK`

`CLI_HELP_STDOUT_OK`

`CLI_IMPLEMENTED_SET_OK`

*Evidence / artifacts (titles/paths only):*

CLI install/help/version logs and command-invocation tests that:

Show `hdctl` is installed and reachable (pyproject entrypoint and `python -m engine.cli`).

Verify `hdctl --help` and `hdctl --version` exit 0 and write to stdout (no stderr noise).

Exercise each documented command and compare observed flags/usage/behavior against PF05’s catalog.

Indexing of these artifacts follows the global Evidence Index & Machine Mirror discipline (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`); PF09 does not restate Mirror schema.

---

## Task HDE-CONJ005 — Reader Surface (API)

**Task ID:** HDE-CONJ005

**Task name/label:** Reader Surface (API)

**Task status:** **Not done**

**Task description:**  
 Provide a six-key Reader v1 envelope on a Catalog JSON success route via the shared presenter/emitter, prove A7 transport invariants (200/HEAD/304, ETag, Vary, encoding invariance), maintain an Endpoint Catalog, and index proofs.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

Missing tokens:

`ENDPOINTS_CATALOG_OK`

`ENDPOINTS_CATALOG_ENV_GATE_OK`

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_ENCODING_INVARIANCE_OK`

`READER_200_CTYPE_JSON_UTF8_OK`

Catalog \+ GET/HEAD/304/encoding proofs are absent.

### Subtask HDE-CONJ005.1 — Reader success body & canonical JSON

**Subtask name/label:** Six-key Reader envelope & canonical JSON

**Subtask description:**  
 Ensure public success body is the six-key envelope:

 {

  "reader\_version": "v1",

 "eligible": \<eligible\>,

"categories": \<categories\>,

"meta": \<meta\>,

"release\_id": \<release\_id\>,

"idempotence\_hash": \<idempotence\_hash\>

}

 Emitted via the single presenter/emitter as canonical JSON: UTF-8 (no BOM); ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and ASCII-sorted; checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`READER_200_CTYPE_JSON_UTF8_OK`

**Evidence / artifacts:**

`artifacts/proofs/success_get.txt` (body \+ headers)

### **Subtask HDE-CONJ005.2 — Endpoint Catalog & env-gates**

**Subtask name/label:** Endpoint Catalog entries & env gating

**Subtask description:**  
 Maintain `docs/ENDPOINTS_CATALOG.json` as the canonical, machine-readable inventory of HTTP endpoints in the repo, and within that inventory clearly identify which endpoints are JSON success routes eligible for A7 proofs. Entries are titles-only; bytes/examples and detailed contract semantics remain routed to their single homes by title only.

**Classification is mandatory.** Each Catalog entry MUST carry a per-endpoint class so CI and QA can enforce distinct rails and posture per class.

**Catalog entry minimum fields (titles-only; schema owned elsewhere).**  
 Each entry in `docs/ENDPOINTS_CATALOG.json` MUST include, at minimum:

* `path`

* `method` (`GET`/`POST`/`HEAD`, or a list if multiple methods are supported)

* `classification ∈ {public_reader, internal_admin, internal_identity, ops, dev_harness}`

* `blueprint_module` (titles-only pointer to owning module)

* `rails_profile` (short, names-only rails/gating summary)

* `a7_eligible` (boolean; true only for JSON success routes eligible for A7 proofs)

* `env_gate` (for entries where reachability is env-gated; titles-only pointer)

**A7 tie-in (explicit flag).**  
 A7 proofs apply only to endpoints explicitly marked as A7-eligible JSON success routes:

* A7 proofs run **only** on entries where `a7_eligible == true`.

* `/internal/*` endpoints are never A7-eligible; `/internal/version` is operator-only and must have `a7_eligible == false` (policy owned by Governance; referenced here by title only).

**Test expectations (mechanics only; tokens routed by title).**

Mechanics requires that:

* Endpoints classified as `public_reader` (and any entries where `a7_eligible == true`) have tests that verify canonical emitter usage and the expected status/header/body posture for their class.

* Endpoints classified as `dev_harness` or `ops` have explicit gating tests (APP\_ENV or equivalent) and are not treated as public transport surfaces.

**CI schema and completeness check (fail-closed).**  
 CI MUST fail if `docs/ENDPOINTS_CATALOG.json` is missing or malformed, including:

* missing required fields (especially `classification` and `a7_eligible`),

* invalid `classification` values, or

* invalid `a7_eligible` type/value (must be boolean).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`ENDPOINTS_CATALOG_OK`

`ENDPOINTS_CATALOG_ENV_GATE_OK`

**Evidence / artifacts:**

`docs/ENDPOINTS_CATALOG.json`

`docs/ENDPOINTS_CATALOG.json.sha256`

`artifacts/proofs/endpoints_env_gate_proof.log`

CI logs (titles-only) showing the Catalog schema/completeness check failing on missing/malformed entries and passing when required fields are present and validated.

Tests (titles-only) showing per-class requirements are exercised (public\_reader canonical emitter/posture tests; dev\_harness/ops gating tests; A7-eligible entries have A7 posture tests as owned by the A7 tasks).

### Subtask HDE-CONJ005.3 — A7 transport invariants (Reader)

**Subtask name/label:** A7 GET/HEAD/304/encoding invariance (Reader)

**Subtask description:**  
 On the Catalog JSON success route, prove:

Strong quoted ETag on 200\.

`Vary: Authorization, Accept-Encoding`.

HEAD 200 parity: `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

304 only after prior 200; omit `Content-Type` and `Content-Length`.

POST non-conditional.

Writers/errors: `Cache-Control: no-store`, no `ETag`.

Encoding invariance: ETag and effective Content-Length stable across accepted encodings.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_ENCODING_INVARIANCE_OK`

**Evidence / artifacts:**

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_encoding_invariance.txt`

`artifacts/proofs/success_writers_errors.txt`

### Subtask HDE-CONJ005.4 — Reader A7 evidence indexing

**Subtask name/label:** Reader Catalog & A7 Evidence Index & mirror

**Subtask description:**  
 Index Catalog and A7 artifacts (`docs/ENDPOINTS_CATALOG.*`, `success_get/head/304/encoding_invariance`, `endpoints_env_gate_proof.log`, `success_writers_errors.txt`) in both Human Index and machine mirror in the same PR.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-CONJ006 — Caching & Transport Wiring (Reader)

**Task ID:** HDE-CONJ006

**Task name/label:** Caching & Transport Wiring (Reader)

**Task status:** **Not done**

**Task description:**  
 Explicitly tie A7 proofs to the Catalog JSON success route and capture GET/HEAD/304/encoding/headers evidence with env-gate proof for Reader transport.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

A7 matrix not proven on a cataloged JSON success route; encoding invariance and env-gate evidence missing.

### Subtask HDE-CONJ006.1 — Enforce A7 matrix on Catalog route

**Subtask name/label:** A7 matrix enforcement on Catalog route

**Subtask description:**  
 Enforce the A7 matrix on the Catalog JSON success route:

ETag on 200 (over canonical LF-terminated body).

304 omits `Content-Type` and `Content-Length`; no body.

HEAD 200 parity.

POST non-conditional.

Writers/errors: `Cache-Control: no-store`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_TRANSPORT_PROOF_OK`

**Evidence / artifacts:**

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_writers_errors.txt`

### Subtask HDE-CONJ006.2 — Encoding invariance & env-gate

**Subtask name/label:** Encoding invariance & env-gate proof

**Subtask description:**  
 Prove encoding invariance across accepted `Accept-Encoding` values and provide env-gate proof for the Catalog route.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`A7_ENCODING_INVARIANCE_OK`

`A7_VARY_AUTH_AE_OK`

**Evidence / artifacts:**

`artifacts/proofs/success_encoding_invariance.txt`

`artifacts/proofs/endpoints_env_gate_proof.log`

### Subtask HDE-CONJ006.3 — Caching & transport evidence indexing

**Subtask name/label:** Reader transport Evidence Index & mirror

**Subtask description:**  
 Update Human Index and mirror in the same PR for Reader transport proofs (success\_get/head/304, encoding\_invariance, writers\_errors, env\_gate).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-CONJ007 — CLI Tooling (showcompat, sample)

**Task ID:** HDE-CONJ007

**Task name/label:** CLI Tooling (showcompat, sample)

**Task status:** **Not done**

**Task description:**  
 Provide showcompat and sample CLI tooling with deterministic, canonical JSON outputs, diversity constraints, parity/determinism harness, and indexed artifacts.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

CLI parity/determinism harness exists as a plan; acceptance tokens not yet proven or indexed.

### Subtask HDE-CONJ007.1 — showcompat semantics & gating

**Subtask name/label:** showcompat body & gating

**Subtask description:**  
 For `showcompat`:

Emit a six-key LF-terminated body via shared emitter.

When `eligible == true` and `v1`, include exactly one `{id: "harmony", band}`.

Keep merge-blocking until parity/determinism tokens pass.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`CLI_READER_EMITTER_PARITY_OK`

`PREIMAGE_RECOMPUTE_OK`

`JSON_CANONICAL_CHECK_OK`

`CLI_AB_BA_PARITY_OK`

`CLI_TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/cli/ab.json`

`artifacts/cli/ba.json`

`artifacts/cli/summary.json`

### Subtask HDE-CONJ007.2 — sample CLI semantics & diversity

**Subtask name/label:** sample IDs, seed, & diversity

**Subtask description:**  
 For `sample` (dev-only):

Return IDs-only with deterministic order.

Echo seed in `meta` when provided.

Enforce diversity window/bounds/recent constraints.

Exactly one LF in output.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`COMPOSITE_ABBA_IDENTITY_OK`

`TWO_RUN_IDENTITY_OK`

**Evidence / artifacts:**

`artifacts/cli/ab.json` / `ba.json` / `summary.json` (reused)

### Subtask HDE-CONJ007.3 — CLI conformance & parity tokens

**Subtask name/label:** CLI conformance & parity harness tokens

**Subtask description:**  
 Ensure CLI conformance tokens and parity-harness tokens are satisfied:

CLI conformance:

`CLI_PYPROJECT_ENTRYPOINT_OK`

`CLI_MODULE_RUN_OK`

`CLI_INSTALL_OK`

`CLI_HELP_EXIT_0_OK`

`CLI_HELP_STDOUT_OK`

Parity harness:

`CLI_SHOWCOMPAT_PRESENT`

`CLI_SHOWCOMPAT_CANON_OK`

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** (as listed above)

**Evidence / artifacts:**

`artifacts/cli/ab.json`

`artifacts/cli/ba.json`

`artifacts/cli/summary.json`

### Subtask HDE-CONJ007.4 — CLI tooling evidence indexing

**Subtask name/label:** showcompat/sample Evidence Index & mirror

**Subtask description:**  
 Index `artifacts/cli/ab.json`, `ba.json`, and `summary.json` in Human Index and mirror (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present) in the same PR.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-CONJ008 — Writer Surfaces (API)

**Task ID:** HDE-CONJ008

**Task name/label:** Writer Surfaces (API)

**Task status:** **Not done**

**Task description:**  
 Implement writer APIs with typed numeric-free envelopes, idempotent write paths, correct headers (no-store, no ETag), canonical JSON output (if any), and indexed writer evidence, while keeping A7 tokens scoped to success routes.

**Task notes:**

Writers: `Cache-Control: no-store`, never 304\.

Writers are not A7 proof surfaces; A7 tokens (`A7_*`, `READER_*`) remain bound to Catalog success routes.

### Subtask HDE-CONJ008.1 — Writer envelope & posture

**Subtask name/label:** Typed success/error envelopes & A7 posture

**Subtask description:**  
 Define typed success and error envelopes (numeric-free) and A7 posture:

Writers: `Cache-Control: no-store`, never 304\.

Errors: typed, numeric-free JSON with `Content-Type: application/json; charset=utf-8`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (A7 family excluded from writers)

**Evidence / artifacts:**

`tests/transport/headers/no_store_writers_errors.snap`

### Subtask HDE-CONJ008.2 — Idempotent writer path & byte parity

**Subtask name/label:** Idempotent write path & emitter parity

**Subtask description:**  
 Ensure an idempotent write path:

Canonicalize body before persist.

Record `release_id`.

Run byte-equality checks between stored bytes and emitter output.

Re-issuing the same valid request leaves state unchanged and preserves response semantics.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown**

**Evidence / artifacts:**

Write/readback byte parity logs.

### Subtask HDE-CONJ008.3 — Writer evidence presence & indexing

**Subtask name/label:** Writer evidence & Index/Mirror discipline

**Subtask description:**  
 Capture and index writer evidence artifacts (write/readback logs, DDL updates, ops logs) with Evidence Index entries and machine mirror records; `EVIDENCE_INDEX_UPDATED_OK` and related Index/Mirror tokens gate that evidence is captured and synchronized.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

Writer DDL updates & ops logs (paths not pinned)

Evidence Index entries for writer artifacts

### Subtask HDE-CONJ008.4 — A7 family excluded for writers

**Subtask name/label:** A7 tokens scoping for writers

**Subtask description:**  
 Ensure Governance A7 tokens (`A7_*`, `READER_*`) remain bound to Catalog JSON success routes only; writer routes are not used as A7 proof surfaces and are not directly gated by A7 tokens.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **None** (behavioral scoping; A7 tokens deliberately not applied)

**Evidence / artifacts:**

Governance configuration and test plans (titles-only in PF docs).

---

## Task HDE-CONJ009 — Global discipline (canonical JSON & Index updates)

**Task ID:** HDE-CONJ009

**Task name/label:** Global discipline (single-emitter canonical JSON & Index updates)

**Task status:** **Not done** (tracked as ongoing global requirement)

**Task description:**  
 Enforce single-emitter canonical JSON rules across all surfaces and require Evidence Index/Mirror updates whenever artifacts change.

**Task notes:**

All surfaces honor single-emitter, canonical JSON rules:

UTF-8, no BOM.

ASCII-sorted keys.

Compact separators.

Exactly one LF.

Arrays-as-sets deduped and ASCII-sorted.

All checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Index updates are mandatory:

Update Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and machine mirror (`artifacts/evidence_index.jsonl`) in the same PR that adds or changes artifacts (records-only canonical JSONL; one LF; unknown-key reject; path-proofs in place).

HDE-Schemas & Artifacts §8.6 is the single home for the entries list; PF09 does not duplicate it.

### Subtask HDE-CONJ009.1 — Canonical JSON invariants (all surfaces)

**Subtask name/label:** Canonical JSON invariants enforcement

**Subtask description:**  
 Enforce canonical JSON invariants (encoding, key order, compactness, LF, set ordering) for all surfaces that emit JSON, using the single shared emitter.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

Canonical-compare logs across phases (various `canonical_json/*.log` and `json_canon_compare` artifacts).

### Subtask HDE-CONJ009.2 — Global Index/Mirror discipline

**Subtask name/label:** Global Evidence Index & Mirror enforcement

**Subtask description:**  
 Ensure that whenever any artifacts are added or changed, the Evidence Index and Machine Mirror are updated in the same PR, with canonical JSONL, unknown-key reject, and path-proofs in place.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

# **Phase V — Fermentation (Narratives & external bridges)**

**Phase master status:** **Not done**

---

## **Task HDE-FERM001 — SAFE rails & provider gate**

**Task ID:** HDE-FERM001

**Task name/label:** SAFE rails & provider gate

**Task status:** Not done

**Task description:**  
 Establish and prove SAFE rails posture and provider gating for vendor HTTP, including closed-rails refusal behavior, pinned open-rails policy (timeouts, retries, backoff, 429 handling), observability, and evidence/indexing discipline.

**Task notes:**

SAFE rails tokens are **missing** and not yet wired as acceptance gates (titles-only; token semantics live in HDE-Governance):

`SAFE_RAILS_CLOSED_OK`

`SAFE_RAILS_OPEN_OK`

`SAFE_LOG_REDACTION_OK`

`SAFE_RETRY_BACKOFF_OK`

`SAFE_429_TYPED_REFUSAL_OK`

No SAFE-rails evidence has been captured yet.

Rails are **closed by default**; vendor HTTP is allowed only when **both** gates are open:

Closed rails: `SAFE_MODE = 1`, `ALLOW_NETWORK = 0`.

Open rails: `SAFE_MODE = 0`, `ALLOW_NETWORK = 1`.

Under **closed rails**:

Refusals are typed, numeric-free JSON bodies, LF-terminated.

No secrets in logs.

No `ETag`.

No `Vary` on error/ops routes.

No response compression on refusal.

Request shapes may be computed for diagnostics, but **no outbound I/O** is permitted.

Routing (titles-only):

Rails policy & token semantics: **HDE-Governance**.

Vendor bytes and on-wire contract: **HDE-CLI-API-Vendor-Ref**.

Mechanics (request shaping, SAFE rails hooks): **HDE-Mechanics Guide** (§7.1/§7.3).

---

### **Subtask HDE-FERM001.1 — SAFE rails closed posture & refusal path**

**Subtask name/label:** Closed-rails refusal posture & log discipline

**Subtask description:**

 Prove that under **closed rails** (`SAFE_MODE=1`, `ALLOW_NETWORK=0`):

**No outbound I/O:**

There are no sockets, DNS lookups, or HTTP calls when rails are closed, including for provider and BodyGraph flows.

**Typed refusal envelope:**

Provider-bound requests produce a typed refusal envelope (for example `PROVIDER_DISABLED`), encoded as numeric-free JSON with exactly one trailing LF.

Refusal responses carry no `ETag`, no `Vary` on error/ops routes, and no response compression.

**Keys-only log redaction:**

Logs for these refusal paths are keys-only, with bounded, stable fields such as:

Header names, route, status, duration, `idempotence_hash`, `release_id`.

All secret values (for example `HD-Api-Key`) are redacted (e.g. `HD-Api-Key: REDACTED`); no payload bodies are logged.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in Governance / Epics):**

`SAFE_RAILS_CLOSED_OK`

`SAFE_LOG_REDACTION_OK`

**Evidence / artifacts (titles/paths only):**

`ci/jobs/rails_closed_refusal.yml` — closed-rails refusal proof harness (no outbound I/O, typed refusal envelopes, keys-only logs).

Rails closed-posture snapshot and refusal fixtures (titles/paths single-homed in Governance/Schemas).

---

### **Subtask HDE-FERM001.2 — SAFE rails open posture & policy (integration gate)**

**Subtask name/label:** Open-rails policy (timeouts, retries, backoff, 429\)

**Subtask description:**

 Define and prove the **open-rails** policy for vendor HTTP, pinning timeouts, retries, backoff, and typed 429 handling before live tests:

**Timeout profiles:**

`timeout_profile ∈ {small, default, long}` mapped to `(connect_timeout_ms, read_timeout_ms, total_timeout_ms)` from **closed integer sets**.

**Retries:**

`max_attempts ∈ {0,1,2,3}` (including the initial attempt).

`retryable = {network_error, 5xx}`.

Do **not** retry 429 or any other 4xx status in this component.

**Backoff:**

`backoff ∈ {none, fixed, exponential}` with closed integer parameters.

No jitter.

Accumulated delay must not exceed `total_timeout_ms`.

**Typed 429 handling:**

On HTTP 429, emit a typed `PROVIDER_RATE_LIMITED` error.

If `Retry-After` is valid (delta-seconds or HTTP-date), compute `retry_after_ms ≥ 0`.

On invalid/unsupported/overflow `Retry-After`, omit `retry_after_ms`.

429 is **never** treated as a success path in this epic.

**Success behavior (open rails):**

Success paths emit canonical JSON envelopes governed by the vendor bytes contract (titles-only to HDE-CLI-API-Vendor-Ref).

Determinism and AB↔BA coherence remain satisfied under this policy (canonical JSON, single LF, two-run identity where applicable).

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in Governance / Epics):**

`SAFE_RAILS_OPEN_OK`

`SAFE_RETRY_BACKOFF_OK`

`SAFE_429_TYPED_REFUSAL_OK`

**Evidence / artifacts (titles/paths only):**

`ci/jobs/rails_open_conformance.yml` — success / retry / 429 exercise under pinned timeout and backoff policy.

`artifacts/vendor/policies_pinned.md` — selected timeout/retry/backoff/429 parameters and profiles.

`artifacts/vendor/retry_after_parse.log` — `Retry-After` parse/normalization traces (valid vs invalid/overflow cases).

---

### **Subtask HDE-FERM001.3 — Observability & log posture (SAFE rails)**

**Subtask name/label:** SAFE rails observability & redaction

**Subtask description:**

 Ensure SAFE rails behavior is observable without leaking payloads or secrets:

**Counters/timers:**

Counters and timers distinguish success vs failure classes, including at least: `network_error`, `4xx`, `5xx`, `429`.

**Bounded labels:**

Labels are bounded and well-defined (for example `route`, `outcome`, `rails_state`, `timeout_profile`), avoiding high-cardinality tags.

**Log posture:**

Logs never include payload bodies or secret header values.

Secret-like fields are consistently redacted while preserving enough keys to diagnose rails state and outcome.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in Governance / Epics):**

`SAFE_LOG_REDACTION_OK`

**Evidence / artifacts (titles/paths only):**

`ci/jobs/logs_keys_only_redaction.yml` — log redaction and keys-only check.

Observability dashboard snapshots or logs (titles/paths single-homed in Governance/Schemas) showing bounded label sets and separated outcome classes.

---

### **Subtask HDE-FERM001.4 — SAFE rails evidence & indexing**

**Subtask name/label:** SAFE rails evidence & Evidence Index discipline

**Subtask description:**

 For SAFE rails and provider-gate artifacts, enforce Evidence Index/Mirror discipline:

**Required SAFE-rails artifacts:**

`ci/jobs/rails_closed_refusal.yml` — closed-rails refusal proof harness.

`ci/jobs/rails_open_conformance.yml` — success / retry / 429 exercise.

`ci/jobs/logs_keys_only_redaction.yml` — log redaction check.

`artifacts/vendor/policies_pinned.md` — pinned timeout/retry/backoff/429 parameters.

`artifacts/vendor/retry_after_parse.log` — `Retry-After` parse/normalization traces.

**Indexing (same-PR rule):**

Update, in the **same PR** that adds or changes any SAFE-rails artifacts:

`docs/evidence/INDEX.json` (Human Index)

`docs/evidence/INDEX.sha256` (hash sentinel)

`artifacts/evidence_index.jsonl` (Machine Mirror)

Keep the Machine Mirror as **records-only canonical JSONL**:

UTF-8, no BOM.

ASCII-sorted keys.

Compact separators.

Exactly one trailing LF per record.

Unknown-key reject.

Fixed field order.

`proof_anchor` pointing to a co-located `*.path_proof.txt`.

Treat **HDE-Schemas & Artifacts** §8.6 as the single home for the evidence listing; Appendix C defines record types and schemas. PF09 (this subtask) does not duplicate those schemas.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in Governance / Epics):**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts (titles/paths only):**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

SAFE-rails artifacts listed above, plus their `*.path_proof.txt` transcripts.

### **Subtask HDE-FERM001.5 — D0 discovery baseline (env, CLI, services)**

**Subtask name/label:** D0 discovery baseline (env, CLI, services)

**Subtask description:**  
 Add a mandatory **D0 discovery gate** for Live QA epics so that environment, rails, CLI health, and basic services/ports are understood and evidenced **before** any high-stakes Live QA steps (including vendor tests) are treated as complete:

**D0 env & rails baseline (open-rails posture).**

* For any Live QA session that intends to exercise vendor or other open-rails behavior, capture a **D0 environment baseline log** under the run’s QA root (for example `audit/qa/<epic>/live-qa-YYYYMMDD/D0_env_baseline.log`) that records, at minimum:

  * `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, and `TZ` values for the intended **open-rails** posture for the session.

  * A brief explanation of how these rails differ from the default closed-rails posture (titles-only to Glow QA Guide and SAFE rails canon).

* This env baseline log is part of the evidence for the QA acceptance token `OPEN_RAILS_ENV_OK`; it proves that any later “open-rails” vendor tests really ran under the mandated rails, not under the default closed-rails posture.

**D0 CLI health check.**

* Before running epic-level tests, produce a **CLI health check log** under QA root (for example `audit/qa/<epic>/live-qa-YYYYMMDD/D0_cli_health.log`) that shows, at minimum:

  * `python -m pytest --version` succeeded under the intended environment (matching the QA bootstrap harness in HDE-CALC003.12).

  * `command -v hdctl` (and any other primary CLI tools such as `jq`) succeeded and reported usable entrypoints.

  * A short summary line indicating whether CLI tools and pytest are **ready for use** or whether there are tooling failures that must be addressed before Live QA can continue.

* Failures captured here are treated as tooling/infra blockers under the QA tooling bootstrap and harness subtasks (HDE-CALC003.12–.14); D-goals that depend on CLI behavior remain pending until CLI health is restored.

**D0 services & ports discovery (Reader/HTTP and vendor connectivity).**

* Produce a **services and ports discovery log** under QA root (for example `audit/qa/<epic>/live-qa-YYYYMMDD/D0_services_and_ports.log`) that records, at minimum:

  * For internal/dev HTTP harnesses (such as `/internal/dev/sampler`), the canonical dev Reader start command and the base URL/port in this environment, preferably leveraging infra-owned bindings such as `DEV_SAMPLER_URL` defined under HDE-CONJ001.4 (titles-only).

  * Any known production or stage URLs/hostnames for Railway or equivalent vendor endpoints that are expected to be used in this session (hostnames and ports only; no secrets).

  * Simple connectivity checks (for example `curl` or CLI “ping” commands) against these endpoints that distinguish “no service / wrong protocol” from “reachable but behavior to be tested later,” without embedding payloads or secrets in logs.

* Missing or inconclusive D0 services/ports evidence MUST be treated as a **discovery gap**: Live vendor D-goals (for example `LIVE_VENDOR_TRANSPORT_OK` in the QA token library) cannot be marked satisfied until D0 services/ports discovery is complete and shows that the relevant services are actually reachable.

**Acceptance and gating posture.**

* This subtask is gated by the QA acceptance token `DISCOVERY_BASELINE_OK` (semantics single-homed in Glow QA Guide and HDE-Phased Epics by title). For any Live QA epic that claims vendor-related D-goals, `DISCOVERY_BASELINE_OK` MUST be satisfied via:

  * a non-empty D0 env baseline log,

  * a non-empty D0 CLI health log, and

  * a non-empty D0 services and ports discovery log,

* all captured under the run’s QA root and stored as governed QA artifacts.

* If any of the D0 logs are missing or empty, Live QA steps that depend on them MUST be classified as **FAIL\_TOOLING** (or the equivalent tooling failure state defined in PF19) rather than as behavior failures or silent passes; subsequent QA runs for the same epic MUST fix discovery/harness issues first.

**Subtask status:** **Not done**

**Epic or card:** **Unknown** (future Live QA / vendor-rails epic to wire D0 discovery into harness and evidence)

**Tokens (titles-only; semantics live in Glow QA Guide / Governance / HDE-Phased Epics):**

`DISCOVERY_BASELINE_OK` — D0 discovery baseline satisfied (env/rails, CLI health, services & ports).

`OPEN_RAILS_ENV_OK` — open-rails env baseline log captured for Live QA steps that require ALLOW\_NETWORK=1.

**Evidence / artifacts (titles/paths only):**

* D0 env & rails baseline log(s):

  * `audit/qa/<epic>/live-qa-YYYYMMDD/D0_env_baseline.log` — open-rails env snapshot and commentary for the session.

* D0 CLI health log(s):

  * `audit/qa/<epic>/live-qa-YYYYMMDD/D0_cli_health.log` — CLI and pytest health checks, including exit codes and short readiness summary.

* D0 services & ports discovery log(s):

  * `audit/qa/<epic>/live-qa-YYYYMMDD/D0_services_and_ports.log` — Reader/HTTP dev harness start command and base URL/port, Railway/vendored endpoints discovered, and basic connectivity checks.

* Evidence Index & Machine Mirror entries for these D0 logs, once governed, via the global Evidence Index discipline (front matter §0.3–§0.5; PF09 does not restate mirror schemas).

**Notes:**  
 This subtask is added in response to the EPIC019 Live vendor QA RCA (Addendum 17), which showed that the lack of a D0 discovery baseline (env, CLI, services/ports) made it impossible to distinguish infra/tooling gaps from sampler/ingest behavior issues and led to repeated, unproductive remediation attempts under closed rails. Together with the QA tooling bootstrap and harness discipline subtasks in Phase I and the dev Reader infra wiring subtask in Phase IV, this D0 discovery gate ensures that future Live QA epics start from a clear, evidenced understanding of env rails, CLI health, and basic services/ports before attempting to satisfy vendor D-goals.

---

## **Task HDE-FERM002 — Narrative Selection Router (keys only)**

**Task ID:** HDE-FERM002

**Task name/label:** Narrative Selection Router (keys only)

**Task status:** Not done

**Task description:**  
 Implement and prove a deterministic **Narrative Selection Router** that operates on **keys only**, not text. For any supported input `(category, band, perspective, viewer_top, flags)`, the router must produce stable `{personal_key, shared_key}` outputs with:

No randomization or time-based behavior.

No implicit fallbacks (missing mappings return `missing_narrative_key`).

Strict CLI↔Reader parity via the shared presenter/emitter (same keys, same canonical JSON bytes).

**Task notes:**

The router **only selects narrative keys**; it never produces narrative prose.

**Inputs:** `(category, band, perspective ∈ {personal, shared}, viewer_top, flags)`.

**Outputs:** `{personal_key, shared_key}` or typed `missing_narrative_key` values.

Deterministic behavior:

No RNG.

No dependence on wall-clock time or ambient environment.

No DB or vendor lookups in the selection path.

CLI and Reader both call the **same router** through the shared presenter/emitter, so keys and bytes remain aligned across surfaces.

Routing (titles-only):

Category framework & mechanics: **HDE-Mechanics Guide** (§7).

Banding & category semantics: **HDE-Math-Spec**.

Narrative Key Registry & pack identity: **HDE-FERM003** / **Narratives Guide** (titles-only).

---

### **Subtask HDE-FERM002.1 — Deterministic router implementation**

**Subtask name/label:** Implement deterministic keys-only router

**Subtask description:**

 Implement the router as a pure, deterministic component and wire it to all relevant surfaces:

**Freeze the argument schema:**

Define and fix the exact router input shape  
 `(category, band, perspective, viewer_top, flags)`  
 with no implicit or hidden parameters.

Treat this schema as part of the public behavior contract for routing; changes must go through a future epic and Doc-Delta.

**Deterministic selection rules:**

Use explicit **total-order** utilities (as in Mechanics §5) for any “top N” or tie-break logic.

Ensure candidate ordering is fully specified and stable (no dependence on Python dict/set iteration order, DB row order, or nondeterministic joins).

**No side effects / external I/O:**

Eliminate clocks, randomness, and external I/O from routing logic:

No `datetime.now()` or equivalent.

No calls to filesystem, network, DB, or vendor adapters in the selection path.

Router decisions must be a pure function of its inputs plus the pinned registry content (titles-only to HDE-FERM003).

**Keys-only behavior:**

Router returns keys from the Narrative Key Registry; it does **not** emit narrative text, snippets, or prose.

When a mapping is missing, router returns a typed `missing_narrative_key` indicator; no implicit fallback keys or packs.

**CLI/Reader integration:**

Wire the router into CLI and Reader via the **shared presenter/emitter** so that:

For identical `(category, band, perspective, viewer_top, flags)`, CLI and Reader receive the same `{personal_key, shared_key}` pair.

The JSON envelopes on each surface are canonical and byte-identical where PF05 defines Reader↔CLI parity.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

`CLI_READER_PARITY_OK` — CLI/Reader parity via shared emitter.

`TWO_RUN_IDENTITY_OK` — repeat runs produce identical router outputs.

A router-specific keys-only token (for example `NARR_ROUTER_KEYS_ONLY_OK`) may be introduced in Governance; PF09 references it by title only when minted.

**Evidence / artifacts (titles/paths only):**

`tests/narratives/test_router.py` — implementation-level tests and edge cases for router behavior (no RNG, no fallbacks, missing mappings).

Implementation wiring evidence is captured indirectly via the parity and coverage artifacts in Subtask HDE-FERM002.2.

---

### **Subtask HDE-FERM002.2 — Router tests, parity, and evidence indexing**

**Subtask name/label:** Router tests, coverage, and Evidence Index discipline

**Subtask description:**

 Add tests and evidence artifacts to prove router behavior and keep all surfaces in parity, and ensure everything is indexed under the standard Evidence discipline:

**Unit tests & coverage:**

For each `(category, band, perspective)` case in the supported matrix:

Verify **two-run identity**: same inputs → same `{personal_key, shared_key}` on repeated runs.

Verify **AB↔BA coherence** where applicable (for example A–B vs B–A inputs yield the same key pairing once normalized).

Cover both `personal` and `shared` perspectives and explicit edge cases:

Known mappings.

Missing mappings (router returns `missing_narrative_key`, not a fallback).

**Acceptance behavior (titles-only):**

Resolver returns `{personal_key, shared_key}` or `missing_narrative_key` for each slot.

Outputs are **canonical JSON**:

UTF-8 (no BOM).

ASCII-sorted keys.

Compact separators.

Exactly one trailing LF.

Reader’s public surface remains **bands-only**; keys map to narrative content by title (via narrative packs, not in PF09).

CLI and Reader use the **same keys** for the same inputs (parity via shared presenter/emitter); where PF05 defines Reader↔CLI parity bytes, router JSON envelopes participate in those parity checks.

**Parity and coverage artifacts (titles/paths only):**

`audit/gates/narratives/keys_10x4.table.json` — router coverage snapshot (e.g. 10 categories × 4 bands), canonical JSON (UTF-8, sorted keys, compact, one LF); shows `{personal_key, shared_key}` and `missing_narrative_key` cases for each `(category, band, perspective)`.

`artifacts/narratives/router/parity_abba.log` — AB↔BA and two-run identity log for router outputs (keys-only, no prose).

`artifacts/narratives/router/cli_http_parity.log` — CLI=HTTP parity compare for router responses, showing byte-identical canonical JSON where parity is defined.

`tests/narratives/test_router.py` — unit tests and edge cases (as above).

**Indexing discipline (Evidence Index & Machine Mirror):**

In the **same PR** that introduces or changes any router artifacts:

Update `docs/evidence/INDEX.json` (Human Index).

Update `docs/evidence/INDEX.sha256` (hash sentinel).

Update `artifacts/evidence_index.jsonl` (Machine Mirror).

Ensure the Machine Mirror remains:

Records-only canonical JSONL (UTF-8; sorted keys; compact; exactly one LF).

Unknown-key rejecting with fixed field order.

Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

**HDE-Schemas & Artifacts** §8.6 and Appendix C remain the single homes for evidence listing and record types; PF09 does not restate schemas.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

`CLI_READER_PARITY_OK` — CLI/Reader parity proven with router outputs.

`TWO_RUN_IDENTITY_OK` — two-run identity for router outputs.

`JSON_CANONICAL_CHECK_OK` — canonical JSON checks for router artifacts.

`EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated for router artifacts.

`MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside Evidence Index.

`EVIDENCE_PATHS_VALIDATED_OK` — router artifact paths validated against the mirror.

**Evidence / artifacts (titles/paths only):**

`audit/gates/narratives/keys_10x4.table.json`

`artifacts/narratives/router/parity_abba.log`

`artifacts/narratives/router/cli_http_parity.log`

`tests/narratives/test_router.py`

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## **Task HDE-FERM003 — Narrative Key Registry & Manifests**

**Task ID:** HDE-FERM003

**Task name/label:** Narrative Key Registry & Manifests

**Task status:** Not done

**Task description:**  
 Establish **versioned, diffable narrative key manifests** as the single source of truth for narrative keys, with **exactly one key per `(category, band, perspective)`**, pack identity derived from canonical manifest bytes, and Doc-Delta plus Evidence Index/Mirror discipline for every change. The registry and manifests are **keys-only**: they carry narrative identifiers and routing metadata, and **no narrative prose or text is stored in the engine**; prose lives in narrative packs/copy docs governed by the Narratives Guide (titles-only).

**Task notes:**

Versioned, diffable manifests are the **single source of truth** for narrative keys.

There is **exactly one key** for each `(category, band, perspective)` combination; closure checks (no missing or duplicate keys) are enforced by the manifest validator and must fail CI on defects.

Manifests are canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF) and contain enough fields to capture `(category, band, perspective, language/variant, key)` per entry; detailed schema is single-homed in HDE-Schemas & Artifacts (titles-only).

Pack identity is:

`pack_sha = sha256(canonical manifest bytes)`, and

Packs are stored under `/narratives/<pack_sha>/`

Exporter and loader behavior for packs is owned by **HDE-Mechanics Guide** and the **Narratives Guide** (titles-only); PF09 does not define exporter/loader mechanics, only that manifests and identity artifacts exist, are canonical, and are indexed with Doc-Delta and Evidence Index/Mirror discipline.

---

### **Subtask HDE-FERM003.1 — Manifest shape & closure validation**

*Subtask name/label:* Manifest shape & registry closure

*Subtask description:*

Define the manifest schema and implement closure checks over the narrative key space.

**Manifest shape:**

Manifests are canonical JSON:

UTF-8 (no BOM).

ASCII-sorted keys.

Compact separators.

Exactly one trailing LF.

Each manifest record includes enough fields to capture:

category

band

perspective (e.g. personal / shared)

language/variant

key

**Closure validator:**

Implement a validator that fails if any required `(category, band, perspective)` combination is missing or duplicated in the registry.

Treat any gaps or duplicates as defects until resolved.

**Registry as single source of truth:**

Ensure that all narrative key usage routes through these manifests; other components (router, packs, exporter/loader) treat the manifests as authoritative, by title only.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

`JSON_CANONICAL_CHECK_OK` — canonical JSON checks for governed manifests and registry files.

`UNKNOWN_IDS_FAIL_CLOSED_OK` — manifest builder rejects unknown or stray IDs in the registry.

`TIEBREAK_TOTAL_ORDER_OK` — deterministic ordering applied when ties occur in the registry key space.

*Evidence / artifacts (titles/paths only):*

`artifacts/narratives/registry/*.json` — narrative key manifests (canonical JSON; one LF) with full `(category, band, perspective, language/variant, key)` coverage.

---

### **Subtask HDE-FERM003.2 — Diffing, Doc-Delta wiring, identity, and indexing**

*Subtask name/label:* Manifests diffing, Doc-Delta, pack identity, and Evidence Index

*Subtask description:*

Add diff tooling, Doc-Delta policy, pack identity computation, and evidence/indexing discipline.

**Diff tooling:**

Build a concise diff artifact for manifest changes:

Capture additions, removals, and modifications of keys across manifests.

Produce a compact, readable artifact for each change set.

**Doc-Delta policy:**

Enforce that any registry change is accompanied by:

A `DOC-DELTA-*.md` entry, recording the change and rationale (titles-only; no payload duplication).

Evidence updates in the same PR.

**Pack identity:**

Compute `pack_sha = sha256(canonical manifest bytes)` for each manifest.

Verify that pack identity matches the manifest bytes used to build `/narratives/<pack_sha>/`

Ensure ABBA / two-run identity remains unaffected by registry changes:

Same manifest bytes → same `pack_sha` in repeated runs.

Swapping inputs in compat/narrative selection flows does not change pack identity once normalized (AB↔BA).

**Evidence & diff artifacts (titles/paths only):**

`artifacts/narratives/registry/*.json` — canonical manifests (see HDE-FERM003.1).

`audit/gates/narratives/registry.diff.json` — compact diff of manifest changes.

`docs/changes/DOC-DELTA-*.md` — Doc-Delta records for registry changes (titles-only; no narrative payload bytes).

**Evidence Index & Machine Mirror:**

In the same PR that changes any registry manifest or diff:

Update `docs/evidence/INDEX.json` (Human Index).

Update `docs/evidence/INDEX.sha256` (hash sentinel).

Update `artifacts/evidence_index.jsonl` (Machine Mirror).

Ensure the Machine Mirror remains:

Records-only canonical JSONL (UTF-8; sorted keys; compact; exactly one LF).

Unknown-key rejecting, with fixed field order.

Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

`HDE-Schemas & Artifacts` §8.6 and Appendix C remain the single homes for listing and record types; PF09 routes to them by title only and does not restate schemas.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

`DOC_DELTA_PRESENT_OK` — Doc-Delta artifacts captured for registry/manifests changes.

`JSON_CANONICAL_CHECK_OK` — canonical JSON checks for manifests and diff artifacts.

`AB_BA_PARITY_OK` — AB↔BA parity remains satisfied after registry changes (where applicable).

`TWO_RUN_IDENTITY_OK` — two-run identity holds for pack identity and related proofs.

`EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated when registry artifacts change.

`EVIDENCE_INDEX_HASH_OK` — index hash recorded for the updated evidence set.

`MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside the Evidence Index.

`EVIDENCE_PATHS_VALIDATED_OK` — registry-related artifact paths validated against the Machine Mirror.

`EVIDENCE_PATH_PROOFS_OK` — each registry-related artifact accompanied by a path proof.

`CI_CHECK_MIRROR_SCHEMA_OK` — CI schema check for the Machine Mirror.

`CI_CHECK_FINAL_LF_OK` — final-LF check for governed JSON/JSONL artifacts.

*Evidence / artifacts (titles/paths only):*

`artifacts/narratives/registry/*.json`

`audit/gates/narratives/registry.diff.json`

`docs/changes/DOC-DELTA-*.md`

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## **Task HDE-FERM004 — Database Runtime Posture**

**Task ID:** HDE-FERM004

**Task name/label:** Database Runtime Posture

**Task status:** Not done (Audit v1 — 2025-11-17)

**Task description:**  
 Define and prove database runtime posture for the engine, including search\_path, role/grants, DDL fingerprint, dev fallback via DB bridge, bridge capability and provider parity, total-failure behavior, and evidence/indexing discipline. All DB posture scripts must use the adapter façade and route token semantics and schemas to HDE-Governance and HDE-Schemas & Artifacts.

**Task notes:**

**Missing tokens** (titles-only; tokens live in HDE-Governance):

`DB_RUNTIME_SEARCH_PATH_OK`

`DB_ROLE_OK`

`DB_SCHEMA_FINGERPRINT_OK`

`DB_CONN_ENV_OK`

`DB_BRIDGE_FALLBACK_OK`

`DEV_DB_BRIDGE_FALLBACK_OK`

`DB_PROVIDER_PARITY_OK`

`DB_BRIDGE_CAPS_OK`

Evidence is currently empty for this phase:  
 **Evidence:** — (no posture/bridge artifacts indexed yet).

PF09 expresses only **which tokens gate DB posture** for this phase; token semantics and artifact schemas live in **HDE-Governance** and **HDE-Schemas & Artifacts** (titles-only).

---

### Subtask HDE-FERM004.1 — Adapter façade, runtime search\_path, and structural posture

*Subtask name/label:* Adapter façade, search\_path, and structural posture

*Subtask description:*

Define and prove the core runtime DB posture, using the provider-agnostic adapter façade, including search\_path, grants, DDL fingerprint, constraints, and boundary view posture:

**Adapter façade only**

All DB posture and evidence scripts **MUST** call the **DBAccess façade** (provider-agnostic adapter), never raw driver clients, to guarantee parity across TCP and HTTPS providers.

**Runtime search\_path**

Prove that the runtime `search_path` is exactly `hde, public` (unquoted, in that order) for the engine’s DB role.

Capture a `check_schema` artifact demonstrating the runtime search\_path and visible namespaces at the moment posture is captured.

**Least-privilege grants**

Capture a grants snapshot for the runtime role.

Verify there are **no extraneous DML/DDL privileges** beyond what the engine requires to serve public workloads.

**DDL fingerprint and constraints**

Capture normalized DDL for the relevant schemas in a stable order and compute a SHA-256 fingerprint; store the result as a governed artifact.

Capture a constraints snapshot, including FK, uniqueness, and any invariants called out in epic/spec documents.

Treat any unexpected change in the DDL fingerprint or constraints snapshot as a posture change that must be tracked via Governance and Schemas by title.

**Boundary view posture**

Capture a dedicated proof that the boundary view used by engine/CLI for public reads is **read-only** and does not permit writes outside the HDE schema.

The boundary-view proof path and schema remain single-homed in **HDE-Schemas & Artifacts**; PF09 only requires that the proof artifact exists and is kept in sync with runtime posture.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

`DB_RUNTIME_SEARCH_PATH_OK`

`DB_ROLE_OK`

`DB_SCHEMA_FINGERPRINT_OK`

*Evidence / artifacts (titles/paths only):*

`artifacts/db/check_schema.txt` — runtime search\_path and visible schemas snapshot.

`artifacts/db/grants.txt` — grants snapshot for the runtime role (least-privilege proof).

`artifacts/db/ddl_fingerprint.json` — normalized DDL fingerprint (includes SHA-256 and any supporting metadata).

`artifacts/db/check_constraints.txt` — constraints snapshot (FK, uniqueness, and invariants referenced from canon).

`boundary_view.readonly.proof` — boundary view read-only posture proof.

---

### **Subtask HDE-FERM004.2 — Dev fallback & bridge capability / provider parity**

**Subtask name/label:** Dev fallback, bridge caps, and provider parity

**Subtask description:**

 Implement dev fallback behavior via the DB bridge and prove bridge capability and provider parity:

**Dev fallback (adapter):**

In `APP_ENV=dev`, when `DATABASE_URL` is present but **unusable**, fallback to `DB_BRIDGE_URL` (HTTPS) via the adapter façade.

Record all attempts and the **selected source** in a resolver snapshot:

Attempts (e.g. `database_url_attempt`, `db_bridge_url_attempt`).

Result (`success` / `failure`).

Final selected provider.

**Bridge capability:**

Snapshot bridge capabilities (endpoints and grants) via the adapter façade.

**Provider parity:**

Demonstrate that queries against the bridge produce results **identical** to direct DB access on a canonical corpus.

Use a normalized output format for comparison and store parity results under governed paths.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

`DEV_DB_BRIDGE_FALLBACK_OK`

`DB_BRIDGE_CAPS_OK`

`DB_PROVIDER_PARITY_OK`

**Evidence / artifacts (titles/paths only):**

`artifacts/runtime/env_connectivity.snapshot.json` — dev resolver snapshot (attempts/result/selected provider).

`artifacts/db_bridge/adapter_selection.snapshot.json` — adapter selection details for DB vs bridge.

`artifacts/db_bridge/caps.snapshot.json` — bridge capabilities (endpoints/grants).

`artifacts/db/provider_parity/*.json` — normalized provider parity results (bridge vs direct DB on canonical corpus).

---

### **Subtask HDE-FERM004.3 — Non-dev total failure behavior and typed errors**

**Subtask name/label:** Non-dev presence-order selection & failure posture

**Subtask description:**

 Define and prove non-dev selection and failure behavior without proactive probes:

**Presence-order selection (non-dev):**

In non-dev environments, use **presence-order** selection for connectivity:

If `DATABASE_URL` is valid, use it.

Else, if `DB_BRIDGE_URL` is valid, use it.

Else, emit a typed error.

**No proactive probes:**

Do **not** run proactive probes beyond what the adapter uses to fulfill a request; do not perform speculative or background connectivity checks.

**Deterministic, numeric-free error on total failure:**

On total failure (no usable provider), emit a deterministic, numeric-free error envelope describing the failure state.

Error payloads must remain numeric-free in user-visible text; traceability goes through IDs and logs, not numeric error codes in public envelopes.

**Subtask status:** Not done

**Epic or card:** Unknown

**Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):**

`DB_CONN_ENV_OK`

`DB_BRIDGE_FALLBACK_OK`

**Evidence / artifacts (titles/paths only):**

`artifacts/runtime/env_connectivity.snapshot.json` — presence-order behavior and total-failure traces.

`artifacts/db/provider_parity/*.json` — may be reused to show correct selection when connections succeed.

---

### Subtask HDE-FERM004.4 — DB posture acceptance, capture discipline, and Evidence Index/Mirror

*Subtask name/label:* DB posture gating, capture discipline, and evidence indexing

*Subtask description:*

Wire DB posture acceptance tokens for this phase and enforce a single capture/indexing discipline over all DB posture and bridge artifacts:

**DB posture & durability tokens** (titles-only; semantics live in HDE-Governance):

`DB_RUNTIME_SEARCH_PATH_OK`

`DB_ROLE_OK`

`DB_SCHEMA_FINGERPRINT_OK`

**Connectivity & error tokens:**

`DB_CONN_ENV_OK` — presence-order behavior and typed, numeric-free error on total failure.

**Bridge & fallback tokens:**

`DB_BRIDGE_FALLBACK_OK`

`DEV_DB_BRIDGE_FALLBACK_OK`

`DB_PROVIDER_PARITY_OK`

`DB_BRIDGE_CAPS_OK`

**Index/mirror/path-proofs tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Posture capture discipline (must):**

Run all governed DB posture captures (including DDL, constraints, boundary view, connectivity, and parity) under deterministic env pins:

`LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Produce canonical JSON or LF-terminated text for all governed artifacts:

UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF.

Keep all posture artifacts and logs **secret-free**:

No credentials, connection strings, or sensitive payload bodies; logs are keys-only.

**Evidence Index & Machine Mirror discipline:**

Whenever any DB posture or bridge artifact changes, update in the **same PR**:

`docs/evidence/INDEX.json` (Human Index).

`docs/evidence/INDEX.sha256` (hash sentinel).

`artifacts/evidence_index.jsonl` (Machine Mirror).

Machine Mirror requirements:

Records-only canonical JSONL (UTF-8, sorted keys, compact, exactly one LF).

Unknown-key reject; a **single** mirror file.

Each record includes a `proof_anchor` pointing to a co-located `*.path_proof.txt`.

PF09 does **not** define mirror schema or token semantics; it routes to **HDE-Schemas & Artifacts** and **HDE-Governance** by title.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

As listed above; PF09 references them by title only.

*Evidence / artifacts (titles/paths only):*

Core DB posture artifacts:

`artifacts/db/check_schema.txt`

`artifacts/db/grants.txt`

`artifacts/db/ddl_fingerprint.json`

`artifacts/db/check_constraints.txt`

`boundary_view.readonly.proof`

Bridge & connectivity artifacts:

`artifacts/runtime/env_connectivity.snapshot.json`

`artifacts/db_bridge/adapter_selection.snapshot.json`

`artifacts/db_bridge/caps.snapshot.json`

`artifacts/db/provider_parity/*.json`

Index artifacts:

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## **Task HDE-FERM005 — CLI Aux preview story (admin surface & evidence)**

*Task ID:* HDE-FERM005

*Task name/label:* CLI Aux preview story (admin surface & evidence)

*Task status:* Done (history-locked via EPIC-010 / EPIC-017)

*Task description:*  
 Track and validate the CLI Aux preview “story” end-to-end: an admin preview surface that uses the shared presenter/emitter, emits narrative text on stdout plus a minimal IDs-only JSON sidecar, and is captured as governed evidence (indexed and mirrored). This task records that the CLI Aux story has been implemented and proven via EPIC-010 and EPIC-017 QA runs.

*Task notes:*

EPIC-010 established the CLI preview posture and indexing for Aux narratives via `artifacts/cli/narrative/stdout.txt` and `artifacts/cli/narrative/sidecar.json`; that work is history-locked as Done.

EPIC-017 QA06/QA07 added QA evidence that, in Codespaces CLI, `hdctl aux-preview` can:

Generate a valid Aux narrative from compat JSON (public text: non-empty, numeric-free, present-tense, no HD jargon or fate/destiny language).

Produce a minimal admin JSON selector with `composition_id`, `pack_sha`, `pair` IDs, and `release_id`, traceable back to compat and the pinned narratives pack.

---

### **Subtask HDE-FERM005.1 — CLI Aux preview posture (enabled, indexed, and evidenced)**

*Subtask name/label:* CLI Aux preview posture (Enabled and Indexed)

*Subtask description:*

Prove that the CLI admin preview surface for Aux narratives is wired, uses the shared presenter/emitter, and is captured under the Evidence Index discipline.

**Preview posture:**

Admin preview is enabled for allowed operators and uses the **same presenter/emitter** as Reader.

Preview output on stdout is LF-terminated text with **no ANSI escapes**.

Narrative IDs and bands are exposed only via an **IDs-only canonical JSON sidecar**.

**Narrative artifacts:**

`artifacts/cli/narrative/stdout.txt`

LF-terminated Aux preview text for the CLI admin surface (no ANSI).

`artifacts/cli/narrative/sidecar.json`

IDs-only canonical JSON sidecar for the same preview (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one LF).

Contains only selectors (for example `composition_id`, `key`, `pack_sha`, `pair` IDs, `release_id`); no narrative prose.

These artifacts must be listed in the **Human Evidence Index** and mirrored in the **Machine Mirror** in the same PR.

**Preview indexing posture and QA story:**

CI gates on `CLI_PREVIEW_ENABLED_OK` and `CLI_PREVIEW_INDEXED_OK` confirm that:

The preview surface exists and is wired to the shared presenter/emitter.

Preview artifacts are captured under the Evidence Index discipline.

EPIC-010 acceptance (history-locked):

`artifacts/cli/narrative/stdout.txt` and `sidecar.json` exist and are indexed.

EPIC-017 QA06 Aux narrative evidence (CLI QA environment):

audit/qa/hde-epic017/logs/step\_aux\_preview1.txt — narrative text produced by:

`hdctl aux-preview --show-narrative` against compat JSON from `showcompat --source vendor` for a synthetic birth pair.

Contains a short, coherent, numeric-free, present-tense narrative with no Human Design jargon and no fate/destiny language, matching Aux public copy canon.

EPIC-017 QA07 Aux admin JSON sidecar evidence (CLI QA environment):

audit/qa/hde-epic017/logs/step\_aux\_preview1\_admin.json — Aux admin JSON sidecar produced by:

`hdctl aux-preview --admin-out` for the same compat JSON.

Contains at minimum:

`composition_id` / `key` of the form `<category>.<band>.<perspective>.<slot>` (for example `heat.open.shared.1`).

`pack_sha` as a 64-character lowercase hex digest for the narratives pack.

`pair.{a_person_uid,b_person_uid}` matching the compat JSON `person_uid`s.

`release_id` as an all-zero 64-hex string consistent with CLI/local identity.

Confirms Aux selects compositions from a pinned narratives pack in a traceable, compat-aligned way.

*For acceptance under this subtask, it is sufficient that:*

A governed admin preview surface exists and is wired to the shared presenter/emitter.

A preview narrative artifact exists and is indexed (`artifacts/cli/narrative/stdout.txt` and `sidecar.json` for EPIC-010).

At least one QA run (such as EPIC-017 QA06/QA07) demonstrates that, from CLI compat JSON, Aux can generate both:

Public narrative text that respects the public covenant (no numerics in text; no HD jargon; appropriate tone).

A minimal admin JSON selector (`composition_id`/`key`, `pack_sha`, `pair` IDs, `release_id`) consistent with compat and the pinned narratives pack.

Deeper determinism checks for Aux (for example AB↔BA and two-run identity for admin JSON and narrative text, multi-pack routing invariants) remain scoped to other tasks and future QA phases; this Fermentation subtask records preview posture, evidence presence, basic tonality compliance, and minimal admin JSON sidecar correctness.

*Subtask status:* Done (EPIC-010 / EPIC-017)

*Epic or card:*

EPIC-010 — Aux narratives and CLI preview (history-locked)

EPIC-017 — Aux narrative QA (QA06/QA07)

*Tokens (titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

`CLI_PREVIEW_ENABLED_OK` — CLI Aux preview surface exists and is wired.

`CLI_PREVIEW_INDEXED_OK` — preview artifacts captured under Evidence Index.

`JSON_CANONICAL_CHECK_OK` — canonical JSON checks for the preview sidecar and mirror records.

`EVIDENCE_INDEX_UPDATED_OK` — Evidence Index updated when preview artifacts change.

`MACHINE_MIRROR_UPDATED_OK` — Machine Mirror refreshed alongside the Evidence Index.

`EVIDENCE_PATHS_VALIDATED_OK` — preview artifact paths validated against the Machine Mirror.

*Evidence / artifacts (titles/paths only):*

`artifacts/cli/narrative/stdout.txt` — canonical LF-terminated Aux preview text for the CLI admin surface.

`artifacts/cli/narrative/sidecar.json` — IDs-only canonical JSON sidecar for the same preview.

`docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` — Human Evidence Index entries and hash sentinel for CLI preview artifacts.

`artifacts/evidence_index.jsonl` — Machine Mirror records for CLI preview artifacts, with `proof_anchor` references to path-proof transcripts.

audit/qa/hde-epic017/logs/step\_aux\_preview1.txt — EPIC-017 QA06 Aux narrative evidence.

audit/qa/hde-epic017/logs/step\_aux\_preview1\_admin.json — EPIC-017 QA07 Aux admin JSON sidecar evidence.

# 

# 

# **Phase VI — Distillation (Evidence & performance)** 

**Phase description:**  
 Integrate gate scripts and evidence harnesses, pack/manifest identity, environment snapshot & observability, and performance/load harnesses to prove determinism, A7 transport posture, rails/DB/BodyGraph mechanics, and evidence-index discipline under canonical JSON.

**Phase master status:** **Not done**

**Notes:**

Harness and gates are specified in canon and PF09.

Release identity core for Freeze-Pack (canonical manifest SoT, byte-identical freeze evidence copy, release\_id recompute proof, and fail-closed identity gate) is now implemented and exercised for the EPIC022 remediation slice (see HDE-DIST002.1–.3).

Environment snapshot, integrated one-button evidence harness coverage beyond release identity, and remaining Phase VI indexing and performance work remain pending.

---

## Task HDE-DIST001 — Gate scripts & evidence harness

**Task ID:** HDE-DIST001

**Task name/label:** Gate scripts & evidence harness

**Task status:** **Not done**

**Task description:**  
 Provide one-button runners that exercise all critical mechanics (determinism, A7, rails, DB posture, BodyGraph) and produce the full set of binary evidence artifacts in a deterministic, repeatable way, with Index/Mirror discipline.

**Task notes:**

This task ties together multiple acceptance dimensions (determinism, transport, rails policy, DB and BodyGraph posture) and a large evidence surface.

PF09 is consumer-only for tokens; semantics live in Governance/CLI/Schemas/Mechanics.

### Subtask HDE-DIST001.1 — Determinism gates

**Subtask name/label:** Determinism & parity gates

**Subtask description:**  
 Implement deterministic gates that:

**Preimage recompute:** Strip `idempotence_hash`, re-serialize the five-key preimage as canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped & ASCII-sorted; `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and compute `sha256(preimage_bytes)`; result must equal the published `idempotence_hash`.

**Reader↔CLI parity:** For a fixed corpus of pairs, run Reader and CLI on the same inputs and byte-compare JSON envelopes; outputs must be identical (single emitter, canonical JSON).

**AB↔BA & two-run identity:** For each Integration pair (e.g., `20–34` vs `34–20`, `20–57` vs `57–20`), show AB/BA narrative & banding coherence and two-run byte identity.

**Canonical JSON compare:** Re-emit a sample of envelopes and verify they are canonical JSON and match their canonical re-serialization.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`PREIMAGE_RECOMPUTE_OK`

`CLI_READER_EMITTER_PARITY_OK`

`CLI_AB_BA_PARITY_OK`

`TWO_RUN_IDENTITY_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

**Determinism / parity:**

**`audit/gates/parity/reader_cli/ab.json`**

**`audit/gates/parity/reader_cli/ba.json`**

**`audit/gates/parity/reader_cli/summary.json`**

**`audit/gates/determinism/abba.bytes`**

**`audit/gates/determinism/tworun_identity.sha256`**

**`audit/gates/canonical_json/json_canon_compare.log`**

**Two-run marker:**

**`artifacts/cards/A3/IDENTITY_OK.txt` — marker card indicating that two-run identity checks have passed for the release corpus.**

**Notes:**

All runs must obey `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

### Subtask HDE-DIST001.2 — A7 transport gates on Catalog route

**Subtask name/label:** A7 & Catalog transport proofs

**Subtask description:**  
 On a **Catalog JSON success route**, prove the full A7 matrix and catalog posture:

200 success with:

`Content-Type: application/json; charset=utf-8`

Strong, quoted ETag over the LF-terminated body.

`Cache-Control: private, max-age=0, must-revalidate`.

`Vary: Authorization, Accept-Encoding`.

HEAD: status 200; no body; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

304: only after a successful 200; no body; omit `Content-Type` and `Content-Length`; validators mirror cached 200\.

POST: non-conditional; never returns 304\.

Writers/errors: `Cache-Control: no-store`; no `ETag` on error responses; errors use `Content-Type: application/json; charset=utf-8`.

Encoding invariance: for a fixed canonical LF-terminated body, ETag and effective `Content-Length` are stable across `identity/gzip/br`.

Env-gating proof: non-prod Catalog entries are unreachable with `APP_ENV=prod`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_ENCODING_INVARIANCE_OK`

`A7_TRANSPORT_PROOF_OK`

`ENDPOINTS_CATALOG_OK`

`ENDPOINTS_CATALOG_ENV_GATE_OK`

**Evidence / artifacts:**

Transport (Catalog route):

`artifacts/reader/endpoints_snapshot.json`

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_writers_errors.txt`

`artifacts/proofs/encoding_invariance.txt`

`artifacts/proofs/endpoints_env_gate_proof.log`

Aux headers-only checks (EPIC-010):

`tests/transport/headers/aux_text_200.snap`

`tests/transport/headers/aux_suppression_200.snap`

**Notes:**

A7 proofs must be captured on a Catalog JSON success route; `/internal/version` is excluded.

### 

### **Subtask HDE-DIST001.3 — CI rails closed/open policy & rails gates**

**Subtask name/label:** CI rails closed/open policy & rails gates

**Subtask description:**  
 Enforce SAFE rails posture for all CI and dev harness runs, with explicit closed/open gates, governed retry/backoff behavior, and typed, numeric-free refusals:

**Rails CLOSED by default.**

Run CI pipelines with rails CLOSED by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).

Under closed rails, vendor and external HTTP calls are not permitted; any attempt to reach a provider must return a typed, numeric-free refusal envelope instead of performing outbound I/O.

**Retry/backoff family (open rails only).**

For any job that opens rails (for example, live vendor or bridge checks), use a policy-pinned retry/backoff family drawn from a closed set `{none, fixed, exponential}` with integer parameters; no jitter is allowed.

Retryable conditions are restricted to `{network_error, 5xx}`; other 4xx responses (beyond the typed 429 behavior below) MUST NOT be retried in this component.

**Closed rails gate.**

Prove there is **no outbound network I/O** under closed rails, including BodyGraph/vendor flows.

Show that refusal envelopes are typed, numeric-free JSON and that logs are keys-only (no payload bodies, header values, or secrets).

Capture a rails posture sanity check log and at least one refusal fixture under closed rails; both artifacts are governed and indexed under the Evidence Index discipline (PF09 does not define their schemas or exact paths; those live in HDE-Governance and HDE-Schemas & Artifacts).

**Open rails gate (pinned).**

Show that retry/backoff behavior matches the pinned profile (family and parameters) and respects the retryable-condition rules above.

Show that `429` responses produce a typed `PROVIDER_RATE_LIMITED` error with `retry_after_ms` only when a valid `Retry-After` header is present; there is no auto-success path in this epic.

Demonstrate that determinism and AB↔BA parity remain intact under open-rails runs (canonical JSON, single LF).

PF09 does not redefine SAFE-rails token semantics or transport matrices; those remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref. This subtask requires that the rails harnesses (closed and open), refusal fixtures, and logs exist and are indexed, and that they prove the SAFE-rails and retry/backoff behavior described above.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`ENV_RAILS_POLICY_OK`

`ENV_LC_ALL_C_OK`

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

Rails CI jobs (titles-only):

`ci/jobs/rails_closed_refusal.yml` — closed-rails refusal and posture sanity.

`ci/jobs/rails_open_conformance.yml` — open-rails retry/backoff and 429 conformance.

`ci/jobs/logs_keys_only_redaction.yml` — keys-only logging and redaction checks.

Rails posture log and refusal fixture for closed rails (titles/paths owned by HDE-Governance and HDE-Schemas & Artifacts).

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### 

### **Subtask HDE-DIST001.4 — DB posture & runtime checks (harness for HDE-FERM004)**

*Subtask name/label:* DB posture & runtime checks (HDE-FERM004 harness)

*Subtask description:*

Use the Distillation harness to **prove and exercise** the DB runtime posture defined in **Task HDE-FERM004 — Database Runtime Posture** for this phase, without redefining posture semantics:

**Semantic home**

DB runtime posture semantics (adapter façade, search\_path, grants, DDL fingerprint, constraints, boundary view posture, bridge fallback, provider parity, and total-failure behavior) are owned by **HDE-FERM004** in Phase V — Fermentation.

This subtask adopts those semantics and focuses on **where** they are proved in the Distillation harness, not on re-specifying behavior.

**Posture artifacts to capture in this harness**

Produce and index the same governed DB posture artifacts required by HDE-FERM004, at minimum:

`artifacts/db/ddl_fingerprint.json` — normalized DDL snapshot of the runtime schema with stable ordering.

`artifacts/db/grants.txt` — baseline roles/grants listing.

`artifacts/db/check_schema.txt` — schema/search\_path echo and verification.

`artifacts/db/check_constraints.txt` — constraint checks (including FK, uniqueness, and invariants called out in epic/spec docs).

`boundary_view.readonly.proof` — boundary view read-only proof (path and schema owned by HDE-Schemas & Artifacts).

`artifacts/runtime/env_connectivity.snapshot.json` — names-only snapshot of how DB connectivity was resolved (dev-only), with schema owned by HDE-Schemas & Artifacts.

When possible, reuse the same scripts and adapter façade entrypoints used for HDE-FERM004 posture captures so that evidence remains consistent across phases.

**Capture discipline (aligned with HDE-FERM004.4)**

Run posture captures under deterministic env pins:

`LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Ensure all governed artifacts are canonical JSON or LF-terminated text:

UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF.

Keep posture artifacts and logs **secret-free** (no credentials or connection strings; logs are keys-only).

**Evidence Index & Mirror**

When this harness adds or updates any DB posture artifacts:

Update `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256` in the same PR.

Update `artifacts/evidence_index.jsonl` under the global Machine Mirror rules (records-only canonical JSONL, unknown-key reject, single file, `proof_anchor` present for each artifact).

PF09 does not define mirror schema or token semantics; it routes to **HDE-Schemas & Artifacts** and **HDE-Governance** by title.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (if verified here; titles-only; tokens live in HDE-Governance / HDE Phased Epics):*

`DB_RUNTIME_SEARCH_PATH_OK`

`DB_ROLE_OK`

`DB_SCHEMA_FINGERPRINT_OK`

`DB_CONN_ENV_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts (titles/paths only):*

`artifacts/db/ddl_fingerprint.json`

`artifacts/db/grants.txt`

`artifacts/db/check_schema.txt`

`artifacts/db/check_constraints.txt`

`boundary_view.readonly.proof`

`artifacts/runtime/env_connectivity.snapshot.json`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### Subtask HDE-DIST001.5 — BodyGraph mechanics gates

**Subtask name/label:** BodyGraph source & policy proofs

**Subtask description:**  
 When verified here, prove BodyGraph behavior:

Source selection and invariance across AB/BA.

Vendor calls disabled in prod as required.

TTL / stale-while-revalidate policy is pinned.

Rate-limit and circuit-breaker policies behave as specified.

**Refresh worker & POLICY alignment (titles-only).** The BodyGraph refresh worker (`scripts/bodygraph/run_refresh_worker.py`) is the dev-only job that drives the TTL/SWR, rate-limit, and circuit-breaker behavior captured in `artifacts/bodygraph/refresh_policy.snapshot.json` and related metrics/logs. PF14 and the ADRs define a v1 nested schema for this snapshot (including `ttl_s`/`swr_s`, nested `rate_limit{requests_per_window,window_s}`, nested `circuit_breaker{fail_threshold,window_s,cooldown_s}`, and a `sample_counts` block with counters such as `refresh_failures`, `breaker_tripped`, and `rate_limit_hits`). This subtask records that the refresh worker’s internal `POLICY` constant and behavior remain in lock-step with that v1 schema and the ADR/snapshot owned by HDE-Build Notes and HDE-Schemas & Artifacts; PF09 does not restate the schema or numeric values here, it only requires that the governed snapshot and associated metrics/logs exist and reflect the policy those documents describe.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (if verified here):**

`BG_SOURCE_SELECTION_OK`

`DEV_DB_BRIDGE_FALLBACK_OK`

`BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`

`BG_SOURCE_INVARIANCE_OK`

`BG_TTL_SWR_POLICY_OK`

`BG_RATE_LIMIT_POLICY_OK`

`BG_CIRCUIT_BREAKER_POLICY_OK`

**Evidence / artifacts:**

BodyGraph proofs:

`artifacts/bodygraph/source_selection.snapshot.json`

`artifacts/bodygraph/source_invariance/ab.json`

`artifacts/bodygraph/source_invariance/ba.json`

`artifacts/bodygraph/source_invariance/summary.json`

`artifacts/bodygraph/refresh_policy.snapshot.json`

`artifacts/bodygraph/metrics.snapshot.json`

`artifacts/bodygraph/keys_only.logs.sample`

### Subtask HDE-DIST001.6 — One-button evidence harness & release sanity pipeline

**Subtask name/label:** One-button evidence harness & release sanity pipeline

**Subtask description:**  
 Implement a one-button runner that executes the release & provenance sanity pipeline end-to-end and fails closed on any drift:

**Ordered steps (minimum sequence).**

Format (code/docs).

Lint / type checks.

Unit \+ property tests (determinism, comparators).

Schema validation (domains and payloads as applicable).

Goldens (AB↔BA, two-run identity, band edges, canonical-compare).

Capture artifacts for **this release**, including at least:

Pack identity artifacts (`artifacts/math/freeze_pack_manifest.json`, `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`).

Reader transport proofs (A7) on a Catalog JSON success route (see A7 tasks and Endpoint Catalog).

Internal-ops `/internal/version` headers/body proofs (see HDE-SEPA004 and runtime packaging tasks).

DB posture artifacts (see DB posture subtasks).

BodyGraph source/policy proofs (see BodyGraph mechanics subtasks).

Index \+ Mirror parity check: update `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in the same commit/PR, then verify:

1:1 join between titles/paths and mirror records.

Canonical JSONL (UTF-8; sorted keys; compact; one LF).

Path-proofs present and referenced by `proof_anchor`.

**Transcript & discipline.**

Emit `artifacts/proofs/sanity_pipeline.transcript.log` capturing ordered steps and pass/fail status.

Run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`; keep all evidence artifacts canonical and secret-free.

PF09 does not redefine token semantics for determinism, A7, `/internal/version`, DB posture, or BodyGraph behavior; those remain single-homed in HDE-Governance, HDE-CLI-API-Vendor-Ref, HDE-Schemas & Artifacts, and Mechanics. This subtask requires that the one-button runner drive all governed gates for a release and enforce Index/Mirror parity for the resulting artifacts.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`artifacts/proofs/sanity_pipeline.transcript.log`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST001.7 — Vendor ingest source policy & proofs**

**Subtask name/label:** Vendor ingest source policy & proofs

**Subtask description:**  
 Prove that the BodyGraph vendor ingest pipeline obeys the environment-aware source policy from Mechanics and Governance and that, for epics which claim **live vendor activity**, there is at least one governed **live vendor transport proof** in addition to offline ingest tests:

**Env-aware source policy (prod vs dev).**

* In **prod**, the database is the source of truth; vendor APIs are never called inline on the hot path. Vendor ingest jobs MUST write via controlled background or admin flows only, consistent with Governance and infra docs (titles-only).

* In **dev** (and other non-prod envs where allowed), direct vendor calls via the adapter façade MAY be used for ingest, but on success the pipeline MUST upsert the BodyGraph into the DB so subsequent reads are repeatable and invariant.

* Under **closed rails** (`SAFE_MODE=1`, `ALLOW_NETWORK=0`), all vendor-bound requests MUST fail closed with a typed refusal envelope; no outbound vendor HTTP is permitted.

**Per-call source selection (no hidden modes).**

* Source selection for BodyGraph flows MUST be **per call** and explicit (for example via CLI flag or ops parameter); there are no hidden “engine modes” that silently flip between DB and vendor.

* For BodyGraph flows, capture a governed source-selection snapshot (for example `artifacts/bodygraph/source_selection.snapshot.json`), showing attempted sources and the selected source for representative calls. Schema and field semantics remain single-homed in HDE-Schemas & Artifacts and Mechanics by title.

**Live vendor transport proofs vs offline ingest tests.**

* Offline ingest tests (unit/integration tests, dry-run pipelines, and source-invariance proofs that never open vendor rails) are **not sufficient** on their own to satisfy “live vendor activity” D-goals; they remain necessary correctness evidence but count as **offline** proofs only.

* For any epic that claims live vendor coverage through this pipeline, Mechanics and QA require at least one **live vendor transport proof**:

  * An Engine/Reader/CLI surface runs under **open rails** (`ALLOW_NETWORK=1` with SAFE rails posture) and makes a real request to a vendor endpoint via the BodyGraph vendor ingest pipeline.

  * Governed evidence for that run MUST record, at minimum:

    * a rails snapshot at call time (names-only env log including `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`);

    * the vendor endpoint hostname/scheme/path and HTTP method (with secrets redacted as required by Governance);

    * the HTTP status code and selected response headers (for example `Date`, `Content-Type`, and rate-limit headers where permitted), plus any vendor-specific error codes needed to interpret the result; and

    * a bounded, names-only or down-sampled view of the body where required for debugging, never raw vendor payloads or PII.

  * The exact artifact names, JSON shapes, and token mapping for these live-vendor proofs (for example, evidence families for live vendor transport) are defined by title in Glow QA Guide, HDE-Phased Epics, HDE-Schemas & Artifacts, and Governance; PF09 records that at least one such artifact MUST exist for any epic that claims live vendor coverage.

**Source invariance and rails-closed vendor behavior.**

* Maintain DB↔vendor **source invariance**: for the same normalized inputs, DB-sourced and vendor-sourced BodyGraph bodies MUST be byte-identical when emitted via the shared presenter/emitter. Use governed invariance artifacts under `artifacts/bodygraph/source_invariance/` (for example `ab.json`, `ba.json`, `summary.json`) to prove `ab_ba_equal: true` where required.

* Under **rails-closed** runs, show that:

  * no outbound vendor HTTP occurs for BodyGraph flows; and

  * vendor-bound attempts yield typed refusal envelopes and keys-only logs (no payload bodies or secret values), consistent with SAFE-rails refusal posture described elsewhere in PF09 and Governance.

**BodyGraph I/O seam boundaries (engine/bodygraph).**

* Network calls for BodyGraph resolution and ingest MUST occur only within the `engine/bodygraph/` seam and only under open network rails (no vendor calls when rails are closed).  
   

* No network I/O occurs in deterministic core modules (`core`, `sampler`, `compat`, `presenter`); vendor/DB I/O is confined to the BodyGraph seam by design.  
   

* Tests exist that assert SAFE\_MODE/ALLOW\_NETWORK gating in the BodyGraph resolver/ingest flows for `source ∈ {vendor, db, auto}` (fail-closed under closed rails; vendor path permitted only when rails are open).  
   

**Acceptance and gating posture.**

* This subtask participates in vendor ingest and rails-policy tokens including:

  * `BG_SOURCE_SELECTION_OK` — governed source-selection snapshot exists and matches policy.

  * `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` — prod posture proves no inline vendor calls on hot paths.

  * `BG_DEV_DIRECT_CALLS_UPSERT_OK` — dev posture proves allowed direct vendor calls upsert into DB.

  * `BG_SOURCE_INVARIANCE_OK` — DB↔vendor invariance proofs exist and are green.

  * `ENV_RAILS_POLICY_OK` — rails posture is consistent with SAFE rails canon.

  * `LIVE_VENDOR_TRANSPORT_OK` — at least one governed live vendor transport proof exists for epics that claim live vendor activity (token semantics and exact artifacts live in Glow QA Guide, HDE-Phased Epics, HDE-Schemas & Artifacts, and Governance; PF09 is consumer-only).

* Offline ingest tests, dry-run pipelines, and source-invariance artifacts remain necessary but do **not** satisfy `LIVE_VENDOR_TRANSPORT_OK` by themselves; that token requires evidence of an actual vendor transport under open rails.

**Subtask status:** **Done**

**Epic or card:**

EPIC-017 (QA08 vendor dry-run resolve) — offline/vendor dry-run slice  
 EPIC-019 (D6 — Live vendor QA and classification, remedial) — open-rails Live Vendor QA harness and artifacts

**Tokens (titles-only; semantics live in Governance / QA / Phased Epics):**

`BG_SOURCE_SELECTION_OK`  
 `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`  
 `BG_DEV_DIRECT_CALLS_UPSERT_OK`  
 `BG_SOURCE_INVARIANCE_OK`  
 `ENV_RAILS_POLICY_OK`  
 `LIVE_VENDOR_TRANSPORT_OK`  
 `EVIDENCE_INDEX_UPDATED_OK`  
 `EVIDENCE_INDEX_MIRROR_OK`  
 `EVIDENCE_PATHS_VALIDATED_OK`  
 `MACHINE_MIRROR_UPDATED_OK`

**Evidence / artifacts (titles/paths only):**

*BodyGraph source selection and invariance artifacts (offline / dry-run slices):*

* `artifacts/bodygraph/source_selection.snapshot.json` — names-only snapshot of attempted and selected sources for BodyGraph flows.

* `artifacts/bodygraph/source_invariance/ab.json` — DB vs vendor AB invariance sample.

* `artifacts/bodygraph/source_invariance/ba.json` — DB vs vendor BA invariance sample.

* `artifacts/bodygraph/source_invariance/summary.json` — summary proving `ab_ba_equal: true` when invariance is implemented.

*Vendor dry-run evidence (EPIC017 QA08; rails and env posture documented in QA logs):*

* `audit/qa/hde-epic017/logs/step_bg_resolve_vendor_dry_run1.txt` — dry-run ingest metadata for `hdctl bg:resolve --source vendor --dry-run` on a synthetic birth tuple and QA user key, showing requested vs resolved source, SAFE rails posture, ingest metadata, `parity_match: true`, and idempotency key details.

*Live vendor transport proofs (EPIC019 D6 — Live vendor QA and classification):*

* Harness:

  * `scripts/qa/d6_live_vendor_qa.py` — open-rails Live Vendor QA harness that:

    * sets `ALLOW_NETWORK=1`, `SAFE_MODE=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` and requires HDAPI credentials (by title);

    * exercises the HDAPI BodyGraph endpoint with a minimal, non-PII BodyGraph payload; and

    * classifies outcomes as `OK` (2xx and parsed), `FAIL_VENDOR` (vendor-side errors like 401/4xx/5xx with parsed error bodies), or `FAIL_TOOLING` (DNS/transport failures, decode errors) without logging secrets.

* Evidence families under `audit/qa/hde-epic019/d6-vendor-live-qa/`:

  * `notes/d6_vendor_live_qa_discovery.md` — discovery notes for D6 (existing vendor surfaces, prior closed-rails posture, open-rails design for this harness).

  * `happy_path.jsonl` — structured JSONL log capturing at least one 2xx response from the HDAPI BodyGraph endpoint under open rails, with:

    * classification `result: "OK"`,

    * a redacted URL (scheme \+ host), HTTP status, and selected response headers, and

    * a parsed, non-PII BodyGraph payload summary.

  * `fail_vendor.jsonl` — structured JSONL log capturing at least one vendor-side error (for example 401 "Invalid API Key") classified as `result: "FAIL_VENDOR"` with parsed error body fields (code, message, status) but no secrets.

  * `fail_tooling.jsonl` — structured JSONL log capturing at least one tooling/infra error (for example hitting `https://invalid.invalid`) classified as `result: "FAIL_TOOLING"`, with status and error details but no secrets.

  * `rails_snapshot.json` — canonical JSON rails snapshot recording the open-rails posture for D6 (including `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `LC_ALL`, `LANG`, `TZ`), the vendor host, surface description (e.g., `engine.cli vendor HTTP POST /bodygraphs`), and PF-canon references by title.

*Human Evidence Index & sentinel:*

* `docs/evidence/INDEX.json` — Human Index entries for the D6 evidence families, with artifact\_keys such as:

  * `"epic019.d6.vendor_live_qa.discovery_notes"` → `audit/qa/hde-epic019/d6-vendor-live-qa/notes/d6_vendor_live_qa_discovery.md`

  * `"epic019.d6.vendor_live_qa.happy_path"` → `audit/qa/hde-epic019/d6-vendor-live-qa/happy_path.jsonl`

  * `"epic019.d6.vendor_live_qa.fail_vendor"` → `audit/qa/hde-epic019/d6-vendor-live-qa/fail_vendor.jsonl`

  * `"epic019.d6.vendor_live_qa.fail_tooling"` → `audit/qa/hde-epic019/d6-vendor-live-qa/fail_tooling.jsonl`

  * `"epic019.d6.vendor_live_qa.rails_snapshot"` → `audit/qa/hde-epic019/d6-vendor-live-qa/rails_snapshot.json`

* `docs/evidence/INDEX.sha256` — sha256 sentinel over canonical `INDEX.json` bytes including the D6 entries.

*Machine Mirror & path-proofs:*

* `artifacts/evidence_index.jsonl` — Machine Mirror records for the D6 evidence families and their path-proofs, following PF12 mirror discipline (records-only canonical JSONL; field order `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`; unknown-key reject; sort-before-write).

* Co-located `*.path_proof.txt` transcripts for each D6 artifact (notes, JSONL logs, rails snapshot), with `proof_anchor` references in the mirror.

*EPIC019 acceptance map and manifest bindings (titles-only):*

* `docs/acceptance_map_epic019.json` — extended with a D6 foundation “D6 — Live vendor QA and classification (HDE-EPIC019 remedial)” and token bindings for `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK`, each wired to the D6 harness and artifacts (`happy_path`, `fail_vendor`, `fail_tooling`, `rails_snapshot`, discovery notes).

* `audit/EPIC019_MANIFEST.json` — updated manifest entries for the D6 artifacts (correct paths, hashes, sizes, roles, and proof\_anchors), consistent with the Human Index and Machine Mirror.

**Notes:**  
 EPIC017 QA08 provides the **offline/vendor dry-run resolve** slice: it exercises `hdctl bg:resolve --source vendor --dry-run` under controlled rails, demonstrates source-selection and invariance behavior, and contributes to `BG_SOURCE_SELECTION_OK`, `BG_DEV_DIRECT_CALLS_UPSERT_OK` (for dev fallback behavior), and `ENV_RAILS_POLICY_OK`.

EPIC019 D6 now supplies the missing **live vendor transport slice**:

* It runs an explicit open-rails Live Vendor QA harness against the HDAPI BodyGraph endpoint, capturing a happy-path 2xx response, a vendor-side failure, and a tooling failure, each classified and logged under governed paths, with an accompanying rails snapshot and discovery notes.

* It wires the new D6 evidence families into the Human Evidence Index and Machine Mirror with path-proofs, and binds the D6 acceptance tokens `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK` in the EPIC019 acceptance map and manifest.

Taken together, the existing offline invariance artifacts, EPIC017 vendor dry-run evidence, and EPIC019 D6 Live Vendor QA harness and artifacts satisfy the vendor ingest source-policy and live-vendor-proof requirements for this Distillation slice. HDE-DIST001.7 is therefore considered **Done**; future vendor ingest work (beyond the current BodyGraph/HDAPI path and EPIC017/EPIC019 coverage) will be tracked via new epics and PF09 rows rather than by reopening this subtask.

### **Subtask HDE-DIST001.8 — Partition plan & verify** 

**Subtask name/label:** Partition plan & verify

**Subtask description:**  
 Enforce EPIC-011’s non-deferred partition stance by producing and indexing partition plan and verification artifacts under governed paths:

`artifacts/db/partition/partition_plan.txt` — planned partition layout for HDE tables in scope.

`artifacts/db/partition/partition_verify.log` — verification output showing that the live DB matches the plan.

For EPIC-011 there is no “defer partition” behavior for these tables: both the partition plan and verify artifacts are required. PF09 does not define partition semantics or thresholds; those remain in HDE-Governance and infra docs. This subtask ensures that the mechanics harness generates the governed artifacts and that they are part of the Evidence Index/Mirror set.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; semantics live in Governance/infra):**

`PARTITION_PLAN_OK`

`DB_SCHEMA_FINGERPRINT_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`artifacts/db/partition/partition_plan.txt`

`artifacts/db/partition/partition_verify.log`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST001.9 — DB–bridge parity & env connectivity**

**Subtask name/label:** DB–bridge parity & env connectivity

**Subtask description:**  
 Prove parity between direct DB reads and bridge-mediated reads for BodyGraph, and capture the associated environment connectivity posture:

**Bridge parity transcripts.**

Produce `artifacts/bodygraph/vendor_upsert.<alias>.json` — vendor upsert transcript for a chosen alias (titles-only to HDE-Schemas & Artifacts for schema).

Produce `artifacts/bodygraph/db_resolve.<alias>.json` — DB resolve transcript for the same alias.

Use `artifacts/presenter/json_canon_compare.log` to show that the DB and bridge bodies are structurally equal under canonical JSON serialization.

**Env connectivity snapshot.**

In the same change window, capture `artifacts/runtime/env_connectivity.snapshot.json` as a canonical JSON snapshot of DB connectivity resolution (dev-only, names-only); schema and required fields are single-homed in HDE-Schemas & Artifacts.

PF09 does not restate the JSON schemas for these artifacts or define DB/bridge policy values; those remain in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed bridge parity and env connectivity artifacts exist, are canonical, and are indexed under the Evidence Index discipline.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; semantics live in Governance/Schemas):**

`DB_CONN_ENV_OK`

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`artifacts/bodygraph/vendor_upsert.<alias>.json`

`artifacts/bodygraph/db_resolve.<alias>.json`

`artifacts/presenter/json_canon_compare.log`

`artifacts/runtime/env_connectivity.snapshot.json`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST001.10 — Architecture snapshot (keys-only) evidence**

**Subtask name/label:** Architecture snapshot (keys-only) evidence

**Subtask description:**  
 Capture and index a keys-only architecture snapshot that reflects the Engine’s public and internal surfaces without exposing secrets or raw payloads:

Emit a governed architecture snapshot artifact (path and schema owned by HDE-Schemas & Artifacts) as canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

Ensure the snapshot is keys-only: no raw birth data, no vendor payloads, no credentials or sensitive header values.

Treat the snapshot as part of the gate harness evidence surface alongside determinism, A7, rails, DB posture, BodyGraph, and narrative key-table artifacts.

PF09 does not define the concrete path or schema for the architecture snapshot; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed snapshot exist, be canonical and secret-free, and be indexed under the global Evidence Index discipline.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; semantics live in Governance/Schemas):**

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

Architecture snapshot artifact (titles-only; schema & path in HDE-Schemas & Artifacts)

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## **Task HDE-DIST002 — Pack/manifest & release identity**

**Task ID:** HDE-DIST002

**Task name/label:** Pack/manifest & release identity

**Task status:** **Partial**

**Task description:**  
 Canonicalize `catalog/manifest.json`, compute and recompute `release_id` as `sha256(canonical_bytes("catalog/manifest.json"))`, enforce manifest structure invariants, and maintain pack/manifest identity artifacts.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done (historical audit note; superseded for EPIC022 identity remediation slice).

**Status (EPIC022 remediation slice):** Core release identity contract is implemented and gated (canonical manifest SoT, byte-identical freeze evidence copy, recompute proof, and fail-closed CI gate). Indexing of identity artifacts in Evidence Index and Machine Mirror remains tracked under HDE-DIST002.4.

### **Subtask HDE-DIST002.1 — Canonical `catalog/manifest.json`**

**Subtask name/label:** Canonical `catalog/manifest.json`

**Subtask description:**  
 Enforce manifest integrity and path invariants for `catalog/manifest.json`:

**Canonical JSON.**

`catalog/manifest.json` MUST be canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF), as defined in HDE-Schemas & Artifacts (titles-only).

**Top-level key set is closed (no extras).**

`catalog/manifest.json` top-level MUST contain exactly: `root`, `version`, `built_at_utc`, `files` (and no other keys).

**File list invariants.**

The manifest’s file list is ASCII-sorted by path.

There are no duplicate paths.

`catalog/manifest.json` MUST NOT appear in its own file list.

**Path constraints & pack root.**

Each listed path is rooted under the pack’s `"catalog/"` tree (path semantics and root rules are single-homed in HDE-Schemas & Artifacts).

Paths are POSIX-style (no `..` segments, no `//` sequences), and each path length is within the governed limits.

These invariants are enforced under the `PACK_ROOT_PINNED_OK`, `MANIFEST_PATH_ASCII_SORT_OK`, and `MANIFEST_NO_DUP_PATHS_OK` token family; PF09 consumes these tokens but does not redefine their semantics.

**Entry identity (by title).**

Per-entry `{path, sha256, size_bytes}` identity is verified via the manifest checksums audit (see HDE-DIST002.3); PF09 does not restate the per-entry schema here.

All manifest checks MUST run under `LC_ALL=C`, `LANG=C`, `TZ=UTC` using canonical JSON rules shared with the rest of the Evidence Index discipline.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC022**

**Tokens:**

`PACK_MANIFEST_NO_SELF_LISTING_OK`

`MANIFEST_PATH_ASCII_SORT_OK`

`MANIFEST_NO_DUP_PATHS_OK`

`PACK_ROOT_PINNED_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

`artifacts/math/freeze_pack_manifest.json`

**Notes:**  
 `catalog/manifest.json` is the single source of truth for Freeze-Pack membership and release identity. `artifacts/math/freeze_pack_manifest.json` is the evidence copy and MUST be byte-identical to `catalog/manifest.json` on canonical bytes (not JSON-equivalent). No derived schema, subset manifest, or alternate contract is permitted at the freeze evidence-copy path.

Any `manifest_snapshot.json` (or similar summary artifacts) are evidence-only and MUST NOT be used as identity inputs or substituted for the Freeze-Pack Manifest.

### **Subtask HDE-DIST002.2 — release\_id compute & recompute**

**Subtask name/label:** release\_id computation & recompute proof

**Subtask description:**

Compute `release_id` as lowercase hex-64 `sha256(canonical_bytes("catalog/manifest.json"))`.

Capture recompute logs showing recomputation equals the on-disk `release_id`, and fail closed on any mismatch.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC022**

**Tokens:**

`RELEASE_ID_RECOMPUTE_OK`

`MANIFEST_SHA256_HEX64_OK`

**Evidence / artifacts:**

`artifacts/math/release_id.txt`

`artifacts/math/release_id_recompute.log`

`tests/scripts/test_release_id_recompute.py`

`tests/transport/test_internal_version_contract.py`

**Notes:**

EPIC022 release-id evidence is canonical at `artifacts/math/release_id.txt` and `artifacts/math/release_id_recompute.log`. Any reference to `audit/gates/release/release_id.txt` is deprecated and MUST NOT be used for evidence indexing or close-pack checks. If a transitional `audit/gates/release/...` file is required, it MUST be produced as a mechanically generated copy sourced from `artifacts/math/`, and indexing/binding remains on the canonical `artifacts/math/` paths.

Fail-closed CI gate (identity recurrence prevention):

* `python scripts/release_id_recompute.py --check` MUST fail closed (non-zero) on any mismatch and MUST NOT introduce alternate release identity semantics.

* `python ci/checks/check_release_identity.sh` is the fail-closed CI identity gate. It enforces closed rails, validates manifest key-set and canonical-bytes posture, asserts byte-equality between `catalog/manifest.json` and `artifacts/math/freeze_pack_manifest.json`, and requires the governed recompute evidence set to exist and be non-empty.

No dual semantics:

* No “branching” semantics are recognized for release identity. Fallback code paths (including /internal/version fallback) MUST derive `release_id` from canonical manifest bytes and MUST NOT hash raw/uncanonical bytes or substitute other manifest-like inputs.

Operator note:

* Running the identity gate or `--check` locally may rewrite `artifacts/math/release_id_recompute.log` as a tool-driven artifact update. In local repos, revert unintended log churn before committing.

### **Subtask HDE-DIST002.3 — Checksums audit**

**Subtask name/label:** Manifest checksums audit

**Subtask description:**  
 Run a checksums audit over manifest-listed artifacts and capture its log. Audit operates on manifest-listed entries and is part of the governed release identity evidence surface.

**Subtask status:** **Done**

**Epic or card:** **HDE-EPIC022**

**Tokens:** **Unknown** (audit behavior; semantics live in canon)

**Evidence / artifacts:**

`artifacts/math/checksums_audit.log`

**Notes:**  
 This log is treated as part of the governed release identity recompute evidence set. It supports the “no drift between manifest-declared identity and on-disk bytes” posture and is expected to be present and non-empty when the release identity gate is claimed as passing.

### 

### Subtask HDE-DIST002.4 — Pack/manifest indexing

**Subtask name/label:** Index pack/manifest identity artifacts

**Subtask description:**  
 Index manifest and release identity artifacts in Human Index and Machine Mirror in the same PR; each mirror record includes a `proof_anchor` path-proof; HDE-Schemas & Artifacts §8.6 is the single home for listing and record types.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-DIST002.5 — Release bindings evidence & indexing**

**Subtask name/label:** Release bindings evidence & indexing

**Subtask description:**  
 Capture and index the release bindings artifact that ties `release_id` to BodyGraph data source policy and refresh behavior:

Produce `artifacts/bodygraph/release_bindings.json` as canonical JSON (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

Record, at minimum, the governed fields `{release_id, data_source_policy, ttl_s, swr_s, snapshot_counts{<snapshot_counts>}}` as defined in HDE-Schemas & Artifacts (titles-only).

Index `release_bindings.json` in `docs/evidence/INDEX.json` and mirror it in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to a co-located path\_proof).

PF09 does not define the JSON schema or semantics of `release_bindings.json`; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed artifact exist, be canonical, and be indexed alongside pack/manifest identity evidence.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`artifacts/bodygraph/release_bindings.json`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-DIST003 — Environment snapshot (singleton) & observability

**Task ID:** HDE-DIST003

**Task name/label:** Environment snapshot (singleton) & observability

**Task status:** **Not done**

**Task description:**  
 Capture a v3 singleton environment snapshot, plus keys-only logs and metrics snapshots, and index them under the Evidence Index discipline.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done; env matrix, metrics, and keys-only log samples are missing.

### Subtask HDE-DIST003.1 — Environment snapshot singleton (v3)

**Subtask name/label:** `env_matrix.snapshot.json` v3 singleton

**Subtask description:**

Produce `artifacts/runtime/env_matrix.snapshot.json` as a **singleton** per repo.

Enforce schema v3 (unknown-key rejection) with canonical JSON (`UTF-8`, sorted keys, compact, one LF).

Minimum shape:

`schema_version: 3`

`default_rails` for `dev/stage/prod/CI` with SAFE\_MODE/ALLOW\_NETWORK pins.

`determinism_pins`: `LC_ALL="C"`, `LANG="C"`, `TZ="UTC"`.

`presence` map for critical env vars (e.g., `DATABASE_URL`, `DB_BRIDGE_URL`, `db_allow_bridge_in_prod`).

`notes: []`.

Open in write mode (overwrite, never append); exactly one JSON object; final LF; no auxiliary content.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`ENV_SNAPSHOT_SINGLETON_OK`

`ENV_SNAPSHOT_SCHEMA_V3_OK`

`ENV_PINS_PRESENT_OK`

**Evidence / artifacts:**

`artifacts/runtime/env_matrix.snapshot.json`

### Subtask HDE-DIST003.2 — Logs observability (keys-only)

**Subtask name/label:** Keys-only logs sample

**Subtask description:**

Ensure logs are keys-only: no raw birth data, no vendor payloads, no secrets.

Redact any key-like values.

Provide a sanitized log sample at `artifacts/bodygraph/keys_only.logs.sample`.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`LOGS_KEYS_ONLY_SAMPLE_OK`

`OBS_KEYS_ONLY_OK`

`BG_PRIVACY_OK`

**Evidence / artifacts:**

`artifacts/bodygraph/keys_only.logs.sample`

### Subtask HDE-DIST003.3 — Metrics observability

**Subtask name/label:** Metrics snapshot

**Subtask description:**

Capture metrics including:

Counters (refresh successes/failures; rate-limit hits; circuit-breaker openings).

Histograms (e.g., `engine.latency_ms`, `presenter.latency_ms`).

Gauges (e.g., staleness%).

Store as canonical JSON at `artifacts/bodygraph/metrics.snapshot.json` (single LF).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`BG_METRICS_OK`

**Evidence / artifacts:**

`artifacts/bodygraph/metrics.snapshot.json`

### Subtask HDE-DIST003.4 — Env snapshot & observability indexing

**Subtask name/label:** Index env snapshot, logs, and metrics

**Subtask description:**  
 Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR to include env snapshot, logs sample, and metrics artifacts, with `proof_anchor` path-proofs.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-DIST004 — Performance & Load Harness

**Task ID:** HDE-DIST004

**Task name/label:** Performance & Load Harness

**Task status:** **Not done**

**Task description:**  
 Provide a non-PII, deterministic performance suite with stable labels, reproducible scenarios, and SLO probes, with evidence and CI jobs.

**Task notes:**

Focus is on reproducible metrics, parity under load, and safe logging.

### Subtask HDE-DIST004.1 — Profiles & run shapes

**Subtask name/label:** Profiles & run shapes

**Subtask description:**  
 Define and run performance profiles for the Engine’s key surfaces and microbenchmarks:

**Surfaces covered:** Reader, Compat, and the Narrative Selection Router (keys-only).

**Profiles:** small / default / long runs; warm vs cold runs; bounded concurrency; rails CLOSED by default unless explicitly opened under the rails gates.

**Microbenchmarks:** compat core computation and narrative key lookups (titles-only to Mechanics/Math for detailed behavior).

PF09 does not define numeric SLO thresholds or success/failure posture; those remain single-homed in Governance. This subtask requires that the performance harness exercise these surfaces and microbenchmarks under the defined profiles.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (performance semantics and SLO tokens live in Governance; PF09 is consumer-only)

**Evidence / artifacts:**

`artifacts/bench/bench_report_{release_id}.json`

### Subtask HDE-DIST004.2 — Metrics & SLO probes

**Subtask name/label:** Metrics, SLOs, and parity under load

**Subtask description:**

Capture percentiles and histograms (e.g., `engine.latency_ms`, `presenter.latency_ms`).

Counters by outcome.

Use bounded labels (`route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`).

Run SLO probes for steady-state latency (p95/p99 bands) and budget for canonicalization and preimage cost.

Prove parity under realistic load.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (SLO semantics are descriptive here)

**Evidence / artifacts:**

`artifacts/bench/bench_report_{release_id}.json`

`artifacts/bench/parity_identity_{release_id}.log`

`artifacts/bench/transport_headers_{release_id}/`

### Subtask HDE-DIST004.3 — Bench CI jobs

**Subtask name/label:** Bench CI orchestration

**Subtask description:**  
 Wire CI jobs for math/transport and vendor-open bench runs and SLO verification:

`ci/jobs/bench_math_transport.yml`

`ci/jobs/bench_vendor_open.yml`

`ci/jobs/slo_verify.yml`

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown**

**Evidence / artifacts:**

The CI job definitions above

### Subtask HDE-DIST004.4 — Performance harness indexing

**Subtask name/label:** Index performance & load artifacts

**Subtask description:**  
 Update Human Index and Machine Mirror in the same PR for bench artifacts (records-only canonical JSONL; one LF; `proof_anchor` present).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-DIST005 — Global discipline (Phase VI)

**Task ID:** HDE-DIST005

**Task name/label:** Global discipline (Phase VI)

**Task status:** **Not done** (treated as an ongoing global requirement)

**Task description:**  
 Enforce that all Phase VI evidence artifacts use canonical encodings and are captured under pinned locale, and that every artifact addition/move/removal is reflected in both Human Index and Machine Mirror in the same PR.

**Task notes:**

All artifacts under evidence are canonical JSON or headers-only text and LF-terminated.

All harnesses and checks that reason about bytes run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Index updates are mandatory for `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl`.

HDE-Schemas & Artifacts §8.6 is the single home for the evidence listing; Appendix C is the single home for record type schemas; PF09 does not redefine them.

### Subtask HDE-DIST005.1 — Canonical encodings & environment pins

**Subtask name/label:** Canonical encodings & LC pins

**Subtask description:**  
 Ensure all Phase VI evidence artifacts:

Use canonical JSON or headers-only text, LF-terminated.

Are produced under `LC_ALL=C`, `LANG=C`, `TZ=UTC` for any byte-sensitive harnesses.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`ENV_LC_ALL_C_OK`

`CI_CHECK_FINAL_LF_OK`

`JSON_CANONICAL_CHECK_OK`

**Evidence / artifacts:**

Various canonical JSON and canonical-compare logs across Phase VI (e.g., `audit/gates/canonical_json/json_canon_compare.log`).

### Subtask HDE-DIST005.2 — Global Index & Mirror discipline

**Subtask name/label:** Evidence Index & Machine Mirror updates

**Subtask description:**  
 For any artifact added/moved/removed in this phase:

Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR.

Keep `artifacts/evidence_index.jsonl` as records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF; unknown-key reject).

Maintain fixed field order and `proof_anchor` to co-located path\_proof files.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

## Task HDE-DIST006 — Identity & Provenance module

*Task name/label:* Identity & Provenance fields, helpers, and evidence

*Task description:*  
 Wire the Identity & Provenance module as the single source of truth for engine and release identity. Identity values are initialized once per cut and are read-only thereafter; all public and operator surfaces consume via helpers (titles-only to PF‑Canon‑HDE‑Mechanics §13). PF09 binds the identity fields, helpers, and evidence artifacts to specific acceptance tokens.

*Task status:* Not done

*Epic or card:* Unknown

### Subtask HDE-DIST006.1 — Identity fields & source-of-truth

*Subtask name/label:* Identity field set & immutability

*Subtask description:*

Ensure the Identity & Provenance module exposes and persists exactly these fields — no extras — as read-only values after freeze (titles-only to Mechanics §13.1):

`engine_tag`

`build_commit`

`invocation_tag`

`invocation_sha256`

`emitter_sha256`

`release_id`

Prove that:

`release_id` is derived only from the PF‑12 freeze pack manifest (`pack/manifest`), as `sha256(canonical manifest bytes)`, and is not recomputed at request time.

`engine_tag`, `build_commit`, `emitter_sha256`, and `invocation_sha256` are taken from the build snapshot at cut time; `invocation_tag` and Invocation bytes come from the Invocation registry (titles-only).

Identity fields are not mutated after freeze and are not overridden by env vars, flags, or other alternate sources on public paths.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; live in Governance / Identity canon):*

`RELEASE_ID_RECOMPUTE_OK`

`TWO_RUN_IDENTITY_OK`

`CLI_READER_EMITTER_PARITY_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts (titles/paths only; schemas live in PF‑Canon‑HDE‑Schemas & Artifacts / PF‑Canon‑HDE‑Mechanics §13.6):*

`artifacts/pack/manifest.json` (or equivalent canonical bytes snapshot) — `pack/manifest`

`artifacts/identity/release_id.json` — `identity/release_id`

`artifacts/identity/release_id_recompute.log` — `identity/release_id_recompute`

### Subtask HDE-DIST006.2 — Identity helpers & parity

*Subtask name/label:* identity\_meta / identity\_admin helpers

*Subtask description:*

Prove that public Reader and CLI code paths obtain identity from the Identity & Provenance module helpers (titles-only to Mechanics §13.2):

`identity_meta()` → `{"engine_tag","invocation_tag"}` is injected into the Reader public envelope before idempotence hashing (preimage) and is present in both Reader and CLI responses on public surfaces.

`identity_admin()` → `{"engine_tag","release_id","invocation_tag","invocation_sha256","build_commit","emitter_sha256"}` is used by internal/admin surfaces (including `/internal/version`) and evidence capture.

Demonstrate CLI↔Reader parity on identity\_meta: the same inputs yield byte-identical public bodies (LF-terminated canonical JSON).

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only):*

`CLI_READER_EMITTER_PARITY_OK`

`TWO_RUN_IDENTITY_OK`

*Evidence / artifacts:*

`artifacts/parity/two_run_identity.log` — `parity/two_run_identity` (two-run identity digest/log for public bodies, LF-terminated)

`artifacts/identity/service_identity.json` — `identity/service_identity` (admin snapshot of identity fields)

### Subtask HDE-DIST006.3 — Identity hashes & mirror discipline

*Subtask name/label:* Identity hashes & Mirror records

*Subtask description:*

Capture and persist build-time hashes for the shared emitter and invocation and index them as identity artifacts (titles-only to Mechanics §13.6):

`identity/emitter_sha256` — hash of the allow-listed presenter/emitter source.

`identity/invocation_sha256` — hash of canonical Invocation bytes.

List the identity artifacts by title/path in `docs/evidence/INDEX.json` and mirror them 1:1 in `artifacts/evidence_index.jsonl` as canonical JSONL (UTF‑8, sorted keys, compact, exactly one LF).

Enforce mirror discipline:

One JSON object per line.

Reject unknown keys in mirror records.

`(artifact_key, discovered_physical_path)` in the mirror matches the human Index entry.

Each record includes a `proof_anchor` path-proof stored alongside the artifact.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only):*

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts:*

`artifacts/identity/emitter_sha256.json` — `identity/emitter_sha256`

`artifacts/identity/invocation_sha256.json` — `identity/invocation_sha256`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

**Acceptance impact**

Tokens referenced (all already defined in PF14 / Governance; no new tokens):

`RELEASE_ID_RECOMPUTE_OK`, `TWO_RUN_IDENTITY_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

These are being **bound** more concretely to identity-module evidence; no new token definitions are introduced.

**Artifacts impact**

New or clarified artifact paths mentioned:

`artifacts/pack/manifest.json` (or equivalent) — `pack/manifest`

`artifacts/identity/release_id.json` — `identity/release_id`

`artifacts/identity/release_id_recompute.log` — `identity/release_id_recompute`

`artifacts/parity/two_run_identity.log` — `parity/two_run_identity`

`artifacts/identity/service_identity.json` — `identity/service_identity`

`artifacts/identity/emitter_sha256.json` — `identity/emitter_sha256`

`artifacts/identity/invocation_sha256.json` — `identity/invocation_sha256`

Schemas and exact field shapes remain routed to PF‑Canon‑HDE‑Schemas & Artifacts / PF14 Mechanics.

# Phase VII — Coagulation (SDKs & runtime packaging) 

**Phase description:**  
 Ship a hardened runtime and minimal client SDKs that emit the six-key public envelope and typed errors, and lock evidence/ops practices to Governance, with no contract bytes or schemas defined here (titles-only routing to canon).

**Phase master status:** **Not done**

**Notes:**

Scope is runtime packaging, production ops posture (including `/internal/version`), A7 behavior on success routes, and minimal SDKs that mirror public contracts.

---

## Task HDE-COAG001 — Packaging & Runtime

**Task ID:** HDE-COAG001

**Task name/label:** Packaging & Runtime

**Task status:** **Not done**

**Task description:**  
 Produce a deterministic, hardened runtime artifact aligned with Governance: reproducible image, env/rails pins, start command capture, ops surface for `/internal/version`, optional caching, and security posture for writers/inputs, with evidence indexed.

**Task notes:**

**Status (Audit v1 — 2025-11-17):** Not done.

Missing tokens (titles-only; tokens live in HDE-Governance):

`SERVICE_START_CMD_CAPTURED_OK`

`GUNICORN_APP_FACTORY_OK`

`ENV_PORT_REQUIRED_OK`

SBOM / start-command / env pins proofs are not yet gathered.

### Subtask HDE-COAG001.1 — Image hygiene

**Subtask name/label:** Runtime image hygiene & reproducibility

**Subtask description:**

Build **reproducible** container images for the engine runtime.

Run as non-root; prefer a read-only filesystem where practical.

Generate a **CycloneDX SBOM** for the runtime image.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (SBOM and reproducibility semantics live in Governance/Security canon)

**Evidence / artifacts:**

`sbom/cyclonedx.json`

`sbom/cyclonedx.json.sha256`

**Notes:**

SBOM must be present and hashed; PF09 only references their paths and gating tokens by title.

### Subtask HDE-COAG001.2 — Env & secrets posture

**Subtask name/label:** Env allow-list & secrets discipline

**Subtask description:**

Enforce an **env allow-list**; ignore or fail on unexpected env keys.

Ensure rails defaults match infra inventory for each environment (dev/stage open; prod/CI closed), per Glow-Infrastructure.

Never log secrets or PII; enforce redaction for any key-like header or token.

Export and verify `LC_ALL=C`, `LANG=C`, `TZ=UTC` in the runtime environment to preserve determinism.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`ENV_LC_ALL_C_OK` (indirectly implied via env pins)

Other env/rails tokens live in Governance; PF09 only routes to them.

**Evidence / artifacts:**

`artifacts/proofs/env_pins.txt` — captures `LC_ALL`, `LANG`, `TZ`, rails posture, and port binding in effect.

### Subtask HDE-COAG001.3 — Start command & service factory

**Subtask name/label:** Service start command & app factory

**Subtask description:**

Capture the exact **production start command** as `artifacts/proofs/start_command_capture.txt` (UTF-8; one LF; no secrets).

Prove the runtime starts via the configured **app factory** (e.g., `adapter.factory:create_app`) rather than ad-hoc entrypoints.

Ensure the service binds `$PORT`, not a hard-coded port (enforce `ENV_PORT_REQUIRED_OK`).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`SERVICE_START_CMD_CAPTURED_OK`

`GUNICORN_APP_FACTORY_OK`

`ENV_PORT_REQUIRED_OK`

**Evidence / artifacts:**

`artifacts/proofs/start_command_capture.txt`

`artifacts/proofs/env_pins.txt` (captures port binding and env pins)

### **Subtask HDE-COAG001.4 — Health & ops surface `/internal/version`**

*Subtask name/label:* `/internal/version` ops surface behavior

*Subtask description:*  
 Implement and prove `/internal/version` behavior, aligned with the Identity & Provenance Module (§13) and Internal Meta Surface (§14) in the Mechanics guide (titles-only). This subtask pins the ops transport posture, payload shape, and evidence artifacts for the internal meta endpoint:

GET `/internal/version` is **operator-only**, always:

`Cache-Control: no-store`

**No ETag**

`Content-Type: application/json; charset=utf-8`

**No `Last-Modified` header**

HEAD `/internal/version`:

Returns 200 with no body.

Mirrors 200 validators, including `Content-Type`.

`Content-Length == len(identity GET body)` (LF-terminated canonical body).

Conditionals (`If-Modified-Since`, `If-None-Match`) are **ignored**; the endpoint never returns 304 and is not A7-eligible.

Body:

Body is canonical JSON (UTF‑8, no BOM, compact, exactly one trailing LF).

Key order is **frozen** and matches the Identity & Provenance / Internal Meta spec (titles-only to Mechanics §13–§14):

`engine_tag`

`build_commit`

`invocation_tag`

`invocation_sha256`

`emitter_sha256`

`release_id`

Values are sourced via `identity_admin()` from the Identity & Provenance module (no direct env reads at emit time; no mutation after freeze).

Token emission gating (no “false OK”):  
 A tool MUST NOT emit any \*\_OK token for `/internal/version` unless the corresponding invariant has been verified against the same captured bytes that are being written as governed artifacts for that run. If the run status is FAIL\_TOOLING (or equivalent), the tool MUST NOT emit \*\_OK tokens for invariants that did not pass (including integrity-success claims such as path-proof match or two-run identity).

Coupling requirement (anti-mixed-target / anti-redirect drift):  
 For each probe run, the evidence must be coupled such that emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target and response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit \*\_OK tokens.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens (titles-only; live in HDE-Governance):*

`INTVER_200_CTYPE_JSON_UTF8_OK`

`INTVER_HEAD_PARITY_OK`

`INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`

`INTVER_200_NO_ETAG_OK`

`TWO_RUN_IDENTITY_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

*Evidence / artifacts:*

`artifacts/ops/internal_version/headers_get.txt` — raw GET headers (`intver/headers_get`)

`artifacts/ops/internal_version/headers_head.txt` — raw HEAD headers (`intver/headers_head`)

`artifacts/ops/internal_version/body_get.json` — exact LF-terminated GET body (`intver/body_get`)

`artifacts/ops/internal_version/cond_if_none_match_headers.txt` — GET with `If-None-Match` still returning 200 (`intver/cond_if_none_match`)

`artifacts/ops/internal_version/cond_if_modified_since_headers.txt` — GET with `If-Modified-Since` still returning 200 (`intver/cond_if_modified_since`)

`artifacts/ops/internal_version/two_run_identity.log` — two-run identity log for `/internal/version` (`intver/two_run_identity`)

**Artifacts impact**

New or refined artifact paths (canonical filename set; single home):

`artifacts/ops/internal_version/body_get.json` (canonical body; replaces generic `body.json` naming)

`artifacts/ops/internal_version/body_get.sha256`

`artifacts/ops/internal_version/headers_get.txt`

`artifacts/ops/internal_version/headers_head.txt`

`artifacts/ops/internal_version/cond_if_none_match_headers.txt`

`artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

`artifacts/ops/internal_version/two_run_identity.log`

**Permitted alias copies (compatibility-only; conditional snapshot files only):**

`artifacts/ops/internal_version/cond_if_none_match.txt`

`artifacts/ops/internal_version/cond_if_modified_since.txt`

**Rules (EPIC022 bridge):**

* EPIC022 Live QA MUST produce the internal\_version evidence bundle using the canonical filename set above.

* EPIC022 Live QA MAY additionally emit the two alias copies above to satisfy acceptance binding naming drift. No other filename variants are permitted.

* Evidence indexing keys MUST map to the canonical filenames; alias files are compatibility-only.

**Acceptance impact**

Tokens referenced here: see the canonical token registry in **HDE Governance** (titles-only). This document must not maintain an independent roster; any token name used in step logs or acceptance artifacts must already exist in the registry.

All tokens already exist in Governance / PF14; we only clarify which artifacts and checks satisfy them for `/internal/version`.

**Artifacts impact**

New or refined artifact paths:

`artifacts/ops/internal_version/body_get.json` (canonical body; replaces generic `body.json` naming)

`artifacts/ops/internal_version/cond_if_none_match.txt`

`artifacts/ops/internal_version/cond_if_modified_since.txt`

`artifacts/ops/internal_version/two_run_identity.log`

`artifacts/ops/internal_version/provenance_note.json`

These correspond to PF14’s `intver/*` artifact keys; schemas remain routed to PF‑Canon‑HDE‑Schemas & Artifacts.

**Canon note (proof artifact is single-home):**  
 `artifacts/ops/internal_version/two_run_identity.log` is the **single governed proof artifact** for `/internal/version` coupling \+ two-run identity. It MUST include:

* Two-run identity result (explicit byte-identity pass/fail for two consecutive captures, with compared digests/identifiers).

* Coupling verification result (explicit pass/fail checks that `/internal/version` fields match their governing identity sources, including `release_id` coupling).

* Rails posture reference and determinism pins reference (names-only pointers; determinism pins themselves remain proven by their canonical governed log).

No new acceptance tokens are introduced for “coupling proof”; bind this proof under the existing identity/internal-version token set.

Clarification (proof format): “the endpoint returns fields” is not a coupling proof. The proof must be a stable, reviewable artifact with explicit pass/fail checks and referenced governing sources, as described above.

### **Subtask HDE-COAG001.5 — Optional production caching**

*Subtask name/label:* Private Reader cache (optional)

*Subtask description:*

If a production cache is used, provide a **private, composite-key cache** for Reader and Compat that preserves A7 transport rules and deterministic invalidation:

**Composite key (keys-only).**

Use a composite cache key of the form:

`{viewer_id | person_id(s)}, design_fingerprint, thresholds_identity, release_id`.

Normalize `{a,b}` pairs to a stable order before keying (AB↔BA neutrality) so that compat/Reader responses for `(A,B)` and `(B,A)` hit the same cache entry.

Include `viewer_id` in the key **only** when cacheable output depends on viewer preferences (e.g. perspective); otherwise, omit it so that the same content is shared across viewers.

**Deterministic key construction.**

Key construction must be pure and reproducible:

No dependence on clocks, randomness, or ambient environment state.

Derived only from the normalized inputs and identity fields listed above (titles-only to Mechanics/Math for design\_fingerprint and thresholds\_identity semantics).

**A7-consistent transport behavior.**

Cache hits must preserve full A7 semantics for the success route:

200: `Content-Type: application/json; charset=utf-8`; strong, quoted ETag over the LF-terminated body (pre-compression); `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.

304: only after a prior 200 for the same ETag; no body; omit `Content-Type` and `Content-Length`; validators mirror the cached 200; ETag present.

HEAD: status 200; no body; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

Writers and errors **bypass** the cache and continue to send `Cache-Control: no-store` with **no ETag**; cached paths must not alter typed error envelopes.

`/internal/version` is never cached.

**Deterministic invalidation.**

Invalidate cache entries immediately on any change to:

`release_id`,

`thresholds_identity`,

design/manifest identity (design\_fingerprint or pack/manifest identity), or

input payloads that affect the response (including viewer\_prefs when present).

Once invalidated, no stale bytes may be served; cache re-populates only via fresh emissions under the same A7 posture.

**Controls & diagnostics.**

Default **OFF**: the production cache is disabled by default and may be enabled **only** via a documented runtime flag or configuration toggle; PF09 does not pin the flag name or config path.

Metrics:

Emit **bounded** counters for cache hits, misses, and invalidations (labels such as `route`, `outcome`, `rails_state`, `timeout_profile`), reusing the global observability/metrics discipline.

Optional diagnostics:

When enabled for debugging, maintain a redaction-safe, keys-only debug log of cache decisions (hits/misses/invalidation) suitable for local analysis; routes, IDs, and state are logged via bounded labels only; no raw payloads or secrets may appear.

PF09 does not define cache internals, SLO thresholds, or diagnostics log paths; those remain single-homed in Governance, Mechanics, and infra/ops docs. This subtask records that, when a production cache is present, it obeys composite-key, determinism, A7-consistent transport, deterministic invalidation, metrics, and optional diagnostic logging as described above.

*Subtask status:* Not done

*Epic or card:* Unknown

*Tokens:* (unchanged; semantics live in Governance; PF09 routes by title only)

*Evidence / artifacts:* (unchanged; cache behavior is supported by existing A7 and parity/observability evidence from other phases)

### Subtask HDE-COAG001.6 — Security posture for writers & inputs

**Subtask name/label:** Writers & input security posture

**Subtask description:**

Apply per-route **rate limits** on writer endpoints; no unbounded fan-out.

Writers and error routes always send `Cache-Control: no-store` and **never send ETag**.

Inputs are validated against schemas (titles-only to HDE-Schemas & Artifacts).

Never log secrets or PII; enforce redaction at the logger boundary.

For browser-facing writers: rotate CSRF token on login and allow exactly one safe retry on CSRF failure.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; PF09 consumer-only):**

A7-related success tokens (for success routes, not writers):

`READER_200_CTYPE_JSON_UTF8_OK`

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`A7_ENCODING_INVARIANCE_OK`

Body parity & pack identity:

`MANIFEST_SHA256_HEX64_OK`

`RELEASE_ID_RECOMPUTE_OK`

`PACK_MANIFEST_NO_SELF_LISTING_OK`

Packaging & Ops:

`SERVICE_START_CMD_CAPTURED_OK`

`GUNICORN_APP_FACTORY_OK`

`ENV_PORT_REQUIRED_OK`

**Evidence / artifacts:**

Writer-specific logs and DDL updates would be indexed via Evidence Index; PF09 only lists high-level paths under other phases.

### Subtask HDE-COAG001.7 — Packaging & runtime indexing

**Subtask name/label:** Index runtime & A7 evidence artifacts

**Subtask description:**  
 For the runtime-related artifacts in this task:

Update, in the same PR:

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

Keep the Machine Mirror as **records-only canonical JSONL** (UTF-8; one LF per record; unknown-key reject; fixed field order; `proof_anchor` to co-located `path_proof.txt`).

Rely on HDE-Schemas & Artifacts §8.6 and Appendix C for entry listings and record-type schemas.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-COAG001.8 — Health/ready probes & graceful shutdown**

**Subtask name/label:** Health/ready probes & graceful shutdown

**Subtask description:**  
 Prove that the runtime exposes canonical health/readiness endpoints and shuts down gracefully:

**HTTP probes.**

Expose `/healthz` as a liveness probe (process up, core initialized).

Expose `/readyz` as a readiness probe (emitter wired, pack loaded, manifest hashed, rails posture read).

Both probes return minimal, numeric-free JSON bodies that are canonical (UTF-8; no BOM; ASCII-sorted keys; compact; exactly one trailing LF), using the shared presenter/emitter and global canonical JSON rules.

**Lifecycle & graceful shutdown.**

On `SIGTERM`, stop accepting new traffic, allow in-flight requests to complete, and then exit cleanly with status 0\.

Emit a final readiness/health snapshot (or log) that clearly indicates the “stopping” state, without leaking payloads or secrets.

**Evidence & indexing.**

Capture governed health/ready and shutdown artifacts (titles and paths owned by the Documentation Artifacts and Registry section) and index them under the Evidence Index discipline: list them in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path\_proof files).

PF09 does not define the exact JSON schema or artifact paths for the probes and lifecycle logs; those remain single-homed in HDE-Schemas & Artifacts and HDE-Governance. This subtask requires that the governed probes and lifecycle behavior exist, are canonical and numeric-free, and are evidenced and indexed.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; semantics live in Governance/Schemas):**

`JSON_CANONICAL_CHECK_OK`

`ENV_LC_ALL_C_OK`

`CI_CHECK_FINAL_LF_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

Health/ready probe artifacts and lifecycle/shutdown logs (titles/paths listed in §36 Documentation Artifacts and Registry).

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

### **Subtask HDE-COAG001.9 — CLI packaging & terminal access (pre-Glow prod)**

**Subtask name/label:** CLI packaging & terminal access (pre-Glow prod)

**Subtask description:**  
 Treat the canonical CLI (hdctl or successor) as a required admin product surface in the pre-Glow period and ensure it can be installed and used from a generic terminal to reach Railway prod and obtain the full product payload:

**Packaging & entrypoints (terminals, not just Codespaces).**

Provide a documented way to install or run the canonical CLI from a **generic shell**, not only from GitHub Codespaces, against the production HD Engine on Railway (per Glow-Infrastructure §2.2/§2.6; titles-only).

Acceptable forms include, for example (titles-only):

A packaged CLI (binary or pip-installable tool) with a pyproject console\_script entrypoint.

A module runner path (`python -m engine.cli`).

A containerized CLI that can be invoked from any shell that can reach Railway.

The packaging must preserve the existing CLI surface defined in HDE-CLI-API-Vendor-Ref (PF05) — commands/flags/behavior remain governed there; this subtask does not redefine CLI bytes or flags.

**Terminal CLI access requirement (pre-Glow).**

In pre-Glow production, any shell that can reach the Railway HD Engine base URL and/or DB (per Glow-Infrastructure §2.6; titles-only) **MUST** be able to:

Install and invoke the canonical CLI using documented entrypoints, **and**

Use CLI subcommands defined in PF05 (for example some composition of `bg:resolve`, `showcompat`, `aux-preview`) to obtain the **full product payload** for a match:

Per-person BodyGraphs (from the existing resolver mechanics).

Compat results with numeric scores and bands.

Three Aux narratives (A→B, B→A, shared) for the match.

Admin GUI alone is **not** sufficient; a build that cannot be exercised from a terminal CLI (within pre-Glow rails) is considered incomplete for this packaging/runtime slice.

**Rails & pre-Glow constraints (titles-only).**

All CLI runs used as evidence here MUST respect the pre-Glow prod rails and constraints already recorded in PF14/PF19/PF07:

No app-level user model; no persistent user-bound BodyGraph rows in prod.

`--user` remains an ephemeral QA key; `bg:resolve --source=vendor --upsert` MUST NOT be used in prod until a future epic explicitly re-opens user-bound upsert flows.

Full payload must therefore be produced via stateless/dry-run flows and/or non-upserting DB paths, within SAFE rails policy (closed by default; explicit open-rails windows governed by HDE-Governance).

This subtask does **not** relax SAFE rails, network policy, or upsert prohibitions; it only requires that, *within* those rails, a terminal CLI remains a usable admin surface for the full product payload.

**Subtask status:** **Not done**

**Epic or card:** **Unknown** (future Admin/Packaging epic; titles-only until assigned)

**Tokens (titles-only; PF09 is consumer-only):**

Existing CLI conformance and install tokens (to be reused):

`CLI_PYPROJECT_ENTRYPOINT_OK`

`CLI_MODULE_RUN_OK`

`CLI_INSTALL_OK`

`CLI_HELP_EXIT_0_OK`

`CLI_HELP_STDOUT_OK`

Canonical JSON and evidence tokens:

`JSON_CANONICAL_CHECK_OK`

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts (titles/paths only; to be supplied by future epic):**

CLI install/help/version logs captured from at least one **non-Codespaces** terminal environment (for example a clean local shell) showing:

Successful install or container run.

`hdctl --help` and `hdctl --version` exiting with code 0 and writing to stdout only.

Available subcommands matching PF05’s CLI catalog (at minimum: `showcompat`, `aux-preview`, `bg:resolve`).

At least one prod-against-Railway QA run from a generic terminal that:

Uses CLI alone (or CLI \+ a thin harness script) to accept a canonical pair input (fixture or births).

Produces a **full product payload** bundle containing both BodyGraphs, compat scores/bands, and three narratives (A→B, B→A, shared).

Stores the resulting bundle JSON under a governed path (for example `Audit/QA/...` or `artifacts/cli/admin_bundle.json`), with:

A sibling path-proof transcript (`*.path_proof.txt`).

Entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` (Machine Mirror) in the same PR, following the global Evidence Index discipline.

**Notes:**  
 SoT: canon — this subtask records that **terminal CLI access to the full product payload is a required product surface** before Glow App integration, echoing the Product Owner’s decision in Addendum 11\. Mechanics for CLI commands/flags, admin bundle composition, and HTTP admin bundle routes will be pinned in PF05/PF14/PF19/PF07; PF09 tracks that a packaging/runtime slice exists to make CLI usable from any terminal that can reach Railway prod and to capture governed evidence for such runs.

---

## Task HDE-COAG002 — SDKs (TypeScript / Python)

**Task ID:** HDE-COAG002

**Task name/label:** SDKs (TypeScript / Python)

**Task status:** **Not done**

**Task description:**  
 Provide minimal TypeScript and Python SDKs that mirror the six-key public envelope and typed error contracts, ensuring canonical JSON behavior and parity with Reader, with no public numerics or hidden behavior.

**Task notes:**

SDKs must route contract ownership by title to HDE-CLI-API-Vendor-Ref; PF09 does not restate schemas or bytes.

### Subtask HDE-COAG002.1 — Models & serialization

**Subtask name/label:** SDK data models & canonical JSON serialization

**Subtask description:**

Define strongly-typed models for:

The six-key success envelope.

Typed error shapes.

Route contract ownership (by title) to HDE-CLI-API-Vendor-Ref.

Implement canonical JSON serialization in SDKs:

UTF-8, no BOM.

Sorted keys.

Compact (no extra whitespace).

Exactly one trailing LF.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`SDK_ROUND_TRIP_CANONICAL_JSON_OK` (implicitly depends on canonical serialization)

**Evidence / artifacts:**

Type and schema fixtures:

`sdks/typescript/schemas/*.json`

`sdks/python/schemas/*.json`

### Subtask HDE-COAG002.2 — Round-trip & Reader parity

**Subtask name/label:** Round-trip and Reader/error parity

**Subtask description:**

Ensure `serialize → parse → serialize` is **byte-exact** for valid payloads (canonical JSON round-trip).

For a shared test corpus, show SDK responses match Reader’s public envelope and typed error shapes exactly:

No extra fields.

No missing fields.

No renaming.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`SDK_ROUND_TRIP_CANONICAL_JSON_OK`

`SDK_READER_PARITY_OK`

`SDK_ERROR_CONTRACT_PARITY_OK`

**Evidence / artifacts:**

Test outputs:

`sdks/typescript/tests/*`

`sdks/python/tests/*`

Artifacts per SDK:

`sdks/<lang>/artifacts/schema_hashes.json`

`sdks/<lang>/artifacts/reader_roundtrip.bytes`

`sdks/<lang>/artifacts/error_contract_snapshot.json`

### Subtask HDE-COAG002.3 — Optional retries & conditional GET

**Subtask name/label:** Optional conditional GET helper

**Subtask description:**

Default: **no automatic retries**; SDK must not introduce its own retry policy.

Where implemented, a conditional GET helper for Reader:

Constructs headers according to the same rules as the core (titles-only).

Must not change ETag semantics.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (conditional GET behavior is referenced by title only)

**Evidence / artifacts:**

`sdks/<lang>/artifacts/conditional_get_headers.snap` (if implemented)

### Subtask HDE-COAG002.4 — SDK artifacts indexing

**Subtask name/label:** Index SDK evidence artifacts

**Subtask description:**  
 Update Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR for all SDK artifacts; ensure mirror records follow HDE-Schemas & Artifacts §8.3/§8.6 (canonical JSONL, single file, `proof_anchor`, governed paths).

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

## Task HDE-COAG003 — Runbooks & Deployment Guards

**Task ID:** HDE-COAG003

**Task name/label:** Runbooks & Deployment Guards

**Task status:** **Not done**

**Task description:**  
 Codify a repeatable go-live and rollback process that enforces Doc-Delta discipline, release identity, Index parity, parity/rails/ops gates, and alerting on critical failures.

**Task notes:**

Phase describes **Build → Verify → Release → Rollback** flows, pre-flight CI jobs, and metrics/alerts, but they are not yet fully implemented or evidenced.

### **Subtask HDE-COAG003.1 — Build/Verify/Release/Rollback & incident runbooks**

**Subtask name/label:** Build/Verify/Release/Rollback & incident runbooks

**Subtask description:**  
 Write concise, operator-focused runbooks for:

**Build → Verify → Release → Rollback** flows, covering:

Regenerating `release_id` from the canonical manifest (via SHA-256).

Rebuilding and verifying evidence for A7, determinism & parity, DB posture, and BodyGraph invariance.

Updating the Human Evidence Index, hash sentinel, and Machine Mirror (same PR).

Performing a safe rollback that preserves data safety and verifies no stale cache entries or A7 breakage.

**Incident handling:**

Elevated `5xx` rates on Reader/Compat surfaces.

Slow Reader/Compat responses (latency regressions).

Stuck queue or processing backlog.

DB lag or degraded DB posture.

Runbooks SHOULD reference the “pointer-flip” rollback pattern by title (flipping pointers to the last known-good `release_id`) where appropriate; PF09 does not restate pointer mechanics or DB migration steps. This subtask requires that operational runbooks exist, are kept in sync with release identity and evidence practices, and are captured as governed artifacts.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (runbooks themselves are not token-gated; tokens apply to the mechanics they orchestrate)

**Evidence / artifacts:**

`docs/runbooks/*.md`

### 

### Subtask HDE-COAG003.2 — Pre-flight CI jobs

**Subtask name/label:** Pre-flight CI gate jobs

**Subtask description:**  
 Add pre-flight CI jobs that **fail fast** on:

Parity drift (CLI↔Reader / SDK↔Reader).

Canonical bytes mismatch (JSON canonicalization).

Stale `docs/evidence/INDEX.json` vs `artifacts/evidence_index.jsonl`.

ETag invariance / A7 regressions.

Rails posture violations and missing env pins.

429 handling regressions.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

Likely re-use of parity, JSON canonical, A7, env, and evidence tokens listed in other phases; PF09 only references them by name.

**Evidence / artifacts:**

`audit/gates/ops/release_dryrun.log` (dry-run output can be part of pre-flight verification)

### **Subtask HDE-COAG003.3 — Ops metrics, dashboards & alerting**

**Subtask name/label:** Ops metrics, dashboards & alerting

**Subtask description:**  
 Configure production metrics, dashboards, and alerts with bounded labels and actionable signals:

**Surfaces & dashboards.**

Provide dashboards for Reader, Compat, the Narrative Selection Router, and the Server Cache.

Include panels for:

Latencies and error rates by surface.

Cache hit/miss ratios and cache-related latencies.

Rate-limit outcomes.

A7 headers health on the Catalog JSON success route (e.g., ETag, Vary, cache headers).

**Metrics & labels.**

Use bounded labels such as `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`.

Capture counters, histograms, and gauges for request counts, latency percentiles, cache hits/misses, rate-limit outcomes, and BodyGraph ingest signals (titles-only to Mechanics/Distillation for schema).

**Alerts.**

Define alerts for:

Unexpected spikes in `5xx` and `429`.

Circuit-breaker activations.

A7 invariant failures or degraded A7 headers health.

Evidence indexing failures (missing mirror records or `proof_anchor` mismatches).

Cache hit-ratio or latency breaching agreed budgets.

PF09 does not define SLO thresholds or alert routing; those remain single-homed in Governance and ops docs. This subtask requires that metrics/dashboards reflect the key Engine surfaces and cache, and that alerts are wired to error/latency/A7/evidence/cache health in a bounded, non-PII way.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:** **Unknown** (SLO/alert tokens, if any, live in Governance; PF09 is consumer-only here)

**Evidence / artifacts:**

`artifacts/ops/alerts/*.json`

### Subtask HDE-COAG003.4 — Runbook & ops indexing

**Subtask name/label:** Index runbooks and ops artifacts

**Subtask description:**  
 Update Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR for runbooks, ops dry runs, and alert configs. Mirror must follow HDE-Schemas & Artifacts §8.3/§8.6 (canonical JSONL, one file, unknown-key reject, `proof_anchor` path-proofs). PF09 depends on Governance and Schemas for token semantics and record schemas; it only requires evidence presence and indexing.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens:**

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_INDEX_HASH_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

`EVIDENCE_PATH_PROOFS_OK`

`CI_CHECK_MIRROR_SCHEMA_OK`

`CI_CHECK_FINAL_LF_OK`

**Evidence / artifacts:**

`docs/evidence/INDEX.json`

`docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

---

### **Subtask HDE-COAG003.5 — Post-deploy smoke harness & indexing**

**Subtask name/label:** Post-deploy smoke harness & indexing

**Subtask description:**  
 Provide a post-deploy smoke harness that runs against the live production environment immediately after deploy and captures a minimal, governed evidence set:

**Scope & pins.**

Run all smoke checks under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

Use a JSON success route listed in `docs/ENDPOINTS_CATALOG.json` as the A7 smoke surface; `/internal/version` remains ops-only and not A7-eligible.

**Success route (A7) transport smoke.**

Capture headers-only proofs for:

`artifacts/proofs/success_get.txt` — 200 with strong quoted ETag, JSON Content-Type, Cache-Control, and Vary.

`artifacts/proofs/success_head.txt` — HEAD parity (no body; validators mirror 200; Content-Type \== GET; Content-Length \== identity 200 body).

`artifacts/proofs/success_304.txt` — 304 only after a prior 200; no body; omit Content-Type and Content-Length; validators mirror cached 200\.

`artifacts/proofs/success_writers_errors.txt` — writers/errors posture (no-store, no ETag; error Content-Type).

**Writers & errors posture smoke.**

Confirm that writers and error routes on the exercised surfaces send `Cache-Control: no-store` and no ETag, and that errors are typed, numeric-free JSON with `Content-Type: application/json; charset=utf-8`, as governed by HDE-CLI-API-Vendor-Ref and HDE-Governance.

**Internal ops `/internal/version` smoke.**

Capture:

`artifacts/ops/internal_version/headers_get.txt` and `headers_head.txt` — GET/HEAD 200 posture (no-store, no ETag; HEAD mirrors GET validators; Content-Length matches LF-terminated body).

`artifacts/ops/internal_version/cond_if_none_match_headers.txt` and `cond_if_modified_since_headers.txt` — conditionals ignored; endpoint never returns 304\.

`artifacts/ops/internal_version/body_get.json` and `body_get.sha256` — canonical JSON body and its hash.

`artifacts/ops/internal_version/provenance_note.md` — human-readable provenance note for the deployed release.

**DB posture smoke.**

Reuse DB posture artifacts from the DB posture tasks to spot-check live DB:

`artifacts/db/ddl_fingerprint.json`, `artifacts/db/grants.txt`, `artifacts/db/check_schema.txt`, `artifacts/db/check_constraints.txt`.

Optional: `artifacts/db/partition_plan.txt` and `artifacts/db/db_rw_smoke.log` for partition and read/write smoke where run.

**Pins & harness evidence.**

Capture `artifacts/proofs/env_pins.txt` showing runtime env pins and rails posture in effect during smoke.

**Indexing.**

List all smoke artifacts in `docs/evidence/INDEX.json` and mirror them in `artifacts/evidence_index.jsonl` in the same PR, using canonical JSONL (one LF; unknown-key reject; fixed field order; `proof_anchor` to co-located path\_proof transcripts).

PF09 does not redefine A7, writers/error, INTVER, or DB token semantics; those remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref. This subtask requires that a post-deploy smoke harness exist, capture the governed artifacts above, and satisfy Evidence Index & Mirror discipline.

**Subtask status:** **Not done**

**Epic or card:** **Unknown**

**Tokens (titles-only; semantics live in Governance/Schemas):**

`A7_GET_QUOTED_ETAG_OK`

`A7_HEAD_PARITY_OK`

`A7_304_OMITS_CT_CL_OK`

`A7_VARY_AUTH_AE_OK`

`READER_200_CTYPE_JSON_UTF8_OK`

`INTVER_200_CTYPE_JSON_UTF8_OK`

`INTVER_HEAD_PARITY_OK`

`INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`

`INTVER_200_NO_ETAG_OK`

DB posture tokens (e.g., `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`)

`EVIDENCE_INDEX_UPDATED_OK`

`EVIDENCE_INDEX_MIRROR_OK`

`EVIDENCE_PATHS_VALIDATED_OK`

**Evidence / artifacts:**

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_writers_errors.txt`

`artifacts/ops/internal_version/headers_get.txt`

`artifacts/ops/internal_version/headers_head.txt`

`artifacts/ops/internal_version/cond_if_none_match_headers.txt`

`artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

`artifacts/ops/internal_version/body_get.json`

`artifacts/ops/internal_version/body_get.sha256`

`artifacts/ops/internal_version/provenance_note.md`

`artifacts/db/ddl_fingerprint.json`

`artifacts/db/grants.txt`

`artifacts/db/check_schema.txt`

`artifacts/db/check_constraints.txt`

`artifacts/db/partition_plan.txt` (if used)

`artifacts/db/db_rw_smoke.log` (optional)

`artifacts/proofs/env_pins.txt`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

## Task HDE-COAG004— Stateless JSON QA mode (non-gating tracker)

*Task ID:* HDE-COAG004  
 *Task name/label:* Stateless JSON QA mode (non-gating tracker)  
 *Task status:* Not done

*Task description:*  
 Track the future stateless JSON QA mode described in PF14 and ensure it does not accidentally become a merge-blocking gate before the owning epic lands:

**Scope and ownership (titles-only).**

PF14 — HDE-Mechanics Guide §17.9 (“Stateless JSON QA mode”) and HDE-Build Notes Addendum 11 define a future, no-DB JSON QA mode for BodyGraph export, compat export, and vendor-to-engine pipelines.

HDE-Schemas & Artifacts, HDE-CLI-API-Vendor-Ref, Glow QA Guide, and HDE Phased Epics remain the single homes for schemas, CLI command shapes, QA plans, and acceptance wiring for these stateless flows.

**Non-gating posture.**

Until the stateless JSON QA mode is implemented and drained into PF04/PF12/PF19/PF20 with explicit tokens, no PF09 acceptance token or CI job may treat the presence or absence of stateless JSON QA artifacts as a merge-blocking gate.

PF09 continues to gate the current DB-backed engine and CLI flows for this slice (BodyGraph, compat, Reader, Aux), as defined elsewhere in this checklist.

**Documentation discipline.**

When the stateless JSON QA epic is created, reference it in this row by title only and update task status, but do not define new transport bytes or schemas here; PF09 only tracks that the epic exists and whether its acceptance tokens are wired.

*Task notes:*  
 This task exists to mirror PF14 §17.9’s non-gating status in PF09. It does not introduce new tokens; any future stateless QA tokens must be defined in HDE-Governance and HDE Phased Epics.

*Epic or card:* Unknown (future stateless JSON QA epic; titles-only)

*Tokens:*  
 None yet; PF14 §17.9 explicitly forbids gating on stateless JSON QA artifacts until a future epic defines tokens. PF09 records the non-gating constraint only.

**Evidence / artifacts:**

`artifacts/proofs/success_get.txt`

`artifacts/proofs/success_head.txt`

`artifacts/proofs/success_304.txt`

`artifacts/proofs/success_writers_errors.txt`

`artifacts/ops/internal_version/headers_get.txt`

`artifacts/ops/internal_version/headers_head.txt`

`artifacts/ops/internal_version/headers_cond_if_none_match.txt`

`artifacts/ops/internal_version/headers_cond_if_modified_since.txt`

`artifacts/ops/internal_version/body_get.json`

`artifacts/ops/internal_version/body_get.sha256`

`artifacts/ops/internal_version/provenance_note.md`

`artifacts/db/ddl_fingerprint.json`

`artifacts/db/grants.txt`

`artifacts/db/check_schema.txt`

`artifacts/db/check_constraints.txt`

`artifacts/db/partition_plan.txt` (if used)

`artifacts/db/db_rw_smoke.log` (optional)

`artifacts/proofs/env_pins.txt`

`docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256`

`artifacts/evidence_index.jsonl`

**Acceptance impact**

No new tokens are introduced; this row explicitly states that there are *no* stateless JSON QA tokens yet and that none may be treated as gates.

This aligns PF09 with PF14 §17.9’s requirement that stateless QA mode is informative/non-gating until explicitly wired in Governance/Phased Epics.

**Artifacts impact**

No new artifact paths are required for this task.

References to stateless BodyGraph/compat/vendor artifacts and run bundles remain titles-only and single-homed in HDE-Schemas & Artifacts, HDE-CLI-API-Vendor-Ref, Glow QA Guide, and HDE Phased Epics.

## **Task HDE-COAG005 — Interim no-user CLI QA posture (pre-Glow prod)**

*Task ID: HDE-COAG005*

*Task name/label:* Interim no-user CLI QA posture (pre-Glow prod)  
 *Task status:* Not done

*Task description:*  
 Encode, for PF09, the pre-Glow production CLI QA constraints from Mechanics and QA canon for environments with no app-level user model, without redefining schemas or transport bytes. In this posture, Live QA behavior tests for compat and BodyGraph must be vendor-backed, and local CLI runs that do not call vendor are treated as offline math/serializer checks only.

*Task notes:*

**Environment assumptions (titles-only).**

In pre-Glow production, there is no app-level user model and no persistent user-bound BodyGraph rows configured in the database.

Mechanics and QA MUST NOT create app-like user records in production ahead of Glow App integration (see Mechanics guide §17.10 and Glow QA Guide by title).

**Compat and Reader Live QA (showcompat).**

In pre-Glow prod Live QA, hdctl showcompat MUST be exercised:

With birth arguments only (for example \--birthdate-a/--birthdate-b, \--birthtime-a/--birthtime-b, \--location-a/--location-b), and

With an explicit vendor source: Live QA behavior steps that intend to test compat behavior MUST use hdctl showcompat \--source vendor in this environment.

\--user-a/--user-b and \--source=db MUST NOT be used in production QA flows while the app user model is absent.

Any hdctl showcompat run that does not call vendor (for example showcompat without an explicit source) MUST be treated as a local/offline math or serializer check only; it may be useful for D1/D2 canonical JSON and determinism proofs under closed rails but MUST NOT be used to satisfy tokens whose intent is “live behavior with vendor rails active” or to satisfy PO Live QA steps.

QA MUST continue to verify, for birth-based compat runs that are vendor-backed:

Canonical JSON on stdout (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one trailing LF).

AB↔BA identity using swapped birth tuples (AB vs BA), reusing the CLI AB/BA parity harness (artifacts/cli/ab.json, artifacts/cli/ba.json, artifacts/cli/summary.json).

Reader v1 envelopes via \--dump-reader, with Reader↔CLI parity proven via the shared presenter/emitter, as governed by Mechanics and the CLI parity tasks in this checklist.

**Aux narratives Live QA (aux-preview).**

In pre-Glow prod, hdctl aux-preview MUST consume compat JSON produced from birth-based hdctl showcompat \--source vendor runs as described above; QA MUST NOT rely on DB-backed users to exercise Aux.

Aux preview remains a file-based consumer of compat JSON in this mode; narrative IDs and bands are exposed to admins only via governed JSON sidecars, as defined in CLI/API, Narratives Guide, and Narrative Deliverables by title.

**BodyGraph resolver and vendor ingest (bg:resolve).**

In pre-Glow prod, CLI \--user arguments passed to bg:resolve MUST be treated as ephemeral QA keys only (for example qa\_epic017\_resolve1, qa\_epic017\_vendor1) and MUST NOT be interpreted as real app user IDs.

Under rails CLOSED, any bg:resolve \--source vendor invocation MUST return a typed refusal and MUST NOT perform outbound HTTP.

Under rails OPEN in pre-Glow prod, QA MAY:

Run bg:resolve \--source vendor \--dry-run to exercise vendor shaping and ingest metadata without writing DB rows, consistent with vendor ingest policy and SAFE rails rules.

Run limited bg:resolve DB/auto stub checks that do not create real DB rows, but such runs MUST be explicitly labeled as local/offline checks and MUST NOT be used to satisfy vendor-backed behavior tokens; live BodyGraph behavior tests in this environment MUST use explicit vendor-backed modes (for example bg:resolve \--source vendor or vendor-backed resolver flows governed in Mechanics and QA canon).

bg:resolve \--source vendor \--upsert MUST NOT be invoked in production until a future epic (recorded in HDE Phased Epics and governed by Glow QA Guide) re-opens user-bound DB coverage for environments with a live app user model.

**Evidence skeleton for CLI QA (pre-Glow prod).**

For Live QA sessions in pre-Glow prod that exercise showcompat, aux-preview, or bg:resolve as vendor-backed behavior tests:

Mechanics MUST snapshot the Human Evidence Index and Machine Mirror before and after the QA run:

docs/evidence/INDEX.json

docs/evidence/INDEX.sha256

artifacts/evidence\_index.jsonl

governed \*.path\_proof.txt records

Any mutation of these governed evidence artifacts during such QA runs MUST be treated as a defect or unexpected side effect. CLI QA flows in this mode consume the evidence skeleton defined elsewhere in this checklist and in PF12/PF14; they do not write governed Evidence Index or Mirror artifacts directly.

QA notes (qa\_notes.md) for Live QA steps in this posture MUST distinguish between:

Vendor-backed behavior runs (for example “Step 2 — D1 compat vendor-backed behavior, hdctl showcompat \--source vendor \<ARGS\>”), and

Local/offline math or serializer checks (for example “local D1 canonical JSON check, no vendor”).

This labeling ensures that PF09 and PF19 can map vendor-backed behavior tokens only to the appropriate steps, and that local-only checks are not misinterpreted as vendor behavior proofs.

**Forward plan (routing only; titles-only).**

Once the Glow App and user model are integrated, a future epic recorded in HDE Phased Epics and governed by the Glow QA Guide will:

Use real app user IDs to exercise DB-backed showcompat and bg:resolve \--source vendor \--upsert in prod or stage.

Close out any acceptance tokens that currently depend on DB-backed user flows, routing to HDE-Governance and HDE Phased Epics by title.

Until that epic is live, QA requirements that assume “existing users in prod” MUST be treated as blocked by environment and satisfied instead using the no-user, vendor-first QA mode recorded in this task.

*Epic or card:* Unknown (pre-Glow QA epic; titles-only)

*Tokens (titles-only; semantics live in Governance and QA docs):*

Rails and env pins: SAFE\_RAILS\_DEFAULT\_OK, ENV\_LC\_ALL\_C\_OK, ENV\_TZ\_UTC\_OK.

Canonical JSON and parity: JSON\_CANONICAL\_CHECK\_OK, CLI\_AB\_BA\_PARITY\_OK, CLI\_TWO\_RUN\_IDENTITY\_OK, CLI\_READER\_EMITTER\_PARITY\_OK.

Evidence discipline: EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK.

*Evidence / artifacts (titles/paths only):*

For compat and Aux QA:

artifacts/cli/ab.json

artifacts/cli/ba.json

artifacts/cli/summary.json

artifacts/cli/narrative/stdout.txt (Aux preview text; titles-only)

artifacts/cli/narrative/sidecar.json (Aux preview IDs-only JSON sidecar)

Evidence skeleton (snapshots, read-only posture):

docs/evidence/INDEX.json

docs/evidence/INDEX.sha256

artifacts/evidence\_index.jsonl

governed \*.path\_proof.txt (paths and schemas single-homed in HDE-Schemas & Artifacts)

## **Task HDE-COAG006 — Admin QA surfaces (full product payload, GUI \+ CLI)**

Task ID: HDE-COAG006

Task name/label: Admin QA surfaces (full product payload, GUI and CLI)

Task status: Not done

Task description:  
 Ensure that, prior to Glow App integration, the Engine exposes a canonical admin-only full product bundle and that both a basic Admin GUI and CLI runs from arbitrary terminals can retrieve and present this bundle for a given pair, with canonical JSON evidence and Evidence Index plus Machine Mirror discipline, and with mandatory authentication and audit rails for all admin bundle surfaces.

Task notes:

Scope is admin QA only: these surfaces are for operators and the Product Owner, not end users. Reader v1 public covenant (bands-only, numeric-free) remains unchanged; app integrations continue to go through Reader and Aux contracts governed in HDE-Math-Spec, HDE-CLI-API-Vendor-Ref, HDE-Narratives Guide, HDE-Narrative Deliverables, and the Glow QA Guide by title.

The full product payload bundle for a given compat evaluation includes, at minimum:

Per-person BodyGraphs as canonical BodyGraph JSON for each party, using resolver mechanics defined in canon.

Compat result over the closed Magic-10 set, including per-category id, score, band, personal\_key, shared\_key, and compat meta as already defined in math, schemas, mechanics, and CLI references.

Three Aux narratives from the narratives system for the match: private A to B, private B to A, and shared.

Mechanics and transport for admin bundle construction and surfaces (internal admin bundle builder, CLI subcommand, HTTP route shape, and Admin GUI wiring) are single-homed in HDE-Mechanics Guide, HDE-CLI-API-Vendor-Ref, HDE-CLI and dev harness sections, and infra and QA docs by title. PF09 tracks that engine-level mechanics and evidence tasks exist, and that QA tokens for admin bundle coverage, parity, and auth rails are wired, but does not redefine schemas or transport bytes.

Addendum 12 tightens pre-Glow canon to require:

An internal admin bundle builder that composes the full product payload into a single canonical JSON object for admin use.

CLI and HTTP admin bundle surfaces that consume the same builder and produce the same bundle for the same inputs.

Authentication and authorization for both CLI and HTTP admin bundle paths, with an admin-only credential, logging and audit requirements, and rotation and revocation discipline.

New QA tokens CLI\_ADMIN\_BUNDLE\_PARITY\_OK, ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK, and ADMIN\_AUTH\_REQUIRED\_OK, which PF09 now consumes by name for this row.

---

### **Subtask HDE-COAG006.1 — CLI full product bundle (any terminal to Railway)**

Subtask name/label: CLI full product bundle (any terminal to Railway)

Subtask description:

Extend existing CLI install and entrypoint coverage so that the canonical CLI (hdctl or successor) can be installed and invoked in at least:

Codespaces images used for HDE QA, and

A clean local environment matching supported Python versions,

using the same entrypoints (pyproject console script and module runner).

Define and document a CLI runbook that, starting from a canonical pair input (fixture or births), yields the admin bundle JSON for a given pair by calling the deployed Engine on Railway production under SAFE rails appropriate for QA. This may be a single aggregator command to be pinned in CLI and mechanics docs or a composition of existing commands such as bg:resolve, showcompat, and aux-preview plus a harness script.

Ensure this CLI flow is reproducible from any terminal that has:

Network reachability to the Railway production HD Engine, and

Correct secrets and environment rails set according to Governance, CLI and infra, and QA docs by title.

Subtask status: Not done

Epic or card: Unknown (planning row; future Admin QA or packaging epic will own this work)

Tokens:

CLI\_PYPROJECT\_ENTRYPOINT\_OK

CLI\_MODULE\_RUN\_OK

CLI\_INSTALL\_OK

CLI\_HELP\_EXIT\_0\_OK

CLI\_HELP\_STDOUT\_OK

EVIDENCE\_INDEX\_UPDATED\_OK

EVIDENCE\_INDEX\_MIRROR\_OK

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence / artifacts:

CLI install logs for supported environments (pyproject entrypoint and module runner).

At least one production-against-Railway run capturing the admin bundle JSON under a governed Audit or artifacts path.

Evidence Index entry and Machine Mirror record for the CLI admin bundle artifact, with co-located path-proof transcripts.

Notes:  
 SoT: canon only at this stage. This subtask records that CLI must be able to produce the full product bundle from any terminal that can reach Railway production; details of the aggregator command or harness remain single-homed in mechanics and CLI references and will be wired back here by a future epic.

---

### **Subtask HDE-COAG006.2 — HTTP admin bundle route and GUI harness**

Subtask name/label: HTTP admin bundle route and GUI harness

Subtask description:

Implement and prove an internal HTTP admin bundle route, to be pinned in mechanics and CLI/API references, that:

Accepts a canonical pair input (fixture, births, or internal identifiers resolved via existing mechanics).

Calls the internal admin bundle builder to assemble the full product payload bundle (BodyGraphs plus compat result plus three narratives).

Emits canonical JSON (UTF-8, sorted keys, compact, exactly one trailing line feed; arrays functioning as sets are deduped and sorted) under an internal or QA-only path with admin-only operations posture (not public and not an A7 proof surface).

Wire a minimal Admin GUI to call this HTTP admin bundle route against the same production Engine on Railway that the Glow App will eventually use:

The GUI is not the Glow App and is not a public surface; it is a basic internal web page for operators and the Product Owner.

For at least one synthetic pair and one real pair, the GUI must render:

Each person’s BodyGraph diagram derived from canonical BodyGraph JSON.

Compat categories with numeric scores and bands.

The three narratives (A to B, B to A, and shared) for the match.

Ensure all JSON bundle outputs from the HTTP admin route are canonical and indexed in the Evidence Index and Machine Mirror, with governed path-proofs.

Subtask status: Not done

Epic or card: Unknown (likely future Admin-UI or admin bundle epic; ID to be assigned)

Tokens:

ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK

JSON\_CANONICAL\_CHECK\_OK

EVIDENCE\_INDEX\_UPDATED\_OK

EVIDENCE\_INDEX\_MIRROR\_OK

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence / artifacts:

HTTP admin bundle JSON artifacts for representative pairs, for example CLI path and Admin GUI path captures.

Evidence Index and Machine Mirror entries for the HTTP admin bundle artifacts, with path-proofs.

Screenshots or HTML snapshots showing the Admin GUI rendering BodyGraphs, compat scores and bands, and three narratives per match.

Notes:  
 This subtask records the requirement for an internal HTTP admin bundle route and a minimal Admin GUI harness. Route naming, detailed request and response schemas, and associated QA tokens remain single-homed in mechanics, CLI/API references, Governance, QA Guide, and Phased Epics by title; PF09 records the work and binds ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK to this slice.

---

### **Subtask HDE-COAG006.3 — CLI versus HTTP admin bundle parity**

Subtask name/label: CLI versus HTTP admin bundle parity

Subtask description:

Prove that, for identical inputs and environment, the CLI admin bundle JSON and the HTTP admin bundle JSON are byte-identical once canonicalization is applied:

For one or more representative pairs, capture the CLI-produced admin bundle and the HTTP admin bundle route output.

Run a canonical compare, using the same canonical JSON rules as elsewhere, to confirm that the two bundles match exactly with no diff after canonicalization.

Apply AB versus BA and two-run identity checks to the admin bundle surface, by title to the math and mechanics canon:

AB versus BA: swapping persons A and B yields identical normalized admin bundles.

Two-run identity: repeating the same GUI or CLI bundle call with identical inputs and environment yields identical bundle bytes with a single trailing line feed.

Subtask status: Not done

Epic or card: Unknown

Tokens:

CLI\_ADMIN\_BUNDLE\_PARITY\_OK

ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK

JSON\_CANONICAL\_CHECK\_OK

TWO\_RUN\_IDENTITY\_OK

EVIDENCE\_INDEX\_UPDATED\_OK

EVIDENCE\_INDEX\_MIRROR\_OK

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence / artifacts:

Pairs of CLI versus HTTP admin bundle JSON artifacts for at least one synthetic and one real pair.

Canonical compare logs proving parity with no differences between CLI and HTTP admin bundles.

AB versus BA and two-run identity logs for admin bundles, with math and serializer mechanics governed by other PF docs.

Notes:  
 This subtask will be considered Done only when there is concrete evidence that CLI and HTTP admin bundle surfaces are in parity under canonical JSON, that the admin bundle always contains the full bundle components covered by ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK, and that AB versus BA and two-run identity properties are enforced and proven in the same way as existing compat and Reader surfaces.

---

### **Subtask HDE-COAG006.4 — Internal admin bundle builder (composition only)**

Subtask name/label: Internal admin bundle builder (composition only)

Subtask description:

Define and implement an internal admin bundle builder as a pure function or module that composes the full product payload into a single JSON object (the admin bundle) with at least the following top-level keys:

a\_bodygraph: canonical BodyGraph JSON for person A.

b\_bodygraph: canonical BodyGraph JSON for person B.

compat: canonical compat JSON for the pair, including categories and meta as already defined in math, CLI/API, and schemas.

narratives: an array of three Aux narrative compositions for this match, including metadata and text, consistent with narrative mechanics and deliverables doc sets.

meta: build and environment metadata such as engine\_tag, release\_id, invocation\_tag or equivalent, bundle source, and any relevant rails information.

Ensure the admin bundle builder:

Uses the single canonical JSON serializer and emitter used for other governed JSON surfaces, producing UTF-8, sorted keys, compact JSON with exactly one trailing line feed.

Is internal and admin-only: it may contain numeric scores and narrative text and is not a Reader public body and not governed by the public numeric-free covenant. It is intended for admin, QA, and internal use only.

Is the common internal surface for both CLI and HTTP admin bundle routes; external admin surfaces must not reconstruct the bundle ad hoc.

Subtask status: Not done

Epic or card: Unknown (future admin bundle epic; planning row)

Tokens:

ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK

JSON\_CANONICAL\_CHECK\_OK

EVIDENCE\_INDEX\_UPDATED\_OK

EVIDENCE\_INDEX\_MIRROR\_OK

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence / artifacts:

Canonical sample admin bundle JSON artifacts for synthetic and real pairs, produced by the internal builder.

Evidence Index and Machine Mirror entries for admin bundle sample artifacts, with governed path-proofs.

Notes:  
 SoT: canon — this subtask encodes that the structure and composition of the admin bundle are now locked by spec for pre-Glow. Implementation, test harnesses, and artifact paths remain to be supplied by a future epic and will be wired back here as evidence when available.

---

### **Subtask HDE-COAG006.5 — Admin surfaces authentication, audit logging, and rotation rails**

Subtask name/label: Admin surfaces authentication, audit logging, and rotation rails

Subtask description:

Enforce authentication and authorization requirements for both CLI admin bundle paths and HTTP admin bundle routes:

Both admin surfaces must require an admin credential; an unauthenticated request must not be able to obtain the full admin bundle.

Pre-Glow minimal requirement:

A secret admin token or equivalent credential must exist with high entropy, not checked into the repository, and stored as a secret in Railway or equivalent infra.

The token must be required on every admin bundle request, for example as an Authorization header or other secure transport mechanism pinned in Governance and CLI/API docs.

The credential must be known only to admin operators and not to end users.

Provide logging and audit behavior for successful admin bundle requests:

Each successful admin bundle request must be logged with, at minimum:

Timestamp.

Who or what called it (CLI operator, GUI user, or service account).

A high-level description of inputs, such as whether the request was birth-based for two anonymous parties or user-identifier-based in a future user-model world.

A correlation identifier suitable for tracing across logs and related artifacts.

These logs must be treated as operations logs and governed by QA and Governance docs for retention, privacy, and security; no sensitive payloads or secrets may be logged.

Ensure token rotation and revocation behavior:

The admin credential must be rotatable without code changes, for example via environment configuration or Infra secrets.

Revocation must be effective: removing or changing the secret must cause old tokens to stop working immediately.

Any change to the admin credential set must be treated as a governed change and, where appropriate, recorded with evidence and Doc-Delta notes in the owning PF docs.

Subtask status: Not done

Epic or card: Unknown

Tokens:

ADMIN\_AUTH\_REQUIRED\_OK

EVIDENCE\_INDEX\_UPDATED\_OK

EVIDENCE\_INDEX\_MIRROR\_OK

EVIDENCE\_PATHS\_VALIDATED\_OK

Evidence / artifacts:

Admin auth harness logs showing that unauthenticated admin bundle requests are rejected and authenticated requests succeed, for both CLI and HTTP admin bundle surfaces.

Operations log samples demonstrating required fields (timestamp, caller, high-level input description, correlation identifier) without payload bodies or secrets.

Evidence Index and Machine Mirror entries for admin auth and audit artifacts, with governed path-proofs, when those artifacts are captured.

Notes:  
 This subtask binds ADMIN\_AUTH\_REQUIRED\_OK to a concrete set of expectations for admin bundle surfaces. Authentication and authorization semantics, header formats, and storage details remain single-homed in Governance, infra, and QA docs by title; PF09 records that there is explicit checklisted work and evidence for these rails and that admin surfaces are no longer permitted to remain open or unauthenticated under canon.

