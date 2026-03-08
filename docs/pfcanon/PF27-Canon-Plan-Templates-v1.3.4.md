# Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v1.3.4

**Status:** Canon

**Effective date:** 2026-03-07

**Last Update Gate:** BN 10.0.5 Drain 32-33

**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **Purpose & scope \[Required−Now\]**

**Purpose.**  
PF27 is the single PF home for **plan and runbook templates** used in the Glow project (including the HDE workstream). It exists to standardize **template shape**, required front matter, evidence posture, and review guards so that plan documents are executable in the PO \+ Codespaces loop and remain canon-aligned.

**Scope (in).**

**PF23 consult (epic planning \+ QA planning).**

* Reality Audits (PF23) are post-epic audits. They are updated at the end of an epic and reflect a latest closed-epic snapshot, not an in-flight PR truth source.

* PF23 consult is required during Epic planning and during QA planning that drafts, reviews, or approves a Live QA Plan.

* In these contexts, PF23 MAY be used to ground component boundaries, canonical pathnames/loci, and repo-reality context for existence or locus framing.

* Consultation is read-only; updates remain PO-only. QA plans MUST NOT mandate PF23 edits, and QA execution MUST NOT include PF23 updates as a required output.

* PF23 consult MUST NOT appear as a required deliverable, a required check, or an acceptance token in implementation plans, QA plans, reviews, or acceptance artifacts.

* Disallowed use: PF23 MUST NOT be consulted for PR analysis, including PR review, remediation review, and diff-first approval loops. PR analysis must rely on the owning PF canon homes and repo reality for the PR under review, without using PF23 as a blocker source.

* PR analysis routing: reviewers MUST rely on the owning PF homes by title (examples: HDE Architecture, HDE Governance, HDE CLI/API reference, HDE Schemas and Artifacts, HDE Build Checklist, HDE Mechanics Guide, Glow QA Guide, Epic Process Guide).

* Drift assessment trigger: if any PF23 Reality Audit statement contradicts PF canon, that contradiction MUST be treated as development drift requiring evaluation, not as an automatic correction in either direction.

* Drift assessment protocol (stub; required posture, not full process): when PF23 contradicts canon during planning:

  * Record the contradiction as a drift item in Tracked Issues with: PF23 claim (quote or precise paraphrase), the conflicting PF canon claim (quote or precise paraphrase), and the impacted epic/surface.

  * Classify the drift into exactly one bucket (tentative): canon defect, implementation drift, or necessary reality shift.

  * Do not fix by assumption, and do not treat the contradiction as resolved unless the PO explicitly adjudicates the resolution path.

  * Resolution routing is PO-owned. The PO decides whether the fix is a canon update, an implementation remediation, or a formalized exception with canon follow-up.

* Epic Plans SHOULD include a short “PF23 Anchors” subsection listing the component(s) consulted and the key pathnames/loci the plan will touch (traceability only; do not duplicate PF23).


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

 **Repository locus validation and file minting posture (hard).**

* Validated references only. Plans MUST NOT include any repository path, module home, command, or uniqueness claim (for example, “only create\_app factory”) that cannot be confirmed via canon or repo inspection.

* Every asserted file path or “where this lives” claim in a plan MUST be validated using exactly one method:

  * Canon-cited: cite the PF canon line(s) that assert the path or locus.

  * CA vetted: include a quoted repo inspection command and its output in “Observed Evidence Snapshot” (portable, attachment-free).

  * IG Approved: quote the locus from the Implementation Guide Inventory (or other IG canon section) inside the plan.

* CA vetted and IG Approved evidence MUST NOT be referenced as external attachments in downstream Codex prompts. If a plan needs the information, embed the quoted evidence in the plan and reference the plan section.

* File minting is allowed. When a plan mints new files or new evidence outputs, it MUST name the exact repository paths and filenames that will be created and the exact primary evidence files that will be produced.

* New roots and second homes are prohibited by default. Plans MUST NOT propose new top-level roots or alternate/duplicate locations for existing artifacts unless an ADR explicitly authorizes the new home and the PO approves the change.

* Evidence is intentionally multi-root across established governed roots. Plans MUST NOT treat multi-root as drift by default. “Single-home” in evidence terms means a single authoritative catalog or index plus canonical path bindings (titles-only: PF12 — HDE-Schemas and Artifacts), not a single directory root.  
* Dual-home patterns are allowed only within established governed roots and only when one path is explicitly declared as the source of truth and the other path is explicitly declared as a pointer or index.  
* Source-of-truth artifacts are the governed catalogs, manifests, ledgers, and evidence bundles that bind acceptance to canonical paths. Documentation pointers (for example: link lists, summary indices, or anchor files) MAY exist in other roots, but MUST only point to the source-of-truth artifact and MUST NOT be treated as an independent truth home for acceptance.  
* When a plan relies on a dual-home pattern, it MUST state:  
  * both paths,

  * which path is authoritative (source of truth),

  * which path is pointer-only,

  * and the refresh rule that keeps the pointer or index consistent with the authoritative artifact.  
* Classification note: if a plan treats additional roots as governed evidence (for example, `scripts/` or `tools/`), the plan MUST either (a) bind them to an evidence family cataloged in PF12 — HDE-Schemas and Artifacts, or (b) treat them as non-governed tooling output and exclude them from acceptance and any “truth home” claims.

* Evidence output naming: plans must avoid wildcard or implied file path patterns and must state concrete filenames for primary governed evidence outputs. For high-churn logs, provide a manifest file path and a bundling rule that yields a stable evidence bundle.

* Example (architecture audit incident): do not assume a new top-level `src/` root. If a plan claims a new root, it must be validated. In EPIC025 audits, HTTP adapter code was asserted to live under `adapter/` as the single home, and `src/` claims were treated as drift until proven.

Template-safe placeholders and ellipsis prohibition (hard).

Allowed placeholder markers: \[REQUIRED\], \[REQUIRED−NOW\], \[OPTIONAL\], \<PLACEHOLDER\>, \<PLACEHOLDER\_ONE\_PER\_LINE\>.

Prohibited placeholder styles: plain TBD, TODO, ???, FIXME, or free-text “fill in later”.

Prohibited characters and sequences (outside code spans where the token is part of literal code under discussion):

the Unicode ellipsis character (U+2026),

any sequence of three consecutive period characters outside code spans,

fenced code blocks (triple-backtick fences).

Mandatory truncation response (NO OUTS): if an ellipsis token (or three-period sequence used as an omission signal) appears in any relied-on passage:

treat the passage as potentially incomplete,

re-open or re-retrieve the source until the full, uncut text is visible, and

redo any dependent work after full retrieval.

If the token can be proven to be present in the true source text (not a viewer artifact), it MUST be removed and replaced with an approved omission marker.

Approved replacements (standard placeholders). When omission or continuity must be expressed, use only:

\[OMITTED\]

\[OMITTED: short reason\]

\[SNIP: n lines omitted\]

\[LIST CONTINUES\]

\[REPEAT BLOCK\]

Code spans exception (narrow): ellipses may appear inside code spans only when they are part of literal code under discussion. Even then, reviewers MUST prefer rewriting examples to avoid ellipses where possible. If a literal code example would require ellipses and cannot be rewritten safely, move the snippet into a repo source file or governed evidence artifact and reference it by path (do not embed the ellipsis in the plan text).

Mechanical blocker posture: any prohibited ellipsis or any fenced code block in planning or QA documents is a mechanical blocker until removed, because it is indistinguishable from viewer truncation and degrades auditability.

\[TBD\] is prohibited unless it is explicitly decision-bounded and appears only inside the Remediation Implementation Guide template under “Open Decisions.”

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

**Planning-time consult for Live QA planning (normative).**

* PF23 MUST be consulted during QA planning. Drafting, reviewing, or approving a Live QA Plan MUST consult PF23 as a primary input for repo-reality context and existence or locus framing.

* If a plan references any repo-resident locus (paths, endpoints, routes, scripts, checks, test identifiers, environment variable names treated as already-existing, or fixed output locations treated as already-existing), the reviewer SHOULD consult PF23 before approval to reduce drift and avoid fabricated or stale locus assumptions.

* Consultation is read-only. PF23 maintenance remains a manual PO operation. Live QA Plans MUST NOT include any required deliverable whose purpose is “PF23 consult capture,” “PF23 note,” or similar.

* Live QA Plans MUST NOT instruct the operator to run repo commands in order to “prove PF23 consult.”

* Conflict posture: if PF23’s current record appears inconsistent with other allowed repo-reality sources, treat this as a reality ambiguity and MUST NOT guess or assert a reconciled locus as fact inside the plan.

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

  #### **Check-centric, single-root evidence posture (normative)**

This runbook is written for the checks-only evidence posture:

* Live QA evidence MUST be organized only by **check\_id** under EPIC\_QA\_ROOT as **current-state evidence**.

* Evidence paths MUST be stable across re-runs. Re-running QA MUST NOT change the directory structure by creating a new run root.

* Per-run directory nesting is disallowed. Run-id directories, timestamped directories, and fresh-directory postures are nonconforming.

* Plans, prompts, and reviews MUST NOT introduce, require, or depend on per-run root selection or any operator-set per-run root variable.

* Plan-created deliverables are allowed, but they MUST live under the stable check directory for the relevant **check\_id**. Plans MUST NOT place plan-created outputs under a per-run directory.

* No “latest\_run\_id” pointer files or “run-id as correctness key.”

* Uppercase characters are allowed in filenames. The lowercase naming rail applies to directory segments and to explicitly-lowercase identifiers (for example, `check_id`).

* `run_id` (or `RUN_ID`) is prohibited as an operator input, plan header field, step-log header field, manifest field, or correctness key. If per-execution history is kept, it remains optional and non-canon and MUST NOT introduce a run-id identity requirement.

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

* `schema_version`: the canonical schema label for this header (example: `pf27.step_log_header.v1`).

* `timestamp_utc`: ISO-8601 UTC timestamp with a `Z`suffix.

* `check_id`: string identifier (matches the Check Block ID).

* `check_name`: string identifier (matches the Check Block name).

* `status`: one of `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `SKIPPED`, `WARN`.

* `fail_status`: MUST be `""`when `status`is `PASS`, else MUST equal `status`.

* `command`: the exact command line executed for this check step (the actual string, not a paraphrase). If multiple commands were executed, `command`MUST be an explicit pipeline or an explicit `;`\-joined sequence that preserves the execution order.

* `command_provenance`: one of `Codex prompt`, `Copy/paste from plan`, or `Explicitly created`.

* evidence\_artifacts: array of one or more paths to evidence artifacts produced for this check (example: the check's `primary.log` path).

* Invariant (PASS): `evidence_artifacts` MUST include the check's `primary.log` path. If a PASS step omits `primary.log` from the artifacts list or manifest, it is an evidence hygiene defect and the step MUST NOT be closed as PASS until remediated.

* captured\_env: JSON object containing the actual env vars for the run (not inferred), limited to canon-defined names.

* `pf_refs`: array of PF document titles consulted (titles-only).

* `intended_tokens`: array of intended acceptance tokens (may be empty).

* `claimed_tokens`: array of claimed acceptance tokens (may be empty).

Notes:

* Step templates MUST generate the header via the canonical header-writer snippet below (or a repo-defined canonical helper that emits the same keys).

* `captured_env`MUST include only canon-defined env var names. Environment variable names are governed interface surfaces (like repo loci and CLI surfaces) and MUST NOT be invented ad hoc for QA convenience.

  * Mechanical blocker: any `MODO_*`environment variables are non-canonical and MUST NOT appear as plan inputs, required exports, required schema keys, or required step-log capture keys.

  * No QA-time env var minting: if a QA plan, runbook, or tool would require a new env var name, that is a development change that requires PO approval and canon documentation before any QA plan can rely on it.

  * Grandfathered exception (HDE-EPIC025 only): `MODO_*`references in the already-approved EPIC025 plan are inert placeholders and MUST NOT be treated as required inputs or copied into new plans.

* `command_provenance`MUST reflect how the exact `command`string was obtained. The plan may provide a directive or a suggested command, but the step log MUST record the exact command(s) executed.

* `pf_refs`MUST contain titles only (no versions).

* Authors MUST NOT add novel env vars or CLI switches to plans or execution artifacts for convenience. Any env var name (and its semantics) is a governed interface surface and can only be introduced via a documented canonical change.

**Canonical step-log header writer (paste-ready; emits header JSON with all required keys):**

This writes a single-line JSON header to stdout. Paste it into `primary.log`as the first line.

The `python - <<`form is part of canon. Do not replace it with `python file.py`.

The plan MUST export the required header-writer inputs for each check immediately before header generation. Do not rely on prior step state.

Anti-drift: a Live QA Plan MUST use one header-writer contract consistently across check blocks (do not mix patterns).

Minimum per-check exports (names must match the header writer contract):

* `CHECK_ID`

* `CHECK_NAME`

* `PASS_FAIL`

* `COMMANDS_JSON`(JSON array of exact command string(s) executed, in order)

* `ARTIFACTS_JSON`(JSON array of evidence artifact paths)

* `PF_REFS_JSON`(JSON array of PF titles)

Optional exports:

* `COMMAND_PROVENANCE`(defaults to `Explicitly created`)

* `INTENDED_TOKENS_JSON`(JSON array)

* `CLAIMED_TOKENS_JSON`(JSON array)

If a header is missing or incorrect due to missing exports, a minimal Moon Loop deviation is allowed to export the missing inputs and regenerate the header. Evidence-capture-only correction MUST reassemble `primary.log`by prepending the corrected JSON header while preserving the existing body verbatim.

`python - << 'PY'`  
 `import datetime`  
 `import json`  
 `import os`  
 `` `def env(name: str, default: str = "") -> str:` ` value = os.environ.get(name)` ` return value if value is not None else default` ``  
 `def env_json(name: str, default):`  
 `raw = os.environ.get(name)`  
 `if raw is None or raw == "":`  
 `return default`  
 `return json.loads(raw)`  
 `` `schema_version = "pf27.step_log_header.v1"` `timestamp_utc = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"` ``  
 `status = env("PASS_FAIL")`  
 `fail_status = "" if status == "PASS" else status`  
 `commands = env_json("COMMANDS_JSON", [])`  
 `if isinstance(commands, str):`  
 `commands = [commands]`  
 `command = "; ".join(commands) if commands else "N/A"`  
 `` `header = {` ` "schema_version": schema_version,` ` "timestamp_utc": timestamp_utc,` ` "check_id": env("CHECK_ID"),` ` "check_name": env("CHECK_NAME"),` ` "status": status,` ` "fail_status": fail_status,` ` "command": command,` ` "command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),` ` "evidence_artifacts": env_json("ARTIFACTS_JSON", []),` ` "captured_env": {` ` "SAFE_MODE": env("SAFE_MODE"),` ` "ALLOW_NETWORK": env("ALLOW_NETWORK"),` ` "APP_ENV": env("APP_ENV"),` ` "LC_ALL": env("LC_ALL"),` ` "LANG": env("LANG"),` ` "TZ": env("TZ"),` ` },` ` "pf_refs": env_json("PF_REFS_JSON", []),` ` "intended_tokens": env_json("INTENDED_TOKENS_JSON", []),` ` "claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),` `}` ``  
 `print(json.dumps(header, ensure_ascii=False))`  
 `PY`

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
* If a plan-listed mismatch is wording-only inside the same check (for example, a PASS/FAIL bullet names a different target than the check title, intent, or inputs) but the intended target remains unambiguous and the evidence proves that intended target, treat it as a **CAVEAT** (not a **BLOCKER**). Record expected → actual wording and do not silently rewrite the predicate after execution.  
* Evidence hygiene follow-ups that are not plan-required deliverables (for example, path-proof refreshes, Evidence Index entry additions) MUST be recorded as **CAVEATS** / follow-ups and MUST NOT be treated as blockers unless explicitly made plan-required.  
* Exception: If a change updates governed artifact bytes and any required integrity sidecars (checksum manifests or path-proof transcripts) become stale or missing, treat the missing sidecar refresh as a **BLOCKER** until regenerated and verified. If the governed artifact is mirrored in multiple canonical loci, sidecar refresh MUST be performed for each locus.

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

#### **Token coverage and evidence binding (required)**

* Every check block in §2.2.3.A MUST satisfy exactly one of the following:

  * Token-attached check: `intended_tokens` contains one or more acceptance tokens, and the check’s PASS predicate produces evidence sufficient to claim some or all of those tokens in `claimed_tokens`.

  * Tokenless evidence check: `intended_tokens` and `claimed_tokens` are empty, and the check is explicitly justified as a non-token evidence requirement with an explicit PASS predicate and captured artifact.

* A Live QA Plan MUST NOT include any step or check that is neither token-attached nor an explicit non-token evidence requirement. No “for good measure” checks are allowed.

* Token coverage requirement: every acceptance token in the epic’s acceptance roster MUST appear in `intended_tokens` of at least one check block in this Live QA Plan.  
* Functional proof requirement (when functional changes exist): the Live QA Plan MUST include at least one named functional proof check per functional seam touched by the epic (including vendor seams where applicable). A functional proof check MUST exercise the runtime path and capture an observable result in evidence (not only static artifact checks).  
  * If the change set is purely non-functional (for example: docs-only or formatting-only), this requirement does not apply.  
  * When in doubt, include at least one minimal functional proof check and keep its rails and proof outputs explicit.

* If a check implements a PF19 standard playbook, the check block MUST cite the playbook (PF19 section or heading) in its `PF_anchors` and MUST follow the playbook steps without ad-hoc rewrites.

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

**Reader proof-surface lint (canonical routes and proof selection; addenda-driven; locked)**

* Canonical Reader route is `GET /reader`.

* Reader v1 is selected via `v=1` query parameter on the Reader route (not a distinct path).

* `/api/reader` may exist only as an environment-specific mount alias when the service is mounted under an `/api` prefix; it is not a separate contract surface.

* Forbidden invented route: `/api/reader-proof/v1` MUST NOT be referenced in plans, runbooks, or endpoint catalogs. Treat any occurrence as DOC\_DRIFT and correct the proof route selection to a real mounted surface before evaluating the check predicate.

* Aux narrative surfaces (example: `/aux/narrative`) are separate from Reader and MUST NOT be substituted for Reader proof unless the check explicitly targets Aux narrative.

* Proof-surface selection posture: choose the proof route from known mounted surfaces (or from an Endpoint Catalog entry that is itself sourced from real mounted surfaces). Do not invent “proof routes.”

#### **CHECK \<check\_id\>: \<check\_name\>**

Surface / D-goal mapping: \<D\# \+ surface\>  
 Rails: SAFE\_MODE=\<value\> ALLOW\_NETWORK=\<value\> APP\_ENV=\<value\>  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PFxx — Title, §XY (titles-only)

Vendor-dependent steps (rails-scoped):

* If the step requires vendor IO (example: `showcompat` when the required BodyGraph bytes are not already locally available), set rails for this step only (typically `ALLOW_NETWORK=1`) and restore the default rails posture immediately after the step.

* Rails posture mismatch is a plan defect: if the plan declares SAFE rails for this step (example: `ALLOW_NETWORK=0`) but execution requires network or vendor IO in practice, the plan MUST be corrected before declaring it stable. The plan MUST either (a) scope the step to allow network for this step (example: `ALLOW_NETWORK=1`), or (b) provide an offline proof mode that can execute with `ALLOW_NETWORK=0`.

* `showcompat` MUST NOT be executed as a zero-argument command. The invocation MUST supply the required argument set defined by HDE-CLI-API-Vendor-Ref.

* If an `showcompat` attempt fails only because rails were closed or required args were missing, classify this step as `FAIL_TOOLING`or `TOOLING_BLOCKED`(not `FAIL_BEHAVIOR`) and record the rails posture used plus the failure signature in the step log.

**Intent (required)**

* State what this check must locate, verify, or prove.

**Discovery step (required only when needed)**

* If any repo-resident locus needed by this check is not proven at planning time, treat it as unknown until discovered during the run.

* The plan MUST prefer real-time discovery and observation over pre-specifying implementation guesses.

* Unknown loci MUST be handled by a discovery step, not by placeholders.

* State the discovery intent: what must be located or verified to exist.

* State the discovery acceptance: what constitutes sufficient proof that the locus exists and is the correct target.

* Require recording the discovered locus string verbatim into the check evidence before using it.

**PO command(s) (minimal; objective-first)**

* Describe the goal of the action, the observable outputs that matter, and the evidence that must be captured.

* Live QA Plans MUST NOT over-specify command lines.

* The executor MUST record the exact command(s) actually used into the check evidence at runtime.

* If the plan includes an exact command string, it MUST be proven by an allowed provenance source.

**Expected result (PASS/FAIL predicates)**

PASS if:

* \<predicate 1\>

* \<predicate 2\>

FAIL\_BEHAVIOR if:

* \<observed behavior contradicts PASS criteria\>

FAIL\_TOOLING if:

* \<tool invocation failure or non-zero RC attributable to tooling\>

TOOLING\_BLOCKED if:

* \<discovery cannot proceed without guessing, or a required input, file, binary, or prerequisite is missing\>  
* If a required input is not a valid product input for the current run, or is explicitly not expected for the current run, classify the step as `TOOLING_BLOCKED` and treat it as an input-availability gate and planning defect, not as `FAIL_BEHAVIOR`.

* Missing artifacts behind that blocked gate are expected blocked outputs, not missing-evidence failures for the current run.

* A re-run is actionable only when the required product input becomes valid or available. Until then, record the blockage mechanically and do not label it as remediable evidence loss.

**Primary evidence artifact (required)**

Canonical (current-state) primary log:

* `audit/qa/<epic-id>/checks/<check_id>/primary.log`  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json` (Canon-defined | Required) — QA-created current-state manifest; MUST include an entry per executed check recording at minimum `check\_id`, `status`, and `log\_path` (additional cryptographic metadata allowed). TOOLING\_BLOCKED steps MUST still be listed (do not omit posture-only checks).  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` (Canon-defined | Required) — QA-created sibling path proof for the manifest (generate after manifest updates).

One-line description:

* “Header (command \+ captured\_env \+ status) \+ transcript \+ grep/diff outputs \+ PASS/FAIL predicates.”

 **Deliverables (minimal evidence set; fully-qualified paths)**

List only what is required to judge this check.

Conditional deliverables (when applicable):

* If a deliverable exists only when a stated condition is met, the plan MUST place it under a clearly labeled conditional subsection and state the exact condition.

* Conditional deliverables are not required for the current run when the condition is unmet. They MUST NOT be listed as unconditional must-exist evidence for PASS or FAIL adjudication.

* When the condition is unmet, the check evidence MUST record the unmet condition and the reason the conditional outputs were not produced.

Path provenance and locus provenance lock (required; per required path or repo-resident locus):

* Allowed provenance sources for repo-reality claims are exclusive:

  * PF10 — HDE Build Notes

  * PF-Canon

  * the initial QA Audit for the epic

* This lock applies to any repo-resident or repo-reality string, including:

  * file paths and directory paths

  * endpoint names and routes

  * module and component identifiers

  * script names, runbook names, and command strings

  * check and test identifiers and CI job names

  * environment variable names when treated as already-existing

  * fixed output locations when treated as already-existing

  * negative existence claims

* Repo-resident locus strings MUST be copied verbatim character-for-character from an allowed provenance source. No invention, no inference, no memory fill-ins, no renaming, no case folding, no wildcard expansion, and no invented variants.

* The plan MUST NOT list any required path or repo-resident locus that is neither Canon-defined, Audit-proven, nor QA-created.

* Any Live QA Plan that contains a repo-resident locus string not proven verbatim by an allowed provenance source is invalid for approval and MUST be returned for revision.

* (Canon-defined) — the path or locus is copied verbatim from PF10 or PF-Canon.

* (Audit-proven) — the path or locus is copied verbatim from the initial QA Audit for the epic.

* (QA-created) — this runbook step will create the path during execution.

Rules (normative):

* If a required path is QA-created, the owning Check Block MUST include:

  * the exact repo-relative path and filename,

  * explicit runnable creation instructions that produce the file at that path, creating parent directories if needed,

  * one sentence stating why the file is created and what proof obligation or deliverable posture it satisfies,

  * PASS/FAIL predicates that validate the created bytes mechanically.

* Creation instructions MUST be sufficient to reproduce the file deterministically and unambiguously when the file is evidence-bearing or required.

* The plan SHOULD label each mentioned file path as repo-resident versus plan-created. Missing labels are non-blocking only when the file is clearly a run-produced deliverable and the plan provides the required path, how, and why.

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
* if a Live QA Plan exists/was used, includes explicit Coverage vs QA Plan accounting that is complete, step-by-step, and auditable. This accounting MUST:  
  * list every QA Plan step in plan order using the stable step identifier from the plan,

  * identify the coverage status for each step,

  * and, for each COVERED step, point to the evidence artifact(s) produced under the governed QA root for the epic.  
  * A planned step MUST NOT be treated as PASS or COVERED unless it has at least one step-scoped evidence pointer under the governed QA root for that same step.

  * If a step record is mislabeled, contaminated with another step’s content, or otherwise fails to preserve stable step identity, that step MUST NOT be treated as PASS until corrected or re-evidenced.

  * Coverage status MAY use `BLOCKED/UNEXECUTABLE` when a planned step could not be executed. When this status is used, the closeout record MUST include:  
    * the blocking precondition,

    * why it could not be satisfied,

    * whether it is a blocker for closeout,

    * and the required follow-up (`plan change` or `implementation change`).  
* any uncovered, blocked, or unauditable step MUST be called out explicitly with the reason (no silent drops, no inference).

* if token claims are part of the closeout posture, the summary MUST reject any token pass that is not paired with a concrete evidence pointer under the governed QA root. Where a token→evidence matrix is required by the QA posture, each claimed token MUST have an auditable matrix row.

* summarizes remediation actions (including any Moon Loop work) as: what changed, why, which check(s) were unblocked / re-verified, where the supporting evidence lives (diff/log paths), and the remediation loop evidence triple:  
  * failure signature,  
  * remediation note,  
  * rerun output.  
  * For document-structure remediation (for example: mislabeled step IDs, contaminated sections, or broken evidence-pointer alignment), the same remediation loop evidence triple MUST be preserved:  
    * failure signature \= the incorrect snippet,  
    * remediation note \= the correction rationale,  
    * rerun output \= post-fix verification output proving headings, step identifiers, and evidence pointers align.  
* enumerates known open issues and deferred work with disposition (waive / defer / follow-up) and the evidence impact.

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

## **Review guardrails**

### **Hard blockers for plan approval/execution**

* All inputs, loci, and paths MUST be explicit and reproducible. Any required executable locus (script, check entrypoint, endpoint/route, or command) that is not canon-defined or audit-proven is blocked. No fabricated loci.

* Structural template completeness is gating. Missing required sections or required structural blocks (including required end markers and required gates) is blocking. Where a template requires canon pointers (for example PF09 or PF14 pointers), missing pointers are blocking. Invalid non-PF references and ungrounded existence claims are blocking.

* Plans MAY consult PF documents during planning and review, but MUST NOT mandate PF document updates as plan deliverables, acceptance criteria, or completion criteria. Reality Audits updates are PO-only. Plans MAY note doc delta candidates as explicitly non-mandatory follow-up intents for PO.

* How plans MUST express reality or existence confirmation: cite a PF clause (titles-only) when PF already establishes the claim, or capture repo-local evidence for the current run under `audit/` when PF is silent. Do not treat an intended PF update as substitute evidence.

* No interactive steps. The plan must be runnable headlessly (and must log all commands).  
* Prompt-family separation (mode boundary; required):  
  * Every QA prompt MUST declare its mode as one of: `AUTHORING` or `REVIEW`.

  * The agent MUST output only the declared mode’s required structure.

  * If mode is `REVIEW`, the agent MUST NOT produce new runbooks or new commands.

  * Review-mode remediation exception: if a command must be suggested, it MUST be copied verbatim from the approved plan and include the plan’s caveats.  
* Workflow recommendation (non-canon; strongly advised): enforce mode with a mechanical gate (mode header token plus a required section list). If the required sections do not match the declared mode, fail fast.

* Command entrypoints must resolve. Any command that references a repo-resident script or file by path MUST point to an existing repo file at review time, unless the path is explicitly declared as QA-created by this plan.

* Live QA Plans MUST NOT invent or assume helper scripts exist.

* Plan-created scripts are permitted only when a required deliverable cannot be produced without one. When a plan requires a plan-created script, it MUST:  
  * name the exact repo-relative path and filename where it will be created,

  * include runnable creation instructions,

  * state why the script is required,

  * keep the script minimal and purpose-bound to the deliverable.  
* If the step is executed via an embedded harness function (no standalone script exists), the plan MUST cite the harness runner repo path when proven, or handle the runner locus via a discovery step that records the discovered locus verbatim before use.

* New recurring artifact families/paths introduced ad hoc in a plan (not already governed by PF10) are blocked until introduced via PF10 addendum.

* The following patterns are vetoed and invalidate approval:  
  * inferred or speculative repo-resident loci,

  * placeholder routes, file paths, module names, or command strings used as scaffolding,

  * any statement that implies app topology certainty without proof.  
* A Live QA Plan that includes invented scripts, speculative app topology claims, or over-specified unproven command lines MUST be returned for revision.

* All evidence artifacts must be under `audit/` and be hashed or proven as required.  
* Epic Implementation Plans and Implementation Guides MUST NOT require the production of extensive QA evidence artifacts (for example step logs, harness outputs, artifact inventories, close-pack bundles) as part of their own required deliverables or completion criteria.

* QA planning is a separate deliverable. QA execution evidence and PASS/FAIL verdicts belong only in QA-run artifacts and closure records.

* Ops tasks are not QA tasks. Ops evidence is not a substitute for QA evidence.

* Separation rule (no category mixing): keep these categories distinct:  
  * implementation work and PR deliverables  
  * ops tasks  
  * QA planning  
  * QA execution evidence and verdicts  
* Future-step artifacts and deferrals (template semantics; required):  
  * Any plan template that enumerates step-scoped evidence paths MUST label future-step artifacts as `NOT RUN` or `DEFERRED` until the producing step has executed.

  * `NOT RUN` / `DEFERRED` MUST NOT be treated as a missing-evidence failure.

  * Missing-evidence is reserved for cases where the producing step has executed and the artifact it should emit is absent or unproven.

  * Closure and rollup steps MUST separate these states explicitly:  
    * `PRESENT`: the producing step has executed and the artifact exists and is referenced by path.

    * `MISSING`: the producing step has executed and the artifact is absent or unproven.

    * `NOT RUN` / `DEFERRED`: the producing step has not executed yet, so no artifact is expected yet.

* `/tmp` helper scripts MUST NOT print or persist secrets.

 **ADR discipline (canon-resolution only; drain targets required):**

* If canon already speaks on a topic, do not write an ADR. Cite the owning PF(s) and remove any ADR placeholder/stub.

* Any ADR included in a Plan or Remediation MUST represent a canon resolution decision (what ambiguity/conflict is resolved, and what decision is taken).

* Every ADR MUST declare explicit drain targets (owning PF docs \+ intended doc-delta updates required to canonize the decision).

* ADRs MUST NOT cite PF20 as a source of requirements, rails, acceptance semantics, or evidence-surface definitions (PF20 is historical-only).

**QoS escalation stop-rule (iteration churn; required):**

* If more than 3 plan↔evidence mismatches occur in a single epic QA run, QA MUST pause execution and repair the plan or template layer before continuing. Continuing without repair is treated as a process defect.

* A plan↔evidence mismatch is a structural remediation required to make plan claims match produced evidence (example: correcting rails posture declarations, or moving future-step artifacts out of required primary evidence pointers for the current run).

* If an epic QA plan requires repeated structural remediation for the same failure mode, escalate from incremental plan edits to systems RCA \+ template or Canon drain.

* Canon drain MUST target the class of failure, not only the incident.

* When escalation is triggered, record the rationale and intended drains in the plan’s QA RCA & Doc Delta summary deliverable.

* Drain targets (titles-only): PF10 and PF27.

* If a plan validity lint exists, extend it to detect the failure mode and fail fast (example: fail artifact generation when a PASS step does not list its `primary.log` in the artifacts list or manifest).

KISS evidence posture for Live QA (normative):

* Live QA Plans MUST minimize required outputs to:

  * one primary step log per check under `audit/qa/<epic-id>/checks/<check_id>/primary.log`, and

  * the step-logs manifest listing check IDs, status, and log paths (current-state, not per-run history).

* Prefer “validate existing canon evidence” over “produce new QA artifacts”:

  * If PF10/PF-canon already establishes an artifact family/path, the QA plan validates it (exists \+ minimal posture checks) and records PASS/FAIL in the check’s primary.log.

  * QA creates new artifacts only when the check is specifically about QA-run outputs (step logs, manifest) or when canon explicitly requires a generated QA artifact family/path.

* Any additional required artifact must be explicitly justified as acceptance-decisive and must be canonized (and path-pinned) by PF10 or PF-canon as a governed evidence family/path.

Explicit non-blockers (do not gate approval):

* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.  
* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.

* Template adherence is structural only. Reviewers evaluate whether required sections and required structural blocks are present. Header styling, heading levels, and indentation are not part of structural adherence.

* Header-format-only redlines are nits and MUST NOT be requested as approval conditions, including changes that only:  
  * switch between bold labels and Markdown headings  
  * adjust heading levels or heading capitalization  
  * restyle bullets or numbering  
  * change indentation, spacing, or cosmetic line wrapping

* Copy/paste perfection MUST NOT be an approval gate. If a plan is executable, copy/paste safe, and meets evidence posture, it is acceptable. Whitespace-only issues (indentation, alignment, wrapping) and minor quoting defects in embedded snippets are non-blocking if command identity and loci are unambiguous. If a formatting defect makes command identity or loci ambiguous, it is gating. During execution, run the semantically correct command and capture it in step log header for that step.

* Command syntax latitude: approval binds to command identity and bounded proof outputs, not to exact shell syntax. JSON-carrying environment variable assignments are treated as intent carriers; do not reject solely on whitespace or quoting style. Plans MAY define plan-level Command Snippets once and reference them by local IDs, provided each executed step log records the resolved command. This latitude MUST NOT be used to accept invented commands or unproven loci.

* Markdown sanitation rule (analysis-only): when quoting a plan for review notes, remove only presentation escapes that exist solely for Markdown rendering. Do not remove semantic escapes used by shell, JSON, regex, or paths, and do not rewrite commands based on sanitized excerpts.

* Optional environment snapshots may be omitted if the plan otherwise references stable loci.

* Minor formatting artifacts are non-blocking if semantic meaning is preserved, and must be treated as nits (they must not change the binary approval outcome). Examples include escaped Markdown list markers, backslashes inserted for rendering, cosmetic whitespace differences, bold/italic marker differences, and bullet style differences. If formatting changes meaning or introduces ambiguity (commands, expected outputs, file paths, loci, artifact names, evidence roots, portability constraints, required structural markers, quoted carryover blocks), it is not minor and may be gating.

* Headings and levels need not match a reviewer’s preferences; only required headings and required template blocks are gating.

* A plan MAY cite upstream scripts or previously-approved plan steps (for example, reused remediation steps), provided it cites exact repo paths and captures the necessary evidence outputs under `audit/`.

* Reviewers MUST NOT request changes solely to make a plan easier for LLM parsing. If a change is requested, it must be justified by execution safety, evidence posture, canon alignment, or mechanical paste safety requirements, and should be the smallest viable edit.

Caveats (allowed, must be mechanically logged):

* DOC\_DRIFT — plan adapts to repo reality; record mismatch mechanically and drain later.

* ENV\_DRIFT — environment differs from baseline; capture mechanically; do not invent new rails.

* UNREGISTERED\_TOKEN — registry mismatch is evidenced mechanically (validator output); do not maintain narrative lists.

### **QA planning QoS guardrails — templates, deferred steps, and prompt-family separation**

**Status:** Addendum (process fix)

These guardrails exist to prevent high-iteration QA loops driven by template mismatch and false missing-evidence outcomes.

#### **Template semantics: future-step artifacts**

Plans and "normative" closure templates can enumerate artifacts for steps that have not executed yet. When a plan template enumerates step-scoped evidence paths, it MUST explicitly label future-step artifacts as `NOT RUN` (or `DEFERRED`) until the producing step has executed.

Rules:

* Plans/templates may list deferred-step artifacts only under an explicitly labeled `Deferred/Not Run` section. Deferred-step artifacts MUST NOT be presented as required primary evidence paths for the current run.  
* `NOT RUN` / `DEFERRED` is not a missing-evidence failure.

* Missing-evidence failures are reserved for cases where the producing step executed but the artifact is absent or unproven.

Closure and rollup steps MUST separate these states clearly for any listed artifact paths:

* PRESENT

* MISSING

* NOT RUN / DEFERRED

#### **Prompt-family separation: AUTHORING vs REVIEW modes for QA prompts**

Every QA prompt MUST declare a mode: `AUTHORING` or `REVIEW`.

* In `AUTHORING` mode, prompts may generate or revise plans, runbooks, and command sequences.

* In `REVIEW` mode, prompts MUST be restricted to evidence review and verdict outputs. In `REVIEW` mode, prompts MUST NOT instruct the agent to create new runbooks or new command sequences, except when issuing remediation in `REVIEW` mode (commands copied verbatim from the plan and its caveats).

* The agent MUST output only the required structure for the declared mode.

Workflow and harness recommendation (non-canon, strongly advised):

* Enforce mode with a mechanical gate (a header token and required section list). If required sections do not match the declared mode, fail fast.

#### **QoS stop-rule: iteration churn escalation**

If a QA plan or closure record exhibits repeated structural remediation for the same failure mode (for example, templates listing future-step artifacts as required now, or producer-step and artifact mismatch), escalate from incremental plan edits to a systems RCA plus a template and canon drain.

The drain MUST target the class of failure (template semantics, artifact map source-of-truth, prompt-family separation), not the individual incident.

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

#### **Business Case (MUST)**

The Business Case MUST describe the practical goals of the epic in Glow product terms (not internal library terms).

Minimum required contents:

* **Problem statement:** who is experiencing the problem and why it matters.

* **Proposed change:** what capability is being introduced or changed and the intended effect.

* **Value/impact:** user value, internal value, and/or risk reduction.

* **Why now:** trigger or urgency (why this is being worked on now).

* **What success looks like:** measurable outcomes where possible, or clear qualitative criteria when not.

* **Scope boundaries:** explicit statement of what is out of scope.

* **Non-goals:** list 1–5 concrete items that are specifically not being pursued in this epic.

* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Plan.

Review posture:

* Missing Business Case (or a Business Case that is purely a technical task list) is blocking and MUST be returned for revision.

#### **Contract and Compatibility Posture (MUST)**

Every Epic Plan MUST include this section. If there are no contract changes, no new surfaces, and no new flags, explicitly state that posture (for example: "No change" or "None") and still complete the backward-compat posture.

Prompts:

* **Contract changes / new surfaces:** Identify any new or changed contracts, surfaces, or externally visible behaviors introduced by this epic.

* **Justification:** For each contract/surface change, explain why it is necessary to achieve the Business Case.

* **Flag strategy (if applicable):**

  * If introducing a new flag: explain why a new flag is required instead of reusing an existing surface.

  * If reusing an existing surface: explain why reuse is safe and preferred (and what safeguards apply).

* **Backward-compat posture:** State what remains unchanged by default, what changes for existing users, and any rollout or migration posture needed to avoid accidental breaking changes.

Review posture:

* Missing Contract and Compatibility Posture is blocking and MUST be returned for revision.

* A "verified later" placeholder is not acceptable for backward-compat posture. If the epic cannot state it yet, the plan MUST be revised before execution.

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
* Canonical tokens only for acceptance. Epic Plans and QA plans MUST express acceptance criteria using canonical token names (from PF04 — HDE Governance, or PF10 if newly minted). Plans MUST NOT use freeform acceptance statements, and MUST NOT invent local terms or aliases.  
* Names-only. Token lists in these templates are pointers to canon; plans MUST NOT redefine token semantics, strength, or pass conditions inside plan text.  
* Canon sources for token claims. A token MAY be listed in `claimed_tokens` only if it exists verbatim in PF04 or PF10.  
* Epic Plan token inventory (required): Epic Plans MUST include a Token Inventory subsection that lists every acceptance token referenced by the epic and confirms each token exists in PF04 or PF10 with exact canonical spelling (and cites the PF anchor for each).  
* No plan-local minting. If an acceptance requirement is not represented by an existing token, record it as a non-token obligation (commands, artifacts, PASS predicate), and route token creation through ADR \+ conflict check \+ Governance Doc-Delta before any plan can claim it as an acceptance token.  
* Token minting workflow (planning gate):  
  * Open an ADR proposing the token and its meaning (owner: PO), including a conflict check against PF04.  
  * Open an ADR proposing the token and its meaning (owner: PO), including a conflict check against PF04.  
  * Only after minting may downstream plans claim the token by name.  
* Token spelling reconciliation. Token spellings in all plans MUST match the Governance registry exactly. If a legacy string appears, treat it as DOC\_DRIFT and normalize before claiming.  
* Known legacy token spellings (normalize; do not claim these legacy strings as acceptance tokens):  
  * CLI\_READER\_EMITTER\_PARITY\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_READER\_EMITTER\_STACK\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * TOKEN\_CLI\_CONFORMANCE\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_READER\_EMITTER\_PROBE\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_READER\_EMITTER\_PROXY\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_READER\_EMITTER\_CODEC\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_READER\_EMITTER\_FORMAT\_OK → CLI\_IO\_CONFORMANCE\_OK  
  * CLI\_HYGIENE\_OK → CLI\_IMPLEMENTATION\_HYGIENE\_OK  
  * IFACE\_AGGREGATOR\_P1\_COMPAT\_OK → IFACE\_CONJ\_P1\_COMPAT\_OK  
  * AGGREGATOR\_P1\_COMPAT\_OK → IFACE\_CONJ\_P1\_COMPAT\_OK  
  * IFACE\_P1\_COMPAT\_KEYSET\_OK → (non-token evidence requirement; do not mint as a new token)  
* Compatibility keyset contract posture: keyset-level compatibility is an evidence requirement, not a token. It MUST NOT be minted as a new acceptance token in plan text.  
* Ownership posture. For token-addition ADR stubs and any Tracked Issues created for token drift or token minting, the accountable owner is the PO.

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
* Close report minimum required fields (required):  
  * Canon pointer fields: the close report MUST include explicit canonical path pointers to the plan’s declared close-pack artifacts (at minimum: the close report path itself, the deterministic path-of-record selection, and any declared manifest, acceptance map, and token→evidence matrix paths).

  * TI-002 mapping (when TI-002 is claimed): the close report MUST include an explicit mapping from TI-002 to the satisfying governed artifact(s), including (a) artifact path(s) and (b) a minimal excerpt or other precise locator sufficient to audit the claim without guessing.

  * For any other token claims that require explicit mapping, apply the same mapping rule as TI-002.

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