# Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v1.1.8

**Status:** Canon

**Effective date:** 2026-01-24

**Last Update Gate:** BN 9.4.4 Drain A30-31

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

 **Template-safe placeholders and ellipsis prohibition (hard).**

* Canonical documents and plan records MUST NOT contain either of:

  * the ASCII triple-dot sequence, or

  * the Unicode ellipsis character.

* Only the following template replacement markers are permitted in canonical documents and plans:

  * `<PLACEHOLDER_NAME>`

  * `[OMITTED]`

  * `[LIST CONTINUES]`

  * `[SNIP: <n> lines omitted]`

  * `[INTENTIONALLY LEFT BLANK]`

* Prohibited placeholders include informal stand-ins such as curly-brace placeholders or the word “TBD” (unless the word “TBD” is part of a formal decision-bounded rule as defined in the Remediation Implementation Guide template).

* Review handling: if an ellipsis is observed in a canonical doc or plan during review, treat it as a hard defect to be corrected (replace with a permitted marker). If the ellipsis appears because a viewer cut text, treat it as a tooling/read failure and re-open until the full source text is visible.

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

#### **Canon set (explicit; stable references only)**

Canon set (titles-only, names-only, no version numbers in prose):

* PF10 — HDE-Build Notes (relevant addenda: list addendum numbers and titles)

* PF04 — HDE-Governance, §\<SECTION\> (token registry and acceptance invariants)

* PF06 — Epic Process Guide, §0.4.1 (Discovery \+ QA RCA/Doc Delta)

* PF09 — HDE Build Checklist, §4.9 (evidence index refresh \+ path-proof regeneration in close-pack)

* PF12 — HDE Schemas & Artifacts, §\<SECTION\> (evidence index refresh flow: canonical filenames \+ refresh order)

* PF19 — Glow QA Guide, §\<SECTION\> (rails, evidence, step logs)

* PF27 — Canon Plan Templates, §\<SECTION\> (template obligations)

Note: PF20 may be cited only for historical record context, never as a source of requirements.

### **Scope statement**

This plan evaluates the following in-scope surfaces / checks:

* D0 \<SURFACE\_OR\_CHECK\_NAME\>

* D1 \<SURFACE\_OR\_CHECK\_NAME\>

* D2 \<SURFACE\_OR\_CHECK\_NAME\>

* D3 \<SURFACE\_OR\_CHECK\_NAME\>

* \[LIST CONTINUES\]

This plan explicitly excludes:

* \<SURFACE\_OR\_CHECK\_NAME\>

* \[LIST CONTINUES\]

#### PF10 overrides / conflicts (if any)

List each as:

* PF10 Addendum \<\#\> — → what it changes for this runbook → impacted PF references

---

### **PF23 anchors**

**Planning-time consult only (normative).**

* PF23 consult is planning-time traceability posture, not a Live QA execution surface.

* Live QA Plans MUST NOT include any required deliverable whose purpose is “PF23 consult capture,” “PF23 note,” or similar. No PF23 consult artifacts are required for QA execution or acceptance review.

* Live QA Plans MUST NOT instruct the operator to run repo commands in order to “prove PF23 consult.”

**Trace anchor (optional; plan text only).**

* If a trace anchor is desired, it lives in the plan text only (names-only).

* A plan MAY include a single PF23 Anchors note (components consulted \+ loci touched), but it is informational only and MUST NOT appear as a required check or required evidence output.

**Rule (normative): PF23 consult is not an acceptance token.**

* Plans and implementations MUST NOT mint, claim, or reference `REALITY_AUDIT_OK` (or any similar “PF23 consult completion” acceptance token) unless and until Governance registers such a token in the token registry.

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

  #### **No VCS workflow content (hard)**

Live QA Plans exist to execute checks and produce evidence. VCS workflow (branches/commits/PRs) is handled manually by the PO.

* Live QA Plans MUST NOT instruct or discuss branch/commit/PR workflow (checkouts, merges, rebases, PR creation, etc.).

* Live QA Plans MUST NOT gate PASS/FAIL on VCS state (“working tree clean”, branch name, commit SHA, PR identifiers, etc.).

* Limited `git <READ_ONLY_COMMAND>` commands are allowed only as optional *non-gating* sanity checks, and only when all are true:

  * Read-only / non-mutating intent (no checkout/reset/commit/push/pull).

  * Used only to confirm “this is a repo” / “repo root exists”.

  * Does not print or rely on branch names, commit SHAs, or PR identifiers.

  * Not used as evidence or acceptance criteria.

  * If the sanity check fails, classify the affected check as TOOLING\_BLOCKED (not FAIL\_BEHAVIOR).

* Traceability comes from governed identity artifacts and captured evidence outputs, not VCS state.

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
* Structured report sidecars (optional; but if listed in the plan’s required deliverables, filenames MUST match the produced outputs):  
  * D23 evidence index snapshot contract: `evidence_index_snapshot_contract_report.json` (canonical; replaces plan-listed `snapshot_contract_validation.json`)  
  * Evidence-path binding validation: `evidence_path_binding_validation_report.json` (canonical; replaces plan-listed `binding_validation_report.json`)  
* Captured CLI output snapshots (optional; REQUIRED when stdout/stderr is treated as the proof payload for a check):  
  * Token registry validity checks (e.g., `po-006_token_registry_validity`): `rg_acceptance_map_output.txt`, `rg_registry_output.txt`  
* Supporting artifacts (optional): `tmp_*` files, `.sha256` sidecars where required, etc.

Optional (non-canon) history retention:

* `audit/qa/hde-epic<NNN>/runs/<attempt_label>/<RUN_LOCAL_SUBTREE>/`  
* where `<attempt_label>` is a UTC timestamp label (git-free).  
  * If you keep run-local copies here, they MUST be treated as convenience copies, not canonical acceptance binding surfaces.

  #### **Step-log header schema expectations (minimum; required)**

Header MUST include, at minimum:

* `check_id`: stable check ID (must match the matrix `check_id`).

* `status`: `PASS` | `FAIL_BEHAVIOR` | `FAIL_TOOLING` | `TOOLING_BLOCKED` | `SKIPPED` | `WARN`.

* `fail_status`: required; MUST be `""` when `status: PASS`; otherwise MUST equal `status`.

* `command`: the exact command string executed (or `N/A` if no command applies).

* `command_provenance`: `Codex Prompt` | `Copy/paste from plan` | `Explicitly created`.

* `captured_env`: object with `MODO_AI_BUNDLE` / `MODO_AI_VERBOSE` / `MODO_RAILS` / `LC_ALL` / `LANG` / `TZ` (values may be blank).

* `pf_refs`: array (may be empty; MUST be present).

* `intended_tokens`: array (may be empty; MUST be present).

* `claimed_tokens`: array (may be empty; MUST be present).

Notes:

* record both the command and the creation mechanics (Codex prompt vs copy/paste vs manual).

* `captured_env` MUST include `MODO_AI_BUNDLE` / `MODO_AI_VERBOSE` / `MODO_RAILS` / `LC_ALL` / `LANG` / `TZ`.

* **No ad-hoc header JSON:** plans MUST NOT instruct operators to hand-type or hand-edit a header JSON object. Step templates MUST generate the header via the canonical header-writer snippet below (or a repo-defined canonical helper that emits the same keys), so required keys cannot drift or be omitted when the schema evolves.

* If a script is required, prefer ephemeral helpers under `/tmp` and write only evidence outputs under `audit/**` or `artifacts/**`.

* If the evidence format is missing required fields (including `pf_refs`, `intended_tokens`, `claimed_tokens`, or `fail_status`), the check MUST record a CAVEAT and MUST NOT be treated as closure-proof until the format is corrected.

* Avoid escaping/control sequences in embedded excerpts, and ensure copy/paste-safe representations.

**Canonical step-log header writer (paste-ready; emits header JSON with all required keys):**

`# Writes a single-line JSON header to stdout.`

`# Set these environment variables before running:`

`#   CHECK_ID, STATUS, COMMAND, COMMAND_PROVENANCE`

`# Optional (defaults are empty/[]):`

`#   FAIL_STATUS, PF_REFS_JSON, INTENDED_TOKENS_JSON, CLAIMED_TOKENS_JSON`

`python - <<'PY'`

`import json, os`

`def get(k, default=""):`

    `v = os.environ.get(k)`

    `return v if v is not None else default`

`header = {`

    `"check_id": get("CHECK_ID"),`

    `"status": get("STATUS"),`

    `"fail_status": get("FAIL_STATUS", ""),`

    `"command": get("COMMAND"),`

    `"command_provenance": get("COMMAND_PROVENANCE"),`

    `"captured_env": {`

        `"MODO_AI_BUNDLE": get("MODO_AI_BUNDLE"),`

        `"MODO_AI_VERBOSE": get("MODO_AI_VERBOSE"),`

        `"MODO_RAILS": get("MODO_RAILS"),`

        `"LC_ALL": get("LC_ALL"),`

        `"LANG": get("LANG"),`

        `"TZ": get("TZ"),`

    `},`

    `"pf_refs": json.loads(get("PF_REFS_JSON", "[]")),`

    `"intended_tokens": json.loads(get("INTENDED_TOKENS_JSON", "[]")),`

    `"claimed_tokens": json.loads(get("CLAIMED_TOKENS_JSON", "[]")),`

`}`

`print(json.dumps(header, ensure_ascii=False))`

`PY`

* 

### Mandatory Step‑0 artifacts

These are execution deliverables and must be mechanically produced.

#### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Purpose: mechanically record repo reality mismatches, missing prerequisites, and canon conflicts as BLOCKERS vs CAVEATS.

**Moon Loop allowed (bounded).**

* A Live QA Plan MAY include a “Moon Loop” clause to allow minimal in-session remediation solely to unblock planned checks that are blocked by trivial prerequisites.

* Moon Loop work MUST be explicitly declared, scoped to the minimum change needed, and captured as evidence (diff/log \+ why \+ which check(s) were unblocked \+ evidence paths) under `audit/qa/<epic-id>/00_meta/delta/`.

* Hard boundary: Moon Loop MUST NOT expand scope into new acceptance surfaces or feature work. If the needed change is not trivially bounded, stop and escalate to a remediation guide.

* Stop condition: If Moon Loop work exceeds a short, bounded threshold (e.g., \>30 minutes or touches multiple subsystems), stop and convert to a remediation guide.

**Doc-delta surfaces (required; two-surface pair).**

MUST treat doc-deltas as a two-surface pair:

1. Draft/staging surface under `audit/docdeltas/` (used for the in-flight doc-delta artifact and token↔evidence binding).

2. Epic-scoped capture surface at `audit/qa/<epic-id>/00_meta/doc_deltas.md` (used as the stable QA record for the epic).

Naming and binding rules:

* The draft/staging surface MUST use a concrete filename. Placeholders like `audit/docdeltas/<doc-delta>.md` are nonconforming.

* SHOULD standardize the draft filename as: `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase epic-id), unless superseded by a later canon naming rule.

* The Epic Plan’s token↔evidence bindings MUST reference:

  * the draft/staging surface for doc-delta token evidence, and

  * the epic-scoped capture file as the authoritative narrative/record surface.

Canonical output (current-state; epic-level):

* `audit/qa/<epic-id>/00_meta/doc_deltas.md`

Requirements:

* Separate findings into BLOCKERS and CAVEATS with stable IDs.  
* Output “no deltas” when empty.  
* MUST be generated by commands (no manual fill placeholders).  
* MUST record plan-vs-execution drift for any runner/command mismatch (including missing scripts replaced by `python (embedded)` harness execution), with an evidence pointer to the step `primary.log` showing the executed command.  
* If a plan-listed mismatch is filename-only (for example, a report JSON name differs) but an equivalent artifact exists and supports the same PASS/FAIL predicate, treat it as a **CAVEAT** (not a **BLOCKER**). Record expected → actual filenames. Do not mark **PASS** unless the predicate can be evaluated from the actual artifact(s).  
* Evidence hygiene follow-ups that are not plan-required deliverables (for example, path-proof refreshes, Evidence Index entry additions) MUST be recorded as **CAVEATS** / follow-ups and MUST NOT be treated as blockers unless explicitly made plan-required.

#### Step‑0C — Prod handshake (identity-only) when target is prod-like

Include only if the plan claims Codespaces → prod behavior.

If using `/internal/version` as part of Step‑0C:

* Interim posture is canon: `/internal/version` is operator-network-only; no application-layer auth yet.  
* Runbooks MUST NOT require an auth header as a prerequisite.  
* A runbook MAY accept an auth header input as an execution convenience, but MUST NOT treat it as canon-required.

---

### Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| D0\_discovery | Discovery posture | D0 | SAFE\_MODE=; ALLOW\_NETWORK=; APP\_ENV= | `<COMMANDS>` | PASS if ; FAIL\_BEHAVIOR if ; TOOLING\_BLOCKED if | `audit/qa/<epic-id>/checks/D0_discovery/primary.log` | `<DELIVERABLE_PATHS>` | \[INTENTIONALLY LEFT BLANK\] | PF27 — Canon Plan Templates, § |
| \<check\_id\> | \<check\_name\> | \<D\_GOAL\> | \<RAILS\_POSTURE\> | `<COMMANDS>` | \<PASS\_FAIL\_PREDICATES\> | `<PRIMARY_EVIDENCE_PATH>` | `<DELIVERABLE_PATHS>` | `<TOKEN_NAME_1>, <TOKEN_NAME_2>` | \<PF\_ANCHORS\> |

Every row MUST have a corresponding Check Block (below).

Matrix rules:

* Every check\_id in the matrix MUST be accompanied by a CHECK block below.

* PASS/FAIL predicates MUST be mechanical and audit-ready.

* Tokens (optional):

  * MUST be names-only and MUST match the PF04 acceptance token roster exactly (case-sensitive).

  * Do not claim aliases or legacy spellings. The deprecated alias `QA_STEP_LOGS_CONSOLIDATED_OK` MUST be normalized to `QA_HARNESS_DISCIPLINE_OK`.

  * D23 evidence index snapshot is tokenless (do not claim acceptance tokens from it).

---

### Check Blocks

Repeat one block per matrix row.

#### **Embedded harness checks (pattern; use when no standalone script exists)**

Use this pattern when a check is executed by invoking an existing harness runner that performs the check internally (no dedicated script exists for the check).

* In the matrix row, set **commands (PO-only)** to the exact `python (embedded)` invocation you will run (include the harness runner repo path).

* In the CHECK block, record the same `python (embedded)` invocation under **PO command(s)**.

* Evidence outputs MUST still be concrete, governed paths. Include the check `primary.log` plus any check-specific governed output(s) produced by the embedded harness (example: `audit/qa/<epic-id>/checks/<check_id>/token_matrix.json`).

* If the Approved Plan named a runner script or auxiliary artifact that does not exist or is not produced, record it as `DOC_DRIFT` in Step-0B (Doc Delta Capture) and proceed only if the governed evidence outputs exist and are verified.

#### **Canon check clarifications (addenda-driven; locked)**

Use this section only when the Live QA Plan includes the referenced check ID.

**D07\_sanity\_pipeline — log evidence surface \+ pytest posture**

* The sanity pipeline log evidence surface is fixed: `audit/gates/sanity_pipeline/sanity_pipeline.log`.  
  * If a plan requires a path-proof transcript for this log, the canonical path-proof is the sibling file `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`.   
  * If a path-proof transcript is not required, the plan MUST NOT list any `*.path_proof.txt` for this log.

* Plans MUST NOT introduce alternate/duplicate locations (example: `artifacts/sanity_pipeline/...`) for the same run.

* Plans MUST NOT assume `pytest` is installed. If `pytest` is missing at execution time, mark the step `TOOLING_BLOCKED` (not `FAIL`) until the dependency is available (or is unblocked via an explicit Moon Loop change captured as DOC\_DRIFT in Step-0B).

**PO-017\_lowercase\_naming — scope and predicate**

* This rail scans **directory names only** (not filenames).

* Scope is limited to QA-created loci: `audit/qa/<epic-id>/` and `artifacts/`.

* `docs/` is out of scope for this rail.

* Uppercase filenames under QA bundles do not violate this rail unless they appear in directory names.

**D08\_cli\_guardrail — CLI main module path reference**

* If the check asserts/inspects the CLI main module path, the expected path is `engine/cli/main.py` (not `cli/main.py`).

* If a plan references a different path, treat the discrepancy as DOC\_DRIFT and capture it in Step-0B (Doc Delta Capture), while ensuring the check predicate is evaluated against the correct on-disk path.

#### CHECK \<check\_id\>: \<check\_name\>

Surface / D-goal mapping: \<D\# \+ surface\>  
Rails: SAFE\_MODE=\<value\> ALLOW\_NETWORK=\<value\> APP\_ENV=\<value\>  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PFxx — Title, §X.Y (titles-only)

**PO command(s) (copy/paste)**

* One command or a tight, explicit pipeline.  
* If multiple commands are required, list them explicitly and capture them in the step log header `command`.  
* If no command is required (manual review only), set the step log header `command: N/A` **and** ensure every required deliverable is Audit-proven (pre-existing at review time). If any required deliverable must be generated during QA (including via a helper script), commands MUST be listed explicitly (no “None required”).

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
* `audit/qa/<epic-id>/qa_step_logs_manifest.json` (Canon-defined | Required) — QA-created current-state manifest; MUST include an entry per executed check recording at minimum `check\_id`, `status`, and `log\_path` (additional cryptographic metadata allowed). TOOLING\_BLOCKED steps MUST still be listed (do not omit posture-only checks).  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` (Canon-defined | Required) — QA-created sibling path proof for the manifest (generate after manifest updates).

One-line description:

* “Header (command \+ captured\_env \+ status) \+ transcript \+ grep/diff outputs \+ PASS/FAIL predicates.”

 **Deliverables (minimal evidence set; fully-qualified paths)**

List only what is required to judge this check.

Path provenance (required; per required path): annotate each required path with exactly one tag:

* (Canon-defined) — the path/pattern is defined by PF canon (explicitly, or as a canonized path family/pattern).

* (Audit-proven) — the path’s existence is proven by existing canon-recognized audit artifacts (governed evidence/proofs) for this epic/run.

* (QA-created) — this runbook step will create the path during execution.

Rules (normative):

* The plan MUST NOT list any required path that is neither Canon-defined, Audit-proven, nor QA-created (no fabricated paths).

* If a required path is QA-created, the owning Check Block MUST include explicit create \+ validate mechanics:

  * exact mkdir \+ write instructions appear in PO command(s) (copy/paste),

  * the purpose of the created bytes is stated, and

  * PASS/FAIL predicates validate the created bytes mechanically (not prose assertions).

* QA-created writes MUST remain under `audit/**` or `artifacts/**` only.

* Plans MUST separate pre-existing artifacts (expected to exist before execution) from QA-run artifacts (created during execution). “Presence” gating MUST apply only to the pre-existing set; QA-run artifacts MUST NOT be treated as preflight requirements unless created in that same preflight step.

Required paths (examples; replace as needed):

* `audit/qa/<epic-id>/checks/<check_id>/primary.log` (Canon-defined)

* \<any required sidecar evidence files (sha256, json, etc.)\> (Canon-defined | QA-created)

If no new files:

* “No new files; inspects \<paths\> only.” (Canon-defined | Audit-proven)

**Tokens (required fields; may be empty)**

For every check, the step log header MUST include `intended\_tokens` and `claimed\_tokens` as arrays (names-only).

If this step is token-relevant, list the intended and claimed tokens:

* `intended\_tokens`: list the intended token names (names-only; must match PF04 exactly)

* `claimed\_tokens`: list the token names actually proven by this check (names-only; must match PF04 exactly)

If this step is not token-relevant:

* `intended\_tokens`: `[]`

* `claimed\_tokens`: `[]`

Rules:

* Names only (no semantics) and must match PF04 exactly.

* `claimed\_tokens` MUST NOT include any `*\_OK` token unless evidence in this step proves it.

* If `status != PASS`, `claimed\_tokens` MUST be an empty list.

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
* includes an explicit readiness / closeout recommendation that is justified with evidence pointers to the QA event stream and named artifacts; missing required tokens/evidence MUST be labeled as **Unknown** (no inference).  
* if a Live QA Plan exists/was used, includes explicit coverage mapping vs the QA Plan step requirements and Findings (no silent drops); any mismatches must be called out explicitly (plan vs execution reality).  
* summarizes remediation actions (including any Moon Loop work) as: what changed, why, which check(s) were unblocked / re-verified, and where the supporting evidence lives (diff/log paths).  
* enumerates known open issues and deferred work with disposition (waive / defer / follow-up) and the evidence impact.

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

## **Review guardrails**

### **Hard blockers for plan approval/execution**

* All inputs and paths MUST be explicit and reproducible. Any required path that is not canon-defined, audit-proven, or explicitly QA-created by this plan with inline create \+ validate mechanics is blocked. No fabricated paths.  
* No interactive steps. The plan must be runnable headlessly (and must log all commands).  
* Command entrypoints must resolve. Any plan-provided command that names a repo file by path MUST either:  
  * (a) point to an existing repo file at review time, OR  
  * (b) be explicitly QA-created by this plan with inline create \+ validate mechanics before execution (and recorded as `DOC_DRIFT` in Step-0B).  
* If the step is executed via an embedded harness function (no standalone script exists), the plan MUST use `python (embedded)` and cite the harness runner repo path.  
* New recurring artifact families/paths introduced ad hoc in a plan (not already governed by PF10) are blocked until introduced via PF10 addendum.  
* Helper/wrapper scripts are blocked unless canon-named by explicit path (for example, `tools/evidence/run_<check>.py`) OR the full tool source is embedded and written under `audit/qa/...` before execution.  
* All evidence artifacts must be under `audit/` and be hashed or proven as required.  
* `/tmp` helper scripts MUST NOT print or persist secrets.

 **ADR discipline (canon-resolution only; drain targets required):**

* If canon already speaks on a topic, do not write an ADR. Cite the owning PF(s) and remove any ADR placeholder/stub.

* Any ADR included in a Plan or Remediation MUST represent a canon resolution decision (what ambiguity/conflict is resolved, and what decision is taken).

* Every ADR MUST declare explicit drain targets (owning PF docs \+ intended doc-delta updates required to canonize the decision).

* ADRs MUST NOT cite PF20 as a source of requirements, rails, acceptance semantics, or evidence-surface definitions (PF20 is historical-only).

KISS evidence posture for Live QA (normative):

* Live QA Plans MUST minimize required outputs to:

  * one primary step log per check under `audit/qa/<epic-id>/checks/<check_id>/primary.log`, and

  * the step-logs manifest listing check IDs, status, and log paths (current-state, not per-run history).

* Prefer “validate existing canon evidence” over “produce new QA artifacts”:

  * If PF10/PF-canon already establishes an artifact family/path, the QA plan validates it (exists \+ minimal posture checks) and records PASS/FAIL in the check’s primary.log.

  * QA creates new artifacts only when the check is specifically about QA-run outputs (step logs, manifest) or when canon explicitly requires a generated QA artifact family/path.

* Any additional required artifact must be explicitly justified as acceptance-decisive and must be canonized (and path-pinned) by PF10 or PF-canon as a governed evidence family/path.

Explicit non-blockers (do not gate approval):

* A plan MUST NOT be rejected solely because it does not use fenced code blocks. The gate is copy/paste safety \+ mechanical evidence, not Markdown rendering.

* Optional environment snapshots (including any “Codespaces snapshot”) MUST NOT be required deliverables and MUST NOT be used to decide PASS vs REMEDIATION NEEDED.

Caveats (allowed, must be mechanically logged):

* DOC\_DRIFT — plan adapts to repo reality; record mismatch mechanically and drain later.

* ENV\_DRIFT — environment differs from baseline; capture mechanically; do not invent new rails.

* UNREGISTERED\_TOKEN — registry mismatch is evidenced mechanically (validator output); do not maintain narrative lists.

  ## **2\) HDE-EPIC-Plan**

This section defines the **Epic Plan** template used for in-flight planning and close preparation.

**Historical-only posture (normative):**

* PF20 HDE-Phased Epics MUST contain only completed epic records.  
* In-flight epics MUST NOT be added to HDE-Phased Epics (no partial records; no placeholders).  
* Archive-on-close: the epic record is added to HDE-Phased Epics only once, at epic close, as a final historical entry.

### **Epic Record Template (Normative)**

For every epic, fill out the following fields as the **Epic Plan record**. At epic close, the final Epic Plan record is archived into HDE-Phased Epics as the historical entry.

#### **Meta**

* **Epic ID:** `HDE-EPICXXX`

* **Epic name (short):**

* **Alchemical phase:** (exact phase name per PF21, e.g. `Calcination`, `Dissolution`)

* **Phase rationale (1–3 sentences):** Why this epic belongs in this phase.

* **Status:** `Planned | In Progress | Blocked | Pending Review | Done | Won’t Do | Superseded`

* **Date started:** `YYYY‑MM‑DD`

* **Date completed:** `YYYY‑MM‑DD` (or \[INTENTIONALLY LEFT BLANK\])

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

* Each OPS task MUST be specified using the required Ops Task record fields defined in PF27 §3, including: Task ID, intent, constraints/rails, success criteria, evidence to capture (repo path), rollback intent, and secret handling note.

* Ops-task completion MUST be proven by evidence in `audit/ops/<epic-id>/<task_id>/` with a corresponding QA evidence pointer in `audit/qa/<epic-id>/<task_id>/`

* Any Ops task included in the epic MUST also be represented as a tracked subtask in **HDE Build Checklist** (titles-only), using the same Task ID and fields.

**Evidence-only deliverables (allowed; not acceptance tokens by default).**

Some deliverables are required evidence artifacts but are not acceptance tokens unless Governance registers tokens and defines their semantics.

Default posture (normative): guard proofs (example: serializer/emitter guard proofs) are **evidence-only deliverables**, not acceptance tokens.

* Plans MUST NOT introduce or claim new “guard tokens” unless the token exists in the canonical token registry owned by HDE Governance.

* Evidence-only does not mean loose: guard proof artifacts MUST be mechanically generated, reviewable, and (when used for closure wiring) follow normal governed-evidence discipline (stable path; index/mirror updates when bytes change; sibling path proofs when required by Evidence Catalog posture).

List **concrete, observable deliverables**; each should be testable:

* **Deliverable D1:**  
  * *Job to be done:*  
  * *Evidence required:* (artifact titles, mirror records, snapshots; titles-only)  
  * *PF references:* (PF titles \+ sections, e.g. “PF14 — HDE Mechanics Guide §1.3 Evidence & CI coupling”)

Repeat D2, D3, and additional deliverables as needed.

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

The Epic Plan MUST list evidence pointers to governed artifacts and demonstrate explicit binding to canonical paths defined in “HDE Schemas & Artifacts.”

**Evidence Index Refresh Flow (reference lock; required when a plan claims index/mirror refresh):**

* The plan MUST cite the canonical refresh sequence defined in PF12.

* The plan MUST state that the refresh updates the canonical refresh set:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

  * `artifacts/evidence_index.jsonl.sha256`

  * and any required sibling path-proof transcripts using the suffix `<artifact>.path_proof.txt` (for example: `docs/evidence/INDEX.json.path_proof.txt` and `artifacts/evidence_index.jsonl.path_proof.txt`).

* The plan SHOULD include the canonical tool invocation and filename set from the Addenda (PF10).

* The plan MUST bind evidence index and mirror operations to canonical paths (no alternate evidence index locations; no alternate mirror homes).

Evidence pointers MUST cite the following canon:

* Epic QA root (canonical; lowercase path): `audit/qa/hde-epic<NNN>/`  
   This is the epic QA root for step logs and run artifacts and must be declared explicitly in the Epic Record.

* Evidence Index (canonical): `docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`

* Machine Mirror (canonical mirror home): `artifacts/evidence_index.jsonl` with companion `artifacts/evidence_index.jsonl.sha256` and sibling path-proof transcript `artifacts/evidence_index.jsonl.path_proof.txt`

* Evidence index snapshot (if produced by D23): `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json` and `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

**CLI serializer/emitter guard evidence:** If the epic uses a canonical serializer/emitter pipeline:

* The plan MUST cite the exact check IDs that prove serializer equivalence and unmodified output.

* Any `audit/gates/guards/<SUBTREE>/` copies used to support the plan MUST be mentioned in the “Evidence pointers” block.

##### D. Normative completion rule

An epic is not marked **Done** in PF20 until:

1. all required acceptance tokens for that epic are listed here, and

2. each token has corresponding evidence indexed in the human Evidence Index and machine mirror in the same PR, per PF06/PF09/PF12/PF19.

##### **E. Naming normalization (planning gate)**

**Directory naming rule (normative).**

* All directory names used in Epic Plans, evidence paths, and expected artifact layouts MUST be lowercase ASCII.

**Close-pack path-of-record rule (normative).**

MUST locate the close-pack pair at the canonical audit/ paths using the `EPIC-###` pattern (3 digits):

* `audit/EPIC-###_close_report.md`

* `audit/EPIC-###_MANIFEST.json`

MUST NOT relocate these close-pack artifacts into alternative directory trees (example: `audit/qa/**`, `artifacts/**`) without an explicit canon change.

**QA evidence roots remain separate.**

* QA evidence roots (example: `audit/qa/<epic-id>/`) remain separate. Do not merge or co-locate artifact families:

* Close-pack path-of-record is the `audit/EPIC-###_*` pair above and must not be dual-homed for acceptance binding.

If legacy artifacts exist under non-canonical naming, treat them as deprecated; preserve for history, but do not create new acceptance bindings against deprecated patterns.

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

  ##### **A. Token registry validation (planning gate)**

Acceptance token names used anywhere in the plan (including acceptance artifacts and acceptance-token claims in step logs) MUST match the canonical acceptance token roster in “HDE Governance” (PF04).  
 Tokens are case-sensitive and names-only (no embedding semantics).  
 If any token name is unregistered or misspelled: do not claim it; normalize to a registered name (if applicable); record DOC\_DRIFT rather than copying the legacy string forward. Plan approval is mechanically blocked until the plan’s token set is registry-valid.

* Token sources:

  * Primary source (spellings): PF04 acceptance token roster.

  * Secondary sources: PF09 check definitions only (may reference tokens but MUST NOT mint new token names or alternate spellings).

* Deprecated alias handling (hard):

  * `QA_STEP_LOGS_CONSOLIDATED_OK` is a deprecated alias for `QA_HARNESS_DISCIPLINE_OK`.

  * All acceptance artifacts and step logs MUST claim `QA_HARNESS_DISCIPLINE_OK` (not the alias).

  * If the alias is encountered in source PF text, interpret it as `QA_HARNESS_DISCIPLINE_OK` and record DOC\_DRIFT for drain.

Token hygiene examples:

* Registry-valid: `QA_HARNESS_DISCIPLINE_OK`

* Not valid: `qa_harness_discipline_ok` (wrong case)

* Not valid in new plan text: `QA_STEP_LOGS_CONSOLIDATED_OK` (deprecated alias; use `QA_HARNESS_DISCIPLINE_OK`)  
* 

##### **B. Close-pack baseline declared (planning gate)**

* The Epic Plan MUST explicitly list the required close-pack artifacts (titles-only) for the epic close stage.

* At minimum, the close-pack baseline MUST include:

  * the epic close report, and

  * the epic manifest, and

  * the epic acceptance map, and

  * the token→evidence matrix (when required by the QA posture for that epic).

**Close-pack deterministic path-of-record (normative).**

MUST locate the close-pack pair at the canonical audit/ paths using the `EPIC-###` pattern (3 digits):

* `audit/EPIC-###_close_report.md`

* `audit/EPIC-###_MANIFEST.json`

These are baseline close-pack artifacts (required closure artifacts), not acceptance tokens.

MUST NOT relocate these artifacts into alternative directory trees (example: `audit/qa/**`, `artifacts/**`) without an explicit canon change.

**Close-pack manifest key\_outputs binding map (normative).**

`audit/EPIC-###_MANIFEST.json` MUST include `key_outputs` as a JSON object (map):

* each key is a stable pointer name (string)

* each value is a repo-relative artifact path (string)

`key_outputs` MUST NOT be a list.

Close-pack validation checks MUST validate the named bindings (keys \+ exact paths), not list membership.

**Doc-delta surfaces (required; two-surface pair; names-only baseline).**

The Epic Plan MUST declare both doc-delta surfaces (concrete filenames; no placeholders):

* Draft/staging surface (token-evidence binding surface): `audit/docdeltas/<epic-id>_doc_deltas.md` (lowercase epic-id)

* Epic-scoped capture surface (stable QA record): `audit/qa/<epic-id>/00_meta/doc_deltas.md`

Binding rule (normative): token↔evidence bindings reference the draft/staging surface; the epic-scoped capture file is the authoritative narrative/record surface.

* Epic Plans MUST NOT be considered approvable if they omit this close-pack baseline and doc-delta baseline file set for eventual epic close.

##### **C. Evidence bundle completeness for local-bundle deliverables (planning gate)**

When a deliverable claims a “local bundle” directory (example: `artifacts/ops/internal_version/*`):

* The deliverable’s “Evidence required” list MUST enumerate the complete required evidence paths (titles/paths only).

* If any required evidence lives outside the local bundle directory, the plan MUST name it explicitly and give its canonical path (titles/paths only), rather than assuming it is implicitly available.

  ##### **D. Canonical evidence-path binding validation (planning gate)**

Authority order (hard):

* Canonical artifact paths and sibling path-proof transcript naming are defined by PF12.

* PF09 defines required checks/gates but MUST bind to PF12-defined canonical paths and filenames (no alternate path strings).

* Status vocabulary for PASS/FAIL and tooling states is defined in PF19; do not invent new status strings.

* Any legacy path string encountered in other PF text is treated as DOC\_DRIFT: plans MUST bind to PF12 canonical paths and record a Doc Delta rather than copying the legacy string forward.

The Epic Plan MUST validate each named evidence pointer is bound to a canonical surface in the “HDE Schemas & Artifacts” evidence catalog (exact path string, including case).  
 Any non-canonical binding is a mechanical blocker unless it is explicitly routed via an ADR.

**Minimum required evidence pointers (stable contract):**

* Close-pack pair:

  * `audit/EPIC-###_close_report.md`

  * `audit/EPIC-###_MANIFEST.json`

* Evidence Index:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

* Machine Mirror (canonical mirror home):

  * `artifacts/evidence_index.jsonl`

  * `artifacts/evidence_index.jsonl.sha256`

  * `artifacts/evidence_index.jsonl.path_proof.txt`

* Evidence index snapshot (only if the plan includes D23):

  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

  * `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

Validator failure posture (execution-time status mapping):

* If validator can run and detects evidence exists but bindings do not match PF12 canonical paths, status is FAIL\_BEHAVIOR.

* If missing required canonical inputs (evidence does not exist or not readable), status is TOOLING\_BLOCKED.

Acceptance artifact hygiene (mechanical, plan-gate rule):

* Token names in acceptance artifacts MUST pass PF04 token registry validation; no legacy spellings or aliases.

* `audit/EPIC-###_MANIFEST.json` MUST reference canonical paths and include path-proof transcript pointers where required.

* Any path-proof transcript MUST use the canonical suffix `<artifact>.path_proof.txt`.

* The plan MUST explicitly list each path-proof transcript file that will be included in close-pack using explicit filenames such as `<ARTIFACT_NAME>.path_proof.txt` (no pattern placeholders).

Prohibited placeholders: informal stand-ins such as curly-brace placeholders or the word “TBD” (unless the word “TBD” is part of a formal decision-bounded rule as defined in the Remediation Implementation Guide template).  
 Use `<PLACEHOLDER_NAME>`, `[OMITTED]`, `[LIST CONTINUES]`, `[SNIP: <n> lines omitted]`, or `[INTENTIONALLY LEFT BLANK]`.

**Canonical JSON gates (directory binding rule; normative).**

* Canonical JSON gate artifacts MUST bind to the single family: `audit/gates/json_gate/canonical/`

* At minimum, the canonical family includes:

  * `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`

  * `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`

  * `audit/gates/json_gate/canonical/json_gate_structured_record.json`

  * plus sibling `*.path_proof.txt` files for the above, as defined by the owning canon.

* Plans and acceptance artifacts MUST NOT require, invent, or dual-home canonical JSON gate bindings across multiple families. The following are legacy/compat-only and MUST NOT be treated as canonical acceptance surfaces unless canon explicitly reinstates them (via PF12):

  * `audit/gates/canonical_json/*`  
  * `audit/gates/canonical_json/json_canonical_check.log (legacy catalog check report; compat-only; do not bind new plans to this path)`  
  * `audit/gates/canonical/*`

**Evidence index snapshot artifacts (directory binding rule; normative).**

* Canonical generator command (repo-local; copy/paste): `python tools/evidence/generate_evidence_index_snapshot.py` (not `run_evidence_index_snapshot.py`).

When an epic produces an evidence index snapshot as part of QA execution (D23 Evidence Index Snapshot):

* Canonical artifact surfaces (already governed):

  * Snapshot JSON: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

  * Snapshot path proof: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

* Snapshot JSON schema (must match exactly):

  * `schema_version` is `1`

  * `generated_at_utc` is a valid RFC3339 UTC timestamp

  * `inputs` (object):

    * `human_index_path` (string; must be `docs/evidence/INDEX.json`)

    * `human_index_sha256` (string; lowercase hex SHA256)

    * `machine_mirror_path` (string; must be `artifacts/evidence_index.jsonl`)

    * `machine_mirror_sha256` (string; lowercase hex SHA256)

  * `parity` (object):

    * `artifact_keys_match` (boolean)

* PASS predicate (mechanical; tokenless):

  * `schema_version` is `1`

  * `inputs.human_index_path` equals `docs/evidence/INDEX.json`

  * `inputs.machine_mirror_path` equals `artifacts/evidence_index.jsonl`

  * `inputs.human_index_sha256` matches SHA256(raw bytes of `docs/evidence/INDEX.json`)

  * `inputs.machine_mirror_sha256` matches SHA256(raw bytes of `artifacts/evidence_index.jsonl`)

  * `parity.artifact_keys_match` is true

* Status mapping:

  * If required canonical inputs are missing or unreadable (for example: the index or mirror does not exist at the canonical path), status is TOOLING\_BLOCKED.

  * If any predicate condition fails (schema mismatch, hash mismatch, parity false), status is FAIL\_BEHAVIOR.

* Token posture:

  * This check is tokenless. Do not claim acceptance tokens from this snapshot.

* Epic-local variants:

  * An epic may carry a non-canonical copy under `audit/qa/hde-epic<NNN>/` for convenience, but it MUST NOT be treated as a closure-required canonical surface and MUST NOT replace the canonical evidence index pair.

**Canon-defined compare artifact surfaces (current; non-exhaustive).**

* Arrays-as-sets compare report (CHECK `D05_arrays_as_sets`): `artifacts/canonical/arrays_as_sets_report.log`

* The owning check’s `primary.log` MUST (a) capture the exact command executed that produced this report (verbatim) and (b) point to the stored report artifact path above (no prose-only assertions).

* Plans MUST NOT bind acceptance to a different arrays-as-sets report path (example: `audit/gates/arrays_as_sets/arrays_as_sets_report.md`) unless introduced via ADR \+ doc-delta and drained into PF-Canon.

**Canonical compare artifacts (no epic-local paths; normative).**

* Compare evidence MUST reuse canon-defined compare artifact surfaces.

* An epic MUST NOT introduce a new compare artifact path as “the canonical compare proof” unless that path is explicitly introduced via ADR \+ doc-delta and drained into the owning PF-Canon homes.

If canon does not define a compare artifact surface for the needed proof, treat it as a canon gap and resolve it before the epic binds acceptance to a new path.

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

Ops tasks are required to capture evidence in governed paths and include path-proof transcripts where applicable.

`Evidence posture:`

`Artifacts:`

``* `audit/ops/<epic-id>/<task_id>/` — Task work products for this ops task.``

``* `audit/qa/<epic-id>/<task_id>/` — QA evidence for this ops task (only if the task produces QA evidence).``

`Path proofs:`

``* For any governed artifact path included in acceptance or close-pack, include the sibling path-proof transcript using the suffix `<artifact>.path_proof.txt`.``


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

Commands included for operator use MUST be mechanically valid in-repo and MUST NOT be dead, ambiguous, or misleading.

Where a check/tool has a single canonical invocation form demonstrated by repo/CI usage, the guide MUST use that exact form as the default command. If multiple invocation variants exist, non-default variants MUST be labeled as non-default and the default choice MUST be justified as **Observed Evidence (non-PF)**.

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
 \<EXECUTIVE\_SUMMARY\>

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

* \[LIST CONTINUES\]

**ADRs Requiring Approval (Canon and External Task Creation)**  
ADR-001 — \<short title\>

* Decision (required; canon-resolution outcome):

* Why an ADR is required (required; must not already be canonized):

* Canon issue being resolved (required; PF references):

* Drain targets (required; owning PF docs \+ intended doc delta):

* Notes / external task creation (optional):