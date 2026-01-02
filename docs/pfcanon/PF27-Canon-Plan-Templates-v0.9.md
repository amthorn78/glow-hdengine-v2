# Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v0.9

**Status:** Canon

**Effective date:** 2026-01-01

**Last Update Gate:** BN 8.7.7 Drain A50-51

**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **Purpose & scope \[Required−Now\]**

**Purpose.**  
PF27 is the single PF home for **plan and runbook templates** used in the Glow project (including the HDE workstream). It exists to standardize **template shape**, required front matter, evidence posture, and review guards so that plan documents are executable in the PO \+ Codespaces loop and remain canon-aligned.

**Scope (in).**

**PF23 consult (required for planning).**

* When planning remediation, development, or QA execution, the guide author MUST consult **PF23 — Reality Audits** as a primary input for component boundaries and canonical pathnames/loci.  
* Guides SHOULD include a short “PF23 Anchors” subsection listing the component(s) consulted and the key pathnames/loci the plan will touch (traceability only; do not duplicate PF23).

**Portability vs provenance (normative).**

* A remediation guide MAY include a short “Evidence inventory reviewed (non-PF)” list for provenance, but it MUST NOT require the executor to open external files to execute the plan.  
* If any non-PF fact is required to execute downstream steps (status lines, headers, error strings, observed file paths, command outputs), the guide MUST embed that fact directly in the document inside “Observed Evidence Snapshot” as a short quote or precise paraphrase.  
* Any Artifact Map (or equivalent) MUST explicitly label non-PF inputs as: `provenance only; not required to execute`. If not labeled, it is treated as an execution dependency and is a portability blocker.  
* If a non-PF observation drives a branching decision, the guide MUST include: the observation to look for (exact string/status/shape), the decision rule, and the output artifact path where the observation is captured (lowercase file path including filename).  
* Normative templates for operational plans/runbooks that must be **step-executable** and produce **governed evidence** (example: Live QA Plans).  
* Required template elements, including:  
  * plan front matter fields (names-only for operators and inputs),  
  * canon precedence statements,  
  * rails and determinism pins declarations (when capturing governed bytes),  
  * evidence root normalization and per-run `QA_ROOT`,  
  * runbook check matrices and per-step blocks with explicit PASS/FAIL predicates.

**Scope (out).**

* The content of any specific plan instance (epic-specific steps, commands, expected outputs), except that templates may require where and how those details are written.  
* Token registry and token semantics (owned by **PF04 — HDE-Governance**).  
* Transport and wire-byte contracts (owned by **PF05 — HDE-CLI-API-Vendor-Ref**).  
* Epic records and epic planning (owned by **PF20 — HDE-Phased Epics**).  
* Schema definitions and governed artifact schemas (owned by **PF12 — HDE-Schemas and Artifacts**).  
* Living deltas and temporary supersedes notes (owned by **PF10 — HDE-Build Notes**).

**Canon precedence for template use.**

* Templates and derived plan documents MUST include the canon precedence rule:  
  “PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”  
* PF27 MUST NOT duplicate bytes, token lists, or schemas. It routes by title to the single-home PF documents.

**Primary audience.**

* Plan authors: PO, QA agent, implementation agents writing executable plans/runbooks.  
* Plan reviewers: QA reviewers validating executability, canon alignment, and explicit blockers.

# A) HDE Templates

## 1\) HDE-Live-QA-Plan

Applies to all epics.

**Canon anchors for template shape (non-exhaustive):**

PF19 — Glow QA Guide, §3.4; PF19 — Glow QA Guide, §4.4; PF19 — Glow QA Guide, §14.4; PF19 — Glow QA Guide, §14.6; PF06 — Epic Process Guide, §0.4.1; PF04 — HDE-Governance, §2.0; PF10 — HDE-Build Notes (cite by addendum number \+ title).

---

### Front matter

* **Epic ID:** `HDE-EPIC###`

* **Plan type:** `Live QA Plan / Runbook`

* **Execution venue:** `Codespaces` (or `Other: ____`)

* **Target environment:** `prod` / `dev` (explicit)

* **Plan revision:** `r#`

* **Date:** `YYYY-MM-DD`

* **Operators (names-only):** `PO`, `QA agent`, (optional) `Codex`

**Canon precedence statement (must include):**

* “PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.” (PF10 — HDE-Build Notes, §0)

---

### Scope statement

#### Epic intent and QA boundaries (names-only, PF-anchored)

* **Epic record anchor(s):** `<PF20 reference(s)>` (PF20 — HDE-Phased Epics, §2.1)

* **In-scope D-goals / surfaces (names-only):**

  * `D0 …`

  * `D1 …`

  * `D2 …`

  * `D3 …`

  * (add/remove as needed; the steps section is variable-length)

#### PF10 overrides / conflicts (if any)

* List each PF10 override as:  
   `PF10 item → what it changes → impacted PF references` (PF10 — HDE-Build Notes, §3)

#### PF23 Anchors (planning trace)

**PF23 consult (required).**  
 When planning for QA, remediation, development, or any other execution work, the plan author MUST consult **PF23 — Reality Audits** as a primary input for:

* component boundaries (what the “thing” is), and

* canonical pathnames / loci (where it lives).

**PF23 Anchors subsection (recommended).**  
 Plans SHOULD include a short “PF23 Anchors” subsection that lists:

* the component(s) consulted from PF23, and

* the key pathnames/loci pulled from PF23 that this plan will touch.

This is a traceability anchor only. It MUST NOT duplicate PF23 contents. If PF23 appears stale or missing required coverage, note it as an observation only (do not assign PF23 updates as agent work).

---

### Environment and rails posture

#### Determinism pins (when capturing governed bytes)

* `LC_ALL=C`

* `LANG=C`

* `TZ=UTC`  
   (PF19 — Glow QA Guide, §14.4.1)

**Rule (normative): canonical pins only.**

* Any Live QA step that produces governed bytes/evidence MUST use only the determinism pins already defined in canon (locale \+ timezone pins; rails as applicable).

* `PYTHONHASHSEED` MUST NOT be added as a required rail/pin for Live QA plan approval or execution.

* If a QA step (or repo tool) produces nondeterministic output due to hash-order dependence, the step MUST normalize ordering explicitly (sort keys; sort lists; avoid set iteration without ordering) rather than relying on `PYTHONHASHSEED`.

* If the nondeterminism exists in repo-provided tools, treat it as an implementation defect to drain via the normal canon paths (not by adding QA-only rails).

* A plan MAY temporarily set `PYTHONHASHSEED` only as an explicitly labeled diagnostic control, and it MUST NOT be interpreted as satisfying or extending the canonical env pins evidence surface.

#### Rails posture

* **Default rails** for this runbook: `SAFE_MODE=__`, `ALLOW_NETWORK=__`, `APP_ENV=__`

* **Where rails change (if anywhere):** list step IDs and why  
   (PF19 — Glow QA Guide, §2.3; PF19 — Glow QA Guide, §3.4)

#### Gitless Live QA (non-negotiable)

* Runbook steps MUST NOT include git gating or “working tree clean” as PASS/FAIL. (PF19 — Glow QA Guide, §3.4)

---

### PO inputs needed (explicit; placeholders are blockers if not listed)

List **all required external inputs** (names-only; never store secret values in snapshots):

* `HDE_BASE_URL` (if needed)

* `HDE_PROD_BASE_URL` (if needed)

* `AUTH_HEADER_NAME` / `AUTH_HEADER_VALUE` (only if required in your environment; do not persist values)

* Any other required URLs/ports/paths required for steps to execute

If a step depends on an input and the input is not available, the step must be marked **TOOLING\_BLOCKED / FAIL\_TOOLING**, not guessed. (PF19 — Glow QA Guide, §4.4; PF19 — Glow QA Guide, §14.6)

---

### Evidence posture and required directory structure

#### QA root normalization (required)

* Epic QA root MUST be lower-case: `audit/qa/hde-epic<NNN>/` (PF19 — Glow QA Guide, §3.4)

  #### **QA\_ROOT for this run (required)**

Define a per-run root (example pattern; you choose the exact substructure, but it must be stable and under the epic QA root):

* `QA_ROOT=audit/qa/hde-epic<NNN>/<run-id>/`

   **Step logs \+ manifest (required)**

* Each step MUST produce **one primary evidence file** under `audit/qa/<epic-id>/…` (PF19 — Glow QA Guide, §3.4)

* Each step MUST have a **Deliverables** subsection naming the minimal evidence set for that step (PF19 — Glow QA Guide, §3.4)

* Maintain `audit/qa/<epic-id>/qa_step_logs_manifest.json` (PF19 — Glow QA Guide, §4.4)

**Manifest idempotency and uniqueness (normative).**

* `qa_step_logs_manifest.json` MUST have at most one entry per `(run_id, step_id)` (equivalently, `(run_id, check_id)`).  
* If a step is re-run within the same `run_id`, update the existing manifest entry in place (overwrite) rather than appending a second entry for the same `(run_id, step_id)`.  
* If the operator needs to preserve a full history of step attempts without overwriting, allocate a new `run_id` (new `QA_ROOT`) and treat it as a separate run.  
* After writing/updating the manifest, validate uniqueness: no duplicate `(run_id, step_id)` pairs. If duplicates exist, treat this as **FAIL\_TOOLING** and do not proceed to any close-pack generation until the manifest is corrected.  
* Evidence filenames and paths (canonical vs alias):  
  * Plans MUST name canonical evidence paths/filenames where canon defines them.  
  * If compatibility aliases are required (legacy acceptance bindings), the plan MAY emit explicitly enumerated alias copies only. Alias copies MUST be mechanically derived from the canonical bytes. Evidence indexing MUST bind to the canonical paths; aliases are compatibility-only.  
* Release identity / Freeze-Pack Manifest semantics (when the plan touches release identity):  
  * **Single SoT:** Freeze-Pack Manifest SoT is `catalog/manifest.json`. No other file may act as SoT for Freeze-Pack membership or release identity.

  * **Manifest schema is closed:** `catalog/manifest.json` MUST contain exactly: `root`, `version`, `built_at_utc`, `files` (and no other keys). The manifest MUST NOT list itself in `files`.  
  * **Canonical bytes:** Identity and verification MUST operate on canonical bytes (canonical JSON rules; single trailing LF). Equality checks MUST be byte-equality on canonical bytes (not “JSON-equivalent”).  
  * **release\_id is fixed:** `release_id = sha256(canonical_bytes(catalog/manifest.json))`, encoded as lowercase 64-hex.  
  * **Canonical evidence paths (when applicable):**  
     `artifacts/math/release_id.txt`  
     `artifacts/math/release_id_recompute.log`  
     `artifacts/math/freeze_pack_manifest.json`  
  * **Evidence-copy meaning is unambiguous:** `artifacts/math/freeze_pack_manifest.json` MUST be a byte-identical copy of the canonical on-disk `catalog/manifest.json`. It MUST NOT be a derived schema, subset manifest, or alternate contract.  
  * **No dual semantics:** Do not create alternate “manifest-like” artifacts that reuse the Freeze-Pack evidence-copy path. Any alternate manifest-like summaries MUST be quarantined under a different name/path and MUST NOT be used as identity inputs.  
  * `manifest_snapshot.json` (and similar summaries) are evidence only and MUST NOT be used as identity inputs or substituted for the Freeze-Pack Manifest.  
* Repo reality tolerance (execution detail):

  * If a referenced path/filename/command conflicts with repo reality, execute using repo-real invocation/paths and capture evidence under `audit/qa/...`.  
  * Record the mismatch as a CAVEAT: `DOC_DRIFT` in Doc Delta Capture (Step-0B), unless it blocks execution or pass/fail judgment.

---

### Mandatory Step‑0 steps (Codespaces Live QA)

If the run is executed in Codespaces, Step‑0 requirements are mandatory. (PF19 — Glow QA Guide, §14.4; PF19 — Glow QA Guide, §14.6)

#### Step-0A — Codespaces snapshot (mechanical)

* Output path under: `audit/qa/<epic-id>/…`  
   (PF19 — Glow QA Guide, §14.4.3)

* Step-0A MUST NOT be “manifest-only.” The plan MUST declare the concrete file outputs for Step-0A (paths under `QA_ROOT`) so later review can retrieve the snapshot itself, not only a manifest reference.

* Required Step-0A outputs (names-only here; make paths concrete in the plan):

  * Step-0A step log file under `QA_ROOT/step_logs/...`

  * Codespaces snapshot artifact under `QA_ROOT/snapshots/...` (secret-free; secrets are presence-only)

  * one `qa_step_logs_manifest.json` entry that points to the Step-0A step log path

#### Step‑0B — Doc Delta Capture (mechanical)

Must mechanically produce a Doc Delta Capture artifact that:

* lists missing/ambiguous prerequisites \+ intended PF fix location \+ resolution status,  
* separates findings into **BLOCKERS** and **CAVEATS** (stable IDs: `BLK-01`, `CAV-01`),  
* outputs “no deltas” if both lists are empty.

Blocker definition (plan approval): an issue that prevents executing the plan or prevents a confident pass/fail judgment for the in-scope behavior.

Caveats are tracked but do not block approval/execution unless they become blockers (examples: `UNREGISTERED_TOKEN`, `DOC_DRIFT`). (PF19 — Glow QA Guide, §14.6)

#### **Step-0C — Prod handshake (identity-only) if plan claims “Codespaces → prod”**

* If the plan depends on prod-facing behavior, include a preflight/identity handshake step and treat ambiguity as **TOOLING\_BLOCKED**, not PO-supplied guessing. (PF19 — Glow QA Guide, §3.5)

* If the handshake step uses `/internal/version` (or the plan claims any `/internal/version`\-based evidence):

  * **Interim posture (normative; until the auth epic lands):** `/internal/version` is treated as **operator-network-only**. Until token auth exists, all runbooks MUST treat any auth header as **optional (never required)**.

  * **Non-invention rule (auth posture):** Do not state `/internal/version` auth posture (public vs gated vs auth-header required) as canon. Any auth posture statement MUST be explicitly labeled **Observed Evidence (non-PF)** until canonized by implementation \+ canon drain.

  * **Deterministic probe input (allowed; does not imply auth posture):**  
     A probe harness MAY accept an auth header input to keep execution deterministic. This MUST be treated as an execution input only and MUST NOT be interpreted as proof that auth is required for `/internal/version`.

  * **Evidence capture (auth posture; secret-free):**

    * Always capture: status line \+ headers for a request with **no auth header**.

    * If an auth header is available (value redacted or presence-only noted), MAY capture a second request with the auth header present. Absence of an auth header MUST NOT be treated as a plan blocker under the interim posture.

  * **Proof-surface invariant checklist (required if this step is used as /internal/version identity proof):**  
     If this step produces governed `/internal/version` evidence or claims any `*_OK` acceptance tokens about `/internal/version`, it MUST explicitly enumerate and verify (at minimum):

     A. Transport

    * GET returns 200

    * HEAD returns 200 (parity expectations are met)

    * conditional requests (If-None-Match / If-Modified-Since) do not yield 304; they return 200

  * B. Headers

    * `Cache-Control: no-store` present

    * `Content-Type: application/json; charset=utf-8` present

    * `ETag` absent

    * `Last-Modified` absent

  * C. Body (identity payload)

    * body is canonical-bytes JSON and LF-terminated

    * body is fixed-schema JSON with exactly these keys (no extras):  
       `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`

  * **Token-claim gating (no “false OK”):** a step MUST NOT claim any `*_OK` token unless the corresponding invariant has been verified against the same captured bytes/headers for that run. If the run is FAIL\_TOOLING / TOOLING\_BLOCKED, the step MUST NOT claim `*_OK` tokens for checks that did not pass.

  * **Coupling requirement:** the captured headers, captured body, and any token claims MUST refer to the same resolved target/response chain. If coupling cannot be established, the step MUST be treated as FAIL\_TOOLING and MUST NOT claim `*_OK` tokens.

  * **Capture hygiene note:** header evidence SHOULD be captured as “status line \+ header lines.” Curl diagnostics/warnings SHOULD be captured to a separate stderr artifact. If warning lines appear in a headers file, the validator MUST ignore non-header lines for parsing and record a CAVEAT unless it blocks verification.

  * Evidence MUST be stored in-repo under a lowercase audit path (for example under `QA_ROOT/snapshots/internal_version/…`) and MUST NOT include secrets.

---

### Acceptance tokens roster and validation (names-only)

#### Token roster source

* Token handling is optional in Live QA plans by default (token load reduction). A plan MUST be executable and reviewable without a full token roster.

* If the plan includes any token list, it MUST be sourced from the epic acceptance roster (names-only). Partial lists are allowed and MUST NOT be treated as a plan-approval blocker.

  #### Token single source of truth rule

* Token names/semantics live in PF04 and must match exactly; no token invention, aliases, or near-matches. (PF04 — HDE-Governance, §2.0)

* PF19 may contain QA operational token guidance, but it MUST reference PF04 token names exactly and MUST NOT introduce new acceptance token names.

* /internal/version conditional semantics token name discipline (no aliases):

  * The canonical token name is: `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`.

  * Any alternate name intended to mean “conditionals return 200 and never 304” (example: `INTERNAL_VERSION_COND_200_NO_304_OK`) is non-canon and MUST NOT appear in plans, matrices, acceptance maps, or token→evidence bindings.

#### Preflight token validation requirement

* Token spelling/registry drift is a CAVEAT by default: record `UNREGISTERED_TOKEN` in Doc Delta Capture (Step-0B). Do not substitute token names. Do not claim unregistered tokens as satisfied for acceptance.

* Treat token correctness as a BLOCKER only when token correctness is required to interpret pass/fail for a specific check, or when a token is being claimed as satisfied for acceptance.

---

### Runbook Check Matrix (required)

This is the “index” of the runbook. **Every row MUST have a corresponding Step Block in §8**.

| step\_id | check\_name | surface / D-goal mapping | rails posture | PO command(s) | expected result (pass/fail predicates) | primary evidence path (QA\_ROOT) | deliverables (minimal set) | tokens claimed (optional; names-only) | PF anchors |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

**Matrix rules**

* Commands must be copy/paste-ready. (PF19 — Glow QA Guide, §3.4)

* Expected results must be explicit and mechanically checkable. (PF19 — Glow QA Guide, §3.4)

* Tokens are optional in the matrix. If used, token names must be PF04-valid and exact. Unregistered tokens are recorded as CAVEAT `UNREGISTERED_TOKEN` (Step-0B) and MUST NOT be substituted or claimed as satisfied. (PF04 — HDE-Governance, §2.0)

---

### Runbook Steps (variable length; repeat one block per matrix row)

This section is the **actual QA steps**. The number of steps is flexible: include **as many Step Blocks as there are checks**.

**Rule:** Every Step Block MUST include:

* one primary baseline command OR a canon-named entrypoint OR an inline tool (see Step Block Template) (PF19 — Glow QA Guide, §3.4)

* one primary artifact (PF19 — Glow QA Guide, §3.4)

* Deliverables list with fully-qualified paths and minimal evidence set (PF19 — Glow QA Guide, §3.4)

* step log status that distinguishes tooling vs behavior (PF19 — Glow QA Guide, §4.4)  
---

  ## **Step Block Template (copy/paste per step)**

STEP \<step\_id\>: \<check\_name\>  
Surface / D-goal mapping: \<D\# \+ surface\>

Rails: SAFE\_MODE=**, ALLOW\_NETWORK=**, APP\_ENV=\_\_, pins: LC\_ALL=C, LANG=C, TZ=UTC (if applicable)  
Do not add non-canonical pins (example: PYTHONHASHSEED). See §1.2.1.

PF anchors: \<PFxx — Title, §X.Y\> (list all that govern this step)

PO command(s) (copy/paste)  
\<command block(s) go here\>

Command/tooling discipline (normative)

* Interactive-shell safety (normative).  
  Copy/paste command blocks MUST NOT include terminal-closing commands or control flow (for example exit) when the intended execution venue is an interactive shell.  
* If strict “exit-on-fail” semantics are required for an enforcement check, run the enforcement in a subshell and capture its output/rc as evidence, without terminating the operator shell.  
* Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is explicitly named by path in PF canon.  
* If a step needs tooling, it MUST be either:  
  * a canon-named entrypoint by explicit path, or  
  * an inline tool whose full source is embedded in the plan step and written into the run-local QA tools directory QA\_ROOT/tools/ (no hidden dependencies).  
* “Baseline commands” means: explicit shell/Python one-liners, direct invocation of canon tools, tee for logs, explicit file writes, with no reliance on opaque runners.  
* When canon is silent on an entrypoint but requires an artifact surface, implement the artifact generation directly rather than inventing a new repo script path.

Optional: set env vars (names-only shown in plan; values supplied by PO at runtime)  
export HDE\_BASE\_URL="..."

Run the step command(s)

Expected result (PASS/FAIL predicates)

PASS if:

* \<explicit predicate 1\> (e.g., exit code \== 0, status==200, header contains…, file contains…, sha matches…)  
* \<explicit predicate 2\>

FAIL\_BEHAVIOR if:

FAIL\_TOOLING / TOOLING\_BLOCKED if:

* \<missing input / missing binary / unreachable service / missing prereq\>  
* (example: empty headers capture)  
  ---

/internal/version invariant checklist (required when the step produces /internal/version governed evidence)

If this step captures /internal/version evidence or claims any \*\_OK tokens about /internal/version, the Expected result MUST explicitly enumerate and verify (at minimum):

A. Transport

* GET returns 200  
* HEAD returns 200 (parity expectations are met)  
* conditional requests (If-None-Match / If-Modified-Since) do not yield 304; they return 200  
  (If a token name is used for this claim, it MUST be INTERNAL\_VERSION\_CONDITIONALS\_IGNORED\_OK.)

B. Headers

* Cache-Control: no-store present  
* Content-Type: application/json; charset=utf-8 present  
* ETag absent  
* Last-Modified absent

Header-capture hygiene (required for reliable parsing)

* Headers evidence files SHOULD contain only:  
  * the HTTP status line, and  
  * Key: Value header lines.  
* Curl diagnostics/warnings SHOULD be captured to a separate stderr artifact.  
* If a warning line appears in a headers file (example: curl: (18) ...), validators MUST ignore non-header lines for header parsing and record a CAVEAT unless it blocks verification.

C. Body (identity payload)

* body is canonical-bytes JSON and LF-terminated  
* body contains exactly these keys, and in fixed order, with no extras:  
  engine\_tag, build\_commit, invocation\_tag, invocation\_sha256, emitter\_sha256, release\_id  
* If the step claims two-run identity, it MUST perform two GETs and prove byte-identical body bytes (and matching sha256 for the captured body bytes).  
* If the step claims coupling to local release identity, it MUST verify release\_id equals artifacts/math/release\_id.txt (or the plan’s declared release\_id evidence path).

Token gating and coupling (normative)

* Do not claim any \*\_OK token unless the invariant is verified against the same captured bytes/headers written as evidence for that run.  
* If the step is FAIL\_TOOLING / TOOLING\_BLOCKED, do not claim \*\_OK tokens for checks that did not pass.  
* Captured headers, captured body, and any token claims MUST refer to the same resolved target/response chain. If coupling cannot be established, treat as FAIL\_TOOLING.  
  ---

Primary evidence artifact (required)

QA\_ROOT//\<primary\_artifact\_name\>.  
One line on what it contains.

Deliverables (minimal evidence set; fully-qualified paths)

List only what is needed to judge this step (no “everything in this folder”):

* —  
* —

(If no new files) No new files; inspects \<existing path(s)\> only. (PF19 — Glow QA Guide, §3.4)

(Optional helper artifacts) .sha256 — sha256 sidecar for (optional unless explicitly required by the epic acceptance roster).

Tokens claimed (optional; names-only)

* (Optional) \<TOKEN\_1\>  
* (Optional) \<TOKEN\_2\>

(If listed, token names must be PF04-valid and exact. Do not claim unregistered tokens; record UNREGISTERED\_TOKEN as a CAVEAT in Step-0B instead.)

Token-claim semantics (normative)

* Tokens listed in step logs and closeout artifacts are claims, not rosters.  
* On PASS, it is allowed to claim \*\_OK tokens that were actually verified by this step.  
* On FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, or PARKED, the step MUST NOT claim any \*\_OK tokens.  
* If the runbook needs to record “intended tokens” for planning or review, record them as non-token workflow metadata (example field name: intended\_tokens) and keep Tokens claimed empty unless the step status is PASS.  
  ---

Step log record (required)

Step log path: QA\_ROOT/step\_logs/\<step\_id\>\_\<check\_name\>\_r.log

* Must be unique per execution attempt.  
* If a step is re-run within the same run\_id, write a new step log file (increment r), and update qa\_step\_logs\_manifest.json idempotently for this (run\_id, step\_id) (overwrite; no duplicates).  
* If the operator needs to preserve full history without overwriting manifest entries, allocate a new run\_id (new QA\_ROOT) instead of duplicating manifest rows.

Status: PASS | FAIL\_BEHAVIOR | FAIL\_TOOLING | TOOLING\_BLOCKED | PARKED (PF19 — Glow QA Guide, §4.4)

Notes on step ordering (optional, but allowed)

* Step ordering must match dependencies: Step-0 → preflights → behavior checks → indexing/close steps.  
* Any step that depends on unresolved prerequisites must be marked TOOLING\_BLOCKED and routed to Doc Delta Capture (Step-0B). (PF19 — Glow QA Guide, §14.6)

---

### Evidence indexing and same-change-set parity (include when the epic requires it)

If this epic requires evidence index / mirror / manifest updates, include explicit steps (as Step Blocks in §8) that:

* update the governed evidence surfaces (by the epic’s acceptance requirements),

* maintain parity between the human evidence index and machine mirror when both are required, in the same change-set.  
   (PF12 — HDE-Schemas and Artifacts, §8.6; PF04 — HDE-Governance, §9.5)

---

### **Close-out artifacts (required for Live QA epics)**

Include explicit **close-out steps** (as Step Blocks in §8) that mechanically produce:

* **D0 Discovery artifact** (PF06 — Epic Process Guide, §0.4.1)

* **QA RCA & Doc Delta summary** (PF06 — Epic Process Guide, §0.4.1)

* **Close report \+ manifest** (PF19 — Glow QA Guide, §3.4)

**Close-pack sequencing (normative).**

* If any remediation run changes a step from `FAIL_*` to `PASS`, the close-pack generation MUST be re-run against the updated `qa_step_logs_manifest.json` so the close report reflects the closure-consistent state.

* Close-pack generation MUST NOT proceed if the step logs manifest violates the uniqueness rule (duplicate `(run_id, step_id)` entries). Treat that condition as **FAIL\_TOOLING** until corrected.

**Close-pack summary semantics (required when a close-out step emits a “failing steps” summary).**

* The close-out summary MUST state whether “failing steps” is:

  * **historical** (any failure recorded in an append-only manifest), or

  * **current-state** (latest status per check\_id / step\_id).

* If historical, it MUST be labeled explicitly as historical so it is not misread as “currently failing.”

---

### Review truncation / source-retrieval guard

**No excerpt-based claims (hard).**

* Do not claim “token missing/mismatched” unless the reviewer has retrieved the full epic acceptance roster passage and the relevant token registry entries for the tokens in question.

* Do not claim a rails/bytes/evidence-rule violation unless the reviewer has retrieved the full governing passage for that specific claim.

**Structural completeness checks (hard; plan review blockers when violated).**

* Runbook check matrix completeness: every matrix row MUST have a corresponding Step Block, and every Step Block MUST have a matching matrix row. Missing-orphan steps are BLOCKERS.

* Step-0A is not “manifest-only”: the plan MUST declare concrete Step-0A outputs (step log \+ snapshot artifact paths under `QA_ROOT`). If Step-0A outputs are not declared, treat as a BLOCKER.

* If the plan lists a step ID (example: “Z1”) without an executable definition (Step Block) and pass/fail predicates, treat as a BLOCKER. (A matrix row alone is not a definition.)

**Review outputs MUST separate findings into:**

* **BLOCKERS** (must fix before execution/approval), and

* **CAVEATS** (tracked; do not block unless they prevent execution or prevent a confident pass/fail judgment).

**Approval rule:**

* If any BLOCKERS exist → plan is rejected for revision.

* If no BLOCKERS exist → plan is approved even if CAVEATS exist.

**Repo reality execution tolerance:**

* When proceeding on repo-real paths/commands, record `DOC_DRIFT` as a CAVEAT and continue unless it blocks execution or confident verification.

## 2\) HDE-EPIC-Plan

Each epic tracked in PF20 **MUST** have exactly one “Epic record”.

* The **phase** is chosen from PF21’s 7 phases (titles-only).  
* Each epic record is **append‑only**; corrections happen via new PF20 changes, not by rewriting history silently.  
* JIRA/JSON boards **mirror** this mapping but do not replace it.

### **Epic Record Template (Normative)**

For every epic, fill out the following fields as the **canonical PF20 record**.

#### **Meta**

* **Epic ID:** `HDE-EPICXXX`  
* **Epic name (short):**  
* **Alchemical phase:** (exact phase name per PF21, e.g. `Calcination`, `Dissolution`, …)  
* **Phase rationale (1–3 sentences):** Why this epic belongs in this phase.  
* **Related boards:** (JIRA epic key(s), JSON board lane/card IDs if needed)  
* **Status:** `Planned | In Progress | Blocked | Pending Review | Done | Won’t Do | Superseded`  
* **Date started:** `YYYY‑MM‑DD`  
* **Date completed:** `YYYY‑MM‑DD` (or `TBD`)

#### **Existing Work Check (MUST)**

Before any new implementation work is planned or started for this epic:

* **Existing features review (summary):**  
  * What features, flows, or components already cover part of this intent?  
  * What prior epics or PF10 build notes are relevant (titles/IDs only)?  
* **Existing tokens validated:**  
  * List **acceptance tokens** already satisfied that this epic will **reuse**, not re‑prove (names-only, e.g. `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`).  
* **Existing evidence located:**  
  * Pointers by title to relevant artifacts and index/mirror records (e.g. “Machine mirror record for `artifact_key=reader_a7_headers`”).  
* **Gap statement:**  
  * Short bullet list of what **remains unproven** or **drifts** that this epic is explicitly meant to address.

**Rule (normative):**

No new work is scoped for this epic until the Existing Work Check is filled in and reviewed. This applies to **features, tokens, and evidence**. If this section is blank or obviously stale, the epic is **not ready** to enter “In Progress”.

#### **Deliverables (Jobs To Be Done)**

**Ops task note (when applicable):**

If any deliverable includes **Ops tasks** (human console/config actions or other privileged external-system changes):

* The Epic Record MUST separate OPS tasks from DEV/PR work and MUST label OPS tasks as **PO-only execution, IA-guided** (not Codex PR work).

* Each OPS task MUST be specified using the required Ops Task record fields defined in PF27 §1.12, including: Task ID, intent, constraints/rails, success criteria, evidence to capture (repo path), rollback intent, and secret handling note.

* Ops-task completion MUST be proven by secret-free, repo-stored evidence under a lowercase `audit/ops/<epic-id>/...` path (or `audit/qa/<epic-id>/...` when part of QA execution).

* Any Ops task included in the epic MUST also be represented as a tracked subtask in **HDE Build Checklist** (titles-only), using the same Task ID and fields.

List **concrete, observable deliverables**; each should be testable:

* **Deliverable D1:**  
  * *Job to be done:*  
  * *Evidence required:* (artifact titles, mirror records, snapshots; titles-only)  
  * *PF references:* (PF titles \+ sections, e.g. “PF14 — HDE Mechanics Guide §1.3 Evidence & CI coupling”)

Repeat D2, D3, … as needed.

These deliverables should map cleanly to PF06 PR plans, PF09 CI jobs, and PF19 QA playbooks (titles-only).

**QA deliverable note (when applicable):**

If a deliverable’s scope includes Live QA, QA tooling bootstrap, QA harness discipline, acceptance-map viability, or other QA\_ROOT evidence production:

* The deliverable’s “Evidence required” list SHOULD name the **intended QA outcomes** (names-only) and the **expected evidence families** (titles-only), and MUST route the detailed runbook/commands/step sequence to “Glow QA Guide” and “Epic Process Guide” (titles-only).  
* Any artifact treated as Live QA evidence MUST be produced mechanically by commands (shell/scripts/tools). Manual editor fill is prohibited for QA evidence files. Placeholder fields such as “(fill PASS/FAIL)” are non-conforming in approved QA plans and templates.  
* PF20 MUST NOT embed a Live QA runbook (commands, step-by-step checks, QA\_ROOT directory design, README generator rules, or per-step artifact layouts). Those are authored as QA work products during Close Gate execution.  
* When a deliverable claims a “local bundle” directory (for example `artifacts/ops/internal_version/*`), its “Evidence required” list MUST be a complete inventory of required evidence paths (titles-only), and MUST explicitly list any shared/global evidence dependencies that live **outside** the local bundle directory (for example determinism env pins logs), rather than assuming they are implicit.

  #### **PF Reference Map**

Summarize **which PF docs and sections this epic leans on** (no duplicated bytes):

* **Core:**  
  * PF21 — 7 Phases of Alchemical Engineering (§phase used)  
  * PF06 — Epic Process Guide (§0.4 Execution posture and flow; §2.x as applicable)  
  * PF09 — HDE Build Checklist (pre/post‑commit CI gates; titles-only)  
  * PF19 — Glow QA Guide (§2 Pre‑commit QA; §5 Component playbooks; §11 Roles)  
* **Additional (as needed):**  
  * PF01 — HDE Math Spec  
  * PF02 — HDE Architecture  
  * PF04 — HDE Governance  
  * PF05 — HDE CLI‑API‑Vendor Ref  
  * PF12 — HDE Schemas & Artifacts  
  * PF14 — HDE Mechanics Guide  
  * PF17 — HDE Narratives Guide

Only **list titles and sections** here; do not restate content.

#### Tokens and Evidence (Acceptance)

This section is the **names-only acceptance roster** plus **titles-only pointers** to where evidence is recorded. Semantics live in the owning PF documents, not here.

##### A. Acceptance tokens

###### *A1. Baseline tokens (required for epic close)*

* `TESTS_PASS_OK`

* `DOC_DELTA_PRESENT_OK`

* `EVIDENCE_INDEX_UPDATED_OK`

* `MACHINE_MIRROR_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK` (when applicable; see PF09/PF12)

###### *A2. QA rail tokens (final PR, both pre- and post-commit)*

* `QA_PRECOMMIT_CHECKLIST_OK` (PF19)

* `QA_POSTCOMMIT_CHECKLIST_OK` (PF19)

* `ENV_RAILS_POLICY_OK` (PF04; closed refusal / open conformance)

###### *A3. Phase-specific tokens (epic-defined, names-only)*

List any additional acceptance tokens required by this epic’s design (names-only). Examples by phase:

* Calcination: tokens that prove audit and kill-list of drift/debt

* Distillation: tokens that prove refactors and repeatability

* Coagulation: tokens that prove solidified, release-grade posture

**Note:** Actual semantics live in PF04/PF09/PF12/PF19, not here.

**Token introduction discipline (planning rule):**

* Epic Plans MUST NOT introduce new acceptance tokens as a convenience for describing behavior. If PF05/PF09 already specify a behavioral constraint (example: stream discipline), represent it as a non-token requirement under the relevant deliverable and prove it via tests/evidence, unless governance explicitly requires a token.

* Unregistered token names are mechanical blockers. If a new token is genuinely required, it MUST be routed via ADR \+ conflict check \+ Governance Doc-Delta before it can appear as a required acceptance token in §2.1.5, acceptance maps, or token→evidence matrices.

##### B. Non-token workflow metadata (do not model as acceptance tokens)

These facts may be recorded as metadata, but they are **not** acceptance tokens:

* PR existence/opened state, PR URL, branch name, review status, CI job links

* PR workflow discipline is governed by PF06. PF20 may reference these facts as metadata, but they are not acceptance tokens.

* Legacy note: Older PF20 epic records may list `PR_OPENED_OK` under “baseline PR tokens.” Treat it as metadata, not as part of the acceptance-token system.

##### **C. Evidence pointers (titles-only)**

* Human Evidence Index: `docs/evidence/INDEX.json` record titles

* Hash sentinel: `docs/evidence/INDEX.sha256`

* Machine Mirror: `artifacts/evidence_index.jsonl` records (artifact\_key \+ proof\_anchor)

* Close pack (canonical; lowercase path): `audit/qa/hde-epic<NNN>/...` (epic-specific close report \+ manifest outputs live under the epic QA root and must be declared explicitly in the Epic Record)

**CLI serializer/emitter guard evidence (when used as acceptance):**  
 If an epic uses CLI serializer/emitter guards as part of its acceptance, the canonical evidence paths MUST be:

* `artifacts/cli/guards/serializer_grep_guard.log`

* `artifacts/cli/guards/emitter_symbol_proof.txt`

Any `audit/gates/guards/...` copies are legacy/auxiliary and not required for epic acceptance.

##### D. Normative completion rule

An epic is not marked **Done** in PF20 until:

1. all required acceptance tokens for that epic are listed here, and

2. each token has corresponding evidence indexed in the human Evidence Index and machine mirror in the same PR, per PF06/PF09/PF12/PF19.

##### **E. Naming normalization (planning gate)**

All directory names used in Epic Records, evidence paths, and examples are non-conforming and must not be introduced into new plans.

In addition, epic close artifacts and epic QA roots MUST use canonical naming.

* **Epic QA root directory (canonical):**

  * `audit/qa/hde-epic<NNN>/` (example: `audit/qa/hde-epic022/`)

* **Epic close-pack outputs (canonical posture):**

  * Close-pack outputs MUST live under the epic QA root in a lowercase path: `audit/qa/hde-epic<NNN>/...`

  * The Epic Record MUST name the concrete close-pack outputs (including filenames) as part of the close-pack baseline, and those paths MUST be lowercase and stable.

Plans and implementations MUST NOT introduce parallel alternate forms (examples: `HDE-EPIC022`, `EPIC_022`, `audit/QA/...`, `audit/qa/HDE-EPIC022/...`, or `audit/EPIC-<NNN>_*`).

If legacy artifacts exist under non-canonical names, treat them as deprecated; preserve for history, but do not create new ones under deprecated patterns.

#### **QA Rails — Open/Close (Final PR)**

This section defines what an Epic Record is allowed to state about QA for the **final PR that closes the epic**.

**Hard boundary (PF20 vs QA canon):**

* PF20 is **epic planning canon**, not QA execution canon. PF20 Epic Records **stage** QA expectations only at the level of:

  * rails posture expectations (closed vs opened rails), and

  * acceptance token names (names-only), and

  * titles-only pointers to the governing QA documents and close-pack artifacts.

* PF20 Epic Records MUST NOT include QA planning artifacts or execution detail, including:

  * runbooks, commands, or command blocks,

  * step sequences / step-level “plans,”

  * embedded checklists or operator instructions,

  * per-step PASS/FAIL criteria,

  * QA\_ROOT subdirectory layout design, evidence directory naming schemes, or README generation rules,

  * CI self-test design details.

These QA execution details are authored as separate QA artifacts during Close Gate execution and are governed by “Glow QA Guide” and “Epic Process Guide” (titles-only).

##### **A. Final PR rails posture (staged configuration; NOT a runbook)**

For the final close PR, the Epic Record MUST make the rails posture explicit and auditable **without** prescribing how to run QA:

* **Closed rails default:** Final-PR CI and any acceptance-relevant proof runs are expected to operate under closed rails by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).

* **Opened rails exception discipline (if applicable):**

  * If any job/run relevant to acceptance is expected to open rails, the Epic Record MUST state that an opened-rails exception exists (for example: “network access is opened for \<scope\>”).

  * The Epic Record MUST require that evidence for **closed refusal** and **open conformance** is captured and indexed/mirrored in the same PR when such evidence is required by the governing QA posture.

  * The Epic Record MUST NOT describe the procedure (no job recipes, no steps, no commands, no operator guidance).

* **Evidence handling (names/pointers only):** Where the epic requires rails-related QA evidence for close, the Epic Record MAY point to the relevant close-pack artifacts (titles-only) that contain the evidence bindings; it MUST NOT duplicate the evidence content or its production procedure.

  ##### **B. Live QA requirement (closeout statement only)**

Live QA is required for eventual epic close.

* The Epic Record MUST include a **single statement** that Live QA is required for close, and may name the governing documents by title (Epic Process Guide; Glow QA Guide).

* The Epic Record MAY list Live-QA-related acceptance tokens that must be Green at close (names-only).

* The Epic Record MUST NOT embed a Live QA plan or runbook (commands, step sequences, QA\_ROOT directory design, evidence directory naming, README generator rules, or CI self-test design).

  ##### **C. QA-heavy epic guidance (planning rule)**

QA-focused epics must not exist solely to test themselves. QA-heavy work SHOULD either:

* upgrade shared QA harness/tools, or

* strengthen Live QA coverage across multiple existing surfaces and epics.

  ##### **D. Tokens (names-only, example set)**

* `QA_PRECOMMIT_CHECKLIST_OK`

* `QA_POSTCOMMIT_CHECKLIST_OK`

* `ENV_RAILS_POLICY_OK`

* `QA_EVIDENCE_ONLY_OK` (when a dedicated Live QA PR is used)

* `QA_CI_DIFF_SCOPED_OK` (when a dedicated Live QA PR is used)

* Any additional rails-specific tokens defined in PF04/PF09/PF19, as applicable.

  #### **Tracked Issues**

When closing an epic, the epic record MUST include a list of **tracked intra-epic issues** and their final status for this epic. 

In this document, an **issue** is any *unexpected* condition, behavior, gap, or risk discovered during implementation or QA, not a synonym for “deliverable” or “task.” An issue exists when reality diverges from the current plan or canon (for example: failing or flaky tests, ambiguous or conflicting specs, misaligned tools, missing or inconsistent evidence, surprising runtime behavior, or hard environment constraints such as “no user IDs in prod”). Planned work items, epics, and deliverables do **not** automatically become issues just because they are incomplete; they are tracked as issues only when there is something structurally blocking, surprising, or unclear about them (for example: “cannot be done under current rails,” “spec is incomplete,” or “tooling cannot represent required behavior”).

Every tracked issue must end the epic in one of these states:

* **Completed under this epic**

* **Carried forward to another epic** (with a concrete epic ID)

* **Promoted to a cross-epic issue** (ISSUE-XXX in §1 “Outstanding Issues”)

* **Explicitly dropped** (with a one-line rationale)

For each tracked intra-epic issue, the epic record SHOULD provide at least:

* **Issue ID** (e.g. `ISSUE-<EPIC>-<NAME>` or a short label if no ID is minted)

* **Title** (short, descriptive name)

* **Status** (for example: `Completed under <EPIC-ID>`, `Carried forward to <EPIC-ID>`, `Cross-epic ISSUE-XXX`, `Dropped`)

* **Scope / description** (1–3 sentences explaining what the issue covers)

* **Disposition for this epic** (brief note describing what happened to this issue in this epic: proved, carried forward, cross-epic, or dropped)

When listing issues:

* **Issues completed:**

  * Short list of issues whose **Status** is “Completed under \<EPIC-ID\>,” linking to §1 “Outstanding Issues (Cross-Epic)” where relevant.

* **Issues not done / out-of-scope:**

  * For each, make the disposition explicit:

    * **Moves to another epic:** name the destination epic ID.

    * **Becomes a new cross-epic issue:** give the ISSUE-XXX ID in §1.

    * **Explicitly dropped:** include a one-line rationale (“no longer aligned with current product scope,” etc.).

**Rule (normative):**  
 No epic is closed as “Done” while silently dropping known issues. Every known issue must be: **proved, carried forward, promoted to a cross-epic ISSUE-XXX, or explicitly dropped** in this section, with statuses and destinations clearly recorded.

#### **Plan Preflight (MUST)**

**PF23 consult (planning gate).**

* Before an Epic Record is treated as ready for approval (or promoted to “In Progress”), planners MUST consult **PF23 — Reality Audits** as a primary input for:

  * component boundaries (what the “thing” is), and

  * canonical pathnames/loci (where it lives).

* Epic Records SHOULD include a short “PF23 Anchors” trace that lists the component(s) consulted and the key pathnames/loci this epic will touch (traceability only; do not duplicate PF23 contents).

* PF23 is PO-maintained. If PF23 appears stale or missing required coverage, the epic record MAY note that as an observation, but MUST NOT assign PF23 updates as agent work.

Before an Epic Record is treated as **ready for approval** (or promoted to “In Progress”), the following MUST be true.

**Scope boundary (hard rule): Plan Preflight is Epic Planning only — not QA planning.**

* PF20 MUST NOT contain QA runbooks **at any time**.

* PF20 MUST NOT include QA execution instructions of any form, including (non-exhaustive):

  * step-by-step procedures,

  * command lines to run,

  * environment setup or “Step 0” snapshot procedures,

  * Codespaces operator instructions,

  * “fill PASS/FAIL” style manual verdict fields,

  * any other runbook-style operational checklist.

* If an epic requires QA execution (including Live QA), PF20 may only capture **planning-level outcomes**:

  * token names (names-only),

  * expected evidence families and canonical evidence paths (titles/paths only),

  * titles-only references to the canonical QA/runbook homes (“Glow QA Guide”, “Epic Process Guide”).

* Any runbook, QA plan, QA checklist, or QA execution rail belongs in its single home (titles-only), not in PF20.

##### .**A. Token registry validation (planning gate)**

* Every acceptance token name listed in the Epic Record (including the Epic Record’s “Tokens and Evidence (Acceptance)” section and the epic-specific acceptance roster) MUST be validated against the canonical token registry in “HDE Governance” (titles-only).

* Token lists in epic records are names-only planning rosters and MUST be treated as a validated view of the token registry, not as an authority.

* Unregistered token names MUST NOT be used in any PF20 acceptance roster or in any acceptance artifacts referenced by the epic (for example: acceptance maps, manifests, token→evidence matrices).

* If a new token is required, it MUST be routed via an explicit ADR and drained into the governing doc before PF20 may list it.

* Until drift is cleared, track token registry drift under the cross-epic issue record reserved in HDE Phased Epics §1 (titles-only); do not create competing local token lists.

##### **B. Close-pack baseline declared (planning gate)**

* The Epic Record MUST explicitly list the required close-pack artifacts (titles-only) for the epic close stage.

* At minimum, the close-pack baseline MUST include:

  * the epic close report, and

  * the epic manifest, and

  * the epic acceptance map, and

  * the token→evidence matrix (when required by the QA posture for that epic).

* Epic Plans MUST NOT be considered approvable if they omit this close-pack baseline file set for eventual epic close.

##### **C. Evidence bundle completeness for local-bundle deliverables (planning gate)**

When a deliverable claims a “local bundle” directory (example: `artifacts/ops/internal_version/*`):

* The deliverable’s “Evidence required” list MUST enumerate the complete required evidence paths (titles/paths only).

* If any required evidence lives outside the local bundle directory, the plan MUST name it explicitly and give its canonical path (titles/paths only), rather than assuming it is implicitly available.

##### **D. Canonical evidence-path binding validation (planning gate)**

Every acceptance token → evidence binding that appears in any of the following MUST be validated against the canonical evidence catalog in “HDE Schemas & Artifacts” (titles-only):

* the Epic Plan’s “Evidence required” lists, and

* the token→evidence matrix, and

* the Human Evidence Index, and

* the Machine Mirror, and

* the mirror proof anchors (path-proofs).

If the evidence catalog defines a fixed canonical path for a token’s evidence surface, the plan and all acceptance artifacts MUST bind to that exact path. Any non-canonical binding is a mechanical blocker unless routed via ADR.

Minimum artifacts that MUST agree when a token is claimed as satisfied:

* Epic Plan required evidence list (per deliverable)

* token→evidence matrix row for the token

* `docs/evidence/INDEX.json` entry for the bound artifact

* `artifacts/evidence_index.jsonl` mirror record for the same artifact key and discovered path

* the corresponding path-proof file referenced by the mirror record (`proof_anchor`)

Acceptance artifact hygiene (mechanical, plan-gate rule):

* The token→evidence matrix and acceptance map MUST NOT contain duplicate rows/entries for the same token.

* Placeholders are allowed only for scaffold-stage planning (example: D0 scaffold PR), and only for tokens that are not yet claimed as satisfied.

  * Once a token is claimed as satisfied, acceptance artifacts MUST bind to concrete, canonical evidence paths and MUST NOT contain placeholder evidence references (examples of prohibited placeholders: `TBD`, `{scenario}`, `{...}`).

* Acceptance artifacts (token→evidence matrix, acceptance map) MUST bind tokens to primary canonical artifacts and/or tests.

  * `*.path_proof.txt` files are proof anchors referenced via the Machine Mirror `proof_anchor` field and MUST NOT be bound as primary evidence unless the evidence catalog explicitly defines them as standalone evidence families.

##### **E. Lowercase directory naming (planning gate)**

All directory names used in Epic Records, evidence paths, and expected artifact layouts MUST be lowercase ASCII. Mixed-case or uppercase directory names are non-conforming and MUST NOT be introduced into new plans.

## **3\) Ops Task Record (Template)**

### **Definition**

An **Ops task** is any work item that requires privileged access to systems outside the repository and therefore cannot be performed by automated agents. This includes (non-exhaustive):

* service configuration

* secrets / env var changes

* deploy / runtime settings

* infrastructure console actions

* certain database operations (creation, grants, production migrations, other privileged state changes)

### **Execution authority (normative)**

* Ops tasks **MUST** be executed by the **PO (human operator) only**.

* Automated agents **MUST NOT** attempt to perform Ops tasks, **MUST NOT** claim completion, and **MUST NOT** simulate external state changes.

### **IA facilitation posture (normative)**

* Ops tasks **MAY** be part of an epic. When included, they are facilitated by the **Implementation Agent (IA)**, who **MUST** guide the PO through execution.

* IA guidance **MUST** specify **intent, constraints, verification, and evidence requirements** in a **what-not-how** manner, then work directly with the PO during execution.

### **Not a PR (normative)**

* Ops tasks are **not** Codex PRs and **MUST NOT** be represented as “implementable PR work.”

* Any plan/guide that includes both DEV work and OPS work **MUST** separate them and clearly label OPS work as: **PO-only execution, IA-guided**.

### **Ops Task record fields (required; what-not-how)**

Every Ops task record **MUST** include:

* **Task ID** (stable; referenced consistently)

* **Owner:** `PO`

* **Facilitator:** `IA`

* **Target system/service** (name only; no secrets)

* **Intent / desired end state** (what changes; what “done” looks like)

* **Constraints / safety rails** (what must remain true while executing)

* **Success criteria** (observable outcomes; not assumptions)

* **Evidence to capture** (what will prove the change; where it will be stored)

* **Rollback intent** (what “revert” means at a high level)

* **Secret handling note** (explicitly: no plaintext secrets in docs or evidence)

### **Evidence posture (required)**

Completion of an Ops task **MUST** produce a repo-stored evidence artifact bundle (text-first) under a lowercase path such as:

* `audit/ops/<epic-id>/...` for Ops execution evidence, or

* `audit/qa/<epic-id>/...` when the evidence is part of QA execution.

The Ops evidence bundle **MUST** include a command transcript sufficient to reproduce and audit what happened, secret-free:

* exact command(s) executed (verbatim)

* stdout capture

* stderr capture (separate from stdout where possible)

* exit status / return code

If the Ops task asserts any checksum verification (example: “OK”), the evidence **MUST** include the verifier output (or the exact verifier command plus its captured stdout/stderr) that produced the “OK” determination. Prose-only assertions are non-auditable.

If any file contents are embedded inside a report, embed the exact file contents as stored. Avoid terminal control sequences in embedded excerpts. If control sequences appear, record a **CAVEAT** and preserve a clean, copy/paste-safe representation alongside the raw file.

Evidence **MUST NOT** include secrets. If a setting/value is sensitive, evidence **MUST** be presence-only, redacted, or hashed, while still being sufficient to verify that the intended state was reached.

### **Build Checklist tracking requirement (normative)**

Any Ops task included in an epic **MUST** be represented as a subtask in **HDE Build Checklist** (titles-only), using the same **Task ID** and the same required fields.

### **No governance drift (normative)**

Ops tasks **MUST NOT** create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it **MUST** map to existing acceptance posture and be proven via evidence artifacts.

---

## **4\) Remediation Implementation Guide (Template)**

### **Scope**

This template applies to Remediation Implementation Guides produced for escalations and remediation execution. It does not change Live QA plan formats.

### **Copy/paste command safety (normative)**

If the guide includes command lines intended for copy/paste, default commands **MUST** be safe for the current epic context.

Do not present an epic-id flag for a different epic as a default. If an `--epic-id` (or similar) flag is mentioned, it **MUST** either:

* match the current epic ID, or

* be explicitly labeled optional/non-default with a one-line rationale.

### **Decision-bounded “TBD” rule (placement and coupling)**

If a placement/coupling decision is not yet proven (example: where a request-chain manifest should live), the guide **MUST NOT** assert a single fixed path.

Instead, mark the decision as `TBD` and constrain it:

* list the small set of plausible options (names/paths), and

* state the decision criteria and the enforcing validator/test that will fail closed if the wrong option is chosen.

### **Permitted step types (only)**

A Remediation Implementation Guide **MUST** use only two step types: **DEV** and **OPS**.  
 No other step types are permitted (no QA, DOC, REVIEW, or “verification-only” steps).

### **Verification embedding requirement (normative)**

All verification **MUST** be embedded inside the owning DEV or OPS step.

Verification **MUST** produce concrete, repo-stored evidence outputs (paths/filenames specified in the step).

### **OPS posture linkage (normative)**

OPS steps **MUST** follow the OPS posture defined in **§3** (PO-executed, IA-guided, not PR work, secret-free evidence, lowercase audit paths).

### **Strict lane separation (normative)**

A step labeled DEV **MUST** contain only DEV actions.

A step labeled OPS **MUST** contain only OPS actions.

If a DEV action depends on an OPS output (or vice versa), the producing step **MUST** come first and the dependent step **MUST** declare its dependency explicitly using the cross-lane dependency line rule below.

### **Cross-lane dependency line rule (locked; required when applicable)**

If a step depends on outputs produced by a prior step in the other lane, the dependent step **MUST** include exactly one cross-lane dependency line in this exact form:

**Inputs needed from Step S\<N\> during implementation: \<exact items\>**

Rules for this line:

* `S<N>` **MUST** be the actual producing step ID (no placeholders such as `Sx`).

* The line **MUST** appear exactly once in the dependent step. It **MUST NOT** be duplicated, nested, or prefixed by a placeholder field label.

* If there is no cross-lane dependency, the line **MUST** be omitted (no placeholder line).  
  **/internal/version auth posture non-invention (when relevant)**

**Interim posture (normative; until the auth epic lands).**

* `/internal/version` is treated as **operator-network-only** until token auth exists.

* Until token auth exists, guides MUST treat any auth header as **optional (never required)**. Any language that implies “auth required” must be treated as non-canonical unless/until implementation exists.

**Non-invention rule.**

If the guide references `/internal/version` access requirements, it **MUST NOT** state auth posture as canon.

Any auth posture statement **MUST** be explicitly labeled **Observed Evidence (non-PF)**.

**Evidence capture (auth posture; secret-free).**

* Always capture: status line \+ headers with **no auth header**.

* If an auth header is available (value redacted / presence-only noted), MAY capture a second request with the auth header present. Absence of an auth header MUST NOT be treated as a blocker under the interim posture.

### **/internal/version token naming (no aliases)**

If the guide references acceptance tokens for `/internal/version`, token names **MUST** match PF04 exactly.

Canonical conditional semantics token name: `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`. Any alias intended to mean “conditionals return 200 and never 304” is non-canon and **MUST NOT** appear in the guide.

### **/internal/version proof-surface invariants (explicit checklist; required when producing governed evidence)**

If the guide produces governed `/internal/version` evidence or claims any `*_OK` tokens about `/internal/version`, it **MUST** explicitly enumerate and verify (at minimum):

**A. Transport**

* GET returns 200

* HEAD returns 200 (parity expectations are met)

* conditional requests (If-None-Match / If-Modified-Since) do not yield 304; they return 200

**B. Headers**

* `Cache-Control: no-store` present

* `Content-Type: application/json; charset=utf-8` present

* `ETag` absent

* `Last-Modified` absent

**C. Body (identity payload)**  
 body is fixed-schema JSON with exactly these keys (no extras):  
 `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`

### **Token gating and coupling (normative)**

A guide **MUST NOT** claim any `*_OK` token unless the corresponding invariant is verified against the same captured bytes/headers written as evidence for that run.

If the run status is `FAIL_TOOLING` (or equivalent), the guide **MUST NOT** claim `*_OK` tokens for invariants that did not pass.

Captured headers, captured body, and any token claims **MUST** refer to the same resolved target/response chain. If coupling cannot be established, the run **MUST** be treated as `FAIL_TOOLING` and **MUST NOT** claim `*_OK` tokens.

### **Canonical template skeleton (paste-ready)**

**Artifact Map**  
 Inputs: `<paths or evidence identifiers>`  
 Output: Remediation Implementation Guide (for approval)

**Executive Summary**  
 ...

**Canon Frame (What “Correct” Means)**  
 `<testable statement> — PFxx — Title, §X.Y`

**Observed Evidence Snapshot (Self-Contained; non-PF)**

**Evidence inventory reviewed (non-PF)**  
 `<paths or quoted excerpts brought into this guide>`

**Primary failure signatures**  
 `<short quotes / exact status lines / exact headers>`

**Root Cause Analysis (RCA)**

**What went wrong**  
 **How it manifested**  
 **Root causes**

* Documentation ignored

* Documentation incorrect

* Documentation missing

**Remediation Implementation Plan (Stepwise, DEV/OPS only)**

**Step Overview (required)**

| Step ID | Step name | Step type | Step intent | Owner/role | Depends on | Cross-lane dependency | Outputs |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

**Step Details (required; repeat per step)**

* Step ID:

* Step name:

* Step type (DEV or OPS):

* Step intent (DISCOVERY or CHANGE):

* Owner/role:

* Preconditions:

* Inputs:

* Canon constraints (PF references):

* Actions (complete but scoped; what-not-how):

* Outputs (required):

* Verification (required, embedded; not a separate step):

* In-flight determinations (only if needed; must not be mechanical blockers):

* ADR linkage (if applicable):

**PF Docs Consulted**

* PFxx — Title

* ...

**ADRs Requiring Approval (Canon and External Task Creation)**  
 ADR-001...

