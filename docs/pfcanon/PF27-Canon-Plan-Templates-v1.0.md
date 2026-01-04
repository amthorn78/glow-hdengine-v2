# Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v1.0

**Status:** Canon

**Effective date:** 2026-01-03

**Last Update Gate:** BN 8.8.4

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

## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC\#\#\#  
Plan type: Live QA Plan / Runbook  
Execution venue: Codespaces (or Other: \_\_\_\_)  
Target environment: prod | dev | other: \_\_\_\_ (explicit)  
Plan revision: r\#  
Date (UTC): YYYY-MM-DD  
Operators (names-only): PO, IA, (optional) QA agent, (optional) Codex

#### Canon precedence statement (required)

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set (explicit; stable references only)

List the governing sources as PF ID \+ Title \+ Section (no filenames/versions).

* PF10 — HDE-Build Notes (relevant addenda: list addendum numbers \+ titles)  
* PF04 — HDE-Governance, §… (token registry \+ relevant invariants)  
* PF06 — Epic Process Guide, §0.4.1 (Discovery \+ QA RCA/Doc Delta)  
* PF19 — Glow QA Guide, §… (rails/evidence/step logs)  
* PF27 — Canon Plan Templates, §… (template obligations)

---

### Scope statement

#### Epic intent and boundaries (names-only; PF-anchored)

Epic record anchor(s): \<PF20 reference(s)\> (titles-only; do not paste PF20 prose here)

**In-scope surfaces / checks (names-only):**

* D0 …  
* D1 …  
* D2 …  
* D3 …

**Out-of-scope surfaces / checks (names-only):**

* …

#### PF10 overrides / conflicts (if any)

List each as:

* PF10 Addendum \<\#\> — → what it changes for this runbook → impacted PF references

---

### PF23 anchors

#### PF23 consult (required for planning)

PF23 is consulted for component boundaries and canonical loci.

#### PF23 anchors (names-only; optional but recommended)

Components consulted: …  
Key loci pulled (paths/names-only): …

(Do not duplicate PF23 content. This is a trace anchor only.)

---

### Environment and rails posture

#### Determinism pins (canonical pins only)

When producing governed bytes (evidence artifacts, canonical JSON, hash inputs), use:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

**Rule (normative):**

* Do not add new “pins” (example: PYTHONHASHSEED) as a plan-approval or execution requirement.  
* If ordering nondeterminism exists, fix it by explicit normalization (sorting keys/lists, stable ordering) in the step/tool, not by adding pins.

#### Rails posture (explicit)

Default rails for this runbook (fill values):

* SAFE\_MODE=\_\_  
* ALLOW\_NETWORK=\_\_  
* APP\_ENV=\_\_

If rails change by check, list it (names-only):

* \<check\_id\> → rails change → why change is needed → what evidence it produces

#### Gitless Live QA (non-negotiable)

* Runbook steps MUST NOT execute any `git …` command.  
* PASS/FAIL MUST NOT be gated on “working tree clean” or git status.  
* Traceability comes from governed identity artifacts and the captured evidence outputs, not VCS state.

---

### PO inputs needed

List all required external inputs by name only (never store secret values in plan artifacts).

Examples:

* HDE\_BASE\_URL (if needed)  
* HDE\_PROD\_BASE\_URL (if needed)  
* PORT (if needed)

Any auth/header inputs only as optional execution inputs where permitted by canon:

* AUTH\_HEADER\_NAME (names-only)  
* AUTH\_HEADER\_VALUE (never persisted; never logged; presence-only is allowed in snapshots)

**Rule (normative):**

* If a required input is missing at runtime, classify the affected check as TOOLING\_BLOCKED (do not guess).

---

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Canonical epic QA root MUST be lowercase:

* EPIC\_QA\_ROOT \= `audit/qa/hde-epic<NNN>/`

#### Check-centric, single-root evidence posture (normative)

This runbook is written for the check-centric posture:

* Canonical evidence outputs are organized by **check\_id** under EPIC\_QA\_ROOT as **current-state evidence**.  
* Per-run directory nesting MAY exist for convenience/history, but it is optional and non-canon.  
* No “latest\_run\_id” pointer files or “run-id as correctness key.”

#### Recommended canonical layout (default for new plans)

Use this layout unless an owning PF document defines a fixed canonical path for a specific artifact family.

* `audit/qa/hde-epic<NNN>/00_meta/`  
  Stable epic-level meta artifacts (current-state).  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/`  
  Current-state evidence for each check.

Within each `checks/<check_id>/`:

* Primary step log (required): `primary.log`  
* Supporting artifacts (optional): `tmp_*` files, `.sha256` sidecars where required, etc.

Optional (non-canon) history retention:

* `audit/qa/hde-epic<NNN>/runs/<attempt_label>/...`  
  Where `<attempt_label>` is a UTC timestamp label (git-free).  
  If you keep run-local copies here, they MUST be treated as convenience copies, not canonical acceptance binding surfaces.

#### Step-log header schema expectations (minimum; required)

Each primary step log MUST begin with a machine-readable header block containing at least:

* `check_id` (stable)  
* `status` (PASS | FAIL\_BEHAVIOR | FAIL\_TOOLING | TOOLING\_BLOCKED | PARKED)  
* `command` (literal command(s) executed for the check)  
* `captured_env` (rails \+ determinism pins \+ materially relevant env keys; values allowed only for non-secrets)

Token fields (only if token-relevant):

* `intended_tokens` (names-only; always populated for token-relevant checks)  
* `claimed_tokens` (names-only; populated only when status=PASS; empty list otherwise)

Notes:

* If a legacy field named `tokens` exists, treat it as `intended_tokens` only (never as a claim surface).

#### Step outcomes: tooling vs behavior (default mapping)

Use this default mapping unless a governing PF rule overrides it:

* Missing required PO inputs or required local files → TOOLING\_BLOCKED  
* Tool/command invocation failure (non-zero RC attributable to tooling) → FAIL\_TOOLING  
* Behavioral failure only when the surface is reachable and a valid response/output is captured, but it contradicts canon → FAIL\_BEHAVIOR

---

### Mandatory Step‑0 artifacts

These are execution deliverables and must be mechanically produced.

#### Step‑0A — Codespaces snapshot (mechanical; evidence not prose)

Purpose: capture rails/pins posture, tooling versions, and presence-only env/secrets context without leaking values.

Canonical output (current-state; epic-level):

* `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json`

Optional (non-canon) run-local copy:

* If produced under a run-local tree, it MUST be byte-identical to the epic-level snapshot.

#### Step‑0B — Doc Delta Capture (mechanical; runbook self-honesty)

Purpose: mechanically record repo reality mismatches, missing prerequisites, and canon conflicts as BLOCKERS vs CAVEATS.

Canonical output (current-state; epic-level):

* `audit/qa/<epic-id>/00_meta/doc_deltas.md` (or equivalent canon-owned name)

Requirements:

* Separate findings into BLOCKERS and CAVEATS with stable IDs.  
* Output “no deltas” when empty.  
* MUST be generated by commands (no manual fill placeholders).

#### Step‑0C — Prod handshake (identity-only) when target is prod-like

Include only if the plan claims Codespaces → prod behavior.

If using `/internal/version` as part of Step‑0C:

* Interim posture is canon: `/internal/version` is operator-network-only; no application-layer auth yet.  
* Runbooks MUST NOT require an auth header as a prerequisite.  
* A runbook MAY accept an auth header input as an execution convenience, but MUST NOT treat it as canon-required.

---

### Runbook Check Matrix

Every row MUST have a corresponding Check Block (below).

| check\_id | check\_name | surface / D-goal mapping | rails posture | PO command(s) | PASS/FAIL predicates | primary evidence path | deliverables (minimal set) | tokens (optional) | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| D0\_codespaces\_snapshot | Codespaces snapshot | D0 / discovery | SAFE\_MODE=?, ALLOW\_NETWORK=? | … | … | `audit/qa/<epic-id>/00_meta/codespaces_snapshot.json` \+ `audit/qa/<epic-id>/checks/<check_id>/primary.log` | … | (optional) | PF… |
| … | … | … | … | … | … | … | … | … | … |

Matrix rules (normative):

* Commands must be copy/paste-ready.  
* PASS/FAIL predicates must be explicit and mechanically checkable.  
* Tokens are optional; if present, use names-only from governed acceptance artifacts; no invention/aliases.

---

### Check Blocks

Repeat one block per matrix row.

#### CHECK \<check\_id\>: \<check\_name\>

Surface / D-goal mapping: \<D\# \+ surface\>  
Rails: SAFE\_MODE=… ALLOW\_NETWORK=… APP\_ENV=…  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PFxx — Title, §X.Y (titles-only)

**PO command(s) (copy/paste)**

* One command or a tight, explicit pipeline.  
* If multiple commands are required, list them explicitly and capture them in the step log header `command`.

**Expected result (PASS/FAIL predicates)**

PASS if:

* \<predicate 1\>  
* \<predicate 2\>

FAIL\_BEHAVIOR if:

* 

FAIL\_TOOLING if:

* \<tool invocation failure / non-zero RC attributable to tooling\>

TOOLING\_BLOCKED if:

* \<missing required input / missing file / missing binary / unreachable prerequisite\>

**Primary evidence artifact (required)**

Canonical (current-state) primary log:

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`

One-line description:

* “Header (command \+ captured\_env \+ status) \+ transcript \+ grep/diff outputs \+ PASS/FAIL predicates.”

**Deliverables (minimal evidence set; fully-qualified paths)**

List only what is required to judge this check:

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
* \<any required sidecar evidence files (sha256, json, etc.)\>

If no new files:

* “No new files; inspects … only.”

**Tokens (optional)**

If this check is token-relevant:

* intended\_tokens: list names-only in the step log header  
* claimed\_tokens: only populate in the step log header when status=PASS

No token-roster labor:

* The plan is not approved/rejected on completeness of token lists.

---

### Close-out deliverables

This runbook MUST ensure the epic produces the execution deliverables required by the Epic Process Guide:

* Discovery artifact (Step‑0 artifacts satisfy this when properly defined by canon)  
* QA RCA & Doc Delta summary (execution deliverable)

#### What “QA RCA & Doc Delta summary” means (explicit; non-drifting)

In this posture, “QA RCA & Doc Delta summary” is not a debugging diary and not a demand for narrative prose.

It is a closure-oriented summary artifact that:

* states what Live QA found (or explicitly states “no new deltas found”),  
* maps any substantive findings to PF-Canon doc delta intents by PF title, and  
* records deferrals (if any) as deferrals (not as “unknowns”).

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

### Review guardrails

Hard blockers for plan approval/execution:

* Manual result placeholders (“fill PASS/FAIL”, “operator summary”, etc.).  
* Any `git …` command in PO-executable steps.  
* Helper/wrapper scripts not canon-named by explicit path (unless the full tool source is embedded in the plan and written under `audit/qa/<epic-id>/...` before execution).  
* Missing Step‑0 mechanical artifacts (Codespaces snapshot \+ Doc Delta Capture) when in Codespaces.  
* Any check listed in the matrix without a corresponding Check Block (or vice versa).  
* Closure-scoped plans containing placeholder non-PASS steps for closure-critical artifact families (scope must be downgraded or resolved via canon-safe ADR before execution).

Caveats (allowed, must be mechanically logged):

* DOC\_DRIFT — plan adapts to repo reality; record mismatch mechanically and drain later.  
* ENV\_DRIFT — environment differs from baseline; capture mechanically; do not invent new rails.  
* UNREGISTERED\_TOKEN — registry mismatch is evidenced mechanically (validator output); do not maintain narrative lists.

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

